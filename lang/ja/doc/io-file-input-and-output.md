## File Input and Output

<!-- category: IO -->
<!-- keywords: appendfile -->
<!-- signatures: appendfile(filename) -->
### Function: appendfile (filename)

コンソールの筆記録を*filename*に追加します。
`appendfile`は、
筆記録ファイルが、存在すれば、いつも追加されることを除いて、
`writefile`と同じです。


`closefile`は、`appendfile`や`writefile`によって開かれた筆記録ファイルを閉じます。

See also: `closefile`.

<!-- category: IO -->
<!-- keywords: batch -->
<!-- signatures: batch(filename), batch(filename, option) -->
### Function: batch (filename)

`batch(filename)`はMaximaの式を*filename*から読み込み、評価します。
`batch`は、リスト`file_search_maxima`の中で*filename*を検索します。
`file_search`も参照してください。


`batch(filename, demo)`は、
`demo(filename)`ようなものです。
この場合、`batch`は、リスト`file_search_demo`の中で
*filename*を検索します。
`demo`を参照してください。


`batch(filename, test)`は、
オプション`display_all=true`を付けた`run_testsuite`ようなものです。
この場合、`batch`は、
`run_testsuite`のようにリスト`file_search_tests`ではなく、
リスト`file_search_maxima`の中で*filename*を検索します。
更に、`run_testsuite`はリスト`testsuite_files`の中にあるテストを実行します。
`batch`を使うと、どんなファイルもテストモードで実行することが可能です。
ファイルはリスト`file_search_maxima`の中であってもいいです。
これはテストファイルを書いている時に便利です。


*filename*は、一連のMaximaの式より成り、それぞれの式は、`;`もしくは`$`で終了します。
特殊変数`%`と関数`%th`は、ファイル内での前の結果を参照します。
ファイルは`:lisp`構成子を含むかもしれません。
ファイルの中の空白、タブ、改行は無視されます。
適した入力ファイルは、テキストエディタもしくは、`stringout`関数で作ることができます。


`batch`は、それぞれの入力式を*filename*から読み込み、
入力をコンソールに表示し、
対応する出力式を計算し、
出力式を表示します。
入力ラベルは入力式に割り当てられ、出力ラベルは出力式に割り当てられます。
`batch`は、エラーがない限り、ファイルの中のすべての入力式を評価します。
もしユーザー入力が（例えば、`asksign`や`askinteger`によって）要求されたら、
`batch`は、ポーズして必要な入力を入手し、続けます。




コンソールで`control-C`をタイプすることで、`batch`を停止させることが可能かもしれません。
`control-C`の効果は、基礎となるLispの実装に依存します。


`batch`にはいくつか用法があります。
役立つコマンドラインの蓄積を供給したり、
エラーのないデモンストレーションを与えたり、
複雑な問題を解く時、人の考えを整理するのを助けたり。


`batch`は引数を評価します。
第二引数なしで呼び出されたり、オプション`demo`で呼び出された時、
`batch`は`filename`のパスを文字列として返します。
オプション`test`で呼び出された時、
戻り値は、空のリスト`[]`か、*filename*と失敗したテストの数を含むリストです。


`load`, `batchload`, `demo`も参照してください。

See also: `file_search_maxima`, `file_search`, `file_search_demo`, `demo`, `%`, `%th`, `stringout`, `asksign`, `askinteger`, `load`, `batchload`.

<!-- category: IO -->
<!-- keywords: batchload -->
<!-- signatures: batchload(filename) -->
### Function: batchload (filename)

*filename*からMaximaの式を読み込み、評価します。
入力式や出力式を表示しません。
ラベルを出力式に割り当てません。
しかし、（`print`や`describe`が生成するような)プリント文の出力は表示されます。


特殊変数`%`や関数`%th`は、
ファイルの中の結果ではなく、対話インタープリタからの以前の結果を参照します。
ファイルは`:lisp`構成子を含むことはできません。


`batchload`は、*filename*のパスを文字列として返します。
`batchload`は引数を評価します。


`batch`や`load`も参照してください。

See also: `%`, `%th`, `batch`, `load`.

<!-- category: IO -->
<!-- keywords: closefile -->
<!-- signatures: closefile() -->
### Function: closefile ()

`writefile`や`appendfile`で開いたトランスクリプトファイルを閉じます。

See also: `writefile`, `appendfile`.

<!-- category: IO -->
<!-- keywords: file_output_append -->
<!-- signatures: file_output_append -->
### Variable: file_output_append

デフォルト値: `false`


`file_output_append`は、
ファイル出力関数が出力ファイルに追加するか、ファイルを切り詰めるか決めます。
`file_output_append`が`true`の時、
ファイル出力関数は出力ファイルに追加します。
そうでなければ，出力ファイルは切り詰められます。


