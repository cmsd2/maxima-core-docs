## dynamics

<!-- category: Plotting -->
<!-- keywords: animation -->
<!-- signatures: animation[animation, propiedad, posiciones] -->
### Variable: animation

*propiedad* deberá ser una de las 4 siguientes propiedades del
objeto: `objeto_origin`,
`objeto_scale`, `objeto_position` o
`objeto_orientation` y *posiciones* deberá ser una
lista de puntos. Cuando se oprime el botón “play”, esa propiedad
tomará sucesivamente los valores en la lista, en intervalos regulares de
tiempo definidos por la opción `scene_tstep`. El botón de
volver al comienzo puede usarse para recomenzar desde el principio de la
lista, haciendo que la animación comience nuevamente cuando se presione
otra vez el botón de play.


Consulte también `objeto_track`.

See also: `objeto_origin`, `objeto_scale`, `objeto_position`, `objeto_orientation`, `scene_tstep`, `objeto_track`.

<!-- category: Plotting -->
<!-- keywords: background -->
<!-- signatures: background[background, color] -->
### Variable: background

Valor predefinido: `black`


El color del fondo de la ventana gráfica. Acepta nombres de colores o
secuencias de caracteres hexadecimales para rojo-verde-azul (ver la
opción `color` de plot2d).

See also: `color`.

<!-- category: Plotting -->
<!-- keywords: center -->
<!-- signatures: center[center, punto] -->
### Variable: center

Valor predefinido: `[0, 0, 0]`


Coordenadas del centro geométrico del objeto, en relación a su posición
(`objeto_position`); *punto* puede ser una lista de
3 números reales o 3 números separados por comas. En objetos de clase
“cylinder”,”cone” o “cube” estará localizado en el punto medio de
la altura y en objetos de clase “sphere” estará en su centro.

See also: `objeto_position`.

<!-- category: Plotting -->
<!-- keywords: chaosgame -->
<!-- signatures: chaosgame([[x1, y1]...[xm, ym]], [x0, y0], b, n, opciones, ...); -->
### Function: chaosgame (([[x1, y1]...[xm, ym]], [x0, y0], b, n, opciones, ...);)

Usa el método llamado juego del caos, para producir fractales: se dibuja
un punto inicial (*x0*, *y0*) y luego se elije aleatoriamente
uno de los *m* puntos `[`*x1*,
*y1*`]`...`[`*xm*, *ym*`]`. Después se dibuja
un nuevo punto que estará en el segmento entre el último punto dibujado
y el punto que se acabó de elegir aleatoriamente, a una distancia del
punto elegido que será *b* veces la longitud del segmento. El
proceso se repite *n* veces.  Este programa acepta las mismas
opciones de `plot2d`.


**Ejemplo**. Gráfico del triángulo de Sierpinsky:



```maxima
(%i1) chaosgame([[0, 0], [1, 0], [0.5, sqrt(3)/2]], [0.1, 0.1], 1/2,
                 30000, [style, dots]);
```


![dynamics7](figures/dynamics7.png)

See also: `plot2d`.

<!-- category: Plotting -->
<!-- keywords: cone -->
<!-- signatures: cone[cone, opciones] -->
### Variable: cone

Crea una pirámide regular con altura 1 unidad y base hexagonal con
vértices a 0.5 unidades del eje. Las opciones
`objeto_height` y `objeto_radius` se pueden
usar para alterar esos valores predefinidos y la opción
`objeto_resolution` se usa para alterar el número de
aristas de la base; valores mayores harán que la pirámide parezca un
cono. Por omisión, el eje estará a lo largo del eje x, el punto medio de
la altura estará en el origen y el vértice en el lado positivo del eje
x; las opciones `objeto_orientation` y
`objeto_center` permiten alterar eso.


**Ejemplo**. El siguiente comando muestra una pirámide que comienza
a dar vueltas cuando se oprime el botón de animación.

 

```maxima
(%i1) scene([cone, [orientation,0,30,0], [tstep,100],
   [animate,orientation,makelist([0,30,i],i,5,360,5)]], restart)$
```

