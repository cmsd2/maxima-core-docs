## atensor

<!-- category: Tensors -->
<!-- keywords: abasep -->
<!-- signatures: abasep(v) -->
### Function: abasep (v)

Checks if its argument is an `atensor` base vector. That is, if it is
an indexed symbol, with the symbol being the same as the value of
`asymbol`, and the index having a numeric value between 1
and `adim`.

<!-- category: Tensors -->
<!-- keywords: adim -->
<!-- signatures: adim -->
### Variable: adim

Default value: 0


The dimensionality of the algebra. `atensor` uses the value of `adim`
to determine if an indexed object is a valid base vector.  See `abasep`.

<!-- category: Tensors -->
<!-- keywords: af -->
<!-- signatures: af(u, v) -->
### Function: af (u, v)

An antisymmetric scalar function that is used in commutation relations.
The default implementation checks if both arguments are base vectors
using `abasep` and if that is the case, substitutes the
corresponding value from the matrix `aform`.

<!-- category: Tensors -->
<!-- keywords: aform -->
<!-- signatures: aform -->
### Variable: aform

Default value: `ident(3)`


Default values for the bilinear forms `sf`, `af`, and
`av`. The default is the identity matrix `ident(3)`.

<!-- category: Tensors -->
<!-- keywords: alg_type -->
<!-- signatures: alg_type -->
### Function: alg_type

The algebra type. Valid values are `universal`, `grassmann`,
`clifford`, `symmetric`, `symplectic` and `lie_envelop`.

<!-- category: Tensors -->
<!-- keywords: asymbol -->
<!-- signatures: asymbol -->
### Variable: asymbol

Default value: `v`


The symbol for base vectors.

<!-- category: Tensors -->
<!-- keywords: atensimp -->
<!-- signatures: atensimp(expr) -->
### Function: atensimp (expr)

Simplifies an algebraic tensor expression *expr* according to the rules
configured by a call to `init_atensor`. Simplification includes
recursive application of commutation relations and resolving calls
to `sf`, `af`, and `av` where applicable. A
safeguard is used to ensure that the function always terminates, even
for complex expressions.

<!-- category: Tensors -->
<!-- keywords: av -->
<!-- signatures: av(u, v) -->
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

<!-- category: Tensors -->
<!-- keywords: init_atensor -->
<!-- signatures: init_atensor(alg_type, opt_dims), init_atensor(alg_type) -->
### Function: init_atensor (alg_type, opt_dims)

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

<!-- category: Tensors -->
<!-- keywords: sf -->
<!-- signatures: sf(u, v) -->
### Function: sf (u, v)

A symmetric scalar function that is used in commutation relations.
The default implementation checks if both arguments are base vectors
using `abasep` and if that is the case, substitutes the
corresponding value from the matrix `aform`.

