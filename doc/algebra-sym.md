## sym

### Function: comp2pui (n, L)

implements passing from the complete symmetric functions given in the list
*L* to the elementary symmetric functions from 0 to *n*. If the
list *L* contains fewer than *n+1* elements, it will be completed with
formal values of the type *h1*, *h2*, etc. If the first element
of the list *L* exists, it specifies the size of the alphabet,
otherwise the size is set to *n*.





```maxima
(%i1) comp2pui (3, [4, g]);
                        2                    2
(%o1)    [4, g, 2 h2 - g , 3 h3 - g h2 + g (g  - 2 h2)]
```

### Function: cont2part (pc, lvar)

returns the partitioned polynomial associated to the contracted form
*pc* whose variables are in *lvar*.






```maxima
(%i1) pc: 2*a^3*b*x^4*y + x^5;
                           3    4      5
(%o1)                   2 a  b x  y + x


(%i2) cont2part (pc, [x, y]);
                                   3
(%o2)              [[1, 5, 0], [2 a  b, 4, 1]]
```

### Function: direct (p_1, ..., p_n, y, f, lvar_1, ..., lvar_n)

calculates the direct image (see M. Giusti, D. Lazard et A. Valibouze,
ISSAC 1988, Rome) associated to the function *f*, in the lists of
variables *lvar_1*, ..., *lvar_n*, and in the polynomials
*p_1*, ..., *p_n* in a variable *y*.  The arity of the
function *f* is important for the calculation.  Thus, if the
expression for *f* does not depend on some variable, it is useless
to include this variable, and not including it will also considerably
reduce the amount of computation.









```maxima
(%i1) direct ([z^2  - e1* z + e2, z^2  - f1* z + f2],
              z, b*v + a*u, [[u, v], [a, b]]);
       2
(%o1) y  - e1 f1 y

                                 2            2             2   2
                  - 4 e2 f2 - (e1  - 2 e2) (f1  - 2 f2) + e1  f1
                + -----------------------------------------------
                                         2


(%i2) ratsimp (%);
              2                2                   2
(%o2)        y  - e1 f1 y + (e1  - 4 e2) f2 + e2 f1


(%i3) ratsimp (direct ([z^3-e1*z^2+e2*z-e3,z^2  - f1* z + f2],
              z, b*v + a*u, [[u, v], [a, b]]));
       6            5         2                        2    2   4
(%o3) y  - 2 e1 f1 y  + ((2 e1  - 6 e2) f2 + (2 e2 + e1 ) f1 ) y

                          3                               3   3
 + ((9 e3 + 5 e1 e2 - 2 e1 ) f1 f2 + (- 2 e3 - 2 e1 e2) f1 ) y

         2       2        4    2
 + ((9 e2  - 6 e1  e2 + e1 ) f2

                    2       2       2                   2    4
 + (- 9 e1 e3 - 6 e2  + 3 e1  e2) f1  f2 + (2 e1 e3 + e2 ) f1 )

  2          2                      2     3          2
 y  + (((9 e1  - 27 e2) e3 + 3 e1 e2  - e1  e2) f1 f2

                 2            2    3                5
 + ((15 e2 - 2 e1 ) e3 - e1 e2 ) f1  f2 - 2 e2 e3 f1 ) y

           2                   3           3     2   2    3
 + (- 27 e3  + (18 e1 e2 - 4 e1 ) e3 - 4 e2  + e1  e2 ) f2

         2      3                   3    2   2
 + (27 e3  + (e1  - 9 e1 e2) e3 + e2 ) f1  f2

                   2    4        2   6
 + (e1 e2 e3 - 9 e3 ) f1  f2 + e3  f1
```


Finding the polynomial whose roots are the sums $a+u$ where $a$
is a root of $z^2 - e_1 z + e_2$ and $u$ is a root of $z^2 - f_1 z + f_2$.






