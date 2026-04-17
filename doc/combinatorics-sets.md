## Sets

<!-- category: Combinatorics -->
<!-- keywords: adjoin -->
<!-- signatures: adjoin(x, a) -->
### Function: adjoin (x, a)

Returns the union of the set *a* with `{x}`.


`adjoin` complains if *a* is not a literal set.


`adjoin(x, a)` and `union(set(x), a)`
are equivalent;
however, `adjoin` may be somewhat faster than `union`.


See also `disjoin`.


Examples:







```maxima
maxima

(%i1) adjoin (c, {a, b});
(%o1)                       {a, b, c}


(%i2) adjoin (a, {a, b});
(%o2)                        {a, b}
```

See also: `disjoin`.

<!-- category: Combinatorics -->
<!-- keywords: belln -->
<!-- signatures: belln(n) -->
### Function: belln (n)

Represents the $n$-th Bell number.
`belln(n)` is the number of partitions of a set with *n* members.


For nonnegative integers *n*,
`belln(n)` simplifies to the $n$-th Bell number.
`belln` does not simplify for any other arguments.


`belln` distributes over equations, lists, matrices, and sets.


Examples:


`belln` applied to nonnegative integers.









```maxima
maxima

(%i1) makelist (belln (i), i, 0, 6);
(%o1)               [1, 1, 2, 5, 15, 52, 203]


(%i2) is (cardinality (set_partitions ({})) = belln (0));
(%o2)                         true


(%i3) is (cardinality (set_partitions ({1, 2, 3, 4, 5, 6})) =
                       belln (6));
(%o3)                         true
```


`belln` applied to arguments which are not nonnegative integers.






```maxima
maxima

(%i1) [belln (x), belln (sqrt(3)), belln (-9)];
(%o1)        [belln(x), belln(sqrt(3)), belln(- 9)]
```

<!-- category: Combinatorics -->
<!-- keywords: cardinality -->
<!-- signatures: cardinality(a) -->
### Function: cardinality (a)

Returns the number of distinct elements of the set *a*. 


`cardinality` ignores redundant elements
even when simplification is disabled.


Examples:









```maxima
maxima

(%i1) cardinality ({});
(%o1)                           0


(%i2) cardinality ({a, a, b, c});
(%o2)                           3


(%i3) simp : false;
(%o3)                         false


(%i4) cardinality ({a, a, b, c});
(%o4)                           3
```

<!-- category: Combinatorics -->
<!-- keywords: cartesian_product -->
<!-- signatures: cartesian_product(b_1, ..., b_n) -->
### Function: cartesian_product (b_1, ..., b_n)

Returns a set of lists of the form `[x_1, ..., x_n]`, where
*x_1*, ..., *x_n* are elements of the sets *b_1*, ... , *b_n*,
respectively.


`cartesian_product` complains if any argument is not a literal set.


See also `cartesian_005fproduct_005flist`.


Examples:









```maxima
maxima

(%i1) cartesian_product ({0, 1});
(%o1)                      {[0], [1]}


(%i2) cartesian_product ({0, 1}, {0, 1});
(%o2)           {[0, 0], [0, 1], [1, 0], [1, 1]}


(%i3) cartesian_product ({x}, {y}, {z});
(%o3)                      {[x, y, z]}


(%i4) cartesian_product ({x}, {-1, 0, 1});
(%o4)              {[x, - 1], [x, 0], [x, 1]}
```

See also: `cartesian_product_list`.

<!-- category: Combinatorics -->
<!-- keywords: cartesian_product_list -->
<!-- signatures: cartesian_product_list(b_1, ..., b_n) -->
### Function: cartesian_product_list (b_1, ..., b_n)

Returns a list of lists of the form `[x_1, ..., x_n]`, where
*x_1*, ..., *x_n* are elements of the lists *b_1*, ... , *b_n*, respectively,
comprising all possible combinations of the elements of *b_1*, ... , *b_n*.


The list returned by `cartesian_product_list` is equivalent to the
following recursive definition.
Let *L* be the list returned by `cartesian_product_list(b_2, ..., b_n)`.
Then `cartesian_product_list(b_1, b_2, ..., b_n)`
(i.e., *b_1* in addition to *b_2*, ..., *b_n*)
returns a list comprising each element of *L* appended to the first element of *b_1*,
each element of *L* appended to the second element of *b_1*,
each element of *L* appended to the third element of *b_1*, etc.
The order of the list returned by `cartesian_product_list(b_1, b_2, ..., b_n)`
may therefore be summarized by saying the lesser indices (1, 2, 3, ...) vary more slowly than the greater indices.


The list returned by `cartesian_product_list` contains duplicate elements
if any argument *b_1*, ..., *b_n* contains duplicates.
In this respect, `cartesian_product_list` differs from `cartesian_product`,
which returns no duplicates.
Also, the ordering of the list returned `cartesian_product_list`
is determined by the order of the elements of *b_1*, ..., *b_n*.
Again, this differs from `cartesian_product`,
which returns a set (with order determined by `orderlessp`).


The length of the list returned by `cartesian_product_list`
is equal to the product of the lengths of the arguments *b_1*, ..., *b_n*.


See also `cartesian_005fproduct`.


`cartesian_product_list` complains if any argument is not a list.


Examples:


`cartesian_product_list` returns a list of lists comprising all possible combinations.










```maxima
maxima

(%i1) cartesian_product_list ([0, 1]);
(%o1)                      [[0], [1]]


(%i2) cartesian_product_list ([0, 1], [0, 1]);
(%o2)           [[0, 0], [0, 1], [1, 0], [1, 1]]


(%i3) cartesian_product_list ([x], [y], [z]);
(%o3)                      [[x, y, z]]


(%i4) cartesian_product_list ([x], [-1, 0, 1]);
(%o4)              [[x, - 1], [x, 0], [x, 1]]


(%i5) cartesian_product_list ([a, h, e], [c, b, 4]);
(%o5) [[a, c], [a, b], [a, 4], [h, c], [h, b], [h, 4], [e, c], 
                                                  [e, b], [e, 4]]
```


