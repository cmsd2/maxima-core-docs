## Polynomials

<!-- category: Polynomials -->
<!-- keywords: algebraic -->
<!-- signatures: algebraic -->
### Variable: algebraic

デフォルト値: `false`


代数的整数の整理の効果が現れるようにするためには、
`algebraic`は`true`に設定されなければいけません。

<!-- category: Polynomials -->
<!-- keywords: berlefact -->
<!-- signatures: berlefact -->
### Variable: berlefact

デフォルト値: `true`


`berlefact`が`false`の時、
Kroneckerの因数分解アルゴリズムが使われます。
そうでなければ、Berlekampのアルゴリズム―これがデフォルトですーが使われます。

<!-- category: Polynomials -->
<!-- keywords: bezout -->
<!-- signatures: bezout(p1, p2, x) -->
### Function: bezout (p1, p2, x)

`resultant`コマンドの代替。
行列を返します。
この行列の`determinant`は、望みの結果です。

<!-- category: Polynomials -->
<!-- keywords: bothcoef -->
<!-- signatures: bothcoef(expr, x) -->
### Function: bothcoef (expr, x)

最初のメンバーが*expr*の中の*x*の
（もし*expr*がCRE形なら`ratcoef`が見つけるような）
係数であり、
２番目のメンバーが*expr*の残りの部分であるリストを返します。
例えば、
`expr = A*x + B`の`[A, B]`。


例:








```maxima
(%i1) islinear (expr, x) := block ([c],
        c: bothcoef (rat (expr, x), x),
        is (freeof (x, c) and c[1] # 0))$
(%i2) islinear ((r^2 - (x - r)^2)/x, x);
(%o2)                         true
```

<!-- category: Polynomials -->
<!-- keywords: coeff -->
<!-- signatures: coeff(expr, x, n), coeff(expr, x) -->
### Function: coeff (expr, x, n)

*expr*の`x^n`の係数を返します。
ここで、*expr*は*x*の多項式か単項式です。


`coeff(expr, x^n)`は
`coeff(expr, x, n)`と同値です。
`coeff(expr, x, 0)`は
*x*を含まない*expr*の剰余項を返します。
もし省略されたら、*n*は1が仮定されます。


*x*は単純変数か添字付き変数か、演算子1つとその引数のすべてから構成されるexprの部分式です。


`expand`か`factor`を適用することで、
*expr*と同値な式の係数を計算することが可能かもしれません。
`coeff`自身は`expand`や`factor`や他のいかなる関数も
適用しません。


例:


`coeff`は*expr*の`x^n`の係数を返します。






```maxima
(%i1) coeff (b^3*a^3 + b^2*a^2 + b*a + 1, a^3);
                                3
(%o1)                          b
```


`coeff(expr, x^n)`は
`coeff(expr, x, n)`と同値です。







```maxima
(%i1) coeff (c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z, 3);
(%o1)                         - c
                                 3
(%i2) coeff (c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z^3);
(%o2)                         - c
                                 3
```


`coeff(expr, x, 0)`は
*expr*の*x*を含まない剰余項です。






```maxima
(%i1) coeff (a*u + b^2*u^2 + c^3*u^3, b, 0);
                            3  3
(%o1)                      c  u  + a u
```


*x*は単純変数か添字付き変数か、演算子1つとその引数のすべてから構成されるexprの部分式です。









```maxima
(%i1) coeff (h^4 - 2*%pi*h^2 + 1, h, 2);
(%o1)                        - 2 %pi
(%i2) coeff (v[1]^4 - 2*%pi*v[1]^2 + 1, v[1], 2);
(%o2)                        - 2 %pi
(%i3) coeff (sin(1+x)*sin(x) + sin(1+x)^3*sin(x)^3, sin(1+x)^3);
                                3
(%o3)                        sin (x)
(%i4) coeff ((d - a)^2*(b + c)^3 + (a + b)^4*(c - d), a + b, 4);
(%o4)                         c - d
```


`coeff`自身は`expand`や`factor`や他のいかなる関数も
適用しません。











```maxima
(%i1) coeff (c*(a + b)^3, a);
(%o1)                           0
(%i2) expand (c*(a + b)^3);
                 3          2        2        3
(%o2)           b  c + 3 a b  c + 3 a  b c + a  c
(%i3) coeff (%, a);
                                2
(%o3)                        3 b  c
(%i4) coeff (b^3*c + 3*a*b^2*c + 3*a^2*b*c + a^3*c, (a + b)^3);
(%o4)                           0
(%i5) factor (b^3*c + 3*a*b^2*c + 3*a^2*b*c + a^3*c);
                                  3
(%o5)                      (b + a)  c
(%i6) coeff (%, (a + b)^3);
(%o6)                           c
```


`coeff`はリスト、行列、等式上を散逸します。








```maxima
(%i1) coeff ([4*a, -3*a, 2*a], a);
(%o1)                      [4, - 3, 2]
(%i2) coeff (matrix ([a*x, b*x], [-c*x, -d*x]), x);
                          [  a    b  ]
(%o2)                     [          ]
                          [ - c  - d ]
(%i3) coeff (a*u - b*v = 7*u + 3*v, u);
(%o3)                         a = 7
```

<!-- category: Polynomials -->
<!-- keywords: content -->
<!-- signatures: content(p_1, x_1, ..., x_n) -->
### Function: content (p_1, x_1, ..., x_n)

最初のメンバーが、多項式変数*p_1*の*x_n*
に関する項の係数（これが中身です）の最大公約数であり、
２番目のメンバーが中身で多項式*p_1*を割ったものであるリストを返します。




例:





```maxima
(%i1) content (2*x*y + 4*x^2*y^2, y);

                                   2
(%o1)                   [2 x, 2 x y  + y]
```

<!-- category: Polynomials -->
<!-- keywords: denom -->
<!-- signatures: denom(expr) -->
### Function: denom (expr)

有理式*expr*の分母を返します。

<!-- category: Polynomials -->
<!-- keywords: divide -->
<!-- signatures: divide(p_1, p_2, x_1, ..., x_n) -->
### Function: divide (p_1, p_2, x_1, ..., x_n)

メインの多項式変数*x_n*に関して、
多項式*p_2*で割った多項式*p_1*の商と余りを計算します。

他の変数は、`ratvars`関数の中でようなものです。
結果は、最初の要素が商で、２番目の要素が余りのリストです。


例:






```maxima
(%i1) divide (x + y, x - y, x);
(%o1)                       [1, 2 y]
(%i2) divide (x + y, x - y);
(%o2)                      [- 1, 2 x]
```



`y`は２番目の例の主変数であることに注意してください。

<!-- category: Polynomials -->
<!-- keywords: eliminate -->
<!-- signatures: eliminate([eqn_1, ..., eqn_n], [x_1, ..., x_k]) -->
### Function: eliminate ([eqn_1, ..., eqn_n], [x_1, ..., x_k])

連続する結果を取ることによって、式（もしくは0に等しいと仮定された式）から変数を消去します。
これは、*k*個の変数*x_1*, ..., *x_k*が消去された
`n - k`個の式のリストを返します。
最初、*x_1*が消去され、`n - 1`個の式をもたらし、
そして、変数*x_2*が消去され、などなど。
もし`k = n`なら、
変数*x_1*, ..., *x_k*に依らないリストの中の単一式が返されます。
この場合、最後の変数について最後の結果を解くため、`solve`がコールされます。


例:








```maxima
(%i1) expr1: 2*x^2 + y*x + z;
                                      2
(%o1)                    z + x y + 2 x
(%i2) expr2: 3*x + 5*y - z - 1;
(%o2)                  - z + 5 y + 3 x - 1
(%i3) expr3: z^2 + x - y^2 + 5;
                          2    2
(%o3)                    z  - y  + x + 5
(%i4) eliminate ([expr3, expr2, expr1], [y, z]);
             8         7         6          5          4
(%o4) [7425 x  - 1170 x  + 1299 x  + 12076 x  + 22887 x

                                    3         2
                            - 5154 x  - 1291 x  + 7688 x + 15376]
```

