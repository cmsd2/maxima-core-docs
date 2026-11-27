## Plotting

<!-- category: Plotting -->
<!-- keywords: adapt_depth -->
<!-- signatures: adapt_depth[adapt_depth, integer] -->
### Variable: adapt_depth

適応プロットルーチンで使われる分割の最大数です。


デフォルト値: 5

<!-- category: Plotting -->
<!-- keywords: axes -->
<!-- signatures: axes[axes, symbol] -->
### Variable: axes

ここで、*symbol*は`true`, `false`, `x`, `y`のいずれかでありえます。
もし`false`なら、軸は表示されません;
もし`x`か`y`に等しいなら、xかy軸のみが表示され、
`true`に等しいなら、両方の軸が表示されます。
このオプションはplot2dとimplicit_plotだけが使います。


デフォルト値: `true`

<!-- category: Plotting -->
<!-- keywords: azimuth -->
<!-- signatures: azimuth[azimuth, number] -->
### Variable: azimuth

plot3dプロットは
plot2dと同様の水平軸と垂直軸に関してx軸とy軸と、
紙から垂直に出てくるz軸で始まるものと考えることができます。
z軸はその後x軸の回りに`elevation`に等しい角度だけ回転され、
その後、xy平面は新しいz軸の回りに角度`azimuth`だけ回転されます。
このオプションはazimuthに関する値を単位、度で設定します。


デフォルト値: 30


`elevation`も参照してください。

<!-- category: Plotting -->
<!-- keywords: color -->
<!-- signatures: color[color, color_1, ..., color_n] -->
### Variable: color

plot2dとimplicit_plotでは、様々な曲線の色を定義します。
plot3dでは、パレットが使われない時、表面のメッシュ線の色を定義します;
表面の片方の側面は色`color_1`を持ち、逆の側面は*color_2*を(またはもし1つの色しかないなら、同じ色を)持ちます。


もし色よりも曲線や表面が多いなら、色は順に繰り返されます。
gnuplotを使う時、色は、 青、赤、緑、マゼンタ、シアンまたは黒です;
xmaximaでは、色はそれらもしくは文字#で始まり、6桁の16進数字が続く文字列です;
2つは赤成分、2つは緑成分、2つが青成分です。
もし未知の色の名前が与えられたら、黒が代わりに使われます。


デフォルト値: blue, red, green, magenta, black, byan

<!-- category: Plotting -->
<!-- keywords: colorbox -->
<!-- signatures: colorbox[colorbox, symbol] -->
### Variable: colorbox

ここで、*symbol*は`true`か`false`であり得ます。
もし`true`なら、
plot3dはzの違った値を表現するために、
違った色のパレットを使う時はいつでも、
zの値の大きさに従って使われた色を示す枠が右に示されます。
このオプションはxmaximaでは機能しません。


デフォルト値: `false`

<!-- category: Plotting -->
<!-- keywords: contour_plot -->
<!-- signatures: contour_plot(expr, x_range, y_range, options, ...) -->
### Function: contour_plot (expr, x_range, y_range, options, ...)

*expr*の等高線を、領域*x_range*、*y_range*でプロットします。
他の引数は、`plot3d`と同じように扱われます。


この関数は、プロットフォーマットが`gnuplot`か`gnuplot_pipes`の時だけ、
動作します。
付加パッケージ`implicit_plot`も等高線をプロットするのに使われ、
それは任意のフォーマットで動作します。
`implicit_plot`も参照してください。


例:






```maxima
(%i1) contour_plot (x^2 + y^2, [x, -4, 4], [y, -4, 4])$
```


![./figures/plotting2](./figures/plotting2.png)






```maxima
(%i1) F(x, y) := x^3 + y^2;
                                   3    2
(%o1)                  F(x, y) := x  + y

(%i2) contour_plot (F, [u, -4, 4], [v, -4, 4])$
```


`plot3d`が受け付ける任意のオプションを足すことができます;
例えば、オプション`legend`にfalseの値を入れると、凡例を取り除きます。
Gnuplotはデフォルトで3つの高等線を示すように選びます。
レベルの数を増やすには、カスタムのgnuplot前置きを指定する必要があります;








```maxima
(%i1) contour_plot (u^3 + v^2, [u, -4, 4], [v, -4, 4], 
                    [legend,false],
                    [gnuplot_preamble, "set cntrparam levels 12"])$
```

<!-- category: Plotting -->
<!-- keywords: elevation -->
<!-- signatures: elevation[elevation, number] -->
### Variable: elevation

plot3dプロットは
plot2dでの水平と垂直軸にxとy軸に
紙から直立に立ったz軸から始まると考えられます。
その後、z軸はx軸の回りを `elevation`に等しい角度だけ回転し、
xy平面は新しいz軸の回りを `azimuth`角度だけ回転します。
このオプションはelevationの値を度単位で設定します。


デフォルト値: 60


`azimuth`も参照してください。

<!-- category: Plotting -->
<!-- keywords: get_plot_option -->
<!-- signatures: get_plot_option(keyword, index) -->
### Function: get_plot_option (keyword, index)