The order of the list returned by `cartesian_product_list`
may be summarized by saying the lesser indices vary more slowly than the greater indices.






```maxima
maxima

(%i1) cartesian_product_list ([1, 2, 3], [a, b], [i, ii]);
(%o1) [[1, a, i], [1, a, ii], [1, b, i], [1, b, ii], [2, a, i], 
[2, a, ii], [2, b, i], [2, b, ii], [3, a, i], [3, a, ii], 
[3, b, i], [3, b, ii]]
```


The list returned by `cartesian_product_list` contains duplicate elements
if any argument contains duplicates.






```maxima
maxima

(%i1) cartesian_product_list ([e, h], [3, 7, 3]);
(%o1)   [[e, 3], [e, 7], [e, 3], [h, 3], [h, 7], [h, 3]]
```


The length of the list returned by `cartesian_product_list`
is equal to the product of the lengths of the arguments.







```maxima
maxima

(%i1) foo: cartesian_product_list ([1, 1, 2, 2, 3], [h, z, h]);
(%o1) [[1, h], [1, z], [1, h], [1, h], [1, z], [1, h], [2, h], 
  [2, z], [2, h], [2, h], [2, z], [2, h], [3, h], [3, z], [3, h]]


(%i2) is (length (foo) = 5*3);
(%o2)                         true
```

See also: `cartesian_product`.

<!-- category: Combinatorics -->
<!-- keywords: disjoin -->
<!-- signatures: disjoin(x, a) -->
### Function: disjoin (x, a)

Returns the set *a* without the member *x*.
If *x* is not a member of *a*, return *a* unchanged.


`disjoin` complains if *a* is not a literal set.


`disjoin(x, a)`, `delete(x, a)`, and
`setdifference(a, set(x))` are all equivalent. 
Of these, `disjoin` is generally faster than the others.


Examples:








```maxima
maxima

(%i1) disjoin (a, {a, b, c, d});
(%o1)                       {b, c, d}


(%i2) disjoin (a + b, {5, z, a + b, %pi});
(%o2)                      {5, %pi, z}


(%i3) disjoin (a - b, {5, z, a + b, %pi});
(%o3)                  {5, %pi, b + a, z}
```

<!-- category: Combinatorics -->
<!-- keywords: disjointp -->
<!-- signatures: disjointp(a, b) -->
### Function: disjointp (a, b)

Returns `true` if and only if the sets *a* and *b* are disjoint.


`disjointp` complains if either *a* or *b* is not a literal set.


Examples:







```maxima
maxima

(%i1) disjointp ({a, b, c}, {1, 2, 3});
(%o1)                         true


(%i2) disjointp ({a, b, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: divisors -->
<!-- signatures: divisors(n) -->
### Function: divisors (n)

Represents the set of divisors of *n*.


`divisors(n)` simplifies to a set of integers
when *n* is a nonzero integer.
The set of divisors includes the members 1 and *n*.
The divisors of a negative integer are the divisors of its absolute value.


`divisors` distributes over equations, lists, matrices, and sets.


Examples:


We can verify that 28 is a perfect number:
the sum of its divisors (except for itself) is 28.







```maxima
maxima

(%i1) s: divisors(28);
(%o1)                 {1, 2, 4, 7, 14, 28}


(%i2) lreduce ("+", args(s)) - 28;
(%o2)                          28
```


`divisors` is a simplifying function.
Substituting 8 for `a` in `divisors(a)`
yields the divisors without reevaluating `divisors(8)`.







```maxima
maxima

(%i1) divisors (a);
(%o1)                      divisors(a)


(%i2) subst (8, a, %);
(%o2)                     {1, 2, 4, 8}
```


`divisors` distributes over equations, lists, matrices, and sets.









```maxima
maxima

(%i1) divisors (a = b);
(%o1)               divisors(a) = divisors(b)


(%i2) divisors ([a, b, c]);
(%o2)        [divisors(a), divisors(b), divisors(c)]


(%i3) divisors (matrix ([a, b], [c, d]));
                  [ divisors(a)  divisors(b) ]
(%o3)             [                          ]
                  [ divisors(c)  divisors(d) ]


(%i4) divisors ({a, b, c});
(%o4)        {divisors(a), divisors(b), divisors(c)}
```

<!-- category: Combinatorics -->
<!-- keywords: elementp -->
<!-- signatures: elementp(x, a) -->
### Function: elementp (x, a)

Returns `true` if and only if *x* is a member of the 
set *a*.


`elementp` complains if *a* is not a literal set.


Examples:







```maxima
maxima

(%i1) elementp (sin(1), {sin(1), sin(2), sin(3)});
(%o1)                         true


(%i2) elementp (sin(1), {cos(1), cos(2), cos(3)});
(%o2)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: emptyp -->
<!-- signatures: emptyp(a) -->
### Function: emptyp (a)

Return `true` if and only if *a* is the empty set or
the empty list.


Examples:







```maxima
maxima

(%i1) map (emptyp, [{}, []]);
(%o1)                     [true, true]


(%i2) map (emptyp, [a + b, {{}}, %pi]);
(%o2)                 [false, false, false]
```

<!-- category: Combinatorics -->
<!-- keywords: equiv_classes -->
<!-- signatures: equiv_classes(s, F) -->
### Function: equiv_classes (s, F)

Returns a set of the equivalence classes of the set *s* with respect
to the equivalence relation *F*.


*F* is a function of two variables defined on the Cartesian product of *s* with *s*.
The return value of *F* is either `true` or `false`,
or an expression *expr* such that `is(expr)` is either `true` or `false`.


When *F* is not an equivalence relation,
`equiv_classes` accepts it without complaint,
but the result is generally incorrect in that case.







Examples:


The equivalence relation is a lambda expression which returns `true` or `false`.







