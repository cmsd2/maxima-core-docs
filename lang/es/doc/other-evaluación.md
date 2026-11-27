## Evaluación

<!-- category: Other -->
<!-- keywords: ' -->
<!-- signatures: ' -->
### Function: '

El operador comilla simple `'` evita la evaluación. 


Aplicado a un símbolo, 
la comilla simple evita la evaluación del símbolo. 


Aplicado a la llamada de una función,
la comilla simple evita la evaluación de la función llamada,
aunque los argumentos de la función son evaluados (siempre y cuando 
la evaluación no se evite de otra manera). 
El resultado es una forma de nombre de la función llamada.  


Aplicado a una expresión con paréntesis, 
la comilla simple evita la evaluación de todos los símbolos y llamadas a funciones que hayan en la expresión. 

E.g., `'(f(x))` significa que no se evalua la expresión `f(x)`. 
`'f(x)` (con la comilla simple aplicada a `f` en cambio de a `f(x)`)
significa el retorno de la forma de nombre de `f` aplicada a `[x]`. 


La comilla simple no evita la simplificación. 


Cuando el interruptor global `noundisp` es `true`, 
los nombres se muestran con una comilla simple. 
Este interruptor siempre tiene como valor `true` cuando 
se muestran definiciones de funciones. 


Ver también los operadores comilla-comilla `''` y `nouns`. 


Ejemplos:


Aplicado a un símbolo, 
la comilla simple evita la evaluación del símbolo. 









```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) aa^2;
(%o2)                        1048576
(%i3) 'aa^2;
                                 2
(%o3)                          aa
(%i4) ''%;
(%o4)                        1048576
```


Aplicado a la llamada de una función,
la comilla simple evita la evaluación de la función llamada,
aunque los argumentos de la función son evaluados (siempre y cuando 
la evaluación no se evite de otra manera). 
El resultado es una forma de nombre de la función llamada.  










```maxima
(%i1) x0: 5;
(%o1)                           5
(%i2) x1: 7;
(%o2)                           7
(%i3) integrate (x^2, x, x0, x1);
                               218
(%o3)                          ---
                                3
(%i4) 'integrate (x^2, x, x0, x1);
                             7
                            /
                            [   2
(%o4)                       I  x  dx
                            ]
                            /
                             5
(%i5) %, nouns;
                               218
(%o5)                          ---
                                3
```


Aplicado a una expresión con paréntesis, la comilla simple evita
la evaluación de todos los símbolos y llamadas a 
funciones que haya dentro en la expresión. 










```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) bb: 19;
(%o2)                          19
(%i3) sqrt(aa) + bb;
(%o3)                          51
(%i4) '(sqrt(aa) + bb);
(%o4)                     bb + sqrt(aa)
(%i5) ''%;
(%o5)                          51
```


La comilla simple no evita la simplificación. 







```maxima
(%i1) sin (17 * %pi) + cos (17 * %pi);
(%o1)                          - 1
(%i2) '(sin (17 * %pi) + cos (17 * %pi));
(%o2)                          - 1
```


Internamente, Maxima considera que las operaciones con números
decimales de coma flotante son simples simplificaciones.







```maxima
(%i1) sin(1.0);
(%o1)                          .8414709848078965
(%i2) '(sin(1.0));
(%o2)                          .8414709848078965
```

<!-- category: Other -->
<!-- keywords: '' -->
<!-- signatures: '' -->
### Function: ''

El operador comilla-comilla `''` (dos comillas simples) modifica la evaluación
en las expresiones de entrada.


Aplicado a cualquier expresión general *expr*, las dos comillas simples hacen que
el valor de *expr* sea sustituido por *expr* en la expresión de entrada.


Aplicado al operador de una expresión, el operador comilla-comilla hace que el operador
pase de ser un nombre a ser un verbo, a menos que ya sea un verbo.


