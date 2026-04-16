## Solving

### Function: # ()

Represents the negation of syntactic equality `_003d`.


Note that because of the rules for evaluation of predicate expressions
(in particular because `not expr` causes evaluation of *expr*),
`not a = b` is equivalent to `is(a # b)`,
instead of `a # b`.


Examples:











```maxima
maxima

(%i1) a = b;
(%o1)                         a = b


(%i2) is (a = b);
(%o2)                         false


(%i3) a # b;
(%o3)                         a # b


(%i4) not a = b;
(%o4)                         true


(%i5) is (a # b);
(%o5)                         true


(%i6) is (not a = b);
(%o6)                         true
```

See also: `=`.

### Function: %and ()

The operator `%and` is a simplifying nonshort-circuited logical
conjunction.  Maxima simplifies an `%and` expression to either true,
false, or a logically equivalent, but simplified, expression.  The
operator `%and` is associative, commutative, and idempotent.  Thus
when `%and` returns a noun form, the arguments of `%and` form
a non-redundant sorted list; for example



```maxima
(%i1) a %and (a %and b);
(%o1)                       a %and b
```


If one argument to a conjunction is the *explicit* the negation of another
argument, `%and` returns false:



```maxima
(%i2) a %and (not a);
(%o2)                         false
```


If any member of the conjunction is false, the conjunction simplifies
to false even if other members are manifestly non-boolean; for example



```maxima
(%i3) 42 %and false;
(%o3)                         false
```


Any argument of an `%and` expression that is an inequation (that
is, an inequality or equation), is simplified using the Fourier
elimination package.  The Fourier elimination simplifier has a
pre-processor that converts some, but not all, nonlinear inequations
into linear inequations; for example the Fourier elimination code
simplifies `abs(x) + 1 > 0` to true, so



```maxima
(%i4) (x < 1) %and (abs(x) + 1 > 0);
(%o4)                         x < 1
```


**Notes**  


- * 
The option variable `prederror` does *not* alter the
simplification `%and` expressions.
- * 
To avoid operator precedence errors, compound expressions
involving the operators `%and, %or`, and `not` should be
fully parenthesized.
- * 
The Maxima operators `and` and `or` are both
short-circuited.  Thus `and` isn’t associative or commutative.


**Limitations** The conjunction `%and` simplifies inequations
*locally, not globally*.  This means that conjunctions such as



```maxima
(%i5) (x < 1) %and (x > 1);
(%o5)                 (x > 1) %and (x < 1)
```


do *not* simplify to false.  Also, the Fourier elimination code *ignores*
the fact database;



```maxima
(%i6) assume(x > 5);
(%o6)                        [x > 5]
(%i7) (x > 1) %and (x > 2);
(%o7)                 (x > 1) %and (x > 2)
```


Finally, nonlinear inequations that aren’t easily converted into an
equivalent linear inequation aren’t simplified.


There is no support for distributing `%and` over `%or`;
neither is there support for distributing a logical negation over
`%and`.


**To use** `load("to_poly_solve")`


**Related functions** `%or, %if, and, or, not`


**Status** The operator `%and` is experimental; the
specifications of this function might change and its functionality
might be merged into other Maxima functions.

### Function: %if (bool, a, b)

The operator `%if` is a simplifying conditional.  The
*conditional* *bool* should be boolean-valued.  When the
conditional is true, return the second argument; when the conditional is
false, return the third; in all other cases, return a noun form.


Maxima inequations (either an inequality or an equality) are *not*
boolean-valued; for example, Maxima does *not* simplify $5 < 6$
to true, and it does not simplify $5 = 6$ to false; however, in
the context of a conditional to an `%if` statement, Maxima
*automatically* attempts to determine the truth value of an
inequation.  Examples:



```maxima
(%i1) f : %if(x # 1, 2, 8);
(%o1)                 %if(x - 1 # 0, 2, 8)
(%i2) [subst(x = -1,f), subst(x=1,f)];
(%o2)                        [2, 8]
```


If the conditional involves an inequation, Maxima simplifies it using
the Fourier elimination package.


**Notes** 



- * 
If the conditional is manifestly non-boolean, Maxima returns a noun form:



```maxima
(%i3) %if(42,1,2);
(%o3)                     %if(42, 1, 2)
```



- * 
The Maxima operator `if` is nary, the operator `%if` *isn’t*
nary.


**Limitations** The Fourier elimination code only simplifies nonlinear
inequations that are readily convertible to an equivalent linear
inequation.


**To use:** `load("to_poly_solve")`


**Status:** The operator `%if` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: %or ()

The operator `%or` is a simplifying nonshort-circuited logical
disjunction.  Maxima simplifies an `%or` expression to either
true, false, or a logically equivalent, but simplified,
expression.  The operator `%or` is associative, commutative, and
idempotent.  Thus when `%or` returns a noun form, the arguments
of `%or` form a non-redundant sorted list; for example



```maxima
(%i1) a %or (a %or b);
(%o1)                        a %or b
```


If one member of the disjunction is the *explicit* the negation of another
member, `%or` returns true:



```maxima
(%i2) a %or (not a);
(%o2)                         true
```


If any member of the disjunction is true, the disjunction simplifies
to true even if other members of the disjunction are manifestly non-boolean;
for example



```maxima
(%i3) 42 %or true;
(%o3)                         true
```


Any argument of an `%or` expression that is an inequation (that
is, an inequality or equation), is simplified using the Fourier
elimination package.  The Fourier elimination code simplifies
`abs(x) + 1 > 0` to true, so we have



```maxima
(%i4) (x < 1) %or (abs(x) + 1 > 0);
(%o4)                         true
```


**Notes**  


- * 
The option variable `prederror` does *not* alter the 
simplification of `%or` expressions.
- * 
You should parenthesize compound expressions involving the
operators `%and, %or`, and `not`; the binding powers of these
operators might not match your expectations.
- * 
The Maxima operators `and` and `or` are both short-circuited.
Thus `or` isn’t associative or commutative.


**Limitations** The conjunction `%or` simplifies inequations
*locally, not globally*.  This means that conjunctions such as





```maxima
(%i1) (x < 1) %or (x >= 1);
(%o1) (x > 1) %or (x >= 1)
```


do *not* simplify to true.  Further, the Fourier elimination code ignores
the fact database;



```maxima
(%i2) assume(x > 5);
(%o2)                        [x > 5]
(%i3) (x > 1) %and (x > 2);
(%o3)                 (x > 1) %and (x > 2)
```


Finally, nonlinear inequations that aren’t easily converted into an
equivalent linear inequation aren’t simplified.


The algorithm that looks for terms that cannot both be false is weak;
also there is no support for distributing `%or` over `%and`;
neither is there support for distributing a logical negation over
`%or`.


**To use** `load("to_poly_solve")`


**Related functions** `%or, %if, and, or, not`


**Status** The operator `%or` is experimental; the
specifications of this function might change and its functionality
might be merged into other Maxima functions.

### Variable: %rnum

Default value: `0`


`%rnum` is the counter for the `%r` variables introduced in solutions by
`solve` and `algsys`..  The next `%r` variable is numbered
`%rnum+1`.


See also `%rnum_list`.

See also: `solve`, `algsys`, `%rnum_list`.

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

### Function: %union (%union, soln_1, soln_2, soln_3, ..., %union)

`%union(soln_1, soln_2, soln_3, ...)` represents the union of its arguments,
each of which represents a solution set,
as determined by `to_poly_solve`.
`%union()` represents the empty set.


In many cases, a solution is a list of equations `[x = ..., y = ..., z = ...]`
where *x*, *y*, and *z* are one or more unknowns.
In such cases, `to_poly_solve` returns a `%union` expression
containing one or more such lists.


The solution set sometimes involves simplifying versions of various
of logical operators including `%and`, `%or`, or `%if`
for conjunction, disjunction, and implication, respectively.


Examples:


`%union(...)` represents the union of its arguments,
each of which represents a solution set,
as determined by `to_poly_solve`.
In many cases, a solution is a list of equations.







```maxima
(%i1) load ("to_poly_solve") $
(%i2) to_poly_solve ([sqrt(x^2 - y^2), x + y], [x, y]);
(%o2)    %union([x = 0, y = 0], [x = %c13, y = - %c13])
```


`%union()` represents the empty set.







