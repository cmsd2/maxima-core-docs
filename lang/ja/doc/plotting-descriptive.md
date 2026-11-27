## descriptive

<!-- category: Plotting -->
<!-- keywords: barsplot, barsplot_description -->
<!-- signatures: barsplot(data1, data2, ..., option_1, option_2, ...), barsplot_description(...) -->
### Function: barsplot (data1, data2, ..., option_1, option_2, ...)

1変量、多変量どちらの標本でも離散統計変数の棒グラフをプロットします


*data*は1標本を意味する結果のリストかもしれませんし、
それぞれサイズ*m*の*n*個の標本を意味する*m*行*n*列の行列かもしれません。


利用可能なオプションは以下のものです:



- *
`draw`パッケージで定義されたもの。
- *
*box_width* (デフォルト, `3/4`): 長方形の相対幅。
値は範囲`[0,1]`内でなければいけません。
- *
*grouping* (デフォルト, `clustered`):
複数の標本をいかに表示するか示します。
有効な値: `clustered`と `stacked`。
- *
*groups_gap* (デフォルト, `1`): 棒の2つの隣り合うグループの隙間を表す正の整数。
- *
*bars_colors* (デフォルト, `[]`): 複数の標本のための色のリスト。
指定された色よりもたくさん標本がある時は、
追加で必要な色はランダムに選ばれます。
更に詳しくは`color`を参照してください。
- *
*frequency* (デフォルト, `absolute`): 縦座標のスケールを示します。
可能な値: `absolute`, `relative`, `percent`。
- *
*ordering* (デフォルト, `orderlessp`): 可能な値は`orderlessp`か`ordergreatp`です。
統計的結果がどちら向きに*x*軸に並んでいるかを示します。
- *
*sample_keys* (デフォルト, `[]`): 凡例に使われる文字列のリスト。
リストの長さが0か標本の長さ以外なら、
エラーメッセージを返します。
- *
*start_at* (デフォルト, `0`): x軸上のどこからプロットされるか示します。
- *
`barsplot`が内部で割り当てる
`xtics`を除くすべてのグローバル `draw`オプション
もしこのオプションに自分の値を設定し、複雑なシーンを構築したいなら、
`barsplot_description`を使用してください。
以下の例を参照してください。
- *
以下のローカル `draw`オプション: `key`, `color`, 
`fill_color`, `fill_density`, `line_width`。
`bars`も参照してください。


関数`barsplot_description`は
他のグラフィックオブジェクトと一緒に複雑なシーンを生成するために
グラフィックオブジェクトを生成します。
wxMaximaとiMaximaインターフェイスで埋め込みヒストグラムを生成するための
関数`wxbarsplot`もあります。


例:


行列形式での1変量標本。絶対頻度。













```maxima
(%i1) load ("descriptive")$
(%i2) m : read_matrix (file_search ("biomed.data"))$

(%i3) barsplot(
        col(m,2),
        title        = "Ages",
        xlabel       = "years",
        box_width    = 1/2,
        fill_density = 3/4)$
```


異なるサイズの2つの標本。
相対頻度とユーザー宣言の色を使って。















```maxima
(%i1) load ("descriptive")$
(%i2) l1:makelist(random(10),k,1,50)$
(%i3) l2:makelist(random(10),k,1,100)$

(%i4) barsplot(
        l1,l2,
        box_width    = 1,
        fill_density = 1,
        bars_colors  = [black, grey],
        frequencies = relative,
        sample_keys = ["A", "B"])$
```


サイズが等しい4つの非数標本。
















```maxima
(%i1) load ("descriptive")$

(%i2) barsplot(
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        title  = "Asking for something to four groups",
        ylabel = "# of individuals",
        groups_gap   = 3,
        fill_density = 0.5,
        ordering     = ordergreatp)$
```


スタックバー。
















```maxima
(%i1) load ("descriptive")$

(%i2) barsplot(
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        makelist([Yes, No, Maybe][random(3)+1],k,1,50),
        title  = "Asking for something to four groups",
        ylabel = "# of individuals",
        grouping     = stacked,
        fill_density = 0.5,
        ordering     = ordergreatp)$
```


複数プロット文脈での`barsplot`。