<!-- category: Polynomials -->
<!-- keywords: ezgcd -->
<!-- signatures: ezgcd(p_1, p_2, p_3, ...) -->
### Function: ezgcd (p_1, p_2, p_3, ...)

最初の要素が、多項式*p_1*, *p_2*, *p_3*, ...の最大公約数で、
残りの要素が、多項式を最大公約数で割ったものであるリストを返します。
これはいつも`ezgcd`アルゴリズムを使います。


`gcd`, `gcdex`, `gcdivide`, `poly_gcd`も参照してください。


例:


三つの多項式は最大公約数 `2*x-3`を持ちます。
GCDは最初、関数 `gcd`で計算され、その後、関数 `ezgcd`で計算されます。



```maxima
(%i1) p1 : 6*x^3-17*x^2+14*x-3;
                        3       2
(%o1)                6 x  - 17 x  + 14 x - 3
(%i2) p2 : 4*x^4-14*x^3+12*x^2+2*x-3;
                    4       3       2
(%o2)            4 x  - 14 x  + 12 x  + 2 x - 3
(%i3) p3 : -8*x^3+14*x^2-x-3;
                          3       2
(%o3)                - 8 x  + 14 x  - x - 3

(%i4) gcd(p1, gcd(p2, p3));
(%o4)                        2 x - 3

(%i5) ezgcd(p1, p2, p3);
                   2               3      2           2
(%o5) [2 x - 3, 3 x  - 4 x + 1, 2 x  - 4 x  + 1, - 4 x  + x + 1]
```

See also: `gcd`, `gcdex`, `gcdivide`, `poly_gcd`.

<!-- category: Polynomials -->
<!-- keywords: facexpand -->
<!-- signatures: facexpand -->
### Variable: facexpand

デフォルト値: `true`


`facexpand`は、`factor`が返すこれ以上小さくできない因子が
展開された形式（デフォルト）か再帰的（正規のCRE）形式かを制御します。

<!-- category: Polynomials -->
<!-- keywords: factor -->
<!-- signatures: factor(expr), factor(expr, p) -->
### Function: factor (expr)

任意の数の変数と関数を含んだ式*expr*を整数上既約な因子に因数分解します。
`factor (expr, p)`は*expr*を、
有理数体上で、最小多項式が*p*である要素で因数分解します。


`factor`は、整数を素因数分解するのに`ifactor`関数を使います。


`factorflag`が`false`なら有理式の整数因子の素因数分解を抑制します。


`dontfactor`は、因数分解しない変数のリストに設定されます。
（初期状態では空です。）
因数分解は、`dontfactor`リスト上のそれらより（CRE形式で仮定された変数順序を使って）重要でない変数に関しても
実行されません。


`savefactors`が`true`なら、
同じ因子のいくつかを含む式の後の因数分解をスピードアップするために、因子の積である式の因子が、ある関数によって保存されます。


`berlefact`が `false`ならKroneckerの因数分解アルゴリズムが使われ、
そうでなければ、デフォルトであるBerlekampのアルゴリズムが使われます。


`intfaclim`が`true`なら、
もし自明な割り算やPollardのロー法の後、因子が見つからないなら、整数の素因数分解をあきらめます。
`false`に設定されていれば（これはユーザーが陽に`factor`をコールする場合です）整数の完全な素因数分解が企てられます。
`intfaclim`のユーザー設定は内部で`factor`がコールされた時に使われます。
`intfaclim`はMaximaが大きな整数を素因数分解するのにありえない長い時間を使うことを妨げるようにリセットされます。


例:




















```maxima
(%i1) factor (2^63 - 1);
                    2
(%o1)              7  73 127 337 92737 649657
(%i2) factor (-8*y - 4*x + z^2*(2*y + x));
(%o2)               (2 y + x) (z - 2) (z + 2)
(%i3) -1 - 2*x - x^2 + y^2 + 2*x*y^2 + x^2*y^2;
                2  2        2    2    2
(%o3)          x  y  + 2 x y  + y  - x  - 2 x - 1
(%i4) block ([dontfactor: [x]], factor (%/36/(1 + 2*y + y^2)));

                       2
                     (x  + 2 x + 1) (y - 1)
(%o4)                ----------------------
                           36 (y + 1)

(%i5) factor (1 + %e^(3*x));
                      x         2 x     x
(%o5)              (%e  + 1) (%e    - %e  + 1)
(%i6) factor (1 + x^4, a^2 - 2);
                    2              2
(%o6)             (x  - a x + 1) (x  + a x + 1)
(%i7) factor (-y^2*z^2 - x*z^2 + x^2*y^2 + x^3);
                       2
(%o7)              - (y  + x) (z - x) (z + x)
(%i8) (2 + x)/(3 + x)/(b + x)/(c + x)^2;
                             x + 2
(%o8)               ------------------------
                                           2
                    (x + 3) (x + b) (x + c)
(%i9) ratsimp (%);
                4                  3
(%o9) (x + 2)/(x  + (2 c + b + 3) x

     2                       2             2                   2
 + (c  + (2 b + 6) c + 3 b) x  + ((b + 3) c  + 6 b c) x + 3 b c )
(%i10) partfrac (%, x);
           2                   4                3
(%o10) - (c  - 4 c - b + 6)/((c  + (- 2 b - 6) c

     2              2         2                2
 + (b  + 12 b + 9) c  + (- 6 b  - 18 b) c + 9 b ) (x + c))

                 c - 2
 - ---------------------------------
     2                             2
   (c  + (- b - 3) c + 3 b) (x + c)

                         b - 2
 + -------------------------------------------------
             2             2       3      2
   ((b - 3) c  + (6 b - 2 b ) c + b  - 3 b ) (x + b)

                         1
 - ----------------------------------------------
             2
   ((b - 3) c  + (18 - 6 b) c + 9 b - 27) (x + 3)
(%i11) map ('factor, %);

              2
             c  - 4 c - b + 6                 c - 2
(%o11) - ------------------------- - ------------------------
                2        2                                  2
         (c - 3)  (c - b)  (x + c)   (c - 3) (c - b) (x + c)

                       b - 2                        1
            + ------------------------ - ------------------------
                             2                          2
              (b - 3) (c - b)  (x + b)   (b - 3) (c - 3)  (x + 3)

(%i12) ratsimp ((x^5 - 1)/(x - 1));
                       4    3    2
(%o12)                x  + x  + x  + x + 1
(%i13) subst (a, x, %);
                       4    3    2
(%o13)                a  + a  + a  + a + 1
(%i14) factor (%th(2), %);
                       2        3        3    2
(%o14)   (x - a) (x - a ) (x - a ) (x + a  + a  + a + 1)
(%i15) factor (1 + x^12);
                       4        8    4
(%o15)               (x  + 1) (x  - x  + 1)
(%i16) factor (1 + x^99);
                 2            6    3
(%o16) (x + 1) (x  - x + 1) (x  - x  + 1)

   10    9    8    7    6    5    4    3    2
 (x   - x  + x  - x  + x  - x  + x  - x  + x  - x + 1)

   20    19    17    16    14    13    11    10    9    7    6
 (x   + x   - x   - x   + x   + x   - x   - x   - x  + x  + x

    4    3            60    57    51    48    42    39    33
 - x  - x  + x + 1) (x   + x   - x   - x   + x   + x   - x

    30    27    21    18    12    9    3
 - x   - x   + x   + x   - x   - x  + x  + 1)
```

<!-- category: Polynomials -->
<!-- keywords: factorflag -->
<!-- signatures: factorflag -->
### Variable: factorflag

デフォルト値: `false`



