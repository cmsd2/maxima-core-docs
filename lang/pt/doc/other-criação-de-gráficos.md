## Criação de Gráficos

<!-- category: Other -->
<!-- keywords: in_netmath -->
<!-- signatures: in_netmath -->
### Variable: in_netmath

Valor por omissão: `false`


Quando `in_netmath` é `true`, `plot3d` imprime uma
saída OpenMath para a consola se `plot_format` é
`openmath`; caso contrário `in_netmath` (mesmo se for
`true`) não tem efeito. `in_netmath` não tem efeito
sobre `plot2d`.

<!-- category: Other -->
<!-- keywords: make_transform -->
<!-- signatures: make_transform(vars, fx, fy, fz) -->
### Function: make_transform (vars, fx, fy, fz)

Produz uma função adequada para a função
transformação em plot3d. Usa-se conjuntamente com a opção
gráfica `transform_xy`.


```maxima
make_transform ([r, th, z], r*cos(th), r*sin(th), z)$
```

é uma transformação para coordenadas polares.

<!-- category: Other -->
<!-- keywords: plot2d -->
<!-- signatures: plot2d(expr, intervalo_x, ..., opções, ...), plot2d([expr_1, ..., expr_n], ..., opções, ...), plot2d([expr_1, ..., expr_n], intervalo_x, ..., opções, ...) -->
### Function: plot2d (expr, intervalo_x, ..., opções, ...)

Onde *expr*, *expr_1*, ..., *expr_n* podem ser
expressões, funções ou operadores do Maxima ou do Lisp, ou ainda
uma lista da forma `[discrete, [x1, ..., xn], [y1, ..., yn]]`, `[discrete, [[x1, y1], ..., [xn, ..., yn]]` ou `[parametric, expr_x, expr_y, intervalo_t]`.


Mostra o gráfico de uma ou mais expressões em função de uma
variável.


`plot2d` produz o gráfico de uma expressão *expr* ou de
várias expressões `[expr_1, ..., expr_n]`. As
expressões que não forem do tipo paramétrico ou discreto, deverão
depender todas de uma única variável *var* e será
obrigatório usar *intervalo_x* para indicar o nome dessa
variável, e os seus valores mínimo e máximo, usando a
sintaxe: `[var, min, max]`. O gráfico
mostrará o eixo horizontal delimitado pelos valores *min* e
*max*.


Uma expressão a ser representada no gráfico pode ser dada também
na forma discreta, ou paramétrica. Nomeadamente, por meio de uma lista
a começar pela palavra “discrete” ou “parametric”. A palavra
chave *discrete* deverá ir seguida por duas listas, ambas do mesmo
comprimento, que serão as coordenadas horizontais e verticais de um
conjunto de pontos; em alternativa, as coordenadas de cada ponto podem
ser colocadas numa lista de dois valores, e todas essas coordenadas
deverão estar dentro de outra lista. A palavra chave *parametric*
deverá ir seguida por duas expressões *expr_x* e *expr_y*, e
um intervalo *intervalo_t* da forma `[param, min, max]`. As duas expressões deverão depender unicamente no
parâmetro *param*, e o gráfico mostrará o percurso seguido
pelo ponto com coordenadas (*expr_x*, *expr_y*) à medida que
*param* aumenta desde *min* até *max*.


O intervalo de valores no eixo vertical não é obrigatório. É
mais uma das opções do comando, com a sintaxe: `[y, min, max]`. Se essa opção for usada, o gráfico
apresentará esse intervalo completo, inclusivamente quando as
expressões não cheguem a atingir esses valores. De outra forma, se
não for indicado um intervalo no eixo vertical por meio de
`set_plot_option`, as fronteiras do eixo vertical serão
seleccionadas automaticamente.


Todas as outras opções deverão ser listas, a começar pelo
nome da opção. A opção *xlabel* pode ser usada para dar
um texto que identificará o eixo horizontal; se essa opção não for
usada, o eixo será identificado com o nome da variável indicada em
*intervalo_x*, ou com a expressão *expr_x*, se houver
unicamente uma expressão paramétrica, ou caso contrário ficará
em branco.


