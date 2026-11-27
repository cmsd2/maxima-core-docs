## stats

<!-- category: Statistics -->
<!-- keywords: cdf_rank_sum -->
<!-- signatures: cdf_rank_sum(x, n, m) -->
### Function: cdf_rank_sum (x, n, m)

順位和統計の正確確率分布の累積密度関数。
引数 *x*は実数であり、
*n*と *m*はともに正の整数です。


`test_rank_sum`も参照してください。

<!-- category: Statistics -->
<!-- keywords: cdf_signed_rank -->
<!-- signatures: cdf_signed_rank(x, n) -->
### Function: cdf_signed_rank (x, n)

符号順位統計の正確確率分布の累積密度関数。
引数 *x*は実数であり、
*n*は正の整数です。


`test_signed_rank`も参照してください。

<!-- category: Statistics -->
<!-- keywords: inference_result -->
<!-- signatures: inference_result(title, values, numbers) -->
### Function: inference_result (title, values, numbers)

statsの関数が返す型の `inference_result`オブジェクトを構成します。
引数 *title*は手続き名の文字列です;
*values*は形式 `symbol = value`の要素を持つリストであり、
*numbers*は
どの値がデフォルトで表示されるか示している
1から `length(values)`までの範囲の正の整数のリストです。


例:


これ
長方形に関する結果を示す簡単な例です。
このオブジェクトのタイトルは
文字列 `"Rectangle"`であり、
, it stores five results, named
`'base`, `'height`, `'diagonal`, `'area`, `'perimeter`
と名付けられた5つの結果を格納しますが、
一番目、二番目、五番目と四番目だけが表示されます。
`'diagonal`はこのオブジェクトに格納されますが、表示されません;
その値にアクセスするには関数 `take_inference`を利用してください。















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


`take_inference`も参照してください。

<!-- category: Statistics -->
<!-- keywords: inferencep -->
<!-- signatures: inferencep(obj) -->
### Function: inferencep (obj)

*obj*が `inference_result`オブジェクトか否かに依存して、
`true`か `false`を返します。

<!-- category: Statistics -->
<!-- keywords: items_inference -->
<!-- signatures: items_inference(obj) -->
### Function: items_inference (obj)

*obj*に格納された項目名のリストを返します。
*obj*は `inference_result`オブジェクトでなければいけません。


例:


`inference_result`オブジェクトは
`'pi`と `'e`と名付けられた2つの値を格納しますが、
二番目だけが表示されます。
`items_inference`関数は、
表示されるされないに関係なく、項目すべての名前を返します。








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
<!-- keywords: pdf_rank_sum -->
<!-- signatures: pdf_rank_sum(x, n, m) -->
### Function: pdf_rank_sum (x, n, m)

順位和統計の正確確率分布の確率密度関数。
引数 *x*は実数であり、
*n*と *m*はともに正の整数です。


`test_rank_sum`も参照してください。

<!-- category: Statistics -->
<!-- keywords: pdf_signed_rank -->
<!-- signatures: pdf_signed_rank(x, n) -->
### Function: pdf_signed_rank (x, n)

符号順位統計の正確確率分布の確率密度関数。
引数 *x*は実数であり、
*n*は正の整数です。


`test_signed_rank`も参照してください。

<!-- category: Statistics -->
<!-- keywords: simple_linear_regression -->
<!-- signatures: simple_linear_regression(x), simple_linear_regression(xoption) -->
### Function: simple_linear_regression (x)

単回帰 $y_i=a+b x_i+e_i$。
ここで、 $e_i$は $N(0,sigma)$の独立確率変数です
引数 *x*は2つの列行列か対のリストでなければいけません。


オプション:



- *
`'conflevel`, デフォルト `95/100`,
比の信頼区間の信頼度;
(0,1)内の値を取る式でなければいけません。
- *
`'regressor`, デフォルト `'x`,
独立変数名。


関数 `simple_linear_regression`の出力は
以下の結果を持つ
`inference_result` Maximaオブジェクトです:



1. `'model`: 適合方程式。
新しい予測を行うのに役立ちます。
以下の例を参照してください。
2. `'means`: 二変量平均。
3. `'variances`: 両方の変数の分散。
4. `'correlation`: 相関係数。
5. `'adc`: 調整済み決定係数。
6. `'a_estimation`: パラメータ *a*の推定。
7. `'a_conf_int`: パラメータ *a*の信頼区間。
8. `'b_estimation`: パラメータ *b*の推定。
9. `'b_conf_int`:　パラメータ *b*の信頼区間。
10. `'hypotheses`: パラメータ *b*について検定される帰無、対立仮説。
11. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
12. `'distribution`: パラメータを伴う標本統計分布。
13. `'p_value`: *b*についての検定の$p$値。
14. `'v_estimation`: 不偏分散推定もしくは残差分散。
15. `'v_conf_int`: 分散信頼区間。
16. `'cond_mean_conf_int`: 条件付き平均の信頼区間。
以下の例を参照してください。
17. `'new_pred_conf_int`: 新しい予測の信頼区間。
以下の例を参照してください。
18. `'residuals`: 予測に関して並べ替えられた対(予測, 残差)のリスト
これは適合度分析に役に立ちます。
以下の例を参照してください。


Only items
上の項目 1, 4, 14, 9, 10, 11, 12, 13だけが
この順で、デフォルトで表示されます。
残りは
ユーザーが関数 `items_inference`と `take_inference`を利用するまで
隠されたままです。


例:


線形モデルの二変量標本へのフィッティング。
入力 `%i4`は
回帰線と一緒に標本をプロットします;
入力 `%i5`は
`x=113`が与えられたとして
`y`を計算します;
`x=113`の時
平均と、新しい予測の信頼区間も計算されます。















```maxima
(%i1) load("stats")$
(%i2) s:[[125,140.7], [130,155.1], [135,160.3], [140,167.2],
                                                [145,169.8]]$
(%i3) z:simple_linear_regression(s,conflevel=0.99);
           |               SIMPLE LINEAR REGRESSION
           |
           |   model = 1.405999999999985 x - 31.18999999999804
           |
           |           correlation = .9611685255255155
           |
           |           v_estimation = 13.57966666666665
           |
(%o3)      | b_conf_int = [.04469633662525263, 2.767303663374718]
           |
           |          hypotheses = H0: b = 0 ,H1: b # 0
           |
           |            statistic = 6.032686683658114
           |
           |            distribution = [student_t, 3]
           |
           |             p_value = 0.0038059549413203
(%i4) plot2d([[discrete, s], take_inference(model,z)],
        [x,120,150],
        [gnuplot_curve_styles, ["with points","with lines"]] )$
(%i5) take_inference(model,z), x=133;
(%o5)                         155.808
(%i6) take_inference(means,z);
(%o6)                     [135.0, 158.62]
(%i7) take_inference(new_pred_conf_int,z), x=133;
(%o7)              [132.0728595995113, 179.5431404004887]
```

<!-- category: Statistics -->
<!-- keywords: stats_numer -->
<!-- signatures: stats_numer -->
### Variable: stats_numer

デフォルト値: `true`


もし `stats_numer`が `true`なら、
推定統計的関数は浮動小数点数で結果を返します。
もし `false`なら、
結果は記号と有理フォーマットで与えられます。

<!-- category: Statistics -->
<!-- keywords: take_inference -->
<!-- signatures: take_inference(n, obj), take_inference(name, obj), take_inference(list, obj) -->
### Function: take_inference (n, obj)

もし *n*が正の整数なら、
*obj*に格納された *n*番目の値を返します。
もし *name*が項目名なら、そう名付けられた項目を返します。
もし一番目の引数が数やシンボルのリストなら、
関数 `take_inference`は対応する結果のリストを返します。


例:


`inference_result`オブジェクトが与えられたとして、
関数 `take_inference`は
それに格納されたある情報を抽出するためにコールされます。


















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


`inference_result`と `take_inference`も参照してください。

<!-- category: Statistics -->
<!-- keywords: test_mean -->
<!-- signatures: test_mean(x), test_mean(x, options...) -->
### Function: test_mean (x)

これは平均t検定です。
引数 *x*は1次元標本を含むリストか列行列です。
もしオプション `'asymptotic`が `true`なら、
*中心極限定理*に基づいた漸近検定も実行します。


オプション:



- *
`'mean`, デフォルト `0`, はチェックされる平均値です。
- *
`'alternative`, デフォルト `'twosided`, は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater`, `'less`。
- *
`'dev`, デフォルト `'unknown`, は既知の時の標準偏差値です;
有効な値は次の通りです: `'unknown`か正の式。
- *
`'conflevel`, デフォルト `95/100`, は信頼区間の信頼度です;
(0,1)内の値を取る式でなければいけません。
- *
`'asymptotic`, デフォルト `false`, は正確確率t検定か、
*中心極限定理*に基づいた漸近検定かどちらを実行するかを示します;
有効な値は `true`と `false`です。


