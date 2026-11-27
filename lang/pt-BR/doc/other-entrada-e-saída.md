## Entrada e Saída

<!-- category: Other -->
<!-- keywords: % -->
<!-- signatures: % -->
### Variable: %

`%` é a expressão de saída (e.g., `%o1`, `%o2`, `%o3`, ...)
mais recentemente calculada pelo Maxima,
pode ou não ser mostrada.


`%` é reconhecida por `batch` e `load`.
Em um arquivo processado por `batch`,
`%` tem o mesmo significado que na linha de comando interativa.
Em um arquivo processado por `load`,
`%` é associado à expressão de entrada mais recentemente calculada na linha de comando interativa 
ou em um arquivo de lote;
`%` não está associada a expressões de saída no arquivo que está sendo processado.


Veja também `_`, `%%`, e `%th`

<!-- category: Other -->
<!-- keywords: %% -->
<!-- signatures: %% -->
### Variable: %%

Em declaração composta,
a saber `block`, `lambda`, ou `(s_1, ..., s_n)`,
`%%` é os valor da declaração anterior.
Por exemplo,



```maxima
block (integrate (x^5, x), ev (%%, x=2) - ev (%%, x=1));
block ([prev], prev: integrate (x^5, x), ev (prev, x=2) - ev (prev, x=1));
```


retornam o mesmo resultado, a saber `21/2`.


Uma declaração composta pode compreender outras declarações compostas.
Pode uma declaração ser simples ou composta, 
`%%` é o valor da declaração anterior.
Por exemplo,



```maxima
block (block (a^n, %%*42), %%/6)
```


retorna `7*a^n`.


Dentro da declaração composta, o valor de `%%` pode ser inspecionado em uma parada de linha de comando,
que é aberta pela execução da função `break`.
Por exemplo, na parada de linha de comando aberta por



```maxima
block (a: 42, break ())$
```


digitando `%%;` retorna `42`.


Na primeira declaração em uma declaração composta,
ou fora de uma declaração composta,
`%%` é indefinido.


`%%`  reconhecido por `batch` e `load`,
e possem o mesmo significao que na linha de comando interativa.


Veja também `%`.

<!-- category: Other -->
<!-- keywords: %edispflag -->
<!-- signatures: %edispflag -->
### Variable: %edispflag

Valor padrão: `false`


Quando `%edispflag` for `true`,
Maxima mostra `%e` para um expoente negativo como um quociente.
Por exemplo, `%e^-x` é mostrado como `1/%e^x`.

<!-- category: Other -->
<!-- keywords: %th -->
<!-- signatures: %th(i) -->
### Function: %th (i)

O valor da *i*’ésima expressão prévia de saída.
Isto é, se a próxima expressão a ser calculada for a *n*’ésima saída,
`%th (m)` será a (*n* - *m*)’ésima saída.


`%th` é útil em arquivos `batch` ou para referir-se a um grupo de expressões de saída.
Por exemplo,



```maxima
block (s: 0, for i:1 thru 10 do s: s + %th (i))$
```


atribui à variável `s` a soma das últimas dez expressões de saída.


`%th` é reconhecido por `batch` e `load`.
Em um arquivo processado por `batch`,
`%th` possue o mesmo significado que na linha de comando interativa.
Em um arquivo processado por `load`,
`%th` refere-se a expressões de saída mais recentemente calculadas na linha de comando interativa
ou em um arquivo de lote;
`%th` não se refere a expressões de saída no arquivo que está sendo processado.


Veja também `%`.

<!-- category: Other -->
<!-- keywords: ? -->
<!-- signatures: ? -->
### Function: ?

Como prefixo para uma função ou nome de variável, `?` significa que
o nome é um nome Lisp, não um nome Maxima.
Por exemplo, `?round` significa a função Lisp `ROUND`.
Veja `Lisp-e-Maxima` para mais sobre esse ponto.


A notação `? palavra` (um ponto de interrogação seguido de uma palavra e separado desta por um espaço em branco)
é equivalente a `describe("palavra")`.
O ponto de interrogação deve aparecer no início de uma linha de entrada;
de outra forma o ponto de interrogação não é reconhecido com um pedido de documentação.

See also: `Lisp-e-Maxima`.

<!-- category: Other -->
<!-- keywords: ?? -->
<!-- signatures: ?? -->
### Function: ??

A notação `?? palavra` (`??` seguido de um espaço em branco e uma palavra)
é equivalente a `describe("palavra", inexact)`.
O ponto de interrogação deve ocorrer no início de uma linha de entrada;
de outra forma não é reconhecido com um pedido de documentação.

<!-- category: Other -->
<!-- keywords: _ -->
<!-- signatures: _ -->
### Variable: _

`_` é a mais recente expressão de  entrada (e.g., `%i1`, `%i2`, `%i3`, ...).


A `_` é atribuída à expressão de entrada antes dela ser simplificada ou avaliada.
Todavia, o valor de `_` é simplificado (mas não avaliado) quando for mostrado.


`_` é reconhecido por `batch` e `load`.
Em um arquivo processado por `batch`,
`_` tem o mesmo significado que na linha de comando interativa.
Em um arquivo processado por load `load`,
`_` está associado à expressão de entrada mais recentemente avaliada na linha de comando interativa
ou em um arquivo de lote;
`_` não está associada a expressões de entrada no arquivo que está sendo processado.


Veja também `__` e `%`.


Exemplos:


















```maxima
(%i1) 13 + 29;
(%o1)                          42
(%i2) :lisp $_
((MPLUS) 13 29)
(%i2) _;
(%o2)                          42
(%i3) sin (%pi/2);
(%o3)                           1
(%i4) :lisp $_
((%SIN) ((MQUOTIENT) $%PI 2))
(%i4) _;
(%o4)                           1
(%i5) a: 13$
(%i6) b: 29$
(%i7) a + b;
(%o7)                          42
(%i8) :lisp $_
((MPLUS) $A $B)
(%i8) _;
(%o8)                         b + a
(%i9) a + b;
(%o9)                          42
(%i10) ev (_);
(%o10)                         42
```

<!-- category: Other -->
<!-- keywords: __ -->
<!-- signatures: __ -->
### Variable: __

`__` é a expressão de entrada atualmente sendo avaliada.
Isto é, enquanto um expressão de entrada *expr* está sendo avaliada, `__` é *expr*.


`__` é atribuída à expressão de entrada antes de a entrada ser simplificada ou avaliada.
Todavia, o valor de `__` é simplificado (mas não avaliado) quando for mostrado.


`__` é reconhecido por `batch` e `load`.
Em um arquivo processado por `batch`,
`__` tem o mesmo significado que na linha de comando interativa.
Em um arquivo processado por `load`,
`__` está associado à expressão de entrada mais recentemente informada no prompt interativo
ou em um arquivo de lote (batch);
`__` não é associado à expressões de entrada no arquivo que está sendo processado.
Em particular, quando `load (nomearquivo)` for chamado a partir da linha de comando interativa,
`__` é associado a `load (nomearquivo)`
enquanto o arquivo está sendo processado.


Veja também `_` e `%`.


Exemplos:










```maxima
(%i1) print ("Eu fui chamada como", __);
Eu fui chamada como print(Eu fui chamada como, __) 
(%o1)              print(Eu fui chamada como, __)
(%i2) foo (__);
(%o2)                     foo(foo(__))
(%i3) g (x) := (print ("Expressão atual de entrada =", __), 0);
(%o3) g(x) := (print("Expressão atual de entrada =", __), 0)
(%i4) [aa : 1, bb : 2, cc : 3];
(%o4)                       [1, 2, 3]
(%i5) (aa + bb + cc)/(dd + ee + g(x));
                               cc + bb + aa
Expressão atual de entrada = -------------- 
                              g(x) + ee + dd
                                6
(%o5)                        -------
                             ee + dd
```

<!-- category: Other -->
<!-- keywords: absboxchar -->
<!-- signatures: absboxchar -->
### Variable: absboxchar

Valor padrão: `!`


`absboxchar` é o caracter usado para para desenhar o sinal de valor
absoluto em torno de expressões que são maiores que uma linha de altura.

