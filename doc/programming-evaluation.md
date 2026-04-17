## Evaluation

<!-- category: Programming -->
<!-- keywords: ' -->
<!-- signatures: ' -->
### Function: '

The single quote operator `'` prevents evaluation.


Applied to a symbol, the single quote prevents evaluation of the symbol.


Applied to a function call, the single quote prevents evaluation of the function
call, although the arguments of the function are still evaluated (if evaluation
is not otherwise prevented).  The result is the noun form of the function call.


Applied to a parenthesized expression, the single quote prevents evaluation of
all symbols and function calls in the expression.

E.g., `'(f(x))` means do not evaluate the expression `f(x)`.
`'f(x)` (with the single quote applied to `f` instead of `f(x)`)
means return the noun form of `f` applied to `[x]`.


The single quote does not prevent simplification.


When the global flag `noundisp` is `true`, nouns display with a single
quote.  This switch is always `true` when displaying function definitions.


See also the quote-quote operator `quote_002dquote` and `nouns`.


Examples:


Applied to a symbol,
the single quote prevents evaluation of the symbol.









```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) aa^2;
(%o2)                        1048576
(%i3) 'aa^2;
                                 2
(%o3)                          aa
(%i4) ''%;
(%o4)                        1048576
```


Applied to a function call, the single quote prevents evaluation of the function
call.  The result is the noun form of the function call.










```maxima
(%i1) x0: 5;
(%o1)                           5
(%i2) x1: 7;
(%o2)                           7
(%i3) integrate (x^2, x, x0, x1);
                               218
(%o3)                          ---
                                3
(%i4) 'integrate (x^2, x, x0, x1);

                             7
                            /
                            [   2
(%o4)                       I  x  dx
                            ]
                            /
                             5

(%i5) %, nouns;
                               218
(%o5)                          ---
                                3
```


Applied to a parenthesized expression, the single quote prevents evaluation of
all symbols and function calls in the expression.










```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) bb: 19;
(%o2)                          19
(%i3) sqrt(aa) + bb;
(%o3)                          51
(%i4) '(sqrt(aa) + bb);
(%o4)                     bb + sqrt(aa)
(%i5) ''%;
(%o5)                          51
```


The single quote does not prevent simplification.







```maxima
(%i1) sin (17 * %pi) + cos (17 * %pi);
(%o1)                          - 1
(%i2) '(sin (17 * %pi) + cos (17 * %pi));
(%o2)                          - 1
```


Maxima considers floating point operations by its in-built mathematical
functions to be a simplification.







```maxima
(%i1) sin(1.0);
(%o1)                          .8414709848078965
(%i2) '(sin(1.0));
(%o2)                          .8414709848078965
```


When the global flag `noundisp` is `true`, nouns display with a single
quote.


















```maxima
(%i1) x:%pi;
(%o1)                                 %pi
(%i2) bfloat(x);
(%o2)                         3.141592653589793b0
(%i3) sin(x);
(%o3)                                  0
(%i4) noundisp;
(%o4)                                false
(%i5) 'bfloat(x);
(%o5)                             bfloat(%pi)
(%i6) bfloat('x);
(%o6)                                  x
(%i7) 'sin(x);
(%o7)                                  0
(%i8) sin('x);
(%o8)                               sin(x)
(%i9) noundisp : not noundisp;
(%o9)                                true
(%i10) 'bfloat(x);
(%o10)                           'bfloat(%pi)
(%i11) bfloat('x);
(%o11)                                 x
(%i12) 'sin(x);
(%o12)                                 0
(%i13) sin('x);
(%o13)                              sin(x)
(%i14)
```

See also: `noundisp`, `quote-quote`, `nouns`.

<!-- category: Programming -->
<!-- keywords: '' -->
<!-- signatures: '' -->
### Function: ''

The quote-quote operator `''` (two single quote marks) modifies
evaluation in input expressions.


Applied to a general expression *expr*, quote-quote causes the value of
*expr* to be substituted for *expr* in the input expression.


Applied to the operator of an expression, quote-quote changes the operator from
a noun to a verb (if it is not already a verb).


The quote-quote operator is applied by the input parser; it is not stored as
part of a parsed input expression.  The quote-quote operator is always applied
as soon as it is parsed, and cannot be quoted.  Thus quote-quote causes
evaluation when evaluation is otherwise suppressed, such as in function
definitions, lambda expressions, and expressions quoted by single quote
`'`.


