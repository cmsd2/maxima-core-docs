## Conjuntos

<!-- category: Other -->
<!-- keywords: adjoin -->
<!-- signatures: adjoin(x, a) -->
### Function: adjoin (x, a)

Calcula la unión del conjunto *a* y `{x}`.


La función `adjoin` emite un mensaje de error si *a*
no es un conjunto literal.


Las sentencias `adjoin(x, a)` y 
`union(set(x), a)` son equivalentes, aunque
`adjoin` puede ser algo más rápida que `union`.


Véase también `disjoin`.


Ejemplos:







```maxima
(%i1) adjoin (c, {a, b});
(%o1)                       {a, b, c}
(%i2) adjoin (a, {a, b});
(%o2)                        {a, b}
```

<!-- category: Other -->
<!-- keywords: belln -->
<!-- signatures: belln(n) -->
### Function: belln (n)

Representa el $n$-ésimo número de Bell, de
modo que `belln(n)` es el número de particiones de un conjunto de 
*n* elementos.


El argumento *n* debe ser un entero no negativo.


La función `belln` se distribuye sobre ecuaciones, listas,
matrices y conjuntos.


Ejemplos:


`belln` se aplica a enteros no negativos,









```maxima
(%i1) makelist (belln (i), i, 0, 6);
(%o1)               [1, 1, 2, 5, 15, 52, 203]
(%i2) is (cardinality (set_partitions ({})) = belln (0));
(%o2)                         true
(%i3) is (cardinality (set_partitions ({1, 2, 3, 4, 5, 6}))
                            = belln (6));
(%o3)                         true
```


Si *n* no es un entero no negativo, la función `belln(n)` no hace cálculo alguno.






```maxima
(%i1) [belln (x), belln (sqrt(3)), belln (-9)];
(%o1)        [belln(x), belln(sqrt(3)), belln(- 9)]
```

<!-- category: Other -->
<!-- keywords: cardinality -->
<!-- signatures: cardinality(a) -->
### Function: cardinality (a)

Devuelve el número de elementos del conjunto *a*.


La función `cardinality` ignora los elementos
redundantes, incluso cuando la simplificación está
desabilitada.


Ejemplos:









```maxima
(%i1) cardinality ({});
(%o1)                           0
(%i2) cardinality ({a, a, b, c});
(%o2)                           3
(%i3) simp : false;
(%o3)                         false
(%i4) cardinality ({a, a, b, c});
(%o4)                           3
```

<!-- category: Other -->
<!-- keywords: cartesian_product -->
<!-- signatures: cartesian_product(b_1, ..., b_n) -->
### Function: cartesian_product (b_1, ..., b_n)

Devuelve un conjunto formado por listas de la forma `[x_1, ..., x_n]`,
siendo *x_1*, ..., *x_n* elementos de los conjuntos *b_1*, ... , *b_n*,
respectivamente.


La función `cartesian_product` emite un mensaje de error si alguno
de sus argumentos no es un conjunto literal.


Ejemplos:









```maxima
(%i1) cartesian_product ({0, 1});
(%o1)                      {[0], [1]}
(%i2) cartesian_product ({0, 1}, {0, 1});
(%o2)           {[0, 0], [0, 1], [1, 0], [1, 1]}
(%i3) cartesian_product ({x}, {y}, {z});
(%o3)                      {[x, y, z]}
(%i4) cartesian_product ({x}, {-1, 0, 1});
(%o4)              {[x, - 1], [x, 0], [x, 1]}
```

<!-- category: Other -->
<!-- keywords: disjoin -->
<!-- signatures: disjoin(x, a) -->
### Function: disjoin (x, a)

Devuelve el conjunto *a* sin el elemento *x*.
Si *x* no es elemento de *a*, entonces el
resultado es el propio *a*.


La función `disjoin` emite un mensaje de error si
*a* no es un conjunto literal.


Las sentencias `disjoin(x, a)`, `delete(x, a)`
y `setdifference(a, set(x))` son todas ellas equivalentes;
pero en general, `disjoin` será más rápida que las otras.


Ejemplos:








```maxima
(%i1) disjoin (a, {a, b, c, d});
(%o1)                       {b, c, d}
(%i2) disjoin (a + b, {5, z, a + b, %pi});
(%o2)                      {5, %pi, z}
(%i3) disjoin (a - b, {5, z, a + b, %pi});
(%o3)                  {5, %pi, b + a, z}
```

<!-- category: Other -->
<!-- keywords: disjointp -->
<!-- signatures: disjointp(a, b) -->
### Function: disjointp (a, b)

Devuelve `true` si y sólo si los conjuntos  *a* y *b*
son disjuntos.


La función `disjointp` emite un mensaje de error si
*a* o *b* no son conjuntos literales.


Ejemplos:







```maxima
(%i1) disjointp ({a, b, c}, {1, 2, 3});
(%o1)                         true
(%i2) disjointp ({a, b, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: divisors -->
<!-- signatures: divisors(n) -->
### Function: divisors (n)

Calcula el conjunto de divisores de *n*.


La sentencia `divisors(n)` devuelve un conjunto
de enteros si *n* es un entero no nulo.
El conjunto de divisores incluye los elementos 1 y *n*.
Los divisores de un entero negativo son los divisores de su
valor absoluto.


La función `divisors` se distribuye sobre las ecuaciones,
listas, matrices y conjuntos.


Ejemplos:


Se puede comprobar que 28 es un número perfecto:
la suma de sus divisores (excepto él mismo) es 28.







```maxima
(%i1) s: divisors(28);
(%o1)                 {1, 2, 4, 7, 14, 28}
(%i2) lreduce ("+", args(s)) - 28;
(%o2)                          28
```


La función `divisors` es simplificadora.
Haciendo la sustitución de `a` por 8 en `divisors(a)`
devuelve los divisores sin tener que reevaluar `divisors(8)`,







```maxima
(%i1) divisors (a);
(%o1)                      divisors(a)
(%i2) subst (8, a, %);
(%o2)                     {1, 2, 4, 8}
```


La función `divisors` se distribuye sobre ecuaciones, listas,
matrices y conjuntos.









```maxima
(%i1) divisors (a = b);
(%o1)               divisors(a) = divisors(b)
(%i2) divisors ([a, b, c]);
(%o2)        [divisors(a), divisors(b), divisors(c)]
(%i3) divisors (matrix ([a, b], [c, d]));
                  [ divisors(a)  divisors(b) ]
(%o3)             [                          ]
                  [ divisors(c)  divisors(d) ]