```maxima
maxima

(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0},
                        lambda ([x, y], is (equal (x, y))));
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


The equivalence relation is the name of a relational function
which `is` evaluates to `true` or `false`.






```maxima
maxima

(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0}, equal);
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


The equivalence classes are numbers which differ by a multiple of 3.







```maxima
maxima

(%i1) equiv_classes ({1, 2, 3, 4, 5, 6, 7},
                     lambda ([x, y], remainder (x - y, 3) = 0));
(%o1)              {{1, 4, 7}, {2, 5}, {3, 6}}
```

<!-- category: Combinatorics -->
<!-- keywords: every -->
<!-- signatures: every(f, s), every(f, L_1, ..., L_n) -->
### Function: every (f, s)

Returns `true` if the predicate *f* is `true` for all given arguments.


Given one set as the second argument, 
`every(f, s)` returns `true`
if `is(f(a_i))` returns `true` for all *a_i* in *s*.
`every` may or may not evaluate *f* for all *a_i* in *s*.
Since sets are unordered,
`every` may evaluate `f(a_i)` in any order.


Given one or more lists as arguments,
`every(f, L_1, ..., L_n)` returns `true`
if `is(f(x_1, ..., x_n))` returns `true` 
for all *x_1*, ..., *x_n* in *L_1*, ..., *L_n*, respectively.
`every` may or may not evaluate 
*f* for every combination *x_1*, ..., *x_n*.
`every` evaluates lists in the order of increasing index.


Given an empty set `{}` or empty lists `[]` as arguments,
`every` returns `true`.


When the global flag `maperror` is `true`, all lists 
*L_1*, ..., *L_n* must have equal lengths.
When `maperror` is `false`, list arguments are
effectively truncated to the length of the shortest list. 


Return values of the predicate *f* which evaluate (via `is`)
to something other than `true` or `false`
are governed by the global flag `prederror`.
When `prederror` is `true`,
such values are treated as `false`,
and the return value from `every` is `false`.
When `prederror` is `false`,
such values are treated as `unknown`,
and the return value from `every` is `unknown`.


Examples:


`every` applied to a single set.
The predicate is a function of one argument.







```maxima
maxima

(%i1) every (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true


(%i2) every (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         false
```


`every` applied to two lists.
The predicate is a function of two arguments.







```maxima
maxima

(%i1) every ("=", [a, b, c], [a, b, c]);
(%o1)                         true


(%i2) every ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Return values of the predicate *f* which evaluate
to something other than `true` or `false`
are governed by the global flag `prederror`.











```maxima
maxima

(%i1) prederror : false;
(%o1)                         false


(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
                   [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]


(%i3) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown


(%i4) prederror : true;
(%o4)                         true


(%i5) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o5)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: extremal_subset -->
<!-- signatures: extremal_subset(s, f, max), extremal_subset(s, f, min) -->
### Function: extremal_subset (s, f, max)

Returns the subset of *s* for which the function *f* takes on maximum or minimum values.


`extremal_subset(s, f, max)` returns the subset of the set or 
list *s* for which the real-valued function *f* takes on its maximum value.


`extremal_subset(s, f, min)` returns the subset of the set or 
list *s* for which the real-valued function *f* takes on its minimum value.


Examples:







```maxima
maxima

(%i1) extremal_subset ({-2, -1, 0, 1, 2}, abs, max);
(%o1)                       {- 2, 2}


(%i2) extremal_subset ({sqrt(2), 1.57, %pi/2}, sin, min);
(%o2)                       {sqrt(2)}
```

<!-- category: Combinatorics -->
<!-- keywords: flatten -->
<!-- signatures: flatten(expr) -->
### Function: flatten (expr)

Collects arguments of subexpressions which have the same operator as *expr*
and constructs an expression from these collected arguments.


Subexpressions in which the operator is different from the main operator of `expr`
are copied without modification,
even if they, in turn, contain some subexpressions in which the operator is the same as for `expr`.


It may be possible for `flatten` to construct expressions in which the number
of arguments differs from the declared arguments for an operator;
this may provoke an error message from the simplifier or evaluator.
`flatten` does not try to detect such situations.


Expressions with special representations, for example, canonical rational expressions (CRE), 
cannot be flattened; in such cases, `flatten` returns its argument unchanged.


Examples:


Applied to a list, `flatten` gathers all list elements that are lists.






```maxima
maxima

(%i1) flatten ([a, b, [c, [d, e], f], [[g, h]], i, j]);
(%o1)            [a, b, c, d, e, f, g, h, i, j]
```


Applied to a set, `flatten` gathers all members of set elements that are sets.







```maxima
maxima

(%i1) flatten ({a, {b}, {{c}}});
(%o1)                       {a, b, c}


(%i2) flatten ({a, {[a], {a}}});
(%o2)                       {a, [a]}
```


`flatten` is similar to the effect of declaring the main operator n-ary.
However, `flatten` has no effect on subexpressions which have an operator
different from the main operator, while an n-ary declaration affects those.








```maxima
maxima

(%i1) expr: flatten (f (g (f (f (x)))));
(%o1)                     f(g(f(f(x))))


(%i2) declare (f, nary);
(%o2)                         done


(%i3) ev (expr);
(%o3)                     f(g(f(f(x))))
```


`flatten` treats subscripted functions the same as any other operator.






```maxima
maxima

(%i1) flatten (f[5] (f[5] (x, y), z));
(%o1)                      f (x, y, z)
                            5
```


It may be possible for `flatten` to construct expressions in which the number
of arguments differs from the declared arguments for an operator;







mod: expected exactly 2 arguments but got 3: [5, 7, 4]
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) 'mod (5, 'mod (7, 4));
(%o1)                   mod(5, mod(7, 4))


(%i2) flatten (%);
(%o2)                     mod(5, 7, 4)

(%i3) ''%, nouns;
```

<!-- category: Combinatorics -->
<!-- keywords: full_listify -->
<!-- signatures: full_listify(a) -->
### Function: full_listify (a)

Replaces every set operator in *a* by a list operator,
and returns the result.
`full_listify` replaces set operators in nested subexpressions,
even if the main operator is not `set`.


`listify` replaces only the main operator.


Examples:







```maxima
maxima

