## Expressões

<!-- category: Other -->
<!-- keywords: %emode -->
<!-- signatures: %emode -->
### Variable: %emode

Valor padrão: `true`


Quando `%emode` for `true`,
`%e^(%pi %i x)` é simplificado como
segue.


`%e^(%pi %i x)` simplifica para `cos (%pi x) + %i sin (%pi x)` se `x` for um inteiro ou
um multiplo de 1/2, 1/3, 1/4, ou 1/6, e então é adicionalmente simplificado.


Para outro `x` numérico,
`%e^(%pi %i x)` simplifica para `%e^(%pi %i y)` onde `y` é `x - 2 k`
para algum inteiro `k` tal que `abs(y) < 1`.  


Quando `%emode` for `false`, nenhuma
simplificação adicional de `%e^(%pi %i x)` é realizada.

<!-- category: Other -->
<!-- keywords: %enumer -->
<!-- signatures: %enumer -->
### Variable: %enumer

Valor padrão: `false`


Quando `%enumer` for `true`,
`%e` é substituido por seu valor numérico
2.718...  mesmo que `numer` seja `true`. 


Quando `%enumer` for `false`, essa substituição é realizada
somente se o expoente em `%e^x` avaliar para um número.


Veja também `ev` e `numer`.

<!-- category: Other -->
<!-- keywords: at -->
<!-- signatures: at(expr, [eqn_1, ..., eqn_n]), at(expr, eqn) -->
### Function: at (expr, [eqn_1, ..., eqn_n])

Avalia a expressão *expr* com
as variáveis assumindo os valores como especificado para elas na lista de
equações `[eqn_1, ..., eqn_n]` ou a equação simples *eqn*.


Se uma subexpressão depender de qualquer das variáveis para a qual um valor foi especificado
mas não existe `atvalue` especificado e essa subexpressão não pode ser avaliada de outra forma,
então uma forma substantiva de `at` é retornada que mostra em uma forma bidimensional.


`at` realiza múltiplas substituições em série, não em paralelo.


Veja também `atvalue`.
Para outras funções que realizam substituições,
veja também `subst` e `ev`.


Exemplos:











```maxima
(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a
(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1
(%i3) printprops (all, atvalue);
                                !
                  d             !
                 --- (f(@1, @2))!       = @2 + 1
                 d@1            !
                                !@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done
(%i4) diff (4*f(x, y)^2 - u(x, y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx
(%i5) at (%, [x = 0, y = 1]);
                                         !
              2              d           !
(%o5)     16 a  - 2 u(0, 1) (-- (u(x, y))!            )
                             dx          !
                                         !x = 0, y = 1
```

<!-- category: Other -->
<!-- keywords: box -->
<!-- signatures: box(expr), box(expr, a) -->
### Function: box (expr)

Retorna *expr* dentro de uma caixa.
O valor de retorno é uma expressão com `box` como o operador e *expr* como o argumento.
Uma caixa é desenhada sobre a tela quando `display2d` for `true`.


`box (expr, a)`
Empacota *expr* em uma caixa rotulada pelo símbolo *a*.
O rótulo é truncado se for maior que a largura da caixa.


`box` avalia seu argumento.
Todavia, uma expressão dentro de uma caixa não avalia para seu conteúdo,
então expressões dentro de caixas são efetivamente excluídas de cálculos.


`boxchar` é o caractere usado para desenhar a caixa em `box`
e nas funções `dpart` e `lpart`.


Exemplos:













```maxima
(%i1) box (a^2 + b^2);
                            """""""""
                            " 2    2"
(%o1)                       "b  + a "
                            """""""""
(%i2) a : 1234;
(%o2)                         1234
(%i3) b : c - d;
(%o3)                         c - d
(%i4) box (a^2 + b^2);
                      """"""""""""""""""""
                      "       2          "
(%o4)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i5) box (a^2 + b^2, term_1);
                      term_1""""""""""""""
                      "       2          "
(%o5)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i6) 1729 - box (1729);
                                 """"""
(%o6)                     1729 - "1729"
                                 """"""
(%i7) boxchar: "-";
(%o7)                           -
(%i8) box (sin(x) + cos(y));
                        -----------------
(%o8)                   -cos(y) + sin(x)-
                        -----------------
```

<!-- category: Other -->
<!-- keywords: boxchar -->
<!-- signatures: boxchar -->
### Variable: boxchar

Valor padrão: `"`


`boxchar` é o caractere usado para desenhar a caixa por `box`
e nas funções `dpart` e `lpart`.


Todas as caixas em uma expressão são desenhadas com o valor atual de `boxchar`;
o caractere de desenho não é armazenado com a expressão de caixa. Isso quer dizer que se você
desenhar uma caixa e em seguida mudar o caractere de desenho a caixa anteriormente
desenhada será redesenhada com o caractere mudado caso isso seja solicitado.

<!-- category: Other -->
<!-- keywords: carg -->
<!-- signatures: carg(z) -->
### Function: carg (z)

Retorna o argumento complexo de *z*.
O argumento complexo é um ângulo `theta` no intervalo de `(-%pi, %pi]`
tal que `r exp (theta %i) = z` onde `r` é o módulo de *z*.



`carg` é uma função computacional,
não uma função de simplificação.




`carg` ignora a declaração `declare (x, complex)`,
e trata *x* como uma variável real.
Isso é um erro. 


Veja também `abs` (módulo de número complexo), `polarform`, `rectform`,
`realpart`, e `imagpart`.


Exemplos:












```maxima
(%i1) carg (1);
(%o1)                           0
(%i2) carg (1 + %i);
                               %pi
(%o2)                          ---
                                4
(%i3) carg (exp (%i));
(%o3)                           1
(%i4) carg (exp (%pi * %i));
(%o4)                          %pi
(%i5) carg (exp (3/2 * %pi * %i));
                                %pi
(%o5)                         - ---
                                 2
(%i6) carg (17 * exp (2 * %i));
(%o6)                           2
```

<!-- category: Other -->
<!-- keywords: constant -->
<!-- signatures: constant -->
### Function: constant

`declare (a, constant)` declara *a* para ser uma constante.
Veja `declare`.

<!-- category: Other -->
<!-- keywords: constantp -->
<!-- signatures: constantp(expr) -->
### Function: constantp (expr)

Retorna `true` se *expr* for uma expressão constante,
de outra forma retorna `false`.



Uma expressão é considerada uma expressão constante se seus argumentos forem
números (incluindo números racionais, como mostrado com `/R/`),
constantes simbólicas como `%pi`, `%e`, e `%i`,
variáveis associadas a uma constante ou constante declarada através de `declare`,
ou funções cujos argumentos forem constantes.


`constantp` avalia seus argumentos.


Exemplos:













```maxima
(%i1) constantp (7 * sin(2));
(%o1)                                true
(%i2) constantp (rat (17/29));
(%o2)                                true
(%i3) constantp (%pi * sin(%e));
(%o3)                                true
(%i4) constantp (exp (x));
(%o4)                                false
(%i5) declare (x, constant);
(%o5)                                done
(%i6) constantp (exp (x));
(%o6)                                true
(%i7) constantp (foo (x) + bar (%e) + baz (2));
(%o7)                                false
(%i8)
```

<!-- category: Other -->
<!-- keywords: declare -->
<!-- signatures: declare(a_1, p_1, a_2, p_2, ...) -->
### Function: declare (a_1, p_1, a_2, p_2, ...)

Atribui aos átomos ou lista de átomos *a_i* a propriedade ou lista de propriedades *p_i*.
Quando *a_i* e/ou *p_i* forem listas,
cada um dos átomos recebe todas as propriedades.


