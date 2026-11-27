## Gráficos

<!-- category: Other -->
<!-- keywords: adapt_depth -->
<!-- signatures: adapt_depth[adapt_depth, integer] -->
### Variable: adapt_depth

Valor por defecto: 5


Número máximo de particiones utilizado por el algoritmo adaptativo
de representación gráfica.

<!-- category: Other -->
<!-- keywords: axes -->
<!-- signatures: axes[axes, symbol] -->
### Variable: axes

Valor por defecto: `true`


El argumento *symbol* puede valer `true`, `false`, `x` 
o `y`. Si vale `false`, no se mostrarán los ejes; si es igual a
`x` o `y`, solo ese eje será el que se representa; si vale
`true`, se mostrarán ambos ejes.


Esta opción solo es relevante para `plot2d` y `implicit_plot`.

<!-- category: Other -->
<!-- keywords: azimuth -->
<!-- signatures: azimuth[azimuth, number] -->
### Variable: azimuth

Valor por defecto: 30


Un gráfico `plot3d` se puede interpretar como comenzando
horizontalmente en el plano xy; a partir de ahí,
la coordenada z se eleva perpendicularmente al papel. El eje z
gira entonces alrededor del eje x un ángulo igual a `elevation`,
luego gira el plano xy alrededor del nuevo eje z un ángulo `azimuth`.
Esta opción establece el valor para `azimuth` en grados
sexagesimales.


Véase también `elevation`.

<!-- category: Other -->
<!-- keywords: color -->
<!-- signatures: color[color, color_1, ..., color_n] -->
### Variable: color

Valor por defecto: blue, red, green, magenta, black, cyan



Define el color para las curvas en `plot2d` y `implicit_plot`. En
`plot3d` define los colores para el enrejado de las superficies si no
se utiliza la paleta; una cara de la superficie tendrá *color_1*
y la otra *color_2*, o el mismo color si se especifica solo uno.


Si hay más curvas o superficies que caras, los colores se repetirán 
secuencialmente. Con Gnuplot, los colores pueden ser: azul, rojo, verde,
magenta, negro y cián; con Xmaxima, los colores pueden ser esos mismos,
o una cadena de texto que comienza con el carácter `#` seguido de
seis dígitos hexadecimales: dos para la componente roja, otros
dos para la verde y otros dos para la azul. Si se introduce un nombre de
color no reconocido, en su lugar se utilizará el negro.

<!-- category: Other -->
<!-- keywords: colorbox -->
<!-- signatures: colorbox[colorbox, symbol] -->
### Variable: colorbox

Valor por defecto: `false`


El argumento *symbol* puede valer `true` o `false`.
Si vale `true` y `plot3d` utiliza la paleta de colores
para representar diferentes valores de z, se dibujará un rectángulo
en la parte derecha, indicando los colores utilizados para
los diferentes valores de z. Esta opción no funciona en Xmaxima.

<!-- category: Other -->
<!-- keywords: elevation -->
<!-- signatures: elevation[elevation, number] -->
### Variable: elevation

Valor por defecto: 60


Un gráfico `plot3d` se puede interpretar como comenzando
horizontalmente en el plano xy; a partir de ahí,
la coordenada z se eleva perpendicularmente al papel. El eje z
gira entonces alrededor del eje x un ángulo igual a `elevation`,
luego gira el plano xy alrededor del nuevo eje z un ángulo `azimuth`.
Esta opción establece el valor para `elevation` en grados
sexagesimales.


Véase también  `azimuth`.

<!-- category: Other -->
<!-- keywords: get_plot_option -->
<!-- signatures: get_plot_option(keyword, index) -->
### Function: get_plot_option (keyword, index)

Devuelve el valor actual de la opción *keyword* almacenada
en la variable global `plot_options`. Si *index* toma
el valor 1, devuelve el propio valor de *keyword*; si vale 2
le añade el primer parámetro, y así sucesivamente.


Véanse también `plot_options`, `set_plot_option` y la
sección Opciones gráficas.

