## Línea de comandos

<!-- category: Other -->
<!-- keywords: % -->
<!-- signatures: % -->
### Variable: %

El símbolo `%` representa la expresión de salida (esto es, `%o1`, `%o2`, `%o3`, ...)
más reciente calculada por Maxima, independientemente de que la haya mostrado o no.


La variable `%` es reconocida por  `batch` y por `load`.
Cuando un fichero es procesado por `batch`, la variable `%`
tiene el mismo significado que en el modo interactivo.
Cuando un fichero es procesado por `load`, a la variable `%`
se le asigna la última expresión introducida, bien desde el modo
interactivo, bien en un fichero por lotes; en ningún caso se le asigna 
a `%` una expresión de entrada del fichero que está siendo procesado.


Véanse también `_`, `%%` y `%th`.

<!-- category: Other -->
<!-- keywords: %% -->
<!-- signatures: %% -->
### Variable: %%

En una sentencia compuesta, como `block`, `lambda` o 
`(s_1, ..., s_n)`, `%%` es el valor de la sentencia previa.


La variable `%%` no estÃ¡ definida cuando se utiliza en la primera sentencia,
o fuera de una sentencia compuesta.


`%%` se puede utilizar con `batch` y `load`, manteniendo en ambos
casos el mismo significado que en el modo interactivo.


Véase también `%`


Ejemplos:


Los siguientes dos ejemplos devuelven el mismo resultado.



```maxima
(%i1) block (integrate (x^5, x), ev (%%, x=2) - ev (%%, x=1));
                               21
(%o1)                          --
                               2
(%i2) block ([prev], prev: integrate (x^5, x),
               ev (prev, x=2) - ev (prev, x=1));
                               21
(%o2)                          --
                               2
```


Una sentencia compuesta puede contener otras sentencias compuestas.
Independientemente de que una sentencia sea simple o compuesta, `%%` es 
el valor de la sentencia previa.



```maxima
(%i3) block (block (a^n, %%*42), %%/6);
                                 n
(%o3)                         7 a
```


Dentro de una sentencia compuesta, el valor de `%%` puede inspeccionarse
en un punto de interrupción que se abra ejecutando la función `break`.
Por ejemplo, escribiendo `%%;` en el siguiente ejemplo se obtiene `42`.



```maxima
(%i4) block (a: 42, break ())$

Entering a Maxima break point. Type 'exit;' to resume.
_%%;
42
_
```

<!-- category: Other -->
<!-- keywords: %edispflag -->
<!-- signatures: %edispflag -->
### Variable: %edispflag

Valor por defecto: `false`


Si `%edispflag` vale `true`, Maxima muestra `%e` elevado
a un exponente negativo como un cociente. Por ejemplo, `%e^-x` se
muestra como `1/%e^x`. Véase también `exptdispflag`.


Ejemplo:








```maxima
(%i1) %e^-10;
                               - 10
(%o1)                        %e
(%i2) %edispflag:true$
(%i3) %e^-10;
                               1
(%o3)                         ----
                                10
                              %e
```

<!-- category: Other -->
<!-- keywords: %th -->
<!-- signatures: %th(i) -->
### Function: %th (i)

Es el valor de la expresión de la *i*-ésima salida anterior.
Esto es, si la siguiente expresión a calcular es la salida *n*-ésima,
`%th (m)` es la salida  (*n* - *m*)-ésima.


`%th` es reconocido por `batch` y `load`, interpretándose
de la misma manera que se acaba de indicar. Cuando un fichero es procesado
por `load`, `%th` se refiere a los cálculos más recientes;
`%th` no hace referencia a las expresiones de salida incluidas en el
propio fichero que se está procesando.


Véanse también `%` y `%%`


Ejemplo:


`%th` es útil en ficheros `batch` para hacer referencia a grupos de resultados
recién obtenidos.  En este ejemplo se asigna a `s` la suma de los cinco resultados.



```maxima
(%i1) 1;2;3;4;5;
(%o1)                           1
(%o2)                           2
(%o3)                           3
(%o4)                           4
(%o5)                           5
(%i6) block (s: 0, for i:1 thru 5 do s: s + %th(i), s);
(%o6)                          15
```

<!-- category: Other -->
<!-- keywords: ? -->
<!-- signatures: ? -->
### Function: ?

Como prefijo de una función o nombre de variable, `?` significa que el nombre es de Lisp, no de Maxima.
Por ejemplo, `?round` representa la función de Lisp `ROUND`.
Véase `Lisp y Maxima` para más información.


La notación `? word` (un símbolo de interrogación
seguido de una palabra y separados por un espacio)
equivale a `describe ("word")`.
El símbolo de interrogación debe escribirse al
comienzo de la línea de entrada; en caso contrario
no se reconoce como una solicitud de documentación.

<!-- category: Other -->
<!-- keywords: ?? -->
<!-- signatures: ?? -->
### Function: ??

La notación `?? palabra` (`??` seguido de un espacio
y una palabra) equivale a `describe("palabra", inexact)`.
El símbolo de interrogación debe escribirse al
comienzo de la línea de entrada; en caso contrario
no se reconoce como una solicitud de documentación.

<!-- category: Other -->
<!-- keywords: _ -->
<!-- signatures: _ -->
### Variable: _

El símbolo `_` representa la última expresión de entrada (esto es, `%i1`, `%i2`, `%i3`, ...).


Al símbolo `_` se le asigna la expresión de entrada antes de que ésta sea simplificada o evaluada. Sin embargo, el valor de `_` se simplifica (pero no se evalúa) cuando se muestra en el terminal.


La variable `_` es reconocida por  `batch` y por `load`.
Cuando un fichero es procesado por `batch`, la variable `_`
tiene el mismo significado que en el modo interactivo.
Cuando un fichero es procesado por `load`, a la variable `_`
se le asigna la última expresión introducida, bien desde el modo
interactivo, bien en un fichero por lotes; en ningún caso se le asigna 
a `_` una expresión de entrada del fichero que está siendo procesado.


Véanse también `__` y `%`.


Ejemplos:


















