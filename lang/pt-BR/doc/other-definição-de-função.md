## Definição de Função

<!-- category: Other -->
<!-- keywords: apply -->
<!-- signatures: apply(F, [x_1, ..., x_n]) -->
### Function: apply (F, [x_1, ..., x_n])

Constrói e avalia uma expressãp `F(arg_1, ..., arg_n)`.


`apply` não tenta distinguir funções de array de funções comuns;
quando *F* for o nome de uma função de array,
`apply` avalia `F(...)`
(isto é, uma chamada de função com parêntesis em lugar de colchêtes).
`arrayapply` avalia uma chamada de função com colchêtes nesse caso.


Exemplos:


`apply` avalia seus argumentos.
Nesse exemplo, `min` é aplicado a `L`.







```maxima
(%i1) L : [1, 5, -10.2, 4, 3];
(%o1)                 [1, 5, - 10.2, 4, 3]
(%i2) apply (min, L);
(%o2)                        - 10.2
```


`apply` avalia argumentos, mesmo se a função *F* disser que os argumentos não devem ser avaliados.










```maxima
(%i1) F (x) := x / 1729;
                                   x
(%o1)                     F(x) := ----
                                  1729
(%i2) fname : F;
(%o2)                           F
(%i3) dispfun (F);
                                   x
(%t3)                     F(x) := ----
                                  1729

(%o3)                         [%t3]
(%i4) dispfun (fname);
fname is not the name of a user function.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) apply (dispfun, [fname]);
                                   x
(%t5)                     F(x) := ----
                                  1729

(%o5)                         [%t5]
```


`apply` avalia o nome de função *F*.
Apóstrofo `'` evita avaliação.
`demoivre` é o nome de uma variável global e também de uma função.









```maxima
(%i1) demoivre;
(%o1)                         false
(%i2) demoivre (exp (%i * x));
(%o2)                  %i sin(x) + cos(x)
(%i3) apply (demoivre, [exp (%i * x)]);
demoivre evaluates to false
Improper name or value in functional position.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) apply ('demoivre, [exp (%i * x)]);
(%o4)                  %i sin(x) + cos(x)
```

<!-- category: Other -->
<!-- keywords: block -->
<!-- signatures: block([v_1, ..., v_m], expr_1, ..., expr_n), block(expr_1, ..., expr_n) -->
### Function: block ([v_1, ..., v_m], expr_1, ..., expr_n)

`block` avalia *expr_1*, ..., *expr_n* em sequência
e retorna o valor da última expressão avaliada.
A sequência pode ser modificada pelas funções `go`, `throw`, e `return`.
A última expressão é *expr_n* a menos que `return` ou uma expressão contendo `throw`
seja avaliada.
Algumas variáveis *v_1*, ..., *v_m* podem ser declaradas locais para o bloco;
essas são distinguidas das variáveis globais dos mesmos nomes.
Se variáveis não forem declaradas locais então a lista pode ser omitida.
Dentro do bloco,
qualquer variável que não *v_1*, ..., *v_m* é uma variável global.


`block` salva os valores correntes das variáveis *v_1*, ..., *v_m* (quaisquer valores)
na hora da entrada para o bloco,
então libera as variáveis dessa forma eles avaliam para si mesmos.
As variáveis locais podem ser associadas a valores arbitrários dentro do bloco mas quando o
bloco é encerrado o valores salvos são restaurados,
e os valores atribuídos dentro do bloco são perdidos.


`block` pode aparecer dentro de outro `block`.
Variáveis locais são estabelecidas cada vez que um novo `block` é avaliado.
Variáveis locais parecem ser globais para quaisquer blocos fechados.
Se uma variável é não local em um bloco,
seu valor é o valor mais recentemente atribuído por um bloco fechado, quaisquer que sejam,
de outra forma, seu valor é o valor da variável no ambiente global.
Essa política pode coincidir com o entendimento usual de "escopo dinâmico".


Se isso for desejado para salvar e restaurar outras propriedades locais
ao lado de `value`, por exemplo `array` (exceto para arrays completos),
`function`, `dependencies`, `atvalue`, `matchdeclare`, `atomgrad`, `constant`, e
`nonscalar` então a função `local` pode ser usada dentro do bloco
com argumentos sendo o nome das variáveis.


O valor do bloco é o valor da última declaração ou o
valor do argumento para a função `return` que pode ser usada para sair
explicitamente do bloco.  A função `go` pode ser usada para transferir o
controle para a declaração do bloco que é identificada com o argumento
para `go`.  Para identificar uma declaração, coloca-se antes dela um argumento atômico como
outra declaração no bloco.  Por exemplo:
`block ([x], x:1, loop, x: x+1, ..., go(loop), ...)`.  O argumento para `go` deve
ser o nome de um identificador que aparece dentro do bloco.  Não se deve usar `go` para
transferir para um identificador em um outro bloco a não ser esse que contém o `go`.


Blocos tipicamente aparecem do lado direito de uma definição de função
mas podem ser usados em outros lugares também.

<!-- category: Other -->
<!-- keywords: break -->
<!-- signatures: break(expr_1, ..., expr_n) -->
### Function: break (expr_1, ..., expr_n)

Avalia e imprime *expr_1*, ..., *expr_n* e então
causa uma parada do Maxima nesse ponto e o usuário pode examinar e alterar
seu ambiente.  Nessa situação digite `exit;` para que o cálculo seja retomado.

<!-- category: Other -->
<!-- keywords: catch -->
<!-- signatures: catch(expr_1, ..., expr_n) -->
### Function: catch (expr_1, ..., expr_n)

Avalia *expr_1*, ..., *expr_n* uma por uma; se qualquer avaliação
levar a uma avaliação de uma expressão da
forma `throw (arg)`, então o valor de `catch` é o valor de
`throw (arg)`, e expressões adicionais não são avaliadas.
Esse "retorno não local" atravessa assim qualquer profundidade de
aninhar para o mais próximo contendo `catch`.
Se não existe nenhum `catch` contendo um `throw`, uma mensagem de erro é impressa.


Se a avaliação de argumentos não leva para a avaliação de qualquer `throw`
então o valor de `catch` é o valor de *expr_n*.



```maxima
(%i1) lambda ([x], if x < 0 then throw(x) else f(x))$
(%i2) g(l) := catch (map (''%, l))$
(%i3) g ([1, 2, 3, 7]);
(%o3)               [f(1), f(2), f(3), f(7)]
(%i4) g ([1, 2, -3, 7]);
(%o4)                          - 3
```



