## Simetrias

<!-- category: Other -->
<!-- keywords: comp2pui -->
<!-- signatures: comp2pui(n, L) -->
### Function: comp2pui (n, L)

implementa a passagem das funções simétricas completamente simétricas fornecidas na lista
*L* para as funções simétricas elementares de 0 a *n*. Se a
lista *L* contiver menos que *n+1* elementos, será completada com
valores formais do tipo *h1*, *h2*, etc. Se o primeiro elemento
da lista *L* existir, ele é interpretado como sendo o tamanho do alfabeto,
de outra forma o tamanho é escolhido para *n*.





```maxima
(%i1) comp2pui (3, [4, g]);
                        2                    2
(%o1)    [4, g, 2 h2 - g , 3 h3 - g h2 + g (g  - 2 h2)]
```

<!-- category: Other -->
<!-- keywords: cont2part -->
<!-- signatures: cont2part(pc, lvar) -->
### Function: cont2part (pc, lvar)

Retorna o polinômio particionado associado 
à forma contraída *pc* cujas variáveis estão em *lvar*.






```maxima
(%i1) pc: 2*a^3*b*x^4*y + x^5;
                           3    4      5
(%o1)                   2 a  b x  y + x
(%i2) cont2part (pc, [x, y]);
                                   3
(%o2)              [[1, 5, 0], [2 a  b, 4, 1]]
```

<!-- category: Other -->
<!-- keywords: direct -->
<!-- signatures: direct([p_1, ..., p_n], y, f, [lvar_1, ..., lvar_n]) -->
### Function: direct ([p_1, ..., p_n], y, f, [lvar_1, ..., lvar_n])

calcula a imagem direta (see M. Giusti, D. Lazard et A. Valibouze,
ISSAC 1988, Rome) associada à função *f*, na lista de
variáveis *lvar_1*, ..., *lvar_n*, e nos polinômios
*p_1*, ..., *p_n* na variável *y*.  A quantidade de argumetnos que a
funçào *f* pode receber é importante para o cálculo.  Dessa forma, se a
expressão para *f* não depende de alguma variável, é inútil
incluir essa variável, e não incluir essa variável irá também reduzir
consideravelmente o montante cálculos efetuados.









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


Encontrando um polinômio cujas raízes são somatórios $a+u$ onde $a$
é uma raíz de $z^2 - e_1 z + e_2$ e $u$ é uma raíz de $z^2 - +f_1 z + f_2$.






```maxima
(%i1) ratsimp (direct ([z^2 - e1* z + e2, z^2 - f1* z + f2],
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


`direct` aceita dois sinalizadores: `elementaires` (elementares) e
`puissances` (exponenciais - valor padrão) que permitem a decomposição
de polinômios simétricos que aparecerem nesses cálculos em
funções simétricas elementares ou em funções exponenciais respectivamente.


Funções de `sym` utilizadas nesta função :


`multi_orbit` (portanto `orbit`), `pui_direct`, `multi_elem`
(portanto `elem`), `multi_pui` (portanto `pui`), `pui2ele`, `ele2pui`
(se o sinalizador `direct` for escolhido para `puissances`).

<!-- category: Other -->
<!-- keywords: ele2comp -->
<!-- signatures: ele2comp(m, L) -->
### Function: ele2comp (m, L)

Vai de funções simétricas elementares para funções completas.
Similar a `comp2ele` e a `comp2pui`.


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: ele2polynome -->
<!-- signatures: ele2polynome(L, z) -->
### Function: ele2polynome (L, z)

retorna o polinômio em *z* de forma que as funções elementares
simétricas de suas raízes estejam na lista `L = [n, e_1, ..., e_n]`, onde *n* é o grau dos
polinômios e *e_i* é a *i*-ésima função simétrica elementar.







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


o inverso: `polynome2ele (P, z)`.

 

Veja também:
`polynome2ele`, `pui2polynome`.

<!-- category: Other -->
<!-- keywords: ele2pui -->
<!-- signatures: ele2pui(m, L) -->
### Function: ele2pui (m, L)

vai de funções simétricas elementares para as funções completas.
Similar a `comp2ele` e `comp2pui`.


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: elem -->
<!-- signatures: elem(ele, sym, lvar) -->
### Function: elem (ele, sym, lvar)

decompõe o polinômio simétrico *sym*, nas variáveis
contidas na lista *lvar*, em termos de funções elementares
simétricas fornecidas na lista *ele*.  Se o primeiro elemento de
*ele* for fornecido, esse primeiro elemento será o tamanho do alfabeto, de outra forma o
tamanho será o grau do polinômio *sym*.  Se valores forem
omitidos na lista *ele*, valores formais do tipo *e1*,
*e2*, etc. serão adicionados.  O polinômio *sym* pode ser fornecido de
três diferentes formas: contraída (`elem` pode então ser 1, seu
valor padrão), particionada (`elem` pode ser 3), ou extendida
(i.e. o polinômio completo, e `elem` pode então ser 2).  A
função `pui` é usada então da mesma forma.


sobre um alfabeto de tamanho 3 com *e1*, a primeira funçào elementar
simétrica, com valor 7, o polinômio simétrico em 3 variáveis cuja
forma contraída (que aqui depende de duas de suas variáveis) é
*x^4-2*x*y* decomposto como segue em funções elementares simétricas:






```maxima
(%i1) elem ([3, 7], x^4 - 2*x*y, [x, y]);
(%o1) 7 (e3 - 7 e2 + 7 (49 - e2)) + 21 e3

                                         + (- 2 (49 - e2) - 2) e2