```maxima
(%i1) 13 + 29;
(%o1)                          42
(%i2) :lisp $_
((MPLUS) 13 29)
(%i2) _;
(%o2)                          42
(%i3) sin (%pi/2);
(%o3)                           1
(%i4) :lisp $_
((%SIN) ((MQUOTIENT) $%PI 2))
(%i4) _;
(%o4)                           1
(%i5) a: 13$
(%i6) b: 29$
(%i7) a + b;
(%o7)                          42
(%i8) :lisp $_
((MPLUS) $A $B)
(%i8) _;
(%o8)                         b + a
(%i9) a + b;
(%o9)                          42
(%i10) ev (_);
(%o10)                         42
```

<!-- category: Other -->
<!-- keywords: __ -->
<!-- signatures: __ -->
### Variable: __

`__` es la expresión de entrada que está siendo actualmente evaluada.
Esto es, mientras se está evaluando una expresión de entrada, 
`__` es igual a *expr*.


A `__` se le asigna la expresión de entrada antes de que ésta sea 
simplificada o evaluada. Sin embargo, el valor de `__` es simplificado,
pero no evaluado, cuando su valor es mostrado en el terminal.


La variable `__` es reconocida por  `batch` y por `load`.
Cuando un fichero es procesado por `batch`, la variable `__`
tiene el mismo significado que en el modo interactivo.
Cuando un fichero es procesado por `load`, a la variable `__`
se le asigna la última expresión introducida, bien desde el modo
interactivo, bien en un fichero por lotes; en ningún caso se le asigna 
a `__` una expresión de entrada del fichero que está siendo procesado.
En particular, si `load (filename)` es ejecutado desde el modo
interactivo, entonces `__` almacena la expresión `load (filename)`
mientras el fichero está siendo procesado.


Véanse también `_` y `%`.


Ejemplos:










```maxima
(%i1) print ("I was called as", __);
I was called as print(I was called as, __) 
(%o1)              print(I was called as, __)
(%i2) foo (__);
(%o2)                     foo(foo(__))
(%i3) g (x) := (print ("Current input expression =", __), 0);
(%o3) g(x) := (print("Current input expression =", __), 0)
(%i4) [aa : 1, bb : 2, cc : 3];
(%o4)                       [1, 2, 3]
(%i5) (aa + bb + cc)/(dd + ee + g(x));
                            cc + bb + aa
Current input expression = -------------- 
                           g(x) + ee + dd
                                6
(%o5)                        -------
                             ee + dd
```

<!-- category: Other -->
<!-- keywords: absboxchar -->
<!-- signatures: absboxchar -->
### Variable: absboxchar

Valor por defecto: `!`


La variable `absboxchar` es el carácter utilizado para representar el valor absoluto de una expresión que ocupa más de una línea de altura.


Ejemplo:



```maxima
(%i1) abs((x^3+1));
                            ! 3    !
(%o1)                       !x  + 1!
```

<!-- category: Other -->
<!-- keywords: disp -->
<!-- signatures: disp(expr_1, expr_2, ...) -->
### Function: disp (expr_1, expr_2, ...)

Es como `display` pero sólo se muestran los valores de
los argumentos, no las ecuaciones. Es útil para argumentos 
complicados que no tienen nombre o en situaciones en las que 
solamente es de interés el valor del argumento pero no su nombre.


Véanse también `ldisp` y `print`.


Ejemplos:








```maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$
(%i3) disp(x, b[1,2], sin(1.0));
                               123

                                  2
                             x - x

                        .8414709848078965

(%o3)                         done
```

<!-- category: Other -->
<!-- keywords: display -->
<!-- signatures: display(expr_1, expr_2, ...) -->
### Function: display (expr_1, expr_2, ...)

Muestra las ecuaciones cuyos miembros izquierdos son 
*expr_i* sin evaluar y cuyos miembros derechos son los 
valores de las expresiones. Esta función es útil en los 
bloques y en las sentencias `for` para mostrar resultados 
intermedios.  Los argumentos de `display` suelen ser átomos, 
variables subindicadas o llamadas a funciones.


Véanse también `ldisplay`, `disp` y `ldisp`.


Ejemplos:








```maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$
(%i3) display(x, b[1,2], sin(1.0));
                             x = 123

                                      2
                         b     = x - x
                          1, 2

                  sin(1.0) = .8414709848078965

(%o3)                         done
```

<!-- category: Other -->
<!-- keywords: display2d -->
<!-- signatures: display2d -->
### Variable: display2d

Valor por defecto: `true`


Si `display2d` vale `false`, la salida por consola es
una cadena unidimensional, en lugar de una expresión bidimensional.


Véase también `leftjust` para cambiar la justificación a
la izquierda o el centrado de la ecuación.


Ejemplo:








```maxima
(%i1) x/(x^2+1);
                               x
(%o1)                        ------
                              2
                             x  + 1
(%i2) display2d:false$
(%i3) x/(x^2+1);
(%o3) x/(x^2+1)
```

<!-- category: Other -->
<!-- keywords: display_format_internal -->
<!-- signatures: display_format_internal -->
### Variable: display_format_internal

Valor por defecto: `false`


Si `display_format_internal` vale `true`,
las expresiones se muestran sin ser transformadas de manera que oculten su representación matemática interna. Se representa lo que la función `inpart` devolvería, en oposición a `part`.


Ejemplos:



```maxima
User     part       inpart
a-b;      a - b     a + (- 1) b

           a            - 1
a/b;       -         a b
           b
                       1/2
sqrt(x);   sqrt(x)    x

          4 X        4
X*4/3;    ---        - X
           3         3
```

<!-- category: Other -->
<!-- keywords: dispterms -->
<!-- signatures: dispterms(expr) -->
### Function: dispterms (expr)

