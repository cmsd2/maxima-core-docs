## distrib

### Function: cdf_bernoulli (x, p)

Returns the value at *x* of the cumulative distribution function of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; p) = I_{1-p}(1-\lfloor x \rfloor, \lfloor x \rfloor + 1)$$


$$F(x; p) = I_{1-p}(1-\lfloor x \rfloor, \lfloor x \rfloor + 1)$$

### Function: cdf_beta (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$.


The cdf is

$$F(x; a, b) = \cases{ 0 & $x < 0$ \cr I_x(a,b) & $0 \le x \le 1$ \cr 1 & $x > 1$ }$$


$$F(x; a, b) =
\cases{
0 & $x < 0$ \cr
I_x(a,b) & $0 \le x \le 1$ \cr
1 & $x > 1$
}$$









```maxima
(%i1) load ("distrib")$

(%i2) cdf_beta(1/3,15,2);
                               11
(%o2)                       --------
                            14348907


(%i3) float(%);
(%o3)                 7.666089131388195e-7
```

### Function: cdf_binomial (x, n, p)

Returns the value at *x* of the cumulative distribution function of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer.


The cdf is

$$F(x; n, p) = I_{1-p}(n-\lfloor x \rfloor, \lfloor x \rfloor + 1)$$


$$F(x; n, p) = I_{1-p}(n-\lfloor x \rfloor, \lfloor x \rfloor + 1)$$



where 
$I_z(a,b)$
is the `beta_005fincomplete_005fregularized`
function.









```maxima
(%i1) load ("distrib")$

(%i2) cdf_binomial(5,7,1/6);
                              7775
(%o2)                         ----
                              7776


(%i3) float(%);
(%o3)                  0.9998713991769548
```

See also: `beta_incomplete_regularized`.

### Function: cdf_cauchy (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Cauchy}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = {1\over 2} + {1\over \pi} \tan^{-1} {x-a\over b}$$


$$F(x; a, b) = {1\over 2} + {1\over \pi} \tan^{-1} {x-a\over b}$$

### Function: cdf_chi2 (x, n)

Returns the value at $x$ of the cumulative distribution function of a
Chi-square random variable 
$\chi^2(n)$
, with $n>0$.


The cdf is

$$F(x; n) = \cases{ 1 - Q\left(\displaystyle{n\over 2}, {x\over 2}\right) & $x > 0$ \cr 0 & otherwise }$$


$$F(x; n) =
\cases{
1 - Q\left(\displaystyle{n\over 2}, {x\over 2}\right) & $x > 0$ \cr
0 & otherwise
}$$



where $Q(a,z)$ is the `gamma_005fincomplete_005fregularized` function.








```maxima
(%i1) load ("distrib")$

(%i2) cdf_chi2(3,4);
                                                 3
(%o2)        1 - gamma_incomplete_regularized(2, -)
                                                 2


(%i3) float(%);
(%o3)                  0.44217459962892525
```

See also: `gamma_incomplete_regularized`.

### Function: cdf_continuous_uniform (x, a, b)

Returns the value at *x* of the cumulative distribution function of a
${\it ContinuousUniform}(a,b)$
random variable, with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = \cases{ 0 & for $x < a$ \cr \cr \displaystyle{x-a\over b-a} & for $a \le x \le b$ \cr \cr 1 & for $x > b$ }$$


$$F(x; a, b) =
\cases{
0 & for $x < a$ \cr
\cr
\displaystyle{x-a\over b-a} & for $a \le x \le b$ \cr
\cr
1 & for $x > b$
}$$

### Function: cdf_discrete_uniform (x, n)

Returns the value at *x* of the cumulative distribution function of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; n) = {\lfloor x \rfloor \over n}$$


$$F(x; n) = {\lfloor x \rfloor \over n}$$

### Function: cdf_exp (x, m)

Returns the value at *x* of the cumulative distribution function of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The cdf is

$$F(x; m) = \cases{ 1 - e^{-mx} & $x \ge 0$ \cr 0 & otherwise }$$


$$F(x; m) =
\cases{
1 - e^{-mx} & $x \ge 0$ \cr
0 & otherwise
}$$








```maxima
(%i1) load ("distrib")$

(%i2) cdf_exp(x,m);
                          - m x
(%o2)              (1 - %e     ) unit_step(x)
```

### Function: cdf_f (x, m, n)

Returns the value at *x* of the cumulative distribution function of a F random variable $F(m,n)$, with $m,n>0$.


The cdf is

$$F(x; m, n) = \cases{ 1 - I_z\left(\displaystyle{m\over 2}, {n\over 2}\right) & $x > 0$ \cr 0 & otherwise }$$


$$F(x; m, n) =
\cases{
1 - I_z\left(\displaystyle{m\over 2}, {n\over 2}\right) & $x > 0$ \cr
0 & otherwise
}$$




where

$$z = {n\over mx+n}$$


$$z = {n\over mx+n}$$




and 
$I_z(a,b)$
is the `beta_005fincomplete_005fregularized`
function.







```maxima
(%i1) load ("distrib")$

(%i2) cdf_f(2,3,9/4);
                                            9  3  3
(%o2)       1 - beta_incomplete_regularized(-, -, --)
                                            8  2  11


(%i3) float(%);
(%o3)                  0.6675672817900802
```

See also: `beta_incomplete_regularized`.

### Function: cdf_gamma (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. 


The cdf is

$$F(x; a, b) = \cases{ 1-Q(a,{x\over b}) & for $x \ge 0$ \cr \cr 0 & for $x < 0$ }$$


$$F(x; a, b) =
\cases{
1-Q(a,{x\over b}) & for $x \ge 0$ \cr
\cr
0 & for $x < 0$
}$$



where $Q(a,z)$ is the `gamma_005fincomplete_005fregularized` function.







```maxima
(%i1) load ("distrib")$

(%i2) cdf_gamma(3,5,21);
                                                 1
(%o2)        1 - gamma_incomplete_regularized(5, -)
                                                 7


(%i3) float(%);
(%o3)                 4.402663157376807e-7
```

See also: `gamma_incomplete_regularized`.

### Function: cdf_general_finite_discrete (x, v)

Returns the value at *x* of the cumulative distribution function of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.









```maxima
(%i1) load ("distrib")$

(%i2) cdf_general_finite_discrete(2, [1/7, 4/7, 2/7]);
                                5
(%o2)                           -
                                7


(%i3) cdf_general_finite_discrete(2, [1, 4, 2]);
                                5
(%o3)                           -
                                7


(%i4) cdf_general_finite_discrete(2+1/2, [1, 4, 2]);
                                5
(%o4)                           -
                                7
```

See also: `pdf_general_finite_discrete`.

### Function: cdf_geometric (x, p)

Returns the value at *x* of the cumulative distribution function of a 
${\it Geometric}(p)$
random variable, with
$0 < p \leq 1$


The cdf is

$$1-(1-p)^{1 + \lfloor x \rfloor}$$


$$1-(1-p)^{1 + \lfloor x \rfloor}$$




`load("distrib")` loads this function.

### Function: cdf_gumbel (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = \exp\left[-\exp\left({a-x\over b}\right)\right]$$


$$F(x; a, b) = \exp\left[-\exp\left({a-x\over b}\right)\right]$$

### Function: cdf_hypergeometric (x, n_1, n_2, n)

Returns the value at *x* of the cumulative distribution function of a 
${\it Hypergeometric}(n1,n2,n)$
random variable, with $n_1$, $n_2$ and $n$ non negative
integers and $n\leq n_1+n_2$. 
See `pdf_hypergeometric` for a more complete description.


To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; n_1, n_2, n) = {n_2+n_1\choose n}^{-1} \sum_{k=0}^{\lfloor x \rfloor} {n_1 \choose k} {n_2 \choose n - k}$$


$$F(x; n_1, n_2, n) = {n_2+n_1\choose n}^{-1}
\sum_{k=0}^{\lfloor x \rfloor} {n_1 \choose k} {n_2 \choose n - k}$$

### Function: cdf_laplace (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = \cases{ \displaystyle{1\over 2} \exp\left({x-a\over b}\right) & for $x < a$\cr \cr 1-\displaystyle{1\over 2} \exp\left({x-a\over b}\right) & for $x \ge a$ }$$


$$F(x; a, b) =
\cases{
\displaystyle{1\over 2} \exp\left({x-a\over b}\right) & for $x < a$\cr
\cr
1-\displaystyle{1\over 2} \exp\left({x-a\over b}\right) & for $x \ge a$
}$$

### Function: cdf_logistic (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Logistic}(a,b)$
random variable , with $b>0$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = {1\over 1+e^{-(x-a)/b}}$$


$$F(x; a, b) = {1\over 1+e^{-(x-a)/b}}$$

### Function: cdf_lognormal (x, m, s)

Returns the value at *x* of the cumulative distribution function of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. This function is defined in terms of Maxima’s built-in error function `erf`.


The cdf is

$$F(x; m, s) = \cases{ \displaystyle{1\over 2}\left[1+{\rm erf}\left({\log x - m\over s\sqrt{2}}\right)\right] & for $x > 0$ \cr \cr 0 & for $x \le 0$ }$$


$$F(x; m, s) =
\cases{
\displaystyle{1\over 2}\left[1+{\rm erf}\left({\log x - m\over s\sqrt{2}}\right)\right] &
for $x > 0$ \cr
\cr
0 & for $x \le 0$
}$$









```maxima
(%i1) load ("distrib")$

(%i2) cdf_lognormal(x,m,s);
                                 log(x) - m
                             erf(----------)
                                 sqrt(2) s     1
(%o2)          unit_step(x) (--------------- + -)
                                    2          2
```


See also `erf`.

See also: `erf`.

### Function: cdf_negative_binomial (x, n, p)

Returns the value at *x* of the cumulative distribution function of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number.


The cdf is

$$F(x; n, p) = I_p(n,\lfloor x \rfloor + 1)$$


$$F(x; n, p) = I_p(n,\lfloor x \rfloor + 1)$$



where 
$I_p(a,b)$
is the `beta_005fincomplete_005fregularized` function.







```maxima
(%i1) load ("distrib")$

(%i2) cdf_negative_binomial(3,4,1/8);
                              3271
(%o2)                        ------
                             524288
```

See also: `beta_incomplete_regularized`.

### Function: cdf_noncentral_chi2 (x, n, ncp)

Returns the value at *x* of the cumulative distribution function of a
noncentral Chi-square random variable 
m4_noncentral_chi2(n,ncp)
, with
$n>0$ and noncentrality parameter 
$ncp \ge 0.$
To make use of this function, write first `load("distrib")`.

### Function: cdf_noncentral_student_t (x, n, ncp)

Returns the value at *x* of the cumulative distribution function of a
noncentral Student random variable 
${\it nc\_t}(n, ncp)$
, with $n>0$ degrees of freedom and noncentrality parameter $ncp$. This function has no closed form and it is numerically computed.







```maxima
(%i1) load ("distrib")$

(%i2) cdf_noncentral_student_t(-2,5,-5);
(%o2)                   0.995203009331975
```

### Function: cdf_normal (x, m, s)

Returns the value at *x* of the cumulative distribution function of a 
${\it Normal}(m, s)$
random variable, with $s>0$. This function is defined in terms of Maxima’s built-in error function `erf`.


The cdf can be written analytically:

$$F(x; m, s) = {1\over 2} + {1\over 2} {\rm erf}\left(x-m\over s\sqrt{2}\right)$$


$$F(x; m, s) = {1\over 2} + {1\over 2} {\rm erf}\left(x-m\over s\sqrt{2}\right)$$









```maxima
(%i1) load ("distrib")$

(%i2) cdf_normal(x,m,s);
                             x - m
                       erf(---------)
                           sqrt(2) s    1
(%o2)                  -------------- + -
                             2          2
```


See also `erf`.

See also: `erf`.

### Function: cdf_pareto (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Pareto}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = \cases{ 1-\left(\displaystyle{b\over x}\right)^a & for $x \ge b$\cr 0 & for $x < b$ }$$


$$F(x; a, b) =
\cases{
1-\left(\displaystyle{b\over x}\right)^a & for $x \ge b$\cr
0 & for $x < b$
}$$

### Function: cdf_poisson (x, m)

Returns the value at *x* of the cumulative distribution function of a 
${\it Poisson}(m)$
random variable, with $m>0$.


The cdf is

$$F(x; m) = Q(\lfloor x \rfloor + 1, m)$$


$$F(x; m) = Q(\lfloor x \rfloor + 1, m)$$



where $Q(x,m)$ is the `gamma_005fincomplete_005fregularized`
function.








```maxima
(%i1) load ("distrib")$

(%i2) cdf_poisson(3,5);
(%o2)          gamma_incomplete_regularized(4, 5)


(%i3) float(%);
(%o3)                  0.26502591529736186
```

See also: `gamma_incomplete_regularized`.

### Function: cdf_rayleigh (x, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The cdf is

$$F(x; b) = \cases{ 1 - e^{-b^2 x^2} & for $x \ge 0$\cr 0 & for $x < 0$ }$$


$$F(x; b) =
\cases{
1 - e^{-b^2 x^2} & for $x \ge 0$\cr
0 & for $x < 0$
}$$








```maxima
(%i1) load ("distrib")$

(%i2) cdf_rayleigh(x,b);
                            2  2
                         - b  x
(%o2)             (1 - %e       ) unit_step(x)
```

### Function: cdf_student_t (x, n)

Returns the value at *x* of the cumulative distribution function of a Student
random variable 
$t(n)$
, with $n>0$ degrees of freedom.


The cdf is

$$F(x; n) = \cases{ 1-\displaystyle{1\over 2} I_t\left({n\over 2}, {1\over 2}\right) & $x \ge 0$ \cr \cr \displaystyle{1\over 2} I_t\left({n\over 2}, {1\over 2}\right) & $x < 0$ }$$


$$F(x; n) =
\cases{
1-\displaystyle{1\over 2} I_t\left({n\over 2}, {1\over 2}\right) & $x \ge 0$ \cr
\cr
\displaystyle{1\over 2} I_t\left({n\over 2}, {1\over 2}\right) & $x < 0$
}$$




where 
$t = n/(n+x^2)$
and 
$I_t(a,b)$
is the
`beta_005fincomplete_005fregularized` function.








```maxima
(%i1) load ("distrib")$

(%i2) cdf_student_t(1/2, 7/3);
                                            7  1  28
                beta_incomplete_regularized(-, -, --)
                                            6  2  31
(%o2)       1 - -------------------------------------
                                  2


(%i3) float(%);
(%o3)                  0.6698450596140415
```

See also: `beta_incomplete_regularized`.

### Function: cdf_weibull (x, a, b)

Returns the value at *x* of the cumulative distribution function of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The cdf is

$$F(x; a, b) = \cases{ 1 - e^{-(x/b)^a} & for $x \ge 0$ \cr 0 & for $x < 0$ }$$


$$F(x; a, b) =
\cases{
1 - e^{-(x/b)^a} & for $x \ge 0$ \cr
0 & for $x < 0$
}$$

### Function: kurtosis_bernoulli (p)

Returns the kurtosis coefficient of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$.


The 
${\it Bernoulli}(p)$
random variable is equivalent to the 
${\it Binomial}(1,p)$
.


The kurtosis coefficient is

$$KU[X] = {1-6p(1-p) \over p(1-p)}$$


$$KU[X] = {1-6p(1-p) \over p(1-p)}$$









```maxima
(%i1) load ("distrib")$

(%i2) kurtosis_bernoulli(p);
                         1 - 6 (1 - p) p
(%o2)                    ---------------
                            (1 - p) p
```

### Function: kurtosis_beta (a, b)

Returns the kurtosis coefficient of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {3(a+b+1)\left(2(a+b)^2+ab(a+b-6)\right) \over ab(a+b+2)(a+b+3)} - 3$$


$$KU[X] = {3(a+b+1)\left(2(a+b)^2+ab(a+b-6)\right) \over
ab(a+b+2)(a+b+3)} - 3$$

### Function: kurtosis_binomial (n, p)

Returns the kurtosis coefficient of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {1-6p(1-p)\over np(1-p)}$$


$$KU[X] = {1-6p(1-p)\over np(1-p)}$$

### Function: kurtosis_chi2 (n)

Returns the kurtosis coefficient of a Chi-square random variable 
$\chi^2(n)$
, with $n>0$.


The 
$\chi^2(n)$
random variable is equivalent to the 
$\Gamma\left(n/2,2\right)$
.


The kurtosis coefficient is

$$KU[X] = {12\over n}$$


$$KU[X] = {12\over n}$$









```maxima
(%i1) load ("distrib")$

(%i2) kurtosis_chi2(n);
                               12
(%o2)                          --
                               n
```

### Function: kurtosis_continuous_uniform (a, b)

Returns the kurtosis coefficient of a 
${\it ContinuousUniform}(a,b)$
random variable, with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = -{6\over5}$$


$$KU[X] = -{6\over5}$$

### Function: kurtosis_discrete_uniform (n)

Returns the kurtosis coefficient of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = - {6(n^2+1)\over 5 (n^2-1)}$$


$$KU[X] = - {6(n^2+1)\over 5 (n^2-1)}$$

### Function: kurtosis_exp (m)

Returns the kurtosis coefficient of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The kurtosis coefficient is

$$KU[X] = 6$$


$$KU[X] = 6$$









```maxima
(%i1) load ("distrib")$

(%i2) kurtosis_exp(m);
(%o2)                           6
```

### Function: kurtosis_f (m, n)

Returns the kurtosis coefficient of a F random variable $F(m,n)$, with $m>0, n>8$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = 12{m(n+m-2)(5n-22) + (n-4)(n-2)^2 \over m(n-8)(n-6)(n+m-2)}$$


$$KU[X] = 12{m(n+m-2)(5n-22) + (n-4)(n-2)^2 \over m(n-8)(n-6)(n+m-2)}$$

### Function: kurtosis_gamma (a, b)

Returns the kurtosis coefficient of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {6\over a}$$


$$KU[X] = {6\over a}$$

### Function: kurtosis_general_finite_discrete (v)

Returns the kurtosis coefficient of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.

See also: `pdf_general_finite_discrete`.

### Function: kurtosis_geometric (p)

Returns the kurtosis coefficient of a geometric random variable  
${\it Geometric}(p)$
, with
$0 < p \leq 1$.


The kurtosis coefficient is

$$KU[X] = {p^2-6p+6 \over 1-p}$$


$$KU[X] = {p^2-6p+6 \over 1-p}$$




`load("distrib")` loads this function.

### Function: kurtosis_gumbel (a, b)

Returns the kurtosis coefficient of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {12\over 5}$$


$$KU[X] = {12\over 5}$$

### Function: kurtosis_hypergeometric (n_1, n_2, n)

Returns the kurtosis coefficient of a 
${\it Hypergeometric}(n_1,n_2,n)$
random variable, with $n_1$, $n_2$ and $n$ non negative integers and $n\leq n1+n2$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$\eqalign{ KU[X] = & \left[{C(1)C(0)^2 \over n n_1 n_2 C(3)C(2)C(n)}\right. \cr & \times \left.\left( {3n_1n_2\left((n-2)C(0)^2+6nC(n)-n^2C(0)\right) \over C(0)^2 } -6nC(n) + C(0)C(-1) \right)\right] \cr &-3 }$$


$$
\eqalign{
KU[X] = &
 \left[{C(1)C(0)^2
   \over
  n n_1 n_2 C(3)C(2)C(n)}\right. \cr
  & \times 
  \left.\left(
    {3n_1n_2\left((n-2)C(0)^2+6nC(n)-n^2C(0)\right)
    \over
    C(0)^2
    }
    -6nC(n) + C(0)C(-1)
  \right)\right] \cr
  &-3
}$$



where 
$C(k) = n_1+n_2-k.$

### Function: kurtosis_laplace (a, b)

Returns the kurtosis coefficient of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = 3$$


$$KU[X] = 3$$

### Function: kurtosis_logistic (a, b)

Returns the kurtosis coefficient of a 
${\it Logistic}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {6\over 5}$$


$$KU[X] = {6\over 5}$$

### Function: kurtosis_lognormal (m, s)

Returns the kurtosis coefficient of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = \exp\left(4s^2\right)+2\exp\left(3s^2\right)+3\exp\left(2s^2\right)-3$$


$$KU[X] = \exp\left(4s^2\right)+2\exp\left(3s^2\right)+3\exp\left(2s^2\right)-3$$

### Function: kurtosis_negative_binomial (n, p)

Returns the kurtosis coefficient of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {p^2-6p+6 \over n(1-p)}$$


$$KU[X] = {p^2-6p+6 \over n(1-p)}$$

### Function: kurtosis_noncentral_chi2 (n, ncp)

Returns the kurtosis coefficient of a noncentral Chi-square random
variable
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality
parameter 
$ncp \ge 0.$


The kurtosis coefficient is

$$KU[X] = {12(n+4\mu)\over (2+2\mu)^2}$$


$$KU[X] = {12(n+4\mu)\over (2+2\mu)^2}$$



where 
$\mu$
is the noncentrality parameter *ncp*.

### Function: kurtosis_noncentral_student_t (n, ncp)

Returns the kurtosis coefficient of a noncentral Student random
variable 
${\it nc\_t}(n, ncp)$
, with $n>4$ degrees of freedom and noncentrality parameter $ncp$. To make use of this function, write first `load("distrib")`.


If $U$ is a non-central Student’s $t$ random variable with
$n$ degrees of freedom and a noncentrality parameter 
$\mu,$
the kurtosis is







$$\eqalign{ KU[U] &= {\mu_4\over \sigma^4} - 3\cr \mu_4 &= {{\left(\mu^4+6\mu^2+3\right)n^2}\over{(n-4)(n-2)}} -\left({{n\left(3(3n-5)+\mu^2(n+1)\right) }\over{(n-3)(n-2)}}-3\sigma^2\right) F \cr \sigma^2 &= {{n\left(\mu^2+1\right)}\over{n-2}}-{{n \mu^2 \Gamma\left({{n-1}\over{2}}\right)^2}\over{2\Gamma\left({{n }\over{2}}\right)^2}} \cr F &= {n\mu^2\Gamma\left({n-1\over 2}\right)^2 \over 2\sigma^4\Gamma\left({n\over 2}\right)^2} }$$