グローバル変数`plot_options`に保存されている
名前*keyword*を持つオプションの値を返します。
添字で1の値はキーワード自身を返します;
2番の値はキーワードに続く一番目のパラメータを返す、などなど。


`plot_options`や`set_plot_option`、Plotting Optionの節も参照してください。

<!-- category: Plotting -->
<!-- keywords: gnuplot_close -->
<!-- signatures: gnuplot_close() -->
### Function: gnuplot_close ()

`gnuplot_pipes`フォーマットで使われたgnuplotへのパイプを閉じます。

<!-- category: Plotting -->
<!-- keywords: gnuplot_curve_styles -->
<!-- signatures: gnuplot_curve_styles -->
### Variable: gnuplot_curve_styles

これは、上記で記載した*style*で置き換えられた古いオプションです。

<!-- category: Plotting -->
<!-- keywords: gnuplot_curve_titles -->
<!-- signatures: gnuplot_curve_titles -->
### Variable: gnuplot_curve_titles

これは、上記で記載した*legend*で置き換えられた古いオプションです。

<!-- category: Plotting -->
<!-- keywords: gnuplot_default_term_command -->
<!-- signatures: gnuplot_default_term_command -->
### Variable: gnuplot_default_term_command

デフォルト端末の端末タイプを設定するgnuplotコマンド。
デフォルト値は、`set term pop`です。

<!-- category: Plotting -->
<!-- keywords: gnuplot_dumb_term_command -->
<!-- signatures: gnuplot_dumb_term_command -->
### Variable: gnuplot_dumb_term_command

ダム端末の端末タイプを設定するgnuplotコマンド。
デフォルト値は、`"set term dumb 79 22"`です。
これは、79文字 x 22文字のテキスト出力を生成します。

<!-- category: Plotting -->
<!-- keywords: gnuplot_out_file -->
<!-- signatures: gnuplot_out_file -->
### Variable: gnuplot_out_file

`gnuplot_term`オプションと関連して使われる時、
Gnuplotがサポートするグラフィックフォーマットの１つで、
ファイルにプロットを保存するのに使われます。
もしポストスクリプトファイルを生成したければ、
代わりにオプション `psfile`を使うことができます。
これは、Openmathでも機能し、たった１つのオプションで同じことができます。



```maxima
[gnuplot_term, png], [gnuplot_out_file, "graph3.png"]
```

<!-- category: Plotting -->
<!-- keywords: gnuplot_pm3d -->
<!-- signatures: gnuplot_pm3d -->
### Variable: gnuplot_pm3d

`false`の値では、PM3Dモードの使用を抑制するのに使われます。
PM3Dモードはデフォルトで使用可能です。

<!-- category: Plotting -->
<!-- keywords: gnuplot_preamble -->
<!-- signatures: gnuplot_preamble -->
### Variable: gnuplot_preamble

プロットを描く前に、gnuplotコマンドを挿入します。
有効などんなgnuplotコマンドも使うことができます。
複数のコマンドは、セミコロンで分離されなければいけません。
示される例はログスケールプロットを生成します。
`gnuplot_preamble`のデフォルト値は、空の文字列`""`です。

<!-- category: Plotting -->
<!-- keywords: gnuplot_ps_term_command -->
<!-- signatures: gnuplot_ps_term_command -->
### Variable: gnuplot_ps_term_command

ポストスクリプト端末の端末タイプを設定するgnuplotコマンド。
デフォルト値は、
`"set size 1.5, 1.5; set term postscript eps enhanced color solid 24"`,
です。
これは、サイズをgnuplotのデフォルトの1.5倍に設定し、フォントサイズを24に設定などします。
`set term postscript`の詳細については、gnuplotドキュメンテーションを
参照してください。

<!-- category: Plotting -->
<!-- keywords: gnuplot_replot -->
<!-- signatures: gnuplot_replot(), gnuplot_replot(s) -->
### Function: gnuplot_replot ()

gnuplotウィンドウを更新します。
もし`gnuplot_replot`が、文字列*s*の中のgnuplotコマンドを引数としてコールされたなら、
`s`はウィンドウが再プロットされる前にgnuplotに送られます。

<!-- category: Plotting -->
<!-- keywords: gnuplot_reset -->
<!-- signatures: gnuplot_reset() -->
### Function: gnuplot_reset ()

`gnuplot_pipes`フォーマットと一緒に使われるgnuplotの状態をリセットします。
gnuplotウィンドウを更新するには、
`gnuplot_reset`の後に`gnuplot_replot`をコールください。

<!-- category: Plotting -->
<!-- keywords: gnuplot_restart -->
<!-- signatures: gnuplot_restart() -->
### Function: gnuplot_restart ()

`gnuplot_pipes`フォーマットで使われたgnuplotへのパイプを閉じて、
新しいパイプを開きます。

<!-- category: Plotting -->
<!-- keywords: gnuplot_start -->
<!-- signatures: gnuplot_start() -->
### Function: gnuplot_start ()

`gnuplot_pipes`フォーマットでのプロットのため使われるgnuplotへのパイプを開きます。
プロットの前に手動でパイプを開く必要はありません。