<!-- category: Other -->
<!-- keywords: grid -->
<!-- signatures: grid[grid, integer, integer] -->
### Variable: grid

Valor por defecto: 30, 30


Establece el número de puntos para los puntos de la rejilla en las
direcciones x e y en escenas 3D.

<!-- category: Other -->
<!-- keywords: legend -->
<!-- signatures: legend[legend, string_1, ..., string_n], legend[legend, false] -->
### Variable: legend

Especifica las etiquetas para los gráficos en los que aparecen
varios objetos.  Si hay más expresiones que etiquetas, éstas se repetirán.
Con el valor `false` no se mostrarán etiquetas.
Por defecto se pasarán los nombres de las expresiones o funciones, o las palabras
`discrete1`, `discrete2`, ..., para gráficos de puntos.
Esta opción no se puede utilizar con *set_plot_option*.

<!-- category: Other -->
<!-- keywords: logx -->
<!-- signatures: logx[logx] -->
### Variable: logx

Hace que el eje de abscisas se dibuje en la escala 
logarítmica. Esta opción no se puede utilizar 
con *set_plot_option*.

<!-- category: Other -->
<!-- keywords: logy -->
<!-- signatures: logy[logy] -->
### Variable: logy

Hace que el eje de ordenadas se dibuje en la escala 
logarítmica. Esta opción no se puede utilizar 
con *set_plot_option*.

<!-- category: Other -->
<!-- keywords: make_transform -->
<!-- signatures: make_transform([var1, var2, var3], fx, fy, fz) -->
### Function: make_transform ([var1, var2, var3], fx, fy, fz)

Devuelve una función que se puede utilizar con la opción `transform_xy`
de `plot3d`. Las tres variables ficticias *var1*, *var2* y *var3* 
representan las tres variables de la función `plot3d`, las dos primeras
independientes y la tercera dependiente. Las tres funciones *fx*, *fy* y
*fz* deben depender solo de las tres variables anteriores y retornar las
correspondientes x, y, z que se deben dibujar. Hay dos transformaciones
predefinidas: `polar_to_xy` y `spherical_to_xyz`.


Véanse `polar_to_xy` y `spherical_to_xyz`.

<!-- category: Other -->
<!-- keywords: mesh_lines_color -->
<!-- signatures: mesh_lines_color[mesh_lines_color, color] -->
### Variable: mesh_lines_color

Valor por defecto: `black`


Establece el color del enrejado en los gráficos creados por `plot3d`
cuando se utiliza una paleta. Acepta los mismos colores que la opción 
`color`. También se le puede dar el valor `false` para eliminar
el enrejado.

<!-- category: Other -->
<!-- keywords: nticks -->
<!-- signatures: nticks[nticks, integer] -->
### Variable: nticks

Valor por defecto: 29


Cuando se dibujan funciones con `plot2d`, establece el número
inicial de puntos utilizado por la rutina gráfica adaptativa. Cuando
se dibujan funciones con `plot3d` o paramétricas con `plot2d`,
su valor es igual al número de puntos que se representarán en el
gráfico.

<!-- category: Other -->
<!-- keywords: palette -->
<!-- signatures: palette[palette, [palette_1], ..., [palette_n]], palette[palette, false] -->
### Variable: palette

Valor por defecto: [hue, 0.25, 0.7, 0.8, 0.5], [hue, 0.65, 0.8, 0.9, 0.55], 
[hue, 0.55, 0.8, 0.9, 0.4], [hue, 0.95, 0.7, 0.8, 0.5]


Puede consistir en una paleta o en una lista de varias paletas. Cada
paleta es una lista con una palabra clave seguida de cuatro números.
Los tres primeros números, que deben tomar valores entre 0 y 1, definen
el matiz, la saturación y el valor de un color básico a asignar al 
mínimo valor de z. La palabra clave especifica cuál de los
tres atributos (`hue`, `saturation` o `value`) incrementará
de acuerdo con los valores de z. El último número se corresponde con el 
incremento del máximo valor de z. Este último número puede ser mayor que
1 o negativo.


