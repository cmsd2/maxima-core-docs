## Plotting

### Variable: adapt_depth

Default value: `5`


The maximum number of splittings used by the adaptive plotting routine
of `plot2d`; *integer* must be a non-negative integer. A value
of zero means that adaptive plotting will not be used and the resulting
plot will have 1+4**nticks* points (see option `nticks`). To
have more control on the number of points and their positions, a list of
points can be created and then plotted using the `discrete` method
of `plot2d`.

See also: `plot2d`, `nticks`.

### Function: add_edge (e, gr)

Adds the edge *e* to the graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) p : path_graph(4)$
(%i3) neighbors(0, p);
(%o3)                          [1]
(%i4) add_edge([0,3], p);
(%o4)                         done
(%i5) neighbors(0, p);
(%o5)                        [3, 1]
```

### Function: add_edges (e_list, gr)

Adds all edges in the list *e_list* to the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : empty_graph(3)$
(%i3) add_edges([[0,1],[1,2]], g)$
(%i4) print_graph(g)$
Graph on 3 vertices with 2 edges.
Adjacencies:
  2 :  1
  1 :  2  0
  0 :  1
```

### Function: add_vertex (v, gr)

Adds the vertex *v* to the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : path_graph(2)$
(%i3) add_vertex(2, g)$
(%i4) print_graph(g)$
Graph on 3 vertices with 1 edges.
Adjacencies:
  2 :
  1 :  0
  0 :  1
```

### Function: add_vertices (v_list, gr)

Adds all vertices in the list *v_list* to the graph *gr*.
A vertex may be any integer,
and *v_list* may contain vertices in any order.

### Function: adjacency_matrix (gr)

Returns the adjacency matrix of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(4)$
(%i3) adjacency_matrix(c5);
                         [ 0  1  0  1 ]
                         [            ]
                         [ 1  0  1  0 ]
(%o3)                    [            ]
                         [ 0  1  0  1 ]
                         [            ]
                         [ 1  0  1  0 ]
```

### Variable: allocation

Default value: `false`


With option `allocation` it is possible to place a scene in the
output window at will; this is of interest in multiplots. When `false`,
the scene is placed automatically, depending on the value assigned to option
`columns`. In any other case, `allocation` must be set to a list of
two pairs of numbers; the first corresponds to the position of the lower left
corner of the scene, and the second pair gives the width and height of the plot.
All quantities must be given in relative coordinates, between 0 and 1.


Examples:


In site graphics.



```maxima
(%i1) draw(
        gr2d(
          explicit(x^2,x,-1,1)),
        gr2d(
          allocation = [[1/4, 1/4],[1/2, 1/2]],
          explicit(x^3,x,-1,1),
          grid = true) ) $
```

(Figure draw_allocation)


Multiplot with selected dimensions.



```maxima
(%i1) draw(
        terminal = wxt,
        gr2d(
          grid=[5,5],
          allocation = [[0, 0],[1, 1/4]],
          explicit(x^2,x,-1,1)),
        gr3d(
          allocation = [[0, 1/4],[1, 3/4]],
          explicit(x^2+y^2,x,-1,1,y,-1,1) ))$
```

(Figure draw_allocation2)


See also option `columns`.

See also: `columns`.

### Function: average_degree (gr)

Returns the average degree of vertices in the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) average_degree(grotzch_graph());
                               40
(%o2)                          --
                               11
```

### Variable: axes

Default value: `true`


Where *symbol* can be either `true`, `false`, `x`,
`y` or `solid`. If `false`, no axes are shown; if equal
to `x` or `y` only the x or y axis will be shown; if it is
equal to `true`, both axes will be shown and `solid` will show
the two axes with a solid line, rather than the default broken
line. This option does not have any effect in the 3 dimensional plots.
The single keywords `axes` and `noaxes` can be used as
synonyms for `[axes, true]` and `[axes, false]`.

### Variable: axis_3d

Default value: `true`


If `axis_3d` is `true`, the *x*, *y* and *z* axis are shown in 3d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(axis_3d = false,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```

(Figure draw_axis3d)


See also `axis_bottom`,  `axis_left`, `axis_top`, and `axis_right` for axis in 2d.

See also: `axis_bottom`, `axis_left`, `axis_top`, `axis_right`.

### Variable: axis_bottom

Default value: `true`


If `axis_bottom` is `true`, the bottom axis is shown in 2d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(axis_bottom = false,
             explicit(x^3,x,-1,1))$
```

(Figure draw_axis_bottom)


See also `axis_left`,  `axis_top`, `axis_right` and `axis_005f3d`.

See also: `axis_left`, `axis_top`, `axis_right`, `axis_3d`.

### Variable: axis_left

Default value: `true`


If `axis_left` is `true`, the left axis is shown in 2d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(axis_left = false,
             explicit(x^3,x,-1,1))$
```


See also `axis_bottom`,  `axis_top`, `axis_right` and `axis_005f3d`.

See also: `axis_bottom`, `axis_top`, `axis_right`, `axis_3d`.

### Variable: axis_right

Default value: `true`


If `axis_right` is `true`, the right axis is shown in 2d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(axis_right = false,
             explicit(x^3,x,-1,1))$
```


See also `axis_bottom`,  `axis_left`, `axis_top` and `axis_005f3d`.

See also: `axis_bottom`, `axis_left`, `axis_top`, `axis_3d`.

### Variable: axis_top

Default value: `true`


If `axis_top` is `true`, the top axis is shown in 2d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(axis_top = false,
             explicit(x^3,x,-1,1))$
```


See also `axis_bottom`,   `axis_left`,  `axis_right`,  and `axis_005f3d`.

See also: `axis_bottom`, `axis_left`, `axis_right`, `axis_3d`.

### Variable: azimuth

Default value: `30`


A plot3d plot can be thought of as starting with the x and y axis in the
horizontal and vertical axis, as in plot2d, and the z axis coming out of
the screen.  The z axis is then rotated around the x axis through an
angle equal to `elevation` and then the new xy plane is rotated
around the new z axis through an angle `azimuth`. This option sets
the value for the azimuth, in degrees.


See also `elevation`.

See also: `elevation`, `azimuth`.

### Variable: background_color

Default value: `white`


Sets the background color for terminals. Default background color is white.


Since this is a global graphics option, its position in the scene description
does not matter.


This option does not work with terminals `epslatex` and `epslatex_standalone`.


See also `color`

### Function: bars (x1, h1, w1, x2, h2, w2, ...)

Draws vertical bars in 2D.


**2D**


`bars ([x1,h1,w1], [x2,h2,w2, ...])` 
draws bars centered at values *x1*, *x2*, ... with heights *h1*, *h2*, ...
and widths *w1*, *w2*, ...


This object is affected by the following *graphic options*: `key`, 
`fill_color`, `fill_density` and `line_005fwidth`.


Example:



```maxima
(%i1) draw2d(
       key          = "Group A",
       fill_color   = blue,
       fill_density = 0.2,
       bars([0.8,5,0.4],[1.8,7,0.4],[2.8,-4,0.4]),
       key          = "Group B",
       fill_color   = red,
       fill_density = 0.6,
       line_width   = 4,
       bars([1.2,4,0.4],[2.2,-2,0.4],[3.2,5,0.4]),
       xaxis = true);
```

(Figure draw_bars)

See also: `key`, `fill_color`, `fill_density`, `line_width`.

### Function: barsplot (data1, data2, ..., option_1, option_2, ...)

Plots bars diagrams for discrete statistical variables,
both for one or multiple samples.


*data* can be a list of outcomes representing one sample, or a 
matrix of *m* rows and *n* columns, representing *n* samples of size 
*m* each.


Available options are:



- *
*box_width* (default, `3/4`): relative width of rectangles. This 
value must be in the range `[0,1]`.
- *
*grouping* (default, `clustered`): indicates how multiple samples are
shown. Valid values are: `clustered` and `stacked`.
- *
*groups_gap* (default, `1`): a positive integer number representing 
the gap between two consecutive groups of bars.
- *
*bars_colors* (default, `[]`): a list of colors for multiple samples.
When there are more samples than specified colors, the extra necessary colors 
are chosen at random. See `color` to learn more about them.
- *
*frequency* (default, `absolute`): indicates the scale of the
ordinates. Possible values are:  `absolute`, `relative`, 
and `percent`.
- *
*ordering* (default, `orderlessp`): possible values are `orderlessp` or `ordergreatp`,
indicating how statistical outcomes should be ordered on the *x*-axis.
- *
*sample_keys* (default, `[]`): a list with the strings to be used in the legend.
When the list length is other than 0 or the number of samples, an error message is returned.
- *
*start_at* (default, `0`): indicates where the plot begins to be plotted on the
x axis.
- *
All global `draw` options, except `xtics`, which is 
internally assigned by `barsplot`.
If you want to set your own values for this option or want to build
complex scenes, make use of `barsplot_description`. See example below.
- *
The following local `Package-draw` options: `key`, `color_draw`,
`fill_color`, `fill_density` and `line_005fwidth`.
See also
`barsplot`.


There is also a function `wxbarsplot` for creating embedded
histograms in interfaces wxMaxima and iMaxima.  `barsplot` in a
multiplot context.


Examples:


Univariate sample in matrix form. Absolute frequencies.













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


Two samples of different sizes, with
relative frequencies and user declared colors.















```maxima
(%i1) load ("descriptive")$
(%i2) l1:makelist(random(10),k,1,50)$
(%i3) l2:makelist(random(10),k,1,100)$

(%i4) barsplot(
   l1,l2,
   box_width = 1,
   fill_density = 1,
   bars_colors = [black, grey],
   frequency = relative,
   sample_keys = ["A", "B"])$
```


Four non numeric samples of equal size.
















```maxima
(%i1) load ("descriptive")$

(%i2) barsplot(
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  title      = "Asking for something to four groups",
  ylabel     = "# of individuals",
  groups_gap = 3,
  fill_density = 0.5,
  ordering = ordergreatp)$
```


Stacked bars.
















```maxima
(%i1) load ("descriptive")$

(%i2) barsplot(
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  makelist([Yes, No, Maybe][random(3)+1],k,1,50),
  title      = "Asking for something to four groups",
  ylabel     = "# of individuals",
  grouping   = stacked,
  fill_density = 0.5,
  ordering = ordergreatp)$
```


For bars diagrams related options, see `barsplot` of package `Package-draw`
See also functions `histogram` and `piechart`.

See also: `Package-draw`, `key`, `color_draw`, `fill_color`, `fill_density`, `line_width`, `barsplot`, `histogram`, `piechart`.

### Function: barsplot_description (...)

Function `barsplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.


Example: `barsplot` in a multiplot context.



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

### Function: base64 (arg)

Returns the base64-representation of *arg* as a string. 
The argument *arg* may be a string, a non-negative integer or a list of octets.


Examples:



```maxima
(%i1) base64: base64("foo bar baz");
(%o1)                          Zm9vIGJhciBiYXo=
(%i2) string: base64_decode(base64);
(%o2)                            foo bar baz
(%i3) obase: 16.$
(%i4) integer: base64_decode(base64, 'number);
(%o4)                       666f6f206261722062617a
(%i5) octets: base64_decode(base64, 'list);
(%o5)            [66, 6F, 6F, 20, 62, 61, 72, 20, 62, 61, 7A]
(%i6) ibase: 16.$
(%i7) base64(octets);
(%o7)                          Zm9vIGJhciBiYXo=
```


Note that if *arg* contains umlauts (resp. octets larger than 127) 
the resulting base64-string is platform dependent.
However the decoded string will be equal to the original.

### Function: base64_decode (base64_decode, base64-string, base64_decode, base64-string, return-type)

By default `base64_decode` decodes the *base64-string* back to the original string. 


The optional argument *return-type* allows `base64_decode` to 
alternatively return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Example: See `base64`.

See also: `base64`.

### Function: biconnected_components (gr)

Returns the (vertex sets of) 2-connected components of the graph
*gr*.


Example:












```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph(
            [1,2,3,4,5,6,7],
            [
             [1,2],[2,3],[2,4],[3,4],
             [4,5],[5,6],[4,6],[6,7]
            ])$
(%i3) biconnected_components(g);
(%o3)        [[6, 7], [4, 5, 6], [1, 2], [2, 3, 4]]
```


(Figure graphs13, Graph with 2-connected vertices)

### Function: bipartition (gr)

Returns a bipartition of the vertices of the graph *gr* or an empty
list if *gr* is not bipartite.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) h : heawood_graph()$
(%i3) [A,B]:bipartition(h);
(%o3)  [[8, 12, 6, 10, 0, 2, 4], [13, 5, 11, 7, 9, 1, 3]]
(%i4) draw_graph(h, show_vertices=A, program=circular)$
```


(Figure graphs02, Bipartition of the vertices in a Heawood graph)

### Variable: border

Default value: `true`


If `border` is `true`, borders of polygons are painted
according to `line_type` and `line_width`.


This option affects the following graphic objects:


- *
`gr2d`: `polygon`, `rectangle` and `ellipse`.


Example:



```maxima
(%i1) draw2d(color       = brown,
             line_width  = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

(Figure draw_border)

See also: `polygon`, `rectangle`, `ellipse`.

### Variable: boundaries_array

Default value: `false`


`boundaries_array` is where the graphic object `geomap` looks
for boundaries coordinates.


Each component of `boundaries_array` is an array of floating
point quantities, the coordinates of a polygonal segment or map boundary.


See also `geomap`.

See also: `geomap`.

### Function: boxplot (data, boxplot, data, option_1, option_2, ...)

This function plots box-and-whisker diagrams. Argument *data* can be a list,
which is not of great interest, since these diagrams are mainly used for
comparing different samples, or a matrix, so it is possible to compare
two or more components of a multivariate statistical variable. 
But it is also allowed *data* to be a list of samples with 
possible different sample sizes, in fact this is the only function 
in package `descriptive` that admits this type of data structure.


The box is plotted from the first quartile to the third, with an horizontal
segment situated at the second quartile or median. By default, lower and 
upper whiskers are plotted at the minimum and maximum values,
respectively. Option *range* can be used to indicate that values greater
than `quantile(x,3/4)+range*(quantile(x,3/4)-quantile(x,1/4))` or 
less than `quantile(x,1/4)-range*(quantile(x,3/4)-quantile(x,1/4))`
must be considered as outliers, in which case they are plotted as
isolated points, and the whiskers are located at the extremes of the rest of
the sample.


Available options are:



- *
*box_width* (default, `3/4`): relative width of boxes.
This  value must be in the range `[0,1]`.
- *
*box_orientation* (default, `vertical`): possible values: `vertical`
and `horizontal`.
- *
*range* (default, `inf`): positive coefficient of the interquartilic range
to set outliers boundaries.
- *
*outliers_size* (default, `1`): circle size for isolated outliers.
- *
All `draw` options, except `points_joined`, `point_size`, `point_type`,
`xtics`, `ytics`, `xrange`, and `yrange`, which are
internally assigned by `boxplot`.
If you want to set your own values for this options or want to build
complex scenes, make use of `boxplot_description`.
- *
The following local `draw` options: `key`, `color`, 
and `line_width`.


There is also a function `wxboxplot` for creating embedded
histograms in interfaces wxMaxima and iMaxima.


Examples:


Box-and-whisker diagram from a multivariate sample.













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


Box-and-whisker diagram from three samples of different sizes.











```maxima
(%i1) load ("descriptive")$

(%i2) A :
 [[6, 4, 6, 2, 4, 8, 6, 4, 6, 4, 3, 2],
  [8, 10, 7, 9, 12, 8, 10],
  [16, 13, 17, 12, 11, 18, 13, 18, 14, 12]]$

(%i3) boxplot (A, box_orientation = horizontal)$
```


Option *range* can be used to handle outliers.




















```maxima
(%i1)  load ("descriptive")$
 B: [[7, 15, 5, 8, 6, 5, 7, 3, 1],
     [10, 8, 12, 8, 11, 9, 20],
     [23, 17, 19, 7, 22, 19]] $
 boxplot (B, range=1)$
 boxplot (B, range=1.5, box_orientation = horizontal)$
 draw2d(
    boxplot_description(
       B,
       range            = 1.5,
       line_width       = 3,
       outliers_size    = 2,
       color            = red,
       background_color = light_gray),
    xtics = {["Low",1],["Medium",2],["High",3]}) $
```

### Function: boxplot_description (...)

Function `boxplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

### Variable: capping

Default value: `[false, false]`


A list with two possible elements, `true` and `false`,
indicating whether the extremes of a graphic object `tube` remain closed
or open. By default, both extremes are left open.


Setting `capping = false` is equivalent to `capping = [false, false]`,
and `capping = true` is equivalent to `capping = [true, true]`.


Example:



```maxima
(%i1) draw3d(
        capping = [false, true],
        tube(0, 0, a, 1,
             a, 0, 8) )$
```

(Figure draw_tube_extremes)

### Variable: cbrange

Default value: `auto`


If `cbrange` is `auto`, the range for the values which are
colored when `enhanced3d` is not `false` is computed
automatically. Values outside of the color range use color of the
nearest extreme.


When `enhanced3d` or `colorbox` is `false`, option `cbrange` has
no effect.


If the user wants a specific interval for the colored values, it must
be given as a Maxima list, as in `cbrange=[-2, 3]`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d (
        enhanced3d     = true,
        color          = green,
        cbrange = [-3,10],
        explicit(x^2+y^2, x,-2,2,y,-2,2)) $
```

(Figure draw_cbrange)


See also `enhanced3d`,  `colorbox` and `cbtics`.

See also: `enhanced3d`, `colorbox`, `cbtics`.

### Variable: cbtics

Default value: `auto`


This graphic option controls the way tic marks are drawn on the colorbox
when option `enhanced3d` is not `false`.


When `enhanced3d` or `colorbox` is `false`, option `cbtics` has
no effect.


See `xtics` for a complete description.


Example :



```maxima
(%i1) draw3d (
        enhanced3d = true,
        color      = green,
        cbtics  = {["High",10],["Medium",05],["Low",0]},
        cbrange = [0, 10],
        explicit(x^2+y^2, x,-2,2,y,-2,2)) $
```

(Figure draw_cbtics)


See also `enhanced3d`,  `colorbox` and `cbrange`.

See also: `enhanced3d`, `colorbox`, `cbrange`.

### Function: chaosgame (x1, y1, ..., xm, ym, x0, y0, b, n, options, ..., ;)

Implements the so-called chaos game: the initial point (*x0*,
*y0*) is plotted and then one of the *m* points
[*x1*, *y1*]...*xm*, *ym*]
will be selected at random. The next point plotted will be on the
segment from the previous point plotted to the point chosen randomly, at a
distance from the random point which will be *b* times that segment’s
length. The procedure is repeated *n* times. The options are the
same as for `plot2d`.


**Example**. A plot of Sierpinsky’s triangle:



```maxima
(%i1) chaosgame([[0, 0], [1, 0], [0.5, sqrt(3)/2]], [0.1, 0.1], 1/2,
                 30000, [style, dots]);
```


(Figure dynamics7)

See also: `plot2d`.

### Function: chromatic_index (gr)

Returns the chromatic index of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) chromatic_index(p);
(%o3)                           4
```

### Function: chromatic_number (gr)

Returns the chromatic number of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) chromatic_number(cycle_graph(5));
(%o2)                           3
(%i3) chromatic_number(cycle_graph(6));
(%o3)                           2
```

### Function: circulant_graph (n, d)

Returns the circulant graph with parameters *n* and *d*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : circulant_graph(10, [1,3])$
(%i3) print_graph(g)$
Graph on 10 vertices with 20 edges.
Adjacencies:
  9 :  2  6  0  8
  8 :  1  5  9  7
  7 :  0  4  8  6
  6 :  9  3  7  5
  5 :  8  2  6  4
  4 :  7  1  5  3
  3 :  6  0  4  2
  2 :  9  5  3  1
  1 :  8  4  2  0
  0 :  7  3  9  1
```

### Function: clear_edge_weight (e, gr)

Removes the weight of the edge  *e* in the graph *gr*.


Example:










```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph(3, [[[0,1], 1.5], [[1,2], 1.3]])$
(%i3) get_edge_weight([0,1], g);
(%o3)                          1.5
(%i4) clear_edge_weight([0,1], g)$
(%i5) get_edge_weight([0,1], g);
(%o5)                           1
```

### Function: clear_vertex_label (v, gr)

Removes the label of the vertex *v* in the graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[0,"Zero"], [1, "One"]], [[0,1]])$
(%i3) get_vertex_label(0, g);
(%o3)                         Zero
(%i4) clear_vertex_label(0, g);
(%o4)                         done
(%i5) get_vertex_label(0, g);
(%o5)                         false
```

### Function: clebsch_graph ()

Returns the Clebsch graph.

### Variable: color

In 2d plots it defines the color (or colors) for the various curves.  In
`plot3d`, it defines the colors used for the mesh lines of the
surfaces, when no palette is being used.


If there are more curves or surfaces than colors, the colors will be
repeated in sequence. The valid colors are `red`, `green`,
`blue`, `magenta`, `cyan`, `yellow`, `orange`,
`violet`, `brown`, `gray`, `black`, `white`, or
a string starting with the character # and followed by six hexadecimal
digits: two for the red component, two for green component and two for
the blue component. If the name of a given color is unknown color, black
will be used instead.

See also: `plot3d`.

### Variable: color_bar

Default value: `false` in plot3d, `true` in mandelbrot and julia


Where *symbol* can be either `true` or `false`.  If
`true`, whenever `plot3d`, `mandelbrot` or
`julia` use a palette to represent different values, a box will be
shown on the right, showing the corresponding between colors and values.
The single keywords `color_bar` and `nocolor_bar` can be used
as synonyms for `[color_bar, true]` and `[color_bar, false]`.

See also: `plot3d`, `mandelbrot`, `julia`.

### Variable: color_bar_tics

Defines the values at which a mark and a number will be placed in the
color bar. The first number is the initial value, the second the
increments and the third is the last value where a mark is placed. The
second and third numbers can be omitted. When only one number is given,
it will be used as the increment from an initial value that will be
chosen automatically. The single keyword `color_bar_tics` removes a
value given previously, making the graphic program use its default for
the values of the tics and `nocolor_bar_tics` will not show any
tics on the color bar.

### Variable: colorbox

Default value: `true`


If `colorbox` is `true`, a color scale without label is drawn together with 
`image` 2D objects, or coloured 3d objects. If `colorbox` is `false`, no 
color scale is shown. If `colorbox` is a string, a color scale with label is drawn.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:


Color scale and images.



```maxima
(%i1) im: apply('matrix,
                 makelist(makelist(random(200),i,1,30),i,1,30))$
(%i2) draw(
          gr2d(image(im,0,0,30,30)),
          gr2d(colorbox = false, image(im,0,0,30,30))
      )$
```

(Figure draw_colorbox)
Color scale and 3D coloured object.



```maxima
(%i1) draw3d(
        colorbox   = "Magnitude",
        enhanced3d = true,
        explicit(x^2+y^2,x,-1,1,y,-1,1))$
```

(Figure draw_colorbox2)


See also `palette_005fdraw`.

See also: `palette_draw`.

### Variable: columns

Default value: 1


`columns` is the number of columns in multiple plots.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


Example:



```maxima
(%i1) scene1: gr2d(title="Ellipse",
                   nticks=30,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i2) scene2: gr2d(title="Triangle",
                   polygon([4,5,7],[6,4,2]))$
(%i3) draw(scene1, scene2, columns = 2)$
```

(Figure draw_columns)

### Function: complement_graph (g)

Returns the complement of the graph *g*.

### Function: complete_bipartite_graph (n, m)

Returns the complete bipartite graph on *n+m* vertices.

### Function: complete_graph (n)

Returns the complete graph on *n* vertices.

### Function: connect_vertices (v_list, u_list, gr)

Connects all vertices from the list *v_list* with the vertices in
the list *u_list* in the graph *gr*.


*v_list* and *u_list* can be single vertices or lists of
vertices.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : empty_graph(4)$
(%i3) connect_vertices(0, [1,2,3], g)$
(%i4) print_graph(g)$
Graph on 4 vertices with 3 edges.
Adjacencies:
  3 :  0
  2 :  0
  1 :  0
  0 :  3  2  1
```

### Function: connected_components (gr)

Returns the (vertex sets of) connected components of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g: graph_union(cycle_graph(5), path_graph(4))$
(%i3) connected_components(g);
(%o3)            [[1, 2, 3, 4, 0], [8, 7, 6, 5]]
```

### Variable: contour

Default value: `none`


Option `contour` enables the user to select where to plot contour lines.
Possible values are:



- *
`none`:
no contour lines are plotted.
- *
`base`:
contour lines are projected on the xy plane.
- *
`surface`:
contour lines are plotted on the surface.
- *
`both`:
two contour lines are plotted: on the xy plane and on the surface.
- *
`map`:
contour lines are projected on the xy plane, and the view point is
set just in the vertical.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 15,
             contour        = both,
             surface_hide   = true) $
```

(Figure draw_contour)



```maxima
(%i1) draw3d(explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 15,
             contour        = map
      ) $
```

(Figure draw_contour2)

### Variable: contour_levels

Default value: 5


This graphic option controls the way contours are drawn. 
`contour_levels` can be set to a positive integer number, a list of three
numbers or an arbitrary set of numbers:



- *
When option `contour_levels` is bounded to positive integer *n*,
*n* contour lines will be drawn at equal intervals. By default, five
equally spaced contours are plotted.
- *
When option `contour_levels` is bounded to a list of length three of the
form `[lowest,s,highest]`, contour lines are plotted from `lowest` 
to `highest` in steps of `s`.
- *
When option `contour_levels` is bounded to a set of numbers of the
form `{n1, n2, ...}`, contour lines are plotted at values `n1`,
`n2`, ...


Since this is a global graphics option, its position in the scene description
does not matter.


Examples:


Ten equally spaced contour lines. The actual number of
levels can be adjusted to give simple labels.


```maxima
(%i1) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 10,
             contour        = both,
             surface_hide   = true) $
```



From -8 to 8 in steps of 4.


```maxima
(%i1) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = [-8,4,8],
             contour        = both,
             surface_hide   = true) $
```


Isolines at levels -7, -6, 0.8 and 5.


```maxima
(%i1) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = {-7, -6, 0.8, 5},
             contour        = both,
             surface_hide   = true) $
```


See also `contour`.

See also: `contour`.

### Function: contract_edge (e, gr)

Contracts the edge *e* in the graph *gr*.


Example:










```maxima
(%i1) load ("graphs")$
(%i2) g: create_graph(
      8, [[0,3],[1,3],[2,3],[3,4],[4,5],[4,6],[4,7]])$
(%i3) print_graph(g)$
Graph on 8 vertices with 7 edges.
Adjacencies:
  7 :  4
  6 :  4
  5 :  4
  4 :  7  6  5  3
  3 :  4  2  1  0
  2 :  3
  1 :  3
  0 :  3
(%i4) contract_edge([3,4], g)$
(%i5) print_graph(g)$
Graph on 7 vertices with 6 edges.
Adjacencies:
  7 :  3
  6 :  3
  5 :  3
  3 :  5  6  7  2  1  0
  2 :  3
  1 :  3
  0 :  3
```

### Function: copy_graph (g)

Returns a copy of the graph *g*.

### Function: crc24sum (crc24sum, octets, crc24sum, octets, return-type)

By default `crc24sum` returns the `CRC24` checksum of an octet-list 
as a string.


The optional argument *return-type* allows `crc24sum` to 
alternatively return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Example:



```maxima
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2.0.22 (GNU/Linux)

iQEcBAEBAgAGBQJVdCTzAAoJEG/1Mgf2DWAqCSYH/AhVFwhu1D89C3/QFcgVvZTM
wnOYzBUURJAL/cT+IngkLEpp3hEbREcugWp+Tm6aw3R4CdJ7G3FLxExBH/5KnDHi
rBQu+I7+3ySK2hpryQ6Wx5J9uZSa4YmfsNteR8up0zGkaulJeWkS4pjiRM+auWVe
vajlKZCIK52P080DG7Q2dpshh4fgTeNwqCuCiBhQ73t8g1IaLdhDN6EzJVjGIzam
/spqT/sTo6sw8yDOJjvU+Qvn6/mSMjC/YxjhRMaQt9EMrR1AZ4ukBF5uG1S7mXOH
WdiwkSPZ3gnIBhM9SuC076gLWZUNs6NqTeE3UzMjDAFhH3jYk1T7mysCvdtIkms=
=WmeC
-----END PGP SIGNATURE-----
```



```maxima
(%i1) ibase : obase : 16.$
(%i2) sig64 : sconcat(
 "iQEcBAEBAgAGBQJVdCTzAAoJEG/1Mgf2DWAqCSYH/AhVFwhu1D89C3/QFcgVvZTM",
 "wnOYzBUURJAL/cT+IngkLEpp3hEbREcugWp+Tm6aw3R4CdJ7G3FLxExBH/5KnDHi",
 "rBQu+I7+3ySK2hpryQ6Wx5J9uZSa4YmfsNteR8up0zGkaulJeWkS4pjiRM+auWVe",
 "vajlKZCIK52P080DG7Q2dpshh4fgTeNwqCuCiBhQ73t8g1IaLdhDN6EzJVjGIzam",
 "/spqT/sTo6sw8yDOJjvU+Qvn6/mSMjC/YxjhRMaQt9EMrR1AZ4ukBF5uG1S7mXOH",
 "WdiwkSPZ3gnIBhM9SuC076gLWZUNs6NqTeE3UzMjDAFhH3jYk1T7mysCvdtIkms=" )$
(%i3) octets: base64_decode(sig64, 'list)$
(%i4) crc24: crc24sum(octets, 'list);
(%o4)                          [5A, 67, 82]
(%i5) base64(crc24);
(%o5)                              WmeC
```

### Function: create_graph (create_graph, v_list, e_list, create_graph, n, e_list, create_graph, v_list, e_list, directed)

Creates a new graph on the set of vertices *v_list* and with edges *e_list*.


