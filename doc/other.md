## Other

### Variable: %e_to_numlog

Default value: `false`


When `true`, `r` some rational number, and `x` some expression,
`%e^(r*log(x))` will be simplified into `x^r` .  It should be noted
that the `radcan` command also does this transformation, and more
complicated transformations of this ilk as well.  The `logcontract`
command "contracts" expressions containing `log`.

### Variable: %emode

Default value: `true`


When `%emode` is `true`, `%e^(%pi %i x)` is simplified as
follows.


`%e^(%pi %i x)` simplifies to `cos (%pi x) + %i sin (%pi x)` if
`x` is a floating point number, an integer, or a multiple of 1/2, 1/3, 1/4,
or 1/6, and then further simplified.


For other numerical `x`, `%e^(%pi %i x)` simplifies to
`%e^(%pi %i y)` where `y` is `x - 2 k` for some integer `k`
such that `abs(y) < 1`.


When `%emode` is `false`, no special simplification of
`%e^(%pi %i x)` is carried out.












```maxima
maxima

(%i1) %emode;
(%o1)                         true


(%i2) %e^(%pi*%i*1);
(%o2)                          - 1


(%i3) %e^(%pi*%i*216/144);
(%o3)                         - %i


(%i4) %e^(%pi*%i*192/144);
                          sqrt(3) %i   1
(%o4)                   - ---------- - -
                              2        2


(%i5) %e^(%pi*%i*180/144);
                           %i         1
(%o5)                  - ------- - -------
                         sqrt(2)   sqrt(2)


(%i6) %e^(%pi*%i*120/144);
                          %i   sqrt(3)
(%o6)                     -- - -------
                          2       2


(%i7) %e^(%pi*%i*121/144);
                            121 %i %pi
                            ----------
                               144
(%o7)                     %e
```

### Variable: %enumer

Default value: `false`


When `%enumer` is `true`, `%e` is replaced by its numeric value
2.718...  whenever `numer` is `true`.


When `%enumer` is `false`, this substitution is carried out
only if the exponent in `%e^x` evaluates to a number.


See also `ev` and `numer`.














```maxima
maxima

(%i1) %enumer;
(%o1)                         false


(%i2) numer;
(%o2)                         false


(%i3) 2*%e;
(%o3)                         2 %e


(%i4) %enumer: not %enumer;
(%o4)                         true


(%i5) 2*%e;
(%o5)                         2 %e


(%i6) numer: not numer;
(%o6)                         true


(%i7) 2*%e;
(%o7)                   5.43656365691809


(%i8) 2*%e^1;
(%o8)                   5.43656365691809


(%i9) 2*%e^x;
                                         x
(%o9)                 2 2.718281828459045
```

See also: `ev`, `numer`.

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

### Function: adjust_external_format ()

Prints information about the current external format of the Lisp reader 
and in case the external format encoding differs from the encoding of the 
application which runs Maxima `adjust_external_format` tries to adjust 
the encoding or prints some help or instruction.
`adjust_external_format` returns `true` when the external format has 
been changed and `false` otherwise.


Functions like `cint`, `unicode`, `octets_005fto_005fstring` 
and `string_005fto_005foctets` need UTF-8 as the external format of the 
Lisp reader to work properly over the full range of Unicode characters. 


Examples (Maxima on Windows, March 2016): 
Using `adjust_external_format` when the default external format 
is not equal to the encoding provided by the application.


1. Command line Maxima


In case a terminal session is preferred it is recommended to use Maxima compiled 
with SBCL. Here Unicode support is provided by default and calls to 
`adjust_external_format` are unnecessary. 


If Maxima is compiled with CLISP or GCL it is recommended to change 
the terminal encoding from CP850 to CP1252. 
`adjust_external_format` prints some help. 


CCL reads UTF-8 while the terminal input is CP850 by default. 
CP1252 is not supported by CCL. `adjust_external_format` 
prints instructions for changing the terminal encoding and external format 
both to iso-8859-1.


2. wxMaxima


In wxMaxima SBCL reads CP1252 by default but the input from the application 
is UTF-8 encoded. Adjustment is needed. 


Calling `adjust_external_format` and restarting Maxima 
permanently changes the default external format to UTF-8.



```maxima
(%i1)adjust_external_format();
The line
(setf sb-impl::*default-external-format* :utf-8)
has been appended to the init file
C:/Users/Username/.sbclrc
Please restart Maxima to set the external format to UTF-8.
(%i1) false
```


Restarting Maxima.



```maxima
(%i1) adjust_external_format();
The external format is currently UTF-8
and has not been changed.
(%i1) false
```

See also: `cint`, `unicode`, `octets_to_string`, `string_to_octets`.

### Function: agd (x)

Returns the inverse Gudermannian function
`log (tan (%pi/4 + x/2))`.


To use this function write first `load("functs")`.

### Function: alphacharp (char)

Returns `true` if *char* is an alphabetic character. 


To identify a non-US-ASCII character as an alphabetic character 
the underlying Lisp must provide full Unicode support. 
E.g. a German umlaut is detected as an alphabetic character with SBCL in GNU/Linux 
but not with GCL. 
(In Windows Maxima, when compiled with SBCL, must be set to UTF-8. 
See `adjust_005fexternal_005fformat` for more.) 


Example: Examination of non-US-ASCII characters.


The underlying Lisp (SBCL, GNU/Linux) is able to convert the typed character 
into a Lisp character and to examine.



```maxima
(%i1) alphacharp("u");
(%o1)                          true
```


In GCL this is not possible. An error break occurs.



```maxima
(%i1) alphacharp("u");
(%o1)                          true
(%i2) alphacharp("u");

package stringproc: u cannot be converted into a Lisp character.
 -- an error.
```

See also: `adjust_external_format`.

### Function: alphanumericp (char)

Returns `true` if *char* is an alphabetic character or a digit 
(only corresponding US-ASCII characters are regarded as digits). 


Note: See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: amortization (rate, amount, num)

Amortization table determined by a specific rate.
*rate* is the interest rate, *amount* is the amount value,
and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) amortization(0.05,56000,12)$
      "n"    "Balance"     "Interest"   "Amortization"  "Payment"      
     0.000     56000.000         0.000         0.000         0.000  
     1.000     52481.777      2800.000      3518.223      6318.223  
     2.000     48787.643      2624.089      3694.134      6318.223  
     3.000     44908.802      2439.382      3878.841      6318.223  
     4.000     40836.019      2245.440      4072.783      6318.223  
     5.000     36559.597      2041.801      4276.422      6318.223  
     6.000     32069.354      1827.980      4490.243      6318.223  
     7.000     27354.599      1603.468      4714.755      6318.223  
     8.000     22404.106      1367.730      4950.493      6318.223  
     9.000     17206.088      1120.205      5198.018      6318.223  
    10.000     11748.170       860.304      5457.919      6318.223  
    11.000      6017.355       587.408      5730.814      6318.223  
    12.000         0.000       300.868      6017.355      6318.223
```

### Variable: animation

*property* should be one of the following 4 object’s properties:
`object_005forigin`, `object_005fscale`,
`object_005fposition` or
`object_005forientation` and *positions* should be a
list of points. When the play button is pressed, the object property
will be changed sequentially through all the values in the list, at
intervals of time given by the option `scene_005ftstep`. The
rewind button can be used to point at the start of the sequence making
the animation restart after the play button is pressed again.


See also `object_005ftrack`.

See also: `object_origin`, `object_scale`, `object_position`, `object_orientation`, `scene_tstep`, `object_track`.

### Function: annuity_fv (rate, FV, num)

We can calculate the annuity knowing the desired value (future value),
it is a constant and periodic payment. *rate* is the interest rate,
*FV* is the future value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) annuity_fv(0.12,65000,10);
(%o2)                3703.970670389863
```

### Function: annuity_pv (rate, PV, num)

We can calculate the annuity knowing the present value (like an amount),
it is a constant and periodic payment. *rate* is the interest rate,
*PV* is the present value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) annuity_pv(0.12,5000,10);
(%o2)                884.9208207992202
```

### Function: arit_amortization (rate, increment, amount, num)

The amortization table determined by a specific rate and with growing payment
can be calculated by `arit_amortization`.
Notice that the payment is not constant, it presents
an arithmetic growing, increment is then the difference between two
consecutive rows in the "Payment" column.
*rate* is the interest rate, *increment* is the increment, *amount*
is the amount value, and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) arit_amortization(0.05,1000,56000,12)$
      "n"    "Balance"     "Interest"   "Amortization"  "Payment"      
     0.000     56000.000         0.000         0.000         0.000  
     1.000     57403.679      2800.000     -1403.679      1396.321  
     2.000     57877.541      2870.184      -473.863      2396.321  
     3.000     57375.097      2893.877       502.444      3396.321  
     4.000     55847.530      2868.755      1527.567      4396.321  
     5.000     53243.586      2792.377      2603.945      5396.321  
     6.000     49509.443      2662.179      3734.142      6396.321  
     7.000     44588.594      2475.472      4920.849      7396.321  
     8.000     38421.703      2229.430      6166.892      8396.321  
     9.000     30946.466      1921.085      7475.236      9396.321  
    10.000     22097.468      1547.323      8848.998     10396.321  
    11.000     11806.020      1104.873     10291.448     11396.321  
    12.000        -0.000       590.301     11806.020     12396.321
```

### Function: arithmetic (a, d, n)

Returns the *n*-th term of the arithmetic series
`a, a + d, a + 2*d, ..., a + (n - 1)*d`.


To use this function write first `load("functs")`.

### Function: arithsum (a, d, n)

Returns the sum of the arithmetic series from 1 to *n*.


To use this function write first `load("functs")`.

### Function: ascii (int)

Returns the US-ASCII character corresponding to the integer *int*
which has to be less than `128`.


See `unicode` for converting code points larger than `127`.


Examples:



```maxima
(%i1) for n from 0 thru 127 do ( 
        ch: ascii(n), 
        if alphacharp(ch) then sprint(ch),
        if n = 96 then newline() )$
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

See also: `unicode`.

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

### Variable: askexp

When `asksign` is called,
`askexp` is the expression `asksign` is testing.


At one time, it was possible for a user to inspect `askexp`
by entering a Maxima break with control-A.

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

### Function: augmented_lagrangian_method (augmented_lagrangian_method, FOM, xx, C, yy, augmented_lagrangian_method, FOM, xx, C, yy, optional_args, augmented_lagrangian_method, FOM, grad, xx, C, yy, augmented_lagrangian_method, FOM, grad, xx, C, yy, optional_args)

Returns an approximate minimum of the expression *FOM*
with respect to the variables *xx*,
holding the constraints *C* equal to zero.
*yy* is a list of initial guesses for *xx*.
The method employed is the augmented Lagrangian method (see Refs [1] and [2]).


*grad*, if present, is the gradient of *FOM* with respect to *xx*,
represented as a list of expressions,
one for each variable in *xx*.
If not present, the gradient is constructed automatically.


*FOM* and each element of *grad*, if present,
must be ordinary expressions, not names of functions or lambda expressions.


`optional_args` represents additional arguments,
specified as `symbol = value`.
The optional arguments recognized are:



**niter** — Number of iterations of the augmented Lagrangian algorithm
**lbfgs_tolerance** — Tolerance supplied to LBFGS
**iprint** — IPRINT parameter (a list of two integers which controls verbosity) supplied to LBFGS
**%lambda** — Initial value of `%lambda` to be used for calculating the augmented Lagrangian


This implementation minimizes the augmented Lagrangian by
applying the limited-memory BFGS (LBFGS) algorithm,
which is a quasi-Newton algorithm.


`load("augmented_lagrangian")` loads this function.


See also `Package-lbfgs`


References:



[1] [http://www-fp.mcs.anl.gov/otc/Guide/OptWeb/continuous/constrained/nonlinearcon/auglag.html]()


[2] [http://www.cs.ubc.ca/spider/ascher/542/chap10.pdf]()


Examples:












```maxima
(%i1) load ("lbfgs");
(%o1)  /home/gunter/src/maxima-code/share/lbfgs/lbfgs.mac


(%i2) load ("augmented_lagrangian");
(%o2) /home/gunter/src/maxima-code/share/contrib/augmented_lagra\
ngian.mac