`declare` não avalia seus argumentos.
`declare` sempre retorna `done`.


Como colocado na descrição para cada sinalizador de declaração,
para alguns sinalizadores
`featurep(objeto, recurso)`
retorna `true` se *objeto* tiver sido declarado para ter *recurso*.
Todavia, `featurep` não reconhece alguns sinalizadores; isso é um erro.


Veja também `features`.


`declare` reconhece as seguintes propriedades:



**`evfun`** — Torna *a_i* conhecido para `ev` de forma que a função nomeada por *a_i*
é aplicada quando *a_i* aparece como um sinalizador argumento de `ev`.
Veja `evfun`.
**`evflag`** — Torna *a_i* conhecido para a função `ev` de forma que *a_i* é associado a `true`
durante a execução de `ev` quando *a_i* aparece como um sinalizador argumento de `ev`.
Veja `evflag`.
**`bindtest`** — Diz ao Maxima para disparar um erro quando *a_i* for avaliado como sendo livre de associação.
**`noun`** — Diz ao Maxima para passar *a_i* como um substantivo. 
O efeito disso é substituir intâncias de *a_i* com `'a_i`
ou `nounify(a_i)`, ependendo do contexto.
**`constant`** — Diz ao Maxima para considerar *a_i* uma constante simbólica.
**`scalar`** — Diz ao Maxima para considerar *a_i* uma variável escalar.
**`nonscalar`** — Diz ao Maxima para considerar *a_i* uma variável não escalar.
The usual application is to declare a variable as a symbolic vector or matrix.
**`mainvar`** — Diz ao Maxima para considerar *a_i* uma "variável principal" (`mainvar`).
`ordergreatp` determina a ordenação de átomos como segue: 
(variáveis principais) > (outras variáveis) > (variáveis escalares) > (constantes) > (números)
**`alphabetic`** — Diz ao Maxima para reconhecer todos os caracteres em *a_i* (que deve ser uma sequência de caracteres) como caractere alfabético.
**`feature`** — Diz ao Maxima para reconhecer *a_i* como nome de um recurso.
Other atoms may then be declared to have the *a_i* property.
**`rassociative`, `lassociative`** — Diz ao Maxima para reconhecer *a_i* como uma funcão associativa a direita ou associativa a esquerda.
**`nary`** — Diz ao Maxima para reconhecer *a_i* como uma função n-ária (com muitos argumentos). 
A declaração `nary` não tem o mesmo objetivo que uma chamada à função `nary`.
O único efeito de `declare(foo, nary)` é para instruir o simplificador do Maxima
a melhorar as próximas expressões,
por exemplo, para simplificar `foo(x, foo(y, z))` para `foo(x, y, z)`.
**`symmetric`, `antisymmetric`, `commutative`** — Diz ao Maxima para reconhecer *a_i* como uma função simétrica ou antisimétrica.
`commutative` é o mesmo que `symmetric`.
**`oddfun`, `evenfun`** — Diz ao Maxima para reconhecer *a_i* como uma função par ou uma função ímpar.
**`outative`** — Diz ao Maxima para simplificar expressões *a_i*
colocando fatores constantes em evidência no primeiro argumento. 
Quando *a_i* tiver um argumento,
um fator é onsiderado constante se for um literal ou se for declarado como sendo constante. 
Quando *a_i* tiver dois ou mais argumentos,
um fator é considerado constante
se o segundo argumento for um símbolo
e o fator estiver livre do segundo argumento.
**`multiplicative`** — Diz ao Maxima para simplificar expressões do tipo *a_i*
através da substituição `a_i(x * y * z * ...)` `-->`
`a_i(x) * a_i(y) * a_i(z) * ...`.
A substituição é realizada no primeiro argumento somente.
**`additive`** — Diz ao Maxima para simplificar expressões do tipo *a_i*
através da substituição `a_i(x + y + z + ...)` `-->`
`a_i(x) + a_i(y) + a_i(z) + ...`.
A substituição é realizada no primeiro argumento somente.
**`linear`** — Equivalente a declarar *a_i* ao mesmo tempo `outative` e `additive`.
**`integer`, `noninteger`** — Diz ao Maxima para reconhecer *a_i* como como uma variável inteira ou como uma variável não inteira.   Maxima reconhece os seguintes recursos de objetos:
**`even`, `odd`** — Diz ao Maxima para reconhecer *a_i* como uma variável inteira par ou como uma variável inteira ímpar.
**`rational`, `irrational`** — Diz ao Maxima para reconhecer *a_i* como uma variável real e racional ou como uma variável real e irracional.
**`real`, `imaginary`, `complex`** — Dia ao Maxima para reconhecer *a_i* como uma variável real, imaginária pura ou complexa.
**`increasing`, `decreasing`** — Dia ao Maxima para reconhecer *a_i* como uma função de incremento ou decremento.
**`posfun`** — Diz ao Maxima para reconhecer *a_i* como uma função positiva.
**`integervalued`** — Diz ao Maxima para reconhecer *a_i* como uma função de valores inteiros.


Exemplos:


Declarações `evfun` e `evflag`.










```maxima
(%i1) declare (expand, evfun);
(%o1)                         done
(%i2) (a + b)^3;
                                   3
(%o2)                       (b + a)
(%i3) (a + b)^3, expand;
                     3        2      2      3
(%o3)               b  + 3 a b  + 3 a  b + a
(%i4) declare (demoivre, evflag);
(%o4)                         done
(%i5) exp (a + b*%i);
                             %i b + a
(%o5)                      %e
(%i6) exp (a + b*%i), demoivre;
                      a
(%o6)               %e  (%i sin(b) + cos(b))
```


Declaração `bindtest`.









```maxima
(%i1) aa + bb;
(%o1)                        bb + aa
(%i2) declare (aa, bindtest);
(%o2)                         done
(%i3) aa + bb;
aa unbound variable
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) aa : 1234;
(%o4)                         1234
(%i5) aa + bb;
(%o5)                       bb + 1234
```


Declaração `noun`.








```maxima
(%i1) factor (12345678);
                             2
(%o1)                     2 3  47 14593
(%i2) declare (factor, noun);
(%o2)                         done
(%i3) factor (12345678);
(%o3)                   factor(12345678)
(%i4) ''%, nouns;
                             2
(%o4)                     2 3  47 14593
```


Declarações `constant`, `scalar`, `nonscalar`, e `mainvar`.








```maxima

```


Declaração `alphabetic`.








```maxima
(%i1) xx\~yy\`\@ : 1729;
(%o1)                         1729
(%i2) declare ("~`@", alphabetic);
(%o2)                         done
(%i3) xx~yy`@ + @yy`xx + `xx@@yy~;
(%o3)               `xx@@yy~ + @yy`xx + 1729
(%i4) listofvars (%);
(%o4)                  [@yy`xx, `xx@@yy~]
```


Declaração `feature`.







```maxima
(%i1) declare (FOO, feature);
(%o1)                         done
(%i2) declare (x, FOO);
(%o2)                         done
(%i3) featurep (x, FOO);
(%o3)                         true
```


Declarações `rassociative` e `lassociative`.






```maxima

```


Declaração `nary`.







```maxima
(%i1) H (H (a, b), H (c, H (d, e)));
(%o1)               H(H(a, b), H(c, H(d, e)))
(%i2) declare (H, nary);
(%o2)                         done
(%i3) H (H (a, b), H (c, H (d, e)));
(%o3)                   H(a, b, c, d, e)
```


