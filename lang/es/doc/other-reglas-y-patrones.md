## Reglas y patrones

<!-- category: Other -->
<!-- keywords: apply1 -->
<!-- signatures: apply1(expr, regla_1, ..., regla_n) -->
### Function: apply1 (expr, regla_1, ..., regla_n)

Aplica de forma repetida la *regla_1* a *expr* hasta que falla, a continuación aplica repetidamente la misma regla a todas las subexpresiones de *expr*, de izquierda a derecha, hasta que la *regla_1* haya fallado en todas las subexpresiones. Llámese *expr_2* al resultado de transformar *expr* de esta forma. Entonces la *regla_2* se aplica de la misma manera comenzando en el nivel superior de *expr_2*. Cuando la *regla_n* falla en la última expresión, se devuelve el resultado.


`maxapplydepth` es el nivel de las subexpresiones más internas procesadas por `apply1` y `apply2`.


Véase también `applyb1`, `apply2` y `let`.

<!-- category: Other -->
<!-- keywords: apply2 -->
<!-- signatures: apply2(expr, regla_1, ..., regla_n) -->
### Function: apply2 (expr, regla_1, ..., regla_n)

Si la *regla_1* falla en una subexpresión dada, entonces se aplica la *regla_2* repetidamente, etc. Sólo si todas las reglas fallan en una subexpresión serán aplicadas todas las reglas de forma repetida a la siguiente subexpresión. Si alguna de las reglas tiene éxito entonces la misma subexpresión es reprocesada, comenzando por la primera regla.


`maxapplydepth` es el nivel de las subexpresiones más internas procesadas por `apply1` y `apply2`.


Véase también `applyb1` y `let`.

<!-- category: Other -->
<!-- keywords: applyb1 -->
<!-- signatures: applyb1(expr, regla_1, ..., regla_n) -->
### Function: applyb1 (expr, regla_1, ..., regla_n)

Aplica la *regla_1* reiteradamente hasta la subexpresión más interna de *expr* hasta que falle, a continuación pasa a aplicar la misma regla en un nivel superior (esto es, en subexpresiones más grandes), hasta que la *regla_1* falle en la expresión de nivel más alto. Después se aplica la *regla_2* de la misma manera al resultado obtenido de *regla_1*. Tras la aplicación de la *regla_n* a la expresión de mayor nivel, se devuelve el resultado.


La función `applyb1` es similar a `apply1` pero opera de abajo-arriba, en lugar de arriba-abajo.


`maxapplyheight` es la máxima altura a la que llega `applyb1` antes de terminar su cometido.


Véase también `apply1`, `apply2` y `let`.

<!-- category: Other -->
<!-- keywords: clear_rules -->
<!-- signatures: clear_rules() -->
### Function: clear_rules ()

Ejecuta `kill (rules)` y después inicializa el siguiente número de regla a 1 para la adición `+`, multiplicación `*` y exponenciación `^`.

<!-- category: Other -->
<!-- keywords: current_let_rule_package -->
<!-- signatures: current_let_rule_package -->
### Variable: current_let_rule_package

Valor por defecto: `default_let_rule_package`


La variable `current_let_rule_package` es el nombre del paquete de reglas que están utilizando las funciones del paquete `let` (`letsimp`, etc.), a menos que se especifique otro paquete de reglas. A esta variable se le puede asignar el nombre de cualquier paquete de reglas definido por medio de la instrucción `let`.


Si se hace la llamada `letsimp (expr, rule_pkg_name)`, el paquete de reglas `rule_pkg_name` será utilizado únicamente para esa llamada y el valor de `current_let_rule_package` no cambia.

<!-- category: Other -->
<!-- keywords: default_let_rule_package -->
<!-- signatures: default_let_rule_package -->
### Variable: default_let_rule_package

Valor por defecto: `default_let_rule_package`



La variable `default_let_rule_package` es el nombre del paquete de reglas utilizado cuando el usuario no especifica otro explícitamente con `let` o cambiando el valor de `current_let_rule_package`.

<!-- category: Other -->
<!-- keywords: defmatch -->
<!-- signatures: defmatch(nombre_prog, patrón, x_1, ..., x_n), defmatch(progname, pattern) -->
### Function: defmatch (nombre_prog, patrón, x_1, ..., x_n)

Define una función `nombre_prog(expr, x_1, ..., x_n)` que analiza si *expr* coincide con el *patrón*.


El argumento *patrón* es una expresión que contiene los
argumentos de patrón *x_1*, ..., *x_n* y algunas variables de patrón.
Los argumentos de patrón se dan de forma explícita
como argumentos a `defmatch`, mientras que las variables de patrón
se declaran mediante la función `matchdeclare`.
Cualquier variable no declarada bien como variable patrón en `matchdeclare`,
bien como argumento patrón en `defmatch` se hace coincidir con ella
misma.


