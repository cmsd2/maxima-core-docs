## Montando Gráficos

<!-- category: Other -->
<!-- keywords: contour_plot -->
<!-- signatures: contour_plot(expr, x_range, y_range, opções, ...) -->
### Function: contour_plot (expr, x_range, y_range, opções, ...)

Monta gráficos de contorno (curvas de nível) de *expr*
sobre a região *x_range* por *y_range*.
Quaisquer argumentos adicionals são tratados da mesma forma que em `plot3d`.


`contour_plot` somente trabalha quando o formato do gráfico for `gnuplot` ou `gnuplot_pipes`.


Veja também `implicit_plot`.


Exemplos:












```maxima
(%i1) contour_plot (x^2 + y^2, [x, -4, 4], [y, -4, 4]);
(%o1) 
(%i2) contour_plot (sin(y) * cos(x)^2, [x, -4, 4], [y, -4, 4]);
(%o2) 
(%i3) F(x, y) := x^3 + y^2;
                                   3    2
(%o3)                  F(x, y) := x  + y
(%i4) contour_plot (F, [u, -4, 4], [v, -4, 4]);
(%o4) 
(%i5) contour_plot (F, [u, -4, 4], [v, -4, 4], [gnuplot_preamble, "set size ratio -1"]);
(%o5) 
(%i6) set_plot_option ([gnuplot_preamble, "set cntrparam levels 12"])$

(%i7) contour_plot (F, [u, -4, 4], [v, -4, 4]);
```

<!-- category: Other -->
<!-- keywords: gnuplot_close -->
<!-- signatures: gnuplot_close() -->
### Function: gnuplot_close ()

Fecha o pipe para o gnuplot que está sendo usado com o formato 
`gnuplot_pipes`.

<!-- category: Other -->
<!-- keywords: gnuplot_replot -->
<!-- signatures: gnuplot_replot(), gnuplot_replot(s) -->
### Function: gnuplot_replot ()

Atualiza a janela gráfica do gnuplot. Se `gnuplot_replot` for chamado com um
comando gnuplot em uma sequência de caracteres *s*, então `s` é enviado para o gnuplot
antes de atualizar a janela.

<!-- category: Other -->
<!-- keywords: gnuplot_reset -->
<!-- signatures: gnuplot_reset() -->
### Function: gnuplot_reset ()

Restaura o estado inicial padrão do gnuplot usado com o formato
`gnuplot_pipes`. Para atualizar a janela do gnuplot chama `gnuplot_replot` após
`gnuplot_reset`.

<!-- category: Other -->
<!-- keywords: gnuplot_restart -->
<!-- signatures: gnuplot_restart() -->
### Function: gnuplot_restart ()

Fecha o pipe para o gnuplot que é usado com o formato 
`gnuplot_pipes` e abre um novo pipe.

<!-- category: Other -->
<!-- keywords: gnuplot_start -->
<!-- signatures: gnuplot_start() -->
### Function: gnuplot_start ()

Abre o pipe para o gnuplot usado para montar um gráfico com o formato
`gnuplot_pipes`. Não é necessário abrir manualmente o
pipe antes de montar o gráfico.

<!-- category: Other -->
<!-- keywords: in_netmath -->
<!-- signatures: in_netmath -->
### Variable: in_netmath

Valor padrão: `false`


Quando `in_netmath` é `true`,
`plot3d` imprime uma saída OpenMath para o console se `plot_format` é `openmath`;
caso contrário `in_netmath` (mesmo se `true`) não tem efeito.
`in_netmath` não tem efeito sobre `plot2d`.

<!-- category: Other -->
<!-- keywords: make_transform -->
<!-- signatures: make_transform(vars, fx, fy, fz) -->
### Function: make_transform (vars, fx, fy, fz)

Retorna uma função adequada para a função transformação em plot3d.  Use
com a opção de montagem de gráfico `transform_xy`.


```maxima
make_transform ([r, th, z], r*cos(th), r*sin(th), z)$
```

é uma transformação para coordenadas polares.

<!-- category: Other -->
<!-- keywords: plot2d -->
<!-- signatures: plot2d(expr, x_range, ..., opções, ...), plot2d([expr_1, ..., expr_n], ..., opções, ...), plot2d([expr_1, ..., expr_n], x_range, ..., opções, ...) -->
### Function: plot2d (expr, x_range, ..., opções, ...)

