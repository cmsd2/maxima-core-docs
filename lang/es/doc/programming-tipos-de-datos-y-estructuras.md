## Tipos de datos y estructuras

<!-- category: Programming -->
<!-- keywords: %e -->
<!-- signatures: %e -->
### Variable: %e

El símbolo `%e` representa a la base de los logaritmos
naturales, también conocido como número de Euler. El valor numérico
de `%e` es el número decimal en coma flotante 2.718281828459045d0.

<!-- category: Programming -->
<!-- keywords: %gamma -->
<!-- signatures: %gamma -->
### Variable: %gamma

Es la constante de Euler-Mascheroni, 0.5772156649015329 ....

<!-- category: Programming -->
<!-- keywords: %i -->
<!-- signatures: %i -->
### Variable: %i

El símbolo `%i` representa la unidad imaginaria, $sqrt(- 1)$.

<!-- category: Programming -->
<!-- keywords: %phi -->
<!-- signatures: %phi -->
### Variable: %phi

El símbolo `%phi` representa a la llamada *razón áurea*,
$(1 + sqrt(5))/2$.
El valor numérico de `%phi` es el número decimal en coma flotante 1.618033988749895d0.


La función `fibtophi` expresa los números de Fibonacci `fib(n)` en
términos de `%phi`.


Por defecto, Maxima desconoce las propiedades algebraicas de `%phi`.
Tras evaluar `tellrat(%phi^2 - %phi - 1)` y `algebraic: true`,
`ratsimp` puede simplificar algunas expresiones que contengan `%phi`.


Ejemplos:


`fibtophi` expresa el número de Fibonacci `fib(n)` en términos de `%phi`.









```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1
(%i4) ratsimp (%);
(%o4)                           0
```


Por defecto, Maxima desconoce las propiedades algebraicas de `%phi`.
Después de evaluar `tellrat (%phi^2 - %phi - 1)` y
`algebraic: true`, `ratsimp` puede simplificar algunas expresiones
que contengan `%phi`.











```maxima
(%i1) e : expand ((%phi^2 - %phi - 1) * (A + 1));
                 2                      2
(%o1)        %phi  A - %phi A - A + %phi  - %phi - 1
(%i2) ratsimp (e);
                  2                     2
(%o2)        (%phi  - %phi - 1) A + %phi  - %phi - 1
(%i3) tellrat (%phi^2 - %phi - 1);
                            2
(%o3)                  [%phi  - %phi - 1]
(%i4) algebraic : true;
(%o4)                         true
(%i5) ratsimp (e);
(%o5)                           0
```

<!-- category: Programming -->
<!-- keywords: %pi -->
<!-- signatures: %pi -->
### Variable: %pi

El símbolo `%pi` representa la razón entre la longitud de
una circunferencia y su radio. 
El valor numérico de `%pi` es el número decimal en coma flotante 3.141592653589793d0.

<!-- category: Programming -->
<!-- keywords: [, ] -->
<!-- signatures: ] -->
### Variable: [

`[` y `]` marcan, respectivamente, el comienzo y el final de una lista.


`[` y `]` también se utilizan para indicar los subíndices
de una lista o de un array.


Ejemplos:














```maxima
(%i1) x: [a, b, c];
(%o1)                       [a, b, c]


(%i2) x[3];
(%o2)                           c


(%i3) array (y, fixnum, 3);
(%o3)                           y


(%i4) y[2]: %pi;
(%o4)                          %pi


(%i5) y[2];
(%o5)                          %pi


(%i6) z['foo]: 'bar;
(%o6)                          bar


(%i7) z['foo];
(%o7)                          bar


(%i8) g[k] := 1/(k^2+1);
                                  1
(%o8)                     g  := ------
                           k     2
                                k  + 1


(%i9) g[10];
                                1
(%o9)                          ---
                               101
```

<!-- category: Programming -->
<!-- keywords: append -->
<!-- signatures: append(lista_1, ..., lista_n) -->
### Function: append (lista_1, ..., lista_n)

Devuelve una lista cuyos elementos son los de la lista *lista_1* seguidos de los de *lista_2*, ...  La función `append` también opera con expresiones generales, como la llamada `append (f(a,b), f(c,d,e));`, de la que se obtiene `f(a,b,c,d,e)`.


Tecléese `example(append);` para ver un ejemplo.

<!-- category: Programming -->
<!-- keywords: array -->
<!-- signatures: array(nombre, dim_1, ..., dim_n), array(nombre, type, dim_1, ..., dim_n), array([nombre_1, ..., nombre_m], dim_1, ..., dim_n) -->
### Function: array (nombre, dim_1, ..., dim_n)

Crea un array de dimensión $n$, que debe ser menor o igual que 5. Los subíndices de la $i$-ésima dimensión son enteros que toman valores entre 0 y *dim_i*.  


La llamada `array (nombre, dim_1, ..., dim_n)` crea un array de tipo general.


La llamada `array (nombre, type, dim_1, ..., dim_n)` crea un array con sus elementos del tipo especificado. El tipo *type* puede ser `fixnum` para enteros de tamaño limitado o `flonum` para números decimales en coma flotante.


La llamada `array ([nombre_1, ..., nombre_m], dim_1, ..., dim_n)`
crea $m$ arrays,  todos ellos de igual dimensión.




Si el usuario asigna un valor a una variable subindicada antes de declarar el array correspondiente, entonces se construye un array no declarado. Los arrays no declarados, también conocidos por el nombre de "arrays de claves" (hashed arrays), son más generales que los arrays declarados. El usuario no necesita declarar su tamaño máximo y pueden ir creciendo de forma dinámica. Los subíndices de los arrays no declarados no necesitan ser necesariamente números. Sin embargo, a menos que un array tenga sus elementos dispersos, probablemente sea más eficiente declararlo siempre que sea posible antes que dejarlo como no declarado. La función `array` puede utilizarse para transformar un array no declarado a a uno declarado.

<!-- category: Programming -->
<!-- keywords: arrayapply -->
<!-- signatures: arrayapply(A, [i_1, ..., i_n]) -->
### Function: arrayapply (A, [i_1, ..., i_n])

Evalúa `A [i_1, ..., i_n]`, donde *A* es un array y *i_1*, ..., *i_n* son enteros.


