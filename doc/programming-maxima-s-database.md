## Maxima’s Database

### Function: activate (context_1, ..., context_n)

Activates the contexts *context_1*, ..., *context_n*.
The facts in these contexts are then available to
make deductions and retrieve information.
The facts in these contexts are not listed by `facts ()`.


The variable `activecontexts` is the list
of contexts which are active by way of the `activate` function.

See also: `activecontexts`.

### Variable: activecontexts

Default value: `[]`


`activecontexts` is a list of the contexts which are active
by way of the `activate` function, as opposed to being active because
they are subcontexts of the current context.

See also: `activate`.

### Variable: alphabetic

`alphabetic` is a property type recognized by `declare`.
The expression `declare(s, alphabetic)` tells Maxima to recognize
as alphabetic all of the characters in *s*, which must be a string.


See also `Identifiers`.


Example:









```maxima
maxima

(%i1) xx\~yy\`\@ : 1729;
(%o1)                         1729


(%i2) declare ("~`@", alphabetic);
(%o2)                         done


(%i3) xx~yy`@ + @yy`xx + `xx@@yy~;
(%o3)               `xx@@yy~ + @yy`xx + 1729


(%i4) listofvars (%);
(%o4)                  [@yy`xx, `xx@@yy~]
```

See also: `declare`, `Identifiers`.

### Function: askequal (askequal, expr1, expr2)

`askequal(expr1, expr2)` attempts to determine from the
`assume` database whether *expr1* is equal to *expr2*,
and prompts the user if it cannot tell.


If the user provides the answer,
the answer is stored in the `assume` database
for the duration of the evaluation of the expression currently in progress.
When the evaluation is completed,
the user-provided answer is removed from the database.


`askequal` returns `yes` or `no`,
whether the answer was determined from the `assume` database
or provided by the user.


See also `equal`.

See also: `equal`.

### Function: askinteger (askinteger, expr, integer, askinteger, expr, askinteger, expr, even, askinteger, expr, odd)

`askinteger (expr, integer)` attempts to determine from the
`assume` database whether *expr* is an integer.
`askinteger` prompts the user if it cannot tell otherwise,


and attempt to install the information in the database if possible.
`askinteger (expr)` is equivalent to
`askinteger (expr, integer)`.


`askinteger (expr, even)` and `askinteger (expr, odd)`
likewise attempt to determine if *expr* is an even integer or odd integer,
respectively.

### Function: asksign (expr)

First attempts to determine whether the specified
expression is positive, negative, or zero.  If it cannot, it asks the
user the necessary questions to complete its deduction.  The user’s
answer is recorded in the data base for the duration of the current
computation.  The return value of `asksign` is one of `pos`,
`neg`, or `zero`.

### Function: assume (pred_1, ..., pred_n)

Adds predicates *pred_1*, ..., *pred_n* to the current context.
If a predicate is inconsistent or redundant with the predicates in the current
context, it is not added to the context.  The context accumulates predicates
from each call to `assume`.


`assume` returns a list whose elements are the predicates added to the
context or the atoms `redundant` or `inconsistent` where applicable.


The predicates *pred_1*, ..., *pred_n* can only be expressions
with the relational operators `< <= equal notequal >=` and `>`.
Predicates cannot be literal equality `=` or literal inequality `#`
expressions, nor can they be predicate functions such as `integerp`.


Compound predicates of the form `pred_1 and ... and pred_n`
are recognized, but not `pred_1 or ... or pred_n`.
`not pred_k` is recognized if *pred_k* is a relational predicate.
Expressions of the form `not (pred_1 and pred_2)`
and `not (pred_1 or pred_2)` are not recognized.


Maxima’s deduction mechanism is not very strong;
there are many obvious consequences which cannot be determined by `is`.
This is a known weakness.


`assume` does not handle predicates with complex numbers.  If a predicate
contains a complex number `assume` returns `inconsistent` or 
`redundant`.


`assume` evaluates its arguments.


See also `is`, `facts`, `forget`,
`context`, and `declare`.


Examples:















```maxima
maxima

(%i1) assume (xx > 0, yy < -1, zz >= 0);
(%o1)              [xx > 0, yy < - 1, zz >= 0]


(%i2) assume (aa < bb and bb < cc);
(%o2)                  [bb > aa, cc > bb]


(%i3) facts ();
(%o3)     [xx > 0, - 1 > yy, zz >= 0, bb > aa, cc > bb]


(%i4) is (xx > yy);
(%o4)                         true


(%i5) is (yy < -yy);
(%o5)                         true


(%i6) is (sinh (bb - aa) > 0);
(%o6)                         true


(%i7) forget (bb > aa);
(%o7)                       [bb > aa]


(%i8) prederror : false;
(%o8)                         false


(%i9) is (sinh (bb - aa) > 0);
(%o9)                        unknown


(%i10) is (bb^2 < cc^2);
(%o10)                       unknown
```

See also: `is`, `facts`, `forget`, `context`, `declare`.

### Variable: assume_pos

Default value: `false`


When `assume_pos` is `true` and the sign of a parameter *x*
cannot be determined from the current context

or other considerations,
`sign` and `asksign (x)` return `true`.
This may forestall some automatically-generated `asksign` queries,
such as may arise from `integrate` or other computations.


