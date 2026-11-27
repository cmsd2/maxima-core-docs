## Simetrías

<!-- category: Other -->
<!-- keywords: comp2pui -->
<!-- signatures: comp2pui(n, l) -->
### Function: comp2pui (n, l)

Realiza el paso de las funciones simétricas completas
de la lista *l* a las funciones simétricas elementales
de 0 a *n*. En caso de que la lista *l*
contenga menos de `n+1` elementos,
se completará con valores formales. 
El primer elemento de la lista *l* almacena
el cardinal del alfabeto, en caso de que exista;
en caso contrario se le da el valor *n*.





```maxima
(%i1) comp2pui (3, [4, g]);
                        2                    2
(%o1)    [4, g, 2 h2 - g , 3 h3 - g h2 + g (g  - 2 h2)]
```

<!-- category: Other -->
<!-- keywords: cont2part -->
<!-- signatures: cont2part(pc, lvar) -->
### Function: cont2part (pc, lvar)

Convierte el polinomio particionado asociado a la
forma contraída *pc*, cuyas variables
se encuentran en *lvar*.






```maxima
(%i1) pc: 2*a^3*b*x^4*y + x^5;
                           3    4      5
(%o1)                   2 a  b x  y + x
(%i2) cont2part (pc, [x, y]);
                                   3
(%o2)              [[1, 5, 0], [2 a  b, 4, 1]]
```


Otras funciones para efectuar cambios de representación son:
`contract`, `explose`, `part2cont`, `partpol`, `tcontract` y `tpartpol`.

<!-- category: Other -->
<!-- keywords: direct -->
<!-- signatures: direct([p_1, ..., p_n], y, f, [lvar_1, ..., lvar_n]) -->
### Function: direct ([p_1, ..., p_n], y, f, [lvar_1, ..., lvar_n])

Calcula la imagen directa 
(véase M. Giusti, D. Lazard et A. Valibouze, ISSAC 1988, Roma)
asociada a la función *f*, en las listas de variables
*lvar_1*, ..., *lvar_n*, y en los polinomios 
*p_1*, ..., *p_n* de una variable *y*. Si la expresión de
*f* no depende de variable alguna, no sólo es inútil
aportar esa variable, sino que también disminuyen considerablemente los
cálculos cuando la variable no se declara.









```maxima
(%i1) direct ([z^2  - e1* z + e2, z^2  - f1* z + f2],
              z, b*v + a*u, [[u, v], [a, b]]);
       2
(%o1) y  - e1 f1 y

                                 2            2             2   2
                  - 4 e2 f2 - (e1  - 2 e2) (f1  - 2 f2) + e1  f1
                + -----------------------------------------------
                                         2
(%i2) ratsimp (%);
              2                2                   2
(%o2)        y  - e1 f1 y + (e1  - 4 e2) f2 + e2 f1
(%i3) ratsimp (direct ([z^3-e1*z^2+e2*z-e3,z^2  - f1* z + f2],
              z, b*v + a*u, [[u, v], [a, b]]));
       6            5         2                        2    2   4
(%o3) y  - 2 e1 f1 y  + ((2 e1  - 6 e2) f2 + (2 e2 + e1 ) f1 ) y

                          3                               3   3
 + ((9 e3 + 5 e1 e2 - 2 e1 ) f1 f2 + (- 2 e3 - 2 e1 e2) f1 ) y

         2       2        4    2
 + ((9 e2  - 6 e1  e2 + e1 ) f2

                    2       2       2                   2    4
 + (- 9 e1 e3 - 6 e2  + 3 e1  e2) f1  f2 + (2 e1 e3 + e2 ) f1 )

  2          2                      2     3          2
 y  + (((9 e1  - 27 e2) e3 + 3 e1 e2  - e1  e2) f1 f2

                 2            2    3                5
 + ((15 e2 - 2 e1 ) e3 - e1 e2 ) f1  f2 - 2 e2 e3 f1 ) y

           2                   3           3     2   2    3
 + (- 27 e3  + (18 e1 e2 - 4 e1 ) e3 - 4 e2  + e1  e2 ) f2

         2      3                   3    2   2
 + (27 e3  + (e1  - 9 e1 e2) e3 + e2 ) f1  f2

                   2    4        2   6
 + (e1 e2 e3 - 9 e3 ) f1  f2 + e3  f1
```


Búsqueda del polinomio cuyas raíces son la suma
$a+u$ o $a$ es la raíz de 
$z^2 - e1* z + e2$ y $u$ es la raíz de
$z^2 - f1* z + f2$






```maxima
(%i1) ratsimp (direct ([z^2  - e1* z + e2, z^2  - f1* z + f2],
                          z, a + u, [[u], [a]]));
       4                    3             2
(%o1) y  + (- 2 f1 - 2 e1) y  + (2 f2 + f1  + 3 e1 f1 + 2 e2

     2   2                              2               2
 + e1 ) y  + ((- 2 f1 - 2 e1) f2 - e1 f1  + (- 2 e2 - e1 ) f1

                  2                     2            2
 - 2 e1 e2) y + f2  + (e1 f1 - 2 e2 + e1 ) f2 + e2 f1  + e1 e2 f1

     2
 + e2
```


