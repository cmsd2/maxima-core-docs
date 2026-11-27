## to_poly_solve

<!-- category: Solving -->
<!-- keywords: %and -->
<!-- signatures: %and -->
### Function: %and

演算子 `%and`は整理化(simplifying)非短絡論理積です。
Maximaは
`%and`式をtrueかfalseか論理的に同値ですが整理された式に整理します。
演算子 `%and`は結合的で可換でべき等的です。
そして、
`%and`が名詞形を返す時、
`%and`の引数は非冗長なソートされたリストを形成します;
例えば、



```maxima
(%i1) a %and (a %and b);
(%o1)                       a %and b
```


もし積の引数の1つが *明示的に*もう一つの引数の否定なら、
`%and`はfalseを返します:



```maxima
(%i2) a %and (not a);
(%o2)                         false
```


積のいずれかのメンバーがfalseなら、
たとえ他のメンバーが明白に非ブーリアンでも積はfalseに整理されます;
例えば、



```maxima
(%i3) 42 %and false;
(%o3)                         false
```


inequation(すなわち、不等もしくは等式)の`%and`式の任意の引数は
Fourier消去パッケージを使って整理されます。
Fourier消去整理器は
すべてでないですがいくつかの非線形inequationを線形inequationに変換する
プリプロセッサを持ちます;
例えば、Fourier消去コードは
`abs(x) + 1 > 0`を trueに整理します。だから、



```maxima
(%i4) (x < 1) %and (abs(x) + 1 > 0);
(%o4)                         x < 1
```


**注釈**  


- *
オプション変数 `prederror`は
`%and`式の整理を変え*ません*。
- *
演算子の優先順位エラーを避けるため、
演算子 `%and, %or`と `not`を含む複合式は完全に括弧でくくらなくてはいけません。
- *
Maxima演算子 `and`と `or`はどちらも短絡的です。
なので `and`は結合的でなかったり可換ではなかったりします。


**制限** 積 `%and`はinequationを
*大域的にではなく局所的に*整理します。
これは以下のような積はfalseに整理*されない*ことを意味します。



```maxima
(%i5) (x < 1) %and (x > 1);
(%o5)                 (x > 1) %and (x < 1)
```


また、 Fourier消去コードは事実データベースを*無視します*。



```maxima
(%i6) assume(x > 5);
(%o6)                        [x > 5]
(%i7) (x > 1) %and (x > 2);
(%o7)                 (x > 1) %and (x > 2)
```


最終的に、同値の線形inequationに容易に変換されない非線形inequationは整理されません。


`%or`上に `%and`を分配するためのサポートはありません;
`%and`上に論理否定を分配するサポートもありません。


**利用のためには** `load("to_poly_solve")`


**関連関数** `%or, %if, and, or, not`


**状況** 演算子 `%and`は実験的です;
この関数の仕様は変更の可能性があり、
その機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: %if -->
<!-- signatures: %if(bool, a, b) -->
### Function: %if (bool, a, b)

演算子 `%if`は整理化条件文です。
*条件* *bool*はブーリアン値でなければいけません。
条件がtrueの時、二番目の引数を返します;
条件がfalseの時、三番目の引数を返します;
その他の場合、名詞形を返します。


Maxima inequations (不等式か等式)はブーリアン値では*ありません*;
例えば、 Maximaは $5 < 6$をtrueに整理 *しません*し、
$5 = 6$をfalseに整理しません;
しかしながら、 to false; however, in
the context of a conditional to an 
`%if`文への条件の文脈では、
Maximaは *自動的に*inequationの真値を決定しようとします。
例:



```maxima
(%i1) f : %if(x # 1, 2, 8);
(%o1)                 %if(x - 1 # 0, 2, 8)
(%i2) [subst(x = -1,f), subst(x=1,f)];
(%o2)                        [2, 8]
```


もし条件がinequationを含むなら、
MaximaはFourier消去パッケージを使ってそれを整理します。


**注釈** 



- *
もし条件が明白に非ブーリアンなら、Maximaは名詞形を返します:



```maxima
(%i3) %if(42,1,2);
(%o3)                     %if(42, 1, 2)
```



- *
Maxima演算子 `if`はn項演算子ですが、演算子 `%if`は n項演算子*ではないです*。


**制限** Fourier消去コードは
同値の線形inequationに容易に変換可能な非線形inequationだけを
整理します。


**利用には:** `load("to_poly_solve")`


**状況:** 演算子 `%if`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: %or -->
<!-- signatures: %or -->
### Function: %or

演算子 `%or`は整理化非短絡論理和です。
Maximaは
`%or`式をtrueかfalseか論理的に同値ですが整理された式に整理します。
演算子 `%or`は結合的で可換でべき等です。
そして
`%or`が名詞形を返す時、
`%or`の引数は非冗長なソートされたリストを形成します;
例えば、



```maxima
(%i1) a %or (a %or b);
(%o1)                        a %or b
```


もし和のメンバーの１つが*明示的に*他のメンバーの否定なら、
`%or`はtrueを返します:



```maxima
(%i2) a %or (not a);
(%o2)                         true
```


もし和の任意のメンバーがtrueなら、
たとえ和の他のメンバーが明白に非ブーリアンでも和はtrueに整理されます。
例えば



```maxima
(%i3) 42 %or true;
(%o3)                         true
```


inequation(不等式か等式)である `%or`式の任意の引数は
Fourier消去パッケージを使って整理されます。
Fourier消去コードは `abs(x) + 1 > 0`をtrueに整理します。
なので、



