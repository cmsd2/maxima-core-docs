## Simplificação

<!-- category: Simplification -->
<!-- keywords: askexp -->
<!-- signatures: askexp -->
### Variable: askexp

Quando `asksign` é chamada,
`askexp` é a expressão que `asksign` está testando.


Antigamente, era possível para um usuário inspecionar `askexp`
entrando em uma parada do Maxima com control-A.

<!-- category: Simplification -->
<!-- keywords: askinteger -->
<!-- signatures: askinteger(expr, integer), askinteger(expr), askinteger(expr, even), askinteger(expr, odd) -->
### Function: askinteger (expr, integer)

`askinteger (expr, integer)` tenta determinar a partir da base de dados do `assume`
se *expr* é um inteiro.
`askinteger` pergunta ao usuário pela linha de comando se isso não puder ser feito de outra forma,

e tenta instalar a informação na base de dados do `assume` se for possível.
`askinteger (expr)` é equivalente a `askinteger (expr, integer)`.


`askinteger (expr, even)` e `askinteger (expr, odd)`
da mesma forma tentam determinar se *expr* é um inteiro par ou inteiro ímpar, respectivamente.

<!-- category: Simplification -->
<!-- keywords: asksign -->
<!-- signatures: asksign(expr) -->
### Function: asksign (expr)

Primeiro tenta determinar se a expressão
especificada é positiva, negativa, ou zero.  Se isso não for possível, `asksign` pergunta ao
usuário pelas questões necessárias para completar a sua dedução.  As respostas
do usuário são guardadas na base de dados pelo tempo que durar a computação
corrente. O valor de retorno de `asksign` é um entre `pos`, `neg`,
ou `zero`.

<!-- category: Simplification -->
<!-- keywords: demoivre -->
<!-- signatures: demoivre(expr) -->
### Function: demoivre (expr)

A função `demoivre (expr)` converte uma expressão
sem escolher a variável global `demoivre`.


Quando a variável `demoivre` for `true`,
exponenciais complexas são convertidas em expressões equivalentes em termos de funções circulares:
`exp (a + b*%i)` simplifica para `%e^a * (cos(b) + %i*sin(b))`
se `b` for livre de `%i`.
`a` e `b` não são expandidos.


O valor padrão de `demoivre` é `false`.


`exponentialize` converte funções circulares e hiperbólicas para a forma exponencial.
`demoivre` e `exponentialize` não podem
ambas serem `true` ao mesmo tempo.

<!-- category: Simplification -->
<!-- keywords: domain -->
<!-- signatures: domain -->
### Variable: domain

Valor padrão: `real`


Quando `domain` for escolhida para `complex`, `sqrt (x^2)` permanecerá
`sqrt (x^2)` em lugar de retornar `abs(x)`.

<!-- category: Simplification -->
<!-- keywords: expand -->
<!-- signatures: expand(expr), expand(expr, p, n) -->
### Function: expand (expr)

Expande a expressão *expr*.
Produtos de somas e somas exponenciadas são
multiplicadas para fora, numeradores de expressões racionais que são adições são
quebradas em suas respectivas parcelas, e multiplicação (comutativa
e não comutativa) é distribuída sobre a adição em todos os níveis de
*expr*.


Para polinômios se pode usar frequêntemente `ratexpand` que possui um
algorítmo mais eficiente.


`maxnegex` e `maxposex` controlam o máximo expoente negativo e
o máximo expoente positivo, respectivamente, que irão expandir.


`expand (expr, p, n)` expande *expr*, 
usando *p* para `maxposex` e *n* para `maxnegex`.
Isso é útil com o objetivo de expandir partes mas não tudo em uma expressão.


`expon` - o expoente da maior potência negativa que é
automaticamente expandida (independente de chamadas a `expand`).  Por Exemplo
se `expon` for 4 então `(x+1)^(-5)` não será automaticamente expandido.


`expop` - o maior expoente positivo que é automaticamente
expandido.  Dessa forma `(x+1)^3`, quando digitado, será automaticamente expandido
somente se `expop` for maior que ou igual a 3.  Se for desejado ter
`(x+1)^n` expandido onde `n` é maior que `expop` então executando
`expand ((x+1)^n)` trabalhará somente se `maxposex` não for menor que `n`.


