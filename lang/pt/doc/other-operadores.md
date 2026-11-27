## Operadores

<!-- category: Other -->
<!-- keywords: ! -->
<!-- signatures: ! -->
### Function: !

O operador factorial.
Para qualquer número complexo `x` (incluíndo números inteiros, racionais, e reais) excepto para
inteiros negativos, `x!` é definido como `gamma(x+1)`.


Para um inteiro `x`, `x!` simplifica para o produto de inteiros de 1 a `x` inclusive.
`0!` simplifica para 1.
Para um número em ponto flutuante `x`, `x!` simplifica para o valor de `gamma (x+1)`.
Para `x` igual a `n/2` onde `n` é um inteiro ímpar,
`x!` simplifica para um factor racional vezes `sqrt (%pi)`
(uma vez que `gamma (1/2)` é igual a `sqrt (%pi)`).
Se `x` for qualquer outra coisa,
`x!` não é simplificado.


As variáveis
`factlim`, `minfactorial`, e `factcomb` controlam a simplificação
de expressões contendo factoriais.


As funções `gamma`, `bffac`, e `cbffac`
são variedades da função `gamma`. 
`makegamma` substitui `gamma` para funções relacionadas a factoriais.


Veja também `binomial`.


O factorial de um inteiro, inteiro dividido por dois, ou argumento em ponto flutuante é simplificado
a menos que o operando seja maior que `factlim`.







```maxima
(%i1) factlim : 10;
(%o1)                          10
(%i2) [0!, (7/2)!, 4.77!, 8!, 20!];
+            105 sqrt(%pi)
+(%o2)   [1, -------------, 81.44668037931199, 40320, 20!]
+                 16
```


O factorial de um número complexo, constante conhecida, ou expressão geral não é simplificado.
Ainda assim pode ser possível simplificar o factorial após avaliar o operando.







```maxima
(%i1) [(%i + 1)!, %pi!, %e!, (cos(1) + sin(1))!];
(%o1)      [(%i + 1)!, %pi!, %e!, (sin(1) + cos(1))!]
(%i2) ev (%, numer, %enumer);
(%o2) [(%i + 1)!, 7.188082728976037, 4.260820476357, 
                                               1.227580202486819]
```


O factorial de um símbolo não associado não é simplificado.







```maxima
(%i1) kill (foo);
(%o1)                         done
(%i2) foo!;
(%o2)                         foo!
```


Factoriais são simplificados, não avaliados.
Dessa forma `x!` pode ser substituído mesmo em uma expressão com apóstrofo.






```maxima
(%i1) '([0!, (7/2)!, 4.77!, 8!, 20!]);
          105 sqrt(%pi)
(%o1) [1, -------------, 81.44668037931199, 40320, 
               16
                                             2432902008176640000]
```

<!-- category: Other -->
<!-- keywords: !! -->
<!-- signatures: !! -->
### Function: !!

O operador de duplo factorial.


Para um número inteiro, número em ponto flutuante, ou número racional `n`,
`n!!` avalia para o produto `n (n-2) (n-4) (n-6) ... (n - 2 (k-1))`
onde `k` é igual a `entier (n/2)`,
que é, o maior inteiro menor que ou igual a `n/2`.
Note que essa definição não coincide com outras definições publicadas
para argumentos que não são inteiros.



Para um inteiro par (ou ímpar) `n`, `n!!` avalia para o produto de
todos os inteiros consecutivos pares (ou ímpares) de 2 (ou 1) até `n` inclusive.


Para um argumento `n` que não é um número inteiro, um número em ponto flutuante, ou um número racional,
`n!!` retorna uma forma substantiva `genfact (n, n/2, 2)`.

<!-- category: Other -->
<!-- keywords: # -->
<!-- signatures: # -->
### Function: #

Representa a negação da igualdade sintática `=`.


Note que pelo facto de as regras de avaliação de expressões predicadas
(em particular pelo facto de `not expr` fazer com que ocorra a avaliação de *expr*),
a forma `not a = b` não é equivalente à forma `a # b` em alguns casos.


Note que devido às regras para avaliação de expressões predicadas
(em particular devido a `not expr` fazer com que a avaliação de *expr* ocorra),
`not a = b` é equivalente a `is(a # b)`,
em lugar de ser equivalente a `a # b`.


Exemplos:










```maxima
(%i1) a = b;
(%o1)                         a = b
(%i2) é (a = b);
(%o2)                         false
(%i3) a # b;
(%o3)                         a # b
(%i4) not a = b;
(%o4)                         true
(%i5) é (a # b);
(%o5)                         true
(%i6) é (not a = b);
(%o6)                         true
```

<!-- category: Other -->
<!-- keywords: ** -->
<!-- signatures: ** -->
### Function: **

Operador de exponenciação.
Maxima reconhece `**` como o mesmo operador que `^` em entrada,
e `**` é mostrado como `^` em saída unidimensional,
ou colocando o expoente  como sobrescrito em saída bidimensional.


A função `fortran` mostra o operador de exponenciação com como `**`,
independente de a entrada ter sido na forma `**` ou a forma `^`.


Exemplos:









```maxima
(%i1) is (a**b = a^b);
(%o1)                         true
(%i2) x**y + x^z;
                              z    y
(%o2)                        x  + x
(%i3) string (x**y + x^z);
(%o3)                        x^z+x^y
(%i4) fortran (x**y + x^z);
      x**z+x**y
(%o4)                         done
```

<!-- category: Other -->
<!-- keywords: +, -, *, /, ^ -->
<!-- signatures: -, *, /, ^ -->
### Function: +

Os símbolos `+` `*` `/` e `^` representam
adição, multiplicação, divisão, e exponenciação, respectivamente.
O nome desses operadores são `"+"` `"*"` `"/"` e `"^"`,
os quais podem aparecer em lugares onde o nome da função ou operador é requerido.


Os símbolos `+` e `-` representam a adição unária e a negação unária, respectivamente,
e os nomes desses operadores são `"+"` e `"-"`, respectivamente.


A subtração `a - b` é representada dentro do Maxima como a adição, `a + (- b)`.
Expressões tais como `a + (- b)` são mostradas como subtração.
Maxima reconhece `"-"` somente como o nome do operador unário de negação,
e não como o nome do operador binário de subração.


A divisão `a / b` é representada dentro do Maxima como multiplicação, `a * b^(- 1)`.
Expressões tais como `a * b^(- 1)` são mostradas como divisão.
Maxima reconhece `"/"` como o nome do operador de divisão.


A adição e a multiplicação são operadores enários e comutativos.
a divisão e a exponenciação são operadores binários e não comutativos.


Maxima ordena os operandos de operadores não comutativos para construir uma representação canónica.
Para armazenamento interno, a ordem é determinada por `orderlessp`.
Para mostrar na tela, a ordem para adição é determinada por `ordergreatp`,
e para a multiplicação, a ordem é a mesma da ordenação para armazenamento interno.


Computações aritiméticas são realizadas sobre números literais
(inteiro, racionais, números comuns em ponto flutuante, e grandes números em ponto flutuante de dupla precisão).
Execto a exponenciação, todas as operações aritméticas sobre números são simplificadas para números.
A exponenciação é simplificada para um número se ou o operando é um número comum em ponto flutuante ou um grande número em ponto flutuante de dupla precisão
ou se o resultado for um inteiro exato ou um racional exato;
de outra forma uma exponenciação pode ser simplificada para `sqrt` ou outra exponenciação ou permanecer inalterada.


A propagação de números em ponto flutuante aplica-se a computações aritiméticas:
Se qualquer operando for um grande número em ponto flutuante, o resultado é um grande número em ponto flutuante;
de outra forma, se qualquer operando for um número em ponto flutuante comum, o resultado é um número comum em ponto flutuante;
de outra forma, se os operandos forem racioanis ou inteiros e o resultado será um racional ou inteiro.


Computaçãoes aritiméticas são uma simplificação, não uma avaliação.
Dessa forma a aritmética é realizada em  expressões com apóstrofo (mas simplificadas).


Operações aritméticas são aplicadas elemento-por-elemento
para listas quando a variável global `listarith` for `true`,
e sempre aplicada elemento-por-elemento para matrizes.
Quando um operando for uma lista ou uma matriz e outro for um operando de algum outro tipo,
o outro operando é combinado com cada um dos elementos da lista ou matriz.


Exemplos:


Adição e multiplicação são opeadores enários comutativos.
Maxima ordena os operandos para construir uma representação canónica.
Os nomes desses operadores são `"+"` e `"*"`.











