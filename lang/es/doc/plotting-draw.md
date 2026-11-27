## draw

<!-- category: Plotting -->
<!-- keywords: allocation -->
<!-- signatures: allocation -->
### Variable: allocation

Valor por defecto: `false`


Con la opción `allocation` es posible colocar a voluntad una escena en la
ventana de salida, lo cual resulta de utilidad en el caso de gráficos 
múltiples. Cuando la opción toma el valor `false`, la escena se coloca
de forma automática, dependiendo del valor asignado a la opción `columns`.
En cualquier otro caso, a `allocation` se le debe asignar una lista con dos
pares de números; el primero se corresponde con la posición de la esquina
inferior izquierda del gráfico y el segundo par hace referencia al ancho y alto
de la escena. Todas las cantidades deben darse en coordenadas relativas, entre
0 y 1.


Ejemplos:


Gráficos internos.



```maxima
(%i1) load("draw")$
(%i2) draw(
        gr2d(
          explicit(x^2,x,-1,1)),
        gr2d(
          allocation = [[1/4, 1/4],[1/2, 1/2]],
          explicit(x^3,x,-1,1),
          grid = true) ) $
```


Multiplot con dimensiones establecidas por el usuario.



```maxima
(%i1) load("draw")$
(%i2) draw(
        terminal = wxt,
        gr2d(
          allocation = [[0, 0],[1, 1/4]],
          explicit(x^2,x,-1,1)),
        gr3d(
          allocation = [[0, 1/4],[1, 3/4]],
          explicit(x^2+y^2,x,-1,1,y,-1,1) ))$
```


Véase también la opción `columns`.

<!-- category: Plotting -->
<!-- keywords: axis_3d -->
<!-- signatures: axis_3d -->
### Variable: axis_3d

Valor por defecto: `true`


Cuando `axis_3d` vale `true`, los ejes *x*, *y* y *z*
permanecen visibles en las escenas 3d.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(axis_3d = false,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```


Véanse también `axis_bottom`,  `axis_left`, `axis_top` y `axis_right` for axis in 2d.

<!-- category: Plotting -->
<!-- keywords: axis_bottom -->
<!-- signatures: axis_bottom -->
### Variable: axis_bottom

Valor por defecto: `true`


Cuando `axis_bottom` vale `true`, el eje inferior permanece visible en las escenas 2d.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_bottom = false,
             explicit(x^3,x,-1,1))$
```


Véanse también `axis_left`,  `axis_top`, `axis_right` y `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: axis_left -->
<!-- signatures: axis_left -->
### Variable: axis_left

Valor por defecto: `true`


Cuando `axis_left` vale `true`, el eje izquierdo permanece visible en las escenas 2d.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_left = false,
             explicit(x^3,x,-1,1))$
```


Véanse también `axis_bottom`,  `axis_top`, `axis_right` y `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: axis_right -->
<!-- signatures: axis_right -->
### Variable: axis_right

Valor por defecto: `true`


Cuando `axis_right` vale `true`, el eje derecho permanece visible en las escenas 2d.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_right = false,
             explicit(x^3,x,-1,1))$
```


Véanse también `axis_bottom`,  `axis_left`, `axis_top` y `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: axis_top -->
<!-- signatures: axis_top -->
### Variable: axis_top

Valor por defecto: `true`


Cuando `axis_top` vale `true`, el eje superior permanece visible en las escenas 2d.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_top = false,
             explicit(x^3,x,-1,1))$
```


Véanse también `axis_bottom`,  `axis_left`, `axis_right` y `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: background_color -->
<!-- signatures: background_color -->
### Variable: background_color

Valor por defecto: `white`


Establece el color de fondo en los terminales `gif`, `png`, `jpg`
y `gif`. El color de fondo por defecto es blanco.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Esta opción no es compatible con los terminales `epslatex` y `epslatex_standalone`.


Véase también `color`.

<!-- category: Plotting -->
<!-- keywords: bars -->
<!-- signatures: bars([x1, h1, w1], [x2, h2, w2, ...]) -->
### Function: bars ([x1, h1, w1], [x2, h2, w2, ...])

Dibuja barras verticales en 2D.


**2D**


`bars ([x1,h1,w1], [x2,h2,w2, ...])` 
dibuja barras centradas en los valores *x1*, *x2*, ... de alturas *h1*, *h2*, ...
y anchos *w1*, *w2*, ...


Este objeto se ve afectado por las siguientes *opciones gráficas*: `key`, 
`fill_color`, `fill_density` y `line_width`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
       key          = "Grupo A",
       fill_color   = blue,
       fill_density = 0.2,
       bars([0.8,5,0.4],[1.8,7,0.4],[2.8,-4,0.4]),
       key          = "Grupo B",
       fill_color   = red,
       fill_density = 0.6,
       line_width   = 4,
       bars([1.2,4,0.4],[2.2,-2,0.4],[3.2,5,0.4]),
       xaxis = true);
```

<!-- category: Plotting -->
<!-- keywords: border -->
<!-- signatures: border -->
### Variable: border

Valor por defecto: `true`


Cuando `border` vale `true`, los bordes de los
polígonos se dibujan de acuerdo con `line_type` y
`line_width`.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `polygon`, `rectangle` y `ellipse`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(color       = brown,
             line_width  = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: boundaries_array -->
<!-- signatures: boundaries_array -->
### Variable: boundaries_array

Valor por defecto: `false`


`boundaries_array` es donde el objeto gráfico `geomap` lee
las coordenadas de las líneas fronterizas.


Cada componente de `boundaries_array` es un array de números decimales
en coma flotante representando las coordenadas que definen un segmento
poligonal o línea fronteriza.


Véase también `geomap`.

<!-- category: Plotting -->
<!-- keywords: capping -->
<!-- signatures: capping -->
### Variable: capping

Valor por defecto: `[false, false]`


Una lista de dos elementos, `true` y `false`,
indicando si los extremos de un objeto gráfico `tube`
permanece abiertos o si deben ser cerrados. Por defecto, ambos
extremos se dejan abiertos.


La asignación `capping = false` equivale a `capping = [false, false]`
y `capping = true` equivale a `capping = [true, true]`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        capping = [false, true],
        tube(0, 0, a, 1,
             a, 0, 8) )$
```

<!-- category: Plotting -->
<!-- keywords: cbrange -->
<!-- signatures: cbrange -->
### Variable: cbrange

Valor por defecto: `auto`


Cuando `cbrange` vale `auto`, el rango de los valores que se
colorean cuando `enhanced3d` es diferente de `false` se calcula
automáticamente. Valores fuera del rango utilizan el color del valor
extremo más cercano.


Cuando `enhanced3d` o `colorbox` vale `false`, la 
opción `cbrange` no tiene efecto alguno.


Si el usuario quiere especificar un intervalo para los valores a colorear,
éste debe expresarse como una lista de Maxima, como en `cbrange=[-2, 3]`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d (
        enhanced3d     = true,
        color          = green,
        cbrange = [-3,10],
        explicit(x^2+y^2, x,-2,2,y,-2,2)) $
```


Véanse también `enhanced3d` y `cbtics`.

<!-- category: Plotting -->
<!-- keywords: cbtics -->
<!-- signatures: cbtics -->
### Variable: cbtics

Valor por defecto: `auto`


Esta opción gráfica controla la forma en la que se dibujarán
las marcas en la escala de color cuando la opción `enhanced3d`
sea diferente de `false`.


Cuando `enhanced3d` o `colorbox` vale `false`, la 
opción `cbtics` no tiene efecto alguno.


Véase `xtics` para una descripción completa.


Ejemplo :



```maxima
(%i1) load("draw")$
(%i2) draw3d (
        enhanced3d = true,
        color      = green,
        cbtics  = {["High",10],["Medium",05],["Low",0]},
        cbrange = [0, 10],
        explicit(x^2+y^2, x,-2,2,y,-2,2)) $
```


See also `enhanced3d`, `colorbox` and `cbrange`.

<!-- category: Plotting -->
<!-- keywords: columns -->
<!-- signatures: columns -->
### Variable: columns

Valor por defecto: 1


`columns` es el número de columnas en gráficos múltiples.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) scene1: gr2d(title="Ellipse",
                   nticks=30,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i3) scene2: gr2d(title="Triangle",
                   polygon([4,5,7],[6,4,2]))$
(%i4) draw(scene1, scene2, columns = 2)$
```

<!-- category: Plotting -->
<!-- keywords: contour -->
<!-- signatures: contour -->
### Variable: contour

Valor por defecto: `none`


La opción `contour` permite al usuario decidir dónde colocar
las líneas de nivel.
Valores posibles son:



- *
`none`:
no se dibujan líneas de nivel.
- *
`base`:
las líneas de nivel se proyectan sobre el plano xy.
- *
`surface`:
las líneas de nivel se dibujan sobre la propia superficie.
- *
`both`:
se dibujan dos conjuntos de líneas de nivel: sobre
la superficie y las que se proyectan sobre el plano xy.
- *
`map`:
las líneas de nivel se proyectan sobre el plano xy
y el punto de vista del observador se coloca perpendicularmente a él.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 15,
             contour        = both,
             surface_hide   = true) $
```


Véase también `contour_levels`.

<!-- category: Plotting -->
<!-- keywords: contour_levels -->
<!-- signatures: contour_levels -->
### Variable: contour_levels

Valor por defecto: 5


Esta opción gráfica controla cómo se dibujarán las líneas
de nivel. A `contour_levels` se le puede asignar un número entero
positivo, una lista de tres números o un conjunto numérico arbitrario:



- *
Si a `contour_levels` se le asigna un entero positivo *n*,
entonces se dibujarán *n* líneas de nivel a intervalos
iguales. Por defecto, se dibujaán cinco isolíneas.
- *
Si a `contour_levels` se le asigna una lista de tres números de la
forma `[inf,p,sup]`, las isolíneas se dibujarán
desde `inf` hasta `sup` en pasos de amplitud `p`.
- *
Si a `contour_levels` se le asigna un conjunto de números de la
forma `{n1, n2, ...}`, entonces se dibujarán las
isolíneas correspondientes a los niveles `n1`,
`n2`, ...


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. 


Ejemplos:


Diez isolíneas igualmente espaciadas. El número
real puede ajustarse a fin de poder conseguir etiquetas más
sencillas.


```maxima
(%i1) load("draw")$
(%i2) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 10,
             contour        = both,
             surface_hide   = true) $
```



Desde -8 hasta 8 en pasos de amplitud 4.


```maxima
(%i1) load("draw")$
(%i2) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = [-8,4,8],
             contour        = both,
             surface_hide   = true) $
```


Líneas correspondientes a los niveles -7, -6, 0.8 y 5.


```maxima
(%i1) load("draw")$
(%i2) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = {-7, -6, 0.8, 5},
             contour        = both,
             surface_hide   = true) $
```


Véase también `contour`.

<!-- category: Plotting -->
<!-- keywords: cylindrical -->
<!-- signatures: cylindrical(radius, z, minz, maxz, azi, minazi, maxazi) -->
### Function: cylindrical (radius, z, minz, maxz, azi, minazi, maxazi)

Dibuja funciones 3D definidas en coordenadas cilíndricas.


**3D**


`cylindrical (radius,z,minz,maxz,azi,minazi,maxazi)`
dibuja la función `radius(z,azi)` definida en coordenadas cilíndricas, con la variable
*z* tomando valores desde *minz* hasta *maxz* y el *azimut* *azi* tomando valores desde
*minazi* hasta *maxazi*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `xu_grid`, 
`yv_grid`, `line_type`, `key`, `wired_surface`, `enhanced3d` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(cylindrical(1,z,-2,2,az,0,2*%pi))$
```

<!-- category: Plotting -->
<!-- keywords: data_file_name -->
<!-- signatures: data_file_name -->
### Variable: data_file_name

Valor por defecto: `"data.gnuplot"`


`data_file_name` es el nombre del fichero que almacena
la información numérica que necesita Gnuplot para crear
el gráfico solicitado.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


Véase ejemplo en `gnuplot_file_name`.

<!-- category: Plotting -->
<!-- keywords: delay -->
<!-- signatures: delay -->
### Variable: delay

Valor por defecto: 5


Este es el retraso en centésimas de segundo entre imágenes
en los ficheros gif animados.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


La opciób `delay` sólo se activa en caso de gifs animados; se ignora en
cualquier otro caso.


Véanse también `terminal`, `dimensions`.

<!-- category: Plotting -->
<!-- keywords: dimensions -->
<!-- signatures: dimensions -->
### Variable: dimensions

Valor por defecto: `[600,500]`


Dimensiones del terminal de salida. Su valor es una lista formada
por el ancho y el alto. El significado de estos dos números
depende del terminal con el que se esté trabajando.


Con los terminales `gif`, `animated_gif`, `png`, `jpg`,
`svg`, `screen`, `wxt` y `aquaterm`, los enteros
representan números de puntos en cada dirección. Si no son enteros
se redondean.


Con los terminales `eps`, `eps_color`, `pdf` y
`pdfcairo`, los números representan centésimas de cm,
lo que significa que, por defecto, las imágenes en estos
formatos tienen 6 cm de ancho por 5 cm de alto.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


Ejemplos:


La opción `dimensions` aplicada a un fichero de salida y al
lienzo wxt.



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        dimensions = [300,300],
        terminal   = 'png,
        explicit(x^4,x,-1,1)) $
(%i3) draw2d(
        dimensions = [300,300],
        terminal   = 'wxt,
        explicit(x^4,x,-1,1)) $
```


La opción `dimensions` aplicada a una salida eps.
En este caso queremos un fichero eps con dimensiones A4.



```maxima
(%i1) load("draw")$
(%i2) A4portrait: 100*[21, 29.7]$
(%i3) draw3d(
        dimensions = A4portrait,
        terminal   = 'eps,
        explicit(x^2-y^2,x,-2,2,y,-2,2)) $
```

<!-- category: Plotting -->
<!-- keywords: draw -->
<!-- signatures: draw(gr2d, ..., gr3d, ..., options, ...) -->
### Function: draw (gr2d, ..., gr3d, ..., options, ...)

Representa gráficamente una serie de escenas; sus argumentos son objetos
`gr2d` y/o `gr3d`, junto con algunas opciones, o listas de escenas y opciones.
Por defecto, las escenas se representan en una columna.


La función `draw` acepta las siguientes opciones globales: `terminal`,
`columns`, `dimensions`, `file_name` y `delay`.


Las funciones `draw2d` y `draw3d` son atajos a utilizar
cuando se quiere representar una única escena en dos o tres
dimensiones, respectivamente.


Véanse también `gr2d` y `gr3d`.


Para utilizar esta función, ejecútese primero `load("draw")`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) scene1: gr2d(title="Ellipse",
                   nticks=30,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i3) scene2: gr2d(title="Triangle",
                   polygon([4,5,7],[6,4,2]))$
(%i4) draw(scene1, scene2, columns = 2)$
```


Las dos sentencias gráficas siguientes son equivalentes:


```maxima
(%i1) load("draw")$
(%i2) draw(gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1)));
(%o2)                          [gr3d(explicit)]
(%i3) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1));
(%o3)                          [gr3d(explicit)]
```


Un fichero gif animado:


```maxima
(%i1) load("draw")$
(%i2) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


Véanse también `gr2d`, `gr3d`, `draw2d` y `draw3d`.

<!-- category: Plotting -->
<!-- keywords: draw2d -->
<!-- signatures: draw2d(option, graphic_object, ...) -->
### Function: draw2d (option, graphic_object, ...)

Esta función es un atajo para
`draw(gr2d(options, ..., graphic_object, ...))`.


Puede utilizarse para representar una única escena en 2d.


Para utilizar esta función, ejecútese primero `load("draw")`.


