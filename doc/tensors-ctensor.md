## ctensor

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

### Function: contortion (tr)

Computes the (2,1) contortion coefficients from the torsion tensor *tr*.

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

### Function: init_ctensor ()

Initializes the `ctensor` package.


The `init_ctensor` function reinitializes the `ctensor` package. It removes all arrays and matrices used by `ctensor`, resets all flags, resets `dim` to 4, and resets the frame metric to the Lorentz-frame.

### Function: invariant1 ()

generates the mixed Euler- Lagrange tensor (field equations) for the
invariant density of R^2. The field equations are the components of an
array named `inv1`.

### Function: invariant2 ()

*** NOT YET IMPLEMENTED ***


generates the mixed Euler- Lagrange tensor (field equations) for the
invariant density of `ric[i,j]*uriem[i,j]`. The field equations are the
components of an array named `inv2`.

### Variable: kinvariant

The Kretschmann invariant. Computed by `rinvariant`.

### Variable: kt

The contortion tensor, computed from `tr` by `contortion`.

### Function: leinstein (dis)

Covariant Einstein-tensor. `leinstein` stores the values of the covariant Einstein tensor in the array `lein`. The covariant Einstein-tensor is computed from the mixed Einstein tensor `ein` by multiplying it with the metric tensor. If the argument *dis* is `true`, then the non-zero values of the covariant Einstein tensor are displayed.

### Variable: lfg

The covariant frame metric. By default, it is initialized to the 4-dimensional Lorentz frame with signature (+,+,+,-). Used when `cframe_flag` is `true`.

### Variable: lg

The metric tensor. This tensor must be specified (as a `dim` by `dim` matrix)
before other computations can be performed.

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

### Function: symmetricp (M, n)

Returns `true` if *M* is a *n* by *n* symmetric matrix or two-dimensional array,
otherwise `false`.


If *n* is less than the size of *M*,
`symmetricp` considers only the *n* by *n* submatrix (respectively, subarray)
comprising rows 1 through *n* and columns 1 through *n*.

### Variable: tensorkill

Variable indicating if the tensor package has been initialized. Set and used by
`csetup`, reset by `init_ctensor`.

### Variable: tr

User-supplied rank-3 tensor representing torsion. Used by `contortion`.

### Variable: ufg

The inverse frame metric. Computed from `lfg` when `cmetric` is called while `cframe_flag` is set to `true`.

### Variable: ug

The inverse of the metric tensor. Computed by `cmetric`.

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

