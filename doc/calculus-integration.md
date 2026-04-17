## Integration

<!-- category: Calculus -->
<!-- keywords: at_difference -->
<!-- signatures: at_difference(expr, x, a, b) -->
### Function: at_difference (expr, x, a, b)

Returns the difference of *expr* evaluated with *x* equal to *b*
minus *expr* evaluated with *x* equal to *a*.


Noun expressions `'at_difference(expr, x, a, b)`
are displayed with a vertical bar.
This is a conventional way to represent the value of a definite integral in some contexts.


When *expr* is an antiderivative of some function, say *f*,
`at_difference` is the value of the integral of *f* with respect to *x*
over the interval from *a* to *b*,
assuming that *expr* is a continuous function of *x* on that interval.


Examples:


`at_difference` returns the difference of *expr* evaluated with *x* equal to *b*
minus *expr* evaluated with *x* equal to *a*.






```maxima
maxima

(%i1) at_difference (sin(u), u, 2, w);
(%o1)                    sin(w) - sin(2)
```


Noun expressions `'at_difference(...)` are displayed with a vertical bar.






```maxima
maxima

(%i1) 'at_difference (sin(u), u, 2, w);
                                |u = w
(%o1)                     sin(u)|
                                |u = 2
```


When *expr* is an antiderivative of some function, say *f*,
`at_difference` is the value of the integral of *f* with respect to *x*
over the interval from *a* to *b*,
assuming that *expr* is a continuous function of *x* on that interval.







```maxima
maxima

(%i1) 'integrate (cos(u), u, 3, 5) = 'at_difference (integrate (cos(u), u), u, 3, 5);
                    5
                   /
                   |                    |u = 5
(%o1)              |  cos(u) du = sin(u)|
                   |                    |u = 3
                   /
                    3


(%i2) ev (%, at_difference);
                  5
                 /
                 |
(%o2)            |  cos(u) du = sin(5) - sin(3)
                 |
                 /
                  3
```

<!-- category: Calculus -->
<!-- keywords: changevar -->
<!-- signatures: changevar(expr, f(x,y), y, x) -->
### Function: changevar (expr, f(x,y), y, x)

Makes the change of variable given by `f(x,y) = 0` in all integrals
occurring in *expr* with integration with respect to *x*.
The new variable is *y*.


The change of variable can also be written `f(x) = g(y)`.









```maxima
maxima
(%i1) assume(a > 0)$

(%i2) 'integrate (%e**sqrt(a*y), y, 0, 4);
                      4
                     /
                     |    sqrt(a) sqrt(y)
(%o2)                |  %e                dy
                     |
                     /
                      0


(%i3) changevar (%, y-z^2/a, z, y);
                      0
                     /
                     |              abs(z)
                   2 |            %e       z dz
                     |
                     /
                      - 2 sqrt(a)
(%o3)            - ----------------------------
                                a
```


An expression containing a noun form, such as the instances of `'integrate`
above, may be evaluated by `ev` with the `nouns` flag.
For example, the expression returned by `changevar` above may be evaluated
by `ev (%o3, nouns)`.


`changevar` may also be used to make changes in the indices of a sum or
product.  However, it must be realized that when a change is made in a
sum or product, this change must be a shift, i.e., `i = j+ ...`, not a
higher degree function.  E.g.,







```maxima
maxima

(%i1) sum (a[i]*x^(i-2), i, 0, inf);
                         inf
                         ____
                         \         i - 2
(%o1)                     >    a  x
                         /      i
                         ----
                         i = 0


(%i2) changevar (%, i-2-n, n, i);
                        inf
                        ____
                        \               n
(%o2)                    >      a      x
                        /        n + 2
                        ----
                        n = - 2
```

<!-- category: Calculus -->
<!-- keywords: dblint -->
<!-- signatures: dblint(f, r, s, a, b) -->
### Function: dblint (f, r, s, a, b)

A double-integral routine which was written in
top-level Maxima and then translated and compiled to machine code.
Use `load ("dblint")` to access this package.  It uses the Simpson’s rule
method in both the x and y directions to calculate



$$\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx$$


$$\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx
$$



The function *f* must be a translated or compiled function of two variables,
and *r* and *s* must each be a translated or compiled function of one
variable, while *a* and *b* must be floating point numbers.  The routine
has two global variables which determine the number of divisions of the x and y
intervals: `dblint_x` and `dblint_y`, both of which are initially 10,
and can be changed independently to other integer values (there are
`2*dblint_x+1` points computed in the x direction, and `2*dblint_y+1`
in the y direction).  The routine subdivides the X axis and then for each value
of X it first computes `r(x)` and `s(x)`; then the Y axis
between `r(x)` and `s(x)` is subdivided and the integral
along the Y axis is performed using Simpson’s rule; then the integral along the
X axis is done using Simpson’s rule with the function values being the
Y-integrals.  This procedure may be numerically unstable for a great variety of
reasons, but is reasonably fast: avoid using it on highly oscillatory functions
and functions with singularities (poles or branch points in the region).  The Y
integrals depend on how far apart `r(x)` and `s(x)` are,
so if the distance `s(x) - r(x)` varies rapidly with X, there
may be substantial errors arising from truncation with different step-sizes in
the various Y integrals.  One can increase `dblint_x` and `dblint_y`
in an effort to improve the coverage of the region, at the expense of
computation time.  The function values are not saved, so if the function is very
time-consuming, you will have to wait for re-computation if you change anything
(sorry).  It is required that the functions *f*, *r*, and *s* be
either translated or compiled prior to calling `dblint`.  This will result
in orders of magnitude speed improvement over interpreted code in many cases!


`demo ("dblint")` executes a demonstration of `dblint` applied to an
example problem.

<!-- category: Calculus -->
<!-- keywords: defint -->
<!-- signatures: defint(expr, x, a, b) -->
### Function: defint (expr, x, a, b)