Gnuplot solo utiliza la primera paleta de la lista; Xmaxima utilizará 
las paletas de la lista secuencialmente cuando haya que representar varias
superficies conjuntamente; si el número de paletas no es suficiente,
se repetirán también de forma secuencial.


El color del enrrejado de la superficie se establece con `mesh_lines_color`.
Si `palette` tiene el valor `false`, las superficies se representan
solo con el enrrejado; en tal caso, el color de las líneas
será el determinado por `color`.

<!-- category: Other -->
<!-- keywords: plot2d -->
<!-- signatures: plot2d(plot, x_range, ..., options, ...), plot2d([plot_1, ..., plot_n], ..., options, ...), plot2d([plot_1, ..., plot_n], x_range, ..., options, ...) -->
### Function: plot2d (plot, x_range, ..., options, ...)

Donde *plot*, *plot_1*, ..., *plot_n* pueden ser
expresiones, nombres de funciones o una
lista de cualquiera de las siguientes formas: 
`[discrete, [x1, ..., xn], [y1, ..., yn]]`, `[discrete, [[x1, y1], ..., [xn, ..., yn]]` o `[parametric, x_expr, y_expr, t_range]`.


Muestra un gráfico de una o más expresiones como función de una variable.


La función `plot2d` representa uno o más gráficos en dos
dimensiones. Las expresiones o nombres de funciones que se utilicen para
definir curvas deben depender todas ellas de una única variable *var*,
siendo obligatorio utilizar *x_range* para nombrar la variable y darle sus
valores mínimo y máximo usando la siguiente sintaxis: 
`[variable, min, max]`.


Un gráfico también se puede definir de forma discreta o paramétrica.
La forma discreta se utiliza para dibujar un conjunto de puntos de
coordenadas dadas. Un gráfico discreto se define como una lista
que empiezan con la palabra clave *discrete* seguida de una o dos
listas de valores numéricos. Cuando haya dos listas, ambas deben ser
de igual longitud, la primera se interpreta como la de abscisas y la
segunda de ordenadas. Cuando haya una lista siguiendo la clave *discrete*,
cada uno de sus elementos debe ser a su vez una lista de solo dos valores,
correspondientes a las coordenadas x e y.


Un gráfico paramétrico se define como una lista que empieza con la
palabra clave *parametric*, seguida de dos expresiones o nombres de
funciones y un rango paramétrico. El rango paramétrico debe ser una
lista formada con el nombre del parámetro seguido de sus valores
mínimo y máximo:
`[param, min, max]`. El gráfico se formará con
los puntos cuyas coordenadas devuelvan las dos expresiones o funciones, 
según *param* aumente desde *min* hasta *max*.


La especificación del rango para el eje vertical es opcional y
toma la forma `[y, min, max]` (*y* se utiliza
siempre para el eje vertical). En caso de utilizar esta opción,
el gráfico mostrará exactamente ese rango vertical, 
independientemente de los valores alcanzados por los elementos
gráficos. Si no se especifica el rango vertical, se ajustará
a los valores extremos alcanzados por las ordenadas de los puntos
que aparezcan en el gráfico.


Cualesquiera otras opciones deben ser listas, comenzando con el
nombre de la opción seguido de uno o más valores. Véase
`plot_options`.


Si hay varias expresiones para ser dibujadas, se mostrará una leyenda
que identifique a cada una de ellas. Las etiquetas a utilizar pueden
especificarse con la opción *legend*. Si no se utiliza esta opción,
Maxima creará etiquetas a partir de las expresiones o nombres de funciones.


Ejemplos:


Dibujando la función sinusoidal:






```maxima
(%i1) plot2d (sin(x), [x, -%pi, %pi])$
```


![plotting6](figures/plotting6.png)


Si la función crece rápidamente puede ser necesario limitar los
valores del eje vertical:






```maxima
(%i1) plot2d (sec(x), [x, -2, 2], [y, -20, 20])$
plot2d: some values were clipped.
```


![plotting7](figures/plotting7.png)


Gráfico con escala logarítmica:






```maxima
(%i1) plot2d (exp(3*s), [s, -2, 2], [logy])$
```


![plotting9](figures/plotting9.png)


Dibujando funciones especificadas por su nombre:









```maxima
(%i1) F(x) := x^2 $

(%i2) :lisp (defun |$g| (x) (m* x x x))
$g

(%i2) H(x) := if x < 0 then x^4 - 1 else 1 - x^5 $
(%i3) plot2d ([F, G, H], [u, -1, 1], [y, -1.5, 1.5])$
```


![plotting10](figures/plotting10.png)


Ejemplo de función paramétrica. Curva de la mariposa:








```maxima
(%i1) r: (exp(cos(t))-2*cos(4*t)-sin(t/12)^5)$
(%i2) plot2d([parametric, r*sin(t), r*cos(t), 
             [t, -8*%pi, 8*%pi]])$
```


![plotting11](figures/plotting11.png)


Gráfico de una circunferencia de radio 1, con centro en el origen, junto con
la función `y=-|x|`. Para que la circunferencia no aparezca como
una elipse, se usa la opción `same_xy` para que la escala sea la misma
en los dos ejes. También se muestra el uso de la opción `nolegend` para
eliminar la leyenda que identifica las dos funciones.







```maxima
(%i1) plot2d([x^2+y^2=1, -abs(x)], [x, -1.5, 1.5], [y, -2, 2], same_xy,
             nolegend);
```


![plotting12](figures/plotting12.png)


Puntos discretos definiendo separadamente las coordenadas x e y:







```maxima
(%i1) plot2d ([discrete, makelist(i*%pi, i, 1, 5),
                            [0.6, 0.9, 0.2, 1.3, 1]])$
```


![plotting14](figures/plotting14.png)



Gráfico de 200 puntos aleatorios entre 0 y 9:






```maxima
(%i1) plot2d ([discrete, makelist ( random(10), 200)])$
```


![plotting13](figures/plotting13.png)


En este ejemplo, se guarda una tabla de tres columnas en el
archivo `data.txt`, que luego será leído
para representar las dos últimas columnas:











```maxima
(%i1) display2d:false$
(%i2) with_stdout ("data.txt", for x:0 thru 10 do
                             print (x, x^2, x^3))$
(%i3) data: read_matrix ("data.txt")$
(%i4) plot2d ([discrete, transpose(data)[2], transpose(data)[3]],
  [style,points], [point_type,diamond], [color,red])$
```


![plotting15](figures/plotting15.png)


Un gráfico de datos empíricos junto con su modelo
teórico:












```maxima
(%i1) xy: [[10, .6], [20, .9], [30, 1.1], [40, 1.3], [50, 1.4]]$
(%i2) plot2d([[discrete, xy], 2*%pi*sqrt(l/980)], [l,0,50],
        [style, points, lines], [color, red, blue],
        [point_type, asterisk],
        [legend, "experiment", "theory"],
        [xlabel, "pendulum's length (cm)"],
        [ylabel, "period (s)"])$
```


![plotting16](figures/plotting16.png)

<!-- category: Other -->
<!-- keywords: plot3d -->
<!-- signatures: plot3d(expr, x_range, y_range, ..., options, ...), plot3d([expr_1, ..., expr_n], x_range, y_range, ..., options, ...) -->
### Function: plot3d (expr, x_range, y_range, ..., options, ...)

Dibuja una o más superficies definidas como funciones de dos variables o en
forma paramétrica.


Las funciones a dibujar se pueden especificar como expresiones o nombres
de funciones.  Puede utilizarse el ratón para hacer girar el gráfico y
observarlo desde distintos ángulos.


Ejemplos:


Gráfico de una función de dos variables:







```maxima
(%i1) plot3d (u^2 - v^2, [u, -2, 2], [v, -3, 3], [grid, 100, 100],
        nomesh_lines)$
```


