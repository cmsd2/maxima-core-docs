## Linha de Comando

<!-- category: Other -->
<!-- keywords: ' -->
<!-- signatures: ' -->
### Function: '

O operador apóstrofo `'` evita avaliação.


Aplicado a um símbolo,
o apóstrofo evita avaliação do símbolo.


Aplicado a uma chamada de função,
o apóstrofo evita avaliação da chamada de função,
embora os argumentos da função sejam ainda avaliados (se a avaliação não for de outra forma evitada).
O resultado é a forma substantiva da chamada de função.


Aplicada a uma espressão com parêntesis,
o apóstrofo evita avaliação de todos os símbolos e chamadas de função na expressão.

E.g., `'(f(x))` significa não avalie a expressão `f(x)`.
`'f(x)` (com apóstrofo aplicado a `f` em lugar de `f(x)`)
retorna a forma substantiva de `f` aplicada a `[x]`.


O apóstrofo nao evita simplificação.


Quando o sinalizador global `noundisp` for `true`,
substantivos são mostrados com um apóstrofo.
Esse comutador é sempre `true` quando mostrando definições de funções.


Veja também operador apóstrofo-apóstrofo `''` e `nouns`.


Exemplos:


Aplicado a um símbolo,
o apóstrofo evita avaliação do símbolo.









```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) aa^2;
(%o2)                        1048576
(%i3) 'aa^2;
                                 2
(%o3)                          aa
(%i4) ''%;
(%o4)                        1048576
```


Aplicado a uma chamada de função,
o apóstrofo evita avaliação da chamada de função.
O resultado é a forma substantiva da chamada de função.










```maxima
(%i1) x0: 5;
(%o1)                           5
(%i2) x1: 7;
(%o2)                           7
(%i3) integrate (x^2, x, x0, x1);
                               218
(%o3)                          ---
                                3
(%i4) 'integrate (x^2, x, x0, x1);
                             7
                            /
                            [   2
(%o4)                       I  x  dx
                            ]
                            /
                             5
(%i5) %, nouns;
                               218
(%o5)                          ---
                                3
```


Aplicado a uma expressão com parêntesis,
o apóstrofo evita avaliação de todos os símbolos e chamadas de função na expressão.










```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) bb: 19;
(%o2)                          19
(%i3) sqrt(aa) + bb;
(%o3)                          51
(%i4) '(sqrt(aa) + bb);
(%o4)                     bb + sqrt(aa)
(%i5) ''%;
(%o5)                          51
```


O apóstrofo não evita simplificação.







```maxima
(%i1) sin (17 * %pi) + cos (17 * %pi);
(%o1)                          - 1
(%i2) '(sin (17 * %pi) + cos (17 * %pi));
(%o2)                          - 1
```

<!-- category: Other -->
<!-- keywords: '' -->
<!-- signatures: '' -->
### Function: ''

O operador apóstrofo-apóstrofo `''` (dois apóstrofost) modifica avaliação em expressões de entrada.


Aplicado a uma expressão geral *expr*, apóstrofo-apóstrofo faz com que o valor de *expr*
seja substituído por *expr* na expressão de entrada.


Aplicado ao operadro de uma expressão,
apóstrofo-apóstrofo modifica o operadro de um susbstantivo para um verbo (se esse operador não for já um verbo).


O operador apóstrofo-apóstrofo é aplicado através do passador de entrada;
o apóstrofo-apóstrofo não é armazenado como parte de uma expressão de entrada passada.
O operador apóstrofo-apóstrofo é sempre aplicado tão rapidamente quanto for passado,
e não pode receber um terceiro apóstrofo.
Dessa forma faz com que ocorra avaliação quando essa avaliação for de outra forma suprimida,
da mesma forma que em definições de função, definições de expressãoes lambda, e expressões que recebem um apóstrofo simples `'`.


Apóstrofo-apóstrofo é reconhecido por `batch` e `load`.


Veja também o operador apóstrofo `'` e `nouns`.


Exemplos:


Aplicado a uma expressão geral *expr*, apóstrofo-apóstrofo fazem com que o valor de *expr*
seja substituido por *expr* na expressão de entrada.



















