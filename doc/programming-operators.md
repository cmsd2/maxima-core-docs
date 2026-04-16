## Operators

### Function: ** ()

Exponentiation operator.
Maxima recognizes `**` as the same operator as `^` in input,
and it is displayed as `^` in 1-dimensional output,
or by placing the exponent as a superscript in 2-dimensional output.


The `fortran` function displays the exponentiation operator as `**`,
whether it was input as `**` or `^`.


Examples:









```maxima
maxima

(%i1) is (a**b = a^b);
(%o1)                         true


(%i2) x**y + x^z;
                              z    y
(%o2)                        x  + x


(%i3) string (x**y + x^z);
(%o3)                        x^z+x^y


(%i4) fortran (x**y + x^z);
      x**z+x**y
(%o4)                         done
```

See also: `^`, `fortran`.

### Function: + ()

The symbols `+` `*` `/` and `^` represent addition,
multiplication, division, and exponentiation, respectively.  The names of these
operators are `"+"` `"*"` `"/"` and `"^"`, which may appear
where the name of a function or operator is required.


The symbols `+` and `-` represent unary addition and negation,
respectively, and the names of these operators are `"+"` and `"-"`,
respectively.


Subtraction `a - b` is represented within Maxima as addition,
`a + (- b)`.  Expressions such as `a + (- b)` are displayed as
subtraction.  Maxima recognizes `"-"` only as the name of the unary
negation operator, and not as the name of the binary subtraction operator.


Division `a / b` is represented within Maxima as multiplication,
`a * b^(- 1)`.  Expressions such as `a * b^(- 1)` are displayed as
division.  Maxima recognizes `"/"` as the name of the division operator.


Addition and multiplication are n-ary, commutative operators.
Division and exponentiation are binary, noncommutative operators.


Maxima sorts the operands of commutative operators to construct a canonical
representation.  For internal storage, the ordering is determined by
`orderlessp`.  For display, the ordering for addition is determined by
`ordergreatp`, and for multiplication, it is the same as the internal
ordering.


Arithmetic computations are carried out on literal numbers (integers, rationals,
ordinary floats, and bigfloats).  Except for exponentiation, all arithmetic
operations on numbers are simplified to numbers.  Exponentiation is simplified
to a number if either operand is an ordinary float or bigfloat or if the result
is an exact integer or rational; otherwise an exponentiation may be simplified
to `sqrt` or another exponentiation or left unchanged.


Floating-point contagion applies to arithmetic computations: if any operand is
a bigfloat, the result is a bigfloat; otherwise, if any operand is an ordinary
float, the result is an ordinary float; otherwise, the operands are rationals
or integers and the result is a rational or integer.


Arithmetic computations are a simplification, not an evaluation.
Thus arithmetic is carried out in quoted (but simplified) expressions.


Arithmetic operations are applied element-by-element to lists when the global
flag `listarith` is `true`, and always applied element-by-element to
matrices.  When one operand is a list or matrix and another is an operand of
some other type, the other operand is combined with each of the elements of the
list or matrix.


Examples:


Addition and multiplication are n-ary, commutative operators.
Maxima sorts the operands to construct a canonical representation.
The names of these operators are `"+"` and `"*"`.











```maxima
maxima

(%i1) c + g + d + a + b + e + f;
(%o1)               g + f + e + d + c + b + a


(%i2) [op (%), args (%)];
(%o2)              [+, [g, f, e, d, c, b, a]]


(%i3) c * g * d * a * b * e * f;
(%o3)                     a b c d e f g


(%i4) [op (%), args (%)];
(%o4)              [*, [a, b, c, d, e, f, g]]


(%i5) apply ("+", [a, 8, x, 2, 9, x, x, a]);
(%o5)                    3 x + 2 a + 19


(%i6) apply ("*", [a, 8, x, 2, 9, x, x, a]);
                                 2  3
(%o6)                       144 a  x
```


Division and exponentiation are binary, noncommutative operators.
The names of these operators are `"/"` and `"^"`.








