## Statistics

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

### Function: cdf_empirical (cdf_empirical, list, option, ..., cdf_empirical, matrix, option, ...)

Empirical distribution function $F(x)$.


Data can be introduced as a list of numbers, or as an one column matrix.


The optional argument is the name of the variable in the returned expression,
which is *x* by default.


Example:


Empirical distribution function.













```maxima
(%i1) load ("descriptive")$

(%i2) F(x):= ''(cdf_empirical([1,3,3,5,7,7,7,8,9]));
(%o2) F(x) := (charfun(x >= 9) + charfun(x >= 8)
 + 3 charfun(x >= 7) + charfun(x >= 5) + 2 charfun(x >= 3)
 + charfun(x >= 1))/9


(%i3) F(6);
                                4
(%o3)                           -
                                9

(%i4) load("draw")$

(%i5) draw2d(
   line_width = 3,
   grid       = true,
   explicit(F(z), z, -2, 12)) $
```

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

### Function: cdf_rank_sum (x, n, m)

Cumulative distribution function of the exact distribution of the
rank sum statistic. Argument *x* is a real
number and *n* and *m* are both positive integers. 


See also `test_005frank_005fsum`.

See also: `test_rank_sum`.

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

### Function: cdf_signed_rank (x, n)

Cumulative distribution function of the exact distribution of the
signed rank statistic. Argument *x* is a real
number and *n* a positive integer. 


See also `test_005fsigned_005frank`.

See also: `test_signed_rank`.

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

### Function: central_moment (central_moment, x, k, central_moment, x, k, w)

Returns the central moment of order *k*.
*x* must be a list or matrix.


When *x* is a list,
`central_moment` returns the central moment of order *k* of *x*.


When *x* is a matrix,
`central_moment` returns a list comprising the central moment of order *k* of each column.


*w* is an optional per-datum weight.
*w* must either be 1, in which case every datum *x[i]* is given equal weight,
or a list of the same length as *x*,
in which case the weight for *x[i]* is given by *w[i]*.
The elements of *w* must be nonnegative and not all zero;
it is not required that they sum to 1.


The unweighted central moment of order *k* is defined as



```maxima
n
                 ====
              1  \          _ k
              -   >    (x - x)
              n  /       i
                 ====
                 i = 1
```


$${{1\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^k}}}$$


The weighted central moment of order *k* is defined as



```maxima
n
                 ====
              1  \             _ k
              -   >    w  (x - x)
              Z  /      i   i
                 ====
                 i = 1
```


$${{1\over{Z}}{\sum_{i=1}^{n}{w_{i} (x_{i}-\bar{x})^k}}}$$


where *Z* is the sum of the weights,



```maxima
n
                  ====
                  \
             Z =   >    w
                  /      i
                  ====
                  i = 1
```


$${Z={\sum_{i=1}^{n}{w_{i}}}}$$


Examples:


Second central moment of a list.
The second central moment is equal to the sample variance.









```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) central_moment (s1, 2), numer;
(%o3)                   8.425899999999999


(%i4) var (s1), numer;
(%o4)                   8.425899999999999
```


Third central moment of each column of a matrix.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) central_moment (s1, 2), numer; /* the variance */
(%o3)                   8.425899999999999

(%i5) s2 : read_matrix (file_search ("wind.data"))$

(%i6) central_moment (s2, 3);
(%o6) [11.29584771375004, 16.97988248298583, 5.626661952750102,
                             37.5986572057918, 25.85981904394192]
```


See also functions `central_moment` and `mean`.

See also: `central_moment`, `mean`.

### Function: cor (cor, matrix, cor, matrix, logical_value)

The correlation matrix of the multivariate sample.


Option:



- *
`'data`, default `'true`, indicates whether the input matrix contains the sample data,
in which case the covariance matrix `cov1` must be calculated, or not, and then the covariance
matrix (symmetric) must be given, instead of the data.


Examples:









```maxima
(%i1) load ("descriptive")$
(%i2) fpprintprec : 7 $
(%i3) s2 : read_matrix (file_search ("wind.data"))$

(%i4) cor (s2);
      [    1.0     0.8476339  0.8803515  0.8239624  0.7519506 ]
      [                                                       ]
      [ 0.8476339     1.0     0.8735834  0.6902622  0.782502  ]
      [                                                       ]
(%o4) [ 0.8803515  0.8735834     1.0     0.7764065  0.8323358 ]
      [                                                       ]
      [ 0.8239624  0.6902622  0.7764065     1.0     0.7293848 ]
      [                                                       ]
      [ 0.7519506  0.782502   0.8323358  0.7293848     1.0    ]
```


Calculate the correlation matrix from the covariance matrix.










```maxima
(%i1) load ("descriptive")$
(%i2) fpprintprec : 7 $
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) s : cov1 (s2)$

(%i5) cor (s, data=false); /* this is faster */
      [    1.0     0.8476339  0.8803515  0.8239624  0.7519506 ]
      [                                                       ]
      [ 0.8476339     1.0     0.8735834  0.6902622  0.782502  ]
      [                                                       ]
(%o5) [ 0.8803515  0.8735834     1.0     0.7764065  0.8323358 ]
      [                                                       ]
      [ 0.8239624  0.6902622  0.7764065     1.0     0.7293848 ]
      [                                                       ]
      [ 0.7519506  0.782502   0.8323358  0.7293848     1.0    ]
```


See also `cov` and `cov1`.

See also: `cov`, `cov1`.

### Function: cov (cov, X, cov, X, w)

Returns the sample covariance matrix.
*X* must be a matrix.


The sample covariance matrix has the same number of rows and columns,
both equal to the number of columns of *X*;
each diagonal element *X[i, i]* is equal to the sample variance of the *i*’th column,
and each off-diagonal element *X[i, j]* is equal to the sample covariance of the *i*’th and *j*’th columns.


*w* is an optional per-datum weight.
*w* must either be 1, in which case every datum *X[i]* is given equal weight,
or a list of the same length as *X*,
in which case the weight for *X[i]* is given by *w[i]*.
The elements of *w* must be nonnegative and not all zero;
it is not required that they sum to 1.


The unweighted sample covariance is defined as



```maxima
n
             ====
          1  \           _        _
      S = -   >    (X  - X) (X  - X)'
          n  /       j        j
             ====
             j = 1
```


$${S={1\over{n}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}$$


where *X[j]* is the *j*’th row of the sample matrix.


The weighted sample covariance is defined as



```maxima
n
             ====
          1  \           _        _
      S = -   >    w  (X  - X) (X  - X)'
          Z  /      j   j        j
             ====
             j = 1
```


$${S={1\over{Z}}{\sum_{j=1}^{n}{w_j \left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}$$


where *Z* is the sum of the weights,



```maxima
n
                  ====
                  \
             Z =   >    w
                  /      i
                  ====
                  i = 1
```


$${Z={\sum_{i=1}^{n}{w_{i}}}}$$


Example:









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec : 7$

(%i4) cov (s2);
      [ 17.22191  13.61811  14.37217  19.39624  15.42162 ]
      [                                                  ]
      [ 13.61811  14.98774  13.30448  15.15834  14.9711  ]
      [                                                  ]
(%o4) [ 14.37217  13.30448  15.47573  17.32544  16.18171 ]
      [                                                  ]
      [ 19.39624  15.15834  17.32544  32.17651  20.44685 ]
      [                                                  ]
      [ 15.42162  14.9711   16.18171  20.44685  24.42308 ]
```


See also function `cov1`.

See also: `cov1`.

### Function: cov1 (matrix)

The covariance matrix of the multivariate sample, defined as


```maxima
n
             ====
         1   \           _        _
   S  = ---   >    (X  - X) (X  - X)'
    1   n-1  /       j        j
             ====
             j = 1
```


$${{1\over{n-1}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}$$

where $X_j$ is the $j$-th row of the sample matrix.


Example:









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec : 7$

(%i4) cov1 (s2);
      [ 17.39587  13.75567  14.51734  19.59216  15.5774  ]
      [                                                  ]
      [ 13.75567  15.13913  13.43887  15.31145  15.12232 ]
      [                                                  ]
(%o4) [ 14.51734  13.43887  15.63205  17.50044  16.34516 ]
      [                                                  ]
      [ 19.59216  15.31145  17.50044  32.50153  20.65338 ]
      [                                                  ]
      [ 15.5774   15.12232  16.34516  20.65338  24.66977 ]
```


See also function `cov`.

See also: `cov`.

### Function: cv (cv, list, cv, matrix)

Returns the variation coefficient,
defined as the sample standard deviation `std` divided by the `mean`.


Examples:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) cv (s1), numer;
(%o3)                  0.6162930116383044

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) cv (s2);
(%o5) [0.4171411291632767, 0.38101703748061055, 
      0.3619561372346568, 0.3609199356430116, 0.3329249251309538]
```


See also functions `std` and `mean`.

See also: `std`, `mean`.

### Function: geometric_mean (geometric_mean, list, geometric_mean, matrix)

The geometric mean, defined as


```maxima
/  n      \ 1/n
                 | /===\   |
                 |  ! !    |
                 |  ! !  x |
                 |  ! !   i|
                 | i = 1   |
                 \         /
```


$$\left(\prod_{i=1}^{n}{x_{i}}\right)^{{{1}\over{n}}}$$


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$

(%i3) geometric_mean (y), numer;
(%o3)                   4.454845412337012

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) geometric_mean (s2);
(%o5) [8.82476274347979, 9.22652604739361, 10.044267571488904, 
                           14.612741263490207, 13.96184163444275]
