## Simplificación

<!-- category: Simplification -->
<!-- keywords: additive -->
<!-- signatures: additive -->
### Variable: additive

Si `declare(f,additive)` ha sido ejecutado, entonces: 


(1) Si `f` es univariado, cada vez que el simplificador encuentre
`f` aplicada a una suma, `f` será distribuida bajo esta suma. Por ejemplo, `f(x+y)` se simplificará a `f(x)+f(y)`. 


(2) Si `f` es una función de 2 o más argumentos, aditivamente es definida como aditiva en el primer argumento de `f`, como en el caso de `sum` o `integrate`. Por ejemplo, `f(h(x)+g(x),x)` se simplificará a `f(h(x),x)+f(g(x),x)`. Esta simplificación no ocurre cuando `f` se aplica a expresiones de la forma `sum(x[i],i,lower-limit,upper-limit)`.


Ejemplo:








```maxima
(%i1) F3 (a + b + c);
(%o1)                     F3(c + b + a)
(%i2) declare (F3, additive);
(%o2)                         done
(%i3) F3 (a + b + c);
(%o3)                 F3(c) + F3(b) + F3(a)
```

<!-- category: Simplification -->
<!-- keywords: antisymmetric -->
<!-- signatures: antisymmetric -->
### Variable: antisymmetric

Si `declare(h,antisymmetric)` es ejecutado, esto dice al 
simplificador que `h` es antisimétrico. E.g. `h(x,z,y)` será 
simplificado a `-h(x,y,z)`. Que es, el producto de (-1)^n por el resultado 
dado por `symmetric` o `commutative`, donde n es el número de intercambios 
necesarios de dos argumentos para convertirle a esta forma.  


Ejemplos:













```maxima
(%i1) S (b, a);
(%o1)                        S(b, a)
(%i2) declare (S, symmetric);
(%o2)                         done
(%i3) S (b, a);
(%o3)                        S(a, b)
(%i4) S (a, c, e, d, b);
(%o4)                   S(a, b, c, d, e)
(%i5) T (b, a);
(%o5)                        T(b, a)
(%i6) declare (T, antisymmetric);
(%o6)                         done
(%i7) T (b, a);
(%o7)                       - T(a, b)
(%i8) T (a, c, e, d, b);
(%o8)                   T(a, b, c, d, e)
```

<!-- category: Simplification -->
<!-- keywords: combine -->
<!-- signatures: combine(expr) -->
### Function: combine (expr)

Simplifica la suma *expr* combinando términos de con igual denominador reduciéndolos a un único término.

<!-- category: Simplification -->
<!-- keywords: commutative -->
<!-- signatures: commutative -->
### Variable: commutative

Si `declare(h,commutative)` es ejecutado, le dice al simplificador
que `h` es una función conmutaiva. Por ejemplo, `h(x,z,y)` se simplificará a `h(x,y,z)`. Esto es lo mismo que `symmetric`.

<!-- category: Simplification -->
<!-- keywords: demoivre -->
<!-- signatures: demoivre(expr) -->
### Function: demoivre (expr)

La función `demoivre (expr)` convierte una expresión sin modificar la variable global `demoivre`.


Cuando `demoivre` vale `true`, los exponenciales complejos se convierten en expresiones equivalentes pero en términos de las funciones trigonométricas:
`exp (a + b*%i)` se reduce a `%e^a * (cos(b) + %i*sin(b))`
si `b` no contiene a `%i`. Las expresiones `a` y `b` no se expanden.


El valor por defecto de `demoivre` es `false`.


La función `exponentialize` convierte funciones trigonométricas e hiperbólicas a la forma exponencial, por lo que  `demoivre` y `exponentialize` no pueden valer `true` al mismo tiempo.

<!-- category: Simplification -->
<!-- keywords: distrib -->
<!-- signatures: distrib(expr) -->
### Function: distrib (expr)

Distribuye sumas sobre productos. Difiere de `expand`
en que trabaja sólo al nivel superior de una expresión, siendo más rápida que `expand`.  Difiere de  `multthru` en que expande todas las sumas del nivel superior.


Ejemplos:



```maxima
(%i1) distrib ((a+b) * (c+d));
(%o1)                 b d + a d + b c + a c
(%i2) multthru ((a+b) * (c+d));
(%o2)                 (b + a) d + (b + a) c
(%i3) distrib (1/((a+b) * (c+d)));
                                1
(%o3)                    ---------------
                         (b + a) (d + c)
(%i4) expand (1/((a+b) * (c+d)), 1, 0);
                                1
(%o4)                 ---------------------
                      b d + a d + b c + a c
```

<!-- category: Simplification -->
<!-- keywords: distribute_over -->
<!-- signatures: distribute_over -->
### Variable: distribute_over

Valor por defecto: `true`


`distribute_over` controla la distribución de funciones sobre
estructuras como listas, matrices y ecuaciones. Actualmente, no todas
las funciones de Maxima tienen esta propiedad. Es posible consultar si
una función tiene esta propiedad con la instrucción `properties`.


La propiedad distributiva se desactiva asignándole a `distribute_over`
el valor `false`.


Ejemplos:


La función `sin` se distribuye sobre una lista:






```maxima
(%i1) sin([x,1,1.0]);
(%o1)                 [sin(x), sin(1), .8414709848078965]
```


`mod` es una función de dos argumentos que se distribuye sobre listas.
La distribución sobre listas anidadas también es posible.







```maxima
(%i2) mod([x,11,2*a],10);
(%o2)                    [mod(x, 10), 1, 2 mod(a, 5)]
(%i3) mod([[x,y,z],11,2*a],10);
(%o3)       [[mod(x, 10), mod(y, 10), mod(z, 10)], 1, 2 mod(a, 5)]
```


Distribución de la función `floor` sobre una matriz y una
ecuación.







```maxima
(%i4) floor(matrix([a,b],[c,d]));
                            [ floor(a)  floor(b) ]
(%o4)                       [                    ]
                            [ floor(c)  floor(d) ]
(%i5) floor(a=b);
(%o5)                         floor(a) = floor(b)
```


Funciones con más de un argumento se distribuyen sobre cualquiera
de sus argumentos, o sobre todos ellos.






```maxima
(%i6) expintegral_e([1,2],[x,y]);
(%o6) [[expintegral_e(1, x), expintegral_e(1, y)], 
       [expintegral_e(2, x), expintegral_e(2, y)]]
```


Comprueba si una función tiene la propiedad `distribute_over`:






```maxima
(%i7) properties(abs);
(%o7) [integral, distributes over bags, noun, rule, gradef]
```

<!-- category: Simplification -->
<!-- keywords: domain -->
<!-- signatures: domain -->
### Variable: domain

Valor por defecto: `real`


Si `domain` vale `complex`, `sqrt (x^2)` permanecerá como
`sqrt (x^2)` en lugar de devolver `abs(x)`.

<!-- category: Simplification -->
<!-- keywords: evenfun, oddfun -->
<!-- signatures: oddfun -->
### Variable: evenfun

`declare(f, evenfun` o `declare(f, oddfun)` indican a Maxima que reconozca
la función `f` como par o impar, respectivamente.


Ejemplos:



```maxima
(%i1) o (- x) + o (x);
(%o1)                     o(x) + o(- x)
(%i2) declare (o, oddfun);
(%o2)                         done
(%i3) o (- x) + o (x);
(%o3)                           0
(%i4) e (- x) - e (x);
(%o4)                     e(- x) - e(x)
(%i5) declare (e, evenfun);
(%o5)                         done
(%i6) e (- x) - e (x);
(%o6)                           0
```

<!-- category: Simplification -->
<!-- keywords: expand -->
<!-- signatures: expand(expr), expand(expr, p, n) -->
### Function: expand (expr)

Expande la expresión *expr*. Los productos de sumas y de sumas con exponentes se multiplican, los numeradores de las expresiones racionales que son sumas se separan en sus respectivos términos, y las multiplicaciones (tanto las que son conmutativas como las que no) se distribuyen sobre las sumas en todos los niveles de *expr*.


En el caso de los polinomios es más aconsejable utilizar `ratexpand`, que utiliza un algoritmo más eficiente.