```maxima
(%i4) (x < 1) %or (abs(x) + 1 > 0);
(%o4)                         true
```


**注釈**  


- *
オプション変数 `prederror`は
`%or`式の整理を変更*しません*。
- *
演算子 `%and, %or`, `not`を含む複合式は括弧でくくらなければいけません;
これらの演算子の結合力は期待と一致しないことがあります。
- *
Maxima演算子 `and`と `or`はどちらも短絡的です。
なので `or`は結合的でないか可換でないかです。


**制限** 和 `%or`はinequationを
*大域的にではなく、局所的に*整理します。
これは以下のような和はtrueに整理*されない*ことを意味します。





```maxima
(%i1) (x < 1) %or (x >= 1);
(%o1) (x > 1) %or (x >= 1)
```


更に Fourier消去コードは事実データベースを無視します:



```maxima
(%i2) assume(x > 5);
(%o2)                        [x > 5]
(%i3) (x > 1) %and (x > 2);
(%o3)                 (x > 1) %and (x > 2)
```


最終的に、同値の線形inequationに容易に変換されない非線形inequationは整理されません。


両方ともfalseである項を探すアルゴリズムは弱いものです;
また、`%and`上に `%or`を分配するためのサポートはありません;
`%or`上に論理否定を分配するサポートもありません。


**利用のためには** `load("to_poly_solve")`


**関連関数** `%or, %if, and, or, not`


**状況** 演算子 `%or`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: complex_number_p -->
<!-- signatures: complex_number_p(x) -->
### Function: complex_number_p (x)

もし引数が
 `a + %i * b`, `a`, `%i b`, `%i`のいずれかなら、
述語論理 `complex_number_p`はtrueを返します。
ここで `a`と `b`は有理数か(多倍長浮動小数点数を含む)浮動小数点数です;
他のすべての入力に対して、
`complex_number_p`はfalseを返します; 例えば



```maxima
(%i1) map('complex_number_p,[2/3, 2 + 1.5 * %i, %i]);
(%o1)                  [true, true, true]
(%i2) complex_number_p((2+%i)/(5-%i));
(%o2)                         false
(%i3) complex_number_p(cos(5 - 2 * %i));
(%o3)                         false
```


**関連関数** `isreal_p`


**利用するには** `load("to_poly_solve")`


**状況** 関数 `complex_number_p`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: compose_functions -->
<!-- signatures: compose_functions(l) -->
### Function: compose_functions (l)

関数コール `compose_functions(l)`は
リスト *l*の中の関数の合成をラムダ形を返します。
関数は*右*から *左*へ適用されます; 例えば



```maxima
(%i1) compose_functions([cos, exp]);
                                        %g151
(%o1)             lambda([%g151], cos(%e     ))
(%i2) %(x);
                                  x
(%o2)                       cos(%e )
```


関数リストが空のとき、恒等関数を返します:



```maxima
(%i3) compose_functions([]);
(%o3)                lambda([%g152], %g152)
(%i4)  %(x);
(%o4)                           x
```


**注釈** 


- *
Maximaがリストメンバーがシンボルやラムダ形でないか決める時、
(`compose_functions`*ではなく*) `funmake`がエラーをシグナルします:



```maxima
(%i5) compose_functions([a < b]);

funmake: first argument must be a symbol, subscripted symbol,
string, or lambda expression; found: a < b
#0: compose_functions(l=[a < b])(to_poly_solve.mac line 40)
 -- an error. To debug this try: debugmode(true);
```



- *
名前の衝突を避けるために、独立変数は
関数 `new_variable`が決めます。



```maxima
(%i6) compose_functions([%g0]);
(%o6)              lambda([%g154], %g0(%g154))
(%i7) compose_functions([%g0]);
(%o7)              lambda([%g155], %g0(%g155))
```



- *
 
独立変数が違っても、
Maximaはこれらのラムダ形が意味的に等しいことを演繹できます:



```maxima
(%i8) is(equal(%o6,%o7));
(%o8)                         true
```


**利用するには** `load("to_poly_solve")`


**状況** 関数 `compose_functions`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: dfloat -->
<!-- signatures: dfloat(x) -->
### Function: dfloat (x)

関数 `dfloat`は
`float`に似ていますが、
`float`が IEEE 倍精度浮動小数点数に評価するのを失敗した時、
関数 `dfloat`は
`rectform`を適用します; 例えば



```maxima
(%i1) float(4.5^(1 + %i));
                               %i + 1
(%o1)                       4.5
(%i2) dfloat(4.5^(1 + %i));
(%o2)        4.48998802962884 %i + .3000124893895671
```


**注釈** 



- *
式の直交形は
数値評価には不完全で合わないかもしれません–例えば、
直交形は不必要に浮動小数点数の差(桁落ち)を含むかもしれません。
- *
識別子 `float`は(デフォルト値がfalseの)オプション変数であり
かつ関数名です。


**関連関数** `float, bfloat`


**利用するには** `load("to_poly_solve")`


**状況** 関数 `dfloat`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: elim -->
<!-- signatures: elim(l, x) -->
### Function: elim (l, x)

関数 `elim`は
集合もしくはリスト `l`内の等式から
集合もしくはリスト`x`内の変数を消去します。
`x`のメンバーそれぞれはシンボルでなければいけません;
 must be a symbol; the members of 
`l`のメンバーは等式か零に等しいと仮定される式であり得ます。


関数 `elim`は2つのリストのリストを返します;
一番目は変数が消去された式のリストです;
二番目はピボットのリストです;
二番目のリストは
`elim`が変数を消去するのに使った式のリストです。