```maxima
(%i1) c + g + d + a + b + e + f;
(%o1)               g + f + e + d + c + b + a
(%i2) [op (%), args (%)];
(%o2)              [+, [g, f, e, d, c, b, a]]
(%i3) c * g * d * a * b * e * f;
(%o3)                     a b c d e f g
(%i4) [op (%), args (%)];
(%o4)              [*, [a, b, c, d, e, f, g]]
(%i5) apply ("+", [a, 8, x, 2, 9, x, x, a]);
(%o5)                    3 x + 2 a + 19
(%i6) apply ("*", [a, 8, x, 2, 9, x, x, a]);
                                 2  3
(%o6)                       144 a  x
```


Divisão e exponenciação são operadores binários e não comutativos.
Os nomes desses operadores são `"/"` e `"^"`.








```maxima
(%i1) [a / b, a ^ b];
                              a   b
(%o1)                        [-, a ]
                              b
(%i2) [map (op, %), map (args, %)];
(%o2)              [[/, ^], [[a, b], [a, b]]]
(%i3) [apply ("/", [a, b]), apply ("^", [a, b])];
                              a   b
(%o3)                        [-, a ]
                              b
```


Subtração e divisão são representados internamente
em termos de adição e multiplicação, respectivamente.







```maxima
(%i1) [inpart (a - b, 0), inpart (a - b, 1), inpart (a - b, 2)];
(%o1)                      [+, a, - b]
(%i2) [inpart (a / b, 0), inpart (a / b, 1), inpart (a / b, 2)];
                                   1
(%o2)                       [*, a, -]
                                   b
```


Cálculos são realizados sobre números lterais.
A propagação de números em poto flutuante aplica-se.







```maxima
(%i1) 17 + b - (1/2)*29 + 11^(2/4);
                                       5
(%o1)                   b + sqrt(11) + -
                                       2
(%i2) [17 + 29, 17 + 29.0, 17 + 29b0];
(%o2)                   [46, 46.0, 4.6b1]
```


Computações aritméticas são uma simplificação, não uma avaliação.









```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) '(17 + 29*11/7 - 5^3);
                              29 11    3
(%o2)                    17 + ----- - 5
                                7
(%i3) simp : true;
(%o3)                         true
(%i4) '(17 + 29*11/7 - 5^3);
                                437
(%o4)                         - ---
                                 7
```


A aritmética é realizada elemento-por-elemento para listas lists (dependendo de `listarith`) e dependendo de matrizes.













```maxima
(%i1) matrix ([a, x], [h, u]) - matrix ([1, 2], [3, 4]);
                        [ a - 1  x - 2 ]
(%o1)                   [              ]
                        [ h - 3  u - 4 ]
(%i2) 5 * matrix ([a, x], [h, u]);
                          [ 5 a  5 x ]
(%o2)                     [          ]
                          [ 5 h  5 u ]
(%i3) listarith : false;
(%o3)                         false
(%i4) [a, c, m, t] / [1, 7, 2, 9];
                          [a, c, m, t]
(%o4)                     ------------
                          [1, 7, 2, 9]
(%i5) [a, c, m, t] ^ x;
                                      x
(%o5)                     [a, c, m, t]
(%i6) listarith : true;
(%o6)                         true
(%i7) [a, c, m, t] / [1, 7, 2, 9];
                              c  m  t
(%o7)                     [a, -, -, -]
                              7  2  9
(%i8) [a, c, m, t] ^ x;
                          x   x   x   x
(%o8)                   [a , c , m , t ]
```

<!-- category: Other -->
<!-- keywords: . -->
<!-- signatures: . -->
### Function: .

O operador ponto, para multiplicação (não comutativa) de matrizes.
Quando "." é usado com essa finalidade, espaços devem ser colocados em ambos os lados desse
operador, e.g. A . B.  Isso distingue o operador ponto plenamente de um ponto decimal em
um número em ponto flutuante.


Veja também
`dot`,
`dot0nscsimp`,
`dot0simp`,
`dot1simp`,
`dotassoc`,
`dotconstrules`,
`dotdistrib`,
`dotexptsimp`,
`dotident`,
e
`dotscrules`.

<!-- category: Other -->
<!-- keywords: : -->
<!-- signatures: : -->
### Function: :

O operador de atribuição.  E.g. A:3 escolhe a variável A para 3.

<!-- category: Other -->
<!-- keywords: :: -->
<!-- signatures: :: -->
### Function: ::

Operador de atribuição.  :: atribui o valor da expressão
em seu lado direito para o valor da quantidade na sua esquerda, que pode
avaliar para uma variável atomica ou variável subscrita.

<!-- category: Other -->
<!-- keywords: ::= -->
<!-- signatures: ::= -->
### Function: ::=

Operador de definição de função de macro.
`::=` define uma função (chamada uma "macro" por razões históricas)
que coloca um apóstrofo em seus argumentos (evitando avaliação),
e a expressão que é retornada (chamada a "expansão de macro")
é avaliada no contexto a partir do qual a macro foi chamada.
Uma função de macro é de outra forma o mesmo que uma função comum.


`macroexpand` retorna uma expansão de macro (sem avaliar a expansão).
`macroexpand (foo (x))` seguida por `''%` é equivalente a `foo (x)`
quando `foo` for uma função de macro.


`::=` coloca o nome da nova função de macro dentro da lista global `macros`.
`kill`, `remove`, e `remfunction` desassocia definições de função de macro
e remove nomes de `macros`.


`fundef` e `dispfun` retornam respectivamente uma definição de função de macro
e uma atribuição dessa definição a um rótulo, respectivamente.


Funções de macro comumente possuem expressões `buildq` e
`splice` para construir uma expressão,
que é então avaliada.


Exemplos