Véanse también `draw` y `gr2d`.

<!-- category: Plotting -->
<!-- keywords: draw3d -->
<!-- signatures: draw3d(option, graphic_object, ...) -->
### Function: draw3d (option, graphic_object, ...)

Esta función es un atajo para
`draw(gr3d(options, ..., graphic_object, ...))`.


Puede utilizarse para representar una única escena en 3d.


Para utilizar esta función, ejecútese primero `load("draw")`.


Véanse también `draw` y `gr3d`.

<!-- category: Plotting -->
<!-- keywords: draw_file -->
<!-- signatures: draw_file(Opción gráfica, ..., Opción gráfica, ...) -->
### Function: draw_file (Opción gráfica, ..., Opción gráfica, ...)

Almacena el gráfico actual en un fichero. Las opciones gráficas que
acepta son: `terminal`, `dimensions` y`file_name`. 


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) /* dibujo en pantalla */
      draw(gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1)))$
(%i3) /* same plot in eps format */
      draw_file(terminal  = eps,
                dimensions = [5,5]) $
```

<!-- category: Plotting -->
<!-- keywords: draw_realpart -->
<!-- signatures: draw_realpart -->
### Variable: draw_realpart

Valor por defecto: `true`


Cuando vale `true`, las funciones a dibujar se consideran funciones complejas cuyas
partes reales se deben dibujar; cuando la opción vale `false`, no se dibujará
nada en caso de que la función no devuelve valores reales.


Esta opción afecta a los objetos `explicit` y `parametric` en 2D y 3D, y al
objeto `parametric_surface`.


Ejemplo:


La opción `draw_realpart` afecta a los objetos `explicit` y `parametric`.



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        draw_realpart = false,
        explicit(sqrt(x^2  - 4*x) - x, x, -1, 5),
        color         = red,
        draw_realpart = true,
        parametric(x,sqrt(x^2  - 4*x) - x + 1, x, -1, 5) );
```

<!-- category: Plotting -->
<!-- keywords: elevation_grid -->
<!-- signatures: elevation_grid(mat, x0, y0, width, height) -->
### Function: elevation_grid (mat, x0, y0, width, height)

Dibuja la matriz *mat* en 3D. Los valores *z* se toman de *mat*,
las abscisas van desde *x0* hasta $x0 + width$
y las ordenadas desde *y0* hasta $y0 + height$. El elemento $a(1,1)$
se proyecta sobre el punto $(x0,y0+height)$, $a(1,n)$ sobre $(x0+width,y0+height)$,
$a(m,1)$ sobre $(x0,y0)$ y $a(m,n)$ sobre $(x0+width,y0)$.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `line_type`,
`line_width`, `key`, `wired_surface`, `enhanced3d` y `color`.


En versiones antiguas de Maxima, `elevation_grid` se llamaba `mesh`.
Véase también `mesh`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) m: apply(
            matrix,
            makelist(makelist(random(10.0),k,1,30),i,1,20)) $
(%i3) draw3d(
         color = blue,
         elevation_grid(m,0,0,3,2),
         xlabel = "x",
         ylabel = "y",
         surface_hide = true);
```

<!-- category: Plotting -->
<!-- keywords: ellipse -->
<!-- signatures: ellipse(xc, yc, a, b, ang1, ang2) -->
### Function: ellipse (xc, yc, a, b, ang1, ang2)

Dibuja elipses y círculos en 2D.



**2D**


`ellipse (xc, yc, a, b, ang1, ang2)`
dibuja una elipse de centro `[xc, yc]` con semiejes horizontal y vertical
*a* y *b*, respectivamente, comenzando en el ángulo *ang1* y trazando un arco
de amplitud igual al ángulo *ang2*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `nticks`, 
`transparent`, `fill_color`, `border`, `line_width`, 
`line_type`, `key` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(transparent = false,
             fill_color  = red,
             color       = gray30,
             transparent = false,
             line_width  = 5,
             ellipse(0,6,3,2,270,-270),
             /* center (x,y), a, b, start & end in degrees */
             transparent = true,
             color       = blue,
             line_width  = 3,
             ellipse(2.5,6,2,3,30,-90),
             xrange      = [-3,6],
             yrange      = [2,9] )$
```

<!-- category: Plotting -->
<!-- keywords: enhanced3d -->
<!-- signatures: enhanced3d -->
### Variable: enhanced3d

Valor por defecto: `none`


Cuando `enhanced3d` vale `none`, las superficies no se colorean en escenas 3D.
Para obtener una superficie coloreada se debe asignar una lista a la opción
`enhanced3d`, en la que el primer elemento es una expresión y el resto
son los nombres de las variables o parámetros utilizados en la expresión.
Una lista tal como `[f(x,y,z), x, y, z]` significa que al punto 
`[x,y,z]` de la superficie se le asigna el número `f(x,y,z)`, el
cual será coloreado de acuerdo con el valor actual de `palette`.
Para aquellos objetos gráficos 3D definidos en términos de parámetros,
es posible definir el número de color en términos de dichos parámetros,
como en `[f(u), u]`, para los objetos `parametric` y `tube`,
o `[f(u,v), u, v]`, para el objeto `parametric_surface`.
Mientras que todos los objetos 3D admiten el modelo basado en coordenadas
absolutas, `[f(x,y,z), x, y, z]`, solamente dos de ellos, esto es
`explicit` y `elevation_grid`, aceptan también el modelo basado en las
coordenadas `[x,y]`, `[f(x,y), x, y]`. El objeto 3D `implicit`
acepta solamente el modelo `[f(x,y,z), x, y, z]`. El objeto `points` 
también acepta el modelo `[f(x,y,z), x, y, z]`, pero cuando los puntos
tienen naturaleza cronológica también admite el modelo `[f(k), k]`,
siendo `k` un parámetro de orden.


Cuando a `enhanced3d` se le asigna algo diferente de `none`, se ignoran
las opciones `color` y `surface_hide`.


Los nombres de las variables definidas en las listas pueden ser diferentes
de aquellas utilizadas en las definiciones de los objetos gráficos.


A fin de mantener compatibilidad con versiones anteriores, `enhanced3d = false` 
es equivalente a `enhanced3d = none` y `enhanced3d = true` es
equivalente a `enhanced3d = [z, x, y, z]`. Si a `enhanced3d` se le
asigna una expresión, sus variables deben ser las mismas utilizadas en la
definición de la superficie. Esto no es necesario cuando se utilizan listas.


Sobre la definición de paletas, véase `palette`.


Ejemplos:


Objeto `explicit` con coloreado definido por el modelo `[f(x,y,z), x, y, z]`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         enhanced3d = [x-z/10,x,y,z],
         palette    = gray,
         explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
```


Objeto `explicit` con coloreado definido por el modelo `[f(x,y), x, y]`.
Los nombres de las variables definidas en las listas pueden ser diferentes
de aquellas utilizadas en las definiciones de los objetos gráficos 3D; en este
caso, `r` corresponde a `x` y `s` a `y`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         enhanced3d = [sin(r*s),r,s],
         explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
```


Objeto `parametric` con coloreado definido por el modelo `[f(x,y,z), x, y, z]`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         nticks = 100,
         line_width = 2,
         enhanced3d = [if y>= 0 then 1 else 0, x, y, z],
         parametric(sin(u)^2,cos(u),u,u,0,4*%pi)) $
```


Objeto `parametric` con coloreado definido por el modelo `[f(u), u]`.
En este caso, `(u-1)^2` es una simplificación de `[(u-1)^2,u]`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         nticks = 60,
         line_width = 3,
         enhanced3d = (u-1)^2,
         parametric(cos(5*u)^2,sin(7*u),u-2,u,0,2))$
```


Objeto `elevation_grid` con coloreado definido por el modelo `[f(x,y), x, y]`.



```maxima
(%i1) load("draw")$
(%i2) m: apply(
           matrix,
           makelist(makelist(cos(i^2/80-k/30),k,1,30),i,1,20)) $
(%i3) draw3d(
         enhanced3d = [cos(x*y*10),x,y],
         elevation_grid(m,-1,-1,2,2),
         xlabel = "x",
         ylabel = "y");
```


Objeto `tube` con coloreado definido por el modelo `[f(x,y,z), x, y, z]`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         enhanced3d = [cos(x-y),x,y,z],
         palette = gray,
         xu_grid = 50,
         tube(cos(a), a, 0, 1, a, 0, 4*%pi) )$
```


Objeto `tube` con coloreado definido por el modelo `[f(u), u]`.
En este caso, `enhanced3d = -a` puede ser una simplificación de 
`enhanced3d = [-foo,foo]`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         capping = [true, false],
         palette = [26,15,-2],
         enhanced3d = [-foo, foo],
         tube(a, a, a^2, 1, a, -2, 2) )$
```


Objetos `implicit` y `points` con coloreado definido por el
modelo `[f(x,y,z), x, y, z]`.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         enhanced3d = [x-y,x,y,z],
         implicit((x^2+y^2+z^2-1)*(x^2+(y-1.5)^2+z^2-0.5)=0.015,
                  x,-1,1,y,-1.2,2.3,z,-1,1)) $
(%i3) m: makelist([random(1.0),random(1.0),random(1.0)],k,1,2000)$
(%i4) draw3d(
         point_type = filled_circle,
         point_size = 2,
         enhanced3d = [u+v-w,u,v,w],
         points(m) ) $
```


cuando los puntos tienen naturaleza cronológica también se admite
el modelo `[f(k), k]`, siendo `k` un parámetro de orden.



```maxima
(%i1) load("draw")$
(%i2) m:makelist([random(1.0), random(1.0), random(1.0)],k,1,5)$
(%i3) draw3d(
         enhanced3d = [sin(j), j],
         point_size = 3,
         point_type = filled_circle,
         points_joined = true,
         points(m)) $
```

<!-- category: Plotting -->
<!-- keywords: error_type -->
<!-- signatures: error_type -->
### Variable: error_type

Valor por defecto: `y`


Dependiendo de su valor, el cual puede ser `x`, `y` o `xy`,
el objeto gráfico `errors` dibujará puntos con barras de error horizontales,
verticales, o ambas. Si `error_type=boxes`, se dibujarán cajas en lugar de cruces.


Véase también `errors`.

<!-- category: Plotting -->
<!-- keywords: errors -->
<!-- signatures: errors([x1, x2, ...], [y1, y2, ...]) -->
### Function: errors ([x1, x2, ...], [y1, y2, ...])

Dibuja puntos con barras de error asociadas horizontales, verticales o de
ambos tipos, según sea el valor de la opción `error_type`.


**2D**


Si `error_type=x`, los argumentos a `errors` deben ser de la forma 
`[x,y,xdelta]` o `[x,y,xlow,xhigh]`. Si `error_type=y`, 
los argumentos deben ser del tipo `[x,y,ydelta]` o `[x,y,ylow,yhigh]`.
Si `error_type=xy` o `error_type=boxes`, los argumentos deben ser de la
forma `[x,y,xdelta,ydelta]` o `[x,y,xlow,xhigh,ylow,yhigh]`.


Véase también `error_type`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `error_type`, 
`points_joined`, `line_width`, `key`, `line_type`, 
`color`, `fill_density`, `xaxis_secondary` y `yaxis_secondary`.


La opción `fill_density` solo es relevante cuando `error_type=boxes`.


Ejemplos:


Barras de error horizontales.



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        error_type = y,
        errors([[1,2,1], [3,5,3], [10,3,1], [17,6,2]]))$
```


Barras de error horizontales y verticales.



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        error_type = xy,
        points_joined = true,
        color = blue,
        errors([[1,2,1,2], [3,5,2,1], [10,3,1,1], [17,6,1/2,2]]));
```

<!-- category: Plotting -->
<!-- keywords: explicit -->
<!-- signatures: explicit(fcn, var, minval, maxval), explicit(fcn, var1, minval1, maxval1, var2, minval2, maxval2) -->
### Function: explicit (fcn, var, minval, maxval)

Dibuja funciones explícitas en 2D y 3D.


**2D**


`explicit (fcn,var,minval,maxval)` dibuja la función explícita *fcn*,
con la variable *var* tomando valores desde *minval* hasta *maxval*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `nticks`, 
`adapt_depth`, `draw_realpart`, `line_width`, `line_type`, `key`, 
`filled_func`, `fill_color` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(line_width = 3,
             color      = blue,
             explicit(x^2,x,-3,3) )$
(%i3) draw2d(fill_color  = brown,
             filled_func = true,
             explicit(x^2,x,-3,3) )$
```


**3D**


`explicit (fcn,var1,minval1,maxval1,var2,minval2,maxval2)`
dibuja la función explícita *fcn*, con la variable 
`var1` tomando valores desde *minval1* hasta *maxval1* y 
la variable *var2* tomando valores desde *minval2* hasta *maxval2*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `draw_realpart`, `xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`
y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(key   = "Gauss",
             color = "#a02c00",
             explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
             yv_grid     = 10,
             color = blue,
             key   = "Plane",
             explicit(x+y,x,-5,5,y,-5,5),
             surface_hide = true)$
```


Véase también `filled_func` para el relleno de curvas.

<!-- category: Plotting -->
<!-- keywords: file_name -->
<!-- signatures: file_name -->
### Variable: file_name

Valor por defecto: `"maxima_out"`


`file_name` es el nombre del fichero en el que los terminales `png`,
`jpg`, `gif`, `eps`, `eps_color`, `pdf`, `pdfcairo`
y `svg` guardarán el gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'png)$
```


Véanse también `terminal`, `dimensions`.

<!-- category: Plotting -->
<!-- keywords: fill_color -->
<!-- signatures: fill_color -->
### Variable: fill_color

Valor por defecto: `"red"`


`fill_color` especifica el color para rellenar polígonos
y funciones explícitas bidimensionales.


Véase `color` para más información sobre cómo definir 
colores.

<!-- category: Plotting -->
<!-- keywords: fill_density -->
<!-- signatures: fill_density -->
### Variable: fill_density

Valor por defecto: 0


`fill_density` es un número entre 0 y 1 que especifica
la intensidad del color de relleno (dado por `fill_color`)
en los objetos `bars`.


Véase `bars` para ejemplos.

<!-- category: Plotting -->
<!-- keywords: filled_func -->
<!-- signatures: filled_func -->
### Variable: filled_func

Valor por defecto: `false`


La opción `filled_func` establece cómo se van a rellenar las regiones
limitadas por funciones. Si `filled_func` vale `true`, la
región limitada por la función definida en el objeto `explicit`
y el borde inferior del la ventana gráfica se rellena con `fill_color`.
Si `filled_func` guarda la expresión de una función, entonces la
región limitada por esta función y la definida en el objeto `explicit`
será la que se rellene. Por defecto, las funciones explícitas
no se rellenan.


Un caso de especial utilidad es `filled_func=0`, con lo que se sombrea la
región limitada por el eje horizontal y la función explícita.


Esta opción sólo afecta al objeto gráfico bidimensional `explicit`.


Ejemplo:


Región limitada por un objeto `explicit` y el borde inferior
de la ventana gráfica.


```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = red,
             filled_func = true,
             explicit(sin(x),x,0,10) )$
```


Región limitada por un objeto `explicit` y la función
definida en la opción `filled_func`. Nótese que la 
variable en `filled_func` debe ser la misma que la utilizada en 
`explicit`.


```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = grey,
             filled_func = sin(x),
             explicit(-sin(x),x,0,%pi));
```


Véanse también `fill_color` y `explicit`.

<!-- category: Plotting -->
<!-- keywords: font -->
<!-- signatures: font -->
### Variable: font

Valor por defecto: `""` (cadena vacía)


Esta opción permite seleccionar el tipo de fuente a utilizar por el
terminal. Sólo se puede utilizar un tipo de fuente y tamaño por
gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Véase también `font_size`.


