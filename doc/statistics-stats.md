## stats

<!-- category: Statistics -->
<!-- keywords: cdf_rank_sum -->
<!-- signatures: cdf_rank_sum(x, n, m) -->
### Function: cdf_rank_sum (x, n, m)

Cumulative distribution function of the exact distribution of the
rank sum statistic. Argument *x* is a real
number and *n* and *m* are both positive integers. 


See also `test_005frank_005fsum`.

See also: `test_rank_sum`.

<!-- category: Statistics -->
<!-- keywords: cdf_signed_rank -->
<!-- signatures: cdf_signed_rank(x, n) -->
### Function: cdf_signed_rank (x, n)

Cumulative distribution function of the exact distribution of the
signed rank statistic. Argument *x* is a real
number and *n* a positive integer. 


See also `test_005fsigned_005frank`.

See also: `test_signed_rank`.

<!-- category: Statistics -->
<!-- keywords: inference_result -->
<!-- signatures: inference_result(title, values, numbers) -->
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

<!-- category: Statistics -->
<!-- keywords: inferencep -->
<!-- signatures: inferencep(obj) -->
### Function: inferencep (obj)

Returns `true` or `false`, depending on whether *obj* is an
`inference_result` object or not.

<!-- category: Statistics -->
<!-- keywords: items_inference -->
<!-- signatures: items_inference(obj) -->
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

<!-- category: Statistics -->
<!-- keywords: linear_regression -->
<!-- signatures: linear_regression(x), linear_regression(xoption) -->
### Function: linear_regression (x)

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

<!-- category: Statistics -->
<!-- keywords: pdf_rank_sum -->
<!-- signatures: pdf_rank_sum(x, n, m) -->
### Function: pdf_rank_sum (x, n, m)

Probability density function of the exact distribution of the
rank sum statistic. Argument *x* is a real
number and *n* and *m* are both positive integers. 


See also `test_005frank_005fsum`.

See also: `test_rank_sum`.

<!-- category: Statistics -->
<!-- keywords: pdf_signed_rank -->
<!-- signatures: pdf_signed_rank(x, n) -->
### Function: pdf_signed_rank (x, n)

Probability density function of the exact distribution of the
signed rank statistic. Argument *x* is a real
number and *n* a positive integer.


See also `test_005fsigned_005frank`.

See also: `test_signed_rank`.

<!-- category: Statistics -->
<!-- keywords: stats_numer -->
<!-- signatures: stats_numer -->
### Variable: stats_numer

Default value: `true`


If `stats_numer` is `true`, inference statistical functions 
return their results in floating point numbers. If it is `false`,
results are given in symbolic and rational format.

<!-- category: Statistics -->
<!-- keywords: take_inference -->
<!-- signatures: take_inference(n, obj), take_inference(name, obj), take_inference(list, obj) -->
### Function: take_inference (n, obj)

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

<!-- category: Statistics -->
<!-- keywords: test_mean -->
<!-- signatures: test_mean(x), test_mean(x, options...) -->
### Function: test_mean (x)

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

<!-- category: Statistics -->
<!-- keywords: test_means_difference -->
<!-- signatures: test_means_difference(x1, x2), test_means_difference(x1, x2, options...) -->
### Function: test_means_difference (x1, x2)

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

<!-- category: Statistics -->
<!-- keywords: test_normality -->
<!-- signatures: test_normality(x) -->
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

<!-- category: Statistics -->
<!-- keywords: test_proportion -->
<!-- signatures: test_proportion(x, n), test_proportion(x, n, options...) -->
### Function: test_proportion (x, n)

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

<!-- category: Statistics -->
<!-- keywords: test_proportions_difference -->
<!-- signatures: test_proportions_difference(x1, n1, x2, n2), test_proportions_difference(x1, n1, x2, n2, options...) -->
### Function: test_proportions_difference (x1, n1, x2, n2)

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

<!-- category: Statistics -->
<!-- keywords: test_rank_sum -->
<!-- signatures: test_rank_sum(x1, x2), test_rank_sum(x1, x2, option) -->
### Function: test_rank_sum (x1, x2)

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

<!-- category: Statistics -->
<!-- keywords: test_sign -->
<!-- signatures: test_sign(x), test_sign(x, options...) -->
### Function: test_sign (x)

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

<!-- category: Statistics -->
<!-- keywords: test_signed_rank -->
<!-- signatures: test_signed_rank(x), test_signed_rank(x, options...) -->
### Function: test_signed_rank (x)

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

<!-- category: Statistics -->
<!-- keywords: test_variance -->
<!-- signatures: test_variance(x), test_variance(x, options, ...) -->
### Function: test_variance (x)

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

<!-- category: Statistics -->
<!-- keywords: test_variance_ratio -->
<!-- signatures: test_variance_ratio(x1, x2), test_variance_ratio(x1, x2, options...) -->
### Function: test_variance_ratio (x1, x2)

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

