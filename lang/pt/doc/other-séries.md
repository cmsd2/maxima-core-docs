## Séries

<!-- category: Other -->
<!-- keywords: cauchysum -->
<!-- signatures: cauchysum -->
### Variable: cauchysum

Valor por omissão: `false`



Quando multiplicando adições jutas com `inf` como seus limites superiores,
se `sumexpand` for `true` e `cauchysum` for `true`
então o produto de Cauchy será usado em lugar do produto
usual.
No produto de Cauchy o índice do somatório interno é uma
função do índice do externo em lugar de variar
independentemente.


Exemplo:



```maxima
(%i1) sumexpand: false$
(%i2) cauchysum: false$
(%i3) s: sum (f(i), i, 0, inf) * sum (g(j), j, 0, inf);
                      inf         inf
                      ====        ====
                      \           \
(%o3)                ( >    f(i))  >    g(j)
                      /           /
                      ====        ====
                      i = 0       j = 0
(%i4) sumexpand: true$
(%i5) cauchysum: true$
(%i6) ''s;
                 inf     i1
                 ====   ====
                 \      \
(%o6)             >      >     g(i1 - i2) f(i2)
                 /      /
                 ====   ====
                 i1 = 0 i2 = 0
```

<!-- category: Other -->
<!-- keywords: deftaylor -->
<!-- signatures: deftaylor(f_1(x_1), expr_1, ..., f_n(x_n), expr_n) -->
### Function: deftaylor (f_1(x_1), expr_1, ..., f_n(x_n), expr_n)

Para cada função *f_i* de uma variável *x_i*, 
`deftaylor` define *expr_i* como a séries de Taylor sobre zero.
*expr_i* é tipicamente um polinómio em *x_i* ou um somatório;
expressões mais gerais são aceitas por `deftaylor` sem reclamações.


`powerseries (f_i(x_i), x_i, 0)`
retorna as séries definidas por `deftaylor`.


`deftaylor` retorna uma lista das funções
*f_1*, ..., *f_n*.
`deftaylor` avalia seus argumentos.


Exemplo:



```maxima
(%i1) deftaylor (f(x), x^2 + sum(x^i/(2^i*i!^2), i, 4, inf));
(%o1)                          [f]
(%i2) powerseries (f(x), x, 0);
                      inf
                      ====      i1
                      \        x         2
(%o2)                  >     -------- + x
                      /       i1    2
                      ====   2   i1!
                      i1 = 4
(%i3) taylor (exp (sqrt (f(x))), x, 0, 4);
                      2         3          4
                     x    3073 x    12817 x
(%o3)/T/     1 + x + -- + ------- + -------- + . . .
                     2     18432     307200
```

<!-- category: Other -->
<!-- keywords: maxtayorder -->
<!-- signatures: maxtayorder -->
### Variable: maxtayorder

Valor por omissão: `true`



Quando `maxtayorder` for `true`, durante a manipulação
algébrica de séries (truncadas) de Taylor, `taylor` tenta reter
tantos termos quantos forem conhecidos serem correctos.

<!-- category: Other -->
<!-- keywords: niceindices -->
<!-- signatures: niceindices(expr) -->
### Function: niceindices (expr)

Renomeia os índices de adições e produtos em *expr*.
`niceindices` tenta renomear cada índice para o valor de `niceindicespref[1]`,
a menos que o nome apareça nas parcelas do somatório ou produtório,
nesses casos `niceindices` tenta
os elementos seguintes de `niceindicespref` por sua vez, até que uma varável não usada unused variable seja encontrada.
Se a lista inteira for exaurida,
índices adicionais são constrídos através da anexaao de inteiros ao valor de
`niceindicespref[1]`, e.g., `i0`, `i1`, `i2`, ....


`niceindices` retorna uma expressão.
`niceindices` avalia seu argumento.


Exemplo:



```maxima
(%i1) niceindicespref;
(%o1)                  [i, j, k, l, m, n]
(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o2)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1
(%i3) niceindices (%);
                     inf  inf
                    /===\ ====
                     ! !  \
(%o3)                ! !   >    f(i j l + k)
                     ! !  /
                    l = 1 ====
                          k = 1
```

<!-- category: Other -->
<!-- keywords: niceindicespref -->
<!-- signatures: niceindicespref -->
### Variable: niceindicespref

