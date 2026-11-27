## distrib

<!-- category: Statistics -->
<!-- keywords: cdf_bernoulli -->
<!-- signatures: cdf_bernoulli(x, p) -->
### Function: cdf_bernoulli (x, p)

Returns the value at *x* of the distribution function of a
$Bernoulli(p)$ random variable, with $0<p<1$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_beta -->
<!-- signatures: cdf_beta(x, a, b) -->
### Function: cdf_beta (x, a, b)

Returns the value at *x* of the distribution function of a $Beta(a,b)$
random variable, with $a,b>0$.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_beta(1/3,15,2);
                             11
(%o2)                     --------
                          14348907
(%i3) float(%);
(%o3)              7.666089131388195E-7
```

<!-- category: Statistics -->
<!-- keywords: cdf_binomial -->
<!-- signatures: cdf_binomial(x, n, p) -->
### Function: cdf_binomial (x, n, p)

Returns the value at *x* of the distribution function of a
$Binomial(n,p)$ random variable, with $0<p<1$ and $n$ a positive
integer.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_binomial(5,7,1/6);
                            7775
(%o2)                       ----
                            7776
(%i3) float(%);
(%o3)               .9998713991769548
```

<!-- category: Statistics -->
<!-- keywords: cdf_cauchy -->
<!-- signatures: cdf_cauchy(x, a, b) -->
### Function: cdf_cauchy (x, a, b)

Returns the value at *x* of the distribution function of a
$Cauchy(a,b)$ random variable, with $b>0$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_chi2 -->
<!-- signatures: cdf_chi2(x, n) -->
### Function: cdf_chi2 (x, n)

Returns the value at *x* of the distribution function of a Chi-square 
random variable $Chi^2(n)$, with $n>0$.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_chi2(3,4);
                                               3
(%o2)      1 - gamma_incomplete_regularized(2, -)
                                               2
(%i3) float(%);
(%o3)               .4421745996289256
```

<!-- category: Statistics -->
<!-- keywords: cdf_continuous_uniform -->
<!-- signatures: cdf_continuous_uniform(x, a, b) -->
### Function: cdf_continuous_uniform (x, a, b)

Returns the value at *x* of the distribution function of a
$Continuous Uniform(a,b)$ random variable, with $a<b$.  To make use
of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_discrete_uniform -->
<!-- signatures: cdf_discrete_uniform(x, n) -->
### Function: cdf_discrete_uniform (x, n)

Returns the value at *x* of the distribution function of a
$Discrete Uniform(n)$ random variable, with $n$ a strictly positive
integer.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_exp -->
<!-- signatures: cdf_exp(x, m) -->
### Function: cdf_exp (x, m)

Returns the value at *x* of the distribution function of an
$Exponential(m)$ random variable, with $m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull distribution is returned.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_exp(x,m);
                                        1
(%o2)                 cdf_weibull(x, 1, -)
                                        m
(%i3) assume(x>0,m>0)$  cdf_exp(x,m);
                                 - m x
(%o4)                      1 - %e
```

<!-- category: Statistics -->
<!-- keywords: cdf_f -->
<!-- signatures: cdf_f(x, m, n) -->
### Function: cdf_f (x, m, n)

Returns the value at *x* of the distribution function of a F random variable
$F(m,n)$, with $m,n>0$.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_f(2,3,9/4);
                                         9  3  3
(%o2)    1 - beta_incomplete_regularized(-, -, --)
                                         8  2  11
(%i3) float(%);
(%o3)                 0.66756728179008
```

<!-- category: Statistics -->
<!-- keywords: cdf_gamma -->
<!-- signatures: cdf_gamma(x, a, b) -->
### Function: cdf_gamma (x, a, b)

Returns the value at *x* of the distribution function of a $Gamma(a,b)$
random variable, with $a,b>0$.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_gamma(3,5,21);
                                              1
(%o2)     1 - gamma_incomplete_regularized(5, -)
                                              7
(%i3) float(%);
(%o3)              4.402663157376807E-7
```

<!-- category: Statistics -->
<!-- keywords: cdf_general_finite_discrete -->
<!-- signatures: cdf_general_finite_discrete(x, v) -->
### Function: cdf_general_finite_discrete (x, v)

Returns the value at *x* of the distribution function of a general finite
discrete random variable, with vector probabilities $v$.


See `pdf_general_finite_discrete` for more details.


Examples:



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

<!-- category: Statistics -->
<!-- keywords: cdf_geometric -->
<!-- signatures: cdf_geometric(x, p) -->
### Function: cdf_geometric (x, p)

Returns the value at *x* of the distribution function of a
$Geometric(p)$ random variable, with $0<p<1$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_gumbel -->
<!-- signatures: cdf_gumbel(x, a, b) -->
### Function: cdf_gumbel (x, a, b)

Returns the value at *x* of the distribution function of a
$Gumbel(a,b)$ random variable, with $b>0$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_hypergeometric -->
<!-- signatures: cdf_hypergeometric(x, n1, n2, n) -->
### Function: cdf_hypergeometric (x, n1, n2, n)

Returns the value at *x* of the distribution function of a
$Hypergeometric(n1,n2,n)$ random variable, with *n1*, *n2* and
*n* non negative integers and $n<=n1+n2$.
See `pdf_hypergeometric` for a more complete description.


To make use of this function, write first `load("distrib")`.

See also: `pdf_hypergeometric`.

<!-- category: Statistics -->
<!-- keywords: cdf_laplace -->
<!-- signatures: cdf_laplace(x, a, b) -->
### Function: cdf_laplace (x, a, b)

Returns the value at *x* of the distribution function of a
$Laplace(a,b)$ random variable, with $b>0$. To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_logistic -->
<!-- signatures: cdf_logistic(x, a, b) -->
### Function: cdf_logistic (x, a, b)

Returns the value at *x* of the distribution function of a
$Logistic(a,b)$ random variable, with $b>0$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_lognormal -->
<!-- signatures: cdf_lognormal(x, m, s) -->
### Function: cdf_lognormal (x, m, s)

Returns the value at *x* of the distribution function of a
$Lognormal(m,s)$ random variable, with $s>0$.  This function is
defined in terms of Maxima’s built-in error function `erf`.



```maxima
(%i1) load ("distrib")$
(%i2) assume(x>0, s>0)$  cdf_lognormal(x,m,s);
                           log(x) - m
                       erf(----------)
                           sqrt(2) s     1
(%o3)                  --------------- + -
                              2          2
```


See also `erf`.

<!-- category: Statistics -->
<!-- keywords: cdf_negative_binomial -->
<!-- signatures: cdf_negative_binomial(x, n, p) -->
### Function: cdf_negative_binomial (x, n, p)

Returns the value at *x* of the distribution function of a
$Negative Binomial(n,p)$ random variable, with $0<p<1$ and $n$
a positive integer.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_negative_binomial(3,4,1/8);
                            3271
(%o2)                      ------
                           524288
(%i3) float(%);
(%o3)              .006238937377929687
```

<!-- category: Statistics -->
<!-- keywords: cdf_noncentral_chi2 -->
<!-- signatures: cdf_noncentral_chi2(x, n, ncp) -->
### Function: cdf_noncentral_chi2 (x, n, ncp)

Returns the value at *x* of the distribution function of a noncentral 
Chi-square random variable $nc_Chi^2(n,ncp)$, with $n>0$ and 
noncentrality parameter $ncp>=0$.  To make use of this function, write 
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_noncentral_student_t -->
<!-- signatures: cdf_noncentral_student_t(x, n, ncp) -->
### Function: cdf_noncentral_student_t (x, n, ncp)

Returns the value at *x* of the distribution function of a noncentral 
Student random variable $nc_t(n,ncp)$, with $n>0$ degrees of freedom 
and noncentrality parameter $ncp$.  This function has no closed form and it 
is numerically computed if the global variable `numer` equals `true` 
or at least one of the arguments is a float,  otherwise it returns a nominal 
expression.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_noncentral_student_t(-2,5,-5);
(%o2) cdf_noncentral_student_t(- 2, 5, - 5)
(%i3) cdf_noncentral_student_t(-2.0,5,-5);
(%o3)          .9952030093319743
```

<!-- category: Statistics -->
<!-- keywords: cdf_normal -->
<!-- signatures: cdf_normal(x, m, s) -->
### Function: cdf_normal (x, m, s)

Returns the value at *x* of the distribution function of a 
$Normal(m,s)$ random variable, with $s>0$.  This function is defined 
in terms of Maxima’s built-in error function `erf`.



```maxima
(%i1) load ("distrib")$
(%i2) assume(s>0)$ cdf_normal(x,m,s);
                             x - m
                       erf(---------)
                           sqrt(2) s    1
(%o3)                  -------------- + -
                             2          2
```


See also `erf`.

<!-- category: Statistics -->
<!-- keywords: cdf_pareto -->
<!-- signatures: cdf_pareto(x, a, b) -->
### Function: cdf_pareto (x, a, b)

Returns the value at *x* of the distribution function of a
$Pareto(a,b)$ random variable, with $a,b>0$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_poisson -->
<!-- signatures: cdf_poisson(x, m) -->
### Function: cdf_poisson (x, m)

Returns the value at *x* of the distribution function of a $Poisson(m)$
random variable, with $m>0$.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_poisson(3,5);
(%o2)       gamma_incomplete_regularized(4, 5)
(%i3) float(%);
(%o3)               .2650259152973623
```

<!-- category: Statistics -->
<!-- keywords: cdf_rayleigh -->
<!-- signatures: cdf_rayleigh(x, b) -->
### Function: cdf_rayleigh (x, b)

Returns the value at *x* of the distribution function of a
$Rayleigh(b)$ random variable, with $b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull distribution is returned.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_rayleigh(x,b);
                                        1
(%o2)                 cdf_weibull(x, 2, -)
                                        b
(%i3) assume(x>0,b>0)$ cdf_rayleigh(x,b);
                                   2  2
                                - b  x
(%o4)                     1 - %e
```