`save`, `stringout`, `with_stdout`は、`file_output_append`を考慮します。
出力ファイルを書き出す他の関数は`file_output_append`を考慮しません。
特に、プロット感巣や変換関数は常に出力ファイルを切り詰め、
`tex`や`appendfile`はいつも追加します。

See also: `save`, `stringout`, `with_stdout`, `tex`, `appendfile`.

<!-- category: IO -->
<!-- keywords: file_search -->
<!-- signatures: file_search(filename), file_search(filename, pathlist) -->
### Function: file_search (filename)

`file_search`は、ファイル*filename*を検索し、
もし見つかれば、（文字列として）ファイルへのパスを返します;
そうでなければ、`file_search`は`false`を返します。
`file_search (filename)`は、
デフォルトのサーチディレクトリを検索します。
デフォルトのサーチディレクトリは、`file_search_maxima`,
`file_search_lisp`, `file_search_demo`変数によって指定されます。


`file_search`は、
名前を「ワイルドカード」ファイルサーチパターンにマッチさせようとする前に、
最初に、渡された実際の名前が存在するかチェックします。
ファイルサーチパターンに関連した`file_search_maxima`を参照してください。


引数*filename*は、パスとファイル名、もしくは単にファイル名、もしくは、
もしファイルサーチディレクトリがファイルサーチパターンを含むなら、単にファイル名のベース（拡張子なし）、を取り得ます。
例えば、



```maxima
file_search ("/home/wfs/special/zeta.mac");
file_search ("zeta.mac");
file_search ("zeta");
```


ファイルが存在していて、`/home/wfs/special/###.mac`が`file_search_maxima`に中にあるという仮定の下で、上記すべては同じファイルを見つけます。


`file_search (filename, pathlist)`は、
*pathlist*によって指定されたディレクトリの中だけを検索します。
ここで、*pathlist*は文字列のりすとです。
引数*pathlist*は、デフォルトの検索ディレクトリに取って代わります。
だから、もしパスリストが与えられたら、デフォルトの検索ディレクトリのいずれでもなく、`file_search`は指定されたところだけを検索します。
*pathlist*の中に１つのディレクトリだけしかない場合でさえ、まだ、
それは、要素１つのリストとして与えられなければいけません。


ユーザーはデフォルト検索ディレクトリを修正できます。
`file_search_maxima`を参照してください。


`file_search`は、`file_search_maxima`と`file_search_lisp`を
を検索ディレクトリとして、
`load`によって呼び出されます。

See also: `file_search_maxima`, `file_search_lisp`, `file_search_demo`, `load`.

<!-- category: IO -->
<!-- keywords: file_search_maxima, file_search_lisp, file_search_demo, file_search_usage, file_search_tests -->
<!-- signatures: file_search_lisp, file_search_demo, file_search_usage, file_search_tests -->
### Variable: file_search_maxima

これらの変数は、`load`, `demo`や他のいくつかのMaximaの関数が検索する
ディレクトリのリストを指定します。
これらの変数のデフォルト値は、Maxima員ストレーションの様々なディレクトリを名指ししています。


ユーザーは、
デフォルト値を置き換えるか、ディレクトリを追加することで、
これらの変数を変更できます
例えば、



```maxima
file_search_maxima: ["/usr/local/foo/###.mac",
    "/usr/local/bar/###.mac"]$
```


は、`file_search_maxima`のデフォルト値を置き換える一方、



```maxima
file_search_maxima: append (file_search_maxima,
    ["/usr/local/foo/###.mac", "/usr/local/bar/###.mac"])$
```


は、２つのディレクトリを追加します。
ファイル`maxima-init.mac`に
Maximaが起動した時にファイル検索パスが自動的に割り当てられるような式を入れておくと便利かもしれません。
`Introduction-for-Runtime-Environment`も参照してください。


特別な「ワイルドカード」構造によって、ファイル名の拡張子やパスを多重にしてすることができます。
文字列`###`は、求められている名前に拡張される一方、
カーリ括弧`{foo,bar,baz}`で囲まれた、コンマで分離されたリストは多重文字列に拡張されます。
例えば、求められてる名前が`neumann`とすると、



```maxima
"/home/{wfs,gcj}/###.{lisp,mac}"
```



は、`/home/wfs/neumann.lisp`, `/home/gcj/neumann.lisp`,
`/home/wfs/neumann.mac`, `/home/gcj/neumann.mac`に展開されます。

See also: `load`, `demo`, `Introduction-for-Runtime-Environment`.

<!-- category: IO -->
<!-- keywords: file_type -->
<!-- signatures: file_type(filename) -->
### Function: file_type (filename)

*filename*の中身について、ファイル名拡張子を下に、推測を返します。
*filename*は、実際のファイルを参照する必要はありません;
ファイルを開いたり、中身を探索したりはしません。


