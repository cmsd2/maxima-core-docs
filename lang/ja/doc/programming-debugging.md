## Debugging

<!-- category: Programming -->
<!-- keywords: debugmode -->
<!-- signatures: debugmode -->
### Variable: debugmode

デフォルト値: `false`


もし`debugmode`が `true`なら、
Maximaのエラーが起こった時Maximaはデバッガーを開始します。
ユーザーはコールバックを検査したり、ブレイクポイントを設定したり、Maximaコードをステップ実行したりなど
コマンドを入力することができます。
デバッガーコマンドのリストに関しては、 `debugging`を参照してください。


`debugmode`をイネーブルにしても、Lispのエラーは捕らえられません。

<!-- category: Programming -->
<!-- keywords: refcheck -->
<!-- signatures: refcheck -->
### Variable: refcheck

デフォルト値: `false`


`refcheck`が`true`の時、
Maximaは
計算の中で、バイドされた変数が最初に使われる度にメッセージを印字します。

<!-- category: Programming -->
<!-- keywords: setcheck -->
<!-- signatures: setcheck -->
### Variable: setcheck

デフォルト値: `false`


もし`setcheck`が(添字付きでもよい)変数のリストに設定されているなら、
Maximaは
変数またはそれらの添字付き出現が通常の割り当て演算子`:`、`::`割り当て演算子、
または関数引数バインドでバインドされた時
(しかし関数割り当て`:=`やマクロ割り当て`::=`演算子でバインドされた時以外)
はいつでも、
メッセージを印字します。
メッセージは変数名とバインドされた値から構成されます。


`setcheck`は、
`all`または`true`に設定することができ、
それによって、すべての変数を含みます。


`setcheck`の新しい要素のそれぞれは、
チェックする変数の新しいリストを確立し、
以前`setcheck`に割り当てられたいかなる変数も忘れられます。


もし自身以外の何かに評価されるなら、
`setcheck`に割り当てられた名前はクォートしなければいけません。
例えば、もし`x`, `y`, `z`が既にバインドされているなら、
チェックする変数のリストに置くには、



```maxima
setcheck: ['x, 'y, 'z]$
```


をタイプしてください。


`setcheck`リスト上の変数が、例えば、`X: 'X`のように、
それ自身に割り当てられた時は、なにも印字されません。

<!-- category: Programming -->
<!-- keywords: setcheckbreak -->
<!-- signatures: setcheckbreak -->
### Variable: setcheckbreak

デフォルト値: `false`


`setcheckbreak`が`true`の時、
`setcheck`リスト上の変数が新しい値を割り当てられた時はいつでも
Maximaはブレイクプロンプトを出します。
ブレイクは、割り当てが実行される前に起こります。
この時点で、`setval`が変数が割り当てられようとしている値を保持します。
ゆえに、
`setval`に割り当てることで、違う値を割り当てることができます。


`setcheck`と`setval`も参照してください。

<!-- category: Programming -->
<!-- keywords: setval -->
<!-- signatures: setval -->
### Variable: setval

`setcheckbreak`が起こった時、変数が設定されようとしている値を保持します。
ゆえに、
`setval`に割り当てることで、違う値を割り当てることができます。


`setcheck`と`setcheckbreak`も参照してください。

<!-- category: Programming -->
<!-- keywords: timer -->
<!-- signatures: timer(f_1, ..., f_n), timer(all), timer() -->
### Function: timer (f_1, ..., f_n)

`timer`は、
タイミング統計が収集される関数のリストに与えられた関数*f_1*, ..., *f_n*
それぞれを入れます。
`timer(f)$ timer(g)$`は、リストに`f`を入れ、その後`g`を入れます;
リストはあるコールから次へ累積されます。


`timer(all)`は、計測される関数のリストに
(グローバル変数`functions`で指名されたように)
ユーザー定義関数すべてを入れます。


引数なしでは、
`timer`は計測される関数のリストを返します。


Maximaは、計測される関数のリストに関して、
関数それぞれを実行するのに費やされる時間を記録します。
`timer_info`は、タイミング統計を返します。
関数コール毎に経過した平均時間、コール回数、総経過時間を含みます。
`untimer`は、計測される関数のリストから関数を削除します。


`timer`は引数をクォートします。
`f(x) := x^2$ g:f$ timer(g)$`は、`f`をタイマーリストに入れません。


もし`trace(f)`が有効なら、`timer(f)`は有効ではないです;
`trace`と`timer`が同時に有効にはできません。


`timer_devalue`も参照してください。

<!-- category: Programming -->
<!-- keywords: timer_devalue -->
<!-- signatures: timer_devalue -->
### Variable: timer_devalue

デフォルト値: `false`


`timer_devalue`が`true`の時、
Maximaは、計られる関数から
他の計測される関数で費やされた時間を引きます。
そうでなければ、関数それぞれについて報告された時間は、
他の関数で計測される時間を含みます。
計測されない関数で費やされた時間は、総時間から引かれないことに注意してください。


`timer`と`timer_info`も参照してください。

<!-- category: Programming -->
<!-- keywords: timer_info -->
<!-- signatures: timer_info(f_1, ..., f_n), timer_info() -->
### Function: timer_info (f_1, ..., f_n)

