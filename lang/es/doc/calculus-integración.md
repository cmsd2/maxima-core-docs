## Integración

<!-- category: Calculus -->
<!-- keywords: changevar -->
<!-- signatures: changevar(expr, f(x,y), y, x) -->
### Function: changevar (expr, f(x,y), y, x)

Hace el cambio de variable dado por `f(x,y) = 0` en todas las integrales que aparecen en *expr* con la integración respecto de *x*. La nueva variable será *y*.




```maxima
(%i1) assume(a > 0)$
(%i2) 'integrate (%e**sqrt(a*y), y, 0, 4);
                      4
                     /
                     [    sqrt(a) sqrt(y)
(%o2)                I  %e                dy
                     ]
                     /
                      0
(%i3) changevar (%, y-z^2/a, z, y);
                      0
                     /
                     [                abs(z)
                   2 I            z %e       dz
                     ]
                     /
                      - 2 sqrt(a)
(%o3)            - ----------------------------
                                a
```


Si una expresión contiene formas nominales, como aquélla en la que aparece `'integrate` en el ejemplo, podrá ser evaluada por `ev` si se utiliza el término `nouns`. Por ejemplo, la expresión devuelta por `changevar` se puede evaluar haciendo `ev (%o3, nouns)`.


La función `changevar` también se puede utilizar para cambiar los índices de una suma o producto.  Sin embargo, debe tenerse en cuenta que cuando se realiza un cambio en una suma o producto, el mismo debe expresarse en términos de sumas, como `i = j+ ...`, no como una función de mayor grado.


Ejemplo:



```maxima
(%i4) sum (a[i]*x^(i-2), i, 0, inf);
                         inf
                         ====
                         \         i - 2
(%o4)                     >    a  x
                         /      i
                         ====
                         i = 0
(%i5) changevar (%, i-2-n, n, i);
                        inf
                        ====
                        \               n
(%o5)                    >      a      x
                        /        n + 2
                        ====
                        n = - 2
```

<!-- category: Calculus -->
<!-- keywords: dblint -->
<!-- signatures: dblint(f, r, s, a, b) -->
### Function: dblint (f, r, s, a, b)

Es una rutina para integrales dobles escrita en lenguaje Maxima y posteriormente traducida y compilada a código máquina. La instrucción `load ("dblint")` carga esta función. Utiliza el método de Simpson en las dos direcciones `x` e `y` para calcular



$$
\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx.
$$


```maxima
/b /s(x)
|  |
|  |    f(x,y) dy dx
|  |
/a /r(x)
```



La función *f* debe ser una función traducida o compilada de dos variables, a la vez que *r* y *s* deben ser cada una de ellas una función traducida o compilada de una variable, mientras que *a* y *b* deben ser números en coma flotante. La rutina tiene dos variables globales que determinan el número de divisiones de los intervalos `x` e `y`: `dblint_x` y `dblint_y`, ambos con un valor por defecto de 10, pero que pueden cambiarse de forma independiente a otros valores enteros (hay `2*dblint_x+1` puntos a calcular en la dirección `x` y `2*dblint_y+1` en la dirección `y`). La rutina subdivide el eje X y luego para cada valor de X calcula primero `r(x)` y `s(x)`; entonces se subdivide el eje Y entre `r(x)` y `s(x)`, evaluándose la integral a lo largo del eje Y aplicando la regla de Simpson; a continuación, se evalúa la integral a lo largo del eje X utilizando también la regla de Simpson tomando como valores de función las integrales sobre Y. Este procedimiento puede ser numéricamente inestable por múltiples motivos, pero es razonablemente rápido: evítese su uso con funciones con grandes oscilaciones o que tengan singularidades. Las integrales del eje Y dependen de la proximidad de los límites `r(x)` y `s(x)`, de manera que si la distancia `s(x) - r(x)` varía rápidamente con X, puede dar lugar errores importantes debido a truncamientos de diferente amplitud en las integrales de Y. Se puede aumentar `dblint_x` y `dblint_y` al objeto de mejorar el recubrimiento de la región de integración, pero a costa del tiempo de cómputo. Es necesario que las funciones *f*, *r* y *s* estén traducidas o compiladas antes de utilizar `dblint`, lo cual redundará en una mejora del tiempo de ejecución de varios órdenes de magnitud respecto de la ejecución de código interpretado.

<!-- category: Calculus -->
<!-- keywords: defint -->
<!-- signatures: defint(expr, x, a, b) -->
### Function: defint (expr, x, a, b)

Intenta calcular una integral definida. La función `defint` es invocada por  `integrate` cuando se especifican los límites de integración, por ejemplo `integrate (expr, x, a, b)`. Así, desde el punto de vista del usuario, es suficiente con utilizar `integrate`.



La función `defint` devuelve una expresión simbólica, bien sea el resultado calculado o la forma nominal.
Véase `quad_qag` y sus funciones relacionadas para aproximaciones numéricas de integrales definidas.

<!-- category: Calculus -->
<!-- keywords: erfflag -->
<!-- signatures: erfflag -->
### Variable: erfflag

Valor por defecto: `true`