<!-- category: Plotting -->
<!-- keywords: gnuplot_term -->
<!-- signatures: gnuplot_term -->
### Variable: gnuplot_term

gnuplot用の出力端末タイプを設定します。


- *
**default** (デフォルト値)

Gnuplot出力が、別のグラフィカルなウィンドウに表示されます。
- *
**dumb**

Gnuplot出力が、Mグラフィックスの"ASCIIアート"近似で、Maximaコンソールに表示されます。
- *
**ps**

Gnuplotが、ポストスクリプトページ記述言語でコマンドを生成します。
もしオプション`gnuplot_out_file`が*filename*に設定されているなら、
gnuplotは、*filename*にポストスクリプトコマンドを書きます。
そうでなければ、`maxplot.ps`ファイルとして保存します。
- *
他のいかなる有効なgnuplot端末仕様

Gnuplotは、png, jpeg, svgのような多くの他のグラフィカルフォーマットで出力を
生成することができます。
これらのフォーマットすべてでプロットを生成するに、`gnuplot_term`に
任意のサポートされたgnuplot端末名(シンボル)もしくは、任意の有効なオプションを伴う
gnuplot端末フル仕様(文字列)さえ設定できます。
例えば、`[gnuplot_term,png]`は、PNG (Portable Network Graphics)形式で
出力を生成する一方、`[gnuplot_term,"png size 1000,1000"]`は、
1000x1000ピクセルサイズのPNGを生成します。

もしオプション`gnuplot_out_file`が*filename*に設定されたら、
gnuplotは、*filename*に出力を書き込みます。
そうでなければ、`maxplot.term`ファイルに書き込みます。
ここで、*term*はgnuplot端末名です。

<!-- category: Plotting -->
<!-- keywords: grid -->
<!-- signatures: grid[grid, integer, integer] -->
### Variable: grid

3次元プロットのためにx方向、y方向で使われるグリッド点の数を設定します。


デフォルト値: 30, 30

<!-- category: Plotting -->
<!-- keywords: legend -->
<!-- signatures: legend[legend, string_1, ..., string_n], legend[legend, false] -->
### Variable: legend

複数のプロットが示される時、プロットのラベルを指定します。
もし与えられたラベルの数より多くの式があるなら、ラベルは繰り返されます。
もし値`false`が与えられるなら、凡例は表示されません。
デフォルトでは、式や関数の名前が使われます。また、点の離散集合に関しては、
単語discrete1, discrete2, ...が使われます。
このオプションは*set_plot_optiion*で設定することができます。

<!-- category: Plotting -->
<!-- keywords: logx -->
<!-- signatures: logx[logx] -->
### Variable: logx

水平軸を対数的にスケールするようにします。
*set_plot_option*では使うことはできません。

<!-- category: Plotting -->
<!-- keywords: logy -->
<!-- signatures: logy[logy] -->
### Variable: logy

垂直軸を対数的にスケールするようにします。
*set_plot_option*では使うことはできません。

<!-- category: Plotting -->
<!-- keywords: make_transform -->
<!-- signatures: make_transform([var1, var2, var3], fx, fy, fz) -->
### Function: make_transform ([var1, var2, var3], fx, fy, fz)

plot3dのオプション`transform_xy`で使われるのに適した関数を返します。
3つの変数*var1*, *var2*, *var3*は3つのダミー変数名です。
それらは、plot3dコマンドが与える3変数
(最初2つの独立変数と、その後それら2つの変数に依存する関数)を表します。
3つの関数*fx*, *fy*, *fz*は、
それら3変数にだけ依存しなければいけなく、プロットすべき対応するx, y, z座標を与えます。
デフォルトで定義された2つの変換があります;
`polar_to_xy`と`spherical_to_xyz`;
それら2つの変換に関するドキュメンテーションを参照してください。

<!-- category: Plotting -->
<!-- keywords: mesh_lines_color -->
<!-- signatures: mesh_lines_color[mesh_lines_color, color] -->
### Variable: mesh_lines_color

パレットが使われる時、plot3dがメッシュ線を描くのに使う色を設定します。
オプション `color`と同じ色を受け付けます。
(`color`で許される色のリストを参照してください。)
値 `false`を与えて、メッシュ線を完全に消すこともできます。


デフォルト値: black

<!-- category: Plotting -->
<!-- keywords: nticks -->
<!-- signatures: nticks[nticks, integer] -->
### Variable: nticks

plot2dで関数をプロットする時、
関数をプロットするための適応プロットルーチンによって使われる点の数の初期値を与えます。
plot2dやplot3dでパラメトリック関数をプロットする時、
プロットで表示される点の数を設定します。


デフォルト値: 29

<!-- category: Plotting -->
<!-- keywords: palette -->
<!-- signatures: palette[palette, [palette_1], ..., [palette_n]], palette[palette, false] -->
### Variable: palette

1つのパレットか複数のパレットのリストで構成されます。
それぞれのパレットは4つの数が続くキーワード付きリストです。
最初の3つの数は、0と1の間でなければならず、
zの最小値に割り当てられる基本色の色調と飽和、値を定義します。
キーワードは3つの属性(色調、飽和、値)のいずれかがzの値に従っての増えることを指定します。
その最後の数は1よりも大きいこともマイナスでもありえます;
変更された属性の対応する値は法1で丸められます。