O sinalizador `expand` usado com `ev` causa expansão.


O arquivo `simplification/facexp.mac`




contém muitas funções relacionadas (em particular `facsum`, `factorfacsum`
e `collectterms`, que são chamadas automaticamente) e variáveis (`nextlayerfactor`
e `facsum_combine`) que fornecem ao usuário com a habilidade para estruturar
expressões por expansão controlada.

Descrições breves de função estão disponível em `simplification/facexp.usg`.
Um arquivo demonstrativo está disponível fazendo `demo("facexp")`.

<!-- category: Simplification -->
<!-- keywords: expandwrt -->
<!-- signatures: expandwrt(expr, x_1, ..., x_n) -->
### Function: expandwrt (expr, x_1, ..., x_n)

Expande a expressão `expr` com relação às 
variáveis *x_1*, ..., *x_n*.
Todos os produtos envolvendo as variáveis aparecem explicitamente.  A forma retornada
será livre de produtos de somas de expressões que não estão livres das
variáveis.   *x_1*, ..., *x_n*
podem ser variáveis, operadores, ou expressões.


Por padrão, denominadores não são expandidos, mas isso pode ser controlado
através do comutador `expandwrt_denom`.


Essa função, `expandwrt`, não é automaticamente chamada a partir de
`simplification/stopex.mac`.

<!-- category: Simplification -->
<!-- keywords: expandwrt_denom -->
<!-- signatures: expandwrt_denom -->
### Variable: expandwrt_denom

Valor padrão: `false`


`expandwrt_denom` controla o tratamento de expressões
racionais por `expandwrt`.  Se `true`, então ambos o numerador e
o denominador da expressão serão expandidos conforme os
argumentos de `expandwrt`, mas se `expandwrt_denom` for `false`, então somente
o numerador será expandido por aquele caminho.

<!-- category: Simplification -->
<!-- keywords: expandwrt_factored -->
<!-- signatures: expandwrt_factored(expr, x_1, ..., x_n) -->
### Function: expandwrt_factored (expr, x_1, ..., x_n)

é similar a `expandwrt`, mas trata expressões que são produtos um tanto quanto diferentemente.
`expandwrt_factored` expande somente sobre esses fatores de `expr`
que contiverem as variáveis *x_1*, ..., *x_n*.



Essa função é automaticamente chamada a aprtir de `simplification/stopex.mac`.

<!-- category: Simplification -->
<!-- keywords: expon -->
<!-- signatures: expon -->
### Variable: expon

Valor padrão: 0


`expon` é o expoente da maior potência negativa que
é automaticamente expandido (independente de chamadas a `expand`).  Por
exemplo, se `expon` for 4 então `(x+1)^(-5)` não será automaticamente
expandido.

<!-- category: Simplification -->
<!-- keywords: exponentialize -->
<!-- signatures: exponentialize(expr) -->
### Function: exponentialize (expr)

A função `exponentialize (expr)` converte 
funções circulares e hiperbólicas em *expr* para exponenciais,
sem escolher a variável global `exponentialize`.


Quando a variável `exponentialize` for `true`,
todas as funções circulares e hiperbólicas  são convertidas para a forma exponencial.
O valor padrão é `false`.


`demoivre` converte exponenciais complexas em funções circulares.
`exponentialize` e `demoivre` não podem
ambas serem `true` ao mesmo tempo.

<!-- category: Simplification -->
<!-- keywords: expop -->
<!-- signatures: expop -->
### Variable: expop

Valor padrão: 0


`expop` - o maior expoente positivo que é 
automaticamente expandido.  Dessa forma `(x+1)^3`, quando digitado, será
automaticamente expandido somente se `expop` for maior que ou igual a 3.  
Se for desejado ter `(x+1)^n` expandido onde `n` é maior que 
`expop` então executando `expand ((x+1)^n)` trabalhará somente se `maxposex` não for 
menor que `n`.

<!-- category: Simplification -->
<!-- keywords: factlim -->
<!-- signatures: factlim -->
### Variable: factlim