Si `erfflag` vale `false`, la función `risch` no introduce la función `erf` en el resultado si no había ninguna en el integrando.

<!-- category: Calculus -->
<!-- keywords: ilt -->
<!-- signatures: ilt(expr, s, t) -->
### Function: ilt (expr, s, t)

Calcula la transformada inversa de Laplace de *expr* con respecto de *s* y parámetro *t*. El argumento  *expr* debe ser una fracción de polinomios cuyo denominador tenga sólo factores lineales y cuadráticos. Utilizando las funciones `laplace` y `ilt`, junto con las funciones `solve` o `linsolve`, el usuario podrá resolver ciertas ecuaciones integrales.



```maxima
(%i1) 'integrate (sinh(a*x)*f(t-x), x, 0, t) + b*f(t) = t**2;
              t
             /
             [                                    2
(%o1)        I  f(t - x) sinh(a x) dx + b f(t) = t
             ]
             /
              0
(%i2) laplace (%, t, s);
                               a laplace(f(t), t, s)   2
(%o2)  b laplace(f(t), t, s) + --------------------- = --
                                       2    2           3
                                      s  - a           s
(%i3) linsolve ([%], ['laplace(f(t), t, s)]);
                                        2      2
                                     2 s  - 2 a
(%o3)     [laplace(f(t), t, s) = --------------------]
                                    5         2     3
                                 b s  + (a - a  b) s
(%i4) ilt (rhs (first (%)), s, t);
Is  a b (a b - 1)  positive, negative, or zero?

pos;
               sqrt(a b (a b - 1)) t
        2 cosh(---------------------)       2
                         b               a t
(%o4) - ----------------------------- + -------
              3  2      2               a b - 1
             a  b  - 2 a  b + a

                                                       2
                                             + ------------------
                                                3  2      2
                                               a  b  - 2 a  b + a
```

<!-- category: Calculus -->
<!-- keywords: intanalysis -->
<!-- signatures: intanalysis -->
### Variable: intanalysis

Valor por defecto: `true`


Cuando vale `true`, la integración definida trata de encontrar polos
en el integrando dentro del intervalo de integración. Si encuentra 
alguno, entonces la integral se calcula como valor principal. Si `intanalysis`
vale `false`, entonces no se realiza esta comprobaciÃ³n y la integración se
realiza sin tener en cuenta los polos.


Véase también `ldefint`.


Ejemplos:


Maxima puede calcular las siguientes integrales cuando a `intanalysis`
se le asigna el valor `false`:










```maxima
(%i1) integrate(1/(sqrt(x)+1),x,0,1);
                                1
                               /
                               [       1
(%o1)                          I  ----------- dx
                               ]  sqrt(x) + 1
                               /
                                0

(%i2) integrate(1/(sqrt(x)+1),x,0,1),intanalysis:false;
(%o2)                            2 - 2 log(2)

(%i3) integrate(cos(a)/sqrt((tan(a))^2 +1),a,-%pi/2,%pi/2);
The number 1 isn't in the domain of atanh
 -- an error. To debug this try: debugmode(true);

(%i4) intanalysis:false$
(%i5) integrate(cos(a)/sqrt((tan(a))^2+1),a,-%pi/2,%pi/2);
                                      %pi
(%o5)                                 ---
                                       2
```

<!-- category: Calculus -->
<!-- keywords: integrate -->
<!-- signatures: integrate(expr, x), integrate(expr, x, a, b) -->
### Function: integrate (expr, x)

Calcula simbólicamente la integral de *expr* respecto de *x*. La llamada
`integrate (expr, x)` resuelve una integral indefinida, mientras que 
 `integrate (expr, x, a, b)` resuelve una integral definida con 
límites de integración *a* y *b*.
Los límites no pueden contener a *x*. El argumento
*a* no necesita ser menor que *b*.
Si *b* es igual a *a*, `integrate` devuelve cero.


Véase `quad_qag` y funciones relacionadas para la aproximación numérica de integrales definidas.
Véase `residue` para el cálculo de residuos (integración compleja).
Véase `antid` para un método alternativo de resolución de integrales indefinidas.


Se obtendrá una integral (es decir, una expresión sin `integrate`) si `integrate` tiene éxito en el cálculo. En otro caso, la respuesta es la forma nominal de la integral (esto es, el operador `'integrate` precedido de apóstrofo) o una expresión que contiene una o más formas nominales. La forma nominal de `integrate` se muestra con un símbolo integral.


En ciertos casos es útil proporcionar una forma nominal ’a mano’, haciendo preceder `integrate` con una comilla simple o apóstrofo, como en `'integrate (expr, x)`.
Por ejemplo, la integral puede depender de algunos parámetros que todavía no han sido calculados.
La forma nominal puede aplicarse después a sus argumentos haciendo `ev (i, nouns)`
donde *i* es la forma nominal de interés.