Gnuplot no puede gestionar por sí mismo las fuentes,
dejando esta tarea a las librerías que dan soporte a los
diferentes terminales, cada uno con su propia manera de controlar
la tipografía. A continuación un breve resumen:



- *
*x11*:
Utiliza el mecanismo habitual para suministrar las fuentes en x11.

Ejemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(font      = "Arial", 
             font_size = 20,
             label(["Arial font, size 20",1,1]))$
```
- *
*windows*:
El terminal de windows no permite cambiar fuentes desde dentro
del gráfico. Una vez se ha creado el gráfico, se pueden cambiar las
fuentes haciendo clic derecho en el menú de la ventana gráfica.
- *
*png, jpeg, gif*:
La librería *libgd* utiliza la ruta a las fuentes
almacenada en la variable de entorno `GDFONTPATH`; en tal caso
sólo es necesario darle a la opción `font` el nombre de la
fuente. También es posible darle la ruta completa al fichero de la fuente.

Ejemplos:

A la opción `font` se le puede dar la ruta completa al fichero de la fuente:

```maxima
(%i1) load("draw")$
(%i2) path: "/usr/share/fonts/truetype/freefont/" $
(%i3) file: "FreeSerifBoldItalic.ttf" $
(%i4) draw2d(
        font      = concat(path, file), 
        font_size = 20,
        color     = red,
        label(["FreeSerifBoldItalic font, size 20",1,1]),
        terminal  = png)$
```

Si la variable de entorno `GDFONTPATH` almacena la ruta
a la carpeta donde se alojan las fuentes, es posible darle a la
opción `font` sólo el nombre de la fuente:

```maxima
(%i1) load("draw")$
(%i2) draw2d(
        font      = "FreeSerifBoldItalic", 
        font_size = 20,
        color     = red,
        label(["FreeSerifBoldItalic font, size 20",1,1]),
        terminal  = png)$
```
- *
*Postscript*:
Las fuentes estándar de Postscript son: `"Times-Roman"`, `"Times-Italic"`, `"Times-Bold"`, `"Times-BoldItalic"`, `"Helvetica"`, `"Helvetica-Oblique"`, `"Helvetica-Bold"`, `"Helvetic-BoldOblique"`, `"Courier"`, `"Courier-Oblique"`, `"Courier-Bold"` y `"Courier-BoldOblique"`.
  
Ejemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(
        font      = "Courier-Oblique", 
        font_size = 15,
        label(["Courier-Oblique font, size 15",1,1]),
        terminal = eps)$
```
- *
*pdf*:
Utiliza las mismas fuentes que *Postscript*.
- *
*pdfcairo*:
Utiliza las mismas fuentes que *wxt*.
- *
*wxt*:
La librería *pango* encuentra las fuentes por medio de la utilidad `fontconfig`.
- *
*aqua*:
La fuente por defecto es `"Times-Roman"`.


La documentación de gnuplot es una importante fuente de información sobre terminales y fuentes.

<!-- category: Plotting -->
<!-- keywords: font_size -->
<!-- signatures: font_size -->
### Variable: font_size

Valor por defecto: 10


Esta opción permite seleccionar el tamaño de la fuente a utilizar por el
terminal. Sólo se puede utilizar un tipo de fuente y tamaño por
gráfico. `font_size` sólo se activa cuando la opción `font`
tiene un valor diferente de la cadena vacía.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Véase también `font`.

<!-- category: Plotting -->
<!-- keywords: geomap -->
<!-- signatures: geomap(numlist), geomap(numlist, 3Dprojection) -->
### Function: geomap (numlist)

Dibuja mapas cartográficos en 2D y 3D.


**2D**


Esta función trabaja junto con la variable global `boundaries_array`.


El argumento *numlist* es una lista de números o de listas de 
números. Todos estos números deben ser enteros mayores o iguales que cero,
representando las componentes del array global `boundaries_array`.


Cada componente de `boundaries_array` es un array de decimales en
coma flotante, las coordenadas de un segmento poligonal o línea
fronteriza.


`geomap (numlist)` toma los enteros de sus argumentos y 
dibuja los segmentos poligonales asociados de `boundaries_array`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `line_width`, 
`line_type` y `color`.


Ejemplos:


Un sencillo mapa hecho a mano:


```maxima
(%i1) load("worldmap")$
(%i2) /* Vertices of boundary #0: {(1,1),(2,5),(4,3)} */
   ( bnd0: make_array(flonum,6),
     bnd0[0]:1.0, bnd0[1]:1.0, bnd0[2]:2.0,
     bnd0[3]:5.0, bnd0[4]:4.0, bnd0[5]:3.0 )$
(%i3) /* Vertices of boundary #1: {(4,3),(5,4),(6,4),(5,1)} */
   ( bnd1: make_array(flonum,8),
     bnd1[0]:4.0, bnd1[1]:3.0, bnd1[2]:5.0, bnd1[3]:4.0,
     bnd1[4]:6.0, bnd1[5]:4.0, bnd1[6]:5.0, bnd1[7]:1.0)$
(%i4) /* Vertices of boundary #2: {(5,1), (3,0), (1,1)} */
   ( bnd2: make_array(flonum,6),
     bnd2[0]:5.0, bnd2[1]:1.0, bnd2[2]:3.0,
     bnd2[3]:0.0, bnd2[4]:1.0, bnd2[5]:1.0 )$
(%i5) /* Vertices of boundary #3: {(1,1), (4,3)} */
   ( bnd3: make_array(flonum,4),
     bnd3[0]:1.0, bnd3[1]:1.0, bnd3[2]:4.0, bnd3[3]:3.0)$
(%i6) /* Vertices of boundary #4: {(4,3), (5,1)} */
   ( bnd4: make_array(flonum,4),
     bnd4[0]:4.0, bnd4[1]:3.0, bnd4[2]:5.0, bnd4[3]:1.0)$
(%i7) /* Pack all together in boundaries_array */
   ( boundaries_array: make_array(any,5),
     boundaries_array[0]: bnd0, boundaries_array[1]: bnd1,
     boundaries_array[2]: bnd2, boundaries_array[3]: bnd3,
     boundaries_array[4]: bnd4 )$
(%i8) draw2d(geomap([0,1,2,3,4]))$
```


El paquete auxiliar `worldmap` asigna al array global
`boundaries_array` líneas fronterizas
reales en coordenadas (longitud, latitud). Estos datos son
de dominio público y proceden de
[http://www-cger.nies.go.jp/grid-e/gridtxt/grid19.html]().
El paquete `worldmap` también define fronteras 
de países, continentes y líneas
costeras a partir de las
componentes de `boundaries_array` (véase el
fichero `share/draw/worldmap.mac` para más
información). El paquete `worldmap` carga
automáticamente el paquete `draw`.


```maxima
(%i1) load("worldmap")$
(%i2) c1: gr2d(geomap([Canada,United_States,
                       Mexico,Cuba]))$
(%i3) c2: gr2d(geomap(Africa))$
(%i4) c3: gr2d(geomap([Oceania,China,Japan]))$
(%i5) c4: gr2d(geomap([France,Portugal,Spain,
                       Morocco,Western_Sahara]))$
(%i6) draw(columns  = 2,
           c1,c2,c3,c4)$
```


`worldmap` se puede utilizar para dibujar países
como polígonos. En este caso, ya no será necesario
hacer uso del objeto gráfico `geomap`, pero sí de
`polygon`. Puesto que en este caso se utilizan listas en lugar de
arrays, los mapas se reproducirán de forma más lenta. Véanse
también `make_poly_country` y `make_poly_continent` para
comprender el siguiente código.


```maxima
(%i1) load("worldmap")$
(%i2) mymap: append(
   [color      = white],  /* borders are white */
   [fill_color = red],             make_poly_country(Bolivia),
   [fill_color = cyan],            make_poly_country(Paraguay),
   [fill_color = green],           make_poly_country(Colombia),
   [fill_color = blue],            make_poly_country(Chile),
   [fill_color = "#23ab0f"],       make_poly_country(Brazil),
   [fill_color = goldenrod],       make_poly_country(Argentina),
   [fill_color = "midnight-blue"], make_poly_country(Uruguay))$
(%i3) apply(draw2d, mymap)$
```


**3D**


`geomap (numlist)` proyecta los mapas sobre la esfera de radio 1
y centro (0,0,0). Es posible cambiar la esfera o el tipo de proyección haciendo
uso de `geomap (numlist,3Dprojection)`.


Proyecciones 3D disponibles:



- *
`[spherical_projection,x,y,z,r]`: proyecta los mapas sobre la esfera de radio
*r* y centro (*x*,*y*,*z*).

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap(Australia), /* default projection */
             geomap(Australia,
                    [spherical_projection,2,2,2,3]))$
```
- *
`[cylindrical_projection,x,y,z,r,rc]`: re-proyecta mapas esféricos
sobre el cilindro de radio *rc* cuyo eje pasa a través de los polos del globo
de radio *r* y centro (*x*,*y*,*z*).

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap([America_coastlines,Eurasia_coastlines],
                    [cylindrical_projection,2,2,2,3,4]))$
```
- *
`[conic_projection,x,y,z,r,alpha]`: re-proyecta mapas esféricos sobre los
conos de ángulo *alpha*, cuyos ejes pasan a través de los polos del globo de radio *r* 
y centro (*x*,*y*,*z*). Ambos conos, norte y sur, son tangentes a la esfera.

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap(World_coastlines,
                    [conic_projection,0,0,0,1,90]))$
```


En [https://riotorto.users.sourceforge.net/Maxima/gnuplot/geomap/]()
hay ejemplos más elaborados.

<!-- category: Plotting -->
<!-- keywords: get_pixel -->
<!-- signatures: get_pixel(pic, x, y) -->
### Function: get_pixel (pic, x, y)

Devuelve el pixel de la imagen *pic*. Las coordenadas *x* e *y*
van desde 0 hasta `ancho-1` y `alto-1`, respectivamente.

<!-- category: Plotting -->
<!-- keywords: gnuplot_file_name -->
<!-- signatures: gnuplot_file_name -->
### Variable: gnuplot_file_name

Valor por defecto: `"maxout.gnuplot"`


`gnuplot_file_name` es el nombre del fichero que 
almacena las instrucciones a ser procesadas por Gnuplot.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
       file_name = "my_file",
       gnuplot_file_name = "my_commands_for_gnuplot",
       data_file_name    = "my_data_for_gnuplot",
       terminal          = png,
       explicit(x^2,x,-1,1)) $
```


Véase también `data_file_name`.

<!-- category: Plotting -->
<!-- keywords: gr2d -->
<!-- signatures: gr2d(Opción gráfica, ..., graphic_object, ...) -->
### Function: gr2d (Opción gráfica, ..., graphic_object, ...)

La función `gr2d` construye un objeto que describe una escena 2d. Los
argumentos son *opciones gráficas* y *objetos gráficos*
o listas que contengan elementos de ambos tipos. Esta escena
se interpreta secuencialmente: las *opciones gráficas* afectan a aquellos
*objetos gráficos* colocados a su derecha. Algunas *opciones gráficas*
afectan al aspecto global de la escena.


La lista de *objetos gráficos* disponibles para escenas en dos
dimensiones: `bars`, `ellipse`, `explicit`, `image`,
`implicit`, `label`, `parametric`, `points`, `polar`,
`polygon`, `quadrilateral`, `rectangle`, `triangle`,
`vector` y `geomap` (este último definido en el paquete `worldmap`).


Véanse también `draw` y `draw2d`.


Para utilizar este objecto, ejecútese primero `load("draw")`.

<!-- category: Plotting -->
<!-- keywords: gr3d -->
<!-- signatures: gr3d(Opción gráfica, ..., graphic_object, ...) -->
### Function: gr3d (Opción gráfica, ..., graphic_object, ...)

La función `gr3d` construye un objeto que describe una escena 3d. Los
argumentos son *opciones gráficas* y *objetos gráficos*
o listas que contengan elementos de ambos tipos. Esta escena
se interpreta secuencialmente: las *opciones gráficas* afectan a aquellos
*objetos gráficos* colocados a su derecha. Algunas *opciones gráficas*
afectan al aspecto global de la escena.


La lista de *objetos gráficos* disponibles para escenas en tres
dimensiones: `cylindrical`, `elevation_grid`, `explicit`, 
`implicit`, `label`, `mesh`, `parametric`, 
`parametric_surface`, `points`, `quadrilateral`, 
`spherical`, `triangle`, `tube`, `vector`
y `geomap` (este último definido en el paquete `worldmap`).


Véanse también `draw` y `draw3d`.


Para utilizar este objeto, ejecútese primero `load("draw")`.

<!-- category: Plotting -->
<!-- keywords: head_angle -->
<!-- signatures: head_angle -->
### Variable: head_angle

Valor por defecto: 45


`head_angle` indica el ángulo, en grados, entre la flecha y el
segmento del vector.


Esta opción sólo es relevante para objetos de tipo `vector`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,10],
             yrange      = [0,9],
             head_length = 0.7,
             head_angle  = 10,
             vector([1,1],[0,6]),
             head_angle  = 20,
             vector([2,1],[0,6]),
             head_angle  = 30,
             vector([3,1],[0,6]),
             head_angle  = 40,
             vector([4,1],[0,6]),
             head_angle  = 60,
             vector([5,1],[0,6]),
             head_angle  = 90,
             vector([6,1],[0,6]),
             head_angle  = 120,
             vector([7,1],[0,6]),
             head_angle  = 160,
             vector([8,1],[0,6]),
             head_angle  = 180,
             vector([9,1],[0,6]) )$
```


Véanse también `head_both`, `head_length` y `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_both -->
<!-- signatures: head_both -->
### Variable: head_both

Valor por defecto: `false`


Cuando `head_both` vale `true`, los vectores se dibujan bidireccionales.
Si vale `false`, se dibujan unidireccionales.


Esta opción sólo es relevante para objetos de tipo `vector`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,8],
             yrange      = [0,8],
             head_length = 0.7,
             vector([1,1],[6,0]),
             head_both   = true,
             vector([1,7],[6,0]) )$
```


Véanse también `head_length`, `head_angle` y `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_length -->
<!-- signatures: head_length -->
### Variable: head_length

Valor por defecto: 2


`head_length` indica, en las unidades del eje *x*, la
longitud de las flechas de los vectores.


Esta opción sólo es relevante para objetos de tipo `vector`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,12],
             yrange      = [0,8],
             vector([0,1],[5,5]),
             head_length = 1,
             vector([2,1],[5,5]),
             head_length = 0.5,
             vector([4,1],[5,5]),
             head_length = 0.25,
             vector([6,1],[5,5]))$
```


Véanse también `head_both`, `head_angle` y `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_type -->
<!-- signatures: head_type -->
### Variable: head_type

Valor por defecto: `filled`


`head_type` se utiliza para especificar cómo se habrán de
dibujar las flechas de los vectores. Los valores posibles para
esta opción son: `filled` (flechas cerradas y rellenas),
`empty` (flechas cerradas pero no rellenas) y `nofilled`
(flechas abiertas).


Esta opción sólo es relevante para objetos de tipo `vector`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,12],
             yrange      = [0,10],
             head_length = 1,
             vector([0,1],[5,5]), /* default type */
             head_type = 'empty,
             vector([3,1],[5,5]),
             head_type = 'nofilled,
             vector([6,1],[5,5]))$
