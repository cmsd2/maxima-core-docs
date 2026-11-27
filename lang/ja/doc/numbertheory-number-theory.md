## Number Theory

<!-- category: NumberTheory -->
<!-- keywords: bern -->
<!-- signatures: bern(n) -->
### Function: bern (n)

整数*n*について*n*番目のBernoulli数を返します。


もし`zerobern`が`false`なら
ゼロに等しいBernoulli数は抑制されます。


`burn`も参照してください。



```maxima
(%i1) zerobern: true$
(%i2) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                  1  1       1      1        1
(%o2)       [1, - -, -, 0, - --, 0, --, 0, - --]
                  2  6       30     42       30
(%i3) zerobern: false$
(%i4) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
            1  1    1   5     691   7    3617  43867
(%o4) [1, - -, -, - --, --, - ----, -, - ----, -----]
            2  6    30  66    2730  6    510    798
```

<!-- category: NumberTheory -->
<!-- keywords: bernpoly -->
<!-- signatures: bernpoly(x, n) -->
### Function: bernpoly (x, n)

変数*x*に関する*n*番目のBernoulli多項式を返します。

<!-- category: NumberTheory -->
<!-- keywords: bfhzeta -->
<!-- signatures: bfhzeta(s, h, n) -->
### Function: bfhzeta (s, h, n)

引数*s*と*h*に関するHurwitzのゼータ関数を返します。
戻り値は多倍長浮動小数点(bfloat)です;
*n*は戻り値の小数点以下の桁数です。


Hurwitzゼータ関数は以下のように定義されます。



$$
\zeta \left(s,h\right) = \sum_{k=0}^\infty {1 \over \left(k+h\right)^{s}}
$$


```maxima
inf
                        ====
                        \        1
         zeta (s,h)  =   >    --------
                        /            s
                        ====  (k + h)
                        k = 0
```


`load ("bffac")`はこの関数をロードします。

<!-- category: NumberTheory -->
<!-- keywords: bfzeta -->
<!-- signatures: bfzeta(s, n) -->
### Function: bfzeta (s, n)

引数*s*に関するRiemannのゼータ関数を返します。
戻り値は多倍長浮動小数点(bfloat)です;
*n*は戻り値の小数点以下の桁数です。

<!-- category: NumberTheory -->
<!-- keywords: burn -->
<!-- signatures: burn(n) -->
### Function: burn (n)

*n*番目のBernoulli数の近似の有理数をを返します。
`burn`は、(有理)Bernoulli数が
まあまあの効率で(超越的)ゼータによって近似できるという観察を利用します。



```maxima
n - 1  1 - 2 n
              (- 1)      2        zeta(2 n) (2 n)!
     B(2 n) = ------------------------------------
                                2 n
                             %pi
```


`bern`は、返す前にインデックス*n*までのBernoulli数すべてを計算するので、
`burn`は、大きな、孤立した*n*(たぶん105以上の*n*)
に対して`bern`より効率的かもしれません。
`burn`は、255よりおおきな偶数*n*に対して近似を呼び出します。
奇数と255以下の*n*に対しては、関数`bern`が呼び出されます。


`load ("bffac")`はこの関数をロードします。`bern`も参照してください。

<!-- category: NumberTheory -->
<!-- keywords: cf -->
<!-- signatures: cf(expr) -->
### Function: cf (expr)

*expr*を連分数に変換します。
*expr*は、
連分数と整数の平方根から成る式です。
式の中のオペランドは　代数演算子を組み合わせられます。
連分数と平方根は別にして、式の中の因子は整数か有理数でなければいけません。
Maximaは、
`cf`の外側で連分数に関する演算について知りません。


`listarith`を`false`にバインドした後、
`cf`は、引数を評価します。
`cf`は、リストとして表現された連分数を返します。


連分数`a + 1/(b + 1/(c + ...))`は、
リスト`[a, b, c, ...]`で表現されます。
リストの要素`a`, `b`, `c`, ...は、
整数に評価されなければいけません。
*expr*は、 may also contain 
`sqrt (n)`も含むかもしれません。`n`は整数です。
この場合、`cf`は、
変数`cflength`の値掛ける周期と同じ数の連分数の項を与えます。