`factorflag`が`false`の時、
有理式の整数因子の素因素分解を抑制します。

<!-- category: Polynomials -->
<!-- keywords: factorout -->
<!-- signatures: factorout(expr, x_1, x_2, ...) -->
### Function: factorout (expr, x_1, x_2, ...)

和*expr*を
形式`f (x_1, x_2, ...)*g`の項の和に再整理します。
ここで、`g`は、いかなる*x_i*も含まない式の積で、`f`は因数分解されています。


オプション変数`keepfloat`は`factorout`に無視されることに注意してください。


例:







```maxima
(%i1) expand (a*(x+1)*(x-1)*(u+1)^2);
             2  2          2      2      2
(%o1)     a u  x  + 2 a u x  + a x  - a u  - 2 a u - a
(%i2) factorout(%,x);
         2
(%o2) a u  (x - 1) (x + 1) + 2 a u (x - 1) (x + 1)
                                              + a (x - 1) (x + 1)
```

<!-- category: Polynomials -->
<!-- keywords: factorsum -->
<!-- signatures: factorsum(expr) -->
### Function: factorsum (expr)

*expr*の因子（それらは和です）の中の項を
それらの和が因数分解可能な項のグループにグループ化しようとします。
`factorsum`は、
`expand ((x + y)^2 + (z + w)^2)`の結果を回復できますが、
項が共通の変数を持つので、
`expand ((x + 1)^2 + (x + y)^2)`は回復できません。


例:






```maxima
(%i1) expand ((x + 1)*((u + v)^2 + a*(w + z)^2));
           2      2                            2      2
(%o1) a x z  + a z  + 2 a w x z + 2 a w z + a w  x + v  x

                                     2        2    2            2
                        + 2 u v x + u  x + a w  + v  + 2 u v + u
(%i2) factorsum (%);
                                   2          2
(%o2)            (x + 1) (a (z + w)  + (v + u) )
```

<!-- category: Polynomials -->
<!-- keywords: fasttimes -->
<!-- signatures: fasttimes(p_1, p_2) -->
### Function: fasttimes (p_1, p_2)

多項式の掛け算のための特殊なアルゴリズムを使って、
多項式*p_1*と*p_2*の積を返します。
`p_1`と`p_2`は、
多変数で、密で、ほぼ同じサイズであるべきです。
`n_1`が`p_1`の次数で、
`n_2`が`p_2`の次数だとすると、
古典的な掛け算は、
`n_1 n_2`のオーダーですが、
`fasttimes`は、`max (n_1, n_2)^1.585`のオーダーです。

<!-- category: Polynomials -->
<!-- keywords: fullratsimp -->
<!-- signatures: fullratsimp(expr) -->
### Function: fullratsimp (expr)

`fullratsimp`は、ratsimpと式の非有理的整理を、式変形されなくなるまで繰り返し適応し、結果を返します。


非有理式が含まれる時、`ratsimp`を１回コールと、その後の非有理的（「一般」）整理だけでは、
整理された結果を返すのに十分でないかもしれません。
時々、複数回のコールが必要とされます。
`fullratsimp`はこのプロセスを楽にしてくれます。


`fullratsimp (expr, x_1, ..., x_n)`は`ratsimp`や`rat`と同様
複数の引数を取ります。


例:








```maxima
(%i1) expr: (x^(a/2) + 1)^2*(x^(a/2) - 1)^2/(x^a - 1);
                       a/2     2   a/2     2
                     (x    - 1)  (x    + 1)
(%o1)                -----------------------
                              a
                             x  - 1
(%i2) ratsimp (expr);
                          2 a      a
                         x    - 2 x  + 1
(%o2)                    ---------------
                              a
                             x  - 1
(%i3) fullratsimp (expr);
                              a
(%o3)                        x  - 1
(%i4) rat (expr);
                       a/2 4       a/2 2
                     (x   )  - 2 (x   )  + 1
(%o4)/R/             -----------------------
                              a
                             x  - 1
```

<!-- category: Polynomials -->
<!-- keywords: fullratsubst -->
<!-- signatures: fullratsubst(a, b, c) -->
### Function: fullratsubst (a, b, c)

結果が変わらなくなるまで、自身を再帰的にコールすることを除いて、
`ratsubst`と同じです。
置き換える式と置き換えられる式が１つ以上の変数を共通に持つ時、
この関数は役に立ちます。


`fullratsubst`は、`lratsubst`のフォーマットでも引数を受け付けます。
すなわち、最初の引数は、１つの代入等式もしくは、そんな等式のリストで、
一方、２番目の引数は処理される式というものです。


`load ("lrats")`は、`fullratsubst`と`lratsubst`をロードします。


例:















```maxima
(%i1) load ("lrats")$
```


- *
`subst`は多重代入を実行できます。
`lratsubst`は`subst`に類似しています。


```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```


- *
もしただ１つの代入が望まれるなら、
最初の引数として１つの等式を与えます。


```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```


- *
`fullratsubst`は、
結果が変わらなくなるまで再帰することを除いて、
`ratsubst`と同値です。


```maxima
(%i5) ratsubst (b*a, a^2, a^3);
                               2
(%o5)                         a  b
(%i6) fullratsubst (b*a, a^2, a^3);
                                 2
(%o6)                         a b
```


- *
`fullratsubst`も、
最初の引数として、等式のリストもしくは１つの式を受け入れます。


```maxima
(%i7) fullratsubst ([a^2 = b, b^2 = c, c^2 = a], a^3*b*c);
(%o7)                           b
(%i8) fullratsubst (a^2 = b*a, a^3);
                                 2
(%o8)                         a b
```


- *
`fullratsubst`は、不確定な再帰を起こすかもしれません。


```maxima
(%i9) errcatch (fullratsubst (b*a^2, a^2, a^3));

*** - Lisp stack overflow. RESET
```

<!-- category: Polynomials -->
<!-- keywords: gcd -->
<!-- signatures: gcd(p_1, p_2, x_1, ...) -->
### Function: gcd (p_1, p_2, x_1, ...)

*p_1*と*p_2*の最大公約数を返します。
フラグ`gcd`は、どのアルゴリズムを利用するか決めます。
`gcd`を`ez`, `subres`, `red`, もしくは`spmod`
設定することは、それぞれ、`ezgcd`, 部分終結式`prs`, 被約, もしくはモジュラーアルゴリズムを選択します。
もし`gcd`が`false`なら、
`gcd (p_1, p_2, x)`は、すべての*x*に関していつも1を返します。
（例えば、`ratsimp`, `factor`, など）多くの関数は、
陰にgcdを計算します。
斉次多項式に関して、
`subres`に等しい`gcd`を使うことが推奨されます。
例えば、`gcd (x^2 - 2*sqrt(2)*x + 2, x - sqrt(2))`のように、代数的数が含まれる時
 `algebraic`は`true`でなくてはいけません。また、`gcd`は`ez`であってはいけません。


`gcd`フラグ―デフォルトは`spmod`―は、
もし`false`なら、
式が標準有理式(CRE)形に変換される時も、最大公約数を計算させません。
もしgcdが要求されないなら、これは、時々計算のスピードを上げます。


`ezgcd`, `gcdex`, `gcdivide`, `poly_gcd`も参照してください。


例:



```maxima
(%i1) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i3) gcd(p1, p2);
                            2
(%o3)                    6 x  + 13 x + 6
(%i4) p1/gcd(p1, p2), ratsimp;
(%o4)                         x + 1
(%i5) p2/gcd(p1, p2), ratsimp;
                              3
(%o5)                        x  + x
```


`ezgcd`は
一番目の要素が多項式 *p_1*と *p_2*の最大公約数で、
残りの要素が最大公約数で多項式を割ったもので構成されるリストを返します。



```maxima
(%i6) ezgcd(p1, p2);
                    2                     3
(%o6)           [6 x  + 13 x + 6, x + 1, x  + x]
```

