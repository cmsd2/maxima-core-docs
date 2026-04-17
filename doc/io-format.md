## format

<!-- category: IO -->
<!-- keywords: %coerce_bag -->
<!-- signatures: %coerce_bag(op, expr) -->
### Function: %coerce_bag (op, expr)

Attempts to coerce *expr* into an expression with *op* (one of
`=, #, <, <=, >, >=, [` or matrix) as the top-level operator. It
coerces the expression by swapping operands between layers but only if
adjacent layers are also lists, matrices or relations. This model
assumes that a list of equations, for example, can be viewed as an
equation whose sides are lists. Certain combinations, particularly those
involving inequalities may not be meaningful, however, so some caution
is advised.

<!-- category: IO -->
<!-- keywords: %format_piece -->
<!-- signatures: %format_piece(piece, nth) -->
### Function: %format_piece (piece, nth)

`lratsubst`’s `eqns` into expression and the result is formatted at the next layer.
Format a given piece of an expression, automatically accounting for
subtemplates and the remaining template chain. A specific subtemplate,
rather than the next one, can be selected by specifying *nth*.

<!-- category: IO -->
<!-- keywords: format -->
<!-- signatures: format(expr, template1, ...) -->
### Function: format (expr, template1, ...)

Each `template` indicates the desired form for an expression;
either the expected form or that into which it will be transformed. At
the same time, the indicated form implies a set of *pieces*; the
next template in the chain applies to those pieces. For example,
`%poly(x)` specifies the transformation into a polynomial in
`x`, with the pieces being the coefficients. The passive
`%frac` treats the expression as a fraction; the pieces are the
numerator and denominator.  Whereas the next template formats all pieces
of the previous layer, positional *subtemplates* may be used to
specify formats for each piece individually. This is most useful when
the pieces have unique roles and need to be treated differently, such as
a fraction’s numerator and denominator.

<!-- category: IO -->
<!-- keywords: function_arguments -->
<!-- signatures: function_arguments(expr, functions...) -->
### Function: function_arguments (expr, functions...)

Returns a list of all argument lists for calls to *functions* in *expr*.

<!-- category: IO -->
<!-- keywords: function_calls -->
<!-- signatures: function_calls(expr, functions...) -->
### Function: function_calls (expr, functions...)

Returns a list of all calls in *expr* involving any of *functions*.

<!-- category: IO -->
<!-- keywords: get_coef -->
<!-- signatures: get_coef(clist, k1, ...) -->
### Function: get_coef (clist, k1, ...)

Gets the coefficient from the coefficient list *clist* corresponding
to the keys *ki*. The keys are matched to variable powers when
*clist* is a `%poly`, `%series` or `%Taylor` form. If
*clist* is a `%trig` then *k1* should be `sin`
or `cos` and the remaining keys are matched to multipliers.

<!-- category: IO -->
<!-- keywords: matching_parts -->
<!-- signatures: matching_parts(expr, predicate, args...) -->
### Function: matching_parts (expr, predicate, args...)

Returns a list of all subexpressions of *expr* for which the application
`predicate(piece,args ... )` returns `true`.

<!-- category: IO -->
<!-- keywords: partition_poly -->
<!-- signatures: partition_poly(expr, test, v1, ...) -->
### Function: partition_poly (expr, test, v1, ...)

Partitions *expr* into two polynomials; the first is made of those
monomials for which the function test returns true and the second is the
remainder. The test function is called on the powers of the *vi*.

<!-- category: IO -->
<!-- keywords: partition_series -->
<!-- signatures: partition_series(expr, test, v, O) -->
### Function: partition_series (expr, test, v, O)

<!-- category: IO -->
<!-- keywords: partition_Taylor -->
<!-- signatures: partition_Taylor(expr, test, v, O) -->
### Function: partition_Taylor (expr, test, v, O)

Analog to `partition_poly` for series.

<!-- category: IO -->
<!-- keywords: partition_trig -->
<!-- signatures: partition_trig(expr, sintest, costest, v1, ...) -->
### Function: partition_trig (expr, sintest, costest, v1, ...)

Trigonometric analog to partition poly; The functions *sintest* and
*costest* select sine and cosine terms, respectively; each are called on
the multipliers of the *vi*.

<!-- category: IO -->
<!-- keywords: uncoef -->
<!-- signatures: uncoef(clist) -->
### Function: uncoef (clist)

Reconstructs the expression from a coefficient list *clist*. The
coefficient list can be any of the coefficient list forms.

