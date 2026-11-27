## grobner

<!-- category: Polynomials -->
<!-- keywords: poly_add -->
<!-- signatures: poly_add(poly1, poly2, varlist) -->
### Function: poly_add (poly1, poly2, varlist)

2つの多項式 *poly1*と *poly2*を足します。


```maxima
(%i1) poly_add(z+x^2*y,x-z,[x,y,z]);
                                    2
(%o1)                              x  y + x
```

<!-- category: Polynomials -->
<!-- keywords: poly_buchberger -->
<!-- signatures: poly_buchberger(polylist_flvarlist) -->
### Function: poly_buchberger (polylist_flvarlist)

`poly_buchberger`は
多項式のリスト上でBuchbergerアルゴリズムを実行し、
結果の Groebner基底を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_buchberger_criterion -->
<!-- signatures: poly_buchberger_criterion(polylist, varlist) -->
### Function: poly_buchberger_criterion (polylist, varlist)

Buchberger判定(criterion)を使って
もし *polylist*が現在の項順序に関して Groebner基底なら
`true`を返します:
Buchberger判定(criterion)は、
*polylist*の2つの多項式 $h1$と $h2$すべてに関して、
S多項式 $S(h1,h2)$が *polylist*を$法$として0に簡約されるというものです。

<!-- category: Polynomials -->
<!-- keywords: poly_coefficient_ring -->
<!-- signatures: poly_coefficient_ring -->
### Variable: poly_coefficient_ring

デフォルト値: `expression_ring`


このスイッチは
grober計算で使われる多項式の係数環を示します。
もし設定されないなら、
*maximaの* 一般式環が使われます。
もし望むなら、この変数を `ring_of_integers`に設定できます。

<!-- category: Polynomials -->
<!-- keywords: poly_colon_ideal -->
<!-- signatures: poly_colon_ideal(polylist1, polylist2, varlist) -->
### Function: poly_colon_ideal (polylist1, polylist2, varlist)

コロンイデアル


$I(polylist1):I(polylist2)$


の簡約Groebner基底を返します。



ここで、 $polylist1$と $polylist2$は2つの多項式リストです。

<!-- category: Polynomials -->
<!-- keywords: poly_content -->
<!-- signatures: poly_content(poly.varlist) -->
### Function: poly_content (poly.varlist)

`poly_content`は係数のGCDを抽出します。


```maxima
(%i1) poly_content(35*y+21*x,[x,y]);
(%o1)                                  7
```

<!-- category: Polynomials -->
<!-- keywords: poly_depends_p -->
<!-- signatures: poly_depends_p(poly, var, varlist) -->
### Function: poly_depends_p (poly, var, varlist)

`poly_depends`は多項式が変数 *var*に依存するかテストします。

<!-- category: Polynomials -->
<!-- keywords: poly_elimination_ideal -->
<!-- signatures: poly_elimination_ideal(polylist, number, varlist) -->
### Function: poly_elimination_ideal (polylist, number, varlist)

`poly_elimination_ideal`は、
(必ずしもGroebner基底である必要はない)生成多項式のリストとして指定されたイデアルの
$number$番目の消去イデアルの
Groebner基底を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_elimination_order -->
<!-- signatures: poly_elimination_order -->
### Variable: poly_elimination_order

デフォルト値: `false`


消去計算で使われるデフォルト消去順序名。
設定されているなら、
変数 `poly_primary_elimination_order`と
`poly_secondary_elimination_order`の設定を上書きします。
ユーザーは
これが消去変数の数に有効な真の消去順序であることを保証しなければいけません。

<!-- category: Polynomials -->
<!-- keywords: poly_exact_divide -->
<!-- signatures: poly_exact_divide(poly1, poly2, varlist) -->
### Function: poly_exact_divide (poly1, poly2, varlist)

多項式 *poly1*を多項式 *poly2*で割ります。
余りのない厳密な割り算が可能と仮定します。
商を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_expand -->
<!-- signatures: poly_expand(poly, varlist) -->
### Function: poly_expand (poly, varlist)

この関数は
多項式を内部形式にパースします。
もし *poly*が多項式を正確にパースしたら、
それは `expand(poly)`と同値です。
もし表現が変数 *varlist*の多項式と互換性がないなら、
結果はエラーです。
式が正確に内部表現にパースするかテストするのに使うことができます。
以下の例は添字付き変数と超越関数変数が許されることを例示します。


