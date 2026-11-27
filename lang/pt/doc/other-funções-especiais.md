## Funções Especiais

<!-- category: Other -->
<!-- keywords: airy_ai -->
<!-- signatures: airy_ai(x) -->
### Function: airy_ai (x)

A função de Airy Ai, como definida em Abramowitz e Stegun,
*Handbook of Mathematical Functions*, Sessão 10.4. 


A equação de Airy `diff (y(x), x, 2) - x y(x) = 0` tem duas 
soluções linearmente independentes, `y = Ai(x)` e `y = Bi(x)`.
A derivada de `diff (airy_ai(x), x)` é `airy_dai(x)`.


Se o argumento `x` for um número real ou um número complexo qualquer deles em ponto
flutuante , o valor numérico de `airy_ai` é retornado 
quando possível.


Veja também `airy_bi`, `airy_dai`, `airy_dbi`.

<!-- category: Other -->
<!-- keywords: airy_bi -->
<!-- signatures: airy_bi(x) -->
### Function: airy_bi (x)

A função de Airy Bi, como definida em Abramowitz e Stegun,
*Handbook of Mathematical Functions*, Sessão 10.4, 
é a segunda solução da equação de Airy
`diff (y(x), x, 2) - x y(x) = 0`.


Se o argumento `x` for um número real ou um número complexo qualquer deles em ponto flutuante,
o valor numérico de `airy_bi` é retornado quando possível.
Em outros casos a expressão não avaliada é retornada.


A derivada de `diff (airy_bi(x), x)` é `airy_dbi(x)`.


Veja `airy_ai`, `airy_dbi`.

<!-- category: Other -->
<!-- keywords: airy_dai -->
<!-- signatures: airy_dai(x) -->
### Function: airy_dai (x)

A derivada da função de Airy Ai `airy_ai(x)`. 


Veja `airy_ai`.

<!-- category: Other -->
<!-- keywords: airy_dbi -->
<!-- signatures: airy_dbi(x) -->
### Function: airy_dbi (x)

A derivada de função de Airy Bi `airy_bi(x)`.


Veja `airy_ai` e `airy_bi`.

<!-- category: Other -->
<!-- keywords: asympa -->
<!-- signatures: asympa -->
### Function: asympa

`asympa` é um pacote para análise assintótica. O pacote contém
funções de simplificação para análise assintótica, incluindo as funções 
“grande O” e “pequeno o” que são largamente usadas em análises de complexidade e
análise numérica.


`load ("asympa")` chama esse pacote.

<!-- category: Other -->
<!-- keywords: bessel -->
<!-- signatures: bessel(z, a) -->
### Function: bessel (z, a)

A função de Bessel de primeiro tipo.


Essa função está desactualizada.  Escreva `bessel_j (z, a)` em lugar dessa.

<!-- category: Other -->
<!-- keywords: bessel_i -->
<!-- signatures: bessel_i(v, z) -->
### Function: bessel_i (v, z)

A função de Bessel modificada de primeiro tipo de ordem $v$ e argumento $z$.


`bessel_i` calcula o array `besselarray` tal que
`besselarray [i] = bessel_i [i + v - int(v)] (z)` para `i` de zero a `int(v)`.


`bessel_i` é definida como



$$
\sum_{k=0}^{\infty } {{1\over{k!\,\Gamma
 \left(v+k+1\right)}} {\left(z\over 2\right)^{v+2\,k}}}
$$


todavia séries infinitas não são usadas nos cálculos.

<!-- category: Other -->
<!-- keywords: bessel_j -->
<!-- signatures: bessel_j(v, z) -->
### Function: bessel_j (v, z)

A função de Bessel do primeiro tipo de ordem $v$ e argumento $z$.


`bessel_j` calcula o array `besselarray` tal que
`besselarray [i] = bessel_j [i + v - int(v)] (z)` para `i` de zero a `int(v)`.


`bessel_j` é definida como



$$
\sum_{k=0}^{\infty }{{{\left(-1\right)^{k}\,\left(z\over 2\right)^{v+2\,k}
 }\over{k!\,\Gamma\left(v+k+1\right)}}}
$$


todavia séries infinitas não são usadas nos cálculos.

<!-- category: Other -->
<!-- keywords: bessel_k -->
<!-- signatures: bessel_k(v, z) -->
### Function: bessel_k (v, z)

A função de Bessel modificada de segundo tipo de ordem $v$ e argumento $z$.


`bessel_k` calcula o array `besselarray` tal que
`besselarray [i] = bessel_k [i + v - int(v)] (z)` para `i` de zero a `int(v)`.


`bessel_k` é definida como

$$
{{\pi\,\csc \left(\pi\,v\right)\,\left(I_{-v}(z)-I_{v}(z)\right)}\over{2}}
$$