El primer argumento de la función definida *nombre_prog* es una expresión
a ser comparada con el patrón y los demás argumentos son los argumentos 
que se corresponden con las variables ficticias *x_1*, ..., *x_n* del patrón.


Si el resultado de la comparación es positivo, *nombre_prog* devuelve
una lista de ecuaciones cuyos miembros izquierdos son los argumentos y variables de
patrón, y cuyos miembros derechos son las subexpresiones en las que se han 
producido las coincidencias con patrones. A las variables de patrón, no a los
argumentos, se les asignan las subexpresiones con las que coinciden. Si la 
comparación falla, *nombre_prog* devuelve `false`.  


Un patrón literal, es decir, que no contiene ni argumentos ni variables de patrón,
devuelve `true` en caso de coincidencia.




A literal pattern
(that is, a pattern which contains neither pattern arguments nor pattern variables)
returns `true` if the match succeeds.


Véase también `matchdeclare`, `defrule`, `tellsimp` y `tellsimpafter`.


Ejemplos:


Define una función `linearp(expr, x)` que comprueba si
`expr` es de la forma `a*x + b`, donde
ni `a` ni `b` contienen a `x` y `a` es no nulo.
La función definida reconoce expresiones lineales respecto de
cualquier variable, pues el argumento de patrón `x` es
pasado a `defmatch`.












```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)),
                    b, freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b, x);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2, z);
                         2
(%o3)              [b = y , a = y + 4, x = z]
(%i4) a;
(%o4)                         y + 4
(%i5) b;
                                2
(%o5)                          y
(%i6) x;
(%o6)                           x
```


Define una función `linearp(expr)` que comprueba si
`expr` es de la forma `a*x + b`, donde
ni `a` ni `b` contienen a `x` y `a` es no nulo.
La función definida sólo reconoce expresiones lineales
únicamente respecto de `x`, pues no se le pasa a `defmatch`
nigún argumento de patrón










```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)),
                    b, freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2);
(%o3)                         false
(%i4) linearp (3*x + (y + 1)*x + y^2);
                             2
(%o4)                  [b = y , a = y + 4]
```


Define una función `checklimits(expr)` que comprueba si
`expr` es una integral definida.














```maxima
(%i1) matchdeclare ([a, f], true);
(%o1)                         done
(%i2) constinterval (l, h) := constantp (h - l);
(%o2)        constinterval(l, h) := constantp(h - l)
(%i3) matchdeclare (b, constinterval (a));
(%o3)                         done
(%i4) matchdeclare (x, atom);
(%o4)                         done
(%i5) simp : false;
(%o5)                         false
(%i6) defmatch (checklimits, 'integrate (f, x, a, b));
(%o6)                      checklimits
(%i7) simp : true;
(%o7)                         true
(%i8) 'integrate (sin(t), t, %pi + x, 2*%pi + x);
                       x + 2 %pi
                      /
                      [
(%o8)                 I          sin(t) dt
                      ]
                      /
                       x + %pi
(%i9) checklimits (%);
(%o9)    [b = x + 2 %pi, a = x + %pi, x = t, f = sin(t)]
```

<!-- category: Other -->
<!-- keywords: defrule -->
<!-- signatures: defrule(nombre_regla, patrón, reemplazamiento) -->
### Function: defrule (nombre_regla, patrón, reemplazamiento)

Define y da nombre a una regla de reemplazamiento para el patrón dado. Si la regla *nombre_regla* es aplicada a una expresión (por `apply1`, `applyb1` o `apply2`), cada subexpresión que coincida con el patrón será reemplazada por el contenido de *reemplazamiento*.


Las propias reglas pueden ser tratadas como funciones que transforman una expresión mediante una operación consistente en la búsqueda de una coincidencia y posterior aplicación de un reemplazamiento. Si la comparación falla, la función que implementa la regla devuelve `false`.

<!-- category: Other -->
<!-- keywords: disprule -->
<!-- signatures: disprule(nombre_regla_1, ..., nombre_regla_n), disprule(all) -->
### Function: disprule (nombre_regla_1, ..., nombre_regla_n)

Muestra las reglas de *nombre_regla_1*, ..., *nombre_regla_n*, tal como son devueltas por `defrule`, `tellsimp` o `tellsimpafter`, o un patrón definido por `defmatch`.
Cada regla se muestra con una etiqueta de expresión intermedia (`%t`).


La llamada `disprule (all)` muestra todas las reglas.


La función `disprule` no evalúa sus argumentos y devuelve la lista de etiquetas de expresiones intermedias correspondientes a las reglas mostradas.


Véase también `letrules`, que muestra las reglas definidas por `let`.


