## Expresiones

<!-- category: Other -->
<!-- keywords: alias -->
<!-- signatures: alias(new_name_1, old_name_1, ..., new_name_n, old_name_n) -->
### Function: alias (new_name_1, old_name_1, ..., new_name_n, old_name_n)

provee un nombre
alternativo para una (bien sea definida por el usuario o por el sistema) función, variable, arreglo, etc. 
Cualquier número par de argumentos puede ser usado.

<!-- category: Other -->
<!-- keywords: aliases -->
<!-- signatures: aliases -->
### Variable: aliases

Valor por defecto: `[]`


La variable `aliases` es la lista de átomos que tienen un "alias" definido por el usuario (establecido mediante las funciones  `alias`, `ordergreat` o `orderless` o declarando el átomo como un `noun` (nombre) con `declare`.

<!-- category: Other -->
<!-- keywords: allbut -->
<!-- signatures: allbut -->
### Variable: allbut

Opera con los comandos `part` (como `part`, `inpart`, `substpart`,
`substinpart`, `dpart` y `lpart`). Por ejemplo:







```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, [2, 5]);
(%o2)                         d + a
```


mientras que: 







```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, allbut (2, 5));
(%o2)                       e + c + b
```


La función `kill` también reconoce a `allbut`.








```maxima
(%i1) [aa : 11, bb : 22, cc : 33, dd : 44, ee : 55];
(%o1)                 [11, 22, 33, 44, 55]
(%i2) kill (allbut (cc, dd));
(%o0)                         done
(%i1) [aa, bb, cc, dd];
(%o1)                   [aa, bb, 33, 44]
```


La sentencia `kill(allbut(a_1, a_2, ...))`
tiene el mismo efecto que `kill(all)`, excepto que no
elimina los símbolos *a_1*, *a_2*, ... .

<!-- category: Other -->
<!-- keywords: args -->
<!-- signatures: args(expr) -->
### Function: args (expr)

Devuelve la lista de argumentos de `expr`, que puede ser cualquier tipo de expresión a excepción de un átomo. Tan solo se muestran los argumentos del operador principal; subexpresiones de `expr` aparecen como elementos o subexpresiones de elementos de la lista de argumentos.


El orden de los miembros de la lista puede depender de la variable global `inflag`.


La llamada `args (expr)` es equivalente a `substpart ("[", expr, 0)`.


Véanse también `substpart` y `op`.

<!-- category: Other -->
<!-- keywords: atom -->
<!-- signatures: atom(expr) -->
### Function: atom (expr)

Devuelve `true` si *expr* es un átomo (número, nombre o cadena alfanumérica) y `false` en caso contario. Así, `atom(5)` devolverá `true`, mientras que `atom(a[1])` y `atom(sin(x))` darán como resultado `false` (dando por hecho que tanto `a[1]` como `x` no tienen valores asignados).

<!-- category: Other -->
<!-- keywords: box -->
<!-- signatures: box(expr), box(expr, a) -->
### Function: box (expr)

Devuelve *expr* encerrada en una caja.
El valor devuelto es una expresión con `box` como operador y *expr* como argumento.
Se dibujará una caja cuando `display2d` valga `true`.


La llamada `box (expr, a)`
encierra *expr* en una caja etiquetada con el símbolo *a*.
La etiqueta se recorta si es más larga que el ancho de la caja.


La función `box` evalúa su argumento. Sin embargo, la expresión 
encerrada no se evalúa, siendo excluída de los cálculos.


La variable `boxchar` guarda el carácter a utilizar para dibujar la caja en las funciones `box`, `dpart` y `lpart`.


Ejemplos:













```maxima
(%i1) box (a^2 + b^2);
                            """""""""
                            " 2    2"
(%o1)                       "b  + a "
                            """""""""
(%i2) a : 1234;
(%o2)                         1234
(%i3) b : c - d;
(%o3)                         c - d
(%i4) box (a^2 + b^2);
                      """"""""""""""""""""
                      "       2          "
(%o4)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i5) box (a^2 + b^2, term_1);
                      term_1""""""""""""""
                      "       2          "
(%o5)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i6) 1729 - box (1729);
                                 """"""
(%o6)                     1729 - "1729"
                                 """"""
(%i7) boxchar: "-";
(%o7)                           -
(%i8) box (sin(x) + cos(y));
                        -----------------
(%o8)                   -cos(y) + sin(x)-
                        -----------------
```

<!-- category: Other -->
<!-- keywords: boxchar -->
<!-- signatures: boxchar -->
### Variable: boxchar

Valor por defecto: `"`


La variable `boxchar` guarda el carácter a utilizar para dibujar la caja en las funciones `box`, `dpart` y `lpart`.


Todas las cajas en una expresión se dibujan con el valor actual de `boxchar`, carácter que no se almacena con las expresión encerrada.

<!-- category: Other -->
<!-- keywords: collapse -->
<!-- signatures: collapse(expr) -->
### Function: collapse (expr)

Colapsa *expr* haciendo que todas las subexpresiones que sean iguales
compartan las mismas celdas, ahorrando espacio. `collapse` es una
subrutina utilizada por la instrucción `optimize`. El uso de 
`collapse` puede ser útil después de  cargar un fichero 
creado con `save`. Se pueden colapsar varias expresiones de forma
conjunta utilizando `collapse ([expr_1, ..., expr_n])`.
También se pueden colapsar los elementos del array `A`
haciendo `collapse (listarray ('A))`.

<!-- category: Other -->
<!-- keywords: disolate -->
<!-- signatures: disolate(expr, x_1, ..., x_n) -->
### Function: disolate (expr, x_1, ..., x_n)

Es similar a `isolate (expr, x)`, excepto que permite al usuario aislar más de una variable simultáneamente. Puede ser útil para hacer un cambio de variables en integrales múltiples en las que tales variables dependan de de dos o más variables de integración.  Esta función se carga automáticamente desde 
`simplification/disol.mac`.  Se dispone de una demostyración en `demo("disol")$`.

<!-- category: Other -->
<!-- keywords: dispform -->
<!-- signatures: dispform(expr), dispform(expr, all) -->
### Function: dispform (expr)

`dispform(expr)` devuelve la representación externa de
*expr* respecto del operador del nivel superior.
`dispform(expr, all)` devuelve la representación
externa respecto de todos los operadores que haya en *expr*.


Véase también `part`, `inpart` y `inflag`.


Ejemplos:


La representación interna de `- x` es "menos uno 
multiplicado por `x`", mientras que la representación externa es
"menos `x`".









```maxima
(%i1) - x;
(%o1)                          - x
(%i2) ?format (true, "~S~%", %);
((MTIMES SIMP) -1 $X)
(%o2)                         false
(%i3) dispform (- x);
(%o3)                          - x
(%i4) ?format (true, "~S~%", %);
((MMINUS SIMP) $X)
(%o4)                         false
```


La representación interna de `sqrt(x)` es 
"`x` elevado a 1/2", mientras que su representación
externa es "raíz de `x`".









```maxima
(%i1) sqrt (x);
(%o1)                        sqrt(x)
(%i2) ?format (true, "~S~%", %);
((MEXPT SIMP) $X ((RAT SIMP) 1 2))
(%o2)                         false
(%i3) dispform (sqrt (x));
(%o3)                        sqrt(x)
(%i4) ?format (true, "~S~%", %);
((%SQRT SIMP) $X)
(%o4)                         false
```


Utilización del argumento opcional `all`.









```maxima
(%i1) expr : sin (sqrt (x));
(%o1)                     sin(sqrt(x))
(%i2) freeof (sqrt, expr);
(%o2)                         true
(%i3) freeof (sqrt, dispform (expr));
(%o3)                         true
(%i4) freeof (sqrt, dispform (expr, all));
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: dpart -->
<!-- signatures: dpart(expr, n_1, ..., n_k) -->
### Function: dpart (expr, n_1, ..., n_k)

Selecciona la misma expresión que `part`, pero en lugar de devolver esa expresión como su valor, devuelve la expresión completa con la subexpresión seleccionada dentro de una caja. La caja es parte de la expresión.



```maxima
(%i1) dpart (x+y/z^2, 1, 2, 1);
                             y
(%o1)                       ---- + x
                               2
                            """
                            "z"
                            """
```

<!-- category: Other -->
<!-- keywords: exptisolate -->
<!-- signatures: exptisolate -->
### Variable: exptisolate

Valor por defecto: `false`


Véase `isolate`.

<!-- category: Other -->
<!-- keywords: exptsubst -->
<!-- signatures: exptsubst -->
### Variable: exptsubst

Valor por defecto: `false`


Si `exptsubst` vale `true` permite la sustitución `y` por `%e^x` en `%e^(a x)`.

<!-- category: Other -->
<!-- keywords: freeof -->
<!-- signatures: freeof(x_1, ..., x_n, expr) -->
### Function: freeof (x_1, ..., x_n, expr)

`freeof (x_1, expr)`
devuelve `true` si ninguna subexpresión de *expr* coincide con *x_1*,
o si *x_1* aparece como variable muda en *expr*, o si *x_1* no es ni
una forma nominal ni verbal de cualesquiera operadores presentes en *expr*,
devolviendo `false` en otro caso.


La llamada `freeof (x_1, ..., x_n, expr)`
equivale a `freeof (x_1, expr) and ... and freeof (x_n, expr)`.


Los argumentos *x_1*, ..., *x_n* 
pueden seer nombres de funciones y variables, nombres subindicados,
operadores (encerrados entre comillas dobles) o expresiones generales.


La función `freeof` evalúa sus argumentos.


Una variable es una variable muda en una expresión si no tiene valor asignado fuera de la expresión.
Variable mudas reconocidas por  `freeof` son el índice de una suma o producto, la variable límite en `limit`,
la variable de integración en la versión de integral definida de `integrate`,
la variable original en `laplace`,
variables formales en expresiones `at` y
los argumentos de las expresiones  `lambda`.


La versión indefinida de  `integrate` no está libre de su variable de integración.


Ejemplos:


Los argumentos son nombres de funciones, variables, nombres subindicados, operaores y expresiones. La llamada `freeof (a, b, expr)` equivale a `freeof (a, expr) and freeof (b, expr)`.



```maxima
(%i1) expr: z^3 * cos (a[1]) * b^(c+d);
                                 d + c  3
(%o1)                   cos(a ) b      z
                             1
(%i2) freeof (z, expr);
(%o2)                         false
(%i3) freeof (cos, expr);
(%o3)                         false
(%i4) freeof (a[1], expr);
(%o4)                         false
(%i5) freeof (cos (a[1]), expr);
(%o5)                         false
(%i6) freeof (b^(c+d), expr);
(%o6)                         false
(%i7) freeof ("^", expr);
(%o7)                         false
(%i8) freeof (w, sin, a[2], sin (a[2]), b*(c+d), expr);
(%o8)                         true
```


`freeof` evalúa sus argumentos.



```maxima
(%i1) expr: (a+b)^5$
(%i2) c: a$
(%i3) freeof (c, expr);
(%o3)                         false
```


`freeof` no considera funciones equivalentes.
La simplificación puede dar una expresión equivalente pero diferente.



```maxima
(%i1) expr: (a+b)^5$
(%i2) expand (expr);
          5        4       2  3       3  2      4      5
(%o2)    b  + 5 a b  + 10 a  b  + 10 a  b  + 5 a  b + a
(%i3) freeof (a+b, %);
(%o3)                         true
(%i4) freeof (a+b, expr);
(%o4)                         false
(%i5) exp (x);
                                 x
(%o5)                          %e
(%i6) freeof (exp, exp (x));
(%o6)                         true
```


Un sumatorio o integral definida está libre de su variable muda.
Una integral indefinida de  `integrate` no está libre de su variable de integración.



```maxima
(%i1) freeof (i, 'sum (f(i), i, 0, n));
(%o1)                         true
(%i2) freeof (x, 'integrate (x^2, x, 0, 1));
(%o2)                         true
(%i3) freeof (x, 'integrate (x^2, x));
(%o3)                         false
```

<!-- category: Other -->
<!-- keywords: inflag -->
<!-- signatures: inflag -->
### Variable: inflag

Valor por defecto: `false`


Si `inflag` vale `true`, las funciones para la extracción de partes inspeccionan la forma interna de `expr`.


Nótese que el simplificador reordena expresiones.
Así,  `first (x + y)` devuelve `x` si `inflag`
vale `true` y `y` si `inflag` vale `false`.
(`first (y + x)` devuelve el mismo resultado.)


Además, dándole a  `inflag` el valor `true` y llamando a `part` o  a `substpart` es lo mismo que llamar a `inpart` o a `substinpart`.


Las funciones que se ven afectadas por el valor de `inflag` son:
`part`, `substpart`, `first`, `rest`, `last`, `length`,
la construcción `for` ... `in`,
`map`, `fullmap`, `maplist`, `reveal` y `pickapart`.

<!-- category: Other -->
<!-- keywords: inpart -->
<!-- signatures: inpart(expr, n_1, ..., n_k) -->
### Function: inpart (expr, n_1, ..., n_k)

Similar a `part`, pero trabaja con la representación interna de la expresión, siendo más rápida. Se debe tener cuidado con el orden de subexpresiones en sumas y productos, pues el orden de las variables en la forma interna es normalmente diferente al que se muestra por el terminal, y cuando se trata con el signo menos unario, resta y división, pues estos operadores desaparecen de la expresión. Las llamadas `part (x+y, 0)` o `inpart (x+y, 0)` devuelven `+`, siendo necesario encerrar el operador entre comillas dobles cuando se haga referencia aél. Por ejemplo,
`... if inpart (%o9,0) = "+" then ...`.


Ejemplos:



```maxima
(%i1) x + y + w*z;
(%o1)                      w z + y + x
(%i2) inpart (%, 3, 2);
(%o2)                           z
(%i3) part (%th (2), 1, 2);
(%o3)                           z
(%i4) 'limit (f(x)^g(x+1), x, 0, minus);
                                  g(x + 1)
(%o4)                 limit   f(x)
                      x -> 0-
(%i5) inpart (%, 1, 2);
(%o5)                       g(x + 1)
```

<!-- category: Other -->
<!-- keywords: isolate -->
<!-- signatures: isolate(expr, x) -->
### Function: isolate (expr, x)

Devuelve *expr* con subexpresiones que son sumas y que no contienen variables reemplazadas por etiquetas de expresiones intermedias (tales etiquetas son símbolos atómicos como `%t1`, `%t2`, ...).  Esta función es de utilidad para evitar la expansión innecesaria de subexpresiones que no contienen la variable de interés. Puesto que las etiquetas intermedias toman el valor de subexpresiones pueden ser todas sustituidas evaluando la expresión en la que aparecen.


Si la variable `exptisolate`, cuyo valor por defecto es `false`, vale `true` hará que `isolate` busque exponentes de átomos (como `%e`) que contengan la variable.


Si `isolate_wrt_times` vale `true`, entonces `isolate` también aislará respecto de los productos. Véase `isolate_wrt_times`.


Para ejemplos, ejecútese `example (isolate)`.

<!-- category: Other -->
<!-- keywords: isolate_wrt_times -->
<!-- signatures: isolate_wrt_times -->
### Variable: isolate_wrt_times

Valor por defecto: `false`


Si `isolate_wrt_times` vale `true`, entonces `isolate` también aislará respecto de los productos. Compárese el comportamiento de `isolate` al cambiar el valor de esta variable global en el siguiente ejemplo,



```maxima
(%i1) isolate_wrt_times: true$
(%i2) isolate (expand ((a+b+c)^2), c);

(%t2)                          2 a


(%t3)                          2 b


                          2            2
(%t4)                    b  + 2 a b + a

                     2
(%o4)               c  + %t3 c + %t2 c + %t4
(%i4) isolate_wrt_times: false$
(%i5) isolate (expand ((a+b+c)^2), c);
                     2
(%o5)               c  + 2 b c + 2 a c + %t4
```

<!-- category: Other -->
<!-- keywords: lfreeof -->
<!-- signatures: lfreeof(list, expr) -->
### Function: lfreeof (list, expr)

Para cada miembro  *m* de *list*, realiza la llamada `freeof (m, expr)`.
Devuelve `false` si alguna de estas llamadas a `freeof` retornó `false`, y `true` en caso contrario.

<!-- category: Other -->
<!-- keywords: listconstvars -->
<!-- signatures: listconstvars -->
### Variable: listconstvars

Valor por defecto: `false`


Si `listconstvars` vale `true`, hará que `listofvars` incluya `%e`, `%pi`, `%i` y cualquier otra variable que sea declarada constante de las que aparezcan en el argumento de `listofvars`.
Estas constantes se omiten por defecto.

<!-- category: Other -->
<!-- keywords: listdummyvars -->
<!-- signatures: listdummyvars -->
### Variable: listdummyvars

Valor por defecto: `true`


Si `listdummyvars` vale `false`, las "variables mudas" de la expresión no serán incluídas en la lista devuelta por `listofvars`. (La definición de "variables mudas" se encuentra en la descripción de `freeof`.
"Variables mudas" son objetos matemáticos como el índice de un sumatorio o producto, una variable límite o la variable de una integración definida.)
Ejemplo:



```maxima
(%i1) listdummyvars: true$
(%i2) listofvars ('sum(f(i), i, 0, n));
(%o2)                        [i, n]
(%i3) listdummyvars: false$
(%i4) listofvars ('sum(f(i), i, 0, n));
(%o4)                          [n]
```

<!-- category: Other -->
<!-- keywords: listofvars -->
<!-- signatures: listofvars(expr) -->
### Function: listofvars (expr)

Devuelve una lista con las variables presentes en *expr*.


Si la variable `listconstvars` vale `true` entonces
`listofvars` incluirá `%e`, `%pi`, `%i`
y cualquier otra variable declarada constante de las que aparezcan
en *expr*.  Estas constantes se omiten por defecto.


Véase también la variable opcional `listdummyvars` para
excluir o incluir variables ficticias en la lista de variables.


Ejemplo:



```maxima
(%i1) listofvars (f (x[1]+y) / g^(2+a));
(%o1)                     [g, a, x , y]
                                  1
```

<!-- category: Other -->
<!-- keywords: lpart -->
<!-- signatures: lpart(label, expr, n_1, ..., n_k) -->
### Function: lpart (label, expr, n_1, ..., n_k)

Similar a `dpart` pero utiliza una caja etiquetada. Una caja etiquetada es similar a la que produce `dpart`, pero con un nombre en la línea superior.

<!-- category: Other -->
<!-- keywords: mainvar -->
<!-- signatures: mainvar -->
### Variable: mainvar

Se pueden declarar variables de tipo `mainvar`.  El orden de los átomos 
es: números < constantes (como `%e` o `%pi`) <
escalares < otras variables < "mainvars".  Por ejemplo, compárese `expand ((X+Y)^4)`
con `(declare (x, mainvar), expand ((x+y)^4))`.  (Nota: Se debe tener cuidado si se quiere hacer uso de esta declaración. Por ejemplo, si se resta una expresión en la que `x` ha sido declarada como `mainvar` de otra en la que `x` no es `mainvar`, puede ser necesario volver a simplificar, `ev (expr, simp)`, a fin de obtener cancelaciones.  Además, si se guarda una expresión en la que `x` es `mainvar`, quizás sea necesario guardar también `x`.)

<!-- category: Other -->
<!-- keywords: noun -->
<!-- signatures: noun -->
### Variable: noun

El símbolo `noun` es una de las opciones de la instrucción `declare`. Hace que una función se declare como "nombre", lo que significa que no se evaluará automáticamente.

<!-- category: Other -->
<!-- keywords: noundisp -->
<!-- signatures: noundisp -->
### Variable: noundisp

Valor por defecto: `false`


Si `noundisp` vale `true`, los nombres se muestran precedidos de un apóstrofo. Siempre debe valer `true` cuando se quiera representar la definición de funciones.

<!-- category: Other -->
<!-- keywords: nounify -->
<!-- signatures: nounify(f) -->
### Function: nounify (f)

Devuelve la forma nominal de la función cuyo nombre es *f*.  Puede ser útil cuando se quiera hacer referencia al nombre de una función sin que ésta se ejecute.  Nótese que algunas funciones verbales devolverán su forma nominal si no pueden ser evaluadas para ciertos argumentos.  Esta es también la expresión que se obtiene cuando la llamada a una función va precedida por del apóstrofo.

<!-- category: Other -->
<!-- keywords: nterms -->
<!-- signatures: nterms(expr) -->
### Function: nterms (expr)

Devuelve el número de términos que  *expr* llegaría a tener si fuese completamente expandida y no hubiesen cancelaciones ni combinaciones de términos semejantes.
Nótese que expresiones como `sin (expr)`, `sqrt (expr)`, `exp (expr)`, etc.
cuentan como un sólo término, independientemente de cuántos términos tenga a su vez *expr* en caso de tratarse de una suma.

<!-- category: Other -->
<!-- keywords: op -->
<!-- signatures: op(expr) -->
### Function: op (expr)

Devuelve el operador principal de la expresión *expr*. La llamada
`op (expr)` equivale a `part (expr, 0)`. 


La función `op` devuelve una cadena si el operador principal es un operador prefijo, infijo (binario o `n`-ario), postfijo, "bi-fijo" o "no-fijo" ("bi-fijo"  se refiere a un par de símbolos que encierran su o sus argumentos, y "no-fijo" es un operador que no necesita argumentos).
Si *expr* es la expresión de una función
subindicada, `op` devuelve la función subindicada;
en cuyo caso el valor devuelto no es un átomo.
En otro caso, *expr* es la expresión de una función array u
ordinaria, y entonces `op` devuelve un símbolo.


La función `op` observa el valor de la variable global `inflag`.


La función `op` evalúa sus argumentos.


Véase también `args`.


Ejemplos:



















```maxima
(%i1) stringdisp: true$
(%i2) op (a * b * c);
(%o2)                          "*"
(%i3) op (a * b + c);
(%o3)                          "+"
(%i4) op ('sin (a + b));
(%o4)                          sin
(%i5) op (a!);
(%o5)                          "!"
(%i6) op (-a);
(%o6)                          "-"
(%i7) op ([a, b, c]);
(%o7)                          "["
(%i8) op ('(if a > b then c else d));
(%o8)                         "if"
(%i9) op ('foo (a));
(%o9)                          foo
(%i10) prefix (foo);
(%o10)                        "foo"
(%i11) op (foo a);
(%o11)                        "foo"
(%i12) op (F [x, y] (a, b, c));
(%o12)                        F
                               x, y
(%i13) op (G [u, v, w]);
(%o13)                          G
```

<!-- category: Other -->
<!-- keywords: operatorp -->
<!-- signatures: operatorp(expr, op), operatorp(expr, [op_1, ..., op_n]) -->
### Function: operatorp (expr, op)

La llamada `operatorp (expr, op)` devuelve `true`
si *op* es igual al operador de *expr*.


La llamada `operatorp (expr, [op_1, ..., op_n])` devuelve `true`
si algún elemento  *op_1*, ..., *op_n* es igual al operador de *expr*.

<!-- category: Other -->
<!-- keywords: opsubst -->
<!-- signatures: opsubst -->
### Variable: opsubst

Valor por defecto: `true`


Si `opsubst` vale `false`, `subst` no sustituye el operdor de una expresión, de manera que `(opsubst: false, subst (x^2, r, r+r[0]))` trabajará correctamente.

<!-- category: Other -->
<!-- keywords: optimize -->
<!-- signatures: optimize(expr) -->
### Function: optimize (expr)

Devuelve una expresión que produce el mismo valor y efectos secundarios que *expr*, pero de forma más eficiente al evitar recalcular subexpresiones comunes. La función `optimize` también tiene el efecto secundario de colapsar su argumento de manera que se compartan todas sus subexpresiones comunes.
Hágase `example (optimize)` para ver ejemplos.

<!-- category: Other -->
<!-- keywords: optimprefix -->
<!-- signatures: optimprefix -->
### Variable: optimprefix

Valor por defecto: `%`


La variable `optimprefix` es el prefijo utilizado para los símbolos generados por la instrucción `optimize`.

<!-- category: Other -->
<!-- keywords: ordergreat, orderless -->
<!-- signatures: ordergreat(v_1, ..., v_n), orderless(v_1, ..., v_n) -->
### Function: ordergreat (v_1, ..., v_n)

`ordergreat` cambia el orden canónico de las expresiones de
Maxima, de manera que *v_1* prevalece sobre *v_2*, que
prevalece sobre ..., que prevalece sobre *v_n*, que prevalece
sobre cualquier otro símbolo no presente en la
lista de argumentos.


`orderless` cambia el orden canónico de las expresiones de
Maxima, de manera que *v_1* precede a *v_2*, que precede a ...,
que precede a *v_n*, que precede a cualquier otra variable no 
presente en la lista de argumentos.


El orden impuesto por `ordergreat` y `orderless` se 
destruye con `unorder`. `ordergreat` y `orderless`
sólo se pueden llamar una vez, a menos que se invoque a `unorder`.
La última llamada a `ordergreat` y `orderless` es la que
se mantiene activa.


Véase también `ordergreatp`.

<!-- category: Other -->
<!-- keywords: ordergreatp, orderlessp -->
<!-- signatures: ordergreatp(expr_1, expr_2), orderlessp(expr_1, expr_2) -->
### Function: ordergreatp (expr_1, expr_2)

`ordergreatp` devuelve `true` si *expr_1* prevalece sobre
*expr_2* en el orden canónico de las expresiones de Maxima, o
`false` en caso contrario.


`orderlessp` devuelve `true` si *expr_1* precede a
*expr_2* en el orden canónico de las expresiones de Maxima, o
`false` en caso contrario.


Todos los átomos y expresiones de Maxima son comparables bajo 
`ordergreatp` y `orderlessp`, aunque existen ejemplos aislados
de expresiones para los que estos predicados no son transitivos.


La ordenación canónica de átomos (símbolos, números
literales y cadenas) es la siguiente: (enteros y decimales en coma flotante)
preceden a (números decimales grandes o *bigfloats*), que preceden a (constantes
declaradas), que preceden a (cadenas), que preceden a (escalares declarados), que preceden a 
(primer argumento de `orderless`), que precede a ..., que precede a (último
argumento de `orderless`), que precede a (otros símbolos), que
preceden a (último argumento de `ordergreat`), que precede a ..., que
precede a (primer argumento de `ordergreat`), que precede a (variables
principales declaradas).


Para las expresiones no atómicas, la ordenación canónica se deriva de la
ordenación de átomos. Para los operadores nativos `+`, `*` y `^`,
los criterios de ordenación no son sencillos de resumir.
Para otros operadores nativos, y todas las demás funciones y operadores,
las expresiones se ordenan por sus argumentos (empezando por el primero),
después por el nombre del operador o función. En caso de expresiones
con subíndices, el símbolo subindicado se
considera operador y el subíndice un argumento del mismo.


El orden canónico de expresiones se modifica mediante las funciones
`ordergreat` y `orderless`, así como por las 
declaraciones `mainvar`, `constant` y `scalar`.


Véase también `sort`.


Ejemplos:


Ordenación de símbolos comunes y constantes.
Nótese que `%pi` no se ordena en función de su valor
numérico.







```maxima
(%i1) stringdisp : true;
(%o1)                         true
(%i2) sort ([%pi, 3b0, 3.0, x, X, "foo", 3, a, 4, "bar", 4.0, 4b0]);
(%o2) [3, 3.0, 4, 4.0, 3.0b0, 4.0b0, %pi, "bar", "foo", a, x, X]
```


Efecto producido por las funciones `ordergreat` y `orderless`.









```maxima
(%i1) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o1)           [A, E, G, H, J, K, M, P, S, T, W]
(%i2) ordergreat (S, J);
(%o2)                         done
(%i3) orderless (M, H);
(%o3)                         done
(%i4) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o4)           [M, H, A, E, G, K, P, T, W, J, S]
```


Efecto producido por las declaraciones `mainvar`, `constant` y `scalar`.










```maxima
(%i1) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o1)   [aa, bar, baz, bb, cc, dd, foo, quux, A1, B1, C1]
(%i2) declare (aa, mainvar);
(%o2)                         done
(%i3) declare ([baz, quux], constant);
(%o3)                         done
(%i4) declare ([A1, B1], scalar);
(%o4)                         done
(%i5) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o5)   [baz, quux, A1, B1, bar, bb, cc, dd, foo, C1, aa]
```


Ordenación de expresiones no atómicas.







```maxima
(%i1) sort ([1, 2, n, f(1), f(2), f(2, 1), g(1), g(1, 2), g(n), f(n, 1)]);
(%o1) [1, 2, f(1), g(1), g(1, 2), f(2), f(2, 1), n, g(n), 
                                                         f(n, 1)]
(%i2) sort ([foo(1), X[1], X[k], foo(k), 1, k]);
(%o2)            [1, foo(1), X , k, foo(k), X ]
                              1              k
```

<!-- category: Other -->
<!-- keywords: part -->
<!-- signatures: part(expr, n_1, ..., n_k) -->
### Function: part (expr, n_1, ..., n_k)

Devuelve partes de la forma mostrada de `expr`. Obtiene la 
parte de `expr` que se especifica por los índices 
*n_1*, ..., *n_k*.  Primero se obtiene la parte *n_1* de 
`expr`, después la parte *n_2* del resultado anterior, 
y así sucesivamente.  El resultado que se obtiene es 
la parte *n_k* de ... la parte *n_2* de la parte *n_1* de `expr`.
Si no se especifican índices, devuelve `expr`.


La función `part` se puede utilizar para obtener un elemento 
de una lista, una fila de una matriz, etc.




Si el último argumento de la función `part` es una lista de 
índices, entonces se toman varias subexpresiones, cada 
una de las cuales correspondiente a un índice de la lista.
Así, `part (x + y + z, [1, 3])` devuelve `z+x`.


La variable `piece` guarda la última expresión seleccionada
con la función `part`. Se actualiza durante la ejecución de
la función, por lo que puede ser referenciada en la misma función.


Si `partswitch` vale `true` entonces de devuelve `end`
cuando no exista la parte seleccionada de una expresión, si vale
`false` se mostrará un mensaje de error.


Véanse también `inpart`, `substpart`, `substinpart`,
`dpart` y `lpart`.


Ejemplos:








```maxima
(%i1) part(z+2*y+a,2);
(%o1)                                 2 y
(%i2) part(z+2*y+a,[1,3]);
(%o2)                                z + a
(%i3) part(z+2*y+a,2,1);
(%o3)                                  2
```


La instrucción `example (part)` muestra más ejemplos.

<!-- category: Other -->
<!-- keywords: partition -->
<!-- signatures: partition(expr, x) -->
### Function: partition (expr, x)

Devuelve una lista con dos expresiones, que son: (1) los factores de 
*expr* si es un producto, los términos de *expr* si es una
suma, o los elementos de *expr*, si es una lista, que no contengan
a *x*, (2) los factores, términos o lista que contengan a *x*.



```maxima
(%i1) partition (2*a*x*f(x), x);
(%o1)                     [2 a, x f(x)]
(%i2) partition (a+b, x);
(%o2)                      [b + a, 0]
(%i3) partition ([a, b, f(a), c], a); 
(%o3)                  [[b, c], [a, f(a)]]
```

<!-- category: Other -->
<!-- keywords: partswitch -->
<!-- signatures: partswitch -->
### Variable: partswitch

Valor por defecto: `false`


Si `partswitch` vale `true` entonces de devuelve `end` cuando no exista la parte seleccionada de una expresión, si vale `false` se mostrará un mensaje de error.

<!-- category: Other -->
<!-- keywords: pickapart -->
<!-- signatures: pickapart(expr, n) -->
### Function: pickapart (expr, n)

Asigna etiquetas de expresiones intermedias a subexpresiones de *expr* al nivel de profundidad *n*, que es un entero. A las subexpresiones a un nivel de profundidad mayor o menor no se les asignan etiquetas. La función
`pickapart` devuelve una expresión en términos de expresiones intermedias equivalente a la expresión original *expr*.


Véanse también `part`, `dpart`, `lpart`, `inpart` y `reveal`.


Ejemplos:



```maxima
(%i1) expr: (a+b)/2 + sin (x^2)/3 - log (1 + sqrt(x+1));
                                          2
                                     sin(x )   b + a
(%o1)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2
(%i2) pickapart (expr, 0);

                                          2
                                     sin(x )   b + a
(%t2)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2

(%o2)                          %t2
(%i3) pickapart (expr, 1);

(%t3)                - log(sqrt(x + 1) + 1)


                                  2
                             sin(x )
(%t4)                        -------
                                3


                              b + a
(%t5)                         -----
                                2

(%o5)                    %t5 + %t4 + %t3
(%i5) pickapart (expr, 2);

(%t6)                 log(sqrt(x + 1) + 1)


                                  2
(%t7)                        sin(x )


(%t8)                         b + a

                         %t8   %t7
(%o8)                    --- + --- - %t6
                          2     3
(%i8) pickapart (expr, 3);

(%t9)                    sqrt(x + 1) + 1


                                2
(%t10)                         x

                  b + a              sin(%t10)
(%o10)            ----- - log(%t9) + ---------
                    2                    3
(%i10) pickapart (expr, 4);

(%t11)                     sqrt(x + 1)

                      2
                 sin(x )   b + a
(%o11)           ------- + ----- - log(%t11 + 1)
                    3        2
(%i11) pickapart (expr, 5);

(%t12)                        x + 1

                   2
              sin(x )   b + a
(%o12)        ------- + ----- - log(sqrt(%t12) + 1)
                 3        2
(%i12) pickapart (expr, 6);
                  2
             sin(x )   b + a
(%o12)       ------- + ----- - log(sqrt(x + 1) + 1)
                3        2
```

<!-- category: Other -->
<!-- keywords: piece -->
<!-- signatures: piece -->
### Variable: piece

Guarda la última expresión seleccionada por las funciones `part`.

<!-- category: Other -->
<!-- keywords: psubst -->
<!-- signatures: psubst(list, expr), psubst(a, b, expr) -->
### Function: psubst (list, expr)

`psubst(a, b, expr)` es simliar a `subst`.  Véase 
`subst`.


A diferencia de `subst`, la función `psubst` hace sustituciones
en paralelo si su primer argumento es una lista de ecuaciones.


Véase también `sublis` para hacer sustituciones en paralelo.


Ejemplo:


El primer ejemplo muestra la sustitución en paralelo con `psubst`.
El segundo ejemplo muestra el resultado de la función `subst`,
que realiza la sustitución en serie.







```maxima
(%i4) psubst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o4)                           sin(b) + sin(a)
(%i5) subst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o5)                              2 sin(a)
```

<!-- category: Other -->
<!-- keywords: rembox -->
<!-- signatures: rembox(expr, unlabelled), rembox(expr, label), rembox(expr) -->
### Function: rembox (expr, unlabelled)

Elimina cajas de *expr*.


La llamada `rembox (expr, unlabelled)` elimina todas las cajas no etiquetadas de *expr*.


La llamada `rembox (expr, label)` sólo elimina las cajas etiquetadas con *label*.


La llamada `rembox (expr)` elimina todas las caajs, independientemente de que estén etiquetadas o no.


Las cajas son dibujadas por las funciones `box`, `dpart` y `lpart`.


Ejemplos:












```maxima
(%i1) expr: (a*d - b*c)/h^2 + sin(%pi*x);
                                  a d - b c
(%o1)                sin(%pi x) + ---------
                                      2
                                     h
(%i2) dpart (dpart (expr, 1, 1), 2, 2);
                        """""""    a d - b c
(%o2)               sin("%pi x") + ---------
                        """""""      """"
                                     " 2"
                                     "h "
                                     """"
(%i3) expr2: lpart (BAR, lpart (FOO, %, 1), 2);
                  FOO"""""""""""   BAR""""""""
                  "    """"""" "   "a d - b c"
(%o3)             "sin("%pi x")" + "---------"
                  "    """"""" "   "  """"   "
                  """"""""""""""   "  " 2"   "
                                   "  "h "   "
                                   "  """"   "
                                   """""""""""
(%i4) rembox (expr2, unlabelled);
                                  BAR""""""""
                   FOO"""""""""   "a d - b c"
(%o4)              "sin(%pi x)" + "---------"
                   """"""""""""   "    2    "
                                  "   h     "
                                  """""""""""
(%i5) rembox (expr2, FOO);
                                  BAR""""""""
                       """""""    "a d - b c"
(%o5)              sin("%pi x") + "---------"
                       """""""    "  """"   "
                                  "  " 2"   "
                                  "  "h "   "
                                  "  """"   "
                                  """""""""""
(%i6) rembox (expr2, BAR);
                   FOO"""""""""""
                   "    """"""" "   a d - b c
(%o6)              "sin("%pi x")" + ---------
                   "    """"""" "     """"
                   """"""""""""""     " 2"
                                      "h "
                                      """"
(%i7) rembox (expr2);
                                  a d - b c
(%o7)                sin(%pi x) + ---------
                                      2
                                     h
```

<!-- category: Other -->
<!-- keywords: reveal -->
<!-- signatures: reveal(expr, nivel) -->
### Function: reveal (expr, nivel)

Reemplaza partes de *expr* al *nivel* especificado y las sutituye por descripciones cortas.



- *
Las sumas y restas se reemplazan por `Sum(n)`,
siendo *n* el número de términos de la suma.
- *
Los productos se reemplazan por `Product(n)`,
siendo *n* el número de factores del producto.
- *
Las potencias se reemplazan por `Expt`.
- *
Los cocientes se reemplazan por `Quotient`.
- *
El símbolo negativo se reemplaza por `Negterm`.
- *
Las listas se reemplazan por `List(n)`, siendo *n* el número de
elementos de la lista.


Si el entero  *depth* es mayor o igual que la profundidad máxima de *expr*,
`reveal (expr, depth)` devuelve *expr* sin modificar.


La función `reveal` evalúa sus argumentos y devuelve la expresión con las modificaciones solicitadas.


Ejemplo:












```maxima
(%i1) e: expand ((a - b)^2)/expand ((exp(a) + exp(b))^2);
                          2            2
                         b  - 2 a b + a
(%o1)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
(%i2) reveal (e, 1);
(%o2)                       Quotient
(%i3) reveal (e, 2);
                             Sum(3)
(%o3)                        ------
                             Sum(3)
(%i4) reveal (e, 3);
                     Expt + Negterm + Expt
(%o4)               ------------------------
                    Product(2) + Expt + Expt
(%i5) reveal (e, 4);
                       2                 2
                      b  - Product(3) + a
(%o5)         ------------------------------------
                         Product(2)     Product(2)
              2 Expt + %e           + %e
(%i6) reveal (e, 5);
                         2            2
                        b  - 2 a b + a
(%o6)              --------------------------
                       Sum(2)     2 b     2 a
                   2 %e       + %e    + %e
(%i7) reveal (e, 6);
                          2            2
                         b  - 2 a b + a
(%o7)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
```

<!-- category: Other -->
<!-- keywords: sublis -->
<!-- signatures: sublis(list, expr) -->
### Function: sublis (list, expr)

Hace sustituciones múltiples en paralelo dentro de las expresiones.
*list* es una lista de ecuaciones, cuyos miembros izquierdos deben
ser átomos.


La variable `sublis_apply_lambda` controla la simplificación
después de `sublis`.


Véase también `psubst` para hacer sustituciones en paralelo.


Ejemplo:






```maxima
(%i1) sublis ([a=b, b=a], sin(a) + cos(b));
(%o1)                    sin(b) + cos(a)
```

<!-- category: Other -->
<!-- keywords: sublis_apply_lambda -->
<!-- signatures: sublis_apply_lambda -->
### Variable: sublis_apply_lambda

Valor por defecto: `true`


Controla si los `lambda` sustituidos son aplicados en la simplificación después de invocar a `sublis`, o si se tiene que hacer un `ev` para hacerlo. Si `sublis_apply_lambda` vale `true`, significa que se ejecute la aplicación.

<!-- category: Other -->
<!-- keywords: subnumsimp -->
<!-- signatures: subnumsimp -->
### Variable: subnumsimp

Valor por defecto: `false`


Si vale `true`, las funciones `subst` y `psubst` puede sustituir
una variable subindicada `f[x]` por un número simplemente utilizando el
símbolo `f`.


Véase también `subst`.



```maxima
(%i1) subst(100,g,g[x]+2);

subst: cannot substitute 100 for operator g in expression g
                                                           x
 -- an error. To debug this try: debugmode(true);

(%i2) subst(100,g,g[x]+2),subnumsimp:true;
(%o2)                          102
```

<!-- category: Other -->
<!-- keywords: subst -->
<!-- signatures: subst(a, b, c) -->
### Function: subst (a, b, c)

Sustituye *a* por *b* en *c*. El argumento  *b* debe ser un átomo o una subexpresión completa de *c*.  Por ejemplo, `x+y+z` es una subexpresión completa de  `2*(x+y+z)/w` mientras que `x+y` no lo es. Cuando *b* no cumple esta característica, se puede utilizar en algunos casos `substpart` o `ratsubst`
(ver más abajo).  Alternativamente, si *b* no es de la forma `e/f` entonces se puede usar `subst (a*f, e, c)`, pero si *b* es de la forma `e^(1/f)` se debe usar `subst (a^f, e, c)`.  La instrucción `subst` también reconoce `x^y` en `x^-y`, de manera que  `subst (a, sqrt(x), 1/sqrt(x))` da `1/a`. Los argumentos *a* y *b* también pueden ser operadores de una expresión acotados por comillas dobles `"` o nombres de funciones.  Si se quiere sustituir la variable independiente en expresiones con derivadas se debe utilizar la función `at` (ver más abajo).


La función `subst` es sinónimo de `substitute`.


La llamada `subst (eq_1, expr)` o 
`subst ([eq_1, ..., eq_k], expr)`
están permitidas. Las *eq_i* son ecuaciones que indican las sustituciones a realizar.
Para cada ecuación, el miembro izquierdo será sustituido por la expresión del 
miembro derecho en *expr*. Las ecuaciones se sustituyen secuencialmente de
izquierda a derecha en *expr*. Véanse las funciones `sublis` y `psubst` 
para sustituciones en paralelo.


Si la variable `exptsubst` vale `true` se permiten ciertas
sustituciones de exponentes; por ejemplo, sustituir `y` por `%e^x`
en `%e^(a*x)`.


Si `opsubst` vale `false`,
`subst` no intentará sustituir un operador de una expresión. Por ejemplo, 
`(opsubst: false, subst (x^2, r, r+r[0]))` trabajará sin problemas.


Ejemplos:







```maxima
(%i1) subst (a, x+y, x + (x+y)^2 + y);
                                    2
(%o1)                      y + x + a
(%i2) subst (-%i, %i, a + b*%i);
(%o2)                       a - %i b
```


La sustitución se hace secuencialmente según una lista de
ecuaciones. Compárese con la sustitución en paralelo.







```maxima
(%i3) subst([a=b, b=c], a+b);
(%o3)                                 2 c
(%i4) sublis([a=b, b=c], a+b);
(%o4)                                c + b
```



Para más ejemplos, ejecútese `example (subst)`.

<!-- category: Other -->
<!-- keywords: substinpart -->
<!-- signatures: substinpart(x, expr, n_1, ..., n_k) -->
### Function: substinpart (x, expr, n_1, ..., n_k)

Es similar a `substinpart`, pero trabaja con la representación interna de *expr*.


Ejemplos:








```maxima
(%i1) x . 'diff (f(x), x, 2);
                              2
                             d
(%o1)                   x . (--- (f(x)))
                               2
                             dx
(%i2) substinpart (d^2, %, 2);
                                  2
(%o2)                        x . d
(%i3) substinpart (f1, f[1](x + 1), 0);
(%o3)                       f1(x + 1)
```


Si el último argumento pasado a la función `part` es una
lista de índices, se obtendrá la lista de subexpresiones
correspondientes a cada uno de los índices.






```maxima
(%i1) part (x + y + z, [1, 3]);
(%o1)                         z + x
```


La variable `piece` guarda el valor de la última expresión seleccionada al
utilizar las funciones `part`. El valor es asignado durante la 
ejecución de la función y puede ser utilizada tal como se muestra más
abajo. Si a `partswitch` se le asigna el valor `true` entonces se
devolverá `end` cuando no existe la parte solicitada; con otro
valor devuelve un mensaje de error.











```maxima
(%i1) expr: 27*y^3 + 54*x*y^2 + 36*x^2*y + y + 8*x^3 + x + 1;
              3         2       2            3
(%o1)     27 y  + 54 x y  + 36 x  y + y + 8 x  + x + 1
(%i2) part (expr, 2, [1, 3]);
                                  2
(%o2)                         54 y
(%i3) sqrt (piece/54);
(%o3)                        abs(y)
(%i4) substpart (factor (piece), expr, [1, 2, 3, 5]);
                               3
(%o4)               (3 y + 2 x)  + y + x + 1
(%i5) expr: 1/x + y/x - 1/z;
                             1   y   1
(%o5)                      - - + - + -
                             z   x   x
(%i6) substpart (xthru (piece), expr, [2, 3]);
                            y + 1   1
(%o6)                       ----- - -
                              x     z
```


Además, dándole a `inflag` el valor `true` y llamando a
`part` o `substpart` es lo mismo que invocar a  `inpart` o `substinpart`.

<!-- category: Other -->
<!-- keywords: substpart -->
<!-- signatures: substpart(x, expr, n_1, ..., n_k) -->
### Function: substpart (x, expr, n_1, ..., n_k)

Sustituye por *x* la subexpresión que se obtiene de aplicar el resto de
argumentos a la función `part`, devolviendo el nuevo valor de *expr*.
*x* puede ser un operador que sustituya otro operador de *expr*. En
ciertos casos, *x* necesita estar entrecomillado por comillas dobles (`"`);
por ejemplo, de `substpart ("+", a*b, 0)` se obtiene `b + a`.


Ejemplo:









```maxima
(%i1) 1/(x^2 + 2);
                               1
(%o1)                        ------
                              2
                             x  + 2
(%i2) substpart (3/2, %, 2, 1, 2);
                               1
(%o2)                       --------
                             3/2
                            x    + 2
(%i3) a*x + f(b, y);
(%o3)                     a x + f(b, y)
(%i4) substpart ("+", %, 1, 0);
(%o4)                    x + f(b, y) + a
```


Además, dándole a `inflag` el valor `true` y llamando a
`part` o `substpart` es lo mismo que invocar a  `inpart` o `substinpart`.

<!-- category: Other -->
<!-- keywords: symbolp -->
<!-- signatures: symbolp(expr) -->
### Function: symbolp (expr)

Devuelve `true` si *expr* es un símbolo y `false` en caso contrario.
La llamada `symbolp(x)` equivale al predicado `atom(x) and not numberp(x)`.


Véase también `Identifiers`.

<!-- category: Other -->
<!-- keywords: unorder -->
<!-- signatures: unorder() -->
### Function: unorder ()

Desactiva las asociaciones creadas por la última utilización de los comandos de ordenación `ordergreat` y `orderless`, los cuales no pueden ser utilizados más de una vez sin invocar a `unorder`. 


`unorder` no sustituye en expresiones los símbolos originales
por los alias introducidos por `ordergreat` y `orderless`. Es por ello
que tras la ejecuciÃ³n de `unorder` los alias aparecen en expresiones
anteriores.


Véase también `ordergreat` y `orderless`.


Ejemplos:


`ordergreat(a)` introduce un alias para el símbolo `a`,
razón por la cual la diferencia de `%o2` y `%o4` no se anula.
`unorder` no restablece el símbolo `a` y el alias
aparece en el resultado `%o7`.












```maxima
(%i1) 
(%o1)                          []
(%i2) b*x+a^2;
                                   2
(%o2)                       b x + a
(%i3) ordergreat(a);
(%o3)                         done
(%i4) b*x+a^2;
                             2
(%o4)                       a  + b x
(%i5) %th(1)-%th(3);
                              2    2
(%o5)                        a  - a
(%i6) unorder();
(%o6)                          [a]
(%i7) %th(2);
                                2    2
(%o7)                      _101a  - a
```

<!-- category: Other -->
<!-- keywords: verbify -->
<!-- signatures: verbify(f) -->
### Function: verbify (f)

Devuelve la forma verbal del nombre de función *f*.


Véanse también `verb`, `noun` y `nounify`.


Ejemplos:









```maxima
(%i1) verbify ('foo);
(%o1)                          foo
(%i2) :lisp $%
$FOO
(%i2) nounify (foo);
(%o2)                          foo
(%i3) :lisp $%
%FOO
```