Valor padrão: -1


`factlim` especifica o maior fatorial que é
automaticamente expandido.  Se for -1 então todos os inteiros são expandidos.

<!-- category: Simplification -->
<!-- keywords: intosum -->
<!-- signatures: intosum(expr) -->
### Function: intosum (expr)

Move fatores multiplicativos fora de um somatório para dentro.
Se o índice for usado na
expressão de fora, então a função tentará achar um índice
razoável, o mesmo que é feito para `sumcontract`.  Isso é essencialmente a
idéia inversa da propriedade `outative` de somatórios, mas note que isso
não remove essa propriedade, somente pula sua verificação.



Em alguns casos,
um `scanmap (multthru, expr)` pode ser necessário antes de `intosum`.

<!-- category: Simplification -->
<!-- keywords: lassociative -->
<!-- signatures: lassociative -->
### Variable: lassociative

`declare (g, lassociative)` diz ao
simplificador do Maxima que `g` é associativa à esquerda.  E.g., `g (g (a, b), g (c, d))` irá
simplificar para `g (g (g (a, b), c), d)`.

<!-- category: Simplification -->
<!-- keywords: linear -->
<!-- signatures: linear -->
### Variable: linear

Uma das propriedades operativas do Maxima.  Para funções de uma única variável `f` então
declarada, a "expansão" `f(x + y)` retorna `f(x) + f(y)`,
`f(a*x)` retorna `a*f(x)` tomando
lugar onde `a` for uma "constante".  para funções de dois ou mais argumentos,
"linearidade" é definida para ser como no caso de `sum` ou `integrate`,
i.e., `f (a*x + b, x)` retorna `a*f(x,x) + b*f(1,x)`
para `a` e `b` livres de `x`.


`linear` é equivalente a `additive` e `outative`.
Veja também `opproperties`.

<!-- category: Simplification -->
<!-- keywords: mainvar -->
<!-- signatures: mainvar -->
### Variable: mainvar

Você pode declarar variáveis para serem `mainvar` (variável principal).  A escala de
ordenação para átomos é essencialmente: números < constantes (e.g., `%e`, `%pi`) <
escalares < outras variáveis < mainvars.  E.g., compare `expand ((X+Y)^4)`
com `(declare (x, mainvar), expand ((x+y)^4))`.  (Nota: Cuidado deve ser
tomado se você eleger o uso desse recurso acima.  E.g., se você subtrair uma
expressão na qual `x` for uma `mainvar` de uma na qual `x` não seja uma
`mainvar`, resimplificação e.g. com `ev (expr, simp)` pode ser
necessária se for para ocorrer um cancelamento.  Também, se você grava uma
expressão na qual `x` é uma `mainvar`, você provavelmente pode também gravar `x`.)

<!-- category: Simplification -->
<!-- keywords: maxapplydepth -->
<!-- signatures: maxapplydepth -->
### Variable: maxapplydepth

Valor padrão: 10000


`maxapplydepth` é a máxima definição para a qual `apply1`
e `apply2` irão pesquisar.

<!-- category: Simplification -->
<!-- keywords: maxapplyheight -->
<!-- signatures: maxapplyheight -->
### Variable: maxapplyheight

Valor padrão: 10000


`maxapplyheight` é a elevação máxima a qual `applyb1`
irá alcançar antes de abandonar.

<!-- category: Simplification -->
<!-- keywords: maxnegex -->
<!-- signatures: maxnegex -->
### Variable: maxnegex

Valor padrão: 1000


`maxnegex` é o maior expoente negativo que será
expandido pelo comando `expand` (veja também `maxposex`).

<!-- category: Simplification -->
<!-- keywords: maxposex -->
<!-- signatures: maxposex -->
### Variable: maxposex

Valor padrão: 1000


`maxposex` é o maior expoente que será
expandido com o comando `expand` (veja também `maxnegex`).

<!-- category: Simplification -->
<!-- keywords: multiplicative -->
<!-- signatures: multiplicative -->
### Variable: multiplicative

`declare (f, multiplicative)` diz ao simplificador do Maxima que `f` é multiplicativa.