A função `g` retorna uma lista de `f` de cada elemento de `l` se `l`
consiste somente de números não negativos; de outra forma, `g` "captura" o
primeiro elemento negativo de `l` e "arremessa-o".

<!-- category: Other -->
<!-- keywords: compfile -->
<!-- signatures: compfile(nomearquivo, f_1, ..., f_n), compfile(nomearquivo, funções), compfile(nomearquivo, all) -->
### Function: compfile (nomearquivo, f_1, ..., f_n)

Traduz fuções Maxima para Lisp 
e escreve o código traduzido no arquivo *nomearquivo*.


`compfile(nomearquivo, f_1, ..., f_n)` traduz as
funções especificadas.
`compfile(nomearquivo, functions)` e `compfile(nomearquivo, all)`
traduz todas as funções definidas pelo usuário.


As traduções Lisp não são avaliadas, nem é o arquivo de saída processado pelo compilador Lisp.

`translate` cria e avalia traduções Lisp.
`compile_file` traduz Maxima para Lisp, e então executa o compilador Lisp.  


Veja também `translate`, `translate_file`, e `compile_file`.

<!-- category: Other -->
<!-- keywords: compile -->
<!-- signatures: compile(f_1, ..., f_n), compile(funções), compile(all) -->
### Function: compile (f_1, ..., f_n)

Traduz funções Maxima *f_1*, ..., *f_n* para Lisp, avalia a tradução Lisp,
e chama a função Lisp `COMPILE` sobre cada função traduzida.
`compile` retorna uma lista de nomes de funções compiladas.


`compile (all)` ou `compile (funções)` compila todas as funções definidas pelo usuário.


`compile` não avalia seus argumentos; 
o operador apóstrofo-apóstrofo `''` faz com que ocorra avaliação sobrepondo-se ao apóstrofo.

<!-- category: Other -->
<!-- keywords: compile_file -->
<!-- signatures: compile_file(nomearquivo), compile_file(nomearquivo, nomearquivo_compilado), compile_file(nomearquivo, nomearquivo_compilado, lisp_nomearquivo) -->
### Function: compile_file (nomearquivo)

Traduz o arquivo Maxima *nomearquivo* para Lisp,
executa o compilador Lisp,
e, se a tradução e a compilação obtiverem sucesso, chama o código compilado dentro do Maxima.


`compile_file` retorna uma lista dos nomes de quatro arquivos:
o arquivo original do Maxima, o nome da tradução Lisp, uma arquivo de notas sobre a tradução, e o nome do arquivo que contém o código compilado.
Se a compilação falhar,
o quarto item é `false`.


Algumas declarações e definições passam a ter efeito tão logo
o código Lisp seja compilado (sem que seja necessário chamar o código compilado).
Isso inclui funções definidas com o operador `:=`,
macros definidas com o operador `::=`, 
`alias`, `declare`,
`define_variable`,  `mode_declare`,
e 
`infix`, `matchfix`,
`nofix`, `postfix`, `prefix`,
e `compfile`.


Atribuições e chamadas de função não serão avaliadas até que o código compilado seja carregado.
Em particular, dentro do arquivo Maxima,
atribuições para sinalizadores traduzidos (`tr_numer`, etc.) não têm efeito sobre a tradução.







*nomearquivo* pode não conter declarações `:lisp`.


`compile_file` avalia seus argumentos.

<!-- category: Other -->
<!-- keywords: declare_translated -->
<!-- signatures: declare_translated(f_1, f_2, ...) -->
### Function: declare_translated (f_1, f_2, ...)

Quando traduzindo um arquivo do código Maxima
para Lisp, é importante para o programa tradutor saber quais funções
no arquivo são para serem chamadas como funções traduzidas ou compiladas,
e quais outras são apenas funções Maxima ou indefinidas.  Colocando essa
declaração no topo do arquivo, faremos conhecido que embora um símbolo
diga que não temos ainda um valor de função Lisp, teremos uma em
tempo de chamada.  `(MFUNCTION-CALL fn arg1 arg2 ...)` é gerado quando
o tradutor n~ao sabe que `fn` está sendo compilada para ser uma função Lisp.

<!-- category: Other -->
<!-- keywords: define -->
<!-- signatures: define(f(x_1, ..., x_n), expr), define(f[x_1, ..., x_n], expr), define(funmake(f, [x_1, ..., x_n]), expr), define(arraymake(f, [x_1, ..., x_n]), expr), define(ev(expr_1), expr_2) -->
### Function: define (f(x_1, ..., x_n), expr)

Define uma função chamada *f* com argumentos *x_1*, ..., *x_n* e corpo da função *expr*.
`define` sempre avalia seu segundo argumento (a menos que explícitamente receba um apostrofo de forma a evitar a avaliação).
A função então definida pode ser uma função comum do Maxima (com argumentos contidos entre parêtesis)
ou uma função de array (com argumentos contidos entre colchêtes).


Quando o último ou único argumento da função *x_n* for uma lista de um elemento,
a função definida por `define` aceita um número variável de argumentos.
Os argumentos atuais são atribuídos um a um a argumentos formais *x_1*, ..., *x_(n - 1)*,
e quaisquer argumentos adicionais atuais, se estiverem presentes, são atribuídos a *x_n* como uma lista.


Quando o primeiro argumento de `define` for uma expressão da forma
`f(x_1, ..., x_n)` or `f[x_1, ..., x_n]`,
os argumentos são avaliados mas *f* não é avaliada,
mesmo se já existe anteriormente uma função ou variável com aquele nome.


Quando o primeiro argumento for uma expressão com operador `funmake`, `arraymake`, ou `ev`,
o primeiro argumento será avaliado;
isso permite para o nome da função seja calculado, também como o corpo.


Todas as definições de função aparecem no mesmo nível de escopo e visibilidade;
definindo uma função `f` dentro de outra função `g`
não limita o escopo de `f` a `g`.


Se algum argumento formal *x_k* for um símbolo com apóstrofo (após ter sido feita uma avaliação),
a função definida por `define` não avalia o correspondente atual argumento.
de outra forma todos os argumentos atuais são avaliados.


Veja também `:=` and `::=`.


Exemplos:


`define` sempre avalia seu segundo argumento (a menos que explícitamente receba um apostrofo de forma a evitar a avaliação).










```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) define (F1 (x, y), expr);
(%o2)              F1(x, y) := cos(y) - sin(x)
(%i3) F1 (a, b);
(%o3)                    cos(b) - sin(a)
(%i4) F2 (x, y) := expr;
(%o4)                   F2(x, y) := expr
(%i5) F2 (a, b);
(%o5)                    cos(y) - sin(x)
```


