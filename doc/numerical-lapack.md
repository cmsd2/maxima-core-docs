## lapack

<!-- category: Numerical -->
<!-- keywords: dgeev -->
<!-- signatures: dgeev(A), dgeev(A, right_p, left_p) -->
### Function: dgeev (A)

Computes the eigenvalues and, optionally, the eigenvectors of a matrix *A*.
All elements of *A* must be integer or floating point numbers.
*A* must be square (same number of rows and columns).
*A* might or might not be symmetric.


To make use of this function, you must load the LaPack package via
`load("lapack")`.


`dgeev(A)` computes only the eigenvalues of *A*.
`dgeev(A, right_p, left_p)` computes the eigenvalues of *A*
and the right eigenvectors when $right_p = true$
and the left eigenvectors when $left_p = true$.


A list of three items is returned.
The first item is a list of the eigenvalues.
The second item is `false` or the matrix of right eigenvectors.
The third item is `false` or the matrix of left eigenvectors.


The right eigenvector
$v_j$
(the $j$-th column of the right eigenvector matrix) satisfies



$$\mathbf{A} v_j = \lambda_j v_j$$


$${\bf A} v_j = \lambda_j v_j
$$



where
$\lambda_j$
is the corresponding eigenvalue.
The left eigenvector
$u_j$
(the $j$-th column of the left eigenvector matrix) satisfies



$$u_j^\mathbf{H} \mathbf{A} = \lambda_j u_j^\mathbf{H}$$


$$u_j^{\bf H} {\bf A} = \lambda_j u_j^{\bf H}
$$



where
$u_j^\mathbf{H}$
denotes the conjugate transpose of
$u_j.$
For a Maxima function to compute the conjugate transpose, `ctranspose`.



The computed eigenvectors are normalized to have Euclidean norm
equal to 1, and largest component has imaginary part equal to zero.


Example:













```maxima
maxima
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
                           [ - 0.666642  - 0.515792 ]
(%o5) [[7.54331, 12.4067], [                        ], 
                           [  0.745378   - 0.856714 ]
                                      [ - 0.856714  - 0.745378 ]
                                      [                        ]]
                                      [  0.515792   - 0.666642 ]


(%i6) D : apply (diag_matrix, L);
                      [ 7.54331     0    ]
(%o6)                 [                  ]
                      [    0     12.4067 ]


(%i7) M . v - v . D;
                [      0.0       - 8.88178e-16 ]
(%o7)           [                              ]
                [ - 8.88178e-16       0.0      ]


(%i8) transpose (u) . M - D . transpose (u);
                     [ 0.0  - 4.44089e-16 ]
(%o8)                [                    ]
                     [ 0.0       0.0      ]
```

See also: `ctranspose`.

<!-- category: Numerical -->
<!-- keywords: dgemm -->
<!-- signatures: dgemm(A, B), dgemm(A, B, options) -->
### Function: dgemm (A, B)

Compute the product of two matrices and optionally add the product to
a third matrix.


In the simplest form, `dgemm(A, B)` computes the
product of the two real matrices, *A* and *B*.


To make use of this function, you must load the LaPack package via
`load("lapack")`.


In the second form, `dgemm` computes
$\alpha {\bf A} {\bf B} + \beta {\bf C}$
where
${\bf A},$
${\bf B},$
and
${\bf C}$
are real matrices of the appropriate sizes and
$\alpha$
and
$\beta$
are real numbers.  Optionally,
${\bf A}$
and/or
${\bf B}$
can
be transposed before computing the product.  The extra parameters are
specified by optional keyword arguments: The keyword arguments are
optional and may be specified in any order.  They all take the form
`key=val`.  The keyword arguments are:



**C** — The matrix
${\bf C}$
that should be added.  The default is `false`,
which means no matrix is added.
**alpha** — The product of
${\bf A}$
and
${\bf B}$
is multiplied by this value.  The
default is 1.
**beta** — If a matrix
${\bf C}$
is given, this value multiplies
${\bf C}$
before it
is added.  The default value is 0, which implies that
${\bf C}$
is not
added, even if
${\bf C}$
is given.  Hence, be sure to specify a non-zero
value for
$\beta.$
**transpose_a** — If `true`, the transpose of
${\bf A}$
is used instead of
${\bf A}$
for the product.  The default is `false`.
**transpose_b** — If `true`, the transpose of
${\bf B}$
is used instead of
${\bf B}$
for the product.  The default is `false`.

