```


Véanse también `head_both`, `head_angle` y `head_length`.

<!-- category: Plotting -->
<!-- keywords: image -->
<!-- signatures: image(im, x0, y0, width, height) -->
### Function: image (im, x0, y0, width, height)

Reproduce una imagen en 2D.


**2D**


`image (im,x0,y0,width,height)`:
dibuja la imagen *im* en la región rectangular desde el vértice `(x0,y0)`
hasta el `(x0+width,y0+height)` del plano real. El argumento *im* debe ser una
matriz de números reales, una matriz de vectores de longitud tres o un objeto
de tipo `picture`.


Si *im* es una matriz de números reales, los valores de los
píxeles se interpretan según indique la opción
gráfica `palette`, que es un vector de longitud tres con sus componentes tomando
valores enteros en el rango desde -36 a +36; cada valor es un 
índice para seleccionar una fórmula que transforma los niveles
numéricos en las componentes cromáticas rojo, verde y azul:


```maxima
0: 0               1: 0.5           2: 1
 3: x               4: x^2           5: x^3
 6: x^4             7: sqrt(x)       8: sqrt(sqrt(x))
 9: sin(90x)       10: cos(90x)     11: |x-0.5|
12: (2x-1)^2       13: sin(180x)    14: |cos(180x)|
15: sin(360x)      16: cos(360x)    17: |sin(360x)|
18: |cos(360x)|    19: |sin(720x)|  20: |cos(720x)|
21: 3x             22: 3x-1         23: 3x-2
24: |3x-1|         25: |3x-2|       26: (3x-1)/2
27: (3x-2)/2       28: |(3x-1)/2|   29: |(3x-2)/2|
30: x/0.32-0.78125 31: 2*x-0.84
32: 4x;1;-2x+1.84;x/0.08-11.5
33: |2*x - 0.5|    34: 2*x          35: 2*x - 0.5
36: 2*x - 1
```

los números negativos se interpretan como colores invertidos
de las componentes cromáticas.


`palette = gray` y `palette = color` son atajos para
`palette = [3,3,3]` y `palette = [7,5,15]`, respectivamente.


Si *im* es una matriz de vectores de longitud tres, éstos se
interpretarán como las componentes cromáticas rojo, verde y azul.


Ejemplos:


Si *im* es una matriz de números reales, los valores de los
píxeles se interpretan según indique la opción
gráfica `palette`.


```maxima
(%i1) load("draw")$
(%i2) im: apply(
           'matrix,
            makelist(makelist(random(200),i,1,30),i,1,30))$
(%i3) /* palette = color, default */
      draw2d(image(im,0,0,30,30))$
(%i4) draw2d(palette = gray, image(im,0,0,30,30))$
(%i5) draw2d(palette = [15,20,-4],
             colorbox=false,
             image(im,0,0,30,30))$
```


Véase también `colorbox`.


Si *im* es una matriz de vectores de longitud tres, éstos se
interpretarán como las componentes cromáticas rojo, verde y azul.


```maxima
(%i1) load("draw")$
(%i2) im: apply(
            'matrix,
             makelist(
               makelist([random(300),
                         random(300),
                         random(300)],i,1,30),i,1,30))$
(%i3) draw2d(image(im,0,0,30,30))$
```


El paquete `draw` carga automáticamente el paquete `picture`. 
En este ejemplo, una imagen de niveles se define a mano, reproduciéndola
a continuación.


```maxima
(%i1) load("draw")$
(%i2) im: make_level_picture([45,87,2,134,204,16],3,2);
(%o2)       picture(level, 3, 2, {Array:  #(45 87 2 134 204 16)})
(%i3) /* default color palette */
      draw2d(image(im,0,0,30,30))$
(%i4) /* gray palette */
      draw2d(palette = gray,
             image(im,0,0,30,30))$
```


Se lee un fichero xpm y se reproduce.


```maxima
(%i1) load("draw")$
(%i2) im: read_xpm("myfile.xpm")$
(%i3) draw2d(image(im,0,0,10,7))$
```


Véanse también `make_level_picture`, `make_rgb_picture` y `read_xpm`.


En [http://www.telefonica.net/web2/biomates/maxima/gpdraw/image]()
se encuentran ejemplos más elaborados.

<!-- category: Plotting -->
<!-- keywords: implicit -->
<!-- signatures: implicit(fcn, x, xmin, xmax, y, ymin, ymax), implicit(fcn, x, xmin, xmax, y, ymin, ymax, z, zmin, zmax) -->
### Function: implicit (fcn, x, xmin, xmax, y, ymin, ymax)

Dibuja funciones implícitas en 2D y 3D.


**2D**


`implicit (fcn,x,xmin,xmax,y,ymin,ymax)`
dibuja la función implícita *fcn*, con la variable
`x` tomando valores desde *xmin* hasta *xmax*,
y la variable *y* tomando valores desde *ymin* hasta *ymax*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `ip_grid`, 
`ip_grid_in`, `line_width`, `line_type`, `key` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal  = eps,
             grid      = true,
             line_type = solid,
             key       = "y^2=x^3-2*x+1",
             implicit(y^2=x^3-2*x+1, x, -4,4, y, -4,4),
             line_type = dots,
             key       = "x^3+y^3 = 3*x*y^2-x-1",
             implicit(x^3+y^3 = 3*x*y^2-x-1, x,-4,4, y,-4,4),
             title     = "Two implicit functions" )$
```


**3D**


`implicit (fcn,x,xmin,xmax, y,ymin,ymax, z,zmin,zmax)`
dibuja la función implícita *fcn*, con la variable *x* 
tomando valores desde *xmin* hasta *xmax*, la variable *y* tomando 
valores desde *ymin* hasta *ymax* y la variable *z* tomando 
valores desde *zmin* hasta *zmax*. Este objeto está programado con el 
algoritmo *marching cubes*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `x_voxel`, 
`y_voxel`, `z_voxel`, `line_width`, `line_type`, `key`, 
`wired_surface`, `enhanced3d` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        color=blue,
        implicit((x^2+y^2+z^2-1)*(x^2+(y-1.5)^2+z^2-0.5)=0.015,
                 x,-1,1,y,-1.2,2.3,z,-1,1),
        surface_hide=true);
```

<!-- category: Plotting -->
<!-- keywords: interpolate_color -->
<!-- signatures: interpolate_color -->
### Variable: interpolate_color

Valor por defecto: `false`


Esta opción solo es relevante si `enhanced3d` tiene un valor 
diferente de `false`.


Si `interpolate_color` vale `false`, las superficies se colorean con
cuadriláteros homogéneos. Si vale `true`, las transiciones de colores se
suavizan por interpolación.


La opción `interpolate_color` también acepta una lista de dos números, `[m,n]`.
Para *m* y *n* positivos, cada cuadrilátero o triángulo se interpola
*m* y *n* veces en la dirección respectiva. Para *m* y *n* negativos,
la frecuencia de interpolación se elige de forma que se dibujen al menos *abs(m)* y
*abs(n)* puntos, pudiéndose considerar esto como una función especial de enrejado.
Con valores nulos, esto es `interpolate_color=[0,0]`, se seleccionará un número 
óptimo de puntos interpolados en la superficie.


Además, `interpolate_color=true` es equivalente a `interpolate_color=[0,0]`.


La interpolación de colores en superficies paramétricas puede dar resultados
imprevisibles.


Ejemplos:


Interpolación de color con funciones explícitas.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        enhanced3d   = sin(x*y),
        explicit(20*exp(-x^2-y^2)-10, x ,-3, 3, y, -3, 3)) $
(%i3) draw3d(
        interpolate_color = true,
        enhanced3d   = sin(x*y),
        explicit(20*exp(-x^2-y^2)-10, x ,-3, 3, y, -3, 3)) $
(%i4) draw3d(
        interpolate_color = [-10,0],
        enhanced3d   = sin(x*y),
        explicit(20*exp(-x^2-y^2)-10, x ,-3, 3, y, -3, 3)) $
```


Interpolación de color con el objeto `mesh`.



```maxima
(%i1) load("draw")$
(%i2) draw3d( 
        enhanced3d = true,
        mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
             [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
             [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
(%i3) draw3d( 
        enhanced3d        = true,
        interpolate_color = true,
        mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
             [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
             [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
(%i4) draw3d( 
        enhanced3d        = true,
        interpolate_color = true,
        view=map,
        mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
             [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
             [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
```


Véase también `enhanced3d`.

<!-- category: Plotting -->
<!-- keywords: ip_grid -->
<!-- signatures: ip_grid -->
### Variable: ip_grid

Valor por defecto: `[50, 50]`


`ip_grid` establece la rejilla del primer muestreo para los
gráficos de funciones implícitas.


Esta opción sólo es relevante para funciones de tipo `implicit`.

<!-- category: Plotting -->
<!-- keywords: ip_grid_in -->
<!-- signatures: ip_grid_in -->
### Variable: ip_grid_in

Valor por defecto: `[5, 5]`


`ip_grid_in` establece la rejilla del segundo muestreo para los
gráficos de funciones implícitas.


Esta opción sólo es relevante para funciones de tipo `implicit`.

<!-- category: Plotting -->
<!-- keywords: key -->
<!-- signatures: key -->
### Variable: key

Valor por defecto: `""` (cadena vacía)


`key` es la clave de una función en la leyenda. Si `key`
es una cadena vacía, las funciones no tendrán clave
asociada en la leyenda.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `points`, `polygon`, `rectangle`,
`ellipse`, `vector`, `explicit`, `implicit`,
`parametric` y `polar`.
- *
`gr3d`: `points`, `explicit`, `parametric`,
y `parametric_surface`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(key   = "Sinus",
             explicit(sin(x),x,0,10),
             key   = "Cosinus",
             color = red,
             explicit(cos(x),x,0,10) )$
```

<!-- category: Plotting -->
<!-- keywords: key_pos -->
<!-- signatures: key_pos -->
### Variable: key_pos

Valor por defecto: `""` (cadena vacía)


La opción `key_pos` establece en qué posición se colocará la leyenda.
Si `key` es una cadena vacía, entonces se utilizará por defecto la
posición `"top_right"`.
Los valores disponibles para esta opción son: `top_left`, `top_center`,
`top_right`, `center_left`, `center`, `center_right`,
`bottom_left`, `bottom_center` y `bottom_right`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplos:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        key_pos = top_left,
        key     = "x",
        explicit(x,  x,0,10),
        color   = red,
        key     = "x squared",
        explicit(x^2,x,0,10))$
(%i3) draw3d(
        key_pos = center,
        key     = "x",
        explicit(x+y,x,0,10,y,0,10),
        color= red,
        key     = "x squared",
        explicit(x^2+y^2,x,0,10,y,0,10))$
```

<!-- category: Plotting -->
<!-- keywords: label -->
<!-- signatures: label([string, x, y], ...), label([string, x, y, z], ...) -->
### Function: label ([string, x, y], ...)

Escribe etiquetas en 2D y 3D.


Las etiquetas coloreadas sólo trabajan con Gnuplot 4.3. Este es un fallo conocido del
paquete `draw`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `label_alignment`, 
`label_orientation` y `color`.


**2D**


`label([string,x,y])` escribe la cadena de caracteres *string* 
en el punto `[x,y]`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(yrange = [0.1,1.4],
             color = red,
             label(["Label in red",0,0.3]),
             color = "#0000ff",
             label(["Label in blue",0,0.6]),
             color = light_blue,
             label(["Label in light-blue",0,0.9],
                   ["Another light-blue",0,1.2])  )$
```


**3D**


`label([string,x,y,z])` escribe la cadena de caracteres *string*
en el punto `[x,y,z]`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3),
             color = red,
             label(["UP 1",-2,0,3], ["UP 2",1.5,0,4]),
             color = blue,
             label(["DOWN 1",2,0,-3]) )$
```

<!-- category: Plotting -->
<!-- keywords: label_alignment -->
<!-- signatures: label_alignment -->
### Variable: label_alignment

Valor por defecto: `center`


`label_alignment` se utiliza para especificar dónde se escribirán
las etiquetas con respecto a las coordenadas de referencia. Los valores posibles para
esta opción son: `center`, `left` y `right`.


Esta opción sólo es relevante para objetos de tipo `label`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange          = [0,10],
             yrange          = [0,10],
             points_joined   = true,
             points([[5,0],[5,10]]),
             color           = blue,
             label(["Centered alignment (default)",5,2]),
             label_alignment = 'left,
             label(["Left alignment",5,5]),
             label_alignment = 'right,
             label(["Right alignment",5,8]))$
```


Véanse también `label_orientation` y `color`.

<!-- category: Plotting -->
<!-- keywords: label_orientation -->
<!-- signatures: label_orientation -->
### Variable: label_orientation

Valor por defecto: `horizontal`


`label_orientation` se utiliza para especificar la orientación
de las etiquetas. Los valores posibles para esta opción son:
`horizontal` y `vertical`.


Esta opción sólo es relevante para objetos de tipo `label`.


Ejemplo:


En este ejemplo, el punto ficticio que se añade sirve para obtener
la imagen, ya que el paquete `draw` necesita siempre de datos para
construir la escena.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange     = [0,10],
             yrange     = [0,10],
             point_size = 0,
             points([[5,5]]),
             color      = navy,
             label(["Horizontal orientation (default)",5,2]),
             label_orientation = 'vertical,
             color             = "#654321",
             label(["Vertical orientation",1,5]))$
```


Véanse también `label_alignment` y `color`.

<!-- category: Plotting -->
<!-- keywords: line_type -->
<!-- signatures: line_type -->
### Variable: line_type

Valor por defecto: `solid`


`line_type` indica cómo se van a dibujar las líneas;
valores posibles son `solid` y `dots`, que están disponibles
en todos los terminales, y `dashes`, `short_dashes`, 
`short_long_dashes`, `short_short_long_dashes` y `dot_dash`,
que no esán disponibles en los terminales `png`, `jpg` y `gif`.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` y `polar`.
- *
`gr3d`: `points`, `explicit`, `parametric` y `parametric_surface`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(line_type = dots,
             explicit(1 + x^2,x,-1,1),
             line_type = solid, /* default */
             explicit(2 + x^2,x,-1,1))$
```


Véase también `line_width`.

<!-- category: Plotting -->
<!-- keywords: line_width -->
<!-- signatures: line_width -->
### Variable: line_width

Valor por defecto: 1


`line_width` es el ancho de las líneas a dibujar.
Su valor debe ser un número positivo.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` y `polar`.
- *
`gr3d`: `points` y `parametric`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^2,x,-1,1), /* default width */
             line_width = 5.5,
             explicit(1 + x^2,x,-1,1),
             line_width = 10,
             explicit(2 + x^2,x,-1,1))$
```


Véase también `line_type`.

<!-- category: Plotting -->
<!-- keywords: logcb -->
<!-- signatures: logcb -->
### Variable: logcb

Valor por defecto: `false`


Cuando `logcb` vale `true`, la escala de colores se dibuja 
logarítmicamente.


Cuando `enhanced3d` o `colorbox` vale `false`, la 
opción `logcb` no tiene efecto alguno.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d (
        enhanced3d = true,
        color      = green,
        logcb = true,
        logz  = true,
        palette = [-15,24,-9],
        explicit(exp(x^2-y^2), x,-2,2,y,-2,2)) $
```


Véanse también `enhanced3d`, `colorbox` y `cbrange`.

<!-- category: Plotting -->
<!-- keywords: logx_secondary -->
<!-- signatures: logx_secondary -->
### Variable: logx_secondary

Valor por defecto: `false`


Si `logx_secondary` vale `true`, el eje secundario de *x* 
se dibuja en la escala logarítmica.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        grid = true,
        key="x^2, linear scale",
        color=red,
        explicit(x^2,x,1,100),
        xaxis_secondary = true,
        xtics_secondary = true,
        logx_secondary  = true,
        key = "x^2, logarithmic x scale",
        color = blue,
        explicit(x^2,x,1,100) )$
```


Véanse también `logx`, `logy`, `logy_secondary` y `logz`.