onde *expr*, *expr_1*, ..., *expr_n* pode ser uma entre
expressões, ou funções do Lisp ou do Maxima ou operadores, ou uma lista com
qualquer das formas: `[discrete, [x1, ..., xn], [y1, ..., yn]]`, `[discrete, [[x1, y1], ..., [xn, ..., yn]]` ou `[parametric, x_expr, y_expr, t_range]`.


Mostra um gráfico de uma ou mais expressões como uma função de uma
variável.


`plot2d` monta o gráfico da expressão *expr* ou muitas expressões
`[name_1, ..., name_n]`. As expressões que não forem
paramétricas ou discretas podem todas depender somente de uma
variável *var* e isso torna obrigatório o uso de *x_range* para
nome daquela variável e fornece seus valores de máximo e de mínimo, usando a
sintaxe: `[variable, min, max]`. O gráfico irá
mostrar o eixo horizontal associado aos valores de *min* e de *max*.


Uma expressão a ser montado o gráfico pode também ser fornecida na forma discreta ou
na forma paramétrica. A saber, como uma lista iniciando-se com a palavra “discrete”
ou a palavra “parametric”. A palavra chave *discrete* deve ser seguida por duas
listas de valores, ambas com o mesmo comprimento, que são as coodenadas horizontais e
as coordenadas verticais de um conjunto de pontos; alternativamente, as coordenadas
de cada ponto pode ser colocada dentro de uma lista com dois valores, e todas as
coordenadas dos pontos podem estar dentro de outra lista. A palavra chave
*parametric* deve ser seguida por douas expressões *x_expr* e
*y_expr*, e um intervalo da forma `[param, min, max]`. As duas expressões devem depender somente do parâmetro
*param*, e o gráfico irá mostrar o caminho percorrido pelo ponto
com coordenadas (*x_expr*, *y_expr*) com *param* variando
de *min* a *max*.


O intervalo do eixo vertical não é obrigatório. É somente mais uma das
opções para o comando, com a sintaxe: `[y, min, max]`. Se aquela opção for usada, o gráfico irá mostrar aquele intervalo
completo, mesmo se a expressão não ocupe todo aquele intervalo. De outra forma,
se um intervalo vertical não for especificado através de `set_plot_option`, as
extremidade do eixo vertical serão encontrada automaticamente.


Todas as outras opções podem também serem listas, iniciando-se com o nome da
opção. A opção *xlabel* pode ser usada para fornecer um ótulo para o
eixo horizontal; se aquela opção não for usada, o eixo horizontal irá
ser rotulado com o nome da variável especificada em *x_range*, ou
com a expressão *x_expr* no caso de apenas uma expressão
paramétrica, ou isso irá ser deichado em branco de outra forma.


Um rótulo para o eixo vertical pode ser fornecido com a opção
*ylabel*. Se existir somente uma expressão a ser montado o gráfico e a
opção *ylabel* não tiver sido usada, o eixo vertical irá ser rotulado com
aquela expressão, a menos que ela seja muito larga, ou com a expressão
*y_expr* se a expressão for paramétrica, ou com o texto
“discrete data” se a expressão for discreta.


As opções `[logx]` e `[logy]` não precisam de quaisquer
parâmetros. Elas irão tornar os eixos horizontal e vertical sejam
escritos em escala logarítmica.


Se houverem muitas expressões para serem montados os gráficos respectivos, uma legenda irá ser
escrita para identificar cada uma das expressões. Os rótulos que podem ser
usados naquela legenda podem ser fornecidos com a opção *legend*. Se a opção *legend*
não for usada, Maxima irá criar rótulos a partir das expressões.


Por padrão, as expressões terão seus gráficos montados como um conjunto de segmentos de reta
saltando pontos adjacentes dentro de um conjunt de pontos que é um dos fornecidos entre
a forma *discrete*, ou calculado automaticamente a partir da expressão
fornecida, usando um algorítmo que automaticamente adapta os passos entre
os pontos usando como uma estimativa inicial do total número de pontos
o conjunto de valores com a opção *nticks*. A opção *style* pode ser
usada para fazer uma das expressões serem representadas como um conjunto de
pontos isolados, ou como pontos e segmentos de reta.


Existem muitas opções globais armazenadas na lsita *plot_options*
que pode ser modificada com a função `set_plot_option`; qualque
daquelas opções globais pode ser sobrescrita com opções fornecidas no
comando *plot2d*.