<!-- category: Statistics -->
<!-- keywords: cdf_student_t -->
<!-- signatures: cdf_student_t(x, n) -->
### Function: cdf_student_t (x, n)

Returns the value at *x* of the distribution function of a Student random 
variable $t(n)$, with $n>0$ degrees of freedom.



```maxima
(%i1) load ("distrib")$
(%i2) cdf_student_t(1/2, 7/3);
                                         7  1  28
             beta_incomplete_regularized(-, -, --)
                                         6  2  31
(%o2)    1 - -------------------------------------
                               2
(%i3) float(%);
(%o3)                .6698450596140415
```

<!-- category: Statistics -->
<!-- keywords: cdf_weibull -->
<!-- signatures: cdf_weibull(x, a, b) -->
### Function: cdf_weibull (x, a, b)

Returns the value at *x* of the distribution function of a
$Weibull(a,b)$ random variable, with $a,b>0$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_bernoulli -->
<!-- signatures: kurtosis_bernoulli(p) -->
### Function: kurtosis_bernoulli (p)

Returns the kurtosis coefficient of a $Bernoulli(p)$ random variable,
with $0<p<1$.


The $Bernoulli(p)$ random variable is equivalent to the
$Binomial(1,p)$, therefore when Maxima has not enough information to get
the result, a noun form based on the binomial kurtosis coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_bernoulli(p);
(%o2)                kurtosis_binomial(1, p)
(%i3) assume(0<p,p<1)$ kurtosis_bernoulli(p);
                         1 - 6 (1 - p) p
(%o4)                    ---------------
                            (1 - p) p
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_beta -->
<!-- signatures: kurtosis_beta(a, b) -->
### Function: kurtosis_beta (a, b)

