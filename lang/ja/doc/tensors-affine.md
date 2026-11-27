## Affine

<!-- category: Tensors -->
<!-- keywords: all_dotsimp_denoms -->
<!-- signatures: all_dotsimp_denoms -->
### Variable: all_dotsimp_denoms

デフォルト値: `false`


`all_dotsimp_denoms`がリストの時、
`dotsimp`が出会う分母がリストに追加されます。
`all_dotsimp_denoms`は、
`dotsimp`をコールする前に
空のリスト`[]`に初期化されるかもしれません。


デフォルトでは、`dotsimp`は分母を集めません。

<!-- category: Tensors -->
<!-- keywords: check_overlaps -->
<!-- signatures: check_overlaps(n, add_to_simps) -->
### Function: check_overlaps (n, add_to_simps)

次数*n*までの重複をチェックします。
すなわち、`dotsimp`が正しく機能するように、
それぞれの次数で十分な整理規則を持つことを確認します。
もしあらかじめ単項式の空間次元が何か知っているなら、
このプロセスは、スピードアップできます。
もし有限グローバル次元なら、
`hilbert`が使われるべきです。
もし単項式次元を知らないなら、
`rank_function`を指定しないでください。
オプションの三番目の引数`reset`は、
`false`は、物事の再設定についてわざわざ問い合わせないように言います。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: declare_weights -->
<!-- signatures: declare_weights(x_1, w_1, ..., x_n, w_n) -->
### Function: declare_weights (x_1, w_1, ..., x_n, w_n)

重み
*w_1*, ..., *w_n*
それぞれを*x_1*, ..., *x_n*に割り当てます。
これらは、`nc_degree`を計算する時に使われる重みです。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: dotsimp -->
<!-- signatures: dotsimp(f) -->
### Function: dotsimp (f)

*f*が方程式によって生成されたイデアルに含まれる時だけ、
すなわち、*f*が方程式の要素の多項式結合の時だけ、
0を返します。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: extract_linear_equations -->
<!-- signatures: extract_linear_equations([p_1, ..., p_n], [m_1, ..., m_n]) -->
### Function: extract_linear_equations ([p_1, ..., p_n], [m_1, ..., m_n])

非可換単項式*m_1*, ..., *m_n*の
非可換多項式*p_1*, ..., *p_n*
の係数のリストを作ります。
係数はスカラーでなければいけません。
単項式のリストを組み立てるには、`list_nc_monomials`を使ってください。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: fast_central_elements -->
<!-- signatures: fast_central_elements([x_1, ..., x_n], n) -->
### Function: fast_central_elements ([x_1, ..., x_n], n)

もし`set_up_dot_simplifications`が以前に実行されていたら、
与えられた次数*n*での変数*x_1*, ..., *x_n*に関する中心多項式
を見つけます。


例えば:


```maxima
set_up_dot_simplifications ([y.x + x.y], 3);
fast_central_elements ([x, y], 2);
[y.y, x.x];
```


`load("affine")` loads this function.

<!-- category: Tensors -->
<!-- keywords: fast_linsolve -->
<!-- signatures: fast_linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: fast_linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

変数*x_1*, ..., *x_n*に関する連立線形方程式*expr_1*, ..., *expr_m*
を解きます。
*expr_i*それぞれは、等式か一般式を取り得ます;
もし一般式として与えられたら、
形式`expr_i = 0`の等式として扱われます。


戻り値は、
形式`[x_1 = a_1, ..., x_n = a_n]`
の等式のリストです。
ここで、*a_1*, ..., *a_n*はすべて*x_1*, ..., *x_n*を含みません。


`fast_linsolve`は、
粗な方程式系に対して`linsolve`より速いです。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: grobner_basis -->
<!-- signatures: grobner_basis([expr_1, ..., expr_m]) -->
### Function: grobner_basis ([expr_1, ..., expr_m])

等式*expr_1*, ..., *expr_m*のグレブナー基底を返します。
等式に関係する他の関数を整理するためには、
その後、関数`polysimp`を使うことができます。



```maxima
grobner_basis ([3*x^2+1, y*x])$

polysimp (y^2*x + x^3*9 + 2) ==> -3*x + 2
```


`polysimp(f)`は、
*f*が*expr_1*, ..., *expr_m*によって生成されたイデアルに含まれるときだけ、
すなわち、*f*が*expr_1*, ..., *expr_m*の要素の多項式結合の時だけ、
0をもたらします。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: list_nc_monomials -->
<!-- signatures: list_nc_monomials([p_1, ..., p_n]), list_nc_monomials(p) -->
### Function: list_nc_monomials ([p_1, ..., p_n])

多項式*p*または多項式のリスト*p_1*, ..., *p_n*
の中に現れる非可換単項式のリストを返します。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: mono -->
<!-- signatures: mono([x_1, ..., x_n], n) -->
### Function: mono ([x_1, ..., x_n], n)

次数*n*の変数*x_1*, ..., *x_n*に関する現在のドット整理に関係した
独立な単項式のリストを返します。


`load("affine")` loads this function.

<!-- category: Tensors -->
<!-- keywords: monomial_dimensions -->
<!-- signatures: monomial_dimensions(n) -->
### Function: monomial_dimensions (n)

カレント代数に関する次数*n*までのヒルベルト級数を計算します。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: nc_degree -->
<!-- signatures: nc_degree(p) -->
### Function: nc_degree (p)

非可換多項式*p*の次数を返します。
`declare_weights`を参照してください。


`load("affine")`はこの関数をロードします。

<!-- category: Tensors -->
<!-- keywords: set_up_dot_simplifications -->
<!-- signatures: set_up_dot_simplifications(eqns, check_through_degree), set_up_dot_simplifications(eqns) -->
### Function: set_up_dot_simplifications (eqns, check_through_degree)

The *eqns*は、非可換変数を含む多項式方程式です
`current_variables`の値は、次数を計算するために使われる変数のリストです。
手続きが終了するためには、方程式は斉次でなければいけません。


もし
*f*の次数上の`dot_simplifications`に関する重複整理をチェックしたら、
以下は真です:
*f*が方程式によって生成されたイデアルに含まれる時だけ、
すなわち、*f*が方程式の要素の多項式結合の時だけ、
`dotsimp (f)`は、0をもたらします。


次数は`nc_degree`で返されるものです。
これは、さらに、個々の変数の重みに影響されます。


`load("affine")`はこの関数をロードします。

