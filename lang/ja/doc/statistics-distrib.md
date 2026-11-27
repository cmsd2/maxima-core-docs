## distrib

<!-- category: Statistics -->
<!-- keywords: cdf_bernoulli -->
<!-- signatures: cdf_bernoulli(x, p) -->
### Function: cdf_bernoulli (x, p)

$0<p<1$で、  $Bernoulli(p)$確率変数の分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_beta -->
<!-- signatures: cdf_beta(x, a, b) -->
### Function: cdf_beta (x, a, b)

$a,b>0$で、 $Beta(a,b)$確率変数の
分布函数の
*x*での値を返します。








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

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の分布函数の*x*での値を返します。








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

$b>0$で、 $Cauchy(a,b)$確率変数の分布函数の*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_chi2 -->
<!-- signatures: cdf_chi2(x, n) -->
### Function: cdf_chi2 (x, n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の分布函数の *x*での値を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_discrete_uniform -->
<!-- signatures: cdf_discrete_uniform(x, n) -->
### Function: cdf_discrete_uniform (x, n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の分風函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_exp -->
<!-- signatures: cdf_exp(x, m) -->
### Function: cdf_exp (x, m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
分布函数の
*x*での値を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull分布に基づいた名詞形を返します。








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

$m,n>0$で、F確率変数 $F(m,n)$の
分布関数の
*x*の値を返します。








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

$a,b>0$で、 $Gamma(a,b)$確率変数の
分布函数の
*x*での値を返します。








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

ベクトル確率 $v$を持つ
一般有限離散確率変数の
分布函数の
*x*での値を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。









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

<!-- category: Statistics -->
<!-- keywords: cdf_geometric -->
<!-- signatures: cdf_geometric(x, p) -->
### Function: cdf_geometric (x, p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_gumbel -->
<!-- signatures: cdf_gumbel(x, a, b) -->
### Function: cdf_gumbel (x, a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の分布函数の*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_hypergeometric -->
<!-- signatures: cdf_hypergeometric(x, n1, n2, n) -->
### Function: cdf_hypergeometric (x, n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_laplace -->
<!-- signatures: cdf_laplace(x, a, b) -->
### Function: cdf_laplace (x, a, b)

$b>0$で、 $Laplace(a,b)$確率変数の分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_logistic -->
<!-- signatures: cdf_logistic(x, a, b) -->
### Function: cdf_logistic (x, a, b)

$b>0$で、 $Logistic(a,b)$確率変数の
分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_lognormal -->
<!-- signatures: cdf_lognormal(x, m, s) -->
### Function: cdf_lognormal (x, m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
分布函数の
*x*での値を返します。
この関数はMaximaの組み込み誤差関数 `erf`を使って定義されます。








```maxima
(%i1) load ("distrib")$
(%i2) assume(x>0, s>0)$  cdf_lognormal(x,m,s);
                           log(x) - m
                       erf(----------)
                           sqrt(2) s     1
(%o3)                  --------------- + -
                              2          2
```


`erf`も参照してください。

<!-- category: Statistics -->
<!-- keywords: cdf_negative_binomial -->
<!-- signatures: cdf_negative_binomial(x, n, p) -->
### Function: cdf_negative_binomial (x, n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の分布函数の
*x*での値を返します。








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

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
分布函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_noncentral_student_t -->
<!-- signatures: cdf_noncentral_student_t(x, n, ncp) -->
### Function: cdf_noncentral_student_t (x, n, ncp)

$n>0$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の分布函数の*x*での値を返します。
この函数は閉形式を持たず、
もしグローバル変数`numer`が`true`に等しいか
引数の少なくとも1つが浮動小数点数なら、数値的に計算されます。
そうでなければ、名目上の式を返します。








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

$s>0$で $Normal(m,s)$(正規)確率変数の密度函数の *x*での値を返します。
この関数はMaximaの組み込み誤差関数 `erf`を使って定義されます。







```maxima
(%i1) load ("distrib")$
(%i2) assume(s>0)$ cdf_normal(x,m,s);
                             x - m
                       erf(---------)
                           sqrt(2) s    1
(%o3)                  -------------- + -
                             2          2
```


`erf`も参照してください。

<!-- category: Statistics -->
<!-- keywords: cdf_pareto -->
<!-- signatures: cdf_pareto(x, a, b) -->
### Function: cdf_pareto (x, a, b)

$a,b>0$で、 $Pareto(a,b)$確率変数の
分布函数の
*x*の値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: cdf_poisson -->
<!-- signatures: cdf_poisson(x, m) -->
### Function: cdf_poisson (x, m)

$m>0$で、 $Poisson(m)$確率変数の分布函数の *x*での値を返します。








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

$b>0$で、 $Rayleigh(b)$確率変数の
分布函数の
*x*での値を返します。


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull分布に基づいた名詞形を返します。








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

$n>0$自由度のStudent確率変数 $t(n)$の分布函数の *x*での値を返します。








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

$a,b>0$で、 $Weibull(a,b)$確率変数の
分布函数の
*x*の値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_bernoulli -->
<!-- signatures: kurtosis_bernoulli(p) -->
### Function: kurtosis_bernoulli (p)

$0<p<1$で、 $Bernoulli(p)$確率変数の尖度係数を返します。


$Bernoulli(p)$確率変数は $Binomial(1,p)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
二項尖度係数に基づいた名詞形を返します。








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

$a,b>0$で、 $Beta(a,b)$確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_binomial -->
<!-- signatures: kurtosis_binomial(n, p) -->
### Function: kurtosis_binomial (n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_chi2 -->
<!-- signatures: kurtosis_chi2(n) -->
### Function: kurtosis_chi2 (n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の尖度係数を返します。


$Chi^2(n)$確率変数は
$Gamma(n/2,2)$に同値なので、
Maximaが結果を得るのに充分な情報を持たない時には、
ガンマ尖度係数に基づいた名詞形を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_discrete_uniform -->
<!-- signatures: kurtosis_discrete_uniform(n) -->
### Function: kurtosis_discrete_uniform (n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_exp -->
<!-- signatures: kurtosis_exp(m) -->
### Function: kurtosis_exp (m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
尖度係数を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull尖度係数に基づいた名詞形を返します。








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