O texto para identificar o eixo vertical pode ser indicado com a
opção *ylabel*. Se só houver uma única expressão a ser
representada, e a opção *ylabel* não tiver sido usada, o
eixo vertical será identificado com essa expressão, a menos que for
muito comprido, ou com a expressão *expr_y*, se a expressão for
paramétrica, ou com o texto “discrete data” se a expressão for
discreta.


As opções *logx* e *logy* não precisam de quaisquer
paraâmetros. Fazem com que os eixos horizontal e vertical sejam
apresentados em forma logarítmica.


Se houver vá rias expressões a serem representadas, será escrita
uma legenda para identificar cada uma dessas expressões. O texto que
deverá ser usado nessa legenda pode ser indicado por meio da
opção *legend*. Se essa opção não for usada, Maxima
criará textos para identificar cada expressão.


Por omissão, as expressões dadas serão representadas por pequenos
segmentos de recta a ligarem pontos adjacentes num conjunto de pontos
que, ou é dado usando a forma *discrete*, ou é calculado
automaticamente a partir das expressões dadas, por meio de um
algoritmo com ajuste automático dos intervalos entre pontos, usando
como estimativa inicial do número de pontos o valor indicado pela
opção *nticks*. A opção *style* serve para fazer com
que alguma das expressões seja representada por pontos isolados ou por
pontos mais segmentos de recta.

 

Existem várias opções globais, armazenadas na lista
*plot_options*, quu podem ser modificadas usando a função
`set_plot_option`; qualquer uma dessad opções pode ser
contrariada pelos valores locais dados no comando *plot2d*.


Uma função a ser representada poderá ser identificada pelo nome
de uma função ou operador do Maxima ou do Lisp, por meio duma
expressão lambda do Maxima, ou como uma expressão geral do Maxima.
Se for especificada como um nome ou como expressão lambda, a
respectiva função deverá depender dum único argumento.


**Exemplos:**


Gráfico de uma função explícita.






```maxima
(%i1) plot2d (sin(x), [x, -%pi, %pi])$
```


![plotting6](figures/plotting6.png)


Se a função aumenta rapidamente, é útil limitar os valores no eixo vertical:






```maxima
(%i1) plot2d (sec(x), [x, -2, 2], [y, -20, 20])$
plot2d: some values were clipped.
```


![plotting7](figures/plotting7.png)


Gráfico com escala logarítmica:






```maxima
(%i1) plot2d (exp(3*s), [s, -2, 2], [logy])$
```


![plotting9](figures/plotting9.png)


Várias formas de indicar as funções a serem traçadas no gráfico:









```maxima
(%i1) F(x) := x^2 $

(%i2) :lisp (defun |$g| (x) (m* x x x))
$g

(%i2) H(x) := if x < 0 then x^4 - 1 else 1 - x^5 $
(%i3) plot2d ([F, G, H], [u, -1, 1], [y, -1.5, 1.5])$
```


![plotting10](figures/plotting10.png)


Exemplo de função paramétrica. Curva da borboleta:








```maxima
(%i1) r: (exp(cos(t))-2*cos(4*t)-sin(t/12)^5)$
(%i2) plot2d([parametric, r*sin(t), r*cos(t), 
             [t, -8*%pi, 8*%pi]])$
```


![plotting11](figures/plotting11.png)


Gráfico de uma circunferência de raio 1, com centro na origem, junto com
a função `y=-|x|`. Para que a circunferência não pareça
uma elipse, usa-se a opção `same_xy` para que a escala seja a mesma
nos dois eixos. Mostra-se também o uso da opção `nolegend` para
eliminar a legenda que identifica as duas funções.







```maxima
(%i1) plot2d([x^2+y^2=1, -abs(x)], [x, -1.5, 1.5], [y, -2, 2], same_xy,
             nolegend);
```


![plotting12](figures/plotting12.png)


Pontos discretos, indicando as coordenadas x e y por separado:







```maxima
(%i1) plot2d ([discrete, makelist(i*%pi, i, 1, 5),
                            [0.6, 0.9, 0.2, 1.3, 1]])$
```


![plotting14](figures/plotting14.png)



Gráfico de 200 pontos aleatórios entre 0 e 9:






```maxima
(%i1) plot2d ([discrete, makelist ( random(10), 200)])$
```


![plotting13](figures/plotting13.png)


