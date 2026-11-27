## Regras e Modelos

<!-- category: Calculus -->
<!-- keywords: apply1 -->
<!-- signatures: apply1(expr, rule_1, ..., rule_n) -->
### Function: apply1 (expr, rule_1, ..., rule_n)

Repetidamente aplica *rule_1* a
*expr* até que isso falhe, então repetidamente aplica a mesma regra a todas
as subexpressões de *expr*, da esquerda para a direita, até que *rule_1* tenha falhado
sobre todas as subexpressões.  Chama o resultado da transformação de *expr* dessa
maneira de *expr_2*.  Então *rule_2* é aplicada no mesmo estilo
iniciando no topo de *expr_2*.  Quando *rule_n* falhar na subexpressão
final, o resultado é retornado.


`maxapplydepth` é a intensidade de nível mais distante de subexpressões processadas por
`apply1` e `apply2`.


Veja também `applyb1`, `apply2`, e `let`.

<!-- category: Calculus -->
<!-- keywords: apply2 -->
<!-- signatures: apply2(expr, rule_1, ..., rule_n) -->
### Function: apply2 (expr, rule_1, ..., rule_n)

Se *rule_1* falhar sobre uma dada subexpressão, então *rule_2* é
repetidamente aplicada, etc.  Somente se todas as regras falharem sobre uma dada
subexpressão é que o conjunto completo de regras é repetidamente aplicada à próxima
subexpressão.  Se uma das regras obtém sucesso, então a mesma
subexpressão é reprocessada, iniciando com a primeira regra.


`maxapplydepth` é a intensidade do nível mais distante de subexpressões processadas através de
`apply1` e `apply2`.


Veja também `apply1` e `let`.

<!-- category: Calculus -->
<!-- keywords: applyb1 -->
<!-- signatures: applyb1(expr, rule_1, ..., rule_n) -->
### Function: applyb1 (expr, rule_1, ..., rule_n)

Repetidamente aplica *rule_1* para a subexpressão mais distante de *expr* até falhar,
então repetidamente aplica a mesma regra um nível mais acima (i.e., subexpressãos mais larga),
até que *rule_1* tenha falhado sobre a expressão de nível mais alto.
Então *rule_2* é aplicada com o mesmo estilo para o resultado de *rule_1*.
após *rule_n* ter sido aplicada à expressão de nível mais elevado,
o resultado é retornado.


`applyb1` é similar a `apply1` mas trabalha da
base para cima em lugar de do topo para baixo.


`maxapplyheight` é o ápice que `applyb1` encontra
antes de interromper.


Veja também `apply1`, `apply2`, e `let`.

<!-- category: Calculus -->
<!-- keywords: clear_rules -->
<!-- signatures: clear_rules() -->
### Function: clear_rules ()

Executa `kill (rules)` e então re-escolhe o próximo número de regra para 1
para adição `+`, multiplicação `*`, e exponenciação `^`.

<!-- category: Calculus -->
<!-- keywords: current_let_rule_package -->
<!-- signatures: current_let_rule_package -->
### Variable: current_let_rule_package

Valor por omissão: `default_let_rule_package`


`current_let_rule_package` é o nome do pacote de regras que está sendo usado por
funções no pacote `let` (`letsimp`, etc.) 
se nenhum outro pacote de regras for especificado.
A essa variável pode ser atribuído o nome de qualquer pacote de regras definido
via comando `let`.


Se uma chamada tal como `letsimp (expr, nome_pct_regras)` for feita,
o pacote de regras `nome_pct_regras` é usado para aquela chamada de função somente,
e o valor de `current_let_rule_package` não é alterado.

<!-- category: Calculus -->
<!-- keywords: default_let_rule_package -->
<!-- signatures: default_let_rule_package -->
### Variable: default_let_rule_package

Valor por omissão: `default_let_rule_package`



`default_let_rule_package` é o nome do pacote de regras usado quando um
não for explicitamente escolhido pelo utilizador com `let` ou através de alteração do valor de
`current_let_rule_package`.

<!-- category: Calculus -->
<!-- keywords: defmatch -->
<!-- signatures: defmatch(prognome, modelo, x_1, ..., x_n), defmatch(prognome, modelo) -->
### Function: defmatch (prognome, modelo, x_1, ..., x_n)

Define uma função `prognome(expr, x_1, ..., x_n)`
que testa *expr* para ver se essa expressão coincide com *modelo*.


*modelo* é uma expressão contendo os argumentos modelo *x_1*, ..., *x_n* (se existir algum)
e alguns modelos de variáveis (se existir algum).
os argumentos modelo são fornecidos explicitamente como argumentos para `defmatch` enquanto os modelos de variáveis
são declarados através da função `matchdeclare`.
Qualquer variável não declarada como modelo em `matchdeclare`
ou como um argumento modelo em `defmatch` coincide somente com si mesma.


O primeiro argumento para a função criada *prognome* é uma expressão
a serem comparadas contra o modelo  e os outros argumentos são os atuais argumetnos
que correspondem às variáveis respectivas *x_1*, ..., *x_n* no modelo.


Se a tentativa de coincidência obtiver sucesso, *prognome* retorna
uma lista de equações cujos lados esquerdos são os
argumetnos de modelo e variáveis de modelo, e cujo lado direito forem as subexpressões
cujos argumentos de modelo e as variáveis coincidem.
Os modelos de variáveis, mas não tos argumentos de modelo, são atribuídos às subexpressões que coincidirem.
Se a coincidência falhar, *prognome* retorna `false`.  


