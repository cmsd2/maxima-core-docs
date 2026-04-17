## descriptive

<!-- category: Plotting -->
<!-- keywords: barsplot -->
<!-- signatures: barsplot(data1, data2, ..., option_1, option_2, ...) -->
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

<!-- category: Plotting -->
<!-- keywords: barsplot_description -->
<!-- signatures: barsplot_description(...) -->
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

<!-- category: Plotting -->
<!-- keywords: boxplot -->
<!-- signatures: boxplot(data), boxplot(data, option_1, option_2, ...) -->
### Function: boxplot (data)

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

<!-- category: Plotting -->
<!-- keywords: boxplot_description -->
<!-- signatures: boxplot_description(...) -->
### Function: boxplot_description (...)

Function `boxplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

<!-- category: Plotting -->
<!-- keywords: histogram -->
<!-- signatures: histogram(list), histogram(list, option_1, option_2, ...), histogram(one_column_matrix), histogram(one_column_matrix, option_1, option_2, ...), histogram(one_row_matrix), histogram(one_row_matrix, option_1, option_2, ...) -->
### Function: histogram (list)

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

<!-- category: Plotting -->
<!-- keywords: histogram_description -->
<!-- signatures: histogram_description(...) -->
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

<!-- category: Plotting -->
<!-- keywords: histogram_skyline -->
<!-- signatures: histogram_skyline -->
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

<!-- category: Plotting -->
<!-- keywords: piechart -->
<!-- signatures: piechart(list), piechart(list, option_1, option_2, ...), piechart(one_column_matrix), piechart(one_column_matrix, option_1, option_2, ...), piechart(one_row_matrix), piechart(one_row_matrix, option_1, option_2, ...) -->
### Function: piechart (list)

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

<!-- category: Plotting -->
<!-- keywords: piechart_description -->
<!-- signatures: piechart_description(...) -->
### Function: piechart_description (...)

Function `piechart_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

<!-- category: Plotting -->
<!-- keywords: scatterplot -->
<!-- signatures: scatterplot(list), scatterplot(list, option_1, option_2, ...), scatterplot(matrix), scatterplot(matrix, option_1, option_2, ...) -->
### Function: scatterplot (list)

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

<!-- category: Plotting -->
<!-- keywords: scatterplot_description -->
<!-- signatures: scatterplot_description(...) -->
### Function: scatterplot_description (...)

Function `scatterplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

<!-- category: Plotting -->
<!-- keywords: starplot -->
<!-- signatures: starplot(data1, data2, ..., option_1, option_2, ...) -->
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

<!-- category: Plotting -->
<!-- keywords: starplot_description -->
<!-- signatures: starplot_description(...) -->
### Function: starplot_description (...)

Function `starplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.

<!-- category: Plotting -->
<!-- keywords: stemplot -->
<!-- signatures: stemplot(data), stemplot(data, option) -->
### Function: stemplot (data)

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