```maxima
(%i1) load ("descriptive")$
(%i2) l1:makelist(random(10),k,1,50)$
(%i3) l2:makelist(random(10),k,1,100)$
(%i4) bp1 : 
        barsplot_description(
         l1,
         box_width = 1,
         fill_density = 0.5,
         bars_colors = [blue],
         frequency = relative)$
(%i5) bp2 : 
        barsplot_description(
         l2,
         box_width = 1,
         fill_density = 0.5,
         bars_colors = [red],
         frequency = relative)$
(%i6) draw(gr2d(bp1), gr2d(bp2))$
```


棒グラフ関連オプションについては、パッケージ`draw`の`bars`を参照してください。
関数`histogram`と`piechart`も参照してください。

<!-- category: Plotting -->
<!-- keywords: boxplot, boxplot_description -->
<!-- signatures: boxplot(data), boxplot(data, option_1, option_2, ...), boxplot_description(...) -->
### Function: boxplot (data)

この関数は箱ひげ図をプロットします。
引数*data*はリストだったり行列だったりします。
箱ひげ図は主に異なる標本の比較に使われるので、リストはあまり興味深くありません。
行列の場合には多変量統計変数の複数成分おw比較することが可能です。
しかし、できる限り異なる標本サイズの標本のリストも許すようにしています。
実際、これは、パッケージ`descriptive`の中で
この種のデータ構造を許容する唯一の関数です


利用可能なオプションは以下のものです:



- *
*box_width* (デフォルト, `3/4`): 箱の相対幅。
この値は範囲`[0,1]`内でなければいけません。
- *
*box_orientation* (デフォルト, `vertical`): 可能な値: `vertical`
と `horizontal`。
- *
`boxplot`が内部で割り当てる
`points_joined`, `point_size`, `point_type`,
`xtics`, `ytics`, `xrange`, `yrange`を除く
すべての `draw`オプション。
もしこのオプションに自分の値を設定し、複雑なシーンを構築したいなら、
`boxplot_description`を使用してください。
- *
以下のローカル `draw`オプション: `key`, `color`,  `line_width`。


関数`boxplot_description`は
他のグラフィックオブジェクトと一緒に複雑なシーンを生成するために
グラフィックオブジェクトを生成します。
wxMaximaとiMaximaインターフェイスで埋め込みヒストグラムを生成するための
関数`wxbarsplot`もあります。


例:


多変量標本の箱ひげ図。













```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix(file_search("wind.data"))$

(%i3) boxplot(s2,
        box_width  = 0.2,
        title      = "Windspeed in knots",
        xlabel     = "Stations",
        color      = red,
        line_width = 2)$
```


異なるサイズの3つの標本の箱ひげ図。











```maxima
(%i1) load ("descriptive")$

(%i2) A :
       [[6, 4, 6, 2, 4, 8, 6, 4, 6, 4, 3, 2],
        [8, 10, 7, 9, 12, 8, 10],
        [16, 13, 17, 12, 11, 18, 13, 18, 14, 12]]$

(%i3) boxplot (A, box_orientation = horizontal)$
```

<!-- category: Plotting -->
<!-- keywords: histogram, histogram_description -->
<!-- signatures: histogram(list), histogram(list, option_1, option_2, ...), histogram(one_column_matrix), histogram(one_column_matrix, option_1, option_2, ...), histogram(one_row_matrix), histogram(one_row_matrix, option_1, option_2, ...), histogram_description(...) -->
### Function: histogram (list)

この関数は一連の標本からヒストグラムをプロットします。
標本データは数のリストか一次元行列に保存しなければいけません。


利用可能なオプションは以下のものです:



- *
*nclasses* (デフォルト, `10`): ヒストグラムのクラス数、もしくは
クラスの境界と数か境界だけを含むリスト。
- *
*frequency* (デフォルト, `absolute`): 縦座標のスケールを示します。
可能な値: `absolute`, `relative`, `percent`。
- *
*htics* (デフォルト, `auto`): ヒストグラムチックのフォーマット。
可能な値: `auto`, `endpoints`, `intervals`, かラベルのリスト。
- *
`histogram`が内部で割り当てる`xrange`, `yrange`, `xtics`を除く
すべてのグローバル `draw`オプション。
もしこれらのオプションに自分の値を設定したいなら、
`histogram_description`を利用してください。
以下の例を参照してください。
- *
以下のローカル `draw`オプション: `key`, `color`, 
`fill_color`, `fill_density`と `line_width`.
`bars`も参照してください。


