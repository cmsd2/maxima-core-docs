## Differentiation

<!-- category: Calculus -->
<!-- keywords: antid -->
<!-- signatures: antid(expr, x, u(x)) -->
### Function: antid (expr, x, u(x))

*expr*の*x*に関する不定積分がリストから構成できるような、
２要素リストを返します。
式*expr*は、未知の関数*u*とその導関数を含むことができます。


Let 
２要素リスト*L*が`antid`の戻り値だとします。
`L[1] + 'integrate (L[2], x)`は
*expr*の*x*に関する不定積分です。


`antid`が完全に成功した時、
戻り値の２番目の要素はゼロです。
そうでなければ、２番目の要素は非ゼロで、最初の要素は非ゼロまたはゼロです。
もし`antid`が全く進展できなければ、
最初の要素はゼロで、２番目は非ゼロです。


`load ("antid")`はこの関数をロードします。
`antid`パッケージは、関数`nonzeroandfreeof`と`linear`も定義します。


`antid`は、以下のように`antidiff`と関係します。
２要素リスト*L*が`antid`の戻り値とします。
`antidiff`の戻り値は、`L[1] + 'integrate (L[2], x)`に
等しいです。
ここで、*x*は積分変数です。


例:














```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

<!-- category: Calculus -->
<!-- keywords: antidiff -->
<!-- signatures: antidiff(expr, x, u(x)) -->
### Function: antidiff (expr, x, u(x))

*expr*の*x*に関する不定積分を返します。
式*expr*は、未知の関数*u*とその導関数を含むことができます。


`antidiff`が完全に成功した時、
結果の式は、積分記号を含みません(すなわち、`integrate`名詞を含みません)。
そうでなければ、`antidiff`は
部分的にまたは完全に積分記号内にある式を返します。
もし`antidiff`が全く進展ができないなら、
戻り値は完全に積分記号内にあります。


`load ("antid")`はこの関数をロードします。
`antid`パッケージは、関数`nonzeroandfreeof`と`linear`も定義します。


`antidiff`は、以下のように`antid`と関係します。
２要素リスト*L*が`antid`の戻り値とします。
`antidiff`の戻り値は、`L[1] + 'integrate (L[2], x)`に
等しいです。
ここで、*x*は積分変数です。


例:














```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

<!-- category: Calculus -->
<!-- keywords: at -->
<!-- signatures: at(expr, [eqn_1, ..., eqn_n]), at(expr, eqn) -->
### Function: at (expr, [eqn_1, ..., eqn_n])

等式のリスト`[eqn_1, ..., eqn_n]`
もしくは１つの等式*eqn*の中で指定されたように値を仮定された変数で、
式*expr*を評価します。


もしも部分式が、値が指定される変数のいずれかに依存するが
指定の`atvalue`がなく、他の方法で評価できないなら、
`at`の名詞形が返され、２次元形式で表示されます。


`at`は多重代入を並列に実行します。


`atvalue`も参照してください。
代入を実行する他の関数に関しては、`subst`や`ev`も参照してください。


例:










```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x, y)^2 - u(x, y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);

                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

<!-- category: Calculus -->
<!-- keywords: atomgrad -->
<!-- signatures: atomgrad -->
### Variable: atomgrad

`atomgrad`は、式のアトムのグラディエントプロパティです。
このプロパティは`gradef`で割り当てられます。

<!-- category: Calculus -->
<!-- keywords: atvalue -->
<!-- signatures: atvalue(expr, [x_1=a_1, ..., x_m=a_m], c), atvalue(expr, x_1=a_1, c) -->
### Function: atvalue (expr, [x_1=a_1, ..., x_m=a_m], c)

値*c*を
点`x = a`の*expr*に割り当てます。
典型的には、境界値はこのメカニズムによって確立されます。


*expr*は、関数引数が陽に現れる
関数評価
`f(x_1, ..., x_m)`または
導関数
`diff (f(x_1, ..., x_m), x_1, n_1, ..., x_n, n_m)`
です。


*n_i*は、*x_i*に関する微分の階数です。


atvalueが確立される点は、等式のリスト`[x_1 = a_1, ..., x_m = a_m]`
によって与えられます。
もし１変数*x_1*なら、
リストとしてくくられることなしに１つの等式は与えられます。


`printprops ([f_1, f_2, ...], atvalue)`は
`atvalue`コールによって指定されるような
関数`f_1, f_2, ...`のatvalueを表示します。


`printprops (f, atvalue)`は、
１関数*f*のatvalueを表示します。
`printprops (all, atvalue)`は、
atvaluesが定義された関数すべてのatvalueを表示します。