(%i4) divisors ({a, b, c});
(%o4)        {divisors(a), divisors(b), divisors(c)}
```

<!-- category: Other -->
<!-- keywords: elementp -->
<!-- signatures: elementp(x, a) -->
### Function: elementp (x, a)

Devuelve `true` si y sólo si *x* es miembro del
conjunto *a*.


La función `elementp` emite un mensaje de error si 
*a* no es un conjunto literal.


Ejemplos: 







```maxima
(%i1) elementp (sin(1), {sin(1), sin(2), sin(3)});
(%o1)                         true
(%i2) elementp (sin(1), {cos(1), cos(2), cos(3)});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: emptyp -->
<!-- signatures: emptyp(a) -->
### Function: emptyp (a)

Devuelve `true` si y sólo si *a* es el conjunto vacío o la lista vacía.


Ejemplos:







```maxima
(%i1) map (emptyp, [{}, []]);
(%o1)                     [true, true]
(%i2) map (emptyp, [a + b, {{}}, %pi]);
(%o2)                 [false, false, false]
```

<!-- category: Other -->
<!-- keywords: equiv_classes -->
<!-- signatures: equiv_classes(s, F) -->
### Function: equiv_classes (s, F)

Devuelve el conjunto de las clases de equivalencia del conjunto *s*
respecto de la relación de equivalencia *F*.


El argumento *F* es una función de dos variables definida sobre
el producto cartesiano *s* por *s*.
El valor devuelto por *F* debe ser `true` o `false`,
o bien una expresión *expr* tal que `is(expr)`
tome el valor `true` o `false`.


Si *F* no es una relación de equivalencia, `equiv_classes`
la acepta sin emitir ningún mensaje de error, pero el resultado
será incorrecto en general.


Ejemplos:


La relación de equivalencia es una expresión lambda que devuelve 
`true` o `false`,







```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0},
                      lambda ([x, y], is (equal (x, y))));
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


La relación de equivalencia es el nombre de una función relacional
en la que `is` evalúa a `true` o `false`,






```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0}, equal);
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


Las clases de equivalencia son números que difieren en un múltiplo de 3.







```maxima
(%i1) equiv_classes ({1, 2, 3, 4, 5, 6, 7}, 
              lambda ([x, y], remainder (x - y, 3) = 0));
(%o1)              {{1, 4, 7}, {2, 5}, {3, 6}}
```

<!-- category: Other -->
<!-- keywords: every -->
<!-- signatures: every(f, s), every(f, L_1, ..., L_n) -->
### Function: every (f, s)

Devuelve `true` si el predicado *f* vale `true`
para todos los argumentos dados.


Dado un conjunto como segundo argumento,
`every(f, s)` devuelve `true`
si `is(f(a_i))` devuelve `true` para todos los
*a_i* pertenecientes *s*.
La función `every` puede evaluar o no *f* para todos los
*a_i* pertenecientes *s*.
Puesto que los conjuntos no están ordenados, `every`
puede evaluar `f(a_i)` en cualquier orden.


Dada una o más listas como argumentos,
`every(f, L_1, ..., L_n)` devuelve `true`
si `is(f(x_1, ..., x_n))` devuelve `true` 
para todo *x_1*, ..., *x_n* en *L_1*, ..., *L_n*, respectivamente.
La función `every` puede evaluar o no 
*f* para cualquier combinación de *x_1*, ..., *x_n*; además,
`every` evalúa las listas en el orden creciente del índice.


Dado un conjunto vacío `{}` o lista vacía 
`[]` como argumentos, `every` devuelve `false`.


Si la variable global `maperror` vale `true`, todas las listas
*L_1*, ..., *L_n* deben ser de igual longitud.
Si `maperror` vale `false`, los argumentos en forma de listas
se truncan para igualar sus longitudes a la de la lista más corta.


Los valores que devuelve el predicado *f* cuando toman 
(mediante `is`) un valor diferente a `true` y `false`
se controlan con la variable global `prederror`.
Si `prederror` vale `true`, tales valores se
consideran como `false` y la respuesta de `every` es `false`.
Si `prederror` vale `false`, tales valores se
consideran como desconocidos (`unknown`) y la respuesta de 
`every` es `unknown`.


Ejemplos:


Se aplica `every` a un único conjunto.
El predicado es una función de un argumento.







```maxima
(%i1) every (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) every (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         false
```


Se aplica `every` a dos listas.
El predicado es una función de dos argumentos.







```maxima
(%i1) every ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) every ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Las respuestas del predicado *f* que se evalúan 
a cualquier cosa diferente de `true` y `false`
están controlados por la variable global `prederror`.











```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
                   [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) prederror : true;
(%o4)                         true
(%i5) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o5)                         false
```

<!-- category: Other -->
<!-- keywords: extremal_subset -->
<!-- signatures: extremal_subset(s, f, max), extremal_subset(s, f, min) -->
### Function: extremal_subset (s, f, max)

Calcula el subconjunto de *s* para el cual la función *f*
toma sus valores mayor y menor.


La sentencia `extremal_subset(s, f, max)`
devuelve el subconjunto del conjunto o lista *s* para el cual
la función real *f* toma su valor máximo.


La sentencia `extremal_subset(s, f, min)`
devuelve el subconjunto del conjunto o lista *s* para el cual
la función real *f* toma su valor mínimo.


Ejemplos







```maxima
(%i1) extremal_subset ({-2, -1, 0, 1, 2}, abs, max);
(%o1)                       {- 2, 2}
(%i2) extremal_subset ({sqrt(2), 1.57, %pi/2}, sin, min);
(%o2)                       {sqrt(2)}
```

<!-- category: Other -->
<!-- keywords: flatten -->
<!-- signatures: flatten(expr) -->
### Function: flatten (expr)

Recoge los argumentos de subexpresiones con el mismo operador que *expr*
y construye con ellas otra expresión a partir de estos argumentos.


Aquellas subexpresiones en las que el operador es diferente del operador
principal de `expr` se copian sin modificarse, incluso cuando ellas
mismas contengan subexpresiones en las que el operador sea el mismo 
que el de `expr`.


Es posible que `flatten` construya expresiones en las que el número
de argumentos difiera del número admitido por el operador, lo cual
hará que se emita un mensaje de error. La función `flatten`
no intentará detectar estas situaciones.


Las expresiones que tengan representaciones especiales, por ejemplo las racionales
canónicas (CRE), no admiten que se aplique sobre ellas la función `flatten`;
en tales casos se devuelve el argumento sin modificación.


Ejemplos:


Aplicada a una lista, `flatten` reune todos los elementos que son a su vez listas.






```maxima
(%i1) flatten ([a, b, [c, [d, e], f], [[g, h]], i, j]);
(%o1)            [a, b, c, d, e, f, g, h, i, j]
```


Aplicado a un conjunto, `flatten` reune todos los elementos que son a su vez conjuntos.







```maxima
(%i1) flatten ({a, {b}, {{c}}});
(%o1)                       {a, b, c}
(%i2) flatten ({a, {[a], {a}}});
(%o2)                       {a, [a]}
```


La función `flatten` es similar a la declaración del operador
principal como n-ario. Sin embargo, `flatten` no tiene efecto alguno
sobre subexpresiones que tengan un operador diferente del principal, mientras
que sí lo tiene una declaración n-aria.









```maxima
(%i1) expr: flatten (f (g (f (f (x)))));
(%o1)                     f(g(f(f(x))))
(%i2) declare (f, nary);
(%o2)                         done
(%i3) ev (expr);
(%o3)                      f(g(f(x)))
```


La función `flatten` trata las funciones subindicadas como
a cualquier otro operador.






```maxima
(%i1) flatten (f[5] (f[5] (x, y), z));
(%o1)                      f (x, y, z)
                            5