(%i2) ratsimp (%);
                              2
(%o2)             28 e3 + 2 e2  - 198 e2 + 2401
```



Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: explose -->
<!-- signatures: explose(pc, lvar) -->
### Function: explose (pc, lvar)

retorna o polinômio simétrico associado com a forma contraída
*pc*. A lista *lvar* conté as variáveis.





```maxima
(%i1) explose (a*x + 1, [x, y, z]);
(%o1)                  a z + a y + a x + 1
```

<!-- category: Other -->
<!-- keywords: kostka -->
<!-- signatures: kostka(part_1, part_2) -->
### Function: kostka (part_1, part_2)

escrita por P. Esperet, calcula o número de Kostka da partição
*part_1* e *part_2*.





```maxima
(%i1) kostka ([3, 3, 3], [2, 2, 2, 1, 1, 1]);
(%o1)                           6
```

<!-- category: Other -->
<!-- keywords: lgtreillis -->
<!-- signatures: lgtreillis(n, m) -->
### Function: lgtreillis (n, m)

retorna a lista de partições de peso *n* e comprimento *m*.





```maxima
(%i1) lgtreillis (4, 2);
(%o1)                   [[3, 1], [2, 2]]
```


Veja também: `ltreillis`, `treillis` e `treinat`.

<!-- category: Other -->
<!-- keywords: ltreillis -->
<!-- signatures: ltreillis(n, m) -->
### Function: ltreillis (n, m)

retorna a lista de partições de peso *n* e comprimento menor que ou
igual a *m*.





```maxima
(%i1) ltreillis (4, 2);
(%o1)               [[4, 0], [3, 1], [2, 2]]
```


Veja também: `lgtreillis`, `treillis` e `treinat`.

<!-- category: Other -->
<!-- keywords: mon2schur -->
<!-- signatures: mon2schur(L) -->
### Function: mon2schur (L)

a lsita *L* representa a função de Schur $S_L$: temos




Essa função de Schur pode ser escrita em termos de monômios usando
`treinat` e `kostka`.  A forma retornada é um polinômio
simétrico na representação contraída nas variáveis $x_1,x_2,\ldots$.







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



o qual significa que para 3 variáveis fornece:




```maxima
2 x1 x2 x3 + x1^2 x2 + x2^2 x1 + x1^2 x3 + x3^2 x1
    + x2^2 x3 + x3^2 x2
```


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: multi_elem -->
<!-- signatures: multi_elem(l_elem, multi_pc, l_var) -->
### Function: multi_elem (l_elem, multi_pc, l_var)

decompões um polinômio multi-simétrico na forma multi-contraída
*multi_pc* nos grupos de variáveis contidas na lista de listas
*l_var* en termos de funções elementares simétricas contidas em
*l_elem*.






```maxima
(%i1) multi_elem ([[2, e1, e2], [2, f1, f2]], a*x + a^2 + x^3, [[x, y], [a, b]]);
                                                  3
(%o1)         - 2 f2 + f1 (f1 + e1) - 3 e1 e2 + e1
(%i2) ratsimp (%);
                         2                       3
