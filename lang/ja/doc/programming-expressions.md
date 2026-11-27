## Expressions

<!-- category: Programming -->
<!-- keywords: alias -->
<!-- signatures: alias(new_name_1, old_name_1, ..., new_name_n, old_name_n) -->
### Function: alias (new_name_1, old_name_1, ..., new_name_n, old_name_n)

(利用者もしくはシステム)関数や変数、配列等に対して別名を与えます。
任意の偶数個の引数を取ります。

<!-- category: Programming -->
<!-- keywords: aliases -->
<!-- signatures: aliases -->
### Variable: aliases

デフォルト値: `[]`


`aliases`は、
(`alias`, `ordergreat`, `orderless`関数によって、もしくは、
`declare`で
アトムを`noun`に宣言することで、設定される)
ユーザー定義のエーリアスを持つ
アトムのリストです。

See also: `alias`, `ordergreat`, `orderless`, `declare`, `noun`.

<!-- category: Programming -->
<!-- keywords: allbut -->
<!-- signatures: allbut -->
### Variable: allbut

`part`コマンド(すなわち、`part`,`inpart`,`substpart`,
`substinpart`,`dpart`, `lpart`)と共に動作します。例えば、







```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, [2, 5]);
(%o2)                         d + a
```


一方、







```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, allbut (2, 5));
(%o2)                       e + c + b
```


`kill`も`allbut`を認識します。








```maxima
(%i1) [aa : 11, bb : 22, cc : 33, dd : 44, ee : 55];
(%o1)                 [11, 22, 33, 44, 55]
(%i2) kill (allbut (cc, dd));
(%o0)                         done
(%i1) [aa, bb, cc, dd];
(%o1)                   [aa, bb, 33, 44]
```


`kill(allbut(a_1, a_2, ...))`は、
シンボル*a_1*, *a_2*, ...をキルしないよう除外して
`kill(all)`を実行します。

See also: `part`, `inpart`, `substpart`, `substinpart`, `dpart`, `lpart`, `kill`.

<!-- category: Programming -->
<!-- keywords: args -->
<!-- signatures: args(expr) -->
### Function: args (expr)

`expr`の引数のリストを返します。
ここで、`expr`アトム以外のいかなる種類の式を取り得ます。
トップレベル演算子の引数だけが抽出されます;
`expr`の部分式は、要素として、または、引数のリストの要素の部分式として現れます。


リストの中の項目の順序は、グローバルフラグ`inflag`に依存するかもしれません。


`args (expr)`は、`substpart ("[", expr, 0)`と同値です。
`substpart`と`op`も参照してください。

See also: `inflag`, `substpart`, `op`.

<!-- category: Programming -->
<!-- keywords: atom -->
<!-- signatures: atom(expr) -->
### Function: atom (expr)

もし *expr*がアトム(すなわち、数や名前や文字)なら、
 `true`、そうでなければ `false`を返します。
例えば、 `atom(5)`は `true`ですが、
(`a[1]`と `x`はバインドされていないと仮定して) `atom(a[1])`や `atom(sin(x))`は `false`です。

<!-- category: Programming -->
<!-- keywords: box -->
<!-- signatures: box(expr), box(expr, a) -->
### Function: box (expr)

枠で囲んだ*expr*を返します。
返り値は、演算子として`box`を持ち、引数として*expr*を持つ式です。
`display2d`が`true`の時、ディスプレイ上に枠が描かれます。


`box (expr, a)`は、
シンボル*a*でラベルされた枠で*expr*を囲みます。
もし枠の幅より長ければ、ラベルは切りつめられます。


`box`は引数を評価します。
しかしながら、枠に入れられた式は中身に評価されないので、
枠に入れられた式は、計算から効果的に除外されます。


`boxchar`は、`box`, `dpart`, `lpart`関数において
枠を描くのに使われる文字です。


例:













```maxima
(%i1) box (a^2 + b^2);
                            """""""""
                            " 2    2"
(%o1)                       "b  + a "
                            """""""""
(%i2) a : 1234;
(%o2)                         1234
(%i3) b : c - d;
(%o3)                         c - d
(%i4) box (a^2 + b^2);
                      """"""""""""""""""""
                      "       2          "
(%o4)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i5) box (a^2 + b^2, term_1);
                      term_1""""""""""""""
                      "       2          "
(%o5)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i6) 1729 - box (1729);
                                 """"""
(%o6)                     1729 - "1729"
                                 """"""
(%i7) boxchar: "-";
(%o7)                           -
(%i8) box (sin(x) + cos(y));
                        -----------------
(%o8)                   -cos(y) + sin(x)-
                        -----------------
```

See also: `boxchar`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: boxchar -->
<!-- signatures: boxchar -->
### Variable: boxchar

デフォルト値: `"`


`boxchar`は、`box`, `dpart`, `lpart`関数において
枠を描くのに使われる文字です。


式の中の枠すべては、`boxchar`の現在値で描かれます;
描画文字は枠式に保存されていません。

See also: `box`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: collapse -->
<!-- signatures: collapse(expr) -->
### Function: collapse (expr)

