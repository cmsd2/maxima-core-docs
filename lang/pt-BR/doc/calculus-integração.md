## Integração

<!-- category: Calculus -->
<!-- keywords: changevar -->
<!-- signatures: changevar(expr, f(x,y), y, x) -->
### Function: changevar (expr, f(x,y), y, x)

Faz a mudança de variável dada por
`f(x,y) = 0` em todas as integrais que ocorrem em *expr* com integração em
relação a *x*.
A nova variável é *y*.




```maxima
(%i1) assume(a > 0)$
(%i2) 'integrate (%e**sqrt(a*y), y, 0, 4);
                      4
                     /
                     [    sqrt(a) sqrt(y)
(%o2)                I  %e                dy
                     ]
                     /
                      0
(%i3) changevar (%, y-z^2/a, z, y);
                      0
                     /
                     [                abs(z)
                   2 I            z %e       dz
                     ]
                     /
                      - 2 sqrt(a)
(%o3)            - ----------------------------
                                a
```


Uma expressão contendo uma forma substantiva, tais como as instâncias de `'integrate` acima,
pode ser avaliada por `ev` com o sinalizador `nouns`.
Por exemplo, a expressão retornada por `changevar` acima pode ser avaliada
por `ev (%o3, nouns)`.


`changevar` pode também ser usada para alterações nos índices de uma soma ou de um
produto.  Todavia, isso deve obrigatóriamente ser realizado de forma que quando uma alteração é feita em uma
soma ou produto, essa mudança deve ser um artifício, i.e., `i = j+ ...`, não uma
função de grau mais alto.  E.g.,



```maxima
(%i4) sum (a[i]*x^(i-2), i, 0, inf);
                         inf
                         ====
                         \         i - 2
(%o4)                     >    a  x
                         /      i
                         ====
                         i = 0
(%i5) changevar (%, i-2-n, n, i);
                        inf
                        ====
                        \               n
(%o5)                    >      a      x
                        /        n + 2
                        ====
                        n = - 2
```

<!-- category: Calculus -->
<!-- keywords: dblint -->
<!-- signatures: dblint(f, r, s, a, b) -->
### Function: dblint (f, r, s, a, b)

Uma rotina de integral dupla que foi escrita no 
alto-nível do Maxima e então traduzida e compilada para linguagem de máquina.
Use `load ("dblint")` para acessar esse pacote.  Isso usa o método da regra de 
Simpson em ambas as direções x e y para calcular



```maxima
/b /s(x)
|  |
|  |    f(x,y) dy dx
|  |
/a /r(x)
```


A função *f* deve ser uma função traduzida ou compilada de duas
variáveis, e *r* e *s* devem cada uma ser uma função traduzida ou
compilada de uma variável, enquanto *a* e *b* devem ser números em ponto
flutuante.  A rotina tem duas variáveis globais que determinam o
número de divisões dos intervalos x e y: `dblint_x` e `dblint_y`,
ambas as quais são inicialmente 10, e podem ser alteradas independentemente para
outros valores inteiros (existem `2*dblint_x+1` pontos calculados na
direção x , e `2*dblint_y+1` na direção y).
A rotina subdivide o eixo X e então para cada valor de X isso
primeiro calcula `r(x)` e `s(x)`; então o eixo Y entre `r(x)` e `s(x)` é
subdividido e a integral ao longo do eixo Y é executada usando
a regra de Simpson; então a integral ao longo do eixo X é concluída usando
a regra de Simpson com os valores da função sendo as integrais-Y.  Esse
procedimento pode ser numericamente instável por uma grande variedade razões,
mas razoávelmente rápido: evite usar isso sobre funções altamente oscilatórias
e funções com singularidades (postes ou pontos de ramificação na
região).  As integrais Y dependem de quanto fragmentados `r(x)` e `s(x)` são,
então se a ditância `s(x) - r(x)` varia rapidamente com X, nesse ponto pode ter
erros substanciais provenientes de truncação com diferentes saltos-tamanhos
nas várias integrais Y.  Um pode incrementar `dblint_x` e `dblint_y` em
uma tentativa para melhorar a convergência da reião, com sacrifício do
tempo de computação.  Os valores da função não são salvos, então se a
função é muito desperdiçadora de tempo,você terá de esperar por
re-computação se você mudar qualquer coisa (desculpe).
Isso é requerido que as funções *f*, *r*, e *s* sejam ainda traduzidas
ou compiladas previamente chamando `dblint`.  Isso resultará em ordens de
magnitude de melhoramentos de velocidade sobre o código interpretado em muitos casos!


`demo (dblint)` executa uma demonstração de `dblint` aplicado a um problema exemplo.

