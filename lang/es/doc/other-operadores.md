## Operadores

<!-- category: Other -->
<!-- keywords: # -->
<!-- signatures: # -->
### Function: #

Representa la negación de la igualdad sintáctica `=`.


Nótese que debido a las reglas de evaluación de expresiones
de tipo predicado (en concreto debido a que `not expr`
obliga a la evaluación previa de *expr*), 
`not a = b` equivale a `is(a # b)`, 
pero no a `a # b`.


Ejemplos:











```maxima
(%i1) a = b;
(%o1)                         a = b
(%i2) is (a = b);
(%o2)                         false
(%i3) a # b;
(%o3)                         a # b
(%i4) not a = b;
(%o4)                         true
(%i5) is (a # b);
(%o5)                         true
(%i6) is (not a = b);
(%o6)                         true
```

<!-- category: Other -->
<!-- keywords: ** -->
<!-- signatures: ** -->
### Function: **

Operador de exponenciación.
Maxima identifica `**` con el operador `^` en la entrada
de expresiones, pero se representa como `^` en las salidas
no formateadas (`display2d=false`), o colocando un 
superíndice en la salida formateada (`display2d=true`).


La función `fortran` representa el operador de exponenciación
con `**`, tanto si se ha introducido como `**` o como `^`.


Ejemplos:









```maxima
(%i1) is (a**b = a^b);
(%o1)                         true
(%i2) x**y + x^z;
                              z    y
(%o2)                        x  + x
(%i3) string (x**y + x^z);
(%o3)                        x^z+x^y
(%i4) fortran (x**y + x^z);
      x**z+x**y
(%o4)                         done
```

<!-- category: Other -->
<!-- keywords: +, -, *, /, ^ -->
<!-- signatures: -, *, /, ^ -->
### Function: +

Los símbolos `+` `*` `/` y `^` representan
la suma, resta, multiplicación, división y exponenciación, respectivamente.
Los nombres de estos operadores son `"+"` `"*"` `"/"` y `"^"`,
que pueden aparecer allá donde se requiera el nombre de una función u operador.


Los símbolos `+` y `-` representan el positivo y negativo unario,
siendo los nombres de estos operadores `"+"` y `"-"`, respectivamente.


En Maxima, la resta `a - b` se representa como la suma `a + (- b)`.
Expresiones tales como `a + (- b)` se muestran como restas. Maxima
reconoce `"-"` tan solo como el operador de negación unaria, no como
el nombre del operador de resta binaria.


La división `a / b` se representa en maxima como la multiplicación
`a * b^(- 1)`. Expresiones tales como `a * b^(- 1)` se muestran 
como divisiones. Maxima reconoce `"/"` como el nombre del operador
de división.


La suma y la multiplicación son operadores conmutativos n-arios. La 
división y la exponenciación son operadores no conmutativos binarios.


Maxima ordena los operandos de los operadores conmutativos para
formar lo que se conoce como representación canónica. A efectos de
almacenamiento interno, la ordenación viene determinada por `orderlessp`.
A efectos de presentación de las expresiones, la ordenación de la suma
la determina `ordergreatp`, y en el caso de la multiplicación, la
ordenación coincide con la del almacenamiento interno.


Los cálculos aritméticos se realizan con números literales
(enteros, racionales, decimales ordinarios y decimales grandes).
Excepto en el caso de la exponenciación, todas las operaciones
aritméticas con números dan lugar a resultados en forma de
números. La exponenciación da como resultado un número
si alguno de los operandos es decimal ordinario o grande (*bigfloat*),
o si el resultado es un entero o racional; en caso contrario,
la exponenciación puede expresarse como una raíz
cuadrada (`sqrt`), como otra potencia, o simplemente no
sufre cambios.


Se produce contagio de los decimales en coma flotante en los
cálculos aritméticos: si algún operando es un número decimal
grande (*bigfloat*), el resultado será también un número
decimal grande; no habiendo decimales grandes, pero sí
ordinarios, el resultado srá también un decimal ordinario; de no
haber operandos decimales, el resultado será un número racional o
entero. 


Los cálculos aritméticos son simplificaciones, no evaluaciones, por lo
que se realizan en expresiones comentadas.


Las operaciones aritméticas se aplican elemento a elemento en el
caso de las listas cuando la variable global `listarith` vale `true`;
pero en el caso de las matrices, siempre se aplican elemento a elemento.
Cuando un operando es una lista o matriz y otro operando lo es de otro tipo
cualquiera, éste se combina con cada uno de los elementos de la lista o
matriz.


Ejemplos:


La suma y la multiplicación son operadores conmutativos n-arios.
Maxima ordena los operandos para formar lo que se conoce como 
representación canónica. Los nombres de estos operadores son
`"+"` y `"-"`.











