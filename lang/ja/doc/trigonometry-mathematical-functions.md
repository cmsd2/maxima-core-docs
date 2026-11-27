## Mathematical Functions

<!-- category: Trigonometry -->
<!-- keywords: %iargs -->
<!-- signatures: %iargs -->
### Variable: %iargs

デフォルト値: `true`


`%iargs`が`true`の時、
引数が明らかに、虚数単位
$%i$
を掛けたものの時、
三角関数は双曲線関数に整理されます。


引数が明らかに実数の時でさえ、整理は実行されます;
Maximaは、ただ、引数が、
$%i$
を文字通り掛けたものかどうかを考慮します。


例:









```maxima
(%i1) %iargs : false$
(%i2) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o2)           [sin(%i x), cos(%i x), tan(%i x)]
(%i3) %iargs : true$
(%i4) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o4)           [%i sinh(x), cosh(x), %i tanh(x)]
```


引数が明らかに実数の時でさえ、整理は実行されます。








```maxima
(%i1) declare (x, imaginary)$

(%i2) [featurep (x, imaginary), featurep (x, real)];
(%o2)                     [true, false]


(%i3) sin (%i * x);
(%o3)                      %i sinh(x)
```

<!-- category: Trigonometry -->
<!-- keywords: %piargs -->
<!-- signatures: %piargs -->
### Variable: %piargs

デフォルト値: `true`


`%piargs`が`true`の時で、
引数が
$%pi$, $%pi/2$, $%pi/3$, $%pi/4$, $%pi/6$のいずれか
の整数倍の時は、
三角関数は、代数定数に整理されます。



Maximaは、
$%pi$
などが、整数変数（すなわち、整数に宣言されたシンボル）倍された時適用できる
いくつかの恒等式を知っています。


例:













```maxima
(%i1) %piargs : false$

(%i2) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                %pi       %pi
(%o2)            [sin(%pi), sin(---), sin(---)]
                                 2         3


(%i3) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                      %pi       %pi       %pi
(%o3)            [sin(---), sin(---), sin(---)]
                       4         5         6

(%i4) %piargs : true$

(%i5) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                sqrt(3)
(%o5)                    [0, 1, -------]
                                   2


(%i6) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                         1         %pi   1
(%o6)                [-------, sin(---), -]
                      sqrt(2)       5    2


(%i7) [cos (%pi/3), cos (10*%pi/3), tan (10*%pi/3),
       cos (sqrt(2)*%pi/3)];
                1    1               sqrt(2) %pi
(%o7)          [-, - -, sqrt(3), cos(-----------)]
                2    2                    3
```


$%pi$ and $%pi/2$
が整数変数にかけられた時、いくつかの恒等式が適用されます。








```maxima
(%i1) declare (n, integer, m, even)$
(%i2) [sin (%pi * n), cos (%pi * m), sin (%pi/2 * m),
       cos (%pi/2 * m)];
                                      m/2
(%o2)                  [0, 1, 0, (- 1)   ]
```

<!-- category: Trigonometry -->
<!-- keywords: acos -->
<!-- signatures: acos(x) -->
### Function: acos (x)

– 逆余弦

<!-- category: Trigonometry -->
<!-- keywords: acosh -->
<!-- signatures: acosh(x) -->
### Function: acosh (x)

– 逆双曲余弦

<!-- category: Trigonometry -->
<!-- keywords: acot -->
<!-- signatures: acot(x) -->
### Function: acot (x)

– 逆余接

<!-- category: Trigonometry -->
<!-- keywords: acoth -->
<!-- signatures: acoth(x) -->
### Function: acoth (x)

– 逆双曲余接

<!-- category: Trigonometry -->
<!-- keywords: acsc -->
<!-- signatures: acsc(x) -->
### Function: acsc (x)

– 逆余割

<!-- category: Trigonometry -->
<!-- keywords: acsch -->
<!-- signatures: acsch(x) -->
### Function: acsch (x)

– 逆双曲余割

<!-- category: Trigonometry -->
<!-- keywords: asec -->
<!-- signatures: asec(x) -->
### Function: asec (x)

– 逆正割

<!-- category: Trigonometry -->
<!-- keywords: asech -->
<!-- signatures: asech(x) -->
### Function: asech (x)

– 逆双曲正割