以下は線形方程式を消去する例です:



```maxima
(%i1) elim(set(x + y + z = 1, x - y  - z = 8, x - z = 1), 
           set(x,y));
(%o1)            [[2 z - 7], [y + 7, z - x + 1]]
```


`x`と `y`の消去は一つの等式 `2 z - 7 = 0`をもたらします;
等式 `y + 7 = 0`と `z - z + 1 = 1`がピボットとして使われました。
これらの等式から3つの変数すべての消去は、線形系を三角化します:



```maxima
(%i2) elim(set(x + y + z = 1, x - y  - z = 8, x - z = 1),
           set(x,y,z));
(%o2)           [[], [2 z - 7, y + 7, z - x + 1]]
```


もちろん、等式は線形である必要はありません:



```maxima
(%i3) elim(set(x^2 - 2 * y^3 = 1,  x - y = 5), [x,y]);
                     3    2
(%o3)       [[], [2 y  - y  - 10 y - 24, y - x + 5]]
```


ユーザーは変数が消去される順序を制御しません。
確かに、アルゴリズムは
最良のピボットと最良の消去順序を選ぼうとする発見的方法を使います。


**注釈** 



- *
関連関数 `eliminate`と違い、
等式の数が変数の数と等しい時、関数 `elim`は
`solve`を呼び出し*ません*。
- *
関数 `elim`は終結式を適用することで機能します;
オプション変数 `resultant`は
Maximaがどのアルゴリズムを使うか決めます。
`sqfr`を使って、 Maximaは
それぞれの終結式を因数分解し、
多重零点を抑制します。
- *
`elim`は多項式方程式の非線形一式を三角化します;
三角化された集合の解集合は
三角化されていない集合の解集合よりも大きい*かもしれません*。
例えば、、
三角化された方程式は*見せかけの*解を持ち得ます。


**関連関数** *elim_allbut, eliminate_using, eliminate*


**オプション変数** *resultant*


**利用するには** `load("to_poly")`


**状況** 関数 `elim`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: elim_allbut -->
<!-- signatures: elim_allbut(l, x) -->
### Function: elim_allbut (l, x)

この関数は
 `elim`に似ています。
等式のリスト `l`内の
リスト `x`内の変数を *除いて*
変数すべてを消去することを除いて



```maxima
(%i1) elim_allbut([x+y = 1, x - 5*y = 1],[]);
(%o1)                 [[], [y, y + x - 1]]
(%i2) elim_allbut([x+y = 1, x - 5*y = 1],[x]);
(%o2)                [[x - 1], [y + x - 1]]
```


**利用するには** `load("to_poly")`


**オプション変数** *resultant*


**関連関数** *elim, eliminate_using, eliminate*


**状況** 関数 `elim_allbut`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: eliminate_using -->
<!-- signatures: eliminate_using(l, e, x) -->
### Function: eliminate_using (l, e, x)

Using `e` as the pivot, eliminate the symbol `x` from the
list or set of equations in `l`.  The function `eliminate_using`
returns a set.



```maxima
(%i1) eq : [x^2 - y^2 - z^3 , x*y - z^2 - 5, x - y + z];
               3    2    2     2
(%o1)      [- z  - y  + x , - z  + x y - 5, z - y + x]
(%i2) eliminate_using(eq,first(eq),z);
        3              2      2      3    2
(%o2) {y  + (1 - 3 x) y  + 3 x  y - x  - x , 
                        4    3  3       2  2             4
                       y  - x  y  + 13 x  y  - 75 x y + x  + 125}
(%i3) eliminate_using(eq,second(eq),z);
        2            2       4    3  3       2  2             4
(%o3) {y  - 3 x y + x  + 5, y  - x  y  + 13 x  y  - 75 x y + x
                                                           + 125}
(%i4) eliminate_using(eq, third(eq),z);
        2            2       3              2      2      3    2
(%o4) {y  - 3 x y + x  + 5, y  + (1 - 3 x) y  + 3 x  y - x  - x }
```


**オプション変数** *resultant*


**関連関数** *elim, eliminate, elim_allbut*


**利用するには** `load("to_poly")`


**状況** 関数 `elimimate_using`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: fourier_elim -->
<!-- signatures: fourier_elim([eq1, eq2, ...], [var1, var, ...]) -->
### Function: fourier_elim ([eq1, eq2, ...], [var1, var, ...])

Fourier消去は
Gauss消去の線形inequation(等式か不等式)に関する類似物です。
関数コール `fourier_elim([eq1, eq2, ...], [var1, var2, ...]`は
線形inequationsのリスト `[eq1, eq2, ...]`上の
変数 `[var1, var2, ...]`に関するFourier消去です;
例えば



```maxima
(%i1) fourier_elim([y-x < 5, x - y < 7, 10 < y],[x,y]);
(%o1)            [y - 5 < x, x < y + 7, 10 < y]
(%i2) fourier_elim([y-x < 5, x - y < 7, 10 < y],[y,x]);
(%o2)        [max(10, x - 7) < y, y < x + 5, 5 < x]
```


Eliminating first with respect to
最初に $x$を次に $y$を消去することは
$y$に依存する、$x$に関する下限と上限、
そして$y$に関する下限と上限(それらは数です)ををもたらします。
他の順序での消去は
$x$依存の$y$の下限と上限、
そして$x$の数値的下限と上限を与えます。


必要な時、 `fourier_elim`はinequationのリストの*論理和*を返します:



```maxima
(%i3) fourier_elim([x # 6],[x]);
(%o3)                  [x < 6] or [6 < x]
```