```maxima
(%i1) c + g + d + a + b + e + f;
(%o1)               g + f + e + d + c + b + a
(%i2) [op (%), args (%)];
(%o2)              [+, [g, f, e, d, c, b, a]]
(%i3) c * g * d * a * b * e * f;
(%o3)                     a b c d e f g
(%i4) [op (%), args (%)];
(%o4)              [*, [a, b, c, d, e, f, g]]
(%i5) apply ("+", [a, 8, x, 2, 9, x, x, a]);
(%o5)                    3 x + 2 a + 19
(%i6) apply ("*", [a, 8, x, 2, 9, x, x, a]);
                                 2  3
(%o6)                       144 a  x
```


La división y la exponenciación son operadores no conmutativos binarios.
Los nombres de estos operadores son `"/"` y `"^"`.








```maxima
(%i1) [a / b, a ^ b];
                              a   b
(%o1)                        [-, a ]
                              b
(%i2) [map (op, %), map (args, %)];
(%o2)              [[/, ^], [[a, b], [a, b]]]
(%i3) [apply ("/", [a, b]), apply ("^", [a, b])];
                              a   b
(%o3)                        [-, a ]
                              b
```


La resta y la división se representan internamente en
términos de la suma y multiplicación, respectivamente.







```maxima
(%i1) [inpart (a - b, 0), inpart (a - b, 1), inpart (a - b, 2)];
(%o1)                      [+, a, - b]
(%i2) [inpart (a / b, 0), inpart (a / b, 1), inpart (a / b, 2)];
                                   1
(%o2)                       [*, a, -]
                                   b
```


Los cálculos se realizan con números literales.
Se produce el contagio de los números decimales.







```maxima
(%i1) 17 + b - (1/2)*29 + 11^(2/4);
                                       5
(%o1)                   b + sqrt(11) + -
                                       2
(%i2) [17 + 29, 17 + 29.0, 17 + 29b0];
(%o2)                   [46, 46.0, 4.6b1]
```


Los cálculos aritméticos son una simplificación, no una
evaluación.









```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) '(17 + 29*11/7 - 5^3);
                              29 11    3
(%o2)                    17 + ----- - 5
                                7
(%i3) simp : true;
(%o3)                         true
(%i4) '(17 + 29*11/7 - 5^3);
                                437
(%o4)                         - ---
                                 7
```


Los cálculos aritméticos se realizan elemento a elemento 
en las listas (según sea el valor de `listarith`) y
matrices.













```maxima
(%i1) matrix ([a, x], [h, u]) - matrix ([1, 2], [3, 4]);
                        [ a - 1  x - 2 ]
(%o1)                   [              ]
                        [ h - 3  u - 4 ]
(%i2) 5 * matrix ([a, x], [h, u]);
                          [ 5 a  5 x ]
(%o2)                     [          ]
                          [ 5 h  5 u ]
(%i3) listarith : false;
(%o3)                         false
(%i4) [a, c, m, t] / [1, 7, 2, 9];
                          [a, c, m, t]
(%o4)                     ------------
                          [1, 7, 2, 9]
(%i5) [a, c, m, t] ^ x;
                                      x
(%o5)                     [a, c, m, t]
(%i6) listarith : true;
(%o6)                         true
(%i7) [a, c, m, t] / [1, 7, 2, 9];
                              c  m  t
(%o7)                     [a, -, -, -]
                              7  2  9
(%i8) [a, c, m, t] ^ x;
                          x   x   x   x
(%o8)                   [a , c , m , t ]
```

<!-- category: Other -->
<!-- keywords: . -->
<!-- signatures: . -->
### Function: .

El operador punto, para multiplicación de matrices (no-conmutativo). 
Cuando `"."` se usa de esta forma, se dejarán espacios a
ambos lados de éste, como en `A . B`. Así se evita que se confunda con el punto decimal de los números. 


Véanse:
`dot`,
`dot0nscsimp`,
`dot0simp`,
`dot1simp`,
`dotassoc`,
`dotconstrules`,
`dotdistrib`,
`dotexptsimp`,
`dotident`
y
`dotscrules`.

<!-- category: Other -->
<!-- keywords: : -->
<!-- signatures: : -->
### Function: :

Operador de asignación.


Cuando el miembro de la izquierda es una variable simple (no subindicada),
`:` evalúa la expresión de la derecha y asigna ese
valor a la variable del lado izquierdo.


Cuando en el lado izquierdo hay un elemento subindicado correspondiente a
una lista, matriz, array declarado de Maxima o array de Lisp, la expresión de
la derecha se asigna a ese elemento. El subíndice debe hacer
referencia a un elemento ya existente, ya que los objetos anteriores no 
pueden ampliarse nombrando elementos no existentes.


Cuando en el lado izquierdo hay un elemento subindicado correspondiente a
un array no declarado de Maxima, la expresión de la derecha se asigna a ese elemento
en caso de que ya exista, o a un nuevo elemento, si éste todavía
no existe.


