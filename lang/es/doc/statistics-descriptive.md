## descriptive

<!-- category: Statistics -->
<!-- keywords: barsplot, barsplot_description -->
<!-- signatures: barsplot(data1, data2, ..., option_1, option_2, ...), barsplot_description(...) -->
### Function: barsplot (data1, data2, ..., option_1, option_2, ...)

Dibuja diagramas de barras para variables estadísticas
discretas, tanto para una como para más muestras.


*data* puede ser una lista de resultados provenientes de una muestra
o una matriz de *m* filas y *n* columnas, representando *n* 
muestras de tamaño *m* cada una.


Las opciones disponibles son:



- *
*grouping* (valor por defecto, `clustered`): indica cómo se agrupan las 
diferentes muestras. Son valores válidos: `clustered` y `stacked`.
- *
*groups_gap* (valor por defecto, `1`): un número positivo que representa
la separación entre dos grupos consecutivos de barras.
- *
*bars_colors* (valor por defecto, `[]`): una lista de colores para múltiples 
muestras. Cuando el número de muestras sea mayor que el de colores especificados, 
los colores adicionales necesarios se seleccionan aleatoriamente. Véase `color` para más
información.
- *
*frequency* (valor por defecto, `absolute`): indica la escala de las ordenadas.
Valores admitidos son:  `absolute`, `relative` y and `percent`.
- *
*ordering* (valor por defecto, `orderlessp`): los valores admitidos para esta 
opción son: `orderlessp` y `ordergreatp`, indicando cómo se deben ordenar
los resultados muestrales sobre el eje-*x*.
- *
*sample_keys* (valor por defecto, `[]`): es una lista de cadenas de 
texto a usar como leyendas. Cuando la lista tenga una longitud diferente de cero o 
del número de muestras, se devolverá un mensaje de error.
- *
*start_at* (valor por defecto, `0`): indica a qué altura comienza 
a dibujarse el gráfico de barra sobre el eje de abscisas.
- *
Todas las opciones globales de `draw`, excepto `xtics`, que se asigna
internamente por `barsplot`. Si es necesario que el usuario le dé su propio
valor a esta opción, o quiere construir una escena más compleja,
debe hacer uso de `barsplot_description`. Véase el ejemplo más abajo.
- *
Las siguientes opciones locales de `draw`: `key`, `color`, 
`fill_color`, `fill_density` y `line_width`. Véase también
`bars`.


La función `barsplot_description` crea un objeto gráfico
útil para formar escenas complejas, junto con otros objetos gráficos.
Se dispone también de la función `wxbarsplot` para crear
histogramas incorporados en los interfaces wxMaxima y iMaxima.


Ejemplos:


Muestra univariante en formato matricial. Frecuencias absolutas.













```maxima
(%i1) load ("descriptive")$
(%i2) m : read_matrix (file_search ("biomed.data"))$

(%i3) barsplot(
        col(m,2),
        title        = "Ages",
        xlabel       = "years",
        box_width    = 1/2,
        fill_density = 3/4)$
```


Dos muestras de diferente tamaño, con frecuencias
relativas y colores definidos por el usuario.















```maxima
(%i1) load ("descriptive")$
(%i2) l1:makelist(random(10),k,1,50)$
(%i3) l2:makelist(random(10),k,1,100)$

(%i4) barsplot(
        l1,l2,
        box_width    = 1,
        fill_density = 1,
        bars_colors  = [black, grey],
        frequency = relative,
        sample_keys = ["A", "B"])$
```


Cuatro muestras no numéricas de igual tamaño.
















```maxima
(%i1) load ("descriptive")$

(%i2) barsplot(
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        title  = "Asking for something to four groups",
        ylabel = "# of individuals",
        groups_gap   = 3,
        fill_density = 0.5,
        ordering     = ordergreatp)$
```


Barras apiladas verticalmente.
















```maxima
(%i1) load ("descriptive")$

(%i2) barsplot(
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        title  = "Asking for something to four groups",
        ylabel = "# of individuals",
        grouping     = stacked,
        fill_density = 0.5,
        ordering     = ordergreatp)$
```


`barsplot` en un contexto multiplot.



```maxima
(%i1) load ("descriptive")$
(%i2) l1:makelist(random(10),k,1,50)$
(%i3) l2:makelist(random(10),k,1,100)$
(%i4) bp1 : 
        barsplot_description(
         l1,
         box_width = 1,
         fill_density = 0.5,
         bars_colors = [blue],
         frequency = relative)$
(%i5) bp2 : 
        barsplot_description(
         l2,
         box_width = 1,
         fill_density = 0.5,
         bars_colors = [red],
         frequency = relative)$
(%i6) draw(gr2d(bp1), gr2d(bp2))$
```


Para las opciones relacionadas con los diagramas de barras, véase `bars`
del paquete `draw`.


Véanse también las funciones `histogram` y `piechart`.

<!-- category: Statistics -->
<!-- keywords: boxplot, boxplot_description -->
<!-- signatures: boxplot(data), boxplot(data, option_1, option_2, ...), boxplot_description(...) -->
### Function: boxplot (data)

Dibuja diagramas de cajas (box-and-whishker). El argumento *data* puede
ser una lista, lo cual no es de gran interés, puesto que estos gráficos 
se utilizan principalmente para comparar distintas muestras, o una matriz,
de manera que sea posible comparar dos o más componentes de una muestra
multivariante. También se permite que *data* sea una lista de muestras
con posibles tamaños diferentes; de hecho, esta es la única función
del paquete `descriptive` que admite esta estructura de datos.


La caja se dibuja desde el primer cuartil hasta el tercero, con un segmento
horizontal situado a la altura del segundo cuartil o mediana. Por defecto,
los bigotes inferior y superior se sitúan a la altura de los valores mínimo
y máximo, respectivamente. La opción *range* se puede utilizar para indicar
que los valores mayores que
`quantile(x,3/4)+range*(quantile(x,3/4)-quantile(x,1/4))`,
o menores que
`quantile(x,1/4)-range*(quantile(x,3/4)-quantile(x,1/4))`,
deben considerarse atípicos, en cuyo caso se dibujan como puntos aislados, al
tiempo que los bigotes se colocan en los extremos del resto de la muestra.


Opciones disponibles:



- *
*box_width* (valor por defecto, `3/4`): ancho relativo de las cajas.
This  value must be in the range `[0,1]`.
- *
*box_orientation* (valor por defecto, `vertical`): valores posibles: `vertical`
y `horizontal`.
- *
*range* (valor por defecto, `inf`): coeficiente positivo del rango intercuartílico para
declarar los límites de los datos atípicos.
- *
*outliers_size* (valor por defecto, `1`): tamaño de los círculos para los datos atípicos.
- *
Todas las opciones globales de `draw`, excepto `points_joined`, 
`point_size`, `point_type`, `xtics`, `ytics`, `xrange`
y `yrange`, que se asignan internamente por `boxplot`. Si es necesario 
que el usuario le dé sus propios valores a estas opciones, o quiere construir 
una escena más compleja, debe hacer uso de `boxplot_description`.
- *
Las siguientes opciones locales de `draw`: `key`, `color`, 
y `line_width`.


La función `boxplot_description` crea un objeto gráfico
útil para formar escenas complejas, junto con otros objetos gráficos.
Se dispone también de la función `wxboxplot` para crear
histogramas incorporados en los interfaces wxMaxima y iMaxima.