Uma função a ter seu gráfico montado pode ser especificada como o nome de uma função
do Maxima ou do Lisp ou um operador, uma expressão lambda do Maxima, ou uma expressão
geral do Maxima.  Se especificado como um nome ou uma expressão lambda, a
função deve ser uma função de um argumento.



**Exemplos:**


Gráficos de funções comuns.






```maxima
(%i1) plot2d (sin(x), [x, -%pi, %pi])$
```


![./figures/plotting6](./figures/plotting6.png)





```maxima
(%i1) plot2d (sec(x), [x, -2, 2], [y, -20, 20])$
```


![./figures/plotting7](./figures/plotting7.png)

Montando gráfico de funções pelo nome.









```maxima
(%i1) F(x) := x^2 $

(%i2) :lisp (defun |$g| (x) (m* x x x))
$g

(%i2) H(x) := if x < 0 then x^4 - 1 else 1 - x^5 $
(%i3) plot2d ([F, G, H], [u, -1, 1], [y, -1.5, 1.5])$
```


![./figures/plotting10](./figures/plotting10.png)

Podemos montar o gráfico de um círculo usando um gráfico paramétrico com um parâmetro
*t*. Não é necessário fornecer um intervalo para intervalo horizontal,
uma vez que o intervalo do parâmetro *t* determina o
domínio. Todavia, usaremos a opção 
*same_xy* para obter a mesma escala em ambos os eixos:







```maxima
(%i1) plot2d([[parametric, cos(t), sin(t), [t,0,2*%pi]], -abs(x)],
         [x, -sqrt(2), sqrt(2)], same_xy)$
```


![./figures/plotting12](./figures/plotting12.png)

Exemplo de um gráfico logarítmico:





```maxima
(%i1) plot2d (exp(3*s), [s, -2, 2], logy)$
```


![./figures/plotting9](./figures/plotting9.png)

Exemplo de gráfico discreto, definindo as coordenadas x e y por separado:







```maxima
(%i1) plot2d ([discrete, makelist(i*%pi, i, 1, 5),
                            [0.6, 0.9, 0.2, 1.3, 1]])$
```


![./figures/plotting14](./figures/plotting14.png)

O gráfico de pontos pode ser mostrado juntamente com um gráfico da
função teorética/doutrinária/estética que prevê as coordenads dos pontos:












```maxima
(%i1) xy: [[10, .6], [20, .9], [30, 1.1], [40, 1.3], [50, 1.4]]$

(%i2) plot2d([[discrete, xy], 2*%pi*sqrt(l/980)], [l,0,50],
        [style, points, lines], [color, red, blue],
        [point_type, asterisk],
        [legend, "experiment", "theory"],
        [xlabel, "pendulum's length (cm)"],
        [ylabel, "period (s)"])$
```


![./figures/plotting16](./figures/plotting16.png)

Veja também `plot_options`, que descreve opções de montagem de gráfico e tem mais exemplos.

<!-- category: Other -->
<!-- keywords: plot3d -->
<!-- signatures: plot3d([expr_1, expr_2, expr_3], x_range, y_range, ..., opções, ...), plot3d(expr, x_range, y_range, ..., opções, ...), plot3d(name, x_range, y_range, ..., opções, ...), plot3d([expr_1, expr_2, expr_3], x_rge, y_rge), plot3d([nome_1, nome_2, nome_3], x_range, y_range, ..., opções, ...) -->
### Function: plot3d ([expr_1, expr_2, expr_3], x_range, y_range, ..., opções, ...)

Mostra um gráfico de uma ou três expressões como funções de duas variáveis.







```maxima
(%i1) plot3d (u^2 - v^2, [u, -2, 2], [v, -3, 3], [grid, 100, 100],
        [mesh_lines_color,false])$
```


![./figures/plotting17](./figures/plotting17.png)

monta o gráfico de `u^2-v^2` com `u` e `v` variando no intervalo fechado [-2,2] e
no intervalo fechado de [-3,3] respectivamente, e com *u* sobre o eixo x, e `v` sobre o eixo
y.


Outro exemplo é uma superfície de Klein:










```maxima
(%i1) expr_1: 5*cos(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)-10$
(%i2) expr_2: -5*sin(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)$
(%i3) expr_3: 5*(-sin(x/2)*cos(y)+cos(x/2)*sin(2*y))$

(%i4) plot3d ([expr_1, expr_2, expr_3], [x, -%pi, %pi],
        [y, -%pi, %pi], [grid, 50, 50])$
```


