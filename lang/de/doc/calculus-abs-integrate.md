## abs_integrate

<!-- category: Calculus -->
<!-- keywords: conditional_integrate -->
<!-- signatures: conditional_integrate(e, x) -->
### Function: conditional_integrate (e, x)

For an integrand with one or more parameters, this function tries to determine
an antiderivative that is valid for all parameter values.  When successful, this
function returns a conditional expression for the antiderivative.



```maxima
(%i1) load("abs_integrate")$
(%i2) conditional_integrate(cos(m*x),x);
                                sin(m x)
(%o2)                %if(m # 0, --------, x)
                                   m
(%i3) conditional_integrate(cos(m*x)*cos(x),x);

(%o3) %if((m - 1 # 0) %and (m + 1 # 0), 
(m - 1) sin((m + 1) x) + (- m - 1) sin((1 - m) x)
-------------------------------------------------, 
                       2
                    2 m  - 2
sin(2 x) + 2 x
--------------)
      4
(%i4) sublis([m=6],%);
                     5 sin(7 x) + 7 sin(5 x)
(%o4)                -----------------------
                               70
(%i5) conditional_integrate(exp(a*x^2+b*x),x);

                                  2
                                 b
                               - ---
                                 4 a      2 a x + b
                   sqrt(%pi) %e      erf(-----------)
                                         2 sqrt(- a)
(%o5) %if(a # 0, - ----------------------------------, 
                              2 sqrt(- a)
                                                         b x
                                                       %e
                                            %if(b # 0, -----, x))
                                                         b
```

<!-- category: Calculus -->
<!-- keywords: convert_to_signum -->
<!-- signatures: convert_to_signum(e) -->
### Function: convert_to_signum (e)

This function replaces subexpressions of the form `abs(q), unit_step(q), min(q1, q2, ..., qn)` and `max(q1, q2, ..., qn)` by equivalent
$signum$ terms.



```maxima
(%i1) load("abs_integrate")$
(%i2) map('convert_to_signum, [abs(x), unit_step(x), 
                               max(a,2), min(a,2)]);

                    signum(x) (signum(x) + 1)
(%o2) [x signum(x), -------------------------, 
                                2
  (a - 2) signum(a - 2) + a + 2  - (a - 2) signum(a - 2) + a + 2
  -----------------------------, -------------------------------]
                2                               2
```


To convert `unit_step` to signum form, the function
`convert_to_signum` uses $unit_step(x) = (1 + signum(x))/2$.


To use `load("abs_integrate")`.


Related functions `signum_to_abs`.

See also: `unit_step`, `signum_to_abs`.

<!-- category: Calculus -->
<!-- keywords: extra_definite_integration_methods -->
<!-- signatures: extra_definite_integration_methods -->
### Variable: extra_definite_integration_methods

Default value: `['abs_defint]`


The list `extra_definite_integration_methods` is a list of extra
functions for *definite* integration.  When `integrate` is
unable to find a definite integral, Maxima uses the methods in
`extra_definite_integration_methods` to attempt to determine an
antiderivative.


Each function `f` in `extra_definite_integration_methods`
should have the form `f(integrand, variable, lo, hi)`, where
`lo` and `hi` are the lower and upper limits of integration,
respectively.  The function `f` may either return `false` to
indicate failure, or it may return an expression involving an
integration noun form.  The integration methods are tried from the
first to the last member of `extra_definite_integration_methods`;
when no method returns an expression that does not involve an
integration noun form, the value of the integral is the last value
that does not fail (or a pure noun form if all methods fail).


Related options `extra_integration_methods`.


To use `load("abs_integrate")`.

See also: `integrate`, `extra_integration_methods`.

<!-- category: Calculus -->
<!-- keywords: extra_integration_methods -->
<!-- signatures: extra_integration_methods -->
### Variable: extra_integration_methods

Default value: `['signum_int, 'abs_integrate_use_if]`


The list `extra_integration_methods` is a list of functions for
integration.  When `integrate` is unable to find an
antiderivative, Maxima uses the methods in
`extra_integration_methods` to attempt to determine an
antiderivative.


Each function `f` in `extra_integration_methods` should have
the form `f(integrand, variable)`.  The function `f` may
either return `false` to indicate failure, or it may return an
expression involving an integration noun form.  The integration methods
are tried from the first to the last member of
`extra_integration_methods`; when no method returns an expression
that does not involve an integration noun form, the value of the
integral is the last value that does not fail (or a pure noun form if
all methods fail).


When the function `abs_integrate_use_if` is successful, it returns
a conditional expression; for example



```maxima
(%i1) load("abs_integrate")$
(%i2) integrate(1/(1 + abs(x+1) + abs(x-1)),x);
                           log(1 - 2 x)            2
(%o2) %if(- (x + 1) > 0, - ------------ + log(3) - -, 
                                2                  3
                                   x   log(3)   1  log(2 x + 1)
                %if(- (x - 1) > 0, - + ------ - -, ------------))
                                   3     2      3       2
(%i3) integrate(exp(-abs(x-1) - abs(x)),x);
                     2 x - 1
                   %e              - 1
(%o3) %if(- x > 0, --------- - 2 %e   , 
                       2
                                               - 1      1 - 2 x
                                   - 1     3 %e       %e
              %if(- (x - 1) > 0, %e    x - -------, - ---------))
                                              2           2
```


For definite integration, these conditional expressions can cause trouble:



```maxima
(%i4) integrate(exp(-abs(x-1) - abs(x)),x, minf,inf);
                               - 1    2 x
                             %e    (%e    - 4)
(%o4) limit     %if(- x > 0, -----------------, 
      x -> inf-                      2
                     - 1                1 - 2 x
                   %e    (2 x - 3)    %e
%if(- (x - 1) > 0, ---------------, - ---------))
                          2               2
                             - 1    2 x
                           %e    (%e    - 4)
 - limit      %if(- x > 0, -----------------, 
   x -> minf+                      2
                     - 1                1 - 2 x
                   %e    (2 x - 3)    %e
%if(- (x - 1) > 0, ---------------, - ---------))
                          2               2
```