La función `integrate` trata de manera diferente las integrales definidas de las indefinidas,
empleando una batería de heurísticas especial para cada caso.
Casos especiales de integrales definidas incluyen las que tienen límites de integración iguales a cero o a infinito (`inf` o `minf`), funciones trigonométricas con límites de integración igual a cero y `%pi` o `2 %pi`, funciones racionales, integrales relacionadas con las funciones `beta` y `psi` y algunas integrales logarítmicas y trigonométricas. El tratamiento de funciones racionales puede incluir el cálculo de residuos.
Si no se reconoce ninguno de los casos especiales, se intenta resolver la integral idefinida y evaluarla en los límites de integración. Esto incluye tomar límites cuando alguno de los extremos del intervalo de integración se acerca a más infinito o a menos infinito; véase también `ldefint`.


Casos especiales de integrales indefinidas incluyen a las funciones trigonométricas, exponenciales, logarítmicas y racionales. La función `integrate` también hace uso de una pequeña tabla de integrales elementales.


La función `integrate` puede llevar a cabo cambios de variable si el integrando es de la forma `f(g(x)) * diff(g(x), x)`, entonces `integrate` trata de encontrar una subexpresión de `g(x)` tal que la derivada de  `g(x)` divida el integrando. Esta búsqueda puede hacer uso de las derivadas establecidas con la función `gradef`.
Véanse también `changevar` y `antid`.


Si ninguna de las heurísticas descritas resuelve la integral indefinida, se ejecuta el algoritmo de Risch.
La variable `risch` puede utilizarse como una `evflag`, en una llamada a `ev` o en la línea de comandos
por ejemplo, `ev (integrate (expr, x), risch)` o `integrate (expr, x), risch`.
Si `risch` está presenta, `integrate` llama a la función `risch` sin intentar primero las heurísticas. Véase también `risch`.



La función `integrate` opera únicamente con relaciones funcionales que se representen explícitamente con la notación `f(x)`, sin considerar las dependencias implícitas establecidas mediante la función `depends`.


Es posible que `integrate` necesite conocer alguna propiedad de alguno de los parámetros presentes en el integrando, en cuyo caso `integrate` consultará en primer lugar la base de datos creada con `assume`, y si la variable de interés no se encuentra ahí, `integrate` le preguntará al usuario. Dependiendo de la pregunta, posibles respuestas son: `yes;`, `no;`, `pos;`, `zero;` o `neg;`.


Por defecto, `integrate` no se considera lineal. Véanse `declare` y `linear`.


La función `integrate` intentará la integración por partes sólo en casos especiales.


Ejemplos:



- *
Integrales elementales indefinidas y definidas.

```maxima
(%i1) integrate (sin(x)^3, x);
                           3
                        cos (x)
(%o1)                   ------- - cos(x)
                           3
(%i2) integrate (x/ sqrt (b^2 - x^2), x);
                                 2    2
(%o2)                    - sqrt(b  - x )
(%i3) integrate (cos(x)^2 * exp(x), x, 0, %pi);
                               %pi
                           3 %e      3
(%o3)                      ------- - -
                              5      5
(%i4) integrate (x^2 * exp(-x^2), x, minf, inf);
                            sqrt(%pi)
(%o4)                       ---------
                                2
```
- *
Utilización de `assume` e interacción.

```maxima
(%i1) assume (a > 1)$
(%i2) integrate (x**a/(x+1)**(5/2), x, 0, inf);
    2 a + 2
Is  -------  an integer?
       5
no;
Is  2 a - 3  positive, negative, or zero?
neg;
                                   3
(%o2)                  beta(a + 1, - - a)
                                   2
```
- *
Cambio de variable. En este ejemplo hay dos cambios de variable:
uno utilizando una derivada establecida con `gradef` y otra utilizando la derivada `diff(r(x))` de una función no especificada `r(x)`.

```maxima
(%i3) gradef (q(x), sin(x**2));
(%o3)                         q(x)
(%i4) diff (log (q (r (x))), x);
                      d               2
                     (-- (r(x))) sin(r (x))
                      dx
(%o4)                ----------------------
                            q(r(x))
(%i5) integrate (%, x);
(%o5)                     log(q(r(x)))
```
- *
El valor devuelto contiene la forma nominal `'integrate`.
En este ejemplo, Maxima puede extraer un factor del denominador de una función racional, pero no puede factorizar el resto. La función `grind` muestra la forma nominal `'integrate` del resultado.
Véase también `integrate_use_rootsof` para más información sobre integrales de funciones racionales.

```maxima
(%i1) expand ((x-4) * (x^3+2*x+1));
                    4      3      2
(%o1)              x  - 4 x  + 2 x  - 7 x - 4
(%i2) integrate (1/%, x);
                              /  2
                              [ x  + 4 x + 18
                              I ------------- dx
                              ]  3
                 log(x - 4)   / x  + 2 x + 1
(%o2)            ---------- - ------------------
                     73               73
(%i3) grind (%);
log(x-4)/73-('integrate((x^2+4*x+18)/(x^3+2*x+1),x))/73$
```
- *
Definición de una función mediante una integral.
El cuerpo de una función no se evalúa cuando ésta se define, de manera que el cuerpo de 
`f_1` en este ejemplo contiene la forma nominal de `integrate`.
El operador comilla-comilla `''` hace que se evalúe la integral y su resultado será el que defina a la función `f_2`.

