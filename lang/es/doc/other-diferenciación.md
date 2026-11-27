## Diferenciación

<!-- category: Other -->
<!-- keywords: antid -->
<!-- signatures: antid(expr, x, u(x)) -->
### Function: antid (expr, x, u(x))

Devuelve una lista con dos elementos, de manera que se pueda calcular la antiderivada de *expr* respecto de  *x* a partir de la lista. La expresión *expr* puede contener una función no especificada *u* y sus derivadas.


Sea *L* la lista con dos elementos que devuelve la función `antid`.
Entonces, `L[1] + 'integrate (L[2], x)`
es una antiderivada de *expr* con respecto a *x*.


Si la ejecución de `antid` resulta exitosa, el segundo elemento de la lista retornada es cero. En caso contrario, el segundo elemento es distinto de cero y el primero puede ser nulo o no. Si `antid` no es capaz de hacer ningún progreso, el primer elemento es nulo y el segundo no nulo.


Es necesario ejecutar `load ("antid")` para cargar esta función. El paquete `antid` define también las funciones `nonzeroandfreeof` y `linear`.


La función `antid` está relacionada con `antidiff` como se indica a continuación.
Sea *L* la lista devuelta por la función `antid`. Entonces, el resultado de `antidiff` es igual a  `L[1] + 'integrate (L[2], x)`, donde *x* es la variable de integración.


Ejemplos:














```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

<!-- category: Other -->
<!-- keywords: antidiff -->
<!-- signatures: antidiff(expr, x, u(x)) -->
### Function: antidiff (expr, x, u(x))

Devuelve la antiderivada de *expr* respecto de *x*.
La expresión *expr* puede contener una función no especificada *u* y sus derivadas.


Cuando `antidiff` se ejecuta con éxito, la expresión resultante no tiene símbolos integrales (esto es, no tiene referencias a la función `integrate`). En otro caso, `antidiff` devuelve una expresión que se encuentra total o parcialmente bajo el signo de integración. Si `antidiff` no puede ralizar ningún progreso, el valor devuelto se encuentra completamente bajo la integral.


Es necesario ejecutar `load ("antid")` para cargar esta función. El paquete `antid` define también las funciones `nonzeroandfreeof` y `linear`.


La función `antidiff` está relacionada con `antid` como se indica a continuación.
Sea *L* la lista de dos elementos que devuelve `antid`. Entonces, el valor retornado por `antidiff` es igual a `L[1] + 'integrate (L[2], x)`, donde *x* es la variable de integración.


Ejemplos:














```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

<!-- category: Other -->
<!-- keywords: at -->
<!-- signatures: at(expr, [eqn_1, ..., eqn_n]), at(expr, eqn) -->
### Function: at (expr, [eqn_1, ..., eqn_n])

Evalúa la expresión *expr* asignando a las variables los valores especificados para ellas en la lista de ecuaciones `[eqn_1, ..., eqn_n]` o en la ecuación simple *eqn*.


Si una subexpresión depende de cualquiera de las variables para la cual se especifica un valor, pero  no puede ser evaluado, entonces `at` devuelve una forma nominal.


La función `at` realiza múltiples sustituciones en serie, no en paralelo.


Véase también `atvalue`.
Para otras funciones que también llevan a cabo sustituciones, consúltense `subst` y `ev`.


Ejemplos:











```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x, y)^2 - u(x, y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);
                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

<!-- category: Other -->
<!-- keywords: atomgrad -->
<!-- signatures: atomgrad -->
### Variable: atomgrad

La propiedad `atomgrad` es asignada por `gradef`.

<!-- category: Other -->
<!-- keywords: atvalue -->
<!-- signatures: atvalue(expr, [x_1=a_1, ..., x_m=a_m], c), atvalue(expr, x_1=a_1, c) -->
### Function: atvalue (expr, [x_1=a_1, ..., x_m=a_m], c)

Asigna el valor *c* a *expr* en el punto `x = a`.


