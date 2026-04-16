## lindstedt

### Function: Lindstedt (eq, pvar, torder, ic)

This is a first pass at a Lindstedt code.  It can solve problems
with initial conditions entered, which can be arbitrary constants,
(just not *%k1* and *%k2*) where the initial conditions on the perturbation
equations are $z[i]=0, z'[i]=0$ for $i>0$. *ic* is the list of 
initial conditions.


Problems occur when initial conditions are not given, as the constants
in the perturbation equations are the same as the zero order equation
solution.  Also, problems occur when the initial conditions for the
perturbation equations are not $z[i]=0, z'[i]=0$ for $i>0$, such as the
Van der Pol equation.


Example:


```maxima
(%i1) load("makeOrders")$

(%i2) load("lindstedt")$

(%i3) Lindstedt('diff(x,t,2)+x-(e*x^3)/6,e,2,[1,0]);
          2
         e  (cos(5 T) - 24 cos(3 T) + 23 cos(T))
(%o3) [[[---------------------------------------
                          36864
   e (cos(3 T) - cos(T))
 - --------------------- + cos(T)],
            192
          2
       7 e    e
T = (- ---- - -- + 1) t]]
       3072   16
```


To use this function write first `load("makeOrders")` and `load("lindstedt")`.

