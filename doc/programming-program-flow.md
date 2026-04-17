## Program Flow

<!-- category: Programming -->
<!-- keywords: backtrace -->
<!-- signatures: backtrace(), backtrace(n) -->
### Function: backtrace ()

Prints the call stack, that is, the list of functions which
called the currently active function.


`backtrace ()` prints the entire call stack.


`backtrace (n)` prints the *n* most recent 
functions, including the currently active function.




`backtrace` can be called from a script, a function, or the interactive
prompt (not only in a debugging context).


Examples:



- *
`backtrace ()` prints the entire call stack.





```maxima
maxima
(%i1) h(x) := g(x/7)$
(%i2) g(x) := f(x-11)$
(%i3) f(x) := e(x^2)$
(%i4) e(x) := (backtrace(), 2*x + 13)$
(%i5) h(10);
#0: e(x=4489/49)
#1: f(x=-(67/7))
#2: g(x=10/7)
#3: h(x=10)
                              9615
(%o5)                         ----
                               49
```



- *
`backtrace (n)` prints the *n* most recent 
functions, including the currently active function.





```maxima
maxima
(%i1) h(x) := (backtrace(1), g(x/7))$
(%i2) g(x) := (backtrace(1), f(x-11))$
(%i3) f(x) := (backtrace(1), e(x^2))$
(%i4) e(x) := (backtrace(1), 2*x + 13)$
(%i5) h(10);
#0: h(x=10)
#0: g(x=10/7)
#0: f(x=-(67/7))
#0: e(x=4489/49)
                              9615
(%o5)                         ----
                               49
```

<!-- category: Programming -->
<!-- keywords: do, while, unless, for, from, thru, step, next, in -->
<!-- signatures: while, unless, for, from, thru, step, next, in -->
### Function: do

The `do` statement is used for performing iteration. The general
form of the `do` statements maxima supports is:



- *
`for variable: initial_value step increment thru limit do body`
- *
`for variable: initial_value step increment while condition do body`
- *
`for variable: initial_value step increment unless condition do body`
- *
`for variable in list do body`
- *
`for variable in expr do body`
- *
`for variable in hash_table do body`


If the loop is expected to generate a list as output the command
`makelist` may be the appropriate command to use instead,
`Performance-considerations-for-Lists`.


*initial_value*, *increment*, *limit*, and *body* can be any
expression. If the increment is 1 then "`step 1`"
may be omitted; As always, if `body` needs to contain more than one command
these commands can be specified as a comma-separated list surrounded
by parenthesis or as a `block`.
Due to its great generality the `do` statement will be described in two parts.
The first form of the `do` statement (which is shown in the first three
items above) is analogous to that used in
several other programming languages (Fortran, Algol, PL/I, etc.); then
the other features will be mentioned.


The execution of the `do` statement proceeds by first assigning
the *initial_value* to the *variable* (henceforth called the
control-variable).  Then: (1) If the control-variable has exceeded the
limit of a `thru` specification, or if the condition of the
`unless` is `true`, or if the condition of the `while`
is `false` then the `do` terminates.  (2) The *body* is
evaluated.  (3) The increment is added to the control-variable.  The
process from (1) to (3) is performed repeatedly until the termination
condition is satisfied.  One may also give several termination
conditions in which case the `do` terminates when any of them is
satisfied.


In general the `thru` test is satisfied when the control-variable
is greater than the *limit* if the *increment* was
non-negative, or when the control-variable is less than the
*limit* if the *increment* was negative.  The
*increment* and *limit* may be non-numeric expressions as
long as this inequality can be determined.  However, unless the
*increment* is syntactically negative (e.g. is a negative number)
at the time the `do` statement is input, Maxima assumes it will
be positive when the `do` is executed.  If it is not positive,
then the `do` may not terminate properly.


