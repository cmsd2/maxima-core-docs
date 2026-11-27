## Data Types and Structures

<!-- category: NumberTheory -->
<!-- keywords: bfloat -->
<!-- signatures: bfloat(expr) -->
### Function: bfloat (expr)

*expr*の中のすべての数や数の関数を多倍長浮動小数点に変換します。
戻り値の多倍長浮動小数点の有効桁数は、
グローバル変数`fpprec`によって規定されます。


`float2bf`が`false`の場合、
浮動小数点が多倍長浮動小数点に変換される時
（精度が落ちることを意味するので）警告メッセージが出力されます。

See also: `fpprec`, `float2bf`.

<!-- category: NumberTheory -->
<!-- keywords: bfloatp -->
<!-- signatures: bfloatp(expr) -->
### Function: bfloatp (expr)

もし*expr*が多倍長浮動小数点数なら`true`を、そうでなければ`false`を返します。

<!-- category: NumberTheory -->
<!-- keywords: bftorat -->
<!-- signatures: bftorat -->
### Variable: bftorat

デフォルト値: `false`


`bftorat`は多倍長浮動小数点の有理数への変換を制御します。
`bftorat`が`false`の時、
`ratepsilon`が変換を制御するのに使われます。
(これは比較的小さな有理数になります。)
`bftorat`が`true`の時、
生成された有理数は多倍長浮動小数点を正確に表します。

See also: `ratepsilon`.

<!-- category: NumberTheory -->
<!-- keywords: bftrunc -->
<!-- signatures: bftrunc -->
### Variable: bftrunc

デフォルト値: `true`


`bftrunc`は、非ゼロの多倍長浮動小数点数の中のずるずる続くゼロを表示しないようにします。
例えば、もし`bftrunc`が`false`なら、
`bfloat (1)`は`1.000000000000000B0`と表示されます。
そうでなければ、これは、`1.0B0`と表示されます。

<!-- category: NumberTheory -->
<!-- keywords: evenp -->
<!-- signatures: evenp(expr) -->
### Function: evenp (expr)

もし*expr*が偶数なら`true`を返します。

他の場合には`false`を返します。

<!-- category: NumberTheory -->
<!-- keywords: float -->
<!-- signatures: float(expr) -->
### Function: float (expr)

*expr*の中の整数、有理数、多倍長浮動小数点を浮動小数点に変換します。
`float`は`evflag`でもあり、
非整数有理数と多倍長浮動小数点を浮動小数点に変換します。

<!-- category: NumberTheory -->
<!-- keywords: float2bf -->
<!-- signatures: float2bf -->
### Variable: float2bf

デフォルト値: `true`

 

`float2bf`が`false`の場合、
浮動小数点が多倍長浮動小数点に変換される時、
（これは精度の無駄使いとなるかもしれないので、）
警告メッセージが表示されます。
デフォルト値は`true`です。

<!-- category: NumberTheory -->
<!-- keywords: floatnump -->
<!-- signatures: floatnump(expr) -->
### Function: floatnump (expr)

もし*expr*が浮動小数点なら
`true`を返し、そうでないなら
`false`を返します。

<!-- category: NumberTheory -->
<!-- keywords: fpprec -->
<!-- signatures: fpprec -->
### Variable: fpprec

デフォルト値: 16


`fpprec`は多倍長浮動小数点上の代数のための有効桁数です。
`fpprec`は通常の浮動小数点上の計算に影響を与えません。


`bfloat`と`fpprintprec`も参照してください。

See also: `bfloat`, `fpprintprec`.

<!-- category: NumberTheory -->
<!-- keywords: fpprintprec -->
<!-- signatures: fpprintprec -->
### Variable: fpprintprec

デフォルト値: 0


`fpprintprec`は、通常の浮動小数点もしくは多倍長浮動小数点を表示する時の
表示する桁数です。


通常の浮動小数点に関しては、
`fpprintprec`が2から16までの値を持つ時、
表示されるディジット数は`fpprintprec`に等しいです。
そうでなければ、`fpprintprec`は0もしくは16より大きく、
表示されるディジット数は16です。


多倍長浮動小数点に関しては、
`fpprintprec`が2から`fpprec`までの値を持つ時、
表示される桁数は、`fpprintprec`に等しいです。
そうでなければ、`fpprintprec`は、0もしくは`fpprec`より大きく、
表示される桁数は`fpprec`に等しいです。


`fpprintprec`は1にはできません。

