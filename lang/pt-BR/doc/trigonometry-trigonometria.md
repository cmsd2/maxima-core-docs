## Trigonometria

<!-- category: Trigonometry -->
<!-- keywords: acos -->
<!-- signatures: acos(x) -->
### Function: acos (x)

- Arco Cosseno.

<!-- category: Trigonometry -->
<!-- keywords: acosh -->
<!-- signatures: acosh(x) -->
### Function: acosh (x)

- Arco Cosseno Hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: acot -->
<!-- signatures: acot(x) -->
### Function: acot (x)

- Arco Cotangente.

<!-- category: Trigonometry -->
<!-- keywords: acoth -->
<!-- signatures: acoth(x) -->
### Function: acoth (x)

- Arco Cotangente Hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: acsc -->
<!-- signatures: acsc(x) -->
### Function: acsc (x)

- Arco Cossecante.

<!-- category: Trigonometry -->
<!-- keywords: acsch -->
<!-- signatures: acsch(x) -->
### Function: acsch (x)

- Arco Cossecante Hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: asec -->
<!-- signatures: asec(x) -->
### Function: asec (x)

- Arco Secante.

<!-- category: Trigonometry -->
<!-- keywords: asech -->
<!-- signatures: asech(x) -->
### Function: asech (x)

- Arco Secante Hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: asin -->
<!-- signatures: asin(x) -->
### Function: asin (x)

- Arco Seno.

<!-- category: Trigonometry -->
<!-- keywords: asinh -->
<!-- signatures: asinh(x) -->
### Function: asinh (x)

- Arco Seno Hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: atan -->
<!-- signatures: atan(x) -->
### Function: atan (x)

- Arco Tangente.

<!-- category: Trigonometry -->
<!-- keywords: atan2 -->
<!-- signatures: atan2(y, x) -->
### Function: atan2 (y, x)

- retorna o valor de `atan(y/x)` no intervalo de `-%pi` a
`%pi`.

<!-- category: Trigonometry -->
<!-- keywords: atanh -->
<!-- signatures: atanh(x) -->
### Function: atanh (x)

- Arco tangente Hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: atrig1 -->
<!-- signatures: atrig1 -->
### Variable: atrig1

O pacote `atrig1` contém muitas regras adicionais de simplificação 
para funções trigonométricas inversas.  Junto com regras
já conhecidas para Maxima, os seguintes ângulos estão completamente implementados:
`0`, `%pi/6`, `%pi/4`, `%pi/3`, e `%pi/2`.  
Os ângulos correspondentes nos outros três quadrantes estão também disponíveis.  
Faça `load("atrig1");` para usá-lo.

<!-- category: Trigonometry -->
<!-- keywords: cos -->
<!-- signatures: cos(x) -->
### Function: cos (x)

- Cosseno.

<!-- category: Trigonometry -->
<!-- keywords: cosh -->
<!-- signatures: cosh(x) -->
### Function: cosh (x)

- Cosseno hiperbólico.

<!-- category: Trigonometry -->
<!-- keywords: cot -->
<!-- signatures: cot(x) -->
### Function: cot (x)

- Cotangente.

<!-- category: Trigonometry -->
<!-- keywords: coth -->
<!-- signatures: coth(x) -->
### Function: coth (x)

- Cotangente Hyperbólica.

<!-- category: Trigonometry -->
<!-- keywords: csc -->
<!-- signatures: csc(x) -->
### Function: csc (x)

- Cossecante.

<!-- category: Trigonometry -->
<!-- keywords: csch -->
<!-- signatures: csch(x) -->
### Function: csch (x)

- Cossecante Hyperbólica.

<!-- category: Trigonometry -->
<!-- keywords: halfangles -->
<!-- signatures: halfangles -->
### Variable: halfangles

Default value: `false`


Quando `halfangles` for `true`,
meios-ângulos são simplificados imediatamente.

<!-- category: Trigonometry -->
<!-- keywords: ntrig -->
<!-- signatures: ntrig -->
### Variable: ntrig

O pacote `ntrig` contém um conjunto de regras de simplificação que são
usadas para simplificar função trigonométrica cujos argumentos estão na forma
`f(n %pi/10)` onde *f* é qualquer das funções 
`sin`, `cos`, `tan`, `csc`, `sec` e `cot`.

<!-- category: Trigonometry -->
<!-- keywords: sec -->
<!-- signatures: sec(x) -->
### Function: sec (x)

- Secante.

