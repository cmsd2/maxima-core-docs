## Base de datos de Maxima

<!-- category: Other -->
<!-- keywords: activate -->
<!-- signatures: activate(context_1, ..., context_n) -->
### Function: activate (context_1, ..., context_n)

Activa los contextos *context_1*, ..., *context_n*.
Los hechos en estos contextos están disponibles para hacer deducciones y extraer información.
Los hechos en estos contextos no se listan al invocar `facts ()`.


La variable `activecontexts` es la lista de contextos que se han activado por medio de la función `activate`.

<!-- category: Other -->
<!-- keywords: activecontexts -->
<!-- signatures: activecontexts -->
### Variable: activecontexts

Valor por defecto: `[]`


La variable `activecontexts` es la lista de contextos que se han activado por medio de la función `activate`, pero que no se han activado por ser subcontextos del contexto actual.

<!-- category: Other -->
<!-- keywords: alphabetic -->
<!-- signatures: alphabetic -->
### Variable: alphabetic

`alphabetic` es un tipo de propiedad reconocida por `declare`.
La expresión `declare(s, alphabetic)` le indica a Maxima que reconozca
como alfabéticos todos los caracteres que haya en *s*, que debe ser una cadena de texto.


Véase también `Identifiers`.


Ejemplo:









```maxima
(%i1) xx\~yy\`\@ : 1729;
(%o1)                         1729
(%i2) declare ("~`@", alphabetic);
(%o2)                         done
(%i3) xx~yy`@ + @yy`xx + `xx@@yy~;
(%o3)               `xx@@yy~ + @yy`xx + 1729
(%i4) listofvars (%);
(%o4)                  [@yy`xx, `xx@@yy~]
```

<!-- category: Other -->
<!-- keywords: askinteger -->
<!-- signatures: askinteger(expr, integer), askinteger(expr), askinteger(expr, even), askinteger(expr, odd) -->
### Function: askinteger (expr, integer)

La llamada `askinteger (expr, integer)` intenta determinar a partir de la base de datos de `assume` si *expr* es un entero. La función `askinteger` pide más información al usuario si no encuentra la respuesta,

tratando de almacenar la nueva información en la base de datos si es posible. La llamada 
`askinteger (expr)` equivale a `askinteger (expr, integer)`.


La llamadas `askinteger (expr, even)` ay `askinteger (expr, odd)` intentan determinar si *expr* es un entero par o impar, respectivamente.

<!-- category: Other -->
<!-- keywords: asksign -->
<!-- signatures: asksign(expr) -->
### Function: asksign (expr)

Primero intenta determinar si la expresión especificada es positiva, negativa o cero.  Si no lo consigue, planteará al usuario preguntas que le ayuden a conpletar la deducción. Las respuestas del usuario son almacenadas en la base de datos durante el tiempo que dure este cálculo. El valor que al final devuelva `asksign` será `pos`, `neg` o `zero`.

<!-- category: Other -->
<!-- keywords: assume -->
<!-- signatures: assume(pred_1, ..., pred_n) -->
### Function: assume (pred_1, ..., pred_n)

Añade los predicados *pred_1*, ..., *pred_n* al contexto actual.
Si un predicado es inconsistente o redundante con los otros predicados
del contexto actual, entonces no es añadido al contexto. 
El contexto va acumulando predicados con cada llamada a `assume`.


La función `assume` devuelve una lista cuyos miembros son los 
predicados que han sido añadidos al contexto, o los átomos 
`redundant` o `inconsistent` si fuere necesario.


Los predicados *pred_1*, ..., *pred_n* tan solo pueden ser
expresiones formadas con los operadores relacionales `< <= equal notequal >=`
y `>`. Los predicados no pueden estar formados por expresiones que sean del
tipo igualdad `=` ni del tipo desigualdad `#`, ni tampoco pueden ser
funciones de predicado como `integerp`.


En cambio, sí se reconocen predicados compuestos de la forma 
`pred_1 and ... and pred_n`, pero no 
`pred_1 or ... or pred_n`.
También se reconoce `not pred_k` si *pred_k* es un
predicado relacional. Expresiones de la forma `not (pred_1 and pred_2)`
y `not (pred_1 or pred_2)` no son reconocidas.


El mecanismo deductivo de Maxima no es muy potente; existen muchas 
consecuencias que, siendo obvias, no pueden ser obtenidas por `is`.
Se trata de una debilidad reconocida.


`assume` no gestiona predicados con números complejos. Si un
predicado contiene un número complejo, `assume` devuelve
`inconsistent` o `redunant`.


La función `assume` evalúa sus argumentos.


Véanse también `is`, `facts`, `forget`, `context` y `declare`.


Ejemplos:
















```maxima
(%i1) assume (xx > 0, yy < -1, zz >= 0);
(%o1)              [xx > 0, yy < - 1, zz >= 0]
(%i2) assume (aa < bb and bb < cc);
(%o2)                  [bb > aa, cc > bb]
(%i3) facts ();
(%o3)     [xx > 0, - 1 > yy, zz >= 0, bb > aa, cc > bb]
(%i4) is (xx > yy);
(%o4)                         true
(%i5) is (yy < -yy);
(%o5)                         true
(%i6) is (sinh (bb - aa) > 0);
(%o6)                         true
(%i7) forget (bb > aa);
(%o7)                       [bb > aa]
(%i8) prederror : false;
(%o8)                         false
(%i9) is (sinh (bb - aa) > 0);
(%o9)                        unknown
(%i10) is (bb^2 < cc^2);
(%o10)                       unknown
```

<!-- category: Other -->
<!-- keywords: assume_pos -->
<!-- signatures: assume_pos -->
### Variable: assume_pos

Valor por defecto: `false`


Si `assume_pos` vale `true` y el signo de un parámetro *x* no puede ser determinado a partir del contexto actual o de otras consideraciones, `sign` y `asksign (x)` devolverán `true`. Con esto se pueden evitar algunas preguntas al usuario que se generan automáticamente, como las que hacen `integrate` y otras funciones.