Uma função de macro coloca um apóstrofo em seus argumentos evitando então a avaliação,
então mensagem (1) mostra `y - z`, não o valor de `y - z`.
A expansão de macro (a expressão com apóstrofo `'(print ("(2) x is equal to", x))`
é avaliada no contexto a partir do qual a macro for chamada,
mostrando a mensagem (2).










```maxima
(%i1) x: %pi;
(%o1)                          %pi
(%i2) y: 1234;
(%o2)                         1234
(%i3) z: 1729 * w;
(%o3)                        1729 w
(%i4) printq1 (x) ::= block (print ("(1) x é igual a", x), '(print ("(2) x é igual a", x)));
(%o4) printq1(x) ::= block(print("(1) x é igual a", x), 
                                '(print("(2) x é igual a", x)))
(%i5) printq1 (y - z);
(1) x é igual a y - z 
(2) x é igual a %pi 
(%o5)                          %pi
```


Uma função comum avalia seus argumentos, então message (1) mostra o valor de `y - z`.
O valor de retorno não é avaliado, então mensagem (2) não é mostrada
até a avaliação explícita `''%`.











```maxima
(%i1) x: %pi;
(%o1)                          %pi
(%i2) y: 1234;
(%o2)                         1234
(%i3) z: 1729 * w;
(%o3)                        1729 w
(%i4) printe1 (x) := block (print ("(1) x é igual a", x), '(print ("(2) x é igual a", x)));
(%o4) printe1(x) := block(print("(1) x é igual a", x), 
                                '(print("(2) x é igual a", x)))
(%i5) printe1 (y - z);
(1) x é igual a 1234 - 1729 w 
(%o5)              print((2) x é igual a, x)
(%i6) ''%;
(2) x é igual a %pi 
(%o6)                          %pi
```


`macroexpand` retorna uma expansão de macro.
`macroexpand (foo (x))` seguido por `''%` é equivalente a `foo (x)`
quando `foo` for uma função de macro.












```maxima
(%i1) x: %pi;
(%o1)                          %pi
(%i2) y: 1234;
(%o2)                         1234
(%i3) z: 1729 * w;
(%o3)                        1729 w
(%i4) g (x) ::= buildq ([x], print ("x é igual a", x));
(%o4)    g(x) ::= buildq([x], print("x é igual a", x))
(%i5) macroexpand (g (y - z));
(%o5)              print(x é igual a, y - z)
(%i6) ''%;
x é igual a 1234 - 1729 w 
(%o6)                     1234 - 1729 w
(%i7) g (y - z);
x é igual a 1234 - 1729 w 
(%o7)                     1234 - 1729 w
```

<!-- category: Other -->
<!-- keywords: := -->
<!-- signatures: := -->
### Function: :=

O operador de definição de função.  E.g. `f(x):=sin(x)` define
uma função `f`.

<!-- category: Other -->
<!-- keywords: <, <=, >=, > -->
<!-- signatures: <=, >=, > -->
### Function: < (=)

<!-- category: Other -->
<!-- keywords: = -->
<!-- signatures: = -->
### Function: =

O operador de equação.


Uma expressão `a = b`, por si mesma, representa
uma equação não avaliada, a qual pode ou não se manter.
Equações não avaliadas podem aparecer como argumentos para `solve` e `algsys`
ou algumas outras funções.


A função `is` avalia `=` para um valor Booleano.
`is(a = b)` avalia `a = b` para `true` quando *a* e *b*
forem idênticos. Isto é, *a* e *b* forem átomos que são idênticos,
ou se eles não forem átomos e seus operadores forem idênticos e seus argumentos forem idênticos.
De outra forma, `is(a = b)` avalia para `false`;
`is(a = b)` nunca avalia para `unknown`.
Quando `is(a = b)` for `true`, *a* e *b* são ditos para serem sintaticamente iguais,
em contraste para serem expressões equivalentes, para as quais `is(equal(a, b))` é `true`.
Expressões podem ser equivalentes e não sintáticamente iguais.


A negação de `=` é representada por `#`.
Da mesma forma que com `=`, uma expressão `a # b`, por si mesma, não é avaliada.
`is(a # b)` avalia `a # b` para
`true` ou `false`.


Complementando a função `is`,
alguns outros operadores avaliam `=` e `#` para `true` ou `false`,
a saber `if`, `and`, `or`, e `not`.


Note que pelo facto de as regras de avaliação de expressões predicadas
(em particular pelo facto de `not expr` fazer com que ocorra a avaliação de *expr*),
a forma `not a = b` é equivalente a `is(a # b)`,
em lugar de ser equivalente a `a # b`.


`rhs` e `lhs` retornam o primeiro membro e o segundo membro de uma equação,
respectivamente, de uma equação ou inequação.


Veja também `equal` e `notequal`.


Exemplos:


Uma expressão `a = b`, por si mesma, representa
uma equação não avaliada, a qual pode ou não se manter.










```maxima
(%i1) eq_1 : a * x - 5 * y = 17;
(%o1)                    a x - 5 y = 17
(%i2) eq_2 : b * x + 3 * y = 29;
(%o2)                    3 y + b x = 29
(%i3) solve ([eq_1, eq_2], [x, y]);
                        196         29 a - 17 b
(%o3)          [[x = ---------, y = -----------]]
                     5 b + 3 a       5 b + 3 a
(%i4) subst (%, [eq_1, eq_2]);
         196 a     5 (29 a - 17 b)
(%o4) [--------- - --------------- = 17, 
       5 b + 3 a      5 b + 3 a
                                  196 b     3 (29 a - 17 b)
                                --------- + --------------- = 29]
                                5 b + 3 a      5 b + 3 a
(%i5) ratsimp (%);
(%o5)                  [17 = 17, 29 = 29]
```


`is(a = b)` avalia `a = b` para `true` quando *a* e *b*
são sintaticamente iguais (isto é, identicos).
Expressões podem ser equivalentes e não sintaticamente iguais.









```maxima
(%i1) a : (x + 1) * (x - 1);
(%o1)                    (x - 1) (x + 1)
(%i2) b : x^2 - 1;
                              2
(%o2)                        x  - 1
(%i3) [is (a = b), is (a # b)];
(%o3)                     [false, true]
(%i4) [is (equal (a, b)), is (notequal (a, b))];
(%o4)                     [true, false]
```


Alguns operadores avaliam `=` e `#` para `true` ou `false`.









```maxima
(%i1) if expand ((x + y)^2) = x^2 + 2 * x * y + y^2 then FOO else BAR;
(%o1)                          FOO
(%i2) eq_3 : 2 * x = 3 * x;
(%o2)                       2 x = 3 x
(%i3) eq_4 : exp (2) = %e^2;
                              2     2
(%o3)                       %e  = %e
(%i4) [eq_3 and eq_4, eq_3 or eq_4, not eq_3];
(%o4)                  [false, true, true]
```


Devido a `not expr` fazer com que a avaliação de *expr* ocorra,
`not a = b` é equivalente a `is(a # b)`.







```maxima
(%i1) [2 * x # 3 * x, not (2 * x = 3 * x)];
(%o1)                   [2 x # 3 x, true]
(%i2) is (2 * x # 3 * x);
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: ^^ -->
<!-- signatures: ^^ -->
### Function: ^^

<!-- category: Other -->
<!-- keywords: abs -->
<!-- signatures: abs(expr) -->
### Function: abs (expr)

Retorna o valor absoluto de *expr*.  Se *expr* for um número complexo, retorna o módulo
complexo de *expr*.

<!-- category: Other -->
<!-- keywords: additive -->
<!-- signatures: additive -->
### Variable: additive

Se `declare(f,additive)` tiver sido executado, então:


(1) Se `f` for uma função de uma única variável, sempre que o simplificador encontrar `f` aplicada
a uma adição, `f` será distribuído sobre aquela adição.  I.e. `f(y+x)` irá
simplificar para `f(y)+f(x)`.


(2) Se `f` for uma função de 2 ou mais argumentos, a adição é definida como 
adição no primeiro argumento para `f`, como no caso de `sum` ou  
`integrate`, i.e. `f(h(x)+g(x),x)` irá simplificar para `f(h(x),x)+f(g(x),x)`.
Essa simplificação não ocorre quando `f` é aplicada para expressões da
forma `sum(x[i],i,lower-limit,upper-limit)`.

<!-- category: Other -->
<!-- keywords: allbut -->
<!-- signatures: allbut -->
### Variable: allbut

trabalha com os comandos `part` (i.e. `part`, `inpart`, `substpart`,
`substinpart`, `dpart`, e `lpart`).  Por exemplo,







```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, [2, 5]);
(%o2)                         d + a
```


enquanto







```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, allbut (2, 5));
(%o2)                       e + c + b
```


`allbut` é também reconhecido por `kill`.

 






```maxima
(%i1) [aa : 11, bb : 22, cc : 33, dd : 44, ee : 55];
(%o1)                 [11, 22, 33, 44, 55]
(%i2) kill (allbut (cc, dd));
(%o0)                         done
(%i1) [aa, bb, cc, dd];
(%o1)                   [aa, bb, 33, 44]
```


`kill(allbut(a_1, a_2, ...))` tem o mesmo efeito que `kill(all)`
excepto que não elimina os símbolos *a_1*, *a_2*, ... .

<!-- category: Other -->
<!-- keywords: and -->
<!-- signatures: and -->
### Function: and

O operador lógico de conjunção.
`and` é um operador n-ário infixo;
seus operandos são expressões Booleanas, e seu resultado é um valor Booleano.


`and` força avaliação (como `is`) de um ou mais operandos,
e pode forçar a avaliação de todos os operandos.


Operandos são avaliados na ordem em que aparecerem.
`and` avalia somente quantos de seus operandos forem necessários para determinar o resultado.
Se qualquer operando for `false`,
o resultado é `false` e os operandos restantes não são avaliados.


O sinalizador global `prederror` governa o comportamento de `and`
quando um operando avaliado não pode ser determinado como sendo `true` ou `false`.
`and` imprime uma mensagem de erro quando `prederror` for `true`.  
De outra forma, `and` retorna `unknown` (desconhecido).


`and` não é comutativo:
`a and b` pode não ser igual a `b and a` devido ao tratamento de operandos indeterminados.

<!-- category: Other -->
<!-- keywords: antisymmetric -->
<!-- signatures: antisymmetric -->
### Variable: antisymmetric

Se `declare(h,antisymmetric)` é concluída, diz ao
simplicador que `h` é uma função antisimétrica.  E.g. `h(x,z,y)` simplificará para
`- h(x, y, z)`.  Isto é, dará (-1)^n vezes o resultado dado por
`symmetric` ou `commutative`, quando n for o número de interescolhas de dois
argumentos necessários para converter isso naquela forma.

<!-- category: Other -->
<!-- keywords: cabs -->
<!-- signatures: cabs(expr) -->
### Function: cabs (expr)

Retorna o valor absoluto complexo (o módulo complexo) de
*expr*.

<!-- category: Other -->
<!-- keywords: ceiling -->
<!-- signatures: ceiling(x) -->
### Function: ceiling (x)

Quando *x* for um número real, retorna o último inteiro que 
é maior que ou igual a *x*.  


Se *x* for uma expressão constante (`10 * %pi`, por exemplo), 
`ceiling` avalia *x* usando grandes números em ponto flutuante, e 
aplica `ceiling` para o grande número em ponto flutuante resultante. Porque `ceiling` usa
avaliação de ponto flutuante, é possível, embora improvável, 
que `ceiling` possa retornar uma valor erroneo para entradas
constantes. Para prevenir erros, a avaliação de ponto flutuante
é concluída usando três valores para `fpprec`.


Para entradas não constantes, `ceiling` tenta retornar um valor
simplificado.  Aqui está um exemplo de simplificações que `ceiling`
conhece:












```maxima
(%i1) ceiling (ceiling (x));
(%o1)                      ceiling(x)
(%i2) ceiling (floor (x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) [ceiling (n), ceiling (abs (n)), ceiling (max (n, 6))];
(%o4)                [n, abs(n), max(n, 6)]
(%i5) assume (x > 0, x < 1)$
(%i6) ceiling (x);
(%o6)                           1
(%i7) tex (ceiling (a));
$$\left \lceil a \right \rceil$$
(%o7)                         false
```


A função `ceiling` não mapeia automaticamente sobre listas ou matrizes.
Finalmente, para todas as entradas que forem manifestamente complexas, `ceiling` retorna 
uma forma substantiva.


Se o intervalo de uma função é um subconjunto dos inteiros, o intervalo pode ser
declarado `integervalued`. Ambas as funções `ceiling` e `floor`
podem usar essa informação; por exemplo:








```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

<!-- category: Other -->
<!-- keywords: charfun -->
<!-- signatures: charfun(p) -->
### Function: charfun (p)

Retorna 0 quando o predicado *p* avaliar para `false`; retorna
1 quando o predicado avaliar para `true`.  Quando o predicado
avaliar para alguma coisa que não `true` ou `false` (`unknown`), 
retorna uma forma substantiva.


Exemplos:









```maxima
(%i1) charfun (x < 1);
(%o1)                    charfun(x < 1)
(%i2) subst (x = -1, %);
(%o2)                           1
(%i3) e : charfun ('"and" (-1 < x, x < 1))$
(%i4) [subst (x = -1, e), subst (x = 0, e), subst (x = 1, e)];
(%o4)                       [0, 1, 0]
```

<!-- category: Other -->
<!-- keywords: commutative -->
<!-- signatures: commutative -->
### Variable: commutative

Se `declare(h,commutative)` é concluída, diz ao
simplicador que `h` é uma função comutativa.  E.g. `h(x,z,y)` irá
simplificar para `h(x, y, z)`.  Isto é o mesmo que `symmetric`.

<!-- category: Other -->
<!-- keywords: compare -->
<!-- signatures: compare(x, y) -->
### Function: compare (x, y)

Retorna um operador de comparação *op*
(`<`, `<=`, `>`, `>=`, `=`, ou `#`) tal que
`is (x op y)` avalia para `true`;
quando ou *x* ou *y* dependendo de `%i` e
`x # y`, retorna `notcomparable`;
Quando não existir tal operador ou
Maxima não estiver apto a determinar o operador, retorna `unknown`.


Exemplos:











```maxima
(%i1) compare (1, 2);
(%o1)                           <
(%i2) compare (1, x);
(%o2)                        unknown
(%i3) compare (%i, %i);
(%o3)                           =
(%i4) compare (%i, %i + 1);
(%o4)                     notcomparable
(%i5) compare (1/x, 0);
(%o5)                           #
(%i6) compare (x, abs(x));
(%o6)                          <=
```


A função `compare` não tenta de terminar se o domínio real de
seus argumentos é não vazio; dessa forma






```maxima
(%i1) compare (acos (x^2 + 1), acos (x^2 + 1) + 1);
(%o1)                           <
```


O domínio real de `acos (x^2 + 1)` é vazio.

<!-- category: Other -->
<!-- keywords: entier -->
<!-- signatures: entier(x) -->
### Function: entier (x)

Retorna o último inteiro menor que ou igual a *x* onde *x* é numérico.  `fix` (como em
`fixnum`) é um sinonimo disso, então `fix(x)` é precisamente o mesmo.

<!-- category: Other -->
<!-- keywords: equal -->
<!-- signatures: equal(a, b) -->
### Function: equal (a, b)

Representa a equivalência, isto é, valor igual.

 

Por si mesma, `equal` não avalia ou simplifica.
A função `is` tenta avaliar `equal` para um valor Booleano.
`is(equal(a, b))` 
retorna `true` (ou `false`) se
e somente se *a* e *b* forem iguais (ou não iguais) para todos os possíveis
valores de suas variáveis, como determinado através da avaliação de `ratsimp(a - b)`;
se `ratsimp` retornar 0, as duas expressões são consideradas equivalentes.
Duas expressões podem ser equivalentes mesmo se mesmo se elas não forem sintaticamente iguais (i.e., identicas).


Quando `is` falhar em reduzir `equal` a `true` ou `false`,
o resultado é governado através do sinalizador global `prederror`.
Quando `prederror` for `true`,
`is` reclama com uma mensagem de erro.
De outra forma, `is` retorna `unknown`.


Complementando `is`,
alguns outros operadores avaliam `equal` e `notequal` para `true` ou `false`,
a saber `if`, `and`, `or`, e `not`.







A negação de `equal` é `notequal`.
Note que devido às regras de avaliação de expressões predicadas
(em particular pelo facto de `not expr` causar a avaliação de *expr*),
`not equal(a, b)`
é equivalente a `is(notequal(a, b))`
em lugar de ser equivalente a `notequal(a, b)`.


Exemplos:


Por si mesmo, `equal` não avalia ou simplifica.








```maxima
(%i1) equal (x^2 - 1, (x + 1) * (x - 1));
                        2
(%o1)            equal(x  - 1, (x - 1) (x + 1))
(%i2) equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) equal (x, y);
(%o3)                      equal(x, y)
```


A função `is` tenta avaliar `equal` para um valor Booleano.
`is(equal(a, b))` retorna `true` quando `ratsimp(a - b)` retornar 0.
Duas expressões podem ser equivalentes mesmo se não forem sintaticamente iguais (i.e., identicas).














```maxima
(%i1) ratsimp (x^2 - 1 - (x + 1) * (x - 1));
(%o1)                           0
(%i2) is (equal (x^2 - 1, (x + 1) * (x - 1)));
(%o2)                         true
(%i3) is (x^2 - 1 = (x + 1) * (x - 1));
(%o3)                         false
(%i4) ratsimp (x - (x + 1));
(%o4)                          - 1
(%i5) is (equal (x, x + 1));
(%o5)                         false
(%i6) is (x = x + 1);
(%o6)                         false
(%i7) ratsimp (x - y);
(%o7)                         x - y
(%i8) is (equal (x, y));
Maxima was unable to evaluate the predicate:
equal(x, y)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i9) is (x = y);
(%o9)                         false
```

 

Quando `is` falha em reduzir `equal` a `true` ou `false`,
o resultado é governado através do sinalizador global `prederror`.

 








 

```maxima
(%i1) [aa : x^2 + 2*x + 1, bb : x^2 - 2*x - 1];
                    2             2
(%o1)             [x  + 2 x + 1, x  - 2 x - 1]
(%i2) ratsimp (aa - bb);
(%o2)                        4 x + 2
(%i3) prederror : true;
 (%o3)                         true
(%i4) is (equal (aa, bb));
Maxima was unable to evaluate the predicate:
       2             2
equal(x  + 2 x + 1, x  - 2 x - 1)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) prederror : false;
(%o5)                         false
(%i6) is (equal (aa, bb));
(%o6)                        unknown
```


Alguns operadores avaliam `equal` e `notequal` para `true` ou `false`.









```maxima
(%i1) if equal (a, b) then FOO else BAR;
Maxima was unable to evaluate the predicate:
equal(a, b)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i2) eq_1 : equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) eq_2 : equal (y^2 + 2*y + 1, (y + 1)^2);
                         2                   2
(%o3)             equal(y  + 2 y + 1, (y + 1) )
(%i4) [eq_1 and eq_2, eq_1 or eq_2, not eq_1];
(%o4)                  [false, true, true]
```


Devido a `not expr` fazer com que ocorra a avaliação de *expr*,
`not equal(a, b)` é equivalente a `is(notequal(a, b))`.







```maxima
(%i1) [notequal (2*z, 2*z - 1), not equal (2*z, 2*z - 1)];
(%o1)            [notequal(2 z, 2 z - 1), true]
(%i2) is (notequal (2*z, 2*z - 1));
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: eval -->
<!-- signatures: eval -->
### Function: eval

Como um argumento em uma chamada a `ev (expr)`,
`eval` causa uma avaliação extra de *expr*.
Veja `ev`.

<!-- category: Other -->
<!-- keywords: evenp -->
<!-- signatures: evenp(expr) -->
### Function: evenp (expr)

Retorna `true` se *expr* for um inteiro sempre.

`false` é retornado em todos os outros casos.

<!-- category: Other -->
<!-- keywords: fix -->
<!-- signatures: fix(x) -->
### Function: fix (x)

Um sinonimo para `entier (x)`.

<!-- category: Other -->
<!-- keywords: floor -->
<!-- signatures: floor(x) -->
### Function: floor (x)

Quando *x* for um número real, retorna o maior inteiro que 
é menor que ou igual a *x*.


Se *x* for uma expressão constante (`10 * %pi`, for exemplo), 
`floor` avalia *x* usando grandes números em ponto flutuante, e 
aplica `floor` ao grande número em ponto flutuante resultante. Porque `floor` usa
avaliação em ponto flutuante, é possível, embora improvável, 
que `floor` não possa retornar um valor erroneo para entradas
constantes.  Para prevenir erros, a avaliação de ponto flutuante
é concluída usando três valores para `fpprec`.


Para entradas não constantes, `floor` tenta retornar um valor
simplificado.  Aqui está exemplos de simplificações que `floor`
conhece:












```maxima
(%i1) floor (ceiling (x));
(%o1)                      ceiling(x)
(%i2) floor (floor (x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) [floor (n), floor (abs (n)), floor (min (n, 6))];
(%o4)                [n, abs(n), min(n, 6)]
(%i5) assume (x > 0, x < 1)$
(%i6) floor (x);
(%o6)                           0
(%i7) tex (floor (a));
$$\left \lfloor a \right \rfloor$$
(%o7)                         false
```


A função `floor` não mapeia automaticamente sobre listas ou matrizes.
Finalmente, para todas as entradas que forem manifestamente complexas, `floor` retorna
uma forma substantiva.


Se o intervalo de uma função for um subconjunto dos inteiros, o intervalo pode ser
declarado `integervalued`. Ambas as funções `ceiling` e `floor`
podem usar essa informação; por exemplo:








```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

<!-- category: Other -->
<!-- keywords: fullmap -->
<!-- signatures: fullmap(f, expr_1, ...) -->
### Function: fullmap (f, expr_1, ...)

Similar a `map`, mas `fullmap` mantém mapeadas para
baixo todas as subexpressões até que os operadores principais não mais sejam os
mesmos.


`fullmap` é usada pelo simplificador do
Maxima para certas manipulações de matrizes; dessa forma, Maxima algumas vezes gera
uma mensagem de erro concernente a `fullmap` mesmo apesar de `fullmap` não ter sido
explicitamente chamada pelo utilizador.


Exemplos:








```maxima
(%i1) a + b * c;
(%o1)                        b c + a
(%i2) fullmap (g, %);
(%o2)                   g(b) g(c) + g(a)
(%i3) map (g, %th(2));
(%o3)                     g(b c) + g(a)
```

<!-- category: Other -->
<!-- keywords: fullmapl -->
<!-- signatures: fullmapl(f, list_1, ...) -->
### Function: fullmapl (f, list_1, ...)

Similar a `fullmap`, mas `fullmapl` somente mapeia sobre
listas e matrizes.


Exemplo:






```maxima
(%i1) fullmapl ("+", [3, [4, 5]], [[a, 1], [0, -1.5]]);
(%o1)                [[a + 3, 4], [4, 3.5]]
```

<!-- category: Other -->
<!-- keywords: is -->
<!-- signatures: is(expr) -->
### Function: is (expr)

Tenta determinar se a *expr* predicada (expressões que avaliam para `true`
ou `false`) é dedutível de factos localizados na base de dados de `assume`.


Se a dedutibilidade do predicado for `true` ou `false`,
`is` retorna `true` ou `false`, respectivamente.
De outra forma, o valor de retorno é governado através do sinalizador global `prederror`.
Quando `prederror` for `true`,
`is` reclama com uma mensagem de erro.
De outra forma, `is` retorna `unknown`.


`ev(expr, pred)`
(que pode ser escrita da forma  `expr, pred` na linha de comando interativa)
é equivalente a `is(expr)`.


Veja também `assume`, `facts`, e `maybe`.


Exemplos:


`is` causa avaliação de predicados.






```maxima
(%i1) %pi > %e;
(%o1)                       %pi > %e
(%i2) é (%pi > %e);
(%o2)                         true
```


`is` tenta derivar predicados da base de dados do `assume`.










```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) assume (b > c);
(%o2)                        [b > c]
(%i3) é (a < b);
(%o3)                         false
(%i4) é (a > c);
(%o4)                         true
(%i5) é (equal (a, c));
(%o5)                         false
```


Se `is` não puder nem comprovar nem refutar uma forma predicada a partir da base de dados de `assume`,
o sinalizador global `prederror` governa o comportamento de `is`.










```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) prederror: true$
(%i3) é (a > 0);
Maxima was unable to evaluate the predicate:
a > 0
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) prederror: false$
(%i5) é (a > 0);
(%o5)                        unknown
```

<!-- category: Other -->
<!-- keywords: isqrt -->
<!-- signatures: isqrt(x) -->
### Function: isqrt (x)

Retorna o "inteiro raíz quadrada"
do valor absoluto de *x*,
que é um inteiro.

<!-- category: Other -->
<!-- keywords: lmax -->
<!-- signatures: lmax(L) -->
### Function: lmax (L)

Quando *L* for uma lista ou um conjunto, retorna `apply ('max, args (L))`.  Quando *L* não for uma
lista ou também não for um conjunto, sinaliza um erro.

<!-- category: Other -->
<!-- keywords: lmin -->
<!-- signatures: lmin(L) -->
### Function: lmin (L)

Quando *L* for uma lista ou um conjunto, retorna `apply ('min, args (L))`. Quando *L* não for uma
lista ou ou também não for um conjunto, sinaliza um erro.

<!-- category: Other -->
<!-- keywords: make_random_state -->
<!-- signatures: make_random_state(n), make_random_state(s), make_random_state(true), make_random_state(false) -->
### Function: make_random_state (n)

Um objecto de estado aleatório representa o estado do gerador de números aleatórios (aleatórios).
O estado compreende 627 palavras de 32 bits.


`make_random_state (n)` retorna um novo objecto de estado aleatório
criado de um valor inteiro semente igual a *n* modulo 2^32.  
*n* pode ser negativo.






`make_random_state (s)` retorna uma copia do estado aleatório *s*.


`make_random_state (true)` retorna um novo objecto de estado aleatório,
usando a hora corrente  do relógio do computador como semente.


`make_random_state (false)` retorna uma cópia do estado corrente
do gerador de números aleatórios.

<!-- category: Other -->
<!-- keywords: max -->
<!-- signatures: max(x_1, ..., x_n) -->
### Function: max (x_1, ..., x_n)

Retorna um valor simplificado para o máximo entre as expressões *x_1* a *x_n*.
Quando `get (trylevel, maxmin)`, for dois ou mais, `max` usa a simplificação 
`max (e, -e) --> |e|`.  Quando `get (trylevel, maxmin)` for 3 ou mais, *max* tenta
eliminar expressões que estiverem entre dois outros argumentos; por exemplo,
`max (x, 2*x, 3*x) --> max (x, 3*x)`. Para escolher o valor de `trylevel` para 2, use
`put (trylevel, 2, maxmin)`.

<!-- category: Other -->
<!-- keywords: maybe -->
<!-- signatures: maybe(expr) -->
### Function: maybe (expr)

Tenta determinar se a *expr* predicada
é dedutível dos factos na base de dados de `assume`.


Se a dedutibilidade do predicado for `true` ou `false`,
`maybe` retorna `true` ou `false`, respectivamente.
De outra forma, `maybe` retorna `unknown`.


`maybe` é funcinalmente equivalente a `is` com `prederror: false`,
mas o resultado é computado sem actualmente atribuir um valor a `prederror`.


Veja também `assume`, `facts`, e `is`.


Exemplos:








```maxima
(%i1) maybe (x > 0);
(%o1)                        unknown
(%i2) assume (x > 1);
(%o2)                        [x > 1]
(%i3) maybe (x > 0);
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: min -->
<!-- signatures: min(x_1, ..., x_n) -->
### Function: min (x_1, ..., x_n)

Retorna um valor simplificado para o mínimo entre as expressões `x_1` até `x_n`.
Quando `get (trylevel, maxmin)`, for 2 ou mais, `min` usa a simplificação 
`min (e, -e) --> -|e|`.  Quando `get (trylevel, maxmin)` for 3 ou mais, `min` tenta
eliminar expressões que estiverem entre dois outros argumentos; por exemplo,
`min (x, 2*x, 3*x) --> min (x, 3*x)`. Para escolher o valor de `trylevel` para 2, use
`put (trylevel, 2, maxmin)`.

<!-- category: Other -->
<!-- keywords: mod -->
<!-- signatures: mod(x, y) -->
### Function: mod (x, y)

Se *x* e *y* forem números reais e *y* for não nulo,
retorna `x - y * floor(x / y)`.
Adicionalmente para todo real *x*, nós temos `mod (x, 0) = x`. Para uma discursão da
definição `mod (x, 0) = x`, veja a Seção 3.4, de "Concrete Mathematics," 
por Graham, Knuth, e Patashnik. A função `mod (x, 1)` 
é uma função dente de serra com período 1 e com `mod (1, 1) = 0` e 
`mod (0, 1) = 0`.


Para encontrar o argumento (um número no intervalo `(-%pi, %pi]`) de um 
número complexo, use a função `x |-> %pi - mod (%pi - x, 2*%pi)`, onde 
*x* é um argumento.


Quando *x* e *y* forem expressões constantes (`10 * %pi`, por exemplo), `mod`
usa o mesmo esquema de avaliação em ponto flutuante que `floor` e `ceiling` usam.
Novamente, é possível, embora improvável, que `mod` possa retornar um
valor erroneo nesses casos.


Para argumentos não numéricos *x* ou *y*, `mod`conhece muitas regras de
simplificação:








```maxima
(%i1) mod (x, 0);
(%o1)                           x
(%i2) mod (a*x, a*y);
(%o2)                      a mod(x, y)
(%i3) mod (0, x);
(%o3)                           0
```

<!-- category: Other -->
<!-- keywords: not -->
<!-- signatures: not -->
### Function: not

O operador lógico de negação.
`not` é operador prefixado;
Seu operando é uma expressão Booleana, e seu resultado é um valor Booleano.


`not` força a avaliação (como `is`) de seu operando.


O sinalizador global `prederror` governa o comportamento de `not`
quando seu operando não pode ser determinado em termos de `true` ou `false`.
`not` imprime uma mensagem de erro quando `prederror` for `true`.
De outra forma, `not` retorna `unknown`.

<!-- category: Other -->
<!-- keywords: notequal -->
<!-- signatures: notequal(a, b) -->
### Function: notequal (a, b)

Represents the negation of `equal(a, b)`.


Note que pelo facto de as regras de avaliação de expressões predicadas
(em particular pelo facto de `not expr` causar a avaliação de *expr*),
`not equal(a, b)`
é equivalente a `is(notequal(a, b))`
em lugar de ser equivalente a `notequal(a, b)`.


Exemplos:


















```maxima
(%i1) equal (a, b);
(%o1)                      equal(a, b)
(%i2) maybe (equal (a, b));
(%o2)                        unknown
(%i3) notequal (a, b);
(%o3)                    notequal(a, b)
(%i4) not equal (a, b);
Maxima was unable to evaluate the predicate:
equal(a, b)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) maybe (notequal (a, b));
(%o5)                        unknown
(%i6) maybe (not equal (a, b));
(%o6)                        unknown
(%i7) assume (a > b);
(%o7)                        [a > b]
(%i8) equal (a, b);
(%o8)                      equal(a, b)
(%i9) maybe (equal (a, b));
(%o9)                         false
(%i10) notequal (a, b);
(%o10)                   notequal(a, b)
(%i11) not equal (a, b);
(%o11)                        true
(%i12) maybe (notequal (a, b));
(%o12)                        true
(%i13) maybe (not equal (a, b));
(%o13)                        true
```

<!-- category: Other -->
<!-- keywords: oddp -->
<!-- signatures: oddp(expr) -->
### Function: oddp (expr)

é `true` se *expr* for um inteiro ímpar.

`false` é retornado em todos os outros casos.

<!-- category: Other -->
<!-- keywords: or -->
<!-- signatures: or -->
### Function: or

O operador lógico de disjunção.
`or` é um operador n-ário infixo;
seus operandos são expressões Booleanas, e seu resultado é um valor Booleano.


`or` força avaliação (como `is`) de um ou mais operandos,
e pode forçar a avaliação de todos os operandos.


Operandos são avaliados na ordem em que aparecem.
`or` avalia somente quantos de seus operandos forem necessários para determinar o resultado.
Se qualquer operando for `true`,
o resultado é `true` e os operandos restantes não são avaliados.


O sinalizador global `prederror` governa o comportamento de `or`
quando um operando avaliado não puder ser determinado como sendo `true` ou `false`.
`or` imprime uma mensagem de erro quando `prederror` for `true`.
De outra forma, `or` retorna `unknown`.


`or` não é comutativo:
`a or b` pode não ser igual a `b or a` devido ao tratamento de operando indeterminados.

<!-- category: Other -->
<!-- keywords: polymod -->
<!-- signatures: polymod(p), polymod(p, m) -->
### Function: polymod (p)

Converte o polinómio *p* para uma representação modular
com relação ao módulo corrente que é o valor da variável
`modulus`.  


`polymod (p, m)` especifica um módulo *m* para ser usado 
em lugar do valor corrente de `modulus`.


Veja `modulus`.

<!-- category: Other -->
<!-- keywords: pred -->
<!-- signatures: pred -->
### Function: pred

Como um argumento em uma chamada a `ev (expr)`,
`pred` faz com que predicados (expressões que avaliam para `true`
ou `false`) sejam avaliados.
Veja `ev`.

<!-- category: Other -->
<!-- keywords: random -->
<!-- signatures: random(x) -->
### Function: random (x)

Retorna um número pseudoaleatório. Se *x* é um inteiro, `random (x)` retorna um
inteiro de 0 a `x - 1` inclusive. Se *x* for um número em ponto flutuante,
`random (x)` retorna um número não negativo em ponto flutuante menor que *x*.
`random` reclama com um erro se *x* não for nem um inteiro nem um número em ponto flutuante,
ou se *x* não for positivo.


As funções `make_random_state` e `set_random_state`
mantém o estado do gerador de números aleatórios.


O gerador de números aleatórios do Maxima é uma implementação do algoritmo de Mersenne twister MT 19937.


Exemplos:


















```maxima
(%i1) s1: make_random_state (654321)$
(%i2) set_random_state (s1);
(%o2)                         done
(%i3) random (1000);
(%o3)                          768
(%i4) random (9573684);
(%o4)                        7657880
(%i5) random (2^75);
(%o5)                11804491615036831636390
(%i6) s2: make_random_state (false)$
(%i7) random (1.0);
(%o7)                   .2310127244107132
(%i8) random (10.0);
(%o8)                   4.394553645870825
(%i9) random (100.0);
(%o9)                   32.28666704056853
(%i10) set_random_state (s2);
(%o10)                        done
(%i11) random (1.0);
(%o11)                  .2310127244107132
(%i12) random (10.0);
(%o12)                  4.394553645870825
(%i13) random (100.0);
(%o13)                  32.28666704056853
```

<!-- category: Other -->
<!-- keywords: rationalize -->
<!-- signatures: rationalize(expr) -->
### Function: rationalize (expr)

Converte todos os números em ponto flutuante de precisão dupla e
grandes números em ponto flutuante na expressão do Maxima *expr*
para seus exatos equivalentes racionais. Se vnão estiver familiarizado
com a representação binária dos números em ponto
flutuante, pode ficar surpreendido em saber que `rationalize (0.1)`
não é igual a 1/10.  Esse comportamento não é especial do Maxima
– o número 1/10 tem uma representação binária
repetitiva e não terminada.












```maxima
(%i1) rationalize (0.5);
                                1
(%o1)                           -
                                2
(%i2) rationalize (0.1);
                               1
(%o2)                          --
                               10
 (%i3) fpprec : 5$
(%i4) rationalize (0.1b0);
                             209715
(%o4)                        -------
                             2097152
(%i5) fpprec : 20$
(%i6) rationalize (0.1b0);
                     236118324143482260685
(%o6)                ----------------------
                     2361183241434822606848
(%i7) rationalize (sin (0.1*x + 5.6));
                              x    28
(%o7)                     sin(-- + --)
                              10   5
```


Exemplo de utilização:

















```maxima
(%i1) unitfrac(r) := block([uf : [], q],
    if not(ratnump(r)) then error("The input to 'unitfrac' must be a rational number"),
    while r # 0 do (
        uf : cons(q : 1/ceiling(1/r), uf),
        r : r - q),
    reverse(uf)); 
