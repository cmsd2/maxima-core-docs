## LinearAlgebra

### Function: addcol (M, list_1, ..., list_n)

Appends the column(s) given by the one
or more lists (or matrices) onto the matrix *M*.


See also `addrow` and `append`.

See also: `addrow`, `append`.

### Function: addmatrices (f, M_1, ..., M_n)

Using the function *f* as the addition function, return the sum of the
matrices *M_1*, ..., *M_n*.  The function *f* must accept any
number of arguments (a Maxima nary function).


Examples:









```maxima
(%i1) m1 : matrix([1,2],[3,4])$
(%i2) m2 : matrix([7,8],[9,10])$
(%i3) addmatrices('max,m1,m2);
(%o3) matrix([7,8],[9,10])
(%i4) addmatrices('max,m1,m2,5*m1);
(%o4) matrix([7,10],[15,20])
```

### Function: addrow (M, list_1, ..., list_n)

Appends the row(s) given by the one or
more lists (or matrices) onto the matrix *M*.


See also `addcol` and `append`.

See also: `addcol`, `append`.

### Function: adjoint (M)

Returns the adjoint of the matrix *M*.
The adjoint matrix is the transpose of the matrix of cofactors of *M*.

### Function: augcoefmatrix (eqn_1, ..., eqn_m, x_1, ..., x_n)

Returns the augmented coefficient
matrix for the variables *x_1*, ..., *x_n* of the system of linear
equations *eqn_1*, ..., *eqn_m*.  This is the coefficient matrix
with a column adjoined for the constant terms in each equation (i.e., those
terms not dependent upon *x_1*, ..., *x_n*).







```maxima
maxima
(%i1) m: [2*x - (a - 1)*y = 5*b, c + b*y + a*x = 0]$

(%i2) augcoefmatrix (m, [x, y]);
                       [ 2  1 - a  - 5 b ]
(%o2)                  [                 ]
                       [ a    b      c   ]
```

### Function: blockmatrixp (M)

Return true if and only if *M* is a matrix and every entry of 
*M* is a matrix.

### Function: cauchy_matrix (cauchy_matrix, x_1, x_2, ..., x_m, y_1, y_2, ..., y_n, cauchy_matrix, x_1, x_2, ..., x_n)

Returns a `n` by *m* Cauchy matrix with the elements *a[i,j]* 
= 1/(*x_i*+*y_i*).  The second argument of `cauchy_matrix` is 
optional.  For this case the elements of the Cauchy matrix are  
*a[i,j]* = 1/(*x_i*+*x_j*).


Remark: In the literature the Cauchy matrix can be found defined in two forms.
A second definition is *a[i,j]* = 1/(*x_i*-*y_i*).


Examples:







```maxima
maxima

(%i1) cauchy_matrix([x1, x2], [y1, y2]);
                      [    1        1    ]
                      [ -------  ------- ]
                      [ y1 + x1  y2 + x1 ]
(%o1)                 [                  ]
                      [    1        1    ]
                      [ -------  ------- ]
                      [ y1 + x2  y2 + x2 ]


(%i2) cauchy_matrix([x1, x2]);
                      [   1         1    ]
                      [  ----    ------- ]
                      [  2 x1    x2 + x1 ]
(%o2)                 [                  ]
                      [    1       1     ]
                      [ -------   ----   ]
                      [ x2 + x1   2 x2   ]
```

### Function: charpoly (M, x)

Returns the characteristic polynomial for the matrix *M*
with respect to variable *x*.  That is,
`determinant (M - diagmatrix (length (M), x))`.













```maxima
maxima

(%i1) a: matrix ([3, 1], [2, 4]);
                            [ 3  1 ]
(%o1)                       [      ]
                            [ 2  4 ]


(%i2) expand (charpoly (a, lambda));
                           2
(%o2)                lambda  - 7 lambda + 10


(%i3) (programmode: true, solve (%));
(%o3)               [lambda = 5, lambda = 2]


(%i4) matrix ([x1], [x2]);
                             [ x1 ]
(%o4)                        [    ]
                             [ x2 ]


(%i5) ev (a . % - lambda*%, %th(2)[1]);
                          [ x2 - 2 x1 ]
(%o5)                     [           ]
                          [ 2 x1 - x2 ]


(%i6) %[1, 1] = 0;
(%o6)                     x2 - 2 x1 = 0


(%i7) x2^2 + x1^2 = 1;
                            2     2
(%o7)                     x2  + x1  = 1


(%i8) solve ([%th(2), %], [x1, x2]);
                  1               2
(%o8) [[x1 = - -------, x2 = - -------], 
               sqrt(5)         sqrt(5)
                                             1             2
                                    [x1 = -------, x2 = -------]]
                                          sqrt(5)       sqrt(5)
```

### Function: cholesky (cholesky, M, cholesky, M, field)

Return the Cholesky factorization of the matrix selfadjoint (or hermitian)
matrix *M*.  The second argument defaults to ’generalring.’ For a
description of the possible values for *field*, see `lu_factor`.

### Function: coefmatrix (eqn_1, ..., eqn_m, x_1, ..., x_n)

Returns the coefficient matrix for the
variables *x_1*, ..., *x_n* of the system of linear equations
*eqn_1*, ..., *eqn_m*.






```maxima
maxima

(%i1) coefmatrix([2*x-(a-1)*y+5*b = 0, b*y+a*x = 3], [x,y]);
                          [ 2  1 - a ]
(%o1)                     [          ]
                          [ a    b   ]
```

### Function: col (M, i)

Returns the *i*’th column of the matrix *M*.
The return value is a matrix.


The matrix returned by `col` does not share memory with the argument *M*;
a modification to the return value does not modify *M*.


Examples:


`col` returns the *i*’th column of the matrix *M*.









```maxima
maxima

(%i1) abc: matrix ([12, 14, -4], [2, x, b], [3*y, -7, 9]);
                        [ 12   14   - 4 ]
                        [               ]
(%o1)                   [  2    x    b  ]
                        [               ]
                        [ 3 y  - 7   9  ]


(%i2) col (abc, 1);
                             [ 12  ]
                             [     ]
(%o2)                        [  2  ]
                             [     ]
                             [ 3 y ]


(%i3) col (abc, 2);
                             [ 14  ]
                             [     ]
(%o3)                        [  x  ]
                             [     ]
                             [ - 7 ]


(%i4) col (abc, 3);
                             [ - 4 ]
                             [     ]
(%o4)                        [  b  ]
                             [     ]
                             [  9  ]
```


The matrix returned by `col` does not share memory with the argument.
In this example,
assigning a new value to `aa2` does not modify `aa`.










```maxima
maxima

(%i1) aa: matrix ([1, 2, x], [7, y, 3]);
                           [ 1  2  x ]
(%o1)                      [         ]
                           [ 7  y  3 ]


(%i2) aa2: col (aa, 2);
                              [ 2 ]
(%o2)                         [   ]
                              [ y ]


(%i3) aa2[2, 1]: 123;
(%o3)                          123


(%i4) aa2;
                             [  2  ]
(%o4)                        [     ]
                             [ 123 ]


(%i5) aa;
                           [ 1  2  x ]
(%o5)                      [         ]
                           [ 7  y  3 ]
```

### Function: columnop (M, i, j, theta)

If *M* is a matrix, return the matrix that results from doing the column
operation `C_i <- C_i - theta * C_j`. If *M* doesn’t have a row
*i* or *j*, signal an error.

### Function: columnspace (M)

If *M* is a matrix, return `span (v_1, ..., v_n)`, where the set
`{v_1, ..., v_n}` is a basis for the column space of *M*.  The span 
of the empty set is `{0}`.  Thus, when the column space has only
one member, return `span ()`.

### Function: columnswap (M, i, j)

If *M* is a matrix, swap columns *i* and *j*.  If *M* doesn’t
have a column *i* or *j*, signal an error.

### Function: columnvector (L)

Returns a matrix of one column and `length (L)` rows,
containing the elements of the list *L*.


`covect` is a synonym for `columnvector`.


`load ("eigen")` loads this function.



This is useful if you want to use parts of the outputs of
the functions in this package in matrix calculations.


Example:







```maxima
maxima
(%i1) load ("eigen")$

(%i2) columnvector ([aa, bb, cc, dd]);
                             [ aa ]
                             [    ]
                             [ bb ]
(%o2)                        [    ]
                             [ cc ]
                             [    ]
                             [ dd ]
```

### Function: copymatrix (M)

Returns a copy of the matrix *M*.  This is the only way
to make a copy aside from copying *M* element by element.


Note that an assignment of one matrix to another, as in `m2: m1`, does not
copy `m1`.  An assignment `m2 [i,j]: x` or `setelmx(x, i, j, m2)`
also modifies `m1 [i,j]`.  Creating a copy with `copymatrix` and then
using assignment creates a separate, modified copy.

### Function: ctranspose (M)

Return the complex conjugate transpose of the matrix *M*.  The function
`ctranspose` uses `matrix_element_transpose` to transpose each matrix
element.

### Function: determinant (M)

Computes the determinant of *M* by a method similar to
Gaussian elimination.



The form of the result depends upon the setting of the switch `ratmx`.



There is a special routine for computing sparse determinants which is called
when the switches `ratmx` and `sparse` are both `true`.


`display_determinant_bars` governs the display of determinants.

See also: `ratmx`, `sparse`.