La expresión *expr* es una función del tipo 
`f(x_1, ..., x_m)`,
o una derivada,
`diff (f(x_1, ..., x_m), x_1, n_1, ..., x_n, n_m)`


en la que aparecen los argumentos de la función de forma explícita.
Los símbolos *n_i* se refieren al orden de diferenciación respecto de *x_i*.


El punto en el que `atvalue` establece el valor se especifica mediante la lista de ecuaciones
`[x_1 = a_1, ..., x_m = a_m]`.
Si hay una única variable *x_1*, la ecuación puede escribirse sin formar parte de una lista.


La llamada `printprops ([f_1, f_2, ...], atvalue)` muestra los valores asignados por `atvalue` a las funciones `f_1, f_2, ...`.
La llamada  `printprops (f, atvalue)` muestra los valores asignados por `atvalue` a la función *f*.
La llamada  `printprops (all, atvalue)` muestra los valores asignados por `atvalue` a todas las funciones.


Los símbolos `@1`, `@2`, ... representan las variables *x_1*, *x_2*, ... cuando se muestran los valores asignados por `atvalue`.


La función `atvalue` evalúa sus argumentos y devuelve *c*, el valor asignado.


Ejemplos:









```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x,y)^2 - u(x,y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);
                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

<!-- category: Other -->
<!-- keywords: cartan -->
<!-- signatures: cartan- -->
### Function: cartan (-)

El cálculo exterior de formas diferenciales es una herramienta básica de la geometría diferencial desarrollada por Elie Cartan, teniendo importantes aplicaciones en la teoría de ecuaciones diferenciales en derivadas parciales.
El paquete `cartan` dispone de las funciones `ext_diff` y `lie_diff`, así como de los operadores `~` (producto exterior) y `|` (contracción de una forma con un vector). La orden `demo (tensor)` permite ver una breve descripción de estas instrucciones, junto con ejemplos.


El paquete `cartan` fue escrito por F.B. Estabrook y H.D. Wahlquist.

<!-- category: Other -->
<!-- keywords: del -->
<!-- signatures: del(x) -->
### Function: del (x)

La expresión `del (x)` representa el diferencial de la variable $x$.


La función `diff` devuelve una expresión que contiene a `del` si no se ha especificado una variable independiente. En este caso, el valor retornado es el llamado "diferencial total".


Ejemplos:







```maxima
(%i1) diff (log (x));
                             del(x)
(%o1)                        ------
                               x
(%i2) diff (exp (x*y));
                     x y              x y
(%o2)            x %e    del(y) + y %e    del(x)
(%i3) diff (x*y*z);
(%o3)         x y del(z) + x z del(y) + y z del(x)
```

<!-- category: Other -->
<!-- keywords: delta -->
<!-- signatures: delta(t) -->
### Function: delta (t)

Es la función delta de Dirac.


En el estado actual de desarrollo de Maxima, sólo `laplace` reconoce la función `delta`.


Ejemplo:



```maxima
(%i1) laplace (delta (t - a) * sin(b*t), t, s);
Is  a  positive, negative, or zero?

p;
                                   - a s