連分数は、
`cfdisrep`が返す代数表現を評価することで、
数に評価することができます。
連分数を評価する別の方法に関しては、
`cfexpand`も参照してください。


`cfdisrep`, `cfexpand`, `cflength`も参照してください。


例:



- *
*expr*は、連分数と整数の平方根から成る式です。

```maxima
(%i1) cf ([5, 3, 1]*[11, 9, 7] + [3, 7]/[4, 3, 2]);
(%o1)               [59, 17, 2, 1, 1, 1, 27]
(%i2) cf ((3/17)*[1, -2, 5]/sqrt(11) + (8/13));
(%o2)        [0, 1, 1, 1, 3, 2, 1, 4, 1, 9, 1, 9, 2]
```
- *
`cflength`は、
連分数の何周期を代数的無理数のために計算するかを制御します。

```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```
- *
連分数は、`cfdisrep`が返す代数的表現を評価することによって評価されることができます。

```maxima
(%i1) cflength: 3$
(%i2) cfdisrep (cf (sqrt (3)))$
(%i3) ev (%, numer);
(%o3)                   1.731707317073171
```
- *
Maximaは、
`cf`の外側で連分数に関する演算について知りません。

```maxima
(%i1) cf ([1,1,1,1,1,2] * 3);
(%o1)                     [4, 1, 5, 2]
(%i2) cf ([1,1,1,1,1,2]) * 3;
(%o2)                  [3, 3, 3, 3, 3, 6]
```

<!-- category: NumberTheory -->
<!-- keywords: cfdisrep -->
<!-- signatures: cfdisrep(list) -->
### Function: cfdisrep (list)

連分数`[a, b, c, ...]`のリスト表現から、
形式`a + 1/(b + 1/(c + ...))`の通常の代数式を構成し返します。



```maxima
(%i1) cf ([1, 2, -3] + [1, -2, 1]);
(%o1)                     [1, 1, 1, 2]
(%i2) cfdisrep (%);
                                  1
(%o2)                     1 + ---------
                                    1
                              1 + -----
                                      1
                                  1 + -
                                      2
```

<!-- category: NumberTheory -->
<!-- keywords: cfexpand -->
<!-- signatures: cfexpand(x) -->
### Function: cfexpand (x)

連分数*x*のコンバージェントの
最後(列1)とその１つ前(列2)の
分子と分母の行列を返します。



```maxima
(%i1) cf (rat (ev (%pi, numer)));

`rat' replaced 3.141592653589793 by 103993/33102 =3.141592653011902
(%o1)                  [3, 7, 15, 1, 292]
(%i2) cfexpand (%); 
                         [ 103993  355 ]
(%o2)                    [             ]
                         [ 33102   113 ]
(%i3) %[1,1]/%[2,1], numer;
(%o3)                   3.141592653011902
```

<!-- category: NumberTheory -->
<!-- keywords: cflength -->
<!-- signatures: cflength -->
### Variable: cflength

デフォルト値: 1


`cflength`は、
値`cflength`掛ける周期として
関数`cf`が与える連分数の項の数を制御します。
従って、デフォルトは1周期を与えます。



```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```

<!-- category: NumberTheory -->
<!-- keywords: divsum -->
<!-- signatures: divsum(n, k), divsum(n) -->
### Function: divsum (n, k)

`divsum (n, k)`は、
*n*の約数の*k*乗した和を返します。


`divsum (n)`は
*n*の約数の和を返します。



```maxima
(%i1) divsum (12);
(%o1)                          28
(%i2) 1 + 2 + 3 + 4 + 6 + 12;
(%o2)                          28
(%i3) divsum (12, 2);
(%o3)                          210
(%i4) 1^2 + 2^2 + 3^2 + 4^2 + 6^2 + 12^2;
(%o4)                          210
```

<!-- category: NumberTheory -->
<!-- keywords: euler -->
<!-- signatures: euler(n) -->
### Function: euler (n)

非負の整数*n*に対して
*n*番目のEuler数を返します。


Euler-Mascheroni定数に関しては、`%gamma`を参照してください。



```maxima
(%i1) map (euler, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1)    [1, 0, - 1, 0, 5, 0, - 61, 0, 1385, 0, - 50521]
```

<!-- category: NumberTheory -->
<!-- keywords: fib -->
<!-- signatures: fib(n) -->
### Function: fib (n)

第*n*項のFibonacci数を返します。
`fib(0)`は0に等しく、`fib(1)`は1に等しく、
`fib (-n)`は`(-1)^(n + 1) * fib(n)`に等しい。


`fib`をコールした後，
`prevfib`は`fib (x - 1)`、
計算された最後の１つ前のFibonacci数に等しい。



```maxima
(%i1) map (fib, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1)         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

