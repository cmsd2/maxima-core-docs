## mnewton

### Function: mnewton (mnewton, FuncList, VarList, GuessList, mnewton, FuncList, VarList, GuessList, DF)

Approximate solution of multiple nonlinear equations by Newton’s method.


*FuncList* is a list of functions to solve,
*VarList* is a list of variable names, and
*GuessList* is a list of initial approximations.
The optional argument *DF* is the Jacobian matrix of the list of functions;
if not supplied, it is calculated automatically from *FuncList*.


*FuncList* may be specified as a list of equations,
in which case the function to be solved is the left-hand side of each equation minus the right-hand side.


If there is only a single function, variable, and initial point,
they may be specified as a single expression, variable, and initial value;
they need not be lists of one element.


A variable may be a simple symbol or a subscripted symbol.


The solution, if any, is returned as a list of one element,
which is a list of equations, one for each variable,
specifying an approximate solution;
this is the same format as returned by `solve`.
If the solution is not found, `[]` is returned.


Functions and initial points may contain complex numbers,
and solutions likewise may contain complex numbers.


`mnewton` is governed by global variables `newtonepsilon` and
`newtonmaxiter`, and the global flag `newtondebug`.


`load("mnewton")` loads this function.


See also `realroots`, `allroots`, `find_root` and
`newton`.


Examples:



```maxima
(%i1) load("mnewton")$

(%i2) mnewton([x1+3*log(x1)-x2^2, 2*x1^2-x1*x2-5*x1+1],
              [x1, x2], [5, 5]);
(%o2) [[x1 = 3.756834008012769, x2 = 2.779849592817897]]
(%i3) mnewton([2*a^a-5],[a],[1]);
(%o3)             [[a = 1.70927556786144]]
(%i4) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o4) [[u = 1.066618389595407, v = 1.552564766841786]]
```


The variable `newtonepsilon` controls the precision of the
approximations.  It also controls if computations are performed with
floats or bigfloats.



```maxima
(%i1) load("mnewton")$

(%i2) (fpprec : 25, newtonepsilon : bfloat(10^(-fpprec+5)))$

(%i3) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o3) [[u = 1.066618389595406772591173b0, 
                               v = 1.552564766841786450100418b0]]
```

See also: `newtonepsilon`, `newtonmaxiter`, `newtondebug`, `realroots`, `allroots`, `find_root`, `newton`.

### Variable: newtondebug

Default value: `false`


When `newtondebug` is `true`, 
`mnewton` prints out debugging information while solving a problem.

### Variable: newtonepsilon

Default value: `10.0^(-fpprec/2)`


Precision to determine when the `mnewton` function has converged towards
the solution.


When `newtonepsilon` is a bigfloat,
`mnewton` computations are done with bigfloats;
otherwise, ordinary floats are used.


See also `mnewton`.

See also: `mnewton`.

### Variable: newtonmaxiter

Default value: `50`


Maximum number of iterations to stop the `mnewton` function
if it does not converge or if it converges too slowly.


See also `mnewton`.

See also: `mnewton`.

