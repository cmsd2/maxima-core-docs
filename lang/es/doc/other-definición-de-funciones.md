## Definición de Funciones

<!-- category: Other -->
<!-- keywords: apply -->
<!-- signatures: apply(F, [x_1, ..., x_n]) -->
### Function: apply (F, [x_1, ..., x_n])

Construye y evalúa la expresión `F(arg_1, ..., arg_n)`.


La función `apply` no hace distinciones entre funciones array y 
funciones ordinarias; cuando *F* es el nombre de una función array,
`apply` evalúa `F(...)`, esto es, hace una llamada con
paréntesis en lugar de corchetes. La función `arrayapply`
evalúa una llamada a función con corchetes para estos casos.


Ejemplos:


La función `apply` evalúa sus argumentos.
En este ejemplo, `min` se aplica al valor de `L`.







```maxima
(%i1) L : [1, 5, -10.2, 4, 3];
(%o1)                 [1, 5, - 10.2, 4, 3]
(%i2) apply (min, L);
(%o2)                        - 10.2
```


La función `apply` evalúa sus argumentos,
incluso cuando la función *F* no lo hace.










```maxima
(%i1) F (x) := x / 1729;
                                   x
(%o1)                     F(x) := ----
                                  1729
(%i2) fname : F;
(%o2)                           F
(%i3) dispfun (F);
                                   x
(%t3)                     F(x) := ----
                                  1729

(%o3)                         [%t3]
(%i4) dispfun (fname);
fname is not the name of a user function.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) apply (dispfun, [fname]);
                                   x
(%t5)                     F(x) := ----
                                  1729

(%o5)                         [%t5]
```


La función `apply` evalúa el nombre de función *F*.
La comilla simple `'` evita la evaluación.
El nombre `demoivre` corresponde a una variable global y
también a una función.









```maxima
(%i1) demoivre;
(%o1)                         false
(%i2) demoivre (exp (%i * x));
(%o2)                  %i sin(x) + cos(x)
(%i3) apply (demoivre, [exp (%i * x)]);
demoivre evaluates to false
Improper name or value in functional position.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) apply ('demoivre, [exp (%i * x)]);
(%o4)                  %i sin(x) + cos(x)
```

<!-- category: Other -->
<!-- keywords: block -->
<!-- signatures: block([v_1, ..., v_m], expr_1, ..., expr_n), block(expr_1, ..., expr_n) -->
### Function: block ([v_1, ..., v_m], expr_1, ..., expr_n)

La función `block` evalúa *expr_1*, ..., *expr_n* secuencialmente y devuelve el valor de la última expresión evaluada. La secuencia puede alterarse con las funciones `go`, `throw` y `return`. La última expresión es *expr_n* a menos que `return` o una expresión que contenga un `throw` sea evaluada. Las variables *v_1*, ..., *v_m* son locales en el bloque; éstas se distiguen de las globales que tengan el mismo nombre. Si no se declaran variables locales entonces se puede omitir la lista. Dentro del bloque, cualquier otra variable distinta de *v_1*, ..., *v_m* se considera global.


La función `block` guarda los valores actuales de las variables *v_1*, ..., *v_m*, si los tienen, a la entrada del bloque y luego las evalúa a sí mismas, es decir les saca el valor temporalmente. A las variables locales se les puede asignar cualquier valor dentro del bloque, pero al salir de éste, los valores inicialmente almacenados quedan restaurados, al tiempo que los asignados dentro del bloque se pierden.


La declaración `local(v_1, ..., v_m)` dentro de un bloque
almacena las propiedades asociadas a los símbolos *v_1*, ..., *v_m*,
borra cualesquiera otras propiedades antes de evaluar las expresiones y
restaura las propiedades guardadas antes de abandonar el bloque.
Algunas declaraciones, como `:=`, `array`, `dependencies`, `atvalue`,
`matchdeclare`, `atomgrad`, `constant`, `nonscalar`, `assume`
y otras se implementan como propiedades de símbolos.
El efecto producido por `local` consiste en hacer que tales declaraciones tengan
efecto sólo dentro del bloque, en otro caso las declaraciones dentro del bloque 
tendrían un efecto global que afectarían al exterior de `block`.


Un `block` puede aparecer dentro de otro `block`. Las variables locales se inicializan cada vez que se entra dentro de un nuevo bloque. Las variables locales de un bloque se consideran globales dentro de otro anidado dentro del primero. Si una variable es no local dentro de un bloque, su valor es el que le corresponde en el bloque superior. Este criterio se conoce con el nombre de "alcance dinámico".


El valor del bloque es el de la última sentencia o el argumento de la función `return`, que puede utilizarse para salir del bloque. La función `go` puede usarse para transferir el control a la sentencia del bloque que esté etiquetada con el argumento de `go`. Para etiquetar una sentencia basta que vaya precedida de un argumento atómico como cualquier otra sentencia dentro del bloque. Por ejemplo, `block ([x], x:1, tururu, x: x+1, ..., go(tururu), ...)`.  El argumento de `go` debe ser el nombre de una etiqueta colocada dentro del bloque. No se puede utilzar `go` para trasladarse a una etiqueta de un bloque que no sea el que contenga a `go`.


Normalmente los bloques aparecerán al lado derecho de las definiciones de funciones, pero también pueden utilizarse en otros contextos.

<!-- category: Other -->
<!-- keywords: break -->
<!-- signatures: break(expr_1, ..., expr_n) -->
### Function: break (expr_1, ..., expr_n)

Calcula e imprime *expr_1*, ..., *expr_n* para luego provocar la detención de Maxima, de modo que el usuario pueda examinar y cambiar el entorno de ejecución. Pulsando posteriormente `exit;` el cálculo se reanuda.

<!-- category: Other -->
<!-- keywords: catch -->
<!-- signatures: catch(expr_1, ..., expr_n) -->
### Function: catch (expr_1, ..., expr_n)

Evalúa *expr_1*, ..., *expr_n* una a una;  si alguna de ellas conlleva la evaluación de una expresión de la forma `throw (arg)`, entonces el valor de `catch` es el de `throw (arg)` y ya no se evalúan más expresiones. Esta respuesta pasa todos los niveles de anidamiento hasta el `catch` más próximo. Si no hay ningún `catch`  que contenga un `throw` se emite un mensaje de error.


Si la evaluación de los argumentos no conlleva la evaluación de ningún `throw`, entonces el valor de `catch` es el devuelto por *expr_n*.



```maxima
(%i1) lambda ([x], if x < 0 then throw(x) else f(x))$
(%i2) g(l) := catch (map (''%, l))$
(%i3) g ([1, 2, 3, 7]);
(%o3)               [f(1), f(2), f(3), f(7)]
(%i4) g ([1, 2, -3, 7]);
(%o4)                          - 3
```


