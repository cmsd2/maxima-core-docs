## Expressions

<!-- category: Programming -->
<!-- keywords: alias -->
<!-- signatures: alias(new_name_1, old_name_1, ..., new_name_n, old_name_n) -->
### Function: alias (new_name_1, old_name_1, ..., new_name_n, old_name_n)

provides an alternate name for a (user or system) function, variable, array,
etc.  Any even number of arguments may be used.

<!-- category: Programming -->
<!-- keywords: aliases -->
<!-- signatures: aliases -->
### Variable: aliases

Default value: `[]`


`aliases` is the list of atoms which have a user defined alias (set up by
the `alias`, `ordergreat`, `orderless` functions or by
declaring the atom a `noun` with `declare`.)

See also: `alias`, `ordergreat`, `orderless`, `noun`, `declare`.

<!-- category: Programming -->
<!-- keywords: allbut -->
<!-- signatures: allbut -->
### Variable: allbut

works with the `part` commands (i.e.  `part`,
`inpart`, `substpart`, `substinpart`,
`dpart`, and `lpart`).
For example,







```maxima
maxima

(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a


(%i2) part (expr, [2, 5]);
(%o2)                         d + a
```


while







```maxima
maxima

(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a


(%i2) part (expr, allbut (2, 5));
(%o2)                       e + c + b
```


`allbut` is also recognized by `kill`.








```maxima
maxima

(%i1) [aa : 11, bb : 22, cc : 33, dd : 44, ee : 55];
(%o1)                 [11, 22, 33, 44, 55]


(%i2) kill (allbut (cc, dd));
(%o0)                         done


(%i1) [aa, bb, cc, dd];
(%o1)                   [aa, bb, 33, 44]
```


`kill(allbut(a_1, a_2, ...))` has the effect of
`kill(all)` except that it does not kill the symbols *a_1*, *a_2*,
...

See also: `part`, `inpart`, `substpart`, `substinpart`, `dpart`, `lpart`, `kill`.

<!-- category: Programming -->
<!-- keywords: args -->
<!-- signatures: args(expr) -->
### Function: args (expr)

Returns the list of arguments of `expr`, which may be any kind of
expression other than an atom.  Only the arguments of the top-level operator
are extracted; subexpressions of `expr` appear as elements or
subexpressions of elements of the list of arguments.


The order of the items in the list may depend on the global flag
`inflag`.


`args (expr)` is equivalent to `substpart ("[", expr, 0)`.
See also `substpart`, `apply`, `funmake`, and `op`.


How to convert a matrix to a nested list:







```maxima
maxima

(%i1) M:matrix([1,2],[3,4]);
                            [ 1  2 ]
(%o1)                       [      ]
                            [ 3  4 ]


(%i2) args(M);
(%o2)                   [[1, 2], [3, 4]]
```


Since maxima internally treats a sum of `n` terms as a summation command
with `n` arguments args() can extract the list of terms in a sum:







```maxima
maxima

(%i1) a+b+c;
(%o1)                       c + b + a


(%i2) args(%);
(%o2)                       [c, b, a]
```

See also: `inflag`, `substpart`, `apply`, `funmake`, `op`.

<!-- category: Programming -->
<!-- keywords: atom -->
<!-- signatures: atom(expr) -->
### Function: atom (expr)

Returns `true` if *expr* is atomic (i.e. a number, name or string) else
`false`.  Thus `atom(5)` is `true` while `atom(a[1])` and
`atom(sin(x))` are `false` (assuming `a[1]` and `x` are
unbound).

<!-- category: Programming -->
<!-- keywords: box -->
<!-- signatures: box(expr), box(expr, a) -->
### Function: box (expr)

Returns *expr* enclosed in a box.  The return value is an expression with
`box` as the operator and *expr* as the argument.  A box is drawn on
the display when `display2d` is `true`.


`box (expr, a)` encloses *expr* in a box labelled by the
symbol *a*.  The label is truncated if it is longer than the width of the
box.


`box` evaluates its argument.  However, a boxed expression does not
evaluate to its content, so boxed expressions are effectively excluded from
computations. `rembox` removes the box again.


`boxchar` is the character used to draw the box in `box` and in the
`dpart` and `lpart` functions.


See also `rembox`, `dpart`, `lpart`, and `display_005fbox_005fdouble_005flines`.


Examples:













```maxima
maxima

(%i1) box (a^2 + b^2);
                            """""""""
                            " 2    2"
(%o1)                       "b  + a "
                            """""""""


(%i2) a : 1234;
(%o2)                         1234


(%i3) b : c - d;
(%o3)                         c - d


(%i4) box (a^2 + b^2);
                      """"""""""""""""""""
                      "       2          "
(%o4)                 "(c - d)  + 1522756"
                      """"""""""""""""""""


(%i5) box (a^2 + b^2, term_1);
                      term_1""""""""""""""
                      "       2          "
(%o5)                 "(c - d)  + 1522756"
                      """"""""""""""""""""


(%i6) 1729 - box (1729);
                                 """"""
(%o6)                     1729 - "1729"
                                 """"""


(%i7) boxchar: "-";
(%o7)                           -


(%i8) box (sin(x) + cos(y));
                        -----------------
(%o8)                   -cos(y) + sin(x)-
                        -----------------
```

See also: `display2d`, `rembox`, `boxchar`, `dpart`, `lpart`, `display_box_double_lines`.

<!-- category: Programming -->
<!-- keywords: boxchar -->
<!-- signatures: boxchar -->
### Variable: boxchar

Default value: `"`


`boxchar` is the character used to draw the box in the `box`
and in the `dpart` and `lpart` functions.


`boxchar` is only used when `display2d_unicode` is `false`.


All boxes in an expression are drawn with the current value of `boxchar`;
the drawing character is not stored with the box expression.

See also: `box`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: collapse -->
<!-- signatures: collapse(expr) -->
### Function: collapse (expr)

Collapses *expr* by causing all of its common (i.e., equal) subexpressions
to share (i.e., use the same cells), thereby saving space.  (`collapse` is
a subroutine used by the `optimize` command.)  Thus, calling
`collapse` may be useful after loading in a `save` file.  You can
collapse several expressions together by using
`collapse ([expr_1, ..., expr_n])`.  Similarly, you can
collapse the elements of the array `A` by doing
`collapse (listarray ('A))`.

See also: `optimize`, `save`.

<!-- category: Programming -->
<!-- keywords: copy -->
<!-- signatures: copy(e) -->
### Function: copy (e)

Return a copy of the Maxima expression *e*.  Although *e* can be any
Maxima expression, the copy function is the most useful when *e* is either 
a list or a matrix; consider:










```maxima
maxima
(%i1) m : [1,[2,3]]$
(%i2) mm : m$
(%i3) mm[2][1] : x$

(%i4) m;
(%o4)                      [1, [x, 3]]


(%i5) mm;
(%o5)                      [1, [x, 3]]
```


Let’s try the same experiment, but this time let *mm* be a copy of *m*










```maxima
maxima
(%i1) m : [1,[2,3]]$
(%i2) mm : copy(m)$
(%i3) mm[2][1] : x$

(%i4) m;
(%o4)                      [1, [2, 3]]


(%i5) mm;
(%o5)                      [1, [x, 3]]
```


This time, the assignment to *mm* does not change the value of *m*.

<!-- category: Programming -->
<!-- keywords: disolate -->
<!-- signatures: disolate(expr, x_1, ..., x_n) -->
### Function: disolate (expr, x_1, ..., x_n)

is similar to `isolate``(expr, x)` except that it enables the
user to isolate more than one variable simultaneously.  This might be useful,
for example, if one were attempting to change variables in a multiple
integration, and that variable change involved two or more of the integration
variables.  This function is autoloaded from `simplification/disol.mac`.
A demo is available by `demo("disol")$`.

See also: `isolate`.

<!-- category: Programming -->
<!-- keywords: dispform -->
<!-- signatures: dispform(expr), dispform(expr, all) -->
### Function: dispform (expr)

Returns the external representation of *expr*.


`dispform(expr)` returns the external representation with respect to
the main (top-level) operator.  `dispform(expr, all)` returns the
external representation with respect to all operators in *expr*.


See also `part`, `inpart`, and `inflag`.


Examples:


The internal representation of `- x` is "negative one times `x`"
while the external representation is "minus `x`".









```maxima
maxima

(%i1) - x;
(%o1)                          - x


(%i2) ?format (true, "~S~%", %);
((MTIMES SIMP) -1 $X)
(%o2)                         false


(%i3) dispform (- x);
(%o3)                          - x


(%i4) ?format (true, "~S~%", %);
((MMINUS SIMP) $X)
(%o4)                         false
```


The internal representation of `sqrt(x)` is "`x` to the power 1/2"
while the external representation is "square root of `x`".









```maxima
maxima

(%i1) sqrt (x);
(%o1)                        sqrt(x)


(%i2) ?format (true, "~S~%", %);
((MEXPT SIMP) $X ((RAT SIMP) 1 2))
(%o2)                         false


(%i3) dispform (sqrt (x));
(%o3)                        sqrt(x)


(%i4) ?format (true, "~S~%", %);
((%SQRT SIMP) $X)
(%o4)                         false
```


Use of the optional argument `all`.









```maxima
maxima

(%i1) expr : sin (sqrt (x));
(%o1)                     sin(sqrt(x))


(%i2) freeof (sqrt, expr);
(%o2)                         true


(%i3) freeof (sqrt, dispform (expr));
(%o3)                         true


(%i4) freeof (sqrt, dispform (expr, all));
(%o4)                         false
```

See also: `part`, `inpart`, `inflag`.

<!-- category: Programming -->
<!-- keywords: display_box_double_lines -->
<!-- signatures: display_box_double_lines -->
### Variable: display_box_double_lines

Default value: `true`


When `display_box_double_lines` is `true`,
`box` expressions are displayed with Unicode double-line characters.


When `display_box_double_lines` is `false`,
`box` expressions are displayed with Unicode single-line characters.


`display_box_double_lines` only has any effect when `display2d_unicode` is `true`.

<!-- category: Programming -->
<!-- keywords: dpart -->
<!-- signatures: dpart(expr, n_1, ..., n_k) -->
### Function: dpart (expr, n_1, ..., n_k)

Selects the same subexpression as `part`, but instead of just returning
that subexpression as its value, it returns the whole expression with the
selected subexpression displayed inside a box.  The box is actually part of the
expression.






```maxima
maxima

(%i1) dpart (x+y/z^2, 1, 2, 1);
                             y
(%o1)                       ---- + x
                               2
                            """
                            "z"
                            """
```

See also: `part`.

<!-- category: Programming -->
<!-- keywords: exptisolate -->
<!-- signatures: exptisolate -->
### Variable: exptisolate

Default value: `false`



`exptisolate`, when `true`, causes `isolate (expr, var)` to
examine exponents of atoms (such as `%e`) which contain `var`.

<!-- category: Programming -->
<!-- keywords: exptsubst -->
<!-- signatures: exptsubst -->
### Variable: exptsubst

Default value: `false`


`exptsubst`, when `true`, permits substitutions such as `y`
for `%e^x` in `%e^(a x)`.










```maxima
maxima

(%i1) %e^(a*x);
                                a x
(%o1)                         %e


(%i2) exptsubst;
(%o2)                         false


(%i3) subst(y, %e^x, %e^(a*x));
                                a x
(%o3)                         %e


(%i4) exptsubst: not exptsubst;
(%o4)                         true


(%i5) subst(y, %e^x, %e^(a*x));
                                a
(%o5)                          y
```

<!-- category: Programming -->
<!-- keywords: freeof -->
<!-- signatures: freeof(x_1, ..., x_n, expr) -->
### Function: freeof (x_1, ..., x_n, expr)

`freeof (x_1, expr)` returns `true` if no subexpression of
*expr* is equal to *x_1* or if *x_1* occurs only as a dummy variable
in *expr*, or if *x_1* is neither the noun nor verb form of any operator
in *expr*, and returns `false` otherwise.


`freeof (x_1, ..., x_n, expr)` is equivalent to 
`freeof (x_1, expr) and ... and freeof (x_n, expr)`.


The arguments *x_1*, ..., *x_n* may be names of functions and
variables, subscripted names, operators (enclosed in double quotes), or general
expressions.  `freeof` evaluates its arguments.


`freeof` operates only on *expr* as it stands (after simplification and
evaluation) and does not attempt to determine if some equivalent expression 
would give a different result.  In particular, simplification may yield an
equivalent but different expression which comprises some different elements than
the original form of *expr*.


A variable is a dummy variable in an expression if it has no binding outside of 
the expression.  Dummy variables recognized by `freeof` are the index of a 
sum or product, the limit variable in `limit`, the integration variable
in the definite integral form of `integrate`, the original variable in
`laplace`, formal variables in `at` expressions, and arguments in
`lambda` expressions.


The indefinite form of `integrate` is *not* free of its variable of 
integration.


Examples:


Arguments are names of functions, variables, subscripted names, operators, and 
expressions.  `freeof (a, b, expr)` is equivalent to 
`freeof (a, expr) and freeof (b, expr)`.