gnuplotはリストの中の最初のパレットだけを使います;
xmaximaは、複数の表面が一緒にプロットされる時、リストの中のパレットを順に使います;
パレットの数が尽きたら、それらは順に繰り返されます。


メッシュ線の色はオプション`mesh_lines_color`で与えられます。
もし`palette`が値`false`を与えられたら、
表面は陰影されず、曲線のメッシュだけで表されます。
その場合、線の色はオプション`color`で決定されます。


デフォルト値: [hue, 0.25, 0.7, 0.8, 0.5], [hue, 0.65, 0.8, 0.9, 0.55], [hue, 0.55, 0.8, 0.9, 0.4], [hue, 0.95, 0.7, 0.8, 0.5]

<!-- category: Plotting -->
<!-- keywords: plot2d -->
<!-- signatures: plot2d(plot, x_range, ..., options, ...), plot2d([plot_1, ..., plot_n], ..., options, ...), plot2d([plot_1, ..., plot_n], x_range, ..., options, ...) -->
### Function: plot2d (plot, x_range, ..., options, ...)

ここで、*plot*, *plot_1*, ..., *plot_n*は式か関数名、もしくは以下のいずれかの形式のリストです:


`[discrete, [x1, ..., xn], [y1, ..., yn]]`,
`[discrete, [[x1, y1], ..., [xn, ..., yn]]`, 
または`[parametric, x_expr, y_expr, t_range]`.


１つもしくは複数の式を１変数か1パラメータの関数としてプロット表示します。


`plot2d`は1つもしくは複数のプロットを2次元に表示します。
プロットを定義するのに式や関数名を使う時には、
それらは１変数*var*だけに依存すべきであり、
変数名とその最小値と最大値を提供するために*x_range*の使用が必須です;
*x_range*の構文法は以下の通りです:


`[variable, min, max]`


プロットを、離散形式やパラメトリック形式で定義することもできます。
離散形式は既定の座標で表された点の集合をプロットするのに使われます。
離散プロットは、キーワード*discrete*で始まり、
値についてのリスト1つか2つが続くリストで定義されます。
もし2つのリストが与えられたら、それらは同じ長さを持たなければいけません;
1番目のリストはプロットされる点のx座標として、
2番目のリストはy座標として解釈されます。
もし*discrete*キーワードの後、1つのリストだけ与えられたら、
リスト上のそれぞれの要素は、点のxとy座標に対応する2つの値を持つリストでなければいけません。


パラメトリックプロットは、
キーワード*parametric*で始まり、
2つの式か関数名と、パラメータの範囲が続くリストで定義されます。
パラメータの範囲は、パラメータ名とその最小値、最大値が続くリストでなければいけません:


`[param, min, max]`。


*param*が*min*から*max*に増えるにつれ、
2つの式または関数で与えられる座標の点によって描かれる軌跡をプロットは表示します。


垂直軸の範囲は以下の形式を持つオプション引数です:


`[y, min, max]`(キーワード*y*はいつも垂直軸に使われます)。


もしこのオプションを使ったなら、
プロットが到達する値と別に、ちょうどオプションの垂直範囲をプロットは表示します。
もし垂直範囲を指定しなかったなら、プロット点のy座標の最小値と最大値に従って、
垂直範囲が設定されます。


他のすべてのオプションも、
キーワードで始まり、1つか複数の値が続くリストでなければいけません。
`plot_options`を参照してください。


もし複数のプロットがプロットされるなら、式のそれぞれを識別するために凡例が書かれます。
その凡例で使われるラベルは、オプション*legend*で与えることができます。
もしそのオプションが使われないなら、Maximaは式や関数名からラベルを生成します。



**例:**


よくある関数のプロット:






```maxima
(%i1) plot2d (sin(x), [x, -%pi, %pi])$
```


![./figures/plotting2](./figures/plotting2.png)

もし関数の増大が速すぎるなら、yオプションを使って、垂直軸の値を制限する必要があるかもしれません:






```maxima
(%i1) plot2d (sec(x), [x, -2, 2], [y, -20, 20])$
plot2d: some values were clipped.
```


![./figures/plotting3](./figures/plotting3.png)

プロットの外観は使うプロットプログラムに依存して異なるかもしれません。
プロットボックスが使用不可能になっている時、Xmaximaは矢印を使って軸をプロットします:







```maxima
(%i1) plot2d ( x^2-1, [x, -3, 3], [y, -2, 10],
                      [box, false], [plot_format, xmaxima])$
```


![./figures/plotting1](./figures/plotting1.png)

対数プロットの例:






```maxima
(%i11) plot2d (exp(3*s), [s, -2, 2], [logy])$
```


![./figures/plotting4](./figures/plotting4.png)

関数を名前でプロット:









```maxima
(%i1) F(x) := x^2 $

(%i2) :lisp (defun |$g| (x) (m* x x x))
$g

(%i2) H(x) := if x < 0 then x^4 - 1 else 1 - x^5 $
(%i3) plot2d ([F, G, H], [u, -1, 1], [y, -1.5, 1.5])$
```