Quote-quote is recognized by `batch` and `load`.


See also `ev`, the single-quote operator `quote` and `nouns`.


Examples:


Applied to a general expression *expr*, quote-quote causes the value of
*expr* to be substituted for *expr* in the input expression.



















```maxima
(%i1) expand ((a + b)^3);
                     3        2      2      3
(%o1)               b  + 3 a b  + 3 a  b + a
(%i2) [_, ''_];
                         3    3        2      2      3
(%o2)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i3) [%i1, ''%i1];
                         3    3        2      2      3
(%o3)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i4) [aa : cc, bb : dd, cc : 17, dd : 29];
(%o4)                   [cc, dd, 17, 29]
(%i5) foo_1 (x) := aa - bb * x;
(%o5)                 foo_1(x) := aa - bb x
(%i6) foo_1 (10);
(%o6)                      cc - 10 dd
(%i7) ''%;
(%o7)                         - 273
(%i8) ''(foo_1 (10));
(%o8)                         - 273
(%i9) foo_2 (x) := ''aa - ''bb * x;
(%o9)                 foo_2(x) := cc - dd x
(%i10) foo_2 (10);
(%o10)                        - 273
(%i11) [x0 : x1, x1 : x2, x2 : x3];
(%o11)                    [x1, x2, x3]
(%i12) x0;
(%o12)                         x1
(%i13) ''x0;
(%o13)                         x2
(%i14) '' ''x0;
(%o14)                         x3
```


Applied to the operator of an expression, quote-quote changes the operator from
a noun to a verb (if it is not already a verb).









```maxima
(%i1) declare (foo, noun);
(%o1)                         done
(%i2) foo (x) := x - 1729;
(%o2)                 ''foo(x) := x - 1729
(%i3) foo (100);
(%o3)                       foo(100)
(%i4) ''foo (100);
(%o4)                        - 1629
```


The quote-quote operator is applied by the input parser; it is not stored as
part of a parsed input expression.










```maxima
(%i1) [aa : bb, cc : dd, bb : 1234, dd : 5678];
(%o1)                 [bb, dd, 1234, 5678]
(%i2) aa + cc;
(%o2)                        dd + bb
(%i3) display (_, op (_), args (_));
                           _ = cc + aa

                         op(cc + aa) = +

                    args(cc + aa) = [cc, aa]

(%o3)                         done
(%i4) ''(aa + cc);
(%o4)                         6912
(%i5) display (_, op (_), args (_));
                           _ = dd + bb

                         op(dd + bb) = +

                    args(dd + bb) = [dd, bb]

(%o5)                         done
```


Quote-quote causes evaluation when evaluation is otherwise suppressed, such as
in function definitions, lambda expressions, and expressions quoted by single
quote `'`.
















```maxima
(%i1) foo_1a (x) := ''(integrate (log (x), x));
(%o1)               foo_1a(x) := x log(x) - x
(%i2) foo_1b (x) := integrate (log (x), x);
(%o2)           foo_1b(x) := integrate(log(x), x)
(%i3) dispfun (foo_1a, foo_1b);
(%t3)               foo_1a(x) := x log(x) - x

(%t4)           foo_1b(x) := integrate(log(x), x)

(%o4)                      [%t3, %t4]
(%i5) integrate (log (x), x);
(%o5)                     x log(x) - x
(%i6) foo_2a (x) := ''%;
(%o6)               foo_2a(x) := x log(x) - x
(%i7) foo_2b (x) := %;
(%o7)                    foo_2b(x) := %
(%i8) dispfun (foo_2a, foo_2b);
(%t8)               foo_2a(x) := x log(x) - x

(%t9)                    foo_2b(x) := %

(%o9)                      [%t7, %t8]
(%i10) F : lambda ([u], diff (sin (u), u));
(%o10)             lambda([u], diff(sin(u), u))
(%i11) G : lambda ([u], ''(diff (sin (u), u)));
(%o11)                  lambda([u], cos(u))
(%i12) '(sum (a[k], k, 1, 3) + sum (b[k], k, 1, 3));
(%o12)         sum(b , k, 1, 3) + sum(a , k, 1, 3)
                    k                  k
(%i13) '(''(sum (a[k], k, 1, 3)) + ''(sum (b[k], k, 1, 3)));
(%o13)             b  + a  + b  + a  + b  + a
                    3    3    2    2    1    1
```

See also: `batch`, `load`, `ev`, `quote`, `nouns`.