<!-- category: NumberTheory -->
<!-- keywords: fibtophi -->
<!-- signatures: fibtophi(expr) -->
### Function: fibtophi (expr)

*expr*に関するFibonacci数を
定数`%phi`を使って表現します。
`%phi`は、`(1 + sqrt(5))/2`, 近似的に1.61803399です。


例:









```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1
(%i4) ratsimp (%);
(%o4)                           0
```

<!-- category: NumberTheory -->
<!-- keywords: ifactors -->
<!-- signatures: ifactors(n) -->
### Function: ifactors (n)

正の整数*n*に対して、
*n*の素因数分解を返します。
もし`n=p1^e1..pk^nk`が
*n*の素因数への分解なら、
ifactorsは`[[p1, e1], ... , [pk, ek]]`を返します。


使われる素因数分解法は9973までの素数による試行除算と、
Pollardのロー法、楕円曲線法です。



```maxima
(%i1) ifactors(51575319651600);
(%o1)     [[2, 4], [3, 2], [5, 2], [1583, 1], [9050207, 1]]
(%i2) apply("*", map(lambda([u], u[1]^u[2]), %));
(%o2)                        51575319651600
```

<!-- category: NumberTheory -->
<!-- keywords: igcdex -->
<!-- signatures: igcdex(n, k) -->
### Function: igcdex (n, k)

リスト `[a, b, u]`を返します。
ここで、 *u*は*n*と *k*の最大公約数で、
*u*は `a n + b k`に等しいです。
引数 *n*と *k*は整数でなければいけません。


`igcdex`はユークリッドのアルゴリズムを実装します。
`gcdex`.も参照してください。


コマンド `load("gcdex")`はこの関数をロードします。


例:



```maxima
(%i1) load("gcdex")$

(%i2) igcdex(30,18);
(%o2)                      [- 1, 2, 6]
(%i3) igcdex(1526757668, 7835626735736);
(%o3)            [845922341123, - 164826435, 4]
(%i4) igcdex(fib(20), fib(21));
(%o4)                   [4181, - 2584, 1]
```

See also: `gcdex`.

<!-- category: NumberTheory -->
<!-- keywords: inrt -->
<!-- signatures: inrt(x, n) -->
### Function: inrt (x, n)

*x*の絶対値の整数*n*乗根を返します。



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], inrt (10^a, 3)), l);
(%o2) [2, 4, 10, 21, 46, 100, 215, 464, 1000, 2154, 4641, 10000]
```

<!-- category: NumberTheory -->
<!-- keywords: inv_mod -->
<!-- signatures: inv_mod(n, m) -->
### Function: inv_mod (n, m)

*m*を法とする*n*の逆元を計算します。
もし*n*が*m*を法とするゼロ因子なら、
`inv_mod (n,m)`は`false`を返します。



```maxima
(%i1) inv_mod(3, 41);
(%o1)                           14
(%i2) ratsimp(3^-1), modulus=41;
(%o2)                           14
(%i3) inv_mod(3, 42);
(%o3)                          false
```

<!-- category: NumberTheory -->
<!-- keywords: isqrt -->
<!-- signatures: isqrt(x) -->
### Function: isqrt (x)

整数 *x*の絶対値の「整数平方根」を返します。

<!-- category: NumberTheory -->
<!-- keywords: jacobi -->
<!-- signatures: jacobi(p, q) -->
### Function: jacobi (p, q)

*p*と*q*のJacobi記号を返します。



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], jacobi (a, 9)), l);
(%o2)         [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
```

