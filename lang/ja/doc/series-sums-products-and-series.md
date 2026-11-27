## Sums, Products, and Series

<!-- category: Series -->
<!-- keywords: bashindices -->
<!-- signatures: bashindices(expr) -->
### Function: bashindices (expr)

それぞれの和や積に独自のインデックスを与えることで、
式*expr*を変換します。
これは、
和や積と一緒に機能する時
`changevar`によりよい精度を与えます。
独自のインデックスの形式は`jnumber`です。
量*number*は、`gensumnum`に参照することで決定されます。
これを、ユーザーは変更することができます。
例えば、`gensumnum:0$`はそれを再設定します。

<!-- category: Series -->
<!-- keywords: cauchysum -->
<!-- signatures: cauchysum -->
### Variable: cauchysum

デフォルト値: `false`



上限として`inf`を持つ和同士を掛ける時、
もし`sumexpand`が`true`、かつ、`cauchysum`が`true`なら、
通常の積ではなくCauchy積が使われます。
Cauchy積では、
内側の和のインデックスは、独立に変化するのではなく、外側のインデックスの関数です。


例:



```maxima
(%i1) sumexpand: false$
(%i2) cauchysum: false$
(%i3) s: sum (f(i), i, 0, inf) * sum (g(j), j, 0, inf);
                      inf         inf
                      ====        ====
                      \           \
(%o3)                ( >    f(i))  >    g(j)
                      /           /
                      ====        ====
                      i = 0       j = 0
(%i4) sumexpand: true$
(%i5) cauchysum: true$
(%i6) ''s;
                 inf     i1
                 ====   ====
                 \      \
(%o6)             >      >     g(i1 - i2) f(i2)
                 /      /
                 ====   ====
                 i1 = 0 i2 = 0
```

<!-- category: Series -->
<!-- keywords: deftaylor -->
<!-- signatures: deftaylor(f_1(x_1), expr_1, ..., f_n(x_n), expr_n) -->
### Function: deftaylor (f_1(x_1), expr_1, ..., f_n(x_n), expr_n)

`deftaylor`は、
ある変数*x_i*の関数*f_i*それぞれに関して、
*expr_i*をゼロの回りのTaylor級数と定義します。
*expr_i*は、典型的には、*x_i*の多項式か和です;
`deftaylor`は、もっと一般的な式も問題なく受け付けます。


`powerseries (f_i(x_i), x_i, 0)`は、
`deftaylor`で定義された級数を返します。


`deftaylor`は、
関数*f_1*, ..., *f_n*のリストを返します。
`deftaylor`は、引数を評価します。


例:



```maxima
(%i1) deftaylor (f(x), x^2 + sum(x^i/(2^i*i!^2), i, 4, inf));
(%o1)                          [f]
(%i2) powerseries (f(x), x, 0);
                      inf
                      ====      i1
                      \        x         2
(%o2)                  >     -------- + x
                      /       i1    2
                      ====   2   i1!
                      i1 = 4
(%i3) taylor (exp (sqrt (f(x))), x, 0, 4);
                      2         3          4
                     x    3073 x    12817 x
(%o3)/T/     1 + x + -- + ------- + -------- + . . .
                     2     18432     307200
```

<!-- category: Series -->
<!-- keywords: intopois -->
<!-- signatures: intopois(a) -->
### Function: intopois (a)

*a*をPoisson符号に変換します。

<!-- category: Series -->
<!-- keywords: intosum -->
<!-- signatures: intosum(expr) -->
### Function: intosum (expr)

和の外側の掛け算因子を内側に移動します。
もし外側の式でインデックスが使われているなら、
関数は、`sumcontract`に関してするのと同じように、合理的なインデックスを見つけようとします。
これは、本質的に、和の`outative`プロパティの逆の考えですが、
このプロパティを取り除かず、ただ無視するだけであることに注意してください。



いくつかの場合、
`intosum`の前に、`scanmap (multthru, expr)`が必要になるかもしれません。

<!-- category: Series -->
<!-- keywords: lsum -->
<!-- signatures: lsum(expr, x, L) -->
### Function: lsum (expr, x, L)

*L*の中のそれぞれの要素*x*に関する*expr*の和を表します。
もし引数*L*がリストに評価されなければ、名詞形`'lsum`が返されます。


例:







```maxima
(%i1) lsum (x^i, i, [1, 2, 7]);
                            7    2
(%o1)                      x  + x  + x
(%i2) lsum (i^2, i, rootsof (x^3 - 1, x));

                     ====
                     \      2
(%o2)                 >    i
                     /
                     ====
                                   3
                     i in rootsof(x  - 1, x)
```

<!-- category: Series -->
<!-- keywords: maxtayorder -->
<!-- signatures: maxtayorder -->
### Variable: maxtayorder

デフォルト値: `true`



`maxtayorder`が`true`の時、
(切り詰められた)Taylor級数の代数操作の間、
`taylor`は、厳密とわかっているできるだけ多くの項を保とうとします。