戻り値はシンボルであり、`object`, `lisp`, `maxima`のいずれかです。
もし拡張子が`file_type_maxima`の中の値の1つと一致したら、
`file_type`は`maxima`を返します。
もし拡張子が"`file_type_lisp`の中の値の1つと一致したら、
`file_type`は`lisp`を返します。
上のいずれでもないなら、`file_type`は`object`を返します。


`pathname_type`も参照してください。


デフォルト値に関しては、`file_type_maxima`と`file_type_lisp`を
参照してください。


例:







```maxima
(%i2) map('file_type,
          ["test.lisp", "test.mac", "test.dem", "test.txt"]);
(%o2)            [lisp, maxima, maxima, object]
```

See also: `pathname_type`, `file_type_maxima`, `file_type_lisp`.

<!-- category: IO -->
<!-- keywords: file_type_lisp -->
<!-- signatures: file_type_lisp -->
### Variable: file_type_lisp

デフォルト値:  `[l, lsp, lisp]`


`file_type_lisp`は、
maximaがLispソースファイルの印として認識するファイル拡張子のリストです。


`file_type`も参照してください。

See also: `file_type`.

<!-- category: IO -->
<!-- keywords: file_type_maxima -->
<!-- signatures: file_type_maxima -->
### Variable: file_type_maxima

デフォルト値:  `[mac, mc, demo, dem, dm1, dm2, dm3, dmt]`


`file_type_maxima`は、
maximaがMaximaソースファイルの印として認識するファイル拡張子のリストです。


`file_type`も参照してください。

See also: `file_type`.

<!-- category: IO -->
<!-- keywords: filename_merge -->
<!-- signatures: filename_merge(path, filename) -->
### Function: filename_merge (path, filename)

*path*と*filename*から修正されたパスを構成します。
もし、*path*の最後の構成要素が形式`###.something`なら、
構成要素は、`filename.something`に置き換えられます。
そうでなければ、最後の構成要素は単に*filename*に置き換えられます。


結果はLispのパス名オブジェクトです。

<!-- category: IO -->
<!-- keywords: get_tex_environment, set_tex_environment -->
<!-- signatures: get_tex_environment(op), set_tex_environment(op, before, after) -->
### Function: get_tex_environment (op)

`tex`によって出力されるTeX環境をカスタマイズします。
これらの関数によって保持されるように、TeX環境は２つの文字列から成ります;
１つは他の任意のTeX出力に前もって出力されるもの、もう１つは後に出力されるものです。


式のトップレベル演算子のTeX環境だけが、出力されます;
他の演算子に関連づけられたTeX環境は無視されます。


`get_tex_environment`は、
演算子*op*に適用されたTeX環境を返します;
もし他の環境が割り当てられていなければ、デフォルトを返します。


`set_tex_environment`は、
演算子*op*のためのTeX環境を割り当てます。


例:









```maxima
(%i1) get_tex_environment (":=");
(%o1) [
\begin{verbatim}
, ;
\end{verbatim}
]
(%i2) tex (f (x) := 1 - x);

\begin{verbatim}
f(x):=1-x;
\end{verbatim}

(%o2)                         false
(%i3) set_tex_environment (":=", "$$", "$$");
(%o3)                       [$$, $$]
(%i4) tex (f (x) := 1 - x);
$$f(x):=1-x$$
(%o4)                         false
```

<!-- category: IO -->
<!-- keywords: get_tex_environment_default, set_tex_environment_default -->
<!-- signatures: get_tex_environment_default(), set_tex_environment_default(before, after) -->
### Function: get_tex_environment_default ()

`tex`によって出力されるTeX環境をカスタマイズします。
これらの関数によって保持されるように、TeX環境は２つの文字列から成ります;
１つは他の任意のTeX出力に前もって出力されるもの、もう１つは後に出力されるものです。


`get_tex_environment_default`は、
トップレベル演算子が（`set_tex_environment`で割り当てられたような）特定のTeX環境を持たない式に適用されたTeX環境を返します。


`set_tex_environment_default`は、デフォルトのTeX環境を割り当てます。


例:











```maxima
(%i1) get_tex_environment_default ();
(%o1)                       [$$, $$]
(%i2) tex (f(x) + g(x));
$$g\left(x\right)+f\left(x\right)$$
(%o2)                         false
(%i3) set_tex_environment_default ("\\begin{equation}
", "
\\end{equation}");
(%o3) [\begin{equation}
, 
\end{equation}]
(%i4) tex (f(x) + g(x));
\begin{equation}
g\left(x\right)+f\left(x\right)
\end{equation}
(%o4)                         false
```

<!-- category: IO -->
<!-- keywords: load -->
<!-- signatures: load(filename) -->
### Function: load (filename)