```maxima
(%i1) expand ((a + b)^3);
                     3        2      2      3
(%o1)               b  + 3 a b  + 3 a  b + a
(%i2) [_, ''_];
                         3    3        2      2      3
(%o2)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i3) [%i1, ''%i1];
                         3    3        2      2      3
(%o3)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i4) [aa : cc, bb : dd, cc : 17, dd : 29];
(%o4)                   [cc, dd, 17, 29]
(%i5) foo_1 (x) := aa - bb * x;
(%o5)                 foo_1(x) := aa - bb x
(%i6) foo_1 (10);
(%o6)                      cc - 10 dd
(%i7) ''%;
(%o7)                         - 273
(%i8) ''(foo_1 (10));
(%o8)                         - 273
(%i9) foo_2 (x) := ''aa - ''bb * x;
(%o9)                 foo_2(x) := cc - dd x
(%i10) foo_2 (10);
(%o10)                        - 273
(%i11) [x0 : x1, x1 : x2, x2 : x3];
(%o11)                    [x1, x2, x3]
(%i12) x0;
(%o12)                         x1
(%i13) ''x0;
(%o13)                         x2
(%i14) '' ''x0;
(%o14)                         x3
```


Aplicado ao operador de uma expressão,
apóstrofo-apóstrofo muda o operadro de um substantivo para um verbo (se esse operadro não for já um verbo).











```maxima
(%i1) sin (1);
(%o1)                        sin(1)
(%i2) ''sin (1);
(%o2)                    0.8414709848079
(%i3) declare (foo, noun);
(%o3)                         done
(%i4) foo (x) := x - 1729;
(%o4)                 ''foo(x) := x - 1729
(%i5) foo (100);
(%o5)                       foo(100)
(%i6) ''foo (100);
(%o6)                        - 1629
```


O operador apóstrofo-apóstrofo é aplicado por meio de um passador de entrada;
operador-apóstrofo não é armazenado como parte da expressão de entrada.










```maxima
(%i1) [aa : bb, cc : dd, bb : 1234, dd : 5678];
(%o1)                 [bb, dd, 1234, 5678]
(%i2) aa + cc;
(%o2)                        dd + bb
(%i3) display (_, op (_), args (_));
                           _ = cc + aa

                         op(cc + aa) = +

                    args(cc + aa) = [cc, aa]

(%o3)                         done
(%i4) ''(aa + cc);
(%o4)                         6912
(%i5) display (_, op (_), args (_));
                           _ = dd + bb

                         op(dd + bb) = +

                    args(dd + bb) = [dd, bb]

(%o5)                         done
```


Apóstrofo apóstrofo faz com que ocorra avaliação quando a avaliação tiver sido de outra forma suprimida,
da mesma forma que em definições de função, da mesma forma que em definições de função lambda expressions, E expressões que recebem o apóstrofo simples `'`.
















```maxima
(%i1) foo_1a (x) := ''(integrate (log (x), x));
(%o1)               foo_1a(x) := x log(x) - x
(%i2) foo_1b (x) := integrate (log (x), x);
(%o2)           foo_1b(x) := integrate(log(x), x)
(%i3) dispfun (foo_1a, foo_1b);
(%t3)               foo_1a(x) := x log(x) - x

(%t4)           foo_1b(x) := integrate(log(x), x)

(%o4)                      [%t3, %t4]
(%i4) integrate (log (x), x);
(%o4)                     x log(x) - x
(%i5) foo_2a (x) := ''%;
(%o5)               foo_2a(x) := x log(x) - x
(%i6) foo_2b (x) := %;
(%o6)                    foo_2b(x) := %
(%i7) dispfun (foo_2a, foo_2b);
(%t7)               foo_2a(x) := x log(x) - x

(%t8)                    foo_2b(x) := %

(%o8)                      [%t7, %t8]
(%i8) F : lambda ([u], diff (sin (u), u));
(%o8)             lambda([u], diff(sin(u), u))
(%i9) G : lambda ([u], ''(diff (sin (u), u)));
(%o9)                  lambda([u], cos(u))
(%i10) '(sum (a[k], k, 1, 3) + sum (b[k], k, 1, 3));
(%o10)         sum(b , k, 1, 3) + sum(a , k, 1, 3)
                    k                  k
(%i11) '(''(sum (a[k], k, 1, 3)) + ''(sum (b[k], k, 1, 3)));
(%o11)             b  + a  + b  + a  + b  + a
                    3    3    2    2    1    1
```

<!-- category: Other -->
<!-- keywords: alias -->
<!-- signatures: alias(new_name_1, old_name_1, ..., new_name_n, old_name_n) -->
### Function: alias (new_name_1, old_name_1, ..., new_name_n, old_name_n)