La función `direct` acepta dos indicadores:
`elementaires` (elementales) y `puissances` (potenciales,
que es el valor por defecto) que permiten hacer la
descomposición de los polinomios simétricos que aparezcan en los 
cálculos en funciones simétricas elementales o en funciones
potenciales, respectivamente.


Funciones de `sym` utilizadas en esta función:


`multi_orbit`(por tanto `orbit`),`pui_direct`, `multi_elem`
(por tanto `elem`), `multi_pui` (por tanto `pui`), `pui2ele`, `ele2pui`
(si al indicador `direct` se le asignó `puissances`).

<!-- category: Other -->
<!-- keywords: ele2comp -->
<!-- signatures: ele2comp(m, l) -->
### Function: ele2comp (m, l)

Pasa las funciones simétricas elementales a funciones
completas, de forma similar a `comp2ele` y `comp2pui`.


Otras funciones para cambio de bases son:


`comp2ele`, `comp2pui`, `ele2pui`, `elem`, `mon2schur`, `multi_elem`,
`multi_pui`, `pui`, `pui2comp`, `pui2ele`, `puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: ele2polynome -->
<!-- signatures: ele2polynome(l, z) -->
### Function: ele2polynome (l, z)

Devuelve el polinomio en *z* en el que las
funciones simétricas elementales de las raíces
son las de la lista *l*.
`l = [n, e_1, ..., e_n]`, donde *n*
es el grado del polinomio y *e_i* la *i*-ésima función
simétrica elemental.







```maxima
(%i1) ele2polynome ([2, e1, e2], z);
                          2
(%o1)                    z  - e1 z + e2
(%i2) polynome2ele (x^7 - 14*x^5 + 56*x^3  - 56*x + 22, x);
(%o2)          [7, 0, - 14, 0, 56, 0, - 56, - 22]
(%i3) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o3)            x  - 14 x  + 56 x  - 56 x + 22
```


La función recíproca es `polynome2ele (P, z)`


Véanse también `polynome2ele` y `pui2polynome`.

<!-- category: Other -->
<!-- keywords: ele2pui -->
<!-- signatures: ele2pui(m, l) -->
### Function: ele2pui (m, l)

Pasa las funciones simétricas elementales a funciones
completas, de forma similar a `comp2ele` y `comp2comp`.


Otras funciones para cambio de bases son:


`comp2ele`, `comp2pui`, `ele2comp`, `elem`, `mon2schur`, `multi_elem`,
`multi_pui`, `pui`, `pui2comp`, `pui2ele`, `puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: elem -->
<!-- signatures: elem(ele, sym, lvar) -->
### Function: elem (ele, sym, lvar)

Descompone el polinomio simétrico *sym* con las variables
continuas de la lista *lvar* en las funciones simétricas 
elementales contenidas en la lista *ele*. 
El primer elemento de la lista *ele* almacena
el cardinal del alfabeto, en caso de que exista;
en caso contrario se le da como valor el grado del polinomio *sym*.
Si faltan valores en la lista *ele*, ésta se completará con
valores formales del tipo "ei".
El polinomio *sym* puede especificarse de tres formas diferentes:
contraído (en cuyo caso `elem` debe valer 1, que
es el valor por defecto), particionado (`elem` valdrá 3) o
extendido (por ejemplo, el polinomio completo) (en este caso, `elem`
valdrá 2). La utilización de la función `pui` se hace
siguiendo este mismo modelo.


Con un alfabeto de cardinal 3 con *e1*, la primera función
simétrica elemental valiendo 7, el polinomio simétrico de
tres variables cuya forma contraída (aquí
dependiendo solamente de dos de sus variables) es $^4-2*x*y$,
se descompone en funciones simétricas elementales:






```maxima
(%i1) elem ([3, 7], x^4 - 2*x*y, [x, y]);
(%o1) 7 (e3 - 7 e2 + 7 (49 - e2)) + 21 e3

                                         + (- 2 (49 - e2) - 2) e2


(%i2) ratsimp (%);
                              2
(%o2)             28 e3 + 2 e2  - 198 e2 + 2401
```




