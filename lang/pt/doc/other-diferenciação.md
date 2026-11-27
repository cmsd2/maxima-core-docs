## Diferenciação

<!-- category: Other -->
<!-- keywords: antid -->
<!-- signatures: antid(expr, x, u(x)) -->
### Function: antid (expr, x, u(x))

Retorna uma lista de dois elementos,
tais que uma antiderivada de *expr* com relação a *x*
pode ser constuída a partir da lista.
A expressão *expr* pode conter uma função desconhecida *u* e suas derivadas.


Tome *L*, uma lista de dois elementos, como sendo o valor de retorno de `antid`.
Então `L[1] + 'integrate (L[2], x)`
é uma antiderivada de *expr* com relação a *x*.


Quando `antid` obtém sucesso inteiramente,
o segundo elemento do valor de retorno é zero.
De outra forma, o segundo elemento é não zero,
e o primeiro elemento não zero ou zero.
Se `antid` não pode fazer nenhum progresso,
o primeiro elemento é zero e o segundo não zero.


`load ("antid")` chama essa função.
O pacote `antid` também define as funções `nonzeroandfreeof` e `linear`.


`antid` está relacionada a `antidiff` como segue.
Tome *L*, uma lista de dois elementos, que é o valor de retorno de `antid`.
Então o valor de retorno de `antidiff` é igual a `L[1] + 'integrate (L[2], x)`
onde *x* é a variável de integração.


Exemplos:














```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

<!-- category: Other -->
<!-- keywords: antidiff -->
<!-- signatures: antidiff(expr, x, u(x)) -->
### Function: antidiff (expr, x, u(x))

Retorna uma antiderivada de *expr* com relação a *x*.
A expressão *expr* pode conter uma função desconhecida *u* e suas derivadas.


Quando `antidiff` obtém sucesso inteiramente,
a expressão resultante é livre do sinal de integral (isto é, livre do substantivo `integrate`).
De outra forma, `antidiff` retorna uma expressão
que é parcialmente ou inteiramente dentro de um sinal de um sinal de integral.
Se `antidiff` não pode fazer qualquer progresso,
o valor de retorno é inteiramente dentro de um sinal de integral.


`load ("antid")` chama essa função.
O pacote `antid` também define as funções `nonzeroandfreeof` e `linear`.


`antidiff` é relacionada a `antid` como segue.
Tome *L*, uma lista de dois elementos, como sendo o valor de retorno de `antid`.
Então o valor de retorno de `antidiff` é igual a `L[1] + 'integrate (L[2], x)`
onde *x* é a variável de integração.


Exemplos:














```maxima
(%i1) load ("antid")$
(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                            z(x)  d
(%o2)                y(x) %e     (-- (z(x)))
                                  dx
(%i3) a1: antid (expr, x, z(x));
                       z(x)      z(x)  d
(%o3)          [y(x) %e    , - %e     (-- (y(x)))]
                                       dx
(%i4) a2: antidiff (expr, x, z(x));
                            /
                     z(x)   [   z(x)  d
(%o4)         y(x) %e     - I %e     (-- (y(x))) dx
                            ]         dx
                            /
(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0
(%i6) antid (expr, x, y(x));
                             z(x)  d
(%o6)             [0, y(x) %e     (-- (z(x)))]
                                   dx
(%i7) antidiff (expr, x, y(x));
                  /
                  [        z(x)  d
(%o7)             I y(x) %e     (-- (z(x))) dx
                  ]              dx
                  /
```

<!-- category: Other -->
<!-- keywords: atomgrad -->
<!-- signatures: atomgrad -->
### Variable: atomgrad

`atomgrad` é a propriedade do gradiente atomico de uma expressão.
Essa propriedade é atribuída por `gradef`.

<!-- category: Other -->
<!-- keywords: atvalue -->
<!-- signatures: atvalue(expr, [x_1=a_1, ..., x_m=a_m], c), atvalue(expr, x_1=a_1, c) -->
### Function: atvalue (expr, [x_1=a_1, ..., x_m=a_m], c)

Atribui o valor *c* a *expr* no ponto `x = a`.
Tipicamente valores de extremidade são estabelecidos por esse mecanismo.


*expr* é a função de avaliação,
`f(x_1, ..., x_m)`,
ou uma derivada,
`diff (f(x_1, ..., x_m), x_1, n_1, ..., x_n, n_m)`


na qual os argumentos da função explicitamente aparecem.
*n_i* é a ordem de diferenciação com relação a *x_i*.


