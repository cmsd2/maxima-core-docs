## simplification

<!-- category: Simplification -->
<!-- keywords: agd -->
<!-- signatures: agd(x) -->
### Function: agd (x)

Retorna o inverso da função de Gudermann
`log (tan (%pi/4 + x/2)))`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: arithmetic -->
<!-- signatures: arithmetic(a, d, n) -->
### Function: arithmetic (a, d, n)

Retorna o *n*-ésiomo termo da série aritmética
`a, a + d, a + 2*d, ..., a + (n - 1)*d`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: arithsum -->
<!-- signatures: arithsum(a, d, n) -->
### Function: arithsum (a, d, n)

Retorna a soma dos elementos da série aritmética de 1 a *n*.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: collectterms -->
<!-- signatures: collectterms(expr, arg_1, ..., arg_n) -->
### Function: collectterms (expr, arg_1, ..., arg_n)

Se muitas expressões tiverem sido
simplificadas com `facsum`, `factorfacsum`,  `factenexpand`,  `facexpten` ou
com `factorfacexpten`,  e elas estão para serem adicionadas umas às outras, pode ser
desejável combiná-las usando a função `collecterms`.
`collecterms` pode pegar como argumentos todos os argumentos que podem ser
fornecidos para essas outras funções associadas com excessão de
`nextlayerfactor`, que não tem efeito sobre `collectterms`.  A vantagem
de `collectterms`  está em que `collectterms` retorna uma forma similar a `facsum`, mas
uma vez que `collectterms` está adicionando forma que já tenham sido processadas por `facsum`,
`collectterms` não precisa repetir aquele esforço.   Essa capacidade é
especialmente útil quando a expressão a ser somada for muito grande.

<!-- category: Simplification -->
<!-- keywords: combination -->
<!-- signatures: combination(n, r) -->
### Function: combination (n, r)

Retorna o número de combinações de *n* objetos
tomados em grupos de *r* elementos.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: covers -->
<!-- signatures: covers(x) -->
### Function: covers (x)

Retorna o *sinus versus* do complemento `1 - sin (x)`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: exsec -->
<!-- signatures: exsec(x) -->
### Function: exsec (x)

Retorna a parte externa da secante `sec (x) - 1`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: facsum -->
<!-- signatures: facsum(expr, arg_1, ..., arg_n) -->
### Function: facsum (expr, arg_1, ..., arg_n)

Retorna uma forma de *expr*  que depende dos
argumentos *arg_1*, ..., *arg_n*.
Os argumentos podem ser quaisquer formas adequadas para `ratvars`, ou eles podem ser
listas  de tais formas.  Se os argumentos não forem listas, então a forma
retornada é completamente expandida com relação aos argumentos,  e os
coeficientes dos argumentos foram fatorados.  Esses coeficientes são
livres dos argumentos, exceto talvez no sentido não racional.


Se quaisquer dos argumentos forem listas, então todas as tais listas são combinadas
em uma lista simples,   e em lugar de chamar `factor`   sobre os
coeficientes  dos  argumentos,  `facsum`  chama a si mesma sobre esses
coeficientes, usando  essa nova lista simples que foi construída como o novo
argumento listo  para essa chamada recursiva.  Esse processo pode ser repetido para um
quantidade arbitrária de repetições por através do aninhamento dos elementos desejados nas listas.


É possível que alguém possa querer usar `facsum` com relação a subexpressões
mais complicadas,  tal como  `log (x + y)`.  Tais argumentos são
também permitidos.   Sem especificação de variável,  por exemplo
`facsum (expr)`, o resultado retornado é o mesmo que o que é retornado por meio de
`ratsimp (expr)`.


Ocasionalmente o usuário pode querer obter quaisquer das formas abaixo
para expressões que são especificadas somente por meio de seus operadores líderes.
Por exemplo, alguém pode querer usar `facsum` com relação a todos os `log`’s.  Nessa
situação, alguém pode incluir no meio dos argumentos ou o código
dos `log`’s específicos que devem ser tratados po esse caminho ou alternativamente a
expressão  `operator (log)` ou a expressão `'operator (log)`.   Se alguém quiser usar
`facsum` na expressão *expr* com relação aos operadores *op_1*, ..., *op_n*,
pode-se avaliar `facsum (expr, operator (op_1, ..., op_n))`.
A forma `operator` pode também aparecer dentro de uma lista de argumentos.


Adicionalmente,  a escolha de comutadores `facsum_combine`  e
`nextlayerfactor` pode afetar o resultado de `facsum`.

<!-- category: Simplification -->
<!-- keywords: facsum_combine -->
<!-- signatures: facsum_combine -->
### Variable: facsum_combine

Valor padrão: `true`