解集合が空の時、 `fourier_elim`は `emptyset`を返し、
解集合が実数すべての時、 `fourier_elim`は `universalset`を返します;
例えば



```maxima
(%i4) fourier_elim([x < 1, x > 1],[x]);
(%o4)                       emptyset
(%i5) fourier_elim([minf < x, x < inf],[x]);
(%o5)                     universalset
```


非線形inequationに対して、 `fourier_elim`は
(幾分) 整理されたinequationsのリストを返します:



```maxima
(%i6) fourier_elim([x^3 - 1 > 0],[x]);

               2                             2
(%o6) [1 < x, x  + x + 1 > 0] or [x < 1, - (x  + x + 1) > 0]

(%i7) fourier_elim([cos(x) < 1/2],[x]);
(%o7)                  [1 - 2 cos(x) > 0]
```


inequationのリストの代わりに、
`fourier_elim`の一番目の引数は
論理和か論理積であるかもしれません:



```maxima
(%i8) fourier_elim((x + y < 5) and (x - y >8),[x,y]);
                                              3
(%o8)            [y + 8 < x, x < 5 - y, y < - -]
                                              2
(%i9) fourier_elim(((x + y < 5) and x < 1) or  (x - y >8),[x,y]);
(%o9)          [y + 8 < x] or [x < min(1, 5 - y)]
```


関数 `fourier_elim`は
inequation演算子 `<, <=, >, >=, #`, `=`をサポートします。


Fourier消去コードは
絶対値や最小、最大関数を含むいくつかの非線形inequationを
線形inequationに変換する
プリプロセッサを持ちます．
加えて、プリプロセッサは
線形項の積か商であるいくつかの式を扱います:



```maxima
(%i10) fourier_elim([max(x,y) > 6, x # 8, abs(y-1) > 12],[x,y]);
(%o10) [6 < x, x < 8, y < - 11] or [8 < x, y < - 11]
 or [x < 8, 13 < y] or [x = y, 13 < y] or [8 < x, x < y, 13 < y]
 or [y < x, 13 < y]
(%i11) fourier_elim([(x+6)/(x-9) <= 6],[x]);
(%o11)           [x = 12] or [12 < x] or [x < 9]
(%i12) fourier_elim([x^2 - 1 # 0],[x]);
(%o12)      [- 1 < x, x < 1] or [1 < x] or [x < - 1]
```


**利用するには** `load("fourier_elim")`

<!-- category: Solving -->
<!-- keywords: isreal_p -->
<!-- signatures: isreal_p(e) -->
### Function: isreal_p (e)

述語論理 `isreal_p`は、
Maximaが
`e`が実数線*全体*上で実数値であることを
決められる時
trueを返します;
Maximaが
実数線の空でないある部分集合上で`e`が実数値で *ない*ことを
決められる時
falseを返します;
他の場合、名詞形を返します。



```maxima
(%i1) map('isreal_p, [-1, 0, %i, %pi]);
(%o1)               [true, true, false, true]
```


Maxima変数は実と仮定されます; たとえば



```maxima
(%i2) isreal_p(x);
(%o2)                         true
```


関数 `isreal_p`は事実データベースを検査します:



```maxima
(%i3) declare(z,complex)$

(%i4) isreal_p(z);
(%o4)                      isreal_p(z)
```


**制限**
頻繁すぎるほど `isreal_p`は
falseを返すことができる時に名詞形を返します;
対数函数は実数線全体で実数値ではありません。
だから `isreal_p(log(x))`はfalseを返すべきです;
しかしながら



```maxima
(%i5) isreal_p(log(x));
(%o5)                   isreal_p(log(x))
```


**利用するには** `load("to_poly_solve")`


**関連関数** *complex_number_p*


**状況** 関数 `real_p`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: new_variable -->
<!-- signatures: new_variable(type) -->
### Function: new_variable (type)

`%[z,n,r,c,g]k`という形のユニークなシンボルを返します。
ここで `k`は整数です
$type$に許される値は *integer, natural_number, real, natural_number,* *general*です。
(自然数(natural number)は *非負整数*を意味します;
なので零は自然数です
自然数の定義のすべてではありませんがいくつかは零を*除外します*。)


$type$が許される値の１つでない時、
$type$は $general$にデフォルト設定されます。
整数、自然数、複素数に対して、
Maximaは自動的にこの情報を事実データベースに追加します。



```maxima
(%i1) map('new_variable,
          ['integer, 'natural_number, 'real, 'complex, 'general]);
(%o1)          [%z144, %n145, %r146, %c147, %g148]
(%i2) nicedummies(%);
(%o2)               [%z0, %n0, %r0, %c0, %g0]
(%i3) featurep(%z0, 'integer);
(%o3)                         true
(%i4) featurep(%n0, 'integer);
(%o4)                         true
(%i5) is(%n0 >= 0);
(%o5)                         true
(%i6) featurep(%c0, 'complex);
(%o6)                         true
```


**注釈** 一般に、`new_variable`の引数はクォートすべきです。
クォートは以下に似たエラーを防ぎます。



```maxima
(%i7) integer : 12$

(%i8) new_variable(integer);
(%o8)                         %g149
(%i9) new_variable('integer);
(%o9)                         %z150
```


**関連関数** *nicedummies*


**利用するには** `load("to_poly_solve")`


**状況** 関数 `new_variable`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: nicedummies -->
<!-- signatures: nicedummies -->
### Function: nicedummies

関数 `nicedummies`は
`new_variable`が導入した式の中の変数を零から再インデックスします;