*v_list* is a list of vertices `[v1, v2, ..., vn]` or a
list of vertices together with vertex labels `[[v1, l1], [v2 ,l2], ..., [vn, ln]]`.
A vertex may be any integer,
and *v_list* may contain vertices in any order.
A label may be any Maxima expression,
and two or more vertices may have the same label.


*n* is the number of vertices. Vertices will be identified by integers from 0 to n-1.


*e_list* is a list of edges `[e1, e2,..., em]` or a list of
edges together with edge-weights `[[e1, w1], ..., [em, wm]]`.


If *directed* is not `false`, a directed graph will be returned.


Example 1: create a cycle on 3 vertices:







```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1,2,3], [[1,2], [2,3], [1,3]])$
(%i3) print_graph(g)$
Graph on 3 vertices with 3 edges.
Adjacencies:
  3 :  1  2
  2 :  3  1
  1 :  3  2
```


Example 2: create a cycle on 3 vertices with edge weights:








```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1,2,3], [[[1,2], 1.0], [[2,3], 2.0],
                          [[1,3], 3.0]])$
(%i3) print_graph(g)$
Graph on 3 vertices with 3 edges.
Adjacencies:
  3 :  1  2
  2 :  3  1
  1 :  3  2
```


Example 3: create a directed graph:













```maxima
(%i1) load ("graphs")$
(%i2) d : create_graph(
        [1,2,3,4],
        [
         [1,3], [1,4],
         [2,3], [2,4]
        ],
        'directed = true)$
(%i3) print_graph(d)$
Digraph on 4 vertices with 4 arcs.
Adjacencies:
  4 :
  3 :
  2 :  4  3
  1 :  4  3
```

### Function: cube_graph (n)

Returns the *n*-dimensional cube.

### Function: cuboctahedron_graph (n)

Returns the cuboctahedron graph.

### Function: cycle_digraph (n)

Returns the directed cycle on *n* vertices.

### Function: cycle_graph (n)

Returns the cycle on *n* vertices.

### Function: cylindrical (radius, z, minz, maxz, azi, minazi, maxazi)

Draws 3D functions defined in cylindrical coordinates.


**3D**


`cylindrical(radius, z, minz, maxz, azi, minazi, maxazi)` plots the function `radius(z, azi)` defined in cylindrical coordinates, with variable *z* taking
values from *minz* to *maxz* and *azimuth* *azi* taking values
from *minazi* to *maxazi*.


This object is affected by the following *graphic options*: `xu_grid`, 
`yv_grid`, `line_type`, `key`, `wired_surface`, `enhanced3d` and `color`


Example:



```maxima
(%i1) draw3d(cylindrical(1,z,-2,2,az,0,2*%pi))$
```

(Figure draw_cylindrical)

See also: `xu_grid`, `yv_grid`, `line_type`, `key`, `wired_surface`.

### Variable: data_file_name

Default value: `"data.gnuplot"`


This is the name of the file with the numeric data needed
by Gnuplot to build the requested plot.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


See example in `gnuplot_file_name`.

### Function: degree_sequence (gr)

Returns the list of vertex degrees of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) degree_sequence(random_graph(10, 0.4));
(%o2)            [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

### Variable: delay

Default value: 5


This is the delay in 1/100 seconds of frames in animated gif files.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


Example:



```maxima
(%i1) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


Option `delay` is only active in animated gif’s; it is ignored in
any other case.


See also `terminal`, and `dimensions`.

See also: `terminal`.

### Function: diameter (gr)

Returns the diameter of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) diameter(dodecahedron_graph());
(%o2)                           5
```

### Function: dimacs_export (dimacs_export, gr, fl, dimacs_export, gr, fl, comment1, ..., commentn)

Exports the graph into the file *fl* in the DIMACS format. Optional
comments will be added to the top of the file.

### Function: dimacs_import (fl)

Returns the graph from file *fl* in the DIMACS format.

### Variable: dimensions

Default value: `[600,500]`


Dimensions of the output terminal. Its value is a list formed by
the width and the height. The meaning of the two numbers depends on
the terminal you are working with.


With terminals `gif`, `animated_gif`, `png`, `jpg`,
`svg`, `screen`, `wxt`, `qt`, `x11`,
`windows` and `aquaterm`, the integers represent the number of
points in each direction. If they are not integers, they are rounded.


With terminals `eps`, `epslatex`, `epslatex_standalone`,
`eps_color`, `multipage_eps`, `multipage_eps_color`,
`cairolatex_pdf`, `cairolatex_pdf_standalone`,
`pdf`, `multipage_pdf`, `pdfcairo`,
`multipage_pdfcairo`, `tikz`, and `tikz_standalone`, both
numbers represent hundredths of cm, which means that, by default,
pictures in these formats are 6 cm in width and 5 cm in height.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


Examples:


Option `dimensions` applied to file output
and to wxt canvas.



```maxima
(%i1) draw2d(
        dimensions = [300,300],
        terminal   = 'png,
        explicit(x^4,x,-1,1)) $
(%i2) draw2d(
        dimensions = [300,300],
        terminal   = 'wxt,
        explicit(x^4,x,-1,1)) $
```


Option `dimensions` applied to eps output.
We want an eps file with A4 portrait dimensions.



```maxima
(%i1) A4portrait: 100*[21, 29.7]$
(%i2) draw3d(
        dimensions = A4portrait,
        terminal   = 'eps,
        explicit(x^2-y^2,x,-2,2,y,-2,2)) $
```

### Function: dodecahedron_graph ()

Returns the dodecahedron graph.

### Function: draw (<arg_1>, ...)

Plots a series of scenes; its arguments are `gr2d` and/or `gr3d` 
objects, together with some options, or lists of scenes and options.
By default, the scenes are put together
in one column.


Besides scenes the function `draw` accepts the following global options:
`terminal`, `columns`, `dimensions`, `file_name`
and `delay`.


Functions `draw2d` and `draw3d` short cuts that can be used 
when only one scene is required, in two or three dimensions, respectively.


See also `gr2d` and `gr3d`.


Examples:



```maxima
(%i1) scene1: gr2d(title="Ellipse",
                   nticks=300,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i2) scene2: gr2d(title="Triangle",
                   polygon([4,5,7],[6,4,2]))$
(%i3) draw(scene1, scene2, columns = 2)$
```

(Figure draw_intro2)



```maxima
(%i1) scene1: gr2d(title="A sinus",
        grid=true,
        explicit(sin(t),t,0,2*%pi))$
(%i2) scene2: gr2d(title="A cosinus",
        grid=true,
        explicit(cos(t),t,0,2*%pi))$
(%i3) draw(scene1, scene2)$
```

(Figure draw_intro3)


The following two draw sentences are equivalent:


```maxima
(%i1) draw(gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1)));
(%o1)                          [gr3d(explicit)]
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1));
(%o2)                          [gr3d(explicit)]
```


Creating an animated gif file:


```maxima
(%i1) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o1)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```

(Figure draw_equiv)
See also `gr2d`, `gr3d`, `draw2d` and `draw3d`.

See also: `terminal`, `columns`, `dimensions`, `file_name`, `delay`, `draw2d`, `draw3d`, `gr2d`, `gr3d`.

### Function: draw2d (argument_1, ...)

This function is a shortcut for
`draw(gr2d(options, ..., graphic_object, ...))`.


It can be used to plot a unique scene in 2d, as can be seen in most examples below.


See also `draw` and `gr2d`.

See also: `draw`, `gr2d`.

### Function: draw3d (argument_1, ...)

This function is a shortcut for
`draw(gr3d(options, ..., graphic_object, ...))`.


It can be used to plot a unique scene in 3d, as can be seen in many examples below.


See also `draw` and `gr3d`.

See also: `draw`, `gr3d`.

### Function: draw_file (graphic option, ..., graphic object, ...)

Saves the current plot into a file. Accepted graphics options are:
`terminal`, `dimensions` and `file_name`. 


Example:



```maxima
(%i1) /* screen plot */
      draw(gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1)))$
(%i2) /* same plot in eps format */
      draw_file(terminal  = eps,
                dimensions = [5,5]) $
```

### Function: draw_graph (draw_graph, graph, draw_graph, graph, option1, ..., optionk)

Draws the graph using the `Package-draw` package.


The algorithm used to position vertices is specified by the optional
argument *program*. The default value is
`program=spring_embedding`. *draw_graph* can also use the
graphviz programs for positioning vertices, but graphviz must be
installed separately.


Example 1:












```maxima
(%i1) load ("graphs")$
(%i2) g:grid_graph(10,10)$
(%i3) m:max_matching(g)$
(%i4) draw_graph(g,
   spring_embedding_depth=100,
   show_edges=m, edge_type=dots,
   vertex_size=0)$
```


(Figure graphs09, Example of the use of draw_graph to draw a graph)


Example 2:






















```maxima
(%i1) load ("graphs")$
(%i2) g:create_graph(16,
    [
     [0,1],[1,3],[2,3],[0,2],[3,4],[2,4],
     [5,6],[6,4],[4,7],[6,7],[7,8],[7,10],[7,11],
     [8,10],[11,10],[8,9],[11,12],[9,15],[12,13],
     [10,14],[15,14],[13,14]
    ])$
(%i3) t:minimum_spanning_tree(g)$
(%i4) draw_graph(
    g,
    show_edges=edges(t),
    show_edge_width=4,
    show_edge_color=green,
    vertex_type=filled_square,
    vertex_size=2
    )$
```


(Figure graphs10, Example of the use of draw_graph to draw a graph)


Example 3:
























```maxima
(%i1) load ("graphs")$
(%i2) g:create_graph(16,
    [
     [0,1],[1,3],[2,3],[0,2],[3,4],[2,4],
     [5,6],[6,4],[4,7],[6,7],[7,8],[7,10],[7,11],
     [8,10],[11,10],[8,9],[11,12],[9,15],[12,13],
     [10,14],[15,14],[13,14]
    ])$
(%i3) mi : max_independent_set(g)$
(%i4) draw_graph(
    g,
    show_vertices=mi,
    show_vertex_type=filled_up_triangle,
    show_vertex_size=2,
    edge_color=cyan,
    edge_width=3,
    show_id=true,
    text_color=brown
    )$
```


(Figure graphs11, Example of the use of draw_graph to draw a graph)


Example 4:



























```maxima
(%i1) load ("graphs")$
(%i2) net : create_graph(
    [0,1,2,3,4,5],
    [
     [[0,1], 3], [[0,2], 2],
     [[1,3], 1], [[1,4], 3],
     [[2,3], 2], [[2,4], 2],
     [[4,5], 2], [[3,5], 2]
    ],
    directed=true
    )$
(%i3) draw_graph(
    net,
    show_weight=true,
    vertex_size=0,
    show_vertices=[0,5],
    show_vertex_type=filled_square,
    head_length=0.2,
    head_angle=10,
    edge_color="dark-green",
    text_color=blue
    )$
```


(Figure graphs12, Example of the use of draw_graph to draw a graph)


Example 5:








```maxima
(%i1) load("graphs")$
(%i2) g: petersen_graph(20, 2);
(%o2)                         GRAPH
(%i3) draw_graph(g, redraw=true, program=planar_embedding);
(%o3)                         done
```


(Figure graphs14, Example of the use of draw_graph to draw a graph)


Example 6:









```maxima
(%i1) load("graphs")$
(%i2) t: tutte_graph();
(%o2)                         GRAPH
(%i3) draw_graph(t, redraw=true, 
                    fixed_vertices=[1,2,3,4,5,6,7,8,9]);
(%o3)                         done
```


(Figure graphs15, Example of the use of draw_graph to draw a graph)

See also: `Package-draw`.

### Variable: draw_graph_program

Default value: *spring_embedding*


The default value for the program used to position vertices in
`draw_graph` program.

### Variable: draw_realpart

Default value: `true`


When `true`, functions to be drawn are considered as complex functions whose
real part value should be plotted; when `false`, nothing will be plotted when
the function does not give a real value. 


This option affects objects `explicit` and `parametric` in 2D and 3D, and
`parametric_005fsurface`.


Example:


```maxima
(%i1) draw2d(
        draw_realpart = false,
        explicit(sqrt(x^2  - 4*x) - x, x, -1, 5),
        color         = red,
        draw_realpart = true,
        parametric(x,sqrt(x^2  - 4*x) - x + 1, x, -1, 5) );
```

See also: `explicit`, `parametric`, `parametric_surface`.

### Variable: draw_renderer

Default value: `gnuplot_pipes`


The only permitted values are `gnuplot_pipes`, `gnuplot`,
`vtk`, `vtk6` or `vtk7`. When `draw_renderer` is set
to `vtk`, the VTK interface is used for draw.

### Function: drawdf (drawdf, dydx, ...options, and, objects..., drawdf, dvdu, u, v, ...options, and, objects..., drawdf, dvdu, u, umin, umax, v, vmin, vmax, ...options, and, objects..., drawdf, dxdt, dydt, ...options, and, objects..., drawdf, dudt, dvdt, u, v, ...options, and, objects..., drawdf, dudt, dvdt, u, umin, umax, v, vmin, vmax, ...options, and, objects...)

Function `drawdf` draws a 2D direction field with optional
solution curves and other graphics using the `draw` package.


The first argument specifies the derivative(s), and must be either an
expression or a list of two expressions.  *dydx*, *dxdt* and
*dydt* are expressions that depend on *x* and *y*.
*dvdu*, *dudt* and *dvdt* are expressions that depend on
*u* and *v*.


If the independent and dependent variables are not *x* and
*y*, then their names must be specified immediately following the
derivative(s), either as a list of two names
`[`*u*,*v*`]`, or as two lists of the form
`[`*u*,*umin*,*umax*`]` and
`[`*v*,*vmin*,*vmax*`]`.


The remaining arguments are *graphic options*, *graphic objects*,
or lists containing graphic options and objects, nested to arbitrary
depth.  The set of graphic options and objects supported by
`drawdf` is a superset of those supported by `draw2d` and
`gr2d` from the `draw` package.


The arguments are interpreted sequentially: *graphic options* affect
all following *graphic objects*.  Furthermore, *graphic objects*
are drawn on the canvas in order specified, and may obscure graphics
drawn earlier.  Some *graphic options* affect the global appearance
of the scene.


The additional *graphic objects* supported by `drawdf` include:
`solns_at`, `points_at`, `saddles_at`, `soln_at`,
`point_at`, and `saddle_at`.


The additional *graphic options* supported by `drawdf` include:
`field_degree`, `soln_arrows`, `field_arrows`,
`field_grid`, `field_color`, `show_field`,
`tstep`, `nsteps`, `duration`, `direction`,
`field_tstep`, `field_nsteps`, and `field_duration`.


Commonly used *graphic objects* inherited from the `draw`
package include: `explicit`, `implicit`, `parametric`,
`polygon`, `points`, `vector`, `label`, and all
others supported by `draw2d` and `gr2d`.


Commonly used *graphic options* inherited from the `draw`
package include:

`points_joined`, `color`,
`point_type`, `point_size`, `line_width`,
`line_type`, `key`, `title`, `xlabel`,
`ylabel`, `user_preamble`, `terminal`,
`dimensions`, `file_name`, and all
others supported by `draw2d` and `gr2d`.


See also `draw2d`, `rk`, `desolve` and 
`ode2`.


Users of wxMaxima or Imaxima may optionally use `wxdrawdf`, which
is identical to `drawdf` except that the graphics are drawn
within the notebook using `wxdraw`.


To make use of this function, write first `load("drawdf")`.


Examples:



```maxima
(%i1) load("drawdf")$
(%i2) drawdf(exp(-x)+y)$        /* default vars: x,y */
(%i3) drawdf(exp(-t)+y, [t,y])$ /* default range: [-10,10] */
(%i4) drawdf([y,-9*sin(x)-y/5], [x,1,5], [y,-2,2])$
```


For backward compatibility, `drawdf` accepts
most of the parameters supported by plotdf.



```maxima
(%i5) drawdf(2*cos(t)-1+y, [t,y], [t,-5,10], [y,-4,9],
             [trajectory_at,0,0])$
```


`soln_at` and `solns_at` draw solution curves
passing through the specified points, using a slightly
enhanced 4th-order Runge Kutta numerical integrator.



```maxima
(%i6) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             solns_at([0,0.1],[0,-0.1]),
             color=blue, soln_at(0,0))$
```


`field_degree=2` causes the field to be composed of quadratic
splines, based on the first and second derivatives at each grid point.
`field_grid=[`*COLS*,*ROWS*`]` specifies the number
of columns and rows in the grid.



```maxima
(%i7) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             field_degree=2, field_grid=[20,15],
             solns_at([0,0.1],[0,-0.1]),
             color=blue, soln_at(0,0))$
```


`soln_arrows=true` adds arrows to the solution curves, and (by
default) removes them from the direction field.  It also changes the
default colors to emphasize the solution curves.



```maxima
(%i8) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             soln_arrows=true,
             solns_at([0,0.1],[0,-0.1],[0,0]))$
```


`duration=40` specifies the time duration of numerical
integration (default 10).  Integration will also stop automatically if
the solution moves too far away from the plotted region, or if the
derivative becomes complex or infinite.  Here we also specify
`field_degree=2` to plot quadratic splines.  The equations below
model a predator-prey system.



```maxima
(%i9) drawdf([x*(1-x-y), y*(3/4-y-x/2)], [x,0,1.1], [y,0,1],
             field_degree=2, duration=40,
             soln_arrows=true, point_at(1/2,1/2),
             solns_at([0.1,0.2], [0.2,0.1], [1,0.8], [0.8,1],
                      [0.1,0.1], [0.6,0.05], [0.05,0.4],
                      [1,0.01], [0.01,0.75]))$
```


`field_degree='solns` causes the field to be composed
of many small solution curves computed by 4th-order
Runge Kutta, with better results in this case.



```maxima
(%i10) drawdf([x*(1-x-y), y*(3/4-y-x/2)], [x,0,1.1], [y,0,1],
              field_degree='solns, duration=40,
              soln_arrows=true, point_at(1/2,1/2),
              solns_at([0.1,0.2], [0.2,0.1], [1,0.8],
                       [0.8,1], [0.1,0.1], [0.6,0.05],
                       [0.05,0.4], [1,0.01], [0.01,0.75]))$
```


`saddles_at` attempts to automatically linearize the equation at
each saddle, and to plot a numerical solution corresponding to each
eigenvector, including the separatrices.  `tstep=0.05` specifies
the maximum time step for the numerical integrator (the default is
0.1).  Note that smaller time steps will sometimes be used in order to
keep the x and y steps small.  The equations below model a damped
pendulum.



```maxima
(%i11) drawdf([y,-9*sin(x)-y/5], tstep=0.05,
              soln_arrows=true, point_size=0.5,
              points_at([0,0], [2*%pi,0], [-2*%pi,0]),
              field_degree='solns,
              saddles_at([%pi,0], [-%pi,0]))$
```


`show_field=false` suppresses the field entirely.



```maxima
(%i12) drawdf([y,-9*sin(x)-y/5], tstep=0.05,
              show_field=false, soln_arrows=true,
              point_size=0.5,
              points_at([0,0], [2*%pi,0], [-2*%pi,0]),
              saddles_at([3*%pi,0], [-3*%pi,0],
                         [%pi,0], [-%pi,0]))$
```


`drawdf` passes all unrecognized parameters to `draw2d` or
`gr2d`, allowing you to combine the full power of the `draw`
package with `drawdf`.



```maxima
(%i13) drawdf(x^2+y^2, [x,-2,2], [y,-2,2], field_color=gray,
              key="soln 1", color=black, soln_at(0,0),
              key="soln 2", color=red, soln_at(0,1),
              key="isocline", color=green, line_width=2,
              nticks=100, parametric(cos(t),sin(t),t,0,2*%pi))$
```


`drawdf` accepts nested lists of graphic options and objects,
allowing convenient use of makelist and other function calls to
generate graphics.



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

See also: `draw2d`, `rk`, `desolve`, `ode2`.

### Variable: edge_color

The color used for displaying edges.

### Function: edge_coloring (gr)

Returns an optimal coloring of the edges of the graph *gr*.


The function returns the chromatic index and a list representing the
coloring of the edges of *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) [ch_index, col] : edge_coloring(p);
(%o3) [4, [[[0, 5], 3], [[5, 7], 1], [[0, 1], 1], [[1, 6], 2], 
[[6, 8], 1], [[1, 2], 3], [[2, 7], 4], [[7, 9], 2], [[2, 3], 2], 
[[3, 8], 3], [[5, 8], 2], [[3, 4], 1], [[4, 9], 4], [[6, 9], 3], 
[[0, 4], 2]]]
(%i4) assoc([0,1], col);
(%o4)                           1
(%i5) assoc([0,5], col);
(%o5)                           3
```

### Function: edge_connectivity (gr)

Returns the edge-connectivity of the graph *gr*.


See also `min_edge_cut`.

See also: `min_edge_cut`.

### Variable: edge_partition

A partition `[[e1,e2,...],...,[ek,...,em]]` of edges of the
graph. The edges of each list in the partition will be drawn using a
different color.

### Variable: edge_type

Defines how edges are displayed. See the *line_type* option for the
`draw` package.

### Variable: edge_width

The width of edges.

### Function: edges (gr)

Returns the list of edges (arcs) in a (directed) graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) edges(complete_graph(4));
(%o2)   [[2, 3], [1, 3], [1, 2], [0, 3], [0, 2], [0, 1]]
```

### Variable: elevation

Default value: `60`


A plot3d plot can be thought of as starting with the x and y axis in the
horizontal and vertical axis, as in plot2d, and the z axis coming out of
the screen.  The z axis is then rotated around the x axis through an
angle equal to `elevation` and then the new xy plane is rotated
around the new z axis through an angle `azimuth`. This option sets
the value for the elevation, in degrees.


See also `azimuth`.

See also: `elevation`, `azimuth`.

### Function: elevation_grid (mat, x0, y0, width, height)

Draws matrix *mat* in 3D space. *z* values are taken from *mat*,
the abscissas range from *x0* to $x0 + width$
and ordinates from *y0* to $y0 + height$. Element $a(1,1)$
is projected on point $(x0,y0+height)$, $a(1,n)$ on $(x0+width,y0+height)$,
$a(m,1)$ on $(x0,y0)$, and $a(m,n)$ on $(x0+width,y0)$.


This object is affected by the following *graphic options*: `line_type`,,
`line_width`  `key`,  `wired_surface`,  `enhanced3d` and `color`


In older versions of Maxima, `elevation_grid` was called `mesh`.
See also `mesh`.


Example:



```maxima
(%i1) m: apply(
            matrix,
            makelist(makelist(random(10.0),k,1,30),i,1,20)) $
(%i2) draw3d(
         color = blue,
         elevation_grid(m,0,0,3,2),
         xlabel = "x",
         ylabel = "y",
         surface_hide = true);
```

(Figure draw_elevation_grid)

See also: `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`, `elevation_grid`, `mesh`.

### Function: ellipse (xc, yc, a, b, ang1, ang2)

Draws ellipses and circles in 2D.



**2D**


`ellipse (xc, yc, a, b, ang1, ang2)`
plots an ellipse centered at `[xc, yc]` with horizontal and vertical
semi axis *a* and *b*, respectively, starting at angle *ang1* with an amplitude
equal to angle *ang2*.


This object is affected by the following *graphic options*: `nticks`, 
`transparent`, `fill_color`, `fill_density`, `border`, `line_width`, 
`line_type`, `key` and `color`


Example:



```maxima
(%i1) draw2d(transparent = false,
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

(Figure draw_ellipse)

See also: `nticks`, `transparent`, `fill_color`, `fill_density`, `border`, `line_type`, `key`.

### Function: empty_graph (n)

Returns the empty graph on *n* vertices.

### Variable: enhanced3d

Default value: `none`


If `enhanced3d` is `none`, surfaces are not colored in 3D plots.
In order to get a colored surface, a list must be assigned to option
`enhanced3d`, where the first element is an expression and the rest
are the names of the variables or parameters used in that expression. A list such 
`[f(x,y,z), x, y, z]` means that point `[x,y,z]` of the surface 
is assigned number `f(x,y,z)`, which will be colored according to 
the actual `palette`. For those 3D graphic objects defined in terms of
parameters, it is possible to define the color number in terms of
the parameters, as in `[f(u), u]`, as in objects `parametric` and 
`tube`, or `[f(u,v), u, v]`, as in object `parametric_surface`.
While all 3D objects admit the model based on absolute coordinates,
`[f(x,y,z), x, y, z]`, only two of them, namely `explicit`
and `elevation_grid`, accept also models defined on the `[x,y]` coordinates,
`[f(x,y), x, y]`. 3D graphic object `implicit` accepts only the
`[f(x,y,z), x, y, z]` model. Object `points` accepts also the
`[f(x,y,z), x, y, z]` model, but when points have a chronological nature,
model `[f(k), k]` is also valid, being `k` an ordering parameter.


When `enhanced3d` is assigned something different to `none`, options
`color` and `surface_hide` are ignored.


The names of the variables defined in the lists may be different to those
used in the definitions of the graphic objects.


In order to maintain back compatibility, `enhanced3d = false` is equivalent
to `enhanced3d = none`, and `enhanced3d = true` is equivalent to 
`enhanced3d = [z, x, y, z]`.  If an expression is given to `enhanced3d`,
its variables must be the same used in the surface definition. This is not
necessary when using lists.


See option `palette` to learn how palettes are specified.


Examples:


`explicit` object with coloring defined by the `[f(x,y,z), x, y, z]` model.



```maxima
(%i1) draw3d(
         enhanced3d = [x-z/10,x,y,z],
         palette    = gray,
         explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
```

(Figure draw_enhanced3d)


`explicit` object with coloring defined by the `[f(x,y), x, y]` model.
The names of the variables defined in the lists may be different to those
used in the definitions of the graphic objects; in this case, `r` corresponds
to `x`, and `s` to `y`.



```maxima
(%i1) draw3d(
         enhanced3d = [sin(r*s),r,s],
         explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
```

(Figure draw_enhanced3d2)


`parametric` object with coloring defined by the `[f(x,y,z), x, y, z]` model.



```maxima
(%i1) draw3d(
         nticks = 100,
         line_width = 2,
         enhanced3d = [if y>= 0 then 1 else 0, x, y, z],
         parametric(sin(u)^2,cos(u),u,u,0,4*%pi)) $
```

(Figure draw_enhanced3d3)


`parametric` object with coloring defined by the `[f(u), u]` model.
In this case, `(u-1)^2` is a shortcut for `[(u-1)^2,u]`.



```maxima
(%i1) draw3d(
         nticks = 60,
         line_width = 3,
         enhanced3d = (u-1)^2,
         parametric(cos(5*u)^2,sin(7*u),u-2,u,0,2))$
```

(Figure draw_enhanced3d4)


`elevation_grid` object with coloring defined by the `[f(x,y), x, y]` model.



```maxima
(%i1) m: apply(
           matrix,
           makelist(makelist(cos(i^2/80-k/30),k,1,30),i,1,20)) $
(%i2) draw3d(
         enhanced3d = [cos(x*y*10),x,y],
         elevation_grid(m,-1,-1,2,2),
         xlabel = "x",
         ylabel = "y");
```

(Figure draw_enhanced3d5)


`tube` object with coloring defined by the `[f(x,y,z), x, y, z]` model.



```maxima
(%i1) draw3d(
         enhanced3d = [cos(x-y),x,y,z],
         palette = gray,
         xu_grid = 50,
         tube(cos(a), a, 0, 1, a, 0, 4*%pi) )$
```

(Figure draw_enhanced3d6)


`tube` object with coloring defined by the `[f(u), u]` model.
Here, `enhanced3d = -a` would be the shortcut for `enhanced3d = [-foo,foo]`.



```maxima
(%i1) draw3d(
         capping = [true, false],
         palette = [26,15,-2],
         enhanced3d = [-foo, foo],
         tube(a, a, a^2, 1, a, -2, 2) )$
```

(Figure draw_enhanced3d7)


`implicit` and `points` objects with coloring defined by the `[f(x,y,z), x, y, z]` model.



```maxima
(%i1) draw3d(
         enhanced3d = [x-y,x,y,z],
         implicit((x^2+y^2+z^2-1)*(x^2+(y-1.5)^2+z^2-0.5)=0.015,
                  x,-1,1,y,-1.2,2.3,z,-1,1)) $
(%i2) m: makelist([random(1.0),random(1.0),random(1.0)],k,1,2000)$
```

(Figure draw_enhanced3d9)


```maxima
(%i3) draw3d(
         point_type = filled_circle,
         point_size = 2,
         enhanced3d = [u+v-w,u,v,w],
         points(m) ) $
```

(Figure draw_enhanced3d10)


When points have a chronological nature, model `[f(k), k]` is also valid,
being `k` an ordering parameter.



```maxima
(%i1) m:makelist([random(1.0), random(1.0), random(1.0)],k,1,5)$
(%i2) draw3d(
         enhanced3d = [sin(j), j],
         point_size = 3,
         point_type = filled_circle,
         points_joined = true,
         points(m)) $
```

(Figure draw_enhanced3d11)

See also: `enhanced3d`, `parametric`, `tube`, `elevation_grid`.

### Variable: error_type

Default value: `y`


Depending on its value, which can be `x`, `y`, or `xy`,
graphic object `errors` will draw points with horizontal, vertical,
or both, error bars. When `error_type=boxes`, boxes will be drawn
instead of crosses.


See also `errors`.

See also: `errors`.

### Function: errors (x1, x2, ..., y1, y2, ...)

Draws points with error bars, horizontally, vertically or both, depending on the
value of option `error_type`.


**2D**


If `error_type = x`, arguments to `errors` must be of the form
`[x, y, xdelta]` or `[x, y, xlow, xhigh]`.  If `error_type = y`, 
arguments must be of the form `[x, y, ydelta]` or
`[x, y, ylow, yhigh]`.  If `error_type = xy` or
`error_type = boxes`, arguments to `errors` must be of the form
`[x, y, xdelta, ydelta]` or `[x, y, xlow, xhigh, ylow, yhigh]`.


See also `error_005ftype`.


This object is affected by the following *graphic options*: `error_type`,  
`points_joined`,  `line_width`,  `key`,  `line_type`,  
`color`  `fill_density`,  `xaxis_secondary`  and  `yaxis_005fsecondary`.


Option `fill_density` is only relevant when `error_type=boxes`.


Examples:


Horizontal error bars.



```maxima
(%i1) draw2d(
        error_type = 'y,
        errors([[1,2,1], [3,5,3], [10,3,1], [17,6,2]]))$
```

(Figure draw_errors)


Vertical and horizontal error bars.



```maxima
(%i1) draw2d(
        error_type = 'xy,
        points_joined = true,
        color = blue,
        errors([[1,2,1,2], [3,5,2,1], [10,3,1,1], [17,6,1/2,2]]));
```

(Figure draw_errors2)

See also: `error_type`, `points_joined`, `line_width`, `key`, `line_type`, `fill_density`, `xaxis_secondary`, `yaxis_secondary`.

### Function: evolution (F, y0, n, ..., options, ..., ;)

Draws *n+1* points in a two-dimensional graph, where the horizontal
coordinates of the points are the integers 0, 1, 2, ..., *n*, and
the vertical coordinates are the corresponding values *y(n)* of the
sequence defined by the recurrence relation


```maxima
y(n+1) = F(y(n))
```


$$y_{n+1} = F(y_n)$$


With initial value *y(0)* equal to *y0*. *F* must be an
expression that depends only on one variable (in the example, it
depend on *y*, but any other variable can be used),
*y0* must be a real number and *n* must be a positive integer.
 This function accepts the same options as `plot2d`.


**Example**.



```maxima
(%i1) evolution(cos(y), 2, 11);
```

(Figure dynamics1)

See also: `plot2d`.

### Function: evolution2d (F, G, u, v, u0, y0, n, options, ..., ;)

Shows, in a two-dimensional plot, the first *n+1* points in the
sequence of points defined by the two-dimensional discrete dynamical
system with recurrence relations


```maxima
u(n+1) = F(u(n), v(n))    v(n+1) = G(u(n), v(n))
```


$$\cases{u_{n+1} = F(u_n, v_n) &\cr v_{n+1} = G(u_n, v_n)}$$


With initial values *u0* and *v0*. *F* and *G* must be
two expressions that depend only on two variables, *u* and
*v*, which must be named explicitly in a list. The options are the
same as for `plot2d`.


**Example**. Evolution of a two-dimensional discrete dynamical system:



```maxima
(%i1) f: 0.6*x*(1+2*x)+0.8*y*(x-1)-y^2-0.9$
(%i2) g: 0.1*x*(1-6*x+4*y)+0.1*y*(1+9*y)-0.4$
(%i3) evolution2d([f,g], [x,y], [-0.5,0], 50000, [style,dots]);
```


(Figure dynamics5)


And an enlargement of a small region in that fractal:



```maxima
(%i9) evolution2d([f,g], [x,y], [-0.5,0], 300000, [x,-0.8,-0.6],
                  [y,-0.4,-0.2], [style, dots]);
```


(Figure dynamics6)

See also: `plot2d`.

### Function: explicit (explicit, expr, var, minval, maxval, explicit, fcn, var, minval, maxval, explicit, expr, var1, minval1, maxval1, var2, minval2, maxval2, explicit, fcn, var1, minval1, maxval1, var2, minval2, maxval2)

Draws explicit functions in 2D and 3D.


**2D**


`explicit(fcn,var,minval,maxval)` plots explicit function *fcn*,
with variable *var* taking values from *minval* to *maxval*.


This object is affected by the following *graphic options*: `nticks`, 
`adapt_depth`, `draw_realpart`, `line_width`, `line_type`, `key`, 
`filled_func`, `fill_color`, `fill_density`, and `color`


Example:



```maxima
(%i1) draw2d(line_width = 3,
             color      = blue,
             explicit(x^2,x,-3,3) )$
```

(Figure draw_explicit)


```maxima
(%i2) draw2d(fill_color  = brown,
             filled_func = true,
             explicit(x^2,x,-3,3) )$
```

(Figure draw_explicit2)


**3D**


`explicit(fcn, var1, minval1, maxval1, var2, minval2, maxval2)` plots the explicit function *fcn*, with
variable *var1* taking values from *minval1* to *maxval1* and
variable *var2* taking values from *minval2* to *maxval2*.


This object is affected by the following *graphic options*: `draw_realpart`, `xu_grid`,
`yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`,
`enhanced3d` and `color`.


Example:



```maxima
(%i1) draw3d(key   = "Gauss",
             color = "#a02c00",
             explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
             yv_grid     = 10,
             color = blue,
             key   = "Plane",
             explicit(x+y,x,-5,5,y,-5,5),
             surface_hide = true)$
```

(Figure draw_explicit3)


See also `filled_func` for filled functions.

See also: `nticks`, `draw_realpart`, `line_width`, `line_type`, `key`, `filled_func`, `fill_color`, `fill_density`, `xu_grid`, `yv_grid`, `wired_surface`, `enhanced3d`.

### Variable: file_name

Default value: `"maxima_out"`


This is the name of the file where terminals `png`, `jpg`, `gif`,
`eps`, `eps_color`, `pdf`, `pdfcairo` and `svg`
will save the graphic.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


Example:



```maxima
(%i1) draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'png)$
```


See also `terminal`,  `dimensions_005fdraw`.

See also: `terminal`, `dimensions_draw`.

### Variable: fill_color

Default value: `"red"`


`fill_color` specifies the color for filling polygons and
2d `explicit` functions.


See `color` to learn how colors are specified.

### Variable: fill_density

Default value: 0


`fill_density` is a number between 0 and 1 that specifies
the intensity of the `fill_color` in `bars` objects.


See `bars` for examples.

### Variable: filled_func

Default value: `false`


Option `filled_func` controls how regions limited by functions
should be filled. When `filled_func` is `true`, the region
bounded by the function defined with object `explicit` and the
bottom of the graphic window is filled with `fill_color`. When 
`filled_func` contains a function expression, then the region bounded
by this function and the function defined with object `explicit` 
will be filled. By default, explicit functions are not filled.


A useful special case is `filled_func=0`, which generates the region 
bond by the horizontal axis and the explicit function.


This option affects only the 2d graphic object `explicit`.


Example:


Region bounded by an `explicit` object and the bottom of the
graphic window.


```maxima
(%i1) draw2d(fill_color  = red,
             filled_func = true,
             explicit(sin(x),x,0,10) )$
```

(Figure draw_filledfunc)


Region bounded by an `explicit` object and the function
defined by option `filled_func`. Note that the variable in
`filled_func` must be the same as that used in `explicit`.


```maxima
(%i1) draw2d(fill_color  = grey,
             filled_func = sin(x),
             explicit(-sin(x),x,0,%pi));
```

(Figure draw_filledfunc2)
See also `fill_color` and `explicit`.

See also: `explicit`, `fill_color`.

### Variable: fixed_vertices

Specifies a list of vertices which will have positions fixed along a regular polygon.
Can be used when `program=spring_embedding`.

### Function: flower_snark (n)

Returns the flower graph on *4n* vertices.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) f5 : flower_snark(5)$
(%i3) chromatic_index(f5);
(%o3)                           4
```

### Variable: font

Default value: `""` (empty string)


This option can be used to set the font face to be used by the terminal.
Only one font face and size can be used throughout the plot.


Since this is a global graphics option, its position in the scene description
does not matter.


See also `font_005fsize`.


Gnuplot doesn’t handle fonts by itself, it leaves this task to the
support libraries of the different terminals, each one with its own
philosophy about it. A brief summary follows:



- *
*x11*:
Uses the normal x11 font server mechanism.

Example:

```maxima
(%i1) draw2d(font      = "Arial", 
             font_size = 20,
             label(["Arial font, size 20",1,1]))$
```
- *
*windows*:
The windows terminal doesn’t support changing of fonts from inside the plot.
Once the plot has been generated, the font can be changed right-clicking on
the menu of the graph window.
- *
*png, jpeg, gif*:
The *libgd* library uses the font path stored in the environment
variable `GDFONTPATH`; in this case, it is only necessary to
set option `font` to the font’s name. It is also possible to
give the complete path to the font file.

Examples:

Option `font` can be given the complete path to the font file:

```maxima
(%i1) path: "/usr/share/fonts/truetype/freefont/" $
(%i2) file: "FreeSerifBoldItalic.ttf" $
(%i3) draw2d(
        font      = concat(path, file), 
        font_size = 20,
        color     = red,
        label(["FreeSerifBoldItalic font, size 20",1,1]),
        terminal  = png)$
```

If environment variable `GDFONTPATH` is set to the
path where font files are allocated, it is possible to
set graphic option `font` to the name of the font.

```maxima
(%i1) draw2d(
        font      = "FreeSerifBoldItalic", 
        font_size = 20,
        color     = red,
        label(["FreeSerifBoldItalic font, size 20",1,1]),
        terminal  = png)$
```
- *
*Postscript*:
Standard Postscript fonts are:
`"Times-Roman"`, `"Times-Italic"`, `"Times-Bold"`,
`"Times-BoldItalic"`,
`"Helvetica"`, `"Helvetica-Oblique"`, `"Helvetica-Bold"`,
`"Helvetic-BoldOblique"`, `"Courier"`,
`"Courier-Oblique"`, `"Courier-Bold"`,
and `"Courier-BoldOblique"`.
  
Example:

```maxima
(%i1) draw2d(
        font      = "Courier-Oblique", 
        font_size = 15,
        label(["Courier-Oblique font, size 15",1,1]),
        terminal = eps)$
```
- *
*pdf*:
Uses same fonts as *Postscript*.
- *
*pdfcairo*:
Uses same fonts as *wxt*.
- *
*wxt*:
The *pango* library finds fonts via the `fontconfig` utility.
- *
*aqua*:
Default is `"Times-Roman"`.


The gnuplot documentation is an important source of information about terminals and fonts.

See also: `font_size`.

### Variable: font_size

Default value: 10


This option can be used to set the font size to be used by the terminal.
Only one font face and size can be used throughout the plot. `font_size` is
active only when option `font` is not equal to the empty string.


Since this is a global graphics option, its position in the scene description
does not matter.


See also `font`.

See also: `font`.

### Function: from_adjacency_matrix (A)

Returns the graph represented by its adjacency matrix *A*.

### Function: frucht_graph ()

Returns the Frucht graph.

### Function: geomap (geomap, numlist, geomap, numlist, 3Dprojection)

Draws cartographic maps in 2D and 3D.


**2D**


This function works together with global variable `boundaries_array`.


Argument *numlist* is a list containing numbers or lists of numbers.
All these numbers must be integers greater or equal than zero, 
representing the components of global array `boundaries_array`.


Each component of `boundaries_array` is an array of floating
point quantities, the coordinates of a polygonal segment or map boundary.


`geomap (numlist)` flattens its arguments and draws the
associated boundaries in `boundaries_array`.


This object is affected by the following *graphic options*: `line_width`, 
`line_type` and `color`.


Examples:


A simple map defined by hand:


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

(Figure worldmap_geomap)


The auxiliary package `worldmap` sets the global variable
`boundaries_array` to real world boundaries in
(longitude, latitude) coordinates. These data are in the 
public domain and come from 

[https://web.archive.org/web/20100310124019/http://www-cger.nies.go.jp/grid-e/gridtxt/grid19.html]().
Package `worldmap` defines also boundaries for countries,
continents and coastlines as lists with the necessary components of 
`boundaries_array` (see file `share/draw/worldmap.mac`
for more information). Package `worldmap` automatically loads 
package `worldmap`.


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

(Figure worldmap_geomap2)


Package `worldmap` is also useful for plotting
countries as polygons. In this case, graphic object
`geomap` is no longer necessary and the `polygon`
object is used instead. Since lists are now used and not
arrays, maps rendering will be slower. See also `make_poly_country`
and `make_poly_continent` to understand the following code.


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

(Figure worldmap_geomap3)



**3D**


`geomap (numlist)` projects map boundaries on the sphere of radius 1
centered at (0,0,0). It is possible to change the sphere or the projection type
by using `geomap (numlist,3Dprojection)`.


Available 3D projections:



- *
`[spherical_projection,x,y,z,r]`: projects map boundaries on the sphere of
radius *r* centered at (*x*,*y*,*z*).

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap(Australia), /* default projection */
             geomap(Australia,
                    [spherical_projection,2,2,2,3]))$
```
(Figure worldmap_geomap4)
- *
`[cylindrical_projection,x,y,z,r,rc]`: re-projects spherical map boundaries on the cylinder of radius
*rc* and axis passing through the poles of the globe of radius *r* centered at (*x*,*y*,*z*).

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap([America_coastlines,Eurasia_coastlines],
                    [cylindrical_projection,2,2,2,3,4]))$
```
(Figure worldmap_geomap5)
- *
`[conic_projection,x,y,z,r,alpha]`: re-projects spherical map boundaries on the cones of angle *alpha*,
with axis passing through the poles of the globe of radius *r* centered at (*x*,*y*,*z*). Both 
the northern and southern cones are tangent to sphere.

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap(World_coastlines,
                    [conic_projection,0,0,0,1,90]))$
```

(Figure worldmap_geomap6)


See also [https://riotorto.users.sourceforge.net/Maxima/gnuplot/geomap/]()
for more elaborated examples.

See also: `line_width`, `line_type`, `make_poly_country`, `make_poly_continent`.

### Variable: geomview

This is an abbreviation for `[plot_format, geomview]`. See
`plot_005fformat`.

See also: `plot_format`.

### Variable: geomview_command

This variable stores the name of the command used to run the geomview
program when the plot format is `geomview`. Its default value is
"geomview".  If the geomview program is not found unless you give
its complete path or if you want to try a different version of it,
you may change the value of this variable. For instance,






```maxima
maxima
(%i1) geomview_command: "/usr/local/bin/my_geomview"$
```


This variable must contain a string.


See also `gnuplot_command` and `xmaxima_005fplot_005fcommand`.

See also: `gnuplot_command`, `xmaxima_plot_command`.

### Function: get_all_vertices_by_label (l, gr)

Returns all vertices, if any, which have the label *l* in graph *gr*.


If there are no such vertices,
`get_all_vertices_by_label` returns an empty list `[]`.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g: create_graph ([[0, "Zero"], [1, "One"], [2, "Other"], [3, "Other"]], []) $
(%i3) get_all_vertices_by_label ("Zero", g);
(%o3)                          [0]
(%i4) get_all_vertices_by_label ("Two", g);
(%o4)                          []
(%i5) get_all_vertices_by_label ("Other", g);
(%o5)                        [2, 3]
```

### Function: get_edge_weight (get_edge_weight, e, gr, get_edge_weight, e, gr, ifnot)

Returns the weight of the edge *e* in the graph *gr*.


If there is no weight assigned to the edge, the function returns 1. If
the edge is not present in the graph, the function signals an error or
returns the optional argument *ifnot*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(5)$
(%i3) get_edge_weight([1,2], c5);
(%o3)                           1
(%i4) set_edge_weight([1,2], 2.0, c5);
(%o4)                         done
(%i5) get_edge_weight([1,2], c5);
(%o5)                          2.0
```

### Function: get_pixel (pic, x, y)

Returns pixel from picture. Coordinates *x* and *y* range from 0 to
`width-1` and `height-1`, respectively.

### Function: get_plot_option (keyword, index)

Returns the current default value of the option named *keyword*,
which is a list. The optional argument *index* must be a positive
integer which can be used to extract only one element from the list
(element 1 is the name of the option).


See also `set_plot_option`, `remove_plot_option` and the
section on `Plotting-Options`.

See also: `set_plot_option`, `remove_plot_option`, `Plotting-Options`.

### Function: get_unique_vertex_by_label (l, gr)

Returns the unique vertex which has the label *l* in graph *gr*.


If there is no such vertex,
`get_unique_vertex_by_label` returns `false`.


If there are two or more vertices with label *l*,
`get_unique_vertex_by_label` reports an error.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g: create_graph ([[0, "Zero"], [1, "One"], [2, "Other"], [3, "Other"]], []) $
(%i3) get_unique_vertex_by_label ("Zero", g);
(%o3)                           0
(%i4) get_unique_vertex_by_label ("Two", g);
(%o4)                         false
(%i5) errcatch (get_unique_vertex_by_label ("Other", g));
get_unique_vertex_by_label: two or more vertices have the same label "Other"
(%o5)                          []
```

### Function: get_vertex_label (v, gr)

Returns the label of the vertex *v* in the graph *gr*.


If no label is assigned to vertex *v*,
`get_vertex_label` returns `false`.


Example:








```maxima
(%i1) load("graphs")$
(%i2) g: create_graph([[0, "Zero"], [1, "One"], 2, 3], [])$
(%i3) get_vertex_label(0, g);
(%o3)                         Zero
(%i4) get_vertex_label(2, g);
(%o4)                         false
```

### Function: girth (gr)

Returns the length of the shortest cycle in *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : heawood_graph()$
(%i3) girth(g);
(%o3)                           6
```

### Variable: gnuplot

This is an abbreviation for `[plot_format, gnuplot]`. See
`plot_005fformat`.

See also: `plot_format`.

### Function: gnuplot_close ()

Closes the pipe to gnuplot which is used with the `gnuplot_pipes` format.

### Variable: gnuplot_command

This variable stores the name of the command used to run the gnuplot
program when the plot format is `gnuplot` or
`gnuplot_pipes`. Its default value is "gnuplot". If the gnuplot
program is not found unless you give its complete path or if you want to
try a different version of it, you may change the value of this
variable. For instance,






```maxima
maxima
(%i1) gnuplot_command: "/usr/local/bin/my_gnuplot"$
```


This variable must contain a string.


See also `geomview_command` and `xmaxima_005fplot_005fcommand`.

See also: `geomview_command`, `xmaxima_plot_command`.

### Variable: gnuplot_curve_styles

This is an obsolete option that has been replaced by `style`.

See also: `style`.

### Variable: gnuplot_curve_titles

This is an obsolete option that has been replaced by `legend` described
above.

See also: `legend`.

### Variable: gnuplot_default_term_command

[gnuplot_default_term_command, *command*]


The gnuplot command to set the terminal type for the default
terminal. It this option is not set, the command used will be: `"set term wxt size 640,480 font \",12\"; set term pop"`.

### Variable: gnuplot_dumb_term_command

[gnuplot_dumb_term_command, *command*]


The gnuplot command to set the terminal type for the dumb terminal.  It
this option is not set, the command used will be: `"set term dumb 79 22"`, which makes the text output 79 characters by 22 characters.

### Variable: gnuplot_file_args

When a graphic file is going to be created using `gnuplot`, this
variable is used to specify the format used to print the file name given
to gnuplot. Its default value is "~a" in SBCL, Openmcl and GCL, and "~s"
in other lisp versions, which means that the name of the file will be
passed without quotes if SBCL, Openmcl or GCL are used, and within
quotes if other Lisp versions are used. The contents of this variable
can be changed in order to add options for the gnuplot program, adding
those options before the format directive "~s".

### Variable: gnuplot_file_name

Default value: `"maxout_xxx.gnuplot"` with `"xxx"`
being a number that is unique to each concurrently-running
maxima process.


This is the name of the file with the necessary commands to
be processed by Gnuplot.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


Example:



```maxima
(%i1) draw2d(
       file_name = "my_file",
       gnuplot_file_name = "my_commands_for_gnuplot",
       data_file_name    = "my_data_for_gnuplot",
       terminal          = png,
       explicit(x^2,x,-1,1)) $
```


See also `data_005ffile_005fname`.

See also: `data_file_name`.

### Variable: gnuplot_out_file

It can be used to replace the default name for the file that contains
the commands that will interpreted by gnuplot, when the terminal is set
to `default`, or to replace the default name of the graphic file
that gnuplot creates, when the terminal is different from
`default`. If it contains one or more slashes, “/”, the name of
the file will be left as it is; otherwise, it will be appended to the
path of the temporary directory. The complete name of the files created
by the plotting commands is always sent as output of those commands so
they can be seen if the command is ended by semi-colon.

### Variable: gnuplot_pdf_term_command

The gnuplot command to set the terminal type for the PDF
terminal.  If this option is not set, the command used will be: `"set term pdfcairo color solid lw 3 size 17.2 cm, 12.9 cm font \",18\""`. See the gnuplot documentation for more information.

### Variable: gnuplot_pipes

This is an abbreviation for `[plot_format, gnuplot_pipes]`. See
`plot_005fformat`.

See also: `plot_format`.

### Variable: gnuplot_pm3d

With a value of `false`, it can be used to disable the use of PM3D
mode, which is enabled by default.

### Variable: gnuplot_png_term_command

The gnuplot command to set the terminal type for the PNG terminal.  If
this option is not set, the command used will be:
`"set term pngcairo font \",12\""`. See the gnuplot documentation
for more information.

### Variable: gnuplot_postamble

This option inserts gnuplot commands after other commands sent to
Gnuplot and right before the plot command is sent. Any valid gnuplot
commands may be used. Multiple commands should be separated with a
semi-colon. See also `gnuplot_005fpreamble`.

See also: `gnuplot_preamble`.

### Variable: gnuplot_preamble

This option inserts gnuplot commands before any other commands sent to
Gnuplot. Any valid gnuplot commands may be used. Multiple commands should
be separated with a semi-colon. See also `gnuplot_005fpostamble`.

See also: `gnuplot_postamble`.

### Variable: gnuplot_ps_term_command

The gnuplot command to set the terminal type for the PostScript
terminal.  If this option is not set, the command used will be: `"set term postscript eps color solid lw 2 size 16.4 cm, 12.3 cm font \",24\""`. See the gnuplot documentation for `set term postscript` for
more information.

### Function: gnuplot_replot (gnuplot_replot, gnuplot_replot, s)

Updates the gnuplot window.  If `gnuplot_replot` is called with a
gnuplot command in a string *s*, then `s` is sent to gnuplot
before reploting the window.

### Function: gnuplot_reset ()

Resets the state of gnuplot used with the `gnuplot_pipes` format.  To
update the gnuplot window call `gnuplot_replot` after `gnuplot_reset`.

See also: `gnuplot_replot`.

### Function: gnuplot_restart ()

Closes the pipe to gnuplot which is used with the `gnuplot_pipes`
format and opens a new pipe.

### Variable: gnuplot_script_file

Creates a plot with `plot2d`, `plot3d`, `mandelbrot` or
`julia` using the `gnuplot` `plot_format` and saving
the script sent to Gnuplot in the file specified by *file_name_or_function*.
The value *file_name_or_function* can be a string or a Maxima function of
one variable that returns a string. If that string corresponds to a
complete file path (directory and file name), the script will be created in
that file and will not be deleted after Maxima is closed; otherwise, the
string will give the name of a file to be created in the temporary directory
and deleted when Maxima is closed.


In this example, the script file name is set to “sin.gnuplot”, in the
current directory.






```maxima
maxima

(%i1) plot2d( sin(x), [x,0,2*%pi], [gnuplot_script_file, "./sin.gnuplot"]);
(%o1)                    [./sin.gnuplot]
```


In this example, `gnuplot_prt(file)` is a function that takes
the default file name, *file*. It constructs a full file name for
the data file by interpolating a random 8-digit integer with a pad of
zeros into the default file name (a 16-character random string followed
by “.gnuplot”). The temporary directory is determined by
`maxima_tempdir` (it is “/tmp” in this example).









```maxima
maxima

(%i1) gnuplot_prt(file) := block([beg,end],
       [beg,end] : split(file,"."),
       printf(false,"~a_~8,'0d.~a",beg,random(10^8-1),end)) $


(%i2) plot2d( sin(x), [x,0,2*%pi], [gnuplot_script_file, gnuplot_prt]);
(%o2)       [/tmp/nxuo4x28s6wocvjw_99211646.gnuplot]
```


By default, the script would have been saved in a file named
`random-string.gnuplot` (random-string = nxuo4x28s6wocvjw_99211646 in this
example) in the temporary directory. If the print statement in function
`gnuplot_prt` above included a directory path, the file would have
been saved in that directory rather than in the temporary directory.

See also: `plot_format`, `maxima_tempdir`.

### Function: gnuplot_send (s)

Sends the command *s* to the gnuplot pipe. If that pipe is not currently
opened, it will be opened before sending the command. *s* must be a
string.

### Function: gnuplot_start ()

Opens the pipe to gnuplot used for plotting with the `gnuplot_pipes`
format.  Is not necessary to manually open the pipe before plotting.

### Variable: gnuplot_strings

With a value of `true`, all strings used in labels and titles will
be interpreted by gnuplot as “enhanced” text, if the terminal being used
supports it. In enhanced mode, some characters such as ^ and _ are not
printed, but interpreted as formatting characters. For a list of the
formatting characters and their meaning, see the documentation for enhanced
in Gnuplot. The default value for this option is `false`, which will
not treat any characters as formatting characters.

### Variable: gnuplot_svg_background

[gnuplot_svg_background, *color*] 

    nognuplot_svg_background


Specify the background color for SVG image output.
*color* must be a string which specifies a color name recognized by Gnuplot,
or an RGB triple of the form `"#xxxxxx"` where `x` is a hexadecimal digit.
The default value is `"white"`.


When the value of `gnuplot_svg_background` is `false`,
the background is the default determined by Gnuplot.
At present (April 2023),
the Gnuplot default is to specify the background in SVG output as `"none"`.


`nognuplot_svg_background`, specified by itself without a value,
is equivalent to `[gnuplot_svg_background, false]`.

### Variable: gnuplot_svg_term_command

The gnuplot command to set the terminal type for the SVG
terminal.  If this option is not set, the command used will be:
`"set term svg font \",14\""`. See the gnuplot documentation for
more information.

### Variable: gnuplot_term

Sets the output terminal type for gnuplot. The argument *terminal_name*
can be a string or one of the following 3 special symbols


- *
**default** (default value)

Gnuplot output is displayed in a separate graphical window and the
gnuplot terminal used will be specified by the value of the option
`gnuplot_005fdefault_005fterm_005fcommand`.
- *
**dumb**

Gnuplot output is saved to a file `random-string.txt` using "ASCII
art" approximation to graphics. If the option `gnuplot_out_file` is
set to *filename*, the plot will be saved there, instead of the
default `random-string.gnuplot`. The settings for the “dumb”
terminal of Gnuplot are given by the value of option
`gnuplot_005fdumb_005fterm_005fcommand`. If option `run_viewer` is set
to true and the plot_format is `gnuplot` that ASCII representation
will also be shown in the Maxima or Xmaxima console.
- *
**ps**

Gnuplot generates commands in the PostScript page description language.
If the option `gnuplot_out_file` is set to *filename*, gnuplot
writes the PostScript commands to *filename*.  Otherwise, it is
saved as `maxplot.ps` file. The settings for this terminal are given by the value of the option `gnuplot_005fdumb_005fterm_005fcommand`.
- *
A string representing any valid gnuplot term specification

Gnuplot can generate output in many other graphical formats such as png,
jpeg, svg etc. To use those formats, option `gnuplot_term` can be
set to any supported gnuplot term name (which must be a symbol) or even a
full gnuplot term specification with any valid options (which must be a string).  For
example `[gnuplot_term, png]` creates output in PNG (Portable
Network Graphics) format while `[gnuplot_term, "png size 1000,1000"]` creates PNG of 1000 x 1000 pixels size.  If the option
`gnuplot_out_file` is set to *filename*, gnuplot writes the
output to *filename*.  Otherwise, it is saved as
`maxplot.term` file, where *term* is gnuplot terminal
name.

See also: `gnuplot_default_term_command`, `gnuplot_out_file`, `gnuplot_dumb_term_command`, `run_viewer`.

### Variable: gnuplot_view_args

This variable is the format used to parse the argument that will be
passed to the gnuplot program when the plot format is
`gnuplot`. Its default value is "-persist ~a" when SBCL, Openmcl or
GCL are used, and "-persist ~s" with other Lisp variants, where "~a" or
"~s" will be replaced with the name of the file where the gnuplot
commands have been written. The file name is usually
"random-string.gnuplot"; "~s" passes that name within quotes, while "~a"
passes it without quotes.


The option `-persist` tells gnuplot to exit after the commands in
the file have been executed, without closing the window that displays
the plot; even though the plot window remains it is inactive, namely,
some actions like trying to rotate a 3d plot or adding a grid will not
respond (the `gnuplot_pipes` format keeps the plot window active).


Those familiar with gnuplot, might want to change the value of this
variable. For example, by changing it to:






```maxima
maxima
(%i1) gnuplot_view_args: "~s -"$
```


gnuplot will not be closed after the commands in the file have been
executed; thus, the window with the plot will remain active, as well as the
gnuplot interactive shell where other commands can be issued in order to
modify the plot (you may have to use ~a instead of ~s, depending on
your Lisp version).

### Function: gr2d (argument_1, ...)

Function `gr2d` builds an object describing a 2D scene. Arguments are
*graphic options*, *graphic objects*, or lists containing both graphic options and objects.
This scene is interpreted sequentially: *graphic options* affect those *graphic objects*
placed on its right. Some *graphic options* affect the global appearance of the scene.


This is the list of *graphic objects* available for scenes in two dimensions:
`bars`, `ellipse`, `explicit`, `image`, `implicit`, `label`,
`parametric`, `points`, `polar`, `polygon`, `quadrilateral`,
`rectangle`, `triangle`, `vector` and `geomap`
(this one defined in package `worldmap`).


See also `draw`
and `draw2d`.





















```maxima
(%i1) draw(
    gr2d(
        key="sin (x)",grid=[2,2],
        explicit(
            sin(x),
            x,0,2*%pi
        )
    ),
    gr2d(
        key="cos (x)",grid=[2,2],
        explicit(
            cos(x),
            x,0,2*%pi
        )
    )
 );
(%o1)           [gr2d(explicit), gr2d(explicit)]
```

(Figure draw_scene)

See also: `bars`, `ellipse`, `explicit`, `image`, `implicit`, `label`, `parametric`, `points`, `polar`, `polygon`, `quadrilateral`, `rectangle`, `triangle`, `vector`, `draw`, `draw2d`.

### Function: gr3d (argument_1, ...)

Function `gr3d` builds an object describing a 3d scene. Arguments are
*graphic options*, *graphic objects*, or lists containing both graphic options
and objects. This scene is interpreted sequentially: *graphic options* affect those 
*graphic objects* placed on its right. Some *graphic options* affect the global
appearance of the scene.


This is the list of *graphic objects* available for scenes in three
dimensions:

`cylindrical`, `elevation_grid`, `explicit`, `implicit`,
`label`, `mesh`, `parametric`,

`parametric_surface`, `points`, `quadrilateral`,
`spherical`, `triangle`, `tube`,

`vector`, and `geomap` (this one defined in package `worldmap`).


See also `draw` and `draw3d`.

See also: `cylindrical`, `elevation_grid`, `explicit`, `implicit`, `label`, `mesh`, `parametric`, `parametric_surface`, `points`, `quadrilateral`, `spherical`, `triangle`, `tube`, `vector`, `geomap`, `draw`, `draw3d`.

### Function: graph6_decode (str)

Returns the graph encoded in the graph6 format in the string *str*.

### Function: graph6_encode (gr)

Returns a string which encodes the graph *gr* in the graph6 format.

### Function: graph6_export (gr_list, fl)

Exports graphs in the list *gr_list* to the file *fl* in the
graph6 format.

### Function: graph6_import (fl)

Returns a list of graphs from the file *fl* in the graph6 format.

### Function: graph_center (gr)

Returns the center of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_center(g);
(%o3)                         [12]
```

### Function: graph_charpoly (gr, x)

Returns the characteristic polynomial (in variable *x*) of the graph
*gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_charpoly(p, x), factor;
                                   5        4
(%o3)               (x - 3) (x - 1)  (x + 2)
```

### Function: graph_eigenvalues (gr)

Returns the eigenvalues of the graph *gr*. The function returns
eigenvalues in the same format as maxima `eigenvalues` function.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_eigenvalues(p);
(%o3)               [[3, - 2, 1], [1, 4, 5]]
```

See also: `eigenvalues`.

### Function: graph_order (gr)

Returns the number of vertices in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_order(p);
(%o3)                          10
```

### Function: graph_periphery (gr)

Returns the periphery of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : grid_graph(5,5)$
(%i3) graph_periphery(g);
(%o3)                    [24, 20, 4, 0]
```

### Function: graph_product (g1, g1)

Returns the direct product of graphs *g1* and *g2*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) grid : graph_product(path_graph(3), path_graph(4))$
(%i3) draw_graph(grid)$
```


(Figure graphs01, Direct product of two graphs)

### Function: graph_size (gr)

Returns the number of edges in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) graph_size(p);
(%o3)                          15
```