```maxima
maxima
(%i1) load ("lapack")$

(%i2) A : matrix([1,2,3],[4,5,6],[7,8,9]);
                           [ 1  2  3 ]
                           [         ]
(%o2)                      [ 4  5  6 ]
                           [         ]
                           [ 7  8  9 ]


(%i3) B : matrix([-1,-2,-3],[-4,-5,-6],[-7,-8,-9]);
                        [ - 1  - 2  - 3 ]
                        [               ]
(%o3)                   [ - 4  - 5  - 6 ]
                        [               ]
                        [ - 7  - 8  - 9 ]


(%i4) C : matrix([3,2,1],[6,5,4],[9,8,7]);
                           [ 3  2  1 ]
                           [         ]
(%o4)                      [ 6  5  4 ]
                           [         ]
                           [ 9  8  7 ]


(%i5) dgemm(A,B);
                  [ - 30.0   - 36.0   - 42.0  ]
                  [                           ]
(%o5)             [ - 66.0   - 81.0   - 96.0  ]
                  [                           ]
                  [ - 102.0  - 126.0  - 150.0 ]


(%i6) A . B;
                     [ - 30   - 36   - 42  ]
                     [                     ]
(%o6)                [ - 66   - 81   - 96  ]
                     [                     ]
                     [ - 102  - 126  - 150 ]


(%i7) dgemm(A,B,transpose_a=true);
                  [ - 66.0  - 78.0   - 90.0  ]
                  [                          ]
(%o7)             [ - 78.0  - 93.0   - 108.0 ]
                  [                          ]
                  [ - 90.0  - 108.0  - 126.0 ]


(%i8) transpose(A) . B;
                     [ - 66  - 78   - 90  ]
                     [                    ]
(%o8)                [ - 78  - 93   - 108 ]
                     [                    ]
                     [ - 90  - 108  - 126 ]


(%i9) dgemm(A,B,c=C,beta=1);
                  [ - 27.0  - 34.0   - 41.0  ]
                  [                          ]
(%o9)             [ - 60.0  - 76.0   - 92.0  ]
                  [                          ]
                  [ - 93.0  - 118.0  - 143.0 ]


(%i10) A . B + C;
                     [ - 27  - 34   - 41  ]
                     [                    ]
(%o10)               [ - 60  - 76   - 92  ]
                     [                    ]
                     [ - 93  - 118  - 143 ]


(%i11) dgemm(A,B,c=C,beta=1, alpha=-1);
                     [ 33.0   38.0   43.0  ]
                     [                     ]
(%o11)               [ 72.0   86.0   100.0 ]
                     [                     ]
                     [ 111.0  134.0  157.0 ]


(%i12) -A . B + C;
                        [ 33   38   43  ]
                        [               ]
(%o12)                  [ 72   86   100 ]
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


To make use of this function, you must load the LaPack package via
`load("lapack")`.


The real square matrix
$\mathbf{A}$
can be decomposed as



$$\mathbf{A} = \mathbf{Q}\mathbf{R}$$


$${\bf A} = {\bf Q} {\bf R}$$



where
${\bf Q}$
is a square orthogonal matrix with the same number of rows as
$\mathbf{A}$
and
${\bf R}$
is an upper triangular matrix and is the same size as
${\bf A}.$


A list of two items is returned.
The first item is the matrix
${\bf Q}.$
The second item is the matrix
${\bf R},$
The product $Q . R$, where "." is the noncommutative multiplication operator,
is equal to *A* (ignoring floating point round-off errors).











```maxima
maxima
(%i1) load ("lapack")$

(%i2) fpprintprec : 6;
(%o2)                           6


(%i3) M : matrix ([1, -3.2, 8], [-11, 2.7, 5.9]);
                      [  1    - 3.2   8  ]
(%o3)                 [                  ]
                      [ - 11   2.7   5.9 ]


(%i4) [q, r] : dgeqrf (M);
       [ - 0.0905357  0.995893  ]
(%o4) [[                        ], 
       [  0.995893    0.0905357 ]
                               [ - 11.0454   2.97863   5.15148 ]
                               [                               ]]
                               [    0.0     - 2.94241  8.50131 ]


(%i5) q . r - M;
         [ - 7.77156e-16   1.77636e-15   - 8.88178e-16 ]
(%o5)    [                                             ]
         [      0.0       - 1.33227e-15   8.88178e-16  ]