El operador comilla-comilla es aplicado por el analizador sintáctico de entrada;
no se almacena como una parte de la expresión de entrada analizada.
Este operador se aplica siempre tan pronto como es detectado y no puede ser comentado con
una comilla simple. De esta manera, el operador comilla-comilla provoca la evaluación de
una expresión cuando ésta no estaba previsto que fuese evaluada, como en la
definición de funciones, expresiones lambda y expresiones comentadas con una comilla simple
`'`.


El operador comilla-comilla es reconocido tanto por `batch` como por `load`.


Véanse también el operador comilla simple `'` y `nouns`.


Ejemplos:


Aplicado a cualquier expresión general *expr*, las dos comillas simples hacen que
el valor de *expr* sea sustituido por *expr* en la expresión de entrada.



















```maxima
(%i1) expand ((a + b)^3);
                     3        2      2      3
(%o1)               b  + 3 a b  + 3 a  b + a
(%i2) [_, ''_];
                         3    3        2      2      3
(%o2)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i3) [%i1, ''%i1];
                         3    3        2      2      3
(%o3)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i4) [aa : cc, bb : dd, cc : 17, dd : 29];
(%o4)                   [cc, dd, 17, 29]
(%i5) foo_1 (x) := aa - bb * x;
(%o5)                 foo_1(x) := aa - bb x
(%i6) foo_1 (10);
(%o6)                      cc - 10 dd
(%i7) ''%;
(%o7)                         - 273
(%i8) ''(foo_1 (10));
(%o8)                         - 273
(%i9) foo_2 (x) := ''aa - ''bb * x;
(%o9)                 foo_2(x) := cc - dd x
(%i10) foo_2 (10);
(%o10)                        - 273
(%i11) [x0 : x1, x1 : x2, x2 : x3];
(%o11)                    [x1, x2, x3]
(%i12) x0;
(%o12)                         x1
(%i13) ''x0;
(%o13)                         x2
(%i14) '' ''x0;
(%o14)                         x3
```


Aplicado al operador de una expresión, la
doble comilla simple hace que el operador
pase de ser nominal a verbal, a menos que ya sea un verbo.









```maxima
(%i1) declare (foo, noun);
(%o1)                         done
(%i2) foo (x) := x - 1729;
(%o2)                 ''foo(x) := x - 1729
(%i3) foo (100);
(%o3)                       foo(100)
(%i4) ''foo (100);
(%o4)                        - 1629
```



El operador comilla-comilla es aplicado por el analizador sintáctico de entrada;
no se almacena como una parte de la expresión de entrada analizada.










```maxima
(%i1) [aa : bb, cc : dd, bb : 1234, dd : 5678];
(%o1)                 [bb, dd, 1234, 5678]
(%i2) aa + cc;
(%o2)                        dd + bb
(%i3) display (_, op (_), args (_));
                           _ = cc + aa

                         op(cc + aa) = +

                    args(cc + aa) = [cc, aa]

(%o3)                         done
(%i4) ''(aa + cc);
(%o4)                         6912
(%i5) display (_, op (_), args (_));
                           _ = dd + bb

                         op(dd + bb) = +

                    args(dd + bb) = [dd, bb]

(%o5)                         done
```


El operador comilla-comilla provoca la evaluación de
una expresión cuando ésta no estaba previsto que fuese evaluada, como en la
definición de funciones, expresiones lambda y expresiones comentadas con una comilla simple
`'`.
















