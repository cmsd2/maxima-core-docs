## Differentiation

### Function: antid (expr, x, u(x))

Returns a two-element list, such that an antiderivative of *expr* with
respect to *x* can be constructed from the list.  The expression *expr*
may contain an unknown function *u* and its derivatives.


Let *L*, a list of two elements, be the return value of `antid`.
Then `L[1] + 'integrate (L[2], x)`
is an antiderivative of *expr* with respect to *x*.


When `antid` succeeds entirely,
the second element of the return value is zero.
Otherwise, the second element is nonzero,
and the first element is nonzero or zero.
If `antid` cannot make any progress,
the first element is zero and the second nonzero.


`load ("antid")` loads this function.  The `antid` package also
defines the functions `nonzeroandfreeof` and `linear`.


`antid` is related to `antidiff` as follows.
Let *L*, a list of two elements, be the return value of `antid`.
Then the return value of `antidiff` is equal to
`L[1] + 'integrate (L[2], x)` where *x* is the
variable of integration.


Examples:












```maxima
maxima
(%i1) load ("antid")$

(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                       z(x)       d
(%o2)                %e     y(x) (-- (z(x)))
                                  dx


(%i3) a1: antid (expr, x, z(x));
                  z(x)           z(x)  d
(%o3)          [%e     y(x), - %e     (-- (y(x)))]
                                       dx


(%i4) a2: antidiff (expr, x, z(x));
                            /
                z(x)        |   z(x)  d
(%o4)         %e     y(x) - | %e     (-- (y(x))) dx
                            |         dx
                            /


(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0


(%i6) antid (expr, x, y(x));
                        z(x)       d
(%o6)             [0, %e     y(x) (-- (z(x)))]
                                   dx


(%i7) antidiff (expr, x, y(x));
                  /
                  |   z(x)       d
(%o7)             | %e     y(x) (-- (z(x))) dx
                  |              dx
                  /
```

See also: `antidiff`.

### Function: antidiff (expr, x, u, x)

Returns an antiderivative of *expr* with respect to *x*.
The expression *expr* may contain an unknown function *u* and its
derivatives.


When `antidiff` succeeds entirely, the resulting expression is free of
integral signs (that is, free of the `integrate` noun).
Otherwise, `antidiff` returns an expression
which is partly or entirely within an integral sign.
If `antidiff` cannot make any progress,
the return value is entirely within an integral sign.


`load ("antid")` loads this function.
The `antid` package also defines the functions `nonzeroandfreeof` and
`linear`.


`antidiff` is related to `antid` as follows.
Let *L*, a list of two elements, be the return value of `antid`.
Then the return value of `antidiff` is equal to
`L[1] + 'integrate (L[2], x)` where *x* is the
variable of integration.


Examples:















```maxima
maxima
(%i1) load ("antid")$

(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                       z(x)       d
(%o2)                %e     y(x) (-- (z(x)))
                                  dx


(%i3) a1: antid (expr, x, z(x));
                  z(x)           z(x)  d
(%o3)          [%e     y(x), - %e     (-- (y(x)))]
                                       dx


(%i4) a2: antidiff (expr, x, z(x));
                            /
                z(x)        |   z(x)  d
(%o4)         %e     y(x) - | %e     (-- (y(x))) dx
                            |         dx
                            /


(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0


(%i6) antid (expr, x, y(x));
                        z(x)       d
(%o6)             [0, %e     y(x) (-- (z(x)))]
                                   dx


(%i7) antidiff (expr, x, y(x));
                  /
                  |   z(x)       d
(%o7)             | %e     y(x) (-- (z(x))) dx
                  |              dx
                  /
```

### Function: at (at, expr, eqn_1, ..., eqn_n, at, expr, eqn)

Evaluates the expression *expr* with the variables assuming the values as
specified for them in the list of equations `[eqn_1, ..., eqn_n]` or the single equation *eqn*.


If a subexpression depends on any of the variables for which a value is
specified but there is no `atvalue` specified and it can’t be otherwise
evaluated, then a noun form of the `at` is returned which displays in a
two-dimensional form.


`at` carries out multiple substitutions in parallel.


See also `atvalue`.  For other functions which carry out substitutions,
see also `subst` and `ev`.


Examples:










```maxima
maxima

(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a


(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1


(%i3) printprops (all, atvalue);
                                |
                  d             |
                 --- (f(@1, @2))|       = @2 + 1
                 d@1            |
                                |@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done


(%i4) diff (4*f(x, y)^2 - u(x, y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx


(%i5) at (%, [x = 0, y = 1]);
                                            |
                 2              d           |
(%o5)        16 a  - 2 u(0, 1) (-- (u(x, 1))|     )
                                dx          |
                                            |x = 0
```


Note that in the last line `y` is treated differently to `x`
as `y` isn’t used as a differentiation variable.


The difference between `subst`, `at` and `ev` can be
seen in the following example:










```maxima
maxima
(%i1) e1:I(t)=C*diff(U(t),t)$
(%i2) e2:U(t)=L*diff(I(t),t)$

(%i3) at(e1,e2);
                               |
                      d        |
(%o3)       I(t) = C (-- (U(t))|                    )
                      dt       |          d
                               |U(t) = L (-- (I(t)))
                                          dt


(%i4) subst(e2,e1);
                            d      d
(%o4)             I(t) = C (-- (L (-- (I(t)))))
                            dt     dt


(%i5) ev(e1,e2,diff);
                                  2
                                 d
(%o5)                I(t) = C L (--- (I(t)))
                                   2
                                 dt
```

See also: `atvalue`, `subst`, `ev`, `at`.

### Variable: atomgrad

`atomgrad` is the atomic gradient property of an expression.
This property is assigned by `gradef`.

### Function: atvalue (atvalue, expr, x_1, =, a_1, ..., x_m, =, a_m, c, atvalue, expr, x_1, =, a_1, c)

Assigns the value *c* to *expr* at the point `x = a`.
Typically boundary values are established by this mechanism.


*expr* is a function evaluation, `f(x_1, ..., x_m)`,
or a derivative, `diff (f(x_1, ..., x_m), x_1, n_1, ..., x_n, n_m)`


in which the function arguments explicitly appear.
*n_i* is the order of differentiation with respect to *x_i*.


The point at which the atvalue is established is given by the list of equations
`[x_1 = a_1, ..., x_m = a_m]`.
If there is a single variable *x_1*,
the sole equation may be given without enclosing it in a list.


`printprops ([f_1, f_2, ...], atvalue)` displays the atvalues
of the functions `f_1, f_2, ...` as specified by calls to
`atvalue`.  `printprops (f, atvalue)` displays the atvalues of
one function *f*.  `printprops (all, atvalue)` displays the atvalues
of all functions for which atvalues are defined.


The symbols `@1`, `@2`, ... represent the
variables *x_1*, *x_2*, ... when atvalues are displayed.


`atvalue` evaluates its arguments.
`atvalue` returns *c*, the atvalue.


See also `at`.


Examples:










```maxima
maxima

(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a


(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1


(%i3) printprops (all, atvalue);
                                |
                  d             |
                 --- (f(@1, @2))|       = @2 + 1
                 d@1            |
                                |@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done


(%i4) diff (4*f(x,y)^2 - u(x,y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx


(%i5) at (%, [x = 0, y = 1]);
                                            |
                 2              d           |
(%o5)        16 a  - 2 u(0, 1) (-- (u(x, 1))|     )
                                dx          |
                                            |x = 0
```

See also: `at`.

### Function: del (x)

`del (x)` represents the differential of the variable $x$.


`diff` returns an expression containing `del`
if an independent variable is not specified.
In this case, the return value is the so-called "total differential".


See also `diff`, `del` and `derivdegree`.


Examples:








```maxima
maxima

(%i1) diff (log (x));
                             del(x)
(%o1)                        ------
                               x


(%i2) diff (exp (x*y));
                   x y              x y
(%o2)            %e    x del(y) + %e    y del(x)


(%i3) diff (x*y*z);
(%o3)         x y del(z) + x z del(y) + y z del(x)
```

See also: `diff`, `del`, `derivdegree`.

### Function: delta (t)

The Dirac Delta function.


Currently only `laplace` knows about the `delta` function.


Example:







```maxima
maxima
(%i1) assume(a > 0)$

(%i2) laplace (delta (t - a) * sin(b*t), t, s);
                  2 %i a b        - a s - %i a b
               (%e         - 1) %e               %i
(%o2)        - ------------------------------------
                                2
```

