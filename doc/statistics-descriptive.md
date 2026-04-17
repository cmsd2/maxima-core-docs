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
(%o2)                         [   ]
                              [ j ]
                              [   ]
                              [ 2 ]


(%i3) mean(sam1);
                              j + 4
(%o3)                        [-----]
                                2

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
(%o2)                       [      ]
                            [ u  2 ]
                            [      ]
                            [ 6  8 ]
                            [      ]
                            [ 6  8 ]


(%i3) cov(sam2);
      [   2                 2                            ]
      [  u  + 158   (u + 28)     2 u + 174   11 (u + 28) ]
      [  -------- - ---------    --------- - ----------- ]
(%o3) [     6          36            6           12      ]
      [                                                  ]
      [ 2 u + 174   11 (u + 28)            21            ]
      [ --------- - -----------            --            ]
      [     6           12                 4             ]

(%i4) barsplot(sam2, grouping=stacked) $
```

<!-- category: Statistics -->
<!-- keywords: cdf_empirical -->
<!-- signatures: cdf_empirical(list, option...), cdf_empirical(matrix, option...) -->
### Function: cdf_empirical (list, option...)

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

<!-- category: Statistics -->
<!-- keywords: central_moment -->
<!-- signatures: central_moment(x, k), central_moment(x, k, w) -->
### Function: central_moment (x, k)

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

<!-- category: Statistics -->
<!-- keywords: continuous_freq -->
<!-- signatures: continuous_freq(data), continuous_freq(data, m) -->
### Function: continuous_freq (data)

Divides the range of *data* into intervals,
and counts how many values fall into each one.


A value *x* falls into an interval with left and right endpoints *a* and *b*
if and only if `x > a` and `x <= b`,
except for the first (least or leftmost) interval,
for which `x >= a` and `x <= b`.
That is, an interval excludes its left endpoint and includes its right endpoint,
except for the first interval, which includes both the left and right endpoints.


*data* must be a list of numbers,
or 1-dimensional array (as created by `make_array`).


*m* is optional, and equals either the number of classes (10 by default),
or a list of two elements (the least and greatest values to be counted),
or a list of three elements (the least and greatest values to be counted, and the number of classes),
or a set containing the endpoints of the class intervals.


It is assumed that class intervals are contiguous.
That is, the right endpoint of one interval is equal to the left endpoint of the next.


`continuous_freq` returns a list of two lists.
The first list comprises all the endpoints of the class intervals,
concatenated into a single list.
The second list contains the class counts for the intervals corresponding to elements of the first list.


If sample values are all equal, this function returns exactly
one class of width 2.


Examples:


Optional argument indicates the number of classes we want.
The first list in the output contains the interval limits, and
the second the corresponding counts: there are 16 digits inside 
the interval `[0, 1.8]`, 24 digits in `(1.8, 3.6]`, and so on.








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) continuous_freq (s1, 5);
               9  18  27  36
(%o3)     [[0, -, --, --, --, 9], [16, 24, 18, 17, 25]]
               5  5   5   5
```


Optional argument indicates we want 7 classes with limits
-2 and 12:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) continuous_freq (s1, [-2,12,7]);
(%o3) [[- 2, 0, 2, 4, 6, 8, 10, 12], [8, 20, 22, 17, 20, 13, 0]]
```


Optional argument indicates we want the default number of classes with limits
-2 and 12:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) continuous_freq (s1, [-2,12]);
               3  4  11  18     32  39  46  53
(%o3) [[- 2, - -, -, --, --, 5, --, --, --, --, 12], 
               5  5  5   5      5   5   5   5
                              [0, 8, 20, 12, 18, 9, 8, 25, 0, 0]]
```


The first argument may be an array.










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) a1 : make_array (fixnum, length (s1)) $

(%i4) fillarray (a1, s1);
(%o4) {Lisp Array: #(3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2\
 6 4 3 3 8 3 2 7 9 5
               0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7\
 4 9 4 4 5 9 2
               3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8\
 2 5 3 4 2 1 1
               7 0 6 7)}


(%i5) continuous_freq (a1);
           9   9  27  18  9  27  63  36  81
(%o5) [[0, --, -, --, --, -, --, --, --, --, 9], 
           10  5  10  5   2  5   10  5   10
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```

<!-- category: Statistics -->
<!-- keywords: cor -->
<!-- signatures: cor(matrix), cor(matrix, logical_value) -->
### Function: cor (matrix)

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

<!-- category: Statistics -->
<!-- keywords: cov -->
<!-- signatures: cov(X), cov(X, w) -->
### Function: cov (X)

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

<!-- category: Statistics -->
<!-- keywords: cv -->
<!-- signatures: cv(list), cv(matrix) -->
### Function: cv (list)

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

<!-- category: Statistics -->
<!-- keywords: discrete_freq -->
<!-- signatures: discrete_freq(data) -->
### Function: discrete_freq (data)

Counts absolute frequencies in discrete samples, both numeric and categorical. Its sole argument is a list,
or 1-dimensional array (as created by `make_array`).


Examples:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) discrete_freq (s1);
(%o3) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```


In the return value,
the first list gives the sample values, and the second, their absolute frequencies.


The argument may be an array.










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) a1 : make_array (fixnum, length (s1)) $

(%i4) fillarray (a1, s1);
(%o4) {Lisp Array: #(3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2\
 6 4 3 3 8 3 2 7 9 5
               0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7\
 4 9 4 4 5 9 2
               3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8\
 2 5 3 4 2 1 1
               7 0 6 7)}


