## draw

<!-- category: Plotting -->
<!-- keywords: adapt_depth -->
<!-- signatures: adapt_depth -->
### Variable: adapt_depth

Valor padrão: 10


`adapt_depth` é o número máximo de quebras usado pelas rotinas adaptativos de impressão.


Essa opção é relevante somente para funções 2d `explicitas`.

<!-- category: Plotting -->
<!-- keywords: axis_3d -->
<!-- signatures: axis_3d -->
### Variable: axis_3d

Valor padrão: `true`


Se `axis_3d` for `true`, os eixos *x*, *y* e *z* são mostrados em fundos gráficos tridimensionais.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(axis_3d = false,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```


Veja também `axis_bottom`,  `axis_left`, `axis_top`, e `axis_right` para eixos em duas dimensões.

<!-- category: Plotting -->
<!-- keywords: axis_bottom -->
<!-- signatures: axis_bottom -->
### Variable: axis_bottom

Valor padrão: `true`


Se `axis_bottom` for `true`, o eixo inferior é mostrado em fundos gráficos bidimensionais.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_bottom = false,
             explicit(x^3,x,-1,1))$
```


Veja também `axis_left`,  `axis_top`, `axis_right`, e `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: axis_left -->
<!-- signatures: axis_left -->
### Variable: axis_left

Valor padrão: `true`


Se `axis_left` for `true`, o eixo da esquerda é mostrado em fundos gráficos bidimensionais.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_left = false,
             explicit(x^3,x,-1,1))$
```


Veja também `axis_bottom`,  `axis_top`, `axis_right`, e `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: axis_right -->
<!-- signatures: axis_right -->
### Variable: axis_right

Valor padrão: `true`


Se `axis_right` for `true`, o eixo da direita é mostrado em fundos gráficos bidimensionais.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_right = false,
             explicit(x^3,x,-1,1))$
```


Veja também `axis_bottom`,  `axis_left`, `axis_top`, e `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: axis_top -->
<!-- signatures: axis_top -->
### Variable: axis_top

Valor padrão: `true`


Se `axis_top` for `true`, o eixo superior é mostrado em fundos gráficos bidimensionais.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(axis_top = false,
             explicit(x^3,x,-1,1))$
```


Veja também `axis_bottom`,  `axis_left`, `axis_right`, e `axis_3d`.

<!-- category: Plotting -->
<!-- keywords: border -->
<!-- signatures: border -->
### Variable: border

Valor padrão: `true`


Se `border` for `true`, bordas de polígonos são colorizadas
de acordo com `line_type` e `line_width`.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `polygon`, `rectangle`, e `ellipse`.


Exemplo:



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
<!-- keywords: color -->
<!-- signatures: color -->
### Variable: color

Valor padrão: `"black"`


`color` especifica a cor para o desenho de linhas, pontos, bordas de
polígonos e rótulos.


Cores podem ser fornecidas como nomes ou em código hexadecimal *rgb*.


Nomes de cores disponíveis atualmente são: 
`"white"`, `"black"`, `"gray0"`, `"grey0"`, `"gray10"`,
`"grey10"`, `"gray20"`, `"grey20"`, `"gray30"`, `"grey30"`,
`"gray40"`, `"grey40"`, `"gray50"`, `"grey50"`, `"gray60"`,
`"grey60"`, `"gray70"`, `"grey70"`, `"gray80"`, `"grey80"`,
`"gray90"`, `"grey90"`, `"gray100"`, `"grey100"`, `"gray"`,
`"grey"`, `"light-gray"`, `"light-grey"`, `"dark-gray"`,
`"dark-grey"`, `"red"`, `"light-red"`, `"dark-red"`, `"yellow"`,
`"light-yellow"`, `"dark-yellow"`, `"green"`, `"light-green"`,
`"dark-green"`, `"spring-green"`, `"forest-green"`, `"sea-green"`,
`"blue"`, `"light-blue"`, `"dark-blue"`, `"midnight-blue"`, 
`"navy"`, `"medium-blue"`, `"royalblue"`, `"skyblue"`, 
`"cyan"`, `"light-cyan"`, `"dark-cyan"`, `"magenta"`, 
`"light-magenta"`, `"dark-magenta"`, `"turquoise"`, 
`"light-turquoise"`, `"dark-turquoise"`, `"pink"`, `"light-pink"`,
`"dark-pink"`, `"coral"`, `"light-coral"`, `"orange-red"`,
`"salmon"`, `"light-salmon"`, `"dark-salmon"`, `"aquamarine"`,
`"khaki"`, `"dark-khaki"`, `"goldenrod"`, `"light-goldenrod"`,
`"dark-goldenrod"`, `"gold"`, `"beige"`, `"brown"`, `"orange"`,
`"dark-orange"`, `"violet"`, `"dark-violet"`, `"plum"` and `"purple"`.


Componentes cromáticos em código hexadecimal são introduzidos na forma `"#rrggbb"`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^2,x,-1,1), /* default is black */
             color = "red",
             explicit(0.5 + x^2,x,-1,1),
             color = blue,
             explicit(1 + x^2,x,-1,1),
             color = "light-blue", /* double quotes if - is used */
             explicit(1.5 + x^2,x,-1,1),
             color = "#23ab0f",
             label("Esse é um rótulo",0,1.2)  )$
```


Veja também `fill_color`.

<!-- category: Plotting -->
<!-- keywords: colorbox -->
<!-- signatures: colorbox -->
### Variable: colorbox

Valor padrão: `true`


If `colorbox` is `true`, a color scale is drawn together with
`image` objects.


Since this is a global graphics option, its position in the scene description
does not matter.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) im: apply('matrix,
                 makelist(makelist(random(200),i,1,30),i,1,30))$
(%i3) draw2d(image(im,0,0,30,30))$
(%i4) draw2d(colorbox=false, image(im,0,0,30,30))$
```


Veja também `palette`.

<!-- category: Plotting -->
<!-- keywords: columns -->
<!-- signatures: columns -->
### Variable: columns

Valor padrão: 1


`columns` é o número de colunas em gráficos multiplos.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo do gráfico
não é importante. Pode também ser usado como um argumento da função `draw`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) scene1: gr2d(title="Elipse",
                   nticks=30,
                   parametric(2*cos(t),5*sin(t),t,0,2*%pi))$