Ejemplos:










```maxima
(%i1) tellsimpafter (foo (x, y), bar (x) + baz (y));
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (x + y, special_add (x, y));
(%o2)                   [+rule1, simplus]
(%i3) defmatch (quux, mumble (x));
(%o3)                         quux
(%i4) disprule (foorule1, "+rule1", quux);
(%t4)        foorule1 : foo(x, y) -> baz(y) + bar(x)

(%t5)          +rule1 : y + x -> special_add(x, y)

(%t6)                quux : mumble(x) -> []

(%o6)                    [%t4, %t5, %t6]
(%i6) ''%;
(%o6) [foorule1 : foo(x, y) -> baz(y) + bar(x), 
     +rule1 : y + x -> special_add(x, y), quux : mumble(x) -> []]
```

<!-- category: Other -->
<!-- keywords: let -->
<!-- signatures: let(prod, repl, predname, arg_1, ..., arg_n), let([prod, repl, predname, arg_1, ..., arg_n], nombre_paquete) -->
### Function: let (prod, repl, predname, arg_1, ..., arg_n)

Define una regla de sustitución para `letsimp` tal que *prod* es sustituido por *repl*, donde *prod* es un producto de potencias positivas o negativas de los términos siguientes:



- *
Átomos que `letsimp` buscará a menos que antes de llamar a `letsimp` se utilice la función `matchdeclare` para asociar un predicado con el átomo. En este caso `letsimp` hará coincidir el átomo con cualquier término del producto que satisfaga el predicado.
- *
Expresiones básicas como `sin(x)`, `n!`, `f(x,y)`, etc.  Como en el caso anterior, `letsimp` buscará coincidencias exactas, a menos que se utilice `matchdeclare` para asociar un predicado con el argumento de la expresión básica (`sin(x)`, `n!`, `f(x,y)`, ...).


Si se incluye un predicado en la función `let` seguido de una lista de argumentos, una coincidencia aceptable  (es decir, una que fuese aceptada si se hubiese omitido el predicado) se aceptará sólo si `predname (arg_1', ..., arg_n')` vale `true`, donde *arg_i’* es el valor coincidente con *arg_i*.  El argumento *arg_i* puede ser el nombre de cualquier átomo o el argumento de cualquier expresión básica que aparezca en *prod*. 
*repl* puede ser cualquier expresión racional. 
Si cualquiera de los átomos o argumentos de *prod* aparece en *repl* se llevan a cabo las sustituciones correspondientes.


La variable global `letrat` controla la simplificación de los cocientes por `letsimp`. Cuando `letrat` vale  `false`, `letsimp` simplifica separadamente el numerador y denominador de  *expr* y no simplifica el cociente. Sustituciones como que `n!/n` se reduzca a `(n-1)!` ya no se realizarán. Cuando  `letrat` vale  `true`, entonces se simplifican el numerador, el denominador y el cociente, en este orden.


Estas funciones de sustitución permiten al usuario trabajar con varios paquetes de reglas al mismo tiempo. Cada paquete de reglas puede contener cierto número de reglas `let` que son referenciadas por un nombre dado por el usuario. 
`let ([prod, repl, predname, arg_1, ..., arg_n], nombre_paquete)` añade la regla  *predname* al paquete de reglas  *nombre_paquete*. `letsimp (expr, package_name)` aplica las reglas de *nombre_paquete*. La llamada `letsimp (expr, nombre_paquete1, nombre_paquete2, ...)`
es equivalente a `letsimp (expr, nombre_paquete1)` seguida de `letsimp (%, nombre_paquete2)`, ....


`current_let_rule_package` es el nombre del paquete de reglas que se está utilizando. A esta variable se le puede asignar el nombre de cualquier paquete de reglas definido mediante el comando `let`. Siempre que una de las funciones incluidas en el paquete  `let` sean invocadas sin nombre de paquete, se utilizará el paquete cuyo nombre se guarde en `current_let_rule_package`. Si se hace una llamada tal como `letsimp (expr, rule_pkg_name)`, el paquete de reglas *rule_pkg_name* es utilizado solamente para ese comando `letsimp`, sin efectuarse cambios en 
`current_let_rule_package`. A menos que se indique otra cosa, `current_let_rule_package` toma por defecto el valor de `default_let_rule_package`.



```maxima
(%i1) matchdeclare ([a, a1, a2], true)$
(%i2) oneless (x, y) := is (x = y-1)$
(%i3) let (a1*a2!, a1!, oneless, a2, a1);
(%o3)         a1 a2! --> a1! where oneless(a2, a1)
(%i4) letrat: true$
(%i5) let (a1!/a1, (a1-1)!);
                        a1!
(%o5)                   --- --> (a1 - 1)!
                        a1
(%i6) letsimp (n*m!*(n-1)!/m);
(%o6)                      (m - 1)! n!
(%i7) let (sin(a)^2, 1 - cos(a)^2);
                        2               2
(%o7)                sin (a) --> 1 - cos (a)
(%i8) letsimp (sin(x)^4);
                        4           2
(%o8)                cos (x) - 2 cos (x) + 1
```