![./figures/plotting5](./figures/plotting5.png)

パラメトリックに定義されたバタフライカーブのプロット:








```maxima
(%i1) r: (exp(cos(t))-2*cos(4*t)-sin(t/12)^5)$
(%i2) plot2d([parametric, r*sin(t), r*cos(t), 
             [t, -8*%pi, 8*%pi], [nticks, 2000]])$
```


![./figures/plotting6](./figures/plotting6.png)

7点だけでプロットする時の2回転「円」:







```maxima
(%i1) plot2d ([parametric, cos(t), sin(t),
              [t, -2*%pi, 2*%pi], [nticks, 8]])$
```


![./figures/plotting7](./figures/plotting7.png)

円のパラメトリック表現と一緒に、よくある関数のプロット。
プロットのサイズは、円を丸く、楕円のように変形しないように、
xとyオプションで調整されています。
これらの値は、このプロットを生成するのに使われたPostscript端末ではうまく機能します;
あなたはあなたのスクリーンのために値を調整しなければいけないかもしれません。








```maxima
(%i1) plot2d([[parametric, cos(t), sin(t),
              [t,0,2*%pi], [nticks, 80]],
        abs(x)], [x,-2,2], [y, -1.5, 1.5])$
plot2d: some values were clipped.
```


![./figures/plotting8](./figures/plotting8.png)

x座標、y座標を別々に定義した点の離散集合のプロット:







```maxima
(%i1) plot2d ([discrete, [10, 20, 30, 40, 50],
                         [.6, .9, 1.1, 1.3, 1.4]])$
```


![./figures/plotting9](./figures/plotting9.png)

それぞれの点を別々に定義し、点を繋ぐ線をなくした、前の例で示された同じ点:








```maxima
(%i1) plot2d([discrete, [[10, .6], [20, .9], [30, 1.1],
                         [40, 1.3], [50, 1.4]]],
                        [style, points])$
```


![./figures/plotting10](./figures/plotting10.png)

この例では、3つの列を持つテーブルがファイル”data.txt”に保存され、
読み込まれ、2番目、3番目の列は2つの軸上にプロットされます:










```maxima
(%i1) with_stdout ("data.txt", for x:0 thru 10 do 
                                   print (x, x^2, x^3))$
(%i2) data: transpose ( read_matrix ("data.txt"))$

(%i3) plot2d ([discrete, transpose(data)[2], transpose(data)[3]],
  [style,points], [point_type,diamond], [color,red])$
```


![./figures/plotting11](./figures/plotting11.png)

実験データ点を、データを予測する理論的関数と一緒にプロット:












```maxima
(%i1) xy: [[10, .6], [20, .9], [30, 1.1], [40, 1.3], [50, 1.4]]$

(%i2) plot2d([[discrete, xy], 2*%pi*sqrt(l/980)], [l,0,50],
        [style, points, lines], [color, red, blue],
        [point_type, asterisk],
        [legend, "experiment", "theory"],
        [xlabel, "pendulum's length (cm)"],
        [ylabel, "period (s)"])$
```


![./figures/plotting12](./figures/plotting12.png)

プロットオプションに関する節も参照してください。

<!-- category: Plotting -->
<!-- keywords: plot3d -->
<!-- signatures: plot3d(expr, x_range, y_range, ..., options, ...), plot3d([expr_1, expr_2, expr_3], x_range, y_range, ..., options, ...) -->
### Function: plot3d (expr, x_range, y_range, ..., options, ...)

２変数関数もしくはパラメトリック形式で定義された、１つか複数の表面のプロットを表示します。


プロットされる関数は、式か関数名として指定できます。
違った側面から表面を見るためにマウスを使ってプロットを回転することができます。


**例:**


よくある関数のプロット:






```maxima
(%i1) plot3d (2^(-u^2 + v^2), [u, -3, 3], [v, -2, 2]);
```


![./figures/plotting13](./figures/plotting13.png)

無限大に発散する関数を制限するためのzオプションの使用(この場合、関数はxとy軸上でマイナス無限だい);
これは線のみ陰影なしでプロットする仕方も示します。







```maxima
(%i1) plot3d ( log ( x^2*y^2 ), [x, -2, 2], [y, -2, 2], [z, -8, 4],
               [palette, false], [color, magenta, blue])$
```


![./figures/plotting14](./figures/plotting14.png)

zの無限大は、いかなる漸近線上にも落ちないグリッドを選ぶことによっても避けることができます;
この例は事前に定義されたパレットの1つ、この場合4番目のものを選択する仕方も示します:








```maxima
(%i1) plot3d( log (x^2*y^2), [x, -2, 2], [y, -2, 2], 
         [grid, 29, 29],
         [palette, get_plot_option(palette,5)])$
```


![./figures/plotting15](./figures/plotting15.png)

同じ領域を共有する同じプロットでの2つの表面;
gnuplotでは2つの表面は同じパレットを使用します:







```maxima
(%i1) plot3d ([2^(-x^2 + y^2), 4*sin(3*(x^2+y^2))/(x^2+y^2),
              [x, -3, 3], [y, -2, 2]])$
```