<!-- category: Calculus -->
<!-- keywords: defint -->
<!-- signatures: defint(expr, x, a, b) -->
### Function: defint (expr, x, a, b)

Tenta calcular uma integral definida.
`defint` é chamada por `integrate` quando limites de integração são especificados,
i.e., quando `integrate` é chamado como `integrate (expr, x, a, b)`.
Dessa forma do ponto de vista do usuário, isso é suficiente para chamar `integrate`.



`defint` retorna uma expressão simbólica,
e executa um dos dois: ou calcula a integral ou a forma substantiva da integral.
Veja `quad_qag` e funções rellacionadas para aproximação numérica de integrais definidas.

<!-- category: Calculus -->
<!-- keywords: erf -->
<!-- signatures: erf(x) -->
### Function: erf (x)

Representa a função de erro, cuja derivada é:
`2*exp(-x^2)/sqrt(%pi)`.

<!-- category: Calculus -->
<!-- keywords: erfflag -->
<!-- signatures: erfflag -->
### Variable: erfflag

Valor padrão: `true`


Quando `erfflag` é `false`, previne `risch` da introdução da
função `erf` na resposta se não houver nenhum no integrando para
começar.

<!-- category: Calculus -->
<!-- keywords: ilt -->
<!-- signatures: ilt(expr, t, s) -->
### Function: ilt (expr, t, s)

Calcula a transformação inversa de Laplace de *expr* em
relação a *t* e parâmetro *s*.  *expr* deve ser uma razão de
polinômios cujo denominador tem somente fatores lineares e quadráticos.
Usando a funções `laplace` e `ilt` juntas com as funções `solve` ou
`linsolve` o usuário pode resolver uma diferencial simples ou
uma equação integral de convolução ou um conjunto delas.



```maxima
(%i1) 'integrate (sinh(a*x)*f(t-x), x, 0, t) + b*f(t) = t**2;
              t
             /
             [                                    2
(%o1)        I  f(t - x) sinh(a x) dx + b f(t) = t
             ]
             /
              0
(%i2) laplace (%, t, s);
                               a laplace(f(t), t, s)   2
(%o2)  b laplace(f(t), t, s) + --------------------- = --
                                       2    2           3
                                      s  - a           s
(%i3) linsolve ([%], ['laplace(f(t), t, s)]);
                                        2      2
                                     2 s  - 2 a
(%o3)     [laplace(f(t), t, s) = --------------------]
                                    5         2     3
                                 b s  + (a - a  b) s
(%i4) ilt (rhs (first (%)), s, t);
Is  a b (a b - 1)  positive, negative, or zero?

pos;
               sqrt(a b (a b - 1)) t
        2 cosh(---------------------)       2
                         b               a t
(%o4) - ----------------------------- + -------
              3  2      2               a b - 1
             a  b  - 2 a  b + a

                                                       2
                                             + ------------------
                                                3  2      2
                                               a  b  - 2 a  b + a
```

<!-- category: Calculus -->
<!-- keywords: integrate -->
<!-- signatures: integrate(expr, x), integrate(expr, x, a, b) -->
### Function: integrate (expr, x)

Tenta símbolicamente calcular a integral de *expr* em relação a *x*.
`integrate (expr, x)` é uma integral indefinida,
enquanto `integrate (expr, x, a, b)` é uma integral definida,
com limites de integração *a* e *b*.
Os limites não poderam conter *x*, embora `integrate` não imponha essa restrição.
*a* não precisa ser menor que *b*.
Se *b* é igual a *a*, `integrate` retorna zero.


Veja `quad_qag` e funções relacionadas para aproximação numérica de integrais definidas.
Veja `residue` para computação de resíduos (integração complexa).
Veja `antid` para uma forma alternativa de calcular integrais indefinidas.


A integral (uma expressão livre de `integrate`) é retornada se `integrate` obtém sucesso.
De outra forma o valor de retorno é
a forma substantiva da integral (o operador com apóstrofo `'integrate`)
ou uma expressão contendo uma ou mais formas substantivas.
A forma substantiva de `integrate` é mostrada com um sinal de integral.


Em algumas circunstâncias isso é útil para construir uma forma substantiva manualmente,
colocando em `integrate` um apóstrofo, e.g., `'integrate (expr, x)`.
Por exemplo, a integral pode depender de alguns parâmetos que não estão ainda calculados.
A forma substantiva pode ser aplicada a seus argumentos por `ev (i, nouns)`
onde *i* é a forma substantiva de interesse.



