# maxima-core-docs

[![Docs](https://img.shields.io/badge/docs-online-blue)](https://cmsd2.github.io/maxima-core-docs/)

Reference documentation for Maxima's built-in functions and variables, packaged as an [mxpm](https://github.com/cmsd2/maxima-mxpm) documentation package.

Generated from the official Maxima Texinfo source using `mxpm doc generate-core-docs`.

## Other languages

`lang/` holds the same documentation from Maxima's translated manuals, one
package per language:

| Package | Language | Symbols documented |
|---|---|---|
| `maxima-core-docs-es` | Spanish | 85% |
| `maxima-core-docs-de` | German | 84% |
| `maxima-core-docs-ja` | Japanese | 82% |
| `maxima-core-docs-pt-br` | Brazilian Portuguese | 64% |
| `maxima-core-docs-pt` | Portuguese | 59% |

Install one beside `maxima-core-docs`, for example
`mxpm install maxima-core-docs-es`. Aximar, the language server and MCP then
show that language where it has a translation, and English elsewhere. Maxima's
own `describe` stays English.

A language gets a pack when its manual documents at least half the English
manual's symbols. To rebuild them from a Maxima source tree, with mxpm 0.9.1 or
later:

```
scripts/language-packs.py generate /path/to/maxima
```

It prints each language's coverage and replaces `lang/`. Russian's manual
documents 48% of the symbols, so it has no pack yet.
CI rebuilds each pack's doc index on every push and fails if one falls below
the threshold (`scripts/language-packs.py rebuild`, then `report`).