(%o1) unitfrac(r) := block([uf : [], q], 
if not ratnump(r) then error("The input to 'unitfrac' must be a rational number"
                                     1
), while r # 0 do (uf : cons(q : ----------, uf), r : r - q), 
                                         1
                                 ceiling(-)
                                         r
reverse(uf))
(%i2) unitfrac (9/10);
                            1  1  1
(%o2)                      [-, -, --]
                            2  3  15
(%i3) apply ("+", %);
                               9
(%o3)                          --
                               10
(%i4) unitfrac (-9/10);
                                  1
(%o4)                       [- 1, --]
                                  10
(%i5) apply ("+", %);
                                9
(%o5)                         - --
                                10
(%i6) unitfrac (36/37);
                        1  1  1  1    1
(%o6)                  [-, -, -, --, ----]
                        2  3  8  69  6808
(%i7) apply ("+", %);
                               36
(%o7)                          --
                               37
```

<!-- category: Other -->
<!-- keywords: set_random_state -->
<!-- signatures: set_random_state(s) -->
### Function: set_random_state (s)

Copia *s* para o estado do gerador de números aleatórios.


`set_random_state` sempre retorna `done`.

<!-- category: Other -->
<!-- keywords: sign -->
<!-- signatures: sign(expr) -->
### Function: sign (expr)

Tenta determinar o sinal de *expr*
a partir dos factos na base de dados corrente.  Retorna uma das
seguintes respostar: `pos` (positivo), `neg` (negativo), `zero`, `pz`
(positivo ou zero), `nz` (negativo ou zero), `pn` (positivo ou negativo),
ou `pnz` (positivo, negativo, ou zero, i.e. nada se sabe sobre o sinal da epressão).

<!-- category: Other -->
<!-- keywords: signum -->
<!-- signatures: signum(x) -->
### Function: signum (x)

Para um *x* numérico retorna 0 se *x* for 0, de outra forma retorna -1 ou +1
à medida que *x* seja menor ou maior que 0, respectivamente.


Se *x* não for numérico então uma forma simplificada mas equivalente é retornada.
Por exemplo, `signum(-x)` fornece `-signum(x)`.

<!-- category: Other -->
<!-- keywords: sort -->
<!-- signatures: sort(L, P), sort(L) -->
### Function: sort (L, P)

Organiza uma lista *L* coforme o predicado `P` de dois argumentos,
de forma que `P (L[k], L[k + 1])` seja `true`
para qualquer dois elementos sucessivos.
O predicado pode ser especificado como o nome de uma função ou operador binário infixo,
ou como uma expressão `lambda`.
Se especificado como o nome de um operador,
o nome deve ser contido entre "aspas duplas".


A lista ordenada é retornada como novo objecto;
o argumento *L* não é modificado.
Para construir o valor de retorno,
`sort` faz uma cópia superficial dos elementos de *L*.


Se o predicado *P* não for uma ordem total sobre os elementos de *L*,
então `sort` possivelvente pode executar para concluir sem error,
mas os resultados são indefinidos.
`sort` reclama se o predicado avaliar para alguma outra coisa
que não seja `true` ou `false`.


`sort (L)` é equivalente a `sort (L, orderlessp)`.
Isto é, a ordem padrão de organização é ascendente,
como determinado por `orderlessp`.
Todos os átomos do Maxima e expressões são comparáveis sob `orderlessp`,
embora exista exemplos isolados de expressões para as quais `orderlessp` não é transitiva;
isso é uma falha.

 

Exemplos:

 










```maxima
(%i1) sort ([11, -17, 29b0, 7.55, 3, -5/2, b + a, 9 * c, 19 - 3 * x]);
               5