Cuando el miembro de la izquierda es una lista de átomos y/o variables subindicadas,
el miembro derecho debe evaluar también a una lista, cuyos elementos serán
asignados en paralelo a las variables de la lista de la izquierda.


Véanse también `kill` y `remvalue`, que deshacen las asociaciones
hechas por el operador `:`.


Ejemplos:


Asignación a una variable simple.








```maxima
(%i1) a;
(%o1)                           a
(%i2) a : 123;
(%o2)                          123
(%i3) a;
(%o3)                          123
```


Asignación a un elemento de una lista.








```maxima
(%i1) b : [1, 2, 3];
(%o1)                       [1, 2, 3]
(%i2) b[3] : 456;
(%o2)                          456
(%i3) b;
(%o3)                      [1, 2, 456]
```


La asignación crea un array no declarado.










```maxima
(%i1) c[99] : 789;
(%o1)                          789
(%i2) c[99];
(%o2)                          789
(%i3) c;
(%o3)                           c
(%i4) arrayinfo (c);
(%o4)                   [hashed, 1, [99]]
(%i5) listarray (c);
(%o5)                         [789]
```


Asignación múltiple.









```maxima
(%i1) [a, b, c] : [45, 67, 89];
(%o1)                     [45, 67, 89]
(%i2) a;
(%o2)                          45
(%i3) b;
(%o3)                          67
(%i4) c;
(%o4)                          89
```


La asignación múltiple se hace en paralelo. Los valores
de `a` y `b` se intercambian en este ejemplo.









```maxima
(%i1) [a, b] : [33, 55];
(%o1)                       [33, 55]
(%i2) [a, b] : [b, a];
(%o2)                       [55, 33]
(%i3) a;
(%o3)                          55
(%i4) b;
(%o4)                          33
```

<!-- category: Other -->
<!-- keywords: :: -->
<!-- signatures: :: -->
### Function: ::

Operador de asignación.


El operador `::` es similar a `:`, excepto que `::`
evalúa ambos miembros, tanto el derecho como el izquierdo.


Ejemplos:













```maxima
(%i1) x : 'foo;
(%o1)                          foo
(%i2) x :: 123;
(%o2)                          123
(%i3) foo;
(%o3)                          123
(%i4) x : '[a, b, c];
(%o4)                       [a, b, c]
(%i5) x :: [11, 22, 33];
(%o5)                     [11, 22, 33]
(%i6) a;
(%o6)                          11
(%i7) b;
(%o7)                          22
(%i8) c;
(%o8)                          33
```

<!-- category: Other -->
<!-- keywords: ::= -->
<!-- signatures: ::= -->
### Function: ::=

El operador de definición de macros `::=` define una función (llamada macro por razones históricas) que no evalúa sus argumentos, siendo la expresión que retorna (llamada "macroexpansión") evaluada dentro del contexto desde el cual se ha invocado la macro. En cualquier otro sentido, una función macro es igual que una función ordinaria.


`macroexpand` devuelve la expresión que a su vez fue devuelta por una macro (sin evaluar la expresión);
`macroexpand (foo (x))` seguida de `''%` es equivalente a `foo (x)` si `foo` es una función macro.


`::=` coloca el nombre de la nueva función macro en la lista global `macros`. Por otro lado, las funciones 
`kill`, `remove` y `remfunction` borran las definiciones de las funciones macro y eliminan sus nombres de la lista `macros`.


Las funciones `fundef` y `dispfun` devuelven la definición de una función macro y le asignan una etiqueta, respectivamente.


Las funciones macro normalmente contienen expresiones `buildq` y `splice` para construir una expresión, que luego será evaluada.


Ejemplos:


Una función macro no evalúa sus argumentos, por lo que el mensaje (1) muestra `y - z`, no el valor de `y - z`.
La macroexpansión (es decir, la expresión no evaluada `'(print ("(2) x is equal to", x))`) se evalúa en el contexto desde el cual se produjo la llamada a la macro, imprimiendo el mensaje (2).











```maxima
(%i1) x: %pi$

(%i2) y: 1234$

(%i3) z: 1729 * w$

(%i4) printq1 (x) ::= block (print ("(1) x is equal to", x),
'(print ("(2) x is equal to", x)))$

(%i5) printq1 (y - z);
(1) x is equal to y - z
(2) x is equal to %pi
(%o5)                                 %pi
```



Una función ordinaria evalúa sus argumentos, por lo que el mensaje (1) muestra el valor de `y - z`.
El valor de retorno no se evalúa, por lo que el mensaje (2) no se imprime hasta la evaluación explícita `''%`.