(%o2)         - 2 f2 + f1  + e1 f1 - 3 e1 e2 + e1
```


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: multi_orbit -->
<!-- signatures: multi_orbit(P, [lvar_1, lvar_2, ..., lvar_p]) -->
### Function: multi_orbit (P, [lvar_1, lvar_2, ..., lvar_p])

*P* é um polinômio no conjunto de variáveis contidas nas lista
*lvar_1*, *lvar_2*, ..., *lvar_p*. Essa função retorna a
órbita do polinômio *P* sob a ação do produto dos
grupos simétricos dos conjuntos de variáveis represetnadas nas *p*
listas.






```maxima
(%i1) multi_orbit (a*x + b*y, [[x, y], [a, b]]);
(%o1)                [b y + a x, a y + b x]
(%i2) multi_orbit (x + y + 2*a, [[x, y], [a, b, c]]);
(%o2)        [y + x + 2 c, y + x + 2 b, y + x + 2 a]
```


Veja também: `orbit` para a ação de um grupo simétrico simples.

<!-- category: Other -->
<!-- keywords: multi_pui -->
<!-- signatures: multi_pui -->
### Function: multi_pui

é para a função `pui` o que a função `multi_elem` é para
a função `elem`.





```maxima
(%i1) multi_pui ([[2, p1, p2], [2, t1, t2]], a*x + a^2 + x^3, [[x, y], [a, b]]);
                                            3
                                3 p1 p2   p1
(%o1)              t2 + p1 t1 + ------- - ---
                                   2       2
```

<!-- category: Other -->
<!-- keywords: multinomial -->
<!-- signatures: multinomial(r, part) -->
### Function: multinomial (r, part)

onde *r* é o peso da partição *part*.  Essa função
retorna o coefinciente multinomial associado: se as partes de
*part* forem *i_1*, *i_2*, ..., *i_k*, o resultado é
`r!/(i_1! i_2! ... i_k!)`.

<!-- category: Other -->
<!-- keywords: multsym -->
<!-- signatures: multsym(ppart_1, ppart_2, n) -->
### Function: multsym (ppart_1, ppart_2, n)

retorna oproduto de dois polinômios simétricos em *n*
varieis trabalhando somente módulo a ação do grupo simétrico de
ordem *n*. O polinômios estão em sua forma particionada.


Dados 2 polinômio simétricos em *x*, *y*:  `3*(x + y) + 2*x*y` e `5*(x^2 + y^2)` cujas formas particionadas são `[[3, 1], [2, 1, 1]]` e `[[5, 2]]`, seu produto irá ser





```maxima
(%i1) multsym ([[3, 1], [2, 1, 1]], [[5, 2]], 2);
(%o1)         [[10, 3, 1], [15, 3, 0], [15, 2, 1]]
```


isso é `10*(x^3*y + y^3*x) + 15*(x^2*y + y^2*x) + 15*(x^3 + y^3)`.

 

Funções para mudar as representacões de um polinômio simétrico:

 

`contract`, `cont2part`, `explose`, `part2cont`,
`partpol`, `tcontract`, `tpartpol`.

<!-- category: Other -->
<!-- keywords: orbit -->
<!-- signatures: orbit(P, lvar) -->
### Function: orbit (P, lvar)

calcula a órbita do polinômio *P* nas variáveis na lista
*lvar* sob a ação do grupo simétrico do conjunto das
variáveis na lista *lvar*.

 




```maxima
(%i1) orbit (a*x + b*y, [x, y]);
(%o1)                [a y + b x, b y + a x]
(%i2) orbit (2*x + x^2, [x, y]);
                        2         2
(%o2)                 [y  + 2 y, x  + 2 x]
```


Veja também `multi_orbit` para a ação de um produto de grupos
simétricos sobre um polinômio.

<!-- category: Other -->
<!-- keywords: part2cont -->
<!-- signatures: part2cont(ppart, lvar) -->
### Function: part2cont (ppart, lvar)

vai da forma particionada para a forma contraída de um polinômio simétrico.
A forma contraída é convertida com as variáveis em *lvar*.





```maxima
(%i1) part2cont ([[2*a^3*b, 4, 1]], [x, y]);
                              3    4