```maxima
(%i1) load ("to_poly_solve") $
(%i2) to_poly_solve (abs(x) = -1, x);
(%o2)                       %union()
```


The solution set sometimes involves simplifying versions of various
of logical operators.









```maxima
(%i1) load ("to_poly_solve") $
(%i2) sol : to_poly_solve (abs(x) = a, x);
(%o2) %union(%if(isnonnegative_p(a), [x = - a], %union()), 
                      %if(isnonnegative_p(a), [x = a], %union()))
(%i3) subst (a = 42, sol);
(%o3)             %union([x = - 42], [x = 42])
(%i4) subst (a = -42, sol);
(%o4)                       %union()
```

### Function: = ()

The equation operator.


An expression `a = b`, by itself, represents an unevaluated
equation, which might or might not hold.  Unevaluated equations may appear as
arguments to `solve` and `algsys` or some other functions.


The function `is` evaluates `=` to a Boolean value.
`is(a = b)` evaluates `a = b` to `true`
when *a* and *b* are identical.  That is, *a* and *b* are atoms
which are identical, or they are not atoms and their operators are identical and
their arguments are identical.  Otherwise, `is(a = b)`
evaluates to `false`; it never evaluates to `unknown`.  When
`is(a = b)` is `true`, *a* and *b* are said to be
syntactically equal, in contrast to equivalent expressions, for which
`is(equal(a, b))` is `true`.  Expressions can be
equivalent and not syntactically equal.


The negation of `=` is represented by `_0023`.
As with `=`, an expression `a # b`, by itself, is not
evaluated.  `is(a # b)` evaluates `a # b` to
`true` or `false`.


In addition to `is`, some other operators evaluate `=` and `#`
to `true` or `false`, namely `if`, `and`,
`or`, and `not`.


Note that because of the rules for evaluation of predicate expressions
(in particular because `not expr` causes evaluation of *expr*),
`not a = b` is equivalent to `is(a # b)`,
instead of `a # b`.


`rhs` and `lhs` return the right-hand and left-hand sides,
respectively, of an equation or inequation.


See also `equal` and `notequal`.


Examples:


An expression `a = b`, by itself, represents
an unevaluated equation, which might or might not hold.










```maxima
maxima

(%i1) eq_1 : a * x - 5 * y = 17;
(%o1)                    a x - 5 y = 17


(%i2) eq_2 : b * x + 3 * y = 29;
(%o2)                    3 y + b x = 29


(%i3) solve ([eq_1, eq_2], [x, y]);
                        196         29 a - 17 b
(%o3)          [[x = ---------, y = -----------]]
                     5 b + 3 a       5 b + 3 a


(%i4) subst (%, [eq_1, eq_2]);
         196 a     5 (29 a - 17 b)
(%o4) [--------- - --------------- = 17, 
       5 b + 3 a      5 b + 3 a
                                  196 b     3 (29 a - 17 b)
                                --------- + --------------- = 29]
                                5 b + 3 a      5 b + 3 a


(%i5) ratsimp (%);
(%o5)                  [17 = 17, 29 = 29]
```


`is(a = b)` evaluates `a = b` to `true`
when *a* and *b* are syntactically equal (that is, identical).
Expressions can be equivalent and not syntactically equal.









```maxima
maxima

(%i1) a : (x + 1) * (x - 1);
(%o1)                    (x - 1) (x + 1)


(%i2) b : x^2 - 1;
                              2
(%o2)                        x  - 1


(%i3) [is (a = b), is (a # b)];
(%o3)                     [false, true]


(%i4) [is (equal (a, b)), is (notequal (a, b))];
(%o4)                     [true, false]
```


Some operators evaluate `=` and `#` to `true` or `false`.










```maxima
maxima

(%i1) if expand ((x + y)^2) = x^2 + 2 * x * y + y^2 then FOO else
      BAR;
(%o1)                          FOO


(%i2) eq_3 : 2 * x = 3 * x;
(%o2)                       2 x = 3 x


(%i3) eq_4 : exp (2) = %e^2;
                              2     2
(%o3)                       %e  = %e


(%i4) [eq_3 and eq_4, eq_3 or eq_4, not eq_3];
(%o4)                  [false, true, true]
```


Because `not expr` causes evaluation of *expr*,
`not a = b` is equivalent to `is(a # b)`.







```maxima
maxima

(%i1) [2 * x # 3 * x, not (2 * x = 3 * x)];
(%o1)                   [2 x # 3 x, true]


(%i2) is (2 * x # 3 * x);
(%o2)                         true
```

See also: `solve`, `algsys`, `is`, `#`, `if`, `and`, `or`, `not`, `rhs`, `lhs`, `equal`, `notequal`.

### Variable: algepsilon

Default value: 10^8



`algepsilon` is used by `algsys`.

See also: `algsys`.

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

### Function: algsys (algsys, expr_1, ..., expr_m, x_1, ..., x_n, algsys, eqn_1, ..., eqn_m, x_1, ..., x_n)

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

### Function: allroots (allroots, expr, allroots, eqn)

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

### Function: bfallroots (bfallroots, expr, bfallroots, eqn)

Computes numerical approximations of the real and complex roots of the
polynomial *expr* or polynomial equation *eqn* of one variable.


In all respects, `bfallroots` is identical to `allroots` except
that `bfallroots` computes the roots using bigfloats.  See 
`allroots` for more information.

See also: `allroots`.

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

### Function: complex_number_p (x)

The predicate `complex_number_p` returns true if its argument is
either `a + %i * b`, `a`, `%i b`, or `%i`,
where `a` and `b` are either rational or floating point
numbers (including big floating point); for all other inputs,
`complex_number_p` returns false; for example



```maxima
(%i1) map('complex_number_p,[2/3, 2 + 1.5 * %i, %i]);
(%o1)                  [true, true, true]
(%i2) complex_number_p((2+%i)/(5-%i));
(%o2)                         false
(%i3) complex_number_p(cos(5 - 2 * %i));
(%o3)                         false
```


**Related functions** `isreal_p`


**To use** `load("to_poly_solve")`


**Status** The operator `complex_number_p` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: compose_functions (l)

The function call `compose_functions(l)` returns a lambda form that is
the *composition* of the functions in the list *l*.  The functions are
applied from *right* to *left*; for example



```maxima
(%i1) compose_functions([cos, exp]);
                                        %g151
(%o1)             lambda([%g151], cos(%e     ))
(%i2) %(x);
                                  x
(%o2)                       cos(%e )
```


When the function list is empty, return the identity function:



```maxima
(%i3) compose_functions([]);
(%o3)                lambda([%g152], %g152)
(%i4)  %(x);
(%o4)                           x
```


**Notes** 


- * 
When Maxima determines that a list member isn’t a symbol or
a lambda form, `funmake` (*not* `compose_functions`)
signals an error:



```maxima
(%i5) compose_functions([a < b]);

funmake: first argument must be a symbol, subscripted symbol,
string, or lambda expression; found: a < b
#0: compose_functions(l=[a < b])(to_poly_solve.mac line 40)
 -- an error. To debug this try: debugmode(true);
```



- * 
To avoid name conflicts, the independent variable is determined by the
function `new_variable`.

```maxima
(%i6) compose_functions([%g0]);
(%o6)              lambda([%g154], %g0(%g154))
(%i7) compose_functions([%g0]);
(%o7)              lambda([%g155], %g0(%g155))
```

Although the independent variables are different, Maxima is able to to
deduce that these lambda forms are semantically equal:

```maxima
(%i8) is(equal(%o6,%o7));
(%o8)                         true
```


**To use** `load("to_poly_solve")`


**Status**  The function `compose_functions` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: dfloat (x)

The function `dfloat` is a similar to `float`, but the function
`dfloat` applies `rectform` when `float` fails to evaluate
to an IEEE double floating point number; thus



```maxima
(%i1) float(4.5^(1 + %i));
                               %i + 1
(%o1)                       4.5
(%i2) dfloat(4.5^(1 + %i));
(%o2)        4.48998802962884 %i + .3000124893895671
```


**Notes** 



- * 
The rectangular form of an expression might be poorly suited for
numerical evaluation–for example, the rectangular form might
needlessly involve the difference of floating point numbers
(subtractive cancellation).
- * 
The identifier `float` is both an option variable (default
value false) and a function name.