Las variables `maxnegex` y `maxposex` controlan los máximos exponentes negativos y positivos que se van a expandir.


La llamada `expand (expr, p, n)` expande *expr* asignando a `maxposex` el valor *p* y a `maxnegex` el *n*. Esto es útil para expandir sólo parte de la expresión.


La variable `expon` guarda el mayor exponente negativo que será expandido automáticamente, independientemente de `expand`. Por ejemplo, si `expon` vale 4 entonces `(x+1)^(-5)` no se expandirá automáticamente.


La variable `expop` guarda el mayor exponente positivo que será expandido automáticamente.  Así, `(x+1)^3` se expandirá automáticamente sólo si `expop` es mayor o igual que 3. Si se quiere expandir `(x+1)^n`, siendo `n` mayor que `expop`, entonces `expand ((x+1)^n)` se desarrollará sólo si `maxposex` no es menor que `n`.


`expand(expr, 0, 0)` provoca que se vuelva a simplificar `expr`.
`expr` no se vuelve a evaluar. A diferencia de `ev(expr, noeval)`,
se elimina la representación canónica de la expresión. 
Véase también `ev`.


La variable `expand` utilizada con `ev` provocará una expansión.


El fichero `share/simplification/facexp.mac`
contiene algunas funciones relacionadas con `expand` (en concreto, `facsum`, `factorfacsum`
y `collectterms`, que se cargan automáticamente) y variables (`nextlayerfactor`
y `facsum_combine`) que permiten al usuario estructurar las expresiones controlando la expansión.

En  `simplification/facexp.usg` se pueden encontrar breves descripciones de estas funciones.
Se accederá a una demostración con la instrucción `demo("facexp")`.


Ejemplo:











```maxima
(%i1) expr:(x+1)^2*(y+1)^3;
                                      2        3
(%o1)                          (x + 1)  (y + 1)
(%i2) expand(expr);
       2  3        3    3      2  2        2      2      2
(%o2) x  y  + 2 x y  + y  + 3 x  y  + 6 x y  + 3 y  + 3 x  y
                                                 2
                                + 6 x y + 3 y + x  + 2 x + 1

(%i3) expand(expr,2);
                      2        3              3          3
(%o3)                x  (y + 1)  + 2 x (y + 1)  + (y + 1)

(%i4) expr:(x+1)^-2*(y+1)^3;
                                          3
                                   (y + 1)
(%o4)                              --------
                                          2
                                   (x + 1)
(%i5) expand(expr);
                 3               2
                y             3 y            3 y             1
(%o5)      ------------ + ------------ + ------------ + ------------
            2              2              2              2
           x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1

(%i6) expand(expr,2,2);
                                          3
                                   (y + 1)
(%o6)                            ------------
                                  2
                                 x  + 2 x + 1
```


Vuelve a simplificar una expresión pero sin expansión:








```maxima
(%i7) expr:(1+x)^2*sin(x);
                                       2
(%o7)                           (x + 1)  sin(x)
(%i8) exponentialize:true;
(%o8)                                true
(%i9) expand(expr,0,0);
                                   2    %i x     - %i x
                         %i (x + 1)  (%e     - %e      )
(%o9)                  - -------------------------------
                                        2
```

<!-- category: Simplification -->
<!-- keywords: expandwrt -->
<!-- signatures: expandwrt(expr, x_1, ..., x_n) -->
### Function: expandwrt (expr, x_1, ..., x_n)

Expande la expresión `expr` con respecto a las variables *x_1*, ..., *x_n*.
Todos los productos que contengan a las variables aparecen explícitamente. El resultado que se obtenga no tendr’a productos de sumas de expresiones que contengan a las variables. Los argumentos  *x_1*, ..., *x_n*
pueden ser variables, operadores o expresiones.


Por defecto, no se expanden los denominadores, pero esto puede cambiarse mediante el uso de la variable `expandwrt_denom`.


Esta función se carga automáticamente de `simplification/stopex.mac`.

<!-- category: Simplification -->
<!-- keywords: expandwrt_denom -->
<!-- signatures: expandwrt_denom -->
### Variable: expandwrt_denom

