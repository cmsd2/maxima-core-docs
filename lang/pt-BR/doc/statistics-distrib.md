## distrib

<!-- category: Statistics -->
<!-- keywords: cdf_bernoulli -->
<!-- signatures: cdf_bernoulli(x, p) -->
### Function: cdf_bernoulli (x, p)

Retorna o valor em *x* da função distribuição de
probabilidade de uma variável aleatória $Bernoulli(p)$, com $0<p<1$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_beta -->
<!-- signatures: cdf_beta(x, a, b) -->
### Function: cdf_beta (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade de
uma variável aleatória $Beta(a,b)$, com $a,b>0$. 


Essa função não possui uma forma fechada e é calculada numericamante se a
variável global `numer` for igual a `true`,  de outra forma essa função
retorna uma expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_beta(1/3,15,2);
                                 1
(%o2)                   cdf_beta(-, 15, 2)
                                 3
(%i3) %,numer;
(%o3)                 7.666089131388224E-7
```

<!-- category: Statistics -->
<!-- keywords: cdf_binomial -->
<!-- signatures: cdf_binomial(x, n, p) -->
### Function: cdf_binomial (x, n, p)

Retorna o valor em *x* da função distribuição de probabilidade
de uma $Binomial(n,p)$ variável aleatória, com $0<p<1$ e $n$ um inteiro positivo.


`cdf_binomial` é calculada numéricamente se a variável global `numer`
for igual a `true`,  de outra forma `cdf_binomial` retorna uma expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_binomial(5,7,1/6);
                                         1
(%o2)                 cdf_binomial(5, 7, -)
                                         6
(%i3) cdf_binomial(5,7,1/6), numer;
(%o3)                   .9998713991769548
```

<!-- category: Statistics -->
<!-- keywords: cdf_cauchy -->
<!-- signatures: cdf_cauchy(x, a, b) -->
### Function: cdf_cauchy (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Cauchy(a,b)$, com $b>0$. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_chi2 -->
<!-- signatures: cdf_chi2(x, n) -->
### Function: cdf_chi2 (x, n)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória Chi-quadrada $Chi^2(n)$, com $n>0$.


Essa função não possui uma forma fechada e é calculada numericamante
se a variável global `numer` for igual a `true`,  de outra forma essa
função retorna uma expressão nominal baseada na 
distribuição gama, uma vez
que a variável aleatória $Chi^2(n)$
é equivalente a    é equivalente a $Gamma(n/2,2)$.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_chi2(3,4);
(%o2)                  cdf_gamma(3, 2, 2)
(%i3) cdf_chi2(3,4),numer;
(%o3)                   .4421745996289249
```

<!-- category: Statistics -->
<!-- keywords: cdf_continuous_uniform -->
<!-- signatures: cdf_continuous_uniform(x, a, b) -->
### Function: cdf_continuous_uniform (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Continuous Uniform(a,b)$, com $a<b$.
Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_discrete_uniform -->
<!-- signatures: cdf_discrete_uniform(x, n) -->
### Function: cdf_discrete_uniform (x, n)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Discrete Uniform(n)$, com $n$ inteiro
estritamente positivo. Para fazer uso dessa função, escreva
primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_exp -->
<!-- signatures: cdf_exp(x, m) -->
### Function: cdf_exp (x, m)

Retorna o valor em *x* da função distribuição de probabilidade
variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na distribuição de
Weibull é
retornada.








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

Retorna o valor em *x* da função distribuição de probabilidade de
uma variável aleatória F, $F(m,n)$, com $m,n>0$. Essa função
não possui uma forma definitiva e é calculada numericamente se
a
variável global
`numer` for igual a `true`,  de outra forma retorna uma expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_f(2,3,9/4);
                                     9
(%o2)                    cdf_f(2, 3, -)
                                     4
(%i3) %,numer;
(%o3)                   0.66756728179008
```

<!-- category: Statistics -->
<!-- keywords: cdf_gamma -->
<!-- signatures: cdf_gamma(x, a, b) -->
### Function: cdf_gamma (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade de
uma variável aleatória $Gamma(a,b)$, com $a,b>0$. 


Essa função não possui uma forma fechada e é calculada numericamante se
a variável global `numer` for igual a `true`,  de outra forma essa função
retorna uma expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_gamma(3,5,21);
(%o2)                  cdf_gamma(3, 5, 21)
(%i3) %,numer;
(%o3)                 4.402663157135039E-7
```

<!-- category: Statistics -->
<!-- keywords: cdf_geometric -->
<!-- signatures: cdf_geometric(x, p) -->
### Function: cdf_geometric (x, p)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Geometric(p)$, com $0<p<1$. Para fazer
uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_gumbel -->
<!-- signatures: cdf_gumbel(x, a, b) -->
### Function: cdf_gumbel (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade de uma
variável aleatória $Gumbel(a,b)$, com $b>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_hypergeometric -->
<!-- signatures: cdf_hypergeometric(x, n1, n2, n) -->
### Function: cdf_hypergeometric (x, n1, n2, n)

Retorna o valor em *x* da função distribuição de
probabilidade de uma variável aleatória $Hypergeometric(n1,n2,n)$,
com *n1*, *n2* e *n* inteiros não negativos e $n<=n1+n2$. Para
fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_laplace -->
<!-- signatures: cdf_laplace(x, a, b) -->
### Function: cdf_laplace (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Laplace(a,b)$, com $b>0$. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_logistic -->
<!-- signatures: cdf_logistic(x, a, b) -->
### Function: cdf_logistic (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Logistic(a,b)$, com $b>0$. Para fazer
uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_lognormal -->
<!-- signatures: cdf_lognormal(x, m, s) -->
### Function: cdf_lognormal (x, m, s)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Lognormal(m,s)$, com $s>0$. Essa
função é definida em termos de funções `erf`de erro
internas do Maxima.







```maxima
(%i1) load ("distrib")$
(%i2) assume(x>0, s>0)$  cdf_lognormal(x,m,s);
                           log(x) - m
                       erf(----------)
                           sqrt(2) s     1
(%o3)                  --------------- + -
                              2          2
```


Veja também `erf`.

<!-- category: Statistics -->
<!-- keywords: cdf_negative_binomial -->
<!-- signatures: cdf_negative_binomial(x, n, p) -->
### Function: cdf_negative_binomial (x, n, p)

Retorna o valor em *x* da função distribuição de probabilidade
de uma $Negative Binomial(n,p)$ variável aleatória, com $0<p<1$ e $n$ um inteiro positivo.


Essa função é calculada numéricamente se a variável global `numer` for
igual a `true`,  de outra forma essa função retorna uma expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_negative_binomial(3,4,1/8);
                                             1
(%o2)            cdf_negative_binomial(3, 4, -)
                                             8
(%i3) cdf_negative_binomial(3,4,1/8), numer;
(%o3)                  .006238937377929698
```

<!-- category: Statistics -->
<!-- keywords: cdf_normal -->
<!-- signatures: cdf_normal(x, m, s) -->
### Function: cdf_normal (x, m, s)

Retorna o valor em *x* da função distribuição de probabilidade
de uma  variável aleatória $Normal(m,s)$, com $s>0$. Essa
função é definida em termos de funções de erro internas do
Maxima,
`erf`.







```maxima
(%i1) load ("distrib")$
(%i2) assume(s>0)$ cdf_normal(x,m,s);
                             x - m
                       erf(---------)
                           sqrt(2) s    1
(%o3)                  -------------- + -
                             2          2
```


Veja também `erf`.

<!-- category: Statistics -->
<!-- keywords: cdf_pareto -->
<!-- signatures: cdf_pareto(x, a, b) -->
### Function: cdf_pareto (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Pareto(a,b)$, com $a,b>0$. Para fazer
uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: cdf_poisson -->
<!-- signatures: cdf_poisson(x, m) -->
### Function: cdf_poisson (x, m)

Retorna o valor em *x* da função distribuição de
probabilidade de uma variável aleatória $Poisson(m)$, com $m>0$.