```


See also functions `mean` and `harmonic_005fmean`.

See also: `mean`, `harmonic_mean`.

### Function: global_variances (global_variances, matrix, global_variances, matrix, options, ...)

Function `global_variances` returns a list of global variance measures:



- *
*total variance*: `trace(S_1)`,
- *
*mean variance*: `trace(S_1)/p`,
- *
*generalized variance*: `determinant(S_1)`,
- *
*generalized standard deviation*: `sqrt(determinant(S_1))`,
- *
*effective variance* `determinant(S_1)^(1/p)`, (defined in: Pena, D. (2002) *Analisis de datos multivariantes*; McGraw-Hill, Madrid.)
- *
*effective standard deviation*: `determinant(S_1)^(1/(2*p))`.

where *p* is the dimension of the multivariate random variable and $S_1$ the covariance matrix returned by `cov1`.


Option:



- *
`'data`, default `'true`, indicates whether the input matrix contains the sample data,
in which case the covariance matrix `cov1` must be calculated, or not, and then the covariance
matrix (symmetric) must be given, instead of the data.


Examples:


Calculate the `global_variances` from sample data.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) global_variances (s2);
(%o3) [105.33834206060595, 21.06766841212119, 12874.34690469686, 
       113.46517926085015, 6.636590811800794, 2.5761581496097623]
```


Calculate the `global_variances` from the covariance matrix.









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) s : cov1 (s2)$

(%i4) global_variances (s, data=false);
(%o4) [105.33834206060595, 21.06766841212119, 12874.34690469686, 
       113.46517926085015, 6.636590811800794, 2.5761581496097623]
```


See also `cov` and `cov1`.

See also: `cov`, `cov1`.

### Function: harmonic_mean (harmonic_mean, list, harmonic_mean, matrix)

The harmonic mean, defined as


```maxima
n
               --------
                n
               ====
               \     1
                >    --
               /     x
               ====   i
               i = 1
```


$${{n}\over{\sum_{i=1}^{n}{{{1}\over{x_{i}}}}}}$$


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$

(%i3) harmonic_mean (y), numer;
(%o3)                  3.9018580276322052

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) harmonic_mean (s2);
(%o5) [6.948015590052786, 7.391967752360356, 9.055658197151745, 
                           13.441990281936924, 13.01439145898509]
```


See also functions `mean` and `geometric_005fmean`.

See also: `mean`, `geometric_mean`.

### Function: inference_result (title, values, numbers)

Constructs an `inference_result` object of the type returned by the
stats functions. Argument *title* is a
string with the name of the procedure; *values* is a list with
elements of the form `symbol = value` and *numbers* is a list
with positive integer numbers ranging from one to `length(values)`,
indicating which values will be shown by default.


Example:


This is a simple example showing results concerning a rectangle. The title of
this object is the string `"Rectangle"`, it stores five results, named
`'base`, `'height`, `'diagonal`, `'area`,
and `'perimeter`, but only the first, second, fifth, and fourth
will be displayed. The `'diagonal` is stored in this object, but it is
not displayed; to access its value, make use of function `take_inference`.
















```maxima
(%i1) load("inference_result")$
(%i2) b: 3$ h: 2$
(%i3) inference_result("Rectangle",
                        ['base=b,
                         'height=h,
                         'diagonal=sqrt(b^2+h^2),
                         'area=b*h,
                         'perimeter=2*(b+h)],
                        [1,2,5,4] );
                        |   Rectangle
                        |
                        |    base = 3
                        |
(%o3)                   |   height = 2
                        |
                        | perimeter = 10
                        |
                        |    area = 6
(%i4) take_inference('diagonal,%);
(%o4)                        sqrt(13)
```


See also `take_005finference`.

See also: `take_inference`.

### Function: inferencep (obj)

Returns `true` or `false`, depending on whether *obj* is an
`inference_result` object or not.

### Function: items_inference (obj)

Returns a list with the names of the items stored in *obj*, which must
be an `inference_result` object.


Example:


The `inference_result` object stores two values, named `'pi` and `'e`,
but only the second is displayed. The `items_inference` function returns the names
of all items, no matter they are displayed or not.








```maxima
(%i1) load("inference_result")$
(%i2) inference_result("Hi", ['pi=%pi,'e=%e],[2]);
                            |   Hi
(%o2)                       |
                            | e = %e
(%i3) items_inference(%);
(%o3)                        [pi, e]
```

### Function: km (km, list, option, ..., km, matrix, option, ...)

Kaplan Meier estimator of the survival, or reliability, function $S(x)=1-F(x)$.


Data can be introduced as a list of pairs, or as a two column matrix. The first
component is the observed time, and the second component a censoring index 
(1 = non censored, 0 = right censored).


The optional argument is the name of the variable in the returned expression,
which is *x* by default.


Examples:


Sample as a list of pairs.











```maxima
(%i1) load ("descriptive")$

(%i2) S: km([[2,1], [3,1], [5,0], [8,1]]);
                       charfun((3 <= x) and (x < 8))
(%o2) charfun(x < 0) + -----------------------------
                                     2
   3 charfun((2 <= x) and (x < 3))
 + -------------------------------
                  4
 + charfun((0 <= x) and (x < 2))

(%i3) load ("draw")$

(%i4) draw2d(
  line_width = 3, grid = true,
  explicit(S, x, -0.1, 10))$
```


Estimate survival probabilities.








```maxima
(%i1) load ("descriptive")$
(%i2) S(t):= ''(km([[2,1], [3,1], [5,0], [8,1]], t)) $

(%i3) S(6);
                                1
(%o3)                           -
                                2
```

### Function: kurtosis (kurtosis, list, kurtosis, matrix)

The kurtosis coefficient, defined as


```maxima
n
                  ====
            1     \          _ 4
           ----    >    (x - x)  - 3
              4   /       i
           n s    ====
                  i = 1
```


$${{1\over{n s^4}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^4}}-3}$$


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) kurtosis (s1), numer;
(%o3)                  - 1.273247946514421

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) kurtosis (s2);
(%o5) [- 0.2715445622195385, 0.119998784429451, 
- 0.42752334904828615, - 0.6405361979019522, 
- 0.4952382132352935]
```


See also functions `mean`, `var` and `skewness`.

See also: `mean`, `var`, `skewness`.

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

### Function: linear_regression (linear_regression, x, linear_regression, x, option)

Multivariate linear regression, 
$y_i = b0 + b1*x_1i + b2*x_2i + ... + bk*x_ki + u_i$,
where $u_i$ are $N(0,sigma)$ independent random variables.
Argument *x* must be a matrix with more than one column. The
last column is considered as the responses ($y_i$).


Option:



- *
`'conflevel`, default `95/100`, confidence level for the
confidence intervals; it must be an expression which takes a value
in (0,1).


The output of function `linear_regression` is an 
`inference_result` Maxima object with the following results:



1. `'b_estimation`: regression coefficients estimates.
2. `'b_covariances`: covariance matrix of the regression 
coefficients estimates.
3. `b_conf_int`: confidence intervals of the regression coefficients.
4. `b_statistics`: statistics for testing coefficient.
5. `b_p_values`: p-values for coefficient tests.
6. `b_distribution`: probability distribution for coefficient tests.
7. `v_estimation`: unbiased variance estimator.
8. `v_conf_int`: variance confidence interval.
9. `v_distribution`: probability distribution for variance test.
10. `residuals`: residuals.
11. `adc`: adjusted determination coefficient.
12. `aic`: Akaike’s information criterion.
13. `bic`: Bayes’s information criterion.


Only items 1, 4, 5, 6, 7, 8, 9 and 11 above, in this order, 
are shown by default. The rest remain hidden until the user
makes use of functions `items_inference` and `take_inference`.


Example:


Fitting a linear model to a trivariate sample. The
last column is considered as the responses ($y_i$).




















```maxima
(%i2) load("stats")$
(%i3) X:matrix(
    [58,111,64],[84,131,78],[78,158,83],
    [81,147,88],[82,121,89],[102,165,99],
    [85,174,101],[102,169,102])$
(%i4) fpprintprec: 4$
(%i5) res: linear_regression(X);
             |       LINEAR REGRESSION MODEL         
             |                                       
             | b_estimation = [9.054, .5203, .2397]  
             |                                       
             | b_statistics = [.6051, 2.246, 1.74]   
             |                                       
             | b_p_values = [.5715, .07466, .1423]   
             |                                       
(%o5)        |   b_distribution = [student_t, 5]     
             |                                       
             |         v_estimation = 35.27          
             |                                       
             |     v_conf_int = [13.74, 212.2]       
             |                                       
             |      v_distribution = [chi2, 5]       
             |                                       
             |             adc = .7922               
(%i6) items_inference(res);
(%o6) [b_estimation, b_covariances, b_conf_int, b_statistics, 
b_p_values, b_distribution, v_estimation, v_conf_int, 
v_distribution, residuals, adc, aic, bic]
(%i7) take_inference('b_covariances, res);
                  [  223.9    - 1.12   - .8532  ]
                  [                             ]
(%o7)             [ - 1.12    .05367   - .02305 ]
                  [                             ]
                  [ - .8532  - .02305   .01898  ]
(%i8) take_inference('bic, res);
(%o8)                          30.98
(%i9) load("draw")$
(%i10) draw2d(
    points_joined = true,
    grid = true,
    points(take_inference('residuals, res)) )$
```

### Function: list_correlations (list_correlations, matrix, list_correlations, matrix, options, ...)

Function `list_correlations` returns a list of correlation measures:



- *
*precision matrix*: the inverse of the covariance matrix $S_1$,

```maxima
-1     ij
      S   = (s  )             
       1         i,j = 1,2,...,p
```

$${S_{1}^{-1}}={\left(s^{ij}\right)_{i,j=1,2,\ldots, p}}$$
- *
*multiple correlation vector*:  $(R_1^2, R_2^2, ..., R_p^2)$, with 

```maxima
2          1
      R  = 1 - -------
       i        ii
               s   s
                    ii
```

$${R_{i}^{2}}={1-{{1}\over{s^{ii}s_{ii}}}}$$
being an indicator of the goodness of fit of the linear multivariate regression model on $X_i$ when the rest of variables are used as regressors.
- *
*partial correlation matrix*: with element $(i, j)$ being

```maxima
ij
                        s
      r        = - ------------
       ij.rest     / ii  jj\ 1/2
                   |s   s  |
                   \       /
```