![./figures/plotting21](./figures/plotting21.png)

Algumas vezes isso é necessário para definir uma função para montar o graico da expressão. Todos
os argumentos para plot3d são avaliados antes de serem passados para plot3d. Tentar
fazer um expressão que faz apenas o que é preciso pode ser 
difícil e pode ser mais fácil fazer uma função.   








```maxima
(%i1) M: matrix([1,2,3,4], [1,2,3,2], [1,2,3,4], [1,2,3,3])$
(%i2) f(x, y) := float('M [round(x), round(y)])$

(%i3) plot3d (f(x,y), [x,1,4],[y,1,4],[grid,3,3],[legend,false])$
```


![./figures/plotting25](./figures/plotting25.png)

Veja `plot_options` para mais exemplos.

<!-- category: Other -->
<!-- keywords: plot_options -->
<!-- signatures: plot_options -->
### Variable: plot_options

Elementos dessa lista estabelecem as opções padrão para a montagem do gráfico.
Se uma opção está presente em uma chamada a `plot2d` ou `plot3d`,
esse valor tem precedência sobre a opção padrão.
De outra forma, o valor em `plot_options` é usado.
Opções padrão são atribuídas por `set_plot_option`.


Cada elemento de `plot_options` é uma lista de dois ou mais ítens.
O primeiro item é o nome de uma opção, e os restantes compreendem o valor ou valores
atribuídos à opção.
Em alguns casos, o valor atribuído é uma lista, que pode compreender muitos ítens.


As opções de montagem de gráfico que são reconhecidas por `plot2d` e `plot3d` são as seguintes:



- *
Opção: `plot_format`

Determina qual interface gráfica é usada por `plot2d` e por
`plot3d`.

  - *
Valor: `gnuplot` padrão para windows
Gnuplot é o mais avançado pacote de montagem de gráficos entre os pacotes
disponíveis no Maxima. Esse valor requer uma instalação externa do gnuplot.
  - *
Valor: `gnuplot_pipes` padrão nas plantaformas não windows
Similar ao formato `gnuplot` exceto que a comunicação com o
gnuplot é realizada através de um pipe. Esse valor pode ser usado para montar um gráfico na tela,
para redirecionar a saída do gráfico para um arquivos é melhor usar o formato `gnuplot`.
  - *
Valor: `mgnuplot`
Mgnuplot é um ambiente montado em volta do gnuplot baseado no Tk.  Esse ambiente está incluído na
distribuíção do Maxima.  Mgnuplot oferece uma GUI rudimentar para o gnuplot,
mas tem menos recursos em geral que a interface plana do
gnuplot.  Mgnuplot requer uma instalação externa do gnuplot e
Tcl/Tk.
  - *
Valor: `openmath`
Openmath é um programa gráfico escrito em Tcl/Tk. Este formato é fornecido pelo pacote
Xmaxima, que é distribuído junto com Maxima; com o objetivo de usar esse
formato você pode instalar o pacote Xmaxima, e o Openmath irá trabalhar não somente
a partir do Xmaxima em si mesmo, mas também a apartir da linha de comando e outras GUI’s para
o Maxima.
- *
Opção: `run_viewer`

Controla se o visualizador apropriado para o formato da montagem do gráfico pode ou não
ser executado.

  - *
Valor padrão: `true`
 
Executa o programa visualizador.
  - *
Valor: `false`
Não executa o programa visualizador.
- *
Opção: `y`

O intervalo vertical do gráfico.

Exemplo:

```maxima
[y, - 3, 3]
```
Especifica intervalo vertical para [-3, 3].
- *
Opção: `plot_realpart`

Quando `plot_realpart` for `true`,
a parte real de um valor complexo *x* é mostrada;
isso é equivalente a mostrar `realpart(x)` em lugar de *x*.
De outra forma,
somente valores com a parte imaginária igual a 0 são mostrados na tela,
e valores complexos são ignorados.

Exemplo:

```maxima
plot2d (log(x), [x, -5, 5], [plot_realpart, false]);
plot2d (log(x), [x, -5, 5], [plot_realpart, true]);
```
O valor padrão é `false`.
- *
Opção: `nticks`