(%i5) discrete_freq (a1);
(%o5) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```

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

<!-- category: Statistics -->
<!-- keywords: global_variances -->
<!-- signatures: global_variances(matrix), global_variances(matrix, options...) -->
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

<!-- category: Statistics -->
<!-- keywords: km -->
<!-- signatures: km(list, option...), km(matrix, option...) -->
### Function: km (list, option...)

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

<!-- category: Statistics -->
<!-- keywords: list_correlations -->
<!-- signatures: list_correlations(matrix), list_correlations(matrix, options...) -->
### Function: list_correlations (matrix)

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

<!-- category: Statistics -->
<!-- keywords: mean -->
<!-- signatures: mean(x), mean(x, w) -->
### Function: mean (x)

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

<!-- category: Statistics -->
<!-- keywords: median -->
<!-- signatures: median(list), median(matrix) -->
### Function: median (list)

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

<!-- category: Statistics -->
<!-- keywords: noncentral_moment -->
<!-- signatures: noncentral_moment(x, k), noncentral_moment(x, k, w) -->
### Function: noncentral_moment (x, k)

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

<!-- category: Statistics -->
<!-- keywords: principal_components -->
<!-- signatures: principal_components(matrix), principal_components(matrix, options...) -->
### Function: principal_components (matrix)

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

<!-- category: Statistics -->
<!-- keywords: qrange -->
<!-- signatures: qrange(x) -->
### Function: qrange (x)

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

<!-- category: Statistics -->
<!-- keywords: quantile -->
<!-- signatures: quantile(list, p), quantile(matrix, p) -->
### Function: quantile (list, p)

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
(%o5)   [19.67, 20.96, 17.369999999999997, 24.38, 22.46]
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

<!-- category: Statistics -->
<!-- keywords: smax -->
<!-- signatures: smax(list), smax(matrix) -->
### Function: smax (list)

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

<!-- category: Statistics -->
<!-- keywords: smin -->
<!-- signatures: smin(list), smin(matrix) -->
### Function: smin (list)

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

<!-- category: Statistics -->
<!-- keywords: standardize -->
<!-- signatures: standardize(list), standardize(matrix) -->
### Function: standardize (list)

Subtracts to each element of the list the sample mean and divides
the result by the standard deviation. When the input is a matrix,
`standardize` subtracts to each row the multivariate mean, and then
divides each component by the corresponding standard deviation.

<!-- category: Statistics -->
<!-- keywords: std -->
<!-- signatures: std(x), std(x, w) -->
### Function: std (x)

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

<!-- category: Statistics -->
<!-- keywords: std1 -->
<!-- signatures: std1(list), std1(matrix) -->
### Function: std1 (list)

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

<!-- category: Statistics -->
<!-- keywords: subsample -->
<!-- signatures: subsample(data_matrix, predicate_function), subsample(data_matrix, predicate_function, col_num1, col_num2, ...) -->
### Function: subsample (data_matrix, predicate_function)

This is a sort of variant of the Maxima `submatrix` function.
The first argument is the data matrix, the second is a predicate function
and optional additional arguments are the numbers of the columns to be taken.


Examples:


These are multivariate records in which the wind speed
in the first meteorological station were greater than 18.
See that in the lambda expression the *i*-th component is
referred to as `v[i]`.








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
components of those records with wind speeds greater or equal than 16
in station number 1 and less than 25 knots in station number 4. The sample
contains only data from stations 1, 2 and 5. In this case,
the predicate function is defined as an ordinary Maxima function.









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
       13 B + 7 A  317
(%o3) [----------, ---, 87.178, 0.06 NA + 81.44999999999999, 
           20      10
                                                    3 NA + 19587
                                18.122999999999998, ------------]
                                                        100
```


Here, the first component is meaningless, since `A` and `B` are categorical, the second component is the mean age of individuals in rational form, and the fourth and last values exhibit some strange behaviour. This is because symbol `NA` is used here to indicate *non available* data, and the two means are nonsense. A possible solution would be to take out from the matrix those rows with `NA` symbols, although this deserves some loss of information.









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
<!-- keywords: transform_sample -->
<!-- signatures: transform_sample(matrix, varlist, exprlist) -->
### Function: transform_sample (matrix, varlist, exprlist)

Transforms the sample *matrix*, where each column is called according to
*varlist*, following expressions in *exprlist*.


Examples:


The second argument assigns names to the three columns. With these names,
a list of expressions define the transformation of the sample.



```maxima
(%i1) load ("descriptive")$
(%i2) data: matrix([3,2,7],[3,7,2],[8,2,4],[5,2,4]) $

(%i3) transform_sample(data, [a,b,c], [c, a*b, log(a)]);
                               [ 7  6   log(3) ]
                               [               ]
                               [ 2  21  log(3) ]
(%o3)                          [               ]
                               [ 4  16  log(8) ]
                               [               ]
                               [ 4  10  log(5) ]
```


Add a constant column and remove the third variable.



```maxima
(%i1) load ("descriptive")$
(%i2) data: matrix([3,2,7],[3,7,2],[8,2,4],[5,2,4]) $
(%i3) transform_sample(data, [a,b,c], [makelist(1,k,length(data)),a,b]);

                                  [ 1  3  2 ]
                                  [         ]
                                  [ 1  3  7 ]
(%o3)                             [         ]
                                  [ 1  8  2 ]
                                  [         ]
                                  [ 1  5  2 ]
```

<!-- category: Statistics -->
<!-- keywords: var -->
<!-- signatures: var(x), var(x, w) -->
### Function: var (x)

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

