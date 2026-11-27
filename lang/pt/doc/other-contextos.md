## Contextos

<!-- category: Other -->
<!-- keywords: activate -->
<!-- signatures: activate(context_1, ..., context_n) -->
### Function: activate (context_1, ..., context_n)

Ativa os contextos *context_1*, ..., *context_n*.
Os factos nesses contextos estão então disponíveis para
fazer deduções e recuperar informação.
Os factos nesses contextos não são listadas através de `facts ()`.


A variável `activecontexts` é a lista
de contextos que estão activos pelo caminho da função `activate`.

<!-- category: Other -->
<!-- keywords: activecontexts -->
<!-- signatures: activecontexts -->
### Variable: activecontexts

Valor por omissão: `[]`


`activecontexts` é a lista de contextos que estão activos
pelo caminho da função `activate`, em oposição a sendo activo porque
eles são subcontextos do contexto corrente.

<!-- category: Other -->
<!-- keywords: assume -->
<!-- signatures: assume(pred_1, ..., pred_n) -->
### Function: assume (pred_1, ..., pred_n)

Adiciona predicados *pred_1*, ..., *pred_n* ao contexto corrente.
Se um predicado for incossistente ou redundante 
com os predicados no contexto corrente,
esses predicados não são adicionados ao contexto.
O contexto acumula predicados de cada chamada a `assume`.


`assume` retorna uma lista cujos elementos são os predicados adicionados ao contexto
ou os átomos `redundant` ou `inconsistent` onde for aplicável.


Os predicados *pred_1*, ..., *pred_n* podem somente ser expressões
com os operadores relacionais `< <= equal notequal >=` e `>`.
Predicados não podem ser expressões de igualdades literais `=` ou expressões de desigualdades literais `#`,
nem podem elas serem funções de predicado tais como `integerp`.


Predicados combinados da forma `pred_1 and ... and pred_n`
são reconhecidos,
mas não `pred_1 or ... or pred_n`.
`not pred_k` é reconhecidos se *pred_k* for um predicado relacional.
Expressões da forma `not (pred_1 e pred_2)`
and `not (pred_1 or pred_2)`
não são reconhecidas.


O mecanismo de dedução do Maxima não é muito forte;
exitem consequências muito óbvias as quais não podem ser determinadas por meio de `is`.
Isso é uma fraqueza conhecida.


`assume` avalia seus argumentos.


Veja também `is`, `facts`, `forget`, `context`, e `declare`.


Exemplos:
















```maxima
(%i1) assume (xx > 0, yy < -1, zz >= 0);
(%o1)              [xx > 0, yy < - 1, zz >= 0]
(%i2) assume (aa < bb and bb < cc);
(%o2)                  [bb > aa, cc > bb]
(%i3) facts ();
(%o3)     [xx > 0, - 1 > yy, zz >= 0, bb > aa, cc > bb]
(%i4) is (xx > yy);
(%o4)                         true
(%i5) is (yy < -yy);
(%o5)                         true
(%i6) is (sinh (bb - aa) > 0);
(%o6)                         true
(%i7) forget (bb > aa);
(%o7)                       [bb > aa]
(%i8) prederror : false;
(%o8)                         false
(%i9) is (sinh (bb - aa) > 0);
(%o9)                        unknown
(%i10) is (bb^2 < cc^2);
(%o10)                       unknown
```

<!-- category: Other -->
<!-- keywords: assume_pos -->
<!-- signatures: assume_pos -->
### Variable: assume_pos

Valor por omissão: `false`


Quando `assume_pos` for `true`
e o sinal de um parâmetro *x* não pode ser determinado a partir do contexto corrente
ou outras considerações,
`sign` e `asksign (x)` retornam `true`.
Isso pode impedir algum questionamento de `asksign` gerado automaticamente,
tal como pode surgir de `integrate` ou de outros cálculos.


Por padrão, um parâmetro é *x* tal como `symbolp (x)`
or `subvarp (x)`.
A classe de expressões consideradas parâmetros pode ser modificada para alguma abrangência
através da variável `assume_pos_pred`.


`sign` e `asksign` tentam deduzir o sinal de expressões
a partir de sinais de operandos dentro da expressão.
Por exemplo, se `a` e `b` são ambos positivos,
então `a + b` é também positivo.


Todavia, não existe caminho para desviar todos os questionamentos de `asksign`.
Particularmente, quando o argumento de `asksign` for uma
diferença `x - y` ou um logaritmo `log(x)`,
`asksign` sempre solicita uma entrada ao utilizador,
mesmo quando `assume_pos` for `true` e `assume_pos_pred` for
uma função que retorna `true` para todos os argumentos.