関数 `histogram_description`は他のグラフィックオブジェクトと一緒に
複雑なシーンを生成するのに適したグラフィックオブジェクトを生成します。
wxMaximaと iMaximaインターフェイスで埋め込みヒストグラムを生成する
関数`wxhistogram`もあります。


例:


8クラスを持つ簡単なヒストグラム。















```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) histogram (
           s1,
           nclasses     = 8,
           title        = "pi digits",
           xlabel       = "digits",
           ylabel       = "Absolute frequency",
           fill_color   = grey,
           fill_density = 0.6)$
```



ヒストグラムの境界を-2と12に、クラス数を3に設定します。
また予め定義されたチックを導入します:



```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) histogram (
           s1,
           nclasses     = [-2,12,3],
           htics        = ["A", "B", "C"],
           terminal     = png,
           fill_color   = "#23afa0",
           fill_density = 0.6)$
```


`xrange`を設定しシーンの中に明示的な曲線を足すのに
`histogram_description`を利用します:



```maxima
(%i1) load ("descriptive")$
(%i2) ( load("distrib"),
        m: 14, s: 2,
        s2: random_normal(m, s, 1000) ) $
(%i3) draw2d(
        grid   = true,
        xrange = [5, 25],
        histogram_description(
          s2,
          nclasses     = 9,
          frequency    = relative,
          fill_density = 0.5),
        explicit(pdf_normal(x,m,s), x, m - 3*s, m + 3* s))$
```

<!-- category: Plotting -->
<!-- keywords: piechart, piechart_description -->
<!-- signatures: piechart(list), piechart(list, option_1, option_2, ...), piechart(one_column_matrix), piechart(one_column_matrix, option_1, option_2, ...), piechart(one_row_matrix), piechart(one_row_matrix, option_1, option_2, ...), piechart_description(...) -->
### Function: piechart (list)

`barsplot`に似ていますが、長方形の代わりに扇をプロットします。


利用可能なオプションは以下のものです:



- *
*sector_colors* (デフォルト, `[]`): セクタの色のリスト。
指定した色よりも多くセクタがあるときは、必要な色の超過分がランダムに選ばれます。
それらについて更に知るには `color`を参照してください。
- *
*pie_center* (デフォルト, `[0,0]`): 円グラフの中心。
- *
*pie_radius*　(デフォルト, `1`): 円グラフの半径。
- *
`piechart`が内部で割り当てる`key`を除いたすべてのグローバル `draw`オプション。
もしこのオプションに自分の値を設定し、複雑なシーンを構築したいなら、
`piechart_description`を利用してください。
- *
以下のローカル `draw`オプション: `key`, `color`,
`fill_display`, `line_width`。
`ellipse`も参照してください。


関数 `piechart_description`は他のグラフィックオブジェクトと一緒に
複雑なシーンを生成するのに適したグラフィックオブジェクトを生成します。
wxMaximaと iMaximaインターフェイスで埋め込みヒストグラムを生成する
関数`wxhistogram`もあります。


例:












```maxima
(%i1) load ("descriptive")$
(%i2) s1 : read_list (file_search ("pidigits.data"))$
(%i3) piechart(
        s1,
        xrange = [-1.1, 1.3],
        yrange = [-1.1, 1.1],
        title  = "Digit frequencies in pi")$
```


関数`barsplot`も参照してください。

<!-- category: Plotting -->
<!-- keywords: scatterplot, scatterplot_description -->
<!-- signatures: scatterplot(list), scatterplot(list, option_1, option_2, ...), scatterplot(matrix), scatterplot(matrix, option_1, option_2, ...), scatterplot_description(...) -->
### Function: scatterplot (list)

1変量(*list*)や多変量(*matrix*)の標本の散布図をプロットします。


利用可能なオプションは `histogram`が許すものと同じです。


関数 `scatterplot_description`は他のグラフィックオブジェクトと一緒に
複雑なシーンを生成するのに適したグラフィックオブジェクトを生成します。
wxMaximaと iMaximaインターフェイスで埋め込みヒストグラムを生成する
関数`wxscatterplot`もあります。


例:


シミュレーティッドGauss標本の1変量散布図。












```maxima
(%i1) load ("descriptive")$
(%i2) load ("distrib")$

(%i3) scatterplot(
        random_normal(0,1,200),
        xaxis      = true,
        point_size = 2,
        dimensions = [600,150])$
```


