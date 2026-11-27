## Fluxo de Programa

<!-- category: Programming -->
<!-- keywords: backtrace -->
<!-- signatures: backtrace(), backtrace(n) -->
### Function: backtrace ()

Imprime a pilha de chamadas, que é, a lista de funções que
foram chamadas pela função correntemente activa.


`backtrace()` imprime toda a pilha de chamadas.


`backtrace (n)` imprime as *n* mais recentes chamadas a
funções, incluindo a função correntemente activa.




`backtrace` pode ser chamada por um script, uma função, ou a partir da linha de comando interativa
(não somente em um contexto de depuração).


Exemplos:



- *
`backtrace()` imprime toda a pilha de chamadas.

```maxima
(%i1) h(x) := g(x/7)$
(%i2) g(x) := f(x-11)$
(%i3) f(x) := e(x^2)$
(%i4) e(x) := (backtrace(), 2*x + 13)$
(%i5) h(10);
#0: e(x=4489/49)
#1: f(x=-67/7)
#2: g(x=10/7)
#3: h(x=10)
                              9615
(%o5)                         ----
                               49
```



- *
`backtrace (n)` imprime as *n* mais recentes chamadas a
funções, incluindo a função correntemente activa.

```maxima
(%i1) h(x) := (backtrace(1), g(x/7))$
(%i2) g(x) := (backtrace(1), f(x-11))$
(%i3) f(x) := (backtrace(1), e(x^2))$
(%i4) e(x) := (backtrace(1), 2*x + 13)$
(%i5) h(10);
#0: h(x=10)
#0: g(x=10/7)
#0: f(x=-67/7)
#0: e(x=4489/49)
                              9615
(%o5)                         ----
                               49
```

<!-- category: Programming -->
<!-- keywords: do -->
<!-- signatures: do -->
### Function: do

A declaração `do` é usada para executar iteração.  Devido à sua
grande generalidade a declaração `do` será  descrita em duas partes.
Primeiro a forma usual será dada que é análoga à forma que é usada em
muitas outras linguagens de programação (Fortran, Algol, PL/I, etc.); em segundo lugar
os outros recursos serão mencionados.


Existem três variantes do operador especial `do` que diferem somente por suas
condições de encerramento.  São elas:



- *
`for Variável: valor_inicial step incremento thru limite do corpo`
- *
`for Variável: valor_inicial step incremento while condition do corpo`
- *
`for Variável: valor_inicial step incremento unless condition do corpo`



(Alternativamente, o `step` pode ser dado após a condição de encerramento
ou limite.)


*valor_inicial*, *incremento*, *limite*, e *corpo* podem ser quaisquer
expressões.  Se o incremento for 1 então "`step 1`" pode ser omitido.


A execução da declaração `do` processa-se primeiro atribuindo o
valor_inicial para a variável (daqui em diante chamada a
variável de controle).  Então: (1) Se a variável de controle excede
o limite de uma especificação `thru`, ou se a condição de `unless` for
`true`, ou se a condição de `while` for `false` então o `do`
será encerrado.  (2) O corpo é avaliado.  (3) O incremento é adicionado à
variável de controle.  O processo de (1) a (3) é executado
repetidamente até que a condição de encerramento seja satisfeita.  Pode-se também
dar muitas condições de encerramento e nesse caso o `do` termina
quando qualquer delas for satisfeita.


Em geral o teste `thru` é satisfeito quando a variável de controle for
maior que o limite se o incremento for não negativo, ou quando a
variável de controle for menor que o limite se o incremento for negativo.
O incremento e o limite podem ser expressões não numéricas enquanto essa
desigualdade puder ser determinada.  Todavia, a menos que o incremento seja
sintaticamente negativo (e.g. for um número negativo) na hora em que a declaração `do`
for iniciada, Maxima assume que o incremento e o limite serão positivos quando o `do` for
executado.  Se o limite e o incremento não forem positivos, então o `do` pode não terminar
propriamente.


Note que o limite, incremento, e condição de encerramento são
avaliados cada vez que ocorre um ciclo.  Dessa forma se qualquer desses for responsável por
muitos cálculos, e retornar um resultado que não muda durante todas
as execuções do corpo, então é mais eficiente escolher uma
variável para seu valor anterior para o `do` e usar essa variável na
forma `do`.


