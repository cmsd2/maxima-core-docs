## simplex

<!-- category: Numerical -->
<!-- keywords: epsilon_lp -->
<!-- signatures: epsilon_lp -->
### Variable: epsilon_lp

デフォルト値: `10^-8`


`linear_program`の数値計算で使われるイプシロン。


以下も参照してください: `linear_program`

<!-- category: Numerical -->
<!-- keywords: linear_program -->
<!-- signatures: linear_program(A, b, c) -->
### Function: linear_program (A, b, c)

`linear_program`は
シンプレックスアルゴリズムの実装です。
`linear_program(A, b, c)`は、
`A.x = b`かつ`x >= 0`を満たすベクトルの中で`c.x`が可能な最小となる
ベクトル*x*を計算します。
引数*A*は行列で、引数*b*と*c*はリストです。


`linear_program`は、
最小化ベクトル*x*と最小値`c.x`を含む
リストを返します。
もし問題が有界でないなら、
"Problem not bounded!"を返し、
もし問題が実現可能でないなら、
"Problem not feasible!"を返します。


この関数を使うためには、最初に`load("simplex");`で`simplex`パッケージをロードしてください。


例:









```maxima
(%i2) A: matrix([1,1,-1,0], [2,-3,0,-1], [4,-5,0,0])$
(%i3) b: [1,1,6]$
(%i4) c: [1,-2,0,0]$
(%i5) linear_program(A, b, c);
                   13     19        3
(%o5)            [[--, 4, --, 0], - -]
                   2      2         2
```


以下も参照してください: `minimize_lp`, `scale_lp`, `epsilon_lp`

<!-- category: Numerical -->
<!-- keywords: maximize_lp -->
<!-- signatures: maximize_lp(obj, cond, [pos]) -->
### Function: maximize_lp (obj, cond, [pos])

いくつかの線形制約*cond*に従う線形目標関数*obj*を最大化します。
引数と戻り値の詳細な記述に関しては、
`minimize_lp`を参照してください。



以下も参照してください: `minimize_lp`.

<!-- category: Numerical -->
<!-- keywords: minimize_lp -->
<!-- signatures: minimize_lp(obj, cond, [pos]) -->
### Function: minimize_lp (obj, cond, [pos])

いくつかの線形制約*cond*に従う線形目標関数*obj*を最小化します。
*cond*は線形等式や不等式のリストです。
厳密な不等式では、`>`は`>=`に、
`<`は`<=`に置き換えられます。
オプションの引数*pos*は
正と仮定される決定変数のリストです。


もし最小が存在するなら、
`minimize_lp`は
目標関数の最小値と最小が得られる決定変数値のリスト
を含むリストです。
もし問題が有界でないなら、
`minimize_lp`は"Problem not bounded!"を返し、
もし問題が実現可能でないなら、
"Ploblem not feasible!"を返します。


決定変数はデフォルトでは非負とは仮定されません。
もし決定変数すべてが正なら、
`nonegative_lp`を`true`に設定してください。
もし決定変数のいくつかだけが正なら、
オプション引数*pos*の中でそれらをリストしてください。
 (これは制約を足すより効率的だということに注意してください。)


`minimize_lp`は
Maximaの`linear_program`関数で実装された
シンプレックスアルゴリズムを使います。


この関数を使うためには、最初に`load("simplex");`で
`simplex`パッケージをロードしてください。


例:









```maxima
(%i1) minimize_lp(x+y, [3*x+y=0, x+2*y>2]);
                      4       6        2
(%o1)                [-, [y = -, x = - -]]
                      5       5        5
(%i2) minimize_lp(x+y, [3*x+y>0, x+2*y>2]), nonegative_lp=true;
(%o2)                [1, [y = 1, x = 0]]
(%i3) minimize_lp(x+y, [3*x+y=0, x+2*y>2]), nonegative_lp=true;
(%o3)                Problem not feasible!
(%i4) minimize_lp(x+y, [3*x+y>0]);
(%o4)                Problem not bounded!
```



いかも参照してください: `maximize_lp`, `nonegative_lp`, `epsilon_lp`。

<!-- category: Numerical -->
<!-- keywords: nonegative_lp -->
<!-- signatures: nonegative_lp -->
### Variable: nonegative_lp

デフォルト値: `false`


もし`nonegative_lp`がtrueなら、
`minimize_lp`と`maximize_lp`の決定変数すべては正と仮定されます。


以下も参照してください: `minimize_lp`。