La función `g` devuelve las imágenes por `f` de todos los elementos de la lista `l` si ésta contiene únicamente números no negativos; si no es este el caso, entonces `g` captura el primer negativo que encuentra y lo devuelve por medio del `throw`.

<!-- category: Other -->
<!-- keywords: compfile -->
<!-- signatures: compfile(filename, f_1, ..., f_n), compfile(filename, functions), compfile(filename, all) -->
### Function: compfile (filename, f_1, ..., f_n)

Traduce funciones de Maxima a código Lisp, guardándolo 
luego en el fichero *filename*.


Con la llamada `compfile(filename, f_1, ..., f_n)`
se traducen las funciones especificadas, mientras que 
`compfile(filename, functions)` y
`compfile(filename, all)` traducen las funciones definidas por
el usuario.


El código Lisp traducido no se evalúa, ni el fichero 
de salida es procesado por el compilador de Lisp.
La función `translate` crea y evalúa las traducciones Lisp, mientras que
`compile_file` traduce primero de Maxima a Lisp y luego
ejecuta el compilador Lisp. 


Véanse también `translate`, `translate_file` y `compile_file`.

<!-- category: Other -->
<!-- keywords: compile -->
<!-- signatures: compile(f_1, ..., f_n), compile(functions), compile(all) -->
### Function: compile (f_1, ..., f_n)

Traduce las funciones de Maxima *f_1*, ..., *f_n* a Lisp, evaluando el código resultante, y llama a la función Lisp `COMPILE` para cada función traducida. La función `compile` devuelve una lista con los nombres de las funciones compiladas.


Las llamadas `compile (all)` o `compile (functions)` compilan todas las funciones definidas por el usuario.


La función `compile` no evalúa sus argumentos, pero con el operador comilla-comilla (`''`) sí lo hace.

<!-- category: Other -->
<!-- keywords: compile_file -->
<!-- signatures: compile_file(nombre_fich), compile_file(nombre_fich, nombre_fich_compilado), compile_file(nombre_fich, nombre_fich_compilado, nombre_fich_lisp) -->
### Function: compile_file (nombre_fich)

Traduce el fichero Maxima *nombre_fich* a Lisp, ejecuta el compilador de Lisp y, en caso de ser exitosa la compilación, carga el código compilado en Maxima.


La función `compile_file` devuelve una lista con los nombres de tres ficheros: el fichero original en Maxima, la traducción Lisp, notas sobre la traducción y el código compilado. Si la compilación falla, el cuarto elemento es  `false`.


Algunas declaraciones y definiciones entran en efecto tan pronto como el código Lisp es compilado (sin cargar el código compilado). Éstas incluyen funciones definidas con el operador `:=`, macros definidas con el operador `::=`, `alias`, `declare`, `define_variable`,  `mode_declare` y `infix`, `matchfix`,
`nofix`, `postfix`, `prefix` y `compfile`.


Asignaciones y llamadas a funciones no se evalúan hasta que el código compilado es cargado. En particular, dentro del fichero Maxima, asignaciones a los controles ("flags") de traducción (`tr_numer`, etc.) no tienen efecto durante la traducción.


El *nombre_fich* no puede contener sentencias del tipo `:lisp`.


La función `compile_file` evalúa sus argumentos.

<!-- category: Other -->
<!-- keywords: declare_translated -->
<!-- signatures: declare_translated(f_1, f_2, ...) -->
### Function: declare_translated (f_1, f_2, ...)

Cuando se traduce un fichero de código Maxima a Lisp, es importante para el traductor saber qué funciones de las que están en el fichero van a ser llamadas como traducidas o compiladas, y cuáles son simplemente funciones Maxima o que no están definidas. Se genera el código `(MFUNCTION-CALL fn arg1 arg2 ...)` cuando el traductor no sabe si `fn` va a ser una función lisp.

<!-- category: Other -->
<!-- keywords: define -->
<!-- signatures: define(f(x_1, ..., x_n), expr), define(f[x_1, ..., x_n], expr), define(funmake(f, [x_1, ..., x_n]), expr), define(arraymake(f, [x_1, ..., x_n]), expr), define(ev(expr_1), expr_2) -->
### Function: define (f(x_1, ..., x_n), expr)

Define una función de nombre *f* con argumentos *x_1*, ..., *x_n* y cuerpo *expr*.
`define` evalúa siempre su segundo argumento, a menos que se
indique lo contrario con el operador de comilla simple. La función así
definida puede ser una función ordinaria de Maxima (con sus argumentos
encerrados entre paréntesis) o una función array (con sus argumentos encerrados
entre corchetes).


Cuando el último o único argumento *x_n* es una lista de un solo 
elemento, la función definida por `define` acepta un número variable
de argumentos. Los valores de los argumentos se van asignando uno a uno a 
*x_1*, ..., *x_(n - 1)*, y los que queden, si los hay, se asignan 
a *x_n* en forma de lista.


Cuando el primer argumento de `define` es una expresión de la
forma `f(x_1, ..., x_n)` o
`f[x_1, ..., x_n]`, se evalúan los argumentos de la función,
pero no *f*, incluso cuando se trate de una función o variable ya existente 
con ese nombre.


Cuando el primer argumento es una expresión con operador `funmake`, 
`arraymake` o `ev`, se evalúa este primer argumento, lo que
permite calcular la función.


Todas las definiciones de funciones aparecen en el mismo espacio
de nombres; definiendo una función `f` dentro de otra
función `g` no limita automáticamente el alcance de `f` a `g`.
Sin embargo, `local(f)` hace que la definición de la función `f`
sea efectiva sólo dentro del bloque o expresión compuesta en el que
aparece `local`.


Si un argumento formal *x_k* es un símbolo afectado
por el operador comilla simple (expresión nominal), la función definida por
`define` no evalúa el correspondiente valor de argumento.
En cualquier otro caso, los argumentos que se pasan son evaluados.


Véanse también `:=` y `::=`.


Ejemplos:


`define` evalúa siempre su segundo argumento, a menos que se
indique lo contrario con el operador de comilla simple.










```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) define (F1 (x, y), expr);
(%o2)              F1(x, y) := cos(y) - sin(x)
(%i3) F1 (a, b);
(%o3)                    cos(b) - sin(a)
(%i4) F2 (x, y) := expr;
(%o4)                   F2(x, y) := expr
(%i5) F2 (a, b);
(%o5)                    cos(y) - sin(x)
```


La función así
definida puede ser una función ordinaria de Maxima o una función array.