(%i3) scene2: gr2d(title="Triângulo",
                   polygon([4,5,7],[6,4,2]))$
(%i4) draw(scene1, scene2, columns = 2)$
```

<!-- category: Plotting -->
<!-- keywords: contour -->
<!-- signatures: contour -->
### Variable: contour

Valor padrão: `none`


Option `contour` torna o usuário capaz de selecionar onde imprimir linhas de contorno.
Valores possíveis são:



- *
`none`:
nenhuma linha de contorno é mostrada.
- *
`base`:
linhas de contorno são projetadas no plano xy.
- *
`surface`:
linhas de contorno são mostradas sobre a superfície.
- *
`both`:
duas linhas de contorno são mostradas: no plano xy e sobre a superfície.
- *
`map`:
linhas de contorno são projetadas sobre o plano xy, e o ponto de boservação é
escolhido na vertical.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



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

Valor padrão: 5


`contour_levels` é o número de níveis em gráficos de contorno.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(20*exp(-x^2-y^2)-10,x,0,2,y,-3,3),
             contour_levels = 15,
             contour        = both,
             surface_hide   = true) $
```

<!-- category: Plotting -->
<!-- keywords: draw -->
<!-- signatures: draw(gr2d, ..., gr3d, ..., opções, ...) -->
### Function: draw (gr2d, ..., gr3d, ..., opções, ...)

Monta o fundo de uma série de gráficos; seus argumentos são objetos `gr2d` e
`gr3d`, juntamente com algumas opções. Por padrão, o fundos gráficos são colocados juntos
em uma coluna.


A função `draw` aceita duas opções possíveis: `terminal` 
e `columns`.


As funções `draw2d` e `draw3d` são atalhos para serem usados 
quando somente um fundo gráfico é requerido, em duas ou três dimensões, respectivamente.


Para fazer uso dessa função escreva primeiramente `load("draw")`.


Exemplo:



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
<!-- keywords: draw2d -->
<!-- signatures: draw2d(opção, objeto gráfico, ...) -->
### Function: draw2d (opção, objeto gráfico, ...)

Essa função é um atalho para
`draw2d(gr2d(opções, ..., objeto gráfico, ...))`.


Pode ser usada para montar gráfico de um único fundo bidimensional.


Para fazer uso dessa função escreva primeiramente `load("draw")`.

<!-- category: Plotting -->
<!-- keywords: draw3d -->
<!-- signatures: draw3d(opção, graphic object, ...) -->
### Function: draw3d (opção, graphic object, ...)

Essa função é um atalho para
`draw3d(gr3d(opções, ..., objeto gráfico, ...))`.


Pode ser usada para montar o fundo gráfico único tridmensional.


Para fazer uso dessa função escreva primeiramente `load("draw")`.

<!-- category: Plotting -->
<!-- keywords: draw_pipes -->
<!-- signatures: draw_pipes -->
### Variable: draw_pipes

Valor padrão: `true`


Quando `draw_pipes` for `true`, Maxima comunica-se com Gnuplot
diretamente (via pipes). Se `draw_pipes` for `false`, Maxima comunica-se 
com Gnuplot via arquivos. Essa opção não está disponível para usuários windows.

<!-- category: Plotting -->
<!-- keywords: enhanced3d -->
<!-- signatures: enhanced3d -->
### Variable: enhanced3d

Valor padrão: `false`


Se `enhanced3d` for `true`, superfícies são coloridas em gráficos tridimensionais;
em outras palavras, pode escolher o modo pm3d do Gnuplot.


Veja a opção `palette` para aprender como paletas são especificadas.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(surface_hide = true,
             enhanced3d   = true,
             palette      = gray,
             explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3))$
```

<!-- category: Plotting -->
<!-- keywords: eps_height -->
<!-- signatures: eps_height -->
### Variable: eps_height

Valor padrão: 8


Essa é a altura (medida em cm) do arquivo Postscript
gerado pelos terminais `eps` e `eps_color`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo gráfico
não é importante. Pode também ser usada como um argumento da função `draw`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal   = 'eps,
             eps_width  = 3,
             eps_height = 3,
             explicit(x^2,x,-1,1))$
```


Veja também `terminal`, `file_name`, e `eps_width`.

<!-- category: Plotting -->
<!-- keywords: eps_width -->
<!-- signatures: eps_width -->
### Variable: eps_width

Valor padrão: 12


Essa é a largura (medida em cm) do arquivo Postscript
gerado pelos terminais `eps` e `eps_color`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo gráfico
não é importante. Pode também ser usada como um argumento da função `draw`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal   = 'eps,
             eps_width  = 3,
             eps_height = 3,
             explicit(x^2,x,-1,1))$
```


Veja também `terminal`, `file_name`, e `eps_height`.

<!-- category: Plotting -->
<!-- keywords: file_name -->
<!-- signatures: file_name -->
### Variable: file_name

Valor padrão: `"maxima_out"`


Esse é o nome do arquivo onde os terminais `png`, `jpg`, `eps`
e `eps_color` guardarão o gráfico.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante. Pode também ser usada como um argumento da função `draw`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'png)$
```


Veja também `terminal`, `pic_width`, e `pic_height`.

<!-- category: Plotting -->
<!-- keywords: fill_color -->
<!-- signatures: fill_color -->
### Variable: fill_color

Valor padrão: `"red"`


`fill_color` especifica a cor para preenchimento de polígonos e
funções explicitamente bidimensionais.


Veja `color` para aprender como cores são especificadas.

<!-- category: Plotting -->
<!-- keywords: filled_func -->
<!-- signatures: filled_func -->
### Variable: filled_func

Valor padrão: `false`


`filled_func` indica se uma função é preenchida (`true`)
ou não (`false`).


Essa opção afeta somente objetos gráfico bidimensional `explicit`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = red,
             filled_func = true,
             explicit(sin(x),x,0,10) )$