Muestra *expr* en partes, una debajo de la otra.
Esto es, primero se muestra el operador de *expr*, luego 
cada término si se trata de una suma, o cada factor si es un 
producto, o si no se muestra separadamente la parte de una expresión 
más general. Es útil si *expr* es demasiado grande para 
representarla de otra forma.  Por ejemplo, si `P1`, `P2`, ...  
son expresiones muy grandes, entonces el programa de representación 
puede superar el espacio de almacenamiento tratando de mostrar 
`P1 + P2 + ...` todo junto.  Sin embargo, `dispterms (P1 + P2 + ...)` 
muestra `P1`, debajo  `P2`, etc.  Cuando una expresión exponencial 
es demasiado ancha para ser representada como `A^B`, si no se utiliza 
`dispterms`, entonces aparecerá como `expt (A, B)` (o como 
`ncexpt (A, B)`, en lugar de `A^^B`).


Ejemplo:



```maxima
(%i1) dispterms(2*a*sin(x)+%e^x);

+

2 a sin(x)

  x
%e

(%o1)                         done
```

<!-- category: Other -->
<!-- keywords: expt, ncexpt -->
<!-- signatures: expt(a, b), ncexpt(a, b) -->
### Function: expt (a, b)

Si una expresión exponencial es demasiado ancha para ser mostrada como `a^b` aparecerá como `expt (a, b)` (o como `ncexpt (a, b)` en lugar de `a^^b`).




Las funciones `expt` y `ncexpt` no se reconocen en una entrada.

<!-- category: Other -->
<!-- keywords: exptdispflag -->
<!-- signatures: exptdispflag -->
### Variable: exptdispflag

Valor por defecto: `true`


Si `exptdispflag` vale `true`, Maxima muestra las expresiones con 
exponentes negativos como cocientes. Véase también `%edispflag`.


Ejemplo:



```maxima
(%i1) exptdispflag:true;
(%o1)                         true
(%i2) 10^-x;
                                1
(%o2)                          ---
                                 x
                               10
(%i3) exptdispflag:false;
(%o3)                         false
(%i4) 10^-x;
                                - x
(%o4)                         10
```

<!-- category: Other -->
<!-- keywords: grind -->
<!-- signatures: grind(expr) -->
### Function: grind (expr)

La función `grind` imprime *expr*
en la consola en un formato admisible como entrada para Maxima. La función 
`grind` devuelve siempre `done`.


Cuando *expr* es el nombre de una función o macro, `grind`
muestra la definición de la función o de la macro en lugar de sólo
su nombre.


Véase también `string`, que devuelve una cadena en lugar de imprimir la salida. La función
`grind` intenta imprimir la expresión de forma que sea lago más sencilla de leer que la salida de `string`.


Cuando la variable `grind` vale `true`,
la salida de `string` y `stringout` tienen el mismo formato que la de `grind`;
en caso contrario no se formatea la salida de esas funciones.
El valor por defecto de la variable `grind` es `false`.


La variable `grind` también se puede utilizar como  argumento en `playback`.
Si `grind` está presente,
`playback` imprime las expresiones de entrada en el mismo formato que lo hace la función `grind`;
en caso contrario no se formatean la expresiones de entrada.


La función `grind` evalúa sus argumentos.


Ejemplos:



























```maxima
(%i1) aa + 1729;
(%o1)                       aa + 1729
(%i2) grind (%);
aa+1729$
(%o2)                         done
(%i3) [aa, 1729, aa + 1729];
(%o3)                 [aa, 1729, aa + 1729]
(%i4) grind (%);
[aa,1729,aa+1729]$
(%o4)                         done
(%i5) matrix ([aa, 17], [29, bb]);
                           [ aa  17 ]
(%o5)                      [        ]
                           [ 29  bb ]
(%i6) grind (%);
matrix([aa,17],[29,bb])$
(%o6)                         done
(%i7) set (aa, 17, 29, bb);
(%o7)                   {17, 29, aa, bb}
(%i8) grind (%);
{17,29,aa,bb}$
(%o8)                         done
(%i9) exp (aa / (bb + 17)^29);
                                aa
                            -----------
                                     29
                            (bb + 17)
(%o9)                     %e
(%i10) grind (%);
%e^(aa/(bb+17)^29)$
(%o10)                        done
(%i11) expr: expand ((aa + bb)^10);
         10           9        2   8         3   7         4   6
(%o11) bb   + 10 aa bb  + 45 aa  bb  + 120 aa  bb  + 210 aa  bb
         5   5         6   4         7   3        8   2
 + 252 aa  bb  + 210 aa  bb  + 120 aa  bb  + 45 aa  bb
        9        10
 + 10 aa  bb + aa
(%i12) grind (expr);
bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6
     +252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2
     +10*aa^9*bb+aa^10$
(%o12)                        done
(%i13) string (expr);
(%o13) bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6\
+252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2+10*aa^9*\
bb+aa^10
(%i14) cholesky (A):= block ([n : length (A), L : copymatrix (A),
  p : makelist (0, i, 1, length (A))], for i thru n do
  for j : i thru n do
  (x : L[i, j], x : x - sum (L[j, k] * L[i, k], k, 1, i - 1),
  if i = j then p[i] : 1 / sqrt(x) else L[j, i] : x * p[i]),
  for i thru n do L[i, i] : 1 / p[i],
  for i thru n do for j : i + 1 thru n do L[i, j] : 0, L)$
(%i15) grind (cholesky);
cholesky(A):=block(
         [n:length(A),L:copymatrix(A),
          p:makelist(0,i,1,length(A))],
         for i thru n do
             (for j from i thru n do
                  (x:L[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),
                   if i = j then p[i]:1/sqrt(x)
                       else L[j,i]:x*p[i])),
         for i thru n do L[i,i]:1/p[i],
         for i thru n do (for j from i+1 thru n do L[i,j]:0),L)$
(%o15)                        done
(%i16) string (fundef (cholesky));
(%o16) cholesky(A):=block([n:length(A),L:copymatrix(A),p:makelis\
t(0,i,1,length(A))],for i thru n do (for j from i thru n do (x:L\
[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),if i = j then p[i]:1/sqrt(x\
) else L[j,i]:x*p[i])),for i thru n do L[i,i]:1/p[i],for i thru \
n do (for j from i+1 thru n do L[i,j]:0),L)
```

<!-- category: Other -->
<!-- keywords: ibase -->
<!-- signatures: ibase -->
### Variable: ibase