**Related functions** `float, bfloat`


**To use** `load("to_poly_solve")`


**Status** The function `dfloat` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: dimension (dimension, eqn, dimension, eqn_1, ..., eqn_n)

`dimen` is a package for dimensional analysis.
`load ("dimen")` loads this package.
`demo ("dimen")` displays a short demonstration.

### Variable: dispflag

Default value: `true`



If set to `false` within a `block` will inhibit the display of output
generated by the solve functions called from within the `block`.
Termination of the `block` with a dollar sign, `$`, sets `dispflag` to
`false`.

### Function: elim (l, x)

The function `elim` eliminates the variables in the set or list
`x` from the equations in the set or list `l`.  Each member
of `x` must be a symbol; the members of `l` can either be
equations, or expressions that are assumed to equal zero.


The function `elim` returns a list of two lists; the first is
the list of expressions with the variables eliminated; the second
is the list of pivots; thus, the second list is a list of
expressions that `elim` used to eliminate the variables.


Here is an example of eliminating between linear equations:



```maxima
(%i1) elim(set(x + y + z = 1, x - y  - z = 8, x - z = 1), 
           set(x,y));
(%o1)            [[2 z - 7], [y + 7, z - x + 1]]
```


Eliminating `x` and `y` yields the single equation `2 z - 7 = 0`;
the equations `y + 7 = 0` and `z - z + 1 = 1` were used as pivots.
Eliminating all three variables from these equations, triangularizes the linear
system:



```maxima
(%i2) elim(set(x + y + z = 1, x - y  - z = 8, x - z = 1),
           set(x,y,z));
(%o2)           [[], [2 z - 7, y + 7, z - x + 1]]
```


Of course, the equations needn’t be linear:



```maxima
(%i3) elim(set(x^2 - 2 * y^3 = 1,  x - y = 5), [x,y]);
                     3    2
(%o3)       [[], [2 y  - y  - 10 y - 24, y - x + 5]]
```


The user doesn’t control the order the variables are
eliminated.  Instead, the algorithm uses a heuristic to *attempt* to
choose the best pivot and the best elimination order.


**Notes** 



- * 
Unlike the related function `eliminate`, the function
`elim` does *not* invoke `solve` when the number of equations
equals the number of variables.
- * 
The function `elim` works by applying resultants; the option
variable `resultant` determines which algorithm Maxima
uses.  Using `sqfr`, Maxima factors each resultant and suppresses
multiple zeros.
- * 
The `elim` will triangularize a nonlinear set of polynomial
equations; the solution set of the triangularized set *can* be larger
than that solution set of the untriangularized set.  Thus, the triangularized
equations can have *spurious* solutions.


**Related functions** *elim_allbut, eliminate_using, eliminate*


**Option variables** *resultant*


**To use** `load("to_poly")`


**Status** The function `elim` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: elim_allbut (l, x)

This function is similar to `elim`, except that it eliminates all the
variables in the list of equations `l` *except* for those variables that
in in the list `x`



```maxima
(%i1) elim_allbut([x+y = 1, x - 5*y = 1],[]);
(%o1)                 [[], [y, y + x - 1]]
(%i2) elim_allbut([x+y = 1, x - 5*y = 1],[x]);
(%o2)                [[x - 1], [y + x - 1]]
```


**To use** `load("to_poly")`


**Option variables** *resultant*


**Related functions** *elim, eliminate_using, eliminate*


**Status** The function `elim_allbut` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: eliminate_using (l, e, x)

Using `e` as the pivot, eliminate the symbol `x` from the
list or set of equations in `l`.  The function `eliminate_using`
returns a set.



```maxima
(%i1) eq : [x^2 - y^2 - z^3 , x*y - z^2 - 5, x - y + z];
               3    2    2     2
(%o1)      [- z  - y  + x , - z  + x y - 5, z - y + x]
(%i2) eliminate_using(eq,first(eq),z);
        3              2      2      3    2
(%o2) {y  + (1 - 3 x) y  + 3 x  y - x  - x , 
                        4    3  3       2  2             4
                       y  - x  y  + 13 x  y  - 75 x y + x  + 125}
(%i3) eliminate_using(eq,second(eq),z);
        2            2       4    3  3       2  2             4
(%o3) {y  - 3 x y + x  + 5, y  - x  y  + 13 x  y  - 75 x y + x
                                                           + 125}
(%i4) eliminate_using(eq, third(eq),z);
        2            2       3              2      2      3    2
(%o4) {y  - 3 x y + x  + 5, y  + (1 - 3 x) y  + 3 x  y - x  - x }
```


**Option variables** *resultant*


**Related functions** *elim, eliminate, elim_allbut*


**To use** `load("to_poly")`


**Status** The function `eliminate_using` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: find_root (find_root, expr, x, a, b, abserr, relerr, find_root, f, a, b, abserr, relerr, bf_find_root, expr, x, a, b, abserr, relerr, bf_find_root, f, a, b, abserr, relerr)

Finds a root of the expression *expr* or the function *f* over the
closed interval $[a, b]$.  The expression *expr* may be an
equation, in which case `find_root` seeks a root of
`lhs(expr) - rhs(expr)`.


Given that Maxima can evaluate *expr* or *f* over
$[a, b]$ and that *expr* or *f* is continuous,
`find_root` is guaranteed to find the root,
or one of the roots if there is more than one.


`find_root` initially applies binary search.
If the function in question appears to be smooth enough,
`find_root` applies linear interpolation instead.


`bf_find_root` is a bigfloat version of `find_root`.  The
function is computed using bigfloat arithmetic and a bigfloat result
is returned.  Otherwise, `bf_find_root` is identical to
`find_root`, and the following description is equally applicable
to `bf_find_root`.


The accuracy of `find_root` is governed by `abserr` and
`relerr`, which are optional keyword arguments to
`find_root`.  These keyword arguments take the form
`key=val`.  The keyword arguments are



**abserr** — Desired absolute error of function value at root.  Default is
`find_root_abs`.
**relerr** — Desired relative error of root.  Default is `find_root_rel`.


`find_root` stops when the function in question evaluates to
something less than or equal to `abserr`, or if successive
approximants *x_0*, *x_1* differ by no more than `relerr * max(abs(x_0), abs(x_1))`.  The default values of
`find_root_abs` and `find_root_rel` are both zero.


`find_root` expects the function in question to have a different sign at
the endpoints of the search interval.
When the function evaluates to a number at both endpoints
and these numbers have the same sign,
the behavior of `find_root` is governed by `find_root_error`.
When `find_root_error` is `true`,
`find_root` prints an error message.
Otherwise `find_root` returns the value of `find_root_error`.
The default value of `find_root_error` is `true`.


If *f* evaluates to something other than a number at any step in the search
algorithm, `find_root` returns a partially-evaluated `find_root`
expression.


The order of *a* and *b* is ignored; the region in which a root is
sought is $[min(a, b), max(a, b)]$.


Examples:

























```maxima
maxima

(%i1) f(x) := sin(x) - x/2;
                                        x
(%o1)                  f(x) := sin(x) - -
                                        2


(%i2) find_root (sin(x) - x/2, x, 0.1, %pi);
(%o2)                   1.895494267033981


(%i3) find_root (sin(x) = x/2, x, 0.1, %pi);
(%o3)                   1.895494267033981


(%i4) find_root (f(x), x, 0.1, %pi);
(%o4)                   1.895494267033981


(%i5) find_root (f, 0.1, %pi);
(%o5)                   1.895494267033981


(%i6) find_root (exp(x) = y, x, 0, 100);
                            x
(%o6)           find_root(%e  = y, x, 0.0, 100.0)


(%i7) find_root (exp(x) = y, x, 0, 100), y = 10;
(%o7)                   2.302585092994046


(%i8) log (10.0);
(%o8)                   2.302585092994046


(%i9) fpprec:32;
(%o9)                          32


(%i10) 32;
(%o10)                         32


(%i11) bf_find_root (exp(x) = y, x, 0, 100), y = 10;
(%o11)         2.3025850929940456840179914546844b0


(%i12) log(10b0);
(%o12)         2.3025850929940456840179914546844b0
```

See also: `find_root`.

### Function: fourier_elim (eq1, eq2, ..., var1, var, ...)