O ponto no qual o `atvalue` é estabelecido é dado pela lista de equações
`[x_1 = a_1, ..., x_m = a_m]`.
Se existe uma variável simples *x_1*,
uma única equação pode ser dada sem ser contida em uma lista.


`printprops ([f_1, f_2, ...], atvalue)` mostra os `atvalues` das
funções `f_1, f_2, ...`
como especificado por chamadas a `atvalue`.
`printprops (f, atvalue)` mostra os `atvalues` de uma função *f*.
`printprops (all, atvalue)` mostra os `atvalue`s de todas as funções para as quais `atvalue`s são definidos.


Os simbolos `@1`, `@2`, ... representam as 
variáveis *x_1*, *x_2*, ... quando `atvalue`s são mostrados.


`atvalue` avalia seus argumentos.
`atvalue` retorna *c*, o `atvalue`.


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
(%i4) diff (4*f(x,y)^2 - u(x,y)^2, x);
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
<!-- keywords: cartan -->
<!-- signatures: cartan- -->
### Function: cartan (-)

O cálculo exterior de formas diferenciais é uma ferramenta básica
de geometria diferencial desenvolvida por Elie Cartan e tem importantes
aplicações na teoria das equações diferenciais parciais.
O pacote `cartan`
implementa as funções `ext_diff` e `lie_diff`,
juntamente com os operadores `~` (produto da cunha) e `|` (contração
de uma forma com um vector.)
Digite `demo (tensor)` para ver uma breve
descrição desses comandos juntamente com exemplos.


`cartan` foi implementado por F.B. Estabrook e H.D. Wahlquist.

<!-- category: Other -->
<!-- keywords: del -->
<!-- signatures: del(x) -->
### Function: del (x)

`del (x)` representa a diferencial da variável $x$.


`diff` retorna uma expressão contendo `del`
se uma variável independente não for especificada.
Nesse caso, o valor de retorno é a então chamada "diferencial total".


Exemplos:







```maxima
(%i1) diff (log (x));
                             del(x)
(%o1)                        ------
                               x
(%i2) diff (exp (x*y));
                     x y              x y
(%o2)            x %e    del(y) + y %e    del(x)
(%i3) diff (x*y*z);
(%o3)         x y del(z) + x z del(y) + y z del(x)
```

<!-- category: Other -->
<!-- keywords: delta -->
<!-- signatures: delta(t) -->
### Function: delta (t)

A função Delta de Dirac.


Correntemente somente `laplace` sabe sobre a função `delta`.


Exemplo:



```maxima
(%i1) laplace (delta (t - a) * sin(b*t), t, s);
Is  a  positive, negative, or zero?

p;
                                   - a s
(%o1)                   sin(a b) %e
```

<!-- category: Other -->
<!-- keywords: dependencies -->
<!-- signatures: dependencies -->
### Variable: dependencies

Valor por omissão: `[]`


`dependencies` é a lista de átomos que possuem dependências
funcionais, atribuídas por `depends` ou `gradef`.
A lista `dependencies` é cumulativa:
cada chamada a `depends` ou a `gradef` anexa ítens adicionais.


Veja `depends` e `gradef`.

<!-- category: Other -->
<!-- keywords: depends -->
<!-- signatures: depends(f_1, x_1, ..., f_n, x_n) -->
### Function: depends (f_1, x_1, ..., f_n, x_n)

Declara dependêcias funcionais entre variáveis para o propósito de calcular derivadas.
Na ausência de dependêcias declaradas,
`diff (f, x)` retorna zero.
Se `depends (f, x)` for declarada,
`diff (f, x)` retorna uma derivada simbólica (isto é, um substantivo `diff`).


Cada argumento *f_1*, *x_1*, etc., pode ser o nome de uma variável ou array,
ou uma lista de nomes.
Todo elemento de *f_i* (talvez apenas um elemento simples)
é declarado para depender
de todo elemento de *x_i* (talvez apenas um elemento simples).
Se algum *f_i* for o nome de um array ou contém o nome de um array,
todos os elementos do array dependem de *x_i*.


`diff` reconhece dependências indirectas estabelecidas por `depends`
e aplica a regra da cadeia nesses casos.


`remove (f, dependency)` remove todas as dependências declaradas para *f*.


`depends` retorna uma lista de dependências estabelecidas.
As dependências são anexadas à variável global `dependencies`.
`depends` avalia seus argumentos.


`diff` é o único comando Maxima que reconhece dependências estabelecidas por `depends`.
Outras funções (`integrate`, `laplace`, etc.)
somente reconhecem dependências explicitamente representadas por seus argumentos.
Por exemplo, `integrate` não reconhece a dependência de `f` sobre `x`
a menos que explicitamente representada como `integrate (f(x), x)`.









