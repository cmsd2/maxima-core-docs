## distrib

<!-- category: Statistics -->
<!-- keywords: cdf_bernoulli -->
<!-- signatures: cdf_bernoulli(x, p) -->
### Function: cdf_bernoulli (x, p)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_beta -->
<!-- signatures: cdf_beta(x, a, b) -->
### Function: cdf_beta (x, a, b)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Beta*$(a,b)$, con $a,b>0$.








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo.








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Cauchy*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_chi2 -->
<!-- signatures: cdf_chi2(x, n) -->
### Function: cdf_chi2 (x, n)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria chi-cuadrado $Chi^2(n)$, con $n>0$.








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_discrete_uniform -->
<!-- signatures: cdf_discrete_uniform(x, n) -->
### Function: cdf_discrete_uniform (x, n)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_exp -->
<!-- signatures: cdf_exp(x, m) -->
### Function: cdf_exp (x, m)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) cdf_exp(x,m);
                                 - m x
(%o2)                      1 - %e
```

<!-- category: Statistics -->
<!-- keywords: cdf_f -->
<!-- signatures: cdf_f(x, m, n) -->
### Function: cdf_f (x, m, n)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria  *F*$(m,n)$, con $m,n>0$.








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. 








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.









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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_gumbel -->
<!-- signatures: cdf_gumbel(x, a, b) -->
### Function: cdf_gumbel (x, a, b)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_hypergeometric -->
<!-- signatures: cdf_hypergeometric(x, n1, n2, n) -->
### Function: cdf_hypergeometric (x, n1, n2, n)

Devuelve el valor correspondiente a *x* de la función de distribución of una variable 
aleatoria *Hipergeométrica*$(n1,n2,n)$, con *n1*, *n2* y *n* enteros 
positivos y $n<=n1+n2$. Véase `pdf_hypergeometric` para una descripción más completa.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_laplace -->
<!-- signatures: cdf_laplace(x, a, b) -->
### Function: cdf_laplace (x, a, b)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_logistic -->
<!-- signatures: cdf_logistic(x, a, b) -->
### Function: cdf_logistic (x, a, b)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_lognormal -->
<!-- signatures: cdf_lognormal(x, m, s) -->
### Function: cdf_lognormal (x, m, s)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Lognormal*$(m,s)$, con $s>0$.   Esta función se define en términos de la función de error, `erf`, de Maxima.







```maxima
(%i1) load ("distrib")$
(%i2) assume(x>0, s>0)$  cdf_lognormal(x,m,s);

                           log(x) - m
                       erf(----------)
                           sqrt(2) s     1
(%o2)                  --------------- + -
                              2          2
```


Véase también `erf`.

<!-- category: Statistics -->
<!-- keywords: cdf_negative_binomial -->
<!-- signatures: cdf_negative_binomial(x, n, p) -->
### Function: cdf_negative_binomial (x, n, p)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ y $n$ positivo.







```maxima
(%i1) load ("distrib")$
(%i2) cdf_negative_binomial(3,4,1/8);
                            3271
(%o2)                      ------
                           524288
```

<!-- category: Statistics -->
<!-- keywords: cdf_noncentral_chi2 -->
<!-- signatures: cdf_noncentral_chi2(x, n, ncp) -->
### Function: cdf_noncentral_chi2 (x, n, ncp)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria chi-cuadrado no centrada $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: cdf_noncentral_student_t -->
<!-- signatures: cdf_noncentral_student_t(x, n, ncp) -->
### Function: cdf_noncentral_student_t (x, n, ncp)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>0$ grados de libertad y parámetro de no centralidad $ncp$. Esta función no tiene expresión compacta y se calcula numéricamente. Para hacer uso de esta función, ejecútese primero `load("distrib")`.







```maxima
(%i1) load ("distrib")$
(%i2) cdf_noncentral_student_t(-2,5,-5);
(%o2)          .9952030093319743
```

<!-- category: Statistics -->
<!-- keywords: cdf_normal -->
<!-- signatures: cdf_normal(x, m, s) -->
### Function: cdf_normal (x, m, s)

Devuelve el valor correspondiente a *x* de la función de distribución de la variable aleatoria *Normal*$(m,s)$, con $s>0$. Esta función se define en términos de la función de error,  `erf`, de Maxima.







```maxima
(%i1) load ("distrib")$
(%i2) cdf_normal(x,m,s);
                                    x - m
                              erf(---------)
                                  sqrt(2) s    1
(%o2)                         -------------- + -
                                    2          2
```


Véase también `erf`.

<!-- category: Statistics -->
<!-- keywords: cdf_pareto -->
<!-- signatures: cdf_pareto(x, a, b) -->
### Function: cdf_pareto (x, a, b)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Pareto*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_poisson -->
<!-- signatures: cdf_poisson(x, m) -->
### Function: cdf_poisson (x, m)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Poisson*$(m)$, con $m>0$.








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







```maxima
(%i1) load ("distrib")$
(%i2) cdf_rayleigh(x,b);
                                   2  2
                                - b  x
(%o2)                     1 - %e
```

<!-- category: Statistics -->
<!-- keywords: cdf_student_t -->
<!-- signatures: cdf_student_t(x, n) -->
### Function: cdf_student_t (x, n)

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de Student $t(n)$, con $n>0$.








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

Devuelve el valor correspondiente a *x* de la función de distribución de una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_bernoulli -->
<!-- signatures: kurtosis_bernoulli(p) -->
### Function: kurtosis_bernoulli (p)

Devuelve el coeficiente de curtosis una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$.


La variable aleatoria *Bernoulli*$(p)$ equivale a una *Binomial*$(1,p)$.







```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_bernoulli(p);
                         1 - 6 (1 - p) p
(%o2)                    ---------------
                            (1 - p) p
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_beta -->
<!-- signatures: kurtosis_beta(a, b) -->
### Function: kurtosis_beta (a, b)

Devuelve el coeficiente de curtosis de una variable aleatoria *Beta*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_binomial -->
<!-- signatures: kurtosis_binomial(n, p) -->
### Function: kurtosis_binomial (n, p)

Devuelve el coeficiente de curtosis de una variable aleatoria binomial  *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_chi2 -->
<!-- signatures: kurtosis_chi2(n) -->
### Function: kurtosis_chi2 (n)

Devuelve el coeficiente de curtosis una variable aleatoria  $Chi^2(n)$, con $n>0$.


La variable aleatoria $Chi^2(n)$ equivale a una *Gamma*$(n/2,2)$.







```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_chi2(n);
                               12
(%o2)                          --
                               n
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_continuous_uniform -->
<!-- signatures: kurtosis_continuous_uniform(a, b) -->
### Function: kurtosis_continuous_uniform (a, b)

Devuelve el coeficiente de curtosis una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_discrete_uniform -->
<!-- signatures: kurtosis_discrete_uniform(n) -->
### Function: kurtosis_discrete_uniform (n)

Devuelve el coeficiente de curtosis de una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_exp -->
<!-- signatures: kurtosis_exp(m) -->
### Function: kurtosis_exp (m)

Devuelve el coeficiente de curtosis una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) kurtosis_exp(m);
(%o3)                           6
```

<!-- category: Statistics -->
<!-- keywords: kurtosis_f -->
<!-- signatures: kurtosis_f(m, n) -->
### Function: kurtosis_f (m, n)

Devuelve el coeficiente de curtosis una variable aleatoria  *F*$(m,n)$, con $m>0, n>8$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_gamma -->
<!-- signatures: kurtosis_gamma(a, b) -->
### Function: kurtosis_gamma (a, b)