```maxima
maxima

(%i1) expr: z^3 * cos (a[1]) * b^(c+d);
                                 d + c  3
(%o1)                   cos(a ) b      z
                             1


(%i2) freeof (z, expr);
(%o2)                         false


(%i3) freeof (cos, expr);
(%o3)                         false


(%i4) freeof (a[1], expr);
(%o4)                         false


(%i5) freeof (cos (a[1]), expr);
(%o5)                         false


(%i6) freeof (b^(c+d), expr);
(%o6)                         false


(%i7) freeof ("^", expr);
(%o7)                         false


(%i8) freeof (w, sin, a[2], sin (a[2]), b*(c+d), expr);
(%o8)                         true
```


`freeof` evaluates its arguments.








```maxima
maxima
(%i1) expr: (a+b)^5$
(%i2) c: a$

(%i3) freeof (c, expr);
(%o3)                         false
```


`freeof` does not consider equivalent expressions.
Simplification may yield an equivalent but different expression.











```maxima
maxima
(%i1) expr: (a+b)^5$

(%i2) expand (expr);
          5        4       2  3       3  2      4      5
(%o2)    b  + 5 a b  + 10 a  b  + 10 a  b  + 5 a  b + a


(%i3) freeof (a+b, %);
(%o3)                         true


(%i4) freeof (a+b, expr);
(%o4)                         false


(%i5) exp (x);
                                 x
(%o5)                          %e


(%i6) freeof (exp, exp (x));
(%o6)                         true
```


A summation or definite integral is free of its dummy variable.
An indefinite integral is not free of its variable of integration.








```maxima
maxima

(%i1) freeof (i, 'sum (f(i), i, 0, n));
(%o1)                         true


(%i2) freeof (x, 'integrate (x^2, x, 0, 1));
(%o2)                         true


(%i3) freeof (x, 'integrate (x^2, x));
(%o3)                         false
```

See also: `limit`, `integrate`, `laplace`, `at`, `lambda`.

<!-- category: Programming -->
<!-- keywords: inflag -->
<!-- signatures: inflag -->
### Variable: inflag

Default value: `false`


When `inflag` is `true`, functions for part extraction inspect the
internal form of `expr`.


Note that the simplifier re-orders expressions.  Thus `first (x + y)`
returns `x` if `inflag` is `true` and `y` if `inflag`
is `false`.  (`first (y + x)` gives the same results.)


Also, setting `inflag` to `true` and calling `part` or
`substpart` is the same as calling `inpart` or `substinpart`.


Functions affected by the setting of `inflag` are: `part`,
`substpart`, `first`, `rest`, `last`,
`length`, the `for` ... `in` construct,
`map`, `fullmap`, `maplist`, `reveal`,
`pickapart`, `args` and `op`.

See also: `part`, `substpart`, `inpart`, `substinpart`, `first`, `rest`, `last`, `length`, `for`, `map`, `fullmap`, `maplist`, `reveal`, `pickapart`, `args`, `op`.

<!-- category: Programming -->
<!-- keywords: inpart -->
<!-- signatures: inpart(expr, n_1, ..., n_k) -->
### Function: inpart (expr, n_1, ..., n_k)

is similar to `part` but works on the internal representation of the
expression rather than the displayed form and thus may be faster since no
formatting is done.  Care should be taken with respect to the order of
subexpressions in sums and products (since the order of variables in the
internal form is often different from that in the displayed form) and in dealing
with unary minus, subtraction, and division (since these operators are removed
from the expression).  `part (x+y, 0)` or `inpart (x+y, 0)` yield
`+`, though in order to refer to the operator it must be enclosed in "s.
For example `... if inpart (%o9,0) = "+" then ...`.


Examples:










```maxima
maxima

(%i1) x + y + w*z;
(%o1)                      w z + y + x


(%i2) inpart (%, 3, 2);
(%o2)                           z


(%i3) part (%th (2), 1, 2);
(%o3)                           z


(%i4) 'limit (f(x)^g(x+1), x, 0, minus);
                                  g(x + 1)
(%o4)                 limit   f(x)
                      x -> 0-


(%i5) inpart (%, 1, 2);
(%o5)                       g(x + 1)
```

See also: `part`.

<!-- category: Programming -->
<!-- keywords: isolate -->
<!-- signatures: isolate(expr, x) -->
### Function: isolate (expr, x)

Returns *expr* with subexpressions which are sums and which do not contain
*var* replaced by intermediate expression labels (these being atomic symbols
like `%t1`, `%t2`, ...).  This is often useful to avoid
unnecessary expansion of subexpressions which don’t contain the variable of
interest.  Since the intermediate labels are bound to the subexpressions they
can all be substituted back by evaluating the expression in which they occur.


`exptisolate` (default value: `false`) if `true` will cause
`isolate` to examine exponents of atoms (like `%e`) which contain
*var*.


`isolate_wrt_times` if `true`, then `isolate` will also isolate
with respect to products.  See `isolate_005fwrt_005ftimes`. See also `disolate`.



Do `example (isolate)` for examples.

See also: `exptisolate`, `isolate_wrt_times`, `disolate`.

<!-- category: Programming -->
<!-- keywords: isolate_wrt_times -->
<!-- signatures: isolate_wrt_times -->
### Variable: isolate_wrt_times

Default value: `false`


When `isolate_wrt_times` is `true`, `isolate` will also isolate
with respect to products.  E.g. compare both settings of the switch on



```maxima
(%i1) isolate_wrt_times: true$
(%i2) isolate (expand ((a+b+c)^2), c);

(%t2)                          2 a


(%t3)                          2 b

                          2            2
(%t4)                    b  + 2 a b + a

                     2
(%o4)               c  + %t3 c + %t2 c + %t4
(%i4) isolate_wrt_times: false$
(%i5) isolate (expand ((a+b+c)^2), c);
                     2
(%o5)               c  + 2 b c + 2 a c + %t4
```

<!-- category: Programming -->
<!-- keywords: lfreeof -->
<!-- signatures: lfreeof(list, expr) -->
### Function: lfreeof (list, expr)

For each member *m* of *list*, calls
`freeof (m, expr)`.  It returns `false` if any call to
`freeof` does and `true` otherwise.


Example:








```maxima
maxima

(%i1) lfreeof ([ a, x], x^2+b);
(%o1)                         false


(%i2) lfreeof ([ b, x], x^2+b);
(%o2)                         false


(%i3) lfreeof ([ a, y], x^2+b);
(%o3)                         true
```

See also: `freeof`.

<!-- category: Programming -->
<!-- keywords: listconstvars -->
<!-- signatures: listconstvars -->
### Variable: listconstvars

Default value: `false`


When `listconstvars` is `true` the list returned by
`listofvars` contains constant variables, such as `%e`,
`%pi`, `%i` or any variables declared as constant that
occur in *expr*. A variable is declared as `constant`
type via `declare`, and `constantp` returns `true`
for all variables declared as `constant`. The default is to
omit constant variables from `listofvars` return value.

