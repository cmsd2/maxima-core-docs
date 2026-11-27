## minpack

<!-- category: Numerical -->
<!-- keywords: minpack_lsquares -->
<!-- signatures: minpack_lsquares(flist, varlist, guess[, tolerance, jacobian]) -->
### Function: minpack_lsquares (flist, varlist, guess[, tolerance, jacobian])

Compute the point that minimizes the sum of the squares of the
functions in the list *flist*.  The variables are in the list
*varlist*.  An initial guess of the optimum point must be provided
in *guess*.  


The optional keyword arguments, *tolerance* and *jacobian*
provide some control over the algorithm.  *tolerance* is the
estimated relative error desired in the sum of squares.
*jacobian* can be used to specify the Jacobian.  If *jacobian*
is not given or is `true` (the default), the Jacobian is computed
from *flist*.  If *jacobian* is `false`, a numerical
approximation is used.


`minpack_lsquares` returns a list.  The first item is the
estimated solution; the second is the sum of squares, and the third
indicates the success of the algorithm.  The possible values are



**0** — improper input parameters.
**1** — algorithm estimates that the relative error in the sum of squares is
at most `tolerance`.
**2** — algorithm estimates that the relative error between x and the solution
is at most `tolerance`.
**3** — conditions for info = 1 and info = 2 both hold.
**4** — fvec is orthogonal to the columns of the jacobian to machine
precision.
**5** — number of calls to fcn with iflag = 1 has reached 100*(n+1).
**6** — tol is too small. no further reduction in the sum of squares is
possible.
**7** — tol is too small. no further improvement in the approximate solution x
is possible.



```maxima
/* Problem 6: Powell singular function */
(%i1) powell(x1,x2,x3,x4) := 
         [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, 
              sqrt(10)*(x1-x4)^2]$
(%i2) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], 
                       [3,-1,0,1]);
(%o2) [[1.652117596168394e-17, - 1.652117596168393e-18, 
        2.643388153869468e-18, 2.643388153869468e-18], 
       6.109327859207777e-34, 4]
```



```maxima
/* Same problem but use numerical approximation to Jacobian */
(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], 
                       [3,-1,0,1], jacobian = false);
(%o3) [[5.060282149485331e-11, - 5.060282149491206e-12, 
        2.179447843547218e-11, 2.179447843547218e-11], 
       3.534491794847031e-21, 5]
```

<!-- category: Numerical -->
<!-- keywords: minpack_solve -->
<!-- signatures: minpack_solve(flist, varlist, guess[, tolerance, jacobian]) -->
### Function: minpack_solve (flist, varlist, guess[, tolerance, jacobian])

Solve a system of `n` equations in `n` unknowns.
The `n` equations are given in the list *flist*, and the
unknowns are in *varlist*.  An initial guess of the solution must
be provided in *guess*.


The optional keyword arguments, *tolerance* and *jacobian*
provide some control over the algorithm.  *tolerance* is the
estimated relative error desired in the sum of squares.
*jacobian* can be used to specify the Jacobian.  If *jacobian*
is not given or is `true` (the default), the Jacobian is computed
from *flist*.  If *jacobian* is `false`, a numerical
approximation is used.


`minpack_solve` returns a list.  The first item is the
estimated solution; the second is the sum of squares, and the third
indicates the success of the algorithm.  The possible values are



**0** — improper input parameters.
**1** — algorithm estimates that the relative error in the solution is
at most `tolerance`.
**2** — number of calls to fcn with iflag = 1 has reached 100*(n+1).
**3** — tol is too small. no further reduction in the sum of squares is
possible.
**4** — Iteration is not making good progress.



```maxima

```