<!-- category: Plotting -->
<!-- keywords: logy_secondary -->
<!-- signatures: logy_secondary -->
### Variable: logy_secondary

Valor por defecto: `false`


Si `logy_secondary` vale `true`, el eje secundario de *y* 
se dibuja en la escala logarítmica.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        grid = true,
        key="x^2, linear scale",
        color=red,
        explicit(x^2,x,1,100),
        yaxis_secondary = true,
        ytics_secondary = true,
        logy_secondary  = true,
        key = "x^2, logarithmic y scale",
        color = blue,
        explicit(x^2,x,1,100) )$
```


Véanse también `logx`, `logy`, `logx_secondary` y `logz`.

<!-- category: Plotting -->
<!-- keywords: logz -->
<!-- signatures: logz -->
### Variable: logz

Valor por defecto: `false`


Cuando `logz` vale `true`, el eje *z* se dibuja
en la escala logarítmica.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(logz = true,
             explicit(exp(u^2+v^2),u,-2,2,v,-2,2))$
```


Véanse también `logx` and `logy`.

<!-- category: Plotting -->
<!-- keywords: make_level_picture -->
<!-- signatures: make_level_picture(data), make_level_picture(data, width, height) -->
### Function: make_level_picture (data)

Devuelve un objeto `picture` consistente en una imagen de niveles.
`make_level_picture (data)` construye el objeto `picture`
a partir de la matriz *data*.
`make_level_picture (data,width,height)`
construye el objeto a partir de una lista de números, en cuyo
caso deben indicarse el ancho *width* y la altura *height*
en píxeles.


El objeto  `picture` devuelto contiene los siguientes cuatro
elemento:



1. el símbolo `level`
2. anchura de la imagen
3. altura de la imagen
4. un array de enteros con los valores de los píxeles
entre 0 y 255. El argumento *data* debe contener sólo números
entre 0 y 255; los cantidades negativas se transforman en ceros y las 
que son mayores de 255 se igualan a este número.


Ejemplo:


Imagen de niveles a partir de una matriz.


```maxima
(%i1) load("draw")$
(%i2) make_level_picture(matrix([3,2,5],[7,-9,3000]));
(%o2)         picture(level, 3, 2, {Array:  #(3 2 5 7 0 255)})
```


Imagen de niveles a partir de una lista numérica.


```maxima
(%i1) load("draw")$
(%i2) make_level_picture([-2,0,54,%pi],2,2);
(%o2)            picture(level, 2, 2, {Array:  #(0 0 54 3)})
```

<!-- category: Plotting -->
<!-- keywords: make_poly_continent -->
<!-- signatures: make_poly_continent(continent_name), make_poly_continent(country_list) -->
### Function: make_poly_continent (continent_name)

Construye los polígonos necesarios para dibujar
un continente o lista de países coloreados.


Ejemplo:



```maxima
(%i1) load("worldmap")$
(%i2) /* A continent */
      make_poly_continent(Africa)$
(%i3) apply(draw2d, %)$
(%i4) /* A list of countries */
      make_poly_continent([Germany,Denmark,Poland])$
(%i5) apply(draw2d, %)$
```

<!-- category: Plotting -->
<!-- keywords: make_poly_country -->
<!-- signatures: make_poly_country(country_name) -->
### Function: make_poly_country (country_name)

Construye los polígonos necesarios para dibujar
un país coloreado. En caso de contener islas,
un país tendrá asociados varios polígonos.


Ejemplo:



```maxima
(%i1) load("worldmap")$
(%i2) make_poly_country(India)$
(%i3) apply(draw2d, %)$
```

<!-- category: Plotting -->
<!-- keywords: make_polygon -->
<!-- signatures: make_polygon(nlist) -->
### Function: make_polygon (nlist)

Devuelve un objeto `polygon` a partie de una lista
de líneas fronterizas y de costas. El
argumento *nlist* debe ser una lista de componentes
de `boundaries_array`.


Ejemplo:


La variable Bhutan (Bután) está definida con los números
fronterizos 171, 173 y 1143, de manera que `make_polygon([171,173,1143])`
concatena los arrays `boundaries_array[171]`, `boundaries_array[173]` y
`boundaries_array[1143]` y devuelve un objeto `polygon`
apto para ser dibujado por `draw`. A fin de evitar mensajes
de errores, los arrays deben ser compatibles en el sentido de que dos
de ellos consecutivos deben tener dos coordenadas comunes en los
extremos. En este ejemplo, las dos primeras componentes de 
`boundaries_array[171]` son iguales a las dos últimas de
`boundaries_array[173]`, y las dos primeras de `boundaries_array[173]`
coinciden con las dos primeras de `boundaries_array[1143]`;
en conclusión, los números de segmentos poligonales171, 173 y 1143
(en este orden) son compatibles y el polígono
coloreado se podrá dibujar.


```maxima
(%i1) load("worldmap")$
(%i2) Bhutan;
(%o2)                        [[171, 173, 1143]]
(%i3) boundaries_array[171];
(%o3) {Array:  
       #(88.750549 27.14727 88.806351 27.25305 88.901367 27.282221
         88.917877 27.321039)}
(%i4) boundaries_array[173];
(%o4) {Array:
       #(91.659554 27.76511 91.6008 27.66666 91.598022 27.62499
         91.631348 27.536381 91.765533 27.45694 91.775253 27.4161 
         92.007751 27.471939 92.11441 27.28583 92.015259 27.168051
         92.015533 27.08083 92.083313 27.02277 92.112183 26.920271
         92.069977 26.86194 91.997192 26.85194 91.915253 26.893881
         91.916924 26.85416 91.8358 26.863331 91.712479 26.799999 
         91.542191 26.80444 91.492188 26.87472 91.418854 26.873329
         91.371353 26.800831 91.307457 26.778049 90.682457 26.77417
         90.392197 26.903601 90.344131 26.894159 90.143044 26.75333
         89.98996 26.73583 89.841919 26.70138 89.618301 26.72694 
         89.636093 26.771111 89.360786 26.859989 89.22081 26.81472
         89.110237 26.829161 88.921631 26.98777 88.873016 26.95499
         88.867737 27.080549 88.843307 27.108601 88.750549 
         27.14727)}
(%i5) boundaries_array[1143];
(%o5) {Array:  
       #(91.659554 27.76511 91.666924 27.88888 91.65831 27.94805 
         91.338028 28.05249 91.314972 28.096661 91.108856 27.971109
         91.015808 27.97777 90.896927 28.05055 90.382462 28.07972
         90.396088 28.23555 90.366074 28.257771 89.996353 28.32333
         89.83165 28.24888 89.58609 28.139999 89.35997 27.87166 
         89.225517 27.795 89.125793 27.56749 88.971077 27.47361
         88.917877 27.321039)}
(%i6) Bhutan_polygon: make_polygon([171,173,1143])$
(%i7) draw2d(Bhutan_polygon)$
```

<!-- category: Plotting -->
<!-- keywords: make_rgb_picture -->
<!-- signatures: make_rgb_picture(redlevel, greenlevel, bluelevel) -->
### Function: make_rgb_picture (redlevel, greenlevel, bluelevel)

Devuelve un objeto *picture* conteniendo una imagen en color (RGB).
Los tres argumentos deben ser imágenes de niveles, para el rojo (R),
verde (G) y azul (B).


El objeto  *picture* devuelto contiene los siguientes cuatro
elemento:



1. el símbolo `rgb`
2. anchura de la imagen
3. altura de la imagen
4. un array de enteros de *3*ancho*alto* con los valores de los píxeles
entre 0 y 255. Cada valor de pixel se representa en el array con tres números consecutivos
(rojo, verde, azul).


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) red: make_level_picture(matrix([3,2],[7,260]));
(%o2)           picture(level, 2, 2, {Array:  #(3 2 7 255)})
(%i3) green: make_level_picture(matrix([54,23],[73,-9]));
(%o3)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
(%i4) blue: make_level_picture(matrix([123,82],[45,32.5698]));
(%o4)          picture(level, 2, 2, {Array:  #(123 82 45 33)})
(%i5) make_rgb_picture(red,green,blue);
(%o5) picture(rgb, 2, 2, 
              {Array:  #(3 54 123 2 23 82 7 73 45 255 0 33)})
```

<!-- category: Plotting -->
<!-- keywords: mesh -->
<!-- signatures: mesh(fila_1, fila_2, ...) -->
### Function: mesh (fila_1, fila_2, ...)

Dibuja un enrejado cuadrangular en 3D.


**3D**


El argumento *fila_i* es una lista de *n* puntos en 3D de la forma
`[[x_i1,y_i1,z_i1], ...,[x_in,y_in,z_in]]`, siendo todas las filas de
igual longitud. Todos estos puntos definen una superficie arbitraria en 3D.
En cierto sentido, se trata de una generalización del objeto `elevation_grid`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `line_type`, 
`line_width`, `color`, `key`, `wired_surface`, `enhanced3d` y `transform`.


Ejemplos:


Un sencillo ejemplo.



```maxima
(%i1) load("draw")$
(%i2) draw3d( 
         mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
              [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
              [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
```


Dibujando un triángulo en 3D.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        line_width = 2,
        mesh([[1,0,0],[0,1,0]],
             [[0,0,1],[0,0,1]])) $
```


Dos cuadriláteros.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        surface_hide = true,
        line_width   = 3,
        color = red,
        mesh([[0,0,0], [0,1,0]],
             [[2,0,2], [2,2,2]]),
        color = blue,
        mesh([[0,0,2], [0,1,2]],
             [[2,0,4], [2,2,4]])) $
```

<!-- category: Plotting -->
<!-- keywords: multiplot_mode -->
<!-- signatures: multiplot_mode(term) -->
### Function: multiplot_mode (term)

Esta función permite a Maxima trabajar en modo de gráficos múltiples en
una sola ventana del terminal *term*; argumentos válidos para esta función 
son `screen`, `wxt`, `aquaterm` y `none`.


Cuando el modo de gráficos múltiples está activo, cada llamada a `draw`
envía un nuevo gr’afico a la misma ventana, sin borrar los anteriores.
Para desactivar el modo de gráficos múltiples escríbase
`multiplot_mode(none)`.


Cuando el modo de gráficos múltiples está activo, la opción global `terminal` 
se bloquea; para desbloquearla y cambiar de terminal es necesario desactivar 
previamente el modo de gráficos múltiples.


Este modo de trabajo no funciona en plataformas Windows.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) set_draw_defaults(
         xrange = [-1,1],
         yrange = [-1,1],
         grid   = true,
         title  = "Step by step plot" )$
(%i3) multiplot_mode(screen)$
(%i4) draw2d(color=blue,  explicit(x^2,x,-1,1))$
(%i5) draw2d(color=red,   explicit(x^3,x,-1,1))$
(%i6) draw2d(color=brown, explicit(x^4,x,-1,1))$
(%i7) multiplot_mode(none)$
```

<!-- category: Plotting -->
<!-- keywords: negative_picture -->
<!-- signatures: negative_picture(pic) -->
### Function: negative_picture (pic)

Devuelve el negativo de la imagen, sea ésta de tipo nivel (*level*)
o color (*rgb*).

<!-- category: Plotting -->
<!-- keywords: numbered_boundaries -->
<!-- signatures: numbered_boundaries(nlist) -->
### Function: numbered_boundaries (nlist)

Dibuja una lista de segmentos poligonales (líneas 
fronterizas), etiquetadas con sus números correspondientes
(coordenadas de `boundaries_array`). Esta función es
de mucha ayuda a la hora de definir nuevas entidades
geográficas.


Ejemplo:


Mapa de Europa con las fronteras y costas etiquetadas con
su componente numérica de `boundaries_array`.


```maxima
(%i1) load("worldmap")$
(%i2) european_borders: 
           region_boundaries(-31.81,74.92,49.84,32.06)$
(%i3) numbered_boundaries(european_borders)$
```

<!-- category: Plotting -->
<!-- keywords: parametric -->
<!-- signatures: parametric(xfun, yfun, par, parmin, parmax), parametric(xfun, yfun, zfun, par, parmin, parmax) -->
### Function: parametric (xfun, yfun, par, parmin, parmax)

Dibuja funciones paramétricas en 2D y 3D.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `nticks`, 
`line_width`, `line_type`, `key`, `color` y `enhanced3d`.


**2D**


`parametric (xfun,yfun,par,parmin,parmax)` dibuja la función paramétrica 
`[xfun,yfun]`, con el parámetro *par* tomando valores desde 
*parmin* hasta *parmax*.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(x),x,-1,3),
             color = red,
             key   = "This is the parametric one!!",
             parametric(2*cos(rrr),rrr^2,rrr,0,2*%pi))$
```


**3D**


`parametric (xfun,yfun,zfun,par,parmin,parmax)` 
dibuja la curva paramétrica `[xfun,yfun,zfun]`, con el parámetro
*par* tomando valores desde *parmin* hasta *parmax*.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3),
             color = royalblue,
             parametric(cos(5*u)^2,sin(7*u),u-2,u,0,2),
             color      = turquoise,
             line_width = 2,
             parametric(t^2,sin(t),2+t,t,0,2),
             surface_hide = true,
             title = "Surface & curves" )$
```

<!-- category: Plotting -->
<!-- keywords: parametric_surface -->
<!-- signatures: parametric_surface(xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max) -->
### Function: parametric_surface (xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max)

Dibuja superficies paramétricas en 3D.


**3D**


`parametric_surface (xfun,yfun,zfun,par1,par1min,par1max,par2,par2min,par2max)`
dibuja la superficie paramétrica `[xfun,yfun,zfun]`, 
con el parámetro *par1* tomando valores desde *par1min* hasta *par1max*
y el parámetro *par2* tomando valores desde *par2min* hasta *par2max*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `draw_realpart`, `xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`
y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(title          = "Sea shell",
             xu_grid        = 100,
             yv_grid        = 25,
             view           = [100,20],
             surface_hide   = true,
             parametric_surface(0.5*u*cos(u)*(cos(v)+1),
                           0.5*u*sin(u)*(cos(v)+1),
                           u*sin(v) - ((u+3)/8*%pi)^2 - 20,
                           u, 0, 13*%pi, v, -%pi, %pi) )$
```

<!-- category: Plotting -->
<!-- keywords: picture_equalp -->
<!-- signatures: picture_equalp(x, y) -->
### Function: picture_equalp (x, y)

Devuelve `true` si los dos argumentos son imágenes idénticas,
o `false` en caso contrario.

<!-- category: Plotting -->
<!-- keywords: picturep -->
<!-- signatures: picturep(x) -->
### Function: picturep (x)

Devuelve `true` si el argumento es una imagen bien formada,
o `false` en caso contrario.

<!-- category: Plotting -->
<!-- keywords: point_size -->
<!-- signatures: point_size -->
### Variable: point_size

Valor por defecto: 1


`point_size` establece el tamaño de los puntos dibujados. Debe
ser un número no negativo.


Esta opción no tiene efecto alguno cuando a la opción gráfica
`point_type` se le ha dado el valor `dot`.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        points(makelist([random(20),random(50)],k,1,10)),
        point_size = 5,
        points(makelist(k,k,1,20),makelist(random(30),k,1,20)))$
```

<!-- category: Plotting -->
<!-- keywords: points -->
<!-- signatures: points([[x1, y1], [x2, y2], ...]), points([x1, x2, ...], [y1, y2, ...]), points([y1, y2, ...]), points([[x1, y1, z1], [x2, y2, z2], ...]), points([x1, x2, ...], [y1, y2, ...], [z1, z2, ...]), points(matrix), points(1d_y_array), points(1d_x_array, 1d_y_array), points(1d_x_array, 1d_y_array, 1d_z_array), points(2d_xy_array), points(2d_xyz_array) -->
### Function: points ([[x1, y1], [x2, y2], ...])

Dibuja puntos en 2D y 3D.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `point_size`, 
`point_type`, `points_joined`, `line_width`, `key`,
`line_type` y `color`. En modo 3D también se ve afectado por `enhanced3d`.


**2D**


`points ([[x1,y1], [x2,y2],...])` o 
`points ([x1,x2,...], [y1,y2,...])`
dibuja los puntos `[x1,y1]`, `[x2,y2]`, etc. Si no se dan las abscisas,
éstas se asignan automáticamente a enteros positivos consecutivos, de forma que
`points([y1,y2,...])` dibuja los puntos `[1,y1]`, `[2,y2]`, etc.
Si *matrix* es una matriz de dos columnas o de dos filas, `points (matrix)`
dibuja los puntos asociados.


Si *1d_y_array* es un array lisp de números en 1D, `points (1d_y_array)`
los dibujará asignando las abscisas a números enteros consecutivos.
`points (1d_x_array, 1d_y_array)` dibuja los puntos cuyas coordenadas
se toman de los dos arrays pasados como argumentos. Si *2d_xy_array* es un array lisp
2D de dos filas, o de dos columnas, `points (2d_xy_array)` dibuja los correspondientes
puntos del plano.


Ejemplos:


Dos tipos de argumentos para `points`, una lista de pares ordenados
y dos listas con las coordenadas separadas.


```maxima
(%i1) load("draw")$
(%i2) draw2d(
        key = "Small points",
        points(makelist([random(20),random(50)],k,1,10)),
        point_type    = circle,
        point_size    = 3,
        points_joined = true,
        key           = "Great points",
        points(makelist(k,k,1,20),makelist(random(30),k,1,20)),
        point_type    = filled_down_triangle,
        key           = "Automatic abscissas",
        color         = red,
        points([2,12,8]))$
```


Dibujando impulsos.


```maxima
(%i1) load("draw")$
(%i2) draw2d(
        points_joined = impulses,
        line_width    = 2,
        color         = red,
        points(makelist([random(20),random(50)],k,1,10)))$
```


Array con ordenadas.


```maxima
(%i1) load("draw")$
(%i2) a: make_array (flonum, 100) $
(%i3) for i:0 thru 99 do a[i]: random(1.0) $
(%i4) draw2d(points(a)) $
```


Dos arrays con coordenadas separadas.


```maxima
(%i1) load("draw")$
(%i2) x: make_array (flonum, 100) $
(%i3) y: make_array (fixnum, 100) $
(%i4) for i:0 thru 99 do (
        x[i]: float(i/100),
        y[i]: random(10) ) $
(%i5) draw2d(points(x, y)) $
```


Un array 2D de dos columnas.


```maxima
(%i1) load("draw")$
(%i2) xy: make_array(flonum, 100, 2) $
(%i3) for i:0 thru 99 do (
        xy[i, 0]: float(i/100),
        xy[i, 1]: random(10) ) $
(%i4) draw2d(points(xy)) $
```


Dibujando un array rellenado con la función `read_array`.


```maxima
(%i1) load("draw")$
(%i2) a: make_array(flonum,100) $
(%i3) read_array (file_search ("pidigits.data"), a) $
(%i4) draw2d(points(a)) $
```


**3D**


`points ([[x1,y1,z1], [x2,y2,z2],...])` o 
`points ([x1,x2,...], [y1,y2,...], [z1,z2,...])`
dibuja los puntos `[x1,y1,z1]`, `[x2,y2,z2]`, etc.
Si *matrix* es una matriz de tres columnas o de tres filas, `points (matrix)`
dibuja los puntos asociados. Si *matrix* es una matriz columna o fila, las abscisas 
se asignan automáticamente. 


En caso de que los argumentos sean arrays lisp, `points (1d_x_array, 1d_y_array, 1d_z_array)`
toma las coordenadas de los tres arrays unidimensionales. Si *2d_xyz_array* es un array 2D de tres columnas,
o de tres filas, entonces `points (2d_xyz_array)` dibuja los puntos correspondientes.


Ejemplos:


Una muestra tridimensional,


```maxima
(%i1) load("draw")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) draw3d(title = "Daily average wind speeds",
             point_size = 2,
             points(args(submatrix (s2, 4, 5))) )$
```


Dos muestras tridimensionales,


```maxima
(%i1) load("draw")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) draw3d(
         title = "Daily average wind speeds. Two data sets",
         point_size = 2,
         key        = "Sample from stations 1, 2 and 3",
         points(args(submatrix (s2, 4, 5))),
         point_type = 4,
         key        = "Sample from stations 1, 4 and 5",
         points(args(submatrix (s2, 2, 3))) )$
```


Arrays unidimensionales,


```maxima
(%i1) load("draw")$
(%i2) x: make_array (fixnum, 10) $
(%i3) y: make_array (fixnum, 10) $
(%i4) z: make_array (fixnum, 10) $
(%i5) for i:0 thru 9 do (
        x[i]: random(10),
        y[i]: random(10),
        z[i]: random(10) ) $
(%i6) draw3d(points(x,y,z)) $
```


Array bidimensional coloreado,


```maxima
(%i1) load("draw")$
(%i2) xyz: make_array(fixnum, 10, 3) $
(%i3) for i:0 thru 9 do (
        xyz[i, 0]: random(10),
        xyz[i, 1]: random(10),
        xyz[i, 2]: random(10) ) $
(%i4) draw3d(
         enhanced3d = true,
         points_joined = true,
         points(xyz)) $
```


Números de colores especificados explícitamente
por el usuario.


```maxima
(%i1) load("draw")$
(%i2) pts: makelist([t,t^2,cos(t)], t, 0, 15)$
(%i3) col_num: makelist(k, k, 1, length(pts))$
(%i4) draw3d(
        enhanced3d = ['part(col_num,k),k],
        point_size = 3,
        point_type = filled_circle,
        points(pts))$
```

<!-- category: Plotting -->
<!-- keywords: points_joined -->
<!-- signatures: points_joined -->
### Variable: points_joined

Valor por defecto: `false`


Cuando `points_joined` vale `true`, los puntos se unen con segmentos;
si vale `false`, se dibujarán puntos aislados. Un tercer valor posible
para esta opción gráfica es `impulses`; en tal caso, se dibujarán
segmentos verticales desde los puntos hasta el eje-x (2D) o hasta el plano-xy (3D).


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange        = [0,10],
             yrange        = [0,4],
             point_size    = 3,
             point_type    = up_triangle,
             color         = blue,
             points([[1,1],[5,1],[9,1]]),
             points_joined = true,
             point_type    = square,
             line_type     = dots,
             points([[1,2],[5,2],[9,2]]),
             point_type    = circle,
             color         = red,
             line_width    = 7,
             points([[1,3],[5,3],[9,3]]) )$
```

<!-- category: Plotting -->
<!-- keywords: polar -->
<!-- signatures: polar(radius, ang, minang, maxang) -->
### Function: polar (radius, ang, minang, maxang)

Dibuja funciones 2D definidas en coordenadas polares.


**2D**


`polar (radius,ang,minang,maxang)` dibuja la función
`radius(ang)` definida en coordenadas polares, con la variable 
*ang* tomando valores desde *minang* hasta *maxang*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `nticks`, 
`line_width`, `line_type`, `key` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(user_preamble = "set grid polar",
             nticks        = 200,
             xrange        = [-5,5],
             yrange        = [-5,5],
             color         = blue,
             line_width    = 3,
             title         = "Hyperbolic Spiral",
             polar(10/theta,theta,1,10*%pi) )$
```

<!-- category: Plotting -->
<!-- keywords: polygon -->
<!-- signatures: polygon([[x1, y1], [x2, y2], ...]), polygon([x1, x2, ...], [y1, y2, ...]) -->
### Function: polygon ([[x1, y1], [x2, y2], ...])

Dibuja polígonos en 2D.


**2D**


`polygon ([[x1,y1], [x2,y2],...])` o 
`polygon ([x1,x2,...], [y1,y2,...])`:
dibuja en el plano un polígono de vértices 
`[x1,y1]`, `[x2,y2]`, etc..


Este objeto se ve afectado por las siguientes *opciones gráficas*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`,
 `line_type` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(color      = "#e245f0",
             line_width = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = yellow,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: proportional_axes -->
<!-- signatures: proportional_axes -->
### Variable: proportional_axes

Valor por defecto: `none`


Cuando `proportional_axes` es igual a `xy` o `xy`, una escena
2D o 3D se dibujará con los ejes proporcionales a sus longitudes relativas.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Esta opción sólo funciona con Gnuplot versión 4.2.6
o superior.


Ejemplos:


Gráfico en 2D.



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        ellipse(0,0,1,1,0,360),
        transparent=true,
        color = blue,
        line_width = 4,
        ellipse(0,0,2,1/2,0,360),
        proportional_axes = xy) $
```


Multiplot.



```maxima
(%i1) load("draw")$
(%i2) draw(
        terminal = wxt,
        gr2d(proportional_axes = xy,
             explicit(x^2,x,0,1)),
        gr2d(explicit(x^2,x,0,1),
             xrange = [0,1],
             yrange = [0,2],
             proportional_axes=xy),
        gr2d(explicit(x^2,x,0,1)))$
```

<!-- category: Plotting -->
<!-- keywords: quadrilateral -->
<!-- signatures: quadrilateral(point_1, point_2, point_3, point_4) -->
### Function: quadrilateral (point_1, point_2, point_3, point_4)

Dibuja un cuadrilátero.


**2D**


`quadrilateral ([x1,y1], [x2,y2], [x3,y3], [x4,y4])` dibuja un cuadrilátero de vértices `[x1,y1]`, 
`[x2,y2]`, `[x3,y3]` y `[x4,y4]`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`, `xaxis_secondary`, 
`yaxis_secondary`, `line_type`, `transform` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        quadrilateral([1,1],[2,2],[3,-1],[2,-2]))$
```


**3D**


`quadrilateral ([x1,y1,z1], [x2,y2,z2], [x3,y3,z3], [x4,y4,z4])` dibuja un cuadrilátero de vértices
`[x1,y1,z1]`, `[x2,y2,z2]`,
`[x3,y3,z3]` y `[x4,y4,z4]`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `line_type`, 
`line_width`, `color`, `key`, `enhanced3d` y `transform`.

<!-- category: Plotting -->
<!-- keywords: read_xpm -->
<!-- signatures: read_xpm(xpm_file) -->
### Function: read_xpm (xpm_file)

Lee el fichero gráfico en formato xpm y devuelve un objeto `picture`.

<!-- category: Plotting -->
<!-- keywords: rectangle -->
<!-- signatures: rectangle([x1, y1], [x2, y2]) -->
### Function: rectangle ([x1, y1], [x2, y2])

Dibuja rectángulos en 2D.


**2D**


`rectangle ([x1,y1], [x2,y2])` dibuja un rectángulo de vértices opuestos
`[x1,y1]` y `[x2,y2]`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`,
`line_type` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = red,
             line_width  = 6,
             line_type   = dots,
             transparent = false,
             fill_color  = blue,
             rectangle([-2,-2],[8,-1]), /* opposite vertices */
             transparent = true,
             line_type   = solid,
             line_width  = 1,
             rectangle([9,4],[2,-1.5]),
             xrange      = [-3,10],
             yrange      = [-3,4.5] )$
```

<!-- category: Plotting -->
<!-- keywords: region -->
<!-- signatures: region(expr, var1, minval1, maxval1, var2, minval2, maxval2) -->
### Function: region (expr, var1, minval1, maxval1, var2, minval2, maxval2)

Dibuja una región del plano definida por desigualdades.


**2D**
*expr* es una expresión formada por desigualdades y los operadores lógicos
`and`, `or` y `not`. La región está acotada por el rectángulo
definido por $[minval1, maxval1]$ y
$[minval2, maxval2]$.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `fill_color`, 
`key`, `x_voxel` y `y_voxel`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        x_voxel = 30,
        y_voxel = 30,
        region(x^2+y^2<1 and x^2+y^2 > 1/2,
               x, -1.5, 1.5, y, -1.5, 1.5));
```

<!-- category: Plotting -->
<!-- keywords: region_boundaries -->
<!-- signatures: region_boundaries(x1, y1, x2, y2) -->
### Function: region_boundaries (x1, y1, x2, y2)

Detecta los segmentos poligonales almacenados en la variable global
`boundaries_array` totalmente contenidos en el rectángulo de vértices
(*x1*,*y1*) -superior izquierdo- y (*x2*,*y2*)
-inferior derecho-.


Ejemplo:


Devuelve los números de los segmentos necesarios para
dibujar el sur de Italia.


```maxima
(%i1) load("worldmap")$
(%i2) region_boundaries(10.4,41.5,20.7,35.4);
(%o2)                [1846, 1863, 1864, 1881, 1888, 1894]
(%i3) draw2d(geomap(%))$
```

<!-- category: Plotting -->
<!-- keywords: region_boundaries_plus -->
<!-- signatures: region_boundaries_plus(x1, y1, x2, y2) -->
### Function: region_boundaries_plus (x1, y1, x2, y2)

Detecta los segmentos poligonales almacenados en la variable global
`boundaries_array` con al menos un vértice dentro del rectángulo 
definido por los extremos (*x1*,*y1*) -superior izquierdo- y (*x2*,*y2*)
-inferior derecho-.


Ejemplo:



```maxima
(%i1) load("worldmap")$
(%i2) region_boundaries_plus(10.4,41.5,20.7,35.4);
(%o2) [1060, 1062, 1076, 1835, 1839, 1844, 1846, 1858,
       1861, 1863, 1864, 1871, 1881, 1888, 1894, 1897]
(%i3) draw2d(geomap(%))$
```

<!-- category: Plotting -->
<!-- keywords: rgb2level -->
<!-- signatures: rgb2level(pic) -->
### Function: rgb2level (pic)

Transforma una imagen en color *rgb* a otra de niveles *level*
promediando los niveles.

<!-- category: Plotting -->
<!-- keywords: set_draw_defaults -->
<!-- signatures: set_draw_defaults(Opción gráfica, ..., Opción gráfica, ...) -->
### Function: set_draw_defaults (Opción gráfica, ..., Opción gráfica, ...)

Establece las opciones gráficas de usuario. Esta función es útil 
para dibujar varios gráficos con las mismas opciones. Llamando
a la función sin argumentos se borran las opciones de usuario por defecto.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) set_draw_defaults(
         xrange = [-10,10],
         yrange = [-2, 2],
         color  = blue,
         grid   = true)$
(%i3) /* dibujo con opciones de usuario */
      draw2d(explicit(((1+x)**2/(1+x*x))-1,x,-10,10))$
(%i4) set_draw_defaults()$
(%i5) /* dibujo con opciones por defecto */
      draw2d(explicit(((1+x)**2/(1+x*x))-1,x,-10,10))$
```


Para utilizar esta función, ejecútese primero `load("draw")`.

<!-- category: Plotting -->
<!-- keywords: spherical -->
<!-- signatures: spherical(radius, azi, minazi, maxazi, zen, minzen, maxzen) -->
### Function: spherical (radius, azi, minazi, maxazi, zen, minzen, maxzen)

Dibuja funciones 3D definidas en coordenadas esféricas.


**3D**


`spherical (radius,azi,minazi,maxazi,zen,minzen,maxzen)`
dibuja la función `radius(azi,zen)` definida en coordenadas esféricas, con el *azimut*
*azi* tomando valores desde *minazi* hasta *maxazi* y el *zenit* *zen* tomando valores desde
*minzen* hasta *maxzen*.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `xu_grid`, 
`yv_grid`, `line_type`, `key`, `wired_surface`, `enhanced3d` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(spherical(1,a,0,2*%pi,z,0,%pi))$
```

<!-- category: Plotting -->
<!-- keywords: surface_hide -->
<!-- signatures: surface_hide -->
### Variable: surface_hide

Valor por defecto: `false`


Cuando `surface_hide` vale `true`, las partes ocultas no
se muestran en las superficies de las escenas 3d.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw(columns=2,
           gr3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)),
           gr3d(surface_hide = true,
                explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)) )$
```

<!-- category: Plotting -->
<!-- keywords: take_channel -->
<!-- signatures: take_channel(im, color) -->
### Function: take_channel (im, color)

Si el argumento *color* es `red`, `green` o `blue`,
la función `take_channel` devuelve el canal de color correspondiente
de la imagen *im*.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) red: make_level_picture(matrix([3,2],[7,260]));
(%o2)           picture(level, 2, 2, {Array:  #(3 2 7 255)})
(%i3) green: make_level_picture(matrix([54,23],[73,-9]));
(%o3)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
(%i4) blue: make_level_picture(matrix([123,82],[45,32.5698]));
(%o4)          picture(level, 2, 2, {Array:  #(123 82 45 33)})
(%i5) make_rgb_picture(red,green,blue);
(%o5) picture(rgb, 2, 2, 
              {Array:  #(3 54 123 2 23 82 7 73 45 255 0 33)})
(%i6) take_channel(%,'green);  /* simple quote!!! */
(%o6)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
```

<!-- category: Plotting -->
<!-- keywords: terminal -->
<!-- signatures: terminal -->
### Variable: terminal

Valor por defecto: `screen`


Selecciona el terminal a utilizar por Gnuplot; valores posibles son:
`screen` (por defecto), `png`, `pngcairo`, `jpg`, `gif`, 
`eps`, `eps_color`, `epslatex`, `epslatex_standalone`, 
`svg`, `dumb`, `dumb_file`, `pdf`, `pdfcairo`, 
`wxt`, `animated_gif`, `multipage_pdfcairo`, `multipage_pdf`, 
`multipage_eps`, `multipage_eps_color` y `aquaterm`.


Los terminales `screen`, `wxt` y `aquaterm` también se pueden 
definir como una lista de dos elementos: el propio nombre del terminal y un 
número entero no negativo. De esta forma se pueden abrir varias ventanas al
mismo tiempo, cada una de ellas con su número correspondiente. Esta modalidad
no funciona en plataformas Windows.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia. También puede
usarse como argumento de la función `draw`.


pdfcairo necesita Gnuplot 4.3. 
`pdf` necesita que Gnuplot haya sido compilado con la opción `--enable-pdf` y libpdf debe
estar instalado ([http://www.pdflib.com/en/download/pdflib-family/pdflib-lite/]()).


Ejemplos:



```maxima
(%i1) load("draw")$
(%i2) /* screen terminal (default) */
      draw2d(explicit(x^2,x,-1,1))$
(%i3) /* png file */
      draw2d(terminal  = 'png,
             explicit(x^2,x,-1,1))$
(%i4) /* jpg file */
      draw2d(terminal   = 'jpg,
             dimensions = [300,300],
             explicit(x^2,x,-1,1))$
(%i5) /* eps file */
      draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'eps)$
(%i6) /* pdf file */
      draw2d(file_name = "mypdf",
             dimensions = 100*[12.0,8.0],
             explicit(x^2,x,-1,1),
             terminal  = 'pdf)$
(%i7) /* wxwidgets window */
      draw2d(explicit(x^2,x,-1,1),
             terminal  = 'wxt)$
```


Ventanas múltiples.


```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^5,x,-2,2), terminal=[screen, 3])$
(%i3) draw2d(explicit(x^2,x,-2,2), terminal=[screen, 0])$
```


Un fichero gif animado.


```maxima
(%i1) load("draw")$
(%i2) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


La opción `delay` sólo se activa en caso de gifs animados; se ignora en
cualquier otro caso.


Salida multipágina en formato eps.


```maxima
(%i1) load("draw")$
(%i2) draw(
        file_name = "parabol",
        terminal  = multipage_eps,
        dimensions = 100*[10,10],
        gr2d(explicit(x^2,x,-1,1)),
        gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1))) $
```


Véanse también `file_name`, `pic_width`, `pic_height` y `delay`.

<!-- category: Plotting -->
<!-- keywords: title -->
<!-- signatures: title -->
### Variable: title

Valor por defecto: `""` (cadena vacía)


La opción `title` almacena una cadena con el 
título de la escena. Por defecto, no se escribe
título alguno.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(u),u,-2,2),
             title = "Exponential function")$
```

<!-- category: Plotting -->
<!-- keywords: transform -->
<!-- signatures: transform -->
### Variable: transform

Valor por defecto: `none`


Si `transform` vale `none`, el espacio no sufre transformación
alguna y los objetos gráficos se representan tal cual se definen. Si es
necesario transformar el espacio, se debe asignar una lista a la opción
`transform`. En caso de una escena 2D, la lista toma la forma
`[f1(x,y), f2(x,y), x, y]`.
En caso de una escena 3D, la lista debe ser de la forma
`[f1(x,y,z), f2(x,y,z), f3(x,y,z), x, y, z]`.


Los nombres de las variables definidas en las listas pueden ser diferentes
de aquellas utilizadas en las definiciones de los objetos gráficos.


Ejemplos:


Rotación en 2D.



```maxima
(%i1) load("draw")$
(%i2) th : %pi / 4$
(%i3) draw2d(
        color = "#e245f0",
        proportional_axes = 'xy,
        line_width = 8,
        triangle([3,2],[7,2],[5,5]),
        border     = false,
        fill_color = yellow,
        transform  = [cos(th)*x - sin(th)*y,
                      sin(th)*x + cos(th)*y, x, y],
        triangle([3,2],[7,2],[5,5]) )$
```


Traslación en 3D.



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        color     = "#a02c00",
        explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
        transform = [x+10,y+10,z+10,x,y,z],
        color     = blue,
        explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3) )$
```

<!-- category: Plotting -->
<!-- keywords: transparent -->
<!-- signatures: transparent -->
### Variable: transparent

Valor por defecto: `false`


Cuando `transparent` vale `false`, las regiones internas de 
los polígonos se rellenan de acuerdo con `fill_color`.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr2d`: `polygon`, `rectangle` y `ellipse`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(polygon([[3,2],[7,2],[5,5]]),
             transparent = true,
             color       = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: triangle -->
<!-- signatures: triangle(punto_1, punto_2, punto_3) -->
### Function: triangle (punto_1, punto_2, punto_3)

Dibuja un triángulo.


**2D**


`triangle ([x1,y1], [x2,y2], [x3,y3])` dibuja
un triángulo de vértices `[x1,y1]`, `[x2,y2]` y
`[x3,y3]`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`, `xaxis_secondary`, 
`yaxis_secondary`, `line_type`, `transform` y `color`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        triangle([1,1],[2,2],[3,-1]))$
```


**3D**


`triangle ([x1,y1,z1], [x2,y2,z2], [x3,y3,z3])` dibuja un triángulo de vértices `[x1,y1,z1]`,
`[x2,y2,z2]` y `[x3,y3,z3]`.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `line_type`, 
`line_width`, `color`, `key`, `enhanced3d` y `transform`.

<!-- category: Plotting -->
<!-- keywords: tube -->
<!-- signatures: tube(xfun, yfun, zfun, rfun, p, pmin, pmax) -->
### Function: tube (xfun, yfun, zfun, rfun, p, pmin, pmax)

Dibuja un tubo en 3D de diámetro variable.


**3D**


`[xfun,yfun,zfun]`
es la curva paramétrica de parámetro *p*, el cual toma valores entre
*pmin* y *pmax*. Se colocan círculos de radio *rfun*
con sus centros sobre la curva paramétrica y perpendiculares a ella.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`,
`color` y `capping`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        enhanced3d = true,
        xu_grid    = 50,
        tube(cos(a), a, 0, cos(a/10)^2,
             a, 0, 4*%pi) )$
```

<!-- category: Plotting -->
<!-- keywords: unit_vectors -->
<!-- signatures: unit_vectors -->
### Variable: unit_vectors

Valor por defecto: `false`


Cuando `unit_vectors` vale `true`, los vectores se dibujan con módulo unidad.
Esta opción es útil para representar campos vectoriales. Cuando `unit_vectors` vale `false`,
los vectores se dibujan con su longitud original.


Esta opción sólo es relevante para objetos de tipo `vector`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [-1,6],
             yrange      = [-1,6],
             head_length = 0.1,
             vector([0,0],[5,2]),
             unit_vectors = true,
             color        = red,
             vector([0,3],[5,2]))$
```

<!-- category: Plotting -->
<!-- keywords: user_preamble -->
<!-- signatures: user_preamble -->
### Variable: user_preamble

Valor por defecto: `""` (cadena vacía)


Usuarios expertos en Gnuplot pueden hacer uso de esta opción para
afinar el comportamiento de Gnuplot escribiendo código que será
enviado justo antes de la instrucción `plot` o `splot`.


El valor dado a esta opción debe ser una cadena alfanumérica o
una lista de cadenas (una por línea).


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:


Se le indica a Gnuplot que dibuje los ejes encima de todos los demás objetos,


```maxima
(%i1) load("draw")$
(%i2) draw2d(
        xaxis =true, xaxis_type=solid,
        yaxis =true, yaxis_type=solid,
        user_preamble="set grid front",
        region(x^2+y^2<1 ,x,-1.5,1.5,y,-1.5,1.5))$
```

<!-- category: Plotting -->
<!-- keywords: vector -->
<!-- signatures: vector([x, y], [dx, dy]), vector([x, y, z], [dx, dy, dz]) -->
### Function: vector ([x, y], [dx, dy])

Dibuja vectores en 2D y 3D.


Este objeto se ve afectado por las siguientes *opciones gráficas*: `head_both`, 
`head_length`, `head_angle`, `head_type`, `line_width`, 
`line_type`, `key` y `color`.


**2D**


`vector ([x,y], [dx,dy])` dibuja el vector 
`[dx,dy]` con origen en `[x,y]`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,12],
             yrange      = [0,10],
             head_length = 1,
             vector([0,1],[5,5]), /* default type */
             head_type = 'empty,
             vector([3,1],[5,5]),
             head_both = true,
             head_type = 'nofilled,
             line_type = dots,
             vector([6,1],[5,5]))$
```


**3D**


`vector([x,y,z], [dx,dy,dz])`
dibuja el vector `[dx,dy,dz]` con 
origen en `[x,y,z]`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(color = cyan,
             vector([0,0,0],[1,1,1]/sqrt(3)),
             vector([0,0,0],[1,-1,0]/sqrt(2)),
             vector([0,0,0],[1,1,-2]/sqrt(6)) )$
```

<!-- category: Plotting -->
<!-- keywords: view -->
<!-- signatures: view -->
### Variable: view

Valor por defecto: `[60,30]`


Un par de ángulos, medidos en grados, indicando la direcciÃ³n del 
observador en una escena 3D. El primer ángulo es la rotación 
vertical alrededor del eje *x*, dentro del intervalo $[0, 360]$.
El segundo es la rotación horizontal alrededor del eje *z*, dentro
del intervalo $[0, 360]$.


Dándole a la opción `view` el valor `map`, la dirección del 
observador se sitúa perpendicularmente al plano-xy.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(view = [170, 50],
             enhanced3d = true,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
(%i3) draw3d(view = map,
             enhanced3d = true,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```

<!-- category: Plotting -->
<!-- keywords: wired_surface -->
<!-- signatures: wired_surface -->
### Variable: wired_surface

Valor por defecto: `false`


Indica si las superficies en 3D en modo `enhanced3d` deben mostrar o no la malla que
unen los puntos.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        enhanced3d    = [sin(x),x,y],
        wired_surface = true,
        explicit(x^2+y^2,x,-1,1,y,-1,1)) $
```

<!-- category: Plotting -->
<!-- keywords: x_voxel -->
<!-- signatures: x_voxel -->
### Variable: x_voxel

Valor por defecto: 10


`x_voxel` es el número de voxels en la dirección x a utilizar
por el algoritmo *marching cubes* implementado por el objeto 
`implicit` tridimensional. También se utiliza como opción
del objeto gráfico `region`.

<!-- category: Plotting -->
<!-- keywords: xaxis -->
<!-- signatures: xaxis -->
### Variable: xaxis

Valor por defecto: `false`


Si `xaxis` vale `true`, se dibujará el eje *x*.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_color = blue)$
```


Véanse también `xaxis_width`, `xaxis_type` y `xaxis_color`.

<!-- category: Plotting -->
<!-- keywords: xaxis_color -->
<!-- signatures: xaxis_color -->
### Variable: xaxis_color

Valor por defecto: `"black"`


`xaxis_color` especifica el color para el eje *x*. Véase
`color` para ver cómo se definen los colores.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_color = red)$
```


Véanse también `xaxis`, `xaxis_width` y `xaxis_type`.

<!-- category: Plotting -->
<!-- keywords: xaxis_secondary -->
<!-- signatures: xaxis_secondary -->
### Variable: xaxis_secondary

Valor por defecto: `false`


Si `xaxis_secondary` vale `true`, los valores de las funciones se pueden representar
respecto del eje *x* secundario, el cual se dibuja en la parte superior de la escena.


Nótese que esta es una opción gráfica local que sólo afecta a objetos 2d.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         key   = "Bottom x-axis",
         explicit(x+1,x,1,2),
         color = red,
         key   = "Above x-axis",
         xtics_secondary = true,
         xaxis_secondary = true,
         explicit(x^2,x,-1,1)) $
```


Véanse también `xrange_secondary`, `xtics_secondary`, `xtics_rotate_secondary`,
`xtics_axis_secondary` y `xaxis_secondary`.

<!-- category: Plotting -->
<!-- keywords: xaxis_type -->
<!-- signatures: xaxis_type -->
### Variable: xaxis_type

Valor por defecto: `dots`


`xaxis_type` indica cómo se debe dibujar el eje *x*; 
valores admisibles son `solid` y `dots`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_type  = solid)$
```


Véanse también `xaxis`, `xaxis_width` y `xaxis_color`.

<!-- category: Plotting -->
<!-- keywords: xaxis_width -->
<!-- signatures: xaxis_width -->
### Variable: xaxis_width

Valor por defecto: 1


`xaxis_width` es el ancho del eje *x*.
Su valor debe ser un número positivo.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_width = 3)$
```


Véanse también `xaxis`, `xaxis_type` y `xaxis_color`.

<!-- category: Plotting -->
<!-- keywords: xlabel_secondary -->
<!-- signatures: xlabel_secondary -->
### Variable: xlabel_secondary

Valor por defecto: `""` (cadena vacía)


La opción `xlabel_secondary` almacena una cadena con la
etiqueta del eje *x* secundario. Por defecto, el eje no tiene etiqueta.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         xaxis_secondary=true,yaxis_secondary=true,
         xtics_secondary=true,ytics_secondary=true,
         xlabel_secondary="t[s]",
         ylabel_secondary="U[V]",
         explicit(sin(t),t,0,10) )$
```


Véanse también `xlabel`, `ylabel`, `ylabel_secondary` y `zlabel`.

<!-- category: Plotting -->
<!-- keywords: xrange -->
<!-- signatures: xrange -->
### Variable: xrange

Valor por defecto: `auto`


Cuando `xrange` vale `auto`, el rango de la coordenada *x*
se calcula de forma automática.


Si el usuario quiere especificar un intervalo para *x*, éste debe
expresarse como una lista de Maxima, como en `xrange=[-2, 3]`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange = [-3,5],
             explicit(x^2,x,-1,1))$
```


Véanse también `yrange` y `zrange`.

<!-- category: Plotting -->
<!-- keywords: xrange_secondary -->
<!-- signatures: xrange_secondary -->
### Variable: xrange_secondary

Valor por defecto: `auto`


Cuando `xrange_secondary` vale `auto`, el rango del eje *x*
secundario se calcula de forma automática.


Si el usuario quiere especificar un intervalo para el eje *x* secundario, éste debe
expresarse como una lista de Maxima, como en `xrange_secondary=[-2, 3]`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Véanse también `xrange`, `yrange`, `zrange` y `yrange_secondary`.

<!-- category: Plotting -->
<!-- keywords: xtics -->
<!-- signatures: xtics -->
### Variable: xtics

Valor por defecto: `true`


Esta opción gráfica controla la forma en la que se dibujarán las marcas
del eje *x*.



- *
Cuando a `xtics` se le da el valor *true*, las marcas se dibujarán de
forma automática.
- *
Cuando a `xtics` se le da el valor *false*, no habrá marcas en los ejes.
- *
Cuando a `xtics` se le da un valor numérico positivo, se interpretará como la
distancia entre dos marcas consecutivas.
- *
Cuando a `xtics` se le da una lista de longitud tres de la forma 
`[start,incr,end]`, las marcas se dibujarán desde `start` 
hasta `end` a intervalos de longitud `incr`.
- *
Cuando a `xtics` se le da un conjunto de números de la forma
`{n1, n2, ...}`, las marcas se dibujarán exactamente en los valores
`n1`, `n2`, ...
- *
Cuando a `xtics` se le da un conjunto de pares de la forma
`{["label1", n1], ["label2", n2], ...}`, las marcas correspondientes a los valores
`n1`, `n2`, ... se etiquetarán con `"label1"`, `"label2"`, ..., respectivamente.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplos:


Marcas desactivadas.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = 'false,
             explicit(x^3,x,-1,1)  )$
```


Marcas cada 1/4 unidades.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = 1/4,
             explicit(x^3,x,-1,1)  )$
```


Marcas desde -3/4 hasta 3/4 en saltos de 1/8.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = [-3/4,1/8,3/4],
             explicit(x^3,x,-1,1)  )$
```


Marcas en los puntos -1/2, -1/4 y 3/4.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = {-1/2,-1/4,3/4},
             explicit(x^3,x,-1,1)  )$