(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x


(%i4) xx: [x, y];
(%o4)                        [x, y]


(%i5) C: [x + y - 1];
(%o5)                      [y + x - 1]


(%i6) yy: [1, 1];
(%o6)                        [1, 1]


(%i7) augmented_lagrangian_method(FOM, xx, C, yy, iprint=[-1,0]);
(%o7) [[x = 0.666659841080023, y = 0.333340272455448], 
                                 %lambda = [- 1.333337940892518]]
```


Same example as before, but this time the gradient is supplied as an argument.














```maxima
(%i1) load ("lbfgs")$
(%i2) load ("augmented_lagrangian")$

(%i3) FOM: x^2 + 2*y^2;
                               2    2
(%o3)                       2 y  + x


(%i4) xx: [x, y];
(%o4)                        [x, y]


(%i5) grad : [2*x, 4*y];
(%o5)                      [2 x, 4 y]


(%i6) C: [x + y - 1];
(%o6)                      [y + x - 1]


(%i7) yy: [1, 1];
(%o7)                        [1, 1]


(%i8) augmented_lagrangian_method ([FOM, grad], xx, C, yy,
                             iprint = [-1, 0]);
(%o8) [[x = 0.6666598410800247, y = 0.3333402724554464], 
                                 %lambda = [- 1.333337940892525]]
```

See also: `Package-lbfgs`.

### Variable: background

Default value: `black`


The color of the graphics window’s background. It accepts color names or
hexadecimal red-green-blue strings (see the `color` option of plot2d).

See also: `color`.

### Function: benefit_cost (rate, input, output)

Calculates the ratio Benefit/Cost. Benefit is the Net Present Value (NPV)
of the inputs, and Cost is the Net Present Value (NPV) of the outputs.
Notice that if there is not an input or output value in a specific period,
the input/output would be a zero for that period.
*rate* is the interest rate, *input* is a list of input values,
and *output* is a list of output values.


Example:



```maxima
(%i1) load("finance")$
(%i2) benefit_cost(0.24,[0,300,500,150],[100,320,0,180]);
(%o2)               1.427249324905784
```

### Function: bernstein_approx (f, [x1, x1, ..., xn], n)

Return the `n`-th order uniform Bernstein polynomial approximation for the
function `(x1, x2, ..., xn) |--> f`.
Examples



```maxima
(%i1) bernstein_approx(f(x),[x], 2);
                 2       1                          2
(%o1)      f(1) x  + 2 f(-) (1 - x) x + f(0) (1 - x)
                         2
(%i2) bernstein_approx(f(x,y),[x,y], 2);
               2  2       1                2
(%o2) f(1, 1) x  y  + 2 f(-, 1) (1 - x) x y
                          2
                  2  2          1   2
 + f(0, 1) (1 - x)  y  + 2 f(1, -) x  (1 - y) y
                                2
       1  1                               1         2
 + 4 f(-, -) (1 - x) x (1 - y) y + 2 f(0, -) (1 - x)  (1 - y) y
       2  2                               2
            2        2       1                      2
 + f(1, 0) x  (1 - y)  + 2 f(-, 0) (1 - x) x (1 - y)
                             2
                  2        2
 + f(0, 0) (1 - x)  (1 - y)
```


To use `bernstein_approx`, first `load("bernstein")`.

### Function: bernstein_expand (e, [x1, x1, ..., xn])

Express the *polynomial* `e` exactly as a linear combination of multi-variable
Bernstein polynomials.



```maxima
(%i1) bernstein_expand(x*y+1,[x,y]);
(%o1)    2 x y + (1 - x) y + x (1 - y) + (1 - x) (1 - y)
(%i2) expand(%);
(%o2)                        x y + 1
```


Maxima signals an error when the first argument isn’t a polynomial.


To use `bernstein_expand`, first `load("bernstein")`.

### Variable: bernstein_explicit

Default value: `false`


When either `k` or `n` are non integers, the option variable 
`bernstein_explicit` controls the expansion of `bernstein(k,n,x)` 
into its explicit form; example:



```maxima
(%i1) bernstein_poly(k,n,x);
(%o1)                bernstein_poly(k, n, x)
(%i2) bernstein_poly(k,n,x), bernstein_explicit : true;
                                       n - k  k
(%o2)            binomial(n, k) (1 - x)      x
```

When both `k` and `n` are explicitly integers, `bernstein(k,n,x)` 
*always* expands to its explicit form.

### Function: bernstein_poly (k, n, x)

Provided `k` is not a negative integer, the Bernstein polynomials
are defined by `bernstein_poly(k,n,x) = binomial(n,k) x^k (1-x)^(n-k)`; for a negative integer `k`, the Bernstein polynomial
`bernstein_poly(k,n,x)` vanishes.  When either `k` or `n` are
non integers, the option variable `bernstein_explicit`
controls the expansion of the Bernstein polynomials into its explicit form;
example:



```maxima
(%i1) load("bernstein")$

(%i2) bernstein_poly(k,n,x);
(%o2)                bernstein_poly(k, n, x)
(%i3) bernstein_poly(k,n,x), bernstein_explicit : true;
                                       n - k  k
(%o3)            binomial(n, k) (1 - x)      x
```


The Bernstein polynomials have both a gradef property and an integrate property:



```maxima
(%i4) diff(bernstein_poly(k,n,x),x);
(%o4) (bernstein_poly(k - 1, n - 1, x)
                                 - bernstein_poly(k, n - 1, x)) n
(%i5) integrate(bernstein_poly(k,n,x),x);
(%o5) 
                                                            k + 1
 hypergeometric([k + 1, k - n], [k + 2], x) binomial(n, k) x
 ----------------------------------------------------------------
                              k + 1
```


For numeric inputs, both real and complex, the Bernstein polynomials evaluate
to a numeric result:



```maxima
(%i6) bernstein_poly(5,9, 1/2 + %i);
                        39375 %i   39375
(%o6)                   -------- + -----
                          128       256
(%i7) bernstein_poly(5,9, 0.5b0 + %i);
(%o7)           3.076171875b2 %i + 1.5380859375b2
```


To use `bernstein_poly`, first `load("bernstein")`.

### Function: binlist (binlist, k, binlist, k, n)

`binlist`(*k*), where *k* must be a natural number,
returns a list of binary digits 0 or 1 corresponding to the digits of
*k* in binary representation. `binlist`(*k*, *n*) does
the same but returns a list of length *n*, with leading zeros as
necessary. Notice that for the result to represent a possible state of
*m* qubits, *n* should be equal to 2^*m* and *k* should
be between 0 and 2^*m*-1.

### Function: binlist2dec (lst)

Given a list *lst* with *n* binary digits, it returns the decimal
number it represents.

### Function: bit_and (int1, ...)

This function calculates a bitwise `and` of two or more signed integers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_and(i,i);
(%o2)                           i


(%i3) bit_and(i,i,i);
(%o3)                           i


(%i4) bit_and(1,3);
(%o4)                           1


(%i5) bit_and(-7,7);
(%o5)                           1
```


If it is known if one of the parameters to `bit_and` is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_and(1,e);
(%o3)                           0


(%i4) bit_and(1,o);
(%o4)                           1
```

### Function: bit_length (int)

determines how many bits a variable needs to be long in order to store the
number `int`. This function only operates on positive numbers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_length(0);
(%o2)                           0


(%i3) bit_length(1);
(%o3)                           1


(%i4) bit_length(7);
(%o4)                           3


(%i5) bit_length(8);
(%o5)                           4
```

### Function: bit_lsh (int, nBits)

This function shifts all bits of the signed integer `int` to the left by
`nBits` bits. The width of the integer is extended by `nBits` for
this process. The result of `bit_lsh` therefore is `int * 2`.












```maxima
(%i1) load("bitwise")$

(%i2) bit_lsh(0,1);
(%o2)                           0


(%i3) bit_lsh(1,0);
(%o3)                           1


(%i4) bit_lsh(1,1);
(%o4)                           2


(%i5) bit_lsh(1,i);
(%o5)                     bit_lsh(1, i)


(%i6) bit_lsh(-3,1);
(%o6)                          - 6


(%i7) bit_lsh(-2,1);
(%o7)                          - 4
```

### Function: bit_not (int)

Inverts all bits of a signed integer. The result of this action reads
`-int - 1`.











```maxima
(%i1) load("bitwise")$

(%i2) bit_not(i);
(%o2)                      bit_not(i)


(%i3) bit_not(bit_not(i));
(%o3)                           i


(%i4) bit_not(3);
(%o4)                          - 4


(%i5) bit_not(100);
(%o5)                         - 101


(%i6) bit_not(-101);
(%o6)                          100
```

### Function: bit_onep (int, nBit)

determines if bits `nBit` is set in the signed integer `int`.












```maxima
(%i1) load("bitwise")$

(%i2) bit_onep(85,0);
(%o2)                         true


(%i3) bit_onep(85,1);
(%o3)                         false


(%i4) bit_onep(85,2);
(%o4)                         true


(%i5) bit_onep(85,3);
(%o5)                         false


(%i6) bit_onep(85,100);
(%o6)                         false


(%i7) bit_onep(i,100);
(%o7)                   bit_onep(i, 100)
```


For signed numbers the sign bit is interpreted to be more than `nBit` to the
left of the leftmost bit of `int` that reads `1`.










```maxima
(%i1) load("bitwise")$

(%i2) bit_onep(-2,0);
(%o2)                         false


(%i3) bit_onep(-2,1);
(%o3)                         true


(%i4) bit_onep(-2,2);
(%o4)                         true


(%i5) bit_onep(-2,3);
(%o5)                         true


(%i6) bit_onep(-2,4);
(%o6)                         true
```



If it is known if the number to be tested is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_onep(e,0);
(%o3)                         false


(%i4) bit_onep(o,0);
(%o4)                         true
```

### Function: bit_or (int1, ...)

This function calculates a bitwise `or` of two or more signed integers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_or(i,i);
(%o2)                           i


(%i3) bit_or(i,i,i);
(%o3)                           i


(%i4) bit_or(1,3);
(%o4)                           3


(%i5) bit_or(-7,7);
(%o5)                          - 1
```


If it is known if one of the parameters to `bit_or` is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_or(1,e);
(%o3)                         e + 1


(%i4) bit_or(1,o);
(%o4)                           o
```

### Function: bit_rsh (int, nBits)

This function shifts all bits of the signed integer `int` to the right by
`nBits` bits. The width of the integer is reduced by `nBits` for
this process.













```maxima
(%i1) load("bitwise")$

(%i2) bit_rsh(0,1);
(%o2)                           0


(%i3) bit_rsh(2,0);
(%o3)                           2


(%i4) bit_rsh(2,1);
(%o4)                           1


(%i5) bit_rsh(2,2);
(%o5)                           0


(%i6) bit_rsh(-3,1);
(%o6)                          - 2


(%i7) bit_rsh(-2,1);
(%o7)                          - 1


(%i8) bit_rsh(-2,2);
(%o8)                          - 1
```

### Function: bit_xor (int1, ...)

This function calculates a bitwise `or` of two or more signed integers.










```maxima
(%i1) load("bitwise")$

(%i2) bit_xor(i,i);
(%o2)                           0


(%i3) bit_xor(i,i,i);
(%o3)                           i


(%i4) bit_xor(1,3);
(%o4)                           2


(%i5) bit_xor(-7,7);
(%o5)                          - 2
```


If it is known if one of the parameters to `bit_xor` is even this information
is taken into consideration by the function.








```maxima
(%i1) load("bitwise")$

(%i2) declare(e,even,o,odd);
(%o2)                         done


(%i3) bit_xor(1,e);
(%o3)                         e + 1


(%i4) bit_xor(1,o);
(%o4)                         o - 1
```

### Function: bug_report ()

Prints out Maxima and Lisp version numbers, and gives a link
to the Maxima project [https://sourceforge.net/p/maxima/bugsbug report web page]().
The version information is the same as reported by `build_005finfo`.


When a bug is reported, it is helpful to copy the Maxima
and Lisp version information into the bug report.


`bug_report` returns an empty string `""`.

See also: `build_info`.

### Function: build_info ()

Returns a summary of the parameters of the Maxima build,
as a Maxima structure (defined by `defstruct`).
When the pretty-printer is enabled (via `display2d`),
the structure is displayed as a short table.


The fields of the structure are:



- * 
version Maxima version
- * 
timestamp Time at which Maxima was compiled
- * 
host Type of system Maxima is running on
- * 
lisp_name Name of the Lisp implementation
- * 
lisp_version Version of the Lisp implementation
- * 
maxima_userdir User directory (value of `maxima_userdir`)
- * 
maxima_tempdir Directory for temporary files (value of `maxima_tempdir`)
- * 
maxima_objdir Directory for compiled files of share packages (value of `maxima_objdir`)
- * 
maxima_frontend Name of user interface, if any (value of `maxima_frontend`)
- * 
maxima_frontend_version User interface version when `maxima_frontend` is present (value of `maxima_frontend_version`)


See also `bug_005freport`.


Examples:













```maxima
(%i1) build_info ();
(%o1) 
Maxima-version: "5.48.1"
Maxima build date: "2025-08-23 10:39:15"
Host type: "x86_64-pc-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49.93+ (2024-07-04) (built 3935171094) (memory 3964959574)"
User dir: "/home/dodier/.maxima"
Temp dir: "/tmp"
Object dir: "/home/dodier/.maxima/binary/5_48_1/clisp/2_49_93___2024_07_04___built_3935171094___memory_3964959574_"
Frontend: false


(%i2) x : build_info ()$
(%i3) x@version;
(%o3)                               5.48.1


(%i4) x@timestamp;
(%o4)                         2025-08-23 10:39:15


(%i5) x@host;
(%o5)                         x86_64-pc-linux-gnu


(%i6) x@lisp_name;
(%o6)                                CLISP


(%i7) x@lisp_version;
(%o7)        2.49.93+ (2024-07-04) (built 3935171094) (memory 3964959574)


(%i8) x;
(%o8) 
Maxima-version: "5.48.1"
Maxima build date: "2025-08-23 10:39:15"
Host type: "x86_64-pc-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49.93+ (2024-07-04) (built 3935171094) (memory 3964959574)"
User dir: "/home/dodier/.maxima"
Temp dir: "/tmp"
Object dir: "/home/dodier/.maxima/binary/5_48_1/clisp/2_49_93___2024_07_04___built_3935171094___memory_3964959574_"
Frontend: false
```


The Maxima version string (here 5.48.1) can look very different:



```maxima
(%i1) build_info();
(%o1) 
Maxima version: "branch_5_37_base_331_g8322940_dirty"
Maxima build date: "2016-01-01 15:37:35"
Host type: "x86_64-unknown-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49 (2010-07-07) (built 3605577779) (memory 3660647857)"
```





In that case, Maxima was not build from a released sourcecode, 
but directly from the Git checkout of the source code.
In the example, the checkout is 331 commits after the latest Git tag
(usually a Maxima release, 5.37 in our example) and the 
abbreviated commit hash of the last commit was "8322940".


User interfaces for maxima can add information about currently being used
by setting the variables `maxima_frontend` and
`maxima_frontend_version` accordingly.

See also: `display2d`, `bug_report`.

### Function: build_sample (build_sample, list, build_sample, matrix)

Builds a sample from a table of absolute frequencies.
The input table can be a matrix or a list of lists, all of
them of equal size. The number of columns or the length of
the lists must be greater than 1. The last element of each
row or list is interpreted as the absolute frequency.
The output is always a sample in matrix form.


Examples:


Univariate frequency table.









```maxima
(%i1) load ("descriptive")$

(%i2) sam1: build_sample([[6,1], [j,2], [2,1]]);
                              [ 6 ]
                              [   ]
                              [ j ]
(%o2)                         [   ]
                              [ j ]
                              [   ]
                              [ 2 ]


(%i3) mean(sam1);
                              j + 4
(%o3)                        [-----]
                                2

(%i4) barsplot(sam1) $
```


Multivariate frequency table.









```maxima
(%i1) load ("descriptive")$

(%i2) sam2: build_sample([[6,3,1], [5,6,2], [u,2,1],[6,8,2]]) ;
                            [ 6  3 ]
                            [      ]
                            [ 5  6 ]
                            [      ]
                            [ 5  6 ]
(%o2)                       [      ]
                            [ u  2 ]
                            [      ]
                            [ 6  8 ]
                            [      ]
                            [ 6  8 ]


(%i3) cov(sam2);
      [   2                 2                            ]
      [  u  + 158   (u + 28)     2 u + 174   11 (u + 28) ]
      [  -------- - ---------    --------- - ----------- ]
(%o3) [     6          36            6           12      ]
      [                                                  ]
      [ 2 u + 174   11 (u + 28)            21            ]
      [ --------- - -----------            --            ]
      [     6           12                 4             ]

(%i4) barsplot(sam2, grouping=stacked) $
```

### Variable: center

Default value: `[0, 0, 0]`


The coordinates of the object’s geometric center, with respect to its
`object_005fposition`. *point* can be a list with 3
real numbers, or 3 real numbers separated by commas. In a cylinder, cone
or cube it will be at half its height and in a sphere at its center.

See also: `object_position`.

### Function: cequal (char_1, char_2)

Returns `true` if *char_1* and *char_2* are the same character.

### Function: cequalignore (char_1, char_2)

Like `cequal` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: cgreaterp (char_1, char_2)

Returns `true` if the code point of *char_1* is greater than the 
code point of *char_2*.

### Function: cgreaterpignore (char_1, char_2)

Like `cgreaterp` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: charp (obj)

Returns `true` if *obj* is a Maxima-character.
See introduction for example.

### Function: chdir (dir)

Change to directory *dir*

### Function: cint (char)

Returns the Unicode code point of *char* which must be a 
Maxima character, i.e. a string of length `1`.


Examples: The hexadecimal code point of some characters 
(Maxima with SBCL on GNU/Linux). 



```maxima
(%i1) obase: 16.$
(%i2) map(cint, ["$","GBP","EUR"]);
(%o2)                           [24, 0A3, 20AC]
```


Warning: It is not possible to enter characters corresponding to code points 
larger than 16 bit in wxMaxima with SBCL on Windows when the external format 
has not been set to UTF-8. See `adjust_005fexternal_005fformat`.








CMUCL doesn’t process these characters as one character. 
`cint` then returns `false`. 

Converting a character to a code point via UTF-8-octets may serve as a workaround: 


`utf8_to_unicode(string_to_octets(character));`








See `utf8_005fto_005funicode`, `string_005fto_005foctets`.

See also: `adjust_external_format`, `utf8_to_unicode`, `string_to_octets`.

### Function: clebsch_gordan (j1, j2, m1, m2, j, m)

Compute the Clebsch-Gordan coefficient <j1, j2, m1, m2 | j, m>.

### Function: clessp (char_1, char_2)

Returns `true` if the code point of *char_1* is less than the 
code point of *char_2*.

### Function: clesspignore (char_1, char_2)

Like `clessp` but ignores case which is only possible for non-US-ASCII 
characters when the underlying Lisp is able to recognize a character as an 
alphabetic character. See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: CNOT (q, i, j)

Changes the value of the *j*’th qubit, in a state *q* of *m*
qubits, when the value of the *i*’th qubit equals 1. It modifies the
list *q* and returns its modified value.

### Function: collectterms (expr, arg_1, ..., arg_n)

Collects all terms that contain *arg_1* ... *arg_n*.
If several expressions have been simplified  with the following functions
`facsum`, `factorfacsum`, `factenexpand`, `facexpten` or
`factorfacexpten`, and they are to be added together, it may be desirable
to combine them using the function  `collecterms`.  `collecterms` can
take as arguments all of the arguments that can be given to these other
associated functions with the exception of `nextlayerfactor`, which has no
effect on `collectterms`.  The advantage of `collectterms` is that it
returns a form  similar to `facsum`, but since it is adding forms that have
already been processed by `facsum`, it does not need to repeat that effort.
This capability is especially useful when the expressions to be summed are very
large.


See also `factor`.


Example:







```maxima
(%i1) (exp(x)+2)*x+exp(x);
                             x          x
(%o1)                   x (%e  + 2) + %e


(%i2) collectterms(expand(%),exp(x));
                                  x
(%o2)                   (x + 1) %e  + 2 x
```

See also: `factor`.

### Function: combination (n, r)

Returns the number of combinations of *n* objects
taken *r* at a time.


To use this function write first `load("functs")`.

### Variable: cone

Creates a regular pyramid with height equal to 1 and a hexagonal base
with vertices 0.5 units away from the axis. Options
`object_005fheight` and `object_005fradius` can be used
to change those defaults and option `object_005fresolution`
can be used to change the number of edges of the base; higher values
will make it look like a cone. By default, the axis will be along the x
axis, the middle point of the axis will be at the origin and the vertex
on the positive side of the x axis; use options
`object_005forientation` and `object_005fcenter` to
change those defaults.


**Example**. This shows a pyramid that starts rotating around the z
axis when the play button is pressed.

 

```maxima
(%i1) scene([cone, [orientation,0,30,0], [tstep,100],
   [animate,orientation,makelist([0,30,i],i,5,360,5)]], restart)$
```

See also: `object_height`, `object_radius`, `object_resolution`, `object_orientation`, `object_center`.

### Function: constituent (char)

Returns `true` if *char* is a graphic character but not a space character.
A graphic character is a character one can see, plus the space character.
(`constituent` is defined by Paul Graham. 
See Paul Graham, ANSI Common Lisp, 1996, page 67.)



```maxima
(%i1) for n from 0 thru 255 do ( 
tmp: ascii(n), if constituent(tmp) then sprint(tmp) )$
! " #  %  ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c
d e f g h i j k l m n o p q r s t u v w x y z { | } ~
```

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

### Function: continuous_freq (continuous_freq, data, continuous_freq, data, m)

Divides the range of *data* into intervals,
and counts how many values fall into each one.


A value *x* falls into an interval with left and right endpoints *a* and *b*
if and only if `x > a` and `x <= b`,
except for the first (least or leftmost) interval,
for which `x >= a` and `x <= b`.
That is, an interval excludes its left endpoint and includes its right endpoint,
except for the first interval, which includes both the left and right endpoints.


*data* must be a list of numbers,
or 1-dimensional array (as created by `make_array`).


*m* is optional, and equals either the number of classes (10 by default),
or a list of two elements (the least and greatest values to be counted),
or a list of three elements (the least and greatest values to be counted, and the number of classes),
or a set containing the endpoints of the class intervals.


It is assumed that class intervals are contiguous.
That is, the right endpoint of one interval is equal to the left endpoint of the next.


`continuous_freq` returns a list of two lists.
The first list comprises all the endpoints of the class intervals,
concatenated into a single list.
The second list contains the class counts for the intervals corresponding to elements of the first list.


If sample values are all equal, this function returns exactly
one class of width 2.


Examples:


Optional argument indicates the number of classes we want.
The first list in the output contains the interval limits, and
the second the corresponding counts: there are 16 digits inside 
the interval `[0, 1.8]`, 24 digits in `(1.8, 3.6]`, and so on.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) continuous_freq (s1, 5);
               9  18  27  36
(%o3)     [[0, -, --, --, --, 9], [16, 24, 18, 17, 25]]
               5  5   5   5
```


Optional argument indicates we want 7 classes with limits
-2 and 12:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) continuous_freq (s1, [-2,12,7]);
(%o3) [[- 2, 0, 2, 4, 6, 8, 10, 12], [8, 20, 22, 17, 20, 13, 0]]
```


Optional argument indicates we want the default number of classes with limits
-2 and 12:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) continuous_freq (s1, [-2,12]);
               3  4  11  18     32  39  46  53
(%o3) [[- 2, - -, -, --, --, 5, --, --, --, --, 12], 
               5  5  5   5      5   5   5   5
                              [0, 8, 20, 12, 18, 9, 8, 25, 0, 0]]
```


The first argument may be an array.










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) a1 : make_array (fixnum, length (s1)) $

(%i4) fillarray (a1, s1);
(%o4) {Lisp Array: #(3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2\
 6 4 3 3 8 3 2 7 9 5
               0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7\
 4 9 4 4 5 9 2
               3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8\
 2 5 3 4 2 1 1
               7 0 6 7)}


(%i5) continuous_freq (a1);
           9   9  27  18  9  27  63  36  81
(%o5) [[0, --, -, --, --, -, --, --, --, --, 9], 
           10  5  10  5   2  5   10  5   10
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```

### Function: controlled (U, q, c, i)

Applies a matrix *U*, acting on *m* qubits, on qubits *i*
through *i*+*m*-1 of the state *q* of *n* qubits
(*n* > *m*), when the value of the *c*’th qubit in *q*
equals 1. *i* should be an integer between 1 and *n*+1-*m*
and *c* should be an integer between 1 and *n*, excluding the
qubits to be modified (*i* through *i*+*m*-1).


*U* can be one of the indices of the array of common matrices
*qmatrix* (see `qmatrix`). The state *q* is modified and
shown in the output.

See also: `qmatrix`.

### Function: covers (x)

Returns the coversed sine `1 - sin (x)`.


To use this function write first `load("functs")`.

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

### Variable: cube

A cube with edges of 1 unit and faces parallel to the xy, xz and yz
planes. The lengths of the three edges can be changed with options
`object_005fxlength`, `object_005fylength` and
`object_005fzlength`, turning it into a rectangular box and
the faces can be rotated with option `object_005forientation`.

See also: `object_xlength`, `object_ylength`, `object_zlength`, `object_orientation`.

### Variable: cylinder

Creates a regular prism with height equal to 1 and a hexagonal base with
vertices 0.5 units away from the axis. Options
`object_005fheight` and `object_005fradius` can be
used to change those defaults and option `object_005fresolution` can be used to change the number of edges of the base;
higher values will make it look like a cylinder. The default height can
be changed with the option `object_005fheight`. By default,
the axis will be along the x axis and the middle point of the axis will
be at the origin; use options `object_005forientation` and
`object_005fcenter` to change those defaults.

See also: `object_height`, `object_radius`, `object_resolution`, `object_orientation`, `object_center`.

### Function: days360 (year1, month1, day1, year2, month2, day2)

Calculates the distance between 2 dates, assuming 360 days years, 30 days months.


Example:



```maxima
(%i1) load("finance")$
(%i2) days360(2008,12,16,2007,3,25);
(%o2)                      - 621
```

### Function: deactivate (context_1, ..., context_n)

Deactivates the specified contexts *context_1*, ..., *context_n*.

### Function: diag (lm)

Constructs a matrix that is the block sum of the elements of
*lm*. The elements of *lm* are assumed to be matrices; if an
element is scalar, it treated as a 1 by 1 matrix.


The resulting matrix will be square if each of the elements of
*lm* is square.


Example:


```maxima
(%i1) load("diag")$

(%i2) a1:matrix([1,2,3],[0,4,5],[0,0,6])$

(%i3) a2:matrix([1,1],[1,0])$

(%i4) diag([a1,x,a2]);
                   [ 1  2  3  0  0  0 ]
                   [                  ]
                   [ 0  4  5  0  0  0 ]
                   [                  ]
                   [ 0  0  6  0  0  0 ]
(%o4)              [                  ]
                   [ 0  0  0  x  0  0 ]
                   [                  ]
                   [ 0  0  0  0  1  1 ]
                   [                  ]
                   [ 0  0  0  0  1  0 ]
(%i5) diag ([matrix([1,2]), 3]);
                        [ 1  2  0 ]
(%o5)                   [         ]
                        [ 0  0  3 ]
```


To use this function write first `load("diag")`.

### Function: digitcharp (char)

Returns `true` if *char* is a digit where only the corresponding 
US-ASCII-character is regarded as a digit.

### Function: discrete_freq (data)

Counts absolute frequencies in discrete samples, both numeric and categorical. Its sole argument is a list,
or 1-dimensional array (as created by `make_array`).


Examples:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) discrete_freq (s1);
(%o3) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```


In the return value,
the first list gives the sample values, and the second, their absolute frequencies.


The argument may be an array.










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) a1 : make_array (fixnum, length (s1)) $

(%i4) fillarray (a1, s1);
(%o4) {Lisp Array: #(3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2\
 6 4 3 3 8 3 2 7 9 5
               0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7\
 4 9 4 4 5 9 2
               3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8\
 2 5 3 4 2 1 1
               7 0 6 7)}


(%i5) discrete_freq (a1);
(%o5) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```

### Function: dispJordan (l)

Returns a matrix in Jordan canonical form (JCF) corresponding to the
list of eigenvalues and multiplicities given by *l*. This list
should be in the format given by the `jordan` function. See
`jordan` for details of this format.


Example:


```maxima
(%i1) load("diag")$

(%i2) b1:matrix([0,0,1,1,1],
                [0,0,0,1,1],
                [0,0,0,0,1],
                [0,0,0,0,0],
                [0,0,0,0,0])$

(%i3) jordan(b1);
(%o3)                  [[0, 3, 2]]
(%i4) dispJordan(%);
                    [ 0  1  0  0  0 ]
                    [               ]
                    [ 0  0  1  0  0 ]
                    [               ]