`integrate` manuseia integrais definidas separadamente das indefinidas,
e utiliza uma gama de heurísticas para manusear cada caso.
Casos especiais de integrais definidas incluem limites de integração iguais a
zero ou infinito (`inf` ou `minf`),
funções trigonométricas com limites de integração iguais a zero e `%pi` ou `2 %pi`,
funções racionais,
integrais relacionadas para as definições de funções `beta` e `psi`,
e algumas integrais logarítmicas e trigonométricas.
Processando funções racionais pode incluir computação de resíduo.
Se um caso especial aplicável não é encontrado,
tentativa será feita para calcular a integra indefinida e avaliar isso nos limites de integração.
Isso pode incluir pegar um limite como um limite de integração tendendo ao infinito ou a menos infinito;
veja também `ldefint`.


Casos especiais de integrais indefinidas incluem funções trigonométricas,
exponenciais e funções logarítmicas,
e funções racionais.
`integrate` pode também fazer uso de uma curta tabela de integais elementares.


`integrate` pode realizar uma mudança de variável
se o integrando tem a forma `f(g(x)) * diff(g(x), x)`.
`integrate` tenta achar uma subexpressão `g(x)` de forma que
a derivada de `g(x)` divida o integrando.
Essa busca pode fazer uso de derivadas definidas pela função `gradef`.
Veja também `changevar` e `antid`.


Se nenhum dos procedimentos heurísticos acha uma integral indefinida,
o algorítmo de Risch é executado.
O sinalizador `risch` pode ser escolhido como um `evflag`,
na chamada para `ev` ou na linha de comando,
e.g., `ev (integrate (expr, x), risch)` ou `integrate (expr, x), risch`.
Se `risch` está presente, `integrate` chama a função `risch`
sem tentar heurísticas primeiro.  Veja também `risch`.



`integrate` trabalha somente com relações funcionais representadas explicitamente com a notação `f(x)`.
`integrate` não respeita dependências implicitas estabelecidas pela função `depends`.
`integrate` pode necessitar conhecer alguma propriedade de um parâmetro no integrando.
`integrate` irá primeiro consultar a base de dados do `assume`,
e , se a variável de interesse não está lá,
`integrate` perguntará ao usuário.
Dependendo da pergunta,
respostas adequadas são `yes;` ou `no;`,
ou `pos;`, `zero;`, ou `neg;`.


`integrate` não é, por padrão, declarada ser linear.  Veja `declare` e `linear`.


`integrate` tenta integração por partes somente em uns poucos casos especiais.


Exemplos:



- *
Integrais definidas e indefinidas elementares.

```maxima
(%i1) integrate (sin(x)^3, x);
                           3
                        cos (x)
(%o1)                   ------- - cos(x)
                           3
(%i2) integrate (x/ sqrt (b^2 - x^2), x);
                                 2    2
(%o2)                    - sqrt(b  - x )
(%i3) integrate (cos(x)^2 * exp(x), x, 0, %pi);
                               %pi
                           3 %e      3
(%o3)                      ------- - -
                              5      5
(%i4) integrate (x^2 * exp(-x^2), x, minf, inf);
                            sqrt(%pi)
(%o4)                       ---------
                                2
```
- *
Uso de `assume` e dúvida interativa.

```maxima
(%i1) assume (a > 1)$
(%i2) integrate (x**a/(x+1)**(5/2), x, 0, inf);
    2 a + 2
Is  -------  an integer?
       5
no;
Is  2 a - 3  positive, negative, or zero?
neg;
                                   3
(%o2)                  beta(a + 1, - - a)
                                   2
```
- *
Mudança de variável.  Existem duas mudanças de variável nesse exemplo:
uma usando a derivada estabelecida por `gradef`,
e uma usando a derivação `diff(r(x))` de uma função não especificada `r(x)`.

```maxima
(%i3) gradef (q(x), sin(x**2));
(%o3)                         q(x)
(%i4) diff (log (q (r (x))), x);
                      d               2
                     (-- (r(x))) sin(r (x))
                      dx
(%o4)                ----------------------
                            q(r(x))
(%i5) integrate (%, x);
(%o5)                     log(q(r(x)))
```
- *
O valor de retorno contém a forma substantiva `'integrate`.
Nesse exemplo, Maxima pode extrair um fator do denominador
de uma função racional, mas não pode fatorar o restante ou de outra forma achar sua integral.
`grind` mostra a forma substantiva `'integrate` no resultado.
Veja também `integrate_use_rootsof` para mais sobre integrais de funções racionais.

```maxima
(%i1) expand ((x-4) * (x^3+2*x+1));
                    4      3      2
(%o1)              x  - 4 x  + 2 x  - 7 x - 4
(%i2) integrate (1/%, x);
                              /  2
                              [ x  + 4 x + 18
                              I ------------- dx
                              ]  3
                 log(x - 4)   / x  + 2 x + 1
(%o2)            ---------- - ------------------
                     73               73
(%i3) grind (%);
log(x-4)/73-('integrate((x^2+4*x+18)/(x^3+2*x+1),x))/73$
```
- *
Definindo uma função em termos de uma integral.
O corpo de uma função não é avaliado quando a função é definida.
Dessa forma o corpo de `f_1` nesse exemplo contém a forma substantiva de `integrate`.
O operador apóstrofo-apóstrofo `''` faz com que a integral seja avaliada,
e o resultado transforme-se no corpo de `f_2`.

