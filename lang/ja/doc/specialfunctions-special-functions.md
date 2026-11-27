## Special Functions

<!-- category: SpecialFunctions -->
<!-- keywords: %f -->
<!-- signatures: %f[p, q]([a],[b],z) -->
### Function: %f ([p, q]([a],[b],z))

pFq(a1,a2,..ap;b1,b2,..bq;z)超幾何関数。
ここで、`a`は長さ`p`のリストで、
`b`は長さ`q`のリストです。

<!-- category: SpecialFunctions -->
<!-- keywords: %m -->
<!-- signatures: %m[k, u](z) -->
### Function: %m ([k, u](z))

Whittaker M関数
`M[k,u](z) = exp(-z/2)*z^(1/2+u)*M(1/2+u-k,1+2*u,z)`.  
(A&S 13.1.32)

<!-- category: SpecialFunctions -->
<!-- keywords: %s -->
<!-- signatures: %s[u, v](z) -->
### Function: %s ([u, v](z))

Lommelの小s[u,v](z)関数。
多分Gradshteyn & Ryzhik 8.570.1.

<!-- category: SpecialFunctions -->
<!-- keywords: %w -->
<!-- signatures: %w[k, u](z) -->
### Function: %w ([k, u](z))

Whittaker W関数  (A&S 13.1.33)

<!-- category: SpecialFunctions -->
<!-- keywords: airy_ai -->
<!-- signatures: airy_ai(x) -->
### Function: airy_ai (x)

エアリー関数Ai(x)。  (A&S 10.4.2)


導関数`diff (airy_ai(x), x)`は、`airy_dai(x)`です。


`airy_bi`, `airy_dai`, `airy_dbi`も参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: airy_bi -->
<!-- signatures: airy_bi(x) -->
### Function: airy_bi (x)

エアリー関数Bi(x)。 (A&S 10.4.3)


導関数`diff (airy_bi(x), x)`は`airy_dbi(x)`です。


`airy_ai`, `airy_dbi`を参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: airy_dai -->
<!-- signatures: airy_dai(x) -->
### Function: airy_dai (x)

エアリー関数Ai `airy_ai(x)`の導関数。


`airy_ai`を参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: airy_dbi -->
<!-- signatures: airy_dbi(x) -->
### Function: airy_dbi (x)

エアリーBi関数`airy_bi(x)`の導関数。


`airy_ai`と`airy_bi`を参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_i -->
<!-- signatures: bessel_i(v, z) -->
### Function: bessel_i (v, z)

次数$v$、独立変数$z$の第一種変形ベッセル関数


`bessel_i`は以下のように定義されます。


```maxima
inf
                    ====   - v - 2 k  v + 2 k
                    \     2          z
                     >    -------------------
                    /     k! gamma(v + k + 1)
                    ====
                    k = 0
```



$$
\sum_{k=0}^{\infty } {{1\over{k!\,\Gamma
 \left(v+k+1\right)}} {\left(z\over 2\right)^{v+2\,k}}}
$$


無限級数は計算には使われませんが。

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_j -->
<!-- signatures: bessel_j(v, z) -->
### Function: bessel_j (v, z)

次数$v$と独立変数$z$の第一種ベッセル関数。


`bessel_j`は以下のように定義されます。



```maxima
inf
                ====       k  - v - 2 k  v + 2 k
                \     (- 1)  2          z
                 >    --------------------------
                /        k! gamma(v + k + 1)
                ====
                k = 0
```



$$
\sum_{k=0}^{\infty }{{{\left(-1\right)^{k}\,\left(z\over 2\right)^{v+2\,k}
 }\over{k!\,\Gamma\left(v+k+1\right)}}}
$$


計算のために無限級数は使われませんが。

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_k -->
<!-- signatures: bessel_k(v, z) -->
### Function: bessel_k (v, z)

次数$v$、独立変数$z$の第二種変形ベッセル関数


$v$が整数の時
`bessel_k`は以下のように定義されます。


```maxima
%pi csc(%pi v) (bessel_i(-v, z) - bessel_i(v, z))
           -------------------------------------------------
                                  2
```


$$
{{\pi\,\csc \left(\pi\,v\right)\,\left(I_{-v}(z)-I_{v}(z)\right)}\over{2}}
$$


もし$v$が整数$n$でないなら、
$v$が$n$に近づく極限が取られます。

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_y -->
<!-- signatures: bessel_y(v, z) -->
### Function: bessel_y (v, z)

次数$v$と独立変数$z$の第二種ベッセル関数


$v$が整数でない時、
`bessel_y`は以下のように定義されます。


```maxima
cos(%pi v) bessel_j(v, z) - bessel_j(-v, z)
              -------------------------------------------
                             sin(%pi v)
```



$$
{{\cos \left(\pi\,v\right)\,J_{v}(z)-J_{-v}(z)}\over{
 \sin \left(\pi\,v\right)}}
$$


$v$が整数$n$の時、
$v$が$n$に近づく極限が取られます。

<!-- category: SpecialFunctions -->
<!-- keywords: besselexpand -->
<!-- signatures: besselexpand -->
### Variable: besselexpand

デフォルト値: `false`



次数が半奇数の時のベッセル関数の展開を制御します。
この場合、ベッセル関数は他の初等関数で展開することができます。
`besselexpand`が`true`の時、
ベッセル関数は展開されます。



```maxima
(%i1) besselexpand: false$
(%i2) bessel_j (3/2, z);
                                    3
(%o2)                      bessel_j(-, z)
                                    2
(%i3) besselexpand: true$
(%i4) bessel_j (3/2, z);
                                        sin(z)   cos(z)
                       sqrt(2) sqrt(z) (------ - ------)
                                           2       z
                                          z
(%o4)                  ---------------------------------
                                   sqrt(%pi)
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta -->
<!-- signatures: beta(a, b) -->
### Function: beta (a, b)

ベータ関数は、`gamma(a) gamma(b)/gamma(a+b)` 
(A&S 6.2.1)として定義されます。


Maximaは、正の整数と、合計すると整数になる有理数についてベータ関数を整理します。
`beta_args_sum_to_integer`が`true`の時、
Maximaは、和が整数になる一般式も整理します。


*a*もしくは*b*がゼロに等しい時には、ベータ関数は未定義です。


一般にベータ関数は、負の整数の引数で未定義です。
例外は、*a=-n*―*n*は正の整数―かつ*b*が*b<=n*の正の整数で、
解析接続を定義することが可能です。
Maximaはこの場合結果を与えます。


`beta_expand`が`true`の時、
`n`を整数とする`beta(a+n,b)`と`beta(a-n,b)`、
もしくは`beta(a,b+n)`と`beta(a,b-n)`
のような式は整理されます。


Maximaは、実数値と複素数値のベータ関数を浮動小数点と多倍長浮動小数点精度で評価できます。
数値評価のために、Maximaは`log_gamma`を使います:



```maxima
- log_gamma(b + a) + log_gamma(b) + log_gamma(a)
         %e
