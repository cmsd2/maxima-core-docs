## Teoria dos Números

<!-- category: Other -->
<!-- keywords: %gamma -->
<!-- signatures: %gamma -->
### Variable: %gamma

A constante de Euler-Mascheroni, 0.5772156649015329 ....

<!-- category: Other -->
<!-- keywords: bern -->
<!-- signatures: bern(n) -->
### Function: bern (n)

Retorna o *n*’ésimo número de Bernoulli para o inteiro *n*.


Números de Bernoulli iguais a zero são suprimidos se `zerobern` for `false`.


Veja também `burn`.



```maxima
(%i1) zerobern: true$
(%i2) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                  1  1       1      1        1
(%o2)       [1, - -, -, 0, - --, 0, --, 0, - --]
                  2  6       30     42       30
(%i3) zerobern: false$
(%i4) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
            1  1    1   5     691   7    3617  43867
(%o4) [1, - -, -, - --, --, - ----, -, - ----, -----]
            2  6    30  66    2730  6    510    798
```

<!-- category: Other -->
<!-- keywords: bernpoly -->
<!-- signatures: bernpoly(x, n) -->
### Function: bernpoly (x, n)

Retorna o *n*’ésimo polinómio de Bernoulli na
variável *x*.

<!-- category: Other -->
<!-- keywords: bfhzeta -->
<!-- signatures: bfhzeta(s, h, n) -->
### Function: bfhzeta (s, h, n)

Retorna a função zeta de Hurwitz para os argumentos *s* e *h*.
O valor de retorno é um grande inteiro em ponto flutuante (bfloat);
*n* é o números de dígitos no valor de retorno.


A função zeta de Hurwitz é definida como



```maxima
sum ((k+h)^-s, k, 0, inf)
```


`load ("bffac")` chama essa função.

<!-- category: Other -->
<!-- keywords: bfzeta -->
<!-- signatures: bfzeta(s, n) -->
### Function: bfzeta (s, n)

Retorna a função zeta de Riemann para o argumento *s*.
O valor de retorno é um grande inteiro em ponto flutuante (bfloat);
*n* é o número de dígitos no valor de retorno.


`load ("bffac")` chama essa função.

<!-- category: Other -->
<!-- keywords: binomial -->
<!-- signatures: binomial(x, y) -->
### Function: binomial (x, y)

O coeficiente binomial `x!/(y! (x - y)!)`.
Se *x* e *y* forem inteiros, então o valor numérico do coeficiente
binomial é calculado.
Se *y*, ou *x - y*, for um inteiro,
o the coeficiente binomial é expresso como um polinómio.


Exemplos:










```maxima
(%i1) binomial (11, 7);
(%o1)                          330
(%i2) 11! / 7! / (11 - 7)!;
(%o2)                          330
(%i3) binomial (x, 7);
        (x - 6) (x - 5) (x - 4) (x - 3) (x - 2) (x - 1) x
(%o3)   -------------------------------------------------
                              5040
(%i4) binomial (x + 7, x);
      (x + 1) (x + 2) (x + 3) (x + 4) (x + 5) (x + 6) (x + 7)
(%o4) -------------------------------------------------------
                               5040
(%i5) binomial (11, y);
(%o5)                    binomial(11, y)
```

<!-- category: Other -->
<!-- keywords: burn -->
<!-- signatures: burn(n) -->
### Function: burn (n)

Retorna o *n*’ésimo número de Bernoulli para o inteiro *n*.
`burn` pode ser mais eficitente que `bern` para valores grandes e isolados de *n*
(talvez *n* maior que 105 ou algo parecido), 
como `bern` calcula todos os números de Bernoulli até o índice *n* antes de retornar.












`burn` explora a observação que números de Bernoulli (racionais) podem ser
aproximados através de zetas (transcendentes) com eficiência tolerável.


`load ("bffac")` chama essa função.

<!-- category: Other -->
<!-- keywords: cf -->
<!-- signatures: cf(expr) -->
### Function: cf (expr)

Converte *expr* em uma fração contínua.
*expr* é uma expressão
compreendendo frações contínuas e raízes quadradas de inteiros.
Operandos na expressão podem ser combinados com operadores aritméticos.
Com excessão de frações contínuas e raízes quadradas,
factores na expressão devem ser números inteiros ou racionais.
Maxima não conhece operações sobre frações contínuas fora de `cf`.


`cf` avalia seus argumentos após associar `listarith` a `false`.
`cf` retorna uma fração contínua, representada como uma lista.


Uma fração contínua `a + 1/(b + 1/(c + ...))`
é representada através da lista `[a, b, c, ...]`.
Os elementos da lista `a`, `b`, `c`, ... devem avaliar para inteiros. 
*expr* pode também conter `sqrt (n)` onde `n` é um inteiro.
Nesse caso `cf` fornecerá tantos
termos de fração contínua quantos forem o valor da variável
`cflength` vezes o período.