$m,n>8$で、F確率変数 $F(m,n)$の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_gamma -->
<!-- signatures: kurtosis_gamma(a, b) -->
### Function: kurtosis_gamma (a, b)

$a,b>0$で、 $Gamma(a,b)$確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_general_finite_discrete -->
<!-- signatures: kurtosis_general_finite_discrete(v) -->
### Function: kurtosis_general_finite_discrete (v)

ベクトル確率 $v$を持つ
一般有限離散確率変数の
尖度係数を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_geometric -->
<!-- signatures: kurtosis_geometric(p) -->
### Function: kurtosis_geometric (p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_gumbel -->
<!-- signatures: kurtosis_gumbel(a, b) -->
### Function: kurtosis_gumbel (a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_hypergeometric -->
<!-- signatures: kurtosis_hypergeometric(n1, n2, n) -->
### Function: kurtosis_hypergeometric (n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_laplace -->
<!-- signatures: kurtosis_laplace(a, b) -->
### Function: kurtosis_laplace (a, b)

$b>0$で、 $Laplace(a,b)$確率変数の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_logistic -->
<!-- signatures: kurtosis_logistic(a, b) -->
### Function: kurtosis_logistic (a, b)

$b>0$で、 $Logistic(a,b)$確率変数の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_lognormal -->
<!-- signatures: kurtosis_lognormal(m, s) -->
### Function: kurtosis_lognormal (m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_negative_binomial -->
<!-- signatures: kurtosis_negative_binomial(n, p) -->
### Function: kurtosis_negative_binomial (n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_noncentral_chi2 -->
<!-- signatures: kurtosis_noncentral_chi2(n, ncp) -->
### Function: kurtosis_noncentral_chi2 (n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
尖度係数を返します。

<!-- category: Statistics -->
<!-- keywords: kurtosis_noncentral_student_t -->
<!-- signatures: kurtosis_noncentral_student_t(n, ncp) -->
### Function: kurtosis_noncentral_student_t (n, ncp)

$n>3$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_normal -->
<!-- signatures: kurtosis_normal(m, s) -->
### Function: kurtosis_normal (m, s)

$s>0$で $Normal(m,s)$(正規)確率変数の尖度を返します。それは常に0に等しいです。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_pareto -->
<!-- signatures: kurtosis_pareto(a, b) -->
### Function: kurtosis_pareto (a, b)

$a>2,b>0$で、 $Pareto(a,b)$確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_poisson -->
<!-- signatures: kurtosis_poisson(m) -->
### Function: kurtosis_poisson (m)

$m>0$で、 $Poisson(m)$確率変数の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_rayleigh -->
<!-- signatures: kurtosis_rayleigh(b) -->
### Function: kurtosis_rayleigh (b)

$b>0$で、 $Rayleigh(b)$確率変数の尖度係数を返します。


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull尖度係数に基づいた名詞形を返します。








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

$n>4$自由度のStudent確率変数 $t(n)$の尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: kurtosis_weibull -->
<!-- signatures: kurtosis_weibull(a, b) -->
### Function: kurtosis_weibull (a, b)

$a,b>0$で、 $Weibull(a,b)$確率変数の
尖度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_bernoulli -->
<!-- signatures: mean_bernoulli(p) -->
### Function: mean_bernoulli (p)

$0<p<1$で、  $Bernoulli(p)$確率変数の平均を返します。


$Bernoulli(p)$確率変数は $Binomial(1,p)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
二項平均に基づいた名詞形を返します。








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

$a,b>0$で、 $Beta(a,b)$確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_binomial -->
<!-- signatures: mean_binomial(n, p) -->
### Function: mean_binomial (n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_chi2 -->
<!-- signatures: mean_chi2(n) -->
### Function: mean_chi2 (n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の平均を返します。


$Chi^2(n)$確率変数は
$Gamma(n/2,2)$に同値なので、
Maximaが結果を得るのに充分な情報を持たない時には、
ガンマ平均に基づいた名詞形を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_discrete_uniform -->
<!-- signatures: mean_discrete_uniform(n) -->
### Function: mean_discrete_uniform (n)

Returns the mean of a $Discrete Uniform(n)$ random variable, with $n$ a strictly positive integer.
この関数を利用するには、初めに `load("distrib")`を書いてください。
 To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_exp -->
<!-- signatures: mean_exp(m) -->
### Function: mean_exp (m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
平均を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull平均に基づいた名詞形を返します。








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

$m,n>2$で、F確率変数 $F(m,n)$の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_gamma -->
<!-- signatures: mean_gamma(a, b) -->
### Function: mean_gamma (a, b)

$a,b>0$で、 $Gamma(a,b)$確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_general_finite_discrete -->
<!-- signatures: mean_general_finite_discrete(v) -->
### Function: mean_general_finite_discrete (v)

ベクトル確率 $v$を持つ
一般有限離散確率変数の
平均を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。

<!-- category: Statistics -->
<!-- keywords: mean_geometric -->
<!-- signatures: mean_geometric(p) -->
### Function: mean_geometric (p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_gumbel -->
<!-- signatures: mean_gumbel(a, b) -->
### Function: mean_gumbel (a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の平均を返します。







```maxima
(%i1) load ("distrib")$
(%i2) assume(b>0)$  mean_gumbel(a,b);
(%o3)                     %gamma b + a
```

ここでシンボル `%gamma`は Euler-Mascheroni定数を表します。
`%gamma`も参照してください。

<!-- category: Statistics -->
<!-- keywords: mean_hypergeometric -->
<!-- signatures: mean_hypergeometric(n1, n2, n) -->
### Function: mean_hypergeometric (n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_laplace -->
<!-- signatures: mean_laplace(a, b) -->
### Function: mean_laplace (a, b)

$b>0$で、 $Laplace(a,b)$確率変数の平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_logistic -->
<!-- signatures: mean_logistic(a, b) -->
### Function: mean_logistic (a, b)

$b>0$で、 $Logistic(a,b)$確率変数の平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_lognormal -->
<!-- signatures: mean_lognormal(m, s) -->
### Function: mean_lognormal (m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_negative_binomial -->
<!-- signatures: mean_negative_binomial(n, p) -->
### Function: mean_negative_binomial (n, p)