Otras funciones para cambio de bases son:
`comp2ele`, `comp2pui`, `ele2comp`, `ele2pui`,
`mon2schur`, `multi_elem`, `multi_pui`,
`pui`, `pui2comp`, `pui2ele`, `puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: explose -->
<!-- signatures: explose(pc, lvar) -->
### Function: explose (pc, lvar)

Devuelve el polinomio simétrico asociado a la forma
contraída *pc*. La lista *lvar*
contiene las variables.





```maxima
(%i1) explose (a*x + 1, [x, y, z]);
(%o1)                  a z + a y + a x + 1
```


Otras funciones para efectuar cambios de representación son:
`contract`, `cont2part`, `part2cont`, `partpol`, `tcontract` y `tpartpol`.

<!-- category: Other -->
<!-- keywords: kostka -->
<!-- signatures: kostka(part_1, part_2) -->
### Function: kostka (part_1, part_2)

Función escrita por P. Espert, calcula el número de Kostka
asociado a las particiones *part_1* y *part_2*.





```maxima
(%i1) kostka ([3, 3, 3], [2, 2, 2, 1, 1, 1]);
(%o1)                           6
```

<!-- category: Other -->
<!-- keywords: lgtreillis -->
<!-- signatures: lgtreillis(n, m) -->
### Function: lgtreillis (n, m)

Devuelve la lista de particiones de peso *n* y longitud *m*.





```maxima
(%i1) lgtreillis (4, 2);
(%o1)                   [[3, 1], [2, 2]]
```


Véanse también `ltreillis`, `treillis` y `treinat`.

<!-- category: Other -->
<!-- keywords: ltreillis -->
<!-- signatures: ltreillis(n, m) -->
### Function: ltreillis (n, m)

Devuelve la lista de particiones de peso *n* y longitud 
menor o igual que *m*.





```maxima
(%i1) ltreillis (4, 2);
(%o1)               [[4, 0], [3, 1], [2, 2]]
```


Véanse tambiént `lgtreillis`, `treillis` y `treinat`.

<!-- category: Other -->
<!-- keywords: mon2schur -->
<!-- signatures: mon2schur(l) -->
### Function: mon2schur (l)

La lista *l* representa la función de Schur S_*l*:
Se tiene *l* = [*i_1*, *i_2*, ..., *i_q*]
con *i_1* <= *i_2* <= ... <= *i_q*.
La función de Schur es S_[*i_1*, *i_2*, ..., *i_q*],
el menor de la matriz infinita (h_{i-j}) *i* >= 1, *j* >= 1
compuesto de las *q* primeras filas y columnas 
*i_1* + 1, *i_2* + 2, ..., *i_q* + *q*.


Se ha escrito esta función de Schur en función de las
formas monomiales utilizando las funciones `treinat` y `kostka`.
La forma devuelta es un polinomio simétrico en una de sus representaciones
contraídas con las variables *x_1*, *x_2*, ...

 





```maxima
(%i1) mon2schur ([1, 1, 1]);
(%o1)                       x1 x2 x3


(%i2) mon2schur ([3]);
                                  2        3
(%o2)                x1 x2 x3 + x1  x2 + x1


(%i3) mon2schur ([1, 2]);
                                      2
(%o3)                  2 x1 x2 x3 + x1  x2
```



Para 3 variables se tendrá:




```maxima
2 x1 x2 x3 + x1^2 x2 + x2^2 x1 + x1^2 x3 + x3^2 x1
    + x2^2 x3 + x3^2 x2
```


Otras funciones para cambio de bases son:


`comp2ele`, `comp2pui`, `ele2comp`, `ele2pui`, `elem`, `multi_elem`,
`multi_pui`, `pui`, `pui2comp`, `pui2ele`, `puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: multi_elem -->
<!-- signatures: multi_elem(l_elem, multi_pc, l_var) -->
### Function: multi_elem (l_elem, multi_pc, l_var)

Descompone un polinomio multisimétrico sobre una forma
multicontraída *multi_pc* en los grupos de
variables contenidas en la lista de listas  *l_var* sobre los
grupos de funciones simétricas elementales contenidas en *l_elem*.






```maxima
(%i1) multi_elem ([[2, e1, e2], [2, f1, f2]], a*x + a^2 + x^3,
      [[x, y], [a, b]]);
                                                  3
(%o1)         - 2 f2 + f1 (f1 + e1) - 3 e1 e2 + e1


(%i2) ratsimp (%);
                         2                       3
(%o2)         - 2 f2 + f1  + e1 f1 - 3 e1 e2 + e1
```



Otras funciones para cambio de bases son:


`comp2ele`, `comp2pui`, `ele2comp`, `ele2pui`, `elem`,
`mon2schur`, `multi_pui`, `pui`, `pui2comp`, `pui2ele`,
`puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: multi_orbit -->
<!-- signatures: multi_orbit(P, [lvar_1, lvar_2, ..., lvar_p]) -->
### Function: multi_orbit (P, [lvar_1, lvar_2, ..., lvar_p])

*P* es un polinomio en el conjunto de variables contenidas 
en las listas *lvar_1*, *lvar_2*, ..., *lvar_p*.
Esta función restablece la órbita del polinomio *P* sobre la
acción del producto de los grupos simétricos de los conjuntos de
variables representadas por esas *p* listas.






```maxima
(%i1) multi_orbit (a*x + b*y, [[x, y], [a, b]]);
(%o1)                [b y + a x, a y + b x]


(%i2) multi_orbit (x + y + 2*a, [[x, y], [a, b, c]]);
(%o2)        [y + x + 2 c, y + x + 2 b, y + x + 2 a]
```



Véase también `orbit` para la acción de un solo grupo simérico.

<!-- category: Other -->
<!-- keywords: multi_pui -->
<!-- signatures: multi_pui -->
### Function: multi_pui

Es a la función `pui` lo que la función `multi_elem` es
a la función `elem`.





```maxima
(%i1) multi_pui ([[2, p1, p2], [2, t1, t2]], a*x + a^2 + x^3,
      [[x, y], [a, b]]);
                                            3
                                3 p1 p2   p1
