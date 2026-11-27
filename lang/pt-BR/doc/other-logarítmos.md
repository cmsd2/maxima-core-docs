## Logarítmos

<!-- category: Other -->
<!-- keywords: %e_to_numlog -->
<!-- signatures: %e_to_numlog -->
### Variable: %e_to_numlog

Valor padrão: `false`


Quando `true`, sendo `r` algum número racional, e
`x` alguma expressão, `%e^(r*log(x))` será simplificado em `x^r` .
Note-se que o comando `radcan` também faz essa transformação,
e transformações mais complicadas desse tipo também.
O comando `logcontract` "contrai" expressões contendo `log`.

<!-- category: Other -->
<!-- keywords: li -->
<!-- signatures: li[s](z) -->
### Function: li ([s](z))

Representa a função polilogarítmo de ordem *s* e argumento *z*,
definida por meio de séries infinitas



```maxima
inf
                                 ====   k
                                 \     z
                        Li (z) =  >    --
                          s      /      s
                                 ====  k
                                 k = 1
```


`li [1]` é `- log (1 - z)`.
`li [2]` e `li [3]` são as funções dilogarítmo e trilogarítmo, respectivamente.


Quando a ordem for 1, o polilogarítmo simplifica para `- log (1 - z)`,
o qual por sua vez simplifica para um valor numérico
se *z* for um número em ponto flutuante real ou complexo ou o sinalizador de avaliação `numer` estiver presente.


Quando a ordem for 2 ou 3,
o polilogarítmo simplifica para um valor numérico
se *z* for um número real em ponto flutuante
ou o sinalizador de avaliação `numer` estiver presente.


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

Representa o logarítmo natural (base $e$) de *x*.


Maxima não possui uma função interna para logarítmo de base 10 ou de outras bases.
`log10(x) := log(x) / log(10)` é uma definição útil.


Simplificação e avaliação de logarítmos são governadas por muitos sinalizadores globais:


`logexpand` - faz com que `log(a^b)` torne-se `b*log(a)`.
Se `logexpand` for escolhida para `all`, `log(a*b)` irá também simplificar para `log(a)+log(b)`.
Se `logexpand` for escolhida para `super`, então `log(a/b)` irá também simplificar para `log(a)-log(b)` para números
racionais `a/b`, `a#1`.  (`log(1/b)`, para `b` inteiro, sempre simplifica).  Se
`logexpand` for escolhida para `false`, todas essas simplificações irão ser desabilitadas.


`logsimp` - se `false` então nenhuma simplificação de `%e` para um expoente
contendo `log`’s é concluída.


`lognumer` - se `true` então argumentos negativos em ponto flutuante para
`log` irá sempre ser convertido para seu valor absoluto antes que `log` seja
tomado.  Se `numer` for também `true`, então argumentos negativos inteiros para `log`
irão também ser convertidos para seu valor absoluto.


`lognegint` - se `true` implementa a regra `log(-n)` ->
`log(n)+%i*%pi` para `n` um inteiro positivo.


`%e_to_numlog` - quando `true`, `r` sendo algum número racional, e
`x` alguma expressão, `%e^(r*log(x))` será simplificado em
`x^r` .  Note-se que o comando `radcan` também
faz essa transformação, e transformações mais complicadas desse tipo também.
O comando `logcontract` "contrai" expressões contendo `log`.

<!-- category: Other -->
<!-- keywords: logabs -->
<!-- signatures: logabs -->
### Variable: logabs

Valor padrão: `false`


Quando fazendo integração indefinida onde
logs são gerados, e.g. `integrate(1/x,x)`, a resposta é dada em
termos de `log(abs(...))` se `logabs` for `true`, mas em termos de `log(...)` se
`logabs` for `false`.  Para integração definida, a escolha `logabs:true` é
usada, porque aqui "avaliação" de integral indefinida nos
extremos é muitas vezes necessária.

<!-- category: Other -->
<!-- keywords: logarc -->
<!-- signatures: logarc(expr) -->
### Variable: logarc