*filename*の中の式を評価します。
そして、変数、関数、他のオブジェクトをMaximaにもたらします。
、*filename*から再生されたバインドは存在するオブジェクトのバインドを上書きします(clobber)。
ファイルを見つけるために、
`load`は、探索ディレクトリとして`file_search_maxima`と`file_search_lisp`を引数として`file_search`をコールします。
もし`load`が成功したら
ファイルの名前を返します。
そうでなければ、`load`はエラーメッセージを出力します。


`load`は、LispコードでもMaximaコードでも等しく機能します。
`save`, `translate_file`, `compile_file`―これらはLispコードを生成します―が生成したファイルはすべて`load`によって処理できます。
`load`は、Lispファイルをロードするために`loadfile`をコールし、
Maximaファイルをロードするために`batchload`をコールします。


`load`は、Maximaファイルの中で`:lisp`構成子を認識しません。
*filename*を処理する時、
グローバル変数`_`, `__`, `%`, `%th`は、
`load`がコールされた時バインドされていた値を持ちます。


`loadfile`, `batch`, `batchload`, `demo`も参照してください。
`loadfile`はLispファイルを処理します;
`batch`, `batchload`, `demo`はMaximaファイルを処理します。


ファイル探索メカニズムについてもっと詳しいことは`file_search`を参照してください。


`load`は引数を評価します。

See also: `save`, `translate_file`, `compile_file`, `batchload`, `loadfile`, `batch`, `demo`, `file_search`.

<!-- category: IO -->
<!-- keywords: load_pathname -->
<!-- signatures: load_pathname -->
### Variable: load_pathname

デフォルト値: `false`


関数`load`や、`loadfile`、`batchload`を使ってファイルがロードされる時、
システム変数`load_pathname`は処理するファイルのパス名を示します。


変数`load_pathname`はロード中にファイルからアクセスすることができます。


例:


ディレクトリ


`"/home/dieter/workspace/mymaxima/temp/"`に、以下のコマンドを含む


バッチファイル`test.mac`があるとしましょう。



```maxima
print("The value of load_pathname is: ", load_pathname)$
print("End of batchfile")$
```


すると、以下の出力を得ます。



```maxima
(%i1) load("/home/dieter/workspace/mymaxima/temp/test.mac")$
The value of load_pathname is:  
                   /home/dieter/workspace/mymaxima/temp/test.mac 
End of batchfile
```

See also: `load`, `loadfile`, `batchload`.

<!-- category: IO -->
<!-- keywords: loadfile -->
<!-- signatures: loadfile(filename) -->
### Function: loadfile (filename)

*filename*の中のLisp式を評価します。
`loadfile`は、`file_search`を呼び出しません。
だから、`filename`はファイル拡張子とファイルを見つけるのに必要なパスも含まなければいけません。


`loadfile`は、`save`, `translate_file`, `compile_file`によって生成されたファイルを処理できます。
ユーザーは、`loadfile`の代わりに`load`を使うほうが便利だと気づくでしょう。

See also: `save`, `translate_file`, `compile_file`, `load`.

<!-- category: IO -->
<!-- keywords: loadprint -->
<!-- signatures: loadprint -->
### Variable: loadprint

デフォルト値: `true`


`loadprint`は、ファイルがロードされた時、メッセージを表示するかどうか告げます。



- *
`loadprint`が`true`の時, いつもメッセージを表示します。
- *
`loadprint`が`'loadfile`の時, ファイルが関数`loadfile`によってロードされた時だけメッセージを表示します。
- *
`loadprint`が`'autoload`の時、
ファイルが自動的にロードされた時だけメッセージを表示します。
`setup_autoload`を参照してください。
- *
`loadprint`が`false`の時, メッセージは決して表示されません。

See also: `setup_autoload`.

<!-- category: IO -->
<!-- keywords: packagefile -->
<!-- signatures: packagefile -->
### Variable: packagefile

デフォルト値: `false`


他の人が使うパッケージ（ファイル）を生成するために`save`や`translate`を使う
パッケージデザイナは、
ファイルがロードされる時必要な場合を除いて、
Maximaの情報リスト（例えば、`values`, `functions`）に情報が追加されることを抑制するために、`packagefile: true`を設定したいかもしれません。
この方法によれば、
ユーザーが自身のデータを追加した時ユーザーの方法では
パッケージの中身は、得られないでしょう。
これは、起こりうる名前衝突の問題を解決はしないことに注意してください。
このフラグは、パッケージファイルへの出力であるものに素直に影響することにも注意してください。
フラグを`true`に設定することは、
Maxima初期化ファイルを生成するにも役に立ちます。

See also: `save`, `translate`, `values`, `functions`.

<!-- category: IO -->
<!-- keywords: pathname_directory, pathname_name, pathname_type -->
<!-- signatures: pathname_directory(pathname), pathname_name(pathname), pathname_type(pathname) -->
### Function: pathname_directory (pathname)