(%o1)                   sin(a b) %e
```

<!-- category: Other -->
<!-- keywords: dependencies -->
<!-- signatures: dependencies -->
### Variable: dependencies

Valor por defecto: `[]`


La variable `dependencies` es la lista de átomos que tienen algún tipo de dependencia funcional, asignada por `depends` o `gradef`. La lista `dependencies` es acumulativa: cada llamada a `depends` o `gradef` añade elementos adicionales.


Véanse `depends` y `gradef`.

<!-- category: Other -->
<!-- keywords: depends -->
<!-- signatures: depends(f_1, x_1, ..., f_n, x_n) -->
### Function: depends (f_1, x_1, ..., f_n, x_n)

Declara dependencias funcionales entre variables con el propósito de calcular derivadas.
En ausencia de una dependencia declarada, `diff (f, x)` devuelve cero.
Si se declara `depends (f, x)`, `diff (f, x)` devuelve una derivada simbólica (esto es, una expresión con `diff`).


Cada argumento  *f_1*, *x_1*, etc., puede ser el nombre de una variable, de un arreglo o una lista de nombres.
Cada elemento de *f_i* (quizás un único elemento) se declara como dependiente de cada elemento de *x_i* (quizás también un único elemento). Si alguno de los  *f_i* es el nombre de un arreglo o contiene el nombre de un arreglo, todos los elemento del arregl dependen de *x_i*.


La función `diff` reconoce dependencias indirectas establecidas por `depends` y aplica la regla de la cadena en tales casos.


La instrucción `remove (f, dependency)` borra todas las dependencias declaradas para *f*.


La función `depends` devuelve una lista con las dependencias que han sido establecidas. Las dependencias se añaden a la variable global `dependencies`. La función `depends` evalúa sus argumentos.


La función `diff` es la única instrucción de Maxima que reconoce las dependencias establecidas por `depends`. Otras funciones (`integrate`, `laplace`, etc.) solamente reconocen dependencias explícitamente representadas por sus argumentos. Por ejemplo, `integrate` no reconoce la dependencia de `f` respecto de `x`
a menos que se represente explícitamente como `integrate (f(x), x)`.









```maxima
(%i1) depends ([f, g], x);
(%o1)                     [f(x), g(x)]
(%i2) depends ([r, s], [u, v, w]);
(%o2)               [r(u, v, w), s(u, v, w)]
(%i3) depends (u, t);
(%o3)                        [u(t)]
(%i4) dependencies;
(%o4)      [f(x), g(x), r(u, v, w), s(u, v, w), u(t)]
(%i5) diff (r.s, u);
                         dr           ds
(%o5)                    -- . s + r . --
                         du           du
```





```maxima
(%i6) diff (r.s, t);
                      dr du           ds du
(%o6)                 -- -- . s + r . -- --
                      du dt           du dt
```






```maxima
(%i7) remove (r, dependency);
(%o7)                         done
(%i8) diff (r.s, t);
                                ds du
(%o8)                       r . -- --
                                du dt
```

<!-- category: Other -->
<!-- keywords: derivabbrev -->
<!-- signatures: derivabbrev -->
### Variable: derivabbrev

Valor por defecto: `false`


Si `derivabbrev` vale `true`, las derivadas simbólicas (esto es, expresiones con `diff`) se muestran como subíndices. En otro caso, las derivadas se muestran en la notación de Leibniz, `dy/dx`.

<!-- category: Other -->
<!-- keywords: derivdegree -->
<!-- signatures: derivdegree(expr, y, x) -->
### Function: derivdegree (expr, y, x)

Devuelve el mayor grado de la derivada de la variable dependiente *y* respecto de la variable independiente *x* que aparece en *expr*.


Ejemplo:





```maxima
(%i1) 'diff (y, x, 2) + 'diff (y, z, 3) + 'diff (y, x) * x^2;
                         3     2
                        d y   d y    2 dy
(%o1)                   --- + --- + x  --
                          3     2      dx
                        dz    dx
(%i2) derivdegree (%, y, x);
(%o2)                           2
```

<!-- category: Other -->
<!-- keywords: derivlist -->
<!-- signatures: derivlist(var_1, ..., var_k) -->
### Function: derivlist (var_1, ..., var_k)

Hace que las derivadas calculadas por la instrucción `ev` se calculen respecto de las variables indicadas.

<!-- category: Other -->
<!-- keywords: derivsubst -->
<!-- signatures: derivsubst -->
### Variable: derivsubst

Valor por defecto: `false`


Si `derivsubst` vale `true`, una sustitución no sintáctica del estilo 
`subst (x, 'diff (y, t), 'diff (y, t, 2))` devuelve `'diff (x, t)`.