See also: `declare`, `constantp`.

<!-- category: Programming -->
<!-- keywords: listdummyvars -->
<!-- signatures: listdummyvars -->
### Variable: listdummyvars

Default value: `true`


When `listdummyvars` is `false`, "dummy variables" in the expression
will not be included in the list returned by `listofvars`.  (The meaning
of "dummy variables" is as given in `freeof`.  "Dummy variables" are
mathematical things like the index of a sum or product, the limit variable,
and the definite integration variable.)


Example:









```maxima
maxima
(%i1) listdummyvars: true$

(%i2) listofvars ('sum(f(i), i, 0, n));
(%o2)                        [i, n]

(%i3) listdummyvars: false$

(%i4) listofvars ('sum(f(i), i, 0, n));
(%o4)                          [n]
```

See also: `listofvars`, `freeof`.

<!-- category: Programming -->
<!-- keywords: listofvars -->
<!-- signatures: listofvars(expr) -->
### Function: listofvars (expr)

Returns a list of the variables in *expr*.


`listconstvars` if `true` causes `listofvars` to include 
`%e`, `%pi`, `%i`, and any variables declared constant in the 
list it returns if they appear in *expr*.  The default is to omit these.


See also the option variable `listdummyvars` to exclude or include
"dummy variables" in the list of variables.






```maxima
maxima

(%i1) listofvars (f (x[1]+y) / g^(2+a));
(%o1)                     [g, a, x , y]
                                  1
```

See also: `listconstvars`, `listdummyvars`.

<!-- category: Programming -->
<!-- keywords: lpart -->
<!-- signatures: lpart(label, expr, n_1, ..., n_k) -->
### Function: lpart (label, expr, n_1, ..., n_k)

is similar to `dpart` but uses a labelled box.  A labelled box is similar
to the one produced by `dpart` but it has a name in the top line.

See also: `dpart`.

<!-- category: Programming -->
<!-- keywords: mainvar -->
<!-- signatures: mainvar -->
### Variable: mainvar

You may declare variables to be `mainvar`.  The ordering scale for atoms is
essentially: numbers `<` constants (e.g., `%e`, `%pi`) `<` scalars `<` other
variables `<` mainvars.  E.g., compare `expand ((X+Y)^4)` with
`(declare (x, mainvar), expand ((x+y)^4))`.  (Note: Care should be taken if
you elect to use the above feature.  E.g., if you subtract an expression in
which `x` is a `mainvar` from one in which `x` isn’t a
`mainvar`, resimplification e.g. with `ev (expr, simp)` may be
necessary if cancellation is to occur.  Also, if you save an expression in which
`x` is a `mainvar`, you probably should also save `x`.)

<!-- category: Programming -->
<!-- keywords: noun -->
<!-- signatures: noun -->
### Variable: noun

`noun` is one of the options of the `declare` command.  It makes a
function so declared a "noun", meaning that it won’t be evaluated
automatically.


Example:









```maxima
maxima

(%i1) factor (12345678);
                             2
(%o1)                     2 3  47 14593


(%i2) declare (factor, noun);
(%o2)                         done


(%i3) factor (12345678);
(%o3)                   factor(12345678)


(%i4) ''%, nouns;
                             2
(%o4)                     2 3  47 14593
```

See also: `declare`.

<!-- category: Programming -->
<!-- keywords: noundisp -->
<!-- signatures: noundisp -->
### Variable: noundisp

Default value: `false`


When `noundisp` is `true`, nouns display with
a single quote.  This switch is always `true` when displaying function
definitions.

<!-- category: Programming -->
<!-- keywords: nounify -->
<!-- signatures: nounify(f) -->
### Function: nounify (f)

Returns the noun form of the function name *f*.  This is
needed if one wishes to refer to the name of a verb function as if it
were a noun.  Note that some verb functions will return their noun
forms if they can’t be evaluated for certain arguments.  This is also
the form returned if a function call is preceded by a quote.


See also `verbify`.

See also: `verbify`.

<!-- category: Programming -->
<!-- keywords: nterms -->
<!-- signatures: nterms(expr) -->
### Function: nterms (expr)

Returns the number of terms that *expr* would have if it were fully
expanded out and no cancellations or combination of terms occurred.
Note that expressions like `sin (expr)`, `sqrt (expr)`,
`exp (expr)`, etc. count as just one term regardless of how many
terms *expr* has (if it is a sum).

<!-- category: Programming -->
<!-- keywords: op -->
<!-- signatures: op(expr) -->
### Function: op (expr)

Returns the main operator of the expression *expr*.
This is equivalent to `part (expr, 0)` with `partswitch` set
to `false`.


`op` returns a string if the main operator is a built-in or user-defined
prefix, binary or n-ary infix, postfix, matchfix, or nofix operator.
Otherwise, if *expr* is a subscripted function expression, `op`
returns the subscripted function; in this case the return value is not an atom.
Otherwise, *expr* is a `memoizing function` or ordinary function expression,
and `op` returns a symbol.


`op` observes the value of the global flag `inflag`.


`op` evaluates it argument.


See also `args`.


Examples:


















```maxima
maxima
(%i1) stringdisp: true$

(%i2) op (a * b * c);
(%o2)                          "*"


(%i3) op (a * b + c);
(%o3)                          "+"


(%i4) op ('sin (a + b));
(%o4)                          sin


(%i5) op (a!);
(%o5)                          "!"


(%i6) op (-a);
(%o6)                          "-"


(%i7) op ([a, b, c]);
(%o7)                          "["


(%i8) op ('(if a > b then c else d));
(%o8)                         "if"


(%i9) op ('foo (a));
(%o9)                          foo


(%i10) prefix (foo);
(%o10)                        "foo"


(%i11) op (foo a);
(%o11)                        "foo"


(%i12) op (F [x, y] (a, b, c));
(%o12)                        F
                               x, y


(%i13) op (G [u, v, w]);
(%o13)                          G
```

See also: `memoizing-function`, `inflag`, `args`.

<!-- category: Programming -->
<!-- keywords: operatorp -->
<!-- signatures: operatorp(expr, op), operatorp(expr, [op_1, ..., op_n]) -->
### Function: operatorp (expr, op)

`operatorp (expr, op)` returns `true`
if *op* is equal to the operator of *expr*.


`operatorp (expr, [op_1, ..., op_n])` returns
`true` if some element *op_1*, ..., *op_n* is equal to the
operator of *expr*.


`operatorp` observes the value of the global flag `inflag`.

See also: `inflag`.

<!-- category: Programming -->
<!-- keywords: opsubst -->
<!-- signatures: opsubst -->
### Variable: opsubst

Default value: `true`


