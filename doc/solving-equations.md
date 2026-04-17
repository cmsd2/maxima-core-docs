## Equations

<!-- category: Solving -->
<!-- keywords: %rnum -->
<!-- signatures: %rnum -->
### Variable: %rnum

Default value: `0`


`%rnum` is the counter for the `%r` variables introduced in solutions by
`solve` and `algsys`..  The next `%r` variable is numbered
`%rnum+1`.


See also `%rnum_list`.

See also: `solve`, `algsys`, `%rnum_list`.

<!-- category: Solving -->
<!-- keywords: %rnum_list -->
<!-- signatures: %rnum_list -->
### Variable: %rnum_list

Default value: `[]`


`%rnum_list` is the list of variables introduced in solutions by
`solve` and `algsys`.  `%r` variables are added to
`%rnum_list` in the order they are created.  This is convenient for doing
substitutions into the solution later on.


See also `%rnum`.



It’s recommended to use this list rather than doing `concat ('%r, j)`.












```maxima
maxima

(%i1) solve ([x + y = 3], [x,y]);
(%o1)               [[x = 3 - %r1, y = %r1]]


(%i2) %rnum_list;
(%o2)                         [%r1]


(%i3) sol : solve ([x + 2*y + 3*z = 4], [x,y,z]);
(%o3)     [[x = - 2 %r3 - 3 %r2 + 4, y = %r3, z = %r2]]


(%i4) %rnum_list;
(%o4)                      [%r2, %r3]


(%i5) for i : 1 thru length (%rnum_list) do
  sol : subst (t[i], %rnum_list[i], sol)$


(%i6) sol;
(%o6)       [[x = - 2 t  - 3 t  + 4, y = t , z = t ]]
                       2      1           2       1
```

See also: `solve`, `algsys`, `%rnum`.

<!-- category: Solving -->
<!-- keywords: algepsilon -->
<!-- signatures: algepsilon -->
### Variable: algepsilon

Default value: 10^8



`algepsilon` is used by `algsys`.

See also: `algsys`.

<!-- category: Solving -->
<!-- keywords: algexact -->
<!-- signatures: algexact -->
### Variable: algexact

Default value: `false`


`algexact` affects the behavior of `algsys` as follows:


If `algexact` is `true`, `algsys` always calls `solve` and
then uses `realroots` on `solve`’s failures.


If `algexact` is `false`, `solve` is called only if the
eliminant was not univariate, or if it was a quadratic or biquadratic.


Thus `algexact: true` does not guarantee only exact solutions, just that
`algsys` will first try as hard as it can to give exact solutions, and
only yield approximations when all else fails.

See also: `algsys`, `solve`, `realroots`.