See also: `objeto_height`, `objeto_radius`, `objeto_resolution`, `objeto_orientation`, `objeto_center`.

<!-- category: Plotting -->
<!-- keywords: cube -->
<!-- signatures: cube[cube, opciones] -->
### Variable: cube

Un cubo con aristas de 1 unidad y caras paralelas al los planos xy, xz y
yz. Las longitudes de las 3 aristas se pueden modificar con las opciones
`objeto_xlength`, `objeto_ylength` y
`objeto_zlength`, convirtiéndolo en un paralelepípedo y
las caras se pueden hacer rotar con la opción
`objeto_orientation`.

See also: `objeto_xlength`, `objeto_ylength`, `objeto_zlength`, `objeto_orientation`.

<!-- category: Plotting -->
<!-- keywords: cylinder -->
<!-- signatures: cylinder[cylinder, opciones] -->
### Variable: cylinder

Crea un prisma regular con altura de 1 unidad y base hexagonal con los
vértices a 0.5 unidades del eje. Las opciones
`objeto_height` y `objeto_radius` permiten
modificar esos valores predefinidos y la opción
`objeto_resolution` se puede usar para modificar el
número de aristas de la base; valores mayores tornan el prisma más
parecido a un cilindro. La altura predefinida se puede alterar con la
opción `objeto_height`. Por omisión el eje estará
orientado a lo largo del eje x, y el punto medio de la altura estará en
el origen; se pueden cambiar esas propiedades con las opciones
`objeto_orientation` y `objeto_center`.

See also: `objeto_height`, `objeto_radius`, `objeto_resolution`, `objeto_orientation`, `objeto_center`.

<!-- category: Plotting -->
<!-- keywords: endphi -->
<!-- signatures: endphi[endphi, ángulo] -->
### Variable: endphi

Valor predefinido: `180`


En una esfera, phi es el ángulo en el plano vertical que pasa por el eje
z, medido a partir de la parte positiva del eje z. *ángulo* debe ser
un múmero entre 0 y 180 que determina el valor final de phi hasta donde
se mostrará la superficie. Valores menores que 180 eliminan una parte de
la superficie.


Consulte también `objeto_startphi` y
`objeto_phiresolution`.

See also: `objeto_startphi`, `objeto_phiresolution`.

<!-- category: Plotting -->
<!-- keywords: endtheta -->
<!-- signatures: endtheta[endtheta, ángulo] -->
### Variable: endtheta

Valor predefinido: `360`


En una esfera, theta es el ángulo en el plano horizontal (longitud),
medido desde la parte positiva del eje x. *ángulo* debe ser un
número entre 0 y 360 que determina el valor final donde la superficie
terminará. Valores menores que 360 hacen que se elimine una parte de la
superficie de la esfera.


Consulte también `objeto_starttheta` y
`objeto_thetaresolution`.

See also: `objeto_starttheta`, `objeto_thetaresolution`.

<!-- category: Plotting -->
<!-- keywords: evolution -->
<!-- signatures: evolutionevolution(F, y0, n, ..., opciones, ...); -->
### Function: evolution (evolution(F, y0, n, ..., opciones, ...);)

Dibuja *n+1* puntos en una gráfica bidimensional (serie de
tiempo), en que las coordenadas horizontales de los puntos son los
números enteros 0, 1, 2, ..., *n*, y las coordenadas verticales
son los valores *y(n)* correspondientes, obtenidos a partir de la
relación de recurrencia


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


Con valor inicial *y(0)* igual a *y0*. *F* deberá ser una
expresión que dependa únicamente de la variable *y* (y no de *n*),
*y0* deberá ser un número real y *n* un número entero positivo.
Esta función acepta las mismas opciones que `plot2d`.


**Ejemplo**.



```maxima
(%i1) evolution(cos(y), 2, 11);
```

![dynamics1](figures/dynamics1.png)

See also: `plot2d`.

<!-- category: Plotting -->
<!-- keywords: evolution2d -->
<!-- signatures: evolution2d([F, G], [u, v], [u0, y0], n, opciones, ...); -->
### Function: evolution2d (([F, G], [u, v], [u0, y0], n, opciones, ...);)

