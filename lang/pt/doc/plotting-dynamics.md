## dynamics

<!-- category: Plotting -->
<!-- keywords: chaosgame -->
<!-- signatures: chaosgame([[x1, y1]...[xm, ym]], [x0, y0], b, n, ...opções...); -->
### Function: chaosgame (([[x1, y1]...[xm, ym]], [x0, y0], b, n, ...opções...);)

Usa o método designado de *jogo do caos*, para produzir fractais:
desenha-se um ponto inicial (*x0*, *y0*) e logo escolhe-se
aleatoriamente um dos *m* pontos `[`*x1*,
*y1*`]`...`[`*xm*, *ym*`]`. A seguir,
desenha-se um novo ponto que estará no segmento entre o último ponto
desenhado e o ponto que se acabou de seleccionar aleatoriamente, a uma
distância do ponto seleccionado que será *b* vezes o comprimento
do segmento. O processo repete-se *n* vezes.

<!-- category: Plotting -->
<!-- keywords: evolution -->
<!-- signatures: evolution(F, y0, n, ...opções...); -->
### Function: evolution ((F, y0, n, ...opções...);)

Desenha *n+1* pontos num gráfico bidimensional (série de tempo),
onde as coordenadas horizontais dos pontos são os números inteiros
0, 1, 2, ..., *n*, e as coordenadas verticais são os valores
*y(n)* correspondentes, obtidos a partir da relação
de recorrência


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


Com valor inicial *y(0)* igual a *y0*. *F* deverá ser uma
expressão que dependa unicamente da variável *y* (e não de *n*),
*y0* deverá ser um número real e *n* um número inteiro positivo.

<!-- category: Plotting -->
<!-- keywords: evolution2d -->
<!-- signatures: evolution2d([F, G], [x0, y0], n, ...opções...); -->
### Function: evolution2d (([F, G], [x0, y0], n, ...opções...);)

Mostra, num gráfico bidimensional, os primeiros *n+1* pontos da
sucessão definida a partir do sistema dinâmico discreto com
relações de recorrência:


```maxima
x(n+1) = F(x(n), y(n))    y(n+1) = G(x(n), y(n))
```


$$
\begin{cases}x_{n+1} = F(x_n, y_n) &\cr y_{n+1} = G(x_n, y_n)\end{cases}
$$


Com valores iniciais *x0* e *y0*. *F* e *G* deverão
ser duas expressões que dependam unicamente de *x* e *y*.

<!-- category: Plotting -->
<!-- keywords: ifs -->
<!-- signatures: ifs([r1, ..., rm], [A1, ..., Am], [[x1, y1]...[xm, ym]], [x0, y0],  -->
### Function: ifs (([r1, ..., rm], [A1, ..., Am], [[x1, y1]...[xm, ym]], [x0, y0],)

*n*, ...opções...);


Usa o método do Sistema de Funções Iteradas (IFS, em
inglês *Iterated Function System*). Esse método é semelhante
ao método descrito na função `chaosgame`, mas em
vez de aproximar o último ponto para ponto seleccionado
aleatoriamente, as duas coordenadas do último ponto multiplicam-se por
uma matriz 2 por 2 *Ai* correspondente ao ponto que tenha sido
escolhido aleatoriamente.


A selecção aleatória de um dos *m* pontos
atractivos pode se realizada com uma função de
probabilidade não uniforme, definida com os pesos
*r1*,...,*rm*. Pesos esses que deverão ser dados em forma
acumulada; por exemplo, se quiser usar 3 pontos com probabilidades
0.2, 0.5 e 0.3, os pesos *r1*, *r2* e *r3* poderiam ser 2, 7
e 10, ou qualquer outro grupo de números que estejam na mesma
proporção.

<!-- category: Plotting -->
<!-- keywords: orbits -->
<!-- signatures: orbits(F, y0, n1, n2, [x, x0, xf, xstep], ...opções...); -->
### Function: orbits ((F, y0, n1, n2, [x, x0, xf, xstep], ...opções...);)