By default, a parameter is *x* such that `symbolp (x)`
or `subvarp (x)`.
The class of expressions considered parameters can be modified to some extent
via the variable `assume_pos_pred`.


`sign` and `asksign` attempt to deduce the sign of expressions
from the sign of operands within the expression.
For example, if `a` and `b` are both positive,
then `a + b` is also positive.


However, there is no way to bypass all `asksign` queries.
In particular, when the `asksign` argument is a
difference `x - y` or a logarithm `log(x)`,
`asksign` always requests an input from the user,
even when `assume_pos` is `true` and `assume_pos_pred` is
a function which returns `true` for all arguments.

### Variable: assume_pos_pred

Default value: `false`


When `assume_pos_pred` is assigned the name of a function
or a lambda expression of one argument *x*,
that function is called to determine
whether *x* is considered a parameter for the purpose of `assume_pos`.
`assume_pos_pred` is ignored when `assume_pos` is `false`.


The `assume_pos_pred` function is called by `sign` and `asksign`
with an argument *x*
which is either an atom, a subscripted variable, or a function call expression.
If the `assume_pos_pred` function returns `true`,
*x* is considered a parameter for the purpose of `assume_pos`.


By default, a parameter is *x* such that `symbolp (x)`
or `subvarp (x)`.


See also `assume` and `assume_005fpos`.


Examples:


















```maxima
maxima
(%i1) assume_pos: true$
(%i2) assume_pos_pred: symbolp$

(%i3) sign (a);
(%o3)                          pos


(%i4) sign (a[1]);
(%o4)                          pnz

(%i5) assume_pos_pred: lambda ([x], display (x), true)$

(%i6) asksign (a);
                              x = a

(%o6)                          pos


(%i7) asksign (a[1]);
                             x = a
                                  1

(%o7)                          pos


(%i8) asksign (foo (a));
                           x = foo(a)

(%o8)                          pos


(%i9) asksign (foo (a) + bar (b));
                           x = foo(a)

                           x = bar(b)

(%o9)                          pos


(%i10) asksign (log (a));
                              x = a

                              x = a

                              x = a

                              x = a

                              x = a

                              x = a

                              x = a

                              x = a

                              x = a



Is a - 1 positive, negative or zero?
p;
(%o10)                         pos


(%i11) asksign (a - b);
                              x = a

                              x = b

                              x = a

                              x = b



Is b - a positive, negative or zero?
p;
(%o11)                         neg
```

See also: `assume`, `assume_pos`.

### Variable: assumescalar

Default value: `true`


`assumescalar` helps govern whether expressions `expr`
for which `nonscalarp (expr)` is `false`
are assumed to behave like scalars for certain transformations.


Let `expr` represent any expression other than a list or a matrix,
and let `[1, 2, 3]` represent any list or matrix.
Then `expr . [1, 2, 3]` yields `[expr, 2 expr, 3 expr]`
if `assumescalar` is `true`, or `scalarp (expr)` is
`true`, or `constantp (expr)` is `true`.


If `assumescalar` is `true`, such
expressions will behave like scalars only for commutative
operators, but not for noncommutative multiplication `.`.


When `assumescalar` is `false`, such
expressions will behave like non-scalars.


When `assumescalar` is `all`, such expressions will behave like
scalars for all the operators listed above.

### Variable: bindtest

The command `declare(x, bindtest)` tells Maxima to trigger an error
when the symbol *x* is evaluated unbound.









evaluation: unbound variable aa
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) aa + bb;
(%o1)                        bb + aa


(%i2) declare (aa, bindtest);
(%o2)                         done

(%i3) aa + bb;

(%i4) aa : 1234;
(%o4)                         1234


(%i5) aa + bb;
(%o5)                       bb + 1234
```

### Function: charfun (p)

Return 0 when the predicate *p* evaluates to `false`; return 1 when
the predicate evaluates to `true`.  When the predicate evaluates to
something other than `true` or `false` (unknown),  return a noun form.


Examples:









```maxima
maxima

(%i1) charfun (x < 1);
(%o1)                    charfun(x < 1)


(%i2) subst (x = -1, %);
(%o2)                           1