Devuelve el coeficiente de curtosis una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_general_finite_discrete -->
<!-- signatures: kurtosis_general_finite_discrete(v) -->
### Function: kurtosis_general_finite_discrete (v)

Devuelve el coeficiente de curtosis de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.

<!-- category: Statistics -->
<!-- keywords: kurtosis_geometric -->
<!-- signatures: kurtosis_geometric(p) -->
### Function: kurtosis_geometric (p)

Devuelve el coeficiente de curtosis de una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_gumbel -->
<!-- signatures: kurtosis_gumbel(a, b) -->
### Function: kurtosis_gumbel (a, b)

Devuelve el coeficiente de curtosis de una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_laplace -->
<!-- signatures: kurtosis_laplace(a, b) -->
### Function: kurtosis_laplace (a, b)

Devuelve el coeficiente de curtosis una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_logistic -->
<!-- signatures: kurtosis_logistic(a, b) -->
### Function: kurtosis_logistic (a, b)

Devuelve el coeficiente de curtosis una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_lognormal -->
<!-- signatures: kurtosis_lognormal(m, s) -->
### Function: kurtosis_lognormal (m, s)

Devuelve el coeficiente de curtosis una variable aleatoria *Lognormal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_negative_binomial -->
<!-- signatures: kurtosis_negative_binomial(n, p) -->
### Function: kurtosis_negative_binomial (n, p)

Devuelve el coeficiente de curtosis una variable aleatoria binomial negativa  $NB(n,p)$, con $0 < p \leq 1$ and $n$ positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_noncentral_chi2 -->
<!-- signatures: kurtosis_noncentral_chi2(n, ncp) -->
### Function: kurtosis_noncentral_chi2 (n, ncp)

Devuelve el coeficiente de curtosis una variable aleatoria chi-cuadrado no centrada $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: kurtosis_noncentral_student_t -->
<!-- signatures: kurtosis_noncentral_student_t(n, ncp) -->
### Function: kurtosis_noncentral_student_t (n, ncp)

Devuelve el coeficiente de curtosis de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>4$ grados de libertad y parámetro de no centralidad $ncp$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_normal -->
<!-- signatures: kurtosis_normal(m, s) -->
### Function: kurtosis_normal (m, s)

Devuelve el coeficiente de curtosis de una variable aleatoria *Normal*$(m,s)$, con $s>0$, que es siempre igual a 0. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_pareto -->
<!-- signatures: kurtosis_pareto(a, b) -->
### Function: kurtosis_pareto (a, b)

Devuelve el coeficiente de curtosis de una variable aleatoria de *Pareto*$(a,b)$, con $a>4,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_poisson -->
<!-- signatures: kurtosis_poisson(m) -->
### Function: kurtosis_poisson (m)

Devuelve el coeficiente de curtosis de una variable aleatoria de *Poisson*$(m)$, con $m>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_rayleigh -->
<!-- signatures: kurtosis_rayleigh(b) -->
### Function: kurtosis_rayleigh (b)

Devuelve el coeficiente de curtosis una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







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

<!-- category: Statistics -->
<!-- keywords: kurtosis_student_t -->
<!-- signatures: kurtosis_student_t(n) -->
### Function: kurtosis_student_t (n)

Devuelve el coeficiente de curtosis una variable aleatoria de Student $t(n)$, con $n>4$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_weibull -->
<!-- signatures: kurtosis_weibull(a, b) -->
### Function: kurtosis_weibull (a, b)

Devuelve el coeficiente de curtosis una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_bernoulli -->
<!-- signatures: mean_bernoulli(p) -->
### Function: mean_bernoulli (p)

Devuelve la media de  una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$.


La variable aleatoria *Bernoulli*$(p)$ equivale a una *Binomial*$(1,p)$.







```maxima
(%i1) load ("distrib")$
(%i2) mean_bernoulli(p);
(%o2)                           p
```

<!-- category: Statistics -->
<!-- keywords: mean_beta -->
<!-- signatures: mean_beta(a, b) -->
### Function: mean_beta (a, b)

Devuelve la media de  una variable aleatoria *Beta*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_binomial -->
<!-- signatures: mean_binomial(n, p) -->
### Function: mean_binomial (n, p)

Devuelve la media de  una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_chi2 -->
<!-- signatures: mean_chi2(n) -->
### Function: mean_chi2 (n)

Devuelve la media de  una variable aleatoria  $Chi^2(n)$, con $n>0$.


La variable aleatoria $Chi^2(n)$ equivale a una *Gamma*$(n/2,2)$.







```maxima
(%i1) load ("distrib")$
(%i2) mean_chi2(n);
(%o2)                           n
```

<!-- category: Statistics -->
<!-- keywords: mean_continuous_uniform -->
<!-- signatures: mean_continuous_uniform(a, b) -->
### Function: mean_continuous_uniform (a, b)

Devuelve la media de  una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_discrete_uniform -->
<!-- signatures: mean_discrete_uniform(n) -->
### Function: mean_discrete_uniform (n)

Devuelve la media de  una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_exp -->
<!-- signatures: mean_exp(m) -->
### Function: mean_exp (m)

Devuelve la media de  una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) mean_exp(m);
                                1
(%o2)                           -
                                m
```

<!-- category: Statistics -->
<!-- keywords: mean_f -->
<!-- signatures: mean_f(m, n) -->
### Function: mean_f (m, n)

Devuelve la media de  una variable aleatoria  *F*$(m,n)$, con $m>0, n>2$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_gamma -->
<!-- signatures: mean_gamma(a, b) -->
### Function: mean_gamma (a, b)

Devuelve la media de  una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_general_finite_discrete -->
<!-- signatures: mean_general_finite_discrete(v) -->
### Function: mean_general_finite_discrete (v)

Devuelve la media de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.

<!-- category: Statistics -->
<!-- keywords: mean_geometric -->
<!-- signatures: mean_geometric(p) -->
### Function: mean_geometric (p)

Devuelve la media de  una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_gumbel -->
<!-- signatures: mean_gumbel(a, b) -->
### Function: mean_gumbel (a, b)

Devuelve la media de  una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$.







```maxima
(%i1) load ("distrib")$
(%i2) mean_gumbel(a,b);
(%o2)                     %gamma b + a
```

donde el símbolo `%gamma` representa la constante de Euler-Mascheroni. Véase también `%gamma`.

<!-- category: Statistics -->
<!-- keywords: mean_hypergeometric -->
<!-- signatures: mean_hypergeometric(n1, n2, n) -->
### Function: mean_hypergeometric (n1, n2, n)

Devuelve la media de  una variable aleatoria uniforme discreta $Hyp(n1,n2,n)$, con *n1*, *n2* y *n* enteros positivos y $n<=n1+n2$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_laplace -->
<!-- signatures: mean_laplace(a, b) -->
### Function: mean_laplace (a, b)

Devuelve la media de  una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_logistic -->
<!-- signatures: mean_logistic(a, b) -->
### Function: mean_logistic (a, b)

Devuelve la media de  una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_lognormal -->
<!-- signatures: mean_lognormal(m, s) -->
### Function: mean_lognormal (m, s)

Devuelve la media de  una variable aleatoria *Lognormal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_negative_binomial -->
<!-- signatures: mean_negative_binomial(n, p) -->
### Function: mean_negative_binomial (n, p)

Devuelve la media de  una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ and $n$ positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_noncentral_chi2 -->
<!-- signatures: mean_noncentral_chi2(n, ncp) -->
### Function: mean_noncentral_chi2 (n, ncp)

Devuelve la media de  una variable aleatoria chi-cuadrado no centrada $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: mean_noncentral_student_t -->
<!-- signatures: mean_noncentral_student_t(n, ncp) -->
### Function: mean_noncentral_student_t (n, ncp)

Devuelve la media de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>1$ grados de libertad y parámetro de no centralidad $ncp$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.







```maxima
(%i1) load ("distrib")$
(%i2) mean_noncentral_student_t(df,k);
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