Note that the *limit*, *increment*, and termination condition are
evaluated each time through the loop.  Thus if any of these involve
much computation, and yield a result that does not change during all
the executions of the *body*, then it is more efficient to set a
variable to their value prior to the `do` and use this variable in the
`do` form.


The value normally returned by a `do` statement is the atom
`done`.  However, the function `return` may be used inside
the *body* to exit the `do` prematurely and give it any
desired value.  Note however that a `return` within a `do`
that occurs in a `block` will exit only the `do` and not the
`block`.  Note also that the `go` function may not be used
to exit from a `do` into a surrounding `block`.


The control-variable is always local to the `do` and thus any
variable may be used without affecting the value of a variable with
the same name outside of the `do`.  The control-variable is unbound
after the `do` terminates.






```maxima
maxima

(%i1) for a:-3 thru 26 step 7 do display(a)$
                             a = - 3

                              a = 4

                             a = 11

                             a = 18

                             a = 25
```








```maxima
maxima
(%i1) s: 0$

(%i2) for i: 1 while i <= 10 do s: s+i;
(%o2)                         done


(%i3) s;
(%o3)                          55
```


Note that the condition `while i <= 10`
is equivalent to `unless i > 10` and also `thru 10`.











```maxima
maxima
(%i1) series: 1$
(%i2) term: exp (sin (x))$

(%i3) for p: 1 unless p > 7 do
    (term: diff (term, x)/p,
     series: series + subst (x=0, term)*x^p)$


(%i4) series;
                  7    6     5    4    2
                 x    x     x    x    x
(%o4)            -- - --- - -- - -- + -- + x + 1
                 90   240   15   8    2
```


which gives 8 terms of the Taylor series for `e^sin(x)`.














```maxima
maxima
(%i1) poly: 0$

(%i2) for i: 1 thru 5 do
    for j: i step -1 thru 1 do
        poly: poly + i*x^j$


(%i3) poly;
                  5      4       3       2
(%o3)          5 x  + 9 x  + 12 x  + 14 x  + 15 x

(%i4) guess: -3.0$

(%i5) for i: 1 thru 10 do
    (guess: subst (guess, x, 0.5*(x + 10/x)),
    if abs (guess^2 - 10) < 0.00005 then return (guess));
(%o5)                  - 3.162280701754386
```


This example computes the negative square root of 10 using the
Newton- Raphson iteration a maximum of 10 times.  Had the convergence
criterion not been met the value returned would have been `done`.


Instead of always adding a quantity to the control-variable one
may sometimes wish to change it in some other way for each iteration.
In this case one may use `next expression` instead of
`step increment`.  This will cause the control-variable to be set to
the result of evaluating *expression* each time through the loop.






```maxima
maxima

(%i1) for count: 2 next 3*count thru 20 do display (count)$
                            count = 2

                            count = 6

                           count = 18
```



As an alternative to `for variable: value ...do...`
the syntax `for variable from value ...do...`  may be
used.  This permits the `from value` to be placed after the
`step` or `next` value or after the termination condition.
If `from value` is omitted then 1 is used as the initial
value.


Sometimes one may be interested in performing an iteration where
the control-variable is never actually used.  It is thus permissible
to give only the termination conditions omitting the initialization
and updating information as in the following example to compute the
square-root of 5 using a poor initial guess.









```maxima
maxima
(%i1) x: 1000$
(%i2) thru 20 do x: 0.5*(x + 5.0/x)$

(%i3) x;
(%o3)                   2.23606797749979


(%i4) sqrt(5), numer;
(%o4)                   2.23606797749979
```


If it is desired one may even omit the termination conditions entirely
and just give `do body` which will continue to evaluate the
*body* indefinitely.  In this case the function `return`
should be used to terminate execution of the `do`.










