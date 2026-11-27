## simplification

<!-- category: Simplification -->
<!-- keywords: agd -->
<!-- signatures: agd(x) -->
### Function: agd (x)

Devuelve la inversa de la función de Gudermann,
`log (tan (%pi/4 + x/2))`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: arithmetic -->
<!-- signatures: arithmetic(a, d, n) -->
### Function: arithmetic (a, d, n)

Devuelve el *n*-ésimo término de la progresión aritmética
`a, a + d, a + 2*d, ..., a + (n - 1)*d`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: arithsum -->
<!-- signatures: arithsum(a, d, n) -->
### Function: arithsum (a, d, n)

Devuelve la suma de la progresión aritmética desde hasta el *n*-ésimo término.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: collectterms -->
<!-- signatures: collectterms(expr, arg_1, ..., arg_n) -->
### Function: collectterms (expr, arg_1, ..., arg_n)

Si algunas expresiones fueron ya simplificadas con `facsum`, `factorfacsum`,
`factenexpand`,  `facexpten` o `factorfacexpten`, debiendo ser 
luego sumadas, puede ser conveniente combinarlas utilizando la función
`collecterms`, la cual admite como argumentos todos aquéllos que se
puedan pasar a las anteriormente citadas funciones, con la excepción de
`nextlayerfactor`, que no tiene efecto alguno sobre `collectterms`.
La ventaja de `collectterms` es que devuelve una forma similar a la de
`facsum`, pero debido a que suma expresiones que ya han sido previamente
procesadas, no necesita repetir esta operación, lo cual 
resulta ser especialmente útil cuando las expresiones a sumar son muy
grandes.

<!-- category: Simplification -->
<!-- keywords: combination -->
<!-- signatures: combination(n, r) -->
### Function: combination (n, r)

Calcula el número de combinaciones de *n* objetos
tomados de *r* en *r*.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: covers -->
<!-- signatures: covers(x) -->
### Function: covers (x)

Devuelve `1 - sin (x)`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: exsec -->
<!-- signatures: exsec(x) -->
### Function: exsec (x)

Devuelve `sec (x) - 1`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: facsum -->
<!-- signatures: facsum(expr, arg_1, ..., arg_n) -->
### Function: facsum (expr, arg_1, ..., arg_n)

Devuelve una expresión equivalente a *expr*, la cual
depende de los argumentos *arg_1*, ..., *arg_n*, y 
éstos pueden ser de cualquiera de las formas aceptables
para `ratvars`, o listas de estas formas. Si los
argumentos no son listas, la forma devuelta se expande
completamente con respecto de los argumentos, siendo los
coeficientes de tales argumentos factorizados. Estos
coeficientes no contienen a ninguno de los argumentos,
excepto quizás de una forma no racional.


En caso de que cualquiera de los argumentos sea una lista, entonces
todos ellos se combinan en una única lista, y en lugar de llamar
a `factor` para los coeficientes de los argumentos, `facsum`
se llama a sí misma utilizando esta nueva lista única
como lista de argumentos.


Es posible que se quiera utilizar `facsum` con respecto a
expresiones más complicadas, tales como `log (x + y)`. Estos
argumentos son también admisibles.


En ocasiones puede ser necesario obtener cualquiera de las formas
anteriores especificadas por sus operadores principales. Por ejemplo,
se puede querer aplicar `facsum` con respecto a todos los 
`log`; en este caso, se puede incluir entre los argumentos bien
los `log` específicos que se quieran tratar de esta
manera, bien la expresión `operator (log)` o `'operator (log)`.
Si se quiere aplicar `facsum` a *expr* con respecto a los 
operadores *op_1*, ..., *op_n*, se debe evaluar 
`facsum (expr, operator (op_1, ..., op_n))`.
La forma `operator` puede aparecer también dentro de las
listas de argumentos.


Además, dándole valores a las variables opcionales `facsum_combine`
y `nextlayerfactor` se puede controlar el resultado de `facsum`.

<!-- category: Simplification -->
<!-- keywords: facsum_combine -->
<!-- signatures: facsum_combine -->
### Variable: facsum_combine

Valor por defecto: `true`


La variable `facsum_combine` controla la forma del resultado final
devuelto por `facsum` si su argumento es un cociente de polinomios.
Si `facsum_combine` vale `false`, el resultado será una suma
completamente expandida, pero si vale `true`, la expresión devuelta
es un cociente de polinomios.

<!-- category: Simplification -->
<!-- keywords: factorfacsum -->
<!-- signatures: factorfacsum(expr, arg_1, ...arg_n) -->
### Function: factorfacsum (expr, arg_1, ...arg_n)