(%i1) full_listify ({a, b, {c, {d, e, f}, g}});
(%o1)               [a, b, [c, [d, e, f], g]]


(%i2) full_listify (F (G ({a, b, H({c, d, e})})));
(%o2)              F(G([a, b, H([c, d, e])]))
```

<!-- category: Combinatorics -->
<!-- keywords: fullsetify -->
<!-- signatures: fullsetify(a) -->
### Function: fullsetify (a)

When *a* is a list, replaces the list operator with a set operator,
and applies `fullsetify` to each member which is a set.
When *a* is not a list, it is returned unchanged.


`setify` replaces only the main operator.


Examples:


In line `(%o2)`, the argument of `f` isn’t converted to a set
because the main operator of `f([b])` isn’t a list.







```maxima
maxima

(%i1) fullsetify ([a, [a]]);
(%o1)                       {a, {a}}


(%i2) fullsetify ([a, f([b])]);
(%o2)                      {a, f([b])}
```

<!-- category: Combinatorics -->
<!-- keywords: identity -->
<!-- signatures: identity(x) -->
### Function: identity (x)

Returns *x* for any argument *x*.


Examples:


`identity` may be used as a predicate when the arguments
are already Boolean values.






```maxima
maxima

(%i1) every (identity, [true, true]);
(%o1)                         true
```

<!-- category: Combinatorics -->
<!-- keywords: integer_partitions -->
<!-- signatures: integer_partitions(n), integer_partitions(n, len) -->
### Function: integer_partitions (n)

Returns integer partitions of *n*, that is,
lists of integers which sum to *n*.


`integer_partitions(n)` returns the set of
all partitions of the integer *n*.
Each partition is a list sorted from greatest to least.


`integer_partitions(n, len)`
returns all partitions that have length *len* or less; in this
case, zeros are appended to each partition with fewer than *len*
terms to make each partition have exactly *len* terms.
Each partition is a list sorted from greatest to least.


A list $[a_1, ..., a_m]$ is a partition of a nonnegative integer
$n$ when (1) each $a_i$ is a nonzero integer, and (2) 
$a_1 + ... + a_m = n.$ Thus 0 has no partitions.


Examples:











```maxima
maxima

(%i1) integer_partitions (3);
(%o1)               {[1, 1, 1], [2, 1], [3]}

(%i2) s: integer_partitions (25)$

(%i3) cardinality (s);
(%o3)                         1958


(%i4) map (lambda ([x], apply ("+", x)), s);
(%o4)                         {25}


(%i5) integer_partitions (5, 3);
(%o5) {[2, 2, 1], [3, 1, 1], [3, 2, 0], [4, 1, 0], [5, 0, 0]}


(%i6) integer_partitions (5, 2);
(%o6)               {[3, 2], [4, 1], [5, 0]}
```


To find all partitions that satisfy a condition, use the function `subset`;
here is an example that finds all partitions of 10 that consist of prime numbers.









```maxima
maxima
(%i1) s: integer_partitions (10)$

(%i2) cardinality (s);
(%o2)                          42

(%i3) xprimep(x) := integerp(x) and (x > 1) and primep(x)$

(%i4) subset (s, lambda ([x], every (xprimep, x)));
(%o4) {[2, 2, 2, 2, 2], [3, 3, 2, 2], [5, 3, 2], [5, 5], [7, 3]}
```

<!-- category: Combinatorics -->
<!-- keywords: intersect -->
<!-- signatures: intersect(a_1, ..., a_n) -->
### Function: intersect (a_1, ..., a_n)

`intersect` is the same as `intersection`, which see.

<!-- category: Combinatorics -->
<!-- keywords: intersection -->
<!-- signatures: intersection(a_1, ..., a_n) -->
### Function: intersection (a_1, ..., a_n)

Returns a set containing the elements that are common to the 
sets *a_1* through *a_n*.


`intersection` complains if any argument is not a literal set.


Examples:













```maxima
maxima

(%i1) S_1 : {a, b, c, d};
(%o1)                     {a, b, c, d}


(%i2) S_2 : {d, e, f, g};
(%o2)                     {d, e, f, g}


(%i3) S_3 : {c, d, e, f};
(%o3)                     {c, d, e, f}


(%i4) S_4 : {u, v, w};
(%o4)                       {u, v, w}


(%i5) intersection (S_1, S_2);
(%o5)                          {d}


(%i6) intersection (S_2, S_3);
(%o6)                       {d, e, f}


(%i7) intersection (S_1, S_2, S_3);
(%o7)                          {d}


(%i8) intersection (S_1, S_2, S_3, S_4);
(%o8)                          {}
```

<!-- category: Combinatorics -->
<!-- keywords: kron_delta -->
<!-- signatures: kron_delta(x1, x2, ..., xp) -->
### Function: kron_delta (x1, x2, ..., xp)

Represents the Kronecker delta function.


`kron_delta` simplifies to 1 when *xi* and *yj* are equal
for all pairs of arguments, and it simplifies to 0 when *xi* and
*yj* are not equal for some pair of arguments. Equality is
determined using `is(equal(xi,xj))` and inequality by
`is(notequal(xi,xj))`. For exactly one argument, `kron_delta`
signals an error.


Examples:










```maxima
maxima

(%i1) kron_delta(a,a);
(%o1)                           1


(%i2) kron_delta(a,b,a,b);
(%o2)                   kron_delta(a, b)


(%i3) kron_delta(a,a,b,a+1);
(%o3)                           0


(%i4) assume(equal(x,y));
(%o4)                     [equal(x, y)]


(%i5) kron_delta(x,y);
(%o5)                           1
```

<!-- category: Combinatorics -->
<!-- keywords: listify -->
<!-- signatures: listify(a) -->
### Function: listify (a)

Returns a list containing the members of *a* when *a* is a set.
Otherwise, `listify` returns *a*.


`full_listify` replaces all set operators in *a* by list operators.


Examples:







```maxima
maxima

