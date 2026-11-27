## stirling

<!-- category: Other -->
<!-- keywords: stirling -->
<!-- signatures: stirling(z, n) -->
### Function: stirling (z, n)

Substitui `gamma(x)` pela fórmula de Stirling $O(1/x^(2n-1))$. Quando *n* for
um inteiro estritamente negativo, sinaliza um erro.


Referência: Abramowitz & Stegun, " Handbook of mathematical functions", 6.1.40.


Exemplos:


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


A função `stirling` conhece a diferença entre a variável *gamma* e
a função `gamma`:



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


Para usar essa função escreva primeiro `load("stirling")`.