Muestra, en una gráfica bidimensional, los primeros *n+1* puntos de
la sucesión definida a partir del sistema dinámico discreto con
relaciones de recurrencia:


```maxima
x(n+1) = F(x(n), y(n))    y(n+1) = G(x(n), y(n))
```


$$
\begin{cases}x_{n+1} = F(x_n, y_n) &\cr y_{n+1} = G(x_n, y_n)\end{cases}
$$


Con valores iniciales *x0* y *y0*. *F* y *G* deben ser dos
expresiones que dependan únicamente de *x* y *y*. Esta función
acepta las mismas opciones que `plot2d`.


**Ejemplo**. Evolución de un sistema dinámico discreto en dos
dimensiones:



```maxima
(%i1) f: 0.6*x*(1+2*x)+0.8*y*(x-1)-y^2-0.9$
(%i2) g: 0.1*x*(1-6*x+4*y)+0.1*y*(1+9*y)-0.4$
(%i3) evolution2d([f,g], [x,y], [-0.5,0], 50000, [style,dots]);
```


![dynamics5](figures/dynamics5.png)


Y un acercamiento de una pequeña región en ese fractal:



```maxima
(%i9) evolution2d([f,g], [x,y], [-0.5,0], 300000, [x,-0.8,-0.6],
                  [y,-0.4,-0.2], [style, dots]);
```


![dynamics6](figures/dynamics6.png)

See also: `plot2d`.

<!-- category: Plotting -->
<!-- keywords: height -->
<!-- signatures: height[height, pixels] -->
### Variable: height

Valor predefinido: `500`


La altura, en pixels, de la ventana gráfica. *pixels* debe ser un
número entero positivo.

<!-- category: Plotting -->
<!-- keywords: ifs -->
<!-- signatures: ifs([r1, ..., rm], [A1, ..., Am], [[x1, y1], ..., [xm, ym]], [x0, y0], n, opciones, ...); -->
### Function: ifs (([r1, ..., rm], [A1, ..., Am], [[x1, y1], ..., [xm, ym]], [x0, y0], n, opciones, ...);)

Usa el método del Sistema de Funciones Iteradas (IFS, en inglés
Iterated Function System). Ese método es semejante al método descrito
en la función `chaosgame`. pero en vez de aproximar el último punto
al punto elegido aleatoriamente, las dos coordenadas del último punto
se multiplican por una matriz 2 por 2 *Ai* correspondiente al punto
que fue elegido aleatoriamente.


La selección aleatoria de uno de los *m* puntos atractivos puede
ser realizada con una función de probabilidad no uniforme, definida
con los pesos *r1*,...,*rm*. Esos pesos deben ser dados en forma
acumulada; por ejemplo, si se quieren 3 puntos con probabilidades 0.2, 0.5 y
0.3, los pesos *r1*, *r2* y *r3* podrían ser 2, 7 y 10, o
cualquier otro grupo de números que tengan la misma proporción. Esta
función acepta las mismas opciones que `plot2d`.


**Ejemplo**. El helecho de Barnsley, creado con 4 matrices y 4
puntos:



```maxima
(%i1) a1: matrix([0.85,0.04],[-0.04,0.85])$
(%i2) a2: matrix([0.2,-0.26],[0.23,0.22])$
(%i3) a3: matrix([-0.15,0.28],[0.26,0.24])$
(%i4) a4: matrix([0,0],[0,0.16])$
(%i5) p1: [0,1.6]$
(%i6) p2: [0,1.6]$
(%i7) p3: [0,0.44]$
(%i8) p4: [0,0]$
(%i9) w: [85,92,99,100]$
(%i10) ifs(w, [a1,a2,a3,a4], [p1,p2,p3,p4], [5,0], 50000, [style,dots]);
```


![dynamics8](figures/dynamics8.png)

See also: `chaosgame`, `plot2d`.

<!-- category: Plotting -->
<!-- keywords: linewidth -->
<!-- signatures: linewidth[linewidth, valor] -->
### Variable: linewidth

Valor predefinido: `1`


