## Matrizes e Álgebra Linear

<!-- category: LinearAlgebra -->
<!-- keywords: [, ] -->
<!-- signatures: ] -->
### Variable: [

`[` e `]` marcam o omeço e o fim, respectivamente, de uma lista.


`[` e `]` também envolvem os subscritos de
uma lista, array, array desordenado, ou função array.


Exemplos:



```maxima
(%i1) x: [a, b, c];
(%o1)                       [a, b, c]
(%i2) x[3];
(%o2)                           c
(%i3) array (y, fixnum, 3);
(%o3)                           y
(%i4) y[2]: %pi;
(%o4)                          %pi
(%i5) y[2];
(%o5)                          %pi
(%i6) z['foo]: 'bar;
(%o6)                          bar
(%i7) z['foo];
(%o7)                          bar
(%i8) g[k] := 1/(k^2+1);
                                  1
(%o8)                     g  := ------
                           k     2
                                k  + 1
(%i9) g[10];
                                1
(%o9)                          ---
                               101
```

<!-- category: LinearAlgebra -->
<!-- keywords: addcol -->
<!-- signatures: addcol(M, list_1, ..., list_n) -->
### Function: addcol (M, list_1, ..., list_n)

Anexa a(s) coluna(s) dadas por uma
ou mais listas (ou matrizes) sobre a matriz *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: addrow -->
<!-- signatures: addrow(M, list_1, ..., list_n) -->
### Function: addrow (M, list_1, ..., list_n)

Anexa a(s) linha(s) dadas por uma ou
mais listas (ou matrizes) sobre a matriz *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: adjoint -->
<!-- signatures: adjoint(M) -->
### Function: adjoint (M)

Retorna a matriz adjunta da matriz *M*.
A matriz adjunta é a transposta da matriz dos cofactores de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: augcoefmatrix -->
<!-- signatures: augcoefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: augcoefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

Retorna a matriz dos coeficientes
aumentada para as variáveis *x_1*, ..., *x_n* do sistema de equações lineares
*eqn_1*, ..., *eqn_m*.  Essa é a matriz dos coeficientes com uma coluna anexada para
os termos independentes em cada equação (i.e., esses termos não dependem de
*x_1*, ..., *x_n*).



```maxima
(%i1) m: [2*x - (a - 1)*y = 5*b, c + b*y + a*x = 0]$
(%i2) augcoefmatrix (m, [x, y]);
                       [ 2  1 - a  - 5 b ]
(%o2)                  [                 ]
                       [ a    b      c   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: charpoly -->
<!-- signatures: charpoly(M, x) -->
### Function: charpoly (M, x)

Retorna um polinómio característico para a matriz *M*
em relação à variável *x*.  Que é,
`determinant (M - diagmatrix (length (M), x))`.



```maxima
(%i1) a: matrix ([3, 1], [2, 4]);
                            [ 3  1 ]
(%o1)                       [      ]
                            [ 2  4 ]
(%i2) expand (charpoly (a, lambda));
                           2
(%o2)                lambda  - 7 lambda + 10
(%i3) (programmode: true, solve (%));
(%o3)               [lambda = 5, lambda = 2]
(%i4) matrix ([x1], [x2]);
                             [ x1 ]
(%o4)                        [    ]
                             [ x2 ]
(%i5) ev (a . % - lambda*%, %th(2)[1]);
                          [ x2 - 2 x1 ]
(%o5)                     [           ]
                          [ 2 x1 - x2 ]
(%i6) %[1, 1] = 0;
(%o6)                     x2 - 2 x1 = 0
(%i7) x2^2 + x1^2 = 1;
                            2     2
(%o7)                     x2  + x1  = 1
(%i8) solve ([%th(2), %], [x1, x2]);
                  1               2
(%o8) [[x1 = - -------, x2 = - -------], 
               sqrt(5)         sqrt(5)

                                             1             2
                                    [x1 = -------, x2 = -------]]
                                          sqrt(5)       sqrt(5)
```

<!-- category: LinearAlgebra -->
<!-- keywords: coefmatrix -->
<!-- signatures: coefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: coefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

Retorna a matriz dos coeficientes para as
variáveis *x_1*, ..., *x_n* do sistema de equações lineares
*eqn_1*, ..., *eqn_m*.



```maxima
(%i1) coefmatrix([2*x-(a-1)*y+5*b = 0, b*y+a*x = 3], [x,y]);
                                 [ 2  1 - a ]
