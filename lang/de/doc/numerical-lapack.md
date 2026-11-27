## lapack

<!-- category: Numerical -->
<!-- keywords: dgeev -->
<!-- signatures: dgeev(A), dgeev(A, right_p, left_p) -->
### Function: dgeev (A)

Computes the eigenvalues and, optionally, the eigenvectors of a matrix *A*.
All elements of *A* must be integer or floating point numbers.
*A* must be square (same number of rows and columns).
*A* might or might not be symmetric.


`dgeev(A)` computes only the eigenvalues of *A*.
`dgeev(A, right_p, left_p)` computes the eigenvalues of
*A* and the right eigenvectors when $right_p = true$
and the left eigenvectors when $left_p = true$.


A list of three items is returned.
The first item is a list of the eigenvalues.
The second item is `false` or the matrix of right eigenvectors.
The third item is `false` or the matrix of left eigenvectors.


The right eigenvector $v(j)$ (the $j$-th column of the right
eigenvector matrix) satisfies


$A . v(j) = lambda(j) . v(j)$


where $lambda(j)$ is the corresponding eigenvalue.
The left eigenvector $u(j)$ (the $j$-th column of the left eigenvector
matrix) satisfies


$u(j)**H . A = lambda(j) . u(j)**H$


where $u(j)**H$ denotes the conjugate transpose of $u(j)$.
The Maxima function `ctranspose` computes the conjugate transpose.


The computed eigenvectors are normalized to have Euclidean norm
equal to 1, and largest component has imaginary part equal to zero.


Example:



```maxima
(%i1) load ("lapack")$
(%i2) fpprintprec : 6;
(%o2)                           6
(%i3) M : matrix ([9.5, 1.75], [3.25, 10.45]);
                         [ 9.5   1.75  ]
(%o3)                    [             ]
                         [ 3.25  10.45 ]
(%i4) dgeev (M);
(%o4)          [[7.54331, 12.4067], false, false]
(%i5) [L, v, u] : dgeev (M, true, true);
                           [ - .666642  - .515792 ]

(%o5) [[7.54331, 12.4067], [                      ], 
                           [  .745378   - .856714 ]
                                        [ - .856714  - .745378 ]
                                        [                      ]]
                                        [  .515792   - .666642 ]

(%i6) D : apply (diag_matrix, L);
                      [ 7.54331     0    ]
(%o6)                 [                  ]
                      [    0     12.4067 ]
(%i7) M . v - v . D;
                [      0.0       - 8.88178E-16 ]
(%o7)           [                              ]
                [ - 8.88178E-16       0.0      ]
(%i8) transpose (u) . M - D . transpose (u);
                     [ 0.0  - 4.44089E-16 ]
(%o8)                [                    ]
                     [ 0.0       0.0      ]
```

<!-- category: Numerical -->
<!-- keywords: dgemm -->
<!-- signatures: dgemm(A, B), dgemm(A, B, options) -->
### Function: dgemm (A, B)

Compute the product of two matrices and optionally add the product to
a third matrix.


In the simplest form, `dgemm(A, B)` computes the
product of the two real matrices, *A* and *B*.


In the second form, `dgemm` computes the $alpha * A * B + beta * C$ where *A*, *B*,
*C* are real matrices of the appropriate sizes and *alpha* and
*beta* are real numbers.  Optionally, *A* and/or *B* can
be transposed before computing the product.  The extra parameters are
specifed by optional keyword arguments: The keyword arguments are
optional and may be specified in any order.  They all take the form
`key=val`.  The keyword arguments are:



**C** — The matrix *C* that should be added.  The default is `false`,
which means no matrix is added.
**alpha** — The product of *A* and *B* is multiplied by this value.  The
default is 1.
**beta** — If a matrix *C* is given, this value multiplies *C* before it
is added.  The default value is 0, which implies that *C* is not
added, even if *C* is given.  Hence, be sure to specify a non-zero
value for *beta*.
**transpose_a** — If `true`, the transpose of *A* is used instead of *A*
for the product.  The default is `false`.
**transpose_b** — If `true`, the transpose of *B* is used instead of *B*
for the product.  The default is `false`.


Examples:



```maxima
(%i1) load ("lapack")$
(%i2) A : matrix([1,2,3],[4,5,6],[7,8,9]);
                                  [ 1  2  3 ]
                                  [         ]
(%o2)                             [ 4  5  6 ]
                                  [         ]
                                  [ 7  8  9 ]
(%i3) B : matrix([-1,-2,-3],[-4,-5,-6],[-7,-8,-9]);
                               [ - 1  - 2  - 3 ]
                               [               ]
(%o3)                          [ - 4  - 5  - 6 ]
                               [               ]
                               [ - 7  - 8  - 9 ]
(%i4) C : matrix([3,2,1],[6,5,4],[9,8,7]);
                                  [ 3  2  1 ]
                                  [         ]
(%o4)                             [ 6  5  4 ]
                                  [         ]
                                  [ 9  8  7 ]
(%i5) dgemm(A,B);
                         [ - 30.0   - 36.0   - 42.0  ]
                         [                           ]
(%o5)                    [ - 66.0   - 81.0   - 96.0  ]
                         [                           ]
                         [ - 102.0  - 126.0  - 150.0 ]
(%i6) A . B;
                            [ - 30   - 36   - 42  ]
                            [                     ]
(%o6)                       [ - 66   - 81   - 96  ]
                            [                     ]
                            [ - 102  - 126  - 150 ]
(%i7) dgemm(A,B,transpose_a=true);

                         [ - 66.0  - 78.0   - 90.0  ]
                         [                          ]
(%o7)                    [ - 78.0  - 93.0   - 108.0 ]
                         [                          ]
                         [ - 90.0  - 108.0  - 126.0 ]

(%i8) transpose(A) . B;
                           [ - 66  - 78   - 90  ]
                           [                    ]
(%o8)                      [ - 78  - 93   - 108 ]
                           [                    ]
                           [ - 90  - 108  - 126 ]
(%i9) dgemm(A,B,c=C,beta=1);
                         [ - 27.0  - 34.0   - 41.0  ]
                         [                          ]
(%o9)                    [ - 60.0  - 76.0   - 92.0  ]
                         [                          ]
                         [ - 93.0  - 118.0  - 143.0 ]
(%i10) A . B + C;
                            [ - 27  - 34   - 41  ]
                            [                    ]
(%o10)                      [ - 60  - 76   - 92  ]
                            [                    ]
                            [ - 93  - 118  - 143 ]
(%i11) dgemm(A,B,c=C,beta=1, alpha=-1);
                            [ 33.0   38.0   43.0  ]
                            [                     ]
(%o11)                      [ 72.0   86.0   100.0 ]
                            [                     ]
                            [ 111.0  134.0  157.0 ]
(%i12) -A . B + C;
                               [ 33   38   43  ]
                               [               ]
(%o12)                         [ 72   86   100 ]
                               [               ]
                               [ 111  134  157 ]
```

<!-- category: Numerical -->
<!-- keywords: dgeqrf -->
<!-- signatures: dgeqrf(A) -->
### Function: dgeqrf (A)

Computes the QR decomposition of the matrix *A*.
All elements of *A* must be integer or floating point numbers.
*A* may or may not have the same number of rows and columns.


A list of two items is returned.
The first item is the matrix *Q*, which is a square, orthonormal matrix
which has the same number of rows as *A*.
The second item is the matrix *R*, which is the same size as *A*,
and which has all elements equal to zero below the diagonal.
The product `Q . R`, where "." is the noncommutative
multiplication operator, is equal to *A* (ignoring floating point round-off
errors).


Examples:



```maxima
(%i1) load ("lapack") $
(%i2) fpprintprec : 6 $
(%i3) M : matrix ([1, -3.2, 8], [-11, 2.7, 5.9]) $
(%i4) [q, r] : dgeqrf (M);
       [ - .0905357  .995893  ]
(%o4) [[                      ], 
       [  .995893    .0905357 ]
                               [ - 11.0454   2.97863   5.15148 ]
                               [                               ]]
                               [     0      - 2.94241  8.50131 ]
(%i5) q . r - M;
         [ - 7.77156E-16   1.77636E-15   - 8.88178E-16 ]
(%o5)    [                                             ]
         [      0.0       - 1.33227E-15   8.88178E-16  ]
(%i6) mat_norm (%, 1);
(%o6)                      3.10862E-15
```

