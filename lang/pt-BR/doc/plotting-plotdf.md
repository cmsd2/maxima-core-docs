## plotdf

<!-- category: Plotting -->
<!-- keywords: plotdf -->
<!-- signatures: plotdf(dydx, ...opções...), plotdf([dxdt, dydt], ...opções...) -->
### Function: plotdf (dydx, ...opções...)

Mostra um campo de direção em duas dimensões *x* e *y*.


*dydx*, *dxdt* e *dydt* são expressões que dependem
de *x* e *y*. Adicionalmente para essas duas variáveis, as
expressões podem também depender de um conjunto de parâmetros, com valores
numéricos fornecidos com os `parâmetros` opção (a sintaxe de opção é
fornecida abaixo), ou com um intervalo de valores permitidos especificados por meio de uma
opção *sliders*.


Muitas outras opções podem ser fornecidas dentro do comando, ou selecionadas no
menu. Curvas integrais podem ser obtidas por meio de um clique no gráfico, ou
com a opção `trajectory_at`. A direção da integração
pode ser controlada com a opção `direction`, que pode ter
valores de *forward* (adiante), *backward*(para trás) or *both* (ambos). O número de
passos de integração é fornecido por meio de `nsteps` e o intervalo de tempo
entre eles é escolhido com a opção `tstep`. O método de Adams
Moulton é usado para a integração; é também possível alternar para um
método adaptativo de Runge-Kutta de quarta ordem.


**Menu da janela do gráfico:**


O menu na janela do gráfico tem as seguintes opções: *Zoom*, irá
modificar o comportamento do mouse de forma que seja permitido a você aproximar uma
região do gráfico por meio de um clique nessa região como o botão esquerdo. Cada clique próximo a um
ponto do gráfico amplia esse gráfico, mantendo o contro no ponto onde você
clicou. Mantendo a tecla Shift pressioada enquanto clica, afasta para a
ampliação anterior. Para continuar calculando trajetórias quando você clica
sobre um ponto, selecione *Integrate* a partir do menu.


A opção *Config* no menu pode ser usada para mudar a(s) EDO(s) em
uso e para várias outras escolhas. Após as mudanças de configuração serem feitas,
a opção do menu *Replot* estará selecionada, para ativar as novas
escolhas.  Se um par de coordenadas for fornecido em um campo
*Trajectory at* na caixa de diálogo *Config* do menu, e a
tecla enter fo pressionada, uma nova curva integral será mostrada,
adicionalmente com as outras já mostradas. Quando *Replot* está selecionada, somente
a última curva integral fornecida será mostrada.


Mantendo o botão direito do mouse pressionado enquanto o cursor é movido, pode ser
usado para arrastar as laterais do gráfico para cima ou para baixo. Parâmetros
adicionais tais como o número de passos, o valor inicial de *t*
e os centros de x e y e raios, podem ser escolhidos no menu Config.


Uma cópia do gráfico pode ser impressa para uma impressora Postscript, ou gravada como um
arquivo postscript, usando a opção *Save* do menu. Para alternar entre
imprimir e gravar para um arquivo Postscript, *Print Options* pode ser
selecionada na janela de diálogo de *Config*. Após as escolhas na
janela de diálogo *Save* serem fornecidas, "Save” deve ser selecionada no primeiro
menu, para cirar o arquivo ou imprimir o gráfico.


**Opções de gráfico:**


O comando `plotdf` pode incluir muitos comandos, cada comando é
uma lista de dois ou mais itens.  O primeiro item é o nome da opção,
e o restante compreende o valor ou valores atribuídos à opção.


As opçõesque são reconhecidas por `plotdf` são as seguintes:



