## Numerical

### Function: bf_fft (y)

Computes the forward complex fast Fourier transform.  This is the
bigfloat version of `fft` that converts the input to
bigfloats and returns a bigfloat result.

See also: `fft`.

### Function: bf_fmin_cobyla (bf_fmin_cobyla, F, X, Y, bf_fmin_cobyla, F, X, Y, optional_args)

This function is identical to `fmin_cobyla`, except that bigfloat
operations are used, and the default value for *rhoend* is
`10^(fpprec/2)`. 


See `fmin_cobyla` for more information.


`load("bf_fmin_cobyla")` loads this function.

See also: `fmin_cobyla`.

### Function: bf_inverse_fft (y)

Computes the inverse complex fast Fourier transform.  This is the
bigfloat version of `inverse_fft` that converts the input to
bigfloats and returns a bigfloat result.

See also: `inverse_fft`.

### Function: bf_inverse_real_fft (y)

Computes the inverse fast Fourier transform with a real-valued
bigfloat output.  This is the bigfloat version of `inverse_real_fft`.

### Function: bf_real_fft (x)

Computes the forward fast Fourier transform of a real-valued input
returning a bigfloat result.  This is the bigfloat version of
`real_fft`.

### Function: bflevin_u_sum (a, n, n_0)

Estimate `sum(a(n), n, n_0, inf)` using the
Levin u-transform in bigfloat arithmetic.



`bflevin_u_sum` attempts to return the sum of the infinite series
with a precision given by the global variable `fpprec` using bigfloat arithmetic.


See `levin_options` for options to control this function.
`bflevin_u_sum` uses an adaptive algorithm to increase both the number of
terms and the bigfloat precision used for internal calculations
until the estimated error is acceptable.


`load("levin")` loads this function.


See `Examples for levin` for examples.

See also: `fpprec`, `levin_options`, `Examples-for-levin`.

### Function: charfun2 (x, a, b)

The characteristic or indicator function on the half-open interval $[a, b)$,
that is, including *a* and excluding *b*.


Package `interpol` loads this function.


See also `charfun`.


Examples:


When $x >= a$ and $x < b$ evaluates to `true` or `false`,
`charfun2` returns 1 or 0, respectively.








```maxima
maxima
(%i1) load ("interpol") $

(%i2) charfun2 (5, 0, 100);
(%o2)                           1


(%i3) charfun2 (-5, 0, 100);
(%o3)                           0
```


Otherwise, `charfun2` returns a partially-evaluated result in terms of `charfun`.










```maxima
maxima
(%i1) load ("interpol") $

(%i2) charfun2 (t, 0, 100);
(%o2)            charfun((0 <= t) and (t < 100))


(%i3) charfun2 (5, u, v);
(%o3)             charfun((u <= 5) and (5 < v))


(%i4) assume (v > u, u > 5);
(%o4)                    [v > u, u > 5]


(%i5) charfun2 (5, u, v);
(%o5)                           0
```

See also: `charfun`.

### Function: colnew_appsln (colnew_appsln, x, zlen, fspace, ispace)

Return a list of solution values from `colnew_expert` results.


The function arguments are:



**x** — List of x-coordinates to calculate solution.
**zlen** — *mstar*, the length of the solution list z
**fspace** — List *fspace* returned from `colnew_005fexpert`.
**ispace** — List *ispace* returned from `colnew_005fexpert`.

See also: `colnew_expert`.

### Function: colnew_expert (colnew_expert, ncomp, m, aleft, aright, zeta, ipar, ltol, tol, fixpnt, ispace, fspace, iflag, fsub, dfsub, gsub, dgsub, guess)

*colnew_expert* solves mixed-order systems of boundary-value problems (BVPs) in ordinary
differential equations (ODEs) using a numerical collocation method.


*colnew_expert* returns the list [*iflag*, *fspace*, *ispace*].
*iflag* is an error flag.  Lists *fspace* and *ispace* contain the
state of the solution 
and can be: used by `colnew_appsln` to calculate solution values
at arbitrary points in the solution domain; and passed back to *colnew_expert* to restart the solution process
with different arguments. 


The function arguments are:



**ncomp** — Number of differential equations   (ncomp ≤ 20)
**m** — Integer list of length *ncomp*.  
$m_j$
is the order of the $j$-th
differential equation,
with 
$1 \le m_j \le 4$
and 
$m^* = \sum_j m_j \le 40.$
**aleft** — Left end of interval
**aright** — Right end of interval
**zeta** — *zeta* 
$(\zeta)$
is a real list of length 
$m^*.$
$\zeta_j$
is the 
$j$-th boundary or side condition point. The
list 
$\zeta$
must be ordered, 
with  
$\zeta_j \le \zeta_{j+1}.$
All side condition
points must be mesh points in all meshes used,
see description of ipar[11] and fixpnt below.
**ipar** — A integer list of length 11.  The parameters in ipar are:  - * 
*ipar[1]*
    
  - * 
0, if the problem is linear
  - * 
1, if the problem is nonlinear
- * 
*ipar[2]* ( = $k$ )
  Number of collocation points per subinterval , where
$\max_j m_j \le k \le 7.$
  If *ipar[2]*=0 then colnew sets 
$k = \max\left(\max_i m_i + 5, 5 - \max_i m_i\right).$
- * 
*ipar[3]*  ( = $n$ )
  Number of subintervals in the initial mesh.
  If *ipar[3]* = 0 then colnew arbitrarily sets $n = 5$.
- * 
*ipar[4]* ( = ntol )
  Number of solution and derivative tolerances.
  Require 
$0 < {\rm ntol} < m^*.$
- * 
*ipar[5]*  ( = ndimf )
  The length of list *fspace*. Its size provides a constraint on *nmax*.
  Choose ipar[5] according to the formula
${\rm ipar[5]} \ge {\rm nmax} \cdot {\rm nsizef}$
  where
${\rm nsizef} = 4 + 3m^* + (5 + {\rm kd})\times{\rm kdm} + (2m^* - {\rm nrec})\times 2 m^*.$
- * 
*ipar[6]* ( = ndimi )
  The length of list *ispace*. Its size provides a constraint on *nmax*, the maximum
  number of subintervals.  Choose *ipar[6]* according to the formula
${\rm ipar[6]} = {\rm nmax}\times {\rm nsizei}$
  where
${\rm nsizei} = 3 + {\rm kdm}$
  with
$$\eqalign{ {\rm kdm} &= {\rm kd} + m^* \cr {\rm kd} &= k + {\rm ncomp} \cr {\rm nrec} &= {\it number\, of\, right\, end\, boundary\, conditions} \cr }$$ $$\eqalign{
    {\rm kdm} &= {\rm kd} + m^* \cr
    {\rm kd} &= k + {\rm ncomp} \cr
    {\rm nrec} &= {\it number\, of\, right\, end\, boundary\, conditions} \cr
  }$$
.
- * 
*ipar[7]* ( = iprint )
  output control
  
  - * 
-1, for full diagnostic printout
  - * 
0, for selected printout
  - * 
1, for no printout
- * 
*ipar[8]* ( = iread )
    
  - * 
0, causes colnew to generate a uniform initial mesh.
  - * 
1,
     if the initial mesh is provided by the user.  it
     is defined in fspace as follows:  the mesh
     aleft=x[1]<x[2]< ... <x[n]<x[n+1]=aright
     will occupy  fspace[1], ..., fspace[n+1]. the
     user needs to supply only the interior mesh
     points  fspace[j] = x[j], j = 2, ..., n.
  - * 
2,
     if the initial mesh is supplied by the user
     as with *ipar[8]*=1, and in addition no adaptive
     mesh selection is to be done.
- * 
*ipar[9]*  ( = iguess )
  
  - * 
0,
        if no initial guess for the solution is provided
  - * 
1,
        if an initial guess is provided by the user
        in subroutine guess.
  - * 
2,
        if an initial mesh and approximate solution
        coefficients are provided by the user in *fspace*.
        (the former and new mesh are the same).
  - * 
3,
        if a former mesh and approximate solution
        coefficients are provided by the user in *fspace*,
        and the new mesh is to be taken twice as coarse;
        i.e.,every second point from the former mesh.
  - * 
4,
        if in addition to a former initial mesh and
        approximate solution coefficients, a new mesh
        is provided in *fspace* as well.
       (see description of output for further details
        on iguess = 2, 3, and 4.)
- * 
*ipar[10]*
  
  - * 
0, if the problem is regular
  - * 
1, if the first relax factor is =rstart, and the
        nonlinear iteration does not rely on past convergence
        (use for an extra sensitive nonlinear problem only).
  - * 
2, if we are to return immediately upon  (a) two
        successive nonconvergences, or  (b) after obtaining
        error estimate for the first time.
- * 
*ipar[11]* ( = nfxpnt , the dimension of fixpnt)
    The number of fixed points in the mesh other than *aleft*
    and *aright*. 
    The code requires that all side condition points
    other than *aleft* and *aright* (see description of
    *zeta*) must be included as fixed points in *fixpnt*.
**ltol** — A list of length *ntol=ipar[4]*. *ltol[j]=k* specifies
that the j-th tolerance in *tol* controls the error
in the k-th component of z(u). 
The list *ltol* must be ordered with
$1 ≤ ltol[1] < ltol[2] < ... < ltol[ntol] ≤ mstar$.
**tol** — An list of length *ntol=ipar[4]*. *tol[j]* is the
error tolerance on the ltol[j]-th component
of z(u). 
Thus, the code attempts to satisfy
for j=1,...,ntol on each subinterval
$abs(z(v)-z(u))[k] ≤ tol(j)*abs(z(u))[k]+tol(j)$
if v(x) is the approximate solution vector.
**fixpnt** — An list of length *ipar[11]*. It contains the points, other than
*aleft* and *aright*, which are to be included in every mesh.
All side condition points other than *aleft* and *aright*
(see *zeta*) be included as fixed points in *fixpnt*.
**ispace** — An integer work list of length *ipar[6]*.
**fspace** — A real work list of length *ipar[5]*.
**fsub** — *fsub* is a function f(x,z1,...,z[mstar]) which realizes
the system of ODEs. 
It returns a list of *ncomp* values, one for each ODE.
Each value is the highest order
derivative in each ode in terms of of x,z1,...,z[mstar] .
**dfsub** — *dfsub* is a function df(x,z1,...,z[mstar]) for evaluating
the Jacobian of f.
**gsub** — Name of subroutine gsub(i,z1,z2,...,z[mstar]) for evaluating the i-th
component of the boundary value function g(z1,...,z[mstar]).
The independent variable x is not an argument of g.  The value
*x=zeta[i]* must be substituted in advance.
**dgsub** — Name of subroutine dgsub(i,z1,...,z[mstar]) for evaluating the
i-th row of the Jacobian of g(z1,...,z[mstar]).
**guess** — Name of subroutine to evaluate the initial
approximation for  (u(x)) and for dmval(u(x))= vector
of the mj-th derivatives of u(x).
This subroutine is needed only if using *ipar(9)* = 1.