![./figures/plotting16](./figures/plotting16.png)

異なる領域を持つ、同じ2つの表面;
xmaximaでは、それぞれの表面は、オプションパレットで定義されたリストから選ばれた
異なるパレットを使います:








```maxima
(%i1) plot3d ( [[2^(-x^2 + y^2),[x,-2,2],[y,-2,2]],
         4*sin(3*(x^2+y^2))/(x^2+y^2),
         [x, -3, 3], [y, -2, 2]], [plot_format,xmaxima])$
```


![./figures/plotting17](./figures/plotting17.png)

パラメトリックに定義されたKleinの壷のプロット:










```maxima
(%i1) expr_1:5*cos(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3.0)-10.0$
(%i2) expr_2:-5*sin(x)*(cos(x/2)*cos(y) + sin(x/2)*sin(2*y) + 3.0)$
(%i3) expr_3: 5*(-sin(x/2)*cos(y) + cos(x/2)*sin(2*y))$

(%i4) plot3d ([expr_1, expr_2, expr_3], [x, -%pi, %pi],
        [y, -%pi, %pi], [grid, 40, 40])$
```


![./figures/plotting18](./figures/plotting18.png)

球座標から直交座標に変換するのにあらかじめ定義された変換`spherical_to_xyz`
を使った球調和のプロット。
`spherical_to_xyz`に関するドキュメンテーションを参照してください。








```maxima
(%i1) plot3d (sin(2*theta)*cos(phi), [theta, 0, %pi],
              [phi, 0, 2*%pi],
              [transform_xy, spherical_to_xyz], [grid,30,60])$
```


![./figures/plotting19](./figures/plotting19.png)

円筒座標から直交座標に変換するのにあらかじめ定義された変換`polar_to_xyz`
を使った球面調和関数のプロット。
`polarl_to_xyz`に関するドキュメンテーションを参照してください。
この例は境界ボックスと凡例を消去する仕方も示します。








```maxima
(%i1) plot3d (r^.33*cos(th/3), [r, 0, 1], [th, 0, 6*%pi],
         [grid, 12, 80],
         [transform_xy, polar_to_xy], [box, false],
         [legend,false])$
```


![./figures/plotting20](./figures/plotting20.png)

球座標から直交座標への変換を使っての球のプロット。
xmaximaでは、球の対称形を維持するように3つの軸は同じ比でスケールされます。
同一色で異なる陰影のパレットが使われます:









```maxima
(%i1) plot3d ( 5, [theta, 0, %pi], [phi, 0, 2*%pi],
         [plot_format,xmaxima],
         [transform_xy, spherical_to_xyz],
         [palette,[value,0.65,0.7,0.1,0.9]])$
```


![./figures/plotting21](./figures/plotting21.png)

行列を使った2変数関数の定義。
関数の定義の中のシングルクォートに注意してください。
行列が整数添字を要求する状況に実際に至る時、plot3dが失敗しないためのものです。









```maxima
(%i1) M: matrix([1, 2, 3, 4], [1, 2, 3, 2], [1, 2, 3, 4],
                [1, 2, 3, 3])$
(%i2) f(x, y) := float('M [round(x), round(y)])$

(%i3) plot3d (f(x,y), [x, 1, 4], [y, 1, 4], [grid, 4, 4])$
apply: subscript must be an integer; found: round(x)
```


![./figures/plotting22](./figures/plotting22.png)

elevationを零の等しく設定することで，
表面は地図として見ることができます。
その地図は、それぞれの色は違ったレベルを表現します。
オプション`colorbox`は、
色とレベルの対応を示すのに使われます。
メッシュ線を使用不可にし、色が見やすいようにしています。







```maxima
(%i1) plot3d (cos (-x^2 + y^3/4), [x, -4, 4], [y, -4, 4],
        [mesh_lines_color, false], [elevation, 0], [azimuth, 0],
        [colorbox, true], [grid, 150, 150])$
```


![./figures/plotting23](./figures/plotting23.png)

プロットオプションについての節も参照してください。

<!-- category: Plotting -->
<!-- keywords: plot_format -->
<!-- signatures: plot_format[plot_format, format] -->
### Variable: plot_format

ここで*format*は以下のいずれかです;
gnuplot, xmaxima, mgnuplot, gnuplot_pipes.


プロットで使われるフォーマットを設定します。


デフォルト値: Windowsシステムではgnuplot, 他のシステムではgnuplot_pipes

<!-- category: Plotting -->
<!-- keywords: plot_options -->
<!-- signatures: plot_options -->
### Variable: plot_options

このリストの要素は、プロットのデフォルトオプションを指定します。
もし`plot2d`もしくは`plot3d`がコールされる時、オプションが指定されたら、
その値は、デフォルトオプションより優先されます。
そうでなければ、`plot_options`の中の値が使われます。
デフォルトオプションは、`set_plot_option`を使って割り当てられます。
それぞれのプロットコマンドに特化したローカルオプションがあり、それらは、この、グローバルオプションのリストには含まれません。


