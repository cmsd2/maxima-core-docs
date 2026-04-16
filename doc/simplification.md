## Simplification

### Variable: additive

If `declare(f,additive)` has been executed, then:


(1) If `f` is univariate, whenever the simplifier encounters `f`
applied to a sum, `f` will be distributed over that sum.  I.e.
`f(y+x)` will simplify to `f(y)+f(x)`.


(2) If `f` is a function of 2 or more arguments, additivity is defined as
additivity in the first argument to `f`, as in the case of `sum` or
`integrate`, i.e.  `f(h(x)+g(x),x)` will simplify to
`f(h(x),x)+f(g(x),x)`.  This simplification does not occur when `f` is
applied to expressions of the form `sum(x[i],i,lower-limit,upper-limit)`.


Example:








```maxima
maxima

(%i1) F3 (a + b + c);
(%o1)                     F3(c + b + a)


(%i2) declare (F3, additive);
(%o2)                         done


(%i3) F3 (a + b + c);
(%o3)                 F3(c) + F3(b) + F3(a)
```

### Variable: antisymmetric

If `declare(h,antisymmetric)` is done, this tells the simplifier that
`h` is antisymmetric.  E.g.  `h(x,z,y)` will simplify to 
`- h(x, y, z)`.  That is, it will give (-1)^n times the result given by
`symmetric` or `commutative`, where n is the number of interchanges
of two arguments necessary to convert it to that form.


Examples:













```maxima
maxima

(%i1) S (b, a);
(%o1)                        S(b, a)


(%i2) declare (S, symmetric);
(%o2)                         done


(%i3) S (b, a);
(%o3)                        S(a, b)


(%i4) S (a, c, e, d, b);
(%o4)                   S(a, b, c, d, e)


(%i5) T (b, a);
(%o5)                        T(b, a)


(%i6) declare (T, antisymmetric);
(%o6)                         done


(%i7) T (b, a);
(%o7)                       - T(a, b)


(%i8) T (a, c, e, d, b);
(%o8)                   T(a, b, c, d, e)
```

See also: `symmetric`, `commutative`.

### Function: apply1 (expr, rule_1, ..., rule_n)

Repeatedly applies *rule_1* to
*expr* until it fails, then repeatedly applies the same rule to all
subexpressions of *expr*, left to right, until *rule_1* has failed
on all subexpressions.  Call the result of transforming *expr* in this
manner *expr_2*.  Then *rule_2* is applied in the same fashion
starting at the top of *expr_2*.  When *rule_n* fails on the final
subexpression, the result is returned.


`maxapplydepth` is the depth of the deepest subexpressions processed by
`apply1` and `apply2`.


See also `applyb1`, `apply2` and `let`.

See also: `applyb1`, `apply2`, `let`.

### Function: apply2 (expr, rule_1, ..., rule_n)

If *rule_1* fails on a given subexpression, then *rule_2* is
repeatedly applied, etc.  Only if all rules fail on a given
subexpression is the whole set of rules repeatedly applied to the next
subexpression.  If one of the rules succeeds, then the same
subexpression is reprocessed, starting with the first rule.


`maxapplydepth` is the depth of the deepest subexpressions processed by
`apply1` and `apply2`.


See also `apply1` and `let`.

See also: `apply1`, `let`.

### Function: applyb1 (expr, rule_1, ..., rule_n)

Repeatedly applies *rule_1* to the deepest subexpression of *expr*
until it fails, then repeatedly applies the same rule one level higher (i.e.,
larger subexpressions), until *rule_1* has failed on the top-level
expression.  Then *rule_2* is applied in the same fashion to the result of
*rule_1*.  After *rule_n* has been applied to the top-level expression,
the result is returned.


`applyb1` is similar to `apply1` but works from
the bottom up instead of from the top down.


`maxapplyheight` is the maximum height which `applyb1` reaches
before giving up.


See also `apply1`, `apply2` and `let`.

See also: `apply1`, `apply2`, `let`.

### Function: clear_rules ()

Executes `kill (rules)` and then resets the next rule number to 1
for addition `+`, multiplication `*`, and exponentiation `^`.

### Function: combine (expr)

Simplifies the sum *expr* by combining terms with the same
denominator into a single term.


See also: `rncombine`.


Example:







```maxima
maxima

(%i1) 1*f/2*b + 2*c/3*a + 3*f/4*b +c/5*b*a;
                      5 b f   a b c   2 a c
(%o1)                 ----- + ----- + -----
                        4       5       3


(%i2) combine (%);
                  75 b f + 4 (3 a b c + 10 a c)
(%o2)             -----------------------------
                               60
```

See also: `rncombine`.

### Variable: commutative

If `declare(h, commutative)` is done, this tells the simplifier that
`h` is a commutative function.  E.g.  `h(x, z, y)` will simplify to
`h(x, y, z)`.  This is the same as `symmetric`.


Example:











```maxima
maxima

(%i1) S (b, a);
(%o1)                        S(b, a)


(%i2) S (a, b) + S (b, a);
(%o2)                   S(b, a) + S(a, b)


(%i3) declare (S, commutative);
(%o3)                         done


(%i4) S (b, a);
(%o4)                        S(a, b)


(%i5) S (a, b) + S (b, a);
(%o5)                       2 S(a, b)


(%i6) S (a, c, e, d, b);
(%o6)                   S(a, b, c, d, e)
```

See also: `symmetric`.

### Variable: current_let_rule_package

Default value: `default_let_rule_package`


`current_let_rule_package` is the name of the rule package that is used by
functions in the `let` package (`letsimp`, etc.) 
if no other rule package is specified.
This variable may be assigned the name of any rule package defined
via the `let` command.


If a call such as `letsimp (expr, rule_pkg_name)` is made,
the rule package `rule_pkg_name` is used for that function call only,
and the value of `current_let_rule_package` is not changed.

### Variable: default_let_rule_package

Default value: `default_let_rule_package`



`default_let_rule_package` is the name of the rule package used when one
is not explicitly set by the user with `let` or by changing the value of
`current_let_rule_package`.

### Function: define_opproperty (property_name, simplifier_fn)

Declares the symbol *property_name* to be an operator property,
which is simplified by *simplifier_fn*,
which may be the name of a Maxima or Lisp function or a lambda expression.
After `define_opproperty` is called,
functions and operators may be declared to have the *property_name* property,
and *simplifier_fn* is called to simplify them.


*simplifier_fn* must be a function of one argument,
which is an expression in which the main operator is declared to have the *property_name* property.


*simplifier_fn* is called with the global flag `simp` disabled.
Therefore *simplifier_fn* must be able to carry out its simplification
without making use of the general simplifier.


`define_opproperty` appends *property_name* to the
global list `opproperties`.


`define_opproperty` returns `done`.


Example:


Declare a new property, `identity`, which is simplified by `simplify_identity`.
Declare that `f` and `g` have the new property.










```maxima
maxima

(%i1) define_opproperty (identity, simplify_identity);
(%o1)                         done


(%i2) simplify_identity(e) := first(e);
(%o2)           simplify_identity(e) := first(e)


(%i3) declare ([f, g], identity);
(%o3)                         done


(%i4) f(10 + t);
(%o4)                        t + 10


(%i5) g(3*u) - f(2*u);
(%o5)                           u
```

See also: `opproperties`.

### Function: defmatch (defmatch, progname, pattern, x_1, ..., x_n, defmatch, progname, pattern)

Defines a function `progname(expr, x_1, ..., x_n)`
which tests *expr* to see if it matches *pattern*.


*pattern* is an expression containing the pattern arguments *x_1*,
..., *x_n* (if any) and some pattern variables (if any).  The pattern
arguments are given explicitly as arguments to `defmatch` while the pattern
variables are declared by the `matchdeclare` function.  Any variable not
declared as a pattern variable in `matchdeclare` or as a pattern argument
in `defmatch` matches only itself.


