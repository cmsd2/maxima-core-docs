## Function Definition

### Function: apply (F, arg_1, ..., arg_n)

Constructs and evaluates an expression `F(arg_1, ..., arg_n)`.
The function arguments `[arg_1, ..., arg_n]` may
be of any length and comprise any expressions.
`apply` evaluates all of its arguments, *F* and *arg_1*, ..., *arg_n* alike,
unless evaluation is prevented by quotation.


`apply` does not attempt to distinguish a `memoizing function` from an ordinary 
function; when *F* is the name of a memoizing function, `apply` evaluates
`F(...)` (that is, a function call with parentheses instead of square
brackets).  `arrayapply` evaluates a function call with square brackets in
this case.


See also `funmake` and `args`.


Examples:


The function arguments `[arg_1, ..., arg_n]` may be of any length.
Here `min` and `"+"` are applied to a list `L`.








```maxima
maxima

(%i1) L : [1, 5, -10.2, 4, 3];
(%o1)                 [1, 5, - 10.2, 4, 3]


(%i2) apply (min, L);
(%o2)                        - 10.2


(%i3) apply ("+", L);
(%o3)                  2.8000000000000007
```


`apply` evaluates all of its arguments, unless evaluation is prevented by quotation.
First example: `dispfun` ordinarily does not evaluate its argument,
but we can ensure the evaluation of the argument via `apply`.









fundef: no such function: fname
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) F (x) := x / 1729;
                                   x
(%o1)                     F(x) := ----
                                  1729


(%i2) fname : F;
(%o2)                           F


(%i3) dispfun (F);
                                   x
(%t3)                     F(x) := ----
                                  1729

(%o3)                         [%t3]

(%i4) dispfun (fname);

(%i5) apply (dispfun, [fname]);
                                   x
(%t5)                     F(x) := ----
                                  1729

(%o5)                         [%t5]
```


`apply` evaluates all of its arguments, unless evaluation is prevented by quotation.
Second example: create a function that declares all of its arguments to be complex.








```maxima
maxima
(%i1) g([u]):=apply('declare,[u,complex])$
(%i2) g(a,b,c)$

(%i3) facts();
(%o3) [kind(a, complex), kind(b, complex), kind(c, complex)]
```


`apply` evaluates all of its arguments, unless evaluation is prevented by quotation.
Third example: `apply` ordinarily evaluates its first argument,
but single quote `'` prevents evaluation.
Note that `demoivre` is the name of a global variable and also a function.








apply: found false where a function was expected.
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) demoivre;
(%o1)                         false


(%i2) demoivre (exp (%i * x));
(%o2)                  %i sin(x) + cos(x)

(%i3) apply (demoivre, [exp (%i * x)]);