(%i1) listify ({a, b, c, d});
(%o1)                     [a, b, c, d]


(%i2) listify (F ({a, b, c, d}));
(%o2)                    F({a, b, c, d})
```

<!-- category: Combinatorics -->
<!-- keywords: makeset -->
<!-- signatures: makeset(expr, x, s) -->
### Function: makeset (expr, x, s)

Returns a set with members generated from the expression *expr*,
where *x* is a list of variables in *expr*,
and *s* is a set or list of lists.
To generate each set member,
*expr* is evaluated with the variables *x* bound in parallel to a member of *s*.


Each member of *s* must have the same length as *x*.
The list of variables *x* must be a list of symbols, without subscripts.
Even if there is only one symbol, *x* must be a list of one element,
and each member of *s* must be a list of one element.






See also `makelist`.


Examples:










```maxima
maxima

(%i1) makeset (i/j, [i, j], [[1, a], [2, b], [3, c], [4, d]]);
                           1  2  3  4
(%o1)                     {-, -, -, -}
                           a  b  c  d

(%i2) S : {x, y, z}$

(%i3) S3 : cartesian_product (S, S, S);
(%o3) {[x, x, x], [x, x, y], [x, x, z], [x, y, x], [x, y, y], 
[x, y, z], [x, z, x], [x, z, y], [x, z, z], [y, x, x], 
[y, x, y], [y, x, z], [y, y, x], [y, y, y], [y, y, z], 
[y, z, x], [y, z, y], [y, z, z], [z, x, x], [z, x, y], 
[z, x, z], [z, y, x], [z, y, y], [z, y, z], [z, z, x], 
[z, z, y], [z, z, z]}


(%i4) makeset (i + j + k, [i, j, k], S3);
(%o4) {3 x, 3 y, y + 2 x, 2 y + x, 3 z, z + 2 x, z + y + x, 
                                       z + 2 y, 2 z + x, 2 z + y}


(%i5) makeset (sin(x), [x], {[1], [2], [3]});
(%o5)               {sin(1), sin(2), sin(3)}
```

See also: `makelist`.

<!-- category: Combinatorics -->
<!-- keywords: moebius -->
<!-- signatures: moebius(n) -->
### Function: moebius (n)

Represents the Moebius function.


When *n* is product of $k$ distinct primes,
`moebius(n)` simplifies to $(-1)^k$;
when $n = 1$, it simplifies to 1;
and it simplifies to 0 for all other positive integers. 


`moebius` distributes over equations, lists, matrices, and sets.


Examples:














```maxima
maxima

(%i1) moebius (1);
(%o1)                           1


(%i2) moebius (2 * 3 * 5);
(%o2)                          - 1


(%i3) moebius (11 * 17 * 29 * 31);
(%o3)                           1


(%i4) moebius (2^32);
(%o4)                           0


(%i5) moebius (n);
(%o5)                      moebius(n)


(%i6) moebius (n = 12);
(%o6)                    moebius(n) = 0


(%i7) moebius ([11, 11 * 13, 11 * 13 * 15]);
(%o7)                      [- 1, 1, 1]


(%i8) moebius (matrix ([11, 12], [13, 14]));
                           [ - 1  0 ]
(%o8)                      [        ]
                           [ - 1  1 ]


(%i9) moebius ({21, 22, 23, 24});
(%o9)                      {- 1, 0, 1}
```

<!-- category: Combinatorics -->
<!-- keywords: multinomial_coeff -->
<!-- signatures: multinomial_coeff(a_1, ..., a_n), multinomial_coeff() -->
### Function: multinomial_coeff (a_1, ..., a_n)

Returns the multinomial coefficient.


When each *a_k* is a nonnegative integer, the multinomial coefficient
gives the number of ways of placing `a_1 + ... + a_n` 
distinct objects into $n$ boxes with *a_k* elements in the 
$k$’th box. In general, `multinomial_coeff (a_1, ..., a_n)`
evaluates to `(a_1 + ... + a_n)!/(a_1! ... a_n!)`.


`multinomial_coeff()` (with no arguments) evaluates to 1.


`minfactorial` may be able to simplify the value returned by `multinomial_coeff`.


Examples:








factorial: factorial of negative integer -6 not defined.
 – an error. To debug this try: debugmode(true);


```maxima
maxima

(%i1) multinomial_coeff (1, 2, x);
                            (x + 3)!
(%o1)                       --------
                              2 x!


(%i2) minfactorial (%);
                     (x + 1) (x + 2) (x + 3)
(%o2)                -----------------------
                                2

(%i3) multinomial_coeff (-6, 2);

(%i4) minfactorial (%);
                     (x + 1) (x + 2) (x + 3)
(%o4)                -----------------------
                                2
```

<!-- category: Combinatorics -->
<!-- keywords: num_distinct_partitions -->
<!-- signatures: num_distinct_partitions(n), num_distinct_partitions(n, list) -->
### Function: num_distinct_partitions (n)

Returns the number of distinct integer partitions of *n*
when *n* is a nonnegative integer.
Otherwise, `num_distinct_partitions` returns a noun expression.


`num_distinct_partitions(n, list)` returns a 
list of the number of distinct partitions of 1, 2, 3, ..., *n*. 


A distinct partition of *n* is
a list of distinct positive integers $k_1$, ..., $k_m$
such that $n = k_1 + ... + k_m$.


Examples:








```maxima
maxima

(%i1) num_distinct_partitions (12);
(%o1)                          15


(%i2) num_distinct_partitions (12, list);
(%o2)        [1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15]