<!-- category: Other -->
<!-- keywords: diff -->
<!-- signatures: diff(expr, x_1, n_1, ..., x_m, n_m), diff(expr, x, n), diff(expr, x), diff(expr) -->
### Function: diff (expr, x_1, n_1, ..., x_m, n_m)

Devuelve la derivada o diferencial de  *expr* respecto de alguna o de todas las variables presentes en *expr*.


La llamada `diff (expr, x, n)` devuelve la *n*-esima derivada de *expr* respecto de *x*.


La llamada `diff (expr, x_1, n_1, ..., x_m, n_m)`
devuelve la derivada parcial de *expr* con respecto de *x_1*, ..., *x_m*.
Equivale a `diff (... (diff (expr, x_m, n_m) ...), x_1, n_1)`.


La llamada `diff (expr, x)`
devuelve la primera derivada de *expr* respecto de la variable *x*.


La llamada `diff (expr)` devuelve el diferencial total de *expr*, esto es, la suma de las derivadas de *expr* respecto de cada una de sus variables, multiplicadas por el diferencial `del` de cada una de ellas.




La forma nominal de `diff` es necesaria en algunos contextos, como para definir ecuaciones diferenciales.
En tales casos, `diff` puede ir precedida de un apóstrofo (como `'diff`) para evitar el cálculo de la derivada.


Si `derivabbrev` vale `true`, las derivadas se muestran como subíndices. En otro caso, se muestran en la notación de Leibniz, `dy/dx`.


Ejemplos:








```maxima
(%i1) diff (exp (f(x)), x, 2);
                     2
              f(x)  d               f(x)  d         2
(%o1)       %e     (--- (f(x))) + %e     (-- (f(x)))
                      2                   dx
                    dx
(%i2) derivabbrev: true$
(%i3) 'integrate (f(x, y), y, g(x), h(x));
                         h(x)
                        /
                        [
(%o3)                   I     f(x, y) dy
                        ]
                        /
                         g(x)
(%i4) diff (%, x);
       h(x)
      /
      [
(%o4) I     f(x, y)  dy + f(x, h(x)) h(x)  - f(x, g(x)) g(x)
      ]            x                     x                  x
      /
       g(x)
```


Para el paquete sobre tensores se han introducido las siguientes modificaciones:


(1) Las derivadas de los objetos indexados en *expr* tendrán las variables *x_i* añadidas como argumentos adicionales. Entonces se ordenarán todos los índices de derivadas.


(2) Las *x_i* pueden ser enteros entre 1 hasta el valor de la variable `dimension` [valor por defecto: 4].  Esto hará que la diferenciación sea llevada a cabo con respecto al *x_i*-ésimo número de la lista `coordinates`, la cual debería contener una lista con los nombres de las coordenadas, por ejemplo, `[x, y, z, t]`. Si `coordinates` es una variableis atómica, entonces esa variable será utilizada como variable de diferenciación. Se permite la utilización de arreglos con los nombres de las coordenadas o nombres con subíndices, como `X[1]`, `X[2]`, ... to be used.  Si a `coordinates` no se le ha asignado ningún valor, entonces las variables serán tratadas como se ha indicado en (1).

<!-- category: Other -->
<!-- keywords: express -->
<!-- signatures: express(expr) -->
### Function: express (expr)

Transforma los nombres de los operadores diferenciales en expresiones que contienen derivadas parciales. Los operadores reconocidos por la función `express` son: `grad` (gradiente), `div` (divergencia), `curl` (rotacional), `laplacian` (laplaciano) y `~` (producto vectorial).


Las derivadas simbólicas (es decir, las que incluyen la forma nominal `diff`) que aparecen en la expresión devuelta por `express`, se pueden calcular pasándole a `ev` el argumento `diff`, o escribiéndolo directamente en la línea de comandos. En este contexto, `diff` actúa como `evfun`.


Es necesario ejecutar `load ("vect")` para cargar esta función.