(%o1) [- 17, - -, 3, 7.55, 11, 2.9b1, b + a, 9 c, 19 - 3 x]
               2
(%i2) sort ([11, -17, 29b0, 7.55, 3, -5/2, b + a, 9 * c, 19 - 3 * x], ordergreatp);
                                                   5
(%o2) [19 - 3 x, 9 c, b + a, 2.9b1, 11, 7.55, 3, - -, - 17]
                                                   2
(%i3) sort ([%pi, 3, 4, %e, %gamma]);
(%o3)                [3, 4, %e, %gamma, %pi]
(%i4) sort ([%pi, 3, 4, %e, %gamma], "<");
(%o4)                [%gamma, %e, 3, %pi, 4]
(%i5) my_list : [[aa, hh, uu], [ee, cc], [zz, xx, mm, cc], [%pi, %e]];
(%o5) [[aa, hh, uu], [ee, cc], [zz, xx, mm, cc], [%pi, %e]]
(%i6) sort (my_list);
(%o6) [[%pi, %e], [aa, hh, uu], [ee, cc], [zz, xx, mm, cc]]
(%i7) sort (my_list, lambda ([a, b], orderlessp (reverse (a), reverse (b))));
(%o7) [[%pi, %e], [ee, cc], [zz, xx, mm, cc], [aa, hh, uu]]
```

<!-- category: Other -->
<!-- keywords: sqrt -->
<!-- signatures: sqrt(x) -->
### Function: sqrt (x)

A raíz quadrada de *x*. É representada internamente por
`x^(1/2)`.  Veja também `rootscontract`.


`radexpand` se `true` fará com que n-ésimas raízes de factores de um produto
que forem potências de n sejam colocados fora do radical, e.g.
`sqrt(16*x^2)` retonará `4*x` somente se `radexpand` for `true`.

<!-- category: Other -->
<!-- keywords: sqrtdispflag -->
<!-- signatures: sqrtdispflag -->
### Variable: sqrtdispflag

Valor por omissão: `true`


Quando `sqrtdispflag` for `false`,
faz com que `sqrt` seja mostrado como expoente 1/2.

<!-- category: Other -->
<!-- keywords: sublis -->
<!-- signatures: sublis(lista, expr) -->
### Function: sublis (lista, expr)

Faz múltiplas substituições paralelas dentro de uma expressão.


A variável `sublis_apply_lambda` controla a simplificação após
`sublis`.


Exemplo:



```maxima