When `opsubst` is `false`, `subst` does not attempt to
substitute into the operator of an expression.  E.g., 
`(opsubst: false, subst (x^2, r, r+r[0]))` will work.










```maxima
maxima

(%i1) r+r[0];
(%o1)                        r + r
                                  0


(%i2) opsubst;
(%o2)                         true


(%i3) subst (x^2, r, r+r[0]);
                            2     2
(%o3)                      x  + (x )
                                    0


(%i4) opsubst: not opsubst;
(%o4)                         false


(%i5) subst (x^2, r, r+r[0]);
                              2
(%o5)                        x  + r
                                   0
```

See also: `subst`.

<!-- category: Programming -->
<!-- keywords: optimize -->
<!-- signatures: optimize(expr) -->
### Function: optimize (expr)

Returns an expression that produces the same value and
side effects as *expr* but does so more efficiently by avoiding the
recomputation of common subexpressions.  `optimize` also has the side
effect of "collapsing" its argument so that all common subexpressions
are shared.  Do `example (optimize)` for examples.

<!-- category: Programming -->
<!-- keywords: optimprefix -->
<!-- signatures: optimprefix -->
### Variable: optimprefix

Default value: `%`


`optimprefix` is the prefix used for generated symbols by
the `optimize` command.

See also: `optimize`.

<!-- category: Programming -->
<!-- keywords: ordergreat, orderless -->
<!-- signatures: ordergreat(v_1, ..., v_n), orderless(v_1, ..., v_n) -->
### Function: ordergreat (v_1, ..., v_n)

`ordergreat` changes the canonical ordering of Maxima expressions
such that *v_1* succeeds *v_2* succeeds ...  succeeds *v_n*,
and *v_n* succeeds any other symbol not mentioned as an argument.


`orderless` changes the canonical ordering of Maxima expressions
such that *v_1* precedes *v_2* precedes ... precedes *v_n*,
and *v_n* precedes any other variable not mentioned as an argument.


The order established by `ordergreat` and `orderless` is dissolved
by `unorder`.  `ordergreat` and `orderless` can be called only
once each, unless `unorder` is called; only the last call to
`ordergreat` and `orderless` has any effect.


See also `ordergreatp`.

See also: `unorder`, `ordergreatp`.

<!-- category: Programming -->
<!-- keywords: ordergreatp, orderlessp -->
<!-- signatures: ordergreatp(expr_1, expr_2), orderlessp(expr_1, expr_2) -->
### Function: ordergreatp (expr_1, expr_2)

`ordergreatp` returns `true` if *expr_1* succeeds *expr_2* in
the canonical ordering of Maxima expressions, and `false` otherwise.


`orderlessp` returns `true` if *expr_1* precedes *expr_2* in
the canonical ordering of Maxima expressions, and `false` otherwise.


All Maxima atoms and expressions are comparable under `ordergreatp` and
`orderlessp`, although there are isolated examples of expressions for which
these predicates are not transitive; that is a bug.


The canonical ordering of atoms (symbols, literal numbers, and strings) is the
following.


(integers and floats) precede (bigfloats) precede
(declared constants) precede (strings) precede (declared scalars)
precede (first argument to `orderless`) precedes ... precedes
(last argument to `orderless`) precedes (other symbols) precede
(last argument to `ordergreat`) precedes ... precedes
(first argument to `ordergreat`) precedes (declared main variables)


For non-atomic expressions, the canonical ordering is derived from the ordering
for atoms.  For the built-in `+` `*` and `^` operators,
the ordering is not easily summarized.  For other built-in operators and all
other functions and operators, expressions are ordered by their arguments
(beginning with the first argument), then by the name of the operator or
function.  In the case of subscripted expressions, the subscripted symbol is
considered the operator and the subscript is considered an argument.


The canonical ordering of expressions is modified by the functions
`ordergreat` and `orderless`, and the `mainvar`,
`constant`, and `scalar` declarations.


See also `sort`.


Examples:


Ordering ordinary symbols and constants.
Note that `%pi` is not ordered according to its numerical value.







```maxima
maxima

(%i1) stringdisp : true;
(%o1)                         true


(%i2) sort ([%pi, 3b0, 3.0, x, X, "foo", 3, a, 4, "bar", 4.0, 4b0]);
(%o2) [3, 3.0, 4, 4.0, 3.0b0, 4.0b0, %pi, "bar", "foo", X, a, x]
```


Effect of `ordergreat` and `orderless` functions.









```maxima
maxima

(%i1) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o1)           [A, E, G, H, J, K, M, P, S, T, W]


(%i2) ordergreat (S, J);
(%o2)                         done


(%i3) orderless (M, H);
(%o3)                         done


(%i4) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o4)           [M, H, A, E, G, K, P, T, W, J, S]
```


Effect of `mainvar`, `constant`, and `scalar` declarations.










```maxima
maxima

(%i1) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o1)   [A1, B1, C1, aa, bar, baz, bb, cc, dd, foo, quux]


(%i2) declare (aa, mainvar);
(%o2)                         done


(%i3) declare ([baz, quux], constant);
(%o3)                         done


(%i4) declare ([A1, B1], scalar);
(%o4)                         done


(%i5) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o5)   [baz, quux, A1, B1, C1, bar, bb, cc, dd, foo, aa]
```


Ordering non-atomic expressions.








```maxima
maxima

(%i1) sort ([1, 2, n, f(1), f(2), f(2, 1), g(1), g(1, 2), g(n),
       f(n, 1)]);
(%o1) [1, 2, f(1), g(1), g(1, 2), f(2), f(2, 1), n, g(n), 
                                                         f(n, 1)]


(%i2) sort ([foo(1), X[1], X[k], foo(k), 1, k]);
(%o2)            [1, X , foo(1), k, X , foo(k)]
                      1              k
```

See also: `orderless`, `ordergreat`, `mainvar`, `constant`, `sort`.

<!-- category: Programming -->
<!-- keywords: part -->
<!-- signatures: part(expr, n_1, ..., n_k) -->
### Function: part (expr, n_1, ..., n_k)

Returns parts of the displayed form of `expr`.  It obtains the part of
`expr` as specified by the indices *n_1*, ..., *n_k*.  First
part *n_1* of `expr` is obtained, then part *n_2* of that, etc.
The result is part *n_k* of ... part *n_2* of part *n_1* of
`expr`.  If no indices are specified `expr` is returned.


`part` can be used to obtain an element of a list, a row of a matrix, etc.




If the last argument to a `part` function is a list of indices then
several subexpressions are picked out, each one corresponding to an
index of the list.  Thus `part (x + y + z, [1, 3])` is `z+x`.


`piece` holds the last expression selected when using the `part`
functions.  It is set during the execution of the function and thus
may be referred to in the function itself as shown below.