Ejemplos:



















```maxima
(%i1) load ("vect")$
(%i2) grad (x^2 + y^2 + z^2);
                              2    2    2
(%o2)                  grad (z  + y  + x )
(%i3) express (%);
       d    2    2    2   d    2    2    2   d    2    2    2
(%o3) [-- (z  + y  + x ), -- (z  + y  + x ), -- (z  + y  + x )]
       dx                 dy                 dz
(%i4) ev (%, diff);
(%o4)                    [2 x, 2 y, 2 z]
(%i5) div ([x^2, y^2, z^2]);
                              2   2   2
(%o5)                   div [x , y , z ]
(%i6) express (%);
                   d    2    d    2    d    2
(%o6)              -- (z ) + -- (y ) + -- (x )
                   dz        dy        dx
(%i7) ev (%, diff);
(%o7)                    2 z + 2 y + 2 x
(%i8) curl ([x^2, y^2, z^2]);
                               2   2   2
(%o8)                   curl [x , y , z ]
(%i9) express (%);
       d    2    d    2   d    2    d    2   d    2    d    2
(%o9) [-- (z ) - -- (y ), -- (x ) - -- (z ), -- (y ) - -- (x )]
       dy        dz       dz        dx       dx        dy
(%i10) ev (%, diff);
(%o10)                      [0, 0, 0]
(%i11) laplacian (x^2 * y^2 * z^2);
                                  2  2  2
(%o11)                laplacian (x  y  z )
(%i12) express (%);
         2                2                2
        d     2  2  2    d     2  2  2    d     2  2  2
(%o12)  --- (x  y  z ) + --- (x  y  z ) + --- (x  y  z )
          2                2                2
        dz               dy               dx
(%i13) ev (%, diff);
                      2  2      2  2      2  2
(%o13)             2 y  z  + 2 x  z  + 2 x  y
(%i14) [a, b, c] ~ [x, y, z];
(%o14)                [a, b, c] ~ [x, y, z]
(%i15) express (%);
(%o15)          [b z - c y, c x - a z, a y - b x]
```

<!-- category: Other -->
<!-- keywords: gradef -->
<!-- signatures: gradef(f(x_1, ..., x_n), g_1, ..., g_m), gradef(a, x, expr) -->
### Function: gradef (f(x_1, ..., x_n), g_1, ..., g_m)

Define las derivadas parciales, o componentes del gradiente, de la función *f* o variable *a*.


La llamada `gradef (f(x_1, ..., x_n), g_1, ..., g_m)`
define `df/dx_i` como *g_i*, 
donde *g_i* es una expresión; *g_i* puede ser una llamada a función, pero no el nombre de una función.
El número de derivadas parciales *m* puede ser menor que el número de argumentos *n*, en cuyo caso las derivadas se definen solamente con respecto a  *x_1*, ...., *x_m*.


La llamada `gradef (a, x, expr)` define la derivada de la variable *a* respecto de *x* en *expr*. Con esto se establece la dependencia de *a* respecto de *x* a través de `depends (a, x)`.


El primer argumento `f(x_1, ..., x_n)` o *a* no se evalúa, pero sí lo hacen el resto de argumentos *g_1*, ..., *g_m*.  La llamada a `gradef` devuelve la función o variable para la que se define la derivada parcial.


La instrucción `gradef` puede redefinir las derivadas de las funciones propias de Maxima.
Por ejemplo, `gradef (sin(x), sqrt (1 - sin(x)^2))` redefine la derivada de `sin`.


La instrucción `gradef` no puede definir derivadas parciales de funciones subindicadas.


La llamada `printprops ([f_1, ..., f_n], gradef)` muestra las derivadas parciales de las funciones *f_1*, ..., *f_n*, tal como las definió `gradef`.


La llamada `printprops ([a_n, ..., a_n], atomgrad)` muestra las derivadas parciales de las variables *a_n*, ..., *a_n*, tal como las definió `gradef`.