```


Es posible que `flatten` construya expresiones en las que el número
de argumentos difiera del número admitido por el operador.








```maxima
(%i1) 'mod (5, 'mod (7, 4));
(%o1)                   mod(5, mod(7, 4))
(%i2) flatten (%);
(%o2)                     mod(5, 7, 4)
(%i3) ''%, nouns;
Wrong number of arguments to mod
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Other -->
<!-- keywords: full_listify -->
<!-- signatures: full_listify(a) -->
### Function: full_listify (a)

Sustituye los operadores de conjunto presentes en *a*
por operadores de listas, devolviendo el resultado.
La función `full_listify` sustituye operadores de 
conjuntos en subexpresiones anidadas, incluso cuando
el operador principal no es `set`.


La función `listify` sustituye únicamente el
operador principal.


Ejemplos:







```maxima
(%i1) full_listify ({a, b, {c, {d, e, f}, g}});
(%o1)               [a, b, [c, [d, e, f], g]]
(%i2) full_listify (F (G ({a, b, H({c, d, e})})));
(%o2)              F(G([a, b, H([c, d, e])]))
```

<!-- category: Other -->
<!-- keywords: fullsetify -->
<!-- signatures: fullsetify(a) -->
### Function: fullsetify (a)

Si *a* es una lista, sustituye el operador de lista por el
de conjunto, aplicando posteriormente `fullsetify` a todos
los elementos que son a su vez conjuntos.
Si *a* no es una lista, se devuelve sin cambio alguno.


La función `setify` sustituye solamente el operador principal.


Ejemplos:


En la salida `(%o2)` el argumento de `f` no se convierte en
conjunto porque el operador principal de `f([b])` no es una lista.







```maxima
(%i1) fullsetify ([a, [a]]);
(%o1)                       {a, {a}}
(%i2) fullsetify ([a, f([b])]);
(%o2)                      {a, f([b])}
```

<!-- category: Other -->
<!-- keywords: identity -->
<!-- signatures: identity(x) -->
### Function: identity (x)

La función `identity` devuelve su argumento cualquiera que sea éste.


Ejemplos:


La función `identity` puede utilizarse como predicado cuando
los argumentos ya son valores booleanos.






```maxima
(%i1) every (identity, [true, true]);
(%o1)                         true
```

<!-- category: Other -->
<!-- keywords: integer_partitions -->
<!-- signatures: integer_partitions(n), integer_partitions(n, len) -->
### Function: integer_partitions (n)

Devuelve particiones enteras de *n*, esto es,
listas de enteros cuyas sumas son *n*.


La sentencia `integer_partitions(n)`
devuelve el conjunto de todas las particiones del entero *n*.
Cada partición es una lista ordenada de mayor a menor.


La sentencia `integer_partitions(n, len)`
devuelve todas las particiones de longitud *len* o menor;
en este caso, se añaden ceros a cada partición con menos
de *len* términos para que todas ellas sean de longitud
*len*. Las particiones son listas ordenadas de mayor a menor.


Una lista $[a_1, ..., a_m]$ es una partición de un entero no
negativo $n$ si (1) cada $a_i$ es entero no nulo y (2)
$a_1 + ... + a_m = n.$ Así, 0 no tiene particiones.


Ejemplos:











```maxima
(%i1) integer_partitions (3);
(%o1)               {[1, 1, 1], [2, 1], [3]}
(%i2) s: integer_partitions (25)$
(%i3) cardinality (s);
(%o3)                         1958
(%i4) map (lambda ([x], apply ("+", x)), s);
(%o4)                         {25}
(%i5) integer_partitions (5, 3);
(%o5) {[2, 2, 1], [3, 1, 1], [3, 2, 0], [4, 1, 0], [5, 0, 0]}
(%i6) integer_partitions (5, 2);
(%o6)               {[3, 2], [4, 1], [5, 0]}
```


Para encontrar todas las particiones que satisfagan cierta
condición, utilícese la función `subset`;
he aquí un ejemplo que encuentra todas las
particiones de 10 formadas por números primos.









```maxima
(%i1) s: integer_partitions (10)$
(%i2) cardinality (s);
(%o2)                          42
(%i3) xprimep(x) := integerp(x) and (x > 1) and primep(x)$
(%i4) subset (s, lambda ([x], every (xprimep, x)));
(%o4) {[2, 2, 2, 2, 2], [3, 3, 2, 2], [5, 3, 2], [5, 5], [7, 3]}
```

<!-- category: Other -->
<!-- keywords: intersect -->
<!-- signatures: intersect(a_1, ..., a_n) -->
### Function: intersect (a_1, ..., a_n)

Es una forma abreviada de la función `intersection`.

<!-- category: Other -->
<!-- keywords: intersection -->
<!-- signatures: intersection(a_1, ..., a_n) -->
### Function: intersection (a_1, ..., a_n)

Devuelve el conjunto de todos los elementos que son
comunes a los conjuntos  *a_1* a *a_n*.


Emite un mensaje de error en caso de que cualquiera de los 
*a_i* no sea un conjunto.


Ejemplos:













```maxima
(%i1) S_1 : {a, b, c, d};
(%o1)                     {a, b, c, d}
(%i2) S_2 : {d, e, f, g};
(%o2)                     {d, e, f, g}
(%i3) S_3 : {c, d, e, f};
(%o3)                     {c, d, e, f}
(%i4) S_4 : {u, v, w};
(%o4)                       {u, v, w}
(%i5) intersection (S_1, S_2);
(%o5)                          {d}
(%i6) intersection (S_2, S_3);
(%o6)                       {d, e, f}
(%i7) intersection (S_1, S_2, S_3);
(%o7)                          {d}
(%i8) intersection (S_1, S_2, S_3, S_4);
(%o8)                          {}
```

<!-- category: Other -->
<!-- keywords: kron_delta -->
<!-- signatures: kron_delta(x1, y1, ..., xp, yp) -->
### Function: kron_delta (x1, y1, ..., xp, yp)

Es la función delta de Kronecker.