```maxima
maxima

(%i1) newton (f, x):= ([y, df, dfx], df: diff (f ('x), 'x),
    do (y: ev(df), x: x - f(x)/y,
        if abs (f (x)) < 5e-6 then return (x)))$
warning: parser: I'll let it stand, but (...) doesn't recognize local variables.
warning: parser: did you mean to say: block([y, df, dfx], ...) ?

(%i2) sqr (x) := x^2 - 5.0$

(%i3) newton (sqr, 1000);
(%o3)                  2.2360680270621947
```



(Note that `return`, when executed, causes the current value of `x` to
be returned as the value of the `do`.  The `block` is exited and this
value of the `do` is returned as the value of the `block` because the
`do` is the last statement in the block.)


A `for` loop can also iterate over the contents of lists, general expressions, and hash tables, as follows.



```maxima
for variable in list end_tests do body

for variable in expr end_tests do body

for variable in hash_table end_tests do body
```


In each case,
*body* is evaluated once for *variable* assigned
each element of *list*,
each argument of *expr*,
or each key-value pair of *hash_table*,
respectively.
If present,
*end_tests* terminate the loop if any test evaluates to `true`;
otherwise the loop terminates when the elements of *list*,
the arguments of *expr*,
or the key-value pairs of *hash_table*
are exhausted,
or when `return` is executed in *body*.


*hash_table* may be an undeclared array,
either as a symbol property (created with `use_fast_arrays` equal to `false`)
or a value (created with `use_fast_arrays` equal to `true`),
or a hash table created by `make_array(hashed, ...)`.


Values are assigned to *variable* using the general assignment operator `":"`.
Therefore any assignment to a symbol (not a subscripted expression) which is possible via `":"`
is also permissible for iterating over the contents of expressions.
In particular,
destructuring assignments are recognized;
these may be useful to work with the key-value pairs of a hash table.


Examples:


A `for` loop can iterate over the elements of a list.






```maxima
maxima

(%i1) for f in [log, rho, atan] do ldisp (f(1)) $
(%t1)                           0

(%t2)                        rho(1)

                               %pi
(%t3)                          ───
                                4
```


A `for` loop can iterate over the arguments of a general expression.







```maxima
maxima

(%i1) e: a + 1/2 + %pi*2;
                                      1
(%o1)                     a + 2 %pi + ─
                                      2
(%i2) for v in e do ldisp (v) $
(%t2)                           a

(%t3)                         2 %pi

                                1
(%t4)                           ─
                                2
```


A `for` loop can iterate over the key-value pairs of hash tables.
In this case, the hash table is an undeclared array.







```maxima
maxima

(%i1) (hh["foo"]: 444, hh["bar"]: 222, hh["baz"]: 777) $

(%i2) for p in hh do ldisp (p);
(%t2)                     [[bar], 222]

(%t3)                     [[baz], 777]

(%t4)                     [[foo], 444]

(%o4)                         done
```


Destructuring assignments are recognized;
these may be useful to work with the key-value pairs of a hash table.







```maxima
maxima

(%i1) (hh["foo"]: 444, hh["bar"]: 222, hh["baz"]: 777) $

(%i2) for [[k], v] in hh do disp (printf (false, "Key ~a --> value ~a", k, v));
                      Key bar --> value 222

                      Key baz --> value 777

                      Key foo --> value 444

(%o2)                         done
```

See also: `makelist`, `Performance-considerations-for-Lists`, `block`.

<!-- category: Programming -->
<!-- keywords: errcatch -->
<!-- signatures: errcatch(expr_1, ..., expr_n) -->
### Function: errcatch (expr_1, ..., expr_n)

Evaluates *expr_1*, ..., *expr_n* one by one and
returns `[expr_n]` (a list) if no error occurs.  If an
error occurs in the evaluation of any argument, `errcatch` 
prevents the error from propagating and
returns the empty list `[]` without evaluating any more arguments.


`errcatch`
is useful in `batch` files where one suspects an error might occur which
would terminate the `batch` if the error weren’t caught.


See also `errormsg`.