<!-- category: Other -->
<!-- keywords: appendfile -->
<!-- signatures: appendfile(nomearquivo) -->
### Function: appendfile (nomearquivo)

Adiciona ao final de *nomearquivo* uma transcrição do console.
`appendfile` é o mesmo que `writefile`, 
exceto que o arquivo transcrito, se já existe, terá sempre alguma coisa adicionada ao seu final.


`closefile` fecha o arquivo transcrito que foi aberto anteriormente por `appendfile` ou por `writefile`.

<!-- category: Other -->
<!-- keywords: batch -->
<!-- signatures: batch(nomearquivo) -->
### Function: batch (nomearquivo)

Lê expressões Maxima do arquivo *nomearquivo* e as avalia.
`batch` procura pelo arquivo *nomearquivo* na lista `file_search_maxima`.
Veja `file_search`.


*nomearquivo* compreende uma sequência de expressões Maxima,
cada uma terminada com `;` ou `$`.
A varável especial `%` e a função `%th`
referem-se a resultados prévios dentro do arquivo.
O arquivo pode incluir construções `:lisp`.
Espaços, tabulações, e o caracter de nova linha no arquivo serão ignorados.
um arquivo de entrada conveniente pode ser criado por um editor de texto ou pela função `stringout`.


`batch` lê cada expressão de entrada de *nomearquivo*,
mostra a entrada para o console, 
calcula a correspondente expressão de saída,
e mostra a expressão de saída.
Rótulos de entrada são atribuídos para expressões de entrada
e rótulos de saída são atribuídos para expressões de saída.
`batch` avalia toda expressão de entrada no arquivo
a menos que exista um erro.
Se uma entrada de usuário for requisitada (por `asksign` ou por `askinteger`, por exemplo)
`batch` interrompe para coletar a entrada requisitada e então continua.




O recurso de requisição de entrada ao usuário possibilita interromper `batch` pela digitação de `control-C` no console.
O efeito de `control-C` depende da subjacente implementação do Lisp.


`batch` tem muitos usos,
tais como fornecer um reservatório para trabalhar linhas de comando,
para fornecer demonstrações livres de erros,
ou para ajudar a organizar alguma coisa na solução de problemas complexos.


`batch` avalia seu argumento.

`batch` não possui valor de retorno.


Veja também `load`, `batchload`, e `demo`.

<!-- category: Other -->
<!-- keywords: batchload -->
<!-- signatures: batchload(nomearquivo) -->
### Function: batchload (nomearquivo)

Lê expressões Maxima de *nomearquivo* e as avalia,
sem mostrar a entrada ou expressões de saída
e sem atribuir rótulos para expressões de saída.
Saídas impressas (tais como produzidas por `print` ou `describe`)
são mostradas, todavia.


A variável especial `%` e a função `%th`
referem-se a resultados anteriores do interpretador interativo,
não a resultados dentro do arquivo.
O arquivo não pode incluir construções `:lisp`.


`batchload` retorna o caminho de *nomearquivo*, como uma sequência de caracteres.
`batchload` avalia seu argumento.


Veja também `batch` e `load`.

<!-- category: Other -->
<!-- keywords: closefile -->
<!-- signatures: closefile() -->
### Function: closefile ()

Fecha o arquivo transcrito aberto por `writefile` ou `appendfile`.

<!-- category: Other -->
<!-- keywords: collapse -->
<!-- signatures: collapse(expr) -->
### Function: collapse (expr)

Reduz *expr* fazendo com que todas as suas
subexpressões comuns (i.e., iguais)  sejam compartilhadas (i.e., usam a mesma células),
dessa forma economizando espaço.  (`collapse` é uma subrotina usada pelo comando
`optimize`.)  Dessa forma, chamar `collapse` pode ser útil
após um `save` arquivo.  Você pode diminuir muitas expressões
juntas pelo uso de `collapse ([expr_1, ..., expr_n])`.  Similarmente, você pode
diminuir os elementos de um array `A` fazendo
`collapse (listarray ('A))`.

<!-- category: Other -->
<!-- keywords: concat -->
<!-- signatures: concat(arg_1, arg_2, ...) -->
### Function: concat (arg_1, arg_2, ...)

Concatena seus argumentos.
Os argumentos devem obrigatóriamente serem avaliados para atomos.
O valor de retorno ou é um símbolo se o primeiro argumento for um símbolo
ou é uma sequência de caracteres no formato do Maxima em caso contrário.


`concat` avalia seus argumentos.
O apóstrofo `'` evita avaliação.



```maxima
(%i1) y: 7$
(%i2) z: 88$
(%i3) concat (y, z/2);
(%o3)                          744
(%i4) concat ('y, z/2);
(%o4)                          y44
```


Um símbolo construído por `concat` pode
ser atribuído a um valor e aparecer em expressões.
O operador de atribuição `::` (duplo dois pontos) avalia seu lado esquerdo.



```maxima
(%i5) a: concat ('y, z/2);
(%o5)                          y44
(%i6) a:: 123;
(%o6)                          123
(%i7) y44;
(%o7)                          123
(%i8) b^a;
                               y44
(%o8)                         b
(%i9) %, numer;
                               123
(%o9)                         b
```


Note que embora `concat (1, 2)` seja visto como números no console, na realidade é uma sequência de caracteres no formato do Maxima.



```maxima
(%i10) concat (1, 2) + 3;
(%o10)                       12 + 3
```

<!-- category: Other -->
<!-- keywords: disp -->
<!-- signatures: disp(expr_1, expr_2, ...) -->
### Function: disp (expr_1, expr_2, ...)

é como `display` mas somente os valores dos
argumentos são mostrados em lugar de equações.  A função `disp` é útil para
argumentos complicados que não possuem nomes ou onde somente o valor
do argumento é de interesse e não o nome.

<!-- category: Other -->
<!-- keywords: dispcon -->
<!-- signatures: dispcon(tensor_1, tensor_2, ...), dispcon(all) -->
### Function: dispcon (tensor_1, tensor_2, ...)

Mostra as propriedades de contração de
seus argumentos da forma que foram dadas para `defcon`.  `dispcon (all)` mostra todas as
propriedades de contração que foram definidas.

<!-- category: Other -->
<!-- keywords: display -->
<!-- signatures: display(expr_1, expr_2, ...) -->
### Function: display (expr_1, expr_2, ...)

Mostra equações cujo lado esquerdo é
*expr_i* não avaliado, e cujo lado direito é o valor da expressão
centrada na linha.  Essa função é útil em blocos e em `for`
declarações com o objetivo de ter resultados intermediários mostrados.  Os
argumentos para `display` são usualmente átomos, variáveis com subscritos, ou
chamadas de função.  Veja também `disp`.



```maxima
(%i1) display(B[1,2]);
                                      2
                         B     = X - X
                          1, 2
(%o1)                            done
```

<!-- category: Other -->
<!-- keywords: display2d -->
<!-- signatures: display2d -->
### Variable: display2d

Valor padrão: `true`


Quando `display2d` for `false`,
O console visualizador é da forma de uma sequência de caracteres (unidimensional) ao invés da
forma bidimensional.

<!-- category: Other -->
<!-- keywords: display_format_internal -->
<!-- signatures: display_format_internal -->
### Variable: display_format_internal

Valor padrão: `false`


Quando `display_format_internal` é `true`,
expressões são mostradas sem ser por caminhos que
escondam a representação matemática interna.  O visualizador então
corresponde ao que `inpart` retorna em lugar de `part`.


Exemplos:



```maxima
User     part       inpart
a-b;      A - B     A + (- 1) B

           A            - 1
a/b;       -         A B
           B
                       1/2
sqrt(x);   sqrt(X)    X

          4 X        4
X*4/3;    ---        - X
           3         3
```

<!-- category: Other -->
<!-- keywords: dispterms -->
<!-- signatures: dispterms(expr) -->
### Function: dispterms (expr)

