## Programación

<!-- category: Programming -->
<!-- keywords: backtrace -->
<!-- signatures: backtrace(), backtrace(n) -->
### Function: backtrace ()

Devuelve la pila de llamadas, esto es, la lista de funciones que han llamado a la función actualmente activa.


La llamada a `backtrace()` devuelve la pila completa de llamadas.


Ejemplos:



```maxima
(%i1) h(x) := g(x/7)$
(%i2) g(x) := f(x-11)$
(%i3) f(x) := e(x^2)$
(%i4) e(x) := (backtrace(), 2*x + 13)$
(%i5) h(10);
#0: e(x=4489/49)
#1: f(x=-67/7)
#2: g(x=10/7)
#3: h(x=10)
                              9615
(%o5)                         ----
                               49
```


La llamada `backtrace (n)` devuelve las *n* funciones más recientes, incluyendo a la función actualmente activa.


Ejemplos:



```maxima
(%i1) h(x) := (backtrace(1), g(x/7))$
(%i2) g(x) := (backtrace(1), f(x-11))$
(%i3) f(x) := (backtrace(1), e(x^2))$
(%i4) e(x) := (backtrace(1), 2*x + 13)$
(%i5) h(10);
#0: h(x=10)
#0: g(x=10/7)
#0: f(x=-67/7)
#0: e(x=4489/49)
                              9615
(%o5)                         ----
                               49
```

<!-- category: Programming -->
<!-- keywords: do -->
<!-- signatures: do -->
### Function: do

La sentencia `do` se utiliza para realizar iteraciones.  Debido a su generalidad la sentencia `do` se describirá en dos partes. En primer lugar se mostrará su forma más usual, análoga a la de otros lenguajes de programación (Fortran, Algol, PL/I, etc.); después se mencionarán otras formas de uso.


Hay tres variantes de esta sentencia que se diferencian entre sí únicamente por las condiciones de fin de bucle. Son las siguientes:



- *
`for variable: valor_inicial step incremento thru límite do cuerpo`
- *
`for variable: valor_inicial step incremento while condición do cuerpo`
- *
`for variable: valor_inicial step incremento unless condición do cuerpo`


El *valor_inicial*, el *incremento*, el *límite* y el *cuerpo* pueden ser cualquier tipo de expresión válida de Maxima. Si el incremento es igual a la unidad (1) entonces "`step 1`" puede omitirse.


La ejecución de la sentencia `do` se realiza asignando el valor_inicial a la variable (llamada de aquí en adelante variable-control). A continuación: (1) si la variable-control ha excedido el límite de la especificación dada por un `thru`, o si la condición impuesta por `unless` es verdadera (`true`), o si la condición dada por `while` es falsa (`false`) entonces la iteración `do` termina. (2) El cuerpo se evalúa.  (3) El incremento es sumado a la variable-control. El proceso de (1) a (3) se repite hasta que la condición de fin de iteración se satisfaga. También es posible especificar varias condiciones de terminación del bucle, en cuyo caso `do` terminará cuando se satisfaga alguna de ellas.


En general la condición `thru` se satisfará cuando la variable-control sea mayor que el límite si el incremento es no negativo, o cuando la variable-control sea menor que el límite cuando el incremento es negativo. El incremento y el límite pueden ser expresiones no numéricas, tanto en cuanto esta desigualdad pueda quedar determinada. Sin embargo, a menos que el incremento sea un número negativo en el momento de comenzar el cómputo de `do`, Maxima supondrá que se evaluará a una cantidad positiva. En caso de no ser efectivamente positivo, la sentencia `do` puede dar un resultado inesperado.


Nótese que el límite, el incremento y la condición de terminación se evalúan en cada iteración del bucle. Así, si alguna de expresiones necesitan de muchos cálculos y devuelven un resultado que no va a cambiar durante toda la ejecución del cuerpo, será más eficiente dar este valor a una variable antes de comenzar la sentencia `do` y utilizarla luego durante su ejecución.


