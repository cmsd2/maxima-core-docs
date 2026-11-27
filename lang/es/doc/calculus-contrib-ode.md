## contrib_ode

<!-- category: Calculus -->
<!-- keywords: %c -->
<!-- signatures: %c -->
### Variable: %c

`%c` es la constante de integración para EDOs de primer
orden.

<!-- category: Calculus -->
<!-- keywords: %k1 -->
<!-- signatures: %k1 -->
### Variable: %k1

`%k1` es la primera constante de integración para EDOs de segundo
orden.

<!-- category: Calculus -->
<!-- keywords: %k2 -->
<!-- signatures: %k2 -->
### Variable: %k2

`%k2` es la segunda constante de integración para EDOs de segundo
orden.

<!-- category: Calculus -->
<!-- keywords: contrib_ode -->
<!-- signatures: contrib_ode(eqn, y, x) -->
### Function: contrib_ode (eqn, y, x)

Devuelve la lista de soluciones de la ecuación diferencia
ordinaria (EDO) *eqn* de variable independiente *x*
y variable dependiente *y*.

<!-- category: Calculus -->
<!-- keywords: dgauss_a -->
<!-- signatures: dgauss_a(a, b, c, x) -->
### Function: dgauss_a (a, b, c, x)

The derivative with respect to x of `gauss_a(a,b,c,x)`.

<!-- category: Calculus -->
<!-- keywords: dgauss_b -->
<!-- signatures: dgauss_b(a, b, c, x) -->
### Function: dgauss_b (a, b, c, x)

Derivada de `gauss_b(a,b,c,x)` respecto de *x*.

<!-- category: Calculus -->
<!-- keywords: dkummer_m -->
<!-- signatures: dkummer_m(a, b, x) -->
### Function: dkummer_m (a, b, x)

Derivada de `kummer_m(a,b,x)` respecto de *x*.

<!-- category: Calculus -->
<!-- keywords: dkummer_u -->
<!-- signatures: dkummer_u(a, b, x) -->
### Function: dkummer_u (a, b, x)

Derivada de `kummer_u(a,b,x)` respecto de *x*.

<!-- category: Calculus -->
<!-- keywords: gauss_a -->
<!-- signatures: gauss_a(a, b, c, x) -->
### Function: gauss_a (a, b, c, x)

`gauss_a(a,b,c,x)` y `gauss_b(a,b,c,x)` son funciones
geométricas 2F1 . Representan dos soluciones independientes
cualesquiera de la ecuación diferencial hipergeométrica
`x(1-x) diff(y,x,2) + [c-(a+b+1)x] diff(y,x) - aby = 0` (A&S 15.5.1).


El único uso que se hace de estas funciones es en las soluciones de
EDOs que devuelven `odelin` y `contrib_ode`. La definición
y utilización de estas funciones puede cambiar en futuras distribuciones
de Maxima.


Véanse también `gauss_b`, `dgauss_a` y `gauss_b`.

<!-- category: Calculus -->
<!-- keywords: gauss_b -->
<!-- signatures: gauss_b(a, b, c, x) -->
### Function: gauss_b (a, b, c, x)

Véase  también `gauss_a`.

<!-- category: Calculus -->
<!-- keywords: kummer_m -->
<!-- signatures: kummer_m(a, b, x) -->
### Function: kummer_m (a, b, x)

Función M de Kummer, tal como la definen Abramowitz y Stegun,
*Handbook of Mathematical Functions*, Sección 13.1.2.


El único uso que se hace de esta función es en las soluciones de
EDOs que devuelven `odelin` y `contrib_ode`. La definición
y utilización de estas funciones puede cambiar en futuras distribuciones
de Maxima.


Véanse también `kummer_u`, `dkummer_m` y `dkummer_u`.

<!-- category: Calculus -->
<!-- keywords: kummer_u -->
<!-- signatures: kummer_u(a, b, x) -->
### Function: kummer_u (a, b, x)

Función U de Kummer, tal como la definen Abramowitz y Stegun,
*Handbook of Mathematical Functions*, Sección 13.1.3.


Véase  también `kummer_m`.

<!-- category: Calculus -->
<!-- keywords: method -->
<!-- signatures: method -->
### Variable: method

A la variable `method` se le asigna el método aplicado.

<!-- category: Calculus -->
<!-- keywords: ode_check -->
<!-- signatures: ode_check(eqn, soln) -->
### Function: ode_check (eqn, soln)

Devuelve el valor de la ecuación diferencia
ordinaria (EDO) *eqn* después de sustituir
una posible solución *soln*. El valor es
cero si *soln* es una solución de *eqn*.










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

La función `odelin` resulve EDOs homogéneas lineales
de primer y segundo orden con variable independiente *x*
y variable dependiente *y*. Devuelve un conjunto fundamental
de soluciones de la EDO.


Para EDOs de segundo orden, `odelin` utiliza un
método desarrollado por Bronstein y Lafaille, que busca las soluciones
en términos de funciones especiales dadas.







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