```maxima
(%i1) f_1 (a) := integrate (x^3, x, 1, a);
                                     3
(%o1)           f_1(a) := integrate(x , x, 1, a)
(%i2) ev (f_1 (7), nouns);
(%o2)                          600
(%i3) /* Note parentheses around integrate(...) here */
      f_2 (a) := ''(integrate (x^3, x, 1, a));
                                   4
                                  a    1
(%o3)                   f_2(a) := -- - -
                                  4    4
(%i4) f_2 (7);
(%o4)                          600
```

<!-- category: Calculus -->
<!-- keywords: integrate_use_rootsof -->
<!-- signatures: integrate_use_rootsof -->
### Variable: integrate_use_rootsof

Valor padrão: `false`


Quando `integrate_use_rootsof` é `true` e o denominador de
uma função racional não pode ser fatorado, `integrate` retorna a integral
em uma forma que é uma soma sobre as raízes (não conhecidas ainda) do denominador.


Por exemplo, com `integrate_use_rootsof` escolhido para `false`,
`integrate` retorna uma integral não resolvida de uma função racional na forma substantiva:



```maxima
(%i1) integrate_use_rootsof: false$
(%i2) integrate (1/(1+x+x^5), x);
        /  2
        [ x  - 4 x + 5
        I ------------ dx                            2 x + 1
        ]  3    2                2            5 atan(-------)
        / x  - x  + 1       log(x  + x + 1)          sqrt(3)
(%o2)   ----------------- - --------------- + ---------------
                7                 14             7 sqrt(3)
```


Agora vamos escolher o sinalizador para ser true e a parte não resolvida da
integral será expressa como um somatório sobre as raízes do denominador da função racional:



```maxima
(%i3) integrate_use_rootsof: true$
(%i4) integrate (1/(1+x+x^5), x);
      ====        2
      \       (%r4  - 4 %r4 + 5) log(x - %r4)
       >      -------------------------------
      /                    2
      ====            3 %r4  - 2 %r4
                        3      2
      %r4 in rootsof(%r4  - %r4  + 1, %r4)
(%o4) ----------------------------------------------------------
               7

                                                             2 x + 1
                                         2            5 atan(-------)
                                    log(x  + x + 1)          sqrt(3)
                                  - --------------- + ---------------
                                          14             7 sqrt(3)
```


Alternativamente o usuário pode calcular as raízes do denominador separadamente,
e então expressar o integrando em termos dessas raízes,
e.g., `1/((x - a)*(x - b)*(x - c))` ou `1/((x^2 - (a+b)*x + a*b)*(x - c))`
se o denominador for um polinômio cúbico.
Algumas vezes isso ajudará Maxima a obter resultados mais úteis.

<!-- category: Calculus -->
<!-- keywords: integration_constant_counter -->
<!-- signatures: integration_constant_counter -->
### Variable: integration_constant_counter

Valor padrão: 0




`integração_constant_counter` é um contador que é atualizado a cada vez que uma
constante de integração (nomeada pelo Maxima, e.g., `integrationconstant1`)
é introduzida em uma expressão pela integração indefinida de uma equação.

<!-- category: Calculus -->
<!-- keywords: ldefint -->
<!-- signatures: ldefint(expr, x, a, b) -->
### Function: ldefint (expr, x, a, b)

Tenta calcular a integral definida de *expr* pelo uso de 
`limit` para avaliar a integral indefinida *expr* em relação a *x*
no limite superior *b* e no limite inferior *a*.
Se isso falha para calcular a integral definida,
`ldefint` retorna uma expressão contendo limites como formas substantivas.


`ldefint` não é chamada por `integrate`,
então executando `ldefint (expr, x, a, b)` pode retornar um resultado diferente de
`integrate (expr, x, a, b)`.
`ldefint` sempre usa o mesmo método para avaliar a integral definida,
enquanto `integrate` pode utilizar várias heurísticas e pode reconhecer alguns casos especiais.

<!-- category: Calculus -->
<!-- keywords: potential -->
<!-- signatures: potential(givengradient) -->
### Function: potential (givengradient)

O cálculo faz uso da variável global `potentialzeroloc[0]`
que deve ser `nonlist` ou da forma



```maxima
[indeterminatej=expressãoj, indeterminatek=expressãok, ...]
```