これらの関数は*pathname*の構成要素を返します。


例:








```maxima
(%i1) pathname_directory("/home/dieter/maxima/changelog.txt");
(%o1)                 /home/dieter/maxima/
(%i2) pathname_name("/home/dieter/maxima/changelog.txt");
(%o2)                       changelog
(%i3) pathname_type("/home/dieter/maxima/changelog.txt");
(%o3)                          txt
```

<!-- category: IO -->
<!-- keywords: printfile -->
<!-- signatures: printfile(path) -->
### Function: printfile (path)

*path*という名前のファイルをコンソールに表示します。
*path*は、文字列もしくはシンボルです;
もしシンボルなら、文字列に変換されます。


もし*path*が現在のワーキングディレクトリからアクセス可能なファイル名なら、
そのファイルがコンソールに表示されます。
そうでなければ、
`printfile`は、
`filename_merge`を介して`file_search_usage`の要素のそれぞれに
*path*を追加することでファイルを見つけようとします。


`printfile`は、もし*path*が存在しているファイルを示しているなら、
*path*を返し、そうでなければ、
成功したファイル名マージの結果を返します。

See also: `filename_merge`, `file_search_usage`.

<!-- category: IO -->
<!-- keywords: save -->
<!-- signatures: save(filename, name_1, name_2, name_3, ...), save(filename, values, functions, labels, ...), save(filename, [m, n]), save(filename, name_1=expr_1, ...), save(filename, all), save(filename, name_1=expr_1, name_2=expr_2, ...) -->
### Function: save (filename, name_1, name_2, name_3, ...)

*filename*に、*name_1*, *name_2*, *name_3*, ...,の現在値を
保存します。
引数は、変数、関数、他のオブジェクトの名前です。
もし名前が関連づけられた値や関数を持たないなら、無視されます。
`save`は、*filename*を返します。


`save`は、データをLisp式の形式で保存します。
`save`で保存されたデータは、`load (filename)`によって回復できます。
`load`を参照してください。


グローバルフラグ `file_output_append`は、
`save`が出力ファイルに追加するか、切り詰めるか決めます。
`file_output_append`が`true`の時、
`save`は出力ファイルに追加します。
そうでなければ、`save`は出力ファイルを切り詰めます。
どちらの場合も、もしファイルが存在しなければ、`save`はファイルを生成します。


特殊形式`save (filename, values, functions, labels, ...)`
は、`values`, `functions`, `labels`, などと名付けられた項目を
保存します。
名前は、変数`infolists`によって指定された任意のものです。
`values`は、ユーザー定義変数すべてから成ります。


特殊形式`save (filename, [m, n])`は、
*m*から*n*までの入力ラベル、出力ラベルの値を保存します。
*m*と*n*は、整数リテラルでなければならないことに注意してください。
例えば、`save ("foo.1", %i42, %o42)`のように、
入力ラベル、出力ラベルは１つ１つ保存することもできます。
`save (filename, labels)`は、
入力ラベル出力ラベルすべてを保存します。
保存されたラベルが回復された時、それらは存在していたラベルを負かします。


特殊形式`save (filename, name_1=expr_1, name_2=expr_2, ...)`は、
*expr_1*, *expr_2*, ...,の値を*name_1*, *name_2*, ...という名前で保存します。
例えば、`save ("foo.1", aa=%o88)`のように、
この形式を入力ラベル出力ラベルに適用することは便利です。
この形式の等式の右辺は任意の式であり、その式は評価されます。
この形式は、新しい名前を現在のMaximaの環境に導入はせず、
ただ、*filename*にそれらを保存します。


これらの特殊形式と`save`の一般形式は自由に混在させることができます。
例えば、`save (filename, aa, bb, cc=42, functions, [11, 17])`。


特殊形式`save (filename, all)`は、Maximaの現在の状態を保存します。
これは、自動的に定義された項目はもちろん、ユーザー定義の変数、関数、配列などすべてを
含みます。
保存される項目は、
もしそれらがユーザーによって新しい値を割り当てられたなら、
`file_search_maxima`や`showtime`のようなシステム変数を含みます。
`myoptions`を参照してください。


`save`は*filename*を評価し、他の引数すべてをクォートします。

See also: `load`, `file_output_append`, `values`, `functions`, `labels`, `infolists`, `file_search_maxima`, `showtime`, `myoptions`.

<!-- category: IO -->
<!-- keywords: stringout -->
<!-- signatures: stringout(filename, expr_1, expr_2, expr_3, ...), stringout(filename, [m, n]), stringout(filename, input), stringout(filename, functions), stringout(filename, values) -->
### Function: stringout (filename, expr_1, expr_2, expr_3, ...)

