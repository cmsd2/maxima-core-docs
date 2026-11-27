## Simplificação

<!-- category: Simplification -->
<!-- keywords: askexp -->
<!-- signatures: askexp -->
### Variable: askexp

Quando `asksign` é chamada, `askexp` é a expressão que
`asksign` está a testar.


Antigamente, era possível para um utilizador inspecionar
`askexp` parando o Maxima com control-A.

<!-- category: Simplification -->
<!-- keywords: askinteger -->
<!-- signatures: askinteger(expr, integer), askinteger(expr), askinteger(expr, even), askinteger(expr, odd) -->
### Function: askinteger (expr, integer)

`askinteger (expr, integer)` tenta determinar a partir da
base de dados do `assume` se *expr* é um inteiro. Se não conseguir,
`askinteger` perguntará ao utilizador, na linha de comandos,

e inserirá essa informação na base de dados do
`assume`, se for possível.  `askinteger (expr)` é equivalente a `askinteger (expr, integer)`.


Da mesma forma, `askinteger (expr, even)` e `askinteger (expr, odd)` tentam determinar se *expr* é um inteiro par ou
inteiro ímpar, respectivamente.

<!-- category: Simplification -->
<!-- keywords: asksign -->
<!-- signatures: asksign(expr) -->
### Function: asksign (expr)

Primeiro tenta determinar se a expressão especificada é positiva,
negativa, ou zero. Se isso não for possível,
`asksign` perguntará ao utilizador as questões necessárias
para completar a sua dedução. As respostas do utilizador
serão guardadas na base de dados pelo tempo que durar a cálculo
actual. O valor de retorno de `asksign` será `pos`,
`neg`, ou `zero`.

<!-- category: Simplification -->
<!-- keywords: demoivre -->
<!-- signatures: demoivre(expr) -->
### Function: demoivre (expr)

A função `demoivre (expr)` transforma uma
expressão sem modificar a variável global `demoivre`.


Quando a variável `demoivre` for `true`, as exponenciais
complexas serão convertidas em expressões equivalentes em termos das
funções circulares: `exp (a + b*%i)` simplifica
para `%e^a * (cos(b) + %i*sin(b))` se `b` não incluir
`%i`.  `a` e `b` não serão expandidos.


O valor padrão de `demoivre` é `false`.


`exponentialize` converte funções circulares e
hiperbólicas para a forma exponencial.  `demoivre` e
`exponentialize` não podem ambas serem `true` ao mesmo
tempo.

<!-- category: Simplification -->
<!-- keywords: domain -->
<!-- signatures: domain -->
### Variable: domain

Valor por omissão: `real`


Quando a `domain` for dado o valor `complex`, `sqrt(x^2)`
permanecerá `sqrt (x^2)` em lugar de retornar `abs(x)`.

<!-- category: Simplification -->
<!-- keywords: expand -->
<!-- signatures: expand(expr), expand(expr, p, n) -->
### Function: expand (expr)

Expande a expressão *expr*.  Nos rodutos de somas e exponenciais
de somas são expandidos os produtos, os numeradores de expressões
racionais que incluirem somas serão quebrados nas suas respectivas
parcelas, e os produtos (comutativos e não comutativos) são
distribuídos sobre as somas em todos os
níveis de *expr*.


Para polinómios se pode usar frequêntemente `ratexpand` que
possui um algoritmo mais eficiente.


`maxnegex` e `maxposex` controlam o máximo expoente negativo
e o máximo expoente positivo, respectivamente, que irão expandir.


`expand (expr, p, n)` expande *expr*, usando
*p* para `maxposex` e *n* para `maxnegex`.  Isso é
útil para expandir partes numa expressão mas não toda.


`expon` - o expoente da maior potência negativa que é
automaticamente expandida (independente de chamadas a `expand`).
Por Exemplo se `expon` for 4 então `(x+1)^(-5)` não será
automaticamente expandido.


`expop` - o maior expoente positivo que é automaticamente
expandido.  Dessa forma `(x+1)^3`, quando digitado, será
automaticamente expandido somente se `expop` for maior que ou igual
a 3.  Se quiser que `(x+1)^n` seja expandido onde `n` for
maior que `expop`, então `expand ((x+1)^n)` funcionará
unicamente se `maxposex` não for menor que `n`.