The return value of *colnew_expert* is the list
*[iflag, fspace, ispace]*, where:



**iflag** — The mode of return from *colnew_expert*.
   - *
    
= 1 for normal return
- *
    
= 0 if the collocation matrix is singular.
- *
    
= -1 if the expected no. of subintervals exceeds storage specifications.
- *
    
= -2 if the nonlinear iteration has not converged.
- *
    
= -3 if there is an input data error.
**fspace** — A list of floats of length *ipar[5]*.
**ispace** — A list of integers of length *ipar[6]*.


`colnew_appsln` uses *fspace* and *ispace* to calculate solution values
at arbitrary points.  The lists can also be used to restart the solution process
with modified meshes and parameters.

See also: `colnew_appsln`.

### Function: cspline (cspline, points, cspline, points, option1, option2, ...)

Computes the polynomial interpolation by the cubic splines method. Argument *points* must be either:



- *
a two column matrix, `p:matrix([2,4],[5,6],[9,3])`,
- *
a list of pairs, `p: [[2,4],[5,6],[9,3]]`,
- *
a list of numbers, `p: [4,6,3]`, in which case the abscissas will be assigned automatically to 1, 2, 3, etc.


In the first two cases the pairs are ordered with respect to the first coordinate before making computations.


There are three options to fit specific needs:


- *
`'d1`, default `'unknown`, is the first derivative at $x_1$; if it is `'unknown`, the second derivative at $x_1$ is made equal to 0 (natural cubic spline); if it is equal to a number, the second derivative is calculated based on this number.
- *
`'dn`, default `'unknown`, is the first derivative at $x_n$; if it is `'unknown`, the second derivative at $x_n$ is made equal to 0 (natural cubic spline); if it is equal to a number, the second derivative is calculated based on this number.
- *
`'varname`, default `'x`, is the name of the independent variable.


See also `lagrange`,  `linearinterpol`,  and `ratinterpol`.


Examples:















```maxima
maxima
(%i1) load("interpol")$
(%i2) p:[[7,2],[8,2],[1,5],[3,2],[6,7]]$

(%i3) cspline(p);
             3         2
       1159 x    1159 x    6091 x   8283
(%o3) (------- - ------- - ------ + ----) charfun(x < 3)
        3288      1096      3288    1096
 + charfun((6 <= x) and (x < 7))
        3          2
  4715 x    15209 x    579277 x   199575
 (------- - -------- + -------- - ------)
   1644       274        1644      274
 + charfun((3 <= x) and (x < 6))
          3         2
    3287 x    2223 x    48275 x   9609
 (- ------- + ------- - ------- + ----)
     4932       274      1644     274
                            3         2
                      2587 x    5174 x    494117 x   108928
 + charfun(7 <= x) (- ------- + ------- - -------- + ------)
                       1644       137       1644      137

(%i4) define (f(x),%)$

(%i5) float (map (f, [2.3,5/7,%pi]));
(%o5) [1.9914607664233568, 5.823200187269903, 2.2274053124295072]


(%i6) plot2d ([f,[discrete,p]], [x,0,10], [y,-8,13], [style,lines,points],
    [legend,"Cubic splines","Points"])$


(%i7) cspline(p,d1=0,dn=0);
             3          2
       1949 x    11437 x    17027 x   1247
(%o7) (------- - -------- + ------- + ----) charfun(x < 3)
        2256       2256      2256     752
 + charfun((6 <= x) and (x < 7))
       3          2
  607 x    35147 x    55706 x   38420
 (------ - -------- + ------- - -----)
   188       564        141      47
 + charfun((3 <= x) and (x < 6))
          3         2
    3895 x    1807 x    5146 x   2148
 (- ------- + ------- - ------ + ----)
     5076       188      141      47
                            3          2
                      1547 x    35581 x    68068 x   173546
 + charfun(7 <= x) (- ------- + -------- - ------- + ------)
                        564       564        141      141

(%i8) define (g(x),%)$

(%i9) plot2d ([f,g,[discrete,p]], [x,0,10], [y,-15,15], [style,lines,lines,points],
       [legend,"Cubic splines","Splines with derivatives","Points"])$
```


(Figure interpol3)


(Figure interpol4)

See also: `lagrange`, `linearinterpol`, `ratinterpol`.

### Function: dgeev (dgeev, A, dgeev, A, right_p, left_p)

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

### Function: dgemm (dgemm, A, B, dgemm, A, B, options)

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

### Function: dgesvd (dgesvd, A, dgesvd, A, left_p, right_p)

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

### Variable: epsilon_lp

Default value: `10^-8`


Epsilon used for numerical computations in `linear_program`; it is
set to 0 in `linear_program` when all inputs are rational.


Example:









```maxima
(%i1) load("simplex")$

(%i2) minimize_lp(-x, [1e-9*x + y <= 1], [x,y]);
Warning: linear_program(A,b,c): non-rat inputs found, epsilon_lp= 1.0e-8
Warning: Solution may be incorrect.
(%o2)                        Problem not bounded!
(%i3) minimize_lp(-x, [10^-9*x + y <= 1], [x,y]);
(%o3)               [- 1000000000, [y = 0, x = 1000000000]]
(%i4) minimize_lp(-x, [1e-9*x + y <= 1], [x,y]), epsilon_lp=0;
(%o4)     [- 9.999999999999999e+8, [y = 0, x = 9.999999999999999e+8]]
```


See also: `linear_program`, `ratnump`.

See also: `linear_program`, `ratnump`.

### Function: fft (x)

Computes the complex fast Fourier transform.
*x* is a list or array (named or unnamed) which contains the data to
transform.  The number of elements must be a power of 2.
The elements must be literal numbers (integers, rationals, floats, or bigfloats)
or symbolic constants,
or expressions `a + b*%i` where `a` and `b` are literal numbers
or symbolic constants.


`fft` returns a new object of the same type as *x*,
which is not modified.
Results are always computed as floats
or expressions `a + b*%i` where `a` and `b` are floats.
If bigfloat precision is needed the function `bf_fft` can be used
instead as a drop-in replacement of `fft` that is slower, but
supports bfloats. In addition if it is known that the input consists
of only real values (no imaginary parts), `real_fft` can be used
which is potentially faster.


The discrete Fourier transform is defined as follows.
Let $y$ be the output of the transform.
Then for $k$ from 0 through $n - 1$,



$$y[k] = {1\over n} \sum_{j=0}^{n-1} x[j] e^{+2i\pi j k / n}$$


$$y[k] = {1\over n} \sum_{j=0}^{n-1} x[j] e^{+2i\pi j k / n}$$



As there are various sign and normalization conventions possible,
this definition of the transform may differ from that used by other mathematical software.


When the data *x* are real,
real coefficients `a` and `b` can be computed such that



$$x[j] = \sum_{k=0}^{n/2} \left(a[k] \cos {2\pi j k\over n} + b[k] \sin {2\pi j k \over n}\right)$$


$$x[j] = \sum_{k=0}^{n/2} \left(a[k] \cos {2\pi j k\over n} + b[k]
\sin {2\pi j k \over n}\right)$$



with



$$\eqalign{ a[0] &= {\rm realpart}(y[0])\cr b[0] &= 0 }$$


$$\eqalign{
a[0] &= {\rm realpart}(y[0])\cr
b[0] &= 0
}$$



and, for $k$ from 1 through $n/2 - 1$,



$$\eqalign{ a[k] &= {\rm realpart}(y[k] + y[n-k]) \cr b[k] &= {\rm imagpart}(y[n-k] - y[k]) }$$


$$\eqalign{
a[k] &= {\rm realpart}(y[k] + y[n-k]) \cr
b[k] &= {\rm imagpart}(y[n-k] - y[k])
}$$



and



$$\eqalign{ a\left[{n\over 2}\right] &= {\rm realpart}\left(y\left[{n\over 2}\right]\right) \cr b\left[{n\over 2}\right] &= 0 }$$


$$\eqalign{
a\left[{n\over 2}\right] &= {\rm realpart}\left(y\left[{n\over 2}\right]\right) \cr
b\left[{n\over 2}\right] &= 0
}$$



`load("fft")` loads this function.


See also `inverse_fft` (inverse transform),
`recttopolar`, and `polartorect`.. See `real_fft`
for FFTs of a real-valued input, and `bf_fft` and
`bf_real_fft` for operations on bigfloat values.  Finally, for
transforms of any size (but limited to float values), see
`fftpack5_fft` and `fftpack5_real_fft`.


Examples:


Real data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $

(%i4) L1 : fft (L);
(%o4) [0.0, 1.811 %i - 0.1036, 0.0, 0.3107 %i + 0.6036, 0.0, 
                    0.6036 - 0.3107 %i, 0.0, - 1.811 %i - 0.1036]


(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 4.441e-16 %i + 2.0, 3.0, 4.0 - 4.441e-16 %i, - 1.0, 
                 - 4.441e-16 %i - 2.0, - 3.0, 4.441e-16 %i - 4.0]


(%i6) lmax (abs (L2 - L));
(%o6)                       4.441e-16
```


Complex data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $

(%i4) L1 : fft (L);
(%o4) [0.5, 0.5, 0.25 %i - 0.25, - 0.3536 %i - 0.3536, 0.0, 0.5, 
                            - 0.25 %i - 0.25, 0.3536 %i + 0.3536]


(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, - 1.0, - 1.0, 
                                 1.0 - 1.0 %i, 1.0 %i + 1.0, 1.0]


(%i6) lmax (abs (L2 - L));
(%o6)                          0.0
```


Computation of sine and cosine coefficients.

























```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, 5, 6, 7, 8] $
(%i4) n : length (L) $
(%i5) x : make_array (any, n) $
(%i6) fillarray (x, L) $
(%i7) y : fft (x) $
(%i8) a : make_array (any, n/2 + 1) $
(%i9) b : make_array (any, n/2 + 1) $
(%i10) a[0] : realpart (y[0]) $
(%i11) b[0] : 0 $

(%i12) for k : 1 thru n/2 - 1 do
   (a[k] : realpart (y[k] + y[n - k]),
    b[k] : imagpart (y[n - k] - y[k]));
(%o12)                        done

(%i13) a[n/2] : y[n/2] $
(%i14) b[n/2] : 0 $

(%i15) listarray (a);
(%o15)          [4.5, - 1.0, - 1.0, - 1.0, - 0.5]


(%i16) listarray (b);
(%o16)             [0, 2.414, 1.0, 0.4142, 0]

(%i17) f(j) := sum (a[k] * cos (2*%pi*j*k / n) + b[k] * sin (2*%pi*j*k / n), k, 0, n/2) $

(%i18) makelist (float (f (j)), j, 0, n - 1);
(%o18)      [1.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0]
```

