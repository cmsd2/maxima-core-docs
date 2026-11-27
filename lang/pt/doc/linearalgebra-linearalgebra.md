## linearalgebra

<!-- category: LinearAlgebra -->
<!-- keywords: addmatrices -->
<!-- signatures: addmatrices(f, M_1, ..., M_n) -->
### Function: addmatrices (f, M_1, ..., M_n)

Usando a função *f* como a função de adição, retorne a adição das
matrizes *M_1*, ..., *M_n*. A função *f* deve aceitar qualquer número de
argumentos (uma função enária do Maxima).


Exemplos:









```maxima
(%i1) m1 : matrix([1,2],[3,4])$
(%i2) m2 : matrix([7,8],[9,10])$
(%i3) addmatrices('max,m1,m2);
(%o3) matrix([7,8],[9,10])
(%i4) addmatrices('max,m1,m2,5*m1);
(%o4) matrix([7,10],[15,20])
```

<!-- category: LinearAlgebra -->
<!-- keywords: blockmatrixp -->
<!-- signatures: blockmatrixp(M) -->
### Function: blockmatrixp (M)

Retorna `true` se e somente se *M* for uma matriz e toda entrada de
*M* também for uma matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: cholesky -->
<!-- signatures: cholesky(M), cholesky(M, corpo) -->
### Function: cholesky (M)

Retorna factorização de Cholesky da matriz hermitiana (or autoadjunta) 
*M*. O valor padrão para o segundo argumento é `generalring`. Para uma descrição dos
possíveis valores para *corpo*, veja `lu_factor`.

<!-- category: LinearAlgebra -->
<!-- keywords: columnop -->
<!-- signatures: columnop(M, i, j, theta) -->
### Function: columnop (M, i, j, theta)

Se *M* for uma matriz, retorna a matriz que resulta de fazer a  
operação de coluna `C_i <- C_i - theta * C_j`. Se *M* não tiver uma linha
*i* ou *j*, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: columnspace -->
<!-- signatures: columnspace(M) -->
### Function: columnspace (M)

Se *M* for uma matriz, retorna `span (v_1, ..., v_n)`, onde o conjunto
`{v_1, ..., v_n}` é uma base para o espaço coluna de *M*.  A diferença entre o maior elemento e o menor elemento do 
conjunto vazio é `{0}`. Dessa forma, quando o espaço coluna tiver somente 
um membro, retorna `span ()`.

<!-- category: LinearAlgebra -->
<!-- keywords: columnswap -->
<!-- signatures: columnswap(M, i, j) -->
### Function: columnswap (M, i, j)

Se *M* for uma matriz, troca as colunas *i* e *j*.  Se *M* não tiver uma coluna
*i* ou *j*, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: copy -->
<!-- signatures: copy(e) -->
### Function: copy (e)

Retorna uma cópia da expressão *e* do Maxima. Embora *e* possa ser qualquer
expressão do Maxima, Afunção `copy` é mais útil quando *e* for ou
uma lista ou uma matriz; considere:

load ("linearalgebra");
m : [1,[2,3]]$
mm : m$
mm[2][1] : x$
m;
mm;



```maxima
(%i1) load("linearalgebra")$
(%i2) m : [1,[2,3]]$
(%i3) mm : m$
(%i4) mm[2][1] : x$
(%i5) m;
(%o5) [1,[x,3]]
(%i6) mm;
(%o6) [1,[x,3]]
```

Vamos tentar a mesma experiência, mas dessa vez tomemos *mm* como sendo uma cópia de *m*

m : [1,[2,3]]$
mm : copy(m)$
mm[2][1] : x$
m;
mm;



```maxima
(%i7) m : [1,[2,3]]$
(%i8) mm : copy(m)$
(%i9) mm[2][1] : x$
(%i10) m;
(%o10) [1,[2,3]]
(%i11) mm;
(%o11) [1,[x,3]]
```

Dessa vez, a atribuição a *mm* não muda o valor de *m*.

<!-- category: LinearAlgebra -->
<!-- keywords: ctranspose -->
<!-- signatures: ctranspose(M) -->
### Function: ctranspose (M)

Retorna a matriz transposta conjugada complexa da matriz *M*. A função
`ctranspose` usa `matrix_element_transpose` para transpor cada elemento da matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: diag_matrix -->
<!-- signatures: diag_matrix(d_1, d_2, ..., d_n) -->
### Function: diag_matrix (d_1, d_2, ..., d_n)

