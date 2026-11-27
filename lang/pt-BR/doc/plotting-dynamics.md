## dynamics

<!-- category: Plotting -->
<!-- keywords: chaosgame -->
<!-- signatures: chaosgame([[x1, y1]...[xm, ym]], [x0, y0], b, n, ...opções...); -->
### Function: chaosgame (([[x1, y1]...[xm, ym]], [x0, y0], b, n, ...opções...);)

Implementa o então chamado jogo do caos: o ponto inicial (*x0*,
*y0*) é colocado no gráfico e então um dos *m* pontos
`[`*x1*, *y1*`]`...`[`*xm*, *ym*`]`
será selecionado de forma aleatória. O próximo ponto colocado no gráfico será sobre o
segmento que vai do ponto anteriormente colocado no gráfico ao ponto escolhido aleatóriamente, à
distância do ponto aleatório que será *b* vezes o comprimento daquele
segmento. o procedimento é repetido *n* vezes.

<!-- category: Plotting -->
<!-- keywords: evolution -->
<!-- signatures: evolution(F, y0, n, ..., opções, ...); -->
### Function: evolution ((F, y0, n, ..., opções, ...);)

Desenha *n+1* pontos em gráfico bidimensional, onde as coordenadas
horizontais dos pontos são os inteiros 0, 1, 2, ..., *n*, e
as coordenadas verticais são os valores correspondentes *y(n)* da
sequência definida pela relação de recorrência


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


com valor inicial *y(0)* igual a *y0*. *F* deve ser uma
expressão que depende somente de uma variável (no exemplo, essa variável
dependente de *y*, mas qualquer outra variável pode ser usada em lugar de *y*),
*y0* deve ser um número real e *n* deve ser um inteiro positivo.

<!-- category: Plotting -->
<!-- keywords: evolution2d -->
<!-- signatures: evolution2d([F, G], [u, v], [u0, y0], n, ..., opções, ...); -->
### Function: evolution2d (([F, G], [u, v], [u0, y0], n, ..., opções, ...);)

Mostra, em um gráfico bidimensional, os primeiros *n+1* pontos na
sequência de pontos definida por meio do sistema dinâmico discreto
bidimensional com relações de recorrência


```maxima
u(n+1) = F(u(n), v(n))    v(n+1) = G(u(n), v(n))
```


$$
\begin{cases}u_{n+1} = F(u_n, v_n) &\cr v_{n+1} = G(u_n, v_n)\end{cases}
$$


Com valores iniciais *u0* e *v0*. *F* e *G* devem ser
duas expressões que dependem somente de duas variáveis *u* e
*v*, que devem ser nomeadas explicitamente em uma lista.

<!-- category: Plotting -->
<!-- keywords: ifs -->
<!-- signatures: ifs([r1, ..., rm], [A1, ..., Am], [[x1, y1], ..., [xm, ym]], [x0, y0], n, ..., opções, ...); -->
### Function: ifs (([r1, ..., rm], [A1, ..., Am], [[x1, y1], ..., [xm, ym]], [x0, y0], n, ..., opções, ...);)

Implemanta o método de Sistemas de Funções iteradas. Esse método é similar
ao método descrito na função `chaosgame`, mas em lugar de
encolher o segmento do ponto corrente ao ponto escolhido
aleatóriamente, as duas componentes daquele segmento irão ser multiplicadas pela matrix 2 por 2
*Ai* que corresponde ao ponto escolhido aleatóriamente.


A escolha aleatória de um dos *m* pontos de atração pode ser feita com
uma distribuição de probabilidade não uniforme definida por meio dos pesos
*r1*,...,*rm*. Esses pesos são fornecidos de forma cumulativa; por exemplo se existem 3 pontos com probabilidades 0.2, 0.5 e
0.3, os pesos *r1*, *r2* e *r3* podem ser 2, 7 e 10.

<!-- category: Plotting -->
<!-- keywords: rk -->
<!-- signatures: rk(EDO, var, inicio, domain), rk([EDO1, ..., EDOm], [v1, ..., vm], [inic1, ..., inicm], domain) -->
### Function: rk (EDO, var, inicio, domain)

A primeira forma resolve numericamente uma equação diferencial  de primeira
ordem, e a segunda formaresolve um sistema de m dessas equações,
usando o método de Runge-Kutta de quarta ordem. `var` representa a variável
dependente. EDO deve ser uma expressão que dependa somente da variável  independente e da
variável dependente e defina a derivada da variável
dependente com relação à variável independente.


A variável independente é especificada com `domain`, que deve ser uma
lista dde quatro elementos como, por exemplo:


```maxima
[t, 0, 10, 0.1]
```

O primeiro elemento da lista identifica a variável independente, o
segundo e o terceiro elementos são os valores inicial e final para para aquela
variável, e o último elemento escolhe o incremento que pode ser usado
dentro daquele intervalo.


Se *m* equações estão sendo resolvidas, podem existir *m*
variáveis dependentes *v1*, *v2*, ..., *vm*. Os valores iniciais
para aquelas variáveis serão *inic1*, *inic2*, ..., *inicm*.
Ainda pode ser apenas uma variável independente definida por `domain`,
como no caso anterior. *EDO1*, ..., *EDOm* são as expressões
que definem as derivadas de cada variável dependente em
termos da variável independente. As variáveis que podem aparecer
naquelas expressões são a variável independente e quaisquer outras variáveis
dependentes. É importante fornecer as derivadas *EDO1*, ...,
*EDOm* na lista exatamente na mesma ordem usada para variáveis
dependentes; por exemplo, o terceiro elemento na lista irá ser interpretado
com a derivada da terceira variável dependente.


O programa tentará integrar as equações a partir do valor inicial
da variável independente até seu último valor, usando incrementos
constantes. Se em algum passo uma das variáveis dependentes recebe um
valor absoluto muito grande, a integração será interrompida naquele
ponto. O resultado será uma lista com tamtos elementos quantos forem o número de
iterações feitas. Cada elemento na lista de resultado é em si mesmo outra lista
comh *m*+1 elementos: o valor da variável independente, seguido
pelos valores das variáveis dependentes correspondentes àquele ponto.

<!-- category: Plotting -->
<!-- keywords: staircase -->
<!-- signatures: staircase(F, y0, n, ...opções...); -->
### Function: staircase ((F, y0, n, ...opções...);)

Desenha um diagrama em escada para a sequência definida pela relação de
recorrência


```maxima
y(n+1) = F(y(n))
```


$$
y_{n+1} = F(y_n)
$$


A interpretação e os valores permitidos dos parâmetros de entrada são os
mesmos que para a função `evolution`. Um diagrama em escada consiste
de um gráfico da função *F(y)*, juntamente com a linha
*G(y)* `=` *y*. Um segmento vertical é desenhado a partir das
point (*y0*, *y0*) on that line until the point where it
intersecções com a função *F*. A partir daquele ponto um segmento horizontal é
desenhado até encontrar o ponto (*y1*, *y1*) sobre a linha, e
o procedimento é repetido *n* vezes até que o ponto (*yn*, *yn*)
é encontrado.