`stringout`は、
式が入力としてタイプされたのと同じ形式で、式をファイルに書き込みます。
なので、ファイルは`batch`や`demo`コマンドの入力として使えますし、
どんな目的のためでも編集できます。
`stringout`は、`writefile`が進行中の間に実行することができます。


グローバルフラグ`file_output_append`は、
`stringout`が出力ファイルに追加するか、切り詰めるか決めます。
`file_output_append`が`true`の時、
`stringout`は、出力ファイルに追加します。
そうでなければ、`stringout`は出力ファイルを切り詰めます。
どちらの場合も、もしファイルが存在しなければ，`stringout`はファイルを生成します。


`stringout`の一般形式は、１つ以上の式の値を出力ファイルに書き込みます。
もし式が変数なら、変数の値だけが書き込まれ、変数名は書き込まれないことに注意してください。
役に立つ特殊な場合として、式は、
入力ラベル(`%i1`, `%i2`, `%i3`, ...)もしくは出力ラベル(`%o1`, `%o2`, `%o3`, ...)でもよいです。
）


もし`grind`が`true`なら、
`stringout`は、`grind`フォーマットを使って出力をフォーマットします。
そうでなければ、`string`フォーマットが使われます。
`grind`と`string`を参照してください。


特殊形式`stringout (filename, [m, n])`は、
mからnまでの入力ラベルの値を書き込みます。


特殊形式 `stringout (filename, input)`は、
入力ラベルすべてをファイルに書き込みます。


特殊形式`stringout (filename, functions)`は、
（グローバルリスト`functions`で名付けられた）ユーザー定義関数すべてをファイルに書き込みます。


特殊形式`stringout (filename, values)`は、
（グローバルリスト`values`で名付けられた）ユーザーが割り当てた変数すべてをファイルに書き込みます。
変数それぞれは、変数名とコロンとその値という割り当て文として出力されます。
`stringout`の一般形式は変数を割り当て文として出力しないことに注意してください。

See also: `batch`, `demo`, `writefile`, `file_output_append`, `grind`, `functions`, `values`.

<!-- category: IO -->
<!-- keywords: tcl_output -->
<!-- signatures: tcl_output(list, i0, skip), tcl_output(list, i0), tcl_output([list_1, ..., list_n], i) -->
### Function: tcl_output (list, i0, skip)

リストの要素を、
カーリ括弧`{ }`で囲んで表示します。
Tcl/Tk言語でプログラムの一部として適した形です。


`tcl_output (list, i0, skip)`
は、
要素*i0*で始まり、要素`i0 + skip`, `i0 + 2 skip`, などを表示するよう、*list*を表示します。


`tcl_output (list, i0)`は、
`tcl_output (list, i0, 2)`と同値です。


`tcl_output ([list_1, ..., list_n], i)`は、
*list_1*, ..., *list_n*の*i*番目の要素を表示します。


例:













```maxima
(%i1) tcl_output ([1, 2, 3, 4, 5, 6], 1, 3)$

 {1.000000000     4.000000000     
 }
(%i2) tcl_output ([1, 2, 3, 4, 5, 6], 2, 3)$

 {2.000000000     5.000000000     
 }
(%i3) tcl_output ([3/7, 5/9, 11/13, 13/17], 1)$

 {((RAT SIMP) 3 7) ((RAT SIMP) 11 13) 
 }
(%i4) tcl_output ([x1, y1, x2, y2, x3, y3], 2)$

 {$Y1 $Y2 $Y3 
 }
(%i5) tcl_output ([[1, 2, 3], [11, 22, 33]], 1)$

 {SIMP 1.000000000     11.00000000     
 }
```

<!-- category: IO -->
<!-- keywords: tex -->
<!-- signatures: tex(expr), tex(expr, destination), tex(expr, false), tex(label), tex(label, destination), tex(label, false) -->
### Function: tex (expr)

TeXドキュメントの準備に適した式の表現を出力します。
結果は、ドキュメントの断片です。
それは、より大きなドキュメントにコピーすることができますが、それ自身では処理されません。


`tex (expr)`は、*expr*のTeX表現をコンソールに出力します。


`tex (label)`は、*label*で名付けられた式のTeX表現を出力し、
（式の左に表示されるよう）等式ラベルをそれに割り当てます。
TeX等式ラベルは、Maximaラベルと同じです。


*destination*は、出力ストリームもしくはファイル名です。
*destination*がファイル名の時、
`tex`は、ファイルに出力を追加します。
関数`openw`と`opena`は、出力ストリームを生成します。


`tex (expr, false)`と`tex (label, false)`は、
TeX出力を文字列として返します。


`tex`は、最初の引数がラベルかどうか見るためにテストした後、最初の引数を評価します。
クォートクォート`''`は、引数の評価を強制し、
その結果、テストをだめにして、ラベルを妨げます。


