## Elementary Functions

### Function: abs (z)

The `abs` function represents the mathematical absolute value function and
works for both numerical and symbolic values. If the argument, *z*, is a
real or complex number, `abs` returns the absolute value of *z*. If
possible, symbolic expressions using the absolute value function are
also simplified.


Maxima can differentiate, integrate and calculate limits for expressions
containing `abs`. The `abs_integrate` package further extends
Maxima’s ability to calculate integrals involving the abs function. See
(%i12) in the examples below.


When applied to a list or matrix, `abs` automatically distributes over
the terms. Similarly, it distributes over both sides of an
equation. To alter this behaviour, see the variable `distribute_005fover`.


See also `cabs`.


Examples:


Calculation of `abs` for real and complex numbers, including numerical
constants and various infinities. The first example shows how `abs`
distributes over the elements of a list.









```maxima
maxima

(%i1) abs([-4, 0, 1, 1+%i]);
(%o1)                  [4, 0, 1, sqrt(2)]


(%i2) abs((1+%i)*(1-%i));
(%o2)                           2


(%i3) abs(%e+%i);
                                 2
(%o3)                     sqrt(%e  + 1)


(%i4) abs([inf, infinity, minf]);
(%o4)                    [inf, inf, inf]
```


Simplification of expressions containing `abs`:









```maxima
maxima

(%i1) abs(x^2);
                                2
(%o1)                          x


(%i2) abs(x^3);
                             2
(%o2)                       x  abs(x)


(%i3) abs(abs(x));
(%o3)                        abs(x)


(%i4) abs(conjugate(x));
(%o4)                        abs(x)
```


Integrating and differentiating with the `abs` function. Note that more
integrals involving the `abs` function can be performed, if the
`abs_integrate` package is loaded. The last example shows the Laplace
transform of `abs`: see `laplace`.












```maxima
maxima

(%i1) diff(x*abs(x),x),expand;
(%o1)                       2 abs(x)


(%i2) integrate(abs(x),x);
                            x abs(x)
(%o2)                       --------
                               2


(%i3) integrate(x*abs(x),x);
                          /
                          |
(%o3)                     | x abs(x) dx
                          |
                          /

(%i4) load("abs_integrate")$

(%i5) integrate(x*abs(x),x);
                           3
                          x  signum(x)
(%o5)                     ------------
                               3


(%i6) integrate(abs(x),x,-2,%pi);
                               2
                            %pi
(%o6)                       ---- + 2
                             2


(%i7) laplace(abs(x),x,s);
                               1
(%o7)                          --
                                2
                               s
```

See also: `distribute_over`, `cabs`, `laplace`.

### Function: cabs (expr)

Calculates the absolute value of an expression representing a complex
number.  Unlike the function `abs`, the `cabs` function always
decomposes its argument into a real and an imaginary part.  If `x` and
`y` represent real variables or expressions, the `cabs` function
calculates the absolute value of `x + %i*y` as











```maxima
maxima

(%i1) cabs (1);
(%o1)                           1


(%i2) cabs (1 + %i);
(%o2)                        sqrt(2)


(%i3) cabs (exp (%i));
(%o3)                           1


(%i4) cabs (exp (%pi * %i));
(%o4)                           1


(%i5) cabs (exp (3/2 * %pi * %i));
(%o5)                           1


(%i6) cabs (17 * exp (2 * %i));
(%o6)                          17
```


If `cabs` returns a noun form this most commonly is caused by
some properties of the variables involved not being known:










```maxima
maxima

(%i1) cabs (a+%i*b);
                                2    2
(%o1)                     sqrt(b  + a )


(%i2) declare(a,real,b,real);
(%o2)                         done


(%i3) cabs (a+%i*b);
                                2    2
(%o3)                     sqrt(b  + a )


(%i4) assume(a>0,b>0);
(%o4)                    [a > 0, b > 0]


(%i5) cabs (a+%i*b);
                                2    2
(%o5)                     sqrt(b  + a )
```


The `cabs` function can use known properties like symmetry properties of
complex functions to help it calculate the absolute value of an expression.  If
such identities exist, they can be advertised to `cabs` using function
properties.  The symmetries that `cabs` understands are: mirror symmetry,
conjugate function and complex characteristic.


`cabs` is a verb function and is not suitable for symbolic
calculations.  For such calculations (including integration,
differentiation and taking limits of expressions containing absolute
values), use `abs`.


The result of `cabs` can include the absolute value function,
`abs`, and the arc tangent, `atan2`.


When applied to a list or matrix, `cabs` automatically distributes over
the terms.  Similarly, it distributes over both sides of an equation.


