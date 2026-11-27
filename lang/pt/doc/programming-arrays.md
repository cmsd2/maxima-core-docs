## Arrays

<!-- category: Programming -->
<!-- keywords: array -->
<!-- signatures: array(name, dim_1, ..., dim_n), array(name, type, dim_1, ..., dim_n), array([nome_1, ..., nome_m], dim_1, ..., dim_n) -->
### Function: array (name, dim_1, ..., dim_n)

Cria um array $n$-dimensional.  
$n$ pode ser menor ou igual a 5.
Os subscritos para
a $i$’ésima dimensão são inteiros no intervalo de 0 a *dim_i*.  


`array (name, dim_1, ..., dim_n)` cria um array genérico.


`array (name, type, dim_1, ..., dim_n)` cria
um array, com elementos de um tipo especificado.
*type* pode ser `fixnum` para
inteiros de tamanho limitado ou `flonum` para números em ponto flutuante.


`array ([nome_1, ..., nome_m], dim_1, ..., dim_n)`
cria $m$ arrays, todos da mesma dimensão.




Se o utilizador atribui a uma variável subscrita antes de declarar o
array correspondente, um array não declarado é criado.
Arrays não declarados, também conhecidos como array desordenado (porque
o codigo desordenado termina nos subscritos), são mais gerais que arrays
declarados.  O utilizador não declara seu tamanho máximo, e ele cresce
dinamicamente e desordenadamente à medida que são atribuídos valores a mais elementos.  Os
subscritos de um array não declarado não precisam sempre ser números.  Todavia,
excepto para um array um tanto quanto esparso, é provavelmente mais eficiente
declarar isso quando possível que deixar não declarado.  A função `array`
pode ser usada para transformar um array não declarado em um array
declarado.

<!-- category: Programming -->
<!-- keywords: arrayapply -->
<!-- signatures: arrayapply(A, [i_1, ..., i_n]) -->
### Function: arrayapply (A, [i_1, ..., i_n])

Avalia `A [i_1, ..., i_n]`,
quando *A* for um array e *i_1*, ..., *i_n* são inteiros.


Ela é remanescente de `apply`, excepto o primeiro argumento que é um array ao invés de uma função.

<!-- category: Programming -->
<!-- keywords: arrayinfo -->
<!-- signatures: arrayinfo(A) -->
### Function: arrayinfo (A)

Retorna informações sobre o array *A*.
O argumento *A* pode ser um array declarado, uma array não declarado ( que sofreu um hash),
uma função de array, ou uma função que possui subscrito.


Para arrays declarados, `arrayinfo` retorna uma lista
compreendendo o átomo `declared`, o n;umero de dimensões, e o tamanho de cada dimensão.
Os elementos do array, ambos associados e não associados, são retornados por `listarray`.


Para arrays não declarados (arrays que sofreram um hash),
`arrayinfo` retorna uma lista compreendendo o átomo `hashed`, o número de subscritos,
e os subscritos de de todo elemento que tiver um valor.
Os valores são retornados por meio de `listarray`.


Para funções de array,
`arrayinfo` retretorna uma lista compreendendo o átomo `hashed`, o número de subscritos,
e quaisquer valores de subscritos para os quais exista valores funcionais armazenados.
Os valores funcionais armazenados são retornados através de `listarray`.


Para funções que possuem subscritos,
`arrayinfo` retorna uma lista compreendendo o átomo `hashed`, o número de subscritos,
e qualquer valores subscritos para os quais existe uma expressões lambda.
As expressões lambda são retornadas por `listarray`.


Examples:


`arrayinfo` e `listarray` aplicado a um array declarado.










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa
(%i2) aa [2, 3] : %pi;
(%o2)                          %pi
(%i3) aa [1, 2] : %e;
(%o3)                          %e
(%i4) arrayinfo (aa);
(%o4)                 [declared, 2, [2, 3]]
(%i5) listarray (aa);
(%o5) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
```


`arrayinfo` e `listarray` aplicado a um array não declarado (no qual foi aplicado um hash).









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)
(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)
(%i3) arrayinfo (bb);
(%o3)               [hashed, 1, [BAR], [FOO]]
(%i4) listarray (bb);
                              3         2
(%o4)                 [(c - d) , (b + a) ]
```