Devuelve la media de  una variable aleatoria *Normal*$(m,s)$, con $s>0$, es decir *m*. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_pareto -->
<!-- signatures: mean_pareto(a, b) -->
### Function: mean_pareto (a, b)

Devuelve la media de  una variable aleatoria de *Pareto*$(a,b)$, con $a>1,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_poisson -->
<!-- signatures: mean_poisson(m) -->
### Function: mean_poisson (m)

Devuelve la media de una variable aleatoria de *Poisson*$(m)$, con  $m>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_rayleigh -->
<!-- signatures: mean_rayleigh(b) -->
### Function: mean_rayleigh (b)

Devuelve la media de  una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







```maxima
(%i1) load ("distrib")$
(%i2) mean_rayleigh(b);
                            sqrt(%pi)
(%o2)                       ---------
                               2 b
```

<!-- category: Statistics -->
<!-- keywords: mean_student_t -->
<!-- signatures: mean_student_t(n) -->
### Function: mean_student_t (n)

Devuelve la media de una variable aleatoria de Student $t(n)$, con $n>0$, que vale siempre 0. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_weibull -->
<!-- signatures: mean_weibull(a, b) -->
### Function: mean_weibull (a, b)

Devuelve la media de  una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_bernoulli -->
<!-- signatures: pdf_bernoulli(x, p) -->
### Function: pdf_bernoulli (x, p)

Devuelve el valor correspondiente a *x* de la función de probabilidad de una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$.


La variable aleatoria *Bernoulli*$(p)$ equivale a una *Binomial*$(1,p)$.







```maxima
(%i1) load ("distrib")$
(%i2) pdf_bernoulli(1,p);
(%o2)                           p
```

<!-- category: Statistics -->
<!-- keywords: pdf_beta -->
<!-- signatures: pdf_beta(x, a, b) -->
### Function: pdf_beta (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria *Beta*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_binomial -->
<!-- signatures: pdf_binomial(x, n, p) -->
### Function: pdf_binomial (x, n, p)

Devuelve el valor correspondiente a *x* de la función de probabilidad de una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_cauchy -->
<!-- signatures: pdf_cauchy(x, a, b) -->
### Function: pdf_cauchy (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de *Cauchy*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_chi2 -->
<!-- signatures: pdf_chi2(x, n) -->
### Function: pdf_chi2 (x, n)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria chi-cuadrado $Chi^2(n)$, con $n>0$. La variable aleatoria $Chi^2(n)$ equivale a una *Gamma*$(n/2,2)$.







```maxima
(%i1) load ("distrib")$
(%i2) pdf_chi2(x,n);
                         n/2 - 1   - x/2
                        x        %e
(%o2)                   ----------------
                          n/2       n
                         2    gamma(-)
                                    2
```

<!-- category: Statistics -->
<!-- keywords: pdf_continuous_uniform -->
<!-- signatures: pdf_continuous_uniform(x, a, b) -->
### Function: pdf_continuous_uniform (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_discrete_uniform -->
<!-- signatures: pdf_discrete_uniform(x, n) -->
### Function: pdf_discrete_uniform (x, n)

Devuelve el valor correspondiente a *x* de la función de probabilidad de una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_exp -->
<!-- signatures: pdf_exp(x, m) -->
### Function: pdf_exp (x, m)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) pdf_exp(x,m);
                                - m x
(%o2)                       m %e
```

<!-- category: Statistics -->
<!-- keywords: pdf_f -->
<!-- signatures: pdf_f(x, m, n) -->
### Function: pdf_f (x, m, n)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria  *F*$(m,n)$, con $m,n>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_gamma -->
<!-- signatures: pdf_gamma(x, a, b) -->
### Function: pdf_gamma (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_general_finite_discrete -->
<!-- signatures: pdf_general_finite_discrete(x, v) -->
### Function: pdf_general_finite_discrete (x, v)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria general discreta finita, con vector de probabilidades $v$, tal que `Pr(X=i) = v_i`. El vector $v$ puede ser una lista de expresiones no negativas, cuyas componentes se normalizarán para obtener un vector de probabilidades. Para hacer uso de esta función, ejecútese primero `load("distrib")`.








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

Devuelve el valor correspondiente a *x* de la función de probabilidad de una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_gumbel -->
<!-- signatures: pdf_gumbel(x, a, b) -->
### Function: pdf_gumbel (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_hypergeometric -->
<!-- signatures: pdf_hypergeometric(x, n1, n2, n) -->
### Function: pdf_hypergeometric (x, n1, n2, n)

Devuelve el valor correspondiente a *x* de la función de probabilidad de una 
variable aleatoria *Hipergeométrica*$(n1,n2,n)$, con *n1*, *n2* y *n* 
enteros positivos y $n<=n1+n2$. Siendo *n1* el número de objetos de la clase A, 
*n2* el número de objetos de la clase B y *n* el tamaño de una muestra sin 
reemplazo, esta función devuelve la probabilidad del suceso 
"extraer exactamente *x* objetos de la clase A".


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_laplace -->
<!-- signatures: pdf_laplace(x, a, b) -->
### Function: pdf_laplace (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_logistic -->
<!-- signatures: pdf_logistic(x, a, b) -->
### Function: pdf_logistic (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_lognormal -->
<!-- signatures: pdf_lognormal(x, m, s) -->
### Function: pdf_lognormal (x, m, s)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria *Lognormal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_negative_binomial -->
<!-- signatures: pdf_negative_binomial(x, n, p) -->
### Function: pdf_negative_binomial (x, n, p)

Devuelve el valor correspondiente a *x* de la función de probabilidad de una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ y $n$ positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_noncentral_chi2 -->
<!-- signatures: pdf_noncentral_chi2(x, n, ncp) -->
### Function: pdf_noncentral_chi2 (x, n, ncp)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria chi-cuadrado no centrada $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$. Para hacer uso de esta función ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_noncentral_student_t -->
<!-- signatures: pdf_noncentral_student_t(x, n, ncp) -->
### Function: pdf_noncentral_student_t (x, n, ncp)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>0$ grados de libertad y parámetro de no centralidad $ncp$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.


En ocasiones es necesario hacer algún trabajo extra para obtener el resultado final.








```maxima
(%i1) load ("distrib")$
(%i2) expand(pdf_noncentral_student_t(3,5,0.1));
                           7/2                         7/2
      0.04296414417400905 5      1.323650307289301e-6 5
(%o2) ------------------------ + -------------------------
         3/2   5/2                       sqrt(%pi)
        2    14    sqrt(%pi)
                                                        7/2
                                   1.94793720435093e-4 5
                                 + ------------------------
                                             %pi
(%i3) float(%);
(%o3)          .02080593159405669
```

<!-- category: Statistics -->
<!-- keywords: pdf_normal -->
<!-- signatures: pdf_normal(x, m, s) -->
### Function: pdf_normal (x, m, s)

Devuelve el valor correspondiente a *x* de la función de densidad de la variable aleatoria *Normal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_pareto -->
<!-- signatures: pdf_pareto(x, a, b) -->
### Function: pdf_pareto (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de *Pareto*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_poisson -->
<!-- signatures: pdf_poisson(x, m) -->
### Function: pdf_poisson (x, m)

Devuelve el valor correspondiente a *x* de la función de probabilidad de una variable aleatoria de *Poisson*$(m)$, con $m>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_rayleigh -->
<!-- signatures: pdf_rayleigh(x, b) -->
### Function: pdf_rayleigh (x, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







```maxima
(%i1) load ("distrib")$
(%i2) pdf_rayleigh(x,b);
                                    2  2
                           2     - b  x
