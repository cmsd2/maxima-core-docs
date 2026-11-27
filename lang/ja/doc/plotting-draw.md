## draw

<!-- category: Plotting -->
<!-- keywords: axis_3d -->
<!-- signatures: axis_3d -->
### Variable: axis_3d

デフォルト値: `true`


もし`axis_3d`が`true`なら、
*x*, *y* *z*軸が3dシーンで表示されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(axis_3d = false,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```


2dでの軸に関しては、
`axis_bottom`,  `axis_left`, `axis_top`, `axis_right`も
参照してください。

<!-- category: Plotting -->
<!-- keywords: axis_bottom -->
<!-- signatures: axis_bottom -->
### Variable: axis_bottom

デフォルト値: `true`


もし`axis_bottom`が`true`なら、
底の軸は2dシーンで表示されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_bottom = false,
             explicit(x^3,x,-1,1))$
```


`axis_left`,  `axis_top`, `axis_right`, `axis_3d`も参照してください。

<!-- category: Plotting -->
<!-- keywords: axis_left -->
<!-- signatures: axis_left -->
### Variable: axis_left

デフォルト値: `true`


もし`axis_left`が`true`なら、
左の軸が2dシーンで表示されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_left = false,
             explicit(x^3,x,-1,1))$
```


`axis_bottom`,  `axis_top`, `axis_right`, `axis_3d`も参照してください。

<!-- category: Plotting -->
<!-- keywords: axis_right -->
<!-- signatures: axis_right -->
### Variable: axis_right

デフォルト値: `true`


もし`axis_right`が`true`なら、
2dシーンで右軸が表示されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_right = false,
             explicit(x^3,x,-1,1))$
```


`axis_bottom`,  `axis_left`, `axis_top`, `axis_3d`も
参照してください。

<!-- category: Plotting -->
<!-- keywords: axis_top -->
<!-- signatures: axis_top -->
### Variable: axis_top

デフォルト値: `true`


もし`axis_top`が`true`なら、
上部の軸が2dシーンで表示されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_top = false,
             explicit(x^3,x,-1,1))$
```


`axis_bottom`,  `axis_left`, `axis_right`, `axis_3d`も参照してください。

<!-- category: Plotting -->
<!-- keywords: background_color -->
<!-- signatures: background_color -->
### Variable: background_color

デフォルト値: `white`


端末`gif`, `png`, `jpg`, `gif`のための背景色を設定します。
デフォルト背景色は白です。


`color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: bars -->
<!-- signatures: bars([x1, h1, w1], [x2, h2, w2, ...]) -->
### Function: bars ([x1, h1, w1], [x2, h2, w2, ...])

2D内に垂直バーを描画します。


**2D**


`bars ([x1,h1,w1], [x2,h2,w2, ...])` 
は
値*x1*, *x2*, ...に中心を持ち、高さ*h1*, *h2*, ...と幅*w1*, *w2*, ...を持つバーを描画します。


このオブジェクトは以下の*graphic options*に影響されます: `key`, 
`fill_color`, `fill_density`, `line_width`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
       key          = "Group A",
       fill_color   = blue,
       fill_density = 0.2,
       bars([0.8,5,0.4],[1.8,7,0.4],[2.8,-4,0.4]),
       key          = "Group B",
       fill_color   = red,
       fill_density = 0.6,
       line_width   = 4,
       bars([1.2,4,0.4],[2.2,-2,0.4],[3.2,5,0.4]),
       xaxis = true);
```

<!-- category: Plotting -->
<!-- keywords: border -->
<!-- signatures: border -->
### Variable: border

デフォルト値: `true`


もし`border`が`true`なら、
ポリゴンの境界は`line_type`と`line_width`に従って塗られます。


このオプションは以下のグラフィックオブジェクトに影響します:


- *
`gr2d`: `polygon`, `rectangle`, と`ellipse`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(color       = brown,
             line_width  = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: boundaries_array -->
<!-- signatures: boundaries_array -->
### Variable: boundaries_array

デフォルト値: `false`


`boundaries_array`は
グラフィックオプション`geomap`が境界座標を探すところです。


Each component of 
`boundaries_array`のそれぞれの成分は
浮動小数点量の配列であり、
多角形のセグメントかマップ境界の座標です。


`geomap`も参照してください。

<!-- category: Plotting -->
<!-- keywords: cbrange -->
<!-- signatures: cbrange -->
### Variable: cbrange

デフォルト値: `auto`


もし`cbrange`が`auto`なら
`enhanced3d`が`false`でない時
色付けられる値の範囲は自動的に計算されます。
カラー範囲外の値は、最も近い端の色を使います。


`enhanced3d`や`colorbox`が`false`の時、
オプション`cbrange`は効果を持ちません。


もしユーザーが
色付けられた値の特定の区間が欲しいなら、
`cbrange=[-2, 3]`のようにMaximaリストとして与えられなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d (
        enhanced3d     = true,
        color          = green,
        cbrange = [-3,10],
        explicit(x^2+y^2, x,-2,2,y,-2,2)) $
```


`enhanced3d`, `colorbox`, `cbtics`も参照してください。

<!-- category: Plotting -->
<!-- keywords: cbtics -->
<!-- signatures: cbtics -->
### Variable: cbtics

デフォルト値: `auto`


このグラフィックオプションは、
オプション`enhanced3d`が`false`でない時、
カラーボックス上にチックマークを描く方法を制御します。


`enhanced3d`か`colorbox`が`false`の時、
オプション`cbtics`は効果を持ちません。


完全な記述に関しては、`xtics`を参照してください。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d (
        enhanced3d = true,
        color      = green,
        cbtics  = {["High",10],["Medium",05],["Low",0]},
        cbrange = [0, 10],
        explicit(x^2+y^2, x,-2,2,y,-2,2)) $
```


`enhanced3d`, `colorbox`, `cbrange`も参照してください。

<!-- category: Plotting -->
<!-- keywords: columns -->
<!-- signatures: columns -->
### Variable: columns

デフォルト値: 1


`columns`は多重プロットでの列の数です。


これはグローバルグラフィックオプションなので、
シーン記述での位置はかまいません。
関数`draw`の引数として使うこともできます。


例:



```maxima
(%i1) load("draw")$
(%i2) scene1: gr2d(title="Ellipse",
                   nticks=30,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i3) scene2: gr2d(title="Triangle",
                   polygon([4,5,7],[6,4,2]))$
(%i4) draw(scene1, scene2, columns = 2)$
```

<!-- category: Plotting -->
<!-- keywords: contour -->
<!-- signatures: contour -->
### Variable: contour

デフォルト値: `none`


オプション`contour`を使うと、ユーザーは
等高線をプロットする場所を選択できます。
可能な値は以下の通りです:



- *
`none`:
等高線がプロットされません。
- *
`base`:
等高線がxy平面上に射影されます。
- *
`surface`:
等高線が表面にプロットされます。
- *
`both`:
2つの等高線がプロットされます:xy平面上と表面と。
- *
`map`:
等高線がxy平面上に射影されて、観点がちょうど垂直に設定されます。


これはグローバルグラフィックオプションなので、
シーン記述での位置はかまいません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 15,
             contour        = both,
             surface_hide   = true) $
```

<!-- category: Plotting -->
<!-- keywords: contour_levels -->
<!-- signatures: contour_levels -->
### Variable: contour_levels

デフォルト値: 5


このグラフィックオプションは、
等高線が描かれる方法を制御します。
`contour_levels`は、正の整数、3つの数のリスト、または、
数の任意の集合に設定することができます:



- *
オプション`contour_levels`が正の整数*n*にバインド(bounded)されている時、
*n*この等高線が等しい間隔で描かれます。
デフォルトでは、
5つの等しく間隔の空けられた等高線がプロットされます。
- *
オプション`contour_levels`が
形式`[lowest,s,highest]`の長さ3のリストにバインド(bounded)されている時、
等高線は
`lowest`から`highest`へ`s`個のステップでプロットされます。
- *
オプション`contour_levels`が
形式`{n1, n2, ...}`の数の集合にバインド(bounded)されている時、
等高線は
値`n1`, `n2`, ...にプロットされます。


これはグローバルグラフィックオプションなので、
シーン記述での位置はかまいません。


例:


10の等しく間隔の空けられた等高線。
レベルの実際の数は簡単なラベルを与えるために調整することができます。


```maxima
(%i1) load("draw")$
(%i2) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 10,
             contour        = both,
             surface_hide   = true) $
```



-8から8まで4つのステップで。


```maxima
(%i1) load("draw")$
(%i2) draw3d(color = green,
             explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = [-8,4,8],
             contour        = both,
             surface_hide   = true) $
```


レベル-7, -6, 0.8, 5での等値線。


```maxima
(%i1) load("draw")$
(%i2) draw3d(color = green,
             Explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             Contour_levels = {-7, -6, 0.8, 5},
             Contour        = both,
             Surface_hide   = true) $
```


`contour`も参照してください。

<!-- category: Plotting -->
<!-- keywords: cylindrical -->
<!-- signatures: cylindrical(radius, z, minz, maxz, azi, minazi, maxazi) -->
### Function: cylindrical (radius, z, minz, maxz, azi, minazi, maxazi)

円柱座標で定義された3D関数を描画します。


**3D**


`cylindrical (radius, z, minz, maxz, azi, minazi, maxazi)`は
*minz*から*maxz*までの値を取る*z*と
*minazi*から*maxazi*まで値を取る*方位角* *azi*を伴う
円柱座標で定義された関数`radius(z,azi)`
をプロットします。


このオブジェクトは以下の*グラフィックオプション*に影響されます:
`xu_grid`, 
`yv_grid`, `line_type`, `key` and `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(cylindrical(1,z,-2,2,az,0,2*%pi))$
```

<!-- category: Plotting -->
<!-- keywords: data_file_name -->
<!-- signatures: data_file_name -->
### Variable: data_file_name

デフォルト値: `"data.gnuplot"`


これは、
リクエストされたプロットを構築するためにGnuplotが必要とする数値データを含む
ファイルの名前です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。
関数`draw`の引数としても使うことができます。


`gnuplot_file_name`の中で例を参照してください。

<!-- category: Plotting -->
<!-- keywords: delay -->
<!-- signatures: delay -->
### Variable: delay

デフォルト値: 5


これは
アニメーションgifファイルにおけるフレームの1/100秒単位の遅延です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。
関数`draw`の引数としても使うことができます。


例:



```maxima
(%i1) load("draw")$
(%i2) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


オプション`delay`はアニメーションgifに関してだけアクティブです;
他のいかなる場合も無視されます。


`terminal`, `dimensions`も参照してください。

<!-- category: Plotting -->
<!-- keywords: dimensions -->
<!-- signatures: dimensions -->
### Variable: dimensions

デフォルト値: `[600,500]`


出力端末の寸法。
その値は、幅と高さで形成されるリストです。
2つの数の意味は使っている端末に依存します。


端末`gif`, `animated_gif`, `png`, `jpg`,
`svg`, `screen`, `wxt`, `aquaterm`では、
整数はそれぞれの方向の点の数を表します。
もし整数でないなら、丸められます。


端末`eps`, `eps_color`, `pdf`, `pdfcairo`では、
両方の数は1/100cm単位の長さを表します。
デフォルトでは、これらのフォーマットでの画像は幅6cm、高さ5cmであることを意味します。


これはグローバルグラフィックオプションなので、
シーン記述での位置は関係ありません。
関数`draw`の引数として使われることもあります。


例:


ファイル出力とwxtキャンバスに適用されたオプション`dimensions`。



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        dimensions = [300,300],
        terminal   = 'png,
        explicit(x^4,x,-1,1)) $
(%i3) draw2d(
        dimensions = [300,300],
        terminal   = 'wxt,
        explicit(x^4,x,-1,1)) $
```


eps出力に適用されたオプション`dimensions`。
A4縦寸法のepsファイルが欲しいです。



```maxima
(%i1) load("draw")$
(%i2) A4portrait: 100*[21, 29.7]$
(%i3) draw3d(
        dimensions = A4portrait,
        terminal   = 'eps,
        explicit(x^2-y^2,x,-2,2,y,-2,2)) $
```

<!-- category: Plotting -->
<!-- keywords: draw -->
<!-- signatures: draw(gr2d, ..., gr3d, ..., options, ...) -->
### Function: draw (gr2d, ..., gr3d, ..., options, ...)

一連のシーンをプロットします;
引数は`gr2d`や`gr3d`のオブジェクトといくつかのオプションです。
デフォルトでは、シーンは1列の中に一緒に置かれます。


関数`draw`は以下のグローバルオプションを受け付けます: `terminal`,
`columns`, `dimensions`, `file_name`, `delay`.


関数`draw2d`や`draw3d`は
それぞれ、2次元と3次元に関して、１つのシーンだけが要求される時に使われる
ショートカットです。


`gr2d`と`gr3d`も参照してください。


この関数を利用するには、最初に`load("draw")`を書いてください。


例:



```maxima
(%i1) load("draw")$
(%i2) scene1: gr2d(title="Ellipse",
                   nticks=30,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i3) scene2: gr2d(title="Triangle",
                   polygon([4,5,7],[6,4,2]))$
(%i4) draw(scene1, scene2, columns = 2)$
```


2つの描画文は同値です:


```maxima
(%i1) load("draw")$
(%i2) draw(gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1)));
(%o2)                          [gr3d(explicit)]
(%i3) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1));
(%o3)                          [gr3d(explicit)]
```


アニメーティドgifファイル:


```maxima
(%i1) load("draw")$
(%i2) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


`gr2d`, `gr3d`, `draw2d`, `draw3d`も参照してください。

<!-- category: Plotting -->
<!-- keywords: draw2d -->
<!-- signatures: draw2d(option, graphic_object, ...) -->
### Function: draw2d (option, graphic_object, ...)

この関数は
`draw(gr2d(options, ..., graphic_object, ...))`.
のショートカットです。


2dで唯一のシーンをプロットするのに使うことができます。


この関数を利用するには、最初に`load("draw")`を書いてください。


`draw`と`gr2d`も参照してください。

<!-- category: Plotting -->
<!-- keywords: draw3d -->
<!-- signatures: draw3d(option, graphic_object, ...) -->
### Function: draw3d (option, graphic_object, ...)

この関数は
`draw(gr3d(options, ..., graphic_object, ...))`
のショートカットです。


3dでユニークなシーンをプロットするのに使うことができます。


この関数を利用するには、最初に`load("draw")`を書いてください。


`draw`と`gr3d`も参照してください。

<!-- category: Plotting -->
<!-- keywords: draw_file -->
<!-- signatures: draw_file(graphic option, ..., graphic object, ...) -->
### Function: draw_file (graphic option, ..., graphic object, ...)

現在のプロットをファイルに保存します。
受け付けられるグラフィックオプションは以下です:
`terminal`, `dimensions`, `file_name`, `file_bgcolor`. 


例:



```maxima
(%i1) load("draw")$
(%i2) /* screen plot */
      draw(gr3d(explicit(x^2+y^2,x,-1,1,y,-1,1)))$
(%i3) /* same plot in eps format */
      draw_file(terminal  = eps,
                dimensions = [5,5]) $
```

<!-- category: Plotting -->
<!-- keywords: elevation_grid -->
<!-- signatures: elevation_grid(mat, x0, y0, width, height) -->
### Function: elevation_grid (mat, x0, y0, width, height)

3D空間に行列*mat*を描画します。
*x0*から$x0 + width$までの横座標範囲と
*y0*から$y0 + height$までの縦座標範囲で、
*z*値は*mat*から取られます。
要素$a(1,1)$は点$(x0,y0+height)$上に射影され、
$a(1,n)$は$(x0+width,y0+height)$上に射影され、
$a(m,1)$は$(x0,y0)$上に射影され、
$a(m,n)$は$(x0+width,y0)$上に射影されます。


このオブジェクトは以下の*グラフィックオプション*に影響されます: `line_type`,
`line_width`, `key`, `enhanced3d`, `color`。


Maximaの古いバージョンでは、`elevation_grid`は`mesh`と呼ばれました。
`mesh`も参照してください。


例:



```maxima
(%i1) load("draw")$
(%i2) m: apply(
            matrix,
            makelist(makelist(random(10.0),k,1,30),i,1,20)) $
(%i3) draw3d(
         color = blue,
         elevation_grid(m,0,0,3,2),
         xlabel = "x",
         ylabel = "y",
         surface_hide = true);
```

<!-- category: Plotting -->
<!-- keywords: ellipse -->
<!-- signatures: ellipse(xc, yc, a, b, ang1, ang2) -->
### Function: ellipse (xc, yc, a, b, ang1, ang2)

2D内で楕円や円を描画します。



**2D**


`ellipse (xc, yc, a, b, ang1, ang2)`
は
`[xc, yc]`を中心とし、水平と垂直半軸にそれぞれ*a*と*b*を持ち、角度*ang1*から始まり、角度*ang2*に等しい振幅を持つ
楕円をプロットします。


このオブジェクトは以下の*graphic options*に影響されます:
`nticks`, 
`transparent`, `fill_color`, `border`, `line_width`, 
`line_type`, `key`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(transparent = false,
             fill_color  = red,
             color       = gray30,
             transparent = false,
             line_width  = 5,
             ellipse(0,6,3,2,270,-270),
             /* center (x,y), a, b, start & end in degrees */
             transparent = true,
             color       = blue,
             line_width  = 3,
             ellipse(2.5,6,2,3,30,-90),
             xrange      = [-3,6],
             yrange      = [2,9] )$
```

<!-- category: Plotting -->
<!-- keywords: enhanced3d -->
<!-- signatures: enhanced3d -->
### Variable: enhanced3d

デフォルト値: `false`


もし`enhanced3d`が`false`なら、
3dプロットで表面は色付けられません。
もし`enhanced3d`が`true`なら、
Gnuplotのpm3dモードを設定して表面が色付けられます。
もし式が`enhanced3d`に与えられるなら、
それは`palette`に従って色を割り当てるのに使われます;
この式の中の変数は表面記述で使われるものと同じでなければいけません。


如何にパレットが指定されるか知るためには、オプション`palette`を参照してください。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
         surface_hide = true,
         enhanced3d   = true,
         palette      = gray,
         explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
(%i3) draw3d(
         surface_hide = true,
         /* same variables x and y as */
         /* in explicit below:        */
         enhanced3d   = sin(x*y),
         explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
(%i4) draw3d(
         color = blue,
         nticks = 60,
         line_width = 3,
         enhanced3d = (u-1)^2,
         parametric(cos(5*u)^2,sin(7*u),u-2,u,0,2))$
```

<!-- category: Plotting -->
<!-- keywords: error_type -->
<!-- signatures: error_type -->
### Variable: error_type

デフォルト値: `y`


値は`x`, `y`, `xy`を取り得ますが、その値に依存して、
グラフィックオブジェクト`errors`は水平エラーバー、垂直エラーバー、その両方を伴って
点を描画します。
`error_type=boxes`の時、クロスの代わりにボックスが描かれます。


`errors`も参照してください。

<!-- category: Plotting -->
<!-- keywords: errors -->
<!-- signatures: errors([x1, x2, ...], [y1, y2, ...]) -->
### Function: errors ([x1, x2, ...], [y1, y2, ...])

オプション`error_type`の値に依存して、
水平、垂直もしくは両方のエラーバーと共に点を描きます。


**2D**


もし`error_type = x`なら、
`errors`の引数は must be of the form 
形式`[x, y, xdelta]`か`[x, y, xlow, xhigh]`でなければいけません。
もし`error_type = y`なら、
引数は形式`[x, y, ydelta]`か`[x, y, ylow, yhigh]`でなければいけません。
もし`error_type = xy`か`error_type = boxes`なら、
`errors`の引数は
形式`[x, y, xdelta, ydelta]`か`[x, y, xlow, xhigh, ylow, yhigh]`でなければいけません。


`error_type`も参照してください。


このオブジェクトは以下の*グラフィックオブジェクト*によって影響されます:
`error_type`,
`points_joined`, `line_width`, `key`, `line_type`, 
`color`, `fill_density`, `xaxis_secondary`, `yaxis_secondary`.


オプション`fill_density`は、`error_type=boxes`の時だけ有効です。


例:


水平エラーバー。



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        error_type = y,
        errors([[1,2,1], [3,5,3], [10,3,1], [17,6,2]]))$
```


垂直および水平エラーバー。



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        error_type = xy,
        points_joined = true,
        color = blue,
        errors([[1,2,1,2], [3,5,2,1], [10,3,1,1], [17,6,1/2,2]]));
```

<!-- category: Plotting -->
<!-- keywords: explicit -->
<!-- signatures: explicit(fcn, var, minval, maxval), explicit(fcn, var1, minval1, maxval1, var2, minval2, maxval2) -->
### Function: explicit (fcn, var, minval, maxval)

2Dおよび3Dにて陽関数を描画します。


**2D**


`explicit(fcn,var,minval,maxval)`は
*minval*から*maxval*まで値を取る変数*var*を伴う
陽関数*fcn*をプロットします。


このオブジェクトは以下の*graphic options*に影響されます:
`nticks`, 
`adapt_depth`, `line_width`, `line_type`, `key`, 
`filled_func`, `fill_color`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(line_width = 3,
             color      = blue,
             explicit(x^2,x,-3,3) )$
(%i3) draw2d(fill_color  = brown,
             filled_func = true,
             explicit(x^2,x,-3,3) )$
```


**3D**


`explicit(fcn, var1, minval1, maxval1, var2, minval2, maxval2)`は
*minval1*から *maxval1*まで値を取る変数 *var1*と
*minval2*から *maxval2*まで値を取る変数 *var2*を伴う
陽関数 *fcn*をプロットします。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます: `xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `enhanced3d`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(key   = "Gauss",
             color = "#a02c00",
             explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
             yv_grid     = 10,
             color = blue,
             key   = "Plane",
             explicit(x+y,x,-5,5,y,-5,5),
             surface_hide = true)$
```


埋められた関数に関しては`filled_func`も参照してください。

<!-- category: Plotting -->
<!-- keywords: file_name -->
<!-- signatures: file_name -->
### Variable: file_name

デフォルト値: `"maxima_out"`


これは、
端末`png`, `jpg`, `eps`, `eps_color`, `pdf`, `pdfcairo`がグラフィックを保存する
ファイルの名前です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'png)$
```


`terminal`, `dimensions`も参照してください。

<!-- category: Plotting -->
<!-- keywords: fill_color -->
<!-- signatures: fill_color -->
### Variable: fill_color

デフォルト値: `"red"`


`fill_color`はポリゴンと2d `explicit`関数を塗りつぶすための色を指定します。


如何に色が指定されるかを知るには`color`を参照してください。

<!-- category: Plotting -->
<!-- keywords: fill_density -->
<!-- signatures: fill_density -->
### Variable: fill_density

デフォルト値: 0


`fill_density`は、`bars`オブジェクトに関して`fill_color`の強度を指定する0と1の間の数です。


例を見るには`bars`を参照してください。

<!-- category: Plotting -->
<!-- keywords: filled_func -->
<!-- signatures: filled_func -->
### Variable: filled_func

デフォルト値: `false`


オプション`filled_func`は
関数によって制限された領域が如何に塗りつぶされるべきかを
制御します。
`filled_func`が`true`の時、
オブジェクト`explicit`とグラフィックウィンドウの底で定義された関数によって
閉ざされた領域は`fill_color`で塗りつぶされます。
`filled_func`が関数式を含む時、
この関数とオブジェクト`explicit` で定義された関数によって閉ざされた領域が
塗りつぶされます。
デフォルトでは、陽な関数は塗りつぶされません。


このオプションは2dグラフィックオブジェクト`explicit`だけに影響します。


例:


`explicit`オブジェクトとグラフィックウィンドウによって閉ざされた領域。


```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = red,
             filled_func = true,
             explicit(sin(x),x,0,10) )$
```


`explicit`オブジェクト
とオプション`filled_func`で定義された関数によって閉ざされた領域。
`filled_func`の中の変数は must be the same as that used in 
`explicit`の中で使われるものと同じでなければいけないことに注意してください。


```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = grey,
             filled_func = sin(x),
             explicit(-sin(x),x,0,%pi));
```


`fill_color`と`explicit`も参照してください。

<!-- category: Plotting -->
<!-- keywords: font -->
<!-- signatures: font -->
### Variable: font

デフォルト値: `""` (empty string)


このオプションは
端末が使う書体を設定するために使うことができます。
プロットを通して書体とサイズは１つだけ使うことができます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


`font_size`も参照してください。


Gnuplotはそれ自身フォントを扱いません。
異なる端末のサポートライブラリに任せます。
それぞれはフォントに関して独自の哲学を持っています。
簡単なまとめは以下の通りです:



- *
*x11*:
通常のX11フォンとサーバーメカニズムを使います。

例:

```maxima
(%i1) load("draw")$
(%i2) draw2d(font      = "Arial", 
             font_size = 20,
             label(["Arial font, size 20",1,1]))$
```
- *
*windows*:
Windows端末はプロット内部でフォントの変更をサポートしません。
一旦プロットが生成されると、グラフウィンドウのメニューを右クリックしてフォントを変更することができます。
- *
*png, jpeg, gif*:
*libgd*ライブラリは
環境変数`GDFONTPATH`の中に保持されたフォントパスを使います;
この場合、オプション`font`をフォント名に設定することだけが必要です。
フォントファイルへの完全なパスを与えることも可能です。

例:

オプション`font`はフォントファイルへの完全なパスを与えることができます:

```maxima
(%i1) load("draw")$
(%i2) path: "/usr/share/fonts/truetype/freefont/" $
(%i3) file: "FreeSerifBoldItalic.ttf" $
(%i4) draw2d(
        font      = concat(path, file), 
        font_size = 20,
        color     = red,
        label(["FreeSerifBoldItalic font, size 20",1,1]),
        terminal  = png)$
```

もし環境変数`GDFONTPATH`が
フォントファイルが配置されているパスに設定されているなら、
set グラフィックオプション`font`をフォント名に設定することが可能です。

```maxima
(%i1) load("draw")$
(%i2) draw2d(
        font      = "FreeSerifBoldItalic", 
        font_size = 20,
        color     = red,
        label(["FreeSerifBoldItalic font, size 20",1,1]),
        terminal  = png)$
```
- *
*Postscript*:
標準ポストスクリプトフォントは以下の通りです:
`"Times-Roman"`, `"Times-Italic"`, `"Times-Bold"`,
`"Times-BoldItalic"`,
`"Helvetica"`, `"Helvetica-Oblique"`, `"Helvetica-Bold"`,
`"Helvetic-BoldOblique"`, `"Courier"`,
`"Courier-Oblique"`, `"Courier-Bold"`,
`"Courier-BoldOblique"`。
  
例:

```maxima
(%i1) load("draw")$
(%i2) draw2d(
        font      = "Courier-Oblique", 
        font_size = 15,
        label(["Courier-Oblique font, size 15",1,1]),
        terminal = eps)$