La función `kron_delta` devuelve 1 cuando *xi* y
*yi* son iguales para todos los pares, devolviendo 0 si existe
un par en el que *xi* y *yi* no sean iguales. La igualdad
se determina utilizando `is(equal(xi,xj))` y la desigualdad
con `is(notequal(xi,xj))`. En caso de un solo argumento,
`kron_delta` devuelve un mensaje de error.


Ejemplos:










```maxima
(%i1) kron_delta(a,a);
(%o1)                                  1
(%i2) kron_delta(a,b,a,b);
(%o2)                          kron_delta(a, b)
(%i3) kron_delta(a,a,b,a+1);
(%o3)                                  0
(%i4) assume(equal(x,y));
(%o4)                            [equal(x, y)]
(%i5) kron_delta(x,y);
(%o5)                                  1
```

<!-- category: Other -->
<!-- keywords: listify -->
<!-- signatures: listify(a) -->
### Function: listify (a)

Si *a* es un conjunto, devuelve una lista con los elementos de *a*;
si  *a* no es un conjunto, devuelve *a*.


La función `full_listify` sustituye todos los operadores
de conjunto en *a* por operadores de lista.


Ejemplos:







```maxima
(%i1) listify ({a, b, c, d});
(%o1)                     [a, b, c, d]
(%i2) listify (F ({a, b, c, d}));
(%o2)                    F({a, b, c, d})
```

<!-- category: Other -->
<!-- keywords: lreduce -->
<!-- signatures: lreduce(f, s), lreduce(f, s, init) -->
### Function: lreduce (f, s)

Amplía la función binaria *F* a n-aria mediante
composición, siendo *s* una lista.


La sentencia  `lreduce(F, s)` devuelve
`F(... F(F(s_1, s_2), s_3), ... s_n)`.
Si se incluye el argumento opcional *s_0*,
el resultado equivale a `lreduce(F, cons(s_0, s))`.


La función *F* se aplica primero a los elementos del
extremo izquierdo de la lista, de ahí el nombre
`lreduce`, (*left reduce*).


Véanse también `rreduce`, `xreduce` y `tree_reduce`.


Ejemplos:


La función `lreduce` sin el argumento opcional,







```maxima
(%i1) lreduce (f, [1, 2, 3]);
(%o1)                     f(f(1, 2), 3)
(%i2) lreduce (f, [1, 2, 3, 4]);
(%o2)                  f(f(f(1, 2), 3), 4)
```


La función `lreduce` con el argumento opcional,






```maxima
(%i1) lreduce (f, [1, 2, 3], 4);
(%o1)                  f(f(f(4, 1), 2), 3)
```


La función `lreduce` aplicada a operadores binarios de Maxima.
El símbolo `/` es el operador división.







```maxima
(%i1) lreduce ("^", args ({a, b, c, d}));
                               b c d
(%o1)                       ((a ) )
(%i2) lreduce ("/", args ({a, b, c, d}));
                                a
(%o2)                         -----
                              b c d
```

<!-- category: Other -->
<!-- keywords: makeset -->
<!-- signatures: makeset(expr, x, s) -->
### Function: makeset (expr, x, s)

Genera un conjunto cuyos miembros se generan a partir de la
expresión *expr*, siendo *x* una lista de variables de
*expr* y *s* un conjunto o lista de listas.
Para generar los elementos del conjunto, se evalúa *expr*
asignando a las variables de *x* los elementos de *s*
en paralelo.


Los elementos de *s* deben tener la misma longitud que *x*.
La lista de variables *x* debe ser una lista de símbolos
sin subíndices. Cuando se trate de un único símbolo,
*x* debe expresarse como una lista de un elemento y cada elemento de *s*
debe ser una lista de un sólo elemento.






Véase también `makelist`.


Ejemplos:










```maxima
(%i1) makeset (i/j, [i, j], [[1, a], [2, b], [3, c], [4, d]]);
                           1  2  3  4
(%o1)                     {-, -, -, -}
                           a  b  c  d
(%i2) S : {x, y, z}$
(%i3) S3 : cartesian_product (S, S, S);
(%o3) {[x, x, x], [x, x, y], [x, x, z], [x, y, x], [x, y, y], 
[x, y, z], [x, z, x], [x, z, y], [x, z, z], [y, x, x], 
[y, x, y], [y, x, z], [y, y, x], [y, y, y], [y, y, z], 
[y, z, x], [y, z, y], [y, z, z], [z, x, x], [z, x, y], 
[z, x, z], [z, y, x], [z, y, y], [z, y, z], [z, z, x], 
[z, z, y], [z, z, z]}
(%i4) makeset (i + j + k, [i, j, k], S3);
(%o4) {3 x, 3 y, y + 2 x, 2 y + x, 3 z, z + 2 x, z + y + x, 
                                       z + 2 y, 2 z + x, 2 z + y}
(%i5) makeset (sin(x), [x], {[1], [2], [3]});
(%o5)               {sin(1), sin(2), sin(3)}
```

<!-- category: Other -->
<!-- keywords: moebius -->
<!-- signatures: moebius(n) -->
### Function: moebius (n)

Representa la función de Moebius.


Si *n* es el producto de $k$ números primos diferentes,
`moebius(n)` devuelve $(-1)^k$, retornando 1 si 
$n = 1$ y 0 para cualesquiera otros enteros positivos.



La función de Moebius se distribuye respecto de ecuaciones,
listas, matrices y conjuntos.


Ejemplos:














```maxima
(%i1) moebius (1);
(%o1)                           1
(%i2) moebius (2 * 3 * 5);
(%o2)                          - 1
(%i3) moebius (11 * 17 * 29 * 31);
(%o3)                           1
(%i4) moebius (2^32);
(%o4)                           0
(%i5) moebius (n);
(%o5)                      moebius(n)
(%i6) moebius (n = 12);
(%o6)                    moebius(n) = 0
(%i7) moebius ([11, 11 * 13, 11 * 13 * 15]);
(%o7)                      [- 1, 1, 1]
(%i8) moebius (matrix ([11, 12], [13, 14]));
                           [ - 1  0 ]
(%o8)                      [        ]
                           [ - 1  1 ]
(%i9) moebius ({21, 22, 23, 24});
(%o9)                      {- 1, 0, 1}
```

<!-- category: Other -->
<!-- keywords: multinomial_coeff -->
<!-- signatures: multinomial_coeff(a_1, ..., a_n), multinomial_coeff() -->
### Function: multinomial_coeff (a_1, ..., a_n)

Calcula el coeficiente multinomial.


Si todos los *a_k* son enteros no negativos, el coeficiente multinomial
es el número de formas de colocar  `a_1 + ... + a_n`
objetos diferentes en  $n$ cajas con *a_k* elementos en la
$k$-ésima caja. En general,
`multinomial_coeff (a_1, ..., a_n)` calcula
`(a_1 + ... + a_n)!/(a_1! ... a_n!)`.


