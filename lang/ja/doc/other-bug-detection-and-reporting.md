## Bug Detection and Reporting

<!-- category: Other -->
<!-- keywords: bug_report -->
<!-- signatures: bug_report() -->
### Function: bug_report ()

MaximaとLispのバージョン番号を表示し、Maximaプロジェクトのバグレポートウェブサイトへのリンクを与えます。
バージョン情報は`build_info`がレポートするものと同じです。


バグをレポートする時、
MaximaとLispのバージョン情報をバグレポートにコピーしてもらえると助かります。


`bug_report`は空の文字列 `""`を返します。

See also: `build_info`.

<!-- category: Other -->
<!-- keywords: build_info -->
<!-- signatures: build_info() -->
### Function: build_info ()

Maximaビルドのパラメータのまとめを表示します。


`build_info`は空の文字列 `""`を返します。
`bug_report`.も参照してください。

See also: `bug_report`.

<!-- category: Other -->
<!-- keywords: run_testsuite -->
<!-- signatures: run_testsuite([options]) -->
### Function: run_testsuite ([options])

Maximaのテストスイートを走らせます。
望みの答えを生成したテストは「パス」とみなされます。
望みの答えを生成しないテストも同様ですが、既知のバグとしてマークされています。


`run_testsuite`は、以下のオプションキーワード引数を取ります。



**display_all** — テストすべてを表示します。
通常は、テストが失敗しない限りテストを表示しません。
（デフォルトでは `false`に設定されます。）
**display_known_bugs** — 既知のバグとしてマークされているテストを表示します。
（デフォルトでは `false`に設定されます。）
**tests** — これは、実行するテストのリストです。
それぞれのテストは文字列かシンボルで指定することができます。
デフォルトではテストすべてを実行します。
テストの完全な組は `testsuite_files`で指定されています。
**time** — 時間情報を表示します。
もし `true`ならそれぞれのテストファイルにかかった時間を表示します。
もし `all`なら `display_all`が `true`の時、
それぞれ個々のテストにかかった時間を示します。
デフォルトは`false`で、時間情報を示しません。


例えば、 `run_testsuite(display_known_bugs = true, tests=[rtest5])`は、
テスト `rtest5`だけを走らせ、既知のバグとしてマークされているテストを表示します。


`run_testsuite(display_all = true, tests=["rtest1", rtest1a])`は、
テスト `rtest1`と `rtest2`を走らせ、
テストそれぞれを表示します。


`run_testsuite`は、Maxima環境を変更します。
通常は、テストスクリプトは
既知の環境（すなわちユーザー定義の関数や変数のない環境）を確立するために
`kill`を実行し、
それからテストにふさわしい関数や変数を定義します。


`run_testsuite`は `done`を返します。

See also: `testsuite_files`, `kill`.

<!-- category: Other -->
<!-- keywords: testsuite_files -->
<!-- signatures: testsuite_files -->
### Variable: testsuite_files

`testsuite_files`は `run_testsuite`が実行するテスト一式です。
それは実行するテストを含むファイル名のリストです。
もしファイルの中のテストのいくつかが失敗することが既知なら、
ファイル名をリストする代わりに、
ファイル名と失敗するテスト番号を含むリストを使います。


例えば、以下はデフォルトのテスト一式の一部です:



```maxima
["rtest13s", ["rtest14", 57, 63]]
```


これは、ファイル"rtest13s", "rtest14"から成るテストスイートを指定しますが、
"rtest14" は失敗することが既知の２つのテスト57と63を含みます。

See also: `run_testsuite`.