Declarações `symmetric` e `antisymmetric`.












```maxima
(%i1) S (b, a);
(%o1)                        S(b, a)
(%i2) declare (S, symmetric);
(%o2)                         done
(%i3) S (b, a);
(%o3)                        S(a, b)
(%i4) S (a, c, e, d, b);
(%o4)                   S(a, b, c, d, e)
(%i5) T (b, a);
(%o5)                        T(b, a)
(%i6) declare (T, antisymmetric);
(%o6)                         done
(%i7) T (b, a);
(%o7)                       - T(a, b)
(%i8) T (a, c, e, d, b);
(%o8)                   T(a, b, c, d, e)
```


Declarações `oddfun` e `evenfun`.










```maxima
(%i1) o (- u) + o (u);
(%o1)                     o(u) + o(- u)
(%i2) declare (o, oddfun);
(%o2)                         done
(%i3) o (- u) + o (u);
(%o3)                           0
(%i4) e (- u) - e (u);
(%o4)                     e(- u) - e(u)
(%i5) declare (e, evenfun);
(%o5)                         done
(%i6) e (- u) - e (u);
(%o6)                           0
```


Declaração `outative`.









```maxima
(%i1) F1 (100 * x);
(%o1)                       F1(100 x)
(%i2) declare (F1, outative);
(%o2)                         done
(%i3) F1 (100 * x);
(%o3)                       100 F1(x)
(%i4) declare (zz, constant);
(%o4)                         done
(%i5) F1 (zz * y);
(%o5)                       zz F1(y)
```


Declaração `multiplicative`.







```maxima
(%i1) F2 (a * b * c);
(%o1)                       F2(a b c)
(%i2) declare (F2, multiplicative);
(%o2)                         done
(%i3) F2 (a * b * c);
(%o3)                   F2(a) F2(b) F2(c)
```


Declaração `additive`.







```maxima
(%i1) F3 (a + b + c);
(%o1)                     F3(c + b + a)
(%i2) declare (F3, additive);
(%o2)                         done
(%i3) F3 (a + b + c);
(%o3)                 F3(c) + F3(b) + F3(a)
```


Declaração `linear`.







```maxima
(%i1) 'sum (F(k) + G(k), k, 1, inf);
                       inf
                       ====
                       \
(%o1)                   >    (G(k) + F(k))
                       /
                       ====
                       k = 1
(%i2) declare (nounify (sum), linear);
(%o2)                         done
(%i3) 'sum (F(k) + G(k), k, 1, inf);
                     inf          inf
                     ====         ====
                     \            \
(%o3)                 >    G(k) +  >    F(k)
                     /            /
                     ====         ====
                     k = 1        k = 1
```

<!-- category: Other -->
<!-- keywords: disolate -->
<!-- signatures: disolate(expr, x_1, ..., x_n) -->
### Function: disolate (expr, x_1, ..., x_n)

é similar a `isolate (expr, x)`
exceto que essa função habilita ao usuário isolar
mais que uma variável simultâneamente.  Isso pode ser útil, por
exemplo, se se tiver tentado mudar variáveis em uma integração
múltipla, e em mudança de variável envolvendo duas ou mais das
variáveis de integração.  Essa função é chamada automaticamente de
`simplification/disol.mac`.  Uma demostração está disponível através de
`demo("disol")$`.

<!-- category: Other -->
<!-- keywords: dispform -->
<!-- signatures: dispform(expr) -->
### Function: dispform (expr)

Retorna a representação externa de *expr* com relação a seu
principal operador.  Isso pode ser útil em conjunção com `part` que
também lida com a representação externa.  Suponha que *expr* seja -A .
Então a representação interna de *expr* é  "*"(-1,A), enquanto que
a representação externa é "-"(A). `dispform (expr, all)` converte a
expressão inteira (não apenas o nível mais alto) para o formato externo.  Por
exemplo, se `expr: sin (sqrt (x))`, então `freeof (sqrt, expr)` e
`freeof (sqrt, dispform (expr))` fornece `true`, enquanto
`freeof (sqrt, dispform (expr, all))` fornece `false`.

<!-- category: Other -->
<!-- keywords: distrib -->
<!-- signatures: distrib(expr) -->
### Function: distrib (expr)

Distribue adições sobre produtos.  `distrib` difere de `expand`
no fato de que `distrib` trabalha em somente no nível mais alto de uma expressão, i.e., `distrib` não
é recursiva e `distrib` é mais rápida que `expand`.  `distrib` difere de `multthru` no
que `distrib` expande todas as adições naquele nível.


Exemplos:



```maxima
(%i1) distrib ((a+b) * (c+d));
(%o1)                 b d + a d + b c + a c
(%i2) multthru ((a+b) * (c+d));
(%o2)                 (b + a) d + (b + a) c
(%i3) distrib (1/((a+b) * (c+d)));
                                1
(%o3)                    ---------------
                         (b + a) (d + c)
(%i4) expand (1/((a+b) * (c+d)), 1, 0);
                                1
(%o4)                 ---------------------
                      b d + a d + b c + a c
```

<!-- category: Other -->
<!-- keywords: dpart -->
<!-- signatures: dpart(expr, n_1, ..., n_k) -->
### Function: dpart (expr, n_1, ..., n_k)

Seleciona a mesma subexpressão que `part`, mas
em lugar de apenas retornar aquela subexpressão como seu valor, isso retorna
a expressão completa com a subexpressão selecionada mostrada dentro
de uma caixa.  A caixa é atualmente parte da expressão.



```maxima
(%i1) dpart (x+y/z^2, 1, 2, 1);
                             y
(%o1)                       ---- + x
                               2
                            """
                            "z"
                            """
```

<!-- category: Other -->
<!-- keywords: exp -->
<!-- signatures: exp(x) -->
### Function: exp (x)

Representa função exponencial.  
Instâncias de `exp (x)` em uma entrada são simplificadas para `%e^x`;
`exp` não aparece em expressões simplificadas.


`demoivre` se `true` faz com que `%e^(a + b %i)` simplificar para
`%e^(a (cos(b) + %i sin(b)))` se `b` for livre de `%i`. veja `demoivre`.


`%emode`, quando `true`, 
faz com que `%e^(%pi %i x)` seja simplificado. Veja `%emode`.


`%enumer`, quando `true` faz com que `%e` seja substituído por
2.718...  quando `numer` for `true`. Veja `%enumer`.

<!-- category: Other -->
<!-- keywords: exptisolate -->
<!-- signatures: exptisolate -->
### Variable: exptisolate

Valor padrão: `false`



`exptisolate`, quando `true`, faz com que `isolate (expr, var)`
examine expoentes de átomos (tais como `%e`) que contenham `var`.

<!-- category: Other -->
<!-- keywords: exptsubst -->
<!-- signatures: exptsubst -->
### Variable: exptsubst

Valor padrão: `false`


`exptsubst`, quando `true`, permite substituições tais como `y`
para `%e^x` em `%e^(a x)`.

<!-- category: Other -->
<!-- keywords: freeof -->
<!-- signatures: freeof(x_1, ..., x_n, expr) -->
### Function: freeof (x_1, ..., x_n, expr)

`freeof (x_1, expr)`
Retorna `true`
se nenhuma subexpressão de *expr* for igual a *x_1*
ou se *x_1* ocorrer somente uma variável que não tenha associação fora da expressão *expr*,
e retorna `false` de outra forma.


`freeof (x_1, ..., x_n, expr)`
é equivalente a `freeof (x_1, expr) and ... and freeof (x_n, expr)`.


