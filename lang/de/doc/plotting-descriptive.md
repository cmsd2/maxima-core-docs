## descriptive

<!-- category: Plotting -->
<!-- keywords: barsplot, barsplot_description -->
<!-- signatures: barsplot(data1, data2, ..., option_1, option_2, ...), barsplot_description(...) -->
### Function: barsplot (data1, data2, ..., option_1, option_2, ...)

Plots bars diagrams for discrete statistical variables, both for one or
multiple samples.


*data* can be a list of outcomes representing one sample, or a matrix of
*m* rows and *n* columns, representing *n* samples of size *m*
each.


Available options are:



- *
*box_width* (default, `3/4`): relative width of rectangles.  This 
value must be in the range `[0,1]`.
- *
*grouping* (default, `clustered`): indicates how multiple samples are
shown.  Valid values are: `clustered` and `stacked`.
- *
*groups_gap* (default, `1`): a positive integer number representing 
the gap between two consecutive groups of bars.
- *
*bars_colors* (default, `[]`): a list of colors for multiple samples.
When there are more samples than specified colors, the extra necesary colors 
are chosen at random.  See `color_graphic_option` to learn more
about them.
- *
*frequency* (default, `absolute`): indicates the scale of the
ordinates.  Possible values are:  `absolute`, `relative`, 
and `percent`.
- *
*ordering* (default, `orderlessp`): possible values are
`orderlessp` or `ordergreatp`, indicating how statistical outcomes
should be ordered on the `x`-axis.
- *
*sample_keys* (default, `[]`): a list with the strings to be used in
the legend.  When the list length is other than `0` or the number of
samples, an error message is returned.
- *
*start_at* (default, `0`): indicates where the plot begins to be
plotted on the `x`-axis.
- *
All global `draw` options, except `xtics`, which is 
internally assigned by `barsplot`.
If you want to set your own values for this option or want to build
complex scenes, make use of `barsplot_description`.  See example below.
- *
The following local `draw` options: `key`, `color`, 
`fill_color`, `fill_density` and `line_width`.  See also
`bars`.


Function `barsplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.  There is also a function `wxbarsplot` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Examples:


Univariate sample in matrix form.  Absolute frequencies.



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


Two samples of different sizes, with relative frequencies and user declared
colors.



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


Four non numeric samples of equal size.



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


Stacked bars.



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


`barsplot` in a multiplot context.



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


For bars diagrams related options, see `bars` of package `draw`.
See also functions `histogram` and `piechart`.

See also: `color_graphic_option`, `bars`, `histogram`, `piechart`.

<!-- category: Plotting -->
<!-- keywords: boxplot, boxplot_description -->
<!-- signatures: boxplot(data), boxplot(data, option_1, option_2, ...), boxplot_description(...) -->
### Function: boxplot (data)

This function plots box-and-whishker diagrams.  Argument *data* can be a
list, which is not of great interest, since these diagrams are mainly used for
comparing different samples, or a matrix, so it is possible to compare
two or more components of a multivariate statistical variable.
But it is also allowed *data* to be a list of samples with 
possible different sample sizes, in fact this is the only function 
in package `descriptive` that admits this type of data structure.


Available options are:



- *
*box_width* (default, `3/4`): relative width of boxes.
This value must be in the range `[0,1]`.
- *
*box_orientation* (default, `vertical`): possible values:
`vertical` and `horizontal`.
- *
All `draw` options, except `points_joined`, `point_size`,
`point_type`, `xtics`, `ytics`, `xrange`, and `yrange`,
which are internally assigned by `boxplot`.
If you want to set your own values for this options or want to build
complex scenes, make use of `boxplot_description`.
- *
The following local `draw` options: `key`, `color`, 
and `line_width`.


Function `boxplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.  There is also a function `wxboxplot` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Examples:


Box-and-whishker diagram from a multivariate sample.



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


Box-and-whishker diagram from three samples of different sizes.



```maxima
(%i1) load ("descriptive")$

(%i2) A :
       [[6, 4, 6, 2, 4, 8, 6, 4, 6, 4, 3, 2],
        [8, 10, 7, 9, 12, 8, 10],
        [16, 13, 17, 12, 11, 18, 13, 18, 14, 12]]$

(%i3) boxplot (A, box_orientation = horizontal)$
```

<!-- category: Plotting -->
<!-- keywords: histogram, histogram_description -->
<!-- signatures: histogram(list), histogram(list, option_1, option_2, ...), histogram(one_column_matrix), histogram(one_column_matrix, option_1, option_2, ...), histogram(one_row_matrix), histogram(one_row_matrix, option_1, option_2, ...), histogram_description(...) -->
### Function: histogram (list)