```maxima
(%i1) depends ([f, g], x);
(%o1)                     [f(x), g(x)]
(%i2) depends ([r, s], [u, v, w]);
(%o2)               [r(u, v, w), s(u, v, w)]
(%i3) depends (u, t);
(%o3)                        [u(t)]
(%i4) dependencies;
(%o4)      [f(x), g(x), r(u, v, w), s(u, v, w), u(t)]
(%i5) diff (r.s, u);
                         dr           ds
(%o5)                    -- . s + r . --
                         du           du
```





```maxima
(%i6) diff (r.s, t);
                      dr du           ds du
(%o6)                 -- -- . s + r . -- --
                      du dt           du dt
```






```maxima
(%i7) remove (r, dependency);
(%o7)                         done
(%i8) diff (r.s, t);
                                ds du
(%o8)                       r . -- --
                                du dt
```

<!-- category: Other -->
<!-- keywords: derivabbrev -->
<!-- signatures: derivabbrev -->
### Variable: derivabbrev

Valor por omissão: `false`


Quando `derivabbrev` for `true`,
derivadas simbólicas (isto é, substantivos `diff`) são mostradas como subscritos.
De outra forma, derivadas são mostradas na notação de Leibniz `dy/dx`.

<!-- category: Other -->
<!-- keywords: derivdegree -->
<!-- signatures: derivdegree(expr, y, x) -->
### Function: derivdegree (expr, y, x)

Retorna o maior grau de uma derivada
da variável dependente *y* com relação à variável independente
*x* ocorrendo em *expr*.


Exemplo:





```maxima
(%i1) 'diff (y, x, 2) + 'diff (y, z, 3) + 'diff (y, x) * x^2;
                         3     2
                        d y   d y    2 dy
(%o1)                   --- + --- + x  --
                          3     2      dx
                        dz    dx
(%i2) derivdegree (%, y, x);
(%o2)                           2
```

<!-- category: Other -->
<!-- keywords: derivlist -->
<!-- signatures: derivlist(var_1, ..., var_k) -->
### Function: derivlist (var_1, ..., var_k)

Causa somente diferenciações com relação às
variáveis indicadas, dentro do comando `ev`.

<!-- category: Other -->
<!-- keywords: derivsubst -->
<!-- signatures: derivsubst -->
### Variable: derivsubst

Valor por omissão: `false`


Quando `derivsubst` for `true`, uma substiruíção não sintática tais como
`subst (x, 'diff (y, t), 'diff (y, t, 2))` retorna `'diff (x, t)`.

<!-- category: Other -->
<!-- keywords: diff -->
<!-- signatures: diff(expr, x_1, n_1, ..., x_m, n_m), diff(expr, x, n), diff(expr, x), diff(expr) -->
### Function: diff (expr, x_1, n_1, ..., x_m, n_m)

Retorna uma derivada ou diferencial de *expr* com relação a alguma ou todas as variáveis em *expr*.


`diff (expr, x, n)` retorna a *n*’ésima derivada de *expr*
com relação a *x*.


`diff (expr, x_1, n_1, ..., x_m, n_m)`
retorna a derivada parcial mista de *expr* com relação a *x_1*, ..., *x_m*.
Isso é equivalente a `diff (... (diff (expr, x_m, n_m) ...), x_1, n_1)`.


`diff (expr, x)`
retorna a primeira derivada de *expr* com relação a
uma variável *x*.


`diff (expr)` retorna a diferencial total de *expr*,
isto é, a soma das derivadas de *expr* com relação a cada uma de suas variáveis
vezes a diferencial `del` de cada variável.

Nenhuma simplificação adicional de `del` é oferecida.


A forma substantiva de `diff` é requerida em alguns contextos,
tal como declarando uma equação diferencial.
Nesses casos, `diff` pode ser colocado apóstrofo (com `'diff`) para retornar a forma substantiva
em lugar da realização da diferenciação.


Quando `derivabbrev` for `true`, derivadas são mostradas como subscritos.
De outra forma, derivadas são mostradas na notação de Leibniz, `dy/dx`.


Exemplos:








```maxima
(%i1) diff (exp (f(x)), x, 2);
                     2
              f(x)  d               f(x)  d         2
(%o1)       %e     (--- (f(x))) + %e     (-- (f(x)))
                      2                   dx
                    dx
(%i2) derivabbrev: true$
(%i3) 'integrate (f(x, y), y, g(x), h(x));
                         h(x)
                        /
                        [
(%o3)                   I     f(x, y) dy
                        ]
                        /
                         g(x)
(%i4) diff (%, x);
       h(x)
      /
      [
(%o4) I     f(x, y)  dy + f(x, h(x)) h(x)  - f(x, g(x)) g(x)
      ]            x                     x                  x
      /
       g(x)
```


