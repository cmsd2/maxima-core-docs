## to_poly_solve

<!-- category: Solving -->
<!-- keywords: %and -->
<!-- signatures: %and -->
### Function: %and

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

<!-- category: Solving -->
<!-- keywords: %if -->
<!-- signatures: %if(bool, a, b) -->
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

<!-- category: Solving -->
<!-- keywords: %or -->
<!-- signatures: %or -->
### Function: %or

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

<!-- category: Solving -->
<!-- keywords: %union -->
<!-- signatures: %union(soln_1, soln_2, soln_3, ...), %union() -->
### Function: %union (soln_1, soln_2, soln_3, ...)

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

<!-- category: Solving -->
<!-- keywords: complex_number_p -->
<!-- signatures: complex_number_p(x) -->
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

<!-- category: Solving -->
<!-- keywords: compose_functions -->
<!-- signatures: compose_functions(l) -->
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

<!-- category: Solving -->
<!-- keywords: dfloat -->
<!-- signatures: dfloat(x) -->
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

<!-- category: Solving -->
<!-- keywords: elim -->
<!-- signatures: elim(l, x) -->
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

<!-- category: Solving -->
<!-- keywords: elim_allbut -->
<!-- signatures: elim_allbut(l, x) -->
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

<!-- category: Solving -->
<!-- keywords: eliminate_using -->
<!-- signatures: eliminate_using(l, e, x) -->
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

<!-- category: Solving -->
<!-- keywords: fourier_elim -->
<!-- signatures: fourier_elim([eq1, eq2, ...], [var1, var, ...]) -->
### Function: fourier_elim ([eq1, eq2, ...], [var1, var, ...])

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

<!-- category: Solving -->
<!-- keywords: isreal_p -->
<!-- signatures: isreal_p(e) -->
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

<!-- category: Solving -->
<!-- keywords: new_variable -->
<!-- signatures: new_variable(type) -->
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

<!-- category: Solving -->
<!-- keywords: nicedummies -->
<!-- signatures: nicedummies -->
### Function: nicedummies

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

<!-- category: Solving -->
<!-- keywords: parg -->
<!-- signatures: parg(x) -->
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

<!-- category: Solving -->
<!-- keywords: real_imagpart_to_conjugate -->
<!-- signatures: real_imagpart_to_conjugate(e) -->
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

<!-- category: Solving -->
<!-- keywords: rectform_log_if_constant -->
<!-- signatures: rectform_log_if_constant(e) -->
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

<!-- category: Solving -->
<!-- keywords: simp_inequality -->
<!-- signatures: simp_inequality(e) -->
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

<!-- category: Solving -->
<!-- keywords: standardize_inverse_trig -->
<!-- signatures: standardize_inverse_trig(e) -->
### Function: standardize_inverse_trig (e)

This function applies the identities `cot(x) = atan(1/x), acsc(x) = asin(1/x),` and similarly for `asec, acoth, acsch`
and `asech` to an expression.  See Abramowitz and Stegun, 
Eqs. 4.4.6 through 4.4.8 and 4.6.4 through 4.6.6.


**To use** `load("to_poly_solve")`


**Status** The function `standardize_inverse_trig` is experimental; its
specifications might change and its functionality might be merged into
other Maxima functions.

<!-- category: Solving -->
<!-- keywords: subst_parallel -->
<!-- signatures: subst_parallel(l, e) -->
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

<!-- category: Solving -->
<!-- keywords: to_poly -->
<!-- signatures: to_poly(e, l) -->
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

<!-- category: Solving -->
<!-- keywords: to_poly_solve -->
<!-- signatures: to_poly_solve(e, l, [options]) -->
### Function: to_poly_solve (e, l, [options])

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

