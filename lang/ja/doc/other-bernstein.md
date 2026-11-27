## Bernstein

<!-- category: Other -->
<!-- keywords: bernstein_approx -->
<!-- signatures: bernstein_approx(f, [x1, x1, ..., xn], n) -->
### Function: bernstein_approx (f, [x1, x1, ..., xn], n)

関数 `(x1, x2, ..., xn) |--> f`の
 `n`次の一様Bernstein多項式近似を返します。


例



```maxima
(%i1) bernstein_approx(f(x),[x], 2);
                 2       1                          2
(%o1)      f(1) x  + 2 f(-) (1 - x) x + f(0) (1 - x)
                         2
(%i2) bernstein_approx(f(x,y),[x,y], 2);
               2  2       1                2
(%o2) f(1, 1) x  y  + 2 f(-, 1) (1 - x) x y
                          2
                  2  2          1   2
 + f(0, 1) (1 - x)  y  + 2 f(1, -) x  (1 - y) y
                                2
       1  1                               1         2
 + 4 f(-, -) (1 - x) x (1 - y) y + 2 f(0, -) (1 - x)  (1 - y) y
       2  2                               2
            2        2       1                      2
 + f(1, 0) x  (1 - y)  + 2 f(-, 0) (1 - x) x (1 - y)
                             2
                  2        2
 + f(0, 0) (1 - x)  (1 - y)
```


`bernstein_approx`を使うには、最初に `load("bernstein")`。

<!-- category: Other -->
<!-- keywords: bernstein_expand -->
<!-- signatures: bernstein_expand(e, [x1, x1, ..., xn]) -->
### Function: bernstein_expand (e, [x1, x1, ..., xn])

*多項式* `e`を
多変数Bernstein多項式の線形結合として厳密に表します。



```maxima
(%i1) bernstein_expand(x*y+1,[x,y]);
(%o1)    2 x y + (1 - x) y + x (1 - y) + (1 - x) (1 - y)
(%i2) expand(%);
(%o2)                        x y + 1
```


一番目の引数が多項式でない時、Maximaはエラーをシグナルします。


`bernstein_expand`を使うには、最初に `load("bernstein")`。

<!-- category: Other -->
<!-- keywords: bernstein_explicit -->
<!-- signatures: bernstein_explicit -->
### Variable: bernstein_explicit

デフォルト値: `false`


`k`か `n`のどちらかが非整数の時、
オプション変数 `bernstein_explicit`は
Bernstein多項式の明示形式への展開を制御します; 例えば:



```maxima
(%i1) bernstein_poly(k,n,x);
(%o1)                bernstein_poly(k, n, x)
(%i2) bernstein_poly(k,n,x), bernstein_explicit : true;
                                       n - k  k
(%o2)            binomial(n, k) (1 - x)      x
```

`k`と `n`の両方が明示的に整数の時、
`bernstein(k,n,x)`は *いつも*明示形式に展開されます。

<!-- category: Other -->
<!-- keywords: bernstein_poly -->
<!-- signatures: bernstein_poly(k, n, x) -->
### Function: bernstein_poly (k, n, x)

`k`が負の整数でないと仮定すると、
Bernstein多項式は
`bernstein_poly(k,n,x) = binomial(n,k) x^k (1-x)^(n-k)`で定義されます;
負の整数`k`に対しては、Bernstein多項式 `bernstein_poly(k,n,x)`は零です。
`k`か `n`のどちらかが非整数の時、
オプション変数 `bernstein_explicit`は
Bernstein多項式の明示形式への展開を制御します。
例:



```maxima
(%i1) load("bernstein")$

(%i2) bernstein_poly(k,n,x);
(%o2)                bernstein_poly(k, n, x)
(%i3) bernstein_poly(k,n,x), bernstein_explicit : true;
                                       n - k  k
(%o3)            binomial(n, k) (1 - x)      x
```


Bernstein多項式はgradefプロパティとintegrateプロパティの両方を持ちます:



```maxima
(%i4) diff(bernstein_poly(k,n,x),x);
(%o4) (bernstein_poly(k - 1, n - 1, x)
                                 - bernstein_poly(k, n - 1, x)) n
(%i5) integrate(bernstein_poly(k,n,x),x);
(%o5) 
                                                            k + 1
 hypergeometric([k + 1, k - n], [k + 2], x) binomial(n, k) x
 ----------------------------------------------------------------
                              k + 1
```


実数と複素数両方の数値入力に対して、
Bernstein多項式は数値結果に評価されます:



```maxima
(%i6) bernstein_poly(5,9, 1/2 + %i);
                        39375 %i   39375
(%o6)                   -------- + -----
                          128       256
(%i7) bernstein_poly(5,9, 0.5b0 + %i);
(%o7)           3.076171875b2 %i + 1.5380859375b2
```


`bernstein_poly`を使うには、最初に `load("bernstein")`。

<!-- category: Other -->
<!-- keywords: multibernstein_poly -->
<!-- signatures: multibernstein_poly([k1,k2,..., kp], [n1,n2,..., np], [x1,x2,..., xp]) -->
### Function: multibernstein_poly ([k1,k2,..., kp], [n1,n2,..., np], [x1,x2,..., xp])

マルチBernstein多項式 `multibernstein_poly ([k1, k2, ..., kp], [n1, n2, ..., np], [x1, x2, ..., xp])`
Bernstein多項式 `bernstein_poly(k1, n1, x1) bernstein_poly(k2, n2, x2) ... bernstein_poly(kp, np, xp)`の積です。


`multibernstein_poly`を使うには、最初に `load("bernstein")`。