The first argument to the created function *progname* is an expression to be
matched against the pattern and the other arguments are the actual arguments
which correspond to the dummy variables *x_1*, ..., *x_n* in the
pattern.


If the match is successful, *progname* returns a list of equations whose
left sides are the pattern arguments and pattern variables, and whose right
sides are the subexpressions which the pattern arguments and variables matched.
The pattern variables, but not the pattern arguments, are assigned the
subexpressions they match.  If the match fails, *progname* returns
`false`.


A literal pattern (that is, a pattern which contains neither pattern arguments
nor pattern variables) returns `true` if the match succeeds.


See also `matchdeclare`, `defrule`, `tellsimp` and
`tellsimpafter`.


Examples:


Define a function `linearp(expr, x)` which
tests `expr` to see if it is of the form `a*x + b`
such that `a` and `b` do not contain `x` and `a` is nonzero.
This match function matches expressions which are linear in any variable,
because the pattern argument `x` is given to `defmatch`.













```maxima
maxima

(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b,
                    freeof(x));
(%o1)                         done


(%i2) defmatch (linearp, a*x + b, x);
(%o2)                        linearp


(%i3) linearp (3*z + (y + 1)*z + y^2, z);
                         2
(%o3)              [b = y , a = y + 4, x = z]


(%i4) a;
(%o4)                         y + 4


(%i5) b;
                                2
(%o5)                          y


(%i6) x;
(%o6)                           x
```


Define a function `linearp(expr)` which tests `expr`
to see if it is of the form `a*x + b`
such that `a` and `b` do not contain `x` and `a` is nonzero.
This match function only matches expressions linear in `x`,
not any other variable, because no pattern argument is given to `defmatch`.










```maxima
maxima

(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b,
                    freeof(x));
(%o1)                         done


(%i2) defmatch (linearp, a*x + b);
(%o2)                        linearp


(%i3) linearp (3*z + (y + 1)*z + y^2);
(%o3)                         false


(%i4) linearp (3*x + (y + 1)*x + y^2);
                             2
(%o4)                  [b = y , a = y + 4]
```


Define a function `checklimits(expr)` which tests `expr`
to see if it is a definite integral.














```maxima
maxima

(%i1) matchdeclare ([a, f], true);
(%o1)                         done


(%i2) constinterval (l, h) := constantp (h - l);
(%o2)        constinterval(l, h) := constantp(h - l)


(%i3) matchdeclare (b, constinterval (a));
(%o3)                         done


(%i4) matchdeclare (x, atom);
(%o4)                         done


(%i5) simp : false;
(%o5)                         false


(%i6) defmatch (checklimits, 'integrate (f, x, a, b));
(%o6)                      checklimits


(%i7) simp : true;
(%o7)                         true


(%i8) 'integrate (sin(t), t, %pi + x, 2*%pi + x);
                       x + 2 %pi
                      /
                      |
(%o8)                 |          sin(t) dt
                      |
                      /
                       x + %pi


(%i9) checklimits (%);
(%o9)    [b = x + 2 %pi, a = x + %pi, x = t, f = sin(t)]
```

See also: `matchdeclare`, `defrule`, `tellsimp`, `tellsimpafter`.

### Function: defrule (rulename, pattern, replacement)

Defines and names a replacement rule for the given pattern.  If the rule named
*rulename* is applied to an expression (by `apply1`, `applyb1`, or
`apply2`), every subexpression matching the pattern will be replaced by the
replacement.  All variables in the replacement which have been
assigned values by the pattern match are assigned those values in the
replacement which is then simplified.


The rules themselves can be
treated as functions which transform an expression by one
operation of the pattern match and replacement.
If the match fails, the rule function returns `false`.

### Function: demoivre (expr)

The function `demoivre (expr)` converts one expression
without setting the global variable `demoivre`.


When the variable `demoivre` is `true`, complex exponentials are
converted into equivalent expressions in terms of circular functions:
`exp (a + b*%i)` simplifies to `%e^a * (cos(b) + %i*sin(b))`
if `b` is free of `%i`.  `a` and `b` are not expanded.


The default value of `demoivre` is `false`.


`exponentialize` converts circular and hyperbolic functions to exponential
form.  `demoivre` and `exponentialize` cannot both be true at the same
time.

### Function: disprule (disprule, rulename_1, ..., rulename_2, disprule, all)

Display rules with the names *rulename_1*, ..., *rulename_n*,
as returned by `defrule`, `tellsimp`, or `tellsimpafter`,
or a pattern defined by `defmatch`.
Each rule is displayed with an intermediate expression label (`%t`).


`disprule (all)` displays all rules.


`disprule` quotes its arguments.
`disprule` returns the list of intermediate expression labels corresponding
to the displayed rules.


See also `letrules`,  which displays rules defined by `let`.


Examples:










```maxima
maxima

(%i1) tellsimpafter (foo (x, y), bar (x) + baz (y));
(%o1)                   [foorule1, false]


(%i2) tellsimpafter (x + y, special_add (x, y));
(%o2)                   [+rule1, simplus]


(%i3) defmatch (quux, mumble (x));
(%o3)                         quux


(%i4) disprule (foorule1, ?\+rule1, quux);
(%t4)        foorule1 : foo(x, y) -> baz(y) + bar(x)

(%t5)          +rule1 : y + x -> special_add(x, y)

(%t6)                quux : mumble(x) -> []

(%o6)                    [%t4, %t5, %t6]


(%i7) ev(%);
(%o7) [foorule1 : foo(x, y) -> baz(y) + bar(x), 
     +rule1 : y + x -> special_add(x, y), quux : mumble(x) -> []]
```

See also: `letrules`, `let`.

### Function: distrib (expr)

Distributes sums over products.  It differs from `expand` in that it works
at only the top level of an expression, i.e., it doesn’t recurse and it is
faster than `expand`.  It differs from `multthru` in that it expands
all sums at that level.


Examples:









```maxima
maxima

(%i1) distrib ((a+b) * (c+d));
(%o1)                 b d + a d + b c + a c


(%i2) multthru ((a+b) * (c+d));
(%o2)                 (b + a) d + (b + a) c


(%i3) distrib (1/((a+b) * (c+d)));
                                1
(%o3)                    ---------------
                         (b + a) (d + c)


(%i4) expand (1/((a+b) * (c+d)), 1, 0);
                                1
(%o4)                 ---------------------
                      b d + a d + b c + a c
```

### Variable: distribute_over

Default value: `true`


`distribute_over` controls the mapping of functions over bags like lists, 
matrices, and equations.  At this time not all Maxima functions have this 
property.  It is possible to look up this property with the command
`properties`..


The mapping of functions is switched off, when setting `distribute_over` 
to the value `false`.


Examples:


The `sin` function maps over a list:






```maxima
maxima

(%i1) sin([x,1,1.0]);
(%o1)         [sin(x), sin(1), 0.8414709848078965]
```


`mod` is a function with two arguments which maps over lists.  Mapping over 
nested lists is possible too:







```maxima
maxima

(%i1) mod([x,11,2*a],10);
(%o1)             [mod(x, 10), 1, 2 mod(a, 5)]


(%i2) mod([[x,y,z],11,2*a],10);
(%o2) [[mod(x, 10), mod(y, 10), mod(z, 10)], 1, 2 mod(a, 5)]
```


Mapping of the `floor` function over a matrix and an equation:







```maxima
maxima

(%i1) floor(matrix([a,b],[c,d]));
                     [ floor(a)  floor(b) ]
(%o1)                [                    ]
                     [ floor(c)  floor(d) ]


(%i2) floor(a=b);
(%o2)                  floor(a) = floor(b)
```


Functions with more than one argument map over any of the arguments or all
arguments:






```maxima
maxima

(%i1) expintegral_e([1,2],[x,y]);
(%o1) [[expintegral_e(1, x), expintegral_e(1, y)], 
                      [expintegral_e(2, x), expintegral_e(2, y)]]
```


Check if a function has the property distribute_over:






```maxima
maxima

(%i1) properties(abs);
(%o1) [limit function, integral, rule, distributes over bags, 
                                          noun, gradef, transfun]
```


The mapping of functions is switched off, when setting `distribute_over` 
to the value `false`.









```maxima
maxima

(%i1) distribute_over;
(%o1)                         true


(%i2) sin([x,1,1.0]);
(%o2)         [sin(x), sin(1), 0.8414709848078965]


(%i3) distribute_over : not distribute_over;
(%o3)                         false


(%i4) sin([x,1,1.0]);
(%o4)                   sin([x, 1, 1.0])
```

See also: `properties`.

### Variable: domain

Default value: `real`


When `domain` is set to `complex`, `sqrt (x^2)` will remain
`sqrt (x^2)` instead of returning `abs(x)`.

### Variable: evenfun

`declare(f, evenfun)` or `declare(f, oddfun)` tells Maxima to recognize
the function `f` as an even or odd function.


Examples:











```maxima
maxima

(%i1) o (- x) + o (x);
(%o1)                     o(x) + o(- x)


(%i2) declare (o, oddfun);
(%o2)                         done


(%i3) o (- x) + o (x);
(%o3)                           0


(%i4) e (- x) - e (x);
(%o4)                     e(- x) - e(x)


(%i5) declare (e, evenfun);
(%o5)                         done


(%i6) e (- x) - e (x);
(%o6)                           0
```

### Function: expand (expand, expr, expand, expr, p, n)

Expand expression *expr*.
Products of sums and exponentiated sums are
multiplied out, numerators of rational expressions which are sums are
split into their respective terms, and multiplication (commutative
and non-commutative) are distributed over addition at all levels of
*expr*.


For polynomials one should usually use `ratexpand` which uses a
more efficient algorithm.


`maxnegex` and `maxposex` control the maximum negative and
positive exponents, respectively, which will expand.


`expand (expr, p, n)` expands *expr*, 
using *p* for `maxposex` and *n* for `maxnegex`.
This is useful in order to expand part but not all of an expression.


`expon` - the exponent of the largest negative power which is
automatically expanded (independent of calls to `expand`).  For example
if `expon` is 4 then `(x+1)^(-5)` will not be automatically expanded.


`expop` - the highest positive exponent which is automatically expanded.
Thus `(x+1)^3`, when typed, will be automatically expanded only if
`expop` is greater than or equal to 3.  If it is desired to have
`(x+1)^n` expanded where `n` is greater than `expop` then
executing `expand ((x+1)^n)` will work only if `maxposex` is not
less than `n`.


`expand(expr, 0, 0)` causes a resimplification of `expr`.  `expr`
is not reevaluated.  In distinction from `ev(expr, noeval)` a special
representation (e. g. a CRE form) is removed.  See also `resimplify` and
`ev`.


The `expand` flag used with `ev` causes expansion.


The file `share/simplification/facexp.mac`




contains several related functions (in particular `facsum`,
`factorfacsum` and `collectterms`, which are autoloaded) and variables
(`nextlayerfactor` and `facsum_combine`) that provide the user with
the ability to structure expressions by controlled expansion.

Brief function descriptions are available in `simplification/facexp.usg`.
A demo is available by doing `demo("facexp")`.


Examples:











```maxima
maxima

(%i1) expr:(x+1)^2*(y+1)^3;
                               2        3
(%o1)                   (x + 1)  (y + 1)


(%i2) expand(expr);
       2  3        3    3      2  2        2      2      2
(%o2) x  y  + 2 x y  + y  + 3 x  y  + 6 x y  + 3 y  + 3 x  y
                                                      2
                                     + 6 x y + 3 y + x  + 2 x + 1


(%i3) expand(expr,2);
               2        3              3          3
(%o3)         x  (y + 1)  + 2 x (y + 1)  + (y + 1)


(%i4) expr:(x+1)^-2*(y+1)^3;
                                   3
                            (y + 1)
(%o4)                       --------
                                   2
                            (x + 1)


(%i5) expand(expr);
            3               2
           y             3 y            3 y             1
(%o5) ------------ + ------------ + ------------ + ------------
       2              2              2              2
      x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1


(%i6) expand(expr,2,2);
                                   3
                            (y + 1)
(%o6)                     ------------
                           2
                          x  + 2 x + 1
```


Resimplify an expression without expansion:








```maxima
maxima

(%i1) expr:(1+x)^2*sin(x);
                                2
(%o1)                    (x + 1)  sin(x)


(%i2) exponentialize:true;
(%o2)                         true


(%i3) expand(expr,0,0);
                     %i x     - %i x            2
                  (%e     - %e      ) %i (x + 1)
(%o3)           - -------------------------------
                                 2
```

See also: `resimplify`, `ev`.

### Function: expandwrt (expr, x_1, ..., x_n)

Expands expression `expr` with respect to the 
variables *x_1*, ..., *x_n*.
All products involving the variables appear explicitly.  The form returned
will be free of products of sums of expressions that are not free of
the variables.  *x_1*, ..., *x_n*
may be variables, operators, or expressions.


By default, denominators are not expanded, but this can be controlled by
means of the switch `expandwrt_denom`.


This function is autoloaded from
`simplification/stopex.mac`.

### Variable: expandwrt_denom

Default value: `false`


`expandwrt_denom` controls the treatment of rational
expressions by `expandwrt`.  If `true`, then both the numerator and
denominator of the expression will be expanded according to the
arguments of `expandwrt`, but if `expandwrt_denom` is `false`,
then only the numerator will be expanded in that way.

### Function: expandwrt_factored (expr, x_1, ..., x_n)

is similar to `expandwrt`, but treats expressions that are products
somewhat differently.  `expandwrt_factored` expands only on those factors
of `expr` that contain the variables *x_1*, ..., *x_n*.



This function is autoloaded from `simplification/stopex.mac`.

### Variable: expon

Default value: 0


`expon` is the exponent of the largest negative power which
is automatically expanded (independent of calls to `expand`).  For
example, if `expon` is 4 then `(x+1)^(-5)` will not be automatically
expanded.

### Function: exponentialize (expr)

The function `exponentialize (expr)` converts 
circular and hyperbolic functions in *expr* to exponentials,
without setting the global variable `exponentialize`.


When the variable `exponentialize` is `true`,
all circular and hyperbolic functions are converted to exponential form.
The default value is `false`.


`demoivre` converts complex exponentials into circular functions.
`exponentialize` and `demoivre` cannot
both be true at the same time.

### Variable: expop

Default value: 0


`expop` is the highest positive exponent which is automatically expanded.
Thus `(x + 1)^3`, when typed, will be automatically expanded only if
`expop` is greater than or equal to 3.  If it is desired to have
`(x + 1)^n` expanded where `n` is greater than `expop` then
executing `expand ((x + 1)^n)` will work only if `maxposex` is not
less than n.

### Variable: lassociative

`declare (g, lassociative)` tells the Maxima simplifier that `g` is
left-associative.  E.g., `g (g (a, b), g (c, d))` will simplify to
`g (g (g (a, b), c), d)`.


See also `rassociative`.

See also: `rassociative`.

### Function: let (let, prod, repl, predname, arg_1, ..., arg_n, let, prod, repl, predname, arg_1, ..., arg_n, package_name)

Defines a substitution rule for `letsimp` such that *prod* is replaced
by *repl*.  *prod* is a product of positive or negative powers of the
following terms:



- *
Atoms which `letsimp` will search for literally unless previous to calling
`letsimp` the `matchdeclare` function is used to associate a
predicate with the atom.  In this case `letsimp` will match the atom to
any term of a product satisfying the predicate.
- *
Kernels such as `sin(x)`, `n!`, `f(x,y)`, etc.  As with atoms
above `letsimp` will look for a literal match unless `matchdeclare`
is used to associate a predicate with the argument of the kernel.


A term to a positive power will only match a term having at least that
power.  A term to a negative power
on the other hand will only match a term with a power at least as
negative.  In the case of negative powers in *prod* the switch
`letrat` must be set to `true`.
See also `letrat`.


If a predicate is included in the `let` function followed by a list of
arguments, a tentative match (i.e. one that would be accepted if the predicate
were omitted) is accepted only if `predname (arg_1', ..., arg_n')`
evaluates to `true` where *arg_i’* is the value matched to *arg_i*.
The *arg_i* may be the name of any atom or the argument of any kernel
appearing in *prod*.
*repl* may be any rational expression.  
If any of the atoms or arguments from *prod* appear in *repl* the
appropriate substitutions are made.  


The global flag `letrat` controls the simplification of quotients by
`letsimp`.  When `letrat` is `false`, `letsimp` simplifies
the numerator and denominator of *expr* separately, and does not simplify
the quotient.  Substitutions such as `n!/n` goes to `(n-1)!` then
fail.  When `letrat` is `true`, then the numerator, denominator, and
the quotient are simplified in that order.


These substitution functions allow you to work with several rule packages at
once.  Each rule package can contain any number of `let` rules and is
referenced by a user-defined name.  The command `let ([prod, repl, predname, arg_1, ..., arg_n], package_name)`
adds the rule *predname* to the rule package *package_name*.  The
command `letsimp (expr, package_name)` applies the rules in 
*package_name*.  `letsimp (expr, package_name1, package_name2, ...)` is equivalent to `letsimp (expr, package_name1)` followed by `letsimp (%, package_name2)`,
...


`current_let_rule_package` is the name of the rule package that is
presently being used.  This variable may be assigned the name of any rule
package defined via the `let` command.  Whenever any of the functions
comprising the `let` package are called with no package name, the package
named by `current_let_rule_package` is used.  If a call such as
`letsimp (expr, rule_pkg_name)` is made, the rule package
*rule_pkg_name* is used for that `letsimp` command only, and
`current_let_rule_package` is not changed.  If not otherwise specified,
`current_let_rule_package` defaults to `default_let_rule_package`.













```maxima
maxima
(%i1) matchdeclare ([a, a1, a2], true)$
(%i2) oneless (x, y) := is (x = y-1)$

(%i3) let (a1*a2!, a1!, oneless, a2, a1);
(%o3)         a1 a2! --> a1! where oneless(a2, a1)

(%i4) letrat: true$

(%i5) let (a1!/a1, (a1-1)!);
                        a1!
(%o5)                   --- --> (a1 - 1)!
                        a1


(%i6) letsimp (n*m!*(n-1)!/m);
(%o6)                      (m - 1)! n!


(%i7) let (sin(a)^2, 1 - cos(a)^2);
                        2               2
(%o7)                sin (a) --> 1 - cos (a)


(%i8) letsimp (sin(x)^4);
                        4           2
(%o8)                cos (x) - 2 cos (x) + 1
```

See also: `letrat`.

### Variable: let_rule_packages

Default value: `[default_let_rule_package]`


`let_rule_packages` is a list of all user-defined let rule packages
plus the default package `default_let_rule_package`.

### Variable: letrat

Default value: `false`


When `letrat` is `false`, `letsimp` simplifies the
numerator and denominator of a ratio separately,
and does not simplify the quotient.


When `letrat` is `true`,
the numerator, denominator, and their quotient are simplified in that order.











```maxima
maxima
(%i1) matchdeclare (n, true)$

(%i2) let (n!/n, (n-1)!);
                         n!
(%o2)                    -- --> (n - 1)!
                         n

(%i3) letrat: false$

(%i4) letsimp (a!/a);
                               a!
(%o4)                          --
                               a

(%i5) letrat: true$

(%i6) letsimp (a!/a);
(%o6)                       (a - 1)!
```

### Function: letrules (letrules, letrules, package_name)

Displays the rules in a rule package.
`letrules ()` displays the rules in the current rule package.
`letrules (package_name)` displays the rules in *package_name*.


The current rule package is named by `current_let_rule_package`.
If not otherwise specified, `current_let_rule_package`
defaults to `default_let_rule_package`.


See also `disprule`, which displays rules defined by `tellsimp` and
`tellsimpafter`.

See also: `disprule`, `tellsimp`, `tellsimpafter`.

### Function: letsimp (letsimp, expr, letsimp, expr, package_name, letsimp, expr, package_name_1, ..., package_name_n)

Repeatedly applies the substitution rules defined by `let`
until no further change is made to *expr*.


`letsimp (expr)` uses the rules from `current_let_rule_package`.


`letsimp (expr, package_name)` uses the rules from
*package_name* without changing `current_let_rule_package`.


`letsimp (expr, package_name_1, ..., package_name_n)`
is equivalent to `letsimp (expr, package_name_1)`,
followed by `letsimp (%, package_name_2)`, and so on.


See also `let`.
For other ways to do substitutions see also `subst`,
`psubst`, `at` and `ratsubst`.













```maxima
maxima

(%i1) e0: e(k) = -(9*y(k))/(5*z)-u(k-1)/(5*z)+(4*y(k))/(5*z^2)
                 +(3*u(k-1))/(5*z^2)+y(k)-(2*u(k-1))/5;
               9 y(k)   u(k - 1)   4 y(k)   3 u(k - 1)
(%o1) e(k) = - ------ - -------- + ------ + ---------- + y(k)
                5 z       5 z          2          2
                                    5 z        5 z
                                                       2 u(k - 1)
                                                     - ----------
                                                           5

(%i2) matchdeclare(h,any)$

(%i3) let(u(h)/z,u(h-1));
                        u(h)
(%o3)                   ---- --> u(h - 1)
                         z


(%i4) let(y(h)/z,y(h-1));
                        y(h)
(%o4)                   ---- --> y(h - 1)
                         z


(%i5) e1:letsimp(e0);
                    9 y(k - 1)   2 u(k - 1)   4 y(k - 2)
(%o5) e(k) = y(k) - ---------- - ---------- + ----------
                        5            5            5
                                            u(k - 2)   3 u(k - 3)
                                          - -------- + ----------
                                               5           5
```

See also: `let`, `subst`, `psubst`, `at`, `ratsubst`.

### Variable: linear

One of Maxima’s operator properties.  For univariate `f` so
declared, "expansion" `f(x + y)` yields `f(x) + f(y)`,
`f(a*x)` yields `a*f(x)` takes
place where `a` is a "constant".  For functions of two or more arguments,
"linearity" is defined to be as in the case of `sum` or `integrate`,
i.e., `f (a*x + b, x)` yields `a*f(x,x) + b*f(1,x)`
for `a` and `b` free of `x`.


Example:









```maxima
maxima

(%i1) declare (f, linear);
(%o1)                         done


(%i2) f(x+y);
(%o2)                      f(y) + f(x)


(%i3) declare (a, constant);
(%o3)                         done


(%i4) f(a*x);
(%o4)                        a f(x)
```


`linear` is equivalent to `additive` and `outative`.
See also `opproperties`.


Example:








```maxima
maxima

(%i1) 'sum (F(k) + G(k), k, 1, inf);
                       inf
                       ____
                       \
(%o1)                   >    (G(k) + F(k))
                       /
                       ----
                       k = 1


(%i2) declare (nounify (sum), linear);
(%o2)                         done


(%i3) 'sum (F(k) + G(k), k, 1, inf);
                     inf          inf
                     ____         ____
                     \            \
(%o3)                 >    G(k) +  >    F(k)
                     /            /
                     ----         ----
                     k = 1        k = 1
```

