## solve_rec

<!-- category: Solving -->
<!-- keywords: product_use_gamma -->
<!-- signatures: product_use_gamma -->
### Variable: product_use_gamma

Valor por defecto:`true` 


Si `product_use_gamma` vale `true`,  `solve_rec`
introduce la función gamma en la expresión del resultado
cuando se simplifican productos.


Véanse también `simplify_products` y `solve_rec`.

<!-- category: Solving -->
<!-- keywords: reduce_order -->
<!-- signatures: reduce_order(rec, sol, var) -->
### Function: reduce_order (rec, sol, var)

Reduce el orden de la expresión recurrente lineal *rec* cuando
se conoce una solución particular *sol*. La recurrencia
reducida puede utilizarse para obterner más soluciones.


Ejemplo:



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

So the general solution is

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

Valor por defecto: `true`


Si `simplify_products` vale `true`, `solve_rec` intentará
simplificar los productos del resultado.


Véase también `solve_rec`.

<!-- category: Solving -->
<!-- keywords: simplify_sum -->
<!-- signatures: simplify_sum(expr) -->
### Function: simplify_sum (expr)

Intenta reducir todas las sumas que aparecen en *expr* a una forma
cerrada.


Para utilizar esta función cárguese previamente el paquete `simplify_sum`
ejecutando la instrucción `load("simplify_sum")`.


Ejemplo:








```maxima
(%i1) load("simplify_sum")$

(%i2) sum(binomial(n+k,k)/2^k,k,1,n)+sum(binomial(2*n,2*k),k,1,n);
        n                          n
       ====                       ====
       \     binomial(n + k, k)   \
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

Obtiene las soluciones hipergeométricas de la expresión recurrente *eqn*
con coeficientes lineales en la variable *var*. Los argumentos opcionales
*init* son condiciones iniciales.


La función `solve_rec` puede resolver expresiones recurrentes con
coeficientes constantes, encuentra soluciones hipergeométricas de
expresiones recurrentes lineales homogéneas con coeficientes 
polinomiales, obtiene soluciones racionales de expresiones recurrentes
lineales con coeficientes lineales y resuelve también expresiones
recurrentes de Ricatti.


Nótese que el tiempo de ejecución del algoritmo para encontrar soluciones 
hipergeométricas es exponencial respecto del grado del coeficiente principal.


Para hacer uso de esta función ejecútese previamente `load("solve_rec");`.


Ejemplo de recurrencia lineal con coeficientes constantes:



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


Ejemplo de recurrencia lineal con coeficientes polinomiales:



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


Ejemplo de recurrencia de Ricatti:



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



Véanse también `solve_rec_rat`, `simplify_products` y `product_use_gamma`.

<!-- category: Solving -->
<!-- keywords: solve_rec_rat -->
<!-- signatures: solve_rec_rat(eqn, var, [init]) -->
### Function: solve_rec_rat (eqn, var, [init])

Calcula las soluciones racionales de las expresiones recurrentes lineales. 
Véase `solve_rec` para la descripción de sus argumentos.


Para hacer uso de esta función ejecútese previamente `load("solve_rec");`.


Ejemplo:



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


Véase también `solve_rec`.

<!-- category: Solving -->
<!-- keywords: summand_to_rec -->
<!-- signatures: summand_to_rec(summand, k, n) -->
### Function: summand_to_rec (summand, k, n)

Devuelve la expresión recurrente que satisface la suma



```maxima
inf
    ====
    \
     >     sumando
    /
    ====
  k = minf
```


donde el sumando es hipergeométrico en  *k* y *n*.


Para hacer uso de esta función deben cargarse previamente los paquetes
`zeilberger` y `solve_rec` mediante la ejecución de las sentencias
`load("solve_rec")` y `load("zeilberger")`.



```maxima
(%i17) load("zeilberger")$
(%i18) summand: binom(3*k+1,k)*binom(3*(n-k),n-k)/(3*k+1)$
(%i19) summand_to_rec(summand, k, n);
Dependent equations eliminated:  (3 2)
(%o19) - 4 (n + 2) (2 n + 3) (2 n + 5) sm
                                         n + 2
                    2
 + 12 (2 n + 3) (9 n  + 27 n + 22) sm
                                     n + 1
 - 81 (n + 1) (3 n + 2) (3 n + 4) sm
                                    n
(%i21) sum(''summand, k, 0, n), n=0;
(%o21)                       1
(%i22) sum(''summand, k, 0, n), n=1;
(%o22)                       4
(%i23) product_use_gamma: false$
(%i24) solve_rec(%o19, sm[n], sm[0]=1, sm[1]=4);
              n - 1               n - 1
              /===\               /===\
               ! !                 ! !                n
             ( ! !   (3 %j + 2)) ( ! !   (3 %j + 4)) 3
               ! !                 ! !
              %j = 0              %j = 0
(%o24) sm  = ------------------------------------------
         n            n - 1
                      /===\
                       ! !                n
                     ( ! !   (2 %j + 3)) 2  n!
                       ! !
                      %j = 0
```