For further ways to compute with complex numbers, see the functions
`rectform`, `realpart`, `imagpart`,
`carg`, `conjugate` and `polarform`.


Examples:


Examples with `sqrt` and `sin`.







```maxima
maxima

(%i1) cabs(sqrt(1+%i*x));
                             2     1/4
(%o1)                      (x  + 1)


(%i2) cabs(sin(x+%i*y));
                    2        2         2        2
(%o2)       sqrt(cos (x) sinh (y) + sin (x) cosh (y))
```


The error function, `erf`, has mirror symmetry, which is used here in
the calculation of the absolute value with a complex argument:






```maxima
maxima

(%i1) cabs(erf(x+%i*y));
                                          2
           (erf(%i y + x) - erf(%i y - x))
(%o1) sqrt(--------------------------------
                          4
                                                               2
                              (- erf(%i y + x) - erf(%i y - x))
                            - ----------------------------------)
                                              4
```


Maxima knows complex identities for the Bessel functions, which allow
it to compute the absolute value for complex arguments.  Here is an
example for `bessel_005fj`.






```maxima
maxima

(%i1) cabs(bessel_j(1,%i));
(%o1)                    bessel_i(1, 1)
```

See also: `abs`, `atan2`, `rectform`, `realpart`, `imagpart`, `carg`, `conjugate`, `polarform`, `sqrt`, `sin`, `erf`, `bessel_j`.

### Function: carg (z)

Returns the complex argument of *z*.  The complex argument is an angle
`theta` in `(-%pi, %pi]` such that `r exp (theta %i) = z`
where `r` is the magnitude of *z*.


`carg` is a computational function, not a simplifying function.



See also `abs` (complex magnitude), `polarform`,
`rectform`, `realpart`, and `imagpart`.


Examples:











```maxima
maxima

(%i1) carg (1);
(%o1)                           0


(%i2) carg (1 + %i);
                               %pi
(%o2)                          ---
                                4


(%i3) carg (exp (%i));
                               sin(1)
(%o3)                     atan(------)
                               cos(1)


(%i4) carg (exp (%pi * %i));
(%o4)                          %pi


(%i5) carg (exp (3/2 * %pi * %i));
                                %pi
(%o5)                         - ---
                                 2


(%i6) carg (17 * exp (2 * %i));
                            sin(2)
(%o6)                  atan(------) + %pi
                            cos(2)
```


If `carg` returns a noun form this most commonly is caused by
some properties of the variables involved not being known:










```maxima
maxima

(%i1) carg (a+%i*b);
(%o1)                      atan2(b, a)


(%i2) declare(a,real,b,real);
(%o2)                         done


(%i3) carg (a+%i*b);
(%o3)                      atan2(b, a)


(%i4) assume(a>0,b>0);
(%o4)                    [a > 0, b > 0]


(%i5) carg (a+%i*b);
                                  b
(%o5)                        atan(-)
                                  a
```

See also: `abs`, `polarform`, `rectform`, `realpart`, `imagpart`.

### Function: ceiling (x)

When *x* is a real number, return the least integer that 
is greater than or equal to *x*.


If *x* is a constant expression (`10 * %pi`, for example), 
`ceiling` evaluates *x* using big floating point numbers, and 
applies `ceiling` to the resulting big float.  Because `ceiling` uses
floating point evaluation, it’s possible, although unlikely, that `ceiling`
could return an erroneous value for constant inputs.  To guard against errors,
the floating point evaluation is done using three values for `fpprec`.


For non-constant inputs, `ceiling` tries to return a simplified value.
Here are examples of the simplifications that `ceiling` knows about:












```maxima
maxima

(%i1) ceiling (ceiling (x));
(%o1)                      ceiling(x)


(%i2) ceiling (floor (x));
(%o2)                       floor(x)

(%i3) declare (n, integer)$

(%i4) [ceiling (n), ceiling (abs (n)), ceiling (max (n, 6))];
(%o4)                [n, abs(n), max(6, n)]

(%i5) assume (x > 0, x < 1)$

(%i6) ceiling (x);
(%o6)                           1


(%i7) tex (ceiling (a));
$$\left \lceil a \right \rceil$$
(%o7)                         false
```


The `ceiling` function distributes over lists, matrices and equations.
See `distribute_005fover`.


Finally, for all inputs that are manifestly complex, `ceiling` returns 
a noun form.


If the range of a function is a subset of the integers, it can be declared to
be `integervalued`.  Both the `ceiling` and `floor` functions
can use this information; for example:








```maxima
maxima
(%i1) declare (f, integervalued)$

(%i2) floor (f(x));
(%o2)                         f(x)


(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```