(%o1)                            [          ]
                                 [ a    b   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: col -->
<!-- signatures: col(M, i) -->
### Function: col (M, i)

Reorna a *i*’ésima coluna da matriz *M*.
O valor de retorno é uma matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: columnvector, covect -->
<!-- signatures: columnvector(L), covect(L) -->
### Function: columnvector (L)

Retorna uma matriz de uma coluna e `length (L)` linhas,
contendo os elementos da lista *L*.


`covect` é um sinonimo para `columnvector`.


`load ("eigen")` chama essa função.



Isso é útil se quiser usar partes das saídas das
funções nesse pacote em cálculos matriciais.


Exemplo:





```maxima
(%i1) load ("eigen")$
Warning - you are redefining the Macsyma function autovalores
Warning - you are redefining the Macsyma function autovectores
(%i2) columnvector ([aa, bb, cc, dd]);
                             [ aa ]
                             [    ]
                             [ bb ]
(%o2)                        [    ]
                             [ cc ]
                             [    ]
                             [ dd ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: conjugate -->
<!-- signatures: conjugate(x) -->
### Function: conjugate (x)

Retorna o conjugado complexo de *x*.










```maxima
(%i1) declare ([aa, bb], real, cc, complex, ii, imaginary);

(%o1)                         done
(%i2) conjugate (aa + bb*%i);

(%o2)                      aa - %i bb
(%i3) conjugate (cc);

(%o3)                     conjugate(cc)
(%i4) conjugate (ii);

(%o4)                         - ii
(%i5) conjugate (xx + yy);

(%o5)             conjugate(yy) + conjugate(xx)
```

<!-- category: LinearAlgebra -->
<!-- keywords: copymatrix -->
<!-- signatures: copymatrix(M) -->
### Function: copymatrix (M)

Retorna uma cópia da matriz *M*.  Esse é o único
para fazer uma copia separada copiando *M* elemento a elemento.


Note que uma atribuição de uma matriz para outra, como em `m2: m1`,
não copia `m1`.
Uma atribuição `m2 [i,j]: x` ou `setelmx (x, i, j, m2` também modifica `m1 [i,j]`.
criando uma cópia com `copymatrix` e então usando atribução cria uma separada e modificada cópia.

<!-- category: LinearAlgebra -->
<!-- keywords: determinant -->
<!-- signatures: determinant(M) -->
### Function: determinant (M)

Calcula o determinante de *M* por um método similar à
eliminação de Gauss.



A forma do resultado depende da escolha
do comutador `ratmx`.



Existe uma rotina especial para calcular
determinantes esparsos que é chamada quando os comutadores
`ratmx` e `sparse` são ambos `true`.

<!-- category: LinearAlgebra -->
<!-- keywords: detout -->
<!-- signatures: detout -->
### Variable: detout

Valor por omissão: `false`


Quando `detout` é `true`, o determinante de uma
matriz cuja inversa é calculada é factorado fora da inversa.


Para esse comutador ter efeito `doallmxops` e `doscmxops` deveram ambos serem
`false` (veja suas transcrições).  Alternativamente esses comutadores podem ser
dados para `ev` o que faz com que os outros dois sejam escolhidos correctamente.


Exemplo:



```maxima
(%i1) m: matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) detout: true$
(%i3) doallmxops: false$
(%i4) doscmxops: false$
(%i5) invert (m);
                          [  d   - b ]
                          [          ]
                          [ - c   a  ]
(%o5)                     ------------
                           a d - b c
```

<!-- category: LinearAlgebra -->
<!-- keywords: diagmatrix -->
<!-- signatures: diagmatrix(n, x) -->
### Function: diagmatrix (n, x)

Retorna uma matriz diagonal de tamanho *n* por *n* com os
elementos da diagonal todos iguais a *x*.
`diagmatrix (n, 1)` retorna uma matriz identidade (o mesmo que `ident (n)`).


*n* deve avaliar para um inteiro, de outra forma `diagmatrix` reclama com uma mensagem de erro.


*x* pode ser qualquer tipo de expresão, incluindo outra matriz.
Se *x* é uma matriz, isso não é copiado; todos os elementos da diagonal referem-se à mesma instância, *x*.

<!-- category: LinearAlgebra -->
<!-- keywords: doallmxops -->
<!-- signatures: doallmxops -->
### Variable: doallmxops

Valor por omissão: `true`


Quando `doallmxops` é `true`,

todas as operações relacionadas a matrizes são realizadas.
Quando isso é `false` então a escolha de
comutadores individuais `dot` governam quais operações são executadas.

<!-- category: LinearAlgebra -->
<!-- keywords: domxexpt -->
<!-- signatures: domxexpt -->
### Variable: domxexpt

Valor por omissão: `true`


Quando `domxexpt` é `true`,
uma matriz exponencial, `exp (M)` onde *M* é a matriz,
é interpretada como uma matriz com elementos `[i,j` iguais a `exp (m[i,j])`.
de outra forma `exp (M)` avalia para `exp (ev(M)`.


`domxexpt`
afecta todas as expresões da forma `base^expoente` onde *base* é uma
expresão assumida escalar ou constante, e *expoente* é uma lista ou
matriz.


Exemplo:



```maxima
(%i1) m: matrix ([1, %i], [a+b, %pi]);
                         [   1    %i  ]
(%o1)                    [            ]
                         [ b + a  %pi ]
(%i2) domxexpt: false$
(%i3) (1 - c)^m;
                             [   1    %i  ]
                             [            ]
                             [ b + a  %pi ]
(%o3)                 (1 - c)
(%i4) domxexpt: true$
(%i5) (1 - c)^m;
                  [                      %i  ]
                  [    1 - c      (1 - c)    ]
(%o5)             [                          ]
                  [        b + a         %pi ]
                  [ (1 - c)       (1 - c)    ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: domxmxops -->
<!-- signatures: domxmxops -->
### Variable: domxmxops

Valor por omissão: `true`


Quando `domxmxops` é `true`, todas as operações matriz-matriz ou
matriz-lista são realizadas (mas não operações
escalar-matriz); se esse comutador é `false` tais operações não são.

<!-- category: LinearAlgebra -->
<!-- keywords: domxnctimes -->
<!-- signatures: domxnctimes -->
### Variable: domxnctimes

Valor por omissão: `false`


Quando `domxnctimes` é `true`, produtos não comutativos de
matrizes são realizados.

<!-- category: LinearAlgebra -->
<!-- keywords: dontfactor -->
<!-- signatures: dontfactor -->
### Variable: dontfactor

Valor por omissão: `[]`


`dontfactor` pode ser escolhido para uma lista de variáveis em relação
a qual factoração não é para ocorrer.  (A lista é inicialmente vazia.)
Factoração também não pegará lugares com relação a quaisquer variáveis que
são menos importantes, conforme a hierarquía de variável assumida para a forma expresão racional canónica (CRE),
que essas na lista `dontfactor`.

<!-- category: LinearAlgebra -->
<!-- keywords: doscmxops -->
<!-- signatures: doscmxops -->
### Variable: doscmxops

Valor por omissão: `false`


Quando `doscmxops` é `true`, operações escalar-matriz são
realizadas.

<!-- category: LinearAlgebra -->
<!-- keywords: doscmxplus -->
<!-- signatures: doscmxplus -->
### Variable: doscmxplus

Valor por omissão: `false`


Quando `doscmxplus` é `true`, operações escalar-matriz retornam
uma matriz resultado.  Esse comutador não é subsomado sob `doallmxops`.

<!-- category: LinearAlgebra -->
<!-- keywords: dot0nscsimp -->
<!-- signatures: dot0nscsimp -->
### Variable: dot0nscsimp

Valor por omissão: `true`



Quando `dot0nscsimp` é `true`, um produto não comutativo de zero
e um termo não escalar é simplificado para um produto comutativo.

<!-- category: LinearAlgebra -->
<!-- keywords: dot0simp -->
<!-- signatures: dot0simp -->
### Variable: dot0simp

Valor por omissão: `true`



Quando `dot0simp` é `true`,
um produto não comutativo de zero e
um termo escalar é simplificado para um produto não comutativo.

<!-- category: LinearAlgebra -->
<!-- keywords: dot1simp -->
<!-- signatures: dot1simp -->
### Variable: dot1simp

Valor por omissão: `true`



Quando `dot1simp` é `true`,
um produto não comutativo de um e
outro termo é simplificado para um produto comutativo.

<!-- category: LinearAlgebra -->
<!-- keywords: dotassoc -->
<!-- signatures: dotassoc -->
### Variable: dotassoc

Valor por omissão: `true`


Quando `dotassoc` é `true`, uma expresão `(A.B).C` simplifica para
`A.(B.C)`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotconstrules -->
<!-- signatures: dotconstrules -->
### Variable: dotconstrules

Valor por omissão: `true`


Quando `dotconstrules` é `true`, um produto não comutativo de uma
constante e outro termo é simplificado para um produto comutativo.

Ativando esse sinalizador efectivamente activamos `dot0simp`, `dot0nscsimp`, e
`dot1simp` também.

<!-- category: LinearAlgebra -->
<!-- keywords: dotdistrib -->
<!-- signatures: dotdistrib -->
### Variable: dotdistrib

Valor por omissão: `false`


Quando `dotdistrib` é `true`, uma expresão `A.(B + C)` simplifica para `A.B + A.C`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotexptsimp -->
<!-- signatures: dotexptsimp -->
### Variable: dotexptsimp

Valor por omissão: `true`


Quando `dotexptsimp` é `true`, uma expresão `A.A` simplifica para `A^^2`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotident -->
<!-- signatures: dotident -->
### Variable: dotident

Valor por omissão: 1


`dotident` é o valor retornado por `X^^0`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotscrules -->
<!-- signatures: dotscrules -->
### Variable: dotscrules

Valor por omissão: `false`


Quando `dotscrules` é `true`, uma expresão `A.SC` ou `SC.A` simplifica
para `SC*A` e `A.(SC*B)` simplifica para `SC*(A.B)`.

<!-- category: LinearAlgebra -->
<!-- keywords: echelon -->
<!-- signatures: echelon(M) -->
### Function: echelon (M)

Retorna a forma escalonada da matriz *M*,
como produzido através da eliminação de Gauss.
A forma escalonada é calculada de *M*
por operações elementares de linha tais que o primeiro
elemento não zero em cada linha na matriz resultante seja o número um e os
elementos da coluna abaixo do primeiro número um em cada linha sejam todos zero.


`triangularize` também realiza eliminação de Gaussian,
mas não normaliza o elemento líder não nulo em cada linha.


`lu_factor` e `cholesky` são outras funções que retornam matrizes triangularizadas.







```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) echelon (M);
                  [ 1  - 8  - 5      - 2     ]
                  [                          ]
                  [         28       11      ]
                  [ 0   1   --       --      ]
(%o2)             [         37       37      ]
                  [                          ]
                  [              37 bb - 119 ]
                  [ 0   0    1   ----------- ]
                  [              37 aa - 313 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: eigenvalues, eivals -->
<!-- signatures: eigenvalues(M), eivals(M) -->
### Function: eigenvalues (M)

Retorna uma lista de duas listas contendo os autovalores da matriz *M*.
A primeira sublista do valor de retorno é a lista de autovalores da
matriz, e a segunda sublista é a lista de
multiplicidade dos autovalores na ordem correspondente.


`eivals` é um sinonimo de `eigenvalues`.


`eigenvalues` chama a função `solve` para achar as raízes do
polinómio característico da matriz.
Algumas vezes `solve` pode não estar habilitado a achar as raízes do polinómio;
nesse caso algumas outras funções nesse
pacote (except `innerproduct`, `unitvector`, `columnvector` e
`gramschmidt`) não irão trabalhar.





Em alguns casos os autovalores achados por `solve` podem ser expresões complicadas.
(Isso pode acontecer quando `solve` retorna uma expresão real não trivial
para um autovalor que é sabidamente real.)
Isso pode ser possível para simplificar os autovalores usando algumas outras funções.



O pacote `eigen.mac` é chamado automaticamente quando
`eigenvalues` ou `eigenvectors` é referenciado.
Se `eigen.mac` não tiver sido ainda chamado,
`load ("eigen")` chama-o.
Após ser chamado, todas as funções e variáveis no pacote estarão disponíveis.

<!-- category: LinearAlgebra -->
<!-- keywords: eigenvectors, eivects -->
<!-- signatures: eigenvectors(M), eivects(M) -->
### Function: eigenvectors (M)

pegam uma matriz *M* como seu argumento e retorna uma lista
de listas cuja primeira sublista é a saída de `eigenvalues`
e as outras sublistas são os autovectores da
matriz correspondente para esses autovalores respectivamente.


`eivects` é um sinonimo para `eigenvectors`.


O pacote `eigen.mac` é chamado automaticamente quando
`eigenvalues` ou `eigenvectors` é referenciado.
Se `eigen.mac` não tiver sido ainda chamado,
`load ("eigen")` chama-o.
Após ser chamado, todas as funções e variáveis no pacote estarão disponíveis.


Os sinalizadores que afectam essa função são:


`nondiagonalizable` é escolhido para `true` ou `false` dependendo de
se a matriz é não diagonalizável ou diagonalizável após o
retorno de `eigenvectors`.


`hermitianmatrix` quando `true`, faz com que os autovectores
degenerados da matriz Hermitiana sejam ortogonalizados usando o
algoritmo de Gram-Schmidt.


`knowneigvals` quando `true` faz com que o pacote `eigen` assumir que os
autovalores da matriz são conhecidos para o utilizador e armazenados sob o
nome global `listeigvals`.  `listeigvals` poderá ser escolhido para uma lista similar
à saída de `eigenvalues`.


A função `algsys` é usada aqui para resolver em relação aos autovectores.  Algumas vezes se os
autovalores estão ausêntes, `algsys` pode não estar habilitado a achar uma solução.
Em alguns casos, isso pode ser possível para simplificar os autovalores por
primeiro achando e então usando o comando `eigenvalues` e então usando outras funções
para reduzir os autovalores a alguma coisa mais simples.
Continuando a simplificação, `eigenvectors` pode ser chamada novamente
com o sinalizador `knowneigvals` escolhido para `true`.

<!-- category: LinearAlgebra -->
<!-- keywords: ematrix -->
<!-- signatures: ematrix(m, n, x, i, j) -->
### Function: ematrix (m, n, x, i, j)

Retorna uma matriz *m* por *n*, todos os elementos da qual
são zero excepto para o elemento `[i, j]` que é *x*.

<!-- category: LinearAlgebra -->
<!-- keywords: entermatrix -->
<!-- signatures: entermatrix(m, n) -->
### Function: entermatrix (m, n)

Retorna uma matriz *m* por *n*, lendo os elementos interativamente.


Se *n* é igual a *m*,
Maxima pergunta pelo tipo de matriz (diagonal, simétrica, antisimétrica, ou genérica)
e por cada elemento.
Cada resposta é terminada por um ponto e vírgula `;` ou sinal de dólar `$`.


Se *n* não é igual a *m*,
Maxima pergunta por cada elemento.


Os elementos podem ser quaisquer expressões, que são avaliadas.
`entermatrix` avalia seus argumentos.



```maxima
(%i1) n: 3$
(%i2) m: entermatrix (n, n)$

Is the matriz  1.  Diagonal  2.  Symmetric  3.  Antisymmetric  4.  General
Answer 1, 2, 3 or 4 : 
1$
Row 1 Column 1: 
(a+b)^n$
Row 2 Column 2: 
(a+b)^(n+1)$
Row 3 Column 3: 
(a+b)^(n+2)$

Matriz entered.
(%i3) m;
                [        3                     ]
                [ (b + a)      0         0     ]
                [                              ]
(%o3)           [                  4           ]
                [    0      (b + a)      0     ]
                [                              ]
                [                            5 ]
                [    0         0      (b + a)  ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: genmatrix -->
<!-- signatures: genmatrix(a, i_2, j_2, i_1, j_1), genmatrix(a, i_2, j_2, i_1), genmatrix(a, i_2, j_2) -->
### Function: genmatrix (a, i_2, j_2, i_1, j_1)

Retorna uma matriz gerada de *a*,
pegando o elemento `a[i_1,j_1]`
como o elemento do canto superior esquerdo e `a[i_2,j_2]`
como o elemento do canto inferior directo da matriz.
Aqui *a* é um array declarado (criado através de `array` mas não por meio de `make_array`)
ou um array não declarado,
ou uma função array,
ou uma expressão lambda de dois argumentos.
(Uma funçãO array é criado como outras funções com `:=` ou `define`,
mas os argumentos são colocados entre colchêtes em lugar de parêntesis.)


Se *j_1* é omitido, isso é assumido ser igual a *i_1*.
Se ambos *j_1* e *i_1* são omitidos, ambos são assumidos iguais a 1.


Se um elemento seleccionado `i,j` de um array for indefinido,
a matriz conterá um elemento simbólico `a[i,j]`.


Exemplos:













```maxima
(%i1) h [i, j] := 1 / (i + j - 1);
                                    1
(%o1)                  h     := ---------
                        i, j    i + j - 1
(%i2) genmatrix (h, 3, 3);
                           [    1  1 ]
                           [ 1  -  - ]
                           [    2  3 ]
                           [         ]
                           [ 1  1  1 ]
(%o2)                      [ -  -  - ]
                           [ 2  3  4 ]
                           [         ]
                           [ 1  1  1 ]
                           [ -  -  - ]
                           [ 3  4  5 ]
(%i3) array (a, fixnum, 2, 2);
(%o3)                           a
(%i4) a [1, 1] : %e;
(%o4)                          %e
(%i5) a [2, 2] : %pi;
(%o5)                          %pi
(%i6) genmatrix (a, 2, 2);
                           [ %e   0  ]
(%o6)                      [         ]
                           [ 0   %pi ]
(%i7) genmatrix (lambda ([i, j], j - i), 3, 3);
                         [  0    1   2 ]
                         [             ]
(%o7)                    [ - 1   0   1 ]
                         [             ]
                         [ - 2  - 1  0 ]
(%i8) genmatrix (B, 2, 2);
                        [ B      B     ]
                        [  1, 1   1, 2 ]
(%o8)                   [              ]
                        [ B      B     ]
                        [  2, 1   2, 2 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: gramschmidt, gschmit -->
<!-- signatures: gramschmidt(x), gschmit(x) -->
### Function: gramschmidt (x)

Realiza o algoritmo de ortonalização de Gram-Schmidt sobre *x*,
seja ela uma matriz ou uma lista de listas.
*x* não é modificado por `gramschmidt`.


Se *x* é uma matriz, o algoritmo é aplicado para as linhas de *x*.
Se *x* é uma lista de listas, o algoritmo é aplicado às sublistas,
que devem ter igual números de elementos.
Nos dois casos,
o valor de retorno é uma lista de listas, as sublistas das listas são ortogonais
e gera o mesmo spaço que *x*.
Se a dimensão do conjunto gerador de *x* é menor que o número de linhas ou sublistas,
algumas sublistas do valor de retorno são zero.


`factor` é chamada a cada estágio do algoritmo para simplificar resultados intermédios.
Como uma consequência, o valor de retorno pode conter inteiros factorados.


`gschmit` (nota ortográfica) é um sinonimo para `gramschmidt`.


`load ("eigen")` chama essa função.


Exemplo:



```maxima
(%i1) load ("eigen")$
Warning - you are redefining the Macsyma function autovalores
Warning - you are redefining the Macsyma function autovectores
(%i2) x: matrix ([1, 2, 3], [9, 18, 30], [12, 48, 60]);
                         [ 1   2   3  ]
                         [            ]
(%o2)                    [ 9   18  30 ]
                         [            ]
                         [ 12  48  60 ]
(%i3) y: gramschmidt (x);
                       2      2            4     3
                      3      3   3 5      2  3  2  3
(%o3)  [[1, 2, 3], [- ---, - --, ---], [- ----, ----, 0]]
                      2 7    7   2 7       5     5
(%i4) i: innerproduct$
(%i5) [i (y[1], y[2]), i (y[2], y[3]), i (y[3], y[1])];
(%o5)                       [0, 0, 0]
```

<!-- category: LinearAlgebra -->
<!-- keywords: ident -->
<!-- signatures: ident(n) -->
### Function: ident (n)

Retorna uma matriz identidade *n* por *n*.

<!-- category: LinearAlgebra -->
<!-- keywords: innerproduct, inprod -->
<!-- signatures: innerproduct(x, y), inprod(x, y) -->
### Function: innerproduct (x, y)

Retorna o produto interno (também chamado produto escalar ou produto do ponto) de *x* e *y*,
que são listas de igual comprimento, ou ambas matrizes 1-coluna ou 1-linha de igual comprimento.
O valor de retorno é `conjugate (x) . y`,
onde `.` é o operador de multiplicação não comutativa.


`load ("eigen")` chama essa função.


`inprod` é um sinonimo para `innerproduct`.

<!-- category: LinearAlgebra -->
<!-- keywords: invert -->
<!-- signatures: invert(M) -->
### Function: invert (M)

Retorna a inversa da matriz *M*.
A inversa é calculada pelo método adjunto.


Isso permite a um utilizador calcular a inversa de uma matriz com
entradas bfloat ou polinómios com coeficientes em ponto flutuante sem
converter para a forma CRE.


Cofactores são calculados pela função  `determinant`,
então se `ratmx` é `false` a inversa é calculada
sem mudar a representação dos elementos.


A implementação
corrente é ineficiente para matrizes de alta ordem.


Quando `detout` é `true`, o determinante é factorado fora da
inversa.


Os elementos da inversa não são automaticamente expandidos.
Se *M* tem elementos polinomiais, melhor aparência de saída pode ser
gerada por `expand (invert (m)), detout`.
Se isso é desejável para ela
divisão até pelo determinante pode ser excelente por `xthru (%)`
ou alternativamente na unha por



```maxima
expe (adjoint (m)) / expand (determinant (m))
invert (m) := adjoint (m) / determinant (m)
```


Veja `^^` (expoente não comutativo) para outro método de inverter uma matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: lmxchar -->
<!-- signatures: lmxchar -->
### Variable: lmxchar

Valor por omissão: `[`


`lmxchar` é o caractere mostrado como o delimitador
esquerdo de uma matriz.
Veja também `rmxchar`.


Exemplo:



```maxima
(%i1) lmxchar: "|"$
(%i2) matrix ([a, b, c], [d, e, f], [g, h, i]);
                           | a  b  c ]
                           |         ]
(%o2)                      | d  e  f ]
                           |         ]
                           | g  h  i ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix -->
<!-- signatures: matrix(row_1, ..., row_n) -->
### Function: matrix (row_1, ..., row_n)

Retorna uma matriz retangular que tem as linhas *row_1*, ..., *row_n*.
Cada linha é uma lista de expressões.
Todas as linhas devem ter o mesmo comprimento.


As operações `+` (adição), `-` (subtração), `*` (multiplicação),
e `/` (divisão), são realizadas elemento por elemento
quando os operandos são duas matrizes, um escalar e uma matriz, ou uma matriz e um escalar.
A operação `^` (exponenciação, equivalentemente `**`)
é realizada elemento por elemento
se os operandos são um escalar e uma matriz ou uma matriz e um escalar,
mas não se os operandos forem duas matrizes.

Todos as operações são normalmente realizadas de forma completa,
incluindo `.` (multiplicação não comutativa).


Multiplicação de matrizes é representada pelo operador de multiplicação não comutativa `.`.
O correspondente operador de exponenciação não comutativa é `^^`.
Para uma matriz `A`, `A.A = A^^2` e
`A^^-1` é a inversa de *A*, se existir.


Existem comutadores para controlar a simplificação de expresões
envolvendo operações escalar e matriz-lista.
São eles
`doallmxops`, `domxexpt`
`domxmxops`, `doscmxops`, e `doscmxplus`.



Existem opções adicionais que são relacionadas a matrizes.  São elas:
`lmxchar`, `rmxchar`, `ratmx`, `listarith`, `detout`,
`scalarmatrix`,
e `sparse`.



Existe um número de
funções que pegam matrizes como argumentos ou devolvem matrizes como valor de retorno.
Veja `eigenvalues`, `eigenvectors`,
`determinant`,
`charpoly`, `genmatrix`, `addcol`, `addrow`, 
`copymatrix`, `transpose`, `echelon`,
e `rank`.



Exemplos:



- *
Construção de matrizes de listas.


```maxima
(%i1) x: matrix ([17, 3], [-8, 11]);
                           [ 17   3  ]
(%o1)                      [         ]
                           [ - 8  11 ]
(%i2) y: matrix ([%pi, %e], [a, b]);
                           [ %pi  %e ]
(%o2)                      [         ]
                           [  a   b  ]
```


- *
Adição, elemento por elemento.


```maxima
(%i3) x + y;
                      [ %pi + 17  %e + 3 ]
(%o3)                 [                  ]
                      [  a - 8    b + 11 ]
```


- *
Subtração, elemento por elemento.


```maxima
(%i4) x - y;
                      [ 17 - %pi  3 - %e ]
(%o4)                 [                  ]
                      [ - a - 8   11 - b ]
```


- *
Multiplicação, elemento por elemento.


```maxima
(%i5) x * y;
                        [ 17 %pi  3 %e ]
(%o5)                   [              ]
                        [ - 8 a   11 b ]
```


- *
Divisão, elemento por elemento.


```maxima
(%i6) x / y;
                        [ 17       - 1 ]
                        [ ---  3 %e    ]
                        [ %pi          ]
(%o6)                   [              ]
                        [   8    11    ]
                        [ - -    --    ]
                        [   a    b     ]
```


- *
Matriz para um expoente escalar, elemento por elemento.


```maxima
(%i7) x ^ 3;
                         [ 4913    27  ]
(%o7)                    [             ]
                         [ - 512  1331 ]
```


- *
Base escalar para um expoente matriz, elemento por elemento.


```maxima
(%i8) exp(y); 
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o8)                    [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
Base matriz para um expoente matriz.  Essa não é realizada elemento por elemento.


```maxima
(%i9) x ^ y;
                                [ %pi  %e ]
                                [         ]
                                [  a   b  ]
                     [ 17   3  ]
(%o9)                [         ]
                     [ - 8  11 ]
```


- *
Multiplicação não comutativa de matrizes.


```maxima
(%i10) x . y;
                  [ 3 a + 17 %pi  3 b + 17 %e ]
(%o10)            [                           ]
                  [ 11 a - 8 %pi  11 b - 8 %e ]
(%i11) y . x;
                [ 17 %pi - 8 %e  3 %pi + 11 %e ]
(%o11)          [                              ]
                [  17 a - 8 b     11 b + 3 a   ]
```


- *
Exponenciação não comutativa de matrizes.
Uma base escalar *b* para uma potência matriz *M*
é realizada elemento por elemento e então `b^^m` é o mesmo que `b^m`.


```maxima
(%i12) x ^^ 3;
                        [  3833   1719 ]
(%o12)                  [              ]
                        [ - 4584  395  ]
(%i13) %e ^^ y;
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o13)                   [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
A matriz elevada a um expoente -1 com exponenciação não comutativa é a matriz inversa,
se existir.


```maxima
(%i14) x ^^ -1;
                         [ 11      3  ]
                         [ ---  - --- ]
                         [ 211    211 ]
(%o14)                   [            ]
                         [  8    17   ]
                         [ ---   ---  ]
                         [ 211   211  ]
(%i15) x . (x ^^ -1);
                            [ 1  0 ]
(%o15)                      [      ]
                            [ 0  1 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_add -->
<!-- signatures: matrix_element_add -->
### Variable: matrix_element_add

Valor por omissão: `+`


`matrix_element_add` é a operação 
invocada em lugar da adição em uma multiplicação de matrizes.
A `matrix_element_add` pode ser atribuído qualquer operador n-ário
(que é, uma função que manuseia qualquer número de argumentos).
Os valores atribuídos podem ser o nome de um operador entre aspas duplas,
o nome da função,
ou uma expressão lambda.


Veja também `matrix_element_mult` e `matrix_element_transpose`.


Exemplo:



```maxima
(%i1) matrix_element_add: "*"$
(%i2) matrix_element_mult: "^"$
(%i3) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o3)                      [         ]
                           [ d  e  f ]
(%i4) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o4)                      [         ]
                           [ x  y  z ]