$${r_{ij.rest}}={-{{s^{ij}}\over \sqrt{s^{ii}s^{jj}}}}$$


Option:



- *
`'data`, default `'true`, indicates whether the input matrix contains the sample data,
in which case the covariance matrix `cov1` must be calculated, or not, and then the covariance
matrix (symmetric) must be given, instead of the data.


Example:












```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) z : list_correlations (s2)$
(%i4) fpprintprec : 5$

(%i5) precision_matrix: z[1];
(%o5) 
    [  0.38486   - 0.13856   - 0.15626   - 0.10239    0.031179  ]
    [                                                           ]
    [ - 0.13856   0.34107    - 0.15233    0.038447   - 0.052842 ]
    [                                                           ]
    [ - 0.15626  - 0.15233    0.47296    - 0.024816  - 0.10054  ]
    [                                                           ]
    [ - 0.10239   0.038447   - 0.024816   0.10937    - 0.034033 ]
    [                                                           ]
    [ 0.031179   - 0.052842  - 0.10054   - 0.034033   0.14834   ]


(%i6) multiple_correlation_vector: z[2];
(%o6)     [0.85063, 0.80634, 0.86474, 0.71867, 0.72675]


(%i7) partial_correlation_matrix: z[3];
      [   - 1.0     0.38244   0.36627   0.49908   - 0.13049 ]
      [                                                     ]
      [  0.38244     - 1.0    0.37927  - 0.19907   0.23492  ]
      [                                                     ]
(%o7) [  0.36627    0.37927    - 1.0    0.10911    0.37956  ]
      [                                                     ]
      [  0.49908   - 0.19907  0.10911    - 1.0     0.26719  ]
      [                                                     ]
      [ - 0.13049   0.23492   0.37956   0.26719     - 1.0   ]
```


See also `cov` and `cov1`.

See also: `cov`, `cov1`.

### Function: lsquares_estimates (lsquares_estimates, D, x, e, a, lsquares_estimates, D, x, e, a, initial, =, L, tol, =, t)

Estimate parameters *a* to best fit the equation *e*
in the variables *x* and *a* to the data *D*,
as determined by the method of least squares.
`lsquares_estimates` first seeks an exact solution,
and if that fails, then seeks an approximate solution.


The return value is a list of lists of equations of the form `[a = ..., b = ..., c = ...]`.
Each element of the list is a distinct, equivalent minimum of the mean square error.


The data *D* must be a matrix.
Each row is one datum (which may be called a ‘record’ or ‘case’ in some contexts),
and each column contains the values of one variable across all data.
The list of variables *x* gives a name for each column of *D*,
even the columns which do not enter the analysis.
The list of parameters *a* gives the names of the parameters for which
estimates are sought.
The equation *e* is an expression or equation in the variables *x* and *a*;
if *e* is not an equation, it is treated the same as `e = 0`.


Additional arguments to `lsquares_estimates`
are specified as equations and passed on verbatim to the function `lbfgs`
which is called to find estimates by a numerical method
when an exact result is not found.


If some exact solution can be found (via `solve`),
the data *D* may contain non-numeric values.
However, if no exact solution is found,
each element of *D* must have a numeric value.
This includes numeric constants such as `%pi` and `%e` as well as literal numbers
(integers, rationals, ordinary floats, and bigfloats).
Numerical calculations are carried out with ordinary floating-point arithmetic,
so all other kinds of numbers are converted to ordinary floats for calculations.


If `lsquares_estimates` needs excessive amounts of time or runs out of memory
`lsquares_estimates_approximate`, which skips the attempt to find an exact 
solution, might still succeed.


`load("lsquares")` loads this function.


See also
`lsquares_estimates_exact`,
`lsquares_estimates_approximate`,

`lsquares_mse`,
`lsquares_residuals`,
and `lsquares_residual_mse`.


Examples:


A problem for which an exact solution is found.










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
        [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]

(%i3) lsquares_estimates (
         M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
```


A problem for which no exact solution is found,
so `lsquares_estimates` resorts to numerical approximation.









```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix ([1, 1], [2, 7/4], [3, 11/4], [4, 13/4]);
                            [ 1  1  ]
                            [       ]
                            [    7  ]
                            [ 2  -  ]
                            [    4  ]
                            [       ]
(%o2)                       [    11 ]
                            [ 3  -- ]
                            [    4  ]
                            [       ]
                            [    13 ]
                            [ 4  -- ]
                            [    4  ]

(%i3) lsquares_estimates (
  M, [x,y], y=a*x^b+c, [a,b,c], initial=[3,3,3], iprint=[-1,0]);
(%o3) [[a = 1.375751433061394, b = 0.7148891534417651, 
                                       c = - 0.4020908910062951]]
```


Exponential functions aren’t well-conditioned for least min square fitting.
In case that fitting to them fails it might be possible to get rid of the
exponential function using an logarithm.













```maxima
(%i1) load ("lsquares")$
(%i2) yvalues: [1,3,5,60,200,203,80]$
(%i3) time: [1,2,4,5,6,8,10]$

(%i4) f: y=a*exp(b*t);
                                   b t
(%o4)                      y = a %e

(%i5) yvalues_log: log(yvalues)$

(%i6) f_log: log(subst(y=exp(y),f));
                                    b t
(%o6)                   y = log(a %e   )


(%i7) lsquares_estimates (transpose(matrix(yvalues_log,time)),
                          [y,t], f_log, [a,b]);
*************************************************
  N=    2   NUMBER OF CORRECTIONS=25
       INITIAL VALUES
 F=  6.802906290754687D+00   GNORM=  2.851243373781393D+01
*************************************************

I NFN FUNC                  GNORM                 STEPLENGTH

1   3 1.141838765593467D+00 1.067358003667488D-01 1.390943719972406D-02  
2   5 1.141118195694385D+00 1.237977833033414D-01 5.000000000000000D+00  
3   6 1.136945723147959D+00 3.806696991691383D-01 1.000000000000000D+00  
4   7 1.133958243220262D+00 3.865103550379243D-01 1.000000000000000D+00  
5   8 1.131725773805499D+00 2.292258231154026D-02 1.000000000000000D+00  
6   9 1.131625585698168D+00 2.664440547017370D-03 1.000000000000000D+00  
7  10 1.131620564856599D+00 2.519366958715444D-04 1.000000000000000D+00  

 THE MINIMIZATION TERMINATED WITHOUT DETECTING ERRORS.
 IFLAG = 0
(%o7)   [[a = 1.155904145765554, b = 0.5772666876959847]]
```

See also: `lsquares_estimates_approximate`, `lsquares_estimates_exact`, `lsquares_mse`, `lsquares_residuals`, `lsquares_residual_mse`.

### Function: lsquares_estimates_approximate (MSE, a, initial, =, L, tol, =, t)

Estimate parameters *a* to minimize the mean square error *MSE*,
via the numerical minimization function `lbfgs`.
The mean square error is an expression in the parameters *a*,
such as that returned by `lsquares_mse`.


The solution returned by `lsquares_estimates_approximate` is a local (perhaps global) minimum
of the mean square error.
For consistency with `lsquares_estimates_exact`,
the return value is a nested list which contains one element,
namely a list of equations of the form `[a = ..., b = ..., c = ...]`.


Additional arguments to `lsquares_estimates_approximate`
are specified as equations and passed on verbatim to the function `lbfgs`.


*MSE* must evaluate to a number when the parameters are assigned numeric values.
This requires that the data from which *MSE* was constructed
comprise only numeric constants such as `%pi` and `%e` and literal numbers
(integers, rationals, ordinary floats, and bigfloats).
Numerical calculations are carried out with ordinary floating-point arithmetic,
so all other kinds of numbers are converted to ordinary floats for calculations.


`load("lsquares")` loads this function.


See also
`lsquares_estimates`,
`lsquares_estimates_exact`,
`lsquares_mse`,

`lsquares_residuals`,
and `lsquares_residual_mse`.


Example:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
         5
        ====
        \                                         2     2
         >    ((- B M    ) - A M     + (M     + D)  - C)
        /            i, 3       i, 2     i, 1
        ====
        i = 1
(%o3)   -------------------------------------------------
                                5

(%i4) lsquares_estimates_approximate (
        mse, [A, B, C, D], iprint = [-1, 0]);
(%o4) [[A = - 3.678504947401971, B = - 1.683070351177937, 
                 C = 10.63469950148714, D = - 3.340357993175297]]
```

See also: `lsquares_estimates`, `lsquares_estimates_exact`, `lsquares_mse`, `lsquares_residuals`, `lsquares_residual_mse`.

### Function: lsquares_estimates_exact (MSE, a)

Estimate parameters *a* to minimize the mean square error *MSE*,
by constructing a system of equations and attempting to solve them symbolically via `solve`.
The mean square error is an expression in the parameters *a*,
such as that returned by `lsquares_mse`.


The return value is a list of lists of equations of the form `[a = ..., b = ..., c = ...]`.
The return value may contain zero, one, or two or more elements.
If two or more elements are returned,
each represents a distinct, equivalent minimum of the mean square error.


See also
`lsquares_estimates`,
`lsquares_estimates_approximate`,
`lsquares_mse`,
`lsquares_residuals`,
and `lsquares_residual_mse`.


Example:










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
         5
        ====
        \                                         2     2
         >    ((- B M    ) - A M     + (M     + D)  - C)
        /            i, 3       i, 2     i, 1
        ====
        i = 1
(%o3)   -------------------------------------------------
                                5

(%i4) lsquares_estimates_exact (mse, [A, B, C, D]);
                  59        27      10921        107
(%o4)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
```

See also: `lsquares_estimates`, `lsquares_estimates_approximate`, `lsquares_mse`, `lsquares_residuals`, `lsquares_residual_mse`.

### Function: lsquares_mse (D, x, e)

Returns the mean square error (MSE), a summation expression, for the equation *e*
in the variables *x*, with data *D*.


The MSE is defined as:



$${1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```


where *n* is the number of data and `e[i]` is the equation *e*
evaluated with the variables in *x* assigned values from the `i`-th datum, `D[i]`.


`load("lsquares")` loads this function.


Example:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
         5
        ====
        \                                         2     2
         >    ((- B M    ) - A M     + (M     + D)  - C)
        /            i, 3       i, 2     i, 1
        ====
        i = 1
(%o3)   -------------------------------------------------
                                5
(%i4) diff (mse, D);
(%o4) 
      5
     ====
     \                                                     2
   4  >    (M     + D) ((- B M    ) - A M     + (M     + D)  - C)
     /       i, 1             i, 3       i, 2     i, 1
     ====
     i = 1
   --------------------------------------------------------------
                                 5

(%i5) ''mse, nouns;
               2                 2         9 2               2
(%o5) (((D + 3)  - C - 2 B - 2 A)  + ((D + -)  - C - B - 2 A)
                                           4
           2               2         3 2               2
 + ((D + 2)  - C - B - 2 A)  + ((D + -)  - C - 2 B - A)
                                     2
           2             2
 + ((D + 1)  - C - B - A) )/5


(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5


(%i4) diff (mse, D);
         5
        ====
        \                             2
      4  >    (D + M    ) ((D + M    )  - C - M     B - M     A)
        /           i, 1         i, 1          i, 3      i, 2
        ====
        i = 1
(%o4) ----------------------------------------------------------
                                  5


(%i5) ''mse, nouns;


               2                 2         9 2               2
(%o5) (((D + 3)  - C - 2 B - 2 A)  + ((D + -)  - C - B - 2 A)
                                           4
           2               2         3 2               2
 + ((D + 2)  - C - B - 2 A)  + ((D + -)  - C - 2 B - A)
                                     2
           2             2
 + ((D + 1)  - C - B - A) )/5
```

### Function: lsquares_residual_mse (D, x, e, a)

Returns the residual mean square error (MSE) for the equation *e*
with specified parameters *a* and data *D*.


The residual MSE is defined as:



$${1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```


where `e[i]` is the equation *e*
evaluated with the variables in *x* assigned values from the `i`-th datum, `D[i]`,
and assigning any remaining free variables from *a*.


`load("lsquares")` loads this function.


Example:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]

(%i3) a : lsquares_estimates (
       M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32


(%i4) lsquares_residual_mse (
       M, [z,x,y], (z + D)^2 = A*x + B*y + C, first (a));
                              169
(%o4)                         ----
                              2560
```

### Function: lsquares_residuals (D, x, e, a)

Returns the residuals for the equation *e*
with specified parameters *a* and data *D*.


*D* is a matrix, *x* is a list of variables,
*e* is an equation or general expression;
if not an equation, *e* is treated as if it were `e = 0`.
*a* is a list of equations which specify values for any free parameters in *e* aside from *x*.


The residuals are defined as:



$${\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right),$$


```maxima
lhs(e ) - rhs(e )
                             i         i
```


where `e[i]` is the equation *e*
evaluated with the variables in *x* assigned values from the `i`-th datum, `D[i]`,
and assigning any remaining free variables from *a*.


`load("lsquares")` loads this function.


Example:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]

(%i3) a : lsquares_estimates (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32


(%i4) lsquares_residuals (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, first(a));
                     13    13    13  13  13
(%o4)               [--, - --, - --, --, --]
                     64    64    32  64  64
```

### Function: mean (mean, x, mean, x, w)

Returns the sample mean.
*x* must be a list or matrix.


When *x* is a list,
`mean` returns the sample mean of *x*.


When *x* is a matrix,
`mean` returns a list comprising the sample mean of each column.


When *x* is an empty list or an empty matrix (no rows),
`mean` returns `und` (undefined).


*w* is an optional per-datum weight.
*w* must either be 1, in which case every datum *x[i]* is given equal weight,
or a list of the same length as *x*,
in which case the weight for *x[i]* is given by *w[i]*.
The elements of *w* must be nonnegative and not all zero;
it is not required that they sum to 1.


The unweighted sample mean is defined as



```maxima
n
                    ====
             _   1  \
             x = -   >    x
                 n  /      i
                    ====
                    i = 1
```


$${\bar{x}={1\over{n}}{\sum_{i=1}^{n}{x_{i}}}}$$


The weighted sample mean is defined as



```maxima
n
                    ====
             _   1  \
             x = -   >    w  x
                 Z  /      i  i
                    ====
                    i = 1
```


$${\bar{x}={1\over{Z}}{\sum_{i=1}^{n}{w_{i} x_{i}}}}$$


where *Z* is the sum of the weights,



```maxima
n
                  ====
                  \
             Z =   >    w
                  /      i
                  ====
                  i = 1
```


$${Z={\sum_{i=1}^{n}{w_{i}}}}$$


Examples:


Sample mean of a list.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) mean (s1);
                               471
(%o3)                          ---
                               100
```


Sample mean of each column of a matrix.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) mean (s2);
(%o3) [9.9485, 10.160700000000004, 10.868499999999997, 
                          15.716600000000001, 14.844100000000001]
```


Weighted sample mean of a list.







```maxima
(%i1) load ("descriptive")$

(%i2) mean ([a, b, c, d], [1, 2, 3, 4]);
                       4 d + 3 c + 2 b + a
(%o2)                  -------------------
                               10
```


Weighted sample mean of each column of a matrix.








```maxima
(%i1) load ("descriptive")$

(%i2) mm: matrix ([p, q, r], [s, t, u]);
                           [ p  q  r ]
(%o2)                      [         ]
                           [ s  t  u ]


(%i3) mean (mm, [vv, ww]);
              s ww + p vv  t ww + q vv  u ww + r vv
(%o3)        [-----------, -----------, -----------]
                ww + vv      ww + vv      ww + vv
```

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

### Function: mean_deviation (mean_deviation, list, mean_deviation, matrix)

The mean deviation, defined as


```maxima
n
                   ====
               1   \          _
               -    >    |x - x|
               n   /       i
                   ====
                   i = 1
```


$${{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-\bar{x}|}}}$$


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) mean_deviation (s1);
                               51