See also: `bf_fft`, `real_fft`, `inverse_fft`, `recttopolar`, `polartorect`, `bf_real_fft`, `fftpack5_fft`, `fftpack5_real_fft`.

### Function: fftpack5_fft (x)

Like `fft` (`fft`), this computes the fast Fourier transform
of a complex sequence.  However, the length of *x* is not limited
to a power of 2.  


`load("fftpack5")` loads this function.


Examples:


Real data.



```maxima
(%i1) load("fftpack5") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2 ,-3, -4] $
(%i4) L1 : fftpack5_fft(L);
(%o4) [0.0, 1.811 %i - 0.1036, 0.0, 0.3107 %i + 0.6036, 0.0, 
                                0.6036 - 0.3107 %i, 0.0, (- 1.811 %i) - 0.1036]
(%i5) L2 : fftpack5_inverse_fft(L1);
(%o5) [1.0, 4.441e-16 %i + 2.0, 1.837e-16 %i + 3.0, 4.0 - 4.441e-16 %i, 
     - 1.0, (- 4.441e-16 %i) - 2.0, (- 1.837e-16 %i) - 3.0, 4.441e-16
       %i - 4.0]
(%i6) lmax (abs (L2-L));
(%o6)                       4.441e-16
(%i7) L : [1, 2, 3, 4, 5, 6]$
(%i8) L1 : fftpack5_fft(L);
(%o8) [3.5, (- 0.866 %i) - 0.5, (- 0.2887 %i) - 0.5, (- 1.48e-16 %i) - 0.5, 
                                               0.2887 %i - 0.5, 0.866
                                                      %%i - 0.5]
(%i9) L2 : fftpack5_inverse_fft (L1);
(%o9) [1.0 - 1.48e-16 %i, 3.701e-17 %i + 2.0, 3.0 - 1.48e-16 %i, 
                     4.0 - 1.811e-16 %i, 5.0 - 1.48e-16 %i, 5.881e-16
                           %i + 6.0]
(%i10) lmax (abs (L2-L));
(%o10)                             9.064e-16
```


Complex data.



```maxima
(%i1) load("fftpack5") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : fftpack5_inverse_fft (L);
(%o4) [4.0, 2.828 %i + 2.828, (- 2.0 %i) - 2.0, 4.0, 0.0, 
                                       (- 2.828 %i) - 2.828, 2.0 %i - 2.0, 4.0]
(%i5) L2 : fftpack5_fft(L1);
(%o5) [1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, (- 2.776e-17 %i) - 1.0, - 1.0, 
                                1.0 - 1.0 %i, 1.0 %i + 1.0, 1.0 -
                                          %2.776e-17 %i]
(%i6) lmax(abs(L2-L));
(%o6)                              1.11e-16
```

See also: `fft`.

### Function: fftpack5_inverse_fft (y)

Computes the inverse complex Fourier transform, like
`inverse_fft`, but is not constrained to be a power of two.

### Function: fftpack5_inverse_real_fft (y, n)

Computes the inverse Fourier transform of *y*, which must have a
length of `floor(n/2) + 1`.  The length of sequence produced by the
inverse transform must be specified by *n*.  This is required
because the length of *y* does not uniquely determine *n*.
The last element of *y* is always real if *n* is even, but it
can be complex when *n* is odd.

### Function: fftpack5_real_fft (x)

Computes the fast Fourier transform of a real-valued sequence *x*,
just like `real_fft`, except the length is not constrained to be
a power of two.


Examples:



```maxima
(%i1) fpprintprec : 4 $
(%i2) L : [1, 2, 3, 4, 5, 6] $
(%i3) L1 : fftpack5_real_fft(L);
(%o3)       [3.5, (- 0.866 %i) - 0.5, (- 0.2887 %i) - 0.5, - 0.5]
(%i4) L2 : fftpack5_inverse_real_fft(L1, 6);
(%o4)                  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
(%i5) lmax(abs(L2-L));
(%o5)                            1.332e-15
(%i6) fftpack5_inverse_real_fft(L1, 7);
(%o6)            [0.5, 2.083, 2.562, 3.7, 4.3, 5.438, 5.917]
```


The last example shows how important it to set the length correctly
for `fftpack5_inverse_real_fft`.

### Function: fmin_cobyla (fmin_cobyla, F, X, Y, fmin_cobyla, F, X, Y, optional_args)

Returns an approximate minimum of the expression *F* with respect
to the variables *X*, subject to an optional set of constraints.
*Y* is a list of initial guesses for *X*.


*F* must be ordinary expressions, not names of functions or lambda expressions.


`optional_args` represents additional arguments,
specified as `symbol = value`.
The optional arguments recognized are:



**constraints** — List of inequality and equality constraints that must be satisfied by
*X*.  The inequality constraints must be actual inequalities of
the form 
$g(X) \ge h(X)$
or 
$g(X) \le h(X).$
The equality constraints must be of the
form 
$g(X) = h(X).$
**rhobeg** — Initial value of the internal *RHO* variable which controls 
the size of simplex.  (Defaults to 1.0)
**rhoend** — The desired final value rho parameter.  It is approximately
 the accuracy in the variables. (Defaults to 1d-6.)
**iprint** — Verbose output level.  (Defaults to 0) 
- *
0 - No output
- *
1 - Summary at the end of the calculation
- *
2 - Each new value of RHO and SIGMA is printed, including 
 the vector of variables, some function information when RHO is reduced.
- *
3 - Like 2, but information is printed when F(X) is computed.
**maxfun** — The maximum number of function evaluations.  (Defaults to 1000).


On return, a vector is given:


1. The value of the variables giving the minimum.  This is a list of
elements of the form `var = value` for each of the
variables listed in *X*.
2. The minimized function value
3. The number of function evaluations.
4. Return code with the following meanings
 

  - 0 - No errors.
  - 1 - Limit on maximum number of function evaluations reached.
  - 2 - Rounding errors inhibiting progress.
  - -1 - *MAXCV* value exceeds *RHOEND*.  This indicates that the
  constraints were probably not satisfied.  User should investigate
  the value of the constraints.


*MAXCV* stands for “MAXimum Constraint Violation” and is the
value of $max(0.0, -c1(x), -c2(x),...-cm(x))$ where $ck(x)$
denotes the k’th constraint function.  (Note that maxima allows
constraints of the form $f(x) = g(x)$, which are internally
converted to $f(x)-g(x) >= 0$ and $g(x)-f(x) >= 0$ which is
required by COBYLA).


`load("fmin_cobyla")` loads this function.

### Function: guess_exact_value (x)

When *x* is a floating point number or bigfloat,
`guess_exact_value` tries to find an exact expression
(in terms of radicals, logarithms, exponentials, and the constant `%pi`)
which is nearly equal to the given number.
If `guess_exact_value` cannot find such an expression,
*x* is returned unchanged.


When *x* is rational number or other mapatom
(other than a float or bigfloat),
*x* is returned unchanged.


Otherwise, *x* is a nonatomic expression,
and `guess_exact_value` is applied to each of the arguments of *x*.


Example:












```maxima
(%i1) load ("pslq.mac");
(%o1)                       pslq.mac
(%i2) root: float (sin (%pi/12));
(%o2)                  0.2588190451025207
(%i3) guess_exact_value (root);
                        sqrt(2 - sqrt(3))
(%o3)                   -----------------
                                2
(%i4) L: makelist (root^i, i, 0, 4);
(%o4) [1.0, 0.2588190451025207, 0.06698729810778066, 
                       0.01733758853025369, 0.004487298107780675]
(%i5) m: pslq_integer_relation(%);
(%o5)                 [- 1, 0, 16, 0, - 16]
(%i6) makelist (x^i, i, 0, 4) . m;
                             4        2
(%o6)                 (- 16 x ) + 16 x  - 1
(%i7) solve(%);
             sqrt(sqrt(3) + 2)      sqrt(sqrt(3) + 2)
(%o7) [x = - -----------------, x = -----------------, 
                     2                      2
                        sqrt(2 - sqrt(3))      sqrt(2 - sqrt(3))
                  x = - -----------------, x = -----------------]
                                2                      2
```

### Function: hompack_polsys (eqnlist, varlist, iflg1, epsbig, epssml, numrr)

Finds the roots of the system of polynomials in the variables
*varlist* in the system of equations in *eqnlist*.  The number
of equations must match number of variables.  Each equation must be a
polynomial with variables in *varlist*.  The coefficients must be
real numbers.


The optional keyword arguments provide some control over the
algorithm.



**epsbig** — is the local error tolerance allowed by the
path tracker, defaulting to 1e-4.
**epssml** — is the accuracy
desired for the final solution, defaulting to 1d-14.
**numrr** — is the number of multiples of 1000 steps that will be tried
before abandoning a path, defaulting to 10.
**iflg1** — defaulting to 0, controls the algorithm as follows: 
**0** — If the problem is to be solved without calling `polsys`’ scaling
routine, `sclgnp`, and without using the projective
transformation.
**1** — If scaling but no projective transformation is to be used.
**10** — If no scaling but projective transformation is to be used.
**11** — If both scaling and projective transformation are to be used.


`hompack_polsys` returns a list.  The elements of the list are:


**retcode** — Indicates whether the solution is valid or not. 
**0** — Solution found without problems
**1** — Solution succeeded but `iflg2` indicates some issues with a
root. (That is, `iflg2` is not all ones.)
**-1** — `NN`, the declared dimension of the number of terms in the
polynomials,  is too small.  (This should not happen.)
**-2** — `MMAXT`, the declared dimension for the internal coefficient and
degree arrays, is too small.  (This should not happen.)
**-3** — `TTOTDG`, the total degree of the equations,  is too small.
(This should not happen.)
**-4** — `LENWK`, the length of the internal real work array, is too
small.  (This should not happen.)
**-5** — `LENIWK`, the length of the internal integer work array, is too
small.  (This should not happen.)
**-6** — *iflg1* is not 0 or 1, or 10 or 11.  (This should not happen; an
error should be thrown before `polsys` is called.)
**roots** — The roots of the system of equations.  This is in the same format as
`solve` would return.
**iflg2** — A list containing information on how the path for the m’th root terminated: 
**1** — Normal return
**2** — Specified error tolerance cannot be met.  Increase *epsbig* and
*epssml*  and rerun.
**3** — Maximum number of steps exceeded.  To track the path further, increase
*numrr* and rerun the path.  However, the path may be diverging, if the
lambda value is near 1 and the roots values are large.
**4** — Jacobian matrix does not have full rank.  The algorithm has failed
(the zero curve of the homotopy map cannot be followed any further).
**5** — The tracking algorithm has lost the zero curve of the homotopy map and
is not making progress.  The error tolerances *epsbig* and
*epssml* were too lenient.  The problem should be restarted with
smaller error tolerances.
**6** — The normal flow newton iteration in `stepnf` or `rootnf`
failed to converge.  The error tolerance *epsbig* may be too
stringent.
**7** — Illegal input parameters, a fatal error.
**lambda** — A list of the final lambda value for the m-th root, where lambda is the
continuation parameter.
**arclen** — A list of the arc length of the m-th root.
**nfe** — A list of the number of jacobian matrix evaluations required to track the m-th
root.