Attempts to compute a definite integral.  `defint` is called by
`integrate` when limits of integration are specified, i.e., when
`integrate` is called as
`integrate (expr, x, a, b)`.
Thus from the user’s point of view, it is sufficient to call `integrate`.



`defint` returns a symbolic expression, either the computed integral or the
noun form of the integral.  See `quad_qag` and related functions for
numerical approximation of definite integrals.

See also: `quad_qag`.

<!-- category: Calculus -->
<!-- keywords: erfflag -->
<!-- signatures: erfflag -->
### Variable: erfflag

Default value: `true`


When `erfflag` is `false`, prevents `risch` from introducing the
`erf` function in the answer if there were none in the integrand to
begin with.

<!-- category: Calculus -->
<!-- keywords: ilt -->
<!-- signatures: ilt(expr, s, t) -->
### Function: ilt (expr, s, t)

Computes the inverse Laplace transform of *expr* with
respect to *s* and parameter *t*. *expr* must be a ratio of
polynomials whose denominator has only linear and quadratic factors;
there is an extension of `ilt`, called `pwilt` (Piece-Wise
Inverse Laplace Transform) that handles several other cases where
`ilt` fails.


By using the functions `laplace` and `ilt` together with the
`solve` or `linsolve` functions the user can solve a single
differential or convolution integral equation or a set of them.













```maxima
maxima

(%i1) 'integrate (sinh(a*x)*f(t-x), x, 0, t) + b*f(t) = t**2;
              t
             /
             |                                    2
(%o1)        |  f(t - x) sinh(a x) dx + b f(t) = t
             |
             /
              0


(%i2) laplace (%, t, s);
       a laplace(f(t), t, s)                           2
(%o2)  --------------------- + b laplace(f(t), t, s) = --
               2    2                                   3
              s  - a                                   s


(%i3) linsolve ([%], ['laplace(f(t), t, s)]);
                                        2      2
                                     2 s  - 2 a
(%o3)     [laplace(f(t), t, s) = --------------------]
                                    5         2     3
                                 b s  + (a - a  b) s


(%i4) ilt (rhs (first (%)), s, t);
Is a b (a b - 1) positive, negative or zero?
pos;

               sqrt(a b (a b - 1)) t
        2 cosh(---------------------)       2
                         b               a t
(%o4) - ----------------------------- + -------
              3  2      2               a b - 1
             a  b  - 2 a  b + a
                                                       2
                                             + ------------------
                                                3  2      2
                                               a  b  - 2 a  b + a

(%i5) pos;
```

See also: `pwilt`.

<!-- category: Calculus -->
<!-- keywords: intanalysis -->
<!-- signatures: intanalysis -->
### Variable: intanalysis

Default value: `true`


When `true`, definite integration tries to find poles in the integrand in 
the interval of integration.  If there are, then the integral is evaluated
appropriately as a principal value integral.  If intanalysis is `false`, 
this check is not performed and integration is done assuming there are no poles.


See also `ldefint`.


Examples:


Maxima can solve the following integrals, when `intanalysis` is set to
`false`:











```maxima
maxima

(%i1) intanalysis:false;
(%o1)                         false


(%i2) integrate(1/(sqrt(x+1)+1),x,0,1);
                                              3/2
(%o2)      - 2 log(sqrt(2) + 1) + 2 log(2) + 2    - 2


(%i3) integrate(1/(sqrt(x)+1),x,0,1),intanalysis:false;
(%o3)                     2 - 2 log(2)


(%i4) integrate(cos(a)/sqrt((tan(a))^2+1),a,-%pi/2,%pi/2),intanalysis:false;
(%o4)               %i log(2) - %i log(2 %i)

(%i5) intanalysis:false$

(%i6) integrate(cos(a)/sqrt((tan(a))^2 +1),a,-%pi/2,%pi/2);
(%o6)               %i log(2) - %i log(2 %i)
```

See also: `ldefint`, `intanalysis`.

<!-- category: Calculus -->
<!-- keywords: integrate -->
<!-- signatures: integrate(expr, x), integrate(expr, x, a, b) -->
### Function: integrate (expr, x)

Attempts to symbolically compute the integral of *expr* with respect to
*x*.  `integrate (expr, x)` is an indefinite integral,
while `integrate (expr, x, a, b)` is a definite
integral, with limits of integration *a* and *b*.  The limits should
not contain *x*, although `integrate` does not enforce this
restriction.  *a* need not be less than *b*.
If *b* is equal to *a*, `integrate` returns zero.


See `quad_qag` and related functions for numerical approximation of
definite integrals.  See `residue` for computation of residues
(complex integration).  See `antid` for an alternative means of computing
indefinite integrals.


The integral (an expression free of `integrate`) is returned if
`integrate` succeeds.  Otherwise the return value is
the noun form of the integral (the quoted operator `'integrate`)
or an expression containing one or more noun forms.
The noun form of `integrate` is displayed with an integral sign.


In some circumstances it is useful to construct a noun form by hand, by quoting
`integrate` with a single quote, e.g.,
`'integrate (expr, x)`.  For example, the integral may depend
on some parameters which are not yet computed.
The noun may be applied to its arguments by `ev (i, nouns)`
where *i* is the noun form of interest.



`integrate` handles definite integrals separately from indefinite, and
employs a range of heuristics to handle each case.  Special cases of definite
integrals include limits of integration equal to zero or infinity (`inf` or
`minf`), trigonometric functions with limits of integration equal to zero
and `%pi` or `2 %pi`, rational functions, integrals related to the
definitions of the `beta` and `psi` functions, and some logarithmic
and trigonometric integrals.  Processing rational functions may include
computation of residues.  If an applicable special case is not found, an attempt
will be made to compute the indefinite integral and evaluate it at the limits of
integration.  This may include taking a limit as a limit of integration goes to
infinity or negative infinity; see also `ldefint`.