Retorna uma matriz diagonal matriz com entradas de diagonal *d_1*, *d_2*,...,*d_n*.
Quando as entradas de diagonal forem matrizes, as entradas zero da matriz retornada
serão todas matrizes de tamanho apropriado; por exemplo:







```maxima
(%i1) load("linearalgebra")$

(%i2) diag_matrix(diag_matrix(1,2),diag_matrix(3,4));

                            [ [ 1  0 ]  [ 0  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  2 ]  [ 0  0 ] ]
(%o2)                       [                    ]
                            [ [ 0  0 ]  [ 3  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  0 ]  [ 0  4 ] ]
(%i3) diag_matrix(p,q);

                                   [ p  0 ]
(%o3)                              [      ]
                                   [ 0  q ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: dotproduct -->
<!-- signatures: dotproduct(u, v) -->
### Function: dotproduct (u, v)

Retorna o produto do ponto (produto escalar) dos vectores *u* e *v*.  Isso é o mesmo
que `conjugate (transpose (u)) . v`.  Os argumentos *u* e *v* devem ser
vectores coluna.

<!-- category: LinearAlgebra -->
<!-- keywords: eigens_by_jacobi -->
<!-- signatures: eigens_by_jacobi(A), eigens_by_jacobi(A, tipo_corpo) -->
### Function: eigens_by_jacobi (A)

Calculam os autovalores e autovectores de *A* pelo método de rotações de Jacobi.
*A* deve ser uma matriz simétrica (mas essa matriz simétrica precisa não ser nem definida positiva e nem semidefinida positiva).
*tipo_corpo* indica o corpo computacional, pode ser ou `floatfield` ou `bigfloatfield`.
Se *tipo_corpo* não for especificado, o padrão é `floatfield`.


Os elementos de *A* devem ser números ou expressões que avaliam para números
via `float` ou `bfloat` (dependendo do valor de *tipo_corpo*).


Exemplos:












```maxima
(%i1) load ("linearalgebra");
(%o1) /home/robert/tmp/maxima-head/maxima/share/linearalgebra/li\
nearalgebra.mac
(%i2) S : matrix ([1/sqrt(2), 1/sqrt(2)], [- 1/sqrt(2), 1/sqrt(2)]);
                     [     1         1    ]
                     [  -------   ------- ]
                     [  sqrt(2)   sqrt(2) ]
(%o2)                [                    ]
                     [      1        1    ]
                     [ - -------  ------- ]
                     [   sqrt(2)  sqrt(2) ]
(%i3) L : matrix ([sqrt(3), 0], [0, sqrt(5)]);
                      [ sqrt(3)     0    ]
(%o3)                 [                  ]
                      [    0     sqrt(5) ]
(%i4) M : S . L . transpose (S);
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- + -------  ------- - ------- ]
            [    2         2        2         2    ]
(%o4)       [                                      ]
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- - -------  ------- + ------- ]
            [    2         2        2         2    ]