```
- *
*pdf*:
*Postscript*と同じフォントを使います。
- *
*pdfcairo*:
*wxt*と同じフォントを使います。
- *
*wxt*:
*pango*ライブラリは
`fontconfig`ユーティリティを介してフォントを見つけます。
- *
*aqua*:
デフォルトは`"Times-Roman"`です。


Gnuplotドキュメンテーションは端末とフォントに関する情報の重要なソースです。

<!-- category: Plotting -->
<!-- keywords: font_size -->
<!-- signatures: font_size -->
### Variable: font_size

デフォルト値: 10


このオプションは、
フォントサイズを端末によって使われるように設定するために使うことができます。
１つの書体とサイズだけがプロットの間中で使うことができます。
オプション`font`が空の文字列に等しくない時だけ、
`font_size`はアクティブです。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


`font`も参照してください。

<!-- category: Plotting -->
<!-- keywords: geomap -->
<!-- signatures: geomap(numlist), geomap(numlist, 3Dprojection) -->
### Function: geomap (numlist)

2Dと3Dに関して地図を描画します。


**2D**


この関数はグローバル変数`boundaries_array`と一緒に機能します。


引数*numlist*は
数や数のリストを含むリストです。
これらすべての数は、
グローバル配列`boundaries_array`の成分を表す
0以上の整数でなければいけません。


Each component of 
`boundaries_array`のそれぞれの成分は
浮動小数点量の配列であり、多角形セグメントやマップ境界の座標です。


`geomap (numlist)`は
引数を平坦化し、`boundaries_array`の中に関連した境界を描画します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`line_width`, `line_type`, `color`.


例:


手で定義された簡単な地図:


```maxima
(%i1) load("draw")$
(%i2) /* Vertices of boundary #0: {(1,1),(2,5),(4,3)} */
   ( bnd0: make_array(flonum,6),
     bnd0[0]:1.0, bnd0[1]:1.0, bnd0[2]:2.0,
     bnd0[3]:5.0, bnd0[4]:4.0, bnd0[5]:3.0 )$
(%i3) /* Vertices of boundary #1: {(4,3),(5,4),(6,4),(5,1)} */
   ( bnd1: make_array(flonum,8),
     bnd1[0]:4.0, bnd1[1]:3.0, bnd1[2]:5.0, bnd1[3]:4.0,
     bnd1[4]:6.0, bnd1[5]:4.0, bnd1[6]:5.0, bnd1[7]:1.0)$
(%i4) /* Vertices of boundary #2: {(5,1), (3,0), (1,1)} */
   ( bnd2: make_array(flonum,6),
     bnd2[0]:5.0, bnd2[1]:1.0, bnd2[2]:3.0,
     bnd2[3]:0.0, bnd2[4]:1.0, bnd2[5]:1.0 )$
(%i5) /* Vertices of boundary #3: {(1,1), (4,3)} */
   ( bnd3: make_array(flonum,4),
     bnd3[0]:1.0, bnd3[1]:1.0, bnd3[2]:4.0, bnd3[3]:3.0)$
(%i6) /* Vertices of boundary #4: {(4,3), (5,1)} */
   ( bnd4: make_array(flonum,4),
     bnd4[0]:4.0, bnd4[1]:3.0, bnd4[2]:5.0, bnd4[3]:1.0)$
(%i7) /* Pack all together in boundaries_array */
   ( boundaries_array: make_array(any,5),
     boundaries_array[0]: bnd0, boundaries_array[1]: bnd1,
     boundaries_array[2]: bnd2, boundaries_array[3]: bnd3,
     boundaries_array[4]: bnd4 )$
(%i8) draw2d(geomap([0,1,2,3,4]))$
```


補助バッケージ `worldmap`は
グローバル変数 `boundaries_array`を
(経度、緯度)座標で
実世界境界に設定します。
これらのデータはパブリックドメインであり、
[http://www-cger.nies.go.jp/­grid-e/­gridtxt/­grid19.html]()
に由来するものです。


パッケージ`worldmap`は、国、大陸、海岸線の境界も
`boundaries_array`の必要な成分を持つリストとして、
定義します。
(更に知るにはファイル`share/draw/worldmap.mac`を参照してください)
パッケージ`draw`は自動的に`worldmap`をロードしません。



```maxima
(%i1) load("worldmap")$
(%i2) c1: gr2d(geomap(Canada,United_States,
                      Mexico,Cuba))$
(%i3) c2: gr2d(geomap(Africa))$
(%i4) c3: gr2d(geomap(Oceania,China,Japan))$
(%i5) c4: gr2d(geomap(France,Portugal,Spain,
                      Morocco,Western_Sahara))$
(%i6) draw(columns  = 2,
           c1,c2,c3,c4)$
```


パッケージ`worldmap`は
国をポリゴンとしてプロットする時にも役に立ちます。
この場合、グラフィックオブジェクト`geomap`は
もはや必要でなく、代わりに`polygon`オブジェクトが使われます。
配列ではなくリストが現在使われているので、
地図レンダリングはより遅いでしょう。
以下のコードを理解するためには、
`make_poly_country`と`make_poly_continent`も
参照してください。


```maxima
(%i1) load("worldmap")$
(%i2) mymap: append(
   [color      = white],  /* borders are white */
   [fill_color = red],             make_poly_country(Bolivia),
   [fill_color = cyan],            make_poly_country(Paraguay),
   [fill_color = green],           make_poly_country(Colombia),
   [fill_color = blue],            make_poly_country(Chile),
   [fill_color = "#23ab0f"],       make_poly_country(Brazil),
   [fill_color = goldenrod],       make_poly_country(Argentina),
   [fill_color = "midnight-blue"], make_poly_country(Uruguay))$
(%i3) apply(draw2d, mymap)$
```



**3D**


`geomap (numlist)`は地図境界を
中心が(0,0,0)で半径1の球上に射影します。
`geomap (numlist,3Dprojection)`を使うことで、
球や射影タイプを変えることが可能です。


利用可能な3D射影:



- *
`[spherical_projection,x,y,z,r]`:
地図境界を
中心(*x*,*y*,*z*)、半径*r*の球上に
射影します。

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap(Australia), /* default projection */
             geomap(Australia,
                    [spherical_projection,2,2,2,3]))$
```
- *
`[cylindrical_projection,x,y,z,r,rc]`:
球地図境界を
中心(*x*,*y*,*z*)の半径*r*の地球の極を通る軸を持ち
半径*rc*の円柱に再射影します。

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap([America_coastlines,Eurasia_coastlines],
                    [cylindrical_projection,2,2,2,3,4]))$
```
- *
`[conic_projection,x,y,z,r,alpha]`:
球地図境界を
中心(*x*,*y*,*z*)の半径*r*の地球の極を通る軸を持ち
角度*alpha*の円錐上に
再射影します。
北円錐と南円錐両方が球に接触します。

```maxima
(%i1) load("worldmap")$
(%i2) draw3d(geomap(World_coastlines,
                    [conic_projection,0,0,0,1,90]))$
```


更に丹念な例を見るには、
[http://www.telefonica.net/web2/biomates/maxima/gpdraw/geomap]()
も参照してください。

<!-- category: Plotting -->
<!-- keywords: get_pixel -->
<!-- signatures: get_pixel(pic, x, y) -->
### Function: get_pixel (pic, x, y)

ピクチャからピクセルを返します。
座標*x*と*y*は
0からそれぞれ`width-1`と`height-1`までの範囲を取ります。

<!-- category: Plotting -->
<!-- keywords: gnuplot_file_name -->
<!-- signatures: gnuplot_file_name -->
### Variable: gnuplot_file_name

デフォルト値: `"maxout.gnuplot"`


これは、
Gnuplotで処理される必要なコマンドを含む
ファイルの名前です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。
関数`draw`の引数としても使うことができます。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
       file_name = "my_file",
       gnuplot_file_name = "my_commands_for_gnuplot",
       data_file_name    = "my_data_for_gnuplot",
       terminal          = png,
       explicit(x^2,x,-1,1)) $
```


`data_file_name`も参照してください。

<!-- category: Plotting -->
<!-- keywords: gr2d -->
<!-- signatures: gr2d(graphic option, ..., graphic object, ...) -->
### Function: gr2d (graphic option, ..., graphic object, ...)

関数`gr2d`は
2Dシーンを記述するオブジェクトを作ります。
引数は*グラフィックオプション*、*グラフィックオブジェクト*、または、
グラフィックオプションとオブジェクト両方を含むリストです。
このシーンは順に解釈されます:
*グラフィックオプション*はその右に置かれたそれらの*グラフィックオブジェクト*に影響します。
いくつかの*グラフィックオプション*はシーンのグローバルな外観に影響します。


以下は2次元のシーンで利用可能な*グラフィックオブジェクト*のリストです:
`bars`, `ellipse`, `explicit`, `image`, `implicit`, `label`,
`parametric`, `points`, `polar`, `polygon`, `quadrilateral`,
`rectangle`, `triangle`, `vector`, `geomap`
(パッケージ`worldmap`で定義されるもの)。


`draw`と`draw2d`も参照してください。


このオブジェクトを利用するには、最初に`load("draw")`を書いてください。

<!-- category: Plotting -->
<!-- keywords: gr3d -->
<!-- signatures: gr3d(graphic option, ..., graphic object, ...) -->
### Function: gr3d (graphic option, ..., graphic object, ...)

関数`gr3d`は3dシーンを記述するオブジェクトを作ります。
引数は*グラフィックオプション*、*グラフィックオブジェクト*、または
グラフィックオプションとオブジェクト両方を含むリストです。
このシーンは順に解釈されます:
*グラフィックオプション*はその右に置かれたそれらの*グラフィックオブジェクト*に影響します。
いくつかの*グラフィックオプション*はシーンのグローバルな外観に影響します。


以下は3次元のシーンで利用可能な*グラフィックオブジェクト*のリストです:
`cylindrical`, `elevation_grid`, `explicit`, `implicit`,
`label`, `mesh`, `parametric`,

`parametric_surface`,
`points`, `quadrilateral`, `spherical`, `triangle`,
`tube`,

`vector`, `geomap`
(パッケージ`worldmap`で定義されるもの)。


`draw`と`draw3d`も参照してください。


このオブジェクトを利用するには、最初に`load("draw")`を書いてください。

<!-- category: Plotting -->
<!-- keywords: head_angle -->
<!-- signatures: head_angle -->
### Variable: head_angle

デフォルト値: 45


`head_angle`は矢印の頭と線分の間の角度を度の単位で示します。


このオプションは`vector`オブジェクトに対してだけ有効です。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,10],
             yrange      = [0,9],
             head_length = 0.7,
             head_angle  = 10,
             vector([1,1],[0,6]),
             head_angle  = 20,
             vector([2,1],[0,6]),
             head_angle  = 30,
             vector([3,1],[0,6]),
             head_angle  = 40,
             vector([4,1],[0,6]),
             head_angle  = 60,
             vector([5,1],[0,6]),
             head_angle  = 90,
             vector([6,1],[0,6]),
             head_angle  = 120,
             vector([7,1],[0,6]),
             head_angle  = 160,
             vector([8,1],[0,6]),
             head_angle  = 180,
             vector([9,1],[0,6]) )$
```


`head_both`, `head_length`, `head_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: head_both -->
<!-- signatures: head_both -->
### Variable: head_both

デフォルト値: `false`


もし`head_both`が`true`なら、
ベクトルは2つの矢先と共に描画されます。
もし`false`なら１つの矢だけが描かれます。


このオプションは`vector`オブジェクトに対してだけ有効です。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,8],
             yrange      = [0,8],
             head_length = 0.7,
             vector([1,1],[6,0]),
             head_both   = true,
             vector([1,7],[6,0]) )$
```


See also `head_length`, `head_angle`, and `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_length -->
<!-- signatures: head_length -->
### Variable: head_length

デフォルト値: 2


`head_length`は矢印の頭の長さを*x*-軸の単位で示します。


このオプションは`vector`オブジェクトに対してだけ有効です。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,12],
             yrange      = [0,8],
             vector([0,1],[5,5]),
             head_length = 1,
             vector([2,1],[5,5]),
             head_length = 0.5,
             vector([4,1],[5,5]),
             head_length = 0.25,
             vector([6,1],[5,5]))$
```


`head_both`, `head_angle`, `head_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: head_type -->
<!-- signatures: head_type -->
### Variable: head_type

デフォルト値: `filled`


`head_type`は矢印の頭を如何にプロットするかを指定するのに使われます。
可能な値は以下の通りです: `filled` (閉じていて塗りつぶされた矢印の頭), `empty`
(閉じているが塗りつぶされていない矢印の頭), `nofilled` (開いた矢印の頭).


このオプションは`vector`オブジェクトにだけ有効です。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,12],
             yrange      = [0,10],
             head_length = 1,
             vector([0,1],[5,5]), /* default type */
             head_type = 'empty,
             vector([3,1],[5,5]),
             head_type = 'nofilled,
             vector([6,1],[5,5]))$
```


`head_both`, `head_angle`, `head_length`も参照してください。

<!-- category: Plotting -->
<!-- keywords: image -->
<!-- signatures: image(im, x0, y0, width, height) -->
### Function: image (im, x0, y0, width, height)

2Dにてイメージを描写します。


**2D**


`image (im,x0,y0,width,height)`は
実平面上の
頂点`(x0,y0)`から`(x0+width,y0+height)`までの長方形領域に
イメージ*im*をプロットします。
引数*im*は実数の行列、長さ3のベクトルの行列もしくは*picture*オブジェクトでなければいけません。


もし*im*が実数の行列か*levels picture*オブジェクトなら、
ピクセル値は
-36から+36に広がる成分を持つ長さ3のベクトルである
グラフィックオプション`palette`に従って解釈されます;
それぞれの値はレベルをそれぞれ赤、緑、青色にマップする公式のインデックスです。


```maxima
0: 0               1: 0.5           2: 1
 3: x               4: x^2           5: x^3
 6: x^4             7: sqrt(x)       8: sqrt(sqrt(x))
 9: sin(90x)       10: cos(90x)     11: |x-0.5|