- *
*tstep* define o comprimento dos incrementos sobre a
variável independente *t*, usado para calcular uma curva integral. Se somente
uma expressão *dydx* for fornecida a `plotdf`, a variável
*x* será diretamente proporcional a *t*.
O valor padrão é 0.1.
- *
*nsteps* define o número de passos de comprimento `tstep`
que será usando para a variável independente, para calcular uma curva
integral.
O valor padrão é 100.
- *
*direction* define a direção da variável
independente que será seguida para calcular uma curva integral. Possíveis
valores são `forward`, para fazer a variável independente aumentar
`nsteps` vezes, com incrementos de `tstep`, `backward`, para
fazer a variável independente diminuir, ou `both` que irá conduzir a
um curva integral que amplia `nsteps` adiante, e `nsteps`
para trás. As palavras chave `right` e `left` podem ser usadas como
sinonimos para `forward` e `backward`.
O valor padrão é `both`.
- *
*tinitial* define o valor inicial da variável *t* usada
para calcular curva integral. Uma vez que equações diferenciais forem
autônomas, aquela esxolha irá aparecer somente no gráfico das curvas como
funções de *t*. 
O valor padrão é 0.
- *
*versus_t* é usado para criar uma segunda janela de gráfico, com um
gráfico de uma curva integral, como duas funções *x*, *y*, da
variável independente *t*. Se para `versus_t` for atribuído qualquer valor
diferente de 0, a segunda janela de gráfico será mostrada. A segunda
janela de gráfico inclui outro menu, semelhante ao menu da janela de gráfico
principal.
O valor padrão é 0.
- *
*trajectory_at* define as coordenadas *xinitial* e
*yinitial* para o ponto de partida de uma curva integral.
A opção está vazia por padrão.
- *
*parameters* define uma lista de parâmetros, e seus
valores numéricos, usados na definição das equações
diferenciais. O nome e valores dos parâmetros devem ser fornecidos em uma
sequência de caracteres com uma sequência de pares  `nome=valor` separados por vírgula.
- *
*sliders* define uma lista de parâmetros que será modificada
interativamente usando botões de deslizamento, e o intervalo de variação desses
parâmetros. Os nomes e intervalos dos parâmetros devem ser fornecidos in a
sequência de caracteres com uma sequência de elementos  `name=min:max` separados por vírgula.
- *
*xfun* define uma sequência de caracteres com uma sequência de funções separadas com
ponto e vírgula *x* para serem mostradas, no topo do campo de direção.
Essas funções irão ser passadas pelo Tcl e não pelo Maxima.
- *
*xradius* é metade do comprimento do intervalo dos valores que
irão ser mostrados na direção x.
O valor padrão é 10.
- *
*yradius* é metade do comprimento do intervalo dos valores que
irão ser mostrados na direção y.
O valor padrão é 10.
- *
*xcenter* é a coordenada x do ponto no centro do
gráfico.
O valor padrão é 0.
- *
*ycenter* é a coordenada y do ponto no centro do
gráfico.
O valor padrão é 0.
- *
*width* define a largura da janela do gráfico, em pixels.
O valor padrão é 500.
- *
*height* define a altura da janela do gráfico, em pixels.
O valor padrão é 500.


**Exemplos:**


NOTA: Dependendo da interface usada para executar o Maxima, as funções que
usam `openmath`, em particular `plotdf`, podem possivelmente disparar um erro se
erminarem com ponto e vírgula e não com um sinal de dólar. Para evitar
problemas, usamos um sinal de dólar em todos os exemplos abaixo.

  

- *
Para mostrar o campo de direção da equação diferencial $y' = exp(-x) + y$ e a solução que vai em toda a extensão do intervalo $(2, -0.1)$:

```maxima
(%i1) load("plotdf")$
(%i2) plotdf(exp(-x)+y,[trajectory_at,2,-0.1]);
```

![./figures/plotdf1](./figures/plotdf1.png)
- *
Para obter o campo de direção para a equação $diff(y,x) = x - y^2$ e a solução com condição inicial $y(-1) = 3$, podemos usar o comando:

```maxima
(%i3) plotdf(x-y^2,[xfun,"sqrt(x);-sqrt(x)"],
          [trajectory_at,-1,3], [direction,forward],
          [yradius,5],[xcenter,6]);
```
O gráfico também mostra a função $y = sqrt(x)$. 

![./figures/plotdf2](./figures/plotdf2.png)
- *
O seguinte exemplo mostra o campo de direção de um oscilador harmônico,
definido pelas duas equações $dx/dt = y$ e $dy/dt = -k*x/m$,
e a curva integral em todo o intervalo $(x,y) = (6,0)$, com um botão de deslizamento que
irá permitir a você mudar o valor de $m$ interativamente ($k$ está
fixado em 2):

```maxima
(%i4) plotdf([y,-k*x/m],[parameters,"m=2,k=2"],
            [sliders,"m=1:5"], [trajectory_at,6,0]);
```

![./figures/plotdf3](./figures/plotdf3.png)
- *
Para montar o gráfico do campo de direção da equação de Duffing, $m*x''+c*x'+k*x+b*x^3 = 0$, introduzimos a variável $y=x'$ e usamos:

```maxima
(%i5) plotdf([y,-(k*x + c*y + b*x^3)/m],
              [parameters,"k=-1,m=1.0,c=0,b=1"],
              [sliders,"k=-2:2,m=-1:1"],[tstep,0.1]);
```

![./figures/plotdf4](./figures/plotdf4.png)
- *
O campo de direção para um pêdulo amortecido, incluindo a
solução para as condições iniciais fornecidas, com um botão de deslizamento que
pode ser usado para mudar o valor da massa $m$, e com um gráfico das
duas  variáveis de estado como uma função do tempo:

```maxima
(%i6) plotdf([y,-g*sin(x)/l - b*y/m/l],
         [parameters,"g=9.8,l=0.5,m=0.3,b=0.05"],
         [trajectory_at,1.05,-9],[tstep,0.01],
         [xradius,6],[yradius,14],
         [xcenter,-4],[direction,forward],[nsteps,300],
         [sliders,"m=0.1:1"], [versus_t,1]);
```

![./figures/plotdf5](./figures/plotdf5.png)![./figures/plotdf6](./figures/plotdf6.png)