```maxima
maxima

(%i1) [a / b, a ^ b];
                              a   b
(%o1)                        [-, a ]
                              b


(%i2) [map (op, %), map (args, %)];
(%o2)              [[/, ^], [[a, b], [a, b]]]


(%i3) [apply ("/", [a, b]), apply ("^", [a, b])];
                              a   b
(%o3)                        [-, a ]
                              b
```


Subtraction and division are represented internally
in terms of addition and multiplication, respectively.







```maxima
maxima

(%i1) [inpart (a - b, 0), inpart (a - b, 1), inpart (a - b, 2)];
(%o1)                      [+, a, - b]


(%i2) [inpart (a / b, 0), inpart (a / b, 1), inpart (a / b, 2)];
                                   1
(%o2)                       [*, a, -]
                                   b
```


Computations are carried out on literal numbers.
Floating-point contagion applies.







```maxima
maxima

(%i1) 17 + b - (1/2)*29 + 11^(2/4);
                                       5
(%o1)                   b + sqrt(11) + -
                                       2


(%i2) [17 + 29, 17 + 29.0, 17 + 29b0];
(%o2)                   [46, 46.0, 4.6b1]
```


Arithmetic computations are a simplification, not an evaluation.









```maxima
maxima

(%i1) simp : false;
(%o1)                         false


(%i2) '(17 + 29*11/7 - 5^3);
                              29 11    3
(%o2)                    17 + ----- - 5
                                7


(%i3) simp : true;
(%o3)                         true


(%i4) '(17 + 29*11/7 - 5^3);
                                437
(%o4)                         - ---
                                 7
```


Arithmetic is carried out element-by-element for lists (depending on
`listarith`) and matrices.













```maxima
maxima

(%i1) matrix ([a, x], [h, u]) - matrix ([1, 2], [3, 4]);
                        [ a - 1  x - 2 ]
(%o1)                   [              ]
                        [ h - 3  u - 4 ]


(%i2) 5 * matrix ([a, x], [h, u]);
                          [ 5 a  5 x ]
(%o2)                     [          ]
                          [ 5 h  5 u ]


(%i3) listarith : false;
(%o3)                         false


(%i4) [a, c, m, t] / [1, 7, 2, 9];
                          [a, c, m, t]
(%o4)                     ------------
                          [1, 7, 2, 9]


(%i5) [a, c, m, t] ^ x;
                                      x
(%o5)                     [a, c, m, t]


(%i6) listarith : true;
(%o6)                         true


(%i7) [a, c, m, t] / [1, 7, 2, 9];
                              c  m  t
(%o7)                     [a, -, -, -]
                              7  2  9


(%i8) [a, c, m, t] ^ x;
                          x   x   x   x
(%o8)                   [a , c , m , t ]
```

See also: `orderlessp`, `ordergreatp`, `sqrt`, `listarith`.

### Function: . ()

The dot operator, for matrix (non-commutative) multiplication.
When `"."` is used in this way, spaces should be left on both sides of
it, e.g.  `A . B`  This distinguishes it plainly from a decimal point in
a floating point number.


See also
`Dot`,
`dot0nscsimp`,
`dot0simp`,
`dot1simp`,
`dotassoc`,
`dotconstrules`,
`dotdistrib`,
`dotexptsimp`,
`dotident`,
and
`dotscrules`.

See also: `Dot`, `dot0nscsimp`, `dot0simp`, `dot1simp`, `dotassoc`, `dotconstrules`, `dotdistrib`, `dotexptsimp`, `dotident`, `dotscrules`.

### Function: : ()

Assignment operator.


When the left-hand side is a simple variable (not subscripted), `:`
evaluates its right-hand side and associates that value with the left-hand side.


When the left-hand side is a subscripted element of a list, matrix, declared
Maxima array, or Lisp array, the right-hand side is assigned to that element.
The subscript must name an existing element; such objects cannot be extended by
naming nonexistent elements.


When the left-hand side is a subscripted element of a `hashed array`,
the right-hand side is assigned to that element, if it already exists,
or a new element is allocated, if it does not already exist.


When the left-hand side is a list of simple and/or subscripted variables, the
right-hand side must evaluate to a list, and the elements of the right-hand
side are assigned to the elements of the left-hand side, in parallel.