<!-- category: Series -->
<!-- keywords: niceindices -->
<!-- signatures: niceindices(expr) -->
### Function: niceindices (expr)

*expr*の中の和や積のインデックスを改名します。
`niceindices`は、
その名前が被加数や非積数の中に現れないなら、
インデックスそれぞれを`niceindicespref[1]`の値に改名しようとします。
現れた場合、
`niceindices`は、
未使用の変数が見つかるまで`niceindicespref`の次の要素を順に試します。
もしリスト全部が使い果たされたら、
例えば, `i0`, `i1`, `i2`, ....というように、
`niceindicespref[1]`の値に整数を追加することで、
追加のインデックスが構成されます。


`niceindices`は式を返します。
`niceindices`は引数を評価します。


例:



```maxima
(%i1) niceindicespref;
(%o1)                  [i, j, k, l, m, n]
(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o2)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1
(%i3) niceindices (%);

                     inf  inf
                    /===\ ====
                     ! !  \
(%o3)                ! !   >    f(i j l + k)
                     ! !  /
                    l = 1 ====
                          k = 1
```

<!-- category: Series -->
<!-- keywords: niceindicespref -->
<!-- signatures: niceindicespref -->
### Variable: niceindicespref

デフォルト値: `[i, j, k, l, m, n]`


`niceindicespref`は、
`niceindices`が和や積のインデックスの名前を取ってくる
リストです。


The elements of 
`niceindicespref`の要素は、
`niceindices`によって強制されませんが、
通常、変数名です。


例:



```maxima
(%i1) niceindicespref: [p, q, r, s, t, u]$
(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o2)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1
(%i3) niceindices (%);
                     inf  inf
                    /===\ ====
                     ! !  \
(%o3)                ! !   >    f(i j q + p)
                     ! !  /
                    q = 1 ====
                          p = 1
```

<!-- category: Series -->
<!-- keywords: nusum -->
<!-- signatures: nusum(expr, x, i_0, i_1) -->
### Function: nusum (expr, x, i_0, i_1)

R.W. Gosperによる決定手続きを使って、
*x*に関する*expr*の不定超幾何総和を実行します。
*expr*と結果は、
整数べき、階乗、二項式、有理関数の積として表現可能でなければいけません。




用語「定」と「不定和」は、
「定」と「不定積分」へ類似して使われています。
不定に和を取ることは、
ただ、例えば0からinfまででなく、
変数の長さの区間上の和に関して、シンボリックな結果を与えることを意味します。
例えば、二項級数の一般的な部分和に関する公式はないので、
`nusum`はそれができません。


`nusum`と`unsum`は、有限積の和と差について少し知っています。
`unsum`も参照してください。


例:



```maxima
(%i1) nusum (n*n!, n, 0, n);

Dependent equations eliminated:  (1)
(%o1)                     (n + 1)! - 1
(%i2) nusum (n^4*4^n/binomial(2*n,n), n, 0, n);
                     4        3       2              n
      2 (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3) 4      2
(%o2) ------------------------------------------------ - ------
                    693 binomial(2 n, n)                 3 11 7
(%i3) unsum (%, n);
                              4  n
                             n  4
(%o3)                   ----------------
                        binomial(2 n, n)
(%i4) unsum (prod (i^2, i, 1, n), n);
                    n - 1
                    /===\
                     ! !   2
(%o4)              ( ! !  i ) (n - 1) (n + 1)
                     ! !
                    i = 1
(%i5) nusum (%, n, 1, n);

Dependent equations eliminated:  (2 3)
                            n
                          /===\
                           ! !   2
(%o5)                      ! !  i  - 1
                           ! !
                          i = 1
```

<!-- category: Series -->
<!-- keywords: outofpois -->
<!-- signatures: outofpois(a) -->
### Function: outofpois (a)

*a*をPoisson符号から一般表現に変換します。
もし*a*がPoisson形式でないなら、
`outofpois`は変換を実行し、
すなわち、その戻り値は、`outofpois (intopois (a))`です。
例えば、この関数は、
特定のタイプのサインやコサイン項のべきの和に関する
標準整理器です。

<!-- category: Series -->
<!-- keywords: pade -->
<!-- signatures: pade(taylor_series, numer_deg_bound, denom_deg_bound) -->
### Function: pade (taylor_series, numer_deg_bound, denom_deg_bound)

分子と分母の次数の和がべき級数の切り詰めレベル以下の
与えられたTaylor級数展開、すなわち、「最良」近似を持ち
加えて指定された次数範囲を満たす、有理関数すべてのリストを返します。


*taylor_series*は１変数Taylor級数です。
*numer_deg_bound*と*denom_deg_bound*は、
分子と分母上の次数範囲を指定する
正の整数です。


