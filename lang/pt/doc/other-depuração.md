## Depuração

<!-- category: Other -->
<!-- keywords: refcheck -->
<!-- signatures: refcheck -->
### Variable: refcheck

Valor por omissão: `false`


Quando `refcheck` for `true`, Maxima imprime uma mensagem
cada vez que uma variável associada for usada pela primeira vez em uma
computação.

<!-- category: Other -->
<!-- keywords: setcheck -->
<!-- signatures: setcheck -->
### Variable: setcheck

Valor por omissão: `false`


Se `setcheck` for escolhido para uma lista de variáveis (as quais podem
ser subscritas), 
Maxima mostra uma mensagem quando as variáveis, ou
ocorrências subscritas delas, forem associadas com o
operador comum de atribuição `:`, o operador `::`
de atribuição, ou associando argumentos de função,
mas não com o operador de atribuição de função `:=` nem o operador de atribuição
`::=` de macro.
A mensagem compreende o nome das variáveis e o
valor associado a ela.


`setcheck` pode ser escolhida para `all` ou `true` incluindo
desse modo todas as variáveis.


Cada nova atribuição de `setcheck` estabelece uma nova lista de variáveis
para verificar, e quaisquer variáveis previamente atribuídas a `setcheck` são esquecidas.


Os nomes atribuídos a `setcheck` devem ter um apóstrofo no início se eles forem de outra forma
avaliam para alguma outra coisa que não eles mesmo.
Por exemplo, se `x`, `y`, e `z` estiverem actualmente associados, então digite



```maxima
setcheck: ['x, 'y, 'z]$
```


para colocá-los na lista de variáveis monitoradas.


Nenhuma saída é gerada quando uma
variável na lista `setcheck` for atribuída a sí mesma, e.g., `X: 'X`.

<!-- category: Other -->
<!-- keywords: setcheckbreak -->
<!-- signatures: setcheckbreak -->
### Variable: setcheckbreak

Valor por omissão: `false`


Quando `setcheckbreak` for `true`,
Maxima mostrará um ponto de parada 
quando uma variável sob a lista `setcheck` for atribuída a um novo valor.
A parada ocorre antes que a atribuíção seja concluída.
Nesse ponto, `setval` retém o valor para o qual a variável está 
para ser atribuída.
Consequentemente, se pode atribuir um valor diferente através da atribuição a `setval`.


Veja também `setcheck` e `setval`.

<!-- category: Other -->
<!-- keywords: setval -->
<!-- signatures: setval -->
### Variable: setval

Mantém o valor para o qual a variável está para ser escolhida quando
um `setcheckbreak` ocorrer.
Consequentemente, se pode atribuir um valor diferente através da atribuição a `setval`.


Veja também `setcheck` e `setcheckbreak`.

<!-- category: Other -->
<!-- keywords: timer -->
<!-- signatures: timer(f_1, ..., f_n), timer() -->
### Function: timer (f_1, ..., f_n)

Dadas as funções *f_1*, ..., *f_n*,
`timer` coloca cada uma na lista de funções para as quais cronometragens estatísticas são colectadas.
`timer(f)$ timer(g)$` coloca `f` e então `g` sobre a lista;
a lista acumula de uma chamada para a chamada seguinte.


Sem argumentos, 
`timer` retorna a lista das funções tempo estatisticamente monitoradas.


Maxima armazena quanto tempo é empregado executando cada função
na lista de funções tempo estatisticamente monitoradas.
`timer_info` retorna a coronometragem estatística, incluindo o
tempo médio decorrido por chamada de função, o número de chamadas, e o
tempo total decorrido.
`untimer` remove funções da lista de funções tempo estatisticamente monitoradas.


`timer` não avalia seus argumentos. 
`f(x) := x^2$ g:f$ timer(g)$` não coloca `f` na lista de funções estatisticamente monitoradas.


Se `trace(f)` está vigorando, então `timer(f)` não tem efeito; `trace` e
`timer` não podem ambas atuarem ao mesmo tempo.


Veja também `timer_devalue`.

<!-- category: Other -->
<!-- keywords: timer_devalue -->
<!-- signatures: timer_devalue -->
### Variable: timer_devalue

Valor Padrão: `false`


Quando `timer_devalue` for `true`, Maxima subtrai de cada função estatisticamente monitorada
o tempo empregado em ou funções estatisticamente monitoradas. De outra forma, o tempo reportado 
para cada função inclui o tempo empregado em outras funções.
Note que tempo empregado em funções não estatisticamente monitoradas não é subtraído do
tempo total.


Veja também `timer` e `timer_info`.

<!-- category: Other -->
<!-- keywords: timer_info -->
<!-- signatures: timer_info(f_1, ..., f_n), timer_info() -->
### Function: timer_info (f_1, ..., f_n)

Dadas as funções *f_1*, ..., *f_n*,
`timer_info` retorna uma matriz contendo informações de cronometragem para cada função.
Sem argumentos, `timer_info` retorna informações de cronometragem para
todas as funções actualmente na lista de funções estatisticamente monitoradas.


A matriz retornada através de `timer_info` contém o nome da função,
tempo por chamda de função, número de chamadas a funções,tempo total,
e `gctime`, cujja forma "tempo de descarte" no Macsyma original
mas agora é sempre zero.