(%i3) e : charfun ('"and" (-1 < x, x < 1))$

(%i4) [subst (x = -1, e), subst (x = 0, e), subst (x = 1, e)];
(%o4) [charfun((- 1 < - 1) and (- 1 < 1)), 
  charfun((- 1 < 0) and (0 < 1)), charfun((- 1 < 1) and (1 < 1))]
```

### Function: compare (x, y)

Return a comparison operator *op* (`<`, `<=`, `>`, `>=`,
`=`, or `#`) such that `is (x op y)` evaluates
to `true`; when either *x* or *y* depends on `%i` and
`x # y`, return `notcomparable`; when there is no such
operator or Maxima isn’t able to determine the operator, return `unknown`.


Examples:











```maxima
maxima

(%i1) compare (1, 2);
(%o1)                           <


(%i2) compare (1, x);
(%o2)                        unknown


(%i3) compare (%i, %i);
(%o3)                           =


(%i4) compare (%i, %i + 1);
(%o4)                     notcomparable


(%i5) compare (1/x, 0);
(%o5)                           #


(%i6) compare (x, abs(x));
(%o6)                          <=
```


The function `compare` doesn’t try to determine whether the real domains of
its arguments are nonempty; thus






```maxima
maxima

(%i1) compare (acos (x^2 + 1), acos (x^2 + 1) + 1);
(%o1)                           <
```



The real domain of `acos (x^2 + 1)` is empty.

### Function: constant ()

`declare(a, constant)` declares *a* to be a constant.  The
declaration of a symbol to be constant does not prevent the assignment of a
nonconstant value to the symbol.


See `constantp` and `declare`.



Example:









```maxima
maxima

(%i1) declare(c, constant);
(%o1)                         done


(%i2) constantp(c);
(%o2)                         true


(%i3) c : x;
(%o3)                           x


(%i4) constantp(c);
(%o4)                         false
```

See also: `constantp`, `declare`.

### Function: constantp (expr)

Returns `true` if *expr* is a constant expression, otherwise returns
`false`.



An expression is considered a constant expression if its arguments are
numbers (including rational numbers, as displayed with `/R/`),
symbolic constants such as `%pi`, `%e`, and `%i`,
variables bound to a constant or declared constant by `declare`,
or functions whose arguments are constant.


`constantp` evaluates its arguments.


See the property `constant` which declares a symbol to be constant.


Examples:












```maxima
maxima

(%i1) constantp (7 * sin(2));
(%o1)                         true


(%i2) constantp (rat (17/29));
(%o2)                         true


(%i3) constantp (%pi * sin(%e));
(%o3)                         true


(%i4) constantp (exp (x));
(%o4)                         false


(%i5) declare (x, constant);
(%o5)                         done


(%i6) constantp (exp (x));
(%o6)                         true


(%i7) constantp (foo (x) + bar (%e) + baz (2));
(%o7)                         false
```

See also: `%pi`, `%e`, `%i`, `declare`, `constant`.

### Variable: context

Default value: `initial`


`context` names the collection of facts maintained by `assume` and
`forget`.  `assume` adds facts to the collection named by
`context`, while `forget` removes facts.


Binding `context` to a name *foo* changes the current context to
*foo*.  If the specified context *foo* does not yet exist,
it is created automatically by a call to `newcontext`.

The specified context is activated automatically.


See `contexts` for a general description of the context mechanism.

See also: `assume`, `forget`, `newcontext`, `contexts`.

### Variable: contexts

Default value: `[initial, global]`


`contexts` is a list of the contexts which
currently exist, including the currently active context.


The context mechanism makes it possible for a user to bind together
and name a collection of facts, called a context.
Once this is done, the user can have Maxima assume or forget large numbers
of facts merely by activating or deactivating their context.


Any symbolic atom can be a context, and the facts contained in that
context will be retained in storage until destroyed one by one
by calling `forget` or destroyed as a whole by calling `kill`
to destroy the context to which they belong.


Contexts exist in a hierarchy, with the root always being
the context `global`, which contains information about Maxima that some
functions need.  When in a given context, all the facts in that
context are "active" (meaning that they are used in deductions and
retrievals) as are all the facts in any context which is a subcontext
of the active context.


When a fresh Maxima is started up, the user is in a
context called `initial`, which has `global` as a subcontext.


See also `facts`, `newcontext`, `supcontext`,
`killcontext`, `activate`, `deactivate`,
`assume`, and `forget`.

See also: `forget`, `kill`, `facts`, `newcontext`, `supcontext`, `killcontext`, `activate`, `deactivate`, `assume`.

### Function: csign (expr)

Attempts to determine the sign of *expr* on the basis of the facts
in the current data base without assuming that *expr* is
real-valued. It returns one of the following answers: `pos`
(positive), `neg` (negative), `zero`, `pz` (positive or
zero), `nz` (negative or zero), `pn` (positive or negative),
`pnz` (positive, negative, or zero), `imaginary`
(purely imaginary), or `complex`, (complex, i.e. nothing known).


Note that while this function does not assume that *expr* is
real-valued, it still assumes that variables are real-valued unless
declared otherwise. This means that `csign(z)` will return
`pnz` unless `declare(z,complex)` or
`declare(z,imaginary)` has been evaluated beforehand.


See also `sign`.

See also: `sign`.

### Function: deactivate (context_1, ..., context_n)

Deactivates the specified contexts *context_1*, ..., *context_n*.

### Function: declare (a_1, p_1, a_2, p_2, ...)

Assigns the atom or list of atoms *a_i* the property or list of properties
*p_i*.  When *a_i* and/or *p_i* are lists, each of the atoms gets
all of the properties.


`declare` quotes its arguments.  `declare` always returns `done`.


As noted in the description for each declaration flag, for some flags
`featurep(object, feature)` returns `true` if *object*
has been declared to have *feature*.


For more information about the features system, see `features`. To
remove a property from an atom, use `remove`.


`declare` recognizes the following properties:



**`additive`** — Tells Maxima to simplify *a_i* expressions by the substitution
`a_i(x + y + z + ...)` `-->`
`a_i(x) + a_i(y) + a_i(z) + ...`.
The substitution is carried out on the first argument only.
**`alphabetic`** — Tells Maxima to recognize all characters in *a_i* (which must be a
string) as alphabetic characters.
**`antisymmetric`, `commutative`, `symmetric`** — Tells Maxima to recognize *a_i* as a symmetric or antisymmetric
function.  `commutative` is the same as `symmetric`.
**`bindtest`** — Tells Maxima to trigger an error when *a_i* is evaluated unbound.
**`constant`** — Tells Maxima to consider *a_i* a symbolic constant.
**`even`, `odd`** — Tells Maxima to recognize *a_i* as an even or odd integer variable.
**`evenfun`, `oddfun`** — Tells Maxima to recognize *a_i* as an odd or even function.
**`evflag`** — Makes *a_i* known to the `ev` function so that *a_i* is bound
to `true` during the execution of `ev` when *a_i* appears as
a flag argument of `ev`.
**`evfun`** — Makes *a_i* known to `ev` so that the function named by *a_i*
is applied when *a_i* appears as a flag argument of `ev`.
**`feature`** — Tells Maxima to recognize *a_i* as the name of a feature.
Other atoms may then be declared to have the *a_i* property.
**`increasing`, `decreasing`** — Tells Maxima to recognize *a_i* as an increasing or decreasing
function.
**`integer`, `noninteger`** — Tells Maxima to recognize *a_i* as an integer or noninteger variable.
**`integervalued`** — Tells Maxima to recognize *a_i* as an integer-valued function.
**`lassociative`, `rassociative`** — Tells Maxima to recognize *a_i* as a right-associative or
left-associative function.
**`linear`** — Equivalent to declaring *a_i* both `outative` and
`additive`.
**`mainvar`** — Tells Maxima to consider *a_i* a "main variable".  A main variable
succeeds all other constants and variables in the canonical ordering of
Maxima expressions, as determined by `ordergreatp`.
**`multiplicative`** — Tells Maxima to simplify *a_i* expressions by the substitution
`a_i(x * y * z * ...)` `-->` 
`a_i(x) * a_i(y) * a_i(z) * ...`.
The substitution is carried out on the first argument only.
**`nary`** — Tells Maxima to recognize *a_i* as an n-ary function. 
The `nary` declaration is not the same as calling the `nary`
function.  The sole effect of `declare(foo, nary)` is to instruct the
Maxima simplifier to flatten nested expressions, for example, to simplify
`foo(x, foo(y, z))` to `foo(x, y, z)`.
**`nonarray`** — Tells Maxima to consider *a_i* not an array.  This declaration
prevents multiple evaluation of a subscripted variable name.
**`nonscalar`** — Tells Maxima to consider *a_i* a nonscalar variable.  The usual
application is to declare a variable as a symbolic vector or matrix.
**`noun`** — Tells Maxima to parse *a_i* as a noun.  The effect of this is to
replace instances of *a_i* with `'a_i` or
`nounify(a_i)`, depending on the context.
**`outative`** — Tells Maxima to simplify *a_i* expressions by pulling constant factors
out of the first argument. 
When *a_i* has one argument, a factor is considered constant if it is
a literal or declared constant. 
When *a_i* has two or more arguments, a factor is considered constant
if the second argument is a symbol and the factor is free of the second
argument.
**`posfun`** — Tells Maxima to recognize *a_i* as a positive function.
**`rational`, `irrational`** — Tells Maxima to recognize *a_i* as a rational or irrational real
variable.
**`real`, `imaginary`, `complex`** — Tells Maxima to recognize *a_i* as a real, pure imaginary, or complex
variable.
**`scalar`** — Tells Maxima to consider *a_i* a scalar variable.


Examples of the usage of the properties are available in the documentation
for each separate description of a property.

See also: `features`, `remove`, `additive`, `alphabetic`, `antisymmetric`, `commutative`, `symmetric`, `bindtest`, `constant`, `even`, `odd`, `evenfun`, `oddfun`, `evflag`, `evfun`, `feature`, `increasing`, `decreasing`, `integer`, `noninteger`, `integervalued`, `lassociative`, `rassociative`, `linear`, `mainvar`, `ordergreatp`, `multiplicative`, `nary`, `nonarray`, `nonscalar`, `noun`, `outative`, `posfun`, `rational`, `irrational`, `real`, `imaginary`, `complex`, `scalar`.

### Variable: decreasing

The commands `declare(f, decreasing)` or
`declare(f, increasing)` tell Maxima to recognize the function
*f* as an decreasing or increasing function.


See also `declare` for more properties.


Example:









```maxima
maxima

(%i1) assume(a > b);
(%o1)                        [a > b]


(%i2) is(f(a) > f(b));
(%o2)                        unknown


(%i3) declare(f, increasing);
(%o3)                         done


(%i4) is(f(a) > f(b));
(%o4)                         true
```

See also: `declare`.

### Function: equal (a, b)

Represents equivalence, that is, equal value.


By itself, `equal` does not evaluate or simplify.
The function `is` attempts to evaluate `equal` to a Boolean value.
`is(equal(a, b))` returns `true` (or `false`) if
and only if *a* and *b* are equal (or not equal) for all possible
values of their variables, as determined by evaluating
`ratsimp(a - b)`; if `ratsimp` returns 0, the two
expressions are considered equivalent.  Two expressions may be equivalent even
if they are not syntactically equal (i.e., identical).


When `is` fails to reduce `equal` to `true` or `false`, the
result is governed by the global flag `prederror`.  When `prederror`
is `true`, `is` complains with an error message.  Otherwise, `is`
returns `unknown`.


In addition to `is`, some other operators evaluate `equal` and
`notequal` to `true` or `false`, namely `if`,
`and`, `or`, and `not`.







The negation of `equal` is `notequal`.


Examples:


By itself, `equal` does not evaluate or simplify.








```maxima
maxima

(%i1) equal (x^2 - 1, (x + 1) * (x - 1));
                        2
(%o1)            equal(x  - 1, (x - 1) (x + 1))


(%i2) equal (x, x + 1);
(%o2)                    equal(x, x + 1)


(%i3) equal (x, y);
(%o3)                      equal(x, y)
```


The function `is` attempts to evaluate `equal` to a Boolean value.
`is(equal(a, b))` returns `true` when
`ratsimp(a - b)` returns 0.  Two expressions may be equivalent
even if they are not syntactically equal (i.e., identical).














```maxima
maxima

(%i1) ratsimp (x^2 - 1 - (x + 1) * (x - 1));
(%o1)                           0


(%i2) is (equal (x^2 - 1, (x + 1) * (x - 1)));
(%o2)                         true


(%i3) is (x^2 - 1 = (x + 1) * (x - 1));
(%o3)                         false


(%i4) ratsimp (x - (x + 1));
(%o4)                          - 1


(%i5) is (equal (x, x + 1));
(%o5)                         false


(%i6) is (x = x + 1);
(%o6)                         false


(%i7) ratsimp (x - y);
(%o7)                         x - y


(%i8) is (equal (x, y));
(%o8)                        unknown


(%i9) is (x = y);
(%o9)                         false
```


When `is` fails to reduce `equal` to `true` or `false`,
the result is governed by the global flag `prederror`.










                                    

2             2
Unable to evaluate predicate equal(x  + 2 x + 1, x  - 2 x - 1)
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) [aa : x^2 + 2*x + 1, bb : x^2 - 2*x - 1];
                    2             2