<!-- category: Other -->
<!-- keywords: assume_pos_pred -->
<!-- signatures: assume_pos_pred -->
### Variable: assume_pos_pred

Valor por omissão: `false`


Quando `assume_pos_pred` for atribuído o nome de uma função
ou uma expressão lambda de um argumento *x*,
aquela função é chamada para determinar
se *x* é considerado um parâmetro para o propósito de `assume_pos`.
`assume_pos_pred` é ignorado quando `assume_pos` for `false`.


A função `assume_pos_pred` é chamada através de `sign` e de `asksign`
com um argumento *x*
que é ou um átomo, uma variável subscrita, ou uma expressão de chamada de função.
Se a função `assume_pos_pred` retorna `true`,
*x* é considerado um parâmetro para o propósito de `assume_pos`.


Por padrão, um parâmetro é *x* tal que `symbolp (x)` ou `subvarp (x)`.


Veja também `assume` e `assume_pos`.


Exemplos:















```maxima
(%i1) assume_pos: true$
(%i2) assume_pos_pred: symbolp$
(%i3) sign (a);
(%o3)                          pos
(%i4) sign (a[1]);
(%o4)                          pnz
(%i5) assume_pos_pred: lambda ([x], display (x), true)$
(%i6) asksign (a);
                              x = a

(%o6)                          pos
(%i7) asksign (a[1]);
                             x = a
                                  1

(%o7)                          pos
(%i8) asksign (foo (a));
                           x = foo(a)

(%o8)                          pos
(%i9) asksign (foo (a) + bar (b));
                           x = foo(a)

                           x = bar(b)

(%o9)                          pos
(%i10) asksign (log (a));
                              x = a

Is  a - 1  positive, negative, or zero?

p;
(%o10)                         pos
(%i11) asksign (a - b);
                              x = a

                              x = b

                              x = a

                              x = b

Is  b - a  positive, negative, or zero?

p;
(%o11)                         neg
```

<!-- category: Other -->
<!-- keywords: assumescalar -->
<!-- signatures: assumescalar -->
### Variable: assumescalar

Valor por omissão: `true`


`assumescalar` ajuda a governar se expressões `expr`
para as quais `nonscalarp (expr)` for `false`
são assumidas comportar-se como escalares
para certas transformações.


Tomemos `expr` representando qualquer expressão outra que não uma lista ou uma matriz,
e tomemos `[1, 2, 3]` representando qualquer lista ou matriz.
Então `expr . [1, 2, 3]` retorna `[expr, 2 expr, 3 expr]`
se `assumescalar` for `true`, ou `scalarp (expr)` for
`true`, ou `constantp (expr)` for `true`.


Se `assumescalar` for `true`, tais
expressões irão comportar-se como escalares somente para operadores
comutativos, mas não para multiplicação não comutativa `.`.


Quando `assumescalar` for `false`, tais
expressões irão comportar-se como não escalares.


Quando `assumescalar` for `all`,
tais expressões irão comportar-se como escalares para todos os operadores listados
acima.

<!-- category: Other -->
<!-- keywords: context -->
<!-- signatures: context -->
### Variable: context

Valor por omissão: `initial`


`context` nomeia a colecção de factos mantida através de `assume` e `forget`.
`assume` adiciona factos à colecção nomeada através de `context`,
enquanto `forget` remove factos.


Associando `context` para um nome *foo* altera o contexto corrente para *foo*.
Se o contexto especificado *foo* não existe ainda,
ele é criado automaticamente através de uma chamada a `newcontext`.

O contexto especificado é activado automaticamente.


Veja `contexts` para uma descrição geral do mecanismo de contexto.

<!-- category: Other -->
<!-- keywords: contexts -->
<!-- signatures: contexts -->
### Variable: contexts

Valor por omissão: `[initial, global]`


`contexts` é uma lista dos contextos que
existem actualmente, incluindo o contexto activo actualmente.


O mecanismo de contexto torna possível para um utilizador associar
e nomear uma porção seleccionada de factos, chamada um contexto.
Assim que isso for concluído, o utilizador pode ter o Maxima assumindo ou esquecendo grande quantidade
de factos meramente através da activação ou desativação seu contexto.


Qualquer átomo simbólico pode ser um contexto, e os factos contidos naquele
contexto irão ser retidos em armazenamento até que sejam destruídos um por um
através de chamadas a `forget` ou destruídos com um conjunto através de uma chamada a `kill`
para destruir o contexto que eles pertencem.


