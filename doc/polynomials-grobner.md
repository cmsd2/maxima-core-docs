## grobner

### Function: poly_add (poly1, poly2, varlist)

Adds two polynomials *poly1* and *poly2*.


```maxima
(%i1) poly_add(z+x^2*y,x-z,[x,y,z]);
                                    2
(%o1)                              x  y + x
```

### Function: poly_buchberger (polylist_fl, varlist)

`poly_buchberger` performs the Buchberger algorithm on a list of
polynomials and returns the resulting Groebner basis.

### Function: poly_buchberger_criterion (polylist, varlist)

Returns `true` if *polylist* is a Groebner basis with respect to the current term
order, by using the Buchberger
criterion: for every two polynomials $h1$ and $h2$ in *polylist* the
S-polynomial $S(h1,h2)$ reduces to 0 $modulo$ *polylist*.

### Variable: poly_coefficient_ring

Default value: `expression_ring`


This switch indicates the coefficient ring of the polynomials that
will be used in grobner calculations. If not set, *maxima’s* general
expression ring will be used. This variable may be set to
`ring_of_integers` if desired.

### Function: poly_colon_ideal (polylist1, polylist2, varlist)

Returns the reduced Groebner basis of the colon ideal 


$I(polylist1):I(polylist2)$



where $polylist1$ and $polylist2$ are two lists of polynomials.

### Function: poly_content (poly, ., varlist)

`poly_content` extracts the GCD of its coefficients


```maxima
(%i1) poly_content(35*y+21*x,[x,y]);
(%o1)                                  7
```

### Function: poly_depends_p (poly, var, varlist)

`poly_depends` tests whether a polynomial depends on a variable *var*.

### Function: poly_elimination_ideal (polylist, number, varlist)

`poly_elimination_ideal` returns the grobner basis of the $number$-th elimination ideal of an
ideal specified as a list of generating polynomials (not necessarily Groebner basis).

### Variable: poly_elimination_order

Default value: `false`


Name of the default elimination order used in elimination
calculations. If set, it overrides the settings in variables
`poly_primary_elimination_order` and `poly_secondary_elimination_order`.
The user must ensure that this is a true elimination order valid
for the number of eliminated variables.

### Function: poly_exact_divide (poly1, poly2, varlist)

Divide a polynomial *poly1* by another polynomial *poly2*. Assumes that exact
division with no remainder is possible. Returns the quotient.

### Function: poly_expand (poly, varlist)

This function parses polynomials to internal form and back. It
is equivalent to `expand(poly)` if *poly* parses correctly to
a polynomial. If the representation is not compatible with a
polynomial in variables *varlist*, the result is an error.
It can be used to test whether an expression correctly parses to the
internal representation. The following examples illustrate that
indexed and transcendental function variables are allowed.


```maxima
(%i1) poly_expand((x-y)*(y+x),[x,y]);
                                     2    2
(%o1)                               x  - y
(%i2) poly_expand((y+x)^2,[x,y]);
                                2            2
(%o2)                          y  + 2 x y + x
(%i3) poly_expand((y+x)^5,[x,y]);
                  5      4         2  3       3  2      4      5
(%o3)            y  + 5 x y  + 10 x  y  + 10 x  y  + 5 x  y + x
(%i4) poly_expand(-1-x*exp(y)+x^2/sqrt(y),[x]);
                                          2
                                  y      x
(%o4)                       - x %e  + ------- - 1
                                       sqrt(y)

(%i5) poly_expand(-1-sin(x)^2+sin(x),[sin(x)]);
                                2
(%o5)                      - sin (x) + sin(x) - 1
```

### Function: poly_expt (poly, number, varlist)

exponentitates *poly* by a positive integer *number*. If *number* is not a positive integer number an error will be raised.


```maxima
(%i1) poly_expt(x-y,3,[x,y])-(x-y)^3,expand;
(%o1)                                  0
```

### Function: poly_gcd (poly1, poly2, varlist)

Returns the greatest common divisor of *poly1* and *poly2*.


See also `ezgcd`, `gcd`, `gcdex`, and
`gcdivide`.


Example:



```maxima
(%i1) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i3) poly_gcd(p1, p2, [x]);
                            2
(%o3)                    6 x  + 13 x + 6
```

See also: `ezgcd`, `gcd`, `gcdex`, `gcdivide`.

### Function: poly_grobner (polylist, varlist)

Returns a Groebner basis of the ideal span by the polynomials *polylist*. Affected by the global flags.

### Variable: poly_grobner_algorithm

Default value: `buchberger`


Possible values: 


- * 
`buchberger`
- * 
`parallel_buchberger`
- * 
`gebauer_moeller`


The name of the algorithm used to find the Groebner Bases.

### Variable: poly_grobner_debug

Default value: `false`


If set to `true`, produce debugging and tracing output.

### Function: poly_grobner_equal (polylist1, polylist2, varlist)

`poly_grobner_equal` tests whether two Groebner Bases generate the same ideal.
Returns `true` if two lists of polynomials *polylist1* and *polylist2*, assumed to be Groebner Bases,
generate the same ideal, and `false` otherwise.
This is equivalent to checking that every polynomial of the first basis reduces to 0
modulo the second basis and vice versa. Note that in the example below the
first list is not a Groebner basis, and thus the result is `false`.



```maxima
(%i1) poly_grobner_equal([y+x,x-y],[x,y],[x,y]);
(%o1)                         false
```

### Function: poly_grobner_member (poly, polylist, varlist)

Returns `true` if a polynomial *poly* belongs to the ideal generated by the
polynomial list *polylist*, which is assumed to be a Groebner basis. Returns `false` otherwise.


