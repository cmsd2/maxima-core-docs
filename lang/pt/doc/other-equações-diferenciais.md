## Equações Diferenciais

<!-- category: Other -->
<!-- keywords: bc2 -->
<!-- signatures: bc2(solução, xval1, yval1, xval2, yval2) -->
### Function: bc2 (solução, xval1, yval1, xval2, yval2)

Resolve um problema de valores fronteira para uma equação
diferencial de segunda ordem.  Aqui: *solução* é
uma solução geral para a equação,
calculada por `ode2`; *xval1* define o valor da variável
independente, num primeiro ponto, na forma `x = x1`, e
*yval1* define o valor da variável dependente, no mesmo ponto, na
forma `y = y1`. As expressões *xval2* e
*yval2* definem os valores das mesmas variáveis, num segundo
ponto, usando a mesma forma.


Veja um exemplo da sua utilização na documentação de
`ode2`.

<!-- category: Other -->
<!-- keywords: desolve -->
<!-- signatures: desolve(eqn, x), desolve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: desolve (eqn, x)

A função `dsolve` resolve sistemas de
equações diferenciais ordinárias lineares usando transformada de
Laplace. Aqui as expressões *eqn* são equações
diferenciais nas variáveis dependentes *x_1*, ..., *x_n*.  A
relação funcional de *x_1*, ..., *x_n* na variável
independente deve ser indicada explicitamente nas variáveis e nas suas
derivadas. Por exemplo, esta forma de definir as equações não
seria correcta:



```maxima
eqn_1: 'diff(f,x,2) = sin(x) + 'diff(g,x);
eqn_2: 'diff(f,x) + x^2 - f = 2*'diff(g,x,2);
```


A forma correcta seria:



```maxima
eqn_1: 'diff(f(x),x,2) = sin(x) + 'diff(g(x),x);
eqn_2: 'diff(f(x),x) + x^2 - f(x) = 2*'diff(g(x),x,2);
```


Assim, a chamada à função `desolve` seria:


```maxima
desolve([eqn_1, eqn_2], [f(x),g(x)]);
```


Se as condições iniciais em `x=0` forem conhecidas, poderão
ser fornecidas antes de usar `desolve`, através de
`atvalue`.











```maxima
(%i1) 'diff(f(x),x)='diff(g(x),x)+sin(x);
                 d           d
(%o1)            -- (f(x)) = -- (g(x)) + sin(x)
                 dx          dx
(%i2) 'diff(g(x),x,2)='diff(f(x),x)-cos(x);
                  2
                 d            d
(%o2)            --- (g(x)) = -- (f(x)) - cos(x)
                   2          dx
                 dx
(%i3) atvalue('diff(g(x),x),x=0,a);
(%o3)                           a
(%i4) atvalue(f(x),x=0,1);
(%o4)                           1
(%i5) desolve([%o1,%o2],[f(x),g(x)]);
                  x
(%o5) [f(x) = a %e  - a + 1, g(x) = 

                                                x
                                   cos(x) + a %e  - a + g(0) - 1]
(%i6) [%o1,%o2],%o5,diff;
             x       x      x                x
(%o6)   [a %e  = a %e , a %e  - cos(x) = a %e  - cos(x)]
```


Se `desolve` não pode obter uma solução, retorna `false`.

<!-- category: Other -->
<!-- keywords: ic1 -->
<!-- signatures: ic1(solução, xval, yval) -->
### Function: ic1 (solução, xval, yval)

Resolve problemas de valor inicial para equações diferenciais de
primeira ordem.  Aqui *solução* é uma solução geral
para a equação, na forma dada por `ode2`, *xval* dá um
valor inicial para a variável independente, na forma `x = x0`, e *yval* dá o valor inicial para a variável
dependente, na forma `y = y0`.


Veja um exemplo da sua utilização na documentação de
`ode2`.

<!-- category: Other -->
<!-- keywords: ic2 -->
<!-- signatures: ic2(solução, xval, yval, dval) -->
### Function: ic2 (solução, xval, yval, dval)