See also: `laplace`.

### Variable: dependencies

The variable `dependencies` is the list of atoms which have functional
dependencies, assigned by `depends`, the function `dependencies`, or `gradef`.
The `dependencies` list is cumulative:
each call to `depends`, `dependencies`, or `gradef` appends additional items.
The default value of `dependencies` is `[]`.


The function `dependencies(f_1, ..., f_n)` appends *f_1*, ..., *f_n*,
to the `dependencies` list,
where *f_1*, ..., *f_n* are expressions of the form `f(x_1, ..., x_m)`,
and *x_1*, ..., *x_m* are any number of arguments.


`dependencies(f(x_1, ..., x_m))` is equivalent to `depends(f, [x_1, ..., x_m])`.


See also `depends` and `gradef`.













```maxima
maxima

(%i1) dependencies;
(%o1)                          []


(%i2) depends (foo, [bar, baz]);
(%o2)                    [foo(bar, baz)]


(%i3) depends ([g, h], [a, b, c]);
(%o3)               [g(a, b, c), h(a, b, c)]


(%i4) dependencies;
(%o4)        [foo(bar, baz), g(a, b, c), h(a, b, c)]


(%i5) dependencies (quux (x, y), mumble (u));
(%o5)                [quux(x, y), mumble(u)]


(%i6) dependencies;
(%o6) [foo(bar, baz), g(a, b, c), h(a, b, c), quux(x, y), 
                                                       mumble(u)]


(%i7) remove (quux, dependency);
(%o7)                         done


(%i8) dependencies;
(%o8)  [foo(bar, baz), g(a, b, c), h(a, b, c), mumble(u)]
```

See also: `depends`, `gradef`.

### Function: depends (f_1, x_1, ..., f_n, x_n)

Declares functional dependencies among variables for the purpose of computing
derivatives.  In the absence of declared dependence, `diff (f, x)` yields
zero.  If `depends (f, x)` is declared, `diff (f, x)` yields a
symbolic derivative (that is, a `diff` noun).


Each argument *f_1*, *x_1*, etc., can be the name of a variable or
array, or a list of names.
Every element of *f_i* (perhaps just a single element)
is declared to depend
on every element of *x_i* (perhaps just a single element).
If some *f_i* is the name of an array or contains the name of an array,
all elements of the array depend on *x_i*.


`diff` recognizes indirect dependencies established by `depends`
and applies the chain rule in these cases.


`remove (f, dependency)` removes all dependencies declared for
*f*.


`depends` returns a list of the dependencies established.
The dependencies are appended to the global variable `dependencies`.
`depends` evaluates its arguments.


`diff` is the only Maxima command which recognizes dependencies established
by `depends`.  Other functions (`integrate`, `laplace`, etc.)
only recognize dependencies explicitly represented by their arguments.
For example, `integrate` does not recognize the dependence of `f` on
`x` unless explicitly represented as `integrate (f(x), x)`.


`depends(f, [x_1, ..., x_n])` is equivalent to `dependencies(f(x_1, ..., x_n))`.


See also `diff`, `del`, `derivdegree` and
`derivabbrev`.










```maxima
maxima

(%i1) depends ([f, g], x);
(%o1)                     [f(x), g(x)]


(%i2) depends ([r, s], [u, v, w]);
(%o2)               [r(u, v, w), s(u, v, w)]


(%i3) depends (u, t);
(%o3)                        [u(t)]


(%i4) dependencies;
(%o4)      [f(x), g(x), r(u, v, w), s(u, v, w), u(t)]


(%i5) diff (r.s, u);
                         dr            ds
(%o5)                   (--) . s + r . --
                         du            du
```






```maxima
maxima

(%i1) diff (r.s, t);
(%o1)                           0
```







```maxima
maxima

(%i1) remove (r, dependency);
(%o1)                         done


(%i2) diff (r.s, t);
(%o2)                           0
```

See also: `dependencies`, `integrate`, `diff`, `del`, `derivdegree`, `derivabbrev`.

### Variable: derivabbrev

Default value: `false`