*taylor_series*は
Laurent級数も可能です。
次数範囲は、`inf`も可能で、
総次数が、冪級数の長さ以下の有理関数すべてを返すことになります。
総次数は
`numer_deg_bound + denom_deg_bound`として定義されます。
べき級数の長さは
`"truncation level" + 1 - min(0, "order of series")`として定義されます。



```maxima
(%i1) taylor (1 + x + x^2 + x^3, x, 0, 3);
                              2    3
(%o1)/T/             1 + x + x  + x  + . . .
(%i2) pade (%, 1, 1);
                                 1
(%o2)                       [- -----]
                               x - 1
(%i3) t: taylor(-(83787*x^10 - 45552*x^9 - 187296*x^8
                   + 387072*x^7 + 86016*x^6 - 1507328*x^5
                   + 1966080*x^4 + 4194304*x^3 - 25165824*x^2
                   + 67108864*x - 134217728)
       /134217728, x, 0, 10);
                    2    3       4       5       6        7
             x   3 x    x    15 x    23 x    21 x    189 x
(%o3)/T/ 1 - - + ---- - -- - ----- + ----- - ----- - ------
             2    16    32   1024    2048    32768   65536

                                  8         9          10
                            5853 x    2847 x    83787 x
                          + ------- + ------- - --------- + . . .
                            4194304   8388608   134217728
(%i4) pade (t, 4, 4);
(%o4)                          []
```


このべき級数展開を持つ次数4の 分子/分母の有理関数はありません。
一般的に、
解くのに十分な数の未知の係数を持つために、
その和が少なくともべき級数の次数になるまで
分子の次数と分母の次数を増やさなければいけません。



```maxima
(%i5) pade (t, 5, 5);
                     5                4                 3
(%o5) [- (520256329 x  - 96719020632 x  - 489651410240 x

                  2
 - 1619100813312 x  - 2176885157888 x - 2386516803584)

               5                 4                  3
/(47041365435 x  + 381702613848 x  + 1360678489152 x

                  2
 + 2856700692480 x  + 3370143559680 x + 2386516803584)]
```

<!-- category: Series -->
<!-- keywords: poisdiff -->
<!-- signatures: poisdiff(a, b) -->
### Function: poisdiff (a, b)

*a*を*b*に関して微分します。
*b*は三角関数の引数の中だけ、または係数の中だけにいなければいけません。

<!-- category: Series -->
<!-- keywords: poisexpt -->
<!-- signatures: poisexpt(a, b) -->
### Function: poisexpt (a, b)

関数的に`intopois (a^b)`と同一です。
*b*は正の整数でなければいけません。

<!-- category: Series -->
<!-- keywords: poisint -->
<!-- signatures: poisint(a, b) -->
### Function: poisint (a, b)

(`poisdiffと`)似て制限された意味で積分します。
もし*b*が三角関数の引数の中にあるなら、
*b*の中の非周期的項は落とされます。

<!-- category: Series -->
<!-- keywords: poislim -->
<!-- signatures: poislim -->
### Variable: poislim

デフォルト値: 5


`poislim`は、三角関数の引数の中の係数の領域を決定します。
初期値5は
区間[-2^(5-1)+1,2^(5-1)]、すなわち[-15,16]に対応しますが、
[-2^(n-1)+1, 2^(n-1)]に設定することができます。

<!-- category: Series -->
<!-- keywords: poismap -->
<!-- signatures: poismap(series, sinfn, cosfn) -->
### Function: poismap (series, sinfn, cosfn)

関数*sinfn*を与えられたPoisson級数のサイン項に、
*cosfn*をコサイン項に
マップします。
*sinfn*と *cosfn*は、２引数関数です。
引数それぞれは、級数の中の項の係数と三角関数部です。

<!-- category: Series -->
<!-- keywords: poisplus -->
<!-- signatures: poisplus(a, b) -->
### Function: poisplus (a, b)

関数的に`intopois (a + b)`と同一です。

<!-- category: Series -->
<!-- keywords: poissimp -->
<!-- signatures: poissimp(a) -->
### Function: poissimp (a)

*a*を、一般表現の*a*に関するPoisson級数に変換します。

<!-- category: Series -->
<!-- keywords: poisson -->
<!-- signatures: poisson -->
### Variable: poisson

シンボル`/P/`は、Poisson級数式の行ラベルに続きます。

<!-- category: Series -->
<!-- keywords: poissubst -->
<!-- signatures: poissubst(a, b, c) -->
### Function: poissubst (a, b, c)

*a*を*c*の中の*b*に代入します。
*c*はPoisson級数です。


(1) *b*が変数*u*, *v*, *w*, *x*, *y*, *z*のいずれかの場合、
*a*はそれらの変数に関して線形の式(例えば、`6*u + 4*v`)でなければいけません。


(2) *b*はそれらの変数以外の場合、
*a*もまたそれらの変数を含んではいけなく、さらに、サインもコサインも含んではいけません。