Fourier elimination is the analog of Gauss elimination for linear inequations
(equations or inequalities).  The function call `fourier_elim([eq1, eq2, ...], [var1, var2, ...])` does Fourier elimination on a list of linear
inequations `[eq1, eq2, ...]` with respect to the variables
`[var1, var2, ...]`; for example



```maxima
(%i1) fourier_elim([y-x < 5, x - y < 7, 10 < y],[x,y]);
(%o1)            [y - 5 < x, x < y + 7, 10 < y]
(%i2) fourier_elim([y-x < 5, x - y < 7, 10 < y],[y,x]);
(%o2)        [max(10, x - 7) < y, y < x + 5, 5 < x]
```


Eliminating first with respect to $x$ and second with respect to
$y$ yields lower and upper bounds for $x$ that depend on
$y$, and lower and upper bounds for $y$ that are numbers.
Eliminating in the other order gives $x$ dependent lower and
upper bounds for $y$, and numerical lower and upper bounds for
$x$.


When necessary, `fourier_elim` returns a *disjunction* of lists of
inequations:



```maxima
(%i3) fourier_elim([x # 6],[x]);
(%o3)                  [x < 6] or [6 < x]
```


When the solution set is empty,  `fourier_elim` returns `emptyset`,
and when the solution set is all reals, `fourier_elim` returns `universalset`;
for example



```maxima
(%i4) fourier_elim([x < 1, x > 1],[x]);
(%o4)                       emptyset
(%i5) fourier_elim([minf < x, x < inf],[x]);
(%o5)                     universalset
```


For nonlinear inequations, `fourier_elim` returns a (somewhat) 
simplified list of inequations:



```maxima
(%i6) fourier_elim([x^3 - 1 > 0],[x]);

               2                             2
(%o6) [1 < x, x  + x + 1 > 0] or [x < 1, - (x  + x + 1) > 0]

(%i7) fourier_elim([cos(x) < 1/2],[x]);
(%o7)                  [1 - 2 cos(x) > 0]
```


Instead of a list of inequations, the first argument to `fourier_elim`
may be a logical disjunction or conjunction:



```maxima
(%i8) fourier_elim((x + y < 5) and (x - y >8),[x,y]);
                                              3
(%o8)            [y + 8 < x, x < 5 - y, y < - -]
                                              2
(%i9) fourier_elim(((x + y < 5) and x < 1) or  (x - y >8),[x,y]);
(%o9)          [y + 8 < x] or [x < min(1, 5 - y)]
```


The function `fourier_elim` supports the inequation operators 
`<, <=, >, >=, #`, and `=`.


The Fourier elimination code has a preprocessor that converts some
nonlinear inequations that involve the absolute value, minimum, and
maximum functions into linear in equations.  Additionally, the preprocessor
handles some expressions that are the product or quotient of linear terms:



```maxima
(%i10) fourier_elim([max(x,y) > 6, x # 8, abs(y-1) > 12],[x,y]);
(%o10) [6 < x, x < 8, y < - 11] or [8 < x, y < - 11]
 or [x < 8, 13 < y] or [x = y, 13 < y] or [8 < x, x < y, 13 < y]
 or [y < x, 13 < y]
(%i11) fourier_elim([(x+6)/(x-9) <= 6],[x]);
(%o11)           [x = 12] or [12 < x] or [x < 9]
(%i12) fourier_elim([x^2 - 1 # 0],[x]);
(%o12)      [- 1 < x, x < 1] or [1 < x] or [x < - 1]
```


**To use** `load("fourier_elim")`

### Function: funcsolve (eqn, g, t)

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

### Function: harmonic_number (x)

When *x* is positive integer $n$, `harmonic_number` is
the $n$’th harmonic number.  More generally,
`harmonic_number(x) = psi[0](x+1) + %gamma`.  (See `polygamma`).










```maxima
(%i1) load("simplify_sum")$

(%i2) harmonic_number(5);
                               137
(%o2)                          ---
                               60


(%i3) sum(1/k, k, 1, 5);
                               137
(%o3)                          ---
                               60


(%i4) float(harmonic_number(sqrt(2)));
(%o4)              %gamma + 0.6601971549171388


(%i5) float(psi[0](1+sqrt(2)))+%gamma;
(%o5)              %gamma + 0.6601971549171388
```

See also: `polygamma`.

### Function: harmonic_to_psi (x)

Converts expressions with `harmonic_number` to the equivalent
expression involving `psi[0]` (see `polygamma`).







```maxima
(%i1) load("simplify_sum")$

(%i2) harmonic_to_psi(harmonic_number(sqrt(2)));
(%o2)              psi (sqrt(2) + 1) + %gamma
                      0
```

See also: `polygamma`.

### Function: horner (horner, expr, x, horner, expr)

Returns a rearranged representation of *expr* as in Horner’s rule, using
*x* as the main variable if it is specified.  `x` may be omitted in
which case the main variable of the canonical rational expression form of
*expr* is used.


`horner` sometimes improves stability if `expr` is
to be numerically evaluated.  It is also useful if Maxima is used to
generate programs to be run in Fortran.  See also `stringout`.









```maxima
maxima

(%i1) expr: 1e-155*x^2 - 5.5*x + 5.2e155;
                            2
(%o1)             1.0e-155 x  - 5.5 x + 5.2e155


(%i2) expr2: horner (%, x), keepfloat: true;
(%o2)         1.0 ((1.0e-155 x - 5.5) x + 5.2e155)


(%i3) ev (expr, x=1e155);
Maxima encountered a Lisp error:

 Arithmetic error FLOATING-POINT-OVERFLOW signalled.
Operation was *, operands (1.0e155 NIL).

Automatically continuing.
To enable the Lisp debugger set *debugger-hook* to nil.


(%i4) ev (expr2, x=1e155);
(%o4)                 7.000000000000006e154
```

See also: `stringout`.

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

### Function: isreal_p (e)

The predicate `isreal_p` returns true when Maxima is able to
determine that `e` is real-valued on the *entire* real line; it
returns false when Maxima is able to determine that `e` *isn’t*
real-valued on some nonempty subset of the real line; and it returns a
noun form for all other cases.



```maxima
(%i1) map('isreal_p, [-1, 0, %i, %pi]);
(%o1)               [true, true, false, true]
```


Maxima variables are assumed to be real; thus



```maxima
(%i2) isreal_p(x);
(%o2)                         true
```


The function `isreal_p` examines the fact database:



```maxima
(%i3) declare(z,complex)$

(%i4) isreal_p(z);
(%o4)                      isreal_p(z)
```


**Limitations**
Too often, `isreal_p` returns a noun form when it should be able
to return false; a simple example: the logarithm function isn’t
real-valued on the entire real line, so `isreal_p(log(x))` should
return false; however



```maxima
(%i5) isreal_p(log(x));
(%o5)                   isreal_p(log(x))
```


**To use** `load("to_poly_solve")`


**Related functions** *complex_number_p*


**Status** The function `isreal_p` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

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

### Function: linsolve (expr_1, ..., expr_m, x_1, ..., x_n)

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

### Variable: linsolve_params

Default value: `true`


When `linsolve_params` is `true`, `linsolve` also generates
the `%r` symbols used to represent arbitrary parameters described in
the manual under `algsys`.  Otherwise, `linsolve` solves an
under-determined system of equations with some variables expressed in terms of
others.

See also: `linsolve`, `algsys`.

### Variable: linsolvewarn

Default value: `true`


When `linsolvewarn` is `true`, `linsolve` prints a message
"Dependent equations eliminated".

See also: `linsolve`.

### Variable: multiplicities

Default value: `not_set_yet`


`multiplicities` is set to a list of the multiplicities of the individual
solutions returned by `solve` or `realroots`.

See also: `solve`, `realroots`.

### Function: new_variable (type)

Return a unique symbol of the form `%[z,n,r,c,g]k`, where
`k` is an integer.  The allowed values for $type$ are
*integer, natural_number, real, complex,* and *general*.
(By natural number, we mean the *nonnegative integers*; thus zero is
a natural number.  Some, but not all, definitions of natural number
*exclude* zero.)


When $type$ isn’t one of the allowed values, $type$ defaults
to $general$.  For integers, natural numbers, and complex numbers,
Maxima automatically appends this information to the fact database.