Here are some examples of using `hompack_polsys`.






```maxima
maxima
(%i1) load(hompack)$

(%i2) hompack_polsys([x1^2-1, x2^2-2],[x1,x2]);
(%o2) [0, [[x1 = 7.493410174972965e-17 %i - 1.0, 
x2 = - 2.1199276810167172e-16 %i - 1.4142135623730951], 
[x1 = 1.0 - 1.7812202259088373e-17 %i, 
x2 = - 9.892128000334418e-17 %i - 1.4142135623730951], 
[x1 = - 8.745710933584358e-17 %i - 1.0, 
x2 = 1.4142135623730951 - 3.1543521174128613e-17 %i], 
[x1 = 1.0 - 5.5487454344135625e-18 %i, 
x2 = 9.617653810456737e-17 %i + 1.4142135623730951]], 
[1, 1, 1, 1], [1.0, 1.0, 0.9999999999999999, 
0.9999999999999999], [4.6126237693413445, 4.6126230108601, 
4.612623872939582, 4.6126231144843475], [40, 40, 40, 40]]
```


The analytical solution can be obtained with solve:





```maxima
maxima

(%i1) solve([x1^2-1, x2^2-2],[x1,x2]);
(%o1) [[x1 = 1, x2 = - sqrt(2)], [x1 = 1, x2 = sqrt(2)], 
            [x1 = - 1, x2 = - sqrt(2)], [x1 = - 1, x2 = sqrt(2)]]
```

We see that `hompack_polsys` returned the correct answer except
that the roots are in a different order and there is a small imaginary
part.


Another example, with corresponding solution from solve:







```maxima
maxima
(%i1) load(hompack)$

(%i2) hompack_polsys([x1^2 + 2*x2^2 + x1*x2 - 5, 2*x1^2 + x2^2 + x2-4],[x1,x2]);
(%o2) [0, [[x1 = 1.2015573017007832 - 6.51849608628558e-16 %i, 
x2 = - 2.2667444298167825e-16 %i - 1.6672703634801431], 
[x1 = - 5.901956169878514e-17 %i - 1.4285291895653132, 
x2 = - 6.670215053038164e-17 %i - 0.9106199083334114], 
[x1 = 1.942890293094024e-16 %i + 0.5920619420732687, 
x2 = 1.383859154368197 - 1.942890293094024e-16 %i], 
[x1 = 0.08945540033671631 - 8.534583737796769e-16 %i, 
x2 = 2.415141536592239e-16 %i + 1.5576674810817213]], 
[1, 1, 1, 1], [1.0000000000000004, 1.0000000000000002, 1.0, 
0.9999999999999999], [6.205795654034981, 7.7222132593900525, 
7.228287079174324, 5.6114742835849105], [35, 41, 48, 40]]


(%i3) solve([x1^2+2*x2^2+x1*x2 - 5, 2*x1^2+x2^2+x2-4],[x1,x2]);
(%o3) [[x1 = 0.08945540336850383, x2 = 1.5576673866090713], 
[x1 = 0.5920619554695062, x2 = 1.3838592860838075], 
[x1 = 1.2015573525007488, x2 = - 1.66727025803531], 
[x1 = - 1.428529150636283, x2 = - 0.9106198942815954]]
```


Note that `hompack_polsys` can sometimes be very slow.  Perhaps
`solve` can be used.  Or perhaps `eliminate` can be used to
convert the system of polynomials into one polynomial for which
`allroots` can find all the roots.

### Function: inverse_fft (y)

Computes the inverse complex fast Fourier transform.
*y* is a list or array (named or unnamed) which contains the data to
transform.  The number of elements must be a power of 2.
The elements must be literal numbers (integers, rationals, floats, or bigfloats)
or symbolic constants,
or expressions $a + bi$ where $a$ and $b$ are literal numbers
or symbolic constants.


`inverse_fft` returns a new object of the same type as $y$,
which is not modified.
Results are always computed as floats
or expressions `a + b*%i` where `a` and `b` are floats.
If bigfloat precision is needed the function `bf_inverse_fft` can
be used instead as a drop-in replacement of `inverse_fft` that is
slower, but supports bfloats. 


The inverse discrete Fourier transform is defined as follows.
Let $x$ be the output of the inverse transform.
Then for $j$ from 0 through $n - 1$,



$$x[j] = \sum_{k=0}^{n-1} y[k] e^{-2i\pi j k/n}$$


$$x[j] = \sum_{k=0}^{n-1} y[k] e^{-2i\pi j k/n}$$



As there are various sign and normalization conventions possible,
this definition of the transform may differ from that used by other mathematical software.


`load("fft")` loads this function.


See also `fft` (forward transform), `recttopolar`, and
`polartorect`.


Examples:


Real data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $

(%i4) L1 : inverse_fft (L);
(%o4) [0.0, - 14.49 %i - 0.8284, 0.0, 4.828 - 2.485 %i, 0.0, 
                        2.485 %i + 4.828, 0.0, 14.49 %i - 0.8284]


(%i5) L2 : fft (L1);
(%o5) [1.0, 2.0 - 4.441e-16 %i, 3.0, 4.441e-16 %i + 4.0, - 1.0, 
                 4.441e-16 %i - 2.0, - 3.0, - 4.441e-16 %i - 4.0]


(%i6) lmax (abs (L2 - L));
(%o6)                       4.441e-16
```


Complex data.











```maxima
maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $

(%i4) L1 : inverse_fft (L);
(%o4) [4.0, 2.828 %i + 2.828, - 2.0 %i - 2.0, 4.0, 0.0, 
                           - 2.828 %i - 2.828, 2.0 %i - 2.0, 4.0]


(%i5) L2 : fft (L1);
(%o5) [1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, - 1.0, - 1.0, 
                                 1.0 - 1.0 %i, 1.0 %i + 1.0, 1.0]


(%i6) lmax (abs (L2 - L));
(%o6)                          0.0
```

See also: `bf_inverse_fft`, `fft`, `recttopolar`, `polartorect`.

### Function: inverse_real_fft (y)

Computes the inverse Fourier transform of *y*, which must have a
length of `N/2+1` where `N` is a power of two.  That is, the
input *x* is expected to be the output of `real_fft`.


No check is made to ensure that the input has the correct format.
(The first and last elements must be purely real.)

### Function: lagrange (lagrange, points, lagrange, points, option)

Computes the polynomial interpolation by the Lagrangian method. Argument *points* must be either:



- *
a two column matrix, `p:matrix([2,4],[5,6],[9,3])`,
- *
a list of pairs, `p: [[2,4],[5,6],[9,3]]`,
- *
a list of numbers, `p: [4,6,3]`, in which case the abscissas will be assigned automatically to 1, 2, 3, etc.


In the first two cases the pairs are ordered with respect to the first coordinate before making computations.


With the *option* argument it is possible to select the name for the independent variable, which is `'x` by default; to define another one, write something like `varname='z`. 


Note that when working with high degree polynomials, floating point evaluations are unstable.


See also `linearinterpol`,  `cspline`,  and `ratinterpol`.


Examples:













```maxima
maxima
(%i1) load("interpol")$
(%i2) p:[[7,2],[8,2],[1,5],[3,2],[6,7]]$

(%i3) lagrange(p);
      (x - 7) (x - 6) (x - 3) (x - 1)
(%o3) -------------------------------
                    35
   (x - 8) (x - 6) (x - 3) (x - 1)
 - -------------------------------
                 12
   7 (x - 8) (x - 7) (x - 3) (x - 1)
 + ---------------------------------
                  30
   (x - 8) (x - 7) (x - 6) (x - 1)
 - -------------------------------
                 60
   (x - 8) (x - 7) (x - 6) (x - 3)
 + -------------------------------
                 84

(%i4) define(f(x),%)$

(%i5) expand(map(f,[2.3,5/7,%pi]));
                                 4          3           2
                   919062  73 %pi    701 %pi    8957 %pi
(%o5) [- 1.567535, ------, ------- - -------- + ---------
                   84035     420       210         420
                                                  5288 %pi   186
                                                - -------- + ---]
                                                    105       5


(%i6) plot2d ([f,[discrete,p]], [x,0,10], [style,lines,points],
       [legend,"Polynomial","Points"])$


(%i7) lagrange(p, varname=w);
      (w - 7) (w - 6) (w - 3) (w - 1)
(%o7) -------------------------------
                    35
   (w - 8) (w - 6) (w - 3) (w - 1)
 - -------------------------------
                 12
   7 (w - 8) (w - 7) (w - 3) (w - 1)
 + ---------------------------------
                  30
   (w - 8) (w - 7) (w - 6) (w - 1)
 - -------------------------------
                 60
   (w - 8) (w - 7) (w - 6) (w - 3)
 + -------------------------------
                 84
```


(Figure interpol1)

See also: `linearinterpol`, `cspline`, `ratinterpol`.

### Function: lbfgs (lbfgs, FOM, X, X0, epsilon, iprint, lbfgs, FOM, grad, X, X0, epsilon, iprint)

Finds an approximate solution of the unconstrained minimization of the figure of merit *FOM*
over the list of variables *X*,
starting from initial estimates *X0*,
such that $norm(grad(FOM)) < epsilon*max(1, norm(X))$.


*grad*, if present, is the gradient of *FOM* with respect to the variables *X*.
*grad* may be a list or a function that returns a list, with one element for each element of *X*.
If not present, the gradient is computed automatically by symbolic differentiation.
If *FOM* is a function, the gradient *grad* must be supplied by the user.


The algorithm applied is a limited-memory quasi-Newton (BFGS) algorithm [1].
It is called a limited-memory method because a low-rank approximation of the
Hessian matrix inverse is stored instead of the entire Hessian inverse.
Each iteration of the algorithm is a line search, that is,
a search along a ray in the variables *X*,
with the search direction computed from the approximate Hessian inverse.
The FOM is always decreased by a successful line search.
Usually (but not always) the norm of the gradient of FOM also decreases.


*iprint* controls progress messages printed by `lbfgs`.



**iprint[1]** — `iprint[1]` controls the frequency of progress messages. 
**iprint[1] < 0** — No progress messages.
**iprint[1] = 0** — Messages at the first and last iterations.
**iprint[1] > 0** — Print a message every `iprint[1]` iterations.
**iprint[2]** — `iprint[2]` controls the verbosity of progress messages. 
**iprint[2] = 0** — Print out iteration count, number of evaluations of *FOM*, value of *FOM*,
norm of the gradient of *FOM*, and step length.
**iprint[2] = 1** — Same as `iprint[2] = 0`, plus *X0* and the gradient of *FOM* evaluated at *X0*.
**iprint[2] = 2** — Same as `iprint[2] = 1`, plus values of *X* at each iteration.
**iprint[2] = 3** — Same as `iprint[2] = 2`, plus the gradient of *FOM* at each iteration.


The columns printed by `lbfgs` are the following.



**I** — Number of iterations. It is incremented for each line search.
**NFN** — Number of evaluations of the figure of merit.
**FUNC** — Value of the figure of merit at the end of the most recent line search.
**GNORM** — Norm of the gradient of the figure of merit at the end of the most recent line search.
**STEPLENGTH** — An internal parameter of the search algorithm.


Additional information concerning details of the algorithm are found in the
comments of the original Fortran code [2].


See also `lbfgs_nfeval_max` and `lbfgs_005fncorrections`.


References:


[1] D. Liu and J. Nocedal. "On the limited memory BFGS method for large
scale optimization". *Mathematical Programming B* 45:503–528 (1989)


[2] [https://www.netlib.org/opt/lbfgs_um.shar]()


Examples:


The same FOM as computed by FGCOMPUTE in the program sdrive.f in the LBFGS package from Netlib.
Note that the variables in question are subscripted variables.
The FOM has an exact minimum equal to zero at $u[k] = 1$ for $k = 1, ..., 8$.












```maxima
(%i1) load ("lbfgs")$
(%i2) t1[j] := 1 - u[j];
(%o2)                     t1  := 1 - u
                            j         j
