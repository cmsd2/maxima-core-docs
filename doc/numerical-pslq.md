## pslq

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