```maxima
(%i1) map('new_variable,
          ['integer, 'natural_number, 'real, 'complex, 'general]);
(%o1)          [%z144, %n145, %r146, %c147, %g148]
(%i2) nicedummies(%);
(%o2)               [%z0, %n0, %r0, %c0, %g0]
(%i3) featurep(%z0, 'integer);
(%o3)                         true
(%i4) featurep(%n0, 'integer);
(%o4)                         true
(%i5) is(%n0 >= 0);
(%o5)                         true
(%i6) featurep(%c0, 'complex);
(%o6)                         true
```


**Note** Generally, the argument to `new_variable` should be quoted.  The quote
will protect against errors similar to



```maxima
(%i7) integer : 12$

(%i8) new_variable(integer);
(%o8)                         %g149
(%i9) new_variable('integer);
(%o9)                         %z150
```


**Related functions** *nicedummies*


**To use** `load("to_poly_solve")`


**Status** The function `new_variable` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: newton (expr, x, x_0, eps)

Returns an approximate solution of `expr = 0` by Newton’s method,
considering *expr* to be a function of one variable, *x*.
The search begins with `x = x_0`
and proceeds until `abs(expr) < eps`
(with *expr* evaluated at the current value of *x*).


`newton` allows undefined variables to appear in *expr*,
so long as the termination test `abs(expr) < eps` evaluates
to `true` or `false`.
Thus it is not necessary that *expr* evaluate to a number.


`load("newton1")` loads this function.


See also `realroots`, `allroots`, `find_root` and
`mnewton`.


Examples:











```maxima
maxima

(%i1) load ("newton1");
(%o1) /maxima/share/numeric/newton1.mac


(%i2) newton (cos (u), u, 1, 1/100);
(%o2)                  1.5706752771612507


(%i3) ev (cos (u), u = %);
(%o3)                 1.2104963335033528e-4


(%i4) assume (a > 0);
(%o4)                        [a > 0]


(%i5) newton (x^2 - a^2, x, a/2, a^2/100);
(%o5)                 1.0003048780487804 a


(%i6) ev (x^2 - a^2, x = %);
                                           2
(%o6)                6.098490481853958e-4 a
```

See also: `realroots`, `allroots`, `find_root`, `mnewton`.

### Function: nicedummies ()

Starting with zero, the function `nicedummies` re-indexes the variables 
in an expression that were introduced by `new_variable`;



```maxima
(%i1) new_variable('integer) + 52 * new_variable('integer);
(%o1)                   52 %z136 + %z135
(%i2) new_variable('integer) - new_variable('integer);
(%o2)                     %z137 - %z138
(%i3) nicedummies(%);
(%o3)                       %z0 - %z1
```


**Related functions** *new_variable*


**To use** `load("to_poly_solve")`


**Status** The function `nicedummies` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

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

### Function: nthroot (p, n)

where *p* is a polynomial with integer coefficients and *n* is a
positive integer returns `q`, a polynomial over the integers, such that
`q^n = p` or prints an error message indicating that *p* is not a
perfect nth power.  This routine is much faster than `factor` or even
`sqfr`.

See also: `factor`, `sqfr`.

### Function: parg (x)

The function `parg` is a simplifying version of the complex argument function 
`carg`; thus



```maxima
(%i1) map('parg,[1,1+%i,%i, -1 + %i, -1]);
                        %pi  %pi  3 %pi
(%o1)               [0, ---, ---, -----, %pi]
                         4    2     4
```


Generally, for a non-constant input, `parg` returns a noun form; thus



```maxima
(%i2) parg(x + %i * sqrt(x));
(%o2)                 parg(x + %i sqrt(x))
```


When `sign` can determine that the input is a positive or negative real
number, `parg` will return a non-noun form for a non-constant input.
Here are two examples:





```maxima
(%i3) parg(abs(x));
(%o3) 0
(%i4) parg(-x^2-1);
(%o4)                          %pi
```


**Note** The `sign` function mostly ignores the variables that are declared
to be complex (`declare(x,complex)`); for variables that are declared
to be complex, the `parg` can return incorrect values; for example





```maxima
(%i1) declare(x,complex)$

(%i2) parg(x^2 + 1);
(%o2) 0
```


**Related function** *carg, isreal_p*


**To use** `load("to_poly_solve")`


**Status** The function `parg` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Variable: polyfactor

Default value: `false`


The option variable `polyfactor` when `true` causes
`allroots` and `bfallroots` to factor the polynomial over the real
numbers if the polynomial is real, or over the complex numbers, if the
polynomial is complex.


See `allroots` for an example.

See also: `allroots`, `bfallroots`.

### Variable: product_use_gamma

Default value: `true`


When simplifying products, `solve_rec` introduces gamma function
into the expression if `product_use_gamma` is `true`.


See also: `simplify_products`, `solve_005frec`.

See also: `simplify_products`, `solve_rec`.

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

### Function: real_imagpart_to_conjugate (e)

The function `real_imagpart_to_conjugate` replaces all occurrences
of `realpart` and `imagpart` to algebraically equivalent expressions
involving the `conjugate`.



```maxima
(%i1) declare(x, complex)$

(%i2) real_imagpart_to_conjugate(realpart(x) +  imagpart(x) = 3);
          conjugate(x) + x   %i (x - conjugate(x))
(%o2)     ---------------- - --------------------- = 3
                 2                     2
```


**To use** `load("to_poly_solve")`


**Status** The function `real_imagpart_to_conjugate` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Variable: realonly

Default value: `false`


When `realonly` is `true`, `algsys` returns only those solutions
which are free of `%i`.

See also: `algsys`.

### Function: realroots (realroots, expr, bound, realroots, eqn, bound, realroots, expr, realroots, eqn)

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

### Function: rectform_log_if_constant (e)

The function `rectform_log_if_constant` converts all terms of the form
`log(c)` to  `rectform(log(c))`, where `c` is
either a declared constant expression or explicitly declared constant



```maxima
(%i1) rectform_log_if_constant(log(1-%i) - log(x - %i));
                                 log(2)   %i %pi
(%o1)            - log(x - %i) + ------ - ------
                                   2        4
(%i2) declare(a,constant, b,constant)$

(%i3) rectform_log_if_constant(log(a + %i*b));
                       2    2
                  log(b  + a )
(%o3)             ------------ + %i atan2(b, a)
                       2
```


**To use** `load("to_poly_solve")`


**Status** The function `rectform_log_if_constant` is
experimental; the specifications of this function might change might change and its functionality
might be merged into other Maxima functions.

### Function: reduce_order (rec, sol, var)

Reduces the order of linear recurrence *rec* when a particular solution
*sol* is known. The reduced recurrence can be used to get other solutions.


Example:



```maxima
(%i3) rec: x[n+2] = x[n+1] + x[n]/n;
                                      x
                                       n
(%o3)               x      = x      + --
                     n + 2    n + 1   n


(%i4) solve_rec(rec, x[n]);
WARNING: found some hypergeometrical solutions! 
(%o4)                    x  = %k  n
                          n     1


(%i5) reduce_order(rec, n, x[n]);
(%t5)                    x  = n %z
                          n       n

                           n - 1
                           ====
                           \
(%t6)                %z  =  >     %u
                       n   /        %j
                           ====
                           %j = 0

(%o6)             (- n - 2) %u     - %u
                              n + 1     n


(%i6) solve_rec((n+2)*%u[n+1] + %u[n], %u[n]);
                                     n
                            %k  (- 1)
                              1
(%o6)                 %u  = ----------
                        n    (n + 1)!

So the general solution is

             n - 1
             ====        j
             \      (- 1)
       %k  n  >    -------- + %k  n
         2   /     (j + 1)!     1
             ====
             j = 0
```

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

### Variable: rootsconmode

Default value: `true`


`rootsconmode` governs the behavior of the `rootscontract` command.
See `rootscontract` for details.

See also: `rootscontract`.

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

### Variable: rootsepsilon

Default value: 1.0e-7


`rootsepsilon` is the tolerance which establishes the confidence interval
for the roots found by the `realroots` function.

See also: `realroots`.

### Function: simp_inequality (e)

The function `simp_inequality` applies basic simplifications to inequations,
returning either a boolean value (true or false) or the original inequation.


The simplification rules used by `simp_inequality`
include some facts about the ranges of the absolute value, power,
and exponential functions along with some elementary algebra facts.