```maxima
(%i1) ratsimp (direct ([z^2 - e1* z + e2, z^2 - f1* z + f2],
                          z, a + u, [[u], [a]]));
       4                    3             2
(%o1) y  + (- 2 f1 - 2 e1) y  + (2 f2 + f1  + 3 e1 f1 + 2 e2

     2   2                              2               2
 + e1 ) y  + ((- 2 f1 - 2 e1) f2 - e1 f1  + (- 2 e2 - e1 ) f1

                  2                     2            2
 - 2 e1 e2) y + f2  + (e1 f1 - 2 e2 + e1 ) f2 + e2 f1  + e1 e2 f1

     2
 + e2
```


`direct` accepts two flags: `elementaires` and
`puissances` (default) which allow decomposing the symmetric
polynomials appearing in the calculation into elementary symmetric
functions, or power functions, respectively.


Functions of `sym` used in this function:


`multi_orbit` (so `orbit`), `pui_direct`, `multi_elem`
(so `elem`), `multi_pui` (so `pui`), `pui2ele`, `ele2pui`
(if the flag `direct` is in `puissances`).

### Function: ele2comp (m, L)

Goes from the elementary symmetric functions to the compete functions.
Similar to `comp2ele` and `comp2pui`.


Other functions for changing bases: `comp2ele`.

### Function: ele2polynome (L, z)

returns the polynomial in *z* s.t. the elementary symmetric
functions of its roots are in the list `L = [n, e_1, ..., e_n]`, where *n* is the degree of the
polynomial and *e_i* the *i*-th elementary symmetric function.







```maxima
(%i1) ele2polynome ([2, e1, e2], z);
                          2
(%o1)                    z  - e1 z + e2


(%i2) polynome2ele (x^7 - 14*x^5 + 56*x^3  - 56*x + 22, x);
(%o2)          [7, 0, - 14, 0, 56, 0, - 56, - 22]


(%i3) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o3)            x  - 14 x  + 56 x  - 56 x + 22
```


The inverse: `polynome2ele (P, z)`.


Also see:
`polynome2ele`, `pui2polynome`.

### Function: ele2pui (m, L)

goes from the elementary symmetric functions to the complete functions.
Similar to `comp2ele` and `comp2pui`.


Other functions for changing bases: `comp2ele`.

### Function: elem (ele, sym, lvar)

decomposes the symmetric polynomial *sym*, in the variables
contained in the list *lvar*, in terms of the elementary symmetric
functions given in the list *ele*.  If the first element of
*ele* is given, it will be the size of the alphabet, otherwise the
size will be the degree of the polynomial *sym*.  If values are
missing in the list *ele*, formal values of the type *e1*,
*e2*, etc. will be added.  The polynomial *sym* may be given in
three different forms: contracted (`elem` should then be 1, its
default value), partitioned (`elem` should be 3), or extended
(i.e. the entire polynomial, and `elem` should then be 2).  The
function `pui` is used in the same way.


On an alphabet of size 3 with *e1*, the first elementary symmetric
function, with value 7, the symmetric polynomial in 3 variables whose
contracted form (which here depends on only two of its variables) is
*x^4-2*x*y* decomposes as follows in elementary symmetric functions:






```maxima
(%i1) elem ([3, 7], x^4 - 2*x*y, [x, y]);
(%o1) 7 (e3 - 7 e2 + 7 (49 - e2)) + 21 e3

                                         + (- 2 (49 - e2) - 2) e2


(%i2) ratsimp (%);
                              2
(%o2)             28 e3 + 2 e2  - 198 e2 + 2401
```



Other functions for changing bases: `comp2ele`.

### Function: explose (pc, lvar)

returns the symmetric polynomial associated with the contracted form
*pc*. The list *lvar* contains the variables.





```maxima
(%i1) explose (a*x + 1, [x, y, z]);
(%o1)                  a z + a y + a x + 1
```

### Function: kostka (part_1, part_2)

written by P. Esperet, calculates the Kostka number of the partition
*part_1* and *part_2*.





```maxima
(%i1) kostka ([3, 3, 3], [2, 2, 2, 1, 1, 1]);
(%o1)                           6
```

### Function: lgtreillis (n, m)

returns the list of partitions of weight *n* and length *m*.





```maxima
(%i1) lgtreillis (4, 2);
(%o1)                   [[3, 1], [2, 2]]
```


Also see: `ltreillis`, `treillis` and `treinat`.