El ancho de las líneas cuando se usa la opción
`objeto_wireframe`. *valor* debe ser un número
positivo.

See also: `objeto_wireframe`.

<!-- category: Plotting -->
<!-- keywords: opacity -->
<!-- signatures: opacity[opacity, valor] -->
### Variable: opacity

Valor predefinido: `1`


*valor* debe se un número entre 0 y 1. Cuanto menor sea el número,
mas transparente será el objeto. El valor predefinido de 1 implica un
objeto completamente opaco.

<!-- category: Plotting -->
<!-- keywords: orbits -->
<!-- signatures: orbits(F, y0, n1, n2, [x, x0, xf, xstep], opciones, ...); -->
### Function: orbits ((F, y0, n1, n2, [x, x0, xf, xstep], opciones, ...);)

Dibuja el diagrama de órbitas de una familia de sistemas dinámicos
discretos unidimensionales, con un parámetro *x*; ese tipo de
diagrama se usa para mostrar las bifurcaciones de un sistema discreto
unidimensional.


La función *F(y)* define una secuencia que comienza con un valor
inicial *y0*, igual que en el caso de la función `evolution`,
pero en este caso la función también dependerá del parámetro *x*, el
cual tomará valores comprendidos en el intervalo de *x0* a *xf*,
con incrementos *xstep*. Cada valor usado para el parámetro *x*
se muestra en el eje horizontal. En el eje vertical se mostrarán
*n2* valores de la sucesión *y(n1+1)*,..., *y(n1+n2+1)*,
obtenidos después de dejarla evolucionar durante *n1* iteraciones
iniciales.


**Ejemplo**. Diagrama de órbitas para el mapa cuadrático



```maxima
(%i1) orbits(x^2+a, 0, 50, 200, [a, -2, 0.25], [style, dots]);
```


![dynamics3](figures/dynamics3.png)


Para ampliar la región alrededor de la bifurcación en la parte de
abajo, cerca de x `=` -1.25, se usa el comando:


```maxima
(%i2) orbits(x^2+a, 0, 100, 400, [a,-1,-1.53], [x,-1.6,-0.8],
             [nticks, 400], [style,dots]);
```


![dynamics4](figures/dynamics4.png)

<!-- category: Plotting -->
<!-- keywords: orientation -->
<!-- signatures: orientation[orientation, ángulos] -->
### Variable: orientation

Valor predefinido: `[0, 0, 0]`


Tres ángulos que de rotaciones que serán realizadas en el objeto,
alrededor de los tres ejes.*ángulos* puede ser una lista con tres
números reales o tres números separados por comas. **Ejemplo**:
`[0, 0, 90]` rota el eje x del objeto hasta el eje y del sistema de
referencia.

<!-- category: Plotting -->
<!-- keywords: origin -->
<!-- signatures: origin[origin, punto] -->
### Variable: origin

Valor predefinido: `[0, 0, 0]`


Coordenadas del origen del objeto, en relación al cual las otras
dimensiones serán definidas. *punto* pueden ser tres números
separados por comas, o una lista de tres números.

<!-- category: Plotting -->
<!-- keywords: phiresolution -->
<!-- signatures: phiresolution[phiresolution, num] -->
### Variable: phiresolution

Valor predefinido: ``


Número de sub-intervalos en que se divide el intervalo de valores del
ángulo phi, que comienza en `objeto_startphi` y termina
en `objeto_endphi`. *num* debe ser un número entero
positivo.


Consulte también `objeto_startphi` y
`objeto_endphi`.

See also: `objeto_startphi`, `objeto_endphi`.

<!-- category: Plotting -->
<!-- keywords: pointsize -->
<!-- signatures: pointsize[pointsize, valor] -->
### Variable: pointsize

Valor predefinido: `1`


Tamaño de los puntos, cuando se usa la opción
`objeto_points`. *valor* debe ser un número positivo.

See also: `objeto_points`.

<!-- category: Plotting -->
<!-- keywords: position -->
<!-- signatures: position[position, punto] -->
### Variable: position

Valor predefinido: `[0, 0, 0]`