`poissubst (a, b, c, d, n)`は、
上のタイプ(1)のように*a*と*b*に関して演算しますが、
*d*がPoisson級数の場合、
*c*の中で*b*に`a + d`を代入した結果を供給するために、
`cos(d)`と`sin(d)`を次数*n*に展開する
特殊なタイプの代入です。
アイデアは、
*d*が小さなパラメータの項に関する展開だということです。
例えば、
`poissubst (u, v, cos(v), %e, 3)`は`cos(u)*(1 - %e^2/2) - sin(u)*(%e - %e^3/6)`をもたらします。

<!-- category: Series -->
<!-- keywords: poistimes -->
<!-- signatures: poistimes(a, b) -->
### Function: poistimes (a, b)

`intopois (a*b)`と同じ機能です。

<!-- category: Series -->
<!-- keywords: poistrim -->
<!-- signatures: poistrim() -->
### Function: poistrim ()

(もしユーザーがそれを定義したら)
Poisson乗算の間、適用する予約関数です。
項の中の*u*, *v*, ..., *z*の係数を引数とする６引数の述語論理関数です。
 (この項の係数に関して)`poistrim`が`true`の項は、
乗算の間に消去されます。

<!-- category: Series -->
<!-- keywords: powerseries -->
<!-- signatures: powerseries(expr, x, a) -->
### Function: powerseries (expr, x, a)

変数*x*に関する点*a*
 (無限大のためには`inf`かもしれません)
の回りの*expr*のべき級数展開の一般形式を返します:


```maxima
inf
           ====
           \               n
            >    b  (x - a)
           /      n
           ====
           n = 0
```


もし`powerseries`が*expr*を展開することができないなら、
`taylor`が、級数の最初のいくつかの項を与えることができます。


`verbose`が`true`の時、
`powerseries`は進捗メッセージを印字します。



```maxima
(%i1) verbose: true$
(%i2) powerseries (log(sin(x)/x), x, 0);
can't expand 
                                 log(sin(x))
so we'll try again after applying the rule:
                                        d
                                      / -- (sin(x))
                                      [ dx
                        log(sin(x)) = i ----------- dx
                                      ]   sin(x)
                                      /
in the first simplification we have returned:
                             /
                             [
                             i cot(x) dx - log(x)
                             ]
                             /
                    inf
                    ====        i1  2 i1             2 i1
                    \      (- 1)   2     bern(2 i1) x
                     >     ------------------------------
                    /                i1 (2 i1)!
                    ====
                    i1 = 1
(%o2)                -------------------------------------
                                      2
```

<!-- category: Series -->
<!-- keywords: printpois -->
<!-- signatures: printpois(a) -->
### Function: printpois (a)

可読フォーマットでPoisson級数を印字します。
`outofpois`と共通で、
もし必要なら、*a*を最初にPoisson符号に変換します。

<!-- category: Series -->
<!-- keywords: product -->
<!-- signatures: product(expr, i, i_0, i_1) -->
### Function: product (expr, i, i_0, i_1)

インデックス*i*が*i_0*から*i_1*まで変えた*expr*の値の積を返します。
名詞形`'product`は、大文字Πとして表示されます。


`product`は、*expr*と下限上限*i_0*、*i_1*を評価し、
`product`は、インデックス*i*をクォートします（評価しません）。


もし上限と下限が整数差だけ違うなら、
*expr*は、インデックス*i*のそれぞれの値に関して評価され、
結果は陽な積です。


そうでなければ、インデックスの範囲は不定です。
積を整理するためにいくつかの規則が適用されます。
グローバル変数`simpproduct`が`true`の時、
更なる規則が適用されます。
いくつかの場合、式整理は、積でない結果を出力します;
そうでなければ、結果は名詞形`'product`です。


`nouns`と`evflag`も参照してください。


例:















```maxima
(%i1) product (x + i*(i+1)/2, i, 1, 4);
(%o1)           (x + 1) (x + 3) (x + 6) (x + 10)
(%i2) product (i^2, i, 1, 7);
(%o2)                       25401600
(%i3) product (a[i], i, 1, 7);
(%o3)                 a  a  a  a  a  a  a
                       1  2  3  4  5  6  7
(%i4) product (a(i), i, 1, 7);
(%o4)          a(1) a(2) a(3) a(4) a(5) a(6) a(7)
(%i5) product (a(i), i, 1, n);
                             n
                           /===\
                            ! !
(%o5)                       ! !  a(i)
                            ! !
                           i = 1
(%i6) product (k, k, 1, n);
                               n
                             /===\
                              ! !
(%o6)                         ! !  k
                              ! !
                             k = 1
(%i7) product (k, k, 1, n), simpproduct;
(%o7)                          n!
(%i8) product (integrate (x^k, x, 0, 1), k, 1, n);
                             n
                           /===\
                            ! !    1
(%o8)                       ! !  -----
                            ! !  k + 1
                           k = 1
(%i9) product (if k <= 5 then a^k else b^k, k, 1, 10);
                              15  40
(%o9)                        a   b
```

