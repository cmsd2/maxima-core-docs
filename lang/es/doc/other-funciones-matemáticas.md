## Funciones matemáticas

<!-- category: Other -->
<!-- keywords: %e_to_numlog -->
<!-- signatures: %e_to_numlog -->
### Variable: %e_to_numlog

Valor por defecto: `false`


Si `%e_to_numlog` vale `true`, `r` es un número racional y `x` una expresión, `%e^(r*log(x))` se reduce a `x^r` .  Téngase en cuenta que la instrucción `radcan` también hace este tipo de transformaciones, así como otras más complicadas. La instrucción `logcontract` "contrae" expresiones que contienen algún `log`.

<!-- category: Other -->
<!-- keywords: %emode -->
<!-- signatures: %emode -->
### Variable: %emode

Valor por defecto: `true`


Si `%emode` vale `true`,
`%e^(%pi %i x)` se simplifica como sigue.


`%e^(%pi %i x)` se simplifica a `cos (%pi x) + %i sin (%pi x)` si `x` es
un número decimal de coma flotante, un entero o un múltiplo de 1/2, 1/3, 1/4 o 1/6, y luego se sigue simplificando.


Para otros valores numéricos de `x`,
`%e^(%pi %i x)` se simplifica a `%e^(%pi %i y)` donde `y` es `x - 2 k`
para algún entero `k` tal que `abs(y) < 1`.  


Si `%emode` vale `false`, no se realizan simplificaciones especiales a `%e^(%pi %i x)`.

<!-- category: Other -->
<!-- keywords: %enumer -->
<!-- signatures: %enumer -->
### Variable: %enumer

Valor por defecto: `false`


Si la variable `%enumer` vale `true` hace que `%e` se reemplace por
2.718...  siempre que `numer` valga `true`. 


Si `%enumer` vale `false`, esta sustitución se realiza sólo si el exponente en `%e^x` tiene un valor numérico.


Véanse también `ev` y `numer`.

<!-- category: Other -->
<!-- keywords: %iargs -->
<!-- signatures: %iargs -->
### Variable: %iargs

Valor por defecto: `true`


Cuando `%iargs` vale `true`, las funciones trigonométricas
se simplifican a funciones hiperbólicas
si el argumento es aparentemente un múltiplo de la unidad imaginaria $%i$.


La simplificación se lleva a cabo incluso cuando el argumento es manifiestamente real;
Maxima sólo se fija en si el argumento es un múltiplo literal de $%i$.


Ejemplos:









```maxima
(%i1) %iargs : false$

(%i2) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o2)           [sin(%i x), cos(%i x), tan(%i x)]

(%i3) %iargs : true$

(%i4) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o4)           [%i sinh(x), cosh(x), %i tanh(x)]
```


La simplificación se aplica incluso en el caso de que
el argumento se reduzca a un número real.








```maxima
(%i1) declare (x, imaginary)$

(%i2) [featurep (x, imaginary), featurep (x, real)];
(%o2)                     [true, false]


(%i3) sin (%i * x);
(%o3)                      %i sinh(x)
```

<!-- category: Other -->
<!-- keywords: %piargs -->
<!-- signatures: %piargs -->
### Variable: %piargs

Valor por defecto: `true`


Cuando `%piargs` vale `true`, las funciones trigonométricas
se simplifican a constantes algebraicas cuando el argumento es múltiplo
entero de 
$%pi$, $%pi/2$, $%pi/3$, $%pi/4$ o $%pi/6$.


Maxima conoce algunas identidades aplicables cuando $%pi$, etc.,
se multiplican por una variable entera (esto es, un símbolo
declarado como entero).


Ejemplo:













```maxima
(%i1) %piargs : false$

(%i2) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                %pi       %pi
(%o2)            [sin(%pi), sin(---), sin(---)]
                                 2         3


(%i3) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                      %pi       %pi       %pi
(%o3)            [sin(---), sin(---), sin(---)]
                       4         5         6

(%i4) %piargs : true$

(%i5) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                sqrt(3)
(%o5)                    [0, 1, -------]
                                   2


(%i6) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                         1         %pi   1
(%o6)                [-------, sin(---), -]
                      sqrt(2)       5    2


(%i7) [cos (%pi/3), cos (10*%pi/3), tan (10*%pi/3),
       cos (sqrt(2)*%pi/3)];
                1    1               sqrt(2) %pi
(%o7)          [-, - -, sqrt(3), cos(-----------)]
                2    2                    3
```



Se aplican ciertas identidades cuando $%pi$ o $%pi/2$ se multiplican por una variable entera.








```maxima
(%i1) declare (n, integer, m, even)$

(%i2) [sin (%pi * n), cos (%pi * m), sin (%pi/2 * m),
       cos (%pi/2 * m)];
                                      m/2
(%o2)                  [0, 1, 0, (- 1)   ]
```

<!-- category: Other -->
<!-- keywords: abs -->
<!-- signatures: abs(z) -->
### Function: abs (z)

La función `abs` representa el valor absoluto y se puede aplicar tanto 
a argumentos numéricos como simbólicos. Si el argumento *z* es un
número real o complejo, `abs` devuelve el valor absoluto de *z*.
Si es posible, las expresiones simbólicas que utilizan la función del
valor absoluto también se simplifican.


Maxima puede derivar, integrar y calcular límites de expresiones
que contengan a `abs`. El paquete `abs_integrate` extiende las
capacidades de Maxima para calcular integrales que contengan llamadas a
`abs`. Véase `(%i12)` en el ejemplo de más abajo.


Cuando se aplica a una lista o matriz, `abs` se distribuye automáticamente
sobre sus elementos. De forma similar, también se distribuye sobre los dos
miembros de una igualdad. Para cambiar este comportamiento por defecto, 
véase la variable `distribute_over`.


Ejemplos:


Cálculo del valor absoluto de números reales y complejos, incluyendo
constantes numéricas e infinitos. El primer ejemplo muestra cómo 
`abs` se distribuye sobre los elementos de una lista.



