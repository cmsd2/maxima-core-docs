## cartan

### Function: ext_diff (form)

The exterior derivative operator. It takes one argument, which should be a differential form.

### Function: init_cartan (x_1, ..., x_m)

Initializes some global variables for the package. The argument, a
Maxima list, is an ordered list of coordinates. The coordinate list is
stored as the value of the variable `cartan_coords`. The value of
the variable `cartan_basis` is a list of the basis 1-forms. The
dimension is stored as the value of the variable `cartan_dim`.

### Function: lie_diff (vector1, vector2, form)

The Lie derivative operator. The first argument is a vector field. The
second argument may be either a vector field or a differential form.

### Function: | ()

The bar “|” is an infix operator which defines the contraction of a
vector on a form. The vector should be given on the left.

### Function: ~ ()

The tilde “~” is an infix operator which denotes the exterior (wedge)
product. The canonical ordering of the products is determined by the
order in which the coordinates were specified. For example, if the
coordinate list is specified as `[x,y,z]`, then the two-form
`dy~dx` simplifies to `-dx~dy`.

