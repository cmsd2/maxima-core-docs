## plotdf

<!-- category: Plotting -->
<!-- keywords: plotdf -->
<!-- signatures: plotdf(dydx, ...opções...), plotdf([dxdt, dydt], ...opções...) -->
### Function: plotdf (dydx, ...opções...)

Desenha um campo de direcções em duas
dimensões *x* e *y*.


*dydx*, *dxdt* e *dydt* são expressões que dependem de
*x* e *y*. Para além dessas duas variáveis, as duas
expressões podem depender de um conjunto de parâmetros, com valores
numéricos que são dados por meio da opção
`parameters` (a sintaxe dessa opção explica-se mais
para a frente), ou com um intervalo de possíveis valores
definidos com a opção *sliders*.


Várias outras opções podem incluirem-se dentro do
comando, ou serem seleccionadas no menú.  Clicando num ponto do
gráfico faz com que seja desenhada a curva integral que passa por esse
ponto; o mesmo pode ser feito dando as coordenadas do ponto com a
opção `trajectory_at` dentro do comando plotdf. A
direcção de integração pode controlar-se
com a opção `direction`, que aceita valores de
*forward*, *backward* ou *both*. O número de passos
realizados na integração numérica controla-se com a
opção `nsteps` e o incremento do tempo em cada
passo com a opção `tstep`. Usa-se o método de
Adams Moulton para fazer a integração numérica;
também é possível mudar para o método de Runge-Kutta
de quarta ordem com ajuste de passos.


**Menú da janela do gráfico:**


O menú da janela gráfica inclui as seguintes opções:
*Zoom*, que permite mudar o comportamento do rato, de maneira que
servirá para fazer zoom na região do gráfico clicando com o
botão esquerdo. Cada clic alarga a imagem mantendo no centro dela o
ponto onde se clicou.  Mantendo carregada a tecla Shift enquanto
se faz clic, faz diminuir o tamanho. Para continuar a desenhar
trajectórias com um clic, selecciona-se a opção
*Integrate* do menú.


A opção *Config* do menú pode usar-se para mudar
a(s) EDO(S) e fazer alguns outros ajustes. Após ter feito alguma
alteração, deverá usar a opção
*Replot* para activar as novas configurações.  Se
introduzir duas coordenadas no campo *Trajectory at* do menú de
diálogo do *Config*, e a seguir carregar na tecla Enter,
será acrescentada mais uma curva integral.  Se seleccionar a
opção *Replot*, só será apresentada a última
curva integral seleccionada.


Mantendo o botão direito carregado enquanto se desloca o cursor,
poderá arrastar o gráfico na horizontal e na vertical.  Outros
parâmetros, por exemplo, o número de passos, o valor inicial de
*t*, as coordenadas do centro e o raio, podem ser alterados no
sub-menú da opção *Config*.


Com a opção *Save*, pode imprimir-se o
gráfico numa impressora Postscript ou gravar uma cópia num ficheiro
Postscript. Para optar entre impressão ou gravação em
ficheiro, selecciona-se *Print Options* na janela de diálogo de
*Config*. Após ter preenchido os campos da janela de diálogo de
*Save*, será necessário seleccionar a opção
*Save* do primeiro menú para criar o ficheiro ou imprimir o
gráfico.


**Opções gráficas:**


A função `plotdf` admite varias
opções, cada uma sendo uma lista de duas ou mais
elementos. O primeiro elemento é o nome da opção, e o
resto estará formado pelos argumentos para essa opção.


A função `plotdf` reconhece as seguintes
opções:



- *
*tstep* estabelece a amplitude dos
incrementos da variável independente *t*, utilizados para calcular
as curvas integrais. Se for dada só uma expressão *dydx*, a
variável *x* será directamente proporcional a *t*.
O valor por omissão é  0.1.
- *
*nsteps* estabelece o número de passos de
comprimento `tstep` que se utilizarão na variável independente
para calcular a curva integral.
O valor por omissão é 100.
- *
*direction* estabelece a
direcção da variável independente que será seguida
para calcular uma curva integral.  Os valores possí são:
`forward`, para fazer que a variável independente aumente
`nsteps` vezes, com incrementos `tstep`; `backward`, para
fazer que a variável independente diminua; `both`, para estender
a curva integral `nsteps` passos para a frente e `nsteps`
passos para atrás.  As palavras `right` e `left` podem serem
usadas como sinónimos de `forward` e `backward`.
O valor por omissão é `both`.
- *
*tinitial* estabelece o valor inicial da
variável *t* utilizado para calcular curvas integrais. Já que as
equações diferenciais são autónomas, esta
opção só aparecerá nos gráficos das curvas em
função de *t*.
O valor por omissão é 0.
- *
*versus_t* utiliza-se para criar uma segunda
janela gráfica, com o gráfico de uma curva integral, como duas
funções *x*, *y*, de variável independente
*t*. Se for dado a `versus_t` qualquer valor diferente de 0,
mostrar-se-á a segunda janela gráfica, que inclui outro menú,
similar ao da janela principal.
O valor por omissão é 0.
- *
*trajectory_at* estabelece as coordenadas
*xinitial* e *yinitial* para o ponto inicial da curva integral.
Não tem atribuído nenhum valor por omissão.
- *
*parameters* estabelece uma lista de
parâmetros, junto com os seus valores numéricos, que são
utilizados na definição da equação
diferencial. Os nomes dos parâmetros e os seus valores devem
escrever-se em formato de cadeia de caracteres como uma sequência de
pares `nome=valor` separados por vírgulas.
- *
*sliders* estabelece uma lista de
parâmetros que poderão ser alterados interactivamente usando barras
com sliders, assim como os intervalos de variação dos
ditos parâmetros.  Os nomes dos parâmetros e os seus intervalos
devem escrever-se em formato de cadeia de caracteres como uma
sequência de pares `nome=min:max` separados por
vírgulas.
- *
*xfun* estabelece uma cadeia de caracteres
com funções de *x* separadas por ponto e
vírgula para ser representadas por cima do campo de
direcções. Essas funções serão
interpretadas por Tcl, e não por Maxima.
- *
*xradius* é metade do comprimento do
intervalo de valores a representar na direcção x.
O valor por omissão é 10.
- *
*yradius* é metade do comprimento do
intervalo de valores a representar na direcção y.
O valor por omissão é 10.
- *
*xcenter* é a coordenada x do ponto
situado no centro do gráfico.
O valor por omissão é 0.
- *
*ycenter* é a coordenada y do ponto
situado no centro do gráfico.
O valor por omissão é 0.
- *
*width* estabelece a largura da janela gráfica em
pixels.
O valor por omissão é 500.
- *
*height* estabelece a altura da janela gráfica em
pixels.
O valor por omissão é 500.


**Exemplos:**


NOTA: Em alguns casos, dependendo da interface usada para executar o
Maxima, as funções que usam `openmath`, em
particular `plotdf`, podem desencadear um bug se terminarem em
ponto e vírgula, e não com o símbolo de
dólar. Para evitar problemas, usaremos o símbolo de
dóla nos exemplos a seguir.



- *
Para mostrar o campo de direcções da
equação diferencial $y' = exp(-x) + y$ e a
solução que passa por $(2, -0.1)$:

```maxima
(%i1) load("plotdf")$
(%i2) plotdf(exp(-x)+y,[trajectory_at,2,-0.1]);
```

![plotdf1](figures/plotdf1.png)
- *
Para mostrar o campo de direcções da
equação $diff(y,x) = x - y^2$ e a
solução com condição inicial $y(-1) = 3$, pode utilizar-se o comando:

```maxima
(%i3) plotdf(x-y^2,[xfun,"sqrt(x);-sqrt(x)"],
          [trajectory_at,-1,3], [direction,forward],
          [yradius,5],[xcenter,6]);
```
O gráfico também mostra a função $y = sqrt(x)$.

![plotdf2](figures/plotdf2.png)
- *
O exemplo seguinte mostra o campo de direcções de um
oscilador harmónico, definido pelas equações
$dx/dt = y$ e $dy/dt = -k*x/m$, e a curva integral que passa
por $(x,y) = (6,0)$, com uma barra de slider que permitirá mudar
o valor de $m$ interactivamente ($k$ permanecerá fixo em 2):

```maxima
(%i4) plotdf([y,-k*x/m],[parameters,"m=2,k=2"],
            [sliders,"m=1:5"], [trajectory_at,6,0]);
```

![plotdf3](figures/plotdf3.png)
- *
Para representar o campo de direcções da
equação de Duffing, $m*x''+c*x'+k*x+b*x^3 = 0$,
introduz-se a variável $y=x'$ e faz-se:

```maxima
(%i5) plotdf([y,-(k*x + c*y + b*x^3)/m],
              [parameters,"k=-1,m=1.0,c=0,b=1"],
              [sliders,"k=-2:2,m=-1:1"],[tstep,0.1]);
```

![plotdf4](figures/plotdf4.png)
- *
O campo de direcções dum pêndulo amortecido, incluindo
a solução para condições iniciales
dadas, com uma barra de slider que pode usar-se para mudar o valor da
masa, $m$, e com o gráfico das duas variáveis de estado em
função do tempo:

```maxima
(%i6) plotdf([y,-g*sin(x)/l - b*y/m/l],
         [parameters,"g=9.8,l=0.5,m=0.3,b=0.05"],
         [trajectory_at,1.05,-9],[tstep,0.01],
         [xradius,6],[yradius,14],
         [xcenter,-4],[direction,forward],[nsteps,300],
         [sliders,"m=0.1:1"], [versus_t,1]);
```

![plotdf5](figures/plotdf5.png)
![plotdf6](figures/plotdf6.png)