(%o4)               [ 0  0  0  0  0 ]
                    [               ]
                    [ 0  0  0  0  1 ]
                    [               ]
                    [ 0  0  0  0  0 ]
```


To use this function write first `load("diag")`. See also `jordan` and `minimalPoly`.

See also: `jordan`, `minimalPoly`.

### Variable: endphi

Default value: `180`


In a sphere phi is the angle on the vertical plane that passes through
the z axis, measured from the positive part of the z axis. *angle*
must be a number between 0 and 180 that sets the final value of phi at
which the surface will end. A value smaller than 180 will eliminate a
part of the sphere’s surface.


See also `object_005fstartphi` and
`object_005fphiresolution`.

See also: `object_startphi`, `object_phiresolution`.

### Variable: endtheta

Default value: `360`


In a sphere theta is the angle on the horizontal plane (longitude),
measured from the positive part of the x axis. *angle* must be a
number between 0 and 360 that sets the final value of theta at which the
surface will end. A value smaller than 360 will eliminate a part of
the sphere’s surface.


See also `object_005fstarttheta` and
`object_005fthetaresolution`.

See also: `object_starttheta`, `object_thetaresolution`.

### Function: erf (z)

The Error Function erf(z):

$${\rm erf}\ z = {{2\over \sqrt{\pi}}} \int_0^z e^{-t^2}\, dt$$


$${\rm erf}\ z = {{2\over \sqrt{\pi}}} \int_0^z e^{-t^2}\, dt$$




([https://personal.math.ubc.ca/~cbm/aands/page_297.htmA&S eqn 7.1.1]()) and ([https://dlmf.nist.gov/7.2.E1DLMF 7.2.E1]()).


See also flag `erfflag`.  This can also be expressed in terms
of a hypergeometric function.  `hypergeometric_005frepresentation`.

See also: `erfflag`, `hypergeometric_representation`.

### Function: erf_generalized (z1, z2)

Generalized Error function Erf(z1,z2):

$${\rm erf}(z_1, z_2) = {{2\over \sqrt{\pi}}} \int_{z_1}^{z_2} e^{-t^2}\, dt$$


$${\rm erf}(z_1, z_2) = {{2\over \sqrt{\pi}}} \int_{z_1}^{z_2} e^{-t^2}\, dt$$




This can also be expressed in terms
of a hypergeometric function.  `hypergeometric_005frepresentation`.

See also: `hypergeometric_representation`.

### Variable: erf_representation

Default value: false


`erf_representation` controls how the error functions are
represented.  It must be set to one of `false`, `erf`,
`erfc`, or `erfi`.  When set to `false`, the error functions are not
modified.  When set to `erf`, all error functions (`erfc`,
`erfi`, `erf_generalized`, `fresnel_s` and
`fresnel_c`) are converted to `erf` functions.  Similarly,
`erfc` converts error functions to `erfc`.  Finally
`erfi` converts the functions to `erfi`.


Converting to `erf`:










```maxima
maxima

(%i1) erf_representation:erf;
(%o1)                          erf


(%i2) erfc(z);
(%o2)                      1 - erf(z)


(%i3) erfi(z);
(%o3)                    - %i erf(%i z)


(%i4) erf_generalized(z1,z2);
(%o4)                   erf(z2) - erf(z1)


(%i5) fresnel_c(z);
                     sqrt(%pi) (%i + 1) z
(%o5) ((1 - %i) (erf(--------------------)
                              2
                                        sqrt(%pi) (1 - %i) z
                               + %i erf(--------------------)))/4
                                                 2


(%i6) fresnel_s(z);
                     sqrt(%pi) (%i + 1) z
(%o6) ((%i + 1) (erf(--------------------)
                              2
                                        sqrt(%pi) (1 - %i) z
                               - %i erf(--------------------)))/4
                                                 2
```


Converting to `erfc`:










```maxima
maxima

(%i1) erf_representation:erfc;
(%o1)                         erfc


(%i2) erf(z);
(%o2)                      1 - erfc(z)


(%i3) erfc(z);
(%o3)                        erfc(z)


(%i4) erf_generalized(z1,z2);
(%o4)                  erfc(z1) - erfc(z2)


(%i5) fresnel_s(c);
                        sqrt(%pi) (%i + 1) c
(%o5) ((%i + 1) (- erfc(--------------------)
                                 2
                                   sqrt(%pi) (1 - %i) c
                    - %i (1 - erfc(--------------------)) + 1))/4
                                            2


(%i6) fresnel_c(c);
                        sqrt(%pi) (%i + 1) c
(%o6) ((1 - %i) (- erfc(--------------------)
                                 2
                                   sqrt(%pi) (1 - %i) c
                    + %i (1 - erfc(--------------------)) + 1))/4
                                            2
```


Converting to `erfc`:












```maxima
maxima

(%i1) erf_representation:erfi;
(%o1)                         erfi


(%i2) erf(z);
(%o2)                    - %i erfi(%i z)


(%i3) erfc(z);
(%o3)                   %i erfi(%i z) + 1


(%i4) erfi(z);
(%o4)                        erfi(z)


(%i5) erf_generalized(z1,z2);
(%o5)            %i erfi(%i z1) - %i erfi(%i z2)


(%i6) fresnel_s(z);
                           sqrt(%pi) %i (%i + 1) z
(%o6) ((%i + 1) (- %i erfi(-----------------------)
                                      2
                                     sqrt(%pi) (1 - %i) %i z
                              - erfi(-----------------------)))/4
                                                2


(%i7) fresnel_c(z);
                      sqrt(%pi) (1 - %i) %i z
(%o7) ((1 - %i) (erfi(-----------------------)
                                 2
                                     sqrt(%pi) %i (%i + 1) z
                           - %i erfi(-----------------------)))/4
                                                2
```

See also: `erf_representation`, `false`, `erf`, `erfc`, `erfi`, `erf_generalized`, `fresnel_s`, `fresnel_c`.

### Function: erfc (z)

The Complementary Error Function erfc(z):

$${\rm erfc}\ z = 1 - {\rm erf}\ z$$


$${\rm erfc}\ z = 1 - {\rm erf}\ z$$




([https://personal.math.ubc.ca/~cbm/aands/page_297.htmA&S eqn 7.1.2]()) and ([https://dlmf.nist.gov/7.2.E2DLMF 7.2.E2]()).


This can also be expressed in terms
of a hypergeometric function.  `hypergeometric_005frepresentation`.

See also: `hypergeometric_representation`.

### Function: erfi (z)

The Imaginary Error Function. 

$${\rm erfi}\ z = -i\, {\rm erf}(i z)$$


$${\rm erfi}\ z = -i\, {\rm erf}(i z)$$

### Variable: ev_point

Default value: `big_primes[10]`


`ev_point` is the value at which the variable *n* is evaluated
when executing the modular test in `parGosper`.

### Function: exp (x)

Represents the exponential function.  Instances of `exp (x)` in input
are simplified to `%e^x`; `exp` does not appear in simplified
expressions.


`demoivre` if `true` causes `%e^(a + b %i)` to simplify to
`%e^(a (cos(b) + %i sin(b)))` if `b` is free of `%i`.
See `demoivre`.


`%emode`, when `true`, causes `%e^(%pi %i x)` to be simplified.
See `_0025emode`.


`%enumer`, when `true` causes `%e` to be replaced by
2.718... whenever `numer` is `true`.  See `_0025enumer`.









```maxima
maxima

(%i1) demoivre;
(%o1)                         false


(%i2) %e^(a + b*%i);
                             %i b + a
(%o2)                      %e


(%i3) demoivre: not demoivre;
(%o3)                         true


(%i4) %e^(a + b*%i);
                      a
(%o4)               %e  (%i sin(b) + cos(b))
```

See also: `demoivre`, `%emode`, `%enumer`.

### Function: exsec (x)

Returns the exsecant `sec (x) - 1`.


To use this function write first `load("functs")`.

### Function: facsum (expr, arg_1, ..., arg_n)

Returns  a form  of *expr*  which depends  on the
arguments *arg_1*, ..., *arg_n*.
The arguments can be any form suitable for `ratvars`, or they can be
lists  of such  forms.  If  the arguments  are not  lists, then  the form
returned is  fully expanded with respect  to the arguments,  and the
coefficients of the arguments are factored.  These  coefficients are
free of the arguments, except perhaps in a non-rational sense.


If any of the arguments are  lists, then all such lists are combined
into  a  single  list,   and  instead  of  calling  `factor`   on  the
coefficients  of  the  arguments,  `facsum`  calls  itself   on  these
coefficients, using  this newly constructed  single list as  the new
argument list  for this  recursive  call.  This  process can  be  repeated to
arbitrary depth by nesting the desired elements in lists.


It is possible that one may wish to `facsum` with respect  to more
complicated subexpressions,  such as  `log (x + y)`.  Such  arguments are
also  permissible.   







Occasionally the user may wish to obtain any of the  above forms
for expressions which are specified only by their leading operators.
For example, one may wish  to `facsum` with respect to all  `log`’s.  In
this situation, one may  include among the arguments either  the specific
`log`’s which are to be treated in this way, or  alternatively, either
the expression  `operator (log)` or `'operator (log)`.   If one  wished to
`facsum` the expression *expr* with respect to the operators *op_1*, ..., *op_n*,
one   would  evaluate  `facsum (expr, operator (op_1, ..., op_n))`.
The `operator` form may also appear inside list arguments.


In  addition,  the  setting  of  the  switches   `facsum_combine`  and
`nextlayerfactor` may affect the result of `facsum`.

### Variable: facsum_combine

Default value: `true`


`facsum_combine` controls the form  of the final result  returned by
`facsum`  when  its  argument  is  a  quotient  of   polynomials.   If
`facsum_combine` is `false`  then the form will  be returned as  a fully
expanded  sum  as described  above,  but if  `true`,  then  the expression
returned is a ratio of polynomials, with each polynomial in the form
described above.


The `true` setting of this switch is useful when one
wants to  `facsum` both  the numerator and  denominator of  a rational
expression,  but  does not  want  the denominator  to  be multiplied
through the terms of the numerator.

### Function: factorfacsum (expr, arg_1, ..., arg_n)

Returns a  form of *expr*  which is
obtained by calling  `facsum` on the factors  of *expr* with *arg_1*, ... *arg_n* as
arguments.  If any of the factors of *expr* is raised to a  power, both
the factor and the exponent will be processed in this way.

### Function: facts (facts, item, facts)

If *item* is the name of a context, `facts (item)` returns a
list of the facts in the specified context.


If *item* is not the name of a context, `facts (item)` returns a
list of the facts known about *item* in the current context.  Facts that
are active, but in a different context, are not listed.


`facts ()` (i.e., without an argument) lists the current context.

### Function: fernfale (n)

4 contractive maps, the probability to choice a transformation must be related 
with the contraction ratio. Argument *n* must be great enough, 10000 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,fernfale(n)], [style,dots])$
```

### Function: forget (forget, pred_1, ..., pred_n, forget, L)

Removes predicates established by `assume`.
The predicates may be expressions equivalent to (but not necessarily identical
to) those previously assumed.


`forget (L)`, where *L* is a list of predicates,
forgets each item on the list.

See also: `assume`.

### Function: fresnel_c (z)

The Fresnel Integral



$$C(z) = \int_0^z \cos\left({\pi \over 2} t^2\right)\, dt$$


$$C(z) = \int_0^z \cos\left({\pi \over 2} t^2\right)\, dt$$



([https://personal.math.ubc.ca/~cbm/aands/page_300.htmA&S eqn 7.3.1]()) and ([https://dlmf.nist.gov/7.2.E7DLMF 7.2.E7]()).


The simplification 
$C(-x) = -C(x)$
is applied when
flag `trigsign` is true.


The simplification 
$C(ix) = iC(x)$
is applied when
flag `%iargs` is true.


See flags `erf_representation` and `hypergeometric_representation`.

See also: `trigsign`, `%iargs`, `erf_representation`, `hypergeometric_representation`.

### Function: fresnel_s (z)

The Fresnel Integral

$$S(z) = \int_0^z \sin\left({\pi \over 2} t^2\right)\, dt$$


$$S(z) = \int_0^z \sin\left({\pi \over 2} t^2\right)\, dt$$




([https://personal.math.ubc.ca/~cbm/aands/page_300.htmA&S eqn 7.3.2]()) and ([https://dlmf.nist.gov/7.2.E8DLMF 7.2.E8]()).


The simplification 
$S(-x) = -S(x)$
is applied when
flag `trigsign` is true.


The simplification 
$S(ix) = iS(x)$
is applied when
flag `%iargs` is true.


See flags `erf_representation` and `hypergeometric_representation`.

See also: `trigsign`, `%iargs`, `erf_representation`, `hypergeometric_representation`.

### Function: fv (rate, PV, num)

We can calculate the future value of a Present one given a certain interest rate.
*rate* is the interest rate, *PV* is the present value and *num* is
the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) fv(0.12,1000,3);
(%o2)                     1404.928
```

### Function: garbage_collect ()

Tries to manually trigger the lisp’s garbage collection. This rarely is necessary
as the lisp will employ an excellent algorithm for determining when to start
garbage collection.


If maxima knows how to do manually trigger the garbage collection for the
current lisp `garbage_collect` returns `true`, else `false`.

### Function: gate (gate, U, q, gate, U, q, i, gate, U, q, i1, ..., im)

*U* must be a matrix acting on states of *m* qubits; *q* a
list corresponding to a state of *n* qubits (*n* >= *m*);
*i* and the *m* numbers *i1*, ..., *im* must be
different integers between 1 and *n*.


`gate`(*U*, *q*) applies matrix *U* to each qubit of
*q*, when *m* equals 1, or to the first *m* qubits of
*q* when *m* is bigger than 1.


`gate`(*U*, *q*, *i*) applies matrix *U* to the
qubits *i* through *i*+*m*-1 of *q*.


`gate`(*U*, *q*, *i1*, ..., *in*) applies
matrix *U* to the in the positions *i1*, ..., *im*.


*U* can be one of the indices of the array of common matrices
*qmatrix* (see `qmatrix`). The state *q* is modified and
shown in the output.

See also: `qmatrix`.

### Function: gate_matrix (gate_matrix, U, n, gate_matrix, U, n, i1, ..., im)

*U* must be a 2 by 2 matrix or one of the indices of the array of
common matrices *qmatrix* (see `qmatrix`).
`gate_matrix`(*U*, *n*) returns the matrix corresponding to
the action of *U* on each qubit in a state of *n* qubits.


`gate_matrix` (*U*, *n*, *i1*, ..., *im*)
returns the matrix corresponding to the action of *U* on qubits
*i1*, ..., *im* of a state of *n* qubits, where
*i1*, ..., *im* are different integers between 1 and
*n*.

See also: `qmatrix`.

### Function: gaussprob (x)

Returns the Gaussian probability function
`%e^(-x^2/2) / sqrt(2*%pi)`.


To use this function write first `load("functs")`.

### Function: gcdivide (p, q)

When the option variable `takegcd` is `true` which is the default,
`gcdivide` divides the polynomials *p* and *q* by their greatest
common divisor and returns the ratio of the results.  `gcdivde` calls the
function `ezgcd` to divide the polynomials by the greatest common divisor.


When `takegcd` is `false`, `gcdivide` returns the ratio
`p/q`.


To use this function write first `load("functs")`.


See also `ezgcd`, `gcd`, `gcdex`, and
`poly_005fgcd`.


Example:



```maxima
(%i1) load("functs")$

(%i2) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o2)                6 x  + 19 x  + 19 x + 6
(%i3) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o3)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i4) gcdivide(p1, p2);
                             x + 1
(%o4)                        ------
                              3
                             x  + x
(%i5) takegcd:false;
(%o5)                         false
(%i6) gcdivide(p1, p2);
                       3       2
                    6 x  + 19 x  + 19 x + 6
(%o6)          ----------------------------------
                  5       4       3       2
               6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i7) ratsimp(%);
                             x + 1
(%o7)                        ------
                              3
                             x  + x
```

See also: `ezgcd`, `gcd`, `gcdex`, `poly_gcd`.

### Function: gcfac (expr)

`gcfac` is a factoring function that attempts to apply the same heuristics which
scientists apply in trying to make expressions simpler.  `gcfac` is limited
to monomial-type factoring.  For a sum, `gcfac` does the following:



1. Factors over the integers.
2. Factors out the largest powers of terms occurring as
coefficients, regardless of the complexity of the terms.
3. Uses (1) and (2) in factoring adjacent pairs of terms.
4. Repeatedly and recursively applies these techniques until
the expression no longer changes.


Item (3) does not necessarily do an optimal job of pairwise
factoring because of the combinatorially-difficult nature of finding
which of all possible rearrangements of the pairs yields the most
compact pair-factored result.


`load ("scifac")` loads this function.
`demo ("scifac")` shows a demonstration of this function.

### Function: gd (x)

Returns the Gudermannian function
`2*atan(%e^x)-%pi/2`.


To use this function write first `load("functs")`.

### Variable: genindex

Default value: `i`


`genindex` is the alphabetic prefix used to generate the
next variable of summation when necessary.

### Variable: gensumnum

Default value: 0


`gensumnum` is the numeric suffix used to generate the next variable
of summation.  If it is set to `false` then the index will consist only
of `genindex` with no numeric suffix.

### Function: gensym (gensym, gensym, x)

`gensym()` creates and returns a fresh symbol.


The name of the new symbol is the concatenation of a prefix, which defaults to
"g", and a suffix, which is an integer that defaults to the value of an internal
counter.


If *x* is supplied, and is a string, then that string is used as a prefix 
instead of "g" for this call to gensym only.


If *x* is supplied, and is a nonnegative integer, then that integer, instead
of the value of the internal counter, is used as the suffix for this call to
gensym only.


If and only if no explicit suffix is supplied, the internal counter is
incremented after it is used.


Examples:








```maxima
(%i1) gensym();
(%o1)                         g887
(%i2) gensym("new");
(%o2)                        new888
(%i3) gensym(123);
(%o3)                         g123
```

### Function: geo_amortization (rate, growing_rate, amount, num)

The amortization table determined by rate, amount,
and number of periods can be found by `geo_amortization`.
Notice that the payment is not constant, it presents
a geometric growing, *growing_rate* is then the quotient between two
consecutive rows in the "Payment" column.
*rate* is the interest rate, *amount*
is the amount value, and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) geo_amortization(0.05,0.03,56000,12)$
      "n"    "Balance"     "Interest"   "Amortization"  "Payment"      
     0.000     56000.000         0.000         0.000         0.000  
     1.000     53365.296      2800.000      2634.704      5434.704  
     2.000     50435.816      2668.265      2929.480      5597.745  
     3.000     47191.930      2521.791      3243.886      5765.677  
     4.000     43612.879      2359.596      3579.051      5938.648  
     5.000     39676.716      2180.644      3936.163      6116.807  
     6.000     35360.240      1983.836      4316.475      6300.311  
     7.000     30638.932      1768.012      4721.309      6489.321  
     8.000     25486.878      1531.947      5152.054      6684.000  
     9.000     19876.702      1274.344      5610.176      6884.520  
    10.000     13779.481       993.835      6097.221      7091.056  
    11.000      7164.668       688.974      6614.813      7303.787  
    12.000         0.000       358.233      7164.668      7522.901
```

### Function: geo_annuity_fv (rate, growing_rate, FV, num)

We can calculate the annuity knowing the desired value (future value),
in a growing periodic payment. *rate* is the interest rate, *growing_rate*
is the growing rate, *FV* is the future value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) geo_annuity_fv(0.14,0.05,5000,10);
(%o2)                216.5203395312695
```

### Function: geo_annuity_pv (rate, growing_rate, PV, num)

We can calculate the annuity knowing the present value (like an amount),
in a growing periodic payment. *rate* is the interest rate, *growing_rate*
is the growing rate, *PV* is the present value and *num* is the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) geo_annuity_pv(0.14,0.05,5000,10);
(%o2)                802.6888176505123
```

### Function: geometric (a, r, n)

Returns the *n*-th term of the geometric series
`a, a*r, a*r^2, ..., a*r^(n - 1)`.


To use this function write first `load("functs")`.

### Function: geosum (a, r, n)

Returns the sum of the geometric series from 1 to *n*.  If *n* is
infinity (`inf`) then a sum is finite only if the absolute value
of *r* is less than 1.


To use this function write first `load("functs")`.

### Function: getcurrentdirectory ()

returns the current working directory.


See also `directory`.

See also: `directory`.

### Function: getenv (env)

Get the value of the environment variable *env*


Example:



```maxima
(%i1) load("operatingsystem")$
(%i2) getenv("PATH");
(%o2) /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