```


Maximaは、ベータ関数が対称で、鏡像対称性を持つことを知っています。


Maximaは、*a*または*b*に関するベータ関数の導関数を知っています。


ベータ関数をガンマ関数の比として表現するには、`makegamma`を参照してください。


例:


引数の１つが整数の時の整理:



```maxima
(%i1) [beta(2,3),beta(2,1/3),beta(2,a)];
                               1   9      1
(%o1)                         [--, -, ---------]
                               12  4  a (a + 1)
```


２つの有理数引数の和が整数になる時の整理:



```maxima
(%i2) [beta(1/2,5/2),beta(1/3,2/3),beta(1/4,3/4)];
                          3 %pi   2 %pi
(%o2)                    [-----, -------, sqrt(2) %pi]
                            8    sqrt(3)
```


`beta_args_sum_to_integer`を`true`に設定した時、
引数の和が整数の時、さらに一般的な式が整理されます:



```maxima
(%i3) beta_args_sum_to_integer:true$
(%i4) beta(a+1,-a+2);
                                %pi (a - 1) a
(%o4)                         ------------------
                              2 sin(%pi (2 - a))
```


引数の１つが負の整数の時、可能な結果: 



```maxima
(%i5) [beta(-3,1),beta(-3,2),beta(-3,3)];
                                    1  1    1
(%o5)                            [- -, -, - -]
                                    3  6    3
```


`beta_expand`が`true`の時、
`n`が整数の`beta(a+n,b)`または`beta(a-n)`は整理されます:



```maxima
(%i6) beta_expand:true$
(%i7) [beta(a+1,b),beta(a-1,b),beta(a+1,b)/beta(a,b+1)];
                    a beta(a, b)  beta(a, b) (b + a - 1)  a
(%o7)              [------------, ----------------------, -]
                       b + a              a - 1           b
```


引数の１つがゼロの時、ベータは未定義です:



```maxima
(%i7) beta(0,b);
beta: expected nonzero arguments; found 0, b
 -- an error.  To debug this try debugmode(true);
```


実数値と複素数値の浮動小数点または多倍長浮動小数点精度での数値評価:



```maxima
(%i8) beta(2.5,2.3);
(%o8) .08694748611299981

(%i9) beta(2.5,1.4+%i);
(%o9) 0.0640144950796695 - .1502078053286415 %i

(%i10) beta(2.5b0,2.3b0);
(%o10) 8.694748611299969b-2

(%i11) beta(2.5b0,1.4b0+%i);
(%o11) 6.401449507966944b-2 - 1.502078053286415b-1 %i
```


ベータは対称で、鏡像対称性を持ちます:



```maxima
(%i14) beta(a,b)-beta(b,a);
(%o14)                                 0
(%i15) declare(a,complex,b,complex)$
(%i16) conjugate(beta(a,b));
(%o16)                 beta(conjugate(a), conjugate(b))
```


`a`に関するベータ関数の導関数:


```maxima
(%i17) diff(beta(a,b),a);
(%o17)               - beta(a, b) (psi (b + a) - psi (a))
                                      0             0
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta_args_sum_to_integer -->
<!-- signatures: beta_args_sum_to_integer -->
### Variable: beta_args_sum_to_integer

デフォルト値: false


`beta_args_sum_to_integer`が`true`の時、
引数*a*と*b*の和が整数の時、
Maximaは`beta(a,b)`を整理します。

<!-- category: SpecialFunctions -->
<!-- keywords: beta_expand -->
<!-- signatures: beta_expand -->
### Variable: beta_expand

デフォルト値: false


`beta_expand`が`true`の時、
$a+n$や$a-n$のような引数に対して
`beta(a,b)` と、関連した関数は展開されます。
ここで$n$は整数です。

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete -->
<!-- signatures: beta_incomplete(a, b, z) -->
### Function: beta_incomplete (a, b, z)

不完全ベータ関数の基本定義(A&S 6.6.1)は、以下の通りです。



```maxima
z
       /
       [         b - 1  a - 1
       I  (1 - t)      t      dt
       ]
       /
        0
```


この定義は、$realpart(a)>0$かつ$realpart(b)>0$かつ$abs(z)<1$で可能です。
他の値では不完全ベータ関数は一般化超幾何関数を通じて定義することができます。



```maxima
gamma(a) hypergeometric_generalized([a, 1 - b], [a + 1], z) z
```


(不完全ベータ関数の完全な定義については、functions.wolfram.comを参照してください。
)


負の整数$a = -n$と正の整数$b=m$で、$m<=n$の場合、
不完全ベータ関数は以下を通して定義されます。



```maxima
m - 1           k
                            ====  (1 - m)  z
                      n - 1 \            k
                     z       >    -----------
                            /     k! (n - k)
                            ====
                            k = 0
```


Maximaは、
負の整数*a*に関する`beta_incomplete`を整理するために、この定義を使います。


*a*が正の整数の時、
任意の引数*b*, *z*に関して、
*b*が正の整数の時、
非負の整数*a*, 任意の*z*に関して、
`beta_incomplete`は整理されます。


$z=0$かつ$realpart(a)>0$の時、`beta_incomplete`は特別な値ゼロを取ります。
*z=1*かつ$realpart(b)>0$の時、
`beta_incomplete`はベータ関数`beta(a,b)`に整理されます。


Maximaは、浮動小数点か多倍長浮動小数点精度の実数値と複素数値に対して、
`beta_incomplete`を数値的に評価します。
数値評価に関して、
不完全ベータ函数の連分数展開を使います。


オプション変数`beta_expand`が`true`の時、
Maximaは`beta_incomplete(a+n,b,z)`や`beta_incomplete(a-n,b,z)`のような式を展開します。ここでnは正の整数です。


