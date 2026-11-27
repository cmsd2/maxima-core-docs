## contrib_ode

<!-- category: Calculus -->
<!-- keywords: %c -->
<!-- signatures: %c -->
### Variable: %c

`%c`は一階ODEの積分定数です。

<!-- category: Calculus -->
<!-- keywords: %k1 -->
<!-- signatures: %k1 -->
### Variable: %k1

`%k1`は二階ODEの最初の積分定数です。

<!-- category: Calculus -->
<!-- keywords: %k2 -->
<!-- signatures: %k2 -->
### Variable: %k2

`%k2`は二階ODEの二番目の積分定数です。

<!-- category: Calculus -->
<!-- keywords: contrib_ode -->
<!-- signatures: contrib_ode(eqn, y, x) -->
### Function: contrib_ode (eqn, y, x)

独立変数*x*と従属変数*y*に関するODE *eqn*の解のリストを返します。

<!-- category: Calculus -->
<!-- keywords: dgauss_a -->
<!-- signatures: dgauss_a(a, b, c, x) -->
### Function: dgauss_a (a, b, c, x)

`gauss_a(a, b, c, x)`の*x*に関する導関数。

<!-- category: Calculus -->
<!-- keywords: dgauss_b -->
<!-- signatures: dgauss_b(a, b, c, x) -->
### Function: dgauss_b (a, b, c, x)

`gauss_b(a, b, c, x)`の*x*に関する導関数。

<!-- category: Calculus -->
<!-- keywords: dkummer_m -->
<!-- signatures: dkummer_m(a, b, x) -->
### Function: dkummer_m (a, b, x)

`kummer_m(a, b, x)`の*x*に関する導関数。

<!-- category: Calculus -->
<!-- keywords: dkummer_u -->
<!-- signatures: dkummer_u(a, b, x) -->
### Function: dkummer_u (a, b, x)

`kummer_u(a, b, x)`の*x*に関する導関数。

<!-- category: Calculus -->
<!-- keywords: gauss_a -->
<!-- signatures: gauss_a(a, b, c, x) -->
### Function: gauss_a (a, b, c, x)

`gauss_a(a,b,c,x)`と`gauss_b(a,b,c,x)`は2F1幾何関数です。
それらは超幾何微分方程式
`x(1-x) diff(y,x,2) + [c-(a+b+1)x diff(y,x) - aby = 0` 
の任意の２つの独立解を表します(A&S 15.5.1)。


これらの関数は
`odelin`と`contrib_ode`が返すODEの解の中でだけ使われます。
これらの関数の定義と使用はMaimaの将来のリリースで変わるかもしれません。


`gauss_b`, `dgauss_a`, `gauss_b`も参照してください。

<!-- category: Calculus -->
<!-- keywords: gauss_b -->
<!-- signatures: gauss_b(a, b, c, x) -->
### Function: gauss_b (a, b, c, x)

See `gauss_a`.

<!-- category: Calculus -->
<!-- keywords: kummer_m -->
<!-- signatures: kummer_m(a, b, x) -->
### Function: kummer_m (a, b, x)

Abramowitz and Stegun,
*Handbook of Mathematical Functions*, Section 13.1.2の中で定義される
KummerのM関数


この関数は
`odelin`と`contrib_ode`が返すODEの解の中でだけ使われます。
この関数の定義と使用はMaimaの将来のリリースで変わるかもしれません。


`kummer_u`, `dkummer_m`, `dkummer_u`も参照してください。

<!-- category: Calculus -->
<!-- keywords: kummer_u -->
<!-- signatures: kummer_u(a, b, x) -->
### Function: kummer_u (a, b, x)

Abramowitz and Stegun,
*Handbook of Mathematical Functions*, Section 13.1.3の中で定義される
KummerのU関数


`kummer_m`を参照してください。

<!-- category: Calculus -->
<!-- keywords: method -->
<!-- signatures: method -->
### Variable: method

変数`method`は成功した解法に設定されます。

<!-- category: Calculus -->
<!-- keywords: ode_check -->
<!-- signatures: ode_check(eqn, soln) -->
### Function: ode_check (eqn, soln)

可能な解*soln*を代入した後、
ODE *eqn*の値を返します。
もし*soln*が*eqn*の解なら
値はゼロと同値です。










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

`odelin`は
独立変数*x*と従属変数*y*に関する
一階および二階線形斉次ODEを解きます。
ODEの基本的な解一式を返します。


二階ODEに対して、`odelin`は、
与えられた特殊関数を使って解を探索する
BronsteinとLafailleによる方法
を使います。







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