### Variable: detout

Default value: `false`


When `detout` is `true`, the determinant of a
matrix whose inverse is computed is factored out of the inverse.


For this switch to have an effect `doallmxops` and `doscmxops` should
be `false` (see their descriptions).  Alternatively this switch can be
given to `ev` which causes the other two to be set correctly.


Example:










```maxima
maxima

(%i1) m: matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]

(%i2) detout: true$
(%i3) doallmxops: false$
(%i4) doscmxops: false$

(%i5) invert (m);
                          [  d   - b ]
                          [          ]
                          [ - c   a  ]
(%o5)                     ------------
                           a d - b c
```

See also: `doallmxops`, `doscmxops`, `ev`.

### Function: diag_matrix (d_1, d_2, ..., d_n)

Return a diagonal matrix with diagonal entries *d_1*, *d_2*, ...,
*d_n*.  When the diagonal entries are matrices, the zero entries of the
returned matrix are zero matrices of the appropriate size; for example:







```maxima
(%i1) diag_matrix(diag_matrix(1,2),diag_matrix(3,4));

                            [ [ 1  0 ]  [ 0  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  2 ]  [ 0  0 ] ]
(%o1)                       [                    ]
                            [ [ 0  0 ]  [ 3  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  0 ]  [ 0  4 ] ]
(%i2) diag_matrix(p,q);

                                   [ p  0 ]
(%o2)                              [      ]
                                   [ 0  q ]
```

### Function: diagmatrix (n, x)

Returns a diagonal matrix of size *n* by *n* with the diagonal elements
all equal to *x*.  `diagmatrix (n, 1)` returns an identity matrix
(same as `ident (n)`).


*n* must evaluate to an integer, otherwise `diagmatrix` complains with
an error message.


*x* can be any kind of expression, including another matrix.  If *x* is
a matrix, it is not copied; all diagonal elements refer to the same instance,
*x*.

### Variable: display_determinant_bars

Default value: `true`


When `display_determinant_bars` is `true`,
a determinant noun expression which has a literal matrix as its sole argument
is displayed with a vertical bar on either side.


Otherwise, `display_determinant_bars` is `false`,
or the determinant is not a noun expression,
or its argument is not a literal matrix;
in these cases, the expression is displayed as an ordinary function call.

### Function: display_matrix_brackets ()

Default value: `true`


When `display_matrix_brackets` is `true`,
matrices are displayed with brackets (square braces) to the left and right.


When `display_matrix_brackets` is `false`,
matrices are not displayed with brackets;
only the matrix elements are displayed.

### Function: display_matrix_padding_horizontal ()

Default value: `true`


When `display_matrix_padding_horizontal` is `true`,
matrices are displayed with spaces between successive columns,
and a space before the first column and a space after the last column.


When `display_matrix_padding_horizontal` is `false`,
matrices are not displayed with spaces between successive columns,
and no space before the first column and no space after the last column.
Successive columns are immediately adjacent to each other,
and the first column is immediately adjacent to the left bracket,
and the last column is immediately adjacent to the right bracket,
if the brackets are present (see `display_matrix_brackets`).

    

See also `display_005fmatrix_005fpadding_005fvertical`.


Examples:









```maxima
maxima

(%i1) display_matrix_padding_horizontal;
(%o1)                         true
(%i2) foo: matrix ([a, b, c], [d, e, f], [g, h, i]);
                           ┌         ┐
                           │ a  b  c │
                           │         │
(%o2)                      │ d  e  f │
                           │         │
                           │ g  h  i │
                           └         ┘


(%i3) display_matrix_padding_horizontal: false;
(%o3)                         false
(%i4) foo;
                              ┌   ┐
                              │abc│
                              │   │
(%o4)                         │def│
                              │   │
                              │ghi│
                              └   ┘
```

See also: `display_matrix_brackets`, `display_matrix_padding_vertical`.

### Function: display_matrix_padding_vertical ()

Default value: `true`


When `display_matrix_padding_vertical` is `true`,
matrices are displayed with an empty line between successive rows.


When `display_matrix_padding_vertical` is `false`,
matrices are not displayed with an empty line between successive rows;
successive rows are immediately adjacent to each other.


See also `display_005fmatrix_005fpadding_005fhorizontal`.


Examples:









```maxima
maxima

(%i1) display_matrix_padding_vertical;
(%o1)                         true
(%i2) foo: matrix ([a, b, c], [d, e, f], [g, h, i]);
                           ┌         ┐
                           │ a  b  c │
                           │         │
(%o2)                      │ d  e  f │
                           │         │
                           │ g  h  i │
                           └         ┘


(%i3) display_matrix_padding_vertical: false;
(%o3)                         false
(%i4) foo;
                           ┌         ┐
                           │ a  b  c │
(%o4)                      │ d  e  f │
                           │ g  h  i │
                           └         ┘
```

See also: `display_matrix_padding_horizontal`.

### Variable: doallmxops

Default value: `true`


When `doallmxops` is `true`,

all operations relating to matrices are carried out.
When it is `false` then the setting of the
individual `dot` switches govern which operations are performed.

### Variable: domxexpt

Default value: `true`


When `domxexpt` is `true`,
a matrix exponential, `exp (M)` where *M* is a matrix, is
interpreted as a matrix with element `[i,j]` equal to `exp (m[i,j])`.
Otherwise `exp (M)` evaluates to `exp (ev(M))`.


`domxexpt` affects all expressions of the form
`base^power` where *base* is an expression assumed scalar
or constant, and *power* is a list or matrix.


Example:










```maxima
maxima

(%i1) m: matrix ([1, %i], [a+b, %pi]);
                         [   1    %i  ]
(%o1)                    [            ]
                         [ b + a  %pi ]

(%i2) domxexpt: false$

(%i3) (1 - c)^m;
                             [   1    %i  ]
                             [            ]
                             [ b + a  %pi ]
(%o3)                 (1 - c)

(%i4) domxexpt: true$

(%i5) (1 - c)^m;
                  [                      %i  ]
                  [    1 - c      (1 - c)    ]
(%o5)             [                          ]
                  [        b + a         %pi ]
                  [ (1 - c)       (1 - c)    ]
```

### Variable: domxmxops

Default value: `true`


When `domxmxops` is `true`, all matrix-matrix or
matrix-list operations are carried out (but not scalar-matrix
operations); if this switch is `false` such operations are not carried out.

### Variable: domxnctimes

Default value: `false`


When `domxnctimes` is `true`, non-commutative products of
matrices are carried out.

### Variable: dontfactor

Default value: `[]`


`dontfactor` may be set to a list of variables with respect to which
factoring is not to occur.  (The list is initially empty.) Factoring also will
not take place with respect to any variables which are less important, according
the variable ordering assumed for canonical rational expression (CRE) form, than
those on the `dontfactor` list.

### Variable: doscmxops

Default value: `false`


When `doscmxops` is `true`, scalar-matrix operations are
carried out.

### Variable: doscmxplus

Default value: `false`


When `doscmxplus` is `true`, scalar-matrix operations yield
a matrix result.  This switch is not subsumed under `doallmxops`.

See also: `doallmxops`.

### Variable: dot0nscsimp

Default value: `true`



When `dot0nscsimp` is `true`, a non-commutative product of zero
and a nonscalar term is simplified to a commutative product.

### Variable: dot0simp

Default value: `true`



When `dot0simp` is `true`,
a non-commutative product of zero and
a scalar term is simplified to a commutative product.

### Variable: dot1simp

Default value: `true`



When `dot1simp` is `true`,
a non-commutative product of one and
another term is simplified to a commutative product.

### Variable: dotassoc

Default value: `true`


When `dotassoc` is `true`, an expression `(A.B).C` simplifies to
`A.(B.C)`.

### Variable: dotconstrules

Default value: `true`


When `dotconstrules` is `true`, a non-commutative product of a
constant and another term is simplified to a commutative product.


Turning on this flag effectively turns on `dot0simp`,
`dot0nscsimp`, and `dot1simp` as well.

See also: `dot0simp`, `dot0nscsimp`, `dot1simp`.

### Variable: dotdistrib

Default value: `false`


When `dotdistrib` is `true`, an expression `A.(B + C)` simplifies
to `A.B + A.C`.

### Variable: dotexptsimp

Default value: `true`


When `dotexptsimp` is `true`, an expression `A.A` simplifies to
`A^^2`.

### Variable: dotident

Default value: 1


`dotident` is the value returned by `X^^0`.

### Function: dotproduct (u, v)

Return the dotproduct of vectors *u* and *v*.  This is the same as
`conjugate (transpose (u)) . v`.  The arguments *u* and
*v* must be column vectors.

### Variable: dotscrules

Default value: `false`


When `dotscrules` is `true`, an expression `A.SC` or `SC.A`
simplifies to `SC*A` and `A.(SC*B)` simplifies to `SC*(A.B)`.

### Function: echelon (M)

Returns the echelon form of the matrix *M*,
as produced by Gaussian elimination.
The echelon form is computed from *M*
by elementary row operations such that the first
non-zero element in each row in the resulting matrix is one and the
column elements under the first one in each row are all zero.


`triangularize` also carries out Gaussian elimination, but it does not
normalize the leading non-zero element in each row.


`lu_factor` and `cholesky` are other functions which yield
triangularized matrices.