```


Veja também `fill_color`.

<!-- category: Plotting -->
<!-- keywords: gr2d -->
<!-- signatures: gr2d(opção gráfica, ..., objeto gráfico, ...) -->
### Function: gr2d (opção gráfica, ..., objeto gráfico, ...)

A função `gr2d` constrói um objeto descrevendo um fundo gráfico em duas dimensões. Arguments are
*opções gráficas* e *objetos gráficos*. Esse fundo gráfico é interpretado
sequêncialmente: *opções gráficas* afetam aqueles *objetos gráficos* colocados
imediatamente à sua direita.


Para fazer uso dessa função escreva primeiramente `load("draw")`.


Adiante encontra-se uma lista de *objetos gráficos* disponívies para fundos gráficos em duas dimensões:



- *
`points([[x1,y1], [x2,y2], [x3,y3],...])` ou `points([x1,x2,x3,...], [y1,y2,y3,...])`:
posiciona os pontos `[x1,y1]`, `[x2,y2]`, `[x2,y2]`, ... no gráfico.

Esse objeto é efetado pelas seguintes *opções gráficas*: `point_size`, 
`point_type`, `points_joined`, `line_width`, `key`,
`line_type` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(key           = "Small points",
             points(makelist([random(20),random(50)],k,1,10)),
             point_type    = 6,
             point_size    = 3,
             points_joined = true,
             key           = "Great points",
             points(makelist(k,k,1,20),makelist(random(30),k,1,20)))$
```
- *
`polygon([[x1,y1], [x2,y2], [x3,y3],...])` ou `polygon([x1,x2,x3,...], [y1,y2,y3,...])`:
desenha um polígono com vértices `[x1,y1]`, `[x2,y2]`, `[x2,y2]`, ... no plano.

Esse objeto é afetado pelas seguintes *opçs gráficas*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`,
`line_type` `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(color      = "#e245f0",
             line_width = 8,
             polygon([[3,2],[7,2],[5,5]]),
             border      = false,
             fill_color  = yellow,
             polygon([[5,2],[9,2],[7,5]]) )$
```
- *
`rectangle([x1,y1], [x2,y2])`:
desenha um retângulo partindo do vértice `[x1,y1]` e terminando no vértice `[x2,y2]` oposto ao primeiro.

Esse objeto é afetado pelas seguintes *opções gráficas*: `transparent`, 
`fill_color`, `border`, `line_width`, `key`,
`line_type` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(fill_color  = red,
             line_width  = 6,
             line_type   = dots,
             transparent = false,
             fill_color   = blue,
             rectangle([-2,-2],[8,-1]),   /* opposite vertices */
             transparent = true,
             line_type   = solid,
             line_width  = 1,
             rectangle([9,4],[2,-1.5]),
             xrange      = [-3,10],
             yrange      = [-3,4.5] )$
```
- *
`ellipse(xc, yc, a, b, ang1, ang2)`:
desenha uma elipse com centro em `[xc, yc]` com semi-eixo maior `a` e
semi-eixo menor `b` traçando um arco de elipse que se inicia no ângulo `ang1` e que vai
até o ângulo `ang2`.
semi axis `a` e `b`, respectively, from angle `ang1` to angle
`ang2`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `nticks`, 
`transparent`, `fill_color`, `border`, `line_width`, 
`line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(transparent = false,
             fill_color  = 8,
             color       = gray30,
             transparent = false,
             line_width  = 5,
             ellipse(0,6,3,2,270,-270),  /* center (x,y), a, b, start & end in degrees */
             transparent = true,
             color       = blue,
             line_width  = 3,
             ellipse(2.5,6,2,3,30,-90),
             xrange      = [-3,6],
             yrange      = [2,9] )$
```
- *
`label(rótulo,x,y)`:
escreve o `rótulo` no ponto `[x,y]`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `label_alignment`, 
`label_orientation` e `color`.

Exemplo:

Nesse exemplo, um ponto imaginário é adicionado para firmar a imagem.
O pacote `draw` precisa sempre da dados para desenhar um fundo.
Essas cores podem mudar em diferentes terminais.

```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^2,x,-1,1),
             color = "red",
             label("Label in red",0,0.3),
             color = "#0000ff",
             label("Label in blue",0,0.6),
             color = "light-blue", /* double quotes if - is used */
             label("Rótulo em light-blue",0,0.9)  )$
```
- *
`vector([x,y], [dx,dy])`:
desenha um vetor de componentes ortogonais `[dx,dy]` com orígem eno ponto `[x,y]`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `head_both`, 
`head_length`, `head_angle`, `head_type`, `line_width`, 
`line_type` e `key`.

Exemplo:

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
- *
`explicit(fcn,var,minval,maxval)`:
monta o gráfico da função explícita `fcn`, com variável `var` assumindo valores
de `minval` a `maxval`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `nticks`, 
`adapt_depth`, `line_width`, `line_type`, `key`,
`filled_func`, `fill_color` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(line_width = 3,
             color      = blue,
             explicit(x^2,x,-3,3) )$
(%i3) draw2d(fill_color  = brown,
             filled_func = true,
             explicit(x^2,x,-3,3) )$
```
- *
`implicit(fcn,x-var,x-minval,x-maxval,y-var,y-minval,y-maxval)`:
monta o gráfico da função implícita definida por `fcn`, com variável `x-var` assumindo
de `x-minval` a `x-maxval`, e variável `y-var` assumindo valores
de `y-minval` a `y-maxval`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `ip_grid`, 
`ip_grid_in`, `line_width`, `line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal  = eps,
             grid      = true,
             line_type = solid,
             key       = "y^2=x^3-2*x+1",
             implicit(y^2=x^3-2*x+1, x, -4,4, y, -4,4),
             line_type = dots,
             key       = "x^3+y^3 = 3*x*y^2-x-1",
             implicit(x^3+y^3 = 3*x*y^2-x-1, x, -4,4, y, -4,4),
             title     = "Duas funções implícitas" )$
```
- *
`polar(radius,ang,minang,maxang)`:
plots function `radius(ang)` defined in polar coordinates, com a variável `ang`
assumindo valores de `minang` a `maxang`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `nticks`, 
`line_width`, `line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(user_preamble = "set grid polar",
             nticks        = 200,
             xrange        = [-5,5],
             yrange        = [-5,5],
             line_type     = 6,
             line_width    = 3,
             title         = "Hyperbolic Spiral",
             polar(10/theta,theta,1,10*%pi) )$
