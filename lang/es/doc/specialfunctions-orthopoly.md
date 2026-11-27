## orthopoly

<!-- category: SpecialFunctions -->
<!-- keywords: assoc_legendre_p -->
<!-- signatures: assoc_legendre_p(n, m, x) -->
### Function: assoc_legendre_p (n, m, x)

Función asociada de Legendre de primera especie de grado *n* y orden *m*.


Referencia: Abramowitz y Stegun, ecuaciones 22.5.37, página 779, 8.6.6
(segunda ecuación), página 334 y  8.2.5, página 333.

<!-- category: SpecialFunctions -->
<!-- keywords: assoc_legendre_q -->
<!-- signatures: assoc_legendre_q(n, m, x) -->
### Function: assoc_legendre_q (n, m, x)

Función asociada de Legendre de segunda especie de grado *n* y orden *m*.


Referencia: Abramowitz y Stegun, ecuaciones 8.5.3 y 8.1.8.

<!-- category: SpecialFunctions -->
<!-- keywords: chebyshev_t -->
<!-- signatures: chebyshev_t(n, x) -->
### Function: chebyshev_t (n, x)

Función de Chebyshev de primera especie.


Referencia: Abramowitz y Stegun, ecuación 22.5.47, página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: chebyshev_u -->
<!-- signatures: chebyshev_u(n, x) -->
### Function: chebyshev_u (n, x)

Función de Chebyshev de segunda especie.


Referencia: Abramowitz y Stegun, ecuación 22.5.48, página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: gen_laguerre -->
<!-- signatures: gen_laguerre(n, a, x) -->
### Function: gen_laguerre (n, a, x)

Polinomio de Laguerre generalizado de grado *n*.


Referencia: Abramowitz y Stegun, ecuación 22.5.54, página 780.

<!-- category: SpecialFunctions -->
<!-- keywords: hermite -->
<!-- signatures: hermite(n, x) -->
### Function: hermite (n, x)

Polinomio de Hermite.


Referencia: Abramowitz y Stegun, ecuación 22.5.55, página 780.

<!-- category: SpecialFunctions -->
<!-- keywords: intervalp -->
<!-- signatures: intervalp(e) -->
### Function: intervalp (e)

Devuelve `true` si la entrada es un intervalo y `false` en caso contrario.

<!-- category: SpecialFunctions -->
<!-- keywords: jacobi_p -->
<!-- signatures: jacobi_p(n, a, b, x) -->
### Function: jacobi_p (n, a, b, x)

Polinomio de Jacobi.


Los polinomios de Jacobi están definidos para todo *a* y *b*;
sin embargo, el peso `(1 - x)^a (1 + x)^b`
no es integrable para `a <= -1` o `b <= -1`.


Referencia: Abramowitz y Stegun, ecuación 22.5.42, página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: laguerre -->
<!-- signatures: laguerre(n, x) -->
### Function: laguerre (n, x)

Polinomio de Laguerre.


Referencia: Abramowitz y Stegun, ecuaciones 22.5.16 y 22.5.54, página 780.

<!-- category: SpecialFunctions -->
<!-- keywords: legendre_p -->
<!-- signatures: legendre_p(n, x) -->
### Function: legendre_p (n, x)

Polinomio de Legendre de primera especie.


Referencia: Abramowitz y Stegun, ecuaciones 22.5.50 y 22.5.51, página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: legendre_q -->
<!-- signatures: legendre_q(n, x) -->
### Function: legendre_q (n, x)

Polinomio de Legendre de segunda especie.


Referencia: Abramowitz y Stegun, ecuaciones 8.5.3 y 8.1.8.

<!-- category: SpecialFunctions -->
<!-- keywords: orthopoly_recur -->
<!-- signatures: orthopoly_recur(f, args) -->
### Function: orthopoly_recur (f, args)

Devuelve una relación recursiva para la familia de funciones
ortogonales *f* con argumentos *args*. La recursión se hace con respecto
al grado del polinomio.






```maxima
(%i1) orthopoly_recur (legendre_p, [n, x]);
                    (2 n + 1) P (x) x - n P     (x)
                               n           n - 1
(%o1)   P     (x) = -------------------------------
         n + 1                   n + 1
```


El segundo argumento de `orthopoly_recur` debe ser una lista con
el número correcto de argumentos para la función *f*; si no
lo es, Maxima emite un mensaje de error.






```maxima
(%i1) orthopoly_recur (jacobi_p, [n, x]);

Function jacobi_p needs 4 arguments, instead it received 2
 -- an error.  Quitting.  To debug this try debugmode(true);
```


Además, si *f* no es el nombre de ninguna de las 
familias de polinomios ortogonales, se emite otro mensaje
de error.






