## Tensors

### Function: abasep (v)

Checks if its argument is an `atensor` base vector. That is, if it is
an indexed symbol, with the symbol being the same as the value of
`asymbol`, and the index having a numeric value between 1
and `adim`.

### Variable: adim

Default value: 0


The dimensionality of the algebra. `atensor` uses the value of `adim`
to determine if an indexed object is a valid base vector.  See `abasep`.

### Function: af (u, v)

An antisymmetric scalar function that is used in commutation relations.
The default implementation checks if both arguments are base vectors
using `abasep` and if that is the case, substitutes the
corresponding value from the matrix `aform`.

### Variable: aform

Default value: `ident(3)`


Default values for the bilinear forms `sf`, `af`, and
`av`. The default is the identity matrix `ident(3)`.

### Function: alg_type ()

The algebra type. Valid values are `universal`, `grassmann`,
`clifford`, `symmetric`, `symplectic` and `lie_envelop`.

### Variable: all_dotsimp_denoms

Default value: `false`


When `all_dotsimp_denoms` is a list,
the denominators encountered by `dotsimp` are appended to the list.
`all_dotsimp_denoms` may be initialized to an empty list `[]`
before calling `dotsimp`.


By default, denominators are not collected by `dotsimp`.

### Variable: allsym

Default value: `false`


If `true` then all indexed objects
are assumed symmetric in all of their covariant and contravariant
indices. If `false` then no symmetries of any kind are assumed
in these indices. Derivative indices are always taken to be symmetric
unless `iframe_flag` is set to `true`.

### Variable: asymbol

Default value: `v`


The symbol for base vectors.

### Function: atensimp (expr)

Simplifies an algebraic tensor expression *expr* according to the rules
configured by a call to `init_atensor`. Simplification includes
recursive application of commutation relations and resolving calls
to `sf`, `af`, and `av` where applicable. A
safeguard is used to ensure that the function always terminates, even
for complex expressions.

### Function: av (u, v)

An antisymmetric function that is used in commutation relations.
The default implementation checks if both arguments are base vectors
using `abasep` and if that is the case, substitutes the
corresponding value from the matrix `aform`.


For instance:










```maxima
(%i1) load("atensor");
(%o1)       /share/tensor/atensor.mac
(%i2) adim:3;
(%o2)                                  3
(%i3) aform:matrix([0,3,-2],[-3,0,1],[2,-1,0]);
                               [  0    3   - 2 ]
                               [               ]
(%o3)                          [ - 3   0    1  ]
                               [               ]
                               [  2   - 1   0  ]
(%i4) asymbol:x;
(%o4)                                  x
(%i5) av(x[1],x[2]);
(%o5)                                 x
                                       3
```

### Function: bdvac (f)

generates the covariant components of the vacuum field equations of
the Brans- Dicke gravitational theory. The scalar field is specified
by the argument *f*, which should be a (quoted) function name
with functional dependencies, e.g., `'p(x)`.


The components of the second rank covariant field tensor are
represented by the array `bd`.

### Function: bimetric ()

*** NOT YET IMPLEMENTED ***


generates the field equations of Rosen’s bimetric theory. The field
equations are the components of an array named `rosen`.

### Function: canform (canform, expr, canform, expr, rename)

Simplifies *expr* by renaming dummy
indices and reordering all indices as dictated by symmetry conditions
imposed on them. If `allsym` is `true` then all indices are assumed
symmetric, otherwise symmetry information provided by `decsym`
declarations will be used. The dummy indices are renamed in the same
manner as in the `rename` function. When `canform` is applied to a large
expression the calculation may take a considerable amount of time.
This time can be shortened by calling `rename` on the expression first.
Also see the example under `decsym`. Note: `canform` may not be able to
reduce an expression completely to its simplest form although it will
always return a mathematically correct result.


The optional second parameter *rename*, if set to `false`, suppresses renaming.

See also: `rename`, `decsym`.

### Function: canten (expr)

Simplifies *expr* by renaming (see `rename`)
and permuting dummy indices. `rename` is restricted to sums of tensor
products in which no derivatives are present. As such it is limited
and should only be used if `canform` is not capable of carrying out the
required simplification.


The `canten` function returns a mathematically correct result only
if its argument is an expression that is fully symmetric in its indices.
For this reason, `canten` returns an error if `allsym` is not
set to `true`.

See also: `rename`, `canform`, `allsym`.

### Function: cdisplay (ten)

displays all the elements of the tensor *ten*, as represented by
a multidimensional array. Tensors of rank 0 and 1, as well as other types
of variables, are displayed as with `ldisplay`. Tensors of rank 2 are
displayed as 2-dimensional matrices, while tensors of higher rank are displayed
as a list of 2-dimensional matrices. For instance, the Riemann-tensor of
the Schwarzschild metric can be viewed as:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) riemann(false);
(%o4)                                done
(%i5) cdisplay(riem);
          [ 0               0                   0           0     ]
          [                                                       ]
          [                              2                        ]
          [      3 m (r - 2 m)   m    2 m                         ]
          [ 0  - ------------- + -- - ----      0           0     ]
          [            4          3     4                         ]
          [           r          r     r                          ]
          [                                                       ]