Mostra *expr* em partes uma abaixo da outra.
Isto é, primeiro o operador de *expr* é mostrado, então cada parcela em
uma adição, ou fatores em um produto, ou parte de uma expressão mais geral é
mostrado separadamente.  Isso é útil se *expr* é muito larga para ser
mostrada de outra forma.  Por exemplo se `P1`, `P2`, ...  são expressões
muito largas então o programa visualizador pode sair fora do espaço de armazenamento na
tentativa de mostrar `P1 + P2 + ...`  tudo de uma vez.  Todavia,
`dispterms (P1 + P2 + ...)` mostra `P1`, então abaixo disso `P2`, etc.  Quando não
usando `dispterms`, se uma expressão exponencial é muito alta para ser
mostrada como `A^B` isso aparece como `expt (A, B)` (ou como `ncexpt (A, B)` no
caso de `A^^B`).

<!-- category: Other -->
<!-- keywords: error_size -->
<!-- signatures: error_size -->
### Variable: error_size

Valor padrão: 10


`error_size` modifica mensagens de erro conforme o tamanho das expressões que aparecem nelas.
Se o tamanho de uma expressão (como determinado pela função Lisp `ERROR-SIZE`)
é maior que `error_size`,
a expressão é substituída na mensagem por um símbolo,
e o o símbolo é atribuído à expressão.
Os símbolos são obtidos da lista `error_syms`.


De outra forma, a expressão é menor que `error_size`,
e a expressão é mostrada na mensagem.


Veja também `error` e `error_syms`.


Exemplo:









O tamanho de `U`, como determinado por `ERROR-SIZE`, é 24.