<!-- category: Trigonometry -->
<!-- keywords: asin -->
<!-- signatures: asin(x) -->
### Function: asin (x)

– 逆正弦

<!-- category: Trigonometry -->
<!-- keywords: asinh -->
<!-- signatures: asinh(x) -->
### Function: asinh (x)

– 逆双曲正弦

<!-- category: Trigonometry -->
<!-- keywords: atan -->
<!-- signatures: atan(x) -->
### Function: atan (x)

– 逆正接

<!-- category: Trigonometry -->
<!-- keywords: atan2 -->
<!-- signatures: atan2(y, x) -->
### Function: atan2 (y, x)

– `-%pi`から`%pi`までの間の`atan(y/x)`の値をもたらします。

<!-- category: Trigonometry -->
<!-- keywords: atanh -->
<!-- signatures: atanh(x) -->
### Function: atanh (x)

– 逆双曲正接

<!-- category: Trigonometry -->
<!-- keywords: atrig1 -->
<!-- signatures: atrig1 -->
### Variable: atrig1

`atrig1`パッケージは、逆三角関数のためのいくつかの追加の整理規則を含みます。
Maximaが既に知っている規則と合わせて、
以下の角度が完全に実装されます:
`0`, `%pi/6`, `%pi/4`, `%pi/3`, `%pi/2`。
他の3象限の対応する角度も利用可能です。
これらを使うには、`load("atrig1");`を実行してください。

<!-- category: Trigonometry -->
<!-- keywords: cos -->
<!-- signatures: cos(x) -->
### Function: cos (x)

– 余弦

<!-- category: Trigonometry -->
<!-- keywords: cosh -->
<!-- signatures: cosh(x) -->
### Function: cosh (x)

– 双曲余弦

<!-- category: Trigonometry -->
<!-- keywords: cot -->
<!-- signatures: cot(x) -->
### Function: cot (x)

– 余接

<!-- category: Trigonometry -->
<!-- keywords: coth -->
<!-- signatures: coth(x) -->
### Function: coth (x)

– 双曲余接

<!-- category: Trigonometry -->
<!-- keywords: csc -->
<!-- signatures: csc(x) -->
### Function: csc (x)

– 余割

<!-- category: Trigonometry -->
<!-- keywords: csch -->
<!-- signatures: csch(x) -->
### Function: csch (x)

– 双曲余割

<!-- category: Trigonometry -->
<!-- keywords: halfangles -->
<!-- signatures: halfangles -->
### Variable: halfangles

デフォルト値: `false`


`halfangles`が`true`の時、
引数`expr/2`の三角関数は、*expr*の関数に整理されます。


区間`0 < x < 2*%pi`の実引数*x*に関して、
半角の正弦は簡単な公式に整理されます:



```maxima
sqrt(1 - cos(x))
                         ----------------
                             sqrt(2)
```


複雑な因子は
すべての複素引数*z*でこの公式を正しくするために必要です:



           realpart(z)
     floor(-----------)
              2 %pi
(- 1)                   (1 - unit_step(- imagpart(z))

                            realpart(z)            realpart(z)
                      floor(-----------) - ceiling(-----------)
                               2 %pi                  2 %pi
                ((- 1)                                          + 1))


Maximaは、この因子と、
関数`sin`, `cos`, `sinh`, `cosh`に関する類似の因子を知っています。
引数$z$の特別な値に関して、
これらの因子は相応に整理されます。


例:











```maxima
(%i1) halfangles:false;
(%o1)                                false
(%i2) sin(x/2);
                                        x
(%o2)                               sin(-)
                                        2
(%i3) halfangles:true;
(%o3)                                true
(%i4) sin(x/2);
                                                    x
                                            floor(-----)
                                                  2 %pi
                      sqrt(1 - cos(x)) (- 1)
(%o4)                 ----------------------------------
                                   sqrt(2)
(%i5) assume(x>0, x<2*%pi)$
(%i6) sin(x/2);
                               sqrt(1 - cos(x))
(%o6)                          ----------------
                                   sqrt(2)
```

<!-- category: Trigonometry -->
<!-- keywords: ntrig -->
<!-- signatures: ntrig -->
### Variable: ntrig

`ntrig`パッケージは、
引数が形式`f(n %pi/10)`
―*f*は関数
`sin`, `cos`, `tan`, `csc`, `sec`, `cot`のいずれか―
の三角関数を整理するのに使われる整理規則の集合を含みます。