Uma fração contínua pode ser avaliada para um número
através de avaliação da representação aritmética
retornada por `cfdisrep`.
Veja também `cfexpand` para outro caminho para avaliar uma fração contínua.


Veja também `cfdisrep`, `cfexpand`, e `cflength`.


Exemplos:



- *
*expr* é uma expressão compreendendo frações contínuas e raízes quadradas de inteiros.

```maxima
(%i1) cf ([5, 3, 1]*[11, 9, 7] + [3, 7]/[4, 3, 2]);
(%o1)               [59, 17, 2, 1, 1, 1, 27]
(%i2) cf ((3/17)*[1, -2, 5]/sqrt(11) + (8/13));
(%o2)        [0, 1, 1, 1, 3, 2, 1, 4, 1, 9, 1, 9, 2]
```
- *
`cflength` controla quantos períodos de fração contínua
são computados para números algébricos, números irracionais.

```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```
- *
Um fração contínua pode ser avaliado através da avaliação da representação aritmética
retornada por `cfdisrep`.

```maxima
(%i1) cflength: 3$
(%i2) cfdisrep (cf (sqrt (3)))$
(%i3) ev (%, numer);
(%o3)                   1.731707317073171
```
- *
Maxima não conhece operações sobre frações contínuas fora de `cf`.

```maxima
(%i1) cf ([1,1,1,1,1,2] * 3);
(%o1)                     [4, 1, 5, 2]
(%i2) cf ([1,1,1,1,1,2]) * 3;
(%o2)                  [3, 3, 3, 3, 3, 6]
```

<!-- category: Other -->
<!-- keywords: cfdisrep -->
<!-- signatures: cfdisrep(list) -->
### Function: cfdisrep (list)

Constrói e retorna uma expressão aritmética comum
da forma `a + 1/(b + 1/(c + ...))`
a partir da representação lista de uma fração contínua `[a, b, c, ...]`.



```maxima
(%i1) cf ([1, 2, -3] + [1, -2, 1]);
(%o1)                     [1, 1, 1, 2]
(%i2) cfdisrep (%);
                                  1
(%o2)                     1 + ---------
                                    1
                              1 + -----
                                      1
                                  1 + -
                                      2
```

<!-- category: Other -->
<!-- keywords: cfexpand -->
<!-- signatures: cfexpand(x) -->
### Function: cfexpand (x)

Retorna uma matriz de numeradores e denominadores dos
último (columa 1) e penúltimo (columa 2) convergentes da fração contínua *x*.



```maxima
(%i1) cf (rat (ev (%pi, numer)));

`rat' replaced 3.141592653589793 by 103993/33102 = 3.141592653011902
(%o1)                  [3, 7, 15, 1, 292]
(%i2) cfexpand (%); 
                         [ 103993  355 ]
(%o2)                    [             ]
                         [ 33102   113 ]
(%i3) %[1,1]/%[2,1], numer;
(%o3)                   3.141592653011902
```

<!-- category: Other -->
<!-- keywords: cflength -->
<!-- signatures: cflength -->
### Variable: cflength

Valor por omissão: 1


`cflength` controla o número de termos da fração
contínua que a função `cf` fornecerá, como o valor de `cflength` vezes o
período.  Dessa forma o padrão é fornecer um período.



```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```

<!-- category: Other -->
<!-- keywords: divsum -->
<!-- signatures: divsum(n, k), divsum(n) -->
### Function: divsum (n, k)

`divsum (n, k)` retorna a adição dos divisores de *n*
elevados à *k*’ésima potência.


`divsum (n)` retorna a adição dos divisores de *n*.



```maxima
(%i1) divsum (12);
(%o1)                          28
(%i2) 1 + 2 + 3 + 4 + 6 + 12;
(%o2)                          28
(%i3) divsum (12, 2);
(%o3)                          210
(%i4) 1^2 + 2^2 + 3^2 + 4^2 + 6^2 + 12^2;
(%o4)                          210
```

<!-- category: Other -->
<!-- keywords: euler -->
<!-- signatures: euler(n) -->
### Function: euler (n)

Retorna o *n*’ésimo número de Euler para o inteiro *n* não negativo.


Para a constante de Euler-Mascheroni, veja `%gamma`.



```maxima
(%i1) map (euler, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1)    [1, 0, - 1, 0, 5, 0, - 61, 0, 1385, 0, - 50521]
```

<!-- category: Other -->
<!-- keywords: factorial -->
<!-- signatures: factorial(x) -->
### Function: factorial (x)

Representa a função factorial. Maxima trata `factorial (x)` da mesma forma que `x!`.
Veja `!`.

<!-- category: Other -->
<!-- keywords: fib -->
<!-- signatures: fib(n) -->
### Function: fib (n)

Retorna o *n*’ésimo número de Fibonacci.
`fib(0)` igual a 0 e `fib(1)` igual a 1,
e
`fib (-n)` igual a `(-1)^(n + 1) * fib(n)`.


Após chamar `fib`,
`prevfib` é iguala `fib (x - 1)`,
o número de Fibonacci anterior ao último calculado.



```maxima
(%i1) map (fib, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1)         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