(%o2)                   2 b  x %e
```

<!-- category: Statistics -->
<!-- keywords: pdf_student_t -->
<!-- signatures: pdf_student_t(x, n) -->
### Function: pdf_student_t (x, n)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de Student $t(n)$, con $n>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_weibull -->
<!-- signatures: pdf_weibull(x, a, b) -->
### Function: pdf_weibull (x, a, b)

Devuelve el valor correspondiente a *x* de la función de densidad de una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_bernoulli -->
<!-- signatures: quantile_bernoulli(q, p) -->
### Function: quantile_bernoulli (q, p)

Devuelve el *q*-cuantil de una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$; en otras palabras, se trata de la inversa de  `cdf_bernoulli`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_beta -->
<!-- signatures: quantile_beta(q, a, b) -->
### Function: quantile_beta (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria *Beta*$(a,b)$, con $a,b>0$; en otras palabras, se trata de la inversa de  `cdf_beta`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_binomial -->
<!-- signatures: quantile_binomial(q, n, p) -->
### Function: quantile_binomial (q, n, p)

Devuelve el *q*-cuantil de una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo; en otras palabras, se trata de la inversa de  `cdf_binomial`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_cauchy -->
<!-- signatures: quantile_cauchy(q, a, b) -->
### Function: quantile_cauchy (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria de *Cauchy*$(a,b)$, con $b>0$; en otras palabras, se trata de la inversa de  `cdf_cauchy`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_chi2 -->
<!-- signatures: quantile_chi2(q, n) -->
### Function: quantile_chi2 (q, n)

Devuelve el *q*-cuantil de una variable aleatoria $Chi^2(n)$, con $n>0$; en otras palabras, se trata de la inversa de  `cdf_chi2`. El argumento *q* debe ser un número de $[0,1]$.


Esta función no tiene expresión compacta y se calcula numéricamente.







```maxima
(%i1) load ("distrib")$
(%i2) quantile_chi2(0.99,9);
(%o2)                   21.66599433346194
```

<!-- category: Statistics -->
<!-- keywords: quantile_continuous_uniform -->
<!-- signatures: quantile_continuous_uniform(q, a, b) -->
### Function: quantile_continuous_uniform (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$; en otras palabras, se trata de la inversa de  `cdf_continuous_uniform`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_discrete_uniform -->
<!-- signatures: quantile_discrete_uniform(q, n) -->
### Function: quantile_discrete_uniform (q, n)

Devuelve el *q*-cuantil de una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo; en otras palabras, se trata de la inversa de  `cdf_discrete_uniform`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_exp -->
<!-- signatures: quantile_exp(q, m) -->
### Function: quantile_exp (q, m)

Devuelve el *q*-cuantil de una variable aleatoria *Exponencial*$(m)$, con $m>0$; en otras palabras, se trata de la inversa de  `cdf_exp`. El argumento *q* debe ser un número de $[0,1]$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.








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

Devuelve el *q*-cuantil de una variable aleatoria  *F*$(m,n)$, con $m,n>0$; en otras palabras, se trata de la inversa de  `cdf_f`. El argumento *q* debe ser un número de $[0,1]$.








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

Devuelve el *q*-cuantil de una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$; en otras palabras, se trata de la inversa de  `cdf_gamma`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_general_finite_discrete -->
<!-- signatures: quantile_general_finite_discrete(q, v) -->
### Function: quantile_general_finite_discrete (q, v)

Devuelve el *q*-cuantil de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.

<!-- category: Statistics -->
<!-- keywords: quantile_geometric -->
<!-- signatures: quantile_geometric(q, p) -->
### Function: quantile_geometric (q, p)

Devuelve el *q*-cuantil de una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$; en otras palabras, se trata de la inversa de  `cdf_geometric`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_gumbel -->
<!-- signatures: quantile_gumbel(q, a, b) -->
### Function: quantile_gumbel (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$; en otras palabras, se trata de la inversa de  `cdf_gumbel`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_hypergeometric -->
<!-- signatures: quantile_hypergeometric(q, n1, n2, n) -->
### Function: quantile_hypergeometric (q, n1, n2, n)

Devuelve el *q*-cuantil de una variable aleatoria *Hipergeométrica*$(n1,n2,n)$, con *n1*, *n2* y *n* enteros positivos y $n<=n1+n2$; en otras palabras, se trata de la inversa de  `cdf_hypergeometric`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_laplace -->
<!-- signatures: quantile_laplace(q, a, b) -->
### Function: quantile_laplace (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria de *Laplace*$(a,b)$, con $b>0$; en otras palabras, se trata de la inversa de  `cdf_laplace`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_logistic -->
<!-- signatures: quantile_logistic(q, a, b) -->
### Function: quantile_logistic (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria *Logística*$(a,b)$, con $b>0$; en otras palabras, se trata de la inversa de  `cdf_logistic`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_lognormal -->
<!-- signatures: quantile_lognormal(q, m, s) -->
### Function: quantile_lognormal (q, m, s)

Devuelve el *q*-cuantil de una variable aleatoria *Lognormal*$(m,s)$, con $s>0$; en otras palabras, se trata de la inversa de  `cdf_lognormal`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_negative_binomial -->
<!-- signatures: quantile_negative_binomial(q, n, p) -->
### Function: quantile_negative_binomial (q, n, p)

Devuelve el *q*-cuantil de una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ y $n$ positivo; en otras palabras, se trata de la inversa de  `cdf_negative_binomial`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_noncentral_chi2 -->
<!-- signatures: quantile_noncentral_chi2(q, n, ncp) -->
### Function: quantile_noncentral_chi2 (q, n, ncp)

Devuelve el *q*-cuantil de una variable aleatoria chi-cuadrado no centrada $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$; en otras palabras, se trata de la inversa de  `cdf_noncentral_chi2`. El argumento *q* debe ser un número de $[0,1]$.


Esta función no tiene expresión compacta y se calcula numéricamente.

<!-- category: Statistics -->
<!-- keywords: quantile_noncentral_student_t -->
<!-- signatures: quantile_noncentral_student_t(q, n, ncp) -->
### Function: quantile_noncentral_student_t (q, n, ncp)

Devuelve el *q*-cuantil de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>0$ grados de libertad y parámetro de no centralidad $ncp$; en otras palabras, se trata de la inversa de `cdf_noncentral_student_t`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_normal -->
<!-- signatures: quantile_normal(q, m, s) -->
### Function: quantile_normal (q, m, s)

Devuelve el *q*-cuantil de una variable aleatoria *Normal*$(m,s)$, con $s>0$; en otras palabras, es la inversa de  `cdf_normal`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.








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

Devuelve el *q*-cuantil de una variable aleatoria de *Pareto*$(a,b)$, con $a,b>0$; en otras palabras, se trata de la inversa de  `cdf_pareto`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_poisson -->
<!-- signatures: quantile_poisson(q, m) -->
### Function: quantile_poisson (q, m)

Devuelve el *q*-cuantil de una variable aleatoria de *Poisson*$(m)$, con $m>0$; en otras palabras, se trata de la inversa de  `cdf_poisson`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_rayleigh -->
<!-- signatures: quantile_rayleigh(q, b) -->
### Function: quantile_rayleigh (q, b)

Devuelve el *q*-cuantil de una variable aleatoria de *Rayleigh*$(b)$, con $b>0$; en otras palabras, se trata de la inversa de  `cdf_rayleigh`. El argumento *q* debe ser un número de $[0,1]$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







```maxima
(%i1) load ("distrib")$
(%i2) quantile_rayleigh(0.99,b);
                        2.145966026289347