Valor por defecto: `10`


`ibase` es la base en la que Maxima lee valores enteros.


A `ibase` se le puede asignar cualquier entero entre
2 y 36 (base decimal), ambos inclusive.
Si `ibase` es mayor que 10,
las cifras a utilizar serán los dígitos de
0 a 9, junto con las letras del alfabeto A, B, C, ..., 
tantas como sean necesarias para completar la base `ibase`.
Las letras se interpretarán como cifras sólo cuando el 
primer dígito sea un valor entre 9.
Es indiferente hacer uso de letras mayúsculas o minúsculas.
Las cifras para la base 36, la mayor posible, son los 
dígitos numéricos de 0 a 9 y las letras desde
la A hasta la Z.


Cualquiera que sea el valor de `ibase`, si un entero termina
con un punto decimal, se interpretará en base 10.


Véase también `obase`.


Ejemplos:


`ibase` menor que 10.








```maxima
(%i1) ibase : 2 $
(%i2) obase;
(%o2)                          10
(%i3) 1111111111111111;
(%o3)                         65535
```


`ibase` mayor que 10.
Las letras se interpretan como dígitos sólo
si el primer dígito es una cifra entre 0 y 9.












```maxima
(%i1) ibase : 16 $
(%i2) obase;
(%o2)                          10
(%i3) 1000;
(%o3)                         4096
(%i4) abcd;
(%o4)                         abcd
(%i5) symbolp (abcd);
(%o5)                         true
(%i6) 0abcd;
(%o6)                         43981
(%i7) symbolp (0abcd);
(%o7)                         false
```


Independientemente del valor de `ibase`, si el entero
termina con un punto decimal, se interpretará en base
diez.









```maxima
(%i1) ibase : 36 $
(%i2) obase;
(%o2)                          10
(%i3) 1234;
(%o3)                         49360
(%i4) 1234.;
(%o4)                         1234
```

<!-- category: Other -->
<!-- keywords: inchar -->
<!-- signatures: inchar -->
### Variable: inchar

Valor por defecto: `%i`


La variable `inchar` es el prefijo de las etiquetas de las
expresiones introducidas por el usuario. Maxima crea automáticamente 
una etiqueta para cada expresión de entrada concatenando `inchar` 
y `linenum`.


A `inchar` se le puede asignar cualquier símbolo 
o cadena, no necesariamente un caracácter sencillo. Puesto que
internamente Maxima solo tiene en cuenta el primer carácter del
prefijo, los prefijos `inchar`, `outchar` y `linechar`
deben comenzar con caracteres diferentes; en caso contrario, sentencias
como `kill(inlables)` pueden dar resultados inesperados.


Véase también `labels`.


Ejemplo:







```maxima
(%i1) inchar: "input";
(%o1)                         input
(input2) expand((a+b)^3);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(input3)
```

<!-- category: Other -->
<!-- keywords: infolists -->
<!-- signatures: infolists -->
### Variable: infolists

Valor por defecto: `[]`


La variable `infolists` es una lista con los nombres de todas las listas que guardan información sobre Maxima. Estas son:



**labels** — Todas las etiquetas `%i`, `%o` y `%t` con valores asignados.
**values** — Todos los átomos que son variables de usuario, no opciones de Maxima creadas con  `:` o `::`.
**functions** — Todas las funciones de usuario creadas con `:=` o `define`.
**arrays** — Arreglos declarados y no declarados, creados por `:`, `::` o `:=`.
**macros** — Cualquier macro definida por el usuario.
**myoptions** — Todas las opciones inicializadas por el usuario, independientemente de que posteriormente hayan sido devueltas a sus valores por defecto.
**rules** — Reglas de patrones y simplificación definidas por el usuario, creadas con `tellsimp`, `tellsimpafter`, `defmatch` o `defrule`.
**aliases** — Átomos que tienen un "alias" definido por el usuario, creado por las funciones `alias`, `ordergreat` o `orderless` o por haber declarado el átomo como `noun` (nombre) con `declare`.
**dependencies** — Átomos que tienen dependencias funcionales, creados por las funciones `depends` o `gradef`.
**gradefs** — Funciones que tienen derivadas definidas por el usuario, creadas por la función `gradef`.
**props** — Todos los átomos que tengan cualquier propiedad que no sea de las mencionadas hasta ahora, como las establecidas por `atvalue`, `matchdeclare`, etc., así como propiedadas especificadas en la función `declare`.
**let_rule_packages** — Todos los paquetes de reglas `let` definidos por el usuario, junto con el paquete especial `default_let_rule_package`; `default_let_rule_package` es el nombre del paquete de reglas utilizado cuando no se use ningún otro especificado por el usuario.

<!-- category: Other -->
<!-- keywords: kill -->
<!-- signatures: kill(a_1, ..., a_n), kill(labels), kill(inlabels, outlabels, linelabels), kill(n), kill([m, n]), kill(values, functions, arrays, ...), kill(all), kill(allbut(a_1, ..., a_n)) -->
### Function: kill (a_1, ..., a_n)

Elimina todas las asignaciones (valor, función, arreglo o regla) hechas a los
argumentos *a_1*, ..., *a_n*.
Un argumento *a_k* puede ser un símbolo o el elemento
de un array. Si *a_k* es elemento de un array, `kill` elimina la
asignación hecha a este elemento sin afectar al resto del array.


Se reconocen varios argumentos especiales. 
Se pueden combinar diferentes clases de argumentos, 
como por ejemplo, `kill (inlabels, functions, allbut (foo, bar))`.


La instrucción `kill (labels)` borra todas las asignaciones asociadas
a las etiquetas de entrada, de salida e intermedias creadas hasta el
momento. La instrucción `kill (inlabels)` elimina únicamente
las asignaciones de las etiquetas de entrada que comienzan con el
valor actual de `inchar`. Del mismo modo, `kill (outlabels)`
elimina únicamente las asignaciones de las etiquetas de salida
que comienzan con el valor actual de `outchar`. Finalmente,
`kill (linelabels)` elimina únicamente las asignaciones
de las etiquetas de las expresiones intermedias
que comienzan con el valor actual de `linechar`.