Neste exemplo, guarda-se uma tabela de três colunas no
ficheiro `data.txt`, que é logo lido para representar as duas últimas
colunas num gráfico:











```maxima
(%i1) display2d:false$
(%i2) with_stdout ("data.txt", for x:0 thru 10 do
                             print (x, x^2, x^3))$
(%i3) data: read_matrix ("data.txt")$
(%i4) plot2d ([discrete, transpose(data)[2], transpose(data)[3]],
  [style,points], [point_type,diamond], [color,red])$
```


![plotting15](figures/plotting15.png)


Um gráfico de dados experimentais junto com o seu modelo teórico:












```maxima
(%i1) xy: [[10, .6], [20, .9], [30, 1.1], [40, 1.3], [50, 1.4]]$
(%i2) plot2d([[discrete, xy], 2*%pi*sqrt(l/980)], [l,0,50],
        [style, points, lines], [color, red, blue],
        [point_type, asterisk],
        [legend, "experiment", "theory"],
        [xlabel, "pendulum's length (cm)"],
        [ylabel, "period (s)"])$
```


![plotting16](figures/plotting16.png)

<!-- category: Other -->
<!-- keywords: plot3d -->
<!-- signatures: plot3d([expr_1, expr_2, expr_3], x_range, y_range, ..., opções, ...), plot3d(expr, x_range, y_range, ..., opções, ...), plot3d(name, x_range, y_range, ..., opções, ...), plot3d([expr_1, expr_2, expr_3], x_rge, y_rge), plot3d([nome_1, nome_2, nome_3], x_range, y_range, ..., opções, ...) -->
### Function: plot3d ([expr_1, expr_2, expr_3], x_range, y_range, ..., opções, ...)

Mostra uma ou mais superfícies definidas como funções de duas variáveis, ou
de forma paramétrica.


As funções a serem representadas podem ser definidas por expressões ou por
nomes de funções. Pode usar-se o rato para rodar o gráfico, podendo observar
as superfícies desde diferente ângulos.


Exemplos:


Gráfico de uma função de duas variáveis:







```maxima
(%i1) plot3d (u^2 - v^2, [u, -2, 2], [v, -3, 3], [grid, 100, 100],
        nomesh_lines)$
```


![plotting17](figures/plotting17.png)


Uso da opção z para limitar um função que se aproxima de infinito
(neste caso, a função aproxima-se de mais ou menos infinito nos eixos
x e y):







```maxima
(%i1) plot3d ( log ( x^2*y^2 ), [x, -2, 2], [y, -2, 2], [z, -8, 4],
         nopalette, [color, magenta])$
```


![plotting18](figures/plotting18.png)


Os valores infinitos de z podem também ser evitados usando uma
gralha que não coincida com os pontos onde a função fica infinita.
Este exemplo mostra também como modificar a paleta de cores e como
incluir uma barra lateral que mostra a correspondência entre cores
e valores de z:









```maxima
(%i1) plot3d (log (x^2*y^2), [x, -2, 2], [y, -2, 2],[grid, 29, 29],
       [palette, [gradient, red, orange, yellow, green]],
       color_bar, [xtics, 1], [ytics, 1], [ztics, 4],
       [color_bar_tics, 4])$
```


![plotting19](figures/plotting19.png)


Duas superfícies num mesmo gráfico. Se os domínios das duas superfícies
forem diferentes, as duas funções deverão ser colocadas em listas separadas,
cada uma com o seu próprio domínio. O domínio por fora dessas listas
define o domínio para todo o gráfico.








```maxima
(%i1) plot3d ([[-3*x - y, [x, -2, 2], [y, -2, 2]],
   4*sin(3*(x^2 + y^2))/(x^2 + y^2), [x, -3, 3], [y, -3, 3]],
   [x, -4, 4], [y, -4, 4])$
```


![plotting20](figures/plotting20.png)


A garrafa de Klein, definida parametricamente:










```maxima
(%i1) expr_1: 5*cos(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)-10$
(%i2) expr_2: -5*sin(x)*(cos(x/2)*cos(y)+sin(x/2)*sin(2*y)+3)$
(%i3) expr_3: 5*(-sin(x/2)*cos(y)+cos(x/2)*sin(2*y))$
(%i4) plot3d ([expr_1, expr_2, expr_3], [x, -%pi, %pi],
        [y, -%pi, %pi], [grid, 50, 50])$
```


