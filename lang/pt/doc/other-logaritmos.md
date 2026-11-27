## Logaritmos

<!-- category: Other -->
<!-- keywords: %e_to_numlog -->
<!-- signatures: %e_to_numlog -->
### Variable: %e_to_numlog

Valor por omissão: `false`


Quando `true`, sendo `r` algum número racional, e `x`
alguma expressão, `%e^(r*log(x))` será simplificado em
`x^r` .  Note-se que o comando `radcan` também faz essa
transformação, assim como algumas transformações mais
complicadas.  O comando `logcontract` *contrai* expressões
contendo `log`.

<!-- category: Other -->
<!-- keywords: li -->
<!-- signatures: li[s](z) -->
### Function: li ([s](z))

Representa a função polilogaritmo de ordem *s*
e argumento *z*, definida por meio da série infinita



```maxima
inf
                                 ====   k
                                 \     z
                        Li (z) =  >    --
                          s      /      s
                                 ====  k
                                 k = 1
```


`li [1]` é `- log (1 - z)`.  `li [2]` e `li [3]`
são as funções dilogaritmo e
trilogaritmo, respectivamente.


Quando a ordem for 1, o polilogaritmo simplifica para
`- log (1 - z)`, o qual por sua vez simplifica para um valor
numérico se *z* for um número em ponto flutuante real ou
complexo ou o sinalizador de avaliação `numer` estiver
presente.


Quando a ordem for 2 ou 3, o polilogaritmo simplifica
para um valor numérico se *z* for um número real em ponto
flutuante ou o sinalizador de avaliação `numer` estiver
presente.


Exemplos:














```maxima
(%i1) assume (x > 0);
(%o1)                        [x > 0]
(%i2) integrate ((log (1 - t)) / t, t, 0, x);
(%o2)                       - li (x)
                                2
(%i3) li [2] (7);
(%o3)                        li (7)
                               2
(%i4) li [2] (7), numer;
(%o4)        1.24827317833392 - 6.113257021832577 %i
(%i5) li [3] (7);
(%o5)                        li (7)
                               3
(%i6) li [2] (7), numer;
(%o6)        1.24827317833392 - 6.113257021832577 %i
(%i7) L : makelist (i / 4.0, i, 0, 8);
(%o7)   [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
(%i8) map (lambda ([x], li [2] (x)), L);
(%o8) [0, .2676526384986274, .5822405249432515, 
.9784693966661848, 1.64493407, 2.190177004178597
 - .7010261407036192 %i, 2.374395264042415
 - 1.273806203464065 %i, 2.448686757245154
 - 1.758084846201883 %i, 2.467401098097648
 - 2.177586087815347 %i]
(%i9) map (lambda ([x], li [3] (x)), L);
(%o9) [0, .2584613953442624, 0.537213192678042, 
.8444258046482203, 1.2020569, 1.642866878950322
 - .07821473130035025 %i, 2.060877505514697
 - .2582419849982037 %i, 2.433418896388322
 - .4919260182322965 %i, 2.762071904015935
 - .7546938285978846 %i]
```

<!-- category: Other -->
<!-- keywords: log -->
<!-- signatures: log(x) -->
### Function: log (x)

Representa o logaritmo natural (base $e$) de
*x*.


Maxima não possui uma função interna para
logaritmo de base 10 ou de outras bases. `log10(x) := log(x) / log(10)` é uma definição útil.


A simplificação e avaliação de logaritmos
são governadas por vários sinalizadores globais:


`logexpand` - faz com que `log(a^b)` se transfome em
`b*log(a)`. Se `logexpand` tiver o valor `all`,
`log(a*b)` irá também simplificar para `log(a)+log(b)`.
Se `logexpand` for igual a `super`, então
`log(a/b)` irá também simplificar para `log(a)-log(b)`
para números racionais `a/b`, `a#1` (`log(1/b)`,
para `b` inteiro, sempre simplifica).  Se `logexpand` for
igaul a `false`, todas essas simplificações irão
ser desabilitadas.


`logsimp` - se tiver valor `false`, não será feita nenhuma
simplificação de `%e` para um expoente contendo
`log`’s.


`lognumer` - se tiver valor `true`, os argumentos negativos
em ponto flutuante para `log` irá sempre ser convertidos para
seu valor absoluto antes que `log` seja calculado. Se
`numer` for também `true`, então argumentos negativos
inteiros para `log` irão também ser convertidos para os seus
valores absolutos.


`lognegint` - se tiver valor `true`, implementa a regra
`log(-n)` -> `log(n)+%i*%pi` para `n` um inteiro
positivo.


`%e_to_numlog` - quando for igual a `true`,
`%e^(r*log(x))`, sendo `r` algum número racional, e
`x` alguma expressão, será simplificado para
`x^r`. Note-se que o comando `radcan` também faz essa
transformação, e outras transformações mais complicadas
desse género.