Special cases of indefinite integrals include trigonometric functions,
exponential and logarithmic functions,
and rational functions.
`integrate` may also make use of a short table of elementary integrals.


`integrate` may carry out a change of variable
if the integrand has the form `f(g(x)) * diff(g(x), x)`.
`integrate` attempts to find a subexpression `g(x)` such that
the derivative of `g(x)` divides the integrand.
This search may make use of derivatives defined by the `gradef` function.
See also `changevar` and `antid`.


If none of the preceding heuristics find the indefinite integral, the Risch
algorithm is executed.  The flag `risch` may be set as an `evflag`,
in a call to `ev` or on the command line, e.g.,
`ev (integrate (expr, x), risch)` or
`integrate (expr, x), risch`.  If `risch` is present,
`integrate` calls the `risch` function without attempting heuristics
first.  See also `risch`.



`integrate` works only with functional relations represented explicitly
with the `f(x)` notation.  `integrate` does not respect implicit
dependencies established by the `depends` function.


`integrate` may need to know some property of a parameter in the integrand.
`integrate` will first consult the `assume` database,
and, if the variable of interest is not there,
`integrate` will ask the user.
Depending on the question,
suitable responses are `yes;` or `no;`,
or `pos;`, `zero;`, or `neg;`.


`integrate` is not, by default, declared to be linear.  See `declare`
and `linear`.


`integrate` attempts integration by parts only in a few special cases.


Examples:



- *
Elementary indefinite and definite integrals.




```maxima
maxima
(%i1) integrate (sin(x)^3, x);
                           3
                        cos (x)
(%o1)                   ------- - cos(x)
                           3

(%i2) integrate (x/ sqrt (b^2 - x^2), x);
                                 2    2
(%o2)                    - sqrt(b  - x )

(%i3) integrate (cos(x)^2 * exp(x), x, 0, %pi);
                               %pi
                           3 %e      3
(%o3)                      ------- - -
                              5      5

(%i4) integrate (x^2 * exp(-x^2), x, minf, inf);
                            sqrt(%pi)
(%o4)                       ---------
                                2
```
- *
Use of `assume` and interactive query.





```maxima
maxima
(%i1) assume (a > 1)$
(%i2) integrate (x**a/(x+1)**(5/2), x, 0, inf);
Is a an integer?
no;

Is 2 a - 1 positive, negative or zero?
neg;
                            3
(%o2)                  beta(- - a, a + 1)
                            2

Is 2 a - 1 positive, negative or zero?
no;
                            3
(%o2)                  beta(- - a, a + 1)
                            2
(%i3) neg;
```
- *
Change of variable.  There are two changes of variable in this example:
one using a derivative established by `gradef`, and one using the
derivation `diff(r(x))` of an unspecified function `r(x)`.




```maxima
maxima
(%i1) gradef (q(x), sin(x**2));
(%o1)                         q(x)

(%i2) diff (log (q (r (x))), x);
                      d               2
                     (-- (r(x))) sin(r (x))
                      dx
(%o2)                ----------------------
                            q(r(x))

(%i3) integrate (%, x);
(%o3)                     log(q(r(x)))
```
- *
Return value contains the `'integrate` noun form.  In this example, Maxima
can extract one factor of the denominator of a rational function, but cannot
factor the remainder or otherwise find its integral.  `grind` shows the
noun form `'integrate` in the result.  See also
`integrate_use_rootsof` for more on integrals of rational functions.




```maxima
maxima
(%i1) expand ((x-4) * (x^3+2*x+1));
                    4      3      2
(%o1)              x  - 4 x  + 2 x  - 7 x - 4

(%i2) integrate (1/%, x);
                              /  2
                              | x  + 4 x + 18
                              | ------------- dx
                              |  3
                 log(x - 4)   / x  + 2 x + 1
(%o2)            ---------- - ------------------
                     73               73

(%i3) grind (%);
log(x-4)/73-('integrate((x^2+4*x+18)/(x^3+2*x+1),x))/73$
(%o3)                         done
```
- *
Defining a function in terms of an integral.  The body of a function is not
evaluated when the function is defined.  Thus the body of `f_1` in this
example contains the noun form of `integrate`.  The quote-quote operator
`''` causes the integral to be evaluated, and the result becomes the
body of `f_2`.




```maxima
maxima
(%i1) f_1 (a) := integrate (x^3, x, 1, a);
                                     3
(%o1)           f_1(a) := integrate(x , x, 1, a)

(%i2) ev (f_1 (7), nouns);
(%o2)                          600

(%i3) /* Note parentheses around integrate(...) here */      f_2 (a) := ''(integrate (x^3, x, 1, a));
                                   4
                                  a    1
(%o3)                   f_2(a) := -- - -
                                  4    4

(%i4) f_2 (7);
(%o4)                          600
```

See also: `quad_qag`, `residue`, `antid`, `inf`, `minf`, `beta`, `psi`, `ldefint`, `changevar`, `risch`, `evflag`, `depends`, `assume`, `gradef`, `grind`, `integrate_use_rootsof`.

<!-- category: Calculus -->
<!-- keywords: integrate_use_rootsof -->
<!-- signatures: integrate_use_rootsof -->
### Variable: integrate_use_rootsof

Default value: `false`


When `integrate_use_rootsof` is `true` and the denominator of
a rational function cannot be factored, `integrate` returns the integral
in a form which is a sum over the roots (not yet known) of the denominator.


For example, with `integrate_use_rootsof` set to `false`,
`integrate` returns an unsolved integral of a rational function in noun
form:







```maxima
maxima
(%i1) integrate_use_rootsof: false$

(%i2) integrate (1/(1+x+x^5), x);
      /  2
      | x  - 4 x + 5
      | ------------ dx                            2 x + 1
      |  3    2                2            5 atan(-------)
      / x  - x  + 1       log(x  + x + 1)          sqrt(3)
(%o2) ----------------- - --------------- + ---------------
              7                 14             7 sqrt(3)
```