<!-- category: Trigonometry -->
<!-- keywords: sec -->
<!-- signatures: sec(x) -->
### Function: sec (x)

– 正割

<!-- category: Trigonometry -->
<!-- keywords: sech -->
<!-- signatures: sech(x) -->
### Function: sech (x)

– 双曲正割

<!-- category: Trigonometry -->
<!-- keywords: sin -->
<!-- signatures: sin(x) -->
### Function: sin (x)

– 正弦

<!-- category: Trigonometry -->
<!-- keywords: sinh -->
<!-- signatures: sinh(x) -->
### Function: sinh (x)

– 双曲正弦

<!-- category: Trigonometry -->
<!-- keywords: tan -->
<!-- signatures: tan(x) -->
### Function: tan (x)

– 正接

<!-- category: Trigonometry -->
<!-- keywords: tanh -->
<!-- signatures: tanh(x) -->
### Function: tanh (x)

– 双曲正接

<!-- category: Trigonometry -->
<!-- keywords: trigexpand -->
<!-- signatures: trigexpand(expr) -->
### Function: trigexpand (expr)

*expr*の中に現れる角の和や角の倍数の三角関数、双曲線関数を展開します。
最もよい結果では、*expr*は展開されるべきです。
整理のユーザー制御を強化するために、
この関数は、一度に１レベルのみ、角の和もしくは角の倍数を展開します。
ただちにサインとコサインへの完全な展開を得るには、
スイッチ`trigexpand: true`を設定してください。


`trigexpand`は、以下のグローバルフラグによって決定されます:



**trigexpand** — もし`true`なら、
続いて現れるサインやコサインを含んでいる式すべての展開を起こします。
**halfangles** — もし`true`なら、
半角が整理されます。
**trigexpandplus** — `trigexpand`の「和」規則を制御します。
和（例えば`sin(x + y)`）の展開は、
`trigexpandplus`が`true`の時だけ起こります。
**trigexpandtimes** — `trigexpand`の「積」規則を制御します。
積(例えば`sin(2 x)`)の展開は、
`trigexpandtimes`が`true`の時だけ起こります。


例:







```maxima
(%i1) x+sin(3*x)/sin(x),trigexpand=true,expand;

                         2           2
(%o1)               - sin (x) + 3 cos (x) + x

(%i2) trigexpand(sin(10*x+y));
(%o2)          cos(10 x) sin(y) + sin(10 x) cos(y)
```

<!-- category: Trigonometry -->
<!-- keywords: trigexpandplus -->
<!-- signatures: trigexpandplus -->
### Variable: trigexpandplus

デフォルト値: `true`


`trigexpandplus`は、`trigexpand`の「和」規則を制御します。
`trigexpand`コマンドが使われるか、もしくは
`trigexpand`スイッチが`true`に設定されている時
和(例えば`sin(x+y))`)の展開は、
`trigexpandplus`が`true`の時だけ起こります。

<!-- category: Trigonometry -->
<!-- keywords: trigexpandtimes -->
<!-- signatures: trigexpandtimes -->
### Variable: trigexpandtimes

デフォルト値: `true`


`trigexpandtimes`は、`trigexpand`の「積」規則を制御します。
`trigexpand`コマンドが使われるか、もしくは、
`trigexpand`スイッチが`true`に設定されている時、
積(例えば`sin(2*x)`)の展開は、
`trigexpandtimes`が`true`の時だけ起こります。

<!-- category: Trigonometry -->
<!-- keywords: triginverses -->
<!-- signatures: triginverses -->
### Variable: triginverses

デフォルト値: `true`


`triginverses`は、
三角関数や双曲線関数とそれらの逆関数の合成の整理を制御します。


もし`all`なら、
例えば、`atan(tan(x))`
と`tan(atan(x))`のどちらも*x*に整理されます。


もし`true`なら、
`arcfun(fun(x))`の整理は止められます。


もし`false`なら、
`arcfun(fun(x))`と
`fun(arcfun(x))`のどちらの整理も止められます。

<!-- category: Trigonometry -->
<!-- keywords: trigrat -->
<!-- signatures: trigrat(expr) -->
### Function: trigrat (expr)