Um modelo literal
(isto é, um modelo que não contiver nem argumentos de modelo nem variáveis de modelo)
retorna `true` se a coincidência ocorrer.


Veja também `matchdeclare`, `defrule`, `tellsimp`, e `tellsimpafter`.


Exemplos:


Define uma função `linearp(expr, x)` que
testa `expr` para ver se essa expressão da forma `a*x + b`
tal que `a` e `b` não contenham `x` e `a` seja não nulo.
Essa função de coincidência coincide com expressões que sejam lineares em qualquer variável,
por que o argumento de modelo `x` é fornecido para `defmatch`.












```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b, freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b, x);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2, z);
                         2
(%o3)              [b = y , a = y + 4, x = z]
(%i4) a;
(%o4)                         y + 4
(%i5) b;
                                2
(%o5)                          y
(%i6) x;
(%o6)                           x
```


Define uma função `linearp(expr)` que testa `expr`
para ver se essa expressão é da forma `a*x + b`
tal que `a` e `b` não contenham `x` e `a` seja não nulo.
Essa função de coincidência somente coincide com expressões lineares em `x`,
não em qualquer outra variável, porque nenhum argumento de modelo é fornecido a `defmatch`.









```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b, freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2);
(%o3)                         false
(%i4) linearp (3*x + (y + 1)*x + y^2);
                             2
(%o4)                  [b = y , a = y + 4]
```


Define uma função `checklimits(expr)` que testa `expr`
para ver se essa expressão é uma integral definida.

 












```maxima
(%i1) matchdeclare ([a, f], true);
(%o1)                         done
(%i2) constinterval (l, h) := constantp (h - l);
(%o2)        constinterval(l, h) := constantp(h - l)
(%i3) matchdeclare (b, constinterval (a));
(%o3)                         done
(%i4) matchdeclare (x, atom);
(%o4)                         done
(%i5) simp : false;
(%o5)                         false
(%i6) defmatch (checklimits, 'integrate (f, x, a, b));
(%o6)                      checklimits
(%i7) simp : true;
(%o7)                         true
(%i8) 'integrate (sin(t), t, %pi + x, 2*%pi + x);
                       x + 2 %pi
                      /
                      [
(%o8)                 I          sin(t) dt
                      ]
                      /
                       x + %pi
(%i9) checklimits (%);
(%o9)    [b = x + 2 %pi, a = x + %pi, x = t, f = sin(t)]
```

<!-- category: Calculus -->
<!-- keywords: defrule -->
<!-- signatures: defrule(nomeregra, modelo, substituição) -->
### Function: defrule (nomeregra, modelo, substituição)

Define e nomeia uma
regra de substituição para o modelo dado.  Se a regra nomeada *nomeregra* for
aplicada a uma expressão (através de `apply1`, `applyb1`, ou `apply2`), toda
subexpressão coincidindo com o modelo será substituída por
`substituição`. Todas as variáveis em `substituição` que tiverem sido
atribuidos valores pela coincidência com o modelo são atribuidas esses valores na
`substituição` que é então simplificado.


As regras por si mesmas podem ser
tratadas como funções que transforma uma expressão através de uma
operação de coincidência de modelo e substituição.
Se a coincidência falhar, a função da regra retorna `false`.

<!-- category: Calculus -->
<!-- keywords: disprule -->
<!-- signatures: disprule(nomeregra_1, ..., nomeregra_2), disprule(all) -->
### Function: disprule (nomeregra_1, ..., nomeregra_2)

Mostra regras com os nomes *nomeregra_1*, ..., *nomeregra_n*,
como retornado por `defrule`, `tellsimp`, ou `tellsimpafter`,
ou um modelo definido por meio de `defmatch`.


Cada regra é mostrada com um rótulo de expressão intermédia (`%t`).


`disprule (all)` mostra todas as regras.


`disprule` não avalia seus argumentos.


`disprule` retorna a lista de rótulos de expressões intermedáirias correspondendo às regras mostradas.


Veja também `letrules`, que mostra regras definidas através de `let`.


Examples:










```maxima
(%i1) tellsimpafter (foo (x, y), bar (x) + baz (y));
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (x + y, special_add (x, y));
(%o2)                   [+rule1, simplus]
(%i3) defmatch (quux, mumble (x));
(%o3)                         quux
(%i4) disprule (foorule1, "+rule1", quux);
(%t4)        foorule1 : foo(x, y) -> baz(y) + bar(x)

(%t5)          +rule1 : y + x -> special_add(x, y)

(%t6)                quux : mumble(x) -> []

(%o6)                    [%t4, %t5, %t6]
(%i6) ''%;
(%o6) [foorule1 : foo(x, y) -> baz(y) + bar(x),
+rule1 : y + x -> special_add(x, y), quux : mumble(x) -> []]
```

<!-- category: Calculus -->
<!-- keywords: let -->
<!-- signatures: let(prod, repl, prednome, arg_1, ..., arg_n), let([prod, repl, prednome, arg_1, ..., arg_n], nome_pacote) -->
### Function: let (prod, repl, prednome, arg_1, ..., arg_n)

Define uma regra de substituição para `letsimp` tal que *prod* é substituído por *repl*.
*prod* é um produto de expoentes positivos ou negativos dos seguintes termos:



- *
Atomos que `letsimp` irá procurar literalmente a menos que previamente
chamando `letsimp` a função `matchdeclare` é usada para associar um
predicado com o átomo.  Nesse caso `letsimp` irá coincidir com o átomo para
qualquer termo de um produto satisfazendo o predicado.
- *
Núcleos tais como `sin(x)`, `n!`, `f(x,y)`, etc.  Como com átomos acima
`letsimp` irá olhar um literal coincidente a menos que `matchdeclare` seja usada para
associar um predicado com o argumento do núcleo.


Um termo para um expoente positivo irá somente coincidir com um termo tendo ao menos aquele
expoente.  Um termo para um expoente negativo
por outro lado irá somente coincidir com um termo com um expoente ao menos já
negativo.  o caso de expentes negativos em *prod* o comutador
`letrat` deve ser escolhido para `true`.
Veja também `letrat`.


Se um predicado for incluído na função `let` seguido por uma lista de
argumentos, uma tentativa de coincidência (i.e. uma que pode ser aceita se o
predicado fosse omitido) é aceita somente se
`prednome (arg_1', ..., arg_n')` avaliar para `true` onde *arg_i’* é o valor
coincidente com *arg_i*.  O *arg_i* pode ser o nome de qualquer átomo ou o argumento
de qualquer núcleo aparecendo em *prod*.
*repl* pode ser qualquer expressão racional. 
Se quaisquer dos átomos ou argumentos de *prod* aparecer em *repl* a
substituição é feita. 


O sinalizador global `letrat` controla a simplificação dos quocientes através de `letsimp`.
Quando `letrat` for `false`,
`letsimp` simplifica o numerador e o
denominador de *expr* separadamente, e não simplifica o quociente.
Substituições tais como `n!/n` vão para `(n-1)!` então falham quando `letrat` for `false`.
Quando `letrat` for `true`, então o numerador,
o denominador, e o quociente são simplificados nessa ordem.


Essas funções de substituição
permitem-lhe trabalhar com muitos pacotes de regras.  Cada pacote de
regras pode conter qualquer número de regras `let` e é
referenciado através de um nome definido pelo utilizador.  `let ([prod, repl, prednome, arg_1, ..., arg_n], nome_pacote)` adiciona a regra *prednome* ao
pacote de regras *nome_pacote*.  `letsimp (expr, nome_pacote)` aplica as regras em *nome_pacote*.
`letsimp (expr, nome_pacote1, nome_pacote2, ...)`
é equivalente a `letsimp (expr, nome_pacote1)`
seguido por `letsimp (%, nome_pacote2)`, ....


`current_let_rule_package` é o nome do pacote de regras que está
actualmente sendo usando.
Essa variável pode receber o nome de
qualquer pacote de regras definidos via o comando `let`.
Quando qualquer das funções compreendidas no pacote `let` são chamadas sem o nome do pacote,
o pacote nomeado por `current_let_rule_package` é usado.
Se uma chamada tal como `letsimp (expr, nome_pct_regras)` é feita,
o pacote de regras *nome_pct_regras* é usado somente para aquele comando `letsimp`,
e `current_let_rule_package` não é alterada.
Se não especificado de outra forma,
`current_let_rule_package` avalia de forma padronizada para `default_let_rule_package`.



```maxima
(%i1) matchdeclare ([a, a1, a2], true)$
(%i2) oneless (x, y) := is (x = y-1)$
(%i3) let (a1*a2!, a1!, oneless, a2, a1);
(%o3)         a1 a2! --> a1! where oneless(a2, a1)
(%i4) letrat: true$
(%i5) let (a1!/a1, (a1-1)!);
                        a1!
(%o5)                   --- --> (a1 - 1)!
                        a1
(%i6) letsimp (n*m!*(n-1)!/m);
(%o6)                      (m - 1)! n!
(%i7) let (sin(a)^2, 1 - cos(a)^2);
                        2               2
(%o7)                sin (a) --> 1 - cos (a)
(%i8) letsimp (sin(x)^4);
                        4           2
(%o8)                cos (x) - 2 cos (x) + 1
```

<!-- category: Calculus -->
<!-- keywords: let_rule_packages -->
<!-- signatures: let_rule_packages -->
### Variable: let_rule_packages

Valor por omissão: `[default_let_rule_package]`


`let_rule_packages` é uma lista de todos os pacotes de regras `let` definidos pelo utilizador
mais o pacote padrão `default_let_rule_package`.

<!-- category: Calculus -->
<!-- keywords: letrat -->
<!-- signatures: letrat -->
### Variable: letrat

Valor por omissão: `false`


Quando `letrat` for `false`, `letsimp` simplifica o
numerador e o denominador de uma razão separadamente,
e não simplifica o quociente.


Quando `letrat` for `true`,
o numerador, o denominador, e seu quocienten são simplificados nessa ordem.



```maxima
(%i1) matchdeclare (n, true)$
(%i2) let (n!/n, (n-1)!);
                         n!
(%o2)                    -- --> (n - 1)!
                         n
(%i3) letrat: false$
(%i4) letsimp (a!/a);
                               a!
(%o4)                          --
                               a
(%i5) letrat: true$
(%i6) letsimp (a!/a);
(%o6)                       (a - 1)!
```

<!-- category: Calculus -->
<!-- keywords: letrules -->
<!-- signatures: letrules(), letrules(nome_pacote) -->
### Function: letrules ()

Mostra as regras em um pacote de regras.
`letrules ()` mostra as regras no pacote de regras corrente.
`letrules (nome_pacote)` mostra as regras em `nome_pacote`.