Maximaは`beta_incomplete`の変数*a*, *b*, *z*についての導関数と
変数*z*についての積分を知っています。


例:


正の整数*a*に関する整理:



```maxima
(%i1) beta_incomplete(2,b,z);
                                       b
                            1 - (1 - z)  (b z + 1)
(%o1)                       ----------------------
                                  b (b + 1)
```


正の整数*b*に関する整理:



```maxima
(%i2) beta_incomplete(a,2,z);
                                               a
                              (a (1 - z) + 1) z
(%o2)                         ------------------
                                  a (a + 1)
```


正の整数*a*, *b*に関する整理:



```maxima
(%i3) beta_incomplete(3,2,z);

                                               3
                              (3 (1 - z) + 1) z
(%o3)                         ------------------
                                      12
```


*a*が負の整数かつ$b<=(-a)$の時、Maximaは整理します:



```maxima
(%i4) beta_incomplete(-3,1,z);
                                       1
(%o4)                              - ----
                                        3
                                     3 z
```


特定の値$z=0$と$z=1$に関して, Maximaは整理します:



```maxima
(%i5) assume(a>0,b>0)$
(%i6) beta_incomplete(a,b,0);
(%o6)                                 0
(%i7) beta_incomplete(a,b,1);
(%o7)                            beta(a, b)
```


浮動小数点または多倍長浮動小数点精度の数値評価:



```maxima
(%i8) beta_incomplete(0.25,0.50,0.9);
(%o8)                          4.594959440269333
(%i9)  fpprec:25$
(%i10) beta_incomplete(0.25,0.50,0.9b0);
(%o10)                    4.594959440269324086971203b0
```


$abs(z)>1$の時、`beta_incomplete`は複素数を返します:



```maxima
(%i11) beta_incomplete(0.25,0.50,1.7);
(%o11)              5.244115108584249 - 1.45518047787844 %i
```


もっと一般的な複素引数に関する結果:



```maxima
(%i14) beta_incomplete(0.25+%i,1.0+%i,1.7+%i);
(%o14)             2.726960675662536 - .3831175704269199 %i
(%i15) beta_incomplete(1/2,5/4*%i,2.8+%i);
(%o15)             13.04649635168716 %i - 5.802067956270001
(%i16)
```


`beta_expand`が`true`の時の展開:



```maxima
(%i23) beta_incomplete(a+1,b,z),beta_expand:true;
                                                       b  a
                   a beta_incomplete(a, b, z)   (1 - z)  z
(%o23)             -------------------------- - -----------
                             b + a                 b + a

(%i24) beta_incomplete(a-1,b,z),beta_expand:true;
                                                           b  a - 1
           beta_incomplete(a, b, z) (- b - a + 1)   (1 - z)  z
(%o24)     -------------------------------------- - ---------------
                           1 - a                         1 - a
```

 

`beta_incomplete`の微分と積分:



```maxima
(%i34) diff(beta_incomplete(a, b, z), z);

                              b - 1  a - 1
(%o34)                 (1 - z)      z

(%i35) integrate(beta_incomplete(a, b, z), z);
              b  a
       (1 - z)  z
(%o35) ----------- + beta_incomplete(a, b, z) z
          b + a
                                       a beta_incomplete(a, b, z)
                                     - --------------------------
                                                 b + a
(%i36) factor(diff(%, z));
(%o36)              beta_incomplete(a, b, z)
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete_generalized -->
<!-- signatures: beta_incomplete_generalized(a, b, z1, z2) -->
### Function: beta_incomplete_generalized (a, b, z1, z2)

一般化不完全ベータ関数の基本的な定義は、以下の通りです。



```maxima
z2
           /
           [          b - 1  a - 1
           I   (1 - t)      t      dt
           ]
           /
            z1
```


Maximaは、
*a*と*b*が正の整数の時、
`beta_incomplete_regularized`を整理します。


$realpart(a)>0$かつ$z1=0$または$z2=0$の時、
Maximaは、
`beta_incomplete_generalized`を`beta_incomplete`に整理します。
$realpart(b)>0$かつ$z1=1$または*z2=1*の時、
Maximaは、`beta`と`beta_incomplete`を含む式に整理します。


Maximaは、実数値と複素数値に関して、浮動小数点と多倍長浮動小数点精度で
`beta_incomplete_regularized`を評価します。


`beta_expand`が`true`の時、
*n*を正の整数とすると、
Maximaは、$a+n$や$a-n$に関して`beta_incomplete_generalized`
を整理します。


Maximaは、
変数*a*, *b*, *z1*, *z2*に関する
`beta_incomplete_generalized`の微分を知っており、
変数*z1*や*z2*に関する積分を知っています。


例:


Maximaは、*a*と*b*が正の整数の時、
`beta_incomplete_generalized`を整理します:



```maxima
(%i1) beta_incomplete_generalized(2,b,z1,z2);
                   b                      b
           (1 - z1)  (b z1 + 1) - (1 - z2)  (b z2 + 1)
(%o1)      -------------------------------------------
                            b (b + 1)
(%i2) beta_incomplete_generalized(a,2,z1,z2);

                              a                      a
           (a (1 - z2) + 1) z2  - (a (1 - z1) + 1) z1
(%o2)      -------------------------------------------
                            a (a + 1)

(%i3) beta_incomplete_generalized(3,2,z1,z2);
              2      2                       2      2
      (1 - z1)  (3 z1  + 2 z1 + 1) - (1 - z2)  (3 z2  + 2 z2 + 1)
(%o3) -----------------------------------------------------------
                                  12
```


特定の値$z1=0$, $z2=0$, $z1=1$または$z2=1$に関する整理:



```maxima
(%i4) assume(a > 0, b > 0)$
(%i5) beta_incomplete_generalized(a,b,z1,0);
(%o5)                    - beta_incomplete(a, b, z1)

(%i6) beta_incomplete_generalized(a,b,0,z2);
(%o6)                    - beta_incomplete(a, b, z2)

(%i7) beta_incomplete_generalized(a,b,z1,1);
(%o7)              beta(a, b) - beta_incomplete(a, b, z1)

(%i8) beta_incomplete_generalized(a,b,1,z2);
(%o8)              beta_incomplete(a, b, z2) - beta(a, b)
```


浮動小数点もしくは多倍長浮動小数点精度での実数値引数に関する数値評価:



```maxima
(%i9) beta_incomplete_generalized(1/2,3/2,0.25,0.31);
(%o9)                        .09638178086368676

