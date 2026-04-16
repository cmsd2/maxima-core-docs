## makeOrders

### Function: makeOrders (indvarlist, orderlist)

Returns a list of all powers for a polynomial up to and including the arguments. 



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

where `[0, 1]` is associated with the term $b$ and `[2, 3]` with $a^2 b^3$.


To use this function write first `load("makeOrders")`.

