## descriptive

<!-- category: Statistics -->
<!-- keywords: build_sample -->
<!-- signatures: build_sample(list), build_sample(matrix) -->
### Function: build_sample (list)

Builds a sample from a table of absolute frequencies.
The input table can be a matrix or a list of lists, all of
them of equal size. The number of columns or the length of
the lists must be greater than 1. The last element of each
row or list is interpreted as the absolute frequency.
The output is always a sample in matrix form.


Examples:


Univariate frequency table.









```maxima
(%i1) load ("descriptive")$
(%i2) sam1: build_sample([[6,1], [j,2], [2,1]]);
                       [ 6 ]
                       [   ]
                       [ j ]
(%o2)                  [   ]
                       [ j ]
                       [   ]
                       [ 2 ]
(%i3) mean(sam1);
                      2 j + 8
(%o3)                [-------]
                         4
(%i4) barsplot(sam1) $
```


Multivariate frequency table.









```maxima
(%i1) load ("descriptive")$
(%i2) sam2: build_sample([[6,3,1], [5,6,2], [u,2,1],[6,8,2]]) ;
                           [ 6  3 ]
                           [      ]
                           [ 5  6 ]
                           [      ]
                           [ 5  6 ]
(%o2)                      [      ]
                           [ u  2 ]
                           [      ]
                           [ 6  8 ]
                           [      ]
                           [ 6  8 ]
(%i3) cov(sam2);
       [   2                 2                            ]
       [  u  + 158   (u + 28)     2 u + 174   11 (u + 28) ]
       [  -------- - ---------    --------- - ----------- ]
(%o3)  [     6          36            6           12      ]
       [                                                  ]
       [ 2 u + 174   11 (u + 28)            21            ]
       [ --------- - -----------            --            ]
       [     6           12                 4             ]
(%i4) barsplot(sam2, grouping=stacked) $
```

<!-- category: Statistics -->
<!-- keywords: central_moment -->
<!-- signatures: central_moment(list, k), central_moment(matrix, k) -->
### Function: central_moment (list, k)

The central moment of order $k$, defined as


```maxima
n
                  ====
              1   \          _ k
              -    >    (x - x)
              n   /       i
                  ====
                  i = 1
```


$$
{{1\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^k}}}
$$


Example:



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

<!-- category: Statistics -->
<!-- keywords: continuous_freq -->
<!-- signatures: continuous_freq(list), continuous_freq(list, m) -->
### Function: continuous_freq (list)

The argument of `continuous_freq` must be a list of numbers.
Divides the range in intervals and counts how many values
are inside them.  The second argument is optional and either
equals the number of classes we want, `10` by default, or
equals a list containing the class limits and the number of
classes we want, or a list containing only the limits.
Argument *list* must be a list of (2 or 3) real numbers.
If sample values are all equal, this function returns only
one class of amplitude 2.


Examples:


Optional argument indicates the number of classes we want.
The first list in the output contains the interval limits, and
the second the corresponding counts: there are 16 digits inside 
the interval `[0, 1.8]`, 24 digits in `(1.8, 3.6]`, and so on.



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, 5);
(%o3) [[0, 1.8, 3.6, 5.4, 7.2, 9.0], [16, 24, 18, 17, 25]]
```


Optional argument indicates we want 7 classes with limits
`-2` and `12`:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, [-2,12,7]);
(%o3) [[- 2, 0, 2, 4, 6, 8, 10, 12], [8, 20, 22, 17, 20, 13, 0]]
```


Optional argument indicates we want the default number of classes with limits
`-2` and `12`:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, [-2,12]);

                3  4  11  18     32  39  46  53
(%o3)  [[- 2, - -, -, --, --, 5, --, --, --, --, 12], 
                5  5  5   5      5   5   5   5
               [0, 8, 20, 12, 18, 9, 8, 25, 0, 0]]
```

<!-- category: Statistics -->
<!-- keywords: cor -->
<!-- signatures: cor(matrix), cor(matrix, logical_value) -->
### Function: cor (matrix)

The correlation matrix of the multivariate sample.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) fpprintprec : 7 $
(%i3) s2 : read_matrix (file_search ("wind.data"))$

(%i4) cor (s2);
      [   1.0     .8476339  .8803515  .8239624  .7519506 ]
      [                                                  ]
      [ .8476339    1.0     .8735834  .6902622  0.782502 ]
      [                                                  ]
(%o4) [ .8803515  .8735834    1.0     .7764065  .8323358 ]
      [                                                  ]
      [ .8239624  .6902622  .7764065    1.0     .7293848 ]
      [                                                  ]
      [ .7519506  0.782502  .8323358  .7293848    1.0    ]
```