<!-- category: Trigonometry -->
<!-- keywords: sech -->
<!-- signatures: sech(x) -->
### Function: sech (x)

- Secante Hyperbólica.

<!-- category: Trigonometry -->
<!-- keywords: sin -->
<!-- signatures: sin(x) -->
### Function: sin (x)

- Seno.

<!-- category: Trigonometry -->
<!-- keywords: sinh -->
<!-- signatures: sinh(x) -->
### Function: sinh (x)

- Seno Hyperbólico.

<!-- category: Trigonometry -->
<!-- keywords: tan -->
<!-- signatures: tan(x) -->
### Function: tan (x)

- Tangente.

<!-- category: Trigonometry -->
<!-- keywords: tanh -->
<!-- signatures: tanh(x) -->
### Function: tanh (x)

- Tangente Hyperbólica.

<!-- category: Trigonometry -->
<!-- keywords: trigexpand -->
<!-- signatures: trigexpand(expr) -->
### Function: trigexpand (expr)

Expande funções trigonometricas e hyperbólicas de
adições de ângulos e de ângulos multiplos que ocorram em *expr*.  Para melhores
resultados, *expr* deve ser expandida.  Para intensificar o controle do usuário
na simplificação, essa função expande somente um nível de cada vez,
expandindo adições de ângulos ou ângulos multiplos.  Para obter expansão completa
dentro de senos e cossenos imediatamente, escolha o comutador `trigexpand: true`.


`trigexpand` é governada pelos seguintes sinalizadores globais:



**trigexpand** — Se `true` causa expansão de todas as
expressões contendo senos e cossenos ocorrendo subsequêntemente.
**halfangles** — Se `true` faz com que meios-ângulos sejam simplificados
imediatamente.
**trigexpandplus** — Controla a regra "soma" para `trigexpand`,
expansão de adições (e.g. `sin(x + y)`) terão lugar somente se
`trigexpandplus` for `true`.
**trigexpandtimes** — Controla a regra "produto" para `trigexpand`,
expansão de produtos (e.g. `sin(2 x)`) terão lugar somente se
`trigexpandtimes` for `true`.


Exemplos:







```maxima
(%i1) x+sin(3*x)/sin(x),trigexpand=true,expand;
                         2           2
(%o1)               - sin (x) + 3 cos (x) + x
(%i2) trigexpand(sin(10*x+y));
(%o2)          cos(10 x) sin(y) + sin(10 x) cos(y)
```

<!-- category: Trigonometry -->
<!-- keywords: trigexpandplus -->
<!-- signatures: trigexpandplus -->
### Variable: trigexpandplus

Valor padrão: `true`