<!-- category: Series -->
<!-- keywords: psexpand -->
<!-- signatures: psexpand -->
### Variable: psexpand

デフォルト値: `false`


`psexpand`が`true`の時、
拡張有理関数展開が完全に展開されて表示されます。
スイッチ`ratexpand`は同じ効果を持ちます。



`psexpand`が`false`の時、
多変数式がちょうど有理関数パッケージにあるかのように表示されます。



`psexpand`が`multi`の時、
変数に関する同じ総次数の項は一緒にまとめられます。

<!-- category: Series -->
<!-- keywords: revert, revert2 -->
<!-- signatures: revert(expr, x), revert2(expr, x, n) -->
### Function: revert (expr, x)

これらの関数は、
変数*x*に関するゼロの回りのTaylor級数*expr*の反転を返します。
`revert`は、
*expr*の最高次数と等しい次数の多項式を返します。
`revert2`は、次数*n*の多項式を返します。
*n*は、*expr*の次数よりも大きい値も小さい値も同じ値も取り得ます。


`load ("revert")`はこれらの関数をロードします。


例:



```maxima
(%i1) load ("revert")$
(%i2) t: taylor (exp(x) - 1, x, 0, 6);
                   2    3    4    5     6
                  x    x    x    x     x
(%o2)/T/      x + -- + -- + -- + --- + --- + . . .
                  2    6    24   120   720
(%i3) revert (t, x);
               6       5       4       3       2
           10 x  - 12 x  + 15 x  - 20 x  + 30 x  - 60 x
(%o3)/R/ - --------------------------------------------
                                60
(%i4) ratexpand (%);
                     6    5    4    3    2
                    x    x    x    x    x
(%o4)             - -- + -- - -- + -- - -- + x
                    6    5    4    3    2
(%i5) taylor (log(x+1), x, 0, 6);
                    2    3    4    5    6
                   x    x    x    x    x
(%o5)/T/       x - -- + -- - -- + -- - -- + . . .
                   2    3    4    5    6
(%i6) ratsimp (revert (t, x) - taylor (log(x+1), x, 0, 6));
(%o6)                           0
(%i7) revert2 (t, x, 4);
                          4    3    2
                         x    x    x
(%o7)                  - -- + -- - -- + x
                         4    3    2
```

<!-- category: Series -->
<!-- keywords: simpsum -->
<!-- signatures: simpsum -->
### Variable: simpsum

デフォルト値: `false`


`simpsum`が`true`の時、
`sum`の結果は、整理されます。
この整理は、時々、閉形式を生成することができるかもしれません。
もし`simpsum`が`false`もしくは、もしクォートされた形`'sum`が使われたなら、
値は、数学で使われるΣ表示の表現である和の名詞形です。

<!-- category: Series -->
<!-- keywords: sum -->
<!-- signatures: sum(expr, i, i_0, i_1) -->
### Function: sum (expr, i, i_0, i_1)

インデックス*i*が*i_0*から*i_1*まで変えた*expr*の値の和を返します。
名詞形`'sum`は、大文字Σとして表示されます。


`sum`は、被和*expr*と下限上限*i_0*、*i_1*を評価し、
`sum`は、インデックス*i*をクォートします（評価しません）。


もし上限と下限が整数差だけ違うなら、
被和*expr*は、インデックス*i*のそれぞれの値に関して評価され、
結果は陽な和です。


そうでなければ、インデックスの範囲は不定です。
積を整理するためにいくつかの規則が適用されます。
グローバル変数`simpsum`が`true`の時、
更なる規則が適用されます。
いくつかの場合、式整理は、和でない結果を出力します;
そうでなければ、結果は名詞形`'sum`です。


`evflag`(評価フラグ) `cauchysum`が`true`の時、
和の積は、コーシー積として表現されます。
コーシー積では、内側の和のインデックスは、独立に変化するのではなく、外側の和のインデックスの関数になります。


グローバル変数`genindex`は、
和の次のインデックスを生成するのに使われるアルファベット前置です。


`gensumnum`は、
自動生成されるインデックスが必要な時、
和の次のインデックスを生成するのに使われる数値接尾です。
`gensumnum`が`false`の時,
自動生成されるインデックスは、接尾なしの`genindex`のみです。


`sumcontract`, `intosum`, `bashindices`, `niceindices`,
`nouns`, `evflag`, `zeilberger`も参照してください。


例:


