atvaluesが表示される時、
シンボル`@1`, `@2`, ... は
変数*x_1*, *x_2*, ...を表します。


`atvalue`は引数を評価します。
`atvalue`はatvalue*c*を返します。


例:









```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x,y)^2 - u(x,y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);
                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

<!-- category: Calculus -->
<!-- keywords: cartan -->
<!-- signatures: cartan -->
### Function: cartan

微分形式の外積代数は
エリーカルタンによって開発された微分幾何の基本ツールであり、
偏微分方程式論での有用な応用を持ちます。
`cartan`パッケージは、
演算子`~` (ウェッジ積)と`|` (形式のベクトルとの縮約)と一緒に、
関数`ext_diff`と`lie_diff`を実装します。
例と一緒にこれらのコマンドの簡潔な記述を見るには、`demo (tensor)`を実行してください。


`cartan`は、F.B. EstabrookとH.D. Wahlquistによって実装されました。

<!-- category: Calculus -->
<!-- keywords: del -->
<!-- signatures: del(x) -->
### Function: del (x)

`del (x)`は、変数$x$の微分を表します。


もし独立変数が指定されないなら、
`diff`は、`del`を含む式を返します。
この場合、戻り値は「全微分」と呼ばれるものです。


例:







```maxima
(%i1) diff (log (x));
                             del(x)
(%o1)                        ------
                               x
(%i2) diff (exp (x*y));
                     x y              x y
(%o2)            x %e    del(y) + y %e    del(x)
(%i3) diff (x*y*z);
(%o3)         x y del(z) + x z del(y) + y z del(x)
```

<!-- category: Calculus -->
<!-- keywords: delta -->
<!-- signatures: delta(t) -->
### Function: delta (t)

Diracのデルタ関数


今のところ、`laplace`だけが`delta`を知っています。


例:



```maxima
(%i1) laplace (delta (t - a) * sin(b*t), t, s);
Is  a  positive, negative, or zero?

p;
                                   - a s
(%o1)                   sin(a b) %e
```

<!-- category: Calculus -->
<!-- keywords: dependencies -->
<!-- signatures: dependencies -->
### Variable: dependencies

デフォルト値: `[]`


`dependencies`は、
`depends`や`gradef`によって割り当てられた、関数依存を持つアトムのリストです。
`dependencies`リストは累積的です:
each call to 
`depends`や`gradef`のコールそれぞれは、上乗せの項目を追加します。


`depends`と`gradef`を参照してください。

<!-- category: Calculus -->
<!-- keywords: depends -->
<!-- signatures: depends(f_1, x_1, ..., f_n, x_n) -->
### Function: depends (f_1, x_1, ..., f_n, x_n)

導関数を計算するために、変数の間の関数依存を宣言します。
宣言された依存関係なしでは、
`diff (f, x)`はゼロをもたらします。
もし`depends (f, x)`が宣言されたら、
`diff (f, x)`はシンボリックな導関数(すなわち、`diff`名詞)をもたらします。


それぞれの引数*f_1*, *x_1*, などは、
変数や配列の名前、または名前のリストをとり得ます。
*f_i* (多分ただ１つの要素)のすべての要素は、
*x_i* (多分ただ１つの要素)のすべての要素に依存するように宣言されます。
もしいくつかの*f_i*が、配列名だったり、配列名を含むなら、
配列の要素すべては*x_i*に依存します。


`diff`は、`depends`によって確立された間接的依存関係を認識し、
これらの場合に連鎖規則を適用します。


`remove (f, dependency)`は、*f*に関して宣言された
依存関係すべてを取り除きます。


`depends`は、確立された依存関係のリストを返します。
依存関係はグローバル変数`dependencies`に適用されます。
`depends`は引数を評価します。


`diff`は、
`depends`によって確立された依存関係を認識する唯一のMaximaコマンドです。
他の関数(`integrate`, `laplace`, など)は、
引数によって陽に表現された依存関係だけを認識します。
例えば、`integrate`は、
`integrate (f(x), x)`のように陽に表現されないなら、
`f`の`x`への依存性を認識しません。









```maxima
(%i1) depends ([f, g], x);
(%o1)                     [f(x), g(x)]
(%i2) depends ([r, s], [u, v, w]);
(%o2)               [r(u, v, w), s(u, v, w)]
(%i3) depends (u, t);
(%o3)                        [u(t)]
(%i4) dependencies;
(%o4)      [f(x), g(x), r(u, v, w), s(u, v, w), u(t)]
(%i5) diff (r.s, u);
                         dr           ds
(%o5)                    -- . s + r . --
                         du           du