Returns the mean of a $Negative Binomial(n,p)$ random variable, with $0<p<1$ and $n$ a positive integer.
この関数を利用するには、初めに `load("distrib")`を書いてください。
 To make use of this function, write first `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_noncentral_chi2 -->
<!-- signatures: mean_noncentral_chi2(n, ncp) -->
### Function: mean_noncentral_chi2 (n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
平均を返します。

<!-- category: Statistics -->
<!-- keywords: mean_noncentral_student_t -->
<!-- signatures: mean_noncentral_student_t(n, ncp) -->
### Function: mean_noncentral_student_t (n, ncp)

$n>0$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。







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

$s>0$で $Normal(m,s)$(正規)確率変数の平均、すなわち *m*を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_pareto -->
<!-- signatures: mean_pareto(a, b) -->
### Function: mean_pareto (a, b)

$a,b>0$で、 $Pareto(a,b)$確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_poisson -->
<!-- signatures: mean_poisson(m) -->
### Function: mean_poisson (m)

$m>0$で、 $Poisson(m)$確率変数の平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_rayleigh -->
<!-- signatures: mean_rayleigh(b) -->
### Function: mean_rayleigh (b)

Returns the mean of a $Rayleigh(b)$ random variable, with $b>0$.


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull平均に基づいた名詞形を返します。








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

$n>0$自由度のStudent確率変数 $t(n)$の平均を返します。
それはいつも0に等しいです。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: mean_weibull -->
<!-- signatures: mean_weibull(a, b) -->
### Function: mean_weibull (a, b)

$a,b>0$で、 $Weibull(a,b)$確率変数の
平均を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_bernoulli -->
<!-- signatures: pdf_bernoulli(x, p) -->
### Function: pdf_bernoulli (x, p)

$0<p<1$で、  $Bernoulli(p)$確率変数の確率函数の
*x*での値を返します。


$Bernoulli(p)$確率変数は $Binomial(1,p)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
二項確率函数に基づいた名詞形を返します。








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

$a,b>0$で、 $Beta(a,b)$確率変数の
密度函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_binomial -->
<!-- signatures: pdf_binomial(x, n, p) -->
### Function: pdf_binomial (x, n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の確率函数の*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。
                                  4
(%o6)                             -
                                  7

<!-- category: Statistics -->
<!-- keywords: pdf_cauchy -->
<!-- signatures: pdf_cauchy(x, a, b) -->
### Function: pdf_cauchy (x, a, b)

$b>0$で、 $Cauchy(a,b)$確率変数の密度函数の*x*での値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_chi2 -->
<!-- signatures: pdf_chi2(x, n) -->
### Function: pdf_chi2 (x, n)

$n>0$でカイ二乗確率変数 $Chi^2(n)$の密度函数の *x*での値を返します。


$Chi^2(n)$確率変数は
$Gamma(n/2,2)$と同値です。
だから Maximaは結果を得るのに充分な情報を持っていない時
ガンマ密度に基づいた名詞形を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の密度函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_discrete_uniform -->
<!-- signatures: pdf_discrete_uniform(x, n) -->
### Function: pdf_discrete_uniform (x, n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の確率函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_exp -->
<!-- signatures: pdf_exp(x, m) -->
### Function: pdf_exp (x, m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
密度函数の
*x*での値を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull密度に基づいた名詞形を返します。








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

$m,n>0$で、F確率変数 $F(m,n)$の密度関数の
*x*の値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_gamma -->
<!-- signatures: pdf_gamma(x, a, b) -->
### Function: pdf_gamma (x, a, b)

$a,b>0$で、 $Gamma(a,b)$確率変数の
密度函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_general_finite_discrete -->
<!-- signatures: pdf_general_finite_discrete(x, v) -->
### Function: pdf_general_finite_discrete (x, v)

`Pr(X=i) = v_i`のような
ベクトル確率 $v$を持つ
一般有限離散確率変数の
確率函数の
*x*での値を返します。
ベクトル $v$は非負式のリストであり得ます。
その成分は確率のベクトルを得るために規格化されます。
この関数を利用するには、初めに `load("distrib")`を書いてください。








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

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の確率函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_gumbel -->
<!-- signatures: pdf_gumbel(x, a, b) -->
### Function: pdf_gumbel (x, a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の密度函数の*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_hypergeometric -->
<!-- signatures: pdf_hypergeometric(x, n1, n2, n) -->
### Function: pdf_hypergeometric (x, n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
確率函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_laplace -->
<!-- signatures: pdf_laplace(x, a, b) -->
### Function: pdf_laplace (x, a, b)

$b>0$で、 $Laplace(a,b)$確率変数の密度函数の
*x*での値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_logistic -->
<!-- signatures: pdf_logistic(x, a, b) -->
### Function: pdf_logistic (x, a, b)

$b>0$で、 $Logistic(a,b)$確率変数の
密度函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_lognormal -->
<!-- signatures: pdf_lognormal(x, m, s) -->
### Function: pdf_lognormal (x, m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
密度函数の
*x*での値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_negative_binomial -->
<!-- signatures: pdf_negative_binomial(x, n, p) -->
### Function: pdf_negative_binomial (x, n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の確率函数の
*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_noncentral_chi2 -->
<!-- signatures: pdf_noncentral_chi2(x, n, ncp) -->
### Function: pdf_noncentral_chi2 (x, n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
密度函数の
*x*での値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_noncentral_student_t -->
<!-- signatures: pdf_noncentral_student_t(x, n, ncp) -->
### Function: pdf_noncentral_student_t (x, n, ncp)

$n>0$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の密度函数の*x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。


時々、最終結果を得るために余分な仕事が必要となります。








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

$s>0$で $Normal(m,s)$(正規)確率変数の密度函数の *x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_pareto -->
<!-- signatures: pdf_pareto(x, a, b) -->
### Function: pdf_pareto (x, a, b)

$a,b>0$で、 $Pareto(a,b)$確率変数の
密度函数の
*x*の値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_poisson -->
<!-- signatures: pdf_poisson(x, m) -->
### Function: pdf_poisson (x, m)

$m>0$で、 $Poisson(m)$確率変数の確率函数の *x*での値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_rayleigh -->
<!-- signatures: pdf_rayleigh(x, b) -->
### Function: pdf_rayleigh (x, b)

$b>0$で、 $Rayleigh(b)$確率変数の
密度函数の
*x*での値を返します。


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull密度に基づいた名詞形を返します。








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

$n>0$自由度のStudent確率変数 $t(n)$の密度函数の *x*での値を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: pdf_weibull -->
<!-- signatures: pdf_weibull(x, a, b) -->
### Function: pdf_weibull (x, a, b)

$a,b>0$で、 $Weibull(a,b)$確率変数の
密度函数の
*x*の値を返します。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_bernoulli -->
<!-- signatures: quantile_bernoulli(q, p) -->
### Function: quantile_bernoulli (q, p)

$0<p<1$で、  $Bernoulli(p)$確率変数の*q*-分位数を返します;
言い換えると、これは `cdf_bernoulli`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_beta -->
<!-- signatures: quantile_beta(q, a, b) -->
### Function: quantile_beta (q, a, b)

$a,b>0$で、 $Beta(a,b)$確率変数の
*q*-分位数を返します;
言い換えると、これは`cdf_beta`の逆函数です。
引数 *q* $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_binomial -->
<!-- signatures: quantile_binomial(q, n, p) -->
### Function: quantile_binomial (q, n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の*q*-分位数を返します;
言い換えれば、これは `cdf_binomial`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_cauchy -->
<!-- signatures: quantile_cauchy(q, a, b) -->
### Function: quantile_cauchy (q, a, b)

$b>0$で、 $Cauchy(a,b)$確率変数の*q*-分位数を返します;
言い換えると、これは `cdf_cauchy`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_chi2 -->
<!-- signatures: quantile_chi2(q, n) -->
### Function: quantile_chi2 (q, n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の *q*-分位数を返します;
言い換えると、これは `cdf_chi2`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。


この函数は閉形式を持たず、
もしグローバル変数`numer`が`true`に等しいか
引数の少なくとも1つが浮動小数点数なら、数値的に計算されます。
そうでなければ、
$Chi^2(n)$確率変数は $Gamma(n/2,2)$と同値なので、
ガンマ分位函数に基づいた名目上の式を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
*q*-分位数を返します。
言い換えると、これは `cdf_continuous_uniform`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_discrete_uniform -->
<!-- signatures: quantile_discrete_uniform(q, n) -->
### Function: quantile_discrete_uniform (q, n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の
*q*-分位数を返します;
言い換えると、これは `cdf_discrete_uniform`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_exp -->
<!-- signatures: quantile_exp(q, m) -->
### Function: quantile_exp (q, m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
*q*-分位数を返します;
言い換えると、これは`cdf_exp`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull分位数に基づいた名詞形を返します。








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

$m,n>0$で、F確率変数 $F(m,n)$の
*q*-分位数を返します;
言い換えると、これは `cdf_f`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。


この関数は閉形式を持たず、
もしグローバル変数 `numer`が `true`に等しいなら、
数値的に計算され、
そうでなければ、名目上の式を返します。








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

$a,b>0$で、 $Gamma(a,b)$確率変数の
*p*-分位数を返します;
言い換えれば、これは `cdf_gamma`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_general_finite_discrete -->
<!-- signatures: quantile_general_finite_discrete(q, v) -->
### Function: quantile_general_finite_discrete (q, v)

ベクトル確率 $v$を持つ
一般有限離散確率変数の
*q*-分位数を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。

<!-- category: Statistics -->
<!-- keywords: quantile_geometric -->
<!-- signatures: quantile_geometric(q, p) -->
### Function: quantile_geometric (q, p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の
*q*-分位数を返します;
言い換えると、これは `cdf_geometric`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_gumbel -->
<!-- signatures: quantile_gumbel(q, a, b) -->
### Function: quantile_gumbel (q, a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の*q*-分位数を返します;
言い換えれば、これは `cdf_gumbel`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_hypergeometric -->
<!-- signatures: quantile_hypergeometric(q, n1, n2, n) -->
### Function: quantile_hypergeometric (q, n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
*q*-分位数を返します。
言い換えると、これは `cdf_hypergeometric`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_laplace -->
<!-- signatures: quantile_laplace(q, a, b) -->
### Function: quantile_laplace (q, a, b)

$b>0$で、 $Laplace(a,b)$確率変数の*q*-分位数を返します;
言い換えれば、これは `cdf_laplace`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_logistic -->
<!-- signatures: quantile_logistic(q, a, b) -->
### Function: quantile_logistic (q, a, b)

$b>0$で、 $Logistic(a,b)$確率変数の
*q*-分位数を返します。
言い換えると、これは `cdf_logistic`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_lognormal -->
<!-- signatures: quantile_lognormal(q, m, s) -->
### Function: quantile_lognormal (q, m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
*q*-分位数を返します;
言い換えると、これは `cdf_lognormal`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。








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

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の
*q*-分位数を返します;
言い換えると、これは `cdf_negative_binomial`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_noncentral_chi2 -->
<!-- signatures: quantile_noncentral_chi2(q, n, ncp) -->
### Function: quantile_noncentral_chi2 (q, n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
*q*-分位数を返します;
言い換えると、これは `cdf_noncentral_chi2`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。


この関数は閉形式を持たず、
もしグローバル変数 `numer`が `true`に等しいなら、
数値的に計算され、
そうでなければ、名目上の式を返します。

<!-- category: Statistics -->
<!-- keywords: quantile_noncentral_student_t -->
<!-- signatures: quantile_noncentral_student_t(q, n, ncp) -->
### Function: quantile_noncentral_student_t (q, n, ncp)

$n>0$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の*q*-分位数を返します。
言い換えると、これは `cdf_noncentral_student_t`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_normal -->
<!-- signatures: quantile_normal(q, m, s) -->
### Function: quantile_normal (q, m, s)

$s>0$で $Normal(m,s)$(正規)確率変数の *q*分位数を返します。
言い換えると、これは `cdf_normal`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。








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

$a,b>0$で、 $Pareto(a,b)$確率変数の
*q*-分位数を返します;
言い換えると、これは `cdf_pareto`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_poisson -->
<!-- signatures: quantile_poisson(q, m) -->
### Function: quantile_poisson (q, m)

$m>0$で、 $Poisson(m)$確率変数の *q*-分位数を返します;
言い換えると、これは `cdf_poisson`の逆函数です。
引数 *q*は $[0,1]$の要素でなればいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_rayleigh -->
<!-- signatures: quantile_rayleigh(q, b) -->
### Function: quantile_rayleigh (q, b)

Returns the *q*-quantile of a $Rayleigh(b)$ random variable, with $b>0$; in other words, this is the inverse of `cdf_rayleigh`. Argument *q* must be an element of $[0,1]$.


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull分位数に基づいた名詞形を返します。








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

$n>0$自由度のStudent確率変数 $t(n)$の *q*-分位数を返します。
言い換えると、これは `cdf_student_t`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: quantile_weibull -->
<!-- signatures: quantile_weibull(q, a, b) -->
### Function: quantile_weibull (q, a, b)

$a,b>0$で、 $Weibull(a,b)$確率変数の
*q*-分位数を返します;
言い換えれば、これは `cdf_weibull`の逆函数です。
引数 *q*は $[0,1]$の要素でなければいけません。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_bernoulli -->
<!-- signatures: random_bernoulli(p), random_bernoulli(p, n) -->
### Function: random_bernoulli (p)

$0<p<1$で、 $Bernoulli(p)$確率変量を返します。
二番目の引数 *n*とともに`random_bernoulli`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


これは `random`組み込みMaxima関数の直接の応用です。


`random`も参照してください。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_beta -->
<!-- signatures: random_beta(a, b), random_beta(a, b, n) -->
### Function: random_beta (a, b)

$a,b>0$で、 $Beta(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_gamma`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは
Cheng, R.C.H.  (1978). *Generating Beta Variates with Nonintegral Shape Parameters*. Communications of the ACM, 21:317-322
に定義されています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_binomial -->
<!-- signatures: random_binomial(n, p), random_binomial(n, p, m) -->
### Function: random_binomial (n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変量を返します。
三番目の引数 *m*とともに`random_binomial`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