```maxima
(%i1) poly_expand((x-y)*(y+x),[x,y]);
                                     2    2
(%o1)                               x  - y
(%i2) poly_expand((y+x)^2,[x,y]);
                                2            2
(%o2)                          y  + 2 x y + x
(%i3) poly_expand((y+x)^5,[x,y]);
                  5      4         2  3       3  2      4      5
(%o3)            y  + 5 x y  + 10 x  y  + 10 x  y  + 5 x  y + x
(%i4) poly_expand(-1-x*exp(y)+x^2/sqrt(y),[x]);
                                          2
                                  y      x
(%o4)                       - x %e  + ------- - 1
                                       sqrt(y)

(%i5) poly_expand(-1-sin(x)^2+sin(x),[sin(x)]);
                                2
(%o5)                      - sin (x) + sin(x) - 1
```

<!-- category: Polynomials -->
<!-- keywords: poly_expt -->
<!-- signatures: poly_expt(poly, number, varlist) -->
### Function: poly_expt (poly, number, varlist)

*poly*の、正の整数 *number*のべき乗を返します。
もし *number*が正の整数でないなら、
エラーが生じます。


```maxima
(%i1) poly_expt(x-y,3,[x,y])-(x-y)^3,expand;
(%o1)                                  0
```

<!-- category: Polynomials -->
<!-- keywords: poly_gcd -->
<!-- signatures: poly_gcd(poly1, poly2, varlist) -->
### Function: poly_gcd (poly1, poly2, varlist)

*poly1*と *poly2*の最大公約数(式)を返します。


`ezgcd`, `gcd`, `gcdex`, `gcdivide`
も参照してください。


例:



```maxima
(%i1) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i3) poly_gcd(p1, p2, [x]);
                            2
(%o3)                    6 x  + 13 x + 6
```

See also: `ezgcd`, `gcd`, `gcdex`, `gcdivide`.

<!-- category: Polynomials -->
<!-- keywords: poly_grobner -->
<!-- signatures: poly_grobner(polylist, varlist) -->
### Function: poly_grobner (polylist, varlist)

多項式リスト *polylist*で張られたイデアルのGroebner基底を返します。
グローバルフラグで影響を受けます。

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_algorithm -->
<!-- signatures: poly_grobner_algorithm -->
### Variable: poly_grobner_algorithm

デフォルト値: `buchberger`


可能な値: 


- * 
`buchberger`
- * 
`parallel_buchberger`
- * 
`gebauer_moeller`


Groebner基底を見つけるのに使われるアルゴリズム名。

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_debug -->
<!-- signatures: poly_grobner_debug -->
### Variable: poly_grobner_debug

デフォルト値: `false`


もし `true`に設定されているなら、
デバッグ用、トレース用出力を生成します。

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_equal -->
<!-- signatures: poly_grobner_equal(polylist1, polylist2, varlist) -->
### Function: poly_grobner_equal (polylist1, polylist2, varlist)

`poly_grobner_equal`は
2つの Groebner基底が同じイデアルを生成するか
テストします。
もし、Groebner基底と仮定された2つの多項式リスト *polylist1*と *polylist2*が
同じイデアルを生成するなら、`true`を返します。
そうでないなら、 `false`を返します。
これは、
一番目の基底のすべての多項式が二番目の基底を法として0に簡約されるかとその逆をチェックする
ことと同値です。
以下の例では、一番目のリストがGroebner基底でないので
結果が `false`であることに注意してください。



```maxima
(%i1) poly_grobner_equal([y+x,x-y],[x,y],[x,y]);
(%o1)                         false
```

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_member -->
<!-- signatures: poly_grobner_member(poly, polylist, varlist) -->
### Function: poly_grobner_member (poly, polylist, varlist)

もし多項式 *poly*が
Groebner基底であると仮定された多項式リスト *polylist*が生成するイデアルに属するなら、
`true`を返します。
そうでないなら、 `false`を返します。


`poly_grobner_member`は
多項式が
Groebner基底であると仮定された多項式のリストが生成するイデアルに属するかテストします。
`normal_form`が0と同値です。

<!-- category: Polynomials -->
<!-- keywords: poly_grobner_subsetp -->
<!-- signatures: poly_grobner_subsetp(polylist1, polylist2, varlist) -->
### Function: poly_grobner_subsetp (polylist1, polylist2, varlist)

`poly_grobner_subsetp`は
*polylist1*が生成するイデアルが
*polylist2*が生成するイデアルに含まれるかテストします。
このテストが常に成功するには、*polylist2*が Groebner基底でなければいけません。

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_intersection -->
<!-- signatures: poly_ideal_intersection(polylist1, polylist2, varlist) -->
### Function: poly_ideal_intersection (polylist1, polylist2, varlist)