Ejemplos:


Diagrama de cajas de una muestra multivariante.













```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix(file_search("wind.data"))$

(%i3) boxplot(s2,
        box_width  = 0.2,
        title      = "Windspeed in knots",
        xlabel     = "Stations",
        color      = red,
        line_width = 2)$
```


Diagrama de cajas de tres muestras de tamaños diferentes.











```maxima
(%i1) load ("descriptive")$

(%i2) A :
       [[6, 4, 6, 2, 4, 8, 6, 4, 6, 4, 3, 2],
        [8, 10, 7, 9, 12, 8, 10],
        [16, 13, 17, 12, 11, 18, 13, 18, 14, 12]]$

(%i3) boxplot (A, box_orientation = horizontal)$
```


La opción *range* puede utilizarse para tratar con datos atípicos.





















```maxima
(%i1) load ("descriptive")$
(%i2) B: [[7, 15, 5, 8, 6, 5, 7, 3, 1],
          [10, 8, 12, 8, 11, 9, 20],
          [23, 17, 19, 7, 22, 19]] $

(%i3) boxplot (B, range=1)$
(%i4) boxplot (B, range=1.5, box_orientation = horizontal)$


(%i5) draw2d(
        boxplot_description(
          B,
          range            = 1.5,
          line_width       = 3,
          outliers_size    = 2,
          color            = red,
          background_color = light_gray),
        xtics = {["Low",1],["Medium",2],["High",3]}) $
```

<!-- category: Statistics -->
<!-- keywords: build_sample -->
<!-- signatures: build_sample(list), build_sample(matrix) -->
### Function: build_sample (list)

Construye una muestra a partir de una tabla de frecuencias absolutas.
La tabla de entrada puede ser una una matriz o una lista de listas,
todas ellas de igual tamaño. El número de columnas o la longitud de
las listas debe ser mayor que la unidad. El último elemento de cada
fila o lista se interpreta como la frecuencia absoluta.
El resultado se devuelve siempre en formato de matriz.


Ejemplos:


Tabla de frecuencias univariante.









```maxima
(%i1) load ("descriptive")$
(%i2) sam1: build_sample([[6,1], [j,2], [2,1]]);
                       [ 6 ]
                       [   ]
                       [ j ]
(%o2)                  [   ]
                       [ j ]
                       [   ]
                       [ 2 ]
(%i3) mean(sam1);
                      2 j + 8
(%o3)                [-------]
                         4
(%i4) barsplot(sam1) $
```


Tabla de frecuencias multivariante.









```maxima
(%i1) load ("descriptive")$
(%i2) sam2: build_sample([[6,3,1], [5,6,2], [u,2,1],[6,8,2]]) ;
                           [ 6  3 ]
                           [      ]
                           [ 5  6 ]
                           [      ]
                           [ 5  6 ]
(%o2)                      [      ]
                           [ u  2 ]
                           [      ]
                           [ 6  8 ]
                           [      ]
                           [ 6  8 ]
(%i3) cov(sam2);
       [   2                 2                            ]
       [  u  + 158   (u + 28)     2 u + 174   11 (u + 28) ]
       [  -------- - ---------    --------- - ----------- ]
(%o3)  [     6          36            6           12      ]
       [                                                  ]
       [ 2 u + 174   11 (u + 28)            21            ]
       [ --------- - -----------            --            ]
       [     6           12                 4             ]
(%i4) barsplot(sam2, grouping=stacked) $
```

<!-- category: Statistics -->
<!-- keywords: cdf_empirical -->
<!-- signatures: cdf_empirical(list, option...), cdf_empirical(matrix, option...) -->
### Function: cdf_empirical (list, option...)

Función de distribución empírica $F(x)$.


Los datos se pueden introducir como una lista de números o como una matriz
columna.


El argumento opcional es el nombre de la variable en la expresión devuelta, la cual
es *x* por defecto.


Ejemplo:


Función de distribución empírica.













```maxima
(%i1) load ("descriptive")$

(%i2) F(x):= ''(cdf_empirical([1,3,3,5,7,7,7,8,9]));
(%o2) F(x) := (charfun(x >= 9) + charfun(x >= 8)
               + 3 charfun(x >= 7) + charfun(x >= 5)
               + 2 charfun(x >= 3) + charfun(x >= 1))/9


(%i3) F(6);
                           4
(%o3)                      -
                           9

(%i4) load("draw")$
(%i5) draw2d(
        line_width = 3,
        grid       = true,
        explicit(F(z), z, -2, 12)) $
```

<!-- category: Statistics -->
<!-- keywords: central_moment -->
<!-- signatures: central_moment(list, k), central_moment(matrix, k) -->
### Function: central_moment (list, k)

Es el momento central de orden $k$, definido como


```maxima
n
                  ====
              1   \          _ k
              -    >    (x - x)
              n   /       i
                  ====
                  i = 1
```


$$
{{1\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^k}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) central_moment (s1, 2), numer; /* the variance */
(%o3)                   8.425899999999999


(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%o5) [11.29584771375004, 16.97988248298583, 5.626661952750102, 
                             37.5986572057918, 25.85981904394192]

(%i6) central_moment (s2, 3);
```


Véanse también `central_moment` y `mean`.

<!-- category: Statistics -->
<!-- keywords: continuous_freq -->
<!-- signatures: continuous_freq(list), continuous_freq(list, m) -->
### Function: continuous_freq (list)

El argumento de `continuous_freq` debe ser una lista de números.
Divide el rango en intervalos y cuenta cuántos valores hay en ellos.
El segundo argumento es opcional y puede ser el número de clases 
deseado, 10 por defecto, o una lista que contenga los límites
de las clases y el número de éstas, o una lista que contenga
únicamente los límites. Si los valores muestrales
son todos iguales, esta función devuelve solamente una clase 
de amplitud 2.


Ejemplos:


El argumento opcional indica el número de clases deseadas. 
La primera lista de la respuesta contiene los límites
de los intervalos y la segunda los totales correspondientes: hay 16
dígitos en el intervalo `[0, 1.8]`, 24 en 
`(1.8, 3.6]` y así sucesivamente.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, 5);
(%o3) [[0, 1.8, 3.6, 5.4, 7.2, 9.0], [16, 24, 18, 17, 25]]
```


El argumento opcional indica que queremos 7 clases con 
límites -2 y 12:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, [-2,12,7]);
(%o3) [[- 2, 0, 2, 4, 6, 8, 10, 12], [8, 20, 22, 17, 20, 13, 0]]
```


El argumento opcional indica que queremos el número por defecto
de clases y límites -2 y 12:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, [-2,12]);
                3  4  11  18     32  39  46  53
(%o3)  [[- 2, - -, -, --, --, 5, --, --, --, --, 12], 
                5  5  5   5      5   5   5   5
               [0, 8, 20, 12, 18, 9, 8, 25, 0, 0]]
```

<!-- category: Statistics -->
<!-- keywords: cor -->
<!-- signatures: cor(matrix), cor(matrix, options...) -->
### Function: cor (matrix)

Es la matriz de correlaciones de la muestra multivariante.


Opción:



- *
`'data`, por defecto `'true`, indica si la matriz de entrada contiene los datos muestrales,
en cuyo caso la matriz de covarianzas `cov1` debe ser calculada; en caso contrario, se le debe
pasar ésta a la función como matriz simétrica en lugar de los datos.


Ejemplo:









```maxima
(%i1) load ("descriptive")$
(%i2) fpprintprec:7$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) cor (s2);
      [   1.0     .8476339  .8803515  .8239624  .7519506 ]
      [                                                  ]
      [ .8476339    1.0     .8735834  .6902622  0.782502 ]
      [                                                  ]
(%o4) [ .8803515  .8735834    1.0     .7764065  .8323358 ]
      [                                                  ]
      [ .8239624  .6902622  .7764065    1.0     .7293848 ]
      [                                                  ]
      [ .7519506  0.782502  .8323358  .7293848    1.0    ]
```


Cálculo de la matriz de correlaciones a partir de la matriz de covarianzas.










```maxima
(%i1) load ("descriptive")$
(%i2) fpprintprec : 7 $
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) s : cov1 (s2)$

(%i5) cor (s, data=false); /* this is faster */
      [   1.0     .8476339  .8803515  .8239624  .7519506 ]
      [                                                  ]
      [ .8476339    1.0     .8735834  .6902622  0.782502 ]
      [                                                  ]
(%o5) [ .8803515  .8735834    1.0     .7764065  .8323358 ]
      [                                                  ]
      [ .8239624  .6902622  .7764065    1.0     .7293848 ]
      [                                                  ]
      [ .7519506  0.782502  .8323358  .7293848    1.0    ]
```


Véanse también `cov` y `cov1`.

<!-- category: Statistics -->
<!-- keywords: cov -->
<!-- signatures: cov(matrix) -->
### Function: cov (matrix)

Es la matriz de covarianzas de una muestra multivariante, definida como


```maxima
n
             ====
          1  \           _        _
      S = -   >    (X  - X) (X  - X)'
          n  /       j        j
             ====
             j = 1
```


$$
{S={1\over{n}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}
$$


siendo $X_j$ la $j$-ésima fila de la matriz muestral.


Ejemplo:









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec : 7$  /* change precision for pretty output */
      [ 17.22191  13.61811  14.37217  19.39624  15.42162 ]
      [                                                  ]
      [ 13.61811  14.98774  13.30448  15.15834  14.9711  ]
      [                                                  ]
(%o4) [ 14.37217  13.30448  15.47573  17.32544  16.18171 ]
      [                                                  ]
      [ 19.39624  15.15834  17.32544  32.17651  20.44685 ]
      [                                                  ]
      [ 15.42162  14.9711   16.18171  20.44685  24.42308 ]
(%i5) cov (s2);
```


Véase también `cov1`.

<!-- category: Statistics -->
<!-- keywords: cov1 -->
<!-- signatures: cov1(matrix) -->
### Function: cov1 (matrix)

Es la matriz de cuasivarianzas de una muestra multivariante, definida como


```maxima
n
             ====
         1   \           _        _
   S  = ---   >    (X  - X) (X  - X)'
    1   n-1  /       j        j
             ====
             j = 1
```


$$
{{1\over{n-1}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}
$$


siendo $X_j$ la $j$-ésima fila de la matriz muestral.


Ejemplo:









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec : 7$ /* change precision for pretty output */
      [ 17.39587  13.75567  14.51734  19.59216  15.5774  ]
      [                                                  ]
      [ 13.75567  15.13913  13.43887  15.31145  15.12232 ]
      [                                                  ]
(%o4) [ 14.51734  13.43887  15.63205  17.50044  16.34516 ]
      [                                                  ]
      [ 19.59216  15.31145  17.50044  32.50153  20.65338 ]
      [                                                  ]
      [ 15.5774   15.12232  16.34516  20.65338  24.66977 ]
(%i5) cov1 (s2);
```


Véase también `cov`.

<!-- category: Statistics -->
<!-- keywords: cv -->
<!-- signatures: cv(list), cv(matrix) -->
### Function: cv (list)

Es el coeficiente de variación, o cociente entre la desviación típica muestral (`std`) y la media (`mean`),










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) cv (s1), numer;
(%o3)                   .6193977819764815

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) cv (s2);
(%o5) [.4192426091090204, .3829365309260502, 0.363779605385983, 
                            .3627381836021478, .3346021393989506]
```


Véanse también `std` y `mean`.

<!-- category: Statistics -->
<!-- keywords: discrete_freq -->
<!-- signatures: discrete_freq(list) -->
### Function: discrete_freq (list)

Calcula las frecuencias absolutas en muestras discretas, tanto numéricas como categóricas. Su único argumento debe ser una lista.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) discrete_freq (s1);
(%o3) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```



La primera lista son los valores de la muestra y la segunda sus frecuencias absolutas. Las instrucciones `? col` y 
`? transpose` pueden ayudar a comprender la última entrada.

<!-- category: Statistics -->
<!-- keywords: geometric_mean -->
<!-- signatures: geometric_mean(list), geometric_mean(matrix) -->
### Function: geometric_mean (list)

Es la media geométrica, definida como


```maxima
/  n      \ 1/n
                 | /===\   |
                 |  ! !    |
                 |  ! !  x |
                 |  ! !   i|
                 | i = 1   |
                 \         /
```


$$
\left(\prod_{i=1}^{n}{x_{i}}\right)^{{{1}\over{n}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$

(%i3) geometric_mean (y), numer;
(%o3)                   4.454845412337012

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) geometric_mean (s2);
(%o5) [8.82476274347979, 9.22652604739361, 10.0442675714889, 
                            14.61274126349021, 13.96184163444275]
```


Véanse también `mean` y `harmonic_mean`.

<!-- category: Statistics -->
<!-- keywords: global_variances -->
<!-- signatures: global_variances(matrix), global_variances(matrix, options...) -->
### Function: global_variances (matrix)

La función `global_variances` devuelve una lista de medidas globales de variabilidad:



- *
*varianza total*: `trace(S_1)`,
- *
*varianza media*: `trace(S_1)/p`,
- *
*varianza generalizada*: `determinant(S_1)`,
- *
*desviación típica generalizada*: `sqrt(determinant(S_1))`,
- *
*varianza efectiva* `determinant(S_1)^(1/p)`, (definida en: Peña, D. (2002) *Análisis de datos multivariantes*; McGraw-Hill, Madrid.)
- *
*desviación típica efectiva*: `determinant(S_1)^(1/(2*p))`.

donde *p* es la dimensión de la variable aleatoria multivariante y $S_1$ la matriz de covarianzas devuelta por la función `cov1`.


Opción:



- *
`'data`, por defecto `'true`, indica si la matriz de entrada contiene los datos muestrales,
en cuyo caso la matriz de covarianzas `cov1` debe ser calculada; en caso contrario, se le debe
pasar ésta a la función como matriz simétrica en lugar de los datos.


Ejemplo:








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) global_variances (s2);
(%o3) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608502, 6.636590811800794, 2.576158149609762]
```


Cálculo de `global_variances` a partir de la matriz de covarianzas.









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) s : cov1 (s2)$

(%i4) global_variances (s, data=false);
(%o4) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608502, 6.636590811800794, 2.576158149609762]
```


Véanse también `cov` y `cov1`.

<!-- category: Statistics -->
<!-- keywords: harmonic_mean -->
<!-- signatures: harmonic_mean(list), harmonic_mean(matrix) -->
### Function: harmonic_mean (list)

Es la media armónica, definida como


```maxima
n
               --------
                n
               ====
               \     1
                >    --
               /     x
               ====   i
               i = 1