(%o1)                      2 a  b x  y
```

<!-- category: Other -->
<!-- keywords: partpol -->
<!-- signatures: partpol(psym, lvar) -->
### Function: partpol (psym, lvar)

*psym* é um polinômio simétrico nas variáveis da lista
*lvar*. Essa função retorna sua represetnação particionada.





```maxima
(%i1) partpol (-a*(x + y) + 3*x*y, [x, y]);
(%o1)               [[3, 1, 1], [- a, 1, 0]]
```

<!-- category: Other -->
<!-- keywords: permut -->
<!-- signatures: permut(L) -->
### Function: permut (L)

retorna a lista de permutações da lista *L*.

<!-- category: Other -->
<!-- keywords: polynome2ele -->
<!-- signatures: polynome2ele(P, x) -->
### Function: polynome2ele (P, x)

fornece a lista `l = [n, e_1, ..., e_n]`
onde *n* é o grau do polinômio *P* na variável
*x* e *e_i* é a *i*-ésima função simétrica elementar
das raízes de *P*.






```maxima
(%i1) polynome2ele (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x);
(%o1)          [7, 0, - 14, 0, 56, 0, - 56, - 22]
(%i2) ele2polynome ([7, 0, -14, 0, 56, 0, -56, -22], x);
                  7       5       3
(%o2)            x  - 14 x  + 56 x  - 56 x + 22
```


A inversa: `ele2polynome (l, x)`

<!-- category: Other -->
<!-- keywords: prodrac -->
<!-- signatures: prodrac(L, k) -->
### Function: prodrac (L, k)

*L* é uma lista contendo as funções simétricas elementares 
sobre um conjunto *A*. `prodrac` retorna o polinômio cujas raízes
são os produtos *k* por *k* dos elementos de *A*.

 

Veja também `somrac`.

<!-- category: Other -->
<!-- keywords: pui -->
<!-- signatures: pui(L, sym, lvar) -->
### Function: pui (L, sym, lvar)

decompõe o polinômio simétrico *sym*, nas variáveis na
lista *lvar*, em termos de funções exponenciais na lista *L*.
Se o primeiro elemento de *L* for fornecido, esse primeiro elemento será o tamanho do
alfabeto, de outra forma o tamanho será o grau do polinômio
*sym*.  Se valores forem omitidos na lista *L*, valores formais do
tipo *p1*, *p2* , etc. serão adicionados. O polinômio
*sym* pode ser fornecido de três diferentes formas: contraída (`elem`
pode então ser 1, seu valor padrão), particionada (`elem` pode ser
3), ou extendida (i.e. o polinômio completo, e `elem` pode então
ser 2). A função `pui` é usada da mesma forma.







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


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: pui2comp -->
<!-- signatures: pui2comp(n, lpui) -->
### Function: pui2comp (n, lpui)

converte a dista das primeiras *n* funções completas (com o
comprimento em primeiro lugar) em termos de funções exponenciais fornecidas na lista
*lpui*. se a lista *lpui* for vazia, o cardinal é *n*,
de outra forma o cardinal será seu primeiro elemento (como em `comp2ele` e em
`comp2pui`).







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


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: pui2ele -->
<!-- signatures: pui2ele(n, lpui) -->
### Function: pui2ele (n, lpui)

efetiva a passagem de funções exponenciais para as funções elementares simétricas.
Se o sinalizador `pui2ele` for `girard`, `pui2ele` irá retornar a lista de
funções elementares simétricas de 1 a *n*, e se o sinalizador for
`close`, `pui2ele` retornará a *n*-ésima função simétrica elementar.


Outras funções para mudanças de base: `comp2ele`.

<!-- category: Other -->
<!-- keywords: pui2polynome -->
<!-- signatures: pui2polynome(x, lpui) -->
### Function: pui2polynome (x, lpui)

calcula o polinômio em *x* cujas funções exponenciais
das raízes são dadas na lista *lpui*.







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


Veja também:
`polynome2ele`, `ele2polynome`.

<!-- category: Other -->
<!-- keywords: pui_direct -->
<!-- signatures: pui_direct(orbite, [lvar_1, ..., lvar_n], [d_1, d_2, ..., d_n]) -->
### Function: pui_direct (orbite, [lvar_1, ..., lvar_n], [d_1, d_2, ..., d_n])

Tomemos *f* para ser um polinômio em *n* blocos de variáveis *lvar_1*,
..., *lvar_n*.  Façamos *c_i* ser o n;umero de variáveis em
*lvar_i*, e *SC* ser o produto de *n* grupos simétricos de
grau *c_1*, ..., *c_n*. Essas ações dos grupos naturalmente sobre *f*.
A lista *orbite* é a órbita, denotada `SC(f)`, da
função *f* sob a ação de *SC*. (Essa lista pode ser
obtida através da função `multi_orbit`.)  Os *di* são inteiros
de forma que $c_1 \le d_1, c_2 \le d_2, \ldots, c_n \le d_n$.  




A função `pui_direct` retorna
as primeiras *n* funções exponenciais de `SD(f)` deduzidas
das funções exponenciais de `SC(f)`, onde *n* é
o tamanho de `SD(f)`.


O resultado está na multi-forma contraída com relação a *SD*, i.e. somente um
elemento é mantido por órbita, sob a ação de *SD*.








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
(%i4) pui_direct ([y + x + 2*c, y + x + 2*b, y + x + 2*a], [[x, y], [a, b, c]], [2, 3]);
                             2              2
(%o4) [3 x + 2 a, 6 x y + 3 x  + 4 a x + 4 a , 

                 2                   3        2       2        3
              9 x  y + 12 a x y + 3 x  + 6 a x  + 12 a  x + 8 a ]
```