See also `kill` and `remvalue`, which undo the association between
the left-hand side and its value.


Examples:


Assignment to a simple variable.








```maxima
maxima

(%i1) a;
(%o1)                           a


(%i2) a : 123;
(%o2)                          123


(%i3) a;
(%o3)                          123
```


Assignment to an element of a list.








```maxima
maxima

(%i1) b : [1, 2, 3];
(%o1)                       [1, 2, 3]


(%i2) b[3] : 456;
(%o2)                          456


(%i3) b;
(%o3)                      [1, 2, 456]
```


Assignment to a variable that neither is the name of a list nor of an array
creates a `hashed-array`.










```maxima
maxima

(%i1) c[99] : 789;
(%o1)                          789


(%i2) c[99];
(%o2)                          789


(%i3) c;
(%o3)                           c


(%i4) arrayinfo (c);
(%o4)                   [hashed, 1, [99]]


(%i5) listarray (c);
(%o5)                         [789]
```


Multiple assignment.









```maxima
maxima

(%i1) [a, b, c] : [45, 67, 89];
(%o1)                     [45, 67, 89]


(%i2) a;
(%o2)                          45


(%i3) b;
(%o3)                          67


(%i4) c;
(%o4)                          89
```


Multiple assignment is carried out in parallel.
The values of `a` and `b` are exchanged in this example.









```maxima
maxima

(%i1) [a, b] : [33, 55];
(%o1)                       [33, 55]


(%i2) [a, b] : [b, a];
(%o2)                       [55, 33]


(%i3) a;
(%o3)                          55


(%i4) b;
(%o4)                          33
```

See also: `hashed-array`, `kill`, `remvalue`.

### Function: :: ()

Assignment operator.


`::` is the same as `:` (which see) except that `::` evaluates
its left-hand side as well as its right-hand side.


Examples:













```maxima
maxima

(%i1) x : 'foo;
(%o1)                          foo


(%i2) x :: 123;
(%o2)                          123


(%i3) foo;
(%o3)                          123


(%i4) x : '[a, b, c];
(%o4)                       [a, b, c]


(%i5) x :: [11, 22, 33];
(%o5)                     [11, 22, 33]


(%i6) a;
(%o6)                          11


(%i7) b;
(%o7)                          22


(%i8) c;
(%o8)                          33
```

See also: `:`.

### Function: ::= ()