See also: `errormsg`.

<!-- category: Programming -->
<!-- keywords: errexp1 -->
<!-- signatures: errexp1 -->
### Variable: errexp1

See `error_005fsyms`.

See also: `error_syms`.

<!-- category: Programming -->
<!-- keywords: error -->
<!-- signatures: error(expr_1, ..., expr_n) -->
### Function: error (expr_1, ..., expr_n)

Evaluates and prints *expr_1*, ..., *expr_n*,
and then causes an error return to top level Maxima
or to the nearest enclosing `errcatch`.


The variable `error` is set to a list describing the error.
The first element of `error` is a format string, which merges all the
strings among the arguments *expr_1*, ..., *expr_n*,
and the remaining elements are the values of any non-string arguments.


`errormsg()` formats and prints `error`.
This is effectively reprinting the most recent error message.

<!-- category: Programming -->
<!-- keywords: error_size -->
<!-- signatures: error_size -->
### Variable: error_size

Default value: 60


`error_size` modifies error messages according to the size of expressions
which appear in them.  If the size of an expression (as determined by the Lisp
function `ERROR-SIZE`) is greater than `error_size`, the expression is
replaced in the message by a symbol, and the symbol is assigned the expression.
The symbols are taken from the list `error_syms`.


Otherwise, the expression is smaller than `error_size`, and the expression
is displayed in the message.


See also `error` and `error_005fsyms`.


Example:









The size of `U`, as determined by `ERROR-SIZE`, is 24.



```maxima
maxima
(%i1) U: (C^D^E + B + A)/(cos(X-1) + 1)$
(%i2) error_size: 20$
(%i3) error ("Example expression is", U);
Example expression is errexp1
 -- an error. To debug this try: debugmode(true);

(%i4) errexp1;
                            E
                           D
                          C   + B + A
(%o4)                    --------------
                         cos(X - 1) + 1

(%i5) error_size: 30$
(%i6) error ("Example expression is", U);

                         E
                        D
                       C   + B + A
Example expression is --------------
                      cos(X - 1) + 1
 -- an error.  Quitting.  To debug this try debugmode(true);
```

See also: `error_syms`, `error`.

<!-- category: Programming -->
<!-- keywords: error_syms -->
<!-- signatures: error_syms -->
### Variable: error_syms

Default value: `[errexp1, errexp2, errexp3]`


In error messages, expressions larger than `error_size` are replaced by
symbols, and the symbols are set to the expressions.  The symbols are taken from
the list `error_syms`.  The first too-large expression is replaced by
`error_syms[1]`, the second by `error_syms[2]`, and so on.


If there are more too-large expressions than there are elements of
`error_syms`, symbols are constructed automatically, with the *n*-th
symbol equivalent to `concat ('errexp, n)`.


See also `error` and `error_005fsize`.

See also: `error_size`, `error`.

<!-- category: Programming -->
<!-- keywords: errormsg -->
<!-- signatures: errormsg() -->
### Function: errormsg ()

Reprints the most recent error message.
The variable `error` holds the message,
and `errormsg` formats and prints it.

See also: `errormsg`.

<!-- category: Programming -->
<!-- keywords: garbage_collect -->
<!-- signatures: garbage_collect() -->
### Function: garbage_collect ()

Tries to manually trigger the lisp’s garbage collection. This rarely is necessary
as the lisp will employ an excellent algorithm for determining when to start
garbage collection.


If maxima knows how to do manually trigger the garbage collection for the
current lisp `garbage_collect` returns `true`, else `false`.

<!-- category: Programming -->
<!-- keywords: go -->
<!-- signatures: go(tag) -->
### Function: go (tag)

is used within a `block` to transfer control to the statement
of the block which is tagged with the argument to `go`.  To tag a
statement, precede it by an atomic argument as another statement in
the `block`.  For example:



```maxima
block ([x], x:1, loop, x+1, ..., go(loop), ...)
```