```
- *
`parametric(xfun,yfun,par,parmin,parmax)`:
monta o gráfico da função paramétrica `[xfun,yfun]`, com parâmetro `par`
assumindo valores de `parmin` a `parmax`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `nticks`, 
`line_width`, `line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(x),x,-1,3),
             color = red,
             key   = "Esse é a unidade paramétrica!!",
             parametric(2*cos(rrr),rrr^2,rrr,0,2*%pi))$
```
- *
`image(im,x0,y0,width,height)`:
monta o gráfico da imágem `im` em uma região retangular do vértice `(x0,y0)` ao vértice
`(x0+width,y0+height)` no plano real. O argumeto `im` deve ser uma
matriz de números reais, ou uma matriz de vetores de comprimento três.

Se `im` for uma matriz de números reais, valores de pixel são interpretados conforme
a opção gráfica `palette`, que é um vetor de comprimento três com componentes
numéricas variando de -36 a +36; cada valor é um índice para uma fórmula mapeando os níveis
sobre as cores vermelha, verde e azul, respectivamente:

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
30: x/0.32-0.78125 31: 2*x-0.84     32: 4x;1;-2x+1.84;x/0.08-11.5
33: |2*x - 0.5|    34: 2*x          35: 2*x - 0.5
36: 2*x - 1
```
números negativos significam componente de cor negativa.

`palette = gray` e `palette = color` são atalhos para
`palette = [3,3,3]` e `palette = [7,5,15]`, respectivamente.

Se `im` for uma matriz de vetores de comprimento três, eles são interpretados
como componenetes das cores vermelho, verde e azul.

Exemplos:

se `im` for uma matriz de números reais, valores de pixel são interpretados conforme
a opção gráfica `palette`.

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

Veja também `colorbox`.

Se `im` for uma matriz de vetores de comprimento três, eles são interpretados
como componentes da cores vermelho, verde e azul.

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


Veja também as seguintes opções gráficas: `xrange`, `yrange`, 
`logx`, `logy`, `terminal`, `grid`, `title`, 
`xlabel`, `ylabel`, `xtics`, `ytics`, `xy_file`, 
`file_name`, `pic_width`, `pic_height`, 
`eps_width`, `eps_height`,
`user_preamble`, `axis_bottom`, `axis_left`, `axis_top`, 
e `axis_right`.

<!-- category: Plotting -->
<!-- keywords: gr3d -->
<!-- signatures: gr3d(opção gráfica, ..., objeto gráfico, ...) -->
### Function: gr3d (opção gráfica, ..., objeto gráfico, ...)

A função `gr3d` constrói um objeto descrevendo um fundo gráfico tridimensional. Argumentos são
*opções gráficas* e *objetos gráficos*. Esse fundo gráfico é interpretado
sequêncialmente: *opções gráficas* afetam aqueles *objetos gráficos* colocados
imediatamente à sua direita.


Para fazer uso dessa função escreva primeiramente `load("draw")`.


Essa é a lista dos *objetos gráficos* disponíveis para fundos gráficos tridimensionais:



- *
`points([[x1,y1,z1], [x2,y2,z2], [x3,y3,z3],...])` ou 
`points([x1,x2,x3,...], [y1,y2,y3,...], [z1,z2,z3,...])`:
posiciona os pontos `[x1,y1,z1]`, `[x2,y2,z2]`, `[x2,y2,z3]`, ... no gráfico.

Esse objeto é afetado pelas seguintes *opções gráficas*: `point_size`, 
`point_type`, `points_joined`, `line_width`, `key`, `line_type`
e `color`.

Exemplos:

Uma amostra tridimensional,

```maxima
(%i1) load("draw")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) draw3d(title      = "Velocidades diárias de ventos disponíveis",
             point_size = 2,
             points(args(submatrix (s2, 4, 5))) )$
```

Duas amostras tridimensionais,

```maxima
(%i1) load("draw")$
(%i2) load ("numericalio")$
(%i3) s2 : read_matrix (file_search ("wind.data"))$
(%i4) draw3d(title      = "Velocidades diárias de ventos disponíveis. Dois conjuntos de dados",
             point_size = 2,
             key        = "Amostras das estações 1, 2 e 3",
             points(args(submatrix (s2, 4, 5))),
             point_type = 4,
             key        = "Amostras das estações 1, 4 e 5",
             points(args(submatrix (s2, 2, 3))) )$
```
- *
`label(rótulo,x,y,z)`:
escreve `rótulo` no ponto `[x,y,z]`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `label_alignment`, 
`label_orientation` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3),
             color = red,
             label("SUBINDO",-2,0,3),
             color = blue,
             label("DESCENDO",2,0,-3) )$
```
- *
`vector([x,y,z], [dx,dy,dz])`:
monta o gráfico do vetor `[dx,dy,dz]` com orígem em `[x,y,z]`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `head_both`, 
`head_type`, `line_width`, 
`line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw3d(color = cyan,
             vector([0,0,0],[1,1,1]/sqrt(3)),
             vector([0,0,0],[1,-1,0]/sqrt(2)),
             vector([0,0,0],[1,1,-2]/sqrt(6)) )$
```
- *
`explicit(fcn,var1,minval1,maxval1,var2,minval2,maxval2)`:
monta o gráfico da função explícita `fcn`, com a variável `var1` assumindo valores
de `minval1` a `maxval1` e variável `var2` assumindo valores
de `minval2` a `maxval2`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `xu_grid`, 
`yv_grid`, `line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw3d(key   = "Gauss",
             color = "#a02c00",
             explicit(20*exp(-x^2-y^2)-10,x,-3,3,y,-3,3),
             color = blue,
             key   = "Plane",
             explicit(x+y,x,-5,5,y,-5,5),
             surface_hide = true)$