```maxima
maxima

(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]


(%i2) echelon (M);
                  [ 1  - 8  - 5      - 2     ]
                  [                          ]
                  [         28       11      ]
                  [ 0   1   --       --      ]
(%o2)             [         37       37      ]
                  [                          ]
                  [              37 bb - 119 ]
                  [ 0   0    1   ----------- ]
                  [              37 aa - 313 ]
```

See also: `triangularize`, `lu_factor`, `cholesky`.

### Function: eigens_by_jacobi (eigens_by_jacobi, A, eigens_by_jacobi, A, field_type)

Computes the eigenvalues and eigenvectors of *A* by the method of Jacobi
rotations.  *A* must be a symmetric matrix (but it need not be positive
definite nor positive semidefinite).  *field_type* indicates the
computational field, either `floatfield` or `bigfloatfield`.
If *field_type* is not specified, it defaults to `floatfield`.


The elements of *A* must be numbers or expressions which evaluate to numbers
via `float` or `bfloat` (depending on *field_type*).


Examples:











```maxima
(%i1) S: matrix([1/sqrt(2), 1/sqrt(2)],[-1/sqrt(2), 1/sqrt(2)]);
                     [     1         1    ]
                     [  -------   ------- ]
                     [  sqrt(2)   sqrt(2) ]
(%o1)                [                    ]
                     [      1        1    ]
                     [ - -------  ------- ]
                     [   sqrt(2)  sqrt(2) ]
(%i2) L : matrix ([sqrt(3), 0], [0, sqrt(5)]);
                      [ sqrt(3)     0    ]
(%o2)                 [                  ]
                      [    0     sqrt(5) ]
(%i3) M : S . L . transpose (S);
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- + -------  ------- - ------- ]
            [    2         2        2         2    ]
(%o3)       [                                      ]
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- - -------  ------- + ------- ]
            [    2         2        2         2    ]
(%i4) eigens_by_jacobi (M);
The largest percent change was 0.1454972243679
The largest percent change was 0.0
number of sweeps: 2
number of rotations: 1
(%o4) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i5) float ([[sqrt(3), sqrt(5)], S]);
(%o5) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i6) eigens_by_jacobi (M, bigfloatfield);
The largest percent change was 1.454972243679028b-1
The largest percent change was 0.0b0
number of sweeps: 2
number of rotations: 1
(%o6) [[1.732050807568877b0, 2.23606797749979b0], 
                [  7.071067811865475b-1   7.071067811865475b-1 ]
                [                                              ]]
                [ - 7.071067811865475b-1  7.071067811865475b-1 ]
```

### Function: eigenvalues (M)

Returns a list of two lists containing the eigenvalues of the matrix *M*.
The first sublist of the return value is the list of eigenvalues of the
matrix, and the second sublist is the list of the
multiplicities of the eigenvalues in the corresponding order.


`eivals` is a synonym for `eigenvalues`.


`eigenvalues` calls the function `solve` to find the roots of the
characteristic polynomial of the matrix.  Sometimes `solve` may not be able
to find the roots of the polynomial; in that case some other functions in this
package (except `innerproduct`, `unitvector`,
`columnvector` and `gramschmidt`) will not work.



Sometimes `solve` may find only a subset of the roots of the polynomial.
This may happen when the factoring of the polynomial contains polynomials
of degree 5 or more. In such cases a warning message is displayed and the
only the roots found and their corresponding multiplicities are returned.


In some cases the eigenvalues found by `solve` may be complicated
expressions.  (This may happen when `solve` returns a not-so-obviously real
expression for an eigenvalue which is known to be real.)  It may be possible to
simplify the eigenvalues using some other functions.



The package `eigen.mac` is loaded automatically when
`eigenvalues` or `eigenvectors` is referenced.
If `eigen.mac` is not already loaded,
`load ("eigen")` loads it.
After loading, all functions and variables in the package are available.



For matrices consisting of only floating-point values, see also
`dgeev`.

See also: `solve`, `innerproduct`, `unitvector`, `columnvector`, `gramschmidt`, `eigenvectors`, `dgeev`.

### Function: eigenvectors (M)

Computes eigenvectors of the matrix *M*.
The return value is a list of two elements.
The first is a list of the eigenvalues of *M*
and a list of the multiplicities of the eigenvalues.
The second is a list of lists of eigenvectors.
There is one list of eigenvectors for each eigenvalue.
There may be one or more eigenvectors in each list.


`eivects` is a synonym for `eigenvectors`.


The package `eigen.mac` is loaded automatically when
`eigenvalues` or `eigenvectors` is referenced.
If `eigen.mac` is not already loaded,
`load ("eigen")` loads it.
After loading, all functions and variables in the package are available.


Note that `eigenvectors` internally calls `eigenvalues` to
obtain eigenvalues. So, when `eigenvalues` returns a subset of
all the eigenvalues, the `eigenvectors` returns the corresponding
subset of the all the eigenvectors, with the same warning displayed as
`eigenvalues`.


The flags that affect this function are:


`nondiagonalizable` is set to `true` or `false` depending on
whether the matrix is nondiagonalizable or diagonalizable after
`eigenvectors` returns.


`hermitianmatrix` when `true`, causes the degenerate
eigenvectors of the Hermitian matrix to be orthogonalized using the
Gram-Schmidt algorithm.


`knowneigvals` when `true` causes the `eigen` package to assume
the eigenvalues of the matrix are known to the user and stored under the global
name `listeigvals`.  `listeigvals` should be set to a list similar
to the output `eigenvalues`.


The function `algsys` is used here to solve for the eigenvectors.
Sometimes if the eigenvalues are messy, `algsys` may not be able to find a
solution.  In some cases, it may be possible to simplify the eigenvalues by
first finding them using `eigenvalues` command and then using other
functions to reduce them to something simpler.  Following simplification,
`eigenvectors` can be called again with the `knowneigvals` flag set
to `true`.


See also `eigenvalues`.


For matrices consisting of only floating-point values, see also
`dgeev`.


Examples:


A matrix which has just one eigenvector per eigenvalue.









```maxima
maxima

(%i1) M1: matrix ([11, -1], [1, 7]);
                           [ 11  - 1 ]
(%o1)                      [         ]
                           [ 1    7  ]


(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[9 - sqrt(3), sqrt(3) + 9], [1, 1]], 
                        [[[1, sqrt(3) + 2]], [[1, 2 - sqrt(3)]]]]


(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                       val  = 9 - sqrt(3)
                          1

                            mult  = 1
                                1

                    vec  = [[1, sqrt(3) + 2]]
                       1

                       val  = sqrt(3) + 9
                          2

                            mult  = 1
                                2

                    vec  = [[1, 2 - sqrt(3)]]
                       2

(%o3)                         done
```


A matrix which has two eigenvectors for one eigenvalue (namely 2).









```maxima
maxima

(%i1) M1 : matrix ([0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]);
                         [ 0  1  0  0 ]
                         [            ]
                         [ 0  0  0  0 ]
(%o1)                    [            ]
                         [ 0  0  2  0 ]
                         [            ]
                         [ 0  0  0  2 ]


(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[0, 2], [2, 2]], [[[1, 0, 0, 0]], 
                                   [[0, 0, 1, 0], [0, 0, 0, 1]]]]


(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                            val  = 0
                               1

                            mult  = 2
                                1

                      vec  = [[1, 0, 0, 0]]
                         1

                            val  = 2
                               2

                            mult  = 2
                                2

               vec  = [[0, 0, 1, 0], [0, 0, 0, 1]]
                  2

(%o3)                         done
```

See also: `eigenvalues`, `algsys`, `dgeev`.

### Function: ematrix (m, n, x, i, j)

Returns an *m* by *n* matrix, all elements of which
are zero except for the `[i, j]` element which is *x*.

### Function: entermatrix (m, n)

Returns an *m* by *n* matrix, reading the elements interactively.


If *n* is equal to *m*, Maxima prompts for the type of the matrix
(diagonal, symmetric, antisymmetric, or general) and for each element.
Each response is terminated by a semicolon `;` or dollar sign `$`.


If *n* is not equal to *m*,
Maxima prompts for each element.


The elements may be any expressions, which are evaluated.
`entermatrix` evaluates its arguments.



```maxima
maxima
(%i1) n: 3$
(%i2) m: entermatrix (n, n)$

Is the matrix  1. Diagonal  2. Symmetric  3. Antisymmetric 
4. General
Answer 1, 2, 3 or 4 : 
1$
Row 1 Column 1: 
(a+b)^n$
Row 2 Column 2: 
(a+b)^(n+1)$
Row 3 Column 3: 
(a+b)^(n+2)$

Matrix entered.
(%i3) m;
                [        3                     ]
                [ (b + a)      0         0     ]
                [                              ]
(%o3)           [                  4           ]
                [    0      (b + a)      0     ]
                [                              ]
                [                            5 ]
                [    0         0      (b + a)  ]
```

### Function: genmatrix (genmatrix, a, i_2, j_2, i_1, j_1, genmatrix, a, i_2, j_2, i_1, genmatrix, a, i_2, j_2)

Returns a matrix generated from *a*, taking element
`a[i_1, j_1]` as the upper-left element and
`a[i_2, j_2]` as the lower-right element of the matrix.
Here *a* is a declared array (created by `array` but not by
`make_array`) or a `hashed array`, or a `memoizing function`, or a lambda
expression of two arguments.  (A `memoizing function` is created like other functions
with `:=` or `define`, but arguments are enclosed in square
brackets instead of parentheses.)


