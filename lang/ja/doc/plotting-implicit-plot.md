## implicit_plot

<!-- category: Plotting -->
<!-- keywords: implicit_plot -->
<!-- signatures: implicit_plot(expr, x_range, y_range), implicit_plot([expr_1, ..., expr_n], x_range, y_range) -->
### Function: implicit_plot (expr, x_range, y_range)

１つ以上の式のプロットを陰形式で表示します。
*expr*はプロットされる式で、
*x_range*は水平軸の範囲、
*y_range*は垂直軸の範囲です。
`implicit_plot`は
*set_plot_option*関数が設定するgnuplotドライバのグローバル設定を考慮します。
オプションはオプション引数として`implicit_plot`関数にも渡されることができます。


`implicit_plot`は
*x_range*と*y_range*で与えられる領域上で符号の変化を辿ることで機能し、
複雑な式では失敗する可能性があります。


`load("implicit_plot")`はこの関数をロードします。


例:


```maxima
(%i1) implicit_plot (x^2 = y^3 - 3*y + 1, [x, -4, 4], [y, -4, 4],
 [gnuplot_preamble, "set zeroaxis"]);
```