<!-- category: Other -->
<!-- keywords: let_rule_packages -->
<!-- signatures: let_rule_packages -->
### Variable: let_rule_packages

Valor por defecto: `[default_let_rule_package]`


La variable `let_rule_packages` guarda una lista con todos los paquetes de reglas definidos por el usuario, junto con el paquete por defecto `default_let_rule_package`.

<!-- category: Other -->
<!-- keywords: letrat -->
<!-- signatures: letrat -->
### Variable: letrat

Valor por defecto: `false`


Cuando `letrat` vale `false`, `letsimp` simplifica separadamente el numerador y denominador de una fracción sin simplificar luego el cociente.


Cuando `letrat` vale `true`, se simplifican el numerador, denominador y cociente, por este orden.



```maxima
(%i1) matchdeclare (n, true)$
(%i2) let (n!/n, (n-1)!);
                         n!
(%o2)                    -- --> (n - 1)!
                         n
(%i3) letrat: false$
(%i4) letsimp (a!/a);
                               a!
(%o4)                          --
                               a
(%i5) letrat: true$
(%i6) letsimp (a!/a);
(%o6)                       (a - 1)!
```

<!-- category: Other -->
<!-- keywords: letrules -->
<!-- signatures: letrules(), letrules(nombre_paquete) -->
### Function: letrules ()

Muestra las reglas de un paquete de reglas. La llamada `letrules ()` muestra las reglas del paquete de reglas actual. La llamada `letrules (nombre_paquete)` muestra las reglas de *nombre_paquete*.


El paquete de reglas actual tiene su nombre almacenado en by `current_let_rule_package`. A menos que se indique de otra manera, `current_let_rule_package` toma por defecto el valor de `default_let_rule_package`.


Véase también `disprule`, que muestra las reglas definidas por `tellsimp` y `tellsimpafter`.

<!-- category: Other -->
<!-- keywords: letsimp -->
<!-- signatures: letsimp(expr), letsimp(expr, nombre_paquete), letsimp(expr, nombre_paquete_1, ..., nombre_paquete_n) -->
### Function: letsimp (expr)

Aplica repetidamente las reglas definidas por `let` hasta que no se puedan hacer más cambios en *expr*.


La llamada `letsimp (expr)` utiliza las reglas de `current_let_rule_package`.


La llamada `letsimp (expr, nombre_paquete)` utiliza las reglas de *nombre_paquete* sin efectuar cambios en `current_let_rule_package`.


La llamada `letsimp (expr, nombre_paquete_1, ..., nombre_paquete_n)`
es equivalente a `letsimp (expr, nombre_paquete_1`, seguida de  `letsimp (%, nombre_paquete_2)` y así sucesivamente.

<!-- category: Other -->
<!-- keywords: matchdeclare -->
<!-- signatures: matchdeclare(a_1, pred_1, ..., a_n, pred_n) -->
### Function: matchdeclare (a_1, pred_1, ..., a_n, pred_n)

Asocia un predicado *pred_k* con una variable o lista de variables  *a_k*, de forma que  *a_k* se comparará con expresiones para las cuales el predicado devuelva algo que no sea `false`.


Un predicado puede ser el nombre de una función, una expresión lambda, una
llamada a función, una llamada a una expresión lambda sin
el último argumento, `true` o `all`.
Cualquier expresión se hace coincidir con `true` o `all`. 


Si el predicado se especifica como una llamada a función o a
una expresión lambda, la expresión a ser analizada es añadida 
a la lista de argumentos, siendo los argumentos evaluados en el 
momento de ser evaluada la comparación. 
En cambio, si el predicado se especifica como un nombre de función
o como una expresión lambda, la expresión a ser analizada será 
su único argumento. No es necesario definir una función de predicado cuando se hace una llamada a `matchdeclare`; el predicado no se evalúa hasta que se ensaya  una comparación.


Un predicado puede devolver tanto una expresión booleana,
como `true` o `false`.
Las expresiones booleanas se evalúan con `is` dentro
de la regla, por lo que no es necesario llamar a `is`
desde dentro del predicado.


Si una expresión satisface un predicado, se asigna a la variable de comparación la expresión, excepto cuando las variables de comparación son operandos de sumas `+` o multiplicaciones `*`. Solamente las sumas y multiplicaciones son tratadas de forma especial; los demás operadores n-arios (tanto los del sistema como los definidos por el usuario) son tratados como funciones ordinarias.