Esto es como `apply`, excepto por el hecho de que el primer argumento es un array en lugar de una función.

<!-- category: Programming -->
<!-- keywords: arrayinfo -->
<!-- signatures: arrayinfo(A) -->
### Function: arrayinfo (A)

Devuelve información sobre el array*A*.
El argumento *A* puede ser un array declarado o no declarado,
una función array o una función subindicada.


En el caso de arrays declarados, `arrayinfo` devuelve una
lista que contiene el átomo `declared`, el número de
dimensiones y el tamaño de cada dimensión.
Los elementos del array, tanto los que tienen valores
asignados como los que no, son devueltos por `listarray`.


En el caso de arrays no declarados (*hashed arrays*), `arrayinfo`
devuelve una lista que contiene el átomo `hashed`, el número
de subíndices y los subíndices de aquellos
elementos que guarden un valor. Los valores son devueltos por `listarray`.


En el caso de funciones array, `arrayinfo` devuelve una lista que 
contiene el átomo `hashed`, el número de subíndices
y los subíndices para los que la función tiene valores almacenados.
Los valores almacenados de la función array son devueltos por `listarray`.


En el caso de funciones subindicadas, `arrayinfo` devuelve una lista que
contiene el átomo `hashed`, el número de subíndices y
los subíndices para los que hay expresiones lambda.
Las expresiones lambda son devueltas por `listarray`.


Ejemplos:


`arrayinfo` y `listarray` aplicadas a una array declarado.










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa
(%i2) aa [2, 3] : %pi;
(%o2)                          %pi
(%i3) aa [1, 2] : %e;
(%o3)                          %e
(%i4) arrayinfo (aa);
(%o4)                 [declared, 2, [2, 3]]
(%i5) listarray (aa);
(%o5) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
```


`arrayinfo` y `listarray` aplicadas a una array no declarado (*hashed arrays*).









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)
(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)
(%i3) arrayinfo (bb);
(%o3)               [hashed, 1, [BAR], [FOO]]
(%i4) listarray (bb);
                              3         2
(%o4)                 [(c - d) , (b + a) ]
```


`arrayinfo` y `listarray` aplicadas a una función array.










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x
(%i2) cc [u, v];
                                v
(%o2)                           -
                                u
(%i3) cc [4, z];
                                z
(%o3)                           -
                                4
(%i4) arrayinfo (cc);
(%o4)              [hashed, 2, [4, z], [u, v]]
(%i5) listarray (cc);
                              z  v
(%o5)                        [-, -]
                              4  u
```


`arrayinfo` y `listarray` aplicadas a una función subindicada.










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x
(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )
(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )
(%i4) arrayinfo (dd);
(%o4)             [hashed, 1, [b + a], [v - u]]
(%i5) listarray (dd);
                         b + a                v - u
(%o5)      [lambda([y], y     ), lambda([y], y     )]
```

<!-- category: Programming -->
<!-- keywords: arraymake -->
<!-- signatures: arraymake(name, [i_1, ..., i_n]) -->
### Function: arraymake (name, [i_1, ..., i_n])

El resultado es una referencia a array no evaluada.


Devuelve la expresión `name [i_1, ..., i_n]`.


Esta función es similar a `funmake`, excepto que el valor retornado es referencia a un array no evaluado, en lugar de una llamada a una función no evaluada.


Ejemplos:



















```maxima
(%i1) arraymake (A, [1]);
(%o1)                          A
                                1
(%i2) arraymake (A, [k]);
(%o2)                          A
                                k
(%i3) arraymake (A, [i, j, 3]);
(%o3)                       A
                             i, j, 3
(%i4) array (A, fixnum, 10);
(%o4)                           A
(%i5) fillarray (A, makelist (i^2, i, 1, 11));
(%o5)                           A
(%i6) arraymake (A, [5]); 
(%o6)                          A
                                5
(%i7) ''%;
(%o7)                          36
(%i8) L : [a, b, c, d, e];
(%o8)                    [a, b, c, d, e]
(%i9) arraymake ('L, [n]);
(%o9)                          L
                                n
(%i10) ''%, n = 3;
(%o10)                          c
(%i11) A2 : make_array (fixnum, 10);
(%o11)          {Array:  #(0 0 0 0 0 0 0 0 0 0)}
(%i12) fillarray (A2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o12)          {Array:  #(1 2 3 4 5 6 7 8 9 10)}
(%i13) arraymake ('A2, [8]);
(%o13)                         A2
                                 8
(%i14) ''%;
(%o14)                          9
```

<!-- category: Programming -->
<!-- keywords: arrays -->
<!-- signatures: arrays -->
### Variable: arrays

Valor por defecto: `[]`
La variable `arrays` es una lista con todos los arrays que han sido alojados,
lo que comprende a los arrays declarados por `array`, a los
no declarados (*hashed arrays*) construidos implícitamente
(asignando algo al elemento de un array) y a las funciones array definidas
mediante `:=` y `define`.
Los arrays definidos mediante `make_array` no se incluyen en
este grupo.


Véanse también
`array`, `arrayapply`, `arrayinfo`, `arraymake`, 
`fillarray`, `listarray` y `rearray`.


Ejemplos:










```maxima
(%i1) array (aa, 5, 7);
(%o1)                          aa
(%i2) bb [FOO] : (a + b)^2;
                                   2
(%o2)                       (b + a)
(%i3) cc [x] := x/100;
                                   x
(%o3)                      cc  := ---
                             x    100
(%i4) dd : make_array ('any, 7);
(%o4)       {Array:  #(NIL NIL NIL NIL NIL NIL NIL)}
(%i5) arrays;
(%o5)                     [aa, bb, cc]
```

<!-- category: Programming -->
<!-- keywords: arraysetapply -->
<!-- signatures: arraysetapply(A, [i_1, ..., i_n], x) -->
### Function: arraysetapply (A, [i_1, ..., i_n], x)

Asigna *x* a `A[i_1, ..., i_n]`,
siendo *A* un array y *i_1*, ..., *i_n* enteros.


`arraysetapply` evalúa sus argumentos.

<!-- category: Programming -->
<!-- keywords: assoc -->
<!-- signatures: assoc(clave, lista, valor_por_defecto), assoc(clave, lista) -->
### Function: assoc (clave, lista, valor_por_defecto)