Coordenadas de la posición del objeto. *punto* puede ser tres
números separados por comas o una lista de tres números.

<!-- category: Plotting -->
<!-- keywords: radius -->
<!-- signatures: radius[radius, valor] -->
### Variable: radius

Valor predefinido: `0.5`


El radio de una esfera o la distancia desde el eje hasta los vértices de
la base en cilindros o conos. *valor* debe ser un número positivo.

<!-- category: Plotting -->
<!-- keywords: resolution -->
<!-- signatures: resolution[resolution, número] -->
### Variable: resolution

Valor predefinido: `6`


*número* debe ser un número entero mayor que 2, que define el número
de aristas de la base en objetos de clase “cone” o “cylinder”.

<!-- category: Plotting -->
<!-- keywords: restart -->
<!-- signatures: restart[restart, valor] -->
### Variable: restart

Valor predefinido: `false`


Un valor ’true’ significa que la animación recomenzará automáticamente
cuando llegue al final. Escribir simplemente “restart” es equivalente
a escribir [restart, *true*].

<!-- category: Plotting -->
<!-- keywords: scale -->
<!-- signatures: scale[scale, factores] -->
### Variable: scale

Valor predefinido: `[1, 1, 1]`


Tres factores de escala en que serán deformadas las dimensiones del
objeto en relación a los tres ejes. *factors* pueden ser tres número
separados por comas o una lista con tres números. **Ejemplo**:
`[2, 0.5, 1]` estira el objeto suplicando sus dimensiones paralelas
la eje x, reduce a mitad las dimensiones paralelas al eje y, dejando
iguales las dimensiones paralelas al eje z.

<!-- category: Plotting -->
<!-- keywords: scene -->
<!-- signatures: scene(objetos, ..., opciones, ...); -->
### Function: scene ((objetos, ..., opciones, ...);)

Acepta una lista vacía o una lista de varios
`scene_objetos` y `scene_opciones`. El
programa ejecuta Xmaxima, que abre una ventana donde se representan los
objetos dados, en un espacio tridimensional y aplicando las opciones
dadas. Cada objeto debe pertenecer una de las 4 clases: sphere, cube,
cylinder o cone (ver `scene_objetos`). Los
objetos se identifican dando el nombre de su clase, o una lista en que
el primer elemento es el nombre de la clase y los restantes elementos
son opciones para ese objeto.

 

**Ejemplo**. Una pirámide hexagonal con fondo azul:





```maxima
(%i1) scene(cone, [background,"#9980e5"])$
```

![scene1](figures/scene1.png)


Presionando el botón izquierdo del ratón mientras se mueve dentro de la
ventana gráfica, se puede rotar la cámara, mostrando diferentes vistas
de la pirámide. Las dos opciones `scene_elevation` y
`scene_azimuth` se pueden usar también para cambiar la
orientación de la cámara. La cámara se puede mover presionando el botón
del medio y moviendo el ratón y el botón del lado derecho se usa para
aumentar o disminuir el zoom, moviendo el ratón para arriba y para
bajo.


Cada opción de un objeto deberá ser una lista comenzando con el nombre
de la opción, seguido por su valor. La lista de posibles opciones se
encuentra en la sección
`objeto_opciones`.


**Ejemplo**. Este ejemplo mostrará una esfera cayendo para el piso
y rebotando sin perder energía. Para comenzar o poner en pausa la
animación se debe oprimir el botón de play/pausa.













```maxima
(%i1) p: makelist ([0,0,2.1- 9.8*t^2/2], t, 0, 0.64, 0.01)$

(%i2) p: append (p, reverse(p))$

(%i3) bola: [sphere, [radius,0.1], [thetaresolution,20],
  [phiresolution,20], [position,0,0,2.1], [color,red],
  [animate,position,p]]$

(%i4) piso: [cube, [xlength,2], [ylength,2], [zlength,0.2],
  [position,0,0,-0.1],[color,violet]]$

(%i5) scene (bola, piso, restart)$
```

![scene2](figures/scene2.png)