Para o pacote tensor, as seguintes modificações foram
incorporadas:


(1) As derivadas de quaisquer objectos indexados em *expr* terão as
variáveis *x_i* anexadas como argumentos adicionais.  Então todos os
índices de derivada serão ordenados.


(2) As variáveis *x_i* podem ser inteiros de 1 até o valor de uma variável
`dimension` [valor padrão: 4].  Isso fará com que a diferenciação
seja concluída com relação aos *x_i*’ésimos membros da lista `coordinates` que
pode ser escolhida para uma lista de nomes de coordenadas, e.g.,
`[x, y, z, t]`. Se `coordinates` for associada a uma variável atomica, então aquela
variável subscrita por *x_i* será usada para uma variável de
diferenciação.  Isso permite um array de nomes de coordenadas ou
nomes subscritos como `X[1]`, `X[2]`, ... sejam usados.  Se `coordinates` não
foram atribuídas um valor, então as variáveis seram tratadas como em (1)
acima.

<!-- category: Other -->
<!-- keywords: dscalar -->
<!-- signatures: dscalar(f) -->
### Function: dscalar (f)

Aplica o d’Alembertiano escalar para a função escalar *f*.




`load ("ctensor")` chama essa função.

<!-- category: Other -->
<!-- keywords: express -->
<!-- signatures: express(expr) -->
### Function: express (expr)

Expande o substantivo do operador diferencial em expressões em termos de derivadas parciais.
`express` reconhece os operadores `grad`, `div`, `curl`, `laplacian`.
`express` também expande o produto do X `~`.


Derivadas simbólicas (isto é, substantivos `diff`)
no valor de retorno de `express` podem ser avaliadas incluíndo `diff`
na chamada à função `ev` ou na linha de comando.
Nesse contexto, `diff` age como uma `evfun`.


`load ("vect")` chama essa função.



Exemplos:



















```maxima
(%i1) load ("vect")$
(%i2) grad (x^2 + y^2 + z^2);
                              2    2    2
(%o2)                  grad (z  + y  + x )
(%i3) express (%);
       d    2    2    2   d    2    2    2   d    2    2    2
(%o3) [-- (z  + y  + x ), -- (z  + y  + x ), -- (z  + y  + x )]
       dx                 dy                 dz
(%i4) ev (%, diff);
(%o4)                    [2 x, 2 y, 2 z]
(%i5) div ([x^2, y^2, z^2]);
                              2   2   2
(%o5)                   div [x , y , z ]
(%i6) express (%);
                   d    2    d    2    d    2
(%o6)              -- (z ) + -- (y ) + -- (x )
                   dz        dy        dx
(%i7) ev (%, diff);
(%o7)                    2 z + 2 y + 2 x
(%i8) curl ([x^2, y^2, z^2]);
                               2   2   2
(%o8)                   curl [x , y , z ]
(%i9) express (%);
       d    2    d    2   d    2    d    2   d    2    d    2
(%o9) [-- (z ) - -- (y ), -- (x ) - -- (z ), -- (y ) - -- (x )]
       dy        dz       dz        dx       dx        dy
(%i10) ev (%, diff);
(%o10)                      [0, 0, 0]
(%i11) laplacian (x^2 * y^2 * z^2);
                                  2  2  2
(%o11)                laplacian (x  y  z )
(%i12) express (%);
         2                2                2
        d     2  2  2    d     2  2  2    d     2  2  2
(%o12)  --- (x  y  z ) + --- (x  y  z ) + --- (x  y  z )
          2                2                2
        dz               dy               dx
(%i13) ev (%, diff);
                      2  2      2  2      2  2
(%o13)             2 y  z  + 2 x  z  + 2 x  y
(%i14) [a, b, c] ~ [x, y, z];
(%o14)                [a, b, c] ~ [x, y, z]
(%i15) express (%);
(%o15)          [b z - c y, c x - a z, a y - b x]
```

<!-- category: Other -->
<!-- keywords: gradef -->
<!-- signatures: gradef(f(x_1, ..., x_n), g_1, ..., g_m), gradef(a, x, expr) -->
### Function: gradef (f(x_1, ..., x_n), g_1, ..., g_m)

