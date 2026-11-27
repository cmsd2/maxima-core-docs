## descriptive

<!-- category: Statistics -->
<!-- keywords: central_moment -->
<!-- signatures: central_moment(list, k), central_moment(matrix, k) -->
### Function: central_moment (list, k)

次数$k$の中心モーメントです。以下のように定義されます。


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


例:










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


関数`noncentral_moment`と`mean`も参照してください。

<!-- category: Statistics -->
<!-- keywords: continuous_freq -->
<!-- signatures: continuous_freq(list), continuous_freq(list, m) -->
### Function: continuous_freq (list)

`continuous_freq`の引数は数のリストでなければいけません。
範囲を区間に分割し、それらの中に値がいくつあるか数えます。
二番目の引数はオプションで、
欲しいクラス数(デフォルトが10)か、
クラス境界と欲しいクラスを含むリストか
境界だけ含むリストのいずれかです。
引数 *list*は(2個か3個の)実数のリストでなければいけません。
もしサンプル値がすべて等しいなら、この関数は振幅2の1クラスだけ返します。


例:


オプション引数は欲しいクラス数を示します。
出力の最初のリストは区間境界を含み、二番目は対応する個数を含みます:
区間`[0, 1.8]`すなわち0か1である桁が16あり、
`(1.8, 3.6]`すなわち2か3である桁が24あり、など。








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, 5);
(%o3) [[0, 1.8, 3.6, 5.4, 7.2, 9.0], [16, 24, 18, 17, 25]]
```


オプション引数は、境界-2と12を持つクラスを7個欲しいことを示します。








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) continuous_freq (s1, [-2,12,7]);
(%o3) [[- 2, 0, 2, 4, 6, 8, 10, 12], [8, 20, 22, 17, 20, 13, 0]]
```


オプション引数は、境界-2と12を持つクラスをデフォルト個欲しいことを示します:








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

多変量標本の相関行列です。


例:









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


関数`cor`はオプションの論理引数を取ります:
`cor(x,true)`は、
Maximaに`x`がデータ行列であることを伝え、`cor(x)`と同様に作られます。
一方、`cor(x,false)`は
`x`がデータ行列ではなく、共分散行列であることを意味し、再計算は避けられます。










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


`cov`と`cov1`も参照してください。

<!-- category: Statistics -->
<!-- keywords: cov -->
<!-- signatures: cov(matrix) -->
### Function: cov (matrix)

多変量標本の共分散行列です。以下のように定義されます。


```maxima
n
             ====
          1  \           _        _
      S = -   >    (X  - X) (X  - X)'
          n  /       j        j
             ====
             j = 1
```


