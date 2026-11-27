## orthopoly

<!-- category: Polynomials -->
<!-- keywords: assoc_legendre_p -->
<!-- signatures: assoc_legendre_p(n, m, x) -->
### Function: assoc_legendre_p (n, m, x)

次数 *n*と位数 *m*の第一種Legendre陪函数。


参考文献: Abramowitz and Stegun, equations 22.5.37, page 779, 8.6.6
(second equation), page 334, and 8.2.5, page 333.

<!-- category: Polynomials -->
<!-- keywords: assoc_legendre_q -->
<!-- signatures: assoc_legendre_q(n, m, x) -->
### Function: assoc_legendre_q (n, m, x)

次数 *n*と位数 *m*の第二種Legendre陪函数。


参考文献: Abramowitz and Stegun, equation 8.5.3 and 8.1.8.

<!-- category: Polynomials -->
<!-- keywords: chebyshev_t -->
<!-- signatures: chebyshev_t(n, x) -->
### Function: chebyshev_t (n, x)

第一種Chebyshev函数。


参考文献: Abramowitz and Stegun, equation 22.5.47, page 779.

<!-- category: Polynomials -->
<!-- keywords: chebyshev_u -->
<!-- signatures: chebyshev_u(n, x) -->
### Function: chebyshev_u (n, x)

第二種Chebyshev函数。


参考文献: Abramowitz and Stegun, equation 22.5.48, page 779.

<!-- category: Polynomials -->
<!-- keywords: gen_laguerre -->
<!-- signatures: gen_laguerre(n, a, x) -->
### Function: gen_laguerre (n, a, x)

次数 *n*の一般化Laguerre多項式。


参考文献: Abramowitz and Stegun, equation 22.5.54, page 780.

<!-- category: Polynomials -->
<!-- keywords: hermite -->
<!-- signatures: hermite(n, x) -->
### Function: hermite (n, x)

Hermite多項式。


参考文献: Abramowitz and Stegun, equation 22.5.55, page 780.

<!-- category: Polynomials -->
<!-- keywords: intervalp -->
<!-- signatures: intervalp(e) -->
### Function: intervalp (e)

もし入力が区間なら `true`を、
そうでないなら `false`を返します。

<!-- category: Polynomials -->
<!-- keywords: jacobi_p -->
<!-- signatures: jacobi_p(n, a, b, x) -->
### Function: jacobi_p (n, a, b, x)

Jacobiの多項式。


Jacobiの多項式は実際には
*a*と *b*すべてに対して定義されます;
しかし、Jacobi多項式の重み
`(1 - x)^a (1 + x)^b`は
`a <= -1`か `b <= -1`で可積分でありません。


参考文献: Abramowitz and Stegun, equation 22.5.42, page 779.

<!-- category: Polynomials -->
<!-- keywords: laguerre -->
<!-- signatures: laguerre(n, x) -->
### Function: laguerre (n, x)

Laguerre多項式。


参考文献: Abramowitz and Stegun, equations 22.5.16 and 22.5.54, page 780.

<!-- category: Polynomials -->
<!-- keywords: legendre_p -->
<!-- signatures: legendre_p(n, x) -->
### Function: legendre_p (n, x)

第一種Legendre多項式。


参考文献: Abramowitz and Stegun, equations 22.5.50 and 22.5.51, page 779.

<!-- category: Polynomials -->
<!-- keywords: legendre_q -->
<!-- signatures: legendre_q(n, x) -->
### Function: legendre_q (n, x)

第二種Legendre多項式。


参考文献: Abramowitz and Stegun, equations 8.5.3 and 8.1.8.

<!-- category: Polynomials -->
<!-- keywords: orthopoly_recur -->
<!-- signatures: orthopoly_recur(f, args) -->
### Function: orthopoly_recur (f, args)

引数 *args*を持つ直交函数族 *f*の漸化式を返します。
再帰は多項式次数に関してです。






```maxima
(%i1) orthopoly_recur (legendre_p, [n, x]);
                (2 n - 1) P     (x) x + (1 - n) P     (x)
                           n - 1                 n - 2
(%o1)   P (x) = -----------------------------------------
         n                          n
```


`orthopoly_recur`の二番目の引数は
関数 *f*の正しい数の引数のリストでなければいけません;
もしそうでないなら、Maximaはエラーをシグナルします。






```maxima
(%i1) orthopoly_recur (jacobi_p, [n, x]);

Function jacobi_p needs 4 arguments, instead it received 2
 -- an error.  Quitting.  To debug this try debugmode(true);
```


更に、
*f*が直交多項式族の1つの名前でないなら、
エラーがシグナルされます。