共通の（すなわち等しい）部分式の全てを共用と（すなわち、同じセルを使用）させることで、
*expr*を縮約し、スペースを節約します。
(`collapse`は、`optimize`コマンドによって使われるサブルーチンです。）
例えば，`collapse`をコールすることは、
`save`ファイルに積んだ後役に立つかもしれません。
`collapse ([expr_1, ..., expr_n])`を使うことで、いくつかの式を
一緒に縮約できます。
同様に、`collapse (listarray ('A))`を実行することで、配列`A`の要素を縮約できます。

See also: `save`.

<!-- category: Programming -->
<!-- keywords: disolate -->
<!-- signatures: disolate(expr, x_1, ..., x_n) -->
### Function: disolate (expr, x_1, ..., x_n)

ユーザーに１つ以上の変数を同時にisolate可能にさせることを除いて、
`isolate (expr, x)`に似ています。
例えば、もし多重積分の中で変数を変えようとしていて、それが２つ以上の積分変数を含んだ変数変換なら、これは役立つかもしれません。
この関数は、`simplification/disol.mac`から自動ロードされます。
`demo("disol")$`でデモが入手可能です。

<!-- category: Programming -->
<!-- keywords: dispform -->
<!-- signatures: dispform(expr), dispform(expr, all) -->
### Function: dispform (expr)

*expr*の外部表現を返します。


`dispform(expr)`は、主（トップレベル）演算子に関して外部表現を返します。
`dispform(expr, all)`は、*expr*の中の演算子すべてに関して
外部表現を返します。


`part`, `inpart`, `inflag`も参照してください。


例:


`- x`の内部表現は、「-1掛ける`x`」ですが、
外部表現は、「マイナス`x`」です。









```maxima
(%i1) - x;
(%o1)                          - x
(%i2) ?format (true, "~S~%", %);
((MTIMES SIMP) -1 $X)
(%o2)                         false
(%i3) dispform (- x);
(%o3)                          - x
(%i4) ?format (true, "~S~%", %);
((MMINUS SIMP) $X)
(%o4)                         false
```


`sqrt(x)`の内部表現は、「`x`の1/2乗」ですが、
外部表現は、「`x`の平方根」です。









```maxima
(%i1) sqrt (x);
(%o1)                        sqrt(x)
(%i2) ?format (true, "~S~%", %);
((MEXPT SIMP) $X ((RAT SIMP) 1 2))
(%o2)                         false
(%i3) dispform (sqrt (x));
(%o3)                        sqrt(x)
(%i4) ?format (true, "~S~%", %);
((%SQRT SIMP) $X)
(%o4)                         false
```


オプション引数`all`の使用。









```maxima
(%i1) expr : sin (sqrt (x));
(%o1)                     sin(sqrt(x))
(%i2) freeof (sqrt, expr);
(%o2)                         true
(%i3) freeof (sqrt, dispform (expr));
(%o3)                         true
(%i4) freeof (sqrt, dispform (expr, all));
(%o4)                         false
```

See also: `part`, `inpart`, `inflag`.

<!-- category: Programming -->
<!-- keywords: dpart -->
<!-- signatures: dpart(expr, n_1, ..., n_k) -->
### Function: dpart (expr, n_1, ..., n_k)

`part`と同じ部分式を選択しますが、
その部分式を値として返すだけの代わりに、
枠の中に表示されて選択された部分式を持つ式全体を返します。
枠は実際に式の一部です。



```maxima
(%i1) dpart (x+y/z^2, 1, 2, 1);
                             y
(%o1)                       ---- + x
                               2
                            """
                            "z"
                            """
```

See also: `part`.

<!-- category: Programming -->
<!-- keywords: exptisolate -->
<!-- signatures: exptisolate -->
### Variable: exptisolate

デフォルト値: `false`



`exptisolate`が`true`の時、
`isolate (expr, var)`は、
`var`を含む(`%e`のような)アトムの指数を検査します。

<!-- category: Programming -->
<!-- keywords: exptsubst -->
<!-- signatures: exptsubst -->
### Variable: exptsubst

デフォルト値: `false`


`exptsubst`が`true`の時、
`%e^(a x)`の中の`%e^x`へ`y`を代入するような代入を許します。

<!-- category: Programming -->
<!-- keywords: freeof -->
<!-- signatures: freeof(x_1, ..., x_n, expr) -->
### Function: freeof (x_1, ..., x_n, expr)

もし*x_1*と等しい*expr*の部分式がないか、
*x_1*が*expr*の中でダミー変数としてのみ現れるか、
*x_1*が*expr*の中で任意の演算子の名詞形でも動詞形でもないなら、
`freeof (x_1, expr)`は、`true`を返します。
そうでなければ、`false`を返します。


`freeof (x_1, ..., x_n, expr)`は、
`freeof (x_1, expr)かつ、 ...かつfreeof (x_n, expr)`と同値です。


引数*x_1*, ..., *x_n* は、
関数や変数の名前、添字付き名前、（ダブルクォートでくくられた）演算子、もしくは一般式
を取り得ます。
`freeof`は引数を評価します。


`freeof`は、そのままは（整理と評価の後）*expr*上でのみ演算し、
ある同値の表現が違った結果を与えるかどうかを決定しようとはしません。
特に、整理は、同値ですが、*expr*の原型とは違った要素を含む異なる式を生成するかもしれません。


もし式の外部にバインドを持たなければ、変数は、式の中のダミー変数です。
`freeof`によって認識されたダミー変数は、
和や積のインデックス、`limit`の中の極限変数、
`integrate`の定積分形の中の積分変数、
`laplace`の中のオリジナル変数、
`at`式の中の形式変数、
`lambda`式の中の引数です。


`integrate`の不定積分形は、積分変数から自由では*ありません*。


例:


引数は、関数、変数、添字付き名前、演算子、式の名前です。
`freeof (a, b, expr)`は
`freeof (a, expr) and freeof (b, expr)`と同値です。



```maxima
(%i1) expr: z^3 * cos (a[1]) * b^(c+d);
                                 d + c  3
(%o1)                   cos(a ) b      z
                             1
(%i2) freeof (z, expr);
(%o2)                         false
(%i3) freeof (cos, expr);
(%o3)                         false
(%i4) freeof (a[1], expr);
(%o4)                         false
(%i5) freeof (cos (a[1]), expr);
(%o5)                         false
(%i6) freeof (b^(c+d), expr);
(%o6)                         false
(%i7) freeof ("^", expr);
(%o7)                         false
(%i8) freeof (w, sin, a[2], sin (a[2]), b*(c+d), expr);
(%o8)                         true
```


`freeof`は引数を評価します。



```maxima
(%i1) expr: (a+b)^5$
(%i2) c: a$
(%i3) freeof (c, expr);
(%o3)                         false
```


`freeof`は、同値の式を考慮しません。
整理は、同値ですが異なる式を生成します。



```maxima
(%i1) expr: (a+b)^5$
(%i2) expand (expr);
          5        4       2  3       3  2      4      5
(%o2)    b  + 5 a b  + 10 a  b  + 10 a  b  + 5 a  b + a
(%i3) freeof (a+b, %);
(%o3)                         true
(%i4) freeof (a+b, expr);
(%o4)                         false
(%i5) exp (x);
                                 x
(%o5)                          %e
(%i6) freeof (exp, exp (x));
(%o6)                         true
```


和や定積分はダミー変数から自由です。
不定積分は積分変数から自由ではありません。



```maxima
(%i1) freeof (i, 'sum (f(i), i, 0, n));
(%o1)                         true
(%i2) freeof (x, 'integrate (x^2, x, 0, 1));
(%o2)                         true
(%i3) freeof (x, 'integrate (x^2, x));
(%o3)                         false
```

See also: `limit`, `integrate`, `laplace`, `at`, `lambda`.

<!-- category: Programming -->
<!-- keywords: inflag -->
<!-- signatures: inflag -->
### Variable: inflag

デフォルト値: `false`


`inflag`が`true`の時、
部分抽出のための関数は、`expr`の内部形式を検査します。


整理器は式を再順序付けすることに注意してください。
例えば、
もし`inflag`が`true`なら、
`first (x + y)`は、`x`を返し、
もしif `inflag`が`false`なら、`y`を返します。
(`first (y + x)`は同じ結果を与えます。)


また、`inflag`を`true`に設定し、`part`や`substpart`をコールすることは、
`inpart`や`substinpart`をコールすることと同じです。


`inflag`の設定に影響される関数は以下の通りです:
`part`, `substpart`, `first`, `rest`, `last`, `length`, `for` ... `in`構成子,
`map`, `fullmap`, `maplist`, `reveal`, `pickapart`。

See also: `part`, `substpart`, `inpart`, `substinpart`, `first`, `rest`, `last`, `length`, `for`, `map`, `fullmap`, `maplist`, `reveal`, `pickapart`.

<!-- category: Programming -->
<!-- keywords: inpart -->
<!-- signatures: inpart(expr, n_1, ..., n_k) -->
### Function: inpart (expr, n_1, ..., n_k)

`part`に似ていますが、表示形式ではなく内部表現上で機能し、
フォーマットが実行されないのでより速いかもしれません。
（内部形式での変数の順序はしばしば表示形式でのそれと異なるので）
和や積の中の部分式の順序や、
（以下の演算子は式から取り除かれるので）単項マイナス、引き算、割り算を扱う際の部分式の順序
に関して注意が必要です。
`part (x+y, 0)`や`inpart (x+y, 0)`は、
`+`を返しますが、
演算子を参照するため、"で囲まれたものになります。
例えば、`... if inpart (%o9,0) = "+" then ...`.


例:



```maxima
(%i1) x + y + w*z;
(%o1)                      w z + y + x
(%i2) inpart (%, 3, 2);
(%o2)                           z
(%i3) part (%th (2), 1, 2);
(%o3)                           z
(%i4) 'limit (f(x)^g(x+1), x, 0, minus);
                                  g(x + 1)
(%o4)                 limit   f(x)
                      x -> 0-
(%i5) inpart (%, 1, 2);
(%o5)                       g(x + 1)
```

<!-- category: Programming -->
<!-- keywords: isolate -->
<!-- signatures: isolate(expr, x) -->
### Function: isolate (expr, x)

和であり、中間式ラベル(それらは`%t1`, `%t2`, ...のようなアトムなシンボルです)
で置き換えられた*x*を含まない部分式を含む*expr*を返します。
興味のある変数を含まない部分式の不必要な展開を避けるのに、これはしばしば役立ちます。
中間ラベルは部分式にバインドされているので、
それらが現れた式を評価することで、それらをすべて元に代入することができます。


もし`exptisolate` (デフォルト値: `false`)が`true`なら、
`isolate`は、*x*を含むか、(`%e`のような)アトムの指数を検査します。


もし`isolate_wrt_times`が`true`なら、
`isolate`は積に関してもisolateします。
`isolate_wrt_times`を参照してください。


サンプルを見るには、`example (isolate)`を実行してください。

See also: `exptisolate`, `isolate_wrt_times`.

<!-- category: Programming -->
<!-- keywords: isolate_wrt_times -->
<!-- signatures: isolate_wrt_times -->
### Variable: isolate_wrt_times

デフォルト値: `false`


`isolate_wrt_times`が`true`の時,
`isolate`は、積に関してもisolateします。
例えば、スイッチの両方の設定を比較すると、



```maxima
(%i1) isolate_wrt_times: true$
(%i2) isolate (expand ((a+b+c)^2), c);

(%t2)                          2 a


(%t3)                          2 b


                          2            2
(%t4)                    b  + 2 a b + a

                     2
(%o4)               c  + %t3 c + %t2 c + %t4
(%i4) isolate_wrt_times: false$
(%i5) isolate (expand ((a+b+c)^2), c);
                     2
(%o5)               c  + 2 b c + 2 a c + %t4
```

<!-- category: Programming -->
<!-- keywords: lfreeof -->
<!-- signatures: lfreeof(list, expr) -->
### Function: lfreeof (list, expr)

*list*のそれぞれのメンバー*m*に関して、
`freeof (m, expr)`をコールします。
もし`freeof`のコールのいずれかが`false`を返すなら、
`false`を返し、そうでなければ、`true`を返します。

<!-- category: Programming -->
<!-- keywords: listconstvars -->
<!-- signatures: listconstvars -->
### Variable: listconstvars

デフォルト値: `false`


`listconstvars`が`true`の時、
`listofvars`は、`%e`, `%pi`, `%i`や
定数と宣言された任意の変数を、
もしそれらが、`listofvars`がコールされた式の中で現れたなら、
戻り値のリストの中に含みます。
デフォルトはこれらを省略します。

See also: `listofvars`.

<!-- category: Programming -->
<!-- keywords: listdummyvars -->
<!-- signatures: listdummyvars -->
### Variable: listdummyvars

デフォルト値: `true`


`listdummyvars`が`false`の時、
式の中の「ダミー変数」は、`listofvars`が返すリストの中に含まれません。
（「ダミー変数」の意味は`freeof`で与えられているものです。
「ダミー変数」は、和や積のインデックスや、極限変数、定積分変数のように数学的なものです。）


例:



```maxima
(%i1) listdummyvars: true$
(%i2) listofvars ('sum(f(i), i, 0, n));
(%o2)                        [i, n]
(%i3) listdummyvars: false$
(%i4) listofvars ('sum(f(i), i, 0, n));
(%o4)                          [n]
```

See also: `listofvars`, `freeof`.

<!-- category: Programming -->
<!-- keywords: listofvars -->
<!-- signatures: listofvars(expr) -->
### Function: listofvars (expr)

*expr*の中の変数のリストを返します。


もし`listconstvars`が`true`なら、
`listofvars`は、`%e`, `%pi`, `%i`や
定数と宣言された任意の変数を、
もしそれらが、*expr*の中で現れたなら、
戻り値のリストの中に含みます。
デフォルトはこれらを省略します。


変数のリストのなかの「ダミー変数」を除外したり含めたりするには、オプション変数 `listdummyvars`も参照してください。



```maxima
(%i1) listofvars (f (x[1]+y) / g^(2+a));
(%o1)                     [g, a, x , y]
                                  1
```

See also: `listconstvars`, `listdummyvars`.

<!-- category: Programming -->
<!-- keywords: lpart -->
<!-- signatures: lpart(label, expr, n_1, ..., n_k) -->
### Function: lpart (label, expr, n_1, ..., n_k)

`dpart`に似ていますが、ラベルされた枠を使います。
ラベルされた枠は、`dpart`によって生成されたものに似ていますが、
トップラインの中での名前を持ちます。

<!-- category: Programming -->
<!-- keywords: mainvar -->
<!-- signatures: mainvar -->
### Variable: mainvar

変数を`mainvar`に宣言することができます。
アトムに関する順序付けスケールは本質的に以下の通りです:
数 < 定数 (例えば、`%e`, `%pi`) < スカラー < 他の変数 < mainvars。
例えば、`(declare (x, mainvar), expand ((x+y)^4))`を伴う
`expand ((X+Y)^4)`。
（上の特長を使うことを選択したなら注意が必要なことに注意してください。
例えば、もし、
`mainvar`である`x`を含む式を、`mainvar`でない`x`を含む式から引くなら、
もし打ち消しが起こるようにするなら、
例えば`ev (expr, simp)`のような再整理が必要かもしれません。
また、`mainvar`である`x`を含む式を保存するなら、
`x`もまた保存すべきです。）

<!-- category: Programming -->
<!-- keywords: noun -->
<!-- signatures: noun -->
### Variable: noun

`noun`は、`declare`コマンドのオプションの１つです。
関数を「名詞」に宣言するのに使います。
「名詞」は、自動的には評価されないことを意味します。

See also: `declare`.

<!-- category: Programming -->
<!-- keywords: noundisp -->
<!-- signatures: noundisp -->
### Variable: noundisp

デフォルト値: `false`


`noundisp`が`true`の時、
名詞は、単一クォートで表示されます。
このスイッチは、関数定義を表示する時には、常に`true`です。

<!-- category: Programming -->
<!-- keywords: nounify -->
<!-- signatures: nounify(f) -->
### Function: nounify (f)

関数名*f*の名詞形を返します。
もし動詞関数の名前をまるで名詞のように参照したいなら、これが必要とされます。
もしある引数に関して関数が評価されないなら、
いくつかの動詞関数は名詞形を返すことに注意してください。
これは、クォートに関数コールが続く時、返される形式でもあります。


`verbify`も参照してください。

See also: `verbify`.

<!-- category: Programming -->
<!-- keywords: nterms -->
<!-- signatures: nterms(expr) -->
### Function: nterms (expr)

もし完全に展開されて、項の打ち消しや結合が起こらない場合の、*expr*が持つ
項の数を返します。
`sin (expr)`, `sqrt (expr)`, `exp (expr)`,
 などのような式は、
*expr*が（もしそれが和なら）
どんなにたくさんの項を持とうと、１項と数えます。

<!-- category: Programming -->
<!-- keywords: op -->
<!-- signatures: op(expr) -->
### Function: op (expr)

式*expr*のメインの演算子を返します。
`op (expr)`は`part (expr, 0)`と同値です。


`op`は、
もしメインの演算子が組み込みもしくはユーザー定義の前置、二項もしくはn項中置、後置、マッチフィックスもしくは無項演算子なら、文字列を返します。
そうでなければ、
もし*expr*が添字付き関数式なら、
`op`は添字付き関数を返します;
この場合、戻り値はアトムではありません。
そうでなければ、
*expr*は配列関数もしくは通常の関数式であり、
`op`はシンボルを返します。


`op`はグローバルフラグ`inflag`の値を見ています。


`op`は引数を評価します。


`args`も参照してください。


例:


















```maxima
(%i1) stringdisp: true$
(%i2) op (a * b * c);
(%o2)                          "*"
(%i3) op (a * b + c);
(%o3)                          "+"
(%i4) op ('sin (a + b));
(%o4)                          sin
(%i5) op (a!);
(%o5)                          "!"
(%i6) op (-a);
(%o6)                          "-"
(%i7) op ([a, b, c]);
(%o7)                          "["
(%i8) op ('(if a > b then c else d));
(%o8)                         "if"
(%i9) op ('foo (a));
(%o9)                          foo
(%i10) prefix (foo);
(%o10)                        "foo"
(%i11) op (foo a);
(%o11)                        "foo"
(%i12) op (F [x, y] (a, b, c));
(%o12)                        F
                               x, y
(%i13) op (G [u, v, w]);
(%o13)                          G
```

See also: `inflag`, `args`.

<!-- category: Programming -->
<!-- keywords: operatorp -->
<!-- signatures: operatorp(expr, op), operatorp(expr, [op_1, ..., op_n]) -->
### Function: operatorp (expr, op)

もし*op*が*expr*の演算子に等しければ、
`operatorp (expr, op)`は`true`を返します。


もしある要素*op_1*, ..., *op_n*が*expr*に等しければ、
`operatorp (expr, [op_1, ..., op_n])`は`true`を返します。

<!-- category: Programming -->
<!-- keywords: opsubst -->
<!-- signatures: opsubst -->
### Variable: opsubst

デフォルト値: `true`


`opsubst`が`false`の時、
`subst`は、式の中の演算子に代入を試みません。
例えば、
`(opsubst: false, subst (x^2, r, r+r[0]))`は機能します。

See also: `subst`.

<!-- category: Programming -->
<!-- keywords: optimize -->
<!-- signatures: optimize(expr) -->
### Function: optimize (expr)

*expr*と同じ値と副作用を生成する式を返しますが、
共通の部分式の再計算を避けることによってより効率的に行います。
`optimize`は、共通の部分式すべてが共用されるように引数を縮約する副作用も持ちます。
例を見るには、`example (optimize)`を実行してください。

<!-- category: Programming -->
<!-- keywords: optimprefix -->
<!-- signatures: optimprefix -->
### Variable: optimprefix

デフォルト値: `%`


`optimprefix`は`optimize`コマンドによって生成されたシンボルのために
使われる前置です。

See also: `optimize`.

<!-- category: Programming -->
<!-- keywords: ordergreat, orderless -->
<!-- signatures: ordergreat(v_1, ..., v_n), orderless(v_1, ..., v_n) -->
### Function: ordergreat (v_1, ..., v_n)

`ordergreat`は、
*v_1*が*v_2*に続き、*v_2*は、..., *v_n*に続き、
そして*v_n*は 引数として言及されなかった他の任意のシンボルに続くというように、
Maximaの式の標準の順序付けを変えます。


`orderless`は、
*v_1*が*v_2*に先行し、*v_2*は、..., *v_n*に先行し、
そして*v_n*は 引数として言及されなかった他の任意のシンボルに先行するというように、
Maximaの式の標準の順序付けを変えます。


`ordergreat`や`orderless`によって確立される順序は、
`unorder`によって解消されます。
`ordergreat`や`orderless`は、
`unorder`がコールされるまで、
それぞれ一度だけコールすることができます;
`ordergreat`の`orderless`の最後のコールだけが効果を持ちます。


`ordergreatp`も参照してください。

See also: `unorder`, `ordergreatp`.

<!-- category: Programming -->
<!-- keywords: ordergreatp, orderlessp -->
<!-- signatures: ordergreatp(expr_1, expr_2), orderlessp(expr_1, expr_2) -->
### Function: ordergreatp (expr_1, expr_2)

もしMaximaの式の標準の順序付けの中で、*expr_1*が*expr_2*に続くなら、
`ordergreatp`は、`true`を返し、
そうでなければ、`false`を返します。


もしMaximaの式の標準の順序付けの中で、*expr_1*が*expr_2*に先行するなら、
`orderlessp`は、`true`を返し、
そうでなければ、`false`を返します。


Maximaのアトムや式のすべては、`ordergreatp`と`orderlessp`の下で比較可能です。これらの述語論理が推移的でないような式の孤立した例はあるけれども; それはバグです。


アトム（シンボル、数リテラル、文字列）の標準の順序付けは以下の通りです。


(整数と浮動小数点)は以下に先行
(多倍長浮動小数点)は以下に先行
(宣言された定数)は以下に先行
(文字列)は以下に先行
(宣言されたスカラー)は以下に先行
(`orderless`の最初の引数)は以下に先行
 ...は以下に先行
(`orderless`の最後の引数)
は以下に先行
(他のシンボル)
は以下に先行
(`ordergreat`の最後の引数)は以下に先行
 ...は以下に先行
(`ordergreat`の最初の引数)は以下に先行
(宣言されたメイン変数)


アトムでない式に関して、標準の順序付けはアトムの順序付けから演繹されます。
組み込みの`+` `*` `^`演算子に関しては、
順序付けは簡単にはまとめられません。
他の組み込み演算子と他の半数や演算子、式すべてに関しては、
（最初の引数から始めて）それらの引数によって順序付けされ、
それから演算子や関数の名前によって順序付けされます。
添字付き式の場合、
添字付きのシンボルは演算子と、添字は引数と考えられます。


式の標準の順序付けは、関数`ordergreat`と`orderless`と、
`mainvar`, `constant`, `scalar`宣言によって変更されます。


`sort`も参照してください。


例:


通常のシンボルや定数の順序付け。
`%pi`は数値に従って順序付けされないことに注意してください。







```maxima
(%i1) stringdisp : true;
(%o1)                         true
(%i2) sort([%pi, 3b0, 3.0, x, X, "foo", 3, a, 4, "bar", 4.0, 4b0]);
(%o2) [3, 3.0, 4, 4.0, 3.0b0, 4.0b0, %pi, "bar", "foo", a, x, X]
```


`ordergreat`、`orderless`関数の効果。









```maxima
(%i1) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o1)           [A, E, G, H, J, K, M, P, S, T, W]
(%i2) ordergreat (S, J);
(%o2)                         done
(%i3) orderless (M, H);
(%o3)                         done
(%i4) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o4)           [M, H, A, E, G, K, P, T, W, J, S]
```


`mainvar`, `constant`, `scalar`宣言の効果










```maxima
(%i1) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o1)   [aa, bar, baz, bb, cc, dd, foo, quux, A1, B1, C1]
(%i2) declare (aa, mainvar);
(%o2)                         done
(%i3) declare ([baz, quux], constant);
(%o3)                         done
(%i4) declare ([A1, B1], scalar);
(%o4)                         done
(%i5) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o5)   [baz, quux, A1, B1, bar, bb, cc, dd, foo, C1, aa]
```


アトムでない式の順序付け








```maxima
(%i1) sort ([1, 2, n, f(1), f(2), f(2, 1), g(1), g(1, 2), g(n),
             f(n, 1)]);
(%o1) [1, 2, f(1), g(1), g(1, 2), f(2), f(2, 1), n, g(n), 
                                                         f(n, 1)]
(%i2) sort ([foo(1), X[1], X[k], foo(k), 1, k]);
(%o2)            [1, foo(1), X , k, foo(k), X ]
                              1              k
```

See also: `orderless`, `ordergreat`, `mainvar`, `constant`, `sort`.

<!-- category: Programming -->
<!-- keywords: part -->
<!-- signatures: part(expr, n_1, ..., n_k) -->
### Function: part (expr, n_1, ..., n_k)

`expr`の表示形式のパーツを返します。
`expr`の最初のパーツ*n_1*、それから、パーツ*n_2*などなど、
結果は、`expr`のパーツ*n_1*のパーツ*n_2*の, ...パーツ*n_k*です。
もし添字が指定されないなら、`expr`を返します。


`part`はリストの要素や行列の行を得るのに使うことができます。




もし`part`関数の最後の引数がインデックスのリストなら、
それぞれがリストのインデックスに対応するいくつかの部分式が抽出されます。
従って、`part (x + y + z, [1, 3])`は`z+x`です。


`piece`は、`part`関数を使ったとき、選択された最後の式を保持します。
それは関数の実行中にセットされ、以下で示すように、関数自身の中で参照されることもあります。


もし`partswitch`が`true`に設定されているなら、
式の選択されたパーツが存在しないとき、`end`が返されます。
そうでなければ、エラーメッセージが出力されます。


`inpart`, `substpart`, `substinpart`, `dpart`, `lpart`も参照してください。


例:








```maxima
(%i1) part(z+2*y+a,2);
(%o1)                                 2 y
(%i2) part(z+2*y+a,[1,3]);
(%o2)                                z + a
(%i3) part(z+2*y+a,2,1);
(%o3)                                  2
```


`example (part)`でさらに例を見ることができます。

See also: `piece`, `partswitch`, `inpart`, `substpart`, `substinpart`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: partition -->
<!-- signatures: partition(expr, x) -->
### Function: partition (expr, x)

２つの式のリストを返します。
それらは、
(1)（積なら）*expr*の因子、（和なら）*expr*項、
もしくは、（リストなら）*x*を含まないリストと、
(2)*x*を含む因子、項、リスト、
です。


例:



```maxima
(%i1) partition (2*a*x*f(x), x);
(%o1)                     [2 a, x f(x)]
(%i2) partition (a+b, x);
(%o2)                      [b + a, 0]
(%i3) partition ([a, b, f(a), c], a); 
(%o3)                  [[b, c], [a, f(a)]]
```

<!-- category: Programming -->
<!-- keywords: partswitch -->
<!-- signatures: partswitch -->
### Variable: partswitch

デフォルト値: `false`


`partswitch`が`true`の時、
式の選択された部分が存在しない時、`end`が返されます。
そうでない時は、エラーメッセージが出力されます。

<!-- category: Programming -->
<!-- keywords: pickapart -->
<!-- signatures: pickapart(expr, n) -->
### Function: pickapart (expr, n)

中間式ラベルを、深さが整数*n*での*expr*の部分式に割り当てます。
より大きなもしくは小さな深さでの部分式はラベルに割り当てられません。
`pickapart`は、元の式*expr*と同値の中間式の項による式を返します。


`part`, `dpart`, `lpart`, `inpart`, 
`reveal`も参照してください。


例:



```maxima
(%i1) expr: (a+b)/2 + sin (x^2)/3 - log (1 + sqrt(x+1));
                                          2
                                     sin(x )   b + a
(%o1)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2
(%i2) pickapart (expr, 0);

                                          2
                                     sin(x )   b + a
(%t2)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2

(%o2)                          %t2
(%i3) pickapart (expr, 1);

(%t3)                - log(sqrt(x + 1) + 1)


                                  2
                             sin(x )
(%t4)                        -------
                                3


                              b + a
(%t5)                         -----
                                2

(%o5)                    %t5 + %t4 + %t3
(%i5) pickapart (expr, 2);

(%t6)                 log(sqrt(x + 1) + 1)


                                  2
(%t7)                        sin(x )


(%t8)                         b + a

                         %t8   %t7
(%o8)                    --- + --- - %t6
                          2     3
(%i8) pickapart (expr, 3);

(%t9)                    sqrt(x + 1) + 1


                                2
(%t10)                         x

                  b + a              sin(%t10)
(%o10)            ----- - log(%t9) + ---------
                    2                    3
(%i10) pickapart (expr, 4);

(%t11)                     sqrt(x + 1)

                      2
                 sin(x )   b + a
(%o11)           ------- + ----- - log(%t11 + 1)
                    3        2

(%i11) pickapart (expr, 5);

(%t12)                        x + 1

                   2
              sin(x )   b + a
(%o12)        ------- + ----- - log(sqrt(%t12) + 1)
                 3        2
(%i12) pickapart (expr, 6);
                  2
             sin(x )   b + a
(%o12)       ------- + ----- - log(sqrt(x + 1) + 1)
                3        2
```

See also: `part`, `dpart`, `lpart`, `inpart`, `reveal`.

<!-- category: Programming -->
<!-- keywords: piece -->
<!-- signatures: piece -->
### Variable: piece

`part`関数を使った時選択された最後の式を返します。

関数の実行中に設定され、関数そのものの中で参照されることもあります。

<!-- category: Programming -->
<!-- keywords: psubst -->
<!-- signatures: psubst(list, expr), psubst(a, b, expr) -->
### Function: psubst (list, expr)

`psubst(a, b, expr)`は`subst`に似ています。
`subst`を参照してください。



`subst`とは違って、
もし最初の引数*list*が等式のリストなら、
関数`psubst`は平行代入します。


並列代入するには、`sublis`も参照してください。


例:


最初の例は、
`psubst`を使った平行代入を示します。
二番目の例は、
関数`subst`での結果を示します。それは逐次代入します。







```maxima
(%i4) psubst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o4)                           sin(b) + sin(a)
(%i5) subst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o5)                              2 sin(a)
```

See also: `sublis`.

<!-- category: Programming -->
<!-- keywords: rembox -->
<!-- signatures: rembox(expr, unlabelled), rembox(expr, label), rembox(expr) -->
### Function: rembox (expr, unlabelled)

*expr*から枠を取り除きます。


`rembox (expr, unlabelled)`は、
*expr*からラベルされていない枠すべてを取り除きます。


`rembox (expr, label)`は、
*label*を負う枠のみを取り除きます。


`rembox (expr)`は、ラベルされているか否か問わず、
枠すべてを取り除きます。


枠は、`box`, `dpart`, `lpart`関数によって描画されます。


例:












```maxima
(%i1) expr: (a*d - b*c)/h^2 + sin(%pi*x);

                                  a d - b c
(%o1)                sin(%pi x) + ---------
                                      2
                                     h

(%i2) dpart (dpart (expr, 1, 1), 2, 2);
                        """""""    a d - b c
(%o2)               sin("%pi x") + ---------
                        """""""      """"
                                     " 2"
                                     "h "
                                     """"
(%i3) expr2: lpart (BAR, lpart (FOO, %, 1), 2);
                  FOO"""""""""""   BAR""""""""
                  "    """"""" "   "a d - b c"
(%o3)             "sin("%pi x")" + "---------"
                  "    """"""" "   "  """"   "
                  """"""""""""""   "  " 2"   "
                                   "  "h "   "
                                   "  """"   "
                                   """""""""""
(%i4) rembox (expr2, unlabelled);
                                  BAR""""""""
                   FOO"""""""""   "a d - b c"
(%o4)              "sin(%pi x)" + "---------"
                   """"""""""""   "    2    "
                                  "   h     "
                                  """""""""""
(%i5) rembox (expr2, FOO);
                                  BAR""""""""
                       """""""    "a d - b c"
(%o5)              sin("%pi x") + "---------"
                       """""""    "  """"   "
                                  "  " 2"   "
                                  "  "h "   "
                                  "  """"   "
                                  """""""""""
(%i6) rembox (expr2, BAR);
                   FOO"""""""""""
                   "    """"""" "   a d - b c
(%o6)              "sin("%pi x")" + ---------
                   "    """"""" "     """"
                   """"""""""""""     " 2"
                                      "h "
                                      """"
(%i7) rembox (expr2);
                                  a d - b c
(%o7)                sin(%pi x) + ---------
                                      2
                                     h
```

See also: `box`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: reveal -->
<!-- signatures: reveal(expr, depth) -->
### Function: reveal (expr, depth)

指定された整数*depth*の*expr*の部分を
記述的な要約で
置き換えます。



- *
和と差分は、`Sum(n)`で置き換えられます。
ここで、*n*は、和のオペランドの数です。
- *
積は`Product(n)`で置き換えられます。
ここで、*n*は、積のオペランドの数です。
- *
指数は、`Expt`で置き換えられます。
- *
商は、`Quotient`で置き換えられます。
- *
単項マイナスは、`Negterm`で置き換えられます。
- *
リストは`List(n)`で置き換えられます
ここで、*n*はリストの要素の数です。


*depth*が*expr*の最大深さ以上の時、
`reveal (expr, depth)`は、*expr*をそのまま返します。


`reveal`は、引数を評価します。
`reveal`は、要約された式を返します。


例:



```maxima
(%i1) e: expand ((a - b)^2)/expand ((exp(a) + exp(b))^2);
                          2            2
                         b  - 2 a b + a
(%o1)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
(%i2) reveal (e, 1);
(%o2)                       Quotient
(%i3) reveal (e, 2);
                             Sum(3)
(%o3)                        ------
                             Sum(3)
(%i4) reveal (e, 3);

                     Expt + Negterm + Expt
(%o4)               ------------------------
                    Product(2) + Expt + Expt

(%i5) reveal (e, 4);
                       2                 2
                      b  - Product(3) + a
(%o5)         ------------------------------------
                         Product(2)     Product(2)
              2 Expt + %e           + %e
(%i6) reveal (e, 5);
                         2            2
                        b  - 2 a b + a
(%o6)              --------------------------
                       Sum(2)     2 b     2 a
                   2 %e       + %e    + %e
(%i7) reveal (e, 6);
                          2            2
                         b  - 2 a b + a
(%o7)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
```

<!-- category: Programming -->
<!-- keywords: sublis -->
<!-- signatures: sublis(list, expr) -->
### Function: sublis (list, expr)

式に対して多重平行代入を行います。
*list*は等式のリストです。
等式の左辺はアトムでなければいけません。


変数`sublis_apply_lambda`は`sublis`の後の式整理を制御します。


平行代入を行うには、`psubst`も参照してください。


例:






```maxima
(%i1) sublis ([a=b, b=a], sin(a) + cos(b));
(%o1)                    sin(b) + cos(a)
```

<!-- category: Programming -->
<!-- keywords: sublis_apply_lambda -->
<!-- signatures: sublis_apply_lambda -->
### Variable: sublis_apply_lambda

デフォルト値: `true`


`lambda`の代入が`sublis`が使われた後の式整理の中で適用されるか
、もしくは、ユーザーが、ものに適用されるように`ev`を実行しなければいけないかを決めます。
`true`は適用を意味します。

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: subnumsimp -->
<!-- signatures: subnumsimp -->
### Variable: subnumsimp

デフォルト値: `false`


もし`true`なら、シンボル`f`が与えられた時だけ、
関数`subst`と`psubst`は添字付き変数`f[x]`に数を代入できます。


`subst`も参照してください。



```maxima
(%i1) subst(100,g,g[x]+2);

subst: cannot substitute 100 for operator g in expression g
                                                           x
 -- an error. To debug this try: debugmode(true);

(%i2) subst(100,g,g[x]+2),subnumsimp:true;
(%o2)                          102
```

<!-- category: Programming -->
<!-- keywords: subst -->
<!-- signatures: subst(a, b, c) -->
### Function: subst (a, b, c)

*c*の中の*b*に*a*を代入します。
*b*はアトムもしくは*c*の完全な部分式でなければなりません。
例えば、`x+y+z`は`2*(x+y+z)`の完全な部分式である一方、`x+y`は完全な部分式ではありません。
*b*がこれらの性質を持たない時は、`substpart`もしくは`ratsubst`が使える時があります（下記参照）。
代わりに、もし*b*が`e/f`形式なら、`subst (a*f, e, c)`が使えますし、
もし*b*が`e^(1/f)`形式なら、`subst (a^f, e, c)`が使えます。
`subst`コマンドは`x^-y`の中の`x^y`も認識するので、
`subst (a, sqrt(x), 1/sqrt(x))`は`1/a`を出力します。
*a*と*b*はダブルクォート`"`で囲まれた式の演算子でも、関数名でも問題ありません。
導関数形式の独立変数に代入したいなら、`at`関数（下記参照）を使うべきです。



`subst`は`substitute`のエーリアスです。


コマンド`subst (eq_1, expr)`もしくは`subst ([eq_1, ..., eq_k], expr)`も許されている形式です。
*eq_i*はされるべき代入を指示する等式です。
それぞれの等式において、右辺が、式*expr*の中の左辺に代入されます。
等式は、*expr*に、左から右へ逐次に代入されます。
平行代入するには、関数`sublis`と`psubst`を参照してください。


`exptsubst`が`true`なら、
`%e^(a*x)`の中の`%e^x`が`y`に置き換えられるような代入が許されます。



`opsubst`が`false`の時、
`subst`は式の演算子への代入を行いません。
例えば、`(opsubst: false, subst (X^2, r, r+r[9]))`は意図通り動作します。


例:







```maxima
(%i1) subst (a, x+y, x + (x+y)^2 + y);
                                    2
(%o1)                      y + x + a
(%i2) subst (-%i, %i, a + b*%i);
(%o2)                       a - %i b
```


代入は、等式のリストに関して逐次になされます。
これを並列代入と比較してください。







```maxima
(%i3) subst([a=b, b=c], a+b);
(%o3)                                 2 c
(%i4) sublis([a=b, b=c], a+b);
(%o4)                                c + b
```



もっと例を見るには、`example (subst)`を実行してください。

See also: `substpart`, `ratsubst`, `exptsubst`.

<!-- category: Programming -->
<!-- keywords: substinpart -->
<!-- signatures: substinpart(x, expr, n_1, ..., n_k) -->
### Function: substinpart (x, expr, n_1, ..., n_k)

`substpart`と同様ですが、`substinpart`は*expr*の内部表現上で
働きます。


例:








```maxima
(%i1) x . 'diff (f(x), x, 2);
                              2
                             d
(%o1)                   x . (--- (f(x)))
                               2
                             dx
(%i2) substinpart (d^2, %, 2);
                                  2
(%o2)                        x . d
(%i3) substinpart (f1, f[1](x + 1), 0);
(%o3)                       f1(x + 1)
```


もし`part`関数の最後の引数がインデックスのリストなら、
複数の部分式が選ばれます。それぞれはリストのインデックスに対応します。
例えば、






```maxima
(%i1) part (x + y + z, [1, 3]);
(%o1)                         z + x
```


`part`関数を使った時、`piece`は、最後の式の値を保持します。
関数の実行の間に設定され、以下で示すように関数自身の中で参照されることもあります。
もし`partswitch`が`true`に設定されたら、
式の選択された部分が存在しない時には`end`が返されます。
そうでなければ、エラーメッセージが出力されます。











```maxima
(%i1) expr: 27*y^3 + 54*x*y^2 + 36*x^2*y + y + 8*x^3 + x + 1;
              3         2       2            3
(%o1)     27 y  + 54 x y  + 36 x  y + y + 8 x  + x + 1
(%i2) part (expr, 2, [1, 3]);
                                  2
(%o2)                         54 y
(%i3) sqrt (piece/54);
(%o3)                        abs(y)
(%i4) substpart (factor (piece), expr, [1, 2, 3, 5]);
                               3
(%o4)               (3 y + 2 x)  + y + x + 1
(%i5) expr: 1/x + y/x - 1/z;
                             1   y   1
(%o5)                      - - + - + -
                             z   x   x
(%i6) substpart (xthru (piece), expr, [2, 3]);
                            y + 1   1
(%o6)                       ----- - -
                              x     z
```


また、
オプション `inflag`を `true`に設定し
`part`か `substpart`をコールすることは
`inpart`か `substinpart`をコールすることと同じです。

See also: `substpart`, `piece`, `partswitch`, `inflag`, `part`.

<!-- category: Programming -->
<!-- keywords: substpart -->
<!-- signatures: substpart(x, expr, n_1, ..., n_k) -->
### Function: substpart (x, expr, n_1, ..., n_k)

*x*を、残りの引数を`part`に食わせた結果の部分式に代入します。
*expr*の新しい値を返します。
*x*は*expr*の演算子に代入される演算子でも問題ありません。
いくつかの場合、*x*はダブルクォート`"`で囲まれる必要があります。
（例えば、`substpart ("+", a*b, 0)`は`b + a`を返します。）


例:









```maxima
(%i1) 1/(x^2 + 2);
                               1
(%o1)                        ------
                              2
                             x  + 2
(%i2) substpart (3/2, %, 2, 1, 2);
                               1
(%o2)                       --------
                             3/2
                            x    + 2
(%i3) a*x + f(b, y);
(%o3)                     a x + f(b, y)
(%i4) substpart ("+", %, 1, 0);
(%o4)                    x + f(b, y) + a
```


また、オプション`inflag`を`true`に設定し、
`part`や`substpart`をコールすることは、
`inpart`や`substinpart`をコールすることと同じになります。

See also: `inflag`, `part`, `substinpart`.

<!-- category: Programming -->
<!-- keywords: symbolp -->
<!-- signatures: symbolp(expr) -->
### Function: symbolp (expr)

もし*expr*がシンボルなら`true`、そうでないなら`false`を返します。
事実上、`symbolp(x)`は、述語論理`atom(x) and not numberp(x)`と同値です。




`Identifiers`も参照してください。

See also: `Identifiers`.

<!-- category: Programming -->
<!-- keywords: unorder -->
<!-- signatures: unorder() -->
### Function: unorder ()

順序付けコマンド`ordergreat`と`orderless`の最後の使用で生成されたエーリアシングを使用不可にします。
`ordergreat`と`orderless`は、
`unorder`を呼び出さずに、一回以上使えないかもしれません。
`unorder`は、
`ordergreat`と`orderless`で導入されたエーリアスに
元のシンボルを式に再代入しません。
それ故に、`unorder`の実行後、以前の式にエーリアスが現れます。

 

`ordergreat`と`orderless`も参照してください。


例s:


`ordergreat(a)`はシンボル`a`のエーリアスを導入します。
それ故に、
`%o2`と`%o4`の違いは消えません。
`unorder`はシンボル`a`を再代入しないし、
出力`%o7`にエーリアスが現れます。












```maxima
(%i1) unorder();
(%o1)                          []
(%i2) b*x+a^2;
                                   2
(%o2)                       b x + a
(%i3) ordergreat(a);
(%o3)                         done
(%i4) b*x+a^2;
                             2
(%o4)                       a  + b x
(%i5) %th(1)-%th(3);
                              2    2
(%o5)                        a  - a
(%i6) unorder();
(%o6)                          [a]
(%i7) %th(2);
                                2    2
(%o7)                      _101a  - a
```

<!-- category: Programming -->
<!-- keywords: verbify -->
<!-- signatures: verbify(f) -->
### Function: verbify (f)

関数名*f*の動詞形を返します。
`verb`, `noun`, `nounify`も参照してください。


例:









```maxima
(%i1) verbify ('foo);
(%o1)                          foo
(%i2) :lisp $%
$FOO
(%i2) nounify (foo);
(%o2)                          foo
(%i3) :lisp $%
%FOO
```

