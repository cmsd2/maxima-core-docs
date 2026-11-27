## drawdf

<!-- category: Plotting -->
<!-- keywords: drawdf -->
<!-- signatures: drawdf(dydx, ...optionsandobjects...), drawdf(dvdu, [u, v], ...optionsandobjects...), drawdf(dvdu, [u, umin, umax], [v, vmin, vmax], ...optionsandobjects...), drawdf([dxdt, dydt], ...optionsandobjects...), drawdf([dudt, dvdt], [u, v], ...optionsandobjects...), drawdf([dudt, dvdt], [u, umin, umax], [v, vmin, vmax], ...optionsandobjects...) -->
### Function: drawdf (dydx, ...optionsandobjects...)

関数`drawdf`は、
オプションの解曲線や`draw`パッケージを使う他のグラフィックスと一緒に、
2D方向場を描きます。


最初の引数は導関数を指定し、式か2つの式のリストでなければいけません。
*dydx*, *dxdt*, *dydt*は*x*と*y*に依存する式です。
*dvdu*, *dudt*, *dvdt*は*u*と*v*に依存する式です。


もし独立変数と従属変数が*x*と*y*でないなら、
それらの名前を、導関数に続いてすぐに、
2つの名前のリスト`[`*u*,*v*`]`のとしてか、
形式`[`*u*,*umin*,*umax*`]`と
`[`*v*,*vmin*,*vmax*`]`の2つのリストとしてのいずれか
のように,指定しなければいけません。


残りの引数は*グラフィックオプション*か*グラフィックオブジェクト*,
任意の深さで入れ子になったグラフィックオプションやオブジェクトを含むリストです。
`drawdf`がサポートするグラフィックオプションとオブジェクトの集合は
`draw`パッケージの`draw2d`と`gr2d`がサポートするもの上位集合です。


引数は順次解釈されます:
*グラフィックオプション*は続く*グラフィックオブジェクト*すべてに影響します。
更に、*グラフィックオブジェクト*は指定された順にキャンバス上に描かれ、
先に描かれたグラフィックスを見えなくするかもしれません。
いくつかの*グラフィックオプション*はシーンのグローバルな外観に影響します。


`drawdf`がサポートする追加の*グラフィックオブジェクト*は以下を含みます:
`solns_at`, `points_at`, `saddles_at`, `soln_at`,
`point_at`, `saddle_at`.


`drawdf`がサポートする追加の*グラフィックオプション*は以下を含みます:
`field_degree`, `soln_arrows`, `field_arrows`,
`field_grid`, `field_color`, `show_field`,
`tstep`, `nsteps`, `duration`, `direction`,
`field_tstep`, `field_nsteps`, `field_duration`.


`draw`パッケージから受け継がれた、共通に使われる*グラフィックオブジェクト*は
以下を含みます: `explicit`, `implicit`, `parametric`,
`polygon`, `points`, `vector`, `label`,
`draw2d`と`gr2d`がサポートする他のすべてのもの。


`draw`パッケージから受け継がれた、共通に使われる*グラフィックオプション*は
以下を含みます:

`points_joined`, `color`,
`point_type`, `point_size`, `line_width`,
`line_type`, `key`, `title`, `xlabel`,
`ylabel`, `user_preamble`, `terminal`,
`dimensions`, `file_name`,
`draw2d`と`gr2d`がサポートする他のすべてのもの。


`draw2d`も参照してください。


wxMaximaやImaximaのユーザーは`wxdrawdf`を代わりに使うかもしれません。
それは、
グラフィックスが`wxdraw`を使うノートブック内で描かれることを除いて、
`drawdf`と同一です。


この関数を利用するには、最初に`load("drawdf")`を書いてください。


例:



```maxima
(%i1) load("drawdf")$
(%i2) drawdf(exp(-x)+y)$        /* default vars: x,y */
(%i3) drawdf(exp(-t)+y, [t,y])$ /* default range: [-10,10] */
(%i4) drawdf([y,-9*sin(x)-y/5], [x,1,5], [y,-2,2])$
```


下位互換のために、`drawdf`はplotdfがサポートしたパラメータのほとんどを
受け付けます。



```maxima
(%i5) drawdf(2*cos(t)-1+y, [t,y], [t,-5,10], [y,-4,9],
             [trajectory_at,0,0])$
```


`soln_at`と`solns_at`は、
少し強化された4次のRunge Kutta数値積分器を使って、
指定された点を通る解曲線を描きます。



```maxima
(%i6) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             solns_at([0,0.1],[0,-0.1]),
             color=blue, soln_at(0,0))$
```