Define as derivadas parciais (i.e., os componentes do gradiente) da função *f*
ou variável *a*.


`gradef (f(x_1, ..., x_n), g_1, ..., g_m)`
define `df/dx_i` como *g_i*, 
onde *g_i* é uma expressão; *g_i* pode ser uma chamada de função, mas não o nome de uma função.
O número de derivadas parciais *m* pode ser menor que o número de argumentos *n*,
nesses casos derivadas são definidas com relação a *x_1* até *x_m* somente.


`gradef (a, x, expr)` define uma derivada de variável *a*
com relação a *x* como *expr*.
Isso também estabelece a dependência de *a* sobre *x* (via `depends (a, x)`).


O primeiro argumento `f(x_1, ..., x_n)` ou *a* é acompanhado de apóstrofo,
mas os argumentos restantes *g_1*, ..., *g_m* são avaliados.
`gradef` retorna a função ou variável para as quais as derivadas parciais são definidas.


`gradef` pode redefinir as derivadas de funções internas do Maxima.
Por exemplo, `gradef (sin(x), sqrt (1 - sin(x)^2))` redefine uma derivada de `sin`.


`gradef` não pode definir derivadas parciais para um função subscrita.


`printprops ([f_1, ..., f_n], gradef)` mostra as derivadas parciais
das funções *f_1*, ..., *f_n*, como definidas por `gradef`.


`printprops ([a_n, ..., a_n], atomgrad)` mostra as derivadas parciais
das variáveis *a_n*, ..., *a_n*, como definidas por `gradef`.


`gradefs` é a lista de funções
para as quais derivadas parciais foram definidas por `gradef`.
`gradefs` não inclui quaisquer variáveis
para quais derivadas parciais foram definidas por `gradef`.



Gradientes são necessários quando, por exemplo, uma função não é conhecida
explicitamente mas suas derivadas primeiras são e isso é desejado para obter
derivadas de ordem superior.

<!-- category: Other -->
<!-- keywords: gradefs -->
<!-- signatures: gradefs -->
### Variable: gradefs

Valor por omissão: `[]`


`gradefs` é a lista de funções
para as quais derivadas parciais foram definidas por `gradef`.
`gradefs` não inclui quaisquer variáveis
para as quais derivadas parciais foram deinidas por `gradef`.

<!-- category: Other -->
<!-- keywords: laplace -->
<!-- signatures: laplace(expr, t, s) -->
### Function: laplace (expr, t, s)

Tenta calcular a transformada de Laplace de *expr* com relação a uma variável *t*
e parâmetro de transformação *s*.
Se `laplace` não pode achar uma solução, um substantivo `'laplace` é retornado.


`laplace` reconhece em *expr* as funções
`delta`, `exp`, `log`, `sin`, `cos`, `sinh`, `cosh`, e `erf`,
também `derivative`, `integrate`, `sum`, e `ilt`.
Se algumas outras funções estiverem presente,
`laplace` pode não ser habilitada a calcular a tranformada.



*expr* pode também ser uma equação linear, diferencial de coeficiente contante no
qual caso o `atvalue` da variável dependente é usado.

O requerido `atvalue` pode ser fornecido ou antes ou depois da transformada ser calculada.
Uma vez que as condições iniciais devem ser especificadas em zero, se um teve condições
de limite impostas em qualquer outro lugar ele pode impor essas sobre a solução
geral e eliminar as constantes resolvendo a solução geral
para essas e substituindo seus valores de volta.


`laplace` reconhece integrais de convolução da forma
`integrate (f(x) * g(t - x), x, 0, t)`;
outros tipos de convoluções não são reconhecidos.


Relações funcionais devem ser explicitamente representadas em *expr*;
relações implícitas, estabelecidas por `depends`, não são reconhecidas.
Isto é, se *f* depende de *x* e *y*,
`f (x, y)` deve aparecer em *expr*.


Veja também `ilt`, a transformada inversa de Laplace.


Exemplos:








```maxima
(%i1) laplace (exp (2*t + a) * sin(t) * t, t, s);
                            a
                          %e  (2 s - 4)
(%o1)                    ---------------
                           2           2
                         (s  - 4 s + 5)
(%i2) laplace ('diff (f (x), x), x, s);
(%o2)             s laplace(f(x), x, s) - f(0)
(%i3) diff (diff (delta (t), t), t);
                          2
                         d
(%o3)                    --- (delta(t))
                           2
                         dt
(%i4) laplace (%, t, s);
                            !
               d            !         2
(%o4)        - -- (delta(t))!      + s  - delta(0) s
               dt           !
                            !t = 0
```