![plotting21](figures/plotting21.png)


Gráfico dum harmônico esférico, utilizando a transformação
predefinida `spherical_to_xyz`:







```maxima
(%i1) plot3d (sin(2*theta)*cos(phi), [theta,0,%pi], [phi,0,2*%pi],
      [transform_xy, spherical_to_xyz], [grid, 30, 60], nolegend)$
```


![plotting22](figures/plotting22.png)


Uso da transformação predefinida `polar_to_xy` para transformar
coordenadas cilíndricas para retangulares. Este exemplo mostra também
como eliminar os eixos e a legenda:







```maxima
(%i1) plot3d (r^.33*cos(th/3), [r,0,1], [th,0,6*%pi], nobox,
    nolegend, [grid, 12, 80], [transform_xy, polar_to_xy])$
```


![plotting23](figures/plotting23.png)


Desenho de uma esfera utilizando a transformação de coordenadas esféricas
para retangulares. A opção `same_xyz` é usada para que a escala
dos três eixos seja a mesma, evitando que a esfera apareça como elipsoide.
Quando sejam usadas transformações, não convém eliminar as linhas sobre
a superfície, para evitar erros de Gnuplot.








```maxima
(%i1) plot3d ( 5, [theta,0,%pi], [phi,0,2*%pi], same_xyz, nolegend,
  [transform_xy, spherical_to_xyz], [mesh_lines_color,blue],
  [palette,[gradient,"#1b1b4e", "#8c8cf8"]])$
```


![plotting24](figures/plotting24.png)


Definição de uma função de duas variáveis usando os valores de uma
matriz. Note-se o uso do apóstrofe na definição da função para evitar
que `plot3d` falhe ao detetar que os índices da matriz devem
ser enteros:








```maxima
(%i1) M: matrix([1,2,3,4], [1,2,3,2], [1,2,3,4], [1,2,3,3])$
(%i2) f(x, y) := float('M [round(x), round(y)])$
(%i3) plot3d (f(x,y), [x,1,4], [y,1,4], [grid,3,3], nolegend)$
```


![plotting25](figures/plotting25.png)


Atribuindo o valor zero à opção `elevation`, uma superfície pode ser
visualizada como um mapa em que diferentes cores representam diferentes
valores.








```maxima
(%i1) plot3d (cos (-x^2 + y^3/4), [x,-4,4], [y,-4,4], [zlabel,""],
       [mesh_lines_color,false], [elevation,0], [azimuth,0],
       color_bar, [grid,80,80], noztics, [color_bar_tics,1])$
```


![plotting26](figures/plotting26.png)


Veja também `plot_options`, que descreve as opções das
funções gráficas e mostra mais exemplos.

<!-- category: Other -->
<!-- keywords: plot_options -->
<!-- signatures: plot_options -->
### Variable: plot_options

Os elementos desta lista estabelecem os valores por omissaão para as
opções usadas na elaboração de gráficos. Se uma
opção estiver presente numa chamada a `plot2d` ou
`plot3d`, esse valor terá precedência sobre o valor por
omissção. De outra forma, será usado o valor em
`plot_options`. Os valores por omissção das opções
podem ser modificados usando `set_plot_option`.


Cada elemento de `plot_options` é uma lista de dois ou mais
ítens.  O primeiro item é o nome de uma opção, e
os restantes compreendem o valor ou valores atribuídos
à opção.  Em alguns casos, o valor atribuído é
uma lista, que pode compreender muitos itens.


As opções globais que são reconhecidas por `plot2d` e
`plot3d` são as seguintes:



- *
Opção: `plot_format`

Determina a interface gráfica que será usada por `plot2d` e
`plot3d`.

  - *
Valor por omissão: `gnuplot`
Gnuplot é o pacote gráfico mais avançado entre os
disponíveis no Maxima. Será preciso que o pacote externo
gnuplot esteja instalado.
  - *
