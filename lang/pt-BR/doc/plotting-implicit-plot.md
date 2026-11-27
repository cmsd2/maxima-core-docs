## implicit_plot

<!-- category: Plotting -->
<!-- keywords: implicit_plot -->
<!-- signatures: implicit_plot(expr, x_range, y_range), implicit_plot([expr_1, ..., expr_n], x_range, y_range) -->
### Function: implicit_plot (expr, x_range, y_range)

Mostra na tela um gráfico de uma ou mais expressões na forma
implícita. *expr* é a expressão a ser montado o gráfico, *x_range* o
intervalo do eixo do eixo horizontal e *y_range* o intervalo do eixo
vertical. `implicit_plot` somente trabalha com o driver do
gnuplot. `implicit_plot` respeita as escolhas globais para o driver do
gnuplot escolhidas por meio da função *set_plot_option*. Opções podem tamb;em serem passadas para
a função `implicit_plot` como argumentos opcionais.


`implicit_plot` trabalha por meio de mudanças de sinal de trilha sobre a área
fornecida através de *x_range* e *y_range* e pode falhar em expressões
complicadas.


`load("implicit_plot")` torna essa função disponível para uso.


Exemplo:






```maxima
(%i1) load("implicit_plot")$
(%i2) implicit_plot (x^2 = y^3 - 3*y + 1, [x, -4, 4], [y, -4, 4])$
```


![./figures/plotting3](./figures/plotting3.png)

