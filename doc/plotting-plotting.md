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

### Function: get_plot_option (keyword, index)

Returns the current default value of the option named *keyword*,
which is a list. The optional argument *index* must be a positive
integer which can be used to extract only one element from the list
(element 1 is the name of the option).


See also `set_plot_option`, `remove_plot_option` and the
section on `Plotting-Options`.

See also: `set_plot_option`, `remove_plot_option`, `Plotting-Options`.

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

### Variable: label

Writes one or several labels in the points with *x*, *y*
coordinates indicated after each label.

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

### Variable: logx

Default value: `false`


Makes the horizontal axes to be scaled logarithmically. It can be either
true or false. The single keywords `logx` and `nologx` can be
used as synonyms for `[logx, true]` and `[logx, false]`.

### Variable: logy

Default value: `false`


Makes the vertical axes to be scaled logarithmically. It can be either
true or false.
The single keywords `logy` and `nology` can be used as
synonyms for `[logy, true]` and `[logy, false]`.

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

### Variable: nticks

Default value: `29`


When plotting functions with `plot2d`, it is gives the initial
number of points used by the adaptive plotting routine for plotting
functions. When plotting parametric functions with `plot3d`,
it sets the number of points that will be shown for the plot.

See also: `plot2d`, `plot3d`.

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

### Variable: point_type

In gnuplot, each set of points to be plotted with the style “points”
or “linespoints” will be represented with objects taken from this
list, in sequential order.  If there are more sets of points than objects
in this list, they will be repeated sequentially.
The possible objects that can be used are: `bullet`, `circle`,
`plus`, `times`, `asterisk`, `box`, `square`,
`triangle`, `delta`, `wedge`, `nabla`, `diamond`,
`lozenge`.

### Function: polar_to_xy ()

It can be given as value for the `transform_xy` option of
plot3d.  Its effect will be to interpret the two independent variables in
plot3d as the distance from the z axis and the azimuthal angle (polar
coordinates), and transform them into x and y coordinates.

See also: `transform_xy`.

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

### Function: remove_plot_option (name)

Removes the global value of an option. The name of the option must be given.


See also `set_plot_option`, `get_plot_option` and
`Plotting Options`.

See also: `set_plot_option`, `get_plot_option`, `Plotting-Options`.

### Function: reset_plot_options ()

Sets the default global values of the plotting options. After changing
the global values of some plotting options, this function is used to
recovered the same values as when Maxima was started.

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

### Function: spherical_to_xyz ()

It can be given as value for the `transform_xy` option of
`plot3d`. Its effect will be to interpret the two independent
variables and the function in `plot3d` as the spherical coordinates
of a point (first, the angle with the z axis, then the angle of the xy
projection with the x axis and finally the distance from the origin) and
transform them into x, y and z coordinates.

See also: `transform_xy`, `plot3d`.

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

### Variable: title

Defines a title that will be written at the top of the plot.

### Variable: transform_xy

Where *symbol* is either `false` or the result obtained by
using the function `transform_xy`.  If different from `false`,
it will be used to transform the 3 coordinates in
plot3d. `notransform_xy` removes any transformation function
previously defined.


See `make_transform`, `polar_to_xy` and
`spherical_005fto_005fxyz`.

See also: `make_transform`, `polar_to_xy`, `spherical_to_xyz`.

### Variable: window

Opens the plot in window number *n*, instead of the default window
0. If window number *n* is already opened, the plot in that window
will be replaced by the current plot.

### Variable: x

When used as the first option in a `plot2d` command (or any of the
first two in `plot3d`), it indicates that the first independent variable
is x and it sets its range.  It can also be used again after the first
option (or after the second option in plot3d) to define the effective
horizontal domain that will be shown in the plot.

See also: `plot2d`, `plot3d`.

### Variable: xlabel

Specifies the *string* that will label the first axis; if this
option is not used, that label will be the name of the independent
variable, when plotting functions with `plot2d` the name of the
first variable, when plotting surfaces with `plot3d`, or the first
expression in the case of a parametric plot. `noxlabel` is equivalent
to `[xlabel, ""]`, which does not print any label on the first axis.

See also: `plot2d`, `plot3d`.

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

### Variable: xy_scale

In a 2d plot, it defines the ratio of the total size of the Window to
the size that will be used for the plot. The two numbers given as
arguments are the scale factors for the x and y axes.


This option does not change the size of the graphic window or the placement
of the graph in the window. If you want to change the aspect ratio of the
plot, it is better to use option `yx_005fratio`. For instance,
`[yx_ratio, 10]` instead of `[xy_scale, 0.1, 1]`.

See also: `yx_ratio`.

### Variable: y

When used as one of the first two options in `plot3d`, it indicates
that one of the independent variables is y and it sets its range.  Otherwise,
it defines the effective domain of the second variable that will be
shown in the plot.

See also: `plot3d`.

### Variable: ylabel

Specifies the *string* that will label the second axis; if this
option is not used, that label will be “y”, when plotting explicit
functions with `plot2d`, or the name of the second variable, when
plotting surfaces with `plot3d`, or the second expression in the
case of a parametric plot. `noylabel` is equivalent to
`[ylabel, ""]`, which does not print any label on the second axis.

See also: `plot2d`, `plot3d`.

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

### Variable: yx_ratio

In a 2d plot, the ratio between the vertical and the horizontal sides of
the rectangle used to make the plot. See also `same_005fxy`.

See also: `same_xy`.

### Variable: z

Used in `plot3d` to set the effective range of values of z that will be
shown in the plot.

See also: `plot3d`.

### Variable: zlabel

Specifies the *string* that will label the third axis, when using
`plot3d`. If this option is not used, that label will be “z”,
when plotting surfaces, or the third expression in the case of a
parametric plot.  It can not be used with `set_plot_option` and it
will be ignored by `plot2d`. `nozlabel` is equivalent to
`[zlabel, ""]`, which does not print any label on the third axis.

See also: `plot3d`, `set_plot_option`, `plot2d`.

### Variable: zmin

In 3d plots, the value of z that will be at the bottom of the plot box.


The single keyword `zmin` removes any value previously
defined, leaving it to the graphic program to decide the value to use.

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