A função definida por `define` pode ser uma função comum do Maxima ou uma função de array.







```maxima
(%i1) define (G1 (x, y), x.y - y.x);
(%o1)               G1(x, y) := x . y - y . x
(%i2) define (G2 [x, y], x.y - y.x);
(%o2)                G2     := x . y - y . x
                       x, y
```


Quando o último ou único argumento da função *x_n* for uma lista de um único elemento,
a função definida por `define` aceita um número variável de argumentos.







```maxima
(%i1) define (H ([L]), '(apply ("+", L)));
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


When the first argument is an expression with operator `funmake`, `arraymake`, or `ev`,
the first argument is evaluated.











```maxima
(%i1) [F : I, u : x];
(%o1)                        [I, x]
(%i2) funmake (F, [u]);
(%o2)                         I(x)
(%i3) define (funmake (F, [u]), cos(u) + 1);
(%o3)                  I(x) := cos(x) + 1
(%i4) define (arraymake (F, [u]), cos(u) + 1);
(%o4)                   I  := cos(x) + 1
                         x
(%i5) define (foo (x, y), bar (y, x));
(%o5)                foo(x, y) := bar(y, x)
(%i6) define (ev (foo (x, y)), sin(x) - cos(y));
(%o6)             bar(y, x) := sin(x) - cos(y)
```

<!-- category: Other -->
<!-- keywords: define_variable -->
<!-- signatures: define_variable(name, default_value, mode) -->
### Function: define_variable (name, default_value, mode)

Introduz uma variável global dentro do ambiente Maxima.

`define_variable` é útil em pacotes escritos pelo usuário, que são muitas vezes traduzidos ou compilados.


`define_variable` realiza os seguintes passos:



1. `mode_declare (name, mode)` declara o modo de *name* para o tradutor.
Veja `mode_declare` para uma lista dos modos possíveis.
2. Se a variável é não associada, *default_value* é atribuído para *name*.
3. `declare (name, special)` declara essa variável especial.
4. Associa *name* com uma função de teste
para garantir que a *name* seja somente atribuído valores do modo declarado.















A propriedade `value_check` pode ser atribuída a qualquer variável que tenha sido definida
via `define_variable` com um outro modo que não `any`.
A propriedade `value_check` é uma expressão lambda ou o nome de uma função de uma variável,
que é chamada quando uma tentativa é feita para atribuir um valor a uma variável.
O argumento da  função `value_check` é o valor que será atribuído.


`define_variable` avalia `default_value`, e não avalia `name` e `mode`.
`define_variable` retorna o valor corrente de `name`,
que é `default_value` se `name` não tiver sido associada antes,
e de outra forma isso é o valor prévio de `name`.


Exemplos:


`foo` é uma variável Booleana, com o valor inicial `true`.









```maxima
(%i1) define_variable (foo, true, boolean);
(%o1)                         true
(%i2) foo;
(%o2)                         true
(%i3) foo: false;
(%o3)                         false
(%i4) foo: %pi;
Error: foo was declared mode boolean, has value: %pi
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) foo;
(%o5)                         false
```


`bar` é uma variável inteira, que deve ser um número primo.










```maxima
(%i1) define_variable (bar, 2, integer);
(%o1)                           2
(%i2) qput (bar, prime_test, value_check);
(%o2)                      prime_test
(%i3) prime_test (y) := if not primep(y) then error (y, "is not prime.");
(%o3) prime_test(y) := if not primep(y)

                                   then error(y, "is not prime.")