`arrayinfo` e `listarray` aplicado a uma função de array.










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x
(%i2) cc [u, v];
                                v
(%o2)                           -
                                u
(%i3) cc [4, z];
                                z
(%o3)                           -
                                4
(%i4) arrayinfo (cc);
(%o4)              [hashed, 2, [4, z], [u, v]]
(%i5) listarray (cc);
                              z  v
(%o5)                        [-, -]
                              4  u
```


`arrayinfo` e `listarray` aplicadas a funções com subscritos.










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x
(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )
(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )
(%i4) arrayinfo (dd);
(%o4)             [hashed, 1, [b + a], [v - u]]
(%i5) listarray (dd);
                         b + a                v - u
(%o5)      [lambda([y], y     ), lambda([y], y     )]
```

<!-- category: Programming -->
<!-- keywords: arraymake -->
<!-- signatures: arraymake(A, [i_1, ..., i_n]) -->
### Function: arraymake (A, [i_1, ..., i_n])

Retorna a expressão `A[i_1, ..., i_n]`.
O resultado é uma referência a um array não avaliado.


`arraymake` é remanicência de `funmake`,
excepto o valor retornado é um array de referência não avaliado
ao invés de uma chamada de função não avaliada.


Exemplos:



















```maxima
(%i1) arraymake (A, [1]);
(%o1)                          A
                                1
(%i2) arraymake (A, [k]);
(%o2)                          A
                                k
(%i3) arraymake (A, [i, j, 3]);
(%o3)                       A
                             i, j, 3
(%i4) array (A, fixnum, 10);
(%o4)                           A
(%i5) fillarray (A, makelist (i^2, i, 1, 11));
(%o5)                           A
(%i6) arraymake (A, [5]); 
(%o6)                          A
                                5
(%i7) ''%;
(%o7)                          36
(%i8) L : [a, b, c, d, e];
(%o8)                    [a, b, c, d, e]
(%i9) arraymake ('L, [n]);
(%o9)                          L
                                n
(%i10) ''%, n = 3;
(%o10)                          c
(%i11) A2 : make_array (fixnum, 10);
(%o11)          {Array:  #(0 0 0 0 0 0 0 0 0 0)}
(%i12) fillarray (A2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o12)          {Array:  #(1 2 3 4 5 6 7 8 9 10)}
(%i13) arraymake ('A2, [8]);
(%o13)                         A2
                                 8
(%i14) ''%;
(%o14)                          9
```

<!-- category: Programming -->
<!-- keywords: arrays -->
<!-- signatures: arrays -->
### Variable: arrays

Valor por omissão: `[]`


`arrays` é uma lista dos arrays que tiverem sido alocados.
Essa lista compreende arrays declarados através de `array`,
arrays desordenados (hashed) construídos através de definição implícita (atribuindo alguma coisa a um elemento de array),
e funções de array definidas por meio de `:=` e `define`.
Arrays definidos por meio de `make_array` não estão incluídos.


Veja também
`array`, `arrayapply`, `arrayinfo`, `arraymake`, 
`fillarray`, `listarray`, e `rearray`.



Exemplos:










```maxima
(%i1) array (aa, 5, 7);
(%o1)                          aa
(%i2) bb [FOO] : (a + b)^2;
                                   2
(%o2)                       (b + a)
(%i3) cc [x] := x/100;
                                   x
(%o3)                      cc  := ---
                             x    100
(%i4) dd : make_array ('any, 7);
(%o4)       {Array:  #(NIL NIL NIL NIL NIL NIL NIL)}
(%i5) arrays;
(%o5)                     [aa, bb, cc]
```