O valor normalmente retornado por uma declaração `do` é o átomo `done`.
Todavia, a função
`return` pode ser usada dentro do corpo para sair da delcaração `do` prematuramente e dar
a isso qualquer valor desejado.
Note todavia que um `return` dentro de um `do` que
ocorre em um `block` encerrará somente o `do` e não o `block`.  Note também
que a função `go` não pode ser usada para sair de dentro de um `do` dentro de um
`block` que o envolve.


A variável de controle é sempre local para o `do` e dessa forma qualquer
variável pode ser usada sem afectar o valor de uma variável com
o mesmo nome fora da declaração `do`.  A variável de controle é liberada
após o encerramento da declaração `do`.



```maxima
(%i1) for a:-3 thru 26 step 7 do display(a)$
                             a = - 3

                              a = 4

                             a = 11

                             a = 18

                             a = 25
```



```maxima
(%i1) s: 0$
(%i2) for i: 1 while i <= 10 do s: s+i;
(%o2)                         done
(%i3) s;
(%o3)                          55
```


Note que a condição `while i <= 10`
é equivalente a `unless i > 10` e também `thru 10`.



```maxima
(%i1) series: 1$
(%i2) term: exp (sin (x))$
(%i3) for p: 1 unless p > 7 do
          (term: diff (term, x)/p, 
           series: series + subst (x=0, term)*x^p)$
(%i4) series;
                  7    6     5    4    2
                 x    x     x    x    x
(%o4)            -- - --- - -- - -- + -- + x + 1
                 90   240   15   8    2
```


que fornece 8 termos da série de Taylor para `e^sin(x)`.



```maxima
(%i1) poly: 0$
(%i2) for i: 1 thru 5 do
          for j: i step -1 thru 1 do
              poly: poly + i*x^j$
(%i3) poly;
                  5      4       3       2
(%o3)          5 x  + 9 x  + 12 x  + 14 x  + 15 x
(%i4) guess: -3.0$
(%i5) for i: 1 thru 10 do
          (guess: subst (guess, x, 0.5*(x + 10/x)),
           if abs (guess^2 - 10) < 0.00005 then return (guess));
(%o5)                  - 3.162280701754386
```


Esse exemplo calcula a raíz quadrada negativa de 10 usando a
iteração de Newton- Raphson um maximum de 10 vezes.  Caso o critério de
convergêcia não tenha sido encontrado o valor retornado pode ser `done`.
Em lugar de sempre adicionar uma quantidade à variável de controle pode-se
algumas vezes desejar alterar isso de alguma outra forma para cada iteração.
Nesse caso pode-se usar `next expressão` em lugar de `step incremento`.
Isso fará com que a variável de controle seja escolhida para o
resultado da expressão de avaliação cada vez que o ciclo de repetição for executado.



```maxima
(%i6) for count: 2 next 3*count thru 20 do display (count)$
                            count = 2

                            count = 6

                           count = 18
```



Como uma alternativa para `for Variável: valor ...do...` a sintaxe
`for Variável from valor ...do...`  pode ser usada.  Isso permite o
`from valor` ser colocado após o `step` ou proximo valor ou após a
condição de encerramento.  Se `from valor` for omitido então 1 é usado como
o valor inicial.


Algumas vezes se pode estar interessado em executar uma iteração onde
a variável de controle nunca seja usada.  Isso é permissível
para dar somente as condições de encerramento omitindo a inicialização
e a informação de actualização como no exemplo seguinte para para calcular a
raíz quadrada de 5 usando uma fraca suposição inicial.



```maxima
(%i1) x: 1000$
(%i2) thru 20 do x: 0.5*(x + 5.0/x)$
(%i3) x;
(%o3)                   2.23606797749979
(%i4) sqrt(5), numer;
(%o4)                   2.23606797749979
```


Se isso for desejado pode-se sempre omitir as condições de encerramento
inteiramente e apenas dar o corpo `do corpo` que continuará a ser 
avaliado indefinidamente.  Nesse caso a função `return` será usada para
encerrar a execução da declaração `do`.



```maxima
(%i1) newton (f, x):= ([y, df, dfx], df: diff (f ('x), 'x),
          do (y: ev(df), x: x - f(x)/y, 
              if abs (f (x)) < 5e-6 then return (x)))$
(%i2) sqr (x) := x^2 - 5.0$
(%i3) newton (sqr, 1000);
(%o3)                   2.236068027062195
```



(Note que `return`, quando executado, faz com que o valor corrente de
`x` seja retornado como o valor da declaração `do`.  O `block` é encerrado e
esse valor da declaração `do` é retornado como o valor do `block` porque o
`do` é a última declaração do `block`.)