See also: `ezgcd`, `gcdex`, `gcdivide`, `poly_gcd`.

<!-- category: Polynomials -->
<!-- keywords: gcdex -->
<!-- signatures: gcdex(f, g), gcdex(f, g, x) -->
### Function: gcdex (f, g)

リスト`[a, b, u]`を返します。
ここで、*u*は*f*と*g*の最大公約数(gcd)であり、
かつ、`a f + b g`は*u*に等しいです。
引数*f*と*g*は、１変数多項式であるか、
そうでなければ、指定された**主**変数*x*の多項式でなければいけません。
これが機能するには単項イデアル整域にある必要があるからです。
gcdは、他の変数の有理関数係数を持つ１変数多項式としての*f*と*g*に関するgcdを意味します。


`gcdex`は、ユークリッドのアルゴリズムを実行します。
すべてが`[f, g, -1]`に直角の`L[i]: [a[i], b[i], r[i]]`の列を持ち、
`q = quotient(r[i]/r[i+1])`なら`L[i+2]: L[i] - q L[i+1]`となるように次を組み立て、
余り`r[i+2]`がゼロの時、`L[i+1]`で終了します。


引数 *f*と *g*は整数であり得ます。
この場合、`gcdex`は関数 `igcdex`を呼び出します。


`ezgcd`, `gcd`, `gcdivide`, `poly_gcd`も参照してください。


例:







```maxima
(%i1) gcdex (x^2 + 1, x^3 + 4);

                       2
                      x  + 4 x - 1  x + 4
(%o1)/R/           [- ------------, -----, 1]
                           17        17

(%i2) % . [x^2 + 1, x^3 + 4, -1];
(%o2)/R/                        0
```



以下のgcdは、
`k(y)[x]`に関して働くので`1`です。
`k[y, x]`で期待する`y+1`ではないことに注意してください。






```maxima
(%i1) gcdex (x*(y + 1), y^2 - 1, x);

                               1
(%o1)/R/                 [0, ------, 1]
                              2
                             y  - 1
```

See also: `igcdex`, `ezgcd`, `gcd`, `gcdivide`, `poly_gcd`.

<!-- category: Polynomials -->
<!-- keywords: gcfactor -->
<!-- signatures: gcfactor(n) -->
### Function: gcfactor (n)

ガウス整数
すなわち、*a*と*b*が有理整数(元々の整数)
である形式`a + b %i`
の数、*n*をガウス整数上に因数分解します。
因子は、*a*と*b*を非負にすることによって正規化されます。

<!-- category: Polynomials -->
<!-- keywords: gfactor -->
<!-- signatures: gfactor(expr) -->
### Function: gfactor (expr)

多項式*expr*をガウス整数（虚数単位`%i`を付け加えた整数）上で因数分解します。

*a*が`%i`となる`factor (expr, a^2+1)`ようなものです。


例:





```maxima
(%i1) gfactor (x^4 - 1);
(%o1)           (x - 1) (x + 1) (x - %i) (x + %i)
```

<!-- category: Polynomials -->
<!-- keywords: gfactorsum -->
<!-- signatures: gfactorsum(expr) -->
### Function: gfactorsum (expr)

`factorsum`に似ていますが、
`factor`の代わりに`gfactor`を適用します。

<!-- category: Polynomials -->
<!-- keywords: hipow -->
<!-- signatures: hipow(expr, x) -->
### Function: hipow (expr, x)

*expr*の中で、*x*の、陽に示された最も大きな指数を返します。
*x*は変数もしくは一般式です。
もし*x*が*expr*の中に現れないなら、
`hipow`は`0`を返します。


`hipow`は、`expr`に等価な式を考慮しません。
特に、`hipow`は、`expr`を展開しないので、
`hipow (expr, x)`と`hipow (expand (expr, x))`
は、違った結果をもたらすかもしれません。


例:



```maxima
(%i1) hipow (y^3 * x^2 + x * y^4, x);
(%o1)                           2
(%i2) hipow ((x + y)^5, x);
(%o2)                           1
(%i3) hipow (expand ((x + y)^5), x);
(%o3)                           5
(%i4) hipow ((x + y)^5, x + y);
(%o4)                           5
(%i5) hipow (expand ((x + y)^5), x + y);
(%o5)                           0
```

<!-- category: Polynomials -->
<!-- keywords: intfaclim -->
<!-- signatures: intfaclim -->
### Variable: intfaclim

デフォルト値: true


もし`true`なら、
もし試し割りとPollardのロー法の後、因子が見つからなければ、
Maximaは、整数の素因素分解をあきらめ、素因数分解は完了しません。


