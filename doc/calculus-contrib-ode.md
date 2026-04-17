## contrib_ode

<!-- category: Calculus -->
<!-- keywords: bessel_simplify -->
<!-- signatures: bessel_simplify(expr) -->
### Function: bessel_simplify (expr)

Simplifies expressions containing Bessel functions `bessel_j`,
`bessel_y`, `bessel_i`, `bessel_k`,
`hankel_1`, `hankel_2`, `struve_h`
and `struve_005fl`.
Recurrence relations  [https://personal.math.ubc.ca/~cbm/aands/page_361.htmA&S eqn 9.1.27]() and [https://dlmf.nist.gov/10.6#iDLMF 10.6#i]()

are used to replace functions of highest order n
by functions of order n-1 and n-2.


This process is repeated until all the orders
differ by less than 2.















```maxima
(%i1) load("contrib_ode")$

(%i2) bessel_simplify(4*bessel_j(n,x^2)*(x^2-n^2/x^2)
  +x*((bessel_j(n-2,x^2)-bessel_j(n,x^2))*x
  -(bessel_j(n,x^2)-bessel_j(n+2,x^2))*x)
  -2*bessel_j(n+1,x^2)+2*bessel_j(n-1,x^2));
(%o2)                           0


(%i3) bessel_simplify( -2*bessel_j(1,z)*z^3 - 10*bessel_j(2,z)*z^2
 + 15*%pi*bessel_j(1,z)*struve_h(3,z)*z - 15*%pi*struve_h(1,z)
   *bessel_j(3,z)*z - 15*%pi*bessel_j(0,z)*struve_h(2,z)*z
 + 15*%pi*struve_h(0,z)*bessel_j(2,z)*z - 30*%pi*bessel_j(1,z)
   *struve_h(2,z) + 30*%pi*struve_h(1,z)*bessel_j(2,z));
(%o3)                           0
```

See also: `bessel_j`, `bessel_y`, `bessel_i`, `bessel_k`, `hankel_1`, `hankel_2`, `struve_h`, `struve_l`.

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

The derivative with respect to *x* 
of `gauss_a``(a, b, c, x)`.

See also: `gauss_a`.

<!-- category: Calculus -->
<!-- keywords: dgauss_b -->
<!-- signatures: dgauss_b(a, b, c, x) -->
### Function: dgauss_b (a, b, c, x)

The derivative with respect to *x* 
of `gauss_b``(a, b, c, x)`.

See also: `gauss_b`.

<!-- category: Calculus -->
<!-- keywords: dkummer_m -->
<!-- signatures: dkummer_m(a, b, x) -->
### Function: dkummer_m (a, b, x)

The derivative with respect to *x*
of `kummer_m``(a, b, x)`.

See also: `kummer_m`.

<!-- category: Calculus -->
<!-- keywords: dkummer_u -->
<!-- signatures: dkummer_u(a, b, x) -->
### Function: dkummer_u (a, b, x)

The derivative with respect to *x*
of `kummer_u``(a, b, x)`.

See also: `kummer_u`.

<!-- category: Calculus -->
<!-- keywords: expintegral_e_simplify -->
<!-- signatures: expintegral_e_simplify(expr) -->
### Function: expintegral_e_simplify (expr)

Simplify expressions containing exponential integral `expintegral_e`
using the recurrence [https://personal.math.ubc.ca/~cbm/aands/page_229.htmA&S eqn 5.1.14]().


   

expintegral_e(n+1,z) 
        = (1/n) * (exp(-z)-z*expintegral_e(n,z))      n = 1,2,3 ....

See also: `expintegral_e`.

<!-- category: Calculus -->
<!-- keywords: gauss_a -->
<!-- signatures: gauss_a(a, b, c, x) -->
### Function: gauss_a (a, b, c, x)

`gauss_a(a,b,c,x)` and `gauss_b(a,b,c,x)` are 2F1 
hypergeometric functions.  They represent any two independent
solutions of the hypergeometric differential equation 
`x*(1-x) diff(y,x,2) + [c-(a+b+1)x] diff(y,x) - a*b*y = 0`
See [https://personal.math.ubc.ca/~cbm/aands/page_562.htmA&S eqn 15.5.1]() and [https://dlmf.nist.gov/15.10DLMF 15.10]().  


The only use of these functions is in solutions of ODEs returned by 
`odelin` and `contrib_ode`.  The definition and use of these 
functions may change in future releases of Maxima.


See also `gauss_b`, `dgauss_a` and `gauss_005fb`.

See also: `odelin`, `contrib_ode`, `gauss_b`, `dgauss_a`.

<!-- category: Calculus -->
<!-- keywords: gauss_b -->
<!-- signatures: gauss_b(a, b, c, x) -->
### Function: gauss_b (a, b, c, x)

See `gauss_005fa`.

See also: `gauss_a`.

<!-- category: Calculus -->
<!-- keywords: kummer_m -->
<!-- signatures: kummer_m(a, b, x) -->
### Function: kummer_m (a, b, x)

Kummer’s M function, see [https://personal.math.ubc.ca/~cbm/aands/page_504.htmA&S eqn 13.1.2]() and [https://dlmf.nist.gov/13.2DLMF 13.2]().


The only use of this function is in solutions of ODEs returned by 
`odelin` and `contrib_ode`.  The definition and use of this 
function may change in future releases of Maxima.


See also `kummer_u`, `dkummer_m`, and `dkummer_005fu`.

See also: `odelin`, `contrib_ode`, `kummer_u`, `dkummer_m`, `dkummer_u`.

<!-- category: Calculus -->
<!-- keywords: kummer_u -->
<!-- signatures: kummer_u(a, b, x) -->
### Function: kummer_u (a, b, x)

Kummer’s U function, see [https://personal.math.ubc.ca/~cbm/aands/page_504.htmA&S eqn 13.1.3]() and [https://dlmf.nist.gov/13.2.6DLMF 13.2.6]().


See `kummer_005fm`.

See also: `kummer_m`.

<!-- category: Calculus -->
<!-- keywords: ode_check -->
<!-- signatures: ode_check(eqn, soln) -->
### Function: ode_check (eqn, soln)

Returns the value of ODE *eqn* after substituting a
possible solution *soln*.  The value is equivalent to 
zero if *soln* is a solution of *eqn*.










```maxima
(%i1) load("contrib_ode")$

(%i2) eqn:'diff(y,x,2)+(a*x+b)*y;
                         2
                        d y
(%o2)                   --- + (b + a x) y
                          2
                        dx

(%i3) ans:[y = bessel_y(1/3,2*(a*x+b)^(3/2)/(3*a))*%k2*sqrt(a*x+b)
         +bessel_j(1/3,2*(a*x+b)^(3/2)/(3*a))*%k1*sqrt(a*x+b)];
                                  3/2
                    1  2 (b + a x)
(%o3) [y = bessel_y(-, --------------) %k2 sqrt(a x + b)
                    3       3 a
                                          3/2
                            1  2 (b + a x)
                 + bessel_j(-, --------------) %k1 sqrt(a x + b)]
                            3       3 a

(%i4) ode_check(eqn,ans[1]);
(%o4)                           0
```

<!-- category: Calculus -->
<!-- keywords: odelin -->
<!-- signatures: odelin(eqn, y, x) -->
### Function: odelin (eqn, y, x)

`odelin` solves linear homogeneous ODEs of first and 
second order with 
independent variable *x* and dependent variable *y*.  
It returns a fundamental solution set of the ODE.


For second order ODEs, `odelin` uses a method, due to Bronstein
and Lafaille, that searches for solutions in terms of given 
special functions. 







```maxima
(%i1) load("contrib_ode")$

(%i2) odelin(x*(x+1)*'diff(y,x,2)+(x+5)*'diff(y,x,1)+(-4)*y,y,x);
       gauss_a(- 6, - 2, - 3, - x)  gauss_b(- 6, - 2, - 3, - x)
(%o2) {---------------------------, ---------------------------}
                    4                            4
                   x                            x
```