See also: `ltreillis`, `treillis`, `treinat`.

### Function: ltreillis (n, m)

returns the list of partitions of weight *n* and length less than or
equal to *m*.





```maxima
(%i1) ltreillis (4, 2);
(%o1)               [[4, 0], [3, 1], [2, 2]]
```


Also see: `lgtreillis`, `treillis` and `treinat`.

See also: `lgtreillis`, `treillis`, `treinat`.

### Function: mon2schur (L)

The list *L* represents the Schur function $S_L$: we have
$L = [i_1, i_2, ..., i_q]$, with $i_1 <= i_2 <= ... <= i_q$.
The Schur function $S_[i_1, i_2, ..., i_q]$ is the minor
of the infinite matrix $h_[i-j]$, $i <= 1, j <= 1$,
consisting of the $q$ first rows and the columns $1 + i_1, 2 + i_2, ..., q + i_q$.


This Schur function can be written in terms of monomials by using
`treinat` and `kostka`.  The form returned is a symmetric
polynomial in a contracted representation in the variables

$x_1,x_2,\ldots$

$x_1,x_2,...$







```maxima
(%i1) mon2schur ([1, 1, 1]);
(%o1)                       x1 x2 x3


(%i2) mon2schur ([3]);
                                  2        3
(%o2)                x1 x2 x3 + x1  x2 + x1


(%i3) mon2schur ([1, 2]);
                                      2
(%o3)                  2 x1 x2 x3 + x1  x2
```



which means that for 3 variables this gives:




```maxima
2 x1 x2 x3 + x1^2 x2 + x2^2 x1 + x1^2 x3 + x3^2 x1
    + x2^2 x3 + x3^2 x2
```


Other functions for changing bases: `comp2ele`.

See also: `treinat`, `kostka`.

### Function: multi_elem (l_elem, multi_pc, l_var)

decomposes a multi-symmetric polynomial in the multi-contracted form
*multi_pc* in the groups of variables contained in the list of lists
*l_var* in terms of the elementary symmetric functions contained in
*l_elem*.






```maxima
(%i1) multi_elem ([[2, e1, e2], [2, f1, f2]], a*x + a^2 + x^3,
      [[x, y], [a, b]]);
                                                  3
(%o1)         - 2 f2 + f1 (f1 + e1) - 3 e1 e2 + e1


(%i2) ratsimp (%);
                         2                       3
(%o2)         - 2 f2 + f1  + e1 f1 - 3 e1 e2 + e1
```


Other functions for changing bases: `comp2ele`.

### Function: multi_orbit (P, lvar_1, lvar_2, ..., lvar_p)

*P* is a polynomial in the set of variables contained in the lists
*lvar_1*, *lvar_2*, ..., *lvar_p*. This function returns the
orbit of the polynomial *P* under the action of the product of the
symmetric groups of the sets of variables represented in these *p*
lists.






```maxima
(%i1) multi_orbit (a*x + b*y, [[x, y], [a, b]]);
(%o1)                [b y + a x, a y + b x]


(%i2) multi_orbit (x + y + 2*a, [[x, y], [a, b, c]]);
(%o2)        [y + x + 2 c, y + x + 2 b, y + x + 2 a]
```


Also see: `orbit` for the action of a single symmetric group.

### Function: multi_pui ()

is to the function `pui` what the function `multi_elem` is to
the function `elem`.





```maxima
(%i1) multi_pui ([[2, p1, p2], [2, t1, t2]], a*x + a^2 + x^3,
      [[x, y], [a, b]]);
                                            3
                                3 p1 p2   p1
(%o1)              t2 + p1 t1 + ------- - ---
                                   2       2
```

### Function: multinomial (r, part)

where *r* is the weight of the partition *part*.  This function
returns the associate multinomial coefficient: if the parts of
*part* are *i_1*, *i_2*, ..., *i_k*, the result is
`r!/(i_1! i_2! ... i_k!)`.

### Function: multsym (ppart_1, ppart_2, n)

returns the product of the two symmetric polynomials in *n*
variables by working only modulo the action of the symmetric group of
order *n*. The polynomials are in their partitioned form.


