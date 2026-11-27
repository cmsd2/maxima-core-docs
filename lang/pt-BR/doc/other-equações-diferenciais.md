## Equações Diferenciais

<!-- category: Other -->
<!-- keywords: bc2 -->
<!-- signatures: bc2(solução, xval1, yval1, xval2, yval2) -->
### Function: bc2 (solução, xval1, yval1, xval2, yval2)

Resolve o problema do valor limite para equações diferenciais de segunda ordem. 
Aqui: *solução* é uma solução geral para a equação, como encontrado por
`ode2`, *xval1* especifica o valor da variável independente
em um primeiro ponto, na forma `x = x1`, e *yval1*
fornece o valor da variável dependente naquele ponto, na forma
`y = y1`. As expressões *xval2* e *yval2*
fornecem os valores para essas variáveis em um segundo ponto, usando a mesma
forma.


Veja `ode2` para um exemplo de sua utilização.

<!-- category: Other -->
<!-- keywords: desolve -->
<!-- signatures: desolve(eqn, x), desolve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: desolve (eqn, x)

A Função `dsolve` resolve sistema de equações diferenciais
lineares ordinárias usando a transformada de Laplace.  Aqui as *eqn*’s
são equações diferenciais nas variáveis dependentes *x_1*, ...,
*x_n*.  A dependência funcional de *x_1*, ..., *x_n* com relação à
variável independente, por exemplo *x*, deve ser explicitamente indicada
nas variáveis e em suas derivadas. Por exemplo, isso pode não ser
caminho correto para definir duas equações:



```maxima
eqn_1: 'diff(f,x,2) = sin(x) + 'diff(g,x);
eqn_2: 'diff(f,x) + x^2 - f = 2*'diff(g,x,2);
```


O caminho correto pode ser:



```maxima
eqn_1: 'diff(f(x),x,2) = sin(x) + 'diff(g(x),x);
eqn_2: 'diff(f(x),x) + x^2 - f(x) = 2*'diff(g(x),x,2);
```


A chamada à função `desolve` pode então ser


```maxima
desolve([eqn_1, eqn_2], [f(x),g(x)]);
```


Se condições iniciais em `x=0` forem conhecidas, elas podem ser fornecidas antes
chamando `desolve` através de `atvalue`.











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

Resolve problemas de valor inicial para equações diferenciais de primeira ordem.
Aqui *solução* é uma solução geral para a equação, como encontrado por
`ode2`, *xval* fornece um valor inicial para a variável
independente na forma `x = x0`, e *yval* fornece o
valor inicial para a variável dependente na forma `y = y0`.


Veja `ode2` para um exemplo de sua utilização.

<!-- category: Other -->
<!-- keywords: ic2 -->
<!-- signatures: ic2(solução, xval, yval, dval) -->
### Function: ic2 (solução, xval, yval, dval)

Resolve problemas de valor inicial para equações diferenciais de segunda ordem.
Aqui *solução* é uma solução geral para a equação, como encontrada por
`ode2`, *xval* fornece o valor inicial para a variável
independente na forma `x = x0`, *yval* fornece o
valor inicial da veriável dependente na forma `y = y0`, e *dval* fornece o valor inicial para a primeira
derivada da variável dependente com relação à variável
independente, na forma `diff(y,x) = dy0`
(`diff` não precisa receber apóstrofo para evitar avaliação).


Veja `ode2` para um exemplo de seu uso.

<!-- category: Other -->
<!-- keywords: ode2 -->
<!-- signatures: ode2(eqn, dvar, ivar) -->
### Function: ode2 (eqn, dvar, ivar)

A função `ode2` resolve uma equação diferencial ordinária (EDO)
de primeira ou de segunda ordem. `ode2` usa três argumentos: uma EDO fornecida por
*eqn*, a variável dependente *dvar*, e a variável
independente *ivar*. Quando `ode2` encontra uma solução, `ode2` retorna ou uma solução explícita ou
uma sulução implícita para a variável dependente. `%c` é usado para
representar a constante de integração no caso de equações de primeira ordem,
e `%k1` e `%k2` as constantes para equações de
segunda ordem. A dependência da variável dependente com relação à variável
independente não tem que ser escrita explicitamente, como no caso de
`desolve`, mas a variável independente deve sempre ser fornecida como o
terceiro argumento.


Se `ode2` não conseguir obter uma solução por qualquer razaão, `ode2` retorna
`false`, após talvez imprimir uma mensagem de erro. Os métodos
implementados para equações de primeira ordem na sequência em que eles foram
testados são: linear, separável, exato - talvez requerendo um fator de
integração, homogêneo, equação de Bernoulli, e um método homogêneo
generalizado. Os tipos de equaçõe de segunda ordem que podem ser resolvidos são:
coeficientes constantes, exato, linear homogêneo com coeficientes
não constantes que podem ser transformados em coeficientes constantes, o
tipo de equação de Euler também chamado de equação equi-dimensional, equações resolvíveis pelo método de
variação de parâmetros, e equações as quais são livres ou da
variável independente ou da dependente de modo que elas possam ser reduzidas a
duas equações lineares de primeira ordem para serem resolvidas sequêncialmente.


Na resolução de EDO’s pelo Maxima, muitas variáveis são escolhidas puramente para
propósitos informativos: `método` denota o método de solução
usado (e.g., `linear`), `intfactor` denota qualquer fator de
integração usado, `odeindex` denota o índice para o método de Bernoulli ou
para o método homogêneo generalizado, e `yp` denota a
solução particular para a técnica de variação de parâmetros.


Com o objetivo de resolver poblemas de valor inicial (PVI) as funções `ic1` e
`ic2` estão disponíveis para equações de primeira e de segunda ordem, e para
resolver problemas do valor de segunda ordem associado (BVP em inglês) a função `bc2`
pode ser usada.


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