(%i3) t2[j] := 10*(u[j + 1] - u[j]^2);
                                          2
(%o3)                t2  := 10 (u      - u )
                       j         j + 1    j
(%i4) n : 8;
(%o4)                           8
(%i5) FOM : sum (t1[2*j - 1]^2 + t2[2*j - 1]^2, j, 1, n/2);
                 2 2           2              2 2           2
(%o5) 100 (u  - u )  + (1 - u )  + 100 (u  - u )  + (1 - u )
            8    7           7           6    5           5
                     2 2           2              2 2           2
        + 100 (u  - u )  + (1 - u )  + 100 (u  - u )  + (1 - u )
                4    3           3           2    1           1
(%i6) lbfgs (FOM, '[u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8]],
       [-1.2, 1, -1.2, 1, -1.2, 1, -1.2, 1], 1e-3, [1, 0]);
*************************************************
  N=    8   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  9.680000000000000D+01   GNORM=  4.657353755084533D+02
*************************************************
```


```maxima
I NFN   FUNC                    GNORM                   STEPLENGTH

 1   3   1.651479526340304D+01   4.324359291335977D+00   7.926153934390631D-04
 2   4   1.650209316638371D+01   3.575788161060007D+00   1.000000000000000D+00
 3   5   1.645461701312851D+01   6.230869903601577D+00   1.000000000000000D+00
 4   6   1.636867301275588D+01   1.177589920974980D+01   1.000000000000000D+00
 5   7   1.612153014409201D+01   2.292797147151288D+01   1.000000000000000D+00
 6   8   1.569118407390628D+01   3.687447158775571D+01   1.000000000000000D+00
 7   9   1.510361958398942D+01   4.501931728123679D+01   1.000000000000000D+00
 8  10   1.391077875774293D+01   4.526061463810630D+01   1.000000000000000D+00
 9  11   1.165625686278198D+01   2.748348965356907D+01   1.000000000000000D+00
10  12   9.859422687859144D+00   2.111494974231706D+01   1.000000000000000D+00
11  13   7.815442521732282D+00   6.110762325764183D+00   1.000000000000000D+00
12  15   7.346380905773044D+00   2.165281166715009D+01   1.285316401779678D-01
13  16   6.330460634066464D+00   1.401220851761508D+01   1.000000000000000D+00
14  17   5.238763939854303D+00   1.702473787619218D+01   1.000000000000000D+00
15  18   3.754016790406625D+00   7.981845727632704D+00   1.000000000000000D+00
16  20   3.001238402313225D+00   3.925482944745832D+00   2.333129631316462D-01
17  22   2.794390709722064D+00   8.243329982586480D+00   2.503577283802312D-01
18  23   2.563783562920545D+00   1.035413426522664D+01   1.000000000000000D+00
19  24   2.019429976373283D+00   1.065187312340952D+01   1.000000000000000D+00
20  25   1.428003167668592D+00   2.475962450735100D+00   1.000000000000000D+00
21  27   1.197874264859232D+00   8.441707983339661D+00   4.303451060697367D-01
22  28   9.023848942003913D-01   1.113189216665625D+01   1.000000000000000D+00
23  29   5.508226405855795D-01   2.380830599637816D+00   1.000000000000000D+00
24  31   3.902893258879521D-01   5.625595817143044D+00   4.834988416747262D-01
25  32   3.207542206881058D-01   1.149444645298493D+01   1.000000000000000D+00
26  33   1.874468266118200D-01   3.632482152347445D+00   1.000000000000000D+00
27  34   9.575763380282112D-02   4.816497449000391D+00   1.000000000000000D+00
28  35   4.085145106760390D-02   2.087009347116811D+00   1.000000000000000D+00
29  36   1.931106005512628D-02   3.886818624052740D+00   1.000000000000000D+00
30  37   6.894000636920714D-03   3.198505769992936D+00   1.000000000000000D+00
31  38   1.443296008850287D-03   1.590265460381961D+00   1.000000000000000D+00
32  39   1.571766574930155D-04   3.098257002223532D-01   1.000000000000000D+00
33  40   1.288011779655132D-05   1.207784334505595D-02   1.000000000000000D+00
34  41   1.806140190993455D-06   4.587890258846915D-02   1.000000000000000D+00
35  42   1.769004612050548D-07   1.790537363138099D-02   1.000000000000000D+00
36  43   3.312164244118216D-10   6.782068546986653D-04   1.000000000000000D+00
```


\halign{\hfil\tt#&\quad\hfil\tt#\quad&\tt#\hfil\quad&\tt#\hfil\quad&\tt#\hfil\cr
I& NFN&   FUNC&                    GNORM&                   STEPLENGTH\cr
&&&&\cr
 1& 3& 1.651479526340304D+01& 4.324359291335977D+00& 7.926153934390631D-04\cr
 2& 4& 1.650209316638371D+01& 3.575788161060007D+00& 1.000000000000000D+00\cr
 3& 5& 1.645461701312851D+01& 6.230869903601577D+00& 1.000000000000000D+00\cr
 4& 6& 1.636867301275588D+01& 1.177589920974980D+01& 1.000000000000000D+00\cr
 5& 7& 1.612153014409201D+01& 2.292797147151288D+01& 1.000000000000000D+00\cr
 6& 8& 1.569118407390628D+01& 3.687447158775571D+01& 1.000000000000000D+00\cr
 7& 9& 1.510361958398942D+01& 4.501931728123680D+01& 1.000000000000000D+00\cr
 8&10& 1.391077875774294D+01& 4.526061463810632D+01& 1.000000000000000D+00\cr
 9&11& 1.165625686278198D+01& 2.748348965356917D+01& 1.000000000000000D+00\cr
10&12& 9.859422687859137D+00& 2.111494974231644D+01& 1.000000000000000D+00\cr
11&13& 7.815442521732281D+00& 6.110762325766556D+00& 1.000000000000000D+00\cr
12&15& 7.346380905773160D+00& 2.165281166714631D+01& 1.285316401779533D-01\cr
13&16& 6.330460634066370D+00& 1.401220851762050D+01& 1.000000000000000D+00\cr
14&17& 5.238763939851439D+00& 1.702473787613255D+01& 1.000000000000000D+00\cr
15&18& 3.754016790406701D+00& 7.981845727704576D+00& 1.000000000000000D+00\cr
16&20& 3.001238402309352D+00& 3.925482944716691D+00& 2.333129631296807D-01\cr
17&22& 2.794390709718290D+00& 8.243329982546473D+00& 2.503577283782332D-01\cr
18&23& 2.563783562918759D+00& 1.035413426521790D+01& 1.000000000000000D+00\cr
19&24& 2.019429976377856D+00& 1.065187312346769D+01& 1.000000000000000D+00\cr
20&25& 1.428003167670903D+00& 2.475962450826961D+00& 1.000000000000000D+00\cr
21&27& 1.197874264861340D+00& 8.441707983493810D+00& 4.303451060808756D-01\cr
22&28& 9.023848941942773D-01& 1.113189216635162D+01& 1.000000000000000D+00\cr
23&29& 5.508226405863770D-01& 2.380830600326308D+00& 1.000000000000000D+00\cr
24&31& 3.902893258815567D-01& 5.625595816584421D+00& 4.834988416524465D-01\cr
25&32& 3.207542206990315D-01& 1.149444645416472D+01& 1.000000000000000D+00\cr
26&33& 1.874468266362791D-01& 3.632482152880997D+00& 1.000000000000000D+00\cr
27&34& 9.575763380706598D-02& 4.816497446154354D+00& 1.000000000000000D+00\cr
28&35& 4.085145107543406D-02& 2.087009350166495D+00& 1.000000000000000D+00\cr
29&36& 1.931106001379290D-02& 3.886818608498966D+00& 1.000000000000000D+00\cr
30&37& 6.894000721499670D-03& 3.198505796342214D+00& 1.000000000000000D+00\cr
31&38& 1.443296033051864D-03& 1.590265471025043D+00& 1.000000000000000D+00\cr
32&39& 1.571766603154336D-04& 3.098257063980634D-01& 1.000000000000000D+00\cr
33&40& 1.288011776581970D-05& 1.207784183577257D-02& 1.000000000000000D+00\cr
34&41& 1.806140173752971D-06& 4.587890233385193D-02& 1.000000000000000D+00\cr
35&42& 1.769004645459358D-07& 1.790537375052208D-02& 1.000000000000000D+00\cr
36&43& 3.312164100763217D-10& 6.782068426119681D-04& 1.000000000000000D+00\cr
}


```maxima
THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o6) [u  = 1.000005339816132, u  = 1.000009942840108, 
        1                       2
u  = 1.000005339816132, u  = 1.000009942840108, 
 3                       4
u  = 1.000005339816132, u  = 1.000009942840108, 
 5                       6
u  = 1.000005339816132, u  = 1.000009942840108]
 7                       8
```


A regression problem.
The FOM is the mean square difference between the predicted value $F(X[i])$
and the observed value $Y[i]$.
The function $F$ is a bounded monotone function (a so-called "sigmoidal" function).
In this example, `lbfgs` computes approximate values for the parameters of $F$
and `plot2d` displays a comparison of $F$ with the observed data.














```maxima
(%i1) load ("lbfgs")$
(%i2) FOM : '((1/length(X))*sum((F(X[i]) - Y[i])^2, i, 1,
                                                length(X)));
                               2
               sum((F(X ) - Y ) , i, 1, length(X))
                       i     i
(%o2)          -----------------------------------
                            length(X)