(%i6) mat_norm (%, 1);
(%o6)                      3.10862e-15
```

<!-- category: Numerical -->
<!-- keywords: dgesv -->
<!-- signatures: dgesv(A, b) -->
### Function: dgesv (A, b)

Computes the solution *x* of the linear equation
${\bf A} x = b,$
where
${\bf A}$
is a square matrix, and $b$ is a matrix of the same number of rows
as
${\bf A}$
and any number of columns.
The return value $x$ is the same size as $b$.


To make use of this function, you must load the LaPack package via
`load("lapack")`.


The elements of *A* and *b* must evaluate to real floating point numbers via `float`;
thus elements may be any numeric type, symbolic numerical constants, or expressions which evaluate to floats.
The elements of *x* are always floating point numbers.
All arithmetic is carried out as floating point operations.


`dgesv` computes the solution via the LU decomposition of *A*.


Examples:


`dgesv` computes the solution of the linear equation $A x = b$.










```maxima
maxima
(%i1) load("lapack")$

(%i2) A : matrix ([1, -2.5], [0.375, 5]);
                        [   1    - 2.5 ]
(%o2)                   [              ]
                        [ 0.375    5   ]


(%i3) b : matrix ([1.75], [-0.625]);
                           [  1.75   ]
(%o3)                      [         ]
                           [ - 0.625 ]


(%i4) x : dgesv (A, b);
                    [  1.2105263157894737   ]
(%o4)               [                       ]
                    [ - 0.21578947368421053 ]


(%i5) dlange (inf_norm, b - A . x);
(%o5)                          0.0
```


*b* is a matrix with the same number of rows as *A* and any number of columns.
*x* is the same size as *b*.










```maxima
maxima
(%i1) load ("lapack")$

(%i2) A : matrix ([1, -0.15], [1.82, 2]);
                        [  1    - 0.15 ]
(%o2)                   [              ]
                        [ 1.82    2    ]


(%i3) b : matrix ([3.7, 1, 8], [-2.3, 5, -3.9]);
                       [  3.7   1    8   ]
(%o3)                  [                 ]
                       [ - 2.3  5  - 3.9 ]


(%i4) x : dgesv (A, b);
(%o4) 
 [ 3.1038275406951175   1.2098548174219095  6.7817861856577215  ]
 [                                                              ]
 [ - 3.974483062032557  1.3990321161460624  - 8.121425428948527 ]


(%i5) dlange (inf_norm, b - A . x);
(%o5)                1.1102230246251565e-15
```


The elements of *A* and *b* must evaluate to real floating point numbers.










```maxima
maxima
(%i1) load ("lapack")$

(%i2) A : matrix ([5, -%pi], [1b0, 11/17]);
                        [   5    - %pi ]
                        [              ]
(%o2)                   [         11   ]
                        [ 1.0b0   --   ]
                        [         17   ]


(%i3) b : matrix ([%e], [sin(1)]);
                           [   %e   ]
(%o3)                      [        ]
                           [ sin(1) ]


(%i4) x : dgesv (A, b);
                     [ 0.6903756431559864  ]
(%o4)                [                     ]
                     [ 0.23351098255295172 ]


(%i5) dlange (inf_norm, b - A . x);
(%o5)                 2.220446049250313e-16
```

<!-- category: Numerical -->
<!-- keywords: dgesvd -->
<!-- signatures: dgesvd(A), dgesvd(A, left_p, right_p) -->
### Function: dgesvd (A)

Computes the singular value decomposition (SVD) of a matrix *A*,
comprising the singular values and, optionally, the left and right singular vectors.
All elements of *A* must be integer or floating point numbers.
*A* might or might not be square (same number of rows and columns).


To make use of this function, you must load the LaPack package via
`load("lapack")`.


Let $m$ be the number of rows, and $n$ the number of columns of *A*.
The singular value decomposition of
$\mathbf{A}$
comprises three matrices,
$\mathbf{U},$
$\mathbf{\Sigma},$
and
$\mathbf{V},$
such that






$$\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$$


$${\bf A} = {\bf U} {\bf \Sigma} {\bf V}^T$$




where
$\mathbf{U}$
is an $m$-by-$m$ unitary matrix,
$\mathbf{\Sigma}$
is an $m$-by-$n$ diagonal matrix,
and
$\mathbf{V}$
is an $n$-by-$n$ unitary matrix.


Let
$\mathbf{\sigma}_i$
be a diagonal element of
$\mathbf{\Sigma},$
that is,
$\mathbf{\Sigma}_{ii} = \sigma_i.$
The elements
$\sigma_i$
are the so-called singular values of
$\mathbf{A};$
these are real and nonnegative, and returned in descending order.
The first
$\min(m, n)$
columns of
$\mathbf{U}$
and
$\mathbf{V}$
are the left and right singular vectors of
$\mathbf{A}.$
Note that `dgesvd` returns the transpose of
$\mathbf{V},$
not
$\mathbf{V}$
itself.


`dgesvd(A)` computes only the singular values of *A*.
`dgesvd(A, left_p, right_p)` computes the singular values of *A*
and the left singular vectors when $left_p = true$
and the right singular vectors when $right_p = true$.


A list of three items is returned.
The first item is a list of the singular values.
The second item is `false` or the matrix of left singular vectors.
The third item is `false` or the matrix of right singular vectors.


Example:


















```maxima
maxima
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
(%o4)     [[14.4744, 6.38637, 0.452547], false, false]