<!-- category: Programming -->
<!-- keywords: ev -->
<!-- signatures: ev(expr, arg_1, ..., arg_n) -->
### Function: ev (expr, arg_1, ..., arg_n)

Evaluates the expression *expr* in the environment specified by the
arguments *arg_1*, ..., *arg_n*.  The arguments are switches
(Boolean flags), assignments, equations, and functions.  `ev` returns the
result (another expression) of the evaluation.


The evaluation is carried out in steps, as follows.



1. First the environment is set up by scanning the arguments which may
be any or all of the following.



  - *
`simp` causes *expr* to be simplified regardless of the setting of the
switch `simp` which inhibits simplification if `false`.
  - *
`noeval` suppresses the evaluation phase of `ev` (see step (4) below).
This is useful in conjunction with the other switches and in causing
*expr* to be resimplified without being reevaluated.
  - *
`nouns` causes the evaluation of noun forms (typically unevaluated
functions such as `'integrate` or `'diff`) in *expr*.
  - *
`expand` causes expansion.
  - *
`expand (m, n)` causes expansion, setting the values of
`maxposex` and `maxnegex` to *m* and *n* respectively.
  - *
`detout` causes any matrix inverses computed in *expr* to have their
determinant kept outside of the inverse rather than dividing through
each element.
  - *
`diff` causes all differentiations indicated in *expr* to be performed.
  - *
`derivlist (x, y, z, ...)` causes only differentiations
with respect to the indicated variables.  See also `derivlist`.
  - *
`risch` causes integrals in *expr* to be evaluated using the Risch
algorithm.  See `risch`.  The standard integration routine is invoked
when using the special symbol `nouns`.
  - *
`float` causes non-integral rational numbers to be converted to floating
point.
  - *
`numer` causes some mathematical functions (including exponentiation)
with numerical arguments to be evaluated in floating point.  It causes
variables in *expr* which have been given numervals to be replaced by
their values.  It also sets the `float` switch on.
  - *
`pred` causes predicates (expressions which evaluate to `true` or
`false`) to be evaluated.
  - *
`eval` causes an extra post-evaluation of *expr* to occur.
(See step (5) below.)
`eval` may occur multiple times.  For each instance of `eval`, the
expression is evaluated again.
  - *
`A` where `A` is an atom declared to be an evaluation flag
`evflag` causes `A` to be bound to `true` during the evaluation
of *expr*.
  - *
`V: expression` (or alternately `V=expression`) causes `V` to be
bound to the value of `expression` during the evaluation of *expr*.
Note that if `V` is a Maxima option, then `expression` is used for
its value during the evaluation of *expr*.  If more than one argument to
`ev` is of this type then the binding is done in parallel.  If `V` is
a non-atomic expression then a substitution rather than a binding is performed.
  - *
`F` where `F`, a function name, has been declared to be an evaluation
function `evfun` causes `F` to be applied to *expr*.
  - *
Any other function names, e.g. `sum`, cause evaluation of occurrences
of those names in *expr* as though they were verbs.
  - *
In addition a function occurring in *expr* (say `F(x)`) may be defined
locally for the purpose of this evaluation of *expr* by giving
`F(x) := expression` as an argument to `ev`.
  - *
If an atom not mentioned above or a subscripted variable or subscripted
expression was given as an argument, it is evaluated and if the result is an
equation or assignment then the indicated binding or substitution is performed.
If the result is a list then the members of the list are treated as if they were
additional arguments given to `ev`.  This permits a list of equations to be
given (e.g. `[X=1, Y=A**2]`) or a list of names of equations (e.g.,
`[%t1, %t2]` where `%t1` and `%t2` are equations) such as that
returned by `solve`.


The arguments of `ev` may be given in any order with the exception of
substitution equations which are handled in sequence, left to right, and
evaluation functions which are composed, e.g., `ev (expr, ratsimp, realpart)` is handled as `realpart (ratsimp (expr))`.


The `simp`, `numer`, and `float` switches may also be set
locally in a block, or globally in Maxima so that they will remain in effect
until being reset.