Function `cor` has an optional logical argument: `cor(x,true)` tells 
Maxima that `x` is the data matrix, making the same as `cor(x)`.  On 
the other hand, `cor(x,false)` means that `x` is not the data matrix, 
but the covariance matrix, avoiding its recalculation,



```maxima
(%i1) load ("descriptive")$
(%i2) fpprintprec : 7 $
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) s : cov1 (s2)$

(%i5) cor (s, false); /* this is faster */
      [   1.0     .8476339  .8803515  .8239624  .7519506 ]
      [                                                  ]
      [ .8476339    1.0     .8735834  .6902622  0.782502 ]
      [                                                  ]
(%o5) [ .8803515  .8735834    1.0     .7764065  .8323358 ]
      [                                                  ]
      [ .8239624  .6902622  .7764065    1.0     .7293848 ]
      [                                                  ]
      [ .7519506  0.782502  .8323358  .7293848    1.0    ]
```


See also `cov` and `cov1`.

<!-- category: Statistics -->
<!-- keywords: cov -->
<!-- signatures: cov(matrix) -->
### Function: cov (matrix)

The covariance matrix of the multivariate sample, defined as


```maxima
n
             ====
          1  \           _        _
      S = -   >    (X  - X) (X  - X)'
          n  /       j        j
             ====
             j = 1
```




where $X_j$ is the $j$-th row of the sample matrix.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec : 7$  /* change precision for pretty output */

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

<!-- category: Statistics -->
<!-- keywords: cov1 -->
<!-- signatures: cov1(matrix) -->
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




where $X_j$ is the $j$-th row of the sample matrix.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) fpprintprec : 7$ /* change precision for pretty output */

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

<!-- category: Statistics -->
<!-- keywords: cv -->
<!-- signatures: cv(list), cv(matrix) -->
### Function: cv (list)

The variation coefficient is the quotient between the sample standard deviation 
(`std`) and the `mean`,



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) cv (s1), numer;
(%o3)                   .6193977819764815

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) cv (s2);
(%o5) [.4192426091090204, .3829365309260502, 0.363779605385983, 
                            .3627381836021478, .3346021393989506]
```


See also functions `std` and `mean`.

<!-- category: Statistics -->
<!-- keywords: discrete_freq -->
<!-- signatures: discrete_freq(list) -->
### Function: discrete_freq (list)

Counts absolute frequencies in discrete samples, both numeric and categorical.
Its unique argument is a list,



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) discrete_freq (s1);

(%o3) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```


The first list gives the sample values and the second their absolute 
frequencies.  Commands `? col` and `? transpose` should help you to 
understand the last input.

<!-- category: Statistics -->
<!-- keywords: geometric_mean -->
<!-- signatures: geometric_mean(list), geometric_mean(matrix) -->
### Function: geometric_mean (list)

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


$$
\left(\prod_{i=1}^{n}{x_{i}}\right)^{{{1}\over{n}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$

(%i3) geometric_mean (y), numer;
(%o3)                   4.454845412337012

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) geometric_mean (s2);
(%o5) [8.82476274347979, 9.22652604739361, 10.0442675714889, 
                            14.61274126349021, 13.96184163444275]
```


See also functions `mean` and `harmonic_mean`.

<!-- category: Statistics -->
<!-- keywords: global_variances -->
<!-- signatures: global_variances(matrix), global_variances(matrix, logical_value) -->
### Function: global_variances (matrix)

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
*efective variance* `determinant(S_1)^(1/p)`, (defined in: Pena, D.
(2002) *Analisis de datos multivariantes*; McGraw-Hill, Madrid.)
- *
*efective standard deviation*: `determinant(S_1)^(1/(2*p))`.

where *p* is the dimension of the multivariate random variable and 
$S_1$ the covariance matrix returned by `cov1`.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) global_variances (s2);
(%o3) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608501, 6.636590811800795, 2.576158149609762]
```


Function `global_variances` has an optional logical argument: 
`global_variances (x, true)` tells Maxima that `x` is the data matrix, 
making the same as `global_variances(x)`.  On the other hand, 
`global_variances(x, false)` means that `x` is not the data matrix, 
but the covariance matrix, avoiding its recalculation,



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) s : cov1 (s2)$

