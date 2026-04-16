## combinatorics

### Function: apply_cycles (cl, l)

Permutes the list or set *l* applying to it the list of cycles
*cl*. The cycles at the end of the list are applied first and the
first cycle in the list *cl* is the last one to be applied.


See also `permute`.


Example:








```maxima
(%i1) load("combinatorics")$

(%i2) lis1:[a,b*c^2,4,z,x/y,1/2,ff23(x),0];
                        2        x  1
(%o2)            [a, b c , 4, z, -, -, ff23(x), 0]
                                 y  2


(%i3) apply_cycles ([[1, 6], [2, 6, 5, 7]], lis1);
                  x  1                       2
(%o3)            [-, -, 4, z, ff23(x), a, b c , 0]
                  y  2
```

See also: `permute`.

### Function: cyclep (c, n)

Returns true if *c* is a valid cycle of order *n* namely, a list
of non-repeated positive integers less or equal to *n*. Otherwise,
it returns false.


See also `permp`.


Examples:










```maxima
(%i1) load("combinatorics")$

(%i2) cyclep ([-2,3,4], 5);
(%o2)                          false


(%i3) cyclep ([2,3,4,2], 5);
(%o3)                          false


(%i4) cyclep ([6,3,4], 5);
(%o4)                          false


(%i5) cyclep ([6,3,4], 6);
(%o5)                          true
```

See also: `permp`.

### Function: perm_cycles (p)

Returns permutation *p* as a product of cycles. The cycles are
written in a canonical form, in which the lowest index in the cycle is
placed in the first position.


See also `perm_005fdecomp`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_cycles ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                 [[1, 4], [2, 6, 5, 7]]
```

See also: `perm_decomp`.

### Function: perm_decomp (p)

Returns the minimum set of adjacent transpositions whose product equals
the given permutation *p*.


See also `perm_005fcycles`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_decomp ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2) [[6, 7], [5, 6], [6, 7], [3, 4], [4, 5], [2, 3], [3, 4], 
                            [4, 5], [5, 6], [1, 2], [2, 3], [3, 4]]
```

See also: `perm_cycles`.

### Function: perm_inverse (p)

Returns the inverse of a permutation of *p*, namely, a permutation
*q* such that the products *pq* and *qp* are equal to the
identity permutation: [1, 2, 3, ..., *n*], where *n* is the
length of *p*.


See also `permult`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_inverse ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                [4, 7, 3, 1, 6, 2, 5, 8]
```

See also: `permult`.

### Function: perm_length (p)

Determines the minimum number of adjacent transpositions necessary to
write permutation *p* as a product of adjacent transpositions. An
adjacent transposition is a cycle with only two numbers, which are
consecutive integers.


See also `perm_005fdecomp`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_length ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                           12
```

See also: `perm_decomp`.

### Function: perm_lex_next (p)

Returns the permutation that comes after the given permutation *p*,
in the sequence of permutations in lexicographic order.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_lex_next ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                [4, 6, 3, 1, 7, 5, 8, 2]
```

### Function: perm_lex_rank (p)

Finds the position of permutation *p*, an integer from 1 to the
degree *n* of the permutation, in the sequence of permutations in
lexicographic order.


See also `perm_lex_unrank` and `perms_005flex`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_lex_rank ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                          18255
```

See also: `perm_lex_unrank`, `perms_lex`.

### Function: perm_lex_unrank (n, i)

Returns the *n*-degree permutation at position *i* (from 1 to
*n*!) in the lexicographic ordering of permutations.


See also `perm_lex_rank` and `perms_005flex`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_lex_unrank (8, 18255);
(%o2)                [4, 6, 3, 1, 7, 5, 2, 8]
```

See also: `perm_lex_rank`, `perms_lex`.

### Function: perm_next (p)

Returns the permutation that comes after the given permutation *p*,
in the sequence of permutations in Trotter-Johnson order.


See also `perms`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_next ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                [4, 6, 3, 1, 7, 5, 8, 2]
```

See also: `perms`.

### Function: perm_parity (p)

Finds the parity of permutation *p*: 0 if the minimum number of
adjacent transpositions necessary to write permutation *p* as a
product of adjacent transpositions is even, or 1 if that number is odd.


See also `perm_005fdecomp`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_parity ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                            0
```

See also: `perm_decomp`.

### Function: perm_rank (p)

Finds the position of permutation *p*, an integer from 1 to the
degree *n* of the permutation, in the sequence of permutations in
Trotter-Johnson order.


See also `perm_unrank` and `perms`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_rank ([4, 6, 3, 1, 7, 5, 2, 8]);
(%o2)                          19729
```

See also: `perm_unrank`, `perms`.

### Function: perm_undecomp (cl, n)

Converts the list of cycles *cl* of degree *n* into an *n*
degree permutation, equal to their product.