```


$$
{{n}\over{\sum_{i=1}^{n}{{{1}\over{x_{i}}}}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$

(%i3) harmonic_mean (y), numer;
(%o3)                   3.901858027632205

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) harmonic_mean (s2);
(%o5) [6.948015590052786, 7.391967752360356, 9.055658197151745, 
                            13.44199028193692, 13.01439145898509]
```


Véanse también `mean` y `geometric_mean`.

<!-- category: Statistics -->
<!-- keywords: histogram, histogram_description -->
<!-- signatures: histogram(list), histogram(list, option_1, option_2, ...), histogram(one_column_matrix), histogram(one_column_matrix, option_1, option_2, ...), histogram(one_row_matrix), histogram(one_row_matrix, option_1, option_2, ...), histogram_description(...) -->
### Function: histogram (list)

Dibuja un histograma a partir de una muestra continua. Los datos
muestrales deben darse en forma de lista de números o como una
matriz unidimensional.


Opciones dispponibles:



- *
*nclasses* (valor por defecto, `10`): número de clases del histograma, o
una lista indicando los límites de las clases y su número,
o solamente los límites.
- *
*frequency* (valor por defecto, `absolute`): indica la escala de las ordenadas.
Valores admitidos son:  `absolute`, `relative`, `percent` y `density`.
Con `density`, el histograma adquiere un área total igual a uno.
- *
*htics* (valor por defecto, `auto`): formato para las marcas sobre el
eje de las abscisas. Valores admitidos son: `auto`, `endpoints`, 
`intervals` o una lista de etiquetas.
- *
Todas las opciones globales de `draw`, excepto `xrange`, `yrange`
y `xtics`, que son asignadas internamente por `histogram`.
Si es necesario que el usuario le dé sus propios valores a estas opciones,
debe hacer uso de `histogram_description`. Véase el ejemplo más abajo.
- *
Las siguientes opciones locales de `draw`: `key`, `color`, 
`fill_color`, `fill_density` y `line_width`. Véase también
`bars`.


La función `histogram_description` crea un objeto gráfico
útil para formar escenas complejas, junto con otros objetos gráficos.
Se dispone también de la función `wxhistogram` para crear
histogramas incorporados en los interfaces wxMaxima y iMaxima.


Ejemplos:


Un histograma con seis clases:















```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) histogram (
           s1,
           nclasses     = 8,
           title        = "pi digits",
           xlabel       = "digits",
           ylabel       = "Absolute frequency",
           fill_color   = grey,
           fill_density = 0.6)$
```


Ajustando los límites del histograma a -2 y 12,
con 3 clases. También se establece un formato predefinido a
las marcas del eje de abscisas:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) histogram (
           s1,
           nclasses     = [-2,12,3],
           htics        = ["A", "B", "C"],
           terminal     = png,
           fill_color   = "#23afa0",
           fill_density = 0.6)$
```


Se hace uso de `histogram_description` para ajustar
la opción `xrange` y añadir una curva
explícita a la escena:



```maxima
(%i1) load ("descriptive")$
(%i2) ( load("distrib"),
        m: 14, s: 2,
        s2: random_normal(m, s, 1000) ) $
(%i3) draw2d(
        grid   = true,
        xrange = [5, 25],
        histogram_description(
          s2,
          nclasses     = 9,
          frequency    = density,
          fill_density = 0.5),
        explicit(pdf_normal(x,m,s), x, m - 3*s, m + 3* s))$
```

<!-- category: Statistics -->
<!-- keywords: km -->
<!-- signatures: km(list, option...), km(matrix, option...) -->
### Function: km (list, option...)

Estimador Kaplan-Meier de la función de supervivencia o fiabilidad $S(x)=1-F(x)$.


Los datos se pueden introducir como una lista de pares de números o como una
matriz de dos columnas. La primera componente es el tiempo observado y la 
segunda componente es el índice de censura (1 = no censurado, 0 = censurado por
la derecha).


El argumento opcional es el nombre de la variable en la expresión devuelta, la cual
es *x* por defecto.


Ejemplos:


Muestra como una lista de pares.











```maxima
(%i1) load ("descriptive")$

(%i2) S: km([[2,1], [3,1], [5,0], [8,1]]);
                       charfun((3 <= x) and (x < 8))
(%o2) charfun(x < 0) + -----------------------------
                                     2
                3 charfun((2 <= x) and (x < 3))
              + ------------------------------- 
                               4
              + charfun((0 <= x) and (x < 2))

(%i3) load ("draw")$

(%i4) draw2d(
        line_width = 3, grid = true,
        explicit(S, x, -0.1, 10))$
```


Estimación de probabilidades de supervivencia.








```maxima
(%i1) load ("descriptive")$
(%i2) S(t):= ''(km([[2,1], [3,1], [5,0], [8,1]], t)) $

(%i3) S(6);
                            1
(%o3)                       -
                            2
```

<!-- category: Statistics -->
<!-- keywords: kurtosis -->
<!-- signatures: kurtosis(list), kurtosis(matrix) -->
### Function: kurtosis (list)

Es el coeficiente de curtosis, definido como


```maxima
n
                  ====
            1     \          _ 4
           ----    >    (x - x)  - 3
              4   /       i
           n s    ====
                  i = 1
```


$$
{{1\over{n s^4}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^4}}-3}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) kurtosis (s1), numer;
(%o3)                  - 1.273247946514421

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) kurtosis (s2);
(%o5) [- .2715445622195385, 0.119998784429451, 
   - .4275233490482866, - .6405361979019522, - .4952382132352935]
```


Véanse también `mean`, `var` y `skewness`.

<!-- category: Statistics -->
<!-- keywords: list_correlations -->
<!-- signatures: list_correlations(matrix), list_correlations(matrix, options...) -->
### Function: list_correlations (matrix)

La función `list_correlations` devuelve una lista con medidas de correlación:



- *
*matriz de precisión*: es la inversa de la matriz de covarianzas $S_1$,

```maxima
-1     ij
      S   = (s  )             
       1         i,j = 1,2,...,p
```

$$
{S_{1}^{-1}}={\left(s^{ij}\right)_{i,j=1,2,\ldots, p}}
$$
- *
*multiple correlation vector*:  $(R_1^2, R_2^2, ..., R_p^2)$, with 

```maxima
2          1
      R  = 1 - -------
       i        ii
               s   s
                    ii
```

$$
{R_{i}^{2}}={1-{{1}\over{s^{ii}s_{ii}}}}
$$
es un indicador de la bondad de ajuste del modelo de regresión lineal multivariante de $X_i$ cuando el resto de variables se utilizan como regresores.
- *
*matriz de correlaciones parciales*: en la que el elemento $(i, j)$ es

```maxima
ij
                        s
      r        = - ------------
       ij.rest     / ii  jj\ 1/2
                   |s   s  |
                   \       /
```

$$
{r_{ij.rest}}={-{{s^{ij}}\over \sqrt{s^{ii}s^{jj}}}}
$$


Opción:



- *
`'data`, por defecto `'true`, indica si la matriz de entrada contiene los datos muestrales,
en cuyo caso la matriz de covarianzas `cov1` debe ser calculada; en caso contrario, se le debe
pasar ésta a la función como matriz simétrica en lugar de los datos.


Ejemplo:












```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) z : list_correlations (s2)$

(%i4) fpprintprec : 5$ /* for pretty output */
      [  .38486   - .13856   - .15626   - .10239    .031179  ]
      [                                                      ]
      [ - .13856   .34107    - .15233    .038447   - .052842 ]
      [                                                      ]
(%o5) [ - .15626  - .15233    .47296    - .024816  - .10054  ]
      [                                                      ]
      [ - .10239   .038447   - .024816   .10937    - .034033 ]
      [                                                      ]
      [ .031179   - .052842  - .10054   - .034033   .14834   ]
(%o6)       [.85063, .80634, .86474, .71867, .72675]
       [  - 1.0     .38244   .36627   .49908   - .13049 ]
       [                                                ]
       [  .38244    - 1.0    .37927  - .19907   .23492  ]
       [                                                ]
(%o7)  [  .36627    .37927   - 1.0    .10911    .37956  ]
       [                                                ]
       [  .49908   - .19907  .10911   - 1.0     .26719  ]
       [                                                ]
       [ - .13049   .23492   .37956   .26719    - 1.0   ]
```


Véanse también `cov` y `cov1`.

<!-- category: Statistics -->
<!-- keywords: mean -->
<!-- signatures: mean(list), mean(matrix) -->
### Function: mean (list)

Es la media muestral, definida como


```maxima
n
                     ====
             _   1   \
             x = -    >    x
                 n   /      i
                     ====
                     i = 1
```


$$
{\bar{x}={1\over{n}}{\sum_{i=1}^{n}{x_{i}}}}
$$



Ejemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) mean (s1);
                               471
(%o3)                          ---
                               100


(%i4) %, numer;
(%o4)                         4.71

(%i5) s2 : read_matrix (file_search ("wind.data"))$

(%i6) mean (s2);
(%o6)     [9.9485, 10.1607, 10.8685, 15.7166, 14.8441]
```

<!-- category: Statistics -->
<!-- keywords: mean_deviation -->
<!-- signatures: mean_deviation(list), mean_deviation(matrix) -->
### Function: mean_deviation (list)

Es la desviación media, definida como


```maxima
n
                   ====
               1   \          _
               -    >    |x - x|
               n   /       i
                   ====
                   i = 1
```


$$
{{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-\bar{x}|}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) mean_deviation (s1);
                               51
(%o3)                          --
                               20

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) mean_deviation (s2);
(%o5) [3.287959999999999, 3.075342, 3.23907, 4.715664000000001, 
                                               4.028546000000002]
```


Véase también `mean`.

<!-- category: Statistics -->
<!-- keywords: median -->
<!-- signatures: median(list), median(matrix) -->
### Function: median (list)

Una vez ordenada una muestra, si el tamaño muestral es impar la mediana es el valor central, en caso contrario será la media de los dos valores centrales.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) median (s1);
                                9
(%o3)                           -
                                2

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) median (s2);
(%o5)         [10.06, 9.855, 10.73, 15.48, 14.105]
```


La mediana es el cuantil 1/2.


Véase también `quantile`.

<!-- category: Statistics -->
<!-- keywords: median_deviation -->
<!-- signatures: median_deviation(list), median_deviation(matrix) -->
### Function: median_deviation (list)

Es la desviación mediana, definida como


```maxima
n
               ====
           1   \
           -    >    |x - med|
           n   /       i
               ====
               i = 1
```


$$
{{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-med|}}}
$$


siendo `med` la mediana de *list*.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) median_deviation (s1);
                                5
(%o3)                           -
                                2

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) median_deviation (s2);
(%o5)           [2.75, 2.755, 3.08, 4.315, 3.31]
```


Véase también `mean`.

<!-- category: Statistics -->
<!-- keywords: noncentral_moment -->
<!-- signatures: noncentral_moment(list, k), noncentral_moment(matrix, k) -->
### Function: noncentral_moment (list, k)

Es el momento no central de orden $k$, definido como


```maxima
n
                     ====
                 1   \      k
                 -    >    x
                 n   /      i
                     ====
                     i = 1
```