Valor por defecto: `false`


La variable `expandwrt_denom` controla el tratamiento de las expresiones racinales por parte de `expandwrt`. Si vale `true`, se expandirán tanto el numerador como el denominador de la expresión respecto de los argumentos de `expandwrt`, pero si `expandwrt_denom` vale `false`, sólo se expandirá el numerador.

<!-- category: Simplification -->
<!-- keywords: expandwrt_factored -->
<!-- signatures: expandwrt_factored(expr, x_1, ..., x_n) -->
### Function: expandwrt_factored (expr, x_1, ..., x_n)

Es similar a `expandwrt`, pero trata a las expresiones que son productos de una forma algo diferente. La función
`expandwrt_factored` expande sólo aquellos factores de `expr` que contienen a las variables *x_1*, ..., *x_n*.



Esta función se carga automáticamente de `simplification/stopex.mac`.

<!-- category: Simplification -->
<!-- keywords: expon -->
<!-- signatures: expon -->
### Variable: expon

Valor por defecto: 0


La variable `expon` guarda el mayor exponente negativo que será expandido automáticamente, independientemente de `expand`. Por ejemplo, si `expon` vale 4 entonces `(x+1)^(-5)` no se expandirá automáticamente.

<!-- category: Simplification -->
<!-- keywords: exponentialize -->
<!-- signatures: exponentialize(expr) -->
### Function: exponentialize (expr)

La función `exponentialize (expr)` convierte las funciones trigonométricas e hiperbólicas de *expr* a exponenciales, sin alterar la variable global `exponentialize`.


Cuando la variable `exponentialize` vale `true`, todas las funciones trigonométricas e hiperbólicas se convierten a forma exponencial. El valor por defecto es `false`.


La función `demoivre` convierte funciones trigonométricas e hiperbólicas a la forma exponencial, por lo que  `demoivre` y `exponentialize` no pueden valer `true` al mismo tiempo.

<!-- category: Simplification -->
<!-- keywords: expop -->
<!-- signatures: expop -->
### Variable: expop

Valor por defecto: 0


La variable `expop` guarda el mayor exponente positivo que será expandido automáticamente.  Así, `(x+1)^3` se expandirá automáticamente sólo si `expop` es mayor o igual que 3. Si se quiere expandir `(x+1)^n`, siendo `n` mayor que `expop`, entonces `expand ((x+1)^n)` se desarrollará sólo si `maxposex` no es menor que `n`.

<!-- category: Simplification -->
<!-- keywords: lassociative -->
<!-- signatures: lassociative -->
### Variable: lassociative

La instrucción `declare (g, lassociative)` le indica al simplificador de Maxima que `g` es asociativo por la izquierda.  Por ejemplo, `g (g (a, b), g (c, d))`se reduce a `g (g (g (a, b), c), d)`.

<!-- category: Simplification -->
<!-- keywords: linear -->
<!-- signatures: linear -->
### Variable: linear

Es una de las propiedades de operadores de Maxima. Si la función 
univariante `f` se declara lineal, la expansión de  `f(x + y)` 
produce `f(x) + f(y)`, `f(a*x)` produce `a*f(x)` si `a` 
es una constante.  Si la función tiene dos o más argumentos, la linealidad 
se interpreta como la de `sum` o `integrate`, esto es, 
`f (a*x + b, x)` produce `a*f(x,x) + b*f(1,x)` si `a` y `b` 
no contienen a `x`.


`linear` equivale a `additive` y `outative`.
Véase también `opproperties`.


Ejemplo:








```maxima
(%i1) 'sum (F(k) + G(k), k, 1, inf);
                       inf
                       ====
                       \
(%o1)                   >    (G(k) + F(k))
                       /
                       ====
                       k = 1
(%i2) declare (nounify (sum), linear);
(%o2)                         done
(%i3) 'sum (F(k) + G(k), k, 1, inf);

                     inf          inf
                     ====         ====
                     \            \
(%o3)                 >    G(k) +  >    F(k)
                     /            /
                     ====         ====
                     k = 1        k = 1
```

<!-- category: Simplification -->
<!-- keywords: maxnegex -->
<!-- signatures: maxnegex -->
### Variable: maxnegex