Valor por omissão: `[i, j, k, l, m, n]`


`niceindicespref` é a lista da qual `niceindices`
obtém os nomes dos índices de adições e produtos products.


Os elementos de `niceindicespref` são tipicamente nomes de variáveis,
embora que não seja imposto por `niceindices`.


Exemplo:



```maxima
(%i1) niceindicespref: [p, q, r, s, t, u]$
(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o2)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1
(%i3) niceindices (%);
                     inf  inf
                    /===\ ====
                     ! !  \
(%o3)                ! !   >    f(i j q + p)
                     ! !  /
                    q = 1 ====
                          p = 1
```

<!-- category: Other -->
<!-- keywords: nusum -->
<!-- signatures: nusum(expr, x, i_0, i_1) -->
### Function: nusum (expr, x, i_0, i_1)

Realiza o somatório hipergeométrico indefinido de *expr* com
relação a *x* usando um procedimento de decisão devido a R.W. Gosper.
*expr* e o resultado deve ser expressável como produtos de expoentes inteiros,
factoriais, binomios, e funções recionais.




Os termos "definido"
and "e somatório indefinido" são usados analogamente a "definida" and
"integração indefinida".
Adicionar indefinidamente significa dar um resultado simólico
para a adição sobre intervalos de comprimentos de variáveis, não apenas e.g. 0 a
infinito.  Dessa forma, uma vez que não existe fórmula para a adição parcial geral de
séries binomiais, `nusum` não pode fazer isso.


`nusum` e `unsum` conhecem um porco sobre adições e subtrações de produtos finitos.
Veja também `unsum`.


Exemplos:



```maxima
(%i1) nusum (n*n!, n, 0, n);

Dependent equations eliminated:  (1)
(%o1)                     (n + 1)! - 1
(%i2) nusum (n^4*4^n/binomial(2*n,n), n, 0, n);
                     4        3       2              n
      2 (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3) 4      2
(%o2) ------------------------------------------------ - ------
                    693 binomial(2 n, n)                 3 11 7
(%i3) unsum (%, n);
                              4  n
                             n  4
(%o3)                   ----------------
                        binomial(2 n, n)
(%i4) unsum (prod (i^2, i, 1, n), n);
                    n - 1
                    /===\
                     ! !   2
(%o4)              ( ! !  i ) (n - 1) (n + 1)
                     ! !
                    i = 1
(%i5) nusum (%, n, 1, n);

Dependent equations eliminated:  (2 3)
                            n
                          /===\
                           ! !   2
(%o5)                      ! !  i  - 1
                           ! !
                          i = 1
```

<!-- category: Other -->
<!-- keywords: pade -->
<!-- signatures: pade(taylor_series, numer_deg_bound, denom_deg_bound) -->
### Function: pade (taylor_series, numer_deg_bound, denom_deg_bound)

Retorna uma lista de
todas as funções racionais que possuem a dada expansão da séries de Taylor
onde a adição dos graus do numerador e do denominador é
menor que ou igual ao nível de truncação das séries de potência, i.e.
são "melhores" aproximações, e que adicionalmente satisfazem o grau
especificado associado.


*taylor_series* é uma séries de Taylor de uma variável.
*numer_deg_bound* e *denom_deg_bound*
são inteiros positivos especificando o grau associado sobre
o numerador e o denominador.


*taylor_series* podem também ser séries de Laurent, e o grau
associado pode ser `inf` que acarreta todas funções racionais cujo grau
total for menor que ou igual ao comprimento das séries de potências a serem
retornadas.  O grau total é definido como `numer_deg_bound + denom_deg_bound`.
O comprimento de séries de potência é definido como
`"nível de trncação" + 1 - min(0, "ordem das séries")`.



```maxima
(%i1) taylor (1 + x + x^2 + x^3, x, 0, 3);
                              2    3
(%o1)/T/             1 + x + x  + x  + . . .
(%i2) pade (%, 1, 1);
                                 1
(%o2)                       [- -----]
                               x - 1
(%i3) t: taylor(-(83787*x^10 - 45552*x^9 - 187296*x^8
                   + 387072*x^7 + 86016*x^6 - 1507328*x^5
                   + 1966080*x^4 + 4194304*x^3 - 25165824*x^2
                   + 67108864*x - 134217728)
       /134217728, x, 0, 10);
                    2    3       4       5       6        7
             x   3 x    x    15 x    23 x    21 x    189 x
(%o3)/T/ 1 - - + ---- - -- - ----- + ----- - ----- - ------
             2    16    32   1024    2048    32768   65536

                                  8         9          10
                            5853 x    2847 x    83787 x
                          + ------- + ------- - --------- + . . .
                            4194304   8388608   134217728
(%i4) pade (t, 4, 4);
(%o4)                          []
```