The argument to `go` must be the name of a tag appearing in the same
`block`.  One cannot use `go` to transfer to tag in a `block`
other than the one containing the `go`.

See also: `block`.

<!-- category: Programming -->
<!-- keywords: if -->
<!-- signatures: if -->
### Function: if

Represents conditional evaluation.  Various forms of `if` expressions are
recognized.


`if cond_1 then expr_1 else expr_0`
eva­lu­ates to *expr_1* if *cond_1* evaluates to `true`,
otherwise the expression evaluates to *expr_0*.


The command `if cond_1 then expr_1 elseif cond_2 then expr_2 elseif ... else expr_0` evaluates to *expr_k* if
*cond_k* is `true` and all preceding conditions are `false`.  If
none of the conditions are `true`, the expression evaluates to
`expr_0`.


A trailing `else false` is assumed if `else` is missing.  That is,
the command `if cond_1 then expr_1` is equivalent to
`if cond_1 then expr_1 else false`, and the command
`if cond_1 then expr_1 elseif ... elseif cond_n then expr_n` is equivalent to `if cond_1 then expr_1 elseif ... elseif cond_n then expr_n else false`.


The alternatives *expr_0*, ..., *expr_n* may be any Maxima
expressions, including nested `if` expressions.  The alternatives are
neither simplified nor evaluated unless the corresponding condition is
`true`.


The conditions *cond_1*, ..., *cond_n* are expressions which
potentially or actually evaluate to `true` or `false`.
When a condition does not actually evaluate to `true` or `false`,
the behavior of `if` is governed by the global flag `prederror`.
When `prederror` is `true`, it is an error if any evaluated condition
does not evaluate to `true` or `false`.  Otherwise, conditions which
do not evaluate to `true` or `false` are accepted, and the result is
a conditional expression.


Among other elements, conditions may comprise relational and logical operators
as follows.











| Operation | Symbol | Type |
| --- | --- | --- |
| less than | `<` | relational infix |
| less than or equal to | `<=` | relational infix |
| equality (syntactic) | `=` | relational infix |
| equality (value) | `equal` | relational function |
| negation of equal | `notequal` | relational function |
| greater than or equal to | `>=` | relational infix |
| greater than | `>` | relational infix |
| and | `and` | logical infix |
| or | `or` | logical infix |
| not | `not` | logical infix |

<!-- category: Programming -->
<!-- keywords: map -->
<!-- signatures: map(f, expr_1, ..., expr_n) -->
### Function: map (f, expr_1, ..., expr_n)

Returns an expression whose leading operator is the same as that of the
expressions *expr_1*, ..., *expr_n* but whose subparts are the
results of applying *f* to the corresponding subparts of the expressions.
*f* is either the name of a function of $n$ arguments or is a
`lambda` form of $n$ arguments.


`maperror` - if `false` will cause all of the mapping
functions to (1) stop when they finish going down the shortest
*expr_i* if not all of the *expr_i* are of the same length and
(2) apply *f* to [*expr_1*, *expr_2*, ...]  if the
*expr_i* are not all the same type of object.  If `maperror`
is `true` then an error message will be given in the above two
instances.


One of the uses of this function is to `map` a function (e.g.
`partfrac`) onto each term of a very large expression where it ordinarily
wouldn’t be possible to use the function on the entire expression due to an
exhaustion of list storage space in the course of the computation.


See also `scanmap`, `maplist`, `outermap`, `matrixmap` and `apply`.












```maxima
maxima

(%i1) map(f,x+a*y+b*z);
(%o1)                f(b z) + f(a y) + f(x)


(%i2) map(lambda([u],partfrac(u,x)),x+1/(x^3+4*x^2+5*x+2));
                    1       1        1
(%o2)             ----- - ----- + -------- + x
                  x + 2   x + 1          2
                                  (x + 1)


(%i3) map(ratsimp, x/(x^2+x)+(y^2+y)/y);
                                1
(%o3)                     y + ----- + 1
                              x + 1


(%i4) map("=",[a,b],[-0.5,3]);
(%o4)                  [a = - 0.5, b = 3]
```

