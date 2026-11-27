## dynamics

<!-- category: Plotting -->
<!-- keywords: chaosgame -->
<!-- signatures: chaosgame([[x1, y1], ..., [xm, ym]], [x0, y0], b, n, ..., options, ...) -->
### Function: chaosgame ([[x1, y1], ..., [xm, ym]], [x0, y0], b, n, ..., options, ...)

Implements the so-called chaos game: the initial point (*x0*,
*y0*) is plotted and then one of the *m* points
`[`*x1*, *y1*`]`, ..., `[`*xm*, *ym*`]`
will be selected at random.  The next point plotted will be on the
segment from the previous point plotted to the point chosen randomly, at a
distance from the random point which will be *b* times that segment’s
length.  The procedure is repeated *n* times.

<!-- category: Plotting -->
<!-- keywords: evolution -->
<!-- signatures: evolution(F, y0, n, ..., options, ...) -->
### Function: evolution (F, y0, n, ..., options, ...)

Draws *n+1* points in a two-dimensional graph, where the horizontal
coordinates of the points are the integers 0, 1, 2, ..., *n*, and
the vertical coordinates are the corresponding values *y(n)* of the
sequence defined by the recurrence relation


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


With initial value *y(0)* equal to *y0*.  *F* must be an
expression that depends only on one variable (in the example, it
depend on *y*, but any other variable can be used),
*y0* must be a real number and *n* must be a positive integer.

<!-- category: Plotting -->
<!-- keywords: evolution2d -->
<!-- signatures: evolution2d([F, G], [u, v], [u0, y0], n, ..., options, ...) -->
### Function: evolution2d ([F, G], [u, v], [u0, y0], n, ..., options, ...)

Shows, in a two-dimensional plot, the first *n+1* points in the
sequence of points defined by the two-dimensional discrete dynamical
system with recurrence relations


```maxima
u(n+1) = F(u(n), v(n))    v(n+1) = G(u(n), v(n))
```


$$
\begin{cases}u_{n+1} = F(u_n, v_n) &\cr v_{n+1} = G(u_n, v_n)\end{cases}
$$


With initial values *u0* and *v0*.  *F* and *G* must be
two expressions that depend only on two variables, *u* and
*v*, which must be named explicitely in a list.

<!-- category: Plotting -->
<!-- keywords: ifs -->
<!-- signatures: ifs([r1, ..., rm], [A1, ..., Am], [[x1, y1], ..., [xm, ym]], [x0, y0], n, ..., options, ...) -->
### Function: ifs ([r1, ..., rm], [A1, ..., Am], [[x1, y1], ..., [xm, ym]], [x0, y0], n, ..., options, ...)

Implements the Iterated Function System method.  This method is similar
to the method described in the function `chaosgame`, but instead of
shrinking the segment from the current point to the randomly chosen
point, the 2 components of that segment will be multiplied by the 2 by 2
matrix *Ai* that corresponds to the point chosen randomly.


The random choice of one of the *m* attractive points can be made with
a non-uniform probability distribution defined by the weights
*r1*, ..., *rm*.  Those weights are given in cumulative form; for 
instance if there are 3 points with probabilities 0.2, 0.5 and
0.3, the weights *r1*, *r2* and *r3* could be 2, 7 and 10.

<!-- category: Plotting -->
<!-- keywords: orbits -->
<!-- signatures: orbits(F, y0, n1, n2, [x, x0, xf, xstep], ..., options, ...) -->
### Function: orbits (F, y0, n1, n2, [x, x0, xf, xstep], ..., options, ...)

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
the sequence evolve *n1* iterations.

<!-- category: Plotting -->
<!-- keywords: rk -->
<!-- signatures: rk(ODE, var, initial, domain), rk([ODE1, ..., ODEm], [v1, ..., vm], [init1, ..., initm], domain) -->
### Function: rk (ODE, var, initial, domain)

The first form solves numerically one first-order ordinary differential
equation, and the second form solves a system of m of those equations,
using the 4th order Runge-Kutta method.  *var* represents the dependent
variable.  *ODE* must be an expression that depends only on the independent
and dependent variables and defines the derivative of the dependent
variable with respect to the independent variable.


The independent variable is specified with `domain`, which must be a
list of four elements as, for instance:


```maxima
[t, 0, 10, 0.1]
```

the first element of the list identifies the independent variable, the
second and third elements are the initial and final values for that
variable, and the last element sets the increments that should be used
within that interval.


If *m* equations are going to be solved, there should be *m*
dependent variables *v1*, *v2*, ..., *vm*.  The initial values
for those variables will be *init1*, *init2*, ..., *initm*.
There will still be just one independent variable defined by `domain`,
as in the previous case.  *ODE1*, ..., *ODEm* are the expressions
that define the derivatives of each dependent variable in
terms of the independent variable.  The only variables that may appear in
those expressions are the independent variable and any of the dependent
variables.  It is important to give the derivatives *ODE1*, ...,
*ODEm* in the list in exactly the same order used for the dependent
variables; for instance, the third element in the list will be interpreted
as the derivative of the third dependent variable.


The program will try to integrate the equations from the initial value
of the independent variable until its last value, using constant
increments.  If at some step one of the dependent variables takes an
absolute value too large, the integration will be interrupted at that
point.  The result will be a list with as many elements as the number of
iterations made.  Each element in the results list is itself another list
with *m*+1 elements: the value of the independent variable, followed
by the values of the dependent variables corresponding to that point.

<!-- category: Plotting -->
<!-- keywords: staircase -->
<!-- signatures: staircase(F, y0, n, ..., options, ...) -->
### Function: staircase (F, y0, n, ..., options, ...)

Draws a staircase diagram for the sequence defined by the recurrence
relation


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


The interpretation and allowed values of the input parameters is the
same as for the function `evolution`.  A staircase diagram consists
of a plot of the function *F(y)*, together with the line
*G(y)* `=` *y*.  A vertical segment is drawn from the
point (*y0*, *y0*) on that line until the point where it
intersects the function *F*.  From that point a horizontal segment is
drawn until it reaches the point (*y1*, *y1*) on the line, and
the procedure is repeated *n* times until the point (*yn*, *yn*)
is reached.