Essa função é calculada numéricamente se a variável global
`numer` for igual a `true`,  de outra forma essa função
retorna uma expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_poisson(3,5);
(%o2)                   cdf_poisson(3, 5)
(%i3) cdf_poisson(3,5), numer;
(%o3)                   .2650259152973617
```

<!-- category: Statistics -->
<!-- keywords: cdf_rayleigh -->
<!-- signatures: cdf_rayleigh(x, b) -->
### Function: cdf_rayleigh (x, b)

Retorna o valor em *x* da função distribuição de probabilidade
de uma variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o
resultado, uma forma nominal baseada na distribuição de Weibull é retornada.








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

Retorna o valor em *x* da função distribuição de probabilidade de
uma variável aleatória de Student $t(n)$, com $n>0$. Essa função
não tem uma forma definitiva e é calculada numericamente
se a
variável global
`numer` for igual a `true`,  de outra froma `cdf_student_t` retorna uma
expressão nominal.








```maxima
(%i1) load ("distrib")$
(%i2) cdf_student_t(1/2, 7/3);
                                     1  7
(%o2)                  cdf_student_t(-, -)
                                     2  3
(%i3) %,numer;
(%o3)                   .6698450596140417
```

<!-- category: Statistics -->
<!-- keywords: cdf_weibull -->
<!-- signatures: cdf_weibull(x, a, b) -->
### Function: cdf_weibull (x, a, b)

Retorna o valor em *x* da função distribuição de probabilidade de uma
variável aleatória $Weibull(a,b)$, com $a,b>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_bernoulli -->
<!-- signatures: kurtosis_bernoulli(p) -->
### Function: kurtosis_bernoulli (p)

Retorna o coeficiente de curtose de uma variável aleatória $Bernoulli(p)$, com $0<p<1$.


A variável aleatória $Bernoulli(p)$ é equivalente a $Binomial(1,p)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de curtose binomial é retornada.








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

Retorna o coeficiente de curtose de uma variável aleatória $Beta(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_binomial -->
<!-- signatures: kurtosis_binomial(n, p) -->
### Function: kurtosis_binomial (n, p)

Retorna o coeficiente de curtose de uma variável aleatória $Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_chi2 -->
<!-- signatures: kurtosis_chi2(n) -->
### Function: kurtosis_chi2 (n)

Retorna o coeficiente de curtose de uma variável aleatória Chi-quadrada
$Chi^2(n)$, com $n>0$.


A variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de curtose da função gama é retornada.








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

Retorna o coeficiente de curtose de uma variável aleatória $Continuous Uniform(a,b)$,
com $a<b$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_discrete_uniform -->
<!-- signatures: kurtosis_discrete_uniform(n) -->
### Function: kurtosis_discrete_uniform (n)

Retorna o coeficiente de curtose de uma variável aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_exp -->
<!-- signatures: kurtosis_exp(m) -->
### Function: kurtosis_exp (m)

Retorna o coeficiente de curtose de uma variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$, embora
quando Maxima não tiver informação disponível para pegar o resultado, uma forma nominal
baseada no coeficiente de curtose de Weibull é retornada.








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

Retorna o coeficiente de curtose de uma variável aleatória F, $F(m,n)$,
com $m>0, n>8$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_gamma -->
<!-- signatures: kurtosis_gamma(a, b) -->
### Function: kurtosis_gamma (a, b)

Retorna o coeficiente de curtose de uma variável aleatória $Gamma(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_geometric -->
<!-- signatures: kurtosis_geometric(p) -->
### Function: kurtosis_geometric (p)

Retorna o coeficiente de curtose de uma geometric variável aleatória  $Geo(p)$,
com $0<p<1$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_gumbel -->
<!-- signatures: kurtosis_gumbel(a, b) -->
### Function: kurtosis_gumbel (a, b)

Retorna o coeficiente de curtose de uma variável aleatória $Gumbel(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_hypergeometric -->
<!-- signatures: kurtosis_hypergeometric(n1, n2, n) -->
### Function: kurtosis_hypergeometric (n1, n2, n)

Retorna o coeficiente de curtose de uma variável aleatória $Hypergeometric(n1,n2,n)$,
com *n1*, *n2* e *n* inteiros não negativos e $n<=n1+n2$. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_laplace -->
<!-- signatures: kurtosis_laplace(a, b) -->
### Function: kurtosis_laplace (a, b)

Retorna o coeficiente de curtose de uma variável aleatória $Laplace(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_logistic -->
<!-- signatures: kurtosis_logistic(a, b) -->
### Function: kurtosis_logistic (a, b)

Retorna o coeficiente de curtose de uma variável aleatória $Logistic(a,b)$ ,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_lognormal -->
<!-- signatures: kurtosis_lognormal(m, s) -->
### Function: kurtosis_lognormal (m, s)

Retorna o coeficiente de curtose de uma variável aleatória $Lognormal(m,s)$,
com $s>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_negative_binomial -->
<!-- signatures: kurtosis_negative_binomial(n, p) -->
### Function: kurtosis_negative_binomial (n, p)

Retorna o coeficiente de curtose de uma variável aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_normal -->
<!-- signatures: kurtosis_normal(m, s) -->
### Function: kurtosis_normal (m, s)

Retorna o coeficiente de curtose de uma  variável aleatória $Normal(m,s)$,
com $s>0$, que é sempre igual  a 0. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_pareto -->
<!-- signatures: kurtosis_pareto(a, b) -->
### Function: kurtosis_pareto (a, b)

Retorna o coeficiente de curtose de uma variável aleatória $Pareto(a,b)$,
com $a>4,b>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_poisson -->
<!-- signatures: kurtosis_poisson(m) -->
### Function: kurtosis_poisson (m)

Retorna o coeficiente de curtose de uma Poisson variável aleatória  $Poi(m)$,
com $m>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_rayleigh -->
<!-- signatures: kurtosis_rayleigh(b) -->
### Function: kurtosis_rayleigh (b)

Retorna o coeficiente de curtose de uma variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de curtose de Weibull é retornada.








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

Retorna o coeficiente de curtose de uma variável aleatória de Student $t(n)$,
com $n>4$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: kurtosis_weibull -->
<!-- signatures: kurtosis_weibull(a, b) -->
### Function: kurtosis_weibull (a, b)

Retorna o coeficiente de curtose de uma variável aleatória $Weibull(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_bernoulli -->
<!-- signatures: mean_bernoulli(p) -->
### Function: mean_bernoulli (p)

Retorna a média de uma variável aleatória $Bernoulli(p)$, com $0<p<1$.


A variável aleatória $Bernoulli(p)$ é equivalente a $Binomial(1,p)$, embora
quando Maxima não tiver informação disponível para pegar o resultado, uma forma
nominal baseada na média binomial é retornada.








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

Retorna a média de uma variável aleatória $Beta(a,b)$, com $a,b>0$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_binomial -->
<!-- signatures: mean_binomial(n, p) -->
### Function: mean_binomial (n, p)

Retorna a média de uma variável aleatória $Binomial(n,p)$, com
$0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_chi2 -->
<!-- signatures: mean_chi2(n) -->
### Function: mean_chi2 (n)

Retorna a média de uma variável aleatória Chi-quadrada $Chi^2(n)$, com $n>0$.


A variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na média da função gama é
retornada.








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

Retorna a média de uma variável aleatória $Continuous Uniform(a,b)$,
com $a<b$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_discrete_uniform -->
<!-- signatures: mean_discrete_uniform(n) -->
### Function: mean_discrete_uniform (n)

Retorna a média de uma variável aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_exp -->
<!-- signatures: mean_exp(m) -->
### Function: mean_exp (m)

Retorna a média de uma variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na média de Weibull é
reornada.








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

Retorna a média de uma variável aleatória F, $F(m,n)$, com $m>0, n>2$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_gamma -->
<!-- signatures: mean_gamma(a, b) -->
### Function: mean_gamma (a, b)

Retorna a média de uma variável aleatória $Gamma(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_geometric -->
<!-- signatures: mean_geometric(p) -->
### Function: mean_geometric (p)

Retorna a média de uma variável aleatória $Geometric(p)$,
com $0<p<1$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_gumbel -->
<!-- signatures: mean_gumbel(a, b) -->
### Function: mean_gumbel (a, b)

Retorna a média de uma variável aleatória $Gumbel(a,b)$, com $b>0$.







```maxima
(%i1) load ("distrib")$
(%i2) assume(b>0)$  mean_gumbel(a,b);
(%o3)                     %gamma b + a
```

onde o símbolol `%gamma` representa a constante de Euler-Mascheroni.
Veja também `%gamma`.

<!-- category: Statistics -->
<!-- keywords: mean_hypergeometric -->
<!-- signatures: mean_hypergeometric(n1, n2, n) -->
### Function: mean_hypergeometric (n1, n2, n)

Retorna a média de uma variável aleatória discreta univorme
$Hyp(n1,n2,n)$, com *n1*, *n2* e *n* inteiros não negativos
e $n<=n1+n2$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_laplace -->
<!-- signatures: mean_laplace(a, b) -->
### Function: mean_laplace (a, b)

Retorna a média de uma variável aleatória $Laplace(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_lognormal -->
<!-- signatures: mean_lognormal(m, s) -->
### Function: mean_lognormal (m, s)

Retorna a média de uma variável aleatória $Lognormal(m,s)$, com $s>0$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_negative_binomial -->
<!-- signatures: mean_negative_binomial(n, p) -->
### Function: mean_negative_binomial (n, p)

Retorna a média de uma variável aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_normal -->
<!-- signatures: mean_normal(m, s) -->
### Function: mean_normal (m, s)

Retorna a média de uma  variável aleatória $Normal(m,s)$, com
$s>0$, a saber *m*. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_pareto -->
<!-- signatures: mean_pareto(a, b) -->
### Function: mean_pareto (a, b)

Retorna a média de uma variável aleatória $Pareto(a,b)$, com
$a>1,b>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_poisson -->
<!-- signatures: mean_poisson(m) -->
### Function: mean_poisson (m)

Retorna a média de uma variável aleatória $Poisson(m)$,
com $m>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_rayleigh -->
<!-- signatures: mean_rayleigh(b) -->
### Function: mean_rayleigh (b)

Retorna a média de uma variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na meia de Weibull é retornada.








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

Retorna a média de uma variável aleatória de Student $t(n)$, com
$n>0$, que é sempre igual a 0. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: mean_weibull -->
<!-- signatures: mean_weibull(a, b) -->
### Function: mean_weibull (a, b)

Retorna a média de uma variável aleatória $Weibull(a,b)$, com
$a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: meanlog -->
<!-- signatures: meanlog(a, b) -->
### Function: meanlog (a, b)

Retorna a média de uma $Logistic(a,b)$ variável aleatória , com $b>0$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_bernoulli -->
<!-- signatures: pdf_bernoulli(x, p) -->
### Function: pdf_bernoulli (x, p)

Retorna o valor em *x* da função de probabilidade de uma
variável aleatória $Bernoulli(p)$, com $0<p<1$.


A variável aleatória $Bernoulli(p)$ é equivalente a $Binomial(1,p)$,
embora quando Maxima não tiver informação disponível para pegar o
resultado, uma forma nominal baseada na função binomial de
probabilidade é retornada.








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

Retorna o valor em *x* da função densidade de probabilidade de uma variável
aleatória $Beta(a,b)$, com $a,b>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_binomial -->
<!-- signatures: pdf_binomial(x, n, p) -->
### Function: pdf_binomial (x, n, p)

Retorna o valor em *x* da função de probabilidade de uma $Binomial(n,p)$
variável aleatória, com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_cauchy -->
<!-- signatures: pdf_cauchy(x, a, b) -->
### Function: pdf_cauchy (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Cauchy(a,b)$, com $b>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_chi2 -->
<!-- signatures: pdf_chi2(x, n) -->
### Function: pdf_chi2 (x, n)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória Chi-quadrada $Chi^2(n)$, com $n>0$.


A  variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$,
portanto quando Maxima não tiver informação para pegar o resultado, uma
forma nomial baseada na função de densidade densidade de probabilidade da
função  gama é
retornada.








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

Retorna o valor em *x* da função densidade de probabilidade
de uma variável aleatória $Continuous Uniform(a,b)$, com $a<b$.
Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_discrete_uniform -->
<!-- signatures: pdf_discrete_uniform(x, n) -->
### Function: pdf_discrete_uniform (x, n)

Retorna o valor em *x* da função de probabilidade de uma variável
aleatória $Discrete Uniform(n)$, com $n$ a strictly positive integer. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_exp -->
<!-- signatures: pdf_exp(x, m) -->
### Function: pdf_exp (x, m)

Retorna o valor em *x* da função densidade de probabilidade
variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a
$Weibull(1,1/m)$, embora quando Maxima não tiver informação
disponível para pegar o resultado, uma forma nominal baseada na função
de densidade de probabilidade de Weibull éretornada.








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

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória F, $F(m,n)$, com $m,n>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_gamma -->
<!-- signatures: pdf_gamma(x, a, b) -->
### Function: pdf_gamma (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Gamma(a,b)$, com $a,b>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_geometric -->
<!-- signatures: pdf_geometric(x, p) -->
### Function: pdf_geometric (x, p)

Retorna o valor em *x* da função de probabilidade de uma variável
aleatória $Geometric(p)$, com $0<p<1$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_gumbel -->
<!-- signatures: pdf_gumbel(x, a, b) -->
### Function: pdf_gumbel (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de uma variável
aleatória $Gumbel(a,b)$, com $b>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_hypergeometric -->
<!-- signatures: pdf_hypergeometric(x, n1, n2, n) -->
### Function: pdf_hypergeometric (x, n1, n2, n)

Retorna o valor em *x* da função de probabilidade de uma
variável aleatória $Hypergeometric(n1,n2,n)$, com *n1*, *n2*
e *n* inteiros não negativos e $n<=n1+n2$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_laplace -->
<!-- signatures: pdf_laplace(x, a, b) -->
### Function: pdf_laplace (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Laplace(a,b)$, com $b>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_logistic -->
<!-- signatures: pdf_logistic(x, a, b) -->
### Function: pdf_logistic (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de
uma variável aleatória $Logistic(a,b)$ , com $b>0$. Para fazer
uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_lognormal -->
<!-- signatures: pdf_lognormal(x, m, s) -->
### Function: pdf_lognormal (x, m, s)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Lognormal(m,s)$, com $s>0$. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_negative_binomial -->
<!-- signatures: pdf_negative_binomial(x, n, p) -->
### Function: pdf_negative_binomial (x, n, p)

Retorna o valor em *x* da função de probabilidade de uma variável
aleatória $Negative Binomial(n,p)$, com $0<p<1$ e $n$ um inteiro
positivo. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_normal -->
<!-- signatures: pdf_normal(x, m, s) -->
### Function: pdf_normal (x, m, s)

Retorna o valor em *x* da função densidade de probabilidade
de uma  variável aleatória $Normal(m,s)$, com $s>0$. Para fazer
uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_pareto -->
<!-- signatures: pdf_pareto(x, a, b) -->
### Function: pdf_pareto (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Pareto(a,b)$, com $a,b>0$. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_poisson -->
<!-- signatures: pdf_poisson(x, m) -->
### Function: pdf_poisson (x, m)

Retorna o valor em *x* da função de probabilidade de uma
variável aleatória $Poisson(m)$, com $m>0$. Para fazer
uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_rayleigh -->
<!-- signatures: pdf_rayleigh(x, b) -->
### Function: pdf_rayleigh (x, b)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na função densidade de probabilidade de Weibull é retornada.








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

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória de Student $t(n)$, com $n>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: pdf_weibull -->
<!-- signatures: pdf_weibull(x, a, b) -->
### Function: pdf_weibull (x, a, b)

Retorna o valor em *x* da função densidade de probabilidade de uma
variável aleatória $Weibull(a,b)$, com $a,b>0$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_bernoulli -->
<!-- signatures: quantile_bernoulli(q, p) -->
### Function: quantile_bernoulli (q, p)

Retorna o *q*-quantil de uma variável aleatória $Bernoulli(p)$,
com $0<p<1$; em outras palavras, essa função é a inversa da
função `cdf_bernoulli`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_beta -->
<!-- signatures: quantile_beta(q, a, b) -->
### Function: quantile_beta (q, a, b)

Retorna o *q*-quantil de uma variável aleatória $Beta(a,b)$, com
$a,b>0$; em outras palavras, essa função é a inversa da função
`cdf_beta`. O argumento *q* deve ser um elemento de
$[0,1]$. Para
fazer uso dessa
função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_binomial -->
<!-- signatures: quantile_binomial(q, n, p) -->
### Function: quantile_binomial (q, n, p)

Retorna o *q*-quantil de uma variável aleatória $Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo; em outras palavras, essa
função é a inversa da função `cdf_binomial`. O argumento
*q* deve ser um elemento de $[0,1]$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_cauchy -->
<!-- signatures: quantile_cauchy(q, a, b) -->
### Function: quantile_cauchy (q, a, b)

Retorna o *q*-quantil de uma variável aleatória $Cauchy(a,b)$, com
$b>0$; em outras palavras, essa função é a inversa da função
`cdf_cauchy`. O argumento *q* deve ser um elemento de $[0,1]$. Para
fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_chi2 -->
<!-- signatures: quantile_chi2(q, n) -->
### Function: quantile_chi2 (q, n)

Retorna o *q*-quantilede uma variável aleatória Chi-quadrada $Chi^2(n)$,
com $n>0$; em outras palavras, essa função é a inversa da função
`cdf_chi2`. O argumento *q* deve ser um elemento
de
$[0,1]$.


This função não possui uma forma fechada e é calculada numericamante se
a variável global `numer` for igual a `true`,  de outra forma essa
função retorna uma expressão nominal baseada no quantil da função
gama, uma vez que a variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$.








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

Retorna o *q*-quantil de uma variável aleatória $Continuous Uniform(a,b)$,
com $a<b$; em outras palavras, essa função é a inversa da função
`cdf_continuous_uniform`. O argumento *q* deve
ser um elemento
de $[0,1]$.
Para
fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_discrete_uniform -->
<!-- signatures: quantile_discrete_uniform(q, n) -->
### Function: quantile_discrete_uniform (q, n)

Retorna o *q*-quantil de uma variável aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo; em outras palavras, essa
função é a inversa da função `cdf_discrete_uniform`. O
argumento *q* deve ser um elemento de $[0,1]$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_exp -->
<!-- signatures: quantile_exp(q, m) -->
### Function: quantile_exp (q, m)

Retorna o *q*-quantil variável aleatória $Exponential(m)$, com $m>0$;
em outras palavras, essa função é inversa da função `cdf_exp`.
O argumento *q* deve ser um elemento de $[0,1]$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no qualtil de Weibull é
retornada.








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

Retorna o *q*-quantil de uma variável aleatória F, $F(m,n)$, com $m,n>0$;
em outras palavras, essa função é o inverso de `cdf_f`. O argumento *q* deve ser um elemento de $[0,1]$.


Essa função não possui uma forma fechada e é calculada numericamante se a
variável global `numer` for igual a `true`,  de outra forma essa função
retorna uma expressão nominal.








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

Retorna o *q*-quantil de uma variável aleatória $Gamma(a,b)$,
com $a,b>0$; em outras palavras, essa função é a inversa da
função `cdf_gamma`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_geometric -->
<!-- signatures: quantile_geometric(q, p) -->
### Function: quantile_geometric (q, p)

Retorna o *q*-quantil de uma variável aleatória $Geometric(p)$,
com $0<p<1$; em outras palavras, essa função é a inversa da
função `cdf_geometric`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_gumbel -->
<!-- signatures: quantile_gumbel(q, a, b) -->
### Function: quantile_gumbel (q, a, b)

Retorna o *q*-quantil de uma variável aleatória $Gumbel(a,b)$, com
$b>0$; em outras palavras, essa função é a inversa da função
`cdf_gumbel`. O argumento *q* deve ser um elemento de $[0,1]$. Para
fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_hypergeometric -->
<!-- signatures: quantile_hypergeometric(q, n1, n2, n) -->
### Function: quantile_hypergeometric (q, n1, n2, n)

Retorna o *q*-quantil de uma variável aleatória $Hypergeometric(n1,n2,n)$,
com *n1*, *n2* e *n* inteiros não negativos e $n<=n1+n2$; em outras
palavras, essa função é a inversa da função `cdf_hypergeometric`.
O argumento *q* deve ser um elemento de $[0,1]$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_laplace -->
<!-- signatures: quantile_laplace(q, a, b) -->
### Function: quantile_laplace (q, a, b)

Retorna o *q*-quantil de uma variável aleatória $Laplace(a,b)$, com
$b>0$; em outras palavras, essa função é a inversa da função
`cdf_laplace`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_logistic -->
<!-- signatures: quantile_logistic(q, a, b) -->
### Function: quantile_logistic (q, a, b)

Retorna o *q*-quantil de uma variável aleatória $Logistic(a,b)$ , com
$b>0$; em outras palavras, essa função é a inversa da função
`cdf_logistic`. O argumento *q* deve ser um elemento de
$[0,1]$.
Para fazer uso
dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_lognormal -->
<!-- signatures: quantile_lognormal(q, m, s) -->
### Function: quantile_lognormal (q, m, s)

Retorna o *q*-quantil de uma variável aleatória $Lognormal(m,s)$,
com $s>0$; em outras palavras, essa função é a inversa da função
`cdf_lognormal`. O argumento *q* deve ser um elemento de $[0,1]$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_negative_binomial -->
<!-- signatures: quantile_negative_binomial(q, n, p) -->
### Function: quantile_negative_binomial (q, n, p)

Retorna o *q*-quantil de uma variável aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo; em outras palavras, essa função
é a inversa da função `cdf_negative_binomial`. O argumento *q* deve ser
um elemento de $[0,1]$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_normal -->
<!-- signatures: quantile_normal(q, m, s) -->
### Function: quantile_normal (q, m, s)

Retorna o *q*-quantil de uma variável aleatória $Normal(m,s)$, com
$s>0$; em outras palavras, isso é o inverso de `cdf_normal`. O argumento
*q* deve ser um elemento de $[0,1]$. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_pareto -->
<!-- signatures: quantile_pareto(q, a, b) -->
### Function: quantile_pareto (q, a, b)

Retorna o *q*-quantile de uma variável aleatória $Pareto(a,b)$,
com $a,b>0$; em outras palavras, essa função é a inversa da
função `cdf_pareto`. O argumento *q* deve ser um elemento de
$[0,1]$. Para
fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_poisson -->
<!-- signatures: quantile_poisson(q, m) -->
### Function: quantile_poisson (q, m)

Retorna o *q*-quantil de uma variável aleatória $Poisson(m)$,
com $m>0$; em outras palavras, essa função é a inversa da
função `cdf_poisson`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_rayleigh -->
<!-- signatures: quantile_rayleigh(q, b) -->
### Function: quantile_rayleigh (q, b)

Retorna o *q*-quantil de uma variável aleatória $Rayleigh(b)$, com
$b>0$; em outras palavras, essa função é a inversa da função
`cdf_rayleigh`. O argumento *q* deve ser um elemento de
$[0,1]$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no quantil de Weibull é
retornada.








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

Retorna o *q*-quantil de uma variável aleatória de Student $t(n)$,
com $n>0$; em outras palavras, `quantile_student_t` é o inverso de
`cdf_student_t`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: quantile_weibull -->
<!-- signatures: quantile_weibull(q, a, b) -->
### Function: quantile_weibull (q, a, b)

Retorna o *q*-quantil de uma variável aleatória $Weibull(a,b)$,
com $a,b>0$; em outras palavras, essa função é a inversa da
função `cdf_weibull`. O argumento *q* deve ser um elemento de
$[0,1]$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_bernoulli -->
<!-- signatures: random_bernoulli(p), random_bernoulli(p, n) -->
### Function: random_bernoulli (p)

Retorna uma variável estatística pseudo-aleatória $Bernoulli(p)$,
com $0<p<1$. Chamando `random_bernoulli` com um segundo
argumento *n*, uma amostra aleatória de tamanho *n* será simulada.


Essa é uma aplicação direta da função `random` built-in função do Maxima.


Veja também `random`. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_beta -->
<!-- signatures: random_beta(a, b), random_beta(a, b, n) -->
### Function: random_beta (a, b)

Retorna uma variável estatística pseudo-aleatória $Beta(a,b)$,
com $a,b>0$. Chamando `random_beta` com um terceiro argumento *n*,
uma amostra aleatória de tamanho *n* será simulada.


Existem três algorítmos implementados para essa função, se pode selecionar
o algorítmo a ser usado fornecendo um certo valor à variável global
`random_beta_algorithm`, cujo valor padrão é `cheng`.


Veja também `random_beta_algorithm`. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_beta_algorithm -->
<!-- signatures: random_beta_algorithm -->
### Variable: random_beta_algorithm

Valor padrão: `cheng`


Esse é o algorítmo selecionado para simular variáveis estatísticas beta
pseudo-aleatórias. Os algorítmos implementados são `cheng`,
`inverse` e `ratio`


- *
`cheng`, esse é o algorítmo definido em Cheng, R.C.H.  (1978). 
*Generating Beta Variates with Nonintegral Shape Parameters*.
Communications of the ACM, 21:317-322
- *
`inverse`, baseado no método inverso genérico.
- *
`ratio`, baseado no fato de que se *X* for uma variável aleatória
$Gamma(a,1)$ e *Y* for $Gamma(b,1)$, então a razão $X/(X+Y)$
está distribuída como $Beta(a,b)$.


Veja também `random_beta`.

<!-- category: Statistics -->
<!-- keywords: random_binomial -->
<!-- signatures: random_binomial(n, p), random_binomial(n, p, m) -->
### Function: random_binomial (n, p)

Retorna uma variável estatística pseudo-aleatória $Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Chamando `random_binomial`
com um terceiro argumento *m*, uma amostra aleatória de tamanho *m* será
simulada.


Existem três algorítmos implementado para essa função, se pode
selecionar o algorítmo a ser usado fornecendo um certo valor à variável
global `random_binomial_algorithm`, cujo valor padrão é `kachit`.


Veja também `random_binomial_algorithm`. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_binomial_algorithm -->
<!-- signatures: random_binomial_algorithm -->
### Variable: random_binomial_algorithm

Valor padrão: `kachit`


Esse é o algorítmo selecionado para simular rvariáveis estatísticas pseudo-aleatórias
binomiais. Os algorítmos implementados são `kachit`, `bernoulli` e `inverse`:


- *
`kachit`, baseado no algorítmo descrito em Kachitvichyanukul, V. and
Schmeiser, B.W. (1988) *Binomial Random Variate Generation*. Communications of the ACM, 31, Feb., 216.
- *
`bernoulli`, baseado na simulação testes de Bernoulli.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_binomial`.