```maxima
(%i1) abs([-4, 0, 1, 1+%i]);
(%o1)                  [4, 0, 1, sqrt(2)]

(%i2) abs((1+%i)*(1-%i));
(%o2)                           2
(%i3) abs(%e+%i);
                                2
(%o3)                    sqrt(%e  + 1)
(%i4) abs([inf, infinity, minf]);
(%o4)                   [inf, inf, inf]
```


Simplificación de expresiones que contienen `abs`:



```maxima
(%i5) abs(x^2);
                                2
(%o5)                          x
(%i6) abs(x^3);
                             2
(%o6)                       x  abs(x)

(%i7) abs(abs(x));
(%o7)                       abs(x)
(%i8) abs(conjugate(x));
(%o8)                       abs(x)
```


Integrando y derivando con la función `abs`. Nótese que se pueden
calcular más integrales que involucren la función `abs` si se
carga el paquete `abs_integrate`. El último ejemplo muestra la
transformada de Laplace de `abs`. Véase `laplace`.



```maxima
(%i9) diff(x*abs(x),x),expand;
(%o9)                       2 abs(x)

(%i10) integrate(abs(x),x);
                             x abs(x)
(%o10)                       --------
                                2

(%i11) integrate(x*abs(x),x);
                           /
                           [
(%o11)                     I x abs(x) dx
                           ]
                           /

(%i12) load("abs_integrate")$
(%i13) integrate(x*abs(x),x);
                      2           3
                     x  abs(x)   x  signum(x)
(%o13)               --------- - ------------
                         2            6

(%i14) integrate(abs(x),x,-2,%pi);
                               2
                            %pi
(%o14)                      ---- + 2
                             2

(%i15) laplace(abs(x),x,s);
                               1
(%o15)                         --
                                2
                               s
```

<!-- category: Other -->
<!-- keywords: acos -->
<!-- signatures: acos(x) -->
### Function: acos (x)

Arco coseno.

<!-- category: Other -->
<!-- keywords: acosh -->
<!-- signatures: acosh(x) -->
### Function: acosh (x)

Arco coseno hiperbólico.

<!-- category: Other -->
<!-- keywords: acot -->
<!-- signatures: acot(x) -->
### Function: acot (x)

Arco cotangente.

<!-- category: Other -->
<!-- keywords: acoth -->
<!-- signatures: acoth(x) -->
### Function: acoth (x)

Arco cotangente hiperbólica.

<!-- category: Other -->
<!-- keywords: acsc -->
<!-- signatures: acsc(x) -->
### Function: acsc (x)

Arco cosecante.

<!-- category: Other -->
<!-- keywords: acsch -->
<!-- signatures: acsch(x) -->
### Function: acsch (x)

Arco cosecante hiperbólica.

<!-- category: Other -->
<!-- keywords: asec -->
<!-- signatures: asec(x) -->
### Function: asec (x)

Arco secante.

<!-- category: Other -->
<!-- keywords: asech -->
<!-- signatures: asech(x) -->
### Function: asech (x)

Arco secante hiperbólica.

<!-- category: Other -->
<!-- keywords: asin -->
<!-- signatures: asin(x) -->
### Function: asin (x)

Arco seno.

<!-- category: Other -->
<!-- keywords: asinh -->
<!-- signatures: asinh(x) -->
### Function: asinh (x)

Arco seno hiperbólico.

<!-- category: Other -->
<!-- keywords: atan -->
<!-- signatures: atan(x) -->
### Function: atan (x)

Arco tangente.

<!-- category: Other -->
<!-- keywords: atan2 -->
<!-- signatures: atan2(y, x) -->
### Function: atan2 (y, x)

Calcula el valor de `atan(y/x)` en el intervalo de `-%pi` a `%pi`.

<!-- category: Other -->
<!-- keywords: atanh -->
<!-- signatures: atanh(x) -->
### Function: atanh (x)

Arco tangente hiperbólica.

<!-- category: Other -->
<!-- keywords: atrig1 -->
<!-- signatures: atrig1 -->
### Variable: atrig1

El paquete `atrig1` contiene ciertas reglas de simplificación adicionales para las funciones trigonométricas inversas. Junto con las reglas que ya conoce Maxima, los siguientes ángulos están completamente implementados:
`0`, `%pi/6`, `%pi/4`, `%pi/3` y `%pi/2`.  
Los ángulos correspondientes en los otros tres cuadrantes también están disponibles.  
Para hacer uso de estas reglas, ejecútese `load("atrig1");`.

<!-- category: Other -->
<!-- keywords: cabs -->
<!-- signatures: cabs(expr) -->
### Function: cabs (expr)

Calcula el valor absoluto de una expresión que representa a un número
complejo. Al contrario que `abs`, la función `cabs` siempre
descompone su argumento en sus partes real e imaginaria. Si `x` e
`y` representan variables o expresiones reales, la función `cabs`
calcula el valor absoluto de `x + %i*y` como


```maxima
2    2
                     sqrt(y  + x )
```


La función `cabs` puede utilizar propiedades como la simetría
de funciones complejas para calcular el valor absoluto de una expresión.


`cabs` no es una función apropiada para cálculos simbólicos; en tales
casos, que incluyen la integración, diferenciación y límites que
contienen valores absolutos, es mejor utilizar `abs`.


El resultado devuelto por `cabs` puede incluir la función de valor absoluto,
`abs`, y el arco tangente, `atan2`.


Cuando se aplica a una lista o matriz, `cabs` automáticamente se distribuye
sobre sus elementos. También se distribuye sobre los dos miembros de una 
igualdad.


Para otras formas de operar con números complejos, véanse las funciones
`rectform`, `realpart`, `imagpart`, `carg`, `conjugate`
y `polarform`.


Ejemplos:


Ejemplos con `sqrt` and `sin`:



```maxima
(%i1) cabs(sqrt(1+%i*x));
                             2     1/4
(%o1)                      (x  + 1)
(%i2) cabs(sin(x+%i*y));
                    2        2         2        2
(%o2)       sqrt(cos (x) sinh (y) + sin (x) cosh (y))
```