provê um
nome alternativo para uma função (de usuário ou de sistema), variável, array, etc.
Qualquer número de argumentos pode ser usado.

<!-- category: Other -->
<!-- keywords: debugmode -->
<!-- signatures: debugmode -->
### Variable: debugmode

Valor padrão: `false`


Quando um erro do Maxima ocorre, Maxima iniciará o depurador se `debugmode` for `true`.
O usuário pode informar comandos para examinar o histórico de chamadas, marcar pontos de parada, percorrer uma linha por vez
o código do Maxima, e assim por diante.  Veja `debugging` para uma lista de opções do depurador.


Habilitando `debugmode` por meio da alteração de seu valor para `true`, não serão capturados erros do Lisp.

<!-- category: Other -->
<!-- keywords: ev -->
<!-- signatures: ev(expr, arg_1, ..., arg_n) -->
### Function: ev (expr, arg_1, ..., arg_n)

Avalia a expressão *expr* no ambiente
especificado pelos argumentos *arg_1*, ..., *arg_n*.
Os argumentos são comutadores (sinalizadores Booleanos), atribuições, equações, e funções.
`ev` retorna o resultado (outra expressão) da avaliação.


A avaliação é realizada em passos, como segue.



1. Primeiro o ambiente é preparado examinando os argumentos que podem
ser quaisquer ou todos os seguintes.



  - *
`simp` faz com que *expr* seja simplificado independentemente da posição do
comutador `simp` que inibe simplificação se `false`.
  - *
`noeval` suprime a fase de avaliação de `ev` (veja passo (4) adiante).
Isso é útil juntamente com outros comutadores e faz com que
*expr* seja simplificado novamente sem ser reavaliado.
  - *
`nouns` causa a avaliação de formas substantivas
(tipicamente funções não avaliadas tais como `'integrate` ou `'diff`)
em *expr*.
  - *
`expand` causa expansão.
  - *
`expand (m, n)` causa expansão, alterando os valores de `maxposex` e
`maxnegex` para *m* e *n* respectivamente.
  - *
`detout` faz com que qualquer matriz inversa calculada em *expr* tenha seu
determinante mantido fora da inversa ao invés de dividindo a
cada elemento.
  - *
`diff` faz com que todas as diferenciações indicadas em *expr* sejam executadas.
  - *
`derivlist (x, y, z, ...)` causa somente diferenciações referentes às
variáveis indicadas.
  - *
`float` faz com que números racionais não inteiros sejam convertidos para ponto 
flutuante.
  - *
`numer` faz com que algumas funções matemáticas (incluindo a exponenciação)
com argumentos sejam valiadas em ponto flutuante.  Isso faz com que
variávels em *expr* que tenham sido dados numervals (valores numéricos) sejam substituídas por
seus valores.  Isso também modifica o comutador `float` para ativado.
  - *
`pred` faz com que predicados (expressões que podem ser avaliados em `true` ou `false`)
sejam avaliadas.
  - *
`eval` faz com que uma avaliação posterior de *expr* ocorra.  (Veja passo (5)
adiante.)
`eval` pode ocorrer multiplas vezes.
Para cada instância de `eval`, a expressão é avaliada novamente.
  - *
`A` onde `A` é um átomo declarado seja um sinalizador de avaliação (veja `evflag`)
faz com que `A` seja associado a
`true` durante a avaliação de *expr*.
  - *
`V: expresão` (ou alternativamente `V=expressão`) faz com que `V` seja associado ao
valor de `expressão` durante a avaliação de *expr*.  Note que se `V` é uma
opção do Maxima, então `expression` é usada para seu valor durante a
avaliação de *expr*.  Se mais que um argumento para `ev` é desse tipo
então a associação termina em paralelo.  Se `V` é uma expressão não atômica
então a substituição, ao invés de uma associação, é executada.
  - *
`F` onde `F`, um nome de função, tenha sido declarado para ser uma função de avaliação (veja `evfun`)
faz com que `F`
seja aplicado a *expr*.
  - *
Qualquer outro nome de função (e.g., `sum`) causa a avaliação de ocorrências
desses nomes em *expr* mesmo que eles tenham sido verbos.
  - *
De forma adicional uma função ocorrendo em *expr* (digamos `F(x)`) pode ser definida
localmente para o propósito dessa avaliação de *expr* dando
`F(x) := expressão` como um argumento para `ev`.
  - *