Valor: `mgnuplot`
Mgnuplot é uma interface Tk para o gnuplot. Vem incluída
na distribuíção do Maxima. Mgnuplot oferece uma GUI
rudimentar para o gnuplot, mas tem menos recursos em geral que a
interface padrão do gnuplot.  Mgnuplot precisa que os pacotes externos
gnuplot e Tcl/Tk estejam instalados.
  - *
Valor: `openmath`
Openmath é um programa gráfico escrito em Tcl/Tk. Este formato é
fornecido pelo pacote Xmaxima, que é distribuido com Maxima. Se quiser
usar este formato instalar o pacote Xmaxima, que funcionará não só
a partir do próprio Xmaxima mas também a partir da linha de comandos
de outras GUI para o Maxima.
- *
Opção: `run_viewer`

Controla se será executado ou não o visualizador apropriado para o
formato do gráfico.

  - *
Valor por omissão: `true`
Executa-se o programa visualizador.
  - *
Valor: `false`
Não se executa o programa visualizador.
- *
Opção: `y`

O intervalo vertical do gráfico.

Exemplo:

```maxima
[y, - 3, 3]
```
Faz com que o intervalo vertical seja [-3, 3].
- *
Opção: `plot_realpart`

Quando `plot_realpart` for `true`, nos pontos onde o valor a
ser representado no eixo vertical for complexo, será apresentada a
sua parte real *x*; isso é equivalente a mostrar
`realpart(x)` em lugar de *x*. De outra forma, somente
valores com a parte imaginária igual a 0 são mostrados no
gráfico, e os valores complexos serão ignorados.

Exemplo:

```maxima
plot2d (log(x), [x, -5, 5], [plot_realpart, false]);
plot2d (log(x), [x, -5, 5], [plot_realpart, true]);
```
O valor por omissão é `false`.
- *
Opção: `nticks`

No plot2d, é o número de pontos usados, inicialmente, pela rotina
gráfica adaptativa. É também o número de pontos que serão
apresentados num gráfico paramétrico.

Exemplo:

```maxima
[nticks, 20]
```
O valor por omissão para `nticks` é 10.
- *
Opção: `adapt_depth`

O número maximo de subdivisões usadas pela rotina gráfica adaptativa.

Exemplo:

```maxima
[adapt_depth, 5]
```
O valor por omissão para `adapt_depth` é 10.
- *
Opção: `xlabel`

O texto que identifica o eixo horizontal num gráfico a 2d.

Exemplo:

```maxima
[xlabel, "Tempo em segundos"]
```
- *
Opção: `ylabel`

O texto que identifica o eixo vertical num gráfico a 2d.

Exemplo:

```maxima
[ylabel, "Temperatura"]
```
- *
Opção: `logx`

Faz com que o eixo horizontal num gráfico a 2d seja representado em
escala logarítmica. Não precisa de nenhum parâmetro
adicional.
- *
Opção: `logy`

Faz com que o eixo vertical num gráfico a 2d seja representado em
escala logarítmica. Não precisa de nenhum parâmetro
adicional.
- *
Opção: `legend`

Os textos para identificar as diversas expressões num gráfico a 2d
com muitas expressões. Se existirem mais expressões do que os textos
dados, serão repetidos. Por omissão, seraão usados os nomes das
expressões ou das funções, ou as palavras discrete1, discrete2,
..., no caso de conjuntos discretos de pontos.

Exemplo:

```maxima
[legend, "Grupo 1", "Grupo 2", "Grupo 3"]
```
- *
Opção: `style`

Os estilos que serão usados para as diversas funções ou
conjuntos discretos de pontos, num gráfico a 2d. A palavra *style*
deverá ir seguida por um ou mais estilos. Se houver mais funções
e conjuntos de dados do que os estilos definidos, serão repetidos
estilos. Cada estilo poderá ser *lines* para segmentos de recta,
*points* para pontos isolados, *linespoints* para segmentos e
pontos, ou *dots* para pequenos pontos isolados. O Gnuplot também
aceita o estilo *impulses*.

Cada um dos estilos poderá ser incorporado numa lista, seguido de
alguns parâmetros adicionais. *lines* admite um ou dois números:
a largura da linha e um inteiro que identifica uma cor. *points*
admite um ou dois números; o primeiro número é o raio dos pontos,
e o segundo número é um inteiro que no Gnuplot permite seleccionar
diferentes formas e cores para os pontos e no Openmath muda a cor dos
pontos usados. *linesdots* admite até quatro números; os dois
primeiros são os mesmos do que para *lines* e os dois últimos
são os mesmos do que para *points*.

