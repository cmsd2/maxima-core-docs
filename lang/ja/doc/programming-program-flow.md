## Program Flow

<!-- category: Programming -->
<!-- keywords: backtrace -->
<!-- signatures: backtrace(), backtrace(n) -->
### Function: backtrace ()

コールスタック、すなわち、
現在アクティブな関数をコールした関数のリスト、を印字します。


`backtrace()`はコールスタック全体を印字します。


`backtrace (n)`は、
現在アクティブな関数を含めて、*n*個の直近の関数を印字します。




`backtrace`は、
(デバッグの文脈でだけでなく、)
スクリプト、関数、対話プロンプトからコールすることができます。


例:



- *
`backtrace()`はコールスタック全体を印字します。

```maxima
(%i1) h(x) := g(x/7)$
(%i2) g(x) := f(x-11)$
(%i3) f(x) := e(x^2)$
(%i4) e(x) := (backtrace(), 2*x + 13)$
(%i5) h(10);
#0: e(x=4489/49)
#1: f(x=-67/7)
#2: g(x=10/7)
#3: h(x=10)
                              9615
(%o5)                         ----
                               49
```



- *
`backtrace (n)`は、
現在アクティブな関数を含めて、*n*個の直近の関数を印字します。

```maxima
(%i1) h(x) := (backtrace(1), g(x/7))$
(%i2) g(x) := (backtrace(1), f(x-11))$
(%i3) f(x) := (backtrace(1), e(x^2))$
(%i4) e(x) := (backtrace(1), 2*x + 13)$
(%i5) h(10);
#0: h(x=10)
#0: g(x=10/7)
#0: f(x=-67/7)
#0: e(x=4489/49)
                              9615
(%o5)                         ----
                               49
```

<!-- category: Programming -->
<!-- keywords: do -->
<!-- signatures: do -->
### Function: do

`do`文は繰り返しを実行するために使われます。
その強力な一般性のために、
`do`文は２編で記述されます。
最初、通常の形式が
(Fortran, Algol, PL/I, など)いくつかの他のプログラミング言語の中で使われるそれ
との類似で与えられます;
それから、他の特長が言及されます。


この形式の、終了条件に関してだけ違う３つの別形があります。
それらは:



- *
`for variable: initial_value step increment thru limit do body`
- *
`for variable: initial_value step increment while condition do body`
- *
`for variable: initial_value step increment unless condition do body`



(代わりに、`step`は終了条件や範囲の後与えられるかもしれません。)


*initial_value*, *increment*, *limit*, *body*は、
任意の式を取り得ます。
もし増分が1なら、 "`step 1`"は省略できます。


`do`文の実行は、最初
*initial_value*を *variable* (今後、制御変数と呼びます)
に割り当てることによって処理されます。
そして:
(1) もし制御変数が `thru`指定の範囲を越えたら、もしくは、
`unless`の条件が `true`なら、
もしくは、 `while`の条件が `false`なら、
`do`は終了します。
(2) *body*が評価されます。
(3) 増分が制御変数に足されます。
終了条件が満たされるまで、
いずれかが満たされる時 `do`が終了する複数の終了条件を与えることもできます。


一般的に、 `thru`テストは、
もし *increment*が非負なら、制御変数が *limit*よりも大きい時、
または、もし *increment*が負なら、制御変数が *limit*よりも小さい時、
満たされます。
*increment*と *limit*は、この不等式が決定できる限り、数値でない式も取り得ます。
しかしながら、
`do`文が入力された時
*increment*が構文法的に負(例えば負の数)でない限り、
Maximaは、 `do`が実行される時、正と仮定します。
もし正でないなら、
`do`は適切に終了しないかもしれません。


*limit*, *increment*, 終了条件は、ループを通して毎回評価されることに注意してください。
もしこれらのいずれかがおおくの計算を含み、
*body*の実行中すべてで変わらない結果をもたらすなら、
`do`に先立って変数をそれらの値に設定し、その変数を
`do`形式の中で使うことはもっと効率的です。