Devuelve una expresión equivalente a *expr* obtenida aplicando
`facsum` a los factores de *expr*, de argumentos
*arg_1*, ... *arg_n*. Si alguno de los factores de *expr* se 
eleva a una potencia, tanto el factor como el exponente se procesarán de
esta manera.

<!-- category: Simplification -->
<!-- keywords: gaussprob -->
<!-- signatures: gaussprob(x) -->
### Function: gaussprob (x)

Devuelve la función de densidad de probabilidad,
normal `%e^(-x^2/2) / sqrt(2*%pi)`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: gcdivide -->
<!-- signatures: gcdivide(p, q) -->
### Function: gcdivide (p, q)

Si la variable opcional `takegcd` vale `true`, que es su valor por defecto, 
`gcdivide` divide los polinomios *p* y *q* por su
máximo común divisor y devuelve el cociente de los resultados.
`gcdivide` hace una llamada a la función `ezgcd` para
dividir los polinomios por su máximo común divisor.


Si `takegcd` vale `false`, `gcdivide` devuelve
el cociente `p/q`.


Para hacer uso de esta función ejecutar `load("functs")`.


Véanse también  `ezgcd`, `gcd`, `gcdex` y
`poly_gcd`.


Ejemplos:



```maxima
(%i1) load("functs")$

(%i2) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o2)                6 x  + 19 x  + 19 x + 6
(%i3) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o3)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i4) gcdivide(p1, p2);
                             x + 1
(%o4)                        ------
                              3
                             x  + x
(%i5) takegcd:false;
(%o5)                         false
(%i6) gcdivide(p1, p2);
                       3       2
                    6 x  + 19 x  + 19 x + 6
(%o6)          ----------------------------------
                  5       4       3       2
               6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i7) ratsimp(%);
                             x + 1
(%o7)                        ------
                              3
                             x  + x
```

<!-- category: Simplification -->
<!-- keywords: gcfac -->
<!-- signatures: gcfac(expr) -->
### Function: gcfac (expr)

Es una función de factorización que intenta aplicar la misma heurística
que los humanos cuando tratan de hacer las expresiones más simples, limitándose
a la factorización de monomios. En caso de sumas, `gcfac` hace lo siguiente:



1. Factoriza los enteros.
2. Factoriza las potencias mayores de los términos que aparecen como
coeficientes, independientemente de su complejidad.
3. Utiliza (1) y (2) en la factorización de pares de términos adyacentes.
4. Aplica estas técnicas repetida y recursivamente hasta que la
expresión deje de sufrir cambios.


En general, el apartado (3) no hace una factorización óptima debido a la
naturaleza combinatoria y compleja de encontrar cuál de todas las ordenaciones
posibles de los pares da lugar a la expresión más compacta.


La instrucción `load ("scifac")` carga esta función y `demo (scifac)`
hace una demostración sobre su uso.

<!-- category: Simplification -->
<!-- keywords: gd -->
<!-- signatures: gd(x) -->
### Function: gd (x)

Devuelve la función de Gudermann,
`2*atan(%e^x)-%pi/2`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: geometric -->
<!-- signatures: geometric(a, r, n) -->
### Function: geometric (a, r, n)

Devuelve el *n*-ésimo término de la progresión geométrica
`a, a*r, a*r^2, ..., a*r^(n - 1)`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: geosum -->
<!-- signatures: geosum(a, r, n) -->
### Function: geosum (a, r, n)

Devuelve la suma de la sucesión geométrica hasta el *n*-ésimo término.
Si *n* es infinito (`inf`) la suma será finita sólo si el valor absoluto de 
*r* es menor que 1.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: harmonic -->
<!-- signatures: harmonic(a, b, c, n) -->
### Function: harmonic (a, b, c, n)

Devuelve el *n*-ésimo término de la progresión armónica
`a/b, a/(b + c), a/(b + 2*c), ..., a/(b + (n - 1)*c)`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: hav -->
<!-- signatures: hav(x) -->
### Function: hav (x)

Devuelve `(1 - cos(x))/2`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: nextlayerfactor -->
<!-- signatures: nextlayerfactor -->
### Variable: nextlayerfactor

Valor por defecto: `false`


Si `nextlayerfactor` vale `true`, las llamadas recursivas de
`facsum` se aplican a los factores de la forma factorizada de los
coeficientes de los argumentos.


Si vale `false`, `facsum` se aplica a cada coeficiente como
un todo cada vez que se efectúen llamadas recursivas a `facsum`.