(%i10) fpprec:32$
(%i10) beta_incomplete_generalized(1/2,3/2,0.25,0.31b0);
(%o10)               9.6381780863686935309170054689964b-2
```


浮動小数点もしくは多倍長浮動小数点精度での複素数値引数に関する数値評価:



```maxima
(%i11) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31);
(%o11)           - .09625463003205376 %i - .003323847735353769
(%i12) fpprec:20$
(%i13) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31b0);
(%o13)     - 9.6254630032054178691b-2 %i - 3.3238477353543591914b-3
```


`beta_expand`が`true`の時、
*n*を正の整数とする、
$a+n$または$a-n$に関する整理:



```maxima
(%i14) beta_expand:true$

(%i15) beta_incomplete_generalized(a+1,b,z1,z2);

               b   a           b   a
       (1 - z1)  z1  - (1 - z2)  z2
(%o15) -----------------------------
                   b + a
                      a beta_incomplete_generalized(a, b, z1, z2)
                    + -------------------------------------------
                                         b + a
(%i16) beta_incomplete_generalized(a-1,b,z1,z2);

       beta_incomplete_generalized(a, b, z1, z2) (- b - a + 1)
(%o16) -------------------------------------------------------
                                1 - a
                                    b   a - 1           b   a - 1
                            (1 - z2)  z2      - (1 - z1)  z1
                          - -------------------------------------
                                            1 - a
```


変数*z1*に関する微分と*z1*や*z2*に関する積分:



```maxima
(%i17) diff(beta_incomplete_generalized(a,b,z1,z2),z1);
                               b - 1   a - 1
(%o17)               - (1 - z1)      z1
(%i18) integrate(beta_incomplete_generalized(a,b,z1,z2),z1);
(%o18) beta_incomplete_generalized(a, b, z1, z2) z1
                                  + beta_incomplete(a + 1, b, z1)
(%i19) integrate(beta_incomplete_generalized(a,b,z1,z2),z2);
(%o19) beta_incomplete_generalized(a, b, z1, z2) z2
                                  - beta_incomplete(a + 1, b, z2)
```

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete_regularized -->
<!-- signatures: beta_incomplete_regularized(a, b, z) -->
### Function: beta_incomplete_regularized (a, b, z)

```maxima
beta_incomplete_regularized(a, b, z) = 
                                      beta_incomplete(a, b, z)
                                      ------------------------
                                             beta(a, b)
```

として定義された正則不完全ベータ関数 A&S 6.6.2。


`beta_incomplete`同様、この定義は完全ではありません。
`beta_incomplete_regularized`の完全な定義については、functions.wolfram.comを参照してください。


`beta_incomplete_regularized`は、*a*または*b*が正の整数の時
整理されます。


$z=0$かつ$realpart(a)>0$の時、
`beta_incomplete_regularized`は、具体的な値0を持ちます。
*z=1*かつ$realpart(b)>0$の時、
`beta_incomplete_regularized`は、1に整理されます。


Maximaは、実数と複素数の引数について、
浮動小数点と多倍長浮動小数点精度で`beta_incomplete_regularized`を評価します。


`beta_expand`が`true`の時、
Maximaは、
nは整数として、引数$a+n$または$a-n$に関して
`beta_incomplete_regularized`を展開します。


Maximaは、変数*a*, *b*, *z*に関する
`beta_incomplete_regularized`の導関数と、
変数*z*に関する積分を知っています。


例:


*a*または*b*が正の整数の時の整理:



```maxima
(%i1) beta_incomplete_regularized(2,b,z);
                                       b
(%o1)                       1 - (1 - z)  (b z + 1)

(%i2) beta_incomplete_regularized(a,2,z);
                                               a
(%o2)                         (a (1 - z) + 1) z

(%i3) beta_incomplete_regularized(3,2,z);
                                               3
(%o3)                         (3 (1 - z) + 1) z
```


特定の値$z=0$, $z=1$について、Maximaは整理します:



```maxima
(%i4) assume(a>0,b>0)$
(%i5) beta_incomplete_regularized(a,b,0);
(%o5)                                 0
(%i6) beta_incomplete_regularized(a,b,1);
(%o6)                                 1
```


実数と複素数引数に関する浮動小数点または多倍長浮動小数点精度の数値評価:



```maxima
(%i7) beta_incomplete_regularized(0.12,0.43,0.9);
(%o7)                         .9114011367359802
(%i8) fpprec:32$
(%i9) beta_incomplete_regularized(0.12,0.43,0.9b0);
(%o9)               9.1140113673598075519946998779975b-1
(%i10) beta_incomplete_regularized(1+%i,3/3,1.5*%i);
(%o10)             .2865367499935403 %i - 0.122995963334684
(%i11) fpprec:20$
(%i12) beta_incomplete_regularized(1+%i,3/3,1.5b0*%i);
(%o12)      2.8653674999354036142b-1 %i - 1.2299596333468400163b-1
```


`beta_expand`が`true`の時の展開:



```maxima
(%i13) beta_incomplete_regularized(a+1,b,z);
                                                     b  a
                                              (1 - z)  z
(%o13) beta_incomplete_regularized(a, b, z) - ------------
                                              a beta(a, b)
(%i14) beta_incomplete_regularized(a-1,b,z);
(%o14) beta_incomplete_regularized(a, b, z)
                                                     b  a - 1
                                              (1 - z)  z
                                         - ----------------------
                                           beta(a, b) (b + a - 1)
```


*z*に関する微分と積分:



```maxima
(%i15) diff(beta_incomplete_regularized(a,b,z),z);
                              b - 1  a - 1
                       (1 - z)      z
(%o15)                 -------------------
                           beta(a, b)
(%i16) integrate(beta_incomplete_regularized(a,b,z),z);
(%o16) beta_incomplete_regularized(a, b, z) z
                                                           b  a
                                                    (1 - z)  z
          a (beta_incomplete_regularized(a, b, z) - ------------)
                                                    a beta(a, b)
        - -------------------------------------------------------
                                   b + a