O pacote de regras corrente é nomeado por `current_let_rule_package`.
Se não especificado de outra forma, `current_let_rule_package`
avalia de forma padrão para `default_let_rule_package`.


Veja também `disprule`, que mostra regras defindas por `tellsimp` e `tellsimpafter`.

<!-- category: Calculus -->
<!-- keywords: letsimp -->
<!-- signatures: letsimp(expr), letsimp(expr, nome_pacote), letsimp(expr, nome_pacote_1, ..., nome_pacote_n) -->
### Function: letsimp (expr)

Repetidamente aplica a substituição definida por `let`
até que nenhuma mudança adicional seja feita para *expr*.


`letsimp (expr)` usa as regras de `current_let_rule_package`.


`letsimp (expr, nome_pacote)` usa as regras de *nome_pacote*
sem alterar `current_let_rule_package`.


`letsimp (expr, nome_pacote_1, ..., nome_pacote_n)`
é equivalente a `letsimp (expr, nome_pacote_1`,
seguido por `letsimp (%, nome_pacote_2)`, e assim sucessivamente.

<!-- category: Calculus -->
<!-- keywords: matchdeclare -->
<!-- signatures: matchdeclare(a_1, pred_1, ..., a_n, pred_n) -->
### Function: matchdeclare (a_1, pred_1, ..., a_n, pred_n)

Associa um predicado *pred_k* 
com uma variável ou lista de variáveis *a_k*
de forma que *a_k* coincida com expressões
para as quais o predicado retorne qualquer coisa que não `false`.


Umpredicado é o nome de uma função,
ou de uma expressão lambda,
ou uma chamada de função ou chamada de função lambda iomitindo o úlltimo argumento,
ou `true` ou `all`.
Qualquer expressão coincide com `true` ou `all`.
Se o predicado for especificado como uma chamada de função ou chamada de função lambda,
a expressão a ser testada é anexada ao final da lista de argumentos;
os argumentos são avaliados ao mesmo tempo que a coincidência é avaliada.
De outra forma, o predicado é especificado como um nome de função ou expressão lambda,
e a expressão a ser testada é o argumento sozinho.
Uma função predicado não precisa ser definida quando `matchdeclare` for chamada;
o predicado não é avaliado até que uma coincidência seja tentada.


Um predicado pode retornar uma expressão Booleana além de `true` ou `false`.
Expressões Booleanas são avaliadas por `is` dentro da função da regra construída,
de forma que não é necessário chamar `is` dentro do predicado.


Se uma expressão satisfaz uma coincidência de predicado,
a variável de coincidência é atribuída à expressão,
excepto para variáveis de coincidência que são operandos de adição `+` ou multiplicação `*`.
Somente adição e multiplicação são manuseadas de forma especial;
outros operadores enários (ambos os definidos internamente e os definidos pelo utilizador) são tratados como funções comuns.



No caso de adição e multiplicação,
a variável de coincidência pode ser atribuida a uma expressão simples que satisfaz o predicado de coincidência,
ou uma adição ou um produto (respectivamente) de tais expressões.
Tal coincidência de termo multiplo é gulosa:
predicados são avaliados na ordem em que suas variáveis associadas
aparecem no modelo de coincidência,
e o termo que satisfizer mais que um predicado é tomado pelo primeiro
predicado que satisfizer.
Cada predicado é testado contra todos os operandos de adição ou produto antes que o próximo predicado seja avaliado.
Adicionalmente,
se 0 ou 1 (respectivamente) satisfazem um predicado de coincidência,
e não existe outros termos que satisfaçam o predicado,
0 ou 1 é atribuído para a variável de coincidência associada com o predicado.


O algoritmo para processar modelos contendo adição e multiplicação faz alguns resultados de coincidência
(por exemplo, um modelo no qual uma variável "coincida com qualquer coisa" aparecer)
dependerem da ordem dos termos no modelo de coincidência e na expressão a ser testada a coincidência.
Todavia,
se todos os predicados de coincidência são mutuamente exclusivos,
o resultado de coincidência é insensível a ordenação,
como um predicado de coincidência não pode aceitar termos de coincidência de outro.


Chamado `matchdeclare` com uma variável *a* como um argumento
muda a propriedade `matchdeclare` para *a*, se a variável *a* tiver sido declarada anteriormente;
somente o `matchdeclare` mais recente está em efeito quando uma regra é definida,
mudanças posteriores para a propriedade `matchdeclare`
(via `matchdeclare` ou `remove`)
não afectam regras existentes.


`propvars (matchdeclare)` retorna a lista de todas as variáveis
para as quais exista uma propriedade `matchdeclare`.
`printprops (a, matchdeclare)` retorna o predicado para a variável `a`.
`printprops (all, matchdeclare)` retorna a lista de predicados para todas as variáveis `matchdeclare`.
`remove (a, matchdeclare)` remove a propriedade `matchdeclare` da variável *a*.


As funções
`defmatch`, `defrule`, `tellsimp`, `tellsimpafter`, e `let`
constroem regras que testam expressões contra modelos.


`matchdeclare` coloca apóstrofo em seus argumentos.
`matchdeclare` sempre retorna `done`.


Exemplos:


Um predicado é o nome de uma função,
ou uma expressão lambda,
ou uma chamada de função ou chamada a função lambda omitindo o último argumento,
or `true` or `all`.