```





```maxima
(%i6) diff (r.s, t);
                      dr du           ds du
(%o6)                 -- -- . s + r . -- --
                      du dt           du dt
```






```maxima
(%i7) remove (r, dependency);
(%o7)                         done
(%i8) diff (r.s, t);
                                ds du
(%o8)                       r . -- --
                                du dt
```

<!-- category: Calculus -->
<!-- keywords: derivabbrev -->
<!-- signatures: derivabbrev -->
### Variable: derivabbrev

デフォルト値: `false`


`derivabbrev`が`true`の時、
シンボリックな導関数(すなわち、`diff`名詞)が下付き添字として表示されます。
そうでなければ、導関数はライプニッツ表記`dy/dx`で表示されます。

<!-- category: Calculus -->
<!-- keywords: derivdegree -->
<!-- signatures: derivdegree(expr, y, x) -->
### Function: derivdegree (expr, y, x)

*expr*に現れる独立変数*x*に関する
従属変数*y*の微分の最高階数を返します。


例:






```maxima
(%i1) 'diff (y, x, 2) + 'diff (y, z, 3) + 'diff (y, x) * x^2;
                         3     2
                        d y   d y    2 dy
(%o1)                   --- + --- + x  --
                          3     2      dx
                        dz    dx
(%i2) derivdegree (%, y, x);
(%o2)                           2
```

<!-- category: Calculus -->
<!-- keywords: derivlist -->
<!-- signatures: derivlist(var_1, ..., var_k) -->
### Function: derivlist (var_1, ..., var_k)

`ev`コマンド内にて、指摘された変数に関する微分のみを起こします。

<!-- category: Calculus -->
<!-- keywords: derivsubst -->
<!-- signatures: derivsubst -->
### Variable: derivsubst

デフォルト値: `false`


`derivsubst`が`true`の時、
`subst (x, 'diff (y, t), 'diff (y, t, 2))`
のような非構文法的代入は`'diff (x, t)`をもらします。

<!-- category: Calculus -->
<!-- keywords: diff -->
<!-- signatures: diff(expr, x_1, n_1, ..., x_m, n_m), diff(expr, x, n), diff(expr, x), diff(expr) -->
### Function: diff (expr, x_1, n_1, ..., x_m, n_m)

*expr*の中のすべての変数の中のいくつかに関する、*expr*の導関数すなわち微分を返します。


`diff (expr, x, n)`は*x*に関する*expr*の*n*階微分を返します。


`diff (expr, x_1, n_1, ..., x_m, n_m)`は
*x_1*, ..., *x_m*に関する*expr*の偏微分を返します。
これは、`diff (... (diff (expr, x_m, n_m) ...), x_1, n_1)`と同値です。


`diff (expr, x)`は変数*x*に関する*expr*の1階微分を返します。


`diff (expr)`は*expr*の全微分を返します。
すなわち、それぞれの変数に関する*expr*の微分に変数それぞれの微分`del`を掛けたものの和を返します。

`del`の更なる整理は提供されません。


`diff`の名詞形式が、微分方程式を記述する時など、いくつかの文脈で要求されます。
これらの場合、`diff`は、微分が実行される代わりに名詞形式を出力するために
(`'diff`として)クォートされるかもしれません。


`derivabbrev`が`true`の時、導関数は下付き添字として表示されます。
そうでなければ、導関数はライブニツ記法の`dy/dx`で表示されます。


例:








```maxima
(%i1) diff (exp (f(x)), x, 2);
                     2
              f(x)  d               f(x)  d         2
(%o1)       %e     (--- (f(x))) + %e     (-- (f(x)))
                      2                   dx
                    dx
(%i2) derivabbrev: true$
(%i3) 'integrate (f(x, y), y, g(x), h(x));
                         h(x)
                        /
                        [
(%o3)                   I     f(x, y) dy
                        ]
                        /
                         g(x)
(%i4) diff (%, x);
       h(x)
      /
      [
(%o4) I     f(x, y)  dy + f(x, h(x)) h(x)  - f(x, g(x)) g(x)
      ]            x                     x                  x
      /
       g(x)
```


テンソルパッケージのために、以下の変更が取り込まれています:


(1) *expr*の中の任意のインデックスされたオブジェクトの導関数は、追加された引数として添えられた変数*x_i*を持ちます。
そして導関数のインデックスはすべてソートされます。