(%o1)              t2 + p1 t1 + ------- - ---
                                   2       2
```

<!-- category: Other -->
<!-- keywords: multinomial -->
<!-- signatures: multinomial(r, part) -->
### Function: multinomial (r, part)

El argumento *r* es el peso de la partición *part*.
Esta función calcula el coeficiente multinomial asociado: si
las partes de las particiones *part* son 
*i_1*, *i_2*, ..., *i_k*, el resultado de `multinomial`
es `r!/(i_1! i_2! ... i_k!)`.

<!-- category: Other -->
<!-- keywords: multsym -->
<!-- signatures: multsym(ppart_1, ppart_2, n) -->
### Function: multsym (ppart_1, ppart_2, n)

Calcula el producto de dos polinomios simétricos de *n* variables
operando solamente con el módulo de la acción del grupo
simétrico de orden *n*. Los polinomios están en su 
representación particionada.


Sean los dos polinomios simétricos en `x` e `y`:
`3*(x + y) + 2*x*y` y `5*(x^2 + y^2)`
cuyas formas particionadas son `[[3, 1], [2, 1, 1]]` y `[[5, 2]]`,
respectivamente; el producto de ambos será:





```maxima
(%i1) multsym ([[3, 1], [2, 1, 1]], [[5, 2]], 2);
(%o1)         [[10, 3, 1], [15, 3, 0], [15, 2, 1]]
```



o sea, `10*(x^3*y + y^3*x) + 15*(x^2*y + y^2*x) + 15*(x^3 + y^3)`.


Funciones de cambio de representación de un polinomio simétrico:


`contract`, `cont2part`, `explose`, `part2cont`,
`partpol`, `tcontract` y `tpartpol`.

<!-- category: Other -->
<!-- keywords: orbit -->
<!-- signatures: orbit(P, lvar) -->
### Function: orbit (P, lvar)

Calcula la órbita de un polinomio *P* en las variables de 
la lista *lvar* bajo la acción del grupo simétrico del
conjunto de variables contenidas en la lista *lvar*.

 




```maxima
(%i1) orbit (a*x + b*y, [x, y]);
(%o1)                [a y + b x, b y + a x]


(%i2) orbit (2*x + x^2, [x, y]);
                        2         2
(%o2)                 [y  + 2 y, x  + 2 x]
```


Véase también `multi_orbit` para la acción de un producto
de grupos simétricos sobre un polinomio.

<!-- category: Other -->
<!-- keywords: part2cont -->
<!-- signatures: part2cont(ppart, lvar) -->
### Function: part2cont (ppart, lvar)

Transforma un polinomio simétrico de su forma particionada a
su forma contraída. La forma contraída
se devuelve con las variables contenidas en *lvar*.





```maxima
(%i1) part2cont ([[2*a^3*b, 4, 1]], [x, y]);
                              3    4
(%o1)                      2 a  b x  y
```



Otras funciones para efectuar cambios de representación son:


`contract`, `cont2part`, `explose`, `partpol`, `tcontract` y `tpartpol`.

<!-- category: Other -->
<!-- keywords: partpol -->
<!-- signatures: partpol(psym, lvar) -->
### Function: partpol (psym, lvar)

Restablece la representación particionada del polinomio
simétrico *psym* de variables en *lvar*.





```maxima
(%i1) partpol (-a*(x + y) + 3*x*y, [x, y]);
(%o1)               [[3, 1, 1], [- a, 1, 0]]
```



Otras funciones para efectuar cambios de representación son:


`contract`, `cont2part`, `explose`, `part2cont`, `tcontract` y `tpartpol`.

<!-- category: Other -->
<!-- keywords: permut -->
<!-- signatures: permut(l) -->
### Function: permut (l)

Devuelve la lista de permutaciones de la lista *l*.

<!-- category: Other -->
<!-- keywords: polynome2ele -->
<!-- signatures: polynome2ele(P, x) -->
### Function: polynome2ele (P, x)

Devuelve la lista `l = [n, e_1, ..., e_n]`,
en la que *n* es el grado del polinomio *P* de variable *x*
y *e_i* es la *i*-ésima función simétrica elemental de las
raíces de *P*.






```maxima
(%i1) polynome2ele (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x);
(%o1)          [7, 0, - 14, 0, 56, 0, - 56, - 22]


(%i2) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o2)            x  - 14 x  + 56 x  - 56 x + 22
```



La función recíproca es `ele2polynome (l, x)`.

<!-- category: Other -->
<!-- keywords: prodrac -->
<!-- signatures: prodrac(l, k) -->
### Function: prodrac (l, k)

Siendo *l* una lista que contiene las funciones simétricas
elementales sobre un conjunto *A*, la función `prodrac`
calcula el polinomio cuyas raíces son los productos 
*k* a *k* de los elementos de *A*.

<!-- category: Other -->
<!-- keywords: pui -->
<!-- signatures: pui(l, sym, lvar) -->
### Function: pui (l, sym, lvar)

Descompone el polinomio simétrico *sym*, cuyas variables
son las contenidas en *lvar*, en las funciones potenciales
contenidas en la lista *l*.
El primer elemento de la lista *l* almacena
el cardinal del alfabeto, en caso de que exista;
en caso contrario se le da el grado del polinomio *sym*.
Si faltan los valores de la lista *l*, en su lugar serán
colocados valores formales del tipo "pi". 
El polinomio *sym* puede especificarse de tres formas diferentes:
contraído (en cuyo caso `pui` debe valer 1, que
es el valor por defecto), particionado (`pui` valdrá 3) o
extendido (por ejemplo, el polinomio completo) (en este caso, `pui`
valdrá 2). La utilización de la función `elem` se hace
siguiendo este mismo modelo.







```maxima
(%i1) pui;
(%o1)                           1