See also: `sum`, `integrate`, `additive`, `outative`, `opproperties`.

### Function: matchdeclare (a_1, pred_1, ..., a_n, pred_n)

Associates a predicate *pred_k* 
with a variable or list of variables *a_k*
so that *a_k* matches expressions
for which the predicate returns anything other than `false`.


A predicate is the name of a function,
or a lambda expression,
or a function call or lambda call missing the last argument,
or `true` or `all`.
Any expression matches `true` or `all`.
If the predicate is specified as a function call or lambda call,
the expression to be tested is appended to the list of arguments;
the arguments are evaluated at the time the match is evaluated.
Otherwise, the predicate is specified as a function name or lambda expression,
and the expression to be tested is the sole argument.
A predicate function need not be defined when `matchdeclare` is called;
the predicate is not evaluated until a match is attempted.


A predicate may return a Boolean expression as well as `true` or
`false`.  Boolean expressions are evaluated by `is` within the
constructed rule function, so it is not necessary to call `is` within the
predicate.


If an expression satisfies a match predicate, the match variable is assigned the
expression, except for match variables which are operands of addition `+`
or multiplication `*`.  Only addition and multiplication are handled
specially; other n-ary operators (both built-in and user-defined) are treated
like ordinary functions.



In the case of addition and multiplication, the match variable may be assigned a
single expression which satisfies the match predicate, or a sum or product
(respectively) of such expressions.  Such multiple-term matching is greedy:
predicates are evaluated in the order in which their associated variables
appear in the match pattern, and a term which satisfies more than one predicate
is taken by the first predicate which it satisfies.  Each predicate is tested
against all operands of the sum or product before the next predicate is
evaluated.  In addition, if 0 or 1 (respectively) satisfies a match predicate,
and there are no other terms which satisfy the predicate, 0 or 1 is assigned to
the match variable associated with the predicate.


The algorithm for processing addition and multiplication patterns makes some
match results (for example, a pattern in which a "match anything" variable
appears) dependent on the ordering of terms in the match pattern and in the
expression to be matched.  However, if all match predicates are mutually
exclusive, the match result is insensitive to ordering, as one match predicate
cannot accept terms matched by another.


Calling `matchdeclare` with a variable *a* as an argument changes the
`matchdeclare` property for *a*, if one was already declared; only the
most recent `matchdeclare` is in effect when a rule is defined.  Later
changes to the `matchdeclare` property (via `matchdeclare` or
`remove`) do not affect existing rules.


`propvars (matchdeclare)` returns the list of all variables for which there
is a `matchdeclare` property.  `printprops (a, matchdeclare)`
returns the predicate for variable `a`.
`printprops (all, matchdeclare)` returns the list of predicates for all
`matchdeclare` variables.  `remove (a, matchdeclare)` removes
the `matchdeclare` property from *a*.


The functions `defmatch`, `defrule`, `tellsimp`,
`tellsimpafter`, and `let` construct rules which test expressions
against patterns.


`matchdeclare` quotes its arguments.
`matchdeclare` always returns `done`.


Examples:


A predicate is the name of a function,
or a lambda expression,
or a function call or lambda call missing the last argument,
or `true` or `all`.











```maxima
maxima

(%i1) matchdeclare (aa, integerp);
(%o1)                         done


(%i2) matchdeclare (bb, lambda ([x], x > 0));
(%o2)                         done


(%i3) matchdeclare (cc, freeof (%e, %pi, %i));
(%o3)                         done


(%i4) matchdeclare (dd, lambda ([x, y], gcd (x, y) = 1) (1728));
(%o4)                         done


(%i5) matchdeclare (ee, true);
(%o5)                         done


(%i6) matchdeclare (ff, all);
(%o6)                         done
```


If an expression satisfies a match predicate,
the match variable is assigned the expression.








```maxima
maxima

(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done


(%i2) defrule (r1, bb^aa, ["integer" = aa, "atom" = bb]);
                    aa
(%o2)        r1 : bb   -> [integer = aa, atom = bb]


(%i3) r1 (%pi^8);
(%o3)               [integer = 8, atom = %pi]
```


In the case of addition and multiplication, the match variable may be assigned
a single expression which satisfies the match predicate, or a sum or product
(respectively) of such expressions.












```maxima
maxima

(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done


(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]


(%i3) r1 (8 + a*b + sin(x));
(%o3)     [all atoms = 8, all nonatoms = sin(x) + a b]


(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]


(%i5) r2 (8 * (a + b) * sin(x));
(%o5)    [all atoms = 8, all nonatoms = (b + a) sin(x)]
```


When matching arguments of `+` and `*`,
if all match predicates are mutually exclusive,
the match result is insensitive to ordering,
as one match predicate cannot accept terms matched by another.












```maxima
maxima

(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done


(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]


(%i3) r1 (8 + a*b + %pi + sin(x) - c + 2^n);
                                                               n
(%o3) [all atoms = %pi + 8, all nonatoms = sin(x) - c + a b + 2 ]


(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]


(%i5) r2 (8 * (a + b) * %pi * sin(x) / c * 2^n);
                                        n + 3
                                       2      (b + a) sin(x)
(%o5) [all atoms = %pi, all nonatoms = ---------------------]
                                                 c
```


The functions `propvars` and `printprops` return information about
match variables.











```maxima
maxima

(%i1) matchdeclare ([aa, bb, cc], atom, [dd, ee], integerp);
(%o1)                         done


(%i2) matchdeclare (ff, floatnump, gg, lambda ([x], x > 100));
(%o2)                         done


(%i3) propvars (matchdeclare);
(%o3)             [aa, bb, cc, dd, ee, ff, gg]


(%i4) printprops (ee, matchdeclare);
(%o4)                    [integerp(ee)]


(%i5) printprops (gg, matchdeclare);
(%o5)              [lambda([x], x > 100)(gg)]


(%i6) printprops (all, matchdeclare);
(%o6) [atom(aa), atom(bb), atom(cc), integerp(dd), integerp(ee), 
                         floatnump(ff), lambda([x], x > 100)(gg)]
```

### Variable: maxapplydepth

Default value: 10000


`maxapplydepth` is the maximum depth to which `apply1`
and `apply2` will delve.

### Variable: maxapplyheight

Default value: 10000


`maxapplyheight` is the maximum height to which `applyb1`
will reach before giving up.

### Variable: maxnegex

Default value: 1000


`maxnegex` is the largest negative exponent which will
be expanded by the `expand` command, see also `maxposex`.

See also: `maxposex`.

### Variable: maxposex

Default value: 1000


`maxposex` is the largest exponent which will be
expanded with the `expand` command, see also `maxnegex`.

See also: `maxnegex`.

### Variable: multiplicative

`declare(f, multiplicative)` tells the Maxima simplifier that `f`
is multiplicative.



1. If `f` is univariate, whenever the simplifier encounters `f` applied
to a product, `f` distributes over that product.  E.g., `f(x*y)`
simplifies to `f(x)*f(y)`.
This simplification is not applied to expressions of the form `f('product(...))`.
2. If `f` is a function of 2 or more arguments, multiplicativity is
defined as multiplicativity in the first argument to `f`, e.g.,
`f (g(x) * h(x), x)` simplifies to `f (g(x) ,x) * f (h(x), x)`.


`declare(nounify(product), multiplicative)` tells Maxima to simplify symbolic products.


Example:








```maxima
maxima

(%i1) F2 (a * b * c);
(%o1)                       F2(a b c)


(%i2) declare (F2, multiplicative);
(%o2)                         done


(%i3) F2 (a * b * c);
(%o3)                   F2(a) F2(b) F2(c)
```