<!-- category: Statistics -->
<!-- keywords: random_cauchy -->
<!-- signatures: random_cauchy(a, b), random_cauchy(a, b, n) -->
### Function: random_cauchy (a, b)

Retorna uma variável estatística pseudo aleatória $Cauchy(a,b)$, com $b>0$.
Chamando `random_cauchy` com um terceiro argumento *n*, uma amostra
aleatória de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_chi2 -->
<!-- signatures: random_chi2(n), random_chi2(n, m) -->
### Function: random_chi2 (n)

Retorna uma variável estatística pseudo-aleatória Chi-square $Chi^2(n)$,
com $n>0$. Chamando `random_chi2` com um segundo argumento *m*,
uma amostra aleatória de tamanho *m* será simulada.


Existem dois algorítmos implementados para essa função, se pode selecionar o
algorítmo a ser usado fornecendo um certo valor à variável global
`random_chi2_algorithm`, cujo valor padrão é
`ahrens_cheng`.


Veja também `random_chi2_algorithm`. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_chi2_algorithm -->
<!-- signatures: random_chi2_algorithm -->
### Variable: random_chi2_algorithm

Valor padrão: `ahrens_cheng`


Esse é o algorítmo selecionado para simular variáveis estatística pseudo-aleatórias
Chi-quadradas. Os algorítmos implementados são `ahrens_cheng` e `inverse`:


- *
`ahrens_cheng`, baseado na simulação aleatória de variáveis gama.
Veja `random_gamma_algorithm` para mais detalhes.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_chi2`.

<!-- category: Statistics -->
<!-- keywords: random_continuous_uniform -->
<!-- signatures: random_continuous_uniform(a, b), random_continuous_uniform(a, b, n) -->
### Function: random_continuous_uniform (a, b)

Retorna uma variável estatística pseudo-aleatória $Continuous Uniform(a,b)$,
com $a<b$. Chamando `random_continuous_uniform` com um terceiro
argumento *n*, uma amostra aleatória de tamanho *n* será simulada.


Essa é uma aplicação direta da função `random` interna do Maxima.


Veja também `random`. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_discrete_uniform -->
<!-- signatures: random_discrete_uniform(n), random_discrete_uniform(n, m) -->
### Function: random_discrete_uniform (n)

Retorna uma variável estatística pseudo-aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo. Chamando `random_discrete_uniform`
com um segundo argumento *m*, uma amostra aleatória de
tamanho *m* será simulada.


Isso é uma aplicação direta da função `random` built-in função do Maxima.


Veja também `random`. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_exp -->
<!-- signatures: random_exp(m), random_exp(m, k) -->
### Function: random_exp (m)

Retorna uma variável estatística pseudo-aleatória $Exponential(m)$,
com $m>0$. Chamando `random_exp` com um segundo argumento
*k*, uma amostra aleatória de tamanho *k* será simulada.


Existem três algorítmos implementados para essa função, se pode
selecionar o algorítmo a ser usado fornecendo um certo valor à variável global
`random_exp_algorithm`, cujo valor padrão é `inverse`.


Veja também `random_exp_algorithm`. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_exp_algorithm -->
<!-- signatures: random_exp_algorithm -->
### Variable: random_exp_algorithm

Valor padrão: `inverse`


Esse é o algorítmo selecionado para simular variáveis exponenciais estatística
pseudo-aleatórias. Os algorítmos implementados são `inverse`,
`ahrens_cheng` e `ahrens_dieter`


- *
`inverse`, baseado no método inverso genérico.
- *
`ahrens_cheng`, baseado no fato de que a variável aleatória $Exp(m)$
é equivalente a $Gamma(1,1/m)$. Veja `random_gamma_algorithm`
para maiores detalhes.
- *
`ahrens_dieter`, baseado no algorítmo descrito em Ahrens, J.H. e Dieter, U. (1972)
*Computer methods for sampling from the exponential and normal distributions.*
Comm, ACM, 15, Oct.,  873-882.


Veja também `random_exp`.

<!-- category: Statistics -->
<!-- keywords: random_f -->
<!-- signatures: random_f(m, n), random_f(m, n, k) -->
### Function: random_f (m, n)

Retorna uma variável estatística pseudo-aleatória F, $F(m,n)$,
com $m,n>0$. Chamando `random_f` com um terceiro argumento
*k*, uma amostra aleatória de tamanho *k* será simulada.


Existem dois algorítmos implementados para essa função, se pode selecionar
o algorítmo a ser usado fornecendo um certo valor à variável global
`random_f_algorithm`, cujo valor padrão é `inverse`.


Veja também `random_f_algorithm`. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_f_algorithm -->
<!-- signatures: random_f_algorithm -->
### Variable: random_f_algorithm

Valor padrão: `inverse`


Esse é o algorítmo selecionado para simular variáveis estatísticas
pseudo-aleatórias F. Os algorítmos implementados são `ratio`
e `inverse`:


- *
`ratio`, baseado no fato de que se *X* for uma variável aleatória
$Chi^2(m)$ e $Y$ for uma variável aleatória $Chi^2(n)$,
então
$$
F={{n X}\over{m Y}}
$$
é uma variável aleatória F com *m* e *n* graus de liberdade, $F(m,n)$.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_f`.