### Function: graph_union (g1, g1)

Returns the union (sum) of graphs *g1* and *g2*.

### Function: great_rhombicosidodecahedron_graph ()

Returns the great rhombicosidodecahedron graph.

### Function: great_rhombicuboctahedron_graph ()

Returns the great rhombicuboctahedron graph.

### Variable: grid

Default value: `30`, `30`


Sets the number of grid points to use in the x- and y-directions for
three-dimensional plotting or for the `julia` and `mandelbrot`
programs.


For a way to actually draw a grid See `grid2d`.

See also: `julia`, `mandelbrot`, `grid2d`.

### Variable: grid2d

Default value: `false`


Shows a grid of lines on the xy plane. The points where the grid lines
are placed are the same points where tics are marked in the x and y
axes, which can be controlled with the `xtics` and `ytics`
options.  The single keywords `grid2d` and `nogrid2d` can be
used as synonyms for `[grid2d, true]` and `[grid2d, false]`.


See also `grid`.

See also: `xtics`, `ytics`, `grid`.

### Function: grid_graph (n, m)

Returns the *n x m* grid.

### Function: grotzch_graph ()

Returns the Grotzch graph.

### Function: hamilton_cycle (gr)

Returns the Hamilton cycle of the graph *gr* or an empty list if
*gr* is not hamiltonian.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) c : cube_graph(3)$
(%i3) hc : hamilton_cycle(c);
(%o3)              [7, 3, 2, 6, 4, 0, 1, 5, 7]
(%i4) draw_graph(c, show_edges=vertices_to_cycle(hc))$
```


(Figure graphs03, Hamilton cycle of a cubic graph)

### Function: hamilton_path (gr)

Returns the Hamilton path of the graph *gr* or an empty list if
*gr* does not have a Hamilton path.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) hp : hamilton_path(p);
(%o3)            [0, 5, 7, 2, 1, 6, 8, 3, 4, 9]
(%i4) draw_graph(p, show_edges=vertices_to_path(hp))$
```


(Figure graphs04, Hamilton path of a Petersen graph)

### Variable: head_angle

Default value: 45


`head_angle` indicates the angle, in degrees, between the arrow heads and
the segment.


This option is relevant only for `vector` objects.


Example:



```maxima
(%i1) draw2d(xrange      = [0,10],
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

(Figure draw_head_angle)


See also `head_both`,  `head_length`,  and `head_005ftype`.

See also: `head_both`, `head_length`, `head_type`.

### Variable: head_both

Default value: `false`


If `head_both` is `true`, vectors are plotted with two arrow heads.
If `false`, only one arrow is plotted.


This option is relevant only for `vector` objects.


Example:



```maxima
(%i1) draw2d(xrange      = [0,8],
             yrange      = [0,8],
             head_length = 0.7,
             vector([1,1],[6,0]),
             head_both   = true,
             vector([1,7],[6,0]) )$
```

(Figure draw_head_both)


See also `head_length`,  `head_angle`,  and `head_005ftype`.

See also: `head_length`, `head_angle`, `head_type`.

### Variable: head_length

Default value: 2


`head_length` indicates, in *x*-axis units, the length of arrow heads.


This option is relevant only for `vector` objects.


Example:



```maxima
(%i1) draw2d(xrange      = [0,12],
             yrange      = [0,8],
             vector([0,1],[5,5]),
             head_length = 1,
             vector([2,1],[5,5]),
             head_length = 0.5,
             vector([4,1],[5,5]),
             head_length = 0.25,
             vector([6,1],[5,5]))$
```

(Figure draw_head_length)


See also `head_both`,  `head_angle`,  and `head_005ftype`.

See also: `head_both`, `head_angle`, `head_type`.

### Variable: head_type

Default value: `filled`


`head_type` is used to specify how arrow heads are plotted. Possible
values are: `filled` (closed and filled arrow heads), `empty`
(closed but not filled arrow heads), and `nofilled` (open arrow heads).


This option is relevant only for `vector` objects.


Example:



```maxima
(%i1) draw2d(xrange      = [0,12],
             yrange      = [0,10],
             head_length = 1,
             vector([0,1],[5,5]), /* default type */
             head_type = 'empty,
             vector([3,1],[5,5]),
             head_type = 'nofilled,
             vector([6,1],[5,5]))$
```

(Figure draw_head_type)


See also `head_both`,  `head_angle`,  and `head_005flength`.

See also: `head_both`, `head_angle`, `head_length`.

### Function: heawood_graph ()

Returns the Heawood graph.

### Function: histogram (histogram, list, histogram, list, option_1, option_2, ..., histogram, one_column_matrix, histogram, one_column_matrix, option_1, option_2, ..., histogram, one_row_matrix, histogram, one_row_matrix, option_1, option_2, ...)

Constructs and displays a histogram from a data sample.
Data must be stored as a list of numbers, or a matrix of one row or one column.


Optional arguments:



- *
`nclasses` (default, 10):
the number of classes (also called bins) in the histogram,
or a list of two numbers (the least and greatest values included in the histogram),
or a list of three numbers (the least and greatest values included in the histogram, and the number of classes),
or a set containing the endpoints of the class intervals,
or a symbol specifying the name of one of three algorithms to automatically determine the number of classes:
`fd` (Ref. [1]), `scott` (Ref. [2]), or `sturges` (Ref. [3]).

A class interval excludes its left endpoint and includes its right endpoint,
except for the first interval, which includes both the left and right endpoints.
It is assumed that class intervals are contiguous.
That is, the right endpoint of one interval is equal to the left endpoint of the next.
- *
`frequency` (default, `absolute`): indicates the scale of the vertical axis.
Possible values are:  `absolute` (heights of bars add up to number of data),
`relative` (heights of bars add up to 1),
`percent` (heights of bars add up to 100),
and `density` (total area of histogram is 1).
- *
`htics` (default, `auto`): format of tic marks on the horizontal axis.
Possible values are: `auto` (tics are placed automatically),
`endpoints` (tics are placed at the divisions between classes),
`intervals` (classes are labeled with the corresponding intervals),
or a list of labels, one for each class.
- *
All global `draw` options, except `xrange`, `yrange`, 
and `xtics`, which are internally assigned by `histogram`.
If you want to set your own values for these options, make use of 
`histogram_description`.
- *
The following local `Package-draw` options: `key`,
`fill_color`, `fill_density`, and `line_005fwidth`.
Note that the outlines of bars,
as well as the interior of bars when `fill_density` is nonzero,
are drawn with `fill_color`, not `color`.


`histogram` honors the global option `histogram_skyline`.
When `histogram_skyline` is `true`,
`histogram` and `histogram_description` construct "skyline" plots,
which shows the outline of the histogram bars,
instead of drawing all the vertical segments.
Otherwise (the default), histograms are displayed with bars showing vertical segments.


There is also a function `wxhistogram` for creating embedded
histograms in interfaces wxMaxima and iMaxima.


See also `continuous_freq`,
which, like `histogram`,
counts data in intervals,
but returns the counts instead of displaying a graphic representation.


See also `barsplot`.


Examples:


A simple histogram with eight classes:















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


Setting the limits of the histogram to -2 and 12, with 3 classes.
Also, we introduce predefined tics:














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


Bounds for varying class widths.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) histogram (s1, nclasses = {0,3,6,7,11})$
```


Freedman-Diaconis formula for the number of classes.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) histogram(s1, nclasses=fd) $
```


References:


[1] Freedman, D., and Diaconis, P. (1981) On the histogram as a density estimator: L_2 theory.
Zeitschrift fur Wahrscheinlichkeitstheorie und verwandte Gebiete 57, 453-476.


[2] Scott, D. W. (1979) On optimal and data-based histograms. Biometrika 66, 605-610.


[3] Sturges, H. A. (1926) The choice of a class interval. Journal of the American Statistical Association 21, 65-66.

See also: `Package-draw`, `key`, `fill_color`, `fill_density`, `line_width`, `continuous_freq`, `barsplot`.

### Function: histogram_description (...)

Creates a graphic object which represents a histogram.
Such an object is suitable for creating complex scenes together with other graphic objects,
to be displayed by `draw2d`.


`histogram_description` takes the same arguments
as the stand-alone function `histogram`.
See `histogram` for more information.


Example:


We make use of `histogram_description` for setting 
`xrange` and adding an explicit curve into the scene:



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

See also: `histogram`.

### Variable: histogram_skyline

Default value: `false`


When `histogram_skyline` is `true`,
`histogram` and `histogram_description` construct "skyline" plots,
which shows the outline of the histogram bars,
instead of drawing all the vertical segments.


The outline is drawn with the current `fill_color` (not the current `color`).
The interior of the histogram is filled with `fill_color`,
but only if `fill_density` is nonzero.


Otherwise, histograms are displayed with bars showing vertical segments.


Examples:


Construct a skyline histogram,
and an ordinary histogram for comparison,
on the same plot.



```maxima
(%i1) load ("descriptive") $
(%i2) L: read_list (file_search ("pidigits.data")) $
(%i3) histogram_skyline: true $
(%i4) skyline_hist: histogram_description (L) $
(%i5) histogram_skyline: false $
(%i6) ordinary_hist: histogram_description (L) $
(%i7) draw (gr2d (skyline_hist), gr2d (ordinary_hist)) $
```


Continuing the preceding example.
Set display options for `fill_color` and `fill_density`.



```maxima
(%i8) histogram_skyline: true $
(%i9) skyline_hist: histogram_description (L, fill_color = blue, fill_density = 0.2) $
(%i10) histogram_skyline: false $
(%i11) ordinary_hist: histogram_description (L, fill_color = blue, fill_density = 0.2) $
(%i12) draw (gr2d (skyline_hist), gr2d (ordinary_hist)) $
```

### Function: icosahedron_graph ()

Returns the icosahedron graph.

### Function: icosidodecahedron_graph ()

Returns the icosidodecahedron graph.

### Function: ifs (r1, ..., rm, A1, ..., Am, x1, y1, ..., xm, ym, x0, y0, n, options, ..., ;)

Implements the Iterated Function System method. This method is similar
to the method described in the function `chaosgame`. but instead of
shrinking the segment from the current point to the randomly chosen
point, the 2 components of that segment will be multiplied by the 2 by 2
matrix *Ai* that corresponds to the point chosen randomly.


The random choice of one of the *m* attractive points can be made
with a non-uniform probability distribution defined by the weights
*r1*,...,*rm*. Those weights are given in cumulative form; for
instance if there are 3 points with probabilities 0.2, 0.5 and 0.3, the
weights *r1*, *r2* and *r3* could be 2, 7 and 10. The
options are the same as for `plot2d`.


**Example**. Barnsley’s fern, obtained with 4 matrices and 4 points:



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


(Figure dynamics8)

See also: `chaosgame`, `plot2d`.

### Function: image (im, x0, y0, width, height)

Renders images in 2D.


**2D**


`image (im,x0,y0,width,height)` plots image *im* in the rectangular
region from vertex `(x0,y0)` to `(x0+width,y0+height)` on the real
plane. Argument *im* must be a matrix of real numbers, a matrix of
vectors of length three or a *picture* object.


If *im* is a matrix of real numbers or a *levels picture* object,
pixel values are interpreted according to graphic option `palette`,
which is a vector of length three with components 
ranging from -36 to +36; each value is an index for a formula mapping the levels
onto red, green and blue colors, respectively:


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
30: x/0.32-0.78125                  31: 2*x-0.84
32: 4x;1;-2x+1.84;x/0.08-11.5
33: |2*x - 0.5|    34: 2*x          35: 2*x - 0.5
36: 2*x - 1
```

negative numbers mean negative colour component.


`palette = gray` and `palette = color` are short cuts for
`palette = [3,3,3]` and `palette = [7,5,15]`, respectively.


If *im* is a matrix of vectors of length three or an *rgb picture* object,
they are interpreted as red, green and blue color components.


Examples:


If *im* is a matrix of real numbers, pixel values are interpreted according
to graphic option `palette`.


```maxima
(%i1) im: apply(
           'matrix,
            makelist(makelist(random(200),i,1,30),i,1,30))$
(%i2) /* palette = color, default */
      draw2d(image(im,0,0,30,30))$
```

(Figure draw_image)


```maxima
(%i3) draw2d(palette = gray, image(im,0,0,30,30))$
```

(Figure draw_image2)


```maxima
(%i4) draw2d(palette = [15,20,-4],
             colorbox=false,
             image(im,0,0,30,30))$
```

(Figure draw_image3)


See also `colorbox`.


If *im* is a matrix of vectors of length three, they are interpreted
as red, green and blue color components.


```maxima
(%i1) im: apply(
            'matrix,
             makelist(
               makelist([random(300),
                         random(300),
                         random(300)],i,1,30),i,1,30))$
(%i2) draw2d(image(im,0,0,30,30))$
```

(Figure draw_image4)


Package `draw` automatically loads package `picture`. In this
example, a level picture object is built by hand and then rendered.


```maxima
(%i1) im: make_level_picture([45,87,2,134,204,16],3,2);
(%o1)       picture(level, 3, 2, {Array:  #(45 87 2 134 204 16)})
(%i2) /* default color palette */
      draw2d(image(im,0,0,30,30))$
```

(Figure draw_image5)


```maxima
(%i3) /* gray palette */
      draw2d(palette = gray,
             image(im,0,0,30,30))$
```

(Figure draw_image6)


An xpm file is read and then rendered.


```maxima
(%i1) im: read_xpm("myfile.xpm")$
(%i2) draw2d(image(im,0,0,10,7))$
```


See also `make_level_picture`,  `make_rgb_picture` and `read_005fxpm`.


[http://www.telefonica.net/web2/biomates/maxima/gpdraw/image]()

contains more elaborated examples.

See also: `colorbox`, `make_level_picture`, `make_rgb_picture`, `read_xpm`.

### Function: implicit (implicit, fcn, x, xmin, xmax, y, ymin, ymax, implicit, fcn, x, xmin, xmax, y, ymin, ymax, z, zmin, zmax)

Draws implicit functions in 2D and 3D.


**2D**


`implicit(fcn,x,xmin,xmax,y,ymin,ymax)`
plots the implicit function defined by *fcn*, with variable *x* taking values
from *xmin* to *xmax*, and variable *y* taking values
from *ymin* to *ymax*.


This object is affected by the following *graphic options*: `ip_grid`, 
`ip_grid_in`, `line_width`, `line_type`, `key` and `color`.


Example:



```maxima
(%i1) draw2d(grid      = true,
             line_type = solid,
             key       = "y^2=x^3-2*x+1",
             implicit(y^2=x^3-2*x+1, x, -4,4, y, -4,4),
             line_type = dots,
             key       = "x^3+y^3 = 3*x*y^2-x-1",
             implicit(x^3+y^3 = 3*x*y^2-x-1, x,-4,4, y,-4,4),
             title     = "Two implicit functions" )$
```

(Figure draw_implicit)


**3D**


`implicit (fcn,x,xmin,xmax, y,ymin,ymax, z,zmin,zmax)`
plots the implicit surface defined by *fcn*, with variable *x* taking values
from *xmin* to *xmax*, variable *y* taking values
from *ymin* to *ymax* and variable *z* taking values
from *zmin* to *zmax*. This object implements the *marching cubes algorithm*.


This object is affected by the following *graphic options*: `x_voxel`, 
`y_voxel`, `z_voxel`, `line_width`, `line_type`, `key`,
`wired_surface`, `enhanced3d` and `color`.


Example:



```maxima
(%i1) draw3d(
        color=blue,
        implicit((x^2+y^2+z^2-1)*(x^2+(y-1.5)^2+z^2-0.5)=0.015,
                 x,-1,1,y,-1.2,2.3,z,-1,1),
        surface_hide=true);
```

(Figure draw_implicit2)

See also: `ip_grid`, `ip_grid_in`, `line_width`, `line_type`, `key`, `x_voxel`, `y_voxel`, `z_voxel`, `wired_surface`, `enhanced3d`.

### Function: in_neighbors (v, gr)

Returns the list of in-neighbors of the vertex *v* in the directed
graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) p : path_digraph(3)$
(%i3) in_neighbors(2, p);
(%o3)                          [1]
(%i4) out_neighbors(2, p);
(%o4)                          []
```

### Function: induced_subgraph (V, g)

Returns the graph induced on the subset *V* of vertices of the graph
*g*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) V : [0,1,2,3,4]$
(%i4) g : induced_subgraph(V, p)$
(%i5) print_graph(g)$
Graph on 5 vertices with 5 edges.
Adjacencies:
  4 :  3  0
  3 :  2  4
  2 :  1  3
  1 :  0  2
  0 :  1  4
```

### Variable: interpolate_color

Default value: `false`


This option is relevant only when `enhanced3d` is not `false`.


When `interpolate_color` is `false`, surfaces are colored with
homogeneous quadrangles. When `true`, color transitions are smoothed
by interpolation.


`interpolate_color` also accepts a list of two numbers, `[m,n]`.
For positive *m* and *n*, each quadrangle or triangle is interpolated
*m* times and *n* times in the respective direction. For negative
*m* and *n*, the interpolation frequency is chosen so that there will be at least
*|m|* and *|n|* points drawn; you can consider this as a special gridding function.
Zeros, i.e. `interpolate_color=[0,0]`, will automatically choose an
optimal number of interpolated surface points.


Also, `interpolate_color=true` is equivalent to `interpolate_color=[0,0]`.


Examples:


Color interpolation with explicit functions.



```maxima
(%i1) draw3d(
        enhanced3d   = sin(x*y),
        explicit(20*exp(-x^2-y^2)-10, x ,-3, 3, y, -3, 3)) $
```

(Figure draw_interpolate_color)


```maxima
(%i2) draw3d(
        interpolate_color = true,
        enhanced3d   = sin(x*y),
        explicit(20*exp(-x^2-y^2)-10, x ,-3, 3, y, -3, 3)) $
```

(Figure draw_interpolate_color2)


```maxima
(%i3) draw3d(
        interpolate_color = [-10,0],
        enhanced3d   = sin(x*y),
        explicit(20*exp(-x^2-y^2)-10, x ,-3, 3, y, -3, 3)) $
```

(Figure draw_interpolate_color3)


Color interpolation with the `mesh` graphic object.


Interpolating colors in parametric surfaces can give unexpected results.



```maxima
(%i1) draw3d( 
        enhanced3d = true,
        mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
             [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
             [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
```

(Figure draw_interpolate_color4)


```maxima
(%i2) draw3d( 
        enhanced3d        = true,
        interpolate_color = true,
        mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
             [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
             [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
```

(Figure draw_interpolate_color5)


```maxima
(%i3) draw3d( 
        enhanced3d        = true,
        interpolate_color = true,
        view=map,
        mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
             [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
             [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
```

(Figure draw_interpolate_color6)


See also `enhanced3d`.

See also: `enhanced3d`.

### Variable: ip_grid

Default value: `[50, 50]`


`ip_grid` sets the grid for the first sampling in implicit plots.


This option is relevant only for `implicit` objects.

### Variable: ip_grid_in

Default value: `[5, 5]`


`ip_grid_in` sets the grid for the second sampling in implicit plots.


This option is relevant only for `implicit` objects.

### Function: is_biconnected (gr)

Returns `true` if *gr* is 2-connected and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_biconnected(cycle_graph(5));
(%o2)                         true
(%i3) is_biconnected(path_graph(5));
(%o3)                         false
```

### Function: is_bipartite (gr)

Returns `true` if *gr* is bipartite (2-colorable) and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_bipartite(petersen_graph());
(%o2)                         false
(%i3) is_bipartite(heawood_graph());
(%o3)                         true
```

### Function: is_connected (gr)

Returns `true` if the graph *gr* is connected and `false` otherwise.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) is_connected(graph_union(cycle_graph(4), path_graph(3)));
(%o2)                         false
```

### Function: is_digraph (gr)

Returns `true` if *gr* is a directed graph and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_digraph(path_graph(5));
(%o2)                         false
(%i3) is_digraph(path_digraph(5));
(%o3)                         true
```

### Function: is_edge_in_graph (e, gr)

Returns `true` if *e* is an edge (arc) in the (directed) graph *g*
and `false` otherwise.


Example:










```maxima
(%i1) load ("graphs")$
(%i2) c4 : cycle_graph(4)$
(%i3) is_edge_in_graph([2,3], c4);
(%o3)                         true
(%i4) is_edge_in_graph([3,2], c4);
(%o4)                         true
(%i5) is_edge_in_graph([2,4], c4);
(%o5)                         false
(%i6) is_edge_in_graph([3,2], cycle_digraph(4));
(%o6)                         false
```

### Function: is_graph (gr)

Returns `true` if *gr* is a graph and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_graph(path_graph(5));
(%o2)                         true
(%i3) is_graph(path_digraph(5));
(%o3)                         false
```

### Function: is_graph_or_digraph (gr)

Returns `true` if *gr* is a graph or a directed graph and `false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_graph_or_digraph(path_graph(5));
(%o2)                         true
(%i3) is_graph_or_digraph(path_digraph(5));
(%o3)                         true
```

### Function: is_isomorphic (gr1, gr2)

Returns `true` if graphs/digraphs *gr1* and *gr2* are isomorphic
and `false` otherwise.


See also `isomorphism`.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) clk5:complement_graph(line_graph(complete_graph(5)))$
(%i3) is_isomorphic(clk5, petersen_graph());
(%o3)                         true
```

See also: `isomorphism`.

### Function: is_planar (gr)

Returns `true` if *gr* is a planar graph and `false` otherwise.


The algorithm used is the Demoucron’s algorithm, which is a quadratic time
algorithm.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) is_planar(dodecahedron_graph());
(%o2)                         true
(%i3) is_planar(petersen_graph());
(%o3)                         false
(%i4) is_planar(petersen_graph(10,2));
(%o4)                         true
```

### Function: is_sconnected (gr)

Returns `true` if the directed graph *gr* is strongly connected and
`false` otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_sconnected(cycle_digraph(5));
(%o2)                         true
(%i3) is_sconnected(path_digraph(5));
(%o3)                         false
```

### Function: is_tree (gr)

Returns `true` if *gr* is a tree and `false`  otherwise.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) is_tree(random_tree(4));
(%o2)                         true
(%i3) is_tree(graph_union(random_tree(4), random_tree(5)));
(%o3)                         false
```

### Function: is_vertex_in_graph (v, gr)

Returns `true` if *v* is a vertex in the graph *g* and `false`  otherwise.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) c4 : cycle_graph(4)$
(%i3) is_vertex_in_graph(0, c4);
(%o3)                         true
(%i4) is_vertex_in_graph(6, c4);
(%o4)                         false
```

### Function: isomorphism (gr1, gr2)

Returns a an isomorphism between graphs/digraphs *gr1* and
*gr2*. If *gr1* and *gr2* are not isomorphic, it returns
an empty list.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) clk5:complement_graph(line_graph(complete_graph(5)))$
(%i3) isomorphism(clk5, petersen_graph());
(%o3) [9 -> 0, 2 -> 1, 6 -> 2, 5 -> 3, 0 -> 4, 1 -> 5, 3 -> 6, 
                                          4 -> 7, 7 -> 8, 8 -> 9]
```

### Variable: iterations

Default value: `9`


Number of iterations made by the programs mandelbrot and julia.

### Function: julia (x, y, ..., options, ...)

Creates a graphic representation of the Julia set for the complex number
(*x* + i *y*). The two mandatory parameters *x* and *y*
must be real. This program is part of the additional package
`dynamics`, but that package does not have to be loaded; the first
time julia is used, it will be loaded automatically.


Each pixel in the grid is given a color corresponding to the number of
iterations it takes the sequence that starts at that point to move out
of the convergence circle of radius 2 centered at the origin. The number
of pixels in the grid is controlled by the `grid` plot option
(default 30 by 30). The maximum number of iterations is set with the
option `iterations`. The program sets its own default palette:
magenta, violet, blue, cyan, green, yellow, orange, red, brown and black,
but it can be changed by adding an explicit `palette` option in the
command.


The default domain used goes from -2 to 2 in both axes and can be
changed with the `x` and `y` options. By default, the two axes
are shown with the same scale, unless the option `yx_ratio` is used
or the option `same_xy` is disabled. Other general plot options are
also accepted.


The following example shows a region of the Julia set for the number
-0.55 + i0.6. The option `color_bar_tics` is used to prevent
Gnuplot from adjusting the color box up to 40, in which case the points
corresponding the maximum 36 iterations would not be black.






Warning: line 394 - example input lines must begin with ’


```maxima
maxima

(%i1) julia (-0.55, 0.6, [iterations, 36], [x, -0.3, 0.2],
  [y, 0.3, 0.9], [grid, 400, 400], [color_bar_tics, 0, 6, 36])$
```


(Figure plotting4)

See also: `grid`, `iterations`, `palette`, `yx_ratio`, `same_xy`, `color_bar_tics`.

### Variable: key

Default value: `""` (empty string)


`key` is the name of a function in the legend. If `key` is an
empty string, no key is assigned to the function.


This option affects the following graphic objects:


- *
`gr2d`: `points`, `polygon`, `rectangle`,
`ellipse`, `vector`, `explicit`, `implicit`,
`parametric` and `polar`.
- *
`gr3d`: `points`, `explicit`, `parametric`
and `parametric_005fsurface`.


Example:



```maxima
(%i1) draw2d(key   = "Sinus",
             explicit(sin(x),x,0,10),
             key   = "Cosinus",
             color = red,
             explicit(cos(x),x,0,10) )$
```

(Figure draw_key)

See also: `points`, `polygon`, `rectangle`, `ellipse`, `vector`, `explicit`, `implicit`, `parametric`, `polar`, `parametric_surface`.

### Variable: key_pos

Default value: `""` (empty string)


`key_pos` defines at which position the legend will be drawn. If `key` is an
empty string, `"top_right"` is used.
Available position specifiers are: `top_left`, `top_center`, `top_right`,
`center_left`, `center`, `center_right`,
`bottom_left`, `bottom_center`, and `bottom_right`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(
        key_pos = top_left,
        key   = "x",
        explicit(x,  x,0,10),
        color= red,
        key   = "x squared",
        explicit(x^2,x,0,10))$
(%i3) draw3d(
        key_pos = center,
        key   = "x",
        explicit(x+y,x,0,10,y,0,10),
        color= red,
        key   = "x squared",
        explicit(x^2+y^2,x,0,10,y,0,10))$
```

(Figure draw_key_pos)

### Variable: label

Writes one or several labels in the points with *x*, *y*
coordinates indicated after each label.

### Variable: label_alignment

Default value: `center`


`label_alignment` is used to specify where to write labels with
respect to the given coordinates. Possible values are: `center`,
`left`, and `right`.


This option is relevant only for `label` objects.


Example:



```maxima
(%i1) draw2d(xrange          = [0,10],
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

(Figure draw_label_alignment)


See also `label_orientation`,  and `color`

See also: `label_orientation`.

### Variable: label_orientation

Default value: `horizontal`


`label_orientation` is used to specify orientation of labels.
Possible values are: `horizontal`, and `vertical`.


This option is relevant only for `label` objects.


Example:


In this example, a dummy point is added to get an image.
Package `draw` needs always data to draw an scene.


```maxima
(%i1) draw2d(xrange     = [0,10],
             yrange     = [0,10],
             point_size = 0,
             points([[5,5]]),
             color      = navy,
             label(["Horizontal orientation (default)",5,2]),
             label_orientation = 'vertical,
             color             = "#654321",
             label(["Vertical orientation",1,5]))$