(%i5) [sigma, U, VT] : dgesvd (M, true, true);
(%o5) [[14.4744, 6.38637, 0.452547], 
[ - 0.256731  0.00816168   0.959029    - 0.119523 ]
[                                                 ]
[ - 0.526456   0.672116   - 0.206236   - 0.478091 ]
[                                                 ], 
[  0.107997   - 0.532278  - 0.0708315  - 0.83666  ]
[                                                 ]
[ - 0.803287  - 0.514659  - 0.180867    0.239046  ]
[ - 0.374486  - 0.538209  - 0.755044 ]
[                                    ]
[  0.130623   - 0.836799    0.5317   ]]
[                                    ]
[ - 0.917986   0.100488    0.383672  ]


(%i6) m : length (U);
(%o6)                           4


(%i7) n : length (VT);
(%o7)                           3


(%i8) Sigma:
  genmatrix(lambda ([i, j], if i=j then sigma[i] else 0),
            m, n);
                 [ 14.4744     0        0     ]
                 [                            ]
                 [    0     6.38637     0     ]
(%o8)            [                            ]
                 [    0        0     0.452547 ]
                 [                            ]
                 [    0        0        0     ]


(%i9) U . Sigma . VT - M;
          [  1.11022e-15        0.0       1.77636e-15 ]
          [                                           ]
          [  1.33227e-15    1.66533e-15       0.0     ]
(%o9)     [                                           ]
          [ - 4.44089e-16  - 8.88178e-16  4.44089e-16 ]
          [                                           ]
          [  8.88178e-16    1.77636e-15   8.88178e-16 ]


(%i10) transpose (U) . U;
       [     1.0      5.55112e-17    2.498e-16     2.77556e-17  ]
       [                                                        ]
       [ 5.55112e-17      1.0       5.55112e-17    4.16334e-17  ]
(%o10) [                                                        ]
       [  2.498e-16   5.55112e-17       1.0       - 2.08167e-16 ]
       [                                                        ]
       [ 2.77556e-17  4.16334e-17  - 2.08167e-16       1.0      ]


(%i11) VT . transpose (VT);
          [      1.0           0.0      - 5.55112e-17 ]
          [                                           ]
(%o11)    [      0.0           1.0       5.55112e-17  ]
          [                                           ]
          [ - 5.55112e-17  5.55112e-17       1.0      ]