```maxima
(%i1) sum (i^2, i, 1, 7);
(%o1)                          140
(%i2) sum (a[i], i, 1, 7);
(%o2)           a  + a  + a  + a  + a  + a  + a
                 7    6    5    4    3    2    1
(%i3) sum (a(i), i, 1, 7);
(%o3)    a(7) + a(6) + a(5) + a(4) + a(3) + a(2) + a(1)
(%i4) sum (a(i), i, 1, n);
                            n
                           ====
                           \
(%o4)                       >    a(i)
                           /
                           ====
                           i = 1
(%i5) sum (2^i + i^2, i, 0, n);
                          n
                         ====
                         \       i    2
(%o5)                     >    (2  + i )
                         /
                         ====
                         i = 0
(%i6) sum (2^i + i^2, i, 0, n), simpsum;
                              3      2
                   n + 1   2 n  + 3 n  + n
(%o6)             2      + --------------- - 1
                                  6
(%i7) sum (1/3^i, i, 1, inf);
                            inf
                            ====
                            \     1
(%o7)                        >    --
                            /      i
                            ====  3
                            i = 1
(%i8) sum (1/3^i, i, 1, inf), simpsum;
                                1
(%o8)                           -
                                2
(%i9) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf);
                              inf
                              ====
                              \     1
(%o9)                      30  >    --
                              /      2
                              ====  i
                              i = 1
(%i10) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf), simpsum;
                                  2
(%o10)                       5 %pi
(%i11) sum (integrate (x^k, x, 0, 1), k, 1, n);
                            n
                           ====
                           \       1
(%o11)                      >    -----
                           /     k + 1
                           ====
                           k = 1
(%i12) sum (if k <= 5 then a^k else b^k, k, 1, 10);
          10    9    8    7    6    5    4    3    2
(%o12)   b   + b  + b  + b  + b  + a  + a  + a  + a  + a
```

<!-- category: Series -->
<!-- keywords: sumcontract -->
<!-- signatures: sumcontract(expr) -->
### Function: sumcontract (expr)

定数だけ異なる上限と下限を持つ足し算の和すべてを結合します。
結果は、
そんな和のそれぞれの集合が、この和を形成するよう抽出されなければならないすべての適切な余分の項に加えられた１つの和を含む式です。
`sumcontract`は、互換性のある和すべてを結合し、
可能なら和の１つからインデックスの１つを使い、もし供給されたどれもが使えないなら、合理的なインデックスを形成するよう試みます。



`sumcontract`の前に、`intosum (expr)`を実行する必要があるかもしれません。

<!-- category: Series -->
<!-- keywords: sumexpand -->
<!-- signatures: sumexpand -->
### Variable: sumexpand

デフォルト値: `false`


`sumexpand`が`true`の時、
和の積と、指数和は、入れ子の和に整理されます。


`cauchysum`も参照してください。


例:



```maxima
(%i1) sumexpand: true$
(%i2) sum (f (i), i, 0, m) * sum (g (j), j, 0, n);

                     m      n
                    ====   ====
                    \      \
(%o2)                >      >     f(i1) g(i2)
                    /      /
                    ====   ====
                    i1 = 0 i2 = 0

(%i3) sum (f (i), i, 0, m)^2;
                     m      m
                    ====   ====
                    \      \
(%o3)                >      >     f(i3) f(i4)
                    /      /
                    ====   ====
                    i3 = 0 i4 = 0
```