Example use:


















```maxima
maxima

(%i1) unitfrac(r) := block([uf : [], q],
    if not(ratnump(r)) then
       error("unitfrac: argument must be a rational number"),
    while r # 0 do (
        uf : cons(q : 1/ceiling(1/r), uf),
        r : r - q),
    reverse(uf));
(%o1) unitfrac(r) := block([uf : [], q], 
if not ratnump(r) then error("unitfrac: argument must be a rational number"
                                     1
), while r # 0 do (uf : cons(q : ----------, uf), r : r - q), 
                                         1
                                 ceiling(-)
                                         r
reverse(uf))


(%i2) unitfrac (9/10);
                            1  1  1
(%o2)                      [-, -, --]
                            2  3  15


(%i3) apply ("+", %);
                               9
(%o3)                          --
                               10


(%i4) unitfrac (-9/10);
                                  1
(%o4)                       [- 1, --]
                                  10


(%i5) apply ("+", %);
                                9
(%o5)                         - --
                                10


(%i6) unitfrac (36/37);
                        1  1  1  1    1
(%o6)                  [-, -, -, --, ----]
                        2  3  8  69  6808


(%i7) apply ("+", %);
                               36
(%o7)                          --
                               37
```

See also: `fpprec`, `distribute_over`, `floor`.

### Function: conjugate (x)

Returns the complex conjugate of *x*.










```maxima
maxima

(%i1) declare ([aa, bb], real, cc, complex, ii, imaginary);
(%o1)                         done


(%i2) conjugate (aa + bb*%i);
(%o2)                      aa - %i bb


(%i3) conjugate (cc);
(%o3)                     conjugate(cc)


(%i4) conjugate (ii);
(%o4)                         - ii


(%i5) conjugate (xx + yy);
(%o5)                        yy + xx
```

### Function: entier (x)

Returns the largest integer less than or equal to *x* where *x* is
numeric.  `fix` (as in `fixnum`) is a synonym for this, so
`fix(x)` is precisely the same.

See also: `fix`.

### Function: fix (x)

A synonym for `entier (x)`.

### Function: floor (x)

When *x* is a real number, return the largest integer that is less than or
equal to *x*.


If *x* is a constant expression (`10 * %pi`, for example), `floor`
evaluates *x* using big floating point numbers, and applies `floor` to
the resulting big float. Because `floor` uses floating point evaluation,
it’s possible, although unlikely, that `floor` could return an erroneous
value for constant inputs.  To guard against errors, the floating point
evaluation is done using three values for `fpprec`.


For non-constant inputs, `floor` tries to return a simplified value.  Here
are examples of the simplifications that `floor` knows about:












```maxima
maxima

(%i1) floor (ceiling (x));
(%o1)                      ceiling(x)


(%i2) floor (floor (x));
(%o2)                       floor(x)

(%i3) declare (n, integer)$

(%i4) [floor (n), floor (abs (n)), floor (min (n, 6))];
(%o4)                [n, abs(n), min(6, n)]

(%i5) assume (x > 0, x < 1)$

(%i6) floor (x);
(%o6)                           0


(%i7) tex (floor (a));
$$\left \lfloor a \right \rfloor$$
(%o7)                         false
```


The `floor` function distributes over lists, matrices and equations.
See `distribute_005fover`.


Finally, for all inputs that are manifestly complex, `floor` returns 
a noun form.


If the range of a function is a subset of the integers, it can be declared to
be `integervalued`.  Both the `ceiling` and `floor` functions
can use this information; for example:








```maxima
maxima
(%i1) declare (f, integervalued)$

(%i2) floor (f(x));
(%o2)                         f(x)


(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

See also: `fpprec`, `distribute_over`, `ceiling`.

### Function: hstep (x)

The Heaviside unit step function, equal to 0 if *x* is negative,
equal to 1 if *x* is positive and equal to 1/2 if *x* is equal
to zero.


If you want a unit step function that takes on the value of 0 at *x*
equal to zero, use `unit_005fstep`.

See also: `unit_step`.

### Function: imagpart (expr)

Returns the imaginary part of the expression *expr*.


`imagpart` is a computational function, not a simplifying function.




See also `abs`, `carg`, `polarform`,
`rectform`, and `realpart`.


Example:









```maxima
maxima

(%i1) imagpart (a+b*%i);
(%o1)                           b


(%i2) imagpart (1+sqrt(2)*%i);
(%o2)                        sqrt(2)


(%i3) imagpart (1);
(%o3)                           0


