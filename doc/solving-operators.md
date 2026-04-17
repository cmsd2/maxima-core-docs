## Operators

<!-- category: Solving -->
<!-- keywords: # -->
<!-- signatures: # -->
### Function: #

Represents the negation of syntactic equality `_003d`.


Note that because of the rules for evaluation of predicate expressions
(in particular because `not expr` causes evaluation of *expr*),
`not a = b` is equivalent to `is(a # b)`,
instead of `a # b`.


Examples:











```maxima
maxima

(%i1) a = b;
(%o1)                         a = b


(%i2) is (a = b);
(%o2)                         false


(%i3) a # b;
(%o3)                         a # b


(%i4) not a = b;
(%o4)                         true


(%i5) is (a # b);
(%o5)                         true


(%i6) is (not a = b);
(%o6)                         true
```

See also: `=`.

<!-- category: Solving -->
<!-- keywords: = -->
<!-- signatures: = -->
### Function: =

The equation operator.


An expression `a = b`, by itself, represents an unevaluated
equation, which might or might not hold.  Unevaluated equations may appear as
arguments to `solve` and `algsys` or some other functions.


The function `is` evaluates `=` to a Boolean value.
`is(a = b)` evaluates `a = b` to `true`
when *a* and *b* are identical.  That is, *a* and *b* are atoms
which are identical, or they are not atoms and their operators are identical and
their arguments are identical.  Otherwise, `is(a = b)`
evaluates to `false`; it never evaluates to `unknown`.  When
`is(a = b)` is `true`, *a* and *b* are said to be
syntactically equal, in contrast to equivalent expressions, for which
`is(equal(a, b))` is `true`.  Expressions can be
equivalent and not syntactically equal.


The negation of `=` is represented by `_0023`.
As with `=`, an expression `a # b`, by itself, is not
evaluated.  `is(a # b)` evaluates `a # b` to
`true` or `false`.


In addition to `is`, some other operators evaluate `=` and `#`
to `true` or `false`, namely `if`, `and`,
`or`, and `not`.


Note that because of the rules for evaluation of predicate expressions
(in particular because `not expr` causes evaluation of *expr*),
`not a = b` is equivalent to `is(a # b)`,
instead of `a # b`.


`rhs` and `lhs` return the right-hand and left-hand sides,
respectively, of an equation or inequation.


See also `equal` and `notequal`.


Examples:


An expression `a = b`, by itself, represents
an unevaluated equation, which might or might not hold.










```maxima
maxima

(%i1) eq_1 : a * x - 5 * y = 17;
(%o1)                    a x - 5 y = 17


(%i2) eq_2 : b * x + 3 * y = 29;
(%o2)                    3 y + b x = 29


(%i3) solve ([eq_1, eq_2], [x, y]);
                        196         29 a - 17 b
(%o3)          [[x = ---------, y = -----------]]
                     5 b + 3 a       5 b + 3 a


(%i4) subst (%, [eq_1, eq_2]);
         196 a     5 (29 a - 17 b)
(%o4) [--------- - --------------- = 17, 
       5 b + 3 a      5 b + 3 a
                                  196 b     3 (29 a - 17 b)
                                --------- + --------------- = 29]
                                5 b + 3 a      5 b + 3 a


(%i5) ratsimp (%);
(%o5)                  [17 = 17, 29 = 29]
```


`is(a = b)` evaluates `a = b` to `true`
when *a* and *b* are syntactically equal (that is, identical).
Expressions can be equivalent and not syntactically equal.









```maxima
maxima

(%i1) a : (x + 1) * (x - 1);
(%o1)                    (x - 1) (x + 1)


(%i2) b : x^2 - 1;
                              2
(%o2)                        x  - 1


(%i3) [is (a = b), is (a # b)];
(%o3)                     [false, true]


(%i4) [is (equal (a, b)), is (notequal (a, b))];
(%o4)                     [true, false]
```


Some operators evaluate `=` and `#` to `true` or `false`.










```maxima
maxima

(%i1) if expand ((x + y)^2) = x^2 + 2 * x * y + y^2 then FOO else
      BAR;
(%o1)                          FOO


(%i2) eq_3 : 2 * x = 3 * x;
(%o2)                       2 x = 3 x


(%i3) eq_4 : exp (2) = %e^2;
                              2     2
(%o3)                       %e  = %e


(%i4) [eq_3 and eq_4, eq_3 or eq_4, not eq_3];
(%o4)                  [false, true, true]
```


Because `not expr` causes evaluation of *expr*,
`not a = b` is equivalent to `is(a # b)`.







```maxima
maxima

(%i1) [2 * x # 3 * x, not (2 * x = 3 * x)];
(%o1)                   [2 x # 3 x, true]


(%i2) is (2 * x # 3 * x);
(%o2)                         true
```

See also: `solve`, `algsys`, `is`, `#`, `if`, `and`, `or`, `not`, `rhs`, `lhs`, `equal`, `notequal`.