La simetría especular de la función de error `erf` se utiliza
para calcular el valor absoluto del argumento complejo:



```maxima
(%i3) cabs(erf(x+%i*y));
                                          2
           (erf(%i y + x) - erf(%i y - x))
(%o3) sqrt(--------------------------------
                          4
                                                               2
                                (erf(%i y + x) + erf(%i y - x))
                              - --------------------------------)
                                               4
```


Dado que Maxima reconoce algunas identidades complejas de las funciones de
Bessel, le permite calcular su valor absoluto cuando tiene argumentos 
complejos. Un ejemplo para `bessel_j`:



```maxima
(%i4) cabs(bessel_j(1,%i));
(%o4)                 abs(bessel_j(1, %i))
```

<!-- category: Other -->
<!-- keywords: carg -->
<!-- signatures: carg(z) -->
### Function: carg (z)

Devuelve el argumento complejo de *z*.
El argumento complejo es un ángulo `theta` en `(-%pi, %pi]`
tal que `r exp (theta %i) = z` donde `r` es la magnitud de *z*.


La función `carg` es computacional, no simplificativa.



Véanse también `abs` (módulo complejo), `polarform`, `rectform`,
`realpart` y `imagpart`.


Ejemplos:












```maxima
(%i1) carg (1);
(%o1)                           0
(%i2) carg (1 + %i);
                               %pi
(%o2)                          ---
                                4
(%i3) carg (exp (%i));
(%o3)                           1
(%i4) carg (exp (%pi * %i));
(%o4)                          %pi
(%i5) carg (exp (3/2 * %pi * %i));
                                %pi
(%o5)                         - ---
                                 2
(%i6) carg (17 * exp (2 * %i));
(%o6)                           2
```

<!-- category: Other -->
<!-- keywords: ceiling -->
<!-- signatures: ceiling(x) -->
### Function: ceiling (x)

Si *x* es un número real, devuelve el menor entero mayor o igual que *x*.  


Si *x* es una expresión constante (por ejemplo, `10 * %pi`), 
`ceiling` evalúa *x* haciendo uso de números grandes en coma flotante (big floats), aplicando a continuación
 `ceiling` al número decimal obtenido. Puesto que `ceiling` hace evaluaciones en coma flotante, es posible, pero improbable, que esta función devuelva un valor erróneo para entradas constantes. Para evitar estos errores, la evaluación en punto flotante se lleva a cabo utilizando tres valores para `fpprec`.


Para argumentos no constantes, `ceiling` intenta devolver un valor simplificado. Aquí se presentan algunos ejemplos sobre las simplificaciones que `ceiling` es capaz de hacer:












```maxima
(%i1) ceiling (ceiling (x));
(%o1)                      ceiling(x)
(%i2) ceiling (floor (x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) [ceiling (n), ceiling (abs (n)), ceiling (max (n, 6))];
(%o4)                [n, abs(n), max(n, 6)]
(%i5) assume (x > 0, x < 1)$
(%i6) ceiling (x);
(%o6)                           1
(%i7) tex (ceiling (a));
$$\left \lceil a \right \rceil$$
(%o7)                                false
```


La función `ceiling` no se extiende automáticamente a los elementos de listas y matrices.
Por último, para todos los argumentos que tengan una forma compleja, `ceiling` devuelve una forma nominal.


Si el rango de una función es subconjunto de los números enteros, entonces puede ser declarada como `integervalued`. Tanto `ceiling` como `floor` son funciones que hacen uso de esta información; por ejemplo:








```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```


Ejemplo de uso:


















```maxima
(%i1) unitfrac(r) := block([uf : [], q],
    if not(ratnump(r)) then
       error("unitfrac: argument must be a rational number"),
    while r # 0 do (
        uf : cons(q : 1/ceiling(1/r), uf),
        r : r - q),
    reverse(uf))$

(%i2) unitfrac (9/10);
                            1  1  1
(%o2)                      [-, -, --]
                            2  3  15
(%i3) apply ("+", %);
                               9
(%o3)                          --
                               10
(%i4) unitfrac (-9/10);
                                  1
(%o4)                       [- 1, --]
                                  10
(%i5) apply ("+", %);
                                9
(%o5)                         - --
                                10
(%i6) unitfrac (36/37);
                        1  1  1  1    1
(%o6)                  [-, -, -, --, ----]
                        2  3  8  69  6808
(%i7) apply ("+", %);
                               36
(%o7)                          --
                               37
```

<!-- category: Other -->
<!-- keywords: conjugate -->
<!-- signatures: conjugate(x) -->
### Function: conjugate (x)

Devuelve el conjugado complejo de *x*.










```maxima
(%i1) declare ([aa, bb], real, cc, complex, ii, imaginary);

(%o1)                         done
(%i2) conjugate (aa + bb*%i);

(%o2)                      aa - %i bb
(%i3) conjugate (cc);

(%o3)                     conjugate(cc)
(%i4) conjugate (ii);

(%o4)                         - ii
(%i5) conjugate (xx + yy);

(%o5)             conjugate(yy) + conjugate(xx)
```

<!-- category: Other -->
<!-- keywords: cos -->
<!-- signatures: cos(x) -->
### Function: cos (x)

Coseno.

<!-- category: Other -->
<!-- keywords: cosh -->
<!-- signatures: cosh(x) -->
### Function: cosh (x)

Coseno hiperbólico.

<!-- category: Other -->
<!-- keywords: cot -->
<!-- signatures: cot(x) -->
### Function: cot (x)

Cotangente.

<!-- category: Other -->
<!-- keywords: coth -->
<!-- signatures: coth(x) -->
### Function: coth (x)

Cotangente hiperbólica.

<!-- category: Other -->
<!-- keywords: csc -->
<!-- signatures: csc(x) -->
### Function: csc (x)

Cosecante.

<!-- category: Other -->
<!-- keywords: csch -->
<!-- signatures: csch(x) -->
### Function: csch (x)