`poly_ideal_intersection`は2つのイデアルの交わりです。

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_polysaturation -->
<!-- signatures: poly_ideal_polysaturation(polylist, polylistlist, varlist) -->
### Function: poly_ideal_polysaturation (polylist, polylistlist, varlist)

*polylistlist*は多項式リストn個のリスト `[polylist1,...,polylistn]`です。
イデアル


I(polylist):I(polylist_1)^inf:...:I(polylist_n)^inf
のsaturationの簡約 Groebner基底を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_polysaturation1 -->
<!-- signatures: poly_ideal_polysaturation1(polylist1, polylist2, varlist) -->
### Function: poly_ideal_polysaturation1 (polylist1, polylist2, varlist)

*polylist2*は2個の多項式のリスト `[poly1,...,polyn]`です。
多項式リスト *polylist1*が生成するイデアルの
多項式リスト *polylist2*の多項式に関する連続saturationの列によって得られるイデアル


I(polylist):poly1^inf:...:polyn^inf



の簡約 Groebner基底を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_saturation -->
<!-- signatures: poly_ideal_saturation(polylist1, polylist2, varlist) -->
### Function: poly_ideal_saturation (polylist1, polylist2, varlist)

イデアル


I(polylist1):I(polylist2)^inf
のsaturationの簡約 Groebner基底を返します。



幾何学的に、代数的閉体上で、
これは
*polylist2*の多様体上で恒等的に0とならない
*polylist1*が生成するイデアルの中の
多項式の集合です。

<!-- category: Polynomials -->
<!-- keywords: poly_ideal_saturation1 -->
<!-- signatures: poly_ideal_saturation1(polylist, poly, varlist) -->
### Function: poly_ideal_saturation1 (polylist, poly, varlist)

イデアル


I(polylist):poly^inf
のsaturationの簡約 Groebner基底を返します。




幾何学的に、代数的閉体上で、
これは
*poly*の多様体上で恒等的に0とならない
*polylist*が生成するイデアルの中の
多項式の集合です。

<!-- category: Polynomials -->
<!-- keywords: poly_lcm -->
<!-- signatures: poly_lcm(poly1, poly2, varlist) -->
### Function: poly_lcm (poly1, poly2, varlist)

*poly1*と *poly2*の最小公倍数(式)を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_minimization -->
<!-- signatures: poly_minimization(polylist, varlist) -->
### Function: poly_minimization (polylist, varlist)

*polylist*と同じ単項式イデアルの最小全域である、
多項式リスト *polylist*の部分リストを返します。
すなわち、部分リストの中の多項式の主単項式はすべて、他の多項式の主単項式を割りません。

<!-- category: Polynomials -->
<!-- keywords: poly_monomial_order -->
<!-- signatures: poly_monomial_order -->
### Variable: poly_monomial_order

デフォルト値: `lex`


このグローバルスイッチは
どの単項式順序が多項式とGroebner基底計算で使われるか制御します。
もし設定されないなら、 `lex`が使われます。

<!-- category: Polynomials -->
<!-- keywords: poly_multiply -->
<!-- signatures: poly_multiply(poly1, poly2, varlist) -->
### Function: poly_multiply (poly1, poly2, varlist)

多項式 *poly1*と *poly2*の積を返します。


```maxima
(%i2) poly_multiply(z+x^2*y,x-z,[x,y,z])-(z+x^2*y)*(x-z),expand;
(%o1)                                  0
```

<!-- category: Polynomials -->
<!-- keywords: poly_normal_form -->
<!-- signatures: poly_normal_form(poly, polylist, varlist) -->
### Function: poly_normal_form (poly, polylist, varlist)

`poly_normal_form`は
多項式の集合 *polylist*に関して
多項式 *poly*の正規形を見つけます。

<!-- category: Polynomials -->
<!-- keywords: poly_normalize -->
<!-- signatures: poly_normalize(poly, varlist) -->
### Function: poly_normalize (poly, varlist)

多項式 *poly1*を主係数で割ったものを返します。
割り算が可能であることを仮定しています。
これは、体の場合には大丈夫ですが、環の場合にはいつも可能なわけではありません。

<!-- category: Polynomials -->
<!-- keywords: poly_normalize_list -->
<!-- signatures: poly_normalize_list(polylist, varlist) -->
### Function: poly_normalize_list (polylist, varlist)

`poly_normalize_list`は
`poly_normalize`をリストの中の多項式それぞれに適用します。
これは
リスト *polylist*の中のすべての多項式を主係数で割ることを意味します。

