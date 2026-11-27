## Teoría de Números

<!-- category: Other -->
<!-- keywords: bern -->
<!-- signatures: bern(n) -->
### Function: bern (n)

Devuelve el *n*-ésimo número de Bernoulli del entero *n*.


Los números de Bernoulli iguales a cero son suprimidos si `zerobern` vale `false`.


Véase también `burn`.



```maxima
(%i1) zerobern: true$
(%i2) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                      1  1       1      1        1
(%o2)           [1, - -, -, 0, - --, 0, --, 0, - --]
                      2  6       30     42       30
(%i3) zerobern: false$
(%i4) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                      1  1    1   1     1   5     691   7
(%o4)           [1, - -, -, - --, --, - --, --, - ----, -]
                      2  6    30  42    30  66    2730  6
```

<!-- category: Other -->
<!-- keywords: bernpoly -->
<!-- signatures: bernpoly(x, n) -->
### Function: bernpoly (x, n)

Devuelve el *n*-ésimo polinomio de Bernoulli de variable *x*.

<!-- category: Other -->
<!-- keywords: bfhzeta -->
<!-- signatures: bfhzeta(s, h, n) -->
### Function: bfhzeta (s, h, n)

Devuelve la función zeta de Hurwitz para los argumentos *s* y *h*. El valor que devuelve es del tipo "big float" (bfloat) y *n*  es su número de dígitos.


La función zeta de Hurwitz se define como



$$
\zeta \left(s,h\right) = \sum_{k=0}^\infty {1 \over \left(k+h\right)^{s}}
$$


```maxima
inf
                        ====
                        \        1
         zeta (s,h)  =   >    --------
                        /            s
                        ====  (k + h)
                        k = 0
```


Ejecútese `load ("bffac")` antes de hacer uso de esta función.

<!-- category: Other -->
<!-- keywords: bfzeta -->
<!-- signatures: bfzeta(s, n) -->
### Function: bfzeta (s, n)

Devuelve la función zeta de Riemann para el argumento *s*. El valor que devuelve es del tipo "big float" (bfloat) y 
*n*  es su número de dígitos.


Es necesario cargar en memoria esta función haciendo `load ("bffac")`.

<!-- category: Other -->
<!-- keywords: burn -->
<!-- signatures: burn(n) -->
### Function: burn (n)

Siendo *n* entero, Devuelve un número racional que aproxima el 
*n*-ésimo número de Bernoulli. La función `burn` aprovecha
el hecho de que los números de Bernoulli racionales se pueden aproximar
con notable precisión gracias a 



```maxima
n - 1  1 - 2 n
              (- 1)      2        zeta(2 n) (2 n)!
     B(2 n) = ------------------------------------
                                2 n
                             %pi
```


La función `burn` puede ser más eficiente que `bern` cuando 
*n* es un número grande, ya que `bern` calcula todos los números
de Bernoulli hasta el *n*-ésimo. Por el contrario, `burn` hace 
uso de la aproximación para enteros pares *n* > 255. En caso de
enteros impares y *n* <= 255, se hace uso de la función `bern`.


Para utilizar esta función hay que cargarla antes en memoria escribiendo
`load ("bffac")`. Véase también `bern`.

<!-- category: Other -->
<!-- keywords: cf -->
<!-- signatures: cf(expr) -->
### Function: cf (expr)

Calcula aproximaciones con fracciones continuas. *expr* es una expresión
que contiene fracciones continuas, raíces cuadradas de enteros,
y números reales (enteros, racionales, decimales en coma flotante y decimales de
precisión arbitraria). `cf` calcula expansiones exactas de números 
racionales, pero las expansiones de nÃºmeros decimales de coma flotante se truncan
de acuerdo con el valor de `ratepsilon`, y la de los de decimales de precisión
arbitraria (bigfloats) lo hacen respecto de `10^(-fpprec)`.


En las expresiones se pueden combinar operandos con operadores aritméticos.
Maxima no conoce operaciones con fracciones continuas más allá de
la función `cf`.


La función `cf` evalúa sus argumentos después de asignar a la 
variable `listarith` el valor `false`, retornando una fracción
continua en forma de lista.


Una fracción continua `a + 1/(b + 1/(c + ...))` se representa como la
lista `[a, b, c, ...]`, donde los elementos `a`, `b`, `c`, ... 
se evalúan como enteros. La expresión *expr* puede contener también  
`sqrt (n)` donde `n` es un entero; en tal caso, `cf` devolverá 
tantos términos de la fracción continua como indique el valor de la variable 
`cflength` multiplicado por el período.


Una fracción continua puede reducirse a un número evaluando la representación 
aritmética que devuelve `cfdisrep`. Véase también  `cfexpand`, 
que es otra alternativa para evaluar fracciones continuas.


Véanse asimismo `cfdisrep`, `cfexpand` y `cflength`.


Ejemplos:



- *
La expresión *expr* contiene fracciones continuas y raíces
cuadradas de enteros.