(%i2) pui ([3, a, b], u*x*y*z, [x, y, z]);
                       2
                   a (a  - b) u   (a b - p3) u
(%o2)              ------------ - ------------
                        6              3


(%i3) ratsimp (%);
                                       3
                      (2 p3 - 3 a b + a ) u
(%o3)                 ---------------------
                                6
```



Otras funciones para cambio de bases son:
`comp2ele`, `comp2pui`, `ele2comp`, `ele2pui`, `elem`, `mon2schur`,
`multi_elem`, `multi_pui`, `pui2comp`, `pui2ele`, `puireduc` y
`schur2comp`.

<!-- category: Other -->
<!-- keywords: pui2comp -->
<!-- signatures: pui2comp(n, lpui) -->
### Function: pui2comp (n, lpui)

Devuelve la lista de las *n* primeras funciones completas
(con el cardinal en primer lugar) en función de las funciones
potenciales dadas en la lista *lpui*. Si la lista *lpui*
estuviese vacía, el cardinal sería *N*;
si no estuviese vacía, se tomaría como
cardinal su primer elemento, de forma similar a como se procede en
`comp2ele` y en `comp2pui`.







```maxima
(%i1) pui2comp (2, []);
                                       2
                                p2 + p1
(%o1)                   [2, p1, --------]
                                   2


(%i2) pui2comp (3, [2, a1]);
                                            2
                                 a1 (p2 + a1 )
                         2  p3 + ------------- + a1 p2
                  p2 + a1              2
(%o2)     [2, a1, --------, --------------------------]
                     2                  3


(%i3) ratsimp (%);
                            2                     3
                     p2 + a1   2 p3 + 3 a1 p2 + a1
(%o3)        [2, a1, --------, --------------------]
                        2               6
```



Otras funciones para cambio de bases son:
`comp2ele`, `comp2pui`, `ele2comp`, `ele2pui`, `elem`,
`mon2schur`, `multi_elem`, `multi_pui`, `pui`, `pui2ele`,
`puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: pui2ele -->
<!-- signatures: pui2ele(n, lpui) -->
### Function: pui2ele (n, lpui)

Transforma las funciones potenciales a funciones simétricas
elementales. Si la variable global `pui2ele` vale `girard`,
se recupera la lista de funciones simétricas elementales de 1 *n*,
y si es igual a `close`, se recupera la *n*-ésima 
función simétrica elemental.


Otras funciones para cambio de bases son:
`comp2ele`, `comp2pui`, `ele2comp`, `ele2pui`, `elem`,
`mon2schur`, `multi_elem`, `multi_pui`, `pui`, `pui2comp`,
`puireduc` y `schur2comp`.

<!-- category: Other -->
<!-- keywords: pui2polynome -->
<!-- signatures: pui2polynome(x, lpui) -->
### Function: pui2polynome (x, lpui)

Calcula el polinomio en *x* cuyas raíces tienen
como funciones potenciales las dadas en la lista *lpui*.







```maxima
(%i1) pui;
(%o1)                           1


(%i2) kill(labels);
(%o0)                         done


(%i1) polynome2ele (x^3 - 4*x^2 + 5*x - 1, x);
(%o1)                     [3, 4, 5, 1]


(%i2) ele2pui (3, %);
(%o2)                     [3, 4, 6, 7]


(%i3) pui2polynome (x, %);
                        3      2
(%o3)                  x  - 4 x  + 5 x - 1
```


Véanse también `polynome2ele` y `ele2polynome`.

<!-- category: Other -->
<!-- keywords: pui_direct -->
<!-- signatures: pui_direct(orbite, [lvar_1, ..., lvar_n], [d_1, d_2, ..., d_n]) -->
### Function: pui_direct (orbite, [lvar_1, ..., lvar_n], [d_1, d_2, ..., d_n])

Sea *f* un polinomio en *n* bloques de variables *lvar_1*, ..., *lvar_n*.
Sea *c_i* el número de variables en *lvar_i* y *SC* el
producto de los *n* grupos simétricos de grados *c_1*, ..., *c_n*,
que actúan sobre *f*.
La lista *orbite* es la órbita, representada por `SC(f)`,
de la función *f* sobre la acción de *SC*, la cual puede ser
obtenida por medio de la función `multi_orbit`.
Los valores `d_i` son enteros tales que 
*c_1* <= *d_1*, *c_2* <= *d_2*, ..., *c_n* <= *d_n*.
Por último, sea *SD* el producto de los grupos simétricos
*S_d1* x *S_d2* x ... x *S_dn*.