```maxima
(%i1) foo_1a (x) := ''(integrate (log (x), x));
(%o1)               foo_1a(x) := x log(x) - x
(%i2) foo_1b (x) := integrate (log (x), x);
(%o2)           foo_1b(x) := integrate(log(x), x)
(%i3) dispfun (foo_1a, foo_1b);
(%t3)               foo_1a(x) := x log(x) - x

(%t4)           foo_1b(x) := integrate(log(x), x)

(%o4)                      [%t3, %t4]
(%i5) integrate (log (x), x);
(%o5)                     x log(x) - x
(%i6) foo_2a (x) := ''%;
(%o6)               foo_2a(x) := x log(x) - x
(%i7) foo_2b (x) := %;
(%o7)                    foo_2b(x) := %
(%i8) dispfun (foo_2a, foo_2b);
(%t8)               foo_2a(x) := x log(x) - x

(%t9)                    foo_2b(x) := %

(%o9)                      [%t7, %t8]
(%i10) F : lambda ([u], diff (sin (u), u));
(%o10)             lambda([u], diff(sin(u), u))
(%i11) G : lambda ([u], ''(diff (sin (u), u)));
(%o11)                  lambda([u], cos(u))
(%i12) '(sum (a[k], k, 1, 3) + sum (b[k], k, 1, 3));
(%o12)         sum(b , k, 1, 3) + sum(a , k, 1, 3)
                    k                  k
(%i13) '(''(sum (a[k], k, 1, 3)) + ''(sum (b[k], k, 1, 3)));
(%o13)             b  + a  + b  + a  + b  + a
                    3    3    2    2    1    1
```

<!-- category: Other -->
<!-- keywords: ev -->
<!-- signatures: ev(expr, arg_1, ..., arg_n) -->
### Function: ev (expr, arg_1, ..., arg_n)

Evalua la expresión *expr* en el entorno especificado
por los argumentos *arg_1*, ..., *arg_n*.
Los argumentos son interruptores (Variables Booleanas), variables de
asignación, ecuaciones y funciones. 
`ev` retorna el resultado (otra expresión) de la evaluación. 


La evaluación se realiza por etapas, como sigue: 



1. Primero se configura el entorno de acuerdo a los argumentos los
cuales pueden ser algunos o todos de la siguiente lista:  



  - *
`simp` causa que *expr* sea simplificada sin importar el valor de la variable interruptor `simp` la cual inhibe la simplificación cuando su valor es `false`.
  - *
`noeval` suprime la fase de evaluación de `ev` (Vea el paso (4) más adelante). 
Esto es muy útil en conjunción con otras variables interruptor y causan en *expr* que sea resimplificada sin ser reevaluada.
  - *
`nouns` causa la evaluación de las formas nominales
(típicamente funciones sin evaluar tales como
`'integrate` or `'diff`) en `expr`.
  - *
`expand` causa expansión.
  - *
`expand (m, n)` causa expansión, asignando los valores de `maxposex` y
`maxnegex` a *m* y *n*, respectivamente.
  - *
`detout` hace que cualesquiera matrices inversas calculadas en *expr* conserven su determinante fuera de la inversa, en vez de que divida a cada elemento.
  - *
`diff` realiza todas las diferenciaciones indicadas en *expr*.
  - *
`derivlist (x, y, z, ...)` realiza sólo las diferenciaciones con respecto a las variables indicadas.
  - *
`risch` hace que las integrales presentes en *expr* se evalúen mediante
el algoritmo de Risch. Véase también `risch`. Cuando se utiliza el 
símbolo especial `nouns`, se aplica la rutina estándar de integración.
  - *
`float` provoca la conversión de los números racionales no-enteros a números decimales de coma flotante.
  - *
`numer` causa que algunas funciones matemáticas (incluyendo potenciación) con argumentos numéricos sean evaluados como punto flotante. Esto causa que las variables en *expr* las cuales hayan sido declaradas como variables numéricas sean reemplazadas por sus respectivos valores. Esto también configura la variable interruptor `float` a `true`.
  - *
`pred` provoca la evaluación de los predicados (expresiones las cuales se evaluan a `true` o `false`).
  - *
`eval` provoca una post-evaluación extra de *expr* (véase el paso (5) más adelante), pudiendo aparecer
`eval` varias veces; por cada aparición de `eval`, la expresión es reevaluada.
  - *
`A`, donde `A` es un átomo declarado como una variable de tipo interruptor, (Vea `evflag`)
causa que `A` tenga como valor `true` durante 
la evaluación de *expr*.
  - *