12: (2x-1)^2       13: sin(180x)    14: |cos(180x)|
15: sin(360x)      16: cos(360x)    17: |sin(360x)|
18: |cos(360x)|    19: |sin(720x)|  20: |cos(720x)|
21: 3x             22: 3x-1         23: 3x-2
24: |3x-1|         25: |3x-2|       26: (3x-1)/2
27: (3x-2)/2       28: |(3x-1)/2|   29: |(3x-2)/2|
30: x/0.32-0.78125                  31: 2*x-0.84
32: 4x;1;-2x+1.84;x/0.08-11.5
33: |2*x - 0.5|    34: 2*x          35: 2*x - 0.5
36: 2*x - 1
```

負の数は負の色成分を意味します。


`palette = gray`と`palette = color`は
それぞれ、
`palette = [3,3,3]`と`palette = [7,5,15]`へのショートカットです。


もし*im*が長さ3のベクトルの行列か*rgb picture*オブジェクトなら、
それらは赤、緑、青の色成分として解釈されます。


例:


もし*im*が実数の行列なら、ピクセル値は
グラフィックオプション`palette`に従って解釈されます。


```maxima
(%i1) load("draw")$
(%i2) im: apply(
           'matrix,
            makelist(makelist(random(200),i,1,30),i,1,30))$
(%i3) /* palette = color, default */
      draw2d(image(im,0,0,30,30))$
(%i4) draw2d(palette = gray, image(im,0,0,30,30))$
(%i5) draw2d(palette = [15,20,-4],
             colorbox=false,
             image(im,0,0,30,30))$
```


`colorbox`も参照してください。


もし*im*が長さ3のベクトルの行列なら、
それらは赤、緑、青の色成分として解釈されます。


```maxima
(%i1) load("draw")$
(%i2) im: apply(
            'matrix,
             makelist(
               makelist([random(300),
                         random(300),
                         random(300)],i,1,30),i,1,30))$
(%i3) draw2d(image(im,0,0,30,30))$
```


パッケージ`draw`は自動的にパッケージ`picture`をロードします。
この例では、レベルピクチャオブジェクトは手動で組み立てられ、描画されます。


```maxima
(%i1) load("draw")$
(%i2) im: make_level_picture([45,87,2,134,204,16],3,2);
(%o2)       picture(level, 3, 2, {Array:  #(45 87 2 134 204 16)})
(%i3) /* default color palette */
      draw2d(image(im,0,0,30,30))$
(%i4) /* gray palette */
      draw2d(palette = gray,
             image(im,0,0,30,30))$
```


xpmファイルが読み込まれ、描写されます。


```maxima
(%i1) load("draw")$
(%i2) im: read_xpm("myfile.xpm")$
(%i3) draw2d(image(im,0,0,10,7))$
```


`make_level_picture`, `make_rgb_picture`, `read_xpm`も参照してください。


[http://www.telefonica.net/web2/biomates/maxima/gpdraw/image]()

には更に丹念な例があります。

<!-- category: Plotting -->
<!-- keywords: implicit -->
<!-- signatures: implicit(fcn, x, xmin, xmax, y, ymin, ymax), implicit(fcn, x, xmin, xmax, y, ymin, ymax, z, zmin, zmax) -->
### Function: implicit (fcn, x, xmin, xmax, y, ymin, ymax)

2Dおよび3Dにて陰関数を描画します。


**2D**


`implicit(fcn,x,xmin,xmax,y,ymin,ymax)`は
*xmin*から*xmax*までの値を取る変数*x*と
*ymin*から*ymax*までの値を取る変数*y*を伴う
*fcn*で定義された陰関数をプロットします。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`ip_grid`, 
`ip_grid_in`, `line_width`, `line_type`, `key`,
 `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal  = eps,
             grid      = true,
             line_type = solid,
             key       = "y^2=x^3-2*x+1",
             implicit(y^2=x^3-2*x+1, x, -4,4, y, -4,4),
             line_type = dots,
             key       = "x^3+y^3 = 3*x*y^2-x-1",
             implicit(x^3+y^3 = 3*x*y^2-x-1, x,-4,4, y,-4,4),
             title     = "Two implicit functions" )$
```


**3D**


`implicit (fcn,x,xmin,xmax, y,ymin,ymax, z,zmin,zmax)`は
*xmin*から*xmax*までの値を取る変数*x*と
*ymin*から*ymax*までの値を取る変数*y*と
*zmin*から*zmax*までの値を取る変数*z*を伴う
*fcn*で定義された陰表面をプロットします。
このオブジェクトは*マーチングキューブアルゴリズム*を実装します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`x_voxel`, 
`y_voxel`, `z_voxel`, `line_width`, `line_type`, `key` , `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        color=blue,
        implicit((x^2+y^2+z^2-1)*(x^2+(y-1.5)^2+z^2-0.5)=0.015,
                 x,-1,1,y,-1.2,2.3,z,-1,1),
        surface_hide=true);
```

<!-- category: Plotting -->
<!-- keywords: ip_grid -->
<!-- signatures: ip_grid -->
### Variable: ip_grid

デフォルト値: `[50, 50]`


`ip_grid`はインプリシットなプロットでの最初のサンプリングのためにグリッドを設定します。


このオプションは`implicit`オブジェクトに対してだけ関係があります。

<!-- category: Plotting -->
<!-- keywords: ip_grid_in -->
<!-- signatures: ip_grid_in -->
### Variable: ip_grid_in

デフォルト値: `[5, 5]`


`ip_gridi_in`はインプリシットなプロットでの二番目のサンプリングのためにグリッドを設定します。


このオプションは`implicit`オブジェクトに対してだけ関係があります。

<!-- category: Plotting -->
<!-- keywords: key -->
<!-- signatures: key -->
### Variable: key

デフォルト値: `""` (empty string)


`key`は凡例の中の関数名です。
もし`key`が空の文字列なら、
関数にキーは割り当てられません。


このオプションは以下のグラフィックオブジェクトに影響します:


- *
`gr2d`: `points`, `polygon`, `rectangle`,
`ellipse`, `vector`, `explicit`, `implicit`,
`parametric`, と`polar`。
- *
`gr3d`: `points`, `explicit`, `parametric`,
と`parametric_surface`


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(key   = "Sinus",
             explicit(sin(x),x,0,10),
             key   = "Cosinus",
             color = red,
             explicit(cos(x),x,0,10) )$
```

<!-- category: Plotting -->
<!-- keywords: label -->
<!-- signatures: label([string, x, y], ...), label([string, x, y, z], ...) -->
### Function: label ([string, x, y], ...)

2Dと3D内でラベルを書きます。


色付けられたラベルはGnuplot 4.3でだけ機能します。
これはパッケージ`draw`に関して既知のバグです。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`label_alignment`, 
`label_orientation`, `color`.


**2D**


`label([string,x,y])`は
点`[x,y]`に*string*を書きます。



例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(yrange = [0.1,1.4],
             color = "red",
             label(["Label in red",0,0.3]),
             color = "#0000ff",
             label(["Label in blue",0,0.6]),
             color = "light-blue",
             label(["Label in light-blue",0,0.9],
                   ["Another light-blue",0,1.2])  )$
```


**3D**


`label([string,x,y,z])`は、
点`[x,y,z]`に*string*を書きます。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3),
             color = red,
             label(["UP 1",-2,0,3], ["UP 2",1.5,0,4]),
             color = blue,
             label(["DOWN 1",2,0,-3]) )$
```

<!-- category: Plotting -->
<!-- keywords: label_alignment -->
<!-- signatures: label_alignment -->
### Variable: label_alignment

デフォルト値: `center`


`label_alignment`は
与えられた座標に関するラベルを書く場所を指定するのに使われます。
可能な値は以下のものです: `center`, `left`, `right`.


このオプションは`label`オブジェクトに対してだけ有効です。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange          = [0,10],
             yrange          = [0,10],
             points_joined   = true,
             points([[5,0],[5,10]]),
             color           = blue,
             label(["Centered alignment (default)",5,2]),
             label_alignment = 'left,
             label(["Left alignment",5,5]),
             label_alignment = 'right,
             label(["Right alignment",5,8]))$
```


`label_orientation`, `color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: label_orientation -->
<!-- signatures: label_orientation -->
### Variable: label_orientation

デフォルト値: `horizontal`


`label_orientation`はラベルの向きを指定するのに使われます。
可能な値は以下のものです: `horizontal`, `vertical`.


このオプションは`label`オブジェクトに対してだけ有効です。


例:


この例では、ダミーの点がイメージを得るために加えられます。
パッケージ`draw`はいつもシーンを描くのにデータを必要とします。


```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange     = [0,10],
             yrange     = [0,10],
             point_size = 0,
             points([[5,5]]),
             color      = navy,
             label(["Horizontal orientation (default)",5,2]),
             label_orientation = 'vertical,
             color             = "#654321",
             label(["Vertical orientation",1,5]))$
```


`label_alignment`と`color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: line_type -->
<!-- signatures: line_type -->
### Variable: line_type

デフォルト値: `solid`


`line_type`は線が如何に表示されるかを示します;
可能な値は`solid`と`dots`です。


このオプションは以下のグラフィックオブジェクトに鋭意供します:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric`と`polar`。
- *
`gr3d`: `points`, `explicit`, `parametric`と`parametric_surface`。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(line_type = dots,
             explicit(1 + x^2,x,-1,1),
             line_type = solid, /* default */
             explicit(2 + x^2,x,-1,1))$
```


See also `line_width`.

<!-- category: Plotting -->
<!-- keywords: line_width -->
<!-- signatures: line_width -->
### Variable: line_width

デフォルト値: 1


`line_width`はプロットされる線の幅です。
その値は正の数でなければいけません。


このオプションは以下のグラフィックオブジェクトに影響します:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` と`polar`.
- *
`gr3d`: `points`と`parametric`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^2,x,-1,1), /* default width */
             line_width = 5.5,
             explicit(1 + x^2,x,-1,1),
             line_width = 10,
             explicit(2 + x^2,x,-1,1))$
```


`line_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: logcb -->
<!-- signatures: logcb -->
### Variable: logcb

デフォルト値: `false`


もし`logcb`が`true`なら、
カラーボックスのチックは対数スケールで描かれます。


`enhanced3d`か`colorbox`が`false`の時、
オプション`logcb`は効果を持ちません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d (
        enhanced3d = true,
        color      = green,
        logcb = true,
        logz  = true,
        palette = [-15,24,-9],
        explicit(exp(x^2-y^2), x,-2,2,y,-2,2)) $
```


`enhanced3d`, `colorbox`, `cbrange`も参照してください。

<!-- category: Plotting -->
<!-- keywords: logz -->
<!-- signatures: logz -->
### Variable: logz

デフォルト値: `false`


もし`logz`が`true`なら、
*z*軸は対数スケールで描かれます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(logz = true,
             explicit(exp(u^2+v^2),u,-2,2,v,-2,2))$
```


`logx`, `logy`も参照してください。

<!-- category: Plotting -->
<!-- keywords: make_level_picture -->
<!-- signatures: make_level_picture(data), make_level_picture(data, width, height) -->
### Function: make_level_picture (data)

レベル*picture*オブジェクトを返します。
`make_level_picture (data)`は
行列*data*から
*picture*オブジェクトを作ります。
`make_level_picture (data,width,height)`は
数のリストからオブジェクトを作ります;
この場合、*width*と*height*両方を与えなければいけません。


返された*picture*オブジェクトは以下の4つの部分を含みます:



1. シンボル `level`
2. イメージの幅
3. イメージの高さ
4. 0から255までの範囲のピクセルデータを持つ整数配列
引数*data*は0から255までの数のみを含まなければいけません;
負の数は0に置き換えられ、255よりも大きな数は255に設定されます。


例:


行列からのレベルピクチャ。


```maxima
(%i1) load("draw")$
(%i2) make_level_picture(matrix([3,2,5],[7,-9,3000]));
(%o2)         picture(level, 3, 2, {Array:  #(3 2 5 7 0 255)})
```


数値リストからのレベルピクチャ


```maxima
(%i1) load("draw")$
(%i2) make_level_picture([-2,0,54,%pi],2,2);
(%o2)            picture(level, 2, 2, {Array:  #(0 0 54 3)})
```

<!-- category: Plotting -->
<!-- keywords: make_poly_continent -->
<!-- signatures: make_poly_continent(continent_name), make_poly_continent(country_list) -->
### Function: make_poly_continent (continent_name)

色付けられた大陸や国のリストを描画するのに必要なポリゴンを作ります。


例:



```maxima
(%i1) load("worldmap")$
(%i2) /* A continent */
      make_poly_continent(Africa)$
(%i3) apply(draw2d, %)$
(%i4) /* A list of countries */
      make_poly_continent([Germany,Denmark,Poland])$
(%i5) apply(draw2d, %)$
```

<!-- category: Plotting -->
<!-- keywords: make_poly_country -->
<!-- signatures: make_poly_country(country_name) -->
### Function: make_poly_country (country_name)

色付けられた国を描画するのに必要なポリゴンを作ります。
もし島が存在するなら、1つの国はただ1つ以上のポリゴンで定義され得ます。


例:



```maxima
(%i1) load("worldmap")$
(%i2) make_poly_country(India)$
(%i3) apply(draw2d, %)$
```

<!-- category: Plotting -->
<!-- keywords: make_polygon -->
<!-- signatures: make_polygon(nlist) -->
### Function: make_polygon (nlist)

境界添字から`polygon`オブジェクトを返します。
引数*nlist*は`boundaries_array`の成分のリストです。


例:


ブータンは境界番号171, 173, 1143で定義されます。
だから、`make_polygon([171,173,1143])`は
appends arrays of coordinates 
座標`boundaries_array[171]`, `boundaries_array[173]`,
 `boundaries_array[1143]`の配列を付加し、
`draw`でプロットされるのに適した`polygon`オブジェクトを返します．
エラーメッセージを避けるには、
任意の連続する配列が端で共通の2つの座標を持つという意味で配列は互換性がなければいけません。
この例では、
`boundaries_array[171]`の最初の2つの成分は
`boundaries_array[173]`の最後の2つの座標と等しく、
`boundaries_array[173]`の最初の2つは
`boundaries_array[1143]`の最初の2つに等しいです;
結論として、境界番号171, 173, 1143は (この順で)互換性があり、色付けられたポリゴンは描画できます。