If `partswitch` is set to `true` then `end` is returned when a
selected part of an expression doesn’t exist, otherwise an error message is
given.


See also `inpart`, `substpart`, `substinpart`,
`dpart`, and `lpart`.


Examples:








```maxima
maxima

(%i1) part(z+2*y+a,2);
(%o1)                          2 y


(%i2) part(z+2*y+a,[1,3]);
(%o2)                         z + a


(%i3) part(z+2*y+a,2,1);
(%o3)                           2
```


`example (part)` displays additional examples.

See also: `piece`, `partswitch`, `inpart`, `substpart`, `substinpart`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: partition -->
<!-- signatures: partition(expr, x) -->
### Function: partition (expr, x)

Returns a list of two expressions.  They are (1) the factors of *expr*
(if it is a product), the terms of *expr* (if it is a sum), or the list
(if it is a list) which don’t contain *x* and, (2) the factors, terms,
or list which do.


Examples:








```maxima
maxima

(%i1) partition (2*a*x*f(x), x);
(%o1)                     [2 a, x f(x)]


(%i2) partition (a+b, x);
(%o2)                      [b + a, 0]


(%i3) partition ([a, b, f(a), c], a);
(%o3)                  [[b, c], [a, f(a)]]
```

<!-- category: Programming -->
<!-- keywords: partswitch -->
<!-- signatures: partswitch -->
### Variable: partswitch

Default value: `false`


When `partswitch` is `true`, `end` is returned
when a selected part of an expression doesn’t exist, otherwise an
error message is given.

<!-- category: Programming -->
<!-- keywords: pickapart -->
<!-- signatures: pickapart(expr, n) -->
### Function: pickapart (expr, n)

Assigns intermediate expression labels to subexpressions of *expr* at depth
*n*, an integer.  Subexpressions at greater or lesser depths are not
assigned labels.  `pickapart` returns an expression in terms of
intermediate expressions equivalent to the original expression *expr*.


See also `part`, `dpart`, `lpart`,
`inpart`, and `reveal`.


Examples:



```maxima
(%i1) expr: (a+b)/2 + sin (x^2)/3 - log (1 + sqrt(x+1));
                                          2
                                     sin(x )   b + a
(%o1)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2
(%i2) pickapart (expr, 0);

                                          2
                                     sin(x )   b + a
(%t2)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2

(%o2)                          %t2
(%i3) pickapart (expr, 1);

(%t3)                - log(sqrt(x + 1) + 1)


                                  2
                             sin(x )
(%t4)                        -------
                                3


                              b + a
(%t5)                         -----
                                2

(%o5)                    %t5 + %t4 + %t3
(%i5) pickapart (expr, 2);

(%t6)                 log(sqrt(x + 1) + 1)


                                  2
(%t7)                        sin(x )


(%t8)                         b + a

                         %t8   %t7
(%o8)                    --- + --- - %t6
                          2     3
(%i8) pickapart (expr, 3);

(%t9)                    sqrt(x + 1) + 1


                                2
(%t10)                         x

                  b + a              sin(%t10)
(%o10)            ----- - log(%t9) + ---------
                    2                    3
(%i10) pickapart (expr, 4);

(%t11)                     sqrt(x + 1)

                      2
                 sin(x )   b + a
(%o11)           ------- + ----- - log(%t11 + 1)
                    3        2

(%i11) pickapart (expr, 5);

(%t12)                        x + 1

                   2
              sin(x )   b + a
(%o12)        ------- + ----- - log(sqrt(%t12) + 1)
                 3        2
(%i12) pickapart (expr, 6);
                  2
             sin(x )   b + a
(%o12)       ------- + ----- - log(sqrt(x + 1) + 1)
                3        2
```

See also: `part`, `dpart`, `lpart`, `inpart`, `reveal`.

<!-- category: Programming -->
<!-- keywords: piece -->
<!-- signatures: piece -->
### Variable: piece

Holds the last expression selected when using the `part` functions.

It is set during the execution of the function and thus may be referred to in
the function itself.

See also: `part`.

<!-- category: Programming -->
<!-- keywords: psubst -->
<!-- signatures: psubst(list, expr), psubst(a, b, expr) -->
### Function: psubst (list, expr)

`psubst(a, b, expr)` is similar to `subst`.  See
`subst`.


In distinction from `subst` the function `psubst` makes parallel 
substitutions, if the first argument *list* is a list of equations.


See also `sublis` for making parallel substitutions and `let` and
`letsimp` for others ways to do substitutions.


Example:


The first example shows parallel substitution with `psubst`.  The second
example shows the result for the function `subst`, which does a serial
substitution.







```maxima
maxima

(%i1) psubst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o1)                    sin(b) + sin(a)


(%i2) subst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o2)                       2 sin(a)
```

See also: `subst`, `sublis`, `let`, `letsimp`.

<!-- category: Programming -->
<!-- keywords: rembox -->
<!-- signatures: rembox(expr, unlabelled), rembox(expr, label), rembox(expr) -->
### Function: rembox (expr, unlabelled)

Removes boxes from *expr*.


`rembox (expr, unlabelled)` removes all unlabelled boxes from
*expr*.


`rembox (expr, label)` removes only boxes bearing *label*.


`rembox (expr)` removes all boxes, labelled and unlabelled.


Boxes are drawn by the `box`, `dpart`, and `lpart`
functions.


Examples:












```maxima
maxima

(%i1) expr: (a*d - b*c)/h^2 + sin(%pi*x);
                                  a d - b c
(%o1)                sin(%pi x) + ---------
                                      2
                                     h


(%i2) dpart (dpart (expr, 1, 1), 2, 2);
                        """""""    a d - b c
(%o2)               sin("%pi x") + ---------
                        """""""      """"
                                     " 2"
                                     "h "
                                     """"


(%i3) expr2: lpart (BAR, lpart (FOO, %, 1), 2);
                  FOO"""""""""""   BAR""""""""
                  "    """"""" "   "a d - b c"
(%o3)             "sin("%pi x")" + "---------"
                  "    """"""" "   "  """"   "
                  """"""""""""""   "  " 2"   "
                                   "  "h "   "
                                   "  """"   "
                                   """""""""""


(%i4) rembox (expr2, unlabelled);
                                  BAR""""""""
                   FOO"""""""""   "a d - b c"
(%o4)              "sin(%pi x)" + "---------"
                   """"""""""""   "    2    "
                                  "   h     "
                                  """""""""""


(%i5) rembox (expr2, FOO);
                                  BAR""""""""
                       """""""    "a d - b c"
(%o5)              sin("%pi x") + "---------"
                       """""""    "  """"   "
                                  "  " 2"   "
                                  "  "h "   "
                                  "  """"   "
                                  """""""""""


(%i6) rembox (expr2, BAR);
                   FOO"""""""""""
                   "    """"""" "   a d - b c
(%o6)              "sin("%pi x")" + ---------
                   "    """"""" "     """"
                   """"""""""""""     " 2"
                                      "h "
                                      """"


(%i7) rembox (expr2);
                                  a d - b c
(%o7)                sin(%pi x) + ---------
                                      2
                                     h
```