`plot_options`のそれぞれの要素は、２つ以上の項目のリストです。
最初の項目はオプション名で、残りはオプションに割り当てられる値です。
いくつかの場合、割り当てられた値はリストであり、複数の項目からなることがあります。


`set_plot_option`と`get_option`、プロットオプションの節も参照してください。

<!-- category: Plotting -->
<!-- keywords: plot_real_part -->
<!-- signatures: plot_real_part[plot_real_part, symbol] -->
### Variable: plot_real_part

`true`に設定される時、プロットされる関数は
実数値がプロットされる複素関数と見なされます;
これは`realpart(function)`をプロットすることと同値です。
もし`false`に設定されたら、
関数が実数値を与えない時には何も表示されません。
例えば、`x`が負の時、`log(x)`は、
実数値が`log(abs(x))`に等しい複素数値を与えます;
もし`plot_real_part` が`true`だったなら、
`log(-5)`は`log(5)`としてプロットされますが、
もし`plot_real_part` が`false`だったなら、
何もプロットされません。


デフォルト値: `false`

<!-- category: Plotting -->
<!-- keywords: point_type -->
<!-- signatures: point_type[point_type, type_1, ..., type_n] -->
### Variable: point_type

gnuplotでは、
, each set of points to be plotted with the style 
スタイル“points”か“linespoints”でプロットされた点のそれぞれの集合は
このリストから取られたオブジェクトで順に表されます。
もしこのリスト内のオブジェクト以上に点の集合があるなら、
それらは順に繰り返されます。
使うことができる可能なオブジェクト: bullet, circle, plus, times,
asterisk, box, square,triangle, delta, wedge, nabla, diamond, lozenge


デフォルト値: bullet, circle, plus, times, asterisk, box, square,triangle, delta, wedge, nabla, diamond, lozenge

<!-- category: Plotting -->
<!-- keywords: polar_to_xy -->
<!-- signatures: polar_to_xy -->
### Function: polar_to_xy

plot3dの`transform_xy`オプションに対する値として与えることができます。
その効果はplot3dの2つの独立変数をz軸からの距離と方位角(極座標)として通訳し、
それらをxとy座標に変換することです。

<!-- category: Plotting -->
<!-- keywords: psfile -->
<!-- signatures: psfile[psfile, string] -->
### Variable: psfile

このオプションは、プロットをスクリーンに表示する代わりに、
*string*に等しい名前のポストスクリプトファイルに保存します。
デフォルトでは、そのファイルは、変数*maxima_tempdir*で定義されたディレクトリに
生成されます;
変数の値を変えて、違うディレクトリにファイルを保存できます。

<!-- category: Plotting -->
<!-- keywords: run_viewer -->
<!-- signatures: run_viewer[run_viewer, symbol] -->
### Variable: run_viewer

プロットフォーマット用の適切なビューアを走らせるかどうか制御します。



デフォルト値: `true`

<!-- category: Plotting -->
<!-- keywords: set_plot_option -->
<!-- signatures: set_plot_option(option) -->
### Function: set_plot_option (option)

プロットオプションの節にリストされているオプションのほとんどを受け付け、
それらをグローバル変数`plot_options`に保存します。


`set_plot_option`は引数を評価し、
(与えられたオプションを変更した後、)完全なリスト`plot_options`を返します。


`plot_options`と`get_option`、プロットオプションの節も参照してください。



例:


`grid`値の変更。






```maxima
(%i1) set_plot_option ([grid, 30, 40]);

(%o1) [[t, - 3, 3], [grid, 30, 40], [transform_xy, false], 
[run_viewer, true], [axes, true], [plot_format, gnuplot_pipes], 
[color, blue, red, green, magenta, black, cyan], 
[point_type, bullet, circle, plus, times, asterisk, box, square, 
triangle, delta, wedge, nabla, diamond, lozenge], 
[palette, [hue, 0.25, 0.7, 0.8, 0.5], 
[hue, 0.65, 0.8, 0.9, 0.55], [hue, 0.55, 0.8, 0.9, 0.4], 
[hue, 0.95, 0.7, 0.8, 0.5]], [gnuplot_term, default], 
[gnuplot_out_file, false], [nticks, 29], [adapt_depth, 5], 
[gnuplot_preamble, ], [gnuplot_default_term_command, 
set term pop], [gnuplot_dumb_term_command, set term dumb 79 22], 
[gnuplot_ps_term_command, set size 1.5, 1.5;set term postscript ¥
eps enhanced color solid 24], [plot_realpart, false]]
```

<!-- category: Plotting -->
<!-- keywords: spherical_to_xyz -->
<!-- signatures: spherical_to_xyz -->
### Function: spherical_to_xyz

plot3dの`transform_xy`オプションに対する値として与えることができます。
その効果はplot3dでの2つの独立変数と関数を点の球座標
(1番目はz軸に対する角度、次にxy射影のx軸に対する角度、最後に原点からの距離)
として解釈し、それらをx,y,z座標に変換することです。

<!-- category: Plotting -->
<!-- keywords: style -->
<!-- signatures: style[style, type_1, ..., type1_n], style[style, [style_1], ..., [style_n]] -->
### Variable: style