```maxima
(%i1) load("worldmap")$
(%i2) Bhutan;
(%o2)                        [[171, 173, 1143]]
(%i3) boundaries_array[171];
(%o3) {Array:  
       #(88.750549 27.14727 88.806351 27.25305 88.901367 27.282221
         88.917877 27.321039)}
(%i4) boundaries_array[173];
(%o4) {Array:
       #(91.659554 27.76511 91.6008 27.66666 91.598022 27.62499
         91.631348 27.536381 91.765533 27.45694 91.775253 27.4161 
         92.007751 27.471939 92.11441 27.28583 92.015259 27.168051
         92.015533 27.08083 92.083313 27.02277 92.112183 26.920271
         92.069977 26.86194 91.997192 26.85194 91.915253 26.893881
         91.916924 26.85416 91.8358 26.863331 91.712479 26.799999 
         91.542191 26.80444 91.492188 26.87472 91.418854 26.873329
         91.371353 26.800831 91.307457 26.778049 90.682457 26.77417
         90.392197 26.903601 90.344131 26.894159 90.143044 26.75333
         89.98996 26.73583 89.841919 26.70138 89.618301 26.72694 
         89.636093 26.771111 89.360786 26.859989 89.22081 26.81472
         89.110237 26.829161 88.921631 26.98777 88.873016 26.95499
         88.867737 27.080549 88.843307 27.108601 88.750549 
         27.14727)}
(%i5) boundaries_array[1143];
(%o5) {Array:  
       #(91.659554 27.76511 91.666924 27.88888 91.65831 27.94805 
         91.338028 28.05249 91.314972 28.096661 91.108856 27.971109
         91.015808 27.97777 90.896927 28.05055 90.382462 28.07972
         90.396088 28.23555 90.366074 28.257771 89.996353 28.32333
         89.83165 28.24888 89.58609 28.139999 89.35997 27.87166 
         89.225517 27.795 89.125793 27.56749 88.971077 27.47361
         88.917877 27.321039)}
(%i6) Bhutan_polygon: make_polygon([171,173,1143])$
(%i7) draw2d(Bhutan_polygon)$
```

<!-- category: Plotting -->
<!-- keywords: make_rgb_picture -->
<!-- signatures: make_rgb_picture(redlevel, greenlevel, bluelevel) -->
### Function: make_rgb_picture (redlevel, greenlevel, bluelevel)

rgb色付けされた*picture*オブジェクトを返します。
3つ引数すべては赤、緑、青のレベルを持つレベルピクチャでなければいけません;


返された*picture*オブジェクトは以下の4つの部分を含みます:



1. シンボル `rgb`
2. イメージの幅
3. イメージの高さ
4. 0から255までの範囲のピクセルデータを持つ長さ*3*width*height*の整数配列。
それぞれのピクセルは。3つの連続する数 (赤、緑、青)で表現されます。


例:



```maxima
(%i1) load("draw")$
(%i2) red: make_level_picture(matrix([3,2],[7,260]));
(%o2)           picture(level, 2, 2, {Array:  #(3 2 7 255)})
(%i3) green: make_level_picture(matrix([54,23],[73,-9]));
(%o3)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
(%i4) blue: make_level_picture(matrix([123,82],[45,32.5698]));
(%o4)          picture(level, 2, 2, {Array:  #(123 82 45 33)})
(%i5) make_rgb_picture(red,green,blue);
(%o5) picture(rgb, 2, 2, 
              {Array:  #(3 54 123 2 23 82 7 73 45 255 0 33)})
```

<!-- category: Plotting -->
<!-- keywords: mesh -->
<!-- signatures: mesh(mat, x0, y0, width, height) -->
### Function: mesh (mat, x0, y0, width, height)

3D空間内に行列*mat*を描画します。
*z*値は*mat*から取られます。
横座標範囲は*x0*から$x0 + width$までを取り、
座標は*y0*から$y0 + height$までを取ります。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`line_type`,
`line_width`, `key`, `enhanced3d`, `color`.


このグラフィックオブジェクトは
`true`と`false`以外の値の`enhanced3d`値を無視します。


例:



```maxima
(%i1) load("draw")$
(%i2) m: apply(
            matrix,
            makelist(makelist(random(10.0),k,1,30),i,1,20)) $
(%i3) draw3d(
         color = blue,
         mesh(m,0,0,3,2),
         xlabel = "x",
         ylabel = "y",
         surface_hide = true);
```

<!-- category: Plotting -->
<!-- keywords: multiplot_mode -->
<!-- signatures: multiplot_mode(term) -->
### Function: multiplot_mode (term)

この関数を使って、Maximaは
端末*term*で1ウィンドウマルチプロットモードで機能することができます;
この関数が受け入れる引数は、`screen`, 
`wxt`, `aquaterm`, `none`です。


マルチプロットモードがイネーブルの時、
`draw`へのそれぞれのコールは、
同じウィンドウに以前のものを消すことなく新しいプロットを送ります。
マルチモードをディセーブルにするには、
`multiplot_mode(none)`を書いてください。


マルチプロットモードがイネーブルの時、
グローバルオプション`terminal`はブロックされます。
別の端末に変更する前に、この機能中のモードをディセーブルしなければいけません。


この特長はWindowsプラットフォームでは機能しません。


例:



```maxima
(%i1) load("draw")$
(%i2) set_draw_defaults(
         xrange = [-1,1],
         yrange = [-1,1],
         grid   = true,
         title  = "Step by step plot" )$
(%i3) multiplot_mode(screen)$
(%i4) draw2d(color=blue,  explicit(x^2,x,-1,1))$
(%i5) draw2d(color=red,   explicit(x^3,x,-1,1))$
(%i6) draw2d(color=brown, explicit(x^4,x,-1,1))$
(%i7) multiplot_mode(none)$
```

<!-- category: Plotting -->
<!-- keywords: negative_picture -->
<!-- signatures: negative_picture(pic) -->
### Function: negative_picture (pic)

(*level*または*rgb*)ピクチャの反転を返します。

<!-- category: Plotting -->
<!-- keywords: numbered_boundaries -->
<!-- signatures: numbered_boundaries(nlist) -->
### Function: numbered_boundaries (nlist)

その数(`boundaries_array`座標)でラベルされた
多角形セグメント(境界)のリストを描画します。
これは新しい地理的なものを作る時に非常に役立ちます。


例:


`boundaries_array`内の成分数で境界をラベルされたヨーロッパの地図


```maxima
(%i1) load("worldmap")$
(%i2) european_borders: 
           region_boundaries(-31.81,74.92,49.84,32.06)$
(%i3) numbered_boundaries(european_borders)$
```

<!-- category: Plotting -->
<!-- keywords: parametric -->
<!-- signatures: parametric(xfun, yfun, par, parmin, parmax), parametric(xfun, yfun, zfun, par, parmin, parmax) -->
### Function: parametric (xfun, yfun, par, parmin, parmax)

2Dおよび3Dにてパラメトリック関数を描画します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`nticks`, 
`line_width`, `line_type`, `key`, `color` and `enhanced3d`.


**2D**


コマンド `parametric(xfun, yfun, par, parmin, parmax)`は
*parmin*から*parmax*まで値を取るパラメータ*par*を伴う
パラメトリック関数`[xfun, yfun]`をプロットします。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(x),x,-1,3),
             color = red,
             key   = "This is the parametric one!!",
             parametric(2*cos(rrr),rrr^2,rrr,0,2*%pi))$
```


**3D**


`parametric (xfun, yfun, zfun, par, parmin, parmax)`は
*parmin*から*parmax*まで値を取るパラメータ*par*を伴う
パラメトリック曲線
`[xfun, yfun, zfun]`をプロットします。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3),
             color = royalblue,
             parametric(cos(5*u)^2,sin(7*u),u-2,u,0,2),
             color      = turquoise,
             line_width = 2,
             parametric(t^2,sin(t),2+t,t,0,2),
             surface_hide = true,
             title = "Surface & curves" )$
```

<!-- category: Plotting -->
<!-- keywords: parametric_surface -->
<!-- signatures: parametric_surface(xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max) -->
### Function: parametric_surface (xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max)

3Dにおいてパラメトリックな表面を描画します。


**3D**


コマンド `parametric_surface (xfun, yfun, zfun, par1, par1min, par1max, par2, par2min, par2max)`は
*par1min*から *par1max*までを値として取るパラメータ *par1*と
*par2min*から *par2max*までを値として取るパラメータ *par2*を伴う
パラメトリックな表面 `[xfun, yfun, zfun]`を
プロットします。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `enhanced3d`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(title          = "Sea shell",
             xu_grid        = 100,
             yv_grid        = 25,
             view           = [100,20],
             surface_hide   = true,
             parametric_surface(0.5*u*cos(u)*(cos(v)+1),
                           0.5*u*sin(u)*(cos(v)+1),
                           u*sin(v) - ((u+3)/8*%pi)^2 - 20,
                           u, 0, 13*%pi, v, -%pi, %pi) )$
```

<!-- category: Plotting -->
<!-- keywords: picture_equalp -->
<!-- signatures: picture_equalp(x, y) -->
### Function: picture_equalp (x, y)

等しいピクチャの場合`true`を、そうでなければ`false`
を返します。

<!-- category: Plotting -->
<!-- keywords: picturep -->
<!-- signatures: picturep(x) -->
### Function: picturep (x)

もし引数が適正なイメージなら
`true`を、そうでなければ`false`を返します。

<!-- category: Plotting -->
<!-- keywords: point_size -->
<!-- signatures: point_size -->
### Variable: point_size

デフォルト値: 1


`point_size`はプロットされる点のサイズを設定します。
非負数でなければいけません。


グラフィックオプション`point_type`が`dot`に設定される時
このオプションは効果を持ちません。


このオプションは以下のグラフィックオブジェクトに影響します:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(points(makelist([random(20),random(50)],k,1,10)),
        point_size = 5,
        points(makelist(k,k,1,20),makelist(random(30),k,1,20)))$
```

<!-- category: Plotting -->
<!-- keywords: points -->
<!-- signatures: points([[x1, y1], [x2, y2], ...]), points([x1, x2, ...], [y1, y2, ...]), points([y1, y2, ...]), points([[x1, y1, z1], [x2, y2, z2], ...]), points([x1, x2, ...], [y1, y2, ...], [z1, z2, ...]), points(matrix), points(1d_y_array), points(1d_x_array, 1d_y_array), points(1d_x_array, 1d_y_array, 1d_z_array), points(2d_xy_array), points(2d_xyz_array) -->
### Function: points ([[x1, y1], [x2, y2], ...])

2Dや3Dの中で点を描画します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`point_size`, 
`point_type`, `points_joined`, `line_width`, `key`,
`line_type`, `color`.
3Dモードでは、`enhanced3d`の影響も受けます。


**2D**


`points ([[x1,y1], [x2,y2],...])`や
`points ([x1,x2,...], [y1,y2,...])`は
点`[x1,y1]`, `[x2,y2]`,などをプロットします。
もし横座標が与えられないなら、
それらは連続する正の整数に設定されます。
だから、
`points ([y1,y2,...])`は、点`[1,y1]`, `[2,y2]`などを描画します。
もし*matrix*が2列または2行行列なら、
`points (matrix)`は関連した点を描画します。
もし*matrix*が1列または1行行列なら、
横座標が自動的に割り当てられます。


もし*1d_y_array*が数の1Dのlisp配列なら、
`points (1d_y_array)`は
横座標を連続する正の整数に設定してそれらをプロットします。
`points (1d_x_array, 1d_y_array)`は
引数として渡された2つの配列から取られた座標を持つ点をプロットします。
もし*2d_xy_array*が2列の2D配列なら、
`points (2d_xy_array)`は平面上に対応する点をプロットします。


例:


`points`への2種類の引数、ペアのリストと分離した座標の2つのリスト。


```maxima
(%i1) load("draw")$
(%i2) draw2d(
        key = "Small points",
        points(makelist([random(20),random(50)],k,1,10)),
        point_type    = circle,
        point_size    = 3,
        points_joined = true,
        key           = "Great points",
        points(makelist(k,k,1,20),makelist(random(30),k,1,20)),
        point_type    = filled_down_triangle,
        key           = "Automatic abscissas",
        color         = red,
        points([2,12,8]))$
```


衝撃を描画。


```maxima
(%i1) load("draw")$
(%i2) draw2d(
        points_joined = impulses,
        line_width    = 2,
        color         = red,
        points(makelist([random(20),random(50)],k,1,10)))$
```


座標の配列。


```maxima
(%i1) load("draw")$
(%i2) a: make_array (flonum, 100) $
(%i3) for i:0 thru 99 do a[i]: random(1.0) $
(%i4) draw2d(points(a)) $
```


分離した座標の2つの配列。


```maxima
(%i1) load("draw")$
(%i2) x: make_array (flonum, 100) $
(%i3) y: make_array (fixnum, 100) $
(%i4) for i:0 thru 99 do (
        x[i]: float(i/100),
        y[i]: random(10) ) $
(%i5) draw2d(points(x, y)) $
```


2列2D配列。


```maxima
(%i1) load("draw")$
(%i2) xy: make_array(flonum, 100, 2) $
(%i3) for i:0 thru 99 do (
        xy[i, 0]: float(i/100),
        xy[i, 1]: random(10) ) $
(%i4) draw2d(points(xy)) $
```


関数`read_array`で埋められた配列の描画。


```maxima
(%i1) load("draw")$
(%i2) a: make_array(flonum,100) $
(%i3) read_array (file_search ("pidigits.data"), a) $
(%i4) draw2d(points(a)) $
```


**3D**


`points([[x1, y1, z1], [x2, y2, z2], ...])` や
`points([x1, x2, ...], [y1, y2, ...], [z1, z2, ...])`は
点`[x1, y1, z1]`, `[x2, y2, z2]`などをプロットします。
もし *matrix*が3列または3行行列なら、
`points (matrix)`は関連した点を描画します。