By default, a parameter is *x* such that `symbolp (x)`
or `subvarp (x)`.


Por defecto, un parámetro *x* es aquel para el que `symbolp (x)` o `subvarp (x)` devuelven `true`.
La clase de expresiones que se consideran parámetros se puede extender mediante la utilización de la variable `assume_pos_pred`.


Las funciones `sign` y `asksign` intentan deducir el signo de una expresión a partir de los signos de los operandos que contiene. Por ejemplo, si `a` y `b` son ambos positivos, entonces `a + b` también es positivo.


Sin embargo, no es posible obviar todas las preguntas que hace `asksign`. En particular, cuando el argumento de `asksign` es una diferencia `x - y` o un logaritmo `log(x)`, `asksign` siempre solicita una respuesta por parte del usuario, incluso cuando `assume_pos` vale `true` y `assume_pos_pred` es una función que devuelve `true` para todos los argumentos.

<!-- category: Other -->
<!-- keywords: assume_pos_pred -->
<!-- signatures: assume_pos_pred -->
### Variable: assume_pos_pred

Valor por defecto: `false`


Cuando a `assume_pos_pred` se le asigna el nombre de una función o una expresión lambda de un único argumento *x*, ésta será invocada para determinar si *x* se considera un parámetro por `assume_pos`. La variable 
`assume_pos_pred` se ignora cuando `assume_pos` vale `false`.


La función `assume_pos_pred` es invocada por  `sign` y por `asksign` con un argumento *x*, el cual puede ser un átomo, una variable subindicada o una expresión de llamada a una función. Si la función `assume_pos_pred` devuelve `true`, *x* será considerada como un parámetro por `assume_pos`.


Por defecto, un parámetro *x* es aquel para el que `symbolp (x)` o `subvarp (x)` devuelven `true`.


Véanse también `assume` y `assume_pos`.


Ejemplos:















```maxima
(%i1) assume_pos: true$
(%i2) assume_pos_pred: symbolp$
(%i3) sign (a);
(%o3)                          pos
(%i4) sign (a[1]);
(%o4)                          pnz
(%i5) assume_pos_pred: lambda ([x], display (x), true)$
(%i6) asksign (a);
                              x = a

(%o6)                          pos
(%i7) asksign (a[1]);
                             x = a
                                  1

(%o7)                          pos
(%i8) asksign (foo (a));
                           x = foo(a)

(%o8)                          pos
(%i9) asksign (foo (a) + bar (b));
                           x = foo(a)

                           x = bar(b)

(%o9)                          pos
(%i10) asksign (log (a));
                              x = a

Is  a - 1  positive, negative, or zero?

p;
(%o10)                         pos
(%i11) asksign (a - b);
                              x = a

                              x = b

                              x = a

                              x = b

Is  b - a  positive, negative, or zero?

p;
(%o11)                         neg
```

<!-- category: Other -->
<!-- keywords: assumescalar -->
<!-- signatures: assumescalar -->
### Variable: assumescalar

Valor por defecto: `true`


La variable `assumescalar` ayuda a controlar si una expresión `expr` para la cual `nonscalarp (expr)` es `false` va a tener un comportamiento similar a un escalar bajo ciertas transformaciones.


Sea `expr` cualquier expresión distinta de una lista o matriz, y sea también `[1, 2, 3]` una lista o una matriz. Entonces, `expr . [1, 2, 3]` dará como resultado `[expr, 2 expr, 3 expr]` si `assumescalar` es `true`, o si `scalarp (expr)` es `true`, o si `constantp (expr)` es `true`.


Si `assumescalar` vale `true`, la expresión se comportará como un escalar sólo en operaciones conmutativas, pero no en el caso de la multiplicación no conmutativa o producto matricial `.`.


Si `assumescalar` vale `false`, la expresión se comportará como un no escalar.


Si `assumescalar` vale `all`, la expresión se comportará como un escalar para todas las operaciones.

<!-- category: Other -->
<!-- keywords: bindtest -->
<!-- signatures: bindtest -->
### Variable: bindtest

La sentencia `declare(x, bindtest` le indica a Maxima que devuelva un mensaje
de error cuando el símbolo *x* no tenga asociado valor alguno.


Ejemplo:










```maxima
(%i1) aa + bb;
(%o1)                        bb + aa
(%i2) declare (aa, bindtest);
(%o2)                         done
(%i3) aa + bb;
aa unbound variable
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) aa : 1234;
(%o4)                         1234
(%i5) aa + bb;
(%o5)                       bb + 1234
```

<!-- category: Other -->
<!-- keywords: charfun -->
<!-- signatures: charfun(p) -->
### Function: charfun (p)

Devuelve 0 cuando el predicado *p* toma el valor `false`, y devuelve
1 cuando vale `true`.  Si el predicado toma un valor diferente de `true` y `false` (desconocido), 
entonces devuelve una forma nominal.


Ejemplos:









```maxima
(%i1) charfun(x<1);
(%o1) charfun(x<1)
(%i2) subst(x=-1,%);
(%o2) 1
(%i3) e : charfun('"and"(-1 < x, x < 1))$
(%i4) [subst(x=-1,e), subst(x=0,e), subst(x=1,e)];
(%o4) [0,1,0]
```

<!-- category: Other -->
<!-- keywords: compare -->
<!-- signatures: compare(x, y) -->
### Function: compare (x, y)

Devuelve un operador de comparación *op*
(`<`, `<=`, `>`, `>=`, `=` o `#`) de manera que
`is (x op y)` tome el valor `true`;
cuando tanto *x* como *y* dependan de `%i` y
`x # y`, devuelve `notcomparable`;
cuando no exista tal operador o Maxima sea incapaz de determinarlo, devolverá `unknown`.


Ejemplos:











```maxima
(%i1) compare(1,2);
(%o1) <
(%i2) compare(1,x);
(%o2) unknown
(%i3) compare(%i,%i);
(%o3) =
(%i4) compare(%i,%i+1);
(%o4) notcomparable
(%i5) compare(1/x,0);
(%o5) #
(%i6) compare(x,abs(x));
(%o6) <=
```


La función `compare` no intenta determinar si los dominios reales de sus argumentos son conjuntos no vacíos; así,






```maxima
(%i1) compare(acos(x^2+1), acos(x^2+1) + 1);
(%o1) <
```


Aquí, el dominio real de `acos (x^2 + 1)` es el conjunto vacío.

<!-- category: Other -->
<!-- keywords: constant -->
<!-- signatures: constant -->
### Function: constant

`declare(a, constant)` declara *a* como constante.  La declaración
de un símbolo como constante no impide que se le asigne un valor no
constante al símbolo.


Véanse `constantp` y `declare`


Ejemplo:



```maxima
(%i1) declare(c, constant);
(%o1)                         done
(%i2) constantp(c);
(%o2)                         true
(%i3) c : x;
(%o3)                           x
(%i4) constantp(c);
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: constantp -->
<!-- signatures: constantp(expr) -->
### Function: constantp (expr)

Devuelve `true` si *expr* es una expresión constante y
`false` en caso contrario.


Una expresión se considera constante si sus argumentos son números 
(incluidos los números racionales que se muestran con `/R/`), 
constantes simbólicas como `%pi`, `%e` o `%i`, variables 
con valor constante o declarada como constante por `declare`,
o funciones cuyos argumentos son constantes.


La función `constantp` evalúa sus argumentos.


Ejemplos:













```maxima
(%i1) constantp (7 * sin(2));
(%o1)                                true
(%i2) constantp (rat (17/29));
(%o2)                                true
(%i3) constantp (%pi * sin(%e));
(%o3)                                true
(%i4) constantp (exp (x));
(%o4)                                false
(%i5) declare (x, constant);
(%o5)                                done
(%i6) constantp (exp (x));
(%o6)                                true
(%i7) constantp (foo (x) + bar (%e) + baz (2));
(%o7)                                false
(%i8)
```

<!-- category: Other -->
<!-- keywords: context -->
<!-- signatures: context -->
### Variable: context

Valor por defecto: `initial`


La variable `context` da nombre al conjunto de hechos establecidos desde `assume` y `forget`. La función `assume` añade nuevos hechos al conjunto nombrado por `context`, mientras que `forget` los va eliminando.
Asignando a `context` un nuevo nombre *foo* cambia el contexto actual a *foo*. Si el contexto *foo* no existe todavía, se crea automáticamente mediante una llamada a `newcontext`.


Véase `contexts` para una descripción general del mecanismo que siguen los contextos.

<!-- category: Other -->
<!-- keywords: contexts -->
<!-- signatures: contexts -->
### Variable: contexts

Valor por defecto: `[initial, global]`


La variable `contexts` es una lista que contiene los contextos existentes, incluyendo el actualmente activo.


El mecanismo que siguen los contextos permiten al usuario agrupar y nombrar un conjunto de hechos, que recibe el nombre de contexto. Una vez hecho esto, el usuario puede hacer que Maxima tenga en cuenta o que olvide cualquier número de hechos sin más que activar o desactivar su contexto.


Cualquier átomo simbólico puede ser el nombre de un contexto, y los hechos contenidos en tal contexto pueden ser almacenados hasta que se destruyan uno a uno mediante llamadas a la función `forget`, o que se destruyan conjuntamente invocando a `kill` para eliminar el contexto al que pertenecen.


Los contextos tienen estructura jerárquica, siendo su raíz el contexto `global`, el cual contiene información sobre Maxima que necesitan algunas funciones. Cuando en un contexto todos los hechos están activos (lo que significa que están siendo utilizados en deducciones) lo estarán también en cualquier subcontexto del contexto actual.


Cuando se comienza una sesión de Maxima, el usuario estará trabajando en un contexto llamado `initial`, el cual tiene un subcontexto de nombre `global`.


Véanse también `facts`, `newcontext`, `supcontext`, `killcontext`, `activate`, `deactivate`, `assume` y `forget`.

<!-- category: Other -->
<!-- keywords: deactivate -->
<!-- signatures: deactivate(contexto_1, ..., contexto_n) -->
### Function: deactivate (contexto_1, ..., contexto_n)

Desactiva los contextos especificados *contexto_1*, ..., *contexto_n*.

<!-- category: Other -->
<!-- keywords: declare -->
<!-- signatures: declare(a_1, f_1, a_2, f_2, ...) -->
### Function: declare (a_1, f_1, a_2, f_2, ...)

Asigna al átomo o lista de átomos *a_i* la propiedad o lista de 
propiedades*p_i*. Si *a_i* y/o *p_i* son listas, cada uno de
los átomos adquiere todas las propiedades.


La función `declare` no evalúa sus argumentos y siempre devuelve la
expresión `done`.


La llamada `featurep (object, feature)` devuelve `true`
si *object* ha sido previamente declarado como poseedor de la propiedad
*feature*.


Véase también `features`.


La función `declare` reconoce las siguientes propiedades:



**additive** — Hace que Maxima simplifique las expresiones *a_i*
      haciendo uso de la sustitución 
      `a_i(x + y + z + ...)` `-->`
      `a_i(x) + a_i(y) + a_i(z) + ...`.
      Tal sustitución se aplica únicamente al primer argumento.
**alphabetic** — Indica a Maxima que reconozca todos los caracteres de la cadena alfanumérica
      *a_i* como caracteres alfabéticos.
**antisymmetric, commutative, symmetric** — Hace que Maxima reconozca a *a_i* como una función simétrica o
      antisimétrica. La propiedad `commutative` equivale a `symmetric`.
**bindtest** — Hace que Maxima envíe un error si *a_i* es evaluado sin habérsele
      asignado un valor.
**constant** — Hace que Maxima considere a *a_i* como una constante
      simbólica.
**even, odd** — Hace que Maxima reconozca a *a_i* como una variable entera par o impar.
**evenfun, oddfun** — Hace que Maxima reconozca a *a_i* como una función par o impar.
**evflag** — Hace que *a_i* sea reconocida por `ev`, de manera que a *a_i* se le
      asigne el valor `true` durante la ejecución de `ev` cuando *a_i* 
      aparezca como argumento de control de `ev`. Véase también `evflag`.
**evfun** — Hace que *a_i* sea reconocida por `ev`, de manera que la función
      nombrada por *a_i* se aplique cuando *a_i* aparezca como argumento
      de control de `ev`. Véase también `evfun`.
**feature** — Hace que Maxima considere a *a_i* como el nombre de una propiedad.
      Otros átomos podrán ser declarados entonces como poseedores de
      la propiedad *a_i*.
**increasing, decreasing** — Hace que Maxima reconozca a *a_i* como una función creciente o decreciente.
**integer, noninteger** — Hace que Maxima reconozca a *a_i* como una variable entera o no entera.
**integervalued** — Hace que Maxima reconozca a *a_i* como una función de valor entero.
**lassociative, rassociative** — Hace que Maxima reconozca a *a_i* como una función asociativa por la derecha o
      por la izquierda.
**linear** — Equivale a declarar *a_i* conjuntamente como `outative` y `additive`.
**mainvar** — Hace que Maxima considere a *a_i* como una "variable principal",
      dándole prioridad frente a cualesquiera otras constantes o
      variables en la ordenación canónica de expresiones de Maxima,
      tal como determina `ordergreatp`.
**multiplicative** — Hace que Maxima simplifique las expresiones *a_i*
      haciendo uso de la sustitución 
      `a_i(x * y * z * ...)` `-->` `a_i(x) * a_i(y) * a_i(z) * ...`.
      Tal sustitución se aplica únicamente al primer argumento.
**nary** — Hace que Maxima reconozca a *a_i* como una función n-aria. 
       La declaración `nary` no es equivalente a la función `nary`.
      El único efecto de `declare(foo, nary)` consiste en hacer que
      el simplificador de Maxima reduzca expresiones anidadas; por ejemplo, 
      para transformar `foo(x, foo(y, z))` a `foo(x, y, z)`.
**nonarray** — Indica que Maxima no debe considerar *a_i* como un array. Esta declaración
      evita la evaluación múltiple de variables subindicadas.
**nonscalar** — Hace que Maxima considere a *a_i* como una variable no escalar.
      Se aplica comúnmente para declarar una variable como un vector simbólico
      o una matriz simbólica.
**noun** — Hace que Maxima considere a *a_i* como un nombre. El efecto
      que se obtiene es que se reemplazan todas las expresiones *a_i*
      por `'a_i` o `nounify (a_i)`,
      dependiendo del contexto.