En el caso de sumas y multiplicaciones, a la variable de comparación se le puede asignar una expresión simple que satisfaga el predicado de comparación, o una suma o producto, respectivamente, de tales expresiones. Los predicados son evaluados en el orden en el que sus variables asociadas aparecen en el patrón de comparación, y un término que satisfaga más de un predicado es tomado por el primer predicado que satisfaga. Cada predicado se compara con todos los operandos de la suma o producto antes de ser evaluado el siguiente predicado. Además, si 0 o 1, respectivamente, satisface un predicado de comparación, y no hay otros términos que lo satisfagan, se asignará el 0 o 1 a la variable de comparación asociada al predicado.


El algoritmo para procesar patrones de suma y multiplicación hace que los resultados de algunas comparaciones dependan del orden de los términos en el patrón de comparación y en la expresión a ser comparada. Sin embargo, si todos los predicados de comparación son mutuamente excluyentes, el resultado de la comparación no depende para nada de la ordenación, puesto que un predicado de comparación no puede aceptar términos aceptados por otros predicados.


Invocando `matchdeclare` con una variable *a* como argumento cambia la propiedad de `matchdeclare` para  *a*, si ya había una declarada; solamente el `matchdeclare` más reciente está activo cuando se define una regla. Cambios posteriores en la propiedad de `matchdeclare` (via `matchdeclare` o `remove`) no afectan a las reglas existentes.


`propvars (matchdeclare)` devuelve la lista de todas las variables para las cuales hay una propiedad de `matchdeclare`. La llamada `printprops (a, matchdeclare)` devuelve el predicado para la variable `a`.
La llamada `printprops (all, matchdeclare)` devuelve la lista de predicados de todas las variables de `matchdeclare`. La llamada `remove (a, matchdeclare)` borra la propiedad `matchdeclare` de *a*.


Las funciones `defmatch`, `defrule`, `tellsimp`, `tellsimpafter` y `let` construyen reglas que analizan expresiones mediante patrones.


`matchdeclare` no evalúa sus argumentos y siempre devuelve `done`.


Ejemplos:


Un predicado puede ser el nombre de una función, una expresión lambda, una
llamada a función, una llamada a una expresión lambda sin
el último argumento, `true` o `all`.











```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) matchdeclare (bb, lambda ([x], x > 0));
(%o2)                         done
(%i3) matchdeclare (cc, freeof (%e, %pi, %i));
(%o3)                         done
(%i4) matchdeclare (dd, lambda ([x, y], gcd (x, y) = 1) (1728));
(%o4)                         done
(%i5) matchdeclare (ee, true);
(%o5)                         done
(%i6) matchdeclare (ff, all);
(%o6)                         done
```


Si una expresión satisface un predicado, se asigna a la variable de comparación la expresión.








```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) defrule (r1, bb^aa, ["integer" = aa, "atom" = bb]);
                    aa
(%o2)        r1 : bb   -> [integer = aa, atom = bb]
(%i3) r1 (%pi^8);
(%o3)               [integer = 8, atom = %pi]
```


En el caso de sumas y multiplicaciones, a la variable de comparación se le puede asignar una expresión simple que satisfaga el predicado de comparación, o una suma o producto, respectivamente, de tales expresiones. 












```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb,
              ["all atoms" = aa, "all nonatoms" = bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + sin(x));
(%o3)     [all atoms = 8, all nonatoms = sin(x) + a b]
(%i4) defrule (r2, aa * bb,
               ["all atoms" = aa, "all nonatoms" = bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * sin(x));
(%o5)    [all atoms = 8, all nonatoms = (b + a) sin(x)]
```

<!-- category: Other -->
<!-- keywords: maxapplydepth -->
<!-- signatures: maxapplydepth -->
### Variable: maxapplydepth

Valor por defecto: 10000


La variable `maxapplydepth` es la máxima profundidad a la que van a introducirse `apply1` y  `apply2`.

<!-- category: Other -->
<!-- keywords: maxapplyheight -->
<!-- signatures: maxapplyheight -->
### Variable: maxapplyheight

Valor por defecto: 10000


La variable `maxapplyheight` es la m2’axima altura a la que escalará `applyb1` antes de detenerse.

<!-- category: Other -->
<!-- keywords: remlet -->
<!-- signatures: remlet(prod, nombre), remlet(), remlet(all), remlet(all, nombre) -->
### Function: remlet (prod, nombre)

Elimina la última regla de sustitución *prod* –> repl que haya sido definida por la función `let`. Si se suministar el nombre la regla será borrada del paquete con ese mismo nombre.