関数 `test_mean`の出力は
以下の結果を示す`inference_result` Maximaオブジェクトです:



1. `'mean_estimate`: 標本平均。
2. `'conf_level`: ユーザーが選択した信頼度。
3. `'conf_interval`: 母平均の信頼度。
4. `'method`: 推定手続き。
5. `'hypotheses`: 検定される帰無と対立仮説。
6. `'statistic`: 帰無仮説を検定するために使われる標本統計の値。
7. `'distribution`: パラメータと合わせて、標本統計分布。
8. `'p_value`: 検定の$p$値


例:


未知の分散で正確確率 *t*検定を実行します。
片側対立 $H_1: mean<50$に対して
帰無仮説は $H_0: mean=50$です;
結果に従うと、$p$値が大きすぎ、
$H_0$を却下する証拠がありません。








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


今回、Maximaは *中心極限定理*に基づく漸近検定を実行します。
両側対立 $H_1: not equal(mean, 50)$に対して
帰無仮説は $H_0: equal(mean, 50)$です;
結果に従うと、
$p$値は非常に小さく、
対立 $H_1$を指示して、$H_0$は却下すべきです。
. Note that, as indicated by the 
`Method`成分が示すように、
この手続きは多くの標本に適用すべきです。










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

これは2つの標本の平均の差 *t*検定です。
引数 *x1*と *x2*は2つの独立標本を含むリストか列行列です。
異なる未知の分散の場合
(以下のオプション `'dev1`, `'dev2`, `'varequal`を参照してください)、
自由度の次数はWelch近似を使って計算されます。
もしオプション `'asymptotic`が `true`に設定されているなら
*中心極限定理*に基づく漸近検定も実行します。


オプション:



- *
- *
`'alternative`, デフォルト `'twosided`, は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater`, `'less`。
- *
`'dev1`, デフォルト `'unknown`,
既知の時、これは*x1*標本の標準偏差値です;
有効な値は次の通りです: `'unknown`もしくは正の式。
- *
`'dev2`, デフォルト `'unknown`, 
既知の時、これは*x2*標本の標準偏差値です;
有効な値は次の通りです: `'unknown`もしくは正の式。
- *
`'varequal`, デフォルト `false`,
分散を等しいと考えるか等しくないと考えるか;
このオプションは
　`'dev1`と `'dev2`の両方もしくはいずれかが `'unknown`の時だけ
有効です。
- *
`'conflevel`, デフォルト `95/100`,
信頼区間の信頼度;
(0,1)内の値を取る式でなければいけません。
- *
`'asymptotic`, デフォルト `false`,
正確確率 *t*検定か
*中心極限定理*に基づく漸近検定どちらを実行するかを示します;
有効な値は `true`と `false`です。


関数 `test_means_difference`の出力は
以下の結果を示す`inference_result` Maximaオブジェクトです:



1. `'diff_estimate`: 平均差推定。
2. `'conf_level`: ユーザーが選択した信頼度。
3. `'conf_interval`: 平均差の信頼区間。
4. `'method`: 推定手続き。
5. `'hypotheses`: 検定される帰無、対立仮説。
6. `'statistic`: 帰無仮説を検定するのに使われる標本統計値
7. `'distribution`: パラメータを伴う標本統計分布。
8. `'p_value`: 検定の$p$値。


例:


母平均 $m_1$と $m_2$で対立 $H_1: m_1>m_2$に対して
2つの小さな標本 *x* *y*で平均が等しいか検定します;
分散は未知で異なると仮定されます。














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


前と同じ検定、
しかし今回は分散が等しいと仮定されます。















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

正規性のShapiro-Wilk検定。
引数 *x*は
数のリストであり、
標本サイズは2より大きく、5000以下でなければいけません。
そうでないなら、関数 `test_normality`はエラーメッセージをシグナルします。


参考文献:


  

[1] Algorithm AS R94, Applied Statistics (1995), vol.44, no.4, 547-551


関数 `test_normality`の出力は
以下の結果を持つ
`inference_result` Maximaオブジェクトです:



1. `'statistic`: *W*統計値
2. `'p_value`: 正規仮定の$p$値。


例:


サイズ9の標本に基づいて母集団の正規性をチェックします。












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