```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) matchdeclare (bb, lambda ([x], x > 0));
(%o2)                         done
(%i3) matchdeclare (cc, freeof (%e, %pi, %i));
(%o3)                         done
(%i4) matchdeclare (dd, lambda ([x, y], gcd (x, y) = 1) (1728));
(%o4)                         done
(%i5) matchdeclare (ee, true);
(%o5)                         done
(%i6) matchdeclare (ff, all);
(%o6)                         done
```


Se uma expressão satisfaz um predicado de coincidência,
a variável de coincidência é atribuída à expressão.








```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) defrule (r1, bb^aa, ["integer" = aa, "atom" = bb]);
                    aa
(%o2)        r1 : bb   -> [integer = aa, atom = bb]
(%i3) r1 (%pi^8);
(%o3)               [integer = 8, atom = %pi]
```


No caso de adição e multiplicação,
à variável de coincidência pode ser atribuída uma expressão simples que satisfaz o predicado de coincidência,
ou um somatório ou produtório (respectivamente) de tais expressões.










```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" = bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + sin(x));
(%o3)     [all atoms = 8, all nonatoms = sin(x) + a b]
(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" = bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * sin(x));
(%o5)    [all atoms = 8, all nonatoms = (b + a) sin(x)]
```


Quando coincidindo argumentos de `+` e `*`,
se todos os predicados de coincidência forem mutuamente exclusivos,
o resultado da coincidência é insensíve à ordenação,
como um predicado de coincidência não pode aceitar termos que coincidiram com outro.










```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" = bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + %pi + sin(x) - c + 2^n);
                                                     n
(%o3) [all atoms = %pi + 8, all nonatoms = sin(x) + 2  - c + a b]
(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" = bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * %pi * sin(x) / c * 2^n);
                                                  n
                                         (b + a) 2  sin(x)
(%o5) [all atoms = 8 %pi, all nonatoms = -----------------]
                                                 c
```


As funções `propvars` e `printprops` retornam informações sobre variávels de coincidência.











```maxima
(%i1) matchdeclare ([aa, bb, cc], atom, [dd, ee], integerp);
(%o1)                         done
(%i2) matchdeclare (ff, floatnump, gg, lambda ([x], x > 100));
(%o2)                         done
(%i3) propvars (matchdeclare);
(%o3)             [aa, bb, cc, dd, ee, ff, gg]
(%i4) printprops (ee, matchdeclare);
(%o4)                    [integerp(ee)]
(%i5) printprops (gg, matchdeclare);
(%o5)              [lambda([x], x > 100, gg)]
(%i6) printprops (all, matchdeclare);
(%o6) [lambda([x], x > 100, gg), floatnump(ff), integerp(ee), 
                      integerp(dd), atom(cc), atom(bb), atom(aa)]
```

<!-- category: Calculus -->
<!-- keywords: matchfix -->
<!-- signatures: matchfix(delimitador_e, delimitador_d), matchfix(delimitador_e, delimitador_d, arg_pos, pos) -->
### Function: matchfix (delimitador_e, delimitador_d)

Declara um operador `matchfix` com delimitadores esquerdo e direito *delimitador_e* e *delimitador_d*.
Os delimitadores são especificados como sequêcias de caracteres.


Um operador "matchfix" é uma função que aceita qualquer número de argumentos,
tal que os argumentos ocorram entre os delimitadores correspondentes esquerdo e direito.
Os delimitadores podem ser quaisquer sequêcias de caracteres, contanto que o analisador de expressões do Maxima possa
distinguir os delimitadores dos operandos 
e de outras expressões e operadores.
Na prática essas regras excluem delimitadores não analisáveis tais como
`%`, `,`, `$` e `;`, 
e pode ser necessário isolar os delimitadores com espaços em branco.
O delimitador da direita pode ser o mesmo ou diferente do delimitador da esquerda.


Um delimitador esquerdo pode ser associado com somente um delimitador direito;
dois diferentes operadores `matchfix` não podem ter o mesmo delimitador esquerdo.


Um operador existente pode ser redeclarado com um operador `matchfix`
sem alterar suas outras propriedades.
Particularmente, operadores internos tais como adição `+` podem
ser declarados `matchfix`,
mas funções operadores não podem ser definidas para operadores internos.


`matchfix (delimitador_e, delimitador_d, arg_pos, pos)` 
declara o argumento *arg_pos* como sendo um entre: expressão lógica,
expressão comum do Maxima mas que não seja do tipo anterior, e qualquer outro
tipo de expressão que não esteja incluída nos dois primeiros tipos.
Essa declaração resulta em *pos* sendo um entre: expressão lógica,
expressão comum do Maxima mas que não seja do tipo anterior, e qualquer outro
tipo de expressão que não esteja incluída nos dois primeiros tipos 
e os delimitadores *delimitador_e* e *delimitador_d*.









A função para realizar uma operação `matchfix` é uma função
comum definida pelo utilizador.
A função operador é definida
da forma usual
com o operador de definição de função `:=` ou `define`.
Os argumentos podem ser escritos entre os delimitadores,
ou com o delimitador esquerdo com uma sequência de caracteres com apóstrofo e os argumentos
seguindo entre parêntesis.
`dispfun (delimitador_e)` mostra a definição da função operador.


O único operador interno `matchfix` é o construtor de listas `[ ]`.
Parêntesis `( )` e aspas duplas `" "` 
atuam como operadores `matchfix`,
mas não são tratados como tal pelo analisador do Maxima.


`matchfix` avalia seus argumentos.
`matchfix` retorna seu primeiro argumento, *delimitador_e*.