```

(Figure draw_label_orientation)


See also `label_alignment` and `color`

See also: `label_alignment`.

### Function: laplacian_matrix (gr)

Returns the laplacian matrix of the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) laplacian_matrix(cycle_graph(5));
                   [  2   - 1   0    0   - 1 ]
                   [                         ]
                   [ - 1   2   - 1   0    0  ]
                   [                         ]
(%o2)              [  0   - 1   2   - 1   0  ]
                   [                         ]
                   [  0    0   - 1   2   - 1 ]
                   [                         ]
                   [ - 1   0    0   - 1   2  ]
```

### Variable: legend

It specifies the labels for the plots when various plots are shown.  If
there are more plots than the number of labels given, they will be
repeated.  If given the value `false`, no legends will be shown.
By default, the names of the expressions or functions will be used, or
the words discrete1, discrete2, ..., for discrete sets of points.
The single keyword `legend` removes any previously defined legends,
leaving it to the plotting program to set up a legend. The keyword
`nolegend` is a synonym for `[legend, false]`.

### Variable: levels

This option is used by `plot2d` to do contour plots. If only one
number is given after the keyword `levels`, it must be a natural
number; `plot2d` will try to plot that number of contours with
values between the minimum and maximum value of the expression given,
with the form d*10^n, where d is either 1, 2 or 5. Since not always it will
be possible to find that number of levels in that interval, the number of
contour lines show will be smaller than the number specified by this
option.


If more than one number are given after the keyword `levels`,
`plot2d`. will show the contour lines corresponding to those
values of the expression plotted, if they exist within the domain used.

See also: `plot2d`.

### Function: line_graph (g)

Returns the line graph of the graph *g*.

### Variable: line_type

Default value: `solid`


`line_type` indicates how lines are displayed; possible values are
`solid` and `dots`, both available in all terminals, and
`dashes`, `short_dashes`, `short_long_dashes`, `short_short_long_dashes`, 
and `dot_dash`, which are not available in `png`, `jpg`, and `gif` terminals. 


This option affects the following graphic objects:


- *
`gr2d`: `points`, `polygon`, `rectangle`,
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` and `polar`.
- *
`gr3d`: `points`, `explicit`, `parametric` and `parametric_005fsurface`.


Example:



```maxima
(%i1) draw2d(line_type = dots,
             explicit(1 + x^2,x,-1,1),
             line_type = solid, /* default */
             explicit(2 + x^2,x,-1,1))$
```

(Figure draw_line_type)


See also `line_005fwidth`.

See also: `points`, `polygon`, `rectangle`, `ellipse`, `vector`, `explicit`, `implicit`, `parametric`, `polar`, `parametric_surface`, `line_width`.

### Variable: line_width

Default value: 1


`line_width` is the width of plotted lines.
Its value must be a positive number.


This option affects the following graphic objects:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` and `polar`.
- *
`gr3d`: `points` and `parametric`.


Example:



```maxima
(%i1) draw2d(explicit(x^2,x,-1,1), /* default width */
             line_width = 5.5,
             explicit(1 + x^2,x,-1,1),
             line_width = 10,
             explicit(2 + x^2,x,-1,1))$
```

(Figure draw_line_width)


See also `line_005ftype`.

See also: `points`, `polygon`, `rectangle`, `ellipse`, `vector`, `explicit`, `implicit`, `parametric`, `polar`, `line_type`.

### Variable: logcb

Default value: `false`


If `logcb` is `true`, the tics in the colorbox will be drawn in the
logarithmic scale.


When `enhanced3d` or `colorbox` is `false`, option `logcb` has
no effect.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d (
        enhanced3d = true,
        color      = green,
        logcb = true,
        logz  = true,
        palette = [-15,24,-9],
        explicit(exp(x^2-y^2), x,-2,2,y,-2,2)) $
```

(Figure draw_logcb)


See also `enhanced3d`,  `colorbox` and `cbrange`.

See also: `logcb`, `enhanced3d`, `colorbox`, `cbrange`.

### Variable: logx

Default value: `false`


Makes the horizontal axes to be scaled logarithmically. It can be either
true or false. The single keywords `logx` and `nologx` can be
used as synonyms for `[logx, true]` and `[logx, false]`.

### Variable: logx_secondary

Default value: `false`


If `logx_secondary` is `true`, the secondary *x* axis 
will be drawn in the logarithmic scale.


This option is relevant only for 2d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(
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

(Figure draw_logx_secondary)


See also `logx_draw`,  `logy_draw`,  `logy_secondary`,  and `logz`.

See also: `logx_draw`, `logy_draw`, `logy_secondary`, `logz`.

### Variable: logy

Default value: `false`


Makes the vertical axes to be scaled logarithmically. It can be either
true or false.
The single keywords `logy` and `nology` can be used as
synonyms for `[logy, true]` and `[logy, false]`.

### Variable: logy_secondary

Default value: `false`


If `logy_secondary` is `true`, the secondary *y* axis 
will be drawn in the logarithmic scale.


This option is relevant only for 2d scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(
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


See also `logx_draw`,  `logy_draw`,  `logx_secondary`,  and `logz`.

See also: `logx_draw`, `logy_draw`, `logx_secondary`, `logz`.

### Variable: logz

Default value: `false`


If `logz` is `true`, the *z* axis will be drawn in the
logarithmic scale.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(logz = true,
             explicit(exp(u^2+v^2),u,-2,2,v,-2,2))$
```


See also `logx_draw` and `logy_005fdraw`.

See also: `logx_draw`, `logy_draw`.

### Function: make_graph (make_graph, vrt, f, make_graph, vrt, f, oriented)

Creates a graph using a predicate function *f*.


*vrt* is a list or set of vertices, or an integer.


When *vrt* is a list or set,
its elements may be any integers,
and, if a list, may be listed in any order.


When *vrt* is an integer,
vertices of the graph will be integers from 1 to *vrt*.


*f* is a predicate function. Two vertices *a* and *b* will
be connected if `f(a,b)=true`.


If *directed* is not *false*, then the graph will be directed.


Example 1:








```maxima
(%i1) load("graphs")$
(%i2) g : make_graph(powerset({1,2,3,4,5}, 2), disjointp)$
(%i3) is_isomorphic(g, petersen_graph());
(%o3)                         true
(%i4) get_vertex_label(1, g);
(%o4)                        {1, 2}
```


Example 2:









```maxima
(%i1) load("graphs")$
(%i2) f(i, j) := is (mod(j, i)=0)$
(%i3) g : make_graph(20, f, directed=true)$
(%i4) out_neighbors(4, g);
(%o4)                    [8, 12, 16, 20]
(%i5) in_neighbors(18, g);
(%o5)                    [1, 2, 3, 6, 9]
```

### Function: make_level_picture (make_level_picture, data, make_level_picture, data, width, height)

Returns a levels *picture* object. `make_level_picture (data)`
builds the *picture* object from matrix *data*.
`make_level_picture (data,width,height)`
builds the object from a list of numbers; in this case, both the
*width* and the *height* must be given.


The returned *picture* object contains the following 
four parts:



1. symbol `level`
2. image width
3. image height
4. an integer array with pixel data ranging from 0 to 255.
Argument *data* must contain only numbers ranged from 0 to 255;
negative numbers are substituted by 0, and those which are
greater than 255 are set to 255.


Example:


Level picture from matrix.


```maxima
(%i1) make_level_picture(matrix([3,2,5],[7,-9,3000]));
(%o1)         picture(level, 3, 2, {Array:  #(3 2 5 7 0 255)})
```


Level picture from numeric list.


```maxima
(%i1) make_level_picture([-2,0,54,%pi],2,2);
(%o1)            picture(level, 2, 2, {Array:  #(0 0 54 3)})
```

### Function: make_poly_continent (make_poly_continent, continent_name, make_poly_continent, country_list)

Makes the necessary polygons to draw a colored continent
or a list of countries.


Example:



```maxima
(%i1) load("worldmap")$
(%i2) /* A continent */
      make_poly_continent(Africa)$
(%i3) apply(draw2d, %)$
```

(Figure worldmap_make_poly_continent)


```maxima
(%i4) /* A list of countries */
      make_poly_continent([Germany,Denmark,Poland])$
(%i5) apply(draw2d, %)$
```

(Figure worldmap_make_poly_continent2)

### Function: make_poly_country (country_name)

Makes the necessary polygons to draw a colored country.
If islands exist, one country can be defined with more than
just one polygon.


Example:



```maxima
(%i1) load("worldmap")$
(%i2) make_poly_country(India)$
(%i3) apply(draw2d, %)$
```

(Figure worldmap_make_poly_country)

### Function: make_polygon (nlist)

Returns a `polygon` object from boundary indices. Argument
*nlist* is a list of components of `boundaries_array`.


Example:


Bhutan is defined by boundary numbers 171, 173
and 1143, so that `make_polygon([171,173,1143])`
appends arrays of coordinates `boundaries_array[171]`,
`boundaries_array[173]` and `boundaries_array[1143]` and 
returns a `polygon` object suited to be plotted by 
`draw`. To avoid an error message, arrays must be
compatible in the sense that any two consecutive
arrays have two coordinates in the extremes in common. In this
example, the two first components of `boundaries_array[171]` are
equal to the last two coordinates of `boundaries_array[173]`, and 
the two first of `boundaries_array[173]` are equal to the two first
of `boundaries_array[1143]`; in conclusion, boundary numbers
171, 173 and 1143 (in this order) are compatible and the colored 
polygon can be drawn.


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

(Figure worldmap_make_polygon)

### Function: make_rgb_picture (redlevel, greenlevel, bluelevel)

Returns an rgb-coloured *picture* object. All three arguments must
be levels picture; with red, green and blue levels.


The returned *picture* object contains the following 
four parts:



1. symbol `rgb`
2. image width
3. image height
4. an integer array of length *3*width*height* with pixel data ranging
from 0 to 255. Each pixel is represented by three consecutive numbers
(red, green, blue).


Example:



```maxima
(%i1) red: make_level_picture(matrix([3,2],[7,260]));
(%o1)           picture(level, 2, 2, {Array:  #(3 2 7 255)})
(%i2) green: make_level_picture(matrix([54,23],[73,-9]));
(%o2)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
(%i3) blue: make_level_picture(matrix([123,82],[45,32.5698]));
(%o3)          picture(level, 2, 2, {Array:  #(123 82 45 33)})
(%i4) make_rgb_picture(red,green,blue);
(%o4) picture(rgb, 2, 2, 
              {Array:  #(3 54 123 2 23 82 7 73 45 255 0 33)})
```

### Function: make_transform (var1, var2, var3, fx, fy, fz)

Returns a function suitable to be used in the option `transform_xy`
of plot3d.  The three variables *var1*, *var2*, *var3* are
three dummy variable names, which represent the 3 variables given by the
plot3d command (first the two independent variables and then the
function that depends on those two variables).  The three functions
*fx*, *fy*, *fz* must depend only on those 3 variables, and
will give the corresponding x, y and z coordinates that should be
plotted.  There are two transformations defined by default:
`polar_to_xy` and `spherical_005fto_005fxyz`. See the documentation
for those two transformations.

See also: `transform_xy`, `polar_to_xy`, `spherical_to_xyz`.

### Function: mandelbrot (options)

Creates a graphic representation of the Mandelbrot set. This program is
part of the additional package `dynamics`, but that package does
not have to be loaded; the first time mandelbrot is used, the package
will be loaded automatically.


This program can be called without any arguments, in which case it will
use a default value of 9 iterations per point, a grid with dimensions
set by the `grid` plot option (default 30 by 30) and a region
that extends from -2 to 2 in both axes. The options are all the same
that plot2d accepts, plus an option `iterations` to change the
number of iterations.


Each pixel in the grid is given a color corresponding to the number of
iterations it takes the sequence starting at zero to move out
of the convergence circle of radius 2, centered at the origin. The
maximum number of iterations is set by the option `iterations`.
The program uses its own default palette: magenta,violet, blue, cyan,
green, yellow, orange, red, brown and black, but it can be changed by
adding an explicit `palette` option in the command. By default, the
two axes are shown with the same scale, unless the option `yx_ratio`
is used or the option `same_xy` is disabled.


Example:





incorrect syntax: end of file while scanning expression.


 

^


```maxima
maxima
(%i1) mandelbrot ([iterations,30], [x,-2,1], [y,-1.2,1.2], [grid,400,400])$
```


(Figure plotting5)

See also: `grid`, `iterations`, `palette`, `yx_ratio`, `same_xy`.

### Function: max_clique (gr)

Returns a maximum clique of the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.5)$
(%i3) max_clique(g);
(%o3)          [6, 12, 31, 36, 52, 59, 62, 63, 80]
```

### Function: max_degree (gr)

Returns the maximal degree of vertices of the graph *gr* and a
vertex of maximal degree.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.02)$
(%i3) max_degree(g);
(%o3)                        [6, 79]
(%i4) vertex_degree(95, g);
(%o4)                           2
```

### Function: max_flow (net, s, t)

Returns a maximum flow through the network *net* with the source
*s* and the sink *t*.


The function returns the value of the maximal flow and a list
representing the weights of the arcs in the optimal flow.


Example:





















```maxima
(%i1) load ("graphs")$
(%i2) net : create_graph(
  [1,2,3,4,5,6],
  [[[1,2], 1.0],
   [[1,3], 0.3],
   [[2,4], 0.2],
   [[2,5], 0.3],
   [[3,4], 0.1],
   [[3,5], 0.1],
   [[4,6], 1.0],
   [[5,6], 1.0]],
  directed=true)$
(%i3) [flow_value, flow] : max_flow(net, 1, 6);
(%o3) [0.7, [[[1, 2], 0.5], [[1, 3], 0.2], [[2, 4], 0.2], 
[[2, 5], 0.3], [[3, 4], 0.1], [[3, 5], 0.1], [[4, 6], 0.3], 
[[5, 6], 0.4]]]
(%i4) fl : 0$
(%i5) for u in out_neighbors(1, net)
     do fl : fl + assoc([1, u], flow)$
(%i6) fl;
(%o6)                          0.7
```

### Function: max_independent_set (gr)

Returns a maximum independent set of the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) mi : max_independent_set(d);
(%o3)             [0, 3, 5, 9, 10, 11, 18, 19]
(%i4) draw_graph(d, show_vertices=mi)$
```


(Figure graphs05, Maximum independent set of a dodecahedral graph)

### Function: max_matching (gr)

Returns a maximum matching of the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) m : max_matching(d);
(%o3) [[5, 7], [8, 9], [6, 10], [14, 19], [13, 18], [12, 17], 
                               [11, 16], [0, 15], [3, 4], [1, 2]]
(%i4) draw_graph(d, show_edges=m)$
```


(Figure graphs06, Maximum matching of a dodecahedral graph)

### Function: md5sum (md5sum, arg, md5sum, arg, return-type)

Returns the `MD5` checksum of a string, non-negative integer,
list of octets, or binary (not character) input stream.
A file for which an input stream is opened may be an ordinary text file;
it is the stream which needs to be binary, not the file itself.


When the argument is an input stream,
`md5sum` reads the entire content of the stream,
but does not close the stream.


The default return value is a string containing 32 hex characters.
The optional argument *return-type* allows `md5sum` to alternatively 
return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Note that in case *arg* contains German umlauts or other non-ASCII 
characters (resp. octets larger than 127) the `MD5` checksum is platform dependent.


Examples:



```maxima
(%i1) ibase: obase: 16.$
(%i2) msg: "foo bar baz"$
(%i3) string: md5sum(msg);
(%o3)                  ab07acbb1e496801937adfa772424bf7
(%i4) integer: md5sum(msg, 'number);
(%o4)                 0ab07acbb1e496801937adfa772424bf7
(%i5) octets: md5sum(msg, 'list);
(%o5)        [0AB,7,0AC,0BB,1E,49,68,1,93,7A,0DF,0A7,72,42,4B,0F7]
(%i6) sdowncase( printf(false, "~{~2,'0x~^:~}", octets) );
(%o6)           ab:07:ac:bb:1e:49:68:01:93:7a:df:a7:72:42:4b:f7
```


The argument may be a binary input stream.



```maxima
(%i1) S: openr_binary (file_search ("md5.lisp"));
(%o1) #<INPUT BUFFERED FILE-STREAM (UNSIGNED-BYTE 8)
  /home/robert/maxima/maxima-code/share/stringproc/md5.lisp>
(%i2) md5sum (S);
(%o2)           31a512ed53daf5b99495c9d05559355f
(%i3) close (S);
(%o3)                         true
```

### Function: mesh (row_1, row_2, ...)

Draws a quadrangular mesh in 3D.


**3D**


Argument *row_i* is a list of *n* 3D points of the form
`[[x_i1,y_i1,z_i1], ...,[x_in,y_in,z_in]]`, and all rows are
of equal length. All these points define an arbitrary surface in 3D and
in some sense it’s a generalization of the `elevation_grid` object.


This object is affected by the following *graphic options*: `line_type`, 
`line_width`, `color`, `key`, `wired_surface`, `enhanced3d` and `transform`.


Examples:


A simple example.



```maxima
(%i1) draw3d( 
         mesh([[1,1,3],   [7,3,1],[12,-2,4],[15,0,5]],
              [[2,7,8],   [4,3,1],[10,5,8], [12,7,1]],
              [[-2,11,10],[6,9,5],[6,15,1], [20,15,2]])) $
```

(Figure draw_mesh)


Plotting a triangle in 3D.



```maxima
(%i1) draw3d(
        line_width = 2,
        mesh([[1,0,0],[0,1,0]],
             [[0,0,1],[0,0,1]])) $
```

(Figure draw_mesh2)


Two quadrilaterals.



```maxima
(%i1) draw3d(
        surface_hide = true,
        line_width   = 3,
        color = red,
        mesh([[0,0,0], [0,1,0]],
             [[2,0,2], [2,2,2]]),
        color = blue,
        mesh([[0,0,2], [0,1,2]],
             [[2,0,4], [2,2,4]])) $
```

(Figure draw_mesh3)

See also: `line_type`, `line_width`, `color`, `key`, `wired_surface`, `enhanced3d`, `transform`.

### Variable: mesh_lines_color

Default value: `black`


It sets the color used by plot3d to draw the mesh lines, when a palette
is being used.  It accepts the same colors as for the option
`color` (see the list of allowed colors in `color`).  It
can also be given a value `false` to eliminate completely the mesh
lines. The single keyword `mesh_lines_color` removes any previously
defined colors, leaving it to the graphic program to decide what color
to use. The keyword `nomesh_lines` is a synonym for
`[mesh_lines_color, false]`

See also: `color`.

### Function: mgf1_sha1 (mgf1_sha1, seed, len, mgf1_sha1, seed, len, return-type)

Returns a pseudo random number of variable length. 
By default the returned value is a number with a length of *len* octets.


The optional argument *return-type* allows `mgf1_sha1` to alternatively 
return the corresponding list of *len* octets.
*return-type* may be `number` or `list`.


The computation of the returned value is described in `RFC 3447`, 
appendix `B.2.1 MGF1`. 
`SHA1` is used as hash function, i.e. the randomness of the computed number
relies on the randomness of `SHA1` hashes.


Example:



```maxima
(%i1) ibase: obase: 16.$
(%i2) number: mgf1_sha1(4711., 8);
(%o2)                        0e0252e5a2a42fea1
(%i3) octets: mgf1_sha1(4711., 8, 'list);
(%o3)                  [0E0,25,2E,5A,2A,42,0FE,0A1]
```

### Function: min_degree (gr)

Returns the minimum degree of vertices of the graph *gr* and a
vertex of minimum degree.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : random_graph(100, 0.1)$
(%i3) min_degree(g);
(%o3)                        [3, 49]
(%i4) vertex_degree(21, g);
(%o4)                           9
```

### Function: min_edge_cut (gr)

Returns the minimum edge cut in the graph *gr*.


See also `edge_005fconnectivity`.

See also: `edge_connectivity`.

### Function: min_vertex_cover (gr)

Returns the minimum vertex cover of the graph *gr*.

### Function: min_vertex_cut (gr)

Returns the minimum vertex cut in the graph *gr*.


See also `vertex_005fconnectivity`.

See also: `vertex_connectivity`.

### Function: minimum_spanning_tree (gr)

Returns the minimum spanning tree of the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(path_graph(10), path_graph(10))$
(%i3) t : minimum_spanning_tree(g)$
(%i4) draw_graph(g, show_edges=edges(t))$
```


(Figure graphs07, Minimum spanning of rectangular graph)

### Function: multiplot_mode (term)

This function enables Maxima to work in one-window multiplot mode with terminal
*term*; accepted arguments for this function are `screen`, 
`wxt`, `aquaterm`, `windows` and `none`.


When multiplot mode is enabled, each call to `draw` sends a new plot to the
same window, without erasing the previous ones. To disable the multiplot mode,
write `multiplot_mode(none)`.


When multiplot mode is enabled, global option `terminal` is blocked and you
have to disable this working mode before changing to another terminal.


On Windows this feature requires Gnuplot 5.0 or newer.
Note, that just plotting multiple expressions into the same plot doesn’t require
multiplot: It can be done by just issuing multiple `explicit` or similar
commands in a row.


Example:



```maxima
(%i1) set_draw_defaults(
         xrange = [-1,1],
         yrange = [-1,1],
         grid   = true,
         title  = "Step by step plot" )$
(%i2) multiplot_mode(screen)$
(%i3) draw2d(color=blue,  explicit(x^2,x,-1,1))$
(%i4) draw2d(color=red,   explicit(x^3,x,-1,1))$
(%i5) draw2d(color=brown, explicit(x^4,x,-1,1))$
(%i6) multiplot_mode(none)$
```

(Figure draw_multiplot)

See also: `explicit`.

### Function: mycielski_graph (g)

Returns the mycielskian graph of the graph *g*.

### Function: negative_picture (pic)

Returns the negative of a (*level* or *rgb*) picture.

### Function: neighbors (v, gr)

Returns the list of neighbors of the vertex *v* in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p : petersen_graph()$
(%i3) neighbors(3, p);
(%o3)                       [4, 8, 2]
```

### Function: new_graph ()

Returns the graph with no vertices and no edges.

### Variable: nticks

Default value: `29`


When plotting functions with `plot2d`, it is gives the initial
number of points used by the adaptive plotting routine for plotting
functions. When plotting parametric functions with `plot3d`,
it sets the number of points that will be shown for the plot.

See also: `plot2d`, `plot3d`.

### Function: number_to_octets (number)

Returns an octet-representation of *number* as a list of octets.
The *number* must be a non-negative integer.


Example:



```maxima
(%i1) ibase : obase : 16.$
(%i2) octets: [0ca,0fe,0ba,0be]$
(%i3) number: octets_to_number(octets);
(%o3)                            0cafebabe
(%i4) number_to_octets(number);
(%o4)                      [0CA, 0FE, 0BA, 0BE]
```

### Function: numbered_boundaries (nlist)

Draws a list of polygonal segments (boundaries), labeled by
its numbers (`boundaries_array` coordinates). This is of great
help when building new geographical entities.


Example:


Map of Europe labeling borders with their component number in
`boundaries_array`.


```maxima
(%i1) load("worldmap")$
(%i2) european_borders: 
           region_boundaries(-31.81,74.92,49.84,32.06)$
(%i3) numbered_boundaries(european_borders)$
```

### Function: octets_to_number (octets)

Returns a number by concatenating the octets in the list of *octets*.


Example: See `number_005fto_005foctets`.

See also: `number_to_octets`.

### Function: octets_to_oid (octets)

Computes an object identifier (OID) from the list of *octets*.


Example: RSA encryption OID



```maxima
(%i1) ibase : obase : 16.$
(%i2) oid: octets_to_oid([2A,86,48,86,0F7,0D,1,1,1]);
(%o2)                      1.2.840.113549.1.1.1
(%i3) oid_to_octets(oid);
(%o3)               [2A, 86, 48, 86, 0F7, 0D, 1, 1, 1]
```

### Function: octets_to_string (octets_to_string, octets, octets_to_string, octets, encoding)

Decodes the list of *octets* into a string according to current system defaults. 
When decoding octets corresponding to Non-US-ASCII characters 
the result depends on the platform, application and underlying Lisp.


Example: Using system defaults 
(Maxima compiled with GCL, which uses no format definition and 
simply passes through the UTF-8-octets encoded by the GNU/Linux terminal).



```maxima
(%i1) octets: string_to_octets("abc");
(%o1)                            [61, 62, 63]
(%i2) octets_to_string(octets);
(%o2)                                 abc
(%i3) ibase: obase: 16.$
(%i4) unicode(20AC);
(%o4)                                  EUR
(%i5) octets: string_to_octets(%);
(%o5)                           [0E2, 82, 0AC]
(%i6) octets_to_string(octets);
(%o6)                                  EUR
(%i7) utf8_to_unicode(octets);
(%o7)                                20AC
```


In case the external format of the Lisp reader is equal to UTF-8 the optional 
argument *encoding* allows to set the encoding for the octet to string conversion. 
If necessary see `adjust_005fexternal_005fformat` for changing the external format. 


Some names of supported encodings (see corresponding Lisp manual for more): 

CCL, CLISP, SBCL: `utf-8, ucs-2be, ucs-4be, iso-8859-1, cp1252, cp850` 

CMUCL: `utf-8, utf-16-be, utf-32-be, iso8859-1, cp1252` 

ECL: `utf-8, ucs-2be, ucs-4be, iso-8859-1, windows-cp1252, dos-cp850` 

   

Example (continued): Using the optional encoding argument 
(Maxima compiled with SBCL, GNU/Linux terminal).



```maxima
(%i8) string_to_octets("EUR", "ucs-2be");
(%o8)                              [20, 0AC]
```

See also: `adjust_external_format`.

### Function: odd_girth (gr)

Returns the length of the shortest odd cycle in the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) g : graph_product(cycle_graph(4), cycle_graph(7))$
(%i3) girth(g);
(%o3)                           4
(%i4) odd_girth(g);
(%o4)                           7
```

### Function: oid_to_octets (oid-string)

Converts an object identifier (OID) to a list of *octets*.


Example: See `octets_005fto_005foid`.

See also: `octets_to_oid`.

### Function: orbits (F, y0, n1, n2, x, x0, xf, xstep, options, ..., ;)

Draws the orbits diagram for a family of one-dimensional
discrete dynamical systems, with one parameter *x*; that kind of
diagram is used to study the bifurcations of an one-dimensional discrete
system.


The function *F(y)* defines a sequence with a starting value of
*y0*, as in the case of the function `evolution`, but in this
case that function will also depend on a parameter *x* that will
take values in the interval from *x0* to *xf* with increments of
*xstep*. Each value used for the parameter *x* is shown on the
horizontal axis. The vertical axis will show the *n2* values
of the sequence *y(n1+1)*,..., *y(n1+n2+1)* obtained after letting
the sequence evolve *n1* iterations.  In addition to the options
accepted by `plot2d`, it accepts an option *pixels* that
sets up the maximum number of different points that will be represented
in the vertical direction.


**Example**. Orbits diagram of the quadratic map, with a parameter
*a*:



```maxima
(%i1) orbits(x^2+a, 0, 50, 200, [a, -2, 0.25], [style, dots]);
```


(Figure dynamics3)


To enlarge the region around the lower bifurcation near x `=` -1.25 use:


```maxima
(%i2) orbits(x^2+a, 0, 100, 400, [a,-1,-1.53], [x,-1.6,-0.8],
             [nticks, 400], [style,dots]);
```


(Figure dynamics4)

See also: `plot2d`.

### Function: out_neighbors (v, gr)

Returns the list of out-neighbors of the vertex *v* in the directed
graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) p : path_digraph(3)$
(%i3) in_neighbors(2, p);
(%o3)                          [1]
(%i4) out_neighbors(2, p);
(%o4)                          []
```

### Variable: palette

It can consist of one palette or a list of several palettes.  Each
palette is a list with a keyword followed by values. If the keyword is
gradient, it should be followed by a list of valid colors.


If the keyword is hue, saturation or value, it must be followed by 4
numbers. The first three numbers, which must be between 0 and 1, define
the hue, saturation and value of a basic color to be assigned to the
minimum value of z. The keyword specifies which of the three attributes
(hue, saturation or value) will be increased according to the values of
z.  The last number indicates the increase corresponding to the maximum
value of z.  That last number can be bigger than 1 or negative; the
corresponding values of the modified attribute will be rounded modulo 1.


Gnuplot only uses the first palette in the list; xmaxima will use the
palettes in the list sequentially, when several surfaces are plotted
together; if the number of palettes is exhausted, they will be repeated
sequentially.


The color of the mesh lines will be given by the option
`mesh_005flines_005fcolor`. If `palette` is given the value
`false`, the surfaces will not be shaded but represented with a
mesh of curves only. In that case, the colors of the lines will be
determined by the option `color`.


The single keyword `palette` removes any palette previously
defined, leaving it to the graphic program to decide the palette to use
and `nopalette` is a synonym for `[palette, false]`.

See also: `mesh_lines_color`, `color`.

### Function: parametric (parametric, xfun, yfun, par, parmin, parmax, parametric, xfun, yfun, zfun, par, parmin, parmax)

Draws parametric functions in 2D and 3D.


This object is affected by the following *graphic options*: `nticks`, 
`line_width`, `line_type`, `key`, `color` and `enhanced3d`.


**2D**


The command `parametric(xfun, yfun, par, parmin, parmax)` plots the parametric function `[xfun, yfun]`,
with parameter *par* taking values from *parmin* to *parmax*.


Example:



```maxima
(%i1) draw2d(explicit(exp(x),x,-1,3),
             color = red,
             key   = "This is the parametric one!!",
             parametric(2*cos(rrr),rrr^2,rrr,0,2*%pi))$