O
formador sendo equivalente para a expressão nonlist para todos os lados
direitos-manuseados mais tarde.  Os lados direitos indicados são usados como o
limite inferior de integração.  O sucesso das integrações pode
depender de seus valores e de sua ordem.  `potentialzeroloc` é inicialmente escolhido
para 0.

<!-- category: Calculus -->
<!-- keywords: quad_qag -->
<!-- signatures: quad_qag(f(x), x, a, b, chave, epsrel, limite), quad_qag(f, x, a, b, chave, epsrel, limite) -->
### Function: quad_qag (f(x), x, a, b, chave, epsrel, limite)

Integração de uma função genérica sobre um intervalo finito.
`quad_qag` implementa um integrador adaptativo globalmente simples usando a estratégia de Aind (Piessens, 1973).
O chamador pode escolher entre 6 pares de fórmulas da quadratura de
Gauss-Kronrod para a componente de avaliação da regra.
As regras de alto nível são adequadas para integrandos fortemente oscilatórios.


`quad_qag` calcula a integral



$$
\int_a^b {f(x) dx}
$$


A função a ser integrada é *f(x)*, com variável
dependente *x*, e a função é para ser integrada entre os
limites *a* e *b*.  *chave* é o integrador a ser usado
e pode ser um inteiro entre 1 e 6, inclusive.  O valor de
*chave* seleciona a ordem da regra de integração de Gauss-Kronrod.
Regra de alta ordem são adequadas para integrandos fortemente oscilatórios.


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


A integração numérica é concluída adaptativamente pela subdivisão a
região de integração até que a precisão desejada for
completada.


Os argumentos opcionais *epsrel* e *limite* são o erro relativo
desejado e o número máximo de subintervalos respectivamente.
*epsrel* padrão em 1e-8 e *limite* é 200.


`quad_qag` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valor de retorno) pode ter os valores:



**0** — se nenhum problema for encontrado;
**1** — se muitos subintervalos foram concluídos;
**2** — se erro excessivo é detectado;
**3** — se ocorre comportamento extremamente ruim do integrando;
**6** — se a entrada é inválida.




Exemplos:



```maxima
(%i1) quad_qag (x^(1/2)*log(1/x), x, 0, 1, 3);
(%o1)    [.4444444444492108, 3.1700968502883E-9, 961, 0]
(%i2) integrate (x^(1/2)*log(1/x), x, 0, 1);
                                4
(%o2)                           -
                                9
```

<!-- category: Calculus -->
<!-- keywords: quad_qagi -->
<!-- signatures: quad_qagi(f(x), x, a, inftype, epsrel, limite), quad_qagi(f, x, a, inftype, epsrel, limite) -->
### Function: quad_qagi (f(x), x, a, inftype, epsrel, limite)

Integração de uma função genérica sobre um intervalo finito ou semi-finito.
O intervalo é mapeado sobre um intervalo finito e
então a mesma estratégia que em `quad_qags` é aplicada.


`quad_qagi` avalia uma das seguintes integrais



$$
\int_a^\infty {f(x) dx}
$$



$$
\int_\infty^a {f(x) dx}
$$



$$
\int_{-\infty}^\infty {f(x) dx}
$$


usando a rotina Quadpack QAGI.  A função a ser integrada é
*f(x)*, com variável dependente *x*, e a função é para
ser integrada sobre um intervalo infinito.


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


O parâmetro *inftype* determina o intervalo de integração como segue:



**inf** — O intervalo vai de *a* ao infinito positivo.
**minf** — O intervalo vai do infinito negativo até *a*.
**both** — O intervalo corresponde a toda reta real.


Os argumentos opcionais *epsrel* e *limite* são o erro relativo
desejado e o número maximo de subintervalos, respectivamente.
*epsrel* padrão para 1e-8 e *limite* é 200.


`quad_qagi` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valor de retorno) pode ter os valores:



**0** — nenhum problema foi encontrado;
**1** — muitos subintervalos foram concluídos;
**2** — erro excessivo é detectado;
**3** — ocorreu comportamento excessivamente ruim do integrando;
**4** — falhou para convergência;
**5** — integral é provavelmente divergente ou lentamente convergente;
**6** — se a entrada for inválida.




Exemplos:



```maxima
(%i1) quad_qagi (x^2*exp(-4*x), x, 0, inf);
(%o1)        [0.03125, 2.95916102995002E-11, 105, 0]
(%i2) integrate (x^2*exp(-4*x), x, 0, inf);
                               1
(%o2)                          --
                               32
```

<!-- category: Calculus -->
<!-- keywords: quad_qags -->
<!-- signatures: quad_qags(f(x), x, a, b, epsrel, limite), quad_qags(f, x, a, b, epsrel, limite) -->
### Function: quad_qags (f(x), x, a, b, epsrel, limite)