See also: `maperror`, `partfrac`, `scanmap`, `maplist`, `outermap`, `matrixmap`, `apply`.

<!-- category: Programming -->
<!-- keywords: mapatom -->
<!-- signatures: mapatom(expr) -->
### Function: mapatom (expr)

Returns `true` if and only if *expr* is treated by the mapping
routines as an atom.  "Mapatoms" are atoms, numbers
(including rational numbers), subscripted variables and structure
references.

<!-- category: Programming -->
<!-- keywords: maperror -->
<!-- signatures: maperror -->
### Variable: maperror

Default value: `true`


When `maperror` is `false`, causes all of the mapping functions,
for example



```maxima
map (f, expr_1, expr_2, ...)
```


to (1) stop when they finish going down the shortest *expr_i* if
not all of the *expr_i* are of the same length and (2) apply
*f* to [*expr_1*, *expr_2*, ...] if the *expr_i* are
not all the same type of object.


If `maperror` is `true` then an error message
is displayed in the above two instances.

<!-- category: Programming -->
<!-- keywords: maplist -->
<!-- signatures: maplist(f, expr_1, ..., expr_n) -->
### Function: maplist (f, expr_1, ..., expr_n)

Returns a list of the applications of *f* to the parts of the expressions
*expr_1*, ..., *expr_n*.  *f* is the name of a function, or a
lambda expression.


`maplist` differs from `map(f, expr_1, ..., expr_n)`
which returns an expression with the same main operator as *expr_i* has
(except for simplifications and the case where `map` does an `apply`).

See also: `map`, `apply`.

<!-- category: Programming -->
<!-- keywords: mapprint -->
<!-- signatures: mapprint -->
### Variable: mapprint

Default value: `true`


When `mapprint` is `true`, various information messages from
`map`, `maplist`, and `fullmap` are produced in certain
situations.  These include situations where `map` would use
`apply`, or `map` is truncating on the shortest list.


If `mapprint` is `false`, these messages are suppressed.

See also: `map`, `maplist`, `fullmap`, `apply`, `mapprint`.

<!-- category: Programming -->
<!-- keywords: outermap -->
<!-- signatures: outermap(f, a_1, ..., a_n) -->
### Function: outermap (f, a_1, ..., a_n)

Applies the function *f* to each one of the elements of the outer product
*a_1* cross *a_2* ... cross *a_n*.


*f* is the name of a function of $n$ arguments or a lambda expression
of $n$ arguments.  Each argument *a_k* may be a list or nested list,
or a matrix, or any other kind of expression.


The `outermap` return value is a nested structure.  Let *x* be the
return value.  Then *x* has the same structure as the first list, nested
list, or matrix argument, `x[i_1]...[i_m]` has the same structure as
the second list, nested list, or matrix argument,
`x[i_1]...[i_m][j_1]...[j_n]` has the same structure as the third
list, nested list, or matrix argument, and so on, where *m*, *n*,
... are the numbers of indices required to access the elements of each
argument (one for a list, two for a matrix, one or more for a nested list).
Arguments which are not lists or matrices have no effect on the structure of
the return value.


Note that the effect of `outermap` is different from that of applying
*f* to each one of the elements of the outer product returned by
`cartesian_product`.  `outermap` preserves the structure of the
arguments in the return value, while `cartesian_product` does not.


`outermap` evaluates its arguments.


See also `map`, `maplist`, and `apply`.



Examples:


Elementary examples of `outermap`.
To show the argument combinations more clearly, `F` is left undefined.










