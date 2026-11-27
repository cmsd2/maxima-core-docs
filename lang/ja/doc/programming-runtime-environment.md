## Runtime Environment

<!-- category: Programming -->
<!-- keywords: absolute_real_time -->
<!-- signatures: absolute_real_time() -->
### Function: absolute_real_time ()

協定世界時で1900年1月1日の深夜以来の
秒数を返します。
戻り値は整数です。


`elapsed_real_time`と`elapsed_run_time`も参照してください。


例:







```maxima
(%i1) absolute_real_time ();
(%o1)                      3385045277
(%i2) 1900 + absolute_real_time () / (365.25 * 24 * 3600);
(%o2)                   2007.265612087104
```

<!-- category: Programming -->
<!-- keywords: elapsed_real_time -->
<!-- signatures: elapsed_real_time() -->
### Function: elapsed_real_time ()

Maximaがもっとも最近スタートしたか再スタートして以来の
(1秒の小数を含む)秒数を返します。
戻り値は浮動小数点数です。


`absolute_real_time`と`elapsed_run_time`も参照してください。


例:








```maxima
(%i1) elapsed_real_time ();
(%o1)                       2.559324
(%i2) expand ((a + b)^500)$
(%i3) elapsed_real_time ();
(%o3)                       7.552087
```

<!-- category: Programming -->
<!-- keywords: elapsed_run_time -->
<!-- signatures: elapsed_run_time() -->
### Function: elapsed_run_time ()

Maximaがもっとも最近スタートしたか再スタートして以来
Maximaが計算に費やした
(1秒の小数を含む)秒数の概算を返します。
戻り値は浮動小数点数です。


`absolute_real_time`と`elapsed_real_time`も参照してください。


例:








```maxima
(%i1) elapsed_run_time ();
(%o1)                         0.04
(%i2) expand ((a + b)^500)$
(%i3) elapsed_run_time ();
(%o3)                         1.26
```

<!-- category: Programming -->
<!-- keywords: feature -->
<!-- signatures: feature -->
### Variable: feature

Maximaは、システムフィーチャと数学式に適用されるフィーチャの、
２つの異なるタイプのフィーチャを理解します。
See also 
システムフィーチャについての情報に関しては、`status`も参照してください。
数学的フィーチャについての情報に関しては、
`features`と`featurep`も参照してください。




`feature`それ自身は、関数名でも変数名でもありません。

<!-- category: Programming -->
<!-- keywords: featurep -->
<!-- signatures: featurep(a, f) -->
### Function: featurep (a, f)

現在のデータベースの中の事実に基づいて
オブジェクト*a*が
フィーチャ*f*を持つかどうか
を決定しようとします。
もしそうなら、`true`を返し、そうでなければ`false`を返します。


`featurep`は、
*f*も*f*の否定も確立できない時は、
`false`を返すことに注意してください。


`featurep`は、引数を評価します。


`declare`と`features`も参照してください。



```maxima
(%i1) declare (j, even)$
(%i2) featurep (j, integer);
(%o2)                           true
```

<!-- category: Programming -->
<!-- keywords: maxima_tempdir -->
<!-- signatures: maxima_tempdir -->
### Variable: maxima_tempdir

`maxima_tempdir`は、Maximaが一時的なファイルを生成するディレクトリを
指名します。
特に、プロットのための一時ファイルが
`maxima_tempdir`に生成されます。


`maxima_tempdir`の初期値は、
もしMaximaが置くことができるなら、ユーザーのホームディレクトリです;
そうでなければ、Maximaは適切なディレクトリについて推量します。


`maxima_tempdir`は、ディレクトリを指名する文字列に割り当てられます。

<!-- category: Programming -->
<!-- keywords: maxima_userdir -->
<!-- signatures: maxima_userdir -->
### Variable: maxima_userdir

`maxima_userdir`は、
Maximaが、MaximaやLispファイルを見つけるために検索するディレクトリを指名します。
(Maximaは、他のディレクトリも検索します;
`file_search_maxima`と`file_search_lisp`は、完全なリストです。)


`maxima_userdir`の初期値は、
もしMaximaが置くことができなら、
ユーザーのホームディレクトリのサブディレクトリです;
そうでなければ、Maximaは適切なディレクトリについて推量します。


`maxima_userdir`は、ディレクトリを指名する文字列に割り当てられます。
しかしながら、
`maxima_userdir`への割り当ては、自動的には
`file_search_maxima`と`file_search_lisp`を変えません;
それらの変数は、別々に変更しなければいけません。

<!-- category: Programming -->
<!-- keywords: room -->
<!-- signatures: room(), room(true), room(false) -->
### Function: room ()

Maximaの記憶装置とスタックマネージメントの状態の描写を印字します。
`room`は、同じ名前のLisp関数をコールします。