**outative** — Hace que Maxima simplifique las expresiones *a_i*
      extrayendo los factores constantes del primer argumento. 
       Cuando *a_i* tenga un único argumento, un factor se considerará constante
      si es una constante literal o declarada. 
       Cuando *a_i* tenga dos o más argumentos, un factor se considerará constante
      si el segundo argumento es un símbolo y el factor no contiene al
      segundo argumento.
**posfun** — Hace que Maxima reconozca a *a_i* como una función positiva.
**rational, irrational** — Hace que Maxima reconozca a *a_i* como una variable real racional o irracional.
**real, imaginary, complex** — Hace que Maxima reconozca a *a_i* como una variable real, imaginaria o compleja.
**scalar** — Hace que Maxima considere a *a_i* como una variable escalar.


Ejemplos sobre el uso de estas propiedades están disponibles en la 
documentación correspondiente a cada propiedad por separado.

<!-- category: Other -->
<!-- keywords: decreasing, increasing -->
<!-- signatures: increasing -->
### Variable: decreasing

Las instrucciones `declare(f, decreasing)` y
`declare(f, increasing` le indican a Maxima que reconozca la función
*f* como una función decreciente o creciente.


Véase también `declare` para más propiedades.


Ejemplo:



```maxima
(%i1) assume(a > b);
(%o1)                        [a > b]
(%i2) is(f(a) > f(b));
(%o2)                        unknown
(%i3) declare(f, increasing);
(%o3)                         done
(%i4) is(f(a) > f(b));
(%o4)                         true
```

<!-- category: Other -->
<!-- keywords: equal -->
<!-- signatures: equal(a, b) -->
### Function: equal (a, b)

Representa la equivalencia, esto es, la igualdad de los valores.


Por sí misma, `equal` no evalúa ni simplifica.
La función `is` intenta evaluar `equal` a un resultado
booleano. La instrucción `is(equal(a, b))`
devuelve `true` (o `false`) si y sólo si
*a* y *b* son iguales (o no iguales) para todos los posibles
valores de sus variables, tal como lo determina `ratsimp(a - b)`;
si `ratsimp` devuelve 0, las dos expresiones se consideran
equivalentes. Dos expresiones pueden ser equivalentes  sin
ser sintácticamente iguales (es decir, idénticas).


Si `is` no consigue reducir `equal` a `true` o `false`,
el resultado está controlado por la variable global `prederror`.
Si `prederror` vale `true`, `is` emite un mensaje
de error; en caso contrario, `is` devuelve `unknown`.


Además de `is`, otros operadores evalúan `equal` y `notequal`
a  `true` o `false`; a saber, `if`, `and`, `or` y `not`.


La negación de `equal` es `notequal`.


Ejemplos:


Por sí misma, `equal` no evalúa ni simplifica.








```maxima
(%i1) equal (x^2 - 1, (x + 1) * (x - 1));
                        2
(%o1)            equal(x  - 1, (x - 1) (x + 1))
(%i2) equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) equal (x, y);
(%o3)                      equal(x, y)
```


