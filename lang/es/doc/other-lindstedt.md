## lindstedt

<!-- category: Other -->
<!-- keywords: Lindstedt -->
<!-- signatures: Lindstedt(eq, pvar, torder, ic) -->
### Function: Lindstedt (eq, pvar, torder, ic)

Este es el primer paso hacia un programa para resolver ecuaciones de Lindstedt.
Puede resolver problemas con condiciones iniciales, las cuales pueden ser
constantes arbitrarias (no pueden usarse *%k1* ni *%k2*) donde las condiciones iniciales sobre las ecuaciones de perturbación son $z[i]=0, z'[i]=0$ para $i>0$.
El argumento *ic* es la lista de condiciones iniciales.


Ejemplo:


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


Antes de hacer uso de esta función ejecútense  `load("makeOrders")` y `load("lindstedt")`.

