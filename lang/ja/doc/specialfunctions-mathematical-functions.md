## Mathematical Functions

<!-- category: SpecialFunctions -->
<!-- keywords: %e_to_numlog -->
<!-- signatures: %e_to_numlog -->
### Variable: %e_to_numlog

デフォルト値: `false`


`true`の時、
`r`をある有理数、`x`をある式とすると、
`%e^(r*log(x))`は`x^r`に整理されます。
`radcan`コマンドもこの変換を行い、その上この同類のさらに複雑な変換をすることに注意すべきです。
`logcontract`コマンドは`log`を含む式を「短縮」します。

<!-- category: SpecialFunctions -->
<!-- keywords: %emode -->
<!-- signatures: %emode -->
### Variable: %emode

デフォルト値: `true`


`%emode`が`true`の時、
`%e^(%pi %i x)`は以下のように整理されます。


もし`x`が浮動小数点、整数、もしくは1/2, 1/3, 1/4, 1/6の整数倍なら、
`%e^(%pi %i x)`は`cos (%pi x) + %i sin (%pi x)`に整理された後、
さらに整理されます。


他の数値`x`に関して、
`%e^(%pi %i x)`は、`%e^(%pi %i y)`に整理されます。
ここで`y`は`x - 2 k`（`k`は`abs(y) < 1`が成り立つような整数）です。


`%emode`が`false`の時には、
`%e^(%pi %i x)`の特別な整理は実行されません。

<!-- category: SpecialFunctions -->
<!-- keywords: %enumer -->
<!-- signatures: %enumer -->
### Variable: %enumer

デフォルト値: `false`


`%enumer`が`true`の時、
`numer`が`true`の時はいつでも、
`%e`は数値2.718...に置き換えられます。


`%enumer`が`false`の時、
`%e^x`の指数が数に評価される時だけ、
この代入が実行されます。


`ev`, `numer`も参照してください。

See also: `ev`, `numer`.

<!-- category: SpecialFunctions -->
<!-- keywords: exp -->
<!-- signatures: exp(x) -->
### Function: exp (x)

指数関数を表します。
入力にある`exp (x)`のインスタンスは、`%e^x`に整理されます;
`exp`は整理された式の中には現れません。


もし`demoivre`が`true`で、かつ、
`b`が`%i`を含まないなら、
`%e^(a + b %i)`は`%e^(a (cos(b) + %i sin(b)))`に整理されます。
`demoivre`を参照してください。


`%emode`が`true`の時、
`%e^(%pi %i x)`は整理されます。
`%emode`を参照してください。


`%enumer`が`true`の時、
`numer`が`true`の時にはいつでも
`%e`は2.718...に置き換えれます。
`%enumer`を参照してください。

See also: `demoivre`, `%emode`, `%enumer`.

<!-- category: SpecialFunctions -->
<!-- keywords: li -->
<!-- signatures: li[s](z) -->
### Function: li ([s](z))

次数*s*、引数*z*の多重対数関数を表します。
これは、以下の無限級数で定義されます。



$$
{\rm Li}_s \left(z\right) = \sum_{k=1}^\infty {z^k \over k^s}
$$


```maxima
inf
                                 ====   k
                                 \     z
                        Li (z) =  >    --
                          s      /      s
                                 ====  k
                                 k = 1
```


`li [1]`は、`- log (1 - z)`です。
`li [2]`と`li [3]`は、それぞれ、dilogarithm関数、trilogarithm関数です。


次数が1の時、多重対数関数は`- log (1 - z)`に整理され、
もし*z*が実数もしくは複素数の浮動小数点数、もしくは、`numer`評価フラグが有効なら、さらに数値に整理されます。


次数が2もしくは3の時、
もし*z*が実数の浮動小数点数、もしくは`numer`評価フラグが有効なら、
多重対数関数は数値に整理されます。


例:














```maxima
(%i1) assume (x > 0);
(%o1)                        [x > 0]
(%i2) integrate ((log (1 - t)) / t, t, 0, x);
(%o2)                       - li (x)
                                2
(%i3) li [2] (7);
(%o3)                        li (7)
                               2
(%i4) li [2] (7), numer;
(%o4)        1.24827317833392 - 6.113257021832577 %i
(%i5) li [3] (7);
(%o5)                        li (7)
                               3
(%i6) li [2] (7), numer;
(%o6)        1.24827317833392 - 6.113257021832577 %i
(%i7) L : makelist (i / 4.0, i, 0, 8);
(%o7)   [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
(%i8) map (lambda ([x], li [2] (x)), L);

(%o8) [0, .2676526384986274, .5822405249432515, 
.9784693966661848, 1.64493407, 2.190177004178597
 - .7010261407036192 %i, 2.374395264042415
 - 1.273806203464065 %i, 2.448686757245154
 - 1.758084846201883 %i, 2.467401098097648
 - 2.177586087815347 %i]

(%i9) map (lambda ([x], li [3] (x)), L);
(%o9) [0, .2584613953442624, 0.537213192678042, 
.8444258046482203, 1.2020569, 1.642866878950322
 - .07821473130035025 %i, 2.060877505514697
 - .2582419849982037 %i, 2.433418896388322
 - .4919260182322965 %i, 2.762071904015935
 - .7546938285978846 %i]
```

<!-- category: SpecialFunctions -->
<!-- keywords: log -->
<!-- signatures: log(x) -->
### Function: log (x)

*x*の自然対数（基数$e$の対数）を表します。


Maximaは、基数10や他の基数の対数の組み込み関数を持ちません。
`log10(x) := log(x) / log(10)`は、役立つ定義です。


対数の整理と評価は、いくつかのグローバルフラグによって管理されます:



**`logexpand`** — `log(a^b)`を`b*log(a)`にします。
もし`all`に設定されているなら、
`log(a*b)`も`log(a)+log(b)`に整理されます。
もし`super`に設定されているなら,
有理数`a/b`ただし`a#1`について`log(a/b)`も`log(a)-log(b)`に整理されます。
(整数`b`に関して`log(1/b)`はいつも整理されます。)
もし`false`に設定されているなら、
これらのすべての整理は止められます。
**`logsimp`** — もし`false`なら、
`%e`は、`log`を含む累乗へ整理がなされます。
**`lognumer`** — もし`true`なら、
引数は、`log`の計算の前に絶対値に変換されます。
もし`numer`も`true`なら、
`log`の引数に負の整数を与えたとき、
引数は、`log`の計算の前に絶対値に変換されます。
**`lognegint`** — もし`true`なら、正の整数`n`に対して規則
`log(-n)` -> `log(n)+%i*%pi`
が実装されます。
**`%e_to_numlog`** — `true`の時、
`r`をある有理数、`x`をある式とすると、
式`%e^(r*log(x))`は`x^r`に整理されます。
`radcan`コマンドもこの変換を行い、その上この同類のさらに複雑な変換をすることに注意すべきです。
`logcontract`コマンドは`log`を含む式を「短縮」します。

<!-- category: SpecialFunctions -->
<!-- keywords: logabs -->
<!-- signatures: logabs -->
### Variable: logabs

デフォルト値: `false`


例えば`integrate(1/x,x)`のように、logが生成される不定積分を実行する時、
もし`logabs`が`true`なら
もし`logabs`が`false`なら
答えは、`log(...)`の形で与えられます。
定積分については、
終端での不定積分の「評価」がしばしば必要になるので、`logabs:true`設定が使われます。

<!-- category: SpecialFunctions -->
<!-- keywords: logarc -->
<!-- signatures: logarc(expr) -->
### Variable: logarc

グローバル変数`logarc`が`true`の時、
逆円関数や逆双曲線関数は、同値の対数関数に置き換えられます。
`logarc`のデフォルト値は`false`です。


関数`logarc(expr)`は、
グローバル変数`logarc`を設定することなしに、式*expr*に対して上記置き換えを実行します。