Las llamadas `remlet()` y `remlet(all)` eliminan todas las reglas de sustitución del paquete de reglas actual. Si se suministra el nombre de un paquete de reglas, como en `remlet (all, nombre)`, el paquete de reglas con ese  *nombre* es también eliminado.


Si es necesario cambiar una sustitución haciendo uso de la misma producción, no es necesario llamar a  `remlet`, simplemente redefínase la sustitución utilizando la misma producción con la función  `let` junto con el nuevo reemplazamiento y/o nombre de predicado. De ser llamado nuevamente `remlet (prod)` la sustitución original sería recuperada.


Véase también `remrule`, que elimina una regla definida por  `tellsimp` o `tellsimpafter`.

<!-- category: Other -->
<!-- keywords: remrule -->
<!-- signatures: remrule(op, nombre_regla), remrule(op, all) -->
### Function: remrule (op, nombre_regla)

Elimina las reglas previamente definidas por `tellsimp` o `tellsimpafter`.


La llamada `remrule (op, nombre_regla)` elimina la regla de nombre  *nombre_regla* del operador *op*.


Independientemente de que  *op* sea un operador propio de Maxima o haya sido definido por el usario (como los establecidos por `infix`, `prefix`, etc.), tanto *op* como *rulename* deben ir encerrados entre comillas dobles.


La llamada `remrule (function, all)` borra todas las reglas para el operador *op*.


Véase también `remlet`, que elimina una regla definida mediante `let`.


Ejemplos:

         


















```maxima
(%i1) tellsimp (foo (aa, bb), bb - aa);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (aa + bb, special_add (aa, bb));
(%o2)                   [+rule1, simplus]
(%i3) infix ("@@");
(%o3)                          @@
(%i4) tellsimp (aa @@ bb, bb/aa);
(%o4)                   [@@rule1, false]
(%i5) tellsimpafter (quux (%pi, %e), %pi - %e);
(%o5)                  [quuxrule1, false]
(%i6) tellsimpafter (quux (%e, %pi), %pi + %e);
(%o6)             [quuxrule2, quuxrule1, false]
(%i7) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
       quux (%e, %pi)];
                                     bb
(%o7) [bb - aa, special_add(aa, bb), --, %pi - %e, %pi + %e]
                                     aa
(%i8) remrule (foo, foorule1);
(%o8)                          foo
(%i9) remrule ("+", ?\+rule1);
(%o9)                           +
(%i10) remrule ("@@", ?\@\@rule1);
(%o10)                         @@
(%i11) remrule (quux, all);
(%o11)                        quux
(%i12) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
        quux (%e, %pi)];
(%o12) [foo(aa, bb), bb + aa, aa @@ bb, quux(%pi, %e), 
                                         quux(%e, %pi)]
```

<!-- category: Other -->
<!-- keywords: tellsimp -->
<!-- signatures: tellsimp(patrón, reemplazamiento) -->
### Function: tellsimp (patrón, reemplazamiento)

La función `tellsimp` es similar a  `tellsimpafter` pero coloca nueva información antes que la antigua, de manera que se aplica antes que las reglas de simplificación de Maxima.


La función `tellsimp` se utiliza cuando es importante utilizar la expresión antes de que el simplificador opere sobre ella; por ejemplo, cuando el simplificador ya "sabe" algo sobre una expresión, pero lo que devuelve no es lo que quiere el usuario. En cambio, cuando  el simplificador ya "sabe" algo sobre una expresión pero lo que devuelve no es lo suficiente para el usuario, entonces éste podrá estar interesado en utilizar `tellsimpafter`.


El patrón no puede ser una suma, ni un producto, ni una variable ni un número.


`rules` es la lista de reglas definidas por
`defrule`, `defmatch`, `tellsimp` y `tellsimpafter`.


Ejemplos:



```maxima
(%i1) matchdeclare (x, freeof (%i));
(%o1)                         done
(%i2) %iargs: false$
(%i3) tellsimp (sin(%i*x), %i*sinh(x));
(%o3)                 [sinrule1, simp-%sin]
(%i4) trigexpand (sin (%i*y + x));
(%o4)         sin(x) cos(%i y) + %i cos(x) sinh(y)
(%i5) %iargs:true$
(%i6) errcatch(0^0);
 0
0  has been generated
(%o6)                          []
(%i7) ev (tellsimp (0^0, 1), simp: false);
(%o7)                  [^rule1, simpexpt]
(%i8) 0^0;
(%o8)                           1
(%i9) remrule ("^", %th(2)[1]);
(%o9)                           ^
(%i10) tellsimp (sin(x)^2, 1 - cos(x)^2);
(%o10)                 [^rule2, simpexpt]
(%i11) (1 + sin(x))^2;
                                      2
(%o11)                    (sin(x) + 1)
(%i12) expand (%);
                                   2
(%o12)               2 sin(x) - cos (x) + 2
(%i13) sin(x)^2;
                                  2
(%o13)                     1 - cos (x)
(%i14) kill (rules);
(%o14)                        done
(%i15) matchdeclare (a, true);
(%o15)                        done
(%i16) tellsimp (sin(a)^2, 1 - cos(a)^2);
(%o16)                 [^rule3, simpexpt]
(%i17) sin(y)^2;
                                  2
(%o17)                     1 - cos (y)
```