Se um átomo não mensionado acima ou uma variável subscrita ou
expressão subscrita for dada como um argumento, isso é avaliado e
se o resultado for uma equação ou uma atribuição então a associação indicada
ou substituição é executada.  Se o resultado for uma lista então os
membros da lista serão tratados  como se eles fossem argumentos adicionais
dados para `ev`.  Isso permite que uma lista de equações seja dada (e.g. `[X=1, Y=A**2]`)
ou que seja dado uma lista de nomes de equações (e.g., `[%t1, %t2]` onde `%t1` e
`%t2` são equações) tais como aquelas listas retornadas por `solve`.


Os argumentos de `ev` podem ser dados em qualquer ordem com exceção de
substituições de equações que são manuseadas em sequência, da esquerda para a direita,
e funções de avaliação que são compostas, e.g., `ev (expr, ratsimp, realpart)` são
manuseadas como `realpart (ratsimp (expr))`.


Os comutadores `simp`, `numer`, `float`, e `pred` podem também ser alterados localmente em um
bloco, ou globalmente no Maxima dessa forma eles irã
permanecer em efeito até serem resetados ao término da execução do bloco.


Se *expr* for uma expressão racional canônica (CRE),
então a expressão retornada por `ev` é também uma CRE,
contanto que os comutadores `numer` e `float` não sejam ambos `true`.
2. Durante o passo (1), é feito uma lista  de variáveis não subscritas
aparecendo do lado esquerdo das equações nos argumentos ou nos
valores de alguns argumentos se o valor for uma equação.  As variáveis
(variáveis subscritas que não possuem funções array
associadas bem como variáveis não subscritas) na expressão *expr* são
substituídas por seus valores globais, exceto para esse aparecendo nessa 
lista.  Usualmente, *expr* é apenas um rótulo ou `%`
(como em `%i2` no exemplo adiante), então esse 
passo simplesmente repete a expressão nomeada pelo rótulo, de modo que `ev`
possa trabalhar sobre isso.
3. Se quaisquer substituições tiveem sido indicadas pelos argumentos, elas serão
realizadas agora.
4. A expressão resultante é então reavaliada (a menos que um dos
argumentos seja `noeval`) e simplificada conforme os argumentos.  Note que
qualquer chamada de função em *expr* será completada depois das variáveis
nela serem avalidas e que `ev(F(x))` dessa forma possa comportar-se como `F(ev(x))`.
5. Para cada instância de `eval` nos argumentos, os passos (3) e (4) são repetidos.


                     

Exemplos



```maxima
(%i1) sin(x) + cos(y) + (w+1)^2 + 'diff (sin(w), w);
                                     d                    2
(%o1)              cos(y) + sin(x) + -- (sin(w)) + (w + 1)
                                     dw
(%i2) ev (%, sin, expand, diff, x=2, y=1);
                          2
(%o2)           cos(w) + w  + 2 w + cos(1) + 1.909297426825682
```


Uma sintaxe alternativa de alto nível tem sido provida por `ev`, por meio da qual
se pode apenas digitar seus argumentos, sem o `ev()`.  Isto é, se pode
escrever simplesmente



```maxima
expr, arg_1, ..., arg_n
```


Isso não é permitido como parte de
outra expressão, e.g., em funções, blocos, etc.


Observe o processo de associação paralela no seguinte exemplo.



```maxima
(%i3) programmode: false;
(%o3)                                false
(%i4) x+y, x: a+y, y: 2;
(%o4)                              y + a + 2
(%i5) 2*x - 3*y = 3$
(%i6) -3*x + 2*y = -4$
(%i7) solve ([%o5, %o6]);
Solution

                                          1
(%t7)                               y = - -
                                          5

                                         6
(%t8)                                x = -
                                         5
(%o8)                            [[%t7, %t8]]
(%i8) %o6, %o8;
(%o8)                              - 4 = - 4
(%i9) x + 1/x > gamma (1/2);
                                   1
(%o9)                          x + - > sqrt(%pi)
                                   x
(%i10) %, numer, x=1/2;
(%o10)                      2.5 > 1.772453850905516
(%i11) %, pred;
(%o11)                               true
```

<!-- category: Other -->
<!-- keywords: evflag -->
<!-- signatures: evflag -->
### Variable: evflag