- *
`room ()`は、適度の描写を印字します。
- *
`room (true)`は、言葉数の多い描写を印字します。
- *
`room (false)`は、簡潔な描写を印字します。

<!-- category: Programming -->
<!-- keywords: sstatus -->
<!-- signatures: sstatus(keyword, item) -->
### Function: sstatus (keyword, item)

*keyword*がシンボル`feature`の時、*item*がシステムフィーチャのリスト上に追加されます。
`sstatus (keyword, item)`が実行された後、
`status (feature, item)`は`true`を返します。
もし*keyword*がシンボル`nofeature`なら、
*item*はシステムフィーチャのリストから削除されます。
これはパッケージ作者が、搭載したフィーチャの追跡をするのに役に立つかもしれません。


`status`も参照してください。

<!-- category: Programming -->
<!-- keywords: status -->
<!-- signatures: status(feature), status(feature, item) -->
### Function: status (feature)

いくつかのシステム依存のフィーチャの存在と不在についての情報を返す。



- *
`status (feature)`は、システムフィーチャのリストを返します。
これらは、Lispのバージョン、オペレーティングシステムのタイプなどを含みます。
リストは、１つのLispタイプからもう１つに変わるかもしれません。
- *
`status (feature, item)`は、
もし*item*が`status (feature)`が返す項目のリスト上にあるなら、
`true`を返し、そうでなければ、`false`を返します。
`status`は、引数*item*をクォートします。
クォート-クォート演算子`''`は、クォーテーションに優先されます。
名前が、ハイフンのように特殊文字を含むフィーチャは、
文字列引数として与えられなければいけません。例えば、
`status (feature, "ansi-cl")`。


`sstatus`も参照してください。


変数`features`は、
数式に適用される
フィーチャのリストを含みます。
もっと情報を知るには、`features`と`featurep`を参照してください。

<!-- category: Programming -->
<!-- keywords: system -->
<!-- signatures: system(command) -->
### Function: system (command)

別のプロセスとして*command*を実行します。
コマンドは実行のためデフォルトのシェルに渡されます。
`system`は、オペレーティングシステムすべてではサポートされませんが、
一般にUnixとUnixライクな環境では存在します。


`_hist.out`が、
`xgraph`を使ってバーグラフとしてプロットしたい頻度のリストだと仮定します。



```maxima
(%i1) (with_stdout("_hist.out",
           for i:1 thru length(hist) do (
             print(i,hist[i]))),
       system("xgraph -bar -brw .7 -nl < _hist.out"));
```


プロットをバックグラウンドで（Maximaに制御を戻すように）させるようにし、終了した後、一次ファルを削除するようにするためには、以下のようにします:



```maxima
system("(xgraph -bar -brw .7 -nl < _hist.out;  rm -f _hist.out)&")
```

<!-- category: Programming -->
<!-- keywords: time -->
<!-- signatures: time(%o1, %o2, %o3, ...) -->
### Function: time (%o1, %o2, %o3, ...)

出力行`%o1`, `%o2`, `%o3`, ...を計算するために使った
時間のリストを秒で返します。
返された時間は、内部計算時間のMaximaの概算であって、経過時間ではありません。
`time`は、出力行変数にだけ適用されます;
他の変数に関して、`time`は`unknown`を返します。


Maximaに出力行それぞれに計算時間と経過時間を印字させるには、
`showtime: true`を設定してください。

<!-- category: Programming -->
<!-- keywords: timedate -->
<!-- signatures: timedate(), timedate(T) -->
### Function: timedate ()

引数なしの`timedate()`は現在時刻と日付を表す文字列を返します。
文字列は、フォーマット`YYYY-MM-DD HH:MM:SS[+|-]ZZ:ZZ`を持ちます。
ここで、欄は、年、月、日、時、分、秒、時間と分のタイムゾーンオフセットです。


`timedate(T)`は
フォーマット`YYYY-MM-DD HH:MM:SS[+|-]ZZ:ZZ`の文字列として
時刻*T*を返します。
*T*は
`absolute_real_time`が返すような
1990年1月1日の真夜中以来の秒数として解釈されます。


例:


引数なしの`timedate()`は現在時刻と日付を表す文字列を返します。







```maxima
(%i1) d : timedate ();
(%o1)                      2010-06-08 04:08:09+01:00
(%i2) print ("timedate reports current time", d) $
timedate reports current time 2010-06-08 04:08:09+01:00
```


引数ありの`timedate`は引数を表す文字列を返します。







```maxima
(%i1) timedate (0);
(%o1)                      1900-01-01 01:00:00+01:00
(%i2) timedate (absolute_real_time () - 7*24*3600);
(%o2)                      2010-06-01 04:19:51+01:00
```