O sinalizador `expand` usado com `ev` causa expansão.


O ficheiro `simplification/facexp.mac`




contém muitas funções relacionadas (em particular
`facsum`, `factorfacsum` e `collectterms`, que são
carregadas automaticamente) e as variáveis (`nextlayerfactor` e
`facsum_combine`) que fornecem ao utilizador a possibilidade de
estruturar expressões por expansão controlada.

Uma descrição breve das função
encontra-se no ficheiro `simplification/facexp.usg`.  Há também
uma demonstração disponível com o comando
`demo("facexp")`.

<!-- category: Simplification -->
<!-- keywords: expandwrt -->
<!-- signatures: expandwrt(expr, x_1, ..., x_n) -->
### Function: expandwrt (expr, x_1, ..., x_n)

Expande a expressão `expr` com relação às
variáveis *x_1*, ..., *x_n*.  Todos os produtos que encvolvam
as variáveis aparecerão explicitamente. O resultado estará livre
de produtos de somas de expressões que não estejam livres das
variáveis.  *x_1*, ..., *x_n* podem ser variáveis,
operadores, ou expressões.


Por omissão, os denominadores não são expandidos, mas isso pode ser
controlado através da variável `expandwrt_denom`.


Esta função é carregada automaticamente a partir de
`simplification/stopex.mac`.

<!-- category: Simplification -->
<!-- keywords: expandwrt_denom -->
<!-- signatures: expandwrt_denom -->
### Variable: expandwrt_denom

Valor por omissão: `false`


`expandwrt_denom` controla a simplificação de expressões
racionais feita por `expandwrt`. Se tiver valor `true`,
então tanto o numerador como o denominador da expressão serão
expandidos conforme os argumentos de `expandwrt`, mas se
`expandwrt_denom` for `false`, então somente o numerador
será expandido.

<!-- category: Simplification -->
<!-- keywords: expandwrt_factored -->
<!-- signatures: expandwrt_factored(expr, x_1, ..., x_n) -->
### Function: expandwrt_factored (expr, x_1, ..., x_n)

é similar a `expandwrt`, mas trata os produtos numa forma
diferente.  `expandwrt_factored` expande somente sobre esses
factores de `expr` que contiverem as variáveis *x_1*, ...,
*x_n*.



Esta função é carregada automaticamente a partir de
`simplification/stopex.mac`.

<!-- category: Simplification -->
<!-- keywords: expon -->
<!-- signatures: expon -->
### Variable: expon

Valor por omissão: 0


`expon` é o expoente da maior potência negativa que é
automaticamente expandido (independente de chamadas a `expand`).
Por exemplo, se `expon` for 4 então `(x+1)^(-5)` não
será automaticamente expandido.

<!-- category: Simplification -->
<!-- keywords: exponentialize -->
<!-- signatures: exponentialize(expr) -->
### Function: exponentialize (expr)

A função `exponentialize (expr)` converte as
funções circulares e hiperbólicas em *expr* para
exponenciais, sem modificar a variável global `exponentialize`.


Quando a variável `exponentialize` for `true`, todas as
funções circulares e hiperbólicas são convertidas
para a forma exponencial. O valor por omissão é `false`.


`demoivre` converte exponenciais complexas em
funções circulares.  `exponentialize` e
`demoivre` não podem ambas serem `true` ao mesmo tempo.

<!-- category: Simplification -->
<!-- keywords: expop -->
<!-- signatures: expop -->
### Variable: expop

Valor por omissão: 0


`expop` - o maior expoente positivo que é automaticamente
expandido.  Dessa forma `(x+1)^3`, será automaticamente expandido
somente se `expop` for maior que ou igual a 3.  Se quiser que
`(x+1)^n` seja expandido onde `n` for maior que `expop`,
então `expand ((x+1)^n)` funcionará somente se `maxposex`
não for menor que `n`.

<!-- category: Simplification -->
<!-- keywords: factlim -->
<!-- signatures: factlim -->
### Variable: factlim

Valor por omissão: -1


`factlim` especifica o maior factorial que é automaticamente
expandido. Se for -1 então todos os inteiros são expandidos.