Given the 2 symmetric polynomials in *x*, *y*:  `3*(x + y) + 2*x*y` and `5*(x^2 + y^2)` whose partitioned forms are `[[3, 1], [2, 1, 1]]` and `[[5, 2]]`, their product will be





```maxima
(%i1) multsym ([[3, 1], [2, 1, 1]], [[5, 2]], 2);
(%o1)         [[10, 3, 1], [15, 3, 0], [15, 2, 1]]
```


that is `10*(x^3*y + y^3*x) + 15*(x^2*y + y^2*x) + 15*(x^3 + y^3)`.


Functions for changing the representations of a symmetric polynomial:


`contract`, `cont2part`, `explose`, `part2cont`,
`partpol`, `tcontract`, `tpartpol`.

### Function: orbit (P, lvar)

computes the orbit of the polynomial *P* in the variables in the list
*lvar* under the action of the symmetric group of the set of
variables in the list *lvar*.






```maxima
(%i1) orbit (a*x + b*y, [x, y]);
(%o1)                [a y + b x, b y + a x]


(%i2) orbit (2*x + x^2, [x, y]);
                        2         2
(%o2)                 [y  + 2 y, x  + 2 x]
```


See also `multi_orbit` for the action of a product of symmetric
groups on a polynomial.

See also: `multi_orbit`.

### Function: part2cont (ppart, lvar)

goes from the partitioned form to the contracted form of a symmetric polynomial.
The contracted form is rendered with the variables in *lvar*.





```maxima
(%i1) part2cont ([[2*a^3*b, 4, 1]], [x, y]);
                              3    4
(%o1)                      2 a  b x  y
```

### Function: partpol (psym, lvar)

*psym* is a symmetric polynomial in the variables of the list
*lvar*. This function returns its partitioned representation.





```maxima
(%i1) partpol (-a*(x + y) + 3*x*y, [x, y]);
(%o1)               [[3, 1, 1], [- a, 1, 0]]
```

### Function: permut (L)

returns the list of permutations of the list *L*.

### Function: polynome2ele (P, x)

gives the list `l = [n, e_1, ..., e_n]`
where *n* is the degree of the polynomial *P* in the variable
*x* and *e_i* is the *i*-the elementary symmetric function
of the roots of *P*.






```maxima
(%i1) polynome2ele (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x);
(%o1)          [7, 0, - 14, 0, 56, 0, - 56, - 22]


(%i2) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o2)            x  - 14 x  + 56 x  - 56 x + 22
```


The inverse: `ele2polynome (l, x)`

### Function: prodrac (L, k)

*L* is a list containing the elementary symmetric functions 
on a set *A*. `prodrac` returns the polynomial whose roots
are the *k* by *k* products of the elements of *A*.


Also see `somrac`.

### Function: pui (L, sym, lvar)

decomposes the symmetric polynomial *sym*, in the variables in the
list *lvar*, in terms of the power functions in the list *L*.
If the first element of *L* is given, it will be the size of the
alphabet, otherwise the size will be the degree of the polynomial
*sym*.  If values are missing in the list *L*, formal values of
the type *p1*, *p2* , etc. will be added. The polynomial
*sym* may be given in three different forms: contracted (`elem`
should then be 1, its default value), partitioned (`elem` should be
3), or extended (i.e. the entire polynomial, and `elem` should then
be 2). The function `pui` is used in the same way.







```maxima
(%i1) pui;
(%o1)                           1


(%i2) pui ([3, a, b], u*x*y*z, [x, y, z]);
                       2
                   a (a  - b) u   (a b - p3) u
(%o2)              ------------ - ------------
                        6              3


(%i3) ratsimp (%);
                                       3
                      (2 p3 - 3 a b + a ) u
(%o3)                 ---------------------
                                6
```


Other functions for changing bases: `comp2ele`.

### Function: pui2comp (n, lpui)

renders the list of the first *n* complete functions (with the
length first) in terms of the power functions given in the list
*lpui*. If the list *lpui* is empty, the cardinal is *n*,
otherwise it is its first element (as in `comp2ele` and
`comp2pui`).







