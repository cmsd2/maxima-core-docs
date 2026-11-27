## drawdf

<!-- category: Plotting -->
<!-- keywords: drawdf -->
<!-- signatures: drawdf(dydx, ...optionsandobjects...), drawdf(dvdu, [u, v], ...opcionesyobjetos...), drawdf(dvdu, [u, umin, umax], [v, vmin, vmax], ...opcionesyobjetos...), drawdf([dxdt, dydt], ...opcionesyobjetos...), drawdf([dudt, dvdt], [u, v], ...opcionesyobjetos...), drawdf([dudt, dvdt], [u, umin, umax], [v, vmin, vmax], ...opcionesyobjetos...) -->
### Function: drawdf (dydx, ...optionsandobjects...)

La función `drawdf` dibuja un campo de direcciones 2D, incluyendo
opcionalmente curvas asociadas a soluciones particulares, así
como otros objeto gráficos del paquete `draw`.


El primer argumento especifica la(s) derivada(s), el cual debe estar
formado por una expresión o una lista de dos expresiones. *dydx*, *dxdt* y
*dydt* son expresiones que dependen de *x* y *y*.
*dvdu*, *dudt* y *dvdt* son expresiones que dependen de
*u* y *v*.


Si las variables independiente y dependiente no son *x* e *y*,
sus nombres deben especificarse a continuación de las derivadas,
bien como una lista de dos nombres,
`[`*u*,*v*`]`, o como dos listas de la forma
`[`*u*,*umin*,*umax*`]` y
`[`*v*,*vmin*,*vmax*`]`.


El resto de argumentos son *opciones gráficas*, *objetos gráficos*,
o listas conteniendo elementos de ambos tipos. El conjunto de opciones y
objetos gráficos soportados por `drawdf` incluye los soportados
por `draw2d` y `gr2d` del paquete `draw`.


Los argumentos se iterpretan secuencialmente: las *opciones gráficas*
afectan a todos los *objetos gráficos* que le siguen. Además,
los *objetos gráficos* se dibujan en el orden en el que se
especifican, pudiendo tapar otros gráficos dibujados con anterioridad.
Algunas *opciones gráficas* afectan al aspecto general de la escena.


Los nuevos *objetos gráficos* que se definen en `drawdf` son:
`solns_at`, `points_at`, `saddles_at`, `soln_at`,
`point_at` y `saddle_at`.


Las nuevas *opciones gráficas* que se definen en `drawdf` son:
`field_degree`, `soln_arrows`, `field_arrows`,
`field_grid`, `field_color`, `show_field`,
`tstep`, `nsteps`, `duration`, `direction`,
`field_tstep`, `field_nsteps` y `field_duration`.


*Objetos gráficos* que se heredan del paquete `draw` incluyen:
`explicit`, `implicit`, `parametric`,
`polygon`, `points`, `vector`, `label` y cualesquiera
otros soportados por `draw2d` y `gr2d`.


*Opciones gráficas* que se heredan del paquete `draw` incluyen:
`points_joined`, `color`,
`point_type`, `point_size`, `line_width`,
`line_type`, `key`, `title`, `xlabel`,
`ylabel`, `user_preamble`, `terminal`,
`dimensions`, `file_name` y cualesquiera
otros soportados por `draw2d` y `gr2d`.


Véase también `draw2d`. 


Los usuarios de wxMaxima y Imaxima pueden hacer uso también `wxdrawdf`,
que es idéntica a `drawdf`, pero que inserta el gráfico en el 
propio documento utilizando la función `wxdraw`.


Para hacer uso de esta función, ejecútese primero `load("drawdf")`.


Ejemplos:



```maxima
(%i1) load("drawdf")$
(%i2) drawdf(exp(-x)+y)$        /* default vars: x,y */
(%i3) drawdf(exp(-t)+y, [t,y])$ /* default range: [-10,10] */
(%i4) drawdf([y,-9*sin(x)-y/5], [x,1,5], [y,-2,2])$
```


A efectos de compatibilidad, `drawdf` acepta la mayor
parte de parámetros soportados por `plotdf`.



```maxima
(%i5) drawdf(2*cos(t)-1+y, [t,y], [t,-5,10], [y,-4,9],
             [trajectory_at,0,0])$
```


`soln_at` y `solns_at` dibujan soluciones particulares
que pasen por los puntos especificados, utilizando el integrador
numérico de Runge Kutta de cuarto orden.