(%o1)             [x  + 2 x + 1, x  - 2 x - 1]


(%i2) ratsimp (aa - bb);
(%o2)                        4 x + 2


(%i3) prederror : true;
(%o3)                         true

(%i4) is (equal (aa, bb));

(%i5) prederror : false;
(%o5)                         false


(%i6) is (equal (aa, bb));
(%o6)                        unknown
```


Some operators evaluate `equal` and `notequal` to `true` or
`false`.









```maxima
maxima

(%i1) if equal (y, y - 1) then FOO else BAR;
(%o1)                          BAR


(%i2) eq_1 : equal (x, x + 1);
(%o2)                    equal(x, x + 1)


(%i3) eq_2 : equal (y^2 + 2*y + 1, (y + 1)^2);
                         2                   2
(%o3)             equal(y  + 2 y + 1, (y + 1) )


(%i4) [eq_1 and eq_2, eq_1 or eq_2, not eq_1];
(%o4)                  [false, true, true]
```


Because `not expr` causes evaluation of *expr*,
`not equal(a, b)` is equivalent to
`is(notequal(a, b))`.







```maxima
maxima

(%i1) [notequal (2*z, 2*z - 1), not equal (2*z, 2*z - 1)];
(%o1)            [notequal(2 z, 2 z - 1), true]


