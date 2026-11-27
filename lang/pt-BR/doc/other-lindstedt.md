## lindstedt

<!-- category: Other -->
<!-- keywords: Lindstedt -->
<!-- signatures: Lindstedt(eq, pvar, torder, ic) -->
### Function: Lindstedt (eq, pvar, torder, ic)

Esse é um primeiro passo para um código de Lindstedt.  Esse código pode resolver problemas
com condições iniciais fornecidas, às quais podem ser constantes arbitrárias,
(não apenas *%k1* e *%k2*) onde as condições iniciais sobre as equações
de perturbação são $z[i]=0, z'[i]=0$ para $i>0$. *ic* é a lista de 
condições iniciais.


Problemas ocorrem quando condições iniciais não forem dadas, como as constantes
nas equações de perturbação são as mesmas que a solução da equação de
ordem zero.  Também, problemas ocorrem quando as condições iniciais para as
equações de perturbação não são $z[i]=0, z'[i]=0$ para $i>0$, tais como a
equação de Van der Pol.


Exemplo:


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


Para usar essa função escreva primeiro `load("makeOrders")` e `load("lindstedt")`.