```maxima
(%i1) orthopoly_recur (foo, [n, x]);

A recursion relation for foo isn't known to Maxima
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Polynomials -->
<!-- keywords: orthopoly_returns_intervals -->
<!-- signatures: orthopoly_returns_intervals -->
### Variable: orthopoly_returns_intervals

デフォルト値: `true`


`orthopoly_returns_intervals`が `true`の時、
浮動小数点の結果が形式 `interval (c, r)`
で返されます。
ここで、 *c*は区間の中心で、
*r*は半径です。
中心は複素数であり得ます;
その場合、区間は複素平面上の円です。

<!-- category: Polynomials -->
<!-- keywords: orthopoly_weight -->
<!-- signatures: orthopoly_weight(f, args) -->
### Function: orthopoly_weight (f, args)

3つの要素のリストを返します;
一番目の要素は
リスト *args*が与える引数を持つ直交多項式族 *f*の重みの公式です;
二番目と三番目の要素は
直交性の区間の下限と上限を与えます。
例えば、







```maxima
(%i1) w : orthopoly_weight (hermite, [n, x]);
                            2
                         - x
(%o1)                 [%e    , - inf, inf]
(%i2) integrate(w[1]*hermite(3, x)*hermite(2, x), x, w[2], w[3]);
(%o2)                           0
```


*f*の主変数はシンボルでなければいけません;
そうでないなら、Maximaはエラーをシグナルします。

<!-- category: Polynomials -->
<!-- keywords: pochhammer -->
<!-- signatures: pochhammer(n, x) -->
### Function: pochhammer (n, x)

Pochhammerシンボル。
`n <= pochhammer_max_index`の非負整数 *n*に対して、
式 `pochhammer (x, n)`は
`n > 0`の時、
積 `x (x + 1) (x + 2) ... (x + n - 1)`
を評価します。
`n = 0`の時は1です。
負の *n*に対しては、
`pochhammer (x, n)`は
`(-1)^n / pochhammer (1 - x, -n)`として定義されます。
従って、







```maxima
(%i1) pochhammer (x, 3);
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, -3);
                                 1
(%o2)               - -----------------------
                      (1 - x) (2 - x) (3 - x)
```


Pochhammerシンボルをガンマ函数の商に変換するには、
(Abramowitz and Stegun, equation 6.1.22を参照してください)
`makegamma`を使ってください;
例えば、






```maxima
(%i1) makegamma (pochhammer (x, n));
                          gamma(x + n)
(%o1)                     ------------
                            gamma(x)
```


*n*が `pochhammer_max_index`を越えるか、
*n*が記号の時、
`pochhammer`は名詞形を返します。






```maxima
(%i1) pochhammer (x, n);
(%o1)                         (x)
                                 n
```

<!-- category: Polynomials -->
<!-- keywords: pochhammer_max_index -->
<!-- signatures: pochhammer_max_index -->
### Variable: pochhammer_max_index

デフォルト値: 100


`pochhammer (n, x)`は
`n <= pochhammer_max_index`の時だけ
積を展開します。


例:







```maxima
(%i1) pochhammer (x, 3), pochhammer_max_index : 3;
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, 4), pochhammer_max_index : 3;
(%o2)                         (x)
                                 4
```


参考文献: Abramowitz and Stegun, equation 6.1.16, page 256.

<!-- category: Polynomials -->
<!-- keywords: spherical_bessel_j -->
<!-- signatures: spherical_bessel_j(n, x) -->
### Function: spherical_bessel_j (n, x)

第一種球Bessel函数。


参考文献: Abramowitz and Stegun, equations 10.1.8, page 437 and 10.1.15, page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_bessel_y -->
<!-- signatures: spherical_bessel_y(n, x) -->
### Function: spherical_bessel_y (n, x)

第二種球Bessel函数。


参考文献: Abramowitz and Stegun, equations 10.1.9, page 437 and 10.1.15, page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_hankel1 -->
<!-- signatures: spherical_hankel1(n, x) -->
### Function: spherical_hankel1 (n, x)

第一種球Hankel函数。


参考文献: Abramowitz and Stegun, equation 10.1.36, page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_hankel2 -->
<!-- signatures: spherical_hankel2(n, x) -->
### Function: spherical_hankel2 (n, x)

第二種球Hankel函数。


参考文献: Abramowitz and Stegun, equation 10.1.17, page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_harmonic -->
<!-- signatures: spherical_harmonic(n, m, x, y) -->
### Function: spherical_harmonic (n, m, x, y)

球調和函数。


参考文献: Merzbacher 9.64.

<!-- category: Polynomials -->
<!-- keywords: ultraspherical -->
<!-- signatures: ultraspherical(n, a, x) -->
### Function: ultraspherical (n, a, x)

(Gegenbauer多項式としても知られている)超球多項式。


参考文献: Abramowitz and Stegun, equation 22.5.46, page 779.

<!-- category: Polynomials -->
<!-- keywords: unit_step -->
<!-- signatures: unit_step(x) -->
### Function: unit_step (x)

左連続の単位階段函数;なので
`unit_step (x)`は`x <= 0`で0であり、
`x > 0`で1です。


もし0で値1/2を取る単位階段函数が欲しいなら、
`(1 + signum (x))/2`を使ってください。