<!-- category: Other -->
<!-- keywords: puireduc -->
<!-- signatures: puireduc(n, lpui) -->
### Function: puireduc (n, lpui)

*lpui* é uma lista cujo primeiro elemento é um inteiro *m*.
`puireduc` fornece as primeiras *n* funções exponenciais em termos das
primeiras *m* funções.





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

calcula a resilvente do polinômio *P* em *x* de grau
*n* >= *d* através da fFunção *f* expressa nas variáveis 
*x_1*, ..., *x_d*.  Para eficiência de computação é
importante não incluir na lista as variáveis
`[x_1, ..., x_d]` que não aparecem na função de transformação *f*.


Para melhorar a eficiência do cálculo se pode escolher sinalizadores em
`resolvante` de forma a usar os algorítmos apropriados:


Se a função *f* for unitária :


- *
um polinômio em uma variável simples,
- *
  
linear ,
- *
  
alternando,
- *
  
um somatório,
- *
  
simétrico,
- *
  
um produto,
- *
a função da resolvente de Cayley (utilizável de grau 5 em diante)


```maxima
(x1*x2 + x2*x3 + x3*x4 + x4*x5 + x5*x1 -
     (x1*x3 + x3*x5 + x5*x2 + x2*x4 + x4*x1))^2
```

  
geral,

o sinalizador da `resolvante` poderá ser respectivamente :


- *
  
unitaire,
- *
  
lineaire,
- *
  
alternee,
- *
  
somme,
- *
  
produit,
- *
  
cayley,
- *
  
generale.

























```maxima
(%i1) resolvante: unitaire$
(%i2) resolvante (x^7 - 14*x^5 + 56*x^3 - 56*x + 22, x, x^3 - 1, [x]);

" resolvante unitaire " [7, 0, 28, 0, 168, 0, 1120, - 154, 7840, - 2772, 56448, - 33880, 

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

" resolvente de Cayley "
        6       5         4          3            2
(%o21) x  - 40 x  + 4080 x  - 92928 x  + 3772160 x  + 37880832 x

                                                       + 93392896
```


Para a resolvente de Cayley, os 2 últimos argumentos são neutros
e o polinômio fornecido na entrada deve ser necessáriamente de grau 5.


Veja também :


`resolvante_bipartite`, `resolvante_produit_sym`,
`resolvante_unitaire`, `resolvante_alternee1`, `resolvante_klein`, 
`resolvante_klein3`, `resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_alternee1 -->
<!-- signatures: resolvante_alternee1(P, x) -->
### Function: resolvante_alternee1 (P, x)

calcula a transformação de 
`P(x)` de grau *n* pela função $\prod_{1\leq i<j\leq n-1} (x_i-x_j)$.




Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante` , `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_bipartite`.

<!-- category: Other -->
<!-- keywords: resolvante_bipartite -->
<!-- signatures: resolvante_bipartite(P, x) -->
### Function: resolvante_bipartite (P, x)

calcula a trasformação de
`P(x)` de mesmo grau *n* através da função 




Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante` , `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`, `resolvante_alternee1`.





```maxima
(%i1) resolvante_bipartite (x^6 + 108, x);
              10        8           6             4
(%o1)        y   - 972 y  + 314928 y  - 34012224 y
```


Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`,
`resolvante_alternee1`.

<!-- category: Other -->
<!-- keywords: resolvante_diedrale -->
<!-- signatures: resolvante_diedrale(P, x) -->
### Function: resolvante_diedrale (P, x)

calcula a transformação de `P(x)` através da função
`x_1 x_2 + x_3 x_4`.