```maxima
(%i1) x: %pi$

(%i2) y: 1234$

(%i3) z: 1729 * w$

(%i4) printe1 (x) := block (print ("(1) x is equal to", x),
'(print ("(2) x is equal to", x)))$

(%i5) printe1 (y - z);
(1) x is equal to 1234 - 1729 w
(%o5)                     print((2) x is equal to, x)
(%i6) ''%;
(2) x is equal to %pi
(%o6)                                 %pi
```


`macroexpand` devuelve la macroexpansión;
`macroexpand (foo (x))` seguida de `''%` es equivalente a `foo (x)` si `foo` es una función macro.












```maxima
(%i1) x: %pi$

(%i2) y: 1234$

(%i3) z: 1729 * w$

(%i4) g (x) ::= buildq ([x], print ("x is equal to", x))$

(%i5) macroexpand (g (y - z));
(%o5)                     print(x is equal to, y - z)
(%i6) ''%;
x is equal to 1234 - 1729 w
(%o6)                            1234 - 1729 w
(%i7) g (y - z);
x is equal to 1234 - 1729 w
(%o7)                            1234 - 1729 w
```

<!-- category: Other -->
<!-- keywords: := -->
<!-- signatures: := -->
### Function: :=

El operador de definición de funciones. 
La expresión `f(x_1, ..., x_n) := expr`
define una función de nombre *f* con argumentos
*x_1*, ..., *x_n* y cuerpo *expr*.
El operador `:=` no evalúa el cuerpo de la función (a menos que
se indique lo contrario mediante el operador comilla-comilla `''`).
La función así definida puede ser una función ordinaria
de Maxima (con argumentos encerrados entre paréntesis) o una función
array (con argumentos encerrados entre corchetes).


Cuando el último o único argumento *x_n* es una lista de un solo
elemento, la función definida por `:=` acepta un número variable
de argumentos. Los valores de los argumentos se asignan uno a uno a los
argumentos formales *x_1*, ..., *x_(n - 1)*, y cualesquiera otros
valores de argumentos, si existen, se asignan a *x_n* en forma de lista.


Todas las definiciones de funciones aparecen en el mismo espacio de
nombres; definiendo una función `f` dentro de otra función `g`
no limita automáticamente el alcance de `f` a `g`.
No obstante, `local(f)` hace que la función `f`
sea efectiva solamente dentro del bloque o empaquetado de expresiones en la
que aparece `local`.


Si un argumento formal *x_k* es un símbolo afectado por el
operador comilla (expresión nominal), la función definida por `:=` no evalúa el
correspondiente valor de argumento. 
En cualquier otro caso, los argumentos que se pasan son evaluados.


Véanse también `define` y `::=`.


Ejemplos:


`:=` no evalúa el cuerpo de la función (a menos que
se indique lo contrario mediante el operador comilla-comilla `''`).










```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) F1 (x, y) := expr;
(%o2)                   F1(x, y) := expr
(%i3) F1 (a, b);
(%o3)                    cos(y) - sin(x)
(%i4) F2 (x, y) := ''expr;
(%o4)              F2(x, y) := cos(y) - sin(x)
(%i5) F2 (a, b);
(%o5)                    cos(b) - sin(a)
```


La función así definida puede ser una función ordinaria
de Maxima o una función array.







```maxima
(%i1) G1 (x, y) := x.y - y.x;
(%o1)               G1(x, y) := x . y - y . x
(%i2) G2 [x, y] := x.y - y.x;
(%o2)                G2     := x . y - y . x
                       x, y
```


Cuando el último o único argumento *x_n* es una lista de un solo
elemento, la función definida por `:=` acepta un número variable
de argumentos.







```maxima
(%i1) H ([L]) := apply ("+", L);
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


`local` define una función como local.









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
<!-- keywords: <, <=, >=, > -->
<!-- signatures: <=, >=, > -->
### Function: < (=)

Los símbolos `<`, `<=`, `>=` y `>`
representan menor que, menor o igual que, mayor o igual que y mayor que, respectivamente.
Los nombres de estos operadores son `"<"` `"<="` `">="` y `">"`,
que pueden aparecer allá donde se requiera el nombre de una función u operador.


Estos operadores relacionales son todos operadores binarios. Maxima
no reconoce expresiones del estilo `a < b < c`.


Las expresiones relacionales devuelven valores booleanos haciendo uso 
de las funciones `is` o `maybe`, así como de las
sentencias condicionales `if`, `while` y `unless`.
Las expresiones relacionales no se evalúan de otra manera, aunque sus
argumentos sí sean evaluados.


Cuando una expresión relacional no pueda ser evaluada a `true` o `false`,
el comportamiento de `is` y de `if` estará controlado por la variable
global `prederror`. Si `prederror` toma el valor `true`, `is` y
`if` emiten un mensaje de error. Si `prederror` toma el valor `false`,
`is` devuelve `unknown` y `if` devuelve una expresión condicional
parcialmente evaluada.


`maybe` se comporta siempre como si `prederror` fuese `false`,
al tiempo que `while` y `unless` se comportan siempre como si
`prederror` fuese `true`.


Los operadores relacionales no se distribuyen sobre listas ni sobre cualesquiera
otros tipos de estructuras de datos.


Véanse también `=`, `#`, `equal` y `notequal`.