See also `perm_005fdecomp`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_undecomp ([[1,6],[2,6,5,7]], 8);
(%o2)                [5, 6, 3, 4, 7, 1, 2, 8]
```

See also: `perm_decomp`.

### Function: perm_unrank (n, i)

Returns the *n*-degree permutation at position *i* (from 1 to
*n*!) in the Trotter-Johnson ordering of permutations.


See also `perm_rank` and `perms`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) perm_unrank (8, 19729);
(%o2)                [4, 6, 3, 1, 7, 5, 2, 8]
```

See also: `perm_rank`, `perms`.

### Function: permp (p)

Returns true if *p* is a valid permutation namely, a list of length
*n*, whose elements are all the positive integers from 1 to *n*,
without repetitions. Otherwise, it returns false.


Examples:








```maxima
(%i1) load("combinatorics")$

(%i2) permp ([2,0,3,1]);
(%o2)                          false


(%i3) permp ([2,1,4,3]);
(%o3)                          true
```

### Function: perms (perms, n, perms, n, i, perms, n, i, j)

`perms(n)` returns a list of all
*n*-degree permutations in the so-called Trotter-Johnson order.


`perms(n, i)` returns the *n*-degree
permutation which is at the *i*th position (from 1 to *n*!) in
the Trotter-Johnson ordering of the permutations.


`perms(n, i, j)` returns a list of the *n*-degree
permutations between positions *i* and *j* in the Trotter-Johnson
ordering of the permutations.


The sequence of permutations in Trotter-Johnson order starts with the
identity permutation and each consecutive permutation can be obtained
from the previous one a by single adjacent transposition.


See also `perm_next`, `perm_rank` and `perm_005funrank`.


Examples:









```maxima
(%i1) load("combinatorics")$

(%i2) perms (4);
(%o2) [[1, 2, 3, 4], [1, 2, 4, 3], [1, 4, 2, 3], [4, 1, 2, 3], 
[4, 1, 3, 2], [1, 4, 3, 2], [1, 3, 4, 2], [1, 3, 2, 4], 
[3, 1, 2, 4], [3, 1, 4, 2], [3, 4, 1, 2], [4, 3, 1, 2], 
[4, 3, 2, 1], [3, 4, 2, 1], [3, 2, 4, 1], [3, 2, 1, 4], 
[2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 3, 1], [4, 2, 3, 1], 
[4, 2, 1, 3], [2, 4, 1, 3], [2, 1, 4, 3], [2, 1, 3, 4]]


(%i3) perms (4, 12);
(%o3)                     [[4, 3, 1, 2]]


(%i4) perms (4, 12, 14);
(%o4)       [[4, 3, 1, 2], [4, 3, 2, 1], [3, 4, 2, 1]]
```

See also: `perm_next`, `perm_rank`, `perm_unrank`.

### Function: perms_lex (perms_lex, n, perms_lex, n, i, perms_lex, n, i, j)

`perms_lex(n)` returns a list of all
*n*-degree permutations in the so-called lexicographic order.


`perms_lex(n, i)` returns the *n*-degree
permutation which is at the *i*th position (from 1 to *n*!) in
the lexicographic ordering of the permutations.


`perms_lex(n, i, j)` returns a list of the *n*-degree
permutations between positions *i* and *j* in the lexicographic
ordering of the permutations.


The sequence of permutations in lexicographic order starts with all the
permutations with the lowest index, 1, followed by all permutations
starting with the following index, 2, and so on. The permutations
starting by an index *i* are the permutations of the first *n*
integers different from *i* and they are also placed in
lexicographic order, where the permutations with the lowest of those
integers are placed first and so on.


See also `perm_lex_next`, `perm_lex_rank` and
`perm_005flex_005funrank`.


Examples:









```maxima
(%i1) load("combinatorics")$

(%i2) perms_lex (4);
(%o2) [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], 
[1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], 
[2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], 
[3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], 
[3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], 
[4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]


(%i3) perms_lex (4, 12);
(%o3)                     [[2, 4, 3, 1]]


(%i4) perms_lex (4, 12, 14);
(%o4)       [[2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2]]
```

See also: `perm_lex_next`, `perm_lex_rank`, `perm_lex_unrank`.

### Function: permult (p_1, ..., p_m)

Returns the product of two or more permutations *p_1*, ..., *p_m*.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) permult ([2,3,1], [3,1,2], [2,1,3]);
(%o2)                        [2, 1, 3]
```

### Function: permute (p, l)

Applies the permutation *p* to the elements of the list (or set)
*l*.


Example:








```maxima
(%i1) load("combinatorics")$

(%i2) lis1: [a,b*c^2,4,z,x/y,1/2,ff23(x),0];
                        2        x  1
(%o2)            [a, b c , 4, z, -, -, ff23(x), 0]
                                 y  2


(%i3) permute ([4, 6, 3, 1, 7, 5, 2, 8], lis1);
                     1                 x     2
(%o3)            [z, -, 4, a, ff23(x), -, b c , 0]
                     2                 y
```

### Function: random_perm (n)

Returns a random permutation of degree *n*.


See also `random_005fpermutation`.


Example:







```maxima
(%i1) load("combinatorics")$

(%i2) random_perm (7);
(%o2)                  [6, 3, 4, 7, 5, 1, 2]
```

See also: `random_permutation`.

