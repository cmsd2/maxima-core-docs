## Limits

### Function: gruntz (gruntz, expr, var, value, gruntz, expr, var, value, direction)

Compute limit of expression *expr* with respect to variable *var* at *value*.
When *value* is not infinite (i.e., not `inf` or `minf`),
*direction* must be supplied,
either `plus` for a limit from above,
or `minus` for a limit from below.


If `gruntz` cannot find the limit,
an unevaluated expression `gruntz(...)` is returned.


`gruntz` implements the method described in the dissertation of
Dominik Gruntz, "On Computing Limits in a Symbolic Manipulation System"
(ETH Zurich, 1996).


The algorithm identifies the most rapidly varying subexpression,
replaces it with a new variable, rewrites the expression in terms
of the new variable, and then repeats.


The algorithm doesn’t handle oscillating functions, so it can’t do things like
`limit(sin(x)/x, x, inf)`.


To handle limits involving functions such as `gamma(x)` and `erf(x)`,
the Gruntz algorithm requires them to be written in terms of asymptotic expansions,
which Maxima cannot currently do.


The Gruntz algorithm assumes that variables and expressions are real,
so, for example, it can’t handle `limit((-2)^x, x, inf)`.


`gruntz` is one of the methods called from `limit`.

### Variable: lhospitallim

Default value: 4


`lhospitallim` is the maximum number of times L’Hospital’s
rule is used in `limit`.  This prevents infinite looping in cases like
`limit (cot(x)/csc(x), x, 0)`.

See also: `limit`.

### Function: limit (limit, expr, x, val, dir, limit, expr, x, val, limit, expr)

Computes the limit of *expr* as the real variable *x* approaches the
value *val* from the direction *dir*.  *dir* may have the value
`plus` for a limit from above, `minus` for a limit from below, or
may be omitted (implying a two-sided limit is to be computed).


`limit` uses the following special symbols: `inf` (positive infinity)
and `minf` (negative infinity).  On output it may also use `und`
(undefined), `ind` (indefinite but bounded) and `infinity` (complex
infinity).


`infinity` (complex infinity) is returned when the limit of
the absolute value of the expression is positive infinity, but
the limit of the expression itself is not positive infinity or
negative infinity.  This includes cases where the limit of the
complex argument is a constant, as in `limit(log(x), x, minf)`, 
cases where the complex argument oscillates, as in
`limit((-2)^x, x, inf)`, and cases where the complex
argument is different for either side of a two-sided limit, as in
`limit(1/x, x, 0)` and `limit(log(x), x, 0)`.


`lhospitallim` is the maximum number of times L’Hospital’s rule
is used in `limit`.  This prevents infinite looping in cases like
`limit (cot(x)/csc(x), x, 0)`.


`tlimswitch` when true will allow the `limit` command to use
Taylor series expansion when necessary.


`limsubst` prevents `limit` from attempting substitutions on
unknown forms.  This is to avoid bugs like `limit (f(n)/f(n+1), n, inf)`
giving 1.  Setting `limsubst` to `true` will allow such
substitutions.


`limit` with one argument is often called upon to simplify constant
expressions, for example, `limit (inf-1)`.



`example (limit)` displays some examples.


For the method see Wang, P., "Evaluation of Definite Integrals by Symbolic
Manipulation", Ph.D. thesis, MAC TR-92, October 1971.

See also: `minf`, `und`, `ind`, `infinity`, `lhospitallim`, `tlimswitch`, `limsubst`.

### Variable: limsubst

Default value: `false`


prevents `limit` from attempting substitutions on unknown forms.  This is
to avoid bugs like `limit (f(n)/f(n+1), n, inf)` giving 1.  Setting
`limsubst` to `true` will allow such substitutions.

See also: `limit`.

### Function: tlimit (tlimit, expr, x, val, dir, tlimit, expr, x, val, tlimit, expr)

Take the limit of the Taylor series expansion of `expr` in `x`
at `val` from direction `dir`.

### Variable: tlimswitch

Default value: `true`


When `tlimswitch` is `true`, the `limit` command will use a
Taylor series expansion if the limit of the input expression cannot be computed
directly.  This allows evaluation of limits such as
`limit(x/(x-1)-1/log(x),x,1,plus)`.  When `tlimswitch` is `false`
and the limit of input expression cannot be computed directly, `limit` will
return an unevaluated limit expression.

See also: `limit`.