`field_degree=2`とすると、
それぞれのグリッド点での1次と2次の導関数に基づいて、
場が二次のスプラインで構成されます。
`field_grid=[`*COLS*,*ROWS*`]`は
グリッドの列と行の数を指定します。



```maxima
(%i7) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             field_degree=2, field_grid=[20,15],
             solns_at([0,0.1],[0,-0.1]),
             color=blue, soln_at(0,0))$
```


`soln_arrows=true`は
解曲線に矢印を加え、
(デフォルトでは)方向場からそれらを削除します。
また、解曲線を強調するようにデフォルトの色を変えます。



```maxima
(%i8) drawdf(2*cos(t)-1+y, [t,-5,10], [y,-4,9],
             soln_arrows=true,
             solns_at([0,0.1],[0,-0.1],[0,0]))$
```


`duration=40`は数値積分の時間間隔を指定します(デフォルトは10))。
もし解がプロット領域から遠くに移動し過ぎたり、
導関数が複素数や無限大になったりしても、積分は自動的に停止します。
ここでも、 `field_degree=2`を指定して二次スプラインをプロットします。
以下の方程式は捕食者-被食者系をモデル化します。



```maxima
(%i9) drawdf([x*(1-x-y), y*(3/4-y-x/2)], [x,0,1.1], [y,0,1],
             field_degree=2, duration=40,
             soln_arrows=true, point_at(1/2,1/2),
             solns_at([0.1,0.2], [0.2,0.1], [1,0.8], [0.8,1],
                      [0.1,0.1], [0.6,0.05], [0.05,0.4],
                      [1,0.01], [0.01,0.75]))$
```


`field_degree='solns`とすると、
場は、4次のRunge Kuttaで計算された多くの小さな解曲線で構成され、
この場合、より良い結果をもたらします。



```maxima
(%i10) drawdf([x*(1-x-y), y*(3/4-y-x/2)], [x,0,1.1], [y,0,1],
              field_degree='solns, duration=40,
              soln_arrows=true, point_at(1/2,1/2),
              solns_at([0.1,0.2], [0.2,0.1], [1,0.8],
                       [0.8,1], [0.1,0.1], [0.6,0.05],
                       [0.05,0.4], [1,0.01], [0.01,0.75]))$
```


`saddles_at`は
自動的にそれぞれの鞍部で方程式を線形化しようとし、
セパラトリクスを含む、それぞれの固有ベクトルに対応した数値解をプロットしようとします。
`tstep=0.05`は
数値積分器の最大時間ステップを指定します(デフォルトは0.1)。
xとyのステップを小さく保つために、小さ目の時間ステップが時々使われます。
以下の方程式は減衰振り子をモデル化します。



```maxima
(%i11) drawdf([y,-9*sin(x)-y/5], tstep=0.05,
              soln_arrows=true, point_size=0.5,
              points_at([0,0], [2*%pi,0], [-2*%pi,0]),
              field_degree='solns,
              saddles_at([%pi,0], [-%pi,0]))$
```


`show_field=false`は場を完全に抑制します。



```maxima
(%i12) drawdf([y,-9*sin(x)-y/5], tstep=0.05,
              show_field=false, soln_arrows=true,
              point_size=0.5,
              points_at([0,0], [2*%pi,0], [-2*%pi,0]),
              saddles_at([3*%pi,0], [-3*%pi,0],
                         [%pi,0], [-%pi,0]))$
```


`drawdf`は、認識しないパラメータすべてを`draw2d`や`gr2d`に渡します。
なので、`draw`パッケージのフルパワーを`drawdf`と組み合わせられます。



```maxima
(%i13) drawdf(x^2+y^2, [x,-2,2], [y,-2,2], field_color=gray,
              key="soln 1", color=black, soln_at(0,0),
              key="soln 2", color=red, soln_at(0,1),
              key="isocline", color=green, line_width=2,
              nticks=100, parametric(cos(t),sin(t),t,0,2*%pi))$
```


`drawdf`はグラフィクオプションやオブジェクトの入れ子のリストを受け付けます。
なので、makelistやグラフィックスを生成する他の関数コールの便利な使用が可能です。



```maxima
(%i14) colors : ['red,'blue,'purple,'orange,'green]$
(%i15) drawdf([x-x*y/2, (x*y - 3*y)/4],
              [x,2.5,3.5], [y,1.5,2.5],
              field_color = gray,
              makelist([ key   = concat("soln",k),
                         color = colors[k],
                         soln_at(3, 2 + k/20) ],
                       k,1,5))$
```