`poly_grobner_member` tests whether a polynomial belongs to an ideal generated by a list of polynomials,
which is assumed to be a Groebner basis. Equivalent to `normal_form` being 0.

### Function: poly_grobner_subsetp (polylist1, polylist2, varlist)

`poly_grobner_subsetp` tests whether an ideal generated by *polylist1*
is contained in the ideal generated by *polylist2*. For this test to always succeed,
*polylist2* must be a Groebner basis.

### Function: poly_ideal_intersection (polylist1, polylist2, varlist)

`poly_ideal_intersection` returns the intersection of two ideals.

### Function: poly_ideal_polysaturation (polylist, polylistlist, varlist)

*polylistlist* is a list of n list of polynomials `[polylist1,...,polylistn]`.
Returns the reduced Groebner basis of the saturation of the ideal


I(polylist):I(polylist_1)^inf:...:I(polylist_n)^inf

### Function: poly_ideal_polysaturation1 (polylist1, polylist2, varlist)

*polylist2* is a list of n polynomials `[poly1,...,polyn]`.
Returns the reduced Groebner basis of the ideal


I(polylist):poly1^inf:...:polyn^inf



obtained by a
sequence of successive saturations in the polynomials
of the polynomial list *polylist2* of the ideal generated by the
polynomial list *polylist1*.

### Function: poly_ideal_saturation (polylist1, polylist2, varlist)

Returns the reduced Groebner basis of the saturation of the ideal


I(polylist1):I(polylist2)^inf



Geometrically, over an algebraically closed field, this is the set of polynomials in
the ideal generated by *polylist1* which do not identically vanish on the
variety of *polylist2*.

### Function: poly_ideal_saturation1 (polylist, poly, varlist)

Returns the reduced Groebner basis of the saturation of the ideal


I(polylist):poly^inf



Geometrically, over an algebraically closed field, this is the set
of polynomials in the ideal generated by *polylist* which do not identically
vanish on the variety of *poly*.

### Function: poly_lcm (poly1, poly2, varlist)

Returns the lowest common multiple of *poly1* and *poly2*.

### Function: poly_minimization (polylist, varlist)

Returns a sublist of the polynomial list *polylist* spanning the same
monomial ideal as *polylist* but minimal, i.e. no leading monomial
of a polynomial in the sublist divides the leading monomial
of another polynomial.

### Variable: poly_monomial_order

Default value: `lex`


This global switch controls which monomial order is used in polynomial and Groebner Bases calculations. If not set, `lex` will be used.

### Function: poly_multiply (poly1, poly2, varlist)

Returns the product of polynomials *poly1* and *poly2*.


```maxima
(%i2) poly_multiply(z+x^2*y,x-z,[x,y,z])-(z+x^2*y)*(x-z),expand;
(%o1)                                  0
```

### Function: poly_normal_form (poly, polylist, varlist)

`poly_normal_form` finds the normal form of a polynomial *poly* with respect
to a set of polynomials *polylist*.

### Function: poly_normalize (poly, varlist)

Returns the polynomial *poly* divided by the leading coefficient.
It assumes that the division is possible, which may not always be the
case in rings which are not fields.

### Function: poly_normalize_list (polylist, varlist)

`poly_normalize_list` applies `poly_normalize` to each polynomial in the list.
That means it divides every polynomial in a list *polylist* by its leading coefficient.

### Function: poly_polysaturation_extension (poly, polylist, varlist1, varlist2)

### Variable: poly_primary_elimination_order

Default value: `false`


Name of the default order for eliminated variables in
elimination-based functions. If not set, `lex` will be used.

### Function: poly_primitive_part (poly1, varlist)

Returns the polynomial *poly* divided by the GCD of its coefficients. 



```maxima
(%i1) poly_primitive_part(35*y+21*x,[x,y]);
(%o1)                              5 y + 3 x
```

### Function: poly_pseudo_divide (poly, polylist, varlist)

Pseudo-divide a polynomial *poly* by the list of $n$ polynomials *polylist*. Return
multiple values. The first value is a list of quotients $a$. The
second value is the remainder $r$. The third argument is a scalar
coefficient $c$, such that $c*poly$ can be divided by *polylist* within the ring
of coefficients, which is not necessarily a field. Finally, the
fourth value is an integer count of the number of reductions
performed. The resulting objects satisfy the equation:


$c*poly=sum(a[i]*polylist[i],i=1...n)+r$.

### Function: poly_reduced_grobner (polylist, varlist)

Returns a reduced Groebner basis of the ideal span by the polynomials *polylist*. Affected by the global flags.

### Function: poly_reduction (polylist, varlist)

`poly_reduction` reduces a list of polynomials *polylist*, so that
each polynomial is fully reduced with respect to the other polynomials.

### Variable: poly_return_term_list

Default value: `false`


If set to `true`, all functions in this package will return each
polynomial as a list of terms in the current monomial order rather
than a *maxima* general expression.

### Function: poly_s_polynomial (poly1, poly2, varlist)

Returns the *syzygy polynomial* (*S-polynomial*) of two polynomials *poly1* and *poly2*.

### Function: poly_saturation_extension (poly, polylist, varlist1, varlist2)

`poly_saturation_extension` implements the famous Rabinowitz trick.

### Variable: poly_secondary_elimination_order

Default value: `false`


Name of the default order for kept variables in elimination-based functions. If not set, `lex` will be used.

### Function: poly_subtract (poly1, poly2, varlist)

Subtracts a polynomial *poly2* from *poly1*.


```maxima
(%i1) poly_subtract(z+x^2*y,x-z,[x,y,z]);
                                      2
(%o1)                          2 z + x  y - x
```

### Variable: poly_top_reduction_only

Default value: `false`


If not `false`, use top reduction only whenever possible. Top
reduction means that division algorithm stops after the first
reduction.