(%o3)                          --
                               20

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) mean_deviation (s2);
(%o5) [3.2879599999999987, 3.075342, 3.2390700000000003, 
                            4.715664000000001, 4.028546000000002]
```


See also function `mean`.

See also: `mean`.

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

### Function: median (median, list, median, matrix)

Once the sample is ordered, if the sample size is odd the median is the central value, otherwise it is the mean of the two central values.


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) median (s1);
                                9
(%o3)                           -
                                2

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) median (s2);
(%o5)   [10.059999999999999, 9.855, 10.73, 15.48, 14.105]
```


The median is the 1/2-quantile.


See also function `quantile`.

See also: `quantile`.

### Function: median_deviation (median_deviation, list, median_deviation, matrix)

The median deviation, defined as


```maxima
n
               ====
           1   \
           -    >    |x - med|
           n   /       i
               ====
               i = 1
```


$${{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-med|}}}$$

where `med` is the median of *list*.


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) median_deviation (s1);
                                5
(%o3)                           -
                                2

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) median_deviation (s2);
(%o5) [2.75, 2.7550000000000003, 3.08, 4.315, 3.3099999999999996]
```


See also function `mean`.

See also: `mean`.

### Function: noncentral_moment (noncentral_moment, x, k, noncentral_moment, x, k, w)

Returns the noncentral moment of order *k*.
*x* must be a list or matrix.


When *x* is a list,
`noncentral_moment` returns the noncentral moment of order *k* of *x*.


When *x* is a matrix,
`noncentral_moment` returns a list comprising the noncentral moment of order *k* of each column.


*w* is an optional per-datum weight.
*w* must either be 1, in which case every datum *x[i]* is given equal weight,
or a list of the same length as *x*,
in which case the weight for *x[i]* is given by *w[i]*.
The elements of *w* must be nonnegative and not all zero;
it is not required that they sum to 1.


The unweighted noncentral moment of order *k* is defined as



```maxima
n
                    ====
                 1  \      k
                 -   >    x
                 n  /      i
                    ====
                    i = 1
```


$${{1\over{n}}{\sum_{i=1}^{n}{x_{i}^k}}}$$


The weighted noncentral moment of order *k* is defined as



```maxima
n
                    ====
                 1  \         k
                 -   >    w  x
                 Z  /      i  i
                    ====
                    i = 1
```


$${{1\over{Z}}{\sum_{i=1}^{n}{w_{i} x_{i}^k}}}$$


where *Z* is the sum of the weights,



```maxima
n
                  ====
                  \
             Z =   >    w
                  /      i
                  ====
                  i = 1
```


$${Z={\sum_{i=1}^{n}{w_{i}}}}$$


Examples:


First noncentral moment of a list.
The first noncentral moment is equal to the sample mean.









```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) noncentral_moment (s1, 1), numer;
(%o3)                         4.71


(%i4) mean (s1), numer;
(%o4)                         4.71
```


Fifth noncentral moment of each column of a matrix.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) noncentral_moment (s2, 5);
(%o3) [319793.87247615046, 320532.19238924625, 
       391249.56213815557, 2502278.205988911, 1691881.7977422548]
```


See also function `central_005fmoment`.

See also: `central_moment`.

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

### Function: pdf_rank_sum (x, n, m)

Probability density function of the exact distribution of the
rank sum statistic. Argument *x* is a real
number and *n* and *m* are both positive integers. 


See also `test_005frank_005fsum`.

See also: `test_rank_sum`.

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

### Function: pdf_signed_rank (x, n)

Probability density function of the exact distribution of the
signed rank statistic. Argument *x* is a real
number and *n* a positive integer.


See also `test_005fsigned_005frank`.

See also: `test_signed_rank`.

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

### Function: pearson_skewness (pearson_skewness, list, pearson_skewness, matrix)

Pearson’s skewness coefficient, defined as 


```maxima
_
             3 (x - med)
             -----------
                  s
```


$${{3\,\left(\bar{x}-med\right)}\over{s}}$$