```
- *
`parametric(xfun,yfun,zfun,par,parmin,parmax)`:
monta o gráfico da curva paramétrica `[xfun,yfun,zfun]`, com parâmetro `par`
assumindo valores de `parmin` a `parmax`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `nticks`, 
`line_width`, `line_type`, `key` e `color`.

Exemplo:

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
- *
`parametric_surface(xfun,yfun,zfun,par1,par1min,par1max,par2,par2min,par2max)`:
monta o gráfico da superfície paramétrica `[xfun,yfun,zfun]`, com parâmetro `par1`
assumindo valores de `par1min` a `par1max` e o parâmetro `par2`
assumindo valores de `par2min` a `par2max`.

Esse objeto é afetado pelas seguintes *opções gráficas*: `xu_grid`, 
`yv_grid`, `line_type`, `key` e `color`.

Exemplo:

```maxima
(%i1) load("draw")$
(%i2) draw3d(title          = "Concha do mar",
             xu_grid        = 100,
             yv_grid        = 25,
             rot_vertical   = 100,
             rot_horizontal = 20,
             surface_hide   = true,
             parametric_surface(0.5*u*cos(u)*(cos(v)+1),
                                0.5*u*sin(u)*(cos(v)+1),
                                u*sin(v) - ((u+3)/8*%pi)^2 - 20,
                                u, 0, 13*%pi, v, -%pi, %pi) )$
```


Veja também as seguintes opções gráficas: `xrange`, `yrange`, 
`zrange`, `logx`, `logy`, `logz`, `terminal`, 
`grid`, `title`, `xlabel`, `ylabel`, `zlabel`, 
`xtics`, `ytics`, `ztics`, `xy_file`, 
`user_preamble`, `axis_bottom`, `axis_left`, 
`axis_top`, `file_name`, `pic_width`, `pic_height`, 
`eps_width`, `eps_height`,
`axis_right`, `rot_vertical`, `rot_horizontal`, 
`axis_3d`, `xu_grid`, `yv_grid`, `surface_hide`, 
`contour`, `contour_levels`, `palette`, `colorbox`
e `enhanced3d`.

<!-- category: Plotting -->
<!-- keywords: grid -->
<!-- signatures: grid -->
### Variable: grid

Valor padrão: `false`


Se `grid` for `true`, uma malha será desenhada sobre o plano *xy*.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(grid = true,
             explicit(exp(u),u,-2,2))$
```

<!-- category: Plotting -->
<!-- keywords: head_angle -->
<!-- signatures: head_angle -->
### Variable: head_angle

Valor padrão: 45


`head_angle` indica o ângulo, em graus, entre a ponta da seta do vetor e
o segmento que forma o corpo do vetor.


Essa opção é relevante somente para objetos do tipo `vector`.


Exemplo:



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


Veja também `head_both`, `head_length`, e `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_both -->
<!-- signatures: head_both -->
### Variable: head_both

Valor padrão: `false`


Se `head_both` for `true`, vetores são mostrados com seta dupla na ponta.
Se `false`, somente uma seta é mostrada.


Essa opção somente é relevante para objetos do tipo `vector`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange      = [0,8],
             yrange      = [0,8],
             head_length = 0.7,
             vector([1,1],[6,0]),
             head_both   = true,
             vector([1,7],[6,0]) )$
```


Veja também `head_length`, `head_angle`, e `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_length -->
<!-- signatures: head_length -->
### Variable: head_length

Valor padrão: 2


`head_length` indica, em unidades do eixo *x*, o comprimento da ponta da seta do vetor.


Essa opção é relevante somente para objetos do tipo `vector`.


Exemplo:



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


Veja também `head_both`, `head_angle`, e `head_type`.

<!-- category: Plotting -->
<!-- keywords: head_type -->
<!-- signatures: head_type -->
### Variable: head_type

Valor padrão: `filled`


`head_type` é usada para especificar como a ponta é mostrada. Valores
possíveis são: `filled` (ponta fechada e preenchida), `empty`
(ponta fechada mas não preenchida), e `nofilled` (ponta aberta).


Essa opção é relevante somente para objetos do tipo `vector`.


Exemplo:



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


Veja também `head_both`, `head_angle`, e `head_length`.

<!-- category: Plotting -->
<!-- keywords: ip_grid -->
<!-- signatures: ip_grid -->
### Variable: ip_grid

Valor padrão: `[50, 50]`


`ip_grid` escolhe a grade para a primeira amostragem em gráficos implícitos.


Essa opção é relevante somente para `implicit` objects.

<!-- category: Plotting -->
<!-- keywords: ip_grid_in -->
<!-- signatures: ip_grid_in -->
### Variable: ip_grid_in

Valor padrão: `[5, 5]`


`ip_grid_in` escolhe a grade para a segunda amostragem em gráficos implícitos.


Essa opção é relevante somente para `implicit` objects.

<!-- category: Plotting -->
<!-- keywords: key -->
<!-- signatures: key -->
### Variable: key

Valor padrão: `""` (a sequência de caracteres vazia)


`key` é o nome de uma função na legenda. Se `key` é uma
sequência de caracteres vazia, nenhuma chave é atribuída à função.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `points`, `polygon`, `rectangle`,
`ellipse`, `vector`, `explicit`, `implicit`,
`parametric`, e `polar`.
- *
`gr3d`: `points`, `explicit`, `parametric`,
e `parametric_surface`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(key = "Seno",
             explicit(sin(x),x,0,10),
             key = "Cosseno",
             line_type = 3,
             explicit(cos(x),x,0,10) )$
```

<!-- category: Plotting -->
<!-- keywords: label_alignment -->
<!-- signatures: label_alignment -->
### Variable: label_alignment

Valor padrão: `center`


`label_alignment` é usado para especificar onde escrever rótulos com
relação às coordenadas fornecidas. Valores possíveis são: `center`,
`left`, e `right`.


Essa opção é relevante somente para objetos do tipo `label`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange          = [0,10],
             yrange          = [0,10],
             points_joined   = true,
             points([[5,0],[5,10]]),
             color           = blue,
             label("Centered alignment (default)",5,2),
             label_alignment = 'left,
             label("Left alignment",5,5),
             label_alignment = 'right,
             label("Right alignment",5,8))$
