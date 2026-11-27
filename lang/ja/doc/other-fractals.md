## fractals

<!-- category: Other -->
<!-- keywords: fernfale -->
<!-- signatures: fernfale(n) -->
### Function: fernfale (n)

変換を選択する確率が縮小比に関係する、4つの縮小写像。
引数*n*は十分大きく、10000以上でなければいけません、


例:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,fernfale(n)], [style,dots])$
```

<!-- category: Other -->
<!-- keywords: hilbertmap -->
<!-- signatures: hilbertmap(nn) -->
### Function: hilbertmap (nn)

Hilbert写像。
*nn*は小さく(例えば5で)なければいけません。
もし7以上ならMaximaはクラッシュするかもしれません。


例:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,hilbertmap(6)])$
```

<!-- category: Other -->
<!-- keywords: julia_parameter -->
<!-- signatures: julia_parameter -->
### Variable: julia_parameter

デフォルト値: `%i`


Juliaフラクタルの複素パラメータ。
デフォルト値は`%i`です;
 we  suggest the  values 
値`-.745+%i*.113002`, 
`-.39054-%i*.58679`, `-.15652+%i*1.03225`, `-.194+%i*.6557`, 
`.011031-%i*.67037`を提案します。

<!-- category: Other -->
<!-- keywords: julia_set -->
<!-- signatures: julia_set(x, y) -->
### Function: julia_set (x, y)

Julia集合。


たくさんの演算を実行しなければいけないので、このプログラムは時間がかかります;
計算時間は格子点の数にも関係します。


例:



```maxima
(%i1) load("fractals")$
(%i2) plot3d (julia_set, [x, -2, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


See also `julia_parameter`.

<!-- category: Other -->
<!-- keywords: julia_sin -->
<!-- signatures: julia_sin(x, y) -->
### Function: julia_sin (x, y)

関数`julia_set`が変換`julia_parameter+z^2`を実装する一方、
関数`julia_sin`は`julia_parameter*sin(z)`を実装します。
詳細はソースコードを参照してください。


たくさんのsinを計算するので、このプログラムはゆっくり実行されます


例:


たくさんの演算を実行しなければいけないので、このプログラムは時間がかかります;
計算時間は格子点の数にも関係します。



```maxima
(%i1) load("fractals")$
(%i2) julia_parameter:1+.1*%i$
(%i3) plot3d (julia_sin, [x, -2, 2], [y, -3, 3], 
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```


See also `julia_parameter`.

<!-- category: Other -->
<!-- keywords: mandelbrot_set -->
<!-- signatures: mandelbrot_set(x, y) -->
### Function: mandelbrot_set (x, y)

Mandelbrot集合。


例:


たくさんの演算を実行しなければいけないので、このプログラムは時間がかかります;
計算時間は格子点の数にも関係します。



```maxima
(%i1) load("fractals")$
(%i2) plot3d (mandelbrot_set, [x, -2.5, 1], [y, -1.5, 1.5],
                [gnuplot_preamble, "set view map"],
                [gnuplot_pm3d, true],
                [grid, 150, 150])$
```

<!-- category: Other -->
<!-- keywords: sierpinskiale -->
<!-- signatures: sierpinskiale(n) -->
### Function: sierpinskiale (n)

Sierpinski三角形: 3つの縮小写像; .5の縮小定数と変形;
すべての写像は同じ縮小比です。
引数*n*は十分大きく、10000以上でなければいけません、


例:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,sierpinskiale(n)], [style,dots])$
```

<!-- category: Other -->
<!-- keywords: sierpinskimap -->
<!-- signatures: sierpinskimap(nn) -->
### Function: sierpinskimap (nn)

Sierpinski写像。
*nn*は小さく(例えば5で)なければいけません。
もし7以上ならMaximaはクラッシュするかもしれません。


例:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,sierpinskimap(6)])$
```

<!-- category: Other -->
<!-- keywords: snowmap -->
<!-- signatures: snowmap(ent, nn) -->
### Function: snowmap (ent, nn)

Koch雪片集合。
関数`snowmap`は、
複素平面内の初期値の閉多角形の頂点上に雪Koch写像をプロットします。
ここで多角形の向きが重要です。
引数Argument *nn*はKoch変換の繰り返し適用の回数です;
*nn*は小さく(5か6で)なければいけません。


例:



```maxima
(%i1) load("fractals")$
(%i2) plot2d([discrete,
              snowmap([1,exp(%i*%pi*2/3),exp(-%i*%pi*2/3),1],4)])$
(%i3) plot2d([discrete,
              snowmap([1,exp(-%i*%pi*2/3),exp(%i*%pi*2/3),1],4)])$
(%i4) plot2d([discrete, snowmap([0,1,1+%i,%i,0],4)])$
(%i5) plot2d([discrete, snowmap([0,%i,1+%i,1,0],4)])$
```

<!-- category: Other -->
<!-- keywords: treefale -->
<!-- signatures: treefale(n) -->
### Function: treefale (n)

すべて同じ縮小比を持つ3つの縮小写像。
引数*n*は十分大きく、10000以上でなければいけません、


例:



```maxima
(%i1) load("fractals")$
(%i2) n: 10000$
(%i3) plot2d([discrete,treefale(n)], [style,dots])$
```

