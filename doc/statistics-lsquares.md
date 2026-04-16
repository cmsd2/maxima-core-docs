## lsquares

### Function: lsquares_estimates (lsquares_estimates, D, x, e, a, lsquares_estimates, D, x, e, a, initial, =, L, tol, =, t)

Estimate parameters *a* to best fit the equation *e*
in the variables *x* and *a* to the data *D*,
as determined by the method of least squares.
`lsquares_estimates` first seeks an exact solution,
and if that fails, then seeks an approximate solution.


The return value is a list of lists of equations of the form `[a = ..., b = ..., c = ...]`.
Each element of the list is a distinct, equivalent minimum of the mean square error.


The data *D* must be a matrix.
Each row is one datum (which may be called a ‘record’ or ‘case’ in some contexts),
and each column contains the values of one variable across all data.
The list of variables *x* gives a name for each column of *D*,
even the columns which do not enter the analysis.
The list of parameters *a* gives the names of the parameters for which
estimates are sought.
The equation *e* is an expression or equation in the variables *x* and *a*;
if *e* is not an equation, it is treated the same as `e = 0`.


Additional arguments to `lsquares_estimates`
are specified as equations and passed on verbatim to the function `lbfgs`
which is called to find estimates by a numerical method
when an exact result is not found.


If some exact solution can be found (via `solve`),
the data *D* may contain non-numeric values.
However, if no exact solution is found,
each element of *D* must have a numeric value.
This includes numeric constants such as `%pi` and `%e` as well as literal numbers
(integers, rationals, ordinary floats, and bigfloats).
Numerical calculations are carried out with ordinary floating-point arithmetic,
so all other kinds of numbers are converted to ordinary floats for calculations.


If `lsquares_estimates` needs excessive amounts of time or runs out of memory
`lsquares_estimates_approximate`, which skips the attempt to find an exact 
solution, might still succeed.


`load("lsquares")` loads this function.


See also
`lsquares_estimates_exact`,
`lsquares_estimates_approximate`,

`lsquares_mse`,
`lsquares_residuals`,
and `lsquares_residual_mse`.


Examples:


A problem for which an exact solution is found.










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
        [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]

(%i3) lsquares_estimates (
         M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
```


A problem for which no exact solution is found,
so `lsquares_estimates` resorts to numerical approximation.









```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix ([1, 1], [2, 7/4], [3, 11/4], [4, 13/4]);
                            [ 1  1  ]
                            [       ]
                            [    7  ]
                            [ 2  -  ]
                            [    4  ]
                            [       ]
(%o2)                       [    11 ]
                            [ 3  -- ]
                            [    4  ]
                            [       ]
                            [    13 ]
                            [ 4  -- ]
                            [    4  ]

(%i3) lsquares_estimates (
  M, [x,y], y=a*x^b+c, [a,b,c], initial=[3,3,3], iprint=[-1,0]);
(%o3) [[a = 1.375751433061394, b = 0.7148891534417651, 
                                       c = - 0.4020908910062951]]
```


Exponential functions aren’t well-conditioned for least min square fitting.
In case that fitting to them fails it might be possible to get rid of the
exponential function using an logarithm.













```maxima
(%i1) load ("lsquares")$
(%i2) yvalues: [1,3,5,60,200,203,80]$
(%i3) time: [1,2,4,5,6,8,10]$

(%i4) f: y=a*exp(b*t);
                                   b t
(%o4)                      y = a %e

(%i5) yvalues_log: log(yvalues)$

(%i6) f_log: log(subst(y=exp(y),f));
                                    b t
(%o6)                   y = log(a %e   )


(%i7) lsquares_estimates (transpose(matrix(yvalues_log,time)),
                          [y,t], f_log, [a,b]);
*************************************************
  N=    2   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  6.802906290754687D+00   GNORM=  2.851243373781393D+01
*************************************************

I NFN FUNC                  GNORM                 STEPLENGTH

1   3 1.141838765593467D+00 1.067358003667488D-01 1.390943719972406D-02  
2   5 1.141118195694385D+00 1.237977833033414D-01 5.000000000000000D+00  
3   6 1.136945723147959D+00 3.806696991691383D-01 1.000000000000000D+00  
4   7 1.133958243220262D+00 3.865103550379243D-01 1.000000000000000D+00  
5   8 1.131725773805499D+00 2.292258231154026D-02 1.000000000000000D+00  
6   9 1.131625585698168D+00 2.664440547017370D-03 1.000000000000000D+00  
7  10 1.131620564856599D+00 2.519366958715444D-04 1.000000000000000D+00  

 THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o7)   [[a = 1.155904145765554, b = 0.5772666876959847]]