様々な関数やデータ一式のために2dプロットで使われるスタイル。
単語*style*の後には、１つ以上のスタイルが続きます。
もし与えられたスタイルよりも多くの関数やデータ集合があったら、スタイルは繰り返されます。
それぞれのスタイルは、実線のためには*lines*、孤立点のためには*points*、
線分と孤立点のためには*linespoints*、点線のためには*dots*を取り得ます。
Gnuplotでは、*impulses*スタイルも使えます。


スタイルのそれぞれは、いくつかの追加のパラメータとリストの中に入れることができます。
*lines*は、１つか２つの数を取ります: 線の太さと、色を指定する整数。
デフォルトの色コードは、1: 青, 2: 赤, 3: マゼンタ, 4: オレンジ, 5: ブラウン, 6: ライム, 7: アクア、です。
もしX11ではない端末でGnuplotを使うなら、これらの色は、違っているかもしれません;
例えば、もしオプション[*gnuplot_term*,*ps*]を使うなら、色インデックス4は、
オレンジではなく、黒に対応します。


*points*は、１つか２つか３つのパラメータを取ります; 最初のパラメータは、点の半径、
２番目のパラメータは、同じ色を選択する（*lines*で使われるコードと同じ）整数、
３番目のパラメータは現在、Gnuplotでだけ使われており、点の代わりにいくつかのオブジェクトに対応します。オブジェクトのデフォルト値は、1: 黒丸, 2: 白丸, 3: 十字, 4: ×,
5: 米印, 6: 黒四角, 7: 白四角, 8: 黒三角, 9: 白三角, 10: 黒逆三角, 11: 白逆三角,
12: 黒菱形, 13: 白菱形、です。


*linesdots*は、４つまでのパラメータを取ります;
線の太さ、点の半径、色、点を置き換えるオブジェクトのタイプ。


デフォルト値: *lines* (太さ1で、オプション`color`で与えられた最初の色を持つ線で結んだ点一式をプロットします)


`color`と`point_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: t -->
<!-- signatures: t[t, min, max] -->
### Variable: t

パラメトリックプロットのデフォルトの範囲。


デフォルト値: -3, 3

<!-- category: Plotting -->
<!-- keywords: transform_xy -->
<!-- signatures: transform_xy[transform_xy, symbol] -->
### Variable: transform_xy

ここで、*symbol*は`false`か
関数`transform_xy`を使うことで得られる結果をとり得ます。
もし`false`と違うなら、
plot3dで3座標を変換するのに使われます。


デフォルト値: `false`


`make_transform`, `polar_to_xy`, `spherical_to_xyz`を参照してください。

<!-- category: Plotting -->
<!-- keywords: x -->
<!-- signatures: x[x, min, max] -->
### Variable: x

2dプロットコマンドの最初の(またはplot3dの最初の二つのどちらかの)
オプションとして使われる時、
1番目の独立変数がxであることを示し、その範囲を設定します。
最初のオプションの後(またはplot3dでは2番目のオプションの後)、
プロット内で示される有効な水平領域を定義するために、
再び使うことができます。

<!-- category: Plotting -->
<!-- keywords: xlabel -->
<!-- signatures: xlabel[xlabel, string] -->
### Variable: xlabel

1番目の軸をラベルする*string*を指定します;
もしこのオプションが使われないなら、
plot2dかimplicit_plotで関数をプロットする時、そのラベルは独立変数の名前です。
plot3dで表面を、もしくはcontour_plotで等高線をプロットする時、
そのラベルは1番目の変数の名前です。
パラメトリックプロットの場合、1番目の式です。
*set_plot_option*では使うことはできません。

<!-- category: Plotting -->
<!-- keywords: y -->
<!-- signatures: y[y, min, max] -->
### Variable: y

plot3dでの最初の2つのオプションの1つとして使われる時、
独立変数の1つがyであることを示し、その範囲を設定します。
そうでなければ、
プロットで示される2番目の変数の有効領域を定義します。

<!-- category: Plotting -->
<!-- keywords: ylabel -->
<!-- signatures: ylabel[ylabel, string] -->
### Variable: ylabel

二番目の軸をラベルする*string*を指定します;
もしこのオプションが使われないなら、
plot2dやimplicit_plotで関数をプロットする時、そのラベルは、”y”となり、
plot3dで表面をプロットするときや、contour_plotで等高線をプロットする時、
二番目の変数名となり、
パラメトリックプロットの場合には、二番目の式になります。
*set_plot_option*では使うことはできません。

<!-- category: Plotting -->
<!-- keywords: z -->
<!-- signatures: z[z, min, max] -->
### Variable: z

プロットで示されるzの値の有効範囲を設定するためにplot3dで使われます。

<!-- category: Plotting -->
<!-- keywords: zlabel -->
<!-- signatures: zlabel[zlabel, string] -->
### Variable: zlabel

plot3dを使う時、第三軸をラベルする*string*を指定します。
もしこのオプションが使われないなら、
そのラベルは、
表面をプロットする時は“z”となり、
パラメトリックプロットの場合には三番目の式になります。
*set_plot_option*では使うことはできません。
また、plot2d, implicit_plotでは無視されます。