```


Veja também `label_orientation`, e `color`.

<!-- category: Plotting -->
<!-- keywords: label_orientation -->
<!-- signatures: label_orientation -->
### Variable: label_orientation

Valor padrão: `horizontal`


`label_orientation` é usada para especificar a orientação dos rótulos.
Valores possíveis são: `horizontal`, e `vertical`.


Essa opção é relevante somente para objetos do tipo `label`.


Exemplo:


Nesse exemplo, um ponto fictício é adicionado para firmar uma imagem.
o pacote `draw` precisa sempre de dados para montar um fundo.


```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange     = [0,10],
             yrange     = [0,10],
             point_size = 0,
             points([[5,5]]),
             color      = navy,
             label("Horizontal orientation (default)",5,2),
             label_orientation = 'vertical,
             color             = "#654321",
             label("Vertical orientation",1,5))$
```


Veja também `label_alignment`, e `color`.

<!-- category: Plotting -->
<!-- keywords: line_type -->
<!-- signatures: line_type -->
### Variable: line_type

Valor padrão: `solid`


`line_type` indica como linhas são mostradas; valores possíveis são
`solid` e `dots`.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` e `polar`.
- *
`gr3d`: `points`, `explicit`, `parametric` e `parametric_surface`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(line_type = dots,
             explicit(1 + x^2,x,-1,1),
             line_type = solid, /* default */
             explicit(2 + x^2,x,-1,1))$
```


Veja também `line_width`.

<!-- category: Plotting -->
<!-- keywords: line_width -->
<!-- signatures: line_width -->
### Variable: line_width

Valor padrão: 1


`line_width` é a lagura das linhas do gráfico.
Seu valor deve ser um número positivo.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `points`, `polygon`, `rectangle`, 
`ellipse`, `vector`, `explicit`, `implicit`, 
`parametric` e `polar`.
- *
`gr3d`: `points` e `parametric`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(x^2,x,-1,1), /* default width */
             line_width = 5.5,
             explicit(1 + x^2,x,-1,1),
             line_width = 10,
             explicit(2 + x^2,x,-1,1))$
```


Veja também `line_type`.

<!-- category: Plotting -->
<!-- keywords: logx -->
<!-- signatures: logx -->
### Variable: logx

Valor padrão: `false`


Se `logx` for `true`, o eixo *x*será desenhado em
escala logarítmica.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(log(x),x,0.01,5),
             logx = true)$
```


Veja também `logy` e `logz`.

<!-- category: Plotting -->
<!-- keywords: logy -->
<!-- signatures: logy -->
### Variable: logy

Valor padrão: `false`


Se `logy` for `true`, o eixo *y*será desenhado em
escala logarítmica.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(logy = true,
             explicit(exp(x),x,0,5))$
```


Veja também `logx` e `logz`.

<!-- category: Plotting -->
<!-- keywords: logz -->
<!-- signatures: logz -->
### Variable: logz

Valor padrão: `false`


Se `logz` for `true`, o eixo *z*será desenhado em
escala logarítmica.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(logz = true,
             explicit(exp(u^2+v^2),u,-2,2,v,-2,2))$
```


Veja também `logx` e `logy`.

<!-- category: Plotting -->
<!-- keywords: nticks -->
<!-- signatures: nticks -->
### Variable: nticks

Valor padrão: 30


`nticks` é o número de amostra de pontos usado pelas rotinas de montagem de gráfico.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `ellipse`, `explicit`, `parametric` e `polar`.
- *
`gr3d`: `parametric`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(transparent = true,
             ellipse(0,0,4,2,0,180),
             nticks = 5,
             ellipse(0,0,4,2,180,180) )$
```

<!-- category: Plotting -->
<!-- keywords: palette -->
<!-- signatures: palette -->
### Variable: palette

Valor padrão: `color`


`palette` indica como mapear os valores reais de uma matriz
passada para o objeto `image` sobre componentes de cor.


`palette` é um vetor comprimento três com componentes 
variando de -36 a +36; cada valor é um índice para uma fórmula mapeando os níveis
sobre as cores vermelho, verde e blue, respectivamente:


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
30: x/0.32-0.78125 31: 2*x-0.84     32: 4x;1;-2x+1.84;x/0.08-11.5
33: |2*x - 0.5|    34: 2*x          35: 2*x - 0.5
36: 2*x - 1
```

números negativos significam componentes negativos de cores.


`palette = gray` and `palette = color` are short cuts for
`palette = [3,3,3]` and `palette = [7,5,15]`, respectively.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo do gráfico
não é importante.


Exemplos:



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


Veja também `colorbox`.

<!-- category: Plotting -->
<!-- keywords: pic_height -->
<!-- signatures: pic_height -->
### Variable: pic_height

Valor padrão: 640


Essa é a altura do arquivo de bitmap gerado pelos terminais `png` e `jpg`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante. Pode também ser usada como um argumento da função `draw`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal   = 'png,
             pic_width  = 300,
             pic_height = 300,
             explicit(x^2,x,-1,1))$
```


Veja também `terminal`, `file_name`, e `pic_width`.

<!-- category: Plotting -->
<!-- keywords: pic_width -->
<!-- signatures: pic_width -->
### Variable: pic_width

Valor padrão: 640


Essa é a largura do arquivo de bitmap gerado pelos terminais `png` e `jpg`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante. Pode também ser usada como um argumento da função `draw`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(terminal   = 'png,
             pic_width  = 300,
             pic_height = 300,
             explicit(x^2,x,-1,1))$
```


Veja também `terminal`, `file_name`, e `pic_height`.

<!-- category: Plotting -->
<!-- keywords: point_size -->
<!-- signatures: point_size -->
### Variable: point_size

Valor padrão: 1


`point_size` escolhe o tamanho para os pontos do gráfico. Esse valor deve ser um
número não negativo.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(points(makelist([random(20),random(50)],k,1,10)),
             point_size = 5,
             points(makelist(k,k,1,20),makelist(random(30),k,1,20)))$
```

<!-- category: Plotting -->
<!-- keywords: point_type -->
<!-- signatures: point_type -->
### Variable: point_type

Valor padrão: 1