(%i4) apply ('demoivre, [exp (%i * x)]);
(%o4)                  %i sin(x) + cos(x)
```


The function arguments `[arg_1, ..., arg_n]` may
be of any length and comprise any expressions.
Convert a nested list into a matrix by calling `apply`.







```maxima
maxima

(%i1) a:[[1,2],[3,4]];
(%o1)                   [[1, 2], [3, 4]]


(%i2) apply(matrix,a);
                            [ 1  2 ]
(%o2)                       [      ]
                            [ 3  4 ]
```

See also: `memoizing-function`, `funmake`, `args`.

### Function: block (block, v_1, ..., v_m, expr_1, ..., expr_n, block, expr_1, ..., expr_n)

The function `block` allows to make the variables *v_1*, ...,
*v_m* to be local for a sequence of commands. If these variables
are already bound `block` saves the current values of the
variables *v_1*, ..., *v_m* (if any) upon entry to the
block, then unbinds the variables so that they evaluate to themselves;
The local variables may be bound to arbitrary values within the block
but when the block is exited the saved values are restored, and the
values assigned within the block are lost.


If there is no need to define local variables then the list at the
beginning of the `block` command may be omitted.
In this case if neither `return` nor `go` are used
`block` behaves similar to the following construct:



```maxima
maxima
( expr_1, expr_2,... , expr_n );
```


*expr_1*, ..., *expr_n* will be evaluated in sequence and
the value of the last expression will be returned. The sequence can be 
modified by the `go`, `throw`, and `return` functions.  The last
expression is *expr_n* unless `return` or an expression containing
`throw` is evaluated.


The declaration `local(v_1, ..., v_m)` within `block`
saves the properties associated with the symbols *v_1*, ..., *v_m*,
removes any properties before evaluating other expressions, and restores any
saved properties on exit from the block.  Some declarations are implemented as
properties of a symbol, including `:=`, `array`, `dependencies`,
`atvalue`, `matchdeclare`, `atomgrad`, `constant`,
`nonscalar`, `assume`, and some others.  The effect of `local`
is to make such declarations effective only within the block; otherwise
declarations within a block are actually global declarations.


`block` may appear within another `block`.
Local variables are established each time a new `block` is evaluated.
Local variables appear to be global to any enclosed blocks.
If a variable is non-local in a block,
its value is the value most recently assigned by an enclosing block, if any,
otherwise, it is the value of the variable in the global environment.
This policy may coincide with the usual understanding of "dynamic scope".


The value of the block is the value of the last statement or the
value of the argument to the function `return` which may be used to exit
explicitly from the block. The function `go` may be used to transfer
control to the statement of the block that is tagged with the argument
to `go`.  To tag a statement, precede it by an atomic argument as
another statement in the block.  For example:
`block ([x], x:1, loop, x: x+1, ..., go(loop), ...)`.  The argument to
`go` must be the name of a tag appearing within the block.  One cannot use
`go` to transfer to a tag in a block other than the one containing the
`go`.


Blocks typically appear on the right side of a function definition
but can be used in other places as well.


See also `return` and `go`.

See also: `return`, `go`.

### Function: break (expr_1, ..., expr_n)

Evaluates and prints *expr_1*, ..., *expr_n* and then
causes a Maxima break at which point the user can examine and change
his environment.  Upon typing `exit;` the computation resumes.

### Function: buildq (L, expr)

Substitutes variables named by the list *L* into the expression *expr*,
in parallel, without evaluating *expr*.  The resulting expression is
simplified, but not evaluated, after `buildq` carries out the substitution.


The elements of *L* are symbols or assignment expressions
`symbol: value`, evaluated in parallel.  That is, the binding
of a variable on the right-hand side of an assignment is the binding of that
variable in the context from which `buildq` was called, not the binding of
that variable in the variable list *L*.  If some variable in *L* is not
given an explicit assignment, its binding in `buildq` is the same as in
the context from which `buildq` was called.


Then the variables named by *L* are substituted into *expr* in parallel.
That is, the substitution for every variable is determined before any
substitution is made, so the substitution for one variable has no effect on any
other.


If any variable *x* appears as `splice (x)` in *expr*,
then *x* must be bound to a list,
and the list is spliced (interpolated) into *expr* instead of substituted.


Any variables in *expr* not appearing in *L* are carried into the result
verbatim, even if they have bindings in the context from which `buildq`
was called.


Examples


`a` is explicitly bound to `x`, while `b` has the same binding
(namely 29) as in the calling context, and `c` is carried through verbatim.
The resulting expression is not evaluated until the explicit evaluation
`''%`.








```maxima
maxima
(%i1) (a: 17, b: 29, c: 1729)$

(%i2) buildq ([a: x, b], a + b + c);
(%o2)                      x + c + 29


(%i3) ''%;
(%o3)                       x + 1758
```


`e` is bound to a list, which appears as such in the arguments of
`foo`, and interpolated into the arguments of `bar`.







```maxima
maxima

(%i1) buildq ([e: [a, b, c]], foo (x, e, y));
(%o1)                 foo(x, [a, b, c], y)


(%i2) buildq ([e: [a, b, c]], bar (x, splice (e), y));
(%o2)                  bar(x, a, b, c, y)
```


The result is simplified after substitution.  If simplification were applied
before substitution, these two results would be the same.







```maxima
maxima

(%i1) buildq ([e: [a, b, c]], splice (e) + splice (e));
(%o1)                    2 c + 2 b + 2 a


(%i2) buildq ([e: [a, b, c]], 2 * splice (e));
(%o2)                        2 a b c
```


The variables in *L* are bound in parallel; if bound sequentially,
the first result would be `foo (b, b)`.
Substitutions are carried out in parallel;
compare the second result with the result of `subst`,
which carries out substitutions sequentially.










```maxima
maxima

(%i1) buildq ([a: b, b: a], foo (a, b));
(%o1)                       foo(b, a)


(%i2) buildq ([u: v, v: w, w: x, x: y, y: z, z: u],
              bar (u, v, w, x, y, z));
(%o2)                 bar(v, w, x, y, z, u)


(%i3) subst ([u=v, v=w, w=x, x=y, y=z, z=u],
             bar (u, v, w, x, y, z));
(%o3)                 bar(u, u, u, u, u, u)
```


Construct a list of equations with some variables or expressions on the
left-hand side and their values on the right-hand side.  `macroexpand`
shows the expression returned by `show_values`.









```maxima
maxima

(%i1) show_values ([L]) ::= buildq ([L], map ("=", 'L, L));
(%o1)   show_values([L]) ::= buildq([L], map("=", 'L, L))

(%i2) (a: 17, b: 29, c: 1729)$

(%i3) show_values (a, b, c - a - b);
(%o3)          [a = 17, b = 29, c - b - a = 1683]


(%i4) macroexpand (show_values (a, b, c - a - b));
(%o4)    map(=, '([a, b, c - b - a]), [a, b, c - b - a])
```


Given a function of several arguments,
create another function for which some of the arguments are fixed.









```maxima
maxima

(%i1) curry (f, [a]) :=
        buildq ([f, a], lambda ([[x]], apply (f, append (a, x))))$


(%i2) by3 : curry ("*", 3);
(%o2)        lambda([[x]], apply(*, append([3], x)))


(%i3) by3 (a + b);
(%o3)                       3 (b + a)
```

### Function: catch (expr_1, ..., expr_n)

Evaluates *expr_1*, ..., *expr_n* one by one; if any
leads to the evaluation of an expression of the
form `throw (arg)`, then the value of the `catch` is the value of
`throw (arg)`, and no further expressions are evaluated.
This "non-local return" thus goes through any depth of
nesting to the nearest enclosing `catch`.  If there is no `catch`
enclosing a `throw`, an error message is printed.


If the evaluation of the arguments does not lead to the evaluation of any
`throw` then the value of `catch` is the value of *expr_n*.









```maxima
maxima
(%i1) lambda ([x], if x < 0 then throw(x) else f(x))$
(%i2) g(l) := catch (map (''%, l))$

(%i3) g ([1, 2, 3, 7]);
(%o3)               [f(1), f(2), f(3), f(7)]


(%i4) g ([1, 2, -3, 7]);
(%o4)                          - 3
```



The function `g` returns a list of `f` of each element of `l` if
`l` consists only of non-negative numbers; otherwise, `g` "catches"
the first negative element of `l` and "throws" it up.

### Function: compfile (compfile, filename, f_1, ..., f_n, compfile, filename, functions, compfile, filename, all)

Translates Maxima functions into Lisp and writes the translated code into the
file *filename*.


`compfile(filename, f_1, ..., f_n)` translates the
specified functions.  `compfile (filename, functions)` and
`compfile (filename, all)` translate all user-defined functions.


The Lisp translations are not evaluated, nor is the output file processed by
the Lisp compiler.

`translate` creates and evaluates Lisp translations.  `compile_file`
translates Maxima into Lisp, and then executes the Lisp compiler.


See also `translate`, `translate_file`, and `compile_005ffile`.

See also: `translate`, `translate_file`, `compile_file`.

### Function: compile (compile, f_1, ..., f_n, compile, functions, compile, all)

Translates Maxima functions *f_1*, ..., *f_n* into Lisp, evaluates
the Lisp translations, and calls the Lisp function `COMPILE` on each
translated function.  `compile` returns a list of the names of the
compiled functions.


`compile (all)` or `compile (functions)` compiles all user-defined
functions.


`compile` quotes its arguments; 
the quote-quote operator `''` defeats quotation.


Compiling a function to native code can mean a big increase in speed and might 
cause the memory footprint to reduce drastically.
Code tends to be especially effective when the flexibility it needs to provide
is limited. If compilation doesn’t provide the speed that is needed a few ways
to limit the code’s functionality are the following:


- * 
If the function accesses global variables the complexity of the function
      can be drastically be reduced by limiting these variables to one data type,
      for example using `mode_declare` or a statement like the following one:
      `put(x_1, bigfloat, numerical_type)`
- * 
The compiler might warn about undeclared variables if text could either be
      a named option to a command or (if they are assigned a value to) the name
      of a variable. Prepending the option with a single quote `'`
      tells the compiler that the text is meant as an option.

See also: `mode_declare`.

### Function: compile_file (compile_file, filename, compile_file, filename, compiled_filename, compile_file, filename, compiled_filename, lisp_filename)

Translates the Maxima file *filename* into Lisp, and executes the Lisp compiler.
The compiled code is not loaded into Maxima.


`compile_file` returns a list of the names of four files: the original
Maxima file, the Lisp translation, notes on translation, and the compiled code.
If the compilation fails, the fourth item is `false`.


Some declarations and definitions take effect as soon
as the Lisp code is compiled (without loading the compiled code).
These include functions defined with the `:=` operator,
macros define with the `::=` operator,

`alias`, `declare`,
`define_variable`,  `mode_declare`,
and 
`infix`, `matchfix`,
`nofix`, `postfix`, `prefix`,
and `compfile`.


Assignments and function calls are not evaluated until the compiled code is
loaded.  In particular, within the Maxima file, assignments to the translation
flags (`tr_numer`, etc.) have no effect on the translation.







*filename* may not contain `:lisp` statements.


`compile_file` evaluates its arguments.

### Function: declare_translated (f_1, f_2, ...)

When translating a file of Maxima code
to Lisp, it is important for the translator to know which functions it
sees in the file are to be called as translated or compiled functions,
and which ones are just Maxima functions or undefined.  Putting this
declaration at the top of the file, lets it know that although a symbol
does which does not yet have a Lisp function value, will have one at
call time.  `(MFUNCTION-CALL fn arg1 arg2 ...)` is generated when
the translator does not know `fn` is going to be a Lisp function.

### Function: define (define, f, x_1, ..., x_n, expr, define, f, x_1, ..., x_n, expr, define, f, x_1, ..., x_n, y_1, ..., y_m, expr, define, funmake, f, x_1, ..., x_n, expr, define, arraymake, f, x_1, ..., x_n, expr, define, ev, expr_1, expr_2)

Defines a function named *f* with arguments *x_1*, ..., *x_n*
and function body *expr*.  `define` always evaluates its second
argument (unless explicitly quoted).  The function so defined may be an ordinary
Maxima function (with arguments enclosed in parentheses) or a `memoizing function`
(with arguments enclosed in square brackets).


When the last or only function argument *x_n* is a list of one element,
the function defined by `define` accepts a variable number of arguments.
Actual arguments are assigned one-to-one to formal arguments *x_1*, ...,
*x_(n - 1)*, and any further actual arguments, if present, are assigned to
*x_n* as a list.


When the first argument of `define` is an expression of the form
`f(x_1, ..., x_n)` or `f[x_1, ..., x_n]`, the function arguments are evaluated but *f* is not evaluated,
even if there is already a function or variable by that name.


When the first argument is an expression with operator `funmake`,
`arraymake`, or `ev`, the first argument is evaluated;
this allows for the function name to be computed, as well as the body.


All function definitions appear in the same namespace; defining a function
`f` within another function `g` does not automatically limit the scope
of `f` to `g`.  However, `local(f)` makes the definition of
function `f` effective only within the block or other compound expression
in which `local` appears.


If some formal argument *x_k* is a quoted symbol (after evaluation), the
function defined by `define` does not evaluate the corresponding actual
argument.  Otherwise all actual arguments are evaluated.


See also `:=` and `_003a_003a_003d`.


Examples:


`define` always evaluates its second argument (unless explicitly quoted).










```maxima
maxima

(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)


(%i2) define (F1 (x, y), expr);
(%o2)              F1(x, y) := cos(y) - sin(x)


(%i3) F1 (a, b);
(%o3)                    cos(b) - sin(a)


(%i4) F2 (x, y) := expr;
(%o4)                   F2(x, y) := expr


(%i5) F2 (a, b);
(%o5)                    cos(y) - sin(x)
```


The function defined by `define` may be an ordinary Maxima function or a
`memoizing function`.







```maxima
maxima

(%i1) define (G1 (x, y), x.y - y.x);
(%o1)               G1(x, y) := x . y - y . x


(%i2) define (G2 [x, y], x.y - y.x);
(%o2)                G2     := x . y - y . x
                       x, y
```


When the last or only function argument *x_n* is a list of one element,
the function defined by `define` accepts a variable number of arguments.







```maxima
maxima

(%i1) define (H ([L]), '(apply ("+", L)));
(%o1)                H([L]) := apply("+", L)


(%i2) H (a, b, c);
(%o2)                       c + b + a
```


When the first argument is an expression with operator `funmake`,
`arraymake`, or `ev`, the first argument is evaluated.











```maxima
maxima

(%i1) [F : I, u : x];
(%o1)                        [I, x]


(%i2) funmake (F, [u]);
(%o2)                         I(x)


(%i3) define (funmake (F, [u]), cos(u) + 1);
(%o3)                  I(x) := cos(x) + 1


(%i4) define (arraymake (F, [u]), cos(u) + 1);
(%o4)                   I  := cos(x) + 1
                         x


(%i5) define (foo (x, y), bar (y, x));
(%o5)                foo(x, y) := bar(y, x)


(%i6) define (ev (foo (x, y)), sin(x) - cos(y));
(%o6)             bar(y, x) := sin(x) - cos(y)
```

See also: `memoizing-function`, `:=`, `::=`.

### Function: define_variable (name, default_value, mode)

Introduces a global variable into the Maxima environment.
`define_variable` is useful in user-written packages, which are often
translated or compiled as it gives the compiler hints of the type (“mode”)
of a variable and therefore avoids requiring it to generate generic code that
can deal with every variable being an integer, float, maxima object, array etc.


`define_variable` carries out the following steps:



1. `mode_declare (name, mode)` declares the mode (“type”) of
*name* to the translator which can considerably speed up compiled code as
it allows having to create generic code. See `mode_declare` for a list of
the possible modes.
2. If the variable is unbound, *default_value* is assigned to *name*.
3. Associates *name* with a test function
to ensure that *name* is only assigned values of the declared mode.















The `value_check` property can be assigned to any variable which has been
defined via `define_variable` with a mode other than `any`.
The `value_check` property is a lambda expression or the name of a function
of one variable, which is called when an attempt is made to assign a value to
the variable.  The argument of the `value_check` function is the would-be
assigned value.


`define_variable` evaluates `default_value`, and quotes `name`
and `mode`.  `define_variable` returns the current value of
`name`, which is `default_value` if `name` was unbound before,
and otherwise it is the previous value of `name`.


Examples:


`foo` is a Boolean variable, with the initial value `true`.









translator: foo was declared with mode boolean
                                          , but it has value: %pi
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) define_variable (foo, true, boolean);
(%o1)                         true


(%i2) foo;
(%o2)                         true


(%i3) foo: false;
(%o3)                         false

(%i4) foo: %pi;

(%i5) foo;
(%o5)                         false
```


`bar` is an integer variable, which must be prime.











1440 is not prime.
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) define_variable (bar, 2, integer);
(%o1)                           2


(%i2) qput (bar, prime_test, value_check);
(%o2)                      prime_test


(%i3) prime_test (y) := if not primep(y) then
                           error (y, "is not prime.");
(%o3) prime_test(y) := if not primep(y)
                                   then error(y, "is not prime.")


(%i4) bar: 1439;
(%o4)                         1439


(%i5) bar: 1440;
#0: prime_test(y=1440)


(%i6) bar;
(%o6)                         1439
```


`baz_quux` is a variable which cannot be assigned a value.
The mode `any_check` is like `any`, but `any_check` enables the
`value_check` mechanism, and `any` does not.











Cannot assign to ‘baz_quux’.
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) define_variable (baz_quux, 'baz_quux, any_check);
(%o1)                       baz_quux


(%i2) F: lambda ([y], if y # 'baz_quux then
                 error ("Cannot assign to `baz_quux'."));
(%o2) lambda([y], if y # 'baz_quux
                        then error(Cannot assign to `baz_quux'.))


(%i3) qput (baz_quux, ''F, value_check);
(%o3) lambda([y], if y # 'baz_quux
                        then error(Cannot assign to `baz_quux'.))


(%i4) baz_quux: 'baz_quux;
(%o4)                       baz_quux


(%i5) baz_quux: sqrt(2);
#0: lambda([y],if y # 'baz_quux then error("Cannot assign to `baz_quux'."))(y=sqrt(2))


(%i6) baz_quux;
(%o6)                       baz_quux
```

See also: `mode_declare`.

### Function: dispfun (dispfun, f_1, ..., f_n, dispfun, all)

Displays the definition of the user-defined functions *f_1*, ...,
*f_n*.  Each argument may be the name of a macro (defined with `::=`),
an ordinary function (defined with `:=` or `define`), an array
function (defined with `:=` or `define`, but enclosing arguments in
square brackets `[ ]`), a subscripted function (defined with `:=` or
`define`, but enclosing some arguments in square brackets and others in
parentheses `( )`), one of a family of subscripted functions selected by a
particular subscript value, or a subscripted function defined with a constant
subscript.


`dispfun (all)` displays all user-defined functions as
given by the `functions`, `arrays`, and `macros` lists,
omitting subscripted functions defined with constant subscripts.


`dispfun` creates an intermediate expression label
(`%t1`, `%t2`, etc.)
for each displayed function, and assigns the function definition to the label.
In contrast, `fundef` returns the function definition.


`dispfun` quotes its arguments; the quote-quote operator `''`
defeats quotation.  `dispfun` returns the list of intermediate expression
labels corresponding to the displayed functions.


Examples:












```maxima
maxima

(%i1) m(x, y) ::= x^(-y);
                                     - y
(%o1)                   m(x, y) ::= x


(%i2) f(x, y) :=  x^(-y);
                                     - y
(%o2)                    f(x, y) := x


(%i3) g[x, y] :=  x^(-y);
                                    - y
(%o3)                     g     := x
                           x, y


(%i4) h[x](y) :=  x^(-y);
                                    - y
(%o4)                     h (y) := x
                           x


(%i5) i[8](y) :=  8^(-y);
                                    - y
(%o5)                     i (y) := 8
                           8


(%i6) dispfun (m, f, g, h, h[5], h[10], i[8]);
                                     - y
(%t6)                   m(x, y) ::= x

                                     - y
(%t7)                    f(x, y) := x

                                    - y
(%t8)                     g     := x
                           x, y

                                    - y
(%t9)                     h (y) := x
                           x

                                    1
(%t10)                     h (y) := --
                            5        y
                                    5

                                     1
(%t11)                    h  (y) := ---
                           10         y
                                    10

                                    - y
(%t12)                    i (y) := 8
                           8

(%o12)       [%t6, %t7, %t8, %t9, %t10, %t11, %t12]


(%i13) ''%;
                     - y              - y            - y
(%o13) [m(x, y) ::= x   , f(x, y) := x   , g     := x   , 
                                            x, y
                  - y           1              1             - y
        h (y) := x   , h (y) := --, h  (y) := ---, i (y) := 8   ]
         x              5        y   10         y   8
                                5             10
```

### Function: fullmap (f, expr_1, ...)

Similar to `map`, but `fullmap` keeps mapping down all subexpressions
until the main operators are no longer the same.


`fullmap` is used by the Maxima simplifier for certain matrix
manipulations; thus, Maxima sometimes generates an error message concerning
`fullmap` even though `fullmap` was not explicitly called by the user.


Examples:








```maxima
maxima

(%i1) a + b * c;
(%o1)                        b c + a


(%i2) fullmap (g, %);
(%o2)                   g(b) g(c) + g(a)


(%i3) map (g, %th(2));
(%o3)                     g(b c) + g(a)
```

### Function: fullmapl (f, list_1, ...)

Similar to `fullmap`, but `fullmapl` only maps onto lists and
matrices.


Example:






```maxima
maxima

(%i1) fullmapl ("+", [3, [4, 5]], [[a, 1], [0, -1.5]]);
(%o1)                [[a + 3, 4], [4, 3.5]]
```

### Variable: functions

Default value: `[]`


`functions` is the list of ordinary Maxima functions
in the current session.
An ordinary function is a function constructed by
`define` or `:=` and called with parentheses `()`.
A function may be defined at the Maxima prompt
or in a Maxima file loaded by `load` or `batch`.


`Memoizing functions` (called with square brackets, e.g., `F[x]`) and subscripted
functions (called with square brackets and parentheses, e.g., `F[x](y)`)
are listed by the global variable `arrays`, and not by `functions`.


Lisp functions are not kept on any list.


Examples:














```maxima
maxima

(%i1) F_1 (x) := x - 100;
(%o1)                   F_1(x) := x - 100


(%i2) F_2 (x, y) := x / y;
                                      x
(%o2)                    F_2(x, y) := -
                                      y


(%i3) define (F_3 (x), sqrt (x));
(%o3)                   F_3(x) := sqrt(x)


(%i4) G_1 [x] := x - 100;
(%o4)                    G_1  := x - 100
                            x


(%i5) G_2 [x, y] := x / y;
                                     x
(%o5)                     G_2     := -
                             x, y    y


(%i6) define (G_3 [x], sqrt (x));
(%o6)                    G_3  := sqrt(x)
                            x


(%i7) H_1 [x] (y) := x^y;
                                      y
(%o7)                     H_1 (y) := x
                             x


(%i8) functions;
(%o8)              [F_1(x), F_2(x, y), F_3(x)]


(%i9) arrays;
(%o9)                 [G_1, G_2, G_3, H_1]
```

See also: `Memoizing-functions`.

### Function: fundef (f)

Returns the definition of the function *f*.


The argument may be


- * 
the name of a macro (defined with `::=`),
- * 
an ordinary function (defined with `:=` or `define`),
- * 
a `memoizing function` (defined with `:=` or `define`, but enclosing arguments in square brackets `[ ]`),
- * 
a subscripted function (defined with `:=` or `define`,
but enclosing some arguments in square brackets and others in parentheses
`( )`),
- * 
one of a family of subscripted functions selected by a particular
subscript value,
- * 
or a subscripted function defined with a constant subscript.


`fundef` quotes its argument;
the quote-quote operator `''` defeats quotation.


`fundef (f)` returns the definition of *f*.
In contrast, `dispfun (f)` creates an intermediate expression label
and assigns the definition to the label.

See also: `memoizing-function`.

### Function: funmake (F, arg_1, ..., arg_n)

Returns an expression `F(arg_1, ..., arg_n)`.
The return value is simplified, but not evaluated,
so the function *F* is not called, even if it exists.


`funmake` does not attempt to distinguish `memoizing functions` from ordinary 
functions; when *F* is the name of a memoizing function,
`funmake` returns `F(...)`
(that is, a function call with parentheses instead of square brackets).
`arraymake` returns a function call with square brackets in this case.


`funmake` evaluates its arguments.


See also `apply` and `args`.


Examples:


`funmake` applied to an ordinary Maxima function.








```maxima
maxima

(%i1) F (x, y) := y^2 - x^2;
                                   2    2
(%o1)                  F(x, y) := y  - x


(%i2) funmake (F, [a + 1, b + 1]);
(%o2)                    F(a + 1, b + 1)


(%i3) ''%;
                              2          2
(%o3)                  (b + 1)  - (a + 1)
```


`funmake` applied to a macro.








```maxima
maxima

(%i1) G (x) ::= (x - 1)/2;
                                  x - 1
(%o1)                    G(x) ::= -----
                                    2


(%i2) funmake (G, [u]);
(%o2)                         G(u)


(%i3) ''%;
                              u - 1
(%o3)                         -----
                                2
```


`funmake` applied to a subscripted function.










```maxima
maxima

(%i1) H [a] (x) := (x - 1)^a;
                                        a
(%o1)                   H (x) := (x - 1)
                         a


(%i2) funmake (H [n], [%e]);
                                       n
(%o2)               lambda([x], (x - 1) )(%e)


(%i3) ''%;
                                    n
(%o3)                       (%e - 1)


(%i4) funmake ('(H [n]), [%e]);
(%o4)                        H (%e)
                              n


(%i5) ''%;
                                    n
(%o5)                       (%e - 1)
```


`funmake` applied to a symbol which is not a defined function of any kind.







```maxima
maxima

(%i1) funmake (A, [u]);
(%o1)                         A(u)


(%i2) ''%;
(%o2)                         A(u)
```


`funmake` evaluates its arguments, but not the return value.










```maxima
maxima

(%i1) det(a,b,c) := b^2 -4*a*c;
                                    2
(%o1)              det(a, b, c) := b  - 4 a c


(%i2) (x : 8, y : 10, z : 12);
(%o2)                          12


(%i3) f : det;
(%o3)                          det


(%i4) funmake (f, [x, y, z]);
(%o4)                    det(8, 10, 12)


(%i5) ''%;
(%o5)                         - 284
```


Maxima simplifies `funmake`’s return value.






```maxima
maxima

(%i1) funmake (sin, [%pi / 2]);
(%o1)                           1
```

See also: `memoizing-functions`, `apply`, `args`.

### Function: lambda (lambda, x_1, ..., x_m, expr_1, ..., expr_n, lambda, L, expr_1, ..., expr_n, lambda, x_1, ..., x_m, L, expr_1, ..., expr_n)

Defines and returns a lambda expression (that is, an anonymous function).
The function may have required arguments *x_1*, ..., *x_m* and/or
optional arguments *L*, which appear within the function body as a list.
The return value of the function is *expr_n*.  A lambda expression can be
assigned to a variable and evaluated like an ordinary function.  A lambda
expression may appear in some contexts in which a function name is expected.


When the function is evaluated, unbound local variables *x_1*, ...,
*x_m* are created.  `lambda` may appear within `block` or another
`lambda`; local variables are established each time another `block` or
`lambda` is evaluated.  Local variables appear to be global to any enclosed
`block` or `lambda`.  If a variable is not local, its value is the
value most recently assigned in an enclosing `block` or `lambda`, if
any, otherwise, it is the value of the variable in the global environment.
This policy may coincide with the usual understanding of "dynamic scope".


After local variables are established, *expr_1* through *expr_n* are
evaluated in turn.  The special variable `%%`, representing the value of
the preceding expression, is recognized.  `throw` and `catch` may also
appear in the list of expressions.


`return` cannot appear in a lambda expression unless enclosed by
`block`, in which case `return` defines the return value of the block
and not of the lambda expression, unless the block happens to be *expr_n*.
Likewise, `go` cannot appear in a lambda expression unless enclosed by
`block`.


`lambda` quotes its arguments; 
the quote-quote operator `''` defeats quotation.


Examples:



- *
A lambda expression can be assigned to a variable and evaluated like an ordinary
function.







```maxima
maxima

(%i1) f: lambda ([x], x^2);
                                      2
(%o1)                    lambda([x], x )


(%i2) f(a);
                                2
(%o2)                          a
```



- *
A lambda expression may appear in contexts in which a function evaluation is expected.








```maxima
maxima

(%i1) lambda ([x], x^2) (a);
                                2
(%o1)                          a


(%i2) apply (lambda ([x], x^2), [a]);
                                2
(%o2)                          a


(%i3) map (lambda ([x], x^2), [a, b, c, d, e]);
                        2   2   2   2   2
(%o3)                 [a , b , c , d , e ]
```



- *
Argument variables are local variables.
Other variables appear to be global variables.
Global variables are evaluated at the time the lambda expression is evaluated,
unless some special evaluation is forced by some means, such as `''`.













```maxima
maxima
(%i1) a: %pi$
(%i2) b: %e$

(%i3) g: lambda ([a], a*b);
(%o3)                   lambda([a], a b)

(%i4) b: %gamma$

(%i5) g(1/2);
                             %gamma
(%o5)                        ------
                               2


(%i6) g2: lambda ([a], a*''b);
(%o6)                 lambda([a], a %gamma)

(%i7) b: %e$

(%i8) g2(1/2);
                             %gamma
(%o8)                        ------
                               2
```



- *
Lambda expressions may be nested.  Local variables within the outer lambda
expression appear to be global to the inner expression unless masked by local
variables of the same names.







```maxima
maxima

(%i1) h: lambda ([a, b], h2: lambda ([a], a*b), h2(1/2));
                                                   1
(%o1)     lambda([a, b], h2 : lambda([a], a b), h2(-))
                                                   2


(%i2) h(%pi, %gamma);
                             %gamma
(%o2)                        ------
                               2
```



- *
Since `lambda` quotes its arguments, lambda expression `i` below does
not define a "multiply by `a`" function.  Such a function can be defined
via `buildq`, as in lambda expression `i2` below.










```maxima
maxima

(%i1) i: lambda ([a], lambda ([x], a*x));
(%o1)             lambda([a], lambda([x], a x))


(%i2) i(1/2);
(%o2)                   lambda([x], a x)


(%i3) i2: lambda([a], buildq([a: a], lambda([x], a*x)));
(%o3)    lambda([a], buildq([a : a], lambda([x], a x)))


(%i4) i2(1/2);
                                    1
(%o4)                  lambda([x], (-) x)
                                    2


(%i5) i2(1/2)(%pi);
                               %pi
(%o5)                          ---
                                2
```



- *
A lambda expression may take a variable number of arguments,
which are indicated by `[L]` as the sole or final argument.
The arguments appear within the function body as a list.









```maxima
maxima

(%i1) f : lambda ([aa, bb, [cc]], aa * cc + bb);
(%o1)          lambda([aa, bb, [cc]], aa cc + bb)


(%i2) f (foo, %i, 17, 29, 256);
(%o2)       [17 foo + %i, 29 foo + %i, 256 foo + %i]


(%i3) g : lambda ([[aa]], apply ("+", aa));
(%o3)             lambda([[aa]], apply(+, aa))


(%i4) g (17, 29, x, y, z, %e);
(%o4)                  z + y + x + %e + 46
```

### Function: local (v_1, ..., v_n)

Saves the properties associated with the symbols *v_1*, ..., *v_n*,
removes any properties before evaluating other expressions,
and restores any saved properties on exit
from the block or other compound expression in which `local` appears.


Some declarations are implemented as properties of a symbol, including
`:=`, `array`, `dependencies`, `atvalue`,
`matchdeclare`, `atomgrad`, `constant`, `nonscalar`,
`assume`, and some others.  The effect of `local` is to make such
declarations effective only within the block or other compound expression in
which `local` appears; otherwise such declarations are global declarations.


`local` can only appear in `block`
or in the body of a function definition or `lambda` expression,
and only one occurrence is permitted in each.


`local` quotes its arguments.
`local` returns `done`.


Example:


A local function definition.









```maxima
maxima

(%i1) foo (x) := 1 - x;
(%o1)                    foo(x) := 1 - x


(%i2) foo (100);
(%o2)                         - 99


(%i3) block (local (foo), foo (x) := 2 * x, foo (100));
(%o3)                          200


(%i4) foo (100);
(%o4)                         - 99
```

### Function: macroexpand (expr)

Returns the macro expansion of *expr* without evaluating it,
when `expr` is a macro function call.
Otherwise, `macroexpand` returns *expr*.


If the expansion of *expr* yields another macro function call,
that macro function call is also expanded.


`macroexpand` quotes its argument.
However, if the expansion of a macro function call has side effects,
those side effects are executed.


See also `::=`, `macros`, and `macroexpand1`..


Examples










```maxima
maxima

(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99


(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))


(%i3) a: 1234;
(%o3)                         1234


(%i4) macroexpand (h (y));
                              y - a
(%o4)                         -----
                               99


(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

See also: `::=`, `macros`, `macroexpand1`.

### Function: macroexpand1 (expr)

Returns the macro expansion of *expr* without evaluating it,
when `expr` is a macro function call.
Otherwise, `macroexpand1` returns *expr*.


`macroexpand1` quotes its argument.
However, if the expansion of a macro function call has side effects,
those side effects are executed.


If the expansion of *expr* yields another macro function call,
that macro function call is not expanded.


See also `::=`, `macros`, and `macroexpand`.


Examples










```maxima
maxima

(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99


(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))


(%i3) a: 1234;
(%o3)                         1234


(%i4) macroexpand1 (h (y));
(%o4)                       g(y - a)


(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

See also: `::=`, `macros`, `macroexpand`.

### Variable: macroexpansion

Default value: `false`


`macroexpansion` controls whether the expansion (that is, the return value)
of a macro function is substituted for the macro function call.
A substitution may speed up subsequent expression evaluations,
at the cost of storing the expansion.



**false** — The expansion of a macro function is not substituted for the macro function call.
**expand** — The first time a macro function call is evaluated,
the expansion is stored.
The expansion is not recomputed on subsequent calls;
any side effects (such as `print` or assignment to global variables) happen
only when the macro function call is first evaluated.
Expansion in an expression does not affect other expressions
which have the same macro function call.
**displace** — The first time a macro function call is evaluated,
the expansion is substituted for the call,
thus modifying the expression from which the macro function was called.
The expansion is not recomputed on subsequent calls;
any side effects happen only when the macro function call is first evaluated.
Expansion in an expression does not affect other expressions
which have the same macro function call.


Examples


When `macroexpansion` is `false`,
a macro function is called every time the calling expression is evaluated,
and the calling expression is not modified.














```maxima
maxima

(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)


(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))


(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))


(%i4) macroexpansion: false;
(%o4)                         false


(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99


(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         [%t6]


(%i7) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o7)                       --------
                            a b + 99
```


When `macroexpansion` is `expand`,
a macro function is called once,
and the calling expression is not modified.














```maxima
maxima

(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)


(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))


(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))


(%i4) macroexpansion: expand;
(%o4)                        expand


(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99


(%i6) dispfun (f);
                      mmacroexpanded(x - 99, h(x))
(%t6)         f(x) := ----------------------------
                      mmacroexpanded(x + 99, g(x))

(%o6)                         [%t6]


(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```


When `macroexpansion` is `displace`,
a macro function is called once,
and the calling expression is modified.














```maxima
maxima

(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)


(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))


(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))


(%i4) macroexpansion: displace;
(%o4)                       displace


(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99


(%i6) dispfun (f);
                                 x - 99
(%t6)                    f(x) := ------
                                 x + 99

(%o6)                         [%t6]


(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```

### Variable: macros

Default value: `[]`


`macros` is the list of user-defined macro functions.
The macro function definition operator `::=` puts a new macro function
onto this list, and `kill`, `remove`, and `remfunction` remove
macro functions from the list.


See also `infolists`.

See also: `infolists`.

### Variable: mode_check_errorp

Default value: `false`


When `mode_check_errorp` is `true`, `mode_declare` calls
error.

### Variable: mode_check_warnp

Default value: `true`



When `mode_check_warnp` is `true`, mode errors are
described.

### Variable: mode_checkp

Default value: `true`


When `mode_checkp` is `true`, `mode_declare` does not only define
which type a variable will be of so the compiler can generate more efficient code,
but will also create a runtime warning if the variable isn’t of the variable type
the code was compiled to deal with.












```maxima
maxima

(%i1) mode_checkp:true;
(%o1)                         true


(%i2) square(f):=(
         mode_declare(f,float),
         f^2);
     compile(square);
     square(2.3);
     square(4);
                                                   2
(%o2)       square(f) := (mode_declare(f, float), f )
```

See also: `mode_declare`.

### Function: mode_declare (y_1, mode_1, ..., y_n, mode_n)

A `mode_declare` informs the compiler which type (lisp programmers name the type:
“mode”) a function parameter or its return value will be of. This can greatly
boost the efficiency of the code the compiler generates: Without knowing the type of
all variables and knowing the return value of all functions a function uses
in advance very generic (and thus potentially slow) code needs to be generated.


The arguments of `mode_declare` are pairs consisting of a variable (or a list
of variables all having the same mode) and a mode. Available modes (“types”) are:


```maxima
array            an declared array (see the detailed description below)
boolean          true or false
integer          integers (including arbitrary-size integers)
fixnum           integers (excluding arbitrary-size integers)
float            machine-size floating-point numbers
real             machine-size floating-point or integer
number           Numbers
any              any kind of object (useful for arrays of any)
```


A function parameter named `a` can be declared as an array filled with elements
of the type `t` the following way:


```maxima
maxima
mode_declare (a, array(t, dim1, dim2, ...))
```

If none of the elements of the array `a` needs to be checked if it still doesn’t
contain a value additional code can be omitted by declaring this fact, too:


```maxima
maxima
mode_declare (a, array (t, complete, dim1, dim2, ...))
```

The `complete` has no effect if all array elements are of the type
`fixnum` or `float`: Machine-sized numbers inevitably contain a value
(and will automatically be initialized to 0 in most lisp implementations).


Another way to tell that all entries of the array `a` are of the type
(“mode”) `m` and have been assigned a value to would be:


```maxima
maxima
mode_declare (completearray (a), m))
```


Numeric code using arrays might run faster still if the size of the array is
known at compile time, as well, as in:


```maxima
maxima
mode_declare (completearray (a [10, 10]), float)
```

for a floating point number array named `a` which is 10 x 10.


`mode_declare` also can be used in order to declare the type of the result
of a function. In this case the function compilation needs to be preceded by
another `mode_declare` statement. For example the expression,


```maxima
maxima
mode_declare ([function (f_1, f_2, ...)], fixnum)
```

declares that the values returned by `f_1`, `f_2`, ... are
single-word integers.


`modedeclare` is a synonym for `mode_declare`.


If the type of function parameters and results doesn’t match the declaration by
`mode_declare` the function may misbehave or a warning or an error might
occur, see `mode_checkp`, `mode_check_errorp` and
`mode_005fcheck_005fwarnp`.


See `mode_identity` for declaring the type of lists and `define_variable` for
declaring the type of all global variables compiled code uses, as well.


Example:











```maxima
maxima

(%i1) square_float(f):=(
     mode_declare(f,float),
     f*f
 );
(%o1)   square_float(f) := (mode_declare(f, float), f f)


(%i2) mode_declare([function(f)],float);
(%o2)                    [[function(f)]]


(%i3) compile(square_float);
(%o3)                    [square_float]


(%i4) square_float(100.0);
(%o4)                        10000.0
```

See also: `mode_checkp`, `mode_check_errorp`, `mode_check_warnp`, `mode_identity`, `define_variable`.

### Function: mode_identity (arg_1, arg_2)

`mode_identity` works similar to `mode_declare`, but is used for
informing the compiler that a thing like a `macro` or a list operation
will only return a specific type of object. The purpose of doing so is that
maxima supports many objects: Machine integers, arbitrary length integers,
equations, machine floats, big floats, which means that for everything that
deals with return values of operations that can result in any object the
compiler needs to output generic (and therefore potentially slow) code.


The first argument to `mode_identity` is the type of return value
something will return (for possible types see `mode_declare`).
(i.e., one of `float`, `fixnum`, `number`,
The second argument is the expression that will return an object of this
type.


If the the return value of this expression is of a type the code was not
compiled for error or warning is signalled.




If you knew that `first (l)` returned a number then you could write



```maxima
mode_identity (number, first (l)).
```

However, if you need this construct more often it would be more efficient
to define a function that returns a number fist:


```maxima
maxima
firstnumb (x) ::= buildq ([x], mode_identity (number, first(x)));
compile(firstnumb)
```

`firstnumb` now can be used every time you need the first element
of a list that is guaranteed to be filled with numbers.

See also: `mode_declare`.

### Function: remfunction (remfunction, f_1, ..., f_n, remfunction, all)

Unbinds the function definitions of the symbols *f_1*, ..., *f_n*.
The arguments may be the names of ordinary functions (created by `:=` or
`define`) or macro functions (created by `::=`).


`remfunction (all)` unbinds all function definitions.


`remfunction` quotes its arguments.


`remfunction` returns a list of the symbols for which the function
definition was unbound.  `false` is returned in place of any symbol for
which there is no function definition.


`remfunction` does not apply to `memoizing functions` or subscripted functions.
`remarray` applies to those types of functions.

See also: `:=`, `define`, `::=`, `memoizing-functions`, `remarray`.

### Variable: savedef

Default value: `true`


When `savedef` is `true`, the Maxima version of a user function is
preserved when the function is translated.  This permits the definition to be
displayed by `dispfun` and allows the function to be edited.


When `savedef` is `false`, the names of translated functions are
removed from the `functions` list.

### Function: splice (a)

Splices (interpolates) the list named by the atom *a* into an expression,
but only if `splice` appears within `buildq`;
otherwise, `splice` is treated as an undefined function.
If appearing within `buildq` as *a* alone (without `splice`),
*a* is substituted (not interpolated) as a list into the result.
The argument of `splice` can only be an atom;
it cannot be a literal list or an expression which yields a list.


Typically `splice` supplies the arguments for a function or operator.
For a function `f`, the expression `f (splice (a))` within
`buildq` expands to `f (a[1], a[2], a[3], ...)`.
For an operator `o`, the expression `"o" (splice (a))` within
`buildq` expands to `"o" (a[1], a[2], a[3], ...)`,
where `o` may be any type of operator (typically one which takes multiple
arguments).  Note that the operator must be enclosed in double quotes `"`.


Examples









```maxima
maxima

(%i1) buildq ([x: [1, %pi, z - y]], foo (splice (x)) / length (x));
                       foo(1, %pi, z - y)
(%o1)                -----------------------
                     length([1, %pi, z - y])


(%i2) buildq ([x: [1, %pi]], "/" (splice (x)));
                                1
(%o2)                          ---
                               %pi


(%i3) matchfix ("<>", "<>");
(%o3)                          <>


(%i4) buildq ([x: [1, %pi, z - y]], "<>" (splice (x)));
(%o4)                   <>1, %pi, z - y<>
```

### Variable: tr_array_as_ref

Default value: `true`


If `translate_fast_arrays` is `false`, array references in Lisp code
emitted by `translate_file` are affected by `tr_array_as_ref`.
When `tr_array_as_ref` is `true`,
array names are evaluated,
otherwise array names appear as literal symbols in translated code.


`tr_array_as_ref` has no effect if `translate_fast_arrays` is
`true`.

### Variable: tr_bound_function_applyp

Default value: `true`


When `tr_bound_function_applyp` is `true` and `tr_function_call_default`
is `general`, if a bound variable (such as a function argument) is found being
used as a function then Maxima will rewrite that function call using `apply` and
print a warning message.


For example, if `g` is defined by `g(f,x) := f(x+1)` then translating
`g` will cause Maxima to print a warning and rewrite `f(x+1)` as
`apply(f,[x+1])`.













```maxima
maxima
(%i1) f (x) := x^2$
(%i2) g (f) := f (3)$
(%i3) tr_bound_function_applyp : true$

(%i4) translate (g)$
warning: f is a bound variable in f(3), but it is used as a function.
note: instead I'll translate it as: apply(f,[3])


(%i5) g (lambda ([x], x));
(%o5)                           3

(%i6) tr_bound_function_applyp : false$
(%i7) translate (g)$

(%i8) g (lambda ([x], x));
(%o8)                           9
```

### Variable: tr_file_tty_messagesp

Default value: `false`


When `tr_file_tty_messagesp` is `true`, messages generated by
`translate_file` during translation of a file are displayed on the console
and inserted into the UNLISP file.  When `false`, messages about
translation of the file are only inserted into the UNLISP file.

### Variable: tr_float_can_branch_complex

Default value: `true`


Tells the Maxima-to-Lisp translator to assume that the functions 
`acos`, `asin`, `asec`, `acsc`, `acosh`,
`asech`, `atanh`, `acoth`, `log` and `sqrt`
can return complex results.


When it is `true` then `acos(x)` is of mode `any`
even if `x` is of mode `float` (as set by `mode_declare`).
When `false` then `acos(x)` is of mode
`float` if and only if `x` is of mode `float`.

### Variable: tr_function_call_default

Default value: `general`


`false` means give up and call `meval`, `expr` means assume Lisp
fixed arg function.  `general`, the default gives code good for
`mexprs` and `mlexprs` but not `macros`.  `general` assures
variable bindings are correct in compiled code.  In `general` mode, when
translating F(X), if F is a bound variable, then it assumes that
`apply (f, [x])` is meant, and translates a such, with appropriate warning.
There is no need to turn this off.  With the default settings, no warning
messages implies full compatibility of translated and compiled code with the
Maxima interpreter.

### Variable: tr_numer

Default value: `false`


When `tr_numer` is `true`, `numer` properties are used for
atoms which have them, e.g. `%pi`.

### Variable: tr_optimize_max_loop

Default value: 100


`tr_optimize_max_loop` is the maximum number of times the
macro-expansion and optimization pass of the translator will loop in
considering a form.  This is to catch macro expansion errors, and
non-terminating optimization properties.

### Variable: tr_state_vars

Default value:


```maxima
maxima
[translate_fast_arrays, tr_function_call_default, tr_bound_function_applyp,
tr_array_as_ref, tr_numer, tr_float_can_branch_complex, define_variable]
```


The list of the switches that affect the form of the
translated output.


This information is useful to system people when
trying to debug the translator.  By comparing the translated product
to what should have been produced for a given state, it is possible to
track down bugs.

### Variable: tr_warn_bad_function_calls

Default value: `true`


- Gives a warning when
when function calls are being made which may not be correct due to
improper declarations that were made at translate time.

### Variable: tr_warn_fexpr

Default value: `compfile`


- Gives a warning if any FEXPRs are
encountered.  FEXPRs should not normally be output in translated code,
all legitimate special program forms are translated.

### Variable: tr_warn_meval

Default value: `compfile`


- Gives a warning if the function `meval` gets called.  If `meval` is
called that indicates problems in the translation.

### Variable: tr_warn_mode

Default value: `all`


- Gives a warning when variables are
assigned values inappropriate for their mode.

### Variable: tr_warn_undeclared

Default value: `compile`


- Determines when to send
warnings about undeclared variables to the TTY.

### Variable: tr_warn_undefined_variable

Default value: `all`


- Gives a warning when
undefined global variables are seen.

### Function: tr_warnings_get ()

Prints a list of warnings which have been given by
the translator during the current translation.

### Function: translate (translate, f_1, ..., f_n, translate, functions, translate, all)

Translates the user-defined functions *f_1*, ..., *f_n* from the
Maxima language into Lisp and evaluates the Lisp translations.
Typically the translated functions run faster than the originals.


`translate (all)` or `translate (functions)` translates all
user-defined functions.


Functions to be translated should include a call to `mode_declare` at the
beginning when possible in order to produce more efficient code.  For example:



```maxima
maxima
f (x_1, x_2, ...) := block ([v_1, v_2, ...],
    mode_declare (v_1, mode_1, v_2, mode_2, ...), ...)
```



where the *x_1*, *x_2*, ...  are the parameters to the function and
the *v_1*, *v_2*, ... are the local variables.


The names of translated functions are removed from the `functions` list
if `savedef` is `false` (see below) and are added to the `props`
lists.


Functions should not be translated unless they are fully debugged.


Expressions are assumed simplified; if they are not, correct but non-optimal
code gets generated.  Thus, the user should not set the `simp` switch to
`false` which inhibits simplification of the expressions to be translated.


The switch `translate`, if `true`, causes automatic
translation of a user’s function to Lisp.


Note that translated
functions may not run identically to the way they did before
translation as certain incompatibilities may exist between the Lisp
and Maxima versions.  Principally, the `rat` function with more than
one argument and the `ratvars` function should not be used if any
variables are `mode_declare`’d canonical rational expressions (CRE).



`savedef` - if `true` will cause the Maxima version of a user
function to remain when the function is `translate`’d.  This permits the
definition to be displayed by `dispfun` and allows the function to be
edited.


`transrun` - if `false` will cause the interpreted version of all
functions to be run (provided they are still around) rather than the
translated version.


The result returned by `translate` is a list of the names of the
functions translated.

### Function: translate_file (translate_file, maxima_filename, translate_file, maxima_filename, lisp_filename)

Translates a file of Maxima code into a file of Lisp code.
`translate_file` returns a list of three filenames:
the name of the Maxima file, the name of the Lisp file, and the name of file
containing additional information about the translation.
`translate_file` evaluates its arguments.


`translate_file ("foo.mac"); load("foo.LISP")` is the same as the command
`batch ("foo.mac")` except for certain restrictions, the use of
`''` and `%`, for example.



`translate_file (maxima_filename)` translates a Maxima file
*maxima_filename* into a similarly-named Lisp file.
For example, `foo.mac` is translated into `foo.LISP`.
The Maxima filename may include a directory name or names,
in which case the Lisp output file is written
to the same directory from which the Maxima input comes.


`translate_file (maxima_filename, lisp_filename)` translates
a Maxima file *maxima_filename* into a Lisp file *lisp_filename*.
`translate_file` ignores the filename extension, if any, of
`lisp_filename`; the filename extension of the Lisp output file is always
`LISP`.  The Lisp filename may include a directory name or names,
in which case the Lisp output file is written to the specified directory.


`translate_file` also writes a file of translator warning
messages of various degrees of severity.
The filename extension of this file is `UNLISP`.
This file may contain valuable information, though possibly obscure,
for tracking down bugs in translated code.
The `UNLISP` file is always written
to the same directory from which the Maxima input comes.


`translate_file` emits Lisp code which causes
some declarations and definitions to take effect as soon
as the Lisp code is compiled.
See `compile_file` for more on this topic.



See also 


`tr_array_as_ref`



`tr_bound_function_applyp`,


`tr_exponent`
`tr_file_tty_messagesp`,
`tr_float_can_branch_complex`,
`tr_function_call_default`,
`tr_numer`,
`tr_optimize_max_loop`,
`tr_state_vars`,
`tr_warnings_get`,

`tr_warn_bad_function_calls`
`tr_warn_fexpr`, 
`tr_warn_meval`,
`tr_warn_mode`,
`tr_warn_undeclared`,
and `tr_005fwarn_005fundefined_005fvariable`.

See also: `tr_bound_function_applyp`, `tr_file_tty_messagesp`, `tr_float_can_branch_complex`, `tr_function_call_default`, `tr_numer`, `tr_optimize_max_loop`, `tr_state_vars`, `tr_warnings_get`, `tr_warn_fexpr`, `tr_warn_meval`, `tr_warn_mode`, `tr_warn_undeclared`, `tr_warn_undefined_variable`.

### Variable: transrun

Default value: `true`


When `transrun` is `false` will cause the interpreted
version of all functions to be run (provided they are still around)
rather than the translated version.