See also: `box`, `dpart`, `lpart`.

<!-- category: Programming -->
<!-- keywords: reveal -->
<!-- signatures: reveal(expr, depth) -->
### Function: reveal (expr, depth)

Replaces parts of *expr* at the specified integer *depth*
with descriptive summaries.



- *
Sums and differences are replaced by `Sum(n)`
where *n* is the number of operands of the sum.
- *
Products are replaced by `Product(n)`
where *n* is the number of operands of the product.
- *
Exponentials are replaced by `Expt`.
- *
Quotients are replaced by `Quotient`.
- *
Unary negation is replaced by `Negterm`.
- *
Lists are replaced by `List(n)` where *n* is the number of
elements of the list.


When *depth* is greater than or equal to the maximum depth of *expr*,
`reveal (expr, depth)` returns *expr* unmodified.


`reveal` evaluates its arguments.
`reveal` returns the summarized expression.


Example:












```maxima
maxima

(%i1) e: expand ((a - b)^2)/expand ((exp(a) + exp(b))^2);
                          2            2
                         b  - 2 a b + a
(%o1)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e


(%i2) reveal (e, 1);
(%o2)                       Quotient


(%i3) reveal (e, 2);
                             Sum(3)
(%o3)                        ------
                             Sum(3)


(%i4) reveal (e, 3);
                     Expt + Negterm + Expt
(%o4)               ------------------------
                    Product(2) + Expt + Expt


(%i5) reveal (e, 4);
                       2                 2
                      b  - Product(3) + a
(%o5)         ------------------------------------
                         Product(2)     Product(2)
              2 Expt + %e           + %e


(%i6) reveal (e, 5);
                         2            2
                        b  - 2 a b + a
(%o6)              --------------------------
                       Sum(2)     2 b     2 a
                   2 %e       + %e    + %e


(%i7) reveal (e, 6);
                          2            2
                         b  - 2 a b + a
(%o7)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
```

<!-- category: Programming -->
<!-- keywords: sqrtdenest -->
<!-- signatures: sqrtdenest(expr) -->
### Function: sqrtdenest (expr)

Denests `sqrt` of simple, numerical, binomial surds, where possible.  E.g.







```maxima
maxima

(%i1) sqrt(sqrt(3)/2+1)/sqrt(11*sqrt(2)-12);
                             sqrt(3)
                        sqrt(------- + 1)
                                2
(%o1)                 ---------------------
                      sqrt(11 sqrt(2) - 12)


(%i2) sqrtdenest(%);
                           sqrt(3)   1
                           ------- + -
                              2      2
(%o2)                     -------------
                             1/4    3/4
                          3 2    - 2
```


Sometimes it helps to apply `sqrtdenest` more than once, on such as
`(19601-13860 sqrt(2))^(7/4)`.

<!-- category: Programming -->
<!-- keywords: sublis -->
<!-- signatures: sublis(list, expr) -->
### Function: sublis (list, expr)

Makes multiple parallel substitutions into an expression.  *list* is a list
of equations.  The left hand side of the equations must be an atom.


The variable `sublis_apply_lambda` controls simplification after
`sublis`.


See also `psubst` for making parallel substitutions.


Example:






```maxima
maxima

(%i1) sublis ([a=b, b=a], sin(a) + cos(b));
(%o1)                    sin(b) + cos(a)
```

See also: `sublis_apply_lambda`, `psubst`.

<!-- category: Programming -->
<!-- keywords: sublis_apply_lambda -->
<!-- signatures: sublis_apply_lambda -->
### Variable: sublis_apply_lambda

Default value: `true`


Controls whether `lambda`’s substituted are applied in simplification after
`sublis` is used or whether you have to do an `ev` to get things to
apply.  `true` means do the application.

See also: `ev`.

<!-- category: Programming -->
<!-- keywords: subnumsimp -->
<!-- signatures: subnumsimp -->
### Variable: subnumsimp

Default value: `false`


If `true` then the functions `subst` and `psubst` can substitute
a subscripted variable `f[x]` with a number, when only the symbol `f`
is given.


See also `subst`.






subst: cannot substitute 100 for operator g in expression g
                                                           x
 – an error. To debug this try: debugmode(true);


```maxima
maxima
(%i1) subst(100,g,g[x]+2);

(%i2) subst(100,g,g[x]+2),subnumsimp:true;
(%o2)                          102
```

See also: `subst`, `psubst`.

<!-- category: Programming -->
<!-- keywords: subst -->
<!-- signatures: subst(a, b, c) -->
### Function: subst (a, b, c)

Substitutes *a* for *b* in *c*.  *b* must be an atom or a
complete subexpression of *c*.  For example, `x+y+z` is a complete
subexpression of `2*(x+y+z)/w` while `x+y` is not.  When *b* does
not have these characteristics, one may sometimes use `substpart` or
`ratsubst` (see below).  Alternatively, if *b* is of the form
`e/f` then one could use `subst (a*f, e, c)` while if *b* is of
the form `e^(1/f)` then one could use `subst (a^f, e, c)`.  The
`subst` command also discerns the `x^y` in `x^-y` so that
`subst (a, sqrt(x), 1/sqrt(x))` yields `1/a`.  *a* and *b*
may also be operators of an expression enclosed in double-quotes `"` or
they may be function names.  If one wishes to substitute for the independent
variable in derivative forms then the `at` function (see below) should be
used.



`subst` is an alias for `substitute`.


The commands `subst (eq_1, expr)` or
`subst ([eq_1, ..., eq_k], expr)` are other permissible
forms.  The *eq_i* are equations indicating substitutions to be made.
For each equation, the right side will be substituted for the left in the 
expression *expr*.  The equations are substituted in serial from left to
right in *expr*.  See the functions `sublis` and `psubst` for 
making parallel substitutions.


`exptsubst` if `true` permits substitutions
like `y` for `%e^x` in `%e^(a*x)` to take place.



When `opsubst` is `false`,
`subst` will not attempt to substitute into the operator of an expression.
E.g. `(opsubst: false, subst (x^2, r, r+r[0]))` will work.


See also `at`, `ev` and `psubst`, as well as `let`
and `letsimp`.


Examples:







```maxima
maxima

(%i1) subst (a, x+y, x + (x+y)^2 + y);
                                    2
(%o1)                      y + x + a


(%i2) subst (-%i, %i, a + b*%i);
(%o2)                       a - %i b
```