```maxima
(%i1) define (G1 (x, y), x.y - y.x);
(%o1)               G1(x, y) := x . y - y . x
(%i2) define (G2 [x, y], x.y - y.x);
(%o2)                G2     := x . y - y . x
                       x, y
```


Cuando el último o único argumento *x_n* es una lista de un solo 
elemento, la función definida por `define` acepta un número variable
de argumentos.







```maxima
(%i1) define (H ([L]), '(apply ("+", L)));
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


Cuando el primer argumento es una expresión con operador `funmake`, 
`arraymake` o `ev`, se evalúa este primer argumento.











```maxima
(%i1) [F : I, u : x];
(%o1)                        [I, x]
(%i2) funmake (F, [u]);
(%o2)                         I(x)
(%i3) define (funmake (F, [u]), cos(u) + 1);
(%o3)                  I(x) := cos(x) + 1
(%i4) define (arraymake (F, [u]), cos(u) + 1);
(%o4)                   I  := cos(x) + 1
                         x
(%i5) define (foo (x, y), bar (y, x));
(%o5)                foo(x, y) := bar(y, x)
(%i6) define (ev (foo (x, y)), sin(x) - cos(y));
(%o6)             bar(y, x) := sin(x) - cos(y)
```

<!-- category: Other -->
<!-- keywords: define_variable -->
<!-- signatures: define_variable(name, default_value, mode) -->
### Function: define_variable (name, default_value, mode)

Introduce una variable global en el entorno de Maxima. La función 
`define_variable` puede ser útil en los paquetes escritos por
los usuarios que vayan a ser compilados o traducidos con frecuencia.


La función `define_variable` ejecuta los siguientes pasos:



1. `mode_declare (name, mode)` declara el modo de *name* al traductor.
Véase `mode_declare` para ver la lista de modos aceptables.
2. Si aún no tiene asignación, se le da a la variable *default_value* el valor *name*.
3. `declare (name, special)` la declara como especial.
4. Asocia *name* a una función de comprobación para asegurar que
a *name* sólo se le asignan valores del modo declarado.















La propiedad `value_check` se puede asociar a cualquier variable que haya
sido definida mediante `define_variable` en cualquiera de los modos diferentes
a `any`. La propiedad `value_check` puede ser una expresión lambda o
una función de una variable, que será invocada al intentar asignar un valor a la
variable; el argumento pasado a la función `value_check` es el valor que
se le quiere asignar a la variable.


La función `define_variable` evalúa `default_value` pero no
`name` ni `mode`; el valor que devuelve es el valor actual de 
`name`, el cual es `default_value` si a `name` no se le ha
aplicado ninguna asignación, o el valor de dicha asignación en caso
contrario.


Ejemplos:


`foo` es una variable booleana con valor inicial `true`.









```maxima
(%i1) define_variable (foo, true, boolean);
(%o1)                         true
(%i2) foo;
(%o2)                         true
(%i3) foo: false;
(%o3)                         false
(%i4) foo: %pi;
Error: foo was declared mode boolean, has value: %pi
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) foo;
(%o5)                         false
```


`bar` es una variable entera, cuyo valor habrá de ser primo.











```maxima
(%i1) define_variable (bar, 2, integer);
(%o1)                           2
(%i2) qput (bar, prime_test, value_check);
(%o2)                      prime_test
(%i3) prime_test (y) := if not primep(y) then
                           error (y, "is not prime.");
(%o3) prime_test(y) := 
         if not primep(y) then error(y, "is not prime.")