(%i4) imagpart (sqrt(2)*%i);
(%o4)                        sqrt(2)
```

See also: `abs`, `carg`, `polarform`, `rectform`, `realpart`.

### Function: lmax (L)

When *L* is a list or a set, return `apply ('max, args (L))`.
When *L* is not a list or a set, signal an error.
See also `lmin` and `max`.

See also: `lmin`, `max`.

### Function: lmin (L)

When *L* is a list or a set, return `apply ('min, args (L))`.
When *L* is not a list or a set, signal an error.
See also `lmax` and `min`.

See also: `lmax`, `min`.

### Function: make_random_state (make_random_state, n, make_random_state, s, make_random_state, true, make_random_state, false)

A random state object represents the state of the random number generator.
The state comprises 627 32-bit words.


`make_random_state (n)` returns a new random state object
created from an integer seed value equal to *n* modulo 2^32.
*n* may be negative.






`make_random_state (s)` returns a copy of the random state *s*.


`make_random_state (true)` returns a new random state object,
using the current computer clock time as the seed.


`make_random_state (false)` returns a copy of the current state
of the random number generator.

### Function: max (x_1, ..., x_n)

Return a simplified value for the numerical maximum of the expressions *x_1* 
through *x_n*. For an empty argument list, `max` yields `minf`.


The option variable `maxmin_effort` controls which simplification methods are 
applied. Using the default value of *twelve* for `maxmin_effort`, 
`max` uses *all* available simplification methods. To to inhibit all 
simplifications, set `maxmin_effort` to zero.


When `maxmin_effort` is one or more, for an explicit list of real numbers, 
`max` returns a number. 


Unless `max` needs to simplify a lengthy list of expressions, we suggest using 
the default value of `maxmin_effort`. Setting `maxmin_effort` to zero 
(no simplifications), will cause problems for some Maxima functions; accordingly, 
generally `maxmin_effort` should be nonzero.


See also `min`, `lmax`., and `lmin`..


**Examples:**


In the first example, setting `maxmin_effort` to zero suppresses simplifications.


```maxima
(%i1) block([maxmin_effort : 0], max(1,2,x,x, max(a,b)));
(%o1) max(1,2,max(a,b),x,x)

(%i2) block([maxmin_effort : 1], max(1,2,x,x, max(a,b)));
(%o2) max(2,a,b,x)
```


When `maxmin_effort` is two or more, `max` compares pairs of members:


```maxima
(%i1) block([maxmin_effort : 1], max(x,x+1,x+3));
(%o1) max(x,x+1,x+3)

(%i2) block([maxmin_effort : 2], max(x,x+1,x+3));
(%o2) x+3
```


Finally, when `maxmin_effort` is three or more, `max` compares triples 
members and excludes those that are in between; for example


```maxima
(%i1) block([maxmin_effort : 4], max(x, 2*x, 3*x, 4*x));
(%o1) max(x,4*x)
```

See also: `min`, `lmax`, `lmin`.

### Function: min (x_1, ..., x_n)

Return a simplified value for the numerical minimum of the expressions *x_1* 
through *x_n*. For an empty argument list, `minf` yields `inf`.


The option variable `maxmin_effort` controls which simplification methods are 
applied. Using the default value of *twelve* for `maxmin_effort`, 
`max` uses *all* available simplification methods. To to inhibit all 
simplifications, set `maxmin_effort` to zero.


When `maxmin_effort` is one or more, for an explicit list of real numbers, 
`min` returns a number. 


Unless `min` needs to simplify a lengthy list of expressions, we suggest using 
the default value of `maxmin_effort`. Setting `maxmin_effort` to zero 
(no simplifications), will cause problems for some Maxima functions; accordingly, 
generally `maxmin_effort` should be nonzero.


See also `max`, `lmax`., and `lmin`..


**Examples:**


In the first example, setting `maxmin_effort` to zero suppresses simplifications.


```maxima
(%i1) block([maxmin_effort : 0], min(1,2,x,x, min(a,b)));
(%o1) min(1,2,a,b,x,x)

(%i2) block([maxmin_effort : 1], min(1,2,x,x, min(a,b)));
(%o2) min(1,a,b,x)
```


When `maxmin_effort` is two or more, `min` compares pairs of members:


```maxima
(%i1) block([maxmin_effort : 1], min(x,x+1,x+3));
(%o1) min(x,x+1,x+3)

(%i2) block([maxmin_effort : 2], min(x,x+1,x+3));
(%o2) x
```


Finally, when `maxmin_effort` is three or more, `min` compares triples 
members and excludes those that are in between; for example


```maxima
(%i1) block([maxmin_effort : 4], min(x, 2*x, 3*x, 4*x));
(%o1) max(x,4*x)
```

See also: `max`, `lmax`, `lmin`.

### Function: polarform (expr)

Returns an expression `r %e^(%i theta)` equivalent to *expr*,
such that `r` and `theta` are purely real.


Example:








```maxima
maxima

(%i1) polarform(a+b*%i);
                   %i atan2(b, a)       2    2
(%o1)            %e               sqrt(b  + a )


(%i2) polarform(1+%i);
                                  %i %pi
                                  ------
                                    4
(%o2)                   sqrt(2) %e


(%i3) polarform(1+2*%i);
                                %i atan(2)
(%o3)                 sqrt(5) %e
```

### Function: random (x)

Returns a pseudorandom number.  If *x* is an integer,
`random (x)` returns an integer from 0 through `x - 1`
inclusive.  If *x* is a floating point number, `random (x)`
returns a nonnegative floating point number less than *x*.  `random`
complains with an error if *x* is neither an integer nor a float, or if
*x* is not positive.


The functions `make_random_state` and `set_random_state`
maintain the state of the random number generator.


The Maxima random number generator is an implementation of the Mersenne twister
MT 19937.


Examples:


















```maxima
maxima
(%i1) s1: make_random_state (654321)$

(%i2) set_random_state (s1);
(%o2)                         done


(%i3) random (1000);
(%o3)                          768


(%i4) random (9573684);
(%o4)                        7657880


(%i5) random (2^75);
(%o5)                11804491615036831636390

(%i6) s2: make_random_state (false)$

(%i7) random (1.0);
(%o7)                  0.2310127244107132


(%i8) random (10.0);
(%o8)                  4.3945536458708245


(%i9) random (100.0);
(%o9)                   32.28666704056853


(%i10) set_random_state (s2);
(%o10)                        done


(%i11) random (1.0);
(%o11)                 0.2310127244107132


(%i12) random (10.0);
(%o12)                 4.3945536458708245


(%i13) random (100.0);
(%o13)                  32.28666704056853
```

### Function: realpart (expr)

Returns the real part of *expr*.  `realpart` and `imagpart` will
work on expressions involving trigonometric and hyperbolic functions,
as well as square root, logarithm, and exponentiation.


Example:









```maxima
maxima

(%i1) realpart (a+b*%i);
(%o1)                           a


(%i2) realpart (1+sqrt(2)*%i);
(%o2)                           1


(%i3) realpart (sqrt(2)*%i);
(%o3)                           0


(%i4) realpart (1);
(%o4)                           1
```

See also: `imagpart`.

### Function: rectform (expr)

Returns an expression `a + b %i` equivalent to *expr*,
such that *a* and *b* are purely real.


Example:








```maxima
maxima

(%i1) rectform(sqrt(2)*%e^(%i*%pi/4));
(%o1)                        %i + 1


(%i2) rectform(sqrt(b^2+a^2)*%e^(%i*atan2(b, a)));
(%o2)                       %i b + a


(%i3) rectform(sqrt(5)*%e^(%i*atan(2)));
(%o3)                       2 %i + 1
```

### Function: round (x)

When *x* is a real number, returns the closest integer to *x*.
Multiples of 1/2 are rounded to the nearest even integer.  Evaluation of
*x* is similar to `floor` and `ceiling`.


The `round` function distributes over lists, matrices and equations.
See `distribute_005fover`.

See also: `floor`, `ceiling`, `distribute_over`.

### Function: set_random_state (s)

Copies *s* to the random number generator state.


`set_random_state` always returns `done`.

### Function: signum (x)

For either real or complex numbers *x*, the signum function returns
0 if *x* is zero; for a nonzero numeric input *x*, the signum function
returns `x/abs(x)`.


For non-numeric inputs, Maxima attempts to determine the sign of the input.
When the sign is negative, zero, or positive, `signum` returns -1,0, 1,
respectively.  For all other values for the sign, `signum` a simplified but
equivalent form.  The simplifications include reflection (`signum(-x)`
gives `-signum(x)`) and multiplicative identity (`signum(x*y)` gives
`signum(x) * signum(y)`).


The `signum` function distributes over a list, a matrix, or an
equation.  See `sign` and `distribute_005fover`.

See also: `sign`, `distribute_over`.

### Function: truncate (x)

When *x* is a real number, return the closest integer to *x* not
greater in absolute value than *x*.  Evaluation of *x* is similar
to `floor` and `ceiling`.


The `truncate` function distributes over lists, matrices and equations.
See `distribute_005fover`.

See also: `floor`, `ceiling`, `distribute_over`.