riem    = [                                m (r - 2 m)            ]
    1, 1  [ 0               0              -----------      0     ]
          [                                     4                 ]
          [                                    r                  ]
          [                                                       ]
          [                                           m (r - 2 m) ]
          [ 0               0                   0     ----------- ]
          [                                                4      ]
          [                                               r       ]

                                [    2 m (r - 2 m)       ]
                                [ 0  -------------  0  0 ]
                                [          4             ]
                                [         r              ]
                     riem     = [                        ]
                         1, 2   [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]

                                [         m (r - 2 m)    ]
                                [ 0  0  - -----------  0 ]
                                [              4         ]
                                [             r          ]
                     riem     = [                        ]
                         1, 3   [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]

                                [            m (r - 2 m) ]
                                [ 0  0  0  - ----------- ]
                                [                 4      ]
                                [                r       ]
                     riem     = [                        ]
                         1, 4   [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]

                               [       0         0  0  0 ]
                               [                         ]
                               [       2 m               ]
                               [ - ------------  0  0  0 ]
                    riem     = [    2                    ]
                        2, 1   [   r  (r - 2 m)          ]
                               [                         ]
                               [       0         0  0  0 ]
                               [                         ]
                               [       0         0  0  0 ]

             [     2 m                                         ]
             [ ------------  0        0               0        ]
             [  2                                              ]
             [ r  (r - 2 m)                                    ]
             [                                                 ]
             [      0        0        0               0        ]
             [                                                 ]
  riem     = [                         m                       ]
      2, 2   [      0        0  - ------------        0        ]
             [                     2                           ]
             [                    r  (r - 2 m)                 ]
             [                                                 ]
             [                                         m       ]
             [      0        0        0         - ------------ ]
             [                                     2           ]
             [                                    r  (r - 2 m) ]

                                [ 0  0       0        0 ]
                                [                       ]
                                [            m          ]
                                [ 0  0  ------------  0 ]
                     riem     = [        2              ]
                         2, 3   [       r  (r - 2 m)    ]
                                [                       ]
                                [ 0  0       0        0 ]
                                [                       ]
                                [ 0  0       0        0 ]

                                [ 0  0  0       0       ]
                                [                       ]
                                [               m       ]
                                [ 0  0  0  ------------ ]
                     riem     = [           2           ]
                         2, 4   [          r  (r - 2 m) ]
                                [                       ]
                                [ 0  0  0       0       ]
                                [                       ]
                                [ 0  0  0       0       ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [ m          ]
                               3, 1   [ -  0  0  0 ]
                                      [ r          ]
                                      [            ]
                                      [ 0  0  0  0 ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [    m       ]
                               3, 2   [ 0  -  0  0 ]
                                      [    r       ]
                                      [            ]
                                      [ 0  0  0  0 ]

                               [   m                      ]
                               [ - -   0   0       0      ]
                               [   r                      ]
                               [                          ]
                               [        m                 ]
                               [  0   - -  0       0      ]
                    riem     = [        r                 ]
                        3, 3   [                          ]
                               [  0    0   0       0      ]
                               [                          ]
                               [              2 m - r     ]
                               [  0    0   0  ------- + 1 ]
                               [                 r        ]

                                    [ 0  0  0    0   ]
                                    [                ]
                                    [ 0  0  0    0   ]
                                    [                ]
                         riem     = [            2 m ]
                             3, 4   [ 0  0  0  - --- ]
                                    [             r  ]
                                    [                ]
                                    [ 0  0  0    0   ]

                                [       0        0  0  0 ]
                                [                        ]
                                [       0        0  0  0 ]
                                [                        ]
                     riem     = [       0        0  0  0 ]
                         4, 1   [                        ]
                                [      2                 ]
                                [ m sin (theta)          ]
                                [ -------------  0  0  0 ]
                                [       r                ]

                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                     riem     = [ 0        0        0  0 ]
                         4, 2   [                        ]
                                [         2              ]
                                [    m sin (theta)       ]
                                [ 0  -------------  0  0 ]
                                [          r             ]

                              [ 0  0          0          0 ]
                              [                            ]
                              [ 0  0          0          0 ]
                              [                            ]
                   riem     = [ 0  0          0          0 ]
                       4, 3   [                            ]
                              [                2           ]
                              [         2 m sin (theta)    ]
                              [ 0  0  - ---------------  0 ]
                              [                r           ]

           [        2                                             ]
           [   m sin (theta)                                      ]
           [ - -------------         0                0         0 ]
           [         r                                            ]
           [                                                      ]
           [                         2                            ]
           [                    m sin (theta)                     ]
riem     = [        0         - -------------         0         0 ]
    4, 4   [                          r                           ]
           [                                                      ]
           [                                          2           ]
           [                                   2 m sin (theta)    ]
           [        0                0         ---------------  0 ]
           [                                          r           ]
           [                                                      ]
           [        0                0                0         0 ]

(%o5)                                done
```

### Variable: cframe_flag

Causes computations to be performed relative to a moving frame as opposed to
a holonomic metric. The frame is defined by the inverse frame array `fri`
and the frame metric `lfg`. For computations using a Cartesian frame,
`lfg` should be the unit matrix of the appropriate dimension; for
computations in a Lorentz frame, `lfg` should have the appropriate
signature.

### Function: cgeodesic (dis)

A function in the `ctensor` (component tensor)
package.  `cgeodesic` computes the geodesic equations of
motion for a given metric.  They are stored in the array `geod[i]`.  If
the argument *dis* is `true` then these equations are displayed.

### Function: changename (old, new, expr)

will change the name of all indexed objects called *old* to *new*
in *expr*. *old* may be either a symbol or a list of the form
`[name, m, n]` in which case only those indexed objects called
*name* with *m* covariant and *n* contravariant indices will be
renamed to *new*.

### Function: check_overlaps (n, add_to_simps)

Checks the overlaps thru degree *n*,
making sure that you have sufficient simplification rules in each
degree, for `dotsimp` to work correctly.  This process can be speeded
up if you know before hand what the dimension of the space of monomials is.
If it is of finite global dimension, then `hilbert` should be used.  If you
don’t know the monomial dimensions, do not specify a `rank_function`.
An optional third argument `reset`, `false` says don’t bother to query
about resetting things.


`load("affine")` loads this function.

### Function: checkdiv ()

computes the covariant divergence of the mixed second rank tensor
(whose first index must be covariant) by printing the
corresponding n components of the vector field (the divergence) where
n = `dim`. If the argument to the function is `g` then the
divergence of the Einstein tensor will be formed and must be zero.
In addition, the divergence (vector) is given the array name `div`.

### Function: christof (dis)

A function in the `ctensor` (component tensor)
package.  It computes the Christoffel symbols of both
kinds.  The argument *dis* determines which results are to be immediately
displayed.  The Christoffel symbols of the first and second kinds are
stored in the arrays `lcs[i,j,k]` and `mcs[i,j,k]` respectively and
defined to be symmetric in the first two indices. If the argument to
`christof` is `lcs` or `mcs` then the unique non-zero values of `lcs[i,j,k]`
or `mcs[i,j,k]`, respectively, will be displayed. If the argument is `all`
then the unique non-zero values of `lcs[i,j,k]` and `mcs[i,j,k]` will be
displayed.  If the argument is `false` then the display of the elements
will not occur. The array elements `mcs[i,j,k]` are defined in such a
manner that the final index is contravariant.

### Function: cmetric (cmetric, dis, cmetric)

A function in the `ctensor` (component tensor) package
that computes the metric inverse and sets up the package for
further calculations.


If `cframe_flag` is `false`, the function computes the inverse metric
`ug` from the (user-defined) matrix `lg`. The metric determinant is
also computed and stored in the variable `gdet`. Furthermore, the
package determines if the metric is diagonal and sets the value
of `diagmetric` accordingly. If the optional argument *dis*
is present and not equal to `false`, the user is prompted to see
the metric inverse.


If `cframe_flag` is `true`, the function expects that the values of
`fri` (the inverse frame matrix) and `lfg` (the frame metric) are
defined. From these, the frame matrix `fr` and the inverse frame
metric `ufg` are computed.

### Variable: cnonmet_flag

Causes the nonmetricity coefficients to be included in the computation of
the connection coefficients. The nonmetricity coefficients are computed
from the user-supplied nonmetricity vector `nm` by the function
`nonmetricity`.

### Function: cograd ()

Computes the covariant gradient of a scalar function allowing the
user to choose the corresponding vector name as the example under
`contragrad` illustrates.

### Function: components (tensor, expr)

permits one to assign an indicial value to an expression
*expr* giving the values of the components of *tensor*. These
are automatically substituted for the tensor whenever it occurs with
all of its indices. The tensor must be of the form `t([...],[...])`
where either list may be empty. *expr* can be any indexed expression
involving other objects with the same free indices as *tensor*. When
used to assign values to the metric tensor wherein the components
contain dummy indices one must be careful to define these indices to
avoid the generation of multiple dummy indices. Removal of this
assignment is given to the function `remcomps`.


It is important to keep in mind that `components` cares only about
the valence of a tensor, not about any particular index ordering. Thus
assigning components to, say, `x([i,-j],[])`, `x([-j,i],[])`, or
`x([i],[j])` all produce the same result, namely components being
assigned to a tensor named `x` with valence `(1,1)`.


Components can be assigned to an indexed expression in four ways, two
of which involve the use of the `components` command:


1) As an indexed expression. For instance:



```maxima
(%i2) components(g([],[i,j]),e([],[i])*p([],[j]))$
(%i3) ishow(g([],[i,j]))$
                                      i  j
(%t3)                                e  p
```


2) As a matrix:



```maxima
(%i5) lg:-ident(4)$lg[1,1]:1$lg;

                            [ 1   0    0    0  ]
                            [                  ]
                            [ 0  - 1   0    0  ]
(%o5)                       [                  ]
                            [ 0   0   - 1   0  ]
                            [                  ]
                            [ 0   0    0   - 1 ]

(%i6) components(g([i,j],[]),lg);
(%o6)                                done
(%i7) ishow(g([i,j],[]))$
(%t7)                                g
                                      i j
(%i8) g([1,1],[]);
(%o8)                                  1
(%i9) g([4,4],[]);
(%o9)                                 - 1
```


3) As a function. You can use a Maxima function to specify the
components of a tensor based on its indices. For instance, the following
code assigns `kdelta` to `h` if `h` has the same number
of covariant and contravariant indices and no derivative indices, and
`g` otherwise:



```maxima
(%i4) h(l1,l2,[l3]):=if length(l1)=length(l2) and length(l3)=0
  then kdelta(l1,l2) else apply(g,append([l1,l2], l3))$
(%i5) ishow(h([i],[j]))$
                                          j
(%t5)                               kdelta
                                          i
(%i6) ishow(h([i,j],[k],l))$
                                     k
(%t6)                               g
                                     i j,l
```


4) Using Maxima’s pattern matching capabilities, specifically the
`defrule` and `applyb1` commands:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) matchdeclare(l1,listp);
(%o2)                                done
(%i3) defrule(r1,m(l1,[]),(i1:idummy(),
      g([l1[1],l1[2]],[])*q([i1],[])*e([],[i1])))$

(%i4) defrule(r2,m([],l1),(i1:idummy(),
      w([],[l1[1],l1[2]])*e([i1],[])*q([],[i1])))$

(%i5) ishow(m([i,n],[])*m([],[i,m]))$

                                    i m
(%t5)                              m    m
                                         i n

(%i6) ishow(rename(applyb1(%,r1,r2)))$
                           %1  %2  %3 m
(%t6)                     e   q   w     q   e   g
                                         %1  %2  %3 n
```

See also: `remcomps`, `kdelta`, `defrule`, `applyb1`.

### Function: concan (expr)

Similar to `canten` but also performs index contraction.

See also: `canten`.

### Function: conmetderiv (expr, tensor)

Simplifies expressions containing ordinary derivatives of
both covariant and con­tra­va­ri­ant forms of the metric tensor (the
current restriction).  For example, `conmetderiv` can relate the
derivative of the contravariant metric tensor with the Christoffel
symbols as seen from the following:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(g([],[a,b],c))$
                                      a b
(%t2)                                g
                                      ,c
(%i3) ishow(conmetderiv(%,g))$
                         %1 b      a       %1 a      b
(%t3)                 - g     ichr2     - g     ichr2
                                   %1 c              %1 c
```

### Function: contortion (tr)

Computes the (2,1) contortion coefficients from the torsion tensor *tr*.

### Function: contract (expr)

Carries out the tensorial contractions in *expr* which may be any
combination of sums and products. This function uses the information
given to the `defcon` function. For best results, `expr`
should be fully expanded. `ratexpand` is the fastest way to expand
products and powers of sums if there are no variables in the denominators
of the terms. The `gcd` switch should be `false` if GCD
cancellations are unnecessary.

See also: `ratexpand`, `gcd`.

### Function: contragrad ()

Computes the contravariant gradient of a scalar function allowing

the user to choose the corresponding vector name as the example
below for the Schwarzschild metric illustrates:













```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(f,r);
(%o4)                               [f(r)]
(%i5) cograd(f,g1);
(%o5)                                done
(%i6) listarray(g1);
(%o6)                            [0, f , 0, 0]
                                      r
(%i7) contragrad(f,g2);
(%o7)                                done
(%i8) listarray(g2);
                               f  r - 2 f  m
                                r        r
(%o8)                      [0, -------------, 0, 0]
                                     r
```

### Function: coord (tensor_1, tensor_2, ...)

Gives *tensor_i* the coordinate differentiation property that the
derivative of contravariant vector whose name is one of the
*tensor_i* yields a Kronecker delta. For example, if `coord(x)` has
been done then `idiff(x([],[i]),j)` gives `kdelta([i],[j])`.
`coord` is a list of all indexed objects having this property.

### Function: covdiff (expr, v_1, v_2, ...)

Yields the covariant derivative of *expr* with
respect to the variables *v_i* in terms of the Christoffel symbols of the
second kind (`ichr2`).  In order to evaluate these, one should use
`ev(expr,ichr2)`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) entertensor()$
Enter tensor name: a;
Enter a list of the covariant indices: [i,j];
Enter a list of the contravariant indices: [k];
Enter a list of the derivative indices: [];
                                      k
(%t2)                                a
                                      i j
(%i3) ishow(covdiff(%,s))$
             k         %1     k         %1     k
(%t3)     - a     ichr2    - a     ichr2    + a
             i %1      j s    %1 j      i s    i j,s

             k     %1
      + ichr2     a
             %1 s  i j
(%i4) imetric:g;
(%o4)                                  g
(%i5) ishow(ev(%th(2),ichr2))$
         %1 %4  k
        g      a     (g       - g       + g      )
                i %1   s %4,j    j s,%4    j %4,s
(%t5) - ------------------------------------------
                            2

    %1 %3  k
   g      a     (g       - g       + g      )
           %1 j   s %3,i    i s,%3    i %3,s
 - ------------------------------------------
                       2
    k %2  %1
   g     a    (g        - g        + g       )
          i j   s %2,%1    %1 s,%2    %1 %2,s     k
 + ------------------------------------------- + a
                        2                         i j,s

(%i6)
```

### Function: csetup ()

A function in the `ctensor` (component tensor) package
which initializes the package and allows the user to enter a metric
interactively. See `ctensor` for more details.

### Variable: ct_coords

Default value: `[]`


An option in the `ctensor` (component tensor)
package.  `ct_coords` contains a list of coordinates.
While normally defined when the function `csetup` is called,
one may redefine the coordinates with the assignment
`ct_coords: [j1, j2, ..., jn]` where the j’s are the new coordinate names.
See also `csetup`.

See also: `csetup`.

### Function: ct_coordsys (ct_coordsys, coordinate_system, extra_arg, ct_coordsys, coordinate_system)

Sets up a predefined coordinate system and metric. The argument
*coordinate_system* can be one of the following symbols:



```maxima
SYMBOL             Dim Coordinates     Description/comments
 ------------------------------------------------------------------
 cartesian2d           2  [x,y]             Cartesian 2D coordinate
                                            system
 polar                 2  [r,phi]           Polar coordinate system
 elliptic              2  [u,v]             Elliptic coord. system
 confocalelliptic      2  [u,v]             Confocal elliptic
                                            coordinates
 bipolar               2  [u,v]             Bipolar coord. system
 parabolic             2  [u,v]             Parabolic coord. system
 cartesian3d           3  [x,y,z]           Cartesian 3D coordinate
                                            system
 polarcylindrical      3  [r,theta,z]       Polar 2D with
                                            cylindrical z
 ellipticcylindrical   3  [u,v,z]           Elliptic 2D with
                                            cylindrical z
 confocalellipsoidal   3  [u,v,w]           Confocal ellipsoidal
 bipolarcylindrical    3  [u,v,z]           Bipolar 2D with
                                            cylindrical z
 paraboliccylindrical  3  [u,v,z]           Parabolic 2D with
                                            cylindrical z
 paraboloidal          3  [u,v,phi]         Paraboloidal coords.
 conical               3  [u,v,w]           Conical coordinates
 toroidal              3  [phi,u,v]         Toroidal coordinates
 spherical             3  [r,theta,phi]     Spherical coord. system
 oblatespheroidal      3  [u,v,phi]         Oblate spheroidal
                                            coordinates
 oblatespheroidalsqrt  3  [u,v,phi]
 prolatespheroidal     3  [u,v,phi]         Prolate spheroidal
                                            coordinates
 prolatespheroidalsqrt 3  [u,v,phi]
 ellipsoidal           3  [r,theta,phi]     Ellipsoidal coordinates
 cartesian4d           4  [x,y,z,t]         Cartesian 4D coordinate
                                            system
 spherical4d           4  [r,theta,eta,phi] Spherical 4D coordinate
                                            system
 exteriorschwarzschild 4  [t,r,theta,phi]   Schwarzschild metric
 interiorschwarzschild 4  [t,z,u,v]         Interior Schwarzschild
                                            metric
 kerr_newman           4  [t,r,theta,phi]   Charged axially
                                            symmetric metric
```


`coordinate_system` can also be a list of transformation functions,
followed by a list containing the coordinate variables. For instance,
you can specify a spherical metric as follows:











```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o2)                                done
(%i3) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o3)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
(%i4) ct_coords;
(%o4)                           [r, theta, phi]
(%i5) dim;
(%o5)                                  3
```


Transformation functions can also be used when `cframe_flag` is `true`:












```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) cframe_flag:true;
(%o2)                                true
(%i3) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o3)                                done
(%i4) fri;
(%o4)
 [cos(phi)cos(theta) -cos(phi) r sin(theta) -sin(phi) r cos(theta)]
 [                                                                ]
 [sin(phi)cos(theta) -sin(phi) r sin(theta)  cos(phi) r cos(theta)]
 [                                                                ]
 [    sin(theta)           r cos(theta)                0          ]

(%i5) cmetric();
(%o5)                                false
(%i6) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o6)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
```


The optional argument *extra_arg* can be any one of the following:



`cylindrical` tells `ct_coordsys` to attach an additional cylindrical coordinate.


`minkowski` tells `ct_coordsys` to attach an additional coordinate with negative metric signature.


`all` tells `ct_coordsys` to call `cmetric` and `christof(false)` after setting up the metric.



If the global variable `verbose` is set to `true`, `ct_coordsys` displays the values of `dim`, `ct_coords`, and either `lg` or `lfg` and `fri`, depending on the value of `cframe_flag`.

### Function: ctaylor ()

The `ctaylor` function truncates its argument by converting
it to a Taylor-series using `taylor`, and then calling
`ratdisrep`. This has the combined effect of dropping terms
higher order in the expansion variable `ctayvar`. The order
of terms that should be dropped is defined by `ctaypov`; the
point around which the series expansion is carried out is specified
in `ctaypt`.


As an example, consider a simple metric that is a perturbation of
the Minkowski metric. Without further restrictions, even a diagonal
metric produces expressions for the Einstein tensor that are far too
complex:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) derivabbrev:true;
(%o3)                                true
(%i4) ct_coords:[t,r,theta,phi];
(%o4)                         [t, r, theta, phi]
(%i5) lg:matrix([-1,0,0,0],[0,1,0,0],[0,0,r^2,0],
                [0,0,0,r^2*sin(theta)^2]);
                        [ - 1  0  0         0        ]
                        [                            ]
                        [  0   1  0         0        ]
                        [                            ]
(%o5)                   [          2                 ]
                        [  0   0  r         0        ]
                        [                            ]
                        [              2    2        ]
                        [  0   0  0   r  sin (theta) ]
(%i6) h:matrix([h11,0,0,0],[0,h22,0,0],[0,0,h33,0],[0,0,0,h44]);
                            [ h11   0    0    0  ]
                            [                    ]
                            [  0   h22   0    0  ]
(%o6)                       [                    ]
                            [  0    0   h33   0  ]
                            [                    ]
                            [  0    0    0   h44 ]
(%i7) depends(l,r);
(%o7)                               [l(r)]
(%i8) lg:lg+l*h;
      [ h11 l - 1      0          0                 0            ]
      [                                                          ]
      [     0      h22 l + 1      0                 0            ]
      [                                                          ]
(%o8) [                        2                                 ]
      [     0          0      r  + h33 l            0            ]
      [                                                          ]
      [                                    2    2                ]
      [     0          0          0       r  sin (theta) + h44 l ]
(%i9) cmetric(false);
(%o9)                                done
(%i10) einstein(false);
(%o10)                               done
(%i11) ntermst(ein);
[[1, 1], 62]
[[1, 2], 0]
[[1, 3], 0]
[[1, 4], 0]
[[2, 1], 0]
[[2, 2], 24]
[[2, 3], 0]
[[2, 4], 0]
[[3, 1], 0]
[[3, 2], 0]
[[3, 3], 46]
[[3, 4], 0]
[[4, 1], 0]
[[4, 2], 0]
[[4, 3], 0]
[[4, 4], 46]
(%o12)                               done
```


However, if we recompute this example as an approximation that is
linear in the variable `l`, we get much simpler expressions:



```maxima
(%i14) ctayswitch:true;
(%o14)                               true
(%i15) ctayvar:l;
(%o15)                                 l
(%i16) ctaypov:1;
(%o16)                                 1
(%i17) ctaypt:0;
(%o17)                                 0
(%i18) christof(false);
(%o18)                               done
(%i19) ricci(false);
(%o19)                               done
(%i20) einstein(false);
(%o20)                               done
(%i21) ntermst(ein);
[[1, 1], 6]
[[1, 2], 0]
[[1, 3], 0]
[[1, 4], 0]
[[2, 1], 0]
[[2, 2], 13]
[[2, 3], 2]
[[2, 4], 0]
[[3, 1], 0]
[[3, 2], 2]
[[3, 3], 9]
[[3, 4], 0]
[[4, 1], 0]
[[4, 2], 0]
[[4, 3], 0]
[[4, 4], 9]
(%o21)                               done
(%i22) ratsimp(ein[1,1]);
                         2      2  4               2     2
(%o22) - (((h11 h22 - h11 ) (l )  r  - 2 h33 l    r ) sin (theta)
                              r               r r

                            2               2      4    2
              - 2 h44 l    r  - h33 h44 (l ) )/(4 r  sin (theta))
                       r r                r
```


This capability can be useful, for instance, when working in the weak
field limit far from a gravitational source.

### Variable: ctaypov

Maximum power used in Taylor-series expansion when `ctayswitch` is
set to `true`.

### Variable: ctaypt

Point around which Taylor-series expansion is carried out when
`ctayswitch` is set to `true`.

### Variable: ctayswitch

If set to `true`, causes some `ctensor` computations to be carried out using
Taylor-series expansions. Presently, `christof`, `ricci`,
`uricci`, `einstein`, and `weyl` take into account this
setting.

### Variable: ctayvar

Variable used for Taylor-series expansion if `ctayswitch` is set to
`true`.

### Variable: ctorsion_flag

Causes the contortion tensor to be included in the computation of the
connection coefficients. The contortion tensor itself is computed by
`contortion` from the user-supplied tensor `tr`.

### Function: ctransform (M)

A function in the `ctensor` (component tensor)
package which will perform a coordinate transformation
upon an arbitrary square symmetric matrix *M*. The user must input the
functions which define the transformation.  (Formerly called `transform`.)
These may also be supplied in the form of a list as an optional second argument.

### Variable: ctrgsimp

Causes trigonometric simplifications to be used when tensors are computed. Presently,
`ctrgsimp` affects only computations involving a moving frame.

### Function: declare_weights (x_1, w_1, ..., x_n, w_n)

Assigns weights *w_1*, ..., *w_n* to *x_1*, ..., *x_n*, respectively.
These are the weights used in computing `nc_degree`.


`load("affine")` loads this function.

### Function: decsym (tensor, m, n, cov_1, cov_2, ..., contr_1, contr_2, ...)

Declares symmetry properties for *tensor* of *m* covariant and
*n* contravariant indices. The *cov_i* and *contr_i* are
pseudofunctions expressing symmetry relations among the covariant and
contravariant indices respectively.  These are of the form
`symoper(index_1, index_2,...)` where `symoper` is one of
`sym`, `anti` or `cyc` and the *index_i* are integers
indicating the position of the index in the *tensor*.  This will
declare *tensor* to be symmetric, antisymmetric or cyclic respectively
in the *index_i*. `symoper(all)` is also an allowable form which
indicates all indices obey the symmetry condition. For example, given an
object `b` with 5 covariant indices,
`decsym(b,5,3,[sym(1,2),anti(3,4)],[cyc(all)])` declares `b`
symmetric in its first and second and antisymmetric in its third and
fourth covariant indices, and cyclic in all of its contravariant indices.
Either list of symmetry declarations may be null.  The function which
performs the simplifications is `canform` as the example below
illustrates.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:contract( expand( a([i1, j1, k1], [])
           *kdels([i, j, k], [i1, j1, k1])))$
(%i3) ishow(expr)$

(%t3)         a      + a      + a      + a      + a      + a
               k j i    k i j    j k i    j i k    i k j    i j k

(%i4) decsym(a,3,0,[sym(all)],[]);
(%o4)                                done
(%i5) ishow(canform(expr))$
(%t5)                              6 a
                                      i j k
(%i6) remsym(a,3,0);
(%o6)                                done
(%i7) decsym(a,3,0,[anti(all)],[]);
(%o7)                                done
(%i8) ishow(canform(expr))$
(%t8)                                  0
(%i9) remsym(a,3,0);
(%o9)                                done
(%i10) decsym(a,3,0,[cyc(all)],[]);
(%o10)                               done
(%i11) ishow(canform(expr))$
(%t11)                        3 a      + 3 a
                                 i k j      i j k
(%i12) dispsym(a,3,0);
(%o12)                     [[cyc, [[1, 2, 3]], []]]
```

### Function: defcon (defcon, tensor_1, defcon, tensor_1, tensor_2, tensor_3)

gives *tensor_1* the property that the
contraction of a product of *tensor_1* and *tensor_2* results in *tensor_3*
with the appropriate indices.  If only one argument, *tensor_1*, is
given, then the contraction of the product of *tensor_1* with any indexed
object having the appropriate indices (say `my_tensor`) will yield an
indexed object with that name, i.e. `my_tensor`, and with a new set of
indices reflecting the contractions performed.
    For example, if `imetric:g`, then `defcon(g)` will implement the
raising and lowering of indices through contraction with the metric
tensor.
    More than one `defcon` can be given for the same indexed object; the
latest one given which applies in a particular contraction will be
used.
`contractions` is a list of those indexed objects which have been given
contraction properties with `defcon`.

### Function: deleten (L, n)

Returns a new list consisting of *L* with the *n*’th element
deleted.

### Function: diagmatrixp (M, n)

Returns `true` if the first *n* rows and *n* columns of *M*
form a diagonal matrix or (2D) array.

### Variable: diagmetric

Default value: `false`


An option in the `ctensor` (component tensor)
package.  If `diagmetric` is `true` special routines compute
all geometrical objects (which contain the metric tensor explicitly)
by taking into consideration the diagonality of the metric. Reduced
run times will, of course, result. Note: this option is set
automatically by `csetup` if a diagonal metric is specified.

### Variable: dim

Default value: 4


An option in the `ctensor` (component tensor)
package.  `dim` is the dimension of the manifold with the
default 4. The command `dim: n` will reset the dimension to any other
value `n`.

### Function: dispcon (dispcon, tensor_1, tensor_2, ..., dispcon, all)

Displays the contraction properties of its arguments as were given to
`defcon`.  `dispcon (all)` displays all the contraction properties
which were defined.

### Function: dispsym (tensor, m, n)

Displays all of the defined symmetries from *tensor* which has *m*
covariant indices and *n* contravariant indices. See `decsym`
for an example.

See also: `decsym`.

### Function: dotsimp (f)

Returns 0 if and only if *f* is in the ideal generated by the equations, i.e.,
if and only if *f* is a polynomial combination of the elements of the equations.


`load("affine")` loads this function.

### Function: dscalar ()

computes the tensor d’Alembertian of the scalar function once
dependencies have been declared upon the function. For example:










```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(p,r);
(%o4)                               [p(r)]
(%i5) factor(dscalar(p));

                          2
                    p    r  - 2 m p    r + 2 p  r - 2 m p
                     r r           r r        r          r
(%o5)               --------------------------------------
                                       2
                                      r
```

### Function: einstein (dis)

A function in the `ctensor` (component tensor)
package.  `einstein` computes the mixed Einstein tensor
after the Christoffel symbols and Ricci tensor have been obtained
(with the functions `christof` and `ricci`).  If the argument *dis* is
`true`, then the non-zero values of the mixed Einstein tensor `ein[i,j]`
will be displayed where `j` is the contravariant index.
The variable `rateinstein` will cause the rational simplification on
these components. If `ratfac` is `true` then the components will
also be factored.

### Function: entertensor (name)

is a function which, by prompting, allows one to create an indexed
object called *name* with any number of tensorial and derivative
indices. Either a single index or a list of indices (which may be
null) is acceptable input (see the example under `covdiff`).

See also: `covdiff`.

### Function: evundiff (expr)

Equivalent to the execution of `undiff`, followed by `ev` and
`rediff`.


The point of this operation is to easily evaluate expressions that cannot
be directly evaluated in derivative form. For instance, the following
causes an error:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) icurvature([i,j,k],[l],m);
Maxima encountered a Lisp error:

 Error in $ICURVATURE [or a callee]:
 $ICURVATURE [or a callee] requires less than three arguments.