```

<!-- category: Other -->
<!-- keywords: sublis_apply_lambda -->
<!-- signatures: sublis_apply_lambda -->
### Variable: sublis_apply_lambda

Valor por omissão: `true` - controla se os substitutos de
`lambda` são aplicados na simplificação após as
`sublis` serem usadas ou se tiver que fazer um `ev` para obter
coisas para aplicar.  `true` significa faça a
aplicação.

<!-- category: Other -->
<!-- keywords: sublist -->
<!-- signatures: sublist(lista, p) -->
### Function: sublist (lista, p)

Retorna a lista de elementos da *lista* da qual o
predicado `p` retornar `true`.


Exemplo:







```maxima
(%i1) L: [1, 2, 3, 4, 5, 6];
(%o1)                  [1, 2, 3, 4, 5, 6]
(%i2) sublist (L, evenp);
(%o2)                       [2, 4, 6]
```

<!-- category: Other -->
<!-- keywords: subst -->
<!-- signatures: subst(a, b, c) -->
### Function: subst (a, b, c)

Substitue *a* por *b* em *c*.  *b* deve ser um átomo ou uma
subexpressão completa de *c*.  Por exemplo, `x+y+z` é uma subexpressão
completa de `2*(x+y+z)/w` enquanto `x+y` não é. Quando *b* não tem
essas características, pode-se algumas vezes usar `substpart` ou `ratsubst`
(veja abaixo).  Alternativamente, se *b* for da forma de `e/f` então se poderá
usar `subst (a*f, e, c)` enquanto se *b* for da forma `e^(1/f)` então se poderá
usar `subst (a^f, e, c)`.  O comando `subst` também discerne o `x^y` de `x^-y`
de modo que `subst (a, sqrt(x), 1/sqrt(x))` retorna `1/a`.  *a* e *b* podem também ser
operadores de uma expressão contida entre aspas duplas `"` ou eles podem ser nomes de
função.  Se se desejar substituir por uma variável independente em
formas derivadas então a função `at` (veja abaixo) poderá ser usada.