`facsum_combine` controla a forma do resultado final retornada por meio de
`facsum`  quando seu argumento é um quociente de polinômios.   Se
`facsum_combine` for `false`  então a forma será retornada como um somatório
completamente expandido como descrito acima,  mas se `true`,  então a expressão
retornada é uma razão de polinômios, com cada polinômio na forma
descrita acima.


A escolha de `true` desse comutador é útil quando se
deseja para `facsum` ambos o numerador e o denominador de uma expressão
racional,  mas não se deseja que o denominador seja multiplicado
de forma completa pelos termos do numerador.

<!-- category: Simplification -->
<!-- keywords: factorfacsum -->
<!-- signatures: factorfacsum(expr, arg_1, ...arg_n) -->
### Function: factorfacsum (expr, arg_1, ...arg_n)

Retorna uma forma de *expr*  que é
obtida por meio de chamada a `facsum` sobre os fatores de *expr* com *arg_1*, ... *arg_n* como
argumentos.  Se qualqeur dos fatores de *expr* estiver elevado a um expoente, ambos
o fator e o expoente irão ser processados por esse meio.

<!-- category: Simplification -->
<!-- keywords: gaussprob -->
<!-- signatures: gaussprob(x) -->
### Function: gaussprob (x)

Retorna a função de probalilidade de Gauss
`%e^(-x^2/2) / sqrt(2*%pi)`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: gcdivide -->
<!-- signatures: gcdivide(p, q) -->
### Function: gcdivide (p, q)

Quando `takegcd` for `true`,
`gcdivide` divide os polinômios *p* e *q* por seu maior divisor comum (MDC)
e retorna a razão dos resultados.


Quando `takegcd` for `false`,
`gcdivide` retorna a razão `p/q`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: gcfac -->
<!-- signatures: gcfac(expr) -->
### Function: gcfac (expr)

`gcfac` função de fatoração que tenta aplicar a mesma heurística que
cientístas aplicam em tentativas de fazer expressões extremamente simples.  `gcfac` está limitada
a fatorações monomiais.  Para um somatório, `gcfac` faz o seguinte:



1. Fatores sobre os inteiros.
2. Coloca em evidência o maior expoente de termos ocorrendo como
coeficientes, independentemente da complexidade dos termos.
3. Usa (1) e (2) em fatorações de pares de termos adjascentes.
4. Repetidamente e recursivamente aplica essas técnicas até que
a expressão não mais mude.


O item (3) não necessáriamente faz uma tarefa ótima fatoração
par a par devido à dificuldade combinatória natural de encontrar
qual de todas dos possíveis rearranjos de pares retorna o mais
compacto resultado de fatoração de um par.


`load ("scifac")` torna essa função disponível para uso.
`demo (scifac)` faz uma demonstração dessa função.

<!-- category: Simplification -->
<!-- keywords: gd -->
<!-- signatures: gd(x) -->
### Function: gd (x)

Retorna a função de Gudermann
`2 * atan(%e^x - %pi/2)`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: geometric -->
<!-- signatures: geometric(a, r, n) -->
### Function: geometric (a, r, n)

Retorna o *n*-ésimo termo da série geométrica
`a, a*r, a*r^2, ..., a*r^(n - 1)`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: geosum -->
<!-- signatures: geosum(a, r, n) -->
### Function: geosum (a, r, n)

Retorna a soma dos elementos da série geométrica de 1 a *n*.  Se *n* for
infinito (`inf`) então a soma será finita se e somente se o valor absoluto
de *r* for menor que 1.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: harmonic -->
<!-- signatures: harmonic(a, b, c, n) -->
### Function: harmonic (a, b, c, n)

Retorna o *n*-ésimo termo da série harmônica
`a/b, a/(b + c), a/(b + 2*c), ..., a/(b + (n - 1)*c)`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: hav -->
<!-- signatures: hav(x) -->
### Function: hav (x)

Retorna o semi-*sinus versus* `(1 - cos(x))/2`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: nextlayerfactor -->
<!-- signatures: nextlayerfactor -->
### Variable: nextlayerfactor

Valor padrão: `false`


Quando `nextlayerfactor` for `true`, chamadas recursivas a `facsum`
são aplicadas aos fatores da forma fatorada dos
coeficientes dos argumentos.


Quando `nextlayerfactor` for `false`, `facsum` é aplicada a
cada coeficiente como um todo mesmo se chamadas recursivas a `facsum` acontecerem.


A inclusão do átomo
`nextlayerfactor` na lista argumento de `facsum`  tem o efeito de
`nextlayerfactor: true`, mas para o próximo nível da expressão *somente*.
Uma vez que `nextlayerfactor` é sempre associado ou a `true` ou a  `false`, `nextlayerfactor`
deve ser apresentada com apóstrofo simples mesmo que `nextlayerfactor` apareça na lista de argumento de `facsum`.