出現率推定。
引数 *x*は
未知の確率でのBernoulli実験の*n*回試行での成功回数です。


オプション:



- *
`'proportion`, デフォルト `1/2`,
はチェックされる出現率の値です。
- *
`'alternative`, デフォルト `'twosided`,
は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater`, `'less`.
- *
`'conflevel`, デフォルト `95/100`,
比の信頼区間の信頼度;
(0,1)内の値を取る式でなければいけません。
- *
`'asymptotic`, デフォルト `false`,
二項分布に基づく正確確率 *t*検定か
*中心極限定理*に基づく漸近検定どちらを実行するかを示します;
有効な値は `true`と `false`です。
- *
`'correct`, デフォルト `true`,
Yates補正が適用されるかどうかを示します。


The output of function
関数 `test_proportion`の出力は
以下の結果を示す
`inference_result` Maximaオブジェクトです:



1. `'sample_proportion`: 標本出現率。
2. `'conf_level`: ユーザーが選択した信頼度。
3. `'conf_interval`: 出現率のWilson信頼区間。
4. `'method`: 推定手続き。
5. `'hypotheses`: 検定される帰無、対立仮説。
6. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
7. `'distribution`: パラメータを伴う標本統計分布。
8. `'p_value`: 検定の$p$値。


例:


正確確率検定を実行します。
片側対立 $H_1: p<1/2$に対して、
帰無仮説は $H_0: p=1/2$です。







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


両側漸近検定。信頼度は99/100です。









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

2つの出現率の差の推定。
引数 *x1*は
一番目の母集団でのBernoulli実験の
*n1*回の試行での成功回数であり、
*x2*と *n2*は
二番目の母集団での対応する値です。
標本は独立で、検定は漸近です。


オプション:



- *
`'alternative`, デフォルト `'twosided`,
は対立仮説です;
有効な値は次の通りです: `'twosided` (`p1 # p2`), `'greater` (`p1 > p2`), `'less` (`p1 < p2`).
- *
`'conflevel`, デフォルト `95/100`,
比の信頼区間の信頼度;
(0,1)内の値を取る式でなければいけません。
- *
`'correct`, デフォルト `true`,
はYates補正が適用されるかどうかを示します。


関数 `test_proportions_difference`の出力は
以下の結果を示す
`inference_result` Maximaオブジェクトです:



1. `'proportions`: 2つの標本出現率のリスト。
2. `'conf_level`: ユーザーが選択した信頼度。
3. `'conf_interval`: 出現率の差 `p1 - p2`の信頼区間。
4. `'method`: 推定手続きと
標本サイズのいずれかが10より小さい場合の警告メッセージ
5. `'hypotheses`: 検定される帰無、対立仮説。
6. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
7. `'distribution`: パラメータを伴う標本統計分布。
8. `'p_value`: 検定の$p$値。


例:


機械が250個のうち、10個の欠陥製品を製造しました。
その機械は、ある保守作業のあと、
150個のうち、4個の欠陥製品を製造しました。
機械が改善したか知るために、
対立 `H0:p1>p2`に対して
帰無仮説 `H0:p1=p2`を検定します。
ここで、
`p1`と `p2`は
保守の前と後で製造された製品が欠陥である確率です。
p値に従うと、対立を受け入れる十分な証拠はありません。









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


データが未知の時の漸近正規分布の正確確率標準偏差。









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

これは
2つの連続母集団のメジアンを比較するWilcoxon-Mann-Whitney検定です。
最初の2つの引数 *x1*と *x2*は
2つの独立標本のデータを持つリストか列行列です。
もし標本サイズのいずれかが10より大きいか、
引き分けがあるなら、
正規近似を実行します。


オプション:



- *
`'alternative`, デフォルト `'twosided`,
は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater` and `'less`.


The output of function
関数 `test_rank_sum`の出力は
以下の結果を持つ
`inference_result` Maximaオブジェクトです:



1. `'method`: 推定手続き。
2. `'hypotheses`: 検定される帰無、対立仮説。
3. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
4. `'distribution`: パラメータを伴う標本統計分布。
5. `'p_value`: 検定の$p$値。


例:


母集団が似たメジアンを持つかチェックします。
標本サイズは小さく、正確確率検定がされます。














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


次は、
より大きな標本で引き分けを含み、
手続きは正規近似をします。
対立仮説は $H_1: median1 < median2$です。














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