<!-- category: Simplification -->
<!-- keywords: intosum -->
<!-- signatures: intosum(expr) -->
### Function: intosum (expr)

Move factores multiplicativos fora de um somatório para dentro.  Se um
índice for usado na expressão de fora, então a
função tentará achar um índice
razoável, o mesmo que é feito para `sumcontract`.  Isto é
essencialmente a ideia inversa da propriedade `outative` de
somatórios, mas repare que não elimina essa propriedade, apenas faz
com que seja ignorada.



Em alguns casos, poderá ser necessário um
`scanmap(multthru,expr)` antes de `intosum`.

<!-- category: Simplification -->
<!-- keywords: lassociative -->
<!-- signatures: lassociative -->
### Variable: lassociative

`declare (g, lassociative)` diz ao simplificador do Maxima que
`g` é associativa à esquerda.  E.g., `g (g (a, b), g (c, d))` irá simplificar para `g (g (g (a, b), c), d)`.

<!-- category: Simplification -->
<!-- keywords: linear -->
<!-- signatures: linear -->
### Variable: linear

Uma das propriedades operativas do Maxima. As funções de
uma única variável `f` assim declaradas fazem com que a
expressão `f(x + y)` seja expandida em `f(x) + f(y)`, a
expressão `f(a*x)` transforma-se em `a*f(x)` se `a` for
uma constante. Para funções de dois ou mais argumentos,
a linearidade define-se igual que no caso de `sum` ou
`integrate`, isto é, `f (a*x + b, x)` retorna `a*f(x,x) + b*f(1,x)`, se `a` e `b` forem independentesx de `x`.


`linear` é equivalente a `additive` e `outative`.
Veja também `opproperties`.

<!-- category: Simplification -->
<!-- keywords: mainvar -->
<!-- signatures: mainvar -->
### Variable: mainvar

Permite declarar variáveis do tipo `mainvar` (variável
principal).  A escala de ordenação para átomos é
essencialmente: números < constantes (e.g., `%e`, `%pi`) <
escalares < outras variáveis < mainvars.  Por exemplo, compare
`expand ((X+Y)^4)` com `(declare (x, mainvar), expand ((x+y)^4))`.  (Nota: este recurso deverá ser usado com cautela. Por
exemplo, se subtrair uma expressão, na qual `x` for uma
`mainvar`, da mesma expressão, mas onde `x` não for
`mainvar`, poderá precisar de resimplificação,
por exemplo, com `ev (expr, simp)`, para que sejam canceladas.
Também, se grava uma expressão na qual `x` for uma
`mainvar`, provavelmente deverá também gravar `x`.)

<!-- category: Simplification -->
<!-- keywords: maxapplydepth -->
<!-- signatures: maxapplydepth -->
### Variable: maxapplydepth

Valor por omissão: 10000


`maxapplydepth` é a profundidade máxima ate a qual `apply1`
e `apply2` deverão descer.

<!-- category: Simplification -->
<!-- keywords: maxapplyheight -->
<!-- signatures: maxapplyheight -->
### Variable: maxapplyheight

Valor por omissão: 10000


`maxapplyheight` é nível máximo a ser atingido
por `applyb1` antes de abandonar.

<!-- category: Simplification -->
<!-- keywords: maxnegex -->
<!-- signatures: maxnegex -->
### Variable: maxnegex

Valor por omissão: 1000


`maxnegex` é o maior expoente negativo que será expandido pelo
comando `expand` (veja também `maxposex`).

<!-- category: Simplification -->
<!-- keywords: maxposex -->
<!-- signatures: maxposex -->
### Variable: maxposex

Valor por omissão: 1000


`maxposex` é o maior expoente que será expandido com o comando
`expand` (veja também `maxnegex`).

<!-- category: Simplification -->
<!-- keywords: multiplicative -->
<!-- signatures: multiplicative -->
### Variable: multiplicative

`declare (f, multiplicative)` diz ao simplificador do Maxima que
`f` é multiplicativa.



1. Se `f` for uma função de uma única variável,
sempre que o simplificador encontrar `f` aplicada a um produto,
`f` será distribuida nesse produto.  Por exemplo, `f(x*y)`
simplifica para `f(x)*f(y)`.
2. Se `f` for uma função de 2 ou mais argumentos, a
multiplicatividade entende-se como multiplicatividade no primeiro
argumento de `f`. Por exemplo, `f (g(x) * h(x), x)` simplifica
para `f (g(x) ,x) * f (h(x), x)`.


