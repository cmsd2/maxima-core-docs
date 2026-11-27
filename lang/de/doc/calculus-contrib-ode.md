## contrib_ode

<!-- category: Calculus -->
<!-- keywords: %c -->
<!-- signatures: %c -->
### Variable: %c

`%c` is the integration constant for first order ODEs.

<!-- category: Calculus -->
<!-- keywords: %k1 -->
<!-- signatures: %k1 -->
### Variable: %k1

`%k1` is the first integration constant for second order ODEs.

<!-- category: Calculus -->
<!-- keywords: %k2 -->
<!-- signatures: %k2 -->
### Variable: %k2

`%k2` is the second integration constant for second order ODEs.

<!-- category: Calculus -->
<!-- keywords: contrib_ode -->
<!-- signatures: contrib_ode(eqn, y, x) -->
### Function: contrib_ode (eqn, y, x)

Returns a list of solutions of the ODE *eqn* with 
independent variable *x* and dependent variable *y*.

<!-- category: Calculus -->
<!-- keywords: dgauss_a -->
<!-- signatures: dgauss_a(a, b, c, x) -->
### Function: dgauss_a (a, b, c, x)

The derivative with respect to *x* of 
`gauss_a(a, b, c, x)`.

<!-- category: Calculus -->
<!-- keywords: dgauss_b -->
<!-- signatures: dgauss_b(a, b, c, x) -->
### Function: dgauss_b (a, b, c, x)

The derivative with respect to *x* of 
`gauss_b(a, b, c, x)`.

<!-- category: Calculus -->
<!-- keywords: dkummer_m -->
<!-- signatures: dkummer_m(a, b, x) -->
### Function: dkummer_m (a, b, x)

The derivative with respect to *x* of 
`kummer_m(a, b, x)`.

<!-- category: Calculus -->
<!-- keywords: dkummer_u -->
<!-- signatures: dkummer_u(a, b, x) -->
### Function: dkummer_u (a, b, x)

The derivative with respect to *x* of 
`kummer_u(a, b, x)`.

<!-- category: Calculus -->
<!-- keywords: gauss_a -->
<!-- signatures: gauss_a(a, b, c, x) -->
### Function: gauss_a (a, b, c, x)

`gauss_a(a,b,c,x)` and `gauss_b(a,b,c,x)` are 2F1 geometric functions.
They represent any two independent solutions of the hypergeometric differential
equation `x(1-x) diff(y,x,2) + [c-(a+b+1)x diff(y,x) - aby = 0`
(A&S 15.5.1).


The only use of these functions is in solutions of ODEs returned by
`odelin` and `contrib_ode`.  The definition and use of these
functions may change in future releases of Maxima.


See also `gauss_b`, `dgauss_a` and `gauss_b`.

<!-- category: Calculus -->
<!-- keywords: gauss_b -->
<!-- signatures: gauss_b(a, b, c, x) -->
### Function: gauss_b (a, b, c, x)

See `gauss_a`.

<!-- category: Calculus -->
<!-- keywords: kummer_m -->
<!-- signatures: kummer_m(a, b, x) -->
### Function: kummer_m (a, b, x)

Kummer’s M function, as defined in Abramowitz and Stegun,
*Handbook of Mathematical Functions*, Section 13.1.2.


The only use of this function is in solutions of ODEs returned by 
`odelin` and `contrib_ode`.  The definition and use of this 
function may change in future releases of Maxima.


See also `kummer_u`, `dkummer_m` and `dkummer_u`.

<!-- category: Calculus -->
<!-- keywords: kummer_u -->
<!-- signatures: kummer_u(a, b, x) -->
### Function: kummer_u (a, b, x)

Kummer’s U function, as defined in Abramowitz and Stegun,
*Handbook of Mathematical Functions*, Section 13.1.3.


See `kummer_m`.

<!-- category: Calculus -->
<!-- keywords: method -->
<!-- signatures: method -->
### Variable: method

The variable `method` is set to the successful solution method.

<!-- category: Calculus -->
<!-- keywords: ode_check -->
<!-- signatures: ode_check(eqn, soln) -->
### Function: ode_check (eqn, soln)

Returns the value of ODE *eqn* after substituting a possible solution
*soln*.  The value is equivalent to zero if *soln* is a solution of
*eqn*.



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

`odelin` solves linear homogeneous ODEs of first and second order with
independent variable *x* and dependent variable *y*.  It returns a
fundamental solution set of the ODE.


For second order ODEs, `odelin` uses a method, due to Bronstein and
Lafaille, that searches for solutions in terms of given special functions.



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