La opción *restart* fue usada para hacer que la animación recomienze
cada vez que se llega al último punto en la lista. Los valores
permitidos para los colores son los mismo que para la opción `color`
de plot2d.

See also: `scene_objetos`, `scene_opciones`, `scene_elevation`, `scene_azimuth`, `objeto_opciones`, `color`.

<!-- category: Plotting -->
<!-- keywords: sphere -->
<!-- signatures: sphere[sphere, opciones] -->
### Variable: sphere

Una esfera de radio igual a 0.5 unidades y centro en el origen.

<!-- category: Plotting -->
<!-- keywords: staircase -->
<!-- signatures: staircase(F, y0, n, opciones, ...); -->
### Function: staircase ((F, y0, n, opciones, ...);)

Dibuja un diagrama de escalera (o diagrama de red) para la sucesión
definida por la ecuación de recurrencia


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


La interpretación y valores permitidos de los parámetros de entrada
es la misma que para la función `evolution`. Un diagrama de
escalera consiste en una gráfica de la función *F(y)*, junto con
la recta *G(y)* `=` *y*. Se comienza por dibujar un
segmento vertical desde el punto (*y0*, *y0*) en la recta, hasta
el punto de intersección con la función *F*. En seguida, desde
ese punto se dibuja un segmento horizontal hasta el punto de
intersección con la recta, (*y1*, *y1*); el procedimiento se
repite *n* veces hasta alcanzar el punto (*yn*, *yn*). Esta
función acepta las mismas opciones que `plot2d`.


**Ejemplo**.



```maxima
(%i1) staircase(cos(y), 1, 11, [y, 0, 1.2]);
```

![dynamics2](figures/dynamics2.png)

See also: `plot2d`.

<!-- category: Plotting -->
<!-- keywords: startphi -->
<!-- signatures: startphi[startphi, ángulo] -->
### Variable: startphi

Valor predefinido: `0`


En una esfera, phi es el ángulo en el plano vertical que pasa por el eje
z, medido a partir de la parte positiva del eje z. *ángulo* debe ser
un múmero entre 0 y 180 que determina el valor inicial de phi desde donde
se mostrará la superficie. Valores superiores a 0 eliminan una parte de
la superficie.


Consulte también `objeto_endphi` y
`objeto_phiresolution`.

See also: `objeto_endphi`, `objeto_phiresolution`.

<!-- category: Plotting -->
<!-- keywords: starttheta -->
<!-- signatures: starttheta[starttheta, ángulo] -->
### Variable: starttheta

Valor predefinido: `0`


En una esfera, theta es el ángulo en el plano horizontal (longitud),
medido desde la parte positiva del eje x. *ángulo* debe ser un
número entre 0 y 360 que determina el valor inicial donde la superficie
comienza. Valores mayores que 0 hacen que se elimine una parte de la
superficie de la esfera.


Consulte también `objeto_endtheta` y
`objeto_thetaresolution`.

See also: `objeto_endtheta`, `objeto_thetaresolution`.

<!-- category: Plotting -->
<!-- keywords: surface -->
<!-- signatures: surface[surface] -->
### Variable: surface

Hace que se muestre la superficie del objeto y no los las líneas ni los
vértices de la triangulación usada para construirlo. Ese es el
comportamiento habitual que se puede alterar con las opciones
`objeto_points` o `objeto_wireframe`.

See also: `objeto_points`, `objeto_wireframe`.

<!-- category: Plotting -->
<!-- keywords: thetaresolution -->
<!-- signatures: thetaresolution[thetaresolution, num] -->
### Variable: thetaresolution

Valor predefinido: ``


Número de sub-intervalos en que se divide el intervalo de valores del
ángulo theta, que comienza en `objeto_starttheta` y termina
en `objeto_endtheta`. *num* debe ser un número entero
positivo.
Consulte también `objeto_starttheta` y
`objeto_endtheta`.

See also: `objeto_starttheta`, `objeto_endtheta`.

<!-- category: Plotting -->
<!-- keywords: track -->
<!-- signatures: track[track, posiciones] -->
### Variable: track