Ejemplos:


Las expresiones relacionales se reducen a valores booleanos a través de ciertas
funciones y sentencias condicionales.











```maxima
(%i1) [x, y, z] : [123, 456, 789];
(%o1)                    [123, 456, 789]
(%i2) is (x < y);
(%o2)                         true
(%i3) maybe (y > z);
(%o3)                         false
(%i4) if x >= z then 1 else 0;
(%o4)                           0
(%i5) block ([S], S : 0, 
             for i:1 while i <= 100 do S : S + i, return (S));
(%o5)                         5050
```


Las expresiones relacionales no se evalúan de otra manera, aunque sus
argumentos sí sean evaluados.








```maxima
(%o1)                    [123, 456, 789]
(%i2) [x < y, y <= z, z >= y, y > z];
(%o2)    [123 < 456, 456 <= 789, 789 >= 456, 456 > 789]
(%i3) map (is, %);
(%o3)               [true, true, true, false]
```

<!-- category: Other -->
<!-- keywords: = -->
<!-- signatures: = -->
### Function: =

Operador de ecuación.


La expresión `a = b` representa una ecuación
sin evaluar, la cual puede verificarse o no. Las ecuaciones sin evaluar 
pueden aparecer como argumentos de `solve`, `algsys`
y de algunas otras funciones.


La función `is` evalúa el operador `=` a un
resultado booleano; `is(a = b)` asigna un valor
de verdad a `a = b`, siendo `true` si
*a* y *b* son idénticos, lo cual acontece si
ambos *a* y *b* son átomos idénticos, o si no
siendo átomos, sus operadores y argumentos respectivos
son idénticos; en caso contrario, `is(a = b)`
devuelve el valor  `false`. Nunca se devuelve el valor `unknown`.
Cuando `is(a = b)` toma el valor `true`, 
se dice que *a* y *b* son sintácticamente iguales,
no expresiones equivalentes, para las cuales 
`is(equal(a, b))` devuelve `true`.
Las expresiones pueden ser equivalentes, pero no 
sintácticamente iguales.


La negación de `=` se representa por `#`.
Como en el caso de `=`, la expresión 
`a # b` no está evaluada; sin embargo,
`is(a # b)` evalúa `a # b`
a `true` o `false`.


Además de `is`, hay otros operadores que evalúan 
`=` y `#` a `true` o `false`;
a saber, `if`, `and`, `or` y `not`.


Nótese que debido a las reglas de evaluación de expresiones
de tipo predicado (en concreto debido a que `not expr`
obliga a la evaluación previa de *expr*), 
`not a = b` equivale a `is(a # b)`, 
pero no a `a # b`.


Las funciones `rhs` y `lhs` devuelven los miembros
derecho e izquierdo, respectivamente, de una ecuación o inecuación.


Véanse también `equal` y `notequal`.


Ejemplos:


La expresión `a = b` representa una ecuación
sin evaluar, la cual puede verificarse o no.










```maxima
(%i1) eq_1 : a * x - 5 * y = 17;
(%o1)                    a x - 5 y = 17
(%i2) eq_2 : b * x + 3 * y = 29;
(%o2)                    3 y + b x = 29
(%i3) solve ([eq_1, eq_2], [x, y]);
                        196         29 a - 17 b
(%o3)          [[x = ---------, y = -----------]]
                     5 b + 3 a       5 b + 3 a
(%i4) subst (%, [eq_1, eq_2]);
         196 a     5 (29 a - 17 b)
(%o4) [--------- - --------------- = 17, 
       5 b + 3 a      5 b + 3 a
                                  196 b     3 (29 a - 17 b)
                                --------- + --------------- = 29]
                                5 b + 3 a      5 b + 3 a
(%i5) ratsimp (%);
(%o5)                  [17 = 17, 29 = 29]
```


`is(a = b)` evalúa `a = b` 
a `true` si *a* y *b*
son sintácticamente iguales (es decir, idénticas).
Las expresiones pueden ser equivalentes, pero no 
sintácticamente iguales.









```maxima
(%i1) a : (x + 1) * (x - 1);
(%o1)                    (x - 1) (x + 1)
(%i2) b : x^2 - 1;
                              2
(%o2)                        x  - 1
(%i3) [is (a = b), is (a # b)];
(%o3)                     [false, true]
(%i4) [is (equal (a, b)), is (notequal (a, b))];
(%o4)                     [true, false]
```


Algunos operadores evalúan `=` y `#` a `true` o `false`.