Os argumentos *x_1*, ..., *x_n* 
podem ser nomes de funções e variáveis, nomes subscritos,
operadores (empacotados em aspas duplas), ou expressões gerais.
`freeof` avalia seus argumentos.


`freeof` opera somente sobre *expr* como isso representa (após simplificação e avaliação) e
não tenta determinar se alguma expressão equivalente pode fornecer um resultado diferente.
Em particular, simplificação pode retornar uma expressão equivalente mas diferente que compreende
alguns diferentes elementos da forma original de *expr*.


Uma variável é uma variável dummy em uma expressão se não tiver associação fora da expressão.
Variáveis dummy recoreconhecidas através de `freeof` são
o índice de um somatório ou produtório, o limite da variável em `limit`,
a variável de integração na forma de integral definida de `integrate`,
a variável original em `laplace`,
variáveis formais em expressoes `at`,
e argumentos em expressões `lambda`.
Variáveis locais em `block` não são reconhecidas por `freeof` como variáveis dummy;
isso é um bug.


A forma indefinida de `integrate` *not* é livre de suas variáveis de integração.



- *
Argumentos são nomes de funções, variáveis, nomes subscritos, operadores, e expressões.
`freeof (a, b, expr)` é equivalente a
`freeof (a, expr) and freeof (b, expr)`.

```maxima
(%i1) expr: z^3 * cos (a[1]) * b^(c+d);
                                 d + c  3
(%o1)                   cos(a ) b      z
                             1
(%i2) freeof (z, expr);
(%o2)                         false
(%i3) freeof (cos, expr);
(%o3)                         false
(%i4) freeof (a[1], expr);
(%o4)                         false
(%i5) freeof (cos (a[1]), expr);
(%o5)                         false
(%i6) freeof (b^(c+d), expr);
(%o6)                         false
(%i7) freeof ("^", expr);
(%o7)                         false
(%i8) freeof (w, sin, a[2], sin (a[2]), b*(c+d), expr);
(%o8)                         true
```
- *
`freeof` avalia seus argumentos.

```maxima
(%i1) expr: (a+b)^5$
(%i2) c: a$
(%i3) freeof (c, expr);
(%o3)                         false
```
- *
`freeof` não considera expressões equivalentes.
Simplificação pode retornar uma expressão equivalente mas diferente.

```maxima
(%i1) expr: (a+b)^5$
(%i2) expand (expr);
          5        4       2  3       3  2      4      5
(%o2)    b  + 5 a b  + 10 a  b  + 10 a  b  + 5 a  b + a
(%i3) freeof (a+b, %);
(%o3)                         true
(%i4) freeof (a+b, expr);
(%o4)                         false
(%i5) exp (x);
                                 x
(%o5)                          %e
(%i6) freeof (exp, exp (x));
(%o6)                         true
```
- * 
Um somatório ou uma integral definida está livre de uma variável dummy.
Uma integral indefinida não é livre de suas variáveis de integração.

```maxima
(%i1) freeof (i, 'sum (f(i), i, 0, n));
(%o1)                         true
(%i2) freeof (x, 'integrate (x^2, x, 0, 1));
(%o2)                         true
(%i3) freeof (x, 'integrate (x^2, x));
(%o3)                         false
```

<!-- category: Other -->
<!-- keywords: genfact -->
<!-- signatures: genfact(x, y, z) -->
### Function: genfact (x, y, z)

Retorna o fatorial generalizado, definido como
`x (x-z) (x - 2 z) ... (x - (y - 1) z)`.  Dessa forma, para integral *x*,
`genfact (x, x, 1) = x!` e `genfact (x, x/2, 2) = x!!`.

<!-- category: Other -->
<!-- keywords: imagpart -->
<!-- signatures: imagpart(expr) -->
### Function: imagpart (expr)

Retorna a parte imaginária da expressão *expr*.


`imagpart` é uma função computacional,
não uma função de simplificação.




Veja também `abs`, `carg`, `polarform`, `rectform`,
e `realpart`.

<!-- category: Other -->
<!-- keywords: infix -->
<!-- signatures: infix(op), infix(op, lbp, rbp), infix(op, lbp, rbp, lpos, rpos, pos) -->
### Function: infix (op)

Declara *op* para ser um operador infixo.
Um operador infixo é uma função de dois argumentos,
com o nome da função escrito entre os argumentos.
Por exemplo, o operador de subtração `-` é um operador infixo.


`infix (op)` declara *op* para ser um operador infixo
com expoentes associados padrão (esquerdo e direito ambos iguais a 180)
e podendo ser qualquer entre prefixado, infixado, posfixado, nário, 
matchfix e nofix (esquerdo e direito ambos iguais a `any`).



`infix (op, lbp, rbp)` declara *op* para ser um operador infixo
com expoentes associados esquerdo e diretio equilibrados
e podendo ser qualquer entre prefixado, infixado, posfixado, nário, 
matchfix e nofix (esquerdo e direito ambos iguais a `any`).


`infix (op, lbp, rbp, lpos, rpos, pos)`
declara *op* para ser um operdor infixo
com expoentes associados padrão e podendo ser um entre 
prefixado, infixado, posfixado, nário, matchfix e nofix.


A precedência de *op* com relação a outros operadores
derivam dos expoentes associados diretiro e esquerdo dos operadores em questão.
Se os expoentes associados esquerdo e direito de *op* forem ambos maiores
que o expoente associado esquerdo e o direito de algum outro operador,
então *op* tem prededência sobre o outro operador.
Se os expoentes associados não forem ambos maior ou menor,
alguma relação mais complicada ocorre.


A associatividade de *op* depende de seus expoentes associados.
Maior expoente associado esquerdo (*eae*) implica uma instância de
*op* é avaliadas antes de outros operadores para sua esquerda em uma expressão,
enquanto maior expoente associado direito (*ead*) implica uma instância de
*op* é avaliada antes de outros operadores para sua direita em uma expressão.
Dessa forma maior *eae* torna *op* associativo à direita,
enquanto maior *ead* torna *op* associativa à esquerda.
Se *eae* for igual a *ead*, *op* é associativa à esquerda.


Veja também `Syntax`.


Exemplos:


Se os expoentes associados esquerdo e direito de *op* forem ambos maiores
que os expoentes associados à direita e à esquerda de algum outro operador,
então *op* tem precedência sobre o outro operador.












```maxima
(%i1) :lisp (get '$+ 'lbp)
100
(%i1) :lisp (get '$+ 'rbp)
100
(%i1) infix ("##", 101, 101);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")");
(%o2)       (a ## b) := sconcat("(", a, ",", b, ")")
(%i3) 1 + a ## b + 2;
(%o3)                       (a,b) + 3
(%i4) infix ("##", 99, 99);
(%o4)                          ##
(%i5) 1 + a ## b + 2;
(%o5)                       (a+1,b+2)
```


grande *eae* torna *op* associativa à direita,
enquanto grande *ead* torna *op* associativa à esquerda.










```maxima
(%i1) infix ("##", 100, 99);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")")$
(%i3) foo ## bar ## baz;
(%o3)                    (foo,(bar,baz))
(%i4) infix ("##", 100, 101);
(%o4)                          ##
(%i5) foo ## bar ## baz;
(%o5)                    ((foo,bar),baz)
```

<!-- category: Other -->
<!-- keywords: inflag -->
<!-- signatures: inflag -->
### Variable: inflag

Velor padrão: `false`


Quando `inflag` for `true`, funções para extração de
partes inspecionam a forma interna de `expr`.


