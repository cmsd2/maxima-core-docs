## romberg

<!-- category: Calculus -->
<!-- keywords: romberg -->
<!-- signatures: romberg(expr, x, a, b), romberg(F, a, b) -->
### Function: romberg (expr, x, a, b)

Integra numéricamente por el método de Romberg.


La llamada `romberg(expr, x, a, b)`
devuelve una estimación de la integral `integrate(expr, x, a, b)`.
El argumento *expr* debe ser una expresión reducible a un valor decimal
en coma flotante cuando *x* es a su vez un número decimal.


La llamada `romberg(F, a, b)` devuelve una estimación
de la integral `integrate(F(x), x, a, b)`, siendo
`x` el único argumento de *F*. El argumento *F* debe ser 
una función en Lisp o en Maxima que devuelva un valor decimal
en coma flotante cuando *x* es a su vez un número decimal; *F*
puede ser el nombre de una función de Maxima traducida o compilada.


La exactitud de `romberg` se controla con las variables globales 
`rombergabs` y `rombergtol`. La función `romberg`
termina con éxito su cálculo cuando la diferencia absoluta entre
sucesivas aproximaciones es menor que `rombergabs`,
o cuando la diferencia relativa de sucesivas aproximaciones es menor que
`rombergtol`. Así, cuando `rombergabs` vale 0.0
(su valor por defecto) sólo tiene efecto el test del error relativo basado
en `romberg`.


La función `romberg` reduce a mitades sucesivas la amplitud del paso un máximo de
`rombergit` veces antes de abandonar el cómputo; el número máximo de 
evaluaciones del integrando es, por consiguiente, igual a `2^rombergit`.
De no satisfacerse el criterio de error establecido por `rombergabs` y
`rombergtol`,  `romberg` devuelve un mensaje de error.
La función `romberg` hace siempre al menos `rombergmin`
iteraciones; se trata de una heurística para evitar
la finalización prematura cuando el integrando oscila mucho.


La función `romberg` evalúa el integrando repetidamente tras asignarle
a la variable de integración un valor específico. Este criterio
permite anidar llamadas a `romberg` para calcular integrales múltiples.
Sin embargo, los errores de cálculo no tienen en cuenta los errores de 
las integraciones anidadas, por lo que tales errores pueden subestimarse.
Por otro lado, métodos especialmente desarrollados para integraciones
múltiples pueden dar la misma exactitud con menos evaluaciones
del integrando.


Para hacer uso de esta función ejecútese primero `load("romberg")`.


Véase también `QUADPACK`, un conjunto de funciones para 
integración numérica.


Ejemplos:


Una integración unidimensional.













```maxima
(%i1) load ("romberg");
(%o1)    /usr/share/maxima/5.11.0/share/numeric/romberg.lisp
(%i2) f(x) := 1/((x - 1)^2 + 1/100) + 1/((x - 2)^2 + 1/1000)
                + 1/((x - 3)^2 + 1/200);
                    1                 1                1
(%o2) f(x) := -------------- + --------------- + --------------
                     2    1           2    1            2    1
              (x - 1)  + ---   (x - 2)  + ----   (x - 3)  + ---
                         100              1000              200
(%i3) rombergtol : 1e-6;
(%o3)                 9.9999999999999995E-7
(%i4) rombergit : 15;
(%o4)                          15
(%i5) estimate : romberg (f(x), x, -5, 5);
(%o5)                   173.6730736617464
(%i6) exact : integrate (f(x), x, -5, 5);
(%o6) 10 sqrt(10) atan(70 sqrt(10))
 + 10 sqrt(10) atan(30 sqrt(10)) + 10 sqrt(2) atan(80 sqrt(2))
 + 10 sqrt(2) atan(20 sqrt(2)) + 10 atan(60) + 10 atan(40)
(%i7) abs (estimate - exact) / exact, numer;
(%o7)                7.5527060865060088E-11
```


Una integración bidimensional, implementada mediante llamadas anidadas a `romberg`.













```maxima
(%i1) load ("romberg");
(%o1)    /usr/share/maxima/5.11.0/share/numeric/romberg.lisp
(%i2) g(x, y) := x*y / (x + y);
                                    x y
(%o2)                   g(x, y) := -----
                                   x + y
(%i3) rombergtol : 1e-6;
(%o3)                 9.9999999999999995E-7
(%i4) estimate : romberg (romberg (g(x, y), y, 0, x/2), x, 1, 3);
(%o4)                   0.81930239628356
(%i5) assume (x > 0);
(%o5)                        [x > 0]
(%i6) integrate (integrate (g(x, y), y, 0, x/2), x, 1, 3);
                                          3
                                    2 log(-) - 1
                    9                     2        9
(%o6)       - 9 log(-) + 9 log(3) + ------------ + -
                    2                    6         2
(%i7) exact : radcan (%);
                    26 log(3) - 26 log(2) - 13
(%o7)             - --------------------------
                                3
(%i8) abs (estimate - exact) / exact, numer;
(%o8)                1.3711979871851024E-10
```

<!-- category: Calculus -->
<!-- keywords: rombergabs -->
<!-- signatures: rombergabs -->
### Variable: rombergabs

Valor por defecto: 0.0


La exactitud de `romberg` se controla con las variables globales 
`rombergabs` y `rombergtol`. La función `romberg`
termina con éxito su cálculo cuando la diferencia absoluta entre
sucesivas aproximaciones es menor que `rombergabs`,
o cuando la diferencia relativa de sucesivas aproximaciones es menor que
`rombergtol`. Así, cuando `rombergabs` vale 0.0
(su valor por defecto) sólo tiene efecto el test del error relativo basado
en `romberg`.


Véanse también `rombergit` y `rombergmin`.

<!-- category: Calculus -->
<!-- keywords: rombergit -->
<!-- signatures: rombergit -->
### Variable: rombergit

Valor por defecto: 11


La función `romberg` reduce a mitades sucesivas la amplitud del paso un máximo de
`rombergit` veces antes de abandonar el cómputo; el número máximo de 
evaluaciones del integrando es, por consiguiente, igual a `2^rombergit`.
La función `romberg` hace siempre al menos `rombergmin`
iteraciones; se trata de una heurística para evitar
la finalización prematura cuando el integrando oscila mucho.



Véanse también `rombergabs` y `rombergtol`.

<!-- category: Calculus -->
<!-- keywords: rombergmin -->
<!-- signatures: rombergmin -->
### Variable: rombergmin

Valor por defecto: 0


La función `romberg` hace siempre al menos `rombergmin`
iteraciones; se trata de una heurística para evitar
la finalización prematura cuando el integrando oscila mucho.


Véanse también `rombergit`, `rombergabs` y `rombergtol`.

<!-- category: Calculus -->
<!-- keywords: rombergtol -->
<!-- signatures: rombergtol -->
### Variable: rombergtol

Valor por defecto: 1e-4


La exactitud de `romberg` se controla con las variables globales 
`rombergabs` y `rombergtol`. La función `romberg`
termina con éxito su cálculo cuando la diferencia absoluta entre
sucesivas aproximaciones es menor que `rombergabs`,
o cuando la diferencia relativa de sucesivas aproximaciones es menor que
`rombergtol`. Así, cuando `rombergabs` vale 0.0
(su valor por defecto) sólo tiene efecto el test del error relativo basado
en `romberg`.


Véanse también `rombergit` y `rombergmin`.