Automatically continuing.
To re-enable the Lisp debugger set *debugger-hook* to nil.
```


However, if `icurvature` is entered in noun form, it can be evaluated
using `evundiff`:



```maxima
(%i3) ishow('icurvature([i,j,k],[l],m))$
                                         l
(%t3)                          icurvature
                                         i j k,m
(%i4) ishow(evundiff(%))$
             l              l         %1           l           %1
(%t4) - ichr2        - ichr2     ichr2      - ichr2       ichr2
             i k,j m        %1 j      i k,m        %1 j,m      i k

             l              l         %1           l           %1
      + ichr2        + ichr2     ichr2      + ichr2       ichr2
             i j,k m        %1 k      i j,m        %1 k,m      i j
```


Note: In earlier versions of Maxima, derivative forms of the
Christoffel-symbols also could not be evaluated. This has been fixed now,
so `evundiff` is no longer necessary for expressions like this:



```maxima
(%i5) imetric(g);
(%o5)                                done
(%i6) ishow(ichr2([i,j],[k],l))$
       k %3
      g     (g         - g         + g        )
              j %3,i l    i j,%3 l    i %3,j l
(%t6) -----------------------------------------
                          2

                         k %3
                        g     (g       - g       + g      )
                         ,l     j %3,i    i j,%3    i %3,j
                      + -----------------------------------
                                         2
```

See also: `undiff`, `ev`, `rediff`, `icurvature`.

### Function: ext_diff (form)

The exterior derivative operator. It takes one argument, which should be a differential form.

### Function: extdiff (expr, i)

Computes the exterior derivative of *expr* with respect to the index
*i*. The exterior derivative is formally defined as the wedge
product of the partial derivative operator and a differential form. As
such, this operation is also controlled by the setting of `igeowedge_flag`.
For instance:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(extdiff(v([i]),j))$
                                  v    - v
                                   j,i    i,j
(%t2)                             -----------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(extdiff(a([i,j]),k))$
                           a      - a      + a
                            j k,i    i k,j    i j,k
(%t4)                      ------------------------
                                      3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(extdiff(v([i]),j))$
(%t6)                             v    - v
                                   j,i    i,j
(%i7) ishow(extdiff(a([i,j]),k))$
(%t7)                    - (a      - a      + a     )
                             k j,i    k i,j    j i,k
```

See also: `igeowedge_flag`.

### Function: extract_linear_equations (p_1, ..., p_n, m_1, ..., m_n)

Makes a list of the coefficients of the noncommutative polynomials *p_1*, ..., *p_n*
of the noncommutative monomials *m_1*, ..., *m_n*.
The coefficients should be scalars.   Use `list_nc_monomials` to build the list of
monomials.


`load("affine")` loads this function.

### Function: fast_central_elements (x_1, ..., x_n, n)

If `set_up_dot_simplifications` has been previously done, finds the central polynomials
in the variables *x_1*, ..., *x_n* in the given degree, *n*.


For example:


```maxima
set_up_dot_simplifications ([y.x + x.y], 3);
fast_central_elements ([x, y], 2);
[y.y, x.x];
```


`load("affine")` loads this function.

### Function: fast_linsolve (expr_1, ..., expr_m, x_1, ..., x_n)

Solves the simultaneous linear equations *expr_1*, ..., *expr_m*
for the variables *x_1*, ..., *x_n*.
Each *expr_i* may be an equation or a general expression;
if given as a general expression, it is treated as an equation of the form `expr_i = 0`.


The return value is a list of equations of the form
`[x_1 = a_1, ..., x_n = a_n]`
where *a_1*, ..., *a_n* are all free of *x_1*, ..., *x_n*.


`fast_linsolve` is faster than `linsolve` for system of equations which
are sparse.


`load("affine")` loads this function.

### Variable: fb

Frame bracket coefficients, as computed by `frame_bracket`.

### Function: findde (A, n)

returns a list of the unique differential equations (expressions)
corresponding to the elements of the *n* dimensional square
array *A*. Presently, *n* may be 2 or 3. `deindex` is a global list
containing the indices of *A* corresponding to these unique
differential equations. For the Einstein tensor (`ein`), which
is a two dimensional array, if computed for the metric in the example
below, `findde` gives the following independent differential equations:

















```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) dim:4;
(%o3)                                  4
(%i4) lg:matrix([a, 0, 0, 0], [ 0, x^2, 0, 0],
                              [0, 0, x^2*sin(y)^2, 0], [0,0,0,-d]);
                          [ a  0       0        0  ]
                          [                        ]
                          [     2                  ]
                          [ 0  x       0        0  ]
(%o4)                     [                        ]
                          [         2    2         ]
                          [ 0  0   x  sin (y)   0  ]
                          [                        ]
                          [ 0  0       0       - d ]
(%i5) depends([a,d],x);
(%o5)                            [a(x), d(x)]
(%i6) ct_coords:[x,y,z,t];
(%o6)                            [x, y, z, t]
(%i7) cmetric();
(%o7)                                done
(%i8) einstein(false);
(%o8)                                done
(%i9) findde(ein,2);
                                            2
(%o9) [d  x - a d + d, 2 a d d    x - a (d )  x - a  d d  x
        x                     x x         x        x    x

                                              2          2
                          + 2 a d d   - 2 a  d , a  x + a  - a]
                                   x       x      x
(%i10) deindex;
(%o10)                     [[1, 1], [2, 2], [4, 4]]
```

### Variable: flipflag

Default value: `false`


If `false` then the indices will be
renamed according to the order of the contravariant indices,
otherwise according to the order of the covariant indices.


If `flipflag` is `false` then `rename` forms a list
of the contravariant indices as they are encountered from left to right
(if `true` then of the covariant indices). The first dummy
index in the list is renamed to `%1`, the next to `%2`, etc.
Then sorting occurs after the `rename`-ing (see the example
under `rename`).

### Function: flush (expr, tensor_1, tensor_2, ...)

Set to zero, in
*expr*, all occurrences of the *tensor_i* that have no derivative indices.

### Function: flush1deriv (expr, tensor)

Set to zero, in `expr`, all occurrences of `tensor` that have
exactly one derivative index.

### Function: flushd (expr, tensor_1, tensor_2, ...)

Set to zero, in
*expr*, all occurrences of the *tensor_i* that have derivative indices.

### Function: flushnd (expr, tensor, n)

Set to zero, in *expr*, all
occurrences of the differentiated object *tensor* that have *n* or more
derivative indices as the following example demonstrates.


```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i],[J,r],k,r)+a([i],[j,r,s],k,r,s))$
                                J r      j r s
(%t2)                          a      + a
                                i,k r    i,k r s
(%i3) ishow(flushnd(%,a,3))$
                                     J r
(%t3)                               a
                                     i,k r
```

### Function: frame_bracket (fr, fri, diagframe)

The frame bracket (`fb[]`).


Computes the frame bracket according to the following definition:



```maxima
c          c         c        d     e
ifb   = ( ifri    - ifri    ) ifr   ifr
   ab         d,e       e,d      a     b
```

### Variable: gdet

The determinant of the metric tensor `lg`. Computed by `cmetric` when
`cframe_flag` is set to `false`.

### Function: grobner_basis (expr_1, ..., expr_m)

Returns a Groebner basis for the equations *expr_1*, ..., *expr_m*.
The function `polysimp` can then
be used to simplify other functions relative to the equations.



```maxima
grobner_basis ([3*x^2+1, y*x])$

polysimp (y^2*x + x^3*9 + 2) ==> -3*x + 2
```


`polysimp(f)` yields 0 if and only if *f* is in the ideal generated by
*expr_1*, ..., *expr_m*, that is,
if and only if *f* is a polynomial combination of the elements of
*expr_1*, ..., *expr_m*.


`load("affine")` loads this function.

### Function: hodge (expr)

Compute the Hodge-dual of *expr*. For instance:
















```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                            done
(%i3) idim(4);
(%o3)                            done
(%i4) icounter:100;
(%o4)                             100
(%i5) decsym(A,3,0,[anti(all)],[])$

(%i6) ishow(A([i,j,k],[]))$
(%t6)                           A
                                 i j k
(%i7) ishow(canform(hodge(%)))$
                          %1 %2 %3 %4
               levi_civita            g        A
                                       %1 %102  %2 %3 %4
(%t7)          -----------------------------------------
                                   6
(%i8) ishow(canform(hodge(%)))$
                 %1 %2 %3 %8            %4 %5 %6 %7
(%t8) levi_civita            levi_civita            g       
                                                     %1 %106
                             g        g        g      A         /6
                              %2 %107  %3 %108  %4 %8  %5 %6 %7
(%i9) lc2kdt(%)$

(%i10) %,kdelta$

(%i11) ishow(canform(contract(expand(%))))$
(%t11)                     - A
                              %106 %107 %108
```

### Function: ic_convert (eqn)

Converts the `itensor` equation *eqn* to a `ctensor` assignment statement.
Implied sums over dummy indices are made explicit while indexed
objects are transformed into arrays (the array subscripts are in the
order of covariant followed by contravariant indices of the indexed
objects). The derivative of an indexed object will be replaced by the
noun form of `diff` taken with respect to `ct_coords` subscripted
by the derivative index. The Christoffel symbols `ichr1` and `ichr2`
will be translated to `lcs` and `mcs`, respectively and if
`metricconvert` is `true` then all occurrences of the metric
with two covariant (contravariant) indices will be renamed to `lg`
(`ug`). In addition, `do` loops will be introduced summing over
all free indices so that the
transformed assignment statement can be evaluated by just doing
`ev`. The following examples demonstrate the features of this
function.


















```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) eqn:ishow(t([i,j],[k])=f([],[])*g([l,m],[])*a([],[m],j)
      *b([i],[l,k]))$
                             k        m   l k
(%t2)                       t    = f a   b    g
                             i j      ,j  i    l m
(%i3) ic_convert(eqn);
(%o3) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 g    , l, 1, dim), m, 1, dim)))
  l, m
(%i4) imetric(g);
(%o4)                                done
(%i5) metricconvert:true;
(%o5)                                true
(%i6) ic_convert(eqn);
(%o6) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 lg    , l, 1, dim), m, 1, dim)))
   l, m
```

See also: `diff`, `ct_coords`, `ichr1`, `ichr2`, `do`, `ev`.

### Variable: icc1

Connection coefficients of the first kind. In `itensor`, defined as



```maxima
icc1    = ichr1    - ikt1    - inmc1
    abc        abc       abc        abc
```


In this expression, if `iframe_flag` is true, the Christoffel-symbol
`ichr1` is replaced with the frame connection coefficient `ifc1`.
If `itorsion_flag` is `false`, `ikt1`
will be omitted. It is also omitted if a frame base is used, as the
torsion is already calculated as part of the frame bracket.
Lastly, of `inonmet_flag` is `false`,
`inmc1` will not be present.

See also: `ikt1`, `inmc1`.

### Variable: icc2

Connection coefficients of the second kind. In `itensor`, defined as



```maxima
c         c        c         c
icc2   = ichr2   - ikt2   - inmc2
    ab        ab       ab        ab
```


In this expression, if `iframe_flag` is true, the Christoffel-symbol
`ichr2` is replaced with the frame connection coefficient `ifc2`.
If `itorsion_flag` is `false`, `ikt2`
will be omitted. It is also omitted if a frame base is used, as the
torsion is already calculated as part of the frame bracket.
Lastly, of `inonmet_flag` is `false`,
`inmc2` will not be present.

See also: `inmc2`.

### Function: ichr1 (i, j, k)

Yields the Christoffel symbol of the first kind via the
definition


```maxima
(g      + g      - g     )/2 .
         ik,j     jk,i     ij,k
```


To evaluate the Christoffel symbols for a particular metric, the
variable `imetric` must be assigned a name as in the example under `chr2`.

### Function: ichr2 (i, j, k)

Yields the Christoffel symbol of the second kind
defined by the relation


```maxima
ks
   ichr2([i,j],[k]) = g    (g      + g      - g     )/2
                             is,j     js,i     ij,s
```

### Variable: icounter

Default value: `1`


Determines the numerical suffix to be used in
generating the next dummy index in the tensor package.  The prefix is
determined by the option `idummy` (default: `%`).

See also: `idummy`.

### Function: icurvature (i, j, k, h)

Yields the Riemann
curvature tensor in terms of the Christoffel symbols of the second
kind (`ichr2`).  The following notation is used:


```maxima
h             h            h         %1         h
  icurvature     = - ichr2      - ichr2     ichr2    + ichr2
            i j k         i k,j        %1 j      i k        i j,k
                            h          %1
                     + ichr2      ichr2
                            %1 k       i j
```

### Function: idiff (expr, v_1, n_1, v_2, n_2, ...)

Indicial differentiation. Unlike `diff`, which differentiates
with respect to an independent variable, `idiff)` can be used
to differentiate with respect to a coordinate. For an indexed object,
this amounts to appending the *v_i* as derivative indices.
Subsequently, derivative indices will be sorted, unless `iframe_flag`
is set to `true`.


`idiff` can also differentiate the determinant of the metric
tensor. Thus, if `imetric` has been bound to `G` then
`idiff(determinant(g),k)` will return
`2 * determinant(g) * ichr2([%i,k],[%i])` where the dummy index `%i`
is chosen appropriately.

### Function: idim (n)

Sets the dimensions of the metric. Also initializes the antisymmetry
properties of the Levi-Civita symbols for the given dimension.

### Function: idummy ()

Increments `icounter` and returns as its value an index of the form
`%n` where n is a positive integer.  This guarantees that dummy indices
which are needed in forming expressions will not conflict with indices
already in use (see the example under `indices`).

See also: `icounter`, `indices`.

### Variable: idummyx

Default value: `%`


Is the prefix for dummy indices (see the example under `indices`).

See also: `indices`.

### Variable: ifb

The frame bracket. The contribution of the frame metric to the connection
coefficients is expressed using the frame bracket:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                  2
```


The frame bracket itself is defined in terms of the frame field and frame
metric. Two alternate methods of computation are used depending on the
value of `frame_bracket_form`. If true (the default) or if the
`itorsion_flag` is `true`:



```maxima
d      e                                      f
ifb =  ifr    ifr   (ifri      - ifri      - ifri    itr   )
   abc    b      c       a d,e       a e,d       a f    d e
```


Otherwise:



```maxima
e      d        d      e
ifb    = (ifr    ifr    - ifr    ifr   ) ifri
   abc       b      c,e      b,e    c        a d
```

### Variable: ifc1

Frame coefficient of the first kind (also known as Ricci-rotation
coefficients.) This tensor represents the contribution
of the frame metric to the connection coefficient of the first kind. Defined
as:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                   2
```

### Variable: ifc2

Frame coefficient of the second kind. This tensor represents the contribution
of the frame metric to the connection coefficient of the second kind. Defined
as a permutation of the frame bracket (`ifb`) with the appropriate
indices raised and lowered as necessary:



```maxima
c       cd
ifc2   = ifg   ifc1
    ab             abd
```

See also: `ifb`.

### Variable: ifg

The frame metric. Defaults to `kdelta`, but can be changed using
`components`.

See also: `kdelta`, `components`.

### Variable: ifgi

The inverse frame metric. Contracts with the frame metric (`ifg`)
to `kdelta`.

See also: `ifg`, `kdelta`.

### Variable: ifr

The frame field. Contracts with the inverse frame field (`ifri`) to
form the frame metric (`ifg`).

See also: `ifri`, `ifg`.

### Variable: iframe_bracket_form

Default value: `true`


Specifies how the frame bracket (`ifb`) is computed.

See also: `ifb`.

### Function: iframes ()

Since in this version of Maxima, contraction identities for `ifr` and
`ifri` are always defined, as is the frame bracket (`ifb`), this
function does nothing.

See also: `ifr`, `ifri`, `ifb`.

### Variable: ifri

The inverse frame field. Specifies the frame base (dual basis vectors). Along
with the frame metric, it forms the basis of all calculations based on
frames.

### Function: igeodesic_coords (expr, name)

Causes undifferentiated Christoffel symbols and
first derivatives of the metric tensor vanish in *expr*. The *name*
in the `igeodesic_coords` function refers to the metric *name*
(if it appears in *expr*) while the connection coefficients must be
called with the names `ichr1` and/or `ichr2`. The following example
demonstrates the verification of the cyclic identity satisfied by the Riemann
curvature tensor using the `igeodesic_coords` function.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(icurvature([r,s,t],[u]))$
             u            u         %1         u     
(%t2) - ichr2      - ichr2     ichr2    + ichr2      
             r t,s        %1 s      r t        r s,t 

                                              u         %1
                                       + ichr2     ichr2
                                              %1 t      r s
(%i3) ishow(igeodesic_coords(%,ichr2))$
                                 u            u
(%t3)                       ichr2      - ichr2
                                 r s,t        r t,s
(%i4) ishow(igeodesic_coords(icurvature([r,s,t],[u]),ichr2)+
            igeodesic_coords(icurvature([s,t,r],[u]),ichr2)+
            igeodesic_coords(icurvature([t,r,s],[u]),ichr2))$
             u            u            u            u
(%t4) - ichr2      + ichr2      + ichr2      - ichr2
             t s,r        t r,s        s t,r        s r,t

                                             u            u
                                      - ichr2      + ichr2
                                             r t,s        r s,t
(%i5) canform(%);
(%o5)                                  0
```

See also: `igeodesic_coords`.

### Variable: igeowedge_flag

Default value: `false`


Controls the behavior of the wedge product and exterior derivative. When
set to `false` (the default), the notion of differential forms will
correspond with that of a totally antisymmetric covariant tensor field.
When set to `true`, differential forms will agree with the notion
of the volume element.

### Variable: ikt1

Covariant permutation of the torsion tensor (also known as contorsion).
Defined as:



```maxima
d           d       d
          -g   itr  - g    itr   - itr   g
            ad    cb    bd    ca      ab  cd
ikt1    = ----------------------------------
    abc                   2
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

See also: `ifg`.

### Variable: ikt2

Contravariant permutation of the torsion tensor (also known as contorsion).
Defined as:



```maxima
c     cd
ikt2   = g   ikt1
    ab           abd
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

See also: `ifg`.

### Function: imetric (g)

Specifies the metric by assigning the variable `imetric:g` in
addition, the con­trac­tion properties of the metric *g* are set up by
executing the commands `defcon(g), defcon(g, g, kdelta)`.
The variable `imetric` (unbound by default), is bound to the metric, assigned by
the `imetric(g)` command.

### Function: indexed_tensor (tensor)

Must be executed before assigning components to a *tensor* for which
a built in value already exists as with `ichr1`, `ichr2`,
`icurvature`. See the example under `icurvature`.

See also: `icurvature`.

### Function: indices (expr)

Returns a list of two elements.  The first is a list of the free
indices in *expr* (those that occur only once). The second is the
list of the dummy indices in *expr* (those that occur exactly twice)
as the following example demonstrates.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i,j],[k,l],m,n)*b([k,o],[j,m,p],q,r))$
                                k l      j m p
(%t2)                          a        b
                                i j,m n  k o,q r
(%i3) indices(%);
(%o3)                 [[l, p, i, n, o, q, r], [k, j, m]]
```


A tensor product containing the same index more than twice is syntactically
illegal. `indices` attempts to deal with these expressions in a
reasonable manner; however, when it is called to operate upon such an
illegal expression, its behavior should be considered undefined.

### Function: init_atensor (init_atensor, alg_type, opt_dims, init_atensor, alg_type)

Initializes the `atensor` package with the specified algebra type. *alg_type*
can be one of the following:


`universal`: The universal algebra has no commutation rules.


`grassmann`: The Grassman algebra is defined by the commutation
relation `u.v+v.u=0`.


`clifford`: The Clifford algebra is defined by the commutation
relation `u.v+v.u=-2*sf(u,v)` where `sf` is a symmetric
scalar-valued function. For this algebra, *opt_dims* can be up
to three nonnegative integers, representing the number of positive,
degenerate, and negative dimensions of the algebra, respectively. If
any *opt_dims* values are supplied, `atensor` will configure the
values of `adim` and `aform` appropriately. Otherwise,
`adim` will default to 0 and `aform` will not be defined.


`symmetric`: The symmetric algebra is defined by the commutation
relation `u.v-v.u=0`.


`symplectic`: The symplectic algebra is defined by the commutation
relation `u.v-v.u=2*af(u,v)` where `af` is an antisymmetric
scalar-valued function. For the symplectic algebra, *opt_dims* can
be up to two nonnegative integers, representing the nondegenerate and
degenerate dimensions, respectively. If any *opt_dims* values are
supplied, `atensor` will configure the values of `adim` and `aform`
appropriately. Otherwise, `adim` will default to 0 and `aform`
will not be defined.


`lie_envelop`: The algebra of the Lie envelope is defined by the
commutation relation `u.v-v.u=2*av(u,v)` where `av` is
an antisymmetric function.


The `init_atensor` function also recognizes several predefined
algebra types:


`complex` implements the algebra of complex numbers as the
Clifford algebra Cl(0,1). The call `init_atensor(complex)` is
equivalent to `init_atensor(clifford,0,0,1)`.


`quaternion` implements the algebra of quaternions. The call
`init_atensor (quaternion)` is equivalent to
`init_atensor (clifford,0,0,2)`.


`pauli` implements the algebra of Pauli-spinors as the Clifford-algebra
Cl(3,0). A call to `init_atensor(pauli)` is equivalent to
`init_atensor(clifford,3)`.


`dirac` implements the algebra of Dirac-spinors as the Clifford-algebra
Cl(3,1). A call to `init_atensor(dirac)` is equivalent to
`init_atensor(clifford,3,0,1)`.

### Function: init_cartan (x_1, ..., x_m)

Initializes some global variables for the package. The argument, a
Maxima list, is an ordered list of coordinates. The coordinate list is
stored as the value of the variable `cartan_coords`. The value of
the variable `cartan_basis` is a list of the basis 1-forms. The
dimension is stored as the value of the variable `cartan_dim`.

### Function: init_ctensor ()

Initializes the `ctensor` package.


The `init_ctensor` function reinitializes the `ctensor` package. It removes all arrays and matrices used by `ctensor`, resets all flags, resets `dim` to 4, and resets the frame metric to the Lorentz-frame.

### Variable: inm

The nonmetricity vector. Conformal nonmetricity is defined through the
covariant derivative of the metric tensor. Normally zero, the metric
tensor’s covariant derivative will evaluate to the following when
`inonmet_flag` is set to `true`:



```maxima
g     =- g  inm
 ij;k     ij   k
```

### Variable: inmc1

Covariant permutation of the nonmetricity vector components. Defined as



```maxima
g   inm  - inm  g   - g   inm
            ab    c      a  bc    ac    b
inmc1    = ------------------------------
     abc                 2
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

See also: `ifg`.

### Variable: inmc2

Contravariant permutation of the nonmetricity vector components. Used
in the connection coefficients if `inonmet_flag` is `true`. Defined
as:



```maxima
c         c         cd
          -inm  kdelta  - kdelta  inm  + g   inm  g
     c        a       b         a    b          d  ab
inmc2   = -------------------------------------------
     ab                        2
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

See also: `ifg`.

### Function: invariant1 ()

generates the mixed Euler- Lagrange tensor (field equations) for the
invariant density of R^2. The field equations are the components of an
array named `inv1`.

### Function: invariant2 ()

*** NOT YET IMPLEMENTED ***


generates the mixed Euler- Lagrange tensor (field equations) for the
invariant density of `ric[i,j]*uriem[i,j]`. The field equations are the
components of an array named `inv2`.

### Function: ishow (expr)

displays *expr* with the indexed objects in it shown having their
covariant indices as subscripts and contravariant indices as
superscripts. The derivative indices are displayed as subscripts,
separated from the covariant indices by a comma (see the examples
throughout this document).

### Variable: itr

The torsion tensor. For a metric with torsion, repeated covariant
differentiation on a scalar function will not commute, as demonstrated
by the following example:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric:g;
(%o2)                                  g
(%i3) covdiff( covdiff( f( [], []), i), j)
                      - covdiff( covdiff( f( [], []), j), i)$
(%i4) ishow(%)$
                                   %4              %2
(%t4)                    f    ichr2    - f    ichr2
                          ,%4      j i    ,%2      i j
(%i5) canform(%);
(%o5)                                  0
(%i6) itorsion_flag:true;
(%o6)                                true
(%i7) covdiff( covdiff( f( [], []), i), j)
                      - covdiff( covdiff( f( [], []), j), i)$
(%i8) ishow(%)$
                           %8             %6
(%t8)             f    icc2    - f    icc2    - f     + f
                   ,%8     j i    ,%6     i j    ,j i    ,i j
(%i9) ishow(canform(%))$
                                   %1             %1
(%t9)                     f    icc2    - f    icc2
                           ,%1     j i    ,%1     i j
(%i10) ishow(canform(ev(%,icc2)))$
                                   %1             %1
(%t10)                    f    ikt2    - f    ikt2
                           ,%1     i j    ,%1     j i
(%i11) ishow(canform(ev(%,ikt2)))$
                      %2 %1                    %2 %1
(%t11)          f    g      ikt1       - f    g      ikt1
                 ,%2            i j %1    ,%2            j i %1
(%i12) ishow(factor(canform(rename(expand(ev(%,ikt1))))))$
                           %3 %2            %1       %1
                     f    g      g      (itr    - itr   )
                      ,%3         %2 %1     j i      i j
(%t12)               ------------------------------------
                                      2
(%i13) decsym(itr,2,1,[anti(all)],[]);
(%o13)                               done
(%i14) defcon(g,g,kdelta);
(%o14)                               done
(%i15) subst(g,nounify(g),%th(3))$
(%i16) ishow(canform(contract(%)))$
                                           %1
(%t16)                           - f    itr
                                    ,%1    i j
```

### Function: kdels (L1, L2)

Symmetrized Kronecker delta, used in some calculations. For instance:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) kdelta([1,2],[2,1]);
(%o2)                                 - 1
(%i3) kdels([1,2],[2,1]);
(%o3)                                  1
(%i4) ishow(kdelta([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  - kdelta  kdelta
                             a       b         a       b
(%i4) ishow(kdels([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  + kdelta  kdelta
                             a       b         a       b
```

### Function: kdelta (L1, L2)

is the generalized Kronecker delta function defined in
the `itensor` package with *L1* the list of covariant indices and *L2*
the list of contravariant indices.  `kdelta([i],[j])` returns the ordinary
Kronecker delta.  The command `ev(expr,kdelta)` causes the evaluation of
an expression containing `kdelta([],[])` to the dimension of the
manifold.


In what amounts to an abuse of this notation, `itensor` also allows
`kdelta` to have 2 covariant and no contravariant, or 2 contravariant
and no covariant indices, in effect providing a co(ntra)variant "unit matrix"
capability. This is strictly considered a programming aid and not meant to
imply that `kdelta([i,j],[])` is a valid tensorial object.

### Variable: kinvariant

The Kretschmann invariant. Computed by `rinvariant`.

### Variable: kt

The contortion tensor, computed from `tr` by `contortion`.

### Function: lc2kdt (expr)

Simplifies expressions containing the Levi-Civita symbol, converting these
to Kronecker-delta expressions when possible. The main difference between
this function and simply evaluating the Levi-Civita symbol is that direct
evaluation often results in Kronecker expressions containing numerical
indices. This is often undesirable as it prevents further simplification.
The `lc2kdt` function avoids this problem, yielding expressions that
are more easily simplified with `rename` or `contract`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([k,l],[])*a([j],[k]))$
                                  i j  k