O comando `logcontract` "contrai" expressões
contendo `log`.

<!-- category: Other -->
<!-- keywords: logabs -->
<!-- signatures: logabs -->
### Variable: logabs

Valor por omissão: `false`


No cálculo de primitivas em que sejam gerados
logaritmos, por exemplo, `integrate(1/x,x)`, a
resposta será dada em termos de `log(abs(...))` se
`logabs` for `true`, mas em termos de `log(...)` se
`logabs` for `false`. Para integrais definidos, usa-se
`logabs:true`, porque nesse caso muitas vezes é necessário
calcular a primitiva nos extremos.

<!-- category: Other -->
<!-- keywords: logarc -->
<!-- signatures: logarc(expr) -->
### Variable: logarc

Quando a variável global `logarc` for igual a `true`, as
funções trigononométricas inversas, circulares e
hiperbólicas, serão substituídas por suas
funções logarítmicas equivalentes. O valor
padrão de `logarc` é `false`.


A função `logarc(expr)` realiza essa
substituição para uma expressão *expr* sem modificar o
valor da variável global `logarc`.

<!-- category: Other -->
<!-- keywords: logconcoeffp -->
<!-- signatures: logconcoeffp -->
### Variable: logconcoeffp

Valor por omissão: `false`


Controla quais coeficientes são contraídos quando se
usa `logcontract`. Poderá ser igual ao nome de uma função
de um argumento. Por exemplo, se quiser gerar raízes
quadradas, pode fazer `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$`. E assim,
`logcontract(1/2*log(x));` produzirá `log(sqrt(x))`.

<!-- category: Other -->
<!-- keywords: logcontract -->
<!-- signatures: logcontract(expr) -->
### Function: logcontract (expr)

Examina recursivamente a expressão *expr*, transformando
subexpressões da forma `a1*log(b1) + a2*log(b2) + c` em
`log(ratsimp(b1^a1 * b2^a2)) + c`







```maxima
(%i1) 2*(a*log(x) + 2*a*log(y))$
(%i2) logcontract(%);
                                 2  4
(%o2)                     a log(x  y )
```


Se fizer `declare(n,integer);` então
`logcontract(2*a*n*log(x));` produzirá
`a*log(x^(2*n))`. Os coeficientes que *contraem* dessa
maneira são os que, tal como 2 e `n` neste exemplo, satisfazem
`featurep(coeficiente,integer)`. O utilizador pode controlar
quais coeficientes são contraídos, dando à variável
`logconcoeffp` o nome de uma função de um argumento. Por
exemplo, se quiser gerar raízes quadradas, pode fazer
`logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) or ratnump(m)$`. E assim, `logcontract(1/2*log(x));` produzirá
`log(sqrt(x))`.

<!-- category: Other -->
<!-- keywords: logexpand -->
<!-- signatures: logexpand -->
### Variable: logexpand

Valor por omissão: `true`


Faz com que `log(a^b)` se transfome em `b*log(a)`. Se
`logexpand` tiver o valor `all`, `log(a*b)` irá
também simplificar para `log(a)+log(b)`.  Se `logexpand`
for igual a `super`, então `log(a/b)` irá também
simplificar para `log(a)-log(b)` para números racionais
`a/b`, `a#1` (`log(1/b)`, para `b` inteiro, sempre
simplifica).  Se `logexpand` for igaul a `false`, todas
essas simplificações irão ser desabilitadas.

<!-- category: Other -->
<!-- keywords: lognegint -->
<!-- signatures: lognegint -->
### Variable: lognegint

Valor por omissão: `false`


Se for igual a `true`, implementa a regra `log(-n)` ->
`log(n)+%i*%pi` para `n` um inteiro positivo.

<!-- category: Other -->
<!-- keywords: lognumer -->
<!-- signatures: lognumer -->
### Variable: lognumer

Valor por omissão: `false`


Se tiver valor `true`, os argumentos negativos em ponto flutuante
para `log` irá sempre ser convertidos para seu valor absoluto
antes que `log` seja calculado. Se `numer` for também
`true`, então argumentos negativos inteiros para `log`
irão também ser convertidos para os seus valores absolutos.

<!-- category: Other -->
<!-- keywords: logsimp -->
<!-- signatures: logsimp -->
### Variable: logsimp

Valor por omissão: `true`


Se tiver valor `false`, não será feita nenhuma
simplificação de `%e` para um expoente contendo
`log`’s.

<!-- category: Other -->
<!-- keywords: plog -->
<!-- signatures: plog(x) -->
### Function: plog (x)

Representa o ramo principal dos logaritmos naturais no
plano complexo, com `-%pi` < `carg(x)` <= `+%pi`.

