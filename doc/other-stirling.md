## stirling

### Function: stirling (stirling, z, n, stirling, z, n, pred)

Replace `gamma(x)` with the $O(1/x^{2n-1})$ Stirling formula. when *n* isn’t
a nonnegative integer, signal an error. With the optional third argument `pred`,
the Stirling formula is applied only when `pred` is true.


Reference: Abramowitz & Stegun, " Handbook of mathematical functions", 6.1.40.


Examples:


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


The function `stirling` knows the difference between the variable ’gamma’ and
the function gamma:



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


To apply the Stirling formula only to terms that involve the variable `k`,
use an optional third argument; for example


```maxima
(%i7) makegamma(pochhammer(a,k)/pochhammer(b,k));
(%o7) (gamma(b)*gamma(k+a))/(gamma(a)*gamma(k+b))
(%i8) stirling(%,1, lambda([s], not(freeof(k,s))));
(%o8) (%e^(b-a)*gamma(b)*(k+a)^(k+a-1/2)*(k+b)^(-k-b+1/2))/gamma(a)
```

The terms `gamma(a)` and `gamma(b)` are free of `k`, so the Stirling formula
was not applied to these two terms.


To use this function write first `load("stirling")`.