<!-- category: Other -->
<!-- keywords: fibtophi -->
<!-- signatures: fibtophi(expr) -->
### Function: fibtophi (expr)

Expressa números de Fibonacci que aparecem em *expr* em termos da constante `%phi`,
que é `(1 + sqrt(5))/2`, aproximadamente 1.61803399.


Exemplos:

 








```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1
(%i4) ratsimp (%);
(%o4)                           0
```

<!-- category: Other -->
<!-- keywords: ifactors -->
<!-- signatures: ifactors(n) -->
### Function: ifactors (n)

Para um inteiro positivo *n* retorna a factoração de *n*. Se
`n=p1^e1..pk^nk` for a decomposição de *n* em factores
primos, `ifactors` retorna `[[p1, e1], ... , [pk, ek]]`.


Os métodos de factoração usados são divisões triviais por primos até 9973,
o método rho de Pollard e o método da curva elíptica.



```maxima
(%i1) ifactors(51575319651600);
(%o1)     [[2, 4], [3, 2], [5, 2], [1583, 1], [9050207, 1]]
(%i2) apply("*", map(lambda([u], u[1]^u[2]), %));
(%o2)                        51575319651600
```

<!-- category: Other -->
<!-- keywords: inrt -->
<!-- signatures: inrt(x, n) -->
### Function: inrt (x, n)

Retorna a parte inteira da *n*’ésima raíz do valor absoluto de *x*.



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], inrt (10^a, 3)), l);
(%o2) [2, 4, 10, 21, 46, 100, 215, 464, 1000, 2154, 4641, 10000]
```

<!-- category: Other -->
<!-- keywords: inv_mod -->
<!-- signatures: inv_mod(n, m) -->
### Function: inv_mod (n, m)

Calcula o  inverso de *n* módulo *m*. 
`inv_mod (n,m)` retorna `false`, 
se *n* modulo *m* for zero.



```maxima
(%i1) inv_mod(3, 41);
(%o1)                           14
(%i2) ratsimp(3^-1), modulus=41;
(%o2)                           14
(%i3) inv_mod(3, 42);
(%o3)                          false
```

<!-- category: Other -->
<!-- keywords: jacobi -->
<!-- signatures: jacobi(p, q) -->
### Function: jacobi (p, q)

Retorna símbolo de Jacobi de *p* e *q*.



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], jacobi (a, 9)), l);
(%o2)         [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
```

<!-- category: Other -->
<!-- keywords: lcm -->
<!-- signatures: lcm(expr_1, ..., expr_n) -->
### Function: lcm (expr_1, ..., expr_n)

Retorna o menor múltiplo comum entre seus argumentos.
Os argumentos podem ser expressões gerais também inteiras.


`load ("functs")` chama essa função.

<!-- category: Other -->
<!-- keywords: minfactorial -->
<!-- signatures: minfactorial(expr) -->
### Function: minfactorial (expr)

Examina *expr* procurando por ocorrências de dois factoriais
que diferem por um inteiro.  
`minfactorial` então converte um em um polinómio vezes o outro.









```maxima
(%i1) n!/(n+2)!;
                               n!
(%o1)                       --------
                            (n + 2)!
(%i2) minfactorial (%);
                                1
(%o2)                    ---------------
                         (n + 1) (n + 2)
```

<!-- category: Other -->
<!-- keywords: next_prime -->
<!-- signatures: next_prime(n) -->
### Function: next_prime (n)

Retorna o menor primo maior que *n*.



```maxima
(%i1) next_prime(27);
(%o1)                       29
```

<!-- category: Other -->
<!-- keywords: partfrac -->
<!-- signatures: partfrac(expr, var) -->
### Function: partfrac (expr, var)

Expande a expressão *expr* em frações parciais
com relação à variável principal *var*.  `partfrac` faz uma decomposição
completa de fração parcial.  O algoritmo utilizado é baseado no
facto que os denominadores de uma expansão de fração parcial (os
factores do denominador original) são relativamente primos.  Os
numeradores podem ser escritos como combinação linear dos denominadores, e
a expansão acontece.