(%t2)                  levi_civita    a  levi_civita
                                       j            k l
(%i3) ishow(ev(expr,levi_civita))$
                                  i j  k       1 2
(%t3)                       kdelta    a  kdelta
                                  1 2  j       k l
(%i4) ishow(ev(%,kdelta))$
             i       j         j       i   k
(%t4) (kdelta  kdelta  - kdelta  kdelta ) a
             1       2         1       2   j

                               1       2         2       1
                        (kdelta  kdelta  - kdelta  kdelta )
                               k       l         k       l
(%i5) ishow(lc2kdt(expr))$
                     k       i       j    k       j       i
(%t5)               a  kdelta  kdelta  - a  kdelta  kdelta
                     j       k       l    j       k       l
(%i6) ishow(contract(expand(%)))$
                                 i           i
(%t6)                           a  - a kdelta
                                 l           l
```


The `lc2kdt` function sometimes makes use of the metric tensor.
If the metric tensor was not defined previously with `imetric`,
this results in an error.



```maxima
(%i7) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([],[k,l])*a([j,k],[]))$

                                 i j            k l
(%t7)                 levi_civita    levi_civita    a
                                                     j k

(%i8) ishow(lc2kdt(expr))$
Maxima encountered a Lisp error:

 Error in $IMETRIC [or a callee]:
 $IMETRIC [or a callee] requires less than two arguments.