![plotting17](figures/plotting17.png)


Uso de la opción z para acotar una función que tiende a infinito
(en este caso, la función tiende a menos infinito en los ejes
x e y):







```maxima
(%i1) plot3d ( log ( x^2*y^2 ), [x, -2, 2], [y, -2, 2], [z, -8, 4],
         nopalette, [color, magenta])$
```


![plotting18](figures/plotting18.png)


Los valores infinitos de z se pueden obviar eligiendo una retícula
que no coincida con las asíntotas; este ejemplo también muestra
cómo alterar la paleta de colores y como incluir una barra
lateral que muestra la correspondencia entre colores y valores de z:









```maxima
(%i1) plot3d (log (x^2*y^2), [x, -2, 2], [y, -2, 2],[grid, 29, 29],
       [palette, [gradient, red, orange, yellow, green]],
       color_bar, [xtics, 1], [ytics, 1], [ztics, 4],
       [color_bar_tics, 4])$
```


![plotting19](figures/plotting19.png)


Dos superficies en un mismo gráfico. Si los dominios de las dos superficies
son diferentes, las dos funciones deben ser colocados en listas separadas,
cada una con su propio dominio. El dominio por fuera de esas listas
define el dominio para todo el gráfico.








```maxima
(%i1) plot3d ([[-3*x - y, [x, -2, 2], [y, -2, 2]],
   4*sin(3*(x^2 + y^2))/(x^2 + y^2), [x, -3, 3], [y, -3, 3]],
   [x, -4, 4], [y, -4, 4])$
```


![plotting20](figures/plotting20.png)


La botella de Klein, definida paramétricamente:










```maxima
(%i1) expr_1: 5*cos(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)-10$
(%i2) expr_2: -5*sin(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)$
(%i3) expr_3: 5*(-sin(x/2)*cos(y)+cos(x/2)*sin(2*y))$
(%i4) plot3d ([expr_1, expr_2, expr_3], [x, -%pi, %pi],
        [y, -%pi, %pi], [grid, 50, 50])$
```


![plotting21](figures/plotting21.png)


Gráfico de un armónico esférico, utilizando la transformación
predefinida `spherical_to_xyz`:







```maxima
(%i1) plot3d (sin(2*theta)*cos(phi), [theta,0,%pi], [phi,0,2*%pi],
      [transform_xy, spherical_to_xyz], [grid, 30, 60], nolegend)$
```


![plotting22](figures/plotting22.png)


Uso de la transformación predefinida `polar_to_xy` para transformar
coordenadas cilíndricas para rectangulares. Este ejemplo también muestra
cómo eliminar el marco y la leyenda:







```maxima
(%i1) plot3d (r^.33*cos(th/3), [r,0,1], [th,0,6*%pi], nobox,
    nolegend, [grid, 12, 80], [transform_xy, polar_to_xy])$
```


![plotting23](figures/plotting23.png)


Dibujo de una esfera utilizando la transformación de coordenadas esféricas
para rectangulares. La opción `same_xyz` se usa para que la escala
de los tres ejes sea la misma, evitando que la esfera parezca un elipsoide.
Cuando se usan transformaciones, no es conveniente eliminar las líneas de
la superficie, para evitar errores en Gnuplot.








```maxima
(%i1) plot3d ( 5, [theta,0,%pi], [phi,0,2*%pi], same_xyz, nolegend,
  [transform_xy, spherical_to_xyz], [mesh_lines_color,blue],
  [palette,[gradient,"#1b1b4e", "#8c8cf8"]])$
```


![plotting24](figures/plotting24.png)


Definición de una función con dos variables utilizando una matriz. 
Nótese la comilla simple en la definición de la función para
prevenir que `plot3d` falle al detectar que la matriz necesita
índices enteros:








```maxima
(%i1) M: matrix([1,2,3,4], [1,2,3,2], [1,2,3,4], [1,2,3,3])$
(%i2) f(x, y) := float('M [round(x), round(y)])$
(%i3) plot3d (f(x,y), [x,1,4], [y,1,4], [grid,3,3], nolegend)$
```


![plotting25](figures/plotting25.png)


Asignando a la opción `elevation` el valor cero, una superficie
puede verse como una aplicación en la que cada color representa un nivel
diferente.








```maxima
(%i1) plot3d (cos (-x^2 + y^3/4), [x,-4,4], [y,-4,4], [zlabel,""],
       [mesh_lines_color,false], [elevation,0], [azimuth,0],
       color_bar, [grid,80,80], noztics, [color_bar_tics,1])$
```


![plotting26](figures/plotting26.png)



Véase también la sección Opciones gráficas.

<!-- category: Other -->
<!-- keywords: plot_format -->
<!-- signatures: plot_format[plot_format, format] -->
### Variable: plot_format

Valor por defecto: en sistemas Windows, `gnuplot`; en otros, `gnuplot_pipes`


Establece el formato a utlizar por las rutinas gráficas.


Debe tomar uno de los siguientes valores: `gnuplot`, `xmaxima`, `mgnuplot`
o `gnuplot_pipes`.

<!-- category: Other -->
<!-- keywords: plot_options -->
<!-- signatures: plot_options -->
### Variable: plot_options

Los elementos de esta lista establecen las opciones por defecto para los gráficos.
Si una opción está presente en una llamada a `plot2d` o a `plot3d`,
este valor adquiere prevalencia sobre las opciones por defecto.
En otro caso se utilizará el valor que tenga en `plot_options`.
Las opciones por defecto se asignan mediante la función `set_plot_option`.


Cada elemento de `plot_options` es una lista de dos o más elementos,
el primero de los cuales es el nombre de la opción, siendo los siguientes 
los valores que toma. En algunos casos el valor asignado es a su vez una lista,
que puede contener varios elementos.


Véanse también `set_plot_option`, `get_option` y la sección
Opciones gráficas.

<!-- category: Other -->
<!-- keywords: plot_realpart -->
<!-- signatures: plot_realpart[plot_realpart, symbol] -->
### Variable: plot_realpart

Valor por defecto: `false`


Cuando vale `true`, se representa gráficamente la parte real
de las funciones; equivale a ejecutar `realpart(función)`.
Si vale `false`, no se representa nada cuando la función
no devuelva un valor real. Por ejemplo, si `x` es negativo, 
`log(x)` devuelve un valor negativo cuya parte real es `log(abs(x))`;
en tal caso, si `plot_realpart` vale `true`, `log(-5)`
se representa como `log(5)`, mientras que no se representa nada 
si `plot_realpart` vale `false`.

<!-- category: Other -->
<!-- keywords: point_type -->
<!-- signatures: point_type[point_type, type_1, ..., type_n] -->
### Variable: point_type

Valor por defecto: `bullet`, `circle`, `plus`, `times`, `asterisk`,
`box`, `square`, `triangle`, `delta`, `wedge`, `nabla`,
`diamond`, `lozenge`


En Gnuplot, cada conjunto de puntos que vaya a ser representado con los
estilos `points` o `linespoints` se hará con objetos tomados
de esta lista en orden secuencial. Si hay más conjuntos de puntos que 
objetos en la lista, se irán repitiendo de forma secuencial. Los objetos
que pueden ser utilizados son: `bullet`, `circle`, `plus`, 
`times`, `asterisk`, `box`, `square`, `triangle`, 
`delta`, `wedge`, `nabla`, `diamond` o `lozenge`

<!-- category: Other -->
<!-- keywords: polar_to_xy -->
<!-- signatures: polar_to_xy -->
### Function: polar_to_xy

Cuando a la opción `transform_xy` de `plot3d` se le pasa el valor 
`polar_to_xy`, se interpretarán las dos primeras variables independientes como 
polares, transformándolas luego a coordenadas cartesianas.