`trigexpandplus` controla a regra da "soma" para
`trigexpand`.  Dessa forma, quando o comando `trigexpand` for usado ou o
comutador `trigexpand` escolhido para `true`, expansão de adições
(e.g. `sin(x+y))` terão lugar somente se `trigexpandplus` for
`true`.

<!-- category: Trigonometry -->
<!-- keywords: trigexpandtimes -->
<!-- signatures: trigexpandtimes -->
### Variable: trigexpandtimes

Valor padrão: `true`


`trigexpandtimes` controla a regra "produto" para
`trigexpand`.  Dessa forma, quando o comando `trigexpand` for usado ou o
comutador `trigexpand` escolhido para `true`, expansão de produtos (e.g. `sin(2*x)`)
terão lugar somente se `trigexpandtimes` for `true`.

<!-- category: Trigonometry -->
<!-- keywords: triginverses -->
<!-- signatures: triginverses -->
### Variable: triginverses

Valor padrão: `all`


`triginverses` controla a simplificação de
composições de funções trigonométricas e hiperbólicas com suas funções
inversas.


Se `all`, ambas e.g. `atan(tan(x))` 
e `tan(atan(x))` simplificarão para *x*.  


Se `true`, a simplificação  de `arcfun(fun(x))` 
é desabilitada.


Se `false`, ambas as simplificações  
`arcfun(fun(x))` e  
`fun(arcfun(x))`
são desabilitadas.

<!-- category: Trigonometry -->
<!-- keywords: trigrat -->
<!-- signatures: trigrat(expr) -->
### Function: trigrat (expr)

Fornece uma forma quase-linear simplificada canônica de uma
expressão trigonométrica; *expr* é uma fração racional de muitos `sin`,
`cos` ou `tan`, os argumentos delas são formas lineares em algumas variáveis (ou
kernels-núcleos) e `%pi/n` (*n* inteiro) com coeficientes inteiros. O resultado é uma
fração simplificada com numerador e denominador ambos lineares em `sin` e `cos`.
Dessa forma `trigrat` lineariza sempre quando isso for passível.






```maxima
(%i1) trigrat(sin(3*a)/sin(a+%pi/3));
(%o1)            sqrt(3) sin(2 a) + cos(2 a) - 1
```


O seguinte exemplo encontra-se em
Davenport, Siret, and Tournier, *Calcul Formel*, Masson (ou em inglês,
Addison-Wesley), seção 1.5.5, teorema de Morley.










```maxima
(%i1) c: %pi/3 - a - b;
                                    %pi
(%o1)                     - b - a + ---
                                     3
(%i2) bc: sin(a)*sin(3*c)/sin(a+b);
                      sin(a) sin(3 b + 3 a)
(%o2)                 ---------------------
                           sin(b + a)
(%i3) ba: bc, c=a, a=c$
(%i4) ac2: ba^2 + bc^2 - 2*bc*ba*cos(b);
         2       2
      sin (a) sin (3 b + 3 a)
(%o4) -----------------------
               2
            sin (b + a)

                                        %pi
   2 sin(a) sin(3 a) cos(b) sin(b + a - ---) sin(3 b + 3 a)
                                         3
 - --------------------------------------------------------
                           %pi
                   sin(a - ---) sin(b + a)
                            3

      2         2         %pi
   sin (3 a) sin (b + a - ---)
                           3
 + ---------------------------
             2     %pi
          sin (a - ---)
                    3
(%i5) trigrat (ac2);
(%o5) - (sqrt(3) sin(4 b + 4 a) - cos(4 b + 4 a)

 - 2 sqrt(3) sin(4 b + 2 a) + 2 cos(4 b + 2 a)

 - 2 sqrt(3) sin(2 b + 4 a) + 2 cos(2 b + 4 a)

 + 4 sqrt(3) sin(2 b + 2 a) - 8 cos(2 b + 2 a) - 4 cos(2 b - 2 a)

 + sqrt(3) sin(4 b) - cos(4 b) - 2 sqrt(3) sin(2 b) + 10 cos(2 b)

 + sqrt(3) sin(4 a) - cos(4 a) - 2 sqrt(3) sin(2 a) + 10 cos(2 a)

 - 9)/4
```

<!-- category: Trigonometry -->
<!-- keywords: trigreduce -->
<!-- signatures: trigreduce(expr, x), trigreduce(expr) -->
### Function: trigreduce (expr, x)

Combina produtos e expoentes de senos e cossenso
trigonométricos e hiperbólicos de *x* dentro daqueles de múltiplos de *x*.
Também tenta eliminar essas funções quando elas ocorrerem em
denominadores.  Se *x* for omitido então todas as variáveis em *expr* são usadas.


Veja também `poissimp`.






```maxima
(%i1) trigreduce(-sin(x)^2+3*cos(x)^2+x);
               cos(2 x)      cos(2 x)   1        1
(%o1)          -------- + 3 (-------- + -) + x - -
                  2             2       2        2
```


As rotinas de simplificação trigonométrica irão usar informações
declaradas em alguns casos simples.  Declarações sobre variáveis são
usadas como segue, e.g.








```maxima
(%i1) declare(j, integer, e, even, o, odd)$
(%i2) sin(x + (e + 1/2)*%pi);
(%o2)                        cos(x)
(%i3) sin(x + (o + 1/2)*%pi);
(%o3)                       - cos(x)
```

<!-- category: Trigonometry -->
<!-- keywords: trigsign -->
<!-- signatures: trigsign -->
### Variable: trigsign

Valor padrão: `true`


Quando `trigsign` for `true`, permite simplificação de argumentos
negativos para funções trigonométricas. E.g., `sin(-x)` transformar-se-á em
`-sin(x)` somente se `trigsign` for `true`.

<!-- category: Trigonometry -->
<!-- keywords: trigsimp -->
<!-- signatures: trigsimp(expr) -->
### Function: trigsimp (expr)

Utiliza as identidades $sin(x)^2 + cos(x)^2 = 1$ and
$cosh(x)^2 - sinh(x)^2 = 1$ para simplificar expressões contendo `tan`, `sec`,
etc., para `sin`, `cos`, `sinh`, `cosh`.


`trigreduce`, `ratsimp`, e `radcan` podem estar
habilitadas a adicionar simplificações ao resultado.


`demo ("trgsmp.dem")` mostra alguns exemplos de `trigsimp`.

