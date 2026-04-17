## simplification

<!-- category: Simplification -->
<!-- keywords: agd -->
<!-- signatures: agd(x) -->
### Function: agd (x)

Returns the inverse Gudermannian function
`log (tan (%pi/4 + x/2))`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: arithmetic -->
<!-- signatures: arithmetic(a, d, n) -->
### Function: arithmetic (a, d, n)

Returns the *n*-th term of the arithmetic series
`a, a + d, a + 2*d, ..., a + (n - 1)*d`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: arithsum -->
<!-- signatures: arithsum(a, d, n) -->
### Function: arithsum (a, d, n)

Returns the sum of the arithmetic series from 1 to *n*.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: collectterms -->
<!-- signatures: collectterms(expr, arg_1, ..., arg_n) -->
### Function: collectterms (expr, arg_1, ..., arg_n)

Collects all terms that contain *arg_1* ... *arg_n*.
If several expressions have been simplified  with the following functions
`facsum`, `factorfacsum`, `factenexpand`, `facexpten` or
`factorfacexpten`, and they are to be added together, it may be desirable
to combine them using the function  `collecterms`.  `collecterms` can
take as arguments all of the arguments that can be given to these other
associated functions with the exception of `nextlayerfactor`, which has no
effect on `collectterms`.  The advantage of `collectterms` is that it
returns a form  similar to `facsum`, but since it is adding forms that have
already been processed by `facsum`, it does not need to repeat that effort.
This capability is especially useful when the expressions to be summed are very
large.


See also `factor`.


Example:







```maxima
(%i1) (exp(x)+2)*x+exp(x);
                             x          x
(%o1)                   x (%e  + 2) + %e


(%i2) collectterms(expand(%),exp(x));
                                  x
(%o2)                   (x + 1) %e  + 2 x
```

See also: `factor`.

<!-- category: Simplification -->
<!-- keywords: combination -->
<!-- signatures: combination(n, r) -->
### Function: combination (n, r)

Returns the number of combinations of *n* objects
taken *r* at a time.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: covers -->
<!-- signatures: covers(x) -->
### Function: covers (x)

Returns the coversed sine `1 - sin (x)`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: exsec -->
<!-- signatures: exsec(x) -->
### Function: exsec (x)

Returns the exsecant `sec (x) - 1`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: facsum -->
<!-- signatures: facsum(expr, arg_1, ..., arg_n) -->
### Function: facsum (expr, arg_1, ..., arg_n)

Returns  a form  of *expr*  which depends  on the
arguments *arg_1*, ..., *arg_n*.
The arguments can be any form suitable for `ratvars`, or they can be
lists  of such  forms.  If  the arguments  are not  lists, then  the form
returned is  fully expanded with respect  to the arguments,  and the
coefficients of the arguments are factored.  These  coefficients are
free of the arguments, except perhaps in a non-rational sense.


If any of the arguments are  lists, then all such lists are combined
into  a  single  list,   and  instead  of  calling  `factor`   on  the
coefficients  of  the  arguments,  `facsum`  calls  itself   on  these
coefficients, using  this newly constructed  single list as  the new
argument list  for this  recursive  call.  This  process can  be  repeated to
arbitrary depth by nesting the desired elements in lists.


It is possible that one may wish to `facsum` with respect  to more
complicated subexpressions,  such as  `log (x + y)`.  Such  arguments are
also  permissible.   







Occasionally the user may wish to obtain any of the  above forms
for expressions which are specified only by their leading operators.
For example, one may wish  to `facsum` with respect to all  `log`’s.  In
this situation, one may  include among the arguments either  the specific
`log`’s which are to be treated in this way, or  alternatively, either
the expression  `operator (log)` or `'operator (log)`.   If one  wished to
`facsum` the expression *expr* with respect to the operators *op_1*, ..., *op_n*,
one   would  evaluate  `facsum (expr, operator (op_1, ..., op_n))`.
The `operator` form may also appear inside list arguments.


In  addition,  the  setting  of  the  switches   `facsum_combine`  and
`nextlayerfactor` may affect the result of `facsum`.

<!-- category: Simplification -->
<!-- keywords: facsum_combine -->
<!-- signatures: facsum_combine -->
### Variable: facsum_combine