`declare(nounify(product), multiplicative)` tells Maxima to simplify symbolic products.








```maxima
maxima

(%i1) product (a[i] * b[i], i, 1, n);
                             n
                           _____
                           |   |
(%o1)                      |   | a  b
                           |   |  i  i
                           i = 1


(%i2) declare (nounify (product), multiplicative);
(%o2)                         done


(%i3) product (a[i] * b[i], i, 1, n);
                          n         n
                        _____     _____
                        |   |     |   |
(%o3)                  (|   | a ) |   | b
                        |   |  i  |   |  i
                        i = 1     i = 1
```

### Function: multthru (multthru, expr, multthru, expr_1, expr_2)

Multiplies a factor (which should be a sum) of *expr* by the other factors
of *expr*.  That is, *expr* is `f_1 f_2 ... f_n`
where at least one factor, say *f_i*, is a sum of terms.  Each term in that
sum is multiplied by the other factors in the product.  (Namely all the factors
except *f_i*).  `multthru` does not expand exponentiated sums.
This function is the fastest way to distribute products (commutative or
noncommutative) over sums.  Since quotients are represented as products
`multthru` can be used to divide sums by products as well.


`multthru (expr_1, expr_2)` multiplies each term in
*expr_2* (which should be a sum or an equation) by *expr_1*.  If
*expr_1* is not itself a sum then this form is equivalent to
`multthru (expr_1*expr_2)`.












```maxima
maxima

(%i1) x/(x-y)^2 - 1/(x-y) - f(x)/(x-y)^3;
                      1        x         f(x)
(%o1)             - ----- + -------- - --------
                    x - y          2          3
                            (x - y)    (x - y)


(%i2) multthru ((x-y)^3, %);
                                      2
(%o2)              x (x - y) - (x - y)  - f(x)


(%i3) ratexpand (%);
                           2
(%o3)                   - y  + x y - f(x)


(%i4) ((a+b)^10*s^2 + 2*a*b*s + (a*b)^2)/(a*b*s^2);
                        10  2              2  2
                 (b + a)   s  + 2 a b s + a  b
(%o4)            ------------------------------
                                  2
                             a b s


(%i5) multthru (%);  /* note that this does not expand (b+a)^10 */
                                        10
                       2   a b   (b + a)
(%o5)                  - + --- + ---------
                       s    2       a b
                           s
(%o6)            a . f + a . c . (e + d) + a . b


(%i7) multthru (a.(b+c.(d+e)+f));
(%o7)         a . f + a . c . e + a . c . d + a . b

(%i8) expand (a.(b+c.(d+e)+f));
```

### Variable: negdistrib

Default value: `true`


When `negdistrib` is `true`, -1 distributes over an expression.
E.g., `-(x + y)` becomes `- y - x`.  Setting it to `false`
will allow `- (x + y)` to be displayed like that.  This is sometimes useful
but be very careful: like the `simp` flag, this is one flag you do not
want to set to `false` as a matter of course or necessarily for other
than local use in your Maxima.


Example:









```maxima
maxima

(%i1) negdistrib;
(%o1)                         true


(%i2) -(x+y);
(%o2)                        - y - x


(%i3) negdistrib : not negdistrib ;
(%o3)                         false


(%i4) -(x+y);
(%o4)                       - (y + x)
```

### Variable: opproperties

`opproperties` is the list of the special operator properties recognized
by the Maxima simplifier.


Items are added to the `opproperties` list by the function `define_005fopproperty`.


Example:






```maxima
maxima

(%i1) opproperties;
(%o1) [linear, additive, multiplicative, outative, evenfun, 
oddfun, commutative, symmetric, antisymmetric, nary, 
lassociative, rassociative]
```

See also: `define_opproperty`.

### Variable: outative

`declare(f, outative)` tells the Maxima simplifier that constant factors
in the argument of `f` can be pulled out.



1. If `f` is univariate, whenever the simplifier encounters `f` applied
to a product, that product will be partitioned into factors that are constant
and factors that are not and the constant factors will be pulled out.  E.g.,
`f(a*x)` will simplify to `a*f(x)` where `a` is a constant.
Non-atomic constant factors will not be pulled out.
2. If `f` is a function of 2 or more arguments, outativity is defined as in
the case of `sum` or `integrate`, i.e., `f (a*g(x), x)` will
simplify to `a * f(g(x), x)` for `a` free of `x`.


`sum`, `integrate`, and `limit` are all `outative`.


Example:










```maxima
maxima

(%i1) F1 (100 * x);
(%o1)                       F1(100 x)


(%i2) declare (F1, outative);
(%o2)                         done


(%i3) F1 (100 * x);
(%o3)                       100 F1(x)


(%i4) declare (zz, constant);
(%o4)                         done


(%i5) F1 (zz * y);
(%o5)                       zz F1(y)
```

See also: `sum`, `integrate`, `limit`.

### Function: radcan (expr)

Simplifies *expr*, which can contain logs, exponentials, and radicals, by 
converting it into a form which is canonical over a large class of expressions 
and a given ordering of variables; that is, all functionally equivalent forms 
are mapped into a unique form.  For a somewhat larger class of expressions,
`radcan` produces a regular form.  Two equivalent expressions in this class 
do not necessarily have the same appearance, but their difference can be 
simplified by `radcan` to zero.


For some expressions `radcan` is quite time consuming.  This is the cost 
of exploring certain relationships among the components of the expression for 
simplifications based on factoring and partial-fraction expansions of exponents.


















Examples:








```maxima
maxima

(%i1) radcan((log(x+x^2)-log(x))^a/log(1+x)^(a/2));
                                    a/2
(%o1)                     log(x + 1)


(%i2) radcan((log(1+2*a^x+a^(2*x))/log(1+a^x)));
(%o2)                           2


(%i3) radcan((%e^x-1)/(1+%e^(x/2)));
                              x/2
(%o3)                       %e    - 1
```

### Variable: radexpand

Default value: `true`


`radexpand` controls some simplifications of radicals.


When `radexpand` is `all`, causes nth roots of factors of a product
which are powers of n to be pulled outside of the radical.  E.g. if
`radexpand` is `all`, `sqrt (16*x^2)` simplifies to `4*x`.



More particularly, consider `sqrt (x^2)`.


- *
If `radexpand` is `all` or `assume (x > 0)` has been executed, 
`sqrt(x^2)` simplifies to `x`.
- *
If `radexpand` is `true` and `domain` is `real`
(its default), `sqrt(x^2)` simplifies to `abs(x)`.
- *
If `radexpand` is `false`, or `radexpand` is `true` and
`domain` is `complex`, `sqrt(x^2)` is not simplified.



Note that `domain` only matters when `radexpand` is `true`.

### Variable: rassociative

`declare (g, rassociative)` tells the Maxima
simplifier that `g` is right-associative.  E.g.,
`g(g(a, b), g(c, d))` simplifies to `g(a, g(b, g(c, d)))`.


See also `lassociative`.

See also: `lassociative`.

### Function: remlet (remlet, prod, name, remlet, remlet, all, remlet, all, name)

Deletes the substitution rule, `prod --> repl`, most
recently defined by the `let` function.  If name is supplied the rule is
deleted from the rule package name.


`remlet()` and `remlet(all)` delete all substitution rules from the
current rule package.  If the name of a rule package is supplied, e.g.
`remlet (all, name)`, the rule package *name* is also deleted.


If a substitution is to be changed using the same
product, `remlet` need not be called, just redefine the substitution
using the same product (literally) with the `let` function and the new
replacement and/or predicate name.  Should `remlet (prod)` now be
called the original substitution rule is revived.


See also `remrule`, which removes a rule defined by `tellsimp` or
`tellsimpafter`.

See also: `remrule`, `tellsimp`, `tellsimpafter`.

### Function: remrule (remrule, op, rulename, remrule, op, all)

