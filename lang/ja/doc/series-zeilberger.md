## zeilberger

<!-- category: Series -->
<!-- keywords: AntiDifference -->
<!-- signatures: AntiDifference(F_k, k) -->
### Function: AntiDifference (F_k, k)

もし存在すれば、$F_k$の超幾何反差を返します。

そうでなければ、 `AntiDifference`は
`no_hyp_antidifference`を返します。

<!-- category: Series -->
<!-- keywords: ev_point -->
<!-- signatures: ev_point -->
### Variable: ev_point

デフォルト値: `big_primes[10]`


`parGosper`でモジュラーテストを実行する時
`ev_point`で変数 *n*が評価されます。

<!-- category: Series -->
<!-- keywords: Gosper -->
<!-- signatures: Gosper(F_k, k) -->
### Function: Gosper (F_k, k)

もし存在すれば、
$F_k$に対する有理証(rational certificate)、
すなわち、
以下のような有理函数を返します。

$$
$F_k = R\left(k+1\right) \, F_{k+1} - R\left(k\right) \, F_k$,
$$

$F_k = R(k+1) F_(k+1) - R(k) F_k$,
そうでなければ、 `Gosper`は `no_hyp_sol`を返します。

<!-- category: Series -->
<!-- keywords: Gosper_in_Zeilberger -->
<!-- signatures: Gosper_in_Zeilberger -->
### Variable: Gosper_in_Zeilberger

デフォルト値: `true`


`Gosper_in_Zeilberger`が `true`の時、
`Zeilberger`関数は
`parGosper`をコールする前に
`Gosper`をコールします。
そうでないなら、 `Zeilberger`はすぐに `parGosper`に向かいます。

<!-- category: Series -->
<!-- keywords: GosperSum -->
<!-- signatures: GosperSum(F_k, k, a, b) -->
### Function: GosperSum (F_k, k, a, b)

もし $F_k$が超幾何反差を持つなら、
$k = a$から $k = b$までの
$F_k$の和を返します。
そうでなければ、 `GosperSum`は `nongosper_summable`を返します。


例:













```maxima
(%i1) load ("zeilberger")$

(%i2) GosperSum ((-1)^k*k / (4*k^2 - 1), k, 1, n);
Dependent equations eliminated:  (1)
                           3       n + 1
                      (n + -) (- 1)
                           2               1
(%o2)               - ------------------ - -
                                  2        4
                      2 (4 (n + 1)  - 1)


(%i3) GosperSum (1 / (4*k^2 - 1), k, 1, n);
                                3
                          - n - -
                                2       1
(%o3)                  -------------- + -
                                2       2
                       4 (n + 1)  - 1


(%i4) GosperSum (x^k, k, 1, n);
                          n + 1
                         x          x
(%o4)                    ------ - -----
                         x - 1    x - 1


(%i5) GosperSum ((-1)^k*a! / (k!*(a - k)!), k, 1, n);
                                n + 1
                a! (n + 1) (- 1)              a!
(%o5)       - ------------------------- - ----------
              a (- n + a - 1)! (n + 1)!   a (a - 1)!


(%i6) GosperSum (k*k!, k, 1, n);
Dependent equations eliminated:  (1)
(%o6)                     (n + 1)! - 1


(%i7) GosperSum ((k + 1)*k! / (k + 1)!, k, 1, n);
                  (n + 1) (n + 2) (n + 1)!
(%o7)             ------------------------ - 1
                          (n + 2)!


(%i8) GosperSum (1 / ((a - k)!*k!), k, 1, n);
(%o8)                  NON_GOSPER_SUMMABLE
```

<!-- category: Series -->
<!-- keywords: linear_solver -->
<!-- signatures: linear_solver -->
### Variable: linear_solver

デフォルト値: `linsolve`


`linear_solver`は
Zeilbergerのアルゴリズムで方程式系を解くのに使うソルバを指定します。

<!-- category: Series -->
<!-- keywords: MAX_ORD -->
<!-- signatures: MAX_ORD -->
### Variable: MAX_ORD

デフォルト値: 5


`MAX_ORD`は
`Zeilberger`が試みる漸化式の最大次数です。

<!-- category: Series -->
<!-- keywords: mod_big_prime -->
<!-- signatures: mod_big_prime -->
### Variable: mod_big_prime

デフォルト値: `big_primes[1]`


`mod_big_prime`は
`parGosper`でモジュラーテストが使う法です。

<!-- category: Series -->
<!-- keywords: mod_test -->
<!-- signatures: mod_test -->
### Variable: mod_test

デフォルト値: `false`


`mod_test`が `true`の時、
`parGosper`は
解を持たない系を除くためにモジュラーテストを実行します。

<!-- category: Series -->
<!-- keywords: mod_threshold -->
<!-- signatures: mod_threshold -->
### Variable: mod_threshold

デフォルト値: 4


`mod_threshold`は
`parGosper`でのモジュラーテストが試みられる際の最大次数です。

<!-- category: Series -->
<!-- keywords: modular_linear_solver -->
<!-- signatures: modular_linear_solver -->
### Variable: modular_linear_solver

デフォルト値: `linsolve`


`modular_linear_solver`は
`parGosper`でのモジュラーテストが使う線形ソルバを指定します。

<!-- category: Series -->
<!-- keywords: parGosper -->
<!-- signatures: parGosper(F_(n,k), k, n, d) -->
### Function: parGosper (F_(n,k), k, n, d)

$F_(n,k)$に対して次数*d*の漸化式を見つけようとします。


アルゴリズムは解の列 $[s_1, s_2, ..., s_m]$をもたらします。
解それぞれは形式


$[R(n, k), [a_0, a_1, ..., a_d]].$


を持ちます。


もし漸化式を見つけられないなら、
`parGosper`は `[]`を返します。

<!-- category: Series -->
<!-- keywords: simplified_output -->
<!-- signatures: simplified_output -->
### Variable: simplified_output

デフォルト値: `false`


`simplified_output`が `true`の時、
`zeilberger`パッケージの関数は
解の更なる整理を試みます。

<!-- category: Series -->
<!-- keywords: trivial_solutions -->
<!-- signatures: trivial_solutions -->
### Variable: trivial_solutions

デフォルト値: `true`


`trivial_solutions`が `true`の時、
`Zeilberger`は
零に等しい証を持つ解か、
すべての係数が零に等しい解
を返します。

<!-- category: Series -->
<!-- keywords: warnings -->
<!-- signatures: warnings -->
### Variable: warnings

デフォルト値: `true`


`warnings`が `true`の時、
`zeilberger`パッケージの関数は
実行中に警告メッッセージを印字します。

<!-- category: Series -->
<!-- keywords: Zeilberger -->
<!-- signatures: Zeilberger(F_(n,k), k, n) -->
### Function: Zeilberger (F_(n,k), k, n)

$F_(n,k)$の超幾何不定総和を計算しようとします。


`Zeilberger`は最初に `Gosper`を呼び出し、
もしそれが解を見つけるのに失敗したら、
次数 1, 2, 3, ..., から `MAX_ORD`までを使って
`parGosper`を呼び出します。
もしZeilbergerが
`MAX_ORD`に達する前に
停止して、解を返します。


アルゴリズムは解の列 $[s_1, s_2, ..., s_m]$をもたらします。
解それぞれは形式


$[R(n,k), [a_0, a_1, ..., a_d]].$


を持ちます。


もし解を見つけられなかったら、
`Zeilberger`は `[]`を返します。


`Zeilberger`は
`Gosper_in_Zeilberger`が `true`の時だけ
`Gosper`を呼び出します。