```

<!-- category: SpecialFunctions -->
<!-- keywords: bffac -->
<!-- signatures: bffac(expr, n) -->
### Function: bffac (expr, n)

階乗（シフトガンマ）関数の多倍長浮動小数点バージョン。
２番目の引数は、保持し返すディジットの数です。
少しの余分を要請するのはいい考えです。

<!-- category: SpecialFunctions -->
<!-- keywords: bfpsi, bfpsi0 -->
<!-- signatures: bfpsi(n, z, fpprec), bfpsi0(z, fpprec) -->
### Function: bfpsi (n, z, fpprec)

`bfpsi`は、実引数*z*と整数次数*n*の多ガンマ関数です。
`bfpsi0`はディガンマ関数です。
`bfpsi0 (z, fpprec)`は`bfpsi (0, z, fpprec)`と同値です。


これらの関数は多倍長浮動小数点値を返します。
*fpprec*は戻り値の多倍長浮動小数点精度です。

<!-- category: SpecialFunctions -->
<!-- keywords: cbffac -->
<!-- signatures: cbffac(z, fpprec) -->
### Function: cbffac (z, fpprec)

複素多倍長浮動小数点の階乗です。


`load ("bffac")`はこの関数をロードします。

<!-- category: SpecialFunctions -->
<!-- keywords: erf -->
<!-- signatures: erf(z) -->
### Function: erf (z)

誤差関数erf(z) (A&S 7.1.1)


See also flag `erfflag`.

<!-- category: SpecialFunctions -->
<!-- keywords: erf_generalized -->
<!-- signatures: erf_generalized(z1, z2) -->
### Function: erf_generalized (z1, z2)

一般化誤差関数Erf(z1,z2)

<!-- category: SpecialFunctions -->
<!-- keywords: erf_representation -->
<!-- signatures: erf_representation -->
### Variable: erf_representation

デフォルト値: false


`true`の時、 erfc, erfi, erf_generalized, fresnel_s, fresnel_c
は、erfに変換されます。

<!-- category: SpecialFunctions -->
<!-- keywords: erfc -->
<!-- signatures: erfc(z) -->
### Function: erfc (z)

相補誤差関数erfc(z) (A&S 7.1.2)


`erfc(z) = 1-erf(z)`

<!-- category: SpecialFunctions -->
<!-- keywords: erfi -->
<!-- signatures: erfi(z) -->
### Function: erfi (z)

虚数誤差関数


`erfi(z) = -%i*erf(%i*z)`

<!-- category: SpecialFunctions -->
<!-- keywords: fresnel_c -->
<!-- signatures: fresnel_c(z) -->
### Function: fresnel_c (z)

フレネル積分C(z) = integrate(cos((%pi/2)*t^2),t,0,z) (A&S 7.3.1)


フラグ`trigsign`が`true`の時、
整理 fresnel_c(-x) = -fresnel_c(x)
が適用されます。


フラグ`%iargs`が`true`の時、
整理 fresnel_c(%i*x) =  %i*fresnel_c(x) 
が適用されます。



フラグ`erf_representation`と`hypergeometric_representation`を参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: fresnel_s -->
<!-- signatures: fresnel_s(z) -->
### Function: fresnel_s (z)

フレネル積分S(z) = integrate(sin((%pi/2)*t^2),t,0,z). (A&S 7.3.2)


フラグ`trigsign`が`true`の時、
整理fresnel_s(-x) = -fresnel_s(x)
が適用されます。


フラグ`%iargs`が`true`の時、
整理 fresnel_s(%i*x) =  %i*fresnel_s(x)
が適用されます。


フラグ`erf_representation`と`hypergeometric_representation`を参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: gamma -->
<!-- signatures: gamma(z) -->
### Function: gamma (z)

ガンマ関数の基本的な定義 (A&S 6.1.1) は、



```maxima
inf
                        /
                        [     z - 1   - t
             gamma(z) = I    t      %e    dt
                        ]
                        /
                         0