<!-- category: Statistics -->
<!-- keywords: random_gamma -->
<!-- signatures: random_gamma(a, b), random_gamma(a, b, n) -->
### Function: random_gamma (a, b)

Retorna uma variável estatística pseudo-aleatória $Gamma(a,b)$,
com $a,b>0$. Chamando `random_gamma` com um terceiro argumento
*n*, uma amostra aleatória de tamanho *n* será simulada.


Existem dois algorítmos implementados para essa função, se pode selecionar
o algorítmo a ser usado fornecendo um certo valor à variável global `random_gamma_algorithm`, cujo valor padrão é
`ahrens_cheng`.


Veja também `random_gamma_algorithm`. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_gamma_algorithm -->
<!-- signatures: random_gamma_algorithm -->
### Variable: random_gamma_algorithm

Valor padrão: `ahrens_cheng`


Esse é o algorítmo selecionado para simular variáveis estatística gama
pseudo-aleatórias. Os algorítmos implementados são `ahrens_cheng`
e `inverse`


- *
`ahrens_cheng`, essa é uma combinação de dois processos, dependendo
do valor do parâmetro *a*:

For $a>=1$, Cheng, R.C.H. e Feast, G.M. (1979). *Some simple gamma variate
generators*. Appl. Stat., 28, 3, 290-295.