Uma outra forma de `do` é disponível no Maxima.  A sintaxe é:



```maxima
for Variável in list end_tests do corpo
```


Os elementos de *list* são quaisquer expressões que irão
sucessivamente ser atribuídas para a variável a cada iteração do
corpo.  O teste opcional *end_tests* pode ser usado para encerrar a execução da
declaração `do`; de outra forma o `do` terminará quando a lista for exaurida ou quando
um `return` for executado no corpo.  (De facto, a lista pode ser qualquer
expressão não atomica, e partes sucessivas são usadas.)



```maxima
(%i1)  for f in [log, rho, atan] do ldisp(f(1))$
(%t1)                                  0
(%t2)                                rho(1)
                                     %pi
(%t3)                                 ---
                                      4
(%i4) ev(%t3,numer);
(%o4)                             0.78539816
```

<!-- category: Programming -->
<!-- keywords: errcatch -->
<!-- signatures: errcatch(expr_1, ..., expr_n) -->
### Function: errcatch (expr_1, ..., expr_n)

Avalia *expr_1*, ..., *expr_n* uma por uma e
retorna `[expr_n]` (uma lista) se nenhum erro ocorrer.  Se um
erro ocorrer na avaliação de qualquer argumento, `errcatch`
evita que o erro se propague e
retorna a lista vazia `[]` sem avaliar quaisquer mais argumentos.


`errcatch`
é útil em ficheiros `batch` onde se suspeita que um erro possa estar ocorrendo o `errcatch`
terminará o `batch` se o erro não for detectado.

<!-- category: Programming -->
<!-- keywords: error -->
<!-- signatures: error(expr_1, ..., expr_n) -->
### Function: error (expr_1, ..., expr_n)

Avalia e imprime *expr_1*, ..., *expr_n*,
e então causa um retorno de erro para o nível mais alto do Maxima
ou para o mais próximo contendo `errcatch`.


A variável `error` é escolhida para uma lista descrevendo o erro.
O primeiro elemento de `error` é uma sequência de caracteres de formato,
que junta todas as sequências de caracteres entre os argumentos *expr_1*, ..., *expr_n*,
e os elementos restantes são os valores de quaisquer argumentos que não são sequências de caracteres.


`errormsg()` formata e imprime `error`.
Isso efectivamente reimprime a mais recente mensagem de erro.

<!-- category: Programming -->
<!-- keywords: errormsg -->
<!-- signatures: errormsg() -->
### Function: errormsg ()

Reimprime a mais recente mensagem de erro.
A variável `error` recebe a mensagem,
e `errormsg` formata e imprime essa mensagem.

<!-- category: Programming -->
<!-- keywords: for -->
<!-- signatures: for -->
### Function: for

Usado em iterações.  Veja `do` para uma descrição das
facilidades de iteração do Maxima.

<!-- category: Programming -->
<!-- keywords: go -->
<!-- signatures: go(tag) -->
### Function: go (tag)

é usada dentro de um `block` para transferir o controle para a declaração
do bloco que for identificada com o argumento para `go`.  Para identificar uma
declaração, coloque antes dessa declaração um argumento atomico como outra declaração no
`block`.  Por exemplo:



```maxima
block ([x], x:1, loop, x+1, ..., go(loop), ...)
```


O argumento para `go` deve ser o nome de um identificardor aparecendo no mesmo
`block`.  Não se pode usar `go` para transferir para um identificador em um outro `block` que não seja
o próprio contendo o `go`.

<!-- category: Programming -->
<!-- keywords: if -->
<!-- signatures: if -->
### Function: if

Representa avaliação condicional. Várias formas de expressões `if` são reconhecidas.
`if cond_1 then expr_1 else expr_0`
avalia para *expr_1* se *cond_1* avaliar para `true`,
de outra forma a expressão avalia para `expr_0`.


`if cond_1 then expr_1 elseif cond_2 then expr_2 elseif ... else expr_0`
avalia para *expr_k* se *cond_k* for `true` e todas as condições precedentes forem `false`.
Se nenhuma das condições forem `true`, a expressão avalia para `expr_0`.


O comportamento `else false` é assumido se `else` for omitido.
Isso é, `if cond_1 then expr_1` é equivalente a
`if cond_1 then expr_1 else false`,
e `if cond_1 then expr_1 elseif ... elseif cond_n then expr_n`
é equivalente a
`if cond_1 then expr_1 elseif ... elseif cond_n then expr_n else false`.