与えられた関数*f_1*, ..., *f_n*,
`timer_info`は、
関数それぞれのタイミング情報を含む
行列を返します。
引数なしでは、
`timer_info`は、
現在タイマーリスト上の関数すべてについての
タイミング情報を返します。
The matrix returned by 
`timer_info`が返す行列は、関数名、
関数コール毎の時間、関数コールの回数、総時間、
`gctime`
を含みます。
`gctime`は、元のMacymaの「ガーベッジコレクション時間」を意味しましたが、
今はいつもゼロです。


`timer_info`が戻り値を構成するデータは、
`get`関数によっても得られることができます:



```maxima
get(f, 'calls);  get(f, 'runtime);  get(f, 'gctime);
```


`timer`も参照してください。

<!-- category: Programming -->
<!-- keywords: trace -->
<!-- signatures: trace(f_1, ..., f_n), trace(all), trace() -->
### Function: trace (f_1, ..., f_n)

関数 *f_1*, ..., *f_n*が与えられたとして、
`trace`は、Maximaに、
それらの関数がコールされたときはいつでも
デバッグ情報を印字するよう指示します。
`trace(f)$ trace(g)$`は、トレースする関数のリストに
`f`を、それから`g`を入れます;
リストは１回のコールから次へ累積します。


`trace(all)`は、(グローバル変数`functions`で指名されたように)
ユーザー定義関数すべてをトレースする関数のリストに入れます。


引数なしでは、
`trace`は、現在とレースする関数すべてのリストを返します。


`untrace`関数はトレースをディセーブルします。
`trace_options`も参照してください。


`trace`は引数をクォートします。
例えば、
`f(x) := x^2$ g:f$ trace(g)$`は、
`f`をトレースリストに入れません。


関数が再定義された時、
タイマーリストから削除されます。
例えば、
`timer(f)$ f(x) := x^2$`の後、
関数`f`はもはやタイマーリストにありません。


もし`timer (f)`が有効なら、
`trace (f)`は有効ではありません;
`trace`と`timer`は、同じ関数で同時には有効にできません。

<!-- category: Programming -->
<!-- keywords: trace_options -->
<!-- signatures: trace_options(f, option_1, ..., option_n), trace_options(f) -->
### Function: trace_options (f, option_1, ..., option_n)

関数*f*についてトレースオプションを設定します。
いかなる以前のオプションも破棄されます。
`trace_options (f, ...)`は、
もし(`trace_options`の前でも後でも). 
`trace (f)`もコールされないなら、
有効になりません。


`trace_options (f)`は、
オプションすべてをデフォルト値に再設定します。


オプションキーワードは以下の通りです:



- *
`noprint`
関数の入り口と出口でメッセージを印字しません。
- *
`break`
関数に入る前と関数を抜けた後、ブレイクポイントを置きます。
`break`を参照してください。
- *
`lisp_print`
引数を表示し、Lispオブジェクトとして値を返します。
- *
`info`
関数の入れ口と出口で`-> true`を印字します
- *
`errorcatch`
エラーをチャッチし、
エラーを知らせるためのオプションに応じて、
関数コールを再試行するか、戻り値を指定します。


トレースオプションは、２つの形式で指定されます。
オプションキーワード単体の存在は、
オプションを無条件に実行します。
(`foo: true`か似た形式を指定することでは、
オプション*foo*は実行されないことに注意してください;
キーワードはクォートする必要はないことにも注意してください。)
オプションキーワードを述語論理関数で指定することは、
オプションを述語論理上の条件付きにします。


述語論理関数の引数リストは、いつも
`[level, direction, function, item]`です。
ここで、`level`は関数の再帰レベルで、
`direction`は`enter`か`exit`、`function`は、
関数名、
name of the function, and 
`item`は(入るときの)引数リストか(出るときの)戻り値です。


以下は無条件とレースオプションの例です:



```maxima
(%i1) ff(n) := if equal(n, 0) then 1 else n * ff(n - 1)$

(%i2) trace (ff)$

(%i3) trace_options (ff, lisp_print, break)$

(%i4) ff(3);
```


以下は述語論理上の条件の`break`オプションを持つ同じ関数です:



```maxima
(%i5) trace_options (ff, break(pp))$

(%i6) pp (level, direction, function, item) := block (print (item),
    return (function = 'ff and level = 3 and direction = exit))$

(%i7) ff(6);
```

<!-- category: Programming -->
<!-- keywords: untimer -->
<!-- signatures: untimer(f_1, ..., f_n), untimer() -->
### Function: untimer (f_1, ..., f_n)

`untimer`はタイマーリストから
与えられた関数*f_1*, ..., *f_n*それぞれを削除します。


引数なしの時、
`untimer`は、現在、タイマーリスト上の関数すべてを削除します。


`untimer (f)`が実行された後、
`timer_info()` (引数なし)は、
現在タイマーリスト上にない関数についての情報を返しませんけれども、
`timer_info (f)`は、まだ以前に集計されたタイミング統計を返します。
`timer (f)`は、
タイミング統計すべてをゼロに再設定し、
`f`をタイマーリストに再び入れます。

<!-- category: Programming -->
<!-- keywords: untrace -->
<!-- signatures: untrace(f_1, ..., f_n), untrace() -->
### Function: untrace (f_1, ..., f_n)

`untrace`は、
与えられた関数*f_1*, ..., *f_n*について、
`trace`関数でイネーブルされたトレースをディセーブルします。
引数なしでは、`untrace`は関数すべてのトレースをディセーブルします。


`untrace`はトレースをディセーブルした関数のリストを返します。