If *j_1* is omitted, it is assumed equal to *i_1*.
If both *j_1* and *i_1* are omitted, both are assumed equal to 1.


If a selected element `i,j` of the array is undefined,
the matrix will contain a symbolic element `a[i,j]`.


Examples:













```maxima
maxima

(%i1) h [i, j] := 1 / (i + j - 1);
                                    1
(%o1)                  h     := ---------
                        i, j    i + j - 1


(%i2) genmatrix (h, 3, 3);
                           [    1  1 ]
                           [ 1  -  - ]
                           [    2  3 ]
                           [         ]
                           [ 1  1  1 ]
(%o2)                      [ -  -  - ]
                           [ 2  3  4 ]
                           [         ]
                           [ 1  1  1 ]
                           [ -  -  - ]
                           [ 3  4  5 ]


(%i3) array (a, fixnum, 2, 2);
(%o3)                           a


(%i4) a [1, 1] : %e;
(%o4)                          %e


(%i5) a [2, 2] : %pi;
(%o5)                          %pi


(%i6) genmatrix (a, 2, 2);
                           [ %e   0  ]
(%o6)                      [         ]
                           [ 0   %pi ]


(%i7) genmatrix (lambda ([i, j], j - i), 3, 3);
                         [  0    1   2 ]
                         [             ]
(%o7)                    [ - 1   0   1 ]
                         [             ]
                         [ - 2  - 1  0 ]


(%i8) genmatrix (B, 2, 2);
                        [ B      B     ]
                        [  1, 1   1, 2 ]
(%o8)                   [              ]
                        [ B      B     ]
                        [  2, 1   2, 2 ]
```

See also: `make_array`, `hashed-array`, `memoizing-function`, `:=`, `define`.

### Function: get_lu_factors (x)

When `x = lu_factor (A)`, then `get_lu_factors` returns a
list of the form `[P, L, U]`, where *P* is a permutation matrix,
*L* is lower triangular with ones on the diagonal, and *U* is upper
triangular, and `A = P L U`.

### Function: gramschmidt (gramschmidt, x, gramschmidt, x, F)

Carries out the Gram-Schmidt orthogonalization algorithm on *x*, which is
either a matrix or a list of lists.  *x* is not modified by
`gramschmidt`.  The inner product employed by `gramschmidt` is
*F*, if present, otherwise the inner product is the function
`innerproduct`.


If *x* is a matrix, the algorithm is applied to the rows of *x*.  If
*x* is a list of lists, the algorithm is applied to the sublists, which must
have equal numbers of elements.  In either case, the return value is a list of
lists, the sublists of which are orthogonal and span the same space as *x*.
If the dimension of the span of *x* is less than the number of rows or
sublists, some sublists of the return value are zero.


`factor` is called at each stage of the algorithm to simplify intermediate
results.  As a consequence, the return value may contain factored integers.


`load("eigen")` loads this function.


Example:


Gram-Schmidt algorithm using default inner product function.









```maxima
maxima
(%i1) load ("eigen")$

(%i2) x: matrix ([1, 2, 3], [9, 18, 30], [12, 48, 60]);
                         [ 1   2   3  ]
                         [            ]
(%o2)                    [ 9   18  30 ]
                         [            ]
                         [ 12  48  60 ]


(%i3) y: gramschmidt (x);
                       2      2            4     3
                      3      3   3 5      2  3  2  3
(%o3)  [[1, 2, 3], [- ---, - --, ---], [- ----, ----, 0]]
                      2 7    7   2 7       5     5


(%i4) map (innerproduct, [y[1], y[2], y[3]], [y[2], y[3], y[1]]);
(%o4)                       [0, 0, 0]
```


Gram-Schmidt algorithm using a specified inner product function.










```maxima
maxima
(%i1) load ("eigen")$

(%i2) ip (f, g) := integrate (f * g, u, a, b);
(%o2)          ip(f, g) := integrate(f g, u, a, b)


(%i3) y: gramschmidt ([1, sin(u), cos(u)], ip), a=-%pi/2, b=%pi/2;
                               %pi cos(u) - 2
(%o3)              [1, sin(u), --------------]
                                    %pi


(%i4) map (ip, [y[1], y[2], y[3]], [y[2], y[3], y[1]]), a=-%pi/2,
         b=%pi/2;
(%o4)                       [0, 0, 0]
```

See also: `innerproduct`, `factor`.

### Function: hankel (hankel, col, hankel, col, row)

Return a Hankel matrix *H*.  The first column of *H* is *col*;
except for the first entry, the last row of *H* is *row*.  The
default for *row* is the zero vector with the same length as *col*.

### Function: hessian (f, x)

Returns the Hessian matrix of *f* with respect to the list of variables
*x*.  The `(i, j)`-th element of the Hessian matrix is
`diff(f, x[i], 1, x[j], 1)`.


Examples:








```maxima
(%i1) hessian (x * sin (y), [x, y]);
                     [   0       cos(y)   ]
(%o1)                [                    ]
                     [ cos(y)  - x sin(y) ]
(%i2) depends (F, [a, b]);
(%o2)                       [F(a, b)]
(%i3) hessian (F, [a, b]);
                        [   2      2   ]
                        [  d F    d F  ]
                        [  ---   ----- ]
                        [    2   da db ]
                        [  da          ]
(%o3)                   [              ]
                        [   2      2   ]
                        [  d F    d F  ]
                        [ -----   ---  ]
                        [ da db     2  ]
                        [         db   ]
```

### Function: hilbert_matrix (n)

Return the *n* by *n* Hilbert matrix.  When *n* isn’t a positive
integer, signal an error.

### Function: ident (n)

Returns an *n* by *n* identity matrix.

### Function: identfor (identfor, M, identfor, M, fld)

Return an identity matrix that has the same shape as the matrix
*M*.  The diagonal entries of the identity matrix are the 
multiplicative identity of the field *fld*; the default for
*fld* is *generalring*.


The first argument *M* should be a square matrix or a non-matrix.  When
*M* is a matrix, each entry of *M* can be a square matrix – thus
*M* can be a blocked Maxima matrix.  The matrix can be blocked to any
(finite) depth.


See also `zerofor`

See also: `zerofor`.

### Function: innerproduct (x, y)

Returns the inner product (also called the scalar product or dot product) of
*x* and *y*, which are lists of equal length, or both 1-column or 1-row
matrices of equal length.  The return value is `conjugate (x) . y`,
where `.` is the noncommutative multiplication operator.


`load ("eigen")` loads this function.


`inprod` is a synonym for `innerproduct`.

### Function: invert (M)

Returns the inverse of the matrix *M*.
The inverse is computed via the LU decomposition.


When `ratmx` is `true`,
elements of *M* are converted to canonical rational expressions (CRE),
and the elements of the return value are also CRE.


When `ratmx` is `false`,
elements of *M* are not converted to a common representation.
In particular, float and bigfloat elements are not converted to rationals.


When `detout` is `true`, the determinant is factored out of the inverse.
The global flags `doallmxops` and `doscmxops` must be `false`
to prevent the determinant from being absorbed into the inverse.
`xthru` can multiply the determinant into the inverse.


`invert` does not apply any simplifications to the elements of the inverse
apart from the default arithmetic simplifications.
`ratsimp` and `expand` can apply additional simplifications.
In particular, when *M* has polynomial elements,
`expand(invert(M))` might be preferable.


`invert(M)` is equivalent to `M^^-1`.

See also: `ratmx`, `detout`, `doallmxops`, `doscmxops`, `xthru`, `invert`, `ratsimp`, `expand`.

### Function: invert_by_adjoint (M)

Returns the inverse of the matrix *M*.
The inverse is computed by the adjoint method.


`invert_by_adjoint` honors the `ratmx` and `detout` flags,
the same as `invert`.

See also: `ratmx`, `detout`, `invert`.

### Function: invert_by_lu (M, (rng generalring))

Invert a matrix *M* by using the LU factorization.  The LU factorization
is done using the ring *rng*.

### Function: jacobian (f, x)

Returns the Jacobian matrix of the list of functions *f* with respect to
the list of variables *x*.  The `(i, j)`-th element of the Jacobian
matrix is `diff(f[i], x[j])`.


Examples:








```maxima
(%i1) jacobian ([sin (u - v), sin (u * v)], [u, v]);
                  [ cos(v - u)  - cos(v - u) ]
(%o1)             [                          ]
                  [ v cos(u v)   u cos(u v)  ]
(%i2) depends ([F, G], [y, z]);
(%o2)                  [F(y, z), G(y, z)]
(%i3) jacobian ([F, G], [y, z]);
                           [ dF  dF ]
                           [ --  -- ]
                           [ dy  dz ]
(%o3)                      [        ]
                           [ dG  dG ]
                           [ --  -- ]
                           [ dy  dz ]
```

### Function: kronecker_product (A, B)

Return the Kronecker product of the matrices *A* and *B*.

### Function: linalg_rank (M)

Return the rank of the matrix *M*. This function is equivalent to
function `rank`, but it uses a different algorithm: it finds the
`columnspace` of the matrix and counts its elements, since the rank
of a matrix is the dimension of its column space. 







```maxima
(%i1) linalg_rank(matrix([1,2],[2,4]));
(%o1)                           1


(%i2) linalg_rank(matrix([1,b],[c,d]));
(%o2)                           2
```

