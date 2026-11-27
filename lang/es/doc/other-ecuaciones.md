## Ecuaciones

<!-- category: Other -->
<!-- keywords: %rnum_list -->
<!-- signatures: %rnum_list -->
### Variable: %rnum_list

Valor por defecto: `[]`


La variable `%rnum_list` es la lista de variables introducidas en las
soluciones por la funciones `solve` y `algsys`.
Las variables `%r` se añaden a `%rnum_list` en su orden de creación.
Esto es útil para hacer sustituciones en la solución a posteriori.












```maxima
(%i1) solve ([x + y = 3], [x,y]);
(%o1)              [[x = 3 - %r1, y = %r1]]


(%i2) %rnum_list;
(%o2)                       [%r1]


(%i3) sol : solve ([x + 2*y + 3*z = 4], [x,y,z]);
(%o3)   [[x = - 2 %r3 - 3 %r2 + 4, y = %r3, z = %r2]]


(%i4) %rnum_list;
(%o4)                     [%r2, %r3]


(%i5) for i : 1 thru length (%rnum_list) do
        sol : subst (t[i], %rnum_list[i], sol)$


(%i6) sol;
(%o6)     [[x = - 2 t  - 3 t  + 4, y = t , z = t ]]
                     2      1           2       1
```

<!-- category: Other -->
<!-- keywords: algexact -->
<!-- signatures: algexact -->
### Variable: algexact

Valor por defecto: `false`


El contenido de la variable `algexact` afecta al comportamiento de `algsys` de la siguiente forma:


Si `algexact` vale `true`, `algsys` llamará siempre a `solve` y luego utilizará `realroots`.


Si `algexact` vale `false`, `solve` será llamada sólo si la ecuación no es univariante, o si es cuadrática o bicuadrática.


Sin embargo, `algexact: true` no garantiza que únicamente se obtengan soluciones exactas, ya que aunque `algsys` intente siempre dar soluciones exactas, dará resultados aproximados si no encuentra una solución mejor.

