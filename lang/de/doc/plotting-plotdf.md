## plotdf

<!-- category: Plotting -->
<!-- keywords: plotdf -->
<!-- signatures: plotdf(dydx, ...options...), plotdf(dvdu, [u, v], ...options...), plotdf([dxdt, dydt], ...options...), plotdf([dudt, dvdt], [u, v], ...options...) -->
### Function: plotdf (dydx, ...options...)

Displays a direction field in two dimensions *x* and *y*.


*dydx*, *dxdt* and *dydt* are expressions that depend on
*x* and *y*.  *dvdu*, *dudt* and *dvdt* are
expressions that depend on *u* and *v*.  In addition to those two
variables, the expressions can also depend on a set of parameters, with
numerical values given with the `parameters` option (the option
syntax is given below), or with a range of allowed values specified by a
*sliders* option.


Several other options can be given within the command, or selected in
the menu.  Integral curves can be obtained by clicking on the plot, or
with the option `trajectory_at`.  The direction of the integration
can be controlled with the `direction` option, which can have
values of *forward*, *backward* or *both*.  The number of
integration steps is given by `nsteps` and the time interval
between them is set up with the `tstep` option.  The Adams Moulton
method is used for the integration; it is also possible to switch to an
adaptive Runge-Kutta 4th order method.


**Plot window menu:**


The menu in the plot window has the following options: *Zoom*, will
change the behavior of the mouse so that it will allow you to zoom in on
a region of the plot by clicking with the left button.  Each click near a
point magnifies the plot, keeping the center at the point where you
clicked.  Holding the Shift key while clicking, zooms out to the
previous magnification.  To resume computing trajectories when you click
on a point, select *Integrate* from the menu.


The option *Config* in the menu can be used to change the ODE(s) in
use and various other settings.  After configuration changes are made,
the menu option *Replot* should be selected, to activate the new
settings.  If a pair of coordinates are entered in the field
*Trajectory at* in the *Config* dialog menu, and the
enter key is pressed, a new integral curve will be shown, in
addition to the ones already shown.  When *Replot* is selected, only
the last integral curve entered will be shown.


Holding the right mouse button down while the cursor is moved, can be
used to drag the plot sideways or up and down.  Additional
parameters such as the number of steps, the initial value of *t*
and the x and y centers and radii, may be set in the Config menu.


A copy of the plot can be saved as a postscript file, using the menu
option *Save*.


**Plot options:**


The `plotdf` command may include several commands, each command is
a list of two or more items.  The first item is the name of the option,
and the remainder comprises the value or values assigned to the option.


The options which are recognized by `plotdf` are the following:



- *
*tstep* defines the length of the increments on the
independent variable *t*, used to compute an integral curve.  If only
one expression *dydx* is given to `plotdf`, the *x*
variable will be directly proportional to *t*.
The default value is 0.1.
- *
*nsteps* defines the number of steps of length `tstep`
that will be used for the independent variable, to compute an integral
curve.
The default value is 100.
- *
*direction* defines the direction of the independent
variable that will be followed to compute an integral curve.  Possible
values are `forward`, to make the independent variable increase
`nsteps` times, with increments `tstep`, `backward`, to
make the independent variable decrease, or `both` that will lead to
an integral curve that extends `nsteps` forward, and `nsteps`
backward.  The keywords `right` and `left` can be used as
synonyms for `forward` and `backward`.
The default value is `both`.
- *
*tinitial* defines the initial value of variable *t* used
to compute integral curves.  Since the differential equations are
autonomous, that setting will only appear in the plot of the curves as
functions of *t*.
The default value is 0.
- *
*versus_t* is used to create a second plot window, with a
plot of an integral curve, as two functions *x*, *y*, of the
independent variable *t*.  If `versus_t` is given any value
different from 0, the second plot window will be displayed.  The second
plot window includes another menu, similar to the menu of the main plot
window.
The default value is 0.
- *
*trajectory_at* defines the coordinates *xinitial* and
*yinitial* for the starting point of an integral curve.
The option is empty by default.
- *
*parameters* defines a list of parameters, and their
numerical values, used in the definition of the differential
equations.  The name and values of the parameters must be given in a
string with a comma-separated sequence of pairs `name=value`.
- *
*sliders* defines a list of parameters that will be changed
interactively using slider buttons, and the range of variation of those
parameters.  The names and ranges of the parameters must be given in a
string with a comma-separated sequence of elements `name=min:max`
- *
*xfun* defines a string with semi-colon-separated sequence
of functions of *x* to be displayed, on top of the direction field.
Those functions will be parsed by Tcl and not by Maxima.
- *
*x* should be followed by two numbers, which will set up the minimum
and maximum values shown on the horizontal axis.  If the variable on the
horizontal axis is not *x*, then this option should have the name of
the variable on the horizontal axis.
The default horizontal range is from -10 to 10.
- *
*y* should be followed by two numbers, which will set up the minimum
and maximum values shown on the vertical axis.  If the variable on the
vertical axis is not *y*, then this option should have the name of
the variable on the vertical axis.
The default vertical range is from -10 to 10.


**Examples:**



- *
To show the direction field of the differential equation $y' = exp(-x) + y$
and the solution that goes through $(2, -0.1)$:

```maxima
(%i1) plotdf(exp(-x)+y,[trajectory_at,2,-0.1])$
```

![./figures/plotdf1](./figures/plotdf1.png)
- *
To obtain the direction field for the equation $diff(y,x) = x - y^2$ and
the solution with initial condition $y(-1) = 3$, we can use the command:

```maxima
(%i1) plotdf(x-y^2,[xfun,"sqrt(x);-sqrt(x)"],
         [trajectory_at,-1,3], [direction,forward],
         [y,-5,5], [x,-4,16])$
```

The graph also shows the function $y = sqrt(x)$.

![./figures/plotdf2](./figures/plotdf2.png)
- *
The following example shows the direction field of a harmonic oscillator,
defined by the two equations $dz/dt = v$ and $dv/dt = -k*z/m$,
and the integral curve through $(z,v) = (6,0)$, with a slider that
will allow you to change the value of $m$ interactively ($k$ is
fixed at 2):

```maxima
(%i1) plotdf([v,-k*z/m], [z,v], [parameters,"m=2,k=2"],
           [sliders,"m=1:5"], [trajectory_at,6,0])$
```

![./figures/plotdf3](./figures/plotdf3.png)
- *
To plot the direction field of the Duffing equation,
$m*x''+c*x'+k*x+b*x^3 = 0$, we introduce the variable $y=x'$ and use:

```maxima
(%i1) plotdf([y,-(k*x + c*y + b*x^3)/m],
             [parameters,"k=-1,m=1.0,c=0,b=1"],
             [sliders,"k=-2:2,m=-1:1"],[tstep,0.1])$
```

![./figures/plotdf4](./figures/plotdf4.png)
- *
The direction field for a damped pendulum, including the
solution for the given initial conditions, with a slider that
can be used to change the value of the mass $m$, and with a plot of
the two state variables as a function of time:

```maxima
(%i1) plotdf([w,-g*sin(a)/l - b*w/m/l], [a,w],
        [parameters,"g=9.8,l=0.5,m=0.3,b=0.05"],
        [trajectory_at,1.05,-9],[tstep,0.01],
        [a,-10,2], [w,-14,14], [direction,forward],
        [nsteps,300], [sliders,"m=0.1:1"], [versus_t,1])$
```

![./figures/plotdf5](./figures/plotdf5.png)![./figures/plotdf6](./figures/plotdf6.png)