```maxima
(%i1) cf ([5, 3, 1]*[11, 9, 7] + [3, 7]/[4, 3, 2]);
(%o1)               [59, 17, 2, 1, 1, 1, 27]
(%i2) cf ((3/17)*[1, -2, 5]/sqrt(11) + (8/13));
(%o2)        [0, 1, 1, 1, 3, 2, 1, 4, 1, 9, 1, 9, 2]
```
- *
La variable `cflength` controla cuantos períodos de la fracción 
continua se calculan para números irracionales algebraicos.

```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```
- *
Una fracción continua puede calcularse evaluando la representación aritmética 
que devuelve `cfdisrep`.

```maxima
(%i1) cflength: 3$
(%i2) cfdisrep (cf (sqrt (3)))$
(%i3) ev (%, numer);
(%o3)                   1.731707317073171
```
- *
Maxima no sabe sobre operaciones con fracciones continuas más de lo que aporta 
la función `cf`.

```maxima
(%i1) cf ([1,1,1,1,1,2] * 3);
(%o1)                     [4, 1, 5, 2]
(%i2) cf ([1,1,1,1,1,2]) * 3;
(%o2)                  [3, 3, 3, 3, 3, 6]
```

<!-- category: Other -->
<!-- keywords: cfdisrep -->
<!-- signatures: cfdisrep(lista) -->
### Function: cfdisrep (lista)

Construye y devuelve una expresión aritmética ordinaria de la forma  `a + 1/(b + 1/(c + ...))` a partir de la representación en formato lista de la fracción continua  `[a, b, c, ...]`.



```maxima
(%i1) cf ([1, 2, -3] + [1, -2, 1]);
(%o1)                     [1, 1, 1, 2]
(%i2) cfdisrep (%);
                                  1
(%o2)                     1 + ---------
                                    1
                              1 + -----
                                      1
                                  1 + -
                                      2
```

<!-- category: Other -->
<!-- keywords: cfexpand -->
<!-- signatures: cfexpand(x) -->
### Function: cfexpand (x)

Devuelve la matriz con los numeradores y denominadores de la última (columna 1) y penúltima (columna 2) convergentes de la fracción continua *x*.



```maxima
(%i1) cf (rat (ev (%pi, numer)));

`rat' replaced 3.141592653589793 by 103993/33102 =3.141592653011902
(%o1)                  [3, 7, 15, 1, 292]
(%i2) cfexpand (%); 
                         [ 103993  355 ]
(%o2)                    [             ]
                         [ 33102   113 ]