```maxima
(%i1) f_1 (a) := integrate (x^3, x, 1, a);
                                     3
(%o1)           f_1(a) := integrate(x , x, 1, a)
(%i2) ev (f_1 (7), nouns);
(%o2)                          600
(%i3) /* Note parentheses around integrate(...) here */
      f_2 (a) := ''(integrate (x^3, x, 1, a));
                                   4
                                  a    1
(%o3)                   f_2(a) := -- - -
                                  4    4
(%i4) f_2 (7);
(%o4)                          600
```

<!-- category: Calculus -->
<!-- keywords: integrate_use_rootsof -->
<!-- signatures: integrate_use_rootsof -->
### Variable: integrate_use_rootsof

Valor por defecto: `false`


Si `integrate_use_rootsof` vale `true` y el denominador de una función racional no se puede factorizar,  `integrate` devuelve la integral como una suma respecto de las raíces desconocidas del denominador.


Por ejemplo, dándole a `integrate_use_rootsof` el valor `false`,
`integrate` devuelve la integral no resuelta de la función racional en forma nominal:



```maxima
(%i1) integrate_use_rootsof: false$
(%i2) integrate (1/(1+x+x^5), x);
        /  2
        [ x  - 4 x + 5
        I ------------ dx                            2 x + 1
        ]  3    2                2            5 atan(-------)
        / x  - x  + 1       log(x  + x + 1)          sqrt(3)
(%o2)   ----------------- - --------------- + ---------------
                7                 14             7 sqrt(3)
```


Si ahora se le da a la variable el valor `true`, la parte no resuelta de la integral se expresa como una suma cuyos sumandos dependen de las raíces del denominador de la función racional:



```maxima
(%i3) integrate_use_rootsof: true$
(%i4) integrate (1/(1+x+x^5), x);
      ====        2
      \       (%r4  - 4 %r4 + 5) log(x - %r4)
       >      -------------------------------
      /                    2
      ====            3 %r4  - 2 %r4
                        3      2
      %r4 in rootsof(%r4  - %r4  + 1, %r4)
(%o4) ----------------------------------------------------------
               7

                                                       2 x + 1
                                   2            5 atan(-------)
                              log(x  + x + 1)          sqrt(3)
                            - --------------- + ---------------
                                    14             7 sqrt(3)
```


Alternativamente, el usuario puede calcular las raíces del denominador separadamente y luego representar el integrando en función de dichas raíces, como por ejemplo `1/((x - a)*(x - b)*(x - c))` o `1/((x^2 - (a+b)*x + a*b)*(x - c))`
si el denominador es un polinomio de tercer grado. En algunos casos, esto ayudará a Maxima mejorar sus resultados.

<!-- category: Calculus -->
<!-- keywords: integration_constant -->
<!-- signatures: integration_constant -->
### Variable: integration_constant

Valor por defecto: `%c`


Cuando una constante de integración se crea durante la integración definida
de una ecuación, el nombre de la constante se construye concatenando
`integration_constant` y `integration_constant_counter`.


A `integration_constant` se le puede asignar un símbolo cualquiera.


Ejemplos:








```maxima
(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integration_constant : 'k;
(%o2)                           k


(%i3) integrate (x^2 = 1, x);
                            3
                           x
(%o3)                      -- = x + k2
                           3
```

<!-- category: Calculus -->
<!-- keywords: integration_constant_counter -->
<!-- signatures: integration_constant_counter -->
### Variable: integration_constant_counter

Valor por defecto: 0


Cuando una constante de integración se crea durante la integración definida
de una ecuación, el nombre de la constante se construye concatenando
`integration_constant` y `integration_constant_counter`.


La variable `integration_constant_counter` se incrementa antes de construir la
constante de integración siguiente.


Ejemplos:










```maxima
(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integrate (x^2 = 1, x);
                           3
                          x
(%o2)                     -- = x + %c2
                          3


(%i3) integrate (x^2 = 1, x);
                           3
                          x
(%o3)                     -- = x + %c3
                          3


(%i4) reset (integration_constant_counter);
(%o4)            [integration_constant_counter]


(%i5) integrate (x^2 = 1, x);
                           3
                          x
(%o5)                     -- = x + %c1
                          3
```

<!-- category: Calculus -->
<!-- keywords: ldefint -->
<!-- signatures: ldefint(expr, x, a, b) -->
### Function: ldefint (expr, x, a, b)

Calcula la integral definida de *expr* utilizando `limit` tras el cálculo de la integral indefinida de *expr* respecto a *x* en los extremos de integración *b* y *a*.
Si no consigue calcular la integral definida,
`ldefint` devuelve una expresión con los límites en forma nominal.


La función `integrate` no llama a `ldefint`,
de modo que la ejecución de `ldefint (expr, x, a, b)` puede dar un resultado diferente que 
`integrate (expr, x, a, b)`. La función 
`ldefint` siempre utiliza el mismo método para calcular la integral definida,
mientras que `integrate` puede hacer uso de varias heurísticas y reconocer así casos especiales.

<!-- category: Calculus -->
<!-- keywords: quad_control -->
<!-- signatures: quad_control(parameter, [value]) -->
### Function: quad_control (parameter, [value])