<!-- category: Numerical -->
<!-- keywords: dgesv -->
<!-- signatures: dgesv(A, b) -->
### Function: dgesv (A, b)

Computes the solution *x* of the linear equation $A x = b$, where *A* is a square matrix, and *b* is a matrix of the same
number of rows as *A* and any number of columns.
The return value *x* is the same size as *b*.


The elements of *A* and *b* must evaluate to real floating point numbers
via `float`; thus elements may be any numeric type, symbolic numerical
constants, or expressions which evaluate to floats.
The elements of *x* are always floating point numbers.
All arithmetic is carried out as floating point operations.


`dgesv` computes the solution via the LU decomposition of *A*.


Examples:


`dgesv` computes the solution of the linear equation $A x = b$.



```maxima
(%i1) A : matrix ([1, -2.5], [0.375, 5]);
                               [   1    - 2.5 ]
(%o1)                          [              ]
                               [ 0.375    5   ]
(%i2) b : matrix ([1.75], [-0.625]);
                                  [  1.75   ]
(%o2)                             [         ]
                                  [ - 0.625 ]
(%i3) x : dgesv (A, b);
                            [  1.210526315789474  ]
(%o3)                       [                     ]
                            [ - 0.215789473684211 ]
(%i4) dlange (inf_norm, b - A.x);
(%o4)                                 0.0
```


*b* is a matrix with the same number of rows as *A* and any number of
columns.  *x* is the same size as *b*.



```maxima
(%i1) A : matrix ([1, -0.15], [1.82, 2]);
                               [  1    - 0.15 ]
(%o1)                          [              ]
                               [ 1.82    2    ]
(%i2) b : matrix ([3.7, 1, 8], [-2.3, 5, -3.9]);
                              [  3.7   1    8   ]
(%o2)                         [                 ]
                              [ - 2.3  5  - 3.9 ]
(%i3) x : dgesv (A, b);
      [  3.103827540695117  1.20985481742191    6.781786185657722 ]
(%o3) [                                                           ]
      [ -3.974483062032557  1.399032116146062  -8.121425428948527 ]
(%i4) dlange (inf_norm, b - A . x);
(%o4)                       1.1102230246251565E-15
```


The elements of *A* and *b* must evaluate to real floating point
numbers.



```maxima
(%i1) A : matrix ([5, -%pi], [1b0, 11/17]);

                               [   5    - %pi ]
                               [              ]
(%o1)                          [         11   ]
                               [ 1.0b0   --   ]
                               [         17   ]

(%i2) b : matrix ([%e], [sin(1)]);
                                  [   %e   ]
(%o2)                             [        ]
                                  [ sin(1) ]
(%i3) x : dgesv (A, b);
                             [ 0.690375643155986 ]
(%o3)                        [                   ]
                             [ 0.233510982552952 ]
(%i4) dlange (inf_norm, b - A . x);
(%o4)                        2.220446049250313E-16
```

<!-- category: Numerical -->
<!-- keywords: dgesvd -->
<!-- signatures: dgesvd(A), dgesvd(A, left_p, right_p) -->
### Function: dgesvd (A)

Computes the singular value decomposition (SVD) of a matrix *A*, comprising
the singular values and, optionally, the left and right singular vectors.
All elements of *A* must be integer or floating point numbers.
*A* might or might not be square (same number of rows and columns).


Let $m$ be the number of rows, and $n$ the number of columns of
*A*.  The singular value decomposition of *A* comprises three matrices,
*U*, *Sigma*, and *V^T*, such that



$A = U . Sigma . V^T$


where *U* is an $m$-by-$m$ unitary matrix,
*Sigma* is an $m$-by-$n$ diagonal matrix,
and *V^T* is an $n$-by-$n$ unitary matrix.


Let $sigma[i]$ be a diagonal element of $Sigma$,
that is, $Sigma[i, i] = sigma[i]$.
The elements $sigma[i]$ are the so-called singular values of *A*;
these are real and nonnegative, and returned in descending order.
The first $min(m, n)$ columns of *U* and *V* are
the left and right singular vectors of *A*.
Note that `dgesvd` returns the transpose of *V*, not *V* itself.