`texput`も参照してください。


例:



```maxima
(%i1) integrate (1/(1+x^3), x);
                                    2 x - 1
                  2            atan(-------)
             log(x  - x + 1)        sqrt(3)    log(x + 1)
(%o1)      - --------------- + ------------- + ----------
                    6             sqrt(3)          3
(%i2) tex (%o1);
$$-{{\log \left(x^2-x+1\right)}\over{6}}+{{\arctan \left({{2\,x-1
 }\over{\sqrt{3}}}\right)}\over{\sqrt{3}}}+{{\log \left(x+1\right)
 }\over{3}}\leqno{\tt (\%o1)}$$
(%o2)                          (\%o1)
(%i3) tex (integrate (sin(x), x));
$$-\cos x$$
(%o3)                           false
(%i4) tex (%o1, "foo.tex");
(%o4)                          (\%o1)
```


`tex (expr, false)`はTeX出力を文字列として返します。







```maxima
(%i1) S : tex (x * y * z, false);
(%o1) $$x\,y\,z$$
(%i2) S;
(%o2) $$x\,y\,z$$
```

See also: `texput`.

<!-- category: IO -->
<!-- keywords: tex1 -->
<!-- signatures: tex1(e) -->
### Function: tex1 (e)

式*e*のTeX出力を表現する文字列を返します。
TeX出力は、等式や他の任意の環境のため、区切り記号で囲まれません。


例:






```maxima
(%i1) tex1 (sin(x) + cos(x));
(%o1)                     \sin x+\cos x
```

<!-- category: IO -->
<!-- keywords: texput -->
<!-- signatures: texput(a, s), texput(a, f), texput(a, s, operator_type), texput(a, [s_1, s_2], matchfix), texput(a, [s_1, s_2, s_3], matchfix) -->
### Function: texput (a, s)

アトム*a*のためのTeX出力を割り当てます。
ここで*a*はシンボルもしくは演算子名です。


`texput (a, s)`は、
`tex`関数に、
*a*の代わりに文字列*s*をTeX出力に入れるようにさせます。


`texput (a, f)`は、
`tex`関数に、
TeX出力を生成するために関数*f*をコールさせます。
*f*は、１つの引数を受け入れなければいけません。
ここで、引数は、演算子*a*を持つ式で、文字列（TeX出力）を返さなければいけません。
*f*は、入力式の引数のためにTeX出力を生成するよう、`tex1`をコールするかもしれません。


*operator_type*が`prefix`, `infix`, `postfix`, `nary`, もしくは `nofix`,として、
`texput (a, s, operator_type)`は、
`tex`関数に
*a*の代わりに*s*をTeX出力に入れるようにさせ、
適切な位置に挿入された手キスを置くようにさせます。


`texput (a, [s_1, s_2], matchfix)`は、
`tex`関数に、
*a*の引数のそれぞれの側に*s_1*と*s_2*を
TeX出力に入れるようにさせます。
（もし複数なら）引数はコンマで分離されます。


`texput (a, [s_1, s_2, s_3], matchfix)`は、
`tex`関数に、
引数を分離する*s_3*と一緒に
*a*の引数のそれぞれの側に*s_1*と*s_2*をTeX出力に入れるようにさせます。


例:


変数にTeX出力を割り当てます。







```maxima
(%i1) texput (me,"\\mu_e");
(%o1)                         \mu_e
(%i2) tex (me);
$$\mu_e$$
(%o2)                         false
```


任意の関数（演算子ではない）にTeX出力を割り当てます。







```maxima
(%i1) texput (lcm, "\\mathrm{lcm}");
(%o1)                     \mathrm{lcm}
(%i2) tex (lcm (a, b));
$$\mathrm{lcm}\left(a , b\right)$$
(%o2)                         false
```


TeX出力を生成する関数をコールします。









```maxima
(%i1) texfoo (e) := block ([a, b], [a, b] : args (e),
  concat ("\\left[\\stackrel{",tex1(b),"}{",tex1(a),"}\\right]"))$
(%i2) texput (foo, texfoo);
(%o2)                        texfoo
(%i3) tex (foo (2^x, %pi));
$$\left[\stackrel{\pi}{2^{x}}\right]$$
(%o3)                         false
```


前置演算子にTeX出力を割り当てます。








```maxima
(%i1) prefix ("grad");
(%o1)                         grad
(%i2) texput ("grad", " \\nabla ", prefix);
(%o2)                        \nabla 
(%i3) tex (grad f);
$$ \nabla f$$
(%o3)                         false
```


中置演算子にTeX出力を割り当てます。








```maxima
(%i1) infix ("~");
(%o1)                           ~
(%i2) texput ("~", " \\times ", infix);
(%o2)                        \times 
(%i3) tex (a ~ b);
$$a \times b$$
(%o3)                         false
```