Em plot2d, essa opção é fornece o número inicial de pontos usado pela
rotina adaptativa de montagem de gráficos para funções de montagem de gráfico. Ess número inicial de pontos é também
o número de pontos que isrá ser mostrado em um gráfico paramétrico.

Exemplo:

```maxima
[nticks, 20]
```
O padrão para `nticks` é 10.
- *
Opção: `adapt_depth`

O número maximo de quebras usada pela rotina adaptativa de montagem do gráfico.

Exemplo:

```maxima
[adapt_depth, 5]
```
O padrão para `adapt_depth` é 10.
- *
Opção: `xlabel`

O rótulo para o eixo horizontal em um gráfico bidimensional.

Exemplo:

```maxima
[xlabel, "Time in seconds"]
```
- *
Opção: `ylabel`

O rótulo do eixo vertical em gráficos bidimensionais.

Exemplo:

```maxima
[ylabel, "Temperatura"]
```
- *
Opção: `logx`

Essa opção faz com que o eixo horizontal de um gráfico bidimensional seja desenhado
em proporção logarítmica. Essa opção não precisa de quaisquer parâmetros adicionais.
- *
Opção: `logy`

Essa opção faz com que o eixo vertical de um gráfico bidimensional seja desenhado
em proporção logarítmica. Essa opção não precisa de quaisquer parâmetros adicionais.
- *
Opção: `legend`

Os rótulos para várias expressões em um gráfico bidimensional com muitas
expressões. Se houverem mais expressões que o número de rótulos
fornecidos, eles irão ser repetidos. Por padrão, os nomes das expressões
ou funçõe irão ser usados, ou as palavras discrete1, discrete2, ..., para
conjuntos discretos de pontos.

Exemplo:

```maxima
[legend, "Conj 1", "Conj 2", "Conj 3"]
```
- *
Opção: `style`

Os estilos que irão ser usados para várias funções ou conjuntos de dados
em um gráfico bidimensional. A palavra *style* deve ser seguida por um ou mais
estilos. Se houverem mais funções e conjuntos de pontos que estilos
fornecidos, os estilos irão ser repetidos. Cada estilo pode ser um entre os seguintes
*lines* para segmentos de reta, *points* para pontos isolados,
*linespoints* para segmentos e pontos, ou *dots* para pequenos
pontos isolados. Gnuplot aceita também o estilo *impulses*.

Cada um dos estilos pode também ser fechado dentro de uma lista com alguns parâmetros
adicionais. *lines* aceita um ou dois números: a largura da
linha e um inteiro que identifica uma cor. *points* aceita um ou
dois parâmetros; o primeiro parâmetro é o raio dos pontos e
o segundo parâmetro é um inteiro que para o Gnuplot seleciona diferentes
ajustes e cores para os ponots e em Openmath modifica a cor
usada para os pontos. *linesdots* aceita até quatro parâmetros;
os primerios dois possuem o mesmo significado que em *lines* e os últimos dois possuem o mesmo
significado que em *points*.

Exemplo:

```maxima
[style,[lines,2,3],[points,1,4]]
```

No Gnuplot, esse exemplo irá montar o gráfico da primeira (e terceira, quinta, etc)
expressão com segmentos de retas azuis de largura 2, ea segunda (e
quarta, sexta, etc) expressão com quadrados verdes de tamanho 1. No
Openmath, a primeira expressão irá ser mostrada com segmentos da cor magenta de
largura 2, e o segundo com pontos alaranjados de raio 1; note que
openmath_color(3) openmath_color(4) retornam “magenta” e
“orange” (alaranjado).

O padrão para a opção de estilo é *lines* com largura 1, e
diferentes cores.
- *
Opção: `grid`

Escolhe o número de pontos da grade para usar nas direções x e y
para montagem de gráficos tridimensionais.

Exemplo:

```maxima
[grid, 50, 50]
```
Escolhe a grade para 50 por 50 pontos.  A grade padrão é 30 por 30.
- *
Opção: `transform_xy`

Permite que transformações sejam aplicadas à montagem de gráficos tridimensionais.

Exemplo:

```maxima
[transform_xy, false]
```
O valor padrão de `transform_xy` é `false`.  Se o valor padrão de `transform_xy` não é `false`, pode ser
a saída de

```maxima
make_transform ([x, y, z], f1(x, y, z), f2(x, y, z), f3(x, y, z))$
```
A transformação `polar_xy` é previamente definida no Maxima.  Isso fornece a mesma
transformação que