### Function: ggf (l)

Compute the generating function (if it is a fraction of two
polynomials) of a sequence, its first terms being given. *l*
is a list of numbers.


The solution is returned as a fraction of two polynomials.
If no solution has been found, it returns with `done`.


This function is controlled by global variables *GGFINFINITY* and *GGFCFMAX*. See also *GGFINFINITY* and *GGFCFMAX*.


To use this function write first `load("ggf")`.




```maxima
(%i1) load("ggf")$
(%i2) makelist(fib(n),n,0,10);
(%o2)                [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
(%i3) ggf(%);
                                       x
(%o3)                            - ----------
                                    2
                                   x  + x - 1
(%i4) taylor(%,x,0,10);
              2      3      4      5      6       7       8       9       10
(%o4)/T/ x + x  + 2 x  + 3 x  + 5 x  + 8 x  + 13 x  + 21 x  + 34 x  + 55 x
                                                                        + . . .
(%i5) makelist(2*fib(n+1)-fib(n),n,0,10);
(%o5)              [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
(%i6) ggf(%);
                                    x - 2
(%o6)                             ----------
                                   2
                                  x  + x - 1
(%i7) taylor(%,x,0,10);
                    2      3      4       5       6       7       8       9
(%o7)/T/ 2 + x + 3 x  + 4 x  + 7 x  + 11 x  + 18 x  + 29 x  + 47 x  + 76 x
                                                                     10
                                                              + 123 x   + . . .
```


As these examples show, the generating function does create a function
whose Taylor series has coefficients that are the elements of the
original list.

### Variable: GGFCFMAX

Default value: 3


This is an option variable for function `ggf`.


When computing the continued fraction of the
generating function, if no good result has been found (see
the *GGFINFINITY* flag) after having computed *GGFCFMAX* partial
quotients, the generating function will be considered as
not being a fraction of two polynomials and the function will
exit. Put freely a greater value for more complicated
generating functions.


See also `ggf`.

See also: `ggf`.

### Variable: GGFINFINITY

Default value: 3


This is an option variable for function `ggf`.


When computing the continued fraction of the
generating function, a partial quotient having a degree
(strictly) greater than *GGFINFINITY* will be discarded and
the current convergent will be considered as the exact value
of the generating function; most often the degree of all
partial quotients will be 0 or 1; if you use a greater value,
then you should give enough terms in order to make the
computation accurate enough.



See also `ggf`.

See also: `ggf`.

### Variable: Gosper_in_Zeilberger

Default value: `true`


When `Gosper_in_Zeilberger` is `true`,
the `Zeilberger` function calls `Gosper` before calling `parGosper`.
Otherwise, `Zeilberger` goes immediately to `parGosper`.

### Function: graph_flow (val)

Plots the money flow in a time line, the positive values are in blue
and upside; the negative ones are in red and downside.
The direction of the flow is given by the sign of the value.
*val* is a list of flow values.


Example:



```maxima
(%i1) load("finance")$
(%i2) graph_flow([-5000,-3000,800,1300,1500,2000])$
```

### Function: harmonic (a, b, c, n)

Returns the *n*-th term of the harmonic series
`a/b, a/(b + c), a/(b + 2*c), ..., a/(b + (n - 1)*c)`.


To use this function write first `load("functs")`.

### Function: hav (x)

Returns the haversine `(1 - cos(x))/2`.


To use this function write first `load("functs")`.

### Variable: height

Default value: `500`


The height, in pixels, of the graphics window. *pixels* must be a
positive integer number.

### Function: hilbertmap (nn)

Hilbert map. Argument *nn* must be small (5, for example).
Maxima can crash if *nn* is 7 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,hilbertmap(6)])$
```

### Variable: hypergeometric_representation

Default value: false


Enables transformation to a Hypergeometric
representation for `fresnel_s` and `fresnel_c` and other
error functions.












```maxima
maxima

(%i1) hypergeometric_representation:true;
(%o1)                         true


(%i2) fresnel_s(z);
                                               2  4
                              3    3  7     %pi  z    3
          %pi hypergeometric([-], [-, -], - -------) z
                              4    2  4       16
(%o2)     ---------------------------------------------
                                6


(%i3) fresnel_c(z);
                                             2  4
                            1    1  5     %pi  z
(%o3)       hypergeometric([-], [-, -], - -------) z
                            4    2  4       16


(%i4) erf(z);
                                                   2
                                    3    2      - z
             2 hypergeometric([1], [-], z ) z %e
                                    2
(%o4)        ---------------------------------------
                            sqrt(%pi)


(%i5) erfi(z);
                                  1    3    2
                2 hypergeometric([-], [-], z ) z
                                  2    2
(%o5)           --------------------------------
                           sqrt(%pi)


(%i6) erfc(z);
                                                     2
                                      3    2      - z
               2 hypergeometric([1], [-], z ) z %e
                                      2
(%o6)      1 - ---------------------------------------
                              sqrt(%pi)


(%i7) erf_generalized(z1,z2);
                                               2
                             3     2       - z2
      2 hypergeometric([1], [-], z2 ) z2 %e
                             2
(%o7) ------------------------------------------
                      sqrt(%pi)
                                                                2
                                              3     2       - z1
                       2 hypergeometric([1], [-], z1 ) z1 %e
                                              2
                     - ------------------------------------------
                                       sqrt(%pi)
```

See also: `fresnel_s`, `fresnel_c`.

### Function: implicit_derivative (f, indvarlist, orderlist, depvar)

This subroutine computes implicit derivatives of multivariable functions.
*f* is an array function, the indexes are the derivative degree in the *indvarlist* order;
*indvarlist* is the independent variable list; *orderlist* is the order desired; and 
*depvar* is the dependent variable.


To use this function write first `load("impdiff")`.

### Function: irr (val, IO)

IRR (Internal Rate of Return) is the value of rate which makes Net Present Value
zero.
*flowValues* is a list of varying cash flows,
*I0* is the initial investment.


Example:



```maxima
(%i1) load("finance")$
(%i2) res:irr([-5000,0,800,1300,1500,2000],0)$
(%i3) rhs(res[1][1]);
(%o3)                .03009250374237132
```

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

### Function: JF (lambda, n)

Returns the Jordan cell of order *n* with eigenvalue *lambda*.


Example:


```maxima
(%i1) load("diag")$

(%i2) JF(2,5);
                    [ 2  1  0  0  0 ]
                    [               ]
                    [ 0  2  1  0  0 ]
                    [               ]
(%o2)               [ 0  0  2  1  0 ]
                    [               ]
                    [ 0  0  0  2  1 ]
                    [               ]
                    [ 0  0  0  0  2 ]
(%i3) JF(3,2);
                         [ 3  1 ]
(%o3)                    [      ]
                         [ 0  3 ]
```


To use this function write first `load("diag")`.

### Function: jordan (mat)

Returns the Jordan form of matrix *mat*, encoded as a list in a
particular format. To get the corresponding matrix, call the function
`dispJordan` using the output of `jordan` as the argument.


The elements of the returned list are themselves lists. The first
element of each is an eigenvalue of *mat*. The remaining elements
are positive integers which are the lengths of the Jordan blocks for
this eigenvalue. These integers are listed in decreasing
order. Eigenvalues are not repeated.


The functions `dispJordan`, `minimalPoly` and
`ModeMatrix` expect the output of a call to `jordan` as an
argument. If you construct this argument by hand, rather than by
calling `jordan`, you must ensure that each eigenvalue only
appears once and that the block sizes are listed in decreasing order,
otherwise the functions might give incorrect answers.


Example:















```maxima
(%i1) load("diag")$

(%i2) A: matrix([2,0,0,0,0,0,0,0],
                [1,2,0,0,0,0,0,0],
                [-4,1,2,0,0,0,0,0],
                [2,0,0,2,0,0,0,0],
                [-7,2,0,0,2,0,0,0],
                [9,0,-2,0,1,2,0,0],
                [-34,7,1,-2,-1,1,2,0],
                [145,-17,-16,3,9,-2,0,3])$


(%i3) jordan (A);
(%o3)                [[2, 3, 3, 1], [3, 1]]

(%i4) dispJordan (%);
                   [ 2  1  0  0  0  0  0  0 ]
                   [                        ]
                   [ 0  2  1  0  0  0  0  0 ]
                   [                        ]
                   [ 0  0  2  0  0  0  0  0 ]
                   [                        ]
                   [ 0  0  0  2  1  0  0  0 ]
(%o4)              [                        ]
                   [ 0  0  0  0  2  1  0  0 ]
                   [                        ]
                   [ 0  0  0  0  0  2  0  0 ]
                   [                        ]
                   [ 0  0  0  0  0  0  2  0 ]
                   [                        ]
                   [ 0  0  0  0  0  0  0  3 ]