後置演算子にTeX出力を割り当てます。








```maxima
(%i1) postfix ("##");
(%o1)                          ##
(%i2) texput ("##", "!!", postfix);
(%o2)                          !!
(%i3) tex (x ##);
$$x!!$$
(%o3)                         false
```


n項演算子にTeX出力を割り当てます。








```maxima
(%i1) nary ("@@");
(%o1)                          @@
(%i2) texput ("@@", " \\circ ", nary);
(%o2)                         \circ 
(%i3) tex (a @@ b @@ c @@ d);
$$a \circ b \circ c \circ d$$
(%o3)                         false
```


無項演算子にTeX出力を割り当てます。








```maxima
(%i1) nofix ("foo");
(%o1)                          foo
(%i2) texput ("foo", "\\mathsc{foo}", nofix);
(%o2)                     \mathsc{foo}
(%i3) tex (foo);
$$\mathsc{foo}$$
(%o3)                         false
```


マッチフィックス演算子にTeX出力を割り当てます。













```maxima
(%i1) matchfix ("<<", ">>");
(%o1)                          <<
(%i2) texput ("<<", [" \\langle ", " \\rangle "], matchfix);
(%o2)                [ \langle ,  \rangle ]
(%i3) tex (<<a>>);
$$ \langle a \rangle $$
(%o3)                         false
(%i4) tex (<<a, b>>);
$$ \langle a , b \rangle $$
(%o4)                         false
(%i5) texput ("<<", [" \\langle ", " \\rangle ", " \\, | \\,"],
      matchfix);
(%o5)           [ \langle ,  \rangle ,  \, | \,]
(%i6) tex (<<a>>);
$$ \langle a \rangle $$
(%o6)                         false
(%i7) tex (<<a, b>>);
$$ \langle a \, | \,b \rangle $$
(%o7)                         false
```

<!-- category: IO -->
<!-- keywords: with_stdout -->
<!-- signatures: with_stdout(f, expr_1, expr_2, expr_3, ...), with_stdout(s, expr_1, expr_2, expr_3, ...) -->
### Function: with_stdout (f, expr_1, expr_2, expr_3, ...)

*expr_1*, *expr_2*, *expr_3*, ...を評価し、
生成された出力すべてをファイル*f*もしくは出力ストリーム*s*に書き込みます。
評価される式は出力に書き込まれません。
出力は、`print`, `display`, `grind`や他の関数によって生成されたものです。


グローバルフラグ `file_output_append`は、
`with_stdout`が出力ファイル*f*に追加するか切り詰めるか決めます。
`file_output_append`が`true`の時、
`with_stdout`は出力ファイルに追加します。
そうでなければ、`with_stdout`は出力ファイルを切り詰めます。
どちらの場合も、もしファイルが存在しないなら、`with_stdout`はファイルを生成します。


`with_stdout`は最後の引数の値を返します。


`writefile`も参照してください。








```maxima
(%i1) with_stdout ("tmp.out", for i:5 thru 10 do
      print (i, "! yields", i!))$
(%i2) printfile ("tmp.out")$
5 ! yields 120 
6 ! yields 720 
7 ! yields 5040 
8 ! yields 40320 
9 ! yields 362880 
10 ! yields 3628800
```

See also: `print`, `display`, `grind`, `file_output_append`, `writefile`.

<!-- category: IO -->
<!-- keywords: writefile -->
<!-- signatures: writefile(filename) -->
### Function: writefile (filename)

Maximaセッションのトランスクリプトを*filename*に書き込むことを開始します。
ユーザーとMaximaの間の対話すべてが、ちょうどコンソールに現れるように、このファイルに記録されます。



トランスクリプトがコンソール出力フォーマットで出力されるので、
それはMaximaに再ロードすることはできません。
最ロード可能な式を含むファイルを作るには、
`save`と`stringout`を参照してください。
`save`は、Lisp形式の式を保存する一方、`stringout`は、Maxima形式
の式を保存します。


*filename*が既に存在している時、`writefile`の実行の効果は、
基礎となるLisp実装に依存します;
トランスクリプファイルは負かされるかもしれませんし、ファイルは追加されるかもしれません。
`appendfile`は、いつもトランスクリプトファイルに追加します。


以前の対話の表示を保存するために`writefile`の後、
`playback`を実行するのが便利かもしれません。
`playback`は入力と出力変数(`%i1`, `%o1`, など)だけを表示し、
（戻り値と対照的に）関数の中のプリント文によって生成された任意の出力は`playback`によって表示されません。


`closefile`は、`writefile`や`appendfile`が開いたトランスクリプトファイルを閉じます。

See also: `save`, `stringout`, `appendfile`, `playback`, `closefile`.