$$
{{1\over{n}}{\sum_{i=1}^{n}{x_{i}^k}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) noncentral_moment (s1, 1), numer; /* the mean */
(%o3)                         4.71


(%i5) s2 : read_matrix (file_search ("wind.data"))$
(%o5) [319793.8724761506, 320532.1923892463, 391249.5621381556, 
                            2502278.205988911, 1691881.797742255]

(%i6) noncentral_moment (s2, 5);
```


Véase también `central_moment`.

<!-- category: Statistics -->
<!-- keywords: pearson_skewness -->
<!-- signatures: pearson_skewness(list), pearson_skewness(matrix) -->
### Function: pearson_skewness (list)

Es el coeficiente de asimetría de Pearson, definido como


```maxima
_
             3 (x - med)
             -----------
                  s
```


$$
{{3\,\left(\bar{x}-med\right)}\over{s}}
$$


siendo *med* la mediana de *list*.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) pearson_skewness (s1), numer;
(%o3)                   .2159484029093895

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) pearson_skewness (s2);
(%o5) [- .08019976629211892, .2357036272952649, 
         .1050904062491204, .1245042340592368, .4464181795804519]
```


Véanse también `mean`, `var` y `median`.

<!-- category: Statistics -->
<!-- keywords: piechart, piechart_description -->
<!-- signatures: piechart(list), piechart(list, option_1, option_2, ...), piechart(one_column_matrix), piechart(one_column_matrix, option_1, option_2, ...), piechart(one_row_matrix), piechart(one_row_matrix, option_1, option_2, ...), piechart_description(...) -->
### Function: piechart (list)

Similar a `barsplot`, pero dibuja sectores en lugar de rectángulos.


Opciones disponibles:




- *
*sector_colors* (valor por defecto, `[]`): una lista de colores para los
sectores. Cuando el número de sectores sea mayor que el de colores especificados, 
los colores adicionales necesarios se seleccionan aleatoriamente. Véase `color` para más
información.
- *
*pie_center* (valor por defecto, `[0,0]`): centro del diagrama
- *
*pie_radius* (valor por defecto, `1`): radio del diagrama.
- *
Todas las opciones globales de `draw`, excepto `key`, que se asigna
internamente por `piechart`. Si es necesario que el usuario le dé su propio
valor a esta opción, o quiere construir una escena más compleja,
debe hacer uso de `piechart_description`.
- *
Las siguientes opciones locales de `draw`: `key`, `color`, 
`fill_density` y `line_width`. Véase también
`bars`.


La función `piechart_description` crea un objeto gráfico
útil para formar escenas complejas, junto con otros objetos gráficos.
Se dispone también de la función `wxpiechart` para crear
histogramas incorporados en los interfaces wxMaxima y iMaxima.


Ejemplo:












```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) piechart(
        s1,
        xrange  = [-1.1, 1.3],
        yrange  = [-1.1, 1.1],
        title   = "Digit frequencies in pi")$
```


Véase también la función `barsplot`.

<!-- category: Statistics -->
<!-- keywords: principal_components -->
<!-- signatures: principal_components(matrix), principal_components(matrix, options...) -->
### Function: principal_components (matrix)

Calcula las componentes principales de una muestra multivariante. Las componentes
principales se utilizan en el análisis estadístico multivariante
para reducir la dimensionalidad de la muestra.


Opción:



- *
`'data`, por defecto `'true`, indica si la matriz de entrada contiene los datos muestrales,
en cuyo caso la matriz de covarianzas `cov1` debe ser calculada; en caso contrario, se le debe
pasar ésta a la función como matriz simétrica en lugar de los datos.


La salida de la función `principal_components` es una lista con los siguientes resultados:



- *
varianzas de las componentes principales,
- *
porcentajes de variación total explicada por cada componente principal,
- *
matriz de rotación.


Ejemplos:


En este ejemplo, la primera componente explica el 83.13 por ciento de la varianza total.



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec:4 $
(%i4) res: principal_components(s2);
0 errors, 0 warnings
(%o4) [[87.57, 8.753, 5.515, 1.889, 1.613], 
[83.13, 8.31, 5.235, 1.793, 1.531], 

[ .4149  .03379   - .4757  - 0.581   - .5126 ]
[                                            ]
[ 0.369  - .3657  - .4298   .7237    - .1469 ]
[                                            ]
[ .3959  - .2178  - .2181  - .2749    .8201  ]]
[                                            ]
[ .5548   .7744    .1857    .2319    .06498  ]
[                                            ]
[ .4765  - .4669   0.712   - .09605  - .1969 ]

(%i5) /* porcentajes acumulados  */
    block([ap: copy(res[2])],
      for k:2 thru length(ap) do ap[k]: ap[k]+ap[k-1],
      ap);
(%o5)                 [83.13, 91.44, 96.68, 98.47, 100.0]
(%i6) /* dimension de la muestra */
      p: length(first(res));
(%o6)                                  5
(%i7) /* dibuja porcentajes para seleccionar el numero de 
         componentes principales para el analisis ulterior */
     draw2d(
        fill_density = 0.2,
        apply(bars, makelist([k, res[2][k], 1/2], k, p)),
        points_joined = true,
        point_type    = filled_circle,
        point_size    = 3,
        points(makelist([k, res[2][k]], k, p)),
        xlabel = "Variances",
        ylabel = "Percentages",
        xtics  = setify(makelist([concat("PC",k),k], k, p))) $
```


En caso de que la matriz de covarianzas sea conocida, se le puede pasar
a la función, pero debe utilizarse la opción `data=false`.



```maxima
(%i1) load ("descriptive")$
(%i2) S: matrix([1,-2,0],[-2,5,0],[0,0,2]);
                                [  1   - 2  0 ]
                                [             ]
(%o2)                           [ - 2   5   0 ]
                                [             ]
                                [  0    0   2 ]
(%i3) fpprintprec:4 $
(%i4) /* el argumento es una matriz de covarianzas */
      res: principal_components(S, data=false);
0 errors, 0 warnings
                                                  [ - .3827  0.0  .9239 ]
                                                  [                     ]
(%o4) [[5.828, 2.0, .1716], [72.86, 25.0, 2.145], [  .9239   0.0  .3827 ]]
                                                  [                     ]
                                                  [   0.0    1.0   0.0  ]
(%i5) /* transformacion para obtener las componentes principales a
         partir de los registros originales */
      matrix([a1,b2,c3],[a2,b2,c2]).last(res);
             [ .9239 b2 - .3827 a1  1.0 c3  .3827 b2 + .9239 a1 ]
(%o5)        [                                                  ]
             [ .9239 b2 - .3827 a2  1.0 c2  .3827 b2 + .9239 a2 ]
```

<!-- category: Statistics -->
<!-- keywords: qrange -->
<!-- signatures: qrange(list), qrange(matrix) -->
### Function: qrange (list)

El rango intercuartílico es la diferencia entre el tercer y primer cuartil,
`quantile(list,3/4) - quantile(list,1/4)`,










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) qrange (s1);
                               21
(%o3)                          --
                               4

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) qrange (s2);
(%o5) [5.385, 5.572499999999998, 6.0225, 8.729999999999999, 
                                               6.650000000000002]
```


Véase también `quantile`.

<!-- category: Statistics -->
<!-- keywords: quantile -->
<!-- signatures: quantile(list, p), quantile(matrix, p) -->
### Function: quantile (list, p)

Es el *p*-cuantil, siendo *p* un número del intervalo $[0, 1]$, de la muestra *list*.
Aunque existen varias definiciones para el cuantil muestral (Hyndman, R. J., Fan, Y. (1996) *Sample quantiles in statistical packages*. American Statistician, 50, 361-365), la programada en el paquete  `descriptive` es la basada en la interpolación lineal.


Ejemplo:











```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) /* 1st and 3rd quartiles */
         [quantile (s1, 1/4), quantile (s1, 3/4)], numer;
(%o3)                      [2.0, 7.25]

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) quantile (s2, 1/4);
(%o5)    [7.2575, 7.477500000000001, 7.82, 11.28, 11.48]
```

<!-- category: Statistics -->
<!-- keywords: quartile_skewness -->
<!-- signatures: quartile_skewness(list), quartile_skewness(matrix) -->
### Function: quartile_skewness (list)

Es el coeficiente de asimetría cuartílico, definido como


```maxima
c    - 2 c    + c
                3/4      1/2    1/4
               --------------------
                   c    - c
                    3/4    1/4
```


$$
{{c_{{{3}\over{4}}}-2\,c_{{{1}\over{2}}}+c_{{{1}\over{4}}}}\over{c
 _{{{3}\over{4}}}-c_{{{1}\over{4}}}}}
$$


siendo $c_p$ el *p*-cuantil de la muestra *list*.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) quartile_skewness (s1), numer;
(%o3)                  .04761904761904762

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) quartile_skewness (s2);
(%o5) [- 0.0408542246982353, .1467025572005382, 
       0.0336239103362392, .03780068728522298, 0.210526315789474]
```


Véase también `quantile`.

<!-- category: Statistics -->
<!-- keywords: range -->
<!-- signatures: range(list), range(matrix) -->
### Function: range (list)

Es la diferencia entre los valores extremos.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) range (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) range (s2);
(%o5)          [19.67, 20.96, 17.37, 24.38, 22.46]
```

<!-- category: Statistics -->
<!-- keywords: scatterplot, scatterplot_description -->
<!-- signatures: scatterplot(list), scatterplot(list, option_1, option_2, ...), scatterplot(matrix), scatterplot(matrix, option_1, option_2, ...), scatterplot_description(...) -->
### Function: scatterplot (list)

Dibuja diagramas de dispersión, tanto de muestras univariantes (*list*)
como multivariantes (*matrix*). 


Las opciones disponibles son las mismas que admite `histogram`.


La función `scatterplot_description` crea un objeto gráfico
útil para formar escenas complejas, junto con otros objetos gráficos.
Se dispone también de la función `wxscatterplot` para crear
histogramas incorporados en los interfaces wxMaxima y iMaxima.


Ejemplos:


Diagrama de dispersión univariante a partir de una muestra normal
simulada. 












```maxima
(%i1) load ("descriptive")$
(%i2) load ("distrib")$

(%i3) scatterplot(
        random_normal(0,1,200),
        xaxis      = true,
        point_size = 2,
        dimensions = [600,150])$
```


