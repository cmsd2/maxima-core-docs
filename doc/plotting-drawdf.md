## drawdf

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