Resolve problemas de valores iniciais para equações diferenciais
de segunda ordem. Aqui *solução* é uma solução geral
para a equação, na forma dada por `ode2`, *xval* dá um
valor inicial para a variável independente, na forma `x = x0`, *yval* dá o valor inicial para a variável dependente,
na forma `y = y0` e *dval* dá o valor inicial
para a primeira derivada da variável dependente, em função da
variável independente, na forma `diff(y,x) = dy0` (`diff` não tem que ser precedido por apóstrofo).


Veja um exemplo da sua utilização na documentação de
`ode2`.

<!-- category: Other -->
<!-- keywords: ode2 -->
<!-- signatures: ode2(eqn, dvar, ivar) -->
### Function: ode2 (eqn, dvar, ivar)

A função `ode2` resolve uma equação diferencial
ordinária (EDO) de primeira ou de segunda ordem.  Precisa de três
argumentos: uma EDO dada por *eqn*, a variável dependente
*dvar*, e a variável independente *ivar*.  Quando conseguir,
retorna uma solução para a variável dependente, na forma
explícita ou implícita. `%c` é usado
para representar a constante de integração no caso de
equações de primeira ordem, e `%k1` e `%k2` as
constantes para equações de segunda ordem. A dependência da
variável dependente na variável independente não tem que ser
escrita em forma explícita, como no caso de
`desolve`, mas a variável independente deverá ser indicada
sempre no terceiro argumento.


Se por alguma razão `ode2` não conseguir encontrar a
solução, retornará `false`, após talvez mostrar uma
mensagem de erro. Os métodos implementados para equações
diferenciais de primeira ordem, na ordem em que serão testados, são:
linear, separável, exacta - talvez requerendo um factor de
integração, homogénea, equação de Bernoulli, homogénea
generalizada. Os tipos de equações de segunda ordem que podem ser
resolvidas são: coeficientes constantes, exactas, linear homogéneas
com coeficientes não-constantes que possam ser transformados para
constates, equação de Euler ou equi-dimensional, equações que
possam ser resolvidas pelo método de variação dos parâmetros,
e equações que não dependam ou da variável independente ou da
variável dependente de modo que possam ser reduzidas a duas
equações lineares de primeira ordem a serem resolvidas
sequêncialmente.


Durante o processo de resolução da EDO, serão dados valores a
várias variáveis locais, com fins puramente informativos:
`método` denota o método de solução usado (por exemplo,
`linear`), `intfactor` denota qualquer factor integrante
utilizado, `odeindex` denota o índice para o método
de Bernoulli ou para o método homogéneo generalizado, e `yp`
denota a solução particular no método de variação dos
parâmetros.


Para resolver problemas de valores iniciais (PVI) estão
disponiveis as funções `ic1` e `ic2`e, para
equações de primeira e segunda ordem, e para resolver problemas de
valores fronteira (PVF) de segunda ordem pode usar-se a função
`bc2`.


Exemplo:












```maxima
(%i1) x^2*'diff(y,x) + 3*y*x = sin(x)/x;
                      2 dy           sin(x)
(%o1)                x  -- + 3 x y = ------
                        dx             x
(%i2) ode2(%,y,x);
                             %c - cos(x)
(%o2)                    y = -----------
                                  3
                                 x
(%i3) ic1(%o2,x=%pi,y=0);
                              cos(x) + 1
(%o3)                   y = - ----------
                                   3
                                  x
(%i4) 'diff(y,x,2) + y*'diff(y,x)^3 = 0;
                         2
                        d y      dy 3
(%o4)                   --- + y (--)  = 0
                          2      dx
                        dx
(%i5) ode2(%,y,x);
                      3
                     y  + 6 %k1 y
(%o5)                ------------ = x + %k2
                          6
(%i6) ratsimp(ic2(%o5,x=0,y=0,'diff(y,x)=2));
                             3
                          2 y  - 3 y
(%o6)                   - ---------- = x
                              6
(%i7) bc2(%o5,x=0,y=1,x=1,y=3);
                         3
                        y  - 10 y       3
(%o7)                   --------- = x - -
                            6           2
```