Note que o simplificador re-organiza expressões.
Dessa forma `first (x + y)` retorna `x` se `inflag`
for `true` e `y` se `inflag` for `false`.
(`first (y + x)` fornece os mesmos resultados.)


Também, escolhendo `inflag` para `true` e chamando `part` ou `substpart` é
o mesmo que chamar `inpart` ou `substinpart`.


As funções afetadas pela posição do sinalizador `inflag` são:
`part`, `substpart`, `first`, `rest`, `last`, `length`,
a estrutura `for` ... `in`,
`map`, `fullmap`, `maplist`, `reveal` e `pickapart`.

<!-- category: Other -->
<!-- keywords: inpart -->
<!-- signatures: inpart(expr, n_1, ..., n_k) -->
### Function: inpart (expr, n_1, ..., n_k)

É similar a `part` mas trabalha sobre a representação
interna da expressão em lugar da forma de exibição e
dessa forma pode ser mais rápida uma vez que nenhuma formatação é realizada.  Cuidado deve ser tomado
com relação à ordem de subexpressões em adições e produtos
(uma vez que a ordem das variáveis na forma interna é muitas vezes diferente
daquela na forma mostrada) e no manuseio com menos unário,
subtração, e divisão (uma vez que esses operadores são removidos da
expressão). `part (x+y, 0)` ou `inpart (x+y, 0)` retorna `+`, embora com o objetivo de
referirse ao operador isso deva ser abraçado por aspas duplas.  Por exemplo
`... if inpart (%o9,0) = "+" then ...`.


Exemplos:



```maxima
(%i1) x + y + w*z;
(%o1)                      w z + y + x
(%i2) inpart (%, 3, 2);
(%o2)                           z
(%i3) part (%th (2), 1, 2);
(%o3)                           z
(%i4) 'limit (f(x)^g(x+1), x, 0, minus);
                                  g(x + 1)
(%o4)                 limit   f(x)
                      x -> 0-
(%i5) inpart (%, 1, 2);
(%o5)                       g(x + 1)
```

<!-- category: Other -->
<!-- keywords: isolate -->
<!-- signatures: isolate(expr, x) -->
### Function: isolate (expr, x)

Retorna *expr* com subexpressões que são adições e
que não possuem *x* substituido por rótulos de expressão intermediária
(esses sendo símbolos atômicos como `%t1`, `%t2`, ...).  Isso é muitas vezes útil
para evitar expansões desnecessárias de subexpressões que não possuam
a variável de interesse.  Uma vez que os rótulos intermediários são associados às
subexpressões eles podem todos ser substituídos de volta por avaliação da
expressão em que ocorrerem.


`exptisolate` (valor padrão: `false`) se `true` fará com que `isolate` examine expoentes de
átomos (como `%e`) que contenham *x*.


`isolate_wrt_times` se `true`, então `isolate` irá também isolar com relação a 
produtos. Veja `isolate_wrt_times`.


Faça `example (isolate)` para exemplos.

<!-- category: Other -->
<!-- keywords: isolate_wrt_times -->
<!-- signatures: isolate_wrt_times -->
### Variable: isolate_wrt_times

Valor padrão: `false`


Quando `isolate_wrt_times` for `true`, `isolate`
irá também isolar com relação a produtos.  E.g. compare ambas as escolhas do
comutador em



```maxima
(%i1) isolate_wrt_times: true$
(%i2) isolate (expand ((a+b+c)^2), c);

(%t2)                          2 a


(%t3)                          2 b


                          2            2
(%t4)                    b  + 2 a b + a

                     2
(%o4)               c  + %t3 c + %t2 c + %t4
(%i4) isolate_wrt_times: false$
(%i5) isolate (expand ((a+b+c)^2), c);
                     2
(%o5)               c  + 2 b c + 2 a c + %t4
```

<!-- category: Other -->
<!-- keywords: lfreeof -->
<!-- signatures: lfreeof(lista, expr) -->
### Function: lfreeof (lista, expr)

Para cada um dos membros *m* de lista, chama `freeof (m, expr)`.
Retorna `false` se qualquer chamada a `freeof` for feita e `true` de outra forma.

<!-- category: Other -->
<!-- keywords: listconstvars -->
<!-- signatures: listconstvars -->
### Variable: listconstvars

Valor padrão: `false`


Quando `listconstvars` for `true`, isso fará com que `listofvars`
inclua `%e`, `%pi`, `%i`, e quaisquer variáveis declaradas contantes na lista
seja retornado se aparecer na expressão que chamar `listofvars`.
O comportamento padrão é omitir isso.

<!-- category: Other -->
<!-- keywords: listdummyvars -->
<!-- signatures: listdummyvars -->
### Variable: listdummyvars

Valor padrão: `true`


Quando `listdummyvars` for `false`, "variáveis dummy" na
expressão não serão incluídas na lista retornada por `listofvars`.
(O significado de "variável dummy" é o mesmo que em `freeof`.
"Variáveis dummy" são conceitos matemáticos como o índice de um somatório ou
produtório, a variável limite, e a variável da integral definida.)
Exemplo:



```maxima
(%i1) listdummyvars: true$
(%i2) listofvars ('sum(f(i), i, 0, n));
(%o2)                        [i, n]
(%i3) listdummyvars: false$
(%i4) listofvars ('sum(f(i), i, 0, n));
(%o4)                          [n]
```

<!-- category: Other -->
<!-- keywords: listofvars -->
<!-- signatures: listofvars(expr) -->
### Function: listofvars (expr)

Retorna uma lista de variáveis em *expr*.


`listconstvars` se `true` faz com que `listofvars` inclua `%e`, `%pi`,
`%i`, e quaisquer variáveis declaradas constantes na lista é retornada se
aparecer em *expr*.  O comportamento padrão é omitir isso.



```maxima
(%i1) listofvars (f (x[1]+y) / g^(2+a));
(%o1)                     [g, a, x , y]
                                  1
```

<!-- category: Other -->
<!-- keywords: lopow -->
<!-- signatures: lopow(expr, x) -->
### Function: lopow (expr, x)

Retorna o menor expoente de *x* que explicitamente aparecer em
*expr*.  Dessa forma



```maxima
(%i1) lopow ((x+y)^2 + (x+y)^a, x+y);
(%o1)                       min(a, 2)
```

<!-- category: Other -->
<!-- keywords: lpart -->
<!-- signatures: lpart(rótulo, expr, n_1, ..., n_k) -->
### Function: lpart (rótulo, expr, n_1, ..., n_k)

é similar a `dpart` mas usa uma
caixa rotulada. Uma moldura rotulada é similar à que é produzida por `dpart`
mas a produzida por `lpart` tem o nome na linha do topo.

<!-- category: Other -->
<!-- keywords: lsum -->
<!-- signatures: lsum(expr, x, L) -->
### Function: lsum (expr, x, L)

Representas a adição de *expr* a cada elemento *x* em *L*.


Uma forma substantiva `'lsum` é retornada
se o argumento *L* não avaliar para uma lista.


Exemplos:







```maxima
(%i1) lsum (x^i, i, [1, 2, 7]);
                            7    2
(%o1)                      x  + x  + x
(%i2) lsum (i^2, i, rootsof (x^3 - 1, x));
                     ====
                     \      2
(%o2)                 >    i
                     /
                     ====
                                   3
                     i in rootsof(x  - 1, x)
```

<!-- category: Other -->
<!-- keywords: multthru -->
<!-- signatures: multthru(expr), multthru(expr_1, expr_2) -->
### Function: multthru (expr)