<!-- category: SpecialFunctions -->
<!-- keywords: logconcoeffp -->
<!-- signatures: logconcoeffp -->
### Variable: logconcoeffp

デフォルト値: `false`


`logcontract`を使った時、どの係数が短縮されるかを制御します。
引数１つの述語論理関数の名前に設定することができます。
例えば、もしSQRTを生成したいなら、
`logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$`を実行できます。
すると、
`logcontract(1/2*log(x));`は`log(sqrt(x))`を与えるでしょう。

<!-- category: SpecialFunctions -->
<!-- keywords: logcontract -->
<!-- signatures: logcontract(expr) -->
### Function: logcontract (expr)

形式`a1*log(b1) + a2*log(b2) + c`の部分式を
`log(ratsimp(b1^a1 * b2^a2)) + c`に変換しながら、
再帰的に式*expr*を走査します。







```maxima
(%i1) 2*(a*log(x) + 2*a*log(y))$
(%i2) logcontract(%);
                                 2  4
(%o2)                     a log(x  y )
```


`declare(n,integer);`を実行すると、
`logcontract(2*a*n*log(x));`は、`a*log(x^(2*n))`に整理されます。
この方法で「短縮」される係数は、ここで2や`n`に当たるもので、`featurep(coeff,integer)`を満たします。
ユーザーは、
オプション`logconcoeffp`を引数１つの述語論理関数名に設定することで、
どの係数を短縮するか制御できます。
例えば、もしSQRTを生成したいなら、
`logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$`を実行できます。
すると、
`logcontract(1/2*log(x));`は`log(sqrt(x))`を与えるでしょう。

<!-- category: SpecialFunctions -->
<!-- keywords: logexpand -->
<!-- signatures: logexpand -->
### Variable: logexpand

デフォルト値: `false`


もし`true`なら、
`log(a^b)`が`b*log(a)`になるようにします。
もし`all`に設定されているなら、
`log(a*b)`も`log(a)+log(b)`に整理されます。
もし`super`に設定されているなら,
有理数`a/b`ただし`a#1`について`log(a/b)`も`log(a)-log(b)`に整理されます。
(整数`b`に関して`log(1/b)`はいつも整理されます。)
もし`false`に設定されているなら、
これらのすべての整理は止められます。

<!-- category: SpecialFunctions -->
<!-- keywords: lognegint -->
<!-- signatures: lognegint -->
### Variable: lognegint

デフォルト値: `false`


もし`true`なら、正の整数`n`に対して規則
`log(-n)` -> `log(n)+%i*%pi`
が実装されます。

<!-- category: SpecialFunctions -->
<!-- keywords: lognumer -->
<!-- signatures: lognumer -->
### Variable: lognumer

デフォルト値: `false`


もし`true`なら、
引数は、`log`の計算の前に絶対値に変換されます。
もし`numer`も`true`なら、
`log`の引数に負の整数を与えたとき、
引数は、`log`の計算の前に絶対値に変換されます。

<!-- category: SpecialFunctions -->
<!-- keywords: logsimp -->
<!-- signatures: logsimp -->
### Variable: logsimp

デフォルト値: `true`


もし`false`なら、
`%e`は、`log`を含む累乗へ整理がなされます。

<!-- category: SpecialFunctions -->
<!-- keywords: plog -->
<!-- signatures: plog(x) -->
### Function: plog (x)

`-%pi` < `carg(x)` <= `+%pi`を虚部係数とする複素数値の自然対数の主値を表します。

<!-- category: SpecialFunctions -->
<!-- keywords: sqrt -->
<!-- signatures: sqrt(x) -->
### Function: sqrt (x)

*x*の平方根。
内部的には`x^(1/2)`で表現されます。
`rootscontract`も参照してください。


`radexpand`が`true`なら、nのべき乗となる積の因子のn番目の根を
累乗根の外部に押し出すようにします。
例えば、
`radexpand`が`true`の時だけ、`sqrt(16*x^2)`は`4*x`になります。