```

(Figure draw_parametric)


**3D**


`parametric(xfun, yfun, zfun, par, parmin, parmax)` plots the parametric curve `[xfun, yfun, zfun]`, with parameter *par* taking values from *parmin* to
*parmax*.


Example:



```maxima
(%i1) draw3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3),
             color = royalblue,
             parametric(cos(5*u)^2,sin(7*u),u-2,u,0,2),
             color      = turquoise,
             line_width = 2,
             parametric(t^2,sin(t),2+t,t,0,2),
             surface_hide = true,
             title = "Surface & curves" )$
```

(Figure draw_parametric2)

See also: `nticks`, `line_width`, `line_type`, `key`, `color`, `enhanced3d`.

### Function: parametric_surface (xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max)

Draws parametric surfaces in 3D.


**3D**


The command `parametric_surface(xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max)` plots the parametric surface `[xfun, yfun, zfun]`, with parameter *par1* taking values from *par1min* to
*par1max* and parameter *par2* taking values from *par2min* to
*par2max*.


This object is affected by the following *graphic options*: `draw_realpart`, `xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`
 and `color`.


Example:



```maxima
(%i1) draw3d(title          = "Sea shell",
             xu_grid        = 100,
             yv_grid        = 25,
             view           = [100,20],
             surface_hide   = true,
             parametric_surface(0.5*u*cos(u)*(cos(v)+1),
                           0.5*u*sin(u)*(cos(v)+1),
                           u*sin(v) - ((u+3)/8*%pi)^2 - 20,
                           u, 0, 13*%pi, v, -%pi, %pi) )$
```

(Figure draw_parametric3)

See also: `draw_realpart`, `xu_grid`, `yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`.

### Function: path_digraph (n)

Returns the directed path on *n* vertices.

### Function: path_graph (n)

Returns the path on *n* vertices.

### Variable: pdf_file

Saves the plot into a PDF file with name equal to *file_name*,
rather than showing it in the screen.  By default, the file will be
created in the directory defined by the variable
`maxima_tempdir`, unless *file_name* contains the character
“/”, in which case it will be assumed to contain the complete path where
the file should be created. The value of `maxima_tempdir` can be changed
to save the file in a different directory. When the option
`gnuplot_pdf_term_command` is also given, it will be used to set up
Gnuplot’s PDF terminal; otherwise, Gnuplot’s pdfcairo terminal
will be used with solid colored lines of width 3, plot
size of 17.2 cm by 12.9 cm and font of 18 points.

See also: `maxima_tempdir`, `gnuplot_pdf_term_command`.

### Function: petersen_graph (petersen_graph, petersen_graph, n, d)

Returns the petersen graph *P_{n,d}*. The default values for
*n* and *d* are `n=5` and `d=2`.

### Function: picture_equalp (x, y)

Returns `true` in case of equal pictures, and `false` otherwise.

### Function: picturep (x)

Returns `true` if the argument is a well formed image,
and `false` otherwise.

### Function: piechart (piechart, list, piechart, list, option_1, option_2, ..., piechart, one_column_matrix, piechart, one_column_matrix, option_1, option_2, ..., piechart, one_row_matrix, piechart, one_row_matrix, option_1, option_2, ...)

Similar to `barsplot`, but plots sectors instead of rectangles.


Available options are:



- *
*sector_colors* (default, `[]`): a list of colors for sectors.
When there are more sectors than specified colors, the extra necessary colors 
are chosen at random. See `color` to learn more about them.
- *
*pie_center* (default, `[0,0]`): diagram’s center.
- *
*pie_radius* (default, `1`): diagram’s radius.
- *
All global `draw` options, except `key`, which is 
internally assigned by `piechart`.
If you want to set your own values for this option or want to build
complex scenes, make use of `piechart_description`.
- *
The following local `draw` options: `key`, `color`, 
`fill_density` and `line_width`. See also
`ellipse`


There is also a function `wxpiechart` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Example:












```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) piechart(
  s1,
  xrange = [-1.1, 1.3],
  yrange = [-1.1, 1.1],
  title  = "Digit frequencies in pi")$
```


See also function `barsplot`.

See also: `barsplot`.

### Function: piechart_description (...)

Function `piechart_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

### Function: planar_embedding (gr)

Returns the list of facial walks in a planar embedding of *gr* and
`false` if *gr* is not a planar graph.


The graph *gr* must be biconnected.


The algorithm used is the Demoucron’s algorithm, which is a quadratic time
algorithm.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) planar_embedding(grid_graph(3,3));
(%o2) [[3, 6, 7, 8, 5, 2, 1, 0], [4, 3, 0, 1], [3, 4, 7, 6], 
                                      [8, 7, 4, 5], [1, 2, 5, 4]]
```

### Function: plot2d (plot2d, expr, range_x, options, plot2d, expr_1, =, expr_2, range_x, range_y, options, plot2d, parametric, expr_x, expr, _y, range, options, plot2d, discrete, points, options, plot2d, contour, expr, range_x, range_y, options, plot2d, type_1, ..., type_n, options)

There are 5 types of plots that can be plotted by `plot2d`:



1. **Explicit functions**. `plot2d` (*expr*, *range_x*,
*options*), where *expr* is an expression that depends on only
one variable, or the name of a function with one input parameter and
numerical results. *range_x* is a list with three elements, the
first one being the name of the variable that will be shown on the
horizontal axis of the plot, and the other two elements should be two
numbers, the first one smaller than the second, that define the minimum
and maximum values to be shown on the horizontal axis. The name of the
variable used in *range_x* must be the same variable on which
*expr* depends. The result will show in the vertical axis the
corresponding values of the expression or function for each value of the
variable in the horizontal axis.
2. **Implicit functions**. `plot2d` (*expr_1*=*expr_2*,
*range_x*, *range_y*, *options*), where *expr_1* and
*expr_2* are two expressions that can depend on one or two
variables. *range_x* and *range_y* must be two lists of three
elements that define the ranges for the variables in the two axes of the
plot; the first element of each list is the name of the corresponding
variable, and the other two elements are the minimum and maximum values
for that variable. The two variables on which *expr_1* and
*expr_2* can depend are those specified by *range_x* and
*range_y*. The result will be a curve or a set of curves where the
equation *expr_1*=*expr_2* is true.
3. **Parametric functions**. `plot2d` ([parametric,
*expr_x*, *expr*_y, *range*], *options*), where
*expr_x* and *expr*_y are two expressions that depend on a
single parameter. *range* must be a three-element list; the first
element must be the name of the parameter on which *expr_x* and
*expr*_y depend, and the other two elements must be the minimum and
maximum values for that parameter. The result will be a curve in which
the horizontal and vertical coordinates of each point are the values of
*expr_x* and *expr*_y for a value of the parameter within the
range given.
4. **Set of points**. `plot2d` ([discrete, *points*],
*options*), displays a list of points, joined by segments by
default. The horizontal and vertical coordinates of each of those points
can be specified in three different ways: With two lists of the same
length, in which the elements of the first list are the horizontal
coordinates of the points and the second list are the vertical
coordinates, or with a list of two-element lists, each one corresponding
to the two coordinates of one of the points, or with a single list that
defines the vertical coordinates of the points; in this last case, the
horizontal coordinates of the n points will be assumed to be the first n
natural numbers.
5. **Contour lines**. `plot2d` ([contour, *expr*],
*range_x*, *range_y*, *options*), where *expr* is an
expression that depends on two variables. *range_x* and
*range_y* will be lists whose first elements are the names of those
two variables, followed by two numbers that set the minimum and maximum
values for them. The first variable will be represented along the
horizontal axis and the second along the vertical axis. The result will
be a set of curves along which the given expression has certain
values. If those values are not specified with the option `levels`,
plotd2d will try to choose, at the most, 8 values of the form d*10^n, where d is
either 1, 2 or 5, all of them within the minimum and maximum values of
*expr* within the given ranges.


At the end of a plot2d command several of the options described in
`Plotting Options` can be used. Many instances of the 5 types
described above can be combined into a single plot, by putting them
inside a list: `plot2d` ([*type_1*, ..., *type_n*],
*options*). If one of the types included in the list require
*range_x* or *range_y*, those ranges should come immediately
after the list.


If there are several plots to be plotted, a legend will be
written to identity each of the expressions.  The labels that should be
used in that legend can be given with the option `legend`.  If that
option is not used, Maxima will create labels from the expressions or
function names.



**Examples:**



1. Explicit function.






```maxima
maxima
(%i1) plot2d (sin(x), [x, -%pi, %pi])$
```


(Figure plotting6)
2. Implicit function.






```maxima
maxima
(%i1) plot2d (x^2-y^3+3*y=2, [x,-2.5,2.5], [y,-2.5,2.5])$
```


(Figure plotting3)
3. Parametric function.







```maxima
maxima
(%i1) r: (exp(cos(t))-2*cos(4*t)-sin(t/12)^5)$
(%i2) plot2d([parametric, r*sin(t), r*cos(t), [t,-8*%pi,8*%pi]])$
```


(Figure plotting11)
4. Set of points.







```maxima
maxima

(%i1) plot2d ([discrete, makelist(i*%pi, i, 1, 5),
                           [0.6, 0.9, 0.2, 1.3, 1]])$
```


(Figure plotting14)
5. Contour lines.






```maxima
maxima
(%i1) plot2d ([contour, u^3 + v^2], [u, -4, 4], [v, -4, 4])$
```


(Figure plotting2)


**Examples using options**.


If an explicit function grows too fast, the `y` option can be used
to limit the values in the vertical axis:






```maxima
maxima

(%i1) plot2d (sec(x), [x, -2, 2], [y, -20, 20])$
plot2d: some values will be clipped.
```


(Figure plotting7)


When the plot box is disabled, no labels are created for the axes. In
that case, instead of using `xlabel` and `ylabel` to set the
names of the axes, it is better to use option `label`, which
allows more flexibility. Option `yx_ratio` is used to change the
default rectangular shape of the plot; in this example the plot will
fill a square.









```maxima
maxima

(%i1) plot2d ( x^2 - 1, [x, -3, 3], nobox, grid2d,
     [yx_ratio, 1], [axes, solid], [xtics, -2, 4, 2],
     [ytics, 2, 2, 6], [label, ["x", 2.9, -0.3],
     ["x^2-1", 0.1, 8]], [title, "A parabola"])$
```


(Figure plotting8)


A plot with a logarithmic scale in the vertical axis:






```maxima
maxima
(%i1) plot2d (exp(3*s), [s, -2, 2], logy)$
```


(Figure plotting9)


Plotting functions by name:









```maxima
maxima
(%i1) F(x) := x^2 $

(%i2) :lisp (defun |$g| (x) (m* x x x))
$g

(%i2) H(x) := if x < 0 then x^4 - 1 else 1 - x^5 $
(%i3) plot2d ([F, G, H], [u, -1, 1], [y, -1.5, 1.5])$
```


(Figure plotting10)


Plot of a circumference of radius 1 centered at the origin, together with the
function `y=-|x|`. To prevent the circumference to look like an
ellipse, option `same_xy` is used to scale the two axes at the same
rate. Option `nolegend` is also used to remove the legend identifying
the two functions.







```maxima
maxima

(%i1) plot2d([x^2+y^2=1, -abs(x)], [x, -1.5, 1.5], [y, -2, 2], same_xy,
        nolegend);
(%o1)                         false
```


(Figure plotting12)


A plot of 200 random numbers between 0 and 9:






```maxima
maxima
(%i1) plot2d ([discrete, makelist ( random(10), 200)])$
```


(Figure plotting13)


In the next example a table with three columns is saved in a file
“data.txt” which is then read and the second and third column are
plotted on the two axes:











```maxima
maxima
(%i1) display2d:false$

(%i2) with_stdout ("data.txt", for x:0 thru 10 do
                             print (x, x^2, x^3))$

(%i3) data: read_matrix ("data.txt")$

(%i4) plot2d ([discrete, transpose(data)[2], transpose(data)[3]],
  [style,points], [point_type,diamond], [color,red])$
```


(Figure plotting15)


A plot of discrete data points together with a continuous function:












```maxima
maxima
(%i1) xy: [[10, .6], [20, .9], [30, 1.1], [40, 1.3], [50, 1.4]]$

(%i2) plot2d([[discrete, xy], 2*%pi*sqrt(l/980)], [l,0,50],
        [style, points, lines], [color, red, blue],
        [point_type, asterisk],
        [legend, "experiment", "theory"],
        [xlabel, "pendulum's length (cm)"],
        [ylabel, "period (s)"])$
```


(Figure plotting16)


See also the `Plotting Options` section.

See also: `Plotting-Options`, `legend`, `y`, `xlabel`, `ylabel`, `label`, `yx_ratio`, `same_xy`, `nolegend`.

### Function: plot3d (plot3d, expr, x_range, y_range, ..., options, ..., plot3d, expr_1, ..., expr_n, x_range, y_range, ..., options, ...)

Displays a plot of one or more surfaces defined as functions of two
variables or in parametric form.


The functions to be plotted may be specified as expressions or function names.
The mouse can be used to rotate the plot looking at the surface from different
sides.


**Examples**.


Plot of a function of two variables:







```maxima
maxima

(%i1) plot3d (u^2 - v^2, [u, -2, 2], [v, -3, 3], [grid, 100, 100],
        nomesh_lines)$
```


(Figure plotting17)


Use of the `z` option to limit a function that goes to infinity
 (in this case the function is minus infinity on the x and y axes); this also
shows how to plot with only lines and no shading:







```maxima
maxima

(%i1) plot3d ( log ( x^2*y^2 ), [x, -2, 2], [y, -2, 2], [z, -8, 4],
         nopalette, [color, magenta])$
log: encountered log(0).
```


(Figure plotting18)


The infinite values of z can also be avoided by choosing a grid that
does not fall on any points where the function is undefined, as in the
next example, which also shows how to change the palette and how to
include a color bar that relates colors to values of the z variable:









```maxima
maxima

(%i1) plot3d (log (x^2*y^2), [x, -2, 2], [y, -2, 2],[grid, 29, 29],
      [palette, [gradient, red, orange, yellow, green]],
      color_bar, [xtics, 1], [ytics, 1], [ztics, 4],
      [color_bar_tics, 4])$
log: encountered log(0).
```


(Figure plotting19)


Two surfaces in the same plot. Ranges specific to one of the surfaces can
be given by placing each expression and its ranges in a separate list;
global ranges for the complete plot are also given after the function
definitions.








```maxima
maxima

(%i1) plot3d ([[-3*x - y, [x, -2, 2], [y, -2, 2]],
   4*sin(3*(x^2 + y^2))/(x^2 + y^2), [x, -3, 3], [y, -3, 3]],
   [x, -4, 4], [y, -4, 4])$
expt: undefined: 0 to a negative exponent.
```


(Figure plotting20)


Plot of a Klein bottle, defined parametrically:










```maxima
maxima
(%i1) expr_1: 5*cos(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)-10$
(%i2) expr_2: -5*sin(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)$
(%i3) expr_3: 5*(-sin(x/2)*cos(y)+cos(x/2)*sin(2*y))$

(%i4) plot3d ([expr_1, expr_2, expr_3], [x, -%pi, %pi],
        [y, -%pi, %pi], [grid, 50, 50])$
```


(Figure plotting21)


Plot of a “spherical harmonic” function, using the predefined
transformation, `spherical_to_xyz` to transform from spherical
coordinates to rectangular coordinates. See the documentation for
`spherical_005fto_005fxyz`.







```maxima
maxima

(%i1) plot3d (sin(2*theta)*cos(phi), [theta,0,%pi], [phi,0,2*%pi],
   [transform_xy, spherical_to_xyz], [grid, 30, 60], nolegend)$
```


(Figure plotting22)


Use of the pre-defined function `polar_to_xy` to transform from
cylindrical to rectangular coordinates.  See the documentation for
`polar_005fto_005fxy`.







```maxima
maxima

(%i1) plot3d (r^.33*cos(th/3), [r,0,1], [th,0,6*%pi], nobox,
    nolegend, [grid, 12, 80], [transform_xy, polar_to_xy])$
```


(Figure plotting23)


Plot of a sphere using the transformation from spherical to rectangular
coordinates. Option `same_xyz` is used to get the three axes
scaled in the same proportion. When transformations are used, it is not
convenient to eliminate the mesh lines, because Gnuplot will not show the
surface correctly.








```maxima
maxima

(%i1) plot3d ( 5, [theta,0,%pi], [phi,0,2*%pi], same_xyz, nolegend,
  [transform_xy, spherical_to_xyz], [mesh_lines_color,blue],
  [palette,[gradient,"#1b1b4e", "#8c8cf8"]])$