```


Marcas etiquetadas.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = {["High",0.75],["Medium",0],["Low",-0.75]},
             explicit(x^3,x,-1,1)  )$
```

<!-- category: Plotting -->
<!-- keywords: xtics_axis -->
<!-- signatures: xtics_axis -->
### Variable: xtics_axis

Valor por defecto: `false`


Si `xtics_axis` vale `true`, las marcas y sus etiquetas se dibujan sobre
el propio eje *x*, si vale `false` las marcas se colocan a lo largo del borde
del gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: xtics_rotate -->
<!-- signatures: xtics_rotate -->
### Variable: xtics_rotate

Valor por defecto: `false`


Si `xtics_rotate` vale `true`, las marcas del eje *x* se giran 
90 grados.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: xtics_rotate_secondary -->
<!-- signatures: xtics_rotate_secondary -->
### Variable: xtics_rotate_secondary

Valor por defecto: `false`


Si `xtics_rotate_secondary` vale `true`, las marcas del eje *x* 
secundario se giran 90 grados.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: xtics_secondary -->
<!-- signatures: xtics_secondary -->
### Variable: xtics_secondary

Valor por defecto: `auto`


Esta opción gráfica controla la forma en la que se dibujarán las marcas
del eje *x* secundario.


Véase `xtics` para una descripción completa.