Automatically continuing.
To re-enable the Lisp debugger set *debugger-hook* to nil.
(%i9) imetric(g);
(%o9)                                done
(%i10) ishow(lc2kdt(expr))$
         %3 i       k   %4 j       l     %3 i       l   %4 j
(%t10) (g     kdelta   g     kdelta   - g     kdelta   g    
                    %3             %4               %3
              k
        kdelta  ) a
              %4   j k
(%i11) ishow(contract(expand(%)))$
                                  l i    l i  j
(%t11)                           a    - g    a
                                              j
```

See also: `rename`, `contract`, `imetric`.

### Function: lc_l ()

Simplification rule used for expressions containing the unevaluated Levi-Civita
symbol (`levi_civita`). Along with `lc_u`, it can be used to simplify
many expressions more efficiently than the evaluation of `levi_civita`.
For example:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) el1:ishow('levi_civita([i,j,k],[])*a([],[i])*a([],[j]))$
                             i  j
(%t2)                       a  a  levi_civita
                                             i j k
(%i3) el2:ishow('levi_civita([],[i,j,k])*a([i])*a([j]))$
                                       i j k
(%t3)                       levi_civita      a  a
                                              i  j
(%i4) canform(contract(expand(applyb1(el1,lc_l,lc_u))));
(%t4)                                  0
(%i5) canform(contract(expand(applyb1(el2,lc_l,lc_u))));
(%t5)                                  0
```