Now we set the flag to be true and the unsolved part of the integral will be
expressed as a summation over the roots of the denominator of the rational
function:







```maxima
maxima
(%i1) integrate_use_rootsof: true$

(%i2) integrate (1/(1+x+x^5), x);
       ____
       \                                         2
(%o2) ( >                                   ((%r1  - 4 %r1 + 5)
       /
       ----
                         3      2
       %r1 in rootsof(%r1  - %r1  + 1, %r1)
                                          2
                     2               log(x  + x + 1)
 log(x - %r1))/(3 %r1  - 2 %r1))/7 - ---------------
                                           14
          2 x + 1
   5 atan(-------)
          sqrt(3)
 + ---------------
      7 sqrt(3)
```


Alternatively the user may compute the roots of the denominator separately,
and then express the integrand in terms of these roots, e.g.,
`1/((x - a)*(x - b)*(x - c))` or `1/((x^2 - (a+b)*x + a*b)*(x - c))`
if the denominator is a cubic polynomial.
Sometimes this will help Maxima obtain a more useful result.

See also: `integrate`.

<!-- category: Calculus -->
<!-- keywords: integration_constant -->
<!-- signatures: integration_constant -->
### Variable: integration_constant

Default value: `%c`


When a constant of integration is introduced by indefinite integration of an
equation, the name of the constant is constructed by concatenating
`integration_constant` and `integration_constant_counter`.


`integration_constant` may be assigned any symbol.


Examples:








```maxima
maxima

(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integration_constant : 'k;
(%o2)                           k


(%i3) integrate (x^2 = 1, x);
                            3
                           x
(%o3)                      -- = x + k2
                           3
```

<!-- category: Calculus -->
<!-- keywords: integration_constant_counter -->
<!-- signatures: integration_constant_counter -->
### Variable: integration_constant_counter

Default value: 0


When a constant of integration is introduced by indefinite integration of an
equation, the name of the constant is constructed by concatenating
`integration_constant` and `integration_constant_counter`.


`integration_constant_counter` is incremented before constructing the next
integration constant.


Examples:










```maxima
maxima

(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integrate (x^2 = 1, x);
                           3
                          x
(%o2)                     -- = x + %c2
                          3


(%i3) integrate (x^2 = 1, x);
                           3
                          x
(%o3)                     -- = x + %c3
                          3


(%i4) reset (integration_constant_counter);
(%o4)            [integration_constant_counter]


(%i5) integrate (x^2 = 1, x);
                           3
                          x
(%o5)                     -- = x + %c1
                          3
```

<!-- category: Calculus -->
<!-- keywords: laplace -->
<!-- signatures: laplace(expr, t, s) -->
### Function: laplace (expr, t, s)

Attempts to compute the Laplace transform of *expr* with respect to the 
variable *t* and transform parameter *s*.  The Laplace
transform of the function `f(t)` is the one-sided transform defined by

$$F(s) = \int_0^{\infty} f(t) e^{-st} dt$$


$$F(s) = \int_0^{\infty} f(t) e^{-st} dt$$




where $F(s)$ is the transform of $f(t)$, represented by *expr*.


`laplace` recognizes in *expr* the functions `delta`, `exp`,
`log`, `sin`, `cos`, `sinh`, `cosh`, and `erf`,
as well as `derivative`, `integrate`, `sum`, and `ilt`. If
`laplace` fails to find a transform the function `specint` is called.
`specint` can find the laplace transform for expressions with special
functions like the bessel functions `bessel_j`, `bessel_i`, ...
and can handle the `unit_step` function.  See also `specint`.


If `specint` cannot find a solution too, a noun `laplace` is returned.



*expr* may also be a linear, constant coefficient differential equation in
which case `atvalue` of the dependent variable is used.

The required atvalue may be supplied either before or after the transform is
computed.  Since the initial conditions must be specified at zero, if one has
boundary conditions imposed elsewhere he can impose these on the general
solution and eliminate the constants by solving the general solution
for them and substituting their values back.


`laplace` recognizes convolution integrals of the form

$$\int_0^t f(x) g(t-x) dx$$


$$\int_0^t f(x) g(t-x) dx$$




Other kinds of convolutions are not recognized.


Functional relations must be explicitly represented in *expr*;
implicit relations, established by `depends`, are not recognized.
That is, if $f$ depends on $x$ and $y$,
$f (x, y)$ must appear in *expr*.


See also `ilt`, the inverse Laplace transform.


Examples:
















```maxima
maxima

(%i1) laplace (exp (2*t + a) * sin(t) * t, t, s);
                            a
                          %e  (2 s - 4)
(%o1)             -----------------------------
                   4      3       2
                  s  - 8 s  + 26 s  - 40 s + 25


(%i2) laplace ('diff (f (x), x), x, s);
(%o2)             s laplace(f(x), x, s) - f(0)


(%i3) diff (diff (delta (t), t), t);
                          2
                         d
(%o3)                    --- (delta(t))
                           2
                         dt


(%i4) laplace (%, t, s);
                            |
               d            |         2
(%o4)        - -- (delta(t))|      + s  - delta(0) s
               dt           |
                            |t = 0

(%i5) assume(a>1)$
(%i6) declare(a, integer)$

(%i7) laplace(gamma_incomplete(a,t),t,s),gamma_expand:true;
                                       - a - 1
                  gamma(a)   gamma(a) s
(%o7)             -------- - -----------------
                     s            1     a
                                 (- + 1)
                                  s


(%i8) factor(laplace(gamma_incomplete(1/2,t),t,s));
                                       s + 1
               sqrt(%pi) (sqrt(s) sqrt(-----) - 1)
                                         s
(%o8)          -----------------------------------
                         3/2      s + 1
                        s    sqrt(-----)
                                    s

(%i9) assume(exp(%pi*s)>1, n > 0)$

(%i10) laplace(sum((-1)^n*unit_step(t-n*%pi)*sin(t),n,0,inf),t,s),
  simpsum;
                              %pi s
                            %e
(%o10)           ------------------------------
                    %pi s       2     %pi s
                 (%e      - 1) s  + %e      - 1
```