La función `pui_direct` devuelve las *n* primeras
funciones potenciales de `SD(f)` deducidas de 
las funciones potenciales de `SC(f)`, siendo 
*n* el cardinal de `SD(f)`.


El resultado se devuelve en la forma multicontraída
respecto de *SD*.








```maxima
(%i1) l: [[x, y], [a, b]];
(%o1)                   [[x, y], [a, b]]


(%i2) pui_direct (multi_orbit (a*x + b*y, l), l, [2, 2]);
                                       2  2
(%o2)               [a x, 4 a b x y + a  x ]


(%i3) pui_direct (multi_orbit (a*x + b*y, l), l, [3, 2]);
                             2  2     2    2        3  3
(%o3) [2 a x, 4 a b x y + 2 a  x , 3 a  b x  y + 2 a  x , 

    2  2  2  2      3    3        4  4
12 a  b  x  y  + 4 a  b x  y + 2 a  x , 

    3  2  3  2      4    4        5  5
10 a  b  x  y  + 5 a  b x  y + 2 a  x , 

    3  3  3  3       4  2  4  2      5    5        6  6
40 a  b  x  y  + 15 a  b  x  y  + 6 a  b x  y + 2 a  x ]


(%i4) pui_direct ([y + x + 2*c, y + x + 2*b, y + x + 2*a],
      [[x, y], [a, b, c]], [2, 3]);
                             2              2
(%o4) [3 x + 2 a, 6 x y + 3 x  + 4 a x + 4 a , 

                 2                   3        2       2        3
              9 x  y + 12 a x y + 3 x  + 6 a x  + 12 a  x + 8 a ]
```

<!-- category: Other -->
<!-- keywords: puireduc -->
<!-- signatures: puireduc(n, lpui) -->
### Function: puireduc (n, lpui)

Siendo *lpui* una lista en la que el primer elemento es
un entero *m*, `puireduc` devuelve las *n* primeras 
funciones potenciales en función de las *m* primeras.





```maxima
(%i1) puireduc (3, [2]);
                                         2
                                   p1 (p1  - p2)
(%o1)          [2, p1, p2, p1 p2 - -------------]
                                         2


(%i2) ratsimp (%);
                                           3
                               3 p1 p2 - p1
(%o2)              [2, p1, p2, -------------]
                                     2
```

<!-- category: Other -->
<!-- keywords: resolvante -->
<!-- signatures: resolvante(P, x, f, [x_1, ..., x_d]) -->
### Function: resolvante (P, x, f, [x_1, ..., x_d])

Calcula la resolvente del polinomio *P* de variable *x* y
grado *n* >= *d* por la función *f* de variables
*x_1*, ..., *x_d*. 
Para mejorar los cálculos, es importante no incluir en la lista
`[x_1, ..., x_d]` las variables que no intervienen
en la función de transformación *f*.


Con el fin de hacer más eficaces los cálculos, se puede asignar a
`resolvante` un indicador que permita seleccionar el algoritmo
más apropiado:





- *
  
`unitaire`,
- *
  
`lineaire`,
- *
  
`alternee`,
- *
  
`somme`,
- *
  
`produit`,
- *
  
`cayley`,
- *
  
`generale`.

























