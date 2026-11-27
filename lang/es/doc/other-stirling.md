## stirling

<!-- category: Other -->
<!-- keywords: stirling -->
<!-- signatures: stirling(z, n), stirling(z, n, pred) -->
### Function: stirling (z, n)

Sustituye `gamma(x)` por la fórmula de Stirling $O(1/x^(2n-1))$.
Si *n* no es un entero no negativo, emite un mensaje de error. Con el
tercer argumento opcional `pred`, la fórmula de Stirling sólo se aplica 
si `pred` vale `true`.


Referencia: Abramowitz & Stegun, " Handbook of mathematical functions", 6.1.40.


Ejemplos:


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


La función `stirling` conoce la diferencia existente entre
la variable ’gamma’ y la función gamma:



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


Para aplicar la fórmula de Stirling sólo a aquellos términos que
contengan la variable `k`, hágase uso del tercer argumento
opcional; por ejemplo,


```maxima
(%i7) makegamma(pochhammer(a,k)/pochhammer(b,k));
(%o7) (gamma(b)*gamma(k+a))/(gamma(a)*gamma(k+b))
(%i8) stirling(%,1, lambda([s], not(freeof(k,s))));
(%o8) (%e^(b-a)*gamma(b)*(k+a)^(k+a-1/2)*(k+b)^(-k-b+1/2))/gamma(a)
```


Los términos `gamma(a)` y `gamma(b)` no contienen a `k`, por
lo que la fórmula de Stirling no ha sido aplicada a ellos.


Antes de hacer uso de esta función ejecútese  `load("stirling")`.