Si no se dan argumentos, `multinomial_coeff()` devuelve 1.


Se puede usar `minfactorial` para simplificar el valor
devuelto por `multinomial_coeff`.


Ejemplos:









```maxima
(%i1) multinomial_coeff (1, 2, x);
                            (x + 3)!
(%o1)                       --------
                              2 x!
(%i2) minfactorial (%);
                     (x + 1) (x + 2) (x + 3)
(%o2)                -----------------------
                                2
(%i3) multinomial_coeff (-6, 2);
                             (- 4)!
(%o3)                       --------
                            2 (- 6)!
(%i4) minfactorial (%);
(%o4)                          10
```

<!-- category: Other -->
<!-- keywords: num_distinct_partitions -->
<!-- signatures: num_distinct_partitions(n), num_distinct_partitions(n, list) -->
### Function: num_distinct_partitions (n)

Si *n* es un entero no negativo, devuelve el número de
particiones enteras distintas de *n*, en caso contrario
`num_distinct_partitions` devuelve una forma nominal.


La sentencia `num_distinct_partitions(n, list)`
devuelve una lista con el número de particiones distintas
de 1, 2, 3, ..., *n*.


Una partición distinta de *n* es una lista de números
enteros positivos distintos $k_1$, ..., $k_m$
tales que $n = k_1 + ... + k_m$.


Ejemplos:








```maxima
(%i1) num_distinct_partitions (12);
(%o1)                          15
(%i2) num_distinct_partitions (12, list);
(%o2)      [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15]
(%i3) num_distinct_partitions (n);
(%o3)              num_distinct_partitions(n)
```

<!-- category: Other -->
<!-- keywords: num_partitions -->
<!-- signatures: num_partitions(n), num_partitions(n, list) -->
### Function: num_partitions (n)

Si *n* es un entero no negativo, devuelve el número de
particiones enteras de *n*, en caso contrario `num_partitions`
devuelve una expresión nominal.


La sentencia `num_partitions(n, list)` devuelve una lista
con los números de particiones enteras de 1, 2, 3, ..., *n*.


Siendo *n* un entero no negativo, `num_partitions(n)`
es igual a `cardinality(integer_partitions(n))`; sin
embargo, `num_partitions` no construye el conjunto de 
particiones, por lo que es más rápido.


Ejemplos:








```maxima
(%i1) num_partitions (5) = cardinality (integer_partitions (5));
(%o1)                         7 = 7
(%i2) num_partitions (8, list);
(%o2)            [1, 1, 2, 3, 5, 7, 11, 15, 22]
(%i3) num_partitions (n);
(%o3)                   num_partitions(n)
```

<!-- category: Other -->
<!-- keywords: partition_set -->
<!-- signatures: partition_set(a, f) -->
### Function: partition_set (a, f)

Particiona el conjunto *a* respecto del predicado *f*.


La función `partition_set` devuelve una lista con dos conjuntos;
el primer conjunto es el subconjunto de *a* para el cual el predicado
*f* devuelve `false` y el segundo contiene al resto de elementos de *a*.


La función `partition_set` no aplica `is` al valor devuelto
por *f*.


La función `partition_set` emite un mensaje de error si *a*
no es un conjunto literal.


Véase también `subset`.


Ejemplos:








```maxima
(%i1) partition_set ({2, 7, 1, 8, 2, 8}, evenp);
(%o1)                   [{1, 7}, {2, 8}]
(%i2) partition_set ({x, rat(y), rat(y) + z, 1},
                  lambda ([x], ratp(x)));
(%o2)/R/              [{1, x}, {y, y + z}]
```

<!-- category: Other -->
<!-- keywords: permutations -->
<!-- signatures: permutations(a) -->
### Function: permutations (a)

Devuelve un conjunto con todas las permutaciones distintas
de los miembros de la lista o conjunto  *a*. Cada permutación
es una lista, no un conjunto.


Si *a* es una lista, sus miembros duplicados no son eliminados
antes de buscar sus permutaciones.


Si *a* no es una lista o conjunto, `permutations` emite
un mensaje de error.


Véase también `random_permutation`.


Ejemplos:







```maxima
(%i1) permutations ([a, a]);
(%o1)                       {[a, a]}
(%i2) permutations ([a, a, b]);
(%o2)           {[a, a, b], [a, b, a], [b, a, a]}
```

<!-- category: Other -->
<!-- keywords: powerset -->
<!-- signatures: powerset(a), powerset(a, n) -->
### Function: powerset (a)

Devuelve el conjunto de todos los subconjuntos del conjunto *a*
o un sunconjunto de ellos.


La sentencia `powerset(a)` devuelve el conjunto de todos
los subconjuntos de *a*, que contendrá `2^cardinality(a)`
elementos.


La sentencia `powerset(a, n)` devuelve el conjunto de todos
los subconjuntos de *a* de cardinalidad *n*.


La función `powerset` emite un mensaje de error si *a* no
es un conjunto literal o si *n* no es un entero no negativo.


Ejemplos:











```maxima
(%i1) powerset ({a, b, c});
(%o1) {{}, {a}, {a, b}, {a, b, c}, {a, c}, {b}, {b, c}, {c}}
(%i2) powerset ({w, x, y, z}, 4);
(%o2)                    {{w, x, y, z}}
(%i3) powerset ({w, x, y, z}, 3);
(%o3)     {{w, x, y}, {w, x, z}, {w, y, z}, {x, y, z}}
(%i4) powerset ({w, x, y, z}, 2);
(%o4)   {{w, x}, {w, y}, {w, z}, {x, y}, {x, z}, {y, z}}
(%i5) powerset ({w, x, y, z}, 1);
(%o5)                 {{w}, {x}, {y}, {z}}
(%i6) powerset ({w, x, y, z}, 0);
(%o6)                         {{}}
```

<!-- category: Other -->
<!-- keywords: random_permutation -->
<!-- signatures: random_permutation(a) -->
### Function: random_permutation (a)

Devuelve una permutación aleatoria del conjunto o lista
*a*, siguiendo el algoritmo de Knuth.


El valor devuelto es una lista nueva distinta del argumento,
incluso cuando todos los elementos son iguales. Sin embargo,
los elementos del argumento no se copian.


Ejemplos:









```maxima
(%i1) random_permutation ([a, b, c, 1, 2, 3]);
(%o1)                  [c, 1, 2, 3, a, b]
(%i2) random_permutation ([a, b, c, 1, 2, 3]);
(%o2)                  [b, 3, 1, c, a, 2]
(%i3) random_permutation ({x + 1, y + 2, z + 3});
(%o3)                 [y + 2, z + 3, x + 1]
(%i4) random_permutation ({x + 1, y + 2, z + 3});
(%o4)                 [x + 1, y + 2, z + 3]
```