`point_type` indica como pontos isolados são mostrados; o valor dessa
opção pode ser qualquer índice inteiro maior que ou igual a -1, ou o nome de
um estilo de ponto: `$none` (-1), `dot` (0), `plus` (1), `multiply` (2),
`asterisk` (3), `square` (4), `filled_square` (5), `circle` (6),
`filled_circle` (7), `up_triangle` (8), `filled_up_triangle` (9),
`down_triangle` (10), `filled_down_triangle` (11), `diamant` (12) e
`filled_diamant` (13).


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange = [0,10],
             yrange = [0,10],
             point_size = 3,
             point_type = 1,
             points([[1,1],[5,1],[9,1]]),
             point_type = 2,
             points([[1,2],[5,2],[9,2]]),
             point_type = asterisk,
             points([[1,3],[5,3],[9,3]]),
             point_type = 4,
             points([[1,4],[5,4],[9,4]]),
             point_type = 5,
             points([[1,5],[5,5],[9,5]]),
             point_type = 6,
             points([[1,6],[5,6],[9,6]]),
             point_type = filled_circle,
             points([[1,7],[5,7],[9,7]]),
             point_type = 8,
             points([[1,8],[5,8],[9,8]]),
             point_type = filled_diamant,
             points([[1,9],[5,9],[9,9]]) )$
```

<!-- category: Plotting -->
<!-- keywords: points_joined -->
<!-- signatures: points_joined -->
### Variable: points_joined

Valor padrão: `false`


Se `points_joined` for `true`, pontos são unidos por linhas retas.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `points`.
- *
`gr3d`: `points`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange        = [0,10],
             yrange        = [0,4],
             point_size    = 3,
             point_type    = 1,
             line_type     = 3,
             points([[1,1],[5,1],[9,1]]),
             points_joined = true,
             point_type    = 3,
             line_type     = 5,
             points([[1,2],[5,2],[9,2]]),
             point_type    = 5,
             line_type     = 8,
             line_width    = 7,
             points([[1,3],[5,3],[9,3]]) )$
```

<!-- category: Plotting -->
<!-- keywords: rot_horizontal -->
<!-- signatures: rot_horizontal -->
### Variable: rot_horizontal

Valor padrão: 30


`rot_horizontal` é o ângulo (em graus) da rotação horizontal (em torno 
do eixo *z*)  para escolher o ponto de visualização em fundos gráficos tridimensionais.


O ângulo é associado ao intervalo $[0, 180]$.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(rot_vertical = 170,
             rot_horizontal = 360,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```


Veja também `rot_vertical`.

<!-- category: Plotting -->
<!-- keywords: rot_vertical -->
<!-- signatures: rot_vertical -->
### Variable: rot_vertical

Valor padrão: 60


`rot_vertical` é o ângulo (em graus) da rotação vertical (em torno 
do eixo *x*) para escolher o ponto de visualização em fundos gráficos tridimensionais.


O ângulo é associado ao intervalo $[0, 180]$.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(rot_vertical = 170,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```


Veja também `rot_horizontal`.

<!-- category: Plotting -->
<!-- keywords: surface_hide -->
<!-- signatures: surface_hide -->
### Variable: surface_hide

Valor padrão: `false`


Se `surface_hide` for `true`, partes escondidas não são mostradas no gráfico em superfícies tridimensioais.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw(columns=2,
           gr3d(explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)),
           gr3d(surface_hide = true,
                explicit(exp(sin(x)+cos(x^2)),x,-3,3,y,-3,3)) )$
```

<!-- category: Plotting -->
<!-- keywords: terminal -->
<!-- signatures: terminal -->
### Variable: terminal

Valor padrão: `screen`


Seleciona o terminal a ser usado pelo Gnuplot; os valores possíveis são:
`screen` (o valor padrão), `png`, `jpg`, `eps`, e `eps_color`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante. Pode também ser usada como um argumento da função `draw`


Exemplos:



```maxima
(%i1) load("draw")$
(%i2) /* screen terminal (default) */
      draw2d(explicit(x^2,x,-1,1))$
(%i3) /* png file */
      draw2d(terminal  = 'png,
             pic_width = 300,
             explicit(x^2,x,-1,1))$
(%i4) /* jpg file */
      draw2d(terminal   = 'jpg,
             pic_width  = 300,
             pic_height = 300,
             explicit(x^2,x,-1,1))$
(%i5) /* eps file */
      draw2d(file_name = "myfile",
             explicit(x^2,x,-1,1),
             terminal  = 'eps)$
```


Veja também `file_name`, `pic_width`, e `pic_height`.

<!-- category: Plotting -->
<!-- keywords: title -->
<!-- signatures: title -->
### Variable: title

Valor padrão: `""` (a sequência de caracteres vazia)


A opção `title` armazena uma sequência de caracteres do Maxima com o título principal de um fundo gráfico.
Por padrão, nenhum título é escrito.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(u),u,-2,2),
             title = "Exponential function")$
```

<!-- category: Plotting -->
<!-- keywords: transparent -->
<!-- signatures: transparent -->
### Variable: transparent

Valor padrão: `false`


Se `transparent` for `true`, regiões internas de poligonos são
preenchidas de acordo com `fill_color`.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr2d`: `polygon`, `rectangle`, e `ellipse`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(polygon([[3,2],[7,2],[5,5]]),
             transparent = true,
             color       = blue,
             polygon([[5,2],[9,2],[7,5]]) )$
```

<!-- category: Plotting -->
<!-- keywords: user_preamble -->
<!-- signatures: user_preamble -->
### Variable: user_preamble

Valor padrão: `""` (a sequência de caracteres vazia)


Usuários experientes de Gnuplot podem fazer uso dessa opção para ajuste fino do comportamento
do Gnuplot escolhendo opções para serem enviadas antes do comando `plot` ou do
comando `splot`.


O valor dessa opção deve ser uma sequência de caracteres ou uma lista de sequência de caracteres (um por linha).


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:


O terminal *dumb* não é suportado pelo pacote `draw`,
mas é possível escolher o terminal *dumb* fazendo uso da opção `user_preamble`,


```maxima
(%i1) load("draw")$
(%i2) draw2d(explicit(exp(x)-1,x,-1,1),
             parametric(cos(u),sin(u),u,0,2*%pi),
             user_preamble="set terminal dumb")$
```

<!-- category: Plotting -->
<!-- keywords: xlabel -->
<!-- signatures: xlabel -->
### Variable: xlabel

Valor padrão: `""` (a sequência de caracteres vazia)


A opção `xlabel` armazena uma sequência de caracteres do Maxima com o rótulo para o eixo *x*.
Por padrão, nenhum rótulo é escrito.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xlabel = "Time",
             explicit(exp(u),u,-2,2),
             ylabel = "Population")$