$$\eqalign{
KU[U] &=
{\mu_4\over \sigma^4} - 3\cr
  \mu_4 &= {{\left(\mu^4+6\mu^2+3\right)n^2}\over{(n-4)(n-2)}}
 -\left({{n\left(3(3n-5)+\mu^2(n+1)\right)
 }\over{(n-3)(n-2)}}-3\sigma^2\right) F \cr
 \sigma^2 &= {{n\left(\mu^2+1\right)}\over{n-2}}-{{n \mu^2
 \Gamma\left({{n-1}\over{2}}\right)^2}\over{2\Gamma\left({{n
 }\over{2}}\right)^2}} \cr
 F &= {n\mu^2\Gamma\left({n-1\over 2}\right)^2 \over
 2\sigma^4\Gamma\left({n\over 2}\right)^2}
}$$

### Function: kurtosis_normal (m, s)

Returns the kurtosis coefficient of a 
${\it Normal}(m, s)$
random variable, with $s>0$, which is always equal to 0. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = 0$$


$$KU[X] = 0$$

### Function: kurtosis_pareto (a, b)

Returns the kurtosis coefficient of a 
${\it Pareto}(a,b)$
random variable, with $a>4,b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {6\left(a^3+a^2-6*a-2\right) \over a(a-3)(a-4)} - 3$$


$$KU[X] = {6\left(a^3+a^2-6*a-2\right) \over a(a-3)(a-4)} - 3$$

### Function: kurtosis_poisson (m)

Returns the kurtosis coefficient of a Poisson random variable  $Poi(m)$, with $m>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {1\over m}$$


$$KU[X] = {1\over m}$$

### Function: kurtosis_rayleigh (b)

Returns the kurtosis coefficient of a
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The kurtosis coefficient is

$$KU[X] = {32-3\pi\over (4-\pi)^2} - 3$$


$$KU[X] = {32-3\pi\over (4-\pi)^2} - 3$$









```maxima
(%i1) load ("distrib")$

(%i2) kurtosis_rayleigh(b);
                                  2
                             3 %pi
                         2 - ------
                               16
(%o2)                    ---------- - 3
                              %pi 2
                         (1 - ---)
                               4
```

### Function: kurtosis_student_t (n)

Returns the kurtosis coefficient of a Student random variable 
$t(n)$
, with $n>4$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = {6\over n-4}$$


$$KU[X] = {6\over n-4}$$

### Function: kurtosis_weibull (a, b)

Returns the kurtosis coefficient of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The kurtosis coefficient is

$$KU[X] = { \Gamma_4 - 4\Gamma_1 \Gamma_3 + 6\Gamma_1^2 \Gamma_2 - 3 \Gamma_1^4 \over \left[\Gamma_2 - \Gamma_1^2\right]^2 } - 3$$


$$KU[X] = {
\Gamma_4
 - 4\Gamma_1 \Gamma_3
 + 6\Gamma_1^2 \Gamma_2
 - 3 \Gamma_1^4
\over
 \left[\Gamma_2 - \Gamma_1^2\right]^2
} - 3$$



where 
$\Gamma_k = \Gamma\left(1+k/a\right).$

### Function: mean_bernoulli (p)

Returns the mean of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$.


The 
${\it Bernoulli}(p)$
random variable is equivalent to the 
${\it Binomial}(1,p)$
.


The mean is

$$E[X] = p$$


$$E[X] = p$$









```maxima
(%i1) load ("distrib")$

(%i2) mean_bernoulli(p);
(%o2)                           p
```

### Function: mean_beta (a, b)

Returns the mean of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {a\over a+b}$$


$$E[X] = {a\over a+b}$$

### Function: mean_binomial (n, p)

Returns the mean of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = np$$


$$E[X] = np$$

### Function: mean_chi2 (n)

Returns the mean of a Chi-square random variable 
$\chi^2(n)$
, with $n>0$.


The 
$\chi^2(n)$
random variable is equivalent to the 
$\Gamma\left(n/2,2\right)$
.


The mean is

$$E[X] = n$$


$$E[X] = n$$









```maxima
(%i1) load ("distrib")$

(%i2) mean_chi2(n);
(%o2)                           n
```

### Function: mean_continuous_uniform (a, b)

Returns the mean of a 
${\it ContinuousUniform}(a,b)$
random variable,
with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {a+b\over 2}$$


$$E[X] = {a+b\over 2}$$

### Function: mean_discrete_uniform (n)

Returns the mean of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {n+1\over 2}$$


$$E[X] = {n+1\over 2}$$

### Function: mean_exp (m)

Returns the mean of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The mean is

$$E[X] = {1\over m}$$


$$E[X] = {1\over m}$$









```maxima
(%i1) load ("distrib")$

(%i2) mean_exp(m);
                                1
(%o2)                           -
                                m
```

### Function: mean_f (m, n)

Returns the mean of a F random variable $F(m,n)$, with $m>0, n>2$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {n\over n-2}$$


$$E[X] = {n\over n-2}$$

### Function: mean_gamma (a, b)

Returns the mean of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = ab$$


$$E[X] = ab$$

### Function: mean_general_finite_discrete (v)

Returns the mean of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.

See also: `pdf_general_finite_discrete`.

### Function: mean_geometric (p)

Returns the mean of a 
${\it Geometric}(p)$
random variable, with
$0 < p \leq 1$.


The mean is

$$E[X] = {1\over p} - 1$$


$$E[X] = {1\over p} - 1$$




The probability from which the mean is derived is defined as $p (1 - p)^x$.
This is interpreted as the probability of $x$ failures before the first success.


`load("distrib")` loads this function.

### Function: mean_gumbel (a, b)

Returns the mean of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$.


The mean is

$$E[X] = a+b\gamma$$


$$E[X] = a+b\gamma$$









```maxima
(%i1) load ("distrib")$

(%i2) mean_gumbel(a,b);
(%o2)                     %gamma b + a
```

where symbol `%gamma` stands for the Euler-Mascheroni constant. See also `_0025gamma`.

See also: `%gamma`.

### Function: mean_hypergeometric (n_1, n_2, n)

Returns the mean of a discrete uniform random variable 
${\it Hypergeometric}(n_1,n_2,n)$
, with $n_1$, $n_2$ and $n$ non negative integers and $n\leq n_1+n_2$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {n n_1\over n_2+n_1}$$


$$E[X] = {n n_1\over n_2+n_1}$$

### Function: mean_laplace (a, b)

Returns the mean of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = a$$


$$E[X] = a$$

### Function: mean_logistic (a, b)

Returns the mean of a 
${\it Logistic}(a,b)$
random variable , with $b>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = a$$


$$E[X] = a$$

### Function: mean_lognormal (m, s)

Returns the mean of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = \exp\left(m+{s^2\over 2}\right)$$


$$E[X] = \exp\left(m+{s^2\over 2}\right)$$

### Function: mean_negative_binomial (n, p)

Returns the mean of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {n(1-p)\over p}$$


$$E[X] = {n(1-p)\over p}$$

### Function: mean_noncentral_chi2 (n, ncp)

Returns the mean of a noncentral Chi-square random variable
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality parameter 
$ncp \ge 0.$


The mean is

$$E[X] = n + \mu$$


$$E[X] = n + \mu$$



where 
$\mu$
is the noncentrality parameter *ncp*.

### Function: mean_noncentral_student_t (n, ncp)

Returns the mean of a noncentral Student random variable 
${\it nc\_t}(n, ncp)$
, with $n>1$ degrees of freedom and noncentrality parameter $ncp$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {\mu \sqrt{n}\; \Gamma\left(\displaystyle{n-1\over 2}\right) \over \sqrt{2}\;\Gamma\left(\displaystyle{n\over 2}\right)}$$


$$E[X] = {\mu \sqrt{n}\; \Gamma\left(\displaystyle{n-1\over 2}\right) \over
\sqrt{2}\;\Gamma\left(\displaystyle{n\over 2}\right)}$$




where 
$\mu$
is the noncentrality parameter $ncp$.







```maxima
(%i1) load ("distrib")$

(%i2) mean_noncentral_student_t(df,k);
                          df - 1
                    gamma(------) sqrt(df) k
                            2
(%o2)               ------------------------
                                     df
                       sqrt(2) gamma(--)
                                     2
```

### Function: mean_normal (m, s)

Returns the mean of a 
${\it Normal}(m, s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = m$$


$$E[X] = m$$

### Function: mean_pareto (a, b)

Returns the mean of a 
${\it Pareto}(a,b)$
random variable, with $a>1,b>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = {ab\over a-1}$$


$$E[X] = {ab\over a-1}$$

### Function: mean_poisson (m)

Returns the mean of a 
${\it Poisson}(m)$
random variable, with  $m>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = m$$


$$E[X] = m$$

### Function: mean_rayleigh (b)

Returns the mean of a 
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The mean is

$$E[X] = {\sqrt{\pi}\over 2b}$$


$$E[X] = {\sqrt{\pi}\over 2b}$$









```maxima
(%i1) load ("distrib")$

(%i2) mean_rayleigh(b);
                            sqrt(%pi)
(%o2)                       ---------
                               2 b
```

### Function: mean_student_t (n)

Returns the mean of a Student random variable 
$t(n)$
, with $n>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = 0$$


$$E[X] = 0$$

### Function: mean_weibull (a, b)

Returns the mean of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The mean is

$$E[X] = b\Gamma\left(1+{1\over a}\right)$$


$$E[X] = b\Gamma\left(1+{1\over a}\right)$$

### Function: pdf_bernoulli (x, p)

Returns the value at *x* of the probability function of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$.


The 
${\it Bernoulli}(p)$
random variable is equivalent to the 
${\it Binomial}(1,p)$
.


The mean is

$$f(x; p) = p^x (1-p)^{1-x}$$


$$f(x; p) = p^x (1-p)^{1-x}$$









```maxima
(%i1) load ("distrib")$

(%i2) pdf_bernoulli(1,p);
(%o2) if equal(p, 0) then 0 elseif equal(p, 1) then 1 else p
```

### Function: pdf_beta (x, a, b)

Returns the value at *x* of the density function of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; a, b) = \cases{ \displaystyle{x^{a-1}(1-x)^{b-1} \over B(a,b)} & for $0 \le x \le 1$ \cr \cr 0 & otherwise }$$


$$f(x; a, b) =
\cases{
\displaystyle{x^{a-1}(1-x)^{b-1} \over B(a,b)} & for $0 \le x \le 1$
\cr
\cr
0 & otherwise
}$$

### Function: pdf_binomial (x, n, p)

Returns the value at *x* of the probability function of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; n, p) = {n\choose x} (1-p)^{n-x}p^x$$


$$f(x; n, p) = {n\choose x} (1-p)^{n-x}p^x$$

### Function: pdf_cauchy (x, a, b)

Returns the value at *x* of the density function of a 
${\it Cauchy}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; a, b) = {b\over \pi\left((x-a)^2+b^2\right)}$$


$$f(x; a, b) = {b\over \pi\left((x-a)^2+b^2\right)}$$

### Function: pdf_chi2 (x, n)

Returns the value at *x* of the density function of a Chi-square
random variable 
$\chi^2(n)$
, with $n>0$.
The 
$\chi^2(n)$
random variable is equivalent to the 
$\Gamma\left(n/2,2\right)$
.


The pdf is



$$f(x; n) = \cases{ \displaystyle{x^{n/2-1} e^{-x/2} \over 2^{n/2} \Gamma\left(\displaystyle{n\over 2}\right)} & for $x > 0$ \cr \cr 0 & otherwise }$$