See also: `delta`, `exp`, `log`, `sin`, `cos`, `sinh`, `cosh`, `erf`, `integrate`, `sum`, `ilt`, `specint`, `bessel_j`, `bessel_i`, `unit_step`, `atvalue`, `depends`.

<!-- category: Calculus -->
<!-- keywords: ldefint -->
<!-- signatures: ldefint(expr, x, a, b) -->
### Function: ldefint (expr, x, a, b)

Attempts to compute the definite integral of *expr* by using `limit`
to evaluate the indefinite integral of *expr* with respect to *x*
at the upper limit *b* and at the lower limit *a*.
If it fails to compute the definite integral,
`ldefint` returns an expression containing limits as noun forms.


`ldefint` is not called from `integrate`, so executing
`ldefint (expr, x, a, b)` may yield a different
result than `integrate (expr, x, a, b)`.
`ldefint` always uses the same method to evaluate the definite integral,
while `integrate` may employ various heuristics and may recognize some
special cases.

See also: `limit`, `integrate`.

<!-- category: Calculus -->
<!-- keywords: potential -->
<!-- signatures: potential(givengradient) -->
### Function: potential (givengradient)

The calculation makes use of the global variable `potentialzeroloc[0]`
which must be `nonlist` or of the form



```maxima
[indeterminatej=expressionj, indeterminatek=expressionk, ...]
```


the former being equivalent to the nonlist expression for all right-hand
sides in the latter.  The indicated right-hand sides are used as the
lower limit of integration.  The success of the integrations may
depend upon their values and order.  `potentialzeroloc` is initially set
to 0.

<!-- category: Calculus -->
<!-- keywords: prefer_d -->
<!-- signatures: prefer_d -->
### Variable: prefer_d

Default value: `false`


When `prefer_d` is `true`, `specint` will prefer to
express solutions using `parabolic_cylinder_d` rather than
hypergeometric functions.


In the example below, the solution contains `parabolic_cylinder_d`
when `prefer_d` is `true`. 








```maxima
maxima

(%i1) assume(s>0);
(%o1)                        [s > 0]


(%i2) factor(ex:specint(%e^-(t^2/8)*exp(-s*t),t));
                        2
                     2 s
(%o2)    - sqrt(2) %e     sqrt(%pi) (erf(sqrt(2) s) - 1)


(%i3) specint(ex,t),prefer_d=true;
                             2
                          2 s
(%o3) specint(- sqrt(2) %e     sqrt(%pi) erf(sqrt(2) s), t)
                                                  2
                                               2 s
                           + specint(sqrt(2) %e     sqrt(%pi), t)
```

See also: `specint`, `parabolic_cylinder_d`.

<!-- category: Calculus -->
<!-- keywords: pwilt -->
<!-- signatures: pwilt(expr, s, t) -->
### Function: pwilt (expr, s, t)

Computes the inverse Laplace transform of *expr* with
respect to *s* and parameter *t*. Unlike `ilt`,
`pwilt` is able to return piece-wise and periodic functions
and can also handle some cases with polynomials of degree greater than 3
in the denominator.


Two examples where `ilt` fails:






```maxima
(%i1) pwilt (exp(-s)*s/(s^3-2*s-s+2), s, t);
                        t - 1               - 2 (t - 1)
                      %e      (t - 1)   2 %e
(%o1)   hstep(t - 1) (--------------- - ---------------)
                             3                 9


(%i2) pwilt ((s^2+2)/(s^2-1), s, t);
                                  t       - t
                              3 %e    3 %e
(%o2)              delta(t) + ----- - -------
                                2        2
```

See also: `ilt`.

<!-- category: Calculus -->
<!-- keywords: quad_control -->
<!-- signatures: quad_control(parameter, [value]) -->
### Function: quad_control (parameter, [value])

Control error handling for quadpack.  The parameter should be one of
the following symbols:



**current_error** — The current error number
**control** — Controls if messages are printed or not.  If it is set to zero or
less, messages are suppressed.
**max_message** — The maximum number of times any message is to be printed.


If *value* is not given, then the current value of the
*parameter* is returned.  If *value* is given, the value of
*parameter* is set to the given value.

<!-- category: Calculus -->
<!-- keywords: quad_qag -->
<!-- signatures: quad_qag(f(x), x, a, b, key, [epsrel, epsabs, limit]), quad_qag(f, x, a, b, key, [epsrel, epsabs, limit]) -->
### Function: quad_qag (f(x), x, a, b, key, [epsrel, epsabs, limit])

Integration of a general function over a finite interval.  `quad_qag`
implements a simple globally adaptive integrator using the strategy of Aind
(Piessens, 1973).  The caller may choose among 6 pairs of Gauss-Kronrod
quadrature formulae for the rule evaluation component.  The high-degree rules
are suitable for strongly oscillating integrands.


`quad_qag` computes the integral



$$\int_a^b f(x)\, dx$$


$$\int_a^b f(x)\, dx$$



The function to be integrated is $f(x)$, with dependent
variable $x$, and the function is to be integrated between the
limits $a$ and $b$.  *key* is the integrator to be used
and should be an integer between 1 and 6, inclusive.  The value of
*key* selects the order of the Gauss-Kronrod integration rule.
High-order rules are suitable for strongly oscillating integrands.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The numerical integration is done adaptively by subdividing the
integration region into sub-intervals until the desired accuracy is
achieved.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qag` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — if no problems were encountered;
**1** — if too many sub-intervals were done;
**2** — if excessive roundoff error is detected;
**3** — if extremely bad integrand behavior occurs;
**6** — if the input is invalid.




Examples:







```maxima
maxima