quando $v$ não for inteiro.  Se $v$ for um inteiro $n$,
então o limite  com $v$ aproximando-se de $n$ é tomado.

<!-- category: Other -->
<!-- keywords: bessel_y -->
<!-- signatures: bessel_y(v, z) -->
### Function: bessel_y (v, z)

A função de Bessel do segundo tipo de ordem $v$ e argumento $z$.


`bessel_y` calcula o array `besselarray` tal que
`besselarray [i] = bessel_y [i + v - int(v)] (z)` para `i` de zero a `int(v)`.


`bessel_y` é definida como



$$
{{\cos \left(\pi\,v\right)\,J_{v}(z)-J_{-v}(z)}\over{
 \sin \left(\pi\,v\right)}}
$$


quando $v$ não for um inteiro.  Quando $v$ for um inteiro $n$,
o limite com $v$ aprocimando-se de $n$ é tomado.

<!-- category: Other -->
<!-- keywords: besselexpand -->
<!-- signatures: besselexpand -->
### Variable: besselexpand

Valor por omissão: `false`



Expansões de controle de funções de Bessel quando a ordem for a metade de
um inteiro ímpar.  Nesse caso, as funções de Bessel podem ser expandidas
em termos de outras funções elementares.  Quando `besselexpand` for `true`,
a função de Bessel é expandida.



```maxima
(%i1) besselexpand: false$
(%i2) bessel_j (3/2, z);
                                    3
(%o2)                      bessel_j(-, z)
                                    2
(%i3) besselexpand: true$
(%i4) bessel_j (3/2, z);
                          2 z   sin(z)   cos(z)
(%o4)                sqrt(---) (------ - ------)
                          %pi      2       z
                                  z
```

<!-- category: Other -->
<!-- keywords: beta -->
<!-- signatures: beta(x, y) -->
### Function: beta (x, y)

A função beta, definida como `gamma(x) gamma(y)/gamma(x + y)`.

<!-- category: Other -->
<!-- keywords: gamma -->
<!-- signatures: gamma(x) -->
### Function: gamma (x)

A função gama.






Veja também `makegamma`.


A variável `gammalim` controla a simplificação da função gama.


A constante de Euler-Mascheroni é `%gamma`.

<!-- category: Other -->
<!-- keywords: gammalim -->
<!-- signatures: gammalim -->
### Variable: gammalim

Valor por omissão: 1000000



`gammalim` controla a simplificação da função
gama para integral e argumentos na forma de números racionais.  Se o valor
absoluto do argumento não for maior que `gammalim`, então
a simplificação ocorrerá.  Note que `factlim` comuta controle de
simplificaçcão do resultado de `gamma` de um argumento inteiro também.

<!-- category: Other -->
<!-- keywords: intopois -->
<!-- signatures: intopois(a) -->
### Function: intopois (a)

Converte *a* em um código de Poisson.

<!-- category: Other -->
<!-- keywords: makefact -->
<!-- signatures: makefact(expr) -->
### Function: makefact (expr)

Transforma instâncias de funções binomiais, gama,
e beta em *expr* para factoriais.


Veja também `makegamma`.

<!-- category: Other -->
<!-- keywords: makegamma -->
<!-- signatures: makegamma(expr) -->
### Function: makegamma (expr)

Transforma instâncias de funções binomiais, factorial,
e beta em *expr* para funções gama.


Veja também `makefact`.

<!-- category: Other -->
<!-- keywords: maxpsifracdenom -->
<!-- signatures: maxpsifracdenom -->
### Variable: maxpsifracdenom

Valor por omissão: 4


Tomemos *x* como sendo um número racional menor que a unidade e da forma `p/q`.
Se `q` for maior que `maxpsifracdeonm`, então
`psi[n](x)` não irá tentar retornar um valor
simplificado.

<!-- category: Other -->
<!-- keywords: maxpsifracnum -->
<!-- signatures: maxpsifracnum -->
### Variable: maxpsifracnum

Valor por omissão: 4


Tomemos *x* como sendo um número racional menor que a unidade e da forma `p/q`.
Se `p` for menor que `maxpsifracnum`, então
`psi[n](x)` não irá tentar retornar um valor
simplificado.

<!-- category: Other -->
<!-- keywords: maxpsinegint -->
<!-- signatures: maxpsinegint -->
### Variable: maxpsinegint

Valor por omissão: -10


`maxpsinegint` é o valor mais negativo para o qual
`psi[n](x)` irá tentar calcular um valor exato.  Isto é, se
*x* for menor que `maxnegint`, `psi[n](x)` não irá
retornar resposta simplificada, mesmo se isso for possível.