```maxima
(%i6) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             solns_at([0,0.1],[0,-0.1]),
             color=blue, soln_at(0,0))$
```


`field_degree=2` hace que el campo se componga de *splines*
cuadráticos basados en las derivadas de primer y segundo orden en
cada punto de la malla. 
`field_grid=[`*COLS*,*ROWS*`]` 
especifica el número de columnas y filas a utilizar en la malla.



```maxima
(%i7) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             field_degree=2, field_grid=[20,15],
             solns_at([0,0.1],[0,-0.1]),
             color=blue, soln_at(0,0))$
```


`soln_arrows=true` añade flechas a las soluciones particulares y,
por defecto, las borra. También cambia los colores por defecto para 
destacar las curvas de las soluciones particulares.



```maxima
(%i8) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             soln_arrows=true,
             solns_at([0,0.1],[0,-0.1],[0,0]))$
```


`duration=40` especifica el intervalo temporal de la integración
numérica, cuyo valor por defecto es 10. La integración se detendrá
automáticamente si la solución se aparta mucho de la región a dibujar,
o si la derivada se vuelve compleja o infinita. Aquí también
hacemos `field_degree=2` para dibujar *splines* cuadráticos. Las
ecuaciones de este ejemplo modelizan un sistema depredador-presa.



```maxima
(%i9) drawdf([x*(1-x-y), y*(3/4-y-x/2)], [x,0,1.1], [y,0,1],
             field_degree=2, duration=40,
             soln_arrows=true, point_at(1/2,1/2),
             solns_at([0.1,0.2], [0.2,0.1], [1,0.8], [0.8,1],
                      [0.1,0.1], [0.6,0.05], [0.05,0.4],
                      [1,0.01], [0.01,0.75]))$
```


`field_degree='solns` hace que el campo se componga de muchas
pequeñas soluciones calculadas a partir del Runge Kutta
de cuarto orden.



```maxima
(%i10) drawdf([x*(1-x-y), y*(3/4-y-x/2)], [x,0,1.1], [y,0,1],
              field_degree='solns, duration=40,
              soln_arrows=true, point_at(1/2,1/2),
              solns_at([0.1,0.2], [0.2,0.1], [1,0.8],
                       [0.8,1], [0.1,0.1], [0.6,0.05],
                       [0.05,0.4], [1,0.01], [0.01,0.75]))$
```


`saddles_at` trata de linearizar automáticamente la ecuación
en cada punto de silla y dibujar la solución numérica correspondiente
a cada vector propio, incluyendo las separatrices. `tstep=0.05` establece
el salto temporal máximo para el integrador numérico, cuyo valor por
defecto es 0.1. Las siguientes ecuaciones modelizan un péndulo amortiguado.



```maxima
(%i11) drawdf([y,-9*sin(x)-y/5], tstep=0.05,
              soln_arrows=true, point_size=0.5,
              points_at([0,0], [2*%pi,0], [-2*%pi,0]),
              field_degree='solns,
              saddles_at([%pi,0], [-%pi,0]))$
```


`show_field=false` elimina el campo completamente.



```maxima
(%i12) drawdf([y,-9*sin(x)-y/5], tstep=0.05,
              show_field=false, soln_arrows=true,
              point_size=0.5,
              points_at([0,0], [2*%pi,0], [-2*%pi,0]),
              saddles_at([3*%pi,0], [-3*%pi,0],
                         [%pi,0], [-%pi,0]))$
```


`drawdf` pasa todos los parámetros que no reconoce a `draw2d`
o `gr2d`, permitiendo combinar la potencia del paquete `draw`
con `drawdf`.



```maxima
(%i13) drawdf(x^2+y^2, [x,-2,2], [y,-2,2], field_color=gray,
              key="soln 1", color=black, soln_at(0,0),
              key="soln 2", color=red, soln_at(0,1),
              key="isocline", color=green, line_width=2,
              nticks=100, parametric(cos(t),sin(t),t,0,2*%pi))$
```


`drawdf` acepta listas anidadas de opciones y objetos gráficos,
permitiendo el uso de `makelist` y otras funciones de forma más
flexible para generar gráficos.



```maxima
(%i14) colors : ['red,'blue,'purple,'orange,'green]$
(%i15) drawdf([x-x*y/2, (x*y - 3*y)/4],
              [x,2.5,3.5], [y,1.5,2.5],
              field_color = gray,
              makelist([ key   = concat("soln",k),
                         color = colors[k],
                         soln_at(3, 2 + k/20) ],
                       k,1,5))$
```