Integração de uma função geral sobre um intervalo finito.
`quad_qags` implementa subdivisão de intervalo globalmente adaptativa com extrapolação
(de Doncker, 1978) através do algorítmo de (Wynn, 1956).


`quad_qags` computes the integral



$$
\int_a^b {f(x) dx}
$$


A função a ser integrada é *f(x)*, com
variável dependente *x*, e a função é para ser integrada
entre os limites *a* e *b*.


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


Os argumentos opcionais *epsrel* e *limite* são o erro relativo
desejado e o número máximo de subintervalos, respectivamente.
*epsrel* padrão em 1e-8 e *limite* é 200.


`quad_qags` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valor de retorno) pode ter os valores:



**0** — nenhum problema foi encontrado;
**1** — muitos subintervalos foram concluídos;
**2** — erro excessivo é detectado;
**3** — ocorreu comportamento excessivamente ruim do integrando;
**4** — falhou para convergência
**5** — integral é provavelmente divergente ou lentamente convergente
**6** — se a entrada é inválida.




Exemplos:



```maxima
(%i1) quad_qags (x^(1/2)*log(1/x), x, 0 ,1);
(%o1)   [.4444444444444448, 1.11022302462516E-15, 315, 0]
```


Note que `quad_qags` é mais preciso e eficiente que `quad_qag` para esse integrando.

<!-- category: Calculus -->
<!-- keywords: quad_qawc -->
<!-- signatures: quad_qawc(f(x), x, c, a, b, epsrel, limite), quad_qawc(f, x, c, a, b, epsrel, limite) -->
### Function: quad_qawc (f(x), x, c, a, b, epsrel, limite)

Calcula o valor principal de Cauchy de $f(x)/(x - c)$ over a finite interval.
A estratégia é globalmente adaptativa, e a integração de
Clenshaw-Curtis modificada é usada sobre as subamplitudes
que possuírem o ponto $x = c$.


`quad_qawc` calcula o valor principal de Cauchy de



$$
\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}
$$


usando a rotina Quadpack QAWC.  A função a ser integrada é
`f(x)/(x - c)`, com variável dependente *x*, e a função
é para ser integrada sobre o intervalo que vai de *a* até *b*.


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


Os argumentos opcionais *epsrel* e *limite* são o erro relativo
desejado e o máximo número de subintervalos, respectivamente.
*epsrel* padrão para 1e-8 e *limite* é 200.


`quad_qawc` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valoor de retorno) pode ter os valores:



**0** — nenhum problema foi encontrado;
**1** — muitos subintervalos foram concluídos;
**2** — erro excessivo é detectado;
**3** — ocorreu comportamento excessivamente ruim do integrando;
**6** — se a entrada é inválida.


Exemplos:



```maxima
(%i1) quad_qawc (2^(-5)*((x-1)^2+4^(-5))^(-1), x, 2, 0, 5);
(%o1)    [- 3.130120337415925, 1.306830140249558E-8, 495, 0]
(%i2) integrate (2^(-alpha)*(((x-1)^2 + 4^(-alpha))*(x-2))^(-1), x, 0, 5);
Principal Value
                       alpha
        alpha       9 4                 9
       4      log(------------- + -------------)
                      alpha           alpha
                  64 4      + 4   64 4      + 4
(%o2) (-----------------------------------------
                        alpha
                     2 4      + 2

         3 alpha                       3 alpha
         -------                       -------
            2            alpha/2          2          alpha/2
      2 4        atan(4 4       )   2 4        atan(4       )   alpha
    - --------------------------- - -------------------------)/2
                alpha                        alpha
             2 4      + 2                 2 4      + 2
(%i3) ev (%, alpha=5, numer);
(%o3)                    - 3.130120337415917
```

<!-- category: Calculus -->
<!-- keywords: quad_qawf -->
<!-- signatures: quad_qawf(f(x), x, a, omega, trig, epsabs, limit, maxp1, limlst), quad_qawf(f, x, a, omega, trig, epsabs, limit, maxp1, limlst) -->
### Function: quad_qawf (f(x), x, a, omega, trig, epsabs, limit, maxp1, limlst)

Calcula uma transformação de cosseno de Fourier ou de um seno de Fourier sobre um intervalo semi-finito.
usando a função QAWF do pacote Quadpack.
A mesma aproxima como em `quad_qawo` quando aplicada sobre intervalos finitos sucessivos,
e aceleração de convergência por meio d algorítimo de Epsilon (Wynn, 1956) 
aplicado a séries de contribuições de integrais.


`quad_qawf` calcula a integral



$$
\int_a^\infty f(x) w(x) dx
$$