`dgesvd(A)` computes only the singular values of *A*.
`dgesvd(A, left_p, right_p)` computes the singular values
of *A* and the left singular vectors when $left_p = true$
and the right singular vectors when $right_p = true$.


A list of three items is returned.
The first item is a list of the singular values.
The second item is `false` or the matrix of left singular vectors.
The third item is `false` or the matrix of right singular vectors.


Example:



```maxima
(%i1) load ("lapack")$
(%i2) fpprintprec : 6;
(%o2)                           6
(%i3) M: matrix([1, 2, 3], [3.5, 0.5, 8], [-1, 2, -3], [4, 9, 7]);

                        [  1    2    3  ]
                        [               ]
                        [ 3.5  0.5   8  ]
(%o3)                   [               ]
                        [ - 1   2   - 3 ]
                        [               ]
                        [  4    9    7  ]

(%i4) dgesvd (M);
(%o4)      [[14.4744, 6.38637, .452547], false, false]
(%i5) [sigma, U, VT] : dgesvd (M, true, true);
(%o5) [[14.4744, 6.38637, .452547], 
[ - .256731  .00816168   .959029    - .119523 ]
[                                             ]
[ - .526456   .672116   - .206236   - .478091 ]
[                                             ], 
[  .107997   - .532278  - .0708315  - 0.83666 ]
[                                             ]
[ - .803287  - .514659  - .180867    .239046  ]
[ - .374486  - .538209  - .755044 ]
[                                 ]
[  .130623   - .836799   0.5317   ]]
[                                 ]
[ - .917986   .100488    .383672  ]
(%i6) m : length (U);
(%o6)                           4
(%i7) n : length (VT);
(%o7)                           3
(%i8) Sigma:
        genmatrix(lambda ([i, j], if i=j then sigma[i] else 0),
                  m, n);
                  [ 14.4744     0        0    ]
                  [                           ]
                  [    0     6.38637     0    ]
(%o8)             [                           ]
                  [    0        0     .452547 ]
                  [                           ]
                  [    0        0        0    ]
(%i9) U . Sigma . VT - M;
          [  1.11022E-15        0.0       1.77636E-15 ]
          [                                           ]
          [  1.33227E-15    1.66533E-15       0.0     ]
(%o9)     [                                           ]
          [ - 4.44089E-16  - 8.88178E-16  4.44089E-16 ]
          [                                           ]
          [  8.88178E-16    1.77636E-15   8.88178E-16 ]
(%i10) transpose (U) . U;

       [     1.0      5.55112E-17    2.498E-16     2.77556E-17  ]
       [                                                        ]
       [ 5.55112E-17      1.0       5.55112E-17    4.16334E-17  ]
(%o10) [                                                        ]
       [  2.498E-16   5.55112E-17       1.0       - 2.08167E-16 ]
       [                                                        ]
       [ 2.77556E-17  4.16334E-17  - 2.08167E-16       1.0      ]

(%i11) VT . transpose (VT);
          [      1.0           0.0      - 5.55112E-17 ]
          [                                           ]
(%o11)    [      0.0           1.0       5.55112E-17  ]
          [                                           ]
          [ - 5.55112E-17  5.55112E-17       1.0      ]
```

<!-- category: Numerical -->
<!-- keywords: dlange, zlange -->
<!-- signatures: dlange(norm, A), zlange(norm, A) -->
### Function: dlange (norm, A)

Computes a norm or norm-like function of the matrix *A*.



**max** — Compute $max(abs(A(i, j)))$ where $i$ and $j$ range over
the rows and columns, respectively, of *A*.
Note that this function is not a proper matrix norm.
**one_norm** — Compute the $L[1]$ norm of *A*,that is, the maximum of the sum of the
absolute value of elements in each column.
**inf_norm** — Compute the $L[inf]$ norm of *A*,
that is, the maximum of the sum of the absolute value of elements in each row.
**frobenius** — Compute the Frobenius norm of *A*,
that is, the square root of the sum of squares of the matrix elements.