(%i4) bar: 1439;
(%o4)                         1439
(%i5) bar: 1440;
1440 é not prime.
#0: prime_test(y=1440)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) bar;
(%o6)                         1439
```


`baz_quux` é uma variável que não pode receber a atribuição de um valor.
O modo `any_check` é como `any`, 
mas `any_check` habilita o mecanismo `value_check`, e `any` não habilita.










```maxima
(%i1) define_variable (baz_quux, 'baz_quux, any_check);
(%o1)                       baz_quux
(%i2) F: lambda ([y], if y # 'baz_quux then error ("Cannot assign to `baz_quux'."));
(%o2) lambda([y], if y # 'baz_quux

                        then error(Cannot assign to `baz_quux'.))
(%i3) qput (baz_quux, ''F, value_check);
(%o3) lambda([y], if y # 'baz_quux

                        then error(Cannot assign to `baz_quux'.))
(%i4) baz_quux: 'baz_quux;
(%o4)                       baz_quux
(%i5) baz_quux: sqrt(2);
Cannot assign to `baz_quux'.
#0: lambda([y],if y # 'baz_quux then error("Cannot assign to `baz_quux'."))(y=sqrt(2))
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) baz_quux;
(%o6)                       baz_quux
```

<!-- category: Other -->
<!-- keywords: dispfun -->
<!-- signatures: dispfun(f_1, ..., f_n), dispfun(all) -->
### Function: dispfun (f_1, ..., f_n)

Mostra a definição de funções definidas pelo usuário *f_1*, ..., *f_n*.
Cada argumento pode ser o nome de uma macro (definida com `::=`),
uma função comum (definida com `:=` ou `define`),
uma função array (definida com `:=` ou com `define`,
mas contendo argumentos entre colchêtes `[ ]`),
uma função subscrita, (definida com `:=` ou `define`,
mas contendo alguns argumentos entre colchêtes e outros entre parêntesis `( )`)
uma da família de funções subscritas selecionadas por um valor subscrito particular,
ou uma função subscrita definida com uma constante subscrita.


`dispfun (all)` mostra todas as funções definidas pelo usuário como
dadas pelas `functions`, `arrays`, e listas de `macros`,
omitindo funções subscritas definidas com constantes subscritas.


`dispfun` cria um Rótulo de expressão intermediária
(`%t1`, `%t2`, etc.)
para cada função mostrada, e atribui a definição de função para o rótulo.
Em contraste, `fundef` retorna a definição de função.


`dispfun` não avalia seus argumentos; 
O operador apóstrofo-apóstrofo `''` faz com que ocorra avaliação.
`dispfun` retorna a lista de rótulos de expressões intermediárias correspondendo às funções mostradas.


Exemplos:












```maxima
(%i1) m(x, y) ::= x^(-y);
                                     - y
(%o1)                   m(x, y) ::= x
(%i2) f(x, y) :=  x^(-y);
                                     - y
(%o2)                    f(x, y) := x
(%i3) g[x, y] :=  x^(-y);
                                    - y
(%o3)                     g     := x
                           x, y
(%i4) h[x](y) :=  x^(-y);
                                    - y
(%o4)                     h (y) := x
                           x
(%i5) i[8](y) :=  8^(-y);
                                    - y
(%o5)                     i (y) := 8
                           8
(%i6) dispfun (m, f, g, h, h[5], h[10], i[8]);
                                     - y
(%t6)                   m(x, y) ::= x

                                     - y
(%t7)                    f(x, y) := x

                                    - y
(%t8)                     g     := x
                           x, y

                                    - y
(%t9)                     h (y) := x
                           x

                                    1
(%t10)                     h (y) := --
                            5        y
                                    5

                                     1
(%t11)                    h  (y) := ---
                           10         y
                                    10

                                    - y
(%t12)                    i (y) := 8
                           8

(%o12)       [%t6, %t7, %t8, %t9, %t10, %t11, %t12]
(%i12) ''%;
                     - y              - y            - y
(%o12) [m(x, y) ::= x   , f(x, y) := x   , g     := x   , 
                                            x, y
                  - y           1              1             - y
        h (y) := x   , h (y) := --, h  (y) := ---, i (y) := 8   ]
         x              5        y   10         y   8
                                5             10
```

<!-- category: Other -->
<!-- keywords: functions -->
<!-- signatures: functions -->
### Variable: functions

Valor padrão: `[]`


`functions` é a lista de todas as funções comuns do Maxima
na sessão corrente.
Uma função comum é uma função construída através de
`define` ou de `:=` e chamada com parêntesis `()`.
Uma função pode ser definida pela linha de comando do Maxima de forma interativa com o usuário
ou em um arquivo Maxima chamado por `load` ou `batch`.


Funções de array (chamadas com colchêtes, e.g., `F[x]`)
e funções com subscritos (chamadas com colchêtes e parêntesis, e.g., `F[x](y)`)
são lsitados através da variável global `arrays`, e não por meio de `functions`.


Funções Lisp não são mantidas em nenhuma lista.


Exemplos:














```maxima
(%i1) F_1 (x) := x - 100;
(%o1)                   F_1(x) := x - 100
(%i2) F_2 (x, y) := x / y;
                                      x
(%o2)                    F_2(x, y) := -
                                      y
(%i3) define (F_3 (x), sqrt (x));
(%o3)                   F_3(x) := sqrt(x)
(%i4) G_1 [x] := x - 100;
(%o4)                    G_1  := x - 100
                            x
(%i5) G_2 [x, y] := x / y;
                                     x
(%o5)                     G_2     := -
                             x, y    y
(%i6) define (G_3 [x], sqrt (x));
(%o6)                    G_3  := sqrt(x)
                            x
(%i7) H_1 [x] (y) := x^y;
                                      y
(%o7)                     H_1 (y) := x
                             x
(%i8) functions;
(%o8)              [F_1(x), F_2(x, y), F_3(x)]
(%i9) arrays;
(%o9)                 [G_1, G_2, G_3, H_1]
```

<!-- category: Other -->
<!-- keywords: fundef -->
<!-- signatures: fundef(f) -->
### Function: fundef (f)

Retorna a definição da função *f*.



O argumento pode ser o nome de uma macro (definida com `::=`),
uma função comum (definida com `:=` ou `define`),
uma função array (definida com `:=` ou `define`,
mas contendo argumentos entre colchêtes `[ ]`),
Uma função subscrita, (definida com `:=` ou `define`,
mas contendo alguns argumentos entre colchêtes e parêntesis `( )`)
uma da família de funções subscritas selecionada por um valor particular subscrito,
ou uma função subscrita definida com uma constante subscrita.


`fundef` não avalia seu argumento;
o operador apóstrofo-apóstrofo `''` faz com que ocorra avaliação.


`fundef (f)` retorna a definição de *f*.
Em contraste, `dispfun (f)` cria um rótulo de expressão intermediária
e atribui a definição para o rótulo.

<!-- category: Other -->
<!-- keywords: funmake -->
<!-- signatures: funmake(F, [arg_1, ..., arg_n]) -->
### Function: funmake (F, [arg_1, ..., arg_n])

Retorna uma expressão `F(arg_1, ..., arg_n)`.
O valor de retorno é simplificado, mas não avaliado,
então a função *F* não é chamada, mesmo se essa função *F* existir.


`funmake` não tenta distinguir funções de array de funções comuns;
quando *F* for o nome de uma função de array,
`funmake` retorna `F(...)`
(isto é, uma chamada de função com parêntesis em lugar de colchêtes).
`arraymake` retorna uma chamada de função com colchêtes nesse caso.


`funmake` avalia seus argumentos.


Exemplos:


`funmake` aplicada a uma função comum do Maxima.








```maxima
(%i1) F (x, y) := y^2 - x^2;
                                   2    2
(%o1)                  F(x, y) := y  - x
(%i2) funmake (F, [a + 1, b + 1]);
(%o2)                    F(a + 1, b + 1)
(%i3) ''%;
                              2          2
(%o3)                  (b + 1)  - (a + 1)
```


`funmake` aplicada a uma macro.








```maxima
(%i1) G (x) ::= (x - 1)/2;
                                  x - 1
(%o1)                    G(x) ::= -----
                                    2
(%i2) funmake (G, [u]);
(%o2)                         G(u)
(%i3) ''%;
                              u - 1
(%o3)                         -----
                                2
```


`funmake` aplicada a uma função subscrita.










```maxima
(%i1) H [a] (x) := (x - 1)^a;
                                        a
(%o1)                   H (x) := (x - 1)
                         a
(%i2) funmake (H [n], [%e]);
                                       n
(%o2)               lambda([x], (x - 1) )(%e)
(%i3) ''%;
                                    n
(%o3)                       (%e - 1)
(%i4) funmake ('(H [n]), [%e]);
(%o4)                        H (%e)
                              n
(%i5) ''%;
                                    n
(%o5)                       (%e - 1)
```


`funmake` aplicada a um símbolo que não é uma função definida de qualquer tipo.







```maxima
(%i1) funmake (A, [u]);
(%o1)                         A(u)
(%i2) ''%;
(%o2)                         A(u)
```


 

`funmake` avalia seus argumentos, mas não o valor de retorno.










```maxima
(%i1) det(a,b,c) := b^2 -4*a*c;
                                    2
(%o1)              det(a, b, c) := b  - 4 a c
(%i2) (x : 8, y : 10, z : 12);
(%o2)                          12
(%i3) f : det;
(%o3)                          det
(%i4) funmake (f, [x, y, z]);
(%o4)                    det(8, 10, 12)
(%i5) ''%;
(%o5)                         - 284
```


Maxima simplifica o valor de retorno de `funmake`.






```maxima
(%i1) funmake (sin, [%pi / 2]);
(%o1)                           1
```

<!-- category: Other -->
<!-- keywords: lambda -->
<!-- signatures: lambda([x_1, ..., x_m], expr_1, ..., expr_n), lambda([[L]], expr_1, ..., expr_n), lambda([x_1, ..., x_m, [L]], expr_1, ..., expr_n) -->
### Function: lambda ([x_1, ..., x_m], expr_1, ..., expr_n)

Define e retorna uma expressão lambda (que é, uma função anônima)
A função pode ter argumentos que sejam necessários *x_1*, ..., *x_m*
e/ou argumentos opcionais *L*, os quais aparecem dentro do corpo da função como uma lista.
O valor de retorno da função é *expr_n*.
Uma expressão lambda pode ser atribuída para uma variável e avaliada como uma função comum.
Uma expressão lambda pode aparecer em alguns contextos nos quais um nome de função é esperado.


Quando a função é avaliada,
variáveis locais não associadas *x_1*, ..., *x_m* são criadas.
`lambda` pode aparecer dentro de `block` ou outra função `lambda`;
variáveis locais são estabelecidas cada vez que outro `block` ou função `lambda` é avaliada.
Variáveis locais parecem ser globais para qualquer coisa contendo `block` ou `lambda`.
Se uma variável é não local,
seu valor é o valor mais recentemente atribuído em alguma coisa contendo `block` ou `lambda`, qualquer que seja,
de outra forma, seu valor é o valor da variável no ambiente global.
Essa política pode coincidir com o entendimento usual de "escopo dinâmico".


Após variáveis locais serem estabelecidas,
*expr_1* até *expr_n* são avaliadas novamente.
a variável especial `%%`, representando o valor da expressão precedente,
é reconhecida.
`throw` e `catch` pode também aparecer na lista de expressões.


`return` não pode aparecer em uma expressão lambda a menos que contendo `block`,
nesse caso `return` define o valor de retorno do  bloco e não da
expressão lambda,
a menos que o bloco seja *expr_n*.
Da mesma forma, `go` não pode aparecer em uma expressão lambda a menos que contendo `block`.


`lambda` não avalia seus argumentos; 
o operador apóstrofo-apóstrofo `''` faz com que ocorra avaliação.


Exemplos:



- *
A expressão lambda pode ser atribuída para uma variável e avaliada como uma função comum.






```maxima
(%i1) f: lambda ([x], x^2);
                                      2
(%o1)                    lambda([x], x )
(%i2) f(a);
                                2
(%o2)                          a
```


- *
Uma expressão lambda pode aparecer em contextos nos quais uma avaliação de função é esperada como resposta.







```maxima
(%i3) lambda ([x], x^2) (a);
                                2
(%o3)                          a
(%i4) apply (lambda ([x], x^2), [a]);
                                2
(%o4)                          a
(%i5) map (lambda ([x], x^2), [a, b, c, d, e]);
                        2   2   2   2   2
(%o5)                 [a , b , c , d , e ]
```


- *
Variáveis argumento são variáveis locais.
Outras variáveis aparecem para serem variáveis globais.
Variáveis globais são avaliadas ao mesmo tempo em que a expressão lambda é avaliada,
a menos que alguma avaliação especial seja forçada por alguns meios, tais como `''`.












```maxima
(%i6) a: %pi$
(%i7) b: %e$
(%i8) g: lambda ([a], a*b);
(%o8)                   lambda([a], a b)
(%i9) b: %gamma$
(%i10) g(1/2);
                             %gamma
(%o10)                       ------
                               2
(%i11) g2: lambda ([a], a*''b);
(%o11)                lambda([a], a %gamma)
(%i12) b: %e$
(%i13) g2(1/2);
                             %gamma
(%o13)                       ------
                               2
```


- *
Expressões lambda podem ser aninhadas.
Variáveis locais dentro de outra expressão lambda parece ser global para a expressão interna
a menos que mascarada por variáveis locais de mesmos nomes.






```maxima
(%i14) h: lambda ([a, b], h2: lambda ([a], a*b), h2(1/2));
                                                   1
(%o14)    lambda([a, b], h2 : lambda([a], a b), h2(-))
                                                   2
(%i15) h(%pi, %gamma);
                             %gamma
(%o15)                       ------
                               2
```


- *
Uma vez que `lambda` não avalia seus argumentos, a expressão lambda `i` abaixo
não define uma função "multiplicação por `a`".
Tanto uma função pode ser definida via `buildq`, como na expressão lambda `i2` abaixo.









```maxima
(%i16) i: lambda ([a], lambda ([x], a*x));
(%o16)            lambda([a], lambda([x], a x))
(%i17) i(1/2);
(%o17)                  lambda([x], a x)
(%i18) i2: lambda([a], buildq([a: a], lambda([x], a*x)));
(%o18)    lambda([a], buildq([a : a], lambda([x], a x)))
(%i19) i2(1/2);
                                     x
(%o19)                   lambda([x], -)
                                     2
(%i20) i2(1/2)(%pi);
                               %pi
(%o20)                         ---
                                2
```


- *
Uma expressão lambda pode receber um número variável de argumentos,
os quais são indicados por meio de `[L]` como o argumento único ou argumento final.
Os argumentos aparecem dentro do corpo da função como uma lista.








```maxima
(%i1) f : lambda ([aa, bb, [cc]], aa * cc + bb);
(%o1)          lambda([aa, bb, [cc]], aa cc + bb)
(%i2) f (foo, %i, 17, 29, 256);
(%o2)       [17 foo + %i, 29 foo + %i, 256 foo + %i]
(%i3) g : lambda ([[aa]], apply ("+", aa));
(%o3)             lambda([[aa]], apply(+, aa))
(%i4) g (17, 29, x, y, z, %e);
(%o4)                  z + y + x + %e + 46
```

<!-- category: Other -->
<!-- keywords: local -->
<!-- signatures: local(v_1, ..., v_n) -->
### Function: local (v_1, ..., v_n)

Declara as variáveis *v_1*, ..., *v_n* para serem locais com
relação a todas as propriedades na declaração na qual essa função
é usada.


`local` não avalia seus argumentos.
`local` retorna `done`.


`local` pode somente ser usada em `block`, no corpo de definições
de função ou expressões `lambda`, ou na função `ev`, e somente uma
ocorrêcia é permitida em cada.


`local` é independente de `context`.

<!-- category: Other -->
<!-- keywords: macroexpansion -->
<!-- signatures: macroexpansion -->
### Variable: macroexpansion

Valor padrão: `false`


`macroexpansion` controla se a expansão (isto é, o valor de retorno) de uma função de macro
é substituído pela chamada à função de macro.
Uma substituição pode aumentar a velocidade de subsequênte avaliações da expressão,
ao custo de armazenar a expansão.



**false** — A expansão de uma função de macro não é substituída pela chamada de função de macro.
**expand** — Da primeira vez que a função de macro é avaliada,
a expansão é armazenada.
A expansão não é recalculada sobre chamadas subsequêntes;
qualquer efeito colateral (tais como `print` ou atribuições a variáveis globais) ocorrem
somente quando chamadas à função de macro forem avaliadas primeiramente.
Expansões em uma expressão não afetam outras expressões
que possuem a mesma chamada à função de macro.
**displace** — Na primeira vez que uma função de macro é avaliada,
a expansão é substituída pela chamada,
dessa forma modificando a expressão a partir da qual a função de macro foi chamada.
A expansão não é recalculada nas chamadas subsequêntes;
qualquer efeito colateral acontece somente quando a chamada à função de macro for avaliada primeiramente.
Expansões na expressão não afetam outras expressões
que possuem a mesma chamada à função de macro.


Exemplos


Quandon `macroexpansion` for `false`,
uma função de macro é chamada a cada vez que a expressão que está chamando é avaliada,
e a expressão que está chamandonão é modificada.












```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x), return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x), return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: false;
(%o4)                         false
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o7)                       --------
                            a b + 99
```


Quando `macroexpansion` for `expand`,
uma função de macro é chamada uma única vez,
e a expressão que está chamando não é modificada.












```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x), return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x), return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: expand;
(%o4)                        expand
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```


Quando `macroexpansion` for `expand`,
uma função de macro é chamada uma única vez,
e a expressão que está chamando é modificada.












```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x), return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x), return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: displace;
(%o4)                       displace
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                 x - 99
(%t6)                    f(x) := ------
                                 x + 99

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```

<!-- category: Other -->
<!-- keywords: mode_check_errorp -->
<!-- signatures: mode_check_errorp -->
### Variable: mode_check_errorp

Valor padrão: `false`



Quando `mode_check_errorp` é `true`, `mode_declare` chama
a função "error".

<!-- category: Other -->
<!-- keywords: mode_check_warnp -->
<!-- signatures: mode_check_warnp -->
### Variable: mode_check_warnp

Valor padrão: `true`



Quando `mode_check_warnp` é `true`, modo "errors" são
descritos.

<!-- category: Other -->
<!-- keywords: mode_checkp -->
<!-- signatures: mode_checkp -->
### Variable: mode_checkp

Valor padrão: `true`



Quando `mode_checkp` é `true`, `mode_declare` verifica os modos
de associação de variáveis.

<!-- category: Other -->
<!-- keywords: mode_declare -->
<!-- signatures: mode_declare(y_1, mode_1, ..., y_n, mode_n) -->
### Function: mode_declare (y_1, mode_1, ..., y_n, mode_n)

`mode_declare` é usado para declarar os modos de variáveis e
funções para subsequênte tradução ou compilação das funções.
`mode_declare` é tipicamente colocada no início de uma definição de
função, no início de um script Maxima, ou executado através da linha de comando de forma interativa.


Os argumentos de `mode_declare` são pares consistindo de  uma variável e o modo que é
um de `boolean`, `fixnum`, `number`, `rational`, ou `float`.
Cada variável pode também
ser uma lista de variáveis todas as quais são declaradas para ter o mesmo modo.



Se uma variável é um array, e se todo elemento do array que é
referenciado tiver um valor então `array (yi, complete, dim1, dim2, ...)`
em lugar de 


```maxima
array(yi, dim1, dim2, ...)
```

deverá ser usado primeiro
declarando as associações do array.

Se todos os elementos do array
estão no modo `fixnum` (`float`), use `fixnum` (`float`) em lugar de `complete`.

Também se todo elemento do array está no mesmo modo, digamos `m`, então



```maxima
mode_declare (completearray (yi), m))
```


deverá ser usado para uma tradução
eficiente.


Código numéricos usando arrays podem rodar mais rápidamente
se for decladado o tamanho esperado do array, como em:



```maxima
mode_declare (completearray (a [10, 10]), float)
```


para um array numérico em ponto flutuante que é 10 x 10.


Pode-se declarar o modo do resultado de uma função
usando `function (f_1, f_2, ...)` como um argumento;
aqui `f_1`, `f_2`, ...  são nomes
de funções.  Por exemplo a expressão,



```maxima
mode_declare ([function (f_1, f_2, ...)], fixnum)
```


declara que os valores retornados por `f_1`, `f_2`, ...  são inteiros palavra simples.


`modedeclare` é um sinônimo para `mode_declare`.

<!-- category: Other -->
<!-- keywords: mode_identity -->
<!-- signatures: mode_identity(arg_1, arg_2) -->
### Function: mode_identity (arg_1, arg_2)

Uma forma especial usada com `mode_declare` e
`macros` para declarar, e.g., uma lista de listas de números em ponto flutuante ou outros
objetos de dados.  O primeiro argumento para `mode_identity` é um valor primitivo
nome de modo como dado para `mode_declare` (i.e., um de `float`, `fixnum`, `number`,
`list`, ou `any`), e o segundo argumento é uma expressão que é
avaliada e retornada com o valor de `mode_identity`.  Todavia, se o
valor de retorno não é permitido pelo modo declarado no primeiro
argumento, um erro ou alerta é sinalizado.  Um ponto importante é
que o modo da expressão como determinado pelo Maxima para o tradutor
Lisp, será aquele dado como o primeiro argumento, independente de
qualquer coisa que vá no segundo argumento.
E.g., `x: 3.3; mode_identity (fixnum, x);` retorna um erro.  `mode_identity (flonum, x)`
returns 3.3 .  
Isso tem númerosas utilidades, e.g., se você soube que `first (l)` retornou um
número então você pode escrever `mode_identity (number, first (l))`.  Todavia,
um mais eficiente caminho para fazer isso é definir uma nova primitiva,



```maxima
firstnumb (x) ::= buildq ([x], mode_identity (number, first(x)));
```


e usar `firstnumb`
toda vez que você pegar o primeiro de uma lista de números.

<!-- category: Other -->
<!-- keywords: tr_array_as_ref -->
<!-- signatures: tr_array_as_ref -->
### Variable: tr_array_as_ref

Valor padrão: `true`


Se `translate_fast_arrays` for `false`, referências a arrays no
Código Lisp emitidas por `translate_file` são afetadas por `tr_array_as_ref`.
Quando `tr_array_as_ref` é `true`,
nomes de arrays são avaliados,
de outra forma nomes de arrays aparecem como símbolos literais no código traduzido.


`tr_array_as_ref` não terão efeito se `translate_fast_arrays` for `true`.

<!-- category: Other -->
<!-- keywords: tr_bound_function_applyp -->
<!-- signatures: tr_bound_function_applyp -->
### Variable: tr_bound_function_applyp

Valor padrão: `true`


Quando `tr_bound_function_applyp` for `true`, Maxima emite um alerta se uma associação
de variável (tal como um argumento de função) é achada sendo usada como uma função.
+
`tr_bound_function_applyp` não afeta o código gerado em tais casos.


Por exemplo, uma expressão tal como `g (f, x) := f (x+1)` irá disparar
a mensagem de alerta.

<!-- category: Other -->
<!-- keywords: tr_file_tty_messagesp -->
<!-- signatures: tr_file_tty_messagesp -->
### Variable: tr_file_tty_messagesp

Valor padrão: `false`


Quando `tr_file_tty_messagesp` é `true`,
messagens geradas por `translate_file` durante a tradução de um arquivo são mostradas
sobre o console e inseridas dentro do arquivo UNLISP.  
Quando `false`, messagens sobre traduções de
arquivos são somente inseridas dentro do arquivo UNLISP.

<!-- category: Other -->
<!-- keywords: tr_float_can_branch_complex -->
<!-- signatures: tr_float_can_branch_complex -->
### Variable: tr_float_can_branch_complex

Valor padrão: `true`


Diz ao tradutor Maxima-para-Lisp assumir que as funções 
`acos`, `asin`, `asec`, e `acsc` podem retornar resultados complexos.


O efeito ostensivo de `tr_float_can_branch_complex` é mostrado adiante.
Todavia, parece que esse sinalizador não tem efeito sobre a saída do tradutor.


Quando isso for `true` então `acos(x)` será do modo `any`
sempre que `x` for do modo `float` (como escolhido por `mode_declare`).
Quando `false` então `acos(x)` será do modo
`float` se e somente se `x` for do modo `float`.

<!-- category: Other -->
<!-- keywords: tr_function_call_default -->
<!-- signatures: tr_function_call_default -->
### Variable: tr_function_call_default

Valor padrão: `general`


`false` significa abandonando e
chamando `meval`, `expr` significa que Lisp assume função de argumento fixado.  `general`, o
código padrão dado como sendo bom para `mexprs` e `mlexprs` mas não `macros`.
`general` garante que associações de variável são corretas em códigos compilados.  No
modo `general`, quando traduzindo F(X), se F for uma variável associada, então isso
assumirá que `apply (f, [x])` é significativo, e traduz como tal, com
o alerta apropriado.  Não é necessário desabilitar isso.  Com as
escolhas padrão, sem mensagens de alerta implica compatibilidade total do
código traduzido e compilado com o interpretador Maxima.

<!-- category: Other -->
<!-- keywords: tr_numer -->
<!-- signatures: tr_numer -->
### Variable: tr_numer

Valor padrão: `false`


Quando `tr_numer` for `true` propriedades `numer` são usadas para
átomos que possuem essa propriedade, e.g. `%pi`.

<!-- category: Other -->
<!-- keywords: tr_optimize_max_loop -->
<!-- signatures: tr_optimize_max_loop -->
### Variable: tr_optimize_max_loop

Valor padrão: 100


`tr_optimize_max_loop` é número máximo de vezes do
passo de macro-expansão e otimização que o tradutor irá executar
considerando uma forma.  Isso é para capturar erros de expansão de macro, e
propriedades de otimização não terminadas.

<!-- category: Other -->
<!-- keywords: tr_semicompile -->
<!-- signatures: tr_semicompile -->
### Variable: tr_semicompile

Valor padrão: `false`


Quando `tr_semicompile` for `true`, as formas de saída de `translate_file`
e `compfile` serão macroexpandidas mas não compiladas em código
de máquina pelo compilador Lisp.

<!-- category: Other -->
<!-- keywords: tr_state_vars -->
<!-- signatures: tr_state_vars -->
### Variable: tr_state_vars

Valor padrão:


```maxima
[transcompile, tr_semicompile, tr_warn_undeclared, tr_warn_meval,
tr_warn_fexpr, tr_warn_mode, tr_warn_undefined_variable,
tr_function_call_default, tr_array_as_ref,tr_numer]
```


A lista de comutadores que afetam a forma de saída da
tradução.

Essa informação é útil para sistemas populares quando
tentam depurar o tradutor.  Comparando o produto traduzido
para o qual pode ter sido produzido por um dado estado, isso é possível para
rastrear erros.

<!-- category: Other -->
<!-- keywords: tr_warn_bad_function_calls -->
<!-- signatures: tr_warn_bad_function_calls -->
### Variable: tr_warn_bad_function_calls

Valor padrão: `true`


- Emite um alerta quando
chamadas de função estão sendo feitas por um caminho que pode não ser correto devido
a declarações impróprias que foram feitas em tempo de tradução.

<!-- category: Other -->
<!-- keywords: tr_warn_fexpr -->
<!-- signatures: tr_warn_fexpr -->
### Variable: tr_warn_fexpr

Valor padrão: `compfile`


- Emite um alerta se quaisquer FEXPRs forem
encontradas.  FEXPRs não poderão normalmente ser saída em código traduzido,
todas as formas de programa especial legítimo são traduzidas.

<!-- category: Other -->
<!-- keywords: tr_warn_meval -->
<!-- signatures: tr_warn_meval -->
### Variable: tr_warn_meval

Valor padrão: `compfile`


- Emite um alerta se a função
`meval` recebe chamadas.  Se `meval` é chamada isso indica problemas na
tradução.

<!-- category: Other -->
<!-- keywords: tr_warn_mode -->
<!-- signatures: tr_warn_mode -->
### Variable: tr_warn_mode

Valor padrão: `all`


- Emite um alerta quando a variáveis forem
atribuídos valores inapropriados para seu modo.

<!-- category: Other -->
<!-- keywords: tr_warn_undeclared -->
<!-- signatures: tr_warn_undeclared -->
### Variable: tr_warn_undeclared

Valor padrão: `compile`


- Determina quando enviar
alertas sobre variáveis não declaradas para o TTY.

<!-- category: Other -->
<!-- keywords: tr_warn_undefined_variable -->
<!-- signatures: tr_warn_undefined_variable -->
### Variable: tr_warn_undefined_variable

Valor padrão: `all`


- Emite um alerta quando
variáveis globais indefinidas forem vistas.

<!-- category: Other -->
<!-- keywords: tr_warnings_get -->
<!-- signatures: tr_warnings_get() -->
### Function: tr_warnings_get ()

Imprime uma lista de alertas que podem ter sido dadas pelo
tradutor durante a tradução corrente.

<!-- category: Other -->
<!-- keywords: transcompile -->
<!-- signatures: transcompile -->
### Variable: transcompile

Valor padrão: `true`


Quando `transcompile` é `true`, `translate` e `translate_file` geram
declarações para fazer o código traduzido mais adequado para compilação.



`compfile` escolhe `transcompile: true` para a duração.

<!-- category: Other -->
<!-- keywords: translate -->
<!-- signatures: translate(f_1, ..., f_n), translate(funções), translate(all) -->
### Function: translate (f_1, ..., f_n)

Traduz funções definidas pelo usuário
*f_1*, ..., *f_n* da linguagem de Maxima para Lisp
e avalia a tradução Lisp.
Tipicamente as funções traduzidas executam mais rápido que as originais.


`translate (all)` ou `translate (funções)` traduz todas as funções definidas pelo usuário.


Funções a serem traduzidas incluir~ao uma chamada para `mode_declare` no
início quando possível com o objetivo de produzir um código mais eficiente.  Por
exemplo:



```maxima
f (x_1, x_2, ...) := block ([v_1, v_2, ...],
    mode_declare (v_1, mode_1, v_2, mode_2, ...), ...)