1. Se `f` for uma função de uma única variável, sempre que o simplificador encontrar `f` aplicada
a um produto, `f` distribue sobre aquele produto.  E.g., `f(x*y)`
simplifica para `f(x)*f(y)`.
2. Se `f` é uma função de 2 ou mais argumentos, multiplicatividade é
definida como multiplicatividade no primeiro argumento para `f`, e.g.,
`f (g(x) * h(x), x)` simplifica para `f (g(x) ,x) * f (h(x), x)`.


Essa simplificação não ocorre quando `f` é aplicada a expressões da
forma `product (x[i], i, m, n)`.

<!-- category: Simplification -->
<!-- keywords: negdistrib -->
<!-- signatures: negdistrib -->
### Variable: negdistrib

Valor padrão: `true`


Quando `negdistrib` for `true`, -1 distribue
sobre uma expressão.  E.g., `-(x + y)` transforma-se em `- y - x`.  Mudando o valor de `negdistrib` para `false`
permitirá que `- (x + y)` seja mostrado como foi escrito.  Isso algumas vezes é útil
mas seja muito cuidadoso: como o sinalizador `simp`, isso é um sinalizador que você pode não
querer escolher para `false` como algo natural ou necessário com excessão
de usar localmente no seu Maxima.

<!-- category: Simplification -->
<!-- keywords: negsumdispflag -->
<!-- signatures: negsumdispflag -->
### Variable: negsumdispflag

Valor padrão: `true`


Quando `negsumdispflag` for `true`, `x - y` é mostrado como `x - y`
em lugar de como `- y + x`.  Escolhendo isso para `false` faz com que a verificação especial em
visualização para a diferença das duas expressões não seja concluída.  Uma
aplicação é que dessa forma `a + %i*b` e `a - %i*b` podem ambos serem mostrados pelo
mesmo caminho.

<!-- category: Simplification -->
<!-- keywords: noeval -->
<!-- signatures: noeval -->
### Variable: noeval

`noeval` suprime a fase de avaliação de `ev`.  Isso é útil em
conjunção com outros comutadores e para fazer com que expressões      
sejam resimplificadas sem serem reavaliadas.

<!-- category: Simplification -->
<!-- keywords: noun -->
<!-- signatures: noun -->
### Variable: noun

`noun` é uma das opções do comando `declare`.  Essa opção faz com que um
função seja declarada como "noun" (substantivo), significando que ela não deve ser avaliada
automaticamente.

<!-- category: Simplification -->
<!-- keywords: noundisp -->
<!-- signatures: noundisp -->
### Variable: noundisp

Valor padrão: `false`


Quando `noundisp` for `true`, substantivos (nouns) são mostrados com
um apóstrofo.  Esse comutador é sempre `true` quando mostrando definições de
função.

<!-- category: Simplification -->
<!-- keywords: nouns -->
<!-- signatures: nouns -->
### Variable: nouns

`nouns` é um `evflag` (sinalizador de avaliação). Quando usado como uma opção para o comando `ev`,
`nouns` converte todas as
formas substantivas ("noun") que ocorrem na expressão que está sendo avaliada para verbos ("verbs"), i.e.,
avalia essas expressões.  Veja também `noun`, `nounify`, `verb`, e `verbify`.

<!-- category: Simplification -->
<!-- keywords: numer -->
<!-- signatures: numer -->
### Variable: numer

`numer` faz com que algumas funções matemáticas (incluindo exponenciação)
com argumentos numéricos sejam avaliados em ponto flutuante. Isso faz com que
variáveis em `expr` às quais tenham sido dados valores numéricos a elas sejam substituídas pelos
seus valores correspondentes.  `numer` também escolhe o sinalizador `float` para `on`.

<!-- category: Simplification -->
<!-- keywords: numerval -->
<!-- signatures: numerval(x_1, expr_1, ..., var_n, expr_n) -->
### Function: numerval (x_1, expr_1, ..., var_n, expr_n)

Declara as variáveis `x_1`, ..., *x_n* para terem
valores numéricos iguais a `expr_1`, ..., `expr_n`.
O valor numérico é avaliado e substituido para a variável
em quaisquer expressões na qual a variável ocorra se o sinalizador `numer` for
`true`. Veja também `ev`.