Exemplos:



- *
Delimitadores podem ser quase quaisquer sequência de caracteres.











```maxima
(%i1) matchfix ("@@", "~");
(%o1)                          @@
(%i2) @@ a, b, c ~;
(%o2)                      @@a, b, c~
(%i3) matchfix (">>", "<<");
(%o3)                          >>
(%i4) >> a, b, c <<;
(%o4)                      >>a, b, c<<
(%i5) matchfix ("foo", "oof");
(%o5)                          foo
(%i6) foo a, b, c oof;
(%o6)                     fooa, b, coof
(%i7) >> w + foo x, y oof + z << / @@ p, q ~;
                     >>z + foox, yoof + w<<
(%o7)                ----------------------
                            @@p, q~
```



- *
Operadores `matchfix` são funções comuns definidas pelo utilizador.


```maxima
(%i1) matchfix ("!-", "-!");
(%o1)                         "!-"
(%i2) !- x, y -! := x/y - y/x;
                                    x   y
(%o2)                   !-x, y-! := - - -
                                    y   x
(%i3) define (!-x, y-!, x/y - y/x);
                                    x   y
(%o3)                   !-x, y-! := - - -
                                    y   x
(%i4) define ("!-" (x, y), x/y - y/x);
                                    x   y
(%o4)                   !-x, y-! := - - -
                                    y   x
(%i5) dispfun ("!-");
                                    x   y
(%t5)                   !-x, y-! := - - -
                                    y   x

(%o5)                         done
(%i6) !-3, 5-!;
                                16
(%o6)                         - --
                                15
(%i7) "!-" (3, 5);
                                16
(%o7)                         - --
                                15
```

<!-- category: Calculus -->
<!-- keywords: remlet -->
<!-- signatures: remlet(prod, nome), remlet(), remlet(all), remlet(all, nome) -->
### Function: remlet (prod, nome)

Apaga a regra de substituiçao, prod –> repl, mais
recentemente definida através dea função `let`.  Se `nome` for fornecido a regra é
apagada do pacote de regras chamado `nome`.


`remlet()` e `remlet(all)` apagam todas as regras de substituição do pacote de regras corrente.
Se o nome de um pacote de regras for fornecido,
e.g. `remlet (all, nome)`, o pacote de regras *nome* é também apagado.


Se uma substituição é para ser mudada usando o mesmo
produto, `remlet` não precisa ser chamada, apenas redefina a substituição
usando o mesmo produto (literalmente) com a função `let` e a nova
substituição e/ou nome de predicado.  Pode agora `remlet (prod)` ser
chamada e a regra de substituição original é ressuscitada.


Veja também `remrule`, que remove uma regra definida através de `tellsimp` ou de `tellsimpafter`.

<!-- category: Calculus -->
<!-- keywords: remrule -->
<!-- signatures: remrule(op, nomeregra), remrule(op, all) -->
### Function: remrule (op, nomeregra)

Remove regras definidas por `tellsimp`, ou `tellsimpafter`.


`remrule (op, nomeregra)`
remove a regra com o nome `nomeregra` do operador *op*.
Quando *op* for um operador interno ou um operador definido pelo utilizador
(como definido por `infix`, `prefix`, etc.),
*op* e *rulename* devem ser colocados entre aspas duplas.


`remrule (op, all)` remove todas as regras para o operador *op*.


Veja também `remlet`, que remove uma regra definida através de `let`.


Examples:



















```maxima
(%i1) tellsimp (foo (aa, bb), bb - aa);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (aa + bb, special_add (aa, bb));
(%o2)                   [+rule1, simplus]
(%i3) infix ("@@");
(%o3)                          @@
(%i4) tellsimp (aa @@ bb, bb/aa);
(%o4)                   [@@rule1, false]
(%i5) tellsimpafter (quux (%pi, %e), %pi - %e);
(%o5)                  [quuxrule1, false]
(%i6) tellsimpafter (quux (%e, %pi), %pi + %e);
(%o6)             [quuxrule2, quuxrule1, false]
(%i7) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
       quux (%e, %pi)];
                                     bb
(%o7) [bb - aa, special_add(aa, bb), --, %pi - %e, %pi + %e]
                                     aa
(%i8) remrule (foo, foorule1);
(%o8)                          foo
(%i9) remrule ("+", "+rule1");
(%o9)                           +
(%i10) remrule ("@@", "@@rule1");
(%o10)                         @@
(%i11) remrule (quux, all);
(%o11)                        quux
(%i12) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
        quux (%e, %pi)];
(%o12) [foo(aa, bb), bb + aa, aa @@ bb, quux(%pi, %e), 
                                         quux(%e, %pi)]
```

<!-- category: Calculus -->
<!-- keywords: tellsimp -->
<!-- signatures: tellsimp(pattern, replacement) -->
### Function: tellsimp (pattern, replacement)

é similar a `tellsimpafter` mas coloca
nova informação antes da antiga de forma que essa nova regra seja aplicada antes das regras
de simplificação internas.


`tellsimp` é usada quando for importante modificar a expressão
antes que o simplificador trabalhe sobre ela, por exemplo se o
simplificador "sabe" alguma coisa sobre a expressão, mas o que ele
retorna não é para sua apreciação.  Se o
simplificador "sabe" alguma coisa sobre o principal operador da
expressão, mas está simplesmente a escondê-lo, provavelmente
querrá usar `tellsimpafter`.