$$f(x; n) =
\cases{
 \displaystyle{x^{n/2-1} e^{-x/2} \over 2^{n/2}
 \Gamma\left(\displaystyle{n\over 2}\right)} & for $x
 > 0$ \cr
\cr
 0 & otherwise
}$$








```maxima
(%i1) load ("distrib")$

(%i2) pdf_chi2(x,n);
                    - x/2  n/2 - 1
                  %e      x        unit_step(x)
(%o2)             -----------------------------
                           n/2       n
                          2    gamma(-)
                                     2
```

### Function: pdf_continuous_uniform (x, a, b)

Returns the value at *x* of the density function of a
${\it ContinuousUniform}(a,b)$
random variable, with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The pdf

$$f(x; a, b) = \cases{ \displaystyle{1\over b-a} & for $0 \le x \le 1$ \cr \cr 0 & otherwise }$$


$$f(x; a, b) =
\cases{
\displaystyle{1\over b-a} & for $0 \le x \le 1$ \cr
\cr
0 & otherwise
}$$



and is 0 otherwise.

### Function: pdf_discrete_uniform (x, n)

Returns the value at *x* of the probability function of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x,n) = {1\over n}$$


$$f(x,n) = {1\over n}$$

### Function: pdf_exp (x, m)

Returns the value at *x* of the density function of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The pdf is

$$f(x; m) = \cases{ me^{-mx} & for $x \ge 0$ \cr 0 & otherwise }$$


$$f(x; m) =
\cases{
me^{-mx} & for $x \ge 0$ \cr
0 & otherwise
}$$









```maxima
(%i1) load ("distrib")$

(%i2) pdf_exp(x,m);
                       - m x
(%o2)                %e      m unit_step(x)
```

### Function: pdf_f (x, m, n)

Returns the value at *x* of the density function of a F random variable $F(m,n)$, with $m,n>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; m, n) = \cases{ B\left(\displaystyle{m\over 2}, \displaystyle{n\over 2}\right)^{-1} \left(\displaystyle{m\over n}\right)^{m/ 2} x^{m/2-1} \left(1 + \displaystyle{m\over n}x\right)^{-\left(n+m\right)/2} & $x > 0$ \cr \cr 0 & otherwise }$$


$$f(x; m, n) =
\cases{
B\left(\displaystyle{m\over 2}, \displaystyle{n\over 2}\right)^{-1}
\left(\displaystyle{m\over n}\right)^{m/ 2}
x^{m/2-1}
\left(1 + \displaystyle{m\over n}x\right)^{-\left(n+m\right)/2} & $x >
0$ \cr
\cr
0 & otherwise
}$$

### Function: pdf_gamma (x, a, b)

Returns the value at *x* of the density function of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The shape parameter is $a$, and the scale parameter is $b$.


The pdf is

$$f(x; a, b) = {x^{a-1}e^{-x/b}\over b^a \Gamma(a)}$$


$$f(x; a, b) = {x^{a-1}e^{-x/b}\over b^a \Gamma(a)}$$

### Function: pdf_general_finite_discrete (x, v)

Returns the value at *x* of the probability function of a general
finite discrete random variable, with vector probabilities $v$,
such that $Pr(X=i) = v_i$. Vector $v$ can be a list of
nonnegative expressions whose components will be normalized to get a
vector of probabilities. To make use of this function, write first
`load("distrib")`.


Note that $i=1$ corresponds to the first element of $v$.








```maxima
(%i1) load ("distrib")$

(%i2) pdf_general_finite_discrete(2, [1/7, 4/7, 2/7]);
                                4
(%o2)                           -
                                7


(%i3) pdf_general_finite_discrete(2, [1, 4, 2]);
                                4
(%o3)                           -
                                7
```

### Function: pdf_geometric (x, p)

Returns the value at *x* of the probability function of a 
${\it Geometric}(p)$
random variable, with
$0 < p \leq 1$


The pdf is

$$f(x; p) = p(1-p)^x$$


$$f(x; p) = p(1-p)^x$$




This is interpreted as the probability of $x$ failures before the first success.


`load("distrib")` loads this function.

### Function: pdf_gumbel (x, a, b)

Returns the value at *x* of the density function of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; a, b) = {1\over b} \exp\left[{a-x\over b} - \exp\left({a-x\over b}\right)\right]$$


$$f(x; a, b) = {1\over b} \exp\left[{a-x\over b} - \exp\left({a-x\over b}\right)\right]$$

### Function: pdf_hypergeometric (x, n_1, n_2, n)

Returns the value at *x* of the probability function of a 
${\it Hypergeometric}(n1,n2,n)$
random variable, with $n_1$, $n_2$ and $n$ non negative
integers and $n\leq n_1+n_2$.
Being $n_1$ the number of objects of class A, $n_2$ the number of objects of class B, and
$n$ the size of the sample without replacement, this function returns the probability of
event "exactly *x* objects are of class A". 


To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; n_1, n_2, n) = {\displaystyle{n_1\choose x} {n_2 \choose n-x} \over \displaystyle{n_2+n_1 \choose n}}$$


$$f(x; n_1, n_2, n) = {\displaystyle{n_1\choose x} {n_2 \choose n-x}
\over \displaystyle{n_2+n_1 \choose n}}$$

### Function: pdf_laplace (x, a, b)

Returns the value at *x* of the density function of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


Here, $a$ is the location parameter (or mean), and $b$ is
the scale parameter, related to the variance.


The pdf is

$$f(x; a, b) = {1\over 2b}\exp\left(-{|x-a|\over b}\right)$$


$$f(x; a, b) = {1\over 2b}\exp\left(-{|x-a|\over b}\right)$$

### Function: pdf_logistic (x, a, b)

Returns the value at *x* of the density function of a 
${\it Logistic}(a,b)$
random variable , with $b>0$. To make use of this function, write first `load("distrib")`.


$a$ is the location parameter and $b$ is the scale
parameter.


The pdf is

$$f(x; a, b) = {e^{-(x-a)/b} \over b\left(1 + e^{-(x-a)/b}\right)^2}$$


$$f(x; a, b) = {e^{-(x-a)/b} \over b\left(1 + e^{-(x-a)/b}\right)^2}$$

### Function: pdf_lognormal (x, m, s)

Returns the value at *x* of the density function of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; m, s) = \cases{ \displaystyle{1\over x s \sqrt{2\pi}} \exp\left(-\displaystyle{\left(\log x - m\right)^2\over 2s^2}\right) & for $x \ge 0$ \cr \cr 0 & for $x < 0$ }$$


$$f(x; m, s) =
\cases{
\displaystyle{1\over x s \sqrt{2\pi}}
\exp\left(-\displaystyle{\left(\log x - m\right)^2\over 2s^2}\right) & for $x \ge
0$ \cr
\cr
0 & for $x < 0$
}$$

### Function: pdf_negative_binomial (x, n, p)

Returns the value at *x* of the probability function of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; n, p) = {x+n-1 \choose n-1} (1-p)^xp^n$$


$$f(x; n, p) = {x+n-1 \choose n-1} (1-p)^xp^n$$

### Function: pdf_noncentral_chi2 (x, n, ncp)

Returns the value at $x$ of the density function of a 
noncentral 
$\chi^2$
random
variable 
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality
parameter 
$ncp \ge 0.$
To 
make use of this function, write first `load("distrib")`.


For $x < 0$, the pdf is 0, and for 
$x \ge 0$
the pdf is

$$f(x; n, \lambda) = {1\over 2}e^{-(x+\lambda)/2} \left(x\over \lambda\right)^{n/4-1/2}I_{{n\over 2} - 1}\left(\sqrt{n \lambda}\right)$$


$$f(x; n, \lambda) =
{1\over 2}e^{-(x+\lambda)/2} \left(x\over
\lambda\right)^{n/4-1/2}I_{{n\over 2} - 1}\left(\sqrt{n \lambda}\right)
$$

### Function: pdf_noncentral_student_t (x, n, ncp)

Returns the value at *x* of the density function of a noncentral
Student random variable 
${\it nc\_t}(n, ncp)$
, with $n>0$ degrees of freedom and noncentrality parameter $ncp$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; n, \mu) = \left[\sqrt{n} B\left({1\over 2}, {n\over 2}\right)\right]^{-1}\left(1+{x^2\over n}\right)^{-{(n+1)/2}} e^{-\mu^2/ 2} \bigg[A_n(x; \mu) + B_n(x; \mu)\bigg]$$


$$f(x; n, \mu) = \left[\sqrt{n} B\left({1\over 2}, {n\over
2}\right)\right]^{-1}\left(1+{x^2\over n}\right)^{-{(n+1)/2}}
e^{-\mu^2/ 2}
\bigg[A_n(x; \mu) + B_n(x; \mu)\bigg]$$



where

$$\eqalign{ A_n(x;\mu) &= {}_1F_1\left({n+1\over 2}; {1\over 2}; {\mu^2 x^2\over 2\left(x^2+n\right)}\right) \cr B_n(x;\mu) &= {\sqrt{2}\mu x \over \sqrt{x^2+n}} {\Gamma\left({n\over 2} + 1\right)\over \Gamma\left({n+1\over 2}\right)}\; {}_1F_1\left({n\over 2} + 1; {3\over 2}; {\mu^2 x^2\over 2\left(x^2+n\right)}\right) }$$


$$\eqalign{
A_n(x;\mu) &= {}_1F_1\left({n+1\over 2}; {1\over 2}; {\mu^2 x^2\over
2\left(x^2+n\right)}\right) \cr
B_n(x;\mu) &= {\sqrt{2}\mu x \over \sqrt{x^2+n}} {\Gamma\left({n\over
2} + 1\right)\over \Gamma\left({n+1\over 2}\right)}\;
{}_1F_1\left({n\over 2} + 1; {3\over 2}; {\mu^2 x^2\over
2\left(x^2+n\right)}\right)
}$$



and 
$\mu$
is the non-centrality parameter $ncp$.


Sometimes an extra work is necessary to get the final result.








```maxima
(%i1) load ("distrib")$

(%i2) expand(pdf_noncentral_student_t(3,5,0.1));
rat: replaced 0.018898223650461364 by 15934951/843198350 = 0.018898223650461364

rat: replaced -8.734356480209641 by -294697965/33740089 = -8.734356480209641

rat: replaced 4.136255165816327 by 51033443/12338079 = 4.136255165816332

rat: replaced 1.0806143216420299 by 49366521/45683756 = 1.0806143216420296

rat: replaced 0.0565127306411839 by 5608717/99246965 = 0.05651273064118384

rat: replaced -300.8069396896258 by -79782423/265228 = -300.80693968962555

rat: replaced 160.62691761849732 by 178374907/1110492 = 160.62691761849703
                            7/2                          7/2
      0.042964144174009046 5      1.3236503072892878e-6 5
(%o2) ------------------------- + --------------------------
         3/2   5/2                        sqrt(%pi)
        2    14    sqrt(%pi)
                                                              7/2
                                         1.94793720435093e-4 5
                                       + ------------------------
                                                   %pi


(%i3) float(%);
(%o3)                 0.020805931594056706
```

### Function: pdf_normal (x, m, s)

Returns the value at *x* of the density function of a 
${\it Normal}(m, s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; m, s) = {1\over s\sqrt{2\pi}} e^{\displaystyle -{(x-m)^2\over 2s^2}}$$