<!-- category: Polynomials -->
<!-- keywords: poly_polysaturation_extension -->
<!-- signatures: poly_polysaturation_extension(poly, polylist, varlist1, varlist2) -->
### Function: poly_polysaturation_extension (poly, polylist, varlist1, varlist2)

<!-- category: Polynomials -->
<!-- keywords: poly_primary_elimination_order -->
<!-- signatures: poly_primary_elimination_order -->
### Variable: poly_primary_elimination_order

デフォルト値: `false`


消去ベース関数で消去される変数のデフォルト順序名。
設定されていないなら、 `lex`が使われます。

<!-- category: Polynomials -->
<!-- keywords: poly_primitive_part -->
<!-- signatures: poly_primitive_part(poly1, varlist) -->
### Function: poly_primitive_part (poly1, varlist)

多項式 *poly1*を係数のGCDで割ったものを返します。



```maxima
(%i1) poly_primitive_part(35*y+21*x,[x,y]);
(%o1)                              5 y + 3 x
```

<!-- category: Polynomials -->
<!-- keywords: poly_pseudo_divide -->
<!-- signatures: poly_pseudo_divide(poly, polylist, varlist) -->
### Function: poly_pseudo_divide (poly, polylist, varlist)

多項式 *poly*を
$n$個の多項式のリスト *polylist*で擬似的に割ります。
複数の値を返します。
一番目の値は
商のリスト $a$です。
二番目の値は余り $r$です。
三番目の値は、
係数環(体である必要はありません)内で*polylist*が$c*poly$を割れるような
スカラ係数 $c$です。
最後に
四番目の値は実行された簡約の回数です。
結果のオブジェクトは以下の等式を満たします:


$c*poly=sum(a[i]*polylist[i],i=1...n)+r$.

<!-- category: Polynomials -->
<!-- keywords: poly_reduced_grobner -->
<!-- signatures: poly_reduced_grobner(polylist, varlist) -->
### Function: poly_reduced_grobner (polylist, varlist)

多項式リスト *polylist*で張られたイデアルの簡約Groebner基底を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_reduction -->
<!-- signatures: poly_reduction(polylist, varlist) -->
### Function: poly_reduction (polylist, varlist)

`poly_reduction`は多項式のリスト *polylist*を簡約します。
それぞれの多項式は他の多項式で完全に簡約されます。

<!-- category: Polynomials -->
<!-- keywords: poly_return_term_list -->
<!-- signatures: poly_return_term_list -->
### Variable: poly_return_term_list

デフォルト値: `false`


もし `true`に設定されているなら、
このパッケージの関数すべては
*maxima*一般式ではなく、
それぞれの多項式を
現在の単項式順序で並べた項のリストとして返します。

<!-- category: Polynomials -->
<!-- keywords: poly_s_polynomial -->
<!-- signatures: poly_s_polynomial(poly1, poly2, varlist) -->
### Function: poly_s_polynomial (poly1, poly2, varlist)

2つの多項式 *poly1*と *poly2*の
*シジジー多項式* (*S多項式*)を返します。

<!-- category: Polynomials -->
<!-- keywords: poly_saturation_extension -->
<!-- signatures: poly_saturation_extension(poly, polylist, varlist1, varlist2) -->
### Function: poly_saturation_extension (poly, polylist, varlist1, varlist2)

`poly_saturation_extension`は有名な Rabinowitzのトリックを実装します。

<!-- category: Polynomials -->
<!-- keywords: poly_secondary_elimination_order -->
<!-- signatures: poly_secondary_elimination_order -->
### Variable: poly_secondary_elimination_order

デフォルト値: `false`


消去ベース関数で保持される変数のデフォルト順序名。
設定されていないなら、 `lex`が使われます。

<!-- category: Polynomials -->
<!-- keywords: poly_subtract -->
<!-- signatures: poly_subtract(poly1, poly2, varlist) -->
### Function: poly_subtract (poly1, poly2, varlist)

多項式 *poly1*から *poly2*を引きます。


```maxima
(%i1) poly_subtract(z+x^2*y,x-z,[x,y,z]);
                                      2
(%o1)                          2 z + x  y - x
```

<!-- category: Polynomials -->
<!-- keywords: poly_top_reduction_only -->
<!-- signatures: poly_top_reduction_only -->
### Variable: poly_top_reduction_only

デフォルト値: `false`


もし `false`でないなら、
可能な時はいつでも、頭項簡約を使います。
頭項簡約は、割り算アルゴリズムが最初の簡約後に停止することを意味します。