(%i3) num_distinct_partitions (n);
(%o3)              num_distinct_partitions(n)
```

<!-- category: Combinatorics -->
<!-- keywords: num_partitions -->
<!-- signatures: num_partitions(n), num_partitions(n, list) -->
### Function: num_partitions (n)

Returns the number of integer partitions of *n*
when *n* is a nonnegative integer.
Otherwise, `num_partitions` returns a noun expression.


`num_partitions(n, list)` returns a
list of the number of integer partitions of 1, 2, 3, ..., *n*.


For a nonnegative integer *n*, `num_partitions(n)` is equal to
`cardinality(integer_partitions(n))`; however, `num_partitions` 
does not actually construct the set of partitions, so it is much faster.


Examples:








```maxima
maxima

(%i1) num_partitions (5) = cardinality (integer_partitions (5));
(%o1)                         7 = 7


(%i2) num_partitions (8, list);
(%o2)              [1, 2, 3, 5, 7, 11, 15, 22]


(%i3) num_partitions (n);
(%o3)                   num_partitions(n)
```

<!-- category: Combinatorics -->
<!-- keywords: partition_set -->
<!-- signatures: partition_set(a, f) -->
### Function: partition_set (a, f)

Partitions the set *a* according to the predicate *f*.


`partition_set` returns a list of two sets.
The first set comprises the elements of *a* for which *f* evaluates to `false`,
and the second comprises any other elements of *a*.
`partition_set` does not apply `is` to the return value of *f*.


`partition_set` complains if *a* is not a literal set.


See also `subset`.


Examples:








```maxima
maxima

(%i1) partition_set ({2, 7, 1, 8, 2, 8}, evenp);
(%o1)                   [{1, 7}, {2, 8}]


(%i2) partition_set ({x, rat(y), rat(y) + z, 1},
                     lambda ([x], ratp(x)));
(%o2)/R/              [{1, x}, {y, y + z}]
```

See also: `subset`.

<!-- category: Combinatorics -->
<!-- keywords: permutations -->
<!-- signatures: permutations(a) -->
### Function: permutations (a)

Returns a set of all distinct permutations of the members of 
the list or set *a*. Each permutation is a list, not a set. 


When *a* is a list, duplicate members of *a* are included
in the permutations.


`permutations` complains if *a* is not a literal list or set.


See also `random_permutation`.


Examples:







```maxima
maxima

(%i1) permutations ([a, a]);
(%o1)                       {[a, a]}


(%i2) permutations ([a, a, b]);
(%o2)           {[a, a, b], [a, b, a], [b, a, a]}
```

See also: `random_permutation`.

<!-- category: Combinatorics -->
<!-- keywords: powerset -->
<!-- signatures: powerset(a), powerset(a, n) -->
### Function: powerset (a)

Returns the set of all subsets of *a*, or a subset of that set.


`powerset(a)` returns the set of all subsets of the set *a*.
`powerset(a)` has `2^cardinality(a)` members.


`powerset(a, n)` returns the set of all subsets of *a* that have 
cardinality *n*.


`powerset` complains if *a* is not a literal set,
or if *n* is not a nonnegative integer.


Examples:











```maxima
maxima

(%i1) powerset ({a, b, c});
(%o1) {{}, {a}, {a, b}, {a, b, c}, {a, c}, {b}, {b, c}, {c}}


(%i2) powerset ({w, x, y, z}, 4);
(%o2)                    {{w, x, y, z}}


(%i3) powerset ({w, x, y, z}, 3);
(%o3)     {{w, x, y}, {w, x, z}, {w, y, z}, {x, y, z}}


(%i4) powerset ({w, x, y, z}, 2);
(%o4)   {{w, x}, {w, y}, {w, z}, {x, y}, {x, z}, {y, z}}


(%i5) powerset ({w, x, y, z}, 1);
(%o5)                 {{w}, {x}, {y}, {z}}


(%i6) powerset ({w, x, y, z}, 0);
(%o6)                         {{}}
```

<!-- category: Combinatorics -->
<!-- keywords: random_permutation -->
<!-- signatures: random_permutation(a) -->
### Function: random_permutation (a)

Returns a random permutation of the set or list *a*,
as constructed by the Knuth shuffle algorithm.


The return value is a new list, which is distinct
from the argument even if all elements happen to be the same.
However, the elements of the argument are not copied.


Examples:









```maxima
maxima

(%i1) random_permutation ([a, b, c, 1, 2, 3]);
(%o1)                  [c, 1, 2, 3, a, b]


(%i2) random_permutation ([a, b, c, 1, 2, 3]);
(%o2)                  [b, 3, 1, c, a, 2]


(%i3) random_permutation ({x + 1, y + 2, z + 3});
(%o3)                 [y + 2, z + 3, x + 1]


(%i4) random_permutation ({x + 1, y + 2, z + 3});
(%o4)                 [x + 1, y + 2, z + 3]
```

<!-- category: Combinatorics -->
<!-- keywords: set_partitions -->
<!-- signatures: set_partitions(a), set_partitions(a, n) -->
### Function: set_partitions (a)

Returns the set of all partitions of *a*, or a subset of that set.


`set_partitions(a, n)` returns a set of all
decompositions of *a* into *n* nonempty disjoint subsets.


`set_partitions(a)` returns the set of all partitions.


`stirling2` returns the cardinality of the set of partitions of a set.


A set of sets $P$ is a partition of a set $S$ when



1. each member of $P$ is a nonempty set,
2. distinct members of $P$ are disjoint,
3. the union of the members of $P$ equals $S$.


Examples:


The empty set is a partition of itself, the conditions 1 and 2 being vacuously true.






```maxima
maxima

(%i1) set_partitions ({});
(%o1)                         {{}}
```


The cardinality of the set of partitions of a set can be found using `stirling2`.








```maxima
maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$

(%i3) cardinality(p) = stirling2 (6, 3);
(%o3)                        90 = 90
```


Each member of `p` should have *n* = 3 members; let’s check.








```maxima
maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$

(%i3) map (cardinality, p);
(%o3)                          {3}
```


Finally, for each member of `p`, the union of its members should 
equal `s`; again let’s check.








```maxima
maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$

