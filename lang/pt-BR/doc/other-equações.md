## Equações

<!-- category: Other -->
<!-- keywords: %rnum_list -->
<!-- signatures: %rnum_list -->
### Variable: %rnum_list

Valor padrão: `[]`


`%rnum_list` é a lista de variáveis introduzidas em soluções
por `algsys`.
`%r` variáveis São adicionadas a `%rnum_list` na ordem em que
forem criadas.
Isso é conveniente para fazer substituições dentro da
solução mais tarde.

É recomendado usar essa lista em lugar de
fazer `concat ('%r, j)`.

<!-- category: Other -->
<!-- keywords: algexact -->
<!-- signatures: algexact -->
### Variable: algexact

Valor padrão: `false`


`algexact` afeta o comportamento de `algsys` como segue:


Se `algexact` é `true`,
`algsys` sempre chama `solve` e então usa `realroots`
sobre falhas de `solve`.


Se `algexact` é `false`, `solve` é chamada somente se
o eliminante não for de uma variável, ou se for uma quadrática ou uma
biquadrada.


Dessa forma `algexact: true` não garante somente soluções
exatas, apenas que `algsys` tentará primeiro pegar
soluções exatas, e somente retorna aproximações quando tudo mais falha.

<!-- category: Other -->
<!-- keywords: algsys -->
<!-- signatures: algsys([expr_1, ..., expr_m], [x_1, ..., x_n]), algsys([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: algsys ([expr_1, ..., expr_m], [x_1, ..., x_n])

Resolve polinômios simultâneos *expr_1*, ..., *expr_m*
ou equações polinômiais *eqn_1*, ..., *eqn_m*
para as variáveis *x_1*, ..., *x_n*.
Uma expressão *expr* é equivalente a uma equação `expr = 0`.
Pode existir mais equações que variáveis ou vice-versa.


`algsys` retorna uma lista de soluções,
com cada solução dada com uma lista de valores de estado das equações
das variáveis *x_1*, ..., *x_n* que satisfazem o sistema de equações.
Se `algsys` não pode achar uma solução, uma lista vazia `[]` é retornada.


Os símbolos `%r1`, `%r2`, ...,
são introduzidos tantos quantos forem necessários para representar parâmetros arbitrários na solução;
essas variáveis são também anexadas à lista `%rnum_list`.


O método usado é o seguinte:


(1) Primeiro as equações são fatoradas e quebradas em subsistemas.


(2) Para cada subsistema *S_i*, uma equação *E* e uma variável *x* são
selecionados.
A variável é escolhida para ter o menor grau não zero.
Então a resultante de *E* e *E_j* em relação a *x* é calculada para cada um das
equações restantes *E_j* nos subsistemas *S_i*.
Isso retorna um novo subsistema *S_i’* em umas poucas variáveis, como *x* tenha sido eliminada.
O processo agora retorna ao passo (1).


(3) Eventualmente, um subsistema consistindo de uma equação simples é
obtido.  Se a equação é de várias variáveis e aproximações na
forma de números em ponto flutuante nã tenham sido introduzidas, então `solve` é
chamada para achar uma solução exata.


Em alguns casos, `solve` não está habilitada a achar uma solução,
ou se isso é feito a solução pode ser uma expressão expressão muito larga.



Se a equação é de uma única variável e é ou linear, ou quadrática, ou
biquadrada, então novamente `solve` é chamada se aproximações não tiverem
sido introduzidas.  Se aproximações tiverem sido introduzidas ou a
equação não é de uma única variável e nem tão pouco linear, quadratica, ou
biquadrada, então o comutador `realonly` é `true`, A função
`realroots` é chamada para achar o valor real das soluções.  Se
`realonly` é `false`, então `allroots` é chamada a qual procura por
soluções reais e complexas.


Se `algsys` produz uma solução que tem
poucos digitos significativos que o requerido, o usuário pode escolher o valor
de `algepsilon` para um valor maior.


Se `algexact` é escolhido para
`true`, `solve` será sempre chamada.



(4) Finalmente, as soluções obtidas no passo (3) são substituídas dentro
dos níveis prévios e o processo de solução retorna para (1).



Quando `algsys` encontrar uma equação de várias variáveis que contém
aproximações em ponto flutuante (usualmente devido a suas falhas em achar
soluções exatas por um estágio mais fácil), então não tentará
aplicar métodos exatos para tais equações e em lugar disso imprime a mensagem:
"`algsys` cannot solve - system too complicated."


Interações com `radcan` podem produzir expressões largas ou
complicadas.
Naquele caso, pode ser possível isolar partes do resultado
com `pickapart` ou `reveal`.


Ocasionalmente, `radcan` pode introduzir uma unidade imaginária
`%i` dentro de uma solução que é atualmente avaliada como real.


Exemplos:




+
+








```maxima
(%i1) e1: 2*x*(1 - a1) - 2*(x - 1)*a2;
(%o1)              2 (1 - a1) x - 2 a2 (x - 1)
(%i2) e2: a2 - a1; 
(%o2)                        a2 - a1
(%i3) e3: a1*(-y - x^2 + 1); 
                                   2
(%o3)                   a1 (- y - x  + 1)
(%i4) e4: a2*(y - (x - 1)^2);
                                       2
(%o4)                   a2 (y - (x - 1) )
(%i5) algsys ([e1, e2, e3, e4], [x, y, a1, a2]);
(%o5) [[x = 0, y = %r1, a1 = 0, a2 = 0], 

                                  [x = 1, y = 0, a1 = 1, a2 = 1]]
(%i6) e1: x^2 - y^2;
                              2    2
(%o6)                        x  - y
(%i7) e2: -1 - y + 2*y^2 - x + x^2;
                         2        2
(%o7)                 2 y  - y + x  - x - 1
(%i8) algsys ([e1, e2], [x, y]);
                 1            1
(%o8) [[x = - -------, y = -------], 
              sqrt(3)      sqrt(3)

        1              1             1        1
[x = -------, y = - -------], [x = - -, y = - -], [x = 1, y = 1]]
     sqrt(3)        sqrt(3)          3        3
```

<!-- category: Other -->
<!-- keywords: allroots -->
<!-- signatures: allroots(expr), allroots(eqn) -->
### Function: allroots (expr)

Calcula aproximações numéricas de raízes reais e complexas do
polinômio *expr* ou equação polinômial *eqn* de uma variável.



O sinalizador `polyfactor` quando `true` faz com que
`allroots` fatore o polinômio sobre os números reais se o
polinômio for real, ou sobre os números complexos, se o polinômio for
complexo.


`allroots` pode retornar resultados imprecisos no caso de multiplas raízes.
Se o polinômio for real, `allroots (%i*p)`) pode retornar
aproximações mais precisas que `allroots (p)`,
como `allroots` invoca um algorítmo diferente naquele caso.


`allroots` rejeita não-polinômios.  Isso requer que o numerador
após a classificação (`rat`’ing) poderá ser um polinômio, e isso requer que o
denominador seja quando muito um número complexo.  Com um resultado disso `allroots`
irá sempre retornar uma expressão equivalente (mas fatorada), se
`polyfactor` for `true`.


Para polinômios complexos um algorítmo por Jenkins e Traub é
usado (Algorithm 419, *Comm.  ACM*, vol.  15, (1972), p.  97).
Para polinômios reais o algorítmo usado é devido a Jenkins (Algorithm 493, *ACM TOMS*,
vol.  1, (1975), p.178).


Exemplos:










```maxima
(%i1) eqn: (1 + 2*x)^3 = 13.5*(1 + x^5);
                            3          5
(%o1)              (2 x + 1)  = 13.5 (x  + 1)
(%i2) soln: allroots (eqn);
(%o2) [x = .8296749902129361, x = - 1.015755543828121, 

x = .9659625152196369 %i - .4069597231924075, 

x = - .9659625152196369 %i - .4069597231924075, x = 1.0]
(%i3) for e in soln
        do (e2: subst (e, eqn), disp (expand (lhs(e2) - rhs(e2))));
                      - 3.5527136788005E-15

                     - 5.32907051820075E-15

         4.44089209850063E-15 %i - 4.88498130835069E-15

        - 4.44089209850063E-15 %i - 4.88498130835069E-15

                       3.5527136788005E-15

(%o3)                         done
(%i4) polyfactor: true$
(%i5) allroots (eqn);
(%o5) - 13.5 (x - 1.0) (x - .8296749902129361)

                           2
 (x + 1.015755543828121) (x  + .8139194463848151 x

 + 1.098699797110288)
```

<!-- category: Other -->
<!-- keywords: backsubst -->
<!-- signatures: backsubst -->
### Variable: backsubst

Valor padrão: `true`



Quando `backsubst` é `false`, evita substituições
em expressões anteriores após as equações terem sido triangularizadas.  Isso pode
ser de grande ajuda em problemas muito grandes onde substituição em expressões anteriores pode vir a causar
a geração de expressões extremamente largas.

<!-- category: Other -->
<!-- keywords: breakup -->
<!-- signatures: breakup -->
### Variable: breakup

Valor padrão: `true`


Quando `breakup` é `true`, `solve` expressa soluções
de equações cúbicas e quárticas em termos de subexpressões comuns,
que são atribuídas a rótulos de expressões intermediárias (`%t1`, `%t2`, etc.).
De outra forma, subexpressões comuns não são identificadas.


`breakup: true` tem efeito somente quando `programmode` é `false`.


Exemplos:



```maxima
(%i1) programmode: false$
(%i2) breakup: true$
(%i3) solve (x^3 + x^2 - 1);

                        sqrt(23)    25 1/3
(%t3)                  (--------- + --)
                        6 sqrt(3)   54
Solution:

                                      sqrt(3) %i   1
                                      ---------- - -
                sqrt(3) %i   1            2        2   1
(%t4)    x = (- ---------- - -) %t3 + -------------- - -
                    2        2            9 %t3        3

                                      sqrt(3) %i   1
                                    - ---------- - -
              sqrt(3) %i   1              2        2   1
(%t5)    x = (---------- - -) %t3 + ---------------- - -
                  2        2             9 %t3         3

                                   1     1
(%t6)                  x = %t3 + ----- - -
                                 9 %t3   3
(%o6)                    [%t4, %t5, %t6]
(%i6) breakup: false$
(%i7) solve (x^3 + x^2 - 1);
Solution:

             sqrt(3) %i   1
             ---------- - -
                 2        2        sqrt(23)    25 1/3
(%t7) x = --------------------- + (--------- + --)
             sqrt(23)    25 1/3    6 sqrt(3)   54
          9 (--------- + --)
             6 sqrt(3)   54

                                              sqrt(3) %i   1    1
                                           (- ---------- - -) - -
                                                  2        2    3

           sqrt(23)    25 1/3  sqrt(3) %i   1
(%t8) x = (--------- + --)    (---------- - -)
           6 sqrt(3)   54          2        2

                                            sqrt(3) %i   1
                                          - ---------- - -
                                                2        2      1
                                      + --------------------- - -
                                           sqrt(23)    25 1/3   3
                                        9 (--------- + --)
                                           6 sqrt(3)   54

            sqrt(23)    25 1/3             1             1
(%t9)  x = (--------- + --)    + --------------------- - -
            6 sqrt(3)   54          sqrt(23)    25 1/3   3
                                 9 (--------- + --)
                                    6 sqrt(3)   54
(%o9)                    [%t7, %t8, %t9]
```

<!-- category: Other -->
<!-- keywords: dimension -->
<!-- signatures: dimension(eqn), dimension(eqn_1, ..., eqn_n) -->
### Function: dimension (eqn)

`dimen` é um pacote de análise dimensional.
`load ("dimen")` chama esse pacote.
`demo ("dimen")` mostra uma cura demostração.

<!-- category: Other -->
<!-- keywords: dispflag -->
<!-- signatures: dispflag -->
### Variable: dispflag

Valor padrão: `true`



Se escolhida para `false` dentro de um `block` inibirá
a visualização da saída gerada pelas funções solve chamadas de
dentro de `block`.  Terminando `block` com um sinal de dolar, $, escolhe
`dispflag` para `false`.

<!-- category: Other -->
<!-- keywords: funcsolve -->
<!-- signatures: funcsolve(eqn, g(t)) -->
### Function: funcsolve (eqn, g(t))

Retorna `[g(t) = ...]`  ou `[]`, dependendo de existir
ou não uma função racional `g(t)` satisfazendo *eqn*,
que deve ser de primeira ordem, polinômio linear em (para esse caso) 
`g(t)` e `g(t+1)`



```maxima
(%i1) eqn: (n + 1)*f(n) - (n + 3)*f(n + 1)/(n + 1) = (n - 1)/(n + 2);
                            (n + 3) f(n + 1)   n - 1
(%o1)        (n + 1) f(n) - ---------------- = -----
                                 n + 1         n + 2
(%i2) funcsolve (eqn, f(n));

Equações dependentes eliminadas:  (4 3)
                                   n
(%o2)                f(n) = ---------------
                            (n + 1) (n + 2)
```


Atenção: essa é uma implementação muito rudimentar – muitas verificações de segurança
e obviamente generalizações estão ausêntes.

<!-- category: Other -->
<!-- keywords: globalsolve -->
<!-- signatures: globalsolve -->
### Variable: globalsolve

Valor padrão: `false`


When `globalsolve` for `true`,
variáveis para as quais as equações são resolvidas são atribuidas aos valores da solução encontrados por `linsolve`,
e por `solve` quando resolvendo duas ou mais equações lineares.


Quando `globalsolve` for `false`,
soluções encontradas por `linsolve` e por `solve` quando resolvendo duas ou mais equações lineares
são espressas como equações,
e as variáveis para as quais a equação foi resolvida não são atribuidas.


Quando resolvendo qualquer coisa outra que não duas equações lineares ou mais,
`solve` ignora `globalsolve`.
Outras funções que resolvem equações (e.g., `algsys`) sempre ignoram `globalsolve`.

    

Exemplos:



```maxima
(%i1) globalsolve: true$
(%i2) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t2)                        x : --
                                 7

                                   1
(%t3)                        y : - -
                                   7
(%o3)                     [[%t2, %t3]]
(%i3) x;
                               17
(%o3)                          --
                               7
(%i4) y;
                                 1
(%o4)                          - -
                                 7
(%i5) globalsolve: false$
(%i6) kill (x, y)$
(%i7) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t7)                        x = --
                                 7

                                   1
(%t8)                        y = - -
                                   7
(%o8)                     [[%t7, %t8]]
(%i8) x;
(%o8)                           x
(%i9) y;
(%o9)                           y
```

<!-- category: Other -->
<!-- keywords: ieqn -->
<!-- signatures: ieqn(ie, unk, tech, n, guess) -->
### Function: ieqn (ie, unk, tech, n, guess)

`inteqn` é um pacote para resolver equações com integrais.
`load ("inteqn")` carrega esse pacote.


*ie* é a equação integral; *unk* é a função desconhecida; *tech* é a
técnica a ser tentada nesses dados acima (*tech* = `first` significa: tente
a primeira técnica que achar uma solução; *tech* = `all` significa: tente todas a
técnicas aplicáveis); *n* é o número máximo de termos a serem usados de
`taylor`, `neumann`, `firstkindseries`, ou `fredseries` (isso é também o
número máximo de ciclos de recurssão para o método de diferenciação); *guess* é
o inicial suposto para `neumann` ou `firstkindseries`.


Valores padrão do segundo até o quinto parâmetro são:


*unk*: `p(x)`, onde *p* é a primeira função encontrada em um integrando
que é desconhecida para Maxima e *x* é a variável que ocorre como um
argumento para a primeira ocorrência de *p* achada fora de uma integral no
caso de equações `secondkind` , ou é somente outra variável
ao lado da variável de integração em equações `firstkind`.  Se uma
tentativa de procurar por *x* falha, o usuário será perguntado para suprir a
variável independente.


tech: `first`


n: 1


guess: `none` o que fará com que `neumann` e `firstkindseries` use
`f(x)` como uma suposição inicial.

<!-- category: Other -->
<!-- keywords: ieqnprint -->
<!-- signatures: ieqnprint -->
### Variable: ieqnprint

Valor padrão: `true`


`ieqnprint` governa o comportamento do resultado
retornado pelo comando `ieqn`.  Quando `ieqnprint` é
`false`, as listas retornadas pela função `ieqn` são da forma


   

[*solução*, *tecnica usada*, *nterms*, *sinalizador*]


onde *sinalizador* é retirado se a solução for exata.


De outra forma, isso é a
palavra `approximate` ou `incomplete` correspondendo à forma inexata ou
forma aberta de solução, respectivamente.  Se um método de série foi usado,
*nterms* fornece o número de termos usados (que poderá ser menor que os n
dados para `ieqn` se ocorrer um erro evita a geração de termos adicionais).

<!-- category: Other -->
<!-- keywords: lhs -->
<!-- signatures: lhs(expr) -->
### Function: lhs (expr)

Retorna o lado esquerdo (isto é, o primeiro argumento)
da expressão *expr*,
quando o operador de *expr*
for um dos operadores relacionais `< <= = # equal notequal >= >`,

um dos operadores de atribuição `:= ::= : ::`,
ou um operadro infixo definido pelo usuário, como declarado por meio de `infix`.


Quando *expr* for um átomo ou
seu operador for alguma coisa que não esses listados acima,
`lhs` retorna *expr*.


Veja também `rhs`.


Exemplos:

















```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [lhs (aa < bb), lhs (aa <= bb), lhs (aa >= bb), lhs (aa > bb)];
(%o4)                   [aa, aa, aa, aa]
(%i5) [lhs (aa = bb), lhs (aa # bb), lhs (equal (aa, bb)), lhs (notequal (aa, bb))];
(%o5)                   [aa, aa, aa, aa]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [lhs (e1), lhs (e2), lhs (e3), lhs (e4)];
(%o10)               [foo(x), bar(y), x, x]
(%i11) infix ("][");
(%o11)                         ][
(%i12) lhs (aa ][ bb);
(%o12)                         aa
```

<!-- category: Other -->
<!-- keywords: linsolve -->
<!-- signatures: linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

Resolve a lista de
equações lineares simultâneas para a lista de variáveis.  As expressões
devem ser cada uma polinômios nas variáveis e podem ser equações.


Quando `globalsolve` é `true` então variáveis que foram resolvidas
serão escolhidas para a solução do conjunto de equações simultâneas.


Quando `backsubst` é `false`, `linsolve`
não realiza substituição em equações anteriores após
as equações terem sido triangularizadas.  Isso pode ser necessário em problemas
muito grandes onde substituição em equações anteriores poderá causar a geração de
expressões extremamente largas.


Quando `linsolve_params` for `true`,
`linsolve` também gera símbolos `%r`
usados para representar parâmetros arbitrários descritos no manual sob
`algsys`.
De outra forma, `linsolve` resolve um menor-determinado sistema de
equações com algumas variáveis expressas em termos de outras.


Quando `programmode` for `false`,
`linsolve` mostra a solução com expressões intermediárias com rótulos (`%t`),
e retorna a lista de rótulos.




















```maxima
(%i1) e1: x + z = y;
(%o1)                       z + x = y
(%i2) e2: 2*a*x - y = 2*a^2;
                                       2
(%o2)                   2 a x - y = 2 a
(%i3) e3: y - 2*z = 2;
(%o3)                      y - 2 z = 2
(%i4) [globalsolve: false, programmode: true];
(%o4)                     [false, true]
(%i5) linsolve ([e1, e2, e3], [x, y, z]);
(%o5)            [x = a + 1, y = 2 a, z = a - 1]
(%i6) [globalsolve: false, programmode: false];
(%o6)                    [false, false]
(%i7) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t7)                       z = a - 1

(%t8)                        y = 2 a

(%t9)                       x = a + 1
(%o9)                    [%t7, %t8, %t9]
(%i9) ''%;
(%o9)            [z = a - 1, y = 2 a, x = a + 1]
(%i10) [globalsolve: true, programmode: false];
(%o10)                    [true, false]
(%i11) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t11)                      z : a - 1

(%t12)                       y : 2 a

(%t13)                      x : a + 1
(%o13)                 [%t11, %t12, %t13]
(%i13) ''%;
(%o13)           [z : a - 1, y : 2 a, x : a + 1]
(%i14) [x, y, z];
(%o14)                 [a + 1, 2 a, a - 1]
(%i15) [globalsolve: true, programmode: true];
(%o15)                    [true, true]
(%i16) linsolve ([e1, e2, e3], '[x, y, z]);
(%o16)           [x : a + 1, y : 2 a, z : a - 1]
(%i17) [x, y, z];
(%o17)                 [a + 1, 2 a, a - 1]
```

<!-- category: Other -->
<!-- keywords: linsolve_params -->
<!-- signatures: linsolve_params -->
### Variable: linsolve_params

Valor padrão: `true`


Quando `linsolve_params` é `true`, `linsolve` também gera
os símbolos `%r` usados para representar parâmetros arbitrários descritos no
manual sob `algsys`.
De outra forma, `linsolve` resolve um menor-determinado sistema de
equações com algumas variáveis expressas em termos e outras.

<!-- category: Other -->
<!-- keywords: linsolvewarn -->
<!-- signatures: linsolvewarn -->
### Variable: linsolvewarn

Valor padrão: `true`


Quando `linsolvewarn` é `true`,
`linsolve` imprime uma mensagem "Dependent equações eliminated".

<!-- category: Other -->
<!-- keywords: multiplicities -->
<!-- signatures: multiplicities -->
### Variable: multiplicities

Valor padrão: `not_set_yet`


`multiplicities` é escolhida para uma lista de
multiplicidades das soluções individuais retornadas por `solve` ou
`realroots`.

<!-- category: Other -->
<!-- keywords: nroots -->
<!-- signatures: nroots(p, low, high) -->
### Function: nroots (p, low, high)

Retorna o número de raízes reais do polinômio 
real de uma única variável *p* no intervalo semi-aberto
`(low, high]`.
Uma extremidade do intervalo podem ser `minf` ou `inf`.
infinito e mais infinito.


`nroots` usa o método das sequuências de Sturm.



```maxima
(%i1) p: x^10 - 2*x^4 + 1/2$
(%i2) nroots (p, -6, 9.1);
(%o2)                           4
```

<!-- category: Other -->
<!-- keywords: nthroot -->
<!-- signatures: nthroot(p, n) -->
### Function: nthroot (p, n)

Onde p é um polinômio com coeficientes inteiros e
n é um inteiro positivo retorna q, um polinômio sobre os inteiros, tal
que q^n=p ou imprime uma mensagem de erro indicando que p não é uma potência n-ésima
perfeita.  Essa rotina é mais rápida que `factor` ou mesmo `sqfr`.

<!-- category: Other -->
<!-- keywords: programmode -->
<!-- signatures: programmode -->
### Variable: programmode

Valor padrão: `true`


Quando `programmode` é `true`,
`solve`, `realroots`, `allroots`, e `linsolve`
retornam soluções como elementos em uma lista.

(Exceto quando `backsubst` é escolhido para `false`, nesse caso
`programmode: false` é assumido.)


Quando `programmode` é `false`, `solve`, etc.
cria rótulos de expressões intermediárias
`%t1`, `t2`, etc., e atribui as soluções para eles.

<!-- category: Other -->
<!-- keywords: realonly -->
<!-- signatures: realonly -->
### Variable: realonly

Valor padrão: `false`


Quando `realonly` é `true`, `algsys` retorna somente
aquelas soluções que estão livres de `%i`.

<!-- category: Other -->
<!-- keywords: realroots -->
<!-- signatures: realroots(expr, bound), realroots(eqn, bound), realroots(expr), realroots(eqn) -->
### Function: realroots (expr, bound)

Calcula aproximações racionais das raízes reais da expressão polinomial *expr*
ou da equação polinomial *eqn* de uma variável,
dentro de uma tolerância de *bound*.
coeficientes de *expr* ou de *eqn* devem ser números literais;
constantes símbolo tais como `%pi` são rejeitadas.


`realroots` atribui as multiplicidades das raízes que encontrar
para a variável global `multiplicities`.


`realroots` constrói uma sequência de Sturm para delimitar cada raíz,
e então palica a bisecção para redefinir as aproximações.
Todos os coeficientes são convertidos para os equivalentes racionais antes da busca por raízes,
e cálculos são realizados por meio de aritmética racional exata.
Mesmo se alguns coeficientes forem números em ponto flutuante,
os resultados são racionais (a menos que forçados a números em ponto flutuante por `float` ou por `numer` flags).


Quando *bound* for menor que 1, todas as raízes inteiras são encontradas exatamente.
Quando *bound* não for especificado, será assumido como sendo igual à variável globa `rootsepsilon`.


Quando a varável global `programmode` for `true`,
`realroots` retorna uma lista da forma `[x = x_1, x = x_2, ...]`.
Quando `programmode` for `false`,
`realroots` cria rótulos de expressões intermediárias `%t1`, `%t2`, ...,
atribui os resultados a eles, e retorna a lista de rótulos.


Exemplos:








```maxima
(%i1) realroots (-1 - x + x^5, 5e-6);
                               612003
(%o1)                     [x = ------]
                               524288
(%i2) ev (%[1], float);
(%o2)                 x = 1.167303085327148
(%i3) ev (-1 - x + x^5, %);
(%o3)                - 7.396496210176905E-6
```








```maxima
(%i1) realroots (expand ((1 - x)^5 * (2 - x)^3 * (3 - x)), 1e-20);
(%o1)                 [x = 1, x = 2, x = 3]
(%i2) multiplicities;
(%o2)                       [5, 3, 1]
```

<!-- category: Other -->
<!-- keywords: rhs -->
<!-- signatures: rhs(expr) -->
### Function: rhs (expr)

Retorna o lado direito (isto é, o segundo argumento)
da expressão *expr*,
quando o operador de *expr*
for um dos operadores relacionais `< <= = # equal notequal >= >`,

um dos operadores de atribuição `:= ::= : ::`,
ou um operador binário infixo definido pelo usuário, como declarado por meio de `infix`.


Quando *expr* for um étomo ou
seu operadro for alguma coisa que não esses listados acima,
`rhs` retorna 0.


Veja também `lhs`.


Exemplos:

















```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [rhs (aa < bb), rhs (aa <= bb), rhs (aa >= bb), rhs (aa > bb)];
(%o4)                   [bb, bb, bb, bb]
(%i5) [rhs (aa = bb), rhs (aa # bb), rhs (equal (aa, bb)), rhs (notequal (aa, bb))];
(%o5)                   [bb, bb, bb, bb]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [rhs (e1), rhs (e2), rhs (e3), rhs (e4)];
(%o10)                  [2 x, 3 y, y, y]
(%i11) infix ("][");
(%o11)                         ][
(%i12) rhs (aa ][ bb);
(%o12)                         bb
```

<!-- category: Other -->
<!-- keywords: rootsconmode -->
<!-- signatures: rootsconmode -->
### Variable: rootsconmode

Valor padrão: `true`


`rootsconmode` governa o comportamento do comando
`rootscontract`.  Veja `rootscontract` para detalhes.

<!-- category: Other -->
<!-- keywords: rootscontract -->
<!-- signatures: rootscontract(expr) -->
### Function: rootscontract (expr)

Converte produtos de raízes em raízes de produtos.
Por exemplo,
`rootscontract (sqrt(x)*y^(3/2))` retorna `sqrt(x*y^3)`.


Quando `radexpand` é `true` e `domain` é `real`,
`rootscontract` converte `abs` em `sqrt`, e.g.,
`rootscontract (abs(x)*sqrt(y))` retorna `sqrt(x^2*y)`.


Existe uma opção `rootsconmode`
afetando `rootscontract` como segue:



```maxima
Problem            Value of        Result of applying
                  rootsconmode        rootscontract
      
x^(1/2)*y^(3/2)      false          (x*y^3)^(1/2)
x^(1/2)*y^(1/4)      false          x^(1/2)*y^(1/4)
x^(1/2)*y^(1/4)      true           (x*y^(1/2))^(1/2)
x^(1/2)*y^(1/3)      true           x^(1/2)*y^(1/3)
x^(1/2)*y^(1/4)      all            (x^2*y)^(1/4)
x^(1/2)*y^(1/3)      all            (x^3*y^2)^(1/6)
```


Quando `rootsconmode` é `false`, `rootscontract` contrai somente como relação a expoentes
de número racional cujos denominadores são os mesmos.  A chave para os exemplos
`rootsconmode: true` é simplesmente que 2 divides 4 mas não 
divide 3.  `rootsconmode: all` envolve pegar o menor multiplo comum
dos denominadores dos expoentes.


`rootscontract` usa `ratsimp` em uma maneira similar a `logcontract`.


Exemplos:


















```maxima
(%i1) rootsconmode: false$
(%i2) rootscontract (x^(1/2)*y^(3/2));
                                   3
(%o2)                      sqrt(x y )
(%i3) rootscontract (x^(1/2)*y^(1/4));
                                   1/4
(%o3)                     sqrt(x) y
(%i4) rootsconmode: true$
(%i5) rootscontract (x^(1/2)*y^(1/4));
(%o5)                    sqrt(x sqrt(y))
(%i6) rootscontract (x^(1/2)*y^(1/3));
                                   1/3
(%o6)                     sqrt(x) y
(%i7) rootsconmode: all$
(%i8) rootscontract (x^(1/2)*y^(1/4));
                              2   1/4
(%o8)                       (x  y)
(%i9) rootscontract (x^(1/2)*y^(1/3));
                             3  2 1/6
(%o9)                      (x  y )
(%i10) rootsconmode: false$
(%i11) rootscontract (sqrt(sqrt(x) + sqrt(1 + x))
                    *sqrt(sqrt(1 + x) - sqrt(x)));
(%o11)                          1
(%i12) rootsconmode: true$
(%i13) rootscontract (sqrt(5 + sqrt(5)) - 5^(1/4)*sqrt(1 + sqrt(5)));
(%o13)                          0
```

<!-- category: Other -->
<!-- keywords: rootsepsilon -->
<!-- signatures: rootsepsilon -->
### Variable: rootsepsilon

Valor padrão: 1.0e-7


`rootsepsilon` é a tolerância que estabelece o
intervalo de conficência para as raízes achadas pela função `realroots`.

<!-- category: Other -->
<!-- keywords: solve -->
<!-- signatures: solve(expr, x), solve(expr), solve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: solve (expr, x)

Resolve a equação algébrica *expr* para a variável
*x* e retorna uma lista de equações solução em *x*.  Se *expr* não é uma
equação, a equação `expr = 0` é assumida em seu lugar.
*x* pode ser uma função (e.g. `f(x)`), ou outra expressão não atômica
exceto uma adição ou um produto.  *x* pode ser omitido se *expr* contém somente uma
variável.  *expr* pode ser uma expressão racional, e pode conter
funções trigonométricas, exponenciais, etc.


O seguinte método é usado:


Tome *E* sendo a expressão e *X* sendo a variável.  Se *E* é linear em *X*
então isso é trivialmente resolvido para *X*.  De outra forma se *E* é da forma
`A*X^N + B` então o resultado é `(-B/A)^1/N)` vezes as `N`’ésimas raízes da
unidade.


Se *E* não é linear em *X* então o máximo divisor comum (mdc) dos expoentes de *X* em *E* (digamos
*N*) é dividido dentro dos expoentes e a multiplicidade das raízes é
multiplicada por *N*.  Então `solve` é chamada novamente sobre o resultado.
Se *E* for dada em fatores então `solve` é chamada sobre cada um dos fatores.  Finalmente
`solve` usará as fórmulas quadráticas, cúbicas, ou quárticas onde
necessário.


No caso onde *E* for um polinômio em alguma função de variável a ser
resolvida, digamos `F(X)`, então isso é primeiro resolvida para `F(X)` (chama o
resultado *C*), então a equação `F(X)=C` pode ser resolvida para *X* fornecendo o
inverso da função *F* que é conhecida.


`breakup` se `false` fará com que `solve` expresse as soluções de
equações cúbicas ou quárticas como expressões simples ao invés de como feito
em cima de várias subexpressões comuns que é o padrão.


`multiplicities` - será escolhido para uma lista de multiplicidades de
soluções individuais retornadas por `solve`, `realroots`, ou `allroots`.
Tente `apropos (solve)` para os comutadores que afetam `solve`.  `describe` pode
então ser usada sobre o nome do comutador individual se seu proprósito não é
claro.


`solve ([eqn_1, ..., eqn_n], [x_1, ..., x_n])`
resolve um sistema de equações polinomiais
(lineares ou não-lineares) simultâneas por chamada a `linsolve` ou
`algsys` e retorna uma lista de listas solução nas variáveis.  No
caso de `linsolve` essa lista conterá uma lista simples de
soluções.  Isso pega duas listas como argumentos.  A primeira lista
representa as equações a serem resolvidas; a segunda lista é a
lista de desconhecidos a ser determinada.  Se o número total de
variáveis nas equações é igual ao número de equações, a
segunda lista-argumento pode ser omitida.  Para sistemas lineares se as dadas
equações não são compatíveis, a mensagem `inconsistent` será
mostrada (veja o comutador `solve_inconsistent_error` ); se não existe
solução única, então `singular` será mostrado.


Quando `programmode` for `false`,
`solve` mostra soluções com rótulos de expressões intermediárias (`%t`),
e retorna a lista de rótulos.


Quando `globalsolve` for `true` e o problema for resolver duas ou mais equações lineares,
cada variável para a qual a equação for resolvida é associada a seu valor na solução das equações.


Exemplos:

















```maxima
(%i1) solve (asin (cos (3*x))*(f(x) - 1), x);

SOLVE is using arc-trig functions to get a solution.
Some solutions will be lost.
                            %pi
(%o1)                  [x = ---, f(x) = 1]
                             6
(%i2) ev (solve (5^f(x) = 125, f(x)), solveradcan);
                                log(125)
(%o2)                   [f(x) = --------]
                                 log(5)
(%i3) [4*x^2 - y^2 = 12, x*y - x = 2];
                      2    2
(%o3)             [4 x  - y  = 12, x y - x = 2]
(%i4) solve (%, [x, y]);
(%o4) [[x = 2, y = 2], [x = .5202594388652008 %i

 - .1331240357358706, y = .0767837852378778

 - 3.608003221870287 %i], [x = - .5202594388652008 %i

 - .1331240357358706, y = 3.608003221870287 %i

 + .0767837852378778], [x = - 1.733751846381093, 

y = - .1535675710019696]]
(%i5) solve (1 + a*x + x^3, x);
                                       3
              sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(%o5) [x = (- ---------- - -) (--------------- - -)
                  2        2      6 sqrt(3)      2

        sqrt(3) %i   1
       (---------- - -) a
            2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

                          3
 sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(---------- - -) (--------------- - -)
     2        2      6 sqrt(3)      2

         sqrt(3) %i   1
      (- ---------- - -) a
             2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

         3
 sqrt(4 a  + 27)   1 1/3               a
(--------------- - -)    - --------------------------]
    6 sqrt(3)      2                  3
                              sqrt(4 a  + 27)   1 1/3
                           3 (--------------- - -)
                                 6 sqrt(3)      2
(%i6) solve (x^3 - 1);
             sqrt(3) %i - 1        sqrt(3) %i + 1
(%o6)   [x = --------------, x = - --------------, x = 1]
                   2                     2
(%i7) solve (x^6 - 1);
           sqrt(3) %i + 1      sqrt(3) %i - 1
(%o7) [x = --------------, x = --------------, x = - 1, 
                 2                   2

                     sqrt(3) %i + 1        sqrt(3) %i - 1
               x = - --------------, x = - --------------, x = 1]
                           2                     2
(%i8) ev (x^6 - 1, %[1]);
                                      6
                      (sqrt(3) %i + 1)
(%o8)                 ----------------- - 1
                             64
(%i9) expand (%);
(%o9)                           0
(%i10) x^2 - 1;
                              2
(%o10)                       x  - 1
(%i11) solve (%, x);
(%o11)                  [x = - 1, x = 1]
(%i12) ev (%th(2), %[1]);
(%o12)                          0
```

<!-- category: Other -->
<!-- keywords: solve_inconsistent_error -->
<!-- signatures: solve_inconsistent_error -->
### Variable: solve_inconsistent_error

Valor padrão: `true`


Quando `solve_inconsistent_error` for `true`, `solve` e
`linsolve` resultam em erro se as equações a serem resolvidas forem inconsistentes.


Se `false`, `solve` e `linsolve` retornam uma lista vazia `[]` 
se as equações forem inconsistentes.


Exemplo:



```maxima
(%i1) solve_inconsistent_error: true$
(%i2) solve ([a + b = 1, a + b = 2], [a, b]);
Inconsistent equações:  (2)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i3) solve_inconsistent_error: false$
(%i4) solve ([a + b = 1, a + b = 2], [a, b]);
(%o4)                          []
```

<!-- category: Other -->
<!-- keywords: solvedecomposes -->
<!-- signatures: solvedecomposes -->
### Variable: solvedecomposes

Valor padrão: `true`


Quando `solvedecomposes` é `true`, `solve` chama
`polydecomp` se perguntado para resolver polinômios.

<!-- category: Other -->
<!-- keywords: solveexplicit -->
<!-- signatures: solveexplicit -->
### Variable: solveexplicit

Valor padrão: `false`


Quando `solveexplicit` é `true`, inibe `solve` de
retornar soluções implícitas, isto é, soluções da forma `F(x) = 0`
onde `F` é alguma função.

<!-- category: Other -->
<!-- keywords: solvefactors -->
<!-- signatures: solvefactors -->
### Variable: solvefactors

Valor padrão: `true`



Quando `solvefactors` é `false`, `solve` não tenta
fatorar a expressão.  O `false` escolhido pode ser desejado em alguns casos
onde a fatoração não é necessária.

<!-- category: Other -->
<!-- keywords: solvenullwarn -->
<!-- signatures: solvenullwarn -->
### Variable: solvenullwarn

Valor padrão: `true`


Quando `solvenullwarn` é `true`, 
`solve` imprime uma mensagem de alerta se chamada com ou uma lista equação ou uma variável lista nula.
Por exemplo, `solve ([], [])` imprimirá duas mensagens de alerta e retorna `[]`.

<!-- category: Other -->
<!-- keywords: solveradcan -->
<!-- signatures: solveradcan -->
### Variable: solveradcan

Valor padrão: `false`


Quando `solveradcan` é `true`, `solve` chama `radcan`
que faz `solve` lento mas permitirá certamente que problemas
contendo exponeniais e logarítmos sejam resolvidos.

<!-- category: Other -->
<!-- keywords: solvetrigwarn -->
<!-- signatures: solvetrigwarn -->
### Variable: solvetrigwarn

Valor padrão: `true`



Quando `solvetrigwarn` é `true`,
`solve` pode imprimir uma mensagem dizendo que está usando funções
trigonométricas inversas para resolver a equação, e desse modo perdendo
soluções.