`subst` é um álias para `substitute`.


`subst (eq_1, expr)` ou `subst ([eq_1, ..., eq_k], expr)`
são outras formas
permitidas.  As *eq_i* são equações indicando substituições a serem feitas.
Para cada equação, o lado direito será substituído pelo lado esquerdo na
expressão *expr*.


`exptsubst` se `true` permite que substituições
como `y` por `%e^x` em `%e^(a*x)` ocorram.



Quando `opsubst` for `false`,
`subst` tentará substituir dentro do operador de uma expressão.
E.g. `(opsubst: false, subst (x^2, r, r+r[0]))` trabalhará.


Exemplos:



```maxima
(%i1) subst (a, x+y, x + (x+y)^2 + y);
                                    2
(%o1)                      y + x + a
(%i2) subst (-%i, %i, a + b*%i);
(%o2)                       a - %i b
```



Para exemplos adicionais, faça `example (subst)`.

<!-- category: Other -->
<!-- keywords: substinpart -->
<!-- signatures: substinpart(x, expr, n_1, ..., n_k) -->
### Function: substinpart (x, expr, n_1, ..., n_k)

Similar a `substpart`, mas `substinpart` trabalha sobre a
representação interna de *expr*.


Exemplos:








```maxima
(%i1) x . 'diff (f(x), x, 2);
                              2
                             d
(%o1)                   x . (--- (f(x)))
                               2
                             dx
(%i2) substinpart (d^2, %, 2);
                                  2
(%o2)                        x . d
(%i3) substinpart (f1, f[1](x + 1), 0);
(%o3)                       f1(x + 1)
```