(%i3) map (lambda ([x], apply (union, listify (x))), p);
(%o3)                 {{0, 1, 2, 3, 4, 5}}
```

<!-- category: Combinatorics -->
<!-- keywords: setdifference -->
<!-- signatures: setdifference(a, b) -->
### Function: setdifference (a, b)

Returns a set containing the elements in the set *a* that are
not in the set *b*.


`setdifference` complains if either *a* or *b* is not a literal set.


Examples:












```maxima
maxima

(%i1) S_1 : {a, b, c, x, y, z};
(%o1)                  {a, b, c, x, y, z}


(%i2) S_2 : {aa, bb, c, x, y, zz};
(%o2)                 {aa, bb, c, x, y, zz}


(%i3) setdifference (S_1, S_2);
(%o3)                       {a, b, z}


(%i4) setdifference (S_2, S_1);
(%o4)                     {aa, bb, zz}


(%i5) setdifference (S_1, S_1);
(%o5)                          {}


(%i6) setdifference (S_1, {});
(%o6)                  {a, b, c, x, y, z}


(%i7) setdifference ({}, S_1);
(%o7)                          {}
```

<!-- category: Combinatorics -->
<!-- keywords: setequalp -->
<!-- signatures: setequalp(a, b) -->
### Function: setequalp (a, b)

Returns `true` if sets *a* and *b* have the same number of elements


and `is(x = y)` is `true`
for `x` in the elements of *a*
and `y` in the elements of *b*,
considered in the order determined by `listify`.
Otherwise, `setequalp` returns `false`.


Examples:








```maxima
maxima

(%i1) setequalp ({1, 2, 3}, {1, 2, 3});
(%o1)                         true


(%i2) setequalp ({a, b, c}, {1, 2, 3});
(%o2)                         false


(%i3) setequalp ({x^2 - y^2}, {(x + y) * (x - y)});
(%o3)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: setify -->
<!-- signatures: setify(a) -->
### Function: setify (a)

Constructs a set from the elements of the list *a*. Duplicate
elements of the list *a* are deleted and the elements
are sorted according to the predicate `orderlessp`.


`setify` complains if *a* is not a literal list.


Examples:








```maxima
maxima

(%i1) setify ([1, 2, 3, a, b, c]);
(%o1)                  {1, 2, 3, a, b, c}


(%i2) setify ([a, b, c, a, b, c]);
(%o2)                       {a, b, c}


(%i3) setify ([7, 13, 11, 1, 3, 9, 5]);
(%o3)                {1, 3, 5, 7, 9, 11, 13}
```

<!-- category: Combinatorics -->
<!-- keywords: setp -->
<!-- signatures: setp(a) -->
### Function: setp (a)

Returns `true` if and only if *a* is a Maxima set.


`setp` returns `true` for unsimplified sets (that is, sets with redundant members)
as well as simplified sets.



`setp` is equivalent to the Maxima function
`setp(a) := not atom(a) and op(a) = 'set`.


Examples:








```maxima
maxima

(%i1) simp : false;
(%o1)                         false


(%i2) {a, a, a};
(%o2)                       {a, a, a}


(%i3) setp (%);
(%o3)                         true
```

<!-- category: Combinatorics -->
<!-- keywords: some -->
<!-- signatures: some(f, a), some(f, L_1, ..., L_n) -->
### Function: some (f, a)

Returns `true` if the predicate *f* is `true` for one or more given arguments.


Given one set as the second argument, 
`some(f, s)` returns `true`
if `is(f(a_i))` returns `true` for one or more *a_i* in *s*.
`some` may or may not evaluate *f* for all *a_i* in *s*.
Since sets are unordered,
`some` may evaluate `f(a_i)` in any order.


Given one or more lists as arguments,
`some(f, L_1, ..., L_n)` returns `true`
if `is(f(x_1, ..., x_n))` returns `true` 
for one or more *x_1*, ..., *x_n* in *L_1*, ..., *L_n*, respectively.
`some` may or may not evaluate 
*f* for some combinations *x_1*, ..., *x_n*.
`some` evaluates lists in the order of increasing index.


Given an empty set `{}` or empty lists `[]` as arguments,
`some` returns `false`.


When the global flag `maperror` is `true`, all lists 
*L_1*, ..., *L_n* must have equal lengths.
When `maperror` is `false`, list arguments are
effectively truncated to the length of the shortest list. 


Return values of the predicate *f* which evaluate (via `is`)
to something other than `true` or `false`
are governed by the global flag `prederror`.
When `prederror` is `true`,
such values are treated as `false`.
When `prederror` is `false`,
such values are treated as `unknown`.


Examples:


`some` applied to a single set.
The predicate is a function of one argument.







```maxima
maxima

(%i1) some (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true


(%i2) some (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         true
```


`some` applied to two lists.
The predicate is a function of two arguments.







```maxima
maxima

(%i1) some ("=", [a, b, c], [a, b, c]);
(%o1)                         true


(%i2) some ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Return values of the predicate *f* which evaluate
to something other than `true` or `false`
are governed by the global flag `prederror`.













```maxima
maxima

(%i1) prederror : false;
(%o1)                         false


(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
           [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]


(%i3) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown


(%i4) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o4)                         true


(%i5) prederror : true;
(%o5)                         true


(%i6) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o6)                         false