<!-- category: Programming -->
<!-- keywords: bashindices -->
<!-- signatures: bashindices(expr) -->
### Function: bashindices (expr)

Transforma a expressão *expr* dando a cada
somatório e a cada produto um único índice.  Isso dá a `changevar` grande
precisão quando se está trabalhando com somatórios e produtos.  A forma do
único índice é `jnumber`.  A quantidade *number* é determindad por
referência a `gensumnum`, que pode ser alterada pelo utilizador.  Por
exemplo, `gensumnum:0$` reseta isso.

<!-- category: Programming -->
<!-- keywords: fillarray -->
<!-- signatures: fillarray(A, B) -->
### Function: fillarray (A, B)

Preenche o array *A* com *B*, que é uma lista ou um array.


Se um tipo específico for declarado para *A* no momento de sua criação,
*A* somente porde ser preenchido com elementos do tipo especificado;
Constitui um erro alguma tentativa feita para copiar um um elemento de um tipo diferente.

 

Se as dimensões dos arrays *A* e *B* forem
diferents, *A* é preenchido no ordem de maior fileira.  Se não existirem elementos
livres em *B* o último elemento é usado para preencher todo o 
resto de *A*.  Se existirem muitos , esses restantes seram ignorados.


`fillarray` retorna esse primeiro argumento.


Exemplos:


Create an array of 9 elements and fill it from a list.