Macro function definition operator.
`::=` defines a function (called a "macro" for historical reasons) which
quotes its arguments, and the expression which it returns (called the "macro
expansion") is evaluated in the context from which the macro was called.
A macro function is otherwise the same as an ordinary function.


`macroexpand` returns a macro expansion (without evaluating it).
`macroexpand (foo (x))` followed by `''%` is equivalent to
`foo (x)` when `foo` is a macro function.


`::=` puts the name of the new macro function onto the global list
`macros`.  `kill`, `remove`, and `remfunction`
unbind macro function definitions and remove names from `macros`.


`fundef` or `dispfun` return a macro function definition or assign it
to a label, respectively.


Macro functions commonly contain `buildq` and `splice` expressions to
construct an expression, which is then evaluated.


Examples


A macro function quotes its arguments, so message (1) shows `y - z`, not
the value of `y - z`.  The macro expansion (the quoted expression
`'(print ("(2) x is equal to", x))`) is evaluated in the context from which
the macro was called, printing message (2).











```maxima
maxima
(%i1) x: %pi$
(%i2) y: 1234$
(%i3) z: 1729 * w$

(%i4) printq1 (x) ::= block (print ("(1) x is equal to", x),
                                '(print ("(2) x is equal to", x)))$


(%i5) printq1 (y - z);
(1) x is equal to y - z 
(2) x is equal to %pi 
(%o5)                          %pi
```


An ordinary function evaluates its arguments, so message (1) shows the value of
`y - z`.  The return value is not evaluated, so message (2) is not printed
until the explicit evaluation `''%`.












```maxima
maxima
(%i1) x: %pi$
(%i2) y: 1234$
(%i3) z: 1729 * w$

(%i4) printe1 (x) := block (print ("(1) x is equal to", x),
      '(print ("(2) x is equal to", x)))$


(%i5) printe1 (y - z);
(1) x is equal to 1234 - 1729 w 
(%o5)              print((2) x is equal to, x)


(%i6) ''%;
(2) x is equal to %pi 
(%o6)                          %pi
```


`macroexpand` returns a macro expansion.
`macroexpand (foo (x))` followed by `''%` is equivalent to
`foo (x)` when `foo` is a macro function.












```maxima
maxima
(%i1) x: %pi$
(%i2) y: 1234$
(%i3) z: 1729 * w$
(%i4) g (x) ::= buildq ([x], print ("x is equal to", x))$

(%i5) macroexpand (g (y - z));
(%o5)              print(x is equal to, y - z)


(%i6) ''%;
x is equal to 1234 - 1729 w 
(%o6)                     1234 - 1729 w


(%i7) g (y - z);
x is equal to 1234 - 1729 w 
(%o7)                     1234 - 1729 w
```

See also: `macroexpand`, `macros`, `kill`, `remove`, `remfunction`, `fundef`, `dispfun`, `buildq`, `splice`.

### Function: := ()

The function definition operator.


`f(x_1, ..., x_n) := expr` defines a function named
*f* with arguments *x_1*, ..., *x_n* and function body
*expr*.  `:=` never evaluates the function body (unless explicitly
evaluated by quote-quote `''`).
The function body is evaluated every time the function is called.


`f[x_1, ..., x_n] := expr` defines a so-called
`memoizing-function`.
Its function body is evaluated just once for each distinct value of its arguments,
and that value is returned, without evaluating the function body,
whenever the arguments have those values again.
(A function of this kind is also known as a “array function”.)


`f[x_1, ..., x_n](y_1, ..., y_m) := expr`
is a special case of a `memoizing-function`.
`f[x_1, ..., x_n]` is a `memoizing function` which returns a lambda expression
with arguments `y_1, ..., y_m`.
The function body is evaluated once for each distinct value of `x_1, ..., x_n`,
and the body of the lambda expression is that value.


When the last or only function argument *x_n* is a list of one element, the
function defined by `:=` accepts a variable number of arguments.  Actual
arguments are assigned one-to-one to formal arguments *x_1*, ...,
*x_(n - 1)*, and any further actual arguments, if present, are assigned to
*x_n* as a list.


All function definitions appear in the same namespace; defining a function
`f` within another function `g` does not automatically limit the scope
of `f` to `g`.  However, `local(f)` makes the definition of
function `f` effective only within the block or other compound expression
in which `local` appears.


If some formal argument *x_k* is a quoted symbol, the function defined by
`:=` does not evaluate the corresponding actual argument.  Otherwise all
actual arguments are evaluated.


See also `define` and `_003a_003a_003d`.


Examples:


`:=` never evaluates the function body (unless explicitly evaluated by
quote-quote).










```maxima
maxima

(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)


(%i2) F1 (x, y) := expr;
(%o2)                   F1(x, y) := expr


(%i3) F1 (a, b);
(%o3)                    cos(y) - sin(x)


(%i4) F2 (x, y) := ''expr;
(%o4)              F2(x, y) := cos(y) - sin(x)


(%i5) F2 (a, b);
(%o5)                    cos(b) - sin(a)
```


`f(x_1, ..., x_n) := ...` defines an ordinary function.









```maxima
maxima

(%i1) G1(x, y) := (print ("Evaluating G1 for x=", x, "and y=", y),
 x.y - y.x);
(%o1) G1(x, y) := (print("Evaluating G1 for x=", x, "and y=", 
                                               y), x . y - y . x)


(%i2) G1([1, a], [2, b]);
Evaluating G1 for x= [1, a] and y= [2, b] 
(%o2)                           0


(%i3) G1([1, a], [2, b]);
Evaluating G1 for x= [1, a] and y= [2, b] 
(%o3)                           0
```


`f[x_1, ..., x_n] := ...` defines a `memoizing-function`.











```maxima
maxima

(%i1) G2[a] := (print ("Evaluating G2 for a=", a), a^2);
                                                     2
(%o1)     G2  := (print("Evaluating G2 for a=", a), a )
            a


(%i2) G2[1234];
Evaluating G2 for a= 1234 
(%o2)                        1522756


(%i3) G2[1234];
(%o3)                        1522756


(%i4) G2[2345];
Evaluating G2 for a= 2345 
(%o4)                        5499025


(%i5) arrayinfo (G2);
(%o5)              [hashed, 1, [1234], [2345]]


(%i6) listarray (G2);
(%o6)                  [1522756, 5499025]
```


`f[x_1, ..., x_n](y_1, ..., y_m) := expr`
is a special case of a `memoizing-function`.












```maxima
maxima

(%i1) G3[n](x) := (print ("Evaluating G3 for n=", n), diff (sin(x)^2,
 x, n));
(%o1) G3 (x) := (print("Evaluating G3 for n=", n), 
        n
                                                     2
                                             diff(sin (x), x, n))


(%i2) G3[2];
Evaluating G3 for n= 2 
                                2           2
(%o2)          lambda([x], 2 cos (x) - 2 sin (x))


(%i3) G3[2];
                                2           2
(%o3)          lambda([x], 2 cos (x) - 2 sin (x))


(%i4) G3[2](1);
                           2           2
(%o4)                 2 cos (1) - 2 sin (1)


(%i5) arrayinfo (G3);
(%o5)                   [hashed, 1, [2]]


(%i6) listarray (G3);
                                2           2
(%o6)         [lambda([x], 2 cos (x) - 2 sin (x))]
```


When the last or only function argument *x_n* is a list of one element,
the function defined by `:=` accepts a variable number of arguments.







```maxima
maxima

(%i1) H ([L]) := apply ("+", L);
(%o1)                H([L]) := apply("+", L)


(%i2) H (a, b, c);
(%o2)                       c + b + a
```


`local` makes a local function definition.









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

See also: `memoizing-function`, `local`, `define`, `::=`.

### Function: < ()

The symbols `<` `<=` `>=` and `>` represent less than, less
than or equal, greater than or equal, and greater than, respectively.  The names
of these operators are `"<"` `"<="` `">="` and `">"`, which
may appear where the name of a function or operator is required.


These relational operators are all binary operators; constructs such as
`a < b < c` are not recognized by Maxima.


Relational expressions are evaluated to Boolean values by the functions
`is` and `maybe`, and the programming constructs
`if`, `while`, and `unless`.  Relational expressions
are not otherwise evaluated or simplified to Boolean values, although the
arguments of relational expressions are evaluated (when evaluation is not
otherwise prevented by quotation).


When a relational expression cannot be evaluated to `true` or `false`,
the behavior of `is` and `if` are governed by the global flag
`prederror`.  When `prederror` is `true`, `is` and
`if` trigger an error.  When `prederror` is `false`, `is`
returns `unknown`, and `if` returns a partially-evaluated conditional
expression.


`maybe` always behaves as if `prederror` were `false`, and
`while` and `unless` always behave as if `prederror` were
`true`.


Relational operators do not distribute over lists or other aggregates.


See also `=`, `#`, `equal`, and `notequal`.


Examples:


Relational expressions are evaluated to Boolean values by some functions and
programming constructs.











```maxima
maxima

(%i1) [x, y, z] : [123, 456, 789];
(%o1)                    [123, 456, 789]


(%i2) is (x < y);
(%o2)                         true


(%i3) maybe (y > z);
(%o3)                         false


(%i4) if x >= z then 1 else 0;
(%o4)                           0


(%i5) block ([S], S : 0, for i:1 while i <= 100 do S : S + i,
       return (S));
(%o5)                         5050
```


Relational expressions are not otherwise evaluated or simplified to Boolean
values, although the arguments of relational expressions are evaluated.








```maxima
maxima

(%i1) [x, y, z] : [123, 456, 789];
(%o1)                    [123, 456, 789]


(%i2) [x < y, y <= z, z >= y, y > z];
(%o2)    [123 < 456, 456 <= 789, 789 >= 456, 456 > 789]


(%i3) map (is, %);
(%o3)               [true, true, true, false]
```

See also: `is`, `maybe`, `if`, `while`, `unless`, `prederror`, `=`, `#`, `equal`, `notequal`.

### Function: ^^ ()

Noncommutative exponentiation operator.
`^^` is the exponentiation operator corresponding to noncommutative
multiplication `.`, just as the ordinary exponentiation operator `^`
corresponds to commutative multiplication `*`.


Noncommutative exponentiation is displayed by `^^` in 1-dimensional output,
and by placing the exponent as a superscript within angle brackets `< >`
in 2-dimensional output.


Examples:







```maxima
maxima

(%i1) a . a . b . b . b + a * a * a * b * b;
                        3  2    <2>    <3>
(%o1)                  a  b  + a    . b


(%i2) string (a . a . b . b . b + a * a * a * b * b);
(%o2)                  a^3*b^2+a^^2 . b^^3
```

### Function: and ()

The logical conjunction operator.  `and` is an n-ary infix operator;
its operands are Boolean expressions, and its result is a Boolean value.


`and` forces evaluation (like `is`) of one or more operands,
and may force evaluation of all operands.


Operands are evaluated in the order in which they appear.  `and` evaluates
only as many of its operands as necessary to determine the result.  If any
operand is `false`, the result is `false` and no further operands are
evaluated.


The global flag `prederror` governs the behavior of `and` when an
evaluated operand cannot be determined to be `true` or `false`.
`and` prints an error message when `prederror` is `true`.
Otherwise, operands which do not evaluate to `true` or `false` are
accepted, and the result is a Boolean expression.


`and` is not commutative: `a and b` might not be equal to
`b and a` due to the treatment of indeterminate operands.

See also: `is`, `prederror`.

### Function: infix (infix, op, infix, op, lbp, rbp, infix, op, lbp, rbp, lpos, rpos, pos)

Declares *op* to be an infix operator.  An infix operator is a function of
two arguments, with the name of the function written between the arguments.
For example, the subtraction operator `-` is an infix operator.


`infix (op)` declares *op* to be an infix operator with default
binding powers (left and right both equal to 180) and parts of speech (left and
right both equal to `any`).



`infix (op, lbp, rbp)` declares *op* to be an infix
operator with stated left and right binding powers and default parts of speech
(left and right both equal to `any`).


`infix (op, lbp, rbp, lpos, rpos, pos)`
declares *op* to be an infix operator with stated left and right binding
powers and parts of speech *lpos*, *rpos*, and *pos* for the left
operand, the right operand, and the operator result, respectively.


"Part of speech", in reference to operator declarations, means expression type.
Three types are recognized: `expr`, `clause`, and `any`,
indicating an algebraic expression, a Boolean expression, or any kind of
expression, respectively.  Maxima can detect some syntax errors by comparing the
declared part of speech to an actual expression.


The precedence of *op* with respect to other operators derives from the left
and right binding powers of the operators in question.  If the left and right
binding powers of *op* are both greater the left and right binding powers of
some other operator, then *op* takes precedence over the other operator.
If the binding powers are not both greater or less, some more complicated
relation holds.


The associativity of *op* depends on its binding powers.  Greater left
binding power (*lbp*) implies an instance of *op* is evaluated before
other operators to its left in an expression, while greater right binding power
(*rbp*) implies  an instance of *op* is evaluated before other operators
to its right in an expression.  Thus greater *lbp* makes *op*
right-associative, while greater *rbp* makes *op* left-associative.
If *lbp* is equal to *rbp*, *op* is left-associative.


See also `Introduction-to-operators`.


Examples:


If the left and right binding powers of *op* are both greater
the left and right binding powers of some other operator,
then *op* takes precedence over the other operator.












```maxima
maxima

(%i1) :lisp (get '$+ 'lbp)
100


(%i1) :lisp (get '$+ 'rbp)
134


(%i1) infix ("##", 101, 101);
(%o1)                          ##


(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")");
(%o2)       (a ## b) := sconcat("(", a, ",", b, ")")


(%i3) 1 + a ## b + 2;
(%o3)                       (a,b) + 3


(%i4) infix ("##", 99, 99);
(%o4)                          ##


(%i5) 1 + a ## b + 2;
(%o5)                       (a+1,b+2)
```


Greater *lbp* makes *op* right-associative,
while greater *rbp* makes *op* left-associative.










```maxima
maxima

(%i1) infix ("##", 100, 99);
(%o1)                          ##

(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")")$

(%i3) foo ## bar ## baz;
(%o3)                    (foo,(bar,baz))


(%i4) infix ("##", 100, 101);
(%o4)                          ##


(%i5) foo ## bar ## baz;
(%o5)                    ((foo,bar),baz)
```


Maxima can detect some syntax errors by comparing the
declared part of speech to an actual expression.








incorrect syntax: Found ALGEBRAIC expression where LOGICAL expression expected
if x ## y then 
             ^


```maxima
maxima

(%i1) infix ("##", 100, 99, expr, expr, expr);
(%o1)                          ##

(%i2) if x ## y then 1 else 0;

(%i2) infix ("##", 100, 99, expr, expr, clause);
(%o2)                          ##


(%i3) if x ## y then 1 else 0;
(%o3)                if x ## y then 1 else 0
```

See also: `Introduction-to-operators`.

### Function: matchfix (matchfix, ldelimiter, rdelimiter, matchfix, ldelimiter, rdelimiter, arg_pos, pos)

Declares a matchfix operator with left and right delimiters *ldelimiter*
and *rdelimiter*.  The delimiters are specified as strings.


A "matchfix" operator is a function of any number of arguments,
such that the arguments occur between matching left and right delimiters.
The delimiters may be any strings, so long as the parser can
distinguish the delimiters from the operands 
and other expressions and operators.
In practice this rules out unparseable delimiters such as
`%`, `,`, `$` and `;`, 
and may require isolating the delimiters with white space.
The right delimiter can be the same or different from the left delimiter.


A left delimiter can be associated with only one right delimiter;
two different matchfix operators cannot have the same left delimiter.


An existing operator may be redeclared as a matchfix operator
without changing its other properties.
In particular, built-in operators such as addition `+` can
be declared matchfix,
but operator functions cannot be defined for built-in operators.


The command `matchfix (ldelimiter, rdelimiter, arg_pos, pos)` declares the argument part-of-speech *arg_pos* and result
part-of-speech *pos*, and the delimiters *ldelimiter* and
*rdelimiter*.


"Part of speech", in reference to operator declarations, means expression type.
Three types are recognized: `expr`, `clause`, and `any`,
indicating an algebraic expression, a Boolean expression, or any kind of
expression, respectively.
Maxima can detect some syntax errors by comparing the
declared part of speech to an actual expression.









The function to carry out a matchfix operation is an ordinary
user-defined function.
The operator function is defined
in the usual way
with the function definition operator `:=` or `define`.
The arguments may be written between the delimiters,
or with the left delimiter as a quoted string and the arguments
following in parentheses.
`dispfun (ldelimiter)` displays the function definition.


The only built-in matchfix operator is the list constructor `[ ]`.
Parentheses `( )` and double-quotes `" "` 
act like matchfix operators,
but are not treated as such by the Maxima parser.


`matchfix` evaluates its arguments.
`matchfix` returns its first argument, *ldelimiter*.



Examples:


Delimiters may be almost any strings.












```maxima
maxima

(%i1) matchfix ("@@", "~");
(%o1)                          @@


(%i2) @@ a, b, c ~;
(%o2)                      @@a, b, c~


(%i3) matchfix (">>", "<<");
(%o3)                          >>


(%i4) >> a, b, c <<;
(%o4)                      >>a, b, c<<


(%i5) matchfix ("foo", "oof");
(%o5)                          foo


(%i6) foo a, b, c oof;
(%o6)                     fooa, b, coof


(%i7) >> w + foo x, y oof + z << / @@ p, q ~;
                     >>z + foox, yoof + w<<
(%o7)                ----------------------
                            @@p, q~
```


Matchfix operators are ordinary user-defined functions.



```maxima
(%i1) matchfix ("!-", "-!");
(%o1)                         "!-"
(%i2) !- x, y -! := x/y - y/x;
                                    x   y
(%o2)                   !-x, y-! := - - -
                                    y   x
(%i3) define (!-x, y-!, x/y - y/x);
                                    x   y
(%o3)                   !-x, y-! := - - -
                                    y   x
(%i4) define ("!-" (x, y), x/y - y/x);
                                    x   y
(%o4)                   !-x, y-! := - - -
                                    y   x
(%i5) dispfun ("!-");
                                    x   y
(%t5)                   !-x, y-! := - - -
                                    y   x

(%o5)                         done
(%i6) !-3, 5-!;
                                16
(%o6)                         - --
                                15
(%i7) "!-" (3, 5);
                                16
(%o7)                         - --
                                15
```

### Function: nary (nary, op, nary, op, bp, arg_pos, pos)

An `nary` operator is used to denote a function of any number of arguments,
each of which is separated by an occurrence of the operator, e.g.  A+B or A+B+C.
The `nary("x")` function is a syntax extension function to declare `x`
to be an `nary` operator.  Functions may be declared to be `nary`.  If
`declare(j,nary);` is done, this tells the simplifier to simplify, e.g.
`j(j(a,b),j(c,d))` to `j(a, b, c, d)`.


See also `Introduction-to-operators`.

See also: `Introduction-to-operators`.

### Function: nofix (nofix, op, nofix, op, pos)

`nofix` operators are used to denote functions of no arguments.
The mere presence of such an operator in a command will cause the
corresponding function to be evaluated.  For example, when one types
"exit;" to exit from a Maxima break, "exit" is behaving similar to a
`nofix` operator.  The function `nofix("x")` is a syntax extension
function which declares `x` to be a `nofix` operator.


See also `Introduction-to-operators`.

See also: `Introduction-to-operators`.

### Function: not ()

The logical negation operator.  `not` is a prefix operator;
its operand is a Boolean expression, and its result is a Boolean value.


`not` forces evaluation (like `is`) of its operand.


The global flag `prederror` governs the behavior of `not` when its
operand cannot be determined to be `true` or `false`.  `not`
prints an error message when `prederror` is `true`.  Otherwise,
operands which do not evaluate to `true` or `false` are accepted,
and the result is a Boolean expression.

See also: `prederror`.

### Function: or ()

The logical disjunction operator.  `or` is an n-ary infix operator;
its operands are Boolean expressions, and its result is a Boolean value.


`or` forces evaluation (like `is`) of one or more operands,
and may force evaluation of all operands.


Operands are evaluated in the order in which they appear.  `or` evaluates
only as many of its operands as necessary to determine the result.  If any
operand is `true`, the result is `true` and no further operands are
evaluated.


The global flag `prederror` governs the behavior of `or` when an
evaluated operand cannot be determined to be `true` or `false`.
`or` prints an error message when `prederror` is `true`.
Otherwise, operands which do not evaluate to `true` or `false` are
accepted, and the result is a Boolean expression.


`or` is not commutative: `a or b` might not be equal to `b or a`
due to the treatment of indeterminate operands.

See also: `is`, `prederror`.

### Function: postfix (postfix, op, postfix, op, lbp, lpos, pos)

`postfix` operators like the `prefix` variety denote functions of a
single argument, but in this case the argument immediately precedes an
occurrence of the operator in the input string, e.g. 3!.  The
`postfix("x")` function is a syntax extension function to declare `x`
to be a `postfix` operator.


See also `Introduction-to-operators`.

See also: `Introduction-to-operators`.

### Function: prefix (prefix, op, prefix, op, rbp, rpos, pos)

A `prefix` operator is one which signifies a function of one argument,
which argument immediately follows an occurrence of the operator.
`prefix("x")` is a syntax extension function to declare `x` to be a
`prefix` operator.


See also `Introduction-to-operators`.

See also: `Introduction-to-operators`.