```maxima
(%i1) if expand ((x + y)^2) = x^2 + 2 * x * y + y^2
        then FOO else BAR;
(%o1)                          FOO
(%i2) eq_3 : 2 * x = 3 * x;
(%o2)                       2 x = 3 x
(%i3) eq_4 : exp (2) = %e^2;
                              2     2
(%o3)                       %e  = %e
(%i4) [eq_3 and eq_4, eq_3 or eq_4, not eq_3];
(%o4)                  [false, true, true]
```


Debido a que `not expr`
obliga a la evaluación previa de *expr*, 
`not a = b` equivale a `is(a # b)`.







```maxima
(%i1) [2 * x # 3 * x, not (2 * x = 3 * x)];
(%o1)                   [2 x # 3 x, true]
(%i2) is (2 * x # 3 * x);
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: ^^ -->
<!-- signatures: ^^ -->
### Function: ^^

Operador de exponenciación no conmutativa.
Se trata del operador de exponenciación correspondiente a la
multiplicación no conmutativa `.`, del mismo modo que el
operador de exponenciación ordinario `^` se corresponde 
con la multiplicación conmutativa `*`.


La exponenciación no conmutativa se representa como `^^`
en las salidas no formateadas (`display2d=false`), o colocando un 
superíndice entre ángulos (`< >`) en la salida 
formateada (`display2d=true`).


Ejemplos:







```maxima
(%i1) a . a . b . b . b + a * a * a * b * b;
                        3  2    <2>    <3>
(%o1)                  a  b  + a    . b
(%i2) string (a . a . b . b . b + a * a * a * b * b);
(%o2)                  a^3*b^2+a^^2 . b^^3
```

<!-- category: Other -->
<!-- keywords: and -->
<!-- signatures: and -->
### Function: and

Operador de conjunción lógica.
El operador `and` es un operador infijo `n`-ario;
sus operandos son expresiones booleanas y su resultado es un valor lógico.


El operador `and` impone la evaluación (igual que `is`) de uno o más operandos,
y puede forzar la evaluación de todos los operandos.


Los operandos se evalúan en el orden en el que aparecen; 
sólo evalúa tantos operandos como sean necesarios para determinar el resultado.
Si algún operando vale `false`,
el resultado es `false` y ya no se evalúan más operandos.


La variable global `prederror` controla el comportamiento de `and`
cuando la evaluación de un operando no da como resultado `true` o `false`;
`and` imprime un mensaje de error cuando `prederror` vale `true`.
Cuando los operandos devuelven un valor diferente a `true` o `false`
al ser evaluados, el resultado es una expresión booleana.


El operador `and` no es conmutativo:
`a and b` puede no ser igual a `b and a` debido al tratamiento de operandos indeterminados.

<!-- category: Other -->
<!-- keywords: infix -->
<!-- signatures: infix(op), infix(op, lbp, rbp), infix(op, lbp, rbp, lpos, rpos, pos) -->
### Function: infix (op)

Declara *op* como operador infijo.
Un operador infijo es una función de dos argumentos,
con el nombre de la función escrito entre sus argumentos.
Por ejemplo, el operador de sustracción `-` es un operador infijo.


`infix (op)` declara *op* como operador infijo
con fuerzas de ligadura por la izquierda y por la derecha iguales a 180, que es el valor por defecto, 
y partes izquierda y derecha iguales a `any`.



`infix (op, lbp, rbp)` declara *op* como operador infijo
con fuerzas de ligadura por la izquierda y por la derecha declaradas en los argumentos, siendo las partes izquierda y derecha iguales a `any`.


`infix (op, lbp, rbp, lpos, rpos, pos)`
declara *op* como operador infijo con fuerzas de ligadura por la 
izquierda y por la derecha, junto con los tipos de expresiones correspondientes
a *lpos*, *rpos* y *pos*, que son el operando de la izquierda,
el de la derecha y el operador del resultado; los tipos reconocidos son:
`expr`, `clause` y `any`, que indican expresión algebraica,
expresión booleana o cualquier otra, respectivamente. Maxima puede detectar
algunos errores sintácticos comparando los tipos declarados con los de la expresión
actual.


La precedencia de *op* con respecto a otros operadores deriva de las fuerzas de ligadura de los operadores en cuestión.
Si las fuerzas de ligadura a izquierda y derecha de *op* son ambas mayores que las fuerzas de ligadura a izquierda y derecha de otro operador, entonces *op* tiene preferencia sobre el otro operador. Si las fuerzas de ligadura no son ambas mayores o menores, se aplican otras relaciones más complejas.


La asociatividad de *op* depende de las fuerzas de ligadura.
Una mayor fuerza de ligadura a la izquierda (*lbp*) implica que *op* sea evaluado antes que otros operadores a su izquierda en la expresión, mientras que mayor fuerza de ligadura a la derecha (*rbp*) implica que *op* sea evaluado antes que otros operadores a su derecha en la expresión.
Así, si *lbp* es mayor, *op* es asociativo por la derecha, mientras que si *rbp* es mayor, *op* es asociativo por la izquierda.


Véase también `Syntax`.


Ejemplos:


Si las fuerzas de ligadura a izquierda y derecha de *op* son ambas mayores que las fuerzas de ligadura a izquierda y derecha de otro operador, entonces *op* tiene preferencia sobre el otro operador.












```maxima
(%i1) :lisp (get '$+ 'lbp)
100
(%i1) :lisp (get '$+ 'rbp)
100
(%i1) infix ("##", 101, 101);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")");
(%o2)       (a ## b) := sconcat("(", a, ",", b, ")")
(%i3) 1 + a ## b + 2;
(%o3)                       (a,b) + 3
(%i4) infix ("##", 99, 99);
(%o4)                          ##
(%i5) 1 + a ## b + 2;
(%o5)                       (a+1,b+2)
```


Mayor *lbp* hace a *op* asociativo por la derecha,
mientras que mayor  *rbp* hace a *op* asociativo por la izquierda.










```maxima
(%i1) infix ("##", 100, 99);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")")$
(%i3) foo ## bar ## baz;
(%o3)                    (foo,(bar,baz))
(%i4) infix ("##", 100, 101);
(%o4)                          ##
(%i5) foo ## bar ## baz;
(%o5)                    ((foo,bar),baz)
```


Maxima puede detectar algunos errores sintácticos comparando
los tipos declarados con los de la expresión actual.









```maxima
(%i1) infix ("##", 100, 99, expr, expr, expr);
(%o1)                          ##
(%i2) if x ## y then 1 else 0;
Incorrect syntax: Found algebraic expression where logical expression expected
if x ## y then 
             ^