El valor que habitualmente devuelva la sentencia `do` será el átomo `done`. Sin embargo, la función `return` puede usarse dentro del cuerpo para salir de `do` de forma prematura retornando un valor determinado.
Nótese no obstante que un `return` dentro de un `do` que está dentro de un bloque (`block`) provocará una salida de `do` pero no de `block`. Repárese también en que la función `go` no puede usarse para salir de `do` e ir a algún lugar de `block`.


La variable-control es siempre local respecto de `do`, por lo que se puede utilizar cualquier nombre de variable sin afectar el valor de cualquier otra variable externa a `do` y que tenga el mismo nombre. La variable-control no tendrá asignado ningún valor una vez se haya concluido el `do`.



```maxima
(%i1) for a:-3 thru 26 step 7 do display(a)$
                             a = - 3

                              a = 4

                             a = 11

                             a = 18

                             a = 25
```



```maxima
(%i1) s: 0$
(%i2) for i: 1 while i <= 10 do s: s+i;
(%o2)                         done
(%i3) s;
(%o3)                          55
```



Nótese que la condición `while i <= 10` es equivalente a `unless i > 10` y a `thru 10`.



```maxima
(%i1) series: 1$
(%i2) term: exp (sin (x))$
(%i3) for p: 1 unless p > 7 do
          (term: diff (term, x)/p, 
           series: series + subst (x=0, term)*x^p)$
(%i4) series;
                  7    6     5    4    2
                 x    x     x    x    x
(%o4)            -- - --- - -- - -- + -- + x + 1
                 90   240   15   8    2
```


lo que da ocho términos del desarrollo de Taylor de la función `e^sin(x)`.



```maxima
(%i1) poly: 0$
(%i2) for i: 1 thru 5 do
          for j: i step -1 thru 1 do
              poly: poly + i*x^j$
(%i3) poly;
                  5      4       3       2
(%o3)          5 x  + 9 x  + 12 x  + 14 x  + 15 x
(%i4) guess: -3.0$
(%i5) for i: 1 thru 10 do
          (guess: subst (guess, x, 0.5*(x + 10/x)),
           if abs (guess^2 - 10) < 0.00005 then return (guess));
(%o5)                  - 3.162280701754386
```


Este ejemplo calcula la raíz cuadrada negativa de 10 haciendo 10 iteraciones del método de Newton-Raphson. De no haberse alcanzado el criterio de convergencia el valor devuelto hubiese sido `done`.


En lugar de añadir siempre una cantidad a la variable-control a veces se puede querer que cambie en cada iteración siguiendo algún otro criterio. En tal caso se puede hacer uso de `next expresión` en lugar de `step incremento`. Esto hará que a la variable-control se le asigne el resultado de evaluar la expresión en cada iteración del bucle.



```maxima
(%i6) for count: 2 next 3*count thru 20 do display (count)$
                            count = 2

                            count = 6

                           count = 18
```


En ocasiones puede interesar realizar una iteración en la que la variable-control no se utilice nunca. Se podrá entonces dar únicamente las condiciones de terminación del bucle omitiendo la inicialización y actualizando la información, tal como se hace en el siguiente ejemplo para calcular la raíz cuadrada de 5 utilizando un valor inicial alejado de la solución.



```maxima
(%i1) x: 1000$
(%i2) thru 20 do x: 0.5*(x + 5.0/x)$
(%i3) x;
(%o3)                   2.23606797749979
(%i4) sqrt(5), numer;
(%o4)                   2.23606797749979
```


Si así se quiere, incluso es posible omitir las condiciones de terminación completamente y escribir únicamente `do body`, lo que provocará entrar en un bucle infinito. En tal caso, debería usarse la función `return` a fin de terminar con la ejecución de `do`.



```maxima
(%i1) newton (f, x):= ([y, df, dfx], df: diff (f ('x), 'x),
          do (y: ev(df), x: x - f(x)/y, 
              if abs (f (x)) < 5e-6 then return (x)))$
(%i2) sqr (x) := x^2 - 5.0$
(%i3) newton (sqr, 1000);
(%o3)                   2.236068027062195
```


(En este ejemplo, cuando se ejecuta `return` obliga a que sea `x` el valor devuelto por `do`. Al salirse del bloque, `x` es también el valor que devuelve `block` por ser `do` la última sentencia del bloque.)