引数がlisp配列の時、
`points (1d_x_array, 1d_y_array, 1d_z_array)`は
3つの1D配列から座標を取ります。
もし*2d_xyz_array*が3列または3行を持つ2D配列なら、
`points (2d_xyz_array)`は対応する点をプロットします。


例:


3次元のサンプル１つ、


```maxima
(%i1) load("draw")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) draw3d(title = "Daily average wind speeds",
             point_size = 2,
             points(args(submatrix (s2, 4, 5))) )$
```


3次元のサンプル２つ、


```maxima
(%i1) load("draw")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) draw3d(
         title = "Daily average wind speeds. Two data sets",
         point_size = 2,
         key        = "Sample from stations 1, 2 and 3",
         points(args(submatrix (s2, 4, 5))),
         point_type = 4,
         key        = "Sample from stations 1, 4 and 5",
         points(args(submatrix (s2, 2, 3))) )$
```


1次元配列、


```maxima
(%i1) load("draw")$
(%i2) x: make_array (fixnum, 10) $
(%i3) y: make_array (fixnum, 10) $
(%i4) z: make_array (fixnum, 10) $
(%i5) for i:0 thru 9 do (
        x[i]: random(10),
        y[i]: random(10),
        z[i]: random(10) ) $
(%i6) draw3d(points(x,y,z)) $
```


2次元色付け配列、


```maxima
(%i1) load("draw")$
(%i2) xyz: make_array(fixnum, 10, 3) $
(%i3) for i:0 thru 9 do (
        xyz[i, 0]: random(10),
        xyz[i, 1]: random(10),
        xyz[i, 2]: random(10) ) $
(%i4) draw3d(
         enhanced3d = true,
         points_joined = true,
         points(xyz)) $
```


ユーザーが陽に指定した色数。


```maxima
(%i1) load("draw")$
(%i2) pts: makelist([t,t^2,cos(t)], t, 0, 15)$
(%i3) col_num: makelist(k, k, 1, length(pts))$
(%i4) draw3d(
        enhanced3d = ['part(col_num,k),k],
        point_size = 3,
        point_type = filled_circle,
        points(pts))$
```

<!-- category: Plotting -->
<!-- keywords: points_joined -->
<!-- signatures: points_joined -->
### Variable: points_joined

デフォルト値: `false`


`points_joined`が`true`の時、
点は線で結ばれます;
`false`の時、孤立した点が描かれます。
このグラフィックオプションの三番目の可能な値は`impulses`です;
この場合、点からx軸(2D)もしくはxy平面(3D)へ垂直の線分が描かれます。


このオプションは以下のグラフィックオブジェクトに影響します:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange        = [0,10],
             yrange        = [0,4],
             point_size    = 3,
             point_type    = up_triangle,
             color         = blue,
             points([[1,1],[5,1],[9,1]]),
             points_joined = true,
             point_type    = square,
             line_type     = dots,
             points([[1,2],[5,2],[9,2]]),
             point_type    = circle,
             color         = red,
             line_width    = 7,
             points([[1,3],[5,3],[9,3]]) )$
```

<!-- category: Plotting -->
<!-- keywords: polar -->
<!-- signatures: polar(radius, ang, minang, maxang) -->
### Function: polar (radius, ang, minang, maxang)

極座標で定義された2D関数を描画します。


**2D**


`polar (radius,ang,minang,maxang)`は
*minang*から*maxang*まで値を取る変数*ang*を伴う
極座標で定義された関数
`radius(ang)`
をプロットします。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`nticks`, 
`line_width`, `line_type`, `key`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(user_preamble = "set grid polar",
             nticks        = 200,
             xrange        = [-5,5],
             yrange        = [-5,5],
             color         = blue,
             line_width    = 3,
             title         = "Hyperbolic Spiral",
             polar(10/theta,theta,1,10*%pi) )$
```

<!-- category: Plotting -->
<!-- keywords: polygon -->
<!-- signatures: polygon([[x1, y1], [x2, y2], ...]), polygon([x1, x2, ...], [y1, y2, ...]) -->
### Function: polygon ([[x1, y1], [x2, y2], ...])

2D内でポリゴンを描画します。


**2D**


コマンド `polygon ([[x1, y1], [x2, y2],...])`や
`polygon ([x1, x2,...], [y1, y2,...])`は
頂点`[x1, y1]`, `[x2, y2]`などを持つポリゴンを
平面上にプロットします。


このオブジェクトは以下の
*グラフィックオプション*の影響を受けます:
`transparent`, 
`fill_color`, `border`, `line_width`, `key`,
 `line_type`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(color      = "#e245f0",
             line_width = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = yellow,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: proportional_axes -->
<!-- signatures: proportional_axes -->
### Variable: proportional_axes

デフォルト値: `none`


`proportional_axes`が`xy`に等しい時、
それらの相対的な長さに比例する軸で2Dシーンが描かれます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


このオプションは2Dプロットでだけ機能します。
一旦Gnuplot 4.3が公式にリリースされたら、
`proportional_axes`は3Dプロットに拡張させるでしょう。


例:


単プロット。



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        ellipse(0,0,1,1,0,360),
        transparent=true,
        color = blue,
        line_width = 4,
        ellipse(0,0,2,1/2,0,360),
        proportional_axes = xy) $
```


多重プロット。



```maxima
(%i1) load("draw")$
(%i2) draw(
        terminal = wxt,
        gr2d(proportional_axes = xy,
             explicit(x^2,x,0,1)),
        gr2d(explicit(x^2,x,0,1),
             xrange = [0,1],
             yrange = [0,2],
             proportional_axes=xy),
        gr2d(explicit(x^2,x,0,1))
```

<!-- category: Plotting -->
<!-- keywords: quadrilateral -->
<!-- signatures: quadrilateral(point_1, point_2, point_3, point_4) -->
### Function: quadrilateral (point_1, point_2, point_3, point_4)

四辺形を描画します。


**2D**


`quadrilateral ([x1, y1], [x2, y2], [x3, y3], [x4, y4])`は
頂点`[x1, y1]`, `[x2, y2]`,
`[x3, y3]`, `[x4, y4]`を持つ四辺形を描画します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:

`transparent`, `fill_color`, `border`, `line_width`,
`key`, `xaxis_secondary`, `yaxis_secondary`, `line_type`,
`transform`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        quadrilateral([1,1],[2,2],[3,-1],[2,-2]))$
```


**3D**


`quadrilateral([x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4])`は
頂点`[x1, y1, z1]`, `[x2, y2, z2]`,
`[x3, y3, z3]`, `[x4, y4, z4]`を持つ
四辺形を描画します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます: `line_type`, 
`line_width`, `color`, `key`, `enhanced3d`, `transform`.

<!-- category: Plotting -->
<!-- keywords: read_xpm -->
<!-- signatures: read_xpm(xpm_file) -->
### Function: read_xpm (xpm_file)

xpm形式のファイルを読み、ピクチャオブジェクトを返します。

<!-- category: Plotting -->
<!-- keywords: rectangle -->
<!-- signatures: rectangle([x1, y1], [x2, y2]) -->
### Function: rectangle ([x1, y1], [x2, y2])

2D内で長方形を描画します。


**2D**


`rectangle ([x1,y1], [x2,y2])`は、
対角頂点
`[x1,y1]`と`[x2,y2]`
を持つ長方形を描画します。


このオブジェクトは以下の
*グラフィックオプション*の影響を受けます: `transparent`, 
`fill_color`, `border`, `line_width`, `key`,
`line_type`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = red,
             line_width  = 6,
             line_type   = dots,
             transparent = false,
             fill_color  = blue,
             rectangle([-2,-2],[8,-1]), /* opposite vertices */
             transparent = true,
             line_type   = solid,
             line_width  = 1,
             rectangle([9,4],[2,-1.5]),
             xrange      = [-3,10],
             yrange      = [-3,4.5] )$
```

<!-- category: Plotting -->
<!-- keywords: region -->
<!-- signatures: region(expr, var1, minval1, maxval1, var2, minval2, maxval2) -->
### Function: region (expr, var1, minval1, maxval1, var2, minval2, maxval2)

平面上に不等式で定義された領域を描画します。


**2D**
*expr*は不等式とブーリアン演算子`and`, `or`, `not`で形成された式です。
領域は
$[minval1, maxval1]$と$[minval2, maxval2]$で
定義された長方形で区切られています。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます: `fill_color`, 
`key`, `x_voxel`, `y_voxel`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        x_voxel = 30,
        y_voxel = 30,
        region(x^2+y^2<1 and x^2+y^2 > 1/2,
               x, -1.5, 1.5, y, -1.5, 1.5));
```

<!-- category: Plotting -->
<!-- keywords: region_boundaries -->
<!-- signatures: region_boundaries(x1, y1, x2, y2) -->
### Function: region_boundaries (x1, y1, x2, y2)

頂点(*x1*,*y1*) -左上- と(*x2*,*y2*) -右下-の長方形に完全に含まれる
グローバル変数`boundaries_array`の多角形セグメント検出します。



例:


南イタリアをプロットするためのセグメントの数を返します。


```maxima
(%i1) load("worldmap")$
(%i2) region_boundaries(10.4,41.5,20.7,35.4);
(%o2)                [1846, 1863, 1864, 1881, 1888, 1894]
(%i3) draw2d(geomap(%))$
```

<!-- category: Plotting -->
<!-- keywords: region_boundaries_plus -->
<!-- signatures: region_boundaries_plus(x1, y1, x2, y2) -->
### Function: region_boundaries_plus (x1, y1, x2, y2)

頂点(*x1*,*y1*) -左上- と(*x2*,*y2*) -右下-で定義された長方形に少なくとも1つ頂点を含まれる
グローバル変数`boundaries_array`の多角形セグメント検出します。
多角形セグメント検出します。


例:



```maxima
(%i1) load("worldmap")$
(%i2) region_boundaries_plus(10.4,41.5,20.7,35.4);
(%o2) [1060, 1062, 1076, 1835, 1839, 1844, 1846, 1858,
       1861, 1863, 1864, 1871, 1881, 1888, 1894, 1897]
(%i3) draw2d(geomap(%))$
```

<!-- category: Plotting -->
<!-- keywords: rgb2level -->
<!-- signatures: rgb2level(pic) -->
### Function: rgb2level (pic)

*rgb*ピクチャを
赤、緑、青チャンネルを平均することで*level*の１つに変換します。

<!-- category: Plotting -->
<!-- keywords: set_draw_defaults -->
<!-- signatures: set_draw_defaults(graphic option, ..., graphic object, ...) -->
### Function: set_draw_defaults (graphic option, ..., graphic object, ...)

ユーザーグラフィックオプションを設定します。
この関数は
共通のグラフィックスオプションで一連のグラフィックスをプロットするのに
役に立ちます。
引数なしにこの関数を呼ぶと、ユーザーデフォルトを取り除きます。


例:



```maxima
(%i1) load("draw")$
(%i2) set_draw_defaults(
         xrange = [-10,10],
         yrange = [-2, 2],
         color  = blue,
         grid   = true)$
(%i3) /* plot with user defaults */
      draw2d(explicit(((1+x)**2/(1+x*x))-1,x,-10,10))$
(%i4) set_draw_defaults()$
(%i5) /* plot with standard defaults */
      draw2d(explicit(((1+x)**2/(1+x*x))-1,x,-10,10))$
```


この関数を利用するには、
最初に`load("draw")`を書いてください。

<!-- category: Plotting -->
<!-- keywords: spherical -->
<!-- signatures: spherical(radius, azi, minazi, maxazi, zen, minzen, maxzen) -->
### Function: spherical (radius, azi, minazi, maxazi, zen, minzen, maxzen)

球座標で定義された3D関数を描画します。


**3D**


`spherical(radius, azi, minazi, maxazi, zen, minzen, maxzen)`は
*minazi*から *maxazi*まで値を取る *方位角* *azi*と
*minzen*から *maxzen*まで値を取る *天頂角* *zen*を伴う
球座標で定義された関数 `radius(azi, zen)`
を描画します。



このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`xu_grid`, 
`yv_grid`, `line_type`, `key`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(spherical(1,a,0,2*%pi,z,0,%pi))$
```

<!-- category: Plotting -->
<!-- keywords: surface_hide -->
<!-- signatures: surface_hide -->
### Variable: surface_hide

デフォルト値: `false`


もし`surface_hide`が`true`なら、
隠れた部分は3d表面にプロットされません。


これはグローバルグラフィックオプションなので、
シーン記述での位置はかまいません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw(columns=2,
           gr3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)),
           gr3d(surface_hide = true,
                explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)) )$
```

<!-- category: Plotting -->
<!-- keywords: take_channel -->
<!-- signatures: take_channel(im, color) -->
### Function: take_channel (im, color)

もし引数*color*が`red`, `green`または`blue`なら、
関数`take_channel`は
ピクチャ*im*の対応する色チャンネルを返します。
例:



```maxima
(%i1) load("draw")$
(%i2) red: make_level_picture(matrix([3,2],[7,260]));
(%o2)           picture(level, 2, 2, {Array:  #(3 2 7 255)})
(%i3) green: make_level_picture(matrix([54,23],[73,-9]));
(%o3)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
(%i4) blue: make_level_picture(matrix([123,82],[45,32.5698]));
(%o4)          picture(level, 2, 2, {Array:  #(123 82 45 33)})
(%i5) make_rgb_picture(red,green,blue);
(%o5) picture(rgb, 2, 2, 
              {Array:  #(3 54 123 2 23 82 7 73 45 255 0 33)})
(%i6) take_channel(%,'green);  /* simple quote!!! */
(%o6)           picture(level, 2, 2, {Array:  #(54 23 73 0)})
```