*posiciones* deberá ser una lista de puntos. Cuando se oprime el
botón de “play”, la posición del objeto tomara secuencialmente los
valores en la lista, a intervalos regulares de tiempo definidos por la
opción `scene_tstep`, dejando un rastro de la
trayectoria del objeto. El botón de volver al comienzo puede usarse para
recomenzar desde el principio de la lista, haciendo que la animación
comience nuevamente cuando se presione otra vez el botón de play.


**Ejemplo**. Estos comandos muestran la trayectoria de una bola
lanzada con velocidad inicial de 5 m/s, a un ángulo de 45 grados, cuando
se puede ignorar la resistencia del aire:



```maxima
(%i1) p: makelist ([0,4*t,4*t- 9.8*t^2/2], t, 0, 0.82, 0.01)$

(%i2) bola: [sphere, [radius,0.1], [color,red], [track,p]]$

(%i3) piso: [cube, [xlength,2], [ylength,4], [zlength,0.2],
      [position,0,1.5,-0.2],[color,green]]$

(%i4) scene (bola, piso)$
```


Consulte también `objeto_animation`.

See also: `scene_tstep`, `objeto_animation`.

<!-- category: Plotting -->
<!-- keywords: tstep -->
<!-- signatures: tstep[tstep, tiempo] -->
### Variable: tstep

Valor predefinido: `10`


El intervalo de tiempo, en milisegundos, entre iteraciones consecutivas
de las partes de una animación. *tiempo* debe ser un número real.

<!-- category: Plotting -->
<!-- keywords: width -->
<!-- signatures: width[width, pixels] -->
### Variable: width

Valor predefinido: `500`


El ancho, en pixels, de la ventana gráfica. *pixels* deberá ser un
número entero positivo.

<!-- category: Plotting -->
<!-- keywords: windowname -->
<!-- signatures: windowname[windowtitle, nombre] -->
### Variable: windowname

Valor predefinido: `.scene`


*nombre* deberá ser una secuencia de caracteres que pueda ser usada
para el nombre de una ventana de Tk, creada por Xmaxima para los
gráficos de `scene`. El valor predefinido `.scene` implica que
será creada una nueva ventana.

<!-- category: Plotting -->
<!-- keywords: windowtitle -->
<!-- signatures: windowtitle[windowtitle, nombre] -->
### Variable: windowtitle

Valor predefinido: `Xmaxima: scene`


*nombre* debe ser una secuencia de caracteres que serán escritos en
el encabezado de la ventana creada por  `scene`.

<!-- category: Plotting -->
<!-- keywords: wireframe -->
<!-- signatures: wireframe[wireframe] -->
### Variable: wireframe

Esta opción hace que en vez de que se muestre la superficie, se muestren
únicamente las aristas de la triangulación usada para construir la
superficie. **Ejemplo**: `[cube, [wireframe]]`


Consulte también `objeto_surface` y
`objeto_points`.

See also: `objeto_surface`, `objeto_points`.

<!-- category: Plotting -->
<!-- keywords: xlength -->
<!-- signatures: xlength[xlength, altura] -->
### Variable: xlength

Valor predefinido: `1`


Altura de un objeto de clase “cube”, en la dirección x. *altura*
debe ser un número positivo. Consulte también
`objeto_ylength` y `objeto_zlength`.

See also: `objeto_ylength`, `objeto_zlength`.

<!-- category: Plotting -->
<!-- keywords: ylength -->
<!-- signatures: ylength[ylength, altura] -->
### Variable: ylength

Valor predefinido: `1`


Altura de un objeto de clase “cube”, en la dirección y. *altura*
debe ser un número positivo. Consulte también
`objeto_xlength` y `objeto_zlength`.

See also: `objeto_xlength`, `objeto_zlength`.

<!-- category: Plotting -->
<!-- keywords: zlength -->
<!-- signatures: zlength[zlength, altura] -->
### Variable: zlength

Valor predefinido: `1`


Altura de un objeto de clase “cube”, en la dirección z. *altura*
debe ser un número positivo. Consulte también
`objeto_xlength` y `objeto_ylength`.

See also: `objeto_xlength`, `objeto_ylength`.