Default value: `true`


`facsum_combine` controls the form  of the final result  returned by
`facsum`  when  its  argument  is  a  quotient  of   polynomials.   If
`facsum_combine` is `false`  then the form will  be returned as  a fully
expanded  sum  as described  above,  but if  `true`,  then  the expression
returned is a ratio of polynomials, with each polynomial in the form
described above.


The `true` setting of this switch is useful when one
wants to  `facsum` both  the numerator and  denominator of  a rational
expression,  but  does not  want  the denominator  to  be multiplied
through the terms of the numerator.

<!-- category: Simplification -->
<!-- keywords: factorfacsum -->
<!-- signatures: factorfacsum(expr, arg_1, ...arg_n) -->
### Function: factorfacsum (expr, arg_1, ...arg_n)

Returns a  form of *expr*  which is
obtained by calling  `facsum` on the factors  of *expr* with *arg_1*, ... *arg_n* as
arguments.  If any of the factors of *expr* is raised to a  power, both
the factor and the exponent will be processed in this way.

<!-- category: Simplification -->
<!-- keywords: gaussprob -->
<!-- signatures: gaussprob(x) -->
### Function: gaussprob (x)

Returns the Gaussian probability function
`%e^(-x^2/2) / sqrt(2*%pi)`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: gcdivide -->
<!-- signatures: gcdivide(p, q) -->
### Function: gcdivide (p, q)

When the option variable `takegcd` is `true` which is the default,
`gcdivide` divides the polynomials *p* and *q* by their greatest
common divisor and returns the ratio of the results.  `gcdivde` calls the
function `ezgcd` to divide the polynomials by the greatest common divisor.


When `takegcd` is `false`, `gcdivide` returns the ratio
`p/q`.


To use this function write first `load("functs")`.


See also `ezgcd`, `gcd`, `gcdex`, and
`poly_005fgcd`.


Example:



```maxima
(%i1) load("functs")$

(%i2) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o2)                6 x  + 19 x  + 19 x + 6
(%i3) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o3)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i4) gcdivide(p1, p2);
                             x + 1
(%o4)                        ------
                              3
                             x  + x
(%i5) takegcd:false;
(%o5)                         false
(%i6) gcdivide(p1, p2);
                       3       2
                    6 x  + 19 x  + 19 x + 6
(%o6)          ----------------------------------
                  5       4       3       2
               6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i7) ratsimp(%);
                             x + 1
(%o7)                        ------
                              3
                             x  + x
```

See also: `ezgcd`, `gcd`, `gcdex`, `poly_gcd`.

<!-- category: Simplification -->
<!-- keywords: gcfac -->
<!-- signatures: gcfac(expr) -->
### Function: gcfac (expr)

`gcfac` is a factoring function that attempts to apply the same heuristics which
scientists apply in trying to make expressions simpler.  `gcfac` is limited
to monomial-type factoring.  For a sum, `gcfac` does the following:



1. Factors over the integers.
2. Factors out the largest powers of terms occurring as
coefficients, regardless of the complexity of the terms.
3. Uses (1) and (2) in factoring adjacent pairs of terms.
4. Repeatedly and recursively applies these techniques until
the expression no longer changes.


Item (3) does not necessarily do an optimal job of pairwise
factoring because of the combinatorially-difficult nature of finding
which of all possible rearrangements of the pairs yields the most
compact pair-factored result.


`load ("scifac")` loads this function.
`demo ("scifac")` shows a demonstration of this function.

<!-- category: Simplification -->
<!-- keywords: gd -->
<!-- signatures: gd(x) -->
### Function: gd (x)

Returns the Gudermannian function
`2*atan(%e^x)-%pi/2`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: geometric -->
<!-- signatures: geometric(a, r, n) -->
### Function: geometric (a, r, n)

Returns the *n*-th term of the geometric series
`a, a*r, a*r^2, ..., a*r^(n - 1)`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: geosum -->
<!-- signatures: geosum(a, r, n) -->
### Function: geosum (a, r, n)

