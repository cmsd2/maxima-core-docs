## fractals

<!-- category: Other -->
<!-- keywords: fernfale -->
<!-- signatures: fernfale(n) -->
### Function: fernfale (n)

4 aplicaciones contractivas, cuyas probabilidades de selección deben estar
relacionadas con su constante de contracción. El argumento *n* debe ser
suficientemente alto, 10000 o mayor.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,fernfale(n)], [style,dots])$
```

<!-- category: Other -->
<!-- keywords: hilbertmap -->
<!-- signatures: hilbertmap(nn) -->
### Function: hilbertmap (nn)

Curva de Hilbert. El argumento *nn* debe ser pequeño (por ejemplo, 5).
Maxima se puede detener si *nn* es 7 o mayor.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,hilbertmap(6)])$
```

<!-- category: Other -->
<!-- keywords: julia_parameter -->
<!-- signatures: julia_parameter -->
### Variable: julia_parameter

Valor por defecto: `%i`


Parámetro complejo para fractales de Julia. Su valor por defecto es `%i`,
y otros que se sugieren son: `-.745+%i*.113002`, `-.39054-%i*.58679`,
`-.15652+%i*1.03225`, `-.194+%i*.6557` y `.011031-%i*.67037`.

<!-- category: Other -->
<!-- keywords: julia_set -->
<!-- signatures: julia_set(x, y) -->
### Function: julia_set (x, y)

Conjuntos de Julia.


Esta función debe realizar muchas operaciones y puede tardar bastante
tiempo en ejecutarse, tiempo que también depende del número de puntos
de la malla.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) plot3d (julia_set, [x, -2, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


Véase también `julia_parameter`.

<!-- category: Other -->
<!-- keywords: julia_sin -->
<!-- signatures: julia_sin(x, y) -->
### Function: julia_sin (x, y)

Mientras que la función `julia_set` implementa la transformación 
`julia_parameter+z^2`, la función `julia_sin` implementa 
`julia_parameter*sin(z)`. Véase el código fuente para más detalles.


Este programa es lento porque calcula muchos senos; el tiempo de ejecución 
también depende del número de puntos de la malla.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) julia_parameter:1+.1*%i$
(%i3) plot3d (julia_sin, [x, -2, 2], [y, -3, 3], 
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


Véase también `julia_parameter`.

<!-- category: Other -->
<!-- keywords: mandelbrot_set -->
<!-- signatures: mandelbrot_set(x, y) -->
### Function: mandelbrot_set (x, y)

Conjunto de Mandelbrot.


Esta función debe realizar muchas operaciones y puede tardar bastante
tiempo en ejecutarse, tiempo que también depende del número de puntos
de la malla.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) plot3d (mandelbrot_set, [x, -2.5, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```

<!-- category: Other -->
<!-- keywords: sierpinskiale -->
<!-- signatures: sierpinskiale(n) -->
### Function: sierpinskiale (n)

Triángulo de Sierpinski: 3 aplicaciones contractivas; constante de contracción de 0.5
y traslaciones. Todas las aplicaciones tienen la misma constante de contracción. El argumento
*n* debe ser suficientemente alto, 10000 o mayor.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,sierpinskiale(n)], [style,dots])$
```

<!-- category: Other -->
<!-- keywords: sierpinskimap -->
<!-- signatures: sierpinskimap(nn) -->
### Function: sierpinskimap (nn)

Curva de Sierpinski. El argumento *nn* debe ser pequeño (por ejemplo, 5).
Maxima se puede detener si *nn* es 7 o mayor.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,sierpinskimap(6)])$
```

<!-- category: Other -->
<!-- keywords: snowmap -->
<!-- signatures: snowmap(ent, nn) -->
### Function: snowmap (ent, nn)

Copos de Koch. La función `snowmap` dibuja el copo de Koch
sobre los vértices de un polígono convexo inicial del
plano complejo. La orientación del polígono es importante.
El argumento *nn* es el número de recursividades de la transformación
de Koch, el cual debe ser pequeño (5 o 6).


Ejemplos:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,
              snowmap([1,exp(%i*%pi*2/3),exp(-%i*%pi*2/3),1],4)])$
(%i3) plot2d([discrete,
              snowmap([1,exp(-%i*%pi*2/3),exp(%i*%pi*2/3),1],4)])$
(%i4) plot2d([discrete, snowmap([0,1,1+%i,%i,0],4)])$
(%i5) plot2d([discrete, snowmap([0,%i,1+%i,1,0],4)])$
```

<!-- category: Other -->
<!-- keywords: treefale -->
<!-- signatures: treefale(n) -->
### Function: treefale (n)

3 aplicaciones contractivas, todas ellas con el mismo coeficiente
de contracción. El argumento *n* debe ser suficientemente alto, 10000 o mayor.


Ejemplo:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,treefale(n)], [style,dots])$
```