(2) *x_i*は、1から変数`dimension` [デフォルト値: 4]の値までの整数を取ります。
これにより、例えば `[x, y, z, t]`など
座標名のリストして設定されたリスト`coordinates`の*x_i*番目のメンバーに関する微分が実行されます。
もし`coordinates`がアトムの変数にバインドされているなら、*x_i*で下付き添字された変数が、微分の変数として使われます。
これにより、座標名や`X[1]`, `X[2]`, ...のような下付き添字された名前の配列が使えることになります。
もし`coordinates`に値が割り当てられていないなら、変数は上の(1)のように扱われます。

<!-- category: Calculus -->
<!-- keywords: dscalar -->
<!-- signatures: dscalar(f) -->
### Function: dscalar (f)

スカラーのダランベルシアンをスカラー関数に*f*に適用します。




`load ("ctensor")`はこの関数をロードします。

<!-- category: Calculus -->
<!-- keywords: express -->
<!-- signatures: express(expr) -->
### Function: express (expr)

微分演算子名詞を偏微分を使った式に展開します。
`express`は、演算子`grad`, `div`, `curl`, `laplacian`を
認識します。
`express`は、外積`~`も展開します。


expressの戻り値の中のシンボリックな導関数(すなわち、`diff`名詞)は、
`ev`関数コールまたはコマンドラインに`diff`を含むことによって、評価されることができます。
この文脈では、`diff`は`evfun`として振る舞います。


`load ("vect")`はこの関数をロードします。



例:



















```maxima
(%i1) load ("vect")$
(%i2) grad (x^2 + y^2 + z^2);
                              2    2    2
(%o2)                  grad (z  + y  + x )
(%i3) express (%);
       d    2    2    2   d    2    2    2   d    2    2    2
(%o3) [-- (z  + y  + x ), -- (z  + y  + x ), -- (z  + y  + x )]
       dx                 dy                 dz
(%i4) ev (%, diff);
(%o4)                    [2 x, 2 y, 2 z]
(%i5) div ([x^2, y^2, z^2]);
                              2   2   2
(%o5)                   div [x , y , z ]
(%i6) express (%);
                   d    2    d    2    d    2
(%o6)              -- (z ) + -- (y ) + -- (x )
                   dz        dy        dx
(%i7) ev (%, diff);
(%o7)                    2 z + 2 y + 2 x
(%i8) curl ([x^2, y^2, z^2]);
                               2   2   2
(%o8)                   curl [x , y , z ]
(%i9) express (%);
       d    2    d    2   d    2    d    2   d    2    d    2
(%o9) [-- (z ) - -- (y ), -- (x ) - -- (z ), -- (y ) - -- (x )]
       dy        dz       dz        dx       dx        dy
(%i10) ev (%, diff);
(%o10)                      [0, 0, 0]
(%i11) laplacian (x^2 * y^2 * z^2);
                                  2  2  2
(%o11)                laplacian (x  y  z )
(%i12) express (%);
         2                2                2
        d     2  2  2    d     2  2  2    d     2  2  2
(%o12)  --- (x  y  z ) + --- (x  y  z ) + --- (x  y  z )
          2                2                2
        dz               dy               dx
(%i13) ev (%, diff);
                      2  2      2  2      2  2
(%o13)             2 y  z  + 2 x  z  + 2 x  y
(%i14) [a, b, c] ~ [x, y, z];
(%o14)                [a, b, c] ~ [x, y, z]
(%i15) express (%);
(%o15)          [b z - c y, c x - a z, a y - b x]
```

<!-- category: Calculus -->
<!-- keywords: gradef -->
<!-- signatures: gradef(f(x_1, ..., x_n), g_1, ..., g_m), gradef(a, x, expr) -->
### Function: gradef (f(x_1, ..., x_n), g_1, ..., g_m)

関数*f*もしくは変数*a*の偏微分（すなわち、勾配の成分）を定義します。


`gradef (f(x_1, ..., x_n), g_1, ..., g_m)`は、
`df/dx_i`を*g_i*として定義します。
ここで、*g_i*は式です; *g_i*は関数コールでもあり得ますが、関数名ではありません。
偏微分の数*m*は、引数の数*n*よりもちいさいかもしれません。
その場合、微分は*x_1*から*x_m*までのみに関して定義されます。


`gradef (a, x, expr)`は、
変数*a*の*x*に関する微分を*expr*と定義します。
これは、 (`depends (a, x)`を介して)
*a*の*x*への依存性を確立もします。


最初の引数`f(x_1, ..., x_n)`または*a*はクォートされますが、
残りの引数*g_1*, ..., *g_m*は評価されます。
`gradef`は偏微分が定義された関数や変数を返します。


`gradef`は、Maximaの組み込み関数の微分を再定義できます。
例えば、`gradef (sin(x), sqrt (1 - sin(x)^2))`は、
`sin`の微分を再定義します。


`gradef`は、添字付き関数の偏微分を定義できません。