Esta simplificação não é feita quando `f` for
aplicada a expressões da forma `product (x[i], i, m, n)`.

<!-- category: Simplification -->
<!-- keywords: negdistrib -->
<!-- signatures: negdistrib -->
### Variable: negdistrib

Valor por omissão: `true`


Quando `negdistrib` for `true`, -1 distribue sobre uma
expressão. Por exemplo, `-(x + y)` transforma-se em `- y - x`.  Mudando o valor de `negdistrib` para `false` permitirá
que `- (x + y)` seja mostrado como foi escrito. Embora isso possa
ser útil, tenha muito cuidado: esta variável e a variável
`simp` não deveriam ser escolhidas sempre como `false`,
excepto em forma local no seu Maxima.

<!-- category: Simplification -->
<!-- keywords: negsumdispflag -->
<!-- signatures: negsumdispflag -->
### Variable: negsumdispflag

Valor por omissão: `true`


Quando `negsumdispflag` for `true`, `x - y` é mostrado
como `x - y` em lugar de como `- y + x`. Mudando para
`false` faz com que não seja feita a verificação
especial para a apresentação da diferença entre duas
expressões.  Uma aplicação é para que `a + %i*b` e `a - %i*b` sejam mostrados na mesma forma.

<!-- category: Simplification -->
<!-- keywords: noeval -->
<!-- signatures: noeval -->
### Variable: noeval

`noeval` suprime a fase de avaliação de `ev`.
Isso é útil conjuntamente com outras condições e para fazer com
que expressões sejam simplificadas sem serem reavaliadas.

<!-- category: Simplification -->
<!-- keywords: noun -->
<!-- signatures: noun -->
### Variable: noun

`noun` é uma das opções do comando
`declare`.  Faz com que as funções assim declaradas sejam
substantivos (noun), implicando que não sejam avaliadas
automaticamente.

<!-- category: Simplification -->
<!-- keywords: noundisp -->
<!-- signatures: noundisp -->
### Variable: noundisp

Valor por omissão: `false`


Quando `noundisp` for `true`, os substantivos (nouns) são
mostrados com um apóstrofo. Sempre que se mostra a
definição de uma função, essa variável
é igual a `true`.

<!-- category: Simplification -->
<!-- keywords: nouns -->
<!-- signatures: nouns -->
### Variable: nouns

`nouns` é um `evflag` (sinalizador de
avaliação). Quando usado como uma opção
para o comando `ev`, `nouns` converte todas as formas
substantivas (noun), na expressão a ser avaliada, para verbos
("verbs"), isto é, avalia essas expressões. Veja também
`noun`, `nounify`, `verb`, e `verbify`.

<!-- category: Simplification -->
<!-- keywords: numer -->
<!-- signatures: numer -->
### Variable: numer

`numer` faz com que algumas funções matemáticas
(incluindo exponenciação) com argumentos numéricos
sejam avaliadas em ponto flutuante. Isto faz com que variáveis em
`expr` que tiverem valores numéricos sejam
substituídas pelos seus valores correspondentes.
`numer` também activa a opção `float`.

<!-- category: Simplification -->
<!-- keywords: numerval -->
<!-- signatures: numerval(x_1, expr_1, ..., var_n, expr_n) -->
### Function: numerval (x_1, expr_1, ..., var_n, expr_n)

Declara as variáveis `x_1`, ..., *x_n* com valores
numéricos iguais a `expr_1`, ..., `expr_n`.  O valor
numérico é avaliado e substituido para a variável em quaisquer
expressões em que a variável aparecer, se o sinalizador `numer`
for igual a `true`. Veja também `ev`.


As expressões `expr_1`, ..., `expr_n` podem ser quaisquer,
não necessariamente numéricas.

<!-- category: Simplification -->
<!-- keywords: opproperties -->
<!-- signatures: opproperties -->
### Variable: opproperties