Multiplica um fator (que pode ser uma adição) de *expr* pelos
outros fatores de *expr*.  Isto é, *expr* é `f_1 f_2 ... f_n`
onde ao menos
um fator, digamos *f_i*, é uma soma de termos.  Cada termo naquela soma é
multiplicado por outros fatores no produto.  (A saber todos os
fatores exceto *f_i*).  `multthru` não expande somas exponenciais.
Essa função é o caminho mais rápido para distribuir produtos (comutativos
ou não) sobre adições.  Uma vez que quocientes são representados como
produtos `multthru` podem ser usados para dividir adições por produtos também.


`multthru (expr_1, expr_2)` multiplica cada termo em *expr_2* (que pode ser uma
adição ou uma equção) por *expr_1*.  Se *expr_1* não for por si mesmo uma adição então essa
forma é equivalente a `multthru (expr_1*expr_2)`.



```maxima
(%i1) x/(x-y)^2 - 1/(x-y) - f(x)/(x-y)^3;
                      1        x         f(x)
(%o1)             - ----- + -------- - --------
                    x - y          2          3
                            (x - y)    (x - y)
(%i2) multthru ((x-y)^3, %);
                           2
(%o2)             - (x - y)  + x (x - y) - f(x)
(%i3) ratexpand (%);
                           2
(%o3)                   - y  + x y - f(x)
(%i4) ((a+b)^10*s^2 + 2*a*b*s + (a*b)^2)/(a*b*s^2);
                        10  2              2  2
                 (b + a)   s  + 2 a b s + a  b
(%o4)            ------------------------------
                                  2
                             a b s
(%i5) multthru (%);  /* note que isso não expande (b+a)^10 */
                                        10
                       2   a b   (b + a)
(%o5)                  - + --- + ---------
                       s    2       a b
                           s
(%i6) multthru (a.(b+c.(d+e)+f));
(%o6)            a . f + a . c . (e + d) + a . b
(%i7) expand (a.(b+c.(d+e)+f));
(%o7)         a . f + a . c . e + a . c . d + a . b
```

<!-- category: Other -->
<!-- keywords: nounify -->
<!-- signatures: nounify(f) -->
### Function: nounify (f)

Retorna a forma substantiva do nome da função *f*.  Isso é
necessário se se quer referir ao nome de uma função verbo como se esse nome
fosse um substantivo.  Note que algumas funções verbos irão retornar sua forma
substantiva senão puderem ser avaliadas para certos argumentos.  A forma substantiva é também
a forma retornada se uma chamada de função é precedida por um apóstrofo.

<!-- category: Other -->
<!-- keywords: nterms -->
<!-- signatures: nterms(expr) -->
### Function: nterms (expr)

Retorna o número de termos que *expr* pode ter se for
completamente expandida e nenhum cancelamento ou combinação de termos
acontecer.
Note expressões como `sin (expr)`, `sqrt (expr)`, `exp (expr)`, etc.
contam como apenas um termo independentemente de quantos termos *expr* tenha (se *expr* for uma
adição).

<!-- category: Other -->
<!-- keywords: op -->
<!-- signatures: op(expr) -->
### Function: op (expr)

Retorna o operador principal da expressão *expr*.
`op (expr)` é equivalente a `part (expr, 0)`. 


`op` retorna uma sequência de caracteres se o operador principal for uma
operador interno ou definido pelo usuário como
prefixado, binário ou n-ário infixo, posfixado, matchfix ou nofix.
De outra forma, se *expr* for uma expressão de função subscrita,
`op` retorna uma função subscrita;
nesse caso o valor de retorno não é um átomo.
De outro modo, *expr* é uma função de array ou uma expressão de função comum,
e `op` retorna um símbolo.


`op` observa o valor do sinalizador global `inflag`.


`op` avalia seus argumentos.


Veja também `args`.


Exemplos:



















```maxima
(%i1) stringdisp: true$
(%i2) op (a * b * c);
(%o2)                          "*"
(%i3) op (a * b + c);
(%o3)                          "+"
(%i4) op ('sin (a + b));
(%o4)                          sin
(%i5) op (a!);
(%o5)                          "!"
(%i6) op (-a);
(%o6)                          "-"
(%i7) op ([a, b, c]);
(%o7)                          "["
(%i8) op ('(if a > b then c else d));
(%o8)                         "if"
(%i9) op ('foo (a));
(%o9)                          foo
(%i10) prefix (foo);
(%o10)                        "foo"
(%i11) op (foo a);
(%o11)                        "foo"
(%i12) op (F [x, y] (a, b, c));
(%o12)                        F
                               x, y
(%i13) op (G [u, v, w]);
(%o13)                          G
```

<!-- category: Other -->
<!-- keywords: operatorp -->
<!-- signatures: operatorp(expr, op), operatorp(expr, [op_1, ..., op_n]) -->
### Function: operatorp (expr, op)

`operatorp (expr, op)` retorna `true`
se *op* for igual ao operador de *expr*.


`operatorp (expr, [op_1, ..., op_n])` retorna `true`
se algum elementos de *op_1*, ..., *op_n* for igual ao operador de *expr*.

<!-- category: Other -->
<!-- keywords: optimize -->
<!-- signatures: optimize(expr) -->
### Function: optimize (expr)

Retorna uma expressão que produz o mesmo valor e
efeito que *expr* mas faz de forma mais eficientemente por evitar a
recomputação de subexpressões comuns.  `optimize` também tem o mesmo
efeito de "colapsar" seus argumentos de forma que todas as subexpressões comuns
são compartilhadas.
Faça `example (optimize)` para exemplos.

<!-- category: Other -->
<!-- keywords: optimprefix -->
<!-- signatures: optimprefix -->
### Variable: optimprefix

Valor padrão: `%`


`optimprefix` é o prefixo usado para símbolos gerados pelo
comando `optimize`.

<!-- category: Other -->
<!-- keywords: ordergreat -->
<!-- signatures: ordergreat(v_1, ..., v_n) -->
### Function: ordergreat (v_1, ..., v_n)

Escolhe aliases para as variáveis *v_1*, ..., *v_n*
tais que *v_1* > *v_2* > ...  > *v_n*,
e *v_n* > qualquer outra variável não mencionada como um
argumento.


Veja também `orderless`.

<!-- category: Other -->
<!-- keywords: ordergreatp -->
<!-- signatures: ordergreatp(expr_1, expr_2) -->
### Function: ordergreatp (expr_1, expr_2)

Retorna `true` se *expr_2* precede *expr_1* na
ordenação escolhida com a função `ordergreat`.

<!-- category: Other -->
<!-- keywords: orderless -->
<!-- signatures: orderless(v_1, ..., v_n) -->
### Function: orderless (v_1, ..., v_n)

Escolhe aliases para as variáveis *v_1*, ..., *v_n*
tais que *v_1* < *v_2* < ...  < *v_n*,
and *v_n* < qualquer outra variável não mencionada como um
argumento.



Dessa forma a escala de ordenação completa é: constantes numéricas <
constantes declaradas < escalares declarados < primeiro argumento para `orderless` <
...  < último argumento para `orderless` < variáveis que começam com A < ...
< variáveis que começam com Z < último argumento para `ordergreat` <
 ... < primeiro argumento para `ordergreat` < `mainvar`s - variáveis principais declaradas.


Veja também `ordergreat` e `mainvar`.

<!-- category: Other -->
<!-- keywords: orderlessp -->
<!-- signatures: orderlessp(expr_1, expr_2) -->
### Function: orderlessp (expr_1, expr_2)

Retorna `true` se *expr_1* precede *expr_2* na
ordenação escolhida pelo comando `orderless`.

