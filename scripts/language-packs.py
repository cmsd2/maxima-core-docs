#!/usr/bin/env python3
"""Language packs: maxima-core-docs in the languages of Maxima's manual.

Each pack is a package of its own in lang/<tag>/, such as lang/es/ for
maxima-core-docs-es, built by `mxpm doc generate-core-docs --lang <tag>` from
Maxima's translated manual in doc/info/<dir>/. A language gets a pack when its
manual documents at least half the symbols the English manual does.

    language-packs.py generate MAXIMA_SRC   rebuild every pack from a Maxima tree
    language-packs.py rebuild               rebuild each pack's doc indexes in place
    language-packs.py report                print each pack's coverage; fail if
                                            one has fallen below the threshold

The packs hold the translated markdown and its doc indexes. They hold no
figures (Aximar has its own) and no .info files, since Maxima's own help
reads the English ones.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "lang"
ENGLISH_INDEX = ROOT / "doc" / "maxima-core-docs-doc-index.json"
THRESHOLD = 0.5
REPOSITORY = "https://github.com/cmsd2/maxima-core-docs"


def tag_for(directory: str) -> str:
    """The BCP 47 tag for a directory of Maxima's manual: pt_BR is pt-BR"""
    return directory.replace("_", "-")


def symbols(index: Path) -> set:
    return set(json.loads(index.read_text())["symbols"])


def coverage(translated: set, english: set) -> float:
    """The share of the English manual's symbols the translation documents"""
    return len(translated & english) / len(english)


def build(maxima_src: Path, tag: str, out: Path) -> str | None:
    """Build one pack into `out`; None on success, else mxpm's last error line"""
    result = subprocess.run(
        ["mxpm", "doc", "generate-core-docs", "--lang", tag,
         "--maxima-src", str(maxima_src), "--output", str(out)],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        return None
    lines = [l for l in result.stderr.splitlines() if l.strip()]
    return next((l for l in lines if "texi:" in l), lines[-1] if lines else "failed")


def rebuild(pack: Path) -> None:
    """Rebuild a pack's doc indexes in place, as CI does after an mxpm release"""
    tag = pack.name
    subprocess.run(
        ["mxpm", "doc", "build", "--lang", tag,
         "--slim", f"doc/maxima-core-docs-slim-doc-index.{tag}.json"],
        cwd=pack, check=True, capture_output=True,
    )


def install(built: Path, pack: Path) -> None:
    """Replace `pack` with the built package, less figures, plus the repository,
    with its indexes built in place"""
    if pack.exists():
        shutil.rmtree(pack)
    shutil.copytree(built, pack, ignore=shutil.ignore_patterns("figures"))
    manifest = pack / "manifest.toml"
    text = manifest.read_text()
    if "repository =" not in text:
        text = text.replace('\nentry = ', f'\nrepository = "{REPOSITORY}"\nentry = ', 1)
    manifest.write_text(text)
    rebuild(pack)


def generate(maxima_src: Path) -> int:
    english = symbols(ENGLISH_INDEX)
    info = maxima_src / "doc" / "info"
    manuals = sorted(d.name for d in info.iterdir() if (d / "maxima.texi").exists())
    print(f"English: {len(english)} symbols. A pack needs {THRESHOLD:.0%} of them.\n")
    print(f"{'language':10} {'symbols':>8} {'coverage':>9}  pack")
    with tempfile.TemporaryDirectory() as work:
        for directory in manuals:
            tag = tag_for(directory)
            pack = PACKS / tag
            out = Path(work) / tag
            error = build(maxima_src, tag, out)
            if error:
                print(f"{tag:10} {'':>8} {'':>9}  not built: {error}")
                continue
            index = out / "doc" / f"maxima-core-docs-doc-index.{tag}.json"
            found = symbols(index)
            share = coverage(found, english)
            if share >= THRESHOLD:
                install(out, pack)
                verdict = f"lang/{tag}"
            else:
                if pack.exists():
                    shutil.rmtree(pack)
                verdict = "below the threshold"
            print(f"{tag:10} {len(found & english):>8} {share:>9.1%}  {verdict}")
    return 0


def report() -> int:
    english = symbols(ENGLISH_INDEX)
    failed = False
    for pack in sorted(p for p in PACKS.iterdir() if p.is_dir()):
        tag = pack.name
        index = pack / "doc" / f"maxima-core-docs-doc-index.{tag}.json"
        share = coverage(symbols(index), english)
        low = share < THRESHOLD
        failed |= low
        print(f"maxima-core-docs-{tag.lower()}: {share:.1%} of the English symbols"
              + (" (below the threshold)" if low else ""))
    return 1 if failed else 0


def main(args: list) -> int:
    match args:
        case ["generate", maxima_src]:
            return generate(Path(maxima_src).resolve())
        case ["rebuild"]:
            for pack in sorted(p for p in PACKS.iterdir() if p.is_dir()):
                rebuild(pack)
                print(f"Rebuilt lang/{pack.name}")
            return 0
        case ["report"]:
            return report()
        case _:
            print(__doc__.strip(), file=sys.stderr)
            return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