`V: expresion` (o alternativamente `V=expresion`) causa que 
`V` tenga el valor de `expresion` durante la evaluación
de *expr*. Notese que si `V` es una opción Maxima, entonces
`expresion` se usa como su valor durante la evaluación de
*expr*. Si más de un argumento de `ev` es de este 
tipo entonces el vínculo se hace en paralelo. Si `V` es una
expresión no atómica entonces se hace una sustitución más que 
un vínculo.
  - *
`F` donde `F`, un nombre de función, ha sido declarado para 
ser una función de evaluación (Vea `evfun`) causa que
`F` sea aplicada a *expr*.
  - *
Cualquier otro nombre de función (e.g., `sum`) causa la evaluación de las ocurrencias de esos nombres en `expr` como si ellos fueran
verbos.
  - *
En adición de que una función ocurra en *expr* (digamos `F(x)`) puede ser definida localmente para el propósito de esta evaluación 
de *expr* pasando `F(x) := expresion` como un argumento a
`ev`.
  - *
Si un átomo no mencionado anteriormente o una variable o expresión 
con subíndices fueran pasadas como un argumento, esta es evaluada y
si el resultado es una ecuación o una asignación entonces el 
vínculo o sustitución se llevará a cabo. Si el resultado es una
lista entonces los miembros de la lista tratados como si ellos fueran
argumentos adicionales pasados a `ev`. Esto permite que una
lista de argumentos sea pasada (e.g., `[X=1, Y=A**2]`) o una lista
de nombres de ecuaciones (e.g., `[%t1, %t2]` donde `%t1` y
`%t2` son ecuaciones) tal como lo que es retornado por 
`solve`.


Los argumentos de `ev` pueden ser pasados en cualquier orden con excepción de la sustitución de ecuaciones las cuales son manipuladas en 
secuencia, de izquierda a derecha y las funciones de evaluación las 
cuales son compuestas, e.g., `ev (expr, ratsimp, realpart)`
es manipulada como `realpart (ratsimp (expr))`. 


Los interruptores `simp`, `numer` y `float` 
pueden también ser configurados localmente en una sentencia block, o
globalmente en Maxima para que su efecto permanezca hasta que
sean reconfiguradas.   


Si *expr* es una Expresión Racional Canónica (CRE, por sus siglas en inglés), entonces la expresión retornada por `ev` es también 
de tipo CRE, siempre que los interruptores `numer` y `float` no sean `true`.
2. Durante el paso (1), se fabrica una lista de las variables que no contienen subíndices que aparecen en el lado izquierdo de las ecuaciones en los
argumentos o en el valor de algunos argumentos si el valor es una ecuación. Las variables (variables que contienen subíndices las cuales no tienen asociado un arreglo de funciones como también las variables que no contienen subíndices) en la expresión *expr* son reemplazadas por sus valores globales, excepto por aquellos que aparezcan en esa lista. 
Usualmente, *expr* es sólo una etiqueta o un `%` 
(como en `%i2` en el ejemplo de más abajo) así que 
este paso simplemente recupera la expresión a la que hace referencia 
la etiqueta y así `ev` puede trabajarla.
3. Si algunas sustituciones son indicadas por los argumentos, ellas
serán llevadas a cabo ahora.
4. La expresión resultante es también reevaluada (a menos que uno de 
los argumentos fuese `noeval`) y simplificada de acuerdo a los 
argumentos. Notese que cualquier llamada a una función en *expr* 
será llevada a cabo después de que las variables sean evaluadas 
en ella y que `ev(F(x))` pueda comportarse como `F(ev(x))`.
5. Por cada aparición de `eval` en los argumentos, se repetirán los pasos (3) y (4).


Ejemplos:







```maxima
(%i1) sin(x) + cos(y) + (w+1)^2 + 'diff (sin(w), w);
                                     d                    2
(%o1)              cos(y) + sin(x) + -- (sin(w)) + (w + 1)
                                     dw
(%i2) ev (%, numer, expand, diff, x=2, y=1);
                               2
(%o2)                cos(w) + w  + 2 w + 2.449599732693821
```