As expressões `expr_1`, ..., `expr_n` podem ser quaisquer expressões,
não necessariamente numéricas.

<!-- category: Simplification -->
<!-- keywords: opproperties -->
<!-- signatures: opproperties -->
### Variable: opproperties

`opproperties` é a lista de propriedades de operadores especiais reconhecidas pelo
simplificador do Maxima:
`linear`, `additive`, `multiplicative`, `outative` (veja logo abaixo), `evenfun`,
`oddfun`, `commutative`, `symmetric`, `antisymmetric`, `nary`, 
`lassociative`, `rassociative`.

<!-- category: Simplification -->
<!-- keywords: opsubst -->
<!-- signatures: opsubst -->
### Variable: opsubst

Valor padrão: `true`


Quando `opsubst` for `false`, `subst` não tenta
substituir dentro de um operador de uma expressão.  E.g., 
`(opsubst: false, subst (x^2, r, r+r[0]))` irá trabalhar.

<!-- category: Simplification -->
<!-- keywords: outative -->
<!-- signatures: outative -->
### Variable: outative

`declare (f, outative)` diz ao simplificador do Maxima que fatores constantes
no argumento de `f` podem ser puxados para fora.



1. Se `f` for uma função de uma única variável, sempre que o simplificador encontrar `f` aplicada
a um produto, aquele produto será particionado em fatores que são
constantes e fatores que não são e os fatores constantes serão
puxados para fora.  E.g., `f(a*x)` simplificará para `a*f(x)` onde `a` é uma
constante.  Fatores de constantes não atômicas não serão puxados para fora.
2. Se `f` for uma função de 2 ou mais argumentos, a colocação para fora é definida
como no caso de `sum` ou `integrate`, i.e., `f (a*g(x), x)` irá simplificar
para `a * f(g(x), x)` sendo `a` livre de `x`.


`sum`, `integrate`, e `limit` são todas `outative`.

<!-- category: Simplification -->
<!-- keywords: posfun -->
<!-- signatures: posfun -->
### Variable: posfun

`declare (f, posfun)` declara `f` para ser uma função positiva.
`is (f(x) > 0)` retorna `true`.

<!-- category: Simplification -->
<!-- keywords: radcan -->
<!-- signatures: radcan(expr) -->
### Function: radcan (expr)

Simplifica *expr*, que pode conter logarítmos, exponenciais, e
radicais, convertendo essa expressão em uma forma que é canônica sobre uma ampla
classe de expressões e uma dada ordenação de variáveis; isto é, todas
formas funcionalmente equivalentes são mapeadas em uma única forma.  Para uma
classe um tanto quanto ampla de expressões, `radcan` produz uma forma regular.
Duas expressões equivalentes nessa classe não possuem necessáriamente a
mesma aparência, mas suas diferenças podem ser simplificadas por `radcan` para
zero.


Para algumas expressões `radcan` é que consome inteiramente o tempo.  Esse
é o custo de explorar certos relacionamentos entre os componentes da
expressão para simplificações baseadas sobre fatoração e
expansões de fração-parcial de expoentes.  




Quando `%e_to_numlog` for `true`, 
`%e^(r*log(expr))` simplifica para `expr^r` se `r` for um número racional.


Quando `radexpand` for `false`, certas transformações são inibidas.
`radcan (sqrt (1-x))` permanece `sqrt (1-x)`
e não é simplificada para `%i sqrt (x-1)`. 
`radcan (sqrt (x^2 - 2*x + 11))` permanece `sqrt (x^2 - 2*x + 1)`
e não é simplificada para `x - 1`.



`example (radcan)` mostra alguns exemplos.

<!-- category: Simplification -->
<!-- keywords: radexpand -->
<!-- signatures: radexpand -->
### Variable: radexpand

Valor padrão: `true`


`radexpand` controla algumas simplificações de radicais.


Quando `radexpand` for `all`, faz com que n-ésimas raízes de
fatores de um produto que são potências de n sejam puxados para fora do
radical.  E.g. Se `radexpand` for `all`, `sqrt (16*x^2)` simplifica para `4*x`.