See also: `levi_civita`, `lc_u`.

### Function: lc_u ()

Simplification rule used for expressions containing the unevaluated Levi-Civita
symbol (`levi_civita`). Along with `lc_u`, it can be used to simplify
many expressions more efficiently than the evaluation of `levi_civita`.
For details, see `lc_l`.

See also: `levi_civita`, `lc_l`.

### Function: leinstein (dis)

Covariant Einstein-tensor. `leinstein` stores the values of the covariant Einstein tensor in the array `lein`. The covariant Einstein-tensor is computed from the mixed Einstein tensor `ein` by multiplying it with the metric tensor. If the argument *dis* is `true`, then the non-zero values of the covariant Einstein tensor are displayed.

### Function: levi_civita (L)

is the permutation (or Levi-Civita) tensor which yields 1 if
the list *L* consists of an even permutation of integers, -1 if it
consists of an odd permutation, and 0 if some indices in *L* are
repeated.

### Variable: lfg

The covariant frame metric. By default, it is initialized to the 4-dimensional Lorentz frame with signature (+,+,+,-). Used when `cframe_flag` is `true`.

### Variable: lg

The metric tensor. This tensor must be specified (as a `dim` by `dim` matrix)
before other computations can be performed.

### Function: lie_diff (vector1, vector2, form)