(%i4) global_variances (s, false);
(%o4) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608501, 6.636590811800795, 2.576158149609762]
```


See also `cov` and `cov1`.

<!-- category: Statistics -->
<!-- keywords: harmonic_mean -->
<!-- signatures: harmonic_mean(list), harmonic_mean(matrix) -->
### Function: harmonic_mean (list)

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


$$
{{n}\over{\sum_{i=1}^{n}{{{1}\over{x_{i}}}}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) y : [5, 7, 2, 5, 9, 5, 6, 4, 9, 2, 4, 2, 5]$

(%i3) harmonic_mean (y), numer;
(%o3)                   3.901858027632205

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) harmonic_mean (s2);
(%o5) [6.948015590052786, 7.391967752360356, 9.055658197151745, 
                            13.44199028193692, 13.01439145898509]
```


See also functions `mean` and `geometric_mean`.

<!-- category: Statistics -->
<!-- keywords: kurtosis -->
<!-- signatures: kurtosis(list), kurtosis(matrix) -->
### Function: kurtosis (list)

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


$$
{{1\over{n s^4}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^4}}-3}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) kurtosis (s1), numer;
(%o3)                  - 1.273247946514421

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) kurtosis (s2);
(%o5) [- .2715445622195385, 0.119998784429451, 
   - .4275233490482861, - .6405361979019522, - .4952382132352935]
```


See also functions `mean`, `var` and `skewness`.

<!-- category: Statistics -->
<!-- keywords: list_correlations -->
<!-- signatures: list_correlations(matrix), list_correlations(matrix, logical_value) -->
### Function: list_correlations (matrix)

Function `list_correlations` returns a list of correlation measures:



- *
*precision matrix*: the inverse of the covariance matrix $S_1$,

```maxima
-1     ij
      S   = (s  )             
       1         i,j = 1,2,...,p
```

$$
{S_{1}^{-1}}={\left(s^{ij}\right)_{i,j=1,2,\ldots, p}}
$$
- *
*multiple correlation vector*:  $(R_1^2, R_2^2, ..., R_p^2)$, with 

```maxima
2          1
      R  = 1 - -------
       i        ii
               s   s
                    ii
```

$$
{R_{i}^{2}}={1-{{1}\over{s^{ii}s_{ii}}}}
$$
being an indicator of the goodness of fit of the linear multivariate regression 
model on $X_i$ when the rest of variables are used as regressors.
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

$$
{r_{ij.rest}}={-{{s^{ij}}\over \sqrt{s^{ii}s^{jj}}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) z : list_correlations (s2)$
(%i4) fpprintprec : 5$ /* for pretty output */

(%i5) z[1];  /* precision matrix */
      [  .38486   - .13856   - .15626   - .10239    .031179  ]
      [                                                      ]
      [ - .13856   .34107    - .15233    .038447   - .052842 ]
      [                                                      ]
(%o5) [ - .15626  - .15233    .47296    - .024816  - .10054  ]
      [                                                      ]
      [ - .10239   .038447   - .024816   .10937    - .034033 ]
      [                                                      ]
      [ .031179   - .052842  - .10054   - .034033   .14834   ]


(%i6) z[2];  /* multiple correlation vector */
(%o6)      [.85063, .80634, .86474, .71867, .72675]


(%i7) z[3];  /* partial correlation matrix */
      [  - 1.0     .38244   .36627   .49908   - .13049 ]
      [                                                ]
      [  .38244    - 1.0    .37927  - .19907   .23492  ]
      [                                                ]
(%o7) [  .36627    .37927   - 1.0    .10911    .37956  ]
      [                                                ]
      [  .49908   - .19907  .10911   - 1.0     .26719  ]
      [                                                ]
      [ - .13049   .23492   .37956   .26719    - 1.0   ]
```


Function `list_correlations` also has an optional logical argument: 
`list_correlations(x,true)` tells Maxima that `x` is the data matrix, 
making the same as `list_correlations(x)`.  On the other hand, 
`list_correlations(x,false)` means that `x` is not the data matrix, 
but the covariance matrix, avoiding its recalculation.


See also `cov` and `cov1`.

<!-- category: Statistics -->
<!-- keywords: maxi -->
<!-- signatures: maxi(list), maxi(matrix) -->
### Function: maxi (list)