(%i2) is (notequal (2*z, 2*z - 1));
(%o2)                         true
```

See also: `is`, `ratsimp`, `prederror`, `if`, `and`, `or`, `not`, `notequal`.

### Variable: even

`declare(a, even)` or `declare(a, odd)` tells Maxima to
recognize the symbol *a* as an even or odd integer variable.  The
properties `even` and `odd` are not recognized by the functions
`evenp`, `oddp`, and `integerp`.


See also `declare` and `askinteger`.


Example:









```maxima
maxima

(%i1) declare(n, even);
(%o1)                         done


(%i2) askinteger(n, even);
(%o2)                          yes


(%i3) askinteger(n);
(%o3)                          yes


(%i4) evenp(n);
(%o4)                         false
```

See also: `evenp`, `oddp`, `integerp`, `declare`, `askinteger`.

### Function: facts (facts, item, facts)

If *item* is the name of a context, `facts (item)` returns a
list of the facts in the specified context.


If *item* is not the name of a context, `facts (item)` returns a
list of the facts known about *item* in the current context.  Facts that
are active, but in a different context, are not listed.


`facts ()` (i.e., without an argument) lists the current context.

### Variable: feature

Maxima understands two distinct types of features, system features and features
which apply to mathematical expressions.  See also `status` for information
about system features.  See also `features` and `featurep` for
information about mathematical features.




`feature` itself is not the name of a function or variable.

See also: `status`, `features`, `featurep`.

### Function: featurep (a, f)

Attempts to determine whether the object *a* has the feature *f* on the
basis of the facts in the current database.  If so, it returns `true`,
else `false`.


Note that `featurep` returns `false` when neither *f*
nor the negation of *f* can be established.


`featurep` evaluates its argument.


See also `declare` and `features`.







```maxima
maxima
(%i1) declare (j, even)$