Controla la gestión de los errores de `QUADPACK`. El parámetro debe
ser uno de los siguientes símbolos:



**current_error** — El número de error actual.
**control** — Controla si los mensajes se imprimen o no. Si el valor es cero o menor,
los mensajes se suprimen.
**max_message** — El máximo número de veces que se imprime cualquier mensaje.


Si no se da *value*, entonces se devuelve el valor actual asociado a
*parameter*. En cambio, si se da *value*, se hace la asignación
correspondiente a *parameter*, adquiriendo este nuevo valor.

<!-- category: Calculus -->
<!-- keywords: quad_qag -->
<!-- signatures: quad_qag(f(x), x, a, b, key, [epsrel, epsabs, limit]), quad_qag(f, x, a, b, key, [epsrel, epsabs, limit]) -->
### Function: quad_qag (f(x), x, a, b, key, [epsrel, epsabs, limit])

Integración de una función general en un intervalo finito.
La función `quad_qag` implementa un integrador global 
adaptativo simple utilizando una estrategia de Aind (Piessens, 1973).
Se puede escoger entre seis pares de fórmulas de cuadratura de
Gauss-Kronrod para la regla de evaluación.
Las reglas de rango superior son útiles en los casos en los que
los integrandos tienen un alto grado de oscilación.


La función `quad_qag` calcula numéricamente la integral



$$
\int_a^b {f(x) dx}
$$


utilizando un integrador adaptativo simple.


La función a integrar es *f(x)*, con variable independiente *x*,
siendo el intervalo de integración el comprendido entre *a* y *b*.
El argumento *key* indica el integrador a utilizar y debe ser un número
entero entre 1 y 6, ambos inclusive.  El valor de *key* selecciona el
orden de la regla de integración de Gauss-Kronrod.
Las reglas de rango superior son útiles en los casos en los que
los integrandos tienen un alto grado de oscilación.


El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima.


La integración numérica se hace de forma adaptativa particionando la región de integración en subintervalos hasta conseguir la precisión requerida.


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsrel** — Error relativo deseado de la aproximación. El valor por defecto es 1d-8.
**epsabs** — Error absoluto deseado de la aproximación. El valor por defecto es 0.
**limit** — Tamaño del array interno utilizado para realizar la cuadratura. 
*limit* es el número máximo de subintervalos
a utilizar. El valor por defecto es 200.


La función `quad_qag` devuelve una lista de cuatro elementos:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**6** — si los argumentos de entrada no son válidos.




Ejemplos:



```maxima
(%i1) quad_qag (x^(1/2)*log(1/x), x, 0, 1, 3, 'epsrel=5d-8);
(%o1)    [.4444444444492108, 3.1700968502883E-9, 961, 0]
(%i2) integrate (x^(1/2)*log(1/x), x, 0, 1);
                                4
(%o2)                           -
                                9
```