Desenha o diagrama de órbitas duma família de sistemas
dinâmicos discretos unidimensionais, com um parâmetro *x*; esse
tipo de diagrama usa-se para mostrar as bifurcações dum
sistema discreto unidimensional.


A função *F(y)* define uma sequência que
começa com um valor inicial *y0*, igual que no caso da
função `evolution`, mas neste caso a
função também dependerá do parâmetro *x*, o
qual terá valores compreendidos no intervalo de *x0* a *xf*,
com incrementos *xstep*. Cada valor usado para o parâmetro *x*
apresenta-se no eixo horizontal. No eixo vertical apresentam-se *n2*
valores da sucessão *y(n1+1)*,..., *y(n1+n2+1)*, obtidos
após deixá-la evoluir durante *n1* iterações
iniciais.

<!-- category: Plotting -->
<!-- keywords: rk -->
<!-- signatures: rk(EDO, var, inicial, dominio), rk([EDO1, ..., EDOm], [v1, ..., vm], [inic1, ..., inicm], domínio) -->
### Function: rk (EDO, var, inicial, dominio)

A primeira forma usa-se para resolver numericamente uma
equação diferencial ordinária de primeira ordem (EDO),
e a segunda forma resolve numericamente um sistema de *m* dessas
equações, usando o método de Runge-Kutta de quarta
ordem. *var* representa a variável dependente.  EDO deverá ser
uma expressão que dependa unicamente das variáveis independente e
dependente, e define a derivada da variável dependente em
função da variável independente.


A variável independente representa-se com *domínio*,
que deverá ser uma lista com quatro elementos, como, por exemplo:


```maxima
[t, 0, 10, 0.1]
```

o primeiro elemento da lista identifica a variável independente, os
segundo e terceiro elementos são os valores inicial e final para essa
variável, e o último elemento dá o valor dos incrementos que
deverão ser usados dentro desse intervalo.


Se se estiverem a resolver *m* equações, deverá
haver *m* variáveis dependentes *v1*, *v2*, ...,
*vm*. Os valores iniciais para essas variáveis serão
*inic1*, *inic2*, ..., *inicm*. Continuará existindo
apenas uma variável independente, definida pela lista *domain*,
tal como no caso anterior. *EDO1*, ..., *EDOm* são as
expressões que definem as derivadas de cada uma das variáveis
dependentes, em função da variável independente. As
únicas variáveis que podem aparecer em cada uma dessas expressões
são a variável independente e qualquer uma das variáveis
dependentes. É importante que as derivadas *EDO1*, ..., *EDOm*
sejam colocadas na lista na mesma ordem em que forem agrupadas as
variáveis dependentes; por exemplo, o terceiro elemento da lista
será interpretado como a derivada da terceira variável dependente.


O programa tenta integrar as equações desde o valor
inicial da variável independente, até o valor final, usando
incrementos fixos. Se em algum passo uma das variáveis dependentes
atingir um valor absoluto muito elevado, a integração
será interrompida nesse ponto. O resultado será uma lista com um
número de elementos igual ao número de iterações
realizadas. Cada elemento na lista de resultados é também uma lista
com *m*+1 elementos: o valor da variável independente, seguido dos
valores das variáveis dependentes nesse ponto.

<!-- category: Plotting -->
<!-- keywords: staircase -->
<!-- signatures: staircase(F, y0, n, ...opções...); -->
### Function: staircase ((F, y0, n, ...opções...);)

Desenha um diagrama de degraus (ou diagrama de teia de aranha) para a
sucessão definida pela equação de recorrência


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


A interpretação e valores permitidos dos parâmetros de
entrada é igual que para a função `evolution`. Um
diagrama de degraus consiste num gráfico da função
*F(y)*, junto com a recta *G(y)* `=`
*y*. Começa-se por desenhar um segmento vertical desde
o ponto (*y0*, *y0*) na recta, até o ponto de
intersecção com a função *F*. A
seguir, desde esse ponto desenha-se um segmento horizontal até o ponto
de intersecção com a recta, (*y1*, *y1*); o
processo repete-se *n* vezes até alcançar o ponto
(*yn*, *yn*).