The Lie derivative operator. The first argument is a vector field. The
second argument may be either a vector field or a differential form.

### Function: liediff (v, ten)

Computes the Lie-derivative of the tensorial expression *ten* with
respect to the vector field *v*. *ten* should be any indexed
tensor expression; *v* should be the name (without indices) of a vector
field. For example:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(liediff(v,a([i,j],[])*b([],[k],l)))$
       k    %2            %2          %2
(%t2) b   (v   a       + v   a     + v   a    )
       ,l       i j,%2    ,j  i %2    ,i  %2 j

                          %1  k        %1  k      %1  k
                      + (v   b      - b   v    + v   b   ) a
                              ,%1 l    ,l  ,%1    ,l  ,%1   i j
```

### Function: list_nc_monomials (list_nc_monomials, p_1, ..., p_n, list_nc_monomials, p)

Returns a list of the non commutative monomials occurring in a polynomial *p*
or a list of polynomials *p_1*, ..., *p_n*.


`load("affine")` loads this function.

### Function: listoftens ()

Lists all tensors in a tensorial expression, complete with their indices. E.g.,



```maxima
(%i6) ishow(a([i,j],[k])*b([u],[],v)+c([x,y],[])*d([],[])*e)$
                                         k
(%t6)                        d e c    + a    b
                                  x y    i j  u,v
(%i7) ishow(listoftens(%))$
                               k
(%t7)                        [a   , b   , c   , d]
                               i j   u,v   x y
```

### Function: lorentz_gauge (expr)

Imposes the Lorentz condition by substituting 0 for all
indexed objects in *expr* that have a derivative index identical to a
contravariant index.

### Variable: lriem

The covariant Riemann tensor. Computed by `lriemann`.

### Function: lriemann (dis)

Covariant Riemann-tensor (`lriem[]`).


Computes the covariant Riemann-tensor as the array `lriem`. If the
argument *dis* is `true`, unique non-zero values are displayed.


If the variable `cframe_flag` is `true`, the covariant Riemann
tensor is computed directly from the frame field coefficients. Otherwise,
the (3,1) Riemann tensor is computed first.


For information on index ordering, see `riemann`.

### Function: makebox (expr, g)

Display *expr* using the metric *g* such that
any tensor d’Alembertian occurring in *expr* will be indicated using the
symbol `[]`.  For example, `[]p([m],[n])` represents
`g([],[i,j])*p([m],[n],i,j)`.

### Function: mono (x_1, ..., x_n, n)

Returns the list of independent
monomials relative to the current dot simplifications of degree *n*
in the variables *x_1*, ..., *x_n*.


`load("affine")` loads this function.

### Function: monomial_dimensions (n)

Compute the Hilbert series through degree *n* for the current algebra.


`load("affine")` loads this function.

### Function: nc_degree (p)

Returns the degree of a noncommutative polynomial *p*.  See `declare_weights`.


`load("affine")` loads this function.

### Variable: nm

User-supplied nonmetricity vector. Used by `nonmetricity`.

### Variable: nmc

The nonmetricity coefficients, computed from `nm` by `nonmetricity`.

### Function: nonmetricity (nm)

Computes the (2,1) nonmetricity coefficients from the nonmetricity
vector *nm*.

### Variable: np

A Newman-Penrose null tetrad. Computed by `nptetrad`.

### Variable: npi

The raised-index Newman-Penrose null tetrad. Computed by `nptetrad`.
Defined as `ug.np`. The product `np.transpose(npi)` is constant:



```maxima
(%i39) trigsimp(np.transpose(npi));
                              [  0   - 1  0  0 ]
                              [                ]
                              [ - 1   0   0  0 ]
(%o39)                        [                ]
                              [  0    0   0  1 ]
                              [                ]
                              [  0    0   1  0 ]
```

### Function: nptetrad ()

Computes a Newman-Penrose null tetrad (`np`) and its raised-index
counterpart (`npi`). See `petrov` for an example.


The null tetrad is constructed on the assumption that a four-dimensional
orthonormal frame metric with metric signature (-,+,+,+) is being used.
The components of the null tetrad are related to the inverse frame matrix
as follows:



```maxima
np  = (fri  + fri ) / sqrt(2)
  1       1      2

np  = (fri  - fri ) / sqrt(2)
  2       1      2

np  = (fri  + %i fri ) / sqrt(2)
  3       3         4

np  = (fri  - %i fri ) / sqrt(2)
  4       3         4
```

### Function: ntermst (f)

gives the user a quick picture of the "size" of the doubly subscripted
tensor (array) *f*.  It prints two element lists where the second
element corresponds to NTERMS of the components specified by the first
elements.  In this way, it is possible to quickly find the non-zero
expressions and attempt simplification.

### Function: petrov ()

Computes the Petrov classification of the metric characterized by `psi[0]`...`psi[4]`.


For example, the following demonstrates how to obtain the Petrov-classification
of the Kerr metric:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) (cframe_flag:true,gcd:spmod,ctrgsimp:true,ratfac:true);
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) ug:invert(lg)$
(%i5) weyl(false);
(%o5)                                done
(%i6) nptetrad(true);
(%t6) np =

[ sqrt(r - 2 m)           sqrt(r)                                 ]
[---------------   ---------------------    0            0        ]
[sqrt(2) sqrt(r)   sqrt(2) sqrt(r - 2 m)                          ]
[                                                                 ]
[ sqrt(r - 2 m)            sqrt(r)                                ]
[---------------  - ---------------------   0            0        ]
[sqrt(2) sqrt(r)    sqrt(2) sqrt(r - 2 m)                         ]
[                                                                 ]
[                                          r      %i r sin(theta) ]
[       0                    0          -------   --------------- ]
[                                       sqrt(2)       sqrt(2)     ]
[                                                                 ]
[                                          r       %i r sin(theta)]
[       0                    0          -------  - ---------------]
[                                       sqrt(2)        sqrt(2)    ]

                             sqrt(r)         sqrt(r - 2 m)
(%t7) npi = matrix([- ---------------------,---------------, 0, 0],
                      sqrt(2) sqrt(r - 2 m) sqrt(2) sqrt(r)

          sqrt(r)            sqrt(r - 2 m)
[- ---------------------, - ---------------, 0, 0],
   sqrt(2) sqrt(r - 2 m)    sqrt(2) sqrt(r)

           1               %i
[0, 0, ---------, --------------------],
       sqrt(2) r  sqrt(2) r sin(theta)

           1                 %i
[0, 0, ---------, - --------------------])
       sqrt(2) r    sqrt(2) r sin(theta)

(%o7)                                done
(%i7) psi(true);
(%t8)                              psi  = 0
                                      0

(%t9)                              psi  = 0
                                      1

                                          m
(%t10)                             psi  = --
                                      2    3
                                          r

(%t11)                             psi  = 0
                                      3

(%t12)                             psi  = 0
                                      4
(%o12)                               done
(%i12) petrov();
(%o12)                                 D
```


The Petrov classification function is based on the algorithm published in
"Classifying geometries in general relativity: III Classification in practice"
by Pollney, Skea, and d’Inverno, Class. Quant. Grav. 17 2885-2902 (2000).
Except for some simple test cases, the implementation is untested as of
December 19, 2004, and is likely to contain errors.

### Variable: ratchristof

Causes rational simplification to be applied by `christof`.

### Variable: rateinstein

Default value: `true`


If `true` rational simplification will be
performed on the non-zero components of Einstein tensors; if
`ratfac` is `true` then the components will also be factored.

### Variable: ratriemann

Default value: `true`


One of the switches which controls
simplification of Riemann tensors; if `true`, then rational
simplification will be done; if `ratfac` is `true` then each of the
components will also be factored.

### Variable: ratweyl

Default value: `true`


If `true`, this switch causes the `weyl` function
to apply rational simplification to the values of the Weyl tensor. If
`ratfac` is `true`, then the components will also be factored.

### Function: rediff (ten)

Evaluates all occurrences of the `idiff` command in the tensorial
expression *ten*.

See also: `idiff`.

### Function: remcomps (tensor)

Unbinds all values from *tensor* which were assigned with the
`components` function.

See also: `components`.

### Function: remcon (remcon, tensor_1, ..., tensor_n, remcon, all)

Removes all the contraction properties
from the (*tensor_1*, ..., *tensor_n*). `remcon(all)` removes all contraction
properties from all indexed objects.

### Function: remcoord (remcoord, tensor_1, tensor_2, ..., remcoord, all)

Removes the coordinate differentiation property from the `tensor_i`
that was established by the function `coord`.  `remcoord(all)`
removes this property from all indexed objects.

### Function: remsym (tensor, m, n)

Removes all symmetry properties from *tensor* which has *m*
covariant indices and *n* contravariant indices.

### Function: rename (rename, expr, rename, expr, count)

Returns an expression equivalent to *expr* but with the dummy indices
in each term chosen from the set `[%1, %2,...]`, if the optional second
argument is omitted. Otherwise, the dummy indices are indexed
beginning at the value of *count*.  Each dummy index in a product
will be different. For a sum, `rename` will operate upon each term in
the sum resetting the counter with each term. In this way `rename` can
serve as a tensorial simplifier. In addition, the indices will be
sorted alphanumerically (if `allsym` is `true`) with respect to
covariant or contravariant indices depending upon the value of `flipflag`.
If `flipflag` is `false` then the indices will be renamed according
to the order of the contravariant indices. If `flipflag` is `true`
the renaming will occur according to the order of the covariant
indices. It often happens that the combined effect of the two renamings will
reduce an expression more than either one by itself.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) allsym:true;
(%o2)                                true
(%i3) g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%4],[%3])*
ichr2([%2,%3],[u])*ichr2([%5,%6],[%1])*ichr2([%7,r],[%2])-
g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%2],[u])*
ichr2([%3,%5],[%1])*ichr2([%4,%6],[%3])*ichr2([%7,r],[%2]),noeval$
(%i4) expr:ishow(%)$

       %4 %5  %6 %7      %3         u          %1         %2
(%t4) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %4      %2 %3      %5 %6      %7 r

        %4 %5  %6 %7      u          %1         %3         %2
     - g      g      ichr2      ichr2      ichr2      ichr2
                          %1 %2      %3 %5      %4 %6      %7 r

(%i5) flipflag:true;
(%o5)                                true
(%i6) ishow(rename(expr))$
       %2 %5  %6 %7      %4         u          %1         %3