(%i7) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o7)                         true
```

<!-- category: Combinatorics -->
<!-- keywords: stirling1 -->
<!-- signatures: stirling1(n, m) -->
### Function: stirling1 (n, m)

Represents the Stirling number of the first kind.


When *n* and *m* are nonnegative 
integers, the magnitude of `stirling1 (n, m)` is the number of 
permutations of a set with *n* members that have *m* cycles.


`stirling1` is a simplifying function.
Maxima knows the following identities:



1. $stirling1(1,k) = kron_delta(1,k), k >= 0$,(see [https://dlmf.nist.gov/26.8.E2]())
2. $stirling1(n,n) = 1, n >= 0$ (see [https://dlmf.nist.gov/26.8.E1]())
3. $stirling1(n,n-1) = -binomial(n,2), n >= 1$, (see [https://dlmf.nist.gov/26.8.E16]())
4. $stirling1(n,0) = kron_delta(n,0), n >=0$  (see [https://dlmf.nist.gov/26.8.E14]() and
   [https://dlmf.nist.gov/26.8.E1]())
5. $stirling1(n,1) =(-1)^(n-1) (n-1)!, n >= 1$ (see [https://dlmf.nist.gov/26.8.E14]())
6. $stirling1(n,k) = 0, n >= 0$ and $k > n$.


These identities are applied when the arguments are literal integers
or symbols declared as integers, and the first argument is nonnegative.
`stirling1` does not simplify for non-integer arguments.



Examples:








```maxima
maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$

(%i3) stirling1 (n, n);
(%o3)                           1
```

<!-- category: Combinatorics -->
<!-- keywords: stirling2 -->
<!-- signatures: stirling2(n, m) -->
### Function: stirling2 (n, m)

Represents the Stirling number of the second kind.


When *n* and *m* are nonnegative 
integers, `stirling2 (n, m)` is the number of ways a set with 
cardinality *n* can be partitioned into *m* disjoint subsets.


`stirling2` is a simplifying function.
Maxima knows the following identities.



1. $stirling2(n,0) = 1, n >= 1$ (see [https://dlmf.nist.gov/26.8.E17]() and stirling2(0,0) = 1)
2. $stirling2(n,n) = 1, n >= 0$, (see [https://dlmf.nist.gov/26.8.E4]())
3. $stirling2(n,1) = 1, n >= 1$, (see [https://dlmf.nist.gov/26.8.E17]() and stirling2(0,1) = 0)
4. $stirling2(n,2) = 2^(n-1) -1, n >= 1$, (see [https://dlmf.nist.gov/26.8.E17]())
5. $stirling2(n,n-1) = binomial(n,2), n>= 1$ (see [https://dlmf.nist.gov/26.8.E16]())
6. $stirling2(n,k) = 0, n >= 0$ and $k > n$.


These identities are applied when the arguments are literal integers
or symbols declared as integers, and the first argument is nonnegative.
`stirling2` does not simplify for non-integer arguments.


Examples:








```maxima
maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$

(%i3) stirling2 (n, n);
(%o3)                           1
```


`stirling2` does not simplify for non-integer arguments.






```maxima
maxima

(%i1) stirling2 (%pi, %pi);
(%o1)                  stirling2(%pi, %pi)
```

<!-- category: Combinatorics -->
<!-- keywords: subset -->
<!-- signatures: subset(a, f) -->
### Function: subset (a, f)

Returns the subset of the set *a* that satisfies the predicate *f*. 


`subset` returns a set which comprises the elements of *a*
for which *f* returns anything other than `false`.
`subset` does not apply `is` to the return value of *f*.


`subset` complains if *a* is not a literal set.


See also `partition_set`.


Examples:







```maxima
maxima

(%i1) subset ({1, 2, x, x + y, z, x + y + z}, atom);
(%o1)                     {1, 2, x, z}


(%i2) subset ({1, 2, 7, 8, 9, 14}, evenp);
(%o2)                      {2, 8, 14}
```

See also: `partition_set`.

<!-- category: Combinatorics -->
<!-- keywords: subsetp -->
<!-- signatures: subsetp(a, b) -->
### Function: subsetp (a, b)

Returns `true` if and only if the set *a* is a subset of *b*.


`subsetp` complains if either *a* or *b* is not a literal set.


Examples:







```maxima
maxima

(%i1) subsetp ({1, 2, 3}, {a, 1, b, 2, c, 3});
(%o1)                         true


(%i2) subsetp ({a, 1, b, 2, c, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Combinatorics -->
<!-- keywords: symmdifference -->
<!-- signatures: symmdifference(a_1, ..., a_n) -->
### Function: symmdifference (a_1, ..., a_n)

Returns the symmetric difference of sets *a_1*, ..., *a_n*.


Given two arguments, `symmdifference (a, b)` is the same as
`union (setdifference (a, b), setdifference (b, a))`.


`symmdifference` complains if any argument is not a literal set.


Examples:













```maxima
maxima

(%i1) S_1 : {a, b, c};
(%o1)                       {a, b, c}


(%i2) S_2 : {1, b, c};
(%o2)                       {1, b, c}


(%i3) S_3 : {a, b, z};
(%o3)                       {a, b, z}


(%i4) symmdifference ();
(%o4)                          {}


(%i5) symmdifference (S_1);
(%o5)                       {a, b, c}


(%i6) symmdifference (S_1, S_2);
(%o6)                        {1, a}


(%i7) symmdifference (S_1, S_2, S_3);
(%o7)                       {1, b, z}


(%i8) symmdifference ({}, S_1, S_2, S_3);
(%o8)                       {1, b, z}
```

<!-- category: Combinatorics -->
<!-- keywords: union -->
<!-- signatures: union(a_1, ..., a_n) -->
### Function: union (a_1, ..., a_n)

Returns the union of the sets *a_1* through *a_n*. 


`union()` (with no arguments) returns the empty set.


`union` complains if any argument is not a literal set.


Examples:













```maxima
maxima

(%i1) S_1 : {a, b, c + d, %e};
(%o1)                   {%e, a, b, d + c}


(%i2) S_2 : {%pi, %i, %e, c + d};
(%o2)                 {%e, %i, %pi, d + c}


(%i3) S_3 : {17, 29, 1729, %pi, %i};
(%o3)                {17, 29, 1729, %i, %pi}


(%i4) union ();
(%o4)                          {}


(%i5) union (S_1);
(%o5)                   {%e, a, b, d + c}


(%i6) union (S_1, S_2);
(%o6)              {%e, %i, %pi, a, b, d + c}


(%i7) union (S_1, S_2, S_3);
(%o7)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}


(%i8) union ({}, S_1, S_2, S_3);
(%o8)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
```