This is the maximum value of the sample *list*,



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) maxi (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) maxi (s2);
(%o5)          [20.25, 21.46, 20.04, 29.63, 27.63]
```


See also function `mini`.

<!-- category: Statistics -->
<!-- keywords: mean -->
<!-- signatures: mean(list), mean(matrix) -->
### Function: mean (list)

This is the sample mean, defined as


```maxima
n
                     ====
             _   1   \
             x = -    >    x
                 n   /      i
                     ====
                     i = 1
```


$$
{\bar{x}={1\over{n}}{\sum_{i=1}^{n}{x_{i}}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) mean (s1);
                               471
(%o3)                          ---
                               100


(%i4) %, numer;
(%o4)                         4.71

(%i5) s2 : read_matrix (file_search ("wind.data"))$

(%i6) mean (s2);
(%o6)     [9.9485, 10.1607, 10.8685, 15.7166, 14.8441]
```

<!-- category: Statistics -->
<!-- keywords: mean_deviation -->
<!-- signatures: mean_deviation(list), mean_deviation(matrix) -->
### Function: mean_deviation (list)

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


$$
{{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-\bar{x}|}}}
$$


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
(%o5) [3.287959999999999, 3.075342, 3.23907, 4.715664000000001, 
                                               4.028546000000002]
```


See also function `mean`.

<!-- category: Statistics -->
<!-- keywords: median -->
<!-- signatures: median(list), median(matrix) -->
### Function: median (list)

Once the sample is ordered, if the sample size is odd the median is the central 
value, otherwise it is the mean of the two central values.


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
(%o5)         [10.06, 9.855, 10.73, 15.48, 14.105]
```


The median is the 1/2-quantile.


See also function `quantile`.

<!-- category: Statistics -->
<!-- keywords: median_deviation -->
<!-- signatures: median_deviation(list), median_deviation(matrix) -->
### Function: median_deviation (list)

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


$$
{{1\over{n}}{\sum_{i=1}^{n}{|x_{i}-med|}}}
$$

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
(%o5)           [2.75, 2.755, 3.08, 4.315, 3.31]
```


See also function `mean`.

<!-- category: Statistics -->
<!-- keywords: mini -->
<!-- signatures: mini(list), mini(matrix) -->
### Function: mini (list)

This is the minimum value of the sample *list*,



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) mini (s1);
(%o3)                           0

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) mini (s2);
(%o5)             [0.58, 0.5, 2.67, 5.25, 5.17]
```


See also function `maxi`.

<!-- category: Statistics -->
<!-- keywords: noncentral_moment -->
<!-- signatures: noncentral_moment(list, k), noncentral_moment(matrix, k) -->
### Function: noncentral_moment (list, k)

The non central moment of order $k$, defined as


```maxima
n
                     ====
                 1   \      k
                 -    >    x
                 n   /      i
                     ====
                     i = 1
```


$$
{{1\over{n}}{\sum_{i=1}^{n}{x_{i}^k}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) noncentral_moment (s1, 1), numer; /* the mean */
(%o3)                         4.71


(%i5) s2 : read_matrix (file_search ("wind.data"))$


(%i6) noncentral_moment (s2, 5);
(%o6) [319793.8724761505, 320532.1923892463,
      391249.5621381556, 2502278.205988911, 1691881.797742255]
```


See also function `central_moment`.

<!-- category: Statistics -->
<!-- keywords: pearson_skewness -->
<!-- signatures: pearson_skewness(list), pearson_skewness(matrix) -->
### Function: pearson_skewness (list)

Pearson’s skewness coefficient, defined as 


```maxima
_
             3 (x - med)
             -----------
                  s
```


$$
{{3\,\left(\bar{x}-med\right)}\over{s}}
$$

where *med* is the median of *list*.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) pearson_skewness (s1), numer;
(%o3)                   .2159484029093895

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) pearson_skewness (s2);
(%o5) [- .08019976629211892, .2357036272952649, 
         .1050904062491204, .1245042340592368, .4464181795804519]
```


See also functions `mean`, `var` and `median`.

<!-- category: Statistics -->
<!-- keywords: qrange -->
<!-- signatures: qrange(list), qrange(matrix) -->
### Function: qrange (list)

The interquartilic range is the difference between the third and first 
quartiles, `quantile(list,3/4) - quantile(list,1/4)`,



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

<!-- category: Statistics -->
<!-- keywords: quantile -->
<!-- signatures: quantile(list, p), quantile(matrix, p) -->
### Function: quantile (list, p)

This is the *p*-quantile, with *p* a number in $[0, 1]$, of the 
sample *list*.  Although there are several definitions for the sample 
quantile (Hyndman, R. J., Fan, Y. (1996) *Sample quantiles in statistical 
packages*.  American Statistician, 50, 361-365), the one based on linear 
interpolation is implemented in package `descriptive`.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) /* 1st and 3rd quartiles */
         [quantile (s1, 1/4), quantile (s1, 3/4)], numer;