(%i1) quad_qag (x^(1/2)*log(1/x), x, 0, 1, 3, 'epsrel=5d-8);
(%o1)  [0.44444444445742953, 8.737223570614865e-9, 899, 0]


(%i2) integrate (x^(1/2)*log(1/x), x, 0, 1);
                                4
(%o2)                           -
                                9
```

<!-- category: Calculus -->
<!-- keywords: quad_qagi -->
<!-- signatures: quad_qagi(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qagi(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qagi (f(x), x, a, b, [epsrel, epsabs, limit])

Integration of a general function over an infinite or semi-infinite interval.
The interval is mapped onto a finite interval and
then the same strategy as in `quad_qags` is applied.


`quad_qagi` evaluates one of the following integrals



$$\int_a^\infty f(x) \, dx$$


$$\int_a^\infty f(x) \, dx$$




$$\int_\infty^a f(x) \, dx$$


$$\int_\infty^a f(x) \, dx$$




$$\int_{-\infty}^\infty f(x) \, dx$$


$$\int_{-\infty}^\infty f(x) \, dx$$



using the Quadpack QAGI routine.  The function to be integrated is
$f(x)$, with dependent variable $x$, and the function is to
be integrated over an infinite range.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


One of the limits of integration must be infinity.  If not, then
`quad_qagi` will just return the noun form.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qagi` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.




Examples:







```maxima
maxima

(%i1) quad_qagi (x^2*exp(-4*x), x, 0, inf, 'epsrel=1d-8);
(%o1)       [0.03125, 2.9591610299500215e-11, 105, 0]


(%i2) integrate (x^2*exp(-4*x), x, 0, inf);
                               1
(%o2)                          --
                               32
```

<!-- category: Calculus -->
<!-- keywords: quad_qagp -->
<!-- signatures: quad_qagp(f(x), x, a, b, points, [epsrel, epsabs, limit]), quad_qagp(f, x, a, b, points, [epsrel, epsabs, limit]) -->
### Function: quad_qagp (f(x), x, a, b, points, [epsrel, epsabs, limit])

Integration of a general function over a finite interval.
`quad_qagp` implements globally adaptive interval subdivision with
extrapolation (de Doncker, 1978) by the Epsilon algorithm (Wynn, 1956).


`quad_qagp` computes the integral



$$\int_a^b f(x) \, dx$$


$$\int_a^b f(x) \, dx$$



The function to be integrated is $f(x)$, with
dependent variable $x$, and the function is to be integrated
between the limits $a$ and $b$.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


To help the integrator, the user must supply a list of points where
the integrand is singular or discontinuous.  The list is provided by
*points*.  It may be an empty list.  The elements of the list must
be between *a* and *b*, exclusive.  An error is thrown if
there are elements out of range.  The list points may be in any order. 


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qagp` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.




Examples:







```maxima
maxima

(%i1) quad_qagp(x^3*log(abs((x^2-1)*(x^2-2))),x,0,3,[1,sqrt(2)]);
(%o1) [52.740748383471434, 2.6247632689546663e-7, 1029, 0]


(%i2) quad_qags(x^3*log(abs((x^2-1)*(x^2-2))), x, 0, 3);
(%o2)  [52.74074847951494, 4.088443219529836e-7, 1869, 0]
```


The integrand has singularities at `1` and `sqrt(2)` so we supply
these points to `quad_qagp`.  We also note that `quad_qagp` is
more accurate and more efficient that `quad_005fqags`.

See also: `quad_qags`.

<!-- category: Calculus -->
<!-- keywords: quad_qags -->
<!-- signatures: quad_qags(f(x), x, a, b, [epsrel, epsabs, limit]), quad_qags(f, x, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qags (f(x), x, a, b, [epsrel, epsabs, limit])

Integration of a general function over a finite interval.
`quad_qags` implements globally adaptive interval subdivision with
extrapolation (de Doncker, 1978) by the Epsilon algorithm (Wynn, 1956).


`quad_qags` computes the integral



$$\int_a^b f(x)\, dx$$


$$\int_a^b f(x)\, dx$$



The function to be integrated is $f(x)$, with
dependent variable $x$, and the function is to be integrated
between the limits $a$ and $b$.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qags` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.




Examples:






```maxima
maxima

(%i1) quad_qags (x^(1/2)*log(1/x), x, 0, 1, 'epsrel=1d-10);
(%o1) [0.44444444444444475, 1.1102230246251565e-15, 315, 0]
```


Note that `quad_qags` is more accurate and efficient than `quad_qag` for this integrand.

<!-- category: Calculus -->
<!-- keywords: quad_qawc -->
<!-- signatures: quad_qawc(f(x), x, c, a, b, [epsrel, epsabs, limit]), quad_qawc(f, x, c, a, b, [epsrel, epsabs, limit]) -->
### Function: quad_qawc (f(x), x, c, a, b, [epsrel, epsabs, limit])

Computes the Cauchy principal value of $f(x)/(x - c)$ over a finite
interval.  The strategy is globally adaptive, and modified
Clenshaw-Curtis integration is used on the subranges
which contain the point $x = c$.


`quad_qawc` computes the Cauchy principal value of



$$\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}$$


$$\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}$$



