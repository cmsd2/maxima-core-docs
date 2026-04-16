## cobyla

### Function: bf_fmin_cobyla (bf_fmin_cobyla, F, X, Y, bf_fmin_cobyla, F, X, Y, optional_args)

This function is identical to `fmin_cobyla`, except that bigfloat
operations are used, and the default value for *rhoend* is
`10^(fpprec/2)`. 


See `fmin_cobyla` for more information.


`load("bf_fmin_cobyla")` loads this function.

See also: `fmin_cobyla`.

### Function: fmin_cobyla (fmin_cobyla, F, X, Y, fmin_cobyla, F, X, Y, optional_args)

Returns an approximate minimum of the expression *F* with respect
to the variables *X*, subject to an optional set of constraints.
*Y* is a list of initial guesses for *X*.


*F* must be ordinary expressions, not names of functions or lambda expressions.


`optional_args` represents additional arguments,
specified as `symbol = value`.
The optional arguments recognized are:



**constraints** — List of inequality and equality constraints that must be satisfied by
*X*.  The inequality constraints must be actual inequalities of
the form 
$g(X) \ge h(X)$
or 
$g(X) \le h(X).$
The equality constraints must be of the
form 
$g(X) = h(X).$
**rhobeg** — Initial value of the internal *RHO* variable which controls 
the size of simplex.  (Defaults to 1.0)
**rhoend** — The desired final value rho parameter.  It is approximately
 the accuracy in the variables. (Defaults to 1d-6.)
**iprint** — Verbose output level.  (Defaults to 0) 
- *
0 - No output
- *
1 - Summary at the end of the calculation
- *
2 - Each new value of RHO and SIGMA is printed, including 
 the vector of variables, some function information when RHO is reduced.
- *
3 - Like 2, but information is printed when F(X) is computed.
**maxfun** — The maximum number of function evaluations.  (Defaults to 1000).


On return, a vector is given:


1. The value of the variables giving the minimum.  This is a list of
elements of the form `var = value` for each of the
variables listed in *X*.
2. The minimized function value
3. The number of function evaluations.
4. Return code with the following meanings
 

  - 0 - No errors.
  - 1 - Limit on maximum number of function evaluations reached.
  - 2 - Rounding errors inhibiting progress.
  - -1 - *MAXCV* value exceeds *RHOEND*.  This indicates that the
  constraints were probably not satisfied.  User should investigate
  the value of the constraints.


*MAXCV* stands for “MAXimum Constraint Violation” and is the
value of $max(0.0, -c1(x), -c2(x),...-cm(x))$ where $ck(x)$
denotes the k’th constraint function.  (Note that maxima allows
constraints of the form $f(x) = g(x)$, which are internally
converted to $f(x)-g(x) >= 0$ and $g(x)-f(x) >= 0$ which is
required by COBYLA).


`load("fmin_cobyla")` loads this function.