For such definite integrals, try disallowing the method
`abs_integrate_use_if`:



```maxima
(%i5) integrate(exp(-abs(x-1) - abs(x)),x, minf,inf),
          extra_integration_methods : ['signum_int];
                                 - 1
(%o5)                        2 %e
```


Related options `extra_definite_integration_methods`.


To use `load("abs_integrate")`

See also: `integrate`, `extra_definite_integration_methods`.

<!-- category: Calculus -->
<!-- keywords: intfudu -->
<!-- signatures: intfudu(e, x) -->
### Function: intfudu (e, x)

This function uses the derivative divides rule for integrands of the
form $f(w(x)) * diff(w(x),x)$.  When `infudu` is unable to find
an antiderivative, it returns false.



```maxima
(%i1) load("abs_integrate")$
(%i2) intfudu(cos(x^2) * x,x);
                                  2
                             sin(x )
(%o2)                        -------
                                2
(%i3) intfudu(x * sqrt(1+x^2),x);
                             2     3/2
                           (x  + 1)
(%o3)                      -----------
                                3
(%i4) intfudu(x * sqrt(1 + x^4),x);
(%o4)                         false
```


For the last example, the derivative divides rule fails, so
`intfudu` returns false.


A hashed array `intable` contains the antiderivative data.  To append a
fact to the hash table, say $integrate(f) = g$, do this:



```maxima
(%i5) intable[f] : lambda([u],  [g(u),diff(u,%voi)]);
(%o5)          lambda([u], [g(u), diff(u, %voi)])
(%i6) intfudu(f(z),z);
(%o6)                         g(z)
(%i7) intfudu(f(w(x)) * diff(w(x),x),x);
(%o7)                        g(w(x))
```


An alternative to calling `intfudu` directly is to use the 
`extra_integration_methods` mechanism; an example:






```maxima
(%i1) load("abs_integrate")$
(%i2) load("basic")$
(%i3) load("partition.mac")$

(%i4) integrate(bessel_j(1,x^2) * x,x);
                                       2
                          bessel_j(0, x )
(%o4)                   - ---------------
                                 2
(%i5) push('intfudu, extra_integration_methods)$

(%i6) integrate(bessel_j(1,x^2) * x,x);
                                       2
                          bessel_j(0, x )
(%o6)                   - ---------------
                                 2
```


To use `load("partition")`.


Additional documentation

[http://www.cs.berkeley.edu/~fateman/papers/partition.pdf]().


Related functions `intfugudu`.

See also: `extra_integration_methods`, `intfugudu`.

<!-- category: Calculus -->
<!-- keywords: intfugudu -->
<!-- signatures: intfugudu(e, x) -->
### Function: intfugudu (e, x)

This function uses the derivative divides rule for integrands of the
form $f(w(x)) * g(w(x)) * diff(w(x),x)$.  When `infugudu` is
unable to find an antiderivative, it returns false.



```maxima
(%i1) load("abs_integrate")$
(%i2) diff(jacobi_sn(x,2/3),x);
                              2               2
(%o2)            jacobi_cn(x, -) jacobi_dn(x, -)
                              3               3
(%i3) intfugudu(%,x);
                                      2
(%o3)                    jacobi_sn(x, -)
                                      3
(%i4) diff(jacobi_dn(x^2,a),x);
                               2                2
(%o4)       - 2 a x jacobi_cn(x , a) jacobi_sn(x , a)
(%i5) intfugudu(%,x);
                                   2
(%o5)                   jacobi_dn(x , a)
```


For a method for automatically calling `infugudu` from `integrate`,
see the documentation for `intfudu`.


To use `load("partition")`.


Additional documentation

[http://www.cs.berkeley.edu/~fateman/papers/partition.pdf]()


Related functions `intfudu`.

See also: `intfudu`.

<!-- category: Calculus -->
<!-- keywords: signum_to_abs -->
<!-- signatures: signum_to_abs(e) -->
### Function: signum_to_abs (e)

This function replaces subexpressions of the form $q signum(q)$ by
$abs(q)$.  Before it does these substitutions, it replaces
subexpressions of the form $signum(p) * signum(q)$ by
$signum(p * q)$; examples:



```maxima
(%i1) load("abs_integrate")$
(%i2) map('signum_to_abs, [x * signum(x), 
                           x * y * signum(x)* signum(y)/2]);
                              abs(x) abs(y)
(%o2)                [abs(x), -------------]
                                    2
```


To use `load("abs_integrate")`.

<!-- category: Calculus -->
<!-- keywords: simp_assuming -->
<!-- signatures: simp_assuming(e, f_1, f_2, ..., f_n) -->
### Function: simp_assuming (e, f_1, f_2, ..., f_n)

Appended the facts $f_1, f_2, ..., f_n$ to the current context and
simplify $e$.  The facts are removed before returning the simplified
expression $e$.



```maxima
(%i1) load("abs_integrate")$
(%i2) simp_assuming(x + abs(x), x < 0);
(%o2)                           0
```


The facts in the current context aren’t ignored:



```maxima
(%i3) assume(x > 0)$
(%i4) simp_assuming(x + abs(x),x < 0);
(%o4)                          2 x
```


Since `simp_assuming` is a macro, effectively `simp_assuming` quotes
is arguments; this allows



```maxima
(%i5) simp_assuming(asksign(p), p < 0);
(%o5)                          neg
```


To use `load("abs_integrate")`.