As alternativas *expr_0*, ..., *expr_n* podem ser quaisquer expressões do Maxima,
incluíndo expressões `if` aninhadas ( if dentro de if).
As alternativas não são nem simplificadas nem avaliadas a menos que a correspondente condição seja `true`.


As condições *cond_1*, ..., *cond_n* são expressões tais que `is(cond_k)` avaliem
para `true` ou para `false`;
de outra forma é um erro.
Entre outros elementos, condições podem compreender operadores lógicos e relacionais como segue.





```maxima
Operação             Símbolo      Tipo
 
menor que            <           infixo relacional
menor que            <=
  ou igual a                     infixo relacional
igualdade            =
  (sintática)                    infixo relacional
negação de =         #           infixo relacional
igualdade (valor)    equal       função relacional
negação de           notequal
  igualdade                      função relacional
maior que            >=
  ou igual a                     infixo relacional
maior que            >           infixo relacional
e                    and         infixo lógico
ou                   or          infixo lógico
não                  not         prefixo lógico
```

<!-- category: Programming -->
<!-- keywords: map -->
<!-- signatures: map(f, expr_1, ..., expr_n) -->
### Function: map (f, expr_1, ..., expr_n)

Retorna uma expressão cujo operador principal
é o mesmo que o das expressões
*expr_1*, ..., *expr_n* mas cujas subpartes são os resultados da
aplicação de *f* nas correspondentes subpartes das expressões.  *f* é ainda
o nome de uma função de $n$ argumentos
ou é uma forma `lambda` de $n$ argumentos.


`maperror` - se `false` fará com que todas as funções mapeadas
(1) parem quando elas terminarem retornando a menor expi se não forem todas as
expi do mesmo comprimento e (2) aplique fn a [exp1, exp2,...]
se expi não forem todas do mesmo tipo de objecto.  Se `maperror` for `true`
então uma mensagem de erro será dada nas duas instâncias acima.


Um dos usos dessa função é para mapear (`map`) uma função (e.g. `partfrac`)
sobre cada termo de uma expressão muito larga onde isso comumente não poderia
ser possível usar a função sobre a expressão inteira devido a uma
exaustão de espaço da lista de armazenamento no decorrer da computação.





```maxima
(%i1) map(f,x+a*y+b*z);
(%o1)                        f(b z) + f(a y) + f(x)
(%i2) map(lambda([u],partfrac(u,x)),x+1/(x^3+4*x^2+5*x+2));
                           1       1        1
(%o2)                     ----- - ----- + -------- + x
                         x + 2   x + 1          2
                                         (x + 1)
(%i3) map(ratsimp, x/(x^2+x)+(y^2+y)/y);
                                      1
(%o3)                            y + ----- + 1
                                    x + 1
(%i4) map("=",[a,b],[-0.5,3]);
(%o4)                          [a = - 0.5, b = 3]
```

<!-- category: Programming -->
<!-- keywords: mapatom -->
<!-- signatures: mapatom(expr) -->
### Function: mapatom (expr)

Retorna `true` se e somente se *expr* for tratada pelas rotinas de
mapeamento como um átomo.  "Mapatoms" são átomos, números
(incluíndo números racioanais), e variáveis subscritas.

<!-- category: Programming -->
<!-- keywords: maperror -->
<!-- signatures: maperror -->
### Variable: maperror

Valor por omissão: `true`


Quando `maperror` é `false`, faz com que todas as funções mapeadas, por exemplo



```maxima
map (f, expr_1, expr_2, ...))
```


(1) parem quando elas terminarem
retornando a menor expi se não forem todas as expi do mesmo
comprimento e (2) aplique `f` a `[expr_1, expr_2, ...]` se `expr_i` não forem todas
do mesmo tipo de objecto.


Se `maperror` for `true` então uma ,mensagem de erro
é mostrada nas duas instâncias acima.

<!-- category: Programming -->
<!-- keywords: maplist -->
<!-- signatures: maplist(f, expr_1, ..., expr_n) -->
### Function: maplist (f, expr_1, ..., expr_n)

Retorna uma lista de aplicações de *f*
em todas as partes das expressões *expr_1*, ..., *expr_n*.
*f* é o nome de uma função, ou uma expressão lambda.


`maplist` difere de `map (f, expr_1, ..., expr_n)`
que retorna uma expressão com o mesmo operador principal que *expr_i* tem
(excepto para simplificações  e o caso onde `map` faz um `apply`).