Contextos existem em uma hierarquía, com o raíz sempre sendo
o contexto `global`, que contém informações sobre Maxima que alguma
função precisa.  Quando em um contexto dado, todos os factos naquele
contexto estão "ativos" (significando que eles são usados em deduções e
recuperados) como estão também todos os factos em qualquer contexto que for um subcontexto
do contexto activo.


Quando um novo Maxima for iniciado, o utilizador está em um
contexto chamado `initial`, que tem `global` como um subcontexto.


Veja também `facts`, `newcontext`,
`supcontext`, `killcontext`, `activate`, `deactivate`, `assume`, e `forget`.

<!-- category: Other -->
<!-- keywords: deactivate -->
<!-- signatures: deactivate(context_1, ..., context_n) -->
### Function: deactivate (context_1, ..., context_n)

Desativa os contextos especificados *context_1*, ..., *context_n*.

<!-- category: Other -->
<!-- keywords: facts -->
<!-- signatures: facts(item), facts() -->
### Function: facts (item)

Se *item* for o nome de um contexto,
`facts (item)` retorna uma lista
de factos no contexto especificado.


Se *item* não for o nome de um contexto,
`facts (item)` retorna uma lista de factos conhecidos sobre *item* no contexto
actual.  Fatos que estão atuvos, mas em um diferente contexto, não são listados.


`facts ()` (i.e., sem argumento) lista o contexto actual.

<!-- category: Other -->
<!-- keywords: features -->
<!-- signatures: features -->
### Variable: features

Maxima recnhece ceertas propriedades matemáticas de funções e variáveis.
Essas são chamadas "recursos".


`declare (x, foo)` fornece a propriedade *foo* para a função ou variável *x*.


`declare (foo, recurso)` declara um novo recurso *foo*.
Por exemplo,
`declare ([red, green, blue], feature)`
declara três novos recursos, `red`, `green`, e `blue`.


O predicado `featurep (x, foo)`
retorna `true` se *x* possui a propriedade *foo*,
e `false` de outra forma.


A infolista `features` é uma lista de recursos conhecidos.
São esses
`integer`, `noninteger`, `even`, `odd`, `rational`,
`irrational`, `real`, `imaginary`, `complex`,
`analytic`, `increasing`, `decreasing`, `oddfun`,
`evenfun`, `posfun`, `commutative`, `lassociative`,
`rassociative`, `symmetric`, e `antisymmetric`,
mais quaisquer recursos definidos pelo utilizador.


`features` é uma lista de recursos matemáticos.
Existe também uma lista de recursos não matemáticos, recursos dependentes do sistema. Veja `status`.

<!-- category: Other -->
<!-- keywords: forget -->
<!-- signatures: forget(pred_1, ..., pred_n), forget(L) -->
### Function: forget (pred_1, ..., pred_n)

Remove predicados estabelecidos através de `assume`.
Os predicados podem ser expressões equivalentes a (mas não necessáriamente idênticas a)
esses prevamentes assumidos.


`forget (L)`, onde *L* é uma lista de predicados,
esquece cada item da lista.

<!-- category: Other -->
<!-- keywords: killcontext -->
<!-- signatures: killcontext(context_1, ..., context_n) -->
### Function: killcontext (context_1, ..., context_n)

Mata os contextos *context_1*, ..., *context_n*.


Se um dos contextos estiver for o contexto actual, o novo contexto
actual irá tornar-se o primeiro subcontexto disponível do contexto
actual que não tiver sido morto.  Se o primeiro contexto disponível
não morto for `global` então `initial` é usado em seu lugar.  Se o contexto
`initial` for morto, um novo, porém vazio contexto `initial` é criado.


`killcontext` recusa-se a matar um contexto que estiver
ativo actualmente, ou porque ele é um subcontexto do contexto
actual, ou através do uso da função `activate`.


`killcontext` avalia seus argumentos.
`killcontext` retorna `done`.

<!-- category: Other -->
<!-- keywords: newcontext -->
<!-- signatures: newcontext(nome) -->
### Function: newcontext (nome)

Cria um novo contexto, porém vazio, chamado *nome*, que
tem `global` como seu único subcontexto.  O contexto recentemente criado
torna-se o contexto activo actualmente.


`newcontext` avalia seu argumento.
`newcontext` retorna *nome*.

<!-- category: Other -->
<!-- keywords: supcontext -->
<!-- signatures: supcontext(nome, context), supcontext(nome) -->
### Function: supcontext (nome, context)

Cria um novo contexto, chamado *nome*,
que tem *context* como um subcontexto.
*context* deve existir.


Se *context* não for especificado, o contexto actual é assumido.

