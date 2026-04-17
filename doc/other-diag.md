## diag

<!-- category: Other -->
<!-- keywords: diag -->
<!-- signatures: diag(lm) -->
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

<!-- category: Other -->
<!-- keywords: dispJordan -->
<!-- signatures: dispJordan(l) -->
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

<!-- category: Other -->
<!-- keywords: JF -->
<!-- signatures: JF(lambda, n) -->
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

<!-- category: Other -->
<!-- keywords: jordan -->
<!-- signatures: jordan(mat) -->
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

<!-- category: Other -->
<!-- keywords: mat_function -->
<!-- signatures: mat_function(f, A) -->
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

<!-- category: Other -->
<!-- keywords: minimalPoly -->
<!-- signatures: minimalPoly(l) -->
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

<!-- category: Other -->
<!-- keywords: ModeMatrix -->
<!-- signatures: ModeMatrix(A, [jordan_info]) -->
### Function: ModeMatrix (A, [jordan_info])

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