```

See also: `lsquares_estimates_approximate`, `lsquares_estimates_exact`, `lsquares_mse`, `lsquares_residuals`, `lsquares_residual_mse`.

### Function: lsquares_estimates_approximate (MSE, a, initial, =, L, tol, =, t)

Estimate parameters *a* to minimize the mean square error *MSE*,
via the numerical minimization function `lbfgs`.
The mean square error is an expression in the parameters *a*,
such as that returned by `lsquares_mse`.


The solution returned by `lsquares_estimates_approximate` is a local (perhaps global) minimum
of the mean square error.
For consistency with `lsquares_estimates_exact`,
the return value is a nested list which contains one element,
namely a list of equations of the form `[a = ..., b = ..., c = ...]`.


Additional arguments to `lsquares_estimates_approximate`
are specified as equations and passed on verbatim to the function `lbfgs`.


*MSE* must evaluate to a number when the parameters are assigned numeric values.
This requires that the data from which *MSE* was constructed
comprise only numeric constants such as `%pi` and `%e` and literal numbers
(integers, rationals, ordinary floats, and bigfloats).
Numerical calculations are carried out with ordinary floating-point arithmetic,
so all other kinds of numbers are converted to ordinary floats for calculations.


`load("lsquares")` loads this function.


See also
`lsquares_estimates`,
`lsquares_estimates_exact`,
`lsquares_mse`,

`lsquares_residuals`,
and `lsquares_residual_mse`.


Example:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
         5
        ====
        \                                         2     2
         >    ((- B M    ) - A M     + (M     + D)  - C)
        /            i, 3       i, 2     i, 1
        ====
        i = 1
(%o3)   -------------------------------------------------
                                5

(%i4) lsquares_estimates_approximate (
        mse, [A, B, C, D], iprint = [-1, 0]);
(%o4) [[A = - 3.678504947401971, B = - 1.683070351177937, 
                 C = 10.63469950148714, D = - 3.340357993175297]]
```

See also: `lsquares_estimates`, `lsquares_estimates_exact`, `lsquares_mse`, `lsquares_residuals`, `lsquares_residual_mse`.

### Function: lsquares_estimates_exact (MSE, a)

Estimate parameters *a* to minimize the mean square error *MSE*,
by constructing a system of equations and attempting to solve them symbolically via `solve`.
The mean square error is an expression in the parameters *a*,
such as that returned by `lsquares_mse`.


The return value is a list of lists of equations of the form `[a = ..., b = ..., c = ...]`.
The return value may contain zero, one, or two or more elements.
If two or more elements are returned,
each represents a distinct, equivalent minimum of the mean square error.


See also
`lsquares_estimates`,
`lsquares_estimates_approximate`,
`lsquares_mse`,
`lsquares_residuals`,
and `lsquares_residual_mse`.


Example:










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
         5
        ====
        \                                         2     2
         >    ((- B M    ) - A M     + (M     + D)  - C)
        /            i, 3       i, 2     i, 1
        ====
        i = 1
(%o3)   -------------------------------------------------
                                5

(%i4) lsquares_estimates_exact (mse, [A, B, C, D]);
                  59        27      10921        107
(%o4)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
```

See also: `lsquares_estimates`, `lsquares_estimates_approximate`, `lsquares_mse`, `lsquares_residuals`, `lsquares_residual_mse`.

### Function: lsquares_mse (D, x, e)

Returns the mean square error (MSE), a summation expression, for the equation *e*
in the variables *x*, with data *D*.


The MSE is defined as:



$${1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```


where *n* is the number of data and `e[i]` is the equation *e*
evaluated with the variables in *x* assigned values from the `i`-th datum, `D[i]`.


`load("lsquares")` loads this function.


Example:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
         5
        ====
        \                                         2     2
         >    ((- B M    ) - A M     + (M     + D)  - C)
        /            i, 3       i, 2     i, 1
        ====
        i = 1
(%o3)   -------------------------------------------------
                                5
(%i4) diff (mse, D);
(%o4) 
      5
     ====
     \                                                     2
   4  >    (M     + D) ((- B M    ) - A M     + (M     + D)  - C)
     /       i, 1             i, 3       i, 2     i, 1
     ====
     i = 1
   --------------------------------------------------------------
                                 5

(%i5) ''mse, nouns;
               2                 2         9 2               2
(%o5) (((D + 3)  - C - 2 B - 2 A)  + ((D + -)  - C - B - 2 A)
                                           4
           2               2         3 2               2
 + ((D + 2)  - C - B - 2 A)  + ((D + -)  - C - 2 B - A)
                                     2
           2             2
 + ((D + 1)  - C - B - A) )/5


(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5


(%i4) diff (mse, D);
         5
        ====
        \                             2
      4  >    (D + M    ) ((D + M    )  - C - M     B - M     A)
        /           i, 1         i, 1          i, 3      i, 2
        ====
        i = 1
(%o4) ----------------------------------------------------------
                                  5


(%i5) ''mse, nouns;


               2                 2         9 2               2
(%o5) (((D + 3)  - C - 2 B - 2 A)  + ((D + -)  - C - B - 2 A)
                                           4
           2               2         3 2               2
 + ((D + 2)  - C - B - 2 A)  + ((D + -)  - C - 2 B - A)
                                     2
           2             2
 + ((D + 1)  - C - B - A) )/5
```

### Function: lsquares_residual_mse (D, x, e, a)

Returns the residual mean square error (MSE) for the equation *e*
with specified parameters *a* and data *D*.


The residual MSE is defined as:



$${1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```


where `e[i]` is the equation *e*
evaluated with the variables in *x* assigned values from the `i`-th datum, `D[i]`,
and assigning any remaining free variables from *a*.


`load("lsquares")` loads this function.


Example:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]

