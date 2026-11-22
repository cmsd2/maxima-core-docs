## Elementary Functions

<!-- category: Combinatorics -->
<!-- keywords: !!, double_factorial -->
<!-- signatures: double_factorial(z) -->
### Function: !!

The double factorial operator.
`!!` and `double_factorial` are equivalent.
The operator is displayed as `!!`
whether input as `!!` or `double_factorial`.


`0!!` simplifies to `1` and `(- 1)!!` simplifies to `1`.


For a positive integer *n*,
`n!!` simplifies to
the product `n (n - 2) (n - 4) (n - 6) ... 5 3 1` for odd *n*
and `n (n - 2) (n - 4) ... 6 4 2` for even *n*.


For a negative odd integer *n*,
the double factorial is equal to `(- 1)^((n - 1)/2)*n/(- n)!!`.
The double factorial is not defined for negative even integers.


For real or complex float or bigfloat argument *z*,
`z!!` simplifies to a real or complex float or bigfloat result,
equal to `sqrt(2/%pi)^((1 - cos(%pi*z))/2)*(2^(z/2))*gamma(1 + z/2)`.
This expression agrees with the product definitions for even and odd positive integers.


When the global flag `factorial_expand` is `true`,
`(z - 1)!!` simplifies to `z!/z!!`,
where *z* is any expression.


Also when the global flag `factorial_expand` is `true` and `k` is an even positive integer,
`(z + k)!!` simplifies to
`(z + 2) (z + 4) (z + 6) ... (z + k) z!!`,
and `z - k` simplifies to
`z!!/((z - k + 2) (z - k + 4) (z - k + 6) ... z)`.


Maxima knows the derivative of the double factorial.


`!!` distributes over lists, matrices, and equations.
See `distribute_over`.


Examples:


`!!` and `double_factorial` are equivalent.










```maxima
maxima

(%i1) 8!!;
(%o1)                          384


(%i2) double_factorial (8);
(%o2)                          384


(%i3) x!!;
(%o3)                          x!!


(%i4) double_factorial (x);
(%o4)                          x!!


(%i5) is (x!! = double_factorial (x));
(%o5)                         true
```


Double factorial of even and odd positive integers.






```maxima
maxima

(%i1) makelist (n!!, n, 1, 9);
(%o1)          [1, 2, 3, 8, 15, 48, 105, 384, 945]
```


Double factorial of odd negative integers.






```maxima
maxima

(%i1) makelist (n!!, n, -9, -1, 2);
                       1     1   1
(%o1)                [---, - --, -, - 1, 1]
                      105    15  3
```


Double factorial of float and bigfloat values.







```maxima
maxima

(%i1) makelist ((float (k + 1/2))!!, k, -5, 5, 2);
(%o1) [0.7363534302684733, - 1.8408835756711817, 
0.9204417878355904, 1.3806626817533858, 4.8323193861368505, 
26.577756623752663]


(%i2) makelist ((bfloat (k + 1/2))!!, k, -5, 5, 2);
(%o2) [7.363534302684728b-1, - 1.840883575671182b0, 
9.20441787835591b-1, 1.380662681753387b0, 4.832319386136853b0, 
2.657775662375269b1]
```


Double factorial of complex float and complex bigfloat values.







```maxima
maxima

(%i1) makelist ((float (k + %i/2))!!, k, -5, 5, 2);
(%o1) [0.0738293842296815 %i + 0.20245223746676777, 
- 0.12026203395566047 %i - 0.644271404515144, 
0.7044024214929739 - 0.2018736683019115 %i, 
0.15032754244457538 %i + 0.8053392556439295, 
0.8536522551556902 %i + 2.3408539957095003, 
5.438688273633204 %i + 11.27744385096966]


(%i2) makelist ((bfloat (k + %i/2))!!, k, -5, 5, 2);
(%o2) [7.382938422968142b-2 %i + 2.024522374667677b-1, 
- 1.202620339556604b-1 %i - 6.442714045151438b-1, 
7.04402421492974b-1 - 2.018736683019115b-1 %i, 
1.503275424445755b-1 %i + 8.053392556439297b-1, 
8.536522551556913b-1 %i + 2.340853995709501b0, 
5.438688273633207b0 %i + 1.127744385096966b1]
```


Simplification of double factorial when `factorial_expand` is `true`.









```maxima
maxima

(%i1) factorial_expand: true;
(%o1)                         true


(%i2) (n - 1)!!;
                               n!
(%o2)                          ---
                               n!!


(%i3) (n + 6)!!;
(%o3)              (n + 2) (n + 4) (n + 6) n!!


(%i4) (n - 6)!!;
                               n!!
(%o4)                   -----------------
                        (n - 4) (n - 2) n
```


Derivative of the double factorial.






```maxima
maxima

(%i1) diff (x!!, x);
                    2
           %pi log(---) sin(%pi x)
                   %pi                    x
      x!! (----------------------- + psi (- + 1) + log(2))
                      2                 0 2
(%o1) ----------------------------------------------------
                               2
```


Distributing the double factorial over a list, a matrix, and an equation.








```maxima
maxima

(%i1) [ 1, 3, 7, 9 ]!!;
(%o1)                   [1, 3, 105, 945]


(%i2) matrix ([1, 3, 7], [9, 11, 13])!!;
                     [  1     3     105   ]
(%o2)                [                    ]
                     [ 945  10395  135135 ]


(%i3) (z = 7)!!;
(%o3)                       z!! = 105
```

See also: `distribute_over`.

<!-- category: Combinatorics -->
<!-- keywords: binomial -->
<!-- signatures: binomial(x, y) -->
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

<!-- category: Combinatorics -->
<!-- keywords: factcomb -->
<!-- signatures: factcomb(expr) -->
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

<!-- category: Combinatorics -->
<!-- keywords: factlim -->
<!-- signatures: factlim -->
### Variable: factlim

Default value: 100000


`factlim` specifies the highest factorial which is
automatically expanded.  If it is -1 then all integers are expanded.

<!-- category: Combinatorics -->
<!-- keywords: factorial, ! -->
<!-- signatures: ! -->
### Function: factorial

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

<!-- category: Combinatorics -->
<!-- keywords: factorial_expand -->
<!-- signatures: factorial_expand -->
### Variable: factorial_expand

Default value: false


The option variable `factorial_expand` controls the simplification of 
expressions like `(x+n)!`, where `n` is an integer.
See `factorial` for an example.

See also: `factorial`.

<!-- category: Combinatorics -->
<!-- keywords: genfact -->
<!-- signatures: genfact(x, y, z) -->
### Function: genfact (x, y, z)

Returns the generalized factorial, defined as
`x (x-z) (x - 2 z) ... (x - (y - 1) z)`.  Thus, when *x* is an integer,
`genfact (x, x, 1) = x!` and `genfact (x, x/2, 2) = x!!`.


When *x* and *z* are integers,
and `floor(y)` is an integer,
`genfact(x, y, y)` simplifies to a number.

<!-- category: Combinatorics -->
<!-- keywords: minfactorial -->
<!-- signatures: minfactorial(expr) -->
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

<!-- category: Combinatorics -->
<!-- keywords: sumsplitfact -->
<!-- signatures: sumsplitfact -->
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

