## Differential Equations

<!-- category: Calculus -->
<!-- keywords: bc2 -->
<!-- signatures: bc2(solution, xval1, yval1, xval2, yval2) -->
### Function: bc2 (solution, xval1, yval1, xval2, yval2)

二階微分方程式の境界値問題を解きます。
ここで: *solution*は、`ode2`が見つけるような方程式の一般解です;
*xval1*は、独立変数の最初の点の値を、形式`x = x1`で指定し、
*yval1*は、その点の従属変数の値を、形式`y = y1`で与えます。
式*xval2*と*yval2*は、
それらの変数の二番目の点での値を、同じ形式を使って与えます。


用法の例については`ode2`を参照してください。

<!-- category: Calculus -->
<!-- keywords: desolve -->
<!-- signatures: desolve(eqn, x), desolve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: desolve (eqn, x)

関数`desolve`は、ラプラス変換を使って線形常微分方程式系を解きます。
ここで、*eqn*群は、従属変数*x_1*, ..., *x_n*に関する微分方程式です。
*x_1*, ..., *x_n*の独立変数、例えば*x*、への関数依存性は、
変数や導関数の中で陽に示されなければいけません。
例えば、これは、２つの方程式を定義する正しい方法ではありません:



```maxima
eqn_1: 'diff(f,x,2) = sin(x) + 'diff(g,x);
eqn_2: 'diff(f,x) + x^2 - f = 2*'diff(g,x,2);
```


正しい方法は以下の通りです:



```maxima
eqn_1: 'diff(f(x),x,2) = sin(x) + 'diff(g(x),x);
eqn_2: 'diff(f(x),x) + x^2 - f(x) = 2*'diff(g(x),x,2);
```


関数`desolve`のコールは、


```maxima
desolve([eqn_1, eqn_2], [f(x),g(x)]);
```

です。


もし`x=0`の初期条件が既知なら、
それらは、`atvalue`を使って、`desolve`コールの前に供給することができます。











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


もし`desolve`が解を得られないなら、
`false`を返します。

<!-- category: Calculus -->
<!-- keywords: ic1 -->
<!-- signatures: ic1(solution, xval, yval) -->
### Function: ic1 (solution, xval, yval)

一階微分方程式の初期値問題を解きます。
ここで、*solution*は、`ode2`が見つけるような、方程式の一般解であり、
*xval*は、独立変数の初期値を、形式`x = x0`で与え、
*yval*は、従属変数の初期値を、形式`y = y0`で与えます。


用法の例については`ode2`を参照してください。

<!-- category: Calculus -->
<!-- keywords: ic2 -->
<!-- signatures: ic2(solution, xval, yval, dval) -->
### Function: ic2 (solution, xval, yval, dval)

二階微分方程式の初期値を解きます。
ここで、 *solution*は、`ode2`が見つけるような、
方程式の一般解のであり、
*xval*は、独立変数の初期値を、形式`x = x0`で与え、
*yval*は、従属変数の初期値を、形式`y = y0`で与え、
*dval*は、従属変数の独立変数に関する一階導関数の初期値を、
形式`diff(y,x) = dy0`で、与えます。
(`diff`はクォートされる必要はありません。)


用法の例については、`ode2`を参照してください。

<!-- category: Calculus -->
<!-- keywords: ode2 -->
<!-- signatures: ode2(eqn, dvar, ivar) -->
### Function: ode2 (eqn, dvar, ivar)

関数`ode2`は、一階または二階常微分方程式(ODE)を解きます。
３つの引数を取ります:
*eqn*で与えられるODE、従属変数*dvar*、独立変数*ivar*。
成功した時、従属変数に関する陽解または陰解を返します。
一階方程式の場合、`%c`が積分定数を表し、
二階方程式の場合、`%k1`と`%k2`が定数を表します。
従属変数の独立変数への依存性は、
`desolve`の場合のように、陽に書かれる必要はありませんが、
独立変数はいつも三番目の引数として与えられなければいけません。


たとえどんな理由でも、もし`ode2`が解を得られなかったら、
おそらく、エラーメッセージを表示した後、`false`を返します。
一階方程式用に実装された方法は、試される順番に、線形、分離、厳密―おそらく因子の積分を要求します―、斉次、ベルヌーイの等式、一般化斉次法、です。
解ける二階方程式のタイプは、定係数、厳密、定数係数に変換可能な非定数係数線形斉次、
オイラーまたは等次元方程式、パラメータ変動法で解ける方程式、
独立変数または従属変数を含まなくて、順に解かれる２つの一階線形方程式に換算できる方程式、
です。


ODEを解く間、いくつかの変数が純粋に参考目的で設定されます:
`method`は、使われた解法(例えば、`linear`)を示し、
`intfactor`は、任意の使われた積分因子を示し、
`odeindex`は、ベルヌーイ法または一般化斉次法のインデックスを示し、
`yp`は、パラメータ変動手法の特殊解を示します。


初期値問題(IVP)を解くためには、
一階と二階方程式のためには関数`ic1`と`ic2`が利用可能であり、
二階境界値問題(BVP)を解くためには、
`bc2`を使うことができます。


例:












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