where *med* is the median of *list*.


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) pearson_skewness (s1), numer;
(%o3)                  0.21594840290938955

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) pearson_skewness (s2);
(%o5) [- 0.08019976629211892, 0.2357036272952649, 
   0.10509040624912039, 0.12450423405923679, 0.44641817958045193]
```


See also functions `mean`, `var` and `median`.

See also: `mean`, `var`, `median`.

### Function: plsquares (plsquares, Mat, VarList, depvars, plsquares, Mat, VarList, depvars, maxexpon, plsquares, Mat, VarList, depvars, maxexpon, maxdegree)

Multivariable polynomial adjustment of a data table by the "least squares"
method. *Mat* is a matrix containing the data, *VarList* is a list of variable names (one for each Mat column, but use "-" instead of varnames to ignore Mat columns), *depvars* is the name of a dependent variable or a list with one or more names of dependent variables (which names should be in *VarList*), *maxexpon* is the optional maximum exponent for each independent variable (1 by default), and *maxdegree* is the optional maximum polynomial degree (*maxexpon* by default); note that the sum of exponents of each term must be equal or smaller than *maxdegree*, and if `maxdgree = 0` then no limit is applied.


If *depvars* is the name of a dependent variable (not in a list), `plsquares` returns the adjusted polynomial. If *depvars* is a list of one or more dependent variables, `plsquares` returns a list with the adjusted polynomial(s). The Coefficients of Determination  are displayed in order to inform about the goodness of fit, which ranges from 0 (no correlation) to 1 (exact correlation). These values are also stored in the global variable *DETCOEF* (a list if *depvars* is a list).



A simple example of multivariable linear adjustment:


```maxima
(%i1) load("plsquares")$

(%i2) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z);
     Determination Coefficient for z = .9897039897039897
                       11 y - 9 x - 14
(%o2)              z = ---------------
                              3
```


The same example without degree restrictions:


```maxima
(%i3) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z,1,0);
     Determination Coefficient for z = 1.0
                    x y + 23 y - 29 x - 19
(%o3)           z = ----------------------
                              6
```


How many diagonals does a N-sides polygon have? What polynomial degree should be used?


```maxima
(%i4) plsquares(matrix([3,0],[4,2],[5,5],[6,9],[7,14],[8,20]),
                [N,diagonals],diagonals,5);
     Determination Coefficient for diagonals = 1.0
                                2
                               N  - 3 N
(%o4)              diagonals = --------
                                  2
(%i5) ev(%, N=9);   /* Testing for a 9 sides polygon */
(%o5)                 diagonals = 27
```


How many ways do we have to put two queens without they are threatened into a n x n chessboard?


```maxima
(%i6) plsquares(matrix([0,0],[1,0],[2,0],[3,8],[4,44]),
                [n,positions],[positions],4);
     Determination Coefficient for [positions] = [1.0]

                         4       3      2
                      3 n  - 10 n  + 9 n  - 2 n
(%o6)    [positions = -------------------------]
                                  6

(%i7) ev(%[1], n=8); /* Testing for a (8 x 8) chessboard */
(%o7)                positions = 1288
```


An example with six dependent variables:


```maxima
(%i8) mtrx:matrix([0,0,0,0,0,1,1,1],[0,1,0,1,1,1,0,0],
                  [1,0,0,1,1,1,0,0],[1,1,1,1,0,0,0,1])$
(%i8) plsquares(mtrx,[a,b,_And,_Or,_Xor,_Nand,_Nor,_Nxor],
                     [_And,_Or,_Xor,_Nand,_Nor,_Nxor],1,0);
      Determination Coefficient for
[_And, _Or, _Xor, _Nand, _Nor, _Nxor] =
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
(%o2) [_And = a b, _Or = - a b + b + a,
_Xor = - 2 a b + b + a, _Nand = 1 - a b,
_Nor = a b - b - a + 1, _Nxor = 2 a b - b - a + 1]
```


To use this function write first `load("lsquares")`.

### Function: principal_components (principal_components, matrix, principal_components, matrix, options, ...)

Calculates the principal components of a multivariate sample. Principal components are
used in multivariate statistical analysis to reduce the dimensionality of the sample.


Option:



- *
`'data`, default `'true`, indicates whether the input matrix contains the sample data,
in which case the covariance matrix `cov1` must be calculated, or not, and then the covariance
matrix (symmetric) must be given, instead of the data.


The output of function `principal_components` is a list with the following results:



- *
variances of the principal components,
- *
percentage of total variance explained by each principal component,
- *
rotation matrix.


Examples:


In this sample, the first component explains 83.13 per cent of total 
variance.



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec:4 $
(%i4) res: principal_components(s2);
0 errors, 0 warnings
(%o4) [[87.57, 8.753, 5.515, 1.889, 1.613], 
[83.13, 8.31, 5.235, 1.793, 1.531], 

[ .4149  .03379   - .4757  - 0.581   - .5126 ]
[                                            ]
[ 0.369  - .3657  - .4298   .7237    - .1469 ]
[                                            ]
[ .3959  - .2178  - .2181  - .2749    .8201  ]]
[                                            ]
[ .5548   .7744    .1857    .2319    .06498  ]
[                                            ]
[ .4765  - .4669   0.712   - .09605  - .1969 ]

(%i5) /* accumulated percentages  */
    block([ap: copy(res[2])],
      for k:2 thru length(ap) do ap[k]: ap[k]+ap[k-1],
      ap);
(%o5)                 [83.13, 91.44, 96.68, 98.47, 100.0]
(%i6) /* sample dimension */
      p: length(first(res));
(%o6)                                  5
(%i7) /* plot percentages to select number of
         principal components for further work */
     draw2d(
        fill_density = 0.2,
        apply(bars, makelist([k, res[2][k], 1/2], k, p)),
        points_joined = true,
        point_type    = filled_circle,
        point_size    = 3,
        points(makelist([k, res[2][k]], k, p)),
        xlabel = "Variances",
        ylabel = "Percentages",
        xtics  = setify(makelist([concat("PC",k),k], k, p))) $
```


In case the covariance matrix is known, it can be passed to the function,
but option `data=false` must be used.



```maxima
(%i1) load ("descriptive")$
(%i2) S: matrix([1,-2,0],[-2,5,0],[0,0,2]);
                                [  1   - 2  0 ]
                                [             ]
(%o2)                           [ - 2   5   0 ]
                                [             ]
                                [  0    0   2 ]
(%i3) fpprintprec:4 $
(%i4) /* the argument is a covariance matrix */
      res: principal_components(S, data=false);
0 errors, 0 warnings
                                                  [ - .3827  0.0  .9239 ]
                                                  [                     ]
(%o4) [[5.828, 2.0, .1716], [72.86, 25.0, 2.145], [  .9239   0.0  .3827 ]]
                                                  [                     ]
                                                  [   0.0    1.0   0.0  ]
(%i5) /* transformation to get the principal components
         from original records */
      matrix([a1,b2,c3],[a2,b2,c2]).last(res);
             [ .9239 b2 - .3827 a1  1.0 c3  .3827 b2 + .9239 a1 ]
(%o5)        [                                                  ]
             [ .9239 b2 - .3827 a2  1.0 c2  .3827 b2 + .9239 a2 ]
```

See also: `cov1`.

### Function: qrange (qrange, x)

Returns the interquartile range,
defined as the difference between the third and first quartiles:
`quantile(x, 3/4) - quantile(x, 1/4)`


*x* must be a list or matrix.
When *x* is a matrix,
`qrange` returns the interquartile range for each column.


Examples:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) qrange (s1);
                               21
(%o3)                          --
                               4

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) qrange (s2);
(%o5) [5.385, 5.572499999999998, 6.022500000000001, 
                            8.729999999999999, 6.649999999999999]
```


See also function `quantile`.

See also: `quantile`.

### Function: quantile (quantile, list, p, quantile, matrix, p)

This is the *p*-quantile, with *p* a number in $[0, 1]$, of the sample *list*.
Although there are several definitions for the sample quantile (Hyndman, R. J., Fan, Y. (1996) *Sample quantiles in statistical packages*. American Statistician, 50, 361-365), the one based on linear interpolation is implemented in package `Package-descriptive`


Examples:


Input is a list. First and third quartiles are computed.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) [quantile (s1, 1/4), quantile (s1, 3/4)], numer;
(%o3)                      [2.0, 7.25]
```


Input is a matrix. First quartile is computed for each column.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) quantile (s2, 1/4);
(%o3)    [7.2575, 7.477500000000001, 7.82, 11.28, 11.48]
```

See also: `Package-descriptive`.

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

### Function: quartile_skewness (quartile_skewness, list, quartile_skewness, matrix)

The quartile skewness coefficient, defined as 


```maxima
c    - 2 c    + c
                3/4      1/2    1/4
               --------------------
                   c    - c
                    3/4    1/4
```


$${{c_{{{3}\over{4}}}-2\,c_{{{1}\over{2}}}+c_{{{1}\over{4}}}}\over{c
 _{{{3}\over{4}}}-c_{{{1}\over{4}}}}}$$

where $c_p$ is the *p*-quantile of sample *list*.


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) quartile_skewness (s1), numer;
(%o3)                 0.047619047619047616

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) quartile_skewness (s2);
(%o5) [- 0.040854224698235304, 0.14670255720053824, 
   0.033623910336239196, 0.03780068728522298, 0.2105263157894735]
```


See also function `quantile`.

See also: `quantile`.

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

### Function: range (range, list, range, matrix)

The range is the difference between the extreme values.


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) range (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) range (s2);
(%o5)   [19.67, 20.96, 17.369999999999997, 24.38, 22.46]
```

### Function: skewness (skewness, list, skewness, matrix)

The skewness coefficient, defined as


```maxima
n
                  ====
            1     \          _ 3
           ----    >    (x - x)
              3   /       i
           n s    ====
                  i = 1