If *expr* is a canonical rational expression (CRE), then the expression
returned by `ev` is also a CRE, provided the `numer` and `float`
switches are not both `true`.
2. During step (1), a list is made of the non-subscripted variables appearing on
the left side of equations in the arguments or in the value of some arguments
if the value is an equation.  The variables (subscripted variables which do not
have associated `memoizing functions` as well as non-subscripted variables) in the
expression *expr* are replaced by their global values, except for those
appearing in this list.  Usually, *expr* is just a label or `%` (as in
`%i2` in the example below), so this step simply retrieves the expression
named by the label, so that `ev` may work on it.
3. If any substitutions are indicated by the arguments, they are carried out now.
4. The resulting expression is then re-evaluated (unless one of the arguments was
`noeval`) and simplified according to the arguments.  Note that any
function calls in *expr* will be carried out after the variables in it are
evaluated and that `ev(F(x))` thus may behave like `F(ev(x))`.
5. For each instance of `eval` in the arguments, steps (3) and (4) are
repeated.


See also `quote_002dquote`, `at` and `subst`.


Examples:







```maxima
(%i1) sin(x) + cos(y) + (w+1)^2 + 'diff (sin(w), w);
                                     d                    2
(%o1)              cos(y) + sin(x) + -- (sin(w)) + (w + 1)
                                     dw
(%i2) ev (%, numer, expand, diff, x=2, y=1);
                               2
(%o2)                cos(w) + w  + 2 w + 2.449599732693821
```


An alternate top level syntax has been provided for `ev`, whereby one
may just type in its arguments, without the `ev()`.  That is, one may
write simply



```maxima
expr, arg_1, ..., arg_n
```


This is not permitted as part of another expression, e.g., in functions,
blocks, etc.


Notice the parallel binding process in the following example.



```maxima
(%i3) programmode: false;
(%o3)                                false
(%i4) x+y, x: a+y, y: 2;
(%o4)                              y + a + 2
(%i5) 2*x - 3*y = 3$
(%i6) -3*x + 2*y = -4$
(%i7) solve ([%o5, %o6]);
Solution

                                          1
(%t7)                               y = - -
                                          5

                                         6
(%t8)                                x = -
                                         5
(%o8)                            [[%t7, %t8]]
(%i8) %o6, %o8;
(%o8)                              - 4 = - 4
(%i9) x + 1/x > gamma (1/2);
                                   1
(%o9)                          x + - > sqrt(%pi)
                                   x
(%i10) %, numer, x=1/2;
(%o10)                      2.5 > 1.772453850905516
(%i11) %, pred;
(%o11)                               true
```

See also: `simp`, `noeval`, `nouns`, `expand`, `maxposex`, `maxnegex`, `detout`, `diff`, `derivlist`, `risch`, `float`, `numer`, `pred`, `eval`, `evflag`, `evfun`, `sum`, `solve`, `memoizing-functions`, `quote-quote`, `at`, `subst`.

<!-- category: Programming -->
<!-- keywords: eval -->
<!-- signatures: eval -->
### Variable: eval

As an argument in a call to `ev (expr)`, `eval` causes an extra
evaluation of *expr*.  See `ev`.


Example:










```maxima
(%i1) [a:b,b:c,c:d,d:e];
(%o1)                            [b, c, d, e]
(%i2) a;
(%o2)                                  b
(%i3) ev(a);
(%o3)                                  c
(%i4) ev(a),eval;
(%o4)                                  e
(%i5) a,eval,eval;
(%o5)                                  e
```

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: evflag -->
<!-- signatures: evflag -->
### Variable: evflag

When a symbol *x* has the `evflag` property, the expressions
`ev(expr, x)` and `expr, x` (at the
interactive prompt) are equivalent to `ev(expr, x = true)`.
That is, *x* is bound to `true` while *expr* is evaluated.


The expression `declare(x, evflag)` gives the `evflag` property
to the variable *x*.


The flags which have the `evflag` property by default are the following:





   algebraic          cauchysum       demoivre
   dotscrules         %emode          %enumer
   exponentialize     exptisolate     factorflag
   float              halfangles      infeval
   isolate_wrt_times  keepfloat       letrat
   listarith          logabs          logarc 
   logexpand          lognegint       
   m1pbranch          numer_pbranch   programmode 
   radexpand          ratalgdenom     ratfac 
   ratmx              ratsimpexpons   simp 
   simpproduct        simpsum         sumexpand
   trigexpand


Examples:

