Não existe função racional de grau 4 numerador/denominador, com essa
expansão de série de potência.  Você obrigatoriamente em geral tem grau do numerador e
grau do denominador adicionando para cima ao menor grau das séries de potência,
com o objectivo de ter disponível coeficientes desconhecidos para resolver.



```maxima
(%i5) pade (t, 5, 5);
                     5                4                 3
(%o5) [- (520256329 x  - 96719020632 x  - 489651410240 x

                  2
 - 1619100813312 x  - 2176885157888 x - 2386516803584)

               5                 4                  3
/(47041365435 x  + 381702613848 x  + 1360678489152 x

                  2
 + 2856700692480 x  + 3370143559680 x + 2386516803584)]
```

<!-- category: Other -->
<!-- keywords: powerdisp -->
<!-- signatures: powerdisp -->
### Variable: powerdisp

Valor por omissão: `false`


Quando `powerdisp` for `true`,
uma adição é mostrada com seus termos em ordem do crescimento do expoente.
Dessa forma um polinómio é mostrado como séries de potências truncadas,
com o termo constante primeiro e o maior expoente por último.


Por padão, termos de uma adição são mostrados em ordem do expoente decrescente.

<!-- category: Other -->
<!-- keywords: powerseries -->
<!-- signatures: powerseries(expr, x, a) -->
### Function: powerseries (expr, x, a)

Retorna a forma geral expansão de séries de potência para *expr*
na variável *x* sobre o ponto *a* (o qual pode ser `inf` para infinito).


Se `powerseries` incapaz de expandir *expr*,
`taylor` pode dar os primeiros muitos termos de séries.


Quando `verbose` for `true`,
`powerseries` mostra mensagens de progresso. 



```maxima
(%i1) verbose: true$
(%i2) powerseries (log(sin(x)/x), x, 0);
can't expand 
                                 log(sin(x))
so we'll try again after applying the rule:
                                        d
                                      / -- (sin(x))
                                      [ dx
                        log(sin(x)) = i ----------- dx
                                      ]   sin(x)
                                      /
in the first simplification we have returned:
                             /
                             [
                             i cot(x) dx - log(x)
                             ]
                             /
                    inf
                    ====        i1  2 i1             2 i1
                    \      (- 1)   2     bern(2 i1) x
                     >     ------------------------------
                    /                i1 (2 i1)!
                    ====
                    i1 = 1
(%o2)                -------------------------------------
                                      2
```

<!-- category: Other -->
<!-- keywords: psexpand -->
<!-- signatures: psexpand -->
### Variable: psexpand

Valor por omissão: `false`


Quando `psexpand` for `true`,
uma expressão função racional extendida é mostrada completamente expandida.
O comutador `ratexpand` tem o mesmo efeito.



Quando `psexpand` for `false`,
uma expressão de várias variáveis é mostrada apenas como no pacote de função racional.



Quando `psexpand` for  `multi`,
então termos com o mesmo grau total nas variáveis são agrupados juntos.

<!-- category: Other -->
<!-- keywords: revert, revert2 -->
<!-- signatures: revert(expr, x), revert2(expr, x, n) -->
### Function: revert (expr, x)

Essas funções retornam a reversão de *expr*, uma série de Taylor sobre zero na variável *x*.
`revert` retorna um polinómio de grau igual ao maior expoente em *expr*.
`revert2` retorna um polinómio de grau *n*,
o qual pode ser maior que, igual a, ou menor que o grau de *expr*.


`load ("revert")` chama essas funções.


Exemplos:



```maxima
(%i1) load ("revert")$
(%i2) t: taylor (exp(x) - 1, x, 0, 6);
                   2    3    4    5     6
                  x    x    x    x     x
(%o2)/T/      x + -- + -- + -- + --- + --- + . . .
                  2    6    24   120   720
(%i3) revert (t, x);
               6       5       4       3       2
           10 x  - 12 x  + 15 x  - 20 x  + 30 x  - 60 x
(%o3)/R/ - --------------------------------------------
                                60
(%i4) ratexpand (%);
                     6    5    4    3    2
                    x    x    x    x    x
(%o4)             - -- + -- - -- + -- - -- + x
                    6    5    4    3    2
(%i5) taylor (log(x+1), x, 0, 6);
                    2    3    4    5    6
                   x    x    x    x    x
(%o5)/T/       x - -- + -- - -- + -- - -- + . . .
                   2    3    4    5    6
(%i6) ratsimp (revert (t, x) - taylor (log(x+1), x, 0, 6));
(%o6)                           0
(%i7) revert2 (t, x, 4);
                          4    3    2
                         x    x    x
(%o7)                  - -- + -- - -- + x
                         4    3    2
```

<!-- category: Other -->
<!-- keywords: taylor -->
<!-- signatures: taylor(expr, x, a, n), taylor(expr, [x_1, x_2, ...], a, n), taylor(expr, [x, a, n, 'asymp]), taylor(expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...]), taylor(expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...) -->
### Function: taylor (expr, x, a, n)

`taylor (expr, x, a, n)` expande a expressão *expr*
em uma série truncada de Taylor ou de Laurent na variável *x*
em torno do ponto *a*,
contendo termos até `(x - a)^n`.


Se *expr* é da forma `f(x)/g(x)`
e `g(x)` não possui de grau acima do grau *n*
então `taylor` tenta expandir `g(x)` acima do gau `2 n`.
Se existe ainda termos não zero, `taylor` dobra o
grau de expansão de `g(x)`
contanto que o grau da expansão o grau da expansão seja menor que ou igual a `n 2^taylordepth`.


`taylor (expr, [x_1, x_2, ...], a, n)`
retorna uma série de potência truncada 
de grau *n* em todas as variáveis *x_1*, *x_2*, ...
sobre o ponto `(a, a, ...)`.


`taylor (expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...)`
retorna uma série de potência truncada nas variáveis *x_1*, *x_2*, ...
sobre o ponto `(a_1, a_2, ...)`,
truncada em *n_1*, *n_2*, ....


`taylor (expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...])`
retorna uma série de potência truncada nas variáveis *x_1*, *x_2*, ...
sobre o ponto `(a_1, a_2, ...)`,
truncada em *n_1*, *n_2*, ....


`taylor (expr, [x, a, n, 'asymp])`
retorna uma expansão de *expr* em expoentes negativos de `x - a`.
O termo de maior ordem é `(x - a)^-n`.


Quando `maxtayorder` for `true`, então durante maniplulação
algébrica da séries de Taylor (truncada), `taylor` tenta reter
tantos termos quantos forem conhecidos serem correctos.


Quando `psexpand` for `true`,
uma expressão de função racional extendida é mostrada completamente expandida.
O comutador `ratexpand` tem o mesmo efeito.
Quando `psexpand` for `false`,
uma expressão de várias variáveis é mostrada apenas como no pacote de função racional.
Quando `psexpand` for  `multi`,
então os termos com o mesmo grau total nas variáveis são agrupados juntos.


Veja também o comutador `taylor_logexpand` para controlar a expansão.


Exemplos:




















```maxima
(%i1) taylor (sqrt (sin(x) + a*x + 1), x, 0, 3);
                           2             2
             (a + 1) x   (a  + 2 a + 1) x
(%o1)/T/ 1 + --------- - -----------------
                 2               8

                                   3      2             3
                               (3 a  + 9 a  + 9 a - 1) x
                             + -------------------------- + . . .
                                           48
(%i2) %^2;
                                    3
                                   x
(%o2)/T/           1 + (a + 1) x - -- + . . .
                                   6
(%i3) taylor (sqrt (x + 1), x, 0, 5);
                       2    3      4      5
                  x   x    x    5 x    7 x
(%o3)/T/      1 + - - -- + -- - ---- + ---- + . . .
                  2   8    16   128    256
(%i4) %^2;
(%o4)/T/                  1 + x + . . .
(%i5) product ((1 + x^i)^2.5, i, 1, inf)/(1 + x^2);
                         inf
                        /===\
                         ! !    i     2.5
                         ! !  (x  + 1)
                         ! !
                        i = 1
(%o5)                   -----------------
                              2
                             x  + 1
(%i6) ev (taylor(%, x,  0, 3), keepfloat);
                               2           3
(%o6)/T/    1 + 2.5 x + 3.375 x  + 6.5625 x  + . . .
(%i7) taylor (1/log (x + 1), x, 0, 3);
                               2       3
                 1   1   x    x    19 x
(%o7)/T/         - + - - -- + -- - ----- + . . .
                 x   2   12   24    720
(%i8) taylor (cos(x) - sec(x), x, 0, 5);
                                4
                           2   x
(%o8)/T/                - x  - -- + . . .
                               6
(%i9) taylor ((cos(x) - sec(x))^3, x, 0, 5);
(%o9)/T/                    0 + . . .
(%i10) taylor (1/(cos(x) - sec(x))^3, x, 0, 5);
                                               2          4
            1     1       11      347    6767 x    15377 x
(%o10)/T/ - -- + ---- + ------ - ----- - ------- - --------
             6      4        2   15120   604800    7983360
            x    2 x    120 x

                                                          + . . .
(%i11) taylor (sqrt (1 - k^2*sin(x)^2), x, 0, 6);
               2  2       4      2   4
              k  x    (3 k  - 4 k ) x
(%o11)/T/ 1 - ----- - ----------------
                2            24

                                    6       4       2   6
                               (45 k  - 60 k  + 16 k ) x
                             - -------------------------- + . . .
                                          720
(%i12) taylor ((x + 1)^n, x, 0, 4);
                      2       2     3      2         3
                    (n  - n) x    (n  - 3 n  + 2 n) x
(%o12)/T/ 1 + n x + ----------- + --------------------
                         2                 6

                               4      3       2         4
                             (n  - 6 n  + 11 n  - 6 n) x
                           + ---------------------------- + . . .
                                          24
(%i13) taylor (sin (y + x), x, 0, 3, y, 0, 3);
               3                 2
              y                 y
(%o13)/T/ y - -- + . . . + (1 - -- + . . .) x
              6                 2

                    3                       2
               y   y            2      1   y            3
          + (- - + -- + . . .) x  + (- - + -- + . . .) x  + . . .
               2   12                  6   12
(%i14) taylor (sin (y + x), [x, y], 0, 3);
                     3        2      2      3
                    x  + 3 y x  + 3 y  x + y
(%o14)/T/   y + x - ------------------------- + . . .
                                6
(%i15) taylor (1/sin (y + x), x, 0, 3, y, 0, 3);
          1   y              1    1               1            2
(%o15)/T/ - + - + . . . + (- -- + - + . . .) x + (-- + . . .) x
          y   6               2   6                3
                             y                    y

                                           1            3
                                      + (- -- + . . .) x  + . . .
                                            4
                                           y
(%i16) taylor (1/sin (y + x), [x, y], 0, 3);
                             3         2       2        3
            1     x + y   7 x  + 21 y x  + 21 y  x + 7 y
(%o16)/T/ ----- + ----- + ------------------------------- + . . .
          x + y     6                   360
```

<!-- category: Other -->
<!-- keywords: taylor_logexpand -->
<!-- signatures: taylor_logexpand -->
### Variable: taylor_logexpand

Valor por omissão: `true`


`taylor_logexpand` controla expansão de logaritmos em
séries de `taylor`.


Quando `taylor_logexpand` for `true`, todos  logaritmos são expandidos completamente dessa forma
problemas de reconhecimento de zero envolvendo envolvendo identidades logarítmicas não
atrapalham o processo de expansão.  Todavia, esse esquema não é sempre
matematicamente correcto uma vez que isso ignora informações de ramo.


Quando `taylor_logexpand` for escolhida para `false`, então a expansão logarítmica que ocorre
é somente aquela que for necessária para obter uma séries de potência formal.

<!-- category: Other -->
<!-- keywords: taylor_order_coefficients -->
<!-- signatures: taylor_order_coefficients -->
### Variable: taylor_order_coefficients

Valor por omissão: `true`


`taylor_order_coefficients` controla a ordenação dos
coeficientes em uma série de Taylor.


Quando `taylor_order_coefficients` for `true`,
coeficientes da séries de Taylor são ordenados canonicamente.

<!-- category: Other -->
<!-- keywords: taylor_simplifier -->
<!-- signatures: taylor_simplifier(expr) -->
### Function: taylor_simplifier (expr)

Simplifica coeficientes da séries  de potência *expr*.
`taylor` chama essa função.

<!-- category: Other -->
<!-- keywords: taylor_truncate_polynomials -->
<!-- signatures: taylor_truncate_polynomials -->
### Variable: taylor_truncate_polynomials

Valor por omissão: `true`



Quando `taylor_truncate_polynomials` for `true`,
polinómios são truncados baseados sobre a entrada de níveis de truncação.


De outra forma,
entrada de polinómios para `taylor` são consideradas terem precisão infinita.

<!-- category: Other -->
<!-- keywords: taylordepth -->
<!-- signatures: taylordepth -->
### Variable: taylordepth

Valor por omissão: 3



Se existem ainda termos não zero, `taylor` dobra o
grau da expansão de `g(x)`
contanto que o grau da expansão seja menor que ou igual a `n 2^taylordepth`.

<!-- category: Other -->
<!-- keywords: taylorinfo -->
<!-- signatures: taylorinfo(expr) -->
### Function: taylorinfo (expr)

Retorna information about the séries de Taylor *expr*.
O valor de retorno é uma lista de listas.
Cada lista compreende o nome de uma variável,
o ponto de expansão, e o grau da expansão.


`taylorinfo` retorna `false` se *expr* não for uma séries de Taylor.


Exemplo:



```maxima
(%i1) taylor ((1 - y^2)/(1 - x), x, 0, 3, [y, a, inf]);
                  2                       2
(%o1)/T/ - (y - a)  - 2 a (y - a) + (1 - a )

         2                        2
 + (1 - a  - 2 a (y - a) - (y - a) ) x

         2                        2   2
 + (1 - a  - 2 a (y - a) - (y - a) ) x

         2                        2   3
 + (1 - a  - 2 a (y - a) - (y - a) ) x  + . . .
(%i2) taylorinfo(%);
(%o2)               [[y, a, inf], [x, 0, 3]]
```

<!-- category: Other -->
<!-- keywords: taylorp -->
<!-- signatures: taylorp(expr) -->
### Function: taylorp (expr)

Retorna `true` se *expr* for uma séries de Taylor,
e `false` de outra forma.

<!-- category: Other -->
<!-- keywords: taytorat -->
<!-- signatures: taytorat(expr) -->
### Function: taytorat (expr)

Converte *expr* da forma `taylor` para a forma de expressão racional canónica (CRE).
O efeito é o mesmo que `rat (ratdisrep (expr))`, mas mais rápido.

<!-- category: Other -->
<!-- keywords: trunc -->
<!-- signatures: trunc(expr) -->
### Function: trunc (expr)

Coloca notas na representação interna da expressão geral *expr*
de modo que isso é mostrado como se suas adições forem séries de Taylor truncadas.
*expr* is not otherwise modified.


Exemplo:



```maxima
(%i1) expr: x^2 + x + 1;
                            2
(%o1)                      x  + x + 1
(%i2) trunc (expr);
                                2
(%o2)                  1 + x + x  + . . .
(%i3) is (expr = trunc (expr));
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: unsum -->
<!-- signatures: unsum(f, n) -->
### Function: unsum (f, n)

Retorna a primeira diferençã de trás para frente `f(n) - f(n - 1)`.
Dessa forma `unsum` logicamente é a inversa de `sum`.


Veja também `nusum`.


Exemplos:








```maxima
(%i1) g(p) := p*4^n/binomial(2*n,n);
                                     n
                                  p 4
(%o1)               g(p) := ----------------
                            binomial(2 n, n)
(%i2) g(n^4);
                              4  n
                             n  4
(%o2)                   ----------------
                        binomial(2 n, n)
(%i3) nusum (%, n, 0, n);
                     4        3       2              n
      2 (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3) 4      2
(%o3) ------------------------------------------------ - ------
                    693 binomial(2 n, n)                 3 11 7
(%i4) unsum (%, n);
                              4  n
                             n  4
(%o4)                   ----------------
                        binomial(2 n, n)
```

<!-- category: Other -->
<!-- keywords: verbose -->
<!-- signatures: verbose -->
### Variable: verbose

Valor por omissão: `false`


Quando `verbose` for `true`,
`powerseries` mostra mensagens de progresso.