```


$${{1\over{n s^3}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^3}}}$$


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) skewness (s1), numer;
(%o3)                 0.009196180476450424

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) skewness (s2);
(%o5) [0.1580509020000978, 0.2926379232061854, 
   0.09242174416107717, 0.20599843481486865, 0.21425202488908313]
```


See also functions `mean`,, `var` and `kurtosis`.

See also: `mean`, `var`, `kurtosis`.

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

### Function: smax (smax, list, smax, matrix)

This is the maximum value of the sample *list*.
When the argument is a matrix, `smax` returns
a list containing the maximum values of the columns,
which are associated to statistical variables.


Examples:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) smax (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) smax (s2);
(%o5)          [20.25, 21.46, 20.04, 29.63, 27.63]
```


See also function `smin`.

See also: `smax`, `smin`.

### Function: smin (smin, list, smin, matrix)

This is the minimum value of the sample *list*.
When the argument is a matrix, `smin` returns
a list containing the minimum values of the columns,
which are associated to statistical variables.


Examples:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) smin (s1);
(%o3)                           0

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) smin (s2);
(%o5)             [0.58, 0.5, 2.67, 5.25, 5.17]
```


See also function `smax`.

See also: `smin`, `smax`.

### Variable: stats_numer

Default value: `true`


If `stats_numer` is `true`, inference statistical functions 
return their results in floating point numbers. If it is `false`,
results are given in symbolic and rational format.

### Function: std (std, x, std, x, w)

Returns the sample standard deviation.
*x* must be a list or matrix.


When *x* is a list,
`std` returns the sample standard deviation of *x*,
which is defined as the square root of the sample variance,
as computed by `var`.


When *x* is a matrix,
`std` returns a list comprising the sample standard deviation of each column.


*w* is an optional per-datum weight.
*w* must either be 1, in which case every datum *x[i]* is given equal weight,
or a list of the same length as *x*,
in which case the weight for *x[i]* is given by *w[i]*.
The elements of *w* must be nonnegative and not all zero;
it is not required that they sum to 1.


Example:


Sample standard deviation of a list.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) std (s1), numer;
(%o3)                  2.9027400848164135
```


Sample standard deviation of each column of a matrix.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) std (s2);
(%o3) [4.149928523480858, 3.8713998127292415, 
        3.9339202775348663, 5.672434260526957, 4.941970881136392]
```


See also functions `var` and `std1`.

See also: `var`, `std1`.

### Function: std1 (std1, list, std1, matrix)

This is the square root of the function `var1`, the variance with denominator $n-1$.


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) std1 (s1), numer;
(%o3)                   2.917363553109228

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) std1 (s2);
(%o5) [4.170835096721089, 3.8909032097803196, 
        3.9537386411375555, 5.701010936401517, 4.966867617451963]
