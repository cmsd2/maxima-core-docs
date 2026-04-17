## augmented_lagrangian

<!-- category: Other -->
<!-- keywords: augmented_lagrangian_method -->
<!-- signatures: augmented_lagrangian_method(FOM, xx, C, yy), augmented_lagrangian_method(FOM, xx, C, yy, optional_args), augmented_lagrangian_method([FOM, grad], xx, C, yy), augmented_lagrangian_method([FOM, grad], xx, C, yy, optional_args) -->
### Function: augmented_lagrangian_method (FOM, xx, C, yy)

Returns an approximate minimum of the expression *FOM*
with respect to the variables *xx*,
holding the constraints *C* equal to zero.
*yy* is a list of initial guesses for *xx*.
The method employed is the augmented Lagrangian method (see Refs [1] and [2]).


*grad*, if present, is the gradient of *FOM* with respect to *xx*,
represented as a list of expressions,
one for each variable in *xx*.
If not present, the gradient is constructed automatically.


*FOM* and each element of *grad*, if present,
must be ordinary expressions, not names of functions or lambda expressions.


`optional_args` represents additional arguments,
specified as `symbol = value`.
The optional arguments recognized are:



**niter** — Number of iterations of the augmented Lagrangian algorithm
**lbfgs_tolerance** — Tolerance supplied to LBFGS
**iprint** — IPRINT parameter (a list of two integers which controls verbosity) supplied to LBFGS
**%lambda** — Initial value of `%lambda` to be used for calculating the augmented Lagrangian


This implementation minimizes the augmented Lagrangian by
applying the limited-memory BFGS (LBFGS) algorithm,
which is a quasi-Newton algorithm.


`load("augmented_lagrangian")` loads this function.


See also `Package-lbfgs`


References:



[1] [http://www-fp.mcs.anl.gov/otc/Guide/OptWeb/continuous/constrained/nonlinearcon/auglag.html]()


[2] [http://www.cs.ubc.ca/spider/ascher/542/chap10.pdf]()


Examples:












```maxima
(%i1) load ("lbfgs");
(%o1)  /home/gunter/src/maxima-code/share/lbfgs/lbfgs.mac


(%i2) load ("augmented_lagrangian");
(%o2) /home/gunter/src/maxima-code/share/contrib/augmented_lagra\
ngian.mac


(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x


(%i4) xx: [x, y];
(%o4)                        [x, y]


(%i5) C: [x + y - 1];
(%o5)                      [y + x - 1]


(%i6) yy: [1, 1];
(%o6)                        [1, 1]


(%i7) augmented_lagrangian_method(FOM, xx, C, yy, iprint=[-1,0]);
(%o7) [[x = 0.666659841080023, y = 0.333340272455448], 
                                 %lambda = [- 1.333337940892518]]
```


Same example as before, but this time the gradient is supplied as an argument.














```maxima
(%i1) load ("lbfgs")$
(%i2) load ("augmented_lagrangian")$

(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x


(%i4) xx: [x, y];
(%o4)                        [x, y]


(%i5) grad : [2*x, 4*y];
(%o5)                      [2 x, 4 y]


(%i6) C: [x + y - 1];
(%o6)                      [y + x - 1]


(%i7) yy: [1, 1];
(%o7)                        [1, 1]


(%i8) augmented_lagrangian_method ([FOM, grad], xx, C, yy,
                             iprint = [-1, 0]);
(%o8) [[x = 0.6666598410800247, y = 0.3333402724554464], 
                                 %lambda = [- 1.333337940892525]]
```

See also: `Package-lbfgs`.

