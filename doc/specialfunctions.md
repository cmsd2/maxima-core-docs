## SpecialFunctions

### Function: %f (p, q, [a],[b],z)

The 
$_{p}F_{q}(a_1,a_2,...,a_p;b_1,b_2,...,b_q;z)$
hypergeometric function,
where *a* a list of length *p* and 
*b* a list of length *q*.

### Function: %m (k, u, z)

Whittaker M function ([https://personal.math.ubc.ca/~cbm/aands/page_505.htmA&S eqn 13.1.32]()):



$$M_{\kappa,\mu}(z) = e^{-{1\over 2}z} z^{{1\over 2} + \mu} M\left({1\over 2} + \mu - \kappa, 1 + 2\mu, z\right)$$


$$M_{\kappa,\mu}(z) = e^{-{1\over 2}z} z^{{1\over 2} + \mu} M\left({1\over 2} + \mu - \kappa, 1 + 2\mu, z\right)$$



where $M(a,b,z)$ is Kummer’s solution of the confluent hypergeometric equation.


This can also be expressed by the series ([https://dlmf.nist.gov/13.14.E6DLMF 13.14.E6]()):

$$M_{\kappa,\mu}(z) = e^{-{1\over 2} z} z^{{1\over 2} + \mu} \sum_{s=0}^{\infty} {\left({1\over 2} + \mu - \kappa\right)_s \over (1 + 2\mu)_s s!} z^s$$


$$M_{\kappa,\mu}(z) = e^{-{1\over 2} z} z^{{1\over 2} + \mu}
\sum_{s=0}^{\infty} {\left({1\over 2} + \mu - \kappa\right)_s \over (1 + 2\mu)_s s!} z^s$$

### Function: %s (u, v, z)

Lommel’s little
$s_{\mu,\nu}(z)$
function.  
([https://dlmf.nist.gov/11.9.E3DLMF 11.9.E3]())(G&R 8.570.1).


This Lommel function is the particular solution of the inhomogeneous
Bessel differential equation:



$${d^2\over dz^2} + {1\over z}{dw\over dz} + \left(1-{\nu^2\over z^2}\right) w = z^{\mu-1}$$


$${d^2\over dz^2} + {1\over z}{dw\over dz} + \left(1-{\nu^2\over z^2}\right) w = z^{\mu-1}$$



This can be defined by the series



$$s_{\mu,\nu}(z) = z^{\mu+1}\sum_{k=0}^{\infty} (-1)^k {z^{2k}\over a_{k+1}(\mu, \nu)}$$


$$s_{\mu,\nu}(z) = z^{\mu+1}\sum_{k=0}^{\infty} (-1)^k {z^{2k}\over a_{k+1}(\mu, \nu)}$$



where



$$a_k(\mu,\nu) = \prod_{m=1}^k \left(\left(\mu + 2m-1\right)^2-\nu^2\right) = 4^k\left(\mu-\nu+1\over 2\right)_k \left(\mu+\nu+1\over 2\right)_k$$


$$a_k(\mu,\nu) = \prod_{m=1}^k \left(\left(\mu + 2m-1\right)^2-\nu^2\right) = 4^k\left(\mu-\nu+1\over 2\right)_k \left(\mu+\nu+1\over 2\right)_k$$

### Function: %w (k, u, z)

Whittaker W function ([https://personal.math.ubc.ca/~cbm/aands/page_505.htmA&S eqn 13.1.33]()):

$$W_{\kappa,\mu}(z) = e^{-{1\over 2}z} z^{{1\over 2} + \mu} U\left({1\over 2} + \mu - \kappa, 1+2\mu,z\right)$$


$$W_{\kappa,\mu}(z) = e^{-{1\over 2}z} z^{{1\over 2} + \mu} U\left({1\over 2} + \mu - \kappa, 1+2\mu,z\right)$$




where $U(a,b,z)$ is Kummer’s second solution of the confluent hypergeometric equation.

### Function: airy_ai (x)

The Airy function 
${\rm Ai}(x).$
See [https://personal.math.ubc.ca/~cbm/aands/page_446.htmA&S eqn 10.4.2]() and [https://dlmf.nist.gov/9DLMF 9]().


See also `airy_bi`, `airy_dai`, and `airy_005fdbi`.

See also: `airy_bi`, `airy_dai`, `airy_dbi`.

### Function: airy_bi (x)

The Airy function 
${\rm Bi}(x).$
See [https://personal.math.ubc.ca/~cbm/aands/page_446.htmA&S eqn 10.4.3]() and  [https://dlmf.nist.gov/9DLMF 9]().


See `airy_ai`, and `airy_005fdbi`.

See also: `airy_ai`, `airy_dbi`.

### Function: airy_dai (x)

The derivative of the Airy function 
${\rm Ai}(x):$




$${\rm airy\_dai}(x) = {d\over dx}{\rm Ai}(x)$$


$${\rm airy\_dai}(x) = {d\over dx}{\rm Ai}(x)$$

 

See `airy_005fai`.

See also: `airy_ai`.

### Function: airy_dbi (x)

The derivative of the Airy function 
${\rm Bi}(x):$




$${\rm airy\_dbi}(x) = {d\over dx}{\rm Bi}(x)$$


$${\rm airy\_dbi}(x) = {d\over dx}{\rm Bi}(x)$$



See `airy_ai`, and `airy_005fbi`.

See also: `airy_ai`, `airy_bi`.

### Function: bessel_i (v, z)

The modified Bessel function of the first kind of order $v$ and argument
$z$. See [https://personal.math.ubc.ca/~cbm/aands/page_375.htmA&S eqn 9.6.10]() and [https://dlmf.nist.gov/10.25.E2DLMF 10.25.E2]().


`bessel_i` is defined as

$$I_v(z) = \sum_{k=0}^{\infty } {{1\over{k!\,\Gamma \left(v+k+1\right)}} {\left(z\over 2\right)^{v+2\,k}}}$$


$$I_v(z) = \sum_{k=0}^{\infty } {{1\over{k!\,\Gamma
 \left(v+k+1\right)}} {\left(z\over 2\right)^{v+2\,k}}}$$




although the infinite series is not used for computations.


When `besselexpand` is `true`, `bessel_i` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.

See also: `bessel_i`, `besselexpand`, `true`.

### Function: bessel_j (v, z)

The Bessel function of the first kind of order $v$ and argument $z$.
See [https://personal.math.ubc.ca/~cbm/aands/page_360.htmA&S eqn 9.1.10]() and [https://dlmf.nist.gov/10.2.E2DLMF 10.2.E2]().


`bessel_j` is defined as



$$J_v(z) = \sum_{k=0}^{\infty }{{{\left(-1\right)^{k}\,\left(z\over 2\right)^{v+2\,k} }\over{k!\,\Gamma\left(v+k+1\right)}}}$$


$$J_v(z) = \sum_{k=0}^{\infty }{{{\left(-1\right)^{k}\,\left(z\over 2\right)^{v+2\,k}
 }\over{k!\,\Gamma\left(v+k+1\right)}}}$$



although the infinite series is not used for computations.


When `besselexpand` is `true`, `bessel_j` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.

See also: `bessel_j`, `besselexpand`, `true`.

### Function: bessel_k (v, z)

The modified Bessel function of the second kind of order $v$ and argument
$z$. See [https://personal.math.ubc.ca/~cbm/aands/page_375.htmA&S eqn 9.6.2]() and [https://dlmf.nist.gov/10.27.E4DLMF 10.27.E4]().


`bessel_k` is defined as

$$K_v(z) = {1\over 2} \pi\, {I_{-v}(z)-I_{v}(z) \over \sin v\pi}$$


$$K_v(z) = {1\over 2} \pi\, {I_{-v}(z)-I_{v}(z) \over \sin v\pi}$$




when $v$ is not an integer.  If $v$ is an integer $n$,
then the limit as $v$ approaches $n$ is taken.


When `besselexpand` is `true`, `bessel_k` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.

See also: `bessel_k`, `besselexpand`, `true`.

### Function: bessel_y (v, z)

The Bessel function of the second kind of order $v$ and argument $z$.
See [https://personal.math.ubc.ca/~cbm/aands/page_358.htmA&S eqn 9.1.2]() and [https://dlmf.nist.gov/10.2.E3DLMF 10.2.E3]().


`bessel_y` is defined as

$$Y_v(z) = {{\cos(\pi v)\, J_v(z) - J_{-v}(z)}\over{\sin{\pi v}}}$$


$$Y_v(z) = {{\cos(\pi v)\, J_v(z) - J_{-v}(z)}\over{\sin{\pi v}}}$$




when $v$ is not an integer.  When $v$ is an integer $n$,
the limit as $v$ approaches $n$ is taken.


When `besselexpand` is `true`, `bessel_y` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.

See also: `bessel_y`, `besselexpand`, `true`.

### Variable: besselexpand

Default value: `false`



Controls expansion of the Bessel, Hankel and Struve functions
when the order is half of
an odd integer.  In this case, the functions can be expanded
in terms of other elementary functions.  When `besselexpand` is `true`,
the Bessel function is expanded.












```maxima
maxima
(%i1) besselexpand: false$

(%i2) bessel_j (3/2, z);
                                  3
(%o2)                    bessel_j(-, z)
                                  2

(%i3) besselexpand: true$

(%i4) bessel_j (3/2, z);
                                 sin(z)   cos(z)
                sqrt(2) sqrt(z) (------ - ------)
                                    2       z
                                   z
(%o4)           ---------------------------------
                            sqrt(%pi)


(%i5) bessel_y(3/2,z);
                                  sin(z)   cos(z)
               sqrt(2) sqrt(z) (- ------ - ------)
                                    z         2
                                             z
(%o5)          -----------------------------------
                            sqrt(%pi)


(%i6) bessel_i(3/2,z);
                                cosh(z)   sinh(z)
               sqrt(2) sqrt(z) (------- - -------)
                                   z         2
                                            z
(%o6)          -----------------------------------
                            sqrt(%pi)


(%i7) bessel_k(3/2,z);
                                1        - z
                     sqrt(%pi) (- + 1) %e
                                z
(%o7)                -----------------------
                         sqrt(2) sqrt(z)
```

See also: `false`, `besselexpand`, `true`.

### Function: beta (a, b)

The beta function is defined as

$${\rm B}(a, b) = {{\Gamma(a) \Gamma(b)}\over{\Gamma(a+b)}}$$


$${\rm B}(a, b) = {{\Gamma(a) \Gamma(b)}\over{\Gamma(a+b)}}$$



([https://dlmf.nist.gov/5.12.E1DLMF 5.12.E1]() and [https://personal.math.ubc.ca/~cbm/aands/page_258.htmA&S eqn 6.2.1]()).


Maxima simplifies the beta function for positive integers and rational 
numbers, which sum to an integer. When `beta_args_sum_to_integer` is 
`true`, Maxima simplifies also general expressions which sum to an integer. 


For *a* or *b* equal to zero the beta function is not defined.


In general the beta function is not defined for negative integers as an 
argument. The exception is for *a=-n*, *n* a positive integer 
and *b* a positive integer with `b<=n`, it is possible to define an
analytic continuation. Maxima gives for this case a result.


When `beta_expand` is `true`, expressions like `beta` and 
`beta` or `beta`
and `beta` with `n` 
an integer are simplified.


Maxima can evaluate the beta function for real and complex values in float and 
bigfloat precision. For numerical evaluation Maxima uses `log_gamma`:



```maxima
- log_gamma(b + a) + log_gamma(b) + log_gamma(a)
         %e
```


Maxima knows that the beta function is symmetric and has mirror symmetry.


Maxima knows the derivatives of the beta function with respect to *a* or 
*b*.


To express the beta function as a ratio of gamma functions see `makegamma`. 


Examples:


Simplification, when one of the arguments is an integer:






```maxima
maxima

(%i1) [beta(2,3),beta(2,1/3),beta(2,a)];
                        1   9      1
(%o1)                  [--, -, ---------]
                        12  4  a (a + 1)
```


Simplification for two rational numbers as arguments which sum to an integer:






```maxima
maxima

(%i1) [beta(1/2,5/2),beta(1/3,2/3),beta(1/4,3/4)];
                   3 %pi   2 %pi
(%o1)             [-----, -------, sqrt(2) %pi]
                     8    sqrt(3)
```


When setting `beta_args_sum_to_integer` to `true` more general 
expression are simplified, when the sum of the arguments is an integer:







```maxima
maxima
(%i1) beta_args_sum_to_integer:true$

(%i2) beta(a+1,-a+2);
                         %pi (a - 1) a
(%o2)                  ------------------
                       2 sin(%pi (2 - a))
```


The possible results, when one of the arguments is a negative integer: 






```maxima
maxima

(%i1) [beta(-3,1),beta(-3,2),beta(-3,3)];
                             1  1    1
(%o1)                     [- -, -, - -]
                             3  6    3
```


`beta` or `beta` with `n` an integer simplifies when 
`beta_expand` is `true`:







```maxima
maxima
(%i1) beta_expand:true$

(%i2) [beta(a+1,b),beta(a-1,b),beta(a+1,b)/beta(a,b+1)];
             a beta(a, b)  beta(a, b) (b + a - 1)  a
(%o2)       [------------, ----------------------, -]
                b + a              a - 1           b
```


Beta is not defined, when one of the arguments is zero:





beta: expected nonzero arguments; found 0, b
 – an error. To debug this try: debugmode(true);


```maxima
maxima
(%i1) beta(0,b);
```


Numerical evaluation for real and complex arguments in float or bigfloat
precision:









```maxima
maxima

(%i1) beta(2.5,2.3);
(%o1)                  0.08694748611299981


(%i2) beta(2.5,1.4+%i);
(%o2)     0.06401449507966957 - 0.15020780532864159 %i


(%i3) beta(2.5b0,2.3b0);
(%o3)                 8.694748611299965b-2


(%i4) beta(2.5b0,1.4b0+%i);
(%o4)    6.401449507966939b-2 - 1.502078053286414b-1 %i
```


Beta is symmetric and has mirror symmetry:








```maxima
maxima

(%i1) beta(a,b)-beta(b,a);
(%o1)                           0

(%i2) declare(a,complex,b,complex)$

(%i3) conjugate(beta(a,b));
(%o3)           beta(conjugate(a), conjugate(b))
```


The derivative of the beta function wrt `a`:






```maxima
maxima

(%i1) diff(beta(a,b),a);
(%o1)         - beta(a, b) (psi (b + a) - psi (a))
                               0             0
```

See also: `beta_args_sum_to_integer`, `true`, `beta_expand`, `beta`, `log_gamma`, `makegamma`.

### Variable: beta_args_sum_to_integer

Default value: false


When `beta_args_sum_to_integer` is `true`, Maxima simplifies 
`beta`, when the arguments *a* and *b* sum to an integer.


`beta` for examples.

See also: `beta_args_sum_to_integer`, `true`, `beta`.

### Variable: beta_expand

Default value: false


When `beta_expand` is `true`, `beta` and related 
functions are expanded for arguments like $a+n$ or $a-n$, 
where $n$ is an integer.


`beta` for examples.

See also: `beta_expand`, `true`, `beta`.

### Function: beta_incomplete (a, b, z)

The basic definition of the incomplete beta function
([https://dlmf.nist.gov/8.17.E1DLMF 8.17.E1]() and [https://personal.math.ubc.ca/~cbm/aands/page_263.htmA&S eqn 6.6.1]()) is



$${\rm B}_z(a,b) = \int_0^z t^{a-1}(1-t)^{b-1}\; dt$$


$${\rm B}_z(a,b) = \int_0^z t^{a-1}(1-t)^{b-1}\; dt$$














This definition is possible for 
${\rm Re}(a) > 0$
and 
${\rm Re}(b) > 0$
and 
$|z| < 1.$
For other values the incomplete beta function can be 
defined through a generalized hypergeometric function:



```maxima
gamma(a) hypergeometric_generalized([a, 1 - b], [a + 1], z) z
```


(See [https://functions.wolfram.com/GammaBetaErf/Beta3/]() for a complete definition of the incomplete beta
function.)


For negative integers $a = -n$ and positive integers $b=m$
with 
$m \le n$
the incomplete beta function is defined through



$$z^{n-1}\sum_{k=0}^{m-1} {{(1-m)_k z^k} \over {k! (n-k)}}$$


$$z^{n-1}\sum_{k=0}^{m-1} {{(1-m)_k z^k} \over {k! (n-k)}}$$












Maxima uses this definition to simplify `beta_incomplete` for *a* a 
negative integer.


For *a* a positive integer, `beta_incomplete` simplifies for any 
argument *b* and *z* and for *b* a positive integer for any 
argument *a* and *z*, with the exception of *a* a negative integer.


For $z=0$ and 
${\rm Re}(a) > 0,$
`beta_incomplete` has the 
specific value zero. For $z=1$ and 
${\rm Re}(b) > 0,$
`beta_incomplete` simplifies to the beta function `beta`.


Maxima evaluates `beta_incomplete` numerically for real and complex values 
in float or bigfloat precision. For the numerical evaluation an expansion of the 
incomplete beta function in continued fractions is used.


When the option variable `beta_expand` is `true`, Maxima expands
expressions like `beta_005fincomplete` and
`beta_005fincomplete` where $n$ is a positive integer.


Maxima knows the derivatives of `beta_incomplete` with respect to the 
variables *a*, *b* and *z* and the integral with respect to the 
variable *z*.


Examples:


Simplification for *a* a positive integer:






```maxima
maxima

(%i1) beta_incomplete(2,b,z);
                                b
                     1 - (1 - z)  (b z + 1)
(%o1)                ----------------------
                           b (b + 1)
```


Simplification for *b* a positive integer:






```maxima
maxima

(%i1) beta_incomplete(a,2,z);
                                        a
                       (a (1 - z) + 1) z
(%o1)                  ------------------
                           a (a + 1)
```


Simplification for *a* and *b* a positive integer:






```maxima
maxima

(%i1) beta_incomplete(3,2,z);
                                        3
                       (3 (1 - z) + 1) z
(%o1)                  ------------------
                               12
```


*a* is a negative integer and $b\le -a$, Maxima simplifies:






```maxima
maxima

(%i1) beta_incomplete(-3,1,z);
                                1
(%o1)                        - ----
                                  3
                               3 z
```


For the specific values $z=0$ and $z=1$, Maxima simplifies:








```maxima
maxima
(%i1) assume(a>0,b>0)$

(%i2) beta_incomplete(a,b,0);
(%o2)                           0


(%i3) beta_incomplete(a,b,1);
(%o3)                      beta(a, b)
```


Numerical evaluation in float or bigfloat precision:








```maxima
maxima

(%i1) beta_incomplete(0.25,0.50,0.9);
(%o1)                   4.594959440269333

(%i2) fpprec:25$

(%i3) beta_incomplete(0.25,0.50,0.9b0);
(%o3)             4.594959440269324086971216b0
```


For $abs(z)>1$ `beta_incomplete` returns a complex result:






```maxima
maxima

(%i1) beta_incomplete(0.25,0.50,1.7);
(%o1)       5.244115108584249 - 1.4551804778784403 %i
```


Results for more general complex arguments:







```maxima
maxima

(%i1) beta_incomplete(0.25+%i,1.0+%i,1.7+%i);
(%o1)      2.7269606756625384 - 0.38311757042691896 %i


(%i2) beta_incomplete(1/2,5/4*%i,2.8+%i);
(%o2)      13.046496351687155 %i - 5.8020679562699975
```


Expansion, when `beta_expand` is `true`:







```maxima
maxima

(%i1) beta_incomplete(a+1,b,z),beta_expand:true;
                                                b  a
            a beta_incomplete(a, b, z)   (1 - z)  z
(%o1)       -------------------------- - -----------
                      b + a                 b + a


(%i2) beta_incomplete(a-1,b,z),beta_expand:true;
                                                      b  a - 1
      beta_incomplete(a, b, z) (- b - a + 1)   (1 - z)  z
(%o2) -------------------------------------- - ---------------
                      1 - a                         1 - a
```

 

Derivative and integral for `beta_incomplete`:








```maxima
maxima

(%i1) diff(beta_incomplete(a, b, z), z);
                              b - 1  a - 1
(%o1)                  (1 - z)      z


(%i2) integrate(beta_incomplete(a, b, z), z);
(%o2) beta_incomplete(a, b, z) z - beta_incomplete(a + 1, b, z)


(%i3) factor(diff(%, z));
(%o3)               beta_incomplete(a, b, z)
```

See also: `beta_incomplete`, `beta`, `beta_expand`, `true`.

### Function: beta_incomplete_generalized (a, b, z1, z2)

The basic definition of the generalized incomplete beta function is



$$\int_{z_1}^{z_2} t^{a-1}(1-t)^{b-1}\; dt$$


$$\int_{z_1}^{z_2} t^{a-1}(1-t)^{b-1}\; dt$$














Maxima simplifies `beta_incomplete_regularized` for *a* and *b* 
a positive integer.


For 
${\rm Re}(a) > 0$
and 
$z_1 = 0$
or 
$z_2 = 0,$
Maxima simplifies
`beta_incomplete_generalized` to `beta_incomplete`.
For 
${\rm Re}(b) > 0$
and 
$z_1 = 1$
or 
$z_2 = 1,$
Maxima simplifies to an 
expression with `beta` and `beta_incomplete`.


Maxima evaluates `beta_incomplete_regularized` for real and complex values 
in float and bigfloat precision.


When `beta_expand` is `true`, Maxima expands 
`beta_incomplete_generalized` for $a+n$ and $a-n$, *n* a 
positive integer.


Maxima knows the derivative of `beta_incomplete_generalized` with respect 
to the variables *a*, *b*, *z1*, and *z2* and the integrals with
respect to the variables *z1* and *z2*.


Examples:


Maxima simplifies `beta_incomplete_generalized` for *a* and *b* a 
positive integer:








```maxima
maxima

(%i1) beta_incomplete_generalized(2,b,z1,z2);
                   b                      b
           (1 - z1)  (b z1 + 1) - (1 - z2)  (b z2 + 1)
(%o1)      -------------------------------------------
                            b (b + 1)


(%i2) beta_incomplete_generalized(a,2,z1,z2);
                              a                      a
           (a (1 - z2) + 1) z2  - (a (1 - z1) + 1) z1
(%o2)      -------------------------------------------
                            a (a + 1)


(%i3) beta_incomplete_generalized(3,2,z1,z2);
              2      2                       2      2
      (1 - z1)  (3 z1  + 2 z1 + 1) - (1 - z2)  (3 z2  + 2 z2 + 1)
(%o3) -----------------------------------------------------------
                                  12
```


Simplification for specific values $z1=0$, $z2=0$, $z1=1$, or 
$z2=1$:










```maxima
maxima
(%i1) assume(a > 0, b > 0)$

(%i2) beta_incomplete_generalized(a,b,z1,0);
(%o2)              - beta_incomplete(a, b, z1)


(%i3) beta_incomplete_generalized(a,b,0,z2);
(%o3)              - beta_incomplete(a, b, z2)


(%i4) beta_incomplete_generalized(a,b,z1,1);
(%o4)        beta(a, b) - beta_incomplete(a, b, z1)


(%i5) beta_incomplete_generalized(a,b,1,z2);
(%o5)        beta_incomplete(a, b, z2) - beta(a, b)
```


Numerical evaluation for real arguments in float or bigfloat precision:








```maxima
maxima

(%i1) beta_incomplete_generalized(1/2,3/2,0.25,0.31);
(%o1)                  0.09638178086368676

(%i2) fpprec:32$

(%i3) beta_incomplete_generalized(1/2,3/2,0.25,0.31b0);
(%o3)         9.6381780863686935309170054689964b-2
```


Numerical evaluation for complex arguments in float or bigfloat precision:








```maxima
maxima

(%i1) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31);
(%o1)   - 0.09625463003205387 %i - 0.0033238477353540463

(%i2) fpprec:20$

(%i3) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31b0);
(%o3) - 9.6254630032054178691b-2 %i - 3.3238477353543591914b-3
```


Expansion for $a+n$ or $a-n$, *n* a positive integer, when 
`beta_expand` is `true`: 








```maxima
maxima
(%i1) beta_expand:true$

(%i2) beta_incomplete_generalized(a+1,b,z1,z2);
              b   a           b   a
      (1 - z1)  z1  - (1 - z2)  z2
(%o2) -----------------------------
                  b + a
                      a beta_incomplete_generalized(a, b, z1, z2)
                    + -------------------------------------------
                                         b + a


(%i3) beta_incomplete_generalized(a-1,b,z1,z2);
      beta_incomplete_generalized(a, b, z1, z2) (- b - a + 1)
(%o3) -------------------------------------------------------
                               1 - a
                                    b   a - 1           b   a - 1
                            (1 - z2)  z2      - (1 - z1)  z1
                          - -------------------------------------
                                            1 - a
```


Derivative wrt the variable *z1* and integrals wrt *z1* and *z2*:








```maxima
maxima

(%i1) diff(beta_incomplete_generalized(a,b,z1,z2),z1);
                               b - 1   a - 1
(%o1)                - (1 - z1)      z1


(%i2) integrate(beta_incomplete_generalized(a,b,z1,z2),z1);
(%o2) beta_incomplete_generalized(a, b, z1, z2) z1
                                  + beta_incomplete(a + 1, b, z1)


(%i3) integrate(beta_incomplete_generalized(a,b,z1,z2),z2);
(%o3) beta_incomplete_generalized(a, b, z1, z2) z2
                                  - beta_incomplete(a + 1, b, z2)
```

See also: `beta_incomplete_regularized`, `beta_incomplete_generalized`, `beta_incomplete`, `beta`, `beta_expand`, `true`.

### Function: beta_incomplete_regularized (a, b, z)

The regularized incomplete beta function ([https://dlmf.nist.gov/8.17.E2DLMF 8.17.E2]() and
[https://personal.math.ubc.ca/~cbm/aands/page_263.htmA&S eqn 6.6.2]()), defined as 



$$I_z(a,b) = {{\rm B}_z(a,b)\over {\rm B}(a,b)}$$


$$I_z(a,b) = {{\rm B}_z(a,b)\over {\rm B}(a,b)}$$









As for `beta_incomplete` this definition is not complete. See 
[https://functions.wolfram.com/GammaBetaErf/BetaRegularized/]() for a complete definition of
`beta_incomplete_regularized`.


`beta_incomplete_regularized` simplifies *a* or *b* a positive 
integer.


For $z=0$ and 
${\rm Re}(a)>0,$
`beta_incomplete_regularized` has 
the specific value 0. For $z=1$ and 
${\rm Re}(b) > 0,$
`beta_incomplete_regularized` simplifies to 1.


Maxima can evaluate `beta_incomplete_regularized` for real and complex 
arguments in float and bigfloat precision.


When `beta_expand` is `true`, Maxima expands 
`beta_incomplete_regularized` for arguments $a+n$ or $a-n$, 
where n is an integer.


Maxima knows the derivatives of `beta_incomplete_regularized` with respect 
to the variables *a*, *b*, and *z* and the integral with respect to 
the variable *z*.


Examples:


Simplification for *a* or *b* a positive integer:








```maxima
maxima

(%i1) beta_incomplete_regularized(2,b,z);
                                b
(%o1)                1 - (1 - z)  (b z + 1)


(%i2) beta_incomplete_regularized(a,2,z);
                                        a
(%o2)                  (a (1 - z) + 1) z


(%i3) beta_incomplete_regularized(3,2,z);
                                        3
(%o3)                  (3 (1 - z) + 1) z
```


For the specific values $z=0$ and $z=1$, Maxima simplifies:








```maxima
maxima
(%i1) assume(a>0,b>0)$

(%i2) beta_incomplete_regularized(a,b,0);
(%o2)                           0


(%i3) beta_incomplete_regularized(a,b,1);
(%o3)                           1
```


Numerical evaluation for real and complex arguments in float and bigfloat 
precision:











```maxima
maxima

(%i1) beta_incomplete_regularized(0.12,0.43,0.9);
(%o1)                  0.9114011367359802

(%i2) fpprec:32$

(%i3) beta_incomplete_regularized(0.12,0.43,0.9b0);
(%o3)         9.1140113673598029169207248506439b-1


(%i4) beta_incomplete_regularized(1+%i,3/3,1.5*%i);
(%o4)      0.2865367499935405 %i - 0.12299596333468409

(%i5) fpprec:20$

(%i6) beta_incomplete_regularized(1+%i,3/3,1.5b0*%i);
(%o6) 2.8653674999354031589b-1 %i - 1.2299596333468401976b-1
```


Expansion, when `beta_expand` is `true`:







```maxima
maxima

(%i1) beta_incomplete_regularized(a+1,b,z);
(%o1)       beta_incomplete_regularized(a + 1, b, z)


(%i2) beta_incomplete_regularized(a-1,b,z);
(%o2)       beta_incomplete_regularized(a - 1, b, z)
```


The derivative and the integral wrt *z*:







```maxima
maxima

(%i1) diff(beta_incomplete_regularized(a,b,z),z);
                              b - 1  a - 1
                       (1 - z)      z
(%o1)                  -------------------
                           beta(a, b)


(%i2) integrate(beta_incomplete_regularized(a,b,z),z);
(%o2) beta_incomplete_regularized(a, b, z) z
                       a beta_incomplete_regularized(a + 1, b, z)
                     - ------------------------------------------
                                         b + a
```

See also: `beta_incomplete`, `beta_incomplete_regularized`, `beta_expand`, `true`.

### Function: bffac (expr, n)

Bigfloat version of the factorial (shifted gamma)
function.  The second argument is how many digits to retain and return,
it’s a good idea to request a couple of extra.








```maxima
maxima

(%i1) bffac(1/2,16);
(%o1)                 8.862269254527584b-1


(%i2) (1/2)!,numer;
(%o2)                   0.886226925452758


(%i3) bffac(1/2,32);
(%o3)          8.862269254527580136490837416707b-1
```

### Function: bfpsi (n, z, fpprec)

`bfpsi` is the polygamma function of real argument *z* and
integer order *n*.  See `polygamma` for further
information.  `bfpsi0` is the digamma function.
`bfpsi0` is equivalent to
`bfpsi`.


These functions return bigfloat values.
*fpprec* is the bigfloat precision of the return value.














```maxima
maxima

(%i1) bfpsi0(1/3, 15);
(%o1)                 - 3.13203378002081b0


(%i2) bfpsi0(1/3, 32);
(%o2)         - 3.1320337800208063229964190742873b0


(%i3) bfpsi(0,1/3,32);
(%o3)         - 3.1320337800208063229964190742873b0


(%i4) psi[0](1/3);
                   3 log(3)      %pi
(%o4)            - -------- - --------- - %gamma
                      2       2 sqrt(3)


(%i5) float(%);
(%o5)                  - 3.132033780020806
```

See also: `bfpsi`, `polygamma`, `bfpsi0`.

### Function: cbffac (z, fpprec)

Complex bigfloat factorial.


`load ("bffac")` loads this function.







```maxima
maxima

(%i1) cbffac(1+%i,16);
(%o1)    3.430658398165453b-1 %i + 6.529654964201666b-1


(%i2) (1+%i)!,numer;
(%o2)      0.3430658398165453 %i + 0.6529654964201667
```

### Variable: expand_hypergeometric

Default value: `false`


When `true`, `hypergeometric` will return a polynomial if
the hypergeometric function represents a polynomial.

See also: `false`, `true`, `hypergeometric`.

### Function: gamma (z)

The basic definition of the gamma function ([https://dlmf.nist.gov/5.2.E1DLMF 5.2.E1]() and [https://personal.math.ubc.ca/~cbm/aands/page_255.htmA&S eqn 6.1.1]()) is



$$\Gamma\left(z\right)=\int_{0}^{\infty }{t^{z-1}\,e^ {- t }\;dt}$$


$$\Gamma\left(z\right)=\int_{0}^{\infty }{t^{z-1}\,e^ {- t }\;dt}$$



Maxima simplifies `gamma` for positive integer and positive and negative 
rational numbers. For half integral values the result is a rational number
times 
$\sqrt{\pi}.$
The simplification for integer values is controlled by 
`factlim`. For integers greater than `factlim` the numerical result of 
the factorial function, which is used to calculate `gamma`, will overflow. 
The simplification for rational numbers is controlled by `gammalim` to 
avoid internal overflow. See `factlim` and `gammalim`.


For negative integers `gamma` is not defined.


Maxima can evaluate `gamma` numerically for real and complex values in float
and bigfloat precision.


`gamma` has mirror symmetry.


When `gamma_expand` is `true`, Maxima expands `gamma` for 
arguments `z+n` and `z-n` where `n` is an integer.


Maxima knows the derivative of `gamma`.


Examples:


Simplification for integer, half integral, and rational numbers:








```maxima
maxima

(%i1) map('gamma,[1,2,3,4,5,6,7,8,9]);
(%o1)        [1, 1, 2, 6, 24, 120, 720, 5040, 40320]


(%i2) map('gamma,[1/2,3/2,5/2,7/2]);
                    sqrt(%pi)  3 sqrt(%pi)  15 sqrt(%pi)
(%o2)   [sqrt(%pi), ---------, -----------, ------------]
                        2           4            8


(%i3) map('gamma,[2/3,5/3,7/3]);
                                  2           1
                          2 gamma(-)  4 gamma(-)
                      2           3           3
(%o3)          [gamma(-), ----------, ----------]
                      3       3           9
```


Numerical evaluation for real and complex values:







```maxima
maxima

(%i1) map('gamma,[2.5,2.5b0]);
(%o1)       [1.329340388179137, 1.329340388179137b0]


(%i2) map('gamma,[1.0+%i,1.0b0+%i]);
(%o2) [0.49801566811835596 - 0.15494982830181073 %i, 
                  4.980156681183561b-1 - 1.549498283018107b-1 %i]
```


`gamma` has mirror symmetry:







```maxima
maxima
(%i1) declare(z,complex)$

(%i2) conjugate(gamma(z));
(%o2)                  gamma(conjugate(z))
```


Maxima expands `gamma` and `gamma`, when `gamma_expand` 
is `true`:







```maxima
maxima
(%i1) gamma_expand:true$

(%i2) [gamma(z+1),gamma(z-1),gamma(z+2)/gamma(z+1)];
                               gamma(z)
(%o2)             [z gamma(z), --------, z + 1]
                                z - 1
```


The derivative of `gamma`:






```maxima
maxima

(%i1) diff(gamma(z),z);
(%o1)                   psi (z) gamma(z)
                           0
```


See also `makegamma`.


The Euler-Mascheroni constant is `%gamma`.

See also: `gamma`, `factlim`, `gammalim`, `gamma_expand`, `true`, `makegamma`, `%gamma`.

### Variable: gamma_expand

Default value: `false`


`gamma_expand` controls expansion of `gamma_incomplete`.
When `gamma_expand` is `true`, `gamma_005fincomplete`
is expanded in terms of
`z`, `exp`, and `gamma_incomplete` or `erfc` when possible.












```maxima
maxima

(%i1) gamma_incomplete(2,z);
(%o1)                gamma_incomplete(2, z)


(%i2) gamma_expand:true;
(%o2)                         true


(%i3) gamma_incomplete(2,z);
                                    - z
(%o3)                     (z + 1) %e


(%i4) gamma_incomplete(3/2,z);
                       - z   sqrt(%pi) erfc(sqrt(z))
(%o4)        sqrt(z) %e    + -----------------------
                                        2


(%i5) gamma_incomplete(4/3,z);
                                             1
                            gamma_incomplete(-, z)
                1/3   - z                    3
(%o5)          z    %e    + ----------------------
                                      3


(%i6) gamma_incomplete(a+2,z);
       a               - z
(%o6) z  (z + a + 1) %e    + a (a + 1) gamma_incomplete(a, z)


(%i7) gamma_incomplete(a-2, z);
      gamma_incomplete(a, z)    a - 2         z            1
(%o7) ---------------------- - z      (--------------- + -----)
         (1 - a) (2 - a)               (a - 2) (a - 1)   a - 2
                                                              - z
                                                            %e
```

See also: `false`, `gamma_expand`, `gamma_incomplete`, `true`, `exp`, `erfc`.

### Function: gamma_incomplete (a, z)

The incomplete upper gamma function ([https://dlmf.nist.gov/8.2.E2DLMF 8.2.E2]() and [https://personal.math.ubc.ca/~cbm/aands/page_260.htmA&S eqn 6.5.3]()):



$$\Gamma\left(a , z\right)=\int_{z}^{\infty }{t^{a-1}\,e^ {- t }\;dt}$$


$$\Gamma\left(a , z\right)=\int_{z}^{\infty }{t^{a-1}\,e^ {- t }\;dt}$$



See also `gamma_expand` for controlling how
`gamma_incomplete` is expressed in terms of elementary functions
and `erfc`.


Also see the related functions `gamma_incomplete_regularized` and
`gamma_incomplete_generalized`.

See also: `gamma_expand`, `gamma_incomplete`, `erfc`, `gamma_incomplete_regularized`, `gamma_incomplete_generalized`.

### Function: gamma_incomplete_generalized (a, z1, z1)

The generalized incomplete gamma function.



$$\Gamma\left(a , z_{1}, z_{2}\right)=\int_{z_{1}}^{z_{2}}{t^{a-1}\,e^ {- t }\;dt}$$


$$\Gamma\left(a , z_{1}, z_{2}\right)=\int_{z_{1}}^{z_{2}}{t^{a-1}\,e^ {- t }\;dt}$$



Also see `gamma_incomplete` and `gamma_incomplete_regularized`.

See also: `gamma_incomplete`, `gamma_incomplete_regularized`.

### Function: gamma_incomplete_lower (a, z)

The lower incomplete gamma function ([https://dlmf.nist.gov/8.2.E1DLMF 8.2.E1]() and [https://personal.math.ubc.ca/~cbm/aands/page_260.htmA&S eqn 6.5.2]()):



$$\gamma\left(a , z\right)=\int_{0}^{z}{t^{a-1}\,e^ {- t }\;dt}$$


$$\gamma\left(a , z\right)=\int_{0}^{z}{t^{a-1}\,e^ {- t }\;dt}$$



See also `gamma_incomplete` (upper incomplete gamma function).

See also: `gamma_incomplete`.

### Function: gamma_incomplete_regularized (a, z)

The regularized incomplete upper gamma function ([https://dlmf.nist.gov/8.2.E4DLMF 8.2.E4]()):



$$Q\left(a , z\right)={{\Gamma\left(a , z\right)}\over{\Gamma\left(a\right)}}$$


$$Q\left(a , z\right)={{\Gamma\left(a , z\right)}\over{\Gamma\left(a\right)}}$$



See also `gamma_expand` for controlling how
`gamma_incomplete` is expressed in terms of elementary functions
and `erfc`.


Also see `gamma_incomplete`.

See also: `gamma_expand`, `gamma_incomplete`, `erfc`.

### Variable: gammalim

Default value: 10000



`gammalim` controls simplification of the gamma
function for integral and rational number arguments.  If the absolute
value of the argument is not greater than `gammalim`, then
simplification will occur.  Note that the `factlim` switch controls
simplification of the result of `gamma` of an integer argument as well.

See also: `gammalim`, `factlim`, `gamma`.

### Function: generalized_lambert_w (k, z)

The *k*-th branch of Lambert’s W function W(z) ([https://dlmf.nist.gov/4.13DLMF 4.13]()), the solution
of 
$z=W(z)e^{W(z)}.$


The principal branch, denoted 
$W_p(z)$
in DLMF, is `lambert_005fw` `=`
`generalized_005flambert_005fw`.


The other branch with real values, denoted 
$W_m(z)$
in DLMF, is `generalized_005flambert_005fw`.

See also: `lambert_w`, `generalized_lambert_w`.

### Function: hankel_1 (v, z)

The Hankel function of the first kind of order $v$ and argument $z$.
See [https://personal.math.ubc.ca/~cbm/aands/page_358.htmA&S eqn 9.1.3]() and [https://dlmf.nist.gov/10.4.E3DLMF 10.4.E3]().


`hankel_1` is defined as



$$H^{(1)}_v(z) = J_v(z) + i Y_v(z)$$


$$H^{(1)}_v(z) = J_v(z) + i Y_v(z)$$



Maxima evaluates `hankel_1` numerically for a complex order $v$ and 
complex argument $z$ in float precision. The numerical evaluation in 
bigfloat precision is not supported.


When `besselexpand` is `true`, `hankel_1` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.


Maxima knows the derivative of `hankel_1` wrt the argument $z$.


Examples:


Numerical evaluation:







```maxima
maxima

(%i1) hankel_1(1,0.5);
(%o1)      0.24226845767487384 - 1.4714723926702433 %i


(%i2) hankel_1(1,0.5+%i);
(%o2)     - 0.2558287994862166 %i - 0.23957560188301597
```


Expansion of `hankel_1` when `besselexpand` is `true`:






```maxima
maxima

(%i1) hankel_1(1/2,z),besselexpand:true;
               sqrt(2) sin(z) - sqrt(2) %i cos(z)
(%o1)          ----------------------------------
                       sqrt(%pi) sqrt(z)
```


Derivative of `hankel_1` wrt the argument $z$. The derivative wrt the 
order $v$ is not supported. Maxima returns a noun form:







```maxima
maxima

(%i1) diff(hankel_1(v,z),z);
             hankel_1(v - 1, z) - hankel_1(v + 1, z)
(%o1)        ---------------------------------------
                                2


(%i2) diff(hankel_1(v,z),v);
                       d
(%o2)                  -- (hankel_1(v, z))
                       dv
```

See also: `hankel_1`, `besselexpand`, `true`.

### Function: hankel_2 (v, z)

The Hankel function of the second kind of order $v$ and argument $z$.
See [https://personal.math.ubc.ca/~cbm/aands/page_358.htmA&S eqn 9.1.4]() and [https://dlmf.nist.gov/10.4.E3DLMF 10.4.E3]().


`hankel_2` is defined as



$$H^{(2)}_v(z) = J_v(z) - i Y_v(z)$$


$$H^{(2)}_v(z) = J_v(z) - i Y_v(z)$$



Maxima evaluates `hankel_2` numerically for a complex order $v$ and 
complex argument $z$ in float precision. The numerical evaluation in 
bigfloat precision is not supported.


When `besselexpand` is `true`, `hankel_2` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.


Maxima knows the derivative of `hankel_2` wrt the argument $z$.


For examples see `hankel_1`.

See also: `hankel_2`, `besselexpand`, `true`, `hankel_1`.

### Function: hgfred (a, b, t)

Simplify the generalized hypergeometric function in terms of other,
simpler, forms.  *a* is a list of numerator parameters and *b*
is a list of the denominator parameters. 


If `hgfred` cannot simplify the hypergeometric function, it returns
an expression of the form `_0025f` where *p* is
the number of elements in *a*, and *q* is the number of elements
in *b*.  This is the usual 
$_pF_q$
generalized hypergeometric
function. 









```maxima
maxima

(%i1) assume(not(equal(z,0)));
(%o1)                   [notequal(z, 0)]


(%i2) hgfred([v+1/2],[2*v+1],2*%i*z);
              v/2                               %i z
             4    bessel_j(v, z) gamma(v + 1) %e
(%o2)        ---------------------------------------
                                v
                               z


(%i3) hgfred([1,1],[2],z);
                            log(1 - z)
(%o3)                     - ----------
                                z


(%i4) hgfred([a,a+1/2],[3/2],z^2);
                        1 - 2 a          1 - 2 a
                 (z + 1)        - (1 - z)
(%o4)            -------------------------------
                          2 (1 - 2 a) z
```


It can be beneficial to load orthopoly too as the following example
shows.  Note that *L* is the generalized Laguerre polynomial.








```maxima
maxima
(%i1) load("orthopoly")$

(%i2) hgfred([-2],[a],z);
                           2
                          z        2 z
(%o2)                  --------- - --- + 1
                       a (a + 1)    a


(%i3) ev(%);
                           2
                          z        2 z
(%o3)                  --------- - --- + 1
                       a (a + 1)    a
```

See also: `hgfred`, `%f`.

### Function: hypergeometric (a1, ..., ap, b1, ..., bq, x)

The hypergeometric function. Unlike Maxima’s `%f` hypergeometric
function, the function `hypergeometric` is a simplifying
function; also, `hypergeometric` supports complex double and
big floating point evaluation. For the Gauss hypergeometric function,
that is $p = 2$ and $q = 1$, floating point evaluation
outside the unit circle is supported, but in general, it is not
supported.


When the option variable `expand_hypergeometric` is `true` (default
is `false`) and one of the arguments `a1` through `ap` is a
negative integer (a polynomial case), `hypergeometric` returns an
expanded polynomial. 


Examples:






```maxima
maxima

(%i1)  hypergeometric([],[],x);
                                 x
(%o1)                          %e
```


Polynomial cases automatically expand when `expand_hypergeometric` is true:







```maxima
maxima

(%i1) hypergeometric([-3],[7],x);
(%o1)             hypergeometric([- 3], [7], x)


(%i2) hypergeometric([-3],[7],x), expand_hypergeometric : true;
                        3       2
                       x     3 x    3 x
(%o2)                - --- + ---- - --- + 1
                       504    56     7
```


Both double float and big float evaluation is supported:








```maxima
maxima

(%i1) hypergeometric([5.1],[7.1 + %i],0.42);
(%o1)      1.3462507863753337 - 0.0559061414208204 %i


(%i2) hypergeometric([5,6],[8], 5.7 - %i);
(%o2)    0.007375824009774945 - 0.0010498136885786736 %i


(%i3) hypergeometric([5,6],[8], 5.7b0 - %i), fpprec : 30;
(%o3) 7.37582400977494674506442010824b-3
                          - 1.04981368857867315858055393376b-3 %i
```

See also: `%f`, `hypergeometric`, `expand_hypergeometric`, `true`, `false`.

### Function: hypergeometric_simp (e)

`hypergeometric_simp` simplifies hypergeometric functions
by applying `hgfred`
to the arguments of any hypergeometric functions in the expression *e*.


Only instances of `hypergeometric` are affected;
any `%f`, `%w`, and `%m` in the expression *e* are not affected.
Any unsimplified hypergeometric functions are returned unchanged
(instead of changing to `%f` as `hgfred` would).


`load("hypergeometric");` loads this function.


See also `hgfred`.


Examples:










```maxima
maxima
(%i1) load ("hypergeometric") $

(%i2) foo : [hypergeometric([1,1], [2], z), hypergeometric([1/2], [1], z)];
(%o2) [hypergeometric([1, 1], [2], z), 
                                                     1
                                     hypergeometric([-], [1], z)]
                                                     2


(%i3) hypergeometric_simp (foo);
                 log(1 - z)    z/2             z
(%o3)         [- ----------, %e    bessel_i(0, -)]
                     z                         2


(%i4) bar : hypergeometric([n], [m], z + 1);
(%o4)            hypergeometric([n], [m], z + 1)


(%i5) hypergeometric_simp (bar);
(%o5)            hypergeometric([n], [m], z + 1)
```

See also: `hypergeometric_simp`, `hgfred`, `hypergeometric`, `%f`, `%w`, `%m`.

### Function: inverse_jacobi_cd (u, m)

The inverse of the Jacobian elliptic function 
${\rm cd}(u,m).$
For 
$-1\le u \le 1,$
it can also be written ([https://dlmf.nist.gov/22.15.E15DLMF 22.15.E15]()):

$${\rm inverse\_jacobi\_cd}(u, m) = \int_u^1 {dt\over \sqrt{(1-t^2)(1-mt^2)}}$$


$${\rm inverse\_jacobi\_cd}(u, m) = \int_u^1 {dt\over \sqrt{(1-t^2)(1-mt^2)}}$$

### Function: inverse_jacobi_cs (u, m)

The inverse of the Jacobian elliptic function 
${\rm cs}(u,m).$
For all $u$ it can also be written ([https://dlmf.nist.gov/22.15.E23DLMF 22.15.E23]()):

$${\rm inverse\_jacobi\_cs}(u, m) = \int_u^{\infty} {dt\over \sqrt{(1+t^2)(t^2+(1-m))}}$$


$${\rm inverse\_jacobi\_cs}(u, m) = \int_u^{\infty} {dt\over \sqrt{(1+t^2)(t^2+(1-m))}}$$

### Function: inverse_jacobi_dc (u, m)

The inverse of the Jacobian elliptic function 
${\rm dc}(u,m).$
For 
$1 \le u,$
it can also be written ([https://dlmf.nist.gov/22.15.E18DLMF 22.15.E18]()):

$${\rm inverse\_jacobi\_dc}(u, m) = \int_1^u {dt\over \sqrt{(t^2-1)(t^2-m)}}$$


$${\rm inverse\_jacobi\_dc}(u, m) = \int_1^u {dt\over \sqrt{(t^2-1)(t^2-m)}}$$

### Function: inverse_jacobi_dn (u, m)

The inverse of the Jacobian elliptic function 
${\rm dn}(u,m).$
For 
$\sqrt{1-m}\le u \le 1,$
it can also be written ([https://dlmf.nist.gov/22.15.E14DLMF 22.15.E14]()):

$${\rm inverse\_jacobi\_dn}(u, m) = \int_u^1 {dt\over \sqrt{(1-t^2)(t^2-(1-m))}}$$


$${\rm inverse\_jacobi\_dn}(u, m) = \int_u^1 {dt\over \sqrt{(1-t^2)(t^2-(1-m))}}$$

### Function: inverse_jacobi_ds (u, m)

The inverse of the Jacobian elliptic function 
${\rm ds}(u,m).$
For 
$\sqrt{1-m}\le u,$
it can also be written ([https://dlmf.nist.gov/22.15.E22DLMF 22.15.E22]()):

$${\rm inverse\_jacobi\_ds}(u, m) = \int_u^{\infty} {dt\over \sqrt{(t^2+m)(t^2-(1-m))}}$$


$${\rm inverse\_jacobi\_ds}(u, m) = \int_u^{\infty} {dt\over \sqrt{(t^2+m)(t^2-(1-m))}}$$

### Function: inverse_jacobi_nc (u, m)

The inverse of the Jacobian elliptic function 
${\rm nc}(u,m).$
For 
$1\le u,$
it can also be written ([https://dlmf.nist.gov/22.15.E19DLMF 22.15.E19]()):

$${\rm inverse\_jacobi\_nc}(u, m) = \int_1^u {dt\over \sqrt{(t^2-1)(m+(1-m)t^2)}}$$


$${\rm inverse\_jacobi\_nc}(u, m) = \int_1^u {dt\over \sqrt{(t^2-1)(m+(1-m)t^2)}}$$

### Function: inverse_jacobi_nd (u, m)

The inverse of the Jacobian elliptic function 
${\rm nd}(u,m).$
For 
$1\le u \le 1/\sqrt{1-m},$
it can also be written ([https://dlmf.nist.gov/22.15.E17DLMF 22.15.E17]()):

$${\rm inverse\_jacobi\_nd}(u, m) = \int_1^u {dt\over \sqrt{(t^2-1)(1-(1-m)t^2)}}$$


$${\rm inverse\_jacobi\_nd}(u, m) = \int_1^u {dt\over \sqrt{(t^2-1)(1-(1-m)t^2)}}$$

### Function: inverse_jacobi_ns (u, m)

The inverse of the Jacobian elliptic function 
${\rm ns}(u,m).$
For 
$1 \le u,$
it can also be written ([https://dlmf.nist.gov/22.15.E121DLMF 22.15.E121]()):

$${\rm inverse\_jacobi\_ns}(u, m) = \int_u^{\infty} {dt\over \sqrt{(1-t^2)(t^2-m)}}$$


$${\rm inverse\_jacobi\_ns}(u, m) = \int_u^{\infty} {dt\over \sqrt{(1-t^2)(t^2-m)}}$$

### Function: inverse_jacobi_sc (u, m)

The inverse of the Jacobian elliptic function 
${\rm sc}(u,m).$
For all $u$ it can also be written ([https://dlmf.nist.gov/22.15.E20DLMF 22.15.E20]()):

$${\rm inverse\_jacobi\_sc}(u, m) = \int_0^u {dt\over \sqrt{(1+t^2)(1+(1-m)t^2)}}$$


$${\rm inverse\_jacobi\_sc}(u, m) = \int_0^u {dt\over \sqrt{(1+t^2)(1+(1-m)t^2)}}$$

### Function: inverse_jacobi_sd (u, m)

The inverse of the Jacobian elliptic function 
${\rm sd}(u,m).$
For 
$-1/\sqrt{1-m}\le u \le 1/\sqrt{1-m},$
it can also be written ([https://dlmf.nist.gov/22.15.E16DLMF 22.15.E16]()):

$${\rm inverse\_jacobi\_sd}(u, m) = \int_0^u {dt\over \sqrt{(1-(1-m)t^2)(1+mt^2)}}$$


$${\rm inverse\_jacobi\_sd}(u, m) = \int_0^u {dt\over \sqrt{(1-(1-m)t^2)(1+mt^2)}}$$

### Function: jacobi_am (u, m)

The Jacobi amplitude function, `jacobi_am`, is defined implicitly by (see
[http://functions.wolfram.com/09.24.02.0001.01]())
$z = {\rm am}(w, m)$
where $w = F(z,m)$ where $F(z,m)$ is the incomplete elliptic
integral of the first kind (`elliptic_005ff`).  It is defined for
all real and complex values of $z$ and $m$.  In particular
for real $z$ and $m$ with $|m|<1$,
${\rm am}(z,m)$
maps the entire real line to the entire real line.  For other values
of $z$ and $m$, the following relationship is used:
${\rm am}(z,m) = \sin^{-1}({\rm jacobi\_sn}(z, m)).$


Some examples:










```maxima
maxima

(%i1) jacobi_am(z,0);
(%o1)                           z


(%i2) jacobi_am(z,1);
                                 z    %pi
(%o2)                   2 atan(%e ) - ---
                                       2


(%i3) jacobi_am(0,m);
(%o3)                           0


(%i4) jacobi_am(100, .5);
(%o4)                   84.70311272411382


(%i5) jacobi_am(0.5, 1.5);
(%o5)                  0.4707197897046991


(%i6) jacobi_am(1.5b0, 1.5b0+%i);
(%o6)    9.340542168700782b-1 - 3.723960452146071b-1 %i
```






```maxima
maxima

(%i1) plot2d([jacobi_am(x,.4),jacobi_am(x,.7),jacobi_am(x,.99),jacobi_am(x,.999999)],[x,0,10*%pi]);
(%o1)                         false
```


Compare this plot with the plot from [https://dlmf.nist.gov/22.16.ivDLMF 22.16.iv]():


(Figure jacobi_am)

See also: `jacobi_am`, `elliptic_f`.

### Function: jacobi_cd (u, m)

The Jacobian elliptic function 
${\rm cd}(u,m) = {\rm cn}(u,m)/{\rm dn}(u,m).$

### Function: jacobi_cn (u, m)

The Jacobian elliptic function 
${\rm cn}(u,m).$

### Function: jacobi_cs (u, m)

The Jacobian elliptic function 
${\rm cs}(u,m) = {\rm cn}(u,m)/{\rm sn}(u,m).$

### Function: jacobi_dc (u, m)

The Jacobian elliptic function 
${\rm dc}(u,m) = {\rm dn}(u,m)/{\rm cn}(u,m).$

### Function: jacobi_dn (u, m)

The Jacobian elliptic function 
${\rm dn}(u,m).$

### Function: jacobi_ds (u, m)

The Jacobian elliptic function 
${\rm ds}(u,m) = {\rm dn}(u,m)/{\rm sn}(u,m).$

### Function: jacobi_nc (u, m)

The Jacobian elliptic function 
${\rm nc}(u,m) = 1/{\rm cn}(u,m).$

### Function: jacobi_nd (u, m)

The Jacobian elliptic function 
${\rm nd}(u,m) = 1/{\rm dn}(u,m).$

### Function: jacobi_ns (u, m)

The Jacobian elliptic function 
${\rm ns}(u,m) = 1/{\rm sn}(u,m).$

### Function: jacobi_sc (u, m)

The Jacobian elliptic function 
${\rm sc}(u,m) = {\rm sn}(u,m)/{\rm cn}(u,m).$

### Function: jacobi_sd (u, m)

The Jacobian elliptic function 
${\rm sd}(u,m) = {\rm sn}(u,m)/{\rm dn}(u,m).$

### Function: jacobi_sn (u, m)

The Jacobian elliptic function 
${\rm sn}(u,m).$

### Function: kbateman (v, x)

The Bateman k function



$$k_v(x) = \frac{2}{\pi} \int_0^{\pi/2} \cos(x \tan\theta-v\theta)d\theta$$


$$k_v(x)
 = \frac{2}{\pi} \int_0^{\pi/2} \cos(x \tan\theta-v\theta)d\theta$$



It is one solution of a differential equation which appears in the
theory of turbulence:



$$x {d^2u\over dx^2} = (x-\nu)u$$


$$x {d^2u\over dx^2} = (x-\nu)u$$



It is a special case of the confluent hypergeometric function for
$x > 0$:



$$k_v(x) = {e^{-x}\over{\Gamma\left(1+{1\over 2}\nu\right)}} U\left(-{1\over 2} \nu, 0, 2x\right)$$


$$k_v(x)
 = {e^{-x}\over{\Gamma\left(1+{1\over 2}\nu\right)}} U\left(-{1\over 2}
 \nu, 0, 2x\right)$$


where $U$ is the confluent hypergeometric function.  Also, we
have

$$k_{2\nu}(z) = {1\over\Gamma(\nu+1)} W_{\nu,1/2}(2z)$$


$$k_{2\nu}(z) = {1\over\Gamma(\nu+1)} W_{\nu,1/2}(2z)$$



where
$W$
is the `_0025w`.


Some examples:










```maxima
(%i1) assume(x > 0)$

(%i2) makelist(kbateman[n](0),n,0,5);
                      2          2         2
(%o2)            [0, ---, 0, - -----, 0, -----]
                     %pi       3 %pi     5 %pi


(%i3) kbateman[0](x);
                                - x
(%o3)                         %e


(%i4) kbateman[2](x);
                                - x
(%o4)                       2 %e    x


(%i5) kbateman[4](x);
                            - x
(%o5)                   2 %e    (x - 1) x


(%i6) kbateman[3](x);
(%o6)                     kbateman (x)
                                  3
```


Maxima can
calculate the Laplace transform of `kbateman` using `laplace`
or `specint`, as shown below:







```maxima
(%i1) assume(s>0)$

(%i2) specint(kbateman[v](z)*exp(-s*z),z);
                               v        v   s - 1
              2 %f    ([2, 1 - -], [2 - -], -----)
                  2, 1         2        2   s + 1
(%o2)         ------------------------------------
                      2           v        v
               (s + 1)  gamma(2 - -) gamma(- + 1)
                                  2        2
```

See also: `%w`, `kbateman`, `laplace`, `specint`.

### Function: lambert_w (z)

The principal branch of Lambert’s W function W(z) ([https://dlmf.nist.gov/4.13DLMF 4.13]()), the solution of 

$$z = W(z)e^{W(z)}$$


$$z = W(z)e^{W(z)}$$

### Function: log_gamma (z)

The natural logarithm of the gamma function.








```maxima
maxima

(%i1) gamma(6);
(%o1)                          120


(%i2) log_gamma(6);
(%o2)                       log(120)


(%i3) log_gamma(0.5);
(%o3)                  0.5723649429247004
```

### Function: makefact (expr)

Transforms instances of binomial, gamma, and beta
functions in *expr* into factorials.


See also `makegamma`.








```maxima
maxima

(%i1) makefact(binomial(n,k));
                               n!
(%o1)                      -----------
                           k! (n - k)!


(%i2) makefact(gamma(x));
(%o2)                       (x - 1)!


(%i3) makefact(beta(a,b));
                        (a - 1)! (b - 1)!
(%o3)                   -----------------
                          (b + a - 1)!
```

See also: `makegamma`.

### Function: makegamma (expr)

Transforms instances of binomial, factorial, and beta
functions in *expr* into gamma functions.


See also `makefact`.








```maxima
maxima

(%i1) makegamma(binomial(n,k));
                          gamma(n + 1)
(%o1)             -----------------------------
                  gamma(k + 1) gamma(n - k + 1)


(%i2) makegamma(x!);
(%o2)                     gamma(x + 1)


(%i3) makegamma(beta(a,b));
                        gamma(a) gamma(b)
(%o3)                   -----------------
                          gamma(b + a)
```

See also: `makefact`.

### Variable: maxpsifracdenom

Default value: 6


Let $x$ be a rational number of the form $p/q$.
If $q$ is greater than `maxpsifracdenom`,
then 
$\psi^{(0)}(x)$
will
not try to return a simplified value.










```maxima
maxima

(%i1) psi[0](3/4);
                                 %pi
(%o1)               - 3 log(2) + --- - %gamma
                                  2


(%i2) psi[2](3/4);
                             1         3
(%o2)                   psi (-) + 4 %pi
                           2 4


(%i3) maxpsifracdenom:2;
(%o3)                           2


(%i4) psi[0](3/4);
                                  3
(%o4)                        psi (-)
                                0 4


(%i5) psi[2](3/4);
                             1         3
(%o5)                   psi (-) + 4 %pi
                           2 4
```

See also: `maxpsifracdenom`.

### Variable: maxpsifracnum

Default value: 6


Let $x$ be a rational number of the form $p/q$.
If $p$ is greater than `maxpsifracnum`,
then 
$\psi^{(0)}(x)$
will not try to
return a simplified value.










```maxima
maxima

(%i1) psi[0](3/4);
                                 %pi
(%o1)               - 3 log(2) + --- - %gamma
                                  2


(%i2) psi[2](3/4);
                             1         3
(%o2)                   psi (-) + 4 %pi
                           2 4


(%i3) maxpsifracnum:2;
(%o3)                           2


(%i4) psi[0](3/4);
                                  3
(%o4)                        psi (-)
                                0 4


(%i5) psi[2](3/4);
                             1         3
(%o5)                   psi (-) + 4 %pi
                           2 4
```

See also: `maxpsifracnum`.

### Variable: maxpsinegint

Default value: -10


`maxpsinegint` is the most negative value for
which 
$\psi^{(0)}(x)$
will try to compute an exact
value for rational $x$.  That is if $x$ is less than
`maxpsinegint`, 
$\psi^{(n)}(x)$
will not
return simplified answer, even if it could.









```maxima
maxima

(%i1) psi[0](-100/9);
                                  100
(%o1)                      psi (- ---)
                              0    9


(%i2) psi[0](-100/11);
                   100 %pi         1     5231385863539
(%o2)      %pi cot(-------) + psi (--) + -------------
                     11          0 11    381905105400


(%i3) psi[2](-100/9);
                                  100
(%o3)                      psi (- ---)
                              2    9


(%i4) psi[2](-100/11);
           3     100 %pi     2 100 %pi         1
(%o4) 2 %pi  cot(-------) csc (-------) + psi (--)
                   11            11          2 11
                           74191313259470963498957651385614962459
                         + --------------------------------------
                            27850718060013605318710152732000000
```

See also: `maxpsinegint`.

### Variable: maxpsiposint

Default value: 20


`maxpsiposint` is the largest positive integer value for
which 
$\psi^{(n)}(m)$
gives an exact value for
rational $x$.









```maxima
maxima

(%i1) psi[0](20);
                       275295799
(%o1)                  --------- - %gamma
                       77597520


(%i2) psi[0](21);
(%o2)                       psi (21)
                               0


(%i3) psi[2](20);
                1683118856778495358491487
(%o3)        2 (------------------------- - zeta(3))
                1401731326612193601024000


(%i4) psi[2](21);
(%o4)                       psi (21)
                               2
```

See also: `maxpsiposint`.

### Function: numfactor (expr)

Returns the numerical factor multiplying the expression
*expr*, which should be a single term.



`content` returns the greatest common divisor (gcd) of all terms in a sum.







```maxima
maxima

(%i1) gamma (7/2);
                          15 sqrt(%pi)
(%o1)                     ------------
                               8


(%i2) numfactor (%);
                               15
(%o2)                          --
                               8
```

See also: `content`.

### Function: nzeta (z)

The Plasma Dispersion Function 

$${\rm nzeta}(z) = i\sqrt{\pi}e^{-z^2}(1-{\rm erf}(-iz))$$


$${\rm nzeta}(z) = i\sqrt{\pi}e^{-z^2}(1-{\rm erf}(-iz))$$

### Function: nzetai (z)

Returns `imagpart(nzeta(z))`.

### Function: nzetar (z)

Returns `realpart(nzeta(z))`.

### Function: psi (n, x)

`psi` is the polygamma function ([https://dlmf.nist.gov/5.2E2DLMF 5.2E2](),
[https://dlmf.nist.gov/5.15DLMF 5.15](), [https://personal.math.ubc.ca/~cbm/aands/page_258.htmA&S eqn 6.3.1]() and [https://personal.math.ubc.ca/~cbm/aands/page_260.htmA&S eqn 6.4.1]()) defined by

$$\psi^{(n)}(x) = {d^{n+1}\over{dx^{n+1}}} \log\Gamma(x)$$


$$\psi^{(n)}(x) = {d^{n+1}\over{dx^{n+1}}} \log\Gamma(x)$$



Thus, `psi` is the first derivative,
`psi` is the second derivative, etc.


Maxima can compute some exact values for rational args as well for
float and bfloat args.  Several variables control what range of
rational args 
$\psi^{(n)}(x)$
will return an
exact value, if possible.  See `maxpsiposint`,
`maxpsinegint`, `maxpsifracnum`, and
`maxpsifracdenom`. That is, $x$ must lie between
`maxpsinegint` and `maxpsiposint`.  If the absolute value of
the fractional part of $x$ is rational and has a numerator less
than `maxpsifracnum` and has a denominator less than
`maxpsifracdenom`, 
$\psi^{(0)}(x)$
will
return an exact value.


The function `bfpsi` in the `bffac` package can compute
numerical values.











```maxima
maxima

(%i1) psi[0](.25);
(%o1)                  - 4.227453533376265


(%i2) psi[0](1/4);
                                 %pi
(%o2)               - 3 log(2) - --- - %gamma
                                  2


(%i3) float(%);
(%o3)                  - 4.227453533376265


(%i4) psi[2](0.75);
(%o4)                 - 5.3026332163376395


(%i5) psi[2](3/4);
                             1         3
(%o5)                   psi (-) + 4 %pi
                           2 4


(%i6) float(%);
(%o6)                 - 5.3026332163376395
```

See also: `psi`, `maxpsiposint`, `maxpsinegint`, `maxpsifracnum`, `maxpsifracdenom`, `bfpsi`, `bffac`.

### Function: scaled_bessel_i (v, z)

The scaled modified Bessel function of the first kind of order
$v$ and argument $z$.  That is,



$${\rm scaled\_bessel\_i}(v,z) = e^{-|z|} I_v(z).$$


$${\rm scaled\_bessel\_i}(v,z) = e^{-|z|} I_v(z).$$



This function is particularly useful
for calculating
$I_v(z)$
for large $z$, which is large.
However, maxima does not otherwise know much about this function.  For
symbolic work, it is probably preferable to work with the expression
`exp(-abs(z))*bessel_i(v, z)`.

### Function: scaled_bessel_i0 (z)

Identical to `scaled_005fbessel_005fi`.

See also: `scaled_bessel_i`.

### Function: scaled_bessel_i1 (z)

Identical to `scaled_005fbessel_005fi`.

See also: `scaled_bessel_i`.

### Function: sinc (x)

The function `sinc` is defined by 

$${\rm sinc}(x) = \left@{ \matrix{ \displaystyle{\frac{\sin x}{x}} & {\rm if}\> x \neq 0\cr & \cr % For extra vertical space 1 & {\rm if}\> x = 0 } \right.$$


$${\rm sinc}(x) = 
\left@{
\matrix{
\displaystyle{\frac{\sin x}{x}} & {\rm if}\> x \neq 0\cr
 & \cr % For extra vertical space
1                & {\rm if}\> x = 0
}
\right.
$$



making `sinc` continuous at zero. The definition used here is the *unnormalized* version of the `sinc`
function.


When `%piargs` is true (the default),
${\rm sinc}(x)$
evaluates to an exact value when $x$ is an 
explicit integer multiple of
$\pi,$
$\pi/4,$
or
$\pi/6.$
For other nonzero symbolic arguments, 
`sinc` does not simplify to
$\sin(x)/x.$


For real or complex floating-point arguments (double or big floats), `sinc` returns a floating-point 
value in rectangular form. When `numer` is true, `sinc` returns a floating-point value in rectangular 
form for all numeric arguments, including rational numbers and big float numbers.












```maxima
maxima

(%i1) sinc(%pi);
(%o1)                           0

(%i2) %piargs : false$

(%i3) sinc(pi);
(%o3)                       sinc(pi)


(%i4) sinc(1.0 + 5.0*%i);
(%o4)      10.111782590680328 - 10.466747175403242 %i


(%i5) sinc(1 + 5*%i);
(%o5)                    sinc(5 %i + 1)


(%i6) sinc(1 + 5*%i), numer;
(%o6)      10.111782590680328 - 10.466747175403242 %i


(%i7) sinc(1.2b0 + 5.6b0*%i), numer;
(%o7)      12.975676863468047 - 19.724089614291696 %i
```

See also: `sinc`, `%piargs`, `numer`.

### Function: slommel (u, v, z)

Lommel’s big
$S_{\mu,\nu}(z)$
function.  
([https://dlmf.nist.gov/11.9.E5DLMF 11.9.E5]())(G&R 8.570.2).


Lommels big S function is another particular solution of the
inhomogeneous Bessel differential equation
(`_0025s`) defined for all values
of
$\mu$
and
$\nu,$
where



$$\eqalign{ S_{\mu,\nu}(z) = s_{\mu,\nu}(z) + 2^{\mu-1} & \Gamma\left({\mu\over 2} + {\nu\over 2} + {1\over 2}\right) \Gamma\left({\mu\over 2} - {\nu\over 2} + {1\over 2}\right) \cr & \times \left(\sin\left({(\mu-\nu)\pi\over 2}\right) J_{\nu}(z) - \cos\left({(\mu-\nu)\pi\over 2}\right) Y_{\nu}(z)\right) }$$


$$\eqalign{
S_{\mu,\nu}(z) = s_{\mu,\nu}(z) + 2^{\mu-1} & \Gamma\left({\mu\over 2} + {\nu\over 2} + {1\over 2}\right) \Gamma\left({\mu\over 2} - {\nu\over 2} + {1\over 2}\right) \cr
& \times \left(\sin\left({(\mu-\nu)\pi\over 2}\right) J_{\nu}(z) - \cos\left({(\mu-\nu)\pi\over 2}\right) Y_{\nu}(z)\right)
}$$



When
$\mu\pm \nu$
is an odd
negative integer, the limit must be used.

See also: `%s`.

### Function: struve_h (v, z)

The Struve Function H of order 
$\nu$
and argument $z$:



$${\bf H}_{\nu}(z) = \left({z\over 2}\right)^{\nu+1} \sum_{k=0}^{\infty} {(-1)^k\left({z\over 2}\right)^{2k} \over \Gamma\left(k + {3\over 2}\right) \Gamma\left(k + \nu + {3\over 2}\right)}$$


$${\bf H}_{\nu}(z) = \left({z\over 2}\right)^{\nu+1}
\sum_{k=0}^{\infty} {(-1)^k\left({z\over 2}\right)^{2k} \over \Gamma\left(k + {3\over 2}\right) \Gamma\left(k + \nu + {3\over 2}\right)}$$



([https://personal.math.ubc.ca/~cbm/aands/page_496.htmA&S eqn 12.1.3]()) and ([https://dlmf.nist.gov/11.2.E1DLMF 11.2.E1]()).


When `besselexpand` is `true`, `struve_h` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.

See also: `besselexpand`, `true`, `struve_h`.

### Function: struve_l (v, z)

The Modified Struve Function L of order 
$\nu$
and argument $z$:

$${\bf L}_{\nu}(z) = -ie^{-{i\nu\pi\over 2}} {\bf H}_{\nu}(iz)$$


$${\bf L}_{\nu}(z) = -ie^{-{i\nu\pi\over 2}} {\bf H}_{\nu}(iz)$$




([https://personal.math.ubc.ca/~cbm/aands/page_498.htmA&S eqn 12.2.1]()) and ([https://dlmf.nist.gov/11.2.E2DLMF 11.2.E2]()).


When `besselexpand` is `true`, `struve_l` is expanded in terms
of elementary functions when the order $v$ is half of an odd integer. 
See `besselexpand`.

See also: `besselexpand`, `true`, `struve_l`.