<!-- category: NumberTheory -->
<!-- keywords: lcm -->
<!-- signatures: lcm(expr_1, ..., expr_n) -->
### Function: lcm (expr_1, ..., expr_n)

引数の最小公倍数を返します。
引数は、整数はもちろん一般式を取り得ます。


`load ("functs")`はこの関数をロードします。

<!-- category: NumberTheory -->
<!-- keywords: mod -->
<!-- signatures: mod(x, y) -->
### Function: mod (x, y)

もし*x*と*y*が実数で、*y*がゼロでないなら、
`x - y * floor(x / y)`を返します。
さらにすべての実数*x*に関して、`mod (x, 0) = x`が成り立ちます。
定義`mod (x, 0) = x`の議論に関しては、
Graham, Knuth, Patashnik著の「コンピュータの数学」の3.4節を参照してください。
関数`mod (x, 1)` は、周期が1で`mod (1, 1) = 0`、`mod (0, 1) = 0`ののこぎり波関数です。


複素数の偏角の主値（区間`(-%pi, %pi]`での数）を見つけるためには、
関数`x |-> %pi - mod (%pi - x, 2*%pi)`を使います。
*x*は引数です。


*x*と*y*が定数式(例えば、`10 * %pi`)の時、
`mod`は、`floor`や`ceiling`が使うのと同じ多倍長浮動小数点評価スキームを
使います。
再び同様に、まれですが、`mod`は間違った値を返すことがありえます。


数値でない引数*x*や*y*に関して,`mod`は、いくつかの式整理規則を知っています:









```maxima
(%i1) mod (x, 0);
(%o1)                           x
(%i2) mod (a*x, a*y);
(%o2)                      a mod(x, y)
(%i3) mod (0, x);
(%o3)                           0
```

<!-- category: NumberTheory -->
<!-- keywords: next_prime -->
<!-- signatures: next_prime(n) -->
### Function: next_prime (n)

*n*よりも大きな最も小さな素数を返します。



```maxima
(%i1) next_prime(27);
(%o1)                       29
```

<!-- category: NumberTheory -->
<!-- keywords: partfrac -->
<!-- signatures: partfrac(expr, var) -->
### Function: partfrac (expr, var)

主変数*var*に関する部分分数式*expr*を展開します。
`partfrac`は、完全な部分分数分解を行います。
利用したアルゴリズムは、
部分分数展開(元の分母の因子)の分母は互いに素であるという事実に基づいています。
分子は分母の線形結合として書け、結果が展開ということになります。



```maxima
(%i1) 1/(1+x)^2 - 2/(1+x) + 2/(2+x);
                      2       2        1
(%o1)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
(%i2) ratsimp (%);
                                 x
(%o2)                 - -------------------
                         3      2
                        x  + 4 x  + 5 x + 2
(%i3) partfrac (%, x);
                      2       2        1
(%o3)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
```

<!-- category: NumberTheory -->
<!-- keywords: power_mod -->
<!-- signatures: power_mod(a, n, m) -->
### Function: power_mod (a, n, m)

`a^n mod m`を計算するために
剰余アルゴリズムを使います。
ここで、*a*と*n*は整数で、*m*は正の整数です。
もし*n*が負なら、`inv_mod`が剰余逆元を見つけるために使われます。



```maxima
(%i1) power_mod(3, 15, 5);
(%o1)                          2
<(%i2) mod(3^15,5);
(%o2)                          2
(%i3) power_mod(2, -1, 5);
(%o3)                          3
(%i4) inv_mod(2,5);
(%o4)                          3
```

<!-- category: NumberTheory -->
<!-- keywords: prev_prime -->
<!-- signatures: prev_prime(n) -->
### Function: prev_prime (n)

*n*よりも小さな最大の素数を返します。



```maxima
(%i1) prev_prime(27);
(%o1)                       23
```

<!-- category: NumberTheory -->
<!-- keywords: primep -->
<!-- signatures: primep(n) -->
### Function: primep (n)

素数テスト。
もし`primep (n)`が`false`を返すなら、
*n*は合成数であり、
もし`true`を返すなら、*n*は非常に高い確立で素数です。