```maxima
(%i1) new_variable('integer) + 52 * new_variable('integer);
(%o1)                   52 %z136 + %z135
(%i2) new_variable('integer) - new_variable('integer);
(%o2)                     %z137 - %z138
(%i3) nicedummies(%);
(%o3)                       %z0 - %z1
```


**関連関数** *new_variable*


**利用するには** `load("to_poly_solve")`


**状況** 関数 `nicedummies`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: parg -->
<!-- signatures: parg(x) -->
### Function: parg (x)

関数 `parg`は
複素偏角関数 `carg`の整理化バージョンです;
例えば



```maxima
(%i1) map('parg,[1,1+%i,%i, -1 + %i, -1]);
                        %pi  %pi  3 %pi
(%o1)               [0, ---, ---, -----, %pi]
                         4    2     4
```


一般に非定数入力に対して `parg`は名詞形を返します;例えば



```maxima
(%i2) parg(x + %i * sqrt(x));
(%o2)                 parg(x + %i sqrt(x))
```


`sign`を使って入力が正の実数か負の実数か決めることができる時
`parg`は非定数入力に対して非名詞形を返します。
以下は2つの例です:





```maxima
(%i3) parg(abs(x));
(%o3) 0
(%i4) parg(-x^2-1);
(%o4)                          %pi
```


**注釈** `sign`関数は
複素数と宣言された変数(`declare(x,complex)`)を
ほとんど無視します;
複素数と宣言された変数に対して、
`parg`は間違った値を返す可能性があります;
例えば





```maxima
(%i1) declare(x,complex)$

(%i2) parg(x^2 + 1);
(%o2) 0
```


**Related function** *carg, isreal_p*


**利用するには** `load("to_poly_solve")`


**状況** 関数 `parg`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: real_imagpart_to_conjugate -->
<!-- signatures: real_imagpart_to_conjugate(e) -->
### Function: real_imagpart_to_conjugate (e)

関数 `real_imagpart_to_conjugate`は
`realpart`と `imagpart`をすべて
`conjugate`を含む代数的に同値な式に置き換えます。



```maxima
(%i1) declare(x, complex)$

(%i2) real_imagpart_to_conjugate(realpart(x) +  imagpart(x) = 3);
          conjugate(x) + x   %i (x - conjugate(x))
(%o2)     ---------------- - --------------------- = 3
                 2                     2
```


**利用するには** `load("to_poly_solve")`


**状況** 関数 `real_imagpart_to_conjugate`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: rectform_log_if_constant -->
<!-- signatures: rectform_log_if_constant(e) -->
### Function: rectform_log_if_constant (e)

関数 `rectform_if_constant`は
`log(c)`の形の項をすべて
`rectform(log(c))`に変換します。
ここで `c`は宣言された定数式か明示的に宣言された定数です。



```maxima
(%i1) rectform_log_if_constant(log(1-%i) - log(x - %i));
                                 log(2)   %i %pi
(%o1)            - log(x - %i) + ------ - ------
                                   2        4
(%i2) declare(a,constant, b,constant)$

(%i3) rectform_log_if_constant(log(a + %i*b));
                       2    2
                  log(b  + a )
(%o3)             ------------ + %i atan2(b, a)
                       2
```


**利用するには** `load("to_poly_solve")`


**状況** 関数 `rectform_log_if_constant`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: simp_inequality -->
<!-- signatures: simp_inequality(e) -->
### Function: simp_inequality (e)

関数 `simp_inequality`は
inequationの論理積と論理和にいくつかの整理を適用します。


**制限** 関数 `simp_inequality`は少なくとも2つの点で制限されます;
第一に整理が局所的です; 例えば





```maxima
(%i1) simp_inequality((x > minf) %and (x < 0));
(%o1) (x>1) %and (x<1)
```


第二に `simp_inequality`は事実データベースを参照しません:



```maxima
(%i2) assume(x > 0)$

(%i3) simp_inequality(x > 0);
(%o3)                         x > 0
```


**利用するには** `load("to_poly_solve")`


**状況** 関数 `simp_inequality`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: standardize_inverse_trig -->
<!-- signatures: standardize_inverse_trig(e) -->
### Function: standardize_inverse_trig (e)

この関数は
恒等式 `cot(x) = atan(1/x), acsc(x) = asin(1/x),`と
 `asec, acoth, acsch` `asech`に関する類似
の恒等式を式に適応します。
Abramowitz and Stegun, 
Eqs. 4.4.6 から 4.4.8までと 4.6.4から 4.6.6までを参照してください。


**利用するには** `load("to_poly_solve")`


**状況** 関数 `standardize_inverse_trig`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: subst_parallel -->
<!-- signatures: subst_parallel(l, e) -->
### Function: subst_parallel (l, e)

`l`が単一の等式か等式のリストの時、
それぞれの等式の右辺側を左辺に代入します。
代入は並列に行われます; 例えば



```maxima
(%i1) load("to_poly_solve")$

(%i2) subst_parallel([x=y,y=x], [x,y]);
(%o2)                        [y, x]
```


これを順にされる代入と比較します:



```maxima
(%i3) subst([x=y,y=x],[x,y]);
(%o3)                        [x, x]
```


関数 `subst_parallel`は
`subst_parallel`は非アトムの代入を許すことを除いて
`sublis`と似ています;
例えば



```maxima
(%i4) subst_parallel([x^2 = a, y = b], x^2 * y);
(%o4)                          a b
(%i5) sublis([x^2 = a, y = b], x^2 * y);

                                                             2
sublis: left-hand side of equation must be a symbol; found: x
 -- an error. To debug this try: debugmode(true);
```