三角関数の整理された標準疑似線形形式を与えます;
*expr*は、`sin`, `cos`もしくは`tan`のいくつかの有理分数であり、
それらの引数は、整数係数を持つ、いくつかの変数（もしくは核）と`%pi/n` (*n*は整数)の線形形式です。
結果は、分子と分母が`sin`と`cos`に関して線形の整理された分数です。
`trigrat`はいつも可能なときは線形化します。






```maxima
(%i1) trigrat(sin(3*a)/sin(a+%pi/3));
(%o1)            sqrt(3) sin(2 a) + cos(2 a) - 1
```


以下の例は、
Davenport, Siret, and Tournierの*Calcul Formel*, Masson (もしくは英語版ではAddison-Wesley), 1.5.5節, モーレイの定理から取られました。










```maxima
(%i1) c : %pi/3 - a - b$
(%i2) bc : sin(a)*sin(3*c)/sin(a+b);

                                          %pi
                  sin(a) sin(3 (- b - a + ---))
                                           3
(%o2)             -----------------------------
                           sin(b + a)

(%i3) ba : bc, c=a, a=c;

                                         %pi
                    sin(3 a) sin(b + a - ---)
                                          3
(%o3)               -------------------------
                                  %pi
                          sin(a - ---)
                                   3

(%i4) ac2 : ba^2 + bc^2 - 2*bc*ba*cos(b);

         2         2         %pi
      sin (3 a) sin (b + a - ---)
                              3
(%o4) ---------------------------
                2     %pi
             sin (a - ---)
                       3
                                       %pi
 - (2 sin(a) sin(3 a) sin(3 (- b - a + ---)) cos(b)
                                        3
             %pi            %pi
 sin(b + a - ---))/(sin(a - ---) sin(b + a))
              3              3
      2       2              %pi
   sin (a) sin (3 (- b - a + ---))
                              3
 + -------------------------------
                2
             sin (b + a)

(%i5) trigrat (ac2);

(%o5) - (sqrt(3) sin(4 b + 4 a) - cos(4 b + 4 a)
 - 2 sqrt(3) sin(4 b + 2 a) + 2 cos(4 b + 2 a)
 - 2 sqrt(3) sin(2 b + 4 a) + 2 cos(2 b + 4 a)
 + 4 sqrt(3) sin(2 b + 2 a) - 8 cos(2 b + 2 a) - 4 cos(2 b - 2 a)
 + sqrt(3) sin(4 b) - cos(4 b) - 2 sqrt(3) sin(2 b) + 10 cos(2 b)
 + sqrt(3) sin(4 a) - cos(4 a) - 2 sqrt(3) sin(2 a) + 10 cos(2 a)
 - 9)/4
```

<!-- category: Trigonometry -->
<!-- keywords: trigreduce -->
<!-- signatures: trigreduce(expr, x), trigreduce(expr) -->
### Function: trigreduce (expr, x)

*x*を引数とする三角と双曲の正弦、余弦の積とべきを
*x*の倍数のそれらに結合します。
これらの関数が分母に現れた時、これらを消去しようともします。
もし*x*が省略されたら、*expr*の中の変数すべてが使われます。


`poissimp`も参照してください。






```maxima
(%i1) trigreduce(-sin(x)^2+3*cos(x)^2+x);

               cos(2 x)      cos(2 x)   1        1
(%o1)          -------- + 3 (-------- + -) + x - -
                  2             2       2        2
```

<!-- category: Trigonometry -->
<!-- keywords: trigsign -->
<!-- signatures: trigsign -->
### Variable: trigsign

デフォルト値: `true`


`trigsign`が`true`の時、
三角関数への負の引数の整理を認めます。
例えば、`sin(-x)`は、
`trigsign`が`true`の時だけ、
`-sin(x)`になります。

<!-- category: Trigonometry -->
<!-- keywords: trigsimp -->
<!-- signatures: trigsimp(expr) -->
### Function: trigsimp (expr)

`tan`, `sec`などを含む式を`sin`, `cos`, `sinh`, `cosh`に整理するために、
恒等式
$sin(x)^2 + cos(x)^2 = 1$
と
$cosh(x)^2 - sinh(x)^2 = 1$
を使います。


`trigreduce`, `ratsimp`, `radcan`
は、結果を更に整理できるかもしれません。


`demo ("trgsmp.dem")`は、`trigsimp`のいくつかの例を表示します。