```maxima
make_transform ([r, th, z], r*cos(th), r*sin(th), z)$
```


**Opções do Gnuplot:**


Existem muitas opções de montagem de gráfico específicas para gnuplot.  Algumas dessas
opções são naturais do gnuplot, especificados como sequências de caracteres. Consulte a
documentação do gnuplot para mais detalhes.



- *
Opção: `gnuplot_term`

Escolhe a saída para o tipo terminal para o gnuplot.

  - *
Valor padrão: `default`
A saída do Gnuplot é mostrada em uma janela gráfica separada.
  - *
Valor: `dumb`
A sída do Gnuplot é mostrada no console do Maxima por meio de uma "concepção artística em ASCII" aproximada para gráficos.
  - *
Valor: `ps`
Gnuplot gera comandos na linguagem PostScript de descrição de página.
Se a opção
`gnuplot_out_file` for escolhida para *nomearquivo*, gnuplot escreve os comandos PostScript em *nomearquivo*.
De outra forma, Esse arquivo é salvo com o nome `maxplot.ps`.
  - *
Valor: qualquer outra especificação válida do terminal `term` do gnuplot
Gnuplot pode gerar saídas em muitos outros formatos gráficos tais
como png, jpeg, svg etc.  Paa criar gráficos em todos esses formatos a opção
`gnuplot_term` pode ser escolhida para qualquer terminalsuportado pelo gnuplot (símbolo)
ou mesmo especificação completa de terminal do gnuplot com quaisquer opções (sequência de caracteres).
Por exemplo `[gnuplot_term,png]` cria saídas no formato PNG (Portable
+Network Graphics) enquanto `[gnuplot_term,"png size 1000,1000"]`
cria PNG de tamanho 1000x1000 pixels. 
Se a opção `gnuplot_out_file` for escolhida para *nomearquivo*, gnuplot 
escreve a saída para *nomearquivo*. De outra forma, esse arquivo é gravado com o nome de
`maxplot.term`, onde *term* é o nome do terminal do
gnuplot .
- *
Opção: `gnuplot_out_file`

Escreve a saída do gnuplot para um arquivo.

  - *
Valor padrão: `false`
Nenhum arquivo de saída especificado.
  - *
Valor: *nomearquivo*
Exemplo: `[gnuplot_out_file, "meugrafico.ps"]`
Esse exemplo envia a saída PostScript para o arquivo `meugrafico.ps` quando
usada conjuntamente com o terminal PostScript do gnuplot.
- *
Opção: `gnuplot_pm3d`

Controla o uso do modo PM3D, que tem recursos
avançados em 3D.  PM3D está somente disponível no gnuplot em versões após a 3.7.  O
valor padrão para `gnuplot_pm3d` é `false`.

Exemplo:

```maxima
[gnuplot_pm3d, true]
```
- *
Opção: `gnuplot_preamble` 

Insere comandos antes que o gráfico seja
desenhado.  Quaisquer comandos válidos para o gnuplot podem ser usados.  Multiplos comandos
podem ser separados com um ponto e vírgula.  O exemplo mostrado produz uma
escala numérica na montagem do gráfico.  O valor padrão para `gnuplot_preamble` é uma sequência de caracteres vazia `""`.

Exemplo:

```maxima
[gnuplot_preamble, "set log y"]
```
- *
Opção: `gnuplot_curve_titles`

Controla os títulos dados na chave da montagem do gráfico.  O
valor padrão é `[default]`, que automaticamente escolhe o título de cada
curva para a função cujo gráfico está sendo construído. Se não contiver `[default]`, `gnuplot_curve_titles`
pode conter uma lista de sequências de caracteres,
cada uma das quais é `"title 'title_string'"`.
(Para disabilitar a chave de impressão de gráfico, adicione `"set nokey"` a `gnuplot_preamble`.)

Exemplo:

```maxima
[gnuplot_curve_titles,
["title 'Minha primeira função'", "title 'Minha segunda função'"]]
```
- *
Opção: `gnuplot_curve_styles`

Uma lista de sequências de caracteres controlando a aparência
das curvas, i.e., cor, largura, brilho, etc., para serem enviadas para o
comando de montagem do gráfico do gnuplot.  O valor padrão é
`["with lines 3", "with lines 1", "with lines 2", "with lines 5", "with lines 4", "with lines 6", "with lines 7"]`, que circula através de diferentes cores.  Veja a
documentação do gnuplot de `plot` para maiores informações.