La función `is` intenta evaluar `equal` a un resultado
booleano. La instrucción `is(equal(a, b))`
devuelve `true` si `ratsimp(a - b)`
devuelve 0. Dos expresiones pueden ser equivalentes  sin
ser sintácticamente iguales (es decir, idénticas).














```maxima
(%i1) ratsimp (x^2 - 1 - (x + 1) * (x - 1));
(%o1)                           0
(%i2) is (equal (x^2 - 1, (x + 1) * (x - 1)));
(%o2)                         true
(%i3) is (x^2 - 1 = (x + 1) * (x - 1));
(%o3)                         false
(%i4) ratsimp (x - (x + 1));
(%o4)                          - 1
(%i5) is (equal (x, x + 1));
(%o5)                         false
(%i6) is (x = x + 1);
(%o6)                         false
(%i7) ratsimp (x - y);
(%o7)                         x - y
(%i8) is (equal (x, y));
(%o8)                        unknown
(%i9) is (x = y);
(%o9)                         false
```


Si `is` no consigue reducir `equal` a `true` o `false`,
el resultado está controlado por la variable global `prederror`.











```maxima
(%i1) [aa : x^2 + 2*x + 1, bb : x^2 - 2*x - 1];
                    2             2
(%o1)             [x  + 2 x + 1, x  - 2 x - 1]
(%i2) ratsimp (aa - bb);
(%o2)                        4 x + 2
(%i3) prederror : true;
(%o3)                         true
(%i4) is (equal (aa, bb));
Maxima was unable to evaluate the predicate:
       2             2
equal(x  + 2 x + 1, x  - 2 x - 1)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) prederror : false;
(%o5)                         false
(%i6) is (equal (aa, bb));
(%o6)                        unknown
```


Otros operadores evalúan `equal` y `notequal`
a  `true` o `false`.









```maxima
(%i1) if equal (y, y - 1) then FOO else BAR;
(%o1)                          BAR
(%i2) eq_1 : equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) eq_2 : equal (y^2 + 2*y + 1, (y + 1)^2);
                         2                   2
(%o3)             equal(y  + 2 y + 1, (y + 1) )
(%i4) [eq_1 and eq_2, eq_1 or eq_2, not eq_1];
(%o4)                  [false, true, true]
```


Debido a que `not expr`
obliga a la evaluación previa de *expr*, 
`not equal(a, b)` equivale a `is(notequal(a, b))`.







```maxima
(%i1) [notequal (2*z, 2*z - 1), not equal (2*z, 2*z - 1)];
(%o1)            [notequal(2 z, 2 z - 1), true]
(%i2) is (notequal (2*z, 2*z - 1));
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: even, odd -->
<!-- signatures: odd -->
### Variable: even

`declare(a, even)` y `declare(a, odd)` le indican a Maxima
que reconozca el símbolo *a* como entero par o impar.  Las
propiedades `even` y `odd` no son reconocidas por las funciones 
`evenp`, `oddp` y `integerp`.


Véanse también `declare` y `askinteger`.


Ejemplo:



```maxima
(%i1) declare(n, even);
(%o1)                         done
(%i2) askinteger(n, even);
(%o2)                          yes
(%i3) askinteger(n);
(%o3)                          yes
(%i4) evenp(n);
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: facts -->
<!-- signatures: facts(item), facts() -->
### Function: facts (item)

Si *item* es el nombre de un contexto,
`facts (item)` devuelve una lista
con los hechos asociados al contexto especificado.


Si *item* no es el nombre de un contexto,
`facts (item)` devuelve una lista con los hechos conocidos acerca de *item* en el contexto actual. Los hechos que estén activos en contextos diferentes no aparecen en la lista.


La llamada `facts ()`, sin argumentos, muestra el contexto actual.

<!-- category: Other -->
<!-- keywords: feature -->
<!-- signatures: feature -->
### Variable: feature

Maxima interpreta dos tipos diferentes de propiedades, del sistema y las que
se aplican a expresiones matemáticas. Véase `status` para obtener
información sobre propiedades del sistema, así como
`features` y `featurep` para propiedades de las expresiones matemáticas.


`feature` no es el nombre de ninguna función o variable.

<!-- category: Other -->
<!-- keywords: featurep -->
<!-- signatures: featurep(a, f) -->
### Function: featurep (a, f)

Intenta determinar si el objeto *a* tiene la propiedad *f* en base a los
hechos almacenados en la base de datos. En caso afirmativo, devuelve `true`,
o `false` en caso contrario.


Nótese que `featurep` devuelve `false` cuando no se puedan verificar ni
*f* ni su negación.


`featurep` evalúa su argumento.


Véanse también `declare` y `features`.


Ejemplos:



```maxima
(%i1) declare (j, even)$
(%i2) featurep (j, integer);
(%o2)                           true
```

<!-- category: Other -->
<!-- keywords: features -->
<!-- signatures: features -->
### Variable: features

Maxima reconoce ciertas propiedades matemáticas sobre funciones y variables.


La llamada `declare (x, foo)` asocia la propiedad *foo* a la función o variable *x*.


La llamada `declare (foo, feature)` declara una nueva propiedad *foo*. 
Por ejemplo, `declare ([rojo, verde, azul], feature)` declara tres nuevas propiedades, 
`rojo`, `verde` y `azul`.


El predicado `featurep (x, foo)`
devuelve `true` si *x* goza de la propiedad *foo*, y `false` en caso contrario.


La lista `features` contiene las propiedades que reconoce Maxima; a saber,



   integer        noninteger      even
   odd            rational        irrational
   real           imaginary       complex
   analytic       increasing      decreasing
   oddfun         evenfun         posfun
   commutative    lassociative    rassociative
   symmetric      antisymmetric


junto con las definidas por el usuario.