A função peso $w$ é selecionada por *trig*:



**cos** — $w(x) = cos (omega x)$
**sin** — $w(x) = sin (omega x)$


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


Os argumentos opcionais são:



**epsabs** — Erro absoluto de aproximação desejado.  Padrão é 1d-10.
**limit** — Tamanho de array interno de trabalho.  (*limit* - *limlst*)/2 é o
maximo número de subintervalos para usar.  O Padrão é 200.
**maxp1** — O número máximo dos momentos de Chebyshev.  Deve ser maior que 0.  O padrão
é 100.
**limlst** — Limite superior sobre número de ciclos.  Deve ser maior ou igual a
3.  O padrão é 10.



*epsabs* e *limit* são o erro relativo
desejado e o número maximo de subintervalos, respectivamente.
*epsrel* padrão para 1e-8 e *limit* é 200.


`quad_qawf` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valor de retorno) pode ter os valores:



**0** — nenhum problema foi encontrado;
**1** — muitos subintervalos foram concluídos;
**2** — erro excessivo é detectado;
**3** — ocorreu um comportamento excessivamente ruim do integrando;
**6** — se a entrada é invalida.


Exemplos:



```maxima
(%i1) quad_qawf (exp(-x^2), x, 0, 1, 'cos);
(%o1)   [.6901942235215714, 2.84846300257552E-11, 215, 0]
(%i2) integrate (exp(-x^2)*cos(x), x, 0, inf);
                          - 1/4
                        %e      sqrt(%pi)
(%o2)                   -----------------
                                2
(%i3) ev (%, numer);
(%o3)                   .6901942235215714
```

<!-- category: Calculus -->
<!-- keywords: quad_qawo -->
<!-- signatures: quad_qawo(f(x), x, a, b, omega, trig, epsabs, limite, maxp1, limlst), quad_qawo(f, x, a, b, omega, trig, epsabs, limite, maxp1, limlst) -->
### Function: quad_qawo (f(x), x, a, b, omega, trig, epsabs, limite, maxp1, limlst)

Integração de $cos(omega x) f(x)$ ou $sin(omega x) f(x)$ sobre um intervalo finito,
onde $omega$ é uma constante.
A componente de avaliação da regra é baseada na técnica modificada de Clenshaw-Curtis.
`quad_qawo` aplica subdivisão adaptativa com extrapolação, similar a `quad_qags`.


`quad_qawo` calcula a integral usando a rotina
Quadpack QAWO:



$$
\int_a^b f(x) w(x) dx
$$



A função peso $w$ é selecionada por *trig*:



**cos** — $w(x) = cos (omega x)$
**sin** — $w(x) = sin (omega x)$


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


Os argumentos opcionais são:



**epsabs** — Erro absoluto desejado de aproximação.  O Padrão é 1d-10.
**limite** — Tamanho do array interno de trabalho.  (*limite* - *limlst*)/2 é o
número máximo de subintervalos a serem usados.  Default é 200.
**maxp1** — Número máximo dos momentos de Chebyshev.  Deve ser maior que 0.  O padrão
é 100.
**limlst** — Limite superior sobre o número de ciclos.  Deve ser maior que ou igual a
3.  O padrão é 10.



*epsabs* e *limite* são o erro relativo
desejado e o número máximo de subintervalos, respectivamente.
*epsrel* o padrão é 1e-8 e *limite* é 200.


`quad_qawo` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valor de retorno) pode ter os valores:



**0** — nenhum problema foi encontrado;
**1** — muitos subintervalos foram concluídos;
**2** — erro excessivo é detectado;
**3** — comportamento extremamente ruim do integrando;
**6** — se a entrada é inválida.


Exemplos:



```maxima
(%i1) quad_qawo (x^(-1/2)*exp(-2^(-2)*x), x, 1d-8, 20*2^2, 1, cos);
(%o1)     [1.376043389877692, 4.72710759424899E-11, 765, 0]
(%i2) rectform (integrate (x^(-1/2)*exp(-2^(-alpha)*x) * cos(x), x, 0, inf));
                   alpha/2 - 1/2            2 alpha
        sqrt(%pi) 2              sqrt(sqrt(2        + 1) + 1)
(%o2)   -----------------------------------------------------
                               2 alpha
                         sqrt(2        + 1)
(%i3) ev (%, alpha=2, numer);
(%o3)                     1.376043390090716
```

<!-- category: Calculus -->
<!-- keywords: quad_qaws -->
<!-- signatures: quad_qaws(f(x), x, a, b, alpha, beta, wfun, epsabs, limite), quad_qaws(f, x, a, b, alpha, beta, wfun, epsabs, limite) -->
### Function: quad_qaws (f(x), x, a, b, alpha, beta, wfun, epsabs, limite)