$$
{S={1\over{n}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}
$$

ここで$X_j$は標本行列の$j$番目の行です。


例:









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


関数`cov1`も参照してください。

<!-- category: Statistics -->
<!-- keywords: cov1 -->
<!-- signatures: cov1(matrix) -->
### Function: cov1 (matrix)

多変量標本の共分散行列です。以下のように定義されます。


```maxima
n
             ====
         1   \           _        _
   S  = ---   >    (X  - X) (X  - X)'
    1   n-1  /       j        j
             ====
             j = 1
```


$$
{{1\over{n-1}}{\sum_{j=1}^{n}{\left(X_{j}-\bar{X}\right)\,\left(X_{j}-\bar{X}\right)'}}}
$$

ここで$X_j$は標本行列の$j$番目の行です。


例:









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


関数`cov`も参照してください。

<!-- category: Statistics -->
<!-- keywords: cv -->
<!-- signatures: cv(list), cv(matrix) -->
### Function: cv (list)

変動係数は標本標準偏差(`std`)を平均`mean`で割った商です。









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


関数`std`と`mean`も参照してください。

<!-- category: Statistics -->
<!-- keywords: discrete_freq -->
<!-- signatures: discrete_freq(list) -->
### Function: discrete_freq (list)

数値的、記述的両方の離散標本の中の絶対頻度を数えます。
唯一の引数はリストです。








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) discrete_freq (s1);
(%o3) [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                             [8, 8, 12, 12, 10, 8, 9, 8, 12, 13]]
```


最初のリストは標本値を与え、二番目はそれらの絶対頻度を与えます。
コマンド`? col`と`? transpose`は最後の入力を理解するのを助けるはずです。

<!-- category: Statistics -->
<!-- keywords: geometric_mean -->
<!-- signatures: geometric_mean(list), geometric_mean(matrix) -->
### Function: geometric_mean (list)

幾何平均です。以下のように定義されます。


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


例:










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


関数`mean`と`harmonic_mean`も参照してください。

<!-- category: Statistics -->
<!-- keywords: global_variances -->
<!-- signatures: global_variances(matrix), global_variances(matrix, logical_value) -->
### Function: global_variances (matrix)

関数`global_variances`は大域分散尺度のリストを返します:



- *
*total variance*: `trace(S_1)`,
- *
*mean variance*: `trace(S_1)/p`,
- *
*generalized variance*: `determinant(S_1)`,
- *
*generalized standard deviation*: `sqrt(determinant(S_1))`,
- *
*efective variance* `determinant(S_1)^(1/p)`, (以下の文献で定義されています: Pena, D. (2002) *Analisis de datos multivariantes*; McGraw-Hill, Madrid.)
- *
*efective standard deviation*: `determinant(S_1)^(1/(2*p))`.

ここで*p*は多変量確率変数の次元であり、
$S_1$は`cov1`が返す共分散行列です。


例:








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) global_variances (s2);
(%o3) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608501, 6.636590811800795, 2.576158149609762]
```


関数`global_variances`はオプションの論理引数を取ります:
`global_variances(x,true)`は、
Maximaに`x`がデータ行列であることを伝え、`global_variances(x)`と同様に作られます。
一方、`global_variances(x,false)`は
`x`がデータ行列ではなく、共分散行列であることを意味し、再計算は避けられます。









```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) s : cov1 (s2)$

(%i4) global_variances (s, false);
(%o4) [105.338342060606, 21.06766841212119, 12874.34690469686, 
         113.4651792608501, 6.636590811800795, 2.576158149609762]
```


`cov`と`cov1`も参照してください。

<!-- category: Statistics -->
<!-- keywords: harmonic_mean -->
<!-- signatures: harmonic_mean(list), harmonic_mean(matrix) -->
### Function: harmonic_mean (list)

調和平均です。以下のように定義されます。


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


例:










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


関数`mean`と`geometric_mean`も参照してください。

<!-- category: Statistics -->
<!-- keywords: kurtosis -->
<!-- signatures: kurtosis(list), kurtosis(matrix) -->
### Function: kurtosis (list)

尖度係数です。以下のように定義されます。


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


例:










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


関数`mean`, `var`, `skewness`も参照してください。

<!-- category: Statistics -->
<!-- keywords: list_correlations -->
<!-- signatures: list_correlations(matrix), list_correlations(matrix, logical_value) -->
### Function: list_correlations (matrix)

関数`list_correlations`は相関尺度のリストを返します:



- *
*precision matrix*: 共分散行列$S_1$の逆行列,

```maxima
-1     ij
      S   = (s  )             
       1         i,j = 1,2,...,p
```

$$
{S_{1}^{-1}}={\left(s^{ij}\right)_{i,j=1,2,\ldots, p}}
$$
- *
*multiple correlation vector*:  $(R_1^2, R_2^2, ..., R_p^2)$,

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
変数の残りが独立変数として使われるとき
これらは$X_i$上の線形多変量回帰モデルの適合度の指標です。
- *
*partial correlation matrix*: $(i, j)$成分が以下の行列

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


例:












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


関数`list_correlations`もオプションの論理引数を取ります:
`list_correlations(x,true)`は、
Maximaに`x`がデータ行列であることを伝え、
`list_correlations(x)`と同様に作られます。
一方、`list_correlations(x,false)`は
`x`がデータ行列ではなく、共分散行列であることを意味し、再計算は避けられます。


`cov`と`cov1`も参照してください。

<!-- category: Statistics -->
<!-- keywords: mean -->
<!-- signatures: mean(list), mean(matrix) -->
### Function: mean (list)

これは標本平均です。以下のように定義されます。


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


例:











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

平均偏差です。以下のように定義されます。


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


例:










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


関数`mean`も参照してください。

<!-- category: Statistics -->
<!-- keywords: median -->
<!-- signatures: median(list), median(matrix) -->
### Function: median (list)

一旦標本が順に並べられると、
もし標本サイズが奇数ならメジアンは中央値であり、
そうでなければ2つの中央値の平均です。


例:










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


メジアンは1/2分位数です。


関数`quantile`も参照してください。

<!-- category: Statistics -->
<!-- keywords: median_deviation -->
<!-- signatures: median_deviation(list), median_deviation(matrix) -->
### Function: median_deviation (list)

メジアン偏差です。以下のように定義されます。


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

ここで`med`は*list*のメジアンです。


例:










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


関数`mean`も参照してください。

<!-- category: Statistics -->
<!-- keywords: noncentral_moment -->
<!-- signatures: noncentral_moment(list, k), noncentral_moment(matrix, k) -->
### Function: noncentral_moment (list, k)

次数$k$の非中心モーメントです。以下のように定義されます。


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


例:










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


関数`central_moment`も参照してください。

<!-- category: Statistics -->
<!-- keywords: pearson_skewness -->
<!-- signatures: pearson_skewness(list), pearson_skewness(matrix) -->
### Function: pearson_skewness (list)

Pearsonの歪度係数です。以下のように定義されます。


```maxima
_
             3 (x - med)
             -----------
                  s
```


$$
{{3\,\left(\bar{x}-med\right)}\over{s}}
$$

ここで *med*は*list*のメジアンです。


例:










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


関数`mean`, `var`, `median`も参照してください。

<!-- category: Statistics -->
<!-- keywords: qrange -->
<!-- signatures: qrange(list), qrange(matrix) -->
### Function: qrange (list)

四分位範囲は
三番目と一番目の分位数の差
`quantile(list,3/4) - quantile(list,1/4)`
です。










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


関数`quantile`も参照してください。

<!-- category: Statistics -->
<!-- keywords: quantile -->
<!-- signatures: quantile(list, p), quantile(matrix, p) -->
### Function: quantile (list, p)

これは標本*list*の*p*分位数です。*p*は$[0, 1]$の範囲の数です。
標本分位数にはいくつかの定義がありますが
(Hyndman, R. J., Fan, Y. (1996) *Sample quantiles in statistical packages*. American Statistician, 50, 361-365)、
パッケージ`descriptive`では線形内挿に基づいたものが実装されています。


例:











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

分位歪度係数です。以下のように定義されます。


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

ここで$c_p$は標本*list*の*p*分位数です。


例:










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


関数`quantile`も参照してください。

<!-- category: Statistics -->
<!-- keywords: range -->
<!-- signatures: range(list), range(matrix) -->
### Function: range (list)

範囲は極値の差です。


例:










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

歪度係数です。以下のように定義されます。


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


例:










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


関数`mean`, `var`, `kurtosis`も参照してください。

<!-- category: Statistics -->
<!-- keywords: smax -->
<!-- signatures: smax(list), smax(matrix) -->
### Function: smax (list)

これは標本*list*の最大値です。
引数が行列の時、
`smax`は
統計変数に関連付けられた列の最大値を含むリストを返します。










```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) smax (s1);
(%o3)                           9

(%i4) s2 : read_matrix (file_search ("wind.data"))$

(%i5) smax (s2);
(%o5)          [20.25, 21.46, 20.04, 29.63, 27.63]
```


関数`smin`も参照してください。

<!-- category: Statistics -->
<!-- keywords: smin -->
<!-- signatures: smin(list), smin(matrix) -->
### Function: smin (list)

これは標本*list*の最小値です。
引数が行列の時、
`smin`は
統計変数に関連付けられた列の最小値を含むリストを返します。










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

<!-- category: Statistics -->
<!-- keywords: std -->
<!-- signatures: std(list), std(matrix) -->
### Function: std (list)

これは分母$n$の分散である関数`var`の平方根です。


例:










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


関数`var`と`std1`も参照してください。

<!-- category: Statistics -->
<!-- keywords: std1 -->
<!-- signatures: std1(list), std1(matrix) -->
### Function: std1 (list)

これは分母$n-1$の分散である関数`var1`の平方根です。


例:










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

これはMaxima `submatrix`関数の変形の一種です。
最初の引数はデータ行列であり、二番目は述語関数であり、
オプションの付加引数は返す列の番号です。
その振る舞いは例を使ってよりよく理解されます。


以下は最初の測候所での風速が18より大きかった多変量レコードです。
ラムダ式の中で*i*番目の成分は`v[i]`として参照されることを参考にしてください。







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


以下の例では、測候所番号1で16以上で、かつ、測候所番号4で25ノットより小さな風速
のレコードの一番目、二番目、五番目の成分だけをリクエストします。
標本は、測候所1, 2, 5からのデータだけを含みます。
この場合、述語関数は通常のMaxima関数として定義されます。








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


以下は`biomed.data`のカテゴリ変数の例です。
38歳より年上のグループ`B`の患者に対応するレコードが欲しいです。








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


統計解析には血圧だけを使うかもしれません。








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


いかは`s3`の多変量平均です。







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


ここで、一番目の成分は、`A`と`B`はカテゴリなので意味がなく、
二番目の成分は個々人の平均の歳の有理表現であり、
四番目と最後の値はある奇妙な振る舞いを示しています。
これは、
This is because symbol 
シンボル`NA`が*non available*データを示すようにここで使われているからで、
二つの平均は無意味です。
情報のある種の喪失を意味しますが、
可能な解は`NA`シンボルを持つ行を行列から取り除くことです。








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

これは標本分散です。以下のように定義されます。


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


例:








```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$

(%i3) var (s1), numer;
(%o3)                   8.425899999999999
```


関数`var1`も参照してください。

<!-- category: Statistics -->
<!-- keywords: var1 -->
<!-- signatures: var1(list), var1(matrix) -->
### Function: var1 (list)

これは標本分散です。以下のように定義されます。


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


例:










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


関数`var`も参照してください。