(%o2)                   -----------------
                                b
```

<!-- category: Statistics -->
<!-- keywords: quantile_student_t -->
<!-- signatures: quantile_student_t(q, n) -->
### Function: quantile_student_t (q, n)

Devuelve el *q*-cuantil de una variable aleatoria de Student $t(n)$, con $n>0$; en otras palabras, se trata de la inversa de  `cdf_student_t`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_weibull -->
<!-- signatures: quantile_weibull(q, a, b) -->
### Function: quantile_weibull (q, a, b)

Devuelve el *q*-cuantil de una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$; en otras palabras, se trata de la inversa de  `cdf_weibull`. El argumento *q* debe ser un número de $[0,1]$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_bernoulli -->
<!-- signatures: random_bernoulli(p), random_bernoulli(p, n) -->
### Function: random_bernoulli (p)

Devuelve un valor aleatorio  *Bernoulli*$(p)$, con $0 \leq p \leq 1$. Llamando a  `random_bernoulli` con un segundo argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


Es aplicación directa de la función `random` de Maxima.


Véase también `random`. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_beta -->
<!-- signatures: random_beta(a, b), random_beta(a, b, n) -->
### Function: random_beta (a, b)

Devuelve un valor aleatorio *Beta*$(a,b)$, con $a,b>0$. Llamando a `random_beta` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación es el decrito en Cheng, R.C.H. (1978). *Generating Beta Variates with Nonintegral Shape Parameters*. Communications of the ACM, 21:317-322.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_binomial -->
<!-- signatures: random_binomial(n, p), random_binomial(n, p, m) -->
### Function: random_binomial (n, p)

Devuelve un valor aleatorio  *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Llamando a  `random_binomial` con un tercer argumento *m*, se simulará una muestra aleatoria de tamaño  *m*.


El algoritmo de simulación es el descrito en Kachitvichyanukul, V. y Schmeiser, B.W. (1988) *Binomial Random Variate Generation*. Communications of the ACM, 31, Feb., 216.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_cauchy -->
<!-- signatures: random_cauchy(a, b), random_cauchy(a, b, n) -->
### Function: random_cauchy (a, b)

Devuelve un valor aleatorio  *Cauchy*$(a,b)$, con $b>0$. Llamando a  `random_cauchy` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_chi2 -->
<!-- signatures: random_chi2(n), random_chi2(n, m) -->
### Function: random_chi2 (n)

Devuelve un valor aleatorio  $Chi^2(n)$, con $n>0$. Llamando a `random_chi2` con un segundo argumento *m*, se simulará una muestra aleatoria de tamaño *m*.


La simulación está basada en el algoritmo de Ahrens-Cheng. Véase `random_gamma` para más detalles.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_continuous_uniform -->
<!-- signatures: random_continuous_uniform(a, b), random_continuous_uniform(a, b, n) -->
### Function: random_continuous_uniform (a, b)

Devuelve un valor aleatorio  *Uniforme Continuo*$(a,b)$, con $a<b$. Llamando a `random_continuous_uniform` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


Esta función es una aplicación directa de la función  `random` de Maxima.


Véase también `random`. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_discrete_uniform -->
<!-- signatures: random_discrete_uniform(n), random_discrete_uniform(n, m) -->
### Function: random_discrete_uniform (n)

Devuelve un valor aleatorio  $Uniforme Discreto(n)$, con $n$ entero positivo. Llamando a  `random_discrete_uniform` con un segundo argumento *m*, se simulará una muestra aleatoria de tamaño  *m*.


Se trata de una aplicación directa de la función `random` de Maxima.


Véase también `random`. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_exp -->
<!-- signatures: random_exp(m), random_exp(m, k) -->
### Function: random_exp (m)

Devuelve un valor aleatorio  *Exponencial*$(m)$, con $m>0$. Llamando a `random_exp2` con un segundo argumento *k*, se simulará una muestra aleatoria de tamaño *k*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_f -->
<!-- signatures: random_f(m, n), random_f(m, n, k) -->
### Function: random_f (m, n)

Devuelve un valor aleatorio  *F*$(m,n)$, con $m,n>0$. Llamando a  `random_f` con un tercer argumento *k*, se simulará una muestra aleatoria de tamaño *k*.


El algoritmo de simulación está basado en el hecho de que si *X* es una variable aleatoria $Chi^2(m)$ y $Y$ es una $Chi^2(n)$, entonces


```maxima
n X
                    F = ---
                        m Y