La instrucción `kill (n)`, siendo *n* un entero,
elimina las asignaciones de las últimas *n* etiquetas, tanto
de entrada como de salida.


La instrucción `kill ([m, n])` elimina las asignaciones
hechas a las etiquetas de entrada y salida desde la *m* hasta la*n*.


La instrucción `kill (infolist)`, siendo *infolist* 
cualquier elemento de `infolists` (como `values`, `functions` 
o `arrays`), elimina todas las asignaciones hechas a los elementos de
*infolist*. Véase también `infolists`.


La instrucción `kill (all)` elimina todas las asignaciones de
todas las variables, pero no reinicia las variables globales a sus
valores por defecto. Véase también `reset`.


La instrucción `kill (allbut (a_1, ..., a_n))`
elimina las asignaciones hechas a todas las variables,
excepto a *a_1*, ..., *a_n*; la instrucción
`kill (allbut (infolist))` elimina todas las asignaciones,
excepto las de los elementos de *infolist*, pudiendo ser *infolist*
igual a `values`, `functions`, `arrays`, etc.


La memoria reservada para una asignación no se libera hasta que
no se vacíen todos los símbolos
asociados con esta asignación; por ejemplo, para liberar la memoria
del valor de un símbolo es necesario eliminar tanto
la asignación de la etiqueta de salida que muestra el resultado,
como la del propio símbolo.


La función `kill` no evalua sus argumentos. 
El operador comilla-comilla, `''`, obliga a que se realice la evaluación.


La llamada `kill (symbol)` elimina todas las propiedades de *symbol*.
Por el contrario, `remvalue`, `remfunction`, `remarray` y `remrule`
eliminan propiedades específicas. 


`kill` siempre devuelve `done`, incluso cuando alguno de sus 
argumentos carecía de asignación previa.

<!-- category: Other -->
<!-- keywords: labels -->
<!-- signatures: labels(symbol) -->
### Function: labels (symbol)

Retorna la lista de etiquetas de entrada, salida o de expresiones intermedias las cuales empiezan con *symbol*. 
Típicamente *symbol* es el valor de las variables `inchar`, `outchar` o `linechar`. 
El caractér de etiqueta puede ser pasado con o sin signo de porcentaje, 
así, por ejemplo, `i` y `%i` producen el mismo resultado.  


Si ninguna etiqueta empieza con *symbol*, `labels` retorna a una
lista vacía. 


La función `labels` no evalua su argumento.
El operador comilla-comilla, `''`, obliga a que se realice la evaluación.
Por ejemplo, 
`labels (''inchar)` devuelve las etiquetas de entrada que empiezan con el caractér de etiqueta de entrada actual. 


La variable `labels` es una lista de las etiquetas de entrada, salida y expresiones intermedias, incluyendo todas las etiquetas anteriores en el caso de que `inchar`, `outchar` o `linechar` hayan sido redefinidas. 


Por defecto, Maxima muestra el resultado de cada expresión introducida por el usuario, asignando al resultado una etiqueta de salida. 
La salida (es decir el resultado) puede ser suprimida terminando la expresión de entrada con un `$` (signo de dólar) en vez de un `;` (punto y coma). 
En este caso, se crea la etiqueta de salida y se le asigna el resultado, aunque éste no se muestre; aún así, la etiqueta puede ser referenciada de la misma forma que se hace con aquéllas cuyos resultados sí son mostrados.


Véanse también: `%`, `%%` y `%th`. 


Las etiquetas de expresiones intermedias pueden ser generadas por algunas funciones. El interruptor `programmode` controla si `solve` y algunas otras funciones generan etiquetas de expresiones intermedias en vez de retornar una lista de expresiones. 
Algunas otras funciones, tales como `ldisplay`, siempre generan etiquetas de expresiones intermedias. 

 

Véase también: `inchar`, `outchar`, `linechar` y `infolists`.

<!-- category: Other -->
<!-- keywords: ldisp -->
<!-- signatures: ldisp(expr_1, ..., expr_n) -->
### Function: ldisp (expr_1, ..., expr_n)

Muestra las expresiones *expr_1*, ..., *expr_n* en la consola con el formato de salida;
`ldisp` asigna una etiqueta a cada argumento y devuelve la lista de etiquetas.


Véanse también `disp`, `display` y `ldisplay`.



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisp (e, f);
                                   3
(%t3)                       (b + a)

                     3        2      2      3
(%t4)               b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                   3
(%o4)                       (b + a)
(%i5) %t4;
                     3        2      2      3
(%o5)               b  + 3 a b  + 3 a  b + a
```

<!-- category: Other -->
<!-- keywords: ldisplay -->
<!-- signatures: ldisplay(expr_1, ..., expr_n) -->
### Function: ldisplay (expr_1, ..., expr_n)

Muestra las expresiones *expr_1*, ..., *expr_n* en la consola con el formato de salida.
Cad expresión se muestra como una ecuación de la forma `lhs = rhs`
en la que `lhs` es uno de los argumentos de `ldisplay`
y `rhs` su valor. Normalmente, cada argumento será el nombre de una variable. La función
`ldisp` asigna una etiqueta a cada ecuación y devuelve la lista de etiquetas.


Véanse también `disp`, `display` y `ldisp`.



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisplay (e, f);
                                     3
(%t3)                     e = (b + a)

                       3        2      2      3
(%t4)             f = b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                     3
(%o4)                     e = (b + a)
(%i5) %t4;
                       3        2      2      3
(%o5)             f = b  + 3 a b  + 3 a  b + a
```

<!-- category: Other -->
<!-- keywords: linechar -->
<!-- signatures: linechar -->
### Variable: linechar

Valor por defecto: `%t`


La variable `linechar` es el prefijo de las etiquetas que
genera Maxima para expresiones intermedias. Cuando sea necesario,
Maxima creará una etiqueta para cada expresión intermedia 
concatenando `linechar` y `linenum`.