`subst_parallel`が行う代入は文字通りであり意味論的ではありません;
なので
`subst_parallel`は
$x * y$が $x^2 * y$の部分式であることを認識*しません*



```maxima
(%i6) subst_parallel([x * y = a], x^2 * y);
                               2
(%o6)                         x  y
```


関数 `subst_parallel`は整理の*前に*すべての代入を完了します。
これは、もし整理が前に行われていたらエラーが起こるような
条件式への代入を許します:



```maxima
(%i7) subst_parallel([x = 0], %if(x < 1, 5, log(x)));
(%o7)                           5
(%i8) subst([x = 0], %if(x < 1, 5, log(x)));

log: encountered log(0).
 -- an error. To debug this try: debugmode(true);
```


**関連関数** *subst, sublis, ratsubst*


**利用するには** `load("to_poly_solve_extra.lisp")`


**状況** 関数 `subst_parallel`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: to_poly -->
<!-- signatures: to_poly(e, l) -->
### Function: to_poly (e, l)

関数 `to_poly`は
等式 `e`を
inequation制約を伴う多項式系に変換しようとします;
制約を満たす多項式系の解は
等式 `e`の解です。
非公式には `to_poly`は
等式 *e*を多項式化しようとします; 
例がわかりやすいかもしれません:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly(sqrt(x) = 3, [x]);
                            2
(%o2) [[%g130 - 3, x = %g130 ], 
                      %pi                               %pi
                   [- --- < parg(%g130), parg(%g130) <= ---], []]
                       2                                 2
```


条件 `-%pi/2<parg(%g6),parg(%g6)<=%pi/2`は
`%g6`が平方根関数の範囲内であることを告げます。
これがtrueの時、
`sqrt(x) = 3`に設定された解は
`%g6-3,x=%g6^2`に設定された解と同じです。


三角式を多項式化するには、
非代数的代入の導入が必要です;
これらの非代数的代入は
`to_poly`が返す三番目のリスト内で返されます;
例えば



```maxima
(%i3) to_poly(cos(x),[x]);
                2                                 %i x