When `derivabbrev` is `true`,
symbolic derivatives (that is, `diff` nouns) are displayed as subscripts.
Otherwise, derivatives are displayed in the Leibniz notation `dy/dx`.

### Function: derivdegree (expr, y, x)

Returns the highest degree of the derivative
of the dependent variable *y* with respect to the independent variable
*x* occurring in *expr*.


Example:







```maxima
maxima

(%i1) 'diff (y, x, 2) + 'diff (y, z, 3) + 'diff (y, x) * x^2;
                         3     2
                        d y   d y    2 dy
(%o1)                   --- + --- + x  --
                          3     2      dx
                        dz    dx


(%i2) derivdegree (%, y, x);
(%o2)                           2
```

### Function: derivlist (var_1, ..., var_k)

Causes only differentiations with respect to
the indicated variables, within the `ev` command.

See also: `ev`.

### Variable: derivsubst

Default value: `false`


When `derivsubst` is `true`, a non-syntactic substitution such as
`subst (x, 'diff (y, t), 'diff (y, t, 2))` yields `'diff (x, t)`.

### Function: diff (diff, expr, x_1, n_1, ..., x_m, n_m, diff, expr, x, n, diff, expr, x, diff, expr)

Returns the derivative or differential of *expr* with respect to some or
all variables in *expr*.


`diff (expr, x, n)` returns the *n*’th derivative of
*expr* with respect to *x*.


`diff (expr, x_1, n_1, ..., x_m, n_m)`
returns the mixed partial derivative of *expr* with respect to *x_1*, 
..., *x_m*.  It is equivalent to `diff (... (diff (expr, x_m, n_m) ...), x_1, n_1)`.


`diff (expr, x)`
returns the first derivative of *expr* with respect to
the variable *x*.


`diff (expr)` returns the total differential of *expr*, that is,
the sum of the derivatives of *expr* with respect to each its variables
times the differential `del` of each variable.

No further simplification of `del` is offered.


The noun form of `diff` is required in some contexts,
such as stating a differential equation.
In these cases, `diff` may be quoted (as `'diff`) to yield the noun
form instead of carrying out the differentiation.


When `derivabbrev` is `true`, derivatives are displayed as subscripts.
Otherwise, derivatives are displayed in the Leibniz notation, `dy/dx`.


See also `depends`, `del`, `derivdegree`, `derivabbrev`, and `gradef`.


Examples:









```maxima
maxima

(%i1) diff (exp (f(x)), x, 2);
                     2
              f(x)  d               f(x)  d         2
(%o1)       %e     (--- (f(x))) + %e     (-- (f(x)))
                      2                   dx
                    dx

(%i2) derivabbrev: true$

(%i3) 'integrate (f(x, y), y, g(x), h(x));
                         h(x)
                        /
                        |
(%o3)                   |     f(x, y) dy
                        |
                        /
                         g(x)


(%i4) diff (%, x);
       h(x)
      /
      |
(%o4) |     (f(x, y))  dy + f(x, h(x)) (h(x))
      |              x                       x
      /
       g(x)
                                             - f(x, g(x)) (g(x))
                                                                x
```


For the tensor package, the following modifications have been
incorporated:


(1) The derivatives of any indexed objects in *expr* will have the
variables *x_i* appended as additional arguments.  Then all the
derivative indices will be sorted.


(2) The *x_i* may be integers from 1 up to the value of the variable
`dimension` [default value: 4].  This will cause the differentiation to be
carried out with respect to the *x_i*’th member of the list
`coordinates` which should be set to a list of the names of the
coordinates, e.g., `[x, y, z, t]`. If `coordinates` is bound to an
atomic variable, then that variable subscripted by *x_i* will be used for
the variable of differentiation.  This permits an array of coordinate names or
subscripted names like `X[1]`, `X[2]`, ... to be used.  If
`coordinates` has not been assigned a value, then the variables will be
treated as in (1) above.

See also: `depends`, `del`, `derivdegree`, `derivabbrev`, `gradef`.

### Function: express (expr)

Expands differential operator nouns into expressions in terms of partial
derivatives.  `express` recognizes the operators `grad`, `div`,
`curl`, `laplacian`.  `express` also expands the cross product
`~`.


Symbolic derivatives (that is, `diff` nouns)
in the return value of express may be evaluated by including `diff`
in the `ev` function call or command line.
In this context, `diff` acts as an `evfun`.


