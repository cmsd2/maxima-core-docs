## Ecuaciones Diferenciales

<!-- category: Other -->
<!-- keywords: bc2 -->
<!-- signatures: bc2(soluc, xval1, yval1, xval2, yval2) -->
### Function: bc2 (soluc, xval1, yval1, xval2, yval2)

Resuelve el problema del valor en la frontera para ecuaciones diferenciales de segundo orden. 
Aquí, *soluc* es una solución general de la ecuación, como las que calcula `ode2`, *xval1* especifica el valor de la variable independiente en el primer punto mediante una expresión de la forma `x = x0`, mientras que *yval1* hace lo propio para la variable dependiente.  Las expresiones *xval2* y *yval2* dan los valores de estas mismas variables en un segundo punto, utilizando el mismo formato.

<!-- category: Other -->
<!-- keywords: desolve -->
<!-- signatures: desolve(ecu, x), desolve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: desolve (ecu, x)

La función `desolve` resuelve sistemas de ecuaciones diferenciales ordinarias lineales utilizando la transformada de Laplace.  Aquí las *eqi* (`i`=1,..,n) son ecuaciones diferenciales con variables dependientes *x_1*, ..., *x_n*. La dependencia funcional de *x_1*, ..., *x_n* respecto de una variable independiente, por ejemplo *x*, debe indicarse explícitamente, tanto en las variables como en las derivadas. Por ejemplo, 




```maxima
eqn_1: 'diff(f,x,2) = sin(x) + 'diff(g,x);
eqn_2: 'diff(f,x) + x^2 - f = 2*'diff(g,x,2);
```


no es el formato apropiado. El método correcto es



```maxima
eqn_1: 'diff(f(x),x,2) = sin(x) + 'diff(g(x),x);
eqn_2: 'diff(f(x),x) + x^2 - f(x) = 2*'diff(g(x),x,2);
```


La llamada a la función `desolve` sería entonces


```maxima
desolve([eqn_1, eqn_2], [f(x),g(x)]);
```


Si las condiciones iniciales en `x=0` son conocidas, deben ser suministradas antes de llamar a `desolve` haciendo uso previo de la función `atvalue`,











```maxima
(%i1) 'diff(f(x),x)='diff(g(x),x)+sin(x);
                 d           d
(%o1)            -- (f(x)) = -- (g(x)) + sin(x)
                 dx          dx
(%i2) 'diff(g(x),x,2)='diff(f(x),x)-cos(x);
                  2
                 d            d
(%o2)            --- (g(x)) = -- (f(x)) - cos(x)
                   2          dx
                 dx
(%i3) atvalue('diff(g(x),x),x=0,a);
(%o3)                           a
(%i4) atvalue(f(x),x=0,1);
(%o4)                           1
(%i5) desolve([%o1,%o2],[f(x),g(x)]);
                  x
(%o5) [f(x) = a %e  - a + 1, g(x) = 

                                                x
                                   cos(x) + a %e  - a + g(0) - 1]
(%i6) [%o1,%o2],%o5,diff;
             x       x      x                x
(%o6)   [a %e  = a %e , a %e  - cos(x) = a %e  - cos(x)]
```


Si `desolve` no encuentra una solución, entonces devuelve `false`.

<!-- category: Other -->
<!-- keywords: ic1 -->
<!-- signatures: ic1(soluc, xval, yval) -->
### Function: ic1 (soluc, xval, yval)

Resuelve el problema del valor inicial en ecuaciones diferenciales de primer orden. 
Aquí, *soluc* es una solución general de la ecuación, como las que calcula `ode2`, *xval* es una ecuación de la forma `x = x0` para la variable independiente y *yval* es una ecuación de la forma `y = y0` para la variable dependiente. Véase `ode2` para un ejemplo sobre su utilización.

<!-- category: Other -->
<!-- keywords: ic2 -->
<!-- signatures: ic2(soluc, xval, yval, dval) -->
### Function: ic2 (soluc, xval, yval, dval)