<!-- category: Other -->
<!-- keywords: rreduce -->
<!-- signatures: rreduce(f, s), rreduce(f, s, init) -->
### Function: rreduce (f, s)

Amplía la función binaria *F* a n-aria mediante
composición, siendo *s* una lista.


La sentencia  `rreduce(F, s)` devuelve
`F(s_1, ... F(s_{n - 2}, F(s_{n - 1}, s_n)))`.
Si se incluye el argumento opcional *s_{n + 1}*,
el resultado equivale a `rreduce(F, endcons(s_{n + 1}, s))`.


La función *F* se aplica primero a los elementos del
extremo derecho de la lista, de ahí el nombre
`rreduce`, (*right reduce*).


Véanse también `lreduce`, `xreduce` y `tree_reduce`.


Ejemplos:


La función `rreduce` sin el argumento opcional,







```maxima
(%i1) rreduce (f, [1, 2, 3]);
(%o1)                     f(1, f(2, 3))
(%i2) rreduce (f, [1, 2, 3, 4]);
(%o2)                  f(1, f(2, f(3, 4)))
```


La función `rreduce` con el argumento opcional,






```maxima
(%i1) rreduce (f, [1, 2, 3], 4);
(%o1)                  f(1, f(2, f(3, 4)))
```


La función `rreduce` aplicada a operadores binarios de Maxima.
El símbolo `/` es el operador división.







```maxima
(%i1) rreduce ("^", args ({a, b, c, d}));
                                 d
                                c
                               b
(%o1)                         a
(%i2) rreduce ("/", args ({a, b, c, d}));
                               a c
(%o2)                          ---
                               b d
```

<!-- category: Other -->
<!-- keywords: set_partitions -->
<!-- signatures: set_partitions(a), set_partitions(a, n) -->
### Function: set_partitions (a)

Devuelve el conjunto de todas las particiones de *a* o
un subconjunto de ellas.


La sentencia `set_partitions(a, n)`
devuelve un conjunto con todas las descomposiciones de *a*
en *n* conjuntos no vacíos disjuntos.


La sentencia `set_partitions(a)` devuelve el
conjunto de todas las particiones.


La función `stirling2` devuelve la cardinalidad del conjunto
de las particiones de un conjunto.


Se dice que un conjunto $P$ es una partición del conjunto $S$ si verifica



1. cada elemento de $P$ es un conjunto no vacío,
2. los elementos de $P$ son disjuntos,
3. la unión de los elementos de $P$ es igual a  $S$.


Ejemplos:


El conjunto vacío forma una partición de sí mismo,






```maxima
(%i1) set_partitions ({});
(%o1)                         {{}}
```


La cardinalidad del conjunto de particiones de un conjunto puede calcularse con `stirling2`,








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) cardinality(p) = stirling2 (6, 3);
(%o3)                        90 = 90
```


Cada elemento de `p` debería tener *n* = 3 miembros,








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (cardinality, p);
(%o3)                          {3}
```


Por último, para cada miembro de `p`, la unión de sus elementos
debe ser igual a `s`,








```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (lambda ([x], apply (union, listify (x))), p);
(%o3)                 {{0, 1, 2, 3, 4, 5}}
```

<!-- category: Other -->
<!-- keywords: setdifference -->
<!-- signatures: setdifference(a, b) -->
### Function: setdifference (a, b)

Devuelve el conjunto con los elementos del conjunto *a* que
no pertenecen al conjunto *b*.


La función `setdifference` emite un mensaje de error si
*a* o *b* no son conjuntos.


Ejemplos:












```maxima
(%i1) S_1 : {a, b, c, x, y, z};
(%o1)                  {a, b, c, x, y, z}
(%i2) S_2 : {aa, bb, c, x, y, zz};
(%o2)                 {aa, bb, c, x, y, zz}
(%i3) setdifference (S_1, S_2);
(%o3)                       {a, b, z}
(%i4) setdifference (S_2, S_1);
(%o4)                     {aa, bb, zz}
(%i5) setdifference (S_1, S_1);
(%o5)                          {}
(%i6) setdifference (S_1, {});
(%o6)                  {a, b, c, x, y, z}
(%i7) setdifference ({}, S_1);
(%o7)                          {}
```

<!-- category: Other -->
<!-- keywords: setequalp -->
<!-- signatures: setequalp(a, b) -->
### Function: setequalp (a, b)

Devuelve  `true` si los conjuntos *a* y *b* tienen
el mismo número de elementos


y `is (x = y)` vale `true`
para `x` perteneciente a *a*
e `y` perteneciente a *b*,
considerados en el orden que determina la función 
`listify`. En caso contrario, `setequalp`
devuelve `false`.


Ejemplos:








```maxima
(%i1) setequalp ({1, 2, 3}, {1, 2, 3});
(%o1)                         true
(%i2) setequalp ({a, b, c}, {1, 2, 3});
(%o2)                         false
(%i3) setequalp ({x^2 - y^2}, {(x + y) * (x - y)});
(%o3)                         false
```

<!-- category: Other -->
<!-- keywords: setify -->
<!-- signatures: setify(a) -->
### Function: setify (a)

Construye un conjunto con los miembros de la lista *a*.
Los elementos duplicados de la lista *a* son borrados
y ordenados de acuerdo con el predicado `orderlessp`.


La función `setify` emite un mensaje de error si
*a* no es un conjunto literal.


Ejemplos:








```maxima
(%i1) setify ([1, 2, 3, a, b, c]);
(%o1)                  {1, 2, 3, a, b, c}
(%i2) setify ([a, b, c, a, b, c]);
(%o2)                       {a, b, c}
(%i3) setify ([7, 13, 11, 1, 3, 9, 5]);
(%o3)                {1, 3, 5, 7, 9, 11, 13}
```

<!-- category: Other -->
<!-- keywords: setp -->
<!-- signatures: setp(a) -->
### Function: setp (a)

Devuelve `true` si y sólo si *a* es un conjunto de Maxima.


La función `setp` devuelve `true` tanto cuando el conjunto
tiene como cuando no tiene elementos repetidos.



La función `setp` is equivalent to the Maxima function
`setp(a) := not atom(a) and op(a) = 'set`.


Ejemplos:








```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) {a, a, a};
(%o2)                       {a, a, a}
(%i3) setp (%);
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: some -->
<!-- signatures: some(f, a), some(f, L_1, ..., L_n) -->
### Function: some (f, a)

Devuelve `true` si el predicado *f* devuelve `true`
para al menos uno de sus argumentos.
Si el segundo argumento es un conjunto, `some (f, a)`
devuelve `true` si `f(a_i)` devuelve también
`true` para alguno de los *a_i* en *a*; puede ser que
`some` no evalúe *f* para todos los *a_i* de *s*.
Puesto que los conjuntos no están ordenados, `some` puede evaluar
`f(a_i)` en cualquier orden.


Dada una o más listas como argumentos,
`some (f, L_1, ..., L_n)` devuelve `true`
si `f(x_1, ..., x_n)` devuelve también
`true` para al menos un  *x_1*, ..., *x_n* de
*L_1*, ..., *L_n*, respectivamente; puede ser que
`some` no evalúe *f* para todos las combinaciones
*x_1*, ..., *x_n*. La función `some` evalúa
las listas en el orden creciente de su índice


Dado un conjunto vacío `{}` o una lista
vacía como argumentos, `some` devuelve `false`.


Si la variable global `maperror` vale `true`,
todas las listas *L_1*, ..., *L_n* deben tener
igual número de elementos. Si `maperror` vale
`false`, los argumentos se truncan para tener todos
el número de elementos de la lista más corta. 


Los valores que devuelve el predicado *f* cuando toman 
(mediante `is`) un valor diferente a `true` y `false`
se controlan con la variable global `prederror`.
Si `prederror` vale `true`, tales valores se
consideran como `false`.
Si `prederror` vale `false`, tales valores se
consideran como desconocidos (`unknown`).


Ejemplos:


La función `some` aplicada a un único conjunto.
El predicado es una función de un argumento,







```maxima
(%i1) some (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) some (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         true
```


La función `some` aplicada a dos listas.
El predicado es una función de dos argumentos,







```maxima
(%i1) some ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) some ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Las respuestas del predicado *f* que se evalúan 
a cualquier cosa diferente de `true` y `false`
están controlados por la variable global `prederror`.













```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
                     [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o4)                         true
(%i5) prederror : true;
(%o5)                         true
(%i6) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o6)                         false
(%i7) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o7)                         true
```

<!-- category: Other -->
<!-- keywords: stirling1 -->
<!-- signatures: stirling1(n, m) -->
### Function: stirling1 (n, m)

Es el número de Stirling de primera especie.


Si tanto *n* como *m* son enteros no negativos,
el valor que toma `stirling1 (n, m)`
es el número de permutaciones de un conjunto de
*n* elementos con *m* ciclos. Para más detalles,
véase Graham, Knuth and Patashnik *Concrete Mathematics*.
Maxima utiliza una relación recursiva para definir
`stirling1 (n, m)` para *m* menor
que 0; no está definida para *n* menor que 0 ni
para argumentos no enteros.


La función `stirling1` es simplificadora. Maxima
reconoce las siguientes identidades:




1. $stirling1(0, n) = kron_delta(0, n)$ (Ref. [1])
2. $stirling1(n, n) = 1$ (Ref. [1])
3. $stirling1(n, n - 1) = binomial(n, 2)$ (Ref. [1])
4. $stirling1(n + 1, 0) = 0$ (Ref. [1])
5. $stirling1(n + 1, 1) = n!$ (Ref. [1])
6. $stirling1(n + 1, 2) = 2^n - 1$ (Ref. [1])


Estas identidades se aplican cuando los argumentos son enteros
literales o símbolos declarados como enteros y
el primer argumento es no negativo. La función `stirling1`
no simplifica para argumentos no enteros.


Referencias:


[1] Donald Knuth, *The Art of Computer Programming,*
Tercera Edición, Volumen 1, Sección 1.2.6, Ecuaciones 48, 49 y 50.


Ejemplos:








```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n, n);
(%o3)                           1
```


La función `stirling1` no simplifica en caso de argumentos no enteros,






```maxima
(%i1) stirling1 (sqrt(2), sqrt(2));
(%o1)              stirling1(sqrt(2), sqrt(2))
```


Maxima aplicas algunas identidades a `stirling1`,









```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n + 1, n);
                            n (n + 1)
(%o3)                       ---------
                                2
(%i4) stirling1 (n + 1, 1);
(%o4)                          n!
```

<!-- category: Other -->
<!-- keywords: stirling2 -->
<!-- signatures: stirling2(n, m) -->
### Function: stirling2 (n, m)

Es el número de Stirling de segunda especie.


Si *n* y *m* son enteros no negativos,
`stirling2 (n, m)` es el número
de formas en las que se puede particionar un conjunto
de cardinal *n* en *m* subconjuntos disjuntos.
Maxima utiliza una relación recursiva para definir
`stirling2 (n, m)` con *m* menor
que 0; la función no está definida para  *n*
menor que 0  ni para argumentos no enteros.


La función `stirling2` es simplificadora. Maxima
reconoce las siguientes identidades:




1. $stirling2(0, n) = kron_delta(0, n)$ (Ref. [1])
2. $stirling2(n, n) = 1$ (Ref. [1])
3. $stirling2(n, n - 1) = binomial(n, 2)$ (Ref. [1])
4. $stirling2(n + 1, 1) = 1$ (Ref. [1])
5. $stirling2(n + 1, 2) = 2^n - 1$ (Ref. [1])
6. $stirling2(n, 0) = kron_delta(n, 0)$ (Ref. [2])
7. $stirling2(n, m) = 0$ when $m > n$ (Ref. [2])
8. $stirling2(n, m) = sum((-1)^(m - k) binomial(m k) k^n,i,1,m) / m!$
si $m$ y $n$ son enteros y $n$ no negativo. (Ref. [3])


Estas identidades se aplican cuando los argumentos son enteros
literales o símbolos declarados como enteros y
el primer argumento es no negativo. La función `stirling2`
no simplifica para argumentos no enteros.


Referencias:


[1] Donald Knuth. *The Art of Computer Programming*,
Tercera Edición, Volumen 1, Sección 1.2.6, Ecuaciones 48, 49 y 50.


[2] Graham, Knuth y Patashnik. *Concrete Mathematics*, Tabla 264.


[3] Abramowitz y Stegun. *Handbook of Mathematical Functions*, Sección 24.1.4.


Ejemplos:








```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n, n);
(%o3)                           1
```


La función `stirling2` no simplifica en caso de argumentos no enteros,






```maxima
(%i1) stirling2 (%pi, %pi);
(%o1)                  stirling2(%pi, %pi)
```


Maxima aplicas algunas identidades a `stirling2`,









```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n + 9, n + 8);
                         (n + 8) (n + 9)
(%o3)                    ---------------
                                2
(%i4) stirling2 (n + 1, 2);
                              n
(%o4)                        2  - 1
```

<!-- category: Other -->
<!-- keywords: subset -->
<!-- signatures: subset(a, f) -->
### Function: subset (a, f)

Devuelve el subconjunto del conjunto *a* que satisface el predicado *f*.


La función `subset` devuelve el conjunto que contiene a los
elementos de *a* para los cuales *f* devuelve un resultado
diferente de `false`. La función `subset` no aplica
`is` al valor retornado por *f*.