Mais particularmente, considere `sqrt (x^2)`.


- *
Se `radexpand` for `all` or `assume (x > 0)` tiver sido executado, 
`sqrt(x^2)` simplifica para `x`.
- *
Se `radexpand` for `true` e `domain` for `real` (isso é o padrão), 
`sqrt(x^2)` simplifica para `abs(x)`.
- *
Se `radexpand` for `false`, ou `radexpand` for `true` e `domain` for `complex`, 
`sqrt(x^2)` não é simplificado.



Note que `domain` somente interessa quando `radexpand` for `true`.

<!-- category: Simplification -->
<!-- keywords: radsubstflag -->
<!-- signatures: radsubstflag -->
### Variable: radsubstflag

Valor padrão: `false`


`radsubstflag`, se `true`, permite a `ratsubst` fazer
substituições tais como `u` por `sqrt (x)` em `x`.

<!-- category: Simplification -->
<!-- keywords: rassociative -->
<!-- signatures: rassociative -->
### Variable: rassociative

`declare (g, rassociative)` diz ao simplificador do
Maxima que `g` é associativa à direita.  E.g.,
`g(g(a, b), g(c, d))` simplifica para `g(a, g(b, g(c, d)))`.

<!-- category: Simplification -->
<!-- keywords: scsimp -->
<!-- signatures: scsimp(expr, rule_1, ..., rule_n) -->
### Function: scsimp (expr, rule_1, ..., rule_n)

Simplificação Sequêncial Comparativa (método devido a Stoute).
`scsimp` tenta simplificar *expr*
conforme as regras *rule_1*, ..., *rule_n*.
Se uma expressão pequena for obtida, o processo
repete-se.  De outra forma após todas as simplificações serem tentadas, `scsimp` retorna
a resposta original.



`example (scsimp)` mostra alguns exemplos.

<!-- category: Simplification -->
<!-- keywords: simpsum -->
<!-- signatures: simpsum -->
### Variable: simpsum

Valor padrão: `false`


Quando `simpsum` for `true`, o resultado de uma `sum` é
simplificado.  Essa simplificação pode algumas vezes estar apta a produzir uma
forma fechada.  Se `simpsum` for `false` ou se a forma com apóstrofo `'sum` for usada, o valor é uma
forma substantiva aditiva que é uma representação da notação sigma usada em
matemática.

<!-- category: Simplification -->
<!-- keywords: sumcontract -->
<!-- signatures: sumcontract(expr) -->
### Function: sumcontract (expr)

Combina todas as parcelas de um somatório que possuem
limites superiores e inferiores que diferem por constantes. O resultado é uma
expressão contendo um somatório para cada escolha de cada tais somatórios
adicionados a todos os termos extras apropriados que tiveram de ser extraídos para a forma
dessa adição.  `sumcontract` combina todas as somas compatíveis e usa os
indices de uma as somas se puder, e então tenta formar um
índice razoável se não for usar qualquer dos fornecidos.



Isso pode ser necessário fazer um `intosum (expr)` antes de `sumcontract`.

<!-- category: Simplification -->
<!-- keywords: sumexpand -->
<!-- signatures: sumexpand -->
### Variable: sumexpand

Valor padrão: `false`


Quando `sumexpand` for `true`, produtos de somas e
somas exponeciadas simplificam para somas aninhadas.


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

Valor padrão: `true`


Quando `sumsplitfact` for `false`,

`minfactorial` é aplicado após um `factcomb`.

<!-- category: Simplification -->
<!-- keywords: symmetric -->
<!-- signatures: symmetric -->
### Variable: symmetric

`declare (h, symmetric)` diz ao simplificador
do Maxima que `h` é uma função simétrica.  E.g., `h (x, z, y)` 
simplifica para `h (x, y, z)`.


`commutative` é sinônimo de `symmetric`.

<!-- category: Simplification -->
<!-- keywords: unknown -->
<!-- signatures: unknown(expr) -->
### Function: unknown (expr)

Retorna `true` se e somente se *expr* contém um operador ou função
não reconhecida pelo simplificador do Maxima.