Exemplo:

```maxima
[style,[lines,2,3],[points,1,4]]
```

No Gnuplot, isso faz com que a primeira (e terceira, quinta, etc)
expressão seja apresentada com segmentos de recta azuis de largura 2,
e a segunda (quarta, sexta, etc) expressão com quadrados verdes de
tamanho 1. No Openmath, a primeira expressão será apresentada com
rectas magenta de largura 2, e a segunda com pontos laranja de raio 1;
repare que openmath_color(3) e openmath_color(4) produzem “magenta” e
“orange”.

O estilo por omissão é segmentos de recta, com largura 1, e com
diferentes cores.
- *
Opção: `grid`

Define o número de pontos nas direções x e y, na grelha usada nos
gráficos tridimensionais.

Exemplo:

```maxima
[grid, 50, 50]
```
Define uma grelha de 50 por 50 pontos. A grelha padrão é 30 por 30.
- *
Opção: `transform_xy`

Permite a aplicação de transformações nos gráficos
tridimensionais.

Exemplo:

```maxima
[transform_xy, false]
```
O valor por omiss~ao de `transform_xy` é `false`. Se não for
`false`, deverá ser o resultado produzido por

```maxima
make_transform ([x, y, z], f1(x, y, z), f2(x, y, z), f3(x, y, z))$
```
A transformação `polar_xy` está previamente definida no
Maxima. É igual ao resultado da transformação

```maxima
make_transform ([r, th, z], r*cos(th), r*sin(th), z)$
```


**Opções do Gnuplot:**


Existem muitas opções específicas para o
Gnuplot. Muitas dessas opções são comandos próprios do
Gnuplot, especificados como sequências de caracteres. Consulte a
documentação do gnuplot para mais pormenores.



- *
`gnuplot_term`

Define o tipo terminal de saída para gnuplot.

  - *
Valor por omissão: `default`
A saída do Gnuplot é mostrada em uma janela gráfica
separada.
  - *
Valor: `dumb`
A saída do Gnuplot é mostrada na consola do Maxima,
usando uma aproximação "arte ASCII" para gráficos.
  - *
Valor: `ps`
Gnuplot gera comandos na linguagem PostScript de descrição de
páginas.  Se à opção `gnuplot_out_file` tiver sido dada o
nome de um ficheiro, gnuplot escreverá os comandos PostScript nesse
ficheiro.  De outra forma, os comandos PostScript serão gravados no
ficheiro `maxplot.ps`.
  - *
Valor: qualquer outro tipo de terminal aceite pelo gnuplot
Gnuplot pode produzir gráficos em muitos outros formatos gráficos
tais como png, jpeg, svg, etc. Para criar gráficos em algum desses
deverá dar-se a `gnuplot_term` um (símbolo)
suportado pelo gnuplot ou uma especificação completa de terminal
do gnuplot com opções válidas (sequência de caracteres).  Por
exemplo `[gnuplot_term,png]` cria gráficos no formato PNG
(Portable Network Graphics) enquanto `[gnuplot_term,"png size 1000,1000"]` cria gráficos no formato PNG com tamanho de 1000x1000
pixels. Se à opção `gnuplot_out_file` for dado o nome de um
ficheiro, gnuplot gravará o graáfico nesse ficheiro. De outra forma,
o gráfico é gravado no ficheiro `maxplot.term`, onde
*term* é o nome do terminal do gnuplot.
- *
Opção: `gnuplot_out_file`

Grava o gráfico criado por gnuplot para um ficheiro.

  - *
Valor por omissão: `false`
Nenhum ficheiro de saída especificado.
  - *
Valor: *filename*
Exemplo: `[gnuplot_out_file, "myplot.ps"]`
Quando usada em conjunto com o terminal PostScript do gnuplot, neste
exemplo o gráfico será gravado em formato PostScript no ficheiro
`myplot.ps`, .
- *
Opção: `gnuplot_pm3d`