(%i2) infix ("##", 100, 99, expr, expr, clause);
(%o2)                          ##
(%i3) if x ## y then 1 else 0;
(%o3)                if x ## y then 1 else 0
```

<!-- category: Other -->
<!-- keywords: matchfix -->
<!-- signatures: matchfix(ldelimiter, rdelimiter), matchfix(ldelimiter, rdelimiter, arg_pos, pos) -->
### Function: matchfix (ldelimiter, rdelimiter)

Declara un operador "matchfix" con delimitadores a la izquierda y derecha, *ldelimiter* y *rdelimiter*, respectivamente. Los delimitadores son cadenas alfanuméricas.


Un operador "matchfix" es una función con un número arbitrario de argumentos, de manera que los argumentos se presentan entre los delimitadores de la izquierda y derecha. Los delimitadores pueden ser cualquier tipo de cadena, en tanto que el analizador sintáctico pueda distinguirlos de los operandos y de expresiones con operadores. En la práctica esto excluye delimitadores como `%`, `,`, `$` y `;`,  necesitando aislar los delimitadores con espacios en blanco. El delimitador de la derecha puede ser igual o diferente del de la izquierda.


Un delimitador de la izquierda sólo puede asociarse con un único delimitador de la derecha; dos operadores "matchfix" diferentes no pueden tener el mismo delimitador por la izquierda.


Un operador ya existente puede declararse como operador "matchfix" sin necesidad de que cambie el resto de propiedades. En particular, los operadores de Maxima tales como la suma `+` pueden ser declarados como "matchfix".


La llamada `matchfix (ldelimiter, rdelimiter, arg_pos, pos)` 
declara el argumento *arg_pos* y el resultado *pos*, así
como los delimitadores  *ldelimiter* y *rdelimiter*.


Los argumentos *arg_pos* y *pos* son tipos de funciones,
reconociéndose como tales: `expr`, `clause` y `any`,
los cuales hacen referencia a una expresión algebraica, booleana o
de cualquier otro tipo, respectivamente.
Maxima puede detectar ciertos errores sintácticos comparando el
tipo de expresión declarado con el de la expresión actual.


La función que ejecutará una operación "matchfix" será una típica función definida por el usuario. La función de operador se define por el método habitual con  `:=` o `define`. Los argumentos pueden escribirse entre los delimitadores, o con el delimitador izquierdo como una cadena precedida de apóstrofo y seguidamente los argumentos entre paréntesis. La llamada `dispfun (ldelimiter)` muestra la definición de la función.


El único operador "matchfix" de Maxima es el constructor de listas `[ ]`. Los paréntesis  `( )` y las comillas dobles  `" "`  actúan como operadores "matchfix", pero son tratados como operadores "matchfix" por el analizador sintáctico de Maxima.


Ejemplos:



- *
Los delimitadores pueden ser practicamente cualquier cadena.











```maxima
(%i1) matchfix ("@@", "~");
(%o1)                          @@
(%i2) @@ a, b, c ~;
(%o2)                      @@a, b, c~
(%i3) matchfix (">>", "<<");
(%o3)                          >>
(%i4) >> a, b, c <<;
(%o4)                      >>a, b, c<<
(%i5) matchfix ("foo", "oof");
(%o5)                          foo
(%i6) foo a, b, c oof;
(%o6)                     fooa, b, coof
(%i7) >> w + foo x, y oof + z << / @@ p, q ~;
                     >>z + foox, yoof + w<<