Quando a variável global `logarc` for `true`,
funções circulares inversas e funções hiperbólicas serão convertidas
em funções logarítimicas equivalentes.
O valor padrão de `logarc` é `false`.


A função `logarc(expr)` realiza aquela substituíção para
uma expressão *expr*
sem modificar o valor da variável global `logarc`.

<!-- category: Other -->
<!-- keywords: logconcoeffp -->
<!-- signatures: logconcoeffp -->
### Variable: logconcoeffp

Valor padrão: `false`


Controla quais coeficientes são
contraídos quando usando `logcontract`.  Pode ser escolhida para o nome de uma
função predicado de um argumento.  E.g. se você gosta de gerar
raízes quadradas, você pode fazer `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) ou ratnump(m)$` .  Então
`logcontract(1/2*log(x));` irá fornecer `log(sqrt(x))`.

<!-- category: Other -->
<!-- keywords: logcontract -->
<!-- signatures: logcontract(expr) -->
### Function: logcontract (expr)

Recursivamente examina a expressão *expr*, transformando
subexpressões da forma `a1*log(b1) + a2*log(b2) + c` em
`log(ratsimp(b1^a1 * b2^a2)) + c`







```maxima
(%i1) 2*(a*log(x) + 2*a*log(y))$
(%i2) logcontract(%);
                                 2  4
(%o2)                     a log(x  y )
```


Se você faz `declare(n,integer);` então `logcontract(2*a*n*log(x));` fornece
`a*log(x^(2*n))`.  Os coeficientes que "contraem" dessa maneira são
aqueles tais que 2 e `n` que satisfazem
`featurep(coeff,integer)`.  O usuário pode controlar quais coeficientes são
contraídos escolhendo a opção `logconcoeffp` para o nome de uma
função predicado de um argumento.  E.g. se você gosta de gerara
raízes quadradas, você pode fazer `logconcoeffp:'logconfun$ logconfun(m):=featurep(m,integer) ou ratnump(m)$` .  Então
`logcontract(1/2*log(x));` irá fornecer `log(sqrt(x))`.

<!-- category: Other -->
<!-- keywords: logexpand -->
<!-- signatures: logexpand -->
### Variable: logexpand

Valor padrão: `true`


Faz com que `log(a^b)` torne-se `b*log(a)`.  Se
for escolhida para `all`, `log(a*b)` irá também simplificar para `log(a)+log(b)`.  Se
for escolhida para `super`, então `log(a/b)` irá também simplificar para `log(a)-log(b)` para
números racionais `a/b`, `a#1`.  (`log(1/b)`, para `b` inteiro, sempre
simplifica).  Se for escolhida para `false`, todas essas simplificações irão
ser desabilitadas.

<!-- category: Other -->
<!-- keywords: lognegint -->
<!-- signatures: lognegint -->
### Variable: lognegint

Valor padrão: `false`


Se `true` implementa a regra
`log(-n)` -> `log(n)+%i*%pi` para `n` um inteiro positivo.

<!-- category: Other -->
<!-- keywords: lognumer -->
<!-- signatures: lognumer -->
### Variable: lognumer

Valor padrão: `false`


Se `true` então argumentos negativos em ponto
flutuante para `log` irão sempre ser convertidos para seus valores absolutos
antes que o `log` seja tomado.  Se `numer` for também `true`, então argumentos inteiros
negativos para `log` irão também ser convertidos para seus valores absolutos.

<!-- category: Other -->
<!-- keywords: logsimp -->
<!-- signatures: logsimp -->
### Variable: logsimp

Valor padrão: `true`


Se `false` então nenhuma simplificação de `%e` para um
expoente contendo `log`’s é concluída.

<!-- category: Other -->
<!-- keywords: plog -->
<!-- signatures: plog(x) -->
### Function: plog (x)

Representa o principal ramo logarítmos naturais avaliados para
complexos com `-%pi` < `carg(x)` <= `+%pi` .