```maxima
(%i1) U: (C^D^E + B + A)/(cos(X-1) + 1)$

(%i2) error_size: 20$

(%i3) error ("Expressão exemplo é", U);

Expressão exemplo é errexp1
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) errexp1;
                            E
                           D
                          C   + B + A
(%o4)                    --------------
                         cos(X - 1) + 1
(%i5) error_size: 30$

(%i6) error ("Expressão exemplo é", U);

                           E
                          D
                         C   + B + A
Expressão exemplo é --------------
                        cos(X - 1) + 1
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Other -->
<!-- keywords: error_syms -->
<!-- signatures: error_syms -->
### Variable: error_syms

Valor padrão: `[errexp1, errexp2, errexp3]`


Em mensagens de erro,
expressões mais largas que `error_size` são substituídas por símbolos, e os
símbolos são escolhidos para as expressões.  Os símbolos são obtidos da
lista `error_syms`.
A primeira expressão muito larga é substituída por `error_syms[1]`,
a segunda por `error_syms[2]`, e assim por diante.


Se houverem mais expressões muito largas que há elementos em `error_syms`,
símbolos são construídos automaticamente,
com o *n*-ésimo símbolo equivalente a `concat ('errexp, n)`.


Veja também `error` e `error_size`.

<!-- category: Other -->
<!-- keywords: expt -->
<!-- signatures: expt(a, b) -->
### Function: expt (a, b)

Se uma expressão exponencial é muito alta para ser mostrada
cmo `a^b` isso aparece como `expt (a, b)` (ou como `ncexpt (a, b)` no caso de
`a^^b`).




`expt` e `ncexpt` não são reconhecidas em entradas.

<!-- category: Other -->
<!-- keywords: exptdispflag -->
<!-- signatures: exptdispflag -->
### Variable: exptdispflag

Valor padrão: `true`


Quando `exptdispflag` é `true`, Maxima mostra expressões
com expoente negativo usando quocientes, e.g., `X^(-1)` como `1/X`.

<!-- category: Other -->
<!-- keywords: file_output_append -->
<!-- signatures: file_output_append -->
### Variable: file_output_append

Valor padrão: `false`


`file_output_append` governa se funções de saída de arquivo
anexam ao final ou truncam seu arquivo de saída.
Quando `file_output_append` for `true`,
tais funções anexam ao final de seu arquivo de saída.
De outra forma, o arquivo de saída é truncado.


`save`, `stringout`, e `with_stdout` respeitam `file_output_append`.
Outras funções que escrevem arquivos de saída não respeitam `file_output_append`.
Em particular, montagem de gráficos e traduções de funções sempre truncam seu arquivo de saída,
e `tex` e `appendfile` sempre anexam ao final.

<!-- category: Other -->
<!-- keywords: file_search -->
<!-- signatures: file_search(nomearquivo), file_search(nomearquivo, listacaminho) -->
### Function: file_search (nomearquivo)

`file_search` procura pelo arquivo *nomearquivo* e retorna o caminho para o arquivo
(como uma sequência de caracteres) se ele for achado; de outra forma `file_search` retorna `false`.
`file_search (nomearquivo)` procura nos diretórios padrões de busca,
que são especificados pelas variáveis `file_search_maxima`, `file_search_lisp`, e `file_search_demo`.


`file_search` primeiro verifica se o nome atual passado existe,
antes de tentar coincidir esse nome atual com o modelo “coringa” de busca do arquivo.
Veja `file_search_maxima` concernente a modelos de busca de arquivos.


O argumento *nomearquivo* pode ser um caminho e nome de arquivo,
ou apenas um nome de arquivo, ou, se um diretório de busca de arquivo inclui um modelo de busca de arquivo,
apenas a base do nome de arquivo (sem uma extensão).
Por exemplo,



```maxima
file_search ("/home/wfs/special/zeta.mac");
file_search ("zeta.mac");
file_search ("zeta");
```


todos encontram o mesmo arquivo, assumindo que o arquivo exista e `/home/wfs/special/###.mac`
está em `file_search_maxima`.


`file_search (nomearquivo, listacaminho)` procura somente nesses diretórios
especificados por *listacaminho*,
que é uma lista de sequências de caracteres.
O argumento *listacaminho* substitui os diretórios de busca padrão,
então se a lista do caminho é dada, `file_search` procura somente nesses especificados,
e não qualquer dos diretórios padrão de busca.
Mesmo se existe somente um diretório em *listacaminho*, esse deve ainda ser dado como uma lista de um único elemento.


O usuário pode modificar o diretório de busca padrão.  Veja `file_search_maxima`.


`file_search` é invocado por `load` com `file_search_maxima` e `file_search_lisp`
como diretórios de busca.

<!-- category: Other -->
<!-- keywords: file_search_maxima, file_search_lisp, file_search_demo -->
<!-- signatures: file_search_lisp, file_search_demo -->
### Variable: file_search_maxima

Essas variáveis especificam listas de diretórios a serem procurados
por `load`, `demo`, e algumas outras funções do Maxima.
O valor padrão dessas variáveis
nomeia vários diretórios na instalaçã padrão do Maxima.


O usuáro pode modificar essas variáveis,
quer substituindo os valores padrão ou colocando no final diretórios adicionais.
Por exemplo,



```maxima
file_search_maxima: ["/usr/local/foo/###.mac",
    "/usr/local/bar/###.mac"]$
```


substitui o valor padrão de `file_search_maxima`,
enquanto



```maxima
file_search_maxima: append (file_search_maxima,
    ["/usr/local/foo/###.mac", "/usr/local/bar/###.mac"])$
```


adiciona no final da lista dois diretórios adicionais.
Isso pode ser conveniente para colocar assim uma expressão no arquivo `maxima-init.mac`
de forma que o caminho de busca de arquivo é atribuído automaticamente quando o Maxima inicia.


Multiplas extensões de arquivo e e multiplos caminhos podem ser especificados por
construções “coringa” especiais.
A sequência de caracteres `###` expande a busca para além do nome básico,
enquanto uma lista separada por vírgulas e entre chaves `{foo,bar,baz}` expande
em multiplas sequências de caracteres.
Por exemplo, supondo que o nome básico a ser procurado seja `neumann`,



```maxima
"/home/{wfs,gcj}/###.{lisp,mac}"
```


expande em `/home/wfs/neumann.lisp`, `/home/gcj/neumann.lisp`, `/home/wfs/neumann.mac`, e `/home/gcj/neumann.mac`.

<!-- category: Other -->
<!-- keywords: file_type -->
<!-- signatures: file_type(nomearquivo) -->
### Function: file_type (nomearquivo)

Retorna uma suposta informação sobre o conteúdo de *nomearquivo*,
baseada na extensão do arquivo.
*nomearquivo* não precisa referir-se a um arquivo atual;
nenhuma tentativa é feita para abrir o arquivo e inspecionar seu conteúdo.


O valor de retorno é um símbolo, qualquer um entre `object`, `lisp`, ou `maxima`.
Se a extensão começa com `m` ou `d`, `file_type` retorna `maxima`.
Se a extensão começa om `l`, `file_type` retorna `lisp`.
Se nenhum dos acima, `file_type` retorna `object`.

<!-- category: Other -->
<!-- keywords: filename_merge -->
<!-- signatures: filename_merge(path, nomearquivo) -->
### Function: filename_merge (path, nomearquivo)

Constroem um caminho modificado de *path* e *nomearquivo*.
Se o componente final de *path* é da forma `###.algumacoisa`,
o componente é substituído com `nomearquivo.algumacoisa`.
De outra forma, o componente final é simplesmente substituído por *nomearquivo*.

<!-- category: Other -->
<!-- keywords: grind -->
<!-- signatures: grind(expr) -->
### Function: grind (expr)

A função `grind` imprime *expr*
para o console em uma forma adequada de entrada para Maxima.
`grind` sempre retorna `done`.


Quando *expr* for um nome de uma função ou o nome de uma macro,
`grind` mostra na tela a definição da função ou da macro em lugar de apenas o nome.


Veja também `string`, que retorna uma sequência de caracteres em lugar de imprimir sua saída.
`grind` tenta imprimir a expressão de uma maneira que a faz
levemente mais fácil para ler que a saída de `string`.


Quando a variável `grind` é `true`,
a saída de `string` e `stringout` tem o mesmo formato que `grind`;
de outra forma nenhuma tentativa é feita para formatar especialmente a saída dessas funções.
O valor padrão da variável `grind` é `false`.


`grind` pode também ser especificado como um argumento de `playback`.
Quando `grind` está presente,
`playback` imprime expressões de entrada no mesmo formato que a função `grind`.
De outra forma, nenhuma tentativa é feita para formatar especialmente as expressões de entrada.


`grind` avalia seus argumentos.


Exemplos:

























```maxima
(%i1) aa + 1729;
(%o1)                       aa + 1729
(%i2) grind (%);
aa+1729$
(%o2)                         done
(%i3) [aa, 1729, aa + 1729];
(%o3)                 [aa, 1729, aa + 1729]
(%i4) grind (%);
[aa,1729,aa+1729]$
(%o4)                         done
(%i5) matrix ([aa, 17], [29, bb]);
                           [ aa  17 ]
(%o5)                      [        ]
                           [ 29  bb ]
(%i6) grind (%);
matrix([aa,17],[29,bb])$
(%o6)                         done
(%i7) set (aa, 17, 29, bb);
(%o7)                   {17, 29, aa, bb}
(%i8) grind (%);
{17,29,aa,bb}$
(%o8)                         done
(%i9) exp (aa / (bb + 17)^29);
                                aa
                            -----------
                                     29
                            (bb + 17)
(%o9)                     %e
(%i10) grind (%);
%e^(aa/(bb+17)^29)$
(%o10)                        done
(%i11) expr: expand ((aa + bb)^10);
         10           9        2   8         3   7         4   6
(%o11) bb   + 10 aa bb  + 45 aa  bb  + 120 aa  bb  + 210 aa  bb
         5   5         6   4         7   3        8   2
 + 252 aa  bb  + 210 aa  bb  + 120 aa  bb  + 45 aa  bb
        9        10
 + 10 aa  bb + aa
(%i12) grind (expr);
bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6
     +252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2
     +10*aa^9*bb+aa^10$
(%o12)                        done
(%i13) string (expr);
(%o13) bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6\
+252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2+10*aa^9*\
bb+aa^10
(%i14) cholesky (A):= block ([n : length (A), L : copymatrix (A),
p : makelist (0, i, 1, length (A))], for i thru n do for j : i thru n do
(x : L[i, j], x : x - sum (L[j, k] * L[i, k], k, 1, i - 1), if i = j then
p[i] : 1 / sqrt(x) else L[j, i] : x * p[i]), for i thru n do L[i, i] : 1 / p[i],
for i thru n do for j : i + 1 thru n do L[i, j] : 0, L)$
(%i15) grind (cholesky);
cholesky(A):=block(
         [n:length(A),L:copymatrix(A),
          p:makelist(0,i,1,length(A))],
         for i thru n do
             (for j from i thru n do
                  (x:L[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),
                   if i = j then p[i]:1/sqrt(x)
                       else L[j,i]:x*p[i])),
         for i thru n do L[i,i]:1/p[i],
         for i thru n do (for j from i+1 thru n do L[i,j]:0),L)$
(%o15)                        done
(%i16) string (fundef (cholesky));
(%o16) cholesky(A):=block([n:length(A),L:copymatrix(A),p:makelis\
t(0,i,1,length(A))],for i thru n do (for j from i thru n do (x:L\
[i,j],x:x-sum(L[j,k]*L[i,k],k,1,i-1),if i = j then p[i]:1/sqrt(x\
) else L[j,i]:x*p[i])),for i thru n do L[i,i]:1/p[i],for i thru \
n do (for j from i+1 thru n do L[i,j]:0),L)
```

<!-- category: Other -->
<!-- keywords: ibase -->
<!-- signatures: ibase -->
### Variable: ibase

Valor padrão: 10


Inteiros fornecidos dentro do Maxima são interpretados
com respeito à base `ibase`.


A `ibase` pode ser atribuído qualquer inteiro entre 2 e 35 (decimal), inclusive.

Quando `ibase` é maior que 10, os numerais compreendem aos numerais decimais de 0 até 9

mais as letras maiúsculas do alfabeto A, B, C, ..., como necessário.
Os numerais para a base 35, a maior base aceitável,
compreendem de 0 até 9 e de A até Y.





Veja também `obase`.

<!-- category: Other -->
<!-- keywords: inchar -->
<!-- signatures: inchar -->
### Variable: inchar

Valor padrão: `%i`


`inchar` é o prefixo dos rótulos de expressões fornecidas pelo usuário.
Maxima automaticamente constrói um rótulo para cada expressão de entrada
por concatenação de `inchar` e `linenum`.
A `inchar` pode ser atribuído qualquer sequência de caracteres ou símbolo, não necessariamente um caracter simples.



```maxima
(%i1) inchar: "input";
(%o1)                                input
(input1) expand ((a+b)^3);
                            3        2      2      3
(%o1)                      b  + 3 a b  + 3 a  b + a
(input2)
```


Veja também `labels`.

<!-- category: Other -->
<!-- keywords: ldisp -->
<!-- signatures: ldisp(expr_1, ..., expr_n) -->
### Function: ldisp (expr_1, ..., expr_n)

Mostra expressões *expr_1*, ..., *expr_n* para o console
como saída impressa na tela.
`ldisp` atribue um rótulo de expressão intermediária a cada argumento
e retorna a lista de rótulos.


Veja também `disp`.



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisp (e, f);
                                   3
(%t3)                       (b + a)

                     3        2      2      3
(%t4)               b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                   3
(%o4)                       (b + a)
(%i5) %t4;
                     3        2      2      3
(%o5)               b  + 3 a b  + 3 a  b + a
```

<!-- category: Other -->
<!-- keywords: ldisplay -->
<!-- signatures: ldisplay(expr_1, ..., expr_n) -->
### Function: ldisplay (expr_1, ..., expr_n)

Mostra expressões *expr_1*, ..., *expr_n* para o console
como saída impressa na tela.
Cada expressão é impressa como uma equação da forma `lhs = rhs`
na qual `lhs` é um dos argumentos de `ldisplay`
e `rhs` é seu valor.
Tipicamente cada argumento é uma variável.
`ldisp` atribui um rótulo de expressão intermediáia a cada equação
e retorna a lista de rótulos.


Veja também `display`.



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisplay (e, f);
                                     3
(%t3)                     e = (b + a)

                       3        2      2      3
(%t4)             f = b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                     3
(%o4)                     e = (b + a)
(%i5) %t4;
                       3        2      2      3
(%o5)             f = b  + 3 a b  + 3 a  b + a
```

<!-- category: Other -->
<!-- keywords: linechar -->
<!-- signatures: linechar -->
### Variable: linechar

Valor padrão: `%t`


`linechar` é o refixo de rótulos de expressões intermediárias gerados pelo Maxima.
Maxima constrói um rótulo para cada expressão intermediária (se for mostrada)
pela concatenação de `linechar` e `linenum`.
A `linechar` pode ser atribuído qualquer sequência de caracteres ou símbolo, não necessáriamente um caractere simples.


Expressões intermediárias podem ou não serem mostradas.
See `programmode` e `labels`.

<!-- category: Other -->
<!-- keywords: linel -->
<!-- signatures: linel -->
### Variable: linel

Valor padrão: 79


`linel` é a largura assumida (em caracteres) do console
para o propósito de mostrar expressões.
A `linel` pode ser atribuído qualquer valor pelo usuário,
embora valores muio pequenos ou muito grandes possam ser impraticáveis.
Textos impressos por funções internas do Maxima, tais como mensagens de erro e a saída de `describe`,
não são afetadas por `linel`.

<!-- category: Other -->
<!-- keywords: lispdisp -->
<!-- signatures: lispdisp -->
### Variable: lispdisp

Valor padrão: `false`


Quando `lispdisp` for `true`,
símbolos Lisp são mostrados com um ponto de interrogação `?` na frente.
De outra forma,
símbolos Lisp serão mostrados sem o ponto de interrogação na frente.


Exemplos:









```maxima
(%i1) lispdisp: false$
(%i2) ?foo + ?bar;
(%o2)                       foo + bar
(%i3) lispdisp: true$
(%i4) ?foo + ?bar;
(%o4)                      ?foo + ?bar
```

<!-- category: Other -->
<!-- keywords: load -->
<!-- signatures: load(nomearquivo) -->
### Function: load (nomearquivo)

Avalia expressões em *nomearquivo*, 
dessa forma conduzindo variáveis, funções, e outros objetos dentro do Maxima.
A associação de qualquer objeto existente é substituída pela associação recuperada de *nomearquivo*.  
Para achar o arquivo,
`load` chama `file_search` com `file_search_maxima` e `file_search_lisp`
como diretórios de busca.
Se `load` obtém sucesso, isso retorna o nome do arquivo.
De outra forma `load` imprime uma mensagem e erro.


`load` trabalha igualmente bem para códigos Lisp e códigos Maxima.
Arquivos criados por `save`, `translate_file`, e `compile_file`, que criam códigos Lisp,
e `stringout`, que criam códigos Maxima,
podem ser processadas por `load`.
`load` chama `loadfile` para carregar arquivos Lisp e `batchload` para carregar arquivos Maxima.


`load` não reconhece construções `:lisp` em arquivos do Maxima,
e quando processando *nomearquivo*,
as variáveis globais `_`, `__`, `%`, e `%th` possuem as mesmas associações
que possuiam quando `load` foi chamada.


Veja também `loadfile`, `batch`, `batchload`, e `demo`.
`loadfile` processa arquivos Lisp;
`batch`, `batchload`, e `demo` processam arquivos Maxima.


Veja `file_search` para mais detalhes sobre o mecanismo de busca de arquivos.


`load` avalia seu argumento.

<!-- category: Other -->
<!-- keywords: loadfile -->
<!-- signatures: loadfile(nomearquivo) -->
### Function: loadfile (nomearquivo)

Avalia expressões Lisp em *nomearquivo*.
`loadfile` não invoca `file_search`, então `nomearquivo` deve obrigatóriamente incluir
a extensão do arquivo e tanto quanto o caminho como necessário para achar o arquivo.


`loadfile` pode processar arquivos criados por `save`, `translate_file`, e `compile_file`.
O usuário pode achar isso mais conveniente para usar `load` em lugar de `loadfile`.

<!-- category: Other -->
<!-- keywords: loadprint -->
<!-- signatures: loadprint -->
### Variable: loadprint

Valor padrão: `true`


`loadprint` diz se deve imprimir uma mensagem quando um arquivo é chamado.



- *
Quando `loadprint` é `true`, sempre imprime uma mensagem.
- *
Quando `loadprint` é `'loadfile`, imprime uma mensagem somente se
um arquivo é chamado pela função `loadfile`.
- *
Quando `loadprint` é `'autoload`,
imprime uma mensagem somente se um arquivo é automaticamente carregado.
Veja `setup_autoload`.
- *
Quando `loadprint` é `false`, nunca imprime uma mensagem.

<!-- category: Other -->
<!-- keywords: obase -->
<!-- signatures: obase -->
### Variable: obase

Valor padrão: 10


`obase` é a base para inteiros mostrados pelo Maxima.


A `obase` poode ser atribuído qualquer inteiro entre 2 e 35 (decimal), inclusive.

Quando `obase` é maior que 10, os numerais compreendem os numerais decimais de 0 até 9
e letras maiúsulas do alfabeto A, B, C, ..., quando necessário.
Os numerais para a base 35, a maior base aceitável,
compreendem de 0 até 9, e de A até Y.


Veja também `ibase`.

<!-- category: Other -->
<!-- keywords: outchar -->
<!-- signatures: outchar -->
### Variable: outchar

Valor padrão: `%o`


`outchar` é o prefixo dos rótulos de expressões calculadas pelo Maxima.
Maxima automaticamente constrói um rótulo para cada expressão calculada
pela concatenação de `outchar` e `linenum`.
A `outchar` pode ser atribuído qualquer sequência de caracteres ou símbolo, não necessáriamente um caractere simples.



```maxima
(%i1) outchar: "output";
(output1)                           output
(%i2) expand ((a+b)^3);
                            3        2      2      3
(output2)                  b  + 3 a b  + 3 a  b + a
(%i3)
```


Veja também `labels`.

<!-- category: Other -->
<!-- keywords: packagefile -->
<!-- signatures: packagefile -->
### Variable: packagefile

Valor padrão: `false`


Projetistas de pacotes que usam `save`
ou `translate` para criar pacotes (arquivos) para outros
usarem podem querer escolher `packagefile: true` para prevenir qu informações
sejam acrescentadas à lista de informações do Maxima (e.g. `values`,
`funções`) exceto onde necessário quando o arquivo é carregado.
Nesse caminho, o conteúdo do pacote não pegará no
caminho do usuário quando ele adicionar seus próprios dados.  Note que isso não
resolve o problema de possíveis conflitos de nome.  Também note que
o sinalizador simplesmente afeta o que é saída para o arquivo pacote.
Escolhendo o sinalizador para `true` é também útil para criar arquivos de
init do Maxima.

<!-- category: Other -->
<!-- keywords: pfeformat -->
<!-- signatures: pfeformat -->
### Variable: pfeformat

Valor padrão: `false`


Quando `pfeformat` é `true`, uma razão de inteiros é
mostrada com o caractere sólido (barra normal),
e um denominador inteiro `n`
é mostrado como um termo multiplicativo em primeiro lugar `1/n`.



```maxima
(%i1) pfeformat: false$
(%i2) 2^16/7^3;
                              65536
(%o2)                         -----
                               343
(%i3) (a+b)/8;
                              b + a
(%o3)                         -----
                                8
(%i4) pfeformat: true$ 
(%i5) 2^16/7^3;
(%o5)                       65536/343
(%i6) (a+b)/8;
(%o6)                      1/8 (b + a)
```

<!-- category: Other -->
<!-- keywords: print -->
<!-- signatures: print(expr_1, ..., expr_n) -->
### Function: print (expr_1, ..., expr_n)

Avalia e mostra *expr_1*, ..., *expr_n*
uma após a outra, da esquerda para a direita,
iniciando no lado esquerdo do console.


O valor retornado por `print` é o valor de seu último argumento.
`print` não gera rótulos de expressão intermediária.


Veja também `display`, `disp`, `ldisplay`, e `ldisp`.
Essas funções mostram uma expressão por linha, enquanto `print` tenta
mostrar duas ou mais expressões por linha.


Para mostrar o conteúdo de um arquivo, veja `printfile`.



```maxima
(%i1) r: print ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is", radcan (log (a^10/b)))$
            3        2      2      3
(a+b)^3 is b  + 3 a b  + 3 a  b + a  log (a^10/b) is 

                                              10 log(a) - log(b) 
(%i2) r;
(%o2)                  10 log(a) - log(b)
(%i3) disp ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is", radcan (log (a^10/b)))$
                           (a+b)^3 is

                     3        2      2      3
                    b  + 3 a b  + 3 a  b + a

                         log (a^10/b) is

                       10 log(a) - log(b)
```

<!-- category: Other -->
<!-- keywords: read -->
<!-- signatures: read(expr_1, ..., expr_n) -->
### Function: read (expr_1, ..., expr_n)

Imprime *expr_1*, ..., *expr_n*, então lê uma expressão do console
e retorna a expressão avaliada.
A expressão é terminada com um ponto e vírgula `;` ou o sinal de dólar `$`.


Veja também `readonly`.



```maxima
(%i1) foo: 42$ 
(%i2) foo: read ("foo is", foo, " -- enter new value.")$
foo is 42  -- enter new value.  
(a+b)^3;
(%i3) foo;
                                     3
(%o3)                         (b + a)
```

<!-- category: Other -->
<!-- keywords: readonly -->
<!-- signatures: readonly(expr_1, ..., expr_n) -->
### Function: readonly (expr_1, ..., expr_n)

Imprime *expr_1*, ..., *expr_n*, então lê uma expressão do console
e retorna a expressão (sem avaliação).
A expressão é terminada com um `;` (ponto e vírgula) ou `$` (sinal de dólar).



```maxima
(%i1) aa: 7$
(%i2) foo: readonly ("Forneça uma expressão:");
Enter an expressão: 
2^aa;
                                  aa
(%o2)                            2
(%i3) foo: read ("Forneça uma expressão:");
Enter an expressão: 
2^aa;
(%o3)                            128
```


Veja também `read`.

<!-- category: Other -->
<!-- keywords: reveal -->
<!-- signatures: reveal(expr, depth) -->
### Function: reveal (expr, depth)

Substitue partes de *expr* no inteiro especificado *depth*
com sumário descritivo.



- *
Somas e diferenças são substituídas por `sum(n)`
onde *n* é o número de operandos do produto.
- *
Produtos são substituídos por `product(n)`
onde *n* é o número de operandos da multiplicação.
- *
Exponenciais são substituídos por `expt`.
- *
Quocientes são substituídos por `quotient`.
- *
Negação unária é substituída por `negterm`.


Quando *depth* é maior que ou igual à máxima intensidade de *expr*,
`reveal (expr, depth)` retornam *expr* sem modificações.


`reveal` avalia seus argumentos.
`reveal` retorna expressão sumarizada.


Exemplo:



```maxima
(%i1) e: expand ((a - b)^2)/expand ((exp(a) + exp(b))^2);
                          2            2
                         b  - 2 a b + a
(%o1)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
(%i2) reveal (e, 1);
(%o2)                       quotient
(%i3) reveal (e, 2);
                             sum(3)
(%o3)                        ------
                             sum(3)
(%i4) reveal (e, 3);
                     expt + negterm + expt
(%o4)               ------------------------
                    product(2) + expt + expt
(%i5) reveal (e, 4);
                       2                 2
                      b  - product(3) + a
(%o5)         ------------------------------------
                         product(2)     product(2)
              2 expt + %e           + %e
(%i6) reveal (e, 5);
                         2            2
                        b  - 2 a b + a
(%o6)              --------------------------
                       sum(2)     2 b     2 a
                   2 %e       + %e    + %e
(%i7) reveal (e, 6);
                          2            2
                         b  - 2 a b + a
(%o7)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
```

<!-- category: Other -->
<!-- keywords: rmxchar -->
<!-- signatures: rmxchar -->
### Variable: rmxchar

Valor padrão: `]`


`rmxchar` é the caractere desenhado lado direito de uma matriz.


Veja também `lmxchar`.

<!-- category: Other -->
<!-- keywords: save -->
<!-- signatures: save(nomearquivo, nome_1, nome_2, nome_3, ...), save(nomearquivo, values, functions, labels, ...), save(nomearquivo, [m, n]), save(nomearquivo, nome_1=expr_1, ...), save(nomearquivo, all), save(nomearquivo, nome_1=expr_1, nome_2=expr_2, ...) -->
### Function: save (nomearquivo, nome_1, nome_2, nome_3, ...)

Armazena os valores correntes de *nome_1*, *nome_2*, *nome_3*, ..., em *nomearquivo*.
Os argumentos são os nomes das variáveis, funções, ou outros objetos.
Se um nome não possui valore ou função associada a ele, esse nome sem nenhum valor ou função associado será ignorado.
`save` retorna *nomearquivo*.


`save` armazena dados na forma de expressões Lisp.
Os dados armazenados por `save` podem ser recuperados por `load (nomearquivo)`.


O sinalizador global `file_output_append` governa
se `save` anexa ao final ou trunca o arquivo de saída.
Quando `file_output_append` for `true`,
`save` anexa ao final doarquivo de saída.
De outra forma, `save` trunca o arquivo de saída.
Nesse caso, `save` cria o arquivo se ele não existir ainda.


A forma especial `save (nomearquivo, values, functions, labels, ...)`
armazena os ítens nomeados por `values`, `funções`, `labels`, etc.
Os nomes podem ser quaisquer especificados pela variável `infolists`.
`values` compreende todas as variáveis definidas pelo usuário.


A forma especial `save (nomearquivo, [m, n])` armazena os valores de
rótulos de entrada e saída de *m* até *n*.
Note que *m* e *n* devem obrigatóriamente ser inteiros literais.
Rótulos de entrada e saída podem também ser armazenados um a um, e.g., `save ("foo.1", %i42, %o42)`.
`save (nomearquivo, labels)` armazena todos os rótulos de entrada e saída.
Quando rótulos armazenados são recuperados, eles substituem rótulos existentes.


A forma especial `save (nomearquivo, nome_1=expr_1, nome_2=expr_2, ...)`
armazena os valores de *expr_1*, *expr_2*, ...,
com nomes *nome_1*, *nome_2*, ....
Isso é útil para aplicar essa forma para rótulos de entrada e saída, e.g., `save ("foo.1", aa=%o88)`.
O lado direito dessa igualdade nessa forma pode ser qualquer expressão, que é avaliada.
Essa forma não introduz os novos nomes no ambiente corrente do Maxima,
mas somente armazena-os em *nomearquivo*.


Essa forma especial e a forma geral de `save` podem ser misturados.
Por exemplo, `save (nomearquivo, aa, bb, cc=42, funções, [11, 17])`.


A forma especial `save (nomearquivo, all)` armazena o estado corrente do Maxima.
Isso inclui todas as variáveis definidas pelo usuário, funções, arrays, etc., bem como
alguns ítens definidos automaticamente.
Os ítes salvos incluem variáveis de sistema,
tais como `file_search_maxima` ou `showtime`, se a elas tiverem sido atribuídos novos valores pelo usuário;
veja `myoptions`.


`save` avalia *nomearquivo* e não avalia todos os outros argumentos.

<!-- category: Other -->
<!-- keywords: savedef -->
<!-- signatures: savedef -->
### Variable: savedef

Valor padrão: `true`


Quando `savedef` é `true`, a vesão Maxima de uma
função de usuário é preservada quando a função é traduzida.
Isso permite que a definição seja mostrada por `dispfun` e autoriza a função a
ser editada.


Quando `savedef` é `false`, os nomes de funções traduzidas são
removidos da lista de `funções`.

<!-- category: Other -->
<!-- keywords: sconcat -->
<!-- signatures: sconcat(arg_1, arg_2, ...) -->
### Function: sconcat (arg_1, arg_2, ...)

Concatena seus argumentos em uma sequência de caracteres.
Ao contrário de `concat`, os argumentos arrumados *não* precisam ser atômicos.


O resultado é uma sequência de caracteres no format do Lisp.




```maxima
(%i1) sconcat ("xx[", 3, "]:", expand ((x+y)^3));
(%o1)               xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
```

<!-- category: Other -->
<!-- keywords: show -->
<!-- signatures: show(expr) -->
### Function: show (expr)

Mostra `expr` com os objetos indexados
tendo índices covariantes como subscritos, índices contravariantes como
sobrescritos.  Os índices derivativos são mostrados como subscritos,
separados dos índices covariantes por uma vírgula.

<!-- category: Other -->
<!-- keywords: showratvars -->
<!-- signatures: showratvars(expr) -->
### Function: showratvars (expr)

Retorna uma lista de variáveis expressão racional canônica (CRE) na expressão `expr`.


Veja também `ratvars`.

<!-- category: Other -->
<!-- keywords: stardisp -->
<!-- signatures: stardisp -->
### Variable: stardisp

Valor padrão: `false`


Quando `stardisp` é `true`, multiplicação é
mostrada com um asterisco `*` entre os operandos.

<!-- category: Other -->
<!-- keywords: string -->
<!-- signatures: string(expr) -->
### Function: string (expr)

Converte `expr` para a notação linear do Maxima
apenas como se tivesse sido digitada.


O valor de retorno de `string` é uma sequência de caracteres,
e dessa forma não pode ser usada em um cálculo.

<!-- category: Other -->
<!-- keywords: stringdisp -->
<!-- signatures: stringdisp -->
### Variable: stringdisp

Valor padrão: `false`


Quando `stringdisp` for `true`,
sequências de caracteres serão mostradas contidas em aspas duplas.
De outra forma,
aspas não são mostradas.


`stringdisp` é sempre `true` quando mostrando na tela uma definição de função.


Exemplos:










```maxima
(%i1) stringdisp: false$
(%i2) "This is an example string.";
(%o2)              This is an example string.
(%i3) foo () := print ("This is a string in a function definition.");
(%o3) foo() := 
              print("This is a string in a function definition.")
(%i4) stringdisp: true$
(%i5) "This is an example string.";
(%o5)             "This is an example string."
```

<!-- category: Other -->
<!-- keywords: stringout -->
<!-- signatures: stringout(nomearquivo, expr_1, expr_2, expr_3, ...), stringout(nomearquivo, [m, n]), stringout(nomearquivo, input), stringout(nomearquivo, functions), stringout(nomearquivo, values) -->
### Function: stringout (nomearquivo, expr_1, expr_2, expr_3, ...)

`stringout` escreve expressões para um arquivo na mesma forma de
expressões que foram digitadas para entrada.  O arquivo pode então ser usado
como entrada para comandos `batch` ou `demo`, e isso pode ser editado para
qualquer propósito.  `stringout` pode ser executado enquanto `writefile` está em progresso.


O sinalizador global `file_output_append` governa
se `stringout` anexa ao final ou trunca o arquivo de saída.
Quando `file_output_append` for `true`,
`stringout` anexa ao final do arquivo de sada.
De outra forma, `stringout` trunca o arquivo de saída.
Nesse caso, `stringout` cria o arquivo de saída se ele não existir ainda.


A forma geral de `stringout` escreve os valores de um ou mais 
expressões para o arquivo de saída.  Note que se uma expressão é uma
variável, somente o valor da variável é escrito e não o nome
da variável.  Como um útil caso especial, as expressões podem ser
rótulos de entrada (`%i1`, `%i2`, `%i3`, ...) ou rótulos de saída (`%o1`, `%o2`, `%o3`, ...).


Se `grind` é `true`, `stringout` formata a saída usando o formato 
`grind`.  De outra forma o formato `string` é usado.  Veja `grind` e `string`.


A forma especial `stringout (nomearquivo, [m, n])` escreve os
valores dos rótulos de entrada de m até n, inclusive.  


A forma especial `stringout (nomearquivo, input)` escreve todos
os rótulos de entrada para o arquivo.


A forma especial `stringout (nomearquivo, functions)` escreve todas
as funções definidas pelo usuário (nomeadas pela lista global `functions`) para o arquivo.


A forma especial `stringout (nomearquivo, values)` escreve todas as
variáveis atribuídas pelo usuário (nomeadas pela lista global `values`)
para o arquivo.  Cada variável é impressa como uma
declaração de atribuição, com o nome da variável seguida de dois pontos, e seu
valor.  Note que a forma geral de `stringout` não imprime 
variáveis como declarações de atribuição.

<!-- category: Other -->
<!-- keywords: system -->
<!-- signatures: system(comando) -->
### Function: system (comando)

Executa *comando* como um processo separado.
O comando é passado ao shell padrão para execução.
`system` não é suportado por todos os sistemas
operacionais, mas geralmente existe em ambientes Unix e Unix-like.


Supondo que `_hist.out`
é uma lista de frequência que você deseja imprimir como um gráfico em barras
usando `xgraph`.  



```maxima
(%i1) (with_stdout("_hist.out",
           for i:1 thru length(hist) do (
             print(i,hist[i]))),
       system("xgraph -bar -brw .7 -nl < _hist.out"));
```


Com o objetivo de fazer com que a impressão do gráfico seja concluída em segundo plano (retornando o controle para o Maxima)
e remover o arquivo temporário após isso ter sido concluído faça:



```maxima
system("(xgraph -bar -brw .7 -nl < _hist.out;  rm -f _hist.out)&")
```

<!-- category: Other -->
<!-- keywords: tcl_output -->
<!-- signatures: tcl_output(list, i0, skip), tcl_output(list, i0), tcl_output([list_1, ..., list_n], i) -->
### Function: tcl_output (list, i0, skip)

Imprime os elementos de uma lista entre chaves `{ }`,
conveniente como parte de um programa na linguagem Tcl/Tk.


`tcl_output (list, i0, skip)`
imprime *list*, começando com o elemento *i0* e imprimindo elementos
`i0 + skip`, `i0 + 2 skip`, etc.


`tcl_output (list, i0)`
é equivalente a `tcl_output (list, i0, 2)`.


`tcl_output ([list_1, ..., list_n], i)`
imprime os *i*’ésimos elementos de *list_1*, ..., *list_n*.


Exemplos:













```maxima
(%i1) tcl_output ([1, 2, 3, 4, 5, 6], 1, 3)$

 {1.000000000     4.000000000     
 }
(%i2) tcl_output ([1, 2, 3, 4, 5, 6], 2, 3)$

 {2.000000000     5.000000000     
 }
(%i3) tcl_output ([3/7, 5/9, 11/13, 13/17], 1)$

 {((RAT SIMP) 3 7) ((RAT SIMP) 11 13) 
 }
(%i4) tcl_output ([x1, y1, x2, y2, x3, y3], 2)$

 {$Y1 $Y2 $Y3 
 }
(%i5) tcl_output ([[1, 2, 3], [11, 22, 33]], 1)$

 {SIMP 1.000000000     11.00000000     
 }
```

<!-- category: Other -->
<!-- keywords: tex -->
<!-- signatures: tex(expr), tex(rótulo), tex(expr, momearquivo), tex(label, nomearquivo) -->
### Function: tex (expr)

Imprime uma representação de uma expressão
adequada para o sistema TeX  de preparação de documento.
O resultado é um fragmento de um documento,
que pode ser copiado dentro de um documento maior
Esse fragmento não pode ser processado de forma direta e isolada.


`tex (expr)` imprime uma representação TeX da *expr* no console.


`tex (rótulo)` imprime uma representação TeX de uma expressão chamada *rótulo*
e atribui a essa um rótulo de equação (a ser mostrado à esquerda da expressão).
O rótulo de equação TeX é o mesmo que o rótulo da equação no Maxima.


`tex (expr, nomearquivo)` anexa ao final uma representação TeX de *expr*
no arquivo *nomearquivo*.


`tex (rótulo, nomearquivo)` anexa ao final uma representação TeX da
expressão chamada de *rótulo*, com um rótulo de equação, ao arquivo *nomearquivo*.


`tex` avalia seu primeiro argumento após testar esse argumento para ver se é um rótulo.
duplo apóstrofo `''` força a avaliação do argumento, desse modo frustrando o teste
e prevenindo o rótulo.


Veja também `texput`.


Exemplos:



```maxima
(%i1) integrate (1/(1+x^3), x);
                                    2 x - 1
                  2            atan(-------)
             log(x  - x + 1)        sqrt(3)    log(x + 1)
(%o1)      - --------------- + ------------- + ----------
                    6             sqrt(3)          3
(%i2) tex (%o1);
$$-{{\log \left(x^2-x+1\right)}\over{6}}+{{\arctan \left({{2\,x-1
 }\over{\sqrt{3}}}\right)}\over{\sqrt{3}}}+{{\log \left(x+1\right)
 }\over{3}}\leqno{\tt (\%o1)}$$
(%o2)                          (\%o1)
(%i3) tex (integrate (sin(x), x));
$$-\cos x$$
(%o3)                           false
(%i4) tex (%o1, "foo.tex");
(%o4)                          (\%o1)
```

<!-- category: Other -->
<!-- keywords: texput -->
<!-- signatures: texput(a, s), texput(a, s, operator_type), texput(a, [s_1, s_2], matchfix), texput(a, [s_1, s_2, s_3], matchfix) -->
### Function: texput (a, s)

Atribui a saída TeX para o átomo *a*,
que pode ser um símbolo ou o nome de um operador.


`texput (a, s)` faz com que a função `tex`
interpole a sequência de caracteres *s* dentro da saída TeX em lugar de *a*.


`texput (a, s, operator_type)`,
onde *operator_type* é `prefix`, `infix`, `postfix`, `nary`, ou `nofix`,
faz com que a função `tex` interpole *s* dentro da saída TeX em lugar de *a*,
e coloca o texto interpolado na posição apropriada.


`texput (a, [s_1, s_2], matchfix)`
faz com que a função `tex` interpole *s_1* e *s_2* dentro da saída TeX
sobre qualquer lado dos argumentos de *a*.
Os argumentos (se mais de um) são separados por vírgulas.


`texput (a, [s_1, s_2, s_3], matchfix)`
faz com que a função `tex` interpole *s_1* e *s_2* dentro da saída TeX
sobre qualquer lado dos argumentos de *a*,
com *s_3* separando os argumentos.


Exemplos:


Atribui saída TeX a uma variável.







```maxima
(%i1) texput (me,"\\mu_e");
(%o1)                         \mu_e
(%i2) tex (me);
$$\mu_e$$
(%o2)                         false
```


Atribui saída TeX a uma função comum (não a um operador).







```maxima
(%i1) texput (lcm, "\\mathrm{lcm}");
(%o1)                     \mathrm{lcm}
(%i2) tex (lcm (a, b));
$$\mathrm{lcm}\left(a , b\right)$$
(%o2)                         false
```


Atribui saída TeX a um operador prefixado.








```maxima
(%i1) prefix ("grad");
(%o1)                         grad
(%i2) texput ("grad", " \\nabla ", prefix);
(%o2)                        \nabla 
(%i3) tex (grad f);
$$ \nabla f$$
(%o3)                         false
```


Atribui saída TeX a um operador infixado.








```maxima
(%i1) infix ("~");
(%o1)                           ~
(%i2) texput ("~", " \\times ", infix);
(%o2)                        \times 
(%i3) tex (a ~ b);
$$a \times b$$
(%o3)                         false
```


Atribui saída TeX a um operadro pósfixado.








```maxima
(%i1) postfix ("##");
(%o1)                          ##
(%i2) texput ("##", "!!", postfix);
(%o2)                          !!
(%i3) tex (x ##);
$$x!!$$
(%o3)                         false
```


Atribui saída TeX a um operador n-ário.








```maxima
(%i1) nary ("@@");
(%o1)                          @@
(%i2) texput ("@@", " \\circ ", nary);
(%o2)                         \circ 
(%i3) tex (a @@ b @@ c @@ d);
$$a \circ b \circ c \circ d$$
(%o3)                         false
```


Atribui saída TeX a um operador nofix.








```maxima
(%i1) nofix ("foo");
(%o1)                          foo
(%i2) texput ("foo", "\\mathsc{foo}", nofix);
(%o2)                     \mathsc{foo}
(%i3) tex (foo);
$$\mathsc{foo}$$
(%o3)                         false
```


Atribui saída TeX a um operadro matchfix.












```maxima
(%i1) matchfix ("<<", ">>");
(%o1)                          <<
(%i2) texput ("<<", [" \\langle ", " \\rangle "], matchfix);
(%o2)                [ \langle ,  \rangle ]
(%i3) tex (<<a>>);
$$ \langle a \rangle $$
(%o3)                         false
(%i4) tex (<<a, b>>);
$$ \langle a , b \rangle $$
(%o4)                         false
(%i5) texput ("<<", [" \\langle ", " \\rangle ", " \\, | \\,"], matchfix);
(%o5)           [ \langle ,  \rangle ,  \, | \,]
(%i6) tex (<<a>>);
$$ \langle a \rangle $$
(%o6)                         false
(%i7) tex (<<a, b>>);
$$ \langle a \, | \,b \rangle $$
(%o7)                         false
```

<!-- category: Other -->
<!-- keywords: ttyoff -->
<!-- signatures: ttyoff -->
### Variable: ttyoff

Valor padrão: `false`


Quando `ttyoff` é `true`, expressões de saída não são mostradas.
Expressões de saída são ainda calculadas e atribuídas rótulos.  Veja `labels`.


Textos impresso por funções internas do Maxima, tais como mensagens de erro e a saída de `describe`,
não são afetadas por `ttyoff`.

<!-- category: Other -->
<!-- keywords: with_stdout -->
<!-- signatures: with_stdout(nomearquivo, expr_1, expr_2, expr_3, ...) -->
### Function: with_stdout (nomearquivo, expr_1, expr_2, expr_3, ...)

Abre *nomearquivo* e então avalia *expr_1*, *expr_2*, *expr_3*, ....
Os valores dos argumentos não são armazenados em *nomearquivo*,
mas qualquer saída impressa gerada pela avaliação dos argumentos
(de `print`, `display`, `disp`, ou `grind`, por exemplo)
vai para *nomearquivo* em lugar do console.


O sinalizador global `file_output_append` governa
se `with_stdout` anexa ao final ou trunca o arquivo de saída.
Quando `file_output_append` for `true`,
`with_stdout` anexa ao final do arquivo de saída.
De outra forma, `with_stdout` trunca o arquivo de saída.
Nesse caso, `with_stdout` cria o arquivo se ele não existir ainda.


`with_stdout` retorna o valor do seu argumento final.


Veja também `writefile`.








```maxima
(%i1) with_stdout ("tmp.out", for i:5 thru 10 do print (i, "! yields", i!))$
(%i2) printfile ("tmp.out")$
5 ! yields 120 
6 ! yields 720 
7 ! yields 5040 
8 ! yields 40320 
9 ! yields 362880 
10 ! yields 3628800
```

<!-- category: Other -->
<!-- keywords: writefile -->
<!-- signatures: writefile(nomearquivo) -->
### Function: writefile (nomearquivo)

Começa escrevendo uma transcrição da sessão Maxima para *nomearquivo*.
Toda interação entre o usuário e Maxima é então gravada nesse arquivo,

da mesma forma que aparece no console.


Como a transcrição é impressa no formato de saída do console,
isso não pode ser reaproveitado pelo Maxima.
Para fazer um arquivo contendo expressões que podem ser reaproveitadas,
veja `save` e `stringout`.
`save` armazena expressões no formato Lisp, enquanto `stringout` armazena expressões no formato Maxima.


O efeito de executar `writefile` quando *nomearquivo* ainda existe
depende da implementação Lisp subjacente;
o arquivo transcrito pode ser substituído, ou o arquivo pode receber um anexo.
`appendfile` sempre anexa para o arquivo transcrito.


Isso pode ser conveniente para executar `playback` após
`writefile` para salvar a visualização de interações prévias.
Como `playback` mostra somente as variáveis de entrada e saída (`%i1`, `%o1`, etc.),
qualquer saída gerada por uma declaração de impressão em uma função
(como oposição a um valor de retorno) não é mostrada por `playback`.


`closefile` fecha o arquivo transcrito aberto por `writefile` ou `appendfile`.

