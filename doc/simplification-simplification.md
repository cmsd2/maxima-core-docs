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