<!-- category: Simplification -->
<!-- keywords: nonzeroandfreeof -->
<!-- signatures: nonzeroandfreeof(x, expr) -->
### Function: nonzeroandfreeof (x, expr)

Retorna `true` se *expr* for diferente de zero e `freeof (x, expr)` retorna `true`.
Retorna `false` de outra forma.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: permutation -->
<!-- signatures: permutation(n, r) -->
### Function: permutation (n, r)

Retorna o número de permutações de *r* objetos
selecionados de um conjunto de *n* objetos.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: rational -->
<!-- signatures: rational(z) -->
### Function: rational (z)

Multiplica o numerador e o denominador de *z* pelo complexo conjugado do denominador,
racionalizando dessa forma o denominador complexo.
Retorna a forma de expressão racional canônica (CRE) se fornecida uma CRE, caso contrário retorna a forma geral.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: reduce_consts -->
<!-- signatures: reduce_consts(expr) -->
### Function: reduce_consts (expr)

Substitui subexpressões constantes de *expr* com
construída com átomos constantes, gravando a definição de todas essas
constantes construídas na lista de equações `const_eqns`, e
retornando a expressão modificada *expr*.  Essas partes de *expr* são constantes que
retornam `true` quando operadas por meio da função `constantp`.  Consequêntemente,
antes de usar `reduce_consts`, se pode fazer



```maxima
declare ([objeto que vai receber a propriedade constante], constant)$
```


para escolher a base de dados das quantidades constantes ocorrendo em suas
expressões.


Se você está planejando gerar saídas em Fortran após esses cálculos
simbólicos, uma das primeiras seções de código pode ser o cálculo
de todas as constantes.  Para gerar esse segmento de código, faça



```maxima
map ('fortran, const_eqns)$
```


Variables como `const_eqns` que afetam `reduce_consts` são:


`const_prefix` (valor padrão: `xx`) é a sequência de caracteres usada para prefixar todos
os símbolos gerados por `reduce_consts` para representar subexpressões constantes.


`const_counter` (valor padrão: 1) é o índice inteiro usado para gerar símbolos
únicos para representar cada subexpressão constante emcontrada por `reduce_consts`.


`load ("rducon")` torna essa função disponível para uso.
`demo (rducon)` faz uma demonstração dessa função.

<!-- category: Simplification -->
<!-- keywords: rempart -->
<!-- signatures: rempart(expr, n) -->
### Function: rempart (expr, n)

Remove a parte *n* da expressão *expr*.


Se *n* é uma lsita da forma `[l, m]`
então as partes de *l* até *m* são removidas.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: sqrtdenest -->
<!-- signatures: sqrtdenest(expr) -->
### Function: sqrtdenest (expr)

Desaninha `sqrt` de simples, numérico, binômios de raízes irracionais de números racionais , onde for possível.  E.g.








```maxima
(%i1) load ("sqdnst")$
(%i2) sqrt(sqrt(3)/2+1)/sqrt(11*sqrt(2)-12);
                                    sqrt(3)
                               sqrt(------- + 1)
                                       2
(%o2)                        ---------------------
                             sqrt(11 sqrt(2) - 12)
(%i3) sqrtdenest(%);
                                  sqrt(3)   1
                                  ------- + -
                                     2      2
(%o3)                            -------------
                                    1/4    3/4
                                 3 2    - 2
```


Algumas vezes isso ajuda na hora de aplicar `sqrtdenest` mais que uma vez, sobre coisas como
`(19601-13860 sqrt(2))^(7/4)`.


`load ("sqdnst")` Torna essa função disponível para uso.

<!-- category: Simplification -->
<!-- keywords: tracematrix -->
<!-- signatures: tracematrix(M) -->
### Function: tracematrix (M)

Retorna o traço (somatório dos elementos da diagonal principal) da matriz *M*.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: vers -->
<!-- signatures: vers(x) -->
### Function: vers (x)

Retorna o *sinus versus* `1 - cos (x)`.


Para usar essa função escreva primeiramente `load("functs")`.

<!-- category: Simplification -->
<!-- keywords: wronskian -->
<!-- signatures: wronskian([f_1, ..., f_n], x) -->
### Function: wronskian ([f_1, ..., f_n], x)

Retorna a matriz Wronskiana das funções *f_1*, ..., *f_n* na variável *x*.


*f_1*, ..., *f_n* pode ser o nome de funções definidas pelo usuário,
ou expressões na variável *x*.


O determinante da matriz Wronskiana é o determinante Wronskiano do conjunto de funções.
As funções são linearmente independentes entre si se seu determinante for igual a zero.


Para usar essa função escreva primeiramente `load("functs")`.