Resuelve el problema del valor inicial en ecuaciones diferenciales de segundo orden.
Aquí, *soluc* es una solución general de la ecuación, como las que calcula `ode2`, *xval* es una ecuación de la forma `x = x0` para la variable independiente y *yval* es una ecuación de la forma `y = y0` para la variable dependiente, siendo *dval* una expresión de la forma `diff(y,x) = dy0` que especifica la primera derivada de la variable dependiente respecto de la independiente en el punto *xval*.


Véase `ode2` para un ejemplo de su uso.

<!-- category: Other -->
<!-- keywords: ode2 -->
<!-- signatures: ode2(ecu, dvar, ivar) -->
### Function: ode2 (ecu, dvar, ivar)

La función `ode2` resuelve ecuaciones diferenciales ordinarias de primer y segundo orden. Admite tres argumentos: 
una ecuación diferencial ordinaria *ecu*, la variable dependiente *dvar* y la variable independiente *ivar*.  Si ha tenido éxito en la resolución de la ecuación, devuelve una solución, explícita o implícita, para la variable dependiente. El símbolo `%c` se utiliza para representar la constante en el caso de ecuaciones de primer orden y los símbolos `%k1` y `%k2` son las constantes de las ecuaciones de segundo orden. Si por cualquier razón `ode2` no puede calcular la solución, devolverá `false`, acompañado quizás de un mensaje de error. Los métodos utilizados para las ecuaciones de primer orden, en el orden en que se hace la tentativa de resolución son: lineal, separable, exacto (pudiendo solicitar en este caso un factor de integración), homogéneo, ecuación de Bernoulli y un método homogéneo generalizado. Para las ecuaciones de segundo orden: coeficiente constante, exacto, homogéneo lineal con coeficientes no constantes  que pueden ser transformados en coeficientes constantes, ecuación equidimensional o de Euler, método de variación de parámetros y ecuaciones exentas de las variables dependientes o independientes de manera que se puedan reducir a dos ecuaciones lineales de primer a ser resueltas secuencialmente. Durante el proceso de resolución de ecuaciones diferenciales ordinarias, ciertas variables se utilizan con el único propósito de suministrar información al usuario: `method` almacena el método utilizado para encontrar la solución (como por ejemplo `linear`), `intfactor` para el factor de integración que se haya podido utilizar, `odeindex` para el índice del método de Bernoulli o el homogéneo generalizado y `yp` para la solución particular del método de variación de parámetros.


A fin de resolver problemas con valores iniciales y problemas con valores en la frontera, la función `ic1` está disponible para ecuaciones de primer orden y las funciones `ic2` y `bc2` para problemas de valores iniciales y de frontera, respectivamente, en el caso de las ecuaciones de segundo orden.


Ejemplo:



```maxima
(%i1) x^2*'diff(y,x) + 3*y*x = sin(x)/x;
                      2 dy           sin(x)
(%o1)                x  -- + 3 x y = ------
                        dx             x
(%i2) ode2(%,y,x);
                             %c - cos(x)
(%o2)                    y = -----------
                                  3
                                 x
(%i3) ic1(%o2,x=%pi,y=0);
                              cos(x) + 1
(%o3)                   y = - ----------
                                   3
                                  x
(%i4) 'diff(y,x,2) + y*'diff(y,x)^3 = 0;
                         2
                        d y      dy 3
(%o4)                   --- + y (--)  = 0
                          2      dx
                        dx
(%i5) ode2(%,y,x);
                      3
                     y  + 6 %k1 y
(%o5)                ------------ = x + %k2
                          6
(%i6) ratsimp(ic2(%o5,x=0,y=0,'diff(y,x)=2));
                             3
                          2 y  - 3 y
(%o6)                   - ---------- = x
                              6
(%i7) bc2(%o5,x=0,y=1,x=1,y=3);
                         3
                        y  - 10 y       3
(%o7)                   --------- = x - -
                            6           2
```