La lista `features` sólo contiene propiedades matemáticas. 
Hay otra lista con propiedades no matemáticas; Véase `status`.


Ejemplo:








```maxima
(%i1) declare (FOO, feature);
(%o1)                         done
(%i2) declare (x, FOO);
(%o2)                         done
(%i3) featurep (x, FOO);
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: forget -->
<!-- signatures: forget(pred_1, ..., pred_n), forget(L) -->
### Function: forget (pred_1, ..., pred_n)

Borra los predicados establecidos por `assume`. Los predicados pueden ser expresiones equivalentes, pero no necesariamente idénticas, a las establecidas por `assume`.


La llamada `forget (L)`, siendo *L* una lista de predicados, borra todos los predicados contenidos en ella.

<!-- category: Other -->
<!-- keywords: get -->
<!-- signatures: get(a, i) -->
### Function: get (a, i)

Recupera la propiedad de usuario indicada por *i* asociada al átomo *a* 
o devuelve `false` si *a* no tiene la propiedad *i*.


La función `get` evalúa sus argumentos.


Véanse también `put` y `qput`.


















```maxima
(%i1) put (%e, 'transcendental, 'type);
(%o1)                    transcendental
(%i2) put (%pi, 'transcendental, 'type)$
(%i3) put (%i, 'algebraic, 'type)$
(%i4) typeof (expr) := block ([q],
        if numberp (expr)
        then return ('algebraic),
        if not atom (expr)
        then return (maplist ('typeof, expr)),
        q: get (expr, 'type),
        if q=false
        then errcatch (error(expr,"is not numeric.")) else q)$
(%i5) typeof (2*%e + x*%pi);
x is not numeric.
(%o5)  [[transcendental, []], [algebraic, transcendental]]
(%i6) typeof (2*%e + %pi);
(%o6)     [transcendental, [algebraic, transcendental]]
```

<!-- category: Other -->
<!-- keywords: integer, noninteger -->
<!-- signatures: noninteger -->
### Variable: integer

`declare(a, integer)` o `declare(a, noninteger)` indica a
Maxima que reconozca *a* como una variable entera o no entera.


Véase también `declare`.


Ejemplo:



```maxima
(%i1) declare(n, integer, x, noninteger);
(%o1)                         done
(%i2) askinteger(n);
(%o2)                          yes
(%i3) askinteger(x);
(%o3)                          no
```

<!-- category: Other -->
<!-- keywords: integervalued -->
<!-- signatures: integervalued -->
### Variable: integervalued

`declare(f, integervalued)` indica a MAxima que reconozca *f* como
una función que toma valores enteros.


Véase también `declare`.


Ejemplo:



```maxima
(%i1) exp(%i)^f(x);
                              %i f(x)
(%o1)                      (%e  )
(%i2) declare(f, integervalued);
(%o2)                         done
(%i3) exp(%i)^f(x);
                              %i f(x)
(%o3)                       %e
```

<!-- category: Other -->
<!-- keywords: is -->
<!-- signatures: is(expr) -->
### Function: is (expr)

Intenta determinar si el predicado *expr*  se puede deducir de los hechos almacenados en la base de datos gestionada por `assume`.


Si el predicado se reduce a `true` o `false`,
`is` devuelve `true` o `false`, respectivamente.
En otro caso, el valor devuelto está controlado por la variable global `prederror`.
Si `prederror` vale `true`, `is` emite un mensaje de error;
en caso contrario, `is` devuelve `unknown`.


La instrucción `ev(expr, pred)`
(que puede escribirse como `expr, pred` en el
modo interactivo) equivale a `is(expr)`.


Véanse también `assume`, `facts` y `maybe`.


Ejemplos:


`is` evalúa los predicados,







```maxima
(%i1) %pi > %e;
(%o1)                       %pi > %e
(%i2) is (%pi > %e);
(%o2)                         true
```


`is` intenta evaluar predicados a partir 
del conocimiento almacenado en la base de datos de `assume`.










```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) assume (b > c);
(%o2)                        [b > c]
(%i3) is (a < b);
(%o3)                         false
(%i4) is (a > c);
(%o4)                         true
(%i5) is (equal (a, c));
(%o5)                         false
```


Si `is` no puede evaluar el valor lógico del predicado 
a partir de la base de datos gestionada por `assume`,
la variable global  `prederror` controla el comportamiento de `is`.










```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) prederror: true$
(%i3) is (a > 0);
Maxima was unable to evaluate the predicate:
a > 0
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) prederror: false$
(%i5) is (a > 0);
(%o5)                        unknown
```

<!-- category: Other -->
<!-- keywords: killcontext -->
<!-- signatures: killcontext(contexto_1, ..., contexto_n) -->
### Function: killcontext (contexto_1, ..., contexto_n)

Elimina los contextos *contexto_1*, ..., *contexto_n*.


Si alguno de estos contextos es el actual, el nuevo contexto activo será el primer subcontexto disponible del actual que no haya sido eliminado. Si el primer contexto no eliminado disponible es `global` entonces `initial` será usado en su lugar.  Si el contexto `initial` es eliminado, se creará un nuevo contexto `initial` completamente vacío.


La función `killcontext` no elimina un contexto actualmente activo si es un subcontexto del contexto actual, o si se hace uso de la función `activate`.


La función `killcontext` evalúa sus argumentos y devuelve `done`.

<!-- category: Other -->
<!-- keywords: maybe -->
<!-- signatures: maybe(expr) -->
### Function: maybe (expr)

Intenta determinar si el predicado *expr*  se puede deducir de los hechos almacenados en la base de datos gestionada por `assume`.


Si el predicado se reduce a `true` o `false`,
`maybe` devuelve `true` o `false`, respectivamente.
En otro caso, `maybe` devuelve `unknown`.


La función `maybe` es funcionalmente equivalente a `is` con `prederror: false`,
pero el resultado se calcula sin asignar valor alguno a `prederror`.


Véanse también `assume`, `facts` y `is`.


Ejemplos:








```maxima
(%i1) maybe (x > 0);
(%o1)                        unknown
(%i2) assume (x > 1);
(%o2)                        [x > 1]
(%i3) maybe (x > 0);
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: newcontext -->
<!-- signatures: newcontext(nombre) -->
### Function: newcontext (nombre)

Crea un nuevo contexto vacío *nombre*, el cual tiene a `global` como su único subcontexto. El recién creado contexto pasa a ser el contexto actualmente activo.


La función `newcontext` evalúa sus argumentos y devuelve *nombre*.

<!-- category: Other -->
<!-- keywords: nonarray -->
<!-- signatures: nonarray -->
### Function: nonarray

La instrucción `declare(a, nonarray)` le indica a Maxima que
no considere *a* como un array. Esta declaración evita la 
evaluación múltiple de *a*, si ésta es una variable subindicada.


Véase también `declare`.


Ejemplo:









```maxima
(%i1) a:'b$ b:'c$ c:'d$

(%i4) a[x];
(%o4)                          d
                                x
(%i5) declare(a, nonarray);
(%o5)                         done
(%i6) a[x];
(%o6)                          a
                                x
```

<!-- category: Other -->
<!-- keywords: nonscalar -->
<!-- signatures: nonscalar -->
### Variable: nonscalar

Hace que los átomos se comporten como hace una lista o matriz 
con respecto del operador `.` del la multiplicación no conmutativa.


Véase también `declare`.

<!-- category: Other -->
<!-- keywords: nonscalarp -->
<!-- signatures: nonscalarp(expr) -->
### Function: nonscalarp (expr)

Devuelve `true` si *expr* no es escalar, es decir, 
si contiene átomos declarados como no escalares, listas o matrices.

<!-- category: Other -->
<!-- keywords: notequal -->
<!-- signatures: notequal(a, b) -->
### Function: notequal (a, b)

Representa la negación de `equal (a, b)`.


Ejemplos:















```maxima
(%i1) equal (a, b);
(%o1)                      equal(a, b)
(%i2) maybe (equal (a, b));
(%o2)                        unknown
(%i3) notequal (a, b);
(%o3)                    notequal(a, b)
(%i4) not equal (a, b);
(%o4)                    notequal(a, b)
(%i5) maybe (notequal (a, b));
(%o5)                        unknown
(%i6) assume (a > b);
(%o6)                        [a > b]
(%i7) equal (a, b);
(%o7)                      equal(a, b)
(%i8) maybe (equal (a, b));
(%o8)                         false
(%i9) notequal (a, b);
(%o9)                    notequal(a, b)
(%i10) maybe (notequal (a, b));
(%o10)                        true
```

<!-- category: Other -->
<!-- keywords: posfun -->
<!-- signatures: posfun -->
### Variable: posfun

La instrucción `declare (f, posfun)` declara a `f` como 
función positiva, de forma que 
`is (f(x) > 0)` devolverá `true`.


Véase también `declare`.

<!-- category: Other -->
<!-- keywords: printprops -->
<!-- signatures: printprops(a, i), printprops([a_1, ..., a_n], i), printprops(all, i) -->
### Function: printprops (a, i)

Muestra la propiedad con el indicador *i* asociado 
con el átomo *a*. *a* puede ser también una lista de
átomos o el átomo `all` en cuyo caso todos los átomos a los cuales se les haya dado esa propiedad serán usados. 
Por ejemplo, `printprops ([f, g], atvalue)`. `printprops` es 
para propiedades que no pueden ser mostradas de otra manera, i.e. para
`atvalue`, `atomgrad`, `gradef`, y `matchdeclare`.

<!-- category: Other -->
<!-- keywords: properties -->
<!-- signatures: properties(a) -->
### Function: properties (a)

Devuelve una lista con los nombres de todas las propiedades asociadas
al tomo *a*.

<!-- category: Other -->
<!-- keywords: props -->
<!-- signatures: props -->
### Variable: props

Valor por defecto: `[]`


`props` son tomos que tienen asociadas otras propiedades además de las
explícitamente mencionadas en `infolists`, tales como las
especificadas por `atvalue`, `matchdeclare` y la función 
`declare`.

<!-- category: Other -->
<!-- keywords: propvars -->
<!-- signatures: propvars(prop) -->
### Function: propvars (prop)

Devuelve la lista con los átomos de la lista `props` que tienen
la propiedad indicada por *prop*. Así, `propvars (atvalue)` 
devuelve la lista con los átomos a los que se les ha asociado valores con
`atvalue`.

<!-- category: Other -->
<!-- keywords: put -->
<!-- signatures: put(átomo, valor, indicador) -->
### Function: put (átomo, valor, indicador)

Asigna el *valor* a la propiedad  (especificada por *indicador*) de *átomo*;
*indicador* puede ser el nombre de cualquier propiedad y no solamente de aquellas definidas por el sistema.


`rem` deshace la asignación realizada por `put`.


La función `put` evalúa sus argumentos y devuelve *valor*.


Ejemplos:



```maxima
(%i1) put (foo, (a+b)^5, expr);
                                   5
(%o1)                       (b + a)
(%i2) put (foo, "Hello", str);
(%o2)                         Hello
(%i3) properties (foo);
(%o3)            [[user properties, str, expr]]
(%i4) get (foo, expr);
                                   5
(%o4)                       (b + a)
(%i5) get (foo, str);
(%o5)                         Hello
```

<!-- category: Other -->
<!-- keywords: qput -->
<!-- signatures: qput(átomo, valor, indicador) -->
### Function: qput (átomo, valor, indicador)

Asigna *valor* a la propiedad de *átomo* que especifique *indicador*.
Actúa del mismo modeo que `put`, excepto que sus argumentos no son evaluados.


Véase también `get`.


Ejemplo:



```maxima
(%i1) foo: aa$ 
(%i2) bar: bb$
(%i3) baz: cc$
(%i4) put (foo, bar, baz);
(%o4)                          bb
(%i5) properties (aa);
(%o5)                [[user properties, cc]]
(%i6) get (aa, cc);
(%o6)                          bb
(%i7) qput (foo, bar, baz);
(%o7)                          bar
(%i8) properties (foo);
(%o8)            [value, [user properties, baz]]
(%i9) get ('foo, 'baz);
(%o9)                          bar
```

<!-- category: Other -->
<!-- keywords: rational, irrational -->
<!-- signatures: irrational -->
### Variable: rational

`declare(a, rational)` o `declare(a, irrational)` indica a
Maxima que reconozca *a* como una variable real racional o irracional.


Véase también `declare`.

<!-- category: Other -->
<!-- keywords: real, imaginary, complex -->
<!-- signatures: imaginary, complex -->
### Variable: real

`declare(a, real)`, `declare(a, imaginary)` o
`declare(a, complex)` indican a Maxima que reconozca *a* como variable real,
imaginaria puro o compleja, respectivamente.


Véase también `declare`.

<!-- category: Other -->
<!-- keywords: rem -->
<!-- signatures: rem(átomo, indicador) -->
### Function: rem (átomo, indicador)

Elimina del *átomo* la propiedad indicada por *indicador*.
`rem` deshace la asignación realizada por `put`.


`rem` devuelve `done` si *átomo* tenía la 
propiedad *indicador* cuando `rem` fue invocado, devolviendo
`false` si carecía tal propiedad.

<!-- category: Other -->
<!-- keywords: remove -->
<!-- signatures: remove(a_1, p_1, ..., a_n, p_n), remove([a_1, ..., a_m], [p_1, ..., p_n], ...), remove("a", operator), remove(a, transfun), remove(all, p) -->
### Function: remove (a_1, p_1, ..., a_n, p_n)

Elimina propiedades asociadas con átomos.


La llamada `remove (a_1, p_1, ..., a_n, p_n)`
elimina la propiedad `p_k` del átomo `a_k`.


La llamada `remove ([a_1, ..., a_m], [p_1, ..., p_n], ...)`
elimina las propiedades `p_1, ..., p_n` de los átomos *a_1*, ..., *a_m*. Puede tener más de un par de listas.


La llamada `remove (all, p)` elimina la propiedad *p* de todos los átomos que la tengan.


Las propiedades eliminadas pueden ser de las que define el sistema, como 
`function`, `macro` o `mode_declare`; `remove` no elimina
las propiedades definidas por `put`.


La llamada `remove ("a", operator)` o su equivalente `remove ("a", op)` elimina de  *a* las propiedades de operador declaradas por `prefix`, `infix`, `nary`, `postfix`, `matchfix` o `nofix`. Nótese que el nombre del operador debe escribirse como cadena precedida de apóstrofo.


La función `remove` devuelve siempre `done` independientemente que haya algún átomo con la propiedad especificada.


La función `remove` no evalúa sus argumentos.

<!-- category: Other -->
<!-- keywords: scalar -->
<!-- signatures: scalar -->
### Variable: scalar

`declare(a, scalar)` indica a Maxima que considere a *a* como
una variable escalar.


Véase también `declare`.

<!-- category: Other -->
<!-- keywords: scalarp -->
<!-- signatures: scalarp(expr) -->
### Function: scalarp (expr)

Devuelve `true` si *expr* es un número, constante  o variable 
declarada como `scalar` con `declare`, o compuesta completamente de tales 
números, constantes o variables, pero que no contengan matrices ni listas.

<!-- category: Other -->
<!-- keywords: sign -->
<!-- signatures: sign(expr) -->
### Function: sign (expr)

Intenta determinar el signo de *expr* en base a los hechos almacenados en la base de datos. Devuelve una de las siguientes respuestas: `pos` (positivo), `neg` (negativo), `zero` (cero), `pz`
(positivo o cero), `nz` (negativo o cero), `pn` (positivo o negativo),
o `pnz` (positivo, negativo o cero, lo que significa que el signo es desconocido).

<!-- category: Other -->
<!-- keywords: supcontext -->
<!-- signatures: supcontext(nombre, contexto), supcontext(nombre) -->
### Function: supcontext (nombre, contexto)

Crea un nuevo contexto *nombre*, que tiene a *contexto* como subcontexto. El argumento
*contexto* debe existir ya.


Si no se especifica *context*, se tomará como tal el actual.

<!-- category: Other -->
<!-- keywords: unknown -->
<!-- signatures: unknown(expr) -->
### Function: unknown (expr)

Devuelve `true` si y sólo si *expr* contiene un operador o función no reconocido por el simplificador de Maxima.

<!-- category: Other -->
<!-- keywords: zeroequiv -->
<!-- signatures: zeroequiv(expr, v) -->
### Function: zeroequiv (expr, v)

Analiza si la expresión *expr* de variable *v* equivale a cero, devolviendo `true`, `false` o
`dontknow`.


La función `zeroequiv` tiene estas restricciones:


1. No utilizar funciones que Maxima no sepa derivar y evaluar.
2. Si la expresión tiene polos en la recta real, pueden aparecer errores en el resultado, aunque es poco probable.
3. Si la expresión contiene funciones que no son soluciones de ecuaciones diferenciales ordinarias de primer orden (como las funciones de Bessel) pueden presentarse resultados incorrectos.
4. El algoritmo utiliza evaluaciones en puntos aleatoriamente seleccionados. Esto conlleva un riesgo,aunque el algoritmo intenta minimizar el error.


Por ejemplo, `zeroequiv (sin(2*x) - 2*sin(x)*cos(x), x)` devuelve
`true` y `zeroequiv (%e^x + x, x)` devuelve `false`.
Por otro lado `zeroequiv (log(a*b) - log(a) - log(b), a)` devuelve `dontknow` debido a la presencia del parámetro `b`.