```


See also functions `var1` and `std`.

See also: `var1`, `std`.

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

### Function: take_inference (take_inference, n, obj, take_inference, name, obj, take_inference, list, obj)

Returns the *n*-th value stored in *obj* if *n* is a positive integer,
or the item named *name* if this is the name of an item. If the first
argument is a list of numbers and/or symbols, function `take_inference` returns
a list with the corresponding results.


Example:


Given an `inference_result` object, function `take_inference` is
called in order to extract some information stored in it.



















```maxima
(%i1) load("inference_result")$
(%i2) b: 3$ h: 2$
(%i3) sol: inference_result("Rectangle",
                            ['base=b,
                             'height=h,
                             'diagonal=sqrt(b^2+h^2),
                             'area=b*h,
                             'perimeter=2*(b+h)],
                            [1,2,5,4] );
                        |   Rectangle
                        |
                        |    base = 3
                        |
(%o3)                   |   height = 2
                        |
                        | perimeter = 10
                        |
                        |    area = 6
(%i4) take_inference('base,sol);
(%o4)                           3
(%i5) take_inference(5,sol);
(%o5)                          10
(%i6) take_inference([1,'diagonal],sol);
(%o6)                     [3, sqrt(13)]
(%i7) take_inference(items_inference(sol),sol);
(%o7)                [3, 2, sqrt(13), 6, 10]
```


See also `inference_result`, and `take_005finference`.

See also: `inference_result`, `take_inference`.

### Function: test_mean (test_mean, x, test_mean, x, options, ...)

This is the mean *t*-test. Argument *x* is a list or a column matrix
containing an one dimensional sample. It also performs an asymptotic test
based on the *Central Limit Theorem* if option `'asymptotic` is
`true`.


Options:



- *
`'mean`, default `0`, is the mean value to be checked.
- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.
- *
`'dev`, default `'unknown`, this is the value of the standard deviation when it is 
known; valid values are: `'unknown` or a positive expression.
- *
`'conflevel`, default `95/100`, confidence level for the confidence interval; it must
be an expression which takes a value in (0,1).
- *
`'asymptotic`, default `false`, indicates whether it performs an exact *t*-test or
an asymptotic one based on the *Central Limit Theorem*;
valid values are `true` and `false`.


The output of function `test_mean` is an `inference_result` Maxima object
showing the following results:



1. `'mean_estimate`: the sample mean.
2. `'conf_level`: confidence level selected by the user.
3. `'conf_interval`: confidence interval for the population mean.
4. `'method`: inference procedure.
5. `'hypotheses`: null and alternative hypotheses to be tested.
6. `'statistic`: value of the sample statistic used for testing the null hypothesis.
7. `'distribution`: distribution of the sample statistic, together with its parameter(s).
8. `'p_value`: $p$-value of the test.


Examples:


Performs an exact *t*-test with unknown variance. The null hypothesis
is $H_0: mean=50$ against the one sided alternative $H_1: mean<50$;
according to the results, the $p$-value is too great, there are no
evidence for rejecting $H_0$.








```maxima
(%i1) load("stats")$
(%i2) data: [78,64,35,45,45,75,43,74,42,42]$
(%i3) test_mean(data,'conflevel=0.9,'alternative='less,'mean=50);
          |                 MEAN TEST
          |
          |            mean_estimate = 54.3
          |
          |              conf_level = 0.9
          |
          | conf_interval = [minf, 61.51314273502712]
          |
(%o3)     |  method = Exact t-test. Unknown variance.
          |
          | hypotheses = H0: mean = 50 , H1: mean < 50
          |
          |       statistic = .8244705235071678
          |
          |       distribution = [student_t, 9]
          |
          |        p_value = .7845100411786889
```


This time Maxima performs an asymptotic test, based on the *Central Limit Theorem*.
The null hypothesis is $H_0: equal(mean, 50)$ against the two sided alternative $H_1: not equal(mean, 50)$;
according to the results, the $p$-value is very small, $H_0$ should be rejected in
favor of the alternative $H_1$. Note that, as indicated by the `Method` component,
this procedure should be applied to large samples.










```maxima
(%i1) load("stats")$
(%i2) test_mean([36,118,52,87,35,256,56,178,57,57,89,34,25,98,35,
              98,41,45,198,54,79,63,35,45,44,75,42,75,45,45,
              45,51,123,54,151],
              'asymptotic=true,'mean=50);
          |                       MEAN TEST
          |
          |           mean_estimate = 74.88571428571429
          |
          |                   conf_level = 0.95
          |
          | conf_interval = [57.72848600856194, 92.04294256286663]
          |
(%o2)     |    method = Large sample z-test. Unknown variance.
          |
          |       hypotheses = H0: mean = 50 , H1: mean # 50
          |
          |             statistic = 2.842831192874313
          |
          |             distribution = [normal, 0, 1]
          |
          |             p_value = .004471474652002261
```

### Function: test_means_difference (test_means_difference, x1, x2, test_means_difference, x1, x2, options, ...)

This is the difference of means *t*-test for two samples.
Arguments *x1* and *x2* are lists or column matrices
containing two independent samples. In case of different unknown variances
(see options `'dev1`, `'dev2` and `'varequal` below),
the degrees of freedom are computed by means of the Welch approximation.
It also performs an asymptotic test
based on the *Central Limit Theorem* if option `'asymptotic` is
set to `true`.


Options:



- *
- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.
- *
`'dev1`, default `'unknown`, this is the value of the standard deviation
of the *x1* sample when it is known; valid values are: `'unknown` or a positive expression.
- *
`'dev2`, default `'unknown`, this is the value of the standard deviation
of the *x2* sample when it is known; valid values are: `'unknown` or a positive expression.
- *
`'varequal`, default `false`, whether variances should be considered to be equal or not;
this option takes effect only when `'dev1` and/or `'dev2` are  `'unknown`.
- *
`'conflevel`, default `95/100`, confidence level for the confidence interval; it must
be an expression which takes a value in (0,1).
- *
`'asymptotic`, default `false`, indicates whether it performs an exact *t*-test or
an asymptotic one based on the *Central Limit Theorem*;
valid values are `true` and `false`.


The output of function `test_means_difference` is an `inference_result` Maxima object
showing the following results:



1. `'diff_estimate`: the difference of means estimate.
2. `'conf_level`: confidence level selected by the user.
3. `'conf_interval`: confidence interval for the difference of means.
4. `'method`: inference procedure.
5. `'hypotheses`: null and alternative hypotheses to be tested.
6. `'statistic`: value of the sample statistic used for testing the null hypothesis.
7. `'distribution`: distribution of the sample statistic, together with its parameter(s).
8. `'p_value`: $p$-value of the test.


Examples:


The equality of means is tested with two small samples *x* and *y*,
against the alternative $H_1: m_1>m_2$, being $m_1$ and $m_2$
the populations means; variances are unknown and supposed to be different.














```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: [1.2,6.9,38.7,20.4,17.2]$
(%i4) test_means_difference(x,y,'alternative='greater);
            |              DIFFERENCE OF MEANS TEST
            |
            |         diff_estimate = 20.31999999999999
            |
            |                 conf_level = 0.95
            |
            |    conf_interval = [- .04597417812882298, inf]
            |
(%o4)       |        method = Exact t-test. Welch approx.
            |
            | hypotheses = H0: mean1 = mean2 , H1: mean1 > mean2
            |
            |           statistic = 1.838004300728477
            |
            |    distribution = [student_t, 8.62758740184604]
            |
            |            p_value = .05032746527991905
```


The same test as before, but now variances are supposed to be
equal.















```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: matrix([1.2],[6.9],[38.7],[20.4],[17.2])$
(%i4) test_means_difference(x,y,'alternative='greater,
                                                 'varequal=true);
            |              DIFFERENCE OF MEANS TEST
            |
            |         diff_estimate = 20.31999999999999
            |
            |                 conf_level = 0.95
            |
            |     conf_interval = [- .7722627696897568, inf]
            |
(%o4)       |   method = Exact t-test. Unknown equal variances
            |
            | hypotheses = H0: mean1 = mean2 , H1: mean1 > mean2
            |
            |           statistic = 1.765996124515009
            |
            |           distribution = [student_t, 9]
            |
            |            p_value = .05560320992529344
```

### Function: test_normality (x)

Shapiro-Wilk test for normality. Argument *x* is a list of numbers, and sample
size must be greater than 2 and less or equal than 5000, otherwise, function
`test_normality` signals an error message.


Reference:


  

[1] Algorithm AS R94, Applied Statistics (1995), vol.44, no.4, 547-551


The output of function `test_normality` is an `inference_result` Maxima object
with the following results:



1. `'statistic`: value of the *W* statistic.
2. `'p_value`: $p$-value under normal assumption.


Examples:


Checks for the normality of a population, based on a sample of size 9.












```maxima
(%i1) load("stats")$
(%i2) x:[12,15,17,38,42,10,23,35,28]$
(%i3) test_normality(x);
                       |      SHAPIRO - WILK TEST
                       |
(%o3)                  | statistic = .9251055695162436
                       |
                       |  p_value = .4361763918860381
```

### Function: test_proportion (test_proportion, x, n, test_proportion, x, n, options, ...)

Inferences on a proportion. Argument *x* is the number of successes
in *n* trials in a Bernoulli experiment with unknown probability.


Options:



- *
`'proportion`, default `1/2`, is the value of the proportion to be checked.
- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.
- *
`'conflevel`, default `95/100`, confidence level for the confidence interval; it must
be an expression which takes a value in (0,1).
- *
`'asymptotic`, default `false`, indicates whether it performs an exact test
based on the binomial distribution, or an asymptotic one based on the *Central Limit Theorem*;
valid values are `true` and `false`.
- *
`'correct`, default `true`, indicates whether Yates correction is applied or not.


The output of function `test_proportion` is an `inference_result` Maxima object
showing the following results:



1. `'sample_proportion`: the sample proportion.
2. `'conf_level`: confidence level selected by the user.
3. `'conf_interval`: Wilson confidence interval for the proportion.
4. `'method`: inference procedure.
5. `'hypotheses`: null and alternative hypotheses to be tested.
6. `'statistic`: value of the sample statistic used for testing the null hypothesis.
7. `'distribution`: distribution of the sample statistic, together with its parameters.
8. `'p_value`: $p$-value of the test.


Examples:


Performs an exact test. The null hypothesis
is $H_0: p=1/2$ against the one sided alternative $H_1: p<1/2$.







```maxima
(%i1) load("stats")$
(%i2) test_proportion(45, 103, alternative = less);
         |            PROPORTION TEST              
         |                                         
         | sample_proportion = .4368932038834951   
         |                                         
         |           conf_level = 0.95             
         |                                         
         | conf_interval = [0, 0.522714149150231]  
         |                                         
(%o2)    |     method = Exact binomial test.       
         |                                         
         | hypotheses = H0: p = 0.5 , H1: p < 0.5  
         |                                         
         |             statistic = 45              
         |                                         
         |  distribution = [binomial, 103, 0.5]    
         |                                         
         |      p_value = .1184509388901454
```


A two sided asymptotic test. Confidence level is 99/100.









```maxima
(%i1) load("stats")$
(%i2) fpprintprec:7$
(%i3) test_proportion(45, 103, 
                  conflevel = 99/100, asymptotic=true);
      |                 PROPORTION TEST                  
      |                                                  
      |           sample_proportion = .43689             
      |                                                  
      |                conf_level = 0.99                 
      |                                                  
      |        conf_interval = [.31422, .56749]          
      |                                                  
(%o3) | method = Asympthotic test with Yates correction.
      |                                                  
      |     hypotheses = H0: p = 0.5 , H1: p # 0.5       
      |                                                  
      |               statistic = .43689                 
      |                                                  
      |      distribution = [normal, 0.5, .048872]       
      |                                                  
      |                p_value = .19662
```

### Function: test_proportions_difference (test_proportions_difference, x1, n1, x2, n2, test_proportions_difference, x1, n1, x2, n2, options, ...)

Inferences on the difference of two proportions. Argument *x1* is the number of successes
in *n1* trials in a Bernoulli experiment in the first population, and *x2* and *n2*
are the corresponding values in the second population. Samples are independent and the test
is asymptotic.


Options:



- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided` (`p1 # p2`), `'greater` (`p1 > p2`)
and `'less` (`p1 < p2`).
- *
`'conflevel`, default `95/100`, confidence level for the confidence interval; it must
be an expression which takes a value in (0,1).
- *
`'correct`, default `true`, indicates whether Yates correction is applied or not.


The output of function `test_proportions_difference` is an `inference_result` Maxima object
showing the following results:



1. `'proportions`: list with the two sample proportions.
2. `'conf_level`: confidence level selected by the user.
3. `'conf_interval`: Confidence interval for the difference of proportions `p1 - p2`.
4. `'method`: inference procedure and warning message in case of any of the samples sizes
is less than 10.
5. `'hypotheses`: null and alternative hypotheses to be tested.
6. `'statistic`: value of the sample statistic used for testing the null hypothesis.
7. `'distribution`: distribution of the sample statistic, together with its parameters.
8. `'p_value`: $p$-value of the test.


Examples:


A machine produced 10 defective articles in a batch of 250.
After some maintenance work, it produces 4 defective in a batch of 150.
In order to know if the machine has improved, we test the null
hypothesis `H0:p1=p2`, against the alternative `H0:p1>p2`,
where `p1` and `p2` are the probabilities for one produced
article to be defective before and after maintenance. According to
the p value, there is not enough evidence to accept the alternative.









```maxima
(%i1) load("stats")$
(%i2) fpprintprec:7$
(%i3) test_proportions_difference(10, 250, 4, 150,
                                alternative = greater);
      |       DIFFERENCE OF PROPORTIONS TEST         
      |                                              
      |       proportions = [0.04, .02666667]        
      |                                              
      |              conf_level = 0.95               
      |                                              
      |      conf_interval = [- .02172761, 1]        
      |                                              
(%o3) | method = Asymptotic test. Yates correction.  
      |                                              
      |   hypotheses = H0: p1 = p2 , H1: p1 > p2     
      |                                              
      |            statistic = .01333333             
      |                                              
      |    distribution = [normal, 0, .01898069]     
      |                                              
      |             p_value = .2411936
```


Exact standard deviation of the asymptotic normal
distribution when the data are unknown.









```maxima
(%i1) load("stats")$
(%i2) stats_numer: false$
(%i3) sol: test_proportions_difference(x1,n1,x2,n2)$
(%i4) last(take_inference('distribution,sol));
               1    1                  x2 + x1
              (-- + --) (x2 + x1) (1 - -------)
               n2   n1                 n2 + n1
(%o4)    sqrt(---------------------------------)
                           n2 + n1
```

### Function: test_rank_sum (test_rank_sum, x1, x2, test_rank_sum, x1, x2, option)

This is the Wilcoxon-Mann-Whitney test for comparing the medians of two
continuous populations. The first two arguments *x1* and *x2* are lists
or column matrices with the data of two independent samples. Performs normal
approximation if any of the sample sizes is greater than 10, or if there are ties.


Option:



- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.


The output of function `test_rank_sum` is an `inference_result` Maxima object
with the following results:



1. `'method`: inference procedure.
2. `'hypotheses`: null and alternative hypotheses to be tested.
3. `'statistic`: value of the sample statistic used for testing the null hypothesis.
4. `'distribution`: distribution of the sample statistic, together with its parameters.
5. `'p_value`: $p$-value of the test.


Examples:


Checks whether populations have similar medians. Samples sizes
are small and an exact test is made.














```maxima
(%i1) load("stats")$
(%i2) x:[12,15,17,38,42,10,23,35,28]$
(%i3) y:[21,18,25,14,52,65,40,43]$
(%i4) test_rank_sum(x,y);
              |                 RANK SUM TEST
              |
              |              method = Exact test
              |
              | hypotheses = H0: med1 = med2 , H1: med1 # med2
(%o4)         |
              |                 statistic = 22
              |
              |        distribution = [rank_sum, 9, 8]
              |
              |          p_value = .1995886466474702
```


Now, with greater samples and ties, the procedure makes 
normal approximation. The alternative hypothesis is
$H_1: median1 < median2$.














```maxima
(%i1) load("stats")$
(%i2) x: [39,42,35,13,10,23,15,20,17,27]$
(%i3) y: [20,52,66,19,41,32,44,25,14,39,43,35,19,56,27,15]$
(%i4) test_rank_sum(x,y,'alternative='less);
             |                  RANK SUM TEST
             |
             |          method = Asymptotic test. Ties
             |
             |  hypotheses = H0: med1 = med2 , H1: med1 < med2
(%o4)        |
             |                 statistic = 48.5
             |
             | distribution = [normal, 79.5, 18.95419580097078]
             |
             |           p_value = .05096985666598441
```

### Function: test_sign (test_sign, x, test_sign, x, options, ...)

This is the non parametric sign test for the median of a continuous population.
Argument *x* is a list or a column matrix containing an one dimensional sample.


Options:



- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.
- *
`'median`, default `0`, is the median value to be checked.


The output of function `test_sign` is an `inference_result` Maxima object
showing the following results:



1. `'med_estimate`: the sample median.
2. `'method`: inference procedure.
3. `'hypotheses`: null and alternative hypotheses to be tested.
4. `'statistic`: value of the sample statistic used for testing the null hypothesis.
5. `'distribution`: distribution of the sample statistic, together with its parameter(s).
6. `'p_value`: $p$-value of the test.


Examples:


Checks whether the population from which the sample was taken has median 6, 
against the alternative $H_1: median > 6$.








```maxima
(%i1) load("stats")$
(%i2) x: [2,0.1,7,1.8,4,2.3,5.6,7.4,5.1,6.1,6]$
(%i3) test_sign(x,'median=6,'alternative='greater);
               |                  SIGN TEST
               |
               |              med_estimate = 5.1
               |
               |      method = Non parametric sign test.
               |
(%o3)          | hypotheses = H0: median = 6 , H1: median > 6
               |
               |                statistic = 7
               |
               |      distribution = [binomial, 10, 0.5]
               |
               |         p_value = .05468749999999989
```

### Function: test_signed_rank (test_signed_rank, x, test_signed_rank, x, options, ...)

This is the Wilcoxon signed rank test to make inferences about the median of a
continuous population. Argument *x* is a list or a column matrix
containing an one dimensional sample. Performs normal approximation if the
sample size is greater than 20, or if there are zeroes or ties.



See also `pdf_rank_test` and `cdf_rank_test`


Options:



- *
`'median`, default `0`, is the median value to be checked.
- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.


The output of function `test_signed_rank` is an `inference_result` Maxima object
with the following results:



1. `'med_estimate`: the sample median.
2. `'method`: inference procedure.
3. `'hypotheses`: null and alternative hypotheses to be tested.
4. `'statistic`: value of the sample statistic used for testing the null hypothesis.
5. `'distribution`: distribution of the sample statistic, together with its parameter(s).
6. `'p_value`: $p$-value of the test.


Examples:


Checks the null hypothesis $H_0: median = 15$ against the 
alternative $H_1: median > 15$. This is an exact test, since
there are no ties.












```maxima
(%i1) load("stats")$
(%i2) x: [17.1,15.9,13.7,13.4,15.5,17.6]$
(%i3) test_signed_rank(x,median=15,alternative=greater);
                 |             SIGNED RANK TEST
                 |
                 |           med_estimate = 15.7
                 |
                 |           method = Exact test
                 |
(%o3)            | hypotheses = H0: med = 15 , H1: med > 15
                 |
                 |              statistic = 14
                 |
                 |     distribution = [signed_rank, 6]
                 |
                 |            p_value = 0.28125
```


Checks the null hypothesis $H_0: equal(median, 2.5)$ against the 
alternative $H_1: not equal(median, 2.5)$. This is an approximated test,
since there are ties.












```maxima
(%i1) load("stats")$
(%i2) y:[1.9,2.3,2.6,1.9,1.6,3.3,4.2,4,2.4,2.9,1.5,3,2.9,4.2,3.1]$
(%i3) test_signed_rank(y,median=2.5);
             |                 SIGNED RANK TEST
             |
             |                med_estimate = 2.9
             |
             |          method = Asymptotic test. Ties
             |
(%o3)        |    hypotheses = H0: med = 2.5 , H1: med # 2.5
             |
             |                 statistic = 76.5
             |
             | distribution = [normal, 60.5, 17.58195097251724]
             |
             |           p_value = .3628097734643669
```

### Function: test_variance (test_variance, x, test_variance, x, options, ...)

This is the variance *chi^2*-test. Argument *x* is a list or a column matrix
containing an one dimensional sample taken from a normal population.


Options:



- *
`'mean`, default `'unknown`, is the population’s mean, when it is known.
- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.
- *
`'variance`, default `1`, this is the variance value (positive) to be checked.
- *
`'conflevel`, default `95/100`, confidence level for the confidence interval; it must
be an expression which takes a value in (0,1).


The output of function `test_variance` is an `inference_result` Maxima object
showing the following results:



1. `'var_estimate`: the sample variance.
2. `'conf_level`: confidence level selected by the user.
3. `'conf_interval`: confidence interval for the population variance.
4. `'method`: inference procedure.
5. `'hypotheses`: null and alternative hypotheses to be tested.
6. `'statistic`: value of the sample statistic used for testing the null hypothesis.
7. `'distribution`: distribution of the sample statistic, together with its parameter.
8. `'p_value`: $p$-value of the test.


Examples:


It is tested whether the variance of a population with unknown mean
is equal to or greater than 200.








```maxima
(%i1) load("stats")$
(%i2) x: [203,229,215,220,223,233,208,228,209]$
(%i3) test_variance(x,'alternative='greater,'variance=200);
             |                  VARIANCE TEST
             |
             |              var_estimate = 110.75
             |
             |                conf_level = 0.95
             |
             |     conf_interval = [57.13433376937479, inf]
             |
(%o3)        | method = Variance Chi-square test. Unknown mean.
             |
             |    hypotheses = H0: var = 200 , H1: var > 200
             |
             |                 statistic = 4.43
             |
             |             distribution = [chi2, 8]
             |
             |           p_value = .8163948512777689
```

### Function: test_variance_ratio (test_variance_ratio, x1, x2, test_variance_ratio, x1, x2, options, ...)

This is the variance ratio *F*-test for two normal populations.
Arguments *x1* and *x2* are lists or column matrices
containing two independent samples.


Options:



- *
`'alternative`, default `'twosided`, is the alternative hypothesis;
valid values are: `'twosided`, `'greater` and `'less`.
- *
`'mean1`, default `'unknown`, when it is known, this is the mean of
the population from which *x1* was taken.
- *
`'mean2`, default `'unknown`, when it is known, this is the mean of
the population from which *x2* was taken.
- *
`'conflevel`, default `95/100`, confidence level for the confidence interval of the
ratio; it must be an expression which takes a value in (0,1).


The output of function `test_variance_ratio` is an `inference_result` Maxima object
showing the following results:



1. `'ratio_estimate`: the sample variance ratio.
2. `'conf_level`: confidence level selected by the user.
3. `'conf_interval`: confidence interval for the variance ratio.
4. `'method`: inference procedure.
5. `'hypotheses`: null and alternative hypotheses to be tested.
6. `'statistic`: value of the sample statistic used for testing the null hypothesis.
7. `'distribution`: distribution of the sample statistic, together with its parameters.
8. `'p_value`: $p$-value of the test.



Examples:


The equality of the variances of two normal populations is checked
against the alternative that the first is greater than the second.














```maxima
(%i1) load("stats")$
(%i2) x: [20.4,62.5,61.3,44.2,11.1,23.7]$
(%i3) y: [1.2,6.9,38.7,20.4,17.2]$
(%i4) test_variance_ratio(x,y,'alternative='greater);
              |              VARIANCE RATIO TEST
              |
              |       ratio_estimate = 2.316933391522034
              |
              |               conf_level = 0.95
              |
              |    conf_interval = [.3703504689507268, inf]
              |
(%o4)         | method = Variance ratio F-test. Unknown means.
              |
              | hypotheses = H0: var1 = var2 , H1: var1 > var2
              |
              |         statistic = 2.316933391522034
              |
              |            distribution = [f, 5, 4]
              |
              |          p_value = .2179269692254457
```

### Function: var (var, x, var, x, w)

Returns the sample variance.
*x* must be a list or matrix.


When *x* is a list,
`var` returns the sample variance of *x*.


When *x* is a matrix,
`var` returns a list comprising the sample variance of each column.


*w* is an optional per-datum weight.
*w* must either be 1, in which case every datum *x[i]* is given equal weight,
or a list of the same length as *x*,
in which case the weight for *x[i]* is given by *w[i]*.
The elements of *w* must be nonnegative and not all zero;
it is not required that they sum to 1.


The unweighted sample variance is defined as



```maxima
n
                  ====
           2   1  \          _ 2
          s  = -   >    (x - x)
               n  /       i
                  ====
                  i = 1
```


$${{1}\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}$$


The weighted sample variance is defined as



```maxima
n
                  ====
           2   1  \             _ 2
          s  = -   >    w  (x - x)
               Z  /      i   i
                  ====
                  i = 1
```


$${{1}\over{Z}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}$$


where *Z* is the sum of the weights,



```maxima
n
                  ====
                  \
             Z =   >    w
                  /      i
                  ====
                  i = 1
```


$${Z={\sum_{i=1}^{n}{w_{i}}}}$$


Example:


Sample variance of a list.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var (s1), numer;
(%o3)                   8.425899999999999
```


Sample variance of each column of a matrix.








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) var (s2);
(%o3) [17.22190675000001, 14.987736510000005, 
       15.475728749999998, 32.17651044000001, 24.423076190000007]
```


Weighted sample variance of a list.







```maxima
(%i1) load ("descriptive")$

(%i2) var ([a - b, a, a + b], [3, 5, 7]);
                                  2
                             134 b
(%o2)                        ------
                              225
```


Weighted sample variance of each column of a matrix.








```maxima
(%i1) load ("descriptive")$

(%i2) mm: matrix ([a - b, c - d], [a, c], [a + b, c + d]);
                        [ a - b  c - d ]
                        [              ]
(%o2)                   [   a      c   ]
                        [              ]
                        [ b + a  d + c ]


(%i3) var (mm, [3, 5, 7]);
                              2       2
                         134 b   134 d
(%o3)                   [------, ------]
                          225     225
```


See also function `var1`.

See also: `var1`.

### Function: var1 (var1, list, var1, matrix)

This is the sample variance, defined as


```maxima
n
                   ====
               1   \          _ 2
              ---   >    (x - x)
              n-1  /       i
                   ====
                   i = 1
```


$${{1\over{n-1}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}}$$


Example:










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var1 (s1), numer;
(%o3)                    8.5110101010101

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) var1 (s2);
(%o5) [17.395865404040414, 15.139127787878794, 
       15.632049242424243, 32.50152569696971, 24.669773929292937]
```


See also function `var`.

See also: `var`.

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