```maxima
(%i1) orthopoly_recur (foo, [n, x]);

A recursion relation for foo isn't known to Maxima
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: SpecialFunctions -->
<!-- keywords: orthopoly_returns_intervals -->
<!-- signatures: orthopoly_returns_intervals -->
### Variable: orthopoly_returns_intervals

Valor por defecto: `true`


Si `orthopoly_returns_intervals` vale `true`, los números
decimales en coma flotante se retornan con el formato 
`interval (c, r)`, donde *c* es el centro del
intervalo y *r* su radio. El centro puede ser un número complejo,
en cuyo caso el intervalo es un disco en el plano complejo.

<!-- category: SpecialFunctions -->
<!-- keywords: orthopoly_weight -->
<!-- signatures: orthopoly_weight(f, args) -->
### Function: orthopoly_weight (f, args)

Devuelve una lista con tres elementos; el primer elemento es la
fórmula del peso para la familia de polinomios ortogonales *f*
con los argumentos dados por la lista *args*; el segundo y tercer
elementos son los extremos inferior y superior del intervalo de
ortogonalidad. Por ejemplo,







```maxima
(%i1) w : orthopoly_weight (hermite, [n, x]);
                            2
                         - x
(%o1)                 [%e    , - inf, inf]
(%i2) integrate (w[1] * hermite (3, x) * hermite (2, x), x, w[2], w[3]);
(%o2)                           0
```


La variable principal de *f* debe ser un símbolo, en caso
contrario Maxima emite un mensaje de error.

<!-- category: SpecialFunctions -->
<!-- keywords: pochhammer -->
<!-- signatures: pochhammer(n, x) -->
### Function: pochhammer (n, x)

Símbolo de Pochhammer. Para enteros no negativos *n* con
`n <= pochhammer_max_index`, la expresión 
`pochhammer (x, n)` se evalúa como el producto 
`x (x + 1) (x + 2) ... (x + n - 1)` si 
`n > 0` y como 1 si `n = 0`. Para *n* negativo,
`pochhammer (x, n)` se define como 
`(-1)^n / pochhammer (1 - x, -n)`.
Así por ejemplo,







```maxima
(%i1) pochhammer (x, 3);
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, -3);
                                 1
(%o2)               - -----------------------
                      (1 - x) (2 - x) (3 - x)
```


A fin de convertir el símbolo de Pochhammer en un cociente 
de funciones gamma (véase Abramowitz y Stegun, ecuación 6.1.22),
hágase uso de `makegamma`. Por ejemplo,






```maxima
(%i1) makegamma (pochhammer (x, n));
                          gamma(x + n)
(%o1)                     ------------
                            gamma(x)
```


Si *n* es mayor que `pochhammer_max_index` o si *n*
es simbólico, `pochhammer` devuelve una forma nominal.






```maxima
(%i1) pochhammer (x, n);
(%o1)                         (x)
                                 n
```

<!-- category: SpecialFunctions -->
<!-- keywords: pochhammer_max_index -->
<!-- signatures: pochhammer_max_index -->
### Variable: pochhammer_max_index

Valor por defecto: 100


`pochhammer (n, x)` se evalúa como un producto
si y sólo si `n <= pochhammer_max_index`.


Ejemplos:







```maxima
(%i1) pochhammer (x, 3), pochhammer_max_index : 3;
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, 4), pochhammer_max_index : 3;
(%o2)                         (x)
                                 4
```


Referencia: Abramowitz y Stegun, ecuación 6.1.16, página 256.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_bessel_j -->
<!-- signatures: spherical_bessel_j(n, x) -->
### Function: spherical_bessel_j (n, x)

Función de Bessel esférica de primera especie.


Referencia: Abramowitz y Stegun, ecuaciones 10.1.8, página 437 y 10.1.15, página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_bessel_y -->
<!-- signatures: spherical_bessel_y(n, x) -->
### Function: spherical_bessel_y (n, x)

Función de Bessel esférica de segunda especie.


Referencia: Abramowitz y Stegun, ecuaciones 10.1.9, página 437 y 10.1.15, página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_hankel1 -->
<!-- signatures: spherical_hankel1(n, x) -->
### Function: spherical_hankel1 (n, x)

Función esférica de Hankel de primera especie.


Referencia: Abramowitz y Stegun, ecuación 10.1.36, página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_hankel2 -->
<!-- signatures: spherical_hankel2(n, x) -->
### Function: spherical_hankel2 (n, x)

Función esférica de Hankel de segunda especie.


Referencia: Abramowitz y Stegun, ecuación 10.1.17, página 439.

<!-- category: SpecialFunctions -->
<!-- keywords: spherical_harmonic -->
<!-- signatures: spherical_harmonic(n, m, x, y) -->
### Function: spherical_harmonic (n, m, x, y)

Función armónica esférica.


Referencia: Merzbacher 9.64.

<!-- category: SpecialFunctions -->
<!-- keywords: ultraspherical -->
<!-- signatures: ultraspherical(n, a, x) -->
### Function: ultraspherical (n, a, x)

Polinomio ultraesférico o de Gegenbauer.


Referencia: Abramowitz y Stegun, ecuación 22.5.46, página 779.

<!-- category: SpecialFunctions -->
<!-- keywords: unit_step -->
<!-- signatures: unit_step(x) -->
### Function: unit_step (x)

Función de escalón unidad continua por la izquierda, definida de
tal forma que `unit_step (x)` se anula para `x <= 0`
y es igual a 1 para `x > 0`.


En caso de ser necesaria una función escalón unidad que tome el
valor 1/2 en el origen, utilícese `(1 + signum (x))/2`.