<!-- category: Other -->
<!-- keywords: psfile -->
<!-- signatures: psfile[psfile, string] -->
### Variable: psfile

Guarda el gráfico en formato Postscript con nombre *string*
en lugar de mostrarlo en pantalla. Por defecto, el fichero se creará
en la carpeta definida en la variable *maxima_tempdir*, cuyo
valor se podrá cambiar para almacenar el fichero en otra carpeta.

<!-- category: Other -->
<!-- keywords: run_viewer -->
<!-- signatures: run_viewer[run_viewer, symbol] -->
### Variable: run_viewer

Valor por defecto: `true`


Controla si el visor apropiado para la salida gráfica debe ejecutarse o no.

<!-- category: Other -->
<!-- keywords: set_plot_option -->
<!-- signatures: set_plot_option(option) -->
### Function: set_plot_option (option)

Acepta la mayor parte de opciones listadas en la sección Opciones gráficas
y las almacena en la variable global `plot_options`.


La función `set_plot_option` evalúa su argumento y devuelve
la lista completa `plot_options` tal como queda después de la actualización.


Véanse también `plot_options`, `get_option` y la sección
Opciones gráficas.


Ejemplos:


Modificación de los valores para `grid`.






```maxima
(%i1) set_plot_option ([grid, 30, 40]);

(%o1) [[t, - 3, 3], [grid, 30, 40], [transform_xy, false], 
[run_viewer, true], [axes, true], [plot_format, gnuplot_pipes], 
[color, blue, red, green, magenta, black, cyan], 
[point_type, bullet, circle, plus, times, asterisk, box, square, 
triangle, delta, wedge, nabla, diamond, lozenge], 
[palette, [hue, 0.25, 0.7, 0.8, 0.5], 
[hue, 0.65, 0.8, 0.9, 0.55], [hue, 0.55, 0.8, 0.9, 0.4], 
[hue, 0.95, 0.7, 0.8, 0.5]], [gnuplot_term, default], 
[gnuplot_out_file, false], [nticks, 29], [adapt_depth, 5], 
[gnuplot_preamble, ], [gnuplot_default_term_command, 
set term pop], [gnuplot_dumb_term_command, set term dumb 79 22], 
[gnuplot_ps_term_command, set size 1.5, 1.5;set term postscript \
eps enhanced color solid 24], [plot_realpart, false]]
```

<!-- category: Other -->
<!-- keywords: spherical_to_xyz -->
<!-- signatures: spherical_to_xyz -->
### Function: spherical_to_xyz

Cuando a la opción `transform_xy` de `plot3d` se le pasa el valor 
`spherical_to_xyz`, se interpretarán las variables independientes como 
esféricas, transformándolas luego a coordenadas cartesianas.

<!-- category: Other -->
<!-- keywords: style -->
<!-- signatures: style[style, type_1, ..., type1_n], style[style, [style_1], ..., [style_n]] -->
### Variable: style

Valor por defecto: *lines* (dibuja todos los puntos unidos por 
líneas de ancho 1 y con el primer color de la lista de la opción `color`).


Estilos a utilizar para las funciones o conjuntos de datos en
gráficos 2d. A la palabra `style` debe seguirle uno o más
estilos. Si hay más funciones o conjuntos de datos que estilos,
éstos se repetirán. Los estilos que se admiten son: *lines*
para segmentos lineales, *points* para puntos aislados,
*linespoints* para segmentos y puntos, *dots* para
pequeños puntos aislados. Gnuplot también acepta el estilo
*impulses*.


Los estilos se pueden escribir como elementos de una lista, junto
con algunos parámetros adicionales. *lines* acepta uno o dos
números: el ancho de la línea y un entero que identifica
el color. Los códigos de color por defecto son: 1, azul; 2, rojo;
3, magenta; 4, naranja; 5, marrón; 6, verde lima; 7, aguamarina.
En caso de utilizar Gnuplot con un terminal diferente de X11, estos
colores pueden cambiar; por ejemplo, bajo la opción 
[*gnuplot_term*,*ps*], el índice 4
se corresponde con el negro en lugar del naranja.