```maxima
(%i1) resolvante_diedrale (x^5 - 3*x^4 + 1, x);
       15       12       11       10        9         8         7
(%o1) x   - 21 x   - 81 x   - 21 x   + 207 x  + 1134 x  + 2331 x

        6         5          4          3          2
 - 945 x  - 4970 x  - 18333 x  - 29079 x  - 20745 x  - 25326 x

 - 697
```


Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante`.

<!-- category: Other -->
<!-- keywords: resolvante_klein -->
<!-- signatures: resolvante_klein(P, x) -->
### Function: resolvante_klein (P, x)

+calculates the transformation of `P(x)` by the function
+`x_1 x_2 x_4 + x_4`.


Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_klein3 -->
<!-- signatures: resolvante_klein3(P, x) -->
### Function: resolvante_klein3 (P, x)

calcula a transformação de `P(x)` através da função
`x_1 x_2 x_4 + x_4`.


Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante`,
`resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_produit_sym -->
<!-- signatures: resolvante_produit_sym(P, x) -->
### Function: resolvante_produit_sym (P, x)

calcula a lista de todas as resolventes de produto do polinômio 
`P(x)`.







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

" resolvente produto "
       10      8       7    6        5       4       3     2
(%o3) y   + 3 y  + 14 y  - y  - 14 y  - 31 y  - 21 y  - 2 y  + 1
```





Veja também :


`resolvante`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`,
`resolvante_klein3`, `resolvante_vierer`,
`resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_unitaire -->
<!-- signatures: resolvante_unitaire(P, Q, x) -->
### Function: resolvante_unitaire (P, Q, x)

calcula a resolvente do polinômio `P(x)` através do
polinomio `Q(x)`. 


Veja também :


`resolvante_produit_sym`, `resolvante`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante_vierer`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: resolvante_vierer -->
<!-- signatures: resolvante_vierer(P, x) -->
### Function: resolvante_vierer (P, x)

calcula a transformação de
`P(x)` pela função `x_1 x_2 - x_3 x_4`.


Veja também :


`resolvante_produit_sym`, `resolvante_unitaire`,
`resolvante_alternee1`, `resolvante_klein`, `resolvante_klein3`,
`resolvante`, `resolvante_diedrale`.

<!-- category: Other -->
<!-- keywords: schur2comp -->
<!-- signatures: schur2comp(P, l_var) -->
### Function: schur2comp (P, l_var)

*P* é um polinômio nas variáveis da lista *l_var*.  Cada
uma dessas variáveis represetna uma função simétrica completa.  Na
lista *l_var* o *i*-ésima função simétrica completa é representada através da
concatenação da letra `h` com o inteiro *i*:
`hi`.  Essa função expressa *P* em termos de funções de
Schur.







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
<!-- signatures: somrac(L, k) -->
### Function: somrac (L, k)

A lista *L* contains função simétrica elementars de um polynomial
*P* . The function computes the polinômio whose roots are the 
*k* by *k* distinct sums of the roots of *P*. 


Also see `prodrac`.

<!-- category: Other -->
<!-- keywords: tcontract -->
<!-- signatures: tcontract(pol, lvar) -->
### Function: tcontract (pol, lvar)

testa se o polinômio *pol* é simétrico nas variáveis da
lista *lvar*.  Se for, `tcontract` retorna uma representação contraída como o faz a
função `contract`.

<!-- category: Other -->
<!-- keywords: tpartpol -->
<!-- signatures: tpartpol(pol, lvar) -->
### Function: tpartpol (pol, lvar)

testa se o polinômio *pol* é simétrico nas variáveis da
lista *lvar*.  Se for, `tpartpol` retorna sua represetnação particionada como
o faz a função `partpol`.

<!-- category: Other -->
<!-- keywords: treillis -->
<!-- signatures: treillis(n) -->
### Function: treillis (n)

retorna todas as partições de peso *n*.





```maxima
(%i1) treillis (4);
(%o1)    [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
```


Veja também: `lgtreillis`, `ltreillis` e `treinat`.

<!-- category: Other -->
<!-- keywords: treinat -->
<!-- signatures: treinat(part) -->
### Function: treinat (part)

retorna a lista de partições inferiores à partiçào *part* com relação à
ordem natural.







```maxima
(%i1) treinat ([5]);
(%o1)                         [[5]]
(%i2) treinat ([1, 1, 1, 1, 1]);
(%o2) [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], 
 
                                                 [1, 1, 1, 1, 1]]
(%i3) treinat ([3, 2]);
(%o3)                 [[5], [4, 1], [3, 2]]
```


Veja também: `lgtreillis`, `ltreillis` e `treillis`.