```maxima
(%i1) resolvante: unitaire$

(%i2) resolvante (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x, x^3 - 1,
      [x]);

" resolvante unitaire " [7, 0, 28, 0, 168, 0, 1120, - 154, 7840,
                         - 2772, 56448, - 33880, 

413952, - 352352, 3076668, - 3363360, 23114112, - 30494464, 

175230832, - 267412992, 1338886528, - 2292126760] 
  3       6      3       9      6      3
[x  - 1, x  - 2 x  + 1, x  - 3 x  + 3 x  - 1, 

 12      9      6      3       15      12       9       6      3
x   - 4 x  + 6 x  - 4 x  + 1, x   - 5 x   + 10 x  - 10 x  + 5 x

       18      15       12       9       6      3
 - 1, x   - 6 x   + 15 x   - 20 x  + 15 x  - 6 x  + 1, 

 21      18       15       12       9       6      3
x   - 7 x   + 21 x   - 35 x   + 35 x  - 21 x  + 7 x  - 1] 
[- 7, 1127, - 6139, 431767, - 5472047, 201692519, - 3603982011] 
       7      6        5         4          3           2
(%o2) y  + 7 y  - 539 y  - 1841 y  + 51443 y  + 315133 y

                                              + 376999 y + 125253

(%i3) resolvante: lineaire$

(%i4) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3]);

" resolvante lineaire " 
       24       20         16            12             8
(%o4) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000

(%i5) resolvante: general$

(%i6) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3]);

" resolvante generale " 
       24       20         16            12             8
(%o6) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000


(%i7) resolvante (x^4 - 1, x, x1 + 2*x2 + 3*x3, [x1, x2, x3, x4]);

" resolvante generale " 
       24       20         16            12             8
(%o7) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000


(%i8) direct ([x^4 - 1], x, x1 + 2*x2 + 3*x3, [[x1, x2, x3]]);
       24       20         16            12             8
(%o8) y   + 80 y   + 7520 y   + 1107200 y   + 49475840 y

                                                    4
                                       + 344489984 y  + 655360000

(%i9) resolvante :lineaire$

(%i10) resolvante (x^4 - 1, x, x1 + x2 + x3, [x1, x2, x3]);

" resolvante lineaire " 
                              4
(%o10)                       y  - 1

(%i11) resolvante: symetrique$

(%i12) resolvante (x^4 - 1, x, x1 + x2 + x3, [x1, x2, x3]);

" resolvante symetrique " 
                              4
(%o12)                       y  - 1


(%i13) resolvante (x^4 + x + 1, x, x1 - x2, [x1, x2]);

" resolvante symetrique " 
                           6      2
(%o13)                    y  - 4 y  - 1

(%i14) resolvante: alternee$

(%i15) resolvante (x^4 + x + 1, x, x1 - x2, [x1, x2]);

" resolvante alternee " 
            12      8       6        4        2
(%o15)     y   + 8 y  + 26 y  - 112 y  + 216 y  + 229

(%i16) resolvante: produit$

(%i17) resolvante (x^7 - 7*x + 3, x, x1*x2*x3, [x1, x2, x3]);

" resolvante produit "
        35      33         29        28         27        26
(%o17) y   - 7 y   - 1029 y   + 135 y   + 7203 y   - 756 y

         24           23          22            21           20
 + 1323 y   + 352947 y   - 46305 y   - 2463339 y   + 324135 y

          19           18             17              15
 - 30618 y   - 453789 y   - 40246444 y   + 282225202 y

             14              12             11            10
 - 44274492 y   + 155098503 y   + 12252303 y   + 2893401 y

              9            8            7             6
 - 171532242 y  + 6751269 y  + 2657205 y  - 94517766 y

            5             3
 - 3720087 y  + 26040609 y  + 14348907

(%i18) resolvante: symetrique$

(%i19) resolvante (x^7 - 7*x + 3, x, x1*x2*x3, [x1, x2, x3]);

" resolvante symetrique " 
        35      33         29        28         27        26
(%o19) y   - 7 y   - 1029 y   + 135 y   + 7203 y   - 756 y

         24           23          22            21           20
 + 1323 y   + 352947 y   - 46305 y   - 2463339 y   + 324135 y

          19           18             17              15
 - 30618 y   - 453789 y   - 40246444 y   + 282225202 y

             14              12             11            10
 - 44274492 y   + 155098503 y   + 12252303 y   + 2893401 y

              9            8            7             6
 - 171532242 y  + 6751269 y  + 2657205 y  - 94517766 y

            5             3
 - 3720087 y  + 26040609 y  + 14348907

(%i20) resolvante: cayley$

(%i21) resolvante (x^5 - 4*x^2 + x + 1, x, a, []);

" resolvante de Cayley "
        6       5         4          3            2
(%o21) x  - 40 x  + 4080 x  - 92928 x  + 3772160 x  + 37880832 x

                                                       + 93392896
```


Para la resolvente de Cayley, los dos últimos argumentos son neutros
y el polinomio dado en el argumento debe ser necesariamente de grado 5.


Véanse también:


`resolvante_bipartite`, `resolvante_produit_sym`,
`resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, 
`resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_alternee1 -->
<!-- signatures: resolvante_alternee1(P, x) -->
### Function: resolvante_alternee1 (P, x)

Calcula la transformación de `P(x)` de
grado *n* por la función $\prod_{1\leq i<j\leq n-1} (x_i-x_j)$.



Véanse también:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante` , `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_bipartite`.

<!-- category: Other -->
<!-- keywords: resolvante_bipartite -->
<!-- signatures: resolvante_bipartite(P, x) -->
### Function: resolvante_bipartite (P, x)

Calcula la transformación de 
`P(x)` de grado *n* (*n* par) por la función 
$x_1x_2\ldots x_{n/2}+x_{n/2+1}\ldotsx_n$





```maxima
(%i1) resolvante_bipartite (x^6 + 108, x);
              10        8           6             4
(%o1)        y   - 972 y  + 314928 y  - 34012224 y
```



Véanse también:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_alternee1`.

<!-- category: Other -->
<!-- keywords: resolvante_diedrale -->
<!-- signatures: resolvante_diedrale(P, x) -->
### Function: resolvante_diedrale (P, x)

Calcula la transformación de
`P(x)` por la función `x_1 x_2 + x_3 x_4`.





```maxima
(%i1) resolvante_diedrale (x^5 - 3*x^4 + 1, x);
       15       12       11       10        9         8         7
(%o1) x   - 21 x   - 81 x   - 21 x   + 207 x  + 1134 x  + 2331 x

        6         5          4          3          2
 - 945 x  - 4970 x  - 18333 x  - 29079 x  - 20745 x  - 25326 x

 - 697
```