using the Quadpack QAWC routine.  The function to be integrated is
$f(x)/(x-c)$, with dependent variable $x$, and the
function is to be integrated over the interval $a$ to $b$.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qawc` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qawc (2^(-5)*((x-1)^2+4^(-5))^(-1), x, 2, 0, 5, 'epsrel=1d-7);
(%o1) [- 3.130120337415925, 1.3068301402495579e-8, 495, 0]


(%i2) integrate (2^(-alpha)*(((x-1)^2 + 4^(-alpha))*(x-2))^(-1), x, 0, 5);
Principal Value
          2 alpha - 1      2 alpha + 4
         2            log(2            + 1)
(%o2) (- ----------------------------------
                     2 alpha
                    2        + 1
    3 alpha       alpha + 2     2 alpha - 1      2 alpha
   2        atan(2         )   2            log(2        + 1)
 - ------------------------- + ------------------------------
          2 alpha                        2 alpha
         2        + 1                   2        + 1
    3 alpha + 1       alpha     3 alpha       alpha
   2            atan(2     )   2        atan(2     )
 - ------------------------- + ---------------------
          2 alpha                   2 alpha
         2        + 1              2        + 1
    2 alpha           2 alpha
   2        log(3)   2        log(2)   alpha
 + --------------- - ---------------)/2
     2 alpha           2 alpha
    2        + 1      2        + 1


(%i3) ev (%, alpha=5, numer);
(%o3)                 - 3.1301203374159177
```

<!-- category: Calculus -->
<!-- keywords: quad_qawf -->
<!-- signatures: quad_qawf(f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst]), quad_qawf(f, x, a, omega, trig, [epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawf (f(x), x, a, omega, trig, [epsabs, limit, maxp1, limlst])

Calculates a Fourier cosine or Fourier sine transform on a semi-infinite
interval using the Quadpack QAWF function.  The same approach as in
`quad_qawo` is applied on successive finite intervals, and convergence
acceleration by means of the Epsilon algorithm (Wynn, 1956) is applied to the
series of the integral contributions.


`quad_qawf` computes the integral



$$\int_a^\infty f(x) \, w(x) \, dx$$


$$\int_a^\infty f(x) \, w(x) \, dx$$



The weight function $w$ is selected by *trig*:



**cos** — $w(x) = \cos\omega x$
**sin** — $w(x) = \sin\omega x$


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsabs** — Desired absolute error of approximation.  Default is 1d-10.
**limit** — Size of internal work array.  (*limit* - *limlst*)/2 is the
maximum number of subintervals to use.  Default is 200.
**maxp1** — Maximum number of Chebyshev moments.  Must be greater than 0.  Default
is 100.
**limlst** — Upper bound on the number of cycles.  Must be greater than or equal to
3.  Default is 10.


`quad_qawf` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qawf (exp(-x^2), x, 0, 1, 'cos, 'epsabs=1d-9);
(%o1)  [0.6901942235215714, 2.848463002545743e-11, 215, 0]


(%i2) integrate (exp(-x^2)*cos(x), x, 0, inf);
                          - 1/4
                        %e      sqrt(%pi)
(%o2)                   -----------------
                                2


(%i3) ev (%, numer);
(%o3)                  0.6901942235215714
```

<!-- category: Calculus -->
<!-- keywords: quad_qawo -->
<!-- signatures: quad_qawo(f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]), quad_qawo(f, x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst]) -->
### Function: quad_qawo (f(x), x, a, b, omega, trig, [epsrel, epsabs, limit, maxp1, limlst])

Integration of 
$\cos(\omega x) f(x)$
or 
$\sin(\omega x)$
over a finite interval,
where 
$\omega$
is a constant.
The rule evaluation component is based on the modified
Clenshaw-Curtis technique.  `quad_qawo` applies adaptive subdivision with
extrapolation, similar to `quad_qags`.


`quad_qawo` computes the integral using the Quadpack QAWO
routine:



$$\int_a^b f(x) \, w(x) \, dx$$


$$\int_a^b f(x) \, w(x) \, dx$$



The weight function $w$ is selected by *trig*:



**cos** — $w(x) = \cos\omega x$
**sin** — $w(x) = \sin\omega x$


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit*/2 is the
maximum number of subintervals to use.  Default is 200.
**maxp1** — Maximum number of Chebyshev moments.  Must be greater than 0.  Default
is 100.
**limlst** — Upper bound on the number of cycles.  Must be greater than or equal to
3.  Default is 10.


`quad_qawo` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qawo (x^(-1/2)*exp(-2^(-2)*x), x, 1d-8, 20*2^2, 1, cos);
(%o1) [1.3760433898776214, 4.7271075942489915e-11, 765, 0]


(%i2) rectform (integrate (x^(-1/2)*exp(-2^(-alpha)*x) * cos(x), x, 0, inf));
         alpha + 1
         --------- - 1
             2                    2 alpha
        2              sqrt(sqrt(2        + 1) %pi + %pi)
(%o2)   -------------------------------------------------
                             2 alpha
                       sqrt(2        + 1)


(%i3) ev (%, alpha=2, numer);
(%o3)                   1.376043390090716

(%i4) ev (%, alpha=2, numer);
```

<!-- category: Calculus -->
<!-- keywords: quad_qaws -->
<!-- signatures: quad_qaws(f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]), quad_qaws(f, x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit]) -->
### Function: quad_qaws (f(x), x, a, b, alpha, beta, wfun, [epsrel, epsabs, limit])

Integration of $w(x) f(x)$ over a finite interval, where $w(x)$ is a
certain algebraic or logarithmic function.  A globally adaptive subdivision
strategy is applied, with modified Clenshaw-Curtis integration on the
subintervals which contain the endpoints of the interval of integration.


`quad_qaws` computes the integral using the Quadpack QAWS routine:



$$\int_a^b f(x) \, w(x) \, dx$$


$$\int_a^b f(x) \, w(x) \, dx$$



The weight function $w$ is selected by *wfun*:



**1** — $w(x) = (x - a)^\alpha (b - x)^\beta$
**2** — $w(x) = (x - a)^\alpha (b - x)^\beta \log(x - a)$
**3** — $w(x) = (x - a)^\alpha (b - x)^\beta \log(b - x)$
**4** — $w(x) = (x - a)^\alpha (b - x)^\beta \log(x - a) \log(b - x)$


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit*is the
maximum number of subintervals to use.  Default is 200.