`do`文が通常返す値は、アトム `done`です。
しかしながら、
早い時点で `do`から抜けて任意の望みの値を与えるために、
関数 `return`を *body*の中で使うことができます。
しかしながら、 `block`の中で起こる `do`の中の `return`は、
`do`だけから抜けて、 `block`からは抜けないことに注意してください。
`do`から囲んでいる `block`に抜けるために、
`go`関数は使えないことにも注意してください。


制御変数はいつも `do`にローカルです。


従って、
`do`の外側の同じ名前を持つ変数の値に影響することなく、任意の変数が使えます。
制御変数は、 `do`が終了した後、バインドされていません。



```maxima
(%i1) for a:-3 thru 26 step 7 do display(a)$
                             a = - 3

                              a = 4

                             a = 11

                             a = 18

                             a = 25
```



```maxima
(%i1) s: 0$
(%i2) for i: 1 while i <= 10 do s: s+i;
(%o2)                         done
(%i3) s;
(%o3)                          55
```


条件`while i <= 10`は、
`unless i > 10`と、また、`thru 10`と同値であることに注意してください。



```maxima
(%i1) series: 1$
(%i2) term: exp (sin (x))$
(%i3) for p: 1 unless p > 7 do
          (term: diff (term, x)/p, 
           series: series + subst (x=0, term)*x^p)$
(%i4) series;
                  7    6     5    4    2
                 x    x     x    x    x
(%o4)            -- - --- - -- - -- + -- + x + 1
                 90   240   15   8    2
```


以上は、`e^sin(x)`のTaylor級数の8項を与えます。




```maxima
(%i1) poly: 0$
(%i2) for i: 1 thru 5 do
          for j: i step -1 thru 1 do
              poly: poly + i*x^j$
(%i3) poly;
                  5      4       3       2
(%o3)          5 x  + 9 x  + 12 x  + 14 x  + 15 x
(%i4) guess: -3.0$
(%i5) for i: 1 thru 10 do
          (guess: subst (guess, x, 0.5*(x + 10/x)),
           if abs (guess^2 - 10) < 0.00005 then return (guess));
(%o5)                  - 3.162280701754386
```


この例は、
Newton-Raphson反復を最大10回使って、
10の負の平方根を計算します。
もし収束基準が満たされないなら、
戻り値は`done`になります。


いつもある量を制御変数に加える代わりに、
繰り返しそれぞれで量をある他の方法で換えたい時があるかもしれません。
この場合、
`step increment`の代わりに
`next expression`を使うことができます。
これは、ループの間、
制御変数が毎回*expression*の評価結果に設定されるようにします。



```maxima
(%i6) for count: 2 next 3*count thru 20 do display (count)$
                            count = 2

                            count = 6

                           count = 18
```



`for variable: value ...do...`の代わりとして、
構文法`for variable from value ...do...`が使えます。
これは、
`from value`を
`step`や`next`値の後や終了条件の後に置くことを許します。
もし`from value`が省略されたら、
初期値として1が使われます。


制御変数が実際には決して使われないような繰り返しを実行することに興味があることがあるかもしれません。
それゆえに、
貧弱な初期推測を使って5の平方根を計算する以下の例にあるように、
初期化と更新情報を省略して終了条件だけ与えることが許されます。



```maxima
(%i1) x: 1000$
(%i2) thru 20 do x: 0.5*(x + 5.0/x)$
(%i3) x;
(%o3)                   2.23606797749979
(%i4) sqrt(5), numer;
(%o4)                   2.23606797749979
```


もし望むなら、終了条件さえ完全に省略し、
無限に*body*を評価し続ける`do body`だけを与えることもできます。
この場合、関数`return`が`do`の実行を終了するのに使われるべきです。



```maxima
(%i1) newton (f, x):= ([y, df, dfx], df: diff (f ('x), 'x),
          do (y: ev(df), x: x - f(x)/y, 
              if abs (f (x)) < 5e-6 then return (x)))$
(%i2) sqr (x) := x^2 - 5.0$
(%i3) newton (sqr, 1000);
(%o3)                   2.236068027062195
```