Quando um símbolo *x* tem a propriedade `evflag`,
as expressões `ev(expr, x)` e `expr, x`
(na linha de comando interativa) são equivalentes a `ev(expr, x = true)`.
Isto é, *x* está associada a `true` enquanto *expr* for avaliada.


A expressão `declare(x, evflag)`
fornece a propriedade `evflag` para a variável *x*.


Os sinalizadores que possuem a propriedade `evflag` por padrão são os seguintes:


`algebraic`,
`cauchysum`,
`demoivre`,
`dotscrules`,
`%emode`,
`%enumer`,
`exponentialize`,
`exptisolate`,
`factorflag`,
`float`,
`halfangles`,
`infeval`,
`isolate_wrt_times`,
`keepfloat`,
`letrat`,
`listarith`,
`logabs`,
`logarc`,
`logexpand`,
`lognegint`,
`lognumer`,
`m1pbranch`,
`numer_pbranch`,
`programmode`,
`radexpand`,
`ratalgdenom`,
`ratfac`,
`ratmx`,
`ratsimpexpons`,
`simp`,
`simpsum`,
`sumexpand`, e
`trigexpand`.


Exemplos:

















```maxima
(%i1) sin (1/2);
                                 1
(%o1)                        sin(-)
                                 2
(%i2) sin (1/2), float;
(%o2)                   0.479425538604203
(%i3) sin (1/2), float=true;
(%o3)                   0.479425538604203
(%i4) simp : false;
(%o4)                         false
(%i5) 1 + 1;
(%o5)                         1 + 1
(%i6) 1 + 1, simp;
(%o6)                           2
(%i7) simp : true;
(%o7)                         true
(%i8) sum (1/k^2, k, 1, inf);
                            inf
                            ====
                            \     1
(%o8)                        >    --
                            /      2
                            ====  k
                            k = 1
(%i9) sum (1/k^2, k, 1, inf), simpsum;
                                 2
                              %pi
(%o9)                         ----
                               6
(%i10) declare (aa, evflag);
(%o10)                        done
(%i11) if aa = true then SIM else NÃO;
(%o11)                         NÃO
(%i12) if aa = true then SIM else NÃO, aa;
(%o12)                         SIM
```

<!-- category: Other -->
<!-- keywords: evfun -->
<!-- signatures: evfun -->
### Variable: evfun

Quando uma função *F* tem a propriedade `evfun`,
as expressões `ev(expr, F)` e `expr, F`
(na linha de comando interativa)
são equivalentes a `F(ev(expr))`.


Se duas ou mais funções *F*, *G*, etc., que possuem a propriedade `evfun` forem especificadas,
as funções serão aplicadas na ordem em que forem especificadas.


A expressão `declare(F, evfun)`
fornece a propriedade `evfun` para a função *F*.


As funções que possuem a propriedade `evfun` por padrão são as seguintes:


`bfloat`,
`factor`,
`fullratsimp`,
`logcontract`,
`polarform`,
`radcan`,
`ratexpand`,
`ratsimp`,
`rectform`,
`rootscontract`,
`trigexpand`, e
`trigreduce`.


Exemplos:

 


















```maxima
(%i1) x^3 - 1;
                              3
(%o1)                        x  - 1
(%i2) x^3 - 1, factor;
                                2
(%o2)                 (x - 1) (x  + x + 1)
(%i3) factor (x^3 - 1);
                                2
(%o3)                 (x - 1) (x  + x + 1)
(%i4) cos(4 * x) / sin(x)^4;
                            cos(4 x)
(%o4)                       --------
                               4
                            sin (x)
(%i5) cos(4 * x) / sin(x)^4, trigexpand;
                 4           2       2         4
              sin (x) - 6 cos (x) sin (x) + cos (x)
(%o5)         -------------------------------------
                                4
                             sin (x)
(%i6) cos(4 * x) / sin(x)^4, trigexpand, ratexpand;
                           2         4
                      6 cos (x)   cos (x)
(%o6)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i7) ratexpand (trigexpand (cos(4 * x) / sin(x)^4));
                           2         4
                      6 cos (x)   cos (x)
(%o7)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i8) declare ([F, G], evfun);
(%o8)                         done
(%i9) (aa : bb, bb : cc, cc : dd);
(%o9)                          dd
(%i10) aa;
(%o10)                         bb
(%i11) aa, F;
(%o11)                        F(cc)
(%i12) F (aa);
(%o12)                        F(bb)
(%i13) F (ev (aa));
(%o13)                        F(cc)
(%i14) aa, F, G;
(%o14)                      G(F(cc))
(%i15) G (F (ev (aa)));
(%o15)                      G(F(cc))
```