$$f(x; m, s) = {1\over s\sqrt{2\pi}} e^{\displaystyle -{(x-m)^2\over 2s^2}}$$

### Function: pdf_pareto (x, a, b)

Returns the value at *x* of the density function of a 
${\it Pareto}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; a, b) = \cases{ \displaystyle{a b^a \over x^{a+1}} & for $x \ge b$ \cr \cr 0 & for $x < b$ }$$


$$f(x; a, b) = 
\cases{
\displaystyle{a b^a \over x^{a+1}} & for $x \ge b$ \cr
\cr
0 & for $x < b$
}$$

### Function: pdf_poisson (x, m)

Returns the value at *x* of the probability function of a 
${\it Poisson}(m)$
random variable, with $m>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; m) = {m^x e^{-m}\over x!}$$


$$f(x; m) = {m^x e^{-m}\over x!}$$

### Function: pdf_rayleigh (x, b)

Returns the value at *x* of the density function of a 
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The pdf is

$$f(x; b) = \cases{ 2b^2 x e^{-b^2 x^2} & for $x \ge 0$ \cr 0 & for $x < 0$ }$$


$$f(x; b) =
\cases{
2b^2 x e^{-b^2 x^2} & for $x \ge 0$ \cr
0 & for $x < 0$
}$$








```maxima
(%i1) load ("distrib")$

(%i2) pdf_rayleigh(x,b);
                         2  2
                      - b  x   2
(%o2)             2 %e        b  x unit_step(x)
```

### Function: pdf_student_t (x, n)

Returns the value at *x* of the density function of a Student
random variable 
$t(n)$
, with $n>0$ degrees of freedom. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; n) = \left[\sqrt{n} B\left({1\over 2}, {n\over 2}\right)\right]^{-1} \left(1+{x^2\over n}\right)^{\displaystyle -{n+1\over 2}}$$


$$f(x; n) = \left[\sqrt{n} B\left({1\over 2}, {n\over 2}\right)\right]^{-1}
\left(1+{x^2\over n}\right)^{\displaystyle -{n+1\over 2}}$$

### Function: pdf_weibull (x, a, b)

Returns the value at *x* of the density function of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The pdf is

$$f(x; a, b) = \cases{ \displaystyle{1\over b} \left({x\over b}\right)^{a-1} e^{-(x/b)^a} & for $x \ge 0$ \cr \cr 0 & for $x < 0$ }$$


$$f(x; a, b) =
\cases{
\displaystyle{1\over b} \left({x\over b}\right)^{a-1} e^{-(x/b)^a} &
for $x \ge 0$ \cr
\cr
0 & for $x < 0$
}$$

### Function: quantile_bernoulli (q, p)

Returns the *q*-quantile of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$; in other words, this is the inverse of `cdf_bernoulli`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_beta (q, a, b)

Returns the *q*-quantile of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$; in other words, this is the inverse of `cdf_beta`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_binomial (q, n, p)

Returns the *q*-quantile of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer; in other words, this is the inverse of `cdf_binomial`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_cauchy (q, a, b)

Returns the *q*-quantile of a 
${\it Cauchy}(a,b)$
random variable, with $b>0$; in other words, this is the inverse of `cdf_cauchy`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_chi2 (q, n)

Returns the *q*-quantile of a Chi-square random variable 
$\chi^2(n)$
, with $n>0$; in other words, this is the inverse of `cdf_chi2`. Argument *q* must be an element of $[0,1]$.


This function has no closed form and it is numerically computed.







```maxima
(%i1) load ("distrib")$

(%i2) quantile_chi2(0.99,9);
(%o2)                   21.66599433346194
```

### Function: quantile_continuous_uniform (q, a, b)

Returns the *q*-quantile of a 
${\it ContinuousUniform}(a,b)$
random
variable, with 
$a \lt b$
; in other words, this is the inverse of `cdf_continuous_uniform`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_discrete_uniform (q, n)

Returns the *q*-quantile of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer; in other words, this is the inverse of `cdf_discrete_uniform`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_exp (q, m)

Returns the *q*-quantile of an 
${\it Exponential}(m)$
random variable, with $m>0$; in other words, this is the inverse of `cdf_exp`. Argument *q* must be an element of $[0,1]$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.








```maxima
(%i1) load ("distrib")$

(%i2) quantile_exp(0.56,5);
(%o2)                  0.1641961104139661


(%i3) quantile_exp(0.56,m);
                       0.8209805520698303
(%o3)                  ------------------
                               m
```

### Function: quantile_f (q, m, n)

Returns the *q*-quantile of a F random variable $F(m,n)$, with $m,n>0$; in other words, this is the inverse of `cdf_f`. Argument *q* must be an element of $[0,1]$.







```maxima
(%i1) load ("distrib")$

(%i2) quantile_f(2/5,sqrt(3),5);
(%o2)                  0.5189478385736904
```

### Function: quantile_gamma (q, a, b)

Returns the *q*-quantile of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$; in other words, this is the inverse of `cdf_gamma`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_general_finite_discrete (q, v)

Returns the *q*-quantile of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.

See also: `pdf_general_finite_discrete`.

### Function: quantile_geometric (q, p)

Returns the *q*-quantile of a 
${\it Geometric}(p)$
random variable,
with 
$0 \lt p \le 1$
;
in other words, this is the inverse of `cdf_geometric`.
Argument *q* must be an element of $[0,1]$.


The probability from which the quantile is derived is defined as $p (1 - p)^x$.
This is interpreted as the probability of $x$ failures before the first success.


`load("distrib")` loads this function.

### Function: quantile_gumbel (q, a, b)

Returns the *q*-quantile of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$; in other words, this is the inverse of `cdf_gumbel`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_hypergeometric (q, n1, n2, n)

Returns the *q*-quantile of a 
${\it Hypergeometric}(n1,n2,n)$
random
variable, with *n1*, *n2* and *n* non negative integers
and $n\leq n1+n2$; in other words, this is the inverse of `cdf_hypergeometric`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_laplace (q, a, b)

Returns the *q*-quantile of a 
${\it Laplace}(a,b)$
random variable, with $b>0$; in other words, this is the inverse of `cdf_laplace`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_logistic (q, a, b)

Returns the *q*-quantile of a 
${\it Logistic}(a,b)$
random variable , with $b>0$; in other words, this is the inverse of `cdf_logistic`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_lognormal (q, m, s)

Returns the *q*-quantile of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$; in other words, this is the inverse of `cdf_lognormal`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.








```maxima
(%i1) load ("distrib")$

(%i2) quantile_lognormal(95/100,0,1);
                     sqrt(2) inverse_erf(9/10)
(%o2)              %e


(%i3) float(%);
(%o3)                   5.180251602233015
```

### Function: quantile_negative_binomial (q, n, p)

Returns the *q*-quantile of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number; in other words, this is the inverse of `cdf_negative_binomial`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_noncentral_chi2 (q, n, ncp)

Returns the *q*-quantile of a noncentral Chi-square random
variable 
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality
parameter 
$ncp \ge 0$
; in other words, this is the inverse of `cdf_noncentral_chi2`. Argument *q* must be an element of $[0,1]$.


This function has no closed form and it is numerically computed.

### Function: quantile_noncentral_student_t (q, n, ncp)

Returns the *q*-quantile of a noncentral Student random variable 
${\it nc\_t}(n, ncp)$
, with $n>0$ degrees of freedom and noncentrality parameter $ncp$; in other words, this is the inverse of `cdf_noncentral_student_t`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_normal (q, m, s)

Returns the *q*-quantile of a 
${\it Normal}(m, s)$
random variable, with $s>0$; in other words, this is the inverse of `cdf_005fnormal`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.








```maxima
(%i1) load ("distrib")$

(%i2) quantile_normal(95/100,0,1);
                                         9
(%o2)                sqrt(2) inverse_erf(--)
                                         10


(%i3) float(%);
(%o3)                  1.6448536269514724
```

See also: `cdf_normal`.

### Function: quantile_pareto (q, a, b)

Returns the *q*-quantile of a 
${\it Pareto}(a,b)$
random variable, with $a,b>0$; in other words, this is the inverse of `cdf_pareto`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_poisson (q, m)

Returns the *q*-quantile of a 
${\it Poisson}(m)$
random variable, with $m>0$; in other words, this is the inverse of `cdf_poisson`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_rayleigh (q, b)

Returns the *q*-quantile of a 
${\it Rayleigh}(b)$
random variable, with $b>0$; in other words, this is the inverse of `cdf_rayleigh`. Argument *q* must be an element of $[0,1]$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.







```maxima
(%i1) load ("distrib")$

(%i2) quantile_rayleigh(0.99,b);
                       2.1459660262893467
(%o2)                  ------------------
                               b
```

### Function: quantile_student_t (q, n)

Returns the *q*-quantile of a Student random variable 
$t(n)$
, with $n>0$; in other words, this is the inverse of `cdf_student_t`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: quantile_weibull (q, a, b)

Returns the *q*-quantile of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$; in other words, this is the inverse of `cdf_weibull`. Argument *q* must be an element of $[0,1]$. To make use of this function, write first `load("distrib")`.

### Function: random_bernoulli (p, random_bernoulli, p, n)

Returns a 
${\it Bernoulli}(p)$
random variate, with $0 \leq p \leq 1$. Calling `random_bernoulli` with a second argument *n*, a random sample of size *n* will be simulated.


This is a direct application of the `random` built-in Maxima function.


See also `random`. To make use of this function, write first `load("distrib")`.

See also: `random`.

### Function: random_beta (a, b, random_beta, a, b, n)

Returns a 
${\it Beta}(a,b)$
random variate, with $a,b>0$. Calling `random_beta` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is defined in Cheng, R.C.H.  (1978). *Generating Beta Variates with Nonintegral Shape Parameters*. Communications of the ACM, 21:317-322


To make use of this function, write first `load("distrib")`.

### Function: random_binomial (n, p, random_binomial, n, p, m)

Returns a 
${\it Binomial}(n,p)$
random variate, with $0 \leq p \leq 1$ and $n$ a positive integer. Calling `random_binomial` with a third argument *m*, a random sample of size *m* will be simulated.


The implemented algorithm is based on the one described in Kachitvichyanukul, V. and Schmeiser, B.W. (1988) *Binomial Random Variate Generation*. Communications of the ACM, 31, Feb., 216.


To make use of this function, write first `load("distrib")`.

### Function: random_cauchy (a, b, random_cauchy, a, b, n)

Returns a 
${\it Cauchy}(a,b)$
random variate, with $b>0$. Calling `random_cauchy` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_chi2 (n, random_chi2, n, m)

Returns a Chi-square random variate 
$\chi^2(n)$
, with $n>0$. Calling `random_chi2` with a second argument *m*, a random sample of size *m* will be simulated.


The simulation is based on the Ahrens-Cheng algorithm. See `random_gamma` for details.


To make use of this function, write first `load("distrib")`.

### Function: random_continuous_uniform (a, b, random_continuous_uniform, a, b, n)

Returns a 
${\it ContinuousUniform}(a,b)$
random variate, with 
$a \lt b.$
Calling `random_continuous_uniform` with a third argument *n*, a random sample of size *n* will be simulated.


This is a direct application of the `random` built-in Maxima function.


