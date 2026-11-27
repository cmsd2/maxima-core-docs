## to_poly_solve

<!-- category: Solving -->
<!-- keywords: %and -->
<!-- signatures: %and -->
### Function: %and

El operador `%and` es una conjunción lógica. Maxima simplifica
una expresión `%and` a `true`, `false` o a una expresión
lógicamente equivalente, pero simplificada. El operador `%and`
es asociativo, conmutativo e idempotente. Así, cuando `%and`
devuelva una forma nominal, sus argumentos no serán redundantes; por ejemplo,



```maxima
(%i1) a %and (a %and b);
(%o1)                       a %and b
```


Si uno de los argumentos de la conjunción es la negación de otro argumento,
`%and` devuelve `false`:



```maxima
(%i2) a %and (not a);
 (%o2) false
```


Si cualquiera de los argumentos vale `false`, la conjunción devuelve
`false`, incluso cuando haya algún otro argumento que sea una
expresión no booleana; por ejemplo,



```maxima
(%i2) a %and (not a);
(%o2)                         false
```


Los argumentos de la expresión `%and` que sean inecuaciones se
reducen con la simplificación de Fourier; el método que se
aplica dispone de un pre-procesador que convierte algunas, pero no
todas, las inecuaciones no lineales a lineales. Por ejemplo, el
método de simplificación de Fourier simplifica `abs(x) + 1 > 0`
a `true`:



```maxima
(%i4) (x < 1) %and (abs(x) + 1 > 0);
(%o4)                         x < 1
```


**Notas**  


- * 
La variable opcional `prederror` no altera la
simplificación de las expresiones `%and`.
- * 
Para evitar errores en la precedencia de las operaciones,
se recomienda utilizar paréntesis en las expresiones combinadas
en las que aparezcan los operadores `%and`,  `%or` y `not` .
- * 
Los operadores `and` y `or`, tal como están
programados en Maxima, no conocen las propiedades asociativa
ni conmutativa.


**Limitaciones** La conjunción `%and` simplifica inecuaciones
*locamente*, no *globalmente*, lo que significa que conjunciones tales como



```maxima
(%i5) (x < 1) %and (x > 1);
(%o5)                 (x > 1) %and (x < 1)
```


*no* simplifican a `false`. Además, las rutinas de eliminación de Fourier
ignoran los hechos almacenados en la base de datos.



```maxima
(%i6) assume(x > 5);
(%o6)                        [x > 5]
(%i7) (x > 1) %and (x > 2);
(%o7)                 (x > 1) %and (x > 2)
```


Por último, las inecuaciones no lineales que no se puedan reducir de
manera sencilla a formas lineales, no se simplifican.


No está soportada la distributividad de `%and` respecto de `%or`,
ni la negación respecto de `%and`.


Para hacer uso de este operador, ejecútese `load("to_poly_solve")`.


Véanse también `%or`, `%if`, `and`, `or` y `not`.

<!-- category: Solving -->
<!-- keywords: %if -->
<!-- signatures: %if(bool, a, b) -->
### Function: %if (bool, a, b)

El operador `%if` es un condicional. La condición *bool*
debe tomar un valor lógico; cuando sea `true`, se devolverá
el segundo argumento, y cuando valga `false`, el segundo. En
cualquier otro caso, se obtiene una forma nominal.


En Maxima, las expresiones con desigualdades o igualdades no adquieren
valores lógicos; por ejemplo, $5 < 6$ no se simplifica a `true`,
ni $5 = 6$ `false`. Sin embargo, en la condición de una
sentencia `%if`, Maxima intenta determinar el valor lógico
de la expresión de forma automática. Véase un ejemplo:



```maxima
(%i1) f : %if(x # 1, 2, 8);
(%o1)                 %if(x - 1 # 0, 2, 8)
(%i2) [subst(x = -1,f), subst(x=1,f)];
(%o2)                        [2, 8]
```


Si en la condición aparece una inecuación, Maxima la
reduce con una simplificación de Fourier.


**Notas** 


- bullet 
Si la condición no se reduce a un valor lógico, Maxima devuelve
una forma nominal:

```maxima
(%i3) %if(42,1,2);
(%o3)                     %if(42, 1, 2)
```
- bullet 
El operador `if` de Maxima es n-ario, pero el operador `%if` no lo es.


Por último, las inecuaciones no lineales que no se puedan reducir de
manera sencilla a formas lineales, no se simplifican.


Para hacer uso de este operador, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: %or -->
<!-- signatures: %or -->
### Function: %or

El operador `%or` es una disyunción lógica. Maxima simplifica
una expresión `%or` a `true`, `false` o a una expresión
lógicamente equivalente, pero simplificada. El operador `%or`
es asociativo, conmutativo e idempotente. Así, cuando `%or`
devuelva una forma nominal, sus argumentos no serán redundantes; por ejemplo,



```maxima
(%i1) a %or (a %or b);
(%o1)                        a %or b
```


Si uno de los argumentos de la disyunción es la negación de otro argumento,
`%or` devuelve `true`:



```maxima
(%i2) a %or (not a);
(%o2)                         true
```


Si cualquiera de los argumentos vale `true`, la disyunción devuelve
`true`, incluso cuando haya algún otro argumento que sea una
expresión no booleana; por ejemplo,



```maxima
(%i3) 42 %or true;
(%o3)                         true
```


Los argumentos de la expresión `%or` que sean inecuaciones se
reducen con la simplificación de Fourier. Por ejemplo, el
método de simplificación de Fourier simplifica `abs(x) + 1 > 0`
a `true`:



```maxima
(%i4) (x < 1) %or (abs(x) + 1 > 0);
(%o4)                         true
```


**Notas**  


- * 
La variable opcional `prederror` no altera la
simplificación de las expresiones `%or`.
- * 
Para evitar errores en la precedencia de las operaciones,
se recomienda utilizar paréntesis en las expresiones combinadas
en las que aparezcan los operadores `%and`,  `%or` y `not` .
- * 
Los operadores `and` y `or`, tal como están
programados en Maxima, no conocen las propiedades asociativa
ni conmutativa.


**Limitaciones** La conjunción `%or` simplifica inecuaciones
*locamente*, no *globalmente*, lo que significa que disyunciones tales como



```maxima
(%i1) (x < 1) %or (x >= 1);
 (%o1) (x > 1) %or (x >= 1)
```


*no* simplifican a `true`. Además, las rutinas de eliminación de Fourier
ignoran los hechos almacenados en la base de datos.



```maxima
(%i2) assume(x > 5);
(%o2)                        [x > 5]
(%i3) (x > 1) %and (x > 2);
(%o3)                 (x > 1) %and (x > 2)
```


Por último, las inecuaciones no lineales que no se puedan reducir de
manera sencilla a formas lineales, no se simplifican.


No está soportada la distributividad de `%or` respecto de `%and`,
ni la negación respecto de `%or`.


Para hacer uso de este operador, ejecútese `load("to_poly_solve")`.


Véanse también `%and`, `%if`, `and`, `or` y `not`.

<!-- category: Solving -->
<!-- keywords: complex_number_p -->
<!-- signatures: complex_number_p(x) -->
### Function: complex_number_p (x)

La función `complex_number_p` devuelve `true` si su
argumento es de cualquiera de las formas `a + %i * b`, `a`, `%i b` o
`%i`, donde `a` y `b` son racionales o decimales en coma flotante,
de precisión doble o arbitraria (*bigfloats*); para cualesquiera otros argumentos,
`complex_number_p` devuelve `false`.


Ejemplo:



```maxima
(%i1) map('complex_number_p,[2/3, 2 + 1.5 * %i, %i]);
(%o1)                  [true, true, true]
(%i2) complex_number_p((2+%i)/(5-%i));
(%o2)                         false
(%i3) complex_number_p(cos(5 - 2 * %i));
(%o3)                         false
```


Véase también `isreal_p`.


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: compose_functions -->
<!-- signatures: compose_functions(l) -->
### Function: compose_functions (l)

La función `compose_functions(l)` devuelve una expresión lambda
que es la composición de las funciones presentes en la lista *l*.
Las funciones se aplican de derecha a izquierda.


Ejemplo:



```maxima
(%i1) compose_functions([cos, exp]);
                                        %g151
(%o1)             lambda([%g151], cos(%e     ))
(%i2) %(x);
                                  x
(%o2)                       cos(%e )
```


Si la lista está vacía devuelve la función identidad:



```maxima
(%i3) compose_functions([]);
(%o3)                lambda([%g152], %g152)
(%i4)  %(x);
(%o4)                           x
```


**Notas** 


- * 
Cuando Maxima detecta que un miembro de la lista no es un
símbolo o expresión lambda, la función 
`funmake` (no `compose_functions`) muestra un mensaje de
error:

```maxima
(%i5) compose_functions([a < b]);
funmake: first argument must be a symbol, subscripted symbol,
string, or lambda expression; found: a < b
#0: compose_functions(l=[a < b])(to_poly_solve.mac line 40)
 -- an error. To debug this try: debugmode(true);
```
- * 
Para evitar conflictos de nombres, la variable independiente se determina
con la función `new_variable`:

```maxima
(%i6) compose_functions([%g0]);
(%o6)              lambda([%g154], %g0(%g154))
(%i7) compose_functions([%g0]);
(%o7)              lambda([%g155], %g0(%g155))
```
Aunque las variables dependientes sean diferentes, Maxima es capaz de
determinar que las expresiones lambda son semánticamente equivalentes:

```maxima
(%i8) is(equal(%o6,%o7));
(%o8)                         true
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: dfloat -->
<!-- signatures: dfloat(x) -->
### Function: dfloat (x)

La función `dfloat` es similar a `float`, pero `dfloat` 
aplica `rectform` cuando `float` no puede evaluar a un número
decimal de coma flotante de doble precisión. Ejemplo:



```maxima
(%i1) float(4.5^(1 + %i));
                               %i + 1
(%o1)                       4.5
(%i2) dfloat(4.5^(1 + %i));
(%o2)        4.48998802962884 %i + .3000124893895671
```


**Notas** 



- * 
La forma rectangular de una expresión puede no ser la
más adecuada para cálculos numéricos
- * 
El identificador `float` es al mismo tiempo una variable opcional,
cuyo valor por defecto es `false` y el nombre de una función.


Véanse también `float` y `bfloat`.


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: elim -->
<!-- signatures: elim(l, x) -->
### Function: elim (l, x)

La función `elim` elimina las variables que se indican en el conjunto
o lista `x` del conjunto o lista de ecuaciones en `l`. Cada
elemento de `x` debe ser un símbolo, mientras que los
elementos de `l` pueden ser ecuaciones o expresiones que se suponen
igualadas a cero.


La función `elim` devuelve una lista formada por dos listas; la
primera está formada por las expresiones con las variables eliminadas y
la segunda es la lista de pivotes o, en otras palabras, es la lista de
expresiones que `elim` ha utilizado para proceder con la eliminación.


Ejemplo:


Eliminación entre ecuaciones lineales. Eliminando `x` e `y`
se obtiene una única ecuación `2 z - 7 = 0`; las ecuaciones
`y + 7 = 0` y `z - z + 1 = 1` se han utilizado como pivotes.



```maxima
(%i1) elim(set(x + y + z = 1, x - y  - z = 8, x - z = 1), 
           set(x,y));
