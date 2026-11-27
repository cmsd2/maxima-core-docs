## makeOrders

<!-- category: Other -->
<!-- keywords: makeOrders -->
<!-- signatures: makeOrders(indvarlist, orderlist) -->
### Function: makeOrders (indvarlist, orderlist)

Devuelve una lista con las potencias de las variables de un polinomio término a término.



```maxima
(%i1) load("makeOrders")$

(%i2) makeOrders([a,b],[2,3]);
(%o2) [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1],
            [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]
(%i3) expand((1+a+a^2)*(1+b+b^2+b^3));
       2  3      3    3    2  2      2    2    2
(%o3) a  b  + a b  + b  + a  b  + a b  + b  + a  b + a b
                                                  2
                                           + b + a  + a + 1
```

donde `[0, 1]` se asocia al término $b$ y `[2, 3]` a $a^2 b^3$.


Antes de hacer uso de esta función ejecútese `load("makeOrders")`.