`intfaclim`が`false`の時、
 (これは、ユーザーが明示的に`factor`をコールした場合です）
完全な素因数分解が試みられます。
`divisors`, `divsum` や`totient`の中で因子が計算される時は、
`intfaclim`は`false`に設定されます




`factor`への内部コールは、
`intfaclim`のユーザー指定の値を考慮します。
`intfaclim`を`true`に設定することは、
大きな整数を素因数分解するのに費やす時間を少なくするかもしれません。

<!-- category: Polynomials -->
<!-- keywords: keepfloat -->
<!-- signatures: keepfloat -->
### Variable: keepfloat

デフォルト値: `false`


`keepfloat`が`true`の時、
浮動小数点数を含む式が標準有理式(CRE)形に変換される時、
浮動小数点が有理数化されないようにします。


関数`solve`とそれを呼び出す関数(例えば`eigenvalues`)は、
現在、このフラグを無視し、とにかく浮動小数点数を変換することに注意してください。


例:







```maxima
(%i1) rat(x/2.0);

`rat' replaced 0.5 by 1/2 = 0.5
                                       x
(%o1)/R/                               -
                                       2
(%i2) rat(x/2.0), keepfloat;

(%o2)/R/                     E        0.5 x
```


`solve` ignores `keepfloat`:






```maxima
(%i3) solve(1.0-x,x), keepfloat;

`rat' replaced 1.0 by 1/1 = 1.0
(%o3)                               [x = 1]
```

<!-- category: Polynomials -->
<!-- keywords: lopow -->
<!-- signatures: lopow(expr, x) -->
### Function: lopow (expr, x)

*expr*の中に陽に現れる*x*の最小の指数を返します。
例えば、



```maxima
(%i1) lopow ((x+y)^2 + (x+y)^a, x+y);
(%o1)                       min(a, 2)
```

<!-- category: Polynomials -->
<!-- keywords: lratsubst -->
<!-- signatures: lratsubst(L, expr) -->
### Function: lratsubst (L, expr)

`subst`の代わりに`ratsubst`を使うことを除いて、
`subst (L, expr)`に類似しています。


`lratsubst`の最初の引数は、
`subst`が受け付けるそれと同一のフォーマットの等式もしくは等式のリストです。
代入は、等式のリストによって与えられた順、すなわち、左から右に、実行されます。


`load ("lrats")`は、`fullratsubst`と`lratsubst`をロードします。


例:









```maxima
(%i1) load ("lrats")$
```


- *
`subst`は多重代入を実行できます。
`lratsubst`は`subst`に似ています。


```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```


- *
もし代入１つだけを望むなら、
１つの等式を最初の引数として与えることができます。


```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```

<!-- category: Polynomials -->
<!-- keywords: modulus -->
<!-- signatures: modulus -->
### Variable: modulus

デフォルト値: `false`


`modulus`が正の数*p*の時、
（`rat`や関連の関数が返すように）有理数上の演算は、
「バランスさせた」モジュラス系と呼ばれるものを使って、
*p*を法とする合同変換が実行されます。
「バランスさせた」モジュラス系では、
`n modulo p`は、
`a p + k`が*n*に等しくなるようなある整数*a*が存在するような整数*k*と定義され、*k*は、
*p*が奇数の時、
`[-(p-1)/2, ..., 0, ..., (p-1)/2]`の中から、
*p*が偶数の時、`[-(p/2 - 1), ..., 0, ...., p/2]`の中から
選ばれます。





`modulus`が再設定された時、もし*expr*が既に標準有理式(CRE)形なら、
正しい結果を得るためには、
例えば`expr: rat (ratdisrep (expr))`というように、*expr*を再ratする必要があるかもしれません。


典型的には、`modulus`は素数が設定されます。
もし`modulus`が正の合成数に設定されたら、
この設定は受け入れられますが、警告メッセージが表示されます。
Maximaは、ゼロや負の整数が`modulus`に割り当てられるのを許します。
それが役に立つ結果を持つかどうか明らかではありませんが。

<!-- category: Polynomials -->
<!-- keywords: num -->
<!-- signatures: num(expr) -->
### Function: num (expr)

もし*expr*が比なら、その分子を返します。
もし*expr*が比でないなら、*expr*が返されます。


`num`は引数を評価します。

<!-- category: Polynomials -->
<!-- keywords: polydecomp -->
<!-- signatures: polydecomp(p, x) -->
### Function: polydecomp (p, x)

変数*x*の多項式*p*を*x*の多項式の関数合成に分解します。
`polydecomp`は、



```maxima
lambda ([x], p_1) (lambda ([x], p_2) (... (lambda ([x], p_n) (x))
  ...))
```


が*p*に等しいようなリスト`[p_1, ..., p_n]`を返します。
*n*より小さい*i*について*p_i*の次数は1より大きいです。


このような分解は一意的ではありません。


例:








```maxima
(%i1) polydecomp (x^210, x);
                          7   5   3   2
(%o1)                   [x , x , x , x ]
(%i2) p : expand (subst (x^3 - x - 1, x, x^2 - a));
                6      4      3    2
(%o2)          x  - 2 x  - 2 x  + x  + 2 x - a + 1
(%i3) polydecomp (p, x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```


以下の関数は、`x`の関数として、
`L = [e_1, ..., e_n]`を合成します;
それはpolydecompの逆です。







```maxima
compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $
```


`compose`を使って、上の例を再表現します:






```maxima
(%i3) polydecomp (compose ([x^2 - a, x^3 - x - 1], x), x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```


`compose (polydecomp (p, x), x)`はいつも
（展開されていない）*p*を返しますが、
`polydecomp (compose ([p_1, ..., p_n], x), x)`は、
必ずしも`[p_1, ..., p_n]`を返さ*ない*ことに注意してください。







```maxima
(%i4) polydecomp (compose ([x^2 + 2*x + 3, x^2], x), x);
                          2       2
(%o4)                   [x  + 2, x  + 1]
(%i5) polydecomp (compose ([x^2 + x + 1, x^2 + x + 1], x), x);
                      2       2
                     x  + 3  x  + 5
(%o5)               [------, ------, 2 x + 1]
                       4       2
```

<!-- category: Polynomials -->
<!-- keywords: polymod -->
<!-- signatures: polymod(p), polymod(p, m) -->
### Function: polymod (p)

多項式*p*を、変数`modulus`の値である現在の法に関してモジュラー表現に変換します。


`polymod (p, m)`は、
`modulus`の現在値の代わりに法*m*を使うように指定します。


`modulus`を参照してください。

<!-- category: Polynomials -->
<!-- keywords: powers -->
<!-- signatures: powers(expr, x) -->
### Function: powers (expr, x)

*expr*に現れる*x*のべきを返します。


`load ("powers")` loads this function.

<!-- category: Polynomials -->
<!-- keywords: quotient -->
<!-- signatures: quotient(p_1, p_2), quotient(p_1, p_2, x_1, ..., x_n) -->
### Function: quotient (p_1, p_2)

多項式*p_1*を多項式*p_2*で割った結果を返します。
引数*x_1*, ..., *x_n*は、`ratvars`と同様に解釈されます。


`quotient`は、`divide`が返す２要素リストの最初の要素を返します。

<!-- category: Polynomials -->
<!-- keywords: radsubstflag -->
<!-- signatures: radsubstflag -->
### Variable: radsubstflag

デフォルト値: `false`


`radsubstflag`がもし `true`なら、
`ratsubst`が
`x`に関して`sqrt (x)`に `u`を代入するような代入をできるようにします。

<!-- category: Polynomials -->
<!-- keywords: rat -->
<!-- signatures: rat(expr), rat(expr, x_1, ..., x_n) -->
### Function: rat (expr)

*expr*を標準有理式(CRE)形式に変換します。
展開し、共通の分母上ですべての項を結合し、通分し、`ratepsilon`の許容誤差内で浮動小数点を有理数に変換します。
変数は、もし指定されたなら、`ratvars`のように*x_1*, ..., *x_n*に従って並び替えられます。


`rat`は一般に、加算`+`, 減算`-`, 乗算`*`, 除算`/`と整数べきの指数を除いた関数を
整理しません。
一方で`ratsimp`はこれらの場合を扱います。
CRE形式の中のアトム(数と変数）は一般形式でのそれと同じではないことに注意してください。
例えば、`rat(x) - x`は`rat(0)`を出力します。
これは0とは違う内部表現を持ちます。



`ratfac`が`true`の時、
`rat`は、CREの一部因数分解された形式を出力します。
有理演算の最中、因数分解パッケージをコールなしに、式は可能な限り因数分解され続けます。
これにより常に、いくつかの計算でメモリと時間を節約することになります。
分子と分母は互いに素になり（例えば、`((x^2 - 1)^4/(x + 10^2)`は`(x - 1)^4 (x + 1)^2`を出力します）、
それぞれの部分の中の因子は互いに素とは限りません。


`ratprint`が`false`ならユーザーに浮動小数点を有理数に変換したことを通知するメッセージの出力を抑制します。


`keepfloat`が`true`なら、浮動小数点が有理数に変換されることを抑制します。


`ratexpand`と`ratsimp`も参照してください。


例:







```maxima
(%i1) ((x - 2*y)^4/(x^2 - 4*y^2)^2 + 1)*(y + a)*(2*y + x) /
      (4*y^2 + x^2);

                                           4
                                  (x - 2 y)
              (y + a) (2 y + x) (------------ + 1)
                                   2      2 2
                                 (x  - 4 y )
(%o1)         ------------------------------------
                              2    2
                           4 y  + x

(%i2) rat (%, y, a, x);
                            2 a + 2 y
(%o2)/R/                    ---------
                             x + 2 y
```

<!-- category: Polynomials -->
<!-- keywords: ratalgdenom -->
<!-- signatures: ratalgdenom -->
### Variable: ratalgdenom

デフォルト値: `true`


`ratalgdenom`が`true`の時、
根号に関する分母の有理化が有効になることを許します。
`ratalgdenom`は、
標準有理式(CRE)が代数モードで使われる時だけ、効果を持ちます。

<!-- category: Polynomials -->
<!-- keywords: ratcoef -->
<!-- signatures: ratcoef(expr, x, n), ratcoef(expr, x) -->
### Function: ratcoef (expr, x, n)

式*expr*の中の式`x^n`の係数を返します。
*n*を省略した場合、*n*は1が仮定されます。


戻り値は、（非有理な意味で可能な場合を除いて、）xの中の変数の制約を受けません。
このタイプの係数が存在しなければ、0を返します。


`ratcoef`は最初の引数を展開し、有理的に整理するので、
純粋に構文法的な`coeff`のそれとは違った答えを生成することがあります。

このように、`ratcoef ((x + 1)/y + x, x)`は`(y + 1)/y`を返しますが、`coeff`は1を返します。


`ratcoef (expr, x, 0)`は、*expr*をsumとして見て、
*x*を含まない項の和を返します。

ゆえに、もし*x*の負のべき乗が存在するなら、*ratcoef*を使うべきではありません。



*expr*は検査される前に有理的に整理されるので、
係数は、想像された形とは全く違って現れることがあります。


例:






```maxima
(%i1) s: a*x + b*x + 5$
(%i2) ratcoef (s, a + b);
(%o2)                           x
```

<!-- category: Polynomials -->
<!-- keywords: ratdenom -->
<!-- signatures: ratdenom(expr) -->
### Function: ratdenom (expr)

*expr*を標準有理式(CRE)に強制した後、*expr*の分母を返します。
戻り値はCREです。



*expr*は、もしまだCREでないなら、`rat`によってCREに強制的に変換されます。
この変換は、すべての項を共通の分母上に置くことによって、
*expr*の形式を変えます。


`denom`は似ていますが、
CREではなく通常の式を返します。
また、`denom`は共通の分母上にすべての項を置こうとはしませんし、
`ratdenom`によって比と見なされるいくつかの式は、`denom`には比と見なされません。

<!-- category: Polynomials -->
<!-- keywords: ratdenomdivide -->
<!-- signatures: ratdenomdivide -->
### Variable: ratdenomdivide

デフォルト値: `true`


`ratdenomdivide`が`true`の時、
`ratexpand`は、分子が和である比を、共通の分母を持つ比の和に展開します。
そうでなければ、`ratexpand`は比の和を１つの比に縮約します。
その比の分子はそれぞれの比の分子の和です。


例:



```maxima
(%i1) expr: (x^2 + x + 1)/(y^2 + 7);
                            2
                           x  + x + 1
(%o1)                      ----------
                              2
                             y  + 7
(%i2) ratdenomdivide: true$
(%i3) ratexpand (expr);
                       2
                      x        x        1
(%o3)               ------ + ------ + ------
                     2        2        2
                    y  + 7   y  + 7   y  + 7
(%i4) ratdenomdivide: false$
(%i5) ratexpand (expr);
                            2
                           x  + x + 1
(%o5)                      ----------
                              2
                             y  + 7
(%i6) expr2: a^2/(b^2 + 3) + b/(b^2 + 3);
                                     2
                           b        a
(%o6)                    ------ + ------
                          2        2
                         b  + 3   b  + 3
(%i7) ratexpand (expr2);
                                  2
                             b + a
(%o7)                        ------
                              2
                             b  + 3
```

<!-- category: Polynomials -->
<!-- keywords: ratdiff -->
<!-- signatures: ratdiff(expr, x) -->
### Function: ratdiff (expr, x)

有理式*expr*を*x*に関して微分します。
*expr*は*x*の多項式もしくは多項式の商でなければなりません。
引数*x*は*expr*の変数もしくは部分式を取り得ます。





たぶん違った形式になりますが、結果は、`diff`と同値です。
有理式の場合、`ratdiff`は`diff`より速いでしょう。


`ratdiff`は、もし*expr*が標準有理式(CRE)なら、標準有理式を返します。
そうでなければ、一般式を返します。


`ratdiff`は、*expr*の*x*への依存のみを考慮し、`depends`で規定された依存性は無視します。







例:










```maxima
(%i1) expr: (4*x^3 + 10*x - 11)/(x^5 + 5);
                           3
                        4 x  + 10 x - 11
(%o1)                   ----------------
                              5
                             x  + 5
(%i2) ratdiff (expr, x);
                    7       5       4       2
                 8 x  + 40 x  - 55 x  - 60 x  - 50
(%o2)          - ---------------------------------
                          10       5
                         x   + 10 x  + 25
(%i3) expr: f(x)^3 - f(x)^2 + 7;
                         3       2
(%o3)                   f (x) - f (x) + 7
(%i4) ratdiff (expr, f(x));
                           2
(%o4)                   3 f (x) - 2 f(x)
(%i5) expr: (a + b)^3 + (a + b)^2;
                              3          2
(%o5)                  (b + a)  + (b + a)
(%i6) ratdiff (expr, a + b);
                    2                    2
(%o6)            3 b  + (6 a + 2) b + 3 a  + 2 a
```

<!-- category: Polynomials -->
<!-- keywords: ratdisrep -->
<!-- signatures: ratdisrep(expr) -->
### Function: ratdisrep (expr)

一般式として引数を返します。
もし*expr*が一般式なら、戻り値は引数から変わりません。


典型的には、`ratdisrep`は、
標準有理式(CRE)を一般式に変換するためにコールされます。

もし「伝染」を止めたかったり、非有理文脈で有理関数を使いたいなら、
これは、時々便利です。


`totaldisrep`も参照してください。

<!-- category: Polynomials -->
<!-- keywords: ratexpand -->
<!-- signatures: ratexpand(expr) -->
### Function: ratexpand (expr)

*expr*を展開します。
指数和や和の積を展開し、共通分母上の分数を結合し、通分し、（もし和なら）分子を分母で割ったそれぞれの項に分割します。


たとえ*expr*が標準有理式(CRE)でも、`ratexpand`の戻り値は一般式です。



スイッチ`ratexpand`が`true`なら、CRE式は、一般式や表示形式に変換された時フルに展開されます。
一方もし`false`なら再帰形式に変換します。
`ratsimp`も参照してください。


`ratdenomdivide`が`true`の時、
`ratexpand`は、分子が和である比を、共通の分母を持つ比の和に展開します。
そうでなければ、`ratexpand`は日の和を、その分子がそれぞれの比の分子の和である単一の比にまとめます。


`keepfloat`が`true`の時、
浮動小数点を含んだ式がCRE形式に変換される時、浮動小数点が有理化されるのを抑制します。


例:








```maxima
(%i1) ratexpand ((2*x - 3*y)^3);
                     3         2       2        3
(%o1)          - 27 y  + 54 x y  - 36 x  y + 8 x
(%i2) expr: (x - 1)/(x + 1)^2 + 1/(x - 1);
                         x - 1       1
(%o2)                   -------- + -----
                               2   x - 1
                        (x + 1)
(%i3) expand (expr);
                    x              1           1
(%o3)          ------------ - ------------ + -----
                2              2             x - 1
               x  + 2 x + 1   x  + 2 x + 1
(%i4) ratexpand (expr);
                        2
                     2 x                 2
(%o4)           --------------- + ---------------
                 3    2            3    2
                x  + x  - x - 1   x  + x  - x - 1
```

<!-- category: Polynomials -->
<!-- keywords: ratfac -->
<!-- signatures: ratfac -->
### Variable: ratfac

デフォルト値: `false`


`ratfac`が`true`の時、
標準有理式(CRE)は部分的に因数分解された形式で操作されます。


有理演算の間、
式は、`factor`をコールすることなしに、
可能な限り最大限因数分解されるよう維持されます。
これは、いつも保存領域を節約し、いくつかの計算では時間も節約ことがあります。
分子と分母は互いに素になります。
例えば、`rat ((x^2 - 1)^4/(x + 1)^2)`は、
`(x - 1)^4 (x + 1)^2)`をもたらしますが、
それぞれの部分の中の因子は互いに素ではないかもしれません。


`ctensr`（成分テンソル操作）パッケージでは、
`ratfac`が`true`の時、
リッチ、アインシュタイン、リーマン、そしてワイルテンソルとスカラー曲率は、
自動的に因数分解されます。
*`ratfac`は、テンソルの成分が２、３の項から成ると知られている場合だけ
設定すべきです。*


`ratfac`と`ratweight`体系は互換性はなく、
同時には使えないかもしれません。

<!-- category: Polynomials -->
<!-- keywords: ratnumer -->
<!-- signatures: ratnumer(expr) -->
### Function: ratnumer (expr)

*expr*を標準有理式(CRE)に強制変換した後、その分子を返します。
戻り値はCREです。



もしまだCREでないなら、*expr*は、`rat`によってCREに強制変換されます。
この変換は、
共通の分母上にすべての項を置くことによって、
*expr*の形式を変えるかもしれません。


`num`は似ていますが、
CREではなく通常の式を返します。
また、`num`は共通の分母上にすべての項を置こうとはしませんし、
`ratnumer`によって比と見なされるいくつかの式は、`num`には比と見なされません。

<!-- category: Polynomials -->
<!-- keywords: ratp -->
<!-- signatures: ratp(expr) -->
### Function: ratp (expr)

もし*expr*が標準有理式(CRE)もしくは拡張CREなら、`true`を返し、
そうでなければ、`false`を返します。


CREは、`rat`と関連関数によって生成されます。
拡張CREは、`taylor`と関連関数によって生成されます。

<!-- category: Polynomials -->
<!-- keywords: ratprint -->
<!-- signatures: ratprint -->
### Variable: ratprint

デフォルト値: `true`


`ratprint`が`true`の時、
ユーザーに浮動小数点を有理数に変換したことを通知するメッセージが表示されます。

<!-- category: Polynomials -->
<!-- keywords: ratsimp -->
<!-- signatures: ratsimp(expr), ratsimp(expr, x_1, ..., x_n) -->
### Function: ratsimp (expr)

式*exp*とその部分式の全てを有理的に整理します（非有理的関数の引数も含みます）。
結果は二つの多項式の商として、再帰的形式—主変数の係数が他の変数の多項式である形式—で返されます。
変数は(例えば、`sin(z^2+1)`のような)非有理関数を含むかもしれませんが、
どんな非有理関数の引数もまた、有理的に整理されます。


`ratsimp (expr, x_1, ..., x_n)`は、`ratvars`で指定した場合と同様に、
変数の順序指定に従って有理的に整理します。


`ratsimpexpons`が`true`の時、
`ratsimp`は式の指数にも適用されます。


`ratexpand`も参照してください。
`ratsimp`は、`ratexpand`に影響するフラグのいくつかに影響されることに注意してください。


例:









```maxima
(%i1) sin (x/(x^2 + x)) = exp ((log(x) + 1)^2 - log(x)^2);

                                         2      2
                   x         (log(x) + 1)  - log (x)
(%o1)        sin(------) = %e
                  2
                 x  + x

(%i2) ratsimp (%);
                             1          2
(%o2)                  sin(-----) = %e x
                           x + 1
(%i3) ((x - 1)^(3/2) - (x + 1)*sqrt(x - 1))/sqrt((x - 1)*(x + 1));

                       3/2
                (x - 1)    - sqrt(x - 1) (x + 1)
(%o3)           --------------------------------
                     sqrt((x - 1) (x + 1))

(%i4) ratsimp (%);
                           2 sqrt(x - 1)
(%o4)                    - -------------
                                 2
                           sqrt(x  - 1)
(%i5) x^(a + 1/a), ratsimpexpons: true;
                               2
                              a  + 1
                              ------
                                a
(%o5)                        x
```

<!-- category: Polynomials -->
<!-- keywords: ratsimpexpons -->
<!-- signatures: ratsimpexpons -->
### Variable: ratsimpexpons

デフォルト値: `false`


`ratsimpexpons`が`true`の時、
式整理の間、`ratsimp`が式の指数に適用されます。

<!-- category: Polynomials -->
<!-- keywords: ratsubst -->
<!-- signatures: ratsubst(a, b, c) -->
### Function: ratsubst (a, b, c)

*c*の中の*b*に*a*を代入し、結果の式を返します。

*b*はsumでもproductでもpowerなどでも問題ありません。



`subst`は純粋に構文法的代入ですが、`ratsubst`は式の意味の何かを知っています。
ゆえに、`subst (a, x + y, x + y + z)`は`x + y + z`を返す一方、
`ratsubst`は`z + a`を返します。


`ratsubstflag`が`true`の時、`ratsubst`は、式が陽には含んでいない根への代入を実行します。


`ratsubst`はオプション変数`keepfloat`の値`true`を無視します。


例:
















```maxima
(%i1) ratsubst (a, x*y^2, x^4*y^3 + x^4*y^8);
                              3      4
(%o1)                      a x  y + a
(%i2) cos(x)^4 + cos(x)^3 + cos(x)^2 + cos(x) + 1;
               4         3         2
(%o2)       cos (x) + cos (x) + cos (x) + cos(x) + 1
(%i3) ratsubst (1 - sin(x)^2, cos(x)^2, %);
            4           2                     2
(%o3)    sin (x) - 3 sin (x) + cos(x) (2 - sin (x)) + 3
(%i4) ratsubst (1 - cos(x)^2, sin(x)^2, sin(x)^4);

                        4           2
(%o4)                cos (x) - 2 cos (x) + 1

(%i5) radsubstflag: false$
(%i6) ratsubst (u, sqrt(x), x);
(%o6)                           x
(%i7) radsubstflag: true$
(%i8) ratsubst (u, sqrt(x), x);
                                2
(%o8)                          u
```

<!-- category: Polynomials -->
<!-- keywords: ratvars -->
<!-- signatures: ratvars(x_1, ..., x_n), ratvars() -->
### Function: ratvars (x_1, ..., x_n)

有理式に関して主変数*x_1*, ..., *x_n*を宣言します。
もし有理式の中に存在するなら、*x_n*は主変数と見なされます。
そうでなければ、もし存在すれば、*x_[n-1]*が主変数と見なされます。
と、先行する変数を通して*x_1*まで続きます。
*x_1*は、続く変数が存在しなかった時だけ主変数と見なされます。


もし有理式の中の変数が`ratvars`リストの中に存在しなかったら、
その変数には、*x_1*よりも低い優先順位が与えられます。


`ratvars`の引数は、変数もしくは`sin(x)`のような非有理関数であり得ます。


変数`ratvars`は、直近にコールされたときの関数`ratvars`の引数のリストです。
関数`ratvars`のコールそれぞれは、リストを再設定します。
`ratvars ()`はリストをクリアします。

<!-- category: Polynomials -->
<!-- keywords: ratvarswitch -->
<!-- signatures: ratvarswitch -->
### Variable: ratvarswitch

デフォルト値: `true`


MaximaはLisp変数`VARLIST`の中に有理式の主変数の内部リストを保持します。
もし`ratvarswitch`が`true`なら、
すべての評価は新しいリスト`VARLIST`で開始します。
これがデフォルトの振る舞いです。
そうでなければ、以前の評価からの主変数は
内部リスト`VARLIST`から取り除かれません。


主変数は関数`ratvars`で宣言されるのですが、
それはオプション変数`ratvarswitch`によって影響されません。


例:


もし `ratvarswitch`が`true`, すべての評価は
新しいリスト`VARLIST`で始まります。










```maxima
(%i1) ratvarswitch:true$

(%i2) rat(2*x+y^2);
                             2
(%o2)/R/                    y  + 2 x
(%i3) :lisp varlist
($X $Y)

(%i3) rat(2*a+b^2);
                             2
(%o3)/R/                    b  + 2 a

(%i4) :lisp varlist
($A $B)
```


もし`ratvarswitch`が`false`なら、
直前の評価からの主変数はまだ存在しています。










```maxima
(%i4) ratvarswitch:false$

(%i5) rat(2*x+y^2);
                             2
(%o5)/R/                    y  + 2 x
(%i6) :lisp varlist
($X $Y)

(%i6) rat(2*a+b^2);
                             2
(%o6)/R/                    b  + 2 a

(%i7) :lisp varlist
($A $B $X $Y)
```

<!-- category: Polynomials -->
<!-- keywords: ratweight -->
<!-- signatures: ratweight(x_1, w_1, ..., x_n, w_n), ratweight() -->
### Function: ratweight (x_1, w_1, ..., x_n, w_n)

重み*w_i*を変数*x_i*に割り当てます。
これは、もし重みが変数`ratwtlvl`の値を越えるなら、項を0に置き換えるようにします。
（デフォルトでは切り詰めはもたらしません。）
項の重みは、項の中の変数の重みの積の和に変数の指数を掛けたものです。
例えば、`3 x_1^2 x_2`の重みは`2 w_1 + w_2`です。
`ratwtlvl`に従った切り詰めは、
標準有理式(CRE)を掛けたり、指数化する時だけ実行されます。


`ratweight ()`は、重み割り当ての累積リストを返します。


注意：`ratfac`と`ratweight`体系は互換性はなく、
同時には使えないかもしれません。


例:









```maxima
(%i1) ratweight (a, 1, b, 1);
(%o1)                     [a, 1, b, 1]
(%i2) expr1: rat(a + b + 1)$
(%i3) expr1^2;
                  2                  2
(%o3)/R/         b  + (2 a + 2) b + a  + 2 a + 1
(%i4) ratwtlvl: 1$
(%i5) expr1^2;
(%o5)/R/                  2 b + 2 a + 1
```

<!-- category: Polynomials -->
<!-- keywords: ratweights -->
<!-- signatures: ratweights -->
### Variable: ratweights

デフォルト値: `[]`


`ratweights`は、`ratweight`で割り当てられた重みのリストです。
リストは累積されます:
`ratweight`のコールそれぞれは、リストに項目を追加します。



`kill (ratweights)`と`save (ratweights)`はともに期待通り動作します。

<!-- category: Polynomials -->
<!-- keywords: ratwtlvl -->
<!-- signatures: ratwtlvl -->
### Variable: ratwtlvl

デフォルト値: `false`


`ratwtlvl`は、
標準有理式(CRE)の切り詰めを制御するために、
`ratweight`関数と組み合わせて使われます。
デフォルト値の`false`では、切り詰めは起こりません。

<!-- category: Polynomials -->
<!-- keywords: remainder -->
<!-- signatures: remainder(p_1, p_2), remainder(p_1, p_2, x_1, ..., x_n) -->
### Function: remainder (p_1, p_2)

多項式*p_1*を多項式*p_2*で割った余りを返します。
引数*x_1*, ..., *x_n*は、`ratvars`と同様に解釈されます。


`remainder`は、`divide`が返す２要素リストの２番目の要素を返します。

<!-- category: Polynomials -->
<!-- keywords: resultant -->
<!-- signatures: resultant(p_1, p_2, x) -->
### Function: resultant (p_1, p_2, x)

変数*x*を消去して、２つの多項式*p_1*と*p_2*の終結式を計算します。
終結式は*p_1*と*p_2*の中の*x*の係数の判別式です。
それは、*p_1*と*p_2*が共通に定数でない因子を持つ時だけゼロに等しいです。


もし*p_1*もしくは*p_2*が因数分解できるなら、
`resultant`をコールする前に`factor`をコールするのが望ましいかもしれません。


変数`resultant`は、
どのアルゴリズムが計算に使われるか制御します。

部分終結式prsには`subres`
モジュラー終結式アルゴリズムには`mod`
通分prsには`red`。
大抵の問題では、`subres`が最適です。
いくつかの大きな次数の１変数もしくは２変数問題では、`mod`がよりよいかもしれません。


関数`bezout`は、`resultant`と同じ引数を取り、
行列を返します。
戻り値の判別式は望みの終結式です。

<!-- category: Polynomials -->
<!-- keywords: savefactors -->
<!-- signatures: savefactors -->
### Variable: savefactors

デフォルト値: `false`



`savefactors`が`true`の時、
同じ因子のいくつかを含む式の因数分解を後でする時にスピードアップするために、
因子の積である式の因子がある関数によって保存されるようにします。

<!-- category: Polynomials -->
<!-- keywords: showratvars -->
<!-- signatures: showratvars(expr) -->
### Function: showratvars (expr)

式`expr`の中の標準有理式 (CRE)変数のリストを返します。


`ratvars`も参照してください。

<!-- category: Polynomials -->
<!-- keywords: sqfr -->
<!-- signatures: sqfr(expr) -->
### Function: sqfr (expr)

多項式因子が「平方にならない」ことを除いて、
`factor`に似ています。
すなわち、それらは、次数１だけの因子を持ちます。
このアルゴリズムは、`factor`の最初の段階でも使われるのですが、
多項式は、n階微分と共通に nよりも大きな次数のすべての因子を持つという事実を使います。
このように、それぞれの変数に関する微分の多項式との最大公約数を取ることによって、
1よりも大きな次数の因子を見つけることができます。


例:





```maxima
(%i1) sqfr (4*x^4 + 4*x^3 - 3*x^2 - 4*x - 1);
                                2   2
(%o1)                  (2 x + 1)  (x  - 1)
```

<!-- category: Polynomials -->
<!-- keywords: tellrat -->
<!-- signatures: tellrat(p_1, ..., p_n), tellrat() -->
### Function: tellrat (p_1, ..., p_n)

多項式*p_1*, ..., *p_n*の解である要素を
Maximaに知られている代数的整数の環に加えます。
それぞれの引数*p_i*は、整数係数の多項式です。


`tellrat (x)`は、実際には、
有理関数の中で*x*に0を代入することを意味します。


`tellrat ()`は、現在の代入のリストを返します。


代数的整数の整理が効果を持つようにするために、
`algebraic`は、`true`に設定されなければいけません。


Maximaは、起動の際には、虚数単位と整数の根すべてについて知っています。


核を取り、`tellrat`プロパティを削除するコマンド`untellrat`があります。


例えば、`tellrat (x^2 - y^2)`のように、
多変数多項式を`tellrat`する時、
`y^2`を`x^2`に代入するのか逆なのかといった
あいまいさがあります。
Maximaは、特定の順序付けを選びますが、
もしユーザーがどちらか指定したいなら、
例えば，`tellrat (y^2 = x^2)`は
`y^2`を`x^2`で置き換えることを示す構文法を供給します。









例:










```maxima
(%i1) 10*(%i + 1)/(%i + 3^(1/3));
                           10 (%i + 1)
(%o1)                      -----------
                                  1/3
                            %i + 3
(%i2) ev (ratdisrep (rat(%)), algebraic);
             2/3      1/3              2/3      1/3
(%o2)    (4 3    - 2 3    - 4) %i + 2 3    + 4 3    - 2
(%i3) tellrat (1 + a + a^2);
                            2
(%o3)                     [a  + a + 1]
(%i4) 1/(a*sqrt(2) - 1) + a/(sqrt(3) + sqrt(2));
                      1                 a
(%o4)           ------------- + -----------------
                sqrt(2) a - 1   sqrt(3) + sqrt(2)
(%i5) ev (ratdisrep (rat(%)), algebraic);
         (7 sqrt(3) - 10 sqrt(2) + 2) a - 2 sqrt(2) - 1
(%o5)    ----------------------------------------------
                               7
(%i6) tellrat (y^2 = x^2);
                        2    2   2
(%o6)                 [y  - x , a  + a + 1]
```

<!-- category: Polynomials -->
<!-- keywords: totaldisrep -->
<!-- signatures: totaldisrep(expr) -->
### Function: totaldisrep (expr)

*expr*のすべての部分式を標準有理式(CRE)から一般形に変換して、
結果を返します。
もし*expr*がそれ自身CRE形なら、`totaldisrep`は、`ratdisrep`と同一です。


`totaldisrep`は、
CRE形の部分式を持つ等式やリストや行列などの式をratdisrepするために役に立つかもしれません。

<!-- category: Polynomials -->
<!-- keywords: untellrat -->
<!-- signatures: untellrat(x_1, ..., x_n) -->
### Function: untellrat (x_1, ..., x_n)

*x_1*, ..., *x_n*から
`tellrat`プロパティを
削除します。