(`return`が実行された時、
`x`の現在値を
`do`の値として返そうとすることに注意してください。
`do`がブロックの最後の文なので、
`block`から抜けて、
`do`の値が
`block`の値として返されます。)


`do`のもう１つ別の形式がMaximaで利用可能です。構文法は:



```maxima
for variable in list end_tests do body
```


*list*の要素は、
*body*の繰り返しのそれぞれで
`variable`に連続的に割り当てられる任意の式です。
オプションの終了テスト*end_tests*は、
`do`の実行を終了するのに使うことができます;
そうでなければ、
*list*が使い果たされた時、または、
*body*の中で
`return`が実行された時、
終了します。
 (実際には、`list`は非アトムの任意の式を取り得えて、連続的な部分が取られます。)



```maxima
(%i1)  for f in [log, rho, atan] do ldisp(f(1))$
(%t1)                                  0
(%t2)                                rho(1)
                                     %pi
(%t3)                                 ---
                                      4
(%i4) ev(%t3,numer);
(%o4)                             0.78539816
```

<!-- category: Programming -->
<!-- keywords: errcatch -->
<!-- signatures: errcatch(expr_1, ..., expr_n) -->
### Function: errcatch (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を１つずつ評価し、
もしエラーが起こらないなら、`[expr_n]` (リスト)を返します。
もしいずれかの引数の評価中にエラーが起こったら、
`errcatch` はエラーが伝搬することを抑制し、
引数をこれ以上評価せずに空のリスト`[]`を返します。


`errcatch`は
もしエラーがチャッチされないなら`batch`を終了させるエラーが起こるかもしれないと疑うような
`batch`ファイルで役立ちます。

<!-- category: Programming -->
<!-- keywords: error -->
<!-- signatures: error(expr_1, ..., expr_n) -->
### Function: error (expr_1, ..., expr_n)

*expr_1*, ..., *expr_n*を評価して印字します。
そして、エラーがあれば、トップレベルMaximaか直近の`errcatch`に戻るようにします。


変数`error`はエラーを記述するリストに設定されます。
`error`の最初の要素はフォーマット文字列です。
引数*expr_1*, ..., *expr_n*の中の文字列すべてを結合したものです。
残りの要素は文字列でない引数の値です。


`errormsg()`は`error`をフォーマットし印字します。
これは直近のエラーメッセージを効果的に再印字します。

<!-- category: Programming -->
<!-- keywords: error_size -->
<!-- signatures: error_size -->
### Variable: error_size

デフォルト値: 10


`error_size`は、
現れる式のサイズに従って、エラーメッセージを変更します。
もし式のサイズが、Lisp関数`ERROR-SIZE`によって決定されるように）
`error_size`より大きいなら、
式は、メッセージの中で、シンボルで置き換えられ、
シンボルは式に割り当てられます。
シンボルはリスト`error_syms`から取られます。


そうでなければ、式は`error_size`より小さく、
メッセージの中に式が表示されます。


`error`と`error_syms`も参照してください。


例:









`U`のサイズは、`ERROR-SIZE`で決められるように、24です。