<!-- category: Other -->
<!-- keywords: infeval -->
<!-- signatures: infeval -->
### Variable: infeval

Habilita o modo "avaliação infinita".  `ev` repetidamente avalia
uma expressão até que ela permaneça invariante.  Para prevenir uma
variável, digamos `X`, seja demoradamente avaliada nesso modo, simplesmente
inclua `X='X` como um argumento para `ev`.  Certamente expressões tais como
`ev (X, X=X+1, infeval)` irão gerar um ciclo infinito.

<!-- category: Other -->
<!-- keywords: kill -->
<!-- signatures: kill(a_1, ..., a_n), kill(labels), kill(inlabels, outlabels, linelabels), kill(n), kill([m, n]), kill(values, functions, arrays, ...), kill(all), kill(allbut(a_1, ..., a_n)) -->
### Function: kill (a_1, ..., a_n)

Remove todas as associações (valor, funções, array, ou regra) dos argumentos
*a_1*, ..., *a_n*.
Um argumento *a_k* pode ser um símbolo ou um elemento de array simples.
Quando *a_k* for um elemento de array simples, `kill` remove a associação daquele elemento
sem afetar qualquer outro elemento do array.


Muitos argumentos especiais são reconhecidos.  
Diferentes famílias de argumentos 
podem ser combinadas, e.g., `kill (inlabels, functions, allbut (foo, bar))`


todos os rótulos de entrada, de saída, e de expressões intermediárias criados até então.
`kill (inlabels)` libera somente rótudos de entrada 
que começam com o valor corrente de `inchar`.
De forma semelhante,
`kill (outlabels)` libera somente rótulos de saída
que começam com o valor corrente de `outchar`,
e `kill (linelabels)` libera somente rótulos de expressões intermediárias
que começam com o valor corrente de `linechar`.


`kill (n)`, onde *n* é um inteiro,
libera os *n* mais recentes rótulos de entrada e saída.


`kill ([m, n])` libera rótulos de entrada e saída de *m* até *n*.


`kill (infolist)`, onde *infolist* é um item em `infolists`
(tais como `values`, `functions`, ou `arrays`)
libera todos os ítens em *infolist*.
Veja também `infolists`.


`kill (all)` liberar todos os ítens em todas as infolists.
`kill (all)` não retorna variáveis globais para seus valores padrões;
Veja `reset` sobre esse ponto.


`kill (allbut (a_1, ..., a_n))`
remove a associação de todos os itens sobre todas as infolistas exceto para *a_1*, ..., *a_n*.
`kill (allbut (infolist))` libera todos os ítens exceto para si próprio em *infolist*,
onde *infolist* é `values`, `functions`, `arrays`, etc.


A memória usada por uma propriedade de associação não será liberada até que todos os símbolos
sejam liberados disso.
Em particular, para liberar a memória usada pelo valor de um símbolo,
deve-se liberar o rótulo de saída que mosta o valor associado, bem como liberando o próprio símbolo.


`kill` coloca um apóstro em seus argumentos (não os avalia).
O operador apóstrofo-apóstrofo, `''`, faz com que ocorra avaliação.


`kill (símbolo)` libera todas as propriedades de *símbolo*.
Em oposição, `remvalue`, `remfunction`, `remarray`, e `remrule`
liberam uma propriedade específica.


`kill` sempre retorna `done`, igualmente se um argumento não tem associações.

<!-- category: Other -->
<!-- keywords: labels -->
<!-- signatures: labels(símbolo) -->
### Function: labels (símbolo)

Retorna a lista de rótulos de entradas, de saída, de expressões intermediárias que começam com *símbolo*.
Tipicamente *símbolo* é o valor de `inchar`, `outchar`, ou `linechar`.
O caracter rótulo pode ser dado com ou sem o sinal de porcentagem,
então, por exemplo, `i` e `%i` retornam o mesmo resultado.


Se nenhum rótulo começa com *símbolo*, `labels` retorna uma lista vazia.


A função `labels` não avalia seu argumento.
O operador apóstrofo-apóstrofo `''` faz com que ocorra avaliação.
Por exemplo,
`labels (''inchar)` retorna os rótulos de entrada que começam com o caractere corrente do rótulo de entrada.