<!-- category: Other -->
<!-- keywords: part -->
<!-- signatures: part(expr, n_1, ..., n_k) -->
### Function: part (expr, n_1, ..., n_k)

Retorna partes da forma exibida de `expr`. Essa função
obtém a parte de `expr` como especificado pelos índices *n_1*, ..., *n_k*.  A primeira
parte *n_1* de `expr` é obtida, então a parte *n_2* daquela  é obtida, etc.  O resultado é
parte *n_k* de ... parte *n_2* da parte *n_1* da `expr`.


`part` pode ser usada para obter um elemento de uma lista, uma linha de uma matriz, etc.




Se o último argumento para uma função `part` for uma lista de índices então
muitas subexpressões serão pinçadas, cada uma correspondendo a um
índice da lista.  Dessa forma `part (x + y + z, [1, 3])` é `z+x`.


`piece` mantém a última expressão selecionada quando usando as funções
`part`.  Isso é escolhido durante a execução da função e dessa forma
pode referir-se à função em si mesma como mostrado abaixo.


Se `partswitch` for escolhido para `true` então `end` é retornado quando uma
parte selecionada de uma expressão não existir, de outra forma uma mensagem de
erro é forncecida.




Exemplo: `part (z+2*y, 2, 1)` retorna 2.



`example (part)` mostra exemplos adicionais.

<!-- category: Other -->
<!-- keywords: partition -->
<!-- signatures: partition(expr, x) -->
### Function: partition (expr, x)

Retorna uma lista de duas expressões.  Elas são (1)
os fatores de *expr* (se essa expressão for um produto), os termos de *expr* (se isso for uma
adição), ou a lista (se isso for uma lsita) que não contiver `var` e, (2)
os fatores, termos, ou lista que faz.



```maxima
(%i1) partition (2*a*x*f(x), x);
(%o1)                     [2 a, x f(x)]
(%i2) partition (a+b, x);
(%o2)                      [b + a, 0]
(%i3) partition ([a, b, f(a), c], a); 
(%o3)                  [[b, c], [a, f(a)]]
```

<!-- category: Other -->
<!-- keywords: partswitch -->
<!-- signatures: partswitch -->
### Variable: partswitch

Valor padrão: `false`


Quando `partswitch` for `true`, `end` é retornado
quando uma parte selecionada de uma expressão não existir, de outra forma uma
mensagem de erro é fornecida.

<!-- category: Other -->
<!-- keywords: pickapart -->
<!-- signatures: pickapart(expr, n) -->
### Function: pickapart (expr, n)

Atribui rótulos de expressão intermediária a subexpressões de
*expr* de comprimento *n*, um inteiro.
A subexpressões maiores ou menores não são atribuidos rótulos.
`pickapart` retorna uma expressão em termos de expressões intermediárias
equivalentes à expressão original *expr*.


Veja também `part`, `dpart`, `lpart`, `inpart`, e `reveal`.


Exemplos:



```maxima
(%i1) expr: (a+b)/2 + sin (x^2)/3 - log (1 + sqrt(x+1));
                                          2
                                     sin(x )   b + a
(%o1)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2
(%i2) pickapart (expr, 0);

                                          2
                                     sin(x )   b + a
(%t2)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2

(%o2)                          %t2
(%i3) pickapart (expr, 1);

(%t3)                - log(sqrt(x + 1) + 1)


                                  2
                             sin(x )
(%t4)                        -------
                                3


                              b + a
(%t5)                         -----
                                2

(%o5)                    %t5 + %t4 + %t3
(%i5) pickapart (expr, 2);

(%t6)                 log(sqrt(x + 1) + 1)


                                  2
(%t7)                        sin(x )


(%t8)                         b + a

                         %t8   %t7
(%o8)                    --- + --- - %t6
                          2     3
(%i8) pickapart (expr, 3);

(%t9)                    sqrt(x + 1) + 1


                                2
(%t10)                         x

                  b + a              sin(%t10)
(%o10)            ----- - log(%t9) + ---------
                    2                    3
(%i10) pickapart (expr, 4);

(%t11)                     sqrt(x + 1)

                      2
                 sin(x )   b + a
(%o11)           ------- + ----- - log(%t11 + 1)
                    3        2
(%i11) pickapart (expr, 5);

(%t12)                        x + 1

                   2
              sin(x )   b + a
(%o12)        ------- + ----- - log(sqrt(%t12) + 1)
                 3        2
(%i12) pickapart (expr, 6);
                  2
             sin(x )   b + a
(%o12)       ------- + ----- - log(sqrt(x + 1) + 1)
                3        2
```

<!-- category: Other -->
<!-- keywords: piece -->
<!-- signatures: piece -->
### Variable: piece

Mantém a ultima expressão selecionada quando usando funções
`part`.

Isso é escolhido durante a execução da função e dessa forma
pode referir-se à função em si mesma.

<!-- category: Other -->
<!-- keywords: polarform -->
<!-- signatures: polarform(expr) -->
### Function: polarform (expr)

Retorna uma expressão `r %e^(%i theta)` equivalente a *expr*,
tal que `r` e `theta` sejam puramente reais.

<!-- category: Other -->
<!-- keywords: powers -->
<!-- signatures: powers(expr, x) -->
### Function: powers (expr, x)

Fornece os expoentes de *x* que ocorrem em expressão *expr*.


`load ("powers")` chama essa função.

<!-- category: Other -->
<!-- keywords: product -->
<!-- signatures: product(expr, i, i_0, i_1) -->
### Function: product (expr, i, i_0, i_1)

Representa um produto dos velores de `expr` com
o índice *i* variando de *i_0* a *i_1*.
A forma substantiva `'product` é mostrada como um pi maiísculo.


`product` avalia *expr* e os limites inferior e superior *i_0* e *i_1*,
`product` coloca um apóstrofo (não avalia) o índice *i*.


Se os limites superiores e inferiores diferirem por um inteiro,
*expr* é avaliada para cada valor do índice *i*,
e o resultado  um produto explícito.


de outra forma, o intervalo do índice é indefinido.
Algumas regras são aplicads para simplificar o produto.
Quando a variável global `simpproduct` for `true`, regras adicionais são aplicadas.
Em alguns casos, simplificação um resultado que não é um produto;
de outra forma, o resultado é uma forma substantiva `'product`.


Veja também `nouns` e `evflag`.


Exemplos:















```maxima
(%i1) product (x + i*(i+1)/2, i, 1, 4);
(%o1)           (x + 1) (x + 3) (x + 6) (x + 10)
(%i2) product (i^2, i, 1, 7);
(%o2)                       25401600
(%i3) product (a[i], i, 1, 7);
(%o3)                 a  a  a  a  a  a  a
                       1  2  3  4  5  6  7
(%i4) product (a(i), i, 1, 7);
(%o4)          a(1) a(2) a(3) a(4) a(5) a(6) a(7)
(%i5) product (a(i), i, 1, n);
                             n
                           /===\
                            ! !
(%o5)                       ! !  a(i)
                            ! !
                           i = 1
(%i6) product (k, k, 1, n);
                               n
                             /===\
                              ! !
(%o6)                         ! !  k
                              ! !
                             k = 1
(%i7) product (k, k, 1, n), simpproduct;
(%o7)                          n!
(%i8) product (integrate (x^k, x, 0, 1), k, 1, n);
                             n
                           /===\
                            ! !    1
(%o8)                       ! !  -----
                            ! !  k + 1
                           k = 1
(%i9) product (if k <= 5 then a^k else b^k, k, 1, 10);
                              15  40
(%o9)                        a   b
```