Removes rules defined by `tellsimp` or `tellsimpafter`.


`remrule (op, rulename)`
removes the rule with the name *rulename* from the operator *op*.
When *op* is a built-in or user-defined operator
(as defined by `infix`, `prefix`, etc.),
*op* and *rulename* must be enclosed in double quote marks.


`remrule (op, all)` removes all rules for the operator *op*.


See also `remlet`, which removes a rule defined by `let`.


Examples:



















```maxima
maxima

(%i1) tellsimp (foo (aa, bb), bb - aa);
(%o1)                   [foorule1, false]


(%i2) tellsimpafter (aa + bb, special_add (aa, bb));
(%o2)                   [+rule1, simplus]


(%i3) infix ("@@");
(%o3)                          @@


(%i4) tellsimp (aa @@ bb, bb/aa);
(%o4)                   [@@rule1, false]


(%i5) tellsimpafter (quux (%pi, %e), %pi - %e);
(%o5)                  [quuxrule1, false]


(%i6) tellsimpafter (quux (%e, %pi), %pi + %e);
(%o6)             [quuxrule2, quuxrule1, false]


(%i7) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
       quux (%e, %pi)];
                                     bb
(%o7) [bb - aa, special_add(aa, bb), --, %pi - %e, %pi + %e]
                                     aa


(%i8) remrule (foo, foorule1);
(%o8)                          foo


(%i9) remrule ("+", ?\+rule1);
(%o9)                           +


(%i10) remrule ("@@", ?\@\@rule1);
(%o10)                         @@


(%i11) remrule (quux, all);
(%o11)                        quux


(%i12) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
        quux (%e, %pi)];
(%o12) [foo(aa, bb), bb + aa, aa @@ bb, quux(%pi, %e), 
                                                   quux(%e, %pi)]
```

See also: `remlet`, `let`.

### Function: resimplify (expr)

Resimplifies the expression *expr* based on the current environment.  This
function is useful when the fact database, option variables, or tellsimp rules
have changed since the expression was last simplified.


Example:










```maxima
maxima

(%i1) expr : sin(x)^2 + cos(x)^2;
                           2         2
(%o1)                   sin (x) + cos (x)


(%i2) exponentialize : true;
(%o2)                         true


(%i3) expr;
                           2         2
(%o3)                   sin (x) + cos (x)


(%i4) resimplify(%);
              %i x     - %i x 2      %i x     - %i x 2
           (%e     + %e      )    (%e     - %e      )
(%o4)      -------------------- - --------------------
                    4                      4


(%i5) ratsimp(%);
(%o5)                           1
```

### Function: scsimp (expr, rule_1, ..., rule_n)

Sequential Comparative Simplification (method due to Stoute).
`scsimp` attempts to simplify *expr*
according to the rules *rule_1*, ..., *rule_n*.
If a smaller expression is obtained, the process repeats.  Otherwise after all
simplifications are tried, it returns the original answer.



`example (scsimp)` displays some examples.

### Variable: simp

Default value: `true`


`simp` enables simplification.  This is the default.  `simp` is also
an `evflag`, which is recognized by the function `ev`.  See `ev`.


When `simp` is used as an `evflag` with a value `false`, the 
simplification is suppressed only during the evaluation phase of an expression.
The flag does not suppress the simplification which follows the evaluation 
phase.


Many Maxima functions and operations require simplification to be enabled to work normally.
When simplification is disabled, many results will be incomplete,
and in addition there may be incorrect results or program errors.


Examples:


The simplification is switched off globally.  The expression `sin(1.0)` is
not simplified to its numerical value.  The `simp`-flag switches the
simplification on.








```maxima
maxima

(%i1) simp:false;
(%o1)                         false


(%i2) sin(1.0);
(%o2)                       sin(1.0)


(%i3) sin(1.0),simp;
(%o3)                  0.8414709848078965
```


The simplification is switched on again.  The `simp`-flag cannot suppress
the simplification completely.  The output shows a simplified expression, but
the variable `x` has an unsimplified expression as a value, because the
assignment has occurred during the evaluation phase of the expression.








```maxima
maxima

(%i1) simp:true;
(%o1)                         true


(%i2) x:sin(1.0),simp:false;
(%o2)                  0.8414709848078965


(%i3) :lisp $x
((%SIN) 1.0)
```

See also: `ev`.

### Variable: symmetric

`declare (h, symmetric)` tells the Maxima
simplifier that `h` is a symmetric function.  E.g., `h (x, z, y)` 
simplifies to `h (x, y, z)`.


`commutative` is synonymous with `symmetric`.

See also: `commutative`.

### Function: tellsimp (pattern, replacement)

is similar to `tellsimpafter` but places
new information before old so that it is applied before the built-in
simplification rules.


`tellsimp` is used when it is important to modify
the expression before the simplifier works on it, for instance if the
simplifier "knows" something about the expression, but what it returns
is not to your liking.
If the simplifier "knows" something about the
main operator of the expression, but is simply not doing enough for
you, you probably want to use `tellsimpafter`.


The pattern may not be a
sum, product, single variable, or number.


The system variable `rules` is the list of rules defined by
`defrule`, `defmatch`, `tellsimp`, and `tellsimpafter`.


Examples:






















```maxima
maxima

(%i1) matchdeclare (x, freeof (%i));
(%o1)                         done

(%i2) %iargs: false$

(%i3) tellsimp (sin(%i*x), %i*sinh(x));
(%o3)                 [sinrule1, simp-%sin]


(%i4) trigexpand (sin (%i*y + x));
(%o4)         sin(x) cos(%i y) + %i cos(x) sinh(y)

(%i5) %iargs:true$

(%i6) errcatch(0^0);
                  0
expt: undefined: 0
(%o6)                          []


(%i7) ev (tellsimp (0^0, 1), simp: false);
(%o7)                  [^rule1, simpexpt]


(%i8) 0^0;
(%o8)                           1


(%i9) remrule ("^", %th(2)[1]);
(%o9)                           ^


(%i10) tellsimp (sin(x)^2, 1 - cos(x)^2);
(%o10)                 [^rule2, simpexpt]


(%i11) (1 + sin(x))^2;
                                      2
(%o11)                    (sin(x) + 1)


(%i12) expand (%);
                                   2
(%o12)               2 sin(x) - cos (x) + 2


(%i13) sin(x)^2;
                                  2
(%o13)                     1 - cos (x)


(%i14) kill (rules);
(%o14)                        done


(%i15) matchdeclare (a, true);
(%o15)                        done


(%i16) tellsimp (sin(a)^2, 1 - cos(a)^2);
(%o16)                 [^rule3, simpexpt]


(%i17) sin(y)^2;
                                  2
(%o17)                     1 - cos (y)
```

### Function: tellsimpafter (pattern, replacement)

Defines a simplification rule which the Maxima simplifier applies after built-in
simplification rules.  *pattern* is an expression, comprising pattern
variables (declared by `matchdeclare`) and other atoms and operators,
considered literals for the purpose of pattern matching.  *replacement* is
substituted for an actual expression which matches *pattern*; pattern
variables in *replacement* are assigned the values matched in the actual
expression.


*pattern* may be any nonatomic expression in which the main operator is not
a pattern variable; the simplification rule is associated with the main
operator.  The names of functions (with one exception, described below), lists,
and arrays may appear in *pattern* as the main operator only as literals
(not pattern variables); this rules out expressions such as `aa(x)` and
`bb[y]` as patterns, if `aa` and `bb` are pattern variables.
Names of functions, lists, and arrays which are pattern variables may appear as
operators other than the main operator in *pattern*.


There is one exception to the above rule concerning names of functions.
The name of a subscripted function in an expression such as `aa[x](y)`
may be a pattern variable, because the main operator is not `aa` but rather
the Lisp atom `mqapply`.  This is a consequence of the representation of
expressions involving subscripted functions.