A `linechar` se le puede asignar cualquier símbolo 
o cadena, no necesariamente un caracácter sencillo. Puesto que
internamente Maxima solo tiene en cuenta el primer carácter del
prefijo, los prefijos `inchar`, `outchar` y `linechar`
deben comenzar con caracteres diferentes; en caso contrario, sentencias
como `kill(inlables)` pueden dar resultados inesperados.


Las expresiones intermedias pueden ser mostradas o no.
Véanse también `programmode` y `labels`.

<!-- category: Other -->
<!-- keywords: linel -->
<!-- signatures: linel -->
### Variable: linel

Valor por defecto: `79`


La variable `linel` es la anchura (medida en número de caracteres) de la consola que se le da a Maxima para que muestre las expresiones. A `linel` se le puede asignar cualquier valor, pero si éste es muy pequeño o grande resultará de poca utilidad. El texto que impriman las funciones internas de Maxima, como los mensajes de error y las salidas de la función `describe`, no se ve afectado por el valor de `linel`.

<!-- category: Other -->
<!-- keywords: linenum -->
<!-- signatures: linenum -->
### Variable: linenum

El número de la línea del par de expresiones de entrada y salida actuales.

<!-- category: Other -->
<!-- keywords: lispdisp -->
<!-- signatures: lispdisp -->
### Variable: lispdisp

Valor por defecto: `false`


Si `lispdisp` vale `true`, los símbolos de Lisp se muestran precedidos del carácter de interrogación `?`. En caso contrario, los símbolos de Lisp se muestran sin esta marca.


Ejemplos:









```maxima
(%i1) lispdisp: false$
(%i2) ?foo + ?bar;
(%o2)                       foo + bar
(%i3) lispdisp: true$
(%i4) ?foo + ?bar;
(%o4)                      ?foo + ?bar
```

<!-- category: Other -->
<!-- keywords: myoptions -->
<!-- signatures: myoptions -->
### Variable: myoptions

Valor por defecto: `[]`


`myoptions` es la lista de todas las opciones que nunca fueron reconfiguradas por el usuario, aunque éstas hayan sido reconfiguradas a su valor por defecto.

<!-- category: Other -->
<!-- keywords: negsumdispflag -->
<!-- signatures: negsumdispflag -->
### Variable: negsumdispflag

Valor por defecto: `true`


Si `negsumdispflag` vale `true`, `x - y` se muestra como `x - y`
en lugar de `- y + x`.  Dándole el valor `false` se realiza un análisis adicional para que no se representen de forma muy diferente dos expresiones similares.  Una aplicación puede ser para que `a + %i*b` y `a - %i*b` se representen ambas de la misma manera.

<!-- category: Other -->
<!-- keywords: nolabels -->
<!-- signatures: nolabels -->
### Variable: nolabels

Valor por defecto: `false`


Cuando `nolabels` vale `true`,
las etiquetas de entrada y salida 
(`%i` y `%o`, respectivamente)
son mostradas, pero a éstas no se les 
asignan los resultados; además, las etiquetas no se
incorporan a la lista `labels`.
Puesto que a las etiquetas no se les asignan resultados, 
el colector de basura puede recuperar la memoria ocupada
por éstos.


En el caso contrario, a las etiquetas de entrada y salida se les asignan los resultados correspondientes y son añadidas a la lista `labels`.


Las etiquetas de expresiones intermedias (`%t`) no se ven afectadas por la variable `nolabels`;
independientemente de que `nolabels` valga `true` o `false`, a las etiquetas de expresiones intermedias se les asignan siempre valores, además de ser añadidas a la lista `labels`.


Véanse también `batch`, `batchload` y `labels`.

<!-- category: Other -->
<!-- keywords: obase -->
<!-- signatures: obase -->
### Variable: obase

Valor por defecto: `10`


`obase` es la base en la que Maxima imprime los números enteros.


A `obase` se le puede asignar cualquier entero entre
2 y 36 (base decimal), ambos inclusive.
Si `obase` es mayor que 10,
las cifras a utilizar serán los dígitos de
0 a 9, junto con las letras del alfabeto A, B, C, ..., 
tantas como sean necesarias para completar la base `obase`.
Si el primer dígito resulta ser una letra, se le
añadirá el cero como prefijo.
Las cifras para la base 36, la mayor posible, son los 
dígitos numéricos de 0 a 9 y las letras desde
la A hasta la Z.


Véase también `ibase`.


Ejemplos:













```maxima
(%i1) obase : 2;
(%o1)                          10
(%i2) 2^8 - 1;
(%o10)                      11111111
(%i3) obase : 8;
(%o3)                          10
(%i4) 8^8 - 1;
(%o4)                       77777777
(%i5) obase : 16;
(%o5)                          10
(%i6) 16^8 - 1;
(%o6)                       0FFFFFFFF
(%i7) obase : 36;
(%o7)                          10
(%i8) 36^8 - 1;
(%o8)                       0ZZZZZZZZ
```

<!-- category: Other -->
<!-- keywords: optionset -->
<!-- signatures: optionset -->
### Variable: optionset

Valor por defecto: `false`


Cuando `optionset` tiene como valor `true`, Maxima imprime un
mensaje cada vez que una opción de Maxima es reconfigurada. Esto es 
muy útil si el usuario duda con frecuencia de la correctitud de alguna
opción y quiere estar seguro de la variable a la que él asignó un
valor fue verdaramente una variable opción (o interruptor). 


Ejemplo:



```maxima
(%i1) optionset:true;
assignment: assigning to option optionset
(%o1)                         true
(%i2) gamma_expand:true;
assignment: assigning to option gamma_expand
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: outchar -->
<!-- signatures: outchar -->
### Variable: outchar

Valor por defecto: `%o`


La variable `outchar` es el prefijo de las etiquetas de las 
expresiones calculadas por Maxima. Maxima crea automáticamente 
una etiqueta para cada expresión calculada concatenando `outchar`
y `linenum`.


A `outchar` se le puede asignar cualquier símbolo 
o cadena, no necesariamente un caracácter sencillo. Puesto que
internamente Maxima solo tiene en cuenta el primer carácter del
prefijo, los prefijos `inchar`, `outchar` y `linechar`
deben comenzar con caracteres diferentes; en caso contrario, sentencias
como `kill(inlables)` pueden dar resultados inesperados.


Véase también `labels`.


Ejemplo:







```maxima
(%i1) outchar: "output";
(output1)                    output
(%i2) expand((a+b)^3);
                     3        2      2      3
