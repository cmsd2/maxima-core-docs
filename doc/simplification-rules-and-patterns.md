## Rules and Patterns

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