```


To use this function write first `load("diag")`. See also `dispJordan` and `minimalPoly`.

See also: `dispJordan`, `minimalPoly`.

### Variable: julia_parameter

Default value: `%i`


Complex parameter for Julia fractals.
Its default value is `%i`; we  suggest the  values `-.745+%i*.113002`, 
`-.39054-%i*.58679`, `-.15652+%i*1.03225`, `-.194+%i*.6557` and 
`.011031-%i*.67037`.

See also: `%i`.

### Function: julia_set (x, y)

Julia sets.


This program is time consuming because it must make a lot of operations; 
the computing time is also related with the number of grid points.


Example:



```maxima
(%i1) load("fractals")$
(%i2) plot3d (julia_set, [x, -2, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


See also `julia_parameter`.

See also: `julia_parameter`.

### Function: julia_sin (x, y)

While function `julia_set` implements the transformation `julia_parameter+z^2`,
function `julia_sin` implements `julia_parameter*sin(z)`. See source code
for more details.


This program runs slowly  because it calculates a lot of sines.


Example:


This program is time consuming because it must make a lot of operations; 
the computing time is also related with the number of grid points.



```maxima
(%i1) load("fractals")$
(%i2) julia_parameter:1+.1*%i$
(%i3) plot3d (julia_sin, [x, -2, 2], [y, -3, 3], 
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


See also `julia_parameter`.

See also: `julia_parameter`.

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

### Function: li (s, z)

Represents the polylogarithm function of order *s* and argument *z*,
defined by the infinite series



$${\rm Li}_s \left(z\right) = \sum_{k=1}^\infty {z^k \over k^s}$$


$${\rm Li}_s \left(z\right) = \sum_{k=1}^\infty {z^k \over k^s}$$




`li[1](z)` is
$-\log(1 - z).$
`li[2]` and `li[3]` are the
dilogarithm and trilogarithm functions, respectively.


When the order is 1, the polylogarithm simplifies to `- log (1 - z)`, which
in turn simplifies to a numerical value if *z* is a real or complex floating
point number or the `numer` evaluation flag is present.


When the order is 2 or 3,
the polylogarithm simplifies to a numerical value
if *z* is a real floating point number
or the `numer` evaluation flag is present.


Examples:


















RETRIEVE: End of file encountered.
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) assume (x > 0);
(%o1)                        [x > 0]


(%i2) integrate ((log (1 - t)) / t, t, 0, x);
Is x - 1 positive, negative or zero?



Is x - 1 positive, negative or zero?
li[4](1);


Is x - 1 positive, negative or zero?
li[5](1);


Is x - 1 positive, negative or zero?
li[2](1/2);


Is x - 1 positive, negative or zero?
li[2](%i);


Is x - 1 positive, negative or zero?
li[2](1+%i);


Is x - 1 positive, negative or zero?
li [2] (7);


Is x - 1 positive, negative or zero?
li [2] (7), numer;


Is x - 1 positive, negative or zero?
li [3] (7);


Is x - 1 positive, negative or zero?
li [2] (7), numer;


Is x - 1 positive, negative or zero?
L : makelist (i / 4.0, i, 0, 8);


Is x - 1 positive, negative or zero?
map (lambda ([x], li [2] (x)), L);


Is x - 1 positive, negative or zero?
map (lambda ([x], li [3] (x)), L);
```

### Function: Lindstedt (eq, pvar, torder, ic)

This is a first pass at a Lindstedt code.  It can solve problems
with initial conditions entered, which can be arbitrary constants,
(just not *%k1* and *%k2*) where the initial conditions on the perturbation
equations are $z[i]=0, z'[i]=0$ for $i>0$. *ic* is the list of 
initial conditions.


Problems occur when initial conditions are not given, as the constants
in the perturbation equations are the same as the zero order equation
solution.  Also, problems occur when the initial conditions for the
perturbation equations are not $z[i]=0, z'[i]=0$ for $i>0$, such as the
Van der Pol equation.


Example:


```maxima
(%i1) load("makeOrders")$

(%i2) load("lindstedt")$

(%i3) Lindstedt('diff(x,t,2)+x-(e*x^3)/6,e,2,[1,0]);
          2
         e  (cos(5 T) - 24 cos(3 T) + 23 cos(T))
(%o3) [[[---------------------------------------
                          36864
   e (cos(3 T) - cos(T))
 - --------------------- + cos(T)],
            192
          2
       7 e    e
T = (- ---- - -- + 1) t]]
       3072   16
```


To use this function write first `load("makeOrders")` and `load("lindstedt")`.

### Variable: linear_solver

Default value: `linsolve`


`linear_solver` names the solver which is used to solve the system
of equations in Zeilberger’s algorithm.

### Variable: linewidth

Default value: `1`


The width of the lines, when option `object_005fwireframe` is
used. *value* must be a positive number.

See also: `object_wireframe`.

### Function: linsert (e, lst, p)

Inserts the expression or list *e* into the list *lst* at position
*p*. The list can be empty and *p* must be an integer between 1 and
the length of *lst* plus 1.

### Function: log (x)

Represents the natural (base $e$) logarithm of *x*.


Maxima does not have a built-in function for the base 10 logarithm or other 
bases. `log10(x) := log(x) / log(10)` is a useful definition.


Simplification and evaluation of logarithms is governed by several global flags:



**`logexpand`** — causes `log(a^b)` to become `b*log(a)`. If it is 
set to `all`, `log(a*b)` will also simplify to `log(a)+log(b)`.
If it is set to `super`, then `log(a/b)` will also simplify to 
`log(a)-log(b)` for rational numbers `a/b`, `a#1`. 
(`log(1/b)`, for `b` integer, always simplifies.) If it is set to 
`false`, all of these simplifications will be turned off.
**`logsimp`** — if `false` then no simplification of `%e` to a power containing 
`log`’s is done.
**`lognegint`** — if `true` implements the rule `log(-n) -> log(n)+%i*%pi` for
`n` a positive integer.
**`%e_to_numlog`** — when `true`, `r` some rational number, and `x` some expression,
the expression `%e^(r*log(x))` will be simplified into `x^r`.  It
should be noted that the `radcan` command also does this transformation,
and more complicated transformations of this as well. The `logcontract` 
command "contracts" expressions containing `log`.

### Variable: logabs

Default value: `false`


When doing indefinite integration where logs are generated, e.g.
`integrate(1/x,x)`, the answer is given in terms of `log(abs(...))`
if `logabs` is `true`, but in terms of `log(...)` if
`logabs` is `false`.  For definite integration, the `logabs:true`
setting is used, because here "evaluation" of the indefinite integral at the
endpoints is often needed.

### Function: logarc (expr)

The function `logarc(expr)` carries out the replacement of
inverse circular and hyperbolic functions with equivalent logarithmic
functions for an expression *expr* without setting the global
variable `logarc`.

### Variable: logconcoeffp

Default value: `false`


Controls which coefficients are
contracted when using `logcontract`.  It may be set to the name of a
predicate function of one argument.  E.g. if you like to generate
SQRTs, you can do `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$` .  Then
`logcontract(1/2*log(x));` will give `log(sqrt(x))`.

### Function: logcontract (expr)

Recursively scans the expression *expr*, transforming
subexpressions of the form `a1*log(b1) + a2*log(b2) + c` into
`log(ratsimp(b1^a1 * b2^a2)) + c`







```maxima
maxima
(%i1) 2*(a*log(x) + 2*a*log(y))$

(%i2) logcontract(%);
                                 2  4
(%o2)                     a log(x  y )
```


The declaration `declare(n,integer)` causes
`logcontract(2*a*n*log(x))` to simplify to `a*log(x^(2*n))`.  The
coefficients that "contract" in this manner are those such as the 2 and the
`n` here which satisfy `featurep(coeff,integer)`.  The user can
control which coefficients are contracted by setting the option
`logconcoeffp` to the name of a predicate function of one argument.
E.g. if you like to generate SQRTs, you can do `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$` .  Then
`logcontract(1/2*log(x));` will give `log(sqrt(x))`.

### Variable: logexpand

Default value: `true`


If `true`, that is the default value, causes `log(a^b)` to become
`b*log(a)`.  If it is set to `all`, `log(a*b)` will also simplify
to `log(a)+log(b)`.  If it is set to `super`, then `log(a/b)`
will also simplify to `log(a)-log(b)` for rational numbers `a/b`,
`a#1`.  (`log(1/b)`, for integer `b`, always simplifies.) If it
is set to `false`, all of these simplifications will be turned off.


When `logexpand` is set to `all` or `super`,
the logarithm of a product expression simplifies to a summation of logarithms.


Examples:


When `logexpand` is `true`,
`log(a^b)` simplifies to `b*log(a)`.






```maxima
maxima

(%i1) log(n^2), logexpand=true;
(%o1)                       2 log(n)
```


When `logexpand` is `all`,
`log(a*b)` simplifies to `log(a)+log(b)`.






```maxima
maxima

(%i1) log(10*x), logexpand=all;
(%o1)                   log(x) + log(10)
```


When `logexpand` is `super`,
`log(a/b)` simplifies to `log(a)-log(b)`
for rational numbers `a/b` with `a#1`.






```maxima
maxima

(%i1) log(a/(n + 1)), logexpand=super;
(%o1)                  log(a) - log(n + 1)
```


When `logexpand` is set to `all` or `super`,
the logarithm of a product expression simplifies to a summation of logarithms.








```maxima
maxima

(%i1) my_product : product (X(i), i, 1, n);
                             n
                           _____
                           |   |
(%o1)                      |   | X(i)
                           |   |
                           i = 1


(%i2) log(my_product), logexpand=all;
                          n
                         ____
                         \
(%o2)                     >    log(X(i))
                         /
                         ----
                         i = 1


(%i3) log(my_product), logexpand=super;
                          n
                         ____
                         \
(%o3)                     >    log(X(i))
                         /
                         ----
                         i = 1
```


When `logexpand` is `false`,
these simplifications are disabled.










```maxima
maxima
(%i1) logexpand : false $

(%i2) log(n^2);
                                  2
(%o2)                        log(n )


(%i3) log(10*x);
(%o3)                       log(10 x)


(%i4) log(a/(n + 1));
                                 a
(%o4)                      log(-----)
                               n + 1


(%i5) log ('product (X(i), i, 1, n));
                               n
                             _____
                             |   |
(%o5)                    log(|   | X(i))
                             |   |
                             i = 1
```

### Variable: lognegint

Default value: `false`


If `true` implements the rule
`log(-n) -> log(n)+%i*%pi` for `n` a positive integer.

### Variable: logsimp

Default value: `true`


If `false` then no simplification of `%e` to a
power containing `log`’s is done.

### Function: lowercasep (char)

Returns `true` if *char* is a lowercase character. 


Note: See remarks on `alphacharp`.

See also: `alphacharp`.

### Function: lreplace (e, lst, p)

If *e* is a list of length *n*, the elements in the positions
*p*, *p*+1, ..., *p*+*n*-1 of the list *lst* are
replaced by *e*, or the first elements of *e* if the end of
*lst* is reached.  If *e* is an expression, the element in
position *p* of list *lst* is replaced by that expression.
*p* must be an integer between 1 and the length of *lst*.

### Function: makeOrders (indvarlist, orderlist)

Returns a list of all powers for a polynomial up to and including the arguments. 



```maxima
(%i1) load("makeOrders")$

(%i2) makeOrders([a,b],[2,3]);
(%o2) [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1],
            [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]
(%i3) expand((1+a+a^2)*(1+b+b^2+b^3));
       2  3      3    3    2  2      2    2    2
(%o3) a  b  + a b  + b  + a  b  + a b  + b  + a  b + a b
                                                  2
                                           + b + a  + a + 1
```

where `[0, 1]` is associated with the term $b$ and `[2, 3]` with $a^2 b^3$.


To use this function write first `load("makeOrders")`.

### Function: mandelbrot_set (x, y)

Mandelbrot set.


Example:


This program is time consuming because it must make a lot of operations; 
the computing time is also related with the number of grid points.



```maxima
(%i1) load("fractals")$
(%i2) plot3d (mandelbrot_set, [x, -2.5, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```

### Function: mat_function (f, A)

Returns $f(A)$, where *f* is an analytic function and *A*
a matrix. This computation is based on the Taylor expansion of
*f*. It is not efficient for numerical evaluation, but can give
symbolic answers for small matrices.





Example 1:


The exponential of a matrix. We only give the first row of the answer,
since the output is rather large.







```maxima
(%i1) load("diag")$
(%i2) A: matrix ([0,1,0], [0,0,1], [-1,-3,-3])$

(%i3) ratsimp (mat_function (exp, t*A)[1]);
           2              - t                   2   - t
         (t  + 2 t + 2) %e       2        - t  t  %e
(%o3)   [--------------------, (t  + t) %e   , --------]
                  2                               2
```


Example 2:


Comparison with the Taylor series for the exponential and also
comparing `exp(%i*A)` with sine and cosine.














```maxima
(%i1) load("diag")$

(%i2) A: matrix ([0,1,1,1],
                 [0,0,0,1],
                 [0,0,0,1],
                 [0,0,0,0])$


(%i3) ratsimp (mat_function (exp, t*A));
                       [           2     ]
                       [ 1  t  t  t  + t ]
                       [                 ]
(%o3)                  [ 0  1  0    t    ]
                       [                 ]
                       [ 0  0  1    t    ]
                       [                 ]
                       [ 0  0  0    1    ]


(%i4) minimalPoly (jordan (A));
                                3
(%o4)                          x


(%i5) ratsimp (ident(4) + t*A + 1/2*(t^2)*A^^2);
                       [           2     ]
                       [ 1  t  t  t  + t ]
                       [                 ]
(%o5)                  [ 0  1  0    t    ]
                       [                 ]
                       [ 0  0  1    t    ]
                       [                 ]
                       [ 0  0  0    1    ]


(%i6) ratsimp (mat_function (exp, %i*t*A));
                  [                        2 ]
                  [ 1  %i t  %i t  %i t - t  ]
                  [                          ]
(%o6)             [ 0   1     0      %i t    ]
                  [                          ]
                  [ 0   0     1      %i t    ]
                  [                          ]
                  [ 0   0     0        1     ]


(%i7) ratsimp (mat_function (cos, t*A) + %i*mat_function (sin, t*A));
                  [                        2 ]
                  [ 1  %i t  %i t  %i t - t  ]
                  [                          ]
(%o7)             [ 0   1     0      %i t    ]
                  [                          ]
                  [ 0   0     1      %i t    ]
                  [                          ]
                  [ 0   0     0        1     ]
```


Example 3:


Power operations.









```maxima
(%i1) load("diag")$
(%i2) A: matrix([1,2,0], [0,1,0], [1,0,1])$
(%i3) integer_pow(x) := block ([k], declare (k, integer), x^k)$

(%i4) mat_function (integer_pow, A);
                       [ 1     2 k     0 ]
                       [                 ]
(%o4)                  [ 0      1      0 ]
                       [                 ]
                       [ k  (k - 1) k  1 ]


(%i5) A^^20;
                         [ 1   40   0 ]
                         [            ]
(%o5)                    [ 0    1   0 ]
                         [            ]
                         [ 20  380  1 ]
```


To use this function write first `load("diag")`.

### Variable: MAX_ORD

Default value: 5


`MAX_ORD` is the maximum recurrence order attempted by `Zeilberger`.

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

### Function: minimalPoly (l)

Returns the minimal polynomial of the matrix whose Jordan form is
described by the list *l*. This list should be in the format given
by the `jordan` function. See `jordan` for details of this
format.


Example:


```maxima
(%i1) load("diag")$

(%i2) a:matrix([2,1,2,0],
               [-2,2,1,2],
               [-2,-1,-1,1],
               [3,1,2,-1])$

(%i3) jordan(a);
(%o3)               [[- 1, 1], [1, 3]]
(%i4) minimalPoly(%);
                            3
(%o4)                (x - 1)  (x + 1)
```


To use this function write first `load("diag")`. See also `jordan` and `dispJordan`.

See also: `jordan`, `dispJordan`.

### Function: mkdir (dir)

Create directory *dir*

### Variable: mod_big_prime

Default value: `big_primes[1]`


`mod_big_prime` is the modulus used by the modular test in `parGosper`.

### Variable: mod_test

Default value: `false`


When `mod_test` is `true`,
`parGosper` executes a
modular test for discarding systems with no solutions.

### Variable: mod_threshold

Default value: 4


`mod_threshold` is the
greatest order for which the modular test in `parGosper` is attempted.

### Function: ModeMatrix (A, jordan_info)

Returns an invertible matrix *M* such that $(M^^-1).A.M$ is
the Jordan form of *A*.


To calculate this, Maxima must find the Jordan form of *A*, which
might be quite computationally expensive. If that has already been
calculated by a previous call to `jordan`, pass it as a second
argument, *jordan_info*. See `jordan` for details of the
required format.


Example:








```maxima
(%i1) load("diag")$
(%i2) A: matrix([2,1,2,0], [-2,2,1,2], [-2,-1,-1,1], [3,1,2,-1])$
(%i3) M: ModeMatrix (A);
                      [  1    - 1   1   1 ]
                      [                   ]
                      [   1               ]
                      [ - -   - 1   0   0 ]
                      [   9               ]
                      [                   ]
(%o3)                 [   13              ]
                      [ - --   1   - 1  0 ]
                      [   9               ]
                      [                   ]
                      [  17               ]
                      [  --   - 1   1   1 ]
                      [  9                ]

(%i4) is ((M^^-1) . A . M = dispJordan (jordan (A)));
(%o4)                         true
```


Note that, in this example, the Jordan form of `A` is computed
twice. To avoid this, we could have stored the output of
`jordan(A)` in a variable and passed that to both
`ModeMatrix` and `dispJordan`.


To use this function write first `load("diag")`. See also
`jordan` and `dispJordan`.

See also: `jordan`, `dispJordan`.

### Variable: modular_linear_solver

Default value: `linsolve`


`modular_linear_solver` names the linear solver used by the modular test in `parGosper`.

### Function: multibernstein_poly ([k1,k2,..., kp], [n1,n2,..., np], [x1,x2,..., xp])

The multibernstein polynomial `multibernstein_poly ([k1, k2, ..., kp], [n1, n2, ..., np], [x1, x2, ..., xp])` is the product of
bernstein polynomials `bernstein_poly(k1, n1, x1) bernstein_poly(k2, n2, x2) ... bernstein_poly(kp, np, xp)`.


To use `multibernstein_poly`, first `load("bernstein")`.

### Function: newcontext (newcontext, name, newcontext)

Creates a new, empty context, called *name*, which
has `global` as its only subcontext.  The newly-created context
becomes the currently active context.


If *name* is not specified, a new name is created (via `gensym`) and returned.


`newcontext` evaluates its argument.
`newcontext` returns *name* (if specified) or the new context name.

### Variable: nextlayerfactor

Default value: `false`


When `nextlayerfactor` is `true`, recursive calls  of `facsum`
are applied  to  the  factors  of  the  factored  form   of  the
coefficients of the arguments.


When  `false`, `facsum` is applied to
each coefficient as a whole whenever recursive calls to  `facsum` occur.


Inclusion   of   the  atom
`nextlayerfactor` in  the argument  list of `facsum`  has the  effect of
`nextlayerfactor: true`, but for the next level of the expression *only*.
Since `nextlayerfactor` is  always bound to  either `true` or  `false`, it
must be presented single-quoted whenever it appears in the argument list of `facsum`.

### Function: nonzeroandfreeof (x, expr)

Returns `true` if *expr* is nonzero and `freeof (x, expr)` returns `true`.
Returns `false` otherwise.


To use this function write first `load("functs")`.

### Function: normalize (q)

Returns the normalized version of a quantum state given as a list *q*.

### Function: npv (rate, val)

Calculates the present value of a value series to evaluate the viability in a
project.
*val* is a list of varying cash flows.


Example:



```maxima
(%i1) load("finance")$
(%i2) npv(0.25,[100,500,323,124,300]);
(%o2)                714.4703999999999
```

### Variable: opacity

Default value: `1`


*value* must be a number between 0 and 1. The lower the number, the
more transparent the object will become. The default value of 1 means a
completely opaque object.

### Variable: orientation

Default value: `[0, 0, 0]`


Three angles by which the object will be rotated with respect to the
three axis. *angles* can be a list with 3 real numbers, or 3 real
numbers separated by commas. **Example**: `[0, 0, 90]` rotates
the x axis of the object to the y axis of the reference frame.

### Variable: origin

Default value: `[0, 0, 0]`


The coordinates of the object’s origin, with respect to which its
other dimensions are defined. *point* can be a list with 3
real numbers, or 3 real numbers separated by commas.

### Variable: packagefile

Default value: `false`


Package designers who use `save` or `translate` to create packages
(files) for others to use may want to set `packagefile: true` to prevent
information from being added to Maxima’s information-lists (e.g.
`values`, `functions`) except where necessary when the file is
loaded in.  In this way, the contents of the package will not get in the user’s
way when he adds his own data.  Note that this will not solve the problem of
possible name conflicts.  Also note that the flag simply affects what is output
to the package file.  Setting the flag to `true` is also useful for
creating Maxima init files.

See also: `save`, `translate`, `values`, `functions`.

### Function: parabolic_cylinder_d (v, z)

The parabolic cylinder function `parabolic_005fcylinder_005fd`. ([https://personal.math.ubc.ca/~cbm/aands/page_687.htmA&S eqn 19.3.1]()).



The solution of the Weber differential equation

$$y''(z) + \left(\nu + {1\over 2} - {1\over 4} z^2\right) y(z) = 0$$


$$y''(z) + \left(\nu + {1\over 2} - {1\over 4} z^2\right) y(z) = 0$$



has two independent solutions, one of which is 
$D_{\nu}(z),$
the parabolic cylinder d function.


Function `specint` can return expressions containing
`parabolic_005fcylinder_005fd` if the option variable
`prefer_d` is `true`.

See also: `parabolic_cylinder_d`, `specint`, `prefer_d`, `true`.

### Function: permutation (n, r)

Returns the number of permutations of *r* objects
selected from a set of *n* objects.


To use this function write first `load("functs")`.

### Variable: phiresolution

Default value: ``


The number of sub-intervals into which the phi angle interval from
`object_005fstartphi` to `object_005fendphi`
will be divided. *num* must be a positive integer.


See also `object_005fstartphi` and
`object_005fendphi`.

See also: `object_startphi`, `object_endphi`.

### Function: plog (x)

Represents the principal branch of the complex-valued natural
logarithm with `-%pi < carg(x) <= +%pi` .

### Variable: pointsize

Default value: `1`


The size of the points, when option `object_005fpoints` is
used. *value* must be a positive number.

See also: `object_points`.

### Variable: position

Default value: `[0, 0, 0]`


The coordinates of the object’s position. *point* can be a list with 3
real numbers, or 3 real numbers separated by commas.

### Function: pv (rate, FV, num)

We can calculate the present value of a Future one given a certain interest rate.
*rate* is the interest rate, *FV* is the future value and *num* is
the number of periods.


Example:



```maxima
(%i1) load("finance")$
(%i2) pv(0.12,1000,3);
(%o2)                711.7802478134108
```

### Function: pytranslate (expr, print-ir)

Translates the expression *expr* to equivalent python3 statements. Output is printed in the stdout.


Example:






```maxima
(%i1) load ("pytranslate")$

(%i2) pytranslate('(for i:8 step -1 unless i<3 do (print(i))));
(%o2) 
v["i"] = 8
while not((v["i"] < 3)):
    m["print"](v["i"])
    v["i"] = (v["i"] + -1)
del v["i"]
```


*expr* is evaluated, and the return value is used for translation. Hence, for statements like assignment, it might be useful to quote the statement:







```maxima
(%i1) load ("pytranslate")$

(%i2) pytranslate(x:20);
(%o2) 
20


(%i3) pytranslate('(x:20));
(%o3) 
v["x"] = 20
```


Passing the optional parameter (*print-ir*) to `pytranslate` as t, will print the internal IR representation of `expr` and return the translated python3 code.








```maxima
(%i1) load("pytranslate");
(%o1) pytranslate


(%i2) pytranslate('(plot3d(lambda([x, y], x^2+y^(-1)), [x, 1, 10],
                   [y, 1, 10])), t);
(body
 (funcall (element-array "m" (string "plot3d"))
          (lambda
              ((symbol "x") (symbol "y")
               (op-no-bracket
                =
                (symbol "v")
                (funcall (symbol "stack") (dictionary) (symbol "v"))))
            (op +
                (funcall (element-array (symbol "m") (string "pow"))
                         (symbol "x") (num 2 0))
                (funcall (element-array (symbol "m") (string "pow"))
                         (symbol "y") (unary-op - (num 1 0)))))
          (struct-list (string "x") (num 1 0) (num 10 0))
          (struct-list (string "y") (num 1 0) (num 10 0))))
(%o2) 
m["plot3d"](lambda x, y, v = Stack({}, v): (m["pow"](x, 2) + m["\
pow"](y, (-1))), ["x", 1, 10], ["y", 1, 10])
```

### Function: qdisplay (q)

Represents the state *q* of a system of *n* qubits as a linear
combination of the computational states with *n* binary digits.  It
returns an expression including strings and symbols.

### Variable: qmatrix

This variable is a predefined hash array of two by two matrices with the
standard matrices: identity, Pauli matrices, Hadamard matrix and the
phase matrix. The six possible indices are I, X, Y, Z, H,
S. *qmatrix*[I] is the identity matrix, *qmatrix*[X] the Pauli x
matrix, *qmatrix*[Y] the Pauli y matrix, *qmatrix*[Z] the Pauli
z matrix, *qmatrix*[H] the Hadamard matrix and *qmatrix*[S] the
phase matrix.

### Function: qmeasure (qmeasure, q, qmeasure, q, i1, ..., im)

Measures the value of one or more qubits in a system of *n* qubits
with state *q*. The *m* positive integers *i1*, ...,
*im* are the positions of the qubits to be measured It requires 1 or
more arguments. The first argument must be the state q. If the only
argument given is *q*, all the n qubits will be measured.


It returns a list with the values of the qubits measured (either 0 or
1), in the same order they were requested or in ascending order if the
only argument given was *q*. It modifies the list *q*,
reflecting the collapse of the quantum state after the measurement.

### Function: qswap (q, i, j)

Interchanges the states of qubits *i* and *j* in the state
*q* of a system of several qubits.  It modifies the list *q* and
returns its modified value.

### Function: qubits (qubits, n, qubits, i1, ..., in)

`qubits`(*n*) returns a list representing the ground state of a
system of *n* qubits.


`qubits`(*i1*, ..., *in*) returns a list with
representing the state of *n* qubits with values *i1*, ...,
*in*.

### Function: racah_v (a, b, c, a1, b1, c1)

Compute Racah’s V coefficient (computed in terms of a related
Clebsch-Gordan coefficient).

### Function: racah_w (j1, j2, j5, j4, j3, j6)

Compute Racah’s W coefficient (computed in terms of a Wigner 6j symbol)

### Variable: radius

Default value: `0.5`


The radius or a sphere or the distance from the axis to the base’s
vertices in a cylinder or a cone. *value* must be a positive number.

### Function: reduce_consts (expr)

Replaces constant subexpressions of *expr* with
constructed constant atoms, saving the definition of all these
constructed constants in the list of equations `const_eqns`, and
returning the modified *expr*.  Those parts of *expr* are constant which
return `true` when operated on by the function `constantp`.  Hence,
before invoking `reduce_consts`, one should do



```maxima
declare ([objects to be given the constant property], constant)$
```


to set up a database of the constant quantities occurring in your
expressions.


If you are planning to generate Fortran output after these symbolic
calculations, one of the first code sections should be the calculation
of all constants.  To generate this code segment, do



```maxima
map ('fortran, const_eqns)$
```


Variables besides `const_eqns` which affect `reduce_consts` are:


`const_prefix` (default value: `xx`) is the string of characters used to prefix all
symbols generated by `reduce_consts` to represent constant subexpressions.


`const_counter` (default value: 1) is the integer index used to generate unique
symbols to represent each constant subexpression found by `reduce_consts`.


`load ("rducon")` loads this function.
`demo ("rducon")` shows a demonstration of this function.

### Function: rempart (expr, n)

Removes part *n* from the expression *expr*.


If *n* is a list of the form `[l, m]`
then parts *l* thru *m* are removed.


To use this function write first `load("functs")`.

### Function: remvalue (remvalue, name_1, ..., name_n, remvalue, all)

Removes the values of user variables *name_1*, ..., *name_n*
(which can be subscripted) from the system.


`remvalue (all)` removes the values of all variables in `values`,
the list of all variables given names by the user
(as opposed to those which are automatically assigned by Maxima).


See also `values`.

See also: `values`.

### Variable: resolution

Default value: `6`


*number* must be an integer greater than 2 that sets the number of
edges in the base of a cone or a cylinder.

### Variable: restart

Default value: `false`


A true value means that animations will restart automatically when the
end of the list is reached. Writing just “restart” is equivalent to
[restart, *true*].

### Function: rmdir (dir)

remove directory *dir*

### Function: rncombine (expr)

Transforms *expr* by combining all terms of *expr* that have
identical denominators or denominators that differ from each other by
numerical factors only.  This is slightly different from the behavior
of `combine`, which collects terms that have identical denominators.


Setting `pfeformat: true` and using `combine` yields results similar
to those that can be obtained with `rncombine`, but `rncombine` takes
the additional step of cross-multiplying numerical denominator factors.
This results in neater forms, and the possibility of recognizing some
cancellations.


`load("rncomb")` loads this function.

See also: `combine`.

### Function: run_testsuite (options)

Run the Maxima test suite.  Tests producing the desired answer are
considered “passes,” as are tests that do not produce the desired
answer, but are marked as known bugs.


`run_testsuite` takes the following optional keyword arguments



**display_all** — Display all tests.  Normally, the tests are not displayed, unless the test
fails.  (Defaults to `false`).
**display_known_bugs** — Displays tests that are marked as known bugs.  (Default is `false`).
**tests** — This is a single test or a list of tests that should be run.  Each test can be specified by
either a string or a symbol.  By default, all tests are run.  The complete set
of tests is specified by `testsuite_005ffiles`.
**time** — Display time information.  If `true`, the time taken for each
test file is displayed.  If `all`, the time for each individual
test is shown if `display_all` is `true`.  The default is
`false`, so no timing information is shown.
**share_tests** — Load additional tests for the `share` directory.  If `true`,
these additional tests are run as a part of the testsuite.  If
`false`, no tests from the `share` directory are run.  If
`only`, only the tests from the `share` directory are run.
Of course, the actual set of test that are run can be controlled by
the `tests` option. The default is `false`.
**answers_from_file** — Read answers to interactive questions from the source file. May only be
`false` or `true` (default). See also
`batch_005fanswers_005ffrom_005ffile`.


For example `run_testsuite(display_known_bugs = true, tests=[rtest5])`
runs just test `rtest5` and displays the test that are marked as
known bugs.


`run_testsuite(display_all = true, tests=["rtest1", rtest1a])` will
run tests `rtest1` and `rtest2`, and displays each test.


`run_testsuite` changes the Maxima environment.
Typically a test script executes `kill` to establish a known environment
(namely one without user-defined functions and variables)
and then defines functions and variables appropriate to the test.


`run_testsuite` returns `done`.

See also: `testsuite_files`, `batch_answers_from_file`, `kill`.

### Function: Rx (a)

Returns the 2 by two matrix (acting on one qubit) corresponding to a
rotation of with an angle of *a* radians around the x axis.

### Function: Ry (a)

Returns the 2 by two matrix (acting on one qubit) corresponding to a
rotation of with an angle of *a* radians around the y axis.

### Function: Rz (a)

Returns the 2 by two matrix (acting on one qubit) corresponding to a
rotation of with an angle of *a* radians around the z axis.

### Function: saving (rate, amount, num)

The table that represents the values in a constant and periodic
saving can be found by `saving`.
*amount* represents the desired quantity and num the number
of periods to save.


Example:



```maxima
(%i1) load("finance")$
(%i2) saving(0.15,12000,15)$
      "n"    "Balance"     "Interest"   "Payment"      
     0.000         0.000         0.000         0.000  
     1.000       252.205         0.000       252.205  
     2.000       542.240        37.831       252.205  
     3.000       875.781        81.336       252.205  
     4.000      1259.352       131.367       252.205  
     5.000      1700.460       188.903       252.205  
     6.000      2207.733       255.069       252.205  
     7.000      2791.098       331.160       252.205  
     8.000      3461.967       418.665       252.205  
     9.000      4233.467       519.295       252.205  
    10.000      5120.692       635.020       252.205  
    11.000      6141.000       768.104       252.205  
    12.000      7314.355       921.150       252.205  
    13.000      8663.713      1097.153       252.205  
    14.000     10215.474      1299.557       252.205  
    15.000     12000.000      1532.321       252.205
```

### Variable: scale

Default value: `[1, 1, 1]`


Three numbers by which the object will be scaled with respect to the
three axis. *factors* can be a list with 3 real numbers, or 3 real
numbers separated by commas. **Example**: `[2, 0.5, 1]`
enlarges the object to twice its size in the x direction, reduces the
dimensions in the y direction to half and leaves the z dimensions
unchanged.

### Function: scene (objects, ..., options, ..., ;)

Accepts an empty list or a list of several `scene_005fobjects`
and `scene_005foptions`. The program launches Xmaxima, which
opens an external window representing the given objects in a
3-dimensional space and applying the options given. Each object must
belong to one of the following 4 classes: sphere, cube, cylinder or cone
(see `scene_005fobjects`). Objects are identified by
giving their name or by a list in which the first element is the class
name and the following elements are options for that object.

 

**Example**. A hexagonal pyramid with a blue background:





```maxima
(%i1) scene(cone, [background,"#9980e5"])$
```

(Figure scene1)


By holding down the left button of the mouse while it is moved on the
graphics window, the camera can be rotated showing different views of
the pyramid. The two plot options `scene_005felevation` and
`scene_005fazimuth` can also be used to change the initial
orientation of the viewing camera. The camera can be moved by holding
the middle mouse button while moving it and holding the right-side mouse
button while moving it up or down will zoom in or out.


Each object option should be a list starting with the option name,
followed by its value. The list of allowed options can be found in the
`object_005foptions` section.


**Example**. This will show a sphere falling to the ground and
bouncing off without losing any energy. To start or pause the
animation, press the play/pause button.













```maxima
(%i1) p: makelist ([0,0,2.1- 9.8*t^2/2], t, 0, 0.64, 0.01)$

(%i2) p: append (p, reverse(p))$

(%i3) ball: [sphere, [radius,0.1], [thetaresolution,20],
  [phiresolution,20], [position,0,0,2.1], [color,red],
  [animate,position,p]]$

(%i4) ground: [cube, [xlength,2], [ylength,2], [zlength,0.2],
  [position,0,0,-0.1],[color,violet]]$

(%i5) scene (ball, ground, restart)$
```

(Figure scene2)


The *restart* option was used to make the animation restart
automatically every time the last point in the position list is reached.
The accepted values for the colors are the same as for the `color`
option of plot2d.

See also: `scene_objects`, `scene_options`, `scene_elevation`, `scene_azimuth`, `object_options`, `color`.

### Function: setup_autoload (filename, function_1, ..., function_n)

Specifies that if any of *function_1*, ..., *function_n* are
referenced and not yet defined, *filename* is loaded via `load`.
*filename* usually contains definitions for the functions specified,
although that is not enforced.


`setup_autoload` does not work for `memoizing-functions`.


`setup_autoload` quotes its arguments.


Example:









```maxima
(%i1) legendre_p (1, %pi);
(%o1)                  legendre_p(1, %pi)
(%i2) setup_autoload ("specfun.mac", legendre_p, ultraspherical);
(%o2)                         done
(%i3) ultraspherical (2, 1/2, %pi);
Warning - you are redefining the Macsyma function ultraspherical
Warning - you are redefining the Macsyma function legendre_p
                            2
                 3 (%pi - 1)
(%o3)            ------------ + 3 (%pi - 1) + 1
                      2
(%i4) legendre_p (1, %pi);
(%o4)                          %pi
(%i5) legendre_q (1, %pi);
                              %pi + 1
                      %pi log(-------)
                              1 - %pi
(%o5)                 ---------------- - 1
                             2
```

See also: `memoizing-functions`.

### Variable: share_testsuite_files

`share_testsuite_files` is the set of tests from the `share`
directory that is run as a part of the test suite by
`run_005ftestsuite`..

See also: `run_testsuite`.

### Function: show_form (expr)

Displays the internal maxima form of `expr`


```maxima
(%i4) show_form(a^b);
((mexpt) $a $b) 
(%o4) a^b
```

### Function: sierpinskiale (n)

Sierpinski Triangle: 3 contractive maps; .5 contraction constant and translations;
all maps have the same contraction ratio. Argument *n* must be great enough, 10000 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,sierpinskiale(n)], [style,dots])$
```

### Function: sierpinskimap (nn)

Sierpinski map. Argument *nn* must be small (5, for example).
Maxima can crash if *nn* is 7 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,sierpinskimap(6)])$
```

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

### Variable: simplified_output

Default value: `false`


When `simplified_output` is `true`,
functions in the `zeilberger` package attempt
further simplification of the solution.

### Function: snowmap (ent, nn)

Koch snowflake sets. Function `snowmap` plots the snow Koch map 
over the vertex of an initial closed polygonal, in the complex plane. Here  
the orientation of the polygon is important. Argument *nn* is the number of 
recursive applications of Koch transformation; *nn* must be small (5 or 6).


Examples:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,
              snowmap([1,exp(%i*%pi*2/3),exp(-%i*%pi*2/3),1],4)])$