Esta función busca la *clave* en el lado derecho de la  *lista*, la cual es de la forma `[x,y,z,...]`, donde cada elemento  es una expresión formada por un operador binario y dos elementos. Por ejemplo, `x=1`, `2^3`, `[a,b]` etc.  La *clave* se compara con el primer operando. La función `assoc` devuelve el segundo operando si se encuentra con que la `clave` coincide.  Si la `clave` no coincide entonces devuelve el valor *valor_por_defecto*. El argumento *valor_por_defecto* es opcional; en caso de no estar presente, se devolverá `false`.

<!-- category: Programming -->
<!-- keywords: cons -->
<!-- signatures: cons(expr, lista) -->
### Function: cons (expr, lista)

Devuelve una nueva lista en la que el elemento *expr* ocupa la primera posición, seguido de los elementos de *lista*. La función  `cons` también opera con otro tipo de expresiones, como  `cons(x, f(a,b,c));`  ->  `f(x,a,b,c)`.

<!-- category: Programming -->
<!-- keywords: copylist -->
<!-- signatures: copylist(lista) -->
### Function: copylist (lista)

Devuelve una copia de la *lista*.

<!-- category: Programming -->
<!-- keywords: create_list -->
<!-- signatures: create_list(form, x_1, list_1, ..., x_n, list_n) -->
### Function: create_list (form, x_1, list_1, ..., x_n, list_n)

Crea una lista mediante la evaluación de *form* con *x_1* tomando cada uno de los
valores de *list_1*, para cada uno de estos valores liga *x_2* con cada elemento de 
*list_2*, .... El número de elementos en el resultado será el producto del número de elementos
en cada lista. Cada variable *x_i* debe ser un símbolo y no será evaluado.
La lista de argumentos será evaluada una vez al comienzo de la iteración.


Ejemplos:






```maxima
(%i1) create_list (x^i, i, [1, 3, 7]);
                                3   7
(%o1)                      [x, x , x ]
```



Con una doble iteración:






```maxima
(%i1) create_list ([i, j], i, [a, b], j, [e, f, h]);
(%o1)   [[a, e], [a, f], [a, h], [b, e], [b, f], [b, h]]
```


En lugar de *list_i* se pueden suministrar dos argumentos cada uno de los cuales 
debería poder evaluarse a un número, los cuales serán los límites inferior
y superior, ambos inclusive, para cada iteración.






```maxima
(%i1) create_list ([i, j], i, [1, 2, 3], j, 1, i);
(%o1)   [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]
```


Nótese que los límites o lista para la variable `j` pueden depender
del valor actual de `i`.

<!-- category: Programming -->
<!-- keywords: delete -->
<!-- signatures: delete(expr_1, expr_2), delete(expr_1, expr_2, n) -->
### Function: delete (expr_1, expr_2)

`delete(expr_1, expr_2)`
elimina de *expr_2* cualesquiera argumentos del operador
del nivel superior que sean iguales a *expr_1*.
Nótese que los argumentos de las subexpresiones no se ven
afectados por esta función.


*expr_1* puede ser un átomo o una expresión no
atómica. *expr_2* puede ser cualquier expresión no
atómica. La función `delete` devuelve una
nueva expresión sin modificar *expr_2*.


`delete(expr_1, expr_2, n)`
elimina de *expr_2* los primeros *n* argumentos
del operador del nivel superior que sean iguales a *expr_1*.
Si hay menos de *n* argumentos iguales, entonces se
eliminan todos ellos.


Ejemplos:


Eliminando elementos de una lista.






```maxima
(%i1) delete (y, [w, x, y, z, z, y, x, w]);
(%o1)                  [w, x, z, z, x, w]
```


Eliminando términos de una suma.






```maxima
(%i1) delete (sin(x), x + sin(x) + y);
(%o1)                         y + x
```


Eliminando factores de un producto.






```maxima
(%i1) delete (u - x, (u - w)*(u - x)*(u - y)*(u - z));
(%o1)                (u - w) (u - y) (u - z)
```


Eliminando argumentos de una expresión arbitraria.






```maxima
(%i1) delete (a, foo (a, b, c, d, a));
(%o1)                     foo(b, c, d)
```


Limitando el número de argumentos a eliminar.






```maxima
(%i1) delete (a, foo (a, b, a, c, d, a), 2);
(%o1)                    foo(b, c, d, a)
```


Los argumentos se comparan respecto de "=".
Aquellos argumentos que verifiquen la condición `equal`,
pero no "=" no serán eliminados.











```maxima
(%i1) [is (equal (0, 0)), is (equal (0, 0.0)), is (equal (0, 0b0))];
rat: replaced 0.0 by 0/1 = 0.0
`rat' replaced 0.0B0 by 0/1 = 0.0B0
(%o1)                  [true, true, true]


(%i2) [is (0 = 0), is (0 = 0.0), is (0 = 0b0)];
(%o2)                 [true, false, false]


(%i3) delete (0, [0, 0.0, 0b0]);
(%o3)                     [0.0, 0.0b0]


(%i4) is (equal ((x + y)*(x - y), x^2 - y^2));
(%o4)                         true


(%i5) is ((x + y)*(x - y) = x^2 - y^2);
(%o5)                         false


(%i6) delete ((x + y)*(x - y), [(x + y)*(x - y), x^2 - y^2]);
                              2    2