O modelo pode não ser uma
adição, um produto, variável simples, ou número.


`rules` é a lista de regras definidas por
`defrule`, `defmatch`, `tellsimp`, e `tellsimpafter`.


Exemplos:



```maxima
(%i1) matchdeclare (x, freeof (%i));
(%o1)                         done
(%i2) %iargs: false$
(%i3) tellsimp (sin(%i*x), %i*sinh(x));
(%o3)                 [sinrule1, simp-%sin]
(%i4) trigexpand (sin (%i*y + x));
(%o4)         sin(x) cos(%i y) + %i cos(x) sinh(y)
(%i5) %iargs:true$
(%i6) errcatch(0^0);
 0
0  has been generated
(%o6)                          []
(%i7) ev (tellsimp (0^0, 1), simp: false);
(%o7)                  [^rule1, simpexpt]
(%i8) 0^0;
(%o8)                           1
(%i9) remrule ("^", %th(2)[1]);
(%o9)                           ^
(%i10) tellsimp (sin(x)^2, 1 - cos(x)^2);
(%o10)                 [^rule2, simpexpt]
(%i11) (1 + sin(x))^2;
                                      2
(%o11)                    (sin(x) + 1)
(%i12) expand (%);
                                   2
(%o12)               2 sin(x) - cos (x) + 2
(%i13) sin(x)^2;
                                  2
(%o13)                     1 - cos (x)
(%i14) kill (rules);
(%o14)                        done
(%i15) matchdeclare (a, true);
(%o15)                        done
(%i16) tellsimp (sin(a)^2, 1 - cos(a)^2);
(%o16)                 [^rule3, simpexpt]
(%i17) sin(y)^2;
                                  2
(%o17)                     1 - cos (y)
```

<!-- category: Calculus -->
<!-- keywords: tellsimpafter -->
<!-- signatures: tellsimpafter(modelo, substituição) -->
### Function: tellsimpafter (modelo, substituição)

Define a uma regra de simplificação que o simplificador do Maxima
aplica após as regras de simplificação internas.
*modelo* é uma expressão, compreendendo variáveis de modelo (declaradas através de `matchdeclare`)
e outros átomos e operações, considerados literais para o propósito de coincidência de modelos.
*substituição* é substituída para uma expressão actual que coincide com *modelo*;
variáveis de modelo em *substituição* são atribuidas a valores coincidentes na expressão actual.


*modelo* pode ser qualquer expressão não atomica
na qual o principal operador não é uma variável de modelo;
a regra de simplificação está associada com o operador principal.
Os nomes de funções (com uma excessão, descrita abaixo), listas, e arrays
podem aparecer em *modelo* como o principal operador somente como literais (não variáveis de modelo);
essas regras fornecem expressões tais como `aa(x)` e `bb[y]` como modelos,
se `aa` e `bb` forem variáveis de modelo.
Nomes de funções, listas, e arrays que são variáveis de modelo podem aparecer como operadores
outros que não o operador principal em *modelo*.


Existe uma excessão para o que foi dito acima com relação a regras e nomes de funções.
O nome de uma função subscrita em uma expressão tal como `aa[x](y)`
pode ser uma variável de modelo,
porque o operador principal não é `aa` mas ao contrário o átomo Lisp `mqapply`.
Isso é uma consequência da representação de expressões envolvendo funções subscritas.










Regras de simplificação são aplicadas após avaliação 
(se não suprimida através de colocação de apóstrofo ou do sinalizador `noeval`).
Regras estabelecidas por `tellsimpafter` são aplicadas na ordem em que forem definidas,
e após quaisquer regras internas.
Regras são aplicadas de baixo para cima, isto é,
aplicadas primeiro a subexpressões antes de ser aplicada à expressão completa.


Isso pode ser necessário para repetidamente simplificar um resultado
(por exemplo, via o operador apóstrofo-apóstrofo `''` ou o sinalizador `infeval`)
para garantir que todas as regras são aplicadas.


Variáveis de modelo são tratadas como variáveis locais em regras de simplificação.
Assim que uma regra é definida, o valor de uma variável de modelo
não afecta a regra, e não é afectado pela regra.
Uma atribuição para uma variável de modelo que resulta em uma coincidência de regra com sucesso
não afecta a atribuição corrente (ou necessita disso) da variável de modelo.
Todavia,
como com todos os átomos no Maxima,
as propriedades de variáveis de modelo (como declarado por `put` e funções relacionadas) são globais.


A regra construída por `tellsimpafter` é nomeada após o operador principal de `modelo`.
Regras para operadores internos, 
e operadores definidos pelo utilizador 
definidos por meio de `infix`, `prefix`, `postfix`, `matchfix`, e `nofix`,
possuem nomes que são sequências de caracteres do Maxima.


Regras para outras funções possuem nomes que são identificadores comuns do Maxima.




O tratamento de substantivos e formas verbais é desprezívelmente confuso. 
Se uma regra é definida para uma forma substantiva (ou verbal)
e uma regra para o verbo correspondente (ou substantivo) já existe, 
então a nova regra definida aplica-se a ambas as formas (substantiva e verbal).
Se uma regra para a correspondente forma verbal (ou substantiva) não existe,
a nova regra definida aplicar-se-á somente para a forma substantiva (ou verbal).


A regra construída através de `tellsimpafter` é uma função Lisp comum.
Se o nome da regra for `$foorule1`,
a construção `:lisp (trace $foorule1)` rastreia a função,
e `:lisp (symbol-function '$foorule1` mostra sua definição.