(%i3) X : [1, 2, 3, 4, 5];
(%o3)                    [1, 2, 3, 4, 5]
(%i4) Y : [0, 0.5, 1, 1.25, 1.5];
(%o4)                [0, 0.5, 1, 1.25, 1.5]
(%i5) F(x) := A/(1 + exp(-B*(x - C)));
                                   A
(%o5)            F(x) := ----------------------
                         1 + exp((- B) (x - C))
(%i6) ''FOM;
                A               2            A                2
(%o6) ((----------------- - 1.5)  + (----------------- - 1.25)
          - B (5 - C)                  - B (4 - C)
        %e            + 1            %e            + 1
            A             2            A               2
 + (----------------- - 1)  + (----------------- - 0.5)
      - B (3 - C)                - B (2 - C)
    %e            + 1          %e            + 1
             2
            A
 + --------------------)/5
      - B (1 - C)     2
   (%e            + 1)
(%i7) estimates : lbfgs (FOM, '[A, B, C], [1, 1, 1], 1e-4, [1, 0]);
*************************************************
  N=    3   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  1.348738534246918D-01   GNORM=  2.000215531936760D-01
*************************************************
```


```maxima
I  NFN  FUNC                    GNORM                   STEPLENGTH
1    3  1.177820636622582D-01   9.893138394953992D-02   8.554435968992371D-01  
2    6  2.302653892214013D-02   1.180098521565904D-01   2.100000000000000D+01  
3    8  1.496348495303004D-02   9.611201567691624D-02   5.257340567840710D-01  
4    9  7.900460841091138D-03   1.325041647391314D-02   1.000000000000000D+00  
5   10  7.314495451266914D-03   1.510670810312226D-02   1.000000000000000D+00  
6   11  6.750147275936668D-03   1.914964958023037D-02   1.000000000000000D+00  
7   12  5.850716021108202D-03   1.028089194579382D-02   1.000000000000000D+00  
8   13  5.778664230657800D-03   3.676866074532179D-04   1.000000000000000D+00  
9   14  5.777818823650780D-03   3.010740179797108D-04   1.000000000000000D+00
```


\halign{\hfil\tt#&\quad\hfil\tt#\quad&\tt#\hfil\quad&\tt#\hfil\quad&\tt#\hfil\cr
I& NFN&   FUNC&                    GNORM&                   STEPLENGTH\cr
&&&&\cr
1&  3&1.177820636622582D-01& 9.893138394953992D-02& 8.554435968992371D-01\cr
2&  6&2.302653892214013D-02& 1.180098521565904D-01& 2.100000000000000D+01\cr
3&  8&1.496348495303004D-02& 9.611201567691624D-02& 5.257340567840710D-01\cr
4&  9&7.900460841091138D-03& 1.325041647391314D-02& 1.000000000000000D+00\cr
5& 10&7.314495451266914D-03& 1.510670810312226D-02& 1.000000000000000D+00\cr
6& 11&6.750147275936668D-03& 1.914964958023037D-02& 1.000000000000000D+00\cr
7& 12&5.850716021108202D-03& 1.028089194579382D-02& 1.000000000000000D+00\cr
8& 13&5.778664230657800D-03& 3.676866074532179D-04& 1.000000000000000D+00\cr
9& 14&5.777818823650780D-03& 3.010740179797108D-04& 1.000000000000000D+00\cr
}


```maxima
THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o7) [A = 1.461933911464101, B = 1.601593973254801, 
                                           C = 2.528933072164855]
(%i8) plot2d ([F(x), [discrete, X, Y]], [x, -1, 6]), ''estimates;
(%o8)
```


Gradient of FOM is specified (instead of computing it automatically).
Both the FOM and its gradient are passed as functions to `lbfgs`.











```maxima
(%i1) load ("lbfgs")$
(%i2) F(a, b, c) := (a - 5)^2 + (b - 3)^4 + (c - 2)^6$
(%i3) define(F_grad(a, b, c),
             map (lambda ([x], diff (F(a, b, c), x)), [a, b, c]))$
(%i4) estimates : lbfgs ([F, F_grad],
                   [a, b, c], [0, 0, 0], 1e-4, [1, 0]);
*************************************************
  N=    3   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  1.700000000000000D+02   GNORM=  2.205175729958953D+02
*************************************************
```


```maxima
I  NFN     FUNC                    GNORM                   STEPLENGTH

   1    2     6.632967565917637D+01   6.498411132518770D+01   4.534785987412505D-03  
   2    3     4.368890936228036D+01   3.784147651974131D+01   1.000000000000000D+00  
   3    4     2.685298972775191D+01   1.640262125898520D+01   1.000000000000000D+00  
   4    5     1.909064767659852D+01   9.733664001790506D+00   1.000000000000000D+00  
   5    6     1.006493272061515D+01   6.344808151880209D+00   1.000000000000000D+00  
   6    7     1.215263596054292D+00   2.204727876126877D+00   1.000000000000000D+00  
   7    8     1.080252896385329D-02   1.431637116951845D-01   1.000000000000000D+00  
   8    9     8.407195124830860D-03   1.126344579730008D-01   1.000000000000000D+00  
   9   10     5.022091686198525D-03   7.750731829225275D-02   1.000000000000000D+00  
  10   11     2.277152808939775D-03   5.032810859286796D-02   1.000000000000000D+00  
  11   12     6.489384688303218D-04   1.932007150271009D-02   1.000000000000000D+00  
  12   13     2.075791943844547D-04   6.964319310814365D-03   1.000000000000000D+00  
  13   14     7.349472666162258D-05   4.017449067849554D-03   1.000000000000000D+00  
  14   15     2.293617477985238D-05   1.334590390856715D-03   1.000000000000000D+00  
  15   16     7.683645404048675D-06   6.011057038099202D-04   1.000000000000000D+00
```


\halign{\hfil\tt#&\quad\hfil\tt#\quad&\tt#\hfil\quad&\tt#\hfil\quad&\tt#\hfil\cr
I& NFN&   FUNC&                    GNORM&                   STEPLENGTH\cr
&&&&\cr
   1&   2&    6.632967565917637D+01&  6.498411132518770D+01&  4.534785987412505D-03\cr
   2&   3&    4.368890936228036D+01&  3.784147651974131D+01&  1.000000000000000D+00\cr
   3&   4&    2.685298972775191D+01&  1.640262125898520D+01&  1.000000000000000D+00\cr
   4&   5&    1.909064767659852D+01&  9.733664001790506D+00&  1.000000000000000D+00\cr
   5&   6&    1.006493272061515D+01&  6.344808151880209D+00&  1.000000000000000D+00\cr
   6&   7&    1.215263596054292D+00&  2.204727876126877D+00&  1.000000000000000D+00\cr
   7&   8&    1.080252896385329D-02&  1.431637116951845D-01&  1.000000000000000D+00\cr
   8&   9&    8.407195124830860D-03&  1.126344579730008D-01&  1.000000000000000D+00\cr
   9&  10&    5.022091686198525D-03&  7.750731829225275D-02&  1.000000000000000D+00\cr
  10&  11&    2.277152808939775D-03&  5.032810859286796D-02&  1.000000000000000D+00\cr
  11&  12&    6.489384688303218D-04&  1.932007150271009D-02&  1.000000000000000D+00\cr
  12&  13&    2.075791943844547D-04&  6.964319310814365D-03&  1.000000000000000D+00\cr
  13&  14&    7.349472666162258D-05&  4.017449067849554D-03&  1.000000000000000D+00\cr
  14&  15&    2.293617477985238D-05&  1.334590390856715D-03&  1.000000000000000D+00\cr
  15&  16&    7.683645404048675D-06&  6.011057038099202D-04&  1.000000000000000D+00\cr
}


```maxima
THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o4) [a = 5.000086823042934, b = 3.052395429705181, 
                                           c = 1.927980629919583]
```

See also: `lbfgs_nfeval_max`, `lbfgs_ncorrections`.

### Variable: lbfgs_ncorrections

Default value: 25


`lbfgs_ncorrections` is the number of corrections applied
to the approximate inverse Hessian matrix which is maintained by `lbfgs`.

### Variable: lbfgs_nfeval_max

Default value: 100


`lbfgs_nfeval_max` is the maximum number of evaluations of the figure of merit (FOM) in `lbfgs`.
When `lbfgs_nfeval_max` is reached,
`lbfgs` returns the result of the last successful line search.

### Function: levin_options ()

Function `bflevin_u_sum` attempts to return the sum of an infinite series
with a precision given by the global variable `fpprec` using bigfloat arithmetic.
`bflevin_u_sum` uses an adaptive algorithm to increase both the number of
terms used and the bigfloat precision used for internal calculations
until the estimated error is acceptable.


The undeclared array `levin_options` contains options for controlling `bflevin_u_sum`.
Note that the subscript values for `levin_options` are strings.



**levin_options["debug"]** — When `true`, `bflevin_u_sum` generates additional output. Default: `false`
**levin_options["min_terms"]** — Minimum number of terms used by `bflevin_u_sum`. Default: 5
**levin_options["max_terms"]** — Maximum number of terms used by `bflevin_u_sum`. Default: 640 (equal to 5*2^7)
**levin_options["min_precision"]** — Initial bigfloat precision for `bflevin_u_sum`. Default: 16
**levin_options["max_precision"]** — Maximum bigfloat precision for `bflevin_u_sum`. Default: 1000

See also: `bflevin_u_sum`, `fpprec`.

### Function: levin_u_sum (levin_u_sum, a, n, n_0, nterms, mode, levin_u_sum, a, n, n_0, nterms)

Estimate `sum(a(n), n, n_0, inf)` using at most *nterms*
terms using the Levin u-transform `levin_002d1973`.


The following values are recognized for the optional argument *mode*.
If *mode* is not supplied, it is assumed to be `levin_algebraic`.



**levin_algebraic** — The calculation is performed in exact arithmetic. `levin_u_sum` returns the result.
**levin_numeric** — The calculation is performed in bigfloat arithmetic.
The return value is a list `[result, variance]`
where *result* is the result of the bigfloat calculation,
and *variance* is in units of `10^(-2*fpprec)`.


`load("levin")` loads this function.


See `Examples for levin` for examples.

See also: `levin-1973`, `Examples-for-levin`.

### Function: linear_program (A, b, c)

`linear_program` is an implementation of the simplex algorithm.
`linear_program(A, b, c)` computes a vector *x* for which
`c.x` is minimum possible among vectors for which `A.x = b`
and `x >= 0`. Argument *A* is a matrix and arguments *b*
and *c* are lists.


`linear_program` returns a list which contains the minimizing
vector *x* and the minimum value `c.x`. If the problem is not
bounded, it returns "Problem not bounded!" and if the problem is not
feasible, it returns "Problem not feasible!".


To use this function first load the `simplex` package with
`load("simplex");`.


Example:









```maxima
(%i2) A: matrix([1,1,-1,0], [2,-3,0,-1], [4,-5,0,0])$
(%i3) b: [1,1,6]$
(%i4) c: [1,-2,0,0]$
(%i5) linear_program(A, b, c);
                   13     19        3