(%i5) eigens_by_jacobi (M);
The largest percent change was 0.1454972243679
The largest percent change was 0.0
number of sweeps: 2
number of rotations: 1
(%o5) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i6) float ([[sqrt(3), sqrt(5)], S]);
(%o6) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i7) eigens_by_jacobi (M, bigfloatfield);
The largest percent change was 1.454972243679028b-1
The largest percent change was 0.0b0
number of sweeps: 2
number of rotations: 1
(%o7) [[1.732050807568877b0, 2.23606797749979b0], 
                [  7.071067811865475b-1   7.071067811865475b-1 ]
                [                                              ]]
                [ - 7.071067811865475b-1  7.071067811865475b-1 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: get_lu_factors -->
<!-- signatures: get_lu_factors(x) -->
### Function: get_lu_factors (x)

Quando `x = lu_factor (A)`, então `get_lu_factors` retorna uma lista da 
forma `[P, L, U]`, onde *P* é uma matriz de permutação, *L* é triangular baixa com
a diagonal preenchida com a unidade, e *U* é triangular alta, e `A = P L U`.

<!-- category: LinearAlgebra -->
<!-- keywords: hankel -->
<!-- signatures: hankel(col), hankel(col, lin) -->
### Function: hankel (col)

Retorna uma matriz de Hankel *H*. A primeira coluna de *H* é *col*;
excepto para a primeira entrada, a última linha de *H* é *lin*. O
valor padrão para *lin* é o vector nulo com o mesmo comprimento que *col*.

<!-- category: LinearAlgebra -->
<!-- keywords: hessian -->
<!-- signatures: hessian(f, vars) -->
### Function: hessian (f, vars)

Retorna a matriz hessiana de *f* com relação às variáveis na lista
*vars*.  As entradas *i*,*j* da matriz hessiana são
*diff(f vars[i],1,vars[j],1)*.

<!-- category: LinearAlgebra -->
<!-- keywords: hilbert_matrix -->
<!-- signatures: hilbert_matrix(n) -->
### Function: hilbert_matrix (n)

Retorna the *n* by *n* matriz de Hilbert. Quando *n* não for um inteiro
positivo, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: identfor -->
<!-- signatures: identfor(M), identfor(M, corpo) -->
### Function: identfor (M)

Retorna uma matriz identidade que tem o mesmo tamanho que a matriz
*M*.  As entradas de diagonal da matriz identidade são a 
identidade multiplicativa do corpo *corpo*; o padrão para
*corpo* é *generalring*.


O primeiro argumento *M* pode ser uma  matriz quadrada ou um 
não matriz. Quando *M* for uma matriz, cada entrada de *M* pode ser uma
matriz quadrada – dessa forma *M* pode ser uma matriz de bloco do Maxima. A
matriz pode ser de bloco para qualquer (finita) quantidade de níveis.


Veja também `zerofor`

<!-- category: LinearAlgebra -->
<!-- keywords: invert_by_lu -->
<!-- signatures: invert_by_lu(M, (rng generalring)) -->
### Function: invert_by_lu (M, (rng generalring))

Inverte a matriz *M* através de factorização linear alta (LU).  A factorização LU
é concluída usando o anel *rng*.

<!-- category: LinearAlgebra -->
<!-- keywords: kronecker_product -->
<!-- signatures: kronecker_product(A, B) -->
### Function: kronecker_product (A, B)

Retorna o produto de Kronecker das matrizes *A* e *B*.

<!-- category: LinearAlgebra -->
<!-- keywords: locate_matrix_entry -->
<!-- signatures: locate_matrix_entry(M, r_1, c_1, r_2, c_2, f, rel) -->
### Function: locate_matrix_entry (M, r_1, c_1, r_2, c_2, f, rel)

O primeiro argumento deve ser uma matriz; os argumentos que vão de
*r_1* até *c_2* determinam um sub-matriz de *M* que consiste de
linhas que vão de *r_1* até *r_2* e colunas que vão de *c_1* até *c_2*. 


Encontra uma entrada na sub-matriz *M* que satisfaz alguma propriedade. 
Existem três casos:


(1) `rel = 'bool` e *f* um predicado: 


Examina a sub-matriz da esquerda para a direita e de cima para baixo,
e retorna o índice da primeira entrada que satisfizer o 
predicado *f*. Se nenhuma entrada da matriz satisfizer o predicado *f*, retorna `false`.


(2) `rel = 'max` e *f* avaliar para um número real:


Examina a sub-matriz procurando por uma entrada que maximize *f*.
Retorna retorna o índice da entrada maximizada.


(3) `rel = 'min` e *f* avaliar para um número real:


Examina a sub-matriz procurando por uma entrada que minimize *f*. 
Retorna o índice de uma entrada minimizada.

<!-- category: LinearAlgebra -->
<!-- keywords: lu_backsub -->
<!-- signatures: lu_backsub(M, b) -->
### Function: lu_backsub (M, b)

Quando `M = lu_factor (A, corpo)`,
então `lu_backsub (M, b)` resolve o sistema
linear `A x = b`.

<!-- category: LinearAlgebra -->
<!-- keywords: lu_factor -->
<!-- signatures: lu_factor(M, corpo) -->
### Function: lu_factor (M, corpo)

Retorna uma lista da forma `[LU, perm, corpo]`, 
ou da forma `[LU, perm, cmp, baixo-cnd alto-cnd]`, onde


  

(1) A matriz *LU* contéa factorização de *M* na forma enpacotada. Forma
      empacotada significa três coisas: Primeiro, as linhas de *LU* são permutadas confirme a 
      lista *perm*.  Se, por exemplo, *perm* for a lista list `[3,2,1]`, a primeira linha actual 
      da factorização *LU* será a terceira linha da matriz *LU*. Segundo,
      o factor triangular baixo de m é a parte triangular baixa de *LU* com as
      entradas de diagonal todas substituídas pela unidade. Terceiro, o factor triangular alto de 
      *M* é a parte triangular alta de *LU*.  


  

(2) Quando o corpo for ou `floatfield` ou `complexfield`,
      os números *baixo-cnd* e *alto-cnd* serão associados baixo e alto para o 
      número condicional de norma infinita de *M*.  Para todos os corpos (fields), o número condicional de norma infinita 
      não pode ser estimado; para tais corpos, `lu_factor` retorna uma lista com dois itens.
      Ambos o baixo e o alto associado  podem diferir de seus verdadeiros valores de 
      factores arbitráriamente grandes. (Veja também `mat_cond`.)

   
  

O argumento *M* deve ser a matriz quadrada.


  

O argumento opcional *cmp* deve ser um símbolo que determine um anel ou corpo. Os corpos e anéis 
  predefinidos são:


    

(a) `generalring` – o anel de expressões do Maxima,
    (b) `floatfield` –  o corpo dos números em ponto flutuante do tipo de precisão dupla,
    (c) `complexfield` –  o corpo dos números complexos em ponto flutuante do 
        tipo de precisão dupla,
    (d) `crering`  – o anel das expressões racionais canónicas (CRE) do Maxima,
    (e) `rationalfield` – o corpo dos números racionais,
    (f) `runningerror` – rastro de todos os erros de arredondamento de números em ponto flutuante,
     (g) `noncommutingring` – o anel de expressões do Maxima onde multiplicação for o
        operador ponto não comutativo.       


Quando o corpo for `floatfield`, `complexfield`, ou
`runningerror`, o algoritmo usa pivotagem parcial; para todos
os outros corpos, linhas são comutadas somente quando necessário para evitar um pivo
nulo.


A adição aritmética em ponto flutuante não é associativa, então o significado
de ’corpo’ difere da definição matemática.


Um membro do corpo `runningerror` é uma lista do Máxima de dois membros
da forma `[x,n]`,onde *x* é um número em onto flutuante e
`n` é um inteiro. A diferença relativa entre o valor de
’verdadeiro’ de `x` e `x` é aproximadamente associado pelo épsilon da
máquina vezes `n`. O erro de execução associado arrasta alguns termos
da ordem do quadrado do épsilon da máquina.


Não existe interface de utilizador definida um novo anel. Um utilizador que estiver
familiazrizado com o Lisp Comum está apto para definir um novo corpo.  Para fazer
isso, um utilizador deve definir funções para as operações aritméticas e
funções para conversão para a representação de corpo do Máxima e
vice-versa. Adicionalmente, para corpos ordenados (onde a pivotagem parcial será
usada), um uduário deve definir funções para módulo e para
comparar membros do corpo.  Após isso tudo que resta é definir uma
estrutura de Lisp Comum `mring`.  O ficheiro `mring` tem muitos
exemplos.

 

Para calcular a factorização, a primeira tarefa é converter cada entrada de
matriz para um elemento do corpo indicado. Quando a cnversão não for
possível, a factorização encerra com uma mensagem de erro. Elementos do
corpo não precisam ser expressões do Maxima.  Elementos do
`complexfield`, por exemplo, são números complexos do Lisp Comum. Dessa forma
após calcular a factorização, como entradas da matriz devem ser
convertidas para expressões do Maxima.


Veja também  `get_lu_factors`.


Exemplos:















```maxima
(%i1) load ("linearalgebra");
Warning - you are redefining the Maxima function require_list
Warning - you are redefining the Maxima function matrix_size
Warning - you are redefining the Maxima function rank
(%o1) /usr/local/share/maxima/5.9.2/share/linearalgebra/linearalgebra.mac
(%i2) w[i,j] := random (1.0) + %i * random (1.0);
(%o2)          w     := random(1.) + %i random(1.)
                i, j
(%i3) showtime : true$
Evaluation took 0.00 seconds (0.00 elapsed)
(%i4) M : genmatrix (w, 100, 100)$
Evaluation took 7.40 seconds (8.23 elapsed)
(%i5) lu_factor (M, complexfield)$
Evaluation took 28.71 seconds (35.00 elapsed)
(%i6) lu_factor (M, generalring)$
Evaluation took 109.24 seconds (152.10 elapsed)
(%i7) showtime : false$

(%i8) M : matrix ([1 - z, 3], [3, 8 - z]); 
                        [ 1 - z    3   ]
(%o8)                   [              ]
                        [   3    8 - z ]
(%i9) lu_factor (M, generalring);
               [ 1 - z         3        ]
               [                        ]
(%o9)         [[   3            9       ], [1, 2]]
               [ -----  - z - ----- + 8 ]
               [ 1 - z        1 - z     ]
(%i10) get_lu_factors (%);
                  [   1    0 ]  [ 1 - z         3        ]
        [ 1  0 ]  [          ]  [                        ]
(%o10) [[      ], [   3      ], [                9       ]]
        [ 0  1 ]  [ -----  1 ]  [   0    - z - ----- + 8 ]
                  [ 1 - z    ]  [              1 - z     ]
(%i11) %[1] . %[2] . %[3];
                        [ 1 - z    3   ]
(%o11)                  [              ]
                        [   3    8 - z ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: mat_cond -->
<!-- signatures: mat_cond(M, 1), mat_cond(M, inf) -->
### Function: mat_cond (M, 1)

Retorna o número condiciona da norma de ordem *p* da matriz
*m*. Os valores permitidos para *p* são 1 e *inf*.  Essa
função utiliza a factorização linear alta para inverter a matriz *m*. Dessa forma
o tempode execução para `mat_cond` é proporcional ao cubo do
tamanho da matriz; `lu_factor` determina as associaçãoes baixa e alta
para o número de condição de norma infinita em tempo proporcional ao
quadrado do tamanho da matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_fullunblocker -->
<!-- signatures: mat_fullunblocker(M) -->
### Function: mat_fullunblocker (M)

Se *M* for uma matriz de bloco, expande todos os blocos da matriz em todos os níveis. Se *M* for uma matriz,
retorna *M*; de outra forma, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_norm -->
<!-- signatures: mat_norm(M, 1), mat_norm(M, inf), mat_norm(M, frobenius) -->
### Function: mat_norm (M, 1)

Retorna a matriz de norma *p* da matriz *M*.  Os valores permitidos para *p* são
1, `inf`, e `frobenius` (a norma da matriz de Frobenius). A matriz *M* pode ser
uma matriz não de bloco.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_trace -->
<!-- signatures: mat_trace(M) -->
### Function: mat_trace (M)

Retorna o traço da matriz *M*. Se *M* não for uma matriz, retorna uma
forma substantiva. Quando *M* for uma matriz de bloco, `mat_trace(M)` retorna
o mesmo valor retornado por `mat_trace(mat_unblocker(m))`.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_unblocker -->
<!-- signatures: mat_unblocker(M) -->
### Function: mat_unblocker (M)

Se *M* for uma matriz de bloco, `mat_unbloker` desfaz o bloco de *M* um nível. Se *M* for uma matriz, 
`mat_unblocker (M)` retorna *M*; de outra forma, emite uma mensagem de erro.


Dessa forma se cada entrada de *M* for matriz, `mat_unblocker (M)` retorna uma 
matriz "desblocada", mas se cada entrada de *M* for uma matriz de bloco, `mat_unblocker (M)` 
retorna uma matriz de bloco com um nível de bloco a menos.


Se usar matrizes de bloco, muito provavelmente irá querer escolher `matrix_element_mult` para 
`"."` e `matrix_element_transpose` para `'transpose`. Veja também `mat_fullunblocker`.


Exemplo:










```maxima
(%i1) load ("linearalgebra");
Warning - you are redefining the Maxima function require_list
Warning - you are redefining the Maxima function matrix_size
Warning - you are redefining the Maxima function rank
(%o1) /usr/local/share/maxima/5.9.2/share/linearalgebra/linearalgebra.mac
(%i2) A : matrix ([1, 2], [3, 4]);
                            [ 1  2 ]
(%o2)                       [      ]
                            [ 3  4 ]
(%i3) B : matrix ([7, 8], [9, 10]);
                            [ 7  8  ]
(%o3)                       [       ]
                            [ 9  10 ]
(%i4) matrix ([A, B]);
                     [ [ 1  2 ]  [ 7  8  ] ]
(%o4)                [ [      ]  [       ] ]
                     [ [ 3  4 ]  [ 9  10 ] ]
(%i5) mat_unblocker (%);
                         [ 1  2  7  8  ]
(%o5)                    [             ]
                         [ 3  4  9  10 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_size -->
<!-- signatures: matrix_size(M) -->
### Function: matrix_size (M)

Retorna uma lista com dois elementos que fornecem o número de linhas e colunas, respectivamente
da matriz *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: nonnegintegerp -->
<!-- signatures: nonnegintegerp(n) -->
### Function: nonnegintegerp (n)

Retorna `true` se e somente se `n >= 0` e *n* for um inteiro.

<!-- category: LinearAlgebra -->
<!-- keywords: nullity -->
<!-- signatures: nullity(M) -->
### Function: nullity (M)

Se *M* for uma matriz, retorna a dimensão do espaço nulo de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: nullspace -->
<!-- signatures: nullspace(M) -->
### Function: nullspace (M)

Se *M* for uma matriz, retorna `span (v_1, ..., v_n)`, onde o conjunto `{v_1, ..., v_n}`
é uma base para o espaço nulo de *M*.  A diferença entre o maior elemento e o menor elemento do conjunto vazio é  `{0}`.  
Dessa forma, quando o espaço nulo tiver somente um membro, retorna `span ()`.

<!-- category: LinearAlgebra -->
<!-- keywords: orthogonal_complement -->
<!-- signatures: orthogonal_complement(v_1, ..., v_n) -->
### Function: orthogonal_complement (v_1, ..., v_n)

Retorna `span (u_1, ..., u_m)`, onde o conjunto `{u_1, ..., u_m}` é uma 
base para o complemento ortogonal do conjunto `(v_1, ..., v_n)`.


Cada vector no intervalo de *v_1* até *v_n* deve ser um vector coluna.

<!-- category: LinearAlgebra -->
<!-- keywords: polynomialp -->
<!-- signatures: polynomialp(p, L, coeffp, exponp), polynomialp(p, L, coeffp), polynomialp(p, L) -->
### Function: polynomialp (p, L, coeffp, exponp)

Retorna `true` se *p* for um polinómio nas variáveis da lista *L*,
O predicado *coeffp* deve avaliar para `true` para cada
coeficiente, e o predicado *exponp* deve avaliar para `true` para todos os 
expoentes das variáveis na lista *L*. Se quiser usar um valor
personalizado para *exponp*, deverá fornecer *coeffp* com um valor mesmo se quiser
o valor padrão para *coeffp*.



`polynomialp (p, L, coeffp)` é equivalente a
`polynomialp (p, L, coeffp, 'nonnegintegerp)`.


`polynomialp (p, L)` é equivalente a
`polynomialp (p, L, 'constantp, 'nonnegintegerp)`.


O polinómio não precisa ser expandido:








```maxima
(%i1) load ("linearalgebra");
Warning - you are redefining the Maxima function require_list
Warning - you are redefining the Maxima function matrix_size
Warning - you are redefining the Maxima function rank
(%o1) /usr/local/share/maxima/5.9.2/share/linearalgebra/linearalgebra.mac
(%i2) polynomialp ((x + 1)*(x + 2), [x]);
(%o2)                         true
(%i3) polynomialp ((x + 1)*(x + 2)^a, [x]);
(%o3)                         false
```


Um exemplo usando um valor personalizado para `coeffp` e para `exponp`:








```maxima
(%i1) load ("linearalgebra");
Warning - you are redefining the Maxima function require_list
Warning - you are redefining the Maxima function matrix_size
Warning - you are redefining the Maxima function rank
(%o1) /usr/local/share/maxima/5.9.2/share/linearalgebra/linearalgebra.mac
(%i2) polynomialp ((x + 1)*(x + 2)^(3/2), [x], numberp, numberp);
(%o2)                         true
(%i3) polynomialp ((x^(1/2) + 1)*(x + 2)^(3/2), [x], numberp, numberp);
(%o3)                         true
```


Polinómios com duas variáveis:








```maxima
(%i1) load ("linearalgebra");
Warning - you are redefining the Maxima function require_list
Warning - you are redefining the Maxima function matrix_size
Warning - you are redefining the Maxima function rank
(%o1) /usr/local/share/maxima/5.9.2/share/linearalgebra/linearalgebra.mac
(%i2) polynomialp (x^2 + 5*x*y + y^2, [x]);
(%o2)                         false
(%i3) polynomialp (x^2 + 5*x*y + y^2, [x, y]);
(%o3)                         true
```

<!-- category: LinearAlgebra -->
<!-- keywords: polytocompanion -->
<!-- signatures: polytocompanion(p, x) -->
### Function: polytocompanion (p, x)

Se *p* for um polinómio em *x*, retorna a atriz companheira de *p*. Para
um polinómio monico *p* de grau *n*,
temos `p = (-1)^n charpoly (polytocompanion (p, x))`.


Quando *p* não for um polinómio em *x*, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: ptriangularize -->
<!-- signatures: ptriangularize(M, v) -->
### Function: ptriangularize (M, v)

Se *M* for uma matriz onde cada entrada dessa matriz for um polinómio em *v*, retorna 
a matriz *M2* tal que


(1) *M2* é triangular alta,


(2) `M2 = E_n ... E_1 M`,
onde os elemetnos de *E_1* a *E_n* são matrizes elementares 
cujas entrada são polinómios em *v*,


(3) `|det (M)| = |det (M2)|`,


Nota: Essa função não verifica se toda entrada é um polinómio em *v*.

<!-- category: LinearAlgebra -->
<!-- keywords: rowop -->
<!-- signatures: rowop(M, i, j, theta) -->
### Function: rowop (M, i, j, theta)

Se *M* for uma matriz, retorna a matriz que resulta de se fazer a  
operação de linha `R_i <- R_i - theta * R_j`. Se *M* não tiver uma linha
*i* ou *j*, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: rowswap -->
<!-- signatures: rowswap(M, i, j) -->
### Function: rowswap (M, i, j)

Se *M* for uma matriz, permuta as linha *i* e *j*. Se *M* não tiver uma linha
*i* ou *j*, emite uma mensagem de erro.

<!-- category: LinearAlgebra -->
<!-- keywords: toeplitz -->
<!-- signatures: toeplitz(col), toeplitz(col, lin) -->
### Function: toeplitz (col)

Retorna uma matriz de Toeplitz *T*. a primeira coluna de *T* é *col*;
excepto para a primeira entrada, a primeira linha de *T* é *lin*. O
padrão para *lin* é o conjugado complexo de *col*. Exemplo:







```maxima
(%i1) load("linearalgebra")$

(%i2)  toeplitz([1,2,3],[x,y,z]);

                                  [ 1  y  z ]
                                  [         ]
(%o2)                             [ 2  1  y ]
                                  [         ]
                                  [ 3  2  1 ]
(%i3)  toeplitz([1,1+%i]);

                              [   1     1 - %I ]
(%o3)                         [                ]
                              [ %I + 1    1    ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: vandermonde_matrix -->
<!-- signatures: vandermonde_matrix([x_1, ..., x_n]) -->
### Function: vandermonde_matrix ([x_1, ..., x_n])

Retorna uma matriz *n* por *n* cuja *i*-ésima linha é 
`[1, x_i, x_i^2, ... x_i^(n-1)]`.

<!-- category: LinearAlgebra -->
<!-- keywords: zerofor -->
<!-- signatures: zerofor(M), zerofor(M, fld) -->
### Function: zerofor (M)

Retorna uma matriz zero que tem o mesmo tamanho da matriz
*M*.  Toda entrada da matriz zero é a
identidade aditiva do anel *fld*; o valor padrão para
*fld* é *generalring*.


O primeiro argumento *M* pode ser uma matriz quadrada ou uma
não matriz. Quando *M* for uma matriz, cada entrada de *M* pode ser uma
matriz quadrada – dessa forma *M* pode ser uma matriz de bloco do Maxima. A
matriz pode ser de bloco para qualquer nível (finito).


Veja também `identfor`

<!-- category: LinearAlgebra -->
<!-- keywords: zeromatrixp -->
<!-- signatures: zeromatrixp(M) -->
### Function: zeromatrixp (M)

Se *M* não for uma matriz de bloco, retorna `true` se `is (equal (e, 0))` 
for verdadeiro para cada elemento *e* da matriz *M*.  Se *M* for uma matriz de bloco, retorna
`true` se `zeromatrixp` avaliar para `true` para cada elemento de *e*.

