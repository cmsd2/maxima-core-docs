## Elementary Functions

### Function: !! ()

The double factorial operator.


For an integer, float, or rational number `n`, `n!!` evaluates to the
product `n (n-2) (n-4) (n-6) ... (n - 2 (k-1))` where `k` is equal to
`entier (n/2)`, that is, the largest integer less than or equal to
`n/2`.  Note that this definition does not coincide with other published
definitions for arguments which are not integers.



For an even (or odd) integer `n`, `n!!` evaluates to the product of
all the consecutive even (or odd) integers from 2 (or 1) through `n`
inclusive.


For an argument `n` which is not an integer, float, or rational, `n!!`
yields a noun form `genfact (n, n/2, 2)`.

### Function: binomial (x, y)

The binomial coefficient `x!/(y! (x - y)!)`.
If *x* and *y* are integers, then the numerical value of the binomial
coefficient is computed.  If *y*, or *x - y*, is an integer, the
binomial coefficient is expressed as a polynomial.


Examples:










```maxima
maxima

(%i1) binomial (11, 7);
(%o1)                          330


(%i2) 11! / 7! / (11 - 7)!;
(%o2)                          330


(%i3) binomial (x, 7);
        (x - 6) (x - 5) (x - 4) (x - 3) (x - 2) (x - 1) x
(%o3)   -------------------------------------------------
                              5040


(%i4) binomial (x + 7, x);
      (x + 1) (x + 2) (x + 3) (x + 4) (x + 5) (x + 6) (x + 7)
(%o4) -------------------------------------------------------
                               5040


(%i5) binomial (11, y);
(%o5)                    binomial(11, y)
```

### Function: factcomb (expr)

Tries to combine the coefficients of factorials in *expr*
with the factorials themselves by converting, for example, `(n + 1)*n!`
into `(n + 1)!`.


`sumsplitfact` if set to `false` will cause `minfactorial` to be
applied after a `factcomb`.


Example:











```maxima
maxima

(%i1) sumsplitfact;
(%o1)                         true


(%i2) (n + 1)*(n + 1)*n!;
                                  2
(%o2)                      (n + 1)  n!


(%i3) factcomb (%);
(%o3)                  (n + 2)! - (n + 1)!


(%i4) sumsplitfact: not sumsplitfact;
(%o4)                         false


(%i5) (n + 1)*(n + 1)*n!;
                                  2
(%o5)                      (n + 1)  n!


(%i6) factcomb (%);
(%o6)                 n (n + 1)! + (n + 1)!
```

See also: `sumsplitfact`, `minfactorial`.

### Variable: factlim

Default value: 100000


`factlim` specifies the highest factorial which is
automatically expanded.  If it is -1 then all integers are expanded.

### Function: factorial ()

Represents the factorial function.  Maxima treats `factorial (x)`
the same as `x!`.


For any complex number `x`, except for negative integers, `x!` is 
defined as `gamma(x+1)`.


For an integer `x`, `x!` simplifies to the product of the integers 
from 1 to `x` inclusive.  `0!` simplifies to 1.  For a real or complex 
number in float or bigfloat precision `x`, `x!` simplifies to the 
value of `gamma (x+1)`.  For `x` equal to `n/2` where `n` is 
an odd integer, `x!` simplifies to a rational factor times 
`sqrt (%pi)` (since `gamma (1/2)` is equal to `sqrt (%pi)`).


The option variables `factlim` and `gammalim` control the numerical
evaluation of factorials for integer and rational arguments.  The functions 
`minfactorial` and `factcomb` simplifies expressions containing
factorials.


The functions `gamma`, `bffac`, and `cbffac` are
varieties of the gamma function.  `bffac` and `cbffac` are called
internally by `gamma` to evaluate the gamma function for real and complex
numbers in bigfloat precision.


`makegamma` substitutes `gamma` for factorials and related functions.


Maxima knows the derivative of the factorial function and the limits for 
specific values like negative integers.


The option variable `factorial_expand` controls the simplification of
expressions like `(n+x)!`, where `n` is an integer.