Controla o uso do modo PM3D, que possui recursos avançados em 3D. O
modo PM3D está somente disponível nas versões de
gnuplot posteriores a 3.7. O valor padrão para `gnuplot_pm3d` é
`false`.

Exemplo:

```maxima
[gnuplot_pm3d, true]
```
- *
Opção: `gnuplot_preamble`

Insere comandos antes que o gráfico seja desenhado. Quaisquer comandos
válidos para o gnuplot podem ser usados. Multiplos comandos podem ser
separados com um ponto e vírgula. O exemplo mostrado
produz uma escala logarítmica no gráfico. O valor
padrão para `gnuplot_preamble` é uma sequência de caracteres
vazia `""`.

Exemplo:

```maxima
[gnuplot_preamble, "set log y"]
```
- *
Opção: `gnuplot_curve_titles`

Controla os títulos dados na legenda do gráfico. O valor
padrão é `[default]`, que escolhe automaticamente um
título para função cujo gráfico está a ser
desenhado. Se não for igual a `[default]`,
`gnuplot_curve_titles` poderá conter uma lista de sequências de
caracteres, cada uma das quais é `"title 'nome'"`.  (Para
desabilitar a legenda do gráfico, adicione `"set nokey"` a
`gnuplot_preamble`.)

Exemplo:

```maxima
[gnuplot_curve_titles,
["title 'Minha primeira função'", "title 'Minha segunda função'"]]
```
- *
Opção: `gnuplot_curve_styles`

Uma lista de sequências de caracteres a ser enviada para o gnuplot
para controlar a aparência das curvas, nomeadamente, cor, largura,
brilho, etc.  O valor padrão é `["with lines 3", "with lines 1", "with lines 2", "with lines 5", "with lines 4", "with lines 6", "with lines 7"]`, que circula através de diferentes cores. Consulte a
documentação de `plot` no manual do gnuplot para mais
informações.

Exemplo:

```maxima
[gnuplot_curve_styles, ["with lines 7", "with lines 2"]]
```
- *
Opção: `gnuplot_default_term_command`

O comando do Gnuplot para escolher o tipo de terminal gráfico. O valor
padrão é a sequência de caracteres vazia `""`, nomeadamente,
usar-se-á o formato padrão do gnuplot.

Exemplo:

```maxima
[gnuplot_default_term_command, "set term x11"]
```
- *
Opção: `gnuplot_dumb_term_command`

O comando gnuplot para escolher o tipo de terminal não gráfico. O
valor padrão é `"set term dumb 79 22"`, que produz
saída em texto com 79 por 22 caracteres.

Exemplo:

```maxima
[gnuplot_dumb_term_command, "set term dumb 132 50"]
```
- *
Opção: `gnuplot_ps_term_command`

O comando gnuplot para escolher o tipo de terminal para o terminal
PostScript. O valor padrão é `"set size 1.5, 1.5;set term postscript eps enhanced color solid 24"`, que escolhe o tamanho para 1.5
vezes o padrão do gnuplot, e o tamanho da fonte para 24, além de
outras coisas. Para mais informação, consulte a documentação
de `set term postscript` no manual do gnuplot.

Exemplo:

Toda as figuras nos exemplos para a função *plot2d* neste
manual forma obtidas a partir de ficheiros Postscript que foram
produzidos após ter mudado `gnuplot_ps_term_command` par:

```maxima
[gnuplot_ps_term_command,
"set size 1.3, 1.3; set term postscript eps color solid lw 2.5 30"]
```

<!-- category: Other -->
<!-- keywords: set_plot_option -->
<!-- signatures: set_plot_option(opção) -->
### Function: set_plot_option (opção)

Atribui valores às opções globais para impressão.
*opção* é especificada como uma lista de dois ou mais
elementos, na qual o primeiro elemeto é uma das palavras chave
dentro da lista `plot_options`.


O argumento dado a `set_plot_option` é avaliado e
`set_plot_option` retorna a lista completa `plot_options` 
(após modificar um desses elementos).


Veja também `plot_options`, `plot2d` e `plot3d`.


Exemplos:


Modifica a gralha (`grid`) e o intervalo de `x`.  Quando uma
palavra chave em `plot_options` tiver um valor
atribuído, colocar um apóstrofo evita que seja
avaliado.









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