(%o3)                      [2.0, 7.25]

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) quantile (s2, 1/4);
(%o5)    [7.2575, 7.477500000000001, 7.82, 11.28, 11.48]
```

<!-- category: Statistics -->
<!-- keywords: quartile_skewness -->
<!-- signatures: quartile_skewness(list), quartile_skewness(matrix) -->
### Function: quartile_skewness (list)

The quartile skewness coefficient, defined as 


```maxima
c    - 2 c    + c
                3/4      1/2    1/4
               --------------------
                   c    - c
                    3/4    1/4
```


$$
{{c_{{{3}\over{4}}}-2\,c_{{{1}\over{2}}}+c_{{{1}\over{4}}}}\over{c
 _{{{3}\over{4}}}-c_{{{1}\over{4}}}}}
$$

where $c_p$ is the *p*-quantile of sample *list*.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) quartile_skewness (s1), numer;
(%o3)                  .04761904761904762

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) quartile_skewness (s2);
(%o5) [- 0.0408542246982353, .1467025572005382, 
       0.0336239103362392, .03780068728522298, .2105263157894735]
```


See also function `quantile`.

<!-- category: Statistics -->
<!-- keywords: range -->
<!-- signatures: range(list), range(matrix) -->
### Function: range (list)

The range is the difference between the extreme values.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) range (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) range (s2);
(%o5)          [19.67, 20.96, 17.37, 24.38, 22.46]
```

<!-- category: Statistics -->
<!-- keywords: skewness -->
<!-- signatures: skewness(list), skewness(matrix) -->
### Function: skewness (list)

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


$$
{{1\over{n s^3}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^3}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) skewness (s1), numer;
(%o3)                  .009196180476450424

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) skewness (s2);
(%o5) [.1580509020000978, .2926379232061854, .09242174416107717, 
                            .2059984348148687, .2142520248890831]
```


See also functions `mean`, `var` and `kurtosis`.

<!-- category: Statistics -->
<!-- keywords: std -->
<!-- signatures: std(list), std(matrix) -->
### Function: std (list)

This is the the square root of function `var`, the variance with 
denominator $n$.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) std (s1), numer;
(%o3)                   2.902740084816414

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) std (s2);
(%o5) [4.149928523480858, 3.871399812729241, 3.933920277534866, 
                            5.672434260526957, 4.941970881136392]
```


See also functions `var` and `std1`.

<!-- category: Statistics -->
<!-- keywords: std1 -->
<!-- signatures: std1(list), std1(matrix) -->
### Function: std1 (list)

This is the the square root of function `var1`, the variance with 
denominator $n-1$.


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) std1 (s1), numer;
(%o3)                   2.917363553109228

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) std1 (s2);
(%o5) [4.170835096721089, 3.89090320978032, 3.953738641137555, 
                            5.701010936401517, 4.966867617451963]
```


See also functions `var1` and `std`.

<!-- category: Statistics -->
<!-- keywords: subsample -->
<!-- signatures: subsample(data_matrix, predicate_function), subsample(data_matrix, predicate_function, col_num1, col_num2, ...) -->
### Function: subsample (data_matrix, predicate_function)

This is a sort of variant of the Maxima `submatrix` function.  The first 
argument is the data matrix, the second is a predicate function and optional 
additional arguments are the numbers of the columns to be taken.  Its behaviour 
is better understood with examples.


These are multivariate records in which the wind speed in the first 
meteorological station were greater than 18.  See that in the lambda expression 
the *i*-th component is refered to as `v[i]`.



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) subsample (s2, lambda([v], v[1] > 18));

              [ 19.38  15.37  15.12  23.09  25.25 ]
              [                                   ]
              [ 18.29  18.66  19.08  26.08  27.63 ]
(%o3)         [                                   ]
              [ 20.25  21.46  19.95  27.71  23.38 ]
              [                                   ]
              [ 18.79  18.96  14.46  26.38  21.84 ]