<!-- category: Programming -->
<!-- keywords: outermap -->
<!-- signatures: outermap(f, a_1, ..., a_n) -->
### Function: outermap (f, a_1, ..., a_n)

Aplica a função *f* para cada um dos elementos do produto externo
*a_1* vezes *a_2* ... vezes *a_n*.


*f* é o nome de uma função de $n$ argumentos
ou uma expressão lambda de $n$ argumentos.
Cada argumento *a_k* pode ser uma lista simples ou lista aninhada ( lista contendo listas como elementos ), ou uma matrz, ou qualquer outro tip de expressão.


O valor de retorno de `outermap` é uma estrutura aninhada.
Tomemos *x* como sendo o valor de retorno.
Então *x* tem a mesma estrutura da primeira lista, lista aninhada, ou argumento matriz,
`x[i_1]...[i_m]` tem a mesma estrutura que a segunda lista, lista aninhada, ou argumento matriz,
`x[i_1]...[i_m][j_1]...[j_n]` tem a mesma estrutura que a terceira lista, lista aninhada, ou argumento matriz,
e assim por diante,
onde *m*, *n*, ... são os números dos índices requeridos para acessar os
elementos de cada argumento (um para uma lista, dois para uma matriz, um ou mais para uma lista aninhada).
Argumentos que não forem listas ou matrizes não afectam a estrutura do valor de retorno.


Note que o efeito de `outermap` é diferente daquele de aplicar *f*
a cada um dos elementos do produto externo retornado por `cartesian_product`.
`outermap` preserva a estrutura dos argumentos no valor de retorno,
enquanto `cartesian_product` não reserva essa mesma estrutura.


`outermap` avalia seus argumentos.


Veja também `map`, `maplist`, e `apply`.



Exemplos:
Exemplos elementares de `outermap`.
Para mostrar a a combinação de argumentos mais claramente, `F` está indefinida à esquerda.










```maxima
(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) outermap (F, matrix ([a, b], [c, d]), matrix ([1, 2], [3, 4]));
         [ [ F(a, 1)  F(a, 2) ]  [ F(b, 1)  F(b, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(a, 3)  F(a, 4) ]  [ F(b, 3)  F(b, 4) ] ]
(%o2)    [                                            ]
         [ [ F(c, 1)  F(c, 2) ]  [ F(d, 1)  F(d, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(c, 3)  F(c, 4) ]  [ F(d, 3)  F(d, 4) ] ]
(%i3) outermap (F, [a, b], x, matrix ([1, 2], [3, 4]));
       [ F(a, x, 1)  F(a, x, 2) ]  [ F(b, x, 1)  F(b, x, 2) ]
(%o3) [[                        ], [                        ]]
       [ F(a, x, 3)  F(a, x, 4) ]  [ F(b, x, 3)  F(b, x, 4) ]
(%i4) outermap (F, [a, b], matrix ([1, 2]), matrix ([x], [y]));
       [ [ F(a, 1, x) ]  [ F(a, 2, x) ] ]
(%o4) [[ [            ]  [            ] ], 
       [ [ F(a, 1, y) ]  [ F(a, 2, y) ] ]
                              [ [ F(b, 1, x) ]  [ F(b, 2, x) ] ]
                              [ [            ]  [            ] ]]
                              [ [ F(b, 1, y) ]  [ F(b, 2, y) ] ]
(%i5) outermap ("+", [a, b, c], [1, 2, 3]);
(%o5) [[a + 1, a + 2, a + 3], [b + 1, b + 2, b + 3], 
                                           [c + 1, c + 2, c + 3]]
```


Uma explanação final do valor de retorno de `outermap`.
Os argumentos primeiro, segundo, e terceiro são matriz, lista, e matriz, respectivamente.
O valor de retorno é uma matriz.
Cada elementos daquela matriz é uma lista,
e cada elemento de cada lista é uma matriz.