```


$$
F={{n X}\over{m Y}}
$$


es una variable aleatoria $F$ con *m* y *n* grados de libertad, *F*$(m,n)$.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_gamma -->
<!-- signatures: random_gamma(a, b), random_gamma(a, b, n) -->
### Function: random_gamma (a, b)

Devuelve un valor aleatorio  *Gamma*$(a,b)$, con $a,b>0$. Llamando a `random_gamma` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño *n*.


El algoritmo de simulación es una combinación de dos procedimientos, según sea el valor del parámetro *a*:


Para $a>=1$, Cheng, R.C.H. y Feast, G.M. (1979). *Some simple gamma variate generators*. Appl. Stat., 28, 3, 290-295.


Para $0<a<1$, Ahrens, J.H. y Dieter, U. (1974). *Computer methods for sampling from gamma, beta, poisson and binomial distributions*. Computing, 12, 223-246.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_general_finite_discrete -->
<!-- signatures: random_general_finite_discrete(v), random_general_finite_discrete(v, m) -->
### Function: random_general_finite_discrete (v)

Devuelve un valor aleatorio de una variable aleatoria general discreta finita, con vector de probabilidades $v$. Llamando a `random_general_finite_discrete` con un segundo argumento *n*, se simulará una muestra aleatoria de tamaño *n*.


Véase `pdf_general_finite_discrete` para más detalles.








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

Devuelve un valor aleatorio *Geométrico*$(p)$, con $0 < p \leq 1$. Llamando a  `random_geometric` con un segundo argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo está basado en la simulación de ensayos de Bernoulli.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_gumbel -->
<!-- signatures: random_gumbel(a, b), random_gumbel(a, b, n) -->
### Function: random_gumbel (a, b)

Devuelve un valor aleatorio  *Gumbel*$(a,b)$, con $b>0$. Llamando a  `random_gumbel` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_hypergeometric -->
<!-- signatures: random_hypergeometric(n1, n2, n), random_hypergeometric(n1, n2, n, m) -->
### Function: random_hypergeometric (n1, n2, n)

Devuelve un valor aleatorio *Hipergeométrico*$(n1,n2,n)$, con *n1*, *n2* y *n* enteros positivos y $n<=n1+n2$. Llamando a  `random_hypergeometric` con un cuarto argumento *m*, se simulará una muestra aleatoria de tamaño  *m*.


Algoritmo descrito en Kachitvichyanukul, V., Schmeiser, B.W. (1985) *Computer generation of hypergeometric random variates.* Journal of Statistical Computation and Simulation 22, 127-145.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_laplace -->
<!-- signatures: random_laplace(a, b), random_laplace(a, b, n) -->
### Function: random_laplace (a, b)

Devuelve un valor aleatorio  *Laplace*$(a,b)$, con $b>0$. Llamando a  `random_laplace` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_logistic -->
<!-- signatures: random_logistic(a, b), random_logistic(a, b, n) -->
### Function: random_logistic (a, b)

Devuelve un valor aleatorio  *Logístico*$(a,b)$, con $b>0$. Llamando a  `random_logistic` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_lognormal -->
<!-- signatures: random_lognormal(m, s), random_lognormal(m, s, n) -->
### Function: random_lognormal (m, s)

Devuelve un valor aleatorio  *Lognormal*$(m,s)$, con $s>0$. Llamando a `random_lognormal` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño *n*.


Las variables lognormales se simulan mediante variables normales. Véase `random_normal` para más detalles.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_negative_binomial -->
<!-- signatures: random_negative_binomial(n, p), random_negative_binomial(n, p, m) -->
### Function: random_negative_binomial (n, p)

Devuelve un valor aleatorio *Binomial Negativo*$(n,p)$, con $0 < p \leq 1$ y $n$ positivo. Llamando a  `random_negative_binomial` con un tercer argumento *m*, se simulará una muestra aleatoria de tamaño  *m*.


Algoritmo descrito en Devroye, L. (1986) *Non-Uniform Random Variate Generation*. Springer Verlag, p. 480.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_noncentral_chi2 -->
<!-- signatures: random_noncentral_chi2(n, ncp), random_noncentral_chi2(n, ncp, m) -->
### Function: random_noncentral_chi2 (n, ncp)

Devuelve un valor aleatorio  $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$. Llamando a `random_noncentral_chi2` con un tercer argumento *m*, se simulará una muestra aleatoria de tamaño *m*.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_noncentral_student_t -->
<!-- signatures: random_noncentral_student_t(n, ncp), random_noncentral_student_t(n, ncp, m) -->
### Function: random_noncentral_student_t (n, ncp)

Devuelve un valor aleatorio $nc_t(n,ncp)$, con $n>0$. Llamando a `random_noncentral_student_t` con un tercer argumento *m*, se obtiene una muestra aleatoria simulada de tamaño *m*.


El algoritmo utilizado está basado en el hecho de que si *X* es una variable aleatoria normal $N(ncp,1)$ y $S^2$ es una chi cuadrada de *n* grados de libertad, $Chi^2(n)$, entonces


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


es una variable aleatoria no central de Student de *n* grados de libertad y parámetro de no centralidad $ncp$, $nc_t(n,ncp)$.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_normal -->
<!-- signatures: random_normal(m, s), random_normal(m, s, n) -->
### Function: random_normal (m, s)

Devuelve un valor aleatorio  *Normal*$(m,s)$, con $s>0$. Llamando a `random_normal` con un tercer argumento *n*, se simula una muestra aleatoria de tamaño *n*.


El algoritmo de simulación es el de Box-Mueller, tal como está descrito en Knuth, D.E. (1981) *Seminumerical Algorithms. The Art of Computer Programming.* Addison-Wesley.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_pareto -->
<!-- signatures: random_pareto(a, b), random_pareto(a, b, n) -->
### Function: random_pareto (a, b)

Devuelve un valor aleatorio  *Pareto*$(a,b)$, con $a>0,b>0$. Llamando a  `random_pareto` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_poisson -->
<!-- signatures: random_poisson(m), random_poisson(m, n) -->
### Function: random_poisson (m)

Devuelve un valor aleatorio  *Poisson*$(m)$, con $m>0$. Llamando a  `random_poisson` con un segundo argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación es el descrito en Ahrens, J.H. and Dieter, U. (1982) *Computer Generation of Poisson Deviates From Modified Normal Distributions*. ACM Trans. Math. Software, 8, 2, June,163-179.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_rayleigh -->
<!-- signatures: random_rayleigh(b), random_rayleigh(b, n) -->
### Function: random_rayleigh (b)

Devuelve un valor aleatorio  *Rayleigh*$(b)$, con $b>0$. Llamando a  `random_rayleigh` con un segundo argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_student_t -->
<!-- signatures: random_student_t(n), random_student_t(n, m) -->
### Function: random_student_t (n)

Devuelve un valor aleatorio $t(n)$, con $n>0$. Llamando a `random_student_t` con un segundo argumento *m*, se obtiene una muestra aleatoria simulada de tamaño *m*.


El algoritmo utilizado está basado en el hecho de que si *Z* es una variable aleatoria normal $N(0,1)$ y $S^2$ es una chi cuadrada de *n* grados de libertad, $Chi^2(n)$, entonces


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


es una variable aleatoria de Student de *n* grados de libertad, $t(n)$.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_weibull -->
<!-- signatures: random_weibull(a, b), random_weibull(a, b, n) -->
### Function: random_weibull (a, b)

Devuelve un valor aleatorio  *Weibull*$(a,b)$, con $a,b>0$. Llamando a  `random_weibull` con un tercer argumento *n*, se simulará una muestra aleatoria de tamaño  *n*.


El algoritmo de simulación está basado en el método inverso.


Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_bernoulli -->
<!-- signatures: skewness_bernoulli(p) -->
### Function: skewness_bernoulli (p)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$.


La variable aleatoria *Bernoulli*$(p)$ equivale a una *Binomial*$(1,p)$.







```maxima
(%i1) load ("distrib")$
(%i2) skewness_bernoulli(p);
                                    1 - 2 p
(%o2)                           ---------------
                                sqrt((1 - p) p)
```

<!-- category: Statistics -->
<!-- keywords: skewness_beta -->
<!-- signatures: skewness_beta(a, b) -->
### Function: skewness_beta (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria *Beta*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_binomial -->
<!-- signatures: skewness_binomial(n, p) -->
### Function: skewness_binomial (n, p)

Devuelve el coeficiente de asimetría de una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_chi2 -->
<!-- signatures: skewness_chi2(n) -->
### Function: skewness_chi2 (n)

Devuelve el coeficiente de asimetría de una variable aleatoria  $Chi^2(n)$, con $n>0$.


La variable aleatoria $Chi^2(n)$ equivale a una *Gamma*$(n/2,2)$.







```maxima
(%i1) load ("distrib")$
(%i2) skewness_chi2(n);

                                     3/2
                                    2
(%o2)                              -------
                                   sqrt(n)
```

<!-- category: Statistics -->
<!-- keywords: skewness_continuous_uniform -->
<!-- signatures: skewness_continuous_uniform(a, b) -->
### Function: skewness_continuous_uniform (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_discrete_uniform -->
<!-- signatures: skewness_discrete_uniform(n) -->
### Function: skewness_discrete_uniform (n)

Devuelve el coeficiente de asimetría de una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_exp -->
<!-- signatures: skewness_exp(m) -->
### Function: skewness_exp (m)

Devuelve el coeficiente de asimetría de una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) skewness_exp(m);
(%o2)                           2
```

<!-- category: Statistics -->
<!-- keywords: skewness_f -->
<!-- signatures: skewness_f(m, n) -->
### Function: skewness_f (m, n)

Devuelve el coeficiente de asimetría de una variable aleatoria  *F*$(m,n)$, con $m>0, n>6$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_gamma -->
<!-- signatures: skewness_gamma(a, b) -->
### Function: skewness_gamma (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_general_finite_discrete -->
<!-- signatures: skewness_general_finite_discrete(v) -->
### Function: skewness_general_finite_discrete (v)

Devuelve el coeficiente de asimetría de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.

<!-- category: Statistics -->
<!-- keywords: skewness_geometric -->
<!-- signatures: skewness_geometric(p) -->
### Function: skewness_geometric (p)

Devuelve el coeficiente de asimetría de una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_gumbel -->
<!-- signatures: skewness_gumbel(a, b) -->
### Function: skewness_gumbel (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$.







```maxima
(%i1) load ("distrib")$
(%i2) skewness_gumbel(a,b);
                                  3/2
                               2 6    zeta(3)
(%o2)                          --------------
                                       3
                                    %pi
```

donde `zeta` representa la función zeta de Riemann.

<!-- category: Statistics -->
<!-- keywords: skewness_hypergeometric -->
<!-- signatures: skewness_hypergeometric(n1, n2, n) -->
### Function: skewness_hypergeometric (n1, n2, n)