<!-- category: Solving -->
<!-- keywords: algsys -->
<!-- signatures: algsys([expr_1, ..., expr_m], [x_1, ..., x_n]), algsys([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: algsys ([expr_1, ..., expr_m], [x_1, ..., x_n])

Solves the simultaneous polynomials *expr_1*, ..., *expr_m* or
polynomial equations *eqn_1*, ..., *eqn_m* for the variables
*x_1*, ..., *x_n*.  An expression *expr* is equivalent to an
equation `expr = 0`.  There may be more equations than variables or
vice versa.


`algsys` returns a list of solutions, with each solution given as a list
of equations stating values of the variables *x_1*, ..., *x_n*
which satisfy the system of equations.  If `algsys` cannot find a solution,
an empty list `[]` is returned.


The symbols `%r1`, `%r2`, ..., are introduced as needed to
represent arbitrary parameters in the solution; these variables are also
appended to the list `_0025rnum_005flist`.


The method is as follows:



1. First the equations are factored and split into subsystems.
2. For each subsystem *S_i*, an equation *E* and a variable *x* are
selected.  The variable is chosen to have lowest nonzero degree.  Then the
resultant of *E* and *E_j* with respect to *x* is computed for each
of the remaining equations *E_j* in the subsystem *S_i*.  This yields a
new subsystem *S_i’* in one fewer variables, as *x* has been eliminated.
The process now returns to (1).
3. Eventually, a subsystem consisting of a single equation is obtained.  If the
equation is multivariate and no approximations in the form of floating point
numbers have been introduced, then `solve` is called to find an exact
solution.


In some cases, `solve` is not be able to find a solution, or if it does
the solution may be a very large expression.



If the equation is univariate and is either linear, quadratic, or biquadratic,
then again `solve` is called if no approximations have been introduced.
If approximations have been introduced or the equation is not univariate and
neither linear, quadratic, or biquadratic, then if the switch
`realonly` is `true`, the function `realroots` is called to find
the real-valued solutions.  If `realonly` is `false`, then
`allroots` is called which looks for real and complex-valued solutions.


If `algsys` produces a solution which has fewer significant digits than
required, the user can change the value of `algepsilon` to a higher value.


If `algexact` is set to `true`, `solve` will always be called.
4. Finally, the solutions obtained in step (3) are substituted into
previous levels and the solution process returns to (1).


When `algsys` encounters a multivariate equation which contains floating
point approximations (usually due to its failing to find exact solutions at an
earlier stage), then it does not attempt to apply exact methods to such
equations and instead prints the message:
"`algsys` cannot solve - system too complicated."


Interactions with `radcan` can produce large or complicated expressions.
In that case, it may be possible to isolate parts of the result with
`pickapart` or `reveal`.


Occasionally, `radcan` may introduce an imaginary unit `%i` into a
solution which is actually real-valued.


Examples:













```maxima
maxima

(%i1) e1: 2*x*(1 - a1) - 2*(x - 1)*a2;
(%o1)              2 (1 - a1) x - 2 a2 (x - 1)


(%i2) e2: a2 - a1;
(%o2)                        a2 - a1


(%i3) e3: a1*(-y - x^2 + 1);
                                   2
(%o3)                   a1 (- y - x  + 1)


(%i4) e4: a2*(y - (x - 1)^2);
                                       2
(%o4)                   a2 (y - (x - 1) )


(%i5) algsys ([e1, e2, e3, e4], [x, y, a1, a2]);
(%o5) [[x = 0, y = %r1, a1 = 0, a2 = 0], 
                                  [x = 1, y = 0, a1 = 1, a2 = 1]]


(%i6) e1: x^2 - y^2;
                              2    2
(%o6)                        x  - y


(%i7) e2: -1 - y + 2*y^2 - x + x^2;
                         2        2
(%o7)                 2 y  - y + x  - x - 1


(%i8) algsys ([e1, e2], [x, y]);
                 1            1
(%o8) [[x = - -------, y = -------], 
              sqrt(3)      sqrt(3)
        1              1             1        1
[x = -------, y = - -------], [x = - -, y = - -], [x = 1, y = 1]]
     sqrt(3)        sqrt(3)          3        3
```

See also: `%rnum_list`, `solve`, `realonly`, `realroots`, `allroots`, `algepsilon`, `radcan`, `pickapart`, `reveal`.

<!-- category: Solving -->
<!-- keywords: allroots -->
<!-- signatures: allroots(expr), allroots(eqn) -->
### Function: allroots (expr)

Computes numerical approximations of the real and complex roots of the
polynomial *expr* or polynomial equation *eqn* of one variable.


The flag `polyfactor` when `true` causes `allroots` to factor
the polynomial over the real numbers if the polynomial is real, or over the
complex numbers, if the polynomial is complex.


`allroots` may give inaccurate results in case of multiple roots.
If the polynomial is real, `allroots (%i*p)` may yield
more accurate approximations than `allroots (p)`, as `allroots`
invokes a different algorithm in that case.


`allroots` rejects non-polynomials.  It requires that the numerator
after `rat`’ing should be a polynomial, and it requires that the
denominator be at most a complex number.  As a result of this `allroots`
will always return an equivalent (but factored) expression, if
`polyfactor` is `true`.


For complex polynomials an algorithm by Jenkins and Traub is used
(Algorithm 419, *Comm. ACM*, vol. 15, (1972), p. 97).  For real polynomials
the algorithm used is due to Jenkins (Algorithm 493, *ACM TOMS*, vol. 1,
(1975), p.178).


Examples:











```maxima
maxima

(%i1) eqn: (1 + 2*x)^3 = 13.5*(1 + x^5);
                            3          5
(%o1)              (2 x + 1)  = 13.5 (x  + 1)


(%i2) soln: allroots (eqn);
(%o2) [x = 0.8296749902129361, x = - 1.0157555438281212, 
x = 0.9659625152196369 %i - 0.4069597231924075, 
x = - 0.9659625152196369 %i - 0.4069597231924075, x = 1.0]


(%i3) for e in soln
        do (e2: subst (e, eqn), disp (expand (lhs(e2) - rhs(e2))));
                     - 3.552713678800501e-15

                     - 8.43769498715119e-15

        2.6645352591003757e-15 %i - 6.217248937900877e-15

       - 2.6645352591003757e-15 %i - 6.217248937900877e-15

                               0.0

(%o3)                         done

(%i4) polyfactor: true$

(%i5) allroots (eqn);
(%o5) - 13.5 (x - 1.0) (x - 0.8296749902129361)
                            2
 (x + 1.0157555438281212) (x  + 0.813919446384815 x
 + 1.0986997971102883)
```

See also: `polyfactor`.

<!-- category: Solving -->
<!-- keywords: backsubst -->
<!-- signatures: backsubst -->
### Variable: backsubst

Default value: `true`




When `backsubst` is `false`, prevents back substitution in
`linsolve` after the equations have been triangularized.  This may
be helpful in very big problems where back substitution would cause
the generation of extremely large expressions.












```maxima
maxima
(%i1) eq1 : x + y + z = 6$
(%i2) eq2 : x - y + z = 2$
(%i3) eq3 : x + y - z = 0$
(%i4) backsubst : false$

(%i5) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o5)               [x = z - y, y = 2, z = 3]

(%i6) backsubst : true$

(%i7) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o7)                 [x = 1, y = 2, z = 3]
```

See also: `linsolve`.

<!-- category: Solving -->
<!-- keywords: bfallroots -->
<!-- signatures: bfallroots(expr), bfallroots(eqn) -->
### Function: bfallroots (expr)

Computes numerical approximations of the real and complex roots of the
polynomial *expr* or polynomial equation *eqn* of one variable.


In all respects, `bfallroots` is identical to `allroots` except
that `bfallroots` computes the roots using bigfloats.  See 
`allroots` for more information.

See also: `allroots`.

<!-- category: Solving -->
<!-- keywords: breakup -->
<!-- signatures: breakup -->
### Variable: breakup

Default value: `true`


When `breakup` is `true`, `solve` expresses solutions of cubic
and quartic equations in terms of common subexpressions, which are assigned to
intermediate expression labels (`%t1`, `%t2`, etc.).
Otherwise, common subexpressions are not identified.


`breakup: true` has an effect only when `programmode` is `false`.


Examples:










```maxima
maxima
(%i1) programmode: false$
(%i2) breakup: true$

(%i3) solve (x^3 + x^2 - 1);
                        sqrt(23)   25 1/3
(%t3)                  (-------- + --)
                            3/2    54
                         2 3
solve: solution:

                                    sqrt(3) %i   - 1
                                    ---------- + ---
            - 1   sqrt(3) %i            2         2    - 1
(%t4)  x = (--- - ----------) %t3 + ---------------- + ---
             2        2                  9 %t3          3

                                    - 1   sqrt(3) %i
                                    --- - ----------
            sqrt(3) %i   - 1         2        2        - 1
(%t5)  x = (---------- + ---) %t3 + ---------------- + ---
                2         2              9 %t3          3

                                  1     - 1
(%t6)                 x = %t3 + ----- + ---
                                9 %t3    3
(%o6)                    [%t4, %t5, %t6]

(%i7) breakup: false$

(%i8) solve (x^3 + x^2 - 1);
solve: solution:

            sqrt(3) %i   - 1
            ---------- + ---
                2         2       sqrt(23)   25 1/3
(%t8) x = -------------------- + (-------- + --)
             sqrt(23)   25 1/3        3/2    54
          9 (-------- + --)        2 3
                 3/2    54
              2 3
                                          - 1   sqrt(3) %i    - 1
                                         (--- - ----------) + ---
                                           2        2          3

           sqrt(23)   25 1/3  sqrt(3) %i   - 1
(%t9) x = (-------- + --)    (---------- + ---)
               3/2    54          2         2
            2 3
                                         - 1   sqrt(3) %i
                                         --- - ----------
                                          2        2          - 1
                                     + -------------------- + ---
                                          sqrt(23)   25 1/3    3
                                       9 (-------- + --)
                                              3/2    54
                                           2 3

            sqrt(23)   25 1/3            1             - 1
(%t10) x = (-------- + --)    + -------------------- + ---
                3/2    54          sqrt(23)   25 1/3    3
             2 3                9 (-------- + --)
                                       3/2    54
                                    2 3
(%o10)                  [%t8, %t9, %t10]
```

See also: `solve`, `programmode`.

<!-- category: Solving -->
<!-- keywords: dimension -->
<!-- signatures: dimension(eqn), dimension(eqn_1, ..., eqn_n) -->
### Function: dimension (eqn)

`dimen` is a package for dimensional analysis.
`load ("dimen")` loads this package.
`demo ("dimen")` displays a short demonstration.

<!-- category: Solving -->
<!-- keywords: dispflag -->
<!-- signatures: dispflag -->
### Variable: dispflag

Default value: `true`



If set to `false` within a `block` will inhibit the display of output
generated by the solve functions called from within the `block`.
Termination of the `block` with a dollar sign, `$`, sets `dispflag` to
`false`.

<!-- category: Solving -->
<!-- keywords: funcsolve -->
<!-- signatures: funcsolve(eqn, g(t)) -->
### Function: funcsolve (eqn, g(t))

Returns `[g(t) = ...]`  or `[]`, depending on whether
or not there exists a rational function `g(t)` satisfying
*eqn*, which must be a first order, linear polynomial in (for this case)
`g(t)` and `g(t+1)`








```maxima
maxima

(%i1) eqn: (n + 1)*f(n) - (n + 3)*f(n + 1)/(n + 1) =
     (n - 1)/(n + 2);
                            (n + 3) f(n + 1)   n - 1
(%o1)        (n + 1) f(n) - ---------------- = -----
                                 n + 1         n + 2


(%i2) funcsolve (eqn, f(n));
solve: dependent equations eliminated: (4 3)
                                   n
(%o2)                f(n) = ---------------
                            (n + 1) (n + 2)
```


Warning: this is a very rudimentary implementation – many safety checks
and obvious generalizations are missing.

<!-- category: Solving -->
<!-- keywords: globalsolve -->
<!-- signatures: globalsolve -->
### Variable: globalsolve

Default value: `false`


When `globalsolve` is `true`, solved-for variables are assigned the
solution values found by `linsolve`, and by `solve` when solving two
or more linear equations.


When `globalsolve` is `false`, solutions found by `linsolve` and
by `solve` when solving two or more linear equations are expressed as
equations, and the solved-for variables are not assigned.


When solving anything other than two or more linear equations, `solve`
ignores `globalsolve`.  Other functions which solve equations (e.g.,
`algsys`) always ignore `globalsolve`.


Examples:














```maxima
maxima
(%i1) globalsolve: true$

(%i2) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
                             17        1
(%o2)                  [[x : --, y : - -]]
                             7         7


(%i3) x;
                               17
(%o3)                          --
                               7


(%i4) y;
                                 1
(%o4)                          - -
                                 7

(%i5) globalsolve: false$
(%i6) kill (x, y)$

(%i7) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
                             17        1
(%o7)                  [[x = --, y = - -]]
                             7         7


(%i8) x;
(%o8)                           x


(%i9) y;
(%o9)                           y
```

See also: `solve`, `linsolve`, `algsys`.

<!-- category: Solving -->
<!-- keywords: ieqn -->
<!-- signatures: ieqn(ie, unk, tech, n, guess) -->
### Function: ieqn (ie, unk, tech, n, guess)

`inteqn` is a package for solving integral equations.
`load ("inteqn")` loads this package.


*ie* is the integral equation; *unk* is the unknown function;
*tech* is the technique to be tried from those given in the lists
below; (*tech* = `first` means: try the first technique which
finds a solution; *tech* = `all` means: try all applicable
techniques); *n* is the maximum number of terms to take for
`taylor`, `neumann`, `firstkindseries`, or
`fredseries` (it is also the maximum depth of recursion for the
differentiation method); *guess* is the initial guess for
`neumann` or `firstkindseries`.


Two types of equations are considered. A second-kind equation of the
following form,


```maxima
b(x)
                          /
                          [
        p(x) = q(x, p(x), I     w(x, u, p(x), p(u)) du)
                          ]
                          /
                           a(x)
```


$$p\left(x\right)=q\left(x, p\left(x\right) , \int_{a\left(x\right)}
^{b\left(x\right)}{w\left(x, u, p\left(x\right), p\left(u\right)\right)
\;du}\right)$$


and a first-kind equation with the form


```maxima
b(x)
                        /
                        [
                 f(x) = I     w(x, u, p(u)) du
                        ]
                        /
                         a(x)
```


$$f\left(x\right)=\int_{a\left(x\right)}^{b\left(x\right)}
{w\left(x, u, p\left(u\right)\right)\;du}$$


The different solution techniques used require particular forms of the
expressions *q* and *w*. The techniques available are the following:


**Second-kind equations**


- * 
`flfrnk2nd`: For fixed-limit, finite-rank integrands.
- * 
`vlfrnk`: For variable-limit, finite-rank integrands.
- * 
`transform`: Laplace transform for convolution types.
- * 
`fredseries`: Fredholm-Carleman series for linear equations.
- * 
`tailor`: Taylor series for quasi-linear variable-limit equations.
- * 
`neumann`: Neumann series for quasi-second kind equations.
- * 
`collocate`: Collocation using a power series form for p(x)
evaluated at equally spaced points.


**First-kind equations**


- * 
`flfrnk1st`: For fixed-limit, finite-rank integrands.
- * 
`vlfrnk`: For variable-limit, finite-rank integrands.
- * 
`abel`: For singular integrands
- * 
`transform`: See above
- * 
`collocate`: See above
- * 
`firstkindseries`: Iteration technique similar to neumann series.


The default values for the 2nd thru 5th parameters in the calling form
are:


*unk*: `p(x)`, where *p* is the first function
encountered in an integrand which is unknown to Maxima and *x* is the
variable which occurs as an argument to the first occurrence of *p* found
outside of an integral in the case of `secondkind` equations, or is the
only other variable besides the variable of integration in `firstkind`
equations. If the attempt to search for *x* fails, the user will be asked
to supply the independent variable. *tech*: `first`. *n*: 1.
*guess*: `none` which will cause `neumann` and
`firstkindseries` to use `f(x)` as an initial guess.


Examples:


```maxima
(%i1) load("inteqn")$

(%i2) e: p(x) - 1 -x + cos(x) + 'integrate(cos(x-u)*p(u),u,0,x)$

(%i3) ieqn(e, p(x), 'transform);
default 4th arg, number of iterations or coll. parms.:  1 
default 5th arg, initial guess:  none 

(%t3)                           [x, transform]
(%o3)                               [%t3]
(%i4) e: 2*'integrate(p(x*sin(u)), u, 0, %pi/2) - a*x - b$

(%i5) ieqn(e, p(x), 'firstkindseries);
default 4th arg, number of iterations or coll. parms.:  1 
default 5th arg, initial guess:  none 

(%t5)          [2 a x + %pi b, firstkindseries, 1, approximate]
(%o5)                               [%t5]
```

<!-- category: Solving -->
<!-- keywords: ieqnprint -->
<!-- signatures: ieqnprint -->
### Variable: ieqnprint

Default value: `true`


`ieqnprint` governs the behavior of the result returned by the
`ieqn` command.  When `ieqnprint` is `false`, the lists returned
by the `ieqn` function are of the form


   

[*solution*, *technique used*, *nterms*, *flag*]


where *flag* is absent if the solution is exact.


Otherwise, it is the word `approximate` or `incomplete` corresponding
to an inexact or non-closed form solution, respectively.  If a series method was
used, *nterms* gives the number of terms taken (which could be less than
the n given to `ieqn` if an error prevented generation of further terms).

See also: `ieqn`.

<!-- category: Solving -->
<!-- keywords: lhs -->
<!-- signatures: lhs(expr) -->
### Function: lhs (expr)

Returns the left-hand side (that is, the first argument) of the expression
*expr*, when the operator of *expr* is one of the relational operators
`< <= = # equal notequal >= >`,

one of the assignment operators `:= ::= : ::`, or a user-defined binary
infix operator, as declared by `infix`.


When *expr* is an atom or its operator is something other than the ones
listed above, `lhs` returns *expr*.


See also `rhs`.


Examples:



















```maxima
maxima

(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc


(%i2) lhs (e);
(%o2)                        bb + aa


(%i3) rhs (e);
(%o3)                          cc


(%i4) [lhs (aa < bb), lhs (aa <= bb), lhs (aa >= bb),
       lhs (aa > bb)];
(%o4)                   [aa, aa, aa, aa]


(%i5) [lhs (aa = bb), lhs (aa # bb), lhs (equal (aa, bb)),
       lhs (notequal (aa, bb))];
(%o5)                   [aa, aa, aa, aa]


(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x


(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y


(%i8) e3: '(x : y);
(%o8)                         x : y


(%i9) e4: '(x :: y);
(%o9)                        x :: y


(%i10) [lhs (e1), lhs (e2), lhs (e3), lhs (e4)];
(%o10)               [foo(x), bar(y), x, x]


(%i11) infix ("][");
(%o11)                         ][


(%i12) lhs (aa ][ bb);
(%o12)                         aa
```

See also: `infix`, `rhs`.

<!-- category: Solving -->
<!-- keywords: linsolve -->
<!-- signatures: linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

Solves the list of simultaneous linear equations for the list of variables.
The expressions must each be polynomials in the variables and may be equations.
If the length of the list of variables doesn’t match the number of
linearly-independent equations to solve the result will be an empty list.


When `globalsolve` is `true`, each solved-for variable is bound to
its value in the solution of the equations.


When `backsubst` is `false`, `linsolve` does not carry out back
substitution after the equations have been triangularized.  This may be
necessary in very big problems where back substitution would cause the
generation of extremely large expressions.


When `linsolve_params` is `true`, `linsolve` also generates the
`%r` symbols used to represent arbitrary parameters described in the manual
under `algsys`.  Otherwise, `linsolve` solves an under-determined
system of equations with some variables expressed in terms of others.


When `programmode` is `false`, `linsolve` displays the solution
with intermediate expression (`%t`) labels, and returns the list of labels.


See also `algsys`, `eliminate`. and `solve`.


Examples:



















```maxima
maxima

(%i1) e1: x + z = y;
(%o1)                       z + x = y


(%i2) e2: 2*a*x - y = 2*a^2;
                                       2
(%o2)                   2 a x - y = 2 a


(%i3) e3: y - 2*z = 2;
(%o3)                      y - 2 z = 2


(%i4) [globalsolve: false, programmode: true];
(%o4)                     [false, true]


(%i5) linsolve ([e1, e2, e3], [x, y, z]);
(%o5)            [x = a + 1, y = 2 a, z = a - 1]


(%i6) [globalsolve: false, programmode: false];
(%o6)                    [false, false]


(%i7) linsolve ([e1, e2, e3], [x, y, z]);
Solution:

(%t7)                       z = a - 1

(%t8)                        y = 2 a

(%t9)                       x = a + 1
(%o9)                    [%t7, %t8, %t9]


(%i10) ''%;
(%o10)           [z = a - 1, y = 2 a, x = a + 1]


(%i11) [globalsolve: true, programmode: false];
(%o11)                    [true, false]


(%i12) linsolve ([e1, e2, e3], [x, y, z]);
Solution:

(%t12)                      z : a - 1

(%t13)                       y : 2 a

(%t14)                      x : a + 1
(%o14)                 [%t12, %t13, %t14]


(%i15) ''%;
(%o15)           [z : a - 1, y : 2 a, x : a + 1]


(%i16) [x, y, z];
(%o16)                 [a + 1, 2 a, a - 1]


(%i17) [globalsolve: true, programmode: true];
(%o17)                    [true, true]


(%i18) linsolve ([e1, e2, e3], '[x, y, z]);
(%o18)           [x : a + 1, y : 2 a, z : a - 1]


(%i19) [x, y, z];
(%o19)                 [a + 1, 2 a, a - 1]
```

See also: `globalsolve`, `backsubst`, `linsolve_params`, `algsys`, `programmode`, `eliminate`, `solve`.

<!-- category: Solving -->
<!-- keywords: linsolve_params -->
<!-- signatures: linsolve_params -->
### Variable: linsolve_params

Default value: `true`


When `linsolve_params` is `true`, `linsolve` also generates
the `%r` symbols used to represent arbitrary parameters described in
the manual under `algsys`.  Otherwise, `linsolve` solves an
under-determined system of equations with some variables expressed in terms of
others.

See also: `linsolve`, `algsys`.

<!-- category: Solving -->
<!-- keywords: linsolvewarn -->
<!-- signatures: linsolvewarn -->
### Variable: linsolvewarn

Default value: `true`


When `linsolvewarn` is `true`, `linsolve` prints a message
"Dependent equations eliminated".

See also: `linsolve`.

<!-- category: Solving -->
<!-- keywords: multiplicities -->
<!-- signatures: multiplicities -->
### Variable: multiplicities

Default value: `not_set_yet`


`multiplicities` is set to a list of the multiplicities of the individual
solutions returned by `solve` or `realroots`.

See also: `solve`, `realroots`.

<!-- category: Solving -->
<!-- keywords: nroots -->
<!-- signatures: nroots(p, low, high) -->
### Function: nroots (p, low, high)

Returns the number of real roots of the real univariate polynomial *p* in
the half-open interval `(low, high]`.  The endpoints of the
interval may be `minf` or `inf`.


`nroots` uses the method of Sturm sequences.







```maxima
maxima
(%i1) p: x^10 - 2*x^4 + 1/2$

(%i2) nroots (p, -6, 9.1);
(%o2)                           4
```

<!-- category: Solving -->
<!-- keywords: nthroot -->
<!-- signatures: nthroot(p, n) -->
### Function: nthroot (p, n)

where *p* is a polynomial with integer coefficients and *n* is a
positive integer returns `q`, a polynomial over the integers, such that
`q^n = p` or prints an error message indicating that *p* is not a
perfect nth power.  This routine is much faster than `factor` or even
`sqfr`.

See also: `factor`, `sqfr`.

<!-- category: Solving -->
<!-- keywords: polyfactor -->
<!-- signatures: polyfactor -->
### Variable: polyfactor

Default value: `false`


The option variable `polyfactor` when `true` causes
`allroots` and `bfallroots` to factor the polynomial over the real
numbers if the polynomial is real, or over the complex numbers, if the
polynomial is complex.


See `allroots` for an example.

See also: `allroots`, `bfallroots`.

<!-- category: Solving -->
<!-- keywords: programmode -->
<!-- signatures: programmode -->
### Variable: programmode

Default value: `true`


When `programmode` is `true`, `solve`,
`realroots`, `allroots`, and `linsolve` return solutions
as elements in a list.

(Except when `backsubst` is set to `false`, in which case
`programmode: false` is assumed.)


When `programmode` is `false`, `solve`, etc. create intermediate
expression labels `%t1`, `%t2`, etc., and assign the solutions to them.

See also: `solve`, `realroots`, `allroots`, `linsolve`, `backsubst`.

<!-- category: Solving -->
<!-- keywords: realonly -->
<!-- signatures: realonly -->
### Variable: realonly

Default value: `false`


When `realonly` is `true`, `algsys` returns only those solutions
which are free of `%i`.

See also: `algsys`.

<!-- category: Solving -->
<!-- keywords: realroots -->
<!-- signatures: realroots(expr, bound), realroots(eqn, bound), realroots(expr), realroots(eqn) -->
### Function: realroots (expr, bound)

Computes rational approximations of the real roots of the polynomial *expr*
or polynomial equation *eqn* of one variable, to within a tolerance of
*bound*.  Coefficients of *expr* or *eqn* must be literal numbers;
symbol constants such as `%pi` are rejected.


`realroots` assigns the multiplicities of the roots it finds
to the global variable `multiplicities`.


`realroots` constructs a Sturm sequence to bracket each root, and then
applies bisection to refine the approximations.  All coefficients are converted
to rational equivalents before searching for roots, and computations are carried
out by exact rational arithmetic.  Even if some coefficients are floating-point
numbers, the results are rational (unless coerced to floats by the
`float` or `numer` flags).


When *bound* is less than 1, all integer roots are found exactly.
When *bound* is unspecified, it is assumed equal to the global variable
`rootsepsilon`.


When the global variable `programmode` is `true`, `realroots`
returns a list of the form `[x = x_1, x = x_2, ...]`.
When `programmode` is `false`, `realroots` creates intermediate
expression labels `%t1`, `%t2`, ...,
assigns the results to them, and returns the list of labels.


See also `allroots`, `bfallroots`, `guess_exact_value`,
and `lhs`.


Examples:








```maxima
maxima

(%i1) realroots (-1 - x + x^5, 5e-6);
                               612003
(%o1)                     [x = ------]
                               524288


(%i2) ev (%[1], float);
(%o2)                x = 1.1673030853271484


(%i3) ev (-1 - x + x^5, %);
(%o3)                - 7.396496210176906e-6
```







```maxima
maxima

(%i1) realroots (expand ((1 - x)^5 * (2 - x)^3 * (3 - x)), 1e-20);
(%o1)                 [x = 1, x = 2, x = 3]


(%i2) multiplicities;
(%o2)                       [5, 3, 1]
```

See also: `multiplicities`, `float`, `numer`, `rootsepsilon`, `programmode`, `allroots`, `bfallroots`, `guess_exact_value`, `lhs`.

<!-- category: Solving -->
<!-- keywords: rhs -->
<!-- signatures: rhs(expr) -->
### Function: rhs (expr)

Returns the right-hand side (that is, the second argument) of the expression
*expr*, when the operator of *expr* is one of the relational operators
`< <= = # equal notequal >= >`,

one of the assignment operators `:= ::= : ::`, or a user-defined binary
infix operator, as declared by `infix`.


When *expr* is an atom or its operator is something other than the ones
listed above, `rhs` returns 0.


See also `lhs`.


Examples:



















```maxima
maxima

(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc


(%i2) lhs (e);
(%o2)                        bb + aa


(%i3) rhs (e);
(%o3)                          cc


(%i4) [rhs (aa < bb), rhs (aa <= bb), rhs (aa >= bb),
       rhs (aa > bb)];
(%o4)                   [bb, bb, bb, bb]


(%i5) [rhs (aa = bb), rhs (aa # bb), rhs (equal (aa, bb)),
       rhs (notequal (aa, bb))];
(%o5)                   [bb, bb, bb, bb]


(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x


(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y


(%i8) e3: '(x : y);
(%o8)                         x : y


(%i9) e4: '(x :: y);
(%o9)                        x :: y


(%i10) [rhs (e1), rhs (e2), rhs (e3), rhs (e4)];
(%o10)                  [2 x, 3 y, y, y]


(%i11) infix ("][");
(%o11)                         ][


(%i12) rhs (aa ][ bb);
(%o12)                         bb
```

See also: `infix`, `lhs`.

<!-- category: Solving -->
<!-- keywords: rootsconmode -->
<!-- signatures: rootsconmode -->
### Variable: rootsconmode

Default value: `true`


`rootsconmode` governs the behavior of the `rootscontract` command.
See `rootscontract` for details.

See also: `rootscontract`.

<!-- category: Solving -->
<!-- keywords: rootscontract -->
<!-- signatures: rootscontract(expr) -->
### Function: rootscontract (expr)

Converts products of roots into roots of products.  For example,
`rootscontract (sqrt(x)*y^(3/2))` yields `sqrt(x*y^3)`.


When `radexpand` is `true` and `domain` is `real`,
`rootscontract` converts `abs` into `sqrt`,  e.g.,
`rootscontract (abs(x)*sqrt(y))` yields `sqrt(x^2*y)`.


There is an option `rootsconmode` affecting `rootscontract` as
follows:



```maxima
Problem            Value of        Result of applying
                  rootsconmode        rootscontract
      
x^(1/2)*y^(3/2)      false          (x*y^3)^(1/2)
x^(1/2)*y^(1/4)      false          x^(1/2)*y^(1/4)
x^(1/2)*y^(1/4)      true           (x*y^(1/2))^(1/2)
x^(1/2)*y^(1/3)      true           x^(1/2)*y^(1/3)
x^(1/2)*y^(1/4)      all            (x^2*y)^(1/4)
x^(1/2)*y^(1/3)      all            (x^3*y^2)^(1/6)
```


When `rootsconmode` is `false`, `rootscontract` contracts only
with respect to rational number exponents whose denominators are the same.  The
key to the `rootsconmode: true` examples is simply that 2 divides into 4
but not into 3.  `rootsconmode: all` involves taking the least common
multiple of the denominators of the exponents.


`rootscontract` uses `ratsimp` in a manner similar to
`logcontract`.


Examples:



















```maxima
maxima
(%i1) rootsconmode: false$

(%i2) rootscontract (x^(1/2)*y^(3/2));
                                   3
(%o2)                      sqrt(x y )


(%i3) rootscontract (x^(1/2)*y^(1/4));
                                   1/4
(%o3)                     sqrt(x) y

(%i4) rootsconmode: true$

(%i5) rootscontract (x^(1/2)*y^(1/4));
(%o5)                    sqrt(x sqrt(y))


(%i6) rootscontract (x^(1/2)*y^(1/3));
                                   1/3
(%o6)                     sqrt(x) y

(%i7) rootsconmode: all$

(%i8) rootscontract (x^(1/2)*y^(1/4));
                              2   1/4
(%o8)                       (x  y)


(%i9) rootscontract (x^(1/2)*y^(1/3));
                             3  2 1/6
(%o9)                      (x  y )

(%i10) rootsconmode: false$

(%i11) rootscontract (sqrt(sqrt(x) + sqrt(1 + x))
                    *sqrt(sqrt(1 + x) - sqrt(x)));
(%o11)                          1

(%i12) rootsconmode: true$

(%i13) rootscontract (sqrt(5 + sqrt(5)) - 5^(1/4)*sqrt(1 + sqrt(5)));
(%o13)                          0
```

See also: `radexpand`, `domain`, `abs`, `sqrt`, `rootsconmode`, `ratsimp`, `logcontract`.

<!-- category: Solving -->
<!-- keywords: rootsepsilon -->
<!-- signatures: rootsepsilon -->
### Variable: rootsepsilon

Default value: 1.0e-7


`rootsepsilon` is the tolerance which establishes the confidence interval
for the roots found by the `realroots` function.

See also: `realroots`.

<!-- category: Solving -->
<!-- keywords: solve -->
<!-- signatures: solve(expr, x), solve(expr), solve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: solve (expr, x)

Solves the algebraic equation *expr* for the variable *x* and returns a
list of solution equations in *x*.  If *expr* is not an equation, the
equation `expr = 0` is assumed in its place.
*x* may be a function (e.g. `f(x)`), or other non-atomic expression
except a sum or product.  *x* may be omitted if *expr* contains only one
variable.  *expr* may be a rational expression, and may contain
trigonometric functions, exponentials, etc.


The following method is used:


Let *E* be the expression and *X* be the variable.  If *E* is linear
in *X* then it is trivially solved for *X*.  Otherwise if *E* is of
the form `A*X^N + B` then the result is `(-B/A)^1/N)` times the
`N`’th roots of unity.


If *E* is not linear in *X* then the gcd of the exponents of *X* in
*E* (say *N*) is divided into the exponents and the multiplicity of the
roots is multiplied by *N*.  Then `solve` is called again on the
result.  If *E* factors then `solve` is called on each of the factors.
Finally `solve` will use the quadratic, cubic, or quartic formulas where
necessary.


In the case where *E* is a polynomial in some function of the variable to be
solved for, say `F(X)`, then it is first solved for `F(X)` (call the
result *C*), then the equation `F(X)=C` can be solved for *X*
provided the inverse of the function *F* is known.


`breakup` if `false` will cause `solve` to express the solutions
of cubic or quartic equations as single expressions rather than as made
up of several common subexpressions which is the default.


`multiplicities` - will be set to a list of the multiplicities of the
individual solutions returned by `solve`, `realroots`, or
`allroots`.  Try `apropos (solve)` for the switches which affect
`solve`.  `describe` may then by used on the individual switch names
if their purpose is not clear.


`solve ([eqn_1, ..., eqn_n], [x_1, ..., x_n])`
solves a system of simultaneous (linear or non-linear) polynomial equations by
calling `linsolve` or `algsys` and returns a list of the solution
lists in the variables.  In the case of `linsolve` this list would contain
a single list of solutions.  It takes two lists as arguments.  The first list
represents the equations to be solved; the second list is a
list of the unknowns to be determined.  If the total number of
variables in the equations is equal to the number of equations, the
second argument-list may be omitted.







When `programmode` is `false`, `solve` displays solutions with
intermediate expression (`%t`) labels, and returns the list of labels.


When `globalsolve` is `true` and the problem is to solve two or more
linear equations, each solved-for variable is bound to its value in the solution
of the equations.


Examples:


















```maxima
maxima

(%i1) solve (asin (cos (3*x))*(f(x) - 1), x);
solve: using arc-trig functions to get a solution.
Some solutions will be lost.
                            %pi
(%o1)                  [x = ---, f(x) = 1]
                             6


(%i2) ev (solve (5^f(x) = 125, f(x)), solveradcan);
                                log(125)
(%o2)                   [f(x) = --------]
                                 log(5)


(%i3) [4*x^2 - y^2 = 12, x*y - x = 2];
                      2    2
(%o3)             [4 x  - y  = 12, x y - x = 2]


(%i4) solve (%, [x, y]);
(%o4) [[x = 2, y = 2], [x = 0.5202594388652008 %i
 - 0.1331240357358706, y = 0.07678378523787788
 - 3.608003221870287 %i], [x = - 0.5202594388652008 %i
 - 0.1331240357358706, y = 3.608003221870287 %i
 + 0.07678378523787788], [x = - 1.733751846381093, 
y = - 0.15356757100196963]]


(%i5) solve (1 + a*x + x^3, x);
                                       3
            - 1   sqrt(3) %i   sqrt(4 a  + 27)   1 1/3
(%o5) [x = (--- - ----------) (--------------- - -)
             2        2               3/2        2
                                   2 3
       sqrt(3) %i   - 1
      (---------- + ---) a
           2         2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
             3/2        2
          2 3
                            3
 sqrt(3) %i   - 1   sqrt(4 a  + 27)   1 1/3
(---------- + ---) (--------------- - -)
     2         2           3/2        2
                        2 3
       - 1   sqrt(3) %i
      (--- - ----------) a
        2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
             3/2        2
          2 3
         3
 sqrt(4 a  + 27)   1 1/3               a
(--------------- - -)    - --------------------------]
        3/2        2                  3
     2 3                      sqrt(4 a  + 27)   1 1/3
                           3 (--------------- - -)
                                     3/2        2
                                  2 3


(%i6) solve (x^3 - 1);
             sqrt(3) %i - 1        sqrt(3) %i + 1
(%o6)   [x = --------------, x = - --------------, x = 1]
                   2                     2


(%i7) solve (x^6 - 1);
           sqrt(3) %i + 1      sqrt(3) %i - 1
(%o7) [x = --------------, x = --------------, x = - 1, 
                 2                   2
                     sqrt(3) %i + 1        sqrt(3) %i - 1
               x = - --------------, x = - --------------, x = 1]
                           2                     2


(%i8) ev (x^6 - 1, %[1]);
                                      6
                      (sqrt(3) %i + 1)
(%o8)                 ----------------- - 1
                             64


(%i9) expand (%);
(%o9)                           0


(%i10) x^2 - 1;
                              2
(%o10)                       x  - 1


(%i11) solve (%, x);
(%o11)                  [x = - 1, x = 1]


(%i12) ev (%th(2), %[1]);
(%o12)                          0
```


The symbols `%r` are used to denote arbitrary constants in a solution.






```maxima
maxima

(%i1) solve([x+y=1,2*x+2*y=2],[x,y]);
solve: dependent equations eliminated: (2)
(%o1)               [[x = 1 - %r1, y = %r1]]
```


See `algsys` and `%rnum_list` for more information.

See also: `breakup`, `multiplicities`, `realroots`, `allroots`, `describe`, `linsolve`, `algsys`, `programmode`, `globalsolve`, `%rnum_list`.

<!-- category: Solving -->
<!-- keywords: solvedecomposes -->
<!-- signatures: solvedecomposes -->
### Variable: solvedecomposes

Default value: `true`


When `solvedecomposes` is `true`, `solve` calls
`polydecomp` if asked to solve polynomials.

See also: `polydecomp`.

<!-- category: Solving -->
<!-- keywords: solveexplicit -->
<!-- signatures: solveexplicit -->
### Variable: solveexplicit

Default value: `false`


When `solveexplicit` is `true`, inhibits `solve` from returning
implicit solutions, that is, solutions of the form `F(x) = 0` where
`F` is some function.

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solvefactors -->
<!-- signatures: solvefactors -->
### Variable: solvefactors

Default value: `true`



When `solvefactors` is `false`, `solve` does not try to factor
the expression.  The `false` setting may be desired in some cases where
factoring is not necessary.

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solvenullwarn -->
<!-- signatures: solvenullwarn -->
### Variable: solvenullwarn

Default value: `true`


When `solvenullwarn` is `true`, `solve` prints a warning message
if called with either a null equation list or a null variable list.  For
example, `solve ([], [])` would print two warning messages and return
`[]`.

See also: `solve`.

<!-- category: Solving -->
<!-- keywords: solveradcan -->
<!-- signatures: solveradcan -->
### Variable: solveradcan

Default value: `false`


When `solveradcan` is `true`, `solve` calls `radcan`
which makes `solve` slower but will allow certain problems containing
exponentials and logarithms to be solved.

See also: `solve`, `radcan`.

<!-- category: Solving -->
<!-- keywords: solvetrigwarn -->
<!-- signatures: solvetrigwarn -->
### Variable: solvetrigwarn

Default value: `true`



When `solvetrigwarn` is `true`, `solve` may print a message
saying that it is using inverse trigonometric functions to solve the equation,
and thereby losing solutions.

See also: `solve`.