(%o5)            [[--, 4, --, 0], - -]
                   2      2         2
```


See also: `minimize_lp`, `scale_lp`, and `epsilon_lp`.

See also: `minimize_lp`, `scale_lp`, `epsilon_lp`.

### Function: linearinterpol (linearinterpol, points, linearinterpol, points, option)

Computes the polynomial interpolation by the linear method. Argument *points* must be either:



- *
a two column matrix, `p:matrix([2,4],[5,6],[9,3])`,
- *
a list of pairs, `p: [[2,4],[5,6],[9,3]]`,
- *
a list of numbers, `p: [4,6,3]`, in which case the abscissas will be assigned automatically to 1, 2, 3, etc.


In the first two cases the pairs are ordered with respect to the first coordinate before making computations.


With the *option* argument it is possible to select the name for the independent variable, which is `'x` by default; to define another one, write something like `varname='z`. 


See also `lagrange`,  `cspline`,  and `ratinterpol`.


Examples:














```maxima
maxima
(%i1) load ("interpol") $
(%i2) p: matrix([7,2],[8,3],[1,5],[3,2],[6,7])$

(%i3) linearinterpol(p);
       13   3 x
(%o3) (-- - ---) charfun(x < 3) + charfun((3 <= x) and (x < 6))
       2     2
  5 x
 (--- - 3) + charfun(7 <= x) (x - 5)
   3
 + charfun((6 <= x) and (x < 7)) (37 - 5 x)

(%i4) define(f(x),%)$

(%i5) map(f, [7.3,25/7,%pi]);
                            62  5 %pi
(%o5)                 [2.3, --, ----- - 3]
                            21    3


(%i6) float(%);
(%o6)     [2.3, 2.9523809523809526, 2.235987755982989]


(%i7) plot2d ([f,[discrete,args(p)]], [x,-5,20], [style,lines,points],
    [legend,"Interpolation line","Points"])$


(%i8) lagrange(p, varname=w);
      3 (w - 7) (w - 6) (w - 3) (w - 1)
(%o8) ---------------------------------
                     70
   (w - 8) (w - 6) (w - 3) (w - 1)
 - -------------------------------
                 12
   7 (w - 8) (w - 7) (w - 3) (w - 1)
 + ---------------------------------
                  30
   (w - 8) (w - 7) (w - 6) (w - 1)
 - -------------------------------
                 60
   (w - 8) (w - 7) (w - 6) (w - 3)
 + -------------------------------
                 84
```


(Figure interpol2)

See also: `lagrange`, `cspline`, `ratinterpol`.

### Function: maximize_lp (obj, cond, pos)

Maximizes linear objective function *obj* subject to some linear
constraints *cond*. See `minimize_lp` for detailed
description of arguments and return value.



See also: `minimize_lp`.

See also: `minimize_lp`.

### Function: minimize_lp (obj, cond, pos)

Minimizes a linear objective function *obj* subject to some linear
constraints *cond*. *cond* a list of linear equations or
inequalities. In strict inequalities `>` is replaced by `>=`
and `<` by `<=`. The optional argument *pos* is a list
of decision variables which are assumed to be positive.


If the minimum exists, `minimize_lp` returns a list which
contains the minimum value of the objective function and a list of
decision variable values for which the minimum is attained. If the
problem is not bounded, `minimize_lp` returns "Problem not
bounded!" and if the problem is not feasible, it returns "Problem not
feasible!".


The decision variables are not assumed to be non-negative by default. If
all decision variables are non-negative, set `nonnegative_lp` to
`true` or include `all` in the optional argument *pos*. If
only some of decision variables are positive, list them in the optional
argument *pos* (note that this is more efficient than adding
constraints).


`minimize_lp` uses the simplex algorithm which is implemented in
maxima `linear_program` function.


To use this function first load the `simplex` package with
`load("simplex");`.


Examples:










```maxima
(%i1) minimize_lp(x+y, [3*x+y=0, x+2*y>2]);
                      4       6        2
(%o1)                [-, [y = -, x = - -]]
                      5       5        5
(%i2) minimize_lp(x+y, [3*x+y>0, x+2*y>2]), nonnegative_lp=true;
(%o2)                [1, [y = 1, x = 0]]
(%i3) minimize_lp(x+y, [3*x+y>0, x+2*y>2], all);
(%o3)                         [1, [y = 1, x = 0]]
(%i4) minimize_lp(x+y, [3*x+y=0, x+2*y>2]), nonnegative_lp=true;
(%o4)                Problem not feasible!
(%i5) minimize_lp(x+y, [3*x+y>0]);
(%o5)                Problem not bounded!
```


There is also a limited ability to solve linear programs with symbolic
constants.



```maxima
(%i1) declare(c,constant)$
(%i2) maximize_lp(x+y, [y<=-x/c+3, y<=-x+4], [x, y]), epsilon_lp=0;
Is (c-1)*c positive, negative or zero?
p;
Is c*(2*c-1) positive, negative or zero?
p;
Is c positive or negative?
p;
Is c-1 positive, negative or zero?
p;
Is 2*c-1 positive, negative or zero?
p;
Is 3*c-4 positive, negative or zero?
p;
                                 1                1
(%o2)                 [4, [x = -----, y = 3 - ---------]]
                                   1               1
                               1 - -          (1 - -) c
                                   c               c
```







```maxima
(%i1) (assume(c>4/3), declare(c,constant))$
(%i2) maximize_lp(x+y, [y<=-x/c+3, y<=-x+4], [x, y]), epsilon_lp=0;
                                 1                1
(%o2)                 [4, [x = -----, y = 3 - ---------]]
                                   1               1
                               1 - -          (1 - -) c
                                   c               c
```


See also: `maximize_lp`, `nonnegative_lp`, `epsilon_lp`.

See also: `maximize_lp`, `nonnegative_lp`, `epsilon_lp`.

### Function: minpack_lsquares (flist, varlist, guess, 'tolerance, =, tolerance, 'jacobian, =, jacobian)

Compute the point that minimizes the sum of the squares of the
functions in the list *flist*.  The variables are in the list
*varlist*.  An initial guess of the optimum point must be provided
in *guess*.


Let *flist* be a list of $m$ functions,
$f_i(x_1, x_2, ..., x_n).$
Then this function can be used to find the values of
$x_1, x_2, ..., x_n$
that solve the least squares problem



$$\sum_i^m f_i(x_1, x_2,...,x_n)^2$$


$$\sum_i^m f_i(x_1, x_2,...,x_n)^2$$




The optional keyword arguments, *tolerance* and *jacobian*
provide some control over the algorithm.



**tolerance** — the estimated relative error desired in the sum of squares.  The
default value is approximately
$1.0537\times 10^{-8}.$
**jacobian** — specifies the Jacobian.  If *jacobian*
is not given or is `true` (the default), the Jacobian is computed
from *flist*.  If *jacobian* is `false`, a numerical
approximation is used.  `jacobian`.


`minpack_lsquares` returns a list of three items as follows:


1. The estimated solution
2. The sum of squares
3. The success of the algorithm. The possible values are


  1. improper input parameters.
  2. algorithm estimates that the relative error in the sum of squares is
at most `tolerance`.
  3. algorithm estimates that the relative error between x and the solution
is at most `tolerance`.
  4. conditions for info = 1 and info = 2 both hold.
  5. fvec is orthogonal to the columns of the jacobian to machine
precision.
  6. number of calls to fcn with iflag = 1 has reached 100*(n+1).
  7. tol is too small. no further reduction in the sum of squares is
possible.
  8. tol is too small. no further improvement in the approximate solution x
is possible.


Here is an example using Powell’s singular function.











```maxima
maxima
(%i1) load("minpack")$
(%i2) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], [3,-1,0,1]);
(%o3) [[1.6521175961683935e-17, - 1.6521175961683934e-18, 
2.6433881538694683e-18, 2.6433881538694683e-18], 
6.109327859207777e-34, 4]
```


Same problem but use numerical approximation to Jacobian.







```maxima
maxima
(%i1) load("minpack")$
(%i2) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], [3,-1,0,1], jacobian = false);
(%o3) [[5.060282149485331e-11, - 5.060282149491206e-12, 
2.1794478435472183e-11, 2.1794478435472183e-11], 
3.534491794847031e-21, 5]
```

See also: `jacobian`.

### Function: minpack_solve (flist, varlist, guess, 'tolerance, =, tolerance, 'jacobian, =, jacobian)

Solve a system of `n` equations in `n` unknowns.
The `n` equations are given in the list *flist*, and the
unknowns are in *varlist*.  An initial guess of the solution must
be provided in *guess*.


Let *flist* be a list of $m$ functions,
$f_i(x_1, x_2, ..., x_n).$
Then this functions solves the system of $m$ nonlinear equations
in $n$ variables:



$$f_i(x_1, x_2, ..., x_n) = 0$$


$$f_i(x_1, x_2, ..., x_n) = 0$$



The optional keyword arguments, *tolerance* and *jacobian*
provide some control over the algorithm.



**tolerance** — the estimated relative error desired in the sum of squares.  The
default value is approximately
$1.0537\times 10^{-8}.$
**jacobian** — specifies the Jacobian.  If *jacobian*
is not given or is `true` (the default), the Jacobian is computed
from *flist*.  If *jacobian* is `false`, a numerical
approximation is used.  `jacobian`.


`minpack_solve` returns a list of three items as follows:


1. The estimated solution
2. The sum of squares
3. The success of the algorithm.  The possible values are


  1. improper input parameters.
  2. algorithm estimates that the relative error in the solution is
at most `tolerance`.
  3. number of calls to fcn with iflag = 1 has reached 100*(n+1).
  4. tol is too small. no further reduction in the sum of squares is
possible.
  5. Iteration is not making good progress.








```maxima
maxima
(%i1) load("minpack")$
(%i2) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i3) minpack_lsquares(powell(x1,x2,x3,x4), [x1,x2,x3,x4], [3,-1,0,1]);
(%o3) [[1.6521175961683935e-17, - 1.6521175961683934e-18, 
2.6433881538694683e-18, 2.6433881538694683e-18], 
6.109327859207777e-34, 4]
```

In this particular case, we can solve this analytically:






```maxima
maxima
(%i1) powell(x1,x2,x3,x4) := [x1+10*x2, sqrt(5)*(x3-x4), (x2-2*x3)^2, sqrt(10)*(x1-x4)^2]$