Devuelve el coeficiente de asimetría de una variable aleatoria *Hipergeométrica*$(n1,n2,n)$, con *n1*, *n2* y *n* enteros positivos y $n<=n1+n2$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_laplace -->
<!-- signatures: skewness_laplace(a, b) -->
### Function: skewness_laplace (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_logistic -->
<!-- signatures: skewness_logistic(a, b) -->
### Function: skewness_logistic (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_lognormal -->
<!-- signatures: skewness_lognormal(m, s) -->
### Function: skewness_lognormal (m, s)

Devuelve el coeficiente de asimetría de una variable aleatoria *Lognormal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_negative_binomial -->
<!-- signatures: skewness_negative_binomial(n, p) -->
### Function: skewness_negative_binomial (n, p)

Devuelve el coeficiente de asimetría de una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ and $n$ positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_noncentral_chi2 -->
<!-- signatures: skewness_noncentral_chi2(n, ncp) -->
### Function: skewness_noncentral_chi2 (n, ncp)

Devuelve el coeficiente de asimetría de una variable aleatoria chi-cuadrado no centrada  $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: skewness_noncentral_student_t -->
<!-- signatures: skewness_noncentral_student_t(n, ncp) -->
### Function: skewness_noncentral_student_t (n, ncp)

Devuelve el coeficiente de asimetría de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>3$ grados de libertad y parámetro de no centralidad $ncp$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_normal -->
<!-- signatures: skewness_normal(m, s) -->
### Function: skewness_normal (m, s)

Devuelve el coeficiente de asimetría de una variable aleatoria *Normal*$(m,s)$, con $s>0$, que es siempre igual a 0. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_pareto -->
<!-- signatures: skewness_pareto(a, b) -->
### Function: skewness_pareto (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Pareto*$(a,b)$, con $a>3,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_poisson -->
<!-- signatures: skewness_poisson(m) -->
### Function: skewness_poisson (m)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Poisson*$(m)$, con $m>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_rayleigh -->
<!-- signatures: skewness_rayleigh(b) -->
### Function: skewness_rayleigh (b)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







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

<!-- category: Statistics -->
<!-- keywords: skewness_student_t -->
<!-- signatures: skewness_student_t(n) -->
### Function: skewness_student_t (n)

Devuelve el coeficiente de asimetría de una variable aleatoria de Student $t(n)$, con $n>3$, que vale siempre 0. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_weibull -->
<!-- signatures: skewness_weibull(a, b) -->
### Function: skewness_weibull (a, b)

Devuelve el coeficiente de asimetría de una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_bernoulli -->
<!-- signatures: std_bernoulli(p) -->
### Function: std_bernoulli (p)

Devuelve la desviación típica de  una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$.


La variable aleatoria *Bernoulli*$(p)$ equivale a una *Binomial*$(1,p)$.







```maxima
(%i1) load ("distrib")$
(%i2) std_bernoulli(p);
(%o2)                           sqrt((1 - p) p)
```

<!-- category: Statistics -->
<!-- keywords: std_beta -->
<!-- signatures: std_beta(a, b) -->
### Function: std_beta (a, b)

Devuelve la desviación típica de  una variable aleatoria *Beta*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_binomial -->
<!-- signatures: std_binomial(n, p) -->
### Function: std_binomial (n, p)

Devuelve la desviación típica de  una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_chi2 -->
<!-- signatures: std_chi2(n) -->
### Function: std_chi2 (n)

Devuelve la desviación típica de  una variable aleatoria  $Chi^2(n)$, con $n>0$.


La variable aleatoria $Chi^2(n)$ equivale a una *Gamma*$(n/2,2)$.







```maxima
(%i1) load ("distrib")$
(%i2) std_chi2(n);
(%o2)                    sqrt(2) sqrt(n)
```

<!-- category: Statistics -->
<!-- keywords: std_continuous_uniform -->
<!-- signatures: std_continuous_uniform(a, b) -->
### Function: std_continuous_uniform (a, b)

Devuelve la desviación típica de  una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_discrete_uniform -->
<!-- signatures: std_discrete_uniform(n) -->
### Function: std_discrete_uniform (n)

Devuelve la desviación típica de  una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_exp -->
<!-- signatures: std_exp(m) -->
### Function: std_exp (m)

Devuelve la desviación típica de  una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) std_exp(m);
                                1
(%o2)                           -
                                m
```

<!-- category: Statistics -->
<!-- keywords: std_f -->
<!-- signatures: std_f(m, n) -->
### Function: std_f (m, n)

Devuelve la desviación típica de  una variable aleatoria  *F*$(m,n)$, con $m>0, n>4$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_gamma -->
<!-- signatures: std_gamma(a, b) -->
### Function: std_gamma (a, b)

Devuelve la desviación típica de  una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_general_finite_discrete -->
<!-- signatures: std_general_finite_discrete(v) -->
### Function: std_general_finite_discrete (v)

Devuelve la desviación típica de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.

<!-- category: Statistics -->
<!-- keywords: std_geometric -->
<!-- signatures: std_geometric(p) -->
### Function: std_geometric (p)

Devuelve la desviación típica de  una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_gumbel -->
<!-- signatures: std_gumbel(a, b) -->
### Function: std_gumbel (a, b)

Devuelve la desviación típica de  una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_hypergeometric -->
<!-- signatures: std_hypergeometric(n1, n2, n) -->
### Function: std_hypergeometric (n1, n2, n)

Devuelve la desviación típica de  una variable aleatoria *Hipergeométrica*$(n1,n2,n)$, con *n1*, *n2* y *n* enteros positivos y $n<=n1+n2$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_laplace -->
<!-- signatures: std_laplace(a, b) -->
### Function: std_laplace (a, b)

Devuelve la desviación típica de  una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_logistic -->
<!-- signatures: std_logistic(a, b) -->
### Function: std_logistic (a, b)

Devuelve la desviación típica de  una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_lognormal -->
<!-- signatures: std_lognormal(m, s) -->
### Function: std_lognormal (m, s)

Devuelve la desviación típica de  una variable aleatoria *Lognormal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_negative_binomial -->
<!-- signatures: std_negative_binomial(n, p) -->
### Function: std_negative_binomial (n, p)

Devuelve la desviación típica de  una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ and $n$ positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_noncentral_chi2 -->
<!-- signatures: std_noncentral_chi2(n, ncp) -->
### Function: std_noncentral_chi2 (n, ncp)

Devuelve la desviación típica de  una variable aleatoria chi-cuadrado no centrada  $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: std_noncentral_student_t -->
<!-- signatures: std_noncentral_student_t(n, ncp) -->
### Function: std_noncentral_student_t (n, ncp)

Devuelve la desviación típica de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>2$ grados de libertad y parámetro de no centralidad $ncp$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_normal -->
<!-- signatures: std_normal(m, s) -->
### Function: std_normal (m, s)

Devuelve la desviación típica de  una variable aleatoria *Normal*$(m,s)$, con $s>0$, es decir *s*. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_pareto -->
<!-- signatures: std_pareto(a, b) -->
### Function: std_pareto (a, b)

Devuelve la desviación típica de  una variable aleatoria de *Pareto*$(a,b)$, con $a>2,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_poisson -->
<!-- signatures: std_poisson(m) -->
### Function: std_poisson (m)

Devuelve la desviación típica de  una variable aleatoria de *Poisson*$(m)$, con $m>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_rayleigh -->
<!-- signatures: std_rayleigh(b) -->
### Function: std_rayleigh (b)

Devuelve la desviación típica de  una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







```maxima
(%i1) load ("distrib")$
(%i2) std_rayleigh(b);
                                   %pi
                          sqrt(1 - ---)
                                    4