<!-- category: Other -->
<!-- keywords: realpart -->
<!-- signatures: realpart(expr) -->
### Function: realpart (expr)

Retorna a parte real de *expr*. `realpart` e `imagpart` irão
trabalhar sobre expressões envolvendo funções trigonométricas e hiperbólicas,
bem como raízes quadradas, logarítmos, e exponenciação.

<!-- category: Other -->
<!-- keywords: rectform -->
<!-- signatures: rectform(expr) -->
### Function: rectform (expr)

Retorna uma expressão `a + b %i` equivalente a *expr*,
tal que *a* e *b* sejam puramente reais.

<!-- category: Other -->
<!-- keywords: rembox -->
<!-- signatures: rembox(expr, unlabelled), rembox(expr, rótulo), rembox(expr) -->
### Function: rembox (expr, unlabelled)

Remove caixas de *expr*.


`rembox (expr, unlabelled)` remove todas as caixas sem rótulos de *expr*.


`rembox (expr, rótulo)` remove somente caixas contendo *rótulo*.


`rembox (expr)` remove todas as caixas, rotuladas e nã rotuladas.


Caixas são desenhadas pelas funções `box`, `dpart`, e `lpart`.


Exemplos:












```maxima
(%i1) expr: (a*d - b*c)/h^2 + sin(%pi*x);
                                  a d - b c
(%o1)                sin(%pi x) + ---------
                                      2
                                     h
(%i2) dpart (dpart (expr, 1, 1), 2, 2);
                        """""""    a d - b c
(%o2)               sin("%pi x") + ---------
                        """""""      """"
                                     " 2"
                                     "h "
                                     """"
(%i3) expr2: lpart (BAR, lpart (FOO, %, 1), 2);
                  FOO"""""""""""   BAR""""""""
                  "    """"""" "   "a d - b c"
(%o3)             "sin("%pi x")" + "---------"
                  "    """"""" "   "  """"   "
                  """"""""""""""   "  " 2"   "
                                   "  "h "   "
                                   "  """"   "
                                   """""""""""
(%i4) rembox (expr2, unlabelled);
                                  BAR""""""""
                   FOO"""""""""   "a d - b c"
(%o4)              "sin(%pi x)" + "---------"
                   """"""""""""   "    2    "
                                  "   h     "
                                  """""""""""
(%i5) rembox (expr2, FOO);
                                  BAR""""""""
                       """""""    "a d - b c"
(%o5)              sin("%pi x") + "---------"
                       """""""    "  """"   "
                                  "  " 2"   "
                                  "  "h "   "
                                  "  """"   "
                                  """""""""""
(%i6) rembox (expr2, BAR);
                   FOO"""""""""""
                   "    """"""" "   a d - b c
(%o6)              "sin("%pi x")" + ---------
                   "    """"""" "     """"
                   """"""""""""""     " 2"
                                      "h "
                                      """"
(%i7) rembox (expr2);
                                  a d - b c
(%o7)                sin(%pi x) + ---------
                                      2
                                     h
```

<!-- category: Other -->
<!-- keywords: sum -->
<!-- signatures: sum(expr, i, i_0, i_1) -->
### Function: sum (expr, i, i_0, i_1)

Representa um somatório dos valores de *expr* com
o índice *i* variando de *i_0* a *i_1*.
A forma substantiva `'sum` é mostrada com uma letra sigma maiúscula.
`sum` avalia seu somando *expr* e limites inferior e superior *i_0* e *i_1*,
`sum` coloca apóstrofo (não avalia) o índice *i*.


Se os limites superiores e inferiores diferirem de um número inteiro,
o somatoriando *expr* é avaliado para cada valor do índice do somatório *i*,
e o resultado é uma adição explícita.


De outra forma, o intervalo dos índices é indefinido.
Algumas regras são aplicadas para simplificar o somatório.
Quando a variável global `simpsum` for `true`, regras adicionais são aplicadas.
Em alguns casos, simplificações retornam um resultado que não é um somatório;
de outra forma, o resultado é uma forma substantiva `'sum`.


Quando o `evflag` (sinalizador de avaliação) `cauchysum` for `true`,
um produto de somatórios é mostrado como um produto de Cauchy,
no qual o índice do somatório mais interno é uma função de
índice de um nível acima, em lugar de variar independentemente.


A variável global `genindex` é o prefixo alfabético usado para gerar o próximo índice do somatório,
quando um índice automaticamente gerado for necessário.


`gensumnum` é o sufixo numérico usando para gerar o próximo índice do somatório,
quando um índice gerado automaticamente for necessário.
Quando `gensumnum` for `false`, um índice gerado automaticamente é somente
`genindex` sem sufixo numérico.


Veja também `sumcontract`, `intosum`,
`bashindices`, `niceindices`,
`nouns`, `evflag`, e `zeilberger`.


Exemplos:


















```maxima
(%i1) sum (i^2, i, 1, 7);
(%o1)                          140
(%i2) sum (a[i], i, 1, 7);
(%o2)           a  + a  + a  + a  + a  + a  + a
                 7    6    5    4    3    2    1
(%i3) sum (a(i), i, 1, 7);
(%o3)    a(7) + a(6) + a(5) + a(4) + a(3) + a(2) + a(1)
(%i4) sum (a(i), i, 1, n);
                            n
                           ====
                           \
(%o4)                       >    a(i)
                           /
                           ====
                           i = 1
(%i5) sum (2^i + i^2, i, 0, n);
                          n
                         ====
                         \       i    2
(%o5)                     >    (2  + i )
                         /
                         ====
                         i = 0
(%i6) sum (2^i + i^2, i, 0, n), simpsum;
                              3      2
                   n + 1   2 n  + 3 n  + n
(%o6)             2      + --------------- - 1
                                  6
(%i7) sum (1/3^i, i, 1, inf);
                            inf
                            ====
                            \     1
(%o7)                        >    --
                            /      i
                            ====  3
                            i = 1
(%i8) sum (1/3^i, i, 1, inf), simpsum;
                                1
(%o8)                           -
                                2
(%i9) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf);
                              inf
                              ====
                              \     1
(%o9)                      30  >    --
                              /      2
                              ====  i
                              i = 1
(%i10) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf), simpsum;
                                  2
(%o10)                       5 %pi
(%i11) sum (integrate (x^k, x, 0, 1), k, 1, n);
                            n
                           ====
                           \       1
(%o11)                      >    -----
                           /     k + 1
                           ====
                           k = 1
(%i12) sum (if k <= 5 then a^k else b^k, k, 1, 10));
Incorrect syntax: Too many )'s
else b^k, k, 1, 10))
                  ^
(%i12) linenum:11;
(%o11)                         11
(%i12) sum (integrate (x^k, x, 0, 1), k, 1, n);
                            n
                           ====
                           \       1
(%o12)                      >    -----
                           /     k + 1
                           ====
                           k = 1
(%i13) sum (if k <= 5 then a^k else b^k, k, 1, 10);
          10    9    8    7    6    5    4    3    2
(%o13)   b   + b  + b  + b  + b  + a  + a  + a  + a  + a
```

<!-- category: Other -->
<!-- keywords: verbify -->
<!-- signatures: verbify(f) -->
### Function: verbify (f)

Retorna a forma verbal da função chamada *f*.


Veja também `verb`, `noun`, e `nounify`.


Exemplos:









```maxima
(%i1) verbify ('foo);
(%o1)                          foo
(%i2) :lisp $%
$FOO
(%i2) nounify (foo);
(%o2)                          foo
(%i3) :lisp $%
%FOO
```