See also `random`. To make use of this function, write first `load("distrib")`.

See also: `random`.

### Function: random_discrete_uniform (n, random_discrete_uniform, n, m)

Returns a 
${\it DiscreteUniform}(n)$
random variate, with $n$ a strictly positive integer. Calling `random_discrete_uniform` with a second argument *m*, a random sample of size *m* will be simulated.


This is a direct application of the `random` built-in Maxima function.


See also `random`. To make use of this function, write first `load("distrib")`.

See also: `random`.

### Function: random_exp (m, random_exp, m, k)

Returns an 
${\it Exponential}(m)$
random variate, with $m>0$. Calling `random_exp` with a second argument *k*, a random sample of size *k* will be simulated.


The simulation algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_f (m, n, random_f, m, n, k)

Returns a F random variate $F(m,n)$, with $m,n>0$. Calling `random_f` with a third argument *k*, a random sample of size *k* will be simulated.


The simulation algorithm is based on the fact that if *X* is a
$Chi^2(m)$ random variable and $Y$ is a 
$\chi^2(n)$
random variable, then

$$F={{n X}\over{m Y}}$$


$$F={{n X}\over{m Y}}$$



is a F random variable with *m* and *n* degrees of freedom, $F(m,n)$.


To make use of this function, write first `load("distrib")`.

### Function: random_gamma (a, b, random_gamma, a, b, n)

Returns a 
$\Gamma\left(a,b\right)$
random variate, with $a,b>0$. Calling `random_gamma` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is a combination of two procedures, depending on the value of parameter *a*:


For 
$a \ge 1,$
Cheng, R.C.H. and Feast, G.M. (1979). *Some simple gamma variate generators*. Appl. Stat., 28, 3, 290-295.


For 
$0 \lt a \lt 1,$
Ahrens, J.H. and Dieter, U. (1974). *Computer methods for sampling from gamma, , poisson and binomial distributions*. Computing, 12, 223-246.


To make use of this function, write first `load("distrib")`.

### Function: random_general_finite_discrete (v, random_general_finite_discrete, v, m)

Returns a general finite discrete random variate, with vector probabilities $v$. Calling `random_general_finite_discrete` with a second argument *m*, a random sample of size *m* will be simulated.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.








```maxima
(%i1) load ("distrib")$

(%i2) random_general_finite_discrete([1,3,1,5]);
(%o2)                           4


(%i3) random_general_finite_discrete([1,3,1,5], 10);
(%o3)            [4, 4, 2, 4, 2, 2, 4, 2, 2, 4]
```

See also: `pdf_general_finite_discrete`.

### Function: random_geometric (p, random_geometric, p, n)

`random_geometric(p)` returns one random sample from a 
${\it Geometric}(p)$
distribution,
with 
$0 \lt p \le 1.$


`random_geometric(p, n)` returns a list of *n* random samples.


The algorithm is based on simulation of Bernoulli trials.


The probability from which the random sample is derived is defined as $p (1 - p)^x$.
This is interpreted as the probability of $x$ failures before the first success.


`load("distrib")` loads this function.

### Function: random_gumbel (a, b, random_gumbel, a, b, n)

Returns a 
${\it Gumbel}(a,b)$
random variate, with $b>0$. Calling `random_gumbel` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_hypergeometric (n1, n2, n, random_hypergeometric, n1, n2, n, m)

Returns a 
${\it Hypergeometric}(n1,n2,n)$
random variate,
with *n1*, *n2* and *n* non negative integers and 
$n \le n_1 + n_2.$
Calling `random_hypergeometric` with a fourth argument *m*, a random sample of size *m* will be simulated.


Algorithm described in Kachitvichyanukul, V., Schmeiser, B.W. (1985) *Computer generation of hypergeometric random variates.* Journal of Statistical Computation and Simulation 22, 127-145.


To make use of this function, write first `load("distrib")`.

### Function: random_laplace (a, b, random_laplace, a, b, n)

Returns a 
${\it Laplace}(a,b)$
random variate, with $b>0$. Calling `random_laplace` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_logistic (a, b, random_logistic, a, b, n)

Returns a 
${\it Logistic}(a,b)$
random variate, with $b>0$. Calling `random_logistic` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_lognormal (m, s, random_lognormal, m, s, n)

Returns a 
${\it Lognormal}(m,s)$
random variate, with $s>0$. Calling `random_lognormal` with a third argument *n*, a random sample of size *n* will be simulated.


Log-normal variates are simulated by means of random normal variates. See `random_normal` for details.


To make use of this function, write first `load("distrib")`.

### Function: random_negative_binomial (n, p, random_negative_binomial, n, p, m)

Returns a 
${\it NegativeBinomial}(n,p)$
random variate, with $0 < p \leq 1$ and $n$ a positive number. Calling `random_negative_binomial` with a third argument *m*, a random sample of size *m* will be simulated.


Algorithm described in Devroye, L. (1986) *Non-Uniform Random Variate Generation*. Springer Verlag, p. 480.


To make use of this function, write first `load("distrib")`.

### Function: random_noncentral_chi2 (n, ncp, random_noncentral_chi2, n, ncp, m)

Returns a noncentral Chi-square random variate
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality parameter 
$ncp \ge 0.$
Calling `random_noncentral_chi2` with a third argument *m*, a random sample of size *m* will be simulated.


To make use of this function, write first `load("distrib")`.

### Function: random_noncentral_student_t (n, ncp, random_noncentral_student_t, n, ncp, m)

Returns a noncentral Student random variate 
${\it nc\_t}(n, ncp)$
, with $n>0$. Calling `random_noncentral_student_t` with a third argument *m*, a random sample of size *m* will be simulated.


The implemented algorithm is based on the fact that if *X* is a
normal random variable 
${\it Normal}(ncp, 1)$
and $S^2$ is
a 
$\chi^2$
random variable with *n* degrees of freedom, 
$\chi^2(n)$
, then

$$U={{X}\over{\sqrt{{S^2}\over{n}}}}$$


$$U={{X}\over{\sqrt{{S^2}\over{n}}}}$$



is a noncentral Student random variable with $n$ degrees of
freedom and noncentrality parameter $ncp$, 
${\it nc\_t}(n, ncp)$
.


To make use of this function, write first `load("distrib")`.

### Function: random_normal (m, s, random_normal, m, s, n)

Returns a 
${\it Normal}(m, s)$
random variate, with $s>0$. Calling `random_normal` with a third argument *n*, a random sample of size *n* will be simulated.


This is an implementation of the Box-Mueller algorithm, as described in Knuth, D.E. (1981) *Seminumerical Algorithms. The Art of Computer Programming.* Addison-Wesley.


To make use of this function, write first `load("distrib")`.

### Function: random_pareto (a, b, random_pareto, a, b, n)

Returns a 
${\it Pareto}(a,b)$
random variate, with $a>0,b>0$. Calling `random_pareto` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_poisson (m, random_poisson, m, n)

Returns a 
${\it Poisson}(m)$
random variate, with $m>0$. Calling `random_poisson` with a second argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is the one described in Ahrens, J.H. and Dieter, U. (1982) *Computer Generation of Poisson Deviates From Modified Normal Distributions*. ACM Trans. Math. Software, 8, 2, June,163-179.


To make use of this function, write first `load("distrib")`.

### Function: random_rayleigh (b, random_rayleigh, b, n)

Returns a 
${\it Rayleigh}(b)$
random variate, with $b>0$. Calling `random_rayleigh` with a second argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: random_student_t (n, random_student_t, n, m)

Returns a Student random variate 
$t(n)$
, with $n>0$. Calling `random_student_t` with a second argument *m*, a random sample of size *m* will be simulated.


The implemented algorithm is based on the fact that if $Z$ is a
normal random variable 
${\it Normal}(0, 1)$
and $S^2$ is
a 
$\chi^2$
random variable with $n$ degrees of
freedom, 
$\chi^2(n)$
, then



$$X={{Z}\over{\sqrt{{S^2}\over{n}}}}$$


$$X={{Z}\over{\sqrt{{S^2}\over{n}}}}$$


is a Student random variable with $n$ degrees of freedom, 
$t(n)$
.


To make use of this function, write first `load("distrib")`.

### Function: random_weibull (a, b, random_weibull, a, b, n)

Returns a 
${\it Weibull}(a,b)$
random variate, with $a,b>0$. Calling `random_weibull` with a third argument *n*, a random sample of size *n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

### Function: skewness_bernoulli (p)

Returns the skewness coefficient of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$.


The 
${\it Bernoulli}(p)$
random variable is equivalent to the 
${\it Binomial}(1,p)$
.


The skewness coefficient is

$$SK[X] = {1-2p \over \sqrt{p(1-p)}}$$


$$SK[X] = {1-2p \over \sqrt{p(1-p)}}$$









```maxima
(%i1) load ("distrib")$

(%i2) skewness_bernoulli(p);
                             1 - 2 p
(%o2)                    ---------------
                         sqrt((1 - p) p)
```

### Function: skewness_beta (a, b)

Returns the skewness coefficient of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {2(b-a)\sqrt{a+b+1} \over (a+b+2)\sqrt{ab}}$$


$$SK[X] = {2(b-a)\sqrt{a+b+1} \over (a+b+2)\sqrt{ab}}$$

### Function: skewness_binomial (n, p)

Returns the skewness coefficient of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {1-2p\over \sqrt{np(1-p)}}$$


$$SK[X] = {1-2p\over \sqrt{np(1-p)}}$$

### Function: skewness_chi2 (n)

Returns the skewness coefficient of a Chi-square random variable 
$\chi^2(n)$
, with $n>0$.


The 
$\chi^2(n)$
random variable is equivalent to the 
$\Gamma\left(n/2,2\right)$
.


The skewness coefficient is

$$SK[X] = \sqrt{8\over n}$$


$$SK[X] = \sqrt{8\over n}$$









```maxima
(%i1) load ("distrib")$

(%i2) skewness_chi2(n);
                               3/2
                              2
(%o2)                        -------
                             sqrt(n)
```

### Function: skewness_continuous_uniform (a, b)

Returns the skewness coefficient of a 
${\it ContinuousUniform}(a,b)$
random variable, with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = 0$$


$$SK[X] = 0$$

### Function: skewness_discrete_uniform (n)

Returns the skewness coefficient of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = 0$$


$$SK[X] = 0$$

### Function: skewness_exp (m)

Returns the skewness coefficient of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The skewness coefficient is

$$SK[X] = 2$$


$$SK[X] = 2$$









```maxima
(%i1) load ("distrib")$

(%i2) skewness_exp(m);
(%o2)                           2
```

### Function: skewness_f (m, n)

Returns the skewness coefficient of a F random variable $F(m,n)$, with $m>0, n>6$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {(n+2m-2)\sqrt{8(n-4)} \over (n-6)\sqrt{m(n+m-2)}}$$


$$SK[X] = {(n+2m-2)\sqrt{8(n-4)} \over (n-6)\sqrt{m(n+m-2)}}$$

### Function: skewness_gamma (a, b)

Returns the skewness coefficient of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {2\over \sqrt{a}}$$


$$SK[X] = {2\over \sqrt{a}}$$

### Function: skewness_general_finite_discrete (v)

Returns the skewness coefficient of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.

See also: `pdf_general_finite_discrete`.

### Function: skewness_geometric (p)