Returns the kurtosis coefficient of a $Beta(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_binomial -->
<!-- signatures: kurtosis_binomial(n, p) -->
### Function: kurtosis_binomial (n, p)

Returns the kurtosis coefficient of a $Binomial(n,p)$ random variable,
with $0<p<1$ and $n$ a positive integer.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_chi2 -->
<!-- signatures: kurtosis_chi2(n) -->
### Function: kurtosis_chi2 (n)

Returns the kurtosis coefficient of a Chi-square random variable 
$Chi^2(n)$, with $n>0$.


The $Chi^2(n)$ random variable is equivalent to the $Gamma(n/2,2)$, 
therefore when Maxima has not enough information to get the result, a noun 
form based on the gamma kurtosis coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_chi2(n);
                                     n
(%o2)                 kurtosis_gamma(-, 2)
                                     2
(%i3) assume(n>0)$ kurtosis_chi2(n);

                               12
(%o4)                          --
                               n
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_continuous_uniform -->
<!-- signatures: kurtosis_continuous_uniform(a, b) -->
### Function: kurtosis_continuous_uniform (a, b)

Returns the kurtosis coefficient of a $Continuous Uniform(a,b)$ random
variable, with $a<b$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_discrete_uniform -->
<!-- signatures: kurtosis_discrete_uniform(n) -->
### Function: kurtosis_discrete_uniform (n)

Returns the kurtosis coefficient of a $Discrete Uniform(n)$ random
variable, with $n$ a strictly positive integer.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_exp -->
<!-- signatures: kurtosis_exp(m) -->
### Function: kurtosis_exp (m)

Returns the kurtosis coefficient of an $Exponential(m)$ random variable,
with $m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull kurtosis coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_exp(m);
                                         1
(%o2)                kurtosis_weibull(1, -)
                                         m
(%i3) assume(m>0)$  kurtosis_exp(m);
(%o4)                           6
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_f -->
<!-- signatures: kurtosis_f(m, n) -->
### Function: kurtosis_f (m, n)

Returns the kurtosis coefficient of a F random variable $F(m,n)$, with
$m>0, n>8$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_gamma -->
<!-- signatures: kurtosis_gamma(a, b) -->
### Function: kurtosis_gamma (a, b)

Returns the kurtosis coefficient of a $Gamma(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_general_finite_discrete -->
<!-- signatures: kurtosis_general_finite_discrete(v) -->
### Function: kurtosis_general_finite_discrete (v)

Returns the kurtosis coefficient of a general finite discrete random variable,
with vector probabilities $v$.


See `pdf_general_finite_discrete` for more details.

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_geometric -->
<!-- signatures: kurtosis_geometric(p) -->
### Function: kurtosis_geometric (p)

Returns the kurtosis coefficient of a geometric random variable  $Geo(p)$,
with $0<p<1$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_gumbel -->
<!-- signatures: kurtosis_gumbel(a, b) -->
### Function: kurtosis_gumbel (a, b)

Returns the kurtosis coefficient of a $Gumbel(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_hypergeometric -->
<!-- signatures: kurtosis_hypergeometric(n1, n2, n) -->
### Function: kurtosis_hypergeometric (n1, n2, n)

Returns the kurtosis coefficient of a $Hypergeometric(n1,n2,n)$ random
variable, with *n1*, *n2* and *n* non negative integers and
$n<=n1+n2$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_laplace -->
<!-- signatures: kurtosis_laplace(a, b) -->
### Function: kurtosis_laplace (a, b)

Returns the kurtosis coefficient of a $Laplace(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_logistic -->
<!-- signatures: kurtosis_logistic(a, b) -->
### Function: kurtosis_logistic (a, b)

Returns the kurtosis coefficient of a $Logistic(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_lognormal -->
<!-- signatures: kurtosis_lognormal(m, s) -->
### Function: kurtosis_lognormal (m, s)

Returns the kurtosis coefficient of a $Lognormal(m,s)$ random variable,
with $s>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_negative_binomial -->
<!-- signatures: kurtosis_negative_binomial(n, p) -->
### Function: kurtosis_negative_binomial (n, p)

Returns the kurtosis coefficient of a $Negative Binomial(n,p)$ random
variable, with $0<p<1$ and $n$ a positive integer.  To make use of
this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_noncentral_chi2 -->
<!-- signatures: kurtosis_noncentral_chi2(n, ncp) -->
### Function: kurtosis_noncentral_chi2 (n, ncp)

Returns the kurtosis coefficient of a noncentral Chi-square random variable
$nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality parameter
$ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: kurtosis_noncentral_student_t -->
<!-- signatures: kurtosis_noncentral_student_t(n, ncp) -->
### Function: kurtosis_noncentral_student_t (n, ncp)

Returns the kurtosis coefficient of a noncentral Student random variable 
$nc_t(n,ncp)$, with $n>4$ degrees of freedom and noncentrality 
parameter $ncp$.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_normal -->
<!-- signatures: kurtosis_normal(m, s) -->
### Function: kurtosis_normal (m, s)

Returns the kurtosis coefficient of a $Normal(m,s)$ random variable, with 
$s>0$, which is always equal to 0.  To make use of this function, write 
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_pareto -->
<!-- signatures: kurtosis_pareto(a, b) -->
### Function: kurtosis_pareto (a, b)

Returns the kurtosis coefficient of a $Pareto(a,b)$ random variable, with
$a>4,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_poisson -->
<!-- signatures: kurtosis_poisson(m) -->
### Function: kurtosis_poisson (m)

Returns the kurtosis coefficient of a Poisson random variable  $Poi(m)$,
with $m>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_rayleigh -->
<!-- signatures: kurtosis_rayleigh(b) -->
### Function: kurtosis_rayleigh (b)

Returns the kurtosis coefficient of a $Rayleigh(b)$ random variable, with
$b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull kurtosis coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_rayleigh(b);
                                         1
(%o2)                kurtosis_weibull(2, -)
                                         b
(%i3) assume(b>0)$ kurtosis_rayleigh(b);
                                  2
                             3 %pi
                         2 - ------
                               16
(%o4)                    ---------- - 3
                              %pi 2
                         (1 - ---)
                               4
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_student_t -->
<!-- signatures: kurtosis_student_t(n) -->
### Function: kurtosis_student_t (n)

Returns the kurtosis coefficient of a Student random variable $t(n)$, with 
$n>4$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_weibull -->
<!-- signatures: kurtosis_weibull(a, b) -->
### Function: kurtosis_weibull (a, b)

Returns the kurtosis coefficient of a $Weibull(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_bernoulli -->
<!-- signatures: mean_bernoulli(p) -->
### Function: mean_bernoulli (p)

Returns the mean of a $Bernoulli(p)$ random variable, with $0<p<1$.


The $Bernoulli(p)$ random variable is equivalent to the
$Binomial(1,p)$, therefore when Maxima has not enough information to get
the result, a noun form based on the binomial mean is returned.



```maxima
(%i1) load ("distrib")$
(%i2) mean_bernoulli(p);
(%o2)                  mean_binomial(1, p)
(%i3) assume(0<p,p<1)$ mean_bernoulli(p);
(%o4)                           p
```

<!-- category: Statistics -->
<!-- keywords: mean_beta -->
<!-- signatures: mean_beta(a, b) -->
### Function: mean_beta (a, b)

Returns the mean of a $Beta(a,b)$ random variable, with $a,b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_binomial -->
<!-- signatures: mean_binomial(n, p) -->
### Function: mean_binomial (n, p)

Returns the mean of a $Binomial(n,p)$ random variable, with $0<p<1$
and $n$ a positive integer.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_chi2 -->
<!-- signatures: mean_chi2(n) -->
### Function: mean_chi2 (n)

Returns the mean of a Chi-square random variable $Chi^2(n)$, with 
$n>0$.


The $Chi^2(n)$ random variable is equivalent to the $Gamma(n/2,2)$, 
therefore when Maxima has not enough information to get the result, a noun 
form based on the gamma mean is returned.



```maxima
(%i1) load ("distrib")$
(%i2) mean_chi2(n);
                                   n
(%o2)                   mean_gamma(-, 2)
                                   2
(%i3) assume(n>0)$ mean_chi2(n);
(%o4)                           n
```

<!-- category: Statistics -->
<!-- keywords: mean_continuous_uniform -->
<!-- signatures: mean_continuous_uniform(a, b) -->
### Function: mean_continuous_uniform (a, b)

Returns the mean of a $Continuous Uniform(a,b)$ random variable, with
$a<b$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_discrete_uniform -->
<!-- signatures: mean_discrete_uniform(n) -->
### Function: mean_discrete_uniform (n)

Returns the mean of a $Discrete Uniform(n)$ random variable, with $n$
a strictly positive integer.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_exp -->
<!-- signatures: mean_exp(m) -->
### Function: mean_exp (m)

Returns the mean of an $Exponential(m)$ random variable, with $m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull mean is returned.



```maxima
(%i1) load ("distrib")$
(%i2) mean_exp(m);
                                       1
(%o2)                  mean_weibull(1, -)
                                       m
(%i3) assume(m>0)$  mean_exp(m);
                                1
(%o4)                           -
                                m
```

<!-- category: Statistics -->
<!-- keywords: mean_f -->
<!-- signatures: mean_f(m, n) -->
### Function: mean_f (m, n)

Returns the mean of a F random variable $F(m,n)$, with $m>0, n>2$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_gamma -->
<!-- signatures: mean_gamma(a, b) -->
### Function: mean_gamma (a, b)

Returns the mean of a $Gamma(a,b)$ random variable, with $a,b>0$.  To
make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_general_finite_discrete -->
<!-- signatures: mean_general_finite_discrete(v) -->
### Function: mean_general_finite_discrete (v)

Returns the mean of a general finite discrete random variable, with vector
probabilities $v$.


See `pdf_general_finite_discrete` for more details.

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: mean_geometric -->
<!-- signatures: mean_geometric(p) -->
### Function: mean_geometric (p)

Returns the mean of a $Geometric(p)$ random variable, with $0<p<1$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_gumbel -->
<!-- signatures: mean_gumbel(a, b) -->
### Function: mean_gumbel (a, b)

Returns the mean of a $Gumbel(a,b)$ random variable, with $b>0$.



```maxima
(%i1) load ("distrib")$
(%i2) assume(b>0)$  mean_gumbel(a,b);
(%o3)                     %gamma b + a
```


where symbol `%gamma` stands for the Euler-Mascheroni constant.
See also `%gamma`.

<!-- category: Statistics -->
<!-- keywords: mean_hypergeometric -->
<!-- signatures: mean_hypergeometric(n1, n2, n) -->
### Function: mean_hypergeometric (n1, n2, n)

Returns the mean of a discrete uniform random variable $Hyp(n1,n2,n)$,
with *n1*, *n2* and *n* non negative integers and $n<=n1+n2$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_laplace -->
<!-- signatures: mean_laplace(a, b) -->
### Function: mean_laplace (a, b)

Returns the mean of a $Laplace(a,b)$ random variable, with $b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_logistic -->
<!-- signatures: mean_logistic(a, b) -->
### Function: mean_logistic (a, b)

Returns the mean of a $Logistic(a,b)$ random variable, with $b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_lognormal -->
<!-- signatures: mean_lognormal(m, s) -->
### Function: mean_lognormal (m, s)

Returns the mean of a $Lognormal(m,s)$ random variable, with $s>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_negative_binomial -->
<!-- signatures: mean_negative_binomial(n, p) -->
### Function: mean_negative_binomial (n, p)

Returns the mean of a $Negative Binomial(n,p)$ random variable, with
$0<p<1$ and $n$ a positive integer.  To make use of this function,
write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_noncentral_chi2 -->
<!-- signatures: mean_noncentral_chi2(n, ncp) -->
### Function: mean_noncentral_chi2 (n, ncp)

Returns the mean of a noncentral Chi-square random variable
$nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality parameter
$ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: mean_noncentral_student_t -->
<!-- signatures: mean_noncentral_student_t(n, ncp) -->
### Function: mean_noncentral_student_t (n, ncp)

Returns the mean of a noncentral Student random variable $nc_t(n,ncp)$, 
with $n>1$ degrees of freedom and noncentrality parameter $ncp$.  To 
make use of this function, write first `load("distrib")`.



```maxima
(%i1) load ("distrib")$
(%i2) (assume(df>1), mean_noncentral_student_t(df,k));
                   df - 1
             gamma(------) sqrt(df) k
                     2
(%o2)        ------------------------
                              df
                sqrt(2) gamma(--)
                              2
```

<!-- category: Statistics -->
<!-- keywords: mean_normal -->
<!-- signatures: mean_normal(m, s) -->
### Function: mean_normal (m, s)

Returns the mean of a $Normal(m,s)$ random variable, with $s>0$, 
namely *m*.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_pareto -->
<!-- signatures: mean_pareto(a, b) -->
### Function: mean_pareto (a, b)

Returns the mean of a $Pareto(a,b)$ random variable, with $a>1,b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_poisson -->
<!-- signatures: mean_poisson(m) -->
### Function: mean_poisson (m)

Returns the mean of a $Poisson(m)$ random variable, with  $m>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_rayleigh -->
<!-- signatures: mean_rayleigh(b) -->
### Function: mean_rayleigh (b)

Returns the mean of a $Rayleigh(b)$ random variable, with $b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull mean is returned.



```maxima
(%i1) load ("distrib")$
(%i2) mean_rayleigh(b);
                                       1
(%o2)                  mean_weibull(2, -)
                                       b
(%i3) assume(b>0)$ mean_rayleigh(b);
                            sqrt(%pi)
(%o4)                       ---------
                               2 b
```

<!-- category: Statistics -->
<!-- keywords: mean_student_t -->
<!-- signatures: mean_student_t(n) -->
### Function: mean_student_t (n)

Returns the mean of a Student random variable $t(n)$, with $n>0$, 
which is always equal to 0.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_weibull -->
<!-- signatures: mean_weibull(a, b) -->
### Function: mean_weibull (a, b)

Returns the mean of a $Weibull(a,b)$ random variable, with $a,b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_bernoulli -->
<!-- signatures: pdf_bernoulli(x, p) -->
### Function: pdf_bernoulli (x, p)

Returns the value at *x* of the probability function of a
$Bernoulli(p)$ random variable, with $0<p<1$.


The $Bernoulli(p)$ random variable is equivalent to the
$Binomial(1,p)$, therefore when Maxima has not enough information to get
the result, a noun form based on the binomial probability function is returned.



```maxima
(%i1) load ("distrib")$
(%i2) pdf_bernoulli(1,p);
(%o2)                 pdf_binomial(1, 1, p)
(%i3) assume(0<p,p<1)$ pdf_bernoulli(1,p);
(%o4)                           p
```

<!-- category: Statistics -->
<!-- keywords: pdf_beta -->
<!-- signatures: pdf_beta(x, a, b) -->
### Function: pdf_beta (x, a, b)

Returns the value at *x* of the density function of a $Beta(a,b)$
random variable, with $a,b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_binomial -->
<!-- signatures: pdf_binomial(x, n, p) -->
### Function: pdf_binomial (x, n, p)

Returns the value at *x* of the probability function of a
$Binomial(n,p)$ random variable, with $0<p<1$ and $n$ a positive
integer.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_cauchy -->
<!-- signatures: pdf_cauchy(x, a, b) -->
### Function: pdf_cauchy (x, a, b)

Returns the value at *x* of the density function of a $Cauchy(a,b)$
random variable, with $b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_chi2 -->
<!-- signatures: pdf_chi2(x, n) -->
### Function: pdf_chi2 (x, n)

Returns the value at *x* of the density function of a Chi-square random 
variable $Chi^2(n)$, with $n>0$.


The $Chi^2(n)$ random variable is equivalent to the $Gamma(n/2,2)$, 
therefore when Maxima has not enough information to get the result, a noun form 
based on the gamma density is returned.



```maxima
(%i1) load ("distrib")$
(%i2) pdf_chi2(x,n);
                                    n
(%o2)                  pdf_gamma(x, -, 2)
                                    2
(%i3) assume(x>0, n>0)$  pdf_chi2(x,n);
                         n/2 - 1   - x/2
                        x        %e
(%o4)                   ----------------
                          n/2       n
                         2    gamma(-)
                                    2
```

<!-- category: Statistics -->
<!-- keywords: pdf_continuous_uniform -->
<!-- signatures: pdf_continuous_uniform(x, a, b) -->
### Function: pdf_continuous_uniform (x, a, b)

Returns the value at *x* of the density function of a
$Continuous Uniform(a,b)$ random variable, with $a<b$.  To make use
of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_discrete_uniform -->
<!-- signatures: pdf_discrete_uniform(x, n) -->
### Function: pdf_discrete_uniform (x, n)

Returns the value at *x* of the probability function of a
$Discrete Uniform(n)$ random variable, with $n$ a strictly positive
integer.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_exp -->
<!-- signatures: pdf_exp(x, m) -->
### Function: pdf_exp (x, m)

Returns the value at *x* of the density function of an $Exponential(m)$
random variable, with $m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull density is returned.



```maxima
(%i1) load ("distrib")$
(%i2) pdf_exp(x,m);
                                        1
(%o2)                 pdf_weibull(x, 1, -)
                                        m
(%i3) assume(x>0,m>0)$  pdf_exp(x,m);
                                - m x
(%o4)                       m %e
```

<!-- category: Statistics -->
<!-- keywords: pdf_f -->
<!-- signatures: pdf_f(x, m, n) -->
### Function: pdf_f (x, m, n)

Returns the value at *x* of the density function of a F random variable
$F(m,n)$, with $m,n>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_gamma -->
<!-- signatures: pdf_gamma(x, a, b) -->
### Function: pdf_gamma (x, a, b)

Returns the value at *x* of the density function of a $Gamma(a,b)$
random variable, with $a,b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_general_finite_discrete -->
<!-- signatures: pdf_general_finite_discrete(x, v) -->
### Function: pdf_general_finite_discrete (x, v)

Returns the value at *x* of the probability function of a general finite
discrete random variable, with vector probabilities $v$, such that
`Pr(X=i) = v_i`.  Vector $v$ can be a list of nonnegative expressions,
whose components will be normalized to get a vector of probabilities.  To make
use of this function, write first `load("distrib")`.


Examples:



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

<!-- category: Statistics -->
<!-- keywords: pdf_geometric -->
<!-- signatures: pdf_geometric(x, p) -->
### Function: pdf_geometric (x, p)

Returns the value at *x* of the probability function of a
$Geometric(p)$ random variable, with $0<p<1$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_gumbel -->
<!-- signatures: pdf_gumbel(x, a, b) -->
### Function: pdf_gumbel (x, a, b)

Returns the value at *x* of the density function of a $Gumbel(a,b)$
random variable, with $b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_hypergeometric -->
<!-- signatures: pdf_hypergeometric(x, n1, n2, n) -->
### Function: pdf_hypergeometric (x, n1, n2, n)

Returns the value at *x* of the probability function of a
$Hypergeometric(n1,n2,n)$ random variable, with *n1*, *n2* and
*n* non negative integers and $n<=n1+n2$.  Being *n1* the number
of objects of class A, *n2* the number of objects of class B, and *n*
the size of the sample without replacement, this function returns the
probability of event "exactly *x* objects are of class A".


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_laplace -->
<!-- signatures: pdf_laplace(x, a, b) -->
### Function: pdf_laplace (x, a, b)

Returns the value at *x* of the density function of a $Laplace(a,b)$
random variable, with $b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_logistic -->
<!-- signatures: pdf_logistic(x, a, b) -->
### Function: pdf_logistic (x, a, b)

Returns the value at *x* of the density function of a $Logistic(a,b)$
random variable, with $b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_lognormal -->
<!-- signatures: pdf_lognormal(x, m, s) -->
### Function: pdf_lognormal (x, m, s)

Returns the value at *x* of the density function of a $Lognormal(m,s)$
random variable, with $s>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_negative_binomial -->
<!-- signatures: pdf_negative_binomial(x, n, p) -->
### Function: pdf_negative_binomial (x, n, p)

Returns the value at *x* of the probability function of a
$Negative Binomial(n,p)$ random variable, with $0<p<1$ and $n$
a positive integer.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_noncentral_chi2 -->
<!-- signatures: pdf_noncentral_chi2(x, n, ncp) -->
### Function: pdf_noncentral_chi2 (x, n, ncp)

Returns the value at *x* of the density function of a noncentral Chi-square 
random variable $nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality 
parameter $ncp>=0$.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_noncentral_student_t -->
<!-- signatures: pdf_noncentral_student_t(x, n, ncp) -->
### Function: pdf_noncentral_student_t (x, n, ncp)

Returns the value at *x* of the density function of a noncentral Student 
random variable $nc_t(n,ncp)$, with $n>0$ degrees of freedom and 
noncentrality parameter $ncp$.  To make use of this function, write first 
`load("distrib")`.


Sometimes an extra work is necessary to get the final result.



```maxima
(%i1) load ("distrib")$
(%i2) expand(pdf_noncentral_student_t(3,5,0.1));

       .01370030107589574 sqrt(5)
(%o2)  --------------------------
       sqrt(2) sqrt(14) sqrt(%pi)
   1.654562884111515E-4 sqrt(5)
 + ----------------------------
            sqrt(%pi)
   .02434921505438663 sqrt(5)
 + --------------------------
              %pi

(%i3) float(%);
(%o3)          .02080593159405669
```

<!-- category: Statistics -->
<!-- keywords: pdf_normal -->
<!-- signatures: pdf_normal(x, m, s) -->
### Function: pdf_normal (x, m, s)

Returns the value at *x* of the density function of a $Normal(m,s)$ 
random variable, with $s>0$.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_pareto -->
<!-- signatures: pdf_pareto(x, a, b) -->
### Function: pdf_pareto (x, a, b)

Returns the value at *x* of the density function of a $Pareto(a,b)$
random variable, with $a,b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_poisson -->
<!-- signatures: pdf_poisson(x, m) -->
### Function: pdf_poisson (x, m)

Returns the value at *x* of the probability function of a $Poisson(m)$
random variable, with $m>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_rayleigh -->
<!-- signatures: pdf_rayleigh(x, b) -->
### Function: pdf_rayleigh (x, b)

Returns the value at *x* of the density function of a $Rayleigh(b)$
random variable, with $b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull density is returned.



```maxima
(%i1) load ("distrib")$
(%i2) pdf_rayleigh(x,b);
                                        1
(%o2)                 pdf_weibull(x, 2, -)
                                        b
(%i3) assume(x>0,b>0)$ pdf_rayleigh(x,b);
                                    2  2
                           2     - b  x
(%o4)                   2 b  x %e
```

<!-- category: Statistics -->
<!-- keywords: pdf_student_t -->
<!-- signatures: pdf_student_t(x, n) -->
### Function: pdf_student_t (x, n)

Returns the value at *x* of the density function of a Student random 
variable $t(n)$, with $n>0$ degrees of freedom.  To make use of this 
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_weibull -->
<!-- signatures: pdf_weibull(x, a, b) -->
### Function: pdf_weibull (x, a, b)

Returns the value at *x* of the density function of a $Weibull(a,b)$
random variable, with $a,b>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_bernoulli -->
<!-- signatures: quantile_bernoulli(q, p) -->
### Function: quantile_bernoulli (q, p)

Returns the *q*-quantile of a $Bernoulli(p)$ random variable, with
$0<p<1$; in other words, this is the inverse of `cdf_bernoulli`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_beta -->
<!-- signatures: quantile_beta(q, a, b) -->
### Function: quantile_beta (q, a, b)

Returns the *q*-quantile of a $Beta(a,b)$ random variable, with
$a,b>0$; in other words, this is the inverse of `cdf_beta`.  Argument
*q* must be an element of $[0,1]$.  To make use of this function, write
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_binomial -->
<!-- signatures: quantile_binomial(q, n, p) -->
### Function: quantile_binomial (q, n, p)

Returns the *q*-quantile of a $Binomial(n,p)$ random variable, with
$0<p<1$ and $n$ a positive integer; in other words, this is the
inverse of `cdf_binomial`.  Argument *q* must be an element of
$[0,1]$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_cauchy -->
<!-- signatures: quantile_cauchy(q, a, b) -->
### Function: quantile_cauchy (q, a, b)

Returns the *q*-quantile of a $Cauchy(a,b)$ random variable, with
$b>0$; in other words, this is the inverse of `cdf_cauchy`.  Argument
*q* must be an element of $[0,1]$.  To make use of this function,
write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_chi2 -->
<!-- signatures: quantile_chi2(q, n) -->
### Function: quantile_chi2 (q, n)

Returns the *q*-quantile of a Chi-square random variable $Chi^2(n)$, 
with $n>0$; in other words, this is the inverse of `cdf_chi2`.
Argument *q* must be an element of $[0,1]$.


This function has no closed form and it is numerically computed if the global 
variable `numer` equals `true`,  otherwise it returns a nominal 
expression based on the gamma quantile function, since the $Chi^2(n)$ 
random variable is equivalent to the $Gamma(n/2,2)$.



```maxima
(%i1) load ("distrib")$
(%i2) quantile_chi2(0.99,9);
(%o2)                   21.66599433346194
(%i3) quantile_chi2(0.99,n);
                                        n
(%o3)              quantile_gamma(0.99, -, 2)
                                        2
```

<!-- category: Statistics -->
<!-- keywords: quantile_continuous_uniform -->
<!-- signatures: quantile_continuous_uniform(q, a, b) -->
### Function: quantile_continuous_uniform (q, a, b)

Returns the *q*-quantile of a $Continuous Uniform(a,b)$ random
variable, with $a<b$; in other words, this is the inverse of
`cdf_continuous_uniform`.  Argument *q* must be an element of
$[0,1]$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_discrete_uniform -->
<!-- signatures: quantile_discrete_uniform(q, n) -->
### Function: quantile_discrete_uniform (q, n)

Returns the *q*-quantile of a $Discrete Uniform(n)$ random variable,
with $n$ a strictly positive integer; in other words, this is the inverse
of `cdf_discrete_uniform`.  Argument *q* must be an element of
$[0,1]$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_exp -->
<!-- signatures: quantile_exp(q, m) -->
### Function: quantile_exp (q, m)

Returns the *q*-quantile of an $Exponential(m)$ random variable, with
$m>0$; in other words, this is the inverse of `cdf_exp`.  Argument
*q* must be an element of $[0,1]$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull quantile is returned.



```maxima
(%i1) load ("distrib")$
(%i2) quantile_exp(0.56,5);
(%o2)                   .1641961104139661
(%i3) quantile_exp(0.56,m);
                                            1
(%o3)             quantile_weibull(0.56, 1, -)
                                            m
```

<!-- category: Statistics -->
<!-- keywords: quantile_f -->
<!-- signatures: quantile_f(q, m, n) -->
### Function: quantile_f (q, m, n)

Returns the *q*-quantile of a F random variable $F(m,n)$, with
$m,n>0$; in other words, this is the inverse of `cdf_f`.  Argument
*q* must be an element of $[0,1]$.


This function has no closed form and it is numerically computed if the global
variable `numer` equals `true`,  otherwise it returns a nominal
expression.



```maxima
(%i1) load ("distrib")$
(%i2) quantile_f(2/5,sqrt(3),5);
                               2
(%o2)               quantile_f(-, sqrt(3), 5)
                               5
(%i3) %,numer;
(%o3)                   0.518947838573693
```

<!-- category: Statistics -->
<!-- keywords: quantile_gamma -->
<!-- signatures: quantile_gamma(q, a, b) -->
### Function: quantile_gamma (q, a, b)

Returns the *q*-quantile of a $Gamma(a,b)$ random variable, with
$a,b>0$; in other words, this is the inverse of `cdf_gamma`.  Argument
*q* must be an element of $[0,1]$.  To make use of this function, write
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_general_finite_discrete -->
<!-- signatures: quantile_general_finite_discrete(q, v) -->
### Function: quantile_general_finite_discrete (q, v)

Returns the *q*-quantile of a general finite discrete random variable, with
vector probabilities $v$.


See `pdf_general_finite_discrete` for more details.

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: quantile_geometric -->
<!-- signatures: quantile_geometric(q, p) -->
### Function: quantile_geometric (q, p)

Returns the *q*-quantile of a $Geometric(p)$ random variable, with
$0<p<1$; in other words, this is the inverse of `cdf_geometric`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_gumbel -->
<!-- signatures: quantile_gumbel(q, a, b) -->
### Function: quantile_gumbel (q, a, b)

Returns the *q*-quantile of a $Gumbel(a,b)$ random variable, with
$b>0$; in other words, this is the inverse of `cdf_gumbel`.  Argument
*q* must be an element of $[0,1]$.  To make use of this function,
write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_hypergeometric -->
<!-- signatures: quantile_hypergeometric(q, n1, n2, n) -->
### Function: quantile_hypergeometric (q, n1, n2, n)

Returns the *q*-quantile of a $Hypergeometric(n1,n2,n)$ random
variable, with *n1*, *n2* and *n* non negative integers and
$n<=n1+n2$; in other words, this is the inverse of
`cdf_hypergeometric`.  Argument *q* must be an element of
$[0,1]$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_laplace -->
<!-- signatures: quantile_laplace(q, a, b) -->
### Function: quantile_laplace (q, a, b)

Returns the *q*-quantile of a $Laplace(a,b)$ random variable, with
$b>0$; in other words, this is the inverse of `cdf_laplace`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_logistic -->
<!-- signatures: quantile_logistic(q, a, b) -->
### Function: quantile_logistic (q, a, b)

Returns the *q*-quantile of a $Logistic(a,b)$ random variable , with
$b>0$; in other words, this is the inverse of `cdf_logistic`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_lognormal -->
<!-- signatures: quantile_lognormal(q, m, s) -->
### Function: quantile_lognormal (q, m, s)

Returns the *q*-quantile of a $Lognormal(m,s)$ random variable, with
$s>0$; in other words, this is the inverse of `cdf_lognormal`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.



```maxima
(%i1) load ("distrib")$
(%i2) quantile_lognormal(95/100,0,1);
                  sqrt(2) inverse_erf(9/10)
(%o2)           %e
(%i3) float(%);
(%o3)               5.180251602233015
```

<!-- category: Statistics -->
<!-- keywords: quantile_negative_binomial -->
<!-- signatures: quantile_negative_binomial(q, n, p) -->
### Function: quantile_negative_binomial (q, n, p)

Returns the *q*-quantile of a $Negative Binomial(n,p)$ random variable,
with $0<p<1$ and $n$ a positive integer; in other words, this is the
inverse of `cdf_negative_binomial`.  Argument *q* must be an element of
$[0,1]$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_noncentral_chi2 -->
<!-- signatures: quantile_noncentral_chi2(q, n, ncp) -->
### Function: quantile_noncentral_chi2 (q, n, ncp)

Returns the *q*-quantile of a noncentral Chi-square random variable
$nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality parameter
$ncp>=0$; in other words, this is the inverse of
`cdf_noncentral_chi2`.  Argument *q* must be an element of
$[0,1]$.


This function has no closed form and it is numerically computed if the global
variable `numer` equals `true`,  otherwise it returns a nominal
expression.

<!-- category: Statistics -->
<!-- keywords: quantile_noncentral_student_t -->
<!-- signatures: quantile_noncentral_student_t(q, n, ncp) -->
### Function: quantile_noncentral_student_t (q, n, ncp)

Returns the *q*-quantile of a noncentral Student random variable 
$nc_t(n,ncp)$, with $n>0$ degrees of freedom and noncentrality 
parameter $ncp$; in other words, this is the inverse of 
`cdf_noncentral_student_t`.  Argument *q* must be an element of 
$[0,1]$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_normal -->
<!-- signatures: quantile_normal(q, m, s) -->
### Function: quantile_normal (q, m, s)

Returns the *q*-quantile of a $Normal(m,s)$ random variable, with 
$s>0$; in other words, this is the inverse of `cdf_normal`.  Argument 
*q* must be an element of $[0,1]$.  To make use of this function, write 
first `load("distrib")`.



```maxima
(%i1) load ("distrib")$
(%i2) quantile_normal(95/100,0,1);
                                      9
(%o2)             sqrt(2) inverse_erf(--)
                                      10
(%i3) float(%);
(%o3)               1.644853626951472
```

<!-- category: Statistics -->
<!-- keywords: quantile_pareto -->
<!-- signatures: quantile_pareto(q, a, b) -->
### Function: quantile_pareto (q, a, b)

Returns the *q*-quantile of a $Pareto(a,b)$ random variable, with
$a,b>0$; in other words, this is the inverse of `cdf_pareto`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_poisson -->
<!-- signatures: quantile_poisson(q, m) -->
### Function: quantile_poisson (q, m)

Returns the *q*-quantile of a $Poisson(m)$ random variable, with
$m>0$; in other words, this is the inverse of `cdf_poisson`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_rayleigh -->
<!-- signatures: quantile_rayleigh(q, b) -->
### Function: quantile_rayleigh (q, b)

Returns the *q*-quantile of a $Rayleigh(b)$ random variable, with
$b>0$; in other words, this is the inverse of `cdf_rayleigh`.
Argument *q* must be an element of $[0,1]$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull quantile is returned.



```maxima
(%i1) load ("distrib")$
(%i2) quantile_rayleigh(0.99,b);
                                            1
(%o2)             quantile_weibull(0.99, 2, -)
                                            b
(%i3) assume(x>0,b>0)$ quantile_rayleigh(0.99,b);
                        2.145966026289347
(%o4)                   -----------------
                                b
```

<!-- category: Statistics -->
<!-- keywords: quantile_student_t -->
<!-- signatures: quantile_student_t(q, n) -->
### Function: quantile_student_t (q, n)

Returns the *q*-quantile of a Student random variable $t(n)$, with 
$n>0$; in other words, this is the inverse of `cdf_student_t`.
Argument *q* must be an element of $[0,1]$.  To make use of this 
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_weibull -->
<!-- signatures: quantile_weibull(q, a, b) -->
### Function: quantile_weibull (q, a, b)

Returns the *q*-quantile of a $Weibull(a,b)$ random variable, with
$a,b>0$; in other words, this is the inverse of `cdf_weibull`.
Argument *q* must be an element of $[0,1]$.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_bernoulli -->
<!-- signatures: random_bernoulli(p), random_bernoulli(p, n) -->
### Function: random_bernoulli (p)

Returns a $Bernoulli(p)$ random variate, with $0<p<1$.  Calling
`random_bernoulli` with a second argument *n*, a random sample of size
*n* will be simulated.


This is a direct application of the `random` built-in Maxima function.


See also `random`. To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_beta -->
<!-- signatures: random_beta(a, b), random_beta(a, b, n) -->
### Function: random_beta (a, b)

Returns a $Beta(a,b)$ random variate, with $a,b>0$.  Calling
`random_beta` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is defined in Cheng, R.C.H. (1978). *Generating
Beta Variates with Nonintegral Shape Parameters*.
Communications of the ACM, 21:317-322


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_binomial -->
<!-- signatures: random_binomial(n, p), random_binomial(n, p, m) -->
### Function: random_binomial (n, p)

Returns a $Binomial(n,p)$ random variate, with $0<p<1$ and $n$ a
positive integer.  Calling `random_binomial` with a third argument *m*,
a random sample of size *m* will be simulated.


The implemented algorithm is based on the one described in Kachitvichyanukul,
V. and Schmeiser, B.W. (1988) *Binomial Random Variate Generation*.
Communications of the ACM, 31, Feb., 216.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_cauchy -->
<!-- signatures: random_cauchy(a, b), random_cauchy(a, b, n) -->
### Function: random_cauchy (a, b)

Returns a $Cauchy(a,b)$ random variate, with $b>0$.  Calling
`random_cauchy` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_chi2 -->
<!-- signatures: random_chi2(n), random_chi2(n, m) -->
### Function: random_chi2 (n)

Returns a Chi-square random variate $Chi^2(n)$, with $n>0$.  Calling 
`random_chi2` with a second argument *m*, a random sample of size 
*m* will be simulated.


The simulation is based on the Ahrens-Cheng algorithm.  See `random_gamma` 
for details.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_continuous_uniform -->
<!-- signatures: random_continuous_uniform(a, b), random_continuous_uniform(a, b, n) -->
### Function: random_continuous_uniform (a, b)

Returns a $Continuous Uniform(a,b)$ random variate, with $a<b$.
Calling `random_continuous_uniform` with a third argument *n*, a
random sample of size *n* will be simulated.


This is a direct application of the `random` built-in Maxima function.


See also `random`.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_discrete_uniform -->
<!-- signatures: random_discrete_uniform(n), random_discrete_uniform(n, m) -->
### Function: random_discrete_uniform (n)

Returns a $Discrete Uniform(n)$ random variate, with $n$ a strictly
positive integer.  Calling `random_discrete_uniform` with a second
argument *m*, a random sample of size *m* will be simulated.


This is a direct application of the `random` built-in Maxima function.


See also `random`.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_exp -->
<!-- signatures: random_exp(m), random_exp(m, k) -->
### Function: random_exp (m)

Returns an $Exponential(m)$ random variate, with $m>0$.  Calling
`random_exp` with a second argument *k*, a random sample of size
*k* will be simulated.


The simulation algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_f -->
<!-- signatures: random_f(m, n), random_f(m, n, k) -->
### Function: random_f (m, n)

Returns a F random variate $F(m,n)$, with $m,n>0$.  Calling
`random_f` with a third argument *k*, a random sample of size *k*
will be simulated.


The simulation algorithm is based on the fact that if *X* is a
$Chi^2(m)$ random variable and $Y$ is a $Chi^2(n)$ random
variable, then


```maxima
n X
                    F = ---
                        m Y
```


$$
F={{n X}\over{m Y}}
$$

is a F random variable with *m* and *n* degrees of freedom,
$F(m,n)$.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_gamma -->
<!-- signatures: random_gamma(a, b), random_gamma(a, b, n) -->
### Function: random_gamma (a, b)

Returns a $Gamma(a,b)$ random variate, with $a,b>0$.  Calling
`random_gamma` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is a combination of two procedures, depending on the
value of parameter *a*:


For $a>=1$, Cheng, R.C.H. and Feast, G.M. (1979).
*Some simple gamma variate generators*. Appl. Stat., 28, 3, 290-295.


For $0<a<1$, Ahrens, J.H. and Dieter, U. (1974). *Computer methods for
sampling from gamma, beta, poisson and binomial cdf_tributions*.
Computing, 12, 223-246.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_general_finite_discrete -->
<!-- signatures: random_general_finite_discrete(v), random_general_finite_discrete(v, m) -->
### Function: random_general_finite_discrete (v)

Returns a general finite discrete random variate, with vector probabilities
$v$.  Calling `random_general_finite_discrete` with a second argument
*m*, a random sample of size *m* will be simulated.


See `pdf_general_finite_discrete` for more details.


Examples:



```maxima
(%i1) load ("distrib")$
(%i2) random_general_finite_discrete([1,3,1,5]);
(%o2)                          4
(%i3) random_general_finite_discrete([1,3,1,5], 10);
(%o3)           [4, 2, 2, 3, 2, 4, 4, 1, 2, 2]
```

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: random_geometric -->
<!-- signatures: random_geometric(p), random_geometric(p, n) -->
### Function: random_geometric (p)

Returns a $Geometric(p)$ random variate, with $0<p<1$.  Calling
`random_geometric` with a second argument *n*, a random sample of size
*n* will be simulated.


The algorithm is based on simulation of Bernoulli trials.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_gumbel -->
<!-- signatures: random_gumbel(a, b), random_gumbel(a, b, n) -->
### Function: random_gumbel (a, b)

Returns a $Gumbel(a,b)$ random variate, with $b>0$.  Calling
`random_gumbel` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_hypergeometric -->
<!-- signatures: random_hypergeometric(n1, n2, n), random_hypergeometric(n1, n2, n, m) -->
### Function: random_hypergeometric (n1, n2, n)

Returns a $Hypergeometric(n1,n2,n)$ random variate, with *n1*,
*n2* and *n* non negative integers and $n<=n1+n2$.  Calling
`random_hypergeometric` with a fourth argument *m*, a random sample of
size *m* will be simulated.


Algorithm described in Kachitvichyanukul, V., Schmeiser, B.W. (1985)
*Computer generation of hypergeometric random variates.* Journal of
Statistical Computation and Simulation 22, 127-145.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_laplace -->
<!-- signatures: random_laplace(a, b), random_laplace(a, b, n) -->
### Function: random_laplace (a, b)

Returns a $Laplace(a,b)$ random variate, with $b>0$.  Calling
`random_laplace` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_logistic -->
<!-- signatures: random_logistic(a, b), random_logistic(a, b, n) -->
### Function: random_logistic (a, b)

Returns a $Logistic(a,b)$ random variate, with $b>0$.  Calling
`random_logistic` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_lognormal -->
<!-- signatures: random_lognormal(m, s), random_lognormal(m, s, n) -->
### Function: random_lognormal (m, s)

Returns a $Lognormal(m,s)$ random variate, with $s>0$.  Calling
`random_lognormal` with a third argument *n*, a random sample of size
*n* will be simulated.


Log-normal variates are simulated by means of random normal variates.
See `random_normal` for details.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_negative_binomial -->
<!-- signatures: random_negative_binomial(n, p), random_negative_binomial(n, p, m) -->
### Function: random_negative_binomial (n, p)

Returns a $Negative Binomial(n,p)$ random variate, with $0<p<1$ and
$n$ a positive integer.  Calling `random_negative_binomial` with a
third argument *m*, a random sample of size *m* will be simulated.


Algorithm described in Devroye, L. (1986) *Non-Uniform Random Variate
Generation*. Springer Verlag, p. 480.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_noncentral_chi2 -->
<!-- signatures: random_noncentral_chi2(n, ncp), random_noncentral_chi2(n, ncp, m) -->
### Function: random_noncentral_chi2 (n, ncp)

Returns a noncentral Chi-square random variate $nc_Chi^2(n,ncp)$, with
$n>0$ and noncentrality parameter $ncp>=0$.  Calling
`random_noncentral_chi2` with a third argument *m*, a random sample of
size *m* will be simulated.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_noncentral_student_t -->
<!-- signatures: random_noncentral_student_t(n, ncp), random_noncentral_student_t(n, ncp, m) -->
### Function: random_noncentral_student_t (n, ncp)

Returns a noncentral Student random variate $nc_t(n,ncp)$, with $n>0$.
Calling `random_noncentral_student_t` with a third argument *m*, a 
random sample of size *m* will be simulated.


The implemented algorithm is based on the fact that if *X* is a normal 
random variable $N(ncp,1)$ and $S^2$ is a chi square random variable 
with *n* degrees of freedom, $Chi^2(n)$, then


```maxima
X
                 U = -------------
                     /   2  \ 1/2
                     |  S   |
                     | ---  |
                     \  n   /
```


$$
U={{X}\over{\sqrt{{S^2}\over{n}}}}
$$

is a noncentral Student random variable with *n* degrees of freedom and 
noncentrality parameter $ncp$, $nc_t(n,ncp)$.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_normal -->
<!-- signatures: random_normal(m, s), random_normal(m, s, n) -->
### Function: random_normal (m, s)

Returns a $Normal(m,s)$ random variate, with $s>0$.  Calling 
`random_normal` with a third argument *n*, a random sample of size 
*n* will be simulated.


This is an implementation of the Box-Mueller algorithm, as described in Knuth, 
D.E. (1981) *Seminumerical Algorithms.  The Art of Computer Programming.* 
Addison-Wesley.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_pareto -->
<!-- signatures: random_pareto(a, b), random_pareto(a, b, n) -->
### Function: random_pareto (a, b)

Returns a $Pareto(a,b)$ random variate, with $a>0,b>0$.  Calling
`random_pareto` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_poisson -->
<!-- signatures: random_poisson(m), random_poisson(m, n) -->
### Function: random_poisson (m)

Returns a $Poisson(m)$ random variate, with $m>0$.  Calling
`random_poisson` with a second argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is the one described in Ahrens, J.H. and Dieter,
U. (1982) *Computer Generation of Poisson Deviates From Modified Normal
Distributions*. ACM Trans. Math. Software, 8, 2, June,163-179.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_rayleigh -->
<!-- signatures: random_rayleigh(b), random_rayleigh(b, n) -->
### Function: random_rayleigh (b)

Returns a $Rayleigh(b)$ random variate, with $b>0$.  Calling
`random_rayleigh` with a second argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_student_t -->
<!-- signatures: random_student_t(n), random_student_t(n, m) -->
### Function: random_student_t (n)

Returns a Student random variate $t(n)$, with $n>0$.  Calling 
`random_student_t` with a second argument *m*, a random sample of size 
*m* will be simulated.


The implemented algorithm is based on the fact that if *Z* is a normal 
random variable $N(0,1)$ and $S^2$ is a chi square random variable 
with *n* degrees of freedom, $Chi^2(n)$, then


```maxima
Z
                 X = -------------
                     /   2  \ 1/2
                     |  S   |
                     | ---  |
                     \  n   /
```


$$
X={{Z}\over{\sqrt{{S^2}\over{n}}}}
$$

is a Student random variable with *n* degrees of freedom, $t(n)$.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_weibull -->
<!-- signatures: random_weibull(a, b), random_weibull(a, b, n) -->
### Function: random_weibull (a, b)

Returns a $Weibull(a,b)$ random variate, with $a,b>0$.  Calling
`random_weibull` with a third argument *n*, a random sample of size
*n* will be simulated.


The implemented algorithm is based on the general inverse method.


To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_bernoulli -->
<!-- signatures: skewness_bernoulli(p) -->
### Function: skewness_bernoulli (p)

Returns the skewness coefficient of a $Bernoulli(p)$ random variable,
with $0<p<1$.


The $Bernoulli(p)$ random variable is equivalent to the
$Binomial(1,p)$, therefore when Maxima has not enough information to get
the result, a noun form based on the binomial skewness coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) skewness_bernoulli(p);
(%o2)                skewness_binomial(1, p)
(%i3) assume(0<p,p<1)$ skewness_bernoulli(p);
                             1 - 2 p
(%o4)                  -------------------
                       sqrt(1 - p) sqrt(p)
```

<!-- category: Statistics -->
<!-- keywords: skewness_beta -->
<!-- signatures: skewness_beta(a, b) -->
### Function: skewness_beta (a, b)

Returns the skewness coefficient of a $Beta(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_binomial -->
<!-- signatures: skewness_binomial(n, p) -->
### Function: skewness_binomial (n, p)

Returns the skewness coefficient of a $Binomial(n,p)$ random variable,
with $0<p<1$ and $n$ a positive integer.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_chi2 -->
<!-- signatures: skewness_chi2(n) -->
### Function: skewness_chi2 (n)

Returns the skewness coefficient of a Chi-square random variable 
$Chi^2(n)$, with $n>0$.


The $Chi^2(n)$ random variable is equivalent to the $Gamma(n/2,2)$, 
therefore when Maxima has not enough information to get the result, a noun 
form based on the gamma skewness coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) skewness_chi2(n);
                                     n
(%o2)                 skewness_gamma(-, 2)
                                     2
(%i3) assume(n>0)$ skewness_chi2(n);
                            2 sqrt(2)
(%o4)                       ---------
                             sqrt(n)
```

<!-- category: Statistics -->
<!-- keywords: skewness_continuous_uniform -->
<!-- signatures: skewness_continuous_uniform(a, b) -->
### Function: skewness_continuous_uniform (a, b)

Returns the skewness coefficient of a $Continuous Uniform(a,b)$ random
variable, with $a<b$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_discrete_uniform -->
<!-- signatures: skewness_discrete_uniform(n) -->
### Function: skewness_discrete_uniform (n)

Returns the skewness coefficient of a $Discrete Uniform(n)$ random
variable, with $n$ a strictly positive integer.  To make use of this
function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_exp -->
<!-- signatures: skewness_exp(m) -->
### Function: skewness_exp (m)

Returns the skewness coefficient of an $Exponential(m)$ random variable,
with $m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull skewness coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) skewness_exp(m);
                                         1
(%o2)                skewness_weibull(1, -)
                                         m
(%i3) assume(m>0)$  skewness_exp(m);
(%o4)                           2
```

<!-- category: Statistics -->
<!-- keywords: skewness_f -->
<!-- signatures: skewness_f(m, n) -->
### Function: skewness_f (m, n)

Returns the skewness coefficient of a F random variable $F(m,n)$, with
$m>0, n>6$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_gamma -->
<!-- signatures: skewness_gamma(a, b) -->
### Function: skewness_gamma (a, b)

Returns the skewness coefficient of a $Gamma(a,b)$ random variable, with
$a,b>0$. To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_general_finite_discrete -->
<!-- signatures: skewness_general_finite_discrete(v) -->
### Function: skewness_general_finite_discrete (v)

Returns the skewness coefficient of a general finite discrete random variable,
with vector probabilities $v$.


See `pdf_general_finite_discrete` for more details.

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: skewness_geometric -->
<!-- signatures: skewness_geometric(p) -->
### Function: skewness_geometric (p)

Returns the skewness coefficient of a $Geometric(p)$ random variable, with
$0<p<1$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_gumbel -->
<!-- signatures: skewness_gumbel(a, b) -->
### Function: skewness_gumbel (a, b)

Returns the skewness coefficient of a $Gumbel(a,b)$ random variable, with
$b>0$.



```maxima
(%i1) load ("distrib")$
(%i2) assume(b>0)$ skewness_gumbel(a,b);
                       12 sqrt(6) zeta(3)
(%o3)                  ------------------
                                 3
                              %pi
(%i4) numer:true$ skewness_gumbel(a,b);
(%o5)                   1.139547099404649
```

where `zeta` stands for the Riemann’s zeta function.

<!-- category: Statistics -->
<!-- keywords: skewness_hypergeometric -->
<!-- signatures: skewness_hypergeometric(n1, n2, n) -->
### Function: skewness_hypergeometric (n1, n2, n)

Returns the skewness coefficient of a $Hypergeometric(n1,n2,n)$ random
variable, with *n1*, *n2* and *n* non negative integers and
$n<=n1+n2$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_laplace -->
<!-- signatures: skewness_laplace(a, b) -->
### Function: skewness_laplace (a, b)

Returns the skewness coefficient of a $Laplace(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_logistic -->
<!-- signatures: skewness_logistic(a, b) -->
### Function: skewness_logistic (a, b)

Returns the skewness coefficient of a $Logistic(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_lognormal -->
<!-- signatures: skewness_lognormal(m, s) -->
### Function: skewness_lognormal (m, s)

Returns the skewness coefficient of a $Lognormal(m,s)$ random variable,
with $s>0$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_negative_binomial -->
<!-- signatures: skewness_negative_binomial(n, p) -->
### Function: skewness_negative_binomial (n, p)

Returns the skewness coefficient of a $Negative Binomial(n,p)$ random
variable, with $0<p<1$ and $n$ a positive integer.  To make use of
this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_noncentral_chi2 -->
<!-- signatures: skewness_noncentral_chi2(n, ncp) -->
### Function: skewness_noncentral_chi2 (n, ncp)

Returns the skewness coefficient of a noncentral Chi-square random variable
$nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality parameter
$ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: skewness_noncentral_student_t -->
<!-- signatures: skewness_noncentral_student_t(n, ncp) -->
### Function: skewness_noncentral_student_t (n, ncp)

Returns the skewness coefficient of a noncentral Student random variable 
$nc_t(n,ncp)$, with $n>3$ degrees of freedom and noncentrality 
parameter $ncp$.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_normal -->
<!-- signatures: skewness_normal(m, s) -->
### Function: skewness_normal (m, s)

Returns the skewness coefficient of a $Normal(m,s)$ random variable, with 
$s>0$, which is always equal to 0.  To make use of this function, write 
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_pareto -->
<!-- signatures: skewness_pareto(a, b) -->
### Function: skewness_pareto (a, b)

Returns the skewness coefficient of a $Pareto(a,b)$ random variable, with
$a>3,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_poisson -->
<!-- signatures: skewness_poisson(m) -->
### Function: skewness_poisson (m)

Returns the skewness coefficient of a $Poisson(m)$ random variable, with
$m>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_rayleigh -->
<!-- signatures: skewness_rayleigh(b) -->
### Function: skewness_rayleigh (b)

Returns the skewness coefficient of a $Rayleigh(b)$ random variable, with
$b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull skewness coefficient is returned.



```maxima
(%i1) load ("distrib")$
(%i2) skewness_rayleigh(b);
                                         1
(%o2)                skewness_weibull(2, -)
                                         b
(%i3) assume(b>0)$ skewness_rayleigh(b);
                         3/2
                      %pi      3 sqrt(%pi)
                      ------ - -----------
                        4           4
(%o4)                 --------------------
                               %pi 3/2
                          (1 - ---)
                                4
```

<!-- category: Statistics -->
<!-- keywords: skewness_student_t -->
<!-- signatures: skewness_student_t(n) -->
### Function: skewness_student_t (n)

Returns the skewness coefficient of a Student random variable $t(n)$, with 
$n>3$, which is always equal to 0.  To make use of this function, write 
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_weibull -->
<!-- signatures: skewness_weibull(a, b) -->
### Function: skewness_weibull (a, b)

Returns the skewness coefficient of a $Weibull(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_bernoulli -->
<!-- signatures: std_bernoulli(p) -->
### Function: std_bernoulli (p)

Returns the standard deviation of a $Bernoulli(p)$ random variable, with
$0<p<1$.


The $Bernoulli(p)$ random variable is equivalent to the
$Binomial(1,p)$, therefore when Maxima has not enough information to get
the result, a noun form based on the binomial standard deviation is returned.



```maxima
(%i1) load ("distrib")$
(%i2) std_bernoulli(p);
(%o2)                  std_binomial(1, p)
(%i3) assume(0<p,p<1)$ std_bernoulli(p);
(%o4)                  sqrt(1 - p) sqrt(p)
```

<!-- category: Statistics -->
<!-- keywords: std_beta -->
<!-- signatures: std_beta(a, b) -->
### Function: std_beta (a, b)

Returns the standard deviation of a $Beta(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_binomial -->
<!-- signatures: std_binomial(n, p) -->
### Function: std_binomial (n, p)

Returns the standard deviation of a $Binomial(n,p)$ random variable, with
$0<p<1$ and $n$ a positive integer.  To make use of this function,
write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_chi2 -->
<!-- signatures: std_chi2(n) -->
### Function: std_chi2 (n)

Returns the standard deviation of a Chi-square random variable $Chi^2(n)$, 
with $n>0$.


The $Chi^2(n)$ random variable is equivalent to the $Gamma(n/2,2)$, 
therefore when Maxima has not enough information to get the result, a noun 
form based on the gamma standard deviation is returned.



```maxima
(%i1) load ("distrib")$
(%i2) std_chi2(n);
                                   n
(%o2)                    std_gamma(-, 2)
                                   2
(%i3) assume(n>0)$ std_chi2(n);
(%o4)                    sqrt(2) sqrt(n)
```

<!-- category: Statistics -->
<!-- keywords: std_continuous_uniform -->
<!-- signatures: std_continuous_uniform(a, b) -->
### Function: std_continuous_uniform (a, b)

Returns the standard deviation of a $Continuous Uniform(a,b)$ random
variable, with $a<b$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_discrete_uniform -->
<!-- signatures: std_discrete_uniform(n) -->
### Function: std_discrete_uniform (n)

Returns the standard deviation of a $Discrete Uniform(n)$ random variable,
with $n$ a strictly positive integer.  To make use of this function, write
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_exp -->
<!-- signatures: std_exp(m) -->
### Function: std_exp (m)

Returns the standard deviation of an $Exponential(m)$ random variable, with
$m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull standard deviation is returned.



```maxima
(%i1) load ("distrib")$
(%i2) std_exp(m);
                                       1
(%o2)                   std_weibull(1, -)
                                       m
(%i3) assume(m>0)$  std_exp(m);
                                1
(%o4)                           -
                                m
```

<!-- category: Statistics -->
<!-- keywords: std_f -->
<!-- signatures: std_f(m, n) -->
### Function: std_f (m, n)

Returns the standard deviation of a F random variable $F(m,n)$, with
$m>0, n>4$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_gamma -->
<!-- signatures: std_gamma(a, b) -->
### Function: std_gamma (a, b)

Returns the standard deviation of a $Gamma(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_general_finite_discrete -->
<!-- signatures: std_general_finite_discrete(v) -->
### Function: std_general_finite_discrete (v)

Returns the standard deviation of a general finite discrete random variable,
with vector probabilities $v$.


See `pdf_general_finite_discrete` for more details.

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: std_geometric -->
<!-- signatures: std_geometric(p) -->
### Function: std_geometric (p)

Returns the standard deviation of a $Geometric(p)$ random variable, with
$0<p<1$. To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_gumbel -->
<!-- signatures: std_gumbel(a, b) -->
### Function: std_gumbel (a, b)

Returns the standard deviation of a $Gumbel(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_hypergeometric -->
<!-- signatures: std_hypergeometric(n1, n2, n) -->
### Function: std_hypergeometric (n1, n2, n)

Returns the standard deviation of a $Hypergeometric(n1,n2,n)$ random
variable, with *n1*, *n2* and *n* non negative integers and
$n<=n1+n2$.  To make use of this function, write first
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_laplace -->
<!-- signatures: std_laplace(a, b) -->
### Function: std_laplace (a, b)

Returns the standard deviation of a $Laplace(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_logistic -->
<!-- signatures: std_logistic(a, b) -->
### Function: std_logistic (a, b)

Returns the standard deviation of a $Logistic(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_lognormal -->
<!-- signatures: std_lognormal(m, s) -->
### Function: std_lognormal (m, s)

Returns the standard deviation of a $Lognormal(m,s)$ random variable, with
$s>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_negative_binomial -->
<!-- signatures: std_negative_binomial(n, p) -->
### Function: std_negative_binomial (n, p)

Returns the standard deviation of a $Negative Binomial(n,p)$ random
variable, with $0<p<1$ and $n$ a positive integer.  To make use of
this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_noncentral_chi2 -->
<!-- signatures: std_noncentral_chi2(n, ncp) -->
### Function: std_noncentral_chi2 (n, ncp)

Returns the standard deviation of a noncentral Chi-square random variable
$nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality parameter
$ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: std_noncentral_student_t -->
<!-- signatures: std_noncentral_student_t(n, ncp) -->
### Function: std_noncentral_student_t (n, ncp)

Returns the standard deviation of a noncentral Student random variable 
$nc_t(n,ncp)$, with $n>2$ degrees of freedom and noncentrality 
parameter $ncp$.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_normal -->
<!-- signatures: std_normal(m, s) -->
### Function: std_normal (m, s)

Returns the standard deviation of a $Normal(m,s)$ random variable, with 
$s>0$, namely *s*.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_pareto -->
<!-- signatures: std_pareto(a, b) -->
### Function: std_pareto (a, b)

Returns the standard deviation of a $Pareto(a,b)$ random variable, with
$a>2,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_poisson -->
<!-- signatures: std_poisson(m) -->
### Function: std_poisson (m)

Returns the standard deviation of a $Poisson(m)$ random variable, with
$m>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_rayleigh -->
<!-- signatures: std_rayleigh(b) -->
### Function: std_rayleigh (b)

Returns the standard deviation of a $Rayleigh(b)$ random variable, with
$b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull standard deviation is returned.



```maxima
(%i1) load ("distrib")$
(%i2) std_rayleigh(b);
                                       1
(%o2)                   std_weibull(2, -)
                                       b
(%i3) assume(b>0)$ std_rayleigh(b);
                                   %pi
                          sqrt(1 - ---)
                                    4
(%o4)                     -------------
                                b
```

<!-- category: Statistics -->
<!-- keywords: std_student_t -->
<!-- signatures: std_student_t(n) -->
### Function: std_student_t (n)

Returns the standard deviation of a Student random variable $t(n)$, with 
$n>2$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_weibull -->
<!-- signatures: std_weibull(a, b) -->
### Function: std_weibull (a, b)

Returns the standard deviation of a $Weibull(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_bernoulli -->
<!-- signatures: var_bernoulli(p) -->
### Function: var_bernoulli (p)

Returns the variance of a $Bernoulli(p)$ random variable, with
$0<p<1$.


The $Bernoulli(p)$ random variable is equivalent to the
$Binomial(1,p)$, therefore when Maxima has not enough information to get
the result, a noun form based on the binomial variance is returned.



```maxima
(%i1) load ("distrib")$
(%i2) var_bernoulli(p);
(%o2)                  var_binomial(1, p)
(%i3) assume(0<p,p<1)$ var_bernoulli(p);
(%o4)                       (1 - p) p
```

<!-- category: Statistics -->
<!-- keywords: var_beta -->
<!-- signatures: var_beta(a, b) -->
### Function: var_beta (a, b)

Returns the variance of a $Beta(a,b)$ random variable, with $a,b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_binomial -->
<!-- signatures: var_binomial(n, p) -->
### Function: var_binomial (n, p)

Returns the variance of a $Binomial(n,p)$ random variable, with
$0<p<1$ and $n$ a positive integer.  To make use of this function,
write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_chi2 -->
<!-- signatures: var_chi2(n) -->
### Function: var_chi2 (n)

Returns the variance of a Chi-square random variable $Chi^2(n)$, with 
$n>0$.


The $Chi^2(n)$ random variable is equivalent to the $Gamma(n/2,2)$, 
therefore when Maxima has not enough information to get the result, a noun 
form based on the gamma variance is returned.



```maxima
(%i1) load ("distrib")$
(%i2) var_chi2(n);
                                   n
(%o2)                    var_gamma(-, 2)
                                   2
(%i3) assume(n>0)$ var_chi2(n);
(%o4)                          2 n
```

<!-- category: Statistics -->
<!-- keywords: var_continuous_uniform -->
<!-- signatures: var_continuous_uniform(a, b) -->
### Function: var_continuous_uniform (a, b)

Returns the variance of a $Continuous Uniform(a,b)$ random variable, with
$a<b$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_discrete_uniform -->
<!-- signatures: var_discrete_uniform(n) -->
### Function: var_discrete_uniform (n)

Returns the variance of a $Discrete Uniform(n)$ random variable, with
$n$ a strictly positive integer.  To make use of this function, write
first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_exp -->
<!-- signatures: var_exp(m) -->
### Function: var_exp (m)

Returns the variance of an $Exponential(m)$ random variable, with
$m>0$.


The $Exponential(m)$ random variable is equivalent to the
$Weibull(1,1/m)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull variance is returned.



```maxima
(%i1) load ("distrib")$
(%i2) var_exp(m);
                                       1
(%o2)                   var_weibull(1, -)
                                       m
(%i3) assume(m>0)$  var_exp(m);
                               1
(%o4)                          --
                                2
                               m
```

<!-- category: Statistics -->
<!-- keywords: var_f -->
<!-- signatures: var_f(m, n) -->
### Function: var_f (m, n)

Returns the variance of a F random variable $F(m,n)$, with $m>0, n>4$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_gamma -->
<!-- signatures: var_gamma(a, b) -->
### Function: var_gamma (a, b)

Returns the variance of a $Gamma(a,b)$ random variable, with $a,b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_general_finite_discrete -->
<!-- signatures: var_general_finite_discrete(v) -->
### Function: var_general_finite_discrete (v)

Returns the variance of a general finite discrete random variable, with vector
probabilities $v$.


See `pdf_general_finite_discrete` for more details.

See also: `pdf_general_finite_discrete`.

<!-- category: Statistics -->
<!-- keywords: var_geometric -->
<!-- signatures: var_geometric(p) -->
### Function: var_geometric (p)

Returns the variance of a $Geometric(p)$ random variable, with
$0<p<1$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_gumbel -->
<!-- signatures: var_gumbel(a, b) -->
### Function: var_gumbel (a, b)

Returns the variance of a $Gumbel(a,b)$ random variable, with $b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_hypergeometric -->
<!-- signatures: var_hypergeometric(n1, n2, n) -->
### Function: var_hypergeometric (n1, n2, n)

Returns the variance of a hypergeometric  random variable $Hyp(n1,n2,n)$,
with *n1*, *n2* and *n* non negative integers and $n<=n1+n2$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_laplace -->
<!-- signatures: var_laplace(a, b) -->
### Function: var_laplace (a, b)

Returns the variance of a $Laplace(a,b)$ random variable, with $b>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_logistic -->
<!-- signatures: var_logistic(a, b) -->
### Function: var_logistic (a, b)

Returns the variance of a $Logistic(a,b)$ random variable, with
$b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_lognormal -->
<!-- signatures: var_lognormal(m, s) -->
### Function: var_lognormal (m, s)

Returns the variance of a $Lognormal(m,s)$ random variable, with
$s>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_negative_binomial -->
<!-- signatures: var_negative_binomial(n, p) -->
### Function: var_negative_binomial (n, p)

Returns the variance of a $Negative Binomial(n,p)$ random variable, with
$0<p<1$ and $n$ a positive integer.  To make use of this function,
write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_noncentral_chi2 -->
<!-- signatures: var_noncentral_chi2(n, ncp) -->
### Function: var_noncentral_chi2 (n, ncp)

Returns the variance of a noncentral Chi-square random variable 
$nc_Chi^2(n,ncp)$, with $n>0$ and noncentrality parameter
$ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: var_noncentral_student_t -->
<!-- signatures: var_noncentral_student_t(n, ncp) -->
### Function: var_noncentral_student_t (n, ncp)

Returns the variance of a noncentral Student random variable 
$nc_t(n,ncp)$, with $n>2$ degrees of freedom and noncentrality 
parameter $ncp$.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_normal -->
<!-- signatures: var_normal(m, s) -->
### Function: var_normal (m, s)

Returns the variance of a $Normal(m,s)$ random variable, with $s>0$, 
namely *s^2*.  To make use of this function, write first 
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_pareto -->
<!-- signatures: var_pareto(a, b) -->
### Function: var_pareto (a, b)

Returns the variance of a $Pareto(a,b)$ random variable, with
$a>2,b>0$.  To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_poisson -->
<!-- signatures: var_poisson(m) -->
### Function: var_poisson (m)

Returns the variance of a $Poisson(m)$ random variable, with  $m>0$.
To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_rayleigh -->
<!-- signatures: var_rayleigh(b) -->
### Function: var_rayleigh (b)

Returns the variance of a $Rayleigh(b)$ random variable, with $b>0$.


The $Rayleigh(b)$ random variable is equivalent to the
$Weibull(2,1/b)$, therefore when Maxima has not enough information to get
the result, a noun form based on the Weibull variance is returned.



```maxima
(%i1) load ("distrib")$
(%i2) var_rayleigh(b);
                                       1
(%o2)                   var_weibull(2, -)
                                       b
(%i3) assume(b>0)$ var_rayleigh(b);

                                 %pi
                             1 - ---
                                  4
(%o4)                        -------
                                2
                               b
```

<!-- category: Statistics -->
<!-- keywords: var_student_t -->
<!-- signatures: var_student_t(n) -->
### Function: var_student_t (n)

Returns the variance of a Student random variable $t(n)$, with $n>2$.



```maxima
(%i1) load ("distrib")$
(%i2) assume(n>2)$  var_student_t(n);
                                n
(%o3)                         -----
                              n - 2
```

<!-- category: Statistics -->
<!-- keywords: var_weibull -->
<!-- signatures: var_weibull(a, b) -->
### Function: var_weibull (a, b)

Returns the variance of a $Weibull(a,b)$ random variable, with
$a,b>0$.  To make use of this function, write first `load("distrib")`.