The substitution is done in serial for a list of equations.  Compare this with
a parallel substitution:







```maxima
maxima

(%i1) subst([a=b, b=c], a+b);
(%o1)                          2 c


(%i2) sublis([a=b, b=c], a+b);
(%o2)                         c + b
```


Single-character Operators like `+` and `-` have to be quoted in
order to be replaced by subst. It is to note, though, that `a+b-c`
might be expressed as `a+b+(-1*c)` internally.






```maxima
maxima

(%i1) subst(["+"="-"],a+b-c);
(%o1)                       c - b + a
```


The difference between `subst` and `at` can be seen in the
following example:







```maxima
maxima

(%i1) g1:y(t)=a*x(t)+b*diff(x(t),t);
                            d
(%o1)             y(t) = b (-- (x(t))) + a x(t)
                            dt


(%i2) subst('diff(x(t),t)=1,g1);
(%o2)                   y(t) = a x(t) + b


(%i3) at(g1,'diff(x(t),t)=1);
                              |
                     d        |
(%o3)      y(t) = b (-- (x(t))|             ) + a x(t)
                     dt       |d
                              |-- (x(t)) = 1
                               dt
```



For further examples, do `example (subst)`.

See also: `substpart`, `ratsubst`, `exptsubst`, `at`, `ev`, `psubst`, `let`, `letsimp`.

<!-- category: Programming -->
<!-- keywords: substinpart -->
<!-- signatures: substinpart(x, expr, n_1, ..., n_k) -->
### Function: substinpart (x, expr, n_1, ..., n_k)

Similar to `substpart`, but `substinpart` works on the
internal representation of *expr*.


Examples:








```maxima
maxima

(%i1) x . 'diff (f(x), x, 2);
                              2
                             d
(%o1)                   x . (--- (f(x)))
                               2
                             dx


(%i2) substinpart (d^2, %, 2);
                                  2
(%o2)                        x . d


(%i3) substinpart (f1, f[1](x + 1), 0);
(%o3)                       f1(x + 1)
```


If the last argument to a `part` function is a list of indices then
several subexpressions are picked out, each one corresponding to an
index of the list.  Thus






```maxima
maxima

(%i1) part (x + y + z, [1, 3]);
(%o1)                         z + x
```


`piece` holds the value of the last expression selected when using the
`part` functions.  It is set during the execution of the function and
thus may be referred to in the function itself as shown below.
If `partswitch` is set to `true` then `end` is returned when a
selected part of an expression doesn’t exist, otherwise an error
message is given.











```maxima
maxima

(%i1) expr: 27*y^3 + 54*x*y^2 + 36*x^2*y + y + 8*x^3 + x + 1;
              3         2       2            3
(%o1)     27 y  + 54 x y  + 36 x  y + y + 8 x  + x + 1


(%i2) part (expr, 2, [1, 3]);
                                  2
(%o2)                         54 y


(%i3) sqrt (piece/54);
(%o3)                        abs(y)


(%i4) substpart (factor (piece), expr, [1, 2, 3, 5]);
                               3
(%o4)               (3 y + 2 x)  + y + x + 1


(%i5) expr: 1/x + y/x - 1/z;
                             1   y   1
(%o5)                      - - + - + -
                             z   x   x


(%i6) substpart (xthru (piece), expr, [2, 3]);
                            y + 1   1
(%o6)                       ----- - -
                              x     z
```


Also, setting the option `inflag` to `true` and calling `part`
or `substpart` is the same as calling `inpart` or `substinpart`.

See also: `substpart`, `piece`, `partswitch`, `inflag`, `part`, `inpart`.

<!-- category: Programming -->
<!-- keywords: substpart -->
<!-- signatures: substpart(x, expr, n_1, ..., n_k) -->
### Function: substpart (x, expr, n_1, ..., n_k)

Substitutes *x* for the subexpression picked out by the rest of the
arguments as in `part`.  It returns the new value of *expr*.  *x*
may be some operator to be substituted for an operator of *expr*.  In some
cases *x* needs to be enclosed in double-quotes `"` (e.g.
`substpart ("+", a*b, 0)` yields `b + a`).


Example:









```maxima
maxima

(%i1) 1/(x^2 + 2);
                               1
(%o1)                        ------
                              2
                             x  + 2


(%i2) substpart (3/2, %, 2, 1, 2);
                               1
(%o2)                       --------
                             3/2
                            x    + 2


(%i3) a*x + f(b, y);
(%o3)                     a x + f(b, y)


(%i4) substpart ("+", %, 1, 0);
(%o4)                    x + f(b, y) + a
```


Also, setting the option `inflag` to `true` and calling `part`
or `substpart` is the same as calling `inpart` or
`substinpart`.

See also: `part`, `inflag`, `substinpart`.

<!-- category: Programming -->
<!-- keywords: symbolp -->
<!-- signatures: symbolp(expr) -->
### Function: symbolp (expr)

Returns `true` if *expr* is a symbol, else `false`.




See also `Identifiers`.

See also: `Identifiers`.

<!-- category: Programming -->
<!-- keywords: unorder -->
<!-- signatures: unorder() -->
### Function: unorder ()

Disables the aliasing created by the last use of the ordering commands 
`ordergreat` and `orderless`.  `ordergreat` and `orderless` 
may not be used more than one time each without calling `unorder`.
`unorder` does not substitute back in expressions the original symbols for
the aliases introduced by `ordergreat` and `orderless`.  Therefore,
after execution of `unorder` the aliases appear in previous expressions.

 

See also `ordergreat` and `orderless`.


Examples:


`ordergreat(a)` introduces an alias for the symbol `a`.  Therefore,
the difference of `%o2` and `%o4` does not vanish.  `unorder`
does not substitute back the symbol `a` and the alias appears in the
output `%o7`.












```maxima
maxima

(%i1) unorder();
(%o1)                          []


(%i2) b*x + a^2;
                                   2
(%o2)                       b x + a


(%i3) ordergreat (a);
(%o3)                         done


(%i4) b*x + a^2;
 %th(1) - %th(3);
                             2
(%o4)                       a  + b x


(%i5) unorder();
                              2    2
(%o5)                        a  - a


(%i6) %th(2);
(%o6)                          [a]
```

<!-- category: Programming -->
<!-- keywords: verbify -->
<!-- signatures: verbify(f) -->
### Function: verbify (f)

Returns the verb form of the function name *f*.
See also `verb`, `noun`, and `nounify`.


Examples:









```maxima
maxima

(%i1) verbify ('foo);
(%o1)                          foo


(%i2) :lisp $%
$FOO


(%i2) nounify (foo);
(%o2)                          foo


(%i3) :lisp $%
%FOO
```