Returns the sum of the geometric series from 1 to *n*.  If *n* is
infinity (`inf`) then a sum is finite only if the absolute value
of *r* is less than 1.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: harmonic -->
<!-- signatures: harmonic(a, b, c, n) -->
### Function: harmonic (a, b, c, n)

Returns the *n*-th term of the harmonic series
`a/b, a/(b + c), a/(b + 2*c), ..., a/(b + (n - 1)*c)`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: hav -->
<!-- signatures: hav(x) -->
### Function: hav (x)

Returns the haversine `(1 - cos(x))/2`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: nextlayerfactor -->
<!-- signatures: nextlayerfactor -->
### Variable: nextlayerfactor

Default value: `false`


When `nextlayerfactor` is `true`, recursive calls  of `facsum`
are applied  to  the  factors  of  the  factored  form   of  the
coefficients of the arguments.


When  `false`, `facsum` is applied to
each coefficient as a whole whenever recursive calls to  `facsum` occur.


Inclusion   of   the  atom
`nextlayerfactor` in  the argument  list of `facsum`  has the  effect of
`nextlayerfactor: true`, but for the next level of the expression *only*.
Since `nextlayerfactor` is  always bound to  either `true` or  `false`, it
must be presented single-quoted whenever it appears in the argument list of `facsum`.

<!-- category: Simplification -->
<!-- keywords: nonzeroandfreeof -->
<!-- signatures: nonzeroandfreeof(x, expr) -->
### Function: nonzeroandfreeof (x, expr)

Returns `true` if *expr* is nonzero and `freeof (x, expr)` returns `true`.
Returns `false` otherwise.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: permutation -->
<!-- signatures: permutation(n, r) -->
### Function: permutation (n, r)

Returns the number of permutations of *r* objects
selected from a set of *n* objects.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: reduce_consts -->
<!-- signatures: reduce_consts(expr) -->
### Function: reduce_consts (expr)

Replaces constant subexpressions of *expr* with
constructed constant atoms, saving the definition of all these
constructed constants in the list of equations `const_eqns`, and
returning the modified *expr*.  Those parts of *expr* are constant which
return `true` when operated on by the function `constantp`.  Hence,
before invoking `reduce_consts`, one should do



```maxima
declare ([objects to be given the constant property], constant)$
```


to set up a database of the constant quantities occurring in your
expressions.


If you are planning to generate Fortran output after these symbolic
calculations, one of the first code sections should be the calculation
of all constants.  To generate this code segment, do



```maxima
map ('fortran, const_eqns)$
```


Variables besides `const_eqns` which affect `reduce_consts` are:


`const_prefix` (default value: `xx`) is the string of characters used to prefix all
symbols generated by `reduce_consts` to represent constant subexpressions.


`const_counter` (default value: 1) is the integer index used to generate unique
symbols to represent each constant subexpression found by `reduce_consts`.


`load ("rducon")` loads this function.
`demo ("rducon")` shows a demonstration of this function.

<!-- category: Simplification -->
<!-- keywords: rempart -->
<!-- signatures: rempart(expr, n) -->
### Function: rempart (expr, n)

Removes part *n* from the expression *expr*.


If *n* is a list of the form `[l, m]`
then parts *l* thru *m* are removed.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: tracematrix -->
<!-- signatures: tracematrix(M) -->
### Function: tracematrix (M)

Returns the trace (sum of the diagonal elements) of matrix *M*.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: vers -->
<!-- signatures: vers(x) -->
### Function: vers (x)

Returns the versed sine `1 - cos (x)`.


To use this function write first `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: wronskian -->
<!-- signatures: wronskian([f_1, ..., f_n], x) -->
### Function: wronskian ([f_1, ..., f_n], x)

Returns the Wronskian matrix of the list of expressions [*f_1*, ..., *f_n*] in the variable *x*.
The determinant of the Wronskian matrix is the Wronskian determinant of the list of expressions.


To use `wronskian`, first `load("functs")`. Example:







```maxima
(%i1) load ("functs")$

(%i2) wronskian([f(x), g(x)],x);
                    [   f(x)       g(x)    ]
                    [                      ]
(%o2)               [ d          d         ]
                    [ -- (f(x))  -- (g(x)) ]
                    [ dx         dx        ]
```