(%i4) bar: 1439;
(%o4)                         1439
(%i5) bar: 1440;
1440 is not prime.
#0: prime_test(y=1440)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) bar;
(%o6)                         1439
```


`baz_quux` es una variable a la que no se le podrá asignar valor alguno.
El modo `any_check` es como `any`, 
pero `any_check` activa el mecanismo `value_check`, cosa que `any`
no hace.











```maxima
(%i1) define_variable (baz_quux, 'baz_quux, any_check);
(%o1)                       baz_quux
(%i2) F: lambda ([y], if y # 'baz_quux then
                 error ("Cannot assign to `baz_quux'."));
(%o2) lambda([y], if y # 'baz_quux
                   then error(Cannot assign to `baz_quux'.))
(%i3) qput (baz_quux, ''F, value_check);
(%o3) lambda([y], if y # 'baz_quux
                   then error(Cannot assign to `baz_quux'.))
(%i4) baz_quux: 'baz_quux;
(%o4)                       baz_quux
(%i5) baz_quux: sqrt(2);
Cannot assign to `baz_quux'.
#0: lambda([y],if y # 'baz_quux then
             error("Cannot assign to `baz_quux'."))(y=sqrt(2))
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) baz_quux;
(%o6)                       baz_quux
```

<!-- category: Other -->
<!-- keywords: dispfun -->
<!-- signatures: dispfun(f_1, ..., f_n), dispfun(all) -->
### Function: dispfun (f_1, ..., f_n)

Muestra la deficnión de las funciones de usuario *f_1*, ..., *f_n*. Cada argumento puede ser el nombre de una macro (definida mediante `::=`), una función ordinaria (definida mediante `:=` o `define`), una función arreglo  (definida mediante `:=` o `define`, pero encerrando los argumentos dentro de corchetes `[ ]`), una función de subíndice (definida mediante `:=` o `define`, pero encerrando algunos argumentos entre corchetes y otros entre paréntesis  `( )`), una función de subíndice seleccionada por un subíndice variable, o una función de subíndice definida con un subíndice constante.


La llamada `dispfun (all)` muestra todas las funciones de usuario tal como las dan las listas `functions`, `arrays` y `macros`, omitiendo las funciones con subíndices definidas con subíndices constantes.


La función `dispfun` crea una etiqueta (`%t1`, `%t2`, etc.) para cada función mostrada, y asigna la definición de la función a la etiqueta. En contraste, `fundef` devuelve las definiciones de las funciones.


La función `dispfun` no evalúa sus argumentos; el operador de comilla-comilla `''` permite la evaluación.


La función `dispfun` devuelve la lista de etiquetas de expresiones intermedias correspondientes a las funciones mostradas.


Ejemplos:












```maxima
(%i1) m(x, y) ::= x^(-y);
                                     - y
(%o1)                   m(x, y) ::= x
(%i2) f(x, y) :=  x^(-y);
                                     - y
(%o2)                    f(x, y) := x
(%i3) g[x, y] :=  x^(-y);
                                    - y
(%o3)                     g     := x
                           x, y
(%i4) h[x](y) :=  x^(-y);
                                    - y
(%o4)                     h (y) := x
                           x
(%i5) i[8](y) :=  8^(-y);
                                    - y
(%o5)                     i (y) := 8
                           8
(%i6) dispfun (m, f, g, h, h[5], h[10], i[8]);
                                     - y
(%t6)                   m(x, y) ::= x

                                     - y
(%t7)                    f(x, y) := x

                                    - y
(%t8)                     g     := x
                           x, y

                                    - y
(%t9)                     h (y) := x
                           x

                                    1
(%t10)                     h (y) := --
                            5        y
                                    5

                                     1
(%t11)                    h  (y) := ---
                           10         y
                                    10

                                    - y
(%t12)                    i (y) := 8
                           8

(%o12)       [%t6, %t7, %t8, %t9, %t10, %t11, %t12]
(%i12) ''%;
                     - y              - y            - y
(%o12) [m(x, y) ::= x   , f(x, y) := x   , g     := x   , 
                                            x, y
                  - y           1              1             - y
        h (y) := x   , h (y) := --, h  (y) := ---, i (y) := 8   ]
         x              5        y   10         y   8
                                5             10
```

<!-- category: Other -->
<!-- keywords: fullmap -->
<!-- signatures: fullmap(f, expr_1, ...) -->
### Function: fullmap (f, expr_1, ...)

Similar a `map`, pero conservará el mapeado
descendente de todas las subexpresiones hasta que los operadores
principales ya no sean los mismos.


La función `fullmap` es utilizada por el simplificador de Maxima
en algunas transformaciones matriciales, por lo que Maxima generará en algunas ocasiones mensajes de error relacionados con `fullmap` aunque el usuario no haya invocado explícitamente esta función.








```maxima
(%i1) a + b * c;
(%o1)                        b c + a
(%i2) fullmap (g, %);
(%o2)                   g(b) g(c) + g(a)
(%i3) map (g, %th(2));
(%o3)                     g(b c) + g(a)
```

<!-- category: Other -->
<!-- keywords: fullmapl -->
<!-- signatures: fullmapl(f, list_1, ...) -->
### Function: fullmapl (f, list_1, ...)

Similar a `fullmap`, pero `fullmapl` sólo hace mapeo
sobre listas y matrices.






```maxima
(%i1) fullmapl ("+", [3, [4, 5]], [[a, 1], [0, -1.5]]);
(%o1)                [[a + 3, 4], [4, 3.5]]
```

<!-- category: Other -->
<!-- keywords: functions -->
<!-- signatures: functions -->
### Variable: functions

Valor por defecto: `[]`


La variable `functions` es una lista que contiene los nombres de las funciones ordinarias de Maxima. Una función ordinaria es aquella que ha sido construida mediante cualquiera de los métodos `define` o `:=` y que es invocada utilizando paréntesis. Una función puede definirse durante una sesión de Maxima o en un fichero que posteriormente será cargado en memoria por `load` o `batch`.


Las funciones array, que son invocadas con corchetes (`F[x]`),
y las funciones subindicadas, que son las invocadas con corchetes y
paréntesis (`F[x](y)`) se registran en la variable global `arrays`,
no en `functions`.


Las funciones Lisp no se registran en ninguna lista.


Ejemplos:














```maxima
(%i1) F_1 (x) := x - 100;
(%o1)                   F_1(x) := x - 100
(%i2) F_2 (x, y) := x / y;
                                      x
(%o2)                    F_2(x, y) := -
                                      y
(%i3) define (F_3 (x), sqrt (x));
(%o3)                   F_3(x) := sqrt(x)
(%i4) G_1 [x] := x - 100;
(%o4)                    G_1  := x - 100
                            x
(%i5) G_2 [x, y] := x / y;
                                     x
(%o5)                     G_2     := -
                             x, y    y
(%i6) define (G_3 [x], sqrt (x));
(%o6)                    G_3  := sqrt(x)
                            x
(%i7) H_1 [x] (y) := x^y;
                                      y
(%o7)                     H_1 (y) := x
                             x
(%i8) functions;
(%o8)              [F_1(x), F_2(x, y), F_3(x)]
(%i9) arrays;
(%o9)                 [G_1, G_2, G_3, H_1]
```

<!-- category: Other -->
<!-- keywords: fundef -->
<!-- signatures: fundef(f) -->
### Function: fundef (f)

Devuelve la definición de la función *f*.


Cada argumento puede ser el nombre de una macro (definida mediante `::=`), una función ordinaria (definida mediante `:=` o `define`), una función arreglo  (definida mediante `:=` o `define`, pero encerrando los argumentos dentro de corchetes `[ ]`), una función de subíndice (definida mediante `:=` o `define`, pero encerrando algunos argumentos entre corchetes y otros entre paréntesis  `( )`), una función de subíndice seleccionada por un subíndice variable, o una función de subíndice definida con un subíndice constante.


La función `fundef` no evalúa sus argumentos; el operador comilla-comilla `''` permite la evaluación.


La llamada de función `fundef (f)` devuelve la definición de *f*. Por el contrario, `dispfun (f)` crea una etiqueta intermedia y le asigna la definición a la etiqueta.

<!-- category: Other -->
<!-- keywords: funmake -->
<!-- signatures: funmake(F, [arg_1, ..., arg_n]) -->
### Function: funmake (F, [arg_1, ..., arg_n])

Devuelve una expresión `F(arg_1, ..., arg_n)`.
El valor así retornado es simplificado pero no evaluado,
de forma que la función *F* no es invocada, incluso cuando exista.


La función `funmake` no hace distinciones entre funciones array
y funciones ordinarias; cuando *F* es el nombre de una función array,
`funmake` devuelve `F(...)`,
esto es, una llamada a función con paréntesis en lugar de corchetes.
La función `arraymake` devuelve una llamada a función con
corchetes para estos casos.


La función `funmake` evalúa sus argumentos.


Ejemplos:


La función `funmake` aplicada a una función ordinaria de Maxima.








```maxima
(%i1) F (x, y) := y^2 - x^2;
                                   2    2
(%o1)                  F(x, y) := y  - x
(%i2) funmake (F, [a + 1, b + 1]);
(%o2)                    F(a + 1, b + 1)
(%i3) ''%;
                              2          2
(%o3)                  (b + 1)  - (a + 1)
```


La función `funmake` aplicada a una macro.








```maxima
(%i1) G (x) ::= (x - 1)/2;
                                  x - 1
(%o1)                    G(x) ::= -----
                                    2
(%i2) funmake (G, [u]);
(%o2)                         G(u)
(%i3) ''%;
                              u - 1
(%o3)                         -----
                                2
```


La función `funmake` aplicada a una función subindicada.










```maxima
(%i1) H [a] (x) := (x - 1)^a;
                                        a
(%o1)                   H (x) := (x - 1)
                         a
(%i2) funmake (H [n], [%e]);
                                       n
(%o2)               lambda([x], (x - 1) )(%e)
(%i3) ''%;
                                    n
(%o3)                       (%e - 1)
(%i4) funmake ('(H [n]), [%e]);
(%o4)                        H (%e)
                              n
(%i5) ''%;
                                    n
(%o5)                       (%e - 1)
```


La función `funmake` aplicada a un símbolo
que no está asociado a función alguna.







```maxima
(%i1) funmake (A, [u]);
(%o1)                         A(u)
(%i2) ''%;
(%o2)                         A(u)
```


La función `funmake` evalúa sus argumentos,
pero no el valor retornado.










```maxima
(%i1) det(a,b,c) := b^2 -4*a*c;
                                    2
(%o1)              det(a, b, c) := b  - 4 a c
(%i2) (x : 8, y : 10, z : 12);
(%o2)                          12
(%i3) f : det;
(%o3)                          det
(%i4) funmake (f, [x, y, z]);
(%o4)                    det(8, 10, 12)
(%i5) ''%;
(%o5)                         - 284
```


Maxima simplifica el valor retornado de `funmake`.






```maxima
(%i1) funmake (sin, [%pi / 2]);
(%o1)                           1
```

<!-- category: Other -->
<!-- keywords: lambda -->
<!-- signatures: lambda([x_1, ..., x_m], expr_1, ..., expr_n), lambda([[L]], expr_1, ..., expr_n), lambda([x_1, ..., x_m, [L]], expr_1, ..., expr_n) -->
### Function: lambda ([x_1, ..., x_m], expr_1, ..., expr_n)

Define y devuelve una expresión lambda (es decir, una función anónima).
La función puede tener argumentos *x_1*, ..., *x_m* y/o argumentos
opcionales *L*, que aparecerán dentro del cuerpo de la función como una lista.
El valor que devuelve la función es *expr_n*.
Una expresión lambda puede asignarse a una variable y ser evaluada como si fuese una función ordinaria. Además, puede aparecer en algunos contextos en los que sea necesario un nombre de función.


Cuando se evalúa la función, se crean las variables *x_1*, ..., *x_m* sin asignación de valores. Una función `lambda` puede aparecer dentro de un `block` o de otra `lambda`. Las variables locales se inicializan cada vez que se entra dentro de un nuevo bloque o de otra función `lambda`. Las variables locales se consideran globales dentro de un bloque o función `lambda` anidado dentro del primero. Si una variable es no local dentro de un bloque o función `lambda`, su valor es el que le corresponde en el bloque o función `lambda` superior. Este criterio se conoce con el nombre de "alcance dinámico".


Una vez establecidas las variables locales *expr_1* a *expr_n* son secuencialmente evaluadas. La variable especial  `%%` representa el valor de la expresión inmediata anterior. Las sentencias `throw` y `catch` pueden aparecer también en la lista de expresiones.


La función `return` no puede aparecer en una expresión `lambda` a menos que se encuentre acotada dentro de un bloque (`block`), en cuyo caso `return` establece el valor de retorno del bloque, pero no de la expresión `lambda`, a menos que el bloque resulte ser precisamente *expr_n*. De igual manera, `go` no puede aparecer en una expresión `lambda` si no es dentro de un `block`.


Las funciones `lambda` no evalúan sus argumentos;  el operador comilla-comilla `''` permite su evaluación.


Ejemplo:



- *
Una función lambda puede asignarse a una variable y ser evaluada como si fuese una función ordinaria.






```maxima
(%i1) f: lambda ([x], x^2);
                                      2
(%o1)                    lambda([x], x )
(%i2) f(a);
                                2
(%o2)                          a
```


- *
Una expresión lambda puede aparecer en algunos contextos en los que sea necesario un nombre de función.







```maxima
(%i3) lambda ([x], x^2) (a);
                                2
(%o3)                          a
(%i4) apply (lambda ([x], x^2), [a]);
                                2
(%o4)                          a
(%i5) map (lambda ([x], x^2), [a, b, c, d, e]);
                        2   2   2   2   2
(%o5)                 [a , b , c , d , e ]
```


- *
Los argumentos son variables locales. Otras variables se consideran globales. Las variables globales son evaluadas en el momento que lo es la expresión, a menos que la evaluación de las mismas sea forzada, como cuando se hace uso de `''`.












```maxima
(%i6) a: %pi$
(%i7) b: %e$
(%i8) g: lambda ([a], a*b);
(%o8)                   lambda([a], a b)
(%i9) b: %gamma$
(%i10) g(1/2);
                             %gamma
(%o10)                       ------
                               2
(%i11) g2: lambda ([a], a*''b);
(%o11)                lambda([a], a %gamma)
(%i12) b: %e$
(%i13) g2(1/2);
                             %gamma
(%o13)                       ------
                               2
```


- *
Las expresiones lambda pueden anidarse. Las variables locales de expresiones lambda exteriores se consideran globales en expresiones internas, a menos que se enmascaren con variables locales de igual nombre.






```maxima
(%i14) h: lambda ([a, b], h2: lambda ([a], a*b), h2(1/2));
                                                   1
(%o14)    lambda([a, b], h2 : lambda([a], a b), h2(-))
                                                   2
(%i15) h(%pi, %gamma);
                             %gamma
(%o15)                       ------
                               2
```


- *
Puesto que `lambda` no evalúa sus argumentos, la expresión lambda `i` de más abajo no define una función del tipo "multiplicar por `a`". Tal tipo de función se puede definir a través de `buildq`, como en la expresión lambda `i2` de más abajo.









```maxima
(%i16) i: lambda ([a], lambda ([x], a*x));
(%o16)            lambda([a], lambda([x], a x))
(%i17) i(1/2);
(%o17)                  lambda([x], a x)
(%i18) i2: lambda([a], buildq([a: a], lambda([x], a*x)));
(%o18)    lambda([a], buildq([a : a], lambda([x], a x)))
(%i19) i2(1/2);
                                     x
(%o19)                   lambda([x], -)
                                     2
(%i20) i2(1/2)(%pi);
                               %pi
(%o20)                         ---
                                2
```


- *
Una expresión lambda puede tener un número variable de argumentos,
los cuales se indican mediante `[L]`, bien sea solo o como un
último argumento. Estos argumentos aparecerán dentro del cuerpo de
la función en forma de lista.








```maxima
(%i1) f : lambda ([aa, bb, [cc]], aa * cc + bb);
(%o1)          lambda([aa, bb, [cc]], aa cc + bb)
(%i2) f (foo, %i, 17, 29, 256);
(%o2)       [17 foo + %i, 29 foo + %i, 256 foo + %i]
(%i3) g : lambda ([[aa]], apply ("+", aa));
(%o3)             lambda([[aa]], apply(+, aa))
(%i4) g (17, 29, x, y, z, %e);
(%o4)                  z + y + x + %e + 46
```

<!-- category: Other -->
<!-- keywords: local -->
<!-- signatures: local(v_1, ..., v_n) -->
### Function: local (v_1, ..., v_n)

La declaración `local(v_1, ..., v_m)` dentro de un bloque
almacena las propiedades asociadas a los símbolos *v_1*, ..., *v_m*,
borra cualesquiera otras propiedades antes de evaluar las expresiones y
restaura las propiedades guardadas antes de abandonar el bloque.


Algunas declaraciones, como `:=`, `array`, `dependencies`, `atvalue`,
`matchdeclare`, `atomgrad`, `constant`, `nonscalar`, `assume`
y otras se implementan como propiedades de símbolos.
El efecto producido por `local` consiste en hacer que tales declaraciones tengan
efecto sólo dentro del bloque, en otro caso las declaraciones dentro del bloque 
tendrían un efecto global que afectarían al exterior de `block`.


La función `local` sólo puede usarse dentro de un `block`, en el
cuerpo de definición de funciones o de expresiones `lambda` o en la
función `ev`, siéndole permitido aparecer una sóla vez en cada una de ellas.


La función `local` no evalúa sus argumentos y devuelve `done`.


Ejemplo:


Definición local de una función.









```maxima
(%i1) foo (x) := 1 - x;
(%o1)                    foo(x) := 1 - x
(%i2) foo (100);
(%o2)                         - 99
(%i3) block (local (foo), foo (x) := 2 * x, foo (100));
(%o3)                          200
(%i4) foo (100);
(%o4)                         - 99
```

<!-- category: Other -->
<!-- keywords: macroexpansion -->
<!-- signatures: macroexpansion -->
### Variable: macroexpansion

Valor por defecto: `false`


La variable `macroexpansion` controla si la expansión (esto es, el valor de retorno) de una función macro se sustituye por la llamada a la función macro. Una sustitución puede acelerar futuras evaluaciones de la expresión, bajo el coste que implica tener que almacenar la expansión.



**false** — La expansión de una función macro no se sustituye por la llamada a la función macro.
**expand** — La primera vez que se evalúa una llamada a función macro se almacena la expansión. De esta manera la expansión no se recalcula en llamadas posteriores; cualesquiera efectos laterales (como `print` o asignaciones a variables globales)
tan solo tienen lugar la primera vez que la función macro es evaluada. La expansión en una expresión no afecta a otras expresiones que llamen a la misma función macro.
**displace** — La primera vez que se evalúa una llamada a una función macro, la expansión se sustituye por la llamada, modificando así la expresión desde la que se hizo la llamada a la función macro. La expansión no se recalcula en llamadas posteriores; cualesquiera efectos laterales tan solo tienen lugar la primera vez que la función macro es evaluada. La expansión en una expresión no afecta a otras expresiones que llamen a la misma función macro.


Ejemplos:


Si `macroexpansion` vale `false`,
una función macro es llamada cada vez que la expresión de llamada es evaluada.














```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                     return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                     return(x - 99))
(%i4) macroexpansion: false;
(%o4)                         false
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o7)                       --------
                            a b + 99
```


Si `macroexpansion` vale `expand`, una función macro tan solo es llamada una vez.














```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                     return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                     return(x - 99))
(%i4) macroexpansion: expand;
(%o4)                        expand
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```


Si `macroexpansion` vale `expand`, una función macro es llamada una vez y la expresión de llamada se modifica.












```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x), return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x), return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: displace;
(%o4)                       displace
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                 x - 99
(%t6)                    f(x) := ------
                                 x + 99

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```

<!-- category: Other -->
<!-- keywords: mode_check_errorp -->
<!-- signatures: mode_check_errorp -->
### Variable: mode_check_errorp

Valor por defecto: `false`



Cuando `mode_check_errorp` vale `true`, `mode_declare` llama a error.

<!-- category: Other -->
<!-- keywords: mode_check_warnp -->
<!-- signatures: mode_check_warnp -->
### Variable: mode_check_warnp

Valor por defecto: `true`



Cuando `mode_check_warnp` vale `true`, se detallan los errores de modo.

<!-- category: Other -->
<!-- keywords: mode_checkp -->
<!-- signatures: mode_checkp -->
### Variable: mode_checkp

Valor por defecto: `true`


Cuando `mode_checkp` vale `true`, `mode_declare` chequea los modos de las variables con valores asignados.

<!-- category: Other -->
<!-- keywords: mode_declare -->
<!-- signatures: mode_declare(y_1, modo_1, ..., y_n, modo_n) -->
### Function: mode_declare (y_1, modo_1, ..., y_n, modo_n)

La función `mode_declare` se utiliza para declarar los modos de variables y funciones para la ulterior traducción a Lisp o compilación de funciones. Se coloca habitualmente al comienzo de la definición de una función, de un script en Maxima o se ejecuta en tiempo real.


Los argumentos de `mode_declare` son pares formados por una variable y un modo, el cual debe ser `boolean`, `fixnum`, `number`, `rational` o `float`. Cada variable puede ser sustituida por una lista de variables, en cuyo caso todas ellas tendrán el mismo modo.




Código numérico que utilice arreglos puede ejecutarse más rápido declarando el tamaño que va a ocupar el arreglo, como en:



```maxima
mode_declare (array (a [10, 10]), float)
```


para un arreglo de números en coma flotante de dimensiones 10 x 10.


Se puede declarar el modo del resultado de una función poniendo `function (f_1, f_2, ...)` como argumento;
aquí `f_1`, `f_2`, ... son los nombres de las funciones. Por ejemplo, la expresión



```maxima
mode_declare ([function (f_1, f_2, ...)], fixnum)
```


declara que el valor a devolver por  `f_1`, `f_2`, ... son enteros de modo "single-word".


El nombre `modedeclare` es sinónimo de `mode_declare`.

<!-- category: Other -->
<!-- keywords: mode_identity -->
<!-- signatures: mode_identity(arg_1, arg_2) -->
### Function: mode_identity (arg_1, arg_2)

Es una forma especial usada con `mode_declare` y `macros` para declarar, por ejemplo, una lista de listas de números.

<!-- category: Other -->
<!-- keywords: remfunction -->
<!-- signatures: remfunction(f_1, ..., f_n), remfunction(all) -->
### Function: remfunction (f_1, ..., f_n)

Desliga las definiciones de función de sus símbolos *f_1*, ..., *f_n*.
Los argumentos pueden ser nombres de funciones ordinarias 
(creadas con `:=` o `define`) o de funciones macro (creadas con `::=`).


La instrucción `remfunction (all)` desliga todas las definiciones de funciones.


La función `remfunction` no evalúa sus argumentos.


La función `remfunction` devuelve una lista con los
símbolos para los que la definición de función
fue desligada. Devuelve `false` en el lugar de cualquier 
símbolo para el que no hay función definida.


La función `remfunction` no se puede aplicar a arrays de funciones ni a
funciones subindicadas. Sí es aplicable en tales casos la 
función `remarray`.

<!-- category: Other -->
<!-- keywords: savedef -->
<!-- signatures: savedef -->
### Variable: savedef

Valor por defecto: `true`


Si `savedef` vale `true`, se mantiene la versión Maxima de una función definida por el usuario cuando ésta se traduce, lo que permite mostrar su código con `dispfun` y que la función pueda ser editada.


Si `savedef` vale `false`, los nombres de las funciones traducidas se eliminan de la lista `functions`.

<!-- category: Other -->
<!-- keywords: tr_array_as_ref -->
<!-- signatures: tr_array_as_ref -->
### Variable: tr_array_as_ref

Valor por defecto: `true`


Si `translate_fast_arrays` vale `false`, referencias de arreglos en el código Lisp creadas por  `translate_file` se ven afectadas por `tr_array_as_ref`.


El valor de la variable `tr_array_as_ref` no tiene ningún efecto cuando `translate_fast_arrays` vale `true`.

<!-- category: Other -->
<!-- keywords: tr_bound_function_applyp -->
<!-- signatures: tr_bound_function_applyp -->
### Variable: tr_bound_function_applyp

Valor por defecto: `true`


Si `tr_bound_function_applyp` vale `true`, Maxima envía un aviso si encuentra una variable con valor asignado que está siendo utilizada como una función. `tr_bound_function_applyp` no influye en el código generado bajo estas circunstancias.


Por ejemplo, una expresión como `g (f, x) := f (x+1)` provocará un mensaje de esta naturaleza.

<!-- category: Other -->
<!-- keywords: tr_file_tty_messagesp -->
<!-- signatures: tr_file_tty_messagesp -->
### Variable: tr_file_tty_messagesp

Valor por defecto: `false`


Si `tr_file_tty_messagesp` vale `true`, los mensajes generados por `translate_file` durante la traducción de un fichero se muestran en la consola y se insertan en el fichero UNLISP.  Si vale `false`, los mensajes sobre la traducción del fichero sólo se incorporan al fichero UNLISP.

<!-- category: Other -->
<!-- keywords: tr_float_can_branch_complex -->
<!-- signatures: tr_float_can_branch_complex -->
### Variable: tr_float_can_branch_complex

Valor por defecto: `true`


Le dice al traductor de Maxima a Lisp que las funciones `acos`, `asin`, `asec` y `acsc` pueden devolver valores complejos.

<!-- category: Other -->
<!-- keywords: tr_function_call_default -->
<!-- signatures: tr_function_call_default -->
### Variable: tr_function_call_default

Valor por defecto: `general`


El valor `false` significa llama a `meval`, `expr` significa que Lisp asignó los argumentos de la función,  `general`, el valor por defecto, devuelve código apropiado para `mexprs` y `mlexprs` pero no para `macros`. La opción `general` asegura que las asignaciones de las variables son correctas en el código compilado. En modo `general`, cuando se traduce F(X), si F es una variable con valor, entonces se entiende que se quiere calcular `apply (f, [x])`, y como tal se traduce, con el apropiado aviso. No es necesario desactivar esto. Con los valores por defecto la falta de mensajes de aviso implica compatibilidad completa entre el código traducido y compilado con el interpretado por Maxima.

<!-- category: Other -->
<!-- keywords: tr_numer -->
<!-- signatures: tr_numer -->
### Variable: tr_numer

Valor por defecto: `false`


Si `tr_numer` vale `true` se utilizan las propiedades numéricas en aquellos átomos que las posean, como en  `%pi`.

<!-- category: Other -->
<!-- keywords: tr_optimize_max_loop -->
<!-- signatures: tr_optimize_max_loop -->
### Variable: tr_optimize_max_loop

Valor por defecto: 100


El valor de `tr_optimize_max_loop` es el número máximo de veces que el traductor repetirá la macro-expansión y la optimización en el tratamiento de una expresión.

<!-- category: Other -->
<!-- keywords: tr_semicompile -->
<!-- signatures: tr_semicompile -->
### Variable: tr_semicompile

Valor por defecto: `false`


Si `tr_semicompile` vale `true`, las salidas de `translate_file` y `compfile` serán macro-expandidas pero no compiladas a código máquina por el compilador de Lisp.

<!-- category: Other -->
<!-- keywords: tr_state_vars -->
<!-- signatures: tr_state_vars -->
### Variable: tr_state_vars

Valor por defecto:



```maxima
[transcompile, tr_semicompile, tr_warn_undeclared, tr_warn_meval,
tr_warn_fexpr, tr_warn_mode, tr_warn_undefined_variable,
tr_function_call_default, tr_array_as_ref,tr_numer]
```


Es la lista de variables que afectan la forma en que se obtiene la salida del código traducido. Esta información es útil para desarrolladores que pretendan corregir posibles fallos del traductor. Comparando el código traducido con el que se debería obtener bajo unas ciertas condiciones, es posible hacer el seguimiento de los fallos.

<!-- category: Other -->
<!-- keywords: tr_warn_bad_function_calls -->
<!-- signatures: tr_warn_bad_function_calls -->
### Variable: tr_warn_bad_function_calls

Valor por defecto: `true`


Devuelve un aviso cuando se hacen llamadas a funciones que quizás no sean correctas debido a declaraciones inapropiadas realizadas durante la traducción.

<!-- category: Other -->
<!-- keywords: tr_warn_fexpr -->
<!-- signatures: tr_warn_fexpr -->
### Variable: tr_warn_fexpr

Valor por defecto: `compfile`


Devuelve un aviso si se encuentra con alguna FEXPR. Las FEXPR no deberían aparecer en el código traducido.

<!-- category: Other -->
<!-- keywords: tr_warn_meval -->
<!-- signatures: tr_warn_meval -->
### Variable: tr_warn_meval

Valor por defecto: `compfile`


Devuelve un aviso si la función `meval` es llamada.  Si `meval` es invocada, es señal de la presencia de problemas en la traducción.

<!-- category: Other -->
<!-- keywords: tr_warn_mode -->
<!-- signatures: tr_warn_mode -->
### Variable: tr_warn_mode

Valor por defecto: `all`


Devuelve un aviso cuando a las variables se les asignan valores incompatibles con su modo.

<!-- category: Other -->
<!-- keywords: tr_warn_undeclared -->
<!-- signatures: tr_warn_undeclared -->
### Variable: tr_warn_undeclared

Valor por defecto: `compile`


Determina cuando enviar mensajes sobre variables no declaradas.

<!-- category: Other -->
<!-- keywords: tr_warn_undefined_variable -->
<!-- signatures: tr_warn_undefined_variable -->
### Variable: tr_warn_undefined_variable

Valor por defecto: `all`


Devuelve un aviso cuando se detectan variables globales no definidas.

<!-- category: Other -->
<!-- keywords: tr_warnings_get -->
<!-- signatures: tr_warnings_get() -->
### Function: tr_warnings_get ()

Devuelve una lista con los avisos dados por el traductor.

<!-- category: Other -->
<!-- keywords: transcompile -->
<!-- signatures: transcompile -->
### Variable: transcompile

Valor por defecto: `true`


Si `transcompile` vale `true`, `translate` y `translate_file` generan declaraciones para hacer el código traducido más apto para la compilación.


La función `compfile` hace la asignación `transcompile: true`.

<!-- category: Other -->
<!-- keywords: translate -->
<!-- signatures: translate(f_1, ..., f_n), translate(functions), translate(all) -->
### Function: translate (f_1, ..., f_n)

Traduce las funciones definidas por el usuario *f_1*, ..., *f_n* del lenguaje de Maxima a Lisp y evalúa las traducciones Lisp. Normalmente las funciones traducidas se ejecutan más rapidamente que las originales.


Las llamadas `translate (all)` o `translate (functions)` traducen todas las funciones de usuario.


Las funciones a ser traducidas deberían incluir una llamada a `mode_declare` al comienzo siempre que sea posible, a fin de producir código más eficiente. Por ejemplo:



```maxima
f (x_1, x_2, ...) := block ([v_1, v_2, ...],
    mode_declare (v_1, modo_1, v_2, modo_2, ...), ...)