(%o1)            [[2 z - 7], [y + 7, z - x + 1]]
```


Eliminando las tres variables de estas ecuaciones se triangulariza el sistema
lineal:



```maxima
(%i2) elim(set(x + y + z = 1, x - y  - z = 8, x - z = 1),
           set(x,y,z));
(%o2)           [[], [2 z - 7, y + 7, z - x + 1]]
```


Las ecuaciones no necesitan ser lineales:



```maxima
(%i3) elim(set(x^2 - 2 * y^3 = 1,  x - y = 5), [x,y]);
                     3    2
(%o3)       [[], [2 y  - y  - 10 y - 24, y - x + 5]]
```


El usuario no puede controlar el orden en el que se eliminan las
variables. El algoritmo utiliza una heurística con
la que intenta escoger el mejor pivote y el mejor orden de eliminación.


**Notas** 



- * 
Al contrario que la función relacionada `eliminate`, la
función `elim` no llama a la función `solve` cuando el
número de ecuaciones iguala al de variables.
- * 
La función `elim` trabaja aplicando resultantes; la variable
opcional `resultant` determina qué algoritmo va a utilizar Maxima.
Con `sqfr`, Maxima factoriza cada resultante y suprime ceros múltiples.
- * 
`elim` triangulariza un conjunto de ecuaciones polinómicas no
lineales; el conjunto solución del conjunto triangularizado puede ser mayor
que el conjunto de soluciones del conjunto no triangularizado, por lo que
las ecuaciones triangularizadas pueden tener soluciones falsas.


Véanse también `elim_allbut`, `eliminate_using`, `eliminate`
y `resultant`.


Para hacer uso de esta función, ejecútese `load("to_poly")`.

<!-- category: Solving -->
<!-- keywords: elim_allbut -->
<!-- signatures: elim_allbut(l, x) -->
### Function: elim_allbut (l, x)

Es similar a `elim`, excepto por el hecho de que elimina todas las variables
que aparecen en la lista de ecuaciones `l` que no están en `x`.


Ejemplo:



```maxima
(%i1) elim_allbut([x+y = 1, x - 5*y = 1],[]);
(%o1)                 [[], [y, y + x - 1]]
(%i2) elim_allbut([x+y = 1, x - 5*y = 1],[x]);
(%o2)                [[x - 1], [y + x - 1]]
```


Para hacer uso de esta función, ejecútese `load("to_poly")`.


Véanse también `elim`, `eliminate_using`, `eliminate`
y `resultant`.

<!-- category: Solving -->
<!-- keywords: eliminate_using -->
<!-- signatures: eliminate_using(l, e, x) -->
### Function: eliminate_using (l, e, x)

Elmina el símbolo `x` de la lista o conjunto de ecuaciones
`l` haciendo uso del pivote `e`.


Ejemplos:



```maxima
(%i1) eq : [x^2 - y^2 - z^3 , x*y - z^2 - 5, x - y + z];
               3    2    2     2
(%o1)      [- z  - y  + x , - z  + x y - 5, z - y + x]
(%i2) eliminate_using(eq,first(eq),z);
        3              2      2      3    2
(%o2) {y  + (1 - 3 x) y  + 3 x  y - x  - x , 
                        4    3  3       2  2             4
                       y  - x  y  + 13 x  y  - 75 x y + x  + 125}
(%i3) eliminate_using(eq,second(eq),z);
        2            2       4    3  3       2  2             4
(%o3) {y  - 3 x y + x  + 5, y  - x  y  + 13 x  y  - 75 x y + x
                                                           + 125}
(%i4) eliminate_using(eq, third(eq),z);
        2            2       3              2      2      3    2