Valor por defecto: 1000


La variable `maxnegex` es el mayor exponente negativo que expandirá la función `expand`. Véase también `maxposex`.

<!-- category: Simplification -->
<!-- keywords: maxposex -->
<!-- signatures: maxposex -->
### Variable: maxposex

Valor por defecto: 1000


La variable `maxposex` es el mayor exponenteque expandirá la función `expand`. Véase también `maxnegex`.

<!-- category: Simplification -->
<!-- keywords: multiplicative -->
<!-- signatures: multiplicative -->
### Variable: multiplicative

La instrucción `declare (f, multiplicative)` indica al simplificador de Maxima que `f` is multiplicativa.



1. Si `f` es univariante, cada vez que el simplificador encuentre a `f` aplicad a un producto, `f` se distribuirá sobre ese producto.  Por ejemplo, `f(x*y)` se reduciría a `f(x)*f(y)`.
2. Si `f` es una función de 2 o más argumentos, la multiplicabilidad se define como multiplicabilidad para el primer argumento de `f`, de modo que `f (g(x) * h(x), x)` se reduciría a `f (g(x) ,x) * f (h(x), x)`.


Esta transformación no se realiza cuando `f` se aplica a expresiones de la forma `product (x[i], i, m, n)`.


Ejemplo:








```maxima
(%i1) F2 (a * b * c);
(%o1)                       F2(a b c)
(%i2) declare (F2, multiplicative);
(%o2)                         done
(%i3) F2 (a * b * c);
(%o3)                   F2(a) F2(b) F2(c)
```

<!-- category: Simplification -->
<!-- keywords: multthru -->
<!-- signatures: multthru(expr), multthru(expr_1, expr_2) -->
### Function: multthru (expr)

Multiplica un factor (que debería ser una suma) de *expr* por los otros factores de *expr*.  Esto es, *expr* es `f_1 f_2 ... f_n`, donde al menos un factor, por ejemplo *f_i*, es una suma de términos.  Cada término en esta suma se multiplica por los otros factores del producto, excepto el propio *f_i*. La función  `multthru` no expande sumas elevadas a exponentes, siendo el método más rápido para distribuir productos (sean o no conmutativos) sobre sumas. Puesto que los cocientes se representan como productos, puede utilizarse`multthru` para dividir sumas entre productos.


La llamada `multthru (expr_1, expr_2)` multiplica cada término de *expr_2* (que debería ser una suma o una ecuación) por *expr_1*.  Si *expr_1* no es ella misma una suma, entonces la llamada es equivalente a `multthru (expr_1*expr_2)`.



```maxima
(%i1) x/(x-y)^2 - 1/(x-y) - f(x)/(x-y)^3;
                      1        x         f(x)
(%o1)             - ----- + -------- - --------
                    x - y          2          3
                            (x - y)    (x - y)
(%i2) multthru ((x-y)^3, %);
                           2
(%o2)             - (x - y)  + x (x - y) - f(x)
(%i3) ratexpand (%);
                           2
(%o3)                   - y  + x y - f(x)
(%i4) ((a+b)^10*s^2 + 2*a*b*s + (a*b)^2)/(a*b*s^2);
                        10  2              2  2
                 (b + a)   s  + 2 a b s + a  b
(%o4)            ------------------------------
                                  2
                             a b s
(%i5) multthru (%);  /* note that this does not expand (b+a)^10 */
                                        10
                       2   a b   (b + a)
(%o5)                  - + --- + ---------
                       s    2       a b
                           s
(%i6) multthru (a.(b+c.(d+e)+f));
(%o6)            a . f + a . c . (e + d) + a . b
(%i7) expand (a.(b+c.(d+e)+f));
(%o7)         a . f + a . c . e + a . c . d + a . b
```

<!-- category: Simplification -->
<!-- keywords: negdistrib -->
<!-- signatures: negdistrib -->
### Variable: negdistrib

Valor por defecto: `true`