See also: `rank`, `columnspace`.

### Function: list_matrix_entries (M)

Returns a list containing the elements of the matrix *M*.


Example:






```maxima
maxima

(%i1) list_matrix_entries(matrix([a,b],[c,d]));
(%o1)                     [a, b, c, d]
```

### Variable: lmxchar

Default value: `[`


`lmxchar` is the character displayed as the left delimiter of a matrix.
See also `rmxchar`.


`lmxchar` is only used when `display2d_unicode` is `false`.


Example:








```maxima
maxima
(%i1) display2d_unicode: false $
(%i2) lmxchar: "|"$

(%i3) matrix ([a, b, c], [d, e, f], [g, h, i]);
                           | a  b  c ]
                           |         ]
(%o3)                      | d  e  f ]
                           |         ]
                           | g  h  i ]
```

See also: `rmxchar`.

### Function: locate_matrix_entry (M, r_1, c_1, r_2, c_2, f, rel)

The first argument must be a matrix; the arguments
*r_1* through *c_2* determine a sub-matrix of *M* that consists of
rows *r_1* through *r_2* and columns *c_1* through *c_2*.


Find an entry in the sub-matrix *M* that satisfies some property.
Three cases:


(1) `rel = 'bool` and *f* a predicate: 


Scan the sub-matrix from left to right then top to bottom,
and return the index of the first entry that satisfies the 
predicate *f*.  If no matrix entry satisfies *f*, return `false`.


(2) `rel = 'max` and *f* real-valued:


Scan the sub-matrix looking for an entry that maximizes *f*.
Return the index of a maximizing entry.


(3) `rel = 'min` and *f* real-valued:


Scan the sub-matrix looking for an entry that minimizes *f*.
Return the index of a minimizing entry.

### Function: lu_backsub (M, b)

When `M = lu_factor (A, field)`,
then `lu_backsub (M, b)` solves the linear
system `A x = b`.


The *n* by *m* matrix `b`, with *n* the number of 
rows of the matrix `A`, contains one right hand side per column. If 
there is only one right hand side then `b` must be a *n* by 1
matrix.


Each column of the matrix `x=lu_backsub (M, b)` is the 
solution corresponding to the respective column of `b`.


Examples:













```maxima
(%i1) A : matrix ([1 - z, 3], [3, 8 - z]);
                               [ 1 - z    3   ]
(%o1)                          [              ]
                               [   3    8 - z ]
(%i2) M : lu_factor (A,generalring);
               [ 1 - z          3         ]
               [                          ]
(%o2)         [[   3              9       ], [1, 2], generalring]
               [ -----  (- z) - ----- + 8 ]
               [ 1 - z          1 - z     ]
(%i3) b : matrix([a],[c]);
                                     [ a ]
(%o3)                                [   ]
                                     [ c ]
(%i4) x : lu_backsub(M,b);
                           [               3 a     ]
                           [       3 (c - -----)   ]
                           [              1 - z    ]
                           [ a - ----------------- ]
                           [               9       ]
                           [     (- z) - ----- + 8 ]
                           [             1 - z     ]
                           [ --------------------- ]
(%o4)                      [         1 - z         ]
                           [                       ]
                           [            3 a        ]
                           [       c - -----       ]
                           [           1 - z       ]
                           [   -----------------   ]
                           [             9         ]
                           [   (- z) - ----- + 8   ]
                           [           1 - z       ]
(%i5) ratsimp(A . x - b);
                                     [ 0 ]
(%o5)                                [   ]
                                     [ 0 ]
(%i6) B : matrix([a,d],[c,f]);
                                   [ a  d ]
(%o6)                              [      ]
                                   [ c  f ]
(%i7) x : lu_backsub(M,B);
               [               3 a                    3 d     ]
               [       3 (c - -----)          3 (f - -----)   ]
               [              1 - z                  1 - z    ]
               [ a - -----------------  d - ----------------- ]
               [               9                      9       ]
               [     (- z) - ----- + 8      (- z) - ----- + 8 ]
               [             1 - z                  1 - z     ]
               [ ---------------------  --------------------- ]
(%o7)          [         1 - z                  1 - z         ]
               [                                              ]
               [            3 a                    3 d        ]
               [       c - -----              f - -----       ]
               [           1 - z                  1 - z       ]
               [   -----------------      -----------------   ]
               [             9                      9         ]
               [   (- z) - ----- + 8      (- z) - ----- + 8   ]
               [           1 - z                  1 - z       ]
(%i8) ratsimp(A . x - B);
                                   [ 0  0 ]
(%o8)                              [      ]
                                   [ 0  0 ]
```

### Function: lu_factor (M, field)

Return a list of the form `[LU, perm, fld]`, or
`[LU, perm, fld, lower-cnd upper-cnd]`, where


(1) The matrix *LU* contains the factorization of *M* in a packed form.
    Packed form means three things: First, the rows of *LU* are permuted
    according to the list *perm*.  If, for example, *perm* is the list
    `[3,2,1]`, the actual first row of the *LU* factorization is the
    third row of the matrix *LU*.  Second, the lower triangular factor of
    m is the lower triangular part of *LU* with the diagonal entries
    replaced by all ones.  Third, the upper triangular factor of *M* is the
    upper triangular part of *LU*.


(2) When the field is either `floatfield` or `complexfield`, the
    numbers *lower-cnd* and *upper-cnd* are lower and upper bounds for
    the infinity norm condition number of *M*.  For all fields, the
    condition number might not be estimated; for such fields, `lu_factor`
    returns a two item list.  Both the lower and upper bounds can differ from
    their true values by arbitrarily large factors.  (See also `mat_cond`.)

   
  

The argument *M* must be a square matrix.


  

The optional argument *fld* must be a symbol that determines a ring or
  field.  The pre-defined fields and rings are:


  

(a) `generalring`      – the ring of Maxima expressions,


  

(b) `floatfield`       – the field of floating point numbers of the
                                 type double,


  

(c) `complexfield`     – the field of complex floating point numbers of
                                 the type double,


  

(d) `crering`          – the ring of Maxima CRE expressions,


  

(e) `rationalfield`    – the field of rational numbers,


  

(f) `runningerror`     – track the all floating point rounding errors,


  

(g) `noncommutingring` – the ring of Maxima expressions where
                                 multiplication is the non-commutative dot
                                 operator.


When the field is `floatfield`, `complexfield`, or
`runningerror`, the algorithm uses partial pivoting; for all
other fields, rows are switched only when needed to avoid a zero
pivot.


Floating point addition arithmetic isn’t associative, so the meaning
of ’field’ differs from the mathematical definition.


A member of the field `runningerror` is a two member Maxima list
of the form `[x,n]`,where *x* is a floating point number and
`n` is an integer.  The relative difference between the ’true’
value of `x` and `x` is approximately bounded by the machine
epsilon times `n`.  The running error bound drops some terms that
of the order the square of the machine epsilon.


There is no user-interface for defining a new field.  A user that is
familiar with Common Lisp should be able to define a new field.  To do
this, a user must define functions for the arithmetic operations and
functions for converting from the field representation to Maxima and
back.  Additionally, for ordered fields (where partial pivoting will be
used), a user must define functions for the magnitude and for
comparing field members.  After that all that remains is to define a
Common Lisp structure `mring`.  The file `mring` has many
examples.

 

To compute the factorization, the first task is to convert each matrix
entry to a member of the indicated field.  When conversion isn’t
possible, the factorization halts with an error message.  Members of
the field needn’t be Maxima expressions.  Members of the
`complexfield`, for example, are Common Lisp complex numbers.  Thus
after computing the factorization, the matrix entries must be
converted to Maxima expressions.


See also  `get_lu_factors`.


Examples:















```maxima
(%i1) w[i,j] := random (1.0) + %i * random (1.0);
(%o1)          w     := random(1.) + %i random(1.)
                i, j
(%i2) showtime : true$
Evaluation took 0.00 seconds (0.00 elapsed)
(%i3) M : genmatrix (w, 100, 100)$
Evaluation took 7.40 seconds (8.23 elapsed)
(%i4) lu_factor (M, complexfield)$
Evaluation took 28.71 seconds (35.00 elapsed)
(%i5) lu_factor (M, generalring)$
Evaluation took 109.24 seconds (152.10 elapsed)
(%i6) showtime : false$

(%i7) M : matrix ([1 - z, 3], [3, 8 - z]); 
                        [ 1 - z    3   ]
(%o7)                   [              ]
                        [   3    8 - z ]
(%i8) lu_factor (M, generalring);
          [ 1 - z         3        ]
          [                        ]
(%o8)    [[   3            9       ], [1, 2], generalring]
          [ -----  - z - ----- + 8 ]
          [ 1 - z        1 - z     ]
(%i9) get_lu_factors (%);
                  [   1    0 ]  [ 1 - z         3        ]
        [ 1  0 ]  [          ]  [                        ]
(%o9)  [[      ], [   3      ], [                9       ]]
        [ 0  1 ]  [ -----  1 ]  [   0    - z - ----- + 8 ]
                  [ 1 - z    ]  [              1 - z     ]
(%i10) %[1] . %[2] . %[3];
                        [ 1 - z    3   ]
(%o10)                  [              ]
                        [   3    8 - z ]
```

See also: `mat_cond`, `get_lu_factors`.