```maxima
maxima

(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]


(%i2) outermap (F, matrix ([a, b], [c, d]), matrix ([1, 2], [3, 4]));
         [ [ F(a, 1)  F(a, 2) ]  [ F(b, 1)  F(b, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(a, 3)  F(a, 4) ]  [ F(b, 3)  F(b, 4) ] ]
(%o2)    [                                            ]
         [ [ F(c, 1)  F(c, 2) ]  [ F(d, 1)  F(d, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(c, 3)  F(c, 4) ]  [ F(d, 3)  F(d, 4) ] ]


(%i3) outermap (F, [a, b], x, matrix ([1, 2], [3, 4]));
       [ F(a, x, 1)  F(a, x, 2) ]  [ F(b, x, 1)  F(b, x, 2) ]
(%o3) [[                        ], [                        ]]
       [ F(a, x, 3)  F(a, x, 4) ]  [ F(b, x, 3)  F(b, x, 4) ]


(%i4) outermap (F, [a, b], matrix ([1, 2]), matrix ([x], [y]));
       [ [ F(a, 1, x) ]  [ F(a, 2, x) ] ]
(%o4) [[ [            ]  [            ] ], 
       [ [ F(a, 1, y) ]  [ F(a, 2, y) ] ]
                              [ [ F(b, 1, x) ]  [ F(b, 2, x) ] ]
                              [ [            ]  [            ] ]]
                              [ [ F(b, 1, y) ]  [ F(b, 2, y) ] ]


(%i5) outermap ("+", [a, b, c], [1, 2, 3]);
(%o5) [[a + 1, a + 2, a + 3], [b + 1, b + 2, b + 3], 
                                           [c + 1, c + 2, c + 3]]
```


A closer examination of the `outermap` return value.  The first, second,
and third arguments are a matrix, a list, and a matrix, respectively.
The return value is a matrix.
Each element of that matrix is a list,
and each element of each list is a matrix.















```maxima
maxima

(%i1) arg_1 :  matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]


(%i2) arg_2 : [11, 22];
(%o2)                       [11, 22]


(%i3) arg_3 : matrix ([xx, yy]);
(%o3)                      [ xx  yy ]


(%i4) xx_0 : outermap (lambda ([x, y, z], x / y + z), arg_1,
                                                   arg_2, arg_3);
               [  [      a        a  ]  [      a        a  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
(%o4)  Col 1 = [                                              ]
               [  [      c        c  ]  [      c        c  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
                 [  [      b        b  ]  [      b        b  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
         Col 2 = [                                              ]
                 [  [      d        d  ]  [      d        d  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]


(%i5) xx_1 : xx_0 [1][1];
           [      a        a  ]  [      a        a  ]
(%o5)     [[ xx + --  yy + -- ], [ xx + --  yy + -- ]]
           [      11       11 ]  [      22       22 ]


(%i6) xx_2 : xx_0 [1][1] [1];
                      [      a        a  ]
(%o6)                 [ xx + --  yy + -- ]
                      [      11       11 ]


(%i7) xx_3 : xx_0 [1][1] [1] [1][1];
                                  a
(%o7)                        xx + --
                                  11


(%i8) [op (arg_1), op (arg_2), op (arg_3)];
(%o8)                  [matrix, [, matrix]


(%i9) [op (xx_0), op (xx_1), op (xx_2)];
(%o9)                  [matrix, [, matrix]
```


`outermap` preserves the structure of the arguments in the return value,
while `cartesian_product` does not.










```maxima
maxima

(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]


(%i2) setify (flatten (%));
(%o2) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}


(%i3) map (lambda ([L], apply (F, L)),
                     cartesian_product ({a, b, c}, {1, 2, 3}));
(%o3) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}


(%i4) is (equal (%, %th (2)));
(%o4)                         true
```

See also: `cartesian_product`, `map`, `maplist`, `apply`.

<!-- category: Programming -->
<!-- keywords: prederror -->
<!-- signatures: prederror -->
### Variable: prederror