This function plots an histogram from a continuous sample.
Sample data must be stored in a list of numbers or an one dimensional matrix.


Available options are:



- *
*nclasses* (default, `10`): number of classes of the histogram, or
a list indicating the limits of the classes and the number of them, or
only the limits.
- *
*frequency* (default, `absolute`): indicates the scale of the
ordinates.  Possible values are:  `absolute`, `relative`, 
and `percent`.
- *
*htics* (default, `auto`): format of the histogram tics.  Possible
values are: `auto`, `endpoints`, `intervals`, or a list
of labels.
- *
All global `draw` options, except `xrange`, `yrange`, 
and `xtics`, which are internally assigned by `histogram`.
If you want to set your own values for these options, make use of 
`histogram_description`.  See examples bellow.
- *
The following local `draw` options: `key`, `color`, 
`fill_color`, `fill_density` and `line_width`.  See also
`bars`.


Function `histogram_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.  There is also a function `wxhistogram` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Examples:


A simple with eight classes:



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


We make use of `histogram_description` for setting 
the `xrange` and adding an explicit curve into the scene:



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
          frequency    = relative,
          fill_density = 0.5),
        explicit(pdf_normal(x,m,s), x, m - 3*s, m + 3* s))$
```

<!-- category: Plotting -->
<!-- keywords: piechart, piechart_description -->
<!-- signatures: piechart(list), piechart(list, option_1, option_2, ...), piechart(one_column_matrix), piechart(one_column_matrix, option_1, option_2, ...), piechart(one_row_matrix), piechart(one_row_matrix, option_1, option_2, ...), piechart_description(...) -->
### Function: piechart (list)

Similar to `barsplot`, but plots sectors instead of rectangles.


Available options are:



- *
*sector_colors* (default, `[]`): a list of colors for sectors.
When there are more sectors than specified colors, the extra necesary colors 
are chosen at random.  See `color_graphic_option` to learn more
about them.
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
`fill_density` and `line_width`.  See also
`ellipse`.


Function `piechart_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.  There is also a function `wxpiechart` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) piechart(
        s1,
        xrange  = [-1.1, 1.3],
        yrange  = [-1.1, 1.1],
        title   = "Digit frequencies in pi")$
```


See also function `barsplot`.

See also: `barsplot`, `color_graphic_option`, `ellipse`.

<!-- category: Plotting -->
<!-- keywords: scatterplot, scatterplot_description -->
<!-- signatures: scatterplot(list), scatterplot(list, option_1, option_2, ...), scatterplot(matrix), scatterplot(matrix, option_1, option_2, ...), scatterplot_description(...) -->
### Function: scatterplot (list)

Plots scatter diagrams both for univariate (*list*) and multivariate 
(*matrix*) samples.


Available options are the same admitted by `histogram`.


Function `scatterplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.  There is also a function `wxscatterplot` for 
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
see `points`.  See also `histogram`.

See also: `histogram`, `points`.

<!-- category: Plotting -->
<!-- keywords: starplot, starplot_description -->
<!-- signatures: starplot(data1, data2, ..., option_1, option_2, ...), starplot_description(...) -->
### Function: starplot (data1, data2, ..., option_1, option_2, ...)

Plots star diagrams for discrete statistical variables, both for one or
multiple samples.


*data* can be a list of outcomes representing one sample, or a matrix of
*m* rows and *n* columns, representing *n* samples of size *m*
each.


Available options are:



- *
*stars_colors* (default, `[]`): a list of colors for multiple samples.
When there are more samples than specified colors, the extra necesary colors 
are chosen at random.  See `color_graphic_option` to learn more
about them.
- *
*frequency* (default, `absolute`): indicates the scale of the
radii.  Possible values are: `absolute` and `relative`.
- *
*ordering* (default, `orderlessp`): possible values are
`orderlessp` or `ordergreatp`, indicating how statistical outcomes
should be ordered.
- *
*sample_keys* (default, `[]`): a list with the strings to be used in
the legend.  When the list length is other than 0 or the number of samples, an
error message is returned.
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


Function `starplot_description` creates a graphic object
suitable for creating complex scenes, together with other
graphic objects.  There is also a function `wxstarplot` for 
creating embedded histograms in interfaces wxMaxima and iMaxima.


Example:


Plot based on absolute frequencies.  Location and radius defined by the user.



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

See also: `color_graphic_option`.

<!-- category: Plotting -->
<!-- keywords: stemplot -->
<!-- signatures: stemplot(data), stemplot(data, option) -->
### Function: stemplot (data)

Plots stem and leaf diagrams.  Unique available option is:



- *
*leaf_unit* (default, `1`): indicates the unit of the leaves;
must be a power of `10`.


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