Si `negdistrib` vale `true`, -1 se distribuye sobre una expresión.  Por ejemplo, `-(x + y)` se transforma en `- y - x`.  Dándole el valor `false` se mostrará `- (x + y)` tal cual. Esto puede ser útil, pero también peligroso; al igual que el indicador `simp`, no conviene asignarle el valor `false`.

<!-- category: Simplification -->
<!-- keywords: opproperties -->
<!-- signatures: opproperties -->
### Variable: opproperties

La variable `opproperties` es la lista con las propiedades especiales de los operadores reconocidas por el simplificador de Maxima:
`linear`, `additive`, `multiplicative`, `outative`, `evenfun`,
`oddfun`, `commutative`, `symmetric`, `antisymmetric`, `nary`, 
`lassociative`, `rassociative`.

<!-- category: Simplification -->
<!-- keywords: outative -->
<!-- signatures: outative -->
### Variable: outative

La instrucción `declare (f, outative)` le indica al simplificador de Maxima 
que los factores constantes del argumento de la función `f` pueden ser 
extraídos.



1. Si `f` es univariante, cada vez que el simplificador se encuentra con `f` 
aplicada a un producto, éste será particionado en factores que son constantes y 
factores que no lo son, siendo entonces los constantes extraídos de la 
función.  Por ejemplo, `f(a*x)` se reducirá a `a*f(x)` siendo `a` 
una constante. Las constantes no atómicas no serán extraídas.
2. Si `f` es una función de 2 o más argumentos, esta propiedad se define como 
en  `sum` o `integrate`, esto es, `f (a*g(x), x)` se reducirá a 
`a * f(g(x), x)` si `a` no contiene a `x`.


Las funciones `sum`, `integrate` y `limit` han sido todas declaradas 
con la propiedad `outative`.


Ejemplo:










```maxima
(%i1) F1 (100 * x);
(%o1)                       F1(100 x)
(%i2) declare (F1, outative);
(%o2)                         done
(%i3) F1 (100 * x);
(%o3)                       100 F1(x)
(%i4) declare (zz, constant);
(%o4)                         done
(%i5) F1 (zz * y);
(%o5)                       zz F1(y)
```

<!-- category: Simplification -->
<!-- keywords: radcan -->
<!-- signatures: radcan(expr) -->
### Function: radcan (expr)

Simplifica la expresión *expr*, que puede contener logaritmos, exponenciales y
radicales, convirtiéndola a una forma canónica, lo que significa que todas las expresiones funcionalmente equivalentes
se reducen a una forma única.  Ciertas expresiones, sin embargo, son reducidas por `radcan` a una forma regular, lo que significa que dos expresiones equivalentes no tienen necesariamente el mismo aspecto, pero su diferencia puede ser reducida por `radcan` a cero.


Con algunas expresiones `radcan` puede consunir mucho tiempo. Este es el coste por explorar ciertas relaciones entre las componentes de la expresión para simplificaciones basadas en factorizaciones y expansiones parciales de fracciones de exponentes.  


Ejemplos:








```maxima
(%i1) radcan((log(x+x^2)-log(x))^a/log(1+x)^(a/2));
                                           a/2
(%o1)                            log(x + 1)

(%i2) radcan((log(1+2*a^x+a^(2*x))/log(1+a^x)));
(%o2)                                  2

(%i3) radcan((%e^x-1)/(1+%e^(x/2)));
                                     x/2
(%o3)                              %e    - 1
```

<!-- category: Simplification -->
<!-- keywords: radexpand -->
<!-- signatures: radexpand -->
### Variable: radexpand

Valor por defecto: `true`


La variable `radexpand` controla algunas simplificaciones de radicales.


Si `radexpand` vale `all`, las raíces *n*-ésimas de los factores de un producto que sean potencias de *n* se extraen del símbolo radical. Por ejemplo, si `radexpand` vale `all`, `sqrt (16*x^2)` se reduce a `4*x`.



Más concretamente, considérese `sqrt (x^2)`.


- *
Si `radexpand` vale `all` o se ha ejecutado `assume (x > 0)`, 
`sqrt(x^2)` se reduce a `x`.
- *
Si `radexpand` vale `true` y `domain` es `real` (su valor por defecto), 
`sqrt(x^2)` se reduce a `abs(x)`.
- *
Si `radexpand` vale `false` o `radexpand` vale `true` y `domain` es `complex`, 
`sqrt(x^2)` no se simplifica.