<!-- category: Plotting -->
<!-- keywords: xtics_secondary_axis -->
<!-- signatures: xtics_secondary_axis -->
### Variable: xtics_secondary_axis

Valor por defecto: `false`


Si `xtics_secondary_axis` vale `true`, las marcas y sus etiquetas se dibujan sobre
el propio eje *x* secundario, si vale `false` las marcas se colocan a lo largo del borde
del gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: xu_grid -->
<!-- signatures: xu_grid -->
### Variable: xu_grid

Valor por defecto: 30


`xu_grid` es el número de coordenadas de la primera variable
(`x` en superficies explcítas y `u` en las
paramétricas) para formar la rejilla de puntos muestrales.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr3d`: `explicit` y `parametric_surface`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


Véase también `yv_grid`.

<!-- category: Plotting -->
<!-- keywords: xy_file -->
<!-- signatures: xy_file -->
### Variable: xy_file

Valor por defecto: `""` (cadena vacía)


`xy_file` es el nombre del fichero donde se almacenarán las
coordenadas después de hacer clic con el botón del ratón en un
punto de la imagen y pulsado la tecla ’x’. Por defecto, las 
coordenadas no se almacenan.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: xyplane -->
<!-- signatures: xyplane -->
### Variable: xyplane

Valor por defecto: `false`


Coloca el plano-xy en escenas 3D. Si `xyplane` vale `false`,
el plano-xy se coloca automáticamente; en cambio, si toma un
valor real, el plano-xy intersectará con el eje *z* a ese nivel.
Esta opción no tiene efecto alguno en escenas 2D.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xyplane = %e-2,
             explicit(x^2+y^2,x,-1,1,y,-1,1))$
```

<!-- category: Plotting -->
<!-- keywords: y_voxel -->
<!-- signatures: y_voxel -->
### Variable: y_voxel

Valor por defecto: 10


`y_voxel` es el número de voxels en la dirección y a utilizar
por el algoritmo *marching cubes* implementado por el objeto 
`implicit` tridimensional. También se utiliza como opción
del objeto gráfico `region`.

<!-- category: Plotting -->
<!-- keywords: yaxis -->
<!-- signatures: yaxis -->
### Variable: yaxis

Valor por defecto: `false`


Si `yaxis` vale `true`, se dibujará el eje *y*.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_color = blue)$
```


Véanse también `yaxis_width`, `yaxis_type` y `yaxis_color`.

<!-- category: Plotting -->
<!-- keywords: yaxis_color -->
<!-- signatures: yaxis_color -->
### Variable: yaxis_color

Valor por defecto: `"black"`


`yaxis_color` especifica el color para el eje *y*. Véase
`color` para ver cómo se definen los colores.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_color = red)$
```


Véanse también `yaxis`, `yaxis_width` y `yaxis_type`.

<!-- category: Plotting -->
<!-- keywords: yaxis_secondary -->
<!-- signatures: yaxis_secondary -->
### Variable: yaxis_secondary

Valor por defecto: `false`


Si `yaxis_secondary` vale `true`, los valores de las funciones se pueden representar
respecto del eje *y* secundario, el cual se dibuja al lado derecho de la escena.


Nótese que esta es una opción gráfica local que sólo afecta a objetos 2d.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         explicit(sin(x),x,0,10),
         yaxis_secondary = true,
         ytics_secondary = true,
         color = blue,
         explicit(100*sin(x+0.1)+2,x,0,10));
```


Véanse también `yrange_secondary`, `ytics_secondary`, `ytics_rotate_secondary`
y `ytics_axis_secondary`.

<!-- category: Plotting -->
<!-- keywords: yaxis_type -->
<!-- signatures: yaxis_type -->
### Variable: yaxis_type

Valor por defecto: `dots`


`yaxis_type` indica cómo se debe dibujar el eje *y*; 
valores admisibles son `solid` y `dots`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_type  = solid)$
```


Véanse también `yaxis`, `yaxis_width` y `yaxis_color`.

<!-- category: Plotting -->
<!-- keywords: yaxis_width -->
<!-- signatures: yaxis_width -->
### Variable: yaxis_width

Valor por defecto: 1


`yaxis_width` es el ancho del eje *y*.
Su valor debe ser un número positivo.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_width = 3)$
```


Véanse también `yaxis`, `yaxis_type` y `yaxis_color`.

<!-- category: Plotting -->
<!-- keywords: ylabel_secondary -->
<!-- signatures: ylabel_secondary -->
### Variable: ylabel_secondary

Valor por defecto: `""` (cadena vacía)



La opción `ylabel_secondary` almacena una cadena con la
etiqueta del eje *y* secundario. Por defecto, el eje no tiene etiqueta.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        key="current",
        xlabel="t[s]",
        ylabel="I[A]",ylabel_secondary="P[W]",
        explicit(sin(t),t,0,10),
        yaxis_secondary=true,
        ytics_secondary=true,
        color=red,key="Power",
        explicit((sin(t))^2,t,0,10)
    )$
```


Véanse también `xlabel`, `xlabel_secondary`, `ylabel` and `zlabel`.

<!-- category: Plotting -->
<!-- keywords: yrange -->
<!-- signatures: yrange -->
### Variable: yrange

Valor por defecto: `auto`


Cuando `yrange` vale `auto`, el rango de la coordenada *y*
se calcula de forma automática.


Si el usuario quiere especificar un intervalo para *y*, éste debe
expresarse como una lista de Maxima, como en `yrange=[-2, 3]`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(yrange = [-2,3],
             explicit(x^2,x,-1,1),
             xrange = [-3,3])$
```


Véanse también `xrange` y `zrange`.

<!-- category: Plotting -->
<!-- keywords: yrange_secondary -->
<!-- signatures: yrange_secondary -->
### Variable: yrange_secondary

Valor por defecto: `auto`


Cuando `yrange_secondary` vale `auto`, el rango del eje *y*
secundario se calcula de forma automática.


Si el usuario quiere especificar un intervalo para el eje *y* secundario, éste debe
expresarse como una lista de Maxima, como en `yrange_secondary=[-2, 3]`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         explicit(sin(x),x,0,10),
         yaxis_secondary = true,
         ytics_secondary = true,
         yrange = [-3, 3],
         yrange_secondary = [-20, 20],
         color = blue,
         explicit(100*sin(x+0.1)+2,x,0,10)) $
```


Véanse también `xrange`, `yrange` y `zrange`.

<!-- category: Plotting -->
<!-- keywords: ytics -->
<!-- signatures: ytics -->
### Variable: ytics

Valor por defecto: `true`


Esta opción gráfica controla la forma en la que se dibujarán las marcas
del eje *y*.


Véase `xtics` para una descripción completa.

<!-- category: Plotting -->
<!-- keywords: ytics_axis -->
<!-- signatures: ytics_axis -->
### Variable: ytics_axis

Valor por defecto: `false`


Si `ytics_axis` vale `true`, las marcas y sus etiquetas se dibujan sobre
el propio eje *y*, si vale `false` las marcas se colocan a lo largo del borde
del gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: ytics_rotate -->
<!-- signatures: ytics_rotate -->
### Variable: ytics_rotate

Valor por defecto: `false`


Si `ytics_rotate` vale `true`, las marcas del eje *y* se giran 
90 grados.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: ytics_rotate_secondary -->
<!-- signatures: ytics_rotate_secondary -->
### Variable: ytics_rotate_secondary

Valor por defecto: `false`


Si `ytics_rotate_secondary` vale `true`, las marcas del eje *y* 
secundario se giran 90 grados.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: ytics_secondary -->
<!-- signatures: ytics_secondary -->
### Variable: ytics_secondary

Valor por defecto: `auto`


Esta opción gráfica controla la forma en la que se dibujarán las marcas
del eje *y* secundario.


Véase `xtics` para una descripción completa.

<!-- category: Plotting -->
<!-- keywords: ytics_secondary_axis -->
<!-- signatures: ytics_secondary_axis -->
### Variable: ytics_secondary_axis

Valor por defecto: `false`


Si `ytics_secondary_axis` vale `true`, las marcas y sus etiquetas se dibujan sobre
el propio eje *y* secundario, si vale `false` las marcas se colocan a lo largo del borde
del gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: yv_grid -->
<!-- signatures: yv_grid -->
### Variable: yv_grid

Valor por defecto: 30


`yv_grid` es el número de coordenadas de la segunda variable
(`y` en superficies explcítas y `v` en las
paramétricas) para formar la rejilla de puntos muestrales.


Esta opción afecta a los siguientes objetos gráficos:


- *
`gr3d`: `explicit` y `parametric_surface`.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


Véase también `xu_grid`.

<!-- category: Plotting -->
<!-- keywords: z_voxel -->
<!-- signatures: z_voxel -->
### Variable: z_voxel

Valor por defecto: 10


`z_voxel` es el número de voxels en la dirección z a utilizar
por el algoritmo *marching cubes* implementado por el objeto 
`implicit` tridimensional.

<!-- category: Plotting -->
<!-- keywords: zaxis -->
<!-- signatures: zaxis -->
### Variable: zaxis

Valor por defecto: `false`


Si `zaxis` vale `true`, se dibujará el eje *z* en
escenas 3D. Esta opción no tiene efecto alguno en escenas 2D.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_color = blue)$
```


Véanse también `zaxis_width`, `zaxis_type` y `zaxis_color`.

<!-- category: Plotting -->
<!-- keywords: zaxis_color -->
<!-- signatures: zaxis_color -->
### Variable: zaxis_color

Valor por defecto: `"black"`


`zaxis_color` especifica el color para el eje *z*. Véase
`color` para ver cómo se definen los colores.
Esta opción no tiene efecto alguno en escenas 2D.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_color = red)$
```


Véanse también `zaxis`, `zaxis_width` y `zaxis_type`.

<!-- category: Plotting -->
<!-- keywords: zaxis_type -->
<!-- signatures: zaxis_type -->
### Variable: zaxis_type

Valor por defecto: `dots`


`zaxis_type` indica cómo se debe dibujar el eje *z*; 
valores admisibles son `solid` y `dots`.
Esta opción no tiene efecto alguno en escenas 2D.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid)$
```


Véanse también `zaxis`, `zaxis_width` y `zaxis_color`.

<!-- category: Plotting -->
<!-- keywords: zaxis_width -->
<!-- signatures: zaxis_width -->
### Variable: zaxis_width

Valor por defecto: 1


`zaxis_width` es el ancho del eje *z*.
Su valor debe ser un número positivo. Esta opción no tiene efecto alguno en escenas 2D.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_width = 3)$
```


Véanse también `zaxis`, `zaxis_type` y `zaxis_color`.

<!-- category: Plotting -->
<!-- keywords: zrange -->
<!-- signatures: zrange -->
### Variable: zrange

Valor por defecto: `auto`


Cuando `zrange` vale `auto`, el rango de la coordenada *z*
se calcula de forma automática.


Si el usuario quiere especificar un intervalo para *z*, éste debe
expresarse como una lista de Maxima, como en `zrange=[-2, 3]`.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.


Ejemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(yrange = [-3,3],
             zrange = [-2,5],
             explicit(x^2+y^2,x,-1,1,y,-1,1),
             xrange = [-3,3])$
```


Véanse también `xrange` y `yrange`.

<!-- category: Plotting -->
<!-- keywords: ztics -->
<!-- signatures: ztics -->
### Variable: ztics

Valor por defecto: `true`


Esta opción gráfica controla la forma en la que se dibujarán las marcas
del eje *z*.


Véase `xtics` para una descripción completa.

<!-- category: Plotting -->
<!-- keywords: ztics_axis -->
<!-- signatures: ztics_axis -->
### Variable: ztics_axis

Valor por defecto: `false`


Si `ztics_axis` vale `true`, las marcas y sus etiquetas se dibujan sobre
el propio eje *z*, si vale `false` las marcas se colocan a lo largo del borde
del gráfico.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

<!-- category: Plotting -->
<!-- keywords: ztics_rotate -->
<!-- signatures: ztics_rotate -->
### Variable: ztics_rotate

Valor por defecto: `false`


Si `ztics_rotate` vale `true`, las marcas del eje *z* se giran 
90 grados.


Puesto que ésta es una opción global, su posición dentro de la
descripción de la escena no reviste importancia.