Cosecante hiperbólica.

<!-- category: Other -->
<!-- keywords: entier -->
<!-- signatures: entier(x) -->
### Function: entier (x)

Devuelve el mayor entero menor o igual a *x*, siendo *x* numérico. La función  `fix` (como en
`fixnum`) es un sinónimo, de modo que `fix(x)` hace justamente lo mismo.

<!-- category: Other -->
<!-- keywords: exp -->
<!-- signatures: exp(x) -->
### Function: exp (x)

Representa la función exponencial.  
La expresión  `exp (x)` en la entrada se simplifica en `%e^x`;
`exp` no aparece en expresiones simplificadas.


Si la variable `demoivre` vale `true` hace que `%e^(a + b %i)` se simplifique a
`%e^(a (cos(b) + %i sin(b)))` si `b` no contiene a `%i`. Véase `demoivre`.


Si la variable `%emode` vale `true`, 
hace que  `%e^(%pi %i x)` se simplifique. Véase `%emode`.


Si la variable `%enumer` vale `true` hace que `%e` se reemplace por
2.718...  siempre que `numer` valga `true`. Véase `%enumer`.

<!-- category: Other -->
<!-- keywords: fix -->
<!-- signatures: fix(x) -->
### Function: fix (x)

Es un sinónimo de  `entier (x)`.

<!-- category: Other -->
<!-- keywords: floor -->
<!-- signatures: floor(x) -->
### Function: floor (x)

Si *x* es un número real, devuelve el mayor entero menor o igual que *x*.


Si *x* es una expresión constante (por ejemplo, `10 * %pi`), 
`floor` evalúa *x* haciendo uso de números grandes en coma flotante (big floats), aplicando a continuación
 `floor` al número decimal obtenido. Puesto que `floor` hace evaluaciones en coma flotante, es posible, pero improbable, que esta función devuelva un valor erróneo para entradas constantes. Para evitar estos errores, la evaluación en punto flotante se lleva a cabo utilizando tres valores para `fpprec`.


Para argumentos no constantes, `floor` intenta devolver un valor simplificado. Aquí se presentan algunos ejemplos sobre las simplificaciones que `floor` es capaz de hacer:












```maxima
(%i1) floor (ceiling (x));
(%o1)                      ceiling(x)
(%i2) floor (floor (x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) [floor (n), floor (abs (n)), floor (min (n, 6))];
(%o4)                [n, abs(n), min(n, 6)]
(%i5) assume (x > 0, x < 1)$
(%i6) floor (x);
(%o6)                           0
(%i7) tex (floor (a));
$$\left \lfloor a \right \rfloor$$
(%o7)                         false
```


La función `floor` no se extiende automáticamente a los elementos de listas y matrices.
Por último, para todos los argumentos que tengan una forma compleja, `floor` devuelve una forma nominal.


Si el rango de una función es subconjunto de los números enteros, entonces puede ser declarada como `integervalued`. Tanto `ceiling` como `floor` son funciones que hacen uso de esta información; por ejemplo:








```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

<!-- category: Other -->
<!-- keywords: halfangles -->
<!-- signatures: halfangles -->
### Variable: halfangles

Valor por defecto: `false`


Si `halfangles` vale `true`, las funciones
trigonométricas con argumentos del tipo `expr/2`
se simplifican a funciones con argumentos *expr*.


Para un argumento real *x* en el intervalo `0 < x < 2*%pi`
el seno del semiángulo se simplifica como



```maxima
sqrt(1 - cos(x))
                    ----------------
                        sqrt(2)
```


Se necesita un factor relativamente complicado para que esta fórmula
sea también válida para cualquier argumento complejo *z*:



```maxima
realpart(z)
     floor(-----------)
              2 %pi
(- 1)                   (1 - unit_step(- imagpart(z))

                      realpart(z)            realpart(z)
                floor(-----------) - ceiling(-----------)
                         2 %pi                  2 %pi
          ((- 1)                                          + 1))
```


Maxima reconoce este factor y otros similares para las funciones `sin`, 
`cos`, `sinh` y `cosh`. Para valores especiales del argumento
$z$, estos factores se simplifican de forma apropiada.


Ejemplos:











```maxima
(%i1) halfangles:false;
(%o1)                                false
(%i2) sin(x/2);
                                        x
(%o2)                               sin(-)
                                        2
(%i3) halfangles:true;
(%o3)                                true
(%i4) sin(x/2);
                                                    x
                                            floor(-----)
                                                  2 %pi
                      sqrt(1 - cos(x)) (- 1)
(%o4)                 ----------------------------------
                                   sqrt(2)
(%i5) assume(x>0, x<2*%pi)$
(%i6) sin(x/2);
                               sqrt(1 - cos(x))
(%o6)                          ----------------
                                   sqrt(2)
```

<!-- category: Other -->
<!-- keywords: imagpart -->
<!-- signatures: imagpart(expr) -->
### Function: imagpart (expr)

Devuelve la parte imaginaria de la expresión *expr*.


La función `imagpart` es computacional,
no simplificativa.




Véanse también `abs`, `carg`, `polarform`, `rectform` y `realpart`.

<!-- category: Other -->
<!-- keywords: li -->
<!-- signatures: li[s](z) -->
### Function: li ([s](z))

Representa la función polilogarítmica de orden *s* y argumento *z*,
definida por la serie infinita



$$
{\rm Li}_s \left(z\right) = \sum_{k=1}^\infty {z^k \over k^s}
$$


```maxima
inf
                                 ====   k
                                 \     z
                        Li (z) =  >    --
                          s      /      s
                                 ====  k
                                 k = 1