### Function: mat_cond (mat_cond, M, 1, mat_cond, M, inf)

Return the *p*-norm matrix condition number of the matrix
*m*.  The allowed values for *p* are 1 and *inf*.  This
function uses the LU factorization to invert the matrix *m*.  Thus
the running time for `mat_cond` is proportional to the cube of
the matrix size; `lu_factor` determines lower and upper bounds
for the infinity norm condition number in time proportional to the
square of the matrix size.

### Function: mat_fullunblocker (M)

If *M* is a block matrix, unblock the matrix to all levels.  If *M* is
a matrix, return *M*; otherwise, signal an error.

### Function: mat_norm (mat_norm, M, 1, mat_norm, M, inf, mat_norm, M, frobenius)

Return the matrix *p*-norm of the matrix *M*.  The allowed values for
*p* are 1, `inf`, and `frobenius` (the Frobenius matrix norm).
The matrix *M* should be an unblocked matrix.

### Function: mat_trace (M)

Return the trace of the matrix *M*.  If *M* isn’t a matrix, return a
noun form.  When *M* is a block matrix, `mat_trace(M)` returns
the same value as does `mat_trace(mat_unblocker(m))`.

### Function: mat_unblocker (M)

If *M* is a block matrix, unblock *M* one level.  If *M* is a
matrix, `mat_unblocker (M)` returns *M*; otherwise, signal an error.


Thus if each entry of *M* is matrix, `mat_unblocker (M)` returns an 
unblocked matrix, but if each entry of *M* is a block matrix,
`mat_unblocker (M)` returns a block matrix with one less level of blocking.


If you use block matrices, most likely you’ll want to set
`matrix_element_mult` to `"."` and `matrix_element_transpose` to
`'transpose`.  See also `mat_fullunblocker`.


Example:









```maxima
(%i1) A : matrix ([1, 2], [3, 4]);
                            [ 1  2 ]
(%o1)                       [      ]
                            [ 3  4 ]
(%i2) B : matrix ([7, 8], [9, 10]);
                            [ 7  8  ]
(%o2)                       [       ]
                            [ 9  10 ]
(%i3) matrix ([A, B]);

                     [ [ 1  2 ]  [ 7  8  ] ]
(%o3)                [ [      ]  [       ] ]
                     [ [ 3  4 ]  [ 9  10 ] ]

(%i4) mat_unblocker (%);
                         [ 1  2  7  8  ]
(%o4)                    [             ]
                         [ 3  4  9  10 ]
```

See also: `mat_fullunblocker`.

### Function: matrix (row_1, ..., row_n)

Returns a rectangular matrix which has the rows *row_1*, ...,
*row_n*.  Each row is a list of expressions.  All rows must be the same
length.


The operations `+` (addition), `-` (subtraction), `*`
(multiplication), and `/` (division), are carried out element by element
when the operands are two matrices, a scalar and a matrix, or a matrix and a
scalar.  The operation `^` (exponentiation, equivalently `**`)
is carried out element by element if the operands are a scalar and a matrix or
a matrix and a scalar, but not if the operands are two matrices.

All operations are normally carried out in full,
including `.` (noncommutative multiplication).


Matrix multiplication is represented by the noncommutative multiplication
operator `.`.  The corresponding noncommutative exponentiation operator
is `^^`.  For a matrix `A`, `A.A = A^^2`
and `A^^-1` is the inverse of *A*, if it exists.
`A^^-1` is equivalent to `invert(A)`.


There are switches for controlling simplification of expressions involving dot
and matrix-list operations.  These are
`doallmxops`, `domxexpt`, `domxmxops`,
`doscmxops`, and `doscmxplus`.



There are additional options which are related to matrices.  These are:
`lmxchar`, `rmxchar`, `ratmx`,
`listarith`, `detout`, `scalarmatrix` and
`sparse`.



There are a number of functions which take matrices as arguments or yield
matrices as return values.
See `eigenvalues`, `eigenvectors`, `determinant`,
`charpoly`, `genmatrix`, `addcol`,
`addrow`, `copymatrix`, `transpose`,
`echelon`, and `rank`.



Option variables `display_matrix_brackets` and `display_matrix_padding_vertical`
govern the display of matrices.


Examples:



- *
Construction of matrices from lists.






```maxima
maxima

(%i1) x: matrix ([17, 3], [-8, 11]);
                           [ 17   3  ]
(%o1)                      [         ]
                           [ - 8  11 ]


(%i2) y: matrix ([%pi, %e], [a, b]);
                           [ %pi  %e ]
(%o2)                      [         ]
                           [  a   b  ]
```


- *
Addition, element by element.


```maxima
(%i3) x + y;
                      [ %pi + 17  %e + 3 ]
(%o3)                 [                  ]
                      [  a - 8    b + 11 ]
```


- *
Subtraction, element by element.


```maxima
(%i4) x - y;
                      [ 17 - %pi  3 - %e ]
(%o4)                 [                  ]
                      [ - a - 8   11 - b ]
```


- *
Multiplication, element by element.


```maxima
(%i5) x * y;
                        [ 17 %pi  3 %e ]
(%o5)                   [              ]
                        [ - 8 a   11 b ]
```


- *
Division, element by element.


```maxima
(%i6) x / y;
                        [ 17       - 1 ]
                        [ ---  3 %e    ]
                        [ %pi          ]
(%o6)                   [              ]
                        [   8    11    ]
                        [ - -    --    ]
                        [   a    b     ]
```


- *
Matrix to a scalar exponent, element by element.


```maxima
(%i7) x ^ 3;
                         [ 4913    27  ]
(%o7)                    [             ]
                         [ - 512  1331 ]
```


- *
Scalar base to a matrix exponent, element by element.


```maxima
(%i8) exp(y); 
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o8)                    [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
Matrix base to a matrix exponent.  This is not carried out element by element.
See also `matrixexp`.


```maxima
(%i9) x ^ y;
                                [ %pi  %e ]
                                [         ]
                                [  a   b  ]
                     [ 17   3  ]
(%o9)                [         ]
                     [ - 8  11 ]
```


- *
Noncommutative matrix multiplication.


```maxima
(%i10) x . y;
                  [ 3 a + 17 %pi  3 b + 17 %e ]
(%o10)            [                           ]
                  [ 11 a - 8 %pi  11 b - 8 %e ]
(%i11) y . x;
                [ 17 %pi - 8 %e  3 %pi + 11 %e ]
(%o11)          [                              ]
                [  17 a - 8 b     11 b + 3 a   ]
```


- *
Noncommutative matrix exponentiation.
A scalar base *b* to a matrix power *M*
is carried out element by element and so `b^^m` is the same as `b^m`.


```maxima
(%i12) x ^^ 3;
                        [  3833   1719 ]
(%o12)                  [              ]
                        [ - 4584  395  ]
(%i13) %e ^^ y;

                         [   %pi    %e ]
                         [ %e     %e   ]