`load ("vect")` loads this function.



Examples:




















```maxima
maxima
(%i1) load ("vect")$

(%i2) grad (x^2 + y^2 + z^2);
                              2    2    2
(%o2)                  grad (z  + y  + x )


(%i3) express (%);
       d    2    2    2   d    2    2    2   d    2    2    2
(%o3) [-- (z  + y  + x ), -- (z  + y  + x ), -- (z  + y  + x )]
       dx                 dy                 dz


(%i4) ev (%, diff);
(%o4)                    [2 x, 2 y, 2 z]


(%i5) div ([x^2, y^2, z^2]);
                              2   2   2
(%o5)                   div [x , y , z ]


(%i6) express (%);
                   d    2    d    2    d    2
(%o6)              -- (z ) + -- (y ) + -- (x )
                   dz        dy        dx


(%i7) ev (%, diff);
(%o7)                    2 z + 2 y + 2 x


(%i8) curl ([x^2, y^2, z^2]);
                               2   2   2
(%o8)                   curl [x , y , z ]


(%i9) express (%);
       d    2    d    2   d    2    d    2   d    2    d    2
(%o9) [-- (z ) - -- (y ), -- (x ) - -- (z ), -- (y ) - -- (x )]
       dy        dz       dz        dx       dx        dy


(%i10) ev (%, diff);
(%o10)                      [0, 0, 0]


(%i11) laplacian (x^2 * y^2 * z^2);
                                  2  2  2
(%o11)                laplacian (x  y  z )


(%i12) express (%);
         2                2                2
        d     2  2  2    d     2  2  2    d     2  2  2
(%o12)  --- (x  y  z ) + --- (x  y  z ) + --- (x  y  z )
          2                2                2
        dz               dy               dx


(%i13) ev (%, diff);
                      2  2      2  2      2  2
(%o13)             2 y  z  + 2 x  z  + 2 x  y


(%i14) [a, b, c] ~ [x, y, z];
(%o14)                [a, b, c] ~ [x, y, z]


(%i15) express (%);
(%o15)          [b z - c y, c x - a z, a y - b x]
```

See also: `~`, `diff`, `evfun`.

### Function: gradef (gradef, f, x_1, ..., x_n, g_1, ..., g_m, gradef, a, x, expr)

Defines the partial derivatives (i.e., the components of the gradient) of the
function *f* or variable *a*.


`gradef (f(x_1, ..., x_n), g_1, ..., g_m)`
defines `df/dx_i` as *g_i*, where *g_i* is an
expression; *g_i* may be a function call, but not the name of a function.
The number of partial derivatives *m* may be less than the number of
arguments *n*, in which case derivatives are defined with respect to
*x_1* through *x_m* only.


`gradef (a, x, expr)` defines the derivative of variable
*a* with respect to *x* as *expr*.  This also establishes the
dependence of *a* on *x* (via `depends (a, x)`).


The first argument `f(x_1, ..., x_n)` or *a* is
quoted, but the remaining arguments *g_1*, ..., *g_m* are evaluated.
`gradef` returns the function or variable for which the partial derivatives
are defined.


`gradef` can redefine the derivatives of Maxima’s built-in functions.
For example, `gradef (sin(x), sqrt (1 - sin(x)^2))` redefines the
derivative of `sin`.


`gradef` cannot define partial derivatives for a subscripted function.


`printprops ([f_1, ..., f_n], gradef)` displays the partial
derivatives of the functions *f_1*, ..., *f_n*, as defined by
`gradef`.


`printprops ([a_n, ..., a_n], atomgrad)` displays the partial
derivatives of the variables *a_n*, ..., *a_n*, as defined by
`gradef`.


`gradefs` is the list of the functions
for which partial derivatives have been defined by `gradef`.
`gradefs` does not include any variables
for which partial derivatives have been defined by `gradef`.



Gradients are needed when, for example, a function is not known
explicitly but its first derivatives are and it is desired to obtain
higher order derivatives.

### Variable: gradefs

Default value: `[]`


`gradefs` is the list of the functions
for which partial derivatives have been defined by `gradef`.
`gradefs` does not include any variables
for which partial derivatives have been defined by `gradef`.