(%i2) solve(powell(x1,x2,x3,x4),[x1,x2,x3,x4]);
(%o2)          [[x1 = 0, x2 = 0, x3 = 0, x4 = 0]]
```

and we see that the numerical solution is quite close the analytical one.

See also: `jacobian`.

### Function: mnewton (mnewton, FuncList, VarList, GuessList, mnewton, FuncList, VarList, GuessList, DF)

Approximate solution of multiple nonlinear equations by Newton’s method.


*FuncList* is a list of functions to solve,
*VarList* is a list of variable names, and
*GuessList* is a list of initial approximations.
The optional argument *DF* is the Jacobian matrix of the list of functions;
if not supplied, it is calculated automatically from *FuncList*.


*FuncList* may be specified as a list of equations,
in which case the function to be solved is the left-hand side of each equation minus the right-hand side.


If there is only a single function, variable, and initial point,
they may be specified as a single expression, variable, and initial value;
they need not be lists of one element.


A variable may be a simple symbol or a subscripted symbol.


The solution, if any, is returned as a list of one element,
which is a list of equations, one for each variable,
specifying an approximate solution;
this is the same format as returned by `solve`.
If the solution is not found, `[]` is returned.


Functions and initial points may contain complex numbers,
and solutions likewise may contain complex numbers.


`mnewton` is governed by global variables `newtonepsilon` and
`newtonmaxiter`, and the global flag `newtondebug`.


`load("mnewton")` loads this function.


See also `realroots`, `allroots`, `find_root` and
`newton`.


Examples:



```maxima
(%i1) load("mnewton")$

(%i2) mnewton([x1+3*log(x1)-x2^2, 2*x1^2-x1*x2-5*x1+1],
              [x1, x2], [5, 5]);
(%o2) [[x1 = 3.756834008012769, x2 = 2.779849592817897]]
(%i3) mnewton([2*a^a-5],[a],[1]);
(%o3)             [[a = 1.70927556786144]]
(%i4) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o4) [[u = 1.066618389595407, v = 1.552564766841786]]
```


The variable `newtonepsilon` controls the precision of the
approximations.  It also controls if computations are performed with
floats or bigfloats.



```maxima
(%i1) load("mnewton")$

(%i2) (fpprec : 25, newtonepsilon : bfloat(10^(-fpprec+5)))$

(%i3) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o3) [[u = 1.066618389595406772591173b0, 
                               v = 1.552564766841786450100418b0]]
```

See also: `newtonepsilon`, `newtonmaxiter`, `newtondebug`, `realroots`, `allroots`, `find_root`, `newton`.

### Variable: newtondebug

Default value: `false`


When `newtondebug` is `true`, 
`mnewton` prints out debugging information while solving a problem.

### Variable: newtonepsilon

Default value: `10.0^(-fpprec/2)`


Precision to determine when the `mnewton` function has converged towards
the solution.


When `newtonepsilon` is a bigfloat,
`mnewton` computations are done with bigfloats;
otherwise, ordinary floats are used.


See also `mnewton`.

See also: `mnewton`.

### Variable: newtonmaxiter

Default value: `50`


Maximum number of iterations to stop the `mnewton` function
if it does not converge or if it converges too slowly.


See also `mnewton`.

See also: `mnewton`.

### Variable: nonnegative_lp

Default value: `false`


If `nonnegative_lp` is true all decision variables to
`minimize_lp` and `maximize_lp` are assumed to be non-negative.
`nonegative_lp` is a deprecated alias.

                   

See also: `minimize_lp`.

See also: `minimize_lp`.

### Variable: pivot_count_sx

After `linear_program` returns,
`pivot_count_sx` is the number of pivots in last computation.

### Variable: pivot_max_sx

`pivot_max_sx` is the maximum number of pivots allowed by `linear_program`.

### Function: polartorect (r, t)

Translates complex values of the form $r e^{i t}$ to the form
$a + b i$, where $r$ is the magnitude and $t$ is the phase.
$r$ and $t$ are 1-dimensional arrays of the same size.
The array size need not be a power of 2.


The original values of the input arrays are
replaced by the real and imaginary parts, $a$ and $b$, on return.
The outputs are calculated as



$$\eqalign{ a &= r \cos t \cr b &= r \sin t }$$


$$\eqalign{
a &= r \cos t \cr
b &= r \sin t
}$$



`polartorect` is the inverse function of `recttopolar`.


`load("fft")` loads this function.  See also `fft`.

See also: `polartorect`, `recttopolar`, `fft`.

### Variable: pslq_depth

Default value: `20 * n`


Number of iterations of the PSLQ algorithm.


The default value is 20 times *n*,
where *n* is the length of the list of numbers supplied to `pslq_integer_relation`.

### Function: pslq_integer_relation (L)

Implements the PSLQ algorithm [1] to find integer relations between bigfloat numbers.


For a given list *L* of floating point numbers,
`pslq_integer_relation` returns a list of integers *m*
such that `m . L = 0`
(with absolute residual error less than `pslq_threshold`).


[1] D.H.Bailey: Integer Relation Detection and Lattice Reduction.


Example:












```maxima
(%i1) load ("pslq.mac");
(%o1)                       pslq.mac
(%i2) root: float (sin (%pi/12));
(%o2)                  0.2588190451025207
(%i3) L: makelist (root^i, i, 0, 4);
(%o3) [1.0, 0.2588190451025207, 0.06698729810778066, 
                       0.01733758853025369, 0.004487298107780675]
(%i4) m: pslq_integer_relation(%);
(%o4)                 [- 1, 0, 16, 0, - 16]
(%i5) m . L;
(%o5)                - 2.359223927328458E-16
(%i6) float (10^(2 - fpprec));
(%o6)                        1.0E-14
(%i7) is (abs (m . L) < 10^(2 - fpprec));
(%o7)                         true
```

### Variable: pslq_precision

Default value: `10^(fpprec - 2)`


Maximum magnitude of some intermediate results in `pslq_integer_relation`.
The search fails if one of the intermediate results has elements
larger than `pslq_precision`.

### Variable: pslq_status

Indicates success or failure for an integer relation search by `pslq_integer_relation`.


When `pslq_status` is 1, it indicates an integer relation was found,
and the absolute residual error is less than `pslq_threshold`.


When `pslq_status` is 2, it indicates an integer relation was not found
because some intermediate results are larger than `pslq_precision`.


When `pslq_status` is 3, it indicates an integer relation was not found
because the number of iterations `pslq_depth` was reached.

### Variable: pslq_threshold

Default value: `10^(2 - fpprec)`


Threshold for absolute residual error of integer relation found by `pslq_integer_relation`.

### Function: ratinterpol (ratinterpol, points, numdeg, ratinterpol, points, numdeg, option1)

Generates a rational interpolator for data given by *points* and the degree of the numerator
being equal to *numdeg*; the degree of the denominator is calculated
automatically. Argument *points* must be either:



- *
a two column matrix, `p:matrix([2,4],[5,6],[9,3])`,
- *
a list of pairs, `p: [[2,4],[5,6],[9,3]]`,
- *
a list of numbers, `p: [4,6,3]`, in which case the abscissas will be assigned automatically to 1, 2, 3, etc.


In the first two cases the pairs are ordered with respect to the first coordinate before making computations.


There is one option to fit specific needs:


- *
`'varname`, default `'x`, is the name of the independent variable.


See also `lagrange`,  `linearinterpol`,  `cspline`,  `minpack_lsquares`,  and `Package-lbfgs`


Examples:










```maxima
maxima
(%i1) load("interpol")$
(%i2) p:[[7.2,2.5],[8.5,2.1],[1.6,5.1],[3.4,2.4],[6.7,7.9]]$

(%i3) for k:0 thru length(p)-1 do


(%i4) plot2d([ratinterpol(p,k),[discrete,p]], [x,0,9], [y,0,10], [style,lines,points],
  [title,concat("Degree of numerator = ",k)], nolegend, gnuplot)$
```


(Figure interpol5)


(Figure interpol6)


(Figure interpol7)


(Figure interpol8)


(Figure interpol9)

See also: `lagrange`, `linearinterpol`, `cspline`, `minpack_lsquares`, `Package-lbfgs`.

### Function: real_fft (x)

Computes the fast Fourier transform of a real-valued sequence
*x*.  This is equivalent to performing `fft(x)`, except that
only the first `N/2+1` results are returned, where `N` is
the length of *x*.  `N` must be power of two.


No check is made that *x* contains only real values.


The symmetry properties of the Fourier transform of real sequences to
reduce he complexity.  In particular the first and last output values
of `real_fft` are purely real.  For larger sequences, `real_fft`
may be computed more quickly than `fft`.


Since the output length is short, the normal `inverse_fft` cannot
be directly used.  Use `inverse_real_fft` to compute the inverse.

See also: `inverse_fft`, `inverse_real_fft`.

### Function: recttopolar (a, b)

Translates complex values of the form $a + b i$ to the form
$r e^{i t}$, where $a$ is the real part and $b$ is the imaginary
part.  $a$ and $b$ are 1-dimensional arrays of the same size.
The array size need not be a power of 2.


The original values of the input arrays are
replaced by the magnitude and angle, $r$ and $t$, on return.
The outputs are calculated as



$$\eqalign{ r &= \sqrt{a^2+b^2} \cr t &= {\rm atan2}(b, a) }$$


$$\eqalign{
r &= \sqrt{a^2+b^2} \cr
t &= {\rm atan2}(b, a)
}$$



The computed angle is in the range
$-\pi$
to
$\pi.$


`recttopolar` is the inverse function of `polartorect`.


`load("fft")` loads this function.  See also `fft`.

See also: `polartorect`, `fft`.

### Function: rk_adaptive (expr, vars, vars_initval, var)

*startval*, *endval*, *params1...*)


Tries to solve the ODE whose derivates are defined by `expr` to the variables
`vars`, starting at their initial values `vars_initval`.
The independent variable (in physics: normally time) is `var`, being stepped from
`startval` to `endval`.


Sometimes it speeds up the calculation to use a floating-point number as
`startval`, as using floars will prevent all results from becoming endless rational
numbers.


The following optional parameters are accepted:



- * 
`maxstep=num`: The maximum step size to be used.
- * 
`minstep=num`: The minimum step size to be used.
- * 
`timestep_initial=num`: The initial guess for the optimum time step to start with.
- * 
`maxabserr=num`: The maximum absolute error of the resulting curves.
- * 
`maxrelerr=num`: The maximum relative error of the resulting curves as a
      fallback for variables with big values for which `maxabserr` might be too sensitive.


See also `rk`.


Example:





```maxima
maxima
(%i1) pnts:rk_adaptive(-1/10*x,x,1,t,0,100)  $
```

See also: `rk`.

### Variable: scale_lp

Default value: `false`


When `scale_lp` is `true`,
`linear_program` scales its input so that the maximum absolute value in each row or column is 1.

### Function: zgeev (zgeev, A, zgeev, A, right_p, left_p)

Like `dgeev`, but the matrix
${\bf A}$
is complex.


To make use of this function, you must load the LaPack package via
`load("lapack")`.

See also: `dgeev`.

### Function: zheev (zheev, A, zheev, A, eigvec_p)

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