<!-- category: Other -->
<!-- keywords: maxpsiposint -->
<!-- signatures: maxpsiposint -->
### Variable: maxpsiposint

Valor por omissão: 20


`maxpsiposint` é o maior valor positivo para o qual
`psi[n](x)` irá tentar calcular um valor exato.

<!-- category: Other -->
<!-- keywords: numfactor -->
<!-- signatures: numfactor(expr) -->
### Function: numfactor (expr)

Retorna o factor numérico multiplicando a expressão
*expr*, que pode ser um termo simples.



`content` retorna o máximo divisor comum (mdc) de todos os termos em uma adição.



```maxima
(%i1) gamma (7/2);
                          15 sqrt(%pi)
(%o1)                     ------------
                               8
(%i2) numfactor (%);
                               15
(%o2)                          --
                               8
```

<!-- category: Other -->
<!-- keywords: outofpois -->
<!-- signatures: outofpois(a) -->
### Function: outofpois (a)

Converte *a* de um código de Poisson para uma representação
geral.  Se *a* não for uma forma de Poisson, `outofpois` realiza a conversão,
i.e., o valor de retorno é `outofpois (intopois (a))`.
Essa função é desse modo um simplificador canónico
para adições e potências de termos de seno e co-seno de um tipo particular.

<!-- category: Other -->
<!-- keywords: poisdiff -->
<!-- signatures: poisdiff(a, b) -->
### Function: poisdiff (a, b)

Deriva *a* com relação a *b*.  *b* deve ocorrer somente
nos argumentos trigonométricos ou somente nos coeficientes.

<!-- category: Other -->
<!-- keywords: poisexpt -->
<!-- signatures: poisexpt(a, b) -->
### Function: poisexpt (a, b)

Funcionalmente identica a `intopois (a^b)`.
*b* deve ser um inteiro positico.

<!-- category: Other -->
<!-- keywords: poisint -->
<!-- signatures: poisint(a, b) -->
### Function: poisint (a, b)

Integra em um senso restrito similarmente (para
`poisdiff`).  Termos não periódicos em *b* são diminuídos se *b* estiver em argumentos
trigonométricos.

<!-- category: Other -->
<!-- keywords: poislim -->
<!-- signatures: poislim -->
### Variable: poislim

Valor por omissão: 5


`poislim` determina o domínio dos coeficientes nos
argumentos de funções trigonométricas.  O valor inicial de 5
corresponde ao intervalo [-2^(5-1)+1,2^(5-1)], ou [-15,16], mas isso
pode ser alterado para [-2^(n-1)+1, 2^(n-1)].

<!-- category: Other -->
<!-- keywords: poismap -->
<!-- signatures: poismap(series, sinfn, cosfn) -->
### Function: poismap (series, sinfn, cosfn)

mapeará as funções *sinfn* sobre os
termos de seno e *cosfn* ssobre os termos de co-seno das séries de Poisson dadas.
*sinfn* e *cosfn* são funções de dois argumentos que são um coeficiente
e uma parte trigonométrica de um termo em séries respectivamente.

<!-- category: Other -->
<!-- keywords: poisplus -->
<!-- signatures: poisplus(a, b) -->
### Function: poisplus (a, b)

É funcionalmente identica a `intopois (a + b)`.

<!-- category: Other -->
<!-- keywords: poissimp -->
<!-- signatures: poissimp(a) -->
### Function: poissimp (a)

Converte *a* em séries de Poisson para *a* em representação
geral.

<!-- category: Other -->
<!-- keywords: poisson -->
<!-- signatures: poisson -->
### Variable: poisson

O símbolo `/P/` segue o rótulo de linha de uma expressão contendo séries de
Poisson.

<!-- category: Other -->
<!-- keywords: poissubst -->
<!-- signatures: poissubst(a, b, c) -->
### Function: poissubst (a, b, c)

Substitue *a* por *b* em *c*.  *c* é uma série de Poisson.


(1) Quando *B* é uma variável *u*, *v*, *w*, *x*, *y*, ou *z*,
então *a* deve ser uma
expressão linear nessas variáveis (e.g., `6*u + 4*v`).


(2) Quando *b* for outra que não essas variáveis, então *a* deve também ser
livre dessas variáveis, e além disso, livre de senos ou co-senos.


`poissubst (a, b, c, d, n)` é um tipo especial d substituição que
opera sobre *a* e *b* como no tipo (1) acima, mas onde *d* é uma série de
Poisson, expande `cos(d)` e `sin(d)` para a ordem *n* como provendo o
resultado da substituição `a + d` por *b* em *c*.  A idéia é que *d* é uma
expansão em termos de um pequeno parâmetro.  Por exemplo,
`poissubst (u, v, cos(v), %e, 3)` retorna `cos(u)*(1 - %e^2/2) - sin(u)*(%e - %e^3/6)`.