```


(Figure plotting24)


Definition of a function of two-variables using a matrix.  Notice the
single quote in the definition of the function, to prevent `plot3d`
from failing when it realizes that the matrix will require integer
indices.








```maxima
maxima
(%i1) M: matrix([1,2,3,4], [1,2,3,2], [1,2,3,4], [1,2,3,3])$
(%i2) f(x, y) := float('M [round(x), round(y)])$
(%i3) plot3d (f(x,y), [x,1,4], [y,1,4], [grid,3,3], nolegend)$
```


(Figure plotting25)


By setting the elevation equal to zero, a surface can be seen as a map
in which each color represents a different level.








```maxima
maxima

(%i1) plot3d (cos (-x^2 + y^3/4), [x,-4,4], [y,-4,4], [zlabel,""],
       [mesh_lines_color,false], [elevation,0], [azimuth,0],
       color_bar, [grid,80,80], noztics, [color_bar_tics,1])$
```


(Figure plotting26)


See also `Plotting-Options`.

See also: `z`, `spherical_to_xyz`, `polar_to_xy`, `same_xyz`, `Plotting-Options`.

### Variable: plot_format

Default value: `gnuplot`, in Windows systems, or `gnuplot_pipes` in
other systems.


Where *format* is one of the following: gnuplot, xmaxima,
gnuplot_pipes or geomview. The four possibilities: `[plot_format, gnuplot]`, `[plot_format, gnuplot_pipes]`, `[plot_format, geomview]` and `[plot_format, xmaxima]`, can be abbreviated by the
keywords `gnuplot`, `gnuplot_pipes`, `geomview` and
`xmaxima`.


It sets the format to be used for plotting as explained in
`Plotting-Formats`.

See also: `Plotting-Formats`.

### Variable: plot_options

This variable is being kept for compatibility with older versions of Wxmaxima,
but its use is deprecated. To set global plotting options, see their current
values or remove options, use `set_plot_option`,
`get_plot_option` `remove_plot_option`, and
`reset_005fplot_005foptions`.

See also: `set_plot_option`, `get_plot_option`, `remove_plot_option`, `reset_plot_options`.

### Variable: plot_realpart

Default value: `false`


If set to `true`, the functions to be plotted will be considered as
complex functions whose real value should be plotted; this is equivalent
to plotting `realpart(function)`.  If set to `false`,
nothing will be plotted when the function does not give a real value.
For instance, when `x` is negative, `log(x)` gives a complex
value, with real value equal to `log(abs(x))`; if
`plot_realpart` were `true`, `log(-5)` would be plotted
as `log(5)`, while nothing would be plotted if `plot_realpart`
were `false`. The single keyword `plot_realpart` can be used
as a synonym for `[plot_realpart, true]` and `noplot_realpart`
is a synonym for `[plot_realpart, false]`.

### Variable: plotepsilon

Default value: 1e-6


This value is used by `plot2d` when plotting implicit functions or
contour lines. When plotting an explicit function `expr_1=expr_2`,
it is converted into `expr_1-expr_2` and the points where that equals
zero are searched. When a contour line for `expr` equal to some value
is going to be plotted, the points where `expr` minus that value
are equal to zero are searched. The search is done by computing those
expressions at a grid of points (see `sample`). If at one of the
points in that grid the absolute value of the expression is less than
the value of `plotepsilon`, it will be assumed to be zero, and
therefore, as being part of the curve to be plotted.

See also: `plot2d`, `sample`.

### Variable: png_file

Saves the plot into a PNG graphics file with name equal to *file_name*,
rather than showing it in the screen. By default, the file will be
created in the directory defined by the variable
`maxima_tempdir`, unless *file_name* contains the character
“/”, in which case it will be assumed to contain the complete path where
the file should be created. The value of `maxima_tempdir` can be changed
to save the file in a different directory. When the option
`gnuplot_png_term_command` is also given, it will be used to set up
Gnuplot’s PNG terminal; otherwise, Gnuplot’s pngcairo terminal
will be used, with a font of size 12.

See also: `maxima_tempdir`, `gnuplot_png_term_command`.

### Variable: point_size

Default value: 1


`point_size` sets the size for plotted points. It must be a
non negative number.


This option has no effect when graphic option `point_type` is
set to `dot`.


This option affects the following graphic objects:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Example:



```maxima
(%i1) draw2d(points(makelist([random(20),random(50)],k,1,10)),
        point_size = 5,
        points(makelist(k,k,1,20),makelist(random(30),k,1,20)))$
```

(Figure draw_point_size)

See also: `points`.

### Variable: point_type

In gnuplot, each set of points to be plotted with the style “points”
or “linespoints” will be represented with objects taken from this
list, in sequential order.  If there are more sets of points than objects
in this list, they will be repeated sequentially.
The possible objects that can be used are: `bullet`, `circle`,
`plus`, `times`, `asterisk`, `box`, `square`,
`triangle`, `delta`, `wedge`, `nabla`, `diamond`,
`lozenge`.

### Function: points (points, x1, y1, x2, y2, ..., points, x1, x2, ..., y1, y2, ..., points, y1, y2, ..., points, x1, y1, z1, x2, y2, z2, ..., points, x1, x2, ..., y1, y2, ..., z1, z2, ..., points, matrix, points, 1d_y_array, points, 1d_x_array, 1d_y_array, points, 1d_x_array, 1d_y_array, 1d_z_array, points, 2d_xy_array, points, 2d_xyz_array)

Draws points in 2D and 3D.


This object is affected by the following *graphic options*: `point_size`, 
`point_type`, `points_joined`, `line_width`, `key`,
`line_type` and `color`. In 3D mode, it is also affected by `enhanced3d`


**2D**


`points ([[x1,y1], [x2,y2],...])` or
`points ([x1,x2,...], [y1,y2,...])`
plots points `[x1,y1]`, `[x2,y2]`, etc. If abscissas
are not given, they are set to consecutive positive integers, so that 
`points ([y1,y2,...])` draws points `[1,y1]`, `[2,y2]`, etc.
If *matrix* is a two-column or two-row matrix, `points (matrix)`
draws the associated points. If *matrix* is an one-column or one-row matrix,
abscissas are assigned automatically.


If *1d_y_array* is a 1D lisp array of numbers, `points (1d_y_array)` plots them
setting abscissas to consecutive positive integers. `points (1d_x_array, 1d_y_array)`
plots points with their coordinates taken from the two arrays passed as arguments. If
*2d_xy_array* is a 2D array with two columns, or with two rows, `points (2d_xy_array)`
plots the corresponding points on the plane.


Examples:


Two types of arguments for `points`, a list of pairs and two lists
of separate coordinates.


```maxima
(%i1) draw2d(
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

(Figure draw_points)


Drawing impulses.


```maxima
(%i1) draw2d(
        points_joined = impulses,
        line_width    = 2,
        color         = red,
        points(makelist([random(20),random(50)],k,1,10)))$
```

(Figure draw_points2)


Array with ordinates.


```maxima
(%i1) a: make_array (flonum, 100) $
(%i2) for i:0 thru 99 do a[i]: random(1.0) $
(%i3) draw2d(points(a)) $
```

(Figure draw_points3)


Two arrays with separate coordinates.


```maxima
(%i1) x: make_array (flonum, 100) $
(%i2) y: make_array (fixnum, 100) $
(%i3) for i:0 thru 99 do (
        x[i]: float(i/100),
        y[i]: random(10) ) $
(%i4) draw2d(points(x, y)) $
```

(Figure draw_points4)


A two-column 2D array.


```maxima
(%i1) xy: make_array(flonum, 100, 2) $
(%i2) for i:0 thru 99 do (
        xy[i, 0]: float(i/100),
        xy[i, 1]: random(10) ) $
(%i3) draw2d(points(xy)) $
```

(Figure draw_points5)


Drawing an array filled with function `read_array`.


```maxima
(%i1) a: make_array(flonum,100) $
(%i2) read_array (file_search ("pidigits.data"), a) $
(%i3) draw2d(points(a)) $
```


**3D**


`points([[x1, y1, z1], [x2, y2, z2], ...])` or `points([x1, x2, ...], [y1, y2, ...], [z1, z2,...])` plots points `[x1, y1, z1]`,
`[x2, y2, z2]`, etc.  If *matrix* is a three-column
or three-row matrix, `points (matrix)` draws the associated points.


When arguments are lisp arrays, `points (1d_x_array, 1d_y_array, 1d_z_array)`
takes coordinates from the three 1D arrays.  If *2d_xyz_array* is a 2D array with three columns,
or with three rows, `points (2d_xyz_array)` plots the corresponding points.


Examples:


One tridimensional sample,


```maxima
(%i1) load ("numericalio")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) draw3d(title = "Daily average wind speeds",
             point_size = 2,
             points(args(submatrix (s2, 4, 5))) )$
```


Two tridimensional samples,


```maxima
(%i1) load ("numericalio")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) draw3d(
         title = "Daily average wind speeds. Two data sets",
         point_size = 2,
         key        = "Sample from stations 1, 2 and 3",
         points(args(submatrix (s2, 4, 5))),
         point_type = 4,
         key        = "Sample from stations 1, 4 and 5",
         points(args(submatrix (s2, 2, 3))) )$
```


Unidimensional arrays,


```maxima
(%i1) x: make_array (fixnum, 10) $
(%i2) y: make_array (fixnum, 10) $
(%i3) z: make_array (fixnum, 10) $
(%i4) for i:0 thru 9 do (
        x[i]: random(10),
        y[i]: random(10),
        z[i]: random(10) ) $
(%i5) draw3d(points(x,y,z)) $
```

(Figure draw_points6)


Bidimensional colored array,


```maxima
(%i1) xyz: make_array(fixnum, 10, 3) $
(%i2) for i:0 thru 9 do (
        xyz[i, 0]: random(10),
        xyz[i, 1]: random(10),
        xyz[i, 2]: random(10) ) $
(%i3) draw3d(
         enhanced3d = true,
         points_joined = true,
         points(xyz)) $
```

(Figure draw_points7)


Color numbers explicitly specified by the user.


```maxima
(%i1) pts: makelist([t,t^2,cos(t)], t, 0, 15)$
(%i2) col_num: makelist(k, k, 1, length(pts))$
(%i3) draw3d(
        enhanced3d = ['part(col_num,k),k],
        point_size = 3,
        point_type = filled_circle,
        points(pts))$
```

(Figure draw_points8)

See also: `point_size`, `point_type`, `points_joined`, `line_width`, `key`, `line_type`, `enhanced3d`.

### Variable: points_joined

Default value: `false`


When `points_joined` is `true`, points are joined by lines; when `false`,
isolated points are drawn. A third possible value for this graphic option is 
`impulses`; in such case, vertical segments are drawn from points to the x-axis (2D)
or to the xy-plane (3D).


This option affects the following graphic objects:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Example:



```maxima
(%i1) draw2d(xrange        = [0,10],
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

(Figure draw_points_joined)

See also: `points`.

### Function: polar (radius, ang, minang, maxang)

Draws 2D functions defined in polar coordinates.


**2D**


`polar (radius,ang,minang,maxang)` plots function 
`radius(ang)` defined in polar coordinates, with variable 
*ang* taking values from 
*minang* to *maxang*.


This object is affected by the following *graphic options*: `nticks`, 
`line_width`, `line_type`, `key` and `color`.


Example:



```maxima
(%i1) draw2d(user_preamble = "set grid polar",
             nticks        = 200,
             xrange        = [-5,5],
             yrange        = [-5,5],
             color         = blue,
             line_width    = 3,
             title         = "Hyperbolic Spiral",
             polar(10/theta,theta,1,10*%pi) )$
```

(Figure draw_polar)

See also: `nticks`, `line_width`, `line_type`, `key`.

### Function: polar_to_xy ()

It can be given as value for the `transform_xy` option of
plot3d.  Its effect will be to interpret the two independent variables in
plot3d as the distance from the z axis and the azimuthal angle (polar
coordinates), and transform them into x and y coordinates.

See also: `transform_xy`.

### Function: polygon (polygon, x1, y1, x2, y2, ..., polygon, x1, x2, ..., y1, y2, ...)

Draws polygons in 2D.


**2D**


The commands `polygon([[x1, y1], [x2, y2], ...])`
or `polygon([x1, x2, ...], [y1, y2, ...])` plot on
the plane a polygon with vertices `[x1, y1]`, `[x2, y2]`, etc.


This object is affected by the following *graphic options*: `transparent`, 
`fill_color`, `fill_density`, `border`, `line_width`, `key`,
 `line_type` and `color`.


Example:



```maxima
(%i1) draw2d(color      = "#e245f0",
             line_width = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = yellow,
             polygon([[5,2],[9,2],[7,5]]) )$
```

(Figure draw_polygon)

See also: `transparent`, `fill_color`, `fill_density`, `border`, `line_width`, `key`, `line_type`.

### Function: print_graph (gr)

Prints some information about the graph *gr*.


Example:










```maxima
(%i1) load ("graphs")$
(%i2) c5 : cycle_graph(5)$
(%i3) print_graph(c5)$
Graph on 5 vertices with 5 edges.
Adjacencies:
  4 :  0  3
  3 :  4  2
  2 :  3  1
  1 :  2  0
  0 :  4  1
(%i4) dc5 : cycle_digraph(5)$
(%i5) print_graph(dc5)$
Digraph on 5 vertices with 5 arcs.
Adjacencies:
  4 :  0
  3 :  4
  2 :  3
  1 :  2
  0 :  1
(%i6) out_neighbors(0, dc5);
(%o6)                          [1]
```

### Variable: program

Defines the program used for positioning vertices of the graph. Can be
one of the graphviz programs (dot, neato, twopi, circ, fdp),
*circular*, *spring_embedding* or
*planar_embedding*. *planar_embedding* is only available for
2-connected planar graphs. When `program=spring_embedding`, a set
of vertices with fixed position can be specified with the
*fixed_vertices* option.

### Variable: proportional_axes

Default value: `none`


When `proportional_axes` is equal to `xy` or `xyz`,
the aspect ratio of the axis units will be set to 1:1 resulting in a 2D or 3D
scene that will be drawn with axes proportional to their relative lengths.


Since this is a global graphics option, its position in the scene description
does not matter.


This option works with Gnuplot version 4.2.6 or greater.


Examples:


Single 2D plot.



```maxima
(%i1) draw2d(
        ellipse(0,0,1,1,0,360),
        transparent=true,
        color = blue,
        line_width = 4,
        ellipse(0,0,2,1/2,0,360),
        proportional_axes = 'xy) $
```

(Figure draw_proportional_axis)


Multiplot.



```maxima
(%i1) draw(
        terminal = wxt,
        gr2d(proportional_axes = 'xy,
             explicit(x^2,x,0,1)),
        gr2d(explicit(x^2,x,0,1),
             xrange = [0,1],
             yrange = [0,2],
             proportional_axes='xy),
        gr2d(explicit(x^2,x,0,1)))$
```

(Figure draw_proportional_axis2)

### Variable: ps_file

Saves the plot into a Postscript file with name equal to *file_name*,
rather than showing it in the screen.  By default, the file will be
created in the directory defined by the variable
`maxima_tempdir`, unless *file_name* contains the character
“/”, in which case it will be assumed to contain the complete path where
the file should be created. The value of `maxima_tempdir` can be changed
to save the file in a different directory. When the option
`gnuplot_ps_term_command` is also given, it will be used to set up
Gnuplot’s Postscript terminal; otherwise, Gnuplot’s postscript terminal
will be used with the EPS option, solid colored lines of width 2, plot
size of 16.4 cm by 12.3 cm and font of 24 points.

See also: `maxima_tempdir`, `gnuplot_ps_term_command`.

### Function: quadrilateral (point_1, point_2, point_3, point_4)

Draws a quadrilateral.


**2D**


`quadrilateral([x1, y1], [x2, y2], [x3, y3], [x4, y4])` draws a quadrilateral with vertices
`[x1, y1]`, `[x2, y2]`, 
`[x3, y3]`, and `[x4, y4]`.


This object is affected by the following *graphic options*:

`transparent`, `fill_color`, `border`, `line_width`,
`key`, `xaxis_secondary`, `yaxis_secondary`, `line_type`,
`transform` and `color`.


Example:



```maxima
(%i1) draw2d(
        quadrilateral([1,1],[2,2],[3,-1],[2,-2]))$
```

(Figure draw_quadrilateral)


**3D**


`quadrilateral([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4])`
draws a quadrilateral with vertices `[x1, y1, z1]`,
`[x2, y2, z2]`, `[x3, y3, z3]`,
and `[x4, y4, z4]`.


This object is affected by the following *graphic options*: `line_type`, 
`line_width`, `color`, `key`, `enhanced3d` and
`transform`.

See also: `transparent`, `fill_color`, `border`, `line_width`, `key`, `xaxis_secondary`, `yaxis_secondary`, `line_type`, `color`, `enhanced3d`, `transform`.

### Function: random_bipartite_graph (a, b, p)

Returns a random bipartite graph on `a+b` vertices. Each edge is
present with probability *p*.

### Function: random_digraph (n, p)

Returns a random directed graph on *n* vertices. Each arc is present
with probability *p*.

### Function: random_graph (n, p)

Returns a random graph on *n* vertices. Each edge is present with
probability *p*.

### Function: random_graph1 (n, m)

Returns a random graph on *n* vertices and random *m* edges.

### Function: random_network (n, p, w)

Returns a random network on *n* vertices. Each arc is present with
probability *p* and has a weight in the range `[0,w]`. The
function returns a list `[network, source, sink]`.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) [net, s, t] : random_network(50, 0.2, 10.0);
(%o2)                   [DIGRAPH, 50, 51]
(%i3) max_flow(net, s, t)$
(%i4) first(%);
(%o4)                   27.65981397932507
```

### Function: random_regular_graph (random_regular_graph, n, random_regular_graph, n, d)

Returns a random *d*-regular graph on *n* vertices. The default
value for *d* is `d=3`.

### Function: random_tournament (n)

Returns a random tournament on *n* vertices.

### Function: random_tree (n)

Returns a random tree on *n* vertices.

### Function: read_xpm (xpm_file)

Reads a file in xpm and returns a picture object.

### Function: rectangle (x1, y1, x2, y2)

Draws rectangles in 2D.


**2D**


`rectangle ([x1,y1], [x2,y2])` draws a rectangle with opposite vertices
`[x1,y1]` and `[x2,y2]`.


This object is affected by the following *graphic options*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`,
`line_type` and `color`.


Example:



```maxima
(%i1) draw2d(fill_color  = red,
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

(Figure draw_rectangle)

See also: `transparent`, `fill_color`, `border`, `line_width`, `key`, `line_type`.

### Variable: redraw

Default value: *false*


If `true`, vertex positions are recomputed even if the positions
have been saved from a previous drawing of the graph.

### Function: region (expr, var1, minval1, maxval1, var2, minval2, maxval2)

Plots a region on the plane defined by inequalities.


**2D**
*expr* is an expression formed by inequalities and boolean operators
`and`, `or`, and `not`. The region is bounded by the rectangle
defined by $[minval1, maxval1]$ and $[minval2, maxval2]$.


This object is affected by the following *graphic options*: `fill_color`, `fill_density`,
`key`, `x_voxel` and `y_005fvoxel`.


Example:



```maxima
(%i1) draw2d(
        x_voxel = 30,
        y_voxel = 30,
        region(x^2+y^2<1 and x^2+y^2 > 1/2,
               x, -1.5, 1.5, y, -1.5, 1.5));
```

See also: `not`, `fill_color`, `fill_density`, `key`, `x_voxel`, `y_voxel`.

### Function: region_boundaries (x1, y1, x2, y2)

Detects polygonal segments of global variable `boundaries_array`
fully contained in the rectangle with vertices (*x1*,*y1*) -upper left- 
and (*x2*,*y2*) -bottom right-.


Example:


Returns segment numbers for plotting southern Italy.


```maxima
(%i1) load("worldmap")$
(%i2) region_boundaries(10.4,41.5,20.7,35.4);
(%o2)                [1846, 1863, 1864, 1881, 1888, 1894]
(%i3) draw2d(geomap(%))$
```

(Figure worldmap_region_boundaries)

### Function: region_boundaries_plus (x1, y1, x2, y2)

Detects polygonal segments of global variable `boundaries_array`
containing at least one vertex in the rectangle defined by vertices (*x1*,*y1*)
-upper left- and (*x2*,*y2*) -bottom right-.


Example:



```maxima
(%i1) load("worldmap")$
(%i2) region_boundaries_plus(10.4,41.5,20.7,35.4);
(%o2) [1060, 1062, 1076, 1835, 1839, 1844, 1846, 1858,
       1861, 1863, 1864, 1871, 1881, 1888, 1894, 1897]
(%i3) draw2d(geomap(%))$
```

(Figure worldmap_region_boundaries_plus)

### Function: remove_edge (e, gr)

Removes the edge *e* from the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) c3 : cycle_graph(3)$
(%i3) remove_edge([0,1], c3)$
(%i4) print_graph(c3)$
Graph on 3 vertices with 2 edges.
Adjacencies:
  2 :  0  1
  1 :  2
  0 :  2
```

### Function: remove_plot_option (name)

Removes the global value of an option. The name of the option must be given.


See also `set_plot_option`, `get_plot_option` and
`Plotting Options`.

See also: `set_plot_option`, `get_plot_option`, `Plotting-Options`.

### Function: remove_vertex (v, gr)

Removes the vertex *v* from the graph *gr*.

### Function: reset_plot_options ()

Sets the default global values of the plotting options. After changing
the global values of some plotting options, this function is used to
recovered the same values as when Maxima was started.

### Function: rgb2level (pic)

Transforms an *rgb* picture into a *level* one by
averaging the red, green and blue channels.

### Variable: run_viewer

Default value: `true`


This option is only used when the plot format is `gnuplot` and the
terminal is `default` or when the Gnuplot terminal is set to
`dumb` (see `gnuplot_term`) and can have a true or false
value.


If the terminal is `default`, a file `random-string.gnuplot` (or
other name specified with `gnuplot_out_file`) is created with the
gnuplot commands necessary to generate the plot. Option `run_viewer`
controls whether or not Gnuplot will be launched to execute those
commands and show the plot.


If the terminal is `default`, gnuplot is run to execute the
commands in `random-string.gnuplot`, producing another file
`maxplot.txt` (or other name specified with
`gnuplot_out_file`). Option `run_viewer` controls whether or
not that file, with an ASCII representation of the plot, will be shown
in the Maxima or Xmaxima console.


Its default value, true, makes the plots appear in either the console or
a separate graphics window. `run_viewer` and `norun_viewer`
are synonyms for `[run_viewer, true]` and `[run_viewer, false]`.

See also: `gnuplot_term`, `gnuplot_out_file`.

### Variable: same_xy

It can be either true or false. If true, the scales used in the x and y
axes will be the same, in either 2d or 3d plots. See also
`yx_005fratio`. `same_xy` and `nosame_xy` are synonyms for
`[same_xy, true]` and `[same_xy, false]`.

See also: `yx_ratio`.

### Variable: same_xyz

It can be either true or false. If true, the scales used in the 3 axes
of a 3d plot will be the same. `same_xyz` and `nosame_xyz` are
synonyms for `[same_xyz, true]` and `[same_xyz, false]`.

### Variable: sample

Default value: `[sample, 47, 47]`


*nx* and *ny* must be two natural numbers that will be used by
`plot2d` to look for the points that make part of the plot of an
implicit function or a contour line. The domain is divided into *nx*
intervals in the horizontal axis and *ny* intervals in the vertical
axis and the numerical value of the expression is computed at the
borders of those intervals. Higher values of *nx* and *ny* will
give smoother curves, but will increase the time needed to trace the
plot. When there are critical points in the plot where the curve changes
direction, to get better results it is more important to try to make
those points to be at the border of the intervals, rather than
increasing *nx* and *ny*.

See also: `plot2d`.

### Function: scatterplot (scatterplot, list, scatterplot, list, option_1, option_2, ..., scatterplot, matrix, scatterplot, matrix, option_1, option_2, ...)

Plots scatter diagrams both for univariate (*list*) and multivariate 
(*matrix*) samples.


Available options are the same admitted by `histogram`.


There is also a function `wxscatterplot` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Examples:


Univariate scatter diagram from a simulated Gaussian sample. 












```maxima
(%i1) load ("descriptive")$
(%i2) load ("distrib")$

(%i3) scatterplot(
  random_normal(0,1,200),
  xaxis      = true,
  point_size = 2,
  dimensions = [600,150])$
```


Two dimensional scatter plot.













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


Three dimensional scatter plot.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) scatterplot(submatrix (s2, 1,2), nclasses=4)$
```


Five dimensional scatter plot, with five classes histograms.














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


For plotting isolated or line-joined points in two and three dimensions,
see `points`. See also `histogram`.

See also: `histogram`.

### Function: scatterplot_description (...)

Function `scatterplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

### Function: set_draw_defaults (graphic option, ..., graphic object, ...)

Sets user graphics options. This function is useful for plotting a sequence
of graphics with common graphics options. Calling this function without
arguments removes user defaults.


Example:



```maxima
(%i1) set_draw_defaults(
         xrange = [-10,10],
         yrange = [-2, 2],
         color  = blue,
         grid   = true)$
(%i2) /* plot with user defaults */
      draw2d(explicit(((1+x)**2/(1+x*x))-1,x,-10,10))$
(%i3) set_draw_defaults()$
(%i4) /* plot with standard defaults */
      draw2d(explicit(((1+x)**2/(1+x*x))-1,x,-10,10))$
```

### Function: set_edge_weight (e, w, gr)

Assigns the weight *w* to the edge *e* in the graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([1, 2], [[[1,2], 1.2]])$
(%i3) get_edge_weight([1,2], g);
(%o3)                          1.2
(%i4) set_edge_weight([1,2], 2.1, g);
(%o4)                         done
(%i5) get_edge_weight([1,2], g);
(%o5)                          2.1
```

### Function: set_plot_option (option)

Accepts any of the options listed in the section `Plotting Options`,
and saves them for use in plotting commands. The values of the options set
in each plotting command will have precedence, but if those options are
not given, the default values set with this function will be used.


`set_plot_option` evaluates its argument and returns the complete
list of options (after modifying the option given). If called without
any arguments, it will simply show the list of current default options.


See also `remove_plot_option`, `get_plot_option` and the section
on `Plotting-Options`.


Example:


Modification of the `grid` values.






```maxima
maxima

(%i1) set_plot_option ([grid, 30, 40]);
(%o1) [[plot_format, gnuplot_pipes], [grid, 30, 40], 
[run_viewer, true], [axes, true], [nticks, 29], 
[adapt_depth, 5], [color, blue, red, green, magenta, black, 
cyan], [point_type, bullet, box, triangle, plus, times, 
asterisk], [palette, [hue, 0.33333333, 0.7, 1, 0.5], 
[hue, 0.8, 0.7, 1, 0.4]], [gnuplot_svg_background, white], 
[gnuplot_preamble, ], [gnuplot_term, default]]
```

See also: `Plotting-Options`, `remove_plot_option`, `get_plot_option`, `grid`.

### Function: set_vertex_label (v, l, gr)

Assigns the label *l* to the vertex *v* in the graph *gr*.


A label may be any Maxima expression,
and two or more vertices may have the same label.


Example:











```maxima
(%i1) load ("graphs")$
(%i2) g : create_graph([[1, "One"], [2, "Two"]], [[1, 2]])$
(%i3) get_vertex_label(1, g);
(%o3)                          One
(%i4) set_vertex_label(1, "oNE", g);
(%o4)                         done
(%i5) get_vertex_label(1, g);
(%o5)                          oNE
(%i6) h : create_graph([[11, x], [22, y], [33, x + y]], [[11, 33], [22, 33]]) $
(%i7) get_vertex_label (33, h);
(%o7)                         y + x
```

### Function: sha1sum (sha1sum, arg, sha1sum, arg, return-type)

Returns the `SHA1` fingerprint of a string, a non-negative integer or 
a list of octets. The default return value is a string containing 40 hex characters.


The optional argument *return-type* allows `sha1sum` to alternatively 
return the corresponding number or list of octets.
*return-type* may be `string`, `number` or `list`.


Example:



```maxima
(%i1) ibase: obase: 16.$
(%i2) msg: "foo bar baz"$
(%i3) string: sha1sum(msg);
(%o3)              c7567e8b39e2428e38bf9c9226ac68de4c67dc39
(%i4) integer: sha1sum(msg, 'number);
(%o4)             0c7567e8b39e2428e38bf9c9226ac68de4c67dc39
(%i5) octets: sha1sum(msg, 'list);
(%o5)  [0C7,56,7E,8B,39,0E2,42,8E,38,0BF,9C,92,26,0AC,68,0DE,4C,67,0DC,39]
(%i6) sdowncase( printf(false, "~{~2,'0x~^:~}", octets) );
(%o6)     c7:56:7e:8b:39:e2:42:8e:38:bf:9c:92:26:ac:68:de:4c:67:dc:39
```


Note that in case *arg* contains German umlauts or other non-ASCII 
characters (resp. octets larger than 127) the `SHA1` fingerprint is platform dependent.

### Function: sha256sum (sha256sum, arg, sha256sum, arg, return-type)

Returns the `SHA256` fingerprint of a string, a non-negative integer or 
a list of octets. The default return value is a string containing 64 hex characters.


The optional argument *return-type* allows `sha256sum` to alternatively 
return the corresponding number or list of octets (see `sha1sum`).


Example:



```maxima
(%i1) string: sha256sum("foo bar baz");
(%o1)  dbd318c1c462aee872f41109a4dfd3048871a03dedd0fe0e757ced57dad6f2d7
```


Note that in case *arg* contains German umlauts or other non-ASCII 
characters (resp. octets larger than 127) the `SHA256` fingerprint is platform dependent.

See also: `sha1sum`.

### Function: shortest_path (u, v, gr)

Returns the shortest path from *u* to *v* in the graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) path : shortest_path(0, 7, d);
(%o3)                   [0, 1, 19, 13, 7]
(%i4) draw_graph(d, show_edges=vertices_to_path(path))$
```


(Figure graphs08, Shortest path between two vertices in a dodecahedral graph)

### Function: shortest_weighted_path (u, v, gr)

Returns the length of the shortest weighted path and the shortest
weighted path from *u* to *v* in the graph *gr*.


The length of a weighted path is the sum of edge weights of edges in the
path. If an edge has no weight, then it has a default weight 1.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) g: petersen_graph(20, 2)$
(%i3) for e in edges(g) do set_edge_weight(e, random(1.0), g)$
(%i4) shortest_weighted_path(0, 10, g);
(%o4) [2.575143920268482, [0, 20, 38, 36, 34, 32, 30, 10]]
```

### Variable: show_edge_color

The color used for displaying edges in the *show_edges* list.

### Variable: show_edge_type

Defines how edges in *show_edges* are displayed. See the
*line_type* option for the `draw` package.

### Variable: show_edge_width

The width of edges in *show_edges*.

### Variable: show_edges

Display edges specified in the list *e_list* using a different
color.

### Variable: show_id

Default value: *false*


If *true* then ids of the vertices are displayed.

### Variable: show_label

Default value: *false*


If *true* then labels of the vertices are displayed.

### Variable: show_vertex_color

The color used for displaying vertices in the *show_vertices* list.

### Variable: show_vertex_size

The size of vertices in *show_vertices*.

### Variable: show_vertex_type

Defines how vertices specified in *show_vertices* are displayed.
See the *point_type* option for the `draw` package for possible
values.

### Variable: show_vertices

Default value: []


Display selected vertices in the using a different color.

### Variable: show_weight

Default value: *false*


If *true* then weights of the edges are displayed.

### Function: small_rhombicosidodecahedron_graph ()

Returns the small rhombicosidodecahedron graph.

### Function: small_rhombicuboctahedron_graph ()

Returns the small rhombicuboctahedron graph.

### Function: snub_cube_graph ()

Returns the snub cube graph.

### Function: snub_dodecahedron_graph ()

Returns the snub dodecahedron graph.

### Function: sparse6_decode (str)

Returns the graph encoded in the sparse6 format in the string *str*.

### Function: sparse6_encode (gr)

Returns a string which encodes the graph *gr* in the sparse6 format.

### Function: sparse6_export (gr_list, fl)

Exports graphs in the list *gr_list* to the file *fl* in the
sparse6 format.

### Function: sparse6_import (fl)

Returns a list of graphs from the file *fl* in the sparse6 format.

### Function: spherical (radius, azi, minazi, maxazi, zen, minzen, maxzen)

Draws 3D functions defined in spherical coordinates.


**3D**


`spherical(radius, azi, minazi, maxazi, zen, minzen, maxzen)` plots the function `radius(azi, zen)` defined in spherical coordinates, with *azimuth* *azi* taking
values from *minazi* to *maxazi* and *zenith* *zen* taking values
from *minzen* to *maxzen*.


This object is affected by the following *graphic options*: `xu_grid`, 
`yv_grid`, `line_type`, `key`, `wired_surface`, `enhanced3d` and `color`.


Example:



```maxima
(%i1) draw3d(spherical(1,a,0,2*%pi,z,0,%pi))$
```

(Figure draw_spherical)

See also: `xu_grid`, `yv_grid`, `line_type`, `key`, `wired_surface`, `enhanced3d`.

### Function: spherical_to_xyz ()

It can be given as value for the `transform_xy` option of
`plot3d`. Its effect will be to interpret the two independent
variables and the function in `plot3d` as the spherical coordinates
of a point (first, the angle with the z axis, then the angle of the xy
projection with the x axis and finally the distance from the origin) and
transform them into x, y and z coordinates.

See also: `transform_xy`, `plot3d`.

### Variable: spring_embedding_depth

Default value: 50


The number of iterations in the spring embedding graph drawing
algorithm.

### Function: staircase (F, y0, n, options, ..., ;)

Draws a staircase diagram for the sequence defined by the recurrence
relation


```maxima
y(n+1) = F(y(n))
```


$$y_{n+1} = F(y_n)$$


The interpretation and allowed values of the input parameters is the
same as for the function `evolution`. A staircase diagram consists
of a plot of the function *F(y)*, together with the line *G(y)*
`=` *y*. A vertical segment is drawn from the point (*y0*,
*y0*) on that line until the point where it intersects the function
*F*. From that point a horizontal segment is drawn until it reaches
the point (*y1*, *y1*) on the line, and the procedure is
repeated *n* times until the point (*yn*, *yn*) is
reached. The options are the same as for `plot2d`.


**Example**.



```maxima
(%i1) staircase(cos(y), 1, 11, [y, 0, 1.2]);
```

(Figure dynamics2)

See also: `evolution`, `plot2d`.

### Function: starplot (data1, data2, ..., option_1, option_2, ...)

Plots star diagrams for discrete statistical variables,
both for one or multiple samples.


*data* can be a list of outcomes representing one sample, or a 
matrix of *m* rows and *n* columns, representing *n* samples of size 
*m* each.


Available options are:



- *
*stars_colors* (default, `[]`): a list of colors for multiple samples.
When there are more samples than specified colors, the extra necessary colors 
are chosen at random. See `color` to learn more about them.
- *
*frequency* (default, `absolute`): indicates the scale of the
radii. Possible values are:  `absolute` and `relative`.
- *
*ordering* (default, `orderlessp`): possible values are `orderlessp` or `ordergreatp`,
indicating how statistical outcomes should be ordered.
- *
*sample_keys* (default, `[]`): a list with the strings to be used in the legend.
When the list length is other than 0 or the number of samples, an error message is returned.
- *
*star_center* (default, `[0,0]`): diagram’s center.
- *
*star_radius* (default, `1`): diagram’s radius.
- *
All global `draw` options, except `points_joined`, `point_type`, 
and `key`, which are internally assigned by `starplot`.
If you want to set your own values for this options or want to build
complex scenes, make use of `starplot_description`.
- *
The following local `draw` option: `line_width`.


There is also a function `wxstarplot` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Example:


Plot based on absolute frequencies.
Location and radius defined by the user. 



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

### Function: starplot_description (...)

Function `starplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

### Function: stemplot (stemplot, data, stemplot, data, option)

Plots stem and leaf diagrams.


The only available option is:



- *
*leaf_unit* (default, `1`): indicates the unit of the leaves; must be a
power of 10.


Example:



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

### Function: string_to_octets (string_to_octets, string, string_to_octets, string, encoding)

Encodes a *string* into a list of octets according to current system defaults. 
When encoding strings containing Non-US-ASCII characters 
the result depends on the platform, application and underlying Lisp.


In case the external format of the Lisp reader is equal to UTF-8 the optional 
argument *encoding* allows to set the encoding for the string to octet conversion. 
If necessary see `adjust_005fexternal_005fformat` for changing the external format. 


See `octets_005fto_005fstring` for examples and some more information.

See also: `adjust_external_format`, `octets_to_string`.

### Function: strong_components (gr)

Returns the strong components of a directed graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) t : random_tournament(4)$
(%i3) strong_components(t);
(%o3)                 [[1], [0], [2], [3]]
(%i4) vertex_out_degree(3, t);
(%o4)                           3
```

### Variable: style

The styles that will be used for the various functions or sets of data
in a 2d plot.  The word *style* must be followed by one or more
styles.  If there are more functions and data sets than the styles
given, the styles will be repeated.  Each style can be either
*lines* for line segments, *points* for isolated points,
*linespoints* for segments and points, or *dots* for small
isolated dots.  Gnuplot accepts also an *impulses* style.


Each of the styles can be enclosed inside a list with some additional
parameters.  *lines* accepts one or two numbers: the width of the
line and an integer that identifies a color.  The default color codes
are: 1: blue, 2: red, 3: magenta, 4: orange, 5: brown, 6: lime and 7:
aqua.  If you use Gnuplot with a terminal different than X11,
those colors might be different; for example, if you use the option
[*gnuplot_term*, *ps*], color index 4 will correspond to black,
instead of orange.


*points* accepts one, two, or three parameters; the first parameter
is the radius of the points, the second parameter is an integer that
selects the color, using the same code used for *lines* and the
third parameter is currently used only by Gnuplot and it corresponds
to several objects instead of points.  The default types of
objects are: 1: filled circles, 2: open circles, 3: plus signs, 4: x,
5: *, 6: filled squares, 7: open squares, 8: filled triangles, 9: open
triangles, 10: filled inverted triangles, 11: open inverted triangles,
12: filled lozenges and 13: open lozenges.


*linespoints* accepts up to five parameters: line width, points
radius, color, type of object to replace the points, and the gnuplot
pointinterval option to control space between points.


See also `color` and `point_005ftype`.

See also: `color`, `point_type`.

### Variable: surface_hide

Default value: `false`


If `surface_hide` is `true`, hidden parts are not plotted in 3d surfaces.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw(columns=2,
           gr3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)),
           gr3d(surface_hide = true,
                explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)) )$