Hay todavía otra forma de `do` en Maxima. Su sintaxis es:



```maxima
for variable in lista test_de_parada do cuerpo
```


Los elementos de *list* son cualesquiera expresiones que se irán asignando sucesivamente a la variable en cada repetición del cuerpo. El test de parada *end_tests* (que es opcional) puede usarse para terminar la ejecución de `do`; de otro modo las iteraciones se pararán cuando la lista se haya agotado o cuando se ejecute un `return` dentro del cuerpo.  (De hecho, la lista puede ser cualquier expresión no atómica, de la cual se irán extrayendo de forma sucesiva sus diferentes partes.)



```maxima
(%i1)  for f in [log, rho, atan] do ldisp(f(1))$
(%t1)                                  0
(%t2)                                rho(1)
                                     %pi
(%t3)                                 ---
                                      4
(%i4) ev(%t3,numer);
(%o4)                             0.78539816
```

<!-- category: Programming -->
<!-- keywords: errcatch -->
<!-- signatures: errcatch(expr_1, ..., expr_n) -->
### Function: errcatch (expr_1, ..., expr_n)

Evalúa las expresiones *expr_1*, ..., *expr_n* una a una y devuelve `[expr_n]` (una lista) en caso de que no ocurra ningún error. En caso de aparecer algún error durante el cálculo de alguno de los argumentos, `errcatch` evita que el error se propague y devuelve la lista vacía `[]` sin evaluar más argumentos.


La función `errcatch` es útil en ficheros `batch` donde se sospeche que pueda aparecer algún error, el cual provocaría la terminación de la ejecución del `batch` de no ser previamente detectado.

<!-- category: Programming -->
<!-- keywords: error -->
<!-- signatures: error(expr_1, ..., expr_n) -->
### Function: error (expr_1, ..., expr_n)

Calcula y devuelve *expr_1*, ..., *expr_n*, enviando posteriormente una seãl de error a Maxima o al `errcatch` más cercano. 


A la variable `error` se le asigna una lista con la descripción del error. El primer elemento de `error` es una cadena de formato, la cual une todas las cadenas de los argumentos *expr_1*, ..., *expr_n*, siendo los demás elementos de la lista los valores de los argumentos que no son cadenas.


La llamada a `errormsg()` formatea e imprime `error`. Se reimprime así el mensaje de error más reciente.

<!-- category: Programming -->
<!-- keywords: error_size -->
<!-- signatures: error_size -->
### Variable: error_size

Valor por defecto: 10


La variable `error_size` modifica los mensajes de error de acuerdo con el tamaño de las expresiones que aparecen en él. Si el tamaño de una expresión (tal como lo determina la función Lisp `ERROR-SIZE`)
es mayor que `error_size`, la expresión se reemplaza en el mensaje por un símbolo, asignándole a éste una expresión. Los símbolos se toman de la lista `error_syms`.


En caso contrario, si la expresión es menor que `error_size`, la expresión se muestra en el propio mensaje.


Véanse también `error` y `error_syms`.


Ejemplo:









El tamaño de `U`, tal como lo determina `ERROR-SIZE`, es 24.