For $0<a<1$, Ahrens, J.H. e Dieter, U. (1974). *Computer methods for sampling
from gamma, beta, poisson and binomial cdf_tributions*. Computing, 12, 223-246.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_gamma`.

<!-- category: Statistics -->
<!-- keywords: random_geometric -->
<!-- signatures: random_geometric(p), random_geometric(p, n) -->
### Function: random_geometric (p)

Retorna um $Geometric(p)$ variável estatística pseudo-aleatória, com $0<p<1$.
Chamando `random_geometric` com um segundo argumento *n*, uma amostra aleatória
de tamanho *n* será simulada.


Existem três algorítmos implementados para essa função, se
pode selecionar o algorítmo a ser usado fornecendo um certo valor à
variável global `random_geometric_algorithm`, cujo valor padrão é
`bernoulli`.


Veja também `random_geometric_algorithm`. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_geometric_algorithm -->
<!-- signatures: random_geometric_algorithm -->
### Variable: random_geometric_algorithm

Valor padrão: `bernoulli`


Esse é o algorítmo selecionado para simular variáveis estatísticas pseudo-aleatórias
geométricas. Algorítmos implementados são `bernoulli`, `devroye` e `inverse`:


- *
`bernoulli`, baseado na simulação de testes de Bernoulli.
- *
`devroye`, baseado no algorítmo descrito em Devroye, L. (1986)
*Non-Uniform Random Variate Generation.* Springer Verlag, p. 480.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_geometric`.

<!-- category: Statistics -->
<!-- keywords: random_gumbel -->
<!-- signatures: random_gumbel(a, b), random_gumbel(a, b, n) -->
### Function: random_gumbel (a, b)

Retorna uma variável estatística pseudo-aleatória $Gumbel(a,b)$,
com $b>0$. Chamando `random_gumbel` com um terceiro argumento *n*,
uma amostra aleatória de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_hypergeometric -->
<!-- signatures: random_hypergeometric(n1, n2, n), random_hypergeometric(n1, n2, n, m) -->
### Function: random_hypergeometric (n1, n2, n)

Retorna uma variável estatística pseudo-aleatória $Hypergeometric(n1,n2,n)$,
com *n1*, *n2* e *n* inteiros não negativos e $n<=n1+n2$. Chamando
`random_hypergeometric` com um quarto argumento *m*, uma amostra
aleatória de tamanho *m* será simulada.


Existem dois algorítmos implementados para essa função, se pode selecionar o
algorítmo a ser usado fornecendo um certo valor à variável global `random_hypergeometric_algorithm`,
cujo valor padrão é `kachit`.


Veja também `random_hypergeometric_algorithm`. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_hypergeometric_algorithm -->
<!-- signatures: random_hypergeometric_algorithm -->
### Variable: random_hypergeometric_algorithm

Valor padrão: `kachit`


Esse é o algorítmo selecionado para simular variáveis estatísticas pseudo
aleatórias hipergeométricas.Os algorítmos implementados são `kachit` e `inverse`:


- *
`kachit`, baseado no algorítmo descrito em Kachitvichyanukul, V., Schmeiser, B.W. (1985)
*Computer generation of hypergeometric variáveis estatística pseudo-aleatórias.* Journal
of Statistical Computation and Simulation 22, 127-145.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_hypergeometric`.

<!-- category: Statistics -->
<!-- keywords: random_laplace -->
<!-- signatures: random_laplace(a, b), random_laplace(a, b, n) -->
### Function: random_laplace (a, b)

Retorna uma variável estatística pseudo-aleatória $Laplace(a,b)$, com $b>0$.
Chamando `random_laplace` com um terceiro argumento *n*, uma
amostra aleatória de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_logistic -->
<!-- signatures: random_logistic(a, b), random_logistic(a, b, n) -->
### Function: random_logistic (a, b)

Retorna uma variável estatística pseudo-aleatória $Logistic(a,b)$, com $b>0$.
Chamando `random_logistic` com um terceiro argumento *n*, uma
amostra aleatória de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_lognormal -->
<!-- signatures: random_lognormal(m, s), random_lognormal(m, s, n) -->
### Function: random_lognormal (m, s)

Retorna uma variável estatística pseudo-aleatória $Lognormal(m,s)$,
com $s>0$. Chamando `random_lognormal` com um terceiro argumento
*n*, uma amostra aleatória de tamanho *n* será simulada.


Variáveis Log-normal são simuladas por meio de variáveis estatísticas normais
pseudo-aleatórias. Existem dois algorítmos implementados para essa função, se
pode selecionar o algorítmo a ser usado fornecendo um certo valor
à variável global
`random_normal_algorithm`, cujo valor padrão é `box_mueller`.


Veja também `random_normal_algorithm`. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_negative_binomial -->
<!-- signatures: random_negative_binomial(n, p), random_negative_binomial(n, p, m) -->
### Function: random_negative_binomial (n, p)

Retorna uma variável estatística pseudo-aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Chamando `random_negative_binomial`
com um terceiro argumento *m*, uma amostra aleatória de tamanho
*m* será simulada.


Existem três algorítmos implementados para essa função, se pode
selecionar o algorítmo a ser usado fornecendo um certo valor à variável global
`random_negative_binomial_algorithm`, cujo valor padrão é `bernoulli`.


Veja também `random_negative_binomial_algorithm`. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_negative_binomial_algorithm -->
<!-- signatures: random_negative_binomial_algorithm -->
### Variable: random_negative_binomial_algorithm

Valor padrão: `bernoulli`


Esse é o algorítmo selecionado para simular variáveis estatísticas pseuso-aleatórias
binomiais negativas. Os algorítmos implementados são `devroye`, `bernoulli`
e `inverse`:


- *
`devroye`, baseado no algorítmo descrito em Devroye, L. (1986)
*Non-Uniform Random Variate Generation*. Springer Verlag, p. 480.
- *
`bernoulli`, baseado na simulação de testes de Bernoulli.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_negative_binomial`.

<!-- category: Statistics -->
<!-- keywords: random_normal -->
<!-- signatures: random_normal(m, s), random_normal(m, s, n) -->
### Function: random_normal (m, s)

Retorna uma variável estatística pseudo-aleatória $Normal(m,s)$,
com $s>0$. Chamando `random_normal` com um terceiro argumento
*n*, uma amostra aleatória de tamanho *n* será simulada.


Existem dois algorítmos implementados para essa função, e o algorítmo
a ser usado pode ser selecionado fornecendo um certo valor para a variável global
`random_normal_algorithm`, cujo valor padrão é
`box_mueller`.


Veja também `random_normal_algorithm`. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_normal_algorithm -->
<!-- signatures: random_normal_algorithm -->
### Variable: random_normal_algorithm

Valor padrão: `box_mueller`


Esse é o algorítmo selecionado para simular variáveis aleatórias normais.
O algorítmos implementados são `box_mueller` e `inverse`:


- *
`box_mueller`, Baseado no algorítmo descrito em Knuth, D.E. (1981)
*Seminumerical Algorithms. The Art of Computer Programming.* Addison-Wesley.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_normal`.

<!-- category: Statistics -->
<!-- keywords: random_pareto -->
<!-- signatures: random_pareto(a, b), random_pareto(a, b, n) -->
### Function: random_pareto (a, b)

Retorna uma variável estatística pseudo-aleatória $Pareto(a,b)$, com
$a>0,b>0$. Chamando `random_pareto` com um terceiro
argumento *n*, uma amostra aleatória de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_poisson -->
<!-- signatures: random_poisson(m), random_poisson(m, n) -->
### Function: random_poisson (m)

Retorna uma variável estatística pseudo-aleatória $Poisson(m)$, com $m>0$.
Chamando `random_poisson` com um segundo argumento *n*, uma amostra
aleatória de tamanho *n* será simulada.


Existem dois algorítmos implementado para essa função, se pode selecionar o
algorítmo a ser usado fornecendo um certo valor à variável global 
`random_poisson_algorithm`, cujo valor padrão é
`ahrens_dieter`.


Veja também `random_poisson_algorithm`. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_poisson_algorithm -->
<!-- signatures: random_poisson_algorithm -->
### Variable: random_poisson_algorithm

Valor padrão: `ahrens_dieter`


Esse é o algorítmo selecionado para simular variáveis estatísticas
pseudo-aleatórias de Poisson.Os algorítmos implementados são `ahrens_dieter` e `inverse`:


- *
`ahrens_dieter`, baseado no algorítmo descrito em Ahrens, J.H. and
Dieter, U. (1982) *Computer Generation of Poisson Deviates From Modified Normal Distributions*.
ACM Trans. Math. Software, 8, 2, June,163-179.
- *
`inverse`, baseado no método inverso genérico.


Veja também `random_poisson`.

<!-- category: Statistics -->
<!-- keywords: random_rayleigh -->
<!-- signatures: random_rayleigh(b), random_rayleigh(b, n) -->
### Function: random_rayleigh (b)

Retorna uma variável estatística pseudo-aleatória $Rayleigh(b)$, com $b>0$.
Chamando `random_rayleigh` com um segundo argumento *n*, uma amostra aleatória
de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_student_t -->
<!-- signatures: random_student_t(n), random_student_t(n, m) -->
### Function: random_student_t (n)

Retorna uma variável estatística pseudo-aleatória de Student $t(n)$,
com $n>0$. Chamando `random_student_t` com um segundo argumento
*m*, uma amostra aleatória de tamanho *m* será simulada.


Existem dois algorítmos implementados para essa função, se pode
selecionar o algorítmo a ser usado fornecendo um certo valor à variável
global `random_student_t_algorithm`, cujo valor padrão é `ratio`.


Veja também `random_student_t_algorithm`. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: random_student_t_algorithm -->
<!-- signatures: random_student_t_algorithm -->
### Variable: random_student_t_algorithm

Valor padrão: `ratio`


Esse é o  algorítmo selecionado para simular variáveis estatísticas pseudo-aleatórias
de Student. Algorítmos implementados são `inverse` e `ratio`:


- *
`inverse`, baseado no método inverso genérico.
- *
`ratio`, baseado no fato que se *Z* for uma variável aleatória normal $N(0,1)$ e
$S^2$ for uma variável aleatória chi quadrada com *n* graus de liberdade,
$Chi^2(n)$, então
$$
X={{Z}\over{\sqrt{{S^2}\over{n}}}}
$$
é uma variável aleatória de Student com *n* graus de liberdade, $t(n)$.


Veja também `random_student_t`.

<!-- category: Statistics -->
<!-- keywords: random_weibull -->
<!-- signatures: random_weibull(a, b), random_weibull(a, b, n) -->
### Function: random_weibull (a, b)

Retorna uma variável estatística pseudo-aleatória $Weibull(a,b)$,
com $a,b>0$. Chamando `random_weibull` com um terceiro argumento
*n*, uma amostra aleatória de tamanho *n* será simulada.


Somente o método inverso genérico está implementado. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_bernoulli -->
<!-- signatures: skewness_bernoulli(p) -->
### Function: skewness_bernoulli (p)

Retorna o coeficiente de assimetria de uma variável aleatória $Bernoulli(p)$, com $0<p<1$.


A variável aleatória $Bernoulli(p)$ é equivalente a $Binomial(1,p)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de assimetria binomial é retornada.








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

Retorna o coeficiente de assimetria de uma variável aleatória $Beta(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_binomial -->
<!-- signatures: skewness_binomial(n, p) -->
### Function: skewness_binomial (n, p)

Retorna o coeficiente de assimetria de uma variável aleatória 
$Binomial(n,p)$, com $0<p<1$ e $n$ um inteiro positivo. Para
fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_chi2 -->
<!-- signatures: skewness_chi2(n) -->
### Function: skewness_chi2 (n)

Retorna o coeficiente de assimetria de uma variável aleatória Chi-quadrada
$Chi^2(n)$, com $n>0$.


A variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de assimetria da
função gama é
retornada.








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

Retorna o coeficiente de assimetria de uma variável aleatória $Continuous Uniform(a,b)$,
com $a<b$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_discrete_uniform -->
<!-- signatures: skewness_discrete_uniform(n) -->
### Function: skewness_discrete_uniform (n)

Retorna o coeficiente de assimetria de uma variável aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_exp -->
<!-- signatures: skewness_exp(m) -->
### Function: skewness_exp (m)

Retorna o coeficiente de assimetria de uma variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de assimetria
de Weibull
é retornada.








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

Retorna o coeficiente de assimetria de uma variável aleatória F, $F(m,n)$,
com $m>0, n>6$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_gamma -->
<!-- signatures: skewness_gamma(a, b) -->
### Function: skewness_gamma (a, b)

Retorna o coeficiente de assimetria de uma variável aleatória $Gamma(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_geometric -->
<!-- signatures: skewness_geometric(p) -->
### Function: skewness_geometric (p)

Retorna o coeficiente de assimetria de uma variável aleatória $Geometric(p)$,
com $0<p<1$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_gumbel -->
<!-- signatures: skewness_gumbel(a, b) -->
### Function: skewness_gumbel (a, b)

Retorna o coeficiente de assimetria de uma variável aleatória $Gumbel(a,b)$, com $b>0$.








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

onde `zeta` representa a função zeta de Riemann.

<!-- category: Statistics -->
<!-- keywords: skewness_hypergeometric -->
<!-- signatures: skewness_hypergeometric(n1, n2, n) -->
### Function: skewness_hypergeometric (n1, n2, n)

Retorna o coeficiente de assimetria de uma variável aleatória $Hypergeometric(n1,n2,n)$,
com *n1*, *n2* e *n* inteiros não negativos e $n<=n1+n2$. Para fazer uso
dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_laplace -->
<!-- signatures: skewness_laplace(a, b) -->
### Function: skewness_laplace (a, b)

Retorna o coeficiente de assimetria de uma variável aleatória $Laplace(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_logistic -->
<!-- signatures: skewness_logistic(a, b) -->
### Function: skewness_logistic (a, b)

Retorna o coeficiente de assimetria de uma variável aleatória $Logistic(a,b)$ ,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_lognormal -->
<!-- signatures: skewness_lognormal(m, s) -->
### Function: skewness_lognormal (m, s)

Retorna o coeficiente de assimetria de uma variável aleatória $Lognormal(m,s)$,
com $s>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_negative_binomial -->
<!-- signatures: skewness_negative_binomial(n, p) -->
### Function: skewness_negative_binomial (n, p)

Retorna o coeficiente de assimetria de uma variável aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_normal -->
<!-- signatures: skewness_normal(m, s) -->
### Function: skewness_normal (m, s)

Retorna o coeficiente de assimetria de uma  variável aleatória $Normal(m,s)$,
com $s>0$, que é sempre igual  a 0. Para fazer uso dessa função,escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_pareto -->
<!-- signatures: skewness_pareto(a, b) -->
### Function: skewness_pareto (a, b)

Retorna o coeficiente de assimetria de uma variável aleatória
$Pareto(a,b)$, com $a>3,b>0$. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_poisson -->
<!-- signatures: skewness_poisson(m) -->
### Function: skewness_poisson (m)

Retorna o coeficiente de assimetria de uma variável aleatória $Poisson(m)$,
com $m>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_rayleigh -->
<!-- signatures: skewness_rayleigh(b) -->
### Function: skewness_rayleigh (b)

Retorna o coeficiente de assimetria de uma variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no coeficiente de assimetria de Weibull  é retornada.








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

Retorna o coeficiente de assimetria de uma variável aleatória de Student $t(n)$,
com $n>3$, que é sempre igual a 0. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: skewness_weibull -->
<!-- signatures: skewness_weibull(a, b) -->
### Function: skewness_weibull (a, b)

Retorna o coeficiente de assimetria de uma variável aleatória $Weibull(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_bernoulli -->
<!-- signatures: std_bernoulli(p) -->
### Function: std_bernoulli (p)

Retorna o desvio padrão de uma variável aleatória $Bernoulli(p)$, com $0<p<1$.


A variável aleatória $Bernoulli(p)$ é equivalente a
$Binomial(1,p)$, embora quando Maxima não tiver informação
disponível para pegar o resultado, uma forma nominal baseada no desvio
padrão binomial é retornada.








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

Retorna o desvio padrão de uma variável aleatória $Beta(a,b)$, com $a,b>0$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_binomial -->
<!-- signatures: std_binomial(n, p) -->
### Function: std_binomial (n, p)

Retorna o desvio padrão de uma variável aleatória $Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_chi2 -->
<!-- signatures: std_chi2(n) -->
### Function: std_chi2 (n)

Retorna o desvio padrão de uma variável aleatória Chi-quadrada
$Chi^2(n)$, com $n>0$.


A variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no desvio padrão da função
gama é retornada.








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

Retorna o desvio padrão de uma variável aleatória $Continuous Uniform(a,b)$,
com $a<b$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_discrete_uniform -->
<!-- signatures: std_discrete_uniform(n) -->
### Function: std_discrete_uniform (n)

Retorna o desvio padrão de uma variável aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_exp -->
<!-- signatures: std_exp(m) -->
### Function: std_exp (m)

Retorna o desvio padrão de uma variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada no desvio padrão de
Weibull é retornada.








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

Retorna o desvio padrão de uma variável aleatória F, $F(m,n)$, com $m>0, n>4$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_gamma -->
<!-- signatures: std_gamma(a, b) -->
### Function: std_gamma (a, b)

Retorna o desvio padrão de uma variável aleatória $Gamma(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_geometric -->
<!-- signatures: std_geometric(p) -->
### Function: std_geometric (p)

Retorna o desvio padrão de uma variável aleatória $Geometric(p)$,
com $0<p<1$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_gumbel -->
<!-- signatures: std_gumbel(a, b) -->
### Function: std_gumbel (a, b)

Retorna o desvio padrão de uma variável aleatória $Gumbel(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_hypergeometric -->
<!-- signatures: std_hypergeometric(n1, n2, n) -->
### Function: std_hypergeometric (n1, n2, n)

Retorna o desvio padrão de uma variável aleatória $Hypergeometric(n1,n2,n)$,
com *n1*, *n2* e *n* inteiros não negativos e $n<=n1+n2$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_laplace -->
<!-- signatures: std_laplace(a, b) -->
### Function: std_laplace (a, b)

Retorna o desvio padrão de uma variável aleatória $Laplace(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_logistic -->
<!-- signatures: std_logistic(a, b) -->
### Function: std_logistic (a, b)

Retorna o desvio padrão de uma variável aleatória $Logistic(a,b)$ ,
com $b>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_lognormal -->
<!-- signatures: std_lognormal(m, s) -->
### Function: std_lognormal (m, s)

Retorna o desvio padrão de uma variável aleatória $Lognormal(m,s)$,
com $s>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_negative_binomial -->
<!-- signatures: std_negative_binomial(n, p) -->
### Function: std_negative_binomial (n, p)

Retorna o desvio padrão de uma variável aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_normal -->
<!-- signatures: std_normal(m, s) -->
### Function: std_normal (m, s)

Retorna o desvio padrão de uma  variável aleatória $Normal(m,s)$,
com $s>0$, a saber *s*. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_pareto -->
<!-- signatures: std_pareto(a, b) -->
### Function: std_pareto (a, b)

Retorna o desvio padrão de uma variável aleatória $Pareto(a,b)$,
com $a>2,b>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_poisson -->
<!-- signatures: std_poisson(m) -->
### Function: std_poisson (m)

Retorna o desvio padrão de uma variável aleatória $Poisson(m)$,
com $m>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_rayleigh -->
<!-- signatures: std_rayleigh(b) -->
### Function: std_rayleigh (b)

Retorna o desvio padrão de uma variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na Weibull desvio padrão é retornada.








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

Retorna o desvio padrão de uma variável aleatória de Student $t(n)$,
com $n>2$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: std_weibull -->
<!-- signatures: std_weibull(a, b) -->
### Function: std_weibull (a, b)

Retorna o desvio padrão de uma variável aleatória $Weibull(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_bernoulli -->
<!-- signatures: var_bernoulli(p) -->
### Function: var_bernoulli (p)

Retorna a variância de uma variável aleatória $Bernoulli(p)$, com $0<p<1$.


A variável aleatória $Bernoulli(p)$ é equivalente a $Binomial(1,p)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na variância binomial é retornada.








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

Retorna a variância de uma variável aleatória $Beta(a,b)$, com $a,b>0$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_binomial -->
<!-- signatures: var_binomial(n, p) -->
### Function: var_binomial (n, p)

Retorna a variância de uma variável aleatória $Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa
função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_chi2 -->
<!-- signatures: var_chi2(n) -->
### Function: var_chi2 (n)

Retorna a variância de uma variável aleatória Chi-quadrada $Chi^2(n)$, com $n>0$.


A variável aleatória $Chi^2(n)$ é equivalente a $Gamma(n/2,2)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na variância da função gama
é retornada.








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

Retorna a variância de uma variável aleatória $Continuous Uniform(a,b)$,
com $a<b$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_discrete_uniform -->
<!-- signatures: var_discrete_uniform(n) -->
### Function: var_discrete_uniform (n)

Retorna a variância de uma variável aleatória $Discrete Uniform(n)$,
com $n$ um inteiro estritamente positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_exp -->
<!-- signatures: var_exp(m) -->
### Function: var_exp (m)

Retorna a variância de uma variável aleatória $Exponential(m)$, com $m>0$.


A variável aleatória $Exponential(m)$ é equivalente a $Weibull(1,1/m)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na variância de Weibull
é retornada.








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

Retorna a variância de uma variável aleatória F, $F(m,n)$, com $m>0, n>4$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_gamma -->
<!-- signatures: var_gamma(a, b) -->
### Function: var_gamma (a, b)

Retorna a variância de uma variável aleatória $Gamma(a,b)$, com
$a,b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_geometric -->
<!-- signatures: var_geometric(p) -->
### Function: var_geometric (p)

Retorna a variância de uma variável aleatória $Geometric(p)$,
com $0<p<1$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_gumbel -->
<!-- signatures: var_gumbel(a, b) -->
### Function: var_gumbel (a, b)

Retorna a variância de uma variável aleatória $Gumbel(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_hypergeometric -->
<!-- signatures: var_hypergeometric(n1, n2, n) -->
### Function: var_hypergeometric (n1, n2, n)

Retorna a variância de uma variável aleatória hipergeométrica
$Hyp(n1,n2,n)$, com *n1*, *n2* e *n* inteiros
não negativos e $n<=n1+n2$. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_laplace -->
<!-- signatures: var_laplace(a, b) -->
### Function: var_laplace (a, b)

Retorna a variância de uma variável aleatória $Laplace(a,b)$,
com $b>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_logistic -->
<!-- signatures: var_logistic(a, b) -->
### Function: var_logistic (a, b)

Retorna a variância de uma variável aleatória $Logistic(a,b)$ , com $b>0$.
Para fazer uso dessa função, escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_lognormal -->
<!-- signatures: var_lognormal(m, s) -->
### Function: var_lognormal (m, s)

Retorna a variância de uma variável aleatória $Lognormal(m,s)$,
com $s>0$. Para fazer uso dessa função, escreva primeiramente
`load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_negative_binomial -->
<!-- signatures: var_negative_binomial(n, p) -->
### Function: var_negative_binomial (n, p)