(%o13)                   [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
A matrix raised to a -1 exponent with noncommutative exponentiation is the
matrix inverse, if it exists.


```maxima
(%i14) x ^^ -1;
                         [ 11      3  ]
                         [ ---  - --- ]
                         [ 211    211 ]
(%o14)                   [            ]
                         [  8    17   ]
                         [ ---   ---  ]
                         [ 211   211  ]
(%i15) x . (x ^^ -1);
                            [ 1  0 ]
(%o15)                      [      ]
                            [ 0  1 ]
```

See also: `doallmxops`, `domxexpt`, `domxmxops`, `doscmxops`, `doscmxplus`, `lmxchar`, `rmxchar`, `ratmx`, `listarith`, `detout`, `sparse`, `eigenvalues`, `eigenvectors`, `determinant`, `charpoly`, `genmatrix`, `addcol`, `addrow`, `copymatrix`, `transpose`, `echelon`, `rank`, `display_matrix_brackets`, `display_matrix_padding_vertical`, `matrixexp`.

### Variable: matrix_element_add

Default value: `+`


`matrix_element_add` is the operation 
invoked in place of addition in a matrix multiplication.
`matrix_element_add` can be assigned any n-ary operator
(that is, a function which handles any number of arguments).
The assigned value may be the name of an operator enclosed in quote marks,
the name of a function,
or a lambda expression.


See also `matrix_element_mult` and `matrix_005felement_005ftranspose`.


Example:










```maxima
maxima
(%i1) matrix_element_add: "*"$
(%i2) matrix_element_mult: "^"$

(%i3) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o3)                      [         ]
                           [ d  e  f ]


(%i4) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o4)                      [         ]
                           [ x  y  z ]


(%i5) aa . transpose (bb);
                     [  u  v  w   x  y  z ]
                     [ a  b  c   a  b  c  ]
(%o5)                [                    ]
                     [  u  v  w   x  y  z ]
                     [ d  e  f   d  e  f  ]
```

See also: `matrix_element_mult`, `matrix_element_transpose`.

### Variable: matrix_element_mult

Default value: `*`


`matrix_element_mult` is the operation 
invoked in place of multiplication in a matrix multiplication.
`matrix_element_mult` can be assigned any binary operator.
The assigned value may be the name of an operator enclosed in quote marks,
the name of a function,
or a lambda expression.


The dot operator `.` is a useful choice in some contexts.


See also `matrix_element_add` and `matrix_005felement_005ftranspose`.


Example:











```maxima
maxima
(%i1) matrix_element_add: lambda ([[x]], sqrt (apply ("+", x)))$
(%i2) matrix_element_mult: lambda ([x, y], (x - y)^2)$

(%i3) [a, b, c] . [x, y, z];
                          2          2          2
(%o3)         sqrt((c - z)  + (b - y)  + (a - x) )


(%i4) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o4)                      [         ]
                           [ d  e  f ]


(%i5) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o5)                      [         ]
                           [ x  y  z ]


(%i6) aa . transpose (bb);
               [             2          2          2  ]
               [ sqrt((c - w)  + (b - v)  + (a - u) ) ]
(%o6)  Col 1 = [                                      ]
               [             2          2          2  ]
               [ sqrt((f - w)  + (e - v)  + (d - u) ) ]
                         [             2          2          2  ]
                         [ sqrt((c - z)  + (b - y)  + (a - x) ) ]
                 Col 2 = [                                      ]
                         [             2          2          2  ]
                         [ sqrt((f - z)  + (e - y)  + (d - x) ) ]
```

See also: `matrix_element_add`, `matrix_element_transpose`.

### Variable: matrix_element_transpose

Default value: `false`


`matrix_element_transpose` is the operation 
applied to each element of a matrix when it is transposed.
`matrix_element_mult` can be assigned any unary operator.
The assigned value may be the name of an operator enclosed in quote marks,
the name of a function, or a lambda expression.


When `matrix_element_transpose` equals `transpose`,
the `transpose` function is applied to every element.
When `matrix_element_transpose` equals `nonscalars`,
the `transpose` function is applied to every nonscalar element.
If some element is an atom, the `nonscalars` option applies
`transpose` only if the atom is declared nonscalar,
while the `transpose` option always applies `transpose`.


The default value, `false`, means no operation is applied.


See also `matrix_element_add` and `matrix_005felement_005fmult`.


Examples:














```maxima
maxima
(%i1) declare (a, nonscalar)$

(%i2) transpose ([a, b]);
                              [ a ]
(%o2)                         [   ]
                              [ b ]

(%i3) matrix_element_transpose: nonscalars$

(%i4) transpose ([a, b]);
                        [ transpose(a) ]
(%o4)                   [              ]
                        [      b       ]

(%i5) matrix_element_transpose: transpose$

(%i6) transpose ([a, b]);
                        [ transpose(a) ]
(%o6)                   [              ]
                        [ transpose(b) ]

(%i7) matrix_element_transpose: lambda ([x], realpart(x) - %i*imagpart(x))$

(%i8) m: matrix ([1 + 5*%i, 3 - 2*%i], [7*%i, 11]);
                     [ 5 %i + 1  3 - 2 %i ]
(%o8)                [                    ]
                     [   7 %i       11    ]


(%i9) transpose (m);
                      [ 1 - 5 %i  - 7 %i ]
(%o9)                 [                  ]
                      [ 2 %i + 3    11   ]
```

See also: `matrix_element_mult`, `transpose`, `matrix_element_add`.

### Function: matrix_size (M)

Return a two member list that gives the number of rows and columns, respectively
of the matrix *M*.

### Function: matrixexp (matrixexp, M, matrixexp, M, n, matrixexp, M, V)

Calculates the matrix exponential
$e^{M\cdot V}$
















. Instead of the vector *V* a number *n* can be specified as the second
argument. If this argument is omitted `matrixexp` replaces it by `1`.


The matrix exponential of a matrix *M* can be expressed as a power series:

$$e^M=\sum_{k=0}^\infty{\left(\frac{M^k}{k!}\right)}$$


$$e^M=\sum_{k=0}^\infty{\left(\frac{M^k}{k!}\right)}$$

### Function: matrixmap (f, M)

Returns a matrix with element `i,j` equal to `f(M[i,j])`.


See also `map`, `fullmap`, `fullmapl`, and
`apply`.

See also: `map`, `fullmap`, `fullmapl`, `apply`.

### Function: matrixp (expr)

Returns `true` if *expr* is a matrix, otherwise `false`.

### Function: mattrace (M)

Returns the trace (that is, the sum of the elements on the main diagonal) of
the square matrix *M*.


`mattrace` is called by `ncharpoly`, an alternative to Maxima’s
`charpoly`.



`load ("nchrpl")` loads this function.

See also: `ncharpoly`, `charpoly`.

### Function: minor (M, i, j)

Returns the *i*, *j* minor of the matrix *M*.  That is, *M*
with row *i* and column *j* removed.

### Function: ncharpoly (M, x)

Returns the characteristic polynomial of the matrix *M*
with respect to *x*.  This is an alternative to Maxima’s `charpoly`.


`ncharpoly` works by computing traces of powers of the given matrix,
which are known to be equal to sums of powers of the roots of the
characteristic polynomial.  From these quantities the symmetric
functions of the roots can be calculated, which are nothing more than
the coefficients of the characteristic polynomial.  `charpoly` works by

forming the determinant of `x * ident [n] - a`.  Thus
`ncharpoly` wins, for example, in the case of large dense matrices filled
with integers, since it avoids polynomial arithmetic altogether.


`load ("nchrpl")` loads this file.

See also: `charpoly`.

### Function: newdet (M)

Computes the determinant of the matrix *M* by the Johnson-Gentleman tree 
minor algorithm.  `newdet` returns the result in CRE form.

### Function: nullity (M)

If *M* is a matrix, return the dimension of the nullspace of *M*.

### Function: nullspace (M)

If *M* is a matrix, return `span (v_1, ..., v_n)`, where the set
`{v_1, ..., v_n}` is a basis for the nullspace of *M*.  The span of
the empty set is `{0}`.  Thus, when the nullspace has only one member,
return `span ()`.

### Function: orthogonal_complement (v_1, ..., v_n)

Return `span (u_1, ..., u_m)`, where the set `{u_1, ..., u_m}` is a 
basis for the orthogonal complement of the set `(v_1, ..., v_n)`.


Each vector *v_1* through *v_n* must be a column vector.

### Function: permanent (M)

Computes the permanent of the matrix *M* by the Johnson-Gentleman tree
minor algorithm.  A permanent is like a determinant but with no sign changes.
`permanent` returns the result in CRE form.


See also `newdet`.

### Function: polytocompanion (p, x)

If *p* is a polynomial in *x*, return the companion matrix of *p*.
For a monic polynomial *p* of degree *n*, we have
`p = (-1)^n charpoly (polytocompanion (p, x))`.


When *p* isn’t a polynomial in *x*, signal an error.

### Function: ptriangularize (M, v)

If *M* is a matrix with each entry a polynomial in *v*, return 
a matrix *M2* such that


(1) *M2* is upper triangular,


(2) `M2 = E_n ... E_1 M`,
where *E_1* through *E_n* are elementary matrices 
whose entries are polynomials in *v*,


(3) `|det (M)| = |det (M2)|`,


Note: This function doesn’t check that every entry is a polynomial in *v*.

### Function: rank (M)

Computes the rank of the matrix *M*.  That is, the order of the
largest non-singular subdeterminant of *M*.



*rank* may return the
wrong answer if it cannot determine that a matrix element that is
equivalent to zero is indeed so.

### Variable: ratmx

Default value: `false`


When `ratmx` is `false`, determinant and matrix
addition, subtraction, and multiplication are performed in the
representation of the matrix elements and cause the result of
matrix inversion to be left in general representation.


When `ratmx` is `true`,
the 4 operations mentioned above are performed in CRE form and the
result of matrix inverse is in CRE form.  Note that this may
cause the elements to be expanded (depending on the setting of `ratfac`)
which might not always be desired.

See also: `ratfac`.

### Variable: rmxchar

Default value: `]`


`rmxchar` is the character drawn on the right-hand side of a matrix.


`rmxchar` is only used when `display2d_unicode` is `false`.


See also `lmxchar`.

See also: `lmxchar`.

### Function: row (M, i)

Returns the *i*’th row of the matrix *M*.
The return value is a matrix.


The matrix returned by `row` shares memory with the argument *M*;
a modification to the return value modifies *M*.


Examples:


`row` returns the *i*’th row of the matrix *M*.









```maxima
maxima

(%i1) abc: matrix ([12, 14, -4], [2, x, b], [3*y, -7, 9]);
                        [ 12   14   - 4 ]
                        [               ]
(%o1)                   [  2    x    b  ]
                        [               ]
                        [ 3 y  - 7   9  ]


(%i2) row (abc, 1);
(%o2)                    [ 12  14  - 4 ]


(%i3) row (abc, 2);
(%o3)                      [ 2  x  b ]


(%i4) row (abc, 3);
(%o4)                    [ 3 y  - 7  9 ]
```


The matrix returned by `row` shares memory with the argument.
In this example,
assigning a new value to `aa2` also modifies `aa`.










```maxima
maxima

(%i1) aa: matrix ([1, 2, x], [7, y, 3]);
                           [ 1  2  x ]
(%o1)                      [         ]
                           [ 7  y  3 ]


(%i2) aa2: row (aa, 2);
(%o2)                      [ 7  y  3 ]


(%i3) aa2[1, 3]: 123;
(%o3)                          123


(%i4) aa2;
(%o4)                     [ 7  y  123 ]


(%i5) aa;
                          [ 1  2   x  ]
(%o5)                     [           ]
                          [ 7  y  123 ]
```

### Function: rowop (M, i, j, theta)

If *M* is a matrix, return the matrix that results from doing the
row operation `R_i <- R_i - theta * R_j`.  If *M* doesn’t have a row
*i* or *j*, signal an error.

### Function: rowswap (M, i, j)

If *M* is a matrix, swap rows *i* and *j*.  If *M* doesn’t
have a row *i* or *j*, signal an error.

### Variable: scalarmatrixp

Default value: `true`


When `scalarmatrixp` is `true`, then whenever a 1 x 1 matrix
is produced as a result of computing the dot product of matrices it
is simplified to a scalar, namely the sole element of the matrix.


When `scalarmatrixp` is `all`,
then all 1 x 1 matrices are simplified to scalars.


When `scalarmatrixp` is `false`, 1 x 1 matrices are not simplified
to scalars.

### Function: scalefactors (coordinatetransform)

Here the argument *coordinatetransform* evaluates to the form
`[[expression1, expression2, ...], indeterminate1, indeterminat2, ...]`,
where the variables *indeterminate1*, *indeterminate2*, etc. are the
curvilinear coordinate variables and where a set of rectangular Cartesian
components is given in terms of the curvilinear coordinates by
`[expression1, expression2, ...]`.  `coordinates` is set to the vector
`[indeterminate1, indeterminate2,...]`, and `dimension` is set to the
length of this vector.  SF[1], SF[2], ..., SF[DIMENSION] are set to the
coordinate scale factors, and `sfprod` is set to the product of these scale
factors.  Initially, `coordinates` is `[X, Y, Z]`, `dimension`
is 3, and SF[1]=SF[2]=SF[3]=SFPROD=1, corresponding to 3-dimensional rectangular
Cartesian coordinates.  To expand an expression into physical components in the
current coordinate system, there is a function with usage of the form

### Function: setelmx (x, i, j, M)

Assigns *x* to the (*i*, *j*)’th element of the matrix *M*,
and returns the altered matrix.


`M [i, j]: x` has the same effect,
but returns *x* instead of *M*.

### Function: similaritytransform (M)

`similaritytransform` computes a similarity transform of the matrix
`M`.  It returns a list which is the output of the `uniteigenvectors`
command.  In addition if the flag `nondiagonalizable` is `false` two
global matrices `leftmatrix` and `rightmatrix` are computed.  These
matrices have the property that `leftmatrix . M . rightmatrix` is a
diagonal matrix with the eigenvalues of *M* on the diagonal.  If
`nondiagonalizable` is `true` the left and right matrices are not
computed.


If the flag `hermitianmatrix` is `true` then `leftmatrix` is the
complex conjugate of the transpose of `rightmatrix`.  Otherwise
`leftmatrix` is the inverse of `rightmatrix`.


`rightmatrix` is the matrix the columns of which are the unit
eigenvectors of *M*.  The other flags (see `eigenvalues` and
`eigenvectors`) have the same effects since
`similaritytransform` calls the other functions in the package in order
to be able to form `rightmatrix`.


`load ("eigen")` loads this function.


`simtran` is a synonym for `similaritytransform`.

### Variable: sparse

Default value: `false`


When `sparse` is `true`, and if `ratmx` is `true`, then
`determinant` will use special routines for computing sparse determinants.

### Function: submatrix (submatrix, i_1, ..., i_m, M, j_1, ..., j_n, submatrix, i_1, ..., i_m, M, submatrix, M, j_1, ..., j_n)

Returns a new matrix composed of the matrix *M* with rows *i_1*,
..., *i_m* deleted, and columns *j_1*, ..., *j_n* deleted.

### Function: toeplitz (toeplitz, col, toeplitz, col, row)

Return a Toeplitz matrix *T*.  The first first column of *T* is
*col*; except for the first entry, the first row of *T* is *row*.
The default for *row* is complex conjugate of *col*.  Example:







```maxima
(%i1)  toeplitz([1,2,3],[x,y,z]);

                                  [ 1  y  z ]
                                  [         ]
(%o1)                             [ 2  1  y ]
                                  [         ]
                                  [ 3  2  1 ]

(%i2)  toeplitz([1,1+%i]);

                              [   1     1 - %I ]
(%o2)                         [                ]
                              [ %I + 1    1    ]
```

### Function: transpose (M)

Returns the transpose of *M*.


If *M* is a matrix, the return value is another matrix *N*
such that `N[i,j] = M[j,i]`.


If *M* is a list, the return value is a matrix *N*
of `length (m)` rows and 1 column, such that `N[i,1] = M[i]`.


Otherwise *M* is a symbol,
and the return value is a noun expression `'transpose (M)`.

### Function: triangularize (M)

Returns the upper triangular form of the matrix `M`,
as produced by Gaussian elimination.
The return value is the same as `echelon`,
except that the leading nonzero coefficient in each row is not normalized to 1.


`lu_factor` and `cholesky` are other functions which yield
triangularized matrices.







```maxima
maxima

(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]


(%i2) triangularize (M);
             [ - 1   8         5            2      ]
             [                                     ]
(%o2)        [  0   - 74     - 56         - 22     ]
             [                                     ]
             [  0    0    626 - 74 aa  238 - 74 bb ]
```

### Function: uniteigenvectors (M)

Computes unit eigenvectors of the matrix *M*.
The return value is a list of lists, the first sublist of which is the
output of the `eigenvalues` command, and the other sublists of which are
the unit eigenvectors of the matrix corresponding to those eigenvalues
respectively.



The flags mentioned in the description of the
`eigenvectors` command have the same effects in this one as well.


When `knowneigvects` is `true`, the `eigen` package assumes
that the eigenvectors of the matrix are known to the user and are
stored under the global name `listeigvects`.  `listeigvects` should
be set to a list similar to the output of the `eigenvectors` command.



If `knowneigvects` is set to `true` and the list of eigenvectors is
given the setting of the flag `nondiagonalizable` may not be correct.  If
that is the case please set it to the correct value.  The author assumes that
the user knows what he is doing and will not try to diagonalize a matrix the
eigenvectors of which do not span the vector space of the appropriate dimension.


`load ("eigen")` loads this function.


`ueivects` is a synonym for `uniteigenvectors`.

### Function: unitvector (x)

Returns $x/norm(x)$;
this is a unit vector in the same direction as *x*.


`load ("eigen")` loads this function.


`uvect` is a synonym for `unitvector`.

### Function: vandermonde_matrix (x_1, ..., x_n)

Return a *n* by *n* matrix whose *i*-th row is 
`[1, x_i, x_i^2, ... x_i^(n-1)]`.

### Variable: vect_cross

Default value: `false`



When `vect_cross` is `true`, it allows DIFF(X~Y,T) to work where
~ is defined in SHARE;VECT (where VECT_CROSS is set to `true`, anyway.)

### Function: vectorpotential (givencurl)

Returns the vector potential of a given curl vector, in the current coordinate
system.  `potentialzeroloc` has a similar role as for `potential`, but
the order of the left-hand sides of the equations must be a cyclic permutation
of the coordinate variables.

### Function: vectorsimp (expr)

Applies simplifications and expansions according to the following global flags:



`expandall`, `expanddot`, `expanddotplus`, `expandcross`, `expandcrossplus`,
`expandcrosscross`, `expandgrad`, `expandgradplus`, `expandgradprod`,
`expanddiv`, `expanddivplus`, `expanddivprod`, `expandcurl`, `expandcurlplus`,
`expandcurlcurl`, `expandlaplacian`, `expandlaplacianplus`,
and `expandlaplacianprod`.



All these flags have default value `false`.  The `plus` suffix refers
to employing additivity or distributivity.  The `prod` suffix refers to the
expansion for an operand that is any kind of product.



**expandcrosscross** — Simplifies 
$p \sim (q \sim r)$
to 
$(p . r)q - (p . q)r.$
**expandcurlcurl** — Simplifies 
${\rm curl}\; {\rm curl}\; p$
to 
${\rm grad}\; {\rm div}\; p + {\rm div}\; {\rm grad}\; p.$
**expandlaplaciantodivgrad** — Simplifies 
${\rm laplacian}\; p$
to 
${\rm div}\; {\rm grad}\; p.$
**expandcross** — Enables `expandcrossplus` and `expandcrosscross`.
**expandplus** — Enables `expanddotplus`, `expandcrossplus`, `expandgradplus`,
`expanddivplus`, `expandcurlplus`, and `expandlaplacianplus`.
**expandprod** — Enables `expandgradprod`, `expanddivprod`, and `expandlaplacianprod`.



These flags have all been declared `evflag`.

### Function: zerofor (zerofor, M, zerofor, M, fld)

Return a zero  matrix that has the same shape as the matrix
*M*.  Every entry of the zero matrix is the
additive identity of the field *fld*; the default for
*fld* is *generalring*.


The first argument *M* should be a square matrix or a
non-matrix.  When *M* is a matrix, each entry of *M* can be a
square matrix – thus *M* can be a blocked Maxima matrix.  The
matrix can be blocked to any (finite) depth.


See also `identfor`

See also: `identfor`.

### Function: zeromatrix (m, n)

Returns an *m* by *n* matrix, all elements of which are zero.

### Function: zeromatrixp (M)

If *M* is not a block matrix, return `true` if
`is (equal (e, 0))` is true for each element *e* of the matrix
*M*.  If *M* is a block matrix, return `true` if `zeromatrixp`
evaluates to `true` for each element of *e*.