(output2)           b  + 3 a b  + 3 a  b + a
(%i3)
```

<!-- category: Other -->
<!-- keywords: pfeformat -->
<!-- signatures: pfeformat -->
### Variable: pfeformat

Valor por defecto: `false`


Si `pfeformat` vale `true`, una fracción de enteros será mostrada con el carácter de barra inclinada `/` entre ellos.




```maxima
(%i1) pfeformat: false$
(%i2) 2^16/7^3;
                              65536
(%o2)                         -----
                               343
(%i3) (a+b)/8;
                              b + a
(%o3)                         -----
                                8
(%i4) pfeformat: true$ 
(%i5) 2^16/7^3;
(%o5)                       65536/343
(%i6) (a+b)/8;
(%o6)                      1/8 (b + a)
```

<!-- category: Other -->
<!-- keywords: playback -->
<!-- signatures: playback(), playback(n), playback([m, n]), playback([m]), playback(input), playback(slow), playback(time), playback(grind) -->
### Function: playback ()

Muestra las entradas, salidas y expresiones intermedias 
sin recalcularlas. 
`playback` sólo muestra las expresiones asociadas con etiquetas; 
cualquier otra salida (tal como texto impreso por `print` o `describe`, o mensajes de error) no es mostrada. 
Véase también: `labels`. 


`playback` no evalua sus argumentos. 
El operador comilla-comilla, `''`, obliga a que se realice la evaluación.
`playback` siempre devuelve `done`. 


`playback ()` (sin argumentos) muestra todas las entradas, salidas y expresiones intermedias generadas hasta el momento. 
Una expresión de salida es mostrada incluso si ésta fue suprimida por el caracter de terminación `$`, cuando fue originalmente calculada. 


`playback (n)`  muestra las *n* expresiones más recientes. Cada entrada, salida y expresión intermedia cuenta como una. 


`playback ([m, n])` muestra entradas, salidas y expresiones intermedias con los números desde *m* hasta *n*, ambos inclusive. 


`playback ([m])` es equivalente a `playback ([m, m])`;
esto usualmente imprime un par de expresiones de entrada y salida. 


`playback (input)` muestra todas las expresiones de entrada generadas hasta el momento. 


`playback (slow)` hace pausas entre expresiones y
espera a que el usuario pulse la tecla `enter` para continuar. 
Esto es un comportamiento similar a `demo`. 




`playback (slow)` es muy útil en conjunción con `save` o
`stringout` cuando se crea un archivo secundario de almacenamiento con el objetivo de elegir cuidadosamente las expresiones realmente útiles. 





`playback (time)` muestra el tiempo de computo por cada expresión. 





`playback (grind)` muestra las expresiones de entrada 
en el mismo formato como la función `grind`. 
Las expresiones de salida no se ven afectadas por la opción 
`grind`. 
Vea `grind`. 
Los argumentos pueden ser combinados, por ejemplo, 
`playback ([5, 10], grind, time, slow)`.

<!-- category: Other -->
<!-- keywords: powerdisp -->
<!-- signatures: powerdisp -->
### Variable: powerdisp

Valor por defecto: `false`


Si `powerdisp` vale `true`, se muestran las sumas con sus términos ordenados de menor a mayor potencia. Así, un polinomio se presenta como una serie de potencias truncada con el término constante al principio y el de mayor potencia al final.


Por defecto, los términos de una suma se muestran en el orden de las potencias decrecientes.


Ejemplo:



```maxima
(%i1) powerdisp:true;
(%o1)                         true
(%i2) x^2+x^3+x^4;
                           2    3    4
(%o2)                     x  + x  + x
(%i3) powerdisp:false;
(%o3)                         false
(%i4) x^2+x^3+x^4;
                           4    3    2
(%o4)                     x  + x  + x
```

<!-- category: Other -->
<!-- keywords: print -->
<!-- signatures: print(expr_1, ..., expr_n) -->
### Function: print (expr_1, ..., expr_n)

Evalúa y muestra las expresiones  *expr_1*, ..., *expr_n* secuencialmente de izquierda a derecha, comenzando la impresión por el borde izquierdo de la consola.


El valor devuelto por `print` es el valor de su último argumento. La función `print` no genera etiquetas para las expresiones intermedias.


Véanse también `display`, `disp`, `ldisplay` y `ldisp`, que muestran una expresión por línea, mientras que `print` trata de mostrar dos o más expresiones por línea.


Para mostrar el contenido de un archivo véase `printfile`.



```maxima
(%i1) r: print ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is",
      radcan (log (a^10/b)))$
            3        2      2      3
(a+b)^3 is b  + 3 a b  + 3 a  b + a  log (a^10/b) is 

                                              10 log(a) - log(b) 
(%i2) r;
(%o2)                  10 log(a) - log(b)
(%i3) disp ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is",
      radcan (log (a^10/b)))$
                           (a+b)^3 is

                     3        2      2      3
                    b  + 3 a b  + 3 a  b + a

                         log (a^10/b) is

                       10 log(a) - log(b)
