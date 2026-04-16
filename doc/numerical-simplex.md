## simplex

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

### Variable: scale_lp

Default value: `false`


When `scale_lp` is `true`,
`linear_program` scales its input so that the maximum absolute value in each row or column is 1.

