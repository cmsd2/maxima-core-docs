## stirling

<!-- category: Other -->
<!-- keywords: stirling -->
<!-- signatures: stirling(z, n), stirling(z, n, pred) -->
### Function: stirling (z, n)

`gamma(x)`を
$O(1/x^(2n-1))$Stirling公式で置き換えます。
*n*が非負の整数の時、エラーを知らせます。
オプションの三番目の引数`pred`があると、
`pred`がtrueの時だけ
Stirling公式は適用されます。


参照文献: Abramowitz & Stegun, " Handbook of mathematical functions", 6.1.40.


例:


```maxima
(%i1) load ("stirling")$

(%i2) stirling(gamma(%alpha+x)/gamma(x),1);
       1/2 - x             x + %alpha - 1/2
(%o2) x        (x + %alpha)
                                   1           1
                            --------------- - ---- - %alpha
                            12 (x + %alpha)   12 x
                          %e
(%i3) taylor(%,x,inf,1);
                    %alpha       2    %alpha
          %alpha   x       %alpha  - x       %alpha
(%o3)/T/ x       + -------------------------------- + . . .
                                 2 x
(%i4) map('factor,%);
                                       %alpha - 1
         %alpha   (%alpha - 1) %alpha x
(%o4)   x       + -------------------------------
                                  2
```


関数`stirling`は変数’gamma’と関数gammaの違いを知っています:



```maxima
(%i5) stirling(gamma + gamma(x),0);
                                    x - 1/2   - x
(%o5)    gamma + sqrt(2) sqrt(%pi) x        %e
(%i6) stirling(gamma(y) + gamma(x),0);
                         y - 1/2   - y
(%o6) sqrt(2) sqrt(%pi) y        %e
                                              x - 1/2   - x
                         + sqrt(2) sqrt(%pi) x        %e
```


変数`k`を含む項だけに
Stirling公式を適用するために
オプションの三番目の引数を使います;
例えば、


```maxima
(%i7) makegamma(pochhammer(a,k)/pochhammer(b,k));
(%o7) (gamma(b)*gamma(k+a))/(gamma(a)*gamma(k+b))
(%i8) stirling(%,1, lambda([s], not(freeof(k,s))));
(%o8) (%e^(b-a)*gamma(b)*(k+a)^(k+a-1/2)*(k+b)^(-k-b+1/2))/gamma(a)
```

項`gamma(a)`と`gamma(b)`は、
`k`を含まないので、
Stirling公式はこれら２つの項に適用されませんでした。


この関数を使うには、最初に`load("stirling")`を書いてください。