Returns the skewness coefficient of a 
${\it Geometric}(p)$
random variable, with
$0 < p \leq 1$.


The skewness coefficient is

$$SK[X] = {2-p \over \sqrt{1-p}}$$


$$SK[X] = {2-p \over \sqrt{1-p}}$$




`load("distrib")` loads this function.

### Function: skewness_gumbel (a, b)

Returns the skewness coefficient of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$.


The skewness coefficient is

$$SK[X] = {12\sqrt{6}\over \pi^3} \zeta(3)$$


$$SK[X] = {12\sqrt{6}\over \pi^3} \zeta(3)$$









```maxima
(%i1) load ("distrib")$

(%i2) skewness_gumbel(a,b);
                            3/2
                         2 6    zeta(3)
(%o2)                    --------------
                                 3
                              %pi
```

where `zeta` stands for the Riemann’s zeta function.

### Function: skewness_hypergeometric (n_1, n_2, n)

Returns the skewness coefficient of a 
${\it Hypergeometric}(n1,n2,n)$
random variable, with $n_1$, $n_2$ and $n$ non negative integers and $n\leq n1+n2$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {(n_2-n_2)(n_1+n_2-2n)\over n_1+n_2-2} \sqrt{n_1+n_2-1 \over n n_1 n_2 (n_1+n_2-n)}$$


$$SK[X] = {(n_2-n_2)(n_1+n_2-2n)\over n_1+n_2-2}
\sqrt{n_1+n_2-1 \over n n_1 n_2 (n_1+n_2-n)}$$

### Function: skewness_laplace (a, b)

Returns the skewness coefficient of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = 0$$


$$SK[X] = 0$$

### Function: skewness_logistic (a, b)

Returns the skewness coefficient of a 
${\it Logistic}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = 0$$


$$SK[X] = 0$$

### Function: skewness_lognormal (m, s)

Returns the skewness coefficient of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = \left(\exp\left(s^2\right)+2\right)\sqrt{\exp\left(s^2\right)-1}$$


$$SK[X] = \left(\exp\left(s^2\right)+2\right)\sqrt{\exp\left(s^2\right)-1}$$

### Function: skewness_negative_binomial (n, p)

Returns the skewness coefficient of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {2-p \over \sqrt{n(1-p)}}$$


$$SK[X] = {2-p \over \sqrt{n(1-p)}}$$

### Function: skewness_noncentral_chi2 (n, ncp)

Returns the skewness coefficient of a noncentral Chi-square random
variable
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality
parameter 
$ncp \ge 0.$


The skewness coefficient is

$$SK[X] = {2^{3/2}(n+3\mu) \over (n+2\mu)^{3/2}}$$


$$SK[X] = {2^{3/2}(n+3\mu) \over (n+2\mu)^{3/2}}$$



where 
$\mu$
is the noncentrality parameter *ncp*.

### Function: skewness_noncentral_student_t (n, ncp)

Returns the skewness coefficient of a noncentral Student random
variable 
${\it nc\_t}(n, ncp)$
, with $n>3$ degrees of freedom and noncentrality parameter $ncp$. To make use of this function, write first `load("distrib")`.





If $U$ is a non-central Student’s $t$ random variable with
$n$ degrees of freedom and a noncentrality parameter 
$\mu,$
the skewness is

$$\eqalign{ SK[U] &= {\mu\sqrt{n}\,\Gamma\left({{n-1}\over{2}}\right) \over{\sqrt{2}\Gamma\left({{n }\over{2}}\right)\sigma^{3}}}\left({{n \left(2n+\mu^2-3\right)}\over{\left(n-3\right)\left(n-2\right)}} -2\sigma^2\right) \cr \sigma^2 &= {{n\left(\mu^2+1\right)}\over{n-2}}-{{n \mu^2\, \Gamma\left({{n-1}\over{2}}\right)^2}\over{2\Gamma\left({{n }\over{2}}\right)^2}} }$$


$$\eqalign{
SK[U] &= 
{\mu\sqrt{n}\,\Gamma\left({{n-1}\over{2}}\right)
\over{\sqrt{2}\Gamma\left({{n
 }\over{2}}\right)\sigma^{3}}}\left({{n
 \left(2n+\mu^2-3\right)}\over{\left(n-3\right)\left(n-2\right)}}
 -2\sigma^2\right) \cr
 \sigma^2 &= {{n\left(\mu^2+1\right)}\over{n-2}}-{{n \mu^2\,
 \Gamma\left({{n-1}\over{2}}\right)^2}\over{2\Gamma\left({{n
 }\over{2}}\right)^2}}
}
$$

### Function: skewness_normal (m, s)