Una sintaxis alternativa de alto nivel ha sido desarrollada para `ev`
por medio de la cual se pueden escribir solamente sus argumentos, sin 
el comando `ev()`; se trata de una forma de escritura simplificada:



```maxima
expr, arg_1, ..., arg_n
```


Esta sintaxis no está permitida dentro de otras expresiones, como
funciones, bloques, etc.


Nótese el proceso de vínculo en paralelo en el siguiente ejemplo:



```maxima
(%i3) programmode: false;
(%o3)                                false
(%i4) x+y, x: a+y, y: 2;
(%o4)                              y + a + 2
(%i5) 2*x - 3*y = 3$
(%i6) -3*x + 2*y = -4$
(%i7) solve ([%o5, %o6]);
Solución

                                          1
(%t7)                               y = - -
                                          5

                                         6
(%t8)                                x = -
                                         5
(%o8)                            [[%t7, %t8]]
(%i8) %o6, %o8;
(%o8)                              - 4 = - 4
(%i9) x + 1/x > gamma (1/2);
                                   1
(%o9)                          x + - > sqrt(%pi)
                                   x
(%i10) %, numer, x=1/2;
(%o10)                      2.5 > 1.772453850905516
(%i11) %, pred;
(%o11)                               true
```

<!-- category: Other -->
<!-- keywords: eval -->
<!-- signatures: eval -->
### Variable: eval

Como argumento en una llamada a `ev (expr)`, `eval` 
fuerza una evaluación extra de *expr*.


Véase también `ev`.


Ejemplo:










```maxima
(%i1) [a:b,b:c,c:d,d:e];
(%o1)                            [b, c, d, e]
(%i2) a;
(%o2)                                  b
(%i3) ev(a);
(%o3)                                  c
(%i4) ev(a),eval;
(%o4)                                  e
(%i5) a,eval,eval;
(%o5)                                  e
```

<!-- category: Other -->
<!-- keywords: evflag -->
<!-- signatures: evflag -->
### Variable: evflag

Cuando un símbolo *x* goza de la propiedad `evflag`,
las expresiones `ev(expr, x)` y `expr, x`
(en modo interactivo) equivalen a `ev(expr, x = true)`.
Esto es, a *x* se le asigna `true` al tiempo que se evalúa *expr*.


La expresión `declare(x, evflag)` dota a la variable *x*
de la propiedad `evflag`.


Los interruptores que tienen la propiedad `evflag` son: 



   algebraic           cauchysum       demoivre         
   dotscrules          %emode          %enumer     
   exponentialize      exptisolate     factorflag
   float               halfangles      infeval
   isolate_wrt_times   keepfloat       letrat
   listarith           logabs          logarc
   logexpand           lognegint
   m1pbranch           numer_pbranch   programmode
   radexpand           ratalgdenom     ratfac
   ratmx               ratsimpexpons   simp
   simpproduct         simpsum         sumexpand
   trigexpand


Ejemplos:

















```maxima
(%i1) sin (1/2);
                                 1
(%o1)                        sin(-)
                                 2
(%i2) sin (1/2), float;
(%o2)                   0.479425538604203
(%i3) sin (1/2), float=true;
(%o3)                   0.479425538604203
(%i4) simp : false;
(%o4)                         false
(%i5) 1 + 1;
(%o5)                         1 + 1
(%i6) 1 + 1, simp;
(%o6)                           2
(%i7) simp : true;
(%o7)                         true
(%i8) sum (1/k^2, k, 1, inf);
                            inf
                            ====
                            \     1
(%o8)                        >    --
                            /      2
                            ====  k
                            k = 1
(%i9) sum (1/k^2, k, 1, inf), simpsum;
                                 2
                              %pi
(%o9)                         ----
                               6
(%i10) declare (aa, evflag);
(%o10)                        done
(%i11) if aa = true then YES else NO;
(%o11)                         NO
(%i12) if aa = true then YES else NO, aa;
(%o12)                         YES
```

<!-- category: Other -->
<!-- keywords: evfun -->
<!-- signatures: evfun -->
### Variable: evfun