Default value: `false`


When `prederror` is `true`, an error message is displayed whenever the
predicate of an `if` statement or an `is` function fails to evaluate
to either `true` or `false`.


If `false`, `unknown` is returned instead in this case.


See also `is` and `maybe`.

See also: `is`, `maybe`.

<!-- category: Programming -->
<!-- keywords: return -->
<!-- signatures: return(value) -->
### Function: return (value)

May be used to exit explicitly from the current `block`, `while`,
`for` or `do` loop bringing its argument. It therefore can be compared
with the `return` statement found in other programming languages but it yields
one difference: In maxima only returns from the current block, not from the entire
function it was called in. In this aspect it more closely resembles the `break`
statement from C.
























```maxima
maxima

(%i1) for i:1 thru 10 do o:i;
(%o1)                         done


(%i2) for i:1 thru 10 do if i=3 then return(i);
(%o2)                           3


(%i3) for i:1 thru 10 do
    (
        block([i],
            i:3,
            return(i)
        ),
        return(8)
    );
(%o3)                           8


(%i4) block([i],
    i:4,
    block([o],
        o:5,
        return(o)
    ),
    return(i),
    return(10)
 );
(%o4)                           4
```



See also `for`, `while`, `do` and `block`.

See also: `block`, `while`, `for`, `do`.

<!-- category: Programming -->
<!-- keywords: scanmap -->
<!-- signatures: scanmap(f, expr), scanmap(f, expr, bottomup), scanmap(f, expr, topdown) -->
### Function: scanmap (f, expr)

Recursively applies *f* to *expr*, in a top
down manner.  This is most useful when complete factorization is
desired, for example:







```maxima
maxima
(%i1) exp:(a^2+2*a+1)*y + x^2$

(%i2) scanmap(factor,exp);
                                2      2
(%o2)                    (a + 1)  y + x
```


Note the way in which `scanmap` applies the given function
`factor` to the constituent subexpressions of *expr*; if
another form of *expr* is presented to `scanmap` then the
result may be different.  Thus, `%o2` is not recovered when
`scanmap` is applied to the expanded form of `exp`:






```maxima
maxima

(%i1) scanmap(factor,expand(exp));
(%o1)                          exp
```


Here is another example of the way in which `scanmap` recursively
applies a given function to all subexpressions, including exponents:







```maxima
maxima
(%i1) expr : u*v^(a*x+b) + c$

(%i2) scanmap('f, expr);
                        f(f(f(a) f(x)) + f(b))
(%o2)    f(f(f(u) f(f(v)                      )) + f(c))
```


`scanmap (f, expr, bottomup)` applies *f* to *expr* in a
bottom-up manner.  E.g., for undefined `f`,



```maxima
scanmap(f,a*x+b) ->
   f(a*x+b) -> f(f(a*x)+f(b)) -> f(f(f(a)*f(x))+f(b))
scanmap(f,a*x+b,bottomup) -> f(a)*f(x)+f(b)
    -> f(f(a)*f(x))+f(b) ->
     f(f(f(a)*f(x))+f(b))
```


In this case, you get the same answer both
ways.


`scanmap (f, expr, topdown)` has the same effect as calling
`scanmap (f, expr)`.

<!-- category: Programming -->
<!-- keywords: throw -->
<!-- signatures: throw(expr) -->
### Function: throw (expr)

Evaluates *expr* and throws the value back to the most recent
`catch`.  `throw` is used with `catch` as a nonlocal return
mechanism.

See also: `catch`.

<!-- category: Programming -->
<!-- keywords: warning -->
<!-- signatures: warning(expr_1, ..., expr_n) -->
### Function: warning (expr_1, ..., expr_n)

Evaluates and prints *expr_1*, ..., *expr_n*,
as a warning message that is formatted in a standard way so a maxima front-end
may be able to recognize the warning and to format it accordingly.


The function `warning` always returns false.