```

<!-- category: Other -->
<!-- keywords: prompt -->
<!-- signatures: prompt -->
### Variable: prompt

Valor por defecto: `_`


`prompt` es el símbolo del prompt de la función `demo`, 
del modo `playback (slow)` y del bucle de interrupción de Maxima (el que se invoca con `break`).

<!-- category: Other -->
<!-- keywords: quit -->
<!-- signatures: quit() -->
### Function: quit ()

Termina una sesión de Maxima. 
Nótese que la función debe ser invocada como `quit();` o `quit()$`, no como `quit`. 


Para parar un cálculo muy demorado 
pulse `Control-C`. 
La acción por defecto es retornar a prompt de Maxima. 
Si `*debugger-hook*` tiene como valor `nil`,
pulsar `Control-C` abrirá el depurador de Lisp. 
Vea también: `debugging`.

<!-- category: Other -->
<!-- keywords: read -->
<!-- signatures: read(expr_1, ..., expr_n) -->
### Function: read (expr_1, ..., expr_n)

Imprime *expr_1*, ..., *expr_n* y a continuación lee una expresión desde la consola y devuelve la expresión evaluada. La expresión termina con un punto y coma `;` o con el símbolo de dólar `$`.


Véase también `readonly`.



```maxima
(%i1) foo: 42$ 
(%i2) foo: read ("foo vale", foo, " -- nuevo valor.")$
foo vale 42  -- nuevo valor. 
(a+b)^3;
(%i3) foo;
                                     3
(%o3)                         (b + a)
```

<!-- category: Other -->
<!-- keywords: readonly -->
<!-- signatures: readonly(expr_1, ..., expr_n) -->
### Function: readonly (expr_1, ..., expr_n)

Imprime *expr_1*, ..., *expr_n* y a continuación lee una expresión desde la consola y devuelve la expresión sin evaluar. La expresión termina con un punto y coma `;` o con el símbolo de dólar `$`.



```maxima
(%i1) aa: 7$
(%i2) foo: readonly ("Introducir expresion:");
Introducir expresion: 
2^aa;
                                  aa
(%o2)                            2
(%i3) foo: read ("Introducir expresion:");
Introducir expresion: 
2^aa;
(%o3)                            128
```


Véase también `read`.

<!-- category: Other -->
<!-- keywords: reset -->
<!-- signatures: reset() -->
### Function: reset ()

Reconfigura muchas variables y opciones globales y algunas otras variables a sus valores por defecto. 


`reset` procesa las variables que se encuentran en la lista Lisp 
`*variable-initial-values*`. 
La macro Lisp `defmvar` pone las variables en ésta lista (entre otras acciones). 
Muchas, pero no todas, las variables y opciones globales son definidas por `defmvar`, y algunas variables definidas por `defmvar` no son ni variables ni opciones globales.

<!-- category: Other -->
<!-- keywords: showtime -->
<!-- signatures: showtime -->
### Variable: showtime

Valor por defecto: `false`


Cuando `showtime` tiene como valor `true`, el tiempo de cálculo y el tiempo de retardo se imprimen junto con la salida de cada expresión. 


El tiempo de cálculo se almacena siempre, de manera que `time` y `playback` puedan mostrar el tiempo de cálculo incluso cuando `showtime` vale `false`.


Véase también `timer`.

<!-- category: Other -->
<!-- keywords: sqrtdispflag -->
<!-- signatures: sqrtdispflag -->
### Variable: sqrtdispflag

Valor por defecto: `true`


Si `sqrtdispflag` vale `false`, hará que `sqrt` se muestre con el exponente 1/2.

<!-- category: Other -->
<!-- keywords: stardisp -->
<!-- signatures: stardisp -->
### Variable: stardisp

Valor por defecto: `false`


Si `stardisp` vale `true`, la multiplicación se muestra con un asterisco `*` entre los operandos.

<!-- category: Other -->
<!-- keywords: to_lisp -->
<!-- signatures: to_lisp() -->
### Function: to_lisp ()

Entra en el intérprete Lisp bajo Maxima. `(to-maxima)` retorna de nuevo a Maxima. 


Ejemplo:


Define una función y entra en el nivel Lisp. La definición
se consulta en la lista de propiedades, luego se extrae la definición
de la función, se factoriza y almacena el resultado en la variable `$result`.
Esta variable se puede utilizar luego una vez se haya vuelto al nivel
de Maxima.



```maxima
(%i1) f(x):=x^2+x;
                                         2
(%o1)                           f(x) := x  + x
(%i2) to_lisp();
Type (to-maxima) to restart, ($quit) to quit Maxima.

MAXIMA> (symbol-plist '$f)
(MPROPS (NIL MEXPR ((LAMBDA) ((MLIST) $X) ((MPLUS) ((MEXPT) $X 2) $X))))
MAXIMA> (setq $result ($factor (caddr (mget '$f 'mexpr))))
((MTIMES SIMP FACTORED) $X ((MPLUS SIMP IRREDUCIBLE) 1 $X))
MAXIMA> (to-maxima)
Returning to Maxima
(%o2)                                true
(%i3) result;
(%o3)                              x (x + 1)
```

<!-- category: Other -->
<!-- keywords: ttyoff -->
<!-- signatures: ttyoff -->
### Variable: ttyoff

Valor por defecto: `false`


Si `ttyoff` vale `true`, no se muestran las expresiones resultantes, pero éstas se calculan de todos modos y se les asignan etiquetas. Véase `labels`.


El texto que escriban las funciones internas de Maxima, tales como los mensajes de error y las salidas de `describe`,
no se ven afectadas por `ttyoff`.

<!-- category: Other -->
<!-- keywords: values -->
<!-- signatures: values -->
### Variable: values

Valor inicial: `[]`


`values` es una lista de todas las variables que el usuario ha creado
(no incluye las opciones de Maxima ni los interruptores). 
La lista comprende los símbolos a los que se ha asignado un
valor mediante `:` o `::`.


Si el valor de una variable se borra con cualquiera de las instrucciones
`kill`, `remove` o `remvalue`, dicha variable desaparece
de la lista `values`.


Véase `functions` para una lista de funciones definidas por el
usuario.


Ejemplos:


Primero, `values` muestra los símbolos `a`, 
`b` y `c`, pero no `d`, pues no tiene valor asignado,
ni la función de usuario `f`. Luego los valores de las variables se
borran y `values` queda como una lista vacía.









```maxima
(%i1) [a:99, b::a-90, c:a-b, d, f(x):= x^2];
                                                  2
(%o1)                     [99, 9, 90, d, f(x) := x ]
(%i2) values;
(%o2)                              [a, b, c]
(%i3) [kill(a), remove(b,value), remvalue(c)];
(%o3)                          [done, done, [c]]
(%i4) values;
(%o4)                                 []
```