```maxima
(%i1) arg_1 :  matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) arg_2 : [11, 22];
(%o2)                       [11, 22]
(%i3) arg_3 : matrix ([xx, yy]);
(%o3)                      [ xx  yy ]
(%i4) xx_0 : outermap (lambda ([x, y, z], x / y + z), arg_1, arg_2, arg_3);
               [  [      a        a  ]  [      a        a  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
(%o4)  Col 1 = [                                              ]
               [  [      c        c  ]  [      c        c  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
                 [  [      b        b  ]  [      b        b  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
         Col 2 = [                                              ]
                 [  [      d        d  ]  [      d        d  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
(%i5) xx_1 : xx_0 [1][1];
           [      a        a  ]  [      a        a  ]
(%o5)     [[ xx + --  yy + -- ], [ xx + --  yy + -- ]]
           [      11       11 ]  [      22       22 ]
(%i6) xx_2 : xx_0 [1][1] [1];
                      [      a        a  ]
(%o6)                 [ xx + --  yy + -- ]
                      [      11       11 ]
(%i7) xx_3 : xx_0 [1][1] [1] [1][1];
                                  a
(%o7)                        xx + --
                                  11
(%i8) [op (arg_1), op (arg_2), op (arg_3)];
(%o8)                  [matrix, [, matrix]
(%i9) [op (xx_0), op (xx_1), op (xx_2)];
(%o9)                  [matrix, [, matrix]
```


`outermap` preserves the structure of the arguments in the return value,
while `cartesian_product` does not.









```maxima
(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) setify (flatten (%));
(%o2) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i3) map (lambda ([L], apply (F, L)), cartesian_product ({a, b, c}, {1, 2, 3}));
(%o3) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i4) is (equal (%, %th (2)));
(%o4)                         true
```

<!-- category: Programming -->
<!-- keywords: prederror -->
<!-- signatures: prederror -->
### Variable: prederror

Valor por omissão: `true`


Quando `prederror` for `true`, uma mensagem de erro é mostrada
sempre que o predicado de uma declaração `if` ou uma função `is` falha em
avaliar ou para `true` ou para  `false`.


Se `false`, `unknown` é retornado
no lugar nesse caso.  O modo `prederror: false` não é suportado no
código traduzido;
todavia, `maybe` é suportado no código traduzido.


Veja também `is` e `maybe`.

<!-- category: Programming -->
<!-- keywords: return -->
<!-- signatures: return(valor) -->
### Function: return (valor)

Pode ser usada para sair explicitamente de um bloco, levando
seu argumento.  Veja `block` para mais informação.

<!-- category: Programming -->
<!-- keywords: scanmap -->
<!-- signatures: scanmap(f, expr), scanmap(f, expr, bottomup) -->
### Function: scanmap (f, expr)

Recursivamente aplica *f* a *expr*, de cima
para baixo.  Isso é muito útil quando uma factoração completa é
desejada, por exemplo:



```maxima
(%i1) exp:(a^2+2*a+1)*y + x^2$
(%i2) scanmap(factor,exp);
                                    2      2
(%o2)                         (a + 1)  y + x
```


Note o caminho através do qual `scanmap` aplica a dada função `factor` para as
subexpressões constituintes de *expr*; se outra forma de *expr* é apresentada
para `scanmap` então o resultado pode ser diferente.  Dessa forma, `%o2` não é
recuperada quando `scanmap` é aplicada para a forma expandida de exp:



```maxima
(%i3) scanmap(factor,expand(exp));
                           2                  2
(%o3)                      a  y + 2 a y + y + x
```


Aqui está um outro exemplo do caminho no qual `scanmap` aplica
recursivamente uma função dada para todas as subexpressões, incluindo expoentes:



```maxima
(%i4) expr : u*v^(a*x+b) + c$
(%i5) scanmap('f, expr);
                    f(f(f(a) f(x)) + f(b))
(%o5) f(f(f(u) f(f(v)                      )) + f(c))
```


`scanmap (f, expr, bottomup)` aplica *f* a *expr* de
baixo para cima.  E.g., para `f` indefinida,



```maxima
scanmap(f,a*x+b) ->
   f(a*x+b) -> f(f(a*x)+f(b)) -> f(f(f(a)*f(x))+f(b))
scanmap(f,a*x+b,bottomup) -> f(a)*f(x)+f(b)
    -> f(f(a)*f(x))+f(b) ->
     f(f(f(a)*f(x))+f(b))
```


Neste caso, obtém-se a mesma resposta pelos dois métodos.

<!-- category: Programming -->
<!-- keywords: throw -->
<!-- signatures: throw(expr) -->
### Function: throw (expr)

Avalia *expr* e descarta o valor retornado para o mais recente
`catch`.  `throw` é usada com `catch` como um mecanismo
de retorno não local.

<!-- category: Programming -->
<!-- keywords: while -->
<!-- signatures: while -->
### Function: while

Veja `do`.