```maxima
(%i1) U: (C^D^E + B + A)/(cos(X-1) + 1)$

(%i2) error_size: 20$

(%i3) error ("Example expression is", U);

Example expression is errexp1
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) errexp1;
                            E
                           D
                          C   + B + A
(%o4)                    --------------
                         cos(X - 1) + 1
(%i5) error_size: 30$

(%i6) error ("Example expression is", U);

                         E
                        D
                       C   + B + A
Example expression is --------------
                      cos(X - 1) + 1
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Programming -->
<!-- keywords: error_syms -->
<!-- signatures: error_syms -->
### Variable: error_syms

Valor por defecto: `[errexp1, errexp2, errexp3]`


En los mensajes de error, las expresiones mayores que `error_size` son reemplazadas por símbolos a los cuales se les asignas estas expresiones.  Los símbolos se toman de la lista `error_syms`. La primera expresión que resulte ser demasiado larga se reemplaza por `error_syms[1]`, la segunda por `error_syms[2]` y así sucesivamente.


Si hay más expresiones largas que elementos en `error_syms`, los símbolos se construyen automáticamente, siendo el *n*-ésimo símbolo equivalente a `concat ('errexp, n)`.


Véanse también `error` y `error_size`.

<!-- category: Programming -->
<!-- keywords: errormsg -->
<!-- signatures: errormsg() -->
### Function: errormsg ()

Reimprime el mensaje de error más reciente. La variable `error` guarda el mensaje y `errormsg` lo formatea e imprime.

<!-- category: Programming -->
<!-- keywords: for -->
<!-- signatures: for -->
### Function: for

Utilizado en las iteraciones. Véase `do` para una descripción de las técnicas de iteración en Maxima.

<!-- category: Programming -->
<!-- keywords: go -->
<!-- signatures: go(etiqueta) -->
### Function: go (etiqueta)

Se utiliza dentro de un bloque (`block`) para transferir el control a la sentencia del bloque que esté etiquetada con el argumento de `go`. Una sentencia queda etiquetada cuando está precedida por un argumento de tipo átomo como cualquier otra sentencia de `block`.  Por ejemplo:



```maxima
block ([x], x:1, tururu, x+1, ..., go(tururu), ...)
```


El argumento de `go` debe ser el nombre de una etiqueta que aparezca en el mismo bloque (`block`). No se puede utilizar `go` para transferir el control a un bloque que no sea aquel que contenga la sentencia `go`.

<!-- category: Programming -->
<!-- keywords: if -->
<!-- signatures: if -->
### Function: if

Evaluación condicionada. Se reconocen varias formas de expresiones `if`.


La expresión `if cond_1 then expr_1 else expr_0`
devuelve *expr_1* si *cond_1* vale `true`,
en caso contrario la respuesta es `expr_0`.


La expresión `if cond_1 then expr_1 elseif cond_2 then expr_2 elseif ... else expr_0`
devuelve *expr_k* si *cond_k* vale `true` y todas las
condiciones anteriores toman el valor `false`.
Si ninguna de las condiciones vale `true`, la respuesta es `expr_0`.


La falta de un `else` final se interpreta como un `else false`;
esto es, la expresión `if cond_1 then expr_1`
equivale a `if cond_1 then expr_1 else false`,
y `if cond_1 then expr_1 elseif ... elseif cond_n then expr_n`
equivale a su vez a
`if cond_1 then expr_1 elseif ... elseif cond_n then expr_n else false`.


Las alternativas *expr_0*, ..., *expr_n* pueden ser expresiones
válidas de Maxima, incluidas expresiones `if` anidadas.
Las alternativas ni se simplifican ni se evalúan, a menos que su
condición asociada valga `true`.


Las condiciones *cond_1*, ..., *cond_n* deben ser expresiones 
capaces de dar como resultado `true` o `false` al ser
evaluadas. Si en un momento dado una condición no da como resultado 
un valor de verdad (`true` o `false`), el comportamiento de `if` se controla
con la variable global `prederror`. Si `prederror` vale `true`,
se considera un error que la condición evaluada no dé como resultado
un valor de verdad; en caso contrario, las condiciones que no
den como resultado un valor de verdad se aceptan, dándose el
resultado como una expresión condicional.


Las condiciones pueden contener operadores lógicos y relacionales, 
así como otros elementos, tal como se indica a continuación:




```maxima
Operación               Símbolo     Tipo
 
menor que               <           operador relacional infijo
menor o igual que       <=          operador relacional infijo
igualdad (sintáctica)   =           operador relacional infijo
negación de =           #           operador relacional infijo
igualdad (por valor)    equal       operador relacional infijo
negación de equal       notequal    operador relacional infijo
mayor o igual que       >=          operador relacional infijo
mayor que               >           operador relacional infijo
y                       and         operador lógico infijo
o                       or          operador lógico infijo
no                      not         operador lógico prefijo
```

<!-- category: Programming -->
<!-- keywords: map -->
<!-- signatures: map(f, expr_1, ..., expr_n) -->
### Function: map (f, expr_1, ..., expr_n)

Devuelve una expresión cuyo operador principal es el mismo 
que aparece en las expresiones *expr_1*, ..., *expr_n* 
pero cuyas subpartes son los resultados de aplicar *f* 
a cada una de las subpartes de las expresiones;  *f* puede ser 
tanto el nombre de una función de $n$ argumentos como
una expresión `lambda` de $n$ argumentos.


Uno de los usos que tiene `map` es la de aplicar (o mapear)
una función (por ejemplo, `partfrac`) sobre cada término
de una expresión extensa en la que normalmente no se 
podría utilizar la función debido a insuficiencias 
en el espacio de almacenamiento durante el curso de un cálculo.



```maxima
(%i1) map(f,x+a*y+b*z);
(%o1)                        f(b z) + f(a y) + f(x)
(%i2) map(lambda([u],partfrac(u,x)),x+1/(x^3+4*x^2+5*x+2));
                           1       1        1
(%o2)                     ----- - ----- + -------- + x
                         x + 2   x + 1          2
                                         (x + 1)
(%i3) map(ratsimp, x/(x^2+x)+(y^2+y)/y);
                                      1
(%o3)                            y + ----- + 1
                                    x + 1
(%i4) map("=",[a,b],[-0.5,3]);
(%o4)                          [a = - 0.5, b = 3]
```


Véase también `maperror` .

<!-- category: Programming -->
<!-- keywords: mapatom -->
<!-- signatures: mapatom(expr) -->
### Function: mapatom (expr)

Devuelve `true` si y sólo *expr* es tratado por las rutinas de mapeo como un átomo.

<!-- category: Programming -->
<!-- keywords: maperror -->
<!-- signatures: maperror -->
### Variable: maperror

Valor por defecto: `true`


Cuando `maperror` toma el valor `false`, 
hace que todas las funciones de mapeo, como por ejemplo



```maxima
map (f, expr_1, expr_2, ...)
```


(1) paren cuando hayan terminado de procesar la *expr_i* más corta,
a menos que todas ellas sean del mismo tamaño y (2) apliquen  `f`
a `[expr_1, expr_2, ...]` si es el caso que las `expr_i`
no son todas del mismo tipo de objeto.


Cuando `maperror` toma el valor `true` entonces se emite un mensaje de error cuando se presenta cualquiera de los dos casos anteriores.

<!-- category: Programming -->
<!-- keywords: maplist -->
<!-- signatures: maplist(f, expr_1, ..., expr_n) -->
### Function: maplist (f, expr_1, ..., expr_n)

Devuelve una lista con las aplicaciones de *f* a las partes de las expresiones *expr_1*, ..., *expr_n*; *f* es el nombre de una función ou una expresión lambda.


La función `maplist` difiere de `map (f, expr_1, ..., expr_n)`, la cual devuelve una expresión con el mismo operador principal que tenga *expr_i*, excepto en simplificaciones y en el caso en el que `map` hace un `apply`.

<!-- category: Programming -->
<!-- keywords: mapprint -->
<!-- signatures: mapprint -->
### Variable: mapprint

Valor por defecto: `true`


Si `mapprint` vale `true`, se producirán ciertos mensajes
por parte de las funciones `map`, `mapl` y `fullmap`
en determinadas situaciones, como cuando `map` hace uso de
`apply`.


Si `mapprint` vale `false`, no se emitirán tales mensajes.

<!-- category: Programming -->
<!-- keywords: outermap -->
<!-- signatures: outermap(f, a_1, ..., a_n) -->
### Function: outermap (f, a_1, ..., a_n)

Aplica la función *f* a cada uno de los elementos del producto vectorial *a_1* por *a_2* ... por *a_n*.


El argumento *f* debe ser el nombre de una función de $n$ argumentos,
o una expresión lambda de $n$ argumentos.
Cada uno de los argumentos *a_k* puede ser una lista, una lista anidada, 
una matriz o cualquier otro tipo de expresión.


El valor devuelto por `outermap` es una estructura anidada. Si *x* es la
respuesta dada por `outermap`, entonces tiene la misma estructura que la primera lista,
lista anidada o matriz, `x[i_1]...[i_m]` tiene la misma estructura que la
segunda lista, lista anidada o matriz, `x[i_1]...[i_m][j_1]...[j_n]` tiene 
la misma estructura que la tercera lista, lista anidada o matriz, y así
sucesivamente, siendo *m*, *n*, ... los números índice
necesarios para acceder a los elementos de cada argumento: uno para las listas,
dos para las matrices y uno o más para las listas anidadas. 
Aquellos argumentos que no sean listas ni matrices no tienen efecto alguno sobre
la estructura del valor retornado.


Nótese que el efecto producido por `outermap` es diferente del que
se obtiene al aplicar *f* a cada uno de los elementos del producto
devuelto por `cartesian_product`. La función `outermap`
mantiene la estructura de los argumentos en la respuesta, miemtras que
`cartesian_product` no lo hace.


La función `outermap` evalúa sus argumentos.


Véanse también `map`, `maplist` y `apply`.


Ejemplos:


Ejemplos elementales de uso de `outermap`.
Con el fin de mostrar con mayor claridad las combinaciones del argumento,
se mantiene sin definir `F`.











```maxima
(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) outermap (F, matrix ([a, b], [c, d]), matrix ([1, 2], [3, 4]));
         [ [ F(a, 1)  F(a, 2) ]  [ F(b, 1)  F(b, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(a, 3)  F(a, 4) ]  [ F(b, 3)  F(b, 4) ] ]
(%o2)    [                                            ]
         [ [ F(c, 1)  F(c, 2) ]  [ F(d, 1)  F(d, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(c, 3)  F(c, 4) ]  [ F(d, 3)  F(d, 4) ] ]
(%i3) outermap (F, [a, b], x, matrix ([1, 2], [3, 4]));
       [ F(a, x, 1)  F(a, x, 2) ]  [ F(b, x, 1)  F(b, x, 2) ]
(%o3) [[                        ], [                        ]]
       [ F(a, x, 3)  F(a, x, 4) ]  [ F(b, x, 3)  F(b, x, 4) ]
(%i4) outermap (F, [a, b], matrix ([1, 2]), matrix ([x], [y]));
       [ [ F(a, 1, x) ]  [ F(a, 2, x) ] ]
(%o4) [[ [            ]  [            ] ], 
       [ [ F(a, 1, y) ]  [ F(a, 2, y) ] ]
                              [ [ F(b, 1, x) ]  [ F(b, 2, x) ] ]
                              [ [            ]  [            ] ]]
                              [ [ F(b, 1, y) ]  [ F(b, 2, y) ] ]
(%i5) outermap ("+", [a, b, c], [1, 2, 3]);
(%o5) [[a + 1, a + 2, a + 3], [b + 1, b + 2, b + 3], 
                                           [c + 1, c + 2, c + 3]]
```


El siguiente ejemplo permite hacer un análisis más profundo del valor
retornado por `outermap`.
Los tres primeros argumentos son una matriz, una lista y otra matriz, en este
orden. El valor devuelto es una matriz, cuyos elementos son listas y
cada elemento de cada una de estas listas es a su vez una matriz.















```maxima
(%i1) arg_1 :  matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) arg_2 : [11, 22];
(%o2)                       [11, 22]
(%i3) arg_3 : matrix ([xx, yy]);
(%o3)                      [ xx  yy ]
(%i4) xx_0 : outermap(lambda([x, y, z], x / y + z), arg_1,
                                                   arg_2, arg_3);
               [  [      a        a  ]  [      a        a  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
(%o4)  Col 1 = [                                              ]
               [  [      c        c  ]  [      c        c  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
                 [  [      b        b  ]  [      b        b  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
         Col 2 = [                                              ]
                 [  [      d        d  ]  [      d        d  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
(%i5) xx_1 : xx_0 [1][1];
           [      a        a  ]  [      a        a  ]
(%o5)     [[ xx + --  yy + -- ], [ xx + --  yy + -- ]]
           [      11       11 ]  [      22       22 ]
(%i6) xx_2 : xx_0 [1][1] [1];
                      [      a        a  ]
(%o6)                 [ xx + --  yy + -- ]
                      [      11       11 ]
(%i7) xx_3 : xx_0 [1][1] [1] [1][1];
                                  a
(%o7)                        xx + --
                                  11
(%i8) [op (arg_1), op (arg_2), op (arg_3)];
(%o8)                  [matrix, [, matrix]
(%i9) [op (xx_0), op (xx_1), op (xx_2)];
(%o9)                  [matrix, [, matrix]
```


La función `outermap` mantiene la estructura de los argumentos en su respuesta,
mientras que `cartesian_product` no lo hace.









```maxima
(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) setify (flatten (%));
(%o2) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i3) map (lambda ([L], apply (F, L)), cartesian_product ({a, b, c}, {1, 2, 3}));
(%o3) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i4) is (equal (%, %th (2)));
(%o4)                         true
```

<!-- category: Programming -->
<!-- keywords: prederror -->
<!-- signatures: prederror -->
### Variable: prederror

Valor por defecto: `false`


Cuando `prederror` toma el valor `true`, se emite un mensaje de error siempre que el predicado de una sentencia  `if` o de una función `is` no se pueda evaluar ni a verdadero (`true`) ni  a falso (`false`).


Si toma el valor `false`, se devuelve bajo las mismas circunstancias anteriores el valor `unknown`. El modo `prederror: false` no está soportado en el código traducido; sin embargo, `maybe` está soportado en código traducido.


Véanse también `is` y `maybe`.

<!-- category: Programming -->
<!-- keywords: return -->
<!-- signatures: return(valor) -->
### Function: return (valor)

Puede utilizarse para salir de un bloque, devolviendo su argumento.
Véase `block` para más información.

<!-- category: Programming -->
<!-- keywords: scanmap -->
<!-- signatures: scanmap(f, expr), scanmap(f, expr, bottomup) -->
### Function: scanmap (f, expr)

Aplica recursivamente *f* sobre *expr*, de arriba hacia abajo. Esto es más útil cuando se busca una factorización completa, por ejemplo:



```maxima
(%i1) exp:(a^2+2*a+1)*y + x^2$
(%i2) scanmap(factor,exp);
                                    2      2
(%o2)                         (a + 1)  y + x
```


Nótese que cómo `scanmap` aplica la función dada `factor` a las subexpresiones que forman a *expr*; si se presenta otra forma de *expr* a `scanmap` entonces el resultado puede ser diferente. Así, `%o2` no se restaura cuando `scanmap` se aplica a la forma expandida de exp:



```maxima
(%i3) scanmap(factor,expand(exp));
                           2                  2
(%o3)                      a  y + 2 a y + y + x
```


Aquí hay otro ejemplo de la forma en que `scanmap` aplica recursivamente una función dada a todas las subexpresiones, incluyendo exponentes:



```maxima
(%i4) expr : u*v^(a*x+b) + c$
(%i5) scanmap('f, expr);
                    f(f(f(a) f(x)) + f(b))
(%o5) f(f(f(u) f(f(v)                      )) + f(c))
```


`scanmap (f, expr, bottomup)` aplica *f* a *expr* de abajo hacia arriba. Por ejemplo, para `f` no definida,



```maxima
scanmap(f,a*x+b) ->
   f(a*x+b) -> f(f(a*x)+f(b)) -> f(f(f(a)*f(x))+f(b))
scanmap(f,a*x+b,bottomup) -> f(a)*f(x)+f(b)
    -> f(f(a)*f(x))+f(b) ->
     f(f(f(a)*f(x))+f(b))
```


En este caso se obtiene la misma respuesta por cualquiera de los dos métodos.

<!-- category: Programming -->
<!-- keywords: throw -->
<!-- signatures: throw(expr) -->
### Function: throw (expr)

Evalúa *expr* y devuelve el valor del `catch` más reciente. La función `throw` se utiliza junto con `catch` como un mecanismo de retorno no local.

<!-- category: Programming -->
<!-- keywords: while, unless -->
<!-- signatures: unless -->
### Function: while

Véase `do`.