```maxima
(%i1) 1/(1+x)^2 - 2/(1+x) + 2/(2+x);
                      2       2        1
(%o1)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
(%i2) ratsimp (%);
                                 x
(%o2)                 - -------------------
                         3      2
                        x  + 4 x  + 5 x + 2
(%i3) partfrac (%, x);
                      2       2        1
(%o3)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
```

<!-- category: Other -->
<!-- keywords: power_mod -->
<!-- signatures: power_mod(a, n, m) -->
### Function: power_mod (a, n, m)

Usa um algoritmo modular para calcular `a^n mod m` 
onde *a* e *n* são inteiros e *m* é um inteiro positivo. 
Se *n* for negativo, `inv_mod` é usada para encontrar o inverso modular.



```maxima
(%i1) power_mod(3, 15, 5);
(%o1)                          2
(%i2) mod(3^15,5);
(%o2)                          2
(%i3) power_mod(2, -1, 5);
(%o3)                          3
(%i4) inv_mod(2,5);
(%o4)                          3
```

<!-- category: Other -->
<!-- keywords: prev_prime -->
<!-- signatures: prev_prime(n) -->
### Function: prev_prime (n)

Retorna o maior primo menor que *n*.



```maxima
(%i1) prev_prime(27);
(%o1)                       23
```

<!-- category: Other -->
<!-- keywords: primep -->
<!-- signatures: primep(n) -->
### Function: primep (n)

Teste de primalidade. Se `primep (n)` retornar `false`, *n* é um
número compostro e se esse teste retornar `true`, *n* é um número primo
com grande probabilidade.


Para *n* menor que 3317044064679887385961981 uma versão deterministra do teste de 
Miller-Rabin é usada. Se `primep (n)` retornar `true`, então *n* é um
número primo.


Para *n* maior que 34155071728321 `primep` usa
`primep_number_of_tests` que é os testes de pseudo-primalidade de Miller-Rabin
e um teste de pseudo-primalidade de Lucas. A probabilidade que *n* irá
passar por um teste de Miller-Rabin é menor que 1/4. Usando o valor padrão 25 para
`primep_number_of_tests`, a probabilidade de *n* passar no teste sendo
composto é muito menor que 10^-15.

<!-- category: Other -->
<!-- keywords: primep_number_of_tests -->
<!-- signatures: primep_number_of_tests -->
### Variable: primep_number_of_tests

Valor por omissão: 25


Número de testes de Miller-Rabin usados em `primep`.

<!-- category: Other -->
<!-- keywords: qunit -->
<!-- signatures: qunit(n) -->
### Function: qunit (n)

Retorna a principal unidade do campo dos números quadráticos reais
`sqrt (n)` onde *n* é um inteiro,
i.e., o elemento cuja norma é unidade.
Isso é importante para resolver a equação de Pell `a^2 - n b^2 = 1`.



```maxima
(%i1) qunit (17);
(%o1)                     sqrt(17) + 4
(%i2) expand (% * (sqrt(17) - 4));
(%o2)                           1
```

<!-- category: Other -->
<!-- keywords: totient -->
<!-- signatures: totient(n) -->
### Function: totient (n)

Retorna o número de inteiros menores que ou iguais a *n* que
são relativamente primos com *n*.

<!-- category: Other -->
<!-- keywords: zerobern -->
<!-- signatures: zerobern -->
### Variable: zerobern

Valor por omissão: `true`


Quando `zerobern` for `false`,
`bern` exclui os números de Bernoulli que forem iguais a zero. 
Veja `bern`.

<!-- category: Other -->
<!-- keywords: zeta -->
<!-- signatures: zeta(n) -->
### Function: zeta (n)

Retorna a função zeta de Riemann se *x* for um inteiro negativo, 0, 1,
ou número par positivo,
e retorna uma forma substantiva `zeta (n)` para todos os outros argumentos,
incluindo não inteiros racionais, ponto flutuante, e argumentos complexos.


Veja também `bfzeta` e `zeta%pi`.



```maxima
(%i1) map (zeta, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]);
                                     2              4
           1        1     1       %pi            %pi
(%o1) [0, ---, 0, - --, - -, inf, ----, zeta(3), ----, zeta(5)]
          120       12    2        6              90
```

<!-- category: Other -->
<!-- keywords: zeta%pi -->
<!-- signatures: zeta%pi -->
### Variable: zeta%pi

Valor por omissão: `true`


Quando `zeta%pi` for `true`, `zeta` retorna uma expressão
proporcional a `%pi^n` para inteiro par `n`.
De outra forma, `zeta` retorna uma forma substantiva `zeta (n)`
para inteiro par `n`.



```maxima
(%i1) zeta%pi: true$
(%i2) zeta (4);
                                 4
                              %pi
(%o2)                         ----
                               90
(%i3) zeta%pi: false$
(%i4) zeta (4);
(%o4)                        zeta(4)
```