A variável `labels` é uma lista de rótulos de entrada, saída, e de expressões intermediárias,
incluindo todos os rótulos anteriores se `inchar`, `outchar`, ou `linechar` que tiverem sido redefinidos.


Por padrão, Maxima mostra o resultado de cada expressão de entrada do usuário,
dando ao resultado um rótulo de saída.
A exibição da saída é suprimida pelo encerramento da entrada com `$` (sinal de dolar)
em lugar de `;` (ponto e vírgula).
Um rótulo de saída é construido e associado ao resultado, mas não é mostrado, 
e o rótulo pode ser referenciado da mesma forma que rótulos de saída mostrados.
Veja também `%`, `%%`, e `%th`.


Rótulos de expressões intermediárias podem ser gerados por algumas funções.
O sinalizador `programmode` controla se `solve` e algumas outras funções
geram rótulos de expressões intermediárias em lugar de retornar uma lista de expressões.
Algumas outras funções, tais como `ldisplay`, sempre geram rótulos de expressões intermediárias.


Veja também `inchar`, `outchar`, `linechar`, e `infolists`.

<!-- category: Other -->
<!-- keywords: linenum -->
<!-- signatures: linenum -->
### Variable: linenum

Retorna o número da linha do par corrente de expressões de entrada e saída.

<!-- category: Other -->
<!-- keywords: myoptions -->
<!-- signatures: myoptions -->
### Variable: myoptions

Valor padrão: `[]`


`myoptions` é a lista de todas as opções alguma vez alteradas pelo usuário,
tenha ou não ele retornado a alteração para o seu valor padrão.

<!-- category: Other -->
<!-- keywords: nolabels -->
<!-- signatures: nolabels -->
### Variable: nolabels

Valor padrão: `false`








Quando `nolabels` for `true`,
rótulos de entrada e saída
(`%i` e `%o`, respectivamente)
são mostrados,
mas os rótulos não são associados aos resultados,
e os rótulos não são anexados ao final da lista `labels`.
Uma vez que rótulos não são associados aos resultados,
a reciclagem pode recuperar a memória tomada pelos resultados.


De outra forma rótulos de entrada e saída são associados aos resultados,
e os rótulos são anexados ao final da lista `labels`.


Veja também `batch`, `batchload`, e `labels`.

<!-- category: Other -->
<!-- keywords: optionset -->
<!-- signatures: optionset -->
### Variable: optionset

Valor padrão: `false`


Quando `optionset` for `true`, Maxima mostrará uma
mensagem sempre que uma opção do Maxima for alterada.  Isso é útil se o
usuário está incerto sobre a ortografia de alguma opção e quer ter certeza
que a variável por ele atribuído um valor foi realmente uma variável de opção.

<!-- category: Other -->
<!-- keywords: playback -->
<!-- signatures: playback(), playback(n), playback([m, n]), playback([m]), playback(input), playback(slow), playback(time), playback(grind) -->
### Function: playback ()

Mostra expressões de entrada, de saída, e expressões intermediárias,
sem refazer os cálculos.
`playback` somente mostra as expressões associadas a rótulos;
qualquer outra saída (tais como textos impressos por `print` ou `describe`, ou messagens de erro)
não é mostrada.
Veja também `labels`.


`playback` não avalia seus argumentos.
O operador apóstrofo-apóstrofo, `''`, sobrepõe-se às aspas.
`playback` sempre retorna `done`.


`playback ()` (sem argumentos) mostra todas as entradas, saídas e expressões intermediárias
geradas até então.
Uma expressão de saída é mostrada mesmo se for suprimida pelo terminador `$`
quando ela tiver sido originalmente calculada.


`playback (n)` mostra as mais recentes *n* expressões.
Cada entrada, saída e expressão intermediária
conta como um.


`playback ([m, n])` mostra entradas, saídas e expressões intermediárias
com os números de *m* até *n*, inclusive.


`playback ([m])` é equivalente a `playback ([m, m])`;
isso usualmente imprime um par de expressões de entrada e saída.


`playback (input)` mostra todas as expressões de entrada geradas até então.


`playback (slow)` insere pausas entre expressões
e espera que o usuário pressione `enter`.
Esse comportamento é similar a `demo`.

`playback (slow)` é útil juntamente com `save` ou `stringout`
quando criamos um arquivo secundário de armazenagem com a finalidade de capturar expressões úteis.


`playback (time)` mostra o tempo de computação de cada expressão.