```maxima
(%i1) pui2comp (2, []);
                                       2
                                p2 + p1
(%o1)                   [2, p1, --------]
                                   2


(%i2) pui2comp (3, [2, a1]);
                                            2
                                 a1 (p2 + a1 )
                         2  p3 + ------------- + a1 p2
                  p2 + a1              2
(%o2)     [2, a1, --------, --------------------------]
                     2                  3


(%i3) ratsimp (%);
                            2                     3
                     p2 + a1   2 p3 + 3 a1 p2 + a1
(%o3)        [2, a1, --------, --------------------]
                        2               6
```


Other functions for changing bases: `comp2ele`.

### Function: pui2ele (n, lpui)

effects the passage from power functions to the elementary symmetric functions.
If the flag `pui2ele` is `girard`, it will return the list of
elementary symmetric functions from 1 to *n*, and if the flag is
`close`, it will return the *n*-th elementary symmetric function.


Other functions for changing bases: `comp2ele`.

### Function: pui2polynome (x, lpui)

calculates the polynomial in *x* whose power functions of the roots
are given in the list *lpui*.







```maxima
(%i1) pui;
(%o1)                           1


(%i2) kill(labels);
(%o0)                         done


(%i1) polynome2ele (x^3 - 4*x^2 + 5*x - 1, x);
(%o1)                     [3, 4, 5, 1]


(%i2) ele2pui (3, %);
(%o2)                     [3, 4, 6, 7]


(%i3) pui2polynome (x, %);
                        3      2
(%o3)                  x  - 4 x  + 5 x - 1
```


See also:
`polynome2ele`, `ele2polynome`.

See also: `polynome2ele`, `ele2polynome`.

### Function: pui_direct (orbite, lvar_1, ..., lvar_n, d_1, d_2, ..., d_n)

Let *f* be a polynomial in *n* blocks of variables *lvar_1*,
..., *lvar_n*.  Let *c_i* be the number of variables in
*lvar_i*, and *SC* be the product of *n* symmetric groups of
degree *c_1*, ..., *c_n*. This group acts naturally on *f*.
The list *orbite* is the orbit, denoted `SC(f)`, of
the function *f* under the action of *SC*. (This list may be
obtained by the function `multi_orbit`.)  The *di* are integers
s.t.
$c_1 <= d_1, c_2 <= d_2, ..., c_n <= d_n$.


Let *SD* be the product of the symmetric groups $S_[d_1] x S_[d_2] x ... x S_[d_n]$.
The function `pui_direct` returns
the first *n* power functions of `SD(f)` deduced
from the power functions of `SC(f)`, where *n* is
the size of `SD(f)`.


The result is in multi-contracted form w.r.t. *SD*, i.e. only one
element is kept per orbit, under the action of *SD*.








```maxima
(%i1) l: [[x, y], [a, b]];
(%o1)                   [[x, y], [a, b]]


(%i2) pui_direct (multi_orbit (a*x + b*y, l), l, [2, 2]);
                                       2  2
(%o2)               [a x, 4 a b x y + a  x ]


(%i3) pui_direct (multi_orbit (a*x + b*y, l), l, [3, 2]);
                             2  2     2    2        3  3
(%o3) [2 a x, 4 a b x y + 2 a  x , 3 a  b x  y + 2 a  x , 

    2  2  2  2      3    3        4  4
12 a  b  x  y  + 4 a  b x  y + 2 a  x , 

    3  2  3  2      4    4        5  5
10 a  b  x  y  + 5 a  b x  y + 2 a  x , 

    3  3  3  3       4  2  4  2      5    5        6  6
40 a  b  x  y  + 15 a  b  x  y  + 6 a  b x  y + 2 a  x ]


(%i4) pui_direct ([y + x + 2*c, y + x + 2*b, y + x + 2*a],
      [[x, y], [a, b, c]], [2, 3]);
                             2              2
(%o4) [3 x + 2 a, 6 x y + 3 x  + 4 a x + 4 a , 

                 2                   3        2       2        3
              9 x  y + 12 a x y + 3 x  + 6 a x  + 12 a  x + 8 a ]
```

### Function: puireduc (n, lpui)

*lpui* is a list whose first element is an integer *m*.
`puireduc` gives the first *n* power functions in terms of the
first *m*.