La inclusión del átomo `nextlayerfactor` en la lista de 
argumentos de `facsum` tiene el mismo efecto que 
`nextlayerfactor: true`, pero *solamente* para el siguiente
nivel de la expresión. Puesto que `nextlayerfactor` toma
siempre uno de los valores `true` o  `false`, debe aparecer
comentado (comilla simple) cada vez que aparezca en la lista de 
argumentos de `facsum`.

<!-- category: Simplification -->
<!-- keywords: nonzeroandfreeof -->
<!-- signatures: nonzeroandfreeof(x, expr) -->
### Function: nonzeroandfreeof (x, expr)

Devuelve `true` si *expr* es diferente de cero y 
`freeof (x, expr)` devuelve `true`.
En caso contrario devuelve `false`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: permutation -->
<!-- signatures: permutation(n, r) -->
### Function: permutation (n, r)

Calcula el número de permutaciones de *r*, seleccionados
de un conjunto de *n*.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: reduce_consts -->
<!-- signatures: reduce_consts(expr) -->
### Function: reduce_consts (expr)

Sustituye subexpresiones constantes de *expr* por átomos,
guardando la definición de todos ellos en la lista de ecuaciones
 `const_eqns` y devolviendo el expresión *expr* ya
modificada. Se consideran partes constantes de *expr* aquellas
que devuelven `true` cuando se les aplica la función `constantp`,
por lo que antes de llamar a `reduce_consts` se debe ejecutar



```maxima
declare ([objetos a los que se quiera dar la propiedad de ser constantes], constant)$
```


para crear la base de datos de las cantidades constantes presentes en
la expresión.


Si se pretende generar código Fortran después de estos cálculos
simbólicos, una de las primeras secciones del código debe ser el
cálculo de las constantes. Para generar este segmento de código hacer



```maxima
map ('fortran, const_eqns)$
```


Junto a `const_eqns`, otras variables que afectan a `reduce_consts` son:


`const_prefix` (Valor por defecto: `xx`) es la cadena de caracteres utilizada como
prefijo para todos los símbolos generados por `reduce_consts` para
representar subexpresiones constantes.


`const_counter` (Valor por defecto: 1) es el índice entero utilizado
para generar los símbolos que representen a las subexpresiones
constantes encontradas por `reduce_consts`.


La instrucción `load ("rducon")` carga esta función y `demo (rducon)`
hace una demostración sobre su uso.

<!-- category: Simplification -->
<!-- keywords: rempart -->
<!-- signatures: rempart(expr, n) -->
### Function: rempart (expr, n)

Elimina la parte *n* de la expresión *expr*.


Si *n* es una lista de la forma `[l, m]`, entonces
las partes desde *l* a *m* serán eliminadas.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: sqrtdenest -->
<!-- signatures: sqrtdenest(expr) -->
### Function: sqrtdenest (expr)

Reduce expresiones en las que se encuentren raíces cuadradas anidadas,
siempre que sea posible


Ejemplo:








```maxima
(%i1) load ("sqdnst")$
(%i2) sqrt(sqrt(3)/2+1)/sqrt(11*sqrt(2)-12);
                                    sqrt(3)
                               sqrt(------- + 1)
                                       2
(%o2)                        ---------------------
                             sqrt(11 sqrt(2) - 12)
(%i3) sqrtdenest(%);
                                  sqrt(3)   1
                                  ------- + -
                                     2      2
(%o3)                            -------------
                                    1/4    3/4
                                 3 2    - 2
```


A veces conviene aplicar `sqrtdenest` más de una vez, como en el caso
`(19601-13860 sqrt(2))^(7/4)`.


La sentencia `load ("sqdnst")` carga esta función.

<!-- category: Simplification -->
<!-- keywords: tracematrix -->
<!-- signatures: tracematrix(M) -->
### Function: tracematrix (M)

Devuelve la traza (suma de los elementos de la diagonal) de la matriz *M*.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: vers -->
<!-- signatures: vers(x) -->
### Function: vers (x)

Devuelve `1 - cos (x)`.


Para hacer uso de esta función ejecutar `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: wronskian -->
<!-- signatures: wronskian([f_1, ..., f_n], x) -->
### Function: wronskian ([f_1, ..., f_n], x)

Devuelve la matriz wronskiana de las expresiones *f_1*, ..., *f_n*
dependeientes de la variable *x*.
El determinante de la matriz wronskiana es el determinante wronskiano de
la lista de expresiones.


Para hacer uso de esta función ejecutar `load("functs")`.


Ejemplo:







```maxima
(%i1) load("functs")$
(%i2) wronskian([f(x), g(x)],x);
(%o2) matrix([f(x),g(x)],['diff(f(x),x,1),'diff(g(x),x,1)])
```