```maxima
(%i1) sin (1/2);
                                 1
(%o1)                        sin(-)
                                 2
(%i2) sin (1/2), float;
(%o2)                   0.479425538604203
(%i3) sin (1/2), float=true;
(%o3)                   0.479425538604203
(%i4) simp : false;
(%o4)                         false
(%i5) 1 + 1;
(%o5)                         1 + 1
(%i6) 1 + 1, simp;
(%o6)                           2
(%i7) simp : true;
(%o7)                         true
(%i8) sum (1/k^2, k, 1, inf);
                            inf
                            ====
                            \     1
(%o8)                        >    --
                            /      2
                            ====  k
                            k = 1
(%i9) sum (1/k^2, k, 1, inf), simpsum;
                                 2
                              %pi
(%o9)                         ----
                               6
(%i10) declare (aa, evflag);
(%o10)                        done
(%i11) if aa = true then YES else NO;
(%o11)                         NO
(%i12) if aa = true then YES else NO, aa;
(%o12)                         YES
```

<!-- category: Programming -->
<!-- keywords: evfun -->
<!-- signatures: evfun -->
### Variable: evfun

When a function *F* has the `evfun` property, the expressions
`ev(expr, F)` and `expr, F` (at the
interactive prompt) are equivalent to `F(ev(expr))`.


If two or more `evfun` functions *F*, *G*, etc., are specified,
the functions are applied in the order that they are specified.


The expression `declare(F, evfun)` gives the `evfun` property
to the function *F*.  The functions which have the `evfun` property by
default are the following:





   bfloat          factor       fullratsimp
   logcontract     polarform    radcan
   ratexpand       ratsimp      rectform
   rootscontract   trigexpand   trigreduce


Examples:




















```maxima
(%i1) x^3 - 1;
                              3
(%o1)                        x  - 1
(%i2) x^3 - 1, factor;
                                2
(%o2)                 (x - 1) (x  + x + 1)
(%i3) factor (x^3 - 1);
                                2
(%o3)                 (x - 1) (x  + x + 1)
(%i4) cos(4 * x) / sin(x)^4;

                            cos(4 x)
(%o4)                       --------
                               4
                            sin (x)

(%i5) cos(4 * x) / sin(x)^4, trigexpand;
                 4           2       2         4
              sin (x) - 6 cos (x) sin (x) + cos (x)
(%o5)         -------------------------------------
                                4
                             sin (x)
(%i6) cos(4 * x) / sin(x)^4, trigexpand, ratexpand;
                           2         4
                      6 cos (x)   cos (x)
(%o6)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i7) ratexpand (trigexpand (cos(4 * x) / sin(x)^4));
                           2         4
                      6 cos (x)   cos (x)
(%o7)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i8) declare ([F, G], evfun);
(%o8)                         done
(%i9) (aa : bb, bb : cc, cc : dd);
(%o9)                          dd
(%i10) aa;
(%o10)                         bb
(%i11) aa, F;
(%o11)                        F(cc)
(%i12) F (aa);
(%o12)                        F(bb)
(%i13) F (ev (aa));
(%o13)                        F(cc)
(%i14) aa, F, G;
(%o14)                      G(F(cc))
(%i15) G (F (ev (aa)));
(%o15)                      G(F(cc))
```

<!-- category: Programming -->
<!-- keywords: infeval -->
<!-- signatures: infeval -->
### Variable: infeval

Enables "infinite evaluation" mode.  `ev` repeatedly evaluates an
expression until it stops changing.  To prevent a variable, say `X`, from
being evaluated away in this mode, simply include `X='X` as an argument to
`ev`.  Of course expressions such as `ev (X, X=X+1, infeval)` will
generate an infinite loop.

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: noeval -->
<!-- signatures: noeval -->
### Variable: noeval

`noeval` suppresses the evaluation phase of `ev`.  This is useful in
conjunction with other switches and in causing expressions      
to be resimplified without being reevaluated.

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: nouns -->
<!-- signatures: nouns -->
### Variable: nouns

`nouns` is an `evflag`.  When used as an option to the `ev`
command, `nouns` converts all "noun" forms occurring in the expression
being `ev`’d to "verbs", i.e., evaluates them.  See also
`noun`, `nounify`, `verb`, and `verbify`.

See also: `evflag`, `ev`, `noun`, `nounify`, `verbify`.

<!-- category: Programming -->
<!-- keywords: pred -->
<!-- signatures: pred -->
### Variable: pred

As an argument in a call to `ev (expr)`, `pred` causes 
predicates (expressions which evaluate to `true` or `false`) to be 
evaluated.  See `ev`.


Example:







```maxima
(%i1) 1<2;
(%o1)                                1 < 2
(%i2) 1<2,pred;
(%o2)                                true
```

See also: `ev`.