(%o7)                ----------------------
                            @@p, q~
```



- *
Los operadores "matchfix" son funciones definidas por el usuario.


```maxima
(%i1) matchfix ("!-", "-!");
(%o1)                         "!-"
(%i2) !- x, y -! := x/y - y/x;
                                    x   y
(%o2)                   !-x, y-! := - - -
                                    y   x
(%i3) define (!-x, y-!, x/y - y/x);
                                    x   y
(%o3)                   !-x, y-! := - - -
                                    y   x
(%i4) define ("!-" (x, y), x/y - y/x);
                                    x   y
(%o4)                   !-x, y-! := - - -
                                    y   x
(%i5) dispfun ("!-");
                                    x   y
(%t5)                   !-x, y-! := - - -
                                    y   x

(%o5)                         done
(%i6) !-3, 5-!;
                                16
(%o6)                         - --
                                15
(%i7) "!-" (3, 5);
                                16
(%o7)                         - --
                                15
```

<!-- category: Other -->
<!-- keywords: nary -->
<!-- signatures: nary(op), nary(op, bp, arg_pos, pos) -->
### Function: nary (op)

Un operador n-ario denota una función con un número arbitrario de
argumentos entre los que se intercal el símbolo del operador,
como en `A+B+C`. La instrucción `nary("x")` declara `x`
como operador n-ario. Las funciones se pueden declarar como n-arias;
de modo que si se ejecuta `declare(j,nary)`, el simplificador
transforma `j(j(a,b),j(c,d))` en `j(a, b, c, d)`.

<!-- category: Other -->
<!-- keywords: nofix -->
<!-- signatures: nofix(op), nofix(op, pos) -->
### Function: nofix (op)

Los operadores no-fijos se utilizan para definir funciones sin argumentos.
La mera presencia de tal operador en una instrucción hará que se
evalúe la función correspondiente. Por ejemplo, cuando se teclea `exit;`
para salir de una interrupción de Maxima, `exit` se comporta como una
función no-fija. La instrucción `nofix("x")` declara `x`
como operador no-fijo.

<!-- category: Other -->
<!-- keywords: not -->
<!-- signatures: not -->
### Function: not

Operador de negación lógica. El operador `not` es un operador prefijo;
su operando es una expresión booleana y su resultado es un valor lógico.


El operador `not` impone la evaluación (igual que `is`) de su operando.


La variable global `prederror` controla el comportamiento de
`not` cuando la evaluación de su operando no da como 
resultado `true` o `false`; `not` imprime un mensaje 
de error cuando `prederror` vale `true`.
Cuando los operandos devuelven un valor diferente a `true` o `false`
al ser evaluados, el resultado es una expresión booleana.

<!-- category: Other -->
<!-- keywords: or -->
<!-- signatures: or -->
### Function: or

Operador de disyunción lógica. El operador `or` es un operador infijo `n`-ario;
sus operandos son expresiones booleanas y su resultado es un valor lógico.


El operador `or` impone la evaluación (igual que `is`) de uno o más operandos,
y puede forzar la evaluación de todos los operandos.


Los operandos se evalúan en el orden en el que aparecen; `or` sólo evalúa tantos operandos como sean necesarios para determinar el resultado. Si un operando vale `true`, el resultado es `true` y ya no se evalúan más operandos.


La variable global `prederror` controla el comportamiento 
de `or` cuando la evaluación de un operando no da como 
resultado `true` o `false`; `or` imprime un 
mensaje de error cuando `prederror` vale `true`.
Cuando los operandos devuelven un valor diferente a `true` o `false`
al ser evaluados, el resultado es una expresión booleana.


El operador `or` no es conmutativo: `a or b` puede no ser igual a `b or a` debido al tratamiento de operandos indeterminados.

<!-- category: Other -->
<!-- keywords: postfix -->
<!-- signatures: postfix(op), postfix(op, lbp, lpos, pos) -->
### Function: postfix (op)

Los operadores sufijos son funciones de un único argumento en las que éste
precede al operador, como en `3!`. La instrucción `postfix("x")`
declara `x` como operador sufijo.

<!-- category: Other -->
<!-- keywords: prefix -->
<!-- signatures: prefix(op), prefix(op, rbp, rpos, pos) -->
### Function: prefix (op)

Los operadores prefijos son funciones de un único argumento en las que éste
se coloca a continuación del operador. La instrucción 
`prefix("x")` declara `x` como operador prefijo.