`opproperties` é a lista de propriedades de operadores especiais
reconhecidas pelo simplificador do Maxima: `linear`,
`additive`, `multiplicative`, `outative`, `evenfun`,
`oddfun`, `commutative`, `symmetric`,
`antisymmetric`, `nary`, `lassociative`,
`rassociative`.

<!-- category: Simplification -->
<!-- keywords: opsubst -->
<!-- signatures: opsubst -->
### Variable: opsubst

Valor por omissão: `true`


Quando `opsubst` for `false`, `subst` não tenta
substituir dentro de um operador de uma expressão.  Por exemplo, 
`(opsubst: false, subst (x^2, r, r+r[0]))`.

<!-- category: Simplification -->
<!-- keywords: outative -->
<!-- signatures: outative -->
### Variable: outative

`declare (f, outative)` diz ao simplificador do Maxima que factores
constantes no argumento de `f` podem ser puxados para fora.



1. Se `f` for uma função de uma única variável,
sempre que o simplificador encontrar `f` aplicada a um produto, os
factores que forem constantes nesse produto serão puxados para
fora. Por exemplo, `f(a*x)` simplificará para `a*f(x)` se
`a` for uma constante.  Factores de constantes não atomicas
não serão puxados para fora.
2. Se `f` for uma função de 2 ou mais argumentos, a
colocação para fora é definida como no caso de
`sum` ou `integrate`, isto é, `f (a*g(x), x)` irá
simplificar para `a * f(g(x), x)` se `a` não depender de
`x`.


`sum`, `integrate`, e `limit` são todas do tipo
`outative`.

<!-- category: Simplification -->
<!-- keywords: posfun -->
<!-- signatures: posfun -->
### Variable: posfun

`declare (f, posfun)` declara `f` como função
positiva.  `is (f(x) > 0)` retorna `true`.

<!-- category: Simplification -->
<!-- keywords: radcan -->
<!-- signatures: radcan(expr) -->
### Function: radcan (expr)

Simplifica *expr*, que pode conter logaritmos,
exponenciais, e radicais, convertendo essa expressão numa forma
canónica sobre uma ampla classe de expressões e com uma dada
ordenação de variáveis; isto é, todas as formas
funcionalmente equivalentes são mapeadas numa única forma.  Para uma
classe ampla de expressões, `radcan` produz uma forma regular.
Duas expressões equivalentes nessa classe não possuem
necessáriamente a mesma aparência, mas as suas diferenças podem
ser simplificadas por `radcan` para zero.


Para algumas expressões `radcan` demora muito tempo. Esse é o
custo de explorar as realções entre as componentes da expressão
para simplificar expoentes usando factorização e expansão em
frações parciais.




Quando `%e_to_numlog` for `true`, `%e^(r*log(expr))`
simplifica para `expr^r` se `r` for um número racional.


Quando `radexpand` for `false`, certas
transformações são inibidas.  `radcan (sqrt (1-x))` permanece `sqrt (1-x)` e não é simplificada para
`%i sqrt (x-1)`.  `radcan (sqrt (x^2 - 2*x + 11))` permanece
`sqrt (x^2 - 2*x + 1)` e não é simplificada para `x - 1`.



`example (radcan)` mostra alguns exemplos.

<!-- category: Simplification -->
<!-- keywords: radexpand -->
<!-- signatures: radexpand -->
### Variable: radexpand

Valor por omissão: `true`


`radexpand` controla algumas simplificações de
radicais.


Quando `radexpand` for `all`, todos os factores que forem
potências de ordem n, dentro de uma raiz de ordem n, serão puxados
para fora do radical. Por exemplo, se `radexpand` for `all`,
`sqrt (16*x^2)` simplifica para `4*x`.



Mais particularmente, considere `sqrt (x^2)`.


- *
Se `radexpand` for `all` ou `assume (x > 0)` tiver sido
executado, `sqrt(x^2)` simplifica para `x`.
- *
Se `radexpand` for `true` e `domain` for `real`
(valores usados por omissão), `sqrt(x^2)` simplifica para
`abs(x)`.
- *
Se `radexpand` for `false`, ou `radexpand` for
`true` e `domain` for `complex`, `sqrt(x^2)` não
é simplificado.



Note que, neste exemplo, `domain` somente interessa quando
`radexpand` for `true`.