<!-- category: Other -->
<!-- keywords: poistimes -->
<!-- signatures: poistimes(a, b) -->
### Function: poistimes (a, b)

É funcionalmente idêntica a `intopois (a*b)`.

<!-- category: Other -->
<!-- keywords: poistrim -->
<!-- signatures: poistrim() -->
### Function: poistrim ()

é um nome de função reservado que (se o utilizador tiver definido
uma função com esse nome) é aplicada durante multiplicação de Poisson.  Isso é uma função
predicada de 6 argumentos que são os coeficientes de *u*, *v*, ..., *z*
em um termo.  Termos para os quais `poistrim` for `true` (para os coeficientes
daquele termo) são eliminados durante a multiplicação.

<!-- category: Other -->
<!-- keywords: printpois -->
<!-- signatures: printpois(a) -->
### Function: printpois (a)

Mostra uma série de Poisson em um formato legível.  Em comum
com `outofpois`, essa função converterá *a* em um código de Poisson primeiro, se
necessário.

<!-- category: Other -->
<!-- keywords: psi -->
<!-- signatures: psi[n](x) -->
### Function: psi ([n](x))

A derivada de `log (gamma (x))` de ordem `n+1`.
Dessa forma, `psi[0](x)` é a primeira derivada,
`psi[1](x)` é a segunda derivada, etc.


Maxima não sabe como, em geral, calcular um valor numérico de
`psi`, mas Maxima pode calcular alguns valores exatos para argumentos racionais.
Muitas variáveis controlam qual intervalo de argumentos racionais `psi` irá
retornar um valor exato, se possível.  Veja `maxpsiposint`,
`maxpsinegint`, `maxpsifracnum`, e `maxpsifracdenom`.
Isto é, *x* deve localizar-se entre `maxpsinegint` e
`maxpsiposint`.  Se o valor absoluto da parte facionária de
*x* for racional e tiver um numerador menor que `maxpsifracnum`
e tiver um denominador menor que `maxpsifracdenom`, `psi`
irá retornar um valor exato.


A função `bfpsi` no pacote `bffac` pode calcular
valores numéricos.

<!-- category: Other -->
<!-- keywords: scaled_bessel_i -->
<!-- signatures: scaled_bessel_i(v, z) -->
### Function: scaled_bessel_i (v, z)

A função homotética modificada de Bessel de primeiro tipo de ordem
$v$ e argumento $z$.  Isto é, $scaled_bessel_i(v,z) = exp(-abs(z))*bessel_i(v, z)$. Essa função é particularmente útil
para calcular $bessel_i$ para grandes valores de $z$.
Todavia, maxima não conhece outra forma muito mais sobre essa função.  Para
computação simbólica, é provavelmete preferível trabalhar com a expressão
`exp(-abs(z))*bessel_i(v, z)`.

<!-- category: Other -->
<!-- keywords: scaled_bessel_i0 -->
<!-- signatures: scaled_bessel_i0(z) -->
### Function: scaled_bessel_i0 (z)

Idêntica a `scaled_bessel_i(0,z)`.

<!-- category: Other -->
<!-- keywords: scaled_bessel_i1 -->
<!-- signatures: scaled_bessel_i1(z) -->
### Function: scaled_bessel_i1 (z)

Idêntica a `scaled_bessel_i(1,z)`.

<!-- category: Other -->
<!-- keywords: specint -->
<!-- signatures: specint(exp(-s*t)*expr, t) -->
### Function: specint (exp(-s*t)*expr, t)

Calcula a transformada de Laplace de *expr* com ralação à variável *t*.
O integrando *expr* pode conter funções especiais.


Se `specint` não puder calcular a integral, o valore de retorno pode
conter vários símbolos do Lisp, incluindo
`other-defint-to-follow-negtest`,
`other-lt-exponential-to-follow`,
`product-of-y-with-nofract-indices`, etc.; isso é um erro.  



`demo(hypgeo)` mostra muitos exemplos de transformadas de Laplace calculados por `specint`.


Exemplos:








```maxima
(%i1) assume (p > 0, a > 0);
(%o1)                    [p > 0, a > 0]
(%i2) specint (t^(1/2) * exp(-a*t/4) * exp(-p*t), t);
                           sqrt(%pi)
(%o2)                     ------------
                                 a 3/2
                          2 (p + -)
                                 4
(%i3) specint (t^(1/2) * bessel_j(1, 2 * a^(1/2) * t^(1/2)) * exp(-p*t), t);
                                   - a/p
                         sqrt(a) %e
(%o3)                    ---------------
                                2
                               p
```