```

(Figure draw_surface_hide)

### Variable: svg_file

Saves the plot into an SVG file with name equal to *file_name*,
rather than showing it in the screen.  By default, the file will be
created in the directory defined by the variable
`maxima_tempdir`, unless *file_name* contains the character
“/”, in which case it will be assumed to contain the complete path where
the file should be created. The value of `maxima_tempdir` can be changed
to save the file in a different directory. When the option
`gnuplot_svg_term_command` is also given, it will be used to set up
Gnuplot’s SVG terminal; otherwise, Gnuplot’s svg terminal
will be used with font of 14 points.

See also: `maxima_tempdir`, `gnuplot_svg_term_command`.

### Variable: t

Default range for parametric plots.

### Function: take_channel (im, color)

If argument *color* is `red`, `green` or `blue`,
function `take_channel` returns the corresponding color channel of
picture *im*.
Example:



```maxima
(%i1) red: make_level_picture(matrix([3,2],[7,260]));
(%o1)           picture(level, 2, 2, {Array:  #(3 2 7 255)})
(%i2) green: make_level_picture(matrix([54,23],[73,-9]));
(%o2)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
(%i3) blue: make_level_picture(matrix([123,82],[45,32.5698]));
(%o3)          picture(level, 2, 2, {Array:  #(123 82 45 33)})
(%i4) make_rgb_picture(red,green,blue);
(%o4) picture(rgb, 2, 2, 
              {Array:  #(3 54 123 2 23 82 7 73 45 255 0 33)})
(%i5) take_channel(%,'green);  /* simple quote!!! */
(%o5)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
```

### Variable: terminal

Default value: `screen`


Selects the terminal to be used by Gnuplot; possible values are:
`screen` (default), `png`, `pngcairo`, `jpg`, `gif`, 
`cairolatex_pdf`, `cairolatex_pdf_standalone`,
`eps`, `eps_color`, `epslatex`, `epslatex_standalone`, 
`svg`, `canvas`, `dumb`, `dumb_file`, `pdf`, `pdfcairo`, 
`wxt`, `animated_gif`, `multipage_pdfcairo`, `multipage_pdf`, 
`multipage_eps`, `multipage_eps_color`, `tikz`, `tikz_standalone`
and `aquaterm`.


Terminals `screen`, `wxt`, `windows` and `aquaterm` can
be also defined as a list
with two elements: the name of the terminal itself and a non negative integer number.
In this form, multiple windows can be opened at the same time, each with its
corresponding number. This feature does not work in Windows platforms.


Since this is a global graphics option, its position in the scene description
does not matter. It can be also used as an argument of function `draw`.


N.B. pdfcairo requires Gnuplot 4.3 or newer. 
`pdf` requires Gnuplot to be compiled with the option `--enable-pdf` and libpdf must
be installed. The pdf library is available from: [http://www.pdflib.com/en/download/pdflib-family/pdflib-lite/]()


Examples:



```maxima
(%i1) /* screen terminal (default) */
      draw2d(explicit(x^2,x,-1,1))$
(%i2) /* png file */
      draw2d(terminal  = 'png,
             explicit(x^2,x,-1,1))$
(%i3) /* jpg file */
      draw2d(terminal   = 'jpg,
             dimensions = [300,300],
             explicit(x^2,x,-1,1))$
(%i4) /* eps file */
      draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'eps)$
(%i5) /* pdf file */
      draw2d(file_name = "mypdf",
             dimensions = 100*[12.0,8.0],
             explicit(x^2,x,-1,1),
             terminal  = 'pdf)$
(%i6) /* wxwidgets window */
      draw2d(explicit(x^2,x,-1,1),
             terminal  = 'wxt)$
(%i7) /* tikz file */
      draw2d(explicit(x^2,x,-1,1),
             file_name = "mytikz",
             dimensions = [8,8], /* in cms */
             terminal = 'tikz)$
```


Multiple windows.


```maxima
(%i1) draw2d(explicit(x^5,x,-2,2), terminal=[screen, 3])$
(%i2) draw2d(explicit(x^2,x,-2,2), terminal=[screen, 0])$
```


An animated gif file.


```maxima
(%i1) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o1)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


Option `delay` is only active in animated gif’s; it is ignored in
any other case.


Multipage output in eps format.


```maxima
(%i1) draw(
        file_name = "parabol",
        terminal  = multipage_eps,
        dimensions = 100*[10,10],
        gr2d(explicit(x^2,x,-1,1)),
        gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1))) $
```


See also `file_name`,  `dimensions_draw` and `delay`.

See also: `file_name`, `dimensions_draw`, `delay`.

### Variable: title

Defines a title that will be written at the top of the plot.

### Function: topological_sort (dag)

Returns a topological sorting of the vertices of a directed graph
*dag* or an empty list if *dag* is not a directed acyclic graph.


Example:













```maxima
(%i1) load ("graphs")$
(%i2) g:create_graph(
         [1,2,3,4,5],
         [
          [1,2], [2,5], [5,3],
          [5,4], [3,4], [1,3]
         ],
         directed=true)$
(%i3) topological_sort(g);
(%o3)                    [1, 2, 5, 3, 4]
```

### Variable: transform

Default value: `none`


If `transform` is `none`, the space is not transformed and
graphic objects are drawn as defined. When a space transformation is
desired, a list must be assigned to option `transform`. In case of
a 2D scene, the list takes the form `[f1(x,y), f2(x,y), x, y]`.
In case of a 3D scene, the list is of the form
`[f1(x,y,z), f2(x,y,z), f3(x,y,z), x, y, z]`.


The names of the variables defined in the lists may be different to those
used in the definitions of the graphic objects.


Examples:


Rotation in 2D.



```maxima
(%i1) th : %pi / 4$
(%i2) draw2d(
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

(Figure draw_transform)


Translation in 3D.



```maxima
(%i1) draw3d(
        color     = "#a02c00",
        explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
        transform = [x+10,y+10,z+10,x,y,z],
        color     = blue,
        explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3) )$
```

### Variable: transform_xy

Where *symbol* is either `false` or the result obtained by
using the function `transform_xy`.  If different from `false`,
it will be used to transform the 3 coordinates in
plot3d. `notransform_xy` removes any transformation function
previously defined.


See `make_transform`, `polar_to_xy` and
`spherical_005fto_005fxyz`.

See also: `make_transform`, `polar_to_xy`, `spherical_to_xyz`.

### Variable: transparent

Default value: `false`


If `transparent` is `false`, interior regions of polygons are 
filled according to `fill_color`.


This option affects the following graphic objects:


- *
`gr2d`: `polygon`, `rectangle` and `ellipse`.


Example:



```maxima
(%i1) draw2d(polygon([[3,2],[7,2],[5,5]]),
             transparent = true,
             color       = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

(Figure draw_transparent)

See also: `polygon`, `rectangle`, `ellipse`.

### Function: triangle (point_1, point_2, point_3)

Draws a triangle.


**2D**


`triangle ([x1,y1], [x2,y2], [x3,y3])` draws a triangle with vertices `[x1,y1]`, `[x2,y2]`,
and `[x3,y3]`.


This object is affected by the following *graphic options*:

`transparent`, `fill_color`, `border`, `line_width`,
`key`, `xaxis_secondary`, `yaxis_secondary`, `line_type`,
`transform` and `color`.


Example:



```maxima
(%i1) draw2d(
        triangle([1,1],[2,2],[3,-1]))$
```

(Figure draw_triangle)


**3D**


`triangle ([x1,y1,z1], [x2,y2,z2], [x3,y3,z3])` draws a triangle with vertices `[x1,y1,z1]`,
`[x2,y2,z2]`, and `[x3,y3,z3]`.


This object is affected by the following *graphic options*: `line_type`, 
`line_width`, `color`, `key`, `enhanced3d` and `transform`.

See also: `transparent`, `fill_color`, `border`, `line_width`, `key`, `xaxis_secondary`, `yaxis_secondary`, `line_type`, `transform`, `color`, `enhanced3d`.

### Function: truncated_cube_graph ()

Returns the truncated cube graph.

### Function: truncated_dodecahedron_graph ()

Returns the truncated dodecahedron graph.

### Function: truncated_icosahedron_graph ()

Returns the truncated icosahedron graph.

### Function: truncated_tetrahedron_graph ()

Returns the truncated tetrahedron graph.

### Function: tube (xfun, yfun, zfun, rfun, p, pmin, pmax)

Draws a tube in 3D with varying diameter.


**3D**


`[xfun,yfun,zfun]`
is the parametric curve with parameter *p* taking values from *pmin*
to *pmax*. Circles of radius *rfun* are placed with their centers on
the parametric curve and perpendicular to it.


This object is affected by the following *graphic options*: `xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`,
`color` and `capping`.


Example:



```maxima
(%i1) draw3d(
        enhanced3d = true,
        xu_grid = 50,
        tube(cos(a), a, 0, cos(a/10)^2,
             a, 0, 4*%pi) )$
```

(Figure draw_tube)

See also: `xu_grid`, `yv_grid`, `line_type`, `line_width`, `key`, `wired_surface`, `enhanced3d`, `color`, `capping`.

### Function: tutte_graph ()

Returns the Tutte graph.

### Function: underlying_graph (g)

Returns the underlying graph of the directed graph *g*.

### Variable: unit_vectors

Default value: `false`


If `unit_vectors` is `true`, vectors are plotted with module 1.
This is useful for plotting vector fields. If `unit_vectors` is `false`,
vectors are plotted with its original length.


This option is relevant only for `vector` objects.


Example:



```maxima
(%i1) draw2d(xrange      = [-1,6],
             yrange      = [-1,6],
             head_length = 0.1,
             vector([0,0],[5,2]),
             unit_vectors = true,
             color        = red,
             vector([0,3],[5,2]))$
```

(Figure draw_unit_vectors)

### Variable: user_preamble

Default value: `""` (empty string)


Expert Gnuplot users can make use of this option to fine tune Gnuplot’s
behaviour by writing settings to be sent before the `plot` or `splot`
command.


The value of this option must be a string or a list of strings (one per line).


Since this is a global graphics option, its position in the scene description
does not matter.


Example:


Tell Gnuplot to draw axes and grid on top of graphics objects,


```maxima
(%i1) draw2d(
        xaxis =true, xaxis_type=solid,
        yaxis =true, yaxis_type=solid,
        user_preamble="set grid front",
        region(x^2+y^2<1 ,x,-1.5,1.5,y,-1.5,1.5))$
```

(Figure draw_user_preamble)


Tell gnuplot to draw all contour lines in black



```maxima
(%i1) draw3d(
          contour=both,
          surface_hide=true,enhanced3d=true,wired_surface=true,
          contour_levels=10,
          user_preamble="set for [i=1:8] linetype i dashtype i linecolor 0",
          explicit(sin(x)*cos(y),x,1,10,y,1,10)
      );
```

(Figure draw_user_preamble2)

### Function: vector (vector, x, y, dx, dy, vector, x, y, z, dx, dy, dz)

Draws vectors in 2D and 3D.


This object is affected by the following *graphic options*: `head_both`, 
`head_length`, `head_angle`, `head_type`, `line_width`, 
`line_type`, `key` and `color`.


**2D**


`vector([x,y], [dx,dy])` plots vector
`[dx,dy]` with origin in `[x,y]`.


Example:



```maxima
(%i1) draw2d(xrange      = [0,12],
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

(Figure draw_vector)


**3D**


`vector([x,y,z], [dx,dy,dz])` 
plots vector `[dx,dy,dz]` with
origin in `[x,y,z]`.


Example:



```maxima
(%i1) draw3d(color = cyan,
             vector([0,0,0],[1,1,1]/sqrt(3)),
             vector([0,0,0],[1,-1,0]/sqrt(2)),
             vector([0,0,0],[1,1,-2]/sqrt(6)) )$
```

(Figure draw_vector2)

See also: `head_both`, `head_length`, `head_angle`, `head_type`, `line_width`, `line_type`, `key`.

### Variable: vertex_color

The color used for displaying vertices.

### Function: vertex_coloring (gr)

Returns an optimal coloring of the vertices of the graph *gr*.


The function returns the chromatic number and a list representing the
coloring of the vertices of *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) p:petersen_graph()$
(%i3) vertex_coloring(p);
(%o3) [3, [[0, 2], [1, 3], [2, 2], [3, 3], [4, 1], [5, 3], 
                                 [6, 1], [7, 1], [8, 2], [9, 2]]]
```

### Function: vertex_connectivity (g)

Returns the vertex connectivity of the graph *g*.


See also `min_005fvertex_005fcut`.

See also: `min_vertex_cut`.

### Function: vertex_degree (v, gr)

Returns the degree of the vertex *v* in the graph *gr*.

### Function: vertex_distance (u, v, gr)

Returns the length of the shortest path between *u* and *v* in
the (directed) graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) d : dodecahedron_graph()$
(%i3) vertex_distance(0, 7, d);
(%o3)                           4
(%i4) shortest_path(0, 7, d);
(%o4)                   [0, 1, 19, 13, 7]
```

### Function: vertex_eccentricity (v, gr)

Returns the eccentricity of the vertex *v* in the graph *gr*.


Example:







```maxima
(%i1) load ("graphs")$
(%i2) g:cycle_graph(7)$
(%i3) vertex_eccentricity(0, g);
(%o3)                           3
```

### Function: vertex_in_degree (v, gr)

Returns the in-degree of the vertex *v* in the directed graph *gr*.


Example:









```maxima
(%i1) load ("graphs")$
(%i2) p5 : path_digraph(5)$
(%i3) print_graph(p5)$
Digraph on 5 vertices with 4 arcs.
Adjacencies:
  4 :
  3 :  4
  2 :  3
  1 :  2
  0 :  1
(%i4) vertex_in_degree(4, p5);
(%o4)                           1
(%i5) in_neighbors(4, p5);
(%o5)                          [3]
```

### Function: vertex_out_degree (v, gr)

Returns the out-degree of the vertex *v* in the directed graph *gr*.


Example:








```maxima
(%i1) load ("graphs")$
(%i2) t : random_tournament(10)$
(%i3) vertex_out_degree(0, t);
(%o3)                           2
(%i4) out_neighbors(0, t);
(%o4)                        [7, 1]
```

### Variable: vertex_partition

Default value: []


A partition `[[v1,v2,...],...,[vk,...,vn]]` of the vertices of the
graph. The vertices of each list in the partition will be drawn in a
different color.

### Variable: vertex_size

The size of vertices.

### Variable: vertex_type

Default value: *circle*


Defines how vertices are displayed. See the *point_type* option for
the `draw` package for possible values.

### Function: vertices (gr)

Returns the list of vertices in the graph *gr*.


Example:






```maxima
(%i1) load ("graphs")$
(%i2) vertices(complete_graph(4));
(%o2)                     [3, 2, 1, 0]
```

### Function: vertices_to_cycle (v_list)

Converts a list *v_list* of vertices to a list of edges of the cycle
defined by *v_list*.

### Function: vertices_to_path (v_list)

Converts a list *v_list* of vertices to a list of edges of the path
defined by *v_list*.

### Variable: view

Default value: `[60,30]`


A pair of angles, measured in degrees, indicating the view direction in a 
3D scene. The first angle is the vertical rotation around the *x* axis, in 
the range $[0, 360]$. The second one is the horizontal rotation around
the *z* axis, in the range $[0, 360]$.


If option `view` is given the value `map`, the view direction is set
to be perpendicular to the xy-plane.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(view = [170, 50],
             enhanced3d = true,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```

(Figure draw_view)


```maxima
(%i2) draw3d(view = map,
             enhanced3d = true,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```

(Figure draw_view2)

### Function: wheel_graph (n)

Returns the wheel graph on *n+1* vertices.

### Function: wiener_index (gr)

Returns the Wiener index of the graph *gr*.


Example:






```maxima
(%i2) wiener_index(dodecahedron_graph());
(%o2)                          500
```

### Variable: window

Opens the plot in window number *n*, instead of the default window
0. If window number *n* is already opened, the plot in that window
will be replaced by the current plot.

### Variable: wired_surface

Default value: `false`


Indicates whether 3D surfaces in `enhanced3d` mode show the grid joining
the points or not.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(
        enhanced3d    = [sin(x),x,y],
        wired_surface = true,
        explicit(x^2+y^2,x,-1,1,y,-1,1)) $
```

(Figure draw_wired_surface)

### Variable: x

When used as the first option in a `plot2d` command (or any of the
first two in `plot3d`), it indicates that the first independent variable
is x and it sets its range.  It can also be used again after the first
option (or after the second option in plot3d) to define the effective
horizontal domain that will be shown in the plot.

See also: `plot2d`, `plot3d`.

### Variable: x_voxel

Default value: 10


`x_voxel` is the number of voxels in the x direction to
be used by the *marching cubes algorithm* implemented
by the 3d `implicit` object. It is also used by graphic
object `region`.

See also: `region`.

### Variable: xaxis

Default value: `false`


If `xaxis` is `true`, the *x* axis is drawn.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_color = blue)$
```

(Figure draw_xaxis)


See also `xaxis_width`,  `xaxis_type` and `xaxis_005fcolor`.

See also: `xaxis_width`, `xaxis_type`, `xaxis_color`.

### Variable: xaxis_color

Default value: `"black"`


`xaxis_color` specifies the color for the *x* axis. See
`color` to know how colors are defined.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_color = red)$
```


See also `xaxis`,  `xaxis_width` and `xaxis_005ftype`.

See also: `xaxis`, `xaxis_width`, `xaxis_type`.

### Variable: xaxis_secondary

Default value: `false`


If `xaxis_secondary` is `true`, function values can be plotted with 
respect to the second *x* axis, which will be drawn on top of the scene.


Note that this is a local graphics option which only affects to 2d plots.


Example:



```maxima
(%i1) draw2d(
         key   = "Bottom x-axis",
         explicit(x+1,x,1,2),
         color = red,
         key   = "Above x-axis",
         xtics_secondary = true,
         xaxis_secondary = true,
         explicit(x^2,x,-1,1)) $
```

(Figure draw_xaxis_secondary)


See also `xrange_secondary`,  `xtics_secondary`,  `xtics_rotate_secondary`, 
`xtics_axis_secondary` and `xaxis_005fsecondary`.

See also: `xrange_secondary`, `xtics_secondary`, `xtics_rotate_secondary`, `xaxis_secondary`.

### Variable: xaxis_type

Default value: `dots`


`xaxis_type` indicates how the *x* axis is displayed; 
possible values are `solid` and `dots`


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_type  = solid)$
```


See also `xaxis`,  `xaxis_width` and `xaxis_005fcolor`.

See also: `xaxis`, `xaxis_width`, `xaxis_color`.

### Variable: xaxis_width

Default value: 1


`xaxis_width` is the width of the *x* axis.
Its value must be a positive number.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_width = 3)$
```


See also `xaxis`,  `xaxis_type` and `xaxis_005fcolor`.

See also: `xaxis`, `xaxis_type`, `xaxis_color`.

### Variable: xlabel

Specifies the *string* that will label the first axis; if this
option is not used, that label will be the name of the independent
variable, when plotting functions with `plot2d` the name of the
first variable, when plotting surfaces with `plot3d`, or the first
expression in the case of a parametric plot. `noxlabel` is equivalent
to `[xlabel, ""]`, which does not print any label on the first axis.

See also: `plot2d`, `plot3d`.

### Variable: xlabel_secondary

Default value: `""` (empty string)


Option `xlabel_secondary`, a string, is the label for the secondary *x* axis.
By default, no label is written.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(
         xaxis_secondary=true,yaxis_secondary=true,
         xtics_secondary=true,ytics_secondary=true,
         xlabel_secondary="t[s]",
         ylabel_secondary="U[V]",
         explicit(sin(t),t,0,10) )$
```

(Figure draw_ylabel_secondary)


See also `xlabel_draw`,  `ylabel_draw`,  `ylabel_secondary` and `zlabel_005fdraw`.

See also: `xlabel_draw`, `ylabel_draw`, `ylabel_secondary`, `zlabel_draw`.

### Variable: xmaxima

This is an abbreviation for `[plot_format, xmaxima]`. See
`plot_005fformat`.

See also: `plot_format`.

### Variable: xmaxima_plot_command

This variable stores the name of the command used to run the xmaxima
program when the plot format is `xmaxima`.
Its default value is "xmaxima". If the xmaxima
program is not found unless you give its complete path or if you want to
try a different version of it, you may change the value of this
variable. For instance,






```maxima
maxima
(%i1) xmaxima_plot_command: "/usr/local/bin/my_xmaxima"$
```


This variable must contain a string.


See also `gnuplot_command` and `geomview_005fcommand`.

See also: `gnuplot_command`, `geomview_command`.

### Variable: xrange

Default value: `auto`


If `xrange` is `auto`, the range for the *x* coordinate is
computed automatically.


If the user wants a specific interval for *x*, it must be given as a 
Maxima list, as in `xrange=[-2, 3]`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(xrange = [-3,5],
             explicit(x^2,x,-1,1))$
```


See also `yrange` and `zrange`.

See also: `yrange`, `zrange`.

### Variable: xrange_secondary

Default value: `auto`


If `xrange_secondary` is `auto`, the range for the second *x* axis is
computed automatically.


If the user wants a specific interval for the second *x* axis, it must be given as a 
Maxima list, as in `xrange_secondary=[-2, 3]`.


Since this is a global graphics option, its position in the scene description
does not matter.


See also `xrange`,  `yrange`,  `zrange` and `yrange_005fsecondary`.

See also: `xrange`, `yrange`, `zrange`, `yrange_secondary`.

### Variable: xtics

Defines the values at which a mark and a number will be placed in the x
axis. The first number is the initial value, the second the increments
and the third is the last value where a mark is placed. The second and
third numbers can be omitted, in which case the first number is the
increment from an initial value that will be chosen by the graphic
program. If `[xtics, false]` is used, no marks or numbers will be
shown along the x axis.


The single keyword `xtics` removes any values previously
defined, leaving it to the graphic program to decide the values to use
and `noxtics` is a synonym for `[xtics, false]`

### Variable: xtics_axis

Default value: `false`


If `xtics_axis` is `true`, tic marks and their labels are plotted just
along the *x* axis, if it is `false` tics are plotted on the border.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: xtics_rotate

Default value: `false`


If `xtics_rotate` is `true`, tic marks on the *x* axis are rotated 
90 degrees.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: xtics_rotate_secondary

Default value: `false`


If `xtics_rotate_secondary` is `true`, tic marks on the secondary *x* axis are rotated 
90 degrees.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: xtics_secondary

Default value: `auto`


This graphic option controls the way tic marks are drawn on the second *x* axis.


See `xtics_draw` for a complete description.

See also: `xtics_draw`.

### Variable: xtics_secondary_axis

Default value: `false`


If `xtics_secondary_axis` is `true`, tic marks and their labels are plotted just
along the secondary *x* axis, if it is `false` tics are plotted on the border.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: xu_grid

Default value: 30


`xu_grid` is the number of coordinates of the first variable
(`x` in explicit and `u` in parametric 3d surfaces) to 
build the grid of sample points.


This option affects the following graphic objects:


- *
`gr3d`: `explicit` and `parametric_surface`.


Example:



```maxima
(%i1) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


See also `yv_005fgrid`.

See also: `yv_grid`.

### Variable: xy_file

Default value: `""` (empty string)


`xy_file` is the name of the file where the coordinates will be saved
after clicking with the mouse button and hitting the ’x’ key. By default,
no coordinates are saved.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: xy_scale

In a 2d plot, it defines the ratio of the total size of the Window to
the size that will be used for the plot. The two numbers given as
arguments are the scale factors for the x and y axes.


This option does not change the size of the graphic window or the placement
of the graph in the window. If you want to change the aspect ratio of the
plot, it is better to use option `yx_005fratio`. For instance,
`[yx_ratio, 10]` instead of `[xy_scale, 0.1, 1]`.

See also: `yx_ratio`.

### Variable: xyplane

Default value: `false`


Allocates the xy-plane in 3D scenes. When `xyplane` is
`false`, the xy-plane is placed automatically; when it is
a real number, the xy-plane intersects the z-axis at this level.
This option has no effect in 2D scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(xyplane = %e-2,
             explicit(x^2+y^2,x,-1,1,y,-1,1))$
```

### Variable: y

When used as one of the first two options in `plot3d`, it indicates
that one of the independent variables is y and it sets its range.  Otherwise,
it defines the effective domain of the second variable that will be
shown in the plot.

See also: `plot3d`.

### Variable: y_voxel

Default value: 10


`y_voxel` is the number of voxels in the y direction to
be used by the *marching cubes algorithm* implemented
by the 3d `implicit` object. It is also used by graphic
object `region`.

See also: `region`.

### Variable: yaxis

Default value: `false`


If `yaxis` is `true`, the *y* axis is drawn.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_color = blue)$
```


See also `yaxis_width`,  `yaxis_type` and `yaxis_005fcolor`.

See also: `yaxis_width`, `yaxis_type`, `yaxis_color`.

### Variable: yaxis_color

Default value: `"black"`


`yaxis_color` specifies the color for the *y* axis. See
`color` to know how colors are defined.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_color = red)$
```


See also `yaxis`,  `yaxis_width` and `yaxis_005ftype`.

See also: `yaxis`, `yaxis_width`, `yaxis_type`.

### Variable: yaxis_secondary

Default value: `false`


If `yaxis_secondary` is `true`, function values can be plotted with 
respect to the second *y* axis, which will be drawn on the right side of the
scene.


Note that this is a local graphics option which only affects to 2d plots.


Example:



```maxima
(%i1) draw2d(
         explicit(sin(x),x,0,10),
         yaxis_secondary = true,
         ytics_secondary = true,
         color = blue,
         explicit(100*sin(x+0.1)+2,x,0,10));
```


See also `yrange_secondary`,  `ytics_secondary`,  `ytics_rotate_secondary`
and `ytics_axis_secondary`

See also: `yrange_secondary`, `ytics_secondary`, `ytics_rotate_secondary`.

### Variable: yaxis_type

Default value: `dots`


`yaxis_type` indicates how the *y* axis is displayed; 
possible values are `solid` and `dots`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_type  = solid)$
```


See also `yaxis`,  `yaxis_width` and `yaxis_005fcolor`.

See also: `yaxis`, `yaxis_width`, `yaxis_color`.

### Variable: yaxis_width

Default value: 1


`yaxis_width` is the width of the *y* axis.
Its value must be a positive number.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_width = 3)$
```


See also `yaxis`,  `yaxis_type` and `yaxis_005fcolor`.

See also: `yaxis`, `yaxis_type`, `yaxis_color`.

### Variable: ylabel

Specifies the *string* that will label the second axis; if this
option is not used, that label will be “y”, when plotting explicit
functions with `plot2d`, or the name of the second variable, when
plotting surfaces with `plot3d`, or the second expression in the
case of a parametric plot. `noylabel` is equivalent to
`[ylabel, ""]`, which does not print any label on the second axis.

See also: `plot2d`, `plot3d`.

### Variable: ylabel_secondary

Default value: `""` (empty string)


Option `ylabel_secondary`, a string, is the label for the secondary *y* axis.
By default, no label is written.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(
        key_pos=bottom_right,
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


See also `xlabel_draw`,  `xlabel_secondary`,  `ylabel_draw` and `zlabel_005fdraw`.

See also: `xlabel_draw`, `xlabel_secondary`, `ylabel_draw`, `zlabel_draw`.

### Variable: yrange

Default value: `auto`


If `yrange` is `auto`, the range for the *y* coordinate is
computed automatically.


If the user wants a specific interval for *y*, it must be given as a 
Maxima list, as in `yrange=[-2, 3]`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(yrange = [-2,3],
             explicit(x^2,x,-1,1),
             xrange = [-3,3])$
```


See also `xrange`,  `yrange_secondary` and `zrange`.

See also: `xrange`, `yrange_secondary`, `zrange`.

### Variable: yrange_secondary

Default value: `auto`


If `yrange_secondary` is `auto`, the range for the second *y* axis is
computed automatically.


If the user wants a specific interval for the second *y* axis, it must be given as a 
Maxima list, as in `yrange_secondary=[-2, 3]`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw2d(
         explicit(sin(x),x,0,10),
         yaxis_secondary = true,
         ytics_secondary = true,
         yrange = [-3, 3],
         yrange_secondary = [-20, 20],
         color = blue,
         explicit(100*sin(x+0.1)+2,x,0,10)) $
```


See also `xrange`,  `yrange` and `zrange`.

See also: `xrange`, `yrange`, `zrange`.

### Variable: ytics

Defines the values at which a mark and a number will be placed in the y
axis. The first number is the initial value, the second the increments
and the third is the last value where a mark is placed. The second and
third numbers can be omitted, in which case the first number is the
increment from an initial value that will be chosen by the graphic
program. If `[ytics, false]` is used, no marks or numbers will be
shown along the y axis.


The single keyword `ytics` removes any values previously
defined, leaving it to the graphic program to decide the values to use
and `noytics` is a synonym for `[ytics, false]`

### Variable: ytics_axis

Default value: `false`


If `ytics_axis` is `true`, tic marks and their labels are plotted just
along the *y* axis, if it is `false` tics are plotted on the border.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: ytics_rotate

Default value: `false`


If `ytics_rotate` is `true`, tic marks on the *y* axis are rotated 
90 degrees.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: ytics_rotate_secondary

Default value: `false`


If `ytics_rotate_secondary` is `true`, tic marks on the secondary *y* axis are rotated 
90 degrees.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: ytics_secondary

Default value: `auto`


This graphic option controls the way tic marks are drawn on the second *y* axis.


See `xtics` for a complete description.

### Variable: ytics_secondary_axis

Default value: `false`


If `ytics_secondary_axis` is `true`, tic marks and their labels are plotted just
along the secondary *y* axis, if it is `false` tics are plotted on the border.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: yv_grid

Default value: 30


`yv_grid` is the number of coordinates of the second variable
(`y` in explicit and `v` in parametric 3d surfaces) to 
build the grid of sample points.


This option affects the following graphic objects:


- *
`gr3d`: `explicit` and `parametric_surface`.


Example:



```maxima
(%i1) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```

(Figure draw_xugrid)


See also `xu_005fgrid`.

See also: `explicit`, `parametric_surface`, `xu_grid`.

### Variable: yx_ratio

In a 2d plot, the ratio between the vertical and the horizontal sides of
the rectangle used to make the plot. See also `same_005fxy`.

See also: `same_xy`.

### Variable: z

Used in `plot3d` to set the effective range of values of z that will be
shown in the plot.

See also: `plot3d`.

### Variable: z_voxel

Default value: 10


`z_voxel` is the number of voxels in the z direction to
be used by the *marching cubes algorithm* implemented
by the 3d `implicit` object.

### Variable: zaxis

Default value: `false`


If `zaxis` is `true`, the *z* axis is drawn in 3D plots.
This option has no effect in 2D scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_color = blue)$
```


See also `zaxis_width`,  `zaxis_type` and `zaxis_005fcolor`.

See also: `zaxis_width`, `zaxis_type`, `zaxis_color`.

### Variable: zaxis_color

Default value: `"black"`


`zaxis_color` specifies the color for the *z* axis. See
`color` to know how colors are defined. 
This option has no effect in 2D scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_color = red)$
```


See also `zaxis`,  `zaxis_width` and `zaxis_005ftype`.

See also: `zaxis`, `zaxis_width`, `zaxis_type`.

### Variable: zaxis_type

Default value: `dots`


`zaxis_type` indicates how the *z* axis is displayed; 
possible values are `solid` and `dots`.
This option has no effect in 2D scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid)$
```


See also `zaxis`,  `zaxis_width` and `zaxis_005fcolor`.

See also: `zaxis`, `zaxis_width`, `zaxis_color`.

### Variable: zaxis_width

Default value: 1


`zaxis_width` is the width of the *z* axis.
Its value must be a positive number. This option has no effect in 2D scenes.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_width = 3)$
```


See also `zaxis`,  `zaxis_type` and `zaxis_005fcolor`.

See also: `zaxis`, `zaxis_type`, `zaxis_color`.

### Variable: zlabel

Specifies the *string* that will label the third axis, when using
`plot3d`. If this option is not used, that label will be “z”,
when plotting surfaces, or the third expression in the case of a
parametric plot.  It can not be used with `set_plot_option` and it
will be ignored by `plot2d`. `nozlabel` is equivalent to
`[zlabel, ""]`, which does not print any label on the third axis.

See also: `plot3d`, `set_plot_option`, `plot2d`.

### Variable: zlabel_rotate

Default value: `"auto"`


This graphics option allows to choose if the z axis label of 3d plots is
drawn horizontal (`false`), vertical (`true`) or if maxima
automatically chooses an orientation based on the length of the label
(`auto`).


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(
          explicit(sin(x)*sin(y),x,0,10,y,0,10),
          zlabel_rotate=false
      )$
```


See also `zlabel_005fdraw`.

See also: `zlabel_draw`.

### Variable: zmin

In 3d plots, the value of z that will be at the bottom of the plot box.


The single keyword `zmin` removes any value previously
defined, leaving it to the graphic program to decide the value to use.

### Variable: zrange

Default value: `auto`


If `zrange` is `auto`, the range for the *z* coordinate is
computed automatically.


If the user wants a specific interval for *z*, it must be given as a 
Maxima list, as in `zrange=[-2, 3]`.


Since this is a global graphics option, its position in the scene description
does not matter.


Example:



```maxima
(%i1) draw3d(yrange = [-3,3],
             zrange = [-2,5],
             explicit(x^2+y^2,x,-1,1,y,-1,1),
             xrange = [-3,3])$
```


See also `xrange` and `yrange`.

See also: `xrange`, `yrange`.

### Variable: ztics

Defines the values at which a mark and a number will be placed in the z
axis. The first number is the initial value, the second the increments
and the third is the last value where a mark is placed. The second and
third numbers can be omitted, in which case the first number is the
increment from an initial value that will be chosen by the graphic
program. If `[ztics, false]` is used, no marks or numbers will be
shown along the z axis. 


The single keyword `ztics` removes any values previously
defined, leaving it to the graphic program to decide the values to use
and `noztics` is a synonym for `[ztics, false]`

### Variable: ztics_axis

Default value: `false`


If `ztics_axis` is `true`, tic marks and their labels are plotted just
along the *z* axis, if it is `false` tics are plotted on the border.


Since this is a global graphics option, its position in the scene description
does not matter.

### Variable: ztics_rotate

Default value: `false`


If `ztics_rotate` is `true`, tic marks on the *z* axis are rotated 
90 degrees.


Since this is a global graphics option, its position in the scene description
does not matter.