Os dados sobre os quais `timer_info` constrói seu valor de retorno
podem também serem obtidos através da função `get`:



```maxima
get(f, 'calls);  get(f, 'runtime);  get(f, 'gctime);
```


Veja também `timer`.

<!-- category: Other -->
<!-- keywords: trace -->
<!-- signatures: trace(f_1, ..., f_n), trace() -->
### Function: trace (f_1, ..., f_n)

Dadas as funções *f_1*, ..., *f_n*,
`trace` instrui Maxima para mostrar
informações de depuração quando essas funções forem chamadas.
`trace(f)$ trace(g)$` coloca `f` e então `g` na lista de funções
para serem colocadas sob a ação de `trace`; a lista acumula de uma chamada para a seguinte.


Sem argumentos,
`trace` retorna uma lista de todas as funções actualmente sob a ação de `trace`.


A função `untrace` desabilita a ação de `trace`.
Veja também `trace_options`. 


`trace` não avalia seus argumentos. Dessa forma,
`f(x) := x^2$ g:f$ trace(g)$` não coloca `f` sobre a lista de funções monitoradas por `trace`.


Quando uma função for redefinida, ela é removida da lista de `timer`.
Dessa forma após `timer(f)$ f(x) := x^2$`,
a função `f` não mais está na lista de `timer`.


Se `timer (f)` estiver em efeito, então `trace (f)` não está agindo; `trace` e
`timer` não podem ambas estar agindo para a mesma função.

<!-- category: Other -->
<!-- keywords: trace_options -->
<!-- signatures: trace_options(f, option_1, ..., option_n), trace_options(f) -->
### Function: trace_options (f, option_1, ..., option_n)

Escolhe as opções de `trace` para a função *f*.
Quaisquer opções anteriores são substituídas.
`trace_options (f, ...)` não tem efeito a menos que
`trace (f)` tenha sido também chamada (ou antes ou após `trace_options`). 


`trace_options (f)` reposiciona todas as opções para seus valores padrão.


As opções de palavra chave são:



- *
`noprint`
Não mostre uma mensagem na entrada da função e saia.
- *
`break`
Coloque um ponto de parada antes da função ser inserida,
e após a funçãos er retirada. Veja `break`.
- *
`lisp_print`
Mostre argumentos e valores de retorno com objectos Lisp.
- *
`info`
Mostre `-> true` na entrada da funçào e saia.
- *
`errorcatch`
Capture os erros, fornecendo a opção para sinalizar um erro,
tentar novamente a chamada de função, ou especificar um valor de retorno.


Opções para `trace` são especificadas em duas formas. A presença da palavra chave de 
opção sozinha coloca a opção para ter efeito incondicionalmente.
(Note que opção *foo* não coloca para ter efeito especificando 
`foo: true` ou uma forma similar; note também que palavras chave não precisam
estar com apóstrofo.) Especificando a opção palavra chave com uma função
predicado torna a opção condicional sobre o predicado.


A lista de argumentos para a função predicado é sempre 
`[level, direction, function, item]` onde `level` é o nível rerecursão
para a função,  `direction` é ou `enter` ou `exit`, `function` é o
nome da função, e `item` é a lista de argumentos (sobre entrada)
ou o valor de retorno (sobre a saída).


Aqui está um exemplo de opções incondicionais de `trace`:



```maxima
(%i1) ff(n) := if equal(n, 0) then 1 else n * ff(n - 1)$

(%i2) trace (ff)$

(%i3) trace_options (ff, lisp_print, break)$

(%i4) ff(3);
```


Aqui está a mesma função, com a opção `break` condicional
sobre um predicado:



```maxima
(%i5) trace_options (ff, break(pp))$

(%i6) pp (level, direction, function, item) := block (print (item),
    return (function = 'ff and level = 3 and direction = exit))$

(%i7) ff(6);
```

<!-- category: Other -->
<!-- keywords: untimer -->
<!-- signatures: untimer(f_1, ..., f_n), untimer() -->
### Function: untimer (f_1, ..., f_n)

Dadas as funções *f_1*, ..., *f_n*,
`untimer` remove cada uma das funções listadas da lista de funções estatisticamente monitoradas.


Sem argumentos, `untimer` remove todas as funções actualmente na  lista de funções estatisticamente monitoradas.


Após `untimer (f)` ser executada, `timer_info (f)` ainda retorna
estatisticas de tempo previamente colectadas,
embora `timer_info()` (sem argumentos) não
retorna informações sobre qualquer função que não estiver actualmente na lista de funções tempo estatisticamente monitoradas.
`timer (f)` reposiciona todas as estatisticas de tempo para zero
e coloca `f` na lista de funções estatisticamente monitoradas novamente.

<!-- category: Other -->
<!-- keywords: untrace -->
<!-- signatures: untrace(f_1, ..., f_n), untrace() -->
### Function: untrace (f_1, ..., f_n)

Dadas as funções *f_1*, ..., *f_n*,
`untrace` desabilita a a monitoração habilitada pela função `trace`.
Sem argumentos, `untrace` desabilita a atuação da função `trade` para todas as funções.


`untrace` retorne uma lista das funções para as quais 
`untrace` desabilita a atuação de `trace`.