<!-- category: Other -->
<!-- keywords: algsys -->
<!-- signatures: algsys([expr_1, ..., expr_m], [x_1, ..., x_n]), algsys([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: algsys ([expr_1, ..., expr_m], [x_1, ..., x_n])

Resuelve el sistema de ecuaciones polinómicas *expr_1*, ..., *expr_m*
o las ecuaciones *eqn_1*, ..., *eqn_m* para las variables *x_1*, ..., *x_n*.
La expresión *expr* equivale a la ecuación `expr = 0`. Puede haber más ecuaciones que variables o viceversa.


La función `algsys` devuelve una lista de soluciones, cada una de las cuales consistente a su vez en una lista de ecuaciones asociando valores a las variables *x_1*, ..., *x_n* que satisfacen el sistema de ecuaciones.
Si `algsys` no puede encontrar soluciones devuelve la lista vacía `[]`.


Si es necesario se introducen en la solución los símbolos  `%r1`, `%r2`, ..., para representar parámetros arbitrarios; estas variables también se añaden a la lista `%rnum_list`.


El proceso que se sigue es el siguiente:


(1) Primero se factorizan las ecuaciones y se reparten en subsistemas.


(2) Para cada subsistema *S_i*, se seleccionan una ecuación *E* y una variable *x*. Se elige la variable que tenga grado menor. Entonces se calcula el resultado de *E* y *E_j* respecto de *x*, siendo las *E_j* el resto de ecuaciones del subsistema *S_i*. De aquí se obtiene otro subsistema *S_i’* con una incógnita menos, ya que *x* ha sido eliminada. El proceso ahora vuelve al paso (1).


(3) En ocasiones se obtiene un subsistema consistente en una única ecuación. Si la ecuación es multivariante y no se han introducido aproximaciones en formato decimal de coma flotante, entonces  se llama a `solve` para tratar de encontrar una solución exacta.


En algunos casos, `solve` no puede encontrar la solución, o si lo consigue puede que el resultado tenga una expresión muy grande.


Si la ecuación tiene una sóla incógnita y es lineal, o cuadrática o bicuadrática, entonces se llama a la función `solve` si no se han introducido aproximaciones en formato decimal. Si se han introducido aproximaciones, o si hay más de una incógnita, o si no es lineal, ni cuadrática ni bicuadrática, y si la variables `realonly` vale `true`, entonces se llama a la función `realroots` para calcular las soluciones reales.  Si
`realonly` vale `false`, entonces se llama a `allroots` para obtener las soluciones reales y complejas.


Si `algsys` devuelve una solución que tiene menos dígitos significativos de los requeridos, el usuario puede cambiar a voluntad el valor de `algepsilon` para obtener mayor precisión.


Si `algexact` vale `true`, se llamará siempre a `solve`.


Cuando `algsys` encuentra una ecuación con múltiples incógnitas y que contiene aproximaciones en coma flotante (normalmente debido a la imposibilidad de encontrar soluciones exactas en pasos anteriores), entonces no intenta aplicar los métodos exactos a estas ecuaciones y presenta el mensaje: 
"`algsys` cannot solve - system too complicated."


Las interacciones con `radcan` pueden dar lugar a expresiones grandes o complicadas. En tal caso, puede ser posible aislar partes del resultado con  `pickapart` o `reveal`.


Ocasionalmente, `radcan` puede introducir la unidad imaginaria `%i` en una solución que de hecho es real.


Ejemplos:













```maxima
(%i1) e1: 2*x*(1 - a1) - 2*(x - 1)*a2;
(%o1)              2 (1 - a1) x - 2 a2 (x - 1)
(%i2) e2: a2 - a1; 
(%o2)                        a2 - a1
(%i3) e3: a1*(-y - x^2 + 1); 
                                   2
(%o3)                   a1 (- y - x  + 1)
(%i4) e4: a2*(y - (x - 1)^2);
                                       2
(%o4)                   a2 (y - (x - 1) )
(%i5) algsys ([e1, e2, e3, e4], [x, y, a1, a2]);
(%o5) [[x = 0, y = %r1, a1 = 0, a2 = 0], 

                                  [x = 1, y = 0, a1 = 1, a2 = 1]]
(%i6) e1: x^2 - y^2;
                              2    2
(%o6)                        x  - y
(%i7) e2: -1 - y + 2*y^2 - x + x^2;
                         2        2
(%o7)                 2 y  - y + x  - x - 1
(%i8) algsys ([e1, e2], [x, y]);
                 1            1
(%o8) [[x = - -------, y = -------], 
              sqrt(3)      sqrt(3)

        1              1             1        1
[x = -------, y = - -------], [x = - -, y = - -], [x = 1, y = 1]]
     sqrt(3)        sqrt(3)          3        3
```

<!-- category: Other -->
<!-- keywords: allroots -->
<!-- signatures: allroots(expr), allroots(eqn) -->
### Function: allroots (expr)

Calcula aproximaciones numéricas de las raíces reales y complejas del polinomio *expr* o ecuación polinómica *eqn* de una variable.



Si la variable `polyfactor` vale `true` hace que la función 
`allroots` factorice el polinomio para números reales si el polinomio es real, o para números complejos si el polinomio es complejo.


La función `allroots` puede dar resultados inexactos en caso de que haya raíces múltiples.
Si el polinomio es real, `allroots (%i*p)`) puede alcanzar mejores aproximaciones que `allroots (p)`,
ya que `allroots` ejecuta entonces un algoritmo diferente.


La función `allroots` no opera sobre expresiones no polinómicas, pues requiere que el numerador sea reducible a un polinomio y el denominador sea, como mucho, un número complejo. 


Para polinomios complejos se utiliza el algoritmo de Jenkins y Traub descrito
en (Algorithm 419, *Comm. ACM*, vol. 15, (1972), p. 97). Para polinomios 
reales se utiliza el algoritmo de Jenkins descrito en 
(Algorithm 493, *ACM TOMS*, vol. 1, (1975), p.178).


Ejemplos:










```maxima
(%i1) eqn: (1 + 2*x)^3 = 13.5*(1 + x^5);
                            3          5
(%o1)              (2 x + 1)  = 13.5 (x  + 1)
(%i2) soln: allroots (eqn);
(%o2) [x = .8296749902129361, x = - 1.015755543828121, 

x = .9659625152196369 %i - .4069597231924075, 

x = - .9659625152196369 %i - .4069597231924075, x = 1.0]
(%i3) for e in soln
        do (e2: subst (e, eqn), disp (expand (lhs(e2) - rhs(e2))));
                      - 3.5527136788005E-15

                     - 5.32907051820075E-15

         4.44089209850063E-15 %i - 4.88498130835069E-15

        - 4.44089209850063E-15 %i - 4.88498130835069E-15

                       3.5527136788005E-15

(%o3)                         done
(%i4) polyfactor: true$
(%i5) allroots (eqn);
(%o5) - 13.5 (x - 1.0) (x - .8296749902129361)

                           2
 (x + 1.015755543828121) (x  + .8139194463848151 x

 + 1.098699797110288)
```

<!-- category: Other -->
<!-- keywords: backsubst -->
<!-- signatures: backsubst -->
### Variable: backsubst

Valor por defecto: `true`



Si `backsubst` vale `false`, evita la retrosustitución 
en `linsolve` tras la triangularización de las ecuaciones. 
Esto puede ser de utilidad en problemas muy grandes, en los que la
retrosustitución puede provocar la generación de expresiones
extremadamente largas.



```maxima
(%i1) eq1 : x + y + z = 6$
(%i2) eq2 : x - y + z = 2$
(%i3) eq3 : x + y - z = 0$
(%i4) backsubst : false$

(%i5) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o5)             [x = z - y, y = 2, z = 3]

(%i6) backsubst : true$

(%i7) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o7)               [x = 1, y = 2, z = 3]
```

<!-- category: Other -->
<!-- keywords: bfallroots -->
<!-- signatures: bfallroots(expr), bfallroots(eqn) -->
### Function: bfallroots (expr)

Calcula aproximaciones numéricas de las raíces
reales y complejas del polinomio *expr* o de la ecuación
polinómica *eqn* de una variable.


En todos los aspectos, `bfallroots` es idéntica a `allroots`,
excepto que `bfallroots` calcula las raíces en 
formato bigfloat (números decimales de precisión arbitraria).


Véase `allroots` para más información.

<!-- category: Other -->
<!-- keywords: breakup -->
<!-- signatures: breakup -->
### Variable: breakup

Valor por defecto: `true`


Si `breakup` vale `true`, `solve` expresa sus soluciones a las ecuaciones cúbicas y cuárticas en términos de subexpresiones comunes, las cuales son asignadas a etiquetas del tipo `%t1`, `%t2`, etc.
En otro caso, no se identifican subexpresiones comunes.


La asignación `breakup: true` sólo tiene efecto cuando `programmode` vale `false`.


Ejemplos:



```maxima
(%i1) programmode: false$
(%i2) breakup: true$
(%i3) solve (x^3 + x^2 - 1);

                        sqrt(23)    25 1/3
(%t3)                  (--------- + --)
                        6 sqrt(3)   54
Solution:

                                      sqrt(3) %i   1
                                      ---------- - -
                sqrt(3) %i   1            2        2   1
(%t4)    x = (- ---------- - -) %t3 + -------------- - -
                    2        2            9 %t3        3

                                      sqrt(3) %i   1
                                    - ---------- - -
              sqrt(3) %i   1              2        2   1
(%t5)    x = (---------- - -) %t3 + ---------------- - -
                  2        2             9 %t3         3

                                   1     1
(%t6)                  x = %t3 + ----- - -
                                 9 %t3   3
(%o6)                    [%t4, %t5, %t6]
(%i6) breakup: false$
(%i7) solve (x^3 + x^2 - 1);
Solution:

             sqrt(3) %i   1
             ---------- - -
                 2        2        sqrt(23)    25 1/3
(%t7) x = --------------------- + (--------- + --)
             sqrt(23)    25 1/3    6 sqrt(3)   54
          9 (--------- + --)
             6 sqrt(3)   54

                                              sqrt(3) %i   1    1
                                           (- ---------- - -) - -
                                                  2        2    3

           sqrt(23)    25 1/3  sqrt(3) %i   1
(%t8) x = (--------- + --)    (---------- - -)
           6 sqrt(3)   54          2        2

                                            sqrt(3) %i   1
                                          - ---------- - -
                                                2        2      1
                                      + --------------------- - -
                                           sqrt(23)    25 1/3   3
                                        9 (--------- + --)
                                           6 sqrt(3)   54

            sqrt(23)    25 1/3             1             1
(%t9)  x = (--------- + --)    + --------------------- - -
            6 sqrt(3)   54          sqrt(23)    25 1/3   3
                                 9 (--------- + --)
                                    6 sqrt(3)   54
(%o9)                    [%t7, %t8, %t9]
```

<!-- category: Other -->
<!-- keywords: dimension -->
<!-- signatures: dimension(eqn), dimension(eqn_1, ..., eqn_n) -->
### Function: dimension (eqn)

El paquete `dimen` es para análisis dimensional. La instrucción `load ("dimen")` carga el paquete y
`demo ("dimen")` presenta una pequeña demostración.

<!-- category: Other -->
<!-- keywords: dispflag -->
<!-- signatures: dispflag -->
### Variable: dispflag

Valor por defecto: `true`



Si `dispflag` vale `false`, entonces se inhibirá que Maxima muestre resultados de las funciones que resuelven ecuaciones cuando éstas son llamadas desde dentro de un bloque (`block`). Cuando un bloque termina con el signo del dólar, $, a la variable `dispflag` se le asigna `false`.

<!-- category: Other -->
<!-- keywords: funcsolve -->
<!-- signatures: funcsolve(eqn, g(t)) -->
### Function: funcsolve (eqn, g(t))

Devuelve `[g(t) = ...]`  o `[]`, dependiendo de que exista o no una función racional  `g(t)` que satisfaga *eqn*, la cual debe ser un polinomio de primer orden, lineal para `g(t)` y `g(t+1)`



```maxima
(%i1) eqn: (n + 1)*f(n) - (n + 3)*f(n + 1)/(n + 1)
                 = (n - 1)/(n + 2);
                            (n + 3) f(n + 1)   n - 1
(%o1)        (n + 1) f(n) - ---------------- = -----
                                 n + 1         n + 2
(%i2) funcsolve (eqn, f(n));

Dependent equations eliminated:  (4 3)
                                   n
(%o2)                f(n) = ---------------
                            (n + 1) (n + 2)
```


Aviso: esta es una implemetación rudimentaria, por lo que debe ser utilizada con cautela.

<!-- category: Other -->
<!-- keywords: globalsolve -->
<!-- signatures: globalsolve -->
### Variable: globalsolve

Valor por defecto: `false`


Si `globalsolve` vale `true`,
a las incógnitas de las ecuaciones se les asignan las soluciones encontradas por `linsolve` y
por `solve` cuando se resuelven sistemas de dos o más ecuaciones lineales.


Si `globalsolve` vale `false`,
las soluciones encontradas por `linsolve` y por `solve` cuando se resuelven sistemas de dos o más ecuaciones lineales se expresan como ecuaciones y a las incógnitas no se le asignan valores.


Cuando se resuelven ecuaciones que no son sistemas de dos o más ecuaciones lineales, `solve` ignora el valor de `globalsolve`. Otras funciones que resuelven ecuaciones (como `algsys`) ignoran siempre el valor de `globalsolve`.


Ejemplos:



```maxima
(%i1) globalsolve: true$
(%i2) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t2)                        x : --
                                 7

                                   1
(%t3)                        y : - -
                                   7
(%o3)                     [[%t2, %t3]]
(%i3) x;
                               17
(%o3)                          --
                               7
(%i4) y;
                                 1
(%o4)                          - -
                                 7
(%i5) globalsolve: false$
(%i6) kill (x, y)$
(%i7) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t7)                        x = --
                                 7

                                   1
(%t8)                        y = - -
                                   7
(%o8)                     [[%t7, %t8]]
(%i8) x;
(%o8)                           x
(%i9) y;
(%o9)                           y
```

<!-- category: Other -->
<!-- keywords: ieqn -->
<!-- signatures: ieqn(ie, unk, tech, n, guess) -->
### Function: ieqn (ie, unk, tech, n, guess)

El paquete `inteqn` se dedica a la resolución de ecuaciones integrales. Para hacer uso de él, ejecutar la instrucción `load ("inteqn")`.


El argumento *ie* es la ecuación integral; *unk* es la función incógnita; *tech* es el método a aplicar para efectuar la resolución del problema (*tech* = `first` significa: aplica el primer método que encuentre una solución; *tech* = `all` significa: aplica todos los métodos posibles); *n* es el número máximo de términos que debe tomar `taylor`, `neumann`, `firstkindseries` o `fredseries` (también es el máximo nivel de recursión para el método de diferenciación); *guess* es la solución candidata inicial para `neumann` o `firstkindseries`.


Valores por defecto para los argumentos segundo a quinto son:


*unk*: `p(x)`, donde *p* es la primera función desconocida que Maxima encuentra en el integrando y *x* es la variable que actúa como argumento en la primera aparición de *p* encontrada fuera de una integral en el caso de ecuaciones de segunda especie (`secondkind`), o es la única variable aparte de la de integración en el caso de ecuaciones de primera especie (`firstkind`). Si el intento de encontrar *x* falla, el usuario será consultado para suministrar una variable independiente.

<!-- category: Other -->
<!-- keywords: ieqnprint -->
<!-- signatures: ieqnprint -->
### Variable: ieqnprint

Valor por defecto: `true`


La variable `ieqnprint` controla el comportamiento del resultado retornado por la instrucción `ieqn`. Si `ieqnprint` vale `false`, la lista devuelta por la función `ieqn` tiene el formato


   

[*solución*, *método utilizado*, *nterms*, *variable*]


donde *variable* estará ausente si la solución es exacta; en otro caso, será la palabra `approximate` o `incomplete` según que la solución sea inexacta o que no tenga forma explícita, respectivamente. Si se ha utilizado un método basado en series, *nterms* es el número de términos utilizado, que puede ser menor que el `n` dado a `ieqn`.

<!-- category: Other -->
<!-- keywords: lhs -->
<!-- signatures: lhs(expr) -->
### Function: lhs (expr)

Devuelve el miembro izquierdo (es decir, el primer argumento)
de la expresión *expr*,
cuando el operador de *expr* es uno de los operadores
de relación `< <= = # equal notequal >= >`,
o un operadores de asignación `:= ::= : ::`,
o un operador infijo binario definido por el usuario mediante `infix`.


Si *expr* es un átomo o si su operador es diferente de los
citados más arriba, `lhs` devuelve *expr*.


Véase también `rhs`.


Ejemplo:



















```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [lhs (aa < bb), lhs (aa <= bb), 
       lhs (aa >= bb), lhs (aa > bb)];
(%o4)                   [aa, aa, aa, aa]
(%i5) [lhs (aa = bb), lhs (aa # bb), lhs (equal (aa, bb)),
       lhs (notequal (aa, bb))];
(%o5)                   [aa, aa, aa, aa]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [lhs (e1), lhs (e2), lhs (e3), lhs (e4)];
(%o10)               [foo(x), bar(y), x, x]
(%i11) infix ("][");
(%o11)                         ][
(%i12) lhs (aa ][ bb);
(%o12)                         aa
```

<!-- category: Other -->
<!-- keywords: linsolve -->
<!-- signatures: linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

Resuelve la lista de ecuaciones lineales simultáneas para la lista de variables. Las expresiones deben ser polinomios lineales respecto de las variables o ecuaciones.


Si `globalsolve` vale `true`,
a cada incógnita se le asigna el valor de la solución encontrada.


Si `backsubst` vale `false`, `linsolve`
no hace la sustitución tras la triangulariación de las ecuaciones. 
Esto puede ser necesario en problemas muy grandes en los que la
sustitución puede dar lugar a la generación de expresiones
enormes.


Si `linsolve_params` vale `true`, `linsolve` también genera símbolos `%r` para representar parámetros arbitrarios como los descritos para la función `algsys`. Si vale `false`, el resultado devuelto por `linsolve` expresará, si es el sistema es indeterminado, unas variables en función de otras.


Si `programmode` vale `false`,
`linsolve` muestra la solución con etiquetas de expresiones 
intermedias (`%t`) y devuelve las lista de etiquetas.




















```maxima
(%i1) e1: x + z = y;
(%o1)                       z + x = y
(%i2) e2: 2*a*x - y = 2*a^2;
                                       2
(%o2)                   2 a x - y = 2 a
(%i3) e3: y - 2*z = 2;
(%o3)                      y - 2 z = 2
(%i4) [globalsolve: false, programmode: true];
(%o4)                     [false, true]
(%i5) linsolve ([e1, e2, e3], [x, y, z]);
(%o5)            [x = a + 1, y = 2 a, z = a - 1]
(%i6) [globalsolve: false, programmode: false];
(%o6)                    [false, false]
(%i7) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t7)                       z = a - 1

(%t8)                        y = 2 a

(%t9)                       x = a + 1
(%o9)                    [%t7, %t8, %t9]
(%i9) ''%;
(%o9)            [z = a - 1, y = 2 a, x = a + 1]
(%i10) [globalsolve: true, programmode: false];
(%o10)                    [true, false]
(%i11) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t11)                      z : a - 1

(%t12)                       y : 2 a

(%t13)                      x : a + 1
(%o13)                 [%t11, %t12, %t13]
(%i13) ''%;
(%o13)           [z : a - 1, y : 2 a, x : a + 1]
(%i14) [x, y, z];
(%o14)                 [a + 1, 2 a, a - 1]
(%i15) [globalsolve: true, programmode: true];
(%o15)                    [true, true]
(%i16) linsolve ([e1, e2, e3], '[x, y, z]);
(%o16)           [x : a + 1, y : 2 a, z : a - 1]
(%i17) [x, y, z];
(%o17)                 [a + 1, 2 a, a - 1]
```

<!-- category: Other -->
<!-- keywords: linsolve_params -->
<!-- signatures: linsolve_params -->
### Variable: linsolve_params

Valor por defecto: `true`


Si `linsolve_params` vale `true`, `linsolve` también genera símbolos `%r` para representar parámetros arbitrarios como los descritos para la función `algsys`. Si vale `false`, el resultado devuelto por `linsolve` expresará, si es el sistema es indeterminado, unas variables en función de otras.

<!-- category: Other -->
<!-- keywords: linsolvewarn -->
<!-- signatures: linsolvewarn -->
### Variable: linsolvewarn

Valor por defecto: `true`


Si `linsolvewarn` vale `true`, `linsolve` mostrará el mensaje: "Dependent equations eliminated".

<!-- category: Other -->
<!-- keywords: multiplicities -->
<!-- signatures: multiplicities -->
### Variable: multiplicities

Valor por defecto: `not_set_yet`


La variable `multiplicities` es una con las multiplicidades de las soluciones encontradas por `solve` o
`realroots`.

<!-- category: Other -->
<!-- keywords: nroots -->
<!-- signatures: nroots(p, low, high) -->
### Function: nroots (p, low, high)

Devuelve el número de raíces reales del polinomio real univariante *p* en el intervalo semiabierto
`(low, high]`. Los extremos del intervalo pueden ser `minf` o `inf`, menos y más infinito.


La función `nroots` utiliza el método de las secuencias de Sturm.



```maxima
(%i1) p: x^10 - 2*x^4 + 1/2$
(%i2) nroots (p, -6, 9.1);
(%o2)                           4
```

<!-- category: Other -->
<!-- keywords: nthroot -->
<!-- signatures: nthroot(p, n) -->
### Function: nthroot (p, n)

Siendo `p` un polinomio de coeficientes enteros y `n` un entero positivo, `nthroot` devuelve un polinomio `q`, también de coeficientes enteros, tal que `q^n=p`, o un mensaje de error indicando que `p` no es una `n`-potencia exacta. Esta función es bastante más rápida que `factor` y que `sqfr`.

<!-- category: Other -->
<!-- keywords: polyfactor -->
<!-- signatures: polyfactor -->
### Variable: polyfactor

Valor por defecto: `false`


Cuando `polyfactor` vale `true`, las funciones
`allroots` y `bfallroots` factorizan el polinomio
sobre los números reales si el polinomio es real, o
factoriza sobre los complejos si el polinomio es complejo.


Véase un ejemplo en `allroots`.

<!-- category: Other -->
<!-- keywords: programmode -->
<!-- signatures: programmode -->
### Variable: programmode

Valor por defecto: `true`


Si `programmode` vale `true`, `solve`, `realroots`, `allroots` y `linsolve`
devuelve sus soluciones como elementos de una lista. 


Si `programmode` vale `false`, `solve` y las demás crean expresiones intermedias etiquetadas `%t1`, `t2`, etc., y les asinan las soluciones.



```maxima
(%i1) solve(x^2+x+1);
                    sqrt(3) %i + 1      sqrt(3) %i - 1
(%o1)        [x = - --------------, x = --------------]
                          2                   2
(%i2) programmode:false$
(%i3) solve(x^2+x+1);
Solution:

                              sqrt(3) %i + 1
(%t3)                   x = - --------------
                                    2

                             sqrt(3) %i - 1
(%t4)                    x = --------------
                                   2
(%o4)                        [%t4, %t5]
```

<!-- category: Other -->
<!-- keywords: realonly -->
<!-- signatures: realonly -->
### Variable: realonly

Valor por defecto: `false`


Si `realonly` vale `true`, `algsys` sólo devuelve aquellas soluciones exentas de la constante `%i`.

<!-- category: Other -->
<!-- keywords: realroots -->
<!-- signatures: realroots(expr, bound), realroots(eqn, bound), realroots(expr), realroots(eqn) -->
### Function: realroots (expr, bound)

Calcula aproximaciones racionales de las raíces reales del
polinomio *expr* o de la ecuación polinómica *eqn* de una variable,
dentro de la tolerancia especificada por *bound*.
Los coeficientes de *expr* o de *eqn* deben ser números literales,
por lo que las constantes simbólicas como `%pi` no son aceptadas.


La función `realroots` guarda las multiplicidades de las
raíces encontradas en la variable global `multiplicities`.


La función `realroots` genera una secuencia de Sturm para acotar cada
raíz, aplicando después el método de bisección para
afinar las aproximaciones. Todos los coeficientes se convierten a formas
racionales equivalentes antes de comenzar la búsqueda de las raíces,
de modo que los cálculos se realizan con aritmética exacta racional. Incluso en
el caso de que algunos coeficientes sean números decimales en coma flotante, los
resultados son racionales, a menos que se les fuerce a ser decimales con las variables
`float` o `numer`.


Si *bound* es menor que la unidad, todas las raíces enteras se expresan
en forma exacta. Si no se especifica *bound*, se le supone igual al valor de la
variable global `rootsepsilon`.


Si la variable global `programmode` vale `true`, la función 
`realroots` devuelve una lista de la forma `[x = x_1, x = x_2, ...]`.
Si `programmode` vale `false`, `realroots` crea etiquetas 
`%t1`, `%t2`, ... para las expresiones intermedias, les asigna valores y, finalmente,
devuelve la lista de etiquetas.


Ejemplos:








```maxima
(%i1) realroots (-1 - x + x^5, 5e-6);
                               612003
(%o1)                     [x = ------]
                               524288
(%i2) ev (%[1], float);
(%o2)                 x = 1.167303085327148
(%i3) ev (-1 - x + x^5, %);
(%o3)                - 7.396496210176905E-6
```








```maxima
(%i1) realroots (expand ((1 - x)^5 * (2 - x)^3 * (3 - x)), 1e-20);
(%o1)                 [x = 1, x = 2, x = 3]
(%i2) multiplicities;
(%o2)                       [5, 3, 1]
```

<!-- category: Other -->
<!-- keywords: rhs -->
<!-- signatures: rhs(expr) -->
### Function: rhs (expr)

Devuelve el miembro derecho (es decir, el segundo argumento)
de la expresión *expr*,
cuando el operador de *expr* es uno de los operadores
de relación `< <= = # equal notequal >= >`,
o un operadores de asignación `:= ::= : ::`,
o un operador infijo binario definido por el usuario mediante `infix`.


Si *expr* es un átomo o si su operador es diferente de los
citados más arriba, `rhs` devuelve *expr*.


Véase también `lhs`.


Ejemplo:



















```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [rhs (aa < bb), rhs (aa <= bb),
       rhs (aa >= bb), rhs (aa > bb)];
(%o4)                   [bb, bb, bb, bb]
(%i5) [rhs (aa = bb), rhs (aa # bb), rhs (equal (aa, bb)),
       rhs (notequal (aa, bb))];
(%o5)                   [bb, bb, bb, bb]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [rhs (e1), rhs (e2), rhs (e3), rhs (e4)];
(%o10)                  [2 x, 3 y, y, y]
(%i11) infix ("][");
(%o11)                         ][
(%i12) rhs (aa ][ bb);
(%o12)                         bb
```

<!-- category: Other -->
<!-- keywords: rootsconmode -->
<!-- signatures: rootsconmode -->
### Variable: rootsconmode

Valor por defecto: `true`


La variable `rootsconmode` controla el comportamiento de la instrucción `rootscontract`.  Véase `rootscontract` para más detalles.

<!-- category: Other -->
<!-- keywords: rootscontract -->
<!-- signatures: rootscontract(expr) -->
### Function: rootscontract (expr)

Convierte productos de raíces en raíces de productos. Por ejemplo, `rootscontract (sqrt(x)*y^(3/2))` devuelve `sqrt(x*y^3)`.


Si `radexpand` vale `true` y `domain` vale `real`,
`rootscontract` convierte `abs` en `sqrt`, por ejemplo,
`rootscontract (abs(x)*sqrt(y))` devuelve `sqrt(x^2*y)`.


La opción `rootsconmode` afecta el resultado de `rootscontract` como sigue:



```maxima
Problema            Valor de         Resultadod de
                  rootsconmode        rootscontract
      
x^(1/2)*y^(3/2)      false          (x*y^3)^(1/2)
x^(1/2)*y^(1/4)      false          x^(1/2)*y^(1/4)
x^(1/2)*y^(1/4)      true           (x*y^(1/2))^(1/2)
x^(1/2)*y^(1/3)      true           x^(1/2)*y^(1/3)
x^(1/2)*y^(1/4)      all            (x^2*y)^(1/4)
x^(1/2)*y^(1/3)      all            (x^3*y^2)^(1/6)
```


Si `rootsconmode` vale `false`, `rootscontract` contrae sólamente respecto de exponentes racionales cuyos denominadores sean iguales. La clave para los ejemplos `rootsconmode: true` es simplemente que 2 divide a 4 pero no a 3. La asignación `rootsconmode: all` hace que se calcule el mínimo común múltiplo de los denominadores de los exponentes.


La función `rootscontract` utiliza `ratsimp` de forma similar a como lo hace `logcontract`.


Ejemplos:


















```maxima
(%i1) rootsconmode: false$
(%i2) rootscontract (x^(1/2)*y^(3/2));
                                   3
(%o2)                      sqrt(x y )
(%i3) rootscontract (x^(1/2)*y^(1/4));
                                   1/4
(%o3)                     sqrt(x) y
(%i4) rootsconmode: true$
(%i5) rootscontract (x^(1/2)*y^(1/4));
(%o5)                    sqrt(x sqrt(y))
(%i6) rootscontract (x^(1/2)*y^(1/3));
                                   1/3
(%o6)                     sqrt(x) y
(%i7) rootsconmode: all$
(%i8) rootscontract (x^(1/2)*y^(1/4));
                              2   1/4
(%o8)                       (x  y)
(%i9) rootscontract (x^(1/2)*y^(1/3));
                             3  2 1/6
(%o9)                      (x  y )
(%i10) rootsconmode: false$
(%i11) rootscontract (sqrt(sqrt(x) + sqrt(1 + x))
                    *sqrt(sqrt(1 + x) - sqrt(x)));
(%o11)                          1
(%i12) rootsconmode: true$
(%i13) rootscontract (sqrt(5 + sqrt(5)) - 5^(1/4)*sqrt(1 + sqrt(5)));
(%o13)                          0
```

<!-- category: Other -->
<!-- keywords: rootsepsilon -->
<!-- signatures: rootsepsilon -->
### Variable: rootsepsilon

Valor por defecto: 1.0e-7


La variable `rootsepsilon` es la tolerancia que establece el intervalo de confianza para las raíces calculadas por la función `realroots`.

<!-- category: Other -->
<!-- keywords: solve -->
<!-- signatures: solve(expr, x), solve(expr), solve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: solve (expr, x)

Resuelve la ecuación algebraica *expr* de incógnita *x* y devuelve una lista de igualdades con la *x* despejada.  Si *expr* no es una igualdad, se supone que se quiere resolver la ecuación `expr = 0`.
El argumento *x* puede ser una función (por ejemplo, `f(x)`), u otra expresión no atómica, excepto una suma o producto. Puede omitirse *x* si *expr* contiene solamente una variable. El argumento *expr* puede ser una expresión racional y puede contener funciones trigonométricas, exponenciales, etc.


Se utiliza el siguiente método de resolución:


Sea *E* la expresión y *X* la incógnita. Si *E* es lineal respecto de *X* entonces *X* se resuelve de forma trivial. En caso contrario, si *E* es de la forma `A*X^N + B` entonces el resultado es `(-B/A)^1/N)` multiplicado por las `N`-ésimas raíces de la unidad.


Si *E* no es lineal respecto de *X* entonces el máximo común divisor de los exponentes de *X* en *E* (supóngase que es *N*) se divide entre los exponentes y la multiplicidad de las raíces se multiplica por *N*.  Entonces es llamado recursivamente `solve` para este resultado. Si *E* es factorizable entonces `solve` es invocado para cada uno de los factores.  Finalmente, `solve` usará, según sea necesario, las fórmulas cuadrática, cúbica o cuártica.


En caso de que *E* sea un polinomio respecto de una función de la incógnita, por ejemplo `F(X)`, entonces se calcula primero para  `F(X)` (sea *C* el resultado obtenido), entonces la ecuación `F(X)=C` se resuelve para *X* en el supuesto que se conozca la inversa de la función *F*.


Si la variable `breakup` vale `false` hará que `solve` muestre las soluciones de las ecuaciones cúbicas o cuárticas como expresiones únicas, en lugar de utilizar varias subexpresiones comunes, que es el formato por defecto.


A la variable `multiplicities` se le asignará una lista con las multiplicidades de las soluciones individuales devueltas por `solve`, `realroots` o `allroots`. La instrucción `apropos (solve)` hará que se muestren las variables optativas que de algún modo afectan al comportamiento de `solve`. Se podrá luego utilizar la función  `describe` para aquellas variables cuyo objeto no esté claro.


La llamada `solve ([eqn_1, ..., eqn_n], [x_1, ..., x_n])`
resuelve un sistema de ecuaciones polinómicas simultáneas (lineales o no) llamando a `linsolve` o `algsys` y devuelve una lista de listas con soluciones para las incógnitas. En caso de haberse llamado a `linsolve` esta lista contendrá una única lista de soluciones. La llamada a `solve` tiene dos listas como argumentos. La primera lista tiene las ecuaciones a resolver y la segunda son las incógnitas cuyos valores se quieren calcular. Si el número de variables en las ecuaciones es igual al número de incógnitas, el segundo argumento puede omitirse.


Si `programmode` vale `false`,
`solve` muestra la solución con etiquetas de expresiones 
intermedias (`%t`) y devuelve las lista de etiquetas.



Si `globalsolve` vale `true` y el problema consiste en resolver un sistema de dos o más ecuaciones lineales, a cada incógnita se le asigna el valor encontrado en la resolución del sistema.


Ejemplos:

















```maxima
(%i1) solve (asin (cos (3*x))*(f(x) - 1), x);

SOLVE is using arc-trig functions to get a solution.
Some solutions will be lost.
                            %pi
(%o1)                  [x = ---, f(x) = 1]
                             6
(%i2) ev (solve (5^f(x) = 125, f(x)), solveradcan);
                                log(125)
(%o2)                   [f(x) = --------]
                                 log(5)
(%i3) [4*x^2 - y^2 = 12, x*y - x = 2];
                      2    2
(%o3)             [4 x  - y  = 12, x y - x = 2]
(%i4) solve (%, [x, y]);
(%o4) [[x = 2, y = 2], [x = .5202594388652008 %i

 - .1331240357358706, y = .0767837852378778

 - 3.608003221870287 %i], [x = - .5202594388652008 %i

 - .1331240357358706, y = 3.608003221870287 %i

 + .0767837852378778], [x = - 1.733751846381093, 

y = - .1535675710019696]]
(%i5) solve (1 + a*x + x^3, x);
                                       3
              sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(%o5) [x = (- ---------- - -) (--------------- - -)
                  2        2      6 sqrt(3)      2

        sqrt(3) %i   1
       (---------- - -) a
            2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

                          3
 sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(---------- - -) (--------------- - -)
     2        2      6 sqrt(3)      2

         sqrt(3) %i   1
      (- ---------- - -) a
             2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

         3
 sqrt(4 a  + 27)   1 1/3               a
(--------------- - -)    - --------------------------]
    6 sqrt(3)      2                  3
                              sqrt(4 a  + 27)   1 1/3
                           3 (--------------- - -)
                                 6 sqrt(3)      2
(%i6) solve (x^3 - 1);
             sqrt(3) %i - 1        sqrt(3) %i + 1
(%o6)   [x = --------------, x = - --------------, x = 1]
                   2                     2
(%i7) solve (x^6 - 1);
           sqrt(3) %i + 1      sqrt(3) %i - 1
(%o7) [x = --------------, x = --------------, x = - 1, 
                 2                   2

                     sqrt(3) %i + 1        sqrt(3) %i - 1
               x = - --------------, x = - --------------, x = 1]
                           2                     2
(%i8) ev (x^6 - 1, %[1]);
                                      6
                      (sqrt(3) %i + 1)
(%o8)                 ----------------- - 1
                             64
(%i9) expand (%);
(%o9)                           0
(%i10) x^2 - 1;
                              2
(%o10)                       x  - 1
(%i11) solve (%, x);
(%o11)                  [x = - 1, x = 1]
(%i12) ev (%th(2), %[1]);
(%o12)                          0
```


Los í `%r` se utilizan para indicar parámetros en
las soluciones.



```maxima
(%i1) solve([x+y=1,2*x+2*y=2],[x,y]);

solve: dependent equations eliminated: (2)
(%o1)                      [[x = 1 - %r1, y = %r1]]
```


Véanse `algsys` y `%rnum_list` para más información.

<!-- category: Other -->
<!-- keywords: solvedecomposes -->
<!-- signatures: solvedecomposes -->
### Variable: solvedecomposes

Valor por defecto: `true`


Si `solvedecomposes` vale `true`, `solve` llama a `polydecomp` en caso de que se le pida resolver ecuaciones polinómicas.

<!-- category: Other -->
<!-- keywords: solveexplicit -->
<!-- signatures: solveexplicit -->
### Variable: solveexplicit

Valor por defecto: `false`


Si `solveexplicit` vale `true`, le inhibe a `solve` devolver soluciones implícitas, esto es, soluciones de la forma `F(x) = 0`, donde `F` es cierta función.

<!-- category: Other -->
<!-- keywords: solvefactors -->
<!-- signatures: solvefactors -->
### Variable: solvefactors

Valor por defecto: `true`



Si `solvefactors` vale `false`, `solve` no intenta factorizar la expresión.  Este valor `false` puede ser útil en algunos casos en los que la factorización no es necesaria.

<!-- category: Other -->
<!-- keywords: solvenullwarn -->
<!-- signatures: solvenullwarn -->
### Variable: solvenullwarn

Valor por defecto: `true`


Si `solvenullwarn` vale `true`,  `solve` muestra un mensaje de aviso si es llamado con una lista de ecuaciones vacía o con una lista de incógnitas vacía. Por ejemplo, `solve ([], [])` imprimirá dos mensajes de aviso y devolverá `[]`.

<!-- category: Other -->
<!-- keywords: solveradcan -->
<!-- signatures: solveradcan -->
### Variable: solveradcan

Valor por defecto: `false`


Si `solveradcan` vale `true`, `solve` llama a `radcan`, lo que hará que `solve` se ejecute de forma más lenta, pero permitirá que se resuelvan ciertas ecuaciones que contengan exponenciales y logaritmos.

<!-- category: Other -->
<!-- keywords: solvetrigwarn -->
<!-- signatures: solvetrigwarn -->
### Variable: solvetrigwarn

Valor por defecto: `true`



Si `solvetrigwarn` vale `true`, `solve` puede presentar un mensaje diciendo que está utilizando funciones trigonométricas inversas para resolver la ecuación, y que por lo tanto puede estar ignorando algunas soluciones.