<!-- category: NumberTheory -->
<!-- keywords: integerp -->
<!-- signatures: integerp(expr) -->
### Function: integerp (expr)

もし*expr*が整数リテラルなら `true`を、
そうでないなら `false`を返します。


もし引数がシンボルならたとえ引数が宣言された整数でも、
`integerp`は `false`を返します。


例:



```maxima
(%i1) integerp (0);
(%o1)                         true
(%i2) integerp (1);
(%o2)                         true
(%i3) integerp (-17);
(%o3)                         true
(%i4) integerp (0.0);
(%o4)                         false
(%i5) integerp (1.0);
(%o5)                         false
(%i6) integerp (%pi);
(%o6)                         false
(%i7) integerp (n);
(%o7)                         false
(%i8) declare (n, integer);
(%o8)                         done
(%i9) integerp (n);
(%o9)                         false
```

<!-- category: NumberTheory -->
<!-- keywords: m1pbranch -->
<!-- signatures: m1pbranch -->
### Variable: m1pbranch

デフォルト値: `false`


`m1pbranch`は `-1`のべき乗の主枝です。
`(-1)^(1/3)`(すなわち、「奇」の有理指数)や
`(-1)^(1/4)`(すなわち、「偶」の有理指数)
のような量は以下のように扱われます:



```maxima
domain:real
                            
(-1)^(1/3):      -1         
(-1)^(1/4):   (-1)^(1/4)   

             domain:complex              
m1pbranch:false          m1pbranch:true
(-1)^(1/3)               1/2+%i*sqrt(3)/2
(-1)^(1/4)              sqrt(2)/2+%i*sqrt(2)/2
```

<!-- category: NumberTheory -->
<!-- keywords: nonnegintegerp -->
<!-- signatures: nonnegintegerp(n) -->
### Function: nonnegintegerp (n)

`n >= 0`かつ *n*が整数の時だけ`true`を返します。

<!-- category: NumberTheory -->
<!-- keywords: numberp -->
<!-- signatures: numberp(expr) -->
### Function: numberp (expr)

もし*expr*が文字リテラルか、有理数か、浮動小数点数か、多倍長浮動小数点なら
`true`を、
そうでなければ `false`を返します。


もし引数がシンボルなら、
たとえ引数が`%pi`や`%i`のようなシンボリックな数でも、また、
`even`, `odd`, `integer`, `rational`, `irrational`, 
`real`, `imaginary`, `complex`のいずれかに宣言されていても、
`numberp`は `false`を返します。


例:



```maxima
(%i1) numberp (42);
(%o1)                         true
(%i2) numberp (-13/19);
(%o2)                         true
(%i3) numberp (3.14159);
(%o3)                         true
(%i4) numberp (-1729b-4);
(%o4)                         true
(%i5) map (numberp, [%e, %pi, %i, %phi, inf, minf]);
(%o5)      [false, false, false, false, false, false]
(%i6) declare (a, even, b, odd, c, integer, d, rational,
     e, irrational, f, real, g, imaginary, h, complex);
(%o6)                         done
(%i7) map (numberp, [a, b, c, d, e, f, g, h]);
(%o7) [false, false, false, false, false, false, false, false]
```

<!-- category: NumberTheory -->
<!-- keywords: numer -->
<!-- signatures: numer -->
### Variable: numer

`numer`は数値の引数を持つ（指数関数を含む）いくつかの数学関数を
浮動小数点に評価するようにします。
数値が与えられた`expr`の中の変数を値に置き換えるようにします。
それは `float`スイッチをオンにもします。


`%enumer`も参照してください。


例:







```maxima
(%i1) [sqrt(2), sin(1), 1/(1+sqrt(3))];
                                        1
(%o1)            [sqrt(2), sin(1), -----------]
                                   sqrt(3) + 1
(%i2) [sqrt(2), sin(1), 1/(1+sqrt(3))],numer;
(%o2) [1.414213562373095, .8414709848078965, .3660254037844387]
```

See also: `float`, `%enumer`.

<!-- category: NumberTheory -->
<!-- keywords: numer_pbranch -->
<!-- signatures: numer_pbranch -->
### Variable: numer_pbranch

デフォルト値: `false`


オプション変数`numer_pbranch`は
負の整数、有理数、または浮動小数点数のべきの数値評価を制御します。
`numer_pbranch`が`true`でかつ、指数が浮動小数点数であるか
オプション変数`numer`も`true`の時、
Maximaは主枝を使って数値結果を評価します。
そうでなければ、式整理されたが未評価の結果が返されます。