```maxima
(%i1) puireduc (3, [2]);
                                         2
                                   p1 (p1  - p2)
(%o1)          [2, p1, p2, p1 p2 - -------------]
                                         2


(%i2) ratsimp (%);
                                           3
                               3 p1 p2 - p1
(%o2)              [2, p1, p2, -------------]
                                     2
```

### Function: resolvante (P, x, f, x_1, ..., x_d)

calculates the resolvent of the polynomial *P* in *x* of degree
`n >= d` by the function *f* expressed in the variables
*x_1*, ..., *x_d*.  For efficiency of computation it is
important to not include in the list `[x_1, ..., x_d]`
variables which do not appear in the transformation function *f*.


To increase the efficiency of the computation one may set flags in
`resolvante` so as to use appropriate algorithms:


If the function *f* is unitary:


- *
A polynomial in a single variable,
- *
  
linear,
- *
  
alternating,
- *
  
a sum,
- *
  
symmetric,
- *
  
a product,
- *
the function of the Cayley resolvent (usable up to degree 5)


```maxima
(x1*x2 + x2*x3 + x3*x4 + x4*x5 + x5*x1 -
     (x1*x3 + x3*x5 + x5*x2 + x2*x4 + x4*x1))^2
```

general,

the flag of `resolvante` may be, respectively:


- *
  
unitaire,
- *
  
lineaire,
- *
  
alternee,
- *
  
somme,
- *
  
produit,
- *
  
cayley,
- *
  
generale.

























```maxima
(%i1) resolvante: unitaire$

(%i2) resolvante (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x, x^3 - 1,
      [x]);

" resolvante unitaire " [7, 0, 28, 0, 168, 0, 1120, - 154, 7840,
                         - 2772, 56448, - 33880, 

413952, - 352352, 3076668, - 3363360, 23114112, - 30494464, 

175230832, - 267412992, 1338886528, - 2292126760] 
  3       6      3       9      6      3
[x  - 1, x  - 2 x  + 1, x  - 3 x  + 3 x  - 1, 

 12      9      6      3       15      12       9       6      3
x   - 4 x  + 6 x  - 4 x  + 1, x   - 5 x   + 10 x  - 10 x  + 5 x

       18      15       12       9       6      3
 - 1, x   - 6 x   + 15 x   - 20 x  + 15 x  - 6 x  + 1, 

 21      18       15       12       9       6      3
x   - 7 x   + 21 x   - 35 x   + 35 x  - 21 x  + 7 x  - 1] 
[- 7, 1127, - 6139, 431767, - 5472047, 201692519, - 3603982011] 
       7      6        5         4          3           2
(%o2) y  + 7 y  - 539 y  - 1841 y  + 51443 y  + 315133 y

                                              + 376999 y + 125253

(%i3) resolvante: lineaire$

(%i4) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3]);

" resolvante lineaire " 
       24       20         16            12             8
(%o4) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000

(%i5) resolvante: general$

(%i6) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3]);

" resolvante generale " 
       24       20         16            12             8
(%o6) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000


(%i7) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3, x4]);

" resolvante generale " 
       24       20         16            12             8
(%o7) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000


(%i8) direct ([x^4 - 1], x, x1 + 2*x2 + 3*x3, [[x1, x2, x3]]);
       24       20         16            12             8
(%o8) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000

(%i9) resolvante :lineaire$

(%i10) resolvante (x^4 - 1, x, x1 + x2 + x3, [x1, x2, x3]);

" resolvante lineaire " 
                              4
(%o10)                       y  - 1

(%i11) resolvante: symetrique$

(%i12) resolvante (x^4 - 1, x, x1 + x2 + x3, [x1, x2, x3]);

" resolvante symetrique " 
                              4
(%o12)                       y  - 1


(%i13) resolvante (x^4 + x + 1, x, x1 - x2, [x1, x2]);

" resolvante symetrique " 
                           6      2
(%o13)                    y  - 4 y  - 1

(%i14) resolvante: alternee$

(%i15) resolvante (x^4 + x + 1, x, x1 - x2, [x1, x2]);

" resolvante alternee " 
            12      8       6        4        2
(%o15)     y   + 8 y  + 26 y  - 112 y  + 216 y  + 229

(%i16) resolvante: produit$

(%i17) resolvante (x^7 - 7*x + 3, x, x1*x2*x3, [x1, x2, x3]);

" resolvante produit "
        35      33         29        28         27        26
(%o17) y   - 7 y   - 1029 y   + 135 y   + 7203 y   - 756 y

         24           23          22            21           20
 + 1323 y   + 352947 y   - 46305 y   - 2463339 y   + 324135 y

          19           18             17              15
 - 30618 y   - 453789 y   - 40246444 y   + 282225202 y

             14              12             11            10
 - 44274492 y   + 155098503 y   + 12252303 y   + 2893401 y

              9            8            7             6
 - 171532242 y  + 6751269 y  + 2657205 y  - 94517766 y

            5             3
 - 3720087 y  + 26040609 y  + 14348907

(%i18) resolvante: symetrique$

(%i19) resolvante (x^7 - 7*x + 3, x, x1*x2*x3, [x1, x2, x3]);

" resolvante symetrique " 
        35      33         29        28         27        26
(%o19) y   - 7 y   - 1029 y   + 135 y   + 7203 y   - 756 y

         24           23          22            21           20
 + 1323 y   + 352947 y   - 46305 y   - 2463339 y   + 324135 y

          19           18             17              15
 - 30618 y   - 453789 y   - 40246444 y   + 282225202 y

             14              12             11            10
 - 44274492 y   + 155098503 y   + 12252303 y   + 2893401 y

              9            8            7             6
 - 171532242 y  + 6751269 y  + 2657205 y  - 94517766 y

            5             3
 - 3720087 y  + 26040609 y  + 14348907

(%i20) resolvante: cayley$

(%i21) resolvante (x^5 - 4*x^2 + x + 1, x, a, []);

" resolvante de Cayley "
        6       5         4          3            2
(%o21) x  - 40 x  + 4080 x  - 92928 x  + 3772160 x  + 37880832 x

                                                       + 93392896
```


