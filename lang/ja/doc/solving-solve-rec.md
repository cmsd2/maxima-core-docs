## solve_rec

<!-- category: Solving -->
<!-- keywords: product_use_gamma -->
<!-- signatures: product_use_gamma -->
### Variable: product_use_gamma

デフォルト値: `true`


積を整理する時、
もし`product_use_gamma`が`true`なら、
`solve_rec`は式の中にガンマ函数を導入します。



以下も参照してください: `simplify_products`, `solve_rec`.

<!-- category: Solving -->
<!-- keywords: reduce_order -->
<!-- signatures: reduce_order(rec, sol, var) -->
### Function: reduce_order (rec, sol, var)

特殊解*sol*が知られている時、
線形漸化式*rec*の次数を減らします。


例:



```maxima
(%i3) rec: x[n+2] = x[n+1] + x[n]/n;
                                      x
                                       n
(%o3)               x      = x      + --
                     n + 2    n + 1   n


(%i4) solve_rec(rec, x[n]);
WARNING: found some hypergeometrical solutions! 
(%o4)                    x  = %k  n
                          n     1


(%i5) reduce_order(rec, n, x[n]);
(%t5)                    x  = n %z
                          n       n

                           n - 1
                           ====
                           \
(%t6)                %z  =  >     %u
                       n   /        %j
                           ====
                           %j = 0

(%o6)             (- n - 2) %u     - %u
                              n + 1     n


(%i6) solve_rec((n+2)*%u[n+1] + %u[n], %u[n]);
                                     n
                            %k  (- 1)
                              1
(%o6)                 %u  = ----------
                        n    (n + 1)!

だから一般解は以下の通りです。

             n - 1
             ====        j
             \      (- 1)
       %k  n  >    -------- + %k  n
         2   /     (j + 1)!     1
             ====
             j = 0
```

<!-- category: Solving -->
<!-- keywords: simplify_products -->
<!-- signatures: simplify_products -->
### Variable: simplify_products

デフォルト値: `true`


もし`simplify_products`が`true`なら、
`solve_rec`は答えの積をを整理しようとします。


以下も参照してください: `solve_rec`.

<!-- category: Solving -->
<!-- keywords: simplify_sum -->
<!-- signatures: simplify_sum(expr) -->
### Function: simplify_sum (expr)

*expr*に現れるすべての和を閉形式に整理しようとします。


この関数を初めて使うには、
`load("simplify_sum")`で
`simplify_sum`パッケージをロードしてください。


例:








```maxima
(%i1) load("simplify_sum")$

(%i2) sum(binomial(n+k,k)/2^k,k,1,n)+sum(binomial(2*n,2*k),k,1,n);
        n                          n
       ====                       ====
       ¥     binomial(n + k, k)   ¥
(%o2)   >    ------------------ +  >    binomial(2 n, 2 k)
       /              k           /
       ====          2            ====
       k = 1                      k = 1


(%i3) simplify_sum(%);

                         2 n - 1    n
(%o3)                   2        + 2  - 2
```

<!-- category: Solving -->
<!-- keywords: solve_rec -->
<!-- signatures: solve_rec(eqn, var, [init]) -->
### Function: solve_rec (eqn, var, [init])

変数*var*に関して多項式係数を持つ線形漸化式*eqn*の超幾何解について解きます。
オプション引数*init*は初期条件です。


`solve_rec`は、
定数係数の線形漸化式を解くことができ、
多項式係数の斉次線形漸化式の超幾何解と多項式係数の有理解を見つけ、
Ricatti型漸化式を解くことができます。


超幾何解を見つけるのに使われるアルゴリズムの実行時間は
主係数と最小次数(trailing)係数の次数に関して指数的であることに注意してください。


この関数を使うには、
最初に
`load("solve_rec");`で`solve_rec`パッケージをロードしてください。



定係数の線形漸化式の例:



```maxima
(%i2) solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n]);
                        n          n
           (sqrt(5) - 1)  %k  (- 1)
                            1           n
(%o2) a  = ------------------------- - ----
       n               n                  n
                      2                5 2
                                                n
                                   (sqrt(5) + 1)  %k
                                                    2    2
                                 + ------------------ - ----
                                            n              n
                                           2            5 2
```


多項式係数の線形漸化式の例:



```maxima
(%i7) 2*x*(x+1)*y[x] - (x^2+3*x-2)*y[x+1] + (x-1)*y[x+2];
                         2
(%o7) (x - 1) y      - (x  + 3 x - 2) y      + 2 x (x + 1) y
               x + 2                   x + 1                x


(%i8) solve_rec(%, y[x], y[1]=1, y[3]=3);
                              x
                           3 2    x!
(%o9)                 y  = ---- - --
                       x    4     2
```


Ricatti型漸化式の例:



```maxima
(%i2) x*y[x+1]*y[x] - y[x+1]/(x+2) + y[x]/(x-1) = 0;
                            y         y
                             x + 1     x
(%o2)         x y  y      - ------ + ----- = 0
                 x  x + 1   x + 2    x - 1

(%i3) solve_rec(%, y[x], y[3]=5)$

(%i4) ratsimp(minfactorial(factcomb(%)));
                                   3
                               30 x  - 30 x
(%o4) y  = - -------------------------------------------------
       x        6      5       4       3       2
             5 x  - 3 x  - 25 x  + 15 x  + 20 x  - 12 x - 1584
```



以下も参照してください: `solve_rec_rat`, `simplify_products`, and `product_use_gamma`.

<!-- category: Solving -->
<!-- keywords: solve_rec_rat -->
<!-- signatures: solve_rec_rat(eqn, var, [init]) -->
### Function: solve_rec_rat (eqn, var, [init])

線形漸化式の有理解について解きます。
引数の記述についてはsolve_recを参照してください。


この関数を使うには、
最初に
`load("solve_rec");`で`solve_rec`パッケージをロードしてください。


例:



```maxima
(%i1) (x+4)*a[x+3] + (x+3)*a[x+2] - x*a[x+1] + (x^2-1)*a[x];
(%o1)  (x + 4) a      + (x + 3) a      - x a
                x + 3            x + 2      x + 1
                                                   2
                                               + (x  - 1) a
                                                            x


(%i2) solve_rec_rat(% = (x+2)/(x+1), a[x]);
                       1
(%o2)      a  = ---------------
            x   (x - 1) (x + 1)
```



以下も参照してください: `solve_rec`.

<!-- category: Solving -->
<!-- keywords: summand_to_rec -->
<!-- signatures: summand_to_rec(summand, k, n), summand_to_rec(summand, [k, lo, hi], n) -->
### Function: summand_to_rec (summand, k, n)

和



```maxima
hi
    ====
    \
     >     summand
    /
    ====
  k = lo
```


が満たす漸化式を返します。
ここで、被和(summand)は*k*と*n*に対して超幾何的です。
もし*lo*と*hi*が省略されたら、
それらは`lo = -inf`、`hi = inf`と仮定されます。


この関数を初めて使うには、
`load("simplify_sum")`で
`simplify_sum`パッケージをロードしてください。


例:



```maxima
(%i1) load("simplify_sum")$

(%i2) summand: binom(n,k);
(%o2)                           binomial(n, k)


(%i3) summand_to_rec(summand,k,n);
(%o3)                      2 sm  - sm      = 0
                               n     n + 1


(%i7) summand: binom(n, k)/(k+1);
                                binomial(n, k)
(%o7)                           --------------
                                    k + 1


(%i8) summand_to_rec(summand, [k, 0, n], n);
(%o8)               2 (n + 1) sm  - (n + 2) sm      = - 1
                                n             n + 1
```

