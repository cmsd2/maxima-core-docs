## romberg

<!-- category: Calculus -->
<!-- keywords: romberg -->
<!-- signatures: romberg(expr, x, a, b), romberg(F, a, b) -->
### Function: romberg (expr, x, a, b)

Calcula uma integração numérica pelo método de Romberg.


`romberg(expr, x, a, b)`
retorna uma estimativa da integral `integrate(expr, x, a, b)`.
*expr* deve ser uma expressão que avalie para um valor em ponto flutuante
quando *x* estiver associado a um valor em ponto flutuante.


`romberg(F, a, b)`
retorna uma estimativa da integral `integrate(F(x), x, a, b)`
onde `x` representa o não nomeado, isolado argumeno de *F*;
o atual argumento não é chamado `x`.
*F* deve ser uma função do Maxima ou do Lisp que retorne um valor em ponto flutuante
quando o argumento for um número em ponto flutuante.
*F* pode nomear uma função traduzida ou compilada do Maxima.


A precisão de `romberg` é governada pelas variáveis globais
`rombergabs` e `rombergtol`.
`romberg` termina com sucesso quando
a diferença absoluta entre duas aproximações sucessivas for menor que `rombergabs`,
ou a diferença relativa em aproximações sucessivas for menor que `rombergtol`.
Dessa forma quando `rombergabs` for 0.0 (o padrão)
somente o erro relativo tem algum efeito sobre `romberg`.


`romberg` divide ao meio o tamanho do passo no máximo `rombergit` vezes antes de interromper;
o número máximo de avaliações de função é portanto `2^rombergit`.
Se o critério de erro estabelecido por `rombergabs` e por `rombergtol`
não for satisfeito, `romberg` mostra uma mensagem de erro.
`romberg` sempre faz ao menos `rombergmin` iterações;
isso é uma intenção eurísstica de previnir encerramentos espúrios quando o integrando for oscilatório.


`romberg` repetidamente avalia o integrando após associar a variável
de integração a um valor específico (e não antes).
Essa política de avaliação torna possível aninhar chamadas a `romberg`,
para calcular integrais multidimensionais.
Todavia, os cálculos de erro não tomam os erros de integrações aninhadas
em consideração, então erros podem ser subestimados.
Também, métodos imaginados especialmente para problemas multidimensionais podem retornar
a mesma precisão com poucas avaliações de função.


`load("romberg")` torna essa função disponível para uso.


Veja também `QUADPACK`, uma coleção de funções de integração numérica.


Exemplos:


Uma integração unidimensonal.












```maxima
(%i1) load ("romberg");
(%o1)    /usr/share/maxima/5.11.0/share/numeric/romberg.lisp
(%i2) f(x) := 1/((x - 1)^2 + 1/100) + 1/((x - 2)^2 + 1/1000) + 1/((x - 3)^2 + 1/200);
                    1                 1                1
(%o2) f(x) := -------------- + --------------- + --------------
                     2    1           2    1            2    1
              (x - 1)  + ---   (x - 2)  + ----   (x - 3)  + ---
                         100              1000              200
(%i3) rombergtol : 1e-6;
(%o3)                 9.9999999999999995E-7
(%i4) rombergit : 15;
(%o4)                          15
(%i5) estimate : romberg (f(x), x, -5, 5);
(%o5)                   173.6730736617464
(%i6) exact : integrate (f(x), x, -5, 5);
(%o6) 10 sqrt(10) atan(70 sqrt(10))
 + 10 sqrt(10) atan(30 sqrt(10)) + 10 sqrt(2) atan(80 sqrt(2))
 + 10 sqrt(2) atan(20 sqrt(2)) + 10 atan(60) + 10 atan(40)
(%i7) abs (estimate - exact) / exact, numer;
(%o7)                7.5527060865060088E-11
```


Uma integração bidimensional, implementada com chamadas aninhadas a `romberg`.













```maxima
(%i1) load ("romberg");
(%o1)    /usr/share/maxima/5.11.0/share/numeric/romberg.lisp
(%i2) g(x, y) := x*y / (x + y);
                                    x y
(%o2)                   g(x, y) := -----
                                   x + y
(%i3) rombergtol : 1e-6;
(%o3)                 9.9999999999999995E-7
(%i4) estimate : romberg (romberg (g(x, y), y, 0, x/2), x, 1, 3);
(%o4)                   0.81930239628356
(%i5) assume (x > 0);
(%o5)                        [x > 0]
(%i6) integrate (integrate (g(x, y), y, 0, x/2), x, 1, 3);
                                          3
                                    2 log(-) - 1
                    9                     2        9
(%o6)       - 9 log(-) + 9 log(3) + ------------ + -
                    2                    6         2
(%i7) exact : radcan (%);
                    26 log(3) - 26 log(2) - 13
(%o7)             - --------------------------
                                3
(%i8) abs (estimate - exact) / exact, numer;
(%o8)                1.3711979871851024E-10
```

<!-- category: Calculus -->
<!-- keywords: rombergabs -->
<!-- signatures: rombergabs -->
### Variable: rombergabs

Valor padrão: 0.0


A precisão de `romberg` é governada pelas variávies globais
`rombergabs` e `rombergtol`.
`romberg` termina com sucesso quando
a diferença absoluta entre duas aproximações sucessivas for menor que `rombergabs`,
ou a diferença relativa em aproximações sucessivas for menor que `rombergtol`.
Dessa forma quando `rombergabs` for 0.0 (o padrão)
somente o erro relativo tem algum efeito sobre `romberg`.


Veja também `rombergit` e `rombergmin`.

<!-- category: Calculus -->
<!-- keywords: rombergit -->
<!-- signatures: rombergit -->
### Variable: rombergit

Valor padrão: 11


`romberg` divide ao meio o tamanho do passo no máximo `rombergit` vezes antes de interromper;
o número máximo de avaliações de função é portanto `2^rombergit`.
`romberg` sempre faz ao menos `rombergmin` iterações;
isso é uma intenção eurísstica de previnir encerramentos espúrios quando o integrando for oscilatório.


Veja também `rombergabs` e `rombergtol`.

<!-- category: Calculus -->
<!-- keywords: rombergmin -->
<!-- signatures: rombergmin -->
### Variable: rombergmin

Valor padrão: 0


`romberg` sempre faz ao menos `rombergmin` iterações;
isso é uma intenção eurísstica para prevenir terminações espúrias quando o integrando for.


Veja também `rombergit`, `rombergabs`, e `rombergtol`.

<!-- category: Calculus -->
<!-- keywords: rombergtol -->
<!-- signatures: rombergtol -->
### Variable: rombergtol

Valor padrão: 1e-4


A precisão de `romberg` é governada pelas variáveis globais
`rombergabs` e `rombergtol`.
`romberg` termina com sucesso quando
a diferença absoluta entre duas aproximações sucessivas for menor que `rombergabs`,
ou a diferença relativa em aproximações sucessivas for menor que `rombergtol`.
Dessa forma quando `rombergabs` for 0.0 (o padrão)
somente o erro relativo tem algum efeito sobre `romberg`.


Veja também `rombergit` e `rombergmin`.