```


$$
¥Gamma¥left(z¥right)=¥int_{0}^{¥infty }{t^{z-1}¥,e^ {- t }¥;dt}
$$

です。


Maximaは、正の整数と正負の有理数に関して、`gamma`を整理します。
半整数値に関して、結果は有理数掛ける`sqrt(%pi)`です。
整数値に関する整理は、`factlim`によって制御されます。


`factlim`より大きな整数に関して、
階乗関数ー`gamma`を計算するのに使われますーの数値的な結果はオーバーフローします。
有理数に関する整理は、内部オーバーフローを避けるために、
`gammalim`によって制御されます。
`factlim`と`gammalim`も参照してください。


負の整数に関して、`gamma`は未定義です。


Maximaは、浮動小数点および多倍長浮動小数点の実数値および複素数値に関して、
`gamma`を数値的に評価できます。


`gamma`は鏡像対称性を持ちます。


`gamma_expand`が`true`の時、
Maximaは、
引数`z+n`と`z-n`―`n`は整数―の`gamma`を
展開します。


Maximaは、`gamma`の導関数を知っています。


例:


整数、半整数、有理数に関する整理:



```maxima
(%i1) map('gamma,[1,2,3,4,5,6,7,8,9]);
(%o1)        [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
(%i2) map('gamma,[1/2,3/2,5/2,7/2]);
                    sqrt(%pi)  3 sqrt(%pi)  15 sqrt(%pi)
(%o2)   [sqrt(%pi), ---------, -----------, ------------]
                        2           4            8
(%i3) map('gamma,[2/3,5/3,7/3]);
                                  2           1
                          2 gamma(-)  4 gamma(-)
                      2           3           3
(%o3)          [gamma(-), ----------, ----------]
                      3       3           9
```


実数と複素数の数値評価:



```maxima
(%i4) map('gamma,[2.5,2.5b0]);
(%o4)     [1.329340388179137, 1.329340388179137b0]
(%i5) map('gamma,[1.0+%i,1.0b0+%i]);
(%o5) [.4980156681183558 - .1549498283018108 %i, 
         4.980156681183561b-1 - 1.549498283018107b-1 %i]
```


`gamma`は鏡像対称性を持ちます:



```maxima
(%i6) declare(z,complex)$
(%i7) conjugate(gamma(z));
(%o7)                  gamma(conjugate(z))
```


`gamma_expand`が`true`の時
Maximaは、`gamma(z+n)`と`gamma(z-n)`を展開します:



```maxima
(%i8) gamma_expand:true$

(%i9) [gamma(z+1),gamma(z-1),gamma(z+2)/gamma(z+1)];
                               gamma(z)
(%o9)             [z gamma(z), --------, z + 1]
                                z - 1
```


`gamma`の導関数:



```maxima
(%i10) diff(gamma(z),z);
(%o10)                  psi (z) gamma(z)
                           0
```


`makegamma`も参照してください。


オイラー-マスケローニ定数は`%gamma`です。

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete -->
<!-- signatures: gamma_incomplete(a, z) -->
### Function: gamma_incomplete (a, z)

第二種不完全ガンマ関数 A&S 6.5.2:



```maxima
inf
                             /
                             [     a - 1   - t
    gamma_incomplete(a, z) = I    t      %e    dt
                             ]
                             /
                              z
```


$$
¥Gamma¥left(a , z¥right)=¥int_{z}^{¥infty }{t^{a-1}¥,e^ {- t }¥;dt}
$$

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_generalized -->
<!-- signatures: gamma_incomplete_generalized(a, z1, z1) -->
### Function: gamma_incomplete_generalized (a, z1, z1)

一般化不完全ガンマ関数



```maxima
gamma_incomplete_generalized(a, z1, z2) = 
                                               z2
                                              /
                                              [    a - 1   - t
                                              I   t      %e    dt
                                              ]
                                              /
                                               z1
```


$$
¥Gamma¥left(a , z_{1}, z_{2}¥right)=¥int_{z_{1}}^{z_{2}}{t^{a-1}¥,e^ {- t }¥;dt}
$$

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_regularized -->
<!-- signatures: gamma_incomplete_regularized(a, z) -->
### Function: gamma_incomplete_regularized (a, z)

正則第二種不完全ガンマ関数 A&S 6.5.1:



```maxima
gamma_incomplete_regularized(a, z) = 
                                        gamma_incomplete(a, z)
                                        ----------------------
                                               gamma(a)
```


$$
{¥it Q}¥left(a , z¥right)={{¥Gamma¥left(a , z¥right)}¥over{¥Gamma¥left(a¥right)}}
$$

<!-- category: SpecialFunctions -->
<!-- keywords: gammalim -->
<!-- signatures: gammalim -->
### Variable: gammalim

デフォルト値: 1000000



`gammalim`は、整数と有理数引数に関してガンマ関数の整理を制御します。
もし引数の絶対値が`gammalim`よりも大きくないなら、
整理が行われます。
`factlim`スイッチは、
整数引数の`gamma`の結果の整理を制御します。
`factlim`スイッチは、
整数引数の`gamma`の結果の整理も制御することに注意してください。

<!-- category: SpecialFunctions -->
<!-- keywords: hankel_1 -->
<!-- signatures: hankel_1(v, z) -->
### Function: hankel_1 (v, z)

次数$v$、独立変数$z$の第一種ハンケル関数 (A&S 9.1.3)。
`hankel_1`は以下のように定義されます。



```maxima
bessel_j(v,z) + %i * bessel_y(v,z)
```


Maximaは、
浮動小数点精度の実数次数$v$と複素独立変数$z$に対して
`hankel_1`を数値的に評価します。
多倍長浮動小数点精度の数値評価と複素次数$v$はサポートされていません。


`besselexpand`が`true`の時、
次数$v$が奇数の1/2の時`hankel_1`は初等関数の項に展開されます。
`besselexpand`を参照してください。


Maximaは`hankel_1`の独立変数$z$に関する導関数を知っています。


例:


数値評価:







```maxima
(%i1) hankel_1(1,0.5);
(%o1)              .2422684576748738 - 1.471472392670243 %i
(%i2) hankel_1(1,0.5+%i);
(%o2)             - .2558287994862166 %i - 0.239575601883016
```


複素次数$v$はサポートされていません。
Maximaは名詞形を返します:






```maxima
(%i3) hankel_1(%i,0.5+%i);
(%o3)                       hankel_1(%i, %i + 0.5)
```


`besselexpand`が`true`の時の`hankel_1`の展開:






```maxima
(%i4) hankel_1(1/2,z),besselexpand:true;
                      sqrt(2) sin(z) - sqrt(2) %i cos(z)
(%o4)                 ----------------------------------
                              sqrt(%pi) sqrt(z)
```


`hankel_1`の独立変数$z$に関する導関数。
次数$v$に関する導関数はサポートされていません。
Maximaは名詞形を返します:







```maxima
(%i5) diff(hankel_1(v,z),z);
                    hankel_1(v - 1, z) - hankel_1(v + 1, z)
(%o5)               ---------------------------------------
                                       2
(%i6) diff(hankel_1(v,z),v);
                             d
(%o6)                        -- (hankel_1(v, z))
                             dv
```

<!-- category: SpecialFunctions -->
<!-- keywords: hankel_2 -->
<!-- signatures: hankel_2(v, z) -->
### Function: hankel_2 (v, z)

次数$v$、独立変数$z$の第二種ハンケル関数 (A&S 9.1.4)。
`hankel_2`は以下のように定義されます。



```maxima
bessel_j(v,z) - %i * bessel_y(v,z)
```


Maximaは、
浮動小数点精度の実数次数$v$と複素独立変数$z$に対して
`hankel_2`を数値的に評価します。
多倍長浮動小数点精度の数値評価と複素次数$v$はサポートされていません。


`besselexpand`が`true`の時、
次数$v$が奇数の1/2の時`hankel_2`は初等関数の項に展開されます。
`besselexpand`を参照してください。


Maximaは`hankel_2`の独立変数$z$に関する導関数を知っています。


例は`hankel_1`を参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: hgfred -->
<!-- signatures: hgfred(a, b, t) -->
### Function: hgfred (a, b, t)

一般化超幾何関数を他のより簡単な形式に整理します。
*a*は分子パラメータのリストで、*b*は分母パラメータのリストです。


もし`hgfred`が超幾何関数を整理できなければ、
形式`%f[p,q]([a], [b], x)`の式を返します。
ここで*p*は*a*の中の要素の数で、
*q*は*b*の中の要素の数です。
これは、通常の`pFq`一般化超幾何関数です。



```maxima
(%i1) assume(not(equal(z,0)));
(%o1)                          [notequal(z, 0)]
(%i2) hgfred([v+1/2],[2*v+1],2*%i*z);

                     v/2                               %i z
                    4    bessel_j(v, z) gamma(v + 1) %e
(%o2)               ---------------------------------------
                                       v
                                      z
(%i3) hgfred([1,1],[2],z);

                                   log(1 - z)
(%o3)                            - ----------
                                       z
(%i4) hgfred([a,a+1/2],[3/2],z^2);

                               1 - 2 a          1 - 2 a
                        (z + 1)        - (1 - z)
(%o4)                   -------------------------------
                                 2 (1 - 2 a) z
```


以下の例が示すように、orthopolyもロードすることは有益なことがあります。
*L*は、一般化ラーゲル多項式であることに注意してください。



```maxima
(%i5) load("orthopoly")$
(%i6) hgfred([-2],[a],z);


                                    (a - 1)
                                 2 L       (z)
                                    2
(%o6)                            -------------
                                   a (a + 1)

(%i7) ev(%);

                                  2
                                 z        2 z
(%o7)                         --------- - --- + 1
                              a (a + 1)    a
```

<!-- category: SpecialFunctions -->
<!-- keywords: hypergeometric -->
<!-- signatures: hypergeometric([a1, ..., ap], [b1, ..., bq], x) -->
### Function: hypergeometric ([a1, ..., ap], [b1, ..., bq], x)

超幾何関数。
Maximaの`%f`超幾何関数と違って，
関数`hypergeometric`は整理関数です;
`hypergeometric`は複素倍精度と多倍長浮動小数点評価もサポートします。
ガウスの超幾何関数、すなわち、$p = 2$かつ$q = 1$、
に関しては、
単位円の外側の浮動小数点評価はサポートされていますが、
一般にはサポートされていません。


オプション変数`expand_hypergeometric`がtrue(デフォルトはfalse)で、
独立変数`a1`から`ap`の１つが負の整数の時(多項式の場合)、
`hypergeometric`は展開された多項式を返します。


例:



```maxima
(%i1)  hypergeometric([],[],x);
(%o1) %e^x
```


`expand_hypergeometric`がtrueの時、多項式の場合は自動的に展開されます:



```maxima
(%i2) hypergeometric([-3],[7],x);
(%o2) hypergeometric([-3],[7],x)

(%i3) hypergeometric([-3],[7],x), expand_hypergeometric : true;
(%o3) -x^3/504+3*x^2/56-3*x/7+1
```


倍精度と多倍長浮動小数点評価の両方がサポートされています:



```maxima
(%i4) hypergeometric([5.1],[7.1 + %i],0.42);
(%o4)       1.346250786375334 - 0.0559061414208204 %i
(%i5) hypergeometric([5,6],[8], 5.7 - %i);
(%o5)     .00737582400977495 - 0.001049813688578674 %i
(%i6) hypergeometric([5,6],[8], 5.7b0 - %i), fpprec : 30;
(%o6) 7.37582400977494674506442010824b-3
                          - 1.04981368857867315858055393376b-3 %i
```

<!-- category: SpecialFunctions -->
<!-- keywords: hypergeometric_representation -->
<!-- signatures: hypergeometric_representation -->
### Variable: hypergeometric_representation

デフォルト値: false


fresnel_sとfresnel_cに関して超幾何表現への変換を可能にします。

<!-- category: SpecialFunctions -->
<!-- keywords: lambert_w -->
<!-- signatures: lambert_w(z) -->
### Function: lambert_w (z)

ランバートW関数W(z)の主枝、
`z = W(z) * exp(W(z))`の解。

<!-- category: SpecialFunctions -->
<!-- keywords: log_gamma -->
<!-- signatures: log_gamma(z) -->
### Function: log_gamma (z)

ガンマ関数の自然対数。

<!-- category: SpecialFunctions -->
<!-- keywords: makefact -->
<!-- signatures: makefact(expr) -->
### Function: makefact (expr)

*expr*の中の二項、ガンマ、ベータ関数のインスタンスを階乗に変換します。


`makegamma`も参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: makegamma -->
<!-- signatures: makegamma(expr) -->
### Function: makegamma (expr)

*expr*の中の２項、階乗、ベータ関数のインスタンスをガンマ関数に変換します。


`makefact`も参照してください。

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsifracdenom -->
<!-- signatures: maxpsifracdenom -->
### Variable: maxpsifracdenom

デフォルト値: 6


*x*を１より小さい、形式`p/q`の有理数とします。
もし`q`が`maxpsifracdenom`より大きいなら
`psi[n](x)`は、
整理された値を返そうとしません。

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsifracnum -->
<!-- signatures: maxpsifracnum -->
### Variable: maxpsifracnum

デフォルト値: 6


*x*を１より小さい、形式`p/q`の有理数とします。
もし`p`が`maxpsifracnum`より大きいなら
`psi[n](x)`は、
整理された値を返そうとしません。

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsinegint -->
<!-- signatures: maxpsinegint -->
### Variable: maxpsinegint

デフォルト値: -10


`maxpsinegint`
`psi[n](x)`が厳密な値を計算しようとする
最も大きな負の値です。
従って、もし
*x*が`maxnegint`よりも小さければ、
たとえ可能でも、
`psi[n](x)`は整理された答えを返しません。

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsiposint -->
<!-- signatures: maxpsiposint -->
### Variable: maxpsiposint

デフォルト値: 20


`maxpsiposint`は、
`psi[n](x)`が厳密な値を計算しようとする
最も大きな正の値です。

<!-- category: SpecialFunctions -->
<!-- keywords: numfactor -->
<!-- signatures: numfactor(expr) -->
### Function: numfactor (expr)

式*expr*を掛ける数値因子を返します。
式*expr*は単一項でなければいけません。



`content`は、輪の中のすべての項の最大公約数を返します。



```maxima
(%i1) gamma (7/2);
                          15 sqrt(%pi)
(%o1)                     ------------
                               8
(%i2) numfactor (%);
                               15
(%o2)                          --
                               8
```

<!-- category: SpecialFunctions -->
<!-- keywords: nzeta -->
<!-- signatures: nzeta(z) -->
### Function: nzeta (z)

プラズマ分散関数
`nzeta(z) = %i*sqrt(%pi)*exp(-z^2)*(1-erf(-%i*z))`

<!-- category: SpecialFunctions -->
<!-- keywords: nzetai -->
<!-- signatures: nzetai(z) -->
### Function: nzetai (z)

`imagpart(nzeta(z))`を返します。

<!-- category: SpecialFunctions -->
<!-- keywords: nzetar -->
<!-- signatures: nzetar(z) -->
### Function: nzetar (z)

`realpart(nzeta(z))`を返します。

<!-- category: SpecialFunctions -->
<!-- keywords: parabolic_cylinder_d -->
<!-- signatures: parabolic_cylinder_d(v, z) -->
### Function: parabolic_cylinder_d (v, z)

放物円筒関数`parabolic_cylinder_d(v,z)`. (A&s 19.3.1)

<!-- category: SpecialFunctions -->
<!-- keywords: psi -->
<!-- signatures: psi[n](x) -->
### Function: psi ([n](x))

`log (gamma (x))`の次数`n+1`の導関数。
例えば、
`psi[0](x)`は１階微分、
`psi[1](x)`は２階微分など。


Maximaは、一般に、`psi`の数値を計算する方法を知りませんが、
有理数の引数に関してはいくつかの厳密な値を計算することができます。
いくつの変数は、`psi`が可能なら厳密な値を返す有理数の引数の範囲を制御します。
`maxpsiposint`,
`maxpsinegint`, `maxpsifracnum`, `maxpsifracdenom`を参照してください。
すなわち、*x*は、`maxpsinegint`と`maxpsiposint`の間になければいけません。
もし*x*の小数部分の絶対値が有理数で、かつ分子が`maxpsifracnum`より小さく、
分母が`maxpsifracdenom`より小さければ、
`psi`は厳密な値を返します。


`bffac`パッケージの中の
関数`bfpsi`は数値を計算できます。

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i -->
<!-- signatures: scaled_bessel_i(v, z) -->
### Function: scaled_bessel_i (v, z)

次数$v$、独立変数$z$のスケールされた第一種変形ベッセル関数。
すなわち、$scaled_bessel_i(v,z) = exp(-abs(z))*bessel_i(v, z)$。
この関数は、大きな$z$に関する$bessel_i$―これはおおきくなりますーの計算に
特に役に立ちます。
しかしながら、そうでなければ、Maximaはこの関数についてあまり知りません。
数式処理のためには、式`exp(-abs(z))*bessel_i(v, z)`を使って取り組むのが多分望ましいです。

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i0 -->
<!-- signatures: scaled_bessel_i0(z) -->
### Function: scaled_bessel_i0 (z)

`scaled_bessel_i(0,z)`と同一です。

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i1 -->
<!-- signatures: scaled_bessel_i1(z) -->
### Function: scaled_bessel_i1 (z)

`scaled_bessel_i(1,z)`と同一です。

<!-- category: SpecialFunctions -->
<!-- keywords: specint -->
<!-- signatures: specint(exp(-s*t)*expr, t) -->
### Function: specint (exp(-s*t)*expr, t)

*expr*の変数*t*に関するラプラス変換を計算します。
以下の特殊関数は`specint`で扱われます:
不完全ベータ関数、誤差関数
（誤差関数`erfi`ではないです。`erfi`は例えば、`erf`に変換することは簡単です。）、
指数積分、（ベッセル関数の積を含む）ベッセル関数、ハンケル関数、エルミートおよびラーゲル多項式。


更に、`specint`は、超幾何関数`%f[p,q]([],[],z)`、
第一種Whittaker関数`%m[u,k](z)`第二種Whittaker関数`%w[u,k](z)`を
扱うことができます。


結果は、特殊関数の項になるかもしれませんし、未整理の超幾何関数を含むかもしれません。


`laplace`がラプラス変換を見つけることに失敗した時、
`specint`がコールされます。
`laplace`はラプラス変換に関するもっと一般的な規則を知っているので、
`specint`ではなく`laplace`を使うのが望ましいです。


`demo(hypgeo)`は、`specint`によって計算されたラプラス変換のいくつかの例を表示します。



例:









```maxima
(%i1) assume (p > 0, a > 0)$
(%i2) specint (t^(1/2) * exp(-a*t/4) * exp(-p*t), t);
                           sqrt(%pi)
(%o2)                     ------------
                                 a 3/2
                          2 (p + -)
                                 4
(%i3) specint (t^(1/2) * bessel_j(1, 2 * a^(1/2) * t^(1/2))
              * exp(-p*t), t);
                                   - a/p
                         sqrt(a) %e
(%o3)                    ---------------
                                2
                               p
```


指数積分の例:



```maxima
(%i4) assume(s>0,a>0,s-a>0)$
(%i5) ratsimp(specint(%e^(a*t)
                      *(log(a)+expintegral_e1(a*t))*%e^(-s*t),t));
                             log(s)
(%o5)                        ------
                             s - a
(%i6) logarc:true$

(%i7) gamma_expand:true$

(%i8) radcan(specint((cos(t)*expintegral_si(t)
                     -sin(t)*expintegral_ci(t))*%e^(-s*t),t));
                             log(s)
(%o8)                        ------
                              2
                             s  + 1
(%i9) ratsimp(specint((2*t*log(a)+2/a*sin(a*t)
                      -2*t*expintegral_ci(a*t))*%e^(-s*t),t));
                               2    2
                          log(s  + a )
(%o9)                     ------------
                                2
                               s
```


`gamma_incomplete`の展開を使った時と、
`expintegral_e1`への表現の変形を使った時のの結果:



```maxima
(%i10) assume(s>0)$
(%i11) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                                            1
                            gamma_incomplete(-, k s)
                                            2
(%o11)                      ------------------------
                               sqrt(%pi) sqrt(s)

(%i12) gamma_expand:true$
(%i13) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                              erfc(sqrt(k) sqrt(s))
(%o13)                        ---------------------
                                     sqrt(s)

(%i14) expintrep:expintegral_e1$
(%i15) ratsimp(specint(1/(t+a)^2*%e^(-s*t),t));
                              a s
                        a s %e    expintegral_e1(a s) - 1
(%o15)                - ---------------------------------
                                        a
```

<!-- category: SpecialFunctions -->
<!-- keywords: struve_h -->
<!-- signatures: struve_h(v, z) -->
### Function: struve_h (v, z)

次数v, 独立変数zのシュトルーベ関数H (A&S 12.1.1)

<!-- category: SpecialFunctions -->
<!-- keywords: struve_l -->
<!-- signatures: struve_l(v, z) -->
### Function: struve_l (v, z)

次数v、独立変数zの変形シュトルーベ関数L (A&S 12.2.1)