(%i2) featurep (j, integer);
(%o2)                         true
```

See also: `declare`, `features`.

### Variable: features

Maxima recognizes certain mathematical properties of functions and variables.
These are called "features".


`declare (x, foo)` gives the property *foo*
to the function or variable *x*.


`declare (foo, feature)` declares a new feature *foo*.
For example,
`declare ([red, green, blue], feature)`
declares three new features, `red`, `green`, and `blue`.


The predicate `featurep (x, foo)`
returns `true` if *x* has the *foo* property,
and `false` otherwise.


The infolist `features` is a list of known features.  These are



   integer        noninteger      even
   odd            rational        irrational
   real           imaginary       complex
   analytic       increasing      decreasing
   oddfun         evenfun         posfun
   constant       commutative     lassociative
   rassociative   symmetric       antisymmetric
   integervalued


plus any user-defined features.


`features` is a list of mathematical features.  There is also a list of
non-mathematical, system-dependent features.  See `status`.


Example:








```maxima
maxima

(%i1) declare (FOO, feature);
(%o1)                         done


(%i2) declare (x, FOO);
(%o2)                         done


(%i3) featurep (x, FOO);
(%o3)                         true
```

See also: `status`.

### Function: forget (forget, pred_1, ..., pred_n, forget, L)

Removes predicates established by `assume`.
The predicates may be expressions equivalent to (but not necessarily identical
to) those previously assumed.


`forget (L)`, where *L* is a list of predicates,
forgets each item on the list.

See also: `assume`.

### Function: get (a, i)

Retrieves the user property indicated by *i* associated with
atom *a* or returns `false` if *a* doesn’t have property *i*.


`get` evaluates its arguments.


See also `put` and `qput`.


















```maxima
maxima

(%i1) put (%e, 'transcendental, 'type);
(%o1)                    transcendental

(%i2) put (%pi, 'transcendental, 'type)$
(%i3) put (%i, 'algebraic, 'type)$