(%o3)    [[%g131  + 1], [2 %g131 # 0], [%g131 = %e    ]]
```


数字1が変数リストのメンバーでない限り定数項は多項式化されません;
例えば



```maxima
(%i4) to_poly(x = sqrt(5),[x]);
(%o4)                [[x - sqrt(5)], [], []]
(%i5) to_poly(x = sqrt(5),[1,x]);
                            2
(%o5) [[x - %g132, 5 = %g132 ], 
                      %pi                               %pi
                   [- --- < parg(%g132), parg(%g132) <= ---], []]
                       2                                 2
```


根の1つとして$sqrt(5) + sqrt(7)$を持つ多項式を生成するには、
以下のコマンドを使います。



```maxima
(%i6) first(elim_allbut(first(to_poly(x = sqrt(5) + sqrt(7),
                                      [1,x])), [x]));
                          4       2
(%o6)                   [x  - 24 x  + 4]
```


**関連関数** *to_poly_solve*


**利用するには** `load("to_poly")`


**状況:** 関数 `to_poly`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

<!-- category: Solving -->
<!-- keywords: to_poly_solve -->
<!-- signatures: to_poly_solve(e, l, [options]) -->
### Function: to_poly_solve (e, l, [options])

関数 `to_poly_solve`は
等式 $e$を
変数 $l$について解こうとします。
等式 $e$は単一の式か式の集合もしくはリストでありえます;
同様に $l$は単一のシンボルかシンボルの集合のリストでありえます;
$e$のメンバーが明示的に等式でない時(例えば $x^2 -1$)、
ソルバは式は0に等しいと仮定します。


`to_poly_solve`の基本戦略は
入力を多項式形に変換するために `to_poly`を使い、
多項式系上で `algsys`をコールします。
なので Thus user options that affect 
`algsys`に影響を与えるユーザーオプション、特に
`algexact`は `to_poly_solve`にも影響を与えます。
`algexact`のデフォルト値はfalseですが、
`to_poly_solve`のためには、、一般的に `algexact`はtrueであるべきです。
関数 `to_poly_solve`は
`algexact`を局所的にtrueに設定しません。
`algsys`が厳密は解を決定することができない時
trueに設定すると近似解を見つけることが不可能になるためです。


`to_poly_solve`が解集合を決定できる時、
解集合のそれぞれのメンバーは
`%union`オブジェクト内のリストです:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly_solve(x*(x-1) = 0, x);
(%o2)               %union([x = 0], [x = 1])
```


`to_poly_solve`が解集合を決定*できない*時
`%solve`名詞形が返されます。(この場合、警告が印字されます。)



```maxima
(%i3) to_poly_solve(x^k + 2* x + 1 = 0, x);

Nonalgebraic argument given to 'to_poly'
unable to solve
                          k
(%o3)            %solve([x  + 2 x + 1 = 0], [x])
```


`%solve`名詞形への代入は時々解に帰着します。



```maxima
(%i4) subst(k = 2, %);
(%o4)                   %union([x = - 1])
```


特に三角等式の場合、
ソルバは時々任意整数の導入を必要とします。
これらの任意整数は
`%zXXX`という形を持ちます。
ここで `XXX`は整数です;
例えば



```maxima
(%i5) to_poly_solve(sin(x) = 0, x);
(%o5)   %union([x = 2 %pi %z33 + %pi], [x = 2 %pi %z35])
```


これらの変数を零から再インデックスするには `nicedummies`を使います:



```maxima
(%i6) nicedummies(%);
(%o6)    %union([x = 2 %pi %z0 + %pi], [x = 2 %pi %z1])
```


時折、ソルバは
`%cXXX`という形の任意複素数か
`%rXXX`という形の任意実数を導入します。
関数 `nicedummies`はこれらの識別子を零から再インデックスします。


解集合は時々
論理積、論理和、含意に関してそれぞれ
`%and`か, `%or`, `%if`を含む様々な論理演算子の
整理化バージョンを含みます;
例えば



```maxima
(%i7) sol : to_poly_solve(abs(x) = a, x);
(%o7) %union(%if(isnonnegative_p(a), [x = - a], %union()), 
                      %if(isnonnegative_p(a), [x = a], %union()))
(%i8) subst(a = 42, sol);
(%o8)             %union([x = - 42], [x = 42])
(%i9) subst(a = -42, sol);
(%o9)                       %union()
```


空集合は `%union`によって表現されます。


関数 `to_poly_solve`は
有理数や非有理べき、絶対値、三角関数、最小最大を含む等式の(すべてではありませんが)
いくつかを解くことができます。
Lambert W 函数を使って解くことができるいくつかの等式も解くことができます;
例:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly_solve(set(max(x,y) = 5, x+y = 2), set(x,y));
(%o2)      %union([x = - 3, y = 5], [x = 5, y = - 3])
(%i3) to_poly_solve(abs(1-abs(1-x)) = 10,x);
(%o3)             %union([x = - 10], [x = 12])
(%i4) to_poly_solve(set(sqrt(x) + sqrt(y) = 5, x + y = 10),
                    set(x,y));
                     3/2               3/2
                    5    %i - 10      5    %i + 10
(%o4) %union([x = - ------------, y = ------------], 
                         2                 2
                                3/2                 3/2
                               5    %i + 10        5    %i - 10
                          [x = ------------, y = - ------------])
                                    2                   2
(%i5) to_poly_solve(cos(x) * sin(x) = 1/2,x,
                    'simpfuncs = ['expand, 'nicedummies]);
                                         %pi
(%o5)              %union([x = %pi %z0 + ---])
                                          4
(%i6) to_poly_solve(x^(2*a) + x^a + 1,x);
                                        2 %i %pi %z81
                                        -------------
                                  1/a         a
                  (sqrt(3) %i - 1)    %e
(%o6) %union([x = -----------------------------------], 
                                  1/a
                                 2

                                                  2 %i %pi %z83
                                                  -------------
                                            1/a         a
                          (- sqrt(3) %i - 1)    %e
                     [x = -------------------------------------])
                                           1/a
                                          2

(%i7) to_poly_solve(x * exp(x) = a, x);
(%o7)              %union([x = lambert_w(a)])
```


*線形*不等式に対して、 `to_poly_solve`は自動的にFourier消去を行います:



```maxima
(%i8) to_poly_solve([x + y < 1, x - y >= 8], [x,y]);
                               7
(%o8) %union([x = y + 8, y < - -], 
                               2
                                                              7
                                 [y + 8 < x, x < 1 - y, y < - -])
                                                              2
```


`to_poly_solve`のオプション引数のそれぞれは等式でなければいけません;
一般にこれらのオプションの順序は問題になりません．



- *
`simpfuncs = l`, 
ここで `l`は函数のリストです。
lのメンバーの合成をそれぞれの解に適用します。



```maxima
(%i1) to_poly_solve(x^2=%i,x);
                               1/4             1/4
(%o1)       %union([x = - (- 1)   ], [x = (- 1)   ])
(%i2) to_poly_solve(x^2= %i,x, 'simpfuncs = ['rectform]);
                      %i         1             %i         1
(%o2) %union([x = - ------- - -------], [x = ------- + -------])
                    sqrt(2)   sqrt(2)        sqrt(2)   sqrt(2)
```



- *
時々追加の整理は整理を戻すことがあります;
例えば



```maxima
(%i3) to_poly_solve(x^2=1,x);
(%o3)              %union([x = - 1], [x = 1])
(%i4) to_poly_solve(x^2= 1,x, 'simpfuncs = [polarform]);
                                        %i %pi
(%o4)            %union([x = 1], [x = %e      ]
```



- *
Maximaは
関数リスト `l`のそれぞれのメンバーが純粋に整理であるかチェックしようとしません;
例えば



```maxima
(%i5) to_poly_solve(x^2 = %i,x, 'simpfuncs = [lambda([s],s^2)]);
(%o5)                   %union([x = %i])
```



- *
それぞれの解を倍精度浮動小数点数に変換するには
`simpfunc = ['dfloat]`を使います:



```maxima
(%i6) to_poly_solve(x^3 +x + 1 = 0,x, 
                    'simpfuncs = ['dfloat]), algexact : true;
(%o6) %union([x = - .6823278038280178], 
[x = .3411639019140089 - 1.161541399997251 %i], 
[x = 1.161541399997251 %i + .3411639019140089])
```



- *
`use_grobner = true`
このオプションを使うと
解を企てる前に関数 `poly_reduced_grobner`が
等式に適用されます
主として、このオプションは
関数 `algsys`の弱みに対する応急措置を提供します。
以下はそんな応急措置の例です:



```maxima
(%i7) to_poly_solve([x^2+y^2=2^2,(x-1)^2+(y-1)^2=2^2],[x,y],
                    'use_grobner = true);

                    sqrt(7) - 1      sqrt(7) + 1
(%o7) %union([x = - -----------, y = -----------], 
                         2                2

                                 sqrt(7) + 1        sqrt(7) - 1
                            [x = -----------, y = - -----------])
                                      2                  2
(%i8) to_poly_solve([x^2+y^2=2^2,(x-1)^2+(y-1)^2=2^2],[x,y]);
(%o8)                       %union()
```



- *
`maxdepth = k`,
ここで `k`は正の整数です。
この関数はソルバの最大再帰深さを制御します。
`maxdepth`のデフォルト値は5です。
再帰深さを越えた時、ソルバはエラーをシグナルします:



```maxima
(%i9) to_poly_solve(cos(x) = x,x, 'maxdepth = 2);

Unable to solve
Unable to solve
(%o9)        %solve([cos(x) = x], [x], maxdepth = 2)
```



- *
`parameters = l`,
ここで `l`はシンボルのリストです。
ソルバは
リスト `l`のメンバーすべてに有効な解を返そうとします;
例えば:



```maxima
(%i10) to_poly_solve(a * x = x, x);
(%o10)                   %union([x = 0])
(%i11) to_poly_solve(a * x = x, x, 'parameters = [a]);
(%o11) %union(%if(a - 1 = 0, [x = %c111], %union()), 
                               %if(a - 1 # 0, [x = 0], %union()))
```



- *
`(%o2)`で、ソルバはダミー変数を導入しました;
これらのダミー変数を再インデックスするには、
関数 `nicedummies`を使います:



```maxima
(%i12) nicedummies(%);
(%o12) %union(%if(a - 1 = 0, [x = %c0], %union()), 
                               %if(a - 1 # 0, [x = 0], %union()))
```


$f(a) = f(b)$という形の等式を解くために
`to_poly_solve`は
ハッシュ配列 `one_to_one_reduce`に記憶されたデータを使います。
割り当て `one_to_one_reduce['f,'f] : lambda([a,b], a=b)`は
`to_poly_solve`に
$f(a) = f(b)$の解集合が$a=b$の解集合に等しいことを告げます;
例えば



```maxima
(%i13) one_to_one_reduce['f,'f] : lambda([a,b], a=b)$

(%i14) to_poly_solve(f(x^2-1) = f(0),x);
(%o14)             %union([x = - 1], [x = 1])
```


さらに一般的に、
割り当て `one_to_one_reduce['f,'g] : lambda([a,b], w(a, b) = 0`は
`to_poly_solve`に
$f(a) = f(b)$の解集合が $w(a,b) = 0$の解集合に等しいことを告げます;
例えば



```maxima
(%i15) one_to_one_reduce['f,'g] : lambda([a,b], a = 1 + b/2)$

(%i16) to_poly_solve(f(x) - g(x),x);
(%o16)                   %union([x = 2])
```


加えて、$f(a) = b$という形の等式を解くために
関数 `to_poly_solve`は
ハッシュ配列 `function_inverse`に記憶されたデータを使います。
割り当て `function_inverse['f] : lambda([s], g(s))`は
`to_poly_solve`に
`f(x) = b`に設定された解が
`x = g(b)`に設定された解に等しいことを知らせます;
2つの例:



```maxima
(%i17) function_inverse['Q] : lambda([s], P(s))$

(%i18) to_poly_solve(Q(x-1) = 2009,x);
(%o18)              %union([x = P(2009) + 1])
(%i19) function_inverse['G] : lambda([s], s+new_variable(integer));
(%o19)       lambda([s], s + new_variable(integer))
(%i20) to_poly_solve(G(x - a) = b,x);
(%o20)             %union([x = b + a + %z125])
```



**注釈**



- *
解く変数はシンボルである必要はありません;
`fullratsubst`が適切に代入できる時、
解く変数は非シンボルであり得ます:



```maxima
(%i1) to_poly_solve([x^2 + y^2 + x * y = 5, x * y = 8],
                    [x^2 + y^2, x * y]);
                                  2    2
(%o1)           %union([x y = 8, y  + x  = - 3])
```



- *
複素共役を含む等式に対して、
ソルバは自動的に共役等式を追加します;
例えば



```maxima
(%i1) declare(x,complex)$

(%i2) to_poly_solve(x + (5 + %i) * conjugate(x) = 1, x);
                                   %i + 21
(%o2)              %union([x = - -----------])
                                 25 %i - 125
(%i3) declare(y,complex)$

(%i4) to_poly_solve(set(conjugate(x) - y = 42 + %i,
                        x + conjugate(y) = 0), set(x,y));
                           %i - 42        %i + 42
(%o4)        %union([x = - -------, y = - -------])
                              2              2
```



- *
絶対値関数を含む等式に対して、
`to_poly_solve`は
絶対値の引数が複素数値か決めるため
事実データベースに問い合わせます。



```maxima
(%i1) to_poly_solve(abs(x) = 6, x);
(%o1)              %union([x = - 6], [x = 6])
(%i2) declare(z,complex)$

(%i3) to_poly_solve(abs(z) = 6, z);
(%o3) %union(%if((%c11 # 0) %and (%c11 conjugate(%c11) - 36 = 
                                       0), [z = %c11], %union()))
```



- *
*これはソルバが事実データベースを参照する唯一の状況です。例えば、もし解く変数が整数と宣言されていたら、`to_poly_solve`はこの宣言を無視します*。


**Relevant option variables** *algexact, resultant, algebraic*


**関連関数** *to_poly*


**利用するには** `load("to_poly_solve")`


**状況:** 関数 `to_poly_solve`は実験的です;
仕様は変更の可能性があり、
機能は他のMaxima関数にマージされるかもしれません。