```maxima
(%i1) U: (C^D^E + B + A)/(cos(X-1) + 1)$

(%i2) error_size: 20$

(%i3) error ("Example expression is", U);

Example expression is errexp1
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) errexp1;
                            E
                           D
                          C   + B + A
(%o4)                    --------------
                         cos(X - 1) + 1
(%i5) error_size: 30$

(%i6) error ("Example expression is", U);

                         E
                        D
                       C   + B + A
Example expression is --------------
                      cos(X - 1) + 1
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Programming -->
<!-- keywords: error_syms -->
<!-- signatures: error_syms -->
### Variable: error_syms

デフォルト値: `[errexp1, errexp2, errexp3]`


エラーメッセージの中で、
`error_size`より大きな式はシンボルで置き換えられ、
シンボルは式に設定されます。
シンボルはリスト`error_syms`から取られます。
最初の大きすぎる式は、`error_syms[1]`で置き換えられ、
２番目は、`error_syms[2]`で置き換えられ、などなど。


もし大きすぎる式が`error_syms`の要素よりもあれば、
シンボルは自動的に構成されます。
*n*番目のシンボルは`concat ('errexp, n)`と同値です。


`error`と`error_size`も参照してください。

<!-- category: Programming -->
<!-- keywords: errormsg -->
<!-- signatures: errormsg() -->
### Function: errormsg ()

直近のエラーメッセージを再印字します。
変数`error`はメッセージを保持し、
`errormsg`はそれをフォーマットし印字します。

<!-- category: Programming -->
<!-- keywords: for -->
<!-- signatures: for -->
### Function: for

繰り返しで使われます。
Maximaの繰り返し機能の記述に関しては、`do`を参照してください。

<!-- category: Programming -->
<!-- keywords: go -->
<!-- signatures: go(tag) -->
### Function: go (tag)

制御を
`go`の引数でタグ付けされたブロックの文に移すために
`block`内部で使われます。
文をタグ付けするには、
その文の前に、
アトムの引数を
`block`の中の別の文として
先行させてください。
例えば:



```maxima
block ([x], x:1, loop, x+1, ..., go(loop), ...)
```


`go`の引数は、同じ`block`の中に現れるタグの名前でなければいけません。
`go`を含む`block`以外の`block`の中のタグに移るために、
`go`を使うことはできません。

<!-- category: Programming -->
<!-- keywords: if -->
<!-- signatures: if -->
### Function: if

条件評価を表します。
`if`式の様々な形が認識されます。


`if cond_1 then expr_1 else expr_0`
は、
もし*cond_1*が`true`評価されたら*expr_1*に*評*価*され、
そうでなければ式は*expr_0*に評価されます。


コマンド `if cond_1 then expr_1 elseif cond_2 then expr_2 elseif ... else expr_0`は、
もし*cond_k*が`true`、かつ、先行する条件がすべて`false`なら、
*expr_k*に評価されます。
もし条件のいずれも`true`でないなら、式は`expr_0`に評価されます。


もし`else`がないなら、
最後に`else false`が仮定されます。
すなわち、コマンド `if cond_1 then expr_1`は、
`if cond_1 then expr_1 else false`と同値で、
コマンド `if cond_1 then expr_1 elseif ... elseif cond_n then expr_n`は、
`if cond_1 then expr_1 elseif ... elseif cond_n then expr_n else false`と同値です。


選択肢*expr_0*, ..., *expr_n*は、任意のMaxima式を取り得ます。
入れ子の`if`式もあり得ます。
選択肢は、
対応する条件が`true`でない限り、
整理も評価もされません。


条件*cond_1*, ..., *cond_n*は、潜在的に、また、実際に
`true`か`false`に評価される式です。
条件が実際には`true`にも`false`にも評価されない時、
`if`の振る舞いはグローバルフラグ`prederror`で決定されます。
`prederror`が`true`の時、
もし評価された条件のいずれかが`true`にも`false`にもならなかったら
、エラーになります。
そうでなければ、`true`にも`false`にも評価されない条件が受け入れられ、
結果は条件式になります。


条件は以下のように、他の要素間の関係演算子と論理演算子からなります。





```maxima
演算                 シンボル     タイプ
 
小なり                <           関係 中置
以下                  <=          関係 中置
等号 (構文法的)        =           関係 中置
不等号 (構文法的)      #           関係 中置
等号 (値)             equal       関係 関数
不等号 (値)           notequal    関係 関数
以上                  >=          関係 中置
大なり                >           関係 中置
かつ                  and         論理 中置
または                or          論理 中置
否定                  not         論理 前置
```

<!-- category: Programming -->
<!-- keywords: map -->
<!-- signatures: map(f, expr_1, ..., expr_n) -->
### Function: map (f, expr_1, ..., expr_n)

`map`は、主演算子（訳注：内部表現の最上位階層のリストに対応する演算子）は
式*expr_1*, ..., *expr_n*のそれと同じ演算子を使い、
そのサブパーツは、引数式の対応するサブパーツに*f*を適用した結果である式を返します。
*f*は$n$個の引数の関数名か、$n$個の引数のラムダ形式です。
(訳注：また、*expr_1*, ..., *expr_n*は内部表現に階層リスト構造を持つ式です。）


`maperror` - もし`maperror`が`fals`eなら、
マッピング関数のすべては、(1)もし*expr_i*のすべてが同じ長さでなければ、
最も短い*expr_i*が完了した時点で停止し、
(2)もし*expr_i*が同じタイプのオブジェクトでなければ、
*f*をリスト[*expr_1*, *expr_2*, ...]に適用します。
もし`maperror`が`true`なら、上の２つの場合、エラーメッセージを出力します。


この関数の用法の１つは、ある関数（例えば、`partfrac`)を非常に長い式に適用する際、
計算の間にリスト保存領域を枯渇させるため式全体に適応するのが不可能な場合に、
それぞれの項に関数をマップすることです。





```maxima
(%i1) map(f,x+a*y+b*z);
(%o1)                        f(b z) + f(a y) + f(x)
(%i2) map(lambda([u],partfrac(u,x)),x+1/(x^3+4*x^2+5*x+2));
                           1       1        1
(%o2)                     ----- - ----- + -------- + x
                         x + 2   x + 1          2
                                         (x + 1)
(%i3) map(ratsimp, x/(x^2+x)+(y^2+y)/y);
                                      1
(%o3)                            y + ----- + 1
                                    x + 1
(%i4) map("=",[a,b],[-0.5,3]);
(%o4)                          [a = - 0.5, b = 3]
```

<!-- category: Programming -->
<!-- keywords: mapatom -->
<!-- signatures: mapatom(expr) -->
### Function: mapatom (expr)

*expr*がマップルーチンでアトムとして扱われる時だけ`true`を返します。
"Mapatoms"はアトム、(有理数を含む)数、添字付き変数です。

<!-- category: Programming -->
<!-- keywords: maperror -->
<!-- signatures: maperror -->
### Variable: maperror

デフォルト値: `true`


`maperror`が`false`の時は、
マップ関数すべてに、以下の例のようにさせます。



```maxima
map (f, expr_1, expr_2, ...)
```


に対しては、
(1) もし*expr_i*のすべてが同じ長さでないなら、
最も短い*expr_i*の終わりまで完了した時、停止するようにさせ、
(2) もし*expr_i*すべてが同じタイプのオブジェクトでないなら、
*f*を[*expr_1*, *expr_2*, ...]に適用するようにさせます。


もし`maperror`が`true`なら、
上の２つの例に関して、エラーメッセージが表示されます。

<!-- category: Programming -->
<!-- keywords: maplist -->
<!-- signatures: maplist(f, expr_1, ..., expr_n) -->
### Function: maplist (f, expr_1, ..., expr_n)

式*expr_1*, ..., *expr_n*のパーツに*f*を適用した結果のリストを返します。
*f*は、関数名かラムダ式です。


`maplist`は`map (f, expr_1, ..., expr_n)`とは違います。
mapは主演算子が*expr_i*と同じ式を返します。
(整理と`map`が`apply`を行う場合は例外です。)

<!-- category: Programming -->
<!-- keywords: mapprint -->
<!-- signatures: mapprint -->
### Variable: mapprint

デフォルト値: `true`


`mapprint`が`true`の時、
`map`, `mapl`, `fullmap`からの様々な情報メッセージが
一定の状況で生成されます。
これらは
`map`が`apply`を使ったり、`map`が
最短のリストで切り詰めているような状況を含みます。


もし`mapprint`が`false`なら、これらのメッセージは抑制されます

<!-- category: Programming -->
<!-- keywords: outermap -->
<!-- signatures: outermap(f, a_1, ..., a_n) -->
### Function: outermap (f, a_1, ..., a_n)

関数*f*を
外積*a_1*掛ける*a_2* ... 掛ける*a_n*の要素のそれぞれに適用します。


*f*は
$n$個の引数の関数の名前か、
$n$個の引数のラムダ式
です。


それぞれの引数*a_k*は、
リストか、入れ子のリストか、行列か、他の任意の種類の式を取り得ます。


`outermap`戻り値は、入れ子の構造です。
*x*を戻り値とします。
すると、
*x*は最初のリストか入れ子のリストか行列引数と同じ構造を持ち、
`x[i_1]...[i_m]`は、
二番目のリストか入れ子のリストか行列引数と同じ構造を持ち、
`x[i_1]...[i_m][j_1]...[j_n]`は、
三番目のリストか入れ子のリストか行列引数と同じ構造を持ち、
以下同様。
ここで、*m*, *n*, ...は、
引数それぞれの要素
をアクセスするために要求される
インデックスの数(リストには１つ、行列には２つ、入れ子のリストには１つ以上)です。
リストや行列でない引数は戻り値の構造に影響を与えません。


Note that the effect of 
`outermap`の効果は
*f*を
`cartesian_product`によって返される
外積の要素のそれぞれに適用することのそれと違います。


`outermap`は、戻り値で引数の構造を保ちますが、
`cartesian_product`は違います。


`outermap`は引数を評価します。


`map`, `maplist`, `apply`も参照してください。



例:


`outermap`の初等的な例。
よりはっきり引数の組み合わせを示すために、
`F`は未定義のままです。










```maxima
(%i1) outermap(F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) outermap(F, matrix([a, b],[c, d]), matrix([1, 2],[3, 4]));
         [ [ F(a, 1)  F(a, 2) ]  [ F(b, 1)  F(b, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(a, 3)  F(a, 4) ]  [ F(b, 3)  F(b, 4) ] ]
(%o2)    [                                            ]
         [ [ F(c, 1)  F(c, 2) ]  [ F(d, 1)  F(d, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(c, 3)  F(c, 4) ]  [ F(d, 3)  F(d, 4) ] ]
(%i3) outermap (F, [a, b], x, matrix ([1, 2], [3, 4]));
       [ F(a, x, 1)  F(a, x, 2) ]  [ F(b, x, 1)  F(b, x, 2) ]
(%o3) [[                        ], [                        ]]
       [ F(a, x, 3)  F(a, x, 4) ]  [ F(b, x, 3)  F(b, x, 4) ]
(%i4) outermap (F, [a, b], matrix ([1, 2]), matrix ([x], [y]));
       [ [ F(a, 1, x) ]  [ F(a, 2, x) ] ]
(%o4) [[ [            ]  [            ] ], 
       [ [ F(a, 1, y) ]  [ F(a, 2, y) ] ]
                              [ [ F(b, 1, x) ]  [ F(b, 2, x) ] ]
                              [ [            ]  [            ] ]]
                              [ [ F(b, 1, y) ]  [ F(b, 2, y) ] ]
(%i5) outermap ("+", [a, b, c], [1, 2, 3]);
(%o5) [[a + 1, a + 2, a + 3], [b + 1, b + 2, b + 3], 
                                           [c + 1, c + 2, c + 3]]
```


`outermap`の戻り値のより密な検査。
最初の、二番目の、三番目の引数は、それぞれ、行列、リスト、行列です。
戻り値は行列です。
その行列の要素それぞれはリストで、
それぞれのリストの要素それぞれは行列です。















```maxima
(%i1) arg_1 :  matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) arg_2 : [11, 22];
(%o2)                       [11, 22]
(%i3) arg_3 : matrix ([xx, yy]);
(%o3)                      [ xx  yy ]
(%i4) xx_0 : outermap(lambda([x, y, z], x / y + z), arg_1,
                                                   arg_2, arg_3);
               [  [      a        a  ]  [      a        a  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
(%o4)  Col 1 = [                                              ]
               [  [      c        c  ]  [      c        c  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]

                 [  [      b        b  ]  [      b        b  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
         Col 2 = [                                              ]
                 [  [      d        d  ]  [      d        d  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]

(%i5) xx_1 : xx_0 [1][1];
           [      a        a  ]  [      a        a  ]
(%o5)     [[ xx + --  yy + -- ], [ xx + --  yy + -- ]]
           [      11       11 ]  [      22       22 ]
(%i6) xx_2 : xx_0 [1][1] [1];
                      [      a        a  ]
(%o6)                 [ xx + --  yy + -- ]
                      [      11       11 ]
(%i7) xx_3 : xx_0 [1][1] [1] [1][1];
                                  a
(%o7)                        xx + --
                                  11
(%i8) [op (arg_1), op (arg_2), op (arg_3)];
(%o8)                  [matrix, [, matrix]
(%i9) [op (xx_0), op (xx_1), op (xx_2)];
(%o9)                  [matrix, [, matrix]
```


`outermap`は、戻り値の中で引数の構造を保持します。
`cartesian_product`は保持しません。










```maxima
(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) setify (flatten (%));
(%o2) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i3) map(lambda([L], apply(F, L)),
                     cartesian_product({a, b, c}, {1, 2, 3}));
(%o3) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i4) is (equal (%, %th (2)));
(%o4)                         true
```

<!-- category: Programming -->
<!-- keywords: prederror -->
<!-- signatures: prederror -->
### Variable: prederror

デフォルト値: `false`


`prederror`が`true`の時、
`if`文の述語論理か`is`関数が
`true`か`false`に評価されるのに失敗した時はいつでも
エラーメッセージが表示されます。


もし`false`なら、この場合，代わりに`unknown`が返されます。
`prederror: false`モードは翻訳コードではサポートされません;
しかしながら、`maybe`は翻訳コードでサポートされます。


`is`と`maybe`も参照してください。

<!-- category: Programming -->
<!-- keywords: return -->
<!-- signatures: return(value) -->
### Function: return (value)

引数を連れて、陽にブロックから抜けるために使われます。
もっと情報を知るには、`block`も参照してください。

<!-- category: Programming -->
<!-- keywords: scanmap -->
<!-- signatures: scanmap(f, expr), scanmap(f, expr, bottomup) -->
### Function: scanmap (f, expr)

トップダウン法で、*f*を*expr*に再帰的に適用します。
完全な因数分解が望まれる時、これは最も役に立ちます。
例えば:



```maxima
(%i1) exp:(a^2+2*a+1)*y + x^2$
(%i2) scanmap(factor,exp);
                                    2      2
(%o2)                         (a + 1)  y + x
```


Note the way in which 
`scanmap`が与えられた関数`factor`を
*expr*の構成部分式に適用する方法に注意してください;
もし
*expr*の別の形がscanmapに適用されるなら、結果は異なるかもしれません。
従って、
`scanmap`が
`exp`の展開形に適用される時、
`%o2`が再現されません:



```maxima
(%i3) scanmap(factor,expand(exp));
                           2                  2
(%o3)                      a  y + 2 a y + y + x
```


`scanmap`が
与えられた関数を指数関数を含む部分式すべてに再帰的に適用する方法の別の例です:



```maxima
(%i4) expr : u*v^(a*x+b) + c$
(%i5) scanmap('f, expr);
                    f(f(f(a) f(x)) + f(b))
(%o5) f(f(f(u) f(f(v)                      )) + f(c))
```


`scanmap (f, expr, bottomup)`は、
ボトムアップ法で
*f*を
*expr*に適用します。
例えば、未定義`f`に関して、



```maxima
scanmap(f,a*x+b) ->
   f(a*x+b) -> f(f(a*x)+f(b)) -> f(f(f(a)*f(x))+f(b))
scanmap(f,a*x+b,bottomup) -> f(a)*f(x)+f(b)
    -> f(f(a)*f(x))+f(b) ->
     f(f(f(a)*f(x))+f(b))
```


この場合、両方の方法で同じ答えを得ます。

<!-- category: Programming -->
<!-- keywords: throw -->
<!-- signatures: throw(expr) -->
### Function: throw (expr)

*expr*を評価し、
直近の`catch`に値を投げ戻します。
`throw`は、
`catch`と一緒に、非ローカルリターンメカニズムとして使われます。

<!-- category: Programming -->
<!-- keywords: while, unless -->
<!-- signatures: unless -->
### Function: while

`do`を参照してください。