実装アルゴリズムは
Kachitvichyanukul, V. and Schmeiser, B.W. (1988) *Binomial Random Variate Generation*. Communications of the ACM, 31, Feb., 216.に
記載されているものに基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_cauchy -->
<!-- signatures: random_cauchy(a, b), random_cauchy(a, b, n) -->
### Function: random_cauchy (a, b)

$b>0$で、 $Cauchy(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_cauchy`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_chi2 -->
<!-- signatures: random_chi2(n), random_chi2(n, m) -->
### Function: random_chi2 (n)

$n>0$で、カイ二乗確率変量 $Chi^2(n)$を返します。
二番目の引数 *m*とともに`random_chi2`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


シミュレーションはAhrens-Chengアルゴリズムに基づきます。
詳細は`random_gamma`を参照してください。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_continuous_uniform -->
<!-- signatures: random_continuous_uniform(a, b), random_continuous_uniform(a, b, n) -->
### Function: random_continuous_uniform (a, b)

$a<b$で、
$Continuous Uniform(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_gamma`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


これは `random`組み込みMaxima関数の直接の応用です。


`random`も参照してください。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_discrete_uniform -->
<!-- signatures: random_discrete_uniform(n), random_discrete_uniform(n, m) -->
### Function: random_discrete_uniform (n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変量を返します。
二番目の引数 *m*とともに`random_discrete_unform`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


これは `random`組み込みMaxima関数の直接の応用です。


`random`も参照してください。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_exp -->
<!-- signatures: random_exp(m), random_exp(m, k) -->
### Function: random_exp (m)

$m>0$で、 $Exponential(m)$(指数)確率変量を返します。
二番目の引数 *k*とともに`random_exp`をコールすると、
サイズ *k*のランダムな標本がシミュレートされます。


シミュレーションアルゴリズムは一般逆函数法です。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_f -->
<!-- signatures: random_f(m, n), random_f(m, n, k) -->
### Function: random_f (m, n)

$m,n>8$で、F確率変量 $F(m,n)$を返します。
三番目の引数 *k*とともに`random_f`をコールすると、
サイズ *k*のランダムな標本がシミュレートされます。


シミュレーションアルゴリズムは、
もし *X*が $Chi^2(m)$確率変数で $Y$が $Chi^2(n)$確率変数なら


```maxima
n X
                    F = ---
                        m Y
```


$$
F={{n X}\over{m Y}}
$$

は *m*と *n*自由度を持つ F確率変数 $F(m,n)$である
という事実に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_gamma -->
<!-- signatures: random_gamma(a, b), random_gamma(a, b, n) -->
### Function: random_gamma (a, b)

$a,b>0$で、 $Gamma(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_gamma`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムはパラメータ *a*の値に依存して、2つの手続きの組み合わせです:


$a>=1$に対して, Cheng, R.C.H. and Feast, G.M. (1979). *Some simple gamma variate generators*. Appl. Stat., 28, 3, 290-295.


$0<a<1$に対して, Ahrens, J.H. and Dieter, U. (1974). *Computer methods for sampling from gamma, beta, poisson and binomial cdf_tributions*. Computing, 12, 223-246.


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_general_finite_discrete -->
<!-- signatures: random_general_finite_discrete(v), random_general_finite_discrete(v, m) -->
### Function: random_general_finite_discrete (v)

ベクトル確率 $v$を持つ
一般有限離散確率変量を返します。
二番目の引数 *m*とともに`random_general_finite_discrete`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。








```maxima
(%i1) load ("distrib")$
(%i2) random_general_finite_discrete([1,3,1,5]);
(%o2)                          4
(%i3) random_general_finite_discrete([1,3,1,5], 10);
(%o3)           [4, 2, 2, 3, 2, 4, 4, 1, 2, 2]
```

<!-- category: Statistics -->
<!-- keywords: random_geometric -->
<!-- signatures: random_geometric(p), random_geometric(p, n) -->
### Function: random_geometric (p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変量を返します。
二番目の引数 *n*とともに`random_geometric`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_gumbel -->
<!-- signatures: random_gumbel(a, b), random_gumbel(a, b, n) -->
### Function: random_gumbel (a, b)

$b>0$で、 $Gumbel(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_gumbel`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_hypergeometric -->
<!-- signatures: random_hypergeometric(n1, n2, n), random_hypergeometric(n1, n2, n, m) -->
### Function: random_hypergeometric (n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変量を返します。
四番目の引数 *m*とともに`random_hypergeometric`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


Kachitvichyanukul, V., Schmeiser, B.W. (1985) *Computer generation of hypergeometric random variates.* Journal of Statistical Computation and Simulation 22, 127-145.に記述されたアルゴリズム。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_laplace -->
<!-- signatures: random_laplace(a, b), random_laplace(a, b, n) -->
### Function: random_laplace (a, b)

$b>0$で、 $Laplace(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_laplace`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_logistic -->
<!-- signatures: random_logistic(a, b), random_logistic(a, b, n) -->
### Function: random_logistic (a, b)

$b>0$で、 $Logistic(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_logistic`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_lognormal -->
<!-- signatures: random_lognormal(m, s), random_lognormal(m, s, n) -->
### Function: random_lognormal (m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変量を返します。
三番目の引数 *n*とともに`random_lognormal`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


対数世紀変量は確率正規変量の平均によってシミュレートされます。
詳細は `random_normal`を見てください。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_negative_binomial -->
<!-- signatures: random_negative_binomial(n, p), random_negative_binomial(n, p, m) -->
### Function: random_negative_binomial (n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変量を返します。
三番目の引数 *m*とともに`random_negative_binomial`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


Devroye, L. (1986) *Non-Uniform Random Variate Generation*. Springer Verlag, p. 480.に記載されたアルゴリズム。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_noncentral_chi2 -->
<!-- signatures: random_noncentral_chi2(n, ncp), random_noncentral_chi2(n, ncp, m) -->
### Function: random_noncentral_chi2 (n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変量 $nc_Chi^2(n,ncp)$を返します。
三番目の引数 *m*とともに`random_noncentral_chi2`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_noncentral_student_t -->
<!-- signatures: random_noncentral_student_t(n, ncp), random_noncentral_student_t(n, ncp, m) -->
### Function: random_noncentral_student_t (n, ncp)

$n>0$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変量 $nc_t(n,ncp)$を返します。
三番目の引数 *m*とともに`random_noncentral_student_t`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


もし *X*が正規確率変数 $N(ncp,1)$で、 
$S^2$が*n*自由度のカイ二乗確率変数 $Chi^2(n)$なら、


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

は *n*自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$であるという事実に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_normal -->
<!-- signatures: random_normal(m, s), random_normal(m, s, n) -->
### Function: random_normal (m, s)

$s>0$で $Normal(m,s)$(正規)確率変量を返します。
三番目の引数 *n*とともに`random_normal`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


これはBox-Muellerアルゴリズムの実装です。
Knuth, D.E. (1981) *Seminumerical Algorithms. The Art of Computer Programming.* Addison-Wesleyに記載されています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_pareto -->
<!-- signatures: random_pareto(a, b), random_pareto(a, b, n) -->
### Function: random_pareto (a, b)

$a>2,b>0$で、 $Pareto(a,b)$確率変量を返します。
三番目の引数 *n*とともに`random_pareto`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_poisson -->
<!-- signatures: random_poisson(m), random_poisson(m, n) -->
### Function: random_poisson (m)

$m>0$で、 $Poisson(m)$確率変量を返します。
二番目の引数 *n*とともに`random_binomial`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは
Ahrens, J.H. and Dieter, U. (1982) *Computer Generation of Poisson Deviates From Modified Normal Distributions*. ACM Trans. Math. Software, 8, 2, June,163-179.に記述されたものです。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_rayleigh -->
<!-- signatures: random_rayleigh(b), random_rayleigh(b, n) -->
### Function: random_rayleigh (b)

$b>0$で、 $Rayleigh(b)$確率変量を返します。
二番目の引数 *n*とともに`random_pareto`をコールすると、
サイズ *n*のランダムな標本がシミュレートされます。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_student_t -->
<!-- signatures: random_student_t(n), random_student_t(n, m) -->
### Function: random_student_t (n)

$n>0$自由度のStudent確率変量 $t(n)$を返します。
三番目の引数 *m*とともに`random_student_t`をコールすると、
サイズ *m*のランダムな標本がシミュレートされます。


実装アルゴリズムは、
もし *Z*が正規確率変数 $N(0,1)$で、 
$S^2$が*n*自由度のカイ二乗確率変数 $Chi^2(n)$なら、


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

は *n*自由度のStudent確率変数 $t(n)$であるという事実に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: random_weibull -->
<!-- signatures: random_weibull(a, b), random_weibull(a, b, n) -->
### Function: random_weibull (a, b)

$a,b>0$で、 $Weibull(a,b)$確率変量を返します。


実装アルゴリズムは一般逆函数法に基づいています。


この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_bernoulli -->
<!-- signatures: skewness_bernoulli(p) -->
### Function: skewness_bernoulli (p)

$0<p<1$で、  $Bernoulli(p)$確率変数の歪度係数を返します。


$Bernoulli(p)$確率変数は $Binomial(1,p)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
二項歪度係数に基づいた名詞形を返します。








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

$a,b>0$で、 $Beta(a,b)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_binomial -->
<!-- signatures: skewness_binomial(n, p) -->
### Function: skewness_binomial (n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_chi2 -->
<!-- signatures: skewness_chi2(n) -->
### Function: skewness_chi2 (n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の歪度係数を返します。


$Chi^2(n)$確率変数は
$Gamma(n/2,2)$に同値なので、
Maximaが結果を得るのに充分な情報を持たない時には、
ガンマ歪度係数に基づいた名詞形を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_discrete_uniform -->
<!-- signatures: skewness_discrete_uniform(n) -->
### Function: skewness_discrete_uniform (n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_exp -->
<!-- signatures: skewness_exp(m) -->
### Function: skewness_exp (m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
歪度係数を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull歪度係数に基づいた名詞形を返します。








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

$m,n>6$で、F確率変数 $F(m,n)$の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_gamma -->
<!-- signatures: skewness_gamma(a, b) -->
### Function: skewness_gamma (a, b)

$a,b>0$で、 $Gamma(a,b)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_general_finite_discrete -->
<!-- signatures: skewness_general_finite_discrete(v) -->
### Function: skewness_general_finite_discrete (v)

ベクトル確率 $v$を持つ
一般有限離散確率変数の
歪度係数を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。

<!-- category: Statistics -->
<!-- keywords: skewness_geometric -->
<!-- signatures: skewness_geometric(p) -->
### Function: skewness_geometric (p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_gumbel -->
<!-- signatures: skewness_gumbel(a, b) -->
### Function: skewness_gumbel (a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の歪度係数を返します。








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

ここで、`zeta`はRiemannのゼータ函数を表します。

<!-- category: Statistics -->
<!-- keywords: skewness_hypergeometric -->
<!-- signatures: skewness_hypergeometric(n1, n2, n) -->
### Function: skewness_hypergeometric (n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_laplace -->
<!-- signatures: skewness_laplace(a, b) -->
### Function: skewness_laplace (a, b)

$b>0$で、 $Laplace(a,b)$確率変数の歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_logistic -->
<!-- signatures: skewness_logistic(a, b) -->
### Function: skewness_logistic (a, b)

$b>0$で、 $Logistic(a,b)$確率変数の歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_lognormal -->
<!-- signatures: skewness_lognormal(m, s) -->
### Function: skewness_lognormal (m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_negative_binomial -->
<!-- signatures: skewness_negative_binomial(n, p) -->
### Function: skewness_negative_binomial (n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_noncentral_chi2 -->
<!-- signatures: skewness_noncentral_chi2(n, ncp) -->
### Function: skewness_noncentral_chi2 (n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
歪度係数を返します。

<!-- category: Statistics -->
<!-- keywords: skewness_noncentral_student_t -->
<!-- signatures: skewness_noncentral_student_t(n, ncp) -->
### Function: skewness_noncentral_student_t (n, ncp)

$n>3$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_normal -->
<!-- signatures: skewness_normal(m, s) -->
### Function: skewness_normal (m, s)

$s>0$で $Normal(m,s)$(正規)確率変数の歪度を返します。それは常に0に等しいです。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_pareto -->
<!-- signatures: skewness_pareto(a, b) -->
### Function: skewness_pareto (a, b)

$a>2,b>0$で、 $Pareto(a,b)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_poisson -->
<!-- signatures: skewness_poisson(m) -->
### Function: skewness_poisson (m)

$m>0$で、 $Poisson(m)$確率変数の歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_rayleigh -->
<!-- signatures: skewness_rayleigh(b) -->
### Function: skewness_rayleigh (b)

$b>0$で、 $Rayleigh(b)$確率変数の歪度係数を返します。


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull歪度係数に基づいた名詞形を返します。








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

$n>3$自由度のStudent確率変数 $t(n)$の歪度係数を返します。
それはいつも0に等しいです。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: skewness_weibull -->
<!-- signatures: skewness_weibull(a, b) -->
### Function: skewness_weibull (a, b)

$a,b>0$で、 $Weibull(a,b)$確率変数の
歪度係数を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_bernoulli -->
<!-- signatures: std_bernoulli(p) -->
### Function: std_bernoulli (p)

$0<p<1$で、  $Bernoulli(p)$確率変数の標準偏差を返します。


$Bernoulli(p)$確率変数は $Binomial(1,p)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
二項標準偏差に基づいた名詞形を返します。








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

$a,b>0$で、 $Beta(a,b)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_binomial -->
<!-- signatures: std_binomial(n, p) -->
### Function: std_binomial (n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_chi2 -->
<!-- signatures: std_chi2(n) -->
### Function: std_chi2 (n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の標準偏差を返します。


$Chi^2(n)$確率変数は
$Gamma(n/2,2)$に同値なので、
Maximaが結果を得るのに充分な情報を持たない時には、
ガンマ標準偏差に基づいた名詞形を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_discrete_uniform -->
<!-- signatures: std_discrete_uniform(n) -->
### Function: std_discrete_uniform (n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_exp -->
<!-- signatures: std_exp(m) -->
### Function: std_exp (m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
標準偏差を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull標準偏差に基づいた名詞形を返します。








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

$m,n>4$で、F確率変数 $F(m,n)$の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_gamma -->
<!-- signatures: std_gamma(a, b) -->
### Function: std_gamma (a, b)

$a,b>0$で、 $Gamma(a,b)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_general_finite_discrete -->
<!-- signatures: std_general_finite_discrete(v) -->
### Function: std_general_finite_discrete (v)

ベクトル確率 $v$を持つ
一般有限離散確率変数の
標準偏差を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。

<!-- category: Statistics -->
<!-- keywords: std_geometric -->
<!-- signatures: std_geometric(p) -->
### Function: std_geometric (p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_gumbel -->
<!-- signatures: std_gumbel(a, b) -->
### Function: std_gumbel (a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_hypergeometric -->
<!-- signatures: std_hypergeometric(n1, n2, n) -->
### Function: std_hypergeometric (n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_laplace -->
<!-- signatures: std_laplace(a, b) -->
### Function: std_laplace (a, b)

$b>0$で、 $Laplace(a,b)$確率変数の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_logistic -->
<!-- signatures: std_logistic(a, b) -->
### Function: std_logistic (a, b)

$b>0$で、 $Logistic(a,b)$確率変数の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_lognormal -->
<!-- signatures: std_lognormal(m, s) -->
### Function: std_lognormal (m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_negative_binomial -->
<!-- signatures: std_negative_binomial(n, p) -->
### Function: std_negative_binomial (n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_noncentral_chi2 -->
<!-- signatures: std_noncentral_chi2(n, ncp) -->
### Function: std_noncentral_chi2 (n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
標準偏差を返します。

<!-- category: Statistics -->
<!-- keywords: std_noncentral_student_t -->
<!-- signatures: std_noncentral_student_t(n, ncp) -->
### Function: std_noncentral_student_t (n, ncp)

$n>2$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_normal -->
<!-- signatures: std_normal(m, s) -->
### Function: std_normal (m, s)

$s>0$で $Normal(m,s)$(正規)確率変数の分散、すなわち *s*を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_pareto -->
<!-- signatures: std_pareto(a, b) -->
### Function: std_pareto (a, b)

$a>2,b>0$で、 $Pareto(a,b)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_poisson -->
<!-- signatures: std_poisson(m) -->
### Function: std_poisson (m)

$m>0$で、 $Poisson(m)$確率変数の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_rayleigh -->
<!-- signatures: std_rayleigh(b) -->
### Function: std_rayleigh (b)

$b>0$で、 $Rayleigh(b)$確率変数の標準偏差を返します。


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull標準偏差に基づいた名詞形を返します。








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

$n>2$自由度のStudent確率変数 $t(n)$の標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: std_weibull -->
<!-- signatures: std_weibull(a, b) -->
### Function: std_weibull (a, b)

$a,b>0$で、 $Weibull(a,b)$確率変数の
標準偏差を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_bernoulli -->
<!-- signatures: var_bernoulli(p) -->
### Function: var_bernoulli (p)

$0<p<1$で、  $Bernoulli(p)$確率変数の分散を返します。


$Bernoulli(p)$確率変数は $Binomial(1,p)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
二項分散に基づいた名詞形を返します。








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

$a,b>0$で、 $Beta(a,b)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_binomial -->
<!-- signatures: var_binomial(n, p) -->
### Function: var_binomial (n, p)

$0<p<1$かつ $n$は正の整数で、
$Binomial(n,p)$確率変数の分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_chi2 -->
<!-- signatures: var_chi2(n) -->
### Function: var_chi2 (n)

$n>0$で、カイ二乗確率変数 $Chi^2(n)$の分散を返します。


$Chi^2(n)$確率変数は
$Gamma(n/2,2)$に同値なので、
Maximaが結果を得るのに充分な情報を持たない時には、
ガンマ分散に基づいた名詞形を返します。








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

$a<b$で、
$Continuous Uniform(a,b)$確率変数の分布函数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_discrete_uniform -->
<!-- signatures: var_discrete_uniform(n) -->
### Function: var_discrete_uniform (n)

$n$が厳密に正の整数で、 $Discrete Uniform(n)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_exp -->
<!-- signatures: var_exp(m) -->
### Function: var_exp (m)

$m>0$で、 $Exponential(m)$(指数)確率変数の
分散を返します。


$Exponential(m)$(指数)確率変数は
 $Weibull(1,1/m)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull分散に基づいた名詞形を返します。








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

$m,n>4$で、F確率変数 $F(m,n)$の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_gamma -->
<!-- signatures: var_gamma(a, b) -->
### Function: var_gamma (a, b)

$a,b>0$で、 $Gamma(a,b)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_general_finite_discrete -->
<!-- signatures: var_general_finite_discrete(v) -->
### Function: var_general_finite_discrete (v)

ベクトル確率 $v$を持つ
一般有限離散確率変数の
分散を返します。


さらなる詳細は `pdf_general_finite_discrete`を参照してください。

<!-- category: Statistics -->
<!-- keywords: var_geometric -->
<!-- signatures: var_geometric(p) -->
### Function: var_geometric (p)

$0<p<1$で、
$Geometric(p)$(幾何)確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_gumbel -->
<!-- signatures: var_gumbel(a, b) -->
### Function: var_gumbel (a, b)

$b>0$で、 $Gumbel(a,b)$確率変数の分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_hypergeometric -->
<!-- signatures: var_hypergeometric(n1, n2, n) -->
### Function: var_hypergeometric (n1, n2, n)

*n1*, *n2*, *n*が非負整数でかつ $n<=n1+n2$で、
$Hypergeometric(n1,n2,n)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_laplace -->
<!-- signatures: var_laplace(a, b) -->
### Function: var_laplace (a, b)

$b>0$で、 $Laplace(a,b)$確率変数の分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_logistic -->
<!-- signatures: var_logistic(a, b) -->
### Function: var_logistic (a, b)

$b>0$で、 $Logistic(a,b)$確率変数の分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_lognormal -->
<!-- signatures: var_lognormal(m, s) -->
### Function: var_lognormal (m, s)

$s>0$で、$Lognormal(m,s)$(対数正規)確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_negative_binomial -->
<!-- signatures: var_negative_binomial(n, p) -->
### Function: var_negative_binomial (n, p)

$0<p<1$かつ $n$が正の整数で、
$Negative Binomial(n,p)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_noncentral_chi2 -->
<!-- signatures: var_noncentral_chi2(n, ncp) -->
### Function: var_noncentral_chi2 (n, ncp)

$n>0$と非中心度パラメータ $ncp>=0$を持つ
非中心カイ二乗確率変数 $nc_Chi^2(n,ncp)$の
分散を返します。

<!-- category: Statistics -->
<!-- keywords: var_noncentral_student_t -->
<!-- signatures: var_noncentral_student_t(n, ncp) -->
### Function: var_noncentral_student_t (n, ncp)

$n>2$自由度で非中心度パラメータ $ncp$を持つ
非中心Student確率変数 $nc_t(n,ncp)$の分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_normal -->
<!-- signatures: var_normal(m, s) -->
### Function: var_normal (m, s)

$s>0$で $Normal(m,s)$(正規)確率変数の分散、すなわち *s^2*を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_pareto -->
<!-- signatures: var_pareto(a, b) -->
### Function: var_pareto (a, b)

$a>2,b>0$で、 $Pareto(a,b)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_poisson -->
<!-- signatures: var_poisson(m) -->
### Function: var_poisson (m)

$m>0$で、 $Poisson(m)$確率変数の分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

<!-- category: Statistics -->
<!-- keywords: var_rayleigh -->
<!-- signatures: var_rayleigh(b) -->
### Function: var_rayleigh (b)

$b>0$で、 $Rayleigh(b)$確率変数の分散を返します。


$Rayleigh(b)$確率変数は $Weibull(2,1/b)$と同値です。
なので、
Maximaが結果を得るのに十分な情報を持たない時は、
Weibull分散に基づいた名詞形を返します。








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

$n>2$自由度のStudent確率変数 $t(n)$の分散を返します。







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

$a,b>0$で、 $Weibull(a,b)$確率変数の
分散を返します。
この関数を利用するには、初めに `load("distrib")`を書いてください。