Se o último argumento para a função `part` for uma lista de índices então
muitas subexpressões são escolhidas, cada uma correspondendo a um
índice da lista.  Dessa forma






```maxima
(%i1) part (x + y + z, [1, 3]);
(%o1)                         z + x
```


`piece` recebe o valor da última expressão seleccionada quando usando as
funções `part`.  `piece` é escolhida durante a execução da função e
dessa forma pode ser referenciada para a própria função como mostrado abaixo.
Se `partswitch` for escolhida para `true` então `end` é retornado quando uma
parte seleccionada de uma expressão não existir, de outra forma uma mensagem
de erro é fornecida.











```maxima
(%i1) expr: 27*y^3 + 54*x*y^2 + 36*x^2*y + y + 8*x^3 + x + 1;
              3         2       2            3
(%o1)     27 y  + 54 x y  + 36 x  y + y + 8 x  + x + 1
(%i2) part (expr, 2, [1, 3]);
                                  2
(%o2)                         54 y
(%i3) sqrt (piece/54);
(%o3)                        abs(y)
(%i4) substpart (factor (piece), expr, [1, 2, 3, 5]);
                               3
(%o4)               (3 y + 2 x)  + y + x + 1
(%i5) expr: 1/x + y/x - 1/z;
                             1   y   1
(%o5)                      - - + - + -
                             z   x   x
(%i6) substpart (xthru (piece), expr, [2, 3]);
                            y + 1   1
(%o6)                       ----- - -
                              x     z
```


Também, escolhendo a opção `inflag` para `true` e chamando `part` ou `substpart` é
o mesmo que chamando `inpart` ou `substinpart`.

<!-- category: Other -->
<!-- keywords: substpart -->
<!-- signatures: substpart(x, expr, n_1, ..., n_k) -->
### Function: substpart (x, expr, n_1, ..., n_k)

Substitue *x* para a subexpressão
seleccionada pelo resto dos argumentos como em `part`.  Isso retorna o
novo valor de *expr*.  *x* pode ser algum operador a ser substituído por um
operador de *expr*.  Em alguns casos *x* precisa ser contido em aspas duplas `"`
(e.g.  `substpart ("+", a*b, 0)` retorna `b + a`).









```maxima
(%i1) 1/(x^2 + 2);
                               1
(%o1)                        ------
                              2
                             x  + 2
(%i2) substpart (3/2, %, 2, 1, 2);
                               1
(%o2)                       --------
                             3/2
                            x    + 2
(%i3) a*x + f (b, y);
(%o3)                     a x + f(b, y)
(%i4) substpart ("+", %, 1, 0);
(%o4)                    x + f(b, y) + a
```


Também, escolhendo a opção `inflag` para `true` e chamando `part` ou `substpart` é
o mesmo que chamando `inpart` ou `substinpart`.

<!-- category: Other -->
<!-- keywords: subvarp -->
<!-- signatures: subvarp(expr) -->
### Function: subvarp (expr)

Retorna `true` se *expr* for uma variável subscrita (i.e. que possui índice ou subscrito em sua grafia), por exemplo
`a[i]`.

<!-- category: Other -->
<!-- keywords: symbolp -->
<!-- signatures: symbolp(expr) -->
### Function: symbolp (expr)

Retorna `true` se *expr* for um símbolo, de outra forma retorna `false`.
com efeito, `symbolp(x)` é equivalente ao predicado `atom(x) and not numberp(x)`.




Veja também *Identificadores*

<!-- category: Other -->
<!-- keywords: unorder -->
<!-- signatures: unorder() -->
### Function: unorder ()

Disabilita a ação de alias criada pelo último uso dos comandos
de ordenação `ordergreat` e `orderless`. `ordergreat` e `orderless` não podem
ser usados mais que uma vez cada sem chamar `unorder`. 
Veja também `ordergreat` e `orderless`.


Exemplos:












```maxima
(%i1) unorder();
(%o1)                          []
(%i2) b*x + a^2;
                                   2
(%o2)                       b x + a
(%i3) ordergreat (a);
(%o3)                         done
(%i4) b*x + a^2;
 %th(1) - %th(3);
                             2
(%o4)                       a  + b x
(%i5) unorder();
                              2    2
(%o5)                        a  - a
```

<!-- category: Other -->
<!-- keywords: vectorpotential -->
<!-- signatures: vectorpotential(givencurl) -->
### Function: vectorpotential (givencurl)

Retorna o potencial do vector de um dado
vector de torção, no sistema de coordenadas corrente.
`potentialzeroloc` tem um papel similar ao de `potential`, mas a ordem dos
lados esquerdos das equações deve ser uma permutação cíclica das
variáveis de coordenadas.

<!-- category: Other -->
<!-- keywords: xthru -->
<!-- signatures: xthru(expr) -->
### Function: xthru (expr)

Combina todos os termos de *expr* (o qual pode ser uma adição) sobre um
denominador comum sem produtos e somas exponenciadas
como `ratsimp` faz.  `xthru` cancela factores comuns no numerador e
denominador de expressões racionais mas somente se os factores são
explícitos.



Algumas vezes é melhor usar `xthru` antes de `ratsimp` em uma
expressão com o objectivo de fazer com que factores explicitos do máximo divisor comum entre o
numerador e o denominador seja cancelado simplificando dessa forma a
expressão a ser aplicado o `ratsimp`.







```maxima
(%i1) ((x+2)^20 - 2*y)/(x+y)^20 + (x+y)^(-19) - x/(x+y)^20;
                                20
                 1       (x + 2)   - 2 y       x
(%o1)        --------- + --------------- - ---------
                    19             20             20
             (y + x)        (y + x)        (y + x)
(%i2) xthru (%);
                                 20
                          (x + 2)   - y
(%o2)                     -------------
                                   20
                            (y + x)
```

<!-- category: Other -->
<!-- keywords: zeroequiv -->
<!-- signatures: zeroequiv(expr, v) -->
### Function: zeroequiv (expr, v)

Testa se a expressão *expr* na variável
*v* é equivalente a zero, retornando `true`, `false`, ou
`dontknow` (não sei).


`zeroequiv` Tem essas restrições:


1. Não use funções que o Maxima não sabe como
diferenciar e avaliar.
2. Se a expressão tem postes sobre o eixo real, podem existir erros
no resultado (mas isso é improvável ocorrer).
3. Se a expressão contem funções que não são soluções para
equações diferenciais de primeira ordem (e.g.  funções de Bessel) pode ocorrer
resultados incorrectos.
4. O algoritmo usa avaliação em pontos aleatóriamente escolhidos para
subexpressões seleccionadas cuidadosamente.  Isso é sempre negócio um tanto
quanto perigoso, embora o algoritmo tente minimizar o
potencial de erro.


Por exemplo
 `zeroequiv (sin(2*x) - 2*sin(x)*cos(x), x)` retorna
`true` e `zeroequiv (%e^x + x, x)` retorna `false`.
Por outro lado `zeroequiv (log(a*b) - log(a) - log(b), a)` retorna `dontknow` devido à
presença de um parâmetro extra `b`.