Retorna a variância de uma variável aleatória $Negative Binomial(n,p)$,
com $0<p<1$ e $n$ um inteiro positivo. Para fazer uso dessa função,
escreva primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_normal -->
<!-- signatures: var_normal(m, s) -->
### Function: var_normal (m, s)

Retorna a variância de uma  variável aleatória $Normal(m,s)$, com
$s>0$, a saber *s^2*. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_pareto -->
<!-- signatures: var_pareto(a, b) -->
### Function: var_pareto (a, b)

Retorna a variância de uma variável aleatória $Pareto(a,b)$,
com $a>2,b>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_poisson -->
<!-- signatures: var_poisson(m) -->
### Function: var_poisson (m)

Retorna a variância de uma variável aleatória $Poisson(m)$,
com  $m>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

<!-- category: Statistics -->
<!-- keywords: var_rayleigh -->
<!-- signatures: var_rayleigh(b) -->
### Function: var_rayleigh (b)

Retorna a variância de uma variável aleatória $Rayleigh(b)$, com $b>0$.


A variável aleatória $Rayleigh(b)$ é equivalente a $Weibull(2,1/b)$,
embora quando Maxima não tiver informação disponível para pegar o resultado,
uma forma nominal baseada na variância de Weibull é retornada.








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

Retorna a variância de uma variável aleatória de Student $t(n)$, com $n>2$.







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

Retorna a variância de uma variável aleatória $Weibull(a,b)$,
com $a,b>0$. Para fazer uso dessa função, escreva
primeiramente `load("distrib")`.