(%i5) aa . transpose (bb);
                     [  u  v  w   x  y  z ]
                     [ a  b  c   a  b  c  ]
(%o5)                [                    ]
                     [  u  v  w   x  y  z ]
                     [ d  e  f   d  e  f  ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_mult -->
<!-- signatures: matrix_element_mult -->
### Variable: matrix_element_mult

Valor por omissão: `*`


`matrix_element_mult` é a operação
invocada em lugar da multiplicação em uma multiplicação de matrizes.
A `matrix_element_mult` pode ser atribuído qualquer operador binário.
O valor atribuído pode ser o nome de um operador entre aspas duplas,
o nome de uma função,
ou uma expressão lambda.


O operador do ponto `.` é uma escolha útil em alguns contextos.


Veja também `matrix_element_add` e `matrix_element_transpose`.


Exemplo:



```maxima
(%i1) matrix_element_add: lambda ([[x]], sqrt (apply ("+", x)))$
(%i2) matrix_element_mult: lambda ([x, y], (x - y)^2)$
(%i3) [a, b, c] . [x, y, z];
                          2          2          2
(%o3)         sqrt((c - z)  + (b - y)  + (a - x) )
(%i4) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o4)                      [         ]
                           [ d  e  f ]
(%i5) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o5)                      [         ]
                           [ x  y  z ]
(%i6) aa . transpose (bb);
               [             2          2          2  ]
               [ sqrt((c - w)  + (b - v)  + (a - u) ) ]
(%o6)  Col 1 = [                                      ]
               [             2          2          2  ]
               [ sqrt((f - w)  + (e - v)  + (d - u) ) ]

                         [             2          2          2  ]
                         [ sqrt((c - z)  + (b - y)  + (a - x) ) ]
                 Col 2 = [                                      ]
                         [             2          2          2  ]
                         [ sqrt((f - z)  + (e - y)  + (d - x) ) ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_transpose -->
<!-- signatures: matrix_element_transpose -->
### Variable: matrix_element_transpose

Valor por omissão: `false`


`matrix_element_transpose` é a operação
aplicada a cada elemento de uma matriz quando for uma transposta.
A `matrix_element_mult` pode ser atribuído qualquer operador unário.
O valor atribuído pode ser  nome de um operador entre aspas duplas,
o nome de uma função,
ou uma expressão lambda.


Quando `matrix_element_transpose` for igual a `transpose`,
a função  `transpose` é aplicada a todo elemento.
Quando `matrix_element_transpose` for igual a `nonscalars`,
a função `transpose` é aplicada a todo elemento não escalar.
Se algum elemento é um átomo, a opção `nonscalars` aplica
`transpose` somente se o átomo for declarado não escalar,
enquanto a opção `transpose` sempre aplica `transpose`.


O valor padrão, `false`, significa nenhuma operação é aplicada.


Veja também `matrix_element_add` e `matrix_element_mult`.


Exemplos:



```maxima
(%i1) declare (a, nonscalar)$
(%i2) transpose ([a, b]);
                        [ transpose(a) ]
(%o2)                   [              ]
                        [      b       ]
(%i3) matrix_element_transpose: nonscalars$
(%i4) transpose ([a, b]);
                        [ transpose(a) ]
(%o4)                   [              ]
                        [      b       ]
(%i5) matrix_element_transpose: transpose$
(%i6) transpose ([a, b]);
                        [ transpose(a) ]
(%o6)                   [              ]
                        [ transpose(b) ]
(%i7) matrix_element_transpose: lambda ([x], realpart(x) - %i*imagpart(x))$
(%i8) m: matrix ([1 + 5*%i, 3 - 2*%i], [7*%i, 11]);
                     [ 5 %i + 1  3 - 2 %i ]
(%o8)                [                    ]
                     [   7 %i       11    ]
(%i9) transpose (m);
                      [ 1 - 5 %i  - 7 %i ]
(%o9)                 [                  ]
                      [ 2 %i + 3    11   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrixmap -->
<!-- signatures: matrixmap(f, M) -->
### Function: matrixmap (f, M)

Retorna uma matriz com elemento `i,j` igual a `f(M[i,j])`.


Veja também `map`, `fullmap`, `fullmapl`, e `apply`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrixp -->
<!-- signatures: matrixp(expr) -->
### Function: matrixp (expr)

Retorna `true` se *expr* é uma matriz, de outra forma retorna `false`.

<!-- category: LinearAlgebra -->
<!-- keywords: mattrace -->
<!-- signatures: mattrace(M) -->
### Function: mattrace (M)

Retorna o traço (que é, a soma dos elementos sobre a diagonal principal) da
matriz quadrada *M*.  


`mattrace` é chamada por `ncharpoly`,
uma alternativa para `charpoly` do Maxima.



`load ("nchrpl")` chama essa função.

<!-- category: LinearAlgebra -->
<!-- keywords: minor -->
<!-- signatures: minor(M, i, j) -->
### Function: minor (M, i, j)

Retorna o *i*, *j* menor do elemento localizado na linha *i* coluna *j* da matriz *M*.  Que é *M*
com linha *i* e coluna *j* ambas removidas.

<!-- category: LinearAlgebra -->
<!-- keywords: ncexpt -->
<!-- signatures: ncexpt(a, b) -->
### Function: ncexpt (a, b)

Se uma expressão exponencial não comutativa é muito
alta para ser mostrada como `a^^b` aparecerá como `ncexpt (a,b)`.


`ncexpt` não é o nome de uma função ou operador;
o nome somente aparece em saídas, e não é reconhecido em entradas.

<!-- category: LinearAlgebra -->
<!-- keywords: ncharpoly -->
<!-- signatures: ncharpoly(M, x) -->
### Function: ncharpoly (M, x)

Retorna o polinómio característico da matriz *M*
com relação a *x*.  Essa é uma alternativa para `charpoly` do Maxima.


`ncharpoly` trabalha pelo cálculo dos traços das potências na dada matriz,
que são sabidos serem iguais a somas de potências das raízes do
polinómio característico.  Para essas quantidade a função
simétrica das raízes pode ser calculada, que nada mais são que
os coeficientes do polinómio característico.  `charpoly` trabalha

formatando o determinante de `x * ident [n] - a`.  Dessa forma `ncharpoly` é vencedor,
por exemplo, no caso de largas e densas matrizes preencidas com inteiros,
desde que isso evite inteiramente a aritmética polinomial.


`load ("nchrpl")` loads this file.

<!-- category: LinearAlgebra -->
<!-- keywords: newdet -->
<!-- signatures: newdet(M, n) -->
### Function: newdet (M, n)

Calcula o determinante de uma matriz ou array *M* pelo
algoritmo da árvore menor de Johnson-Gentleman.

O argumento *n* é a ordem; isso é opcional se *M* for uma matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: nonscalar -->
<!-- signatures: nonscalar -->
### Variable: nonscalar

Faz átomos ser comportarem da mesma forma que uma lista ou matriz em relação ao
operador do ponto.

<!-- category: LinearAlgebra -->
<!-- keywords: nonscalarp -->
<!-- signatures: nonscalarp(expr) -->
### Function: nonscalarp (expr)

Retorna `true` se *expr* é um não escalar, i.e., isso contém
átomos declarados como não escalares, listas, ou matrizes.

<!-- category: LinearAlgebra -->
<!-- keywords: permanent -->
<!-- signatures: permanent(M, n) -->
### Function: permanent (M, n)

Calcula o permanente da matriz *M*.  Um permanente
é como um determinante mas sem mudança de sinal.

<!-- category: LinearAlgebra -->
<!-- keywords: rank -->
<!-- signatures: rank(M) -->
### Function: rank (M)

Calcula o posto da matriz *M*.  Que é, a ordem do
mais largo determinante não singular de *M*.



*rank* pode retornar uma
resposta ruim se não puder determinar que um elemento da matriz que é
equivalente a zero é realmente isso.

<!-- category: LinearAlgebra -->
<!-- keywords: ratmx -->
<!-- signatures: ratmx -->
### Variable: ratmx

Valor por omissão: `false`


Quando `ratmx` é `false`, adição, subtração,
e multiplicação para determinantes e matrizes são executados na
representação dos elementos da matriz e fazem com que o resultado da
inversão de matrizes seja esquerdo na representação geral.


Quando `ratmx` é `true`,
as 4 operações mencionadas acima são executadas na forma CRE e o
resultado da matriz inversa é dado na forma CRE.  Note isso pode
fazer com que os elementos sejam expandidos (dependendo da escolha de `ratfac`)
o que pode não ser desejado sempre.

<!-- category: LinearAlgebra -->
<!-- keywords: row -->
<!-- signatures: row(M, i) -->
### Function: row (M, i)

retorna a *i*’ésima linha da matriz *M*.
O valor de retorno é uma matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: scalarmatrixp -->
<!-- signatures: scalarmatrixp -->
### Variable: scalarmatrixp

Valor por omissão: `true`


Quando `scalarmatrixp` é `true`, então sempre que uma matriz 1 x 1
é produzida como um resultado de cálculos o produto do ponto de matrizes 
é simplificado para um escalar, a saber o elemento solitário da matriz.


Quando `scalarmatrixp` é `all`,
então todas as matrizes 1 x 1 serão simplificadas para escalares.


Quando `scalarmatrixp` é `false`, matrizes 1 x 1 não são simplificadas para escalares.

<!-- category: LinearAlgebra -->
<!-- keywords: scalefactors -->
<!-- signatures: scalefactors(coordinatetransform) -->
### Function: scalefactors (coordinatetransform)

Aqui coordinatetransform
avalia para a forma [[expresão1, expresão2, ...],
indeterminação1, indeterminação2, ...], onde indeterminação1,
indeterminação2, etc.  são as variáveis de coordenadas curvilíneas e
onde a escolha de componentes cartesianas retangulares é dada em termos das
coordenadas curvilíneas por [expresão1, expresão2, ...].
`coordinates` é escolhida para o vector [indeterminação1, indeterminação2,...],
e `dimension` é escolhida para o comprimento desse vector.  SF[1], SF[2],
..., SF[DIMENSION] são escohidos para factores de escala de coordenada, e `sfprod`
é escohido para o produto desse factores de escala.  Inicialmente, `coordinates`
é [X, Y, Z], `dimension` é 3, e SF[1]=SF[2]=SF[3]=SFPROD=1,
correspondendo a coordenadas Cartesianas retangulares 3-dimensional.
Para expandir uma expresão dentro de componentes físicos no sistema de coordenadas
corrente , existe uma função com uso da forma

<!-- category: LinearAlgebra -->
<!-- keywords: setelmx -->
<!-- signatures: setelmx(x, i, j, M) -->
### Function: setelmx (x, i, j, M)

Atribue *x* para o (*i*, *j*)’ésimo elemento da matriz *M*,
e retorna a matriz alterada.


`M [i, j]: x` tem o mesmo efeito,
mas retorna *x* em lugar de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: similaritytransform, simtran -->
<!-- signatures: similaritytransform(M), simtran(M) -->
### Function: similaritytransform (M)

`similaritytransform` calcula uma transformação homotética da matriz `M`.
Isso retorna uma lista que é a saída do
comando `uniteigenvectors`.  Em adição se o sinalizador `nondiagonalizable`
é `false` duas matrizes globais `leftmatrix` e `rightmatrix` são calculadas.
Essas matrizes possuem a propriedade de
`leftmatrix . M . rightmatrix` é uma matriz diagonal com os autovalores
de *M* sobre a diagonal.  Se `nondiagonalizable` é `true` as matrizes esquerda e
direita não são computadas.


Se o sinalizador `hermitianmatrix` é `true`
então `leftmatrix` é o conjugado complexo da transposta de
`rightmatrix`.  De outra forma `leftmatrix` é a inversa de `rightmatrix`.


`rightmatrix` é a matriz cujas colunas são os autovectores
unitários de *M*.  Os outros sinalizadores (veja `eigenvalues` e
`eigenvectors`) possuem o mesmo efeito desde que
`similaritytransform` chama as outras funções no pacote com o objectivo de
estar habilitado para a forma `rightmatrix`.


`load ("eigen")` chama essa função.


`simtran` é um sinonimo para `similaritytransform`.

<!-- category: LinearAlgebra -->
<!-- keywords: sparse -->
<!-- signatures: sparse -->
### Variable: sparse

Valor por omissão: `false`


Quando `sparse` é `true`, e se `ratmx` é `true`, então `determinant`
usará rotinas especiais para calcular determinantes esparsos.

<!-- category: LinearAlgebra -->
<!-- keywords: submatrix -->
<!-- signatures: submatrix(i_1, ..., i_m, M, j_1, ..., j_n), submatrix(i_1, ..., i_m, M), submatrix(M, j_1, ..., j_n) -->
### Function: submatrix (i_1, ..., i_m, M, j_1, ..., j_n)

Retorna uma nova matriz formada pela
matrix *M* com linhas *i_1*, ..., *i_m* excluídas, e colunas *j_1*, ..., *j_n* excluídas.

<!-- category: LinearAlgebra -->
<!-- keywords: transpose -->
<!-- signatures: transpose(M) -->
### Function: transpose (M)

Retorna a transposta de *M*.


Se *M* é uma matriz, o valor de retorno é outra matriz *N*
tal que `N[i,j] = M[j,i]`.


Se *M* for uma lista, o valor de retorno é uma matrix *N*
de `length (m)` linhas e 1 coluna, tal que `N[i,1] = M[i]`.


De outra forma *M* é um símbolo,
e o valor de retorno é uma expressão substantiva `'transpose (M)`.

<!-- category: LinearAlgebra -->
<!-- keywords: triangularize -->
<!-- signatures: triangularize(M) -->
### Function: triangularize (M)

Retorna a maior forma triangular da matriz `M`, como produzido através da eliminação de Gauss.
O valor de retorno é o mesmo que `echelon`,
excepto que o o coeficiente lider não nulo em cada linha não é normalizado para 1.


`lu_factor` e `cholesky` são outras funções que retornam matrizes triangularizadas.







```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) triangularize (M);
             [ - 1   8         5            2      ]
             [                                     ]
(%o2)        [  0   - 74     - 56         - 22     ]
             [                                     ]
             [  0    0    626 - 74 aa  238 - 74 bb ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: uniteigenvectors, ueivects -->
<!-- signatures: uniteigenvectors(M), ueivects(M) -->
### Function: uniteigenvectors (M)

Calcula autovectores unitários da matriz *M*.
O valor de retorno é uma lista de listas, a primeiro sublista é a
saída do comando `eigenvalues`, e as outras sublistas são
os autovectores unitários da matriz correspondente a esses autovalores
respectivamente.



Os sinalizadores mencionados na descrição do
comando `eigenvectors` possuem o mesmo efeito aqui também.


Quando `knowneigvects` é `true`, o pacote `eigen` assume
que os autovectores da matriz são conhecidos para o utilizador são
armazenados sob o nome global `listeigvects`.  `listeigvects` pode ser ecolhido
para uma lista similar à saída do comando `eigenvectors`.



Se `knowneigvects` é escolhido para `true` e a lista de autovectores é dada a
escolha do sinalizador `nondiagonalizable` pode não estar correcta.  Se esse é
o caso por favor ecolha isso para o valor correcto.  O autor assume que
o utilizador sabe o que está fazendo e que não tentará diagonalizar uma
matriz cujos autovectores não geram o mesmo espaço vectorial de
dimensão apropriada.


`load ("eigen")` chama essa função.


`ueivects` é um sinonimo para `uniteigenvectors`.

<!-- category: LinearAlgebra -->
<!-- keywords: unitvector, uvect -->
<!-- signatures: unitvector(x), uvect(x) -->
### Function: unitvector (x)

Retorna $x/norm(x)$;
isso é um vector unitário na mesma direção que *x*.


`load ("eigen")` chama essa função.


`uvect` é um sinonimo para `unitvector`.

<!-- category: LinearAlgebra -->
<!-- keywords: vect_cross -->
<!-- signatures: vect_cross -->
### Variable: vect_cross

Valor por omissão: `false`



Quando `vect_cross` é `true`, isso permite DIFF(X~Y,T) trabalhar onde
~ é definido em SHARE;VECT (onde VECT_CROSS é escolhido para `true`, de qualqeur modo.)

<!-- category: LinearAlgebra -->
<!-- keywords: vectorsimp -->
<!-- signatures: vectorsimp(expr) -->
### Function: vectorsimp (expr)

Aplica simplificações e expansões conforme
os seguintes sinalizadores globais:


`expandall`, `expanddot`, `expanddotplus`, `expandcross`, `expandcrossplus`,
`expandcrosscross`, `expandgrad`, `expandgradplus`, `expandgradprod`,
`expanddiv`, `expanddivplus`, `expanddivprod`, `expandcurl`, `expandcurlplus`,
`expandcurlcurl`, `expandlaplacian`, `expandlaplacianplus`,
e `expandlaplacianprod`.


Todos esses sinalizadores possuem valor padrão `false`.  O sufixo `plus` refere-se a
utilização aditivamente ou distribuitivamente.  O sufixo `prod` refere-se a
expansão para um operando que é qualquer tipo de produto.



**expandcrosscross** — Simplifica $p ~ (q ~ r)$ para $(p . r)*q - (p . q)*r$.
**expandcurlcurl** — Simplifica $curl curl p$ para $grad div p + div grad p$.
**expandlaplaciantodivgrad** — Simplifica $laplacian p$ para $div grad p$.
**expandcross** — Habilita `expandcrossplus` e `expandcrosscross`.
**expandplus** — Habilita `expanddotplus`, `expandcrossplus`, `expandgradplus`,
`expanddivplus`, `expandcurlplus`, e `expandlaplacianplus`.
**expandprod** — Habilita `expandgradprod`, `expanddivprod`, e `expandlaplacianprod`.



Esses sinalizadores foram todos declarados `evflag`.

<!-- category: LinearAlgebra -->
<!-- keywords: zeromatrix -->
<!-- signatures: zeromatrix(m, n) -->
### Function: zeromatrix (m, n)

Retorna um matriz *m* por *n*, com todos os elementos sendo zero.