<!-- category: Other -->
<!-- keywords: tellsimpafter -->
<!-- signatures: tellsimpafter(patrón, reemplazamiento) -->
### Function: tellsimpafter (patrón, reemplazamiento)

Define una regla de simplificación que el simplificador aplicará después de las reglas de simplificación propias de de Maxima. El *patrón* es una expresión que contiene variables de patrón (declaradas por `matchdeclare`) junto con otros átomos y operadores. El contenido de *reemplazamiento* sustituye una expresión que coincida con el patrón; a las variables de patrón en *reemplazamiento* se les asignan los valores coincidentes en la expresión.


El *patrón* puede ser una expresión no atómica en la que el operador principal no sea una variable de patrón; la regla de simplificación se asocia con el operador principal. Los nombres de las funciones (con una excepción que se indica más abajo), listas y arrays pueden aparecer en el *patrón* como operador principal sólo como literales (no variables de patrones); esto excluye expresiones como  `aa(x)` y `bb[y]`, si tanto `aa` como `bb` son patrones de variables. Nombres de funciones, listas y arrays que sean variables de patrón pueden aparecer como operadores que no sean el operador principal de  *patrón*.


Hay una excepción a la regla indicada más arriba concerniente a los nombres de funciones. El nombre de una función subindicada en una expresión tal como `aa[x](y)` puede ser una variable de patrón porque el operador principal no es  `aa` sino el átomo de Lisp  `mqapply`. Esta es una consecuencia de la representación de expresiones que contienen funciones subindicadas.


Las reglas de simplificación se aplican tras las evaluaciones (a menos que se supriman con el apóstrofo o la variable `noeval`). Las reglas establecidas por `tellsimpafter` se aplican en el orden en que han sido definidas y después de las reglas propias de Maxima. Las reglas se aplican de abajo arriba, esto es, se aplican primero a las subexpresiones antes que a toda la expresión. Puede ser necesario simplificar repetidamente un resultado (por ejemplo, mediante el operador de doble comilla simple `''` o la variable `infeval`) para asegurar que se aplican todas las reglas.


Las variables de patrón se tratan como variables locales en las reglas de simplificación. Una vez definida una regla, el valor de una variable de patrón no afecta a la regla, ni se ve influenciada poe ésta. Una asignación a una variable de patrón que resulta de la aplicación exitosa de una regla no afecta a la asignación actual de la variable de patrón. Sin embargo, como cualquier otro átomo de Maxima, las propiedades de las variables de patrón (tal como se definen con `put` y sus funciones relacionadas) son globales.


La regla construida por  `tellsimpafter` es nombrada detrás del operador principal de *patrón*. Reglas para operadores de Maxima y operadores definidos por el usuario con `infix`, `prefix`, `postfix`, `matchfix` y `nofix`, tienen nombres que son cadenas alfanuméricas de Maxima. Reglas para otras funciones tienen nombres que son identificadores ordinarios de Maxima.


El tratamiento de formas nominales y verbales es hasta cierto punto confuso. Si se define una regla para una forma nominal (o verbal)  y ya existe una regla para la correspondiente forma verbal (o nominal), la regla recién definida se aplica a ambas formas (nominal y verbal). Si no existe regla para una forma verbal (o nominal) la regla recién definida se aplica únicamente a la forma nominal (o verbal).


La regla construida por  `tellsimpafter` es una típica función de Lisp. Si el nombre de la regla es `$foorule1`, la sentencia `:lisp (trace $foorule1)` hace una traza de la función y  `:lisp (symbol-function '$foorule1)` muestra su definición.


La función `tellsimpafter` no evalúa sus argumentos y devuelve la lista de reglas para el operador principal de  *patrón*, incluida la regla recién establecida.


Véanse también `matchdeclare`, `defmatch`, `defrule`, `tellsimp`, `let`,
`kill`, `remrule` y `clear_rules`.


Ejemplos:


*pattern* puede ser cualquier expresión no atómica en la que el operador principal no sea una variable de patrón.