Diagrama de dispersión bidimensional.













```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) scatterplot(
       submatrix(s2, 1,2,3),
       title      = "Data from stations #4 and #5",
       point_type = diamant,
       point_size = 2,
       color      = blue)$
```


Diagrama de dispersión tridimensional.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) scatterplot(submatrix (s2, 1,2), nclasses=4)$
```


Diagrama de dispersión de cinco dimensiones, con histogramas de
cinco classes.














```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) scatterplot(
        s2,
        nclasses     = 5,
        frequency    = relative,
        fill_color   = blue,
        fill_density = 0.3,
        xtics        = 5)$
```


Para dibujar puntos aislados o unidos por segmentos, tanto en dos
como en tres dimensiones, véase `points`.
Véase también `histogram`.

<!-- category: Statistics -->
<!-- keywords: skewness -->
<!-- signatures: skewness(list), skewness(matrix) -->
### Function: skewness (list)

Es el coeficiente de asimetría, definido como


```maxima
n
                  ====
            1     \          _ 3
           ----    >    (x - x)
              3   /       i
           n s    ====
                  i = 1
```


$$
{{1\over{n s^3}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^3}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) skewness (s1), numer;
(%o3)                  .009196180476450306

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) skewness (s2);
(%o5) [.1580509020000979, .2926379232061854, .09242174416107717, 
                            .2059984348148687, .2142520248890832]
```


Véanse también `mean`, `var` y `kurtosis`.

<!-- category: Statistics -->
<!-- keywords: smax -->
<!-- signatures: smax(list), smax(matrix) -->
### Function: smax (list)

Es el valor máximo de la muestra *list*.
Cuando el argumento es una matriz, `smax` devuelve
una lista con los valores máximos de las
columnas, las cuales están asociadas a variables
estadísticas.










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) smax (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) smax (s2);
(%o5)          [20.25, 21.46, 20.04, 29.63, 27.63]
```


Véase también `smin`.

<!-- category: Statistics -->
<!-- keywords: smin -->
<!-- signatures: smin(list), smin(matrix) -->
### Function: smin (list)

Es el valor mínimo de la muestra *list*.
Cuando el argumento es una matriz, `smin` devuelve
una lista con los valores mínimos de las
columnas, las cuales están asociadas a variables
estadísticas.










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) smin (s1);
(%o3)                           0

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) smin (s2);
(%o5)             [0.58, 0.5, 2.67, 5.25, 5.17]
```


Véase también `smax`.

<!-- category: Statistics -->
<!-- keywords: standardize -->
<!-- signatures: standardize(list), standardize(matrix) -->
### Function: standardize (list)

Resta a cada elemento de la lista la media muestral y luego divide el resultado por
la desviación típica. Si la entrada es una matriz, `standardize` 
resta a cada fila la media multivariante y luego divide cada componente por la
desviación típica correspondiente.

<!-- category: Statistics -->
<!-- keywords: starplot, starplot_description -->
<!-- signatures: starplot(data1, data2, ..., option_1, option_2, ...), starplot_description(...) -->
### Function: starplot (data1, data2, ..., option_1, option_2, ...)

Dibuja diagramas de estrellas para variables estadísticas
discretas, tanto para una como para más muestras.


*data* puede ser una lista de resultados provenientes de una muestra
o una matriz de *m* filas y *n* columnas, representando *n* 
muestras de tamaño *m* cada una.


Las opciones disponibles son:



- *
*stars_colors* (valor por defecto, `[]`): una lista de colores para muestras
múltiples. Cuando haya más muestras que colores especificados, los colores que faltan
se eligen aleatoriamente. Véase `color` para más información.
- *
*frequency* (valor por defecto, `absolute`): indica la escala de los radios.
Valores admitidos son:  `absolute` y `relative`.
- *
*ordering* (valor por defecto, `orderlessp`): los valores admitidos para esta 
opción son: `orderlessp` y `ordergreatp`, indicando cómo se deben ordenar
los resultados muestrales sobre el eje-*x*.
- *
*sample_keys* (valor por defecto, `[]`): es una lista de cadenas de 
texto a usar como leyendas. Cuando la lista tenga una longitud diferente de cero o 
del número de muestras, se devolverá un mensaje de error.
- *
*star_center* (valor por defecto, `[0,0]`): centro del diagrama.
- *
*star_radius* (valor por defecto, `1`): radio del diagrama.
- *
Todas las opciones globales de `draw`, excepto `points_joined`, `point_type`, 
and `key`, que se asignan internamente por `starplot`. Si es necesario que el 
usuario les dé sus propios valores a estas opciones, o quiere construir una escena más compleja,
debe hacer uso de `starplot_description`.
- *
La siguiente opción local de `draw`: `line_width`.


La función `starplot_description` crea un objeto gráfico
útil para formar escenas complejas, junto con otros objetos gráficos.
Se dispone también de la función `wxstarplot` para crear
histogramas incorporados en los interfaces wxMaxima y iMaxima.


Ejemplo:


Gráfico basado en frecuencias absolutas. La localización y
el radios lo define el usuario.



```maxima
(%i1) load ("descriptive")$
(%i2) l1: makelist(random(10),k,1,50)$
(%i3) l2: makelist(random(10),k,1,200)$

(%i4) starplot(
        l1, l2,
        stars_colors = [blue,red],
        sample_keys = ["1st sample", "2nd sample"],
        star_center = [1,2],
        star_radius = 4,
        proportional_axes = xy,
        line_width = 2 ) $
```

<!-- category: Statistics -->
<!-- keywords: std -->
<!-- signatures: std(list), std(matrix) -->
### Function: std (list)

Es la desviación típica muestral, raíz cuadrada de `var`.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) std (s1), numer;
(%o3)                   2.902740084816414

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) std (s2);
(%o5) [4.149928523480858, 3.871399812729241, 3.933920277534866, 
                            5.672434260526957, 4.941970881136392]
```


Véanse también `var` y `std1`.

<!-- category: Statistics -->
<!-- keywords: std1 -->
<!-- signatures: std1(list), std1(matrix) -->
### Function: std1 (list)

Es la cuasidesviación típica muestral, raíz cuadrada de `var1`.


Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) std1 (s1), numer;
(%o3)                   2.917363553109228

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) std1 (s2);
(%o5) [4.17083509672109, 3.89090320978032, 3.953738641137555, 
                            5.701010936401517, 4.966867617451963]
```


Véanse también `var1` y `std`.

<!-- category: Statistics -->
<!-- keywords: stemplot -->
<!-- signatures: stemplot(m), stemplot(m, option) -->
### Function: stemplot (m)

Dibuja diagrama de tallos y hojas.


La única opción disponible es:



- *
*leaf_unit* (valor por defecto, `1`): indica la unidad de las hojas; debe ser
una potencia de 10.


Ejemplo:



```maxima
(%i1) load ("descriptive")$
(%i2) load("distrib")$

(%i3) stemplot(
        random_normal(15, 6, 100),
        leaf_unit = 0.1);
-5|4
 0|37
 1|7
 3|6
 4|4
 5|4
 6|57
 7|0149
 8|3
 9|1334588
10|07888
11|01144467789
12|12566889
13|24778
14|047
15|223458
16|4
17|11557
18|000247
19|4467799
20|00
21|1
22|2335
23|01457
24|12356
25|455
27|79
key: 6|3 =  6.3
(%o3)                  done
```