For conjunctions or disjunctions of inequations,
`simp_inequality` is applied to each individual inequation,
but no effort is made to simplify the entire logical expression.


Effectively, simp_inequality creates a new empty context,
so database facts are not used to simplify inequations.


`load("to_poly_solve")` loads this function.


Examples:



```maxima
(%i2) simp_inequality(1 # 0);
(%o2) true
```



```maxima
(%i3) simp_inequality(1 < 0);
(%o3) false
```



```maxima
(%i4) simp_inequality(a=a);
(%o4) true
```



```maxima
(%i5) simp_inequality(a # a);
(%o5) false
```



```maxima
(%i6) simp_inequality(a + 1 # a);
(%o6) true
```



```maxima
(%i7) simp_inequality(a < a+1);
(%o7) true
```



```maxima
(%i8) simp_inequality(abs(x) >= 0);
(%o8) true
```



```maxima
(%i9) simp_inequality(exp(x)  > 0);
(%o9) true
```



```maxima
(%i10) simp_inequality(x^2 >= 0);
(%o10) true
```



```maxima
(%i11) simp_inequality(2^x  # 0);
(%o11) true
```



```maxima
(%i12) simp_inequality(2^(x+1) > 2^x);
(%o12) true
```


The fact database is not consulted.
For example:



```maxima
(%i13) assume(xx > 0)$
(%i14) simp_inequality(xx > 0);
(%o14) xx>0
```


And finally, for conjunctions or disjunctions of inequations,
each inequation is simplified,
but no effort is made to simplify the entire logical expression;
for example:



```maxima
(%i15) simp_inequality((1 > 0) and (x < 0) and (x > 0));
(%o15) x<0 and x>0
```

### Variable: simplify_products

Default value: `true`


If `simplify_products` is `true`, `solve_rec` will try to
simplify products in result.


See also: `solve_005frec`.

See also: `solve_rec`.

### Function: simplify_sum (expr)

Tries to simplify all sums appearing in *expr* to a closed form.


To use this function first load the `simplify_sum` package with
`load("simplify_sum")`.


Example:








```maxima
(%i1) load("simplify_sum")$

(%i2) sum(binomial(n+k,k)/2^k, k, 1, n) + sum(binomial(2*n, 2*k), k, 1,n);
        n                          n
       ====                       ====
       \     binomial(n + k, k)   \
(%o2)   >    ------------------ +  >    binomial(2 n, 2 k)
       /              k           /
       ====          2            ====
       k = 1                      k = 1


(%i3) simplify_sum(%);
                         2 n - 1    n
(%o3)                   2        + 2  - 2
```

### Function: solve (solve, expr, x, solve, expr, solve, eqn_1, ..., eqn_n, x_1, ..., x_n)

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

### Function: solve_rec (eqn, var, init)

Solves for hypergeometrical solutions to linear recurrence *eqn* with
polynomials coefficient in variable *var*. Optional arguments *init*
are initial conditions.


`solve_rec` can solve linear recurrences with constant coefficients,
finds hypergeometrical solutions to homogeneous linear recurrences with
polynomial coefficients, rational solutions to linear recurrences with
polynomial coefficients and can solve Ricatti type recurrences.


Note that the running time of the algorithm used to find hypergeometrical
solutions is exponential in the degree of the leading and trailing
coefficient.


To use this function first load the `solve_rec` package with
`load("solve_rec");`.


Example of linear recurrence with constant coefficients:



```maxima
(%i2) solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n]);
                        n          n
           (sqrt(5) - 1)  %k  (- 1)
                            1           n
(%o2) a  = ------------------------- - ----
       n               n                  n
                      2                5 2
                                                n
                                   (sqrt(5) + 1)  %k
                                                    2    2
                                 + ------------------ - ----
                                            n              n
                                           2            5 2
```


Example of linear recurrence with polynomial coefficients:



```maxima
(%i7) 2*x*(x+1)*y[x] - (x^2+3*x-2)*y[x+1] + (x-1)*y[x+2];
                         2
(%o7) (x - 1) y      - (x  + 3 x - 2) y      + 2 x (x + 1) y
               x + 2                   x + 1                x


(%i8) solve_rec(%, y[x], y[1]=1, y[3]=3);
                              x
                           3 2    x!
(%o9)                 y  = ---- - --
                       x    4     2
```


Example of Ricatti type recurrence:



```maxima
(%i2) x*y[x+1]*y[x] - y[x+1]/(x+2) + y[x]/(x-1) = 0;
                            y         y
                             x + 1     x
(%o2)         x y  y      - ------ + ----- = 0
                 x  x + 1   x + 2    x - 1

(%i3) solve_rec(%, y[x], y[3]=5)$

(%i4) ratsimp(minfactorial(factcomb(%)));
                                   3
                               30 x  - 30 x
(%o4) y  = - -------------------------------------------------
       x        6      5       4       3       2
             5 x  - 3 x  - 25 x  + 15 x  + 20 x  - 12 x - 1584
```



See also: `solve_rec_rat`, `simplify_products` and `product_005fuse_005fgamma`.

See also: `solve_rec_rat`, `simplify_products`, `product_use_gamma`.

### Function: solve_rec_rat (eqn, var, init)

Solves for rational solutions to linear recurrences. See solve_rec for
description of arguments.


To use this function first load the `solve_rec` package with
`load("solve_rec");`.


Example:



```maxima
(%i1) (x+4)*a[x+3] + (x+3)*a[x+2] - x*a[x+1] + (x^2-1)*a[x];
(%o1)  (x + 4) a      + (x + 3) a      - x a
                x + 3            x + 2      x + 1
                                                   2
                                               + (x  - 1) a
                                                            x


(%i2) solve_rec_rat(% = (x+2)/(x+1), a[x]);
                       1
(%o2)      a  = ---------------
            x   (x - 1) (x + 1)
```



See also: `solve_005frec`.

See also: `solve_rec`.

### Variable: solvedecomposes

Default value: `true`


When `solvedecomposes` is `true`, `solve` calls
`polydecomp` if asked to solve polynomials.

See also: `polydecomp`.

### Variable: solveexplicit

Default value: `false`


When `solveexplicit` is `true`, inhibits `solve` from returning
implicit solutions, that is, solutions of the form `F(x) = 0` where
`F` is some function.

See also: `solve`.

### Variable: solvefactors

Default value: `true`



When `solvefactors` is `false`, `solve` does not try to factor
the expression.  The `false` setting may be desired in some cases where
factoring is not necessary.

See also: `solve`.

### Variable: solvenullwarn

Default value: `true`


When `solvenullwarn` is `true`, `solve` prints a warning message
if called with either a null equation list or a null variable list.  For
example, `solve ([], [])` would print two warning messages and return
`[]`.

See also: `solve`.

### Variable: solveradcan

Default value: `false`


When `solveradcan` is `true`, `solve` calls `radcan`
which makes `solve` slower but will allow certain problems containing
exponentials and logarithms to be solved.

See also: `solve`, `radcan`.

### Variable: solvetrigwarn

Default value: `true`



When `solvetrigwarn` is `true`, `solve` may print a message
saying that it is using inverse trigonometric functions to solve the equation,
and thereby losing solutions.

See also: `solve`.

### Function: standardize_inverse_trig (e)

This function applies the identities `cot(x) = atan(1/x), acsc(x) = asin(1/x),` and similarly for `asec, acoth, acsch`
and `asech` to an expression.  See Abramowitz and Stegun, 
Eqs. 4.4.6 through 4.4.8 and 4.6.4 through 4.6.6.


**To use** `load("to_poly_solve")`


**Status** The function `standardize_inverse_trig` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: subst_parallel (l, e)

When `l` is a single equation or a list of equations, substitute
the right hand side of each equation for the left hand side.  The
substitutions are made in parallel; for example



```maxima
(%i1) load("to_poly_solve")$

(%i2) subst_parallel([x=y,y=x], [x,y]);
(%o2)                        [y, x]
```


Compare this to substitutions made serially:



```maxima
(%i3) subst([x=y,y=x],[x,y]);
(%o3)                        [x, x]
```


The function `subst_parallel` is similar to `sublis` except that
`subst_parallel` allows for substitution of nonatoms; for example