(%o2)                     -------------
                                b
```

<!-- category: Statistics -->
<!-- keywords: std_student_t -->
<!-- signatures: std_student_t(n) -->
### Function: std_student_t (n)

Devuelve la desviación típica de una variable aleatoria de Student $t(n)$, con $n>2$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_weibull -->
<!-- signatures: std_weibull(a, b) -->
### Function: std_weibull (a, b)

Devuelve la desviación típica de  una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_bernoulli -->
<!-- signatures: var_bernoulli(p) -->
### Function: var_bernoulli (p)

Devuelve la varianza de  una variable aleatoria de *Bernoulli*$(p)$, con $0 \leq p \leq 1$.


La variable aleatoria *Bernoulli*$(p)$ equivale a una *Binomial*$(1,p)$.







```maxima
(%i1) load ("distrib")$
(%i2) var_bernoulli(p);
(%o2)                       (1 - p) p
```

<!-- category: Statistics -->
<!-- keywords: var_beta -->
<!-- signatures: var_beta(a, b) -->
### Function: var_beta (a, b)

Devuelve la varianza de  una variable aleatoria *Beta*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_binomial -->
<!-- signatures: var_binomial(n, p) -->
### Function: var_binomial (n, p)

Devuelve la varianza de  una variable aleatoria *Binomial*$(n,p)$, con $0 \leq p \leq 1$ y $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_chi2 -->
<!-- signatures: var_chi2(n) -->
### Function: var_chi2 (n)

Devuelve la varianza de  una variable aleatoria  $Chi^2(n)$, con $n>0$.


La variable aleatoria $Chi^2(n)$ equivale a una *Gamma*$(n/2,2)$.







```maxima
(%i1) load ("distrib")$
(%i2) var_chi2(n);
(%o2)                          2 n
```

<!-- category: Statistics -->
<!-- keywords: var_continuous_uniform -->
<!-- signatures: var_continuous_uniform(a, b) -->
### Function: var_continuous_uniform (a, b)

Devuelve la varianza de  una variable aleatoria  *Uniforme Continua*$(a,b)$, con $a<b$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_discrete_uniform -->
<!-- signatures: var_discrete_uniform(n) -->
### Function: var_discrete_uniform (n)

Devuelve la varianza de  una variable aleatoria *Uniforme Discreta*$(n)$, con $n$ entero positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_exp -->
<!-- signatures: var_exp(m) -->
### Function: var_exp (m)

Devuelve la varianza de  una variable aleatoria *Exponencial*$(m)$, con $m>0$.


La variable aleatoria *Exponencial*$(m)$ equivale a una *Weibull*$(1,1/m)$.







```maxima
(%i1) load ("distrib")$
(%i2) var_exp(m);
                               1
(%o2)                          --
                                2
                               m
```

<!-- category: Statistics -->
<!-- keywords: var_f -->
<!-- signatures: var_f(m, n) -->
### Function: var_f (m, n)

Devuelve la varianza de  una variable aleatoria  *F*$(m,n)$, con $m>0, n>4$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_gamma -->
<!-- signatures: var_gamma(a, b) -->
### Function: var_gamma (a, b)

Devuelve la varianza de  una variable aleatoria *Gamma*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_general_finite_discrete -->
<!-- signatures: var_general_finite_discrete(v) -->
### Function: var_general_finite_discrete (v)

Devuelve la varianza de una variable aleatoria general discreta finita, con vector de probabilidades $v$.


Véase `pdf_general_finite_discrete` para más detalles.

<!-- category: Statistics -->
<!-- keywords: var_geometric -->
<!-- signatures: var_geometric(p) -->
### Function: var_geometric (p)

Devuelve la varianza de  una variable aleatoria *Geométrica*$(p)$, con $0 < p \leq 1$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_gumbel -->
<!-- signatures: var_gumbel(a, b) -->
### Function: var_gumbel (a, b)

Devuelve la varianza de  una variable aleatoria de *Gumbel*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_hypergeometric -->
<!-- signatures: var_hypergeometric(n1, n2, n) -->
### Function: var_hypergeometric (n1, n2, n)

Devuelve la varianza de  una variable aleatoria *Hipergeométrica*$(n1,n2,n)$, con *n1*, *n2* y *n* enteros positivos y $n<=n1+n2$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_laplace -->
<!-- signatures: var_laplace(a, b) -->
### Function: var_laplace (a, b)

Devuelve la varianza de  una variable aleatoria de *Laplace*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_logistic -->
<!-- signatures: var_logistic(a, b) -->
### Function: var_logistic (a, b)

Devuelve la varianza de  una variable aleatoria *Logística*$(a,b)$, con $b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_lognormal -->
<!-- signatures: var_lognormal(m, s) -->
### Function: var_lognormal (m, s)

Devuelve la varianza de  una variable aleatoria *Lognormal*$(m,s)$, con $s>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_negative_binomial -->
<!-- signatures: var_negative_binomial(n, p) -->
### Function: var_negative_binomial (n, p)

Devuelve la varianza de  una variable aleatoria *Binomial Negativa*$(n,p)$, con $0 < p \leq 1$ and $n$ positivo. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_noncentral_chi2 -->
<!-- signatures: var_noncentral_chi2(n, ncp) -->
### Function: var_noncentral_chi2 (n, ncp)

Devuelve la varianza de  una variable aleatoria chi-cuadrado no centrada  $nc_Chi^2(n,ncp)$, con $n>0$ y parámetro de no centralidad $ncp>=0$.

<!-- category: Statistics -->
<!-- keywords: var_noncentral_student_t -->
<!-- signatures: var_noncentral_student_t(n, ncp) -->
### Function: var_noncentral_student_t (n, ncp)

Devuelve la varianza de una variable aleatoria no central de Student $nc_t(n,ncp)$, con $n>2$ grados de libertad y parámetro de no centralidad $ncp$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_normal -->
<!-- signatures: var_normal(m, s) -->
### Function: var_normal (m, s)

Devuelve la varianza de  una variable aleatoria *Normal*$(m,s)$, con $s>0$, es decir *s^2*.

<!-- category: Statistics -->
<!-- keywords: var_pareto -->
<!-- signatures: var_pareto(a, b) -->
### Function: var_pareto (a, b)

Devuelve la varianza de  una variable aleatoria de *Pareto*$(a,b)$, con $a>2,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_poisson -->
<!-- signatures: var_poisson(m) -->
### Function: var_poisson (m)

Devuelve la varianza de  una variable aleatoria de *Poisson*$(m)$, con  $m>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_rayleigh -->
<!-- signatures: var_rayleigh(b) -->
### Function: var_rayleigh (b)

Devuelve la varianza de  una variable aleatoria de *Rayleigh*$(b)$, con $b>0$.


La variable aleatoria *Rayleigh*$(b)$ equivale a una *Weibull*$(2,1/b)$.







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

<!-- category: Statistics -->
<!-- keywords: var_student_t -->
<!-- signatures: var_student_t(n) -->
### Function: var_student_t (n)

Devuelve la varianza de una variable aleatoria de Student $t(n)$, con $n>2$.







```maxima
(%i1) load ("distrib")$
(%i2) var_student_t(n);
                                n
(%o2)                         -----
                              n - 2
```

<!-- category: Statistics -->
<!-- keywords: var_weibull -->
<!-- signatures: var_weibull(a, b) -->
### Function: var_weibull (a, b)

Devuelve la varianza de  una variable aleatoria de *Weibull*$(a,b)$, con $a,b>0$. Para hacer uso de esta función, ejecútese primero `load("distrib")`.