```


In the following example, we request only the first, second and fifth 
components of those records with wind speeds greater or equal than 16 in 
station number 1 and less than 25 knots in station number 4.  The sample
contains only data from stations 1, 2 and 5.  In this case, the predicate 
function is defined as an ordinary Maxima function.



```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) g(x):= x[1] >= 16 and x[4] < 25$
(%i4) subsample (s2, g, 1, 2, 5);

                     [ 19.38  15.37  25.25 ]
                     [                     ]
                     [ 17.33  14.67  19.58 ]
(%o4)                [                     ]
                     [ 16.92  13.21  21.21 ]
                     [                     ]
                     [ 17.25  18.46  23.87 ]
```


Here is an example with the categorical variables of `biomed.data`.
We want the records corresponding to those patients in group `B`
who are older than 38 years.



```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) h(u):= u[1] = B and u[2] > 38 $
(%i4) subsample (s3, h);

                [ B  39  28.0  102.3  17.1  146 ]
                [                               ]
                [ B  39  21.0  92.4   10.3  197 ]
                [                               ]
                [ B  39  23.0  111.5  10.0  133 ]
                [                               ]
                [ B  39  26.0  92.6   12.3  196 ]
(%o4)           [                               ]
                [ B  39  25.0  98.7   10.0  174 ]
                [                               ]
                [ B  39  21.0  93.2   5.9   181 ]
                [                               ]
                [ B  39  18.0  95.0   11.3  66  ]
                [                               ]
                [ B  39  39.0  88.5   7.6   168 ]
```


Probably, the statistical analysis will involve only the blood measures,



```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) subsample (s3, lambda([v], v[1] = B and v[2] > 38),
                 3, 4, 5, 6);

                   [ 28.0  102.3  17.1  146 ]
                   [                        ]
                   [ 21.0  92.4   10.3  197 ]
                   [                        ]
                   [ 23.0  111.5  10.0  133 ]
                   [                        ]
                   [ 26.0  92.6   12.3  196 ]
(%o3)              [                        ]
                   [ 25.0  98.7   10.0  174 ]
                   [                        ]
                   [ 21.0  93.2   5.9   181 ]
                   [                        ]
                   [ 18.0  95.0   11.3  66  ]
                   [                        ]
                   [ 39.0  88.5   7.6   168 ]
```


This is the multivariate mean of `s3`,



```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) mean (s3);

       65 B + 35 A  317          6 NA + 8144.999999999999
(%o3) [-----------, ---, 87.178, ------------------------, 
           100      10                     100
                                                    3 NA + 19587
                                            18.123, ------------]
                                                        100
```


Here, the first component is meaningless, since `A` and `B` are 
categorical, the second component is the mean age of individuals in rational 
form, and the fourth and last values exhibit some strange behaviour.  This is 
because symbol `NA` is used here to indicate *non available* data, 
and the two means are nonsense.  A possible solution would be to take out from 
the matrix those rows with `NA` symbols, although this deserves some 
loss of information.



```maxima
(%i1) load ("descriptive")$
(%i2) s3 : read_matrix (file_search ("biomed.data"))$
(%i3) g(v):= v[4] # NA and v[6] # NA $
(%i4) mean (subsample (s3, g, 3, 4, 5, 6));

(%o4) [79.4923076923077, 86.2032967032967, 16.93186813186813, 
                                                            2514
                                                            ----]
                                                             13
```

<!-- category: Statistics -->
<!-- keywords: var -->
<!-- signatures: var(list), var(matrix) -->
### Function: var (list)

This is the sample variance, defined as


```maxima
n
                   ====
           2   1   \          _ 2
          s  = -    >    (x - x)
               n   /       i
                   ====
                   i = 1
```


$$
{{1}\over{n}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var (s1), numer;
(%o3)                   8.425899999999999
```


See also function `var1`.

<!-- category: Statistics -->
<!-- keywords: var1 -->
<!-- signatures: var1(list), var1(matrix) -->
### Function: var1 (list)

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


$$
{{1\over{n-1}}{\sum_{i=1}^{n}{(x_{i}-\bar{x})^2}}}
$$


Example:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var1 (s1), numer;
(%o3)                    8.5110101010101

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) var1 (s2);
(%o5) [17.39586540404041, 15.13912778787879, 15.63204924242424, 
                            32.50152569696971, 24.66977392929294]
```


See also function `var`.