Cuando la función *F* goza de la propiedad `evfun`,
las expresiones `ev(expr, F)` y `expr, F`
(en modo interactivo) equivalen a `F(ev(expr))`.


Si se especifican dos o más funciones, *F*, *G*, etc., como poseedoras 
de la propiedad `evfun`, éstas se aplican en el mismo orden en el que han sido 
especificadas como tales.


La expresión `declare(F, evfun)` dota a la función  *F*
de la propiedad `evfun`.


Las funciones que tienen la propiedad `evfun` por defecto son: 





   bfloat          factor       fullratsimp
   logcontract     polarform    radcan
   ratexpand       ratsimp      rectform
   rootscontract   trigexpand   trigreduce


Ejemplos:




















```maxima
(%i1) x^3 - 1;
                              3
(%o1)                        x  - 1
(%i2) x^3 - 1, factor;
                                2
(%o2)                 (x - 1) (x  + x + 1)
(%i3) factor (x^3 - 1);
                                2
(%o3)                 (x - 1) (x  + x + 1)
(%i4) cos(4 * x) / sin(x)^4;
                            cos(4 x)
(%o4)                       --------
                               4
                            sin (x)
(%i5) cos(4 * x) / sin(x)^4, trigexpand;
                 4           2       2         4
              sin (x) - 6 cos (x) sin (x) + cos (x)
(%o5)         -------------------------------------
                                4
                             sin (x)
(%i6) cos(4 * x) / sin(x)^4, trigexpand, ratexpand;
                           2         4
                      6 cos (x)   cos (x)
(%o6)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i7) ratexpand (trigexpand (cos(4 * x) / sin(x)^4));
                           2         4
                      6 cos (x)   cos (x)
(%o7)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i8) declare ([F, G], evfun);
(%o8)                         done
(%i9) (aa : bb, bb : cc, cc : dd);
(%o9)                          dd
(%i10) aa;
(%o10)                         bb
(%i11) aa, F;
(%o11)                        F(cc)
(%i12) F (aa);
(%o12)                        F(bb)
(%i13) F (ev (aa));
(%o13)                        F(cc)
(%i14) aa, F, G;
(%o14)                      G(F(cc))
(%i15) G (F (ev (aa)));
(%o15)                      G(F(cc))
```

<!-- category: Other -->
<!-- keywords: infeval -->
<!-- signatures: infeval -->
### Variable: infeval

Habilita el modo de "evaluación infinita". `ev` repetidamente 
evalua una expresión hasta que se pare de hacer cambios. Para prevenir
que una variable, digamos `X`, sea evaluada sin parar en este modo, 
simplemente incluya `X='X` como argumento de `ev`. 
Esta claro que expresiones como `ev (X, X=X+1, infeval)` generarán un bucle infinito.

<!-- category: Other -->
<!-- keywords: noeval -->
<!-- signatures: noeval -->
### Variable: noeval

El símbolo `noeval` evita la fase de evaluación de `ev`.
Es útil conjuntamente con otras variables globales y para poder volver a 
simplificar expresiones sin tener que evaluarlas otra vez.

<!-- category: Other -->
<!-- keywords: nouns -->
<!-- signatures: nouns -->
### Variable: nouns

El símbolo `nouns` es una `evflag`, lo que significa 
que cuando se utilice como una opción de la instrucción `ev`, 
todas las formas nominales que aparezcan en una expresión las convierte en 
verbales, esto es, las evalúa.  Véanse también `noun`, `nounify`, 
`verb` y `verbify`.

<!-- category: Other -->
<!-- keywords: pred -->
<!-- signatures: pred -->
### Variable: pred

Cuando se utiliza como argumento en una llamada a
`ev (expr)`, `pred` provoca que los
predicados (expresiones que se reducen a `true` o
`false`) se evalúen.


Véase `ev`.


Ejemplo:







```maxima
(%i1) 1<2;
(%o1)                                1 < 2
(%i2) 1<2,pred;
(%o2)                                true
```