(%i4) typeof (expr) := block ([q],
        if numberp (expr)
        then return ('algebraic),
        if not atom (expr)
        then return (maplist ('typeof, expr)),
        q: get (expr, 'type),
        if q=false
        then errcatch (error(expr,"is not numeric.")) else q)$


(%i5) typeof (2*%e + x*%pi);
x is not numeric.
(%o5)  [[transcendental, []], [algebraic, transcendental]]


(%i6) typeof (2*%e + %pi);
(%o6)     [transcendental, [algebraic, transcendental]]
```

See also: `put`, `qput`.

### Variable: integer

`declare(a, integer)` or `declare(a, noninteger)` tells
Maxima to recognize *a* as an integer or noninteger variable.


See also `declare`.


Example:








```maxima
maxima

(%i1) declare(n, integer, x, noninteger);
(%o1)                         done


(%i2) askinteger(n);
(%o2)                          yes


(%i3) askinteger(x);
(%o3)                          no
```

See also: `declare`.

### Variable: integervalued

`declare(f, integervalued)` tells Maxima to recognize *f* as an
integer-valued function.


See also `declare`.


Example:








```maxima
maxima

(%i1) exp(%i)^f(x);
                              %i f(x)
(%o1)                       %e


(%i2) declare(f, integervalued);
(%o2)                         done


(%i3) exp(%i)^f(x);
                              %i f(x)
(%o3)                       %e
```

See also: `declare`.

### Function: is (expr)

Attempts to determine whether the predicate *expr* is provable from the
facts in the `assume` database.


If the predicate is provably `true` or `false`, `is` returns
`true` or `false`, respectively.  Otherwise, the return value is
governed by the global flag `prederror`.  When `prederror` is
`true`, `is` complains with an error message.  Otherwise, `is`
returns `unknown`.


`ev(expr, pred)` (which can be written  `expr, pred` at
the interactive prompt) is equivalent to `is(expr)`.


See also `assume`, `facts`, and `maybe`.


Examples:


`is` causes evaluation of predicates.







```maxima
maxima

(%i1) %pi > %e;
(%o1)                       %pi > %e


(%i2) is (%pi > %e);
(%o2)                         true
```


`is` attempts to derive predicates from the `assume` database.










```maxima
maxima

(%i1) assume (a > b);
(%o1)                        [a > b]


(%i2) assume (b > c);
(%o2)                        [b > c]


(%i3) is (a < b);
(%o3)                         false


(%i4) is (a > c);
(%o4)                         true


(%i5) is (equal (a, c));
(%o5)                         false
```


If `is` can neither prove nor disprove a predicate from the `assume`
database, the global flag `prederror` governs the behavior of `is`.









Unable to evaluate predicate a > 0
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) assume (a > b);
(%o1)                        [a > b]

(%i2) prederror: true$
(%i3) is (a > 0);
(%i4) prederror: false$

(%i5) is (a > 0);
(%o5)                        unknown
```

See also: `prederror`, `assume`, `facts`, `maybe`.

### Function: killcontext (context_1, ..., context_n)

Kills the contexts *context_1*, ..., *context_n*.


If one of the contexts is the current context, the new current context will
become the first available subcontext of the current context which has not been
killed.  If the first available unkilled context is `global` then
`initial` is used instead.  If the `initial` context is killed, a
new, empty `initial` context is created.


`killcontext` refuses to kill a context which is
currently active, either because it is a subcontext of the current
context, or by use of the function `activate`.


`killcontext` evaluates its arguments.
`killcontext` returns `done`.

See also: `activate`.

### Function: maybe (expr)

Attempts to determine whether the predicate *expr* is provable from the
facts in the `assume` database.


If the predicate is provably `true` or `false`, `maybe` returns
`true` or `false`, respectively.  Otherwise, `maybe` returns
`unknown`.


`maybe` is functionally equivalent to `is` with
`prederror: false`, but the result is computed without actually assigning
a value to `prederror`.


See also `assume`, `facts`, and `is`.


Examples:








```maxima
maxima

(%i1) maybe (x > 0);
(%o1)                        unknown


(%i2) assume (x > 1);
(%o2)                        [x > 1]


(%i3) maybe (x > 0);
(%o3)                         true
```

See also: `assume`, `facts`, `is`.

### Function: newcontext (newcontext, name, newcontext)

Creates a new, empty context, called *name*, which
has `global` as its only subcontext.  The newly-created context
becomes the currently active context.


If *name* is not specified, a new name is created (via `gensym`) and returned.


`newcontext` evaluates its argument.
`newcontext` returns *name* (if specified) or the new context name.

### Function: nonarray ()

The command `declare(a, nonarray)` tells Maxima to consider *a* not
an array.  This declaration prevents multiple evaluation, if *a* is a
subscripted variable.


See also `declare`.


Example:









```maxima
maxima
(%i1) a:'b$ b:'c$ c:'d$

(%i4) a[x];
(%o4)                          d
                                x


(%i5) declare(a, nonarray);
(%o5)                         done


(%i6) a[x];
(%o6)                          a
                                x
```

See also: `declare`.

### Variable: nonscalar

Makes atoms behave as does a list or matrix with respect to the dot operator.


See also `declare`.

See also: `declare`.

### Function: nonscalarp (expr)

Returns `true` if *expr* is a non-scalar, i.e., it contains
atoms declared as non-scalars, lists, or matrices.


See also the predicate function `scalarp` and `declare`.

See also: `scalarp`, `declare`.

### Function: notequal (a, b)

Represents the negation of `equal(a, b)`.


Examples:















```maxima
maxima

(%i1) equal (a, b);
(%o1)                      equal(a, b)


(%i2) maybe (equal (a, b));
(%o2)                        unknown


(%i3) notequal (a, b);
(%o3)                    notequal(a, b)


(%i4) not equal (a, b);
(%o4)                    notequal(a, b)


(%i5) maybe (notequal (a, b));
(%o5)                        unknown


(%i6) assume (a > b);
(%o6)                        [a > b]


(%i7) equal (a, b);
(%o7)                      equal(a, b)


(%i8) maybe (equal (a, b));
(%o8)                         false


(%i9) notequal (a, b);
(%o9)                    notequal(a, b)


(%i10) maybe (notequal (a, b));
(%o10)                        true
```

### Variable: posfun

`declare (f, posfun)` declares `f` to be a positive function.
`is (f(x) > 0)` yields `true`.


See also `declare`.

See also: `declare`.

### Function: printprops (printprops, a, i, printprops, a_1, ..., a_n, i, printprops, all, i)

Displays the property with the indicator *i* associated with the atom
*a*.  *a* may also be a list of atoms or the atom `all` in which
case all of the atoms with the given property will be used.  For example,
`printprops ([f, g], atvalue)`.  `printprops` is for properties that
cannot otherwise be displayed, i.e.  for `atvalue`,
`atomgrad`, `gradef`, and `matchdeclare`.

See also: `atvalue`, `atomgrad`, `gradef`, `matchdeclare`.

### Function: properties (a)

Returns a list of the names of all the properties associated with the atom
*a*.

### Variable: props

Default value: `[]`


`props` are atoms which have any property other than those explicitly
mentioned in `infolists`, such as specified by `atvalue`,
`matchdeclare`, etc., as well as properties specified in the
`declare` function.

See also: `infolists`, `atvalue`, `matchdeclare`, `declare`.

### Function: propvars (prop)

Returns a list of those atoms on the `props` list which
have the property indicated by *prop*.  Thus `propvars (atvalue)`
returns a list of atoms which have atvalues.

See also: `props`.

### Function: put (atom, value, indicator)

Assigns *value* to the property (specified by *indicator*) of
*atom*.  *indicator* may be the name of any property, not just a
system-defined property.


`rem` reverses the effect of `put`.


`put` evaluates its arguments.
`put` returns *value*.


See also `qput` and `get`.


Examples:










```maxima
maxima

(%i1) put (foo, (a+b)^5, expr);
                                   5
(%o1)                       (b + a)


(%i2) put (foo, "Hello", str);
(%o2)                         Hello


(%i3) properties (foo);
(%o3)            [[user properties, str, expr]]


(%i4) get (foo, expr);
                                   5
(%o4)                       (b + a)


(%i5) get (foo, str);
(%o5)                         Hello
```

See also: `rem`, `qput`, `get`.

### Function: qput (atom, value, indicator)

Assigns *value* to the property (specified by *indicator*) of
*atom*.  This is the same as `put`, except that the arguments are
quoted.


See also `get`.


Example:














```maxima
maxima
(%i1) foo: aa$
(%i2) bar: bb$
(%i3) baz: cc$

(%i4) put (foo, bar, baz);
(%o4)                          bb


(%i5) properties (aa);
(%o5)                [[user properties, cc]]


(%i6) get (aa, cc);
(%o6)                          bb


(%i7) qput (foo, bar, baz);
(%o7)                          bar


(%i8) properties (foo);
(%o8)            [value, [user properties, baz]]


(%i9) get ('foo, 'baz);
(%o9)                          bar
```

See also: `put`, `get`.

### Variable: rational

`declare(a, rational)` or `declare(a, irrational)` tells
Maxima to recognize *a* as a rational or irrational real variable.


See also `declare`.

See also: `declare`.

### Variable: real

`declare(a, real)`, `declare(a, imaginary)`, or
`declare(a, complex)` tells Maxima to recognize *a* as a real,
pure imaginary, or complex variable.


See also `declare`.

See also: `declare`.

### Function: rem (atom, indicator)

Removes the property indicated by *indicator* from *atom*.
`rem` reverses the effect of `put`.


`rem` returns `done` if *atom* had an *indicator* property
when `rem` was called, or `false` if it had no such property.

See also: `put`.

### Function: remove (remove, a_1, p_1, ..., a_n, p_n, remove, a_1, ..., a_m, p_1, ..., p_n, ..., remove, ", a, ", operator, remove, a, transfun, remove, all, p)

Removes properties associated with atoms.


`remove (a_1, p_1, ..., a_n, p_n)`
removes property `p_k` from atom `a_k`.


`remove ([a_1, ..., a_m], [p_1, ..., p_n], ...)`
removes properties `p_1, ..., p_n`
from atoms *a_1*, ..., *a_m*.
There may be more than one pair of lists.



`remove (all, p)` removes the property *p* from all atoms which
have it.



The removed properties may be system-defined properties such as
`function`, `macro`, or `mode_005fdeclare`.
`remove` does not remove properties defined by `put`.




A property may be `transfun` to remove
the translated Lisp version of a function.
After executing this, the Maxima version of the function is executed
rather than the translated version.


`remove ("a", operator)` or, equivalently,
`remove ("a", op)` removes from *a* the operator properties
declared by `prefix`, `infix`,
`function_005fnary`, `postfix`, `matchfix`, or
`nofix`.  Note that the name of the operator must be written as a quoted
string.


`remove` always returns `done` whether or not an atom has a specified
property.  This behavior is unlike the more specific remove functions
`remvalue`, `remarray`, `remfunction`, and
`remrule`.


`remove` quotes its arguments.

See also: `mode_declare`, `put`, `prefix`, `infix`, `function_nary`, `postfix`, `matchfix`, `nofix`, `remvalue`, `remarray`, `remfunction`, `remrule`.

### Variable: scalar

`declare(a, scalar)` tells Maxima to consider *a* a scalar
variable.


See also `declare`.

See also: `declare`.

### Function: scalarp (expr)

Returns `true` if *expr* is a number, constant, or variable declared
`scalar` with `declare`, or composed entirely of numbers,
constants, and such variables, but not containing matrices or lists.


See also the predicate function `nonscalarp`.

See also: `scalar`, `declare`, `nonscalarp`.

### Function: sign (expr)

Attempts to determine the sign of *expr* on the basis of the facts in the
current data base.  It returns one of the following answers: `pos`
(positive), `neg` (negative), `zero`, `pz` (positive or zero),
`nz` (negative or zero), `pn` (positive or negative), or `pnz`
(positive, negative, or zero, i.e. nothing known).


Note that this function assumes that *expr* is a real-valued
expression, such that for example `sign(sqrt(x))` will yield `pz`
even though `sqrt(x)` may return a complex-valued result for `x<0`.


See also `signum`.

See also: `signum`.

### Function: supcontext (supcontext, name, context, supcontext, name, supcontext)

Creates a new context, called *name*, which has *context* as a
subcontext.  *context* must exist.


If *context* is not specified, the current context is assumed.


If *name* is not specified, a new name is created (via `gensym`) and returned.


`supcontext` evaluates its argument.
`supcontext` returns *name* (if specified) or the new context name.

### Function: unknown (expr)

Returns `true` if and only if *expr* contains an operator or function
not recognized by the Maxima simplifier.

### Function: zeroequiv (expr, v)

Tests whether the expression *expr* in the variable *v* is equivalent
to zero, returning `true`, `false`, or `dontknow`.


`zeroequiv` has these restrictions:



1. Do not use functions that Maxima does not know how to
differentiate and evaluate.
2. If the expression has poles on the real line, there may be errors
in the result (but this is unlikely to occur).
3. If the expression contains functions which are not solutions to first order
differential equations (e.g. Bessel functions) there may be incorrect results.
4. The algorithm uses evaluation at randomly chosen points for carefully selected
subexpressions.  This is always a somewhat hazardous business, although the
algorithm tries to minimize the potential for error.


For example `zeroequiv (sin(2 * x) - 2 * sin(x) * cos(x), x)` returns
`true` and `zeroequiv (%e^x + x, x)` returns `false`.
On the other hand `zeroequiv (log(a * b) - log(a) - log(b), a)` returns 
`dontknow` because of the presence of an extra parameter `b`.