```maxima
(%i4) subst_parallel([x^2 = a, y = b], x^2 * y);
(%o4)                          a b
(%i5) sublis([x^2 = a, y = b], x^2 * y);

                                                             2
sublis: left-hand side of equation must be a symbol; found: x
 -- an error. To debug this try: debugmode(true);
```


The substitutions made by `subst_parallel` are literal, not semantic; thus 
`subst_parallel` *does not* recognize that $x * y$ is a subexpression 
of $x^2 * y$



```maxima
(%i6) subst_parallel([x * y = a], x^2 * y);
                               2
(%o6)                         x  y
```


The function `subst_parallel` completes all substitutions
*before* simplifications.  This allows for substitutions into
conditional expressions where errors might occur if the
simplifications were made earlier:



```maxima
(%i7) subst_parallel([x = 0], %if(x < 1, 5, log(x)));
(%o7)                           5
(%i8) subst([x = 0], %if(x < 1, 5, log(x)));

log: encountered log(0).
 -- an error. To debug this try: debugmode(true);
```


**Related functions** *subst, sublis, ratsubst*


**To use** `load("to_poly_solve_extra.lisp")`


**Status** The function `subst_parallel` is experimental; the
specifications of this function might change might change and its
functionality might be merged into other Maxima functions.

### Function: summand_to_rec (summand_to_rec, summand, k, n, summand_to_rec, summand, k, lo, hi, n)

Returns the recurrence satisfied by the sum



```maxima
hi
    ====
    \
     >     summand
    /
    ====
  k = lo
```


where summand is hypergeometrical in *k* and *n*. If *lo* and *hi*
are omitted, they are assumed to be `lo = -inf` and `hi = inf`.


To use this function first load the `simplify_sum` package with
`load("simplify_sum")`.


Example:



```maxima
(%i1) load("simplify_sum")$

(%i2) summand: binom(n,k);
(%o2)                           binomial(n, k)


(%i3) summand_to_rec(summand,k,n);
(%o3)                      2 sm  - sm      = 0
                               n     n + 1


(%i7) summand: binom(n, k)/(k+1);
                                binomial(n, k)
(%o7)                           --------------
                                    k + 1


(%i8) summand_to_rec(summand, [k, 0, n], n);
(%o8)               2 (n + 1) sm  - (n + 2) sm      = - 1
                                n             n + 1
```

### Function: to_poly (e, l)

The function `to_poly` attempts to convert the equation `e`
into a polynomial system along with inequality constraints; the
solutions to the polynomial system that satisfy the constraints are
solutions to the equation `e`.  Informally, `to_poly`
attempts to polynomialize the equation *e*; an example might
clarify:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly(sqrt(x) = 3, [x]);
                            2
(%o2) [[%g130 - 3, x = %g130 ], 
                      %pi                               %pi
                   [- --- < parg(%g130), parg(%g130) <= ---], []]
                       2                                 2
```


The conditions `-%pi/2<parg(%g130),parg(%g130)<=%pi/2` tell us that
`%g130` is in the range of the square root function.  When this is
true, the solution set to `sqrt(x) = 3` is the same as the
solution set to `%g130-3,x=%g130^2`.


To polynomialize trigonometric expressions, it is necessary to
introduce a non algebraic substitution; these non algebraic substitutions
are returned in the third list returned by `to_poly`; for example



```maxima
(%i3) to_poly(cos(x),[x]);
                2                                 %i x