`tellsimpafter` não avalia seus argumentos.
`tellsimpafter` retorna a lista de regras para o operador principal de *modelo*,
incluindo a mais recente regra estabelecia.



Veja também `matchdeclare`, `defmatch`, `defrule`, `tellsimp`, `let`,
`kill`, `remrule`, e `clear_rules`.


Exemplos:


*modelo* pode ser qualquer expressão não atomica na qual o 
principal operador não é uma variável de modelo.












```maxima
(%i1) matchdeclare (aa, atom, [ll, mm], listp, xx, true)$
(%i2) tellsimpafter (sin (ll), map (sin, ll));
(%o2)                 [sinrule1, simp-%sin]
(%i3) sin ([1/6, 1/4, 1/3, 1/2, 1]*%pi);
                    1  sqrt(2)  sqrt(3)
(%o3)              [-, -------, -------, 1, 0]
                    2     2        2
(%i4) tellsimpafter (ll^mm, map ("^", ll, mm));
(%o4)                  [^rule1, simpexpt]
(%i5) [a, b, c]^[1, 2, 3];
                                2   3
(%o5)                      [a, b , c ]
(%i6) tellsimpafter (foo (aa (xx)), aa (foo (xx)));
(%o6)                   [foorule1, false]
(%i7) foo (bar (u - v));
(%o7)                    bar(foo(u - v))
```


Regras são aplicadas na ordem em que forem definidas.
Se duas regras podem coincidir com uma expressão,
a regra que foi primeiro definida é a que será aplicada.









```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) tellsimpafter (foo (aa), bar_1 (aa));
(%o2)                   [foorule1, false]
(%i3) tellsimpafter (foo (aa), bar_2 (aa));
(%o3)              [foorule2, foorule1, false]
(%i4) foo (42);
(%o4)                       bar_1(42)
```


variáveis de modelo são tratadas como variáveis locais em regras de simplificação.
(Compare a `defmatch`, que trata variáveis de modelo como variáveis globais.)










```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) bb: 12345;
(%o3)                         12345
(%i4) foo (42, %e);
(%o4)                 bar(aa = 42, bb = %e)
(%i5) bb;
(%o5)                         12345
```


Como com todos os átomos, propriedades de variáveis de modelo são globais embora valores sejam locais.
Nesse exemplo, uma propriedade de atribuição é declarada via `define_variable`.
Essa é a propriedade do átomo `bb` através de todo o Maxima.










```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) foo (42, %e);
(%o3)                 bar(aa = 42, bb = %e)
(%i4) define_variable (bb, true, boolean);
(%o4)                         true
(%i5) foo (42, %e);
Error: bb was declared mode boolean, has value: %e
 -- an error.  Quitting.  To debug this try debugmode(true);
```


Regras são nomeadas após operadores principais.
Nomes de regras para operadores internos e operadores definidos pelo utilizador são sequências de caracteres,
enquanto nomes para outras funções são identificadores comuns.


















```maxima
(%i1) tellsimpafter (foo (%pi + %e), 3*%pi);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (foo (%pi * %e), 17*%e);
(%o2)              [foorule2, foorule1, false]
(%i3) tellsimpafter (foo (%i ^ %e), -42*%i);
(%o3)         [foorule3, foorule2, foorule1, false]
(%i4) tellsimpafter (foo (9) + foo (13), quux (22));
(%o4)                   [+rule1, simplus]
(%i5) tellsimpafter (foo (9) * foo (13), blurf (22));
(%o5)                  [*rule1, simptimes]
(%i6) tellsimpafter (foo (9) ^ foo (13), mumble (22));
(%o6)                  [^rule1, simpexpt]
(%i7) rules;
(%o7) [trigrule0, trigrule1, trigrule2, trigrule3, trigrule4, 
htrigrule1, htrigrule2, htrigrule3, htrigrule4, foorule1, 
foorule2, foorule3, +rule1, *rule1, ^rule1]
(%i8) foorule_name: first (%o1);
(%o8)                       foorule1
(%i9) plusrule_name: first (%o4);
(%o9)                        +rule1
(%i10) [?mstringp (foorule_name), symbolp (foorule_name)];
(%o10)                    [false, true]
(%i11) [?mstringp (plusrule_name), symbolp (plusrule_name)];
(%o11)                    [true, true]
(%i12) remrule (foo, foorule1);
(%o12)                         foo
(%i13) remrule ("^", "^rule1");
(%o13)                          ^
```


Um exemplo trabalhado: multiplicação anticomutativa.












```maxima
(%i1) gt (i, j) := integerp(j) and i < j;
(%o1)           gt(i, j) := integerp(j) and i < j
(%i2) matchdeclare (i, integerp, j, gt(i));
(%o2)                         done
(%i3) tellsimpafter (s[i]^^2, 1);
(%o3)                 [^^rule1, simpncexpt]
(%i4) tellsimpafter (s[i] . s[j], -s[j] . s[i]);
(%o4)                   [.rule1, simpnct]
(%i5) s[1] . (s[1] + s[2]);
(%o5)                    s  . (s  + s )
                          1     2    1
(%i6) expand (%);
(%o6)                      1 - s  . s
                                2    1
(%i7) factor (expand (sum (s[i], i, 0, 9)^^5));
(%o7) 100 (s  + s  + s  + s  + s  + s  + s  + s  + s  + s )
            9    8    7    6    5    4    3    2    1    0
```