3317044064679887385961981より小さな*n*に対して、
Miller-Rabinのテストの決定的バージョンが使われます。
もし`primep (n)`が`true`を返すなら、
*n*は素数です。


3317044064679887385961981よりの大きな*n*に対して、
`primep`は、
`primep_number_of_tests`個のMiller-Rabinの疑似素数テストと
1つのLucasの疑似素数テストを使います。
*n*がMiller-Rabinのテスト１つを通過する確率は
1/4より小さいです。
`primep_number_of_tests`に関してデフォルト値25を使うと、
通過した*n*が合成である確率は
10^-15よりもはるかに小さいです。

<!-- category: NumberTheory -->
<!-- keywords: primep_number_of_tests -->
<!-- signatures: primep_number_of_tests -->
### Variable: primep_number_of_tests

デフォルト値: 25


`primep`の中で使われるMiller-Rabinのテストの回数。

<!-- category: NumberTheory -->
<!-- keywords: qunit -->
<!-- signatures: qunit(n) -->
### Function: qunit (n)

実二次数体`sqrt (n)`の基本単数、
すなわち、ノルムが1の要素を返します。
ここで、*n*は整数です。
これは、結果的にペル方程式`a^2 - n b^2 = 1`を解くことになります。



```maxima
(%i1) qunit (17);
(%o1)                     sqrt(17) + 4
(%i2) expand (% * (sqrt(17) - 4));
(%o2)                           1
```

<!-- category: NumberTheory -->
<!-- keywords: totient -->
<!-- signatures: totient(n) -->
### Function: totient (n)

*n*以下の、
*n*と互いに素な整数の数を返します。

<!-- category: NumberTheory -->
<!-- keywords: zerobern -->
<!-- signatures: zerobern -->
### Variable: zerobern

デフォルト値: `true`


`zerobern`が`false`の時、
`bern`はBernoulli数を除外し、`euler`はゼロに等しいEuler数を除外します。
`bern`と`euler`を参照してください。

<!-- category: NumberTheory -->
<!-- keywords: zeta -->
<!-- signatures: zeta(n) -->
### Function: zeta (n)

Riemannのゼータ関数を返します。
もし*x*が負の整数、0, 1,または、正の偶数なら、
Reimannのゼータ関数は厳密な値に整理されます。
正の偶数に対しては、
加えて、オプション変数`zeta%pi`は`true`でなければいけません。
(`zeta%pi`を参照してください。)
浮動小数点または多倍長浮動小数点数に対して、Reimannゼータ関数は数値的に評価されます。
Maximaは、
有理非整数、浮動小数点数、複素数の引数を含む
他の引数すべてに対して、また、もし`zeta%pi`が値`false`なら偶数に対して、
名詞形`zeta (n)`を返します。


`zeta(1)`は未定義ですが、
Maximaは上からと下からの極限`limit(zeta(x), x, ,1)`を知っています。


`bfzeta`と`zeta%pi`も参照してください。


例：









```maxima
(%i1) zeta([-2, -1, 0, 0.5, 2, 3, 1+%i]);
                                             2
            1     1                       %pi
(%o1) [0, - --, - -, - 1.460354508809586, ----, zeta(3), 
            12    2                        6
                                                    zeta(%i + 1)]
(%i2) limit(zeta(x),x,1,plus);
(%o2)                          inf
(%i3) limit(zeta(x),x,1,minus);
(%o3)                         minf
```

<!-- category: NumberTheory -->
<!-- keywords: zeta%pi -->
<!-- signatures: zeta%pi -->
### Variable: zeta%pi

デフォルト値: `true`


`zeta%pi`が`true`の時、
偶数`n`に対して、`zeta`は`%pi^n`に比例する式を返します。
そうでないなら、
偶数`n`に対して、`zeta`は名詞形`zeta (n)`を返します。


例:









```maxima
(%i1) zeta%pi: true$
(%i2) zeta (4);
                                 4
                              %pi
(%o2)                         ----
                               90
(%i3) zeta%pi: false$
(%i4) zeta (4);
(%o4)                        zeta(4)
```

