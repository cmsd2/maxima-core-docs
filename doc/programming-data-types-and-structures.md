## Data Types and Structures

### Variable: %catalan

`%catalan` represents Catalan’s constant, $G$, defined by

$$G = \sum_{n=0}^\infty {(-1)^n\over (2n+1)^2}$$


$$G = \sum_{n=0}^\infty {(-1)^n\over (2n+1)^2}$$



(It is also sometimes denoted by $C$).


The numeric value of `%catalan` is approximately
0.915965594177219.  (See [https://dlmf.nist.gov/25.11.E40DLMF 25.11.E40]()).

### Variable: %e

`%e` represents the base of the natural logarithm, also known as Euler’s
number.  The numeric value of `%e` is the double-precision floating-point
value 2.718281828459045d0.  (See [https://personal.math.ubc.ca/~cbm/aands/page_67.htmA&S eqn 4.1.16](), [https://personal.math.ubc.ca/~cbm/aands/page_67.htmA&S 4.1.17]().)

### Variable: %gamma

The Euler-Mascheroni constant, 0.5772156649015329.... It is defined by ([https://personal.math.ubc.ca/~cbm/aands/page_255.htmA&S eqn 6.1.3]() and [https://dlmf.nist.gov/5.2.iiDLMF 5.2.ii]())

$$\gamma = \lim_{n \rightarrow \infty} \left(\sum_{k=1}^n {1\over k} - \log n\right)$$


$$\gamma = \lim_{n \rightarrow \infty} \left(\sum_{k=1}^n {1\over k} - \log n\right)$$

### Variable: %i

`%i` represents the imaginary unit, 
$\sqrt{-1}.$

### Variable: %phi

`%phi` represents the so-called *golden mean*, 
$(1+\sqrt{5})/2.$
The numeric value of `%phi` is the double-precision floating-point value
1.618033988749895d0.


`fibtophi` expresses Fibonacci numbers `fib(n)` in terms of
`%phi`.


By default, Maxima does not know the algebraic properties of `%phi`.
After evaluating `tellrat(%phi^2 - %phi - 1)` and `algebraic: true`,
`ratsimp` can simplify some expressions containing `%phi`.


Examples:


`fibtophi` expresses Fibonacci numbers `fib(n)` in terms of `%phi`.









```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1


(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)


(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1


(%i4) ratsimp (%);
(%o4)                           0
```


By default, Maxima does not know the algebraic properties of `%phi`.
After evaluating `tellrat (%phi^2 - %phi - 1)` and `algebraic: true`,
`ratsimp` can simplify some expressions containing `%phi`.










```maxima
(%i1) e : expand ((%phi^2 - %phi - 1) * (A + 1));
                 2                      2
(%o1)        %phi  A - %phi A - A + %phi  - %phi - 1


(%i2) ratsimp (e);
                  2                     2
(%o2)        (%phi  - %phi - 1) A + %phi  - %phi - 1


(%i3) tellrat (%phi^2 - %phi - 1);
                            2
(%o3)                  [%phi  - %phi - 1]


(%i4) algebraic : true;
(%o4)                         true


(%i5) ratsimp (e);
(%o5)                           0
```

See also: `fibtophi`, `ratsimp`.

### Variable: %pi

`%pi` represents the ratio of the perimeter of a circle to its diameter.
The numeric value of `%pi` is the double-precision floating-point value
3.141592653589793d0.

### Function: @ ()

`@` is the structure field access operator.
The expression `x@ a` refers to the value of field *a* of the structure instance *x*.
The field name is not evaluated.


If the field *a* in *x* has not been assigned a value,
`x@ a` evaluates to itself.


`kill(x@ a)` removes the value of field *a* in *x*.


Examples:













```maxima
(%i1) defstruct (foo (x, y, z));
(%o1)                    [foo(x, y, z)]
(%i2) u : new (foo (123, a - b, %pi));
(%o2)           foo(x = 123, y = a - b, z = %pi)
(%i3) u@z;
(%o3)                          %pi
(%i4) u@z : %e;
(%o4)                          %e
(%i5) u;
(%o5)            foo(x = 123, y = a - b, z = %e)
(%i6) kill (u@z);
(%o6)                         done
(%i7) u;
(%o7)              foo(x = 123, y = a - b, z)
(%i8) u@z;
(%o8)                          u@z
```


The field name is not evaluated.













```maxima
(%i1) defstruct (bar (g, h));
(%o1)                      [bar(g, h)]
(%i2) x : new (bar);
(%o2)                       bar(g, h)
(%i3) x@h : 42;
(%o3)                          42
(%i4) h : 123;
(%o4)                          123
(%i5) x@h;
(%o5)                          42
(%i6) x@h : 19;
(%o6)                          19
(%i7) x;
(%o7)                    bar(g, h = 19)
(%i8) h;
(%o8)                          123
```

### Variable: [

`[` and `]` mark the beginning and end, respectively, of a list.


`[` and `]` also enclose the subscripts of
a list, array, `hashed array`, or `memoizing-function`. Note that
other than for arrays accessing the `n`th element of a list
may need an amount of time that is roughly proportional to  `n`,
`Performance-considerations-for-Lists`.


Note that if an element of a subscripted variable is written to before
a list or an array of this name is declared a `hashed array`
(`Arrays`) is created, not a list.


Examples:














```maxima
(%i1) x: [a, b, c];
(%o1)                       [a, b, c]


(%i2) x[3];
(%o2)                           c


(%i3) array (y, fixnum, 3);
(%o3)                           y


(%i4) y[2]: %pi;
(%o4)                          %pi


(%i5) y[2];
(%o5)                          %pi


(%i6) z['foo]: 'bar;
(%o6)                          bar


(%i7) z['foo];
(%o7)                          bar


(%i8) g[k] := 1/(k^2+1);
                                  1
(%o8)                     g  := ------
                           k     2
                                k  + 1


(%i9) g[10];
                                1
(%o9)                          ---
                               101
```

See also: `hashed-array`, `memoizing-function`, `Performance-considerations-for-Lists`, `Arrays`.

### Function: accumulate (accumulate, op, X, X0, accumulate, op, X)

Returns a list comprising the partial results of *op* applied to successive elements of the list *X*.


*op* must be a function of two arguments, or an n-ary function.


When the optional argument *X0* is present,
`accumulate` returns
`[X0, op(X0, X[1]), op(op(X0, X[1]), X[2]), ...]`.


When the optional argument *X0* is absent,
`accumulate` returns
`[X[1], op(X[1], X[2]), op(op(X[1], X[2]), X[3]), ...]`.


The final element returned by `accumulate` is the same as the result returned by `lreduce`.
The difference is that `accumulate` also returns the partial results leading up to the final element.


Examples:












```maxima
maxima

(%i1) accumulate ("+", [a, b, c]);
(%o1)                 [a, b + a, c + b + a]


(%i2) accumulate ("+", [a, b, c], 10);
(%o2)       [10, a + 10, b + a + 10, c + b + a + 10]


(%i3) accumulate ("*", [a, b, c]);
(%o3)                    [a, a b, a b c]


(%i4) accumulate ("/", [a, b, c], 100);
                           100  100   100
(%o4)                [100, ---, ---, -----]
                            a   a b  a b c


(%i5) accumulate (f, [a, b, c], 0);
(%o5)   [0, f(0, a), f(f(0, a), b), f(f(f(0, a), b), c)]


(%i6) lreduce (f, [a, b, c], 0);
(%o6)                  f(f(f(0, a), b), c)


(%i7) accumulate ("+", [2, 3, 5, 7, 11, 13, 17, 19]);
(%o7)            [2, 5, 10, 17, 28, 41, 58, 77]
```

See also: `lreduce`.

### Function: append (list_1, ..., list_n)

Returns a single list of the elements of *list_1* followed
by the elements of *list_2*, ...  `append` also works on
general expressions, e.g. `append (f(a,b), f(c,d,e));` yields
`f(a,b,c,d,e)`.


See also `addrow`, `addcol` and `join`.


Do `example(append);` for an example.

See also: `addrow`, `addcol`, `join`.

### Function: array (array, name, dim_1, ..., dim_n, array, name, type, dim_1, ..., dim_n, array, name_1, ..., name_m, dim_1, ..., dim_n)

Creates an $n$-dimensional array.  $n$ may be less than or equal to 5.
The subscripts for the $i$’th dimension are the integers running from 0 to
*dim_i*.


`array (name, dim_1, ..., dim_n)` creates a general
array.


`array (name, type, dim_1, ..., dim_n)` creates
an array, with elements of a specified type.  *type* can be `fixnum`
for integers of limited size or `flonum` for floating-point numbers.


`array ([name_1, ..., name_m], dim_1, ..., dim_n)`
creates $m$ arrays, all of the same dimensions.



See also `arraymake`, `arrayinfo` and `make_005farray`.

See also: `arraymake`, `arrayinfo`, `make_array`.

### Function: arrayapply (A, i_1, ..., i_n)

Evaluates `A [i_1, ..., i_n]`,
where *A* is an array and *i_1*, ..., *i_n* are integers.


This is reminiscent of `apply`, except the first argument is an array
instead of a function.

See also: `apply`.

### Function: arrayinfo (A)

Returns information about the array *A*.
The argument *A* may be a declared array, a `hashed array`,
a `memoizing function`, or a subscripted function.


For declared arrays, `arrayinfo` returns a list comprising the atom
`declared`, the number of dimensions, and the size of each dimension.
The elements of the array, both bound and unbound, are returned by
`listarray`.


For undeclared arrays (hashed arrays), `arrayinfo` returns a list
comprising the atom `hashed`, the number of subscripts,
and the subscripts of every element which has a value.
The values are returned by `listarray`.


For `memoizing functions`, `arrayinfo` returns a list comprising the atom
`hashed`, the number of subscripts,
and any subscript values for which there are stored function values.
The stored function values are returned by `listarray`.


For subscripted functions, `arrayinfo` returns a list comprising the atom
`hashed`, the number of subscripts,
and any subscript values for which there are lambda expressions.
The lambda expressions are returned by `listarray`.


See also `listarray`.


Examples:


`arrayinfo` and `listarray` applied to a declared array.










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa


(%i2) aa [2, 3] : %pi;
(%o2)                          %pi


(%i3) aa [1, 2] : %e;
(%o3)                          %e


(%i4) arrayinfo (aa);
(%o4)                 [declared, 2, [2, 3]]


(%i5) listarray (aa);
(%o5) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
```


`arrayinfo` and `listarray` applied to an undeclared array (`hashed-array`.).









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)


(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)


(%i3) arrayinfo (bb);
(%o3)               [hashed, 1, [BAR], [FOO]]


(%i4) listarray (bb);
                              3         2
(%o4)                 [(c - d) , (b + a) ]
```


`arrayinfo` and `listarray` applied to a `memoizing-function`.










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x


(%i2) cc [u, v];
                                v
(%o2)                           -
                                u


(%i3) cc [4, z];
                                z
(%o3)                           -
                                4


(%i4) arrayinfo (cc);
(%o4)              [hashed, 2, [4, z], [u, v]]


(%i5) listarray (cc);
                              z  v
(%o5)                        [-, -]
                              4  u
```



Using `arrayinfo` in order to convert an undeclared array to a declared array:










```maxima
(%i1) for i:0 thru 10 do a[i]:i^2$

(%i2) indices:map(first,rest(rest(arrayinfo(a))));
(%o2)          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

(%i3) array(A,fixnum,length(indices)-1)$
(%i4) fillarray(A,map(lambda([x],a[x]),indices))$

(%i5) listarray(A);
(%o5)       [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


`arrayinfo` and `listarray` applied to a subscripted function.










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x


(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )


(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )


(%i4) arrayinfo (dd);
(%o4)             [hashed, 1, [b + a], [v - u]]


(%i5) listarray (dd);
                         b + a                v - u
(%o5)      [lambda([y], y     ), lambda([y], y     )]
```

See also: `hashed-array`, `memoizing-function`, `listarray`, `memoizing-functions`.

### Function: arraymake (A, i_1, ..., i_n)

Returns the expression `A[i_1, ..., i_n]`.
The result is an unevaluated array reference.


`arraymake` is reminiscent of `funmake`, except the return value
is an unevaluated array reference instead of an unevaluated function call.


Examples:


















```maxima
(%i1) arraymake (A, [1]);
(%o1)                          A
                                1


(%i2) arraymake (A, [k]);
(%o2)                          A
                                k


(%i3) arraymake (A, [i, j, 3]);
(%o3)                       A
                             i, j, 3


(%i4) array (A, fixnum, 10);
(%o4)                           A


(%i5) fillarray (A, makelist (i^2, i, 1, 11));
(%o5)                           A


(%i6) arraymake (A, [5]);
(%o6)                          A
                                5


(%i7) ''%;
(%o7)                          36


(%i8) L : [a, b, c, d, e];
(%o8)                    [a, b, c, d, e]


(%i9) arraymake ('L, [n]);
(%o9)                          L
                                n


(%i10) ''%, n = 3;
(%o10)                          c


(%i11) A2 : make_array (fixnum, 10);
(%o11)        {Lisp Array: #(0 0 0 0 0 0 0 0 0 0)}


(%i12) fillarray (A2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o12)        {Lisp Array: #(1 2 3 4 5 6 7 8 9 10)}


(%i13) arraymake ('A2, [8]);
(%o13)                         A2
                                 8


(%i14) ''%;
(%o14)                          9
```

See also: `funmake`.

### Variable: arrays

Default value: `[]`


`arrays` is a list of arrays that have been allocated.
These comprise arrays declared by `array`, `hashed arrays` that can be
constructed by implicit definition (assigning something to an element that isn’t yet
declared as a list or an array),
and `memoizing functions` defined by `:=` and `define`.
Arrays defined by `make_array` are not included.


See also
`array`, `arrayapply`, `arrayinfo`,
`arraymake`, `fillarray`, `listarray`, and
`rearray`.



Examples:










```maxima
(%i1) array (aa, 5, 7);
(%o1)                          aa


(%i2) bb [FOO] : (a + b)^2;
                                   2
(%o2)                       (b + a)


(%i3) cc [x] := x/100;
                                   x
(%o3)                      cc  := ---
                             x    100


(%i4) dd : make_array ('any, 7);
(%o4)     {Lisp Array: #(NIL NIL NIL NIL NIL NIL NIL)}


(%i5) arrays;
(%o5)                     [aa, bb, cc]
```

See also: `array`, `hashed-arrays`, `memoizing-functions`, `define`, `make_array`, `arrayapply`, `arrayinfo`, `arraymake`, `fillarray`, `listarray`, `rearray`.

### Function: arraysetapply (A, i_1, ..., i_n, x)

Assigns *x* to `A[i_1, ..., i_n]`,
where *A* is an array and *i_1*, ..., *i_n* are integers.


`arraysetapply` evaluates its arguments.

### Function: assoc (assoc, key, e, default, assoc, key, e)

`assoc` searches for *key* as the first part of an argument of *e*
and returns the second part of the first match, if any.


*key* may be any expression.
*e* must be a nonatomic expression,
and every argument of *e* must have exactly two parts.
`assoc` returns the second part of the first matching argument of *e*.
Matches are determined by `is(key = first(a))`
where *a* is an argument of *e*.


If there are two or more matches, only the first is returned.
If there are no matches, *default* is returned, if specified.
Otherwise, `false` is returned.


See also `sublist` and `member`.


Examples:


*key* may be any expression.
*e* must be a nonatomic expression,
and every argument of *e* must have exactly two parts.
`assoc` returns the second part of the first matching argument of *e*.






```maxima
(%i1) assoc (f(x), foo(g(x) = y, f(x) = z + 1, h(x) = 2*u));
(%o1)                         z + 1
```


If there are two or more matches, only the first is returned.






```maxima
(%i1) assoc (yy, [xx = 111, yy = 222, yy = 333, yy = 444]);
(%o1)                          222
```


If there are no matches, *default* is returned, if specified.
Otherwise, `false` is returned.







```maxima
(%i1) assoc (abc, [[x, 111], [y, 222], [z, 333]], none);
(%o1)                         none


(%i2) assoc (abc, [[x, 111], [y, 222], [z, 333]]);
(%o2)                         false
```

See also: `sublist`, `member`.

### Function: cons (cons, expr, list, cons, expr_1, expr_2)

`cons (expr, list)` returns a new list constructed of the element 
*expr* as its first element, followed by the elements of *list*. This is 
analogous to the Lisp language construction operation "cons".


The Maxima function `cons` can also be used where the second argument is other
than a list and this might be useful. In this case, `cons (expr_1, expr_2)`
returns an expression with same operator as *expr_2* but with argument `cons(expr_1, args(expr_2))`.
Examples:







```maxima
(%i1) cons(a,[b,c,d]);
(%o1)                     [a, b, c, d]


(%i2) cons(a,f(b,c,d));
(%o2)                     f(a, b, c, d)
```


In general, `cons` applied to a nonlist doesn’t make sense. For instance, `cons(a,b^c)`
results in an illegal expression, since ’^’ cannot take three arguments. 


When `inflag` is true, `cons` operates on the internal structure of an expression, otherwise
`cons` operates on the displayed form. Especially when `inflag` is true, `cons` applied 
to a nonlist sometimes gives a surprising result; for example







```maxima
(%i1) cons(a,-a), inflag : true;
                                 2
(%o1)                         - a


(%i2) cons(a,-a), inflag : false;
(%o2)                           0
```

### Function: copylist (list)

Returns a copy of the list *list*.

### Function: create_list (form, x_1, list_1, ..., x_n, list_n)

Create a list by evaluating *form* with *x_1* bound to
each element of *list_1*, and for each such binding bind *x_2*
to each element of *list_2*, ...
The number of elements in the result will be
the product of the number of elements in each list.
Each variable *x_i* must actually be a symbol – it will not be evaluated.
The list arguments will be evaluated once at the beginning of the
iteration.






```maxima
(%i1) create_list (x^i, i, [1, 3, 7]);
                                3   7
(%o1)                      [x, x , x ]
```



With a double iteration:






```maxima
(%i1) create_list ([i, j], i, [a, b], j, [e, f, h]);
(%o1)   [[a, e], [a, f], [a, h], [b, e], [b, f], [b, h]]
```


Instead of *list_i* two args may be supplied each of which should
evaluate to a number.  These will be the inclusive lower and
upper bounds for the iteration.






```maxima
(%i1) create_list ([i, j], i, [1, 2, 3], j, 1, i);
(%o1)   [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]
```


Note that the limits or list for the `j` variable can
depend on the current value of `i`.

### Function: defstruct (defstruct, S, a_1, ..., a_n, defstruct, S, a_1, =, v_1, ..., a_n, =, v_n)

Define a structure, which is a list of named fields *a_1*, ...,
*a_n* associated with a symbol *S*.
An instance of a structure is just an expression which has operator *S*
and exactly `n` arguments.
`new(S)` creates a new instance of structure *S*.


An argument which is just a symbol *a* specifies the name of a field.
An argument which is an equation `a = v` specifies the field name *a*
and its default value *v*.
The default value can be any expression.


`defstruct` puts *S* on the list of user-defined structures, `structures`.


`kill(S)` removes *S* from the list of user-defined structures,
and removes the structure definition.


Examples:













```maxima
(%i1) defstruct (foo (a, b, c));
(%o1)                    [foo(a, b, c)]
(%i2) structures;
(%o2)                    [foo(a, b, c)]
(%i3) new (foo);
(%o3)                     foo(a, b, c)
(%i4) defstruct (bar (v, w, x = 123, y = %pi));
(%o4)             [bar(v, w, x = 123, y = %pi)]
(%i5) structures;
(%o5)      [foo(a, b, c), bar(v, w, x = 123, y = %pi)]
(%i6) new (bar);
(%o6)              bar(v, w, x = 123, y = %pi)
(%i7) kill (foo);
(%o7)                         done
(%i8) structures;
(%o8)             [bar(v, w, x = 123, y = %pi)]
```

### Function: delete (delete, expr_1, expr_2, delete, expr_1, expr_2, n)

`delete(expr_1, expr_2)`
removes from *expr_2* any arguments of its top-level operator
which are the same (as determined by "=") as *expr_1*.
Note that "=" tests for formal equality, not equivalence.
Note also that arguments of subexpressions are not affected.


*expr_1* may be an atom or a non-atomic expression.
*expr_2* may be any non-atomic expression.
`delete` returns a new expression;
it does not modify *expr_2*.


`delete(expr_1, expr_2, n)`
removes from *expr_2* the first *n* arguments of the top-level operator
which are the same as *expr_1*.
If there are fewer than *n* such arguments,
then all such arguments are removed.


Examples:


Removing elements from a list.






```maxima
(%i1) delete (y, [w, x, y, z, z, y, x, w]);
(%o1)                  [w, x, z, z, x, w]
```


Removing terms from a sum.






```maxima
(%i1) delete (sin(x), x + sin(x) + y);
(%o1)                         y + x
```


Removing factors from a product.






```maxima
(%i1) delete (u - x, (u - w)*(u - x)*(u - y)*(u - z));
(%o1)                (u - w) (u - y) (u - z)
```


Removing arguments from an arbitrary expression.






```maxima
(%i1) delete (a, foo (a, b, c, d, a));
(%o1)                     foo(b, c, d)
```


Limit the number of removed arguments.






```maxima
(%i1) delete (a, foo (a, b, a, c, d, a), 2);
(%o1)                    foo(b, c, d, a)
```


Whether arguments are the same as *expr_1* is determined by "=".
Arguments which are `equal` but not "=" are not removed.











```maxima
(%i1) [is (equal (0, 0)), is (equal (0, 0.0)), is (equal (0, 0b0))];
(%o1)                  [true, true, true]


(%i2) [is (0 = 0), is (0 = 0.0), is (0 = 0b0)];
(%o2)                 [true, false, false]


(%i3) delete (0, [0, 0.0, 0b0]);
(%o3)                     [0.0, 0.0b0]


(%i4) is (equal ((x + y)*(x - y), x^2 - y^2));
(%o4)                         true


(%i5) is ((x + y)*(x - y) = x^2 - y^2);
(%o5)                         false


(%i6) delete ((x + y)*(x - y), [(x + y)*(x - y), x^2 - y^2]);
                              2    2
(%o6)                       [x  - y ]
```

### Function: eighth (expr)

Returns the 8th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: endcons (endcons, expr, list, endcons, expr_1, expr_2)

`endcons (expr, list)` returns a new list constructed of the elements of 
*list* followed by *expr*. The Maxima function `endcons` can also be used where 
the second argument is other than a list and this might be useful. In this case,
`endcons (expr_1, expr_2)` returns an expression with same operator as 
*expr_2* but with argument `endcons(expr_1, args(expr_2))`. Examples:







```maxima
(%i1) endcons(a,[b,c,d]);
(%o1)                     [b, c, d, a]


(%i2) endcons(a,f(b,c,d));
(%o2)                     f(b, c, d, a)
```


In general, `endcons` applied to a nonlist doesn’t make sense. For instance, `endcons(a,b^c)`
results in an illegal expression, since ’^’ cannot take three arguments. 


When `inflag` is true, `endcons` operates on the internal structure of an expression, otherwise
`endcons` operates on the displayed form. Especially when `inflag` is true, `endcons` applied 
to a nonlist sometimes gives a surprising result; for example







```maxima
(%i1) endcons(a,-a), inflag : true;
                                 2
(%o1)                         - a


(%i2) endcons(a,-a), inflag : false;
(%o2)                           0
```

### Variable: false

`false` represents the Boolean constant of the same name.
Maxima implements `false` by the value `NIL` in Lisp.

### Function: fifth (expr)

Returns the 5th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: fillarray (A, B)

Fills array *A* from *B*, which is a list or an array.


If a specific type was declared for *A* when it was created,
it can only be filled with elements of that same type;
it is an error if an attempt is made to copy an element of a different type.


If the dimensions of the arrays *A* and *B* are
different, *A* is filled in row-major order.  If there are not enough
elements in *B* the last element is used to fill out the
rest of *A*.  If there are too many, the remaining ones are ignored.


`fillarray` returns its first argument.


Examples:


Create an array of 9 elements and fill it from a list.









```maxima
(%i1) array (a1, fixnum, 8);
(%o1)                          a1


(%i2) listarray (a1);
(%o2)              [0, 0, 0, 0, 0, 0, 0, 0, 0]


(%i3) fillarray (a1, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
(%o3)                          a1


(%i4) listarray (a1);
(%o4)              [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


When there are too few elements to fill the array,
the last element is repeated.
When there are too many elements,
the extra elements are ignored.









```maxima
(%i1) a2 : make_array (fixnum, 8);
(%o1)           {Lisp Array: #(0 0 0 0 0 0 0 0)}


(%i2) fillarray (a2, [1, 2, 3, 4, 5]);
(%o2)           {Lisp Array: #(1 2 3 4 5 5 5 5)}


(%i3) fillarray (a2, [4]);
(%o3)           {Lisp Array: #(4 4 4 4 4 4 4 4)}


(%i4) fillarray (a2, makelist (i, i, 1, 100));
(%o4)           {Lisp Array: #(1 2 3 4 5 6 7 8)}
```


Multiple-dimension arrays are filled in row-major order.









```maxima
(%i1) a3 : make_array (fixnum, 2, 5);
(%o1)      {Lisp Array: #2A((0 0 0 0 0) (0 0 0 0 0))}


(%i2) fillarray (a3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o2)      {Lisp Array: #2A((1 2 3 4 5) (6 7 8 9 10))}


(%i3) a4 : make_array (fixnum, 5, 2);
(%o3)   {Lisp Array: #2A((0 0) (0 0) (0 0) (0 0) (0 0))}


(%i4) fillarray (a4, a3);
(%o4)   {Lisp Array: #2A((1 2) (3 4) (5 6) (7 8) (9 10))}
```

### Function: first (expr)

Returns the first part of *expr* which may result in the first element of a
list, the first row of a matrix, the first term of a sum, etc.:



```maxima
(%i1) matrix([1,2],[3,4]);
                                   [ 1  2 ]
(%o1)                              [      ]
                                   [ 3  4 ]
(%i2) first(%);
(%o2)                              [1,2]
(%i3) first(%);
(%o3)                              1
(%i4) first(a*b/c+d+e/x);
                                   a b
(%o4)                              ---
                                    c
(%i5) first(a=b/c+d+e/x);
(%o5)                              a
```


Note that
`first` and its related functions, `rest` and `last`, work
on the form of *expr* which is displayed not the form which is typed on
input.  If the variable `inflag` is set to `true` however, these
functions will look at the internal form of *expr*. One reason why this may
make a difference is that the simplifier re-orders expressions:



```maxima
(%i1) x+y;
(%o1)                              y+1
(%i2) first(x+y),inflag : true;
(%o2)                              x
(%i3) first(x+y),inflag : false;
(%o3)                              y
```


The functions `second` ...
`tenth` yield the second through the tenth part of their input argument.


See also `firstn` and `part`.

See also: `inflag`, `firstn`, `part`.

### Function: firstn (expr, count)

Returns the first *count* arguments of *expr*, if *expr* has at least *count* arguments.
Returns *expr* if *expr* has less than *count* arguments.


*expr* may be any nonatomic expression. 
When *expr* is something other than a list,
`firstn` returns an expression which has the same operator as *expr*.
*count* must be a nonnegative integer.


`firstn` honors the global flag `inflag`,
which governs whether the internal form of an expression is processed (when `inflag` is true)
or the displayed form (when `inflag` is false).


Note that `firstn(expr, 1)`,
which returns a nonatomic expression containing the first argument,
is not the same as `first(expr)`,
which returns the first argument by itself.


See also `lastn` and `rest`.


Examples:


`firstn` returns the first *count* elements of *expr*, if *expr* has at least *count* elements.










```maxima
(%i1) mylist : [1, a, 2, b, 3, x, 4 - y, 2*z + sin(u)];
(%o1)        [1, a, 2, b, 3, x, 4 - y, 2 z + sin(u)]


(%i2) firstn (mylist, 0);
(%o2)                          []


(%i3) firstn (mylist, 1);
(%o3)                          [1]


(%i4) firstn (mylist, 2);
(%o4)                        [1, a]


(%i5) firstn (mylist, 7);
(%o5)               [1, a, 2, b, 3, x, 4 - y]
```


`firstn` returns *expr* if *expr* has less than *count* elements.







```maxima
(%i1) mylist : [1, a, 2, b, 3, x, 4 - y, 2*z + sin(u)];
(%o1)        [1, a, 2, b, 3, x, 4 - y, 2 z + sin(u)]


(%i2) firstn (mylist, 100);
(%o2)        [1, a, 2, b, 3, x, 4 - y, 2 z + sin(u)]
```


*expr* may be any nonatomic expression. 











```maxima
(%i1) myfoo : foo(1, a, 2, b, 3, x, 4 - y, 2*z + sin(u));
(%o1)      foo(1, a, 2, b, 3, x, 4 - y, 2 z + sin(u))


(%i2) firstn (myfoo, 4);
(%o2)                    foo(1, a, 2, b)


(%i3) mybar : bar[m, n](1, a, 2, b, 3, x, 4 - y, 2*z + sin(u));
(%o3)    bar    (1, a, 2, b, 3, x, 4 - y, 2 z + sin(u))
            m, n


(%i4) firstn (mybar, 4);
(%o4)                  bar    (1, a, 2, b)
                          m, n

(%i5) mymatrix : genmatrix (lambda ([i, j], 10*i + j), 10, 4) $

(%i6) firstn (mymatrix, 3);
                       [ 11  12  13  14 ]
                       [                ]
(%o6)                  [ 21  22  23  24 ]
                       [                ]
                       [ 31  32  33  34 ]
```


`firstn` honors the global flag `inflag`.








```maxima
(%i1) myexpr : a + b + c + d + e;
(%o1)                   e + d + c + b + a


(%i2) firstn (myexpr, 3), inflag=true;
(%o2)                       c + b + a


(%i3) firstn (myexpr, 3), inflag=false;
(%o3)                       e + d + c
```


Note that `firstn(expr, 1)` is not the same as `first(expr)`.







```maxima
(%i1) firstn ([w, x, y, z], 1);
(%o1)                          [w]


(%i2) first ([w, x, y, z]);
(%o2)                           w
```

See also: `lastn`, `rest`.

### Function: fourth (expr)

Returns the 4th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: has_key (A, L)

Returns `true` if the undeclared array or hash table *A* has the key or keys (i.e., subscripts) *L*,
otherwise `false`.


*A* must be an undeclared array,
or a hash table value returned by `make_array`
or created as an undeclared array with `use_fast_arrays` equal to `true`.


*L* must be supplied as a list even if there is only one key.


See also `arrayinfo` which returns all the keys for an undeclared array or hash table.


Examples:


`aa` is an undeclared array, which has one key.
The key must be supplied to `has_key` as a list even though there is only one.









```maxima
maxima

(%i1) aa["abc"]: "defghi";
(%o1)                        defghi


(%i2) arrayinfo (aa);
(%o2)                  [hashed, 1, [abc]]


(%i3) has_key (aa, ["abc"]);
(%o3)                         true


(%i4) has_key (aa, ["abcd"]);
(%o4)                         false
```


`bb` is a hash table returned by `make_array`.
`bb` has one key.










```maxima
maxima

(%i1) bb: make_array ('hashed);
(%o1) 
    {Lisp Array: #<HASH-TABLE :TEST EQUAL :COUNT 1 {1202136213}>}


(%i2) bb[9876]: 1 + x + y + z;
(%o2)                     z + y + x + 1


(%i3) arrayinfo (bb);
(%o3)                 [hash_table, 1, 9876]


(%i4) has_key (bb, [9876]);
(%o4)                         true


(%i5) has_key (bb, [1234]);
(%o5)                         false
```


`cc` is a hash table created as an undeclared array with `use_fast_arrays` equal to `true`.
`cc` has two keys.











```maxima
maxima
(%i1) use_fast_arrays: true $

(%i2) cc["xyz", 123]: 1729;
(%o2)                         1729


(%i3) cc;
(%o3) 
    {Lisp Array: #<HASH-TABLE :TEST EQUAL :COUNT 1 {1202136733}>}


(%i4) arrayinfo (cc);
(%o4)            [hash_table, true, [xyz, 123]]


(%i5) has_key (cc, ["xyz", 123]);
(%o5)                         true


(%i6) has_key (cc, [567, "ghi"]);
(%o6)                         false
```

See also: `make_array`, `use_fast_arrays`, `arrayinfo`.

### Variable: ind

`ind` represents a bounded, indefinite result.


See also `limit`.


Example:






```maxima
(%i1) limit (sin(1/x), x, 0);
(%o1)                          ind
```

See also: `limit`.

### Variable: inf

`inf` represents real positive infinity.

### Variable: infinity

`infinity` represents complex infinity.

### Function: join (l, m)

Creates a new list containing the elements of lists *l* and *m*,
interspersed.  The result has elements `[l[1], m[1], l[2], m[2], ...]`.  The lists *l* and *m* may contain any
type of elements.


If the lists are different lengths, `join` ignores elements of the longer
list.


Maxima complains if *l* or *m* is not a list.


See also `append`.


Examples:








```maxima
(%i1) L1: [a, sin(b), c!, d - 1];
(%o1)                [a, sin(b), c!, d - 1]


(%i2) join (L1, [1, 2, 3, 4]);
(%o2)          [a, 1, sin(b), 2, c!, 3, d - 1, 4]


(%i3) join (L1, [aa, bb, cc, dd, ee, ff]);
(%o3)        [a, aa, sin(b), bb, c!, cc, d - 1, dd]
```

See also: `append`.

### Function: last (expr)

Returns the last part (term, row, element, etc.) of the *expr*.


See also `lastn`.

See also: `lastn`.

### Function: lastn (expr, count)

Returns the last *count* arguments of *expr*, if *expr* has at least *count* arguments.
Returns *expr* if *expr* has less than *count* arguments.


*expr* may be any nonatomic expression. 
When *expr* is something other than a list,
`lastn` returns an expression which has the same operator as *expr*.
*count* must be a nonnegative integer.


`lastn` honors the global flag `inflag`,
which governs whether the internal form of an expression is processed (when `inflag` is true)
or the displayed form (when `inflag` is false).


Note that `lastn(expr, 1)`,
which returns a nonatomic expression containing the last argument,
is not the same as `last(expr)`,
which returns the last argument by itself.


See also `firstn` and `rest`.


Examples:


`lastn` returns the last *count* elements of *expr*, if *expr* has at least *count* elements.










```maxima
(%i1) mylist : [1, a, 2, b, 3, x, 4 - y, 2*z + sin(u)];
(%o1)        [1, a, 2, b, 3, x, 4 - y, 2 z + sin(u)]


(%i2) lastn (mylist, 0);
(%o2)                          []


(%i3) lastn (mylist, 1);
(%o3)                    [2 z + sin(u)]


(%i4) lastn (mylist, 2);
(%o4)                 [4 - y, 2 z + sin(u)]


(%i5) lastn (mylist, 7);
(%o5)         [a, 2, b, 3, x, 4 - y, 2 z + sin(u)]
```


`lastn` returns *expr* if *expr* has less than *count* elements.







```maxima
(%i1) mylist : [1, a, 2, b, 3, x, 4 - y, 2*z + sin(u)];
(%o1)        [1, a, 2, b, 3, x, 4 - y, 2 z + sin(u)]


(%i2) lastn (mylist, 100);
(%o2)        [1, a, 2, b, 3, x, 4 - y, 2 z + sin(u)]
```


*expr* may be any nonatomic expression. 











```maxima
(%i1) myfoo : foo(1, a, 2, b, 3, x, 4 - y, 2*z + sin(u));
(%o1)      foo(1, a, 2, b, 3, x, 4 - y, 2 z + sin(u))


(%i2) lastn (myfoo, 4);
(%o2)            foo(3, x, 4 - y, 2 z + sin(u))


(%i3) mybar : bar[m, n](1, a, 2, b, 3, x, 4 - y, 2*z + sin(u));
(%o3)    bar    (1, a, 2, b, 3, x, 4 - y, 2 z + sin(u))
            m, n


(%i4) lastn (mybar, 4);
(%o4)          bar    (3, x, 4 - y, 2 z + sin(u))
                  m, n

(%i5) mymatrix : genmatrix (lambda ([i, j], 10*i + j), 10, 4) $

(%i6) lastn (mymatrix, 3);
                     [ 81   82   83   84  ]
                     [                    ]
(%o6)                [ 91   92   93   94  ]
                     [                    ]
                     [ 101  102  103  104 ]
```


`lastn` honors the global flag `inflag`.








```maxima
(%i1) myexpr : a + b + c + d + e;
(%o1)                   e + d + c + b + a


(%i2) lastn (myexpr, 3), inflag=true;
(%o2)                       e + d + c


(%i3) lastn (myexpr, 3), inflag=false;
(%o3)                       c + b + a
```


Note that `lastn(expr, 1)` is not the same as `last(expr)`.







```maxima
(%i1) lastn ([w, x, y, z], 1);
(%o1)                          [z]


(%i2) last ([w, x, y, z]);
(%o2)                           z
```

See also: `firstn`, `rest`.

### Variable: least_negative_float

The least negative floating-point number in Maxima.  That is, the
negative floating-point number closest to 0.  It is approximately
-4.94065e-324, when
[https://en.wikipedia.org/wiki/Subnormal_numberdenormal]() numbers
are supported.  Otherwise it is the same as
`least_negative_normalized_float`.

See also: `least_negative_normalized_float`.

### Variable: least_negative_normalized_float

The least negative normalized floating-point number in Maxima.  That
is, the negative normalized floating-point number closest to 0.  It is
approximately -2.22507e-308.

### Variable: least_positive_float

The least positive floating-point number in Maxima.  That is, the
positive floating-point number closest to 0.  It is approximately
4.94065e-324, when
[https://en.wikipedia.org/wiki/Subnormal_numberdenormal]() numbers
are supported.  Otherwise it is the same as
`least_positive_normalized_float`.

See also: `least_positive_normalized_float`.

### Variable: least_positive_normalized_float

The least positive normalized floating-point number in Maxima.  That
is, the positive normalized floating-point number closest to 0.  It is
approximately 2.22507e-308.

### Function: length (expr)

Returns (by default) the number of parts in the external
(displayed) form of *expr*.  For lists this is the number of elements,
for matrices it is the number of rows, and for sums it is the number
of terms (see `dispform`).


The `length` command is affected by the `inflag` switch.  So, e.g.
`length(a/(b*c));` gives 2 if `inflag` is `false` (Assuming
`exptdispflag` is `true`), but 3 if `inflag` is `true` (the
internal representation is essentially `a*b^-1*c^-1`).


Determining a list’s length typically needs an amount of time proportional
to the number of elements in the list. If the length of a list is used inside
a loop it therefore might drastically increase the performance if the length
is calculated outside the loop instead.

See also: `dispform`, `inflag`, `exptdispflag`.

### Variable: listarith

Default value: `true` 


If `false` causes any arithmetic operations with lists to be suppressed;
when `true`, list-matrix operations are contagious causing lists to be
converted to matrices yielding a result which is always a matrix.  However,
list-list operations should return lists.

### Function: listarray (A)

Returns a list of the elements of the array *A*.
The argument *A* may be an array, an undeclared array (`hashed array`),
a `memoizing function`, or a subscripted function.


Elements are listed in row-major order.
That is, elements are sorted according to the first index, then according to
the second index, and so on.  The sorting order of index values is the same as
the order established by `orderless`.


For undeclared arrays (`hashed arrays`), `memoizing functions`, and subscripted functions,
the elements correspond to the index values returned by `arrayinfo`.


Unbound elements of general arrays (that is, not `fixnum` and not
`flonum`) are returned as `#####`.
Unbound elements of `fixnum` or `flonum` arrays
are returned as 0 or 0.0, respectively.
Unbound elements of hashed arrays, `memoizing functions`,
and subscripted functions are not returned.


Examples:


`listarray` and `arrayinfo` applied to a declared array.










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa


(%i2) aa [2, 3] : %pi;
(%o2)                          %pi


(%i3) aa [1, 2] : %e;
(%o3)                          %e


(%i4) listarray (aa);
(%o4) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]


(%i5) arrayinfo (aa);
(%o5)                 [declared, 2, [2, 3]]
```


`listarray` and `arrayinfo` applied to an undeclared array (`hashed array`).









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)


(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)


(%i3) listarray (bb);
                              3         2
(%o3)                 [(c - d) , (b + a) ]


(%i4) arrayinfo (bb);
(%o4)               [hashed, 1, [BAR], [FOO]]
```


`listarray` and `arrayinfo` applied to a `memoizing-function`.










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x


(%i2) cc [u, v];
                                v
(%o2)                           -
                                u


(%i3) cc [4, z];
                                z
(%o3)                           -
                                4


(%i4) listarray (cc);
                              z  v
(%o4)                        [-, -]
                              4  u


(%i5) arrayinfo (cc);
(%o5)              [hashed, 2, [4, z], [u, v]]
```


`listarray` and `arrayinfo` applied to a subscripted function.










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x


(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )


(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )


(%i4) listarray (dd);
                         b + a                v - u
(%o4)      [lambda([y], y     ), lambda([y], y     )]


(%i5) arrayinfo (dd);
(%o5)             [hashed, 1, [b + a], [v - u]]
```

See also: `hashed-array`, `memoizing-function`, `orderless`, `hashed-arrays`, `memoizing-functions`, `arrayinfo`.

### Function: listp (expr)

Returns `true` if *expr* is a list else `false`.

### Function: lreduce (lreduce, F, s, lreduce, F, s, s_0)

Extends the binary function *F* to an n-ary function by composition,
where *s* is a list.


`lreduce(F, s)` returns `F(... F(F(s_1, s_2), s_3), ... s_n)`.
When the optional argument *s_0* is present,
the result is equivalent to `lreduce(F, cons(s_0, s))`.


The function *F* is first applied to the
*leftmost* list elements, thus the name "lreduce".


See also `rreduce`, `xreduce`, and `tree_reduce`.


Examples:


`lreduce` without the optional argument.







```maxima
(%i1) lreduce (f, [1, 2, 3]);
(%o1)                     f(f(1, 2), 3)


(%i2) lreduce (f, [1, 2, 3, 4]);
(%o2)                  f(f(f(1, 2), 3), 4)
```


`lreduce` with the optional argument.






```maxima
(%i1) lreduce (f, [1, 2, 3], 4);
(%o1)                  f(f(f(4, 1), 2), 3)
```


`lreduce` applied to built-in binary operators.
`/` is the division operator.







```maxima
(%i1) lreduce ("^", [a, b, c, d]);
                               b c d
(%o1)                       ((a ) )


(%i2) lreduce ("/", [a, b, c, d]);
                                a
(%o2)                         -----
                              b c d
```

See also: `rreduce`, `xreduce`, `tree_reduce`.

### Function: make_array (type, dim_1, ..., dim_n)

Creates and returns a Lisp array.  *type* may
be `any`, `flonum`, `fixnum`, `hashed` or 
`functional`.
There are $n$ indices,
and the $i$’th index runs from 0 to $dim_i - 1$.


The advantage of `make_array` over `array` is that the return value
doesn’t have a name, and once a pointer to it goes away, it will also go away.
For example, if `y: make_array (...)` then `y` points to an object 
which takes up space, but after `y: false`, `y` no longer
points to that object, so the object can be garbage collected.











Examples:

















```maxima
(%i1) A1 : make_array (fixnum, 10);
(%o1)         {Lisp Array: #(0 0 0 0 0 0 0 0 0 0)}


(%i2) A1 [8] : 1729;
(%o2)                         1729


(%i3) A1;
(%o3)        {Lisp Array: #(0 0 0 0 0 0 0 0 1729 0)}


(%i4) A2 : make_array (flonum, 10);
(%o4) {Lisp Array: #(0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}


(%i5) A2 [2] : 2.718281828;
(%o5)                      2.718281828


(%i6) A2;
(%o6) 
 {Lisp Array: #(0.0 0.0 2.718281828 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}


(%i7) A3 : make_array (any, 10);
(%o7) {Lisp Array: #(NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL)}


(%i8) A3 [4] : x - y - z;
(%o8)                     (- z) - y + x


(%i9) A3;
(%o9) {Lisp Array: #(NIL NIL NIL NIL
               ((MPLUS SIMP) $X ((MTIMES SIMP) -1 $Y) ((MTIMES S\
IMP) -1 $Z))
               NIL NIL NIL NIL NIL)}


(%i10) A4 : make_array (fixnum, 2, 3, 5);
(%o10) {Lisp Array: #3A(((0 0 0 0 0) (0 0 0 0 0) (0 0 0 0 0))
                 ((0 0 0 0 0) (0 0 0 0 0) (0 0 0 0 0)))}


(%i11) fillarray (A4, makelist (i, i, 1, 2*3*5));
(%o11) {Lisp Array: #3A(((1 2 3 4 5) (6 7 8 9 10) (11 12 13 14 1\
5))
                 ((16 17 18 19 20) (21 22 23 24 25) (26 27 28 29\
 30)))}


(%i12) A4 [0, 2, 1];
(%o12)                         12
```

See also: `array`.

### Function: makelist (makelist, makelist, expr, makelist, expr, n, makelist, expr, i, i_max, makelist, expr, i, i_0, i_max, makelist, expr, i, i_0, i_max, step, makelist, expr, x, list)

The first form, `makelist ()`, creates an empty list. The second form,
`makelist (expr)`, creates a list with *expr* as its single
element. `makelist (expr, n)` creates a list of *n*
elements generated from *expr*.


The most general form, `makelist (expr, i, i_0, i_max, step)`, returns the list of elements obtained when
`ev (expr, i=j)` is applied to the elements
*j* of the sequence: *i_0*, *i_0* + *step*, *i_0* +
2**step*, ..., with *|j|* less than or equal to *|i_max|*.


The increment *step* can be a number (positive or negative) or an
expression. If it is omitted, the default value 1 will be used. If both
*i_0* and *step* are omitted, they will both have a default
value of 1.


`makelist (expr, x, list)` returns a list, the
`j`th element of which is equal to
`ev (expr, x=list[j])` for `j` equal to 1 through
`length (list)`.


Examples:











```maxima
(%i1) makelist (concat (x,i), i, 6);
(%o1)               [x1, x2, x3, x4, x5, x6]


(%i2) makelist (x=y, y, [a, b, c]);
(%o2)                 [x = a, x = b, x = c]


(%i3) makelist (x^2, x, 3, 2*%pi, 2);
(%o3)                        [9, 25]


(%i4) makelist (random(6), 4);
(%o4)                     [2, 0, 2, 5]


(%i5) flatten (makelist (makelist (i^2, 3), i, 4));
(%o5)        [1, 1, 1, 4, 4, 4, 9, 9, 9, 16, 16, 16]


(%i6) flatten (makelist (makelist (i^2, i, 3), 4));
(%o6)         [1, 4, 9, 1, 4, 9, 1, 4, 9, 1, 4, 9]
```

### Function: member (expr_1, expr_2)

Returns `true` if `is(expr_1 = a)`
for some element *a* in `args(expr_2)`,
otherwise returns `false`.


`expr_2` is typically a list, in which case
`args(expr_2) = expr_2` and `is(expr_1 = a)`
for some element *a* in `expr_2` is the test.


`member` does not inspect parts of the arguments of `expr_2`, so it
may return `false` even if `expr_1` is a part of some argument of
`expr_2`.


See also `elementp`.


Examples:













```maxima
(%i1) member (8, [8, 8.0, 8b0]);
(%o1)                         true


(%i2) member (8, [8.0, 8b0]);
(%o2)                         false


(%i3) member (b, [a, b, c]);
(%o3)                         true


(%i4) member (b, [[a, b], [b, c]]);
(%o4)                         false


(%i5) member ([b, c], [[a, b], [b, c]]);
(%o5)                         true


(%i6) F (1, 1/2, 1/4, 1/8);
                               1  1  1
(%o6)                     F(1, -, -, -)
                               2  4  8


(%i7) member (1/8, %);
(%o7)                         true


(%i8) member ("ab", ["aa", "ab", sin(1), a + b]);
(%o8)                         true
```

See also: `elementp`.

### Variable: minf

`minf` represents real minus (i.e., negative) infinity.

### Variable: most_negative_float

The most negative floating-point number in Maxima.  It is
approximately -1.79769e+308.

### Variable: most_positive_float

The most positive floating-point number in Maxima.  It is
approximately 1.797693e+308.

### Function: new (new, S, new, S, v_1, ..., v_n)

`new` creates new instances of structures.


`new(S)` creates a new instance of structure *S*
in which each field is assigned its default value, if any,
or no value at all if no default was specified in the structure definition.


`new(S(v_1, ..., v_n))` creates a new instance of *S*
in which fields are assigned the values *v_1*, ..., *v_n*.


Examples:








```maxima
(%i1) defstruct (foo (w, x = %e, y = 42, z));
(%o1)              [foo(w, x = %e, y = 42, z)]
(%i2) new (foo);
(%o2)               foo(w, x = %e, y = 42, z)
(%i3) new (foo (1, 2, 4, 8));
(%o3)            foo(w = 1, x = 2, y = 4, z = 8)
```

### Function: ninth (expr)

Returns the 9th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: ordering (ordering, L, ordering, L, P)

Returns a permutation *O* of the list *L* such that
`permute(O, L)` is equal to `sort(L, P)`.
That is, `ordering` returns a permutation
which sorts *L* according to the predicate *P*.


The sorting predicate *P* is optional;
if unspecified, it is assumed to be `orderlessp`.
All Maxima expressions are comparable under `orderlessp`.


When some elements are equivalent
(i.e., there exist elements `L[i]` and `L[j]`
such that `i` and `j` are different
and neither `P(L[i], L[j])` nor `P(L[j], L[i])`),
the permutation returned is the one which keeps equivalent elements
in the same order in which they occur in *L*.
When all of the elements of *L* are nonequivalent under the predicate *P*,
the permutation returned by `ordering` is unique.


Examples:


`ordering` returns a permutation
which sorts *L* according to the predicate *P*.










```maxima
maxima

(%i1) L: [ "abc", "Abc", "Bcd", "Bc", "bcd", "cde", "C", "B", "A" ];
(%o1)        [abc, Abc, Bcd, Bc, bcd, cde, C, B, A]


(%i2) O: ordering (L, 'slessp);
(%o2)              [9, 2, 8, 4, 3, 7, 1, 5, 6]


(%i3) permute (O, L);
(%o3)        [A, Abc, B, Bc, Bcd, C, abc, bcd, cde]


(%i4) sort (L, slessp);
(%o4)        [A, Abc, B, Bc, Bcd, C, abc, bcd, cde]


(%i5) is (permute (O, L) = sort (L, 'slessp));
(%o5)                         true
```


The sorting predicate *P* is optional;
if unspecified, it is assumed to be `orderlessp`.
All Maxima expressions are comparable under `orderlessp`.










```maxima
maxima

(%i1) L: [ "xyz", 1.5, 7.25, 1/3, 3.125, %pi, %e, 4/7, sin(x) ];
                          1                  4
(%o1)    [xyz, 1.5, 7.25, -, 3.125, %pi, %e, -, sin(x)]
                          3                  7


(%i2) sort (L);
          1  4
(%o2)    [-, -, 1.5, 3.125, 7.25, %e, %pi, xyz, sin(x)]
          3  7


(%i3) O: ordering (L);
(%o3)              [4, 8, 2, 5, 3, 7, 6, 1, 9]


(%i4) permute (O, L);
          1  4
(%o4)    [-, -, 1.5, 3.125, 7.25, %e, %pi, xyz, sin(x)]
          3  7


(%i5) is (permute (O, L) = sort (L));
(%o5)                         true
```


When some elements are equivalent under *P*,
the permutation returned is the one which keeps equivalent elements
in the same order in which they occur in *L*.












```maxima
maxima

(%i1) L1: [ "ABC", "aBc", "abC", "abc", "Abc" ];
(%o1)               [ABC, aBc, abC, abc, Abc]


(%i2) L2: [ "Xyz", "xyz", "XYZ", "xYz", "xyZ" ];
(%o2)               [Xyz, xyz, XYZ, xYz, xyZ]


(%i3) L: flatten (makelist ([ L1[i], L2[i] ], i, 1, 5));
(%o3)  [ABC, Xyz, aBc, xyz, abC, XYZ, abc, xYz, Abc, xyZ]


(%i4) sort (L, 'slesspignore);
(%o4)  [ABC, aBc, abC, abc, Abc, Xyz, xyz, XYZ, xYz, xyZ]


(%i5) O: ordering (L, 'slesspignore);
(%o5)            [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


(%i6) permute (O, L);
(%o6)  [ABC, aBc, abC, abc, Abc, Xyz, xyz, XYZ, xYz, xyZ]


(%i7) is (permute (O, L) = sort (L, 'slesspignore));
(%o7)                         true
```


When all of the elements of *L* are nonequivalent under the predicate *P*,
the permutation returned by `ordering` is unique.












```maxima
maxima

(%i1) L1: [ "ABC", "aBc", "abC", "abc", "Abc" ];
(%o1)               [ABC, aBc, abC, abc, Abc]


(%i2) L2: [ "Xyz", "xyz", "XYZ", "xYz", "xyZ" ];
(%o2)               [Xyz, xyz, XYZ, xYz, xyZ]


(%i3) L: flatten (makelist ([ L1[i], L2[i] ], i, 1, 5));
(%o3)  [ABC, Xyz, aBc, xyz, abC, XYZ, abc, xYz, Abc, xyZ]


(%i4) sort (L, 'slessp);
(%o4)  [ABC, Abc, XYZ, Xyz, aBc, abC, abc, xYz, xyZ, xyz]


(%i5) O: ordering (L, 'slessp);
(%o5)            [1, 9, 6, 2, 3, 5, 7, 8, 10, 4]


(%i6) permute (O, L);
(%o6)  [ABC, Abc, XYZ, Xyz, aBc, abC, abc, xYz, xyZ, xyz]


(%i7) is (permute (O, L) = sort (L, 'slessp));
(%o7)                         true
```

### Function: pop (list)

`pop` removes and returns the first element from the list *list*. The argument
*list* must be a mapatom that is bound to a nonempty list. If the argument *list* is 
not bound to a nonempty list, Maxima signals an error. For examples, see `push`.

See also: `push`.

### Function: push (item, list)

`push` prepends the item *item* to the list *list* and returns a copy of the new list. 
The second argument *list* must be a mapatom that is bound to a list. The first argument *item* 
can be any Maxima symbol or expression. If the argument *list* is not bound to a list, Maxima 
signals an error.



To remove the first item from a list, see `pop`.



Examples:














```maxima
(%i1) ll: [];
(%o1)                          []


(%i2) push (x, ll);
(%o2)                          [x]


(%i3) push (x^2+y, ll);
                                 2
(%o3)                      [y + x , x]


(%i4) a: push ("string", ll);
                                     2
(%o4)                  [string, y + x , x]


(%i5) pop (ll);
(%o5)                        string


(%i6) pop (ll);
                                  2
(%o6)                        y + x


(%i7) pop (ll);
(%o7)                           x


(%i8) ll;
(%o8)                          []


(%i9) a;
                                     2
(%o9)                  [string, y + x , x]
```

See also: `pop`.

### Function: ranks (ranks, L, P, ties_method, ranks, L, P, ranks, L)

Returns the ranks of the elements of the list *L* as ordered by the predicate *P*,
and handling elements which are equivalent under *P* by *ties_method*.


If *ties_method* is absent, `mean_rank` is assumed.
Note that if *ties_method* is present,
then *P* must also be present.


If *P* is absent, `orderlessp` is assumed.


Elements `L[i]` and `L[j]` are said to be equivalent under *P*
if neither `P(L[i], L[j])` nor `P(L[j], L[i])`.
An element `L[j]` is said to precede `L[i]` under *P*
if `P(L[j], L[i])`.


Let `m` be the number of elements equivalent to `L[i]`.
Let `n` be the number of elements preceding `L[i]`.
The rank of the `i`-th element is `n`
plus a term which accounts for equivalent elements as follows.



- *
`mean_rank` Rank is `n` plus `(m + 1)/2`.
- *
`min_rank` Rank is `n` plus 1.
- *
`max_rank` Rank is `n` plus `m`.
- *
`distinct_ranks` Let `L[j[1]], L[j[2]], ..., L[j[m]]` be the elements of *L*
which are equivalent to `L[i]`,
such that `j[1] < j[2] < ... < j[m]`.
That is, the equivalent elements are indexed in the order in which they appear in *L*.
Rank is `n` plus `k` where `j[k] = i`.


When `L[i]` is not equivalent to any other element,
all four methods yield the same result, namely `n` plus 1.


When no two elements of *L* are equivalent,
there are no ties,
and `ranks` returns the inverse permutation of `ordering`.


Examples:


`ranks` returns the ranks of the elements of the list *L* as ordered by the predicate *P*,
and handling elements which are equivalent under *P* by *ties_method*.
If not specified, *P* is assumed to be `orderlessp`,
and *ties_method* is assumed to be `mean_rank`.
Sort the list and inspect the ranks to see the effect of `mean_rank` more clearly.









```maxima
maxima

(%i1) L: [ sin(z), cos(y), tan(x), 1 - x, f(u), cos(y), g(a), 1/h, tanh(s), sin(z), 1 - x, sec(u) ];
                                                          1
(%o1) [sin(z), cos(y), tan(x), 1 - x, f(u), cos(y), g(a), -, 
                                                          h
                                  tanh(s), sin(z), 1 - x, sec(u)]


(%i2) L1: sort (L);
             1
(%o2) [g(a), -, tanh(s), f(u), sec(u), 1 - x, 1 - x, tan(x), 
             h
                                  cos(y), cos(y), sin(z), sin(z)]


(%i3) ranks (L1);
                           13  13     19  19  23  23
(%o3)      [1, 2, 3, 4, 5, --, --, 8, --, --, --, --]
                           2   2      2   2   2   2


(%i4) ranks (L);
            23  19     13     19           23  13
(%o4)      [--, --, 8, --, 4, --, 1, 2, 3, --, --, 5]
            2   2      2      2            2   2
```


*ties_method* is `mean_rank`.
Sort by `sgreaterp` so that `"aa"` has the highest rank.
Sort the list and inspect the ranks to see the effect of `mean_rank` more clearly.









```maxima
maxima

(%i1) L: [ "dd", "aa", "zz", "aa", "bb", "zz", "cc", "aa", "aa", "cc", "zz", "aa" ];
(%o1)   [dd, aa, zz, aa, bb, zz, cc, aa, aa, cc, zz, aa]


(%i2) L1: sort (L, 'sgreaterp);
(%o2)   [zz, zz, zz, dd, cc, cc, bb, aa, aa, aa, aa, aa]


(%i3) ranks (L1, 'sgreaterp, 'mean_rank);
                        11  11
(%o3)      [2, 2, 2, 4, --, --, 7, 10, 10, 10, 10, 10]
                        2   2


(%i4) ranks (L, 'sgreaterp, 'mean_rank);
                                11          11
(%o4)      [4, 10, 2, 10, 7, 2, --, 10, 10, --, 2, 10]
                                2           2
```


*ties_method* is `min_rank`.
Sort by `sgreaterp` so that `"aa"` has the highest rank.
Sort the list and inspect the ranks to see the effect of `min_rank` more clearly.









```maxima
maxima

(%i1) L: [ "dd", "aa", "zz", "aa", "bb", "zz", "cc", "aa", "aa", "cc", "zz", "aa" ];
(%o1)   [dd, aa, zz, aa, bb, zz, cc, aa, aa, cc, zz, aa]


(%i2) L1: sort (L, 'sgreaterp);
(%o2)   [zz, zz, zz, dd, cc, cc, bb, aa, aa, aa, aa, aa]


(%i3) ranks (L1, 'sgreaterp, 'min_rank);
(%o3)         [1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 8, 8]


(%i4) ranks (L, 'sgreaterp, 'min_rank);
(%o4)         [4, 8, 1, 8, 7, 1, 5, 8, 8, 5, 1, 8]
```


*ties_method* is `max_rank`.
Sort by `sgreaterp` so that `"aa"` has the highest rank.
Sort the list and inspect the ranks to see the effect of `max_rank` more clearly.









```maxima
maxima

(%i1) L: [ "dd", "aa", "zz", "aa", "bb", "zz", "cc", "aa", "aa", "cc", "zz", "aa" ];
(%o1)   [dd, aa, zz, aa, bb, zz, cc, aa, aa, cc, zz, aa]


(%i2) L1: sort (L, 'sgreaterp);
(%o2)   [zz, zz, zz, dd, cc, cc, bb, aa, aa, aa, aa, aa]


(%i3) ranks (L1, 'sgreaterp, 'max_rank);
(%o3)       [3, 3, 3, 4, 6, 6, 7, 12, 12, 12, 12, 12]


(%i4) ranks (L, 'sgreaterp, 'max_rank);
(%o4)       [4, 12, 3, 12, 7, 3, 6, 12, 12, 6, 3, 12]
```


*ties_method* is `distinct_ranks`.
Sort by `sgreaterp` so that `"aa"` has the highest rank.
Sort the list and inspect the ranks to see the effect of `distinct_ranks` more clearly.









```maxima
maxima

(%i1) L: [ "dd", "aa", "zz", "aa", "bb", "zz", "cc", "aa", "aa", "cc", "zz", "aa" ];
(%o1)   [dd, aa, zz, aa, bb, zz, cc, aa, aa, cc, zz, aa]


(%i2) L1: sort (L, 'sgreaterp);
(%o2)   [zz, zz, zz, dd, cc, cc, bb, aa, aa, aa, aa, aa]


(%i3) ranks (L1, 'sgreaterp, 'distinct_ranks);
(%o3)        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


(%i4) ranks (L, 'sgreaterp, 'distinct_ranks);
(%o4)        [4, 8, 1, 9, 7, 2, 5, 10, 11, 6, 3, 12]
```


When no two elements of *L* are equivalent,
there are no ties,
and `ranks` returns the inverse permutation of `ordering`.
Sort by `sgreaterp` so that `"ab"` has the highest rank.









```maxima
maxima

(%i1) L: [ "xyz", "z", "abc", "bc", "ab", "wyx", "tuvw", "ghi" ];
(%o1)         [xyz, z, abc, bc, ab, wyx, tuvw, ghi]


(%i2) R: ranks (L, 'sgreaterp);
(%o2)               [2, 1, 7, 6, 8, 3, 4, 5]


(%i3) O: ordering (L, 'sgreaterp);
(%o3)               [2, 1, 6, 7, 8, 4, 3, 5]


(%i4) is (R = perm_inverse (O));
(%o4)                         true
```

### Function: rearray (A, dim_1, ..., dim_n)

Changes the dimensions of an array.
The new array will be filled with the elements of the old one in
row-major order.  If the old array was too small, 
the remaining elements are filled with
`false`, `0.0` or `0`,
depending on the type of the array.  The type of the array cannot be
changed.

### Function: remarray (remarray, A_1, ..., A_n, remarray, all)

Removes arrays and array associated functions and frees the storage occupied.
The arguments may be declared arrays, `hashed arrays`, array
functions, and subscripted functions.


`remarray (all)` removes all items in the global list `arrays`.


It may be necessary to use this function if it is
desired to clear the cache of a `memoizing-function`.


`remarray` returns the list of arrays removed.


`remarray` quotes its arguments.

See also: `hashed-arrays`, `arrays`, `memoizing-function`.

### Function: rest (rest, expr, n, rest, expr)

Returns *expr* with its first *n* elements removed if *n*
is positive and its last `- n` elements removed if *n*
is negative. If *n* is 1 it may be omitted. The first argument
*expr* may be a list, matrix, or other expression. When *expr*
is an atom, `rest` signals an error; when *expr* is an empty
list and `partswitch` is false, `rest` signals an error. When 
*expr* is an empty list and `partswitch` is true, `rest` 
returns `end`.


Applying `rest` to expression such as `f(a,b,c)` returns
`f(b,c)`. In general, applying `rest` to a nonlist doesn’t
make sense. For example, because ’^’ requires two arguments,
`rest(a^b)` results in an error message. The functions
`args` and `op` may be useful as well, since `args(a^b)`
returns `[a,b]` and `op(a^b)` returns ^.


See also `firstn` and `lastn`.



```maxima
(%i1) rest(a+b+c);
(%o1) b+a
(%i2) rest(a+b+c,2);
(%o2) a
(%i3) rest(a+b+c,-2);
(%o3) c
```

See also: `firstn`, `lastn`.

### Function: reverse (list)

Reverses the order of the members of the *list* (not
the members themselves).  `reverse` also works on general expressions,
e.g.  `reverse(a=b);` gives `b=a`.


See also `sreverse`.

See also: `sreverse`.

### Function: rreduce (rreduce, F, s, rreduce, F, s, s_{n + 1})

Extends the binary function *F* to an n-ary function by composition,
where *s* is a list.


`rreduce(F, s)` returns `F(s_1, ... F(s_{n - 2}, F(s_{n - 1}, s_n)))`.
When the optional argument *s_{n + 1}* is present,
the result is equivalent to `rreduce(F, endcons(s_{n + 1}, s))`.


The function *F* is first applied to the
*rightmost* list elements, thus the name "rreduce".


See also `lreduce`, `tree_reduce`, and `xreduce`.


Examples:


`rreduce` without the optional argument.







```maxima
(%i1) rreduce (f, [1, 2, 3]);
(%o1)                     f(1, f(2, 3))


(%i2) rreduce (f, [1, 2, 3, 4]);
(%o2)                  f(1, f(2, f(3, 4)))
```


`rreduce` with the optional argument.






```maxima
(%i1) rreduce (f, [1, 2, 3], 4);
(%o1)                  f(1, f(2, f(3, 4)))
```


`rreduce` applied to built-in binary operators.
`/` is the division operator.







```maxima
(%i1) rreduce ("^", [a, b, c, d]);
                                 d
                                c
                               b
(%o1)                         a


(%i2) rreduce ("/", [a, b, c, d]);
                               a c
(%o2)                          ---
                               b d
```

See also: `lreduce`, `tree_reduce`, `xreduce`.

### Function: second (expr)

Returns the 2nd item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: seventh (expr)

Returns the 7th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: sixth (expr)

Returns the 6th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: sort (sort, L, P, sort, L)

`sort(L, P)` sorts a list *L* according to a predicate `P` of two arguments
which defines a strict weak order on the elements of *L*.
If `P(a, b)` is `true`, then `a` appears before `b` in the result.
If neither `P(a, b)` nor `P(b, a)` are `true`,
then `a` and `b` are equivalent, and appear in the result in the same order as in the input.
That is, `sort` is a stable sort.


If `P(a, b)` and `P(b, a)` are both `true` for some elements of *L*,
then *P* is not a valid sort predicate, and the result is undefined.
If `P(a, b)` is something other than `true` or `false`, `sort` signals an error.


The predicate may be specified as the name of a function 
or binary infix operator, or as a `lambda` expression.  If specified as
the name of an operator, the name must be enclosed in double quotes.


The sorted list is returned as a new object; the argument *L* is not modified.


`sort(L)` is equivalent to `sort(L, orderlessp)`.


The default sorting order is ascending, as determined by `orderlessp`. The predicate `ordergreatp` sorts a list in descending order.


All Maxima atoms and expressions are comparable under `orderlessp` and `ordergreatp`.


Operators `<` and `>` order numbers, constants, and constant expressions by magnitude.
Note that `orderlessp` and `ordergreatp` do not order numbers, constants, and constant expressions by magnitude.


`ordermagnitudep` orders numbers, constants, and constant expressions the same as `<`,
and all other elements the same as `orderlessp`.


Examples:


`sort` sorts a list according to a predicate of two arguments
which defines a strict weak order on the elements of the list.







```maxima
(%i1) sort ([1, a, b, 2, 3, c], 'orderlessp);
(%o1)                  [1, 2, 3, a, b, c]


(%i2) sort ([1, a, b, 2, 3, c], 'ordergreatp);
(%o2)                  [c, b, a, 3, 2, 1]
```


The predicate may be specified as the name of a function 
or binary infix operator, or as a `lambda` expression.  If specified as
the name of an operator, the name must be enclosed in double quotes.












```maxima
(%i1) L : [[1, x], [3, y], [4, w], [2, z]];
(%o1)           [[1, x], [3, y], [4, w], [2, z]]


(%i2) foo (a, b) := a[1] > b[1];
(%o2)                 foo(a, b) := a  > b
                                    1    1


(%i3) sort (L, 'foo);
(%o3)           [[4, w], [3, y], [2, z], [1, x]]


(%i4) infix (">>");
(%o4)                          >>


(%i5) a >> b := a[1] > b[1];
(%o5)                  (a >> b) := a  > b
                                    1    1


(%i6) sort (L, ">>");
(%o6)           [[4, w], [3, y], [2, z], [1, x]]


(%i7) sort (L, lambda ([a, b], a[1] > b[1]));
(%o7)           [[4, w], [3, y], [2, z], [1, x]]
```


`sort(L)` is equivalent to `sort(L, orderlessp)`.








```maxima
(%i1) L : [a, 2*b, -5, 7, 1 + %e, %pi];
(%o1)             [a, 2 b, - 5, 7, %e + 1, %pi]


(%i2) sort (L);
(%o2)             [- 5, 7, %e + 1, %pi, a, 2 b]


(%i3) sort (L, 'orderlessp);
(%o3)             [- 5, 7, %e + 1, %pi, a, 2 b]
```


The default sorting order is ascending, as determined by `orderlessp`. The predicate `ordergreatp` sorts a list in descending order.








```maxima
(%i1) L : [a, 2*b, -5, 7, 1 + %e, %pi];
(%o1)             [a, 2 b, - 5, 7, %e + 1, %pi]


(%i2) sort (L);
(%o2)             [- 5, 7, %e + 1, %pi, a, 2 b]


(%i3) sort (L, 'ordergreatp);
(%o3)             [2 b, a, %pi, %e + 1, 7, - 5]
```


All Maxima atoms and expressions are comparable under `orderlessp` and `ordergreatp`.








```maxima
(%i1) L : [11, -17, 29b0, 9*c, 7.55, foo(x, y), -5/2, b + a];
                                                 5
(%o1)  [11, - 17, 2.9b1, 9 c, 7.55, foo(x, y), - -, b + a]
                                                 2


(%i2) sort (L, orderlessp);
                5
(%o2)  [- 17, - -, 7.55, 11, 2.9b1, b + a, 9 c, foo(x, y)]
                2


(%i3) sort (L, ordergreatp);
                                                  5
(%o3)  [foo(x, y), 9 c, b + a, 2.9b1, 11, 7.55, - -, - 17]
                                                  2
```


Operators `<` and `>` order numbers, constants, and constant expressions by magnitude.
Note that `orderlessp` and `ordergreatp` do not order numbers, constants, and constant expressions by magnitude.








```maxima
(%i1) L : [%pi, 3, 4, %e, %gamma];
(%o1)                [%pi, 3, 4, %e, %gamma]


(%i2) sort (L, ">");
(%o2)                [4, %pi, 3, %e, %gamma]


(%i3) sort (L, ordergreatp);
(%o3)                [%pi, %gamma, %e, 4, 3]
```


`ordermagnitudep` orders numbers, constants, and constant expressions the same as `<`,
and all other elements the same as `orderlessp`.








```maxima
(%i1) L: [%i, 1+%i, 2*x, minf, inf, %e, sin(1), 0, 1,2,3, 1.0, 1.0b0];
(%o1) [%i, %i + 1, 2 x, minf, inf, %e, sin(1), 0, 1, 2, 3, 1.0, 
                                                           1.0b0]


(%i2) sort (L, ordermagnitudep);
(%o2) [minf, 0, sin(1), 1, 1.0, 1.0b0, 2, %e, 3, inf, %i, 
                                                     %i + 1, 2 x]


(%i3) sort (L, orderlessp);
(%o3) [0, 1, 1.0, 2, 3, sin(1), 1.0b0, %e, %i, %i + 1, inf, 
                                                       minf, 2 x]
```

See also: `orderlessp`.

### Variable: structures

`structures` is the list of user-defined structures defined by `defstruct`.

### Function: sublist (list, p)

Returns the list of elements of *list* for which the predicate `p`
returns `true`.


Example:







```maxima
(%i1) L: [1, 2, 3, 4, 5, 6];
(%o1)                  [1, 2, 3, 4, 5, 6]


(%i2) sublist (L, evenp);
(%o2)                       [2, 4, 6]
```

### Function: sublist_indices (L, P)

Returns the indices of the elements `x` of the list *L* for which
the predicate `maybe(P(x))` returns `true`;
this excludes `unknown` as well as `false`.
*P* may be the name of a function or a lambda expression.
*L* must be a literal list.


Examples:













```maxima
(%i1) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b],
                       lambda ([x], x='b));
(%o1)                     [2, 3, 7, 9]


(%i2) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b], symbolp);
(%o2)                  [1, 2, 3, 4, 7, 9]


(%i3) sublist_indices ([1 > 0, 1 < 0, 2 < 1, 2 > 1, 2 > 0],
                       identity);
(%o3)                       [1, 4, 5]


(%i4) assume (x < -1);
(%o4)                       [x < - 1]


(%i5) map (maybe, [x > 0, x < 0, x < -2]);
(%o5)                [false, true, unknown]


(%i6) sublist_indices ([x > 0, x < 0, x < -2], identity);
(%o6)                          [2]
```

### Function: subvar (x, i)

Evaluates the subscripted expression `x[i]`.


`subvar` evaluates its arguments.


`arraymake (x, [i])` constructs the expression
`x[i]`, but does not evaluate it.


Examples:












```maxima
(%i1) x : foo $
(%i2) i : 3 $

(%i3) subvar (x, i);
(%o3)                         foo
                                 3

(%i4) foo : [aa, bb, cc, dd, ee]$

(%i5) subvar (x, i);
(%o5)                          cc


(%i6) arraymake (x, [i]);
(%o6)                         foo
                                 3


(%i7) ''%;
(%o7)                          cc
```

### Function: subvarp (expr)

Returns `true` if *expr* is a subscripted variable, for example
`a[i]`.

### Function: tenth (expr)

Returns the 10th item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Function: third (expr)

Returns the 3rd item of expression or list *expr*.
See `first` for more details.

See also: `first`.

### Variable: translate_fast_arrays

Default value: `false`


When `translate_fast_arrays` is `true`,
the Maxima-to-Lisp translator generates code that assumes arrays are values instead of properties,
as if `use_fast_arrays` were `true`.


When `translate_fast_arrays` is `false`,
the Maxima-to-Lisp translator generates code that assumes arrays are properties,
as if `use_fast_arrays` were `false`.

### Function: tree_reduce (tree_reduce, F, s, tree_reduce, F, s, s_0)

Extends the binary function *F* to an n-ary function by composition,
where *s* is a set or list.


`tree_reduce` is equivalent to the following:
Apply *F* to successive pairs of elements
to form a new list `[F(s_1, s_2), F(s_3, s_4), ...]`,
carrying the final element unchanged if there are an odd number of elements.
Then repeat until the list is reduced to a single element, which is the return value.


When the optional argument *s_0* is present,
the result is equivalent `tree_reduce(F, cons(s_0, s))`.


For addition of floating point numbers,
`tree_reduce` may return a sum that has a smaller rounding error
than either `rreduce` or `lreduce`.


The elements of *s* and the partial results may be arranged in a minimum-depth binary tree,
thus the name "tree_reduce".


Examples:


`tree_reduce` applied to a list with an even number of elements.






```maxima
(%i1) tree_reduce (f, [a, b, c, d]);
(%o1)                  f(f(a, b), f(c, d))
```


`tree_reduce` applied to a list with an odd number of elements.






```maxima
(%i1) tree_reduce (f, [a, b, c, d, e]);
(%o1)               f(f(f(a, b), f(c, d)), e)
```

### Variable: true

`true` represents the Boolean constant of the same name.
Maxima implements `true` by the value `T` in Lisp.

### Variable: und

`und` represents an undefined result.


See also `limit`.


Example:






```maxima
(%i1) limit (x*sin(x), x, inf);
(%o1)                          und
```

See also: `limit`.

### Function: unique (L)

Returns the unique elements of the list *L*.


When all the elements of *L* are unique,
`unique` returns a shallow copy of *L*,
not *L* itself.


If *L* is not a list, `unique` returns *L*.


Example:






```maxima
(%i1) unique ([1, %pi, a + b, 2, 1, %e, %pi, a + b, [1]]);
(%o1)              [1, 2, %e, %pi, [1], b + a]
```

### Variable: use_fast_arrays

Default value: `false`


When `use_fast_arrays` is `true`,
arrays declared by `array` are values instead of properties,
and undeclared arrays (`hashed arrays`) are implemented as Lisp hashed arrays.


When `use_fast_arrays` is `false`,
arrays declared by `array` are properties,
and undeclared arrays are implemented with Maxima’s own hashed array implementation.


Note that the code `use_fast_arrays` switches to is not necessarily faster
than the default one; Arrays created by `make_array` are not affected by
`use_fast_arrays`.


See also `translate_005ffast_005farrays`.

See also: `hashed-arrays`, `make_array`, `translate_fast_arrays`.

### Function: xreduce (xreduce, F, s, xreduce, F, s, s_0)

Extends the function *F* to an n-ary function by composition,
or, if *F* is already n-ary, applies *F* to *s*.
When *F* is not n-ary, `xreduce` is the same as `lreduce`.
The argument *s* is a list.


Functions known to be n-ary include
addition `+`, multiplication `*`, `and`, `or`, `max`,
`min`, and `append`.
Functions may also be declared n-ary by `declare(F, nary)`.
For these functions,
`xreduce` is expected to be faster than either `rreduce` or `lreduce`.


When the optional argument *s_0* is present,
the result is equivalent to `xreduce(s, cons(s_0, s))`.




Floating point addition is not exactly associative; be that as it may,
`xreduce` applies Maxima’s n-ary addition when *s* contains floating point numbers.


Examples:


`xreduce` applied to a function known to be n-ary.
`F` is called once, with all arguments.








```maxima
(%i1) declare (F, nary);
(%o1)                         done


(%i2) F ([L]) := L;
(%o2)                      F([L]) := L


(%i3) xreduce (F, [a, b, c, d, e]);
(%o3)                    [a, b, c, d, e]
```


`xreduce` applied to a function not known to be n-ary.
`G` is called several times, with two arguments each time.








```maxima
(%i1) G ([L]) := L;
(%o1)                      G([L]) := L


(%i2) xreduce (G, [a, b, c, d, e]);
(%o2)                 [[[[a, b], c], d], e]


(%i3) lreduce (G, [a, b, c, d, e]);
(%o3)                 [[[[a, b], c], d], e]
```

### Variable: zeroa

`zeroa` represents an infinitesimal above zero.  `zeroa` can be used
in expressions.  `limit` simplifies expressions which contain
infinitesimals.


See also `zerob` and `limit`.


Example:


`limit` simplifies expressions which contain infinitesimals:







```maxima
(%i1) limit(zeroa);
(%o1)                           0


(%i2) limit(zeroa+x);
(%o2)                           x
```

See also: `zerob`, `limit`.

### Variable: zerob

`zerob` represents an infinitesimal below zero.  `zerob` can be used
in expressions.  `limit` simplifies expressions which contain
infinitesimals.


See also `zeroa` and `limit`.

See also: `zeroa`, `limit`.