(%i3) plot2d([discrete,
              snowmap([1,exp(-%i*%pi*2/3),exp(%i*%pi*2/3),1],4)])$
(%i4) plot2d([discrete, snowmap([0,1,1+%i,%i,0],4)])$
(%i5) plot2d([discrete, snowmap([0,%i,1+%i,1,0],4)])$
```

### Variable: space

The space character.

### Variable: sphere

A sphere with default radius of 0.5 units and center at the origin.

### Function: sqrt (x)

The square root of *x*.  It is represented internally by
`x^(1/2)`.  See also `rootscontract` and `radexpand`.

See also: `rootscontract`, `radexpand`.

### Function: standardize (standardize, list, standardize, matrix)

Subtracts to each element of the list the sample mean and divides
the result by the standard deviation. When the input is a matrix,
`standardize` subtracts to each row the multivariate mean, and then
divides each component by the corresponding standard deviation.

### Variable: startphi

Default value: `0`


In a sphere phi is the angle on the vertical plane that passes through
the z axis, measured from the positive part of the z axis. *angle*
must be a number between 0 and 180 that sets the initial value of phi at
which the surface will start. A value bigger than 0 will eliminate a
part of the sphere’s surface.


See also `object_005fendphi` and
`object_005fphiresolution`.

See also: `object_endphi`, `object_phiresolution`.

### Variable: starttheta

Default value: `0`


In a sphere theta is the angle on the horizontal plane (longitude),
measured from the positive part of the x axis. *angle* must be a
number between 0 and 360 that sets the initial value of theta at which
the surface will start. A value bigger than 0 will eliminate a part of
the sphere’s surface.


See also `object_005fendtheta` and
`object_005fthetaresolution`.

See also: `object_endtheta`, `object_thetaresolution`.

### Function: stirling (stirling, z, n, stirling, z, n, pred)

Replace `gamma(x)` with the $O(1/x^{2n-1})$ Stirling formula. when *n* isn’t
a nonnegative integer, signal an error. With the optional third argument `pred`,
the Stirling formula is applied only when `pred` is true.


Reference: Abramowitz & Stegun, " Handbook of mathematical functions", 6.1.40.


Examples:


```maxima
(%i1) load ("stirling")$

(%i2) stirling(gamma(%alpha+x)/gamma(x),1);
       1/2 - x             x + %alpha - 1/2
(%o2) x        (x + %alpha)
                                   1           1
                            --------------- - ---- - %alpha
                            12 (x + %alpha)   12 x
                          %e
(%i3) taylor(%,x,inf,1);
                    %alpha       2    %alpha
          %alpha   x       %alpha  - x       %alpha
(%o3)/T/ x       + -------------------------------- + . . .
                                 2 x
(%i4) map('factor,%);
                                       %alpha - 1
         %alpha   (%alpha - 1) %alpha x
(%o4)   x       + -------------------------------
                                  2
```


The function `stirling` knows the difference between the variable ’gamma’ and
the function gamma:



```maxima
(%i5) stirling(gamma + gamma(x),0);
                                    x - 1/2   - x
(%o5)    gamma + sqrt(2) sqrt(%pi) x        %e
(%i6) stirling(gamma(y) + gamma(x),0);
                         y - 1/2   - y
(%o6) sqrt(2) sqrt(%pi) y        %e
                                              x - 1/2   - x
                         + sqrt(2) sqrt(%pi) x        %e
```


To apply the Stirling formula only to terms that involve the variable `k`,
use an optional third argument; for example


```maxima
(%i7) makegamma(pochhammer(a,k)/pochhammer(b,k));
(%o7) (gamma(b)*gamma(k+a))/(gamma(a)*gamma(k+b))
(%i8) stirling(%,1, lambda([s], not(freeof(k,s))));
(%o8) (%e^(b-a)*gamma(b)*(k+a)^(k+a-1/2)*(k+b)^(-k-b+1/2))/gamma(a)
```

The terms `gamma(a)` and `gamma(b)` are free of `k`, so the Stirling formula
was not applied to these two terms.


To use this function write first `load("stirling")`.

### Function: subsample (subsample, data_matrix, predicate_function, subsample, data_matrix, predicate_function, col_num1, col_num2, ...)

This is a sort of variant of the Maxima `submatrix` function.
The first argument is the data matrix, the second is a predicate function
and optional additional arguments are the numbers of the columns to be taken.


Examples:


These are multivariate records in which the wind speed
in the first meteorological station were greater than 18.
See that in the lambda expression the *i*-th component is
referred to as `v[i]`.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) subsample (s2, lambda([v], v[1] > 18));
              [ 19.38  15.37  15.12  23.09  25.25 ]
              [                                   ]
              [ 18.29  18.66  19.08  26.08  27.63 ]
(%o3)         [                                   ]
              [ 20.25  21.46  19.95  27.71  23.38 ]
              [                                   ]
              [ 18.79  18.96  14.46  26.38  21.84 ]
```


In the following example, we request only the first, second and fifth
components of those records with wind speeds greater or equal than 16
in station number 1 and less than 25 knots in station number 4. The sample
contains only data from stations 1, 2 and 5. In this case,
the predicate function is defined as an ordinary Maxima function.









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) g(x):= x[1] >= 16 and x[4] < 25$

(%i4) subsample (s2, g, 1, 2, 5);
                     [ 19.38  15.37  25.25 ]
                     [                     ]
                     [ 17.33  14.67  19.58 ]
(%o4)                [                     ]
                     [ 16.92  13.21  21.21 ]
                     [                     ]
                     [ 17.25  18.46  23.87 ]
```


Here is an example with the categorical variables of `biomed.data`.
We want the records corresponding to those patients in group `B`
who are older than 38 years.









```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) h(u):= u[1] = B and u[2] > 38 $

(%i4) subsample (s3, h);
                [ B  39  28.0  102.3  17.1  146 ]
                [                               ]
                [ B  39  21.0  92.4   10.3  197 ]
                [                               ]
                [ B  39  23.0  111.5  10.0  133 ]
                [                               ]
                [ B  39  26.0  92.6   12.3  196 ]
(%o4)           [                               ]
                [ B  39  25.0  98.7   10.0  174 ]
                [                               ]
                [ B  39  21.0  93.2   5.9   181 ]
                [                               ]
                [ B  39  18.0  95.0   11.3  66  ]
                [                               ]
                [ B  39  39.0  88.5   7.6   168 ]
```


Probably, the statistical analysis will involve only the blood measures,









```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$

(%i3) subsample (s3, lambda([v], v[1] = B and v[2] > 38),
           3, 4, 5, 6);
                   [ 28.0  102.3  17.1  146 ]
                   [                        ]
                   [ 21.0  92.4   10.3  197 ]
                   [                        ]
                   [ 23.0  111.5  10.0  133 ]
                   [                        ]
                   [ 26.0  92.6   12.3  196 ]
(%o3)              [                        ]
                   [ 25.0  98.7   10.0  174 ]
                   [                        ]
                   [ 21.0  93.2   5.9   181 ]
                   [                        ]
                   [ 18.0  95.0   11.3  66  ]
                   [                        ]
                   [ 39.0  88.5   7.6   168 ]
```


This is the multivariate mean of `s3`,








```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$

(%i3) mean (s3);
       13 B + 7 A  317
(%o3) [----------, ---, 87.178, 0.06 NA + 81.44999999999999, 
           20      10
                                                    3 NA + 19587
                                18.122999999999998, ------------]
                                                        100
```


Here, the first component is meaningless, since `A` and `B` are categorical, the second component is the mean age of individuals in rational form, and the fourth and last values exhibit some strange behaviour. This is because symbol `NA` is used here to indicate *non available* data, and the two means are nonsense. A possible solution would be to take out from the matrix those rows with `NA` symbols, although this deserves some loss of information.









```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) g(v):= v[4] # NA and v[6] # NA $

(%i4) mean (subsample (s3, g, 3, 4, 5, 6));
(%o4) [79.4923076923077, 86.2032967032967, 16.93186813186813, 
                                                            2514
                                                            ----]
                                                             13
```

### Function: supcontext (supcontext, name, context, supcontext, name, supcontext)

Creates a new context, called *name*, which has *context* as a
subcontext.  *context* must exist.


If *context* is not specified, the current context is assumed.


If *name* is not specified, a new name is created (via `gensym`) and returned.


`supcontext` evaluates its argument.
`supcontext` returns *name* (if specified) or the new context name.

### Variable: surface

The surfaces of the object will be rendered and the lines and points of
the triangulation used to build the surface will not be shown. This is
the default behavior, which can be changed using either the option
`object_005fpoints` or `object_005fwireframe`.

See also: `object_points`, `object_wireframe`.

### Variable: tab

The tab character.

### Function: tcl_output (tcl_output, list, i0, skip, tcl_output, list, i0, tcl_output, list_1, ..., list_n, i)

Prints elements of a list enclosed by curly braces `{ }`,
suitable as part of a program in the Tcl/Tk language.


`tcl_output (list, i0, skip)`
prints *list*, beginning with element *i0* and printing elements
`i0 + skip`, `i0 + 2 skip`, etc.


`tcl_output (list, i0)`
is equivalent to `tcl_output (list, i0, 2)`.


`tcl_output ([list_1, ..., list_n], i)`
prints the *i*’th elements of *list_1*, ..., *list_n*.


Examples:













```maxima
(%i1) tcl_output ([1, 2, 3, 4, 5, 6], 1, 3)$

 {1.000000000     4.000000000     
 }
(%i2) tcl_output ([1, 2, 3, 4, 5, 6], 2, 3)$

 {2.000000000     5.000000000     
 }
(%i3) tcl_output ([3/7, 5/9, 11/13, 13/17], 1)$

 {((RAT SIMP) 3 7) ((RAT SIMP) 11 13) 
 }
(%i4) tcl_output ([x1, y1, x2, y2, x3, y3], 2)$

 {$Y1 $Y2 $Y3 
 }
(%i5) tcl_output ([[1, 2, 3], [11, 22, 33]], 1)$

 {SIMP 1.000000000     11.00000000     
 }
```

### Variable: testsuite_files

`testsuite_files` is the set of tests to be run by
`run_005ftestsuite`.  It is a list of names of the files containing
the tests to run.  If some of the tests in a file are known to fail,
then instead of listing the name of the file, a list containing the
file name and the test numbers that fail is used.


For example, this is a part of the default set of tests:



```maxima
["rtest13s", ["rtest14", 57, 63]]
```


This specifies the testsuite consists of the files "rtest13s" and
"rtest14", but "rtest14" contains two tests that are known to fail: 57
and 63.

See also: `run_testsuite`.

### Variable: thetaresolution

Default value: ``


The number of sub-intervals into which the theta angle interval from
`object_005fstarttheta` to `object_005fendtheta`
will be divided. *num* must be a positive integer.


See also `object_005fstarttheta` and
`object_005fendtheta`.

See also: `object_starttheta`, `object_endtheta`.

### Function: todd_coxeter (todd_coxeter, relations, subgroup, todd_coxeter, relations)

Find the order of G/H where G is the Free Group modulo *relations*, and
H is the subgroup of G generated by *subgroup*.  *subgroup* is an optional
argument, defaulting to [].  In doing this it produces a
multiplication table for the right action of G on G/H, where the
cosets are enumerated [H,Hg2,Hg3,...].  This can be seen internally in
the variable `todd_coxeter_state`.


Example:














```maxima
maxima

(%i1) symet(n):=create_list(
        if (j - i) = 1 then (p(i,j))^^3 else
            if (not i = j) then (p(i,j))^^2 else
                p(i,i) , j, 1, n-1, i, 1, j);
                                                       <3>
(%o1) symet(n) := create_list(if j - i = 1 then p(i, j)
                                <2>
 else (if not i = j then p(i, j)    else p(i, i)), j, 1, n - 1, 
i, 1, j)


(%i2) p(i,j) := concat(x,i).concat(x,j);
(%o2)        p(i, j) := concat(x, i) . concat(x, j)


(%i3) symet(5);
         <2>           <3>    <2>           <2>           <3>
(%o3) [x1   , (x1 . x2)   , x2   , (x1 . x3)   , (x2 . x3)   , 
            <2>           <2>           <2>           <3>    <2>
          x3   , (x1 . x4)   , (x2 . x4)   , (x3 . x4)   , x4   ]


(%i4) todd_coxeter(%o3);
Rows tried 426
(%o4)                          120


(%i5) todd_coxeter(%o3,[x1]);
Rows tried 213
(%o5)                          60


(%i6) todd_coxeter(%o3,[x1,x2]);
Rows tried 71
(%o6)                          20
```

### Function: toffoli (q, i, j, k)

Changes the value of the *k*’th qubit, in the state *q* of
*n* qubits, if the values of the *i*’th anf *j*’th qubits
are equal to 1. It modifies the list *q* and returns its new value.

### Function: tprod (o1, ..., on)

Returns the tensor product of the *n* matrices or lists *o1*,
..., *on*.

### Function: tracematrix (M)

Returns the trace (sum of the diagonal elements) of matrix *M*.


To use this function write first `load("functs")`.

### Variable: track

*positions* should be a list of points. When the play button is
pressed, the object position will be changed sequentially through all
the points in the list, at intervals of time given by the option
`scene_005ftstep`, leaving behind a track of the object’s
trajectory. The rewind button can be used to point at the start of the
sequence making the animation restart after the play button is pressed
again.


**Example**. This will show the trajectory of a ball thrown with
speed of 5 m/s, at an angle of 45 degrees, when the air resistance can
be neglected:



```maxima
(%i1) p: makelist ([0,4*t,4*t- 9.8*t^2/2], t, 0, 0.82, 0.01)$

(%i2) ball: [sphere, [radius,0.1], [color,red], [track,p]]$

(%i3) ground: [cube, [xlength,2], [ylength,4], [zlength,0.2],
      [position,0,1.5,-0.2],[color,green]]$

(%i4) scene (ball, ground)$
```


See also `object_005fanimation`.

See also: `scene_tstep`, `object_animation`.

### Function: transform_sample (matrix, varlist, exprlist)

Transforms the sample *matrix*, where each column is called according to
*varlist*, following expressions in *exprlist*.


Examples:


The second argument assigns names to the three columns. With these names,
a list of expressions define the transformation of the sample.



```maxima
(%i1) load ("descriptive")$
(%i2) data: matrix([3,2,7],[3,7,2],[8,2,4],[5,2,4]) $

(%i3) transform_sample(data, [a,b,c], [c, a*b, log(a)]);
                               [ 7  6   log(3) ]
                               [               ]
                               [ 2  21  log(3) ]
(%o3)                          [               ]
                               [ 4  16  log(8) ]
                               [               ]
                               [ 4  10  log(5) ]
```


Add a constant column and remove the third variable.



```maxima
(%i1) load ("descriptive")$
(%i2) data: matrix([3,2,7],[3,7,2],[8,2,4],[5,2,4]) $
(%i3) transform_sample(data, [a,b,c], [makelist(1,k,length(data)),a,b]);

                                  [ 1  3  2 ]
                                  [         ]
                                  [ 1  3  7 ]