(%o6)                       [x  - y ]
```

<!-- category: Programming -->
<!-- keywords: eighth -->
<!-- signatures: eighth(expr) -->
### Function: eighth (expr)

Devuelve el octavo elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: endcons -->
<!-- signatures: endcons(expr, lista) -->
### Function: endcons (expr, lista)

Devuelve una nueva lista formada por los elementos de `lista` seguidos de los de *expr*. La función `endcons` también opera con expresiones generales, por ejemplo `endcons(x, f(a,b,c));`  ->  `f(a,b,c,x)`.

<!-- category: Programming -->
<!-- keywords: false -->
<!-- signatures: false -->
### Variable: false

El símbolo `false` representa al valor lógico
"falso". Maxima implementa `false` con el valor `NIL` de
Lisp.

<!-- category: Programming -->
<!-- keywords: fifth -->
<!-- signatures: fifth(expr) -->
### Function: fifth (expr)

Devuelve el quinto elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: fillarray -->
<!-- signatures: fillarray(A, B) -->
### Function: fillarray (A, B)

Rellena el array *A* con los valores de *B*, que puede ser una lista o array.


Si se ha declarado *A* de un determinado tipo en el momento de su
creación, sólo podrá contener elementos de ese tipo, produciéndose
un error en caso de intentar asignarle un elemento de tipo distinto.


Si las dimensiones de los arrays *A* y *B* son diferentes,
*A* se rellena según el orden de las filas. Si no hay 
suficientes elementos en *B* el último elemento se utiliza 
para cubrir el resto de *A*. Si hay demasiados, los elementos 
sobrantes son ignorados.


La función `fillarray` devuelve su primer argumento.


Ejemplos:


Creación de un array de 9 elementos y posterior relleno a partir de una lista.









```maxima
(%i1) array (a1, fixnum, 8);
(%o1)                          a1
(%i2) listarray (a1);
(%o2)              [0, 0, 0, 0, 0, 0, 0, 0, 0]
(%i3) fillarray (a1, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
(%o3)                          a1
(%i4) listarray (a1);
(%o4)              [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


Si no hay suficientes elementos para cubrir el array, se repite el
último elemento. Si hay demasiados, los elementos 
sobrantes son ignorados.









```maxima
(%i1) a2 : make_array (fixnum, 8);
(%o1)             {Array:  #(0 0 0 0 0 0 0 0)}
(%i2) fillarray (a2, [1, 2, 3, 4, 5]);
(%o2)             {Array:  #(1 2 3 4 5 5 5 5)}
(%i3) fillarray (a2, [4]);
(%o3)             {Array:  #(4 4 4 4 4 4 4 4)}
(%i4) fillarray (a2, makelist (i, i, 1, 100));
(%o4)             {Array:  #(1 2 3 4 5 6 7 8)}
```


Arrays multidimensionales se rellenan según el orden de las filas.









```maxima
(%i1) a3 : make_array (fixnum, 2, 5);
(%o1)        {Array:  #2A((0 0 0 0 0) (0 0 0 0 0))}
(%i2) fillarray (a3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o2)        {Array:  #2A((1 2 3 4 5) (6 7 8 9 10))}
(%i3) a4 : make_array (fixnum, 5, 2);
(%o3)     {Array:  #2A((0 0) (0 0) (0 0) (0 0) (0 0))}
(%i4) fillarray (a4, a3);
(%o4)     {Array:  #2A((1 2) (3 4) (5 6) (7 8) (9 10))}
```

<!-- category: Programming -->
<!-- keywords: first -->
<!-- signatures: first(expr) -->
### Function: first (expr)

Devuelve la primera parte de *expr*, que puede consistir en el primer elemento de una lista, la primera fila de una matriz, el primer término de una suma, etc. Nótese que tanto `first` como sus funciones relacionadas, `rest` y `last`, operan sobre la forma en la que *expr* es mostrada por Maxima, no sobre la forma en la que es introducida la expresión. Sin embargo, cuando la variable `inflag` toma el valor `true` estas funciones tendrán en cuenta el formato interno de *expr*. Téngase en cuenta que el simplificador reordena las expresiones.  Así, `first(x+y)` devolverá `x` si `inflag` vale `true` y `y` cuando `inflag` tome el valor `false` (`first(y+x)` devuelve el mismo resultado). Las funciones `second` ... `tenth` devuelven desde el segundo hasta el décimo elemento del argumento de entrada.

<!-- category: Programming -->
<!-- keywords: fourth -->
<!-- signatures: fourth(expr) -->
### Function: fourth (expr)

Devuelve el cuarto elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: ind -->
<!-- signatures: ind -->
### Variable: ind

`ind` representa un resultado acotado indeterminado.


Véase también `limit`.


Ejemplo:






```maxima
(%i1) limit (sin(1/x), x, 0);
(%o1)                          ind
```

<!-- category: Programming -->
<!-- keywords: inf -->
<!-- signatures: inf -->
### Variable: inf

El símbolo `inf` representa al infinito real positivo.

<!-- category: Programming -->
<!-- keywords: infinity -->
<!-- signatures: infinity -->
### Variable: infinity

El símbolo `infinity` representa al infinito complejo.

<!-- category: Programming -->
<!-- keywords: join -->
<!-- signatures: join(l, m) -->
### Function: join (l, m)

Crea una nueva lista con los elementos de las listas *l* y *m* alternados.
El resultado tiene como elementos `[l[1], m[1], l[2], m[2], ...]`.
Las listas *l* y *m* pueden contener cualquier tipo de elementos.


Si las listas son de diferente longitud, `join` ignora los elementos sobrantes de la lista más larga.


Maxima da error si o bien *l* o *m* no son listas.


Ejemplos:








```maxima
(%i1) L1: [a, sin(b), c!, d - 1];
(%o1)                [a, sin(b), c!, d - 1]


(%i2) join (L1, [1, 2, 3, 4]);
(%o2)          [a, 1, sin(b), 2, c!, 3, d - 1, 4]


(%i3) join (L1, [aa, bb, cc, dd, ee, ff]);
(%o3)        [a, aa, sin(b), bb, c!, cc, d - 1, dd]
```

<!-- category: Programming -->
<!-- keywords: last -->
<!-- signatures: last(expr) -->
### Function: last (expr)

Devuelve la última parte (término, fila, elemento, etc.) de *expr*.

<!-- category: Programming -->
<!-- keywords: length -->
<!-- signatures: length(expr) -->
### Function: length (expr)

Devuelve (por defecto) el número de partes de que consta *expr* en la versión correspondiente a la que muestra.  En el caso de listas, se devuelve el número de elementos, si se trata de matrices el número de filas y se se trata de sumas el número de términos o sumandos (véase `dispform`).


La función `length` se ve afectada por el valor de la variable `inflag`.  Así, `length(a/(b*c));` devuelve 2 si `inflag` vale `false` (dando por hecho que `exptdispflag` vale `true`), pero devuelve 3 si `inflag` vale `true` (ya que la representación interna es `a*b^-1*c^-1`).

<!-- category: Programming -->
<!-- keywords: listarith -->
<!-- signatures: listarith -->
### Variable: listarith

Valor por defecto: `true`


Cuando vale `false` provoca que no se realicen operaciones aritméticas con listas;  cuando vale `true`, las operaciones con listas y matrices son contagiosas, en el sentido de que las listas se transforman en matrices, retornando resultados de este último tipo. Sin embargo, operaciones que involucren listas con listas devolverán también listas.

<!-- category: Programming -->
<!-- keywords: listarray -->
<!-- signatures: listarray(A) -->
### Function: listarray (A)

Devuelve una lista con los elementos del array *A*.
El argumento *A* puede ser un array declarado o no declarado,
una función array o una función subindicada.


Los elementos se ordenan en primera instancia respecto del primer 
índice, después respecto del segundo índice
y así sucesivamente.
La ordenación de los índices es la misma que la 
establecida por `orderless`.


En el caso de arrays no declarados, funciones array y funciones
subindicadas, los elementos corresponden a los índices
devueltos por `arrayinfo`.


Los elementos de los arrays declarados que no tienen valores asignados
(excepto `fixnum` y `flonum`) se devuelven como `#####`.
Los elementos sin valores asignados de los arrays `fixnum` y `flonum`
son devueltos como 0 y 0.0, respectivamente.
Los elementos sin valor asignado de los arrays no declarados, 
funciones array y funciones subindicadas no son devueltos.


Ejemplos:


`listarray` y `arrayinfo` aplicadas a un array declarado.










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa
(%i2) aa [2, 3] : %pi;
(%o2)                          %pi
(%i3) aa [1, 2] : %e;
(%o3)                          %e
(%i4) listarray (aa);
(%o4) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
(%i5) arrayinfo (aa);
(%o5)                 [declared, 2, [2, 3]]
```


`listarray` y `arrayinfo` aplicadas a un array no declarado (*hashed array*).









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)
(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)
(%i3) listarray (bb);
                              3         2
(%o3)                 [(c - d) , (b + a) ]
(%i4) arrayinfo (bb);
(%o4)               [hashed, 1, [BAR], [FOO]]
```


`listarray` y `arrayinfo` aplicadas a una función array.










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x
(%i2) cc [u, v];
                                v
(%o2)                           -
                                u
(%i3) cc [4, z];
                                z
(%o3)                           -
                                4
(%i4) listarray (cc);
                              z  v
(%o4)                        [-, -]
                              4  u
(%i5) arrayinfo (cc);
(%o5)              [hashed, 2, [4, z], [u, v]]
```


`listarray` y `arrayinfo` aplicadas a una función subindicada.










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x
(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )
(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )
(%i4) listarray (dd);
                         b + a                v - u
(%o4)      [lambda([y], y     ), lambda([y], y     )]
(%i5) arrayinfo (dd);
(%o5)             [hashed, 1, [b + a], [v - u]]
```

<!-- category: Programming -->
<!-- keywords: listp -->
<!-- signatures: listp(expr) -->
### Function: listp (expr)

Devuelve el valor `true` si *expr* es una lista, y `false` en caso contrario.

<!-- category: Programming -->
<!-- keywords: make_array -->
<!-- signatures: make_array(tipo, dim_1, ..., dim_n) -->
### Function: make_array (tipo, dim_1, ..., dim_n)

Construye y devuelve un array de Lisp. El argumento *tipo* puede ser
`any`, `flonum`, `fixnum`, `hashed` o `functional`.
Hay $n$ índices, y el índice $i$-ésimo
va de  0 a $dim_i - 1$.


La ventaja de `make_array` sobre `array` estriba en que el valor
retornado no tiene nombre, y una vez que un puntero deja de referenciarlo,
el valor desaparece. Por ejemplo, si `y: make_array (...)` entonces
`y` apunta a un objeto que ocupa cierto espacio en la memoria, pero
después de `y: false`, `y` ya no apunta al objeto, por lo
que éste puede ser considerado basura y posteriormente eliminado.  


Ejemplos:

















```maxima
(%i1) A1 : make_array (fixnum, 10);
(%o1)           {Array:  #(0 0 0 0 0 0 0 0 0 0)}
(%i2) A1 [8] : 1729;
(%o2)                         1729
(%i3) A1;
(%o3)          {Array:  #(0 0 0 0 0 0 0 0 1729 0)}
(%i4) A2 : make_array (flonum, 10);
(%o4) {Array:  #(0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}
(%i5) A2 [2] : 2.718281828;
(%o5)                      2.718281828
(%i6) A2;
(%o6) 
     {Array:  #(0.0 0.0 2.718281828 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}
(%i7) A3 : make_array (any, 10);
(%o7) {Array:  #(NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL)}
(%i8) A3 [4] : x - y - z;
(%o8)                      - z - y + x
(%i9) A3;
(%o9) {Array:  #(NIL NIL NIL NIL ((MPLUS SIMP) $X ((MTIMES SIMP)\
 -1 $Y) ((MTIMES SIMP) -1 $Z))
  NIL NIL NIL NIL NIL)}
(%i10) A4 : make_array (fixnum, 2, 3, 5);
(%o10) {Array:  #3A(((0 0 0 0 0) (0 0 0 0 0) (0 0 0 0 0)) ((0 0 \
0 0 0) (0 0 0 0 0) (0 0 0 0 0)))}
(%i11) fillarray (A4, makelist (i, i, 1, 2*3*5));
(%o11) {Array:  #3A(((1 2 3 4 5) (6 7 8 9 10) (11 12 13 14 15))
    ((16 17 18 19 20) (21 22 23 24 25) (26 27 28 29 30)))}
(%i12) A4 [0, 2, 1];
(%o12)                         12
```

<!-- category: Programming -->
<!-- keywords: makelist -->
<!-- signatures: makelist(), makelist(expr, n), makelist(expr, i, i_max), makelist(expr, i, i_0, i_max), makelist(expr, i, i_0, i_max, step), makelist(expr, x, list) -->
### Function: makelist ()

El primer formato, `makelist ()`, crea una lista vacía. El
segundo formato, `makelist (expr)`, crea una lista con *expr*
como único elemento. `makelist (expr, n)` crea una lista
de *n* elementos generados a partir de *expr*.


El formato más general, `makelist (expr, i, i_0, i_max, step)`, devuelve la lista de elementos obtenidos al
aplicar `ev (expr, i=j)` a los elementos *j* 
de la secuencia *i_0*, *i_0* + *step*, *i_0* +
2**step*, ..., siendo *|j|* menor o igual que *|i_max|*.


El incremento *step* puede ser un número (positivo o negativo) o una
expresión. En caso de omitirse, se utilizará 1 como valor por defecto.
Si se omiten  *i_0* y *step*, se le asignará a ambos 1 como valor
por defecto.


`makelist (expr, x, list)` devuelve una lista, cuyo
`j`-ésimo elemento es igual a
`ev (expr, x=list[j])` tomando `j` valores desde
1 hasta `length (list)`.



Ejemplos:











```maxima
(%i1) makelist (concat (x,i), i, 6);
(%o1)               [x1, x2, x3, x4, x5, x6]


(%i2) makelist (x=y, y, [a, b, c]);
(%o2)                 [x = a, x = b, x = c]


(%i3) makelist (x^2, x, 3, 2*%pi, 2);
(%o3)                        [9, 25]


(%i4) makelist (random(6), 4);
(%o4)                     [2, 0, 2, 5]


(%i5) flatten (makelist (makelist (i^2, 3), i, 4));
(%o5)        [1, 1, 1, 4, 4, 4, 9, 9, 9, 16, 16, 16]


(%i6) flatten (makelist (makelist (i^2, i, 3), 4));
(%o6)         [1, 4, 9, 1, 4, 9, 1, 4, 9, 1, 4, 9]
```

<!-- category: Programming -->
<!-- keywords: member -->
<!-- signatures: member(expr_1, expr_2) -->
### Function: member (expr_1, expr_2)

Devuelve `true` si `is(expr_1 = a)`
para algún elemento *a* de `args(expr_2)`,
en caso contrario devuelve `false`.


Normalmente, `expr_2` será una lista,
en cuyo caso `args(expr_2) = expr_2`,
y la comprobación será si `is(expr_1 = a)` para 
algún elemento *a* de `expr_2`.


La función `member` no inspecciona las partes de los argumentos de `expr_2`,
por lo que puede devolver `false` si `expr_1` es parte de alguno de los argumentos de `expr_2`.


Véase también `elementp`.


Ejemplos:













```maxima
(%i1) member (8, [8, 8.0, 8b0]);
(%o1)                         true


(%i2) member (8, [8.0, 8b0]);
(%o2)                         false


(%i3) member (b, [a, b, c]);
(%o3)                         true


(%i4) member (b, [[a, b], [b, c]]);
(%o4)                         false


(%i5) member ([b, c], [[a, b], [b, c]]);
(%o5)                         true


(%i6) F (1, 1/2, 1/4, 1/8);
                               1  1  1
(%o6)                     F(1, -, -, -)
                               2  4  8


(%i7) member (1/8, %);
(%o7)                         true


(%i8) member ("ab", ["aa", "ab", sin(1), a + b]);
(%o8)                         true
```

<!-- category: Programming -->
<!-- keywords: minf -->
<!-- signatures: minf -->
### Variable: minf

El símbolo `minf` representa al infinito real negativo.

<!-- category: Programming -->
<!-- keywords: ninth -->
<!-- signatures: ninth(expr) -->
### Function: ninth (expr)

Devuelve el noveno elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: pop -->
<!-- signatures: pop(list) -->
### Function: pop (list)

Borra el primer elemento de la lista *list* y devuelve este
mismo elemento.


Si el argumento *list* es una lista vacía, o
simplemente no es una lista, Maxima devuelve un mensaje de error.


Véase `push` para los ejemplos.


Ejecútese `load("basic")` antes de utilizar esta función.

<!-- category: Programming -->
<!-- keywords: push -->
<!-- signatures: push(item, list) -->
### Function: push (item, list)

Añade al comienzo de la lista *list* el elemento *item*,
devolviendo este mismo elemento. El argumento *list* debe ser necesariamente
una lista, mientras que *item* puede ser cualquier símbolo
o expresión.


Si el argumento *list* no es una lista, Maxima devuelve un
mensaje de error.


Véase `pop` para eliminar el primer elemento de una lista.


Ejecútese `load("basic")` antes de utilizar esta función.


Ejemplos:















```maxima
(%i1) load ("basic")$

(%i2) ll: [];
(%o2)                          []


(%i3) push (x, ll);
(%o3)                          [x]


(%i4) push (x^2+y, ll);
                                 2
(%o4)                      [y + x , x]


(%i5) a: push ("string", ll);
                                     2
(%o5)                  [string, y + x , x]


(%i6) pop (ll);
(%o6)                        string


(%i7) pop (ll);
                                  2
(%o7)                        y + x


(%i8) pop (ll);
(%o8)                           x


(%i9) ll;
(%o9)                          []


(%i10) a;
                                     2
(%o10)                 [string, y + x , x]
```

<!-- category: Programming -->
<!-- keywords: rearray -->
<!-- signatures: rearray(A, dim_1, ..., dim_n) -->
### Function: rearray (A, dim_1, ..., dim_n)

Cambia las dimensiones de un array. El nuevo array será rellenado con los elementos del viejo según el orden de las filas. Si el array antiguo era demasiado pequeño, los elementos restantes se rellenan con `false`, `0.0` o `0`, dependiendo del tipo del array. El tipo del array no se puede cambiar.

<!-- category: Programming -->
<!-- keywords: remarray -->
<!-- signatures: remarray(A_1, ..., A_n), remarray(all) -->
### Function: remarray (A_1, ..., A_n)

Borra los arrays y las funciones relacionadas con ellos, liberando el espacio de memoria ocupado.
Los argumentos pueden ser arrays declarados, arrays no declarados (*hashed arrays*), 
funciones array y funciones subindicadas.


La llamada `remarray (all)` borra todos los elementos de la lista global `arrays`.


La función `remarray` devuelve la lista de los arrays borrados.


La función `remarray` no evalúa sus argumentos.

<!-- category: Programming -->
<!-- keywords: rest -->
<!-- signatures: rest(expr, n), rest(expr) -->
### Function: rest (expr, n)

Devuelve *expr* sin sus primeros *n* elementos si *n* es positivo, o sus últimos `- n` elementos si *n* es negativo. En caso de que *n* tome el valor 1 puede ser omitido. La expresión  *expr* puede ser una lista, una matriz o cualquier otra expresión.

<!-- category: Programming -->
<!-- keywords: reverse -->
<!-- signatures: reverse(lista) -->
### Function: reverse (lista)

Invierte el orden de los elementos de la *lista* (no los propios elementos). La función `reverse` también opera sobre expresiones generales, como en  `reverse(a=b);` gives `b=a`.

<!-- category: Programming -->
<!-- keywords: second -->
<!-- signatures: second(expr) -->
### Function: second (expr)

Devuelve el segundo elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: seventh -->
<!-- signatures: seventh(expr) -->
### Function: seventh (expr)

Devuelve el séptimo elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: sixth -->
<!-- signatures: sixth(expr) -->
### Function: sixth (expr)

Devuelve el sexto elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: sort -->
<!-- signatures: sort(L, P), sort(L) -->
### Function: sort (L, P)

`sort(L, P)` ordena la lista *L* de acuerdo con el predicado `P`
de dos argumentos, el cual define un preorden total sobre los elementos de *L*.
Si `P(a, b)` vale `true`, entonces `a` aparece antes que `b` en
el resultado. Si ninguna de las expresiones `P(a, b)` y `P(b, a)`
valen `true`, entonces `a` y `b` son equivalentes y aparecen en el
resultado en el mismo orden que a la entrada; esto es, `sort` es un orden estable.


Si tanto `P(a, b)` como `P(b, a)` valen ambos `true` para
algunos elementos de *L*, entonces *P* no es un predicado de orden correcto,
siento entonces el resultado indefinido. Si `P(a, b)` toma un valor diferente
a `true` o `false`, entonces `sort` devuelve un error.


El predicado puede especificarse como el nombre de una función, de una operación binaria
infija o como una expresión `lambda`. Si se especifica con el nombre de un operador,
dicho nombre debe encerrarse con comillas dobles.


La lista ordenada se devuelve como un nuevo objeto, no modificándose el argumento *L*.


`sort(L)` equivale a `sort(L, orderlessp)`.


La ordenación por defecto es ascendente, tal como queda determinada por `orderlessp`.
El predicado `ordergreatp` ordena las listas en orden descendente.


Todos los átomos y expresiones de Maxima son comparables respecto de los predicados
`orderlessp` y `ordergreatp`.


Los operadores `<` y `>` ordenan números, constantes y expresiones constantes por
magnitud. Nótese que `orderlessp` y `ordergreatp` no ordenan números, 
constantes y expresiones constantes por magnitud.


`ordermagnitudep` ordena números, constantes y expresiones constantes de igual modo
que lo hace `<`, y cualesquiera otros elementos lo hace igual que `orderlessp`.


Ejemplos:


`sort` ordena una lista respecto de un predicado de dos argumentos que define un
preorden total en los elementos de la lista.







```maxima
(%i1) sort ([1, a, b, 2, 3, c], 'orderlessp);
(%o1)                  [1, 2, 3, a, b, c]
(%i2) sort ([1, a, b, 2, 3, c], 'ordergreatp);
(%o2)                  [c, b, a, 3, 2, 1]
```


El predicado puede especificarse con el nombre de una función, de un
operador binario infijo o una expresión `lambda`. Si se especifica
con el nombre de un operador, dicho nombre debe encerrarse con comillas dobles.












```maxima
(%i1) L : [[1, x], [3, y], [4, w], [2, z]];
(%o1)           [[1, x], [3, y], [4, w], [2, z]]
(%i2) foo (a, b) := a[1] > b[1];
(%o2)                 foo(a, b) := a  > b
                                    1    1
(%i3) sort (L, 'foo);
(%o3)           [[4, w], [3, y], [2, z], [1, x]]
(%i4) infix (">>");
(%o4)                          >>
(%i5) a >> b := a[1] > b[1];
(%o5)                   a >> b := a  > b
                                   1    1
(%i6) sort (L, ">>");
(%o6)           [[4, w], [3, y], [2, z], [1, x]]
(%i7) sort (L, lambda ([a, b], a[1] > b[1]));
(%o7)           [[4, w], [3, y], [2, z], [1, x]]
```


`sort(L)` equivale a `sort(L, orderlessp)`.








```maxima
(%i1) L : [a, 2*b, -5, 7, 1 + %e, %pi];
(%o1)             [a, 2 b, - 5, 7, %e + 1, %pi]
(%i2) sort (L);
(%o2)             [- 5, 7, %e + 1, %pi, a, 2 b]
(%i3) sort (L, 'orderlessp);
(%o3)             [- 5, 7, %e + 1, %pi, a, 2 b]
```


La ordenación por defecto es ascendente, tal como queda determinada por `orderlessp`.
El predicado `ordergreatp` ordena las listas en orden descendente.








```maxima
(%i1) L : [a, 2*b, -5, 7, 1 + %e, %pi];
(%o1)                    [a, 2 b, - 5, 7, %e + 1, %pi]
(%i2) sort (L);
(%o2)                    [- 5, 7, %e + 1, %pi, a, 2 b]
(%i3) sort (L, 'ordergreatp);
(%o3)                    [2 b, a, %pi, %e + 1, 7, - 5]
```


Todos los átomos y expresiones de Maxima son comparables respecto de los predicados
`orderlessp` y `ordergreatp`.








```maxima
(%i1) L : [11, -17, 29b0, 9*c, 7.55, foo(x, y), -5/2, b + a];
                                                 5
(%o1)  [11, - 17, 2.9b1, 9 c, 7.55, foo(x, y), - -, b + a]
                                                 2
(%i2) sort (L, orderlessp);
                5
(%o2)  [- 17, - -, 7.55, 11, 2.9b1, b + a, 9 c, foo(x, y)]
                2
(%i3) sort (L, ordergreatp);
                                                  5
(%o3)  [foo(x, y), 9 c, b + a, 2.9b1, 11, 7.55, - -, - 17]
                                                  2
```


Los operadores `<` y `>` ordenan números, constantes y expresiones constantes por
magnitud. Nótese que `orderlessp` y `ordergreatp` no ordenan números, 
constantes y expresiones constantes por magnitud.








```maxima
(%i1) L : [%pi, 3, 4, %e, %gamma];
(%o1)                [%pi, 3, 4, %e, %gamma]
(%i2) sort (L, ">");
(%o2)                [4, %pi, 3, %e, %gamma]
(%i3) sort (L, ordergreatp);
(%o3)                [%pi, %gamma, %e, 4, 3]
```


`ordermagnitudep` ordena números, constantes y expresiones constantes de igual modo
que lo hace `<`, y cualesquiera otros elementos lo hace igual que `orderlessp`.








```maxima
(%i1) L : [%i, 1+%i, 2*x, minf, inf, %e, sin(1), 0, 1, 2, 3, 1.0, 1.0b0];
(%o1) [%i, %i + 1, 2 x, minf, inf, %e, sin(1), 0, 1, 2, 3, 1.0, 
                                                           1.0b0]
(%i2) sort (L, ordermagnitudep);
(%o2) [minf, 0, sin(1), 1, 1.0, 1.0b0, 2, %e, 3, inf, %i, 
                                                     %i + 1, 2 x]
(%i3) sort (L, orderlessp);
(%o3) [0, 1, 1.0, 2, 3, %e, %i, %i + 1, inf, minf, sin(1), 
                                                      1.0b0, 2 x]
```

<!-- category: Programming -->
<!-- keywords: sublist -->
<!-- signatures: sublist(list, p) -->
### Function: sublist (list, p)

Devuelve la lista de elementos de *list* para los cuales el predicado `p` retorna `true`.


Ejemplo:







```maxima
(%i1) L: [1, 2, 3, 4, 5, 6];
(%o1)                  [1, 2, 3, 4, 5, 6]


(%i2) sublist (L, evenp);
(%o2)                       [2, 4, 6]
```

<!-- category: Programming -->
<!-- keywords: sublist_indices -->
<!-- signatures: sublist_indices(L, P) -->
### Function: sublist_indices (L, P)

Devuelve los índices de los elementos `x` de la
lista *L* para la cual el predicado `maybe(P(x))`
devuelve `true`, lo que excluye a `unknown` y a `false`.
*P* puede ser el nombre de una función o de una expresión lambda.
*L* debe ser una lista literal.


Ejemplos:













```maxima
(%i1) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b],
                       lambda ([x], x='b));
(%o1)                     [2, 3, 7, 9]


(%i2) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b], symbolp);
(%o2)                  [1, 2, 3, 4, 7, 9]


(%i3) sublist_indices ([1 > 0, 1 < 0, 2 < 1, 2 > 1, 2 > 0],
                       identity);
(%o3)                       [1, 4, 5]


(%i4) assume (x < -1);
(%o4)                       [x < - 1]


(%i5) map (maybe, [x > 0, x < 0, x < -2]);
(%o5)                [false, true, unknown]


(%i6) sublist_indices ([x > 0, x < 0, x < -2], identity);
(%o6)                          [2]
```

<!-- category: Programming -->
<!-- keywords: subvar -->
<!-- signatures: subvar(x, i) -->
### Function: subvar (x, i)

Evalúa la expresión subindicada `x[i]`.


La función `subvar` evalúa sus argumentos.


La instrucción `arraymake (x, [i])` construye la expresión `x[i]`,
pero no la evalúa.


Ejemplos:












```maxima
(%i1) x : foo $

(%i2) i : 3 $

(%i3) subvar (x, i);
(%o3)                         foo
                                 3
(%i4) foo : [aa, bb, cc, dd, ee]$

(%i5) subvar (x, i);
(%o5)                          cc
(%i6) arraymake (x, [i]);
(%o6)                         foo
                                 3
(%i7) ''%;
(%o7)                          cc
```

<!-- category: Programming -->
<!-- keywords: subvarp -->
<!-- signatures: subvarp(expr) -->
### Function: subvarp (expr)

Devuelve `true` si *expr* es una variable subindicada, como `a[i]`.

<!-- category: Programming -->
<!-- keywords: tenth -->
<!-- signatures: tenth(expr) -->
### Function: tenth (expr)

Devuelve el décimo elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: third -->
<!-- signatures: third(expr) -->
### Function: third (expr)

Devuelve el tercer elemento de la lista o expresión *expr*. Véase `first` para más detalles.

<!-- category: Programming -->
<!-- keywords: true -->
<!-- signatures: true -->
### Variable: true

El símbolo `true` representa al valor lógico
"verdadero". Maxima implementa `true` con el valor `T` de
Lisp.

<!-- category: Programming -->
<!-- keywords: und -->
<!-- signatures: und -->
### Variable: und

`und` representa un resultado indefinido.


Véase también `limit`.


Ejemplo:






```maxima
(%i1) limit (x*sin(x), x, inf);
(%o1)                          und
```

<!-- category: Programming -->
<!-- keywords: unique -->
<!-- signatures: unique(L) -->
### Function: unique (L)

Devuelve la lista *L* sin redundancias, es decir, sin
elementos repetidos


Cuando ninguno de los elementos de *L* está repetido,
`unique` devuelve una réplica de *L*, no la
propia *L*.


Si *L* no es una lista, `unique` devuelve *L*.


Ejemplo:






```maxima
(%i1) unique ([1, %pi, a + b, 2, 1, %e, %pi, a + b, [1]]);
(%o1)              [1, 2, %e, %pi, [1], b + a]
```

<!-- category: Programming -->
<!-- keywords: use_fast_arrays -->
<!-- signatures: use_fast_arrays -->
### Variable: use_fast_arrays

Valor por defecto: `false`


Si `use_fast_arrays` vale `true` entonces tan solo se reconocen dos tipos de arrays.

<!-- category: Programming -->
<!-- keywords: zeroa -->
<!-- signatures: zeroa -->
### Variable: zeroa

`zeroa` representa un infinitesimal mayor que cero. 
`zeroa` puede utilizarse en expresiones. `limit`
simplifica expresiones que contienen infinitesimales.


Véanse también `zerob` y `limit`.


Ejemplo:


`limit` simplifica expresiones que contienen infinitesimales:







```maxima
(%i1) limit(zeroa);
(%o1)                                  0
(%i2) limit(x+zeroa);
(%o2)                                  x
```

<!-- category: Programming -->
<!-- keywords: zerob -->
<!-- signatures: zerob -->
### Variable: zerob

`zerob` representa un infinitesimal menor que cero. 
`zerob` puede utilizarse en expresiones. `limit`
simplifica expresiones que contienen infinitesimales.


Véanse también `zeroa` y `limit`.