<!-- category: Calculus -->
<!-- keywords: quad_qagi -->
<!-- signatures: quad_qagi(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qagi(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qagi (f(x), x, a, b, [epsrel, epsabs, limit])

Integración de una función general en un intervalo infinito o semi-infinito.
El intervalo se proyecta sobre un intervalo finito y luego se aplica la
misma estrategia que en `quad_qags`.


La función `quad_qagi` calcula cualquiera las siguientes integrales:



$$
\int_a^\infty {f(x) dx}
$$



$$
\int_\infty^a {f(x) dx}
$$



$$
\int_{-\infty}^\infty {f(x) dx}
$$


utilizando la rutina QAGI de Quadpack QAGI. La función a integrar es *f(x)*, con variable independiente *x*, siendo el intervalo de integración de rango infinito.


El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima.


Uno de los límites de integración debe ser infinito. De no ser
así, `quad_qagi` devolverá una forma nominal.


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsrel** — Error relativo deseado de la aproximación. El valor por defecto es 1d-8.
**epsabs** — Error absoluto deseado de la aproximación. El valor por defecto es 0.
**limit** — Tamaño del array interno utilizado para realizar la cuadratura. 
*limit* es el número máximo de subintervalos
a utilizar. El valor por defecto es 200.


La función `quad_qagi` devuelve una lista de cuatro elementos:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**4** — fallo de convergencia;
**5** — la integral es probablemente divergente o de convergencia lenta;
**6** — si los argumentos de entrada no son válidos.




Ejemplos:



```maxima
(%i1) quad_qagi (x^2*exp(-4*x), x, 0, inf, 'epsrel=1d-8);
(%o1)        [0.03125, 2.95916102995002E-11, 105, 0]
(%i2) integrate (x^2*exp(-4*x), x, 0, inf);
                               1
(%o2)                          --
                               32
```

<!-- category: Calculus -->
<!-- keywords: quad_qagp -->
<!-- signatures: quad_qagp(f(x), x, a, b, points, [epsrel, epsabs, limit]), quad_qagp(f, x, a, b, points, [epsrel, epsabs, limit]) -->
### Function: quad_qagp (f(x), x, a, b, points, [epsrel, epsabs, limit])

Integra una función general sobre un intervalo acotado. La función
`quad_qagp` implementa un método adaptativo global de subdivisión
del intervalo con extrapolación (de Doncker, 1978) basado en el algoritmo
Epsilon (Wynn, 1956).


`quad_qagp` calcula la integral


$integrate (f(x), x, a, b)$

$$
\int_a^b {f(x) \, dx}
$$



La función a integrar es *f(x)*, con variable independiente
*x*, en el intervalo limitado por *a* y *b*.


El integrando puede especificarse mediante el nombre de una función de
Maxima o de Lisp o un operador, como una expresión lambda de Maxima, o
como una expresión general de Maxima.


Para ayudar al integrador, el usuario debe aportar una lista de puntos 
donde el integrando es singular o discontinuo.


Las opciones se suministran como argumentos y se pueden escribir en
cualquier orden. Deben tomar la forma `opción=valor`. Las 
opciones son:



**epsrel** — Error relativo de aproximación deseado. Valor por defecto es 1d-8.
**epsabs** — Error absoluto de aproximación deseado. Valor por defecto es 0.
**limit** — Tamaño del array interno de trabajo. *limit* es el máximo
número de subintervalos a utilizar. Valor por defecto es 200.


`quad_qagp` devuelve una lista con cuatro elementos:



- *
una aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (cuarto elemento de la lista devuelta) puede tener los
siguientes valores:



**0** — no se encontraron errores;
**1** — se han hecho demasiados subintervalos;
**2** — se detectó un error de redondeo muy grande;
**3** — se ha observado un comportamiento del integrando extremadamente malo;
**4** — fallo de convergencia;
**5** — la integral es probablemente divergengente o converge muy lentamente;
**6** — entrada inválida.


Ejemplos:



```maxima
(%i1) quad_qagp(x^3*log(abs((x^2-1)*(x^2-2))),x,0,3,[1,sqrt(2)]);
(%o1)   [52.74074838347143, 2.6247632689546663e-7, 1029, 0]


(%i2) quad_qags(x^3*log(abs((x^2-1)*(x^2-2))), x, 0, 3);
(%o2)   [52.74074847951494, 4.088443219529836e-7, 1869, 0]
```


El integrando tiene singularidades en `1` y `sqrt(2)`, de manera que
suministramos estos puntos a `quad_qagp`. También se observa que `quad_qagp`
es más exacto y eficiente que `quad_qags`.

<!-- category: Calculus -->
<!-- keywords: quad_qags -->
<!-- signatures: quad_qags(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qags(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qags (f(x), x, a, b, [epsrel, epsabs, limit])

Integración de una función general en un intervalo finito.
La función `quad_qags` implementa la subdivisión de intervalos 
global adaptativa con extrapolación (de Doncker, 1978) mediante
el algoritmo Epsilon  (Wynn, 1956).


La función `quad_qags` calcula la integral



$$
\int_a^b {f(x) dx}
$$


La función a integrar es *f(x)*, de variable independiente *x*, 
siendo el intervalo de integración el comprendido entre *a* y *b*.


El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima.


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsrel** — Error relativo deseado de la aproximación. El valor por defecto es 1d-8.
**epsabs** — Error absoluto deseado de la aproximación. El valor por defecto es 0.
**limit** — Tamaño del array interno utilizado para realizar la cuadratura. 
*limit* es el número máximo de subintervalos
a utilizar. El valor por defecto es 200.


La función `quad_qags` devuelve una lista de cuatro elementos:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**4** — fallo de convergencia;
**5** — la integral es probablemente divergente o de convergencia lenta;
**6** — si los argumentos de entrada no son válidos.




Ejemplos:



```maxima
(%i1) quad_qags (x^(1/2)*log(1/x), x, 0, 1, 'epsrel=1d-10);
(%o1)   [.4444444444444448, 1.11022302462516E-15, 315, 0]
```


Nótese que `quad_qags` es más precisa y eficiente que `quad_qag` para este integrando.

<!-- category: Calculus -->
<!-- keywords: quad_qawc -->
<!-- signatures: quad_qawc(f(x), x, c, a, b, [epsrel, epsabs, limit]), quad_qawc(f, x, c, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qawc (f(x), x, c, a, b, [epsrel, epsabs, limit])

Calcula el valor principal de Cauchy de $f(x)/(x - c)$ en un
intervalo finito $(a, b)$ para una $c$ dada.
La estrategia es global adaptativa, utilizando la integración de 
Clenshaw-Curtis modificada en los subintervalos que contienen a $x = c$.


La función `quad_qawc` calcula el valor principal de Cauchy de



$$
\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}
$$


utilizando la rutina QAWC de Quadpack.  La función a integrar es
`f(x)/(x - c)`, con variable independiente *x*, siendo el intervalo de integración el comprendido entre *a* y *b*.


El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima.


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsrel** — Error relativo deseado de la aproximación. El valor por defecto es 1d-8.
**epsabs** — Error absoluto deseado de la aproximación. El valor por defecto es 0.
**limit** — Tamaño del array interno utilizado para realizar la cuadratura. 
*limit* es el número máximo de subintervalos
a utilizar. El valor por defecto es 200.


`quad_qawc` returns a list of four elements:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**6** — si los argumentos de entrada no son válidos.


Ejemplos:



```maxima
(%i1) quad_qawc (2^(-5)*((x-1)^2+4^(-5))^(-1), x, 2, 0, 5,
                 'epsrel=1d-7);
(%o1)    [- 3.130120337415925, 1.306830140249558E-8, 495, 0]
(%i2) integrate (2^(-alpha)*(((x-1)^2 + 4^(-alpha))*(x-2))^(-1),
                 x, 0, 5);
Principal Value
        alpha        9 4                 9
       4      log(-------------- + --------------)
                   alpha + 3        alpha + 3
                  4          + 4   4          + 4
(%o2) (-------------------------------------------
                         alpha
                      2 4      + 2
    3 alpha                   3 alpha
    -------                   -------
       2          alpha/2        2              alpha/2
   4        atan(4       )   4        atan(- 4 4       )
 - ----------------------- + ---------------------------)
          alpha                       alpha
         4      + 1                  4      + 1
  alpha
/2
(%i3) ev (%, alpha=5, numer);
(%o3)                    - 3.130120337415917
```

<!-- category: Calculus -->
<!-- keywords: quad_qawf -->
<!-- signatures: quad_qawf(f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst]), quad_qawf(f, x, a, omega, trig, [epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawf (f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst])

Calcula la transformada seno o coseno de Fourier en un intervalo semi-infinito.
Se aplica el mismo método que en `quad_qawo` a sucesivos intervalos
finitos, acelerando la convergencia mediante el algoritmo Epsilon (Wynn, 1956).


La función `quad_qawf` calcula la integral



$$
\int_a^\infty f(x) w(x) dx
$$


La función peso $w$ se selecciona mediante *trig*:



**cos** — $w(x) = cos (omega x)$
**sin** — $w(x) = sin (omega x)$



El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsabs** — El error absoluto deseado para la aproximación. El valor por defecto es 1d-10.
**limit** — Tamaño del arreglo interno de trabajo.  (*limit* - *limlst*)/2 es el número máximo de subintervalos para la partición. El valor por defecto es 200.
**maxp1** — Número máximo de momentos de Chebyshev. Debe ser mayor que 0.  El valor por defecto es 100.
**limlst** — Cota superior del número de ciclos. Debe ser mayor o igual que 3.  El valor por defecto es 10.


`quad_qawf` returns a list of four elements:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**6** — si los argumentos de entrada no son válidos.


Ejemplos:



```maxima
(%i1) quad_qawf (exp(-x^2), x, 0, 1, 'cos, 'epsabs=1d-9);
(%o1)   [.6901942235215714, 2.84846300257552E-11, 215, 0]
(%i2) integrate (exp(-x^2)*cos(x), x, 0, inf);
                          - 1/4
                        %e      sqrt(%pi)
(%o2)                   -----------------
                                2
(%i3) ev (%, numer);
(%o3)                   .6901942235215714
```

<!-- category: Calculus -->
<!-- keywords: quad_qawo -->
<!-- signatures: quad_qawo(f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]), quad_qawo(f, x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawo (f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst])

Integración de $cos(omega x) f(x)$ o $sin(omega x) f(x)$ en un
intervalo finito, siendo $omega$ una constante. La regla de 
evaluación se basa en la técnica modificada de Clenshaw-Curtis.
La función `quad_qawo` aplica la subdivisión adaptativa con extrapolación, 
de forma similar a `quad_qags`.


La función `quad_qawo` realiza la integración utilizando la rutina QAWO de Quadpack:



$$
\int_a^b f(x) w(x) dx
$$


La función peso $w$ se selecciona mediante *trig*:



**cos** — $w(x) = cos (omega x)$
**sin** — $w(x) = sin (omega x)$


El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsrel** — El error absoluto deseado para la aproximación. El valor por defecto es 1d-8.
**epsabs** — Error absoluto deseado de la aproximación. El valor por defecto es 0.
**limit** — Tamaño del arreglo interno de trabajo. *limit*/2 es el número máximo de subintervalos para la partición. El valor por defecto es 200.
**maxp1** — Número máximo de momentos de Chebyshev. Debe ser mayor que 0.  El valor por defecto es 100.
**limlst** — Cota superior del número de ciclos. Debe ser mayor o igual que 3.  El valor por defecto es 10.


`quad_qawo` returns a list of four elements:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**6** — si los argumentos de entrada no son válidos.


Ejemplos:



```maxima
(%i1) quad_qawo (x^(-1/2)*exp(-2^(-2)*x), x, 1d-8, 20*2^2, 1, cos);
(%o1)     [1.376043389877692, 4.72710759424899E-11, 765, 0]
(%i2) rectform (integrate (x^(-1/2)*exp(-2^(-alpha)*x) * cos(x),
                           x, 0, inf));
                   alpha/2 - 1/2            2 alpha
        sqrt(%pi) 2              sqrt(sqrt(2        + 1) + 1)
(%o2)   -----------------------------------------------------
                               2 alpha
                         sqrt(2        + 1)
(%i3) ev (%, alpha=2, numer);
(%o3)                     1.376043390090716
```

<!-- category: Calculus -->
<!-- keywords: quad_qaws -->
<!-- signatures: quad_qaws(f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]), quad_qaws(f, x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]) -->
### Function: quad_qaws (f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit])

Integración de $w(x) f(x)$ en un intervalo finito $[a, b]$,
siendo $w$ una función de la forma $(x - a)^alpha (b - x)^beta v(x)$,
con  $v(x)$ igual a 1, a $log(x - a)$, a $log(b - x)$ o a
$log(x - a) log(b - x)$ y con $alpha > -1$, y $beta > -1$.
Se aplica una estrategia de subdivisión adaptativa global,
con integración de Clenshaw-Curtis modificada en los subintervalos que
contienen a $a$ y a $b$.


La función `quad_qaws` realiza la integración utizando la rutina QAWS de Quadpack:



$$
\int_a^b f(x) w(x) dx
$$


La función peso $w$ se selecciona mediante *wfun*:



**1** — $w(x) = (x - a)^alfa (b - x)^beta$
**2** — $w(x) = (x - a)^alfa (b - x)^beta log(x - a)$
**3** — $w(x) = (x - a)^alfa (b - x)^beta log(b - x)$
**4** — $w(x) = (x - a)^alfa (b - x)^beta log(x - a) log(b - x)$


El integrando se puede especificar con el nombre de una función u operador de Maxima 
o de Lisp, como una expresión lambda o como una expresión general de Maxima


Los argumentos opcionales pueden especificarse en cualquier orden. 
Todos ellos toman la forma `key=val`. Tales argumentos son:



**epsrel** — El error absoluto deseado para la aproximación. El valor por defecto es 1d-8.
**epsabs** — Error absoluto deseado de la aproximación. El valor por defecto es 0.
**limit** — Tamaño del array interno utilizado para realizar la cuadratura. 
(*limit* - *limlst*)/2 es el número máximo de subintervalos
a utilizar. El valor por defecto es 200.


`quad_qaws` returns a list of four elements:



- *
la aproximación a la integral,
- *
el error absoluto estimado de la aproximación,
- *
el número de evaluaciones del integrando,
- *
un código de error.


El código de error (el cuarto elemento del resultado) puede tener los siguientes valores:



**0** — si no ha habido problemas;
**1** — si se utilizaron demasiados intervalos;
**2** — si se encontró un número excesivo de errores de redondeo;
**3** — si el integrando ha tenido un comportamiento extraño frente a la integración;
**6** — si los argumentos de entrada no son válidos.


Ejemplos:



```maxima
(%i1) quad_qaws (1/(x+1+2^(-4)), x, -1, 1, -0.5, -0.5, 1,
                 'epsabs=1d-9);
(%o1)     [8.750097361672832, 1.24321522715422E-10, 170, 0]
(%i2) integrate ((1-x*x)^(-1/2)/(x+1+2^(-alpha)), x, -1, 1);
       alpha
Is  4 2      - 1  positive, negative, or zero?

pos;
                          alpha         alpha
                   2 %pi 2      sqrt(2 2      + 1)
(%o2)              -------------------------------
                               alpha
                            4 2      + 2
(%i3) ev (%, alpha=4, numer);
(%o3)                     8.750097361672829
```

<!-- category: Calculus -->
<!-- keywords: residue -->
<!-- signatures: residue(expr, z, z_0) -->
### Function: residue (expr, z, z_0)

Calcula el residuo en el plano complejo de la expresión  *expr* cuando la variable *z* toma el valor *z_0*.  El residuo es el coeficiente de `(z - z_0)^(-1)` en el desarrollo de Laurent de *expr*.



```maxima
(%i1) residue (s/(s**2+a**2), s, a*%i);
                                1
(%o1)                           -
                                2
(%i2) residue (sin(a*x)/x**4, x, 0);
                                 3
                                a
(%o2)                         - --
                                6
```

<!-- category: Calculus -->
<!-- keywords: risch -->
<!-- signatures: risch(expr, x) -->
### Function: risch (expr, x)

Integra *expr* respecto de *x* utilizando el caso trascendental del algoritmo de Risch. El caso algebraico del algoritmo de Risch no se ha implementado. Este método trata los casos de exponenciales y logaritmos anidados que no resuelve el procedimiento principal de `integrate`. La función `integrate` llamará automáticamente a `risch` si se presentan estos casos.


Si la variable `erfflag` vale `false`, evita que `risch` introduzca la función `erf`
en la respuesta si ésta no estaba presente previamente en el integrando.



```maxima
(%i1) risch (x^2*erf(x), x);
                                                        2
             3                      2                - x
        %pi x  erf(x) + (sqrt(%pi) x  + sqrt(%pi)) %e
(%o1)   -------------------------------------------------
                              3 %pi
(%i2) diff(%, x), ratsimp;
                             2
(%o2)                       x  erf(x)
```

<!-- category: Calculus -->
<!-- keywords: tldefint -->
<!-- signatures: tldefint(expr, x, a, b) -->
### Function: tldefint (expr, x, a, b)

Equivale a `ldefint` cuando `tlimswitch` vale `true`.