```




quando *x_1*, *x_2*, ...  são parâmetros para a função e
*v_1*, *v_2*, ...  são variáveis locais.


Os nomes de funções traduzidas
são removidos da lista `functions` se `savedef` é `false` (veja abaixo)
e são adicionados nas listas `props`.


Funções não poderão ser traduzidas
a menos que elas sejam totalmente depuradas.


Expressões são assumidas simplificadas; se não forem, um código correto será gerado mas não será um código
ótimo.  Dessa forma, o usuário não poderá escolher o comutador `simp` para `false`
o qual inibe simplificação de expressões a serem traduzidas.


O comutador `translate`, se `true`, causa tradução
automatica de uma função de usuário para Lisp.


Note que funções
traduzidas podem não executar identicamente para o caminho que elas faziam antes da
tradução como certas incompatabilidades podem existir entre o Lisp
e versões do Maxima.  Principalmente, a função  `rat` com mais de
um argumento e a função `ratvars` não poderá ser usada se quaisquer
variáveis são declaradas com `mode_declare` como sendo expressões rotacionais canônicas(CRE).
Também a escolha `prederror: false`
não traduzirá.



`savedef` - se `true` fará com que a versão Maxima de uma função
 usuário permaneça quando a função é traduzida com `translate`.  Isso permite a
que definição seja mostrada por `dispfun` e autoriza a função a ser
editada.


`transrun` - se `false` fará com que a versão interpretada de todas as
funções sejam executadas (desde que estejam ainda disponíveis) em lugar da
versão traduzida.


O resultado retornado por `translate` é uma lista de nomes de
funções traduzidas.

<!-- category: Other -->
<!-- keywords: translate_file -->
<!-- signatures: translate_file(maxima_nomearquivo), translate_file(maxima_nomearquivo, lisp_nomearquivo) -->
### Function: translate_file (maxima_nomearquivo)

Traduz um arquivo com código Maxima para um arquivo com código Lisp.
`translate_file` retorna uma lista de três nomes de arquivo:
O nome do arquivo Maxima, o nome do arquivo Lisp, e o nome do arquivo
contendo informações adicionais sobre a tradução.
`translate_file` avalia seus argumentos.


`translate_file ("foo.mac"); load("foo.LISP")` é o mesmo que
`batch ("foo.mac")` exceto por certas restrições,
o uso de `''` e `%`, por exemplo.



`translate_file (maxima_nomearquivo)` traduz um arquivo Maxima *maxima_nomearquivo*
para um similarmente chamado arquivo Lisp.
Por exemplo, `foo.mac` é traduzido em `foo.LISP`.
O nome de arquivo Maxima pod incluir nome ou nomes de diretório(s),
nesse caso o arquivo de saída Lisp é escrito
para o mesmo diretório que a entrada Maxima.


`translate_file (maxima_nomearquivo, lisp_nomearquivo)` traduz
um arquivo Maxima *maxima_nomearquivo* em um arquivo Lisp *lisp_nomearquivo*.
`translate_file` ignora a extensão do nome do arquivo, se qualquer, de `lisp_nomearquivo`;
a extensão do arquivo de saída Lisp é sempre `LISP`.
O nome de arquivo Lisp pode incluir um nome ou nomes de diretórios),
nesse caso o arquivo de saída Lisp é escrito para o diretório especificado.


`translate_file` também escreve um arquivo de mensagens de alerta
do tradutor em vários graus de severidade.
A extensão do nome de arquivo desse arquivo é `UNLISP`.
Esse arquivo pode conter informação valiosa, apesar de possivelmente obscura,
para rastrear erros no código traduzido.
O arquivo `UNLISP` é sempre escrito
para o mesmo diretório que a entrada Maxima.


`translate_file` emite código Lisp o qual faz com que
algumas definições tenham efeito tão logo
o código Lisp é compilado.
Veja `compile_file` para mais sobre esse tópico.



Veja também `tr_array_as_ref`,



`tr_bound_function_applyp`,


`tr_exponent`,
`tr_file_tty_messagesp`, 
`tr_float_can_branch_complex`,
`tr_function_call_default`, 
`tr_numer`,
`tr_optimize_max_loop`, 
`tr_semicompile`,
`tr_state_vars`, 
`tr_warnings_get`,
`tr_warn_bad_function_calls`,
`tr_warn_fexpr`, 
`tr_warn_meval`,
`tr_warn_mode`,
`tr_warn_undeclared`,
e `tr_warn_undefined_variable`.

<!-- category: Other -->
<!-- keywords: transrun -->
<!-- signatures: transrun -->
### Variable: transrun

Valor padrão: `true`


Quando `transrun` é `false` fará com que a versão
interpretada de todas as funções sejam executadas (desde que estejam ainda disponíveis)
em lugar de versão traduzidas.