For the Cayley resolvent, the 2 last arguments are neutral and the input
polynomial must necessarily be of degree 5.


See also:


`resolvante_bipartite`, `resolvante_produit_sym`,
`resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, 
`resolvante_klein3`, `resolvante_vierer`, `resolvante_005fdiedrale`.

See also: `resolvante_bipartite`, `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`.

### Function: resolvante_alternee1 (P, x)

calculates the transformation
`P(x)` of degree *n* by the function
$product(x_i - x_j, 1 <= i < j <= n - 1)$.


See also:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante`,  `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_005fbipartite`.

See also: `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante`, `resolvante_klein`, `resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`, `resolvante_bipartite`.

### Function: resolvante_bipartite (P, x)

calculates the transformation of
`P(x)` of even degree *n* by the function 


$x_1 x_2 ... x_[n/2] + x_[n/2 + 1] ... x_n$.





```maxima
(%i1) resolvante_bipartite (x^6 + 108, x);
              10        8           6             4
(%o1)        y   - 972 y  + 314928 y  - 34012224 y
```


See also:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_005falternee1`.

See also: `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante`, `resolvante_klein`, `resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`, `resolvante_alternee1`.

### Function: resolvante_diedrale (P, x)

calculates the transformation of `P(x)` by the function
`x_1 x_2 + x_3 x_4`.





```maxima
(%i1) resolvante_diedrale (x^5 - 3*x^4 + 1, x);
       15       12       11       10        9         8         7
(%o1) x   - 21 x   - 81 x   - 21 x   + 207 x  + 1134 x  + 2331 x

        6         5          4          3          2
 - 945 x  - 4970 x  - 18333 x  - 29079 x  - 20745 x  - 25326 x

 - 697
```


See also:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante`.

See also: `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`, `resolvante_vierer`, `resolvante`.

### Function: resolvante_klein (P, x)

calculates the transformation of `P(x)` by the function
`x_1 x_2 x_4 + x_4`.