```maxima
(%i1) matchdeclare (aa, atom, [ll, mm], listp, xx, true)$
(%i2) tellsimpafter (sin (ll), map (sin, ll));
(%o2)                 [sinrule1, simp-%sin]
(%i3) sin ([1/6, 1/4, 1/3, 1/2, 1]*%pi);
                    1  sqrt(2)  sqrt(3)
(%o3)              [-, -------, -------, 1, 0]
                    2     2        2
(%i4) tellsimpafter (ll^mm, map ("^", ll, mm));
(%o4)                  [^rule1, simpexpt]
(%i5) [a, b, c]^[1, 2, 3];
                                2   3
(%o5)                      [a, b , c ]
(%i6) tellsimpafter (foo (aa (xx)), aa (foo (xx)));
(%o6)                   [foorule1, false]
(%i7) foo (bar (u - v));
(%o7)                    bar(foo(u - v))
```


Las reglas se aplican en el orden en que se definen. Si dos reglas coinciden con una expresión, se aplica aquélla que haya sido definida en primer lugar.



```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) tellsimpafter (foo (aa), bar_1 (aa));
(%o2)                   [foorule1, false]
(%i3) tellsimpafter (foo (aa), bar_2 (aa));
(%o3)              [foorule2, foorule1, false]
(%i4) foo (42);
(%o4)                       bar_1(42)
```


Las variables de patrón se tratan como variables locales en las reglas de simplificación.
(Compárese con `defmatch`, que trata las variables de patrón como globales.)



```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) bb: 12345;
(%o3)                         12345
(%i4) foo (42, %e);
(%o4)                 bar(aa = 42, bb = %e)
(%i5) bb;
(%o5)                         12345
```


Como cualquier otro átomo, las propiedades de las variables de patrón son globales, incluso cuando sus valores sean locales. En este ejemplo se declara una propiedad de asignación a treavés de  `define_variable`. Esta es una propiedad del átomo  `bb` en todo Maxima.



```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) foo (42, %e);
(%o3)                 bar(aa = 42, bb = %e)
(%i4) define_variable (bb, true, boolean);
(%o4)                         true
(%i5) foo (42, %e);
Error: bb was declared mode boolean, has value: %e
 -- an error.  Quitting.  To debug this try debugmode(true);
```


Las reglas se nombran después de los operadores principales. Los nombres de reglas tanto para las funciones de Maxima como para las definidas por el usuario son cadenas alfanuméricas, mientras que los nombres de las otras funciones son identificadores típicos.



```maxima
(%i1) tellsimpafter (foo (%pi + %e), 3*%pi);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (foo (%pi * %e), 17*%e);
(%o2)              [foorule2, foorule1, false]
(%i3) tellsimpafter (foo (%i ^ %e), -42*%i);
(%o3)         [foorule3, foorule2, foorule1, false]
(%i4) tellsimpafter (foo (9) + foo (13), quux (22));
(%o4)                   [+rule1, simplus]
(%i5) tellsimpafter (foo (9) * foo (13), blurf (22));
(%o5)                  [*rule1, simptimes]
(%i6) tellsimpafter (foo (9) ^ foo (13), mumble (22));
(%o6)                  [^rule1, simpexpt]
(%i7) rules;
(%o7) [trigrule0, trigrule1, trigrule2, trigrule3, trigrule4, 
htrigrule1, htrigrule2, htrigrule3, htrigrule4, foorule1, 
foorule2, foorule3, +rule1, *rule1, ^rule1]
(%i8) foorule_name: first (%o1);
(%o8)                       foorule1
(%i9) plusrule_name: first (%o4);
(%o9)                        +rule1
(%i10) [?mstringp (foorule_name), symbolp (foorule_name)];
(%o10)                    [false, true]
(%i11) [?mstringp (plusrule_name), symbolp (plusrule_name)];
(%o11)                    [true, true]
(%i12) remrule (foo, foorule1);
(%o12)                         foo
(%i13) remrule ("^", "^rule1");
(%o13)                          ^
```


Un ejemplo de producto anticonmutativo.












```maxima
(%i1) gt (i, j) := integerp(j) and i < j;
(%o1)           gt(i, j) := integerp(j) and i < j
(%i2) matchdeclare (i, integerp, j, gt(i));
(%o2)                         done
(%i3) tellsimpafter (s[i]^^2, 1);
(%o3)                 [^^rule1, simpncexpt]
(%i4) tellsimpafter (s[i] . s[j], -s[j] . s[i]);
(%o4)                   [.rule1, simpnct]
(%i5) s[1] . (s[1] + s[2]);
(%o5)                    s  . (s  + s )
                          1     2    1
(%i6) expand (%);
(%o6)                      1 - s  . s
                                2    1
(%i7) factor (expand (sum (s[i], i, 0, 9)^^5));
(%o7) 100 (s  + s  + s  + s  + s  + s  + s  + s  + s  + s )
            9    8    7    6    5    4    3    2    1    0
```