```


`li [1]` es `- log (1 - z)`.
`li [2]` y `li [3]` son las funciones di- y trilogaritmo, respectivamente.


Cuando el orden es 1, el polilogaritmo se simplifica a `- log (1 - z)`,
el cual a su vez se reduce a un valor numérico si *z* es un número
real o complejo en coma flotante o si está presente el término `numer`.


Cuando el orden es 2 ó 3,
el polilogaritmo se reduce a un valor numérico si *z* es
un número real en coma flotante o si está presente el término `numer`.


Ejemplos:














```maxima
(%i1) assume (x > 0);
(%o1)                        [x > 0]
(%i2) integrate ((log (1 - t)) / t, t, 0, x);
(%o2)                       - li (x)
                                2
(%i3) li [2] (7);
(%o3)                        li (7)
                               2
(%i4) li [2] (7), numer;
(%o4)        1.24827317833392 - 6.113257021832577 %i
(%i5) li [3] (7);
(%o5)                        li (7)
                               3
(%i6) li [2] (7), numer;
(%o6)        1.24827317833392 - 6.113257021832577 %i
(%i7) L : makelist (i / 4.0, i, 0, 8);
(%o7)   [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
(%i8) map (lambda ([x], li [2] (x)), L);
(%o8) [0, .2676526384986274, .5822405249432515, 
.9784693966661848, 1.64493407, 2.190177004178597
 - .7010261407036192 %i, 2.374395264042415
 - 1.273806203464065 %i, 2.448686757245154
 - 1.758084846201883 %i, 2.467401098097648
 - 2.177586087815347 %i]
(%i9) map (lambda ([x], li [3] (x)), L);
(%o9) [0, .2584613953442624, 0.537213192678042, 
.8444258046482203, 1.2020569, 1.642866878950322
 - .07821473130035025 %i, 2.060877505514697
 - .2582419849982037 %i, 2.433418896388322
 - .4919260182322965 %i, 2.762071904015935
 - .7546938285978846 %i]
```

<!-- category: Other -->
<!-- keywords: lmax -->
<!-- signatures: lmax(L) -->
### Function: lmax (L)

Si *L* es una lista o conjunto, devuelve `apply ('max, args (L))`.  Si *L* no es una lista o conjunto, envía un mensaje de error.

<!-- category: Other -->
<!-- keywords: lmin -->
<!-- signatures: lmin(L) -->
### Function: lmin (L)

Si *L* es una lista o conjunto, devuelve `apply ('min, args (L))`.  Si *L* no es una lista o conjunto, envía un mensaje de error.

<!-- category: Other -->
<!-- keywords: log -->
<!-- signatures: log(x) -->
### Function: log (x)

Representa el logaritmo natural (en base $e$) de *x*.


Maxima no tiene definida una función para el logaritmo de base 10 u
otras bases. El usuario puede hacer uso de la definición 
`log10(x) := log(x) / log(10)`.


La simplificación y evaluación de logaritmos se controla con
ciertas variables globales:



**`logexpand`** — hace que `log(a^b)` se convierta en `b*log(a)`.
Si toma el valor `all`, `log(a*b)` también se reducirá a  `log(a)+log(b)`.
Si toma el valor `super`, entonces `log(a/b)` también se reducirá a
`log(a)-log(b)`, siendo `a/b` racional con `a#1`, 
(la expresión `log(1/b)`, para `b` entero, se simplifica siempre). 
Si toma el valor  `false`, se desactivarán todas estas simplificaciones.
**`logsimp`** — si vale `false`, entonces no se transforma `%e` a potencias que contengan logaritmos.
**`lognegint`** — si vale `true` se aplica la regla `log(-n)` -> `log(n)+%i*%pi`,
siendo `n` un entero positivo.
**`%e_to_numlog`** — si vale `true`, `r` es un número racional y `x` una expresión,
`%e^(r*log(x))` se reduce a `x^r`. Téngase en cuenta que la 
instrucción `radcan` también hace este tipo de transformaciones, 
así como otras más complicadas. La instrucción `logcontract`
"contrae" expresiones que contengan algún `log`.

<!-- category: Other -->
<!-- keywords: logabs -->
<!-- signatures: logabs -->
### Variable: logabs

Valor por defecto: `false`


Cuando se calculan integrales indefinidas en las que se generan logaritmos, como en `integrate(1/x,x)`, el resultado se devuelve de la forma  `log(abs(...))` si `logabs` vale `true`, o de la forma `log(...)` si
`logabs` vale `false`. En la integración definida se hace la asignación `logabs:true`, ya que aquí es normalmente necesario evaluar la integral indefinida en los extremos del intervalo de integración.

<!-- category: Other -->
<!-- keywords: logarc -->
<!-- signatures: logarc(expr) -->
### Variable: logarc

Si la variable global `logarc` toma el valor `true`,
las funciones circulares e hiperbólicas inversas se 
reemplazan por funciones logarítmicas equivalentes.
El valor por defecto de `logarc` es `false`.


La función `logarc(expr)` realiza la anterior transformación
en la expresión *expr* sin necesidad de alterar el valor de la
variable global `logarc`.

<!-- category: Other -->
<!-- keywords: logconcoeffp -->
<!-- signatures: logconcoeffp -->
### Variable: logconcoeffp

Valor por defecto: `false`


Controla qué coeficientes se contraen cuando se utiliza `logcontract`. Se le puede asignar el nombre de una función de predicado de un argumento; por ejemplo, si se quiere introducir raíces cuadradas, se puede hacer `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$` .  Entonces 
`logcontract(1/2*log(x));` devolverá `log(sqrt(x))`.

<!-- category: Other -->
<!-- keywords: logcontract -->
<!-- signatures: logcontract(expr) -->
### Function: logcontract (expr)

Analiza la expresión *expr* recursivamente, transformando subexpresiones de la forma `a1*log(b1) + a2*log(b2) + c` en `log(ratsimp(b1^a1 * b2^a2)) + c`







```maxima
(%i1) 2*(a*log(x) + 2*a*log(y))$
(%i2) logcontract(%);
                                 2  4
(%o2)                     a log(x  y )
```


Si se hace `declare(n,integer);` entonces `logcontract(2*a*n*log(x));` da
`a*log(x^(2*n))`.  Los coeficientes que se contraen de esta manera son aquellos que como el 2 y el `n` satisfacen 
`featurep(coeff,integer)`. El usuario puede controlar qué coeficientes se contraen asignándole a la variable global `logconcoeffp` el nombre de una función de predicado de un argumento; por ejemplo, si se quiere introducir raíces cuadradas, se puede hacer `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$` .  Entonces `logcontract(1/2*log(x));` devolverá `log(sqrt(x))`.

<!-- category: Other -->
<!-- keywords: logexpand -->
<!-- signatures: logexpand -->
### Variable: logexpand

Valor por defecto: `true`


Si `logexpand` vale `true` hace que `log(a^b)` se convierta
en `b*log(a)`. Si toma el valor `all`, `log(a*b)` también se
reducirá a  `log(a)+log(b)`. Si toma el valor `super`, entonces 
`log(a/b)` también se reducirá a `log(a)-log(b)`, siendo 
`a/b` racional con `a#1`,  (la expresión `log(1/b)`, para
`b` entero, se simplifica siempre). Si toma el valor  `false`,
se desactivarán todas estas simplificaciones.

<!-- category: Other -->
<!-- keywords: lognegint -->
<!-- signatures: lognegint -->
### Variable: lognegint

Valor por defecto: `false`


Si `lognegint` vale `true` se aplica la regla `log(-n)` -> `log(n)+%i*%pi` siendo `n` un entero positivo.

<!-- category: Other -->
<!-- keywords: logsimp -->
<!-- signatures: logsimp -->
### Variable: logsimp

Valor por defecto: `true`


Si `logsimp` vale `false`, entonces no se transforma `%e` a potencias que contengan logaritmos.

<!-- category: Other -->
<!-- keywords: make_random_state -->
<!-- signatures: make_random_state(n), make_random_state(s), make_random_state(true), make_random_state(false) -->
### Function: make_random_state (n)

Un objeto de estado aleatorio representa el estado del generador de números aleatorios. El estado consiste en 627 cadenas binarias de 32 bits.


La llamada `make_random_state (n)` devuelve un nuevo objeto de estado aleatorio creado a partir de una semilla entera igual a *n* módulo 2^32. El argumento *n* puede ser negativo.


La llamada `make_random_state (s)` devuelve una copia del estado aleatorio *s*.


La llamada `make_random_state (true)` devuelve un nuevo objeto de estado aleatorio, cuya semilla se genera a partir de la hora actual del reloj del sistema como semilla.


La llamada `make_random_state (false)` devuelve una copia del estado actual del generador de números aleatorios.

<!-- category: Other -->
<!-- keywords: max -->
<!-- signatures: max(x_1, ..., x_n) -->
### Function: max (x_1, ..., x_n)

Devuelve un valor simplificado de la mayor de las expresiones desde *x_1* hasta *x_n*.
Si `get (trylevel, maxmin)` es 2 o más, `max` aplica la simplificación 
`max (e, -e) --> |e|`.  Si `get (trylevel, maxmin)` es 3 o más, *max* intenta
eliminar las expresiones que estén entre otros dos de los argumentos dados; por ejemplo,
`max (x, 2*x, 3*x) --> max (x, 3*x)`. Para asignar el valor 2 a `trylevel` se puede hacer
`put (trylevel, 2, maxmin)`.

<!-- category: Other -->
<!-- keywords: min -->
<!-- signatures: min(x_1, ..., x_n) -->
### Function: min (x_1, ..., x_n)

Devuelve un valor simplificado de la menor de las expresiones desde *x_1* hasta *x_n*.
Si `get (trylevel, maxmin)` es 2 o más, `min` aplica la simplificación 
`min (e, -e) --> |e|`.  Si `get (trylevel, maxmin)` es 3 o más, *min* intenta
eliminar las expresiones que estén entre otros dos de los argumentos dados; por ejemplo,
`min (x, 2*x, 3*x) --> min (x, 3*x)`. Para asignar el valor 2 a `trylevel` se puede hacer
`put (trylevel, 2, maxmin)`.

<!-- category: Other -->
<!-- keywords: ntrig -->
<!-- signatures: ntrig -->
### Variable: ntrig

El paquete `ntrig` contiene un conjunto de reglas de simplificación que se pueden usar para simplificar funciones trigonométricas cuyos argumentos son de la forma
`f(n %pi/10)` donde *f* es cualquiera de las funciones 
`sin`, `cos`, `tan`, `csc`, `sec` o `cot`.

<!-- category: Other -->
<!-- keywords: plog -->
<!-- signatures: plog(x) -->
### Function: plog (x)

Representa la rama principal del logaritmo natural complejo con `-%pi` < `carg(x)` <= `+%pi` .

<!-- category: Other -->
<!-- keywords: polarform -->
<!-- signatures: polarform(expr) -->
### Function: polarform (expr)

Devuelve una expresión de la forma `r %e^(%i theta)` equivalente a *expr*,
con `r` y `theta` son reales.

<!-- category: Other -->
<!-- keywords: random -->
<!-- signatures: random(x) -->
### Function: random (x)

Devuelve un número seudoaleatorio. Si *x* es un entero, `random (x)` devuelve un
entero entre 0 y `x - 1`, ambos inclusive. Si *x* es un decimal en punto flotante,
`random (x)` devuelve un decimal no negativo en punto flotante menor que *x*.
La función `random` emite un mensaje de error si *x* no es ni entero ni de punto flotante,
o si *x* no es positivo.


Las funciones `make_random_state` y `set_random_state`
permiten controlar el estado del generador de números aleatorios.


El generador de números aleatorios de Maxima implementa el algoritmo de Mersenne twister MT 19937.


Ejemplos:


















```maxima
(%i1) s1: make_random_state (654321)$
(%i2) set_random_state (s1);
(%o2)                         done
(%i3) random (1000);
(%o3)                          768
(%i4) random (9573684);
(%o4)                        7657880
(%i5) random (2^75);
(%o5)                11804491615036831636390
(%i6) s2: make_random_state (false)$
(%i7) random (1.0);
(%o7)                   .2310127244107132
(%i8) random (10.0);
(%o8)                   4.394553645870825
(%i9) random (100.0);
(%o9)                   32.28666704056853
(%i10) set_random_state (s2);
(%o10)                        done
(%i11) random (1.0);
(%o11)                  .2310127244107132
(%i12) random (10.0);
(%o12)                  4.394553645870825
(%i13) random (100.0);
(%o13)                  32.28666704056853
```

<!-- category: Other -->
<!-- keywords: realpart -->
<!-- signatures: realpart(expr) -->
### Function: realpart (expr)

Devuelve la parte real de *expr*. La funciones `realpart` y `imagpart` operan también con expresiones que contengan funciones trigonométricas e hiperbólicas, raíces cuadradas, logaritmos y exponentes.

<!-- category: Other -->
<!-- keywords: rectform -->
<!-- signatures: rectform(expr) -->
### Function: rectform (expr)

Devuelve una expresión de la forma `a + b %i` equivalente a *expr*, con *a* y *b* reales.

<!-- category: Other -->
<!-- keywords: round -->
<!-- signatures: round(x) -->
### Function: round (x)

Si *x* es un número real, la función devuelve el entero más 
próximo a *x*. Los múltiplos de 1/2 se redondean al entero par más próximo.
La evaluación de *x* es similar a `floor` y `ceiling`.

<!-- category: Other -->
<!-- keywords: sec -->
<!-- signatures: sec(x) -->
### Function: sec (x)

Secante.

<!-- category: Other -->
<!-- keywords: sech -->
<!-- signatures: sech(x) -->
### Function: sech (x)

Secante hiperbólica.

<!-- category: Other -->
<!-- keywords: set_random_state -->
<!-- signatures: set_random_state(s) -->
### Function: set_random_state (s)

Establece *s* como estado del generador de números aleatorios.


La función `set_random_state` devuelve `done` en todo caso.

<!-- category: Other -->
<!-- keywords: signum -->
<!-- signatures: signum(x) -->
### Function: signum (x)

Tanto sea *x* real o complejo, la función `signum` devuelve 0 si *x*
es cero. Para un valor no nulo de *x*, la función devuelve `x/abs(x)`.


Para valores no numéricos de *x*, Maxima intenta determinar el
signo del argumento. Cuando es negativo, cero o positivo, `signum`
devuelve -1, 0 o 1, respectivamente. En caso de no poder determinarse,
`signum` devuelve una forma simplificada equivalente. Estas 
simplificaciones incluyen la transformación de `signum(-x)`
en `-signum(x)` y la de `signum(x*y)` en
`signum(x) * signum(y)`.


La función `signum` es distributiva respecto de listas,
matrices o ecuaciones. Véase `distribute_over`.

<!-- category: Other -->
<!-- keywords: sin -->
<!-- signatures: sin(x) -->
### Function: sin (x)

Seno.

<!-- category: Other -->
<!-- keywords: sinh -->
<!-- signatures: sinh(x) -->
### Function: sinh (x)

Seno hiperbólico.

<!-- category: Other -->
<!-- keywords: sqrt -->
<!-- signatures: sqrt(x) -->
### Function: sqrt (x)

Raíz cuadrada de *x*. Se representa internamente por `x^(1/2)`.  Véase también `rootscontract`.


Si la variable `radexpand` vale `true` hará que las raíces `n`-ésimas de los factores de un producto que sean potencias de `n` sean extraídas del radical; por ejemplo, `sqrt(16*x^2)` se convertirá en `4*x` sólo si `radexpand` vale `true`.

<!-- category: Other -->
<!-- keywords: tan -->
<!-- signatures: tan(x) -->
### Function: tan (x)

Tangente.

<!-- category: Other -->
<!-- keywords: tanh -->
<!-- signatures: tanh(x) -->
### Function: tanh (x)

Tangente hiperbólica.

<!-- category: Other -->
<!-- keywords: trigexpand -->
<!-- signatures: trigexpand(expr) -->
### Function: trigexpand (expr)

Expande funciones trigonométricas e hiperbólicas de sumas de ángulos y de múltiplos de ángulos presentes en *expr*.  Para mejorar los resultados, *expr* debería expandirse. Para facilitar el control por parte del usuario de las simplificaciones, esta función tan solo expande un nivel de cada vez, expandiendo sumas de ángulos o de múltiplos de ángulos. A fin de obtener una expansión completa en senos y coseno, se le dará a la variable `trigexpand` el valor `true`.


La función `trigexpand` está controlada por las siguientes variables:



**trigexpand** — Si vale `true`, provoca la expansión de todas las expresiones que contengan senos y cosenos.
**trigexpandplus** — Controla la regla de la suma para `trigexpand`, la expansión de una suma como `sin(x + y)` se llevará a cabo sólo si `trigexpandplus` vale `true`.
**trigexpandtimes** — Controla la regla del producto para `trigexpand`, la expansión de un producto como `sin(2 x)` se llevará a cabo sólo si `trigexpandtimes` vale `true`.


Ejemplos:







```maxima
(%i1) x+sin(3*x)/sin(x),trigexpand=true,expand;
                         2           2
(%o1)               - sin (x) + 3 cos (x) + x


(%i2) trigexpand(sin(10*x+y));
(%o2)          cos(10 x) sin(y) + sin(10 x) cos(y)
```

<!-- category: Other -->
<!-- keywords: trigexpandplus -->
<!-- signatures: trigexpandplus -->
### Variable: trigexpandplus

Valor por defecto: `true`


La variable `trigexpandplus` controla la regla de la suma para `trigexpand`.  Así, si la instrucción `trigexpand` se utiliza o si la variable `trigexpand` vale `true`, se realizará la expansión de sumas como `sin(x+y)` sólo si `trigexpandplus` vale `true`.

<!-- category: Other -->
<!-- keywords: trigexpandtimes -->
<!-- signatures: trigexpandtimes -->
### Variable: trigexpandtimes

Valor por defecto: `true`


La variable `trigexpandtimes` controla la regla del producto para `trigexpand`.  Así, si la instrucción `trigexpand` se utiliza o si la variable `trigexpand` vale `true`, se realizará la expansión de productos como `sin(2*x)` sólo si `trigexpandtimes` vale `true`.

<!-- category: Other -->
<!-- keywords: triginverses -->
<!-- signatures: triginverses -->
### Variable: triginverses

Valor por defecto: `true`


La variable `triginverses` controla la simplificación de la composición de funciones trigonométricas e hiperbólicas con sus funciones inversas.


Si vale `all`, tanto `atan(tan(x))`  como `tan(atan(x))` se reducen a *x*.  


Si vale `true`, se desactiva la simplificación de `arcfun(fun(x))`.


Si vale `false`, se desactivan las simplificaciones de 
`arcfun(fun(x))` y 
`fun(arcfun(x))`.

<!-- category: Other -->
<!-- keywords: trigrat -->
<!-- signatures: trigrat(expr) -->
### Function: trigrat (expr)

Devuelve una forma canónica simplificada cuasi-lineal de una expresión trigonométrica;
*expr* es una fracción racional que contiene `sin`, `cos` o `tan`, 
cuyos argumentos son formas lineales respecto de ciertas variables (o kernels) y `%pi/n`
(*n* entero) con coeficientes enteros. El resultado es una fracción simplificada con 
el numerador y denominador lineales respecto de `sin` y `cos`. Así,
 `trigrat` devuelve una expresión lineal siempre que sea posible.






```maxima
(%i1) trigrat(sin(3*a)/sin(a+%pi/3));
(%o1)            sqrt(3) sin(2 a) + cos(2 a) - 1
```


El siguiente ejemplo se ha tomado de
Davenport, Siret y Tournier, *Calcul Formel*, Masson (o en inglés,
Addison-Wesley), sección 1.5.5, teorema de Morley.










```maxima
(%i1) c : %pi/3 - a - b$

(%i2) bc : sin(a)*sin(3*c)/sin(a+b);
                                          %pi
                  sin(a) sin(3 (- b - a + ---))
                                           3
(%o2)             -----------------------------
                           sin(b + a)


(%i3) ba : bc, c=a, a=c;
                                         %pi
                    sin(3 a) sin(b + a - ---)
                                          3
(%o3)               -------------------------
                                  %pi
                          sin(a - ---)
                                   3


(%i4) ac2 : ba^2 + bc^2 - 2*bc*ba*cos(b);
         2         2         %pi
      sin (3 a) sin (b + a - ---)
                              3
(%o4) ---------------------------
                2     %pi
             sin (a - ---)
                       3
                                       %pi
 - (2 sin(a) sin(3 a) sin(3 (- b - a + ---)) cos(b)
                                        3
             %pi            %pi
 sin(b + a - ---))/(sin(a - ---) sin(b + a))
              3              3
      2       2              %pi
   sin (a) sin (3 (- b - a + ---))
                              3
 + -------------------------------
                2
             sin (b + a)


(%i5) trigrat (ac2);
(%o5) - (sqrt(3) sin(4 b + 4 a) - cos(4 b + 4 a)
 - 2 sqrt(3) sin(4 b + 2 a) + 2 cos(4 b + 2 a)
 - 2 sqrt(3) sin(2 b + 4 a) + 2 cos(2 b + 4 a)
 + 4 sqrt(3) sin(2 b + 2 a) - 8 cos(2 b + 2 a) - 4 cos(2 b - 2 a)
 + sqrt(3) sin(4 b) - cos(4 b) - 2 sqrt(3) sin(2 b) + 10 cos(2 b)
 + sqrt(3) sin(4 a) - cos(4 a) - 2 sqrt(3) sin(2 a) + 10 cos(2 a)
 - 9)/4
```

<!-- category: Other -->
<!-- keywords: trigreduce -->
<!-- signatures: trigreduce(expr, x), trigreduce(expr) -->
### Function: trigreduce (expr, x)

Combina productos y potencias de senos y cosenos trigonométricos e hiperbólicos de *x*, transformándolos en otros que son múltiplos de *x*.  También intenta eliminar estas funciones cuando aparecen en los denominadores.  Si no se introduce el argumento *x*, entonces se utilizan todas las variables de *expr*.


Véase también `poissimp`.






```maxima
(%i1) trigreduce(-sin(x)^2+3*cos(x)^2+x);
               cos(2 x)      cos(2 x)   1        1
(%o1)          -------- + 3 (-------- + -) + x - -
                  2             2       2        2
```



Las rutinas de simplificación trigonométrica utilizan información declarada en algunos casos sencillos. Las declaraciones sobre variables se utilizan como se indica a continuación:








```maxima
(%i1) declare(j, integer, e, even, o, odd)$
(%i2) sin(x + (e + 1/2)*%pi);
(%o2)                        cos(x)
(%i3) sin(x + (o + 1/2)*%pi);
(%o3)                       - cos(x)
```

<!-- category: Other -->
<!-- keywords: trigsign -->
<!-- signatures: trigsign -->
### Variable: trigsign

Valor por defecto: `true`


Si `trigsign` vale `true`, se permite la simplificación de argumentos negativos en funciones trigonométricas, como en `sin(-x)`, que se transformará en `-sin(x)` sólo si `trigsign` vale `true`.

<!-- category: Other -->
<!-- keywords: trigsimp -->
<!-- signatures: trigsimp(expr) -->
### Function: trigsimp (expr)

Utiliza las identidades $sin(x)^2 + cos(x)^2 = 1$ y
$cosh(x)^2 - sinh(x)^2 = 1$ para simplificar expresiones que contienen `tan`, `sec`,
etc., en expresiones con `sin`, `cos`, `sinh`, `cosh`.


Las funciones `trigreduce`, `ratsimp` y `radcan` puden seguir siendo útiles para continuar el proceso de simplificación.


La instrucción `demo ("trgsmp.dem")` muestra algunos ejemplos de `trigsimp`.