(%i3) a : lsquares_estimates (
       M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32


(%i4) lsquares_residual_mse (
       M, [z,x,y], (z + D)^2 = A*x + B*y + C, first (a));
                              169
(%o4)                         ----
                              2560
```

### Function: lsquares_residuals (D, x, e, a)

Returns the residuals for the equation *e*
with specified parameters *a* and data *D*.


*D* is a matrix, *x* is a list of variables,
*e* is an equation or general expression;
if not an equation, *e* is treated as if it were `e = 0`.
*a* is a list of equations which specify values for any free parameters in *e* aside from *x*.


The residuals are defined as:



$${\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right),$$


```maxima
lhs(e ) - rhs(e )
                             i         i
```


where `e[i]` is the equation *e*
evaluated with the variables in *x* assigned values from the `i`-th datum, `D[i]`,
and assigning any remaining free variables from *a*.


`load("lsquares")` loads this function.


Example:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]

(%i3) a : lsquares_estimates (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32


(%i4) lsquares_residuals (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, first(a));
                     13    13    13  13  13
(%o4)               [--, - --, - --, --, --]
                     64    64    32  64  64
```

### Function: plsquares (plsquares, Mat, VarList, depvars, plsquares, Mat, VarList, depvars, maxexpon, plsquares, Mat, VarList, depvars, maxexpon, maxdegree)

Multivariable polynomial adjustment of a data table by the "least squares"
method. *Mat* is a matrix containing the data, *VarList* is a list of variable names (one for each Mat column, but use "-" instead of varnames to ignore Mat columns), *depvars* is the name of a dependent variable or a list with one or more names of dependent variables (which names should be in *VarList*), *maxexpon* is the optional maximum exponent for each independent variable (1 by default), and *maxdegree* is the optional maximum polynomial degree (*maxexpon* by default); note that the sum of exponents of each term must be equal or smaller than *maxdegree*, and if `maxdgree = 0` then no limit is applied.


If *depvars* is the name of a dependent variable (not in a list), `plsquares` returns the adjusted polynomial. If *depvars* is a list of one or more dependent variables, `plsquares` returns a list with the adjusted polynomial(s). The Coefficients of Determination  are displayed in order to inform about the goodness of fit, which ranges from 0 (no correlation) to 1 (exact correlation). These values are also stored in the global variable *DETCOEF* (a list if *depvars* is a list).



A simple example of multivariable linear adjustment:


```maxima
(%i1) load("plsquares")$

(%i2) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z);
     Determination Coefficient for z = .9897039897039897
                       11 y - 9 x - 14
(%o2)              z = ---------------
                              3
```


The same example without degree restrictions:


```maxima
(%i3) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z,1,0);
     Determination Coefficient for z = 1.0
                    x y + 23 y - 29 x - 19
(%o3)           z = ----------------------
                              6
```


How many diagonals does a N-sides polygon have? What polynomial degree should be used?


```maxima
(%i4) plsquares(matrix([3,0],[4,2],[5,5],[6,9],[7,14],[8,20]),
                [N,diagonals],diagonals,5);
     Determination Coefficient for diagonals = 1.0
                                2
                               N  - 3 N
(%o4)              diagonals = --------
                                  2
(%i5) ev(%, N=9);   /* Testing for a 9 sides polygon */
(%o5)                 diagonals = 27
```


How many ways do we have to put two queens without they are threatened into a n x n chessboard?


```maxima
(%i6) plsquares(matrix([0,0],[1,0],[2,0],[3,8],[4,44]),
                [n,positions],[positions],4);
     Determination Coefficient for [positions] = [1.0]

                         4       3      2
                      3 n  - 10 n  + 9 n  - 2 n
(%o6)    [positions = -------------------------]
                                  6

(%i7) ev(%[1], n=8); /* Testing for a (8 x 8) chessboard */
(%o7)                positions = 1288
```


An example with six dependent variables:


```maxima
(%i8) mtrx:matrix([0,0,0,0,0,1,1,1],[0,1,0,1,1,1,0,0],
                  [1,0,0,1,1,1,0,0],[1,1,1,1,0,0,0,1])$
(%i8) plsquares(mtrx,[a,b,_And,_Or,_Xor,_Nand,_Nor,_Nxor],
                     [_And,_Or,_Xor,_Nand,_Nor,_Nxor],1,0);
      Determination Coefficient for
[_And, _Or, _Xor, _Nand, _Nor, _Nxor] =
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
(%o2) [_And = a b, _Or = - a b + b + a,
_Xor = - 2 a b + b + a, _Nand = 1 - a b,
_Nor = a b - b - a + 1, _Nxor = 2 a b - b - a + 1]
```


To use this function write first `load("lsquares")`.