Véanse también:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante`.

<!-- category: Other -->
<!-- keywords: resolvante_klein -->
<!-- signatures: resolvante_klein(P, x) -->
### Function: resolvante_klein (P, x)

Calcula la transformación de
`P(x)` por la función `x_1 x_2 x_4 + x_4`.


Véanse también:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_klein3 -->
<!-- signatures: resolvante_klein3(P, x) -->
### Function: resolvante_klein3 (P, x)

Calcula la transformación de
`P(x)` por la función `x_1 x_2 x_4 + x_4`.


Véanse también:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante`,
`resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_produit_sym -->
<!-- signatures: resolvante_produit_sym(P, x) -->
### Function: resolvante_produit_sym (P, x)

Calcula la lista de todas las resolventes producto
del polinomio `P(x)`.







```maxima
(%i1) resolvante_produit_sym (x^5 + 3*x^4 + 2*x - 1, x);
        5      4             10      8       7       6       5
(%o1) [y  + 3 y  + 2 y - 1, y   - 2 y  - 21 y  - 31 y  - 14 y

    4       3      2       10      8       7    6       5       4
 - y  + 14 y  + 3 y  + 1, y   + 3 y  + 14 y  - y  - 14 y  - 31 y

       3      2       5      4
 - 21 y  - 2 y  + 1, y  - 2 y  - 3 y - 1, y - 1]

(%i2) resolvante: produit$

(%i3) resolvante (x^5 + 3*x^4 + 2*x - 1, x, a*b*c, [a, b, c]);

" resolvante produit "
       10      8       7    6        5       4       3     2
(%o3) y   + 3 y  + 14 y  - y  - 14 y  - 31 y  - 21 y  - 2 y  + 1
```






Véanse también:


`resolvante`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`,
`resolvante_klein3`, `resolvante_vierer`,
`resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_unitaire -->
<!-- signatures: resolvante_unitaire(P, Q, x) -->
### Function: resolvante_unitaire (P, Q, x)

Calcula la resolvente del polinomio `P(x)` 
por el polinomio `Q(x)`.


Véanse también:


`resolvante_produit_sym`, `resolvante`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_vierer -->
<!-- signatures: resolvante_vierer(P, x) -->
### Function: resolvante_vierer (P, x)

Calcula la transformación de
`P(x)` por la función `x_1 x_2 - x_3 x_4`.


Véanse también:


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: schur2comp -->
<!-- signatures: schur2comp(P, l_var) -->
### Function: schur2comp (P, l_var)

*P* es un polinomio de variables contenidas en
la lista *l_var*. Cada una de las variables de *l_var*
representa una función simétrica completa. 
La *i*-ésima función simétrica completa de *l_var*
se representa como la concatenación de la letra `h` con el
entero *i*: `hi`.
La función `schur2comp` devuelve la expresión de *P*
en función de las funciones de Schur.






```maxima
(%i1) schur2comp (h1*h2 - h3, [h1, h2, h3]);
(%o1)                         s
                               1, 2


(%i2) schur2comp (a*h3, [h3]);
(%o2)                         s  a
                               3
```

<!-- category: Other -->
<!-- keywords: somrac -->
<!-- signatures: somrac(l, k) -->
### Function: somrac (l, k)

Si la lista *l* contiene las funciones simétricas elementales de
un polinomio *P*, la función `somrac` calcula el polinomio cuyas
raíces son las sumas *k* a *k* de las raíces
de *P*. 


Véase también `prodrac`.

<!-- category: Other -->
<!-- keywords: tcontract -->
<!-- signatures: tcontract(pol, lvar) -->
### Function: tcontract (pol, lvar)

Comprueba si el polinomio *pol* es simétrico en las
variable contenidas en la lista *lvar*. En caso afirmativo,
devuelve una forma contraída tal como lo hace la
función `contract`.


Otras funciones para efectuar cambios de representación son:
`contract`, `cont2part`, `explose`, `part2cont`, `partpol` y `tpartpol`.

<!-- category: Other -->
<!-- keywords: tpartpol -->
<!-- signatures: tpartpol(pol, lvar) -->
### Function: tpartpol (pol, lvar)

Comprueba si el polinomio *pol* es simétrico en las
variable contenidas en la lista *lvar*. En caso afirmativo,
devuelve una forma particionada tal como lo hace la
función `partpol`.


Otras funciones para efectuar cambios de representación son:
`contract`, `cont2part`, `explose`, `part2cont`, `partpol` y `tcontract`.

<!-- category: Other -->
<!-- keywords: treillis -->
<!-- signatures: treillis(n) -->
### Function: treillis (n)

Devuelve todas las particiones de pesos *n*.





```maxima
(%i1) treillis (4);
(%o1)    [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
```



Véanse también `lgtreillis`, `ltreillis` y `treinat`.

<!-- category: Other -->
<!-- keywords: treinat -->
<!-- signatures: treinat(part) -->
### Function: treinat (part)

Devuelve la lista de las particiones inferiores de la partición
*part* en su orden natural.







```maxima
(%i1) treinat ([5]);
(%o1)                         [[5]]


(%i2) treinat ([1, 1, 1, 1, 1]);
(%o2) [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], 

                                                 [1, 1, 1, 1, 1]]


(%i3) treinat ([3, 2]);
(%o3)                 [[5], [4, 1], [3, 2]]
```



Véanse también `lgtreillis`, `ltreillis` y `treillis`.