See also:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_005fdiedrale`.

See also: `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante_alternee1`, `resolvante`, `resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`.

### Function: resolvante_klein3 (P, x)

calculates the transformation of `P(x)` by the function
`x_1 x_2 x_4 + x_4`.


See also:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante`,
`resolvante_vierer`, `resolvante_005fdiedrale`.

See also: `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, `resolvante`, `resolvante_vierer`, `resolvante_diedrale`.

### Function: resolvante_produit_sym (P, x)

calculates the list of all product resolvents of the polynomial
`P(x)`.







```maxima
(%i1) resolvante_produit_sym (x^5 + 3*x^4 + 2*x - 1, x);
        5      4             10      8       7       6       5
(%o1) [y  + 3 y  + 2 y - 1, y   - 2 y  - 21 y  - 31 y  - 14 y

    4       3      2       10      8       7    6       5       4
 - y  + 14 y  + 3 y  + 1, y   + 3 y  + 14 y  - y  - 14 y  - 31 y

       3      2       5      4
 - 21 y  - 2 y  + 1, y  - 2 y  - 3 y - 1, y - 1]

(%i2) resolvante: produit$

(%i3) resolvante (x^5 + 3*x^4 + 2*x - 1, x, a*b*c, [a, b, c]);

" resolvante produit "
       10      8       7    6        5       4       3     2
(%o3) y   + 3 y  + 14 y  - y  - 14 y  - 31 y  - 21 y  - 2 y  + 1
```





See also:


`resolvante`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`,
`resolvante_klein3`, `resolvante_vierer`,
`resolvante_005fdiedrale`.

See also: `resolvante`, `resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`.

### Function: resolvante_unitaire (P, Q, x)

computes the resolvent of the polynomial `P(x)` by the
polynomial `Q(x)`. 


See also:


`resolvante_produit_sym`, `resolvante`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_005fdiedrale`.

See also: `resolvante_produit_sym`, `resolvante`, `resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`.

### Function: resolvante_vierer (P, x)

computes the transformation of
`P(x)` by the function `x_1 x_2 - x_3 x_4`.


See also:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante`, `resolvante_005fdiedrale`.

See also: `resolvante_produit_sym`, `resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`, `resolvante`, `resolvante_diedrale`.

### Function: schur2comp (P, l_var)

*P* is a polynomial in the variables of the list *l_var*.  Each
of these variables represents a complete symmetric function.  In
*l_var* the *i*-th complete symmetric function is represented by
the concatenation of the letter `h` and the integer *i*:
`hi`.  This function expresses *P* in terms of Schur
functions.







```maxima
(%i1) schur2comp (h1*h2 - h3, [h1, h2, h3]);
(%o1)                         s
                               1, 2


(%i2) schur2comp (a*h3, [h3]);
(%o2)                         s  a
                               3
```

### Function: somrac (L, k)

The list *L* contains elementary symmetric functions of a polynomial
*P* . The function computes the polynomial whose roots are the 
*k* by *k* distinct sums of the roots of *P*. 


Also see `prodrac`.

### Function: tcontract (pol, lvar)

tests if the polynomial *pol* is symmetric in the variables of the
list *lvar*.  If so, it returns a contracted representation like the
function `contract`.

### Function: tpartpol (pol, lvar)

tests if the polynomial *pol* is symmetric in the variables of the
list *lvar*.  If so, it returns its partitioned representation like
the function `partpol`.

### Function: treillis (n)

returns all partitions of weight *n*.





```maxima
(%i1) treillis (4);
(%o1)    [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
```


See also: `lgtreillis`, `ltreillis` and `treinat`.

See also: `lgtreillis`, `ltreillis`, `treinat`.

### Function: treinat (part)

returns the list of partitions inferior to the partition *part* w.r.t.
the natural order.







```maxima
(%i1) treinat ([5]);
(%o1)                         [[5]]


(%i2) treinat ([1, 1, 1, 1, 1]);
(%o2) [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], 

                                                 [1, 1, 1, 1, 1]]


(%i3) treinat ([3, 2]);
(%o3)                 [[5], [4, 1], [3, 2]]
```


See also: `lgtreillis`, `ltreillis` and `treillis`.

See also: `lgtreillis`, `ltreillis`, `treillis`.

