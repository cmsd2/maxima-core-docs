## fractals

<!-- category: Other -->
<!-- keywords: fernfale -->
<!-- signatures: fernfale(n) -->
### Function: fernfale (n)

4 contractive maps, the probability to choice a transformation must be related 
with the contraction ratio. Argument *n* must be great enough, 10000 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,fernfale(n)], [style,dots])$
```

<!-- category: Other -->
<!-- keywords: hilbertmap -->
<!-- signatures: hilbertmap(nn) -->
### Function: hilbertmap (nn)

Hilbert map. Argument *nn* must be small (5, for example).
Maxima can crash if *nn* is 7 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,hilbertmap(6)])$
```

<!-- category: Other -->
<!-- keywords: julia_parameter -->
<!-- signatures: julia_parameter -->
### Variable: julia_parameter

Default value: `%i`


Complex parameter for Julia fractals.
Its default value is `%i`; we  suggest the  values `-.745+%i*.113002`, 
`-.39054-%i*.58679`, `-.15652+%i*1.03225`, `-.194+%i*.6557` and 
`.011031-%i*.67037`.

See also: `%i`.

<!-- category: Other -->
<!-- keywords: julia_set -->
<!-- signatures: julia_set(x, y) -->
### Function: julia_set (x, y)

Julia sets.


This program is time consuming because it must make a lot of operations; 
the computing time is also related with the number of grid points.


Example:



```maxima
(%i1) load("fractals")$
(%i2) plot3d (julia_set, [x, -2, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


See also `julia_parameter`.

See also: `julia_parameter`.

<!-- category: Other -->
<!-- keywords: julia_sin -->
<!-- signatures: julia_sin(x, y) -->
### Function: julia_sin (x, y)

While function `julia_set` implements the transformation `julia_parameter+z^2`,
function `julia_sin` implements `julia_parameter*sin(z)`. See source code
for more details.


This program runs slowly  because it calculates a lot of sines.


Example:


This program is time consuming because it must make a lot of operations; 
the computing time is also related with the number of grid points.



```maxima
(%i1) load("fractals")$
(%i2) julia_parameter:1+.1*%i$
(%i3) plot3d (julia_sin, [x, -2, 2], [y, -3, 3], 
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


See also `julia_parameter`.

See also: `julia_parameter`.

<!-- category: Other -->
<!-- keywords: mandelbrot_set -->
<!-- signatures: mandelbrot_set(x, y) -->
### Function: mandelbrot_set (x, y)

Mandelbrot set.


Example:


This program is time consuming because it must make a lot of operations; 
the computing time is also related with the number of grid points.



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

Sierpinski Triangle: 3 contractive maps; .5 contraction constant and translations;
all maps have the same contraction ratio. Argument *n* must be great enough, 10000 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,sierpinskiale(n)], [style,dots])$
```

<!-- category: Other -->
<!-- keywords: sierpinskimap -->
<!-- signatures: sierpinskimap(nn) -->
### Function: sierpinskimap (nn)

Sierpinski map. Argument *nn* must be small (5, for example).
Maxima can crash if *nn* is 7 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,sierpinskimap(6)])$
```

<!-- category: Other -->
<!-- keywords: snowmap -->
<!-- signatures: snowmap(ent, nn) -->
### Function: snowmap (ent, nn)

Koch snowflake sets. Function `snowmap` plots the snow Koch map 
over the vertex of an initial closed polygonal, in the complex plane. Here  
the orientation of the polygon is important. Argument *nn* is the number of 
recursive applications of Koch transformation; *nn* must be small (5 or 6).


Examples:



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

3 contractive maps all with the same contraction ratio.
Argument *n* must be great enough, 10000 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,treefale(n)], [style,dots])$
```

