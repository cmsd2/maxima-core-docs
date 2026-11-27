## Listas

<!-- category: Programming -->
<!-- keywords: append -->
<!-- signatures: append(list_1, ..., list_n) -->
### Function: append (list_1, ..., list_n)

Retorna uma lista simples dos elementos de *list_1* seguidos
pelos elementos de *list_2*, ....  `append` também trabalha sobre
expressões gerais, e.g. `append (f(a,b), f(c,d,e));` retorna
`f(a,b,c,d,e)`.


Faça `example(append);` para um exemplo.

<!-- category: Programming -->
<!-- keywords: assoc -->
<!-- signatures: assoc(key, list, default), assoc(key, list) -->
### Function: assoc (key, list, default)

Essa função procura pela chave *key* do lado esquerdo da entrada *list*
que é da forma `[x,y,z,...]` onde cada elemento de *list* é uma expressão de
um operando binário e 2 elementos.  Por exemplo `x=1`, `2^3`, `[a,b]` etc.
A chave *key* é verificada contra o primeiro operando.  `assoc` retorna o segundo
operando se `key` for achada.  Se a chave `key` não for achada isso
retorna o valor padrão *default*.  *default* é opcional
e o padrão é `false`.

<!-- category: Programming -->
<!-- keywords: atom -->
<!-- signatures: atom(expr) -->
### Function: atom (expr)

Retorna `true` se *expr* for atomica (i.e. um número, nome ou sequência de caracteres) de outra forma retorna
`false`.  Desse modo `atom(5)` é `true` enquanto `atom(a[1])` e `atom(sin(x))` São
`false` (assumindo `a[1]` e `x` não estão associados).

<!-- category: Programming -->
<!-- keywords: cons -->
<!-- signatures: cons(expr, list) -->
### Function: cons (expr, list)

Retorna uma nova lista construída do elemento *expr* como
seu primeiro elemento, seguido por elementos de *list*.  `cons` também trabalha
sobre outras expressões, e.g. `cons(x, f(a,b,c));`  ->  `f(x,a,b,c)`.

<!-- category: Programming -->
<!-- keywords: copylist -->
<!-- signatures: copylist(list) -->
### Function: copylist (list)

Retorna uma cópia da lista *list*.

<!-- category: Programming -->
<!-- keywords: create_list -->
<!-- signatures: create_list(form, x_1, list_1, ..., x_n, list_n) -->
### Function: create_list (form, x_1, list_1, ..., x_n, list_n)

Cria uma lista por avaliação de *form* com *x_1* associando a
cada elemento *list_1*, e para cada tal associação anexa *x_2*
para cada elemento de *list_2*, ....
O número de elementos no resultado será
o produto do número de elementos de cada lista.
Cada variável *x_i* pode atualmente ser um síbolo –o qual não pode ser avaliado.
A lista de argumentos será avaliada uma única vez no início do bloco de 
repetição.  



```maxima
(%i82) create_list1(x^i,i,[1,3,7]);
(%o82) [x,x^3,x^7]
```



Com um bloco de repetição duplo:



```maxima
(%i79) create_list([i,j],i,[a,b],j,[e,f,h]);
(%o79) [[a,e],[a,f],[a,h],[b,e],[b,f],[b,h]]
```


Em lugar de *list_i* dois argumentos podem ser fornecidos cada um dos quais será
avaliado como um número.   Esses podem vir a ser inclusive o limite inferior e
superior do bloco de repetição.   



```maxima
(%i81) create_list([i,j],i,[1,2,3],j,1,i);
(%o81) [[1,1],[2,1],[2,2],[3,1],[3,2],[3,3]]
```


Note que os limites ou lista para a variável `j` podem
depender do valor corrente de `i`.

<!-- category: Programming -->
<!-- keywords: delete -->
<!-- signatures: delete(expr_1, expr_2), delete(expr_1, expr_2, n) -->
### Function: delete (expr_1, expr_2)

Remove todas as ocorrências de *expr_1* em *expr_2*. *expr_1*
pode ser uma parcela de *expr_2* (se isso for uma adição) ou um fator de *expr_2*
(se isso for um produto).






```maxima
(%i1) delete(sin(x), x+sin(x)+y);
(%o1)                         y + x
```


`delete(expr_1, expr_2, n)` remove as primeiras *n* ocorrências de
*expr_1* em *expr_2*.  Se houver menos que *n*
ocorrências de *expr_1* em *expr_2* então todas as corrências seram excluídas.







```maxima
(%i1) delete(a, f(a,b,c,d,a));
(%o1)                      f(b, c, d)
(%i2) delete(a, f(a,b,a,c,d,a), 2);
(%o2)                     f(b, c, d, a)
```

<!-- category: Programming -->
<!-- keywords: eighth -->
<!-- signatures: eighth(expr) -->
### Function: eighth (expr)

Retorna o oitavo item de uma expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: endcons -->
<!-- signatures: endcons(expr, list) -->
### Function: endcons (expr, list)

