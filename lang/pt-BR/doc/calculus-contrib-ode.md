## contrib_ode

<!-- category: Calculus -->
<!-- keywords: %c -->
<!-- signatures: %c -->
### Variable: %c

`%c` é a constante de integração para EDO’s de primeira ordem.

<!-- category: Calculus -->
<!-- keywords: %k1 -->
<!-- signatures: %k1 -->
### Variable: %k1

`%k1` é a primeira constante de integração para EDO’s de segunda ordem.

<!-- category: Calculus -->
<!-- keywords: %k2 -->
<!-- signatures: %k2 -->
### Variable: %k2

`%k2` é a segunda constante de integração para EDO’s de segunda ordem.

<!-- category: Calculus -->
<!-- keywords: contrib_ode -->
<!-- signatures: contrib_ode(eqn, y, x) -->
### Function: contrib_ode (eqn, y, x)

Retorna uma lista de soluções da EDO *eqn* com
variável independente *x* e variável dependente *y*.

<!-- category: Calculus -->
<!-- keywords: dgauss_a -->
<!-- signatures: dgauss_a(a, b, c, x) -->
### Function: dgauss_a (a, b, c, x)

A derivada em relação a x de `gauss_a(a,b,c,x)`.

<!-- category: Calculus -->
<!-- keywords: dgauss_b -->
<!-- signatures: dgauss_b(a, b, c, x) -->
### Function: dgauss_b (a, b, c, x)

A derivada em relação a x de `gauss_b(a,b,c,x)`.

<!-- category: Calculus -->
<!-- keywords: dkummer_m -->
<!-- signatures: dkummer_m(a, b, x) -->
### Function: dkummer_m (a, b, x)

A derivada com relação a x de `kummer_m(a,b,x)`.

<!-- category: Calculus -->
<!-- keywords: dkummer_u -->
<!-- signatures: dkummer_u(a, b, x) -->
### Function: dkummer_u (a, b, x)

A derivada com relação a x de  `kummer_u(a,b,x)`.

<!-- category: Calculus -->
<!-- keywords: gauss_a -->
<!-- signatures: gauss_a(a, b, c, x) -->
### Function: gauss_a (a, b, c, x)

`gauss_a(a,b,c,x)` e `gauss_b(a,b,c,x)` são funções
hipergeométricas 2F1.  Elas represetnam quaisquer duas soluções
independentes da equação diferencial hipergeométrica
`x(1-x) diff(y,x,2) + [c-(a+b+1)x diff(y,x) - aby = 0` (A&S 15.5.1).  


O único uso dessas funções é em soluções de EDO’s retornadas por
`odelin` e `contrib_ode`.  A definição e o uso dessas
funções pode mudar em futuras versões do maxima.


Veja também `gauss_b`, `dgauss_a` e `gauss_b`.

<!-- category: Calculus -->
<!-- keywords: gauss_b -->
<!-- signatures: gauss_b(a, b, c, x) -->
### Function: gauss_b (a, b, c, x)

Veja `gauss_a`.

<!-- category: Calculus -->
<!-- keywords: kummer_m -->
<!-- signatures: kummer_m(a, b, x) -->
### Function: kummer_m (a, b, x)

A função  M de Kummer, como definida em Abramowitz e Stegun,
*Handbook of Mathematical Functions*, Section 13.1.2.


O único uso dessas funções é em soluções de EDO’s retornadas por
`odelin` e `contrib_ode`.  A definição e o uso dessas
funções pode mudar em futuras versões do maxima.


Veja também `kummer_u`, `dkummer_m` e `dkummer_u`.

<!-- category: Calculus -->
<!-- keywords: kummer_u -->
<!-- signatures: kummer_u(a, b, x) -->
### Function: kummer_u (a, b, x)

A função U de Kummer, como definida em Abramowitz e Stegun,
*Handbook of Mathematical Functions*, Section 13.1.3.


Veja `kummer_m`.

<!-- category: Calculus -->
<!-- keywords: method -->
<!-- signatures: method -->
### Variable: method

A variável `method` é escolhida para o método que resolver com sucesso
uma dada EDO.

<!-- category: Calculus -->
<!-- keywords: ode_check -->
<!-- signatures: ode_check(eqn, sol) -->
### Function: ode_check (eqn, sol)

Retorna o valor da EDO *eqn* após substituir uma
possível solução *sol*.  O valor é igual a
zero se *sol* for uma solução of *eqn*.










```maxima
(%i1) load("contrib_ode")$

(%i2) eqn:'diff(y,x,2)+(a*x+b)*y;

                         2
                        d y
(%o2)                   --- + (a x + b) y
                          2
                        dx
(%i3) ans:[y = bessel_y(1/3,2*(a*x+b)^(3/2)/(3*a))*%k2*sqrt(a*x+b)
         +bessel_j(1/3,2*(a*x+b)^(3/2)/(3*a))*%k1*sqrt(a*x+b)];

                                  3/2
                    1  2 (a x + b)
(%o3) [y = bessel_y(-, --------------) %k2 sqrt(a x + b)
                    3       3 a
                                          3/2
                            1  2 (a x + b)
                 + bessel_j(-, --------------) %k1 sqrt(a x + b)]
                            3       3 a
(%i4) ode_check(eqn,ans[1]);

(%o4)                           0
```

<!-- category: Calculus -->
<!-- keywords: odelin -->
<!-- signatures: odelin(eqn, y, x) -->
### Function: odelin (eqn, y, x)

`odelin` resolve EDO’s lineares homogêneas de primeira e 
segunda ordem com
variável independente *x* e variável dependente *y*.  
`odelin` retorna um conjunto solução fundamental da EDO.


para EDO’s de segunda ordem, `odelin` usa um método, devido a Bronstein
e Lafaille, que busca por soluções em termos de funções 
especiais dadas. 







```maxima
(%i1) load("contrib_ode");

(%i2) odelin(x*(x+1)*'diff(y,x,2)+(x+5)*'diff(y,x,1)+(-4)*y,y,x);
...trying factor method
...solving 7 equations in 4 variables
...trying the Bessel solver
...solving 1 equations in 2 variables
...trying the F01 solver
...solving 1 equations in 3 variables
...trying the spherodial wave solver
...solving 1 equations in 4 variables
...trying the square root Bessel solver
...solving 1 equations in 2 variables
...trying the 2F1 solver
...solving 9 equations in 5 variables
       gauss_a(- 6, - 2, - 3, - x)  gauss_b(- 6, - 2, - 3, - x)
(%o2) {---------------------------, ---------------------------}
                    4                            4
                   x                            x
```