Integração de $w(x) f(x)$ sobre um intervalo finito,
onde $w(x)$ é uma certa função algébrica ou logarítmica.
Uma estratégia de subdivisão globalmente adaptativa é aplicada,
com integração modificada de Clenshaw-Curtis sobre os subintervalos que possuírem os pontos finais
dos intervalos de integração.

 

`quad_qaws` calcula a integral usando a rotina
Quadpack QAWS:

 

$$
\int_a^b f(x) w(x) dx
$$


A função peso $w$ é selecionada por *wfun*:



**1** — $w(x) = (x - a)^alpha (b - x)^beta$
**2** — $w(x) = (x - a)^alpha (b - x)^beta log(x - a)$
**3** — $w(x) = (x - a)^alpha (b - x)^beta log(b - x)$
**4** — $w(x) = (x - a)^alpha (b - x)^beta log(x - a) log(b - x)$


O integrando pode ser especidficado como o nome de uma função Maxima ou uma função Lisp ou um operador,
uma expressão lambda do Maxima, ou uma expressão geral do Maxima.


O argumentos opcionais são:



**epsabs** — Erro absoluto desejado de aproximação.  O padrão é 1d-10.
**limite** — Tamanho do array interno de trabalho.  (*limite* - *limlst*)/2 é o
número máximo de subintervalos para usar.  O padrão é 200.



*epsabs* e *limit* são o erro relativo
desejado e o número máximo de subintervalos, respectivamente.
*epsrel* o padrão é 1e-8 e *limite* é 200.


`quad_qaws` retorna uma lista de quatro elementos:



- *
uma aproximação para a integral,
- *
o erro absoluto estimado da aproximação,
- *
o número de avaliações do integrando,
- *
um código de erro.


O código de erro (quarto elemento do valor de retorno) pode ter os valores:



**0** — nenhum problema foi encontrado;
**1** — muitos subintervalos foram concluídos;
**2** — erro excessivo é detectado;
**3** — ocorreu um comportamento excessivamente ruim do integrando;
**6** — se a entrada é invalida.


Exemplos:



```maxima
(%i1) quad_qaws (1/(x+1+2^(-4)), x, -1, 1, -0.5, -0.5, 1);
(%o1)     [8.750097361672832, 1.24321522715422E-10, 170, 0]
(%i2) integrate ((1-x*x)^(-1/2)/(x+1+2^(-alpha)), x, -1, 1);
       alpha
Is  4 2      - 1  positive, negative, or zero?

pos;
                          alpha         alpha
                   2 %pi 2      sqrt(2 2      + 1)
(%o2)              -------------------------------
                               alpha
                            4 2      + 2
(%i3) ev (%, alpha=4, numer);
(%o3)                     8.750097361672829
```

<!-- category: Calculus -->
<!-- keywords: residue -->
<!-- signatures: residue(expr, z, z_0) -->
### Function: residue (expr, z, z_0)

Calcula o resíduo no plano complexo da
expressão *expr* quando a variável *z* assumes o valor *z_0*.  O
resíduo é o coeficiente de `(z - z_0)^(-1)` nas séries de Laurent
para *expr*.



```maxima
(%i1) residue (s/(s**2+a**2), s, a*%i);
                                1
(%o1)                           -
                                2
(%i2) residue (sin(a*x)/x**4, x, 0);
                                 3
                                a
(%o2)                         - --
                                6
```

<!-- category: Calculus -->
<!-- keywords: risch -->
<!-- signatures: risch(expr, x) -->
### Function: risch (expr, x)

Integra *expr* em relação a *x* usando um
caso transcendental do algorítmo de Risch.  (O caso algébrico do
algorítmo de Risch foi implementado.)  Isso atualmente
manuseia os casos de exponenciais aninhadas e logarítmos que a parte
principal de `integrate` não pode fazer.  `integrate` irá aplicar automaticamente `risch`
se dados esses casos.


`erfflag`, se `false`, previne `risch` da introdução da função
`erf` na resposta se não for achado nenhum no integrando para 
começar.



```maxima
(%i1) risch (x^2*erf(x), x);
                                                        2
             3                      2                - x
        %pi x  erf(x) + (sqrt(%pi) x  + sqrt(%pi)) %e
(%o1)   -------------------------------------------------
                              3 %pi
(%i2) diff(%, x), ratsimp;
                             2
(%o2)                       x  erf(x)
```

<!-- category: Calculus -->
<!-- keywords: tldefint -->
<!-- signatures: tldefint(expr, x, a, b) -->
### Function: tldefint (expr, x, a, b)

Equivalente a `ldefint` com `tlimswitch` escolhido para `true`.