Retorna uma nova lista consistindo de elementos de
`list` seguidos por *expr*.  `endcons` também trabalha  sobre expressões gerais, e.g.
`endcons(x, f(a,b,c));`  ->  `f(a,b,c,x)`.

<!-- category: Programming -->
<!-- keywords: fifth -->
<!-- signatures: fifth(expr) -->
### Function: fifth (expr)

Retorna o quinto item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: first -->
<!-- signatures: first(expr) -->
### Function: first (expr)

Retorna a primeira parte de *expr* que pode resultar no primeiro
elemento de uma lista, a primeira linha de uma matriz, a primeira parcela de uma adição,
etc.  Note que `first` e suas funções relacionadas, `rest` e `last`, trabalham
sobre a forma de *expr* que é mostrada não da forma que é digitada na
entrada.  Se a variável `inflag` é escolhida para `true` todavia, essa
funções olharão  na forma interna de *expr*.  Note que o
simplificador re-ordena expressões.  Desse modo `first(x+y)` será `x` se `inflag`
for `true` e `y` se `inflag` for `false` (`first(y+x)` fornece os mesmos
resultados).  As funções `second` .. `tenth` retornam da segunda até a
décima parte do seu argumento.

<!-- category: Programming -->
<!-- keywords: fourth -->
<!-- signatures: fourth(expr) -->
### Function: fourth (expr)

Retorna o quarto item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: get -->
<!-- signatures: get(a, i) -->
### Function: get (a, i)

Recupera a propriedade de usuário indicada por *i* associada com
o átomo *a* ou retorna `false` se "a" não tem a propriedade *i*.


`get` avalia seus argumentos.


















```maxima
(%i1) put (%e, 'transcendental, 'type);
(%o1)                    transcendental
(%i2) put (%pi, 'transcendental, 'type)$
(%i3) put (%i, 'algebraic, 'type)$
(%i4) typeof (expr) := block ([q],
        if numberp (expr)
        then return ('algebraic),
        if not atom (expr)
        then return (maplist ('typeof, expr)),
        q: get (expr, 'type),
        if q=false
        then errcatch (error(expr,"is not numeric.")) else q)$
(%i5) typeof (2*%e + x*%pi);
x is not numeric.
(%o5)  [[transcendental, []], [algebraic, transcendental]]
(%i6) typeof (2*%e + %pi);
(%o6)     [transcendental, [algebraic, transcendental]]
```

<!-- category: Programming -->
<!-- keywords: join -->
<!-- signatures: join(l, m) -->
### Function: join (l, m)

Cria uma nova lista contendo os elementos das lista *l* e *m*, intercaladas.
O resultado tem os elementos `[l[1], m[1], l[2], m[2], ...]`.
As listas *l* e *m* podem conter qualquer tipo de elementos.


Se as listas forem de diferentes comprimentos, `join` ignora elementos da lista mais longa.


Maxima reclama se *l* ou *m* não for uma lista.


Exemplos:








```maxima
(%i1) L1: [a, sin(b), c!, d - 1];
(%o1)                [a, sin(b), c!, d - 1]
(%i2) join (L1, [1, 2, 3, 4]);
(%o2)          [a, 1, sin(b), 2, c!, 3, d - 1, 4]
(%i3) join (L1, [aa, bb, cc, dd, ee, ff]);
(%o3)        [a, aa, sin(b), bb, c!, cc, d - 1, dd]
```

<!-- category: Programming -->
<!-- keywords: last -->
<!-- signatures: last(expr) -->
### Function: last (expr)

Retorna a última parte (parcela, linha, elemento, etc.) de *expr*.

<!-- category: Programming -->
<!-- keywords: length -->
<!-- signatures: length(expr) -->
### Function: length (expr)

Retorna (por padrão) o número de partes na forma
externa (mostrada) de *expr*.  Para listas isso é o número de elementos,
para matrizes isso é o número de linhas, e para adições isso é o número
de parcelas (veja `dispform`).


O comando `length` é afetado pelo comutador
`inflag`.  Então, e.g. `length(a/(b*c));` retorna 2 se
`inflag` for `false` (Assumindo `exptdispflag` sendo `true`), mas 3 se `inflag` for
`true` (A representação interna é essencialmente `a*b^-1*c^-1`).

<!-- category: Programming -->
<!-- keywords: listarith -->
<!-- signatures: listarith -->
### Variable: listarith

Valor padrão: `true` - se `false` faz com que quaisquer operações aritméticas
com listas sejam suprimidas; quando `true`, operações lista-matriz são
contagiosas fazendo com que listas sejam convertidas para matrizes retornando um resultado
que é sempre uma matriz.  Todavia, operações lista-lista podem retornar
listas.

<!-- category: Programming -->
<!-- keywords: listp -->
<!-- signatures: listp(expr) -->
### Function: listp (expr)

Retorna `true` se *expr* for uma lista de outra forma retorna `false`.

<!-- category: Programming -->
<!-- keywords: makelist -->
<!-- signatures: makelist(expr, i, i_0, i_1), makelist(expr, x, list) -->
### Function: makelist (expr, i, i_0, i_1)