<!-- category: Plotting -->
<!-- keywords: terminal -->
<!-- signatures: terminal -->
### Variable: terminal

デフォルト値: `screen`


Gnuplotが使う端末を選択します; 可能な値は:
`screen` (デフォルト), `png`, `pngcairo`, `jpg`, `eps`, `eps_color`,
`pdf`, `pdfcairo`, `gif`, `animated_gif`, `wxt`, `aquaterm`.


端末`screen`, `wxt`, `aquaterm`は２つの要素を持つリストとしても定義できます:
端末自身の名前と非負の整数。
この形式では、それぞれ対応する番号を持つ複数のウィンドウを同時に開くことができます。
この特長はWindowsプラットフォームでは機能しません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。
関数`draw`の引数としても使われます。


注意せよ―pdfcairoはGnuplot 4.3を必要とします。
(2008年11月)現在、Gnuplot 4.3は開発バージョンです。
pdfは、
Gnuplot 4.2/4.3を
オプション`--enable-pdf`でコンパイルすることを
必要とし、libpdfがインストールされていなければいけません。
pdfライブラリは以下で利用可能です: [http://www.pdflib.com/en/download/pdflib-family/pdflib-lite/]()


例:



```maxima
(%i1) load("draw")$
(%i2) /* screen terminal (default) */
      draw2d(explicit(x^2,x,-1,1))$
(%i3) /* png file */
      draw2d(terminal  = 'png,
             explicit(x^2,x,-1,1))$
(%i4) /* jpg file */
      draw2d(terminal   = 'jpg,
             dimensions = [300,300],
             explicit(x^2,x,-1,1))$
(%i5) /* eps file */
      draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'eps)$
(%i6) /* pdf file */
      draw2d(file_name = "mypdf",
             dimensions = 100*[12.0,8.0],
             explicit(x^2,x,-1,1),
             terminal  = 'pdf)$
(%i7) /* wxwidgets window */
      draw2d(explicit(x^2,x,-1,1),
             terminal  = 'wxt)$
```


複数のウィンドウ。


```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^5,x,-2,2), terminal=[screen, 3])$
(%i3) draw2d(explicit(x^2,x,-2,2), terminal=[screen, 0])$
```


動画gifファイル。


```maxima
(%i1) load("draw")$
(%i2) draw(
        delay     = 100,
        file_name = "zzz",
        terminal  = 'animated_gif,
        gr2d(explicit(x^2,x,-1,1)),
        gr2d(explicit(x^3,x,-1,1)),
        gr2d(explicit(x^4,x,-1,1)));
End of animation sequence
(%o2)          [gr2d(explicit), gr2d(explicit), gr2d(explicit)]
```


オプション`delay`は動画gifでだけ有効です;
他のいかなる場合も無視されます。


`file_name`, `dimensions`, `delay`も参照してください。

<!-- category: Plotting -->
<!-- keywords: title -->
<!-- signatures: title -->
### Variable: title

デフォルト値: `""` (empty string)


オプション`title`、文字列は、シーンのメインタイトルです。
デフォルトではタイトルは書かれません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(u),u,-2,2),
             title = "Exponential function")$
```

<!-- category: Plotting -->
<!-- keywords: transform -->
<!-- signatures: transform -->
### Variable: transform

デフォルト値: `none`


もし`transform`が`none`なら、
空間は変換されず、グラフィックオブジェクトは定義の通り描画されます。
空間変換が望まれた時、リストがオプション`transform`に割り当てられなければいけません。
2Dシーンの場合、
リストは形式`[f1(x,y), f2(x,y), x, y]`を取ります。
3Dシーンの場合、
リストは形式`[f1(x,y,z), f2(x,y,z), f3(x,y,z), x, y, z]`を取ります。
リストの中で定義されている変数名は
グラフィックオブジェクトの定義の中で使われるものと異なるかもしれません。


例:


2Dの回転。



```maxima
(%i1) load("draw")$
(%i2) th : %pi / 4$
(%i3) draw2d(
        color = "#e245f0",
        proportional_axes = 'xy,
        line_width = 8,
        triangle([3,2],[7,2],[5,5]),
        border     = false,
        fill_color = yellow,
        transform  = [cos(th)*x - sin(th)*y,
                      sin(th)*x + cos(th)*y, x, y],
        triangle([3,2],[7,2],[5,5]) )$
```


3Dでの変形。



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        color     = "#a02c00",
        explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
        transform = [x+10,y+10,z+10,x,y,z],
        color     = blue,
        explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3) )$
```

<!-- category: Plotting -->
<!-- keywords: transparent -->
<!-- signatures: transparent -->
### Variable: transparent

デフォルト値: `false`


もし`transparent`が`true`なら、
ポリゴンの内側の領域は`fill_color`に従って塗りつぶされます。


このオプションは以下のグラフィックオブジェクトに影響します:


- *
`gr2d`: `polygon`, `rectangle`, と`ellipse`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(polygon([[3,2],[7,2],[5,5]]),
             transparent = true,
             color       = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: triangle -->
<!-- signatures: triangle(point_1, point_2, point_3) -->
### Function: triangle (point_1, point_2, point_3)

三角形を描画します。


**2D**


`triangle ([x1,y1], [x2,y2], [x3,y3])`は、頂点`[x1,y1]`, `[x2,y2]`, `[x3,y3]`を持つ三角形を描画します。


このオブジェクトは、
以下の*グラフィックオプション*に影響されます:

`transparent`, `fill_color`, `border`, `line_width`,
`key`, `xaxis_secondary`, `yaxis_secondary`, `line_type`,
`transform`, `color`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
        triangle([1,1],[2,2],[3,-1]))$
```


**3D**


`triangle ([x1,y1,z1], [x2,y2,z2], [x3,y3,z3])`は
頂点`[x1,y1,z1]`, `[x2,y2,z2]`,
`[x3,y3,z3]`を持つ三角形を描画します。


このオブジェクトは以下の*グラフィックオプション*に影響されます:
`line_type`, `line_width`, `color`, `key`, `enhanced3d`, `transform`.

<!-- category: Plotting -->
<!-- keywords: tube -->
<!-- signatures: tube(xfun, yfun, zfun, rfun, p, pmin, pmax) -->
### Function: tube (xfun, yfun, zfun, rfun, p, pmin, pmax)

3Dにおいて
径が変化する管を描画します。


**3D**


`[xfun,yfun,zfun]`は
*pmin*から*pmax*まで値を取るパラメータ*p*を伴う
パラメトリックな曲線です。
パラメトリックな曲線上に中心を持ち、曲線と垂直な半径*rfun*の円が置かれます。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`xu_grid`, 
`yv_grid`, `line_type`, `line_width`, `key`, `enhanced3d`,
`color`, `tube_extremes`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        enhanced3d = true,
        xu_grid = 50,
        tube(cos(a), a, 0, cos(a/10)^2,
             a, 0, 4*%pi) )$
```

<!-- category: Plotting -->
<!-- keywords: tube_extremes -->
<!-- signatures: tube_extremes -->
### Variable: tube_extremes

デフォルト値: `[open, open]`


グラフィックオブジェクト`tube`の極値が開いたままか
閉じていなければいけないかを示唆する
2つの可能性のある要素`open`と`closed`を持つリスト。
デフォルトでは、どちらの極値も開いたままです。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(
        tube_extremes = [open, closed],
        tube(0, 0, a, 1,
             a, 0, 8) )$
```

<!-- category: Plotting -->
<!-- keywords: unit_vectors -->
<!-- signatures: unit_vectors -->
### Variable: unit_vectors

デフォルト値: `false`


もし`unit_vectors`が`true`なら、
ベクトルは単位1でプロットされます。
これはベクトル場をプロットするのに役に立ちます。
もし`unit_vectors`が`false`なら、
ベクトルは元の長さでプロットされます。


このオプションは`vector`オブジェクトに対してだけ有効です。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [-1,6],
             yrange      = [-1,6],
             head_length = 0.1,
             vector([0,0],[5,2]),
             unit_vectors = true,
             color        = red,
             vector([0,3],[5,2]))$
```

<!-- category: Plotting -->
<!-- keywords: user_preamble -->
<!-- signatures: user_preamble -->
### Variable: user_preamble

デフォルト値: `""` (empty string)


熟練Gnuplotユーザーは、
`plot`や`splot`コマンドの前に送られる設定を書くことで、
このオプションを利用して、
Gnuplotの振る舞いを微調整することができます。


このオプションの値は文字列か(行毎に１つの)文字列のリスト
でなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:


*ダム*端末は、パッケージ`draw`でサポートされていませんが、
オプション`user_preamble`の利用によって、それを設定することが可能です。


```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(x)-1,x,-1,1),
             parametric(cos(u),sin(u),u,0,2*%pi),
             user_preamble="set terminal dumb")$
```

<!-- category: Plotting -->
<!-- keywords: vector -->
<!-- signatures: vector([x, y], [dx, dy]), vector([x, y, z], [dx, dy, dz]) -->
### Function: vector ([x, y], [dx, dy])

2Dおよび3D内でベクトルを描画します。


このオブジェクトは以下の*グラフィックオプション*の影響を受けます:
`head_both`, 
`head_length`, `head_angle`, `head_type`, `line_width`, 
`line_type`, `key`, `color`.


**2D**


`vector([x,y], [dx,dy])`は
`[x,y]`を原点とするベクトル`[dx,dy]`を
プロットします。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,12],
             yrange      = [0,10],
             head_length = 1,
             vector([0,1],[5,5]), /* default type */
             head_type = 'empty,
             vector([3,1],[5,5]),
             head_both = true,
             head_type = 'nofilled,
             line_type = dots,
             vector([6,1],[5,5]))$
```


**3D**


`vector([x,y,z], [dx,dy,dz])`は
`[x,y,z]`を原点とする
ベクトル`[dx,dy,dz]`をプロットします。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(color = cyan,
             vector([0,0,0],[1,1,1]/sqrt(3)),
             vector([0,0,0],[1,-1,0]/sqrt(2)),
             vector([0,0,0],[1,1,-2]/sqrt(6)) )$
```

<!-- category: Plotting -->
<!-- keywords: view -->
<!-- signatures: view -->
### Variable: view

デフォルト値: `[60,30]`


3Dシーンでビュー方向を示す度数で測られた角度の対。
最初の角度は*x*軸回りの垂直回転であり、$[0, 180]$の範囲です。
二番目は*z*回りの水平回転であり、$[0, 360]$の範囲です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(view = [170, 360],
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```

<!-- category: Plotting -->
<!-- keywords: x_voxel -->
<!-- signatures: x_voxel -->
### Variable: x_voxel

デフォルト値: 10


`x_voxel`は
3d `暗黙の`オブジェクトで実装された*マーチングキューブアルゴリズム*
x方向のボクセルの数です。
グラフィックオブジェクト`region`でも使われます。

<!-- category: Plotting -->
<!-- keywords: xaxis -->
<!-- signatures: xaxis -->
### Variable: xaxis

デフォルト値: `false`


もし`xaxis`が`true`なら、
*x*軸が描かれます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_color = blue)$
```


`xaxis_width`, `xaxis_type`, `xaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xaxis_color -->
<!-- signatures: xaxis_color -->
### Variable: xaxis_color

デフォルト値: `"black"`


`xaxis_color`は*x*軸の色を指定します。
いかに色が定義されるかを知るには`color`を参照してください。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_color = red)$
```


`xaxis`, `xaxis_width`, `xaxis_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xaxis_secondary -->
<!-- signatures: xaxis_secondary -->
### Variable: xaxis_secondary

デフォルト値: `false`


もし`xaxis_secondary`が`true`なら、
関数値が、二番目の*x*軸に関してプロットされるかもしれません。
二番目の*x*軸はシーンのトップに描かれます。


これは、2dプロットにだけ影響する局所的なグラフィックオプションであることに注意してください。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         key   = "Bottom x-axis",
         explicit(x+1,x,1,2),
         color = red,
         key   = "Above x-axis",
         xtics_secondary = true,
         xaxis_secondary = true,
         explicit(x^2,x,-1,1)) $
```


`xrange_secondary`, `xtics_secondary`, `xtics_rotate_secondary`,
`xtics_axis_secondary`, `xaxis_secondary`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xaxis_type -->
<!-- signatures: xaxis_type -->
### Variable: xaxis_type

デフォルト値: `dots`


`xaxis_type`は*x*軸がいかに表示されるかを示します;
可能な値は`solid`と`dots`です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_type  = solid)$
```


`xaxis`, `xaxis_width`, `xaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xaxis_width -->
<!-- signatures: xaxis_width -->
### Variable: xaxis_width

デフォルト値: 1


`xaxis_width`は*x*軸の幅です。
その値は正数でなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             xaxis       = true,
             xaxis_width = 3)$
```


`xaxis`, `xaxis_type`, `xaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xrange -->
<!-- signatures: xrange -->
### Variable: xrange

デフォルト値: `auto`


もし`xrange`が`auto`なら、
*x*座標の範囲は自動的に計算されます。


もしユーザーが
*x*に関して特定の区間が欲しいなら、
`xrange=[-2, 3]`のように、Maximaリストとして与えられなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange = [-3,5],
             explicit(x^2,x,-1,1))$