(%o3)                             [         ]
                                  [ 1  8  2 ]
                                  [         ]
                                  [ 1  5  2 ]
```

### Function: treefale (n)

3 contractive maps all with the same contraction ratio.
Argument *n* must be great enough, 10000 or greater.


Example:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,treefale(n)], [style,dots])$
```

### Variable: trivial_solutions

Default value: `true`


When `trivial_solutions` is `true`,
`Zeilberger` returns solutions
which have certificate equal to zero, or all coefficients equal to zero.

### Variable: tstep

Default value: `10`


The amount of time, in mili-seconds, between iterations among
consecutive animation frames. *time* must be a real number.

### Function: unicode (arg)

Returns the character defined by *arg* which might be a Unicode code point 
or a name string if the underlying Lisp provides full Unicode support. 


Example: Characters defined by hexadecimal code points
(Maxima with SBCL on GNU/Linux). 



```maxima
(%i1) ibase: 16.$
(%i2) map(unicode, [24, 0A3, 20AC]);
(%o2)                            [$, GBP, EUR]
```


Warning: In wxMaxima with SBCL on Windows it is not possible to convert 
code points larger than 16 bit to characters when the external format 
has not been set to UTF-8. See `adjust_005fexternal_005fformat` for more information.








CMUCL doesn’t process code points larger than 16 bit. 
In these cases `unicode` returns `false`. 

Converting a code point to a character via UTF-8 octets may serve as a workaround: 


`octets_to_string(unicode_to_utf8(code_point));`








See `octets_005fto_005fstring`, `unicode_005fto_005futf8`.


In case the underlying Lisp provides full Unicode support the character might be 
specified by its name. The following is possible in ECL, CLISP and SBCL, 
where in SBCL on Windows the external format has to be set to UTF-8.
`unicode(name)` is supported by CMUCL too but again limited to 16 bit 
characters. 


The string argument to `unicode` is basically the same string returned by 
`printf` using the "~@c" specifier. 
But as shown below the prefix "#\" must be omitted. 
Underlines might be replaced by spaces and uppercase letters by lowercase ones.


Example (continued): Characters defined by names 
(Maxima with SBCL on GNU/Linux). 



```maxima
(%i3) printf(false, "~@c", unicode(0DF));
(%o3)                    #\LATIN_SMALL_LETTER_SHARP_S
(%i4) unicode("LATIN_SMALL_LETTER_SHARP_S");
(%o4)                                  ß
(%i5) unicode("Latin small letter sharp s");
(%o5)                                  ß
```

See also: `adjust_external_format`, `octets_to_string`, `unicode_to_utf8`.

### Function: unicode_to_utf8 (code_point)

Returns a list containing the UTF-8 code corresponding to the Unicode *code_point*.


Examples: Converting Unicode code points to UTF-8 and vice versa. 



```maxima
(%i1) ibase: obase: 16.$
(%i2) map(cint, ["$","GBP","EUR"]);
(%o2)                           [24, 0A3, 20AC]
(%i3) map(unicode_to_utf8, %);
(%o3)                 [[24], [0C2, 0A3], [0E2, 82, 0AC]]
(%i4) map(utf8_to_unicode, %);
(%o4)                           [24, 0A3, 20AC]
```

### Function: uppercasep (char)

Returns `true` if *char* is an uppercase character. 


Note: See remarks on `alphacharp`.

See also: `alphacharp`.

### Variable: us_ascii_only

This option variable affects Maxima when the character encoding 
provided by the application which runs Maxima is UTF-8 but the 
external format of the Lisp reader is not equal to UTF-8. 


On GNU/Linux this is true when Maxima is built with GCL 
and on Windows in wxMaxima with GCL- and SBCL-builds. 
With SBCL it is recommended to change the external format to UTF-8. 
Setting `us_ascii_only` is unnecessary then. 
See `adjust_005fexternal_005fformat` for details. 


`us_ascii_only` is `false` by default. 
Maxima itself then (i.e. in the above described situation) parses the UTF-8 encoding.


When `us_ascii_only` is set to `true` it is assumed that all strings 
used as arguments to string processing functions do not contain Non-US-ASCII characters. 
Given that promise, Maxima avoids parsing UTF-8 and strings can be processed more efficiently.

See also: `adjust_external_format`.

### Function: utf8_to_unicode (list)

Returns a Unicode code point corresponding to the *list* which must contain 
the UTF-8 encoding of a single character.


Examples: See `unicode_005fto_005futf8`.

See also: `unicode_to_utf8`.

### Function: vers (x)

Returns the versed sine `1 - cos (x)`.


To use this function write first `load("functs")`.

### Variable: warnings

Default value: `true`


When `warnings` is `true`,
functions in the `zeilberger` package print
warning messages during execution.

### Variable: wc_defaultsigma

Default value: `6`


Defines how many sigmas of the gauss distribution that represents the
tolerances of a parameter correspond to a *tol[n]* value of -1...1.


See also `wc_005fmintypmax_005frss`.


Example:


















```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$

(%i3) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o3) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 1000.0 (0.01 tol  + 1)]
                                                          2


(%i4) assume(U_In>0);
(%o4)                      [U_In > 0]


(%i5) divider:U_Out=U_In*R_1/(R_1+R_2);
                                R_1 U_In
(%o5)                   U_Out = ---------
                                R_2 + R_1

(%i6) wc_defaultsigma:1$

(%i7) lhs(divider)=wc_mintypmax_rss(subst(vals,rhs(divider)),6);
(%o7) U_Out = [min = 0.4787867965644036 U_In, typ = 0.5 U_In, 
 max = 0.5212132034355964 U_In, Fail = 0.0019731752898266564 ppm]

(%i8) wc_defaultsigma:3$

(%i9) lhs(divider)=wc_mintypmax_rss(subst(vals,rhs(divider)),6);
(%o9) U_Out = [min = 0.49292893218813455 U_In, typ = 0.5 U_In, 
 max = 0.5070710678118655 U_In, Fail = 0.0019731752898266564 ppm]

(%i10) wc_defaultsigma:6$

(%i11) lhs(divider)=wc_mintypmax_rss(subst(vals,rhs(divider)),6);
(%o11) U_Out = [min = 0.49646446609406725 U_In, typ = 0.5 U_In, 
 max = 0.5035355339059328 U_In, Fail = 0.0019731752898266564 ppm]
```

See also: `wc_mintypmax_rss`.

### Variable: wc_defaultvaluespertol

Default value: `3`


Defines how many samples per *tol[n]* the EWC method of
`wc_systematic` and `wc_mintypmax` shall use by default.


See also `wc_systematic` and `wc_005fmintypmax`.


Example:
















```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$

(%i3) vals: [
   R_1= 100.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o3) [R_1 = 100.0 (0.01 tol  + 1), R_2 = 1000.0 (0.01 tol  + 1)]
                            1                             2

(%i4) wc_defaultvaluespertol:2$

(%i5) wc_systematic(vals);
(%o5) [[R_1 = 99.0, R_2 = 990.0], [R_1 = 99.0, R_2 = 1010.0], 
         [R_1 = 101.0, R_2 = 990.0], [R_1 = 101.0, R_2 = 1010.0]]

(%i6) wc_defaultvaluespertol:3$

(%i7) wc_systematic(vals);
(%o7) [[R_1 = 99.0, R_2 = 990.0], [R_1 = 99.0, R_2 = 1000.0], 
[R_1 = 99.0, R_2 = 1010.0], [R_1 = 100.0, R_2 = 990.0], 
[R_1 = 100.0, R_2 = 1000.0], [R_1 = 100.0, R_2 = 1010.0], 
[R_1 = 101.0, R_2 = 990.0], [R_1 = 101.0, R_2 = 1000.0], 
[R_1 = 101.0, R_2 = 1010.0]]

(%i8) wc_defaultvaluespertol:5$

(%i9) wc_systematic(vals);
(%o9) [[R_1 = 99.0, R_2 = 990.0], [R_1 = 99.0, R_2 = 995.0], 
[R_1 = 99.0, R_2 = 1000.0], [R_1 = 99.0, 
R_2 = 1004.9999999999999], [R_1 = 99.0, R_2 = 1010.0], 
[R_1 = 99.5, R_2 = 990.0], [R_1 = 99.5, R_2 = 995.0], 
[R_1 = 99.5, R_2 = 1000.0], [R_1 = 99.5, 
R_2 = 1004.9999999999999], [R_1 = 99.5, R_2 = 1010.0], 
[R_1 = 100.0, R_2 = 990.0], [R_1 = 100.0, R_2 = 995.0], 
[R_1 = 100.0, R_2 = 1000.0], [R_1 = 100.0, 
R_2 = 1004.9999999999999], [R_1 = 100.0, R_2 = 1010.0], 
[R_1 = 100.49999999999999, R_2 = 990.0], 
[R_1 = 100.49999999999999, R_2 = 995.0], 
[R_1 = 100.49999999999999, R_2 = 1000.0], 
[R_1 = 100.49999999999999, R_2 = 1004.9999999999999], 
[R_1 = 100.49999999999999, R_2 = 1010.0], 
[R_1 = 101.0, R_2 = 990.0], [R_1 = 101.0, R_2 = 995.0], 
[R_1 = 101.0, R_2 = 1000.0], [R_1 = 101.0, 
R_2 = 1004.9999999999999], [R_1 = 101.0, R_2 = 1010.0]]
```

See also: `wc_systematic`, `wc_mintypmax`.

### Function: wc_ewc_simplify (expression, definitions, ...)

Brute-forcing through all combinations of *tol[n]* in order to find the
worst-case combination is O(m^n)-complete and therefore computationally intensive
for high numbers of tol[n].


`wc_ewc_simplify` uses the sign of the derivatives of *expression* to combine
as many `tol[n]`, as possible. The result is an expression that might run much
faster through `wc_mintypmax` and `wc_systematic`, but that, if the derivate
of *expression* doesn’t change sign in the *tol[n]* space, still yields the
same results for the brute-force approaches to worst-case analysis.


Note that changing the number of *tol[n]* will change the statistical distribution
of the results over the *tol[n]* space and therefore will change the statistical
distribution of the montecarlo method and the results of the root sum square functions.



See also `wc_mintypmax` and `wc_005fmontecarlo`.


*definitions* allows to temporarily asssign values to specific *tol[n]* during
the optimizations (normally optimizagion is done with all *tol[n]* being zero)
which has the side-effect of excempting these *tol[n]* from the
optimization.


Example:


















```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 2000.0*(1+tol[2]*.01)
 ];
(%o2) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 2000.0 (0.01 tol  + 1)]
                                                          2


(%i3) ratprint:false;
(%o3)                         false


(%i4) assume(U_In>0);
(%o4)                      [U_In > 0]


(%i5) divider: U_Out=U_In*(R_1)/(R_1+R_2);
                                R_1 U_In
(%o5)                   U_Out = ---------
                                R_2 + R_1


(%i6) divider_vals:subst(vals,divider);
                        1000.0 (0.01 tol  + 1) U_In
                                        1
(%o6) U_Out = -----------------------------------------------
              2000.0 (0.01 tol  + 1) + 1000.0 (0.01 tol  + 1)
                              2                        1


(%i7) divider_vals_simplified:lhs(divider_vals)=wc_ewc_simplify(rhs(divider_vals));
                        1000.0 (1 - 0.01 tol ) U_In
                                            2
(%o7) U_Out = -----------------------------------------------
              2000.0 (0.01 tol  + 1) + 1000.0 (1 - 0.01 tol )
                              2                            2


(%i8) wc_systematic(rhs(divider_vals));
(%o8) [0.33333333333333337 U_In, 0.3311036789297659 U_In, 
0.3289036544850498 U_In, 0.3355704697986577 U_In, 
0.3333333333333333 U_In, 0.33112582781456956 U_In, 
0.3377926421404682 U_In, 0.3355481727574751 U_In, 
0.3333333333333333 U_In]


(%i9) wc_systematic(rhs(divider_vals_simplified));
(%o9) [0.3377926421404682 U_In, 0.3333333333333333 U_In, 
                                         0.3289036544850498 U_In]


(%i10) lhs(divider_vals)=wc_mintypmax(rhs(divider_vals));
(%o10) U_Out = [min = 0.3289036544850498 U_In, 
    typ = 0.3333333333333333 U_In, max = 0.3377926421404682 U_In]


(%i11) lhs(divider_vals_simplified)=wc_mintypmax(rhs(divider_vals_simplified));
(%o11) U_Out = [min = 0.3289036544850498 U_In, 
    typ = 0.3333333333333333 U_In, max = 0.3377926421404682 U_In]
```


Use case for adding definitions (*tol["E_Gain"]* cannot be optimized without
knowing the sign of *tol["U_In"]*):

















```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [
   U_In=1.2*tol["U_In"], /* The input voltage range */
   n_Bits=16,            /* The ADC's number of bits */
   U_Ref=1.2*(1+.01*tol["U_Ref"]), /* The Adc's reference */
   E_Gain=1+1.2e-6*tol["E_Gain"], /* Gain error */
   E_Offset=1.5e-6                /* Offset error */
 ];
(%o2) [U_In = 1.2 tol    , n_Bits = 16, 
                     U_In
U_Ref = 1.2 (0.01 tol      + 1), E_Gain = 1.2e-6 tol       + 1, 
                     U_Ref                          E_Gain
E_Offset = 1.5e-6]


(%i3) ratprint:false;
(%o3)                         false


(%i4) wc_inputvalueranges(vals);
           [   U_In      - 1.2      0        1.2    ]
           [                                        ]
           [  n_Bits      16        16       16     ]
           [                                        ]
(%o4)      [  U_Ref      1.188     1.2      1.212   ]
           [                                        ]
           [  E_Gain   0.9999988    1     1.0000012 ]
           [                                        ]
           [ E_Offset   1.5e-6    1.5e-6   1.5e-6   ]


(%i5) ndsadc:n_DSADC=((U_In*E_Gain+E_Offset)/U_Ref+.5)*(2^(n_Bits)-1);
                  n_Bits       E_Gain U_In + E_Offset
(%o5) n_DSADC = (2       - 1) (---------------------- + 0.5)
                                       U_Ref


(%i6) lhs(ndsadc)=wc_ewc_simplify(subst(vals,rhs(ndsadc)));
(%o6) n_DSADC = 65535 ((0.8333333333333334
 (1.5e-6 - 1.2 (1.2e-6 tol       + 1) tol     ))
                          E_Gain         U_Ref
/(0.01 tol      + 1) + 0.5)
          U_Ref


(%i7) lhs(ndsadc)=wc_ewc_simplify(subst(vals,rhs(ndsadc)),tol["U_In"]=1);
(%o7) n_DSADC = 65535 ((0.8333333333333334
 (1.2 tol     (1 - 1.2e-6 tol     ) + 1.5e-6))
         U_In                U_Ref
/(0.01 tol      + 1) + 0.5)
          U_Ref
```

See also: `wc_mintypmax`, `wc_montecarlo`.

### Function: wc_inputvalueassumptions (expr)

Often it is good practice to keep all numeric values with tolerances in a list
and to introduce them into the equations only when needed.


`wc_inputvalueassumptions` in this case can inform the
`assume` database about the range each variable in that list will
be in.


See also `wc_tolassumptions`, `wc_inputvalueranges` and
`assume`.


Example:














```maxima
maxima

(%i1) load("wrstcse");
(%o1) /home/gunter/src/maxima-code/share/contrib/wrstcse.mac


(%i2) vals:[
    R_1=100*(1+1/100*tol["R1"])*(1+1/100*tol["Temp"]),
    R_2=200*(1+1/100*tol["R2"])*(1+1/100*tol["Temp"])];
                  tol         tol
                     R1          Temp
(%o2) [R_1 = 100 (----- + 1) (------- + 1), 
                   100          100
                                        tol         tol
                                           R2          Temp
                             R_2 = 200 (----- + 1) (------- + 1)]
                                         100          100


(%i3) float(wc_inputvalueassumptions(%));
(%o3) [R_2 >= 196.02, R_2 <= 204.02, R_1 >= 98.01, R_1 <= 102.01]


(%i4) is(R_1>R_2);
(%o4)                         false


(%i5) is(R_1>90);
(%o5)                         true


(%i6) is(R_1>200);
(%o6)                         false


(%i7) is(R_1<200);
(%o7)                         true


(%i8) is(R_1>100);
(%o8)                        unknown
```

See also: `wc_tolassumptions`, `wc_inputvalueranges`, `assume`.

### Function: wc_inputvalueranges (expression, show_tols)

Convenience function: Displays a list which parameter can vary between
which values.


If *show_tols* is `true` then this function additionally displays
which *tol[n]* each variable is affected by.


See also `wc_mintypmax2tol` and `wc_005finputvalueassumptions`.


Example:













```maxima
maxima

(%i1) fpprintprec:4;
(%o1)                           4

(%i2) load("wrstcse")$

(%i3) vals: [
   R_1= 1000.0*(1+tol["R_1"]*.01+tol["Temp"]*.001),
   R_2= 2000.0*(1+tol["R_2"]*.01+tol["Temp"]*.001),
   R_3= 2000.0*(1+tol["R_3"]*.01)
 ];
(%o3) [R_1 = 1000.0 (0.001 tol     + 0.01 tol    + 1), 
                              Temp           R_1
R_2 = 2.0e+3 (0.001 tol     + 0.01 tol    + 1), 
                       Temp           R_2
R_3 = 2.0e+3 (0.01 tol    + 1)]
                      R_3


(%i4) wc_inputvalueranges(vals);
               [ R_1   989.0    1000.0  1.011e+3 ]
               [                                 ]
(%o4)          [ R_2  1.978e+3  2.0e+3  2.022e+3 ]
               [                                 ]
               [ R_3  1.98e+3   2.0e+3  2.02e+3  ]


(%i5) wc_inputvalueranges(vals,true);
      [ R_1   989.0    1000.0  1.011e+3  [tol    , tol   ] ]
      [                                      Temp     R_1  ]
      [                                                    ]
(%o5) [ R_2  1.978e+3  2.0e+3  2.022e+3  [tol    , tol   ] ]
      [                                      Temp     R_2  ]
      [                                                    ]
      [ R_3  1.98e+3   2.0e+3  2.02e+3       [tol   ]      ]
      [                                          R_3       ]
```

See also: `wc_mintypmax2tol`, `wc_inputvalueassumptions`.

### Function: wc_inputvalues_max (listofinputvalues)

Sets all the input values contained in *listofinputvalues* to their
maximum values and returns the result. Helpful for example when trying
to determine the maximum result of complicated filters;


See also `wc_005finputvalues_005fmin`.


Example:














```maxima
maxima

(%i1) fpprintprec:4;
(%o1)                           4

(%i2) load("wrstcse")$

(%i3) vals: [
   R_1= 1000.0*(1+tol["R_1"]*.01+tol["Temp"]*.001),
   R_2= 2000.0*(1+tol["R_2"]*.01+tol["Temp"]*.001),
   R_3= 2000.0*(1+tol["R_3"]*.01)
 ];
(%o3) [R_1 = 1000.0 (0.001 tol     + 0.01 tol    + 1), 
                              Temp           R_1
R_2 = 2.0e+3 (0.001 tol     + 0.01 tol    + 1), 
                       Temp           R_2
R_3 = 2.0e+3 (0.01 tol    + 1)]
                      R_3


(%i4) wc_inputvalueranges(vals);
               [ R_1   989.0    1000.0  1.011e+3 ]
               [                                 ]
(%o4)          [ R_2  1.978e+3  2.0e+3  2.022e+3 ]
               [                                 ]
               [ R_3  1.98e+3   2.0e+3  2.02e+3  ]


(%i5) vals_max:wc_inputvalues_max(vals);
(%o5)    [R_1 = 1.011e+3, R_2 = 2.022e+3, R_3 = 2.02e+3]


(%i6) wc_inputvalueranges(vals_max);
              [ R_1  1.011e+3  1.011e+3  1.011e+3 ]
              [                                   ]
(%o6)         [ R_2  2.022e+3  2.022e+3  2.022e+3 ]
              [                                   ]
              [ R_3  2.02e+3   2.02e+3   2.02e+3  ]
```

See also: `wc_inputvalues_min`.

### Function: wc_inputvalues_min (listofinputvalues)

Sets all the input values contained in *listofinputvalues* to their
minimum values and returns the result. Helpful for example when trying
to determine the minimum result of complicated filters;


See also `wc_005finputvalues_005fmin`.


Example:













```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [
   R_1= 1000.0*(1+tol["R_1"]*.01+tol["Temp"]*.001),
   R_2= 2000.0*(1+tol["R_2"]*.01+tol["Temp"]*.001),
   R_3= 2000.0*(1+tol["R_3"]*.01)
 ];
(%o2) [R_1 = 1000.0 (0.001 tol     + 0.01 tol    + 1), 
                              Temp           R_1
R_2 = 2000.0 (0.001 tol     + 0.01 tol    + 1), 
                       Temp           R_2
R_3 = 2000.0 (0.01 tol    + 1)]
                      R_3


(%i3) wc_inputvalueranges(vals);
           [ R_1  989.0   1000.0  1010.9999999999999 ]
           [                                         ]
(%o3)      [ R_2  1978.0  2000.0  2021.9999999999998 ]
           [                                         ]
           [ R_3  1980.0  2000.0        2020.0       ]


(%i4) vals_min:wc_inputvalues_min(vals);
(%o4)       [R_1 = 989.0, R_2 = 1978.0, R_3 = 1980.0]


(%i5) wc_inputvalueranges(vals_min);
                 [ R_1  989.0   989.0   989.0  ]
                 [                             ]
(%o5)            [ R_2  1978.0  1978.0  1978.0 ]
                 [                             ]
                 [ R_3  1980.0  1980.0  1980.0 ]
```

See also: `wc_inputvalues_min`.

### Function: wc_max (expr, num)

Outputs only the maximum value of *expr*). If *num* is present it tells
maxima how many samples to try out of the range of each tolerance.


See also `wc_max`, `wc_typicalvalues` and `wc_005fmintypmax`.


Example:











```maxima
maxima

(%i1) load("wrstcse");
(%o1) /home/gunter/src/maxima-code/share/contrib/wrstcse.mac


(%i2) vals:[
    R_1=100*(1+1/100*tol["R1"])*(1+1/100*tol["Temp"]),
    R_2=200*(1+1/100*tol["R2"])*(1+1/100*tol["Temp"])];
                  tol         tol
                     R1          Temp
(%o2) [R_1 = 100 (----- + 1) (------- + 1), 
                   100          100
                                        tol         tol
                                           R2          Temp
                             R_2 = 200 (----- + 1) (------- + 1)]
                                         100          100


(%i3) rtotal:R_Total=R_1+R_2;
(%o3)                  R_Total = R_2 + R_1


(%i4) wc_mintypmax(subst(vals,rhs(rtotal)));
                     29403                   30603
(%o4)         [min = -----, typ = 300, max = -----]
                      100                     100


(%i5) wc_max(subst(vals,rhs(rtotal)));
                              30603
(%o5)                         -----
                               100
```

See also: `wc_max`, `wc_typicalvalues`, `wc_mintypmax`.

### Function: wc_min (expr, num)

Outputs only the minimum value of *expr*). If *num* is present it tells
maxima how many samples to try out of the range of each tolerance.


See also `wc_max`, `wc_typicalvalues` and `wc_005fmintypmax`.


Example:











```maxima
maxima

(%i1) load("wrstcse");
(%o1) /home/gunter/src/maxima-code/share/contrib/wrstcse.mac


(%i2) vals:[
    R_1=100*(1+1/100*tol["R1"])*(1+1/100*tol["Temp"]),
    R_2=200*(1+1/100*tol["R2"])*(1+1/100*tol["Temp"])];
                  tol         tol
                     R1          Temp
(%o2) [R_1 = 100 (----- + 1) (------- + 1), 
                   100          100
                                        tol         tol
                                           R2          Temp
                             R_2 = 200 (----- + 1) (------- + 1)]
                                         100          100


(%i3) rtotal:R_Total=R_1+R_2;
(%o3)                  R_Total = R_2 + R_1


(%i4) wc_mintypmax(subst(vals,rhs(rtotal)));
                     29403                   30603
(%o4)         [min = -----, typ = 300, max = -----]
                      100                     100


(%i5) wc_min(subst(vals,rhs(rtotal)));
                              29403
(%o5)                         -----
                               100
```

See also: `wc_max`, `wc_typicalvalues`, `wc_mintypmax`.

### Function: wc_mintypmax (expr, n)

Prints the minimum, maximum and typical value of *expr*. If *n*
is positive, *n* values for each parameter will be tried systematically.
If *n* is negative, *-n* random values are used instead.
If no *n* is given, *wc_defaultvaluespertol* is assumed.


See also `wc_mintypmax_percent`, `wc_mintypmax_rss`,
`wc_mintypmax_num`,
`wc_min`,
`wc_max`,
`wc_ewc_simplify` and `wc_005fsystematic`.


Example:













```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$

(%i3) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o3) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 1000.0 (0.01 tol  + 1)]
                                                          2


(%i4) assume(U_In>0);
(%o4)                      [U_In > 0]


(%i5) divider:U_Out=U_In*R_1/(R_1+R_2);
                                R_1 U_In
(%o5)                   U_Out = ---------
                                R_2 + R_1


(%i6) lhs(divider)=wc_mintypmax(subst(vals,rhs(divider)));
(%o6) U_Out = [min = 0.495 U_In, typ = 0.5 U_In, 
                                                max = 0.505 U_In]
```

See also: `wc_mintypmax_percent`, `wc_mintypmax_rss`, `wc_mintypmax_num`, `wc_min`, `wc_max`, `wc_ewc_simplify`, `wc_systematic`.

### Function: wc_mintypmax2tol (tolname, minval, typval, maxval)

Generates a parameter that uses the tolerance *tolname* and tolerates between the
given values.


Example:









```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [U_Diode=wc_mintypmax2tol(tol[1],.5,.75,.82),
       R=wc_mintypmax2tol(tol[2],1,1.1,1.3),
       U_In=wc_mintypmax2tol(tol[3],0,0,15)];
(%o2) [U_Diode = 0.034999999999999976 (|tol | + tol )
                                       |   1|      1
 + 0.125 (tol  - |tol |) + 0.75, 
             1   |   1|
R = 0.09999999999999998 (|tol | + tol )
                         |   2|      2
 + 0.050000000000000044 (tol  - |tol |) + 1.1, 
                            2   |   2|
       15 (|tol | + tol )
           |   3|      3
U_In = ------------------]
               2


(%i3) wc_inputvalueranges(vals);
                  [ U_Diode  0.5  0.75  0.82 ]
                  [                          ]
(%o3)             [    R     1.0  1.1   1.3  ]
                  [                          ]
                  [  U_In     0    0     15  ]
```

### Function: wc_mintypmax_num (equation, var, range_min)

*range_max*, [*n*])


For each tolerance calculation in *equation* this tries to numerically find the value
of *var* that solves *equation*. Expects the value of *var* to be in the range
*range_min*...*range_max*. Additionally expects `lhs(equation)-rhs(equation)`
to change sign within that range.


See also `wc_mintypmax`,


Example:














```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$

(%i3) vals: [
   f=(1+tol["f"]*.2),
   A=(1+tol["A"]*.1)
 ]$


(%i4) wc_inputvalueranges(vals,true);
                   [ f  0.8  1  1.2  [tol ] ]
                   [                     f  ]
(%o4)              [                        ]
                   [ A  0.9  1  1.1  [tol ] ]
                   [                     A  ]


(%i5) assume(U_In>0);
(%o5)                      [U_In > 0]


(%i6) eq:cos(2*%pi*f*x)=A*x;
(%o6)                 cos(2 %pi f x) = A x


(%i7) x=wc_mintypmax_num(subst(vals,eq),x,0,.3);
(%o7) x = [min = 0.18165213379777342, typ = 0.21544061525279004, 
                                        max = 0.2646539803703126]
```

See also: `wc_mintypmax`.

### Function: wc_mintypmax_percent (expr, sigmas)

Like `wc_mintypmax`, but outputs the tolerance range in percent.


See `wc_005fmintypmax`.


Example:















```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$
(%i3) wc_defaultsigma:6$

(%i4) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o4) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 1000.0 (0.01 tol  + 1)]
                                                          2


(%i5) assume(U_In>0);
(%o5)                      [U_In > 0]


(%i6) divider:U_Out=U_In*R_1/(R_1+R_2);
                                R_1 U_In
(%o6)                   U_Out = ---------
                                R_2 + R_1


(%i7) lhs(divider)=wc_mintypmax(subst(vals,rhs(divider)));
(%o7) U_Out = [min = 0.495 U_In, typ = 0.5 U_In, 
                                                max = 0.505 U_In]


(%i8) lhs(divider)=wc_mintypmax_percent(subst(vals,rhs(divider)));
(%o8) U_Out = [min = - 1.0000000000000009 %, typ = 0.5 U_In, 
                                      max = 1.0000000000000009 %]
```

See also: `wc_mintypmax`.

### Function: wc_mintypmax_rss (expr, sigmas)

Prints the minimum and maximum of *expr*, as well as how high the
probability is that *expr* will lie out of that range based on a root
sum square calculation and assuming all input ranges will be gauss-shaped.


*wc_defaultsigma* defines how many sigma of an input value’s tolerance
distribution the range of *tol[n]*=[-1...1] corresponds to.


The RSS methods has a few advantages a brute-force worst-case calculation:
It is fast even witput `wc_ewc_simplify`. It prevents overengineering
resulting from assuming all tolerances to add up in a catastrophical way if
this only happens in a neglectible number of cases. But it will yield only
the correct results if the gaussian distribution of the input data is known.


Due to its nature this method doesn’t support tolerances that aren’t
symmetrical. Therefore in that case the tolerances are extended in the
direction that is less wide.


See also `wc_defaultsigma` `wc_mintypmax_rss_percent`, and
`wc_005fmintypmax`.


Example:














```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$
(%i3) wc_defaultsigma:6$

(%i4) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o4) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 1000.0 (0.01 tol  + 1)]
                                                          2


(%i5) assume(U_In>0);
(%o5)                      [U_In > 0]


(%i6) divider:U_Out=U_In*R_1/(R_1+R_2);
                                R_1 U_In
(%o6)                   U_Out = ---------
                                R_2 + R_1


(%i7) lhs(divider)=wc_mintypmax_rss(subst(vals,rhs(divider)),6);
(%o7) U_Out = [min = 0.49646446609406725 U_In, typ = 0.5 U_In, 
 max = 0.5035355339059328 U_In, Fail = 0.0019731752898266564 ppm]
```

See also: `wc_ewc_simplify`, `wc_defaultsigma`, `wc_mintypmax_rss_percent`, `wc_mintypmax`.

### Function: wc_mintypmax_rss_percent (expr, sigmas)

Like `wc_mintypmax_rss`, but outputs the tolerance range in percent.


See `wc_005fmintypmax_005frss`.


Example:















```maxima
maxima
(%i1) load("wrstcse")$
(%i2) ratprint:false$
(%i3) wc_defaultsigma:6$

(%i4) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o4) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 1000.0 (0.01 tol  + 1)]
                                                          2


(%i5) assume(U_In>0);
(%o5)                      [U_In > 0]


(%i6) divider:U_Out=U_In*R_1/(R_1+R_2);
                                R_1 U_In
(%o6)                   U_Out = ---------
                                R_2 + R_1


(%i7) lhs(divider)=wc_mintypmax_rss(subst(vals,rhs(divider)),6);
(%o7) U_Out = [min = 0.49646446609406725 U_In, typ = 0.5 U_In, 
 max = 0.5035355339059328 U_In, Fail = 0.0019731752898266564 ppm]


(%i8) lhs(divider)=float(wc_mintypmax_rss_percent(subst(vals,rhs(divider)),6));
(%o8) U_Out = [min = - 0.7071067811865506 %, typ = 0.5 U_In, 
    max = 0.7071067811865506 %, Fail = 0.0019731752898266564 ppm]
```

See also: `wc_mintypmax_rss`.

### Function: wc_montecarlo (expression, num)

Introduces *num* random values per parameter into
*expression* and returns a list of the result.


See also `wc_005fsystematic`.


Example:











```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 2000.0*(1+tol[2]*.01)
 ];
(%o2) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 2000.0 (0.01 tol  + 1)]
                                                          2


(%i3) divider: U_Out=U_In*(R_1)/(R_1+R_2);
                                R_1 U_In
(%o3)                   U_Out = ---------
                                R_2 + R_1


(%i4) wc_montecarlo(subst(vals,rhs(divider)),10);
(%o4) [0.3301505377099377 U_In, 0.33276843198354916 U_In, 
0.33406203454153227 U_In, 0.33434833585190965 U_In, 
0.3341006856369802 U_In, 0.3359647531928058 U_In, 
0.32911646313213117 U_In, 0.333158315034511 U_In, 
0.3325173140803672 U_In, 0.3331108406798784 U_In]
```

See also: `wc_systematic`.

### Function: wc_systematic (expression, num)

Systematically introduces *num* values per parameter into *expression*
and returns a list of the result. If no *num* is given, *num* defaults
to *wc_defaultvaluespertol*. Negative values for *num* make
`wc_systematic` use the monte carlo method with *num* samples,
instead.


If an equation uses the following values with tolerances:


`vals:[R_1=100+tol[1],R_2=100+tol[2]];`


`num=2` will cause the following combinations of tolerances to be tested:
(Figure wrstcse_ewc_2)
`num=3` will cause the following combinations of tolerances to be tested:
(Figure wrstcse_ewc_3)
`num=-500` will cause the following combinations of tolerances to
be tested, instead:
(Figure wrstcse_montecarlo)


See also `wc_defaultvaluespertol`, `wc_mintypmax`,
`wc_defaultvaluespertol`,
`wc_ewc_simplify` and `wc_005fmontecarlo`.


Example:











```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 2000.0*(1+tol[2]*.01)
 ];
(%o2) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 2000.0 (0.01 tol  + 1)]
                                                          2


(%i3) divider: U_Out=U_In*(R_1)/(R_1+R_2);
                                R_1 U_In
(%o3)                   U_Out = ---------
                                R_2 + R_1


(%i4) wc_systematic(subst(vals,rhs(divider)));
(%o4) [0.33333333333333337 U_In, 0.3311036789297659 U_In, 
0.3289036544850498 U_In, 0.3355704697986577 U_In, 
0.3333333333333333 U_In, 0.33112582781456956 U_In, 
0.3377926421404682 U_In, 0.3355481727574751 U_In, 
0.3333333333333333 U_In]
```

See also: `wc_defaultvaluespertol`, `wc_mintypmax`, `wc_ewc_simplify`, `wc_montecarlo`.

### Function: wc_tolappend (list1, list2, ...)

Appends lists of parameters from independent sources making sure that
tolerances of all elements in one list will stay independent from all
elements in the others.


Works like append() in that it appends all values from all of its
arguments to make one big list. But this command, if one list
happens to contain a *tol[n]* with the same *n* as another
list, changes one of these *n* to a new value that makes
it independent from all tolerances from the other list.


See also `append`.


Example:















```maxima
maxima
(%i1) load("wrstcse")$

(%i2) val_a: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 1000.0*(1+tol[2]*.01)
 ];
(%o2) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 1000.0 (0.01 tol  + 1)]
                                                          2


(%i3) val_b: [
   R_3= 1000.0*(1+tol[1]*.01),
   R_4= 1000.0*(1+tol[4]*.01)
 ];
(%o3) [R_3 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_4 = 1000.0 (0.01 tol  + 1)]
                                                          4


(%i4) append(val_a,val_b);
(%o4) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
R_2 = 1000.0 (0.01 tol  + 1), R_3 = 1000.0 (0.01 tol  + 1), 
                      2                             1
R_4 = 1000.0 (0.01 tol  + 1)]
                      4


(%i5) wc_tolappend(val_a,val_b);
                            used = 1

(%o5) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
R_2 = 1000.0 (0.01 tol  + 1), R_3 = 1000.0 (0.01 tol  + 1), 
                      2                             5
R_4 = 1000.0 (0.01 tol  + 1)]
                      4
```

See also: `append`.

### Function: wc_tolassumptions (expr)

Adds the range of the *tol[n]* contained in *expr* to the assume
database.


See also `wc_inputvalueassumptions`, `wc_inputvalueranges` and `assume`.


Example:














```maxima
maxima

(%i1) load("wrstcse");
(%o1) /home/gunter/src/maxima-code/share/contrib/wrstcse.mac


(%i2) vals:[
    R_1=100*(1+1/100*tol["R1"])*(1+1/100*tol["Temp"]),
    R_2=200*(1+1/100*tol["R2"])*(1+1/100*tol["Temp"])];
                  tol         tol
                     R1          Temp
(%o2) [R_1 = 100 (----- + 1) (------- + 1), 
                   100          100
                                        tol         tol
                                           R2          Temp
                             R_2 = 200 (----- + 1) (------- + 1)]
                                         100          100


(%i3) float(wc_tolassumptions(%));
(%o3) [tol   >= - 1.0, tol   <= 1.0, tol     >= - 1.0, 
          R1              R1            Temp
                    tol     <= 1.0, tol   >= - 1.0, tol   <= 1.0]
                       Temp            R2              R2


(%i4) is(tol[R_1]>tol[R_2]);
(%o4)                        unknown


(%i5) is(tol[R_1]>1);
(%o5)                        unknown


(%i6) is(tol[R_1]<-1);
(%o6)                        unknown


(%i7) is(tol[R_1]<0);
(%o7)                        unknown


(%i8) is(tol[R_2]>2);
(%o8)                        unknown
```

See also: `wc_inputvalueassumptions`, `wc_inputvalueranges`, `assume`.

### Function: wc_typicalvalues (expression)

Returns what happens if all *tol[n]* happen to be 0, which moves
all parameter to the middle of their tolerance range.


Example:












```maxima
maxima
(%i1) load("wrstcse")$

(%i2) vals: [
   R_1= 1000.0*(1+tol[1]*.01),
   R_2= 2000.0*(1+tol[2]*.01)
 ];
(%o2) [R_1 = 1000.0 (0.01 tol  + 1), 
                             1
                                    R_2 = 2000.0 (0.01 tol  + 1)]
                                                          2


(%i3) divider:U_Out=U_In*R_1/(R_1+R_2);
                                R_1 U_In
(%o3)                   U_Out = ---------
                                R_2 + R_1


(%i4) wc_typicalvalues(vals);
(%o4)             [R_1 = 1000.0, R_2 = 2000.0]


(%i5) wc_typicalvalues(subst(vals,divider));
(%o5)            U_Out = 0.3333333333333333 U_In
```

### Variable: width

Default value: `500`


The width, in pixels, of the graphics window. *pixels* must be a
positive integer number.

### Function: wigner_3j (j1, j2, j3, m1, m2, m3)

Compute Wigner’s 3j symbol (computed in terms of a related
Clebsch-Gordan coefficient).

### Function: wigner_6j (j1, j2, j3, j4, j5, j6)

Compute Wigner’s 6j symbol.

### Function: wigner_9j (a, b, c, d, e, f, g, h, i, j)

Compute Wigner’s 9j symbol.

### Variable: windowname

Default value: `.scene`


*name* must be a string that can be used as the name of the Tk
window created by Xmaxima for the `scene` graphics. The default
value `.scene` implies that a new top level window will be created.

### Variable: windowtitle

Default value: `Xmaxima: scene`


*name* must be a string that will be written in the title of the
window created by `scene`.

### Variable: wireframe

Only the edges of the triangulation used to render the surface will be
shown. **Example**: `[cube, [wireframe]]`


See also `object_005fsurface` and
`object_005fpoints`.

See also: `object_surface`, `object_points`.

### Function: wronskian (f_1, ..., f_n, x)

Returns the Wronskian matrix of the list of expressions [*f_1*, ..., *f_n*] in the variable *x*.
The determinant of the Wronskian matrix is the Wronskian determinant of the list of expressions.


To use `wronskian`, first `load("functs")`. Example:







```maxima
(%i1) load ("functs")$

(%i2) wronskian([f(x), g(x)],x);
                    [   f(x)       g(x)    ]
                    [                      ]
(%o2)               [ d          d         ]
                    [ -- (f(x))  -- (g(x)) ]
                    [ dx         dx        ]
```

### Variable: xlength

Default value: `1`


The height of a cube in the x direction. *length* must be a positive
number. See also `object_005fylength` and
`object_005fzlength`.

See also: `object_ylength`, `object_zlength`.

### Variable: ylength

Default value: `1`


The height of a cube in the y direction. *length* must be a positive
number. See also `object_005fxlength` and
`object_005fzlength`.

See also: `object_xlength`, `object_zlength`.

### Variable: zlength

Default value: `1`


The height of a cube in z the direction. *length* must be a positive
 number.  See also `object_005fxlength` and
 `object_005fylength`.

See also: `object_xlength`, `object_ylength`.