Constrói e retorna uma lista,
cada elemento dessa lista é gerado usando *expr*.


`makelist (expr, i, i_0, i_1)` retorna uma lista,
o `j`’ésimo elemento dessa lista é igual a `ev (expr, i=j)`
para `j` variando de *i_0* até *i_1*.


`makelist (expr, x, list)` retorna uma lista,
o `j`’ésimo elemento é igual a `ev (expr, x=list[j])`
para `j` variando de 1 até `length (list)`.


Exemplos:







```maxima
(%i1) makelist(concat(x,i),i,1,6);
(%o1)               [x1, x2, x3, x4, x5, x6]
(%i2) makelist(x=y,y,[a,b,c]);
(%o2)                 [x = a, x = b, x = c]
```

<!-- category: Programming -->
<!-- keywords: member -->
<!-- signatures: member(expr_1, expr_2) -->
### Function: member (expr_1, expr_2)

Retorna `true` se `is(expr_1 = a)`
para algum elemento *a* em `args(expr_2)`,
de outra forma retorna `false`.


`expr_2` é tipicamente uma lista,
nesse caso `args(expr_2) = expr_2`
e `is(expr_1 = a)` para algum elemento *a* em `expr_2` é o teste.


`member` não inspeciona partes dos argumentos de `expr_2`,
então `member` pode retornar `false` mesmo se `expr_1` for uma parte de algum argumento de `expr_2`.


Veja também `elementp`.


Exemplos:













```maxima
(%i1) member (8, [8, 8.0, 8b0]);
(%o1)                         true
(%i2) member (8, [8.0, 8b0]);
(%o2)                         false
(%i3) member (b, [a, b, c]);
(%o3)                         true
(%i4) member (b, [[a, b], [b, c]]);
(%o4)                         false
(%i5) member ([b, c], [[a, b], [b, c]]);
(%o5)                         true
(%i6) F (1, 1/2, 1/4, 1/8);
                               1  1  1
(%o6)                     F(1, -, -, -)
                               2  4  8
(%i7) member (1/8, %);
(%o7)                         true
(%i8) member ("ab", ["aa", "ab", sin(1), a + b]);
(%o8)                         true
```

<!-- category: Programming -->
<!-- keywords: ninth -->
<!-- signatures: ninth(expr) -->
### Function: ninth (expr)

Retorna o nono item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: rest -->
<!-- signatures: rest(expr, n), rest(expr) -->
### Function: rest (expr, n)

Retorna *expr* com seus primeiros *n* elementos removidos se *n* for
positivo e seus últimos `- n` elementos removidos se *n* for negativo.  Se *n* for 1
isso pode ser omitido.  *expr* pode ser uma lista, matriz, ou outra expressão.

<!-- category: Programming -->
<!-- keywords: reverse -->
<!-- signatures: reverse(list) -->
### Function: reverse (list)

Ordem reversa para os membros de *list* (não
os membros em si mesmos).  `reverse` também trabalha sobre expressões gerais,
e.g.  `reverse(a=b);` fornece `b=a`.

<!-- category: Programming -->
<!-- keywords: second -->
<!-- signatures: second(expr) -->
### Function: second (expr)

Retorna o segundo item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: seventh -->
<!-- signatures: seventh(expr) -->
### Function: seventh (expr)

Retorna o sétimo item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: sixth -->
<!-- signatures: sixth(expr) -->
### Function: sixth (expr)

Retorna o sexto item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: sublist_indices -->
<!-- signatures: sublist_indices(L, P) -->
### Function: sublist_indices (L, P)

Retorna os índices dos elementos `x` da lista *L* para os quais
o predicado `maybe(P(x))` retornar `true`;
isso inclui `unknown` bem como `false`.
*P* pode ser um nome de função ou uma expressão lambda.
*L* deve ser uma lista literal.


Exemplos:











```maxima
(%i1) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b], lambda ([x], x='b));
(%o1)                     [2, 3, 7, 9]
(%i2) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b], symbolp);
(%o2)                  [1, 2, 3, 4, 7, 9]
(%i3) sublist_indices ([1 > 0, 1 < 0, 2 < 1, 2 > 1, 2 > 0], identity);
(%o3)                       [1, 4, 5]
(%i4) assume (x < -1);
(%o4)                       [x < - 1]
(%i5) map (maybe, [x > 0, x < 0, x < -2]);
(%o5)                [false, true, unknown]
(%i6) sublist_indices ([x > 0, x < 0, x < -2], identity);
(%o6)                          [2]
```

<!-- category: Programming -->
<!-- keywords: tenth -->
<!-- signatures: tenth(expr) -->
### Function: tenth (expr)

Retorna o décimo item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

<!-- category: Programming -->
<!-- keywords: third -->
<!-- signatures: third(expr) -->
### Function: third (expr)

Retorna o terceiro item da expressão ou lista *expr*.
Veja `first` para maiores detalhes.