```


`yrange`と`zrange`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xrange_secondary -->
<!-- signatures: xrange_secondary -->
### Variable: xrange_secondary

デフォルト値: `auto`


もし`xrange_secondary`が`auto`なら、
二番目の*x*軸の範囲は自動的に計算されます。


もしユーザーが
二番目の*x*軸の特定した区間が欲しいなら、
`xrange_secondary=[-2, 3]`のように、Maximaリストとして与えられなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


`xrange`, `yrange`, `zrange`, `yrange_secondary`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xtics -->
<!-- signatures: xtics -->
### Variable: xtics

デフォルト値: `auto`


このグラフィックオプション制御は
チックマークを*x*軸上に描く方法を制御します。



- *
オプション`xtics`がシンボル*auto*にバインドされている時
チックマークは自動的に描かれます。
- *
オプション`xtics`がシンボル*none*にバインドされている時
チックマークは描かれません。
- *
オプション`xtics`が正の数にバインドされている時、
これは２つの連続するチックマークの間の距離になります。
- *
オプション`xtics`が
形式`[start,incr,end]`の長さ３のリストにバインドされている時、
チックマークは
`start`から`end`まで
長さ`incr`の間隔でプロットされます。
- *
オプション`xtics`が
形式`{n1, n2, ...}`の数の集合にバインドされている時、
チックマークは
値`n1`, `n2`, ...にプロットされます。
- *
オプション`xtics`が
形式`{["label1", n1], ["label2", n2], ...}`の対の集合にバインドされている時、
値`n1`, `n2`, ...に対応する
チックマークはそれぞれ、
`"label1"`, `"label2"`, ...にラベルされます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:


チックをディセーブルします。


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = 'none,
             explicit(x^3,x,-1,1)  )$
```


1/4単位毎のチック。


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = 1/4,
             explicit(x^3,x,-1,1)  )$
```


-3/4から3/4まで
1/8のステップでチック。


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = [-3/4,1/8,3/4],
             explicit(x^3,x,-1,1)  )$
```


点-1/2, -1/4, 3/4にチック。


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = {-1/2,-1/4,3/4},
             explicit(x^3,x,-1,1)  )$
```


ラベルされたチック。


```maxima
(%i1) load("draw")$
(%i2) draw2d(xtics = {["High",0.75],["Medium",0],["Low",-0.75]},
             explicit(x^3,x,-1,1)  )$
```


`ytics`, `ztics`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xtics_axis -->
<!-- signatures: xtics_axis -->
### Variable: xtics_axis

デフォルト値: `false`


もし`xtics_axis`が`true`なら、
チックマークとそれらのラベルが
*x*軸に沿ってだけプロットされます。
もし`false`なら、チックは境界上にプロットされます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: xtics_rotate -->
<!-- signatures: xtics_rotate -->
### Variable: xtics_rotate

デフォルト値: `false`


もし`xtics_rotate`が`true`なら、
*x*軸上のチックマークが90度回転されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: xtics_rotate_secondary -->
<!-- signatures: xtics_rotate_secondary -->
### Variable: xtics_rotate_secondary

デフォルト値: `false`


もし`xtics_rotate_secondary`が`true`なら、
補助的な*x*軸上のチックマークが90度回転されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: xtics_secondary -->
<!-- signatures: xtics_secondary -->
### Variable: xtics_secondary

デフォルト値: `auto`


このグラフィックオプションは、
二番目の*x*軸上にチックマークを描く方法を制御します。


完全な記述に関しては、`xtics`を参照してください。

<!-- category: Plotting -->
<!-- keywords: xtics_secondary_axis -->
<!-- signatures: xtics_secondary_axis -->
### Variable: xtics_secondary_axis

デフォルト値: `false`


もし`xtics_secondary_axis`が`true`なら、
チックマークとそれらのラベルは補助的な*x*軸に沿ってだけプロットされ、
もし`false`なら、境界上にプロットされます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: xu_grid -->
<!-- signatures: xu_grid -->
### Variable: xu_grid

デフォルト値: 30


`xu_grid`は
サンプル点のグリッドを構築するための一番目の変数
(陽での`x`、パラメトリック3d表面での`u`)の座標の数です。


このオプションは以下のグラフィックオブジェクトに影響を与えます:


- *
`gr3d`: `explicit`と`parametric_surface`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


`yv_grid`も参照してください。

<!-- category: Plotting -->
<!-- keywords: xy_file -->
<!-- signatures: xy_file -->
### Variable: xy_file

デフォルト値: `""` (empty string)


`xy_file`は、
マウスでクリックし、’x’キーを叩いた後、座標が保存される
ファイルの名前です。
デフォルトでは、座標は保存されません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。

<!-- category: Plotting -->
<!-- keywords: xyplane -->
<!-- signatures: xyplane -->
### Variable: xyplane

デフォルト値: `false`


3Dシーンの中にxy平面を配置します。
`xyplane`が`false`の時、
xy平面は自動的に置かれます;
実数の時、xy平面はこのレベルでz軸と交わります。
このオプションは2Dシーンでは効果を持ちません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xyplane = %e-2,
             explicit(x^2+y^2,x,-1,1,y,-1,1))$
```

<!-- category: Plotting -->
<!-- keywords: y_voxel -->
<!-- signatures: y_voxel -->
### Variable: y_voxel

デフォルト値: 10


`y_voxel`は
3d`暗黙の`オブジェクトで実装された*マーチングキューブアルゴリズム*
で使われるy方向のボクセルの数です。
グラフィックオブジェクト`region`でも使われます。

<!-- category: Plotting -->
<!-- keywords: yaxis -->
<!-- signatures: yaxis -->
### Variable: yaxis

デフォルト値: `false`


もし`yaxis`が`true`なら、*y*軸が描かれます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_color = blue)$
```


`yaxis_width`, `yaxis_type`, `yaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: yaxis_color -->
<!-- signatures: yaxis_color -->
### Variable: yaxis_color

デフォルト値: `"black"`


`yaxis_color`は*y*軸の色を指定します。
色がどのように定義されているか知るには
`color`を参照してください。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_color = red)$
```


`yaxis`, `yaxis_width`, `yaxis_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: yaxis_secondary -->
<!-- signatures: yaxis_secondary -->
### Variable: yaxis_secondary

デフォルト値: `false`


もし`yaxis_secondary`が`true`なら、
関数値は二番目の*y*軸に関してプロットされるかもしれません。
二番目の*y*軸はシーンの右側に描かれます。


これは、2dプロットにだけ影響する局所的なグラフィックオプションであることに注意してください。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         explicit(sin(x),x,0,10),
         yaxis_secondary = true,
         ytics_secondary = true,
         color = blue,
         explicit(100*sin(x+0.1)+2,x,0,10));
```


`yrange_secondary`, `ytics_secondary`, `ytics_rotate_secondary`
, `ytics_axis_secondary`も参照してください。

<!-- category: Plotting -->
<!-- keywords: yaxis_type -->
<!-- signatures: yaxis_type -->
### Variable: yaxis_type

デフォルト値: `dots`


`yaxis_type`は*y*軸がどのように表示されるか示します; 
可能な値は`solid`と`dots`です。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_type  = solid)$
```


`yaxis`, `yaxis_width`, `yaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: yaxis_width -->
<!-- signatures: yaxis_width -->
### Variable: yaxis_width

デフォルト値: 1


`yaxis_width`は*y*軸の幅です。
その値は正の数でなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^3,x,-1,1),
             yaxis       = true,
             yaxis_width = 3)$
```


`yaxis`, `yaxis_type`, `yaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: yrange -->
<!-- signatures: yrange -->
### Variable: yrange

デフォルト値: `auto`


もし`yrange`が`auto`なら、
*y*座標の範囲は自動的に計算されます。


もしユーザーが*y*の特定の区間が欲しいなら、
`yrange=[-2, 3]`のように、Maximaリストとして与えられなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(yrange = [-2,3],
             explicit(x^2,x,-1,1),
             xrange = [-3,3])$
```


`xrange`, `yrange_secondary`, `zrange`も参照してください。

<!-- category: Plotting -->
<!-- keywords: yrange_secondary -->
<!-- signatures: yrange_secondary -->
### Variable: yrange_secondary

デフォルト値: `auto`


もし`yrange_secondary`が`auto`なら、
二番目の*y*軸の範囲は自動的に計算されます。


もしユーザーが二番目の*y*軸の特定の区間が欲しいなら、
`yrange_secondary=[-2, 3]`のように、Maximaリストとして与えられなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw2d(
         explicit(sin(x),x,0,10),
         yaxis_secondary = true,
         ytics_secondary = true,
         yrange = [-3, 3],
         yrange_secondary = [-20, 20],
         color = blue,
         explicit(100*sin(x+0.1)+2,x,0,10)) $
```


`xrange`, `yrange`, `zrange`も参照してください。

<!-- category: Plotting -->
<!-- keywords: ytics -->
<!-- signatures: ytics -->
### Variable: ytics

デフォルト値: `auto`


このグラフィックオプションは、
*y*軸上にチックマークを描く方法を制御します。


完全な記述に関しては、`xtics`を参照してください。

<!-- category: Plotting -->
<!-- keywords: ytics_axis -->
<!-- signatures: ytics_axis -->
### Variable: ytics_axis

デフォルト値: `false`


もし`ytics_axis`が`true`なら、
チックマークとそれらのラベルは*y*軸に沿ってだけプロットされ、
もし`false`なら、境界上にプロットされます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: ytics_rotate -->
<!-- signatures: ytics_rotate -->
### Variable: ytics_rotate

デフォルト値: `false`


もし`ytics_rotate`が`true`なら、
*y*軸上のチックマークが90度回転されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: ytics_rotate_secondary -->
<!-- signatures: ytics_rotate_secondary -->
### Variable: ytics_rotate_secondary

デフォルト値: `false`


もし`ytics_rotate_secondary`が`true`なら、
補助的な*y*軸上のチックマークが90度回転されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: ytics_secondary -->
<!-- signatures: ytics_secondary -->
### Variable: ytics_secondary

デフォルト値: `auto`


このグラフィックオプションは、
二番目の*y*軸上にチックマークを描く方法を制御します。


完全な記述に関しては、`xtics`を参照してください。

<!-- category: Plotting -->
<!-- keywords: ytics_secondary_axis -->
<!-- signatures: ytics_secondary_axis -->
### Variable: ytics_secondary_axis

デフォルト値: `false`


もし`ytics_secondary_axis`が`true`なら、
チックマークとそれらのラベルは補助的な*y*軸に沿ってだけプロットされ、
もし`false`なら、境界上にプロットされます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: yv_grid -->
<!-- signatures: yv_grid -->
### Variable: yv_grid

デフォルト値: 30


`yv_grid`は
サンプル点のグリッドを構築するための
二番目の変数(陽での`y`、パラメトリック3d表面での`v`)の座標の数です。


このオプションは以下のグラフィックオブジェクトに影響を与えます:


- *
`gr3d`: `explicit`と`parametric_surface`.


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


`xu_grid`も参照してください。

<!-- category: Plotting -->
<!-- keywords: z_voxel -->
<!-- signatures: z_voxel -->
### Variable: z_voxel

デフォルト値: 10


`z_voxel`は
3d`implicit`オブジェクトで実装された*マーチングキューブアルゴリズム*
で使われるz方向のボクセルの数です。

<!-- category: Plotting -->
<!-- keywords: zaxis -->
<!-- signatures: zaxis -->
### Variable: zaxis

デフォルト値: `false`


もし`zaxis`が`true`なら、3Dプロットで*z*軸が描かれます。
このオプションは2Dシーンでは効果を持ちません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_color = blue)$
```


`zaxis_width`, `zaxis_type`, `zaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: zaxis_color -->
<!-- signatures: zaxis_color -->
### Variable: zaxis_color

デフォルト値: `"black"`


`zaxis_color`は*z*軸の色を指定します。
色がどのように定義されているか知るには`color`を参照してください。
このオプションは2Dシーンでは効果を持ちません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_color = red)$
```


`zaxis`, `zaxis_width`, `zaxis_type`も参照してください。

<!-- category: Plotting -->
<!-- keywords: zaxis_type -->
<!-- signatures: zaxis_type -->
### Variable: zaxis_type

デフォルト値: `dots`


`zaxis_type`は*z*軸がどのように表示されるか示します;
可能な値は`solid`と`dots`です。
このオプションは2Dシーンでは効果を持ちません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid)$
```


`zaxis`, `zaxis_width`, `zaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: zaxis_width -->
<!-- signatures: zaxis_width -->
### Variable: zaxis_width

デフォルト値: 1


`zaxis_width`は*z*軸の幅です。
その値は正の数でなければいけません。
このオプションは2Dシーンでは効果を持ちません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題なりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(x^2+y^2,x,-1,1,y,-1,1),
             zaxis       = true,
             zaxis_type  = solid,
             zaxis_width = 3)$
```


`zaxis`, `zaxis_type`, `zaxis_color`も参照してください。

<!-- category: Plotting -->
<!-- keywords: zrange -->
<!-- signatures: zrange -->
### Variable: zrange

デフォルト値: `auto`


もし`zrange`が`auto`なら、
*z*座標の範囲は自動的に計算されます。


もしユーザーが
*z*の特定の区間が欲しいなら、
`zrange=[-2, 3]`のようにMaximaリストとして与えられなければいけません。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。


例:



```maxima
(%i1) load("draw")$
(%i2) draw3d(yrange = [-3,3],
             zrange = [-2,5],
             explicit(x^2+y^2,x,-1,1,y,-1,1),
             xrange = [-3,3])$
```


`xrange`, `yrange`も参照してください。

<!-- category: Plotting -->
<!-- keywords: ztics -->
<!-- signatures: ztics -->
### Variable: ztics

デフォルト値: `auto`


このグラフィックオプションは、
*z*軸上にチックマークを描く方法を制御します。


完全な記述に関しては、`xtics`を参照してください。

<!-- category: Plotting -->
<!-- keywords: ztics_axis -->
<!-- signatures: ztics_axis -->
### Variable: ztics_axis

デフォルト値: `false`


もし`ztics_secondary_axis`が`true`なら、
チックマークとそれらのラベルは補助的な*z*軸に沿ってだけプロットされ、
もし`false`なら、境界上にプロットされます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

<!-- category: Plotting -->
<!-- keywords: ztics_rotate -->
<!-- signatures: ztics_rotate -->
### Variable: ztics_rotate

デフォルト値: `false`


もし`ztics_rotate`が`true`なら、
*z*軸上のチックマークが90度回転されます。


これはグローバルグラフィックスオプションなので、
シーン記述の位置は問題になりません。

