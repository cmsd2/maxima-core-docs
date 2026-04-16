## Elementary Functions

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

### Function: plog (x)

Represents the principal branch of the complex-valued natural
logarithm with `-%pi < carg(x) <= +%pi` .

### Function: sqrt (x)

The square root of *x*.  It is represented internally by
`x^(1/2)`.  See also `rootscontract` and `radexpand`.

See also: `rootscontract`, `radexpand`.

