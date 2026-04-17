## minpack

<!-- category: Numerical -->
<!-- keywords: minpack_lsquares -->
<!-- signatures: minpack_lsquares(flist, varlist, guess, ['tolerance=tolerance, 'jacobian=jacobian]) -->
### Function: minpack_lsquares (flist, varlist, guess, ['tolerance=tolerance, 'jacobian=jacobian])

Compute the point that minimizes the sum of the squares of the
functions in the list *flist*.  The variables are in the list
*varlist*.  An initial guess of the optimum point must be provided
in *guess*.


Let *flist* be a list of $m$ functions,
$f_i(x_1, x_2, ..., x_n).$
Then this function can be used to find the values of
$x_1, x_2, ..., x_n$
that solve the least squares problem



$$\sum_i^m f_i(x_1, x_2,...,x_n)^2$$


$$\sum_i^m f_i(x_1, x_2,...,x_n)^2$$




The optional keyword arguments, *tolerance* and *jacobian*
provide some control over the algorithm.



**tolerance** — the estimated relative error desired in the sum of squares.  The
default value is approximately
$1.0537\times 10^{-8}.$
**jacobian** — specifies the Jacobian.  If *jacobian*
is not given or is `true` (the default), the Jacobian is computed
from *flist*.  If *jacobian* is `false`, a numerical
approximation is used.  `jacobian`.


`minpack_lsquares` returns a list of three items as follows:


1. The estimated solution
2. The sum of squares
3. The success of the algorithm. The possible values are


  1. improper input parameters.
  2. algorithm estimates that the relative error in the sum of squares is
at most `tolerance`.
  3. algorithm estimates that the relative error between x and the solution
is at most `tolerance`.
  4. conditions for info = 1 and info = 2 both hold.
  5. fvec is orthogonal to the columns of the jacobian to machine
precision.
  6. number of calls to fcn with iflag = 1 has reached 100*(n+1).
  7. tol is too small. no further reduction in the sum of squares is
possible.
  8. tol is too small. no further improvement in the approximate solution x
is possible.


Here is an example using Powell’s singular function.











```maxima
maxima
(%i1) load("minpack")$
(%i2) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], [3,-1,0,1]);
(%o3) [[1.6521175961683935e-17, - 1.6521175961683934e-18, 
2.6433881538694683e-18, 2.6433881538694683e-18], 
6.109327859207777e-34, 4]
```


Same problem but use numerical approximation to Jacobian.







```maxima
maxima
(%i1) load("minpack")$
(%i2) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], [3,-1,0,1], jacobian = false);
(%o3) [[5.060282149485331e-11, - 5.060282149491206e-12, 
2.1794478435472183e-11, 2.1794478435472183e-11], 
3.534491794847031e-21, 5]
```

See also: `jacobian`.

<!-- category: Numerical -->
<!-- keywords: minpack_solve -->
<!-- signatures: minpack_solve(flist, varlist, guess, ['tolerance=tolerance, 'jacobian=jacobian]) -->
### Function: minpack_solve (flist, varlist, guess, ['tolerance=tolerance, 'jacobian=jacobian])

Solve a system of `n` equations in `n` unknowns.
The `n` equations are given in the list *flist*, and the
unknowns are in *varlist*.  An initial guess of the solution must
be provided in *guess*.


Let *flist* be a list of $m$ functions,
$f_i(x_1, x_2, ..., x_n).$
Then this functions solves the system of $m$ nonlinear equations
in $n$ variables:



$$f_i(x_1, x_2, ..., x_n) = 0$$


$$f_i(x_1, x_2, ..., x_n) = 0$$



The optional keyword arguments, *tolerance* and *jacobian*
provide some control over the algorithm.



**tolerance** — the estimated relative error desired in the sum of squares.  The
default value is approximately
$1.0537\times 10^{-8}.$
**jacobian** — specifies the Jacobian.  If *jacobian*
is not given or is `true` (the default), the Jacobian is computed
from *flist*.  If *jacobian* is `false`, a numerical
approximation is used.  `jacobian`.


`minpack_solve` returns a list of three items as follows:


1. The estimated solution
2. The sum of squares
3. The success of the algorithm.  The possible values are


  1. improper input parameters.
  2. algorithm estimates that the relative error in the solution is
at most `tolerance`.
  3. number of calls to fcn with iflag = 1 has reached 100*(n+1).
  4. tol is too small. no further reduction in the sum of squares is
possible.
  5. Iteration is not making good progress.








```maxima
maxima
(%i1) load("minpack")$
(%i2) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], [3,-1,0,1]);
(%o3) [[1.6521175961683935e-17, - 1.6521175961683934e-18, 
2.6433881538694683e-18, 2.6433881538694683e-18], 
6.109327859207777e-34, 4]
```

In this particular case, we can solve this analytically:






```maxima
maxima
(%i1) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i2) solve(powell(x1,x2,x3,x4),[x1,x2,x3,x4]);
(%o2)          [[x1 = 0, x2 = 0, x3 = 0, x4 = 0]]
```

and we see that the numerical solution is quite close the analytical one.

See also: `jacobian`.