`playback (grind)` mostra expressões de entrada
no mesmo formato da função `grind`.
Expressões de saída não são afetadas pela opção `grind`.
Veja `grind`.


Argumentos podem ser combinados, e.g., 
`playback ([5, 10], grind, time, slow)`.

<!-- category: Other -->
<!-- keywords: printprops -->
<!-- signatures: printprops(a, i), printprops([a_1, ..., a_n], i), printprops(all, i) -->
### Function: printprops (a, i)

Mostra a propriedade como o indicador *i*
associada com o átomo *a*.  *a* pode também ser uma lista de átomos ou o átomo
`all` nesse caso todos os átomos com a propriedade dada serão
usados.  Por exemplo, `printprops ([f, g], atvalue)`.  `printprops` é para
propriedades que não podem  ser mostradas de outra forma, i.e. para
`atvalue`, `atomgrad`, `gradef`, e `matchdeclare`.

<!-- category: Other -->
<!-- keywords: prompt -->
<!-- signatures: prompt -->
### Variable: prompt

Valor padrão: `_`


`prompt` é o símbolo de linha de comando da função `demo`,
modo `playback (slow)`, e da interrupção de ciclos do Maxima (como invocado por `break`).

<!-- category: Other -->
<!-- keywords: quit -->
<!-- signatures: quit() -->
### Function: quit ()

Encerra a sessão do Maxima.
Note que a função pode ser invocada como `quit();` ou `quit()$`,
não por sí mesma `quit`.


Para parar um cálculo muito longo,
digite `control-C`.
A ação padrão é retornar à linha de comando do Maxima.
Se `*debugger-hook*` é `nil`,
`control-C` abre o depurador Lisp.
Veja também `debugging`.

<!-- category: Other -->
<!-- keywords: remfunction -->
<!-- signatures: remfunction(f_1, ..., f_n), remfunction(all) -->
### Function: remfunction (f_1, ..., f_n)

Desassocia as definições de função dos síbolos *f_1*, ..., *f_n*.
Os argumentos podem ser os nomes de funções comuns (criadas por meio de `:=` ou `define`)
ou funções macro (criadas por meio de `::=`).


`remfunction (all)` desassocia todas as definições de funcção.


`remfunction` coloca um ap’ostrofo em seus argumentos (não os avalia).


`remfunction` retorna uma lista de símbolos para a qual a definição de função foi desassociada.
`false` é retornado em lugar de qualquer símbolo para o qual não exista definição de função.

<!-- category: Other -->
<!-- keywords: reset -->
<!-- signatures: reset() -->
### Function: reset ()

Retorna muitas variáveis globais e opções, e algumas outras variáveis, para seus valores padrões.


`reset` processa as variáveis na lista Lisp `*variable-initial-values*`.
A macro Lisp `defmvar` coloca variáveis nessa lista (entre outras ações).
Muitas, mas não todas, variáveis globais e opções são definidas por `defmvar`,
 e algumas variáveis definidas por `defmvar` não são variáveis globais ou variáveis de opção.

<!-- category: Other -->
<!-- keywords: showtime -->
<!-- signatures: showtime -->
### Variable: showtime

Valor padrão: `false`


Quando `showtime` for `true`, o tempo de computação e o tempo decorrido são
impressos na tela com cada expressão de saída.


O tempo de cálculo é sempre gravado,
então `time` e `playback` podem mostrar o tempo de cálculo
mesmo quando `showtime` for `false`.


Veja também `timer`.

<!-- category: Other -->
<!-- keywords: sstatus -->
<!-- signatures: sstatus(recurso, pacote) -->
### Function: sstatus (recurso, pacote)

Altera o status de *recurso* em *pacote*.
Após `sstatus (recurso, pacote)` ser executado,
`status (recurso, pacote)` retorna `true`.
Isso pode ser útil para quem escreve pacotes, para
manter um registro de quais recursos os pacotes usam.

<!-- category: Other -->
<!-- keywords: to_lisp -->
<!-- signatures: to_lisp() -->
### Function: to_lisp ()

Insere o sistema Lisp dentro do Maxima.  `(to-maxima)` retorna para o Maxima.

<!-- category: Other -->
<!-- keywords: values -->
<!-- signatures: values -->
### Variable: values

Valor inicial: `[]`


`values` é uma lista de todas as varáveis de usuário associadas (não opções Maxima ou comutadores).
A lista compreende símbolos associados por `:` , `::`, ou `:=`.