```maxima
(%i1) array (a1, fixnum, 8);
(%o1)                          a1
(%i2) listarray (a1);
(%o2)              [0, 0, 0, 0, 0, 0, 0, 0, 0]
(%i3) fillarray (a1, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
(%o3)                          a1
(%i4) listarray (a1);
(%o4)              [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


Quando existirem poucos elementos para preencher o array,
o último elemento é repetido.
Quando houverem muitos elementos,
os elementos extras são ignorados.









```maxima
(%i1) a2 : make_array (fixnum, 8);
(%o1)             {Array:  #(0 0 0 0 0 0 0 0)}
(%i2) fillarray (a2, [1, 2, 3, 4, 5]);
(%o2)             {Array:  #(1 2 3 4 5 5 5 5)}
(%i3) fillarray (a2, [4]);
(%o3)             {Array:  #(4 4 4 4 4 4 4 4)}
(%i4) fillarray (a2, makelist (i, i, 1, 100));
(%o4)             {Array:  #(1 2 3 4 5 6 7 8)}
```


Arrays multi-dimensionais são preenchidos em ordem de maior fileira.









```maxima
(%i1) a3 : make_array (fixnum, 2, 5);
(%o1)        {Array:  #2A((0 0 0 0 0) (0 0 0 0 0))}
(%i2) fillarray (a3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o2)        {Array:  #2A((1 2 3 4 5) (6 7 8 9 10))}
(%i3) a4 : make_array (fixnum, 5, 2);
(%o3)     {Array:  #2A((0 0) (0 0) (0 0) (0 0) (0 0))}
(%i4) fillarray (a4, a3);
(%o4)     {Array:  #2A((1 2) (3 4) (5 6) (7 8) (9 10))}
```

<!-- category: Programming -->
<!-- keywords: listarray -->
<!-- signatures: listarray(A) -->
### Function: listarray (A)

Retorna uma lista dos elementos do array *A*.
O argumento *A* pode ser um array declarado, um array não declarado (desordenado - hashed),
uma função de array, ou uma função com subscritos.


Elementos são listados em ordem de linha maior.
Isto é, elementos são ordenados conforme o primeiro índice, en seguida conforme o segundo índice, e assim sucessivamente.
A sequuência de ordenação por meio dos valores dos índices é a mesma ordem estabelecida por meio de `orderless`.


Para arrays não declarados , funções de arrays, e funções com subscritos,
os elementos correspondem aos valores de índice retornados através de `arrayinfo`.


Elemetos não associados de arrays genéricos declarados (isto é, não `fixnum` e não `flonum`)
são retornados como `#####`.
Elementos não associados de arrays declarados `fixnum` ou `flonum`
são retornados como 0 ou 0.0, respectivamente.
Elementos não associados de arrays não declarados, funções de array,
e funções subscritas não são retornados.


Exemplos:


`listarray` e `arrayinfo` aplicados a um array declarado.










```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa
(%i2) aa [2, 3] : %pi;
(%o2)                          %pi
(%i3) aa [1, 2] : %e;
(%o3)                          %e
(%i4) listarray (aa);
(%o4) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
(%i5) arrayinfo (aa);
(%o5)                 [declared, 2, [2, 3]]
```


`listarray` e `arrayinfo` aplicadas a arrays não declarados (hashed - desordenados).









```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)
(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)
(%i3) listarray (bb);
                              3         2
(%o3)                 [(c - d) , (b + a) ]
(%i4) arrayinfo (bb);
(%o4)               [hashed, 1, [BAR], [FOO]]
```


`listarray` e `arrayinfo` aplicada a uma função de array.










```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x
(%i2) cc [u, v];
                                v
(%o2)                           -
                                u
(%i3) cc [4, z];
                                z
(%o3)                           -
                                4
(%i4) listarray (cc);
                              z  v
(%o4)                        [-, -]
                              4  u
(%i5) arrayinfo (cc);
(%o5)              [hashed, 2, [4, z], [u, v]]
```


`listarray` e `arrayinfo` aplicadas a funções com subscritos.










```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x
(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )
(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )
(%i4) listarray (dd);
                         b + a                v - u
(%o4)      [lambda([y], y     ), lambda([y], y     )]
(%i5) arrayinfo (dd);
(%o5)             [hashed, 1, [b + a], [v - u]]
```

<!-- category: Programming -->
<!-- keywords: make_array -->
<!-- signatures: make_array(type, dim_1, ..., dim_n) -->
### Function: make_array (type, dim_1, ..., dim_n)

Cria e retorna um array de Lisp.  *type* pode
ser `any`, `flonum`, `fixnum`, `hashed` ou
`functional`.
Existem $n$ indices,
e o $i$’enésimo indice está no intervalo de 0 a $dim_i - 1$.


A vantagem de `make_array` sobre `array` é que o valor de retorno não tem 
um nome, e uma vez que um ponteiro a ele vai, ele irá também.
Por exemplo, se `y: make_array (...)` então `y` aponta para um objecto 
que ocupa espaço, mas depois de `y: false`, `y` não mais
aponta para aquele objecto, então o objecto pode ser descartado.  












Exemplos:

















```maxima
(%i1) A1 : make_array (fixnum, 10);
(%o1)           {Array:  #(0 0 0 0 0 0 0 0 0 0)}
(%i2) A1 [8] : 1729;
(%o2)                         1729
(%i3) A1;
(%o3)          {Array:  #(0 0 0 0 0 0 0 0 1729 0)}
(%i4) A2 : make_array (flonum, 10);
(%o4) {Array:  #(0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}
(%i5) A2 [2] : 2.718281828;
(%o5)                      2.718281828
(%i6) A2;
(%o6) 
     {Array:  #(0.0 0.0 2.718281828 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}
(%i7) A3 : make_array (any, 10);
(%o7) {Array:  #(NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL)}
(%i8) A3 [4] : x - y - z;
(%o8)                      - z - y + x
(%i9) A3;
(%o9) {Array:  #(NIL NIL NIL NIL ((MPLUS SIMP) $X ((MTIMES SIMP)\
 -1 $Y) ((MTIMES SIMP) -1 $Z))
  NIL NIL NIL NIL NIL)}
(%i10) A4 : make_array (fixnum, 2, 3, 5);
(%o10) {Array:  #3A(((0 0 0 0 0) (0 0 0 0 0) (0 0 0 0 0)) ((0 0 \
0 0 0) (0 0 0 0 0) (0 0 0 0 0)))}
(%i11) fillarray (A4, makelist (i, i, 1, 2*3*5));
(%o11) {Array:  #3A(((1 2 3 4 5) (6 7 8 9 10) (11 12 13 14 15))
    ((16 17 18 19 20) (21 22 23 24 25) (26 27 28 29 30)))}
(%i12) A4 [0, 2, 1];
(%o12)                         12
```

<!-- category: Programming -->
<!-- keywords: rearray -->
<!-- signatures: rearray(A, dim_1, ..., dim_n) -->
### Function: rearray (A, dim_1, ..., dim_n)

Altera as dimenções de um array.  
O novo array será preenchido com os elementos do antigo em
ordem da maior linha.  Se o array antigo era muito pequeno, 
os elementos restantes serão preenchidos com
`false`, `0.0` ou `0`,
dependendo do tipo do array.  O tipo do array não pode ser
alterado.

<!-- category: Programming -->
<!-- keywords: remarray -->
<!-- signatures: remarray(A_1, ..., A_n), remarray(all) -->
### Function: remarray (A_1, ..., A_n)

Remove arrays e funções associadas
a arrays e libera o espaço ocupado.
Os argumentos podem ser arrays declarados, arrays não declarados (dsordenados - hashed), funções de array functions, e funções com subscritos.


`remarray (all)` remove todos os ítens na lista global `arrays`.



Isso pode ser necessário para usar essa função se isso é
desejado para redefinir os valores em um array desordenado.


`remarray` retorna a lista dos arrays removidos.

<!-- category: Programming -->
<!-- keywords: subvar -->
<!-- signatures: subvar(x, i) -->
### Function: subvar (x, i)

Avalia a expressão subscrita `x[i]`.


`subvar` avalia seus argumentos.


`arraymake (x, [i]` constrói a expressão `x[i]`,
mas não a avalia.


Exemplos:












```maxima
(%i1) x : foo $
(%i2) i : 3 $

(%i3) subvar (x, i);
(%o3)                         foo
                                 3

(%i4) foo : [aa, bb, cc, dd, ee]$

(%i5) subvar (x, i);
(%o5)                          cc


(%i6) arraymake (x, [i]);
(%o6)                         foo
                                 3


(%i7) ''%;
(%o7)                          cc
```

<!-- category: Programming -->
<!-- keywords: use_fast_arrays -->
<!-- signatures: use_fast_arrays -->
### Variable: use_fast_arrays

- Se `true` somente dois tipos de arrays são reconhecidos.  


1) O array art-q (t no Lisp Comum) que pode ter muitas dimensões
indexadas por inteiros, e pode aceitar qualquer objecto do Lisp ou do Maxima como uma
entrada.  Para construir assim um array, insira `a:make_array(any,3,4);` 
então `a` terá como valor, um array com doze posições, e o 
índice é baseado em zero.


2) O array Hash_table que é o tipo padrão de array criado se um
faz `b[x+1]:y^2` (e `b` não é ainda um array, uma lista, ou uma
matriz – se isso ou um desses ocorrer um erro pode ser causado desde
`x+1` não poderá ser um subscrito válido para um array art-q, uma lista ou
uma matriz).  Esses índices (também conhecidos como chaves) podem ser quaisquer objectos.  
Isso somente pega uma chave por vez a cada vez (`b[x+1,u]:y` ignorará o `u`).  
A referência termina em `b[x+1] ==> y^2`.  Certamente a chave poe ser uma lista
, e.g.  `b[[x+1,u]]:y` poderá ser válido.  Isso é incompatível 
com os arrays antigos do Maxima, mas poupa recursos.


Uma vantagem de armazenar os arrays como valores de símbolos é que as
convenções usuais sobre variáveis locais de uma função aplicam-se a arrays
também.  O tipo Hash_table também usa menos recursos e é mais eficiente
que o velho tipo hashar do Maxima.  Para obter comportamento consistente em
códigos traduzidos e compilados posicione `translate_fast_arrays` para ser
`true`.