La función `subset` emite un mensaje de error si *a*
no es un conjunto literal.


Véase también `partition_set`.


Ejemplos:







```maxima
(%i1) subset ({1, 2, x, x + y, z, x + y + z}, atom);
(%o1)                     {1, 2, x, z}
(%i2) subset ({1, 2, 7, 8, 9, 14}, evenp);
(%o2)                      {2, 8, 14}
```

<!-- category: Other -->
<!-- keywords: subsetp -->
<!-- signatures: subsetp(a, b) -->
### Function: subsetp (a, b)

Devuelve `true` si y sólo si el conjunto *a* es un subconjunto de *b*.


La función `subsetp` emite un mensaje de error si
cualesquiera *a* o *b* no es un conjunto literal.


Ejemplos:







```maxima
(%i1) subsetp ({1, 2, 3}, {a, 1, b, 2, c, 3});
(%o1)                         true
(%i2) subsetp ({a, 1, b, 2, c, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: symmdifference -->
<!-- signatures: symmdifference(a_1, ..., a_n) -->
### Function: symmdifference (a_1, ..., a_n)

Devuelve la diferencia simétrica de los conjuntos `a_1, ..., a_n`.


Dados dos argumentos, `symmdifference (a, b)` equivale a
`union (setdifference (a, b), setdifference (b, a))`.


La función `symmdifference` emite un mensaje de error si alguno de
su argumentos no es un conjunto literal.


Ejemplos:













```maxima
(%i1) S_1 : {a, b, c};
(%o1)                       {a, b, c}
(%i2) S_2 : {1, b, c};
(%o2)                       {1, b, c}
(%i3) S_3 : {a, b, z};
(%o3)                       {a, b, z}
(%i4) symmdifference ();
(%o4)                          {}
(%i5) symmdifference (S_1);
(%o5)                       {a, b, c}
(%i6) symmdifference (S_1, S_2);
(%o6)                        {1, a}
(%i7) symmdifference (S_1, S_2, S_3);
(%o7)                       {1, b, z}
(%i8) symmdifference ({}, S_1, S_2, S_3);
(%o8)                       {1,b, z}
```

<!-- category: Other -->
<!-- keywords: tree_reduce -->
<!-- signatures: tree_reduce(F, s), tree_reduce(F, s, s_0) -->
### Function: tree_reduce (F, s)

Amplía la función binaria *F* a n-aria, siendo *s* una lista.


La función `tree_reduce` equivale a lo suguiente:
Aplicar *F* a pares sucesivos de elementos para formar
una nueva lista `[F(s_1, s_2), F(s_3, s_4), ...]`,
llevando el elemento final sin cambiar si el número de elementos es impar;
después repetir hasta que la lista se reduzca a un único elemento,
que es el valor de retorno.


Cuando está presente el argumento opcional *s_0*,
el resultado equivale a `tree_reduce(F, cons(s_0, s)`.


Para la suma de números decimales en coma flotante,
`tree_reduce` puede devolver una suma que tenga un error
de redondeo menor que el conseguido por `rreduce` o `lreduce`.


Los elementos de *s* y los resultados parciales pueden colocarse
en un árbol binario de mínima profundidad, de ahí
el nombre de *tree_reduce*.


Ejemplos:


La función `tree_reduce` aplicada a una lista con un número
par de elementos,






```maxima
(%i1) tree_reduce (f, [a, b, c, d]);
(%o1)                  f(f(a, b), f(c, d))
```


La función `tree_reduce` aplicada a una lista con un número
impar de elementos,






```maxima
(%i1) tree_reduce (f, [a, b, c, d, e]);
(%o1)               f(f(f(a, b), f(c, d)), e)
```

<!-- category: Other -->
<!-- keywords: union -->
<!-- signatures: union(a_1, ..., a_n) -->
### Function: union (a_1, ..., a_n)

Devuelve la unión de los conjuntos *a_1* hasta *a_n*.


La sentencia `union()` (sin argumentos) devuelve el
conjunto vacío.


La función `union` emite un mensaje de error si alguno
de sus argumentos no es un conjunto literal.


Ejemplos:













```maxima
(%i1) S_1 : {a, b, c + d, %e};
(%o1)                   {%e, a, b, d + c}
(%i2) S_2 : {%pi, %i, %e, c + d};
(%o2)                 {%e, %i, %pi, d + c}
(%i3) S_3 : {17, 29, 1729, %pi, %i};
(%o3)                {17, 29, 1729, %i, %pi}
(%i4) union ();
(%o4)                          {}
(%i5) union (S_1);
(%o5)                   {%e, a, b, d + c}
(%i6) union (S_1, S_2);
(%o6)              {%e, %i, %pi, a, b, d + c}
(%i7) union (S_1, S_2, S_3);
(%o7)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
(%i8) union ({}, S_1, S_2, S_3);
(%o8)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
```

<!-- category: Other -->
<!-- keywords: xreduce -->
<!-- signatures: xreduce(F, s), xreduce(F, s, s_0) -->
### Function: xreduce (F, s)

Amplía la función *F* a n-aria mediante
composición; si *F* ya es n-aria, aplica *F* a *s*.
Si *F* no es n-aria, `xreduce` equivale a `lreduce`.
El argumento *s* debe ser una lista.


Funciones n-arias reconocidas por Maxima son la suma `+`, la
multiplicación `*`, `and`, `or`, `max`,
`min` y `append`. Las funciones también se pueden
declarar n-arias mediante `declare(F, nary)`;
para estas funciones, `xreduce` será más rápida que
`rreduce` o `lreduce`.


Cuando está presente el argumento opcional *s_0*,
el resultado equivale a `xreduce(s, cons(s_0, s))`.


La suma de números decimales en coma flotante no es exactamente asociativa;
aún así, `xreduce` aplica la suma n-aria cuando *s*
contiene números en coma flotante.


Ejemplos:


La función `xreduce` aplicada a una función n-aria;
`F` es invocada una sóla vez, con todos sus argumentos,








```maxima
(%i1) declare (F, nary);
(%o1)                         done
(%i2) F ([L]) := L;
(%o2)                      F([L]) := L
(%i3) xreduce (F, [a, b, c, d, e]);
(%o3)         [[[[[("[", simp), a], b], c], d], e]
```


La función `xreduce` aplicada a una función que se desconoce si
es n-aria; `G` es invocada varias veces, con dos argumentos de cada vez,








```maxima
(%i1) G ([L]) := L;
(%o1)                      G([L]) := L
(%i2) xreduce (G, [a, b, c, d, e]);
(%o2)         [[[[[("[", simp), a], b], c], d], e]
(%i3) lreduce (G, [a, b, c, d, e]);
(%o3)                 [[[[a, b], c], d], e]
```