```




donde *x_1*, *x_2*, ... son los parámetros que se pasan a la función y *v_1*, *v_2*, ... son las variables locales.


Los nombres de las funciones traducidas son eliminados de la lista `functions` si `savedef` vale `false` (ver más abajo) y son añadidos a las listas `props`.


Las funciones no deberían ser traducidas hasta no estar completamente depuradas.


Se supone que las expresiones están simplificadas; en caso de no estarlo, se generará código correcto pero ineficiente. Así, el usuario no debería asignar a `simp` el valor `false`, el cual inhibe la simplificación de la expresión a ser traducida.


Cuando la variable `translate` vale `true`, se traducen automáticamente las funciones de usuario a Lisp.


Nótese que las funciones traducidas puede que no se ejecuten exactamente igual a como lo hacían antes de la traducción, debido a posibles incompatibilidades entre las versiones de Maxima y Lisp. En general, la función `rat` con más de un argumento y la función `ratvars` no deberían utilizarse si algunas de las variables son declaradas como expresiones racionales canónicas (CRE) mediante `mode_declare`. Además, la asignación  `prederror: false` no traducirá.


Si `savedef` vale `true`, entonces la versión de Maxima de una función de usuario permanecerá cuando la función sea traducida por `translate`. Con esto se hace posible que se muestre la definición llamando a `dispfun` y que la función sea editada.


Si `transrun` vale `false` entonces las versiones interpretadas de todas las funciones serán ejecutadas en lugar de las versiones traducidas.


El resultado devuelto por `translate` es una lista con los nombres de las funciones traducidas.

<!-- category: Other -->
<!-- keywords: translate_file -->
<!-- signatures: translate_file(nombre_fichero_maxima), translate_file(nombre_fichero_maxima, nombre_fichero_lisp) -->
### Function: translate_file (nombre_fichero_maxima)

Traduce un fichero en código Maxima a un fichero en código Lisp. La función `translate_file` devuelve una lista con los nombres de tres ficheros: el nombre del ficheero en Maxima, el nombre del fichero en Lisp y el nombre del fichero que contiene información adicional sobre la traducción. La función `translate_file` evalúa sus argumentos.


La llamada `translate_file ("foo.mac"); load("foo.LISP")` es lo mismo que `batch ("foo.mac")`, excepto por la presencia de ciertas restricciones, como el uso de `''` y `%`, por ejemplo.



La llamada `translate_file (nombre_fichero_maxima)` traduce un fichero en Maxima, *nombre_fichero_maxima*, a otro en Lisp de nombre similar. Por ejemplo, `foo.mac` se traduce en `foo.LISP`. El nombre del fichero en Maxima puede incluir el nombre de un directorio, en cuyo caso el fichero de salida Lisp se guardará en el mismo directorio desde el que se leyó la fuente Maxima.


La llamada `translate_file (nombre_fichero_maxima, nombre_fichero_lisp)` traduce el fichero Maxima  *nombre_fichero_maxima* en el fichero Lisp *nombre_fichero_lisp*. La función `translate_file` ignora la extensión del fichero, en caso de que exista, de `nombre_fichero_lisp`; la extensión del fichero de salida Lisp  será invariablemente `LISP`. El nombre del fichero Lisp puede incluir la ruta del directorio, en cuyo caso se almacenará en el directorio especificado.


La función `translate_file` también escribe un fichero de mensajes de avisos del traductor con diversos niveles de gravedad. La extensión de este fichero es `UNLISP`. Este fichero puede contener información valiosa, aunque de difícil interpretación, para detectar fallos en el código traducido. El fichero `UNLISP` se guarda siempre en el mismo directorio desde el que se leyó la fuente de Maxima.


La función `translate_file` emite código Lisp que incluye algunas declaraciones y definiciones que entran en efecto tan pronto como el código Lisp es compilado. Véase `compile_file` para más información sobre este particular.



Véanse también `tr_array_as_ref`,



`tr_bound_function_applyp`,


`tr_exponent`,
`tr_file_tty_messagesp`, 
`tr_float_can_branch_complex`,
`tr_function_call_default`, 
`tr_numer`,
`tr_optimize_max_loop`, 
`tr_semicompile`,
`tr_state_vars`, 
`tr_warnings_get`,
`tr_warn_bad_function_calls`,
`tr_warn_fexpr`, 
`tr_warn_meval`,
`tr_warn_mode`,
`tr_warn_undeclared`,
y `tr_warn_undefined_variable`.

<!-- category: Other -->
<!-- keywords: transrun -->
<!-- signatures: transrun -->
### Variable: transrun

Valor por defecto: `true`


Si `transrun` vale `false` entonces se ejecutarán las versiones interpretadas de todas las funciones, en lugar de las versiones traducidas.