La variable `gradefs` contiene la lista de las funciones para las que se han definido derivadas parciales con la instrucción `gradef`, pero no incluye las variables para las que se han definido las derivadas parciales.



Los gradientes son necesarios cuando una función no se conoce explícitamente pero sí sus primeras derivadas y es necesario calcular las derivadas de orden mayor.

<!-- category: Other -->
<!-- keywords: gradefs -->
<!-- signatures: gradefs -->
### Variable: gradefs

Valor por defecto: `[]`


La variable `gradefs` contiene la lista de las funciones para las que se han definido derivadas parciales con la instrucción `gradef`, pero no incluye las variables para las que se han definido las derivadas parciales.

<!-- category: Other -->
<!-- keywords: laplace -->
<!-- signatures: laplace(expr, t, s) -->
### Function: laplace (expr, t, s)

Calcula la transformada de Laplace de *expr* con respecto
de la variable *t* y parámetro de transformación *s*.


La función `laplace` reconoce en *expr* las funciones
`delta`, `exp`, `log`, `sin`, `cos`,
`sinh`, `cosh` y `erf`, así como 
`derivative`, `integrate`, `sum` y `ilt`. 
Si `laplace` no encuentra una transformada, entonces
llama a la función `specint`, la cual puede encontrar
la transformada de Laplace de expresiones con funciones especiales,
tales como las de Bessel. `specint` también puede manipular la 
función `unit_step`. Véase `specint` para más información.


Cuando tampoco `specint` sea capaz de encontrar una solución,
se devolverá una forma nominal.






La función `laplace` reconoce integrales de convolución 
de la forma `integrate (f(x) * g(t - x), x, 0, t)`,
no pudiendo reconocer otros tipos de convoluciones.


Las relaciones funcionales se deben representar explícitamente en *expr*; las relaciones implícitas establecidas por `depends` no son reconocidas. Así, si *f* depende de *x* y *y*, `f (x, y)` debe aparecer en *expr*.


Véase también `ilt`, la transformada inversa de Laplace.


Ejemplos:








```maxima
(%i1) laplace (exp (2*t + a) * sin(t) * t, t, s);
                            a
                          %e  (2 s - 4)
(%o1)                    ---------------
                           2           2
                         (s  - 4 s + 5)
(%i2) laplace ('diff (f (x), x), x, s);
(%o2)             s laplace(f(x), x, s) - f(0)
(%i3) diff (diff (delta (t), t), t);
                          2
                         d
(%o3)                    --- (delta(t))
                           2
                         dt
(%i4) laplace (%, t, s);
                            !
               d            !         2
(%o4)        - -- (delta(t))!      + s  - delta(0) s
               dt           !
                            !t = 0
(%i5) assume(a>0)$
(%i6) laplace(gamma_incomplete(a,t),t,s),gamma_expand:true;
                                              - a - 1
                         gamma(a)   gamma(a) s
(%o6)                    -------- - -----------------
                            s            1     a
                                        (- + 1)
                                         s
(%i7) factor(laplace(gamma_incomplete(1/2,t),t,s));
                                              s + 1
                      sqrt(%pi) (sqrt(s) sqrt(-----) - 1)
                                                s
(%o7)                 -----------------------------------
                                3/2      s + 1
                               s    sqrt(-----)
                                           s
(%i8) assume(exp(%pi*s)>1)$
(%i9) laplace(sum((-1)^n*unit_step(t-n*%pi)*sin(t),n,0,inf),t,s),simpsum;
                         %i                         %i
              ------------------------ - ------------------------
                              - %pi s                    - %pi s
              (s + %i) (1 - %e       )   (s - %i) (1 - %e       )
(%o9)         ---------------------------------------------------
                                       2
(%i9) factor(%);
                                      %pi s
                                    %e
(%o9)                   -------------------------------
                                             %pi s
                        (s - %i) (s + %i) (%e      - 1)
```