<!-- category: Series -->
<!-- keywords: taylor -->
<!-- signatures: taylor(expr, x, a, n), taylor(expr, [x_1, x_2, ...], a, n), taylor(expr, [x, a, n, 'asymp]), taylor(expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...]), taylor(expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...) -->
### Function: taylor (expr, x, a, n)

`taylor (expr, x, a, n)`は、
式*expr*を、変数*x*の*a*の周りのTaylorもしくはLaurent級数を
`(x - a)^n`まで展開します。


もし*expr*が形式`f(x)/g(x)` の形であり、
`g(x)`が*n*次まで項を持たないなら、
`taylor`は`g(x)`を`2 n`次まで展開しようとします。
もしまだ0でない項がないなら、
`taylor`は、展開の次数が`n 2^taylordepth`以下である限り
`g(x)`の展開の次数を倍にしていきます。


`taylor (expr, [x_1, x_2, ...], a, n)`
は、すべての変数*x_1*, *x_2*, ...について
点`(a, a, , ...)`の周りで*n*次までのべき級数を返します。


`taylor (expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...)`は、変数*x_1*, *x_2*, ...について
点`(a_1, a_2, ...)`の回りで
*n_1*次, *n_2*次, ....まで展開したべき級数を返します。


`taylor (expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...])`は、
変数*x_1*, *x_2*, ...について、
点`(a_1, a_2, ...)`の回りで
*n_1*次, *n_2*次, ....まで展開したべき級数を返します。


`taylor (expr, [x, a, n, 'asymp])`は、
*expr*の`x - a`の負のべき乗展開を返します。
最高次の項は`(x - a)^-n`です。


`maxtaylorder`が`true`の時、
（丸められた）Taylor級数の代数操作の間、
`talyor`は正確とわかっている限り多くの項を保とうとします。


`psexpand`が`true`の時、
拡張有理関数式は、フルに展開されて表示されます。
スイッチ`ratexpand`は同じ効果を持ちます。
`psexpand`が`false`の時、
有理関数パッケージかのように多変数式が表示されます。
`psexpand`が`multi`なら、同じ総次数の項が一緒にグループ化されます。


展開を制御するには、`taylor_logexpand`スイッチも参照してください。


例:




















```maxima
(%i1) taylor (sqrt (sin(x) + a*x + 1), x, 0, 3);
                           2             2
             (a + 1) x   (a  + 2 a + 1) x
(%o1)/T/ 1 + --------- - -----------------
                 2               8

                                   3      2             3
                               (3 a  + 9 a  + 9 a - 1) x
                             + -------------------------- + . . .
                                           48
(%i2) %^2;
                                    3
                                   x
(%o2)/T/           1 + (a + 1) x - -- + . . .
                                   6
(%i3) taylor (sqrt (x + 1), x, 0, 5);
                       2    3      4      5
                  x   x    x    5 x    7 x
(%o3)/T/      1 + - - -- + -- - ---- + ---- + . . .
                  2   8    16   128    256
(%i4) %^2;
(%o4)/T/                  1 + x + . . .
(%i5) product ((1 + x^i)^2.5, i, 1, inf)/(1 + x^2);

                         inf
                        /===\
                         ! !    i     2.5
                         ! !  (x  + 1)
                         ! !
                        i = 1
(%o5)                   -----------------
                              2
                             x  + 1

(%i6) ev (taylor(%, x,  0, 3), keepfloat);
                               2           3
(%o6)/T/    1 + 2.5 x + 3.375 x  + 6.5625 x  + . . .
(%i7) taylor (1/log (x + 1), x, 0, 3);
                               2       3
                 1   1   x    x    19 x
(%o7)/T/         - + - - -- + -- - ----- + . . .
                 x   2   12   24    720
(%i8) taylor (cos(x) - sec(x), x, 0, 5);
                                4
                           2   x
(%o8)/T/                - x  - -- + . . .
                               6
(%i9) taylor ((cos(x) - sec(x))^3, x, 0, 5);
(%o9)/T/                    0 + . . .
(%i10) taylor (1/(cos(x) - sec(x))^3, x, 0, 5);
                                               2          4
            1     1       11      347    6767 x    15377 x
(%o10)/T/ - -- + ---- + ------ - ----- - ------- - --------
             6      4        2   15120   604800    7983360
            x    2 x    120 x

                                                          + . . .
(%i11) taylor (sqrt (1 - k^2*sin(x)^2), x, 0, 6);
               2  2       4      2   4
              k  x    (3 k  - 4 k ) x
(%o11)/T/ 1 - ----- - ----------------
                2            24

                                    6       4       2   6
                               (45 k  - 60 k  + 16 k ) x
                             - -------------------------- + . . .
                                          720
(%i12) taylor ((x + 1)^n, x, 0, 4);

                      2       2     3      2         3
                    (n  - n) x    (n  - 3 n  + 2 n) x
(%o12)/T/ 1 + n x + ----------- + --------------------
                         2                 6

                               4      3       2         4
                             (n  - 6 n  + 11 n  - 6 n) x
                           + ---------------------------- + . . .
                                          24

(%i13) taylor (sin (y + x), x, 0, 3, y, 0, 3);
               3                 2
              y                 y
(%o13)/T/ y - -- + . . . + (1 - -- + . . .) x
              6                 2

                    3                       2
               y   y            2      1   y            3
          + (- - + -- + . . .) x  + (- - + -- + . . .) x  + . . .
               2   12                  6   12
(%i14) taylor (sin (y + x), [x, y], 0, 3);
                     3        2      2      3
                    x  + 3 y x  + 3 y  x + y
(%o14)/T/   y + x - ------------------------- + . . .
                                6
(%i15) taylor (1/sin (y + x), x, 0, 3, y, 0, 3);
          1   y              1    1               1            2
(%o15)/T/ - + - + . . . + (- -- + - + . . .) x + (-- + . . .) x
          y   6               2   6                3
                             y                    y

                                           1            3
                                      + (- -- + . . .) x  + . . .
                                            4
                                           y
(%i16) taylor (1/sin (y + x), [x, y], 0, 3);
                             3         2       2        3
            1     x + y   7 x  + 21 y x  + 21 y  x + 7 y
(%o16)/T/ ----- + ----- + ------------------------------- + . . .
          x + y     6                   360
```

<!-- category: Series -->
<!-- keywords: taylor_logexpand -->
<!-- signatures: taylor_logexpand -->
### Variable: taylor_logexpand

デフォルト値: `true`


`taylor_logexpand`は、
`taylor`級数の中の対数の展開を制御します。


`taylor_logexpand`が`true`の時、
対数すべては完全に展開されるので、対数的恒等式を含むゼロ認識問題は
展開プロセスを邪魔しません。
しかしながら、分岐情報を無視するので、この方法はいつも数学的にただしいわけではありません。


`taylor_logexpand`が`false`に設定されている時、
生じる対数の唯一の展開は、
形式的なべき級数を得るのに必要なものです。

<!-- category: Series -->
<!-- keywords: taylor_order_coefficients -->
<!-- signatures: taylor_order_coefficients -->
### Variable: taylor_order_coefficients

デフォルト値: `true`


`taylor_order_coefficients`は、
Taylor級数の中の係数の順序付けを制御します。


`taylor_order_coefficients`が`true`の時、
Taylor級数の係数は標準に順序付けられます。

<!-- category: Series -->
<!-- keywords: taylor_simplifier -->
<!-- signatures: taylor_simplifier(expr) -->
### Function: taylor_simplifier (expr)

べき級数*expr*の係数を整理します。
`taylor`はこの関数をコールします。

<!-- category: Series -->
<!-- keywords: taylor_truncate_polynomials -->
<!-- signatures: taylor_truncate_polynomials -->
### Variable: taylor_truncate_polynomials

デフォルト値: `true`



`taylor_truncate_polynomials`が`true`の時、
多項式は入力切り詰めレベルを基礎に切り詰められます。


そうでないなら、
`taylor`への多項式入力は、
不定の精度を持つと考えられます。

<!-- category: Series -->
<!-- keywords: taylordepth -->
<!-- signatures: taylordepth -->
### Variable: taylordepth

デフォルト値: 3



もしまだ非ゼロ項がないなら、
展開の次数が`n 2^taylordepth`以下である限り、
`taylor`は、
`g(x)`の展開の次数を倍にします。

<!-- category: Series -->
<!-- keywords: taylorinfo -->
<!-- signatures: taylorinfo(expr) -->
### Function: taylorinfo (expr)

Taylor級数*expr*についての情報を返します。
戻り値はリストのリストです。
リストそれぞれは、変数名、展開点、展開次数から成ります。


もし*expr*がTaylor級数でないなら、
`taylorinfo`は`false`を返します。


例:



```maxima
(%i1) taylor ((1 - y^2)/(1 - x), x, 0, 3, [y, a, inf]);
                  2                       2
(%o1)/T/ - (y - a)  - 2 a (y - a) + (1 - a )

         2                        2
 + (1 - a  - 2 a (y - a) - (y - a) ) x

         2                        2   2
 + (1 - a  - 2 a (y - a) - (y - a) ) x

         2                        2   3
 + (1 - a  - 2 a (y - a) - (y - a) ) x  + . . .
(%i2) taylorinfo(%);
(%o2)               [[y, a, inf], [x, 0, 3]]
```

<!-- category: Series -->
<!-- keywords: taylorp -->
<!-- signatures: taylorp(expr) -->
### Function: taylorp (expr)

もし*expr*がTaylor級数なら、`true`を、
そうでないなら、`false`を返します。

<!-- category: Series -->
<!-- keywords: taytorat -->
<!-- signatures: taytorat(expr) -->
### Function: taytorat (expr)

`taylor`形式から標準有理式(CRE)形式に
*expr*を変換します。
効果は`rat (ratdisrep (expr))`と同じですが、より速いです。

<!-- category: Series -->
<!-- keywords: trunc -->
<!-- signatures: trunc(expr) -->
### Function: trunc (expr)

一般式*expr*の内部表現をアノテートするので、まるでその和が切り詰められたTaylor級数かのように表示されます。
*expr*は別に変更されません。


例:



```maxima
(%i1) expr: x^2 + x + 1;
                            2
(%o1)                      x  + x + 1
(%i2) trunc (expr);
                                2
(%o2)                  1 + x + x  + . . .
(%i3) is (expr = trunc (expr));
(%o3)                         true
```

<!-- category: Series -->
<!-- keywords: unsum -->
<!-- signatures: unsum(f, n) -->
### Function: unsum (f, n)

最初の後方差`f(n) - f(n - 1)`を返します。
従って、
`unsum`は、ある意味、`sum`の逆です。


`nusum`も参照してください。


例:








```maxima
(%i1) g(p) := p*4^n/binomial(2*n,n);
                                     n
                                  p 4
(%o1)               g(p) := ----------------
                            binomial(2 n, n)
(%i2) g(n^4);
                              4  n
                             n  4
(%o2)                   ----------------
                        binomial(2 n, n)
(%i3) nusum (%, n, 0, n);
                     4        3       2              n
      2 (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3) 4      2
(%o3) ------------------------------------------------ - ------
                    693 binomial(2 n, n)                 3 11 7
(%i4) unsum (%, n);
                              4  n
                             n  4
(%o4)                   ----------------
                        binomial(2 n, n)
```

<!-- category: Series -->
<!-- keywords: verbose -->
<!-- signatures: verbose -->
### Variable: verbose

デフォルト値: `false`


`verbose`が`true`の時、
`powerseries`は進捗メッセージを印字します。