<!-- category: Simplification -->
<!-- keywords: radsubstflag -->
<!-- signatures: radsubstflag -->
### Variable: radsubstflag

Valor por omissão: `false`


Se `radsubstflag` for `true`, permite a `ratsubst` fazer
substituições tais como `u` por `sqrt (x)` em
`x`.

<!-- category: Simplification -->
<!-- keywords: rassociative -->
<!-- signatures: rassociative -->
### Variable: rassociative

`declare (g, rassociative)` diz ao simplificador do Maxima que
`g` é associativa à direita, isto é, `g(g(a, b), g(c, d))`
simplifica para `g(a, g(b, g(c, d)))`.

<!-- category: Simplification -->
<!-- keywords: scsimp -->
<!-- signatures: scsimp(expr, rule_1, ..., rule_n) -->
### Function: scsimp (expr, rule_1, ..., rule_n)

Simplificação Sequêncial Comparativa (método devido
a Stoute).  `scsimp` tenta simplificar *expr* conforme as
regras *rule_1*, ..., *rule_n*.  Se uma expressão pequena for
obtida, o processo repete-se.  De outra forma após todas as
simplificações serem tentadas, `scsimp` retorna a
resposta original.



`example (scsimp)` mostra alguns exemplos.

<!-- category: Simplification -->
<!-- keywords: simpsum -->
<!-- signatures: simpsum -->
### Variable: simpsum

Valor por omissão: `false`


Quando `simpsum` for `true`, o resultado de um comando
`sum` é simplificado.  Essa simplificação pode
algumas vezes produzir uma forma fechada.  Se `simpsum` for
`false`, ou se a forma com apóstrofo `'sum` for usada, o
valor é uma forma substantiva aditiva que é uma
representação da notação sigma usada em
matemática.

<!-- category: Simplification -->
<!-- keywords: sumcontract -->
<!-- signatures: sumcontract(expr) -->
### Function: sumcontract (expr)

Combina vários somatórios que possuem limites superiores e inferiores
que diferem por constantes. O resultado é uma expressão que contém
apenas um somatório mais todos os termos adicionais que tiveram de ser
extraídos para obter essa forma.  `sumcontract`
combina todas as somas compatíveis e usa os indices de uma
das somas, se puder, ou tenta formar um índice razoável
se não poder usar nenhum dos que foram fornecidos.



Poderá ser necessário usar `intosum (expr)` antes de
`sumcontract`.

<!-- category: Simplification -->
<!-- keywords: sumexpand -->
<!-- signatures: sumexpand -->
### Variable: sumexpand

Valor por omissão: `false`


Quando `sumexpand` for `true`, produtos de somas e somas
exponeciadas simplificam para somas aninhadas.


Veja também `cauchysum`.


Exemplos:



```maxima
(%i1) sumexpand: true$
(%i2) sum (f (i), i, 0, m) * sum (g (j), j, 0, n);
                     m      n
                    ====   ====
                    \      \
(%o2)                >      >     f(i1) g(i2)
                    /      /
                    ====   ====
                    i1 = 0 i2 = 0
(%i3) sum (f (i), i, 0, m)^2;
                     m      m
                    ====   ====
                    \      \
(%o3)                >      >     f(i3) f(i4)
                    /      /
                    ====   ====
                    i3 = 0 i4 = 0
```

<!-- category: Simplification -->
<!-- keywords: sumsplitfact -->
<!-- signatures: sumsplitfact -->
### Variable: sumsplitfact

Valor por omissão: `true`


Quando `sumsplitfact` for `false`,

`minfactorial` é aplicado após `factcomb`.

<!-- category: Simplification -->
<!-- keywords: symmetric -->
<!-- signatures: symmetric -->
### Variable: symmetric

`declare (h, symmetric)` diz ao simplificador do Maxima que
`h` é uma função simétrica.  Nomeadamente,
`h (x, z, y)` simplifica para `h (x, y, z)`.


`commutative` é sinonimo de `symmetric`.

<!-- category: Simplification -->
<!-- keywords: unknown -->
<!-- signatures: unknown(expr) -->
### Function: unknown (expr)

Retorna `true` se e somente se *expr* contém um operador ou
função não reconhecida pelo simplificador do Maxima.