これは連続母集団のメジアンに関するノンパラメトリック符号検定です。
引数 *x*は1次元標本を含むリストか列行列です。


オプション:



- *
`'alternative`, デフォルト `'twosided`,
は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater`, `'less`.
- *
`'median`, デフォルト `0`, はチェックされるメジアン値です。


関数 `test_sign`の出力は
以下の結果を示す
`inference_result` Maximaオブジェクトです:



1. `'med_estimate`: 標本メジアン。
2. `'method`: 推定手続き。
3. `'hypotheses`: 検定される帰無、対立仮説。
4. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
5. `'distribution`: パラメータを伴う標本統計分布。
6. `'p_value`: 検定の$p$値。


例:


対立 $H_1: median > 6$に対して、
標本が採られた母集団がメジアン6を持つかどうかチェックします。








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

これは
連続母集団のメジアンに関する推定を行う
Wilcoxonの符号順位検定です。
引数 *x*は
1次元標本を含む
リストか列行列です。
もし標本サイズが20より大きいか、複数の零すなわち引き分けがあれば、
正規近似を実行します


`pdf_rank_test`と `cdf_rank_test`も参照してください。


オプション:



- *
`'median`, デフォルト `0`,
はチェックされるメジアン値です。
- *
`'alternative`, デフォルト `'twosided`,
は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater` and `'less`.


関数 `test_signed_rank`の出力は
以下の結果を持つ
`inference_result` Maximaオブジェクトです:



1. `'med_estimate`: 標本メジアン。
2. `'method`: 推定手続き。
3. `'hypotheses`: 検定される帰無、対立仮説。
4. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
5. `'distribution`: パラメータを伴う標本統計分布。
6. `'p_value`: 検定の$p$値。


例:


対立 $H_1: median > 15$に対して
帰無仮説 $H_0: median = 15$をチェックします。
引き分けがないので、これは正確確率検定です。












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

これは分散 *chi^2*検定です。
引数 *x*は
正規母集団から取られた1次元標本を含む
リストか列行列です。


オプション:



- *
`'mean`, デフォルト `'unknown`,
は、既知の時、母平均です。
- *
`'alternative`, デフォルト `'twosided`,
対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater`, `'less`.
- *
`'variance`, デフォルト `1`,
これはチェックされる分散値(正)です。
- *
`'conflevel`, デフォルト `95/100`,
信頼区間の信頼度;
(0,1)内の値を取る式でなければいけません。


関数 `test_variance`の出力は
以下の結果を示す`inference_result` Maximaオブジェクトです:



1. `'var_estimate`: 標本分散。
2. `'conf_level`: ユーザーが選択した信頼度。
3. `'conf_interval`: 母分散の信頼区間。
4. `'method`: 推定手続き。
5. `'hypotheses`: 検定される帰無、対立仮説。
6. `'statistic`: 帰無仮説を検定するのに使う標本統計値。
7. `'distribution`: パラメータを伴う標本統計分布。
8. `'p_value`: 検定の $p$値。


例:


平均が未知の母集団の分散が200以上か検定します。








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

これは2つの正規母集団の分散比 *F*検定です。
引数 *x1*と *x2*は
2つの独立標本を含むリストか列行列です。


オプション:



- *
`'alternative`, デフォルト `'twosided`,
は対立仮説です;
有効な値は次の通りです: `'twosided`, `'greater`, `'less`.
- *
`'mean1`, デフォルト `'unknown`,
既知の時、これは*x1*が取られた母集団の平均です。
- *
`'mean2`, デフォルト `'unknown`,
既知の時、これは*x2*が取られた母集団の平均です。
- *
`'conflevel`, デフォルト `95/100`,
比の信頼区間の信頼度;
(0,1)内の値を取る式でなければいけません。


関数 `test_variance_ratio`の出力は
以下の結果を示す`inference_result` Maximaオブジェクトです:



1. `'ratio_estimate`: 標本分散比。
2. `'conf_level`: ユーザーが選択した信頼度。
3. `'conf_interval`: 分散比の信頼区間。
4. `'method`: 推定手続き。
5. `'hypotheses`: 検定される帰無、対立仮説。
6. `'statistic`: 帰無仮説を検定するのに使われる標本統計値。
7. `'distribution`: パラメータを伴う標本統計分布。
8. `'p_value`: 検定の$p$値。



例:


前者が後者より大きいという対立仮説に対して、
2つの正規母集団の分散の等しさが














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

