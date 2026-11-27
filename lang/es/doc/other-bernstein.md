## Bernstein

<!-- category: Other -->
<!-- keywords: bernstein_approx -->
<!-- signatures: bernstein_approx(f, [x1,x1,...,xn], n) -->
### Function: bernstein_approx (f, [x1,x1,...,xn], n)

Devuelve el polinomio de Bernstein uniforme de `n`-ésimo orden que aproxima 
la función `(x1,x2,..xn) |--> f`.


Ejemplos:



```maxima
(%i1) bernstein_approx(f(x),[x], 2);
                        2       1                          2
(%o1)             f(1) x  + 2 f(-) (1 - x) x + f(0) (1 - x)
                                2
(%i2) bernstein_approx(f(x,y),[x,y], 2);
               2  2       1                2                  2  2
(%o2) f(1, 1) x  y  + 2 f(-, 1) (1 - x) x y  + f(0, 1) (1 - x)  y
                          2
          1   2                 1  1
 + 2 f(1, -) x  (1 - y) y + 4 f(-, -) (1 - x) x (1 - y) y
          2                     2  2
          1         2                      2        2
 + 2 f(0, -) (1 - x)  (1 - y) y + f(1, 0) x  (1 - y)
          2
       1                      2                  2        2
 + 2 f(-, 0) (1 - x) x (1 - y)  + f(0, 0) (1 - x)  (1 - y)
       2
```


Para hacer uso de `bernstein_approx`, ejecútese primero `load("bernstein")`.

<!-- category: Other -->
<!-- keywords: bernstein_expand -->
<!-- signatures: bernstein_expand(e, [x1,x1,...,xn]) -->
### Function: bernstein_expand (e, [x1,x1,...,xn])

Expresa el polinomio `e` como una combinación lineal de polinomios de
Bernstein multivariantes.



```maxima
(%i1) bernstein_expand(x*y+1,[x,y]);
(%o1)           2 x y + (1 - x) y + x (1 - y) + (1 - x) (1 - y)
(%i2) expand(%);
(%o2)                               x y + 1
```


Maxima devuelve un error si el primer argumento no es un polinomio.


Para hacer uso de `bernstein_expand`, ejecútese primero `load("bernstein")`.

<!-- category: Other -->
<!-- keywords: bernstein_explicit -->
<!-- signatures: bernstein_explicit -->
### Variable: bernstein_explicit

Valor por defecto: `false`


Cuando o bien `k` o `n` no son enteros, la variable opcional `bernstein_explicit` controla
la expansión de los polinomios de Bernstein a su forma explícita.


Ejemplo:



```maxima
(%i1) bernstein_poly(k,n,x);
(%o1)                       bernstein_poly(k, n, x)
(%i2) bernstein_poly(k,n,x), bernstein_explicit : true;
                                              n - k  k
(%o2)                   binomial(n, k) (1 - x)      x
```


Cuando tanto `k` como `n` son enteros, `bernstein(k,n,x)` se
expande siempre a su forma explícita.

<!-- category: Other -->
<!-- keywords: bernstein_poly -->
<!-- signatures: bernstein_poly(k, n, x) -->
### Function: bernstein_poly (k, n, x)

Si `k` no es un entero negativo, los polinomios de Bernstein se 
definen como `bernstein_poly(k,n,x) = binomial(n,k) x^k (1-x)^(n-k)`; 
en cambio, si `k` es un entero negativo, el polinomio de Bernstein
`bernstein_poly(k,n,x)` se anula. Cuando o bien `k` o `n` 
no son enteros, la variable opcional `bernstein_explicit` controla
la expansión de los polinomios de Bernstein a su forma explícita.


Ejemplo:



```maxima
(%i1) load("bernstein")$

(%i2) bernstein_poly(k,n,x);
(%o2)                bernstein_poly(k, n, x)
(%i3) bernstein_poly(k,n,x), bernstein_explicit : true;
                                       n - k  k
(%o3)            binomial(n, k) (1 - x)      x
```


Los polinomios de Bernstein tienen definidas su derivada e integral:



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


Cuando los argumentos contienen números decimales en coma flotante, los
polinomios de Bernstein también devuelven resultados decimales.



```maxima
(%i6) bernstein_poly(5,9, 1/2 + %i);
                        39375 %i   39375
(%o6)                   -------- + -----
                          128       256
(%i7) bernstein_poly(5,9, 0.5b0 + %i);
(%o7)           3.076171875b2 %i + 1.5380859375b2
```


Para hacer uso de `bernstein_poly`, ejecútese primero `load("bernstein")`.

<!-- category: Other -->
<!-- keywords: multibernstein_poly -->
<!-- signatures: multibernstein_poly([k1,k2,...,kp], [n1,n2,..., np], [x1,x2,..., xp]) -->
### Function: multibernstein_poly ([k1,k2,...,kp], [n1,n2,..., np], [x1,x2,..., xp])

La sentencia `multibernstein_poly ([k1,k2,...,kp],[n1,n2,..., np],[x1,x2,..., xp])`
es el producto de polinomios de Bernstein 
`bernstein_poly(k1,n1,x1) bernstein_poly(k2,n2,x2) ... bernstein_poly(kp,np,xp)`.


Para hacer uso de `multibernstein_poly`, ejecútese primero `load("bernstein")`.