(%i3) %[1,1]/%[2,1], numer;
(%o3)                   3.141592653011902
```

<!-- category: Other -->
<!-- keywords: cflength -->
<!-- signatures: cflength -->
### Variable: cflength

Valor por defecto: 1


La variable `cflength` controla el número de términos de la fracción continua que devuelve la función `cf`, que será `cflength` multiplicado por el período. Así, el valor por defecto será el de un período.



```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```

<!-- category: Other -->
<!-- keywords: chinese -->
<!-- signatures: chinese([r_1, ..., r_n], [m_1, ..., m_n]) -->
### Function: chinese ([r_1, ..., r_n], [m_1, ..., m_n])

Resulve el sistema de congruencias `x = r_1 mod m_1`, ..., `x = r_n mod m_n`.
Los restos *r_n* pueden ser enteros arbitrarios, mientras que los módulos *m_n*
deben ser positivos y primos dos a dos. 



```maxima
(%i1) mods : [1000, 1001, 1003, 1007];
(%o1)                   [1000, 1001, 1003, 1007]
(%i2) lreduce('gcd, mods);
(%o2)                               1
(%i3) x : random(apply("*", mods));
(%o3)                         685124877004
(%i4) rems : map(lambda([z], mod(x, z)), mods);
(%o4)                       [4, 568, 54, 624]
(%i5) chinese(rems, mods);
(%o5)                         685124877004
(%i6) chinese([1, 2], [3, n]);
(%o6)                    chinese([1, 2], [3, n])
(%i7) %, n = 4;
(%o7)                              10
```

<!-- category: Other -->
<!-- keywords: divsum -->
<!-- signatures: divsum(n, k), divsum(n) -->
### Function: divsum (n, k)

La llamada `divsum (n, k)` devuelve la suma de los divisores de *n* elevados a la *k*-ésima potencia.


La llamada `divsum (n)` devuelve la suma de los divisores de *n*.



```maxima
(%i1) divsum (12);
(%o1)                          28
(%i2) 1 + 2 + 3 + 4 + 6 + 12;
(%o2)                          28
(%i3) divsum (12, 2);
(%o3)                          210
(%i4) 1^2 + 2^2 + 3^2 + 4^2 + 6^2 + 12^2;
(%o4)                          210
```

<!-- category: Other -->
<!-- keywords: euler -->
<!-- signatures: euler(n) -->
### Function: euler (n)

Devuelve el *n*-ésimo número de Euler del entero no negativo *n*.
Los número de Euler iguales a cero se eliminan si `zerobern` vale `false`.


Para la constante de Euler-Mascheroni, véase `%gamma`.



```maxima
(%i1) zerobern: true$
(%i2) map (euler, [0, 1, 2, 3, 4, 5, 6]);
(%o2)               [1, 0, - 1, 0, 5, 0, - 61]
(%i3) zerobern: false$
(%i4) map (euler, [0, 1, 2, 3, 4, 5, 6]);
(%o4)               [1, - 1, 5, - 61, 1385, - 50521, 2702765]
```

<!-- category: Other -->
<!-- keywords: factors_only -->
<!-- signatures: factors_only -->
### Variable: factors_only

Valor por defecto: `false`


Controla el resultado devuelto por `ifactors`. El valor por defecto
`false` hace que `ifactors` no dé información sobre las
multiplicidades de los factores primos calculados. Cuando `factors_only`
vale `true`, `ifactors` solo devuelve la lista de factores primos.


Para ejemplos, véase `ifactors`.

<!-- category: Other -->
<!-- keywords: fib -->
<!-- signatures: fib(n) -->
### Function: fib (n)

Devuelve el *n*-ésimo número de Fibonacci. La llamada `fib(0)` 
devuelve 0, `fib(1)` devuelve 1 y `fib (-n)` es igual a 
`(-1)^(n + 1) * fib(n)`.


Después de llamar a `fib`, la variable `prevfib` toma el valor 
`fib (n - 1)`, que es el número de Fibonacci que precede al último calculado.



```maxima
(%i1) map (fib, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o1)           [- 3, 2, - 1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
```

<!-- category: Other -->
<!-- keywords: fibtophi -->
<!-- signatures: fibtophi(expr) -->
### Function: fibtophi (expr)

Expresa los números de Fibonacci en *expr* en términos de la razón áurea `%phi`,
que es `(1 + sqrt(5))/2`, aproximadamente 1.61803399.


Ejemplos:









```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1
(%i4) ratsimp (%);
(%o4)                           0
```

<!-- category: Other -->
<!-- keywords: ifactors -->
<!-- signatures: ifactors(n) -->
### Function: ifactors (n)

Devuelve la factorización del entero positivo *n*. Si `n=p1^e1..pk^nk` es
la descomposición de *n* en números primos, `ifactors` devuelve 
`[[p1, e1], ... , [pk, ek]]`.


Los métodos de factorización se basan en divisiones tentativas con números primos
hasta 9973, en los métodos rho y p-1 de Pollard y en curvas elípticas.


La respuesta que se obtiene de `ifactors` está controlada por la variable opcional
`factors_only`. El valor por defecto `false` hace que `ifactors` no 
dé información sobre las multiplicidades de los factores primos calculados. 
Cuando `factors_only` vale `true`, `ifactors` solo devuelve la lista 
de factores primos.



```maxima
(%i1) ifactors(51575319651600);
(%o1)     [[2, 4], [3, 2], [5, 2], [1583, 1], [9050207, 1]]
(%i2) apply("*", map(lambda([u], u[1]^u[2]), %));
(%o2)                        51575319651600
(%i3) ifactors(51575319651600), factors_only : true;
(%o3)                   [2, 3, 5, 1583, 9050207]
```

<!-- category: Other -->
<!-- keywords: igcdex -->
<!-- signatures: igcdex(n, k) -->
### Function: igcdex (n, k)

Devuelve la lista `[a, b, u]`, donde *u* es
el máximo común divisor de *n* y *k*, siendo *u*
igual a `a n + b k`. Los argumentos
*n* y *k* deben ser enteros.


`igcdex` implementa el algoritmo de Euclides. Véase también `gcdex`.


La instrucción `load("gcdex")` carga esta función.


Ejemplos:



```maxima
(%i1) load("gcdex")$

(%i2) igcdex(30,18);
(%o2)                      [- 1, 2, 6]
(%i3) igcdex(1526757668, 7835626735736);
(%o3)            [845922341123, - 164826435, 4]
(%i4) igcdex(fib(20), fib(21));
(%o4)                   [4181, - 2584, 1]
```

<!-- category: Other -->
<!-- keywords: inrt -->
<!-- signatures: inrt(x, n) -->
### Function: inrt (x, n)

Devuelve la raíz entera *n*-ésima del valor absoluto de  *x*.



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], inrt (10^a, 3)), l);
(%o2) [2, 4, 10, 21, 46, 100, 215, 464, 1000, 2154, 4641, 10000]
```

<!-- category: Other -->
<!-- keywords: inv_mod -->
<!-- signatures: inv_mod(n, m) -->
### Function: inv_mod (n, m)

Calcula el inverso de *n* módulo *m*. 
La llamada `inv_mod (n,m)` devuelve `false`
si *n* es un divisor nulo módulo *m*.



```maxima
(%i1) inv_mod(3, 41);
(%o1)                           14
(%i2) ratsimp(3^-1), modulus = 41;
(%o2)                           14
(%i3) inv_mod(3, 42);
(%o3)                          false
```

<!-- category: Other -->
<!-- keywords: isqrt -->
<!-- signatures: isqrt(x) -->
### Function: isqrt (x)

Devuelve la "raíz cuadrada entera"
del valor absoluto de *x*,
el cual debe ser un entero.

<!-- category: Other -->
<!-- keywords: jacobi -->
<!-- signatures: jacobi(p, q) -->
### Function: jacobi (p, q)

Devuelve el símbolo de Jacobi para *p* y *q*.



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], jacobi (a, 9)), l);
(%o2)         [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
```

<!-- category: Other -->
<!-- keywords: lcm -->
<!-- signatures: lcm(expr_1, ..., expr_n) -->
### Function: lcm (expr_1, ..., expr_n)

Devuelve el mínimo común múltiplo de sus argumentos. 
Los argumentos pueden ser tanto expresiones en general como enteros.


Es necesario cargar en memoria esta función haciendo `load ("functs")`.

<!-- category: Other -->
<!-- keywords: lucas -->
<!-- signatures: lucas(n) -->
### Function: lucas (n)

Devuelve el *n*-ésimo número de Lucas.
`lucas(0)` es igual a 2, `lucas(1)` es igual a 1 y 
`lucas(-n)` es igual a `(-1)^(-n) * lucas(n)`.



```maxima
(%i1) map (lucas, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o1)             [7, - 4, 3, - 1, 2, 1, 3, 4, 7, 11, 18, 29, 47]
```


Después de llamar a `lucas`, la variable global `next_lucas`
es igual a `lucas (n + 1)`, el número de Lucas que sigue al
último que se ha devuelto. El ejemplo muestra como los números de
Fibonacci se pueden calcular mediante  `lucas` y `next_lucas`.



```maxima
(%i1) fib_via_lucas(n) := 
         block([lucas : lucas(n)],
         signum(n) * (2*next_lucas - lucas)/5 )$
(%i2) map (fib_via_lucas, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o2)             [- 3, 2, - 1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
```

<!-- category: Other -->
<!-- keywords: mod -->
<!-- signatures: mod(x, y) -->
### Function: mod (x, y)

Si *x* e *y* son números reales e *y* es distinto de cero,
devuelve `x - y * floor(x / y)`.
Para todos los reales *x*, se tiene `mod (x, 0) = x`. Para información sobre la definición de  `mod (x, 0) = x`, véase la sección 3.4 de "Concrete Mathematics", 
by Graham, Knuth, and Patashnik. La función `mod (x, 1)` es de diente de sierra con periodo unidad y con `mod (1, 1) = 0` y `mod (0, 1) = 0`.


Para encontrar el argumento principal (un número del intervalo `(-%pi, %pi]`) de un número complejo, hágase uso de la función `x |-> %pi - mod (%pi - x, 2*%pi)`, donde *x* es un argumento.


Si *x* e *y* son expresiones constantes (por ejemplo, `10 * %pi`), `mod` utiliza el mismo esquema de evaluación basado en números grandes en coma flotante (big floats) que `floor` y `ceiling`. También es posible, pero improbable, que `mod` pueda retornar un valor erróneo en tales casos.


Para argumentos no numéricos *x* o *y*, `mod` aplica algunas reglas de simplificación:








```maxima
(%i1) mod (x, 0);
(%o1)                           x
(%i2) mod (a*x, a*y);
(%o2)                      a mod(x, y)
(%i3) mod (0, x);
(%o3)                           0
```

<!-- category: Other -->
<!-- keywords: next_prime -->
<!-- signatures: next_prime(n) -->
### Function: next_prime (n)

Devuelve el menor de los primos mayores que *n*.



```maxima
(%i1) next_prime(27);
(%o1)                       29
```

<!-- category: Other -->
<!-- keywords: partfrac -->
<!-- signatures: partfrac(expr, var) -->
### Function: partfrac (expr, var)

Expande la expresión *expr* en fracciones parciales respecto de la variable principal *var*. La función `partfrac` hace una descomposición completa en fracciones parciales. El algoritmo que se utiliza se basa en el hecho de que los denominadores de la expansión en fracciones parciales (los factores del denominador original) son primos relativos. Los numeradores se pueden escribir como combinaciones lineales de los denominadores.



```maxima
(%i1) 1/(1+x)^2 - 2/(1+x) + 2/(2+x);
                      2       2        1
(%o1)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
(%i2) ratsimp (%);
                                 x
(%o2)                 - -------------------
                         3      2
                        x  + 4 x  + 5 x + 2
(%i3) partfrac (%, x);
                      2       2        1
(%o3)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
```

<!-- category: Other -->
<!-- keywords: power_mod -->
<!-- signatures: power_mod(a, n, m) -->
### Function: power_mod (a, n, m)

Utiliza un algoritmo modular para calcular `a^n mod m`,
siendo *a* y *n* enteros cualesquiera y *m* un entero positivo.
Si *n* es negativo, se utilizará `inv_mod` para encontrar el
inverso modular.



```maxima
(%i1) power_mod(3, 15, 5);
(%o1)                          2
(%i2) mod(3^15,5);
(%o2)                          2
(%i3) power_mod(2, -1, 5);
(%o3)                          3
(%i4) inv_mod(2,5);
(%o4)                          3
```

<!-- category: Other -->
<!-- keywords: prev_prime -->
<!-- signatures: prev_prime(n) -->
### Function: prev_prime (n)

Devuelve el mayor de los primos menores que *n*.



```maxima
(%i1) prev_prime(27);
(%o1)                       23
```

<!-- category: Other -->
<!-- keywords: primep -->
<!-- signatures: primep(n) -->
### Function: primep (n)

Comprueba si el número entero *n* es o no primo, devolviendo `true`
o `false` según el caso.


Cuando el resultado de `primep (n)` es `false`, *n* es un
número compuesto, y si es `true`, *n* es primo con alta probabilidad.


Si *n* es menor que 3317044064679887385961981, se utiliza una versión 
determinística de la prueba de Miller-Rabin. En tal caso,
si `primep (n)` devuelve `true`, entonces *n* es un número primo.


Para *n* mayor que 3317044064679887385961981 `primep` realiza 
`primep_number_of_tests` pruebas de seudo-primalidad de Miller-Rabin y una 
prueba de seudo-primalidad de Lucas. La probabilidad de que un número compuesto 
*n* pase una prueba de Miller-Rabin es menor que 1/4. Con el valor por defecto de 
`primep_number_of_tests`, que es 25, la probabilidad de que *n*
sea compuesto es menor que 10^-15.

<!-- category: Other -->
<!-- keywords: primep_number_of_tests -->
<!-- signatures: primep_number_of_tests -->
### Variable: primep_number_of_tests

Valor por defecto: 25


Número de pruebas de Miller-Rabin a realizar por `primep`.

<!-- category: Other -->
<!-- keywords: qunit -->
<!-- signatures: qunit(n) -->
### Function: qunit (n)

Devuelve la unidad principal de `sqrt (n)`, siendo *n* un entero; consiste en la resolución de la ecuación de Pell  `a^2 - n b^2 = 1`.



```maxima
(%i1) qunit (17);
(%o1)                     sqrt(17) + 4
(%i2) expand (% * (sqrt(17) - 4));
(%o2)                           1
```

<!-- category: Other -->
<!-- keywords: totient -->
<!-- signatures: totient(n) -->
### Function: totient (n)

Devuelve el número de enteros menores o iguales a *n* que son primos relativos con *n*.

<!-- category: Other -->
<!-- keywords: zerobern -->
<!-- signatures: zerobern -->
### Variable: zerobern

Valor por defecto: `true`


Si `zerobern` vale `false`, `bern` excluye los números de Bernoulli
y `euler` excluye los números de Euler que sean iguales a cero.
Véase `bern` y `euler`.

<!-- category: Other -->
<!-- keywords: zeta -->
<!-- signatures: zeta(n) -->
### Function: zeta (n)

Devuelve la función zeta de Riemann. Si *n* es entero negativo,
0 o número par positivo, la función zeta de Riemann devuelve un
valor exacto; en el caso de número par positivo, la variable opcional
`zeta%pi`, además, tiene que tener el valor `true` 
(véase `zeta%pi`). 
Cuando el argumento es un número decimal o bigfloat,
entonces la función zeta de Riemann se calcula numéricamente.
Maxima devuelve una forma nominal `zeta (n)` para
cualesquiera otros argumentos, incluidos los racionales no enteros,
los números complejos y los enteros pares si `zeta%pi` vale
`false`.


`zeta(1)` no está definida, pero Maxima conce el límite 
de `limit(zeta(x), x, 1)` por ambos lados.


La función zeta de Riemann se distribuye sobre las listas, matrices
y ecuaciones.


Véanse también `bfzeta` y `zeta%pi`.


Ejemplos:








```maxima
(%i1) zeta([-2,-1,0,0.5,2,3,1+%i]);
                                              2
             1     1                       %pi
(%o1)  [0, - --, - -, - 1.460354508809587, ----, zeta(3), zeta(%i + 1)]
             12    2                        6 

(%i2) limit(zeta(x),x,1,plus);
(%o2)                                 inf
(%i3) limit(zeta(x),x,1,minus);
(%o3)                                minf
```

<!-- category: Other -->
<!-- keywords: zeta%pi -->
<!-- signatures: zeta%pi -->
### Variable: zeta%pi

Valor por defecto: `true`


Si `zeta%pi` vale `true`, `zeta` devuelve una expresión proporcional a `%pi^n` si `n` es un número par positivo. En caso contrario, `zeta` no se evalúa y devuelve la forma nominal `zeta (n)`.


Ejemplos:









```maxima
(%i1) zeta%pi: true$
(%i2) zeta (4);
                                 4
                              %pi
(%o2)                         ----
                               90
(%i3) zeta%pi: false$
(%i4) zeta (4);
(%o4)                        zeta(4)
```

<!-- category: Other -->
<!-- keywords: zn_add_table -->
<!-- signatures: zn_add_table(n) -->
### Function: zn_add_table (n)

Muestra la tabla de la suma de todos los elementos de (Z/*n*Z).


Véanse también `zn_mult_table` y `zn_power_table`.

<!-- category: Other -->
<!-- keywords: zn_determinant -->
<!-- signatures: zn_determinant(matrix, p) -->
### Function: zn_determinant (matrix, p)

Utiliza el procedimiento de la descomposición LU para calcular el determinante
de *matrix* sobre (Z/*p*Z). El argumento *p* debe ser un número primo.


Si el determinante es igual a cero, el procedimiento puede fallar, en cuyo caso
`zn_determinant` calcula el determinante no modular y luego reduce.


Véase también `zn_invert_by_lu`.


Ejemplo:



```maxima
(%i1) m : matrix([1,3],[2,4]);
                                [ 1  3 ]
(%o1)                           [      ]
                                [ 2  4 ]
(%i2) zn_determinant(m, 5);
(%o2)                               3
(%i3) m : matrix([2,4,1],[3,1,4],[4,3,2]);
                               [ 2  4  1 ]
                               [         ]
(%o3)                          [ 3  1  4 ]
                               [         ]
                               [ 4  3  2 ]
(%i4) zn_determinant(m, 5);
(%o4)                               0
```

<!-- category: Other -->
<!-- keywords: zn_invert_by_lu -->
<!-- signatures: zn_invert_by_lu(matrix, p) -->
### Function: zn_invert_by_lu (matrix, p)

Utiliza el procedimiento de la descomposición LU para calcular la inversa
modular de *matrix* sobre (Z/*p*Z). El argumento *p* debe ser 
un número primo y *matrix* invertible. La función `zn_invert_by_lu`
devuelve `false` si *matrix* no es invertible.


Véase `zn_determinant`.


Ejemplo:



```maxima
(%i1) m : matrix([1,3],[2,4]);
                                [ 1  3 ]
(%o1)                           [      ]
                                [ 2  4 ]
(%i2) zn_determinant(m, 5);
(%o2)                               3
(%i3) mi : zn_invert_by_lu(m, 5);
                                [ 3  4 ]
(%o3)                           [      ]
                                [ 1  2 ]
(%i4) matrixmap(lambda([a], mod(a, 5)), m . mi);
                                [ 1  0 ]
(%o4)                           [      ]
                                [ 0  1 ]
```

<!-- category: Other -->
<!-- keywords: zn_log -->
<!-- signatures: zn_log(a, g, n), zn_log(a, g, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_log (a, g, n)

Calcula el logaritmo discreto. Sea (Z/*n*Z)* un grupo cíclico,
*g* una raíz primitiva módulo *n* y *a* un miembro
de este grupo, entonces `zn_log (a, g, n)` calcula la congruencia `g^x = a mod n`.


El algoritmo que se aplica necesita una factorización prima de `totient(n)`. Esta 
factorización puede requerir mucho tiempo de cálculo, por lo que en ciertos casos puede
ser aconsejable factorizar primero y luego pasar la lista de factores a `zn_log` como
cuarto argumento. La lista debe ser de la misma forma que las lista devuelta por 
`ifactors(totient(n))` utilizando la opción por defecto `factors_only : false`.


El algoritmo utiliza la reducción de Pohlig-Hellman y el método Rho de Pollard
para los logaritmos discretos. El tiempo de ejecución de `zn_log` depende en
primer lugar del número de bits del mayor factor primo del totient.


Véanse también `zn_primroot`, `zn_order`, `ifactors` y `totient`.


Ejemplos:


`zn_log (a, g, n)` resuelve la congruencia `g^x = a mod n`.



```maxima
(%i1) n : 22$
(%i2) g : zn_primroot(n);
(%o2)                               7
(%i3) ord_7 : zn_order(7, n);
(%o3)                              10
(%i4) powers_7 : makelist(power_mod(g, x, n), x, 0, ord_7 - 1);
(%o4)              [1, 7, 5, 13, 3, 21, 15, 17, 9, 19]
(%i5) zn_log(21, g, n);
(%o5)                               5
(%i6) map(lambda([x], zn_log(x, g, n)), powers_7);
(%o6)                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


El cuarto argumento opcional debe ser de la misma forma que la lista devuelta por
`ifactors(totient(n))`. 



```maxima
(%i1) (p : 2^127-1, primep(p));
(%o1)                             true
(%i2) ifs : ifactors(p - 1)$
(%i3) g : zn_primroot(p, ifs);
(%o3)                              43
(%i4) a : power_mod(g, 1234567890, p)$
(%i5) zn_log(a, g, p, ifs);
(%o5)                          1234567890
(%i6) time(%o5);  
(%o6)                            [1.204]
(%i7) f_max : last(ifs);
(%o7)                       [77158673929, 1]
(%i8) slength( printf(false, "~b", f_max[1]) );
(%o8)                              37
```

<!-- category: Other -->
<!-- keywords: zn_mult_table -->
<!-- signatures: zn_mult_table(n), zn_mult_table(n, all) -->
### Function: zn_mult_table (n)

Sin el argumento opcional *all*, `zn_mult_table(n)` 
muestra la tabla de multiplicación de los elementos de (Z/*n*Z)*,
que son todos elementos invertibles módulo *n*.


El argumento opcional *all* hace que la tabla se genere para todos los 
elementos no nulos.


Véanse también `zn_add_table` y `zn_power_table`.


Ejemplo:



```maxima
(%i1) zn_mult_table(4);
                                [ 1  3 ]
(%o1)                           [      ]
                                [ 3  1 ]
(%i2) zn_mult_table(4, all);
                               [ 1  2  3 ]
                               [         ]
(%o2)                          [ 2  0  2 ]
                               [         ]
                               [ 3  2  1 ]
```

<!-- category: Other -->
<!-- keywords: zn_order -->
<!-- signatures: zn_order(x, n), zn_order(x, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_order (x, n)

Devuelve el orden de *x* si es una unidad del grupo finito (Z/*n*Z)*, o devuelve `false`.
*x* una unidad módulo *n* si es coprimo con *n*.


El algoritmo que se aplica necesita una factorización prima de `totient(n)`. Esta 
factorización puede requerir mucho tiempo de cálculo, por lo que en ciertos casos puede
ser aconsejable factorizar primero y luego pasar la lista de factores a `zn_log` como
tercer argumento. La lista debe ser de la misma forma que las lista devuelta por 
`ifactors(totient(n))` utilizando la opción por defecto `factors_only : false`.


Véanse también `zn_primroot`, `ifactors` y `totient`.


Ejemplos:


`zn_order` calcula el orden de la unidad *x* en (Z/*n*Z)*.



```maxima
(%i1) n : 22$
(%i2) g : zn_primroot(n);
(%o2)                               7
(%i3) units_22 : sublist(makelist(i,i,1,21), lambda([x], gcd(x, n) = 1));
(%o3)              [1, 3, 5, 7, 9, 13, 15, 17, 19, 21]
(%i4) (ord_7 : zn_order(7, n)) = totient(n);
(%o4)                            10 = 10
(%i5) powers_7 : makelist(power_mod(g,i,n), i,0,ord_7 - 1);
(%o5)              [1, 7, 5, 13, 3, 21, 15, 17, 9, 19]
(%i6) map(lambda([x], zn_order(x, n)), powers_7);
(%o6)              [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]
(%i7) map(lambda([x], ord_7/gcd(x, ord_7)), makelist(i, i,0,ord_7 - 1));
(%o7)              [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]
(%i8) totient(totient(n));
(%o8)                               4
```


El tercer argumento opcional debe ser de la misma forma que la lista devuelta
por `ifactors(totient(n))`.



```maxima
(%i1) (p : 2^142 + 217, primep(p));
(%o1)                             true
(%i2) ifs : ifactors( totient(p) )$
(%i3) g : zn_primroot(p, ifs);
(%o3)                               3
(%i4) is( (ord_3 : zn_order(g, p, ifs)) = totient(p) );
(%o4)                             true
(%i5) map(lambda([x], ord_3/zn_order(x, p, ifs)), makelist(i,i,2,15));
(%o5)        [22, 1, 44, 10, 5, 2, 22, 2, 8, 2, 1, 1, 20, 1]
```

<!-- category: Other -->
<!-- keywords: zn_power_table -->
<!-- signatures: zn_power_table(n), zn_power_table(n, all) -->
### Function: zn_power_table (n)

Sin el argumento opcional *all*, `zn_power_table(n)` 
muestra la tabla de potencias de los elementos de (Z/*n*Z)*,
que son todos elementos invertibles módulo *n*. El exponente 
se obtiene con un bucle desde `1` hasta `totient(n)`
y la tabla termina con una columna de unos al lado derecho.


El argumento opcional *all* hace que la tabla se genere para todos los 
elementos no nulos. En este caso, el exponente se calcula con un bucle desde
`1` hasta `totient(n) + 1` y la última columna es por lo tanto 
igual a la primera.


Véanse también `zn_add_table` y `zn_mult_table`.


Ejemplo:



```maxima
(%i1) zn_power_table(6);
                                [ 1  1 ]
(%o1)                           [      ]
                                [ 5  1 ]
(%i2) zn_power_table(6, all);
                               [ 1  1  1 ]
                               [         ]
                               [ 2  4  2 ]
                               [         ]
(%o2)                          [ 3  3  3 ]
                               [         ]
                               [ 4  4  4 ]
                               [         ]
                               [ 5  1  5 ]
```

<!-- category: Other -->
<!-- keywords: zn_primroot -->
<!-- signatures: zn_primroot(n), zn_primroot(n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_primroot (n)

Si el grupo multiplicativo es cíclico, `zn_primroot`
calcula la menor raíz primitiva de módulo *n*. (Z/*n*Z)* es
cíclico si *n* es igual a `2`, `4`, `p^k` o `2*p^k`,
siendo `p` primo y mayor que `2` y `k` un número natural.
Si a la variable opcional `zn_primroot_pretest`, cuyo valor por defecto es
`false`, se le da el valor `true`, entonces `zn_primroot` 
realiza una prueba previa. En cualquier caso, el cálculo está limitado por la
cota superior `zn_primroot_limit`.


Si (Z/*n*Z)* no es cíclico o si no tiene raíces
primitivas menores que `zn_primroot_limit`, `zn_primroot` devuelve
`false`.


El algoritmo que se aplica necesita una factorización prima de `totient(n)`. Esta 
factorización puede requerir mucho tiempo de cálculo, por lo que en ciertos casos puede
ser aconsejable factorizar primero y luego pasar la lista de factores a `zn_log` como
argumento adicional. La lista debe ser de la misma forma que las lista devuelta por 
`ifactors(totient(n))` utilizando la opción por defecto `factors_only : false`.


Véanse también `zn_primroot_p`, `zn_order`, `ifactors` y `totient`.


Ejemplos:


`zn_primroot` calcula la menor raíz primitiva de módulo *n* o
devuelve `false`.



```maxima
(%i1) n : 14$
(%i2) g : zn_primroot(n);
(%o2)                               3
(%i3) zn_order(g, n) = totient(n);
(%o3)                             6 = 6
(%i4) n : 15$
(%i5) zn_primroot(n);
(%o5)                             false
```


El argumento opcional debe ser de la misma forma que la lista devuelta
por `ifactors(totient(n))`.



```maxima
(%i1) (p : 2^142 + 217, primep(p));
(%o1)                             true
(%i2) ifs : ifactors( totient(p) )$
(%i3) g : zn_primroot(p, ifs);
(%o3)                               3
(%i4) [time(%o2), time(%o3)];
(%o4)                    [[15.556972], [0.004]]
(%i5) is(zn_order(g, p, ifs) = p - 1);
(%o5)                             true
(%i6) n : 2^142 + 216$
(%i7) ifs : ifactors(totient(n))$
(%i8) zn_primroot(n, ifs), 
      zn_primroot_limit : 200, zn_primroot_verbose : true;
`zn_primroot' stopped at zn_primroot_limit = 200
(%o8)                             false
```

<!-- category: Other -->
<!-- keywords: zn_primroot_limit -->
<!-- signatures: zn_primroot_limit -->
### Variable: zn_primroot_limit

Valor por defecto: `1000` 


Si `zn_primroot` no puede encontrar una raíz primitiva,
entonces se para en esta cota superior. Si a la variable opcional 
`zn_primroot_verbose` se le da el valor `true`, se imprimirá un
mensaje cuando `zn_primroot_limit` sea alcanzado.

<!-- category: Other -->
<!-- keywords: zn_primroot_p -->
<!-- signatures: zn_primroot_p(x, n), zn_primroot_p(x, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_primroot_p (x, n)

Comprueba si *x* es una raíz primitiva en el 
grupo multiplizativo (Z/*n*Z)*.


El algoritmo que se aplica necesita una factorización prima de `totient(n)`. Esta 
factorización puede requerir mucho tiempo de cálculo, por lo que en ciertos casos puede
ser aconsejable factorizar primero y luego pasar la lista de factores a `zn_log` como
tercer argumento. La lista debe ser de la misma forma que las lista devuelta por 
`ifactors(totient(n))` utilizando la opción por defecto `factors_only : false`.


Véanse también `zn_primroot`, `zn_order`, `ifactors` y `totient`.


Ejemplos:


`zn_primroot_p` como función de predicado.



```maxima
(%i1) n : 14$
(%i2) units_14 : sublist(makelist(i,i,1,13), lambda([i], gcd(i, n) = 1));
(%o2)                     [1, 3, 5, 9, 11, 13]
(%i3) zn_primroot_p(13, n);
(%o3)                            false
(%i4) sublist(units_14, lambda([x], zn_primroot_p(x, n)));
(%o4)                            [3, 5]
(%i5) map(lambda([x], zn_order(x, n)), units_14);
(%o5)                      [1, 6, 6, 3, 3, 2]
```


El tercer argumento opcional debe ser de la misma forma que la lista
devuelta por `ifactors(totient(n))`.



```maxima
(%i1) (p : 2^142 + 217, primep(p));
(%o1)                             true
(%i2) ifs : ifactors( totient(p) )$
(%i3) sublist(makelist(i,i,1,50), lambda([x], zn_primroot_p(x, p, ifs)));
(%o3)      [3, 12, 13, 15, 21, 24, 26, 27, 29, 33, 38, 42, 48]
(%i4) [time(%o2), time(%o3)];
(%o4)                   [[7.748484], [0.036002]]
```

<!-- category: Other -->
<!-- keywords: zn_primroot_pretest -->
<!-- signatures: zn_primroot_pretest -->
### Variable: zn_primroot_pretest

Valor por defecto: `false` 


El grupo multiplicativo (Z/*n*Z)* es cíclico si if *n*
es igual a `2`, `4`, `p^k` o `2*p^k`, siendo `p`
un número primo mayor que `2` y `k` es un número natural.


La variable `zn_primroot_pretest` controla si `zn_primroot` debe
comprobar si sucede alguna de estas situaciones antes de calcular la menor
raíz primitiva. Solo se realizará esta comprobación si
`zn_primroot_pretest` toma el valor `true`.

<!-- category: Other -->
<!-- keywords: zn_primroot_verbose -->
<!-- signatures: zn_primroot_verbose -->
### Variable: zn_primroot_verbose

Valor por defecto: `false` 


Controla si `zn_primroot` imprime un mensaje cuando alcanza `zn_primroot_limit`.