(%t6) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %2      %3 %4      %5 %6      %7 r

        %4 %5  %6 %7      u          %1         %3         %2
     - g      g      ichr2      ichr2      ichr2      ichr2
                          %1 %2      %3 %4      %5 %6      %7 r
(%i7) flipflag:false;
(%o7)                                false
(%i8) rename(%th(2));
(%o8)                                  0
(%i9) ishow(rename(expr))$
       %1 %2  %3 %4      %5         %6         %7        u
(%t9) g      g      ichr2      ichr2      ichr2     ichr2
                         %1 %6      %2 %3      %4 r      %5 %7

        %1 %2  %3 %4      %6         %5         %7        u
     - g      g      ichr2      ichr2      ichr2     ichr2
                          %1 %3      %2 %6      %4 r      %5 %7
```

See also: `allsym`, `flipflag`.

### Variable: ric

The covariant Ricci-tensor. Computed by `ricci`.

### Function: ricci (dis)

A function in the `ctensor` (component tensor)
package. `ricci` computes the covariant (symmetric)
components `ric[i,j]` of the Ricci tensor.  If the argument *dis* is `true`,
then the non-zero components are displayed.

### Variable: riem

The (3,1) Riemann tensor. Computed when the function `riemann` is invoked. For information about index ordering, see the description of `riemann`.


If `cframe_flag` is `true`, `riem` is computed from the covariant Riemann-tensor `lriem`.

### Function: riemann (dis)

A function in the `ctensor` (component tensor)
package.  `riemann` computes the Riemann curvature tensor
from the given metric and the corresponding Christoffel symbols. The following
index conventions are used:



```maxima
l      _l       _l       _l   _m    _l   _m
 R[i,j,k,l] =  R    = |      - |      + |    |   - |    |
                ijk     ij,k     ik,j     mk   ij    mj   ik
```


This notation is consistent with the notation used by the `itensor`
package and its `icurvature` function.
If the optional argument *dis* is `true`,
the unique non-zero components `riem[i,j,k,l]` will be displayed.
As with the Einstein tensor, various switches set by the user
control the simplification of the components of the Riemann tensor.
If `ratriemann` is `true`, then
rational simplification will be done. If `ratfac`
is `true` then
each of the components will also be factored.


If the variable `cframe_flag` is `false`, the Riemann tensor is
computed directly from the Christoffel-symbols. If `cframe_flag` is
`true`, the covariant Riemann-tensor is computed first from the
frame field coefficients.

### Function: rinvariant ()

Forms the Kretschmann-invariant (`kinvariant`) obtained by
contracting the tensors



```maxima
lriem[i,j,k,l]*uriem[i,j,k,l].
```


This object is not automatically simplified since it can be very large.

### Function: scurvature ()

Returns the scalar curvature (obtained by contracting
the Ricci tensor) of the Riemannian manifold with the given metric.

### Function: set_up_dot_simplifications (set_up_dot_simplifications, eqns, check_through_degree, set_up_dot_simplifications, eqns)

The *eqns* are polynomial equations in non commutative variables.
The value of `current_variables` is the
list of variables used for computing degrees.  The equations must be
homogeneous, in order for the procedure to terminate.


If you have checked overlapping simplifications in `dot_simplifications`
above the degree of *f*, then the following is true:
`dotsimp (f)` yields 0 if and only if *f* is in the
ideal generated by the equations, i.e.,
if and only if *f* is a polynomial combination
of the elements of the equations.


The degree is that returned by `nc_degree`.   This in turn is influenced by
the weights of individual variables.


`load("affine")` loads this function.

### Function: sf (u, v)

A symmetric scalar function that is used in commutation relations.
The default implementation checks if both arguments are base vectors
using `abasep` and if that is the case, substitutes the
corresponding value from the matrix `aform`.

### Function: showcomps (tensor)

Shows component assignments of a tensor, as made using the `components`
command. This function can be particularly useful when a matrix is assigned
to an indicial tensor using `components`, as demonstrated by the
following example:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) load("itensor");
(%o2)      /share/tensor/itensor.lisp
(%i3) lg:matrix([sqrt(r/(r-2*m)),0,0,0],[0,r,0,0],
                [0,0,sin(theta)*r,0],[0,0,0,sqrt((r-2*m)/r)]);
        [         r                                     ]
        [ sqrt(-------)  0       0              0       ]
        [      r - 2 m                                  ]
        [                                               ]
        [       0        r       0              0       ]
(%o3)   [                                               ]
        [       0        0  r sin(theta)        0       ]
        [                                               ]
        [                                      r - 2 m  ]
        [       0        0       0        sqrt(-------) ]
        [                                         r     ]
(%i4) components(g([i,j],[]),lg);
(%o4)                                done
(%i5) showcomps(g([i,j],[]));
             [         r                                     ]
             [ sqrt(-------)  0       0              0       ]
             [      r - 2 m                                  ]
             [                                               ]
             [       0        r       0              0       ]
(%t5) g    = [                                               ]
       i j   [       0        0  r sin(theta)        0       ]
             [                                               ]
             [                                      r - 2 m  ]
             [       0        0       0        sqrt(-------) ]
             [                                         r     ]
(%o5)                                false
```


The `showcomps` command can also display components of a tensor of
rank higher than 2.

See also: `components`.

### Function: simpmetderiv (simpmetderiv, expr, simpmetderiv, expr, stop)

Simplifies expressions containing products of the derivatives of the
metric tensor. Specifically, `simpmetderiv` recognizes two identities:



```maxima
ab        ab           ab                 a
  g   g   + g   g     = (g   g  )   = (kdelta )   = 0
   ,d  bc        bc,d         bc ,d          c ,d
```


hence



```maxima
ab          ab
  g   g   = - g   g
   ,d  bc          bc,d
```


and



```maxima
ab          ab
 g   g     = g   g
  ,j  ab,i    ,i  ab,j
```


which follows from the symmetries of the Christoffel symbols.


The `simpmetderiv` function takes one optional parameter which, when
present, causes the function to stop after the first successful
substitution in a product expression. The `simpmetderiv` function
also makes use of the global variable `flipflag` which determines
how to apply a “canonical” ordering to the product indices.


Put together, these capabilities can be used to achieve powerful
simplifications that are difficult or impossible to accomplish otherwise.
This is demonstrated through the following example that explicitly uses the
partial simplification features of `simpmetderiv` to obtain a
contractible expression:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                                done
(%i3) ishow(g([],[a,b])*g([],[b,c])*g([a,b],[],d)*g([b,c],[],e))$
                             a b  b c
(%t3)                       g    g    g      g
                                       a b,d  b c,e
(%i4) ishow(canform(%))$

errexp1 has improper indices
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) ishow(simpmetderiv(%))$
                             a b  b c
(%t5)                       g    g    g      g
                                       a b,d  b c,e
(%i6) flipflag:not flipflag;
(%o6)                                true
(%i7) ishow(simpmetderiv(%th(2)))$
                               a b  b c
(%t7)                         g    g    g    g
                               ,d   ,e   a b  b c
(%i8) flipflag:not flipflag;
(%o8)                                false
(%i9) ishow(simpmetderiv(%th(2),stop))$
                               a b  b c
(%t9)                       - g    g    g      g
                                    ,e   a b,d  b c
(%i10) ishow(contract(%))$
                                    b c
(%t10)                           - g    g
                                    ,e   c b,d
```


See also `weyl.dem` for an example that uses `simpmetderiv`
and `conmetderiv` together to simplify contractions of the Weyl tensor.

See also: `flipflag`, `simpmetderiv`, `conmetderiv`.

### Function: symmetricp (M, n)

Returns `true` if *M* is a *n* by *n* symmetric matrix or two-dimensional array,
otherwise `false`.


If *n* is less than the size of *M*,
`symmetricp` considers only the *n* by *n* submatrix (respectively, subarray)
comprising rows 1 through *n* and columns 1 through *n*.

### Variable: tensorkill

Variable indicating if the tensor package has been initialized. Set and used by
`csetup`, reset by `init_ctensor`.

### Function: tentex (expr)

To use the `tentex` function, you must first load `tentex`,
as in the following example:










```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) load("tentex");
(%o2)       /share/tensor/tentex.lisp
(%i3) idummyx:m;
(%o3)                                  m
(%i4) ishow(icurvature([j,k,l],[i]))$
            m1       i           m1       i           i
(%t4)  ichr2    ichr2     - ichr2    ichr2     - ichr2
            j k      m1 l        j l      m1 k        j l,k

                                                      i
                                               + ichr2
                                                      j k,l
(%i5) tentex(%)$
$$\Gamma_{j\,k}^{m_1}\,\Gamma_{l\,m_1}^{i}-\Gamma_{j\,l}^{m_1}\,
 \Gamma_{k\,m_1}^{i}-\Gamma_{j\,l,k}^{i}+\Gamma_{j\,k,l}^{i}$$
```


Note the use of the `idummyx` assignment, to avoid the appearance
of the percent sign in the TeX expression, which may lead to compile errors.


NB: This version of the `tentex` function is somewhat experimental.

### Variable: tr

User-supplied rank-3 tensor representing torsion. Used by `contortion`.

### Variable: ufg

The inverse frame metric. Computed from `lfg` when `cmetric` is called while `cframe_flag` is set to `true`.

### Variable: ug

The inverse of the metric tensor. Computed by `cmetric`.

### Function: undiff (expr)

Returns an expression equivalent to *expr* but with all derivatives
of indexed objects replaced by the noun form of the `idiff` function. Its
arguments would yield that indexed object if the differentiation were
carried out.  This is useful when it is desired to replace a
differentiated indexed object with some function definition resulting
in *expr* and then carry out the differentiation by saying
`ev(expr, idiff)`.

See also: `idiff`.

### Variable: uric

The mixed-index Ricci-tensor. Computed by `uricci`.

### Function: uricci (dis)

This function first computes the
covariant components `ric[i,j]` of the Ricci tensor.
Then the mixed Ricci tensor is computed using the
contravariant metric tensor.  If the value of the argument *dis*
is `true`, then these mixed components, `uric[i,j]` (the
index `i` is covariant and the index `j` is contravariant), will be displayed
directly.  Otherwise, `ricci(false)` will simply compute the entries
of the array `uric[i,j]` without displaying the results.

### Variable: uriem

The contravariant Riemann tensor. Computed by `uriemann`.

### Function: uriemann (dis)

Computes the contravariant components of the Riemann
curvature tensor as array elements `uriem[i,j,k,l]`.  These are displayed
if *dis* is `true`.

### Function: weyl (dis)

Computes the Weyl conformal tensor.  If the argument *dis* is
`true`, the non-zero components `weyl[i,j,k,l]` will be displayed to the
user.  Otherwise, these components will simply be computed and stored.
If the switch `ratweyl` is set to `true`, then the components will be
rationally simplified; if `ratfac` is `true` then the results will be
factored as well.

### Function: | ()

The bar “|” is an infix operator which defines the contraction of a
vector on a form. The vector should be given on the left.

### Function: ~ ()

The tilde “~” is an infix operator which denotes the exterior (wedge)
product. The canonical ordering of the products is determined by the
order in which the coordinates were specified. For example, if the
coordinate list is specified as `[x,y,z]`, then the two-form
`dy~dx` simplifies to `-dx~dy`.

