## zeilberger

<!-- category: Series -->
<!-- keywords: AntiDifference -->
<!-- signatures: AntiDifference(F_k, k) -->
### Function: AntiDifference (F_k, k)

Returns the hypergeometric anti-difference
of $F_k$, if it exists.
Otherwise `AntiDifference` returns `no_hyp_antidifference`.

<!-- category: Series -->
<!-- keywords: ev_point -->
<!-- signatures: ev_point -->
### Variable: ev_point

Valor por defecto: `big_primes[10]`


La variable `ev_point` guarda el valor para el que debe evaluarse *n*
durante la ejecución de la prueba modular de `parGosper`.

<!-- category: Series -->
<!-- keywords: Gosper -->
<!-- signatures: Gosper(F_k, k) -->
### Function: Gosper (F_k, k)

Devuelve, si existe, el elemento racional asociado a *F_k*, esto es,
la función racional que verifica



$$
$F_k = R\left(k+1\right) \, F_{k+1} - R\left(k\right) \, F_k$,
$$

$F_k = R(k+1) F_(k+1) - R(k) F_k$,


En caso de no existir este elemento, `Gosper` devuelve `no_hyp_sol`.

<!-- category: Series -->
<!-- keywords: Gosper_in_Zeilberger -->
<!-- signatures: Gosper_in_Zeilberger -->
### Variable: Gosper_in_Zeilberger

Valor por defecto: `true`


Si `Gosper_in_Zeilberger` vale `true`,
la función `Zeilberger` llama a la función `Gosper`
antes de llamar a `parGosper`.
En caso contrario, `Zeilberger` invoca inmediatamente a `parGosper`.

<!-- category: Series -->
<!-- keywords: GosperSum -->
<!-- signatures: GosperSum(F_k, k, a, b) -->
### Function: GosperSum (F_k, k, a, b)

Devuelve la suma de los términos $F_k$ desde $k = a$ hasta
$k = b$ si $F_k$ tiene una antidiferencia
hipergeométrica. En caso contrario, `GosperSum` devuelve
`nongosper_summable`.


Ejemplos:













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

Valor por defecto: `linsolve`


La variable `linear_solver` guarda el nombre de la función que
se utilizará para resolver el sistema de ecuaciones del algoritmo de
Zeilberger.

<!-- category: Series -->
<!-- keywords: max_ord -->
<!-- signatures: max_ord -->
### Variable: max_ord

Valor por defecto: 5


`max_ord` es el máximo orden de recurrencia que ensayará la función `Zeilberger`.

<!-- category: Series -->
<!-- keywords: mod_big_prime -->
<!-- signatures: mod_big_prime -->
### Variable: mod_big_prime

Valor por defecto: `big_primes[1]`


La variable `mod_big_prime` guarda el módulo utilizado por la prueba
modular de `parGosper`.

<!-- category: Series -->
<!-- keywords: mod_test -->
<!-- signatures: mod_test -->
### Variable: mod_test

Valor por defecto: `false`


Si `mod_test` vale `true`,
la función `parGosper` ejecuta una prueba modular 
para descartar sistemas sin soluciones.

<!-- category: Series -->
<!-- keywords: mod_threshold -->
<!-- signatures: mod_threshold -->
### Variable: mod_threshold

Valor por defecto: 4


La variable `mod_threshold` es el máximo orden que ensaya la prueba modular
de `parGosper`.

<!-- category: Series -->
<!-- keywords: modular_linear_solver -->
<!-- signatures: modular_linear_solver -->
### Variable: modular_linear_solver

Valor por defecto: `linsolve`


La variable `modular_linear_solver` guarda el nombre de la función
que deberá ser llamada por la prueba modular de `parGosper` para
resolver sistemas lineales.

<!-- category: Series -->
<!-- keywords: parGosper -->
<!-- signatures: parGosper(F_{n,k}, k, n, d) -->
### Function: parGosper (F_{n,k}, k, n, d)

Intenta calcular una recurrecia de orden *d* para *F_{n,k}*.


El algoritmo devuelve una secuencia $[s_1, s_2, ..., s_m]$ de
soluciones, cada una de las cuales tiene la forma 


$[R(n, k), [a_0, a_1, ..., a_d]]$.


La función `parGosper` devuelve `[]` si no encuentra
ninguna recurrencia.

<!-- category: Series -->
<!-- keywords: simplified_output -->
<!-- signatures: simplified_output -->
### Variable: simplified_output

Valor por defecto: `false`


Si `simplified_output` vale `true`,
las funciones del paquete `zeilberger` tratan de
presentar las soluciones simplificadas.

<!-- category: Series -->
<!-- keywords: trivial_solutions -->
<!-- signatures: trivial_solutions -->
### Variable: trivial_solutions

Valor por defecto: `true`


Si `trivial_solutions` vale `true`,
la función `Zeilberger` devuelve soluciones triviales.

<!-- category: Series -->
<!-- keywords: warnings -->
<!-- signatures: warnings -->
### Variable: warnings

Valor por defecto: `true`


Si `warnings` vale `true`,
las funciones del paquete `zeilberger` emiten
mensajes de aviso durante su ejecución.

<!-- category: Series -->
<!-- keywords: Zeilberger -->
<!-- signatures: Zeilberger(F_{n,k}, k, n) -->
### Function: Zeilberger (F_{n,k}, k, n)

Intenta calcular la suma hipergeométrica indefinida de *F_{n,k}*.


La función `Zeilberger` invoca en primer lugar a `Gosper`,
y en caso de no encontrar una solución, llama después a `parGosper`
con los órdenes 1, 2, 3, ..., hasta `max_ord`. Si `Zeilberger`
encuentra una solución antes de alcanzar `max_ord`, se detiene su
ejecución y devuelve el resultado.


El algoritmo devuelve una secuencia $[s_1, s_2, ..., s_m]$ de
soluciones, cada una de las cuales tiene la forma 


$[R(n, k), [a_0, a_1, ..., a_d]]$.


La función `Zeilberger` devuelve `[]` si no encuentra
ninguna solución.


La función `Zeilberger` llama a `Gosper` sólo si 
`Gosper_in_Zeilberger` tiene el valor `true`.