Exemplo:

```maxima
[gnuplot_curve_styles, ["with lines 7", "with lines 2"]]
```
- *
Opção: `gnuplot_default_term_command`

O comando gnuplot para escolher o
tipo de terminal para o terminal padrão. O valor padrão é `set term windows "Verdana" 15` em sistemas windows, e `set term x11 font "Helvetica,16"` em sistemas de janelas do X11.
 
Exemplo:

```maxima
[gnuplot_default_term_command, "set term x11"]
```
- *
Opção: `gnuplot_dumb_term_command`

O comando gnuplot para escolher o
tipo de terminal para o terminal dumb.  O valor padrão é `"set term dumb 79 22"`,
que faz a saída texto com 79 caracteres por 22
caracteres.

Exemplo:

```maxima
[gnuplot_dumb_term_command, "set term dumb 132 50"]
```
- *
Opção: `gnuplot_ps_term_command`

O comando gnuplot para escolher o tipo
de terminal para o terminal PostScript.  O valor padrão é 
`"set size 1.5, 1.5;set term postscript eps enhanced color solid 24"`,
que escolhe o
tamanho para 1.5 vezes o padrão do gnuplot, e o tamanho da fonte para 24, além de
outras coisas.  Veja a documentação do gnuplot de `set term postscript` para mais informação.

Exemplo:

Todos os números nos exemplos para a função *plot2d* nesse
manual foram obtidos de arquivos Postscript que foram gerados após
escolher `gnuplot_ps_term_command` como:

```maxima
[gnuplot_ps_term_command,
"set size 1.3, 1.3; set term postscript eps color solid lw 2.5 30"]
```

<!-- category: Other -->
<!-- keywords: set_plot_option -->
<!-- signatures: set_plot_option(opção) -->
### Function: set_plot_option (opção)

Atribui uma das varáveis globais para impressão.
*opção* é especificada como uma lista de dois ou mais elementos,
na qual o primeiro elemento é uma das palavras chave
dentro da lista `plot_options`.


`set_plot_option` avalia seu argumento e
retorna a liasta completa `plot_options`
(após modificar um de seus elementos).


Veja também `plot_options`, `plot2d`, e `plot3d`.


Exemplos:


Modifica a malha (`grid`) e valores de `x`.
Quando uma palavra chave em `plot_options` tem um valor atribuído,
colocar um apóstrofo evita avaliação.









```maxima
(%i1) set_plot_option ([grid, 30, 40]);
(%o1) [[x, - 1.755559702014E+305, 1.755559702014E+305], 
[y, - 1.755559702014E+305, 1.755559702014E+305], [t, - 3, 3], 
[grid, 30, 40], [transform_xy, false], [run_viewer, true], 
[plot_format, gnuplot], [gnuplot_term, default], 
[gnuplot_out_file, false], [nticks, 10], [adapt_depth, 10], 
[gnuplot_pm3d, false], [gnuplot_preamble, ], 
[gnuplot_curve_titles, [default]], 
[gnuplot_curve_styles, [with lines 3, with lines 1, 
with lines 2, with lines 5, with lines 4, with lines 6, 
with lines 7]], [gnuplot_default_term_command, ], 
[gnuplot_dumb_term_command, set term dumb 79 22], 
[gnuplot_ps_term_command, set size 1.5, 1.5;set term postscript #
eps enhanced color solid 24]]
(%i2) x: 42;
(%o2)                          42
(%i3) set_plot_option (['x, -100, 100]);
(%o3) [[x, - 100.0, 100.0], [y, - 1.755559702014E+305, 
1.755559702014E+305], [t, - 3, 3], [grid, 30, 40], 
[transform_xy, false], [run_viewer, true], 
[plot_format, gnuplot], [gnuplot_term, default], 
[gnuplot_out_file, false], [nticks, 10], [adapt_depth, 10], 
[gnuplot_pm3d, false], [gnuplot_preamble, ], 
[gnuplot_curve_titles, [default]], 
[gnuplot_curve_styles, [with lines 3, with lines 1, 
with lines 2, with lines 5, with lines 4, with lines 6, 
with lines 7]], [gnuplot_default_term_command, ], 
[gnuplot_dumb_term_command, set term dumb 79 22], 
[gnuplot_ps_term_command, set size 1.5, 1.5;set term postscript #
eps enhanced color solid 24]]
```