例:










```maxima
(%i1) (-2)^0.75;
(%o1) (-2)^0.75

(%i2) (-2)^0.75,numer_pbranch:true;
(%o2) 1.189207115002721*%i-1.189207115002721

(%i3) (-2)^(3/4);
(%o3) (-1)^(3/4)*2^(3/4)

(%i4) (-2)^(3/4),numer;
(%o4) 1.681792830507429*(-1)^0.75

(%i5) (-2)^(3/4),numer,numer_pbranch:true;
(%o5) 1.189207115002721*%i-1.189207115002721
```

See also: `numer`.

<!-- category: NumberTheory -->
<!-- keywords: numerval -->
<!-- signatures: numerval(x_1, expr_1, ..., x_n, expr_n) -->
### Function: numerval (x_1, expr_1, ..., x_n, expr_n)

変数`x_1`, ..., `x_n`を
`expr_1`, ..., `expr_n`に等しい数値を持つ変数だと宣言します。
もし `numer`フラグが `true`なら、
変数が現れる任意の式にて、数値は評価され、変数に代入されます。
`ev`も参照してください。


式`expr_1`, ..., `expr_n`は、任意の式を取り得ます。数値である必要はありません。

See also: `ev`.

<!-- category: NumberTheory -->
<!-- keywords: oddp -->
<!-- signatures: oddp(expr) -->
### Function: oddp (expr)

もしも*exp*が奇数であれば`true`を返し、

それ以外では`false`を返します。

<!-- category: NumberTheory -->
<!-- keywords: ratepsilon -->
<!-- signatures: ratepsilon -->
### Variable: ratepsilon

デフォルト値: 2.0e-8


`ratepsilon`は浮動小数点数を有理数に変換する際に使われる許容誤差です。

<!-- category: NumberTheory -->
<!-- keywords: rationalize -->
<!-- signatures: rationalize(expr) -->
### Function: rationalize (expr)

Maximaの式*expr*の中の倍精度浮動小数点やビッグフローすべてを同値の有理数に変換します。
もし浮動小数点の２値表現に詳しくなれば、`rationalize (0.1)`が1/10に等しくないことに
驚くかもしれません。
この振る舞いはMaximaに特別なわけではありません。―1/10は２値の循環小数表現を持ちます。












```maxima
(%i1) rationalize (0.5);
                                1
(%o1)                           -
                                2
(%i2) rationalize (0.1);
                               1
(%o2)                          --
                               10
(%i3) fpprec : 5$
(%i4) rationalize (0.1b0);
                             209715
(%o4)                        -------
                             2097152
(%i5) fpprec : 20$
(%i6) rationalize (0.1b0);
                     236118324143482260685
(%o6)                ----------------------
                     2361183241434822606848
(%i7) rationalize (sin (0.1*x + 5.6));
                              x    28
(%o7)                     sin(-- + --)
                              10   5
```


使用例:


















```maxima
(%i1) unitfrac(r) := block([uf : [], q],
    if not(ratnump(r)) then
       error("The input to 'unitfrac' must be a rational number"),
    while r # 0 do (
        uf : cons(q : 1/ceiling(1/r), uf),
        r : r - q),
    reverse(uf))$

(%o1) unitfrac(r) := block([uf : [], q], 
if not ratnump(r) then
   error("The input to 'unitfrac' must be a rational number"),
                                  1
while r # 0 do (uf : cons(q : ----------, uf), r : r - q), 
                                      1
                              ceiling(-)
                                      r
reverse(uf))
(%i2) unitfrac (9/10);
                            1  1  1
(%o2)                      [-, -, --]
                            2  3  15
(%i3) apply ("+", %);
                               9
(%o3)                          --
                               10
(%i4) unitfrac (-9/10);
                                  1
(%o4)                       [- 1, --]
                                  10
(%i5) apply ("+", %);
                                9
(%o5)                         - --
                                10
(%i6) unitfrac (36/37);
                        1  1  1  1    1
(%o6)                  [-, -, -, --, ----]
                        2  3  8  69  6808
(%i7) apply ("+", %);
                               36
(%o7)                          --
                               37
```

<!-- category: NumberTheory -->
<!-- keywords: ratnump -->
<!-- signatures: ratnump(expr) -->
### Function: ratnump (expr)

もし*expr*が整数リテラルもしくは整数リテラルの比なら `true`を返し、
そうでなければ `false`を返します。