*points* acepta uno, dos o tres parámetros; el primer parámetro
es el radio de los puntos, el segundo es un entero para seleccionar el color,
con igual codificación que en *lines* y el tercer parámetro sólo
es utilizado por Gnuplot y hace referencia a varios objetos para representar
los puntos. Los tipos de objetos disponibles son: 1, círculos
rellenos; 2, circunferencias; 3, +; 4, x; 5, *; 6, cuadrados rellenos;
7, cuadrados huecos; 8, triángulos rellenos; 9, triángulos huecos;
10, triángulos rellenos invertidos; 11, triángulos huecos invertidos;
12, rombos rellenos; 13, rombos huecos.


*linesdots* acepta hasta cuatro parámetros: ancho de línea,
radio de los puntos, color y tipo de objetos para representar puntos.


Véanse también `color` y `point_type`.

<!-- category: Other -->
<!-- keywords: transform_xy -->
<!-- signatures: transform_xy[transform_xy, symbol] -->
### Variable: transform_xy

Valor por defecto: `false`


La variable *symbol* puede ser `false` o el resultado
devuelto por la función `transform_xy`. Si es distinto de
`false`, se utiliza para transformar las tres coordenadas en
`plot3d`.


Véanse `make_transform`, `polar_to_xy` y `spherical_to_xyz`.

<!-- category: Other -->
<!-- keywords: x -->
<!-- signatures: x[x, min, max] -->
### Variable: x

Cuando se utiliza como primera opción en una instrucción para
un gráfico 2D (o cualquiera de las dos primeras en un gráfico 3D),
indica que su primera variable independiente es x y ajusta su rango.
También se puede utilizar después de la primera opción
(o después de la segunda opción en un gráfico 3D) para definir
el dominio horizontal que se representará en el gráfico.

<!-- category: Other -->
<!-- keywords: xlabel -->
<!-- signatures: xlabel[xlabel, string] -->
### Variable: xlabel

Especifica la etiqueta para el primer eje. Si no se utiliza esta
opción, la etquieta será el nombre de la variable independiente,
cuando se utilicen `plot2d` o `implicit_plot`, o el nombre
de la primera variable cuando se utilicen `plot3d` o `contour_plot`,
o la primera expresión en el caso de una curva paramétrica.
No puede utilizarse con *set_plot_option*.

<!-- category: Other -->
<!-- keywords: y -->
<!-- signatures: y[y, min, max] -->
### Variable: y

Cuando se utiliza como una de las dos primeras opciones en `plot3d`,
indica que una de las variables independientes es “y” y ajusta su
rango. En otro caso, define el dominio de la segunda variable que se mostrará
en el gráfico.

<!-- category: Other -->
<!-- keywords: ylabel -->
<!-- signatures: ylabel[ylabel, string] -->
### Variable: ylabel

Especifica la etiqueta para el segundo eje. Si no se utiliza esta
opción, la etiqueta será “y”,
cuando se utilicen `plot2d` o `implicit_plot`, o el nombre
de la segunda variable cuando se utilicen `plot3d` o `contour_plot`,
o la segunda expresión en el caso de una curva paramétrica.
No puede utilizarse con *set_plot_option*.

<!-- category: Other -->
<!-- keywords: z -->
<!-- signatures: z[z, min, max] -->
### Variable: z

Se utiliza en `plot3d` para ajustar el rango de valores de z que se
mostrará en el gáfico.

<!-- category: Other -->
<!-- keywords: zlabel -->
<!-- signatures: zlabel[zlabel, string] -->
### Variable: zlabel

Especifica la etiqueta para el tercer eje cuando se utiliza `plot3d`.
Si no se utiliza esta opción, la etiqueta será “z”
en el caso de superficies, o la tercera expresión en el caso de una curva paramétrica.
No puede utilizarse con *set_plot_option* y se ignora 
en `plot2d` y `implicit_plot`.