```

<!-- category: Numerical -->
<!-- keywords: dlange, zlange -->
<!-- signatures: dlange(norm, A), zlange(norm, A) -->
### Function: dlange (norm, A)

Computes a norm or norm-like function of the matrix *A*.  If
*A* is a real matrix, use `dlange`.  For a matrix with
complex elements, use `zlange`.


To make use of this function, you must load the LaPack package via
`load("lapack")`.


`norm` specifies the kind of norm to be computed:


**max** — Compute
$\max(|{\bf A}_{ij}|)$
where $i$ and $j$ range over
the rows and columns, respectively, of
${\bf A}.$
Note that this function is not a proper matrix norm.
**one_norm** — Compute the
$L_1$
norm of
${\bf A},$
that is, the maximum of the sum of the absolute value of elements in each column.
**inf_norm** — Compute the
$L_\infty$
norm of
${\bf A},$
that is, the maximum of the sum of the absolute value of elements in each row.
**frobenius** — Compute the Frobenius norm of
${\bf A},$
that is, the square root of the sum of squares of the matrix elements.

<!-- category: Numerical -->
<!-- keywords: zgeev -->
<!-- signatures: zgeev(A), zgeev(A, right_p, left_p) -->
### Function: zgeev (A)

Like `dgeev`, but the matrix
${\bf A}$
is complex.


To make use of this function, you must load the LaPack package via
`load("lapack")`.

See also: `dgeev`.

<!-- category: Numerical -->
<!-- keywords: zheev -->
<!-- signatures: zheev(A), zheev(A, eigvec_p) -->
### Function: zheev (A)

Like `dgeev`, but the matrix
${\bf A}$
is assumed to be a square
complex Hermitian matrix. If *eigvec_p* is `true`, then the
eigenvectors of the matrix are also computed.


To make use of this function, you must load the LaPack package via
`load("lapack")`.


No check is made that the matrix
${\bf A}$
is, in fact, Hermitian.


A list of two items is returned, as in `dgeev`: a list of
eigenvalues, and `false` or the matrix of the eigenvectors.















```maxima
maxima
(%i1) load("lapack")$

(%i2) M: matrix(
     [9.14 +%i*0.00 ,   -4.37 -%i*9.22 ,  -1.98 -%i*1.72 ,  -8.96 -%i*9.50],
     [-4.37 +%i*9.22 ,  -3.35 +%i*0.00 ,   2.25 -%i*9.51 ,   2.57 +%i*2.40],
     [-1.98 +%i*1.72 ,   2.25 +%i*9.51 ,  -4.82 +%i*0.00 ,  -3.24 +%i*2.04],
     [-8.96 +%i*9.50 ,   2.57 -%i*2.40 ,  -3.24 -%i*2.04 ,   8.44 +%i*0.00]);
               [      9.14      ]         [ - 9.22 %i - 4.37 ]
               [                ]         [                  ]
               [ 9.22 %i - 4.37 ]         [      - 3.35      ]
(%o2)  Col 1 = [                ] Col 2 = [                  ]
               [ 1.72 %i - 1.98 ]         [  9.51 %i + 2.25  ]
               [                ]         [                  ]
               [ 9.5 %i - 8.96  ]         [  2.57 - 2.4 %i   ]
                 [ - 1.72 %i - 1.98 ]         [ - 9.5 %i - 8.96 ]
                 [                  ]         [                 ]
                 [  2.25 - 9.51 %i  ]         [  2.4 %i + 2.57  ]
         Col 3 = [                  ] Col 4 = [                 ]
                 [      - 4.82      ]         [ 2.04 %i - 3.24  ]
                 [                  ]         [                 ]
                 [ - 2.04 %i - 3.24 ]         [      8.44       ]


(%i3) zheev(M);
(%o3) [[- 16.004746472094734, - 6.764970154793324, 
                   6.6657114535070985, 25.51400517338097], false]

(%i4) E: zheev(M,true)$

(%i5) E[1];
(%o5) [- 16.004746472094737, - 6.764970154793325, 
                           6.665711453507101, 25.514005173380962]


(%i6) E[2];
               [  0.26746505331727455 %i + 0.21754535866650165  ]
               [                                                ]
               [  0.002696730886619885 %i + 0.6968836773391712  ]
(%o6)  Col 1 = [                                                ]
               [ - 0.6082406376714117 %i - 0.012106142926979313 ]
               [                                                ]
               [              0.15930818580950368               ]
         [  0.26449374706674444 %i + 0.4773693349937472   ]
         [                                                ]
         [ - 0.28523890360316206 %i - 0.14143627420116733 ]
 Col 2 = [                                                ]
         [  0.2654607680986639 %i + 0.44678181171841735   ]
         [                                                ]
         [               0.5750762708542709               ]
         [  0.28106497673059216 %i - 0.13352639282451817  ]
         [                                                ]
         [  0.28663101328695556 %i - 0.4536971347853274   ]
 Col 3 = [                                                ]
         [ - 0.29336843237542953 %i - 0.49549724255410565 ]
         [                                                ]
         [               0.5325337537576771               ]
         [ - 0.5737316575503476 %i - 0.39661467994277055 ]
         [                                               ]
         [ 0.018265026190214573 %i + 0.35305577043870173 ]
 Col 4 = [                                               ]
         [ 0.16737009000854253 %i + 0.01476684746229564  ]
         [                                               ]
         [              0.6002632636961784               ]
```

See also: `dgeev`.