Simplification rules are applied after evaluation 
(if not suppressed through quotation or the flag `noeval`).
Rules established by `tellsimpafter` are applied in the order they were
defined, and after any built-in rules.
Rules are applied bottom-up, that is,
applied first to subexpressions before application to the whole expression.


It may be necessary to repeatedly simplify a result (for example, via the
quote-quote operator `''` or the flag `infeval`)
to ensure that all rules are applied.


Pattern variables are treated as local variables in simplification rules.
Once a rule is defined, the value of a pattern variable
does not affect the rule, and is not affected by the rule.
An assignment to a pattern variable which results from a successful rule match
does not affect the current assignment (or lack of it) of the pattern variable.
However, as with all atoms in Maxima, the properties of pattern variables (as
declared by `put` and related functions) are global.


The rule constructed by `tellsimpafter` is named after the main operator of
*pattern*.  Rules for built-in operators, and user-defined operators defined
by `infix`, `prefix`, `postfix`, `matchfix`, and
`nofix`, have names which are Lisp identifiers.


Rules for other functions have names which are Maxima identifiers.




The treatment of noun and verb forms is slightly confused.  
If a rule is defined for a noun (or verb) form
and a rule for the corresponding verb (or noun) form already exists, 
the newly-defined rule applies to both forms (noun and verb).
If a rule for the corresponding verb (or noun) form does not exist,
the newly-defined rule applies only to the noun (or verb) form.


The rule constructed by `tellsimpafter` is an ordinary Lisp function.
If the name of the rule is `$foorule1`,
the construct `:lisp (trace $foorule1)` traces the function,
and `:lisp (symbol-function '$foorule1)` displays its definition.


`tellsimpafter` quotes its arguments.
`tellsimpafter` returns the list of rules for the main operator of
*pattern*, including the newly established rule.



See also `matchdeclare`, `defmatch`, `defrule`, `tellsimp`,
`let`, `kill`, `remrule` and `clear_005frules`.


Examples:


*pattern* may be any nonatomic expression in which the 
main operator is not a pattern variable.












```maxima
maxima
(%i1) matchdeclare (aa, atom, [ll, mm], listp, xx, true)$

(%i2) tellsimpafter (sin (ll), map (sin, ll));
(%o2)                 [sinrule1, simp-%sin]


(%i3) sin ([1/6, 1/4, 1/3, 1/2, 1]*%pi);
                    1     1     sqrt(3)
(%o3)              [-, -------, -------, 1, 0]
                    2  sqrt(2)     2


(%i4) tellsimpafter (ll^mm, map ("^", ll, mm));
(%o4)                  [^rule1, simpexpt]


(%i5) [a, b, c]^[1, 2, 3];
                                2   3
(%o5)                      [a, b , c ]


(%i6) tellsimpafter (foo (aa (xx)), aa (foo (xx)));
(%o6)                   [foorule1, false]


(%i7) foo (bar (u - v));
(%o7)                    bar(foo(u - v))
```


Rules are applied in the order they were defined.
If two rules can match an expression,
the rule which was defined first is applied.









```maxima
maxima

(%i1) matchdeclare (aa, integerp);
(%o1)                         done


(%i2) tellsimpafter (foo (aa), bar_1 (aa));
(%o2)                   [foorule1, false]


(%i3) tellsimpafter (foo (aa), bar_2 (aa));
(%o3)              [foorule2, foorule1, false]


(%i4) foo (42);
(%o4)                       bar_1(42)
```


Pattern variables are treated as local variables in simplification rules.
(Compare to `defmatch`, which treats pattern variables as global
variables.)










```maxima
maxima

(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done


(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]


(%i3) bb: 12345;
(%o3)                         12345


(%i4) foo (42, %e);
(%o4)                 bar(aa = 42, bb = %e)


(%i5) bb;
(%o5)                         12345
```


As with all atoms, properties of pattern variables are global even though values
are local.  In this example, an assignment property is declared via
`define_variable`.  This is a property of the atom `bb` throughout
Maxima.









translator: bb was declared with mode boolean, but it has value: 
                                                               %e
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done


(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]


(%i3) foo (42, %e);
(%o3)                 bar(aa = 42, bb = %e)


(%i4) define_variable (bb, true, boolean);
(%o4)                         true

(%i5) foo (42, %e);
```


Rules are named after main operators.
Names of rules for built-in and user-defined operators are Lisp identifiers,
while names for other functions are Maxima identifiers.

















```maxima
maxima

(%i1) tellsimpafter (foo (%pi + %e), 3*%pi);
(%o1)                   [foorule1, false]


(%i2) tellsimpafter (foo (%pi * %e), 17*%e);
(%o2)              [foorule2, foorule1, false]


(%i3) tellsimpafter (foo (%i ^ %e), -42*%i);
(%o3)         [foorule3, foorule2, foorule1, false]


(%i4) tellsimpafter (foo (9) + foo (13), quux (22));
(%o4)                   [+rule1, simplus]


(%i5) tellsimpafter (foo (9) * foo (13), blurf (22));
(%o5)                  [*rule1, simptimes]


(%i6) tellsimpafter (foo (9) ^ foo (13), mumble (22));
(%o6)                  [^rule1, simpexpt]


(%i7) rules;
(%o7) [foorule1, foorule2, foorule3, +rule1, *rule1, ^rule1]


(%i8) foorule_name: first (%o1);
(%o8)                       foorule1


(%i9) plusrule_name: first (%o4);
(%o9)                        +rule1


(%i10) remrule (foo, foorule1);
(%o10)                         foo


(%i11) remrule ("^", ?\^rule1);
(%o11)                          ^


(%i12) rules;
(%o12)        [foorule2, foorule3, +rule1, *rule1]
```


A worked example: anticommutative multiplication.












```maxima
maxima

(%i1) gt (i, j) := integerp(j) and i < j;
(%o1)          gt(i, j) := integerp(j) and (i < j)


(%i2) matchdeclare (i, integerp, j, gt(i));
(%o2)                         done


(%i3) tellsimpafter (s[i]^^2, 1);
(%o3)                 [^^rule1, simpncexpt]


(%i4) tellsimpafter (s[i] . s[j], -s[j] . s[i]);
(%o4)                   [.rule1, simpnct]


(%i5) s[1] . (s[1] + s[2]);
(%o5)                    s  . (s  + s )
                          1     2    1


(%i6) expand (%);
(%o6)                      1 - s  . s
                                2    1


(%i7) factor (expand (sum (s[i], i, 0, 9)^^5));
(%o7) 100 (s  + s  + s  + s  + s  + s  + s  + s  + s  + s )
            9    8    7    6    5    4    3    2    1    0
```

See also: `matchdeclare`, `defmatch`, `defrule`, `tellsimp`, `let`, `kill`, `remrule`, `clear_rules`.

### Function: xthru (expr)

Combines all terms of *expr* (which should be a sum) over a common
denominator without expanding products and exponentiated sums as `ratsimp`
does.  `xthru` cancels common factors in the numerator and denominator of
rational expressions but only if the factors are explicit.



Sometimes it is better to use `xthru` before `ratsimp`ing an
expression in order to cause explicit factors of the gcd of the numerator and
denominator to be canceled thus simplifying the expression to be
`ratsimp`ed.


Examples:







```maxima
maxima

(%i1) ((x+2)^20 - 2*y)/(x+y)^20 + (x+y)^(-19) - x/(x+y)^20;
                                20
                 1       (x + 2)   - 2 y       x
(%o1)        --------- + --------------- - ---------
                    19             20             20
             (y + x)        (y + x)        (y + x)


(%i2) xthru (%);
                                 20
                          (x + 2)   - y
(%o2)                     -------------
                                   20
                            (y + x)
```