<!-- category: Statistics -->
<!-- keywords: subsample -->
<!-- signatures: subsample(data_matrix, predicate_function), subsample(data_matrix, predicate_function, col_num, col_num, ...) -->
### Function: subsample (data_matrix, predicate_function)

Esta es una variante de la función `submatrix` de Maxima.
El primer argumento es una matriz de datos, el segundo es una 
función de predicado y el resto de argumentos opcionales son
los números de las columnas a tomar en consideración.


Estos son los registros multivariantes en los que la velocidad del viento
en la primera estación meteorológica fue menor de 18 nudos. Véase 
cómo en la expresión lambda la *i*-ésima componente 
se la referencia como `v[i]`.







```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) subsample (s2, lambda([v], v[1] > 18));
              [ 19.38  15.37  15.12  23.09  25.25 ]
              [                                   ]
              [ 18.29  18.66  19.08  26.08  27.63 ]
(%o3)         [                                   ]
              [ 20.25  21.46  19.95  27.71  23.38 ]
              [                                   ]
              [ 18.79  18.96  14.46  26.38  21.84 ]
```


En el siguiente ejemplo, se solicitan únicamente la primera, segunda y
quinta componentes de aquellos registros con velocidades del viento mayores
o iguales que 16 nudos en la estación número 1 y menores que 25 nudos
en la estación número 4. La muestra sólo contiene los datos referidos
a las estaciones 1, 2 y 5. En este caso, la función de predicado se
define por medio de una función de Maxima ordinaria.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) g(x):= x[1] >= 16 and x[4] < 25$

(%i4) subsample (s2, g, 1, 2, 5);
                     [ 19.38  15.37  25.25 ]
                     [                     ]
                     [ 17.33  14.67  19.58 ]
(%o4)                [                     ]
                     [ 16.92  13.21  21.21 ]
                     [                     ]
                     [ 17.25  18.46  23.87 ]
```


He aquí un ejemplo con las variables categóricas de `biomed.data`.
Se piden los registros correspondientes a aquellos pacientes del grupo `B` mayores de 38 anños,








```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) h(u):= u[1] = B and u[2] > 38 $
(%i4) subsample (s3, h);
                [ B  39  28.0  102.3  17.1  146 ]
                [                               ]
                [ B  39  21.0  92.4   10.3  197 ]
                [                               ]
                [ B  39  23.0  111.5  10.0  133 ]
                [                               ]
                [ B  39  26.0  92.6   12.3  196 ]
(%o4)           [                               ]
                [ B  39  25.0  98.7   10.0  174 ]
                [                               ]
                [ B  39  21.0  93.2   5.9   181 ]
                [                               ]
                [ B  39  18.0  95.0   11.3  66  ]
                [                               ]
                [ B  39  39.0  88.5   7.6   168 ]
```


Es probable que el análisis estadístico
requiera únicamente de las medidas sanguíneas.








```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) subsample (s3, lambda([v], v[1] = B and v[2] > 38),
           3, 4, 5, 6);
                   [ 28.0  102.3  17.1  146 ]
                   [                        ]
                   [ 21.0  92.4   10.3  197 ]
                   [                        ]
                   [ 23.0  111.5  10.0  133 ]
                   [                        ]
                   [ 26.0  92.6   12.3  196 ]
(%o3)              [                        ]
                   [ 25.0  98.7   10.0  174 ]
                   [                        ]
                   [ 21.0  93.2   5.9   181 ]
                   [                        ]
                   [ 18.0  95.0   11.3  66  ]
                   [                        ]
                   [ 39.0  88.5   7.6   168 ]
```


Esta es la media multivariante de `s3`.







```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$

(%i3) mean (s3);
       65 B + 35 A  317          6 NA + 8145.0
(%o3) [-----------, ---, 87.178, -------------, 18.123, 
           100      10                100
                                                    3 NA + 19587
                                                    ------------]
                                                        100
```


Aquí la primera componente carece de significado, ya que tanto `A` como `B` son categóricas, la segunda componente es la edad media de los individuos en forma racional, al tiempo que los valores cuarto y quinto muestran cierto comportamiento extraño; lo cual se debe a que el símbolo `NA` se utiliza para indicar datos *no disponibles*, por lo que ambas medias no tienen sentido. Una posible solución puede ser extraer de la matriz aquellas filas con símbolos `NA`, lo que acarrearía cierta pérdida de información.








```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) g(v):= v[4] # NA and v[6] # NA $

(%i4) mean (subsample (s3, g, 3, 4, 5, 6));
(%o4) [79.4923076923077, 86.2032967032967, 16.93186813186813, 
                                                            2514
                                                            ----]
                                                             13
```

<!-- category: Statistics -->
<!-- keywords: transform_sample -->
<!-- signatures: transform_sample(matriz, varlist, exprlist) -->
### Function: transform_sample (matriz, varlist, exprlist)

Transforma la *matriz* de datos, en la que a cada columna se le asigna
un nombre de acuerdo con la lista *varlist*, según las expresiones de *exprlist*.


Ejemplos:


El segundo argumento asigna nombres a las tres columnas, con ellos la lista de expresiones
define la transformación de la muestra.



```maxima
(%i1) load ("descriptive")$
(%i2) data: matrix([3,2,7],[3,7,2],[8,2,4],[5,2,4]) $

(%i3) transform_sample(data, [a,b,c], [c, a*b, log(a)]);
                               [ 7  6   log(3) ]
                               [               ]
                               [ 2  21  log(3) ]
(%o3)                          [               ]
                               [ 4  16  log(8) ]
                               [               ]
                               [ 4  10  log(5) ]
```


Añade una columna constante y elimina la tercera variable.



```maxima
(%i1) load ("descriptive")$
(%i2) data: matrix([3,2,7],[3,7,2],[8,2,4],[5,2,4]) $
(%i3) transform_sample(data, [a,b,c], [makelist(1,k,length(data)),a,b]);

                                  [ 1  3  2 ]
                                  [         ]
                                  [ 1  3  7 ]
(%o3)                             [         ]
                                  [ 1  8  2 ]
                                  [         ]
                                  [ 1  5  2 ]
```

<!-- category: Statistics -->
<!-- keywords: var -->
<!-- signatures: var(list), var(matrix) -->
### Function: var (list)

Es la varianza muestral, definida como


```maxima
n
                   ====
           2   1   \          _ 2
          s  = -    >    (x - x)
               n   /       i
                   ====
                   i = 1
```


$$
{{1}\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}
$$



Ejemplo:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var (s1), numer;
(%o3)                   8.425899999999999
```


Véase también `var1`.

<!-- category: Statistics -->
<!-- keywords: var1 -->
<!-- signatures: var1(list), var1(matrix) -->
### Function: var1 (list)

Es la cuasivarianza muestral, definida como


```maxima
n
                   ====
               1   \          _ 2
              ---   >    (x - x)
              n-1  /       i
                   ====
                   i = 1
```


$$
{{1\over{n-1}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}}
$$



Ejemplo:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var1 (s1), numer;
(%o3)                    8.5110101010101

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) var1 (s2);
(%o5) [17.39586540404041, 15.13912778787879, 15.63204924242424, 
                            32.50152569696971, 24.66977392929294]
```


Véase también `var`.