二次元散布図。













```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) scatterplot(
       submatrix(s2, 1,2,3),
       title      = "Data from stations #4 and #5",
       point_type = diamant,
       point_size = 2,
       color      = blue)$
```


3次元散布図。








```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$
(%i3) scatterplot(submatrix (s2, 1,2), nclasses=4)$
```


5つのクラスのヒストグラムと5次元散布図。














```maxima
(%i1) load ("descriptive")$
(%i2) s2 : read_matrix (file_search ("wind.data"))$

(%i3) scatterplot(
        s2,
        nclasses     = 5,
        frequency    = relative,
        fill_color   = blue,
        fill_density = 0.3,
        xtics        = 5)$
```


2次元か3次元で孤立点か線で結んだ点をプロットすることについては、
`points`を参照してください。
`histogram`も参照してください。

<!-- category: Plotting -->
<!-- keywords: starplot, starplot_description -->
<!-- signatures: starplot(data1, data2, ..., option_1, option_2, ...), starplot_description(...) -->
### Function: starplot (data1, data2, ..., option_1, option_2, ...)

1変量、多変量どちらの標本でも離散統計変数のスターダイアグラムをプロットします


*data*は1標本を意味する結果のリストかもしれませんし、
それぞれサイズ*m*の*n*個の標本を意味する*m*行*n*列の行列かもしれません。


利用可能なオプションは以下のものです:



- *
*stars_colors* (デフォルト, `[]`): 多変量標本の色のリスト。
指定した色よりも多くセクタがあるときは、必要な色の超過分がランダムに選ばれます。
それらについて更に知るには `color`を参照してください。
- *
*frequency* (デフォルト, `absolute`): 半径のスケールを示します。
可能な値: `absolute`, `relative`, `percent`。
- *
*ordering* (デフォルト, `orderlessp`): 可能な値は`orderlessp`か`ordergreatp`です。
統計的結果がどちら向きに*x*軸に並んでいるかを示します。
- *
*sample_keys* (デフォルト, `[]`): 凡例に使われる文字列のリスト。
リストの長さが0か標本の長さ以外なら、
エラーメッセージを返します。
- *
*star_center* (デフォルト, `[0,0]`): ダイアグラムの中心。
- *
*star_radius* (デフォルト, `1`): ダイアグラムの半径。
- *
`starplot`が内部で割り当てる`points_joined`, `point_type`, `key`を除いたすべてのグローバル `draw`オプション。
もしこのオプションに自分の値を設定し、複雑なシーンを構築したいなら、
`starplot_description`を利用してください。
- *
以下のローカル `draw`オプション: `line_width`。


関数 `starplot_description`は他のグラフィックオブジェクトと一緒に
複雑なシーンを生成するのに適したグラフィックオブジェクトを生成します。
wxMaximaと iMaximaインターフェイスで埋め込みヒストグラムを生成する
関数`wxstarplot`もあります。


例:


絶対頻度に基づいたプロット。
ユーザーが定義した位置と半径。



```maxima
(%i1) load ("descriptive")$
(%i2) l1: makelist(random(10),k,1,50)$
(%i3) l2: makelist(random(10),k,1,200)$

(%i4) starplot(
        l1, l2,
        stars_colors = [blue,red],
        sample_keys = ["1st sample", "2nd sample"],
        star_center = [1,2],
        star_radius = 4,
        proportional_axes = xy,
        line_width = 2 ) $
```

<!-- category: Plotting -->
<!-- keywords: stemplot -->
<!-- signatures: stemplot(data), stemplot(data, option) -->
### Function: stemplot (data)

幹葉図をプロットします。


固有の利用可能なオプションは:



- *
*leaf_unit* (デフォルト, `1`): 葉の単位を示します;
10のべきでなければいけません。


例:



```maxima
(%i1) load ("descriptive")$
(%i2) load("distrib")$

(%i3) stemplot(
        random_normal(15, 6, 100),
        leaf_unit = 0.1);
-5|4
 0|37
 1|7
 3|6
 4|4
 5|4
 6|57
 7|0149
 8|3
 9|1334588
10|07888
11|01144467789
12|12566889
13|24778
14|047
15|223458
16|4
17|11557
18|000247
19|4467799
20|00
21|1
22|2335
23|01457
24|12356
25|455
27|79
key: 6|3 =  6.3
(%o3)                  done
```