`printprops ([f_1, ..., f_n], gradef)`は、
関数*f_1*, ..., *f_n*の偏微分を
`gradef`で定義されたように、表示します。


`printprops ([a_n, ..., a_n], atomgrad)`は、
変数*a_n*, ..., *a_n*の偏微分を
`gradef`で定義されたように、表示します。


`gradefs`は、偏微分が`gradef`によって定義された
関数のリストです。
`gradefs`は、
偏微分が`gradef`によって定義されたいかなる変数も含みません。



例えば、関数が陽に知られていないが、一階微分が知られていて、
高階の微分を得ることが望まれる時、勾配が必要です。

<!-- category: Calculus -->
<!-- keywords: gradefs -->
<!-- signatures: gradefs -->
### Variable: gradefs

デフォルト値: `[]`


`gradefs`は、偏微分が`gradef`によって定義された
関数のリストです。
`gradefs`は、
偏微分が`gradef`によって定義されたいかなる変数も含みません。

<!-- category: Calculus -->
<!-- keywords: laplace -->
<!-- signatures: laplace(expr, t, s) -->
### Function: laplace (expr, t, s)

変数*t*に関するラブラス変換*expr*を計算し、パラメータ*s*に変換しようとします。


`laplace`は、
*expr*の中で、
`derivative`, `integrate`, `sum`, `ilt`はもちろん、
関数`delta`, `exp`,
`log`, `sin`, `cos`, `sinh`, `cosh`, and `erf`
を認識します。
もし、laplaceが変換を見つけられなかったら、
関数`specint`がコールされます。
`specint`は、
ベッセル関数`bessel_j`, `bessel_i`, ...のような
特殊関数を含む式のラプラス変換を見つけることができ、
`unit_step`関数を扱うことができます。
`specint`も参照してください。


もし`specint`も解を見つけられないなら、
名詞`laplace`が返されます。



*expr*は、従属変数の`atvalue`が使われる線形定数係数微分方程式であるかもしれません。

要求されるatvalueは、
変換が計算される前か後に供給されるかもしれません。
初期条件がゼロで指定されなければいけないので、
もし他に課される境界条件を持つなら
一般解にそれらを課すことができ、それらに関して一般解を解き、それらの値を代入し返すことによって、
定数を消去できます。


`laplace`は、形式
`integrate (f(x) * g(t - x), x, 0, t)`の畳み込み積分を認識します;
他の種類の畳み込みは認識されません。


関数関係は、 *expr*で陽に表現されなければいけません;
`depends`で確立した暗黙の関係は認識されません。
例えば、もし*f*が*x*と*y*に依存するなら、
`f (x, y)`が*expr*の中に現れなければいけません。


逆ラプラス変換`ilt`も参照してください。


例:








```maxima
(%i1) laplace (exp (2*t + a) * sin(t) * t, t, s);
                            a
                          %e  (2 s - 4)
(%o1)                    ---------------
                           2           2
                         (s  - 4 s + 5)
(%i2) laplace ('diff (f (x), x), x, s);
(%o2)             s laplace(f(x), x, s) - f(0)
(%i3) diff (diff (delta (t), t), t);
                          2
                         d
(%o3)                    --- (delta(t))
                           2
                         dt
(%i4) laplace (%, t, s);
                            !
               d            !         2
(%o4)        - -- (delta(t))!      + s  - delta(0) s
               dt           !
                            !t = 0
(%i5) assume(a>0)$
(%i6) laplace(gamma_incomplete(a,t),t,s),gamma_expand:true;
                                              - a - 1
                         gamma(a)   gamma(a) s
(%o6)                    -------- - -----------------
                            s            1     a
                                        (- + 1)
                                         s
(%i7) factor(laplace(gamma_incomplete(1/2,t),t,s));
                                              s + 1
                      sqrt(%pi) (sqrt(s) sqrt(-----) - 1)
                                                s
(%o7)                 -----------------------------------
                                3/2      s + 1
                               s    sqrt(-----)
                                           s
(%i8) assume(exp(%pi*s)>1)$
(%i9) laplace(sum((-1)^n*unit_step(t-n*%pi)*sin(t),n,0,inf),t,s),
         simpsum;

                         %i                         %i
              ------------------------ - ------------------------
                              - %pi s                    - %pi s
              (s + %i) (1 - %e       )   (s - %i) (1 - %e       )
(%o9)         ---------------------------------------------------
                                       2

(%i9) factor(%);
                                      %pi s
                                    %e
(%o9)                   -------------------------------
                                             %pi s
                        (s - %i) (s + %i) (%e      - 1)
```