`quad_qaws` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qaws (1/(x+1+2^(-4)), x, -1, 1, -0.5, -0.5, 1, 'epsabs=1d-9);
(%o1)  [8.750097361672843, 1.2761903591126173e-8, 130, 0]


(%i2) integrate ((1-x*x)^(-1/2)/(x+1+2^(-alpha)), x, -1, 1);
                            alpha
                           2      %pi
(%o2)                 --------------------
                            alpha + 1
                      sqrt(2          + 1)


(%i3) ev (%, alpha=4, numer);
(%o3)                   8.75009736167283
```

<!-- category: Calculus -->
<!-- keywords: residue -->
<!-- signatures: residue(expr, z, z_0) -->
### Function: residue (expr, z, z_0)

Computes the residue in the complex plane of the expression *expr* when the
variable *z* assumes the value *z_0*.  The residue is the coefficient of
`(z - z_0)^(-1)` in the Laurent series for *expr*.







```maxima
maxima

(%i1) residue (s/(s**2+a**2), s, a*%i);
                                1
(%o1)                           -
                                2


(%i2) residue (sin(a*x)/x**4, x, 0);
                                 3
                                a
(%o2)                         - --
                                6
```

<!-- category: Calculus -->
<!-- keywords: risch -->
<!-- signatures: risch(expr, x) -->
### Function: risch (expr, x)

Integrates *expr* with respect to *x* using the
transcendental case of the Risch algorithm.  (The algebraic case of
the Risch algorithm has not been implemented.)  This currently
handles the cases of nested exponentials and logarithms which the main
part of `integrate` can’t do.  `integrate` will automatically apply
`risch` if given these cases.


`erfflag`, if `false`, prevents `risch` from introducing the
`erf` function in the answer if there were none in the integrand to begin
with.







```maxima
maxima

(%i1) risch (x^2*erf(x), x);
                             2
             3            - x              2
        %pi x  erf(x) + %e     (sqrt(%pi) x  + sqrt(%pi))
(%o1)   -------------------------------------------------
                              3 %pi


(%i2) diff(%, x), ratsimp;
                             2
(%o2)                       x  erf(x)
```

See also: `integrate`.

<!-- category: Calculus -->
<!-- keywords: specint -->
<!-- signatures: specint(exp(-s*t)*expr, t) -->
### Function: specint (exp(-s*t)*expr, t)

Compute the Laplace transform of *expr* with respect to the variable *t*.
The integrand *expr* may contain special functions.   The
parameter *s* maybe be named something else; it is determined
automatically, as the examples below show where *p* is used in
some places.


The following special functions are handled by `specint`: incomplete gamma 
function, error functions (but not the error function `erfi`, it is easy to 
transform `erfi` e.g. to the error function `erf`), exponential 
integrals, bessel functions (including products of bessel functions), hankel 
functions, hermite and the laguerre polynomials.


Furthermore, `specint` can handle the hypergeometric function 
`%f[p,q]([],[],z)`, the Whittaker function of the first kind 
`%m[u,k](z)` and of the second kind `%w[u,k](z)`.


The result may be in terms of special functions and can include unsimplified 
hypergeometric functions.  If variable `prefer_d` is `true`
then the `parabolic_cylinder_d` function may be used in the result
in preference to hypergeometric functions.


When `laplace` fails to find a Laplace transform, `specint` is called. 
Because `laplace` knows more general rules for Laplace transforms, it is 
preferable to use `laplace` and not `specint`.


`demo("hypgeo")` displays several examples of Laplace transforms computed by 
`specint`.


Examples:








```maxima
maxima
(%i1) assume (p > 0, a > 0)$

(%i2) specint (t^(1/2) * exp(-a*t/4) * exp(-p*t), t);
                           sqrt(%pi)
(%o2)                     ------------
                                 a 3/2
                          2 (p + -)
                                 4


(%i3) specint (t^(1/2) * bessel_j(1, 2 * a^(1/2) * t^(1/2))
              * exp(-p*t), t);
                           - a/p
                         %e      sqrt(a)
(%o3)                    ---------------
                                2
                               p
```


Examples for exponential integrals:











```maxima
maxima
(%i1) assume(s>0,a>0,s-a>0)$

(%i2) ratsimp(specint(%e^(a*t)*(log(a)+expintegral_e1(a*t))*%e^(-s*t),t));
                             log(s)
(%o2)                        ------
                             s - a

(%i3) logarc:true$
(%i4) gamma_expand:true$

(%i5) radcan(specint((cos(t)*expintegral_si(t) -sin(t)*expintegral_ci(t))*%e^(-s*t),t));
                             log(s)
(%o5)                        ------
                              2
                             s  + 1


(%i6) ratsimp(specint((2*t*log(a)+2/a*sin(a*t) -2*t*expintegral_ci(a*t))*%e^(-s*t),t));
                               2    2
                          log(s  + a )
(%o6)                     ------------
                                2
                               s
```


Results when using the expansion of `gamma_incomplete` and when changing 
the representation to `expintegral_e1`:











```maxima
maxima
(%i1) assume(s>0)$

(%i2) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                                     1
                    gamma_incomplete(-, k s)
                                     2
(%o2)               ------------------------
                       sqrt(%pi) sqrt(s)

(%i3) gamma_expand:true$

(%i4) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                      erfc(sqrt(k) sqrt(s))
(%o4)                 ---------------------
                             sqrt(s)

(%i5) expintrep:expintegral_e1$

(%i6) ratsimp(specint(1/(t+a)^2*%e^(-s*t),t));
                       a s
                 a s %e    expintegral_e1(a s) - 1
(%o6)          - ---------------------------------
                                 a
```

See also: `prefer_d`, `parabolic_cylinder_d`, `laplace`, `gamma_incomplete`, `expintegral_e1`.

<!-- category: Calculus -->
<!-- keywords: tldefint -->
<!-- signatures: tldefint(expr, x, a, b) -->
### Function: tldefint (expr, x, a, b)

Equivalent to `ldefint` with `tlimswitch` set to `true`.