See also `binomial`.


The factorial of an integer is simplified to an exact number unless the operand 
is greater than `factlim`.  The factorial for real and complex numbers is 
evaluated in float or bigfloat precision.









```maxima
maxima

(%i1) factlim : 10;
(%o1)                          10


(%i2) [0!, (7/2)!, 8!, 20!];
                     105 sqrt(%pi)
(%o2)            [1, -------------, 40320, 20!]
                          16


(%i3) [4,77!, (1.0+%i)!];
(%o3) [4, 77!, 0.3430658398165453 %i + 0.6529654964201667]


(%i4) [2.86b0!, (1.0b0+%i)!];
(%o4) [5.046635586910012b0, 3.430658398165454b-1 %i
                                          + 6.529654964201667b-1]
```


The factorial of a known constant, or general expression is not simplified.
Even so it may be possible to simplify the factorial after evaluating the
operand.







```maxima
maxima

(%i1) [(%i + 1)!, %pi!, %e!, (cos(1) + sin(1))!];
(%o1)      [(%i + 1)!, %pi!, %e!, (sin(1) + cos(1))!]


(%i2) ev (%, numer, %enumer);
(%o2) [0.3430658398165453 %i + 0.6529654964201667, 
         7.188082728976031, 4.260820476357003, 1.227580202486819]
```
















Factorials are simplified, not evaluated.
Thus `x!` may be replaced even in a quoted expression.






```maxima
maxima

(%i1) '([0!, (7/2)!, 4.77!, 8!, 20!]);
          105 sqrt(%pi)
(%o1) [1, -------------, 81.44668037931197, 40320, 
               16
                                             2432902008176640000]
```


Maxima knows the derivative of the factorial function.






```maxima
maxima

(%i1) diff(x!,x);
(%o1)                    x! psi (x + 1)
                               0
```


The option variable `factorial_expand` controls expansion and 
simplification of expressions with the factorial function.






```maxima
maxima

(%i1) (n+1)!/n!,factorial_expand:true;
(%o1)                         n + 1
```

See also: `factlim`, `gammalim`, `minfactorial`, `factcomb`, `gamma`, `bffac`, `cbffac`, `makegamma`, `factorial_expand`, `binomial`.

### Variable: factorial_expand

Default value: false


The option variable `factorial_expand` controls the simplification of 
expressions like `(x+n)!`, where `n` is an integer.
See `factorial` for an example.

See also: `factorial`.

### Function: genfact (x, y, z)

Returns the generalized factorial, defined as
`x (x-z) (x - 2 z) ... (x - (y - 1) z)`.  Thus, when *x* is an integer,
`genfact (x, x, 1) = x!` and `genfact (x, x/2, 2) = x!!`.


When *x* and *z* are integers,
and `floor(y)` is an integer,
`genfact(x, y, y)` simplifies to a number.

### Function: minfactorial (expr)

Examines *expr* for occurrences of two factorials
which differ by an integer.
`minfactorial` then turns one into a polynomial times the other.













```maxima
maxima

(%i1) n!/(n+2)!;
                               n!
(%o1)                       --------
                            (n + 2)!


(%i2) minfactorial (%);
                                1
(%o2)                    ---------------
                         (n + 1) (n + 2)
```

### Variable: sumsplitfact

Default value: `true`


When `sumsplitfact` is `false`,

`minfactorial` is applied after a `factcomb`.











```maxima
maxima

(%i1) sumsplitfact;
(%o1)                         true


(%i2) n!/(n+2)!;
                               n!
(%o2)                       --------
                            (n + 2)!


(%i3) factcomb(%);
                               n!
(%o3)                       --------
                            (n + 2)!


(%i4) sumsplitfact: not sumsplitfact ;
(%o4)                         false


(%i5) n!/(n+2)!;
                               n!
(%o5)                       --------
                            (n + 2)!


(%i6) factcomb(%);
                                1
(%o6)                    ---------------
                         (n + 1) (n + 2)
```

See also: `minfactorial`, `factcomb`.