Nótese que  `domain` sólo se tiene en cuenta si `radexpand` vale `true`.

<!-- category: Simplification -->
<!-- keywords: rassociative -->
<!-- signatures: rassociative -->
### Variable: rassociative

La instrucción `declare (g, rassociative)` le indica al simplificador de Maxima que `g` es asociativa por la derecha.  Por ejemplo, `g(g(a, b), g(c, d))` se reduce a `g(a, g(b, g(c, d)))`.

<!-- category: Simplification -->
<!-- keywords: scsimp -->
<!-- signatures: scsimp(expr, rule_1, ..., rule_n) -->
### Function: scsimp (expr, rule_1, ..., rule_n)

Es el "Sequential Comparative Simplification" (método debido a Stoute).
La función `scsimp` intenta simplificar *expr* de acuerdo con las reglas *rule_1*, ..., *rule_n*.
Si se obtiene una expresión más pequeña, el proceso se repite. En caso contrario, después de que se hayan intentado todas las simplificaciones, devuelve la respuesta original.


La instrucción `example (scsimp)` muestra algunos ejemplos.

<!-- category: Simplification -->
<!-- keywords: simp -->
<!-- signatures: simp -->
### Variable: simp

Valor por defecto: `true`


La variable `simp` activa y desactiva la simplificación.
La simplificación está activada por defecto. La variable `simp`
también es reconocida por la función `ev` como variable de entorno.
Véase también `ev`.


Cuando `simp` se utiliza en un entorno `ev` con el valor `false`,
la simplificación se evita sólo durante la fase de evaluación de una
expresión. La variable no evita la simplificación que sigue a la fase de
evaluación.


Ejemplos:


La simplificación se suspende globalmente. La expresión `sin(1.0)`
no se simplifica a su valor numérico. La variable de entorno `simp`
conmuta el estado de la simplificación.








```maxima
(%i1) simp:false;
(%o1)                                false
(%i2) sin(1.0);
(%o2)                              sin(1.0)
(%i3) sin(1.0),simp;
(%o3)                          .8414709848078965
```


La simplificación se vuelve a activar. La variable de entorno `simp`
no puede suprimir totalmente la simplificación. El resultado muestra una
expresión simplificada, pero la variable `x` guarda como valor una
expresión sin simplificar, porque la asignación se realizó durante 
la fase de evaluación de la expresión.








```maxima
(%i4) simp:true;
(%o4)                                true
(%i5) x:sin(1.0),simp:false;
(%o5)                          .8414709848078965
(%i6) :lisp $X
((%SIN) 1.0)
```

<!-- category: Simplification -->
<!-- keywords: symmetric -->
<!-- signatures: symmetric -->
### Variable: symmetric

La instrucción `declare (h, symmetric)` le indica al simplificador de  Maxima que `h` es una función simétrica.  Por ejemplo, `h (x, z, y)`  se reduce a `h (x, y, z)`.


El nombre `commutative` es sinónimo de `symmetric`.

<!-- category: Simplification -->
<!-- keywords: xthru -->
<!-- signatures: xthru(expr) -->
### Function: xthru (expr)

Combina todos los términos de *expr* (la cual debe ser una suma) sobre un común denominador sin expandir productos ni sumas elevadas a exponentes al modo que lo hace `ratsimp`. La función `xthru` cancela factores comunes en el numerador y denominador de expresiones racionales, pero sólo si los factores son explícitos.


En ocasiones puede ser útil el uso de `xthru` antes de la llamada a `ratsimp` a fin de cancelar factores explícitos del máximo común divisor del numerador y denominador y así simplificar la expresión a la que se va a aplicar `ratsimp`.







```maxima
(%i1) ((x+2)^20 - 2*y)/(x+y)^20 + (x+y)^(-19) - x/(x+y)^20;
 xthru (%);
                                20
                 1       (x + 2)   - 2 y       x
(%o1)        --------- + --------------- - ---------
                    19             20             20
             (y + x)        (y + x)        (y + x)
```