(%o3)    [[%g131  + 1], [2 %g131 # 0], [%g131 = %e    ]]
```


Constant terms aren’t polynomializied unless the number one is a member of
the variable list; for example



```maxima
(%i4) to_poly(x = sqrt(5),[x]);
(%o4)                [[x - sqrt(5)], [], []]
(%i5) to_poly(x = sqrt(5),[1,x]);
                            2
(%o5) [[x - %g132, 5 = %g132 ], 
                      %pi                               %pi
                   [- --- < parg(%g132), parg(%g132) <= ---], []]
                       2                                 2
```


To generate a polynomial with $sqrt(5) + sqrt(7)$ as
one of its roots, use the commands



```maxima
(%i6) first(elim_allbut(first(to_poly(x = sqrt(5) + sqrt(7),
                                      [1,x])), [x]));
                          4       2
(%o6)                   [x  - 24 x  + 4]
```


**Related functions** *to_poly_solve*


**To use** `load("to_poly")`


**Status:** The function `to_poly` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

### Function: to_poly_solve (e, l, options)

The function `to_poly_solve` tries to solve the equations $e$
for the variables $l$.  The equation(s) $e$ can either be a
single expression or a set or list of expressions; similarly, $l$
can either be a single symbol or a list of set of symbols.  When
a member of $e$ isn’t explicitly an equation, for example $x^2 -1$,
the solver assumes that the expression vanishes.


The basic strategy of `to_poly_solve` is to convert the input into a polynomial form and to 
call `algsys` on the polynomial system. Internally  `to_poly_solve` defaults `algexact` 
to true. To change the default for `algexact`, append ’algexact=false to the `to_poly_solve` 
argument list.


When `to_poly_solve` is able to determine the solution set, each
member of the solution set is a list in a `%union` object:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly_solve(x*(x-1) = 0, x);
(%o2)               %union([x = 0], [x = 1])
```


When  `to_poly_solve` is *unable* to determine the solution set, a
`%solve` nounform is returned (in this case, a warning is printed)



```maxima
(%i3) to_poly_solve(x^k + 2* x + 1 = 0, x);

Nonalgebraic argument given to 'to_poly'
unable to solve
                          k
(%o3)            %solve([x  + 2 x + 1 = 0], [x])
```


Substitution into a `%solve` nounform can sometimes result in the solution



```maxima
(%i4) subst(k = 2, %);
(%o4)                   %union([x = - 1])
```


Especially for trigonometric equations, the solver sometimes needs
to introduce an arbitrary integer.  These arbitrary integers have the 
form `%zXXX`, where `XXX` is an integer; for example



```maxima
(%i5) to_poly_solve(sin(x) = 0, x);
(%o5)   %union([x = 2 %pi %z33 + %pi], [x = 2 %pi %z35])
```


To re-index these variables to zero, use `nicedummies`:



```maxima
(%i6) nicedummies(%);
(%o6)    %union([x = 2 %pi %z0 + %pi], [x = 2 %pi %z1])
```


Occasionally, the solver introduces an arbitrary complex number of the
form `%cXXX` or an  arbitrary real number of the form `%rXXX`.
The function `nicedummies` will re-index these identifiers to zero.


The solution set sometimes involves simplifying versions of various
of logical operators including `%and`, `%or`, or `%if`
for conjunction, disjunction, and implication, respectively; for example



```maxima
(%i7) sol : to_poly_solve(abs(x) = a, x);
(%o7) %union(%if(isnonnegative_p(a), [x = - a], %union()), 
                      %if(isnonnegative_p(a), [x = a], %union()))
(%i8) subst(a = 42, sol);
(%o8)             %union([x = - 42], [x = 42])
(%i9) subst(a = -42, sol);
(%o9)                       %union()
```


The empty set is represented by `%union()`.


The function `to_poly_solve` is able to solve some, but not all,
equations involving rational powers, some nonrational powers, absolute
values, trigonometric functions, and minimum and maximum.  Also, some it
can solve some equations that are solvable in in terms of the Lambert W
function; some examples:



```maxima
(%i1) load("to_poly_solve")$

(%i2) to_poly_solve(set(max(x,y) = 5, x+y = 2), set(x,y));
(%o2)      %union([x = - 3, y = 5], [x = 5, y = - 3])
(%i3) to_poly_solve(abs(1-abs(1-x)) = 10,x);
(%o3)             %union([x = - 10], [x = 12])
(%i4) to_poly_solve(set(sqrt(x) + sqrt(y) = 5, x + y = 10),
                    set(x,y));
                     3/2               3/2
                    5    %i - 10      5    %i + 10
(%o4) %union([x = - ------------, y = ------------], 
                         2                 2
                                3/2                 3/2
                               5    %i + 10        5    %i - 10
                          [x = ------------, y = - ------------])
                                    2                   2
(%i5) to_poly_solve(cos(x) * sin(x) = 1/2,x,
                    'simpfuncs = ['expand, 'nicedummies]);
                                         %pi
(%o5)              %union([x = %pi %z0 + ---])
                                          4
(%i6) to_poly_solve(x^(2*a) + x^a + 1,x);
                                        2 %i %pi %z81
                                        -------------
                                  1/a         a
                  (sqrt(3) %i - 1)    %e
(%o6) %union([x = -----------------------------------], 
                                  1/a
                                 2

                                                  2 %i %pi %z83
                                                  -------------
                                            1/a         a
                          (- sqrt(3) %i - 1)    %e
                     [x = -------------------------------------])
                                           1/a
                                          2

(%i7) to_poly_solve(x * exp(x) = a, x);
(%o7)              %union([x = lambert_w(a)])
```


For *linear* inequalities, `to_poly_solve` automatically does Fourier
elimination:



```maxima
(%i8) to_poly_solve([x + y < 1, x - y >= 8], [x,y]);
                               7
(%o8) %union([x = y + 8, y < - -], 
                               2
                                                              7
                                 [y + 8 < x, x < 1 - y, y < - -])
                                                              2
```


Each optional argument to `to_poly_solve` must be an equation;
generally, the order of these options does not matter.



- * 
`simpfuncs = l`, where `l` is a list of functions.
Apply the composition of the members of l to each solution.

```maxima
(%i1) to_poly_solve(x^2=%i,x);
                               1/4             1/4
(%o1)       %union([x = - (- 1)   ], [x = (- 1)   ])
(%i2) to_poly_solve(x^2= %i,x, 'simpfuncs = ['rectform]);
                      %i         1             %i         1
(%o2) %union([x = - ------- - -------], [x = ------- + -------])
                    sqrt(2)   sqrt(2)        sqrt(2)   sqrt(2)
```

Sometimes additional simplification can revert a simplification; for example

```maxima
(%i3) to_poly_solve(x^2=1,x);
(%o3)              %union([x = - 1], [x = 1])
(%i4) to_poly_solve(x^2= 1,x, 'simpfuncs = [polarform]);
                                        %i %pi
(%o4)            %union([x = 1], [x = %e      ]
```

Maxima doesn’t try to check that each member of the function list `l` is
purely a simplification; thus

```maxima
(%i5) to_poly_solve(x^2 = %i,x, 'simpfuncs = [lambda([s],s^2)]);
(%o5)                   %union([x = %i])
```

To convert each solution to a double float, use `simpfunc = ['dfloat]`:

```maxima
(%i6) to_poly_solve(x^3 +x + 1 = 0,x, 
                    'simpfuncs = ['dfloat]), algexact : true;
(%o6) %union([x = - .6823278038280178], 
[x = .3411639019140089 - 1.161541399997251 %i], 
[x = 1.161541399997251 %i + .3411639019140089])
```
- * 
`use_grobner = true` With this option, the function
`poly_reduced_grobner` is applied to the equations before
attempting their solution.  Primarily, this option provides a workaround
for weakness in the function `algsys`.  Here is an example of
such a workaround:

```maxima
(%i7) to_poly_solve([x^2+y^2=2^2,(x-1)^2+(y-1)^2=2^2],[x,y],
                    'use_grobner = true);
                    sqrt(7) - 1      sqrt(7) + 1
(%o7) %union([x = - -----------, y = -----------], 
                         2                2
                                 sqrt(7) + 1        sqrt(7) - 1
                            [x = -----------, y = - -----------])
                                      2                  2
(%i8) to_poly_solve([x^2+y^2=2^2,(x-1)^2+(y-1)^2=2^2],[x,y]);
(%o8)                       %union()
```
- * 
`maxdepth = k`, where `k` is a positive integer.  This
function controls the maximum recursion depth for the solver.  The
default value for `maxdepth` is five.  When the recursions depth is
exceeded, the solver signals an error:

```maxima
(%i9) to_poly_solve(cos(x) = x,x, 'maxdepth = 2);
Unable to solve
Unable to solve
(%o9)        %solve([cos(x) = x], [x], maxdepth = 2)
```
- * 
`parameters = l`, where `l` is a list of symbols.  The solver
attempts to return a solution that is valid for all members of the list
`l`; for example:

```maxima
(%i10) to_poly_solve(a * x = x, x);
(%o10)                   %union([x = 0])
(%i11) to_poly_solve(a * x = x, x, 'parameters = [a]);
(%o11) %union(%if(a - 1 = 0, [x = %c111], %union()), 
                               %if(a - 1 # 0, [x = 0], %union()))
```

In `(%o2)`, the solver introduced a dummy variable; to re-index the
these dummy variables, use the function `nicedummies`:

```maxima
(%i12) nicedummies(%);
(%o12) %union(%if(a - 1 = 0, [x = %c0], %union()), 
                               %if(a - 1 # 0, [x = 0], %union()))
```


The `to_poly_solve` uses data stored in the hashed array
`one_to_one_reduce` to solve equations of the form $f(a) = f(b)$.  The assignment `one_to_one_reduce['f,'f] : lambda([a,b], a=b)` tells `to_poly_solve` that the solution set of $f(a) = f(b)$ equals the solution set of $a=b$; for example



```maxima
(%i13) one_to_one_reduce['f,'f] : lambda([a,b], a=b)$

(%i14) to_poly_solve(f(x^2-1) = f(0),x);
(%o14)             %union([x = - 1], [x = 1])
```


More generally, the assignment `one_to_one_reduce['f,'g] : lambda([a,b], w(a, b) = 0` tells `to_poly_solve` that the solution set of $f(a) = f(b)$ equals the solution set of $w(a,b) = 0$; for example



```maxima
(%i15) one_to_one_reduce['f,'g] : lambda([a,b], a = 1 + b/2)$

(%i16) to_poly_solve(f(x) - g(x),x);
(%o16)                   %union([x = 2])
```


Additionally, the function `to_poly_solve` uses data stored in the hashed array 
`function_inverse` to solve equations of the form $f(a) = b$.
The assignment `function_inverse['f] : lambda([s], g(s))` 
informs  `to_poly_solve` that the solution set to `f(x) = b` equals
the solution set to `x = g(b)`; two examples:



```maxima
(%i17) function_inverse['Q] : lambda([s], P(s))$

(%i18) to_poly_solve(Q(x-1) = 2009,x);
(%o18)              %union([x = P(2009) + 1])
(%i19) function_inverse['G] : lambda([s], s+new_variable(integer));
(%o19)       lambda([s], s + new_variable(integer))
(%i20) to_poly_solve(G(x - a) = b,x);
(%o20)             %union([x = b + a + %z125])
```



**Notes**



- * 
The solve variables needn’t be symbols; when `fullratsubst` is 
able to appropriately make substitutions, the solve variables can be nonsymbols:



```maxima
(%i1) to_poly_solve([x^2 + y^2 + x * y = 5, x * y = 8],
                    [x^2 + y^2, x * y]);
                                  2    2
(%o1)           %union([x y = 8, y  + x  = - 3])
```



- * 
For equations that involve complex conjugates, the solver automatically
appends the conjugate equations; for example



```maxima
(%i1) declare(x,complex)$

(%i2) to_poly_solve(x + (5 + %i) * conjugate(x) = 1, x);
                                   %i + 21
(%o2)              %union([x = - -----------])
                                 25 %i - 125
(%i3) declare(y,complex)$

(%i4) to_poly_solve(set(conjugate(x) - y = 42 + %i,
                        x + conjugate(y) = 0), set(x,y));
                           %i - 42        %i + 42
(%o4)        %union([x = - -------, y = - -------])
                              2              2
```



- * 
For an equation that involves the absolute value function, the
`to_poly_solve` consults the fact database to decide if the
argument to the absolute value is complex valued.  When

```maxima
(%i1) to_poly_solve(abs(x) = 6, x);
(%o1)              %union([x = - 6], [x = 6])
(%i2) declare(z,complex)$
(%i3) to_poly_solve(abs(z) = 6, z);
(%o3) %union(%if((%c11 # 0) %and (%c11 conjugate(%c11) - 36 = 
                                       0), [z = %c11], %union()))
```

*This is the only situation that the solver consults the fact database.  If
a solve variable is declared to be an integer, for example, `to_poly_solve`
ignores this declaration*.


**Relevant option variables** *algexact, resultant, algebraic*


**Related functions** *to_poly*


**To use** `load("to_poly_solve")`


**Status:** The function `to_poly_solve` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