Returns the skewness coefficient of a 
${\it Normal}(m, s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = 0$$


$$SK[X] = 0$$

### Function: skewness_pareto (a, b)

Returns the skewness coefficient of a 
${\it Pareto}(a,b)$
random variable, with $a>3,b>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {2(a+1)\over a-3} \sqrt{a-2\over a}$$


$$SK[X] = {2(a+1)\over a-3} \sqrt{a-2\over a}$$

### Function: skewness_poisson (m)

Returns the skewness coefficient of a 
${\it Poisson}(m)$
random variable, with $m>0$. To make use of this function, write first `load("distrib")`.


The skewness is

$$SK[X] = {1\over \sqrt{m}}$$


$$SK[X] = {1\over \sqrt{m}}$$

### Function: skewness_rayleigh (b)

Returns the skewness coefficient of a
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The skewness coefficient is

$$SK[X] = {2\sqrt{\pi}(\pi - 3)\over (4-\pi)^{3/2}}$$


$$SK[X] = {2\sqrt{\pi}(\pi - 3)\over (4-\pi)^{3/2}}$$









```maxima
(%i1) load ("distrib")$

(%i2) skewness_rayleigh(b);
                         3/2
                      %pi      3 sqrt(%pi)
                      ------ - -----------
                        4           4
(%o2)                 --------------------
                               %pi 3/2
                          (1 - ---)
                                4
```

### Function: skewness_student_t (n)

Returns the skewness coefficient of a Student random variable 
$t(n)$
, with $n>3$, which is always equal to 0. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = 0$$


$$SK[X] = 0$$

### Function: skewness_weibull (a, b)

Returns the skewness coefficient of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The skewness coefficient is

$$SK[X] = {\displaystyle\Gamma\left(1+{3\over a}\right) -3\Gamma\left(1+{1\over a}\right)\Gamma\left(1+{2\over a}\right)+2\Gamma\left(1+{1\over a}\right)^3 \over \displaystyle\left[\Gamma\left(1+{2\over a}\right)-\Gamma\left(1+{1\over a}\right)^2\right]^{3/2} }$$


$$SK[X] = {\displaystyle\Gamma\left(1+{3\over a}\right)
-3\Gamma\left(1+{1\over a}\right)\Gamma\left(1+{2\over
a}\right)+2\Gamma\left(1+{1\over a}\right)^3
 \over
 \displaystyle\left[\Gamma\left(1+{2\over a}\right)-\Gamma\left(1+{1\over
 a}\right)^2\right]^{3/2}
} 
$$

### Function: std_bernoulli (p)

Returns the standard deviation of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$.


The 
${\it Bernoulli}(p)$
random variable is equivalent to the
${\it Binomial}(1,p)$
.


The standard deviation is

$$D[X] = \sqrt{p(1-p)}$$


$$D[X] = \sqrt{p(1-p)}$$









```maxima
(%i1) load ("distrib")$

(%i2) std_bernoulli(p);
(%o2)                    sqrt((1 - p) p)
```

### Function: std_beta (a, b)

Returns the standard deviation of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {1\over a+b}\sqrt{ab\over a+b+1}$$


$$D[X] = {1\over a+b}\sqrt{ab\over a+b+1}$$

### Function: std_binomial (n, p)

Returns the standard deviation of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = \sqrt{np(1-p)}$$


$$D[X] = \sqrt{np(1-p)}$$

### Function: std_chi2 (n)

Returns the standard deviation of a Chi-square random variable 
$\chi^2(n)$
, with $n>0$.


The 
$\chi^2(n)$
random variable is equivalent to the 
$\Gamma\left(n/2,2\right)$
.


The standard deviation is

$$D[X] = \sqrt{2n}$$


$$D[X] = \sqrt{2n}$$









```maxima
(%i1) load ("distrib")$

(%i2) std_chi2(n);
(%o2)                    sqrt(2) sqrt(n)
```

### Function: std_continuous_uniform (a, b)

Returns the standard deviation of a 
${\it ContinuousUniform}(a,b)$
random variable, with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {b-a \over 2\sqrt{3}}$$


$$D[X] = {b-a \over 2\sqrt{3}}$$

### Function: std_discrete_uniform (n)

Returns the standard deviation of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {\sqrt{n^2-1} \over 2\sqrt{3}}$$


$$D[X] = {\sqrt{n^2-1} \over 2\sqrt{3}}$$

### Function: std_exp (m)

Returns the standard deviation of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The standard deviation is

$$D[X] = {1\over m}$$


$$D[X] = {1\over m}$$









```maxima
(%i1) load ("distrib")$

(%i2) std_exp(m);
                                1
(%o2)                           -
                                m
```

### Function: std_f (m, n)

Returns the standard deviation of a F random variable $F(m,n)$, with $m>0, n>4$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {\sqrt{2}\, n \over n-2} \sqrt{n+m-2\over m(n-4)}$$


$$D[X] = {\sqrt{2}\, n \over n-2} \sqrt{n+m-2\over m(n-4)}$$

### Function: std_gamma (a, b)

Returns the standard deviation of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = b\sqrt{a}$$


$$D[X] = b\sqrt{a}$$

### Function: std_general_finite_discrete (v)

Returns the standard deviation of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.

See also: `pdf_general_finite_discrete`.

### Function: std_geometric (p)

Returns the standard deviation of a 
${\it Geometric}(p)$
random variable, with
$0 < p \leq 1$.



$$D[X] = {\sqrt{1-p} \over p}$$


$$D[X] = {\sqrt{1-p} \over p}$$



`load("distrib")` loads this function.

### Function: std_gumbel (a, b)

Returns the standard deviation of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {\pi \over \sqrt{6}} b$$


$$D[X] = {\pi \over \sqrt{6}} b$$

### Function: std_hypergeometric (n_1, n_2, n)

Returns the standard deviation of a 
${\it Hypergeometric}(n_1,n_2,n)$
random variable, with $n_1$, $n_2$ and $n$ non negative integers and $n\leq n_1+n_2$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {1\over n_1+n_2}\sqrt{n n_1 n_2 (n_1 + n_2 - n) \over n_1+n_2-1}$$


$$D[X] = {1\over n_1+n_2}\sqrt{n n_1 n_2 (n_1 + n_2 - n) \over n_1+n_2-1}$$

### Function: std_laplace (a, b)

Returns the standard deviation of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = \sqrt{2} b$$


$$D[X] = \sqrt{2} b$$

### Function: std_logistic (a, b)

Returns the standard deviation of a 
${\it Logistic}(a,b)$
random variable , with $b>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {\pi b\over \sqrt{3}}$$


$$D[X] = {\pi b\over \sqrt{3}}$$

### Function: std_lognormal (m, s)

Returns the standard deviation of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = \sqrt{\left(\exp\left(s^2\right) - 1\right)} \exp\left(m+{s^2\over 2}\right)$$


$$D[X] = \sqrt{\left(\exp\left(s^2\right) - 1\right)}
\exp\left(m+{s^2\over 2}\right)$$

### Function: std_negative_binomial (n, p)

Returns the standard deviation of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {\sqrt{n(1-p)}\over p}$$


$$D[X] = {\sqrt{n(1-p)}\over p}$$

### Function: std_noncentral_chi2 (n, ncp)

Returns the standard deviation of a noncentral Chi-square random
variable 
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality
parameter 
$ncp \ge 0.$


The standard deviation is

$$D[X] = \sqrt{2(n+2\mu)}$$


$$D[X] = \sqrt{2(n+2\mu)}$$



where 
$\mu$
is the noncentrality parameter *ncp*.

### Function: std_noncentral_student_t (n, ncp)

Returns the standard deviation of a noncentral Student random variable 
${\it nc\_t}(n, ncp)$
, with $n>2$ degrees of freedom and noncentrality parameter $ncp$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = \sqrt{{n(\mu^2+1)\over n-2} - {n\mu^2\; \Gamma\left(\displaystyle{n-1\over 2}\right)^2 \over 2\Gamma\left(\displaystyle{n\over 2}\right)^2}}$$


$$$$

### Function: std_normal (m, s)

Returns the standard deviation of a 
${\it Normal}(m, s)$
random variable, with $s>0$, namely *s*. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = s$$


$$D[X] = s$$

### Function: std_pareto (a, b)

Returns the standard deviation of a 
${\it Pareto}(a,b)$
random variable, with $a>2,b>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = {b\over a-1} \sqrt{a\over a-2}$$


$$D[X] = {b\over a-1} \sqrt{a\over a-2}$$

### Function: std_poisson (m)

Returns the standard deviation of a 
${\it Poisson}(m)$
random variable, with $m>0$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$V[X] = \sqrt{m}$$


$$V[X] = \sqrt{m}$$

### Function: std_rayleigh (b)

Returns the standard deviation of a 
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The standard deviation is

$$D[X] = {1\over b}\sqrt{\displaystyle 1 - {\pi\over 4}}$$


$$D[X] = {1\over b}\sqrt{\displaystyle 1 - {\pi\over 4}}$$









```maxima
(%i1) load ("distrib")$

(%i2) std_rayleigh(b);
                                   %pi
                          sqrt(1 - ---)
                                    4
(%o2)                     -------------
                                b
```

### Function: std_student_t (n)

Returns the standard deviation of a Student random variable 
$t(n)$
, with $n>2$. To make use of this function, write first `load("distrib")`.


The standard deviation is

$$D[X] = \sqrt{\displaystyle{n\over n-2}}$$


$$D[X] = \sqrt{\displaystyle{n\over n-2}}$$

### Function: std_weibull (a, b)

Returns the standard deviation of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$D[X] = b\sqrt{\Gamma\left(1+{2\over a}\right) - \Gamma\left(1+{1\over a}\right)^2}$$


$$D[X] = b\sqrt{\Gamma\left(1+{2\over a}\right) -
\Gamma\left(1+{1\over a}\right)^2}$$

### Function: var_bernoulli (p)

Returns the variance of a 
${\it Bernoulli}(p)$
random variable, with $0 \leq p \leq 1$.


The 
${\it Bernoulli}(p)$
random variable is equivalent to the 
${\it Binomial}(1,p)$
.


The variance is

$$V[X] = p(1-p)$$


$$V[X] = p(1-p)$$









```maxima
(%i1) load ("distrib")$

(%i2) var_bernoulli(p);
(%o2)                       (1 - p) p
```

### Function: var_beta (a, b)

Returns the variance of a 
${\it Beta}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {ab \over (a+b)^2(a+b+1)}$$


$$V[X] = {ab \over (a+b)^2(a+b+1)}$$

### Function: var_binomial (n, p)

Returns the variance of a 
${\it Binomial}(n,p)$
random variable, with $0 \leq p \leq 1$ and $n$ a positive integer. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = np(1-p)$$


$$V[X] = np(1-p)$$

### Function: var_chi2 (n)

Returns the variance of a Chi-square random variable 
$\chi^2(n)$
, with $n>0$.


The 
$\chi^2(n)$
random variable is equivalent to the 
$\Gamma\left(n/2,2\right)$
.


The variance is

$$V[X] = 2n$$


$$V[X] = 2n$$









```maxima
(%i1) load ("distrib")$

(%i2) var_chi2(n);
(%o2)                          2 n
```

### Function: var_continuous_uniform (a, b)

Returns the variance of a 
${\it ContinuousUniform}(a,b)$
random
variable, with 
$a \lt b.$
To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {(b-a)^2\over 12}$$


$$V[X] = {(b-a)^2\over 12}$$

### Function: var_discrete_uniform (n)

Returns the variance of a 
${\it DiscreteUniform}(n)$
random variable, with $n$ a strictly positive integer. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {n^2-1 \over 12}$$


$$V[X] = {n^2-1 \over 12}$$

### Function: var_exp (m)

Returns the variance of an 
${\it Exponential}(m)$
random variable, with $m>0$.


The 
${\it Exponential}(m)$
random variable is equivalent to the 
${\it Weibull}(1,1/m)$
.


The variance is

$$V[X] = {1\over m^2}$$


$$V[X] = {1\over m^2}$$








```maxima
(%i1) load ("distrib")$

(%i2) var_exp(m);
                               1
(%o2)                          --
                                2
                               m
```

### Function: var_f (m, n)

Returns the variance of a F random variable $F(m,n)$, with $m>0, n>4$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {2n^2(n+m-2) \over m(n-4)(n-2)^2}$$


$$V[X] = {2n^2(n+m-2) \over m(n-4)(n-2)^2}$$

### Function: var_gamma (a, b)

Returns the variance of a 
$\Gamma\left(a,b\right)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = ab^2$$


$$V[X] = ab^2$$

### Function: var_general_finite_discrete (v)

Returns the variance of a general finite discrete random variable, with vector probabilities $v$.


See `pdf_005fgeneral_005ffinite_005fdiscrete` for more details.

See also: `pdf_general_finite_discrete`.

### Function: var_geometric (p)

Returns the variance of a 
${\it Geometric}(p)$
random variable, with
$0 < p \leq 1$.


The variance is

$$V[X] = {1-p\over p^2}$$


$$V[X] = {1-p\over p^2}$$




`load("distrib")` loads this function.

### Function: var_gumbel (a, b)

Returns the variance of a 
${\it Gumbel}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {\pi^2\over 6} b^2$$


$$V[X] = {\pi^2\over 6} b^2$$

### Function: var_hypergeometric (n1, n2, n)

Returns the variance of a hypergeometric  random variable 
${\it Hypergeometric}(n_1,n_2,n)$
,
with $n_1$, $n_2$ and $n$ non negative integers and 
$n \le n_1 + n_2.$
To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {n n_1 n_2 (n_1 + n_2 - n) \over (n_1 + n_2 - 1) (n_1 + n_2)^2}$$


$$V[X] = {n n_1 n_2 (n_1 + n_2 - n)
 \over
 (n_1 + n_2 - 1) (n_1 + n_2)^2}$$

### Function: var_laplace (a, b)

Returns the variance of a 
${\it Laplace}(a,b)$
random variable, with $b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = 2b^2$$


$$V[X] = 2b^2$$

### Function: var_logistic (a, b)

Returns the variance of a 
${\it Logistic}(a,b)$
random variable , with $b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {\pi^2 b^2 \over 3}$$


$$V[X] = {\pi^2 b^2 \over 3}$$

### Function: var_lognormal (m, s)

Returns the variance of a 
${\it Lognormal}(m,s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = \left(\exp\left(s^2\right) - 1\right) \exp\left(2m+s^2\right)$$


$$V[X] = \left(\exp\left(s^2\right) - 1\right) \exp\left(2m+s^2\right)$$

### Function: var_negative_binomial (n, p)

Returns the variance of a 
${\it NegativeBinomial}(n,p)$
random variable, with $0 < p \leq 1$ and $n$ a positive number. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {n(1-p)\over p^2}$$


$$V[X] = {n(1-p)\over p^2}$$

### Function: var_noncentral_chi2 (n, ncp)

Returns the variance of a noncentral Chi-square random variable
m4_noncentral_chi2(n,ncp)
, with $n>0$ and noncentrality parameter 
$ncp \ge 0.$


The variance is

$$V[X] = 2(n+2\mu)$$


$$V[X] = 2(n+2\mu)$$



where 
$\mu$
is the noncentrality parameter *ncp*.

### Function: var_noncentral_student_t (n, ncp)

Returns the variance of a noncentral Student random variable 
${\it nc\_t}(n, ncp)$
, with $n>2$ degrees of freedom and noncentrality parameter $ncp$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {n(\mu^2+1)\over n-2} - {n\mu^2\; \Gamma\left(\displaystyle{n-1\over 2}\right)^2 \over 2\Gamma\left(\displaystyle{n\over 2}\right)^2}$$


$$V[X] = {n(\mu^2+1)\over n-2} - {n\mu^2\; \Gamma\left(\displaystyle{n-1\over 2}\right)^2
\over 2\Gamma\left(\displaystyle{n\over 2}\right)^2}$$




where 
$\mu$
is the noncentrality parameter $ncp$.

### Function: var_normal (m, s)

Returns the variance of a 
${\it Normal}(m, s)$
random variable, with $s>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = s^2$$


$$V[X] = s^2$$

### Function: var_pareto (a, b)

Returns the variance of a 
${\it Pareto}(a,b)$
random variable, with $a>2,b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = {ab^2\over (a-2)(a-1)^2}$$


$$V[X] = {ab^2\over (a-2)(a-1)^2}$$

### Function: var_poisson (m)

Returns the variance of a 
${\it Poisson}(m)$
random variable, with  $m>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = m$$


$$V[X] = m$$

### Function: var_rayleigh (b)

Returns the variance of a 
${\it Rayleigh}(b)$
random variable, with $b>0$.


The 
${\it Rayleigh}(b)$
random variable is equivalent to the 
${\it Weibull}(2,1/b)$
.


The variance is

$$V[X] = {1\over b^2}\left(1-{\pi \over 4}\right)$$


$$V[X] = {1\over b^2}\left(1-{\pi \over 4}\right)$$









```maxima
(%i1) load ("distrib")$

(%i2) var_rayleigh(b);
                                 %pi
                             1 - ---
                                  4
(%o2)                        -------
                                2
                               b
```

### Function: var_student_t (n)

Returns the variance of a Student random variable 
$t(n)$
, with $n>2$.


The variance is

$$V[X] = {n\over n-2}$$


$$V[X] = {n\over n-2}$$








```maxima
(%i1) load ("distrib")$

(%i2) var_student_t(n);
                                n
(%o2)                         -----
                              n - 2
```

### Function: var_weibull (a, b)

Returns the variance of a 
${\it Weibull}(a,b)$
random variable, with $a,b>0$. To make use of this function, write first `load("distrib")`.


The variance is

$$V[X] = b^2\left[\Gamma\left(1+{2\over a}\right) - \Gamma\left(1+{1\over a}\right)^2\right]$$


$$V[X] = b^2\left[\Gamma\left(1+{2\over a}\right) -
\Gamma\left(1+{1\over a}\right)^2\right]$$