```


Veja também `ylabel`, e `zlabel`.

<!-- category: Plotting -->
<!-- keywords: xrange -->
<!-- signatures: xrange -->
### Variable: xrange

Valor padrão: `false`


Se `xrange` for `false`, o intevalo para a coordenada *x* é
calculado automaticamente.


Caso o usuário deseje um intervalo específico para *x*, esse intervalo deve ser fornecido como uma 
lista da forma definida pelo Maxima, como em `xrange=[-2, 3]`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xrange = [-3,5],
             explicit(x^2,x,-1,1))$
```


Veja também `yrange` e `zrange`.

<!-- category: Plotting -->
<!-- keywords: xtics -->
<!-- signatures: xtics -->
### Variable: xtics

Valor padrão: `true`


Se `xtics` for `true`, a marcação numérica será feitas sobre o eixo *x*.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) /* No tics in the x-axis */
      draw2d(xtics = false,
             explicit(exp(u),u,-2,2))$
```


Veja também `ytics`, e `ztics`.

<!-- category: Plotting -->
<!-- keywords: xu_grid -->
<!-- signatures: xu_grid -->
### Variable: xu_grid

Valor padrão: 30


`xu_grid` é o número de coordenadas da primeira variável
(`x` na forma explícita e o número de coordenadas de `u` em superfícies tridimensionais na forma paramétrica) para 
contruir a grade dos pontos de amostra.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr3d`: `explicit` e `parametric_surface`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


Veja também `yv_grid`.

<!-- category: Plotting -->
<!-- keywords: xy_file -->
<!-- signatures: xy_file -->
### Variable: xy_file

Valor padrão: `""` (a sequência de caracteres vazia)


`xy_file` é o nome do arquivo onde as coordenada serão armazenadas
após um clique com o botão do mouse e pressionar a tecla ’x’. Por padrão,
nenhuma coordenada é armazenada.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.

<!-- category: Plotting -->
<!-- keywords: ylabel -->
<!-- signatures: ylabel -->
### Variable: ylabel

Valor padrão: `""` (a sequência de caracteres vazia)


A opção `ylabel` armazena uma sequência de caracteres do Maxima com o rótulo para o eixo *y*.
Por padrão, nenhum rótulo é escrito.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(xlabel = "Time",
             ylabel = "Population",
             explicit(exp(u),u,-2,2) )$
```


Veja também `xlabel`, e `zlabel`.

<!-- category: Plotting -->
<!-- keywords: yrange -->
<!-- signatures: yrange -->
### Variable: yrange

Valor padrão: `false`


Se `yrange` for `false`, the range for the *y* coordinate is
computed automatically.


Se o usuário sesejar um intervalo específico para *y*, esse intervalo deve ser fornecido como uma 
lista da forma definida pelo Maxima, como em `yrange=[-2, 3]`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(yrange = [-2,3],
             explicit(x^2,x,-1,1),
             xrange = [-3,3])$
```


Veja também `xrange` e `zrange`.

<!-- category: Plotting -->
<!-- keywords: ytics -->
<!-- signatures: ytics -->
### Variable: ytics

Valor padrão: `true`


Se `ytics` for `true`, a marcação numérica será feitas sobre o eixo *y*.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw2d(ytics = false,
             explicit(exp(u),u,-2,2),
             xtics = false)$
```


Veja também `xtics`, e `ztics`.

<!-- category: Plotting -->
<!-- keywords: yv_grid -->
<!-- signatures: yv_grid -->
### Variable: yv_grid

Valor padrão: 30


`yv_grid` é o número de coordenadas da segunda variável
(`y` na forma explícita e o número de coordenadas de `v` em superfícies tridimensionais na forma paramétrica) para 
construir a grade dos pontos de amostra.


Essa opção afeta os seguintes objetos gráficos:


- *
`gr3d`: `explicit` e `parametric_surface`.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(xu_grid = 10,
             yv_grid = 50,
             explicit(x^2+y^2,x,-3,3,y,-3,3) )$
```


Veja também `xu_grid`.

<!-- category: Plotting -->
<!-- keywords: zlabel -->
<!-- signatures: zlabel -->
### Variable: zlabel

Valor padrão: `""` (a sequência de caracteres vazia)


A opção `zlabel` armazena uma sequência de caracteres do Maxima com o rótulo para o eixo *z*.
Por padrão, nenhum rótulo é escrito.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(zlabel = "Z variable",
             ylabel = "Y variable",
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2),
             xlabel = "X variable" )$
```


Veja também `xlabel`, e `ylabel`.

<!-- category: Plotting -->
<!-- keywords: zrange -->
<!-- signatures: zrange -->
### Variable: zrange

Valor padrão: `false`


Se `zrange` for `false`, o intervalo para a coordenada *z* é
calculado automaticamente.


Se o usuário sesejar um intervalo específico para *z*, esse intervalo deve ser fornecido como uma 
lista da forma definida pelo Maxima, como em `zrange=[-2, 3]`.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) draw3d(yrange = [-3,3],
             zrange = [-2,5],
             explicit(x^2+y^2,x,-1,1,y,-1,1),
             xrange = [-3,3])$
```


Veja também `yrange` e `zrange`.

<!-- category: Plotting -->
<!-- keywords: ztics -->
<!-- signatures: ztics -->
### Variable: ztics

Valor padrão: `true`


Se `ztics` for `true`, a marcação numérica será feitas sobre o eixo *z*.


Uma vez que essa é uma opção gráfica global, sua posição na descrição do fundo
não é importante.


Exemplo:



```maxima
(%i1) load("draw")$
(%i2) /* No tics in the z-axis */
      draw3d(ztics = false,
             explicit(sin(x^2+y^2),x,-2,2,y,-2,2) )$
```


Veja também `xtics`, e `ytics`.

