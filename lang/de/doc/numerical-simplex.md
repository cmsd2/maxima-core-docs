## simplex

<!-- category: Numerical -->
<!-- keywords: epsilon_lp -->
<!-- signatures: epsilon_lp -->
### Variable: epsilon_lp

Default value: `10^-8`


Epsilon used for numerical computations in `linear_program`.


See also: `linear_program`.

<!-- category: Numerical -->
<!-- keywords: linear_program -->
<!-- signatures: linear_program(A, b, c) -->
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

<!-- category: Numerical -->
<!-- keywords: maximize_lp -->
<!-- signatures: maximize_lp(obj, cond, [pos]) -->
### Function: maximize_lp (obj, cond, [pos])

Maximizes linear objective function *obj* subject to some linear
constraints *cond*. See `minimize_lp` for detailed
description of arguments and return value.



See also: `minimize_lp`.

<!-- category: Numerical -->
<!-- keywords: minimize_lp -->
<!-- signatures: minimize_lp(obj, cond, [pos]) -->
### Function: minimize_lp (obj, cond, [pos])

Minimizes a linear objective function *obj* subject to some linear
constraints *cond*. *cond* a list of linear equations or
inequalities. In strict inequalities `>` is replaced by `>=`
and `<` by `<=`. The optional argument *pos* is a list
of decision variables which are assumed to be positive.


If the minimum exists, `minimize_lp` returns a list which
contains the minimum value of the objective function and a list of
decision variable values for which the minimum is attained. If the
problem is not bounded, `minimize_lp` returns "Problem not
bounded!" and if the problem is not feasible, it returns "Ploblem not
feasible!".


The decision variables are not assumed to be nonegative by default. If
all decision variables are nonegative, set `nonegative_lp` to
`true`.  If only some of decision variables are positive, list
them in the optional argument *pos* (note that this is more
efficient than adding constraints).


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
(%i2) minimize_lp(x+y, [3*x+y>0, x+2*y>2]), nonegative_lp=true;
(%o2)                [1, [y = 1, x = 0]]
(%i3) minimize_lp(x+y, [3*x+y=0, x+2*y>2]), nonegative_lp=true;
(%o3)                Problem not feasible!
(%i4) minimize_lp(x+y, [3*x+y>0]);
(%o4)                Problem not bounded!
```



See also: `maximize_lp`, `nonegative_lp`, `epsilon_lp`.

<!-- category: Numerical -->
<!-- keywords: nonegative_lp -->
<!-- signatures: nonegative_lp -->
### Variable: nonegative_lp

Default value: `false`


If `nonegative_lp` is true all decision variables to
`minimize_lp` and `maximize_lp` are assumed to be positive.


See also: `minimize_lp`.