(%o4) {y  - 3 x y + x  + 5, y  + (1 - 3 x) y  + 3 x  y - x  - x }
```


Para hacer uso de esta función, ejecútese `load("to_poly")`.


Véanse también `elim`, `elim_allbut`, `eliminate`
y `resultant`.

<!-- category: Solving -->
<!-- keywords: fourier_elim -->
<!-- signatures: fourier_elim([eq1, eq2, ...], [var1, var, ...]) -->
### Function: fourier_elim ([eq1, eq2, ...], [var1, var, ...])

La instrucción `fourier_elim([eq1,eq2,...], [var1,var2,...]` aplica el
algoritmo de eliminación de Fourier para resolver el sistema de inecuaciones 
lineales `[eq1,eq2,...]` respecto de las variables `[var1,var2,...]`.


Ejemplos:



```maxima
(%i1) fourier_elim([y-x < 5, x - y < 7, 10 < y],[x,y]);
(%o1)            [y - 5 < x, x < y + 7, 10 < y]
(%i2) fourier_elim([y-x < 5, x - y < 7, 10 < y],[y,x]);
(%o2)        [max(10, x - 7) < y, y < x + 5, 5 < x]
```


Eliminando primero respecto de $x$ y luego respecto de $y$,
se obtienen límites inferior y superior para $x$
que dependen de $y$, y límites numéricos para $y$.
Si se eliminan en orden inverso, se obtienen los límites
de $y$ en función de $x$, y los de $x$ son números.


De ser necesario, `fourier_elim` devuelve una disyunción de listas
de ecuaciones:



```maxima
(%i3) fourier_elim([x # 6],[x]);
(%o3)                  [x < 6] or [6 < x]
```


Si no existe solución, `fourier_elim` devuelve `emptyset`,
y si la solución son todos los reales, `fourier_elim` devuelve 
`universalset`:



```maxima
(%i4) fourier_elim([x < 1, x > 1],[x]);
(%o4)                       emptyset
(%i5) fourier_elim([minf < x, x < inf],[x]);
(%o5)                     universalset
```


En caso de que las inecuaciones no sean lineales, `fourier_elim`
devuelve una lista de inecuaciones simplificadas:



```maxima
(%i6) fourier_elim([x^3 - 1 > 0],[x]);
               2                             2
(%o6) [1 < x, x  + x + 1 > 0] or [x < 1, - (x  + x + 1) > 0]
(%i7) fourier_elim([cos(x) < 1/2],[x]);
(%o7)                  [1 - 2 cos(x) > 0]
```


En lugar de una lista de inecuaciones, el primer argumento pasado a
`fourier_elim` puede ser una conjunción o disyunción lógica.



```maxima
(%i8) fourier_elim((x + y < 5) and (x - y >8),[x,y]);
                                              3
(%o8)            [y + 8 < x, x < 5 - y, y < - -]
                                              2
(%i9) fourier_elim(((x + y < 5) and x < 1) or  (x - y >8),[x,y]);
(%o9)          [y + 8 < x] or [x < min(1, 5 - y)]
```


La función `fourier_elim` soporta los operadores de desigualdad 
`<`, `<=`, `>`, `>=`, `#` y `=`.


La rutina de eliminación de Fourier dispone de un preprocesador que
convierte algunas inecuaciones no lineales formadas con las funciones
del valor absoluto, mínimo y máximo a inecuaciones 
lineales. Además, el preprocesador admite algunas expresiones 
que son productos o cocientes de términos lineales:



```maxima
(%i10) fourier_elim([max(x,y) > 6, x # 8, abs(y-1) > 12],[x,y]);
(%o10) [6 < x, x < 8, y < - 11] or [8 < x, y < - 11]
 or [x < 8, 13 < y] or [x = y, 13 < y] or [8 < x, x < y, 13 < y]
 or [y < x, 13 < y]
(%i11) fourier_elim([(x+6)/(x-9) <= 6],[x]);
(%o11)           [x = 12] or [12 < x] or [x < 9]
(%i12) fourier_elim([x^2 - 1 # 0],[x]);
(%o12)      [- 1 < x, x < 1] or [1 < x] or [x < - 1]
```


Para hacer uso de esta función, ejecútese `load("fourier_elim")`.

<!-- category: Solving -->
<!-- keywords: isreal_p -->
<!-- signatures: isreal_p(e) -->
### Function: isreal_p (e)

El predicado `isreal_p` devuelve `true` si `e` representa un
número real y `false` si no representa un punto de la recta; en cualquier
otro caso devuelve una forma nominal.



```maxima
(%i1) map('isreal_p, [-1, 0, %i, %pi]);
(%o1)               [true, true, false, true]
```


Las variables de Maxima se interpretan como números reales:



```maxima
(%i2) isreal_p(x);
(%o2)                         true
```


La función `isreal_p` consulta los hechos almacenados en la base de datos:


```maxima
(%i3) declare(z,complex)$

(%i4) isreal_p(z);
(%o4)                      isreal_p(z)
```


Con frecuencia, `isreal_p` devuelve una forma nominal cuando debería
devolver `false`; por ejemplo, la función logarítmica no toma valores
reales en toda la recta real, por lo que  `isreal_p(log(x))` debería
devolver `false`, sin embargo:



```maxima
(%i5) isreal_p(log(x));
(%o5)                   isreal_p(log(x))
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.


Véase también `complex_number_p`.


La función `isreal_p` es experimental; sus
especificaciones pueden cambiar y su funcionalidad puede incorporarse a otras funciones
de Maxima.

<!-- category: Solving -->
<!-- keywords: new_variable -->
<!-- signatures: new_variable(type) -->
### Function: new_variable (type)

Devuelve un símbolo de la forma `%[z,n,r,c,g]k`,
siendo `k` un número entero. Los valores admisibles para *type*
son `integer`, `natural_number`, `real`, `natural_number`
y `general`. Por número natural se entiende *entero negativo*, de 
manera que el ceero es un número natural.


Cuando *type* no es de ninguno de los tipos indicados más arriba,
*type* toma por defecto el valor `general`. Para enteros, números
naturales y números complejos, Maxima añade esta información a la base de
datos de forma automática.



```maxima
(%i1) map('new_variable,
          ['integer, 'natural_number, 'real, 'complex, 'general]);
(%o1)          [%z144, %n145, %r146, %c147, %g148]
(%i2) nicedummies(%);
(%o2)               [%z0, %n0, %r0, %c0, %g0]
(%i3) featurep(%z0, 'integer);
(%o3)                         true
(%i4) featurep(%n0, 'integer);
(%o4)                         true
(%i5) is(%n0 >= 0);
(%o5)                         true
(%i6) featurep(%c0, 'complex);
(%o6)                         true
```


Es recomendable que al argumento de `new_variable` se le
aplique el operador de comilla simple para evitar su evaluación,
de esta manera se evitan errores como el siguiente:



```maxima
(%i7) integer : 12$

(%i8) new_variable(integer);
(%o8)                         %g149
(%i9) new_variable('integer);
(%o9)                         %z150
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.


Véase también `nicedummies`.

<!-- category: Solving -->
<!-- keywords: nicedummies -->
<!-- signatures: nicedummies -->
### Function: nicedummies

La función `nicedummies` reescribe los índices,
comenzando por cero, de las variables de una expresión qua hayan
sido introducidas por `new_variable`:



```maxima
(%i1) new_variable('integer) + 52 * new_variable('integer);
(%o1)                   52 %z136 + %z135
(%i2) new_variable('integer) - new_variable('integer);
(%o2)                     %z137 - %z138
(%i3) nicedummies(%);
(%o3)                       %z0 - %z1
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.


Véase también `new_variable`.

<!-- category: Solving -->
<!-- keywords: parg -->
<!-- signatures: parg(x) -->
### Function: parg (x)

La función `parg` es una versión con capacidades simplificadoras
de la función de argumento complejo `carg`:



```maxima
(%i1) map('parg,[1,1+%i,%i, -1 + %i, -1]);
                        %pi  %pi  3 %pi
(%o1)               [0, ---, ---, -----, %pi]
                         4    2     4
```


Si el argumento pasado a la función `parg` no es una constante,
se devolverá una forma nominal:



```maxima
(%i2) parg(x + %i * sqrt(x));
(%o2)                 parg(x + %i sqrt(x))
```


Si `sign` detecta que la entrada es un número real negativo o
positivo, `parg` devuelve una forma no nominal aunque la entrada
no sea una constante:



```maxima
(%i3) parg(abs(x));
(%o3) 0
(%i4) parg(-x^2-1);
(%o4)                          %pi
```


La función `sign` suele ignorar las variables declaradas complejas
(`declare(x,complex)`); en tales casos, `parg`
puede retornar valores incorrectos:



```maxima
(%i1) declare(x,complex)$

(%i2) parg(x^2 + 1);
(%o2) 0
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.


Véanse también `carg`, `isreal_p`.

<!-- category: Solving -->
<!-- keywords: real_imagpart_to_conjugate -->
<!-- signatures: real_imagpart_to_conjugate(e) -->
### Function: real_imagpart_to_conjugate (e)

La función `real_imagpart_to_conjugate` reemplaza todas las
llamadas a `realpart` y `imagpart` presentes en una expresión 
por llamadas a `conjugate`, obteniendo otra expresión equivalente:



```maxima
(%i1) declare(x, complex)$

(%i2) real_imagpart_to_conjugate(realpart(x) +  imagpart(x) = 3);
          conjugate(x) + x   %i (x - conjugate(x))
(%o2)     ---------------- - --------------------- = 3
                 2                     2
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: rectform_log_if_constant -->
<!-- signatures: rectform_log_if_constant(e) -->
### Function: rectform_log_if_constant (e)

La función `rectform_log_if_constant` convierte todos los términos
de la forma `log(c)` a `rectform(log(c))`, siendo `c` 
una expresión constante o declarada como tal.



```maxima
(%i1) rectform_log_if_constant(log(1-%i) - log(x - %i));
                                 log(2)   %i %pi
(%o1)            - log(x - %i) + ------ - ------
                                   2        4
(%i2) declare(a,constant, b,constant)$

(%i3) rectform_log_if_constant(log(a + %i*b));
                       2    2
                  log(b  + a )
(%o3)             ------------ + %i atan2(b, a)
                       2
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: simp_inequality -->
<!-- signatures: simp_inequality(e) -->
### Function: simp_inequality (e)

La función `simp_inequality` aplica ciertas simplificaciones
a conjunciones y disyunciones de inecuaciones.


**Limitaciones** La función `simp_inequality` está limitada en
al menos dos aspectos; en primer lugar, las simplificaciones son locales:



```maxima
(%i1) simp_inequality((x > minf) %and (x < 0));
(%o2) (x>1) %and (x<1)
```


En segundo lugar, `simp_inequality` no tiene en cuenta los hechos de la
base de datos:



```maxima
(%i2) assume(x > 0)$

(%i3) simp_inequality(x > 0);
(%o3)                         x > 0
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: standardize_inverse_trig -->
<!-- signatures: standardize_inverse_trig(e) -->
### Function: standardize_inverse_trig (e)

Esta función aplica las identidades `cot(x) = atan(1/x)` y
`acsc(x) = asin(1/x)` y similares con `asec`, `acoth`
y `acsch`. Consúltese Abramowitz y Stegun, ecuaciones
4.4.6 a 4.4.8 y 4.6.4 a 4.6.6.


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.

<!-- category: Solving -->
<!-- keywords: subst_parallel -->
<!-- signatures: subst_parallel(l, e) -->
### Function: subst_parallel (l, e)

Dada la ecuación o lista de ecuaciones *l* y la expresión
*e*, sustituye *en paralelo* en *e* los miembros izquierdos
de las ecuaciones por los derechos:



```maxima
(%i1) load("to_poly_solve")$

(%i2) subst_parallel([x=y,y=x], [x,y]);
(%o2)                        [y, x]
```


Compárese el resultado anterior con las sustituciones hechas en serie: 



```maxima
(%i3) subst([x=y,y=x],[x,y]);
(%o3)                        [x, x]
```


La función `subst_parallel` es similar a `sublis`, excepto por
el hecho de que `subst_parallel` permite la sustitución de expresiones
no atómicas:



```maxima
(%i4) subst_parallel([x^2 = a, y = b], x^2 * y);
(%o4)                          a b
(%i5) sublis([x^2 = a, y = b], x^2 * y);

                                                             2
sublis: left-hand side of equation must be a symbol; found: x
 -- an error. To debug this try: debugmode(true);
```


Las sustituciones hechas por `subst_parallel` son literales, no semánticas,
por lo que `subst_parallel` no reconoce que $x * y$ sea una subexpresión
de $x^2 * y$:



```maxima
(%i6) subst_parallel([x * y = a], x^2 * y);
                               2
(%o6)                         x  y
```


La función `subst_parallel` realiza todas las sustituciones
antes de proceder a la simplificación, lo que permite sustituciones
en expresiones condicionales que podrín producir 
errores en caso de simplificar antes de sustituir:



```maxima
(%i7) subst_parallel([x = 0], %if(x < 1, 5, log(x)));
(%o7)                           5
(%i8) subst([x = 0], %if(x < 1, 5, log(x)));

log: encountered log(0).
 -- an error. To debug this try: debugmode(true);
```


Para hacer uso de esta función, ejecútese `load("to_poly_solve_extra.lisp")`.


Véanse también `subst`, `sublis` y `ratsubst`.

<!-- category: Solving -->
<!-- keywords: to_poly -->
<!-- signatures: to_poly(e, l) -->
### Function: to_poly (e, l)

La función `to_poly` intenta convertir la ecuación *e*
en un sistema de polinomios, junto con restricciones en forma de
desigualdades. Las soluciones del sistema polinómico que cumplan
las restricciones son, a su vez, las soluciones de la ecuación *e*.
Dicho de manera informal, `to_poly` intenta pasar a forma de
polinomio la ecuación *e*; un ejemplo ayudará a aclarar su
comportamiento:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly(sqrt(x) = 3, [x]);
                            2
(%o2) [[%g130 - 3, x = %g130 ], 
                      %pi                               %pi
                   [- --- < parg(%g130), parg(%g130) <= ---], []]
                       2                                 2
```


Las condiciones `-%pi/2<parg(%g130),parg(%g130)<=%pi/2` dicen que
`%g130` está en el rango de la función radical; cuando eso se
cumpla, el conjunto de ecuaciones de `sqrt(x) = 3` coincide con
el de `%g130-3,x=%g130^2`.


Para convertir a forma polinómica una expresión trigonométrica,
es necesario introducir una sustitución no algebraica; tal sustitución
se devuelve en la tercera lista de la respuesta de `to_poly`:



```maxima
(%i3) to_poly(cos(x),[x]);
                2                                 %i x
(%o3)    [[%g131  + 1], [2 %g131 # 0], [%g131 = %e    ]]
```


Los términos constantes no se transforman a polinomios a menos que el
número uno se introduzca en la lista de variables:



```maxima
(%i4) to_poly(x = sqrt(5),[x]);
(%o4)                [[x - sqrt(5)], [], []]
(%i5) to_poly(x = sqrt(5),[1,x]);
                            2
(%o5) [[x - %g132, 5 = %g132 ], 
                      %pi                               %pi
                   [- --- < parg(%g132), parg(%g132) <= ---], []]
                       2                                 2
```


Para generar un polinomio que tenga $sqrt(5) + sqrt(7)$ como
raíz puede hacerse lo siguiente:



```maxima
(%i6) first(elim_allbut(first(to_poly(x = sqrt(5) + sqrt(7),
                                      [1,x])), [x]));
                          4       2
(%o6)                   [x  - 24 x  + 4]
```


Para hacer uso de esta función, ejecútese `load("to_poly")`.


Véase también `to_poly_solve`.

<!-- category: Solving -->
<!-- keywords: to_poly_solve -->
<!-- signatures: to_poly_solve(e, l, [options]) -->
### Function: to_poly_solve (e, l, [options])

La función `to_poly_solve` intenta resolver las ecuaciones *e*
de incógnitas *l*. El argumento *e* puede ser una única ecuación,
o una lista o conjunto de ecuaciones; de forma similar, *l* puede ser un
símbolo o una lista o conjunto de símbolos. Cuando
uno de los elementos de *e* no sea una igualdad, como $x^2 -1$,
se supodrá que es igual a cero.


La estrategia básica de `to_poly_solve` consiste en convertir la entrada en un
polinomio y luego invocar a la función `algsys`. Internamente,  `to_poly_solve`
asigna a `algexact` el valor `true`. Para cambiar el valor de `algexact`,
debe anñadirse `'algexact=false` a la lista de argumentos de `to_poly_solve`.


Cuando `to_poly_solve` consigue determinar el conjunto de soluciones, cada
miembro del conjunto de soluciones es una lista en un objeto  `%union`:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly_solve(x*(x-1) = 0, x);
(%o2)               %union([x = 0], [x = 1])
```


Cuando `to_poly_solve` es incapaz de determinar el conjunto de soluciones,
devuelve una forma nominal de `%solve` y muestra un mensaje de aviso:



```maxima
(%i3) to_poly_solve(x^k + 2* x + 1 = 0, x);

Nonalgebraic argument given to 'to_poly'
unable to solve
                          k
(%o3)            %solve([x  + 2 x + 1 = 0], [x])
```


A veces se puede obtener la solución haciendo una sustitución en `%solve`:



```maxima
(%i4) subst(k = 2, %);
(%o4)                   %union([x = - 1])
```


Especialmente en el caso de las funciones trigonométricas, los resultados pueden
incorporar números enteros arbitrarios de la forma `%zXXX`, siendo `XXX`
un índice entero:



```maxima
(%i5) to_poly_solve(sin(x) = 0, x);
(%o5)   %union([x = 2 %pi %z33 + %pi], [x = 2 %pi %z35])
```


Para inicializar los índices, hágase uso de `nicedummies`:



```maxima
(%i6) nicedummies(%);
(%o6)    %union([x = 2 %pi %z0 + %pi], [x = 2 %pi %z1])
```


En ocasiones, se introducen números complejos arbitrarios de la forma
`%cXXX`, o reales de la forma `%rXXX`. La función `nicedummies`
inicializa estos identificadores a cero.


También a veces, la solución incorpora versiones simplificadas de los
operadores lógicos `%and`, `%or` y `%if`, que representan, respectivamente,
la conjunción, la disyunción y la implicación:



```maxima
(%i7) sol : to_poly_solve(abs(x) = a, x);
(%o7) %union(%if(isnonnegative_p(a), [x = - a], %union()), 
                      %if(isnonnegative_p(a), [x = a], %union()))
(%i8) subst(a = 42, sol);
(%o8)             %union([x = - 42], [x = 42])
(%i9) subst(a = -42, sol);
(%o9)                       %union()
```


El conjunto vacío se representa por `%union`.


La función `to_poly_solve` es capaz de resolver algunas ecuaciones
con potencias racionales, potencias no racionales, valores absolutos, funciones
trigonométricas y funciones del mínimo y del máximo. 
También puede resolver algunas ecuaciones resolubles en términos de la
función W de Lambert:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly_solve(set(max(x,y) = 5, x+y = 2), set(x,y));
(%o2)      %union([x = - 3, y = 5], [x = 5, y = - 3])
(%i3) to_poly_solve(abs(1-abs(1-x)) = 10,x);
(%o3)             %union([x = - 10], [x = 12])
(%i4) to_poly_solve(set(sqrt(x) + sqrt(y) = 5, x + y = 10),
                    set(x,y));
                     3/2               3/2
                    5    %i - 10      5    %i + 10
(%o4) %union([x = - ------------, y = ------------], 
                         2                 2
                                3/2                 3/2
                               5    %i + 10        5    %i - 10
                          [x = ------------, y = - ------------])
                                    2                   2
(%i5) to_poly_solve(cos(x) * sin(x) = 1/2,x,
                    'simpfuncs = ['expand, 'nicedummies]);
                                         %pi
(%o5)              %union([x = %pi %z0 + ---])
                                          4
(%i6) to_poly_solve(x^(2*a) + x^a + 1,x);
                                        2 %i %pi %z81
                                        -------------
                                  1/a         a
                  (sqrt(3) %i - 1)    %e
(%o6) %union([x = -----------------------------------], 
                                  1/a
                                 2
                                                  2 %i %pi %z83
                                                  -------------
                                            1/a         a
                          (- sqrt(3) %i - 1)    %e
                     [x = -------------------------------------])
                                           1/a
                                          2
(%i7) to_poly_solve(x * exp(x) = a, x);
(%o7)              %union([x = lambert_w(a)])
```


En el caso de inecuaciones lineales, `to_poly_solve` aplica automáticamente
la eliminación de Fourier:



```maxima
(%i8) to_poly_solve([x + y < 1, x - y >= 8], [x,y]);
                               7
(%o8) %union([x = y + 8, y < - -], 
                               2
                                                              7
                                 [y + 8 < x, x < 1 - y, y < - -])
                                                              2
```


Los argumentos opcionales deben tener forma de ecuación; generalmente, el orden
de estas opciones no reviste importancia.



- * 
`simpfuncs = l`, siendo `l` una lista de funciones,
aplica la composición de los elementos de `l` a cada solución:

```maxima
(%i1) to_poly_solve(x^2=%i,x);
                               1/4             1/4
(%o1)       %union([x = - (- 1)   ], [x = (- 1)   ])
(%i2) to_poly_solve(x^2= %i,x, 'simpfuncs = ['rectform]);
                      %i         1             %i         1
(%o2) %union([x = - ------- - -------], [x = ------- + -------])
                    sqrt(2)   sqrt(2)        sqrt(2)   sqrt(2)
```

A veces, una simplificación puede anular una simplificación anterior:

```maxima
(%i3) to_poly_solve(x^2=1,x);
(%o3)              %union([x = - 1], [x = 1])
(%i4) to_poly_solve(x^2= 1,x, 'simpfuncs = [polarform]);
                                        %i %pi
(%o4)            %union([x = 1], [x = %e      ]
```

Maxima no comprueba que los elementos de la lista de funciones `l` sean
todos simplificaciones:

```maxima
(%i5) to_poly_solve(x^2 = %i,x, 'simpfuncs = [lambda([s],s^2)]);
(%o5)                   %union([x = %i])
```

Para convertir cada solución a real de doble precisión hágase uso de
`simpfunc = ['dfloat]`:

```maxima
(%i6) to_poly_solve(x^3 +x + 1 = 0,x, 
                    'simpfuncs = ['dfloat]), algexact : true;
(%o6) %union([x = - .6823278038280178], 
[x = .3411639019140089 - 1.161541399997251 %i], 
[x = 1.161541399997251 %i + .3411639019140089])
```
- * 
Con la opción `use_grobner = true` se aplica la función 
`poly_reduced_grobner` a las ecuaciones antes de intentar resolverlas.
En primer lugar, esta opción proporciona una manera de soslayar algunas
debilidades de la función `algsys`:

```maxima
(%i7) to_poly_solve([x^2+y^2=2^2,(x-1)^2+(y-1)^2=2^2],[x,y],
                    'use_grobner = true);
                    sqrt(7) - 1      sqrt(7) + 1
(%o7) %union([x = - -----------, y = -----------], 
                         2                2
                                 sqrt(7) + 1        sqrt(7) - 1
                            [x = -----------, y = - -----------])
                                      2                  2
(%i8) to_poly_solve([x^2+y^2=2^2,(x-1)^2+(y-1)^2=2^2],[x,y]);
(%o8)                       %union()
```
- * 
`maxdepth = k`, siendo `k` un positivo entero, controla el nivel
de recursión. El valor por defecto es cinco. Cuando se excede el nivel de recursión
se obtiene un mensaje de error:

```maxima
(%i9) to_poly_solve(cos(x) = x,x, 'maxdepth = 2);
Unable to solve
Unable to solve
(%o9)        %solve([cos(x) = x], [x], maxdepth = 2)
```
- * 
Con `parameters = l`, siendo `l` una lista de símbolos,
el programa intenta encontrar una solución válida para todos los miembros de la
lista `l`:

```maxima
(%i10) to_poly_solve(a * x = x, x);
(%o10)                   %union([x = 0])
(%i11) to_poly_solve(a * x = x, x, 'parameters = [a]);
(%o11) %union(%if(a - 1 = 0, [x = %c111], %union()), 
                               %if(a - 1 # 0, [x = 0], %union()))
```
En `(%o2)`, el programa introduce una variable ficticia; para reinicializarla,
úsese la función `nicedummies`:

```maxima
(%i12) nicedummies(%);
(%o12) %union(%if(a - 1 = 0, [x = %c0], %union()), 
                               %if(a - 1 # 0, [x = 0], %union()))
```


`to_poly_solve` utiliza información almacenada en el array `one_to_one_reduce`
para resolver ecuaciones de la forma  $f(a) = f(b)$. La asignación 
`one_to_one_reduce['f,'f] : lambda([a,b], a=b)` le dice a `to_poly_solve`
que el conjunto de soluciones de $f(a) = f(b)$ es igual al conjunto de soluciones
de $a=b$:


```maxima
(%i13) one_to_one_reduce['f,'f] : lambda([a,b], a=b)$

(%i14) to_poly_solve(f(x^2-1) = f(0),x);
(%o14)             %union([x = - 1], [x = 1])
```


De forma más general, la asignación 
`one_to_one_reduce['f,'g] : lambda([a,b], w(a,b)=0` le indica a
`to_poly_solve` que el cojunto de soluciones de $f(a) = f(b)$ 
es igual al conjunto de soluciones de $w(a,b) = 0$:


```maxima
(%i15) one_to_one_reduce['f,'g] : lambda([a,b], a = 1 + b/2)$

(%i16) to_poly_solve(f(x) - g(x),x);
(%o16)                   %union([x = 2])
```


Además, `to_poly_solve` utiliza información almacenada en el array
`function_inverse` para resolver ecuaciones de la forma $f(a) = b$.
La asignación `function_inverse['f] : lambda([s], g(s))` le dice a
`to_poly_solve` que el conjunto de soluciones de $f(x) = b$ es
igual al conjunto de soluciones de $x = g(b)$:


```maxima
(%i17) function_inverse['Q] : lambda([s], P(s))$

(%i18) to_poly_solve(Q(x-1) = 2009,x);
(%o18)              %union([x = P(2009) + 1])
(%i19) function_inverse['G] : lambda([s], s+new_variable(integer));
(%o19)       lambda([s], s + new_variable(integer))
(%i20) to_poly_solve(G(x - a) = b,x);
(%o20)             %union([x = b + a + %z125])
```


**Notas**



- * 
Las incógnitas a resolver no necesitan ser símbolos, lo cual es
cierto cuando `fullratsubst` es capaz de hacer las sustituciones de forma apropiadas:

```maxima
(%i1) to_poly_solve([x^2 + y^2 + x * y = 5, x * y = 8],
                    [x^2 + y^2, x * y]);
                                  2    2
(%o1)           %union([x y = 8, y  + x  = - 3])
```
- * 
Cuando las ecuaciones involucran conjugados de complejos, el programa
añade automáticamente las ecuaciones conjugadas:

```maxima
(%i1) declare(x,complex)$
(%i2) to_poly_solve(x + (5 + %i) * conjugate(x) = 1, x);
                                   %i + 21
(%o2)              %union([x = - -----------])
                                 25 %i - 125
(%i3) declare(y,complex)$
(%i4) to_poly_solve(set(conjugate(x) - y = 42 + %i,
                        x + conjugate(y) = 0), set(x,y));
                           %i - 42        %i + 42
(%o4)        %union([x = - -------, y = - -------])
                              2              2
```
- * 
Cuando las funciones involucran valores absolutos, `to_poly_solve`
consulta los hechos de la base de datos para decidir si los argumentos de los valores
absolutos son números complejos:

```maxima
(%i1) to_poly_solve(abs(x) = 6, x);
(%o1)              %union([x = - 6], [x = 6])
(%i2) declare(z,complex)$
(%i3) to_poly_solve(abs(z) = 6, z);
(%o3) %union(%if((%c11 # 0) %and (%c11 conjugate(%c11) - 36 = 
                                       0), [z = %c11], %union()))
```

Esta es la única situación en la que `to_poly_solve` consulta la base de
datos; si una incógnita se declara, por ejemplo, como entero, `to_poly_solve` lo ignora.


Para hacer uso de esta función, ejecútese `load("to_poly_solve")`.


Véase también `algexact`, `resultant`, `algebraic` y `to_poly`.

