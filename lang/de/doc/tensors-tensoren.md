## Tensoren

<!-- category: Tensors -->
<!-- keywords: abasep -->
<!-- signatures: abasep(v) -->
### Function: abasep (v)

Pruft, ob das Argument *v* ein Basisvektor ist.  Ein Basisvektor ist ein
indiziertes Symbol mit dem Symbol `asymbol` als Bezeichner und einem
Index im Bereich von `1` bis `adim`.


Beispiel:



```maxima
(%i1) load("atensor")$
(%i2) asymbol: x$
(%i3) adim:3$
(%i4) abasep(x[1]);
(%o4)                         true
(%i5) abasep(x[3]);
(%o5)                         true
(%i6) abasep(x[4]);
(%o6)                         false
```

See also: `asymbol`, `adim`.

<!-- category: Tensors -->
<!-- keywords: adim -->
<!-- signatures: adim -->
### Variable: adim

Standardwert: `0`






Die Dimension der Algebra, die bei der Vereinfachung von Ausdrucken mit der
Funktion `atensimp` angewendet wird.  Die Dimension wird von der Funktion
`init_atensor` initialisiert.  Ein indiziertes Symbol mit dem Bezeichner
`asymbol` ist dann ein Basisvektor, wenn der Index kleiner oder gleich
der Dimension `adim` ist.


Beispiel:


Die Dirac-Algebra hat die Dimension `4` und `v[4]` ist ein
Basisvektor.



```maxima
(%i1) load("atensor")$

(%i2) init_atensor(dirac);
(%o2)                         done
(%i3) adim;
(%o3)                           4
(%i4) abasep(v[4]);
(%o4)                         true
```

See also: `atensimp`, `init_atensor`, `asymbol`.

<!-- category: Tensors -->
<!-- keywords: af -->
<!-- signatures: af(u, v) -->
### Function: af (u, v)

Eine antisymmetrische Bilinearform, die bei der Vereinfachung von Ausdrucken
mit der Funktion `atensimp` angewendet wird.  Die Funktion kann vom Nutzer
durch eine neue Funktion ersetzt werden.  Die Standardimplementation pruft
mit der Funktion `abasep`, ob die Argumente *u* und *v*
Basisvektoren sind und setzt fur diesen Fall den entsprechenden Wert der
Matrix `aform` ein.

See also: `atensimp`, `abasep`, `aform`.

<!-- category: Tensors -->
<!-- keywords: aform -->
<!-- signatures: aform -->
### Variable: aform

Standardwert: `ident(3)`





Matrix mit den Werten der Bilinearformen `sf`, `af` und
`av`.  Der Standardwert ist die dreidimensionale Einheitsmatrix.


Beispiel:


Das Beispiel zeigt die Matrix `aform` fur eine Lie-Algebra mit drei
Dimensionen und die Ergebnisse der Bilinearform `av` fur diese Algebra.



```maxima
(%i1) load("atensor")$

(%i2) init_atensor(lie_envelop, 3);
(%o2)                         done
(%i3) aform;
                        [  0    3   - 2 ]
                        [               ]
(%o3)                   [ - 3   0    1  ]
                        [               ]
                        [  2   - 1   0  ]
(%i4) av(v[1], v[2]);
(%o4)                          v
                                3
(%i5) av(v[1], v[3]);
(%o5)                         - v
                                 2
```

See also: `sf`, `af`, `av`.

<!-- category: Tensors -->
<!-- keywords: alg_type -->
<!-- signatures: alg_type -->
### Variable: alg_type

Standardwert: `universal`





Der Typ der Algebra, die bei der Vereinfachung von Ausdrucken mit der
Funktion `atensimp` angewendet wird.  Die Algebra wird von der Funktion
`init_atensor` initialisiert.  Mogliche Algebren sind `universal`,
`grassmann`, `clifford`, `symmetric`, `symplectic` und
`lie_envelop`.  Siehe fur eine ausfuhrliche Erlauterung der Algebren
die Funktion `init_atensor`.

See also: `atensimp`, `init_atensor`.

<!-- category: Tensors -->
<!-- keywords: allsym -->
<!-- signatures: allsym -->
### Variable: allsym

Standardwert: `false`








Hat die Optionsvariable `allsym` den Wert `true`, werden alle
indizierten Großen  als symmetrisch in ihren kovarianten und
kontravarianten Indizes angenommen.  Ist der Wert `false`, werden keine
Symmetrien fur die Indizes angenommen.  Die Indizes von Ableitungen werden
immer als symmetrisch angenommen, außer wenn die Optionsvariable
`iframe_flag` den Wert `true` hat.

See also: `iframe_flag`.

<!-- category: Tensors -->
<!-- keywords: asymbol -->
<!-- signatures: asymbol -->
### Variable: asymbol

Standardwert: `v`




Enthalt das Symbol, das einen Basisvektor des Paketes `atensor`
bezeichnet.  Mit der Funktion `abasep` kann getestet werde, ob ein
indiziertes Symbol einen Basisvektor der Algebra bezeichnet.


Beispiel:


In diesem Beispiel wird `asymbol` auf den Wert `x` gesetzt.



```maxima
(%i1) load("atensor")$

(%i2) init_atensor(symmetric, 2);
(%o2)                         done
(%i3) asymbol;
(%o3)                           v
(%i4) abasep(v[2]);
(%o4)                         true
(%i5) asymbol: x;
(%o5)                           x
(%i6) abasep(x[2]);
(%o6)                         true
```

See also: `abasep`.

<!-- category: Tensors -->
<!-- keywords: atensimp -->
<!-- signatures: atensimp(expr) -->
### Function: atensimp (expr)

Vereinfacht einen Ausdruck *expr* entsprechend der Regeln fur die Algebra,
die mit der Funktion `init_atensor` festgelegt ist.  Die Regeln werden
rekursiv auf den Ausdruck angewendet.  Dabei werden auch Bilinearformen
`sf`, `af` und `av` ausgewertet.


Beispiele:


Die folgenden Beispiele zeigen das Rechnen mit der Algebra der Quaternionen.



```maxima
(%i1) load("atensor")$

(%i2) init_atensor(quaternion);
(%o2)                         done
(%i3) atensimp(v[1].v[1]);
(%o3)                          - 1
(%i4) atensimp(v[2].v[2]);
(%o4)                          - 1
(%i5) atensimp((v[1].v[2]) . (v[1].v[2]));
(%o5)                          - 1
(%i6) expand((2*v[1]+3*v[2])^^2);
(%o6) 9 (v  . v ) + 6 (v  . v ) + 6 (v  . v ) + 4 (v  . v )
          2    2        2    1        1    2        1    1
(%i7) atensimp(%);
(%o7)                         - 13
```

See also: `init_atensor`, `sf`, `af`, `av`.

<!-- category: Tensors -->
<!-- keywords: av -->
<!-- signatures: av(u, v) -->
### Function: av (u, v)

Eine antisymmetrische Bilinearform, die bei der Vereinfachung von Ausdrucken
mit der Funktion `atensimp` angewendet wird.  Die Funktion kann vom Nutzer
durch eine neue Funktion ersetzt werden.  Die Standardimplementation pruft
mit der Funktion `abasep`, ob die Argumente *u* und *v*
Basisvektoren sind und setzt fur diesen Fall den entsprechenden Wert
`v[aform[i,j]]` der Matrix `aform` ein.


Beispiel:



```maxima
(%i1) load("atensor")$
(%i2) adim: 3;
(%o2)                           3
(%i3) aform:matrix([0,3,-2],[-3,0,1],[2,-1,0]);
                        [  0    3   - 2 ]
                        [               ]
(%o3)                   [ - 3   0    1  ]
                        [               ]
                        [  2   - 1   0  ]
(%i4) asymbol: x;
(%o4)                           x
(%i5) av(x[1], x[2]);
(%o5)                          x
                                3
(%i6) av(x[1], x[3]);
(%o6)                         - x
                                 2
```

See also: `atensimp`, `abasep`, `aform`.

<!-- category: Tensors -->
<!-- keywords: bdvac -->
<!-- signatures: bdvac(f) -->
### Function: bdvac (f)

generates the covariant components of the vacuum field equations of
the Brans- Dicke gravitational theory. The scalar field is specified
by the argument *f*, which should be a (quoted) function name
with functional dependencies, e.g., `'p(x)`.


The components of the second rank covariant field tensor are
represented by the array `bd`.

<!-- category: Tensors -->
<!-- keywords: bimetric -->
<!-- signatures: bimetric() -->
### Function: bimetric ()

*** NOT YET IMPLEMENTED ***


generates the field equations of Rosen’s bimetric theory. The field
equations are the components of an array named `rosen`.

<!-- category: Tensors -->
<!-- keywords: canform -->
<!-- signatures: canform(expr), canform(expr, rename) -->
### Function: canform (expr)

Vereinfacht den Ausdruck *expr* indem alle Dummy-Indizes umbenannt und
umgeordnet werden, wobei vorhandene Symmetrieeigenschaften angewendet werden.
Hat die Optionsvariable `allsym` den Wert `true`, werden alle Indizes
als symmetrisch angenommen.  Ansonsten werden Symmetrieeigenschaften angewendet,
die mit der Funktion `decsym` definiert sind.  Die Dummy-Indizes werden
auf gleiche Weise umbenannt wie von der Funktion `rename`.  Wird 
`canform` auf einen großen Ausdruck angewendet, kann die Ausfuhrung
eine lange Zeit beanspruchen.  Die Rechenzeit kann verkurzt werden, indem
zuerst die Funktion `rename` auf den Ausdruck angewendet wird.


`canform` kann einen Ausdruck nicht immer in die einfachste Form bringen,
jedoch ist das Ergebnis immer mathematisch korrekt.


Erhalt das optionale zweite Argument *rename* den Wert `false`, wird
die Umbenennung mit der Funktion `rename` nicht ausgefuhrt.


Fur ein Beispiel siehe die Funktion `decsym`.

See also: `decsym`, `rename`.

<!-- category: Tensors -->
<!-- keywords: canten -->
<!-- signatures: canten(expr) -->
### Function: canten (expr)

Ist vergleichbar mit der Funktion `rename` und vereinfacht den Ausdruck
*expr* indem gebundene Indizes umbenannt und permutiert werden.  Wie die
Funktion `rename` kann `canten` nur Ausdrucke mit Summen von
Tensorprodukten vereinfachen, in denen keine Ableitungen nach Tensorkomponenten
auftreten.  Daher sollte `canten` nur verwendet werden, wenn sich mit
der Funktion `canform` nicht die gewunschte Vereinfachung eines
Ausdrucks erzielen lasst.







Das Ergebnis der Funktion `canten` ist mathematisch nur korrekt, wenn
die Tensoren symmetrisch in ihren Indizes sind.  Hat die Optionsvariable 
`allsym` *nicht* den Wert `true`, bricht `canten` mit einer
Fehlermeldung ab.


Siehe auch die Funktion `concan`, mit der Ausdrucke mit Tensoren
ebenfalls vereinfacht werden konnen, wobei `concan` zusatzlich
Tensorverjungungen ausfuhrt.

See also: `rename`, `canform`, `allsym`, `concan`.

<!-- category: Tensors -->
<!-- keywords: cdisplay -->
<!-- signatures: cdisplay(ten) -->
### Function: cdisplay (ten)

displays all the elements of the tensor *ten*, as represented by
a multidimensional array. Tensors of rank 0 and 1, as well as other types
of variables, are displayed as with `ldisplay`. Tensors of rank 2 are
displayed as 2-dimensional matrices, while tensors of higher rank are displayed
as a list of 2-dimensional matrices. For instance, the Riemann-tensor of
the Schwarzschild metric can be viewed as:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) riemann(false);
(%o4)                                done
(%i5) cdisplay(riem);
          [ 0               0                   0           0     ]
          [                                                       ]
          [                              2                        ]
          [      3 m (r - 2 m)   m    2 m                         ]
          [ 0  - ------------- + -- - ----      0           0     ]
          [            4          3     4                         ]
          [           r          r     r                          ]
          [                                                       ]
riem    = [                                m (r - 2 m)            ]
    1, 1  [ 0               0              -----------      0     ]
          [                                     4                 ]
          [                                    r                  ]
          [                                                       ]
          [                                           m (r - 2 m) ]
          [ 0               0                   0     ----------- ]
          [                                                4      ]
          [                                               r       ]

                                [    2 m (r - 2 m)       ]
                                [ 0  -------------  0  0 ]
                                [          4             ]
                                [         r              ]
                     riem     = [                        ]
                         1, 2   [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]

                                [         m (r - 2 m)    ]
                                [ 0  0  - -----------  0 ]
                                [              4         ]
                                [             r          ]
                     riem     = [                        ]
                         1, 3   [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]
                                [                        ]
                                [ 0  0        0        0 ]

                                [            m (r - 2 m) ]
                                [ 0  0  0  - ----------- ]
                                [                 4      ]
                                [                r       ]
                     riem     = [                        ]
                         1, 4   [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]
                                [                        ]
                                [ 0  0  0        0       ]

                               [       0         0  0  0 ]
                               [                         ]
                               [       2 m               ]
                               [ - ------------  0  0  0 ]
                    riem     = [    2                    ]
                        2, 1   [   r  (r - 2 m)          ]
                               [                         ]
                               [       0         0  0  0 ]
                               [                         ]
                               [       0         0  0  0 ]

             [     2 m                                         ]
             [ ------------  0        0               0        ]
             [  2                                              ]
             [ r  (r - 2 m)                                    ]
             [                                                 ]
             [      0        0        0               0        ]
             [                                                 ]
  riem     = [                         m                       ]
      2, 2   [      0        0  - ------------        0        ]
             [                     2                           ]
             [                    r  (r - 2 m)                 ]
             [                                                 ]
             [                                         m       ]
             [      0        0        0         - ------------ ]
             [                                     2           ]
             [                                    r  (r - 2 m) ]

                                [ 0  0       0        0 ]
                                [                       ]
                                [            m          ]
                                [ 0  0  ------------  0 ]
                     riem     = [        2              ]
                         2, 3   [       r  (r - 2 m)    ]
                                [                       ]
                                [ 0  0       0        0 ]
                                [                       ]
                                [ 0  0       0        0 ]

                                [ 0  0  0       0       ]
                                [                       ]
                                [               m       ]
                                [ 0  0  0  ------------ ]
                     riem     = [           2           ]
                         2, 4   [          r  (r - 2 m) ]
                                [                       ]
                                [ 0  0  0       0       ]
                                [                       ]
                                [ 0  0  0       0       ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [ m          ]
                               3, 1   [ -  0  0  0 ]
                                      [ r          ]
                                      [            ]
                                      [ 0  0  0  0 ]

                                      [ 0  0  0  0 ]
                                      [            ]
                                      [ 0  0  0  0 ]
                                      [            ]
                           riem     = [    m       ]
                               3, 2   [ 0  -  0  0 ]
                                      [    r       ]
                                      [            ]
                                      [ 0  0  0  0 ]

                               [   m                      ]
                               [ - -   0   0       0      ]
                               [   r                      ]
                               [                          ]
                               [        m                 ]
                               [  0   - -  0       0      ]
                    riem     = [        r                 ]
                        3, 3   [                          ]
                               [  0    0   0       0      ]
                               [                          ]
                               [              2 m - r     ]
                               [  0    0   0  ------- + 1 ]
                               [                 r        ]

                                    [ 0  0  0    0   ]
                                    [                ]
                                    [ 0  0  0    0   ]
                                    [                ]
                         riem     = [            2 m ]
                             3, 4   [ 0  0  0  - --- ]
                                    [             r  ]
                                    [                ]
                                    [ 0  0  0    0   ]

                                [       0        0  0  0 ]
                                [                        ]
                                [       0        0  0  0 ]
                                [                        ]
                     riem     = [       0        0  0  0 ]
                         4, 1   [                        ]
                                [      2                 ]
                                [ m sin (theta)          ]
                                [ -------------  0  0  0 ]
                                [       r                ]

                                [ 0        0        0  0 ]
                                [                        ]
                                [ 0        0        0  0 ]
                                [                        ]
                     riem     = [ 0        0        0  0 ]
                         4, 2   [                        ]
                                [         2              ]
                                [    m sin (theta)       ]
                                [ 0  -------------  0  0 ]
                                [          r             ]

                              [ 0  0          0          0 ]
                              [                            ]
                              [ 0  0          0          0 ]
                              [                            ]
                   riem     = [ 0  0          0          0 ]
                       4, 3   [                            ]
                              [                2           ]
                              [         2 m sin (theta)    ]
                              [ 0  0  - ---------------  0 ]
                              [                r           ]

           [        2                                             ]
           [   m sin (theta)                                      ]
           [ - -------------         0                0         0 ]
           [         r                                            ]
           [                                                      ]
           [                         2                            ]
           [                    m sin (theta)                     ]
riem     = [        0         - -------------         0         0 ]
    4, 4   [                          r                           ]
           [                                                      ]
           [                                          2           ]
           [                                   2 m sin (theta)    ]
           [        0                0         ---------------  0 ]
           [                                          r           ]
           [                                                      ]
           [        0                0                0         0 ]

(%o5)                                done
```

<!-- category: Tensors -->
<!-- keywords: cframe_flag -->
<!-- signatures: cframe_flag -->
### Variable: cframe_flag

Standardwert: `false`


When the variable `cframe_flag` is set to true, the `ctensor` package
performs its calculations using a moving frame.

<!-- category: Tensors -->
<!-- keywords: cgeodesic -->
<!-- signatures: cgeodesic(dis) -->
### Function: cgeodesic (dis)

A function in the `ctensor` (component tensor)
package.  `cgeodesic` computes the geodesic equations of
motion for a given metric.  They are stored in the array `geod[i]`.  If
the argument *dis* is `true` then these equations are displayed.

<!-- category: Tensors -->
<!-- keywords: changename -->
<!-- signatures: changename(old, new, expr) -->
### Function: changename (old, new, expr)

Andert den Namen aller Tensoren im Ausdruck *expr* von
*old* nach *new*.  Das Argument *old* kann ein Symbol oder eine
Liste der Form `[name, m, n]` sein.  Im letzteren Fall
werden nur die Tensoren zu *new* umbenannt, die den Namen *name*
sowie *m* kovariante und *n* kontravariante Indizes haben.


Beispiel:


In diesem Beispiel wird der Name *c* zu *w* geandert.



```maxima
(%i1) load("itensor")$

(%i2) expr:a([i,j],[k])*b([u],[],v)+c([x,y],[])*d([],[])*e$

(%i3) ishow(changename(c, w, expr))$
                                  k
(%t3)                 d e w    + a    b
                           x y    i j  u,v
```

<!-- category: Tensors -->
<!-- keywords: checkdiv -->
<!-- signatures: checkdiv() -->
### Function: checkdiv ()

computes the covariant divergence of the mixed second rank tensor
(whose first index must be covariant) by printing the
corresponding n components of the vector field (the divergence) where
n = `dim`. If the argument to the function is `g` then the
divergence of the Einstein tensor will be formed and must be zero.
In addition, the divergence (vector) is given the array name `div`.

<!-- category: Tensors -->
<!-- keywords: christof -->
<!-- signatures: christof(dis) -->
### Function: christof (dis)

A function in the `ctensor` (component tensor) package.  It computes the 
Christoffel symbols of both kinds.  The argument *dis* determines which 
results are to be immediately displayed.  The Christoffel symbols of the first 
and second kinds are stored in the arrays `lcs[i,j,k]` and 
`mcs[i,j,k]` respectively and defined to be symmetric in the first two 
indices.  If the argument to `christof` is `lcs` or `mcs` then 
the unique non-zero values of `lcs[i,j,k]` or `mcs[i,j,k]`, 
respectively, will be displayed. If the argument is `all` then the unique 
non-zero values of `lcs[i,j,k]` and `mcs[i,j,k]` will be displayed.  
If the argument is `false` then the display of the elements will not occur.
The array elements `mcs[i,j,k]` are defined in such a manner that the final
index is contravariant.

<!-- category: Tensors -->
<!-- keywords: cmetric -->
<!-- signatures: cmetric(dis), cmetric() -->
### Function: cmetric (dis)

Die Funktion `cmetric` berechnet die inverse der Metrik und fuhrt weitere
Initialisierungen fur die Rechnung mit Tensoren aus.










Hat die Optionsvariable `cframe_flag` den Wert `false`, wird die
inverse Metrik mit der vom Nutzer angegebenen Metrik berechnet, die in der
Matrix `lg` enthalten ist, und in der Matrix `ug` abgespeichert.
Die Determinante der Metrik wird in der Variablen `gdet` abgelegt.
Ist die Metrik diagonal wird die Variable `diagmetric` entsprechend
gesetzt.  Hat das optionale Argument *dis* einen von `false`
verschiedenen Wert wird die inverse Metrik ausgegeben.







Hat die Optionsvariable `cframe_flag` den Wert `true`, erwartet
`cmetric`, dass die Matrizen `lfg` fur die Metrik des bewegten
Bezugssystems und `fri` fur die inverse dieser Metrik definiert sind.
Mit diesen Matrizen berechnet `cmetric` dann die Werte der Matrizen
`fr` und die inverse `ufg`.

See also: `cframe_flag`, `lg`, `ug`, `gdet`, `diagmetric`, `lfg`, `ufg`.

<!-- category: Tensors -->
<!-- keywords: cnonmet_flag -->
<!-- signatures: cnonmet_flag -->
### Variable: cnonmet_flag

Causes the nonmetricity coefficients to be included in the computation of
the connection coefficients. The nonmetricity coefficients are computed
from the user-supplied nonmetricity vector `nm` by the function
`nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: cograd -->
<!-- signatures: cograd() -->
### Function: cograd ()

Computes the covariant gradient of a scalar function allowing the
user to choose the corresponding vector name as the example under
`contragrad` illustrates.

<!-- category: Tensors -->
<!-- keywords: components -->
<!-- signatures: components(tensor, expr) -->
### Function: components (tensor, expr)

Erlaubt die Zuweisung von Werten an die Komponenten eines Tensors *tensor*,
die mit dem Argument *expr* angegeben werden.  Immer wenn der Tensor
*tensor* mit all seinen Indizes in einem Ausdruck auftritt, werden die
Komponenten mit den angegebenen Werten substituiert.  Der Tensor muss die Form
`t([...],[...])` haben, wobei die Listen auch leer sein konnen.  Das
Argument *expr* ist irgendein Ausdruck, der dieselben freien Indizes wie
der Tensor *tensor* hat.  Sollen Werte an einen Metriktensor zugewiesen
werden, der Dummy-Indizes hat, so muss auf die Benennung der Indizes
sorgfaltig geachtet werden, um das Auftreten von Mehrfachen Dummy-Indizes zu
vermeiden.  Mit der Funktion `remcomps` werden Zuweisungen der Funktion
`components` an die Komponenten eines Tensors entfernt.








Es muss beachtet werden, dass die Funktion `components` nur den Typ eines
Tensors, aber nicht die Ordnung der Indizes beachtet.  Werden daher Werte
an die Komponenten der Tensoren `x([i,-j],[])`, `x([-j,i],[])` oder
`x([i],[j])` zugewiesen, ergibt sich jeweils dasselbe Ergebnis.





Komponenten konnen einem indizierten Ausdruck auf vier verschiedene Methoden
zugeordnet werden.  Zwei Methoden nutzen die Funktion `components`.




1) Als ein indizierte Ausdruck:



```maxima
(%i2) components(g([],[i,j]), e([],[i])*p([],[j]))$
(%i3) ishow(g([],[i,j]))$
                                      i  j
(%t3)                                e  p
```




2) Als eine Matrix:



```maxima
(%i5) lg:-ident(4)$ lg[1,1]:1$ lg;
                            [ 1   0    0    0  ]
                            [                  ]
                            [ 0  - 1   0    0  ]
(%o5)                       [                  ]
                            [ 0   0   - 1   0  ]
                            [                  ]
                            [ 0   0    0   - 1 ]

(%i6) components(g([i,j],[]), lg);
(%o6)                                done
(%i7) ishow(g([i,j],[]))$
(%t7)                                g
                                      i j
(%i8) g([1,1],[]);
(%o8)                                  1
(%i9) g([4,4],[]);
(%o9)                                 - 1
```








3) Als eine Funktion: Die Werte der Komponenten eines Tensors werden durch eine
Funktion gegeben.



```maxima
(%i4) h(l1,l2,[l3]):=if length(l1)=length(l2) and length(l3)=0
  then kdelta(l1,l2) else apply(g,append([l1,l2], l3))$
(%i5) ishow(h([i],[j]))$
                                          j
(%t5)                               kdelta
                                          i
(%i6) ishow(h([i,j],[k],l))$
                                     k
(%t6)                               g
                                     i j,l
```





4) Mit Mustern und Regeln: Im Folgenden wird ein Beispiel mit den Funktionen
`defrule` und `applyb1` gezeigt.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) matchdeclare(l1,listp);
(%o2)                                done
(%i3) defrule(r1,m(l1,[]),(i1:idummy(),
      g([l1[1],l1[2]],[])*q([i1],[])*e([],[i1])))$

(%i4) defrule(r2,m([],l1),(i1:idummy(),
      w([],[l1[1],l1[2]])*e([i1],[])*q([],[i1])))$

(%i5) ishow(m([i,n],[])*m([],[i,m]))$
                                    i m
(%t5)                              m    m
                                         i n
(%i6) ishow(rename(applyb1(%,r1,r2)))$
                           %1  %2  %3 m
(%t6)                     e   q   w     q   e   g
                                         %1  %2  %3 n
```

See also: `remcomps`, `defrule`, `applyb1`.

<!-- category: Tensors -->
<!-- keywords: concan -->
<!-- signatures: concan(expr) -->
### Function: concan (expr)

Ist vergleichbar mit der Funktion `canten`.  Im Unterschied zu
`canten` werden zusatzlich Tensorverjungungen ausgefuhrt.

See also: `canten`.

<!-- category: Tensors -->
<!-- keywords: conmetderiv -->
<!-- signatures: conmetderiv(expr, tensor) -->
### Function: conmetderiv (expr, tensor)

Vereinfacht Ausdrucke, die kovariante und kontravariante Ableitungen des
Metriktensors enthalten.  `conmetderiv` kann zum Beispiel die Ableitungen
des kontravarianten Metriktensors in Beziehung zu den Christoffel-Symbolen 
setzen:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(g([],[a,b],c))$
                                      a b
(%t2)                                g
                                      ,c
(%i3) ishow(conmetderiv(%,g))$
                         %1 b      a       %1 a      b
(%t3)                 - g     ichr2     - g     ichr2
                                   %1 c              %1 c
```

<!-- category: Tensors -->
<!-- keywords: contortion -->
<!-- signatures: contortion(tr) -->
### Function: contortion (tr)

Computes the (2,1) contortion coefficients from the torsion tensor *tr*.

<!-- category: Tensors -->
<!-- keywords: contract -->
<!-- signatures: contract(expr) -->
### Function: contract (expr)

Fuhrt die Tensorverjungungen im Ausdruck *expr* aus, die beliebige
Summen und Produkte sein konnen.  `contract` nutzt die Informationen,
die fur die Tensoren mit der Funktion `defcon` definiert sind.  Die
besten Ergebnisse werden erzielt, wenn der Ausdruck *expr* vollstandig
expandiert wird.  Die Funktion `radexpand` expandiert Produkte und
Potenzen von Summen am schnellsten, sofern keine Variablen im Nenner der Terme
auftreten.  Die Optionsvariable `gcd` sollte den Wert `false` haben,
wenn das Kurzen durch einen großten gemeinsamen Teiler nicht notwendig
ist.

See also: `defcon`, `radexpand`, `gcd`.

<!-- category: Tensors -->
<!-- keywords: contractions -->
<!-- signatures: contractions -->
### Variable: contractions

Die Liste `contractions` enthalt die Tensoren, die mit der Funktion
`defcon` die Eigenschaft einer Tensorverjungung erhalten haben.

See also: `contractions`.

<!-- category: Tensors -->
<!-- keywords: contragrad -->
<!-- signatures: contragrad() -->
### Function: contragrad ()

Computes the contravariant gradient of a scalar function allowing

the user to choose the corresponding vector name as the example
below for the Schwarzschild metric illustrates:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(f,r);
(%o4)                               [f(r)]
(%i5) cograd(f,g1);
(%o5)                                done
(%i6) listarray(g1);
(%o6)                            [0, f , 0, 0]
                                      r
(%i7) contragrad(f,g2);
(%o7)                                done
(%i8) listarray(g2);
                               f  r - 2 f  m
                                r        r
(%o8)                      [0, -------------, 0, 0]
                                     r
```

<!-- category: Tensors -->
<!-- keywords: coord -->
<!-- signatures: coord(tensor_1, tensor_2, ...) -->
### Function: coord (tensor_1, tensor_2, ...)

Gibt der tensoriellen Große *tensor_i* die Eigenschaft, dass die
kovariante Ableitung eines Vektors mit dem Namen *tensor_i* das Ergebnis
Kronecker-Delta hat.


`coord` ist auch eine Systemvariable, die alle tensoriellen Großen
enthalt, die mit der Funktion `coord` die Eigenschaft der kovarianten
Ableitung erhalten haben.



Beispiel:



```maxima
(%i1) coord(x);
(%o1)                         done
(%i2) idiff(x([],[i]),j);
(%o2)                   kdelta([j], [i])
(%i3) coord;
(%o3)                          [x]
```

<!-- category: Tensors -->
<!-- keywords: covdiff -->
<!-- signatures: covdiff(expr, v_1, v_2, ...) -->
### Function: covdiff (expr, v_1, v_2, ...)

Gibt die kovariante Ableitung des Ausdruck *expr* nach den Variablen
*v_i* in einer Darstellung mit Christoffel-Symbolen der zweiten Art
`ichr2` zuruck.  Um den erhaltenen Ausdruck auszuwerten, kann das 
Kommando `ev(expr, ichr2)`.



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) entertensor()$
Enter tensor name: a;
Enter a list of the covariant indices: [i,j];
Enter a list of the contravariant indices: [k];
Enter a list of the derivative indices: [];

                                      k
(%t2)                                a
                                      i j

(%i3) ishow(covdiff(%,s))$
             k         %1     k         %1     k
(%t3)     - a     ichr2    - a     ichr2    + a
             i %1      j s    %1 j      i s    i j,s

             k     %1
      + ichr2     a
             %1 s  i j
(%i4) imetric:g;
(%o4)                                  g
(%i5) ishow(ev(%th(2),ichr2))$
         %1 %4  k
        g      a     (g       - g       + g      )
                i %1   s %4,j    j s,%4    j %4,s
(%t5) - ------------------------------------------
                            2
    %1 %3  k
   g      a     (g       - g       + g      )
           %1 j   s %3,i    i s,%3    i %3,s
 - ------------------------------------------
                       2
    k %2  %1
   g     a    (g        - g        + g       )
          i j   s %2,%1    %1 s,%2    %1 %2,s     k
 + ------------------------------------------- + a
                        2                         i j,s
(%i6)
```

See also: `ichr2`.

<!-- category: Tensors -->
<!-- keywords: csetup -->
<!-- signatures: csetup() -->
### Function: csetup ()

Mit der Funktion `csetup` wird das Paket `ctensor` initialisiert.  Vom
Nutzer werden die Angaben zu einer Metrik abgefragt.  Fur ein Beispiel siehe 
`Einführung-in-ctensor`.

See also: `Einführung-in-ctensor`.

<!-- category: Tensors -->
<!-- keywords: ct_coords -->
<!-- signatures: ct_coords -->
### Variable: ct_coords

Default value: `[]`


An option in the `ctensor` (component tensor)
package.  `ct_coords` contains a list of coordinates.
While normally defined when the function `csetup` is called,
one may redefine the coordinates with the assignment
`ct_coords: [j1, j2, ..., jn]` where the j’s are the new coordinate names.
See also `csetup`.

<!-- category: Tensors -->
<!-- keywords: ct_coordsys -->
<!-- signatures: ct_coordsys(coordinate_system, extra_arg), ct_coordsys(coordinate_system) -->
### Function: ct_coordsys (coordinate_system, extra_arg)

Sets up a predefined coordinate system and metric. The argument
*coordinate_system* can be one of the following symbols:



```maxima
SYMBOL             Dim Coordinates     Description/comments
 ------------------------------------------------------------------
 cartesian2d           2  [x,y]             Cartesian 2D coordinate
                                            system
 polar                 2  [r,phi]           Polar coordinate system
 elliptic              2  [u,v]             Elliptic coord. system
 confocalelliptic      2  [u,v]             Confocal elliptic
                                            coordinates
 bipolar               2  [u,v]             Bipolar coord. system
 parabolic             2  [u,v]             Parabolic coord. system
 cartesian3d           3  [x,y,z]           Cartesian 3D coordinate
                                            system
 polarcylindrical      3  [r,theta,z]       Polar 2D with
                                            cylindrical z
 ellipticcylindrical   3  [u,v,z]           Elliptic 2D with
                                            cylindrical z
 confocalellipsoidal   3  [u,v,w]           Confocal ellipsoidal
 bipolarcylindrical    3  [u,v,z]           Bipolar 2D with
                                            cylindrical z
 paraboliccylindrical  3  [u,v,z]           Parabolic 2D with
                                            cylindrical z
 paraboloidal          3  [u,v,phi]         Paraboloidal coords.
 conical               3  [u,v,w]           Conical coordinates
 toroidal              3  [u,v,phi]         Toroidal coordinates
 spherical             3  [r,theta,phi]     Spherical coord. system
 oblatespheroidal      3  [u,v,phi]         Oblate spheroidal
                                            coordinates
 oblatespheroidalsqrt  3  [u,v,phi]
 prolatespheroidal     3  [u,v,phi]         Prolate spheroidal
                                            coordinates
 prolatespheroidalsqrt 3  [u,v,phi]
 ellipsoidal           3  [r,theta,phi]     Ellipsoidal coordinates
 cartesian4d           4  [x,y,z,t]         Cartesian 4D coordinate
                                            system
 spherical4d           4  [r,theta,eta,phi] Spherical 4D coordinate
                                            system
 exteriorschwarzschild 4  [t,r,theta,phi]   Schwarzschild metric
 interiorschwarzschild 4  [t,z,u,v]         Interior Schwarzschild
                                            metric
 kerr_newman           4  [t,r,theta,phi]   Charged axially
                                            symmetric metric
```


`coordinate_system` can also be a list of transformation functions,
followed by a list containing the coordinate variables. For instance,
you can specify a spherical metric as follows:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
                   r*sin(theta),[r,theta,phi]]);
(%o2)                                done
(%i3) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o3)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
(%i4) ct_coords;
(%o4)                           [r, theta, phi]
(%i5) dim;
(%o5)                                  3
```


Transformation functions can also be used when `cframe_flag` is 
`true`:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) cframe_flag:true;
(%o2)                                true
(%i3) ct_coordsys([r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),
      r*sin(theta),[r,theta,phi]]);
(%o3)                                done
(%i4) fri;
(%o4)
 [cos(phi)cos(theta) -cos(phi) r sin(theta) -sin(phi) r cos(theta)]
 [                                                                ]
 [sin(phi)cos(theta) -sin(phi) r sin(theta)  cos(phi) r cos(theta)]
 [                                                                ]
 [    sin(theta)           r cos(theta)                0          ]

(%i5) cmetric();
(%o5)                                false
(%i6) lg:trigsimp(lg);
                           [ 1  0         0        ]
                           [                       ]
                           [     2                 ]
(%o6)                      [ 0  r         0        ]
                           [                       ]
                           [         2    2        ]
                           [ 0  0   r  cos (theta) ]
```


The optional argument *extra_arg* can be any one of the following:




`cylindrical` tells `ct_coordsys` to attach an additional cylindrical 
coordinate.


`minkowski` tells `ct_coordsys` to attach an additional coordinate 
with negative metric signature.


`all` tells `ct_coordsys` to call `cmetric` and 
`christof(false)` after setting up the metric.



If the global variable `verbose` is set to `true`, `ct_coordsys` 
displays the values of `dim`, `ct_coords`, and either `lg` or 
`lfg` and `fri`, depending on the value of `cframe_flag`.

<!-- category: Tensors -->
<!-- keywords: ctaylor -->
<!-- signatures: ctaylor() -->
### Function: ctaylor ()

The `ctaylor` function truncates its argument by converting
it to a Taylor-series using `taylor`, and then calling
`ratdisrep`. This has the combined effect of dropping terms
higher order in the expansion variable `ctayvar`. The order
of terms that should be dropped is defined by `ctaypov`; the
point around which the series expansion is carried out is specified
in `ctaypt`.


As an example, consider a simple metric that is a perturbation of
the Minkowski metric. Without further restrictions, even a diagonal
metric produces expressions for the Einstein tensor that are far too
complex:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) ratfac:true;
(%o2)                                true
(%i3) derivabbrev:true;
(%o3)                                true
(%i4) ct_coords:[t,r,theta,phi];
(%o4)                         [t, r, theta, phi]
(%i5) lg:matrix([-1,0,0,0],[0,1,0,0],[0,0,r^2,0],
                [0,0,0,r^2*sin(theta)^2]);
                        [ - 1  0  0         0        ]
                        [                            ]
                        [  0   1  0         0        ]
                        [                            ]
(%o5)                   [          2                 ]
                        [  0   0  r         0        ]
                        [                            ]
                        [              2    2        ]
                        [  0   0  0   r  sin (theta) ]
(%i6) h:matrix([h11,0,0,0],[0,h22,0,0],[0,0,h33,0],[0,0,0,h44]);
                            [ h11   0    0    0  ]
                            [                    ]
                            [  0   h22   0    0  ]
(%o6)                       [                    ]
                            [  0    0   h33   0  ]
                            [                    ]
                            [  0    0    0   h44 ]
(%i7) depends(l,r);
(%o7)                               [l(r)]
(%i8) lg:lg+l*h;
      [ h11 l - 1      0          0                 0            ]
      [                                                          ]
      [     0      h22 l + 1      0                 0            ]
      [                                                          ]
(%o8) [                        2                                 ]
      [     0          0      r  + h33 l            0            ]
      [                                                          ]
      [                                    2    2                ]
      [     0          0          0       r  sin (theta) + h44 l ]
(%i9) cmetric(false);
(%o9)                                done
(%i10) einstein(false);
(%o10)                               done
(%i11) ntermst(ein);
[[1, 1], 62]
[[1, 2], 0]
[[1, 3], 0]
[[1, 4], 0]
[[2, 1], 0]
[[2, 2], 24]
[[2, 3], 0]
[[2, 4], 0]
[[3, 1], 0]
[[3, 2], 0]
[[3, 3], 46]
[[3, 4], 0]
[[4, 1], 0]
[[4, 2], 0]
[[4, 3], 0]
[[4, 4], 46]
(%o12)                               done
```


However, if we recompute this example as an approximation that is
linear in the variable `l`, we get much simpler expressions:



```maxima
(%i14) ctayswitch:true;
(%o14)                               true
(%i15) ctayvar:l;
(%o15)                                 l
(%i16) ctaypov:1;
(%o16)                                 1
(%i17) ctaypt:0;
(%o17)                                 0
(%i18) christof(false);
(%o18)                               done
(%i19) ricci(false);
(%o19)                               done
(%i20) einstein(false);
(%o20)                               done
(%i21) ntermst(ein);
[[1, 1], 6]
[[1, 2], 0]
[[1, 3], 0]
[[1, 4], 0]
[[2, 1], 0]
[[2, 2], 13]
[[2, 3], 2]
[[2, 4], 0]
[[3, 1], 0]
[[3, 2], 2]
[[3, 3], 9]
[[3, 4], 0]
[[4, 1], 0]
[[4, 2], 0]
[[4, 3], 0]
[[4, 4], 9]
(%o21)                               done
(%i22) ratsimp(ein[1,1]);
                         2      2  4               2     2
(%o22) - (((h11 h22 - h11 ) (l )  r  - 2 h33 l    r ) sin (theta)
                              r               r r

                            2               2      4    2
              - 2 h44 l    r  - h33 h44 (l ) )/(4 r  sin (theta))
                       r r                r
```


This capability can be useful, for instance, when working in the weak
field limit far from a gravitational source.

<!-- category: Tensors -->
<!-- keywords: ctaypov -->
<!-- signatures: ctaypov -->
### Variable: ctaypov

Maximum power used in Taylor-series expansion when `ctayswitch` is
set to `true`.

<!-- category: Tensors -->
<!-- keywords: ctaypt -->
<!-- signatures: ctaypt -->
### Variable: ctaypt

Point around which Taylor-series expansion is carried out when
`ctayswitch` is set to `true`.

<!-- category: Tensors -->
<!-- keywords: ctayswitch -->
<!-- signatures: ctayswitch -->
### Variable: ctayswitch

If set to `true`, causes some `ctensor` computations to be carried out
using Taylor-series expansions. Presently, `christof`, `ricci`,
`uricci`, `einstein`, and `weyl` take into account this
setting.

<!-- category: Tensors -->
<!-- keywords: ctayvar -->
<!-- signatures: ctayvar -->
### Variable: ctayvar

Variable used for Taylor-series expansion if `ctayswitch` is set to
`true`.

<!-- category: Tensors -->
<!-- keywords: ctorsion_flag -->
<!-- signatures: ctorsion_flag -->
### Variable: ctorsion_flag

Causes the contortion tensor to be included in the computation of the
connection coefficients. The contortion tensor itself is computed by
`contortion` from the user-supplied tensor `tr`.

<!-- category: Tensors -->
<!-- keywords: ctransform -->
<!-- signatures: ctransform(M) -->
### Function: ctransform (M)

A function in the `ctensor` (component tensor)
package which will perform a coordinate transformation
upon an arbitrary square symmetric matrix *M*. The user must input the
functions which define the transformation.  (Formerly called `transform`.)

<!-- category: Tensors -->
<!-- keywords: ctrgsimp -->
<!-- signatures: ctrgsimp -->
### Variable: ctrgsimp

Causes trigonometric simplifications to be used when tensors are computed. 
Presently, `ctrgsimp` affects only computations involving a moving frame.

<!-- category: Tensors -->
<!-- keywords: decsym -->
<!-- signatures: decsym(tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...]) -->
### Function: decsym (tensor, m, n, [cov_1, cov_2, ...], [contr_1, contr_2, ...])

Definiert Symmetrieeigenschaften fur den Tensor *tensor* mit *m*
kovarianten und *n* kontravarianten Indizes.  Die Argumente *cov_i* und
*contr_i* geben Symmetrieeigenschaften zwischen den kontravarianten und
kontravarianten Indizes an.  Die Argumente haben die Form
`symoper(index_1, index_2, ...`.  `symoper` ist einer der
Symmetrieeigenschaften `sym` fur symmetrisch, `anti` fur
antisymmetrisch oder `cyc` fur zyklisch und die Argumente *index_i*
sind ganze Zahlen, die die Position des Index im Tensor *tensor* angegeben.
Weiterhin ist die Form `symoper(all)` moglich.  In diesem Fall wird
die entsprechende Symmetrieeigenschaft fur alle Indizes angenommen.


Ist zum Beispiel `b` ein Tensor mit 5 kovarianten Indizes, dann wird mit
`decsym(b, 5, 3, [sym(1,2), anti(3,4)], [cyc(all)])` definiert, dass
`b` symmetrisch in den Indizes `1` und `2`, antisymmetrisch in
den Indizes `3` und `4` sowie zyklisch in allen kontravarianten
Indizes ist.


Symmetrieeigenschaften, die mit der Funktion `decsym` definiert werden,
werden von der Funktion `canform` angewendet.


Beispiele:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:contract( expand( a([i1, j1, k1], [])
           *kdels([i, j, k], [i1, j1, k1])))$
(%i3) ishow(expr)$
(%t3)         a      + a      + a      + a      + a      + a
               k j i    k i j    j k i    j i k    i k j    i j k
(%i4) decsym(a,3,0,[sym(all)],[]);
(%o4)                                done
(%i5) ishow(canform(expr))$
(%t5)                              6 a
                                      i j k
(%i6) remsym(a,3,0);
(%o6)                                done
(%i7) decsym(a,3,0,[anti(all)],[]);
(%o7)                                done
(%i8) ishow(canform(expr))$
(%t8)                                  0
(%i9) remsym(a,3,0);
(%o9)                                done
(%i10) decsym(a,3,0,[cyc(all)],[]);
(%o10)                               done
(%i11) ishow(canform(expr))$

(%t11)                        3 a      + 3 a
                                 i k j      i j k

(%i12) dispsym(a,3,0);
(%o12)                     [[cyc, [[1, 2, 3]], []]]
```

See also: `canform`.

<!-- category: Tensors -->
<!-- keywords: defcon -->
<!-- signatures: defcon(tensor_1), defcon(tensor_1, tensor_2, tensor_3) -->
### Function: defcon (tensor_1)

Gibt einem Tensor *tensor_1* die Eigenschaft, dass die Tensorverjungung
des Produktes *tensor_1* mit *tensor_2* das Ergebnis *tensor_3*
hat.  Wird nur ein Argument *tensor_1* angegeben, dann hat die
Tensorverjungung fur jeden Tensor `tensor`, der die korrekten
Indizes hat, das Ergebnis `tensor` mit neuen Indizes, die die
Tensorverjungung widerspiegeln.





Wird zum Beispiel die Metrik als `imetric: g` gesetzt, dann wird
mit `defcon(g)` das Hochstellen und Herunterstellen der Indizes mit dem
Metriktensor definiert.





Wird `defcon` wiederholt fur einen Tensor aufgerufen, ist jeweils die
letzte Definition wirksam.





Die Liste `contractions` enthalt die Tensoren, die mit der Funktion
`defcon` die Eigenschaft einer Tensorverjungung erhalten haben.

See also: `contractions`.

<!-- category: Tensors -->
<!-- keywords: deleten -->
<!-- signatures: deleten(L, n) -->
### Function: deleten (L, n)

Returns a new list consisting of *L* with the *n*’th element
deleted.

<!-- category: Tensors -->
<!-- keywords: diagmatrixp -->
<!-- signatures: diagmatrixp(M) -->
### Function: diagmatrixp (M)

Returns `true` if *M* is a diagonal matrix or (2D) array.

<!-- category: Tensors -->
<!-- keywords: diagmetric -->
<!-- signatures: diagmetric -->
### Variable: diagmetric

Default value: `false`


An option in the `ctensor` (component tensor)
package.  If `diagmetric` is `true` special routines compute
all geometrical objects (which contain the metric tensor explicitly)
by taking into consideration the diagonality of the metric. Reduced
run times will, of course, result. Note: this option is set
automatically by `csetup` if a diagonal metric is specified.

<!-- category: Tensors -->
<!-- keywords: dim -->
<!-- signatures: dim -->
### Variable: dim

Default value: 4


An option in the `ctensor` (component tensor)
package.  `dim` is the dimension of the manifold with the
default 4. The command `dim: n` will reset the dimension to any other
value `n`.

<!-- category: Tensors -->
<!-- keywords: dispcon -->
<!-- signatures: dispcon(tensor_1, tensor_2, ...), dispcon(all) -->
### Function: dispcon (tensor_1, tensor_2, ...)

Zeigt die Kontraktionseigenschaften der Tensoren *tensor_1*, *tensor_2*,
... wie sie mit der Funktion `defcon` definiert wurden.  Das Kommando
`dispcon(all)` zeigt alle vom Nutzer definierten Kontraktionseigenschaften.


Beispiel:


Wird das Paket `itensor` geladen, gibt `dispcon` das folgende
Ergebnis.



```maxima
(%i1) load("itensor")$

(%i2) dispcon(all);
(%o2)      [[[ifr, ifri, ifg]], [[ifg, ifg, kdelta]]]
```

See also: `defcon`.

<!-- category: Tensors -->
<!-- keywords: dscalar -->
<!-- signatures: dscalar() -->
### Function: dscalar ()

computes the tensor d’Alembertian of the scalar function once
dependencies have been declared upon the function. For example:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) depends(p,r);
(%o4)                               [p(r)]
(%i5) factor(dscalar(p));
                          2
                    p    r  - 2 m p    r + 2 p  r - 2 m p
                     r r           r r        r          r
(%o5)               --------------------------------------
                                       2
                                      r
```

<!-- category: Tensors -->
<!-- keywords: einstein -->
<!-- signatures: einstein(dis) -->
### Function: einstein (dis)

A function in the `ctensor` (component tensor) package.  `einstein` 
computes the mixed Einstein tensor after the Christoffel symbols and Ricci 
tensor have been obtained (with the functions `christof` and `ricci`).
If the argument *dis* is `true`, then the non-zero values of the mixed 
Einstein tensor `ein[i,j]` will be displayed where `j` is the 
contravariant index.  The variable `rateinstein` will cause the rational 
simplification on these components. If `ratfac` is `true` then the 
components will also be factored.

<!-- category: Tensors -->
<!-- keywords: entertensor -->
<!-- signatures: entertensor(name) -->
### Function: entertensor (name)

Die Funktion `entertensor` ermoglicht die Eingabe eines indizierten
Tensors mit einer beliebigen Anzahl an Tensorindizes und Ableitungen.  Es kann
ein einzelner Index oder eine Liste mit Indizes angegeben werden.  Die Liste
kann eine leere Liste sein.


Beispiel:



```maxima
(%i1) load("itensor")$

(%i2) entertensor()$
Enter tensor name: a;
Enter a list of the covariant indices: [i,j];
Enter a list of the contravariant indices: [k];
Enter a list of the derivative indices: [];
                               k
(%t2)                         a
                               i j
```

<!-- category: Tensors -->
<!-- keywords: evundiff -->
<!-- signatures: evundiff(expr) -->
### Function: evundiff (expr)

Ist aquivalent zur Ausfuhrung der Funktion `undiff`, der die
Funktionen `ev` und `rediff` nachfolgen.






`evundiff` erlaubt die Auswertung von Ausdrucken, die nicht direkt in
ihrer abgeleiteten Form ausgewertet werden konnen.  So fuhrt das folgende
Beispiel zu einer Fehlermeldung:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) icurvature([i,j,k],[l],m);
Maxima encountered a Lisp error:

 Error in $ICURVATURE [or a callee]:
 $ICURVATURE [or a callee] requires less than three arguments.

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
```





Wird jedoch `icurvature` in der Substantivform verwendet, kann der
Ausdruck mit `evundiff` ausgewertet werden:



```maxima
(%i3) ishow('icurvature([i,j,k],[l],m))$

                                         l
(%t3)                          icurvature
                                         i j k,m

(%i4) ishow(evundiff(%))$
             l              l         %1           l           %1
(%t4) - ichr2        - ichr2     ichr2      - ichr2       ichr2
             i k,j m        %1 j      i k,m        %1 j,m      i k

             l              l         %1           l           %1
      + ichr2        + ichr2     ichr2      + ichr2       ichr2
             i j,k m        %1 k      i j,m        %1 k,m      i j
```






Um Christoffel-Symbole abzuleiten, wird die Funktion `evundiff`
nicht benotigt:



```maxima
(%i5) imetric(g);
(%o5)                                done
(%i6) ishow(ichr2([i,j],[k],l))$

       k %3
      g     (g         - g         + g        )
              j %3,i l    i j,%3 l    i %3,j l
(%t6) -----------------------------------------
                          2


                         k %3
                        g     (g       - g       + g      )
                         ,l     j %3,i    i j,%3    i %3,j
                      + -----------------------------------
                                         2
```

See also: `undiff`, `ev`, `rediff`.

<!-- category: Tensors -->
<!-- keywords: extdiff -->
<!-- signatures: extdiff(expr, i) -->
### Function: extdiff (expr, i)

Computes the exterior derivative of *expr* with respect to the index
*i*. The exterior derivative is formally defined as the wedge
product of the partial derivative operator and a differential form. As
such, this operation is also controlled by the setting of `igeowedge_flag`.
For instance:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(extdiff(v([i]),j))$
                                  v    - v
                                   j,i    i,j
(%t2)                             -----------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(extdiff(a([i,j]),k))$
                           a      - a      + a
                            j k,i    i k,j    i j,k
(%t4)                      ------------------------
                                      3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(extdiff(v([i]),j))$
(%t6)                             v    - v
                                   j,i    i,j
(%i7) ishow(extdiff(a([i,j]),k))$
(%t7)                    - (a      - a      + a     )
                             k j,i    k i,j    j i,k
```

<!-- category: Tensors -->
<!-- keywords: fb -->
<!-- signatures: fb -->
### Variable: fb

Frame bracket coefficients, as computed by `frame_bracket`.

<!-- category: Tensors -->
<!-- keywords: findde -->
<!-- signatures: findde(A, n) -->
### Function: findde (A, n)

returns a list of the unique differential equations (expressions)
corresponding to the elements of the *n* dimensional square
array *A*. Presently, *n* may be 2 or 3. `deindex` is a global list
containing the indices of *A* corresponding to these unique
differential equations. For the Einstein tensor (`ein`), which
is a two dimensional array, if computed for the metric in the example
below, `findde` gives the following independent differential equations:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) derivabbrev:true;
(%o2)                                true
(%i3) dim:4;
(%o3)                                  4
(%i4) lg:matrix([a, 0, 0, 0], [ 0, x^2, 0, 0],
                              [0, 0, x^2*sin(y)^2, 0], [0,0,0,-d]);
                          [ a  0       0        0  ]
                          [                        ]
                          [     2                  ]
                          [ 0  x       0        0  ]
(%o4)                     [                        ]
                          [         2    2         ]
                          [ 0  0   x  sin (y)   0  ]
                          [                        ]
                          [ 0  0       0       - d ]
(%i5) depends([a,d],x);
(%o5)                            [a(x), d(x)]
(%i6) ct_coords:[x,y,z,t];
(%o6)                            [x, y, z, t]
(%i7) cmetric();
(%o7)                                done
(%i8) einstein(false);
(%o8)                                done
(%i9) findde(ein,2);
                                            2
(%o9) [d  x - a d + d, 2 a d d    x - a (d )  x - a  d d  x
        x                     x x         x        x    x

                                              2          2
                          + 2 a d d   - 2 a  d , a  x + a  - a]
                                   x       x      x
(%i10) deindex;
(%o10)                     [[1, 1], [2, 2], [4, 4]]
```

<!-- category: Tensors -->
<!-- keywords: flipflag -->
<!-- signatures: flipflag -->
### Variable: flipflag

Standardwert: `false`






Hat die Optionsvariable `flipflag` den Wert `false`, werden die
Indizes von der Funktion `rename` bei der Umbenennung in der Reihenfolge
der kontravarianten Indizes sortiert, ansonsten in der Reihenfolge der
kovarianten Indizes.


Siehe auch das Beispiel fur die Funktion `rename`.

See also: `rename`.

<!-- category: Tensors -->
<!-- keywords: flush -->
<!-- signatures: flush(expr, tensor_1, tensor_2, ...) -->
### Function: flush (expr, tensor_1, tensor_2, ...)

Alle tensoriellen Großen *tensor_i* die im Ausdruck *expr*
auftreten und keine Ableitungen haben, werden zu Null gesetzt.

<!-- category: Tensors -->
<!-- keywords: flush1deriv -->
<!-- signatures: flush1deriv(expr, tensor) -->
### Function: flush1deriv (expr, tensor)

Setzt alle tensoriellen Großen, die genau einen Ableitungsindex haben,
auf den Wert Null.

<!-- category: Tensors -->
<!-- keywords: flushd -->
<!-- signatures: flushd(expr, tensor_1, tensor_2, ...) -->
### Function: flushd (expr, tensor_1, tensor_2, ...)

Alle tensoriellen Großen *tensor_i* die im Ausdruck *expr*
auftreten und Ableitungen haben, werden zu Null gesetzt.

<!-- category: Tensors -->
<!-- keywords: flushnd -->
<!-- signatures: flushnd(expr, tensor, n) -->
### Function: flushnd (expr, tensor, n)

Setzt alle Ableitungen der tensoriellen Große *tensor* die im Ausdruck
*expr* auftritt und *n* oder mehr Ableitungen hat, auf den Wert Null.


Beispiele:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i],[J,r],k,r)+a([i],[j,r,s],k,r,s))$
                                J r      j r s
(%t2)                          a      + a
                                i,k r    i,k r s
(%i3) ishow(flushnd(%,a,3))$
                                     J r
(%t3)                               a
                                     i,k r
```

<!-- category: Tensors -->
<!-- keywords: frame_bracket -->
<!-- signatures: frame_bracket(fr, fri, diagframe) -->
### Function: frame_bracket (fr, fri, diagframe)

The frame bracket (`fb[]`).


Computes the frame bracket according to the following definition:



```maxima
c          c         c        d     e
ifb   = ( ifri    - ifri    ) ifr   ifr
   ab         d,e       e,d      a     b
```

<!-- category: Tensors -->
<!-- keywords: gdet -->
<!-- signatures: gdet -->
### Variable: gdet

The determinant of the metric tensor `lg`. Computed by `cmetric` when
`cframe_flag` is set to `false`.

<!-- category: Tensors -->
<!-- keywords: hodge -->
<!-- signatures: hodge(expr) -->
### Function: hodge (expr)

Compute the Hodge-dual of *expr*. For instance:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                            done
(%i3) idim(4);
(%o3)                            done
(%i4) icounter:100;
(%o4)                             100
(%i5) decsym(A,3,0,[anti(all)],[])$

(%i6) ishow(A([i,j,k],[]))$
(%t6)                           A
                                 i j k
(%i7) ishow(canform(hodge(%)))$

                          %1 %2 %3 %4
               levi_civita            g        A
                                       %1 %102  %2 %3 %4
(%t7)          -----------------------------------------
                                   6

(%i8) ishow(canform(hodge(%)))$
                 %1 %2 %3 %8            %4 %5 %6 %7
(%t8) levi_civita            levi_civita            g       
                                                     %1 %106
                             g        g        g      A         /6
                              %2 %107  %3 %108  %4 %8  %5 %6 %7
(%i9) lc2kdt(%)$

(%i10) %,kdelta$

(%i11) ishow(canform(contract(expand(%))))$
(%t11)                     - A
                              %106 %107 %108
```

<!-- category: Tensors -->
<!-- keywords: ic_convert -->
<!-- signatures: ic_convert(eqn) -->
### Function: ic_convert (eqn)

Konvertiert eine `itensor`-Gleichung *eqn* in einen
`ctensor`-Ausdruck.  Implizite Summen uber Dummy-Indizes werden explizit
ausgefuhrt und indizierte Großen werden in Arrays umgewandelt.  Die
Indizes der Arrays sind in der Reihenfolge der kovarianten und dann der
kontravarianten Indizes der indizierte Große.  Die Ableitung einer
indizierten Große wird durch die Substantivform der Ableitung
`diff` nach der Variablen `ct_coords` ersetzt, die den Index der
Ableitung erhalt.  Die Christoffel-Symbole `ichr1` und `ichr2`
werden zu den Funktionen `lcs` und `mcs` transformiert.  Hat
`metricconvert` den Wert `true`, dann wird der Metriktensor mit zwei
kovarianten Indizes durch `lg` und mit zwei kontravarianten Indizes durch
`ug` ersetzt.  Weiterhin werden `do`-Schleifen fur die Summation
uber die freien Indizes eingefuhrt.


Beispiele:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) eqn:ishow(t([i,j],[k])=f([],[])*g([l,m],[])*a([],[m],j)
      *b([i],[l,k]))$
                             k        m   l k
(%t2)                       t    = f a   b    g
                             i j      ,j  i    l m
(%i3) ic_convert(eqn);

(%o3) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 g    , l, 1, dim), m, 1, dim)))
  l, m

(%i4) imetric(g);
(%o4)                                done
(%i5) metricconvert:true;
(%o5)                                true
(%i6) ic_convert(eqn);

(%o6) for i thru dim do (for j thru dim do (
       for k thru dim do
        t        : f sum(sum(diff(a , ct_coords ) b
         i, j, k                   m           j   i, l, k

 lg    , l, 1, dim), m, 1, dim)))
   l, m
```

See also: `diff`, `ct_coords`, `ichr1`, `ichr2`, `lg`, `ug`.

<!-- category: Tensors -->
<!-- keywords: icc1 -->
<!-- signatures: icc1 -->
### Variable: icc1

Connection coefficients of the first kind.  In `itensor`, defined as



```maxima
icc1    = ichr1    - ikt1    - inmc1
    abc        abc       abc        abc
```


In this expression, if `iframe_flag` is true, the Christoffel-symbol
`ichr1` is replaced with the frame connection coefficient `ifc1`.
If `itorsion_flag` is `false`, `ikt1`
will be omitted.  It is also omitted if a frame base is used, as the
torsion is already calculated as part of the frame bracket.
Lastly, of `inonmet_flag` is `false`,
`inmc1` will not be present.

<!-- category: Tensors -->
<!-- keywords: icc2 -->
<!-- signatures: icc2 -->
### Variable: icc2

Connection coefficients of the second kind.  In `itensor`, defined as



```maxima
c         c        c         c
icc2   = ichr2   - ikt2   - inmc2
    ab        ab       ab        ab
```


In this expression, if `iframe_flag` is true, the Christoffel-symbol
`ichr2` is replaced with the frame connection coefficient `ifc2`.
If `itorsion_flag` is `false`, `ikt2`
will be omitted.  It is also omitted if a frame base is used, as the
torsion is already calculated as part of the frame bracket.
Lastly, of `inonmet_flag` is `false`,
`inmc2` will not be present.

<!-- category: Tensors -->
<!-- keywords: ichr1 -->
<!-- signatures: ichr1([i, j, k]) -->
### Function: ichr1 ([i, j, k])

Gibt das Christoffel-Symbol der ersten Art zuruck, das definiert ist als



```maxima
(g      + g      - g     )/2 .
         ik,j     jk,i     ij,k
```





Um das Christoffel-Symbol fur eine spezielle Metrik auszuwerten, muss der
Optionsvariablen `imetric` ein Wert zugewiesen werden.  Siehe dazu das
Beispiel zu `ichr2`.

See also: `imetric`, `ichr2`.

<!-- category: Tensors -->
<!-- keywords: ichr2 -->
<!-- signatures: ichr2([i, j], [k]) -->
### Function: ichr2 ([i, j], [k])

Gibt das Christoffel-Symbol der zweiten Art zuruck, das definiert ist als



```maxima
ks
   ichr2([i,j],[k]) = g    (g      + g      - g     )/2
                             is,j     js,i     ij,s
```

<!-- category: Tensors -->
<!-- keywords: icounter -->
<!-- signatures: icounter -->
### Variable: icounter

Standardwert: `0`






Enthalt die laufende Nummer, um den nachsten Dummy-Index zu bilden.
`icounter` wird automatisch erhoht, bevor der neue Index gebildet wird.
Dem Wert `icounter` wird er Prafix `idummyx` vorangestellt.  Der
Standardwert von `idummyx` ist `%`.

See also: `idummyx`.

<!-- category: Tensors -->
<!-- keywords: icurvature -->
<!-- signatures: icurvature([i, j, k], [h]) -->
### Function: icurvature ([i, j, k], [h])

Gibt den Riemannschen Krummungstensor in einer Darstellung mit
Christoffel-Symbolen zuruck:



```maxima
h             h            h         %1         h
  icurvature     = - ichr2      - ichr2     ichr2    + ichr2
            i j k         i k,j        %1 j      i k        i j,k
                            h          %1
                     + ichr2      ichr2
                            %1 k       i j
```

<!-- category: Tensors -->
<!-- keywords: idiff -->
<!-- signatures: idiff(expr, v_1, [n_1, [v_2, n_2]...]) -->
### Function: idiff (expr, v_1, [n_1, [v_2, n_2]...])

`idiff` fuhrt Ableitungen nach den Koordinaten einer tensoriellen
Große aus.  Im Unterschied dazu fuhrt die Funktion `diff`
Ableitungen nach den unabhangigen Variablen aus.  Eine tensorielle Große
erhalt zusatzlich den Index *v_1*, der die Ableitung bezeichnet.
Mehrfache Indizes fur Ableitungen werden sortiert, außer wenn die
Optionsvariable `iframe_flag` den Wert `true` hat.








`idiff` kann auch die Determinante des Metriktensors ableiten.  Wird zum
Beispiel der Optionsvariablen `imetric` der Wert `g` zugewiesen,
dann hat das Kommando `idiff(determinant(g), k)` das Ergebnis
`2 * determinant(g) * ichr2([%i,k], [%i])`, wobei die Dummy-Variable
passend gewahlt wird.

See also: `diff`, `iframe_flag`, `imetric`.

<!-- category: Tensors -->
<!-- keywords: idim -->
<!-- signatures: idim(n) -->
### Function: idim (n)

Die Funktion `idim` setzt die Dimension der Metrik zu *n*.  Die
Variable `dim` auf den Wert *n* gesetzt und die antisymmetrischen
Eigenschaften des Levi-Civita-Symbols fur die Dimension *n*
werden initialisiert.

<!-- category: Tensors -->
<!-- keywords: idummy -->
<!-- signatures: idummy() -->
### Function: idummy ()

Erhoht den Wert der laufenden Nummer `icounter` und gibt einen neuen
Index zuruck, indem der Prafix `idummyx` der Nummer `icounter`
vorangestellt wird.  Siehe auch die Funktion `indices`.

See also: `icounter`, `idummyx`, `indices`.

<!-- category: Tensors -->
<!-- keywords: idummyx -->
<!-- signatures: idummyx -->
### Variable: idummyx

Standardwert: `%`




Enthalt den Prafix, der einem neuen Index vorangestellt wird, der mit der
Funktion `idummy` gebildet wird.

See also: `idummy`.

<!-- category: Tensors -->
<!-- keywords: ifb -->
<!-- signatures: ifb -->
### Variable: ifb

The frame bracket.  The contribution of the frame metric to the connection
coefficients is expressed using the frame bracket:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                  2
```


The frame bracket itself is defined in terms of the frame field and frame
metric.  Two alternate methods of computation are used depending on the
value of `frame_bracket_form`.  If true (the default) or if the
`itorsion_flag` is `true`:



```maxima
d      e                                      f
ifb =  ifr    ifr   (ifri      - ifri      - ifri    itr   )
   abc    b      c       a d,e       a e,d       a f    d e
```


Otherwise:



```maxima
e      d        d      e
ifb    = (ifr    ifr    - ifr    ifr   ) ifri
   abc       b      c,e      b,e    c        a d
```

<!-- category: Tensors -->
<!-- keywords: ifc1 -->
<!-- signatures: ifc1 -->
### Variable: ifc1

Frame coefficient of the first kind (also known as Ricci-rotation
coefficients.) This tensor represents the contribution
of the frame metric to the connection coefficient of the first kind.  Defined
as:



```maxima
- ifb      + ifb      + ifb
               c a b      b c a      a b c
ifc1    = --------------------------------
    abc                   2
```

<!-- category: Tensors -->
<!-- keywords: ifc2 -->
<!-- signatures: ifc2 -->
### Variable: ifc2

Frame coefficient of the first kind.  This tensor represents the contribution
of the frame metric to the connection coefficient of the first kind.  Defined
as a permutation of the frame bracket (`ifb`) with the appropriate
indices raised and lowered as necessary:



```maxima
c       cd
ifc2   = ifg   ifc1
    ab             abd
```

<!-- category: Tensors -->
<!-- keywords: ifg -->
<!-- signatures: ifg -->
### Variable: ifg

The frame metric.  Defaults to `kdelta`, but can be changed using
`components`.

<!-- category: Tensors -->
<!-- keywords: ifgi -->
<!-- signatures: ifgi -->
### Variable: ifgi

The inverse frame metric.  Contracts with the frame metric (`ifg`)
to `kdelta`.

<!-- category: Tensors -->
<!-- keywords: ifr -->
<!-- signatures: ifr -->
### Variable: ifr

The frame field.  Contracts with the inverse frame field (`ifri`) to
form the frame metric (`ifg`).

<!-- category: Tensors -->
<!-- keywords: iframe_bracket_form -->
<!-- signatures: iframe_bracket_form -->
### Variable: iframe_bracket_form

Default value: `true`


Specifies how the frame bracket (`ifb`) is computed.

<!-- category: Tensors -->
<!-- keywords: iframe_flag -->
<!-- signatures: iframe_flag -->
### Variable: iframe_flag

Standardwert: `false`


To use frames, you must first set `iframe_flag` to `true`.  This
causes the Christoffel-symbols, `ichr1` and `ichr2`, to be replaced
by the more general frame connection coefficients `icc1` and `icc2`
in calculations.  Speficially, the behavior of `covdiff` and
`icurvature` is changed.


The frame is defined by two tensors: the inverse frame field (`ifri`,
the dual basis tetrad),
and the frame metric `ifg`.  The frame metric is the identity matrix for
orthonormal frames, or the Lorentz metric for orthonormal frames in Minkowski
spacetime.  The inverse frame field defines the frame base (unit vectors).
Contraction properties are defined for the frame field and the frame metric.


When `iframe_flag` is true, many `itensor` expressions use the frame
metric `ifg` instead of the metric defined by `imetric` for
raising and lowerind indices.


IMPORTANT: Setting the variable `iframe_flag` to `true` does NOT
undefine the contraction properties of a metric defined by a call to
`defcon` or `imetric`.  If a frame field is used, it is best to
define the metric by assigning its name to the variable `imetric`
and NOT invoke the `imetric` function.

<!-- category: Tensors -->
<!-- keywords: iframes -->
<!-- signatures: iframes() -->
### Function: iframes ()

Since in this version of Maxima, contraction identities for `ifr` and
`ifri` are always defined, as is the frame bracket (`ifb`), this
function does nothing.

<!-- category: Tensors -->
<!-- keywords: ifri -->
<!-- signatures: ifri -->
### Variable: ifri

The inverse frame field.  Specifies the frame base (dual basis vectors).  Along
with the frame metric, it forms the basis of all calculations based on
frames.

<!-- category: Tensors -->
<!-- keywords: igeodesic_coords -->
<!-- signatures: igeodesic_coords(expr, name) -->
### Function: igeodesic_coords (expr, name)

Bewirkt, dass nicht abgeleitete Christoffel-Symbole und erste Ableitungen des
Metriktensors im Ausdruck *expr* verschwinden.  Das Argument *name*
bezeichnet die Metrik *name*, wenn im Ausdruck *expr* vorhanden und die
Christoffel-Symbole werden mit *ichr1* und *ichr2* bezeichnet.







Beispiele:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(icurvature([r,s,t],[u]))$

             u            u         %1         u     
(%t2) - ichr2      - ichr2     ichr2    + ichr2      
             r t,s        %1 s      r t        r s,t 

                                              u         %1
                                       + ichr2     ichr2
                                              %1 t      r s

(%i3) ishow(igeodesic_coords(%,ichr2))$
                                 u            u
(%t3)                       ichr2      - ichr2
                                 r s,t        r t,s
(%i4) ishow(igeodesic_coords(icurvature([r,s,t],[u]),ichr2)+
            igeodesic_coords(icurvature([s,t,r],[u]),ichr2)+
            igeodesic_coords(icurvature([t,r,s],[u]),ichr2))$
             u            u            u            u
(%t4) - ichr2      + ichr2      + ichr2      - ichr2
             t s,r        t r,s        s t,r        s r,t

                                             u            u
                                      - ichr2      + ichr2
                                             r t,s        r s,t
(%i5) canform(%);
(%o5)                                  0
```

<!-- category: Tensors -->
<!-- keywords: igeowedge_flag -->
<!-- signatures: igeowedge_flag -->
### Variable: igeowedge_flag

Default value: `false`


Controls the behavior of the wedge product and exterior derivative. When
set to `false` (the default), the notion of differential forms will
correspond with that of a totally antisymmetric covariant tensor field.
When set to `true`, differential forms will agree with the notion
of the volume element.

<!-- category: Tensors -->
<!-- keywords: ikt1 -->
<!-- signatures: ikt1 -->
### Variable: ikt1

Covariant permutation of the torsion tensor (also known as contorsion).
Defined as:



```maxima
d           d       d
          -g   itr  - g    itr   - itr   g
            ad    cb    bd    ca      ab  cd
ikt1    = ----------------------------------
    abc                   2
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

<!-- category: Tensors -->
<!-- keywords: ikt2 -->
<!-- signatures: ikt2 -->
### Variable: ikt2

Contravariant permutation of the torsion tensor (also known as contorsion).
Defined as:



```maxima
c     cd
ikt2   = g   ikt1
    ab           abd
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

<!-- category: Tensors -->
<!-- keywords: imetric -->
<!-- signatures: imetric(g) -->
### Function: imetric (g)

Spezifiziert die Metrik, indem der Variablen `imetric` der Wert `g`
zugewiesen wird.  Die Eigenschaften fur die Verjungung von Tensoren werden
mit den Kommandos `defcon(g)` und
`defcon(g, g, kdelta)` initialisiert.

<!-- category: Tensors -->
<!-- keywords: indexed_tensor -->
<!-- signatures: indexed_tensor(tensor) -->
### Function: indexed_tensor (tensor)

Muss ausgefuhrt werden, bevor einem Tensors *tensor* Komponenten
zugewiesen werden, fur die bereits interne Werte vorliegen wie fur
`ichr1`, `ichr2` oder `icurvature`.  Siehe das Beispiel
zur Funktion `icurvature`.

See also: `ichr1`, `ichr2`, `icurvature`.

<!-- category: Tensors -->
<!-- keywords: indices -->
<!-- signatures: indices(expr) -->
### Function: indices (expr)

Gibt eine Liste mit zwei Elementen zuruck.  Das erste Element ist eine Liste
mit den Indizes im Ausdruck *expr* die frei sind, also nur einmal auftreten.
Das zweite Elemente ist eine Liste mit den Indizes, uber die summiert wird,
die also im Ausdruck genau zweimal auftreten.







Ein Tensorprodukt mit einem Index der mehr als zweimal auftritt, ist nicht
korrekt formuliert.  Die Funktion `indices` gibt in einem solchen Fall
jedoch keinen Fehler aus.


Beispiel:



```maxima
(%i1) load("itensor")$

(%i2) ishow(a([i,j],[k,l],m,n)*b([k,o],[j,m,p],q,r))$
                         k l      j m p
(%t2)                   a        b
                         i j,m n  k o,q r
(%i3) indices(%);
(%o3)          [[l, p, i, n, o, q, r], [k, j, m]]
```

<!-- category: Tensors -->
<!-- keywords: init_atensor -->
<!-- signatures: init_atensor(alg_type, opt_dims), init_atensor(alg_type) -->
### Function: init_atensor (alg_type, opt_dims)

Initialisiert das Paket `atensor` mit der angegebenen Algebra
*alg_type*.  Das Argument *alg_type* kann einen der folgenden
Werte haben:



**universal** — Eine allgemeine Algebra, fur die keine Vertauschungsregeln definiert sind.
**grassmann** — Eine Graßmann-Algebra, fur die die Vertauschungsregel `u.v + v.u = 0`
definiert ist.
**clifford** — Eine Clifford-Algebra, die durch die Vertauschungsregel `u.v + v.u = -2*sf(u,v)` definiert ist.  Die Bilinearform `sf` ist eine symmetrische
Funktion, die einen skalaren Wert als Ergebnis hat.  Das Argument *opt_dims*
kann bis zu drei positive ganze Zahlen sein, die die positiven, 
entarteten und negativen Dimensionen der Algebra bezeichnen.  Die Dimension
`adim` und die Matrix `aform` werden entsprechend der angegebenen
Argumente *opt_dims* initialisiert.  Sind keine Argumente *opt_dims*
vorhanden, wird die Dimension `adim` zu Null initialisiert und keine
Matrix `aform` definiert.
**symmetric** — Eine symmetrische Algebra, die durch die Vertauschungsregel `u.v - v.u = 0`
definiert ist.
**symplectic** — Eine symplektische Algebra, die durch die Vertauschungsregel
`u.v - v.u = 2*af(u,v)` definiert ist.  Die Bilinearform `af` ist
eine antisymmetrische Funktion, die einen skalaren Wert als Ergebnis hat.  Das 
Argument *opt_dims* kann bis zu zwei positive ganze Zahlen enthalten,
die die nicht-degenerierten und degenerierten Dimensionen der Algebra
bezeichnen.  Die Dimension `adim` und die Matrix `aform`
werden entsprechend der angegebenen Argumente *opt_dims* initialisiert.
Sind keine Argumente *opt_dims* vorhanden, wird die Dimension `adim`
zu Null initialisiert und keine Matrix `aform` definiert.
**lie_envelop** — Eine einhullende Lie-Algebra, die durch die Vertauschungsregel
`u.v - v.u = 2*av(u,v)` definiert ist, wobei die Bilinearform `av`
eine antisymmetrische Funktion ist.  Das Argument *opt_dims* kann eine
positive ganze Zahl sein, welche die Dimension der Lie-Algebra angibt.  Die
Dimension `adim` und die Matrix `aform` werden entsprechend des
Argumentes *opt_dims* initialisiert.  Ist kein Argument *opt_dims*
vorhanden, wird die Dimension `adim` zu Null initialisiert und keine Matrix
`aform` definiert.





Die Funktion `init_atensor` kennt weiterhin einige vordefinierte
Algebren:



**complex** — Die Algebra der komplexen Zahlen, die als eine Clifford-Algebra Cl(0,1)
definiert wird.  Das Kommando `init_atensor(complex)` ist aquivalent zum
Kommando `init_atensor(clifford, 0, 0, 1)`.
**quaternion** — Die Algebra der Quaternionen, die als eine Clifford-Algebra vom Typ Cl(0,2)
definiert wird.  Das Kommando `init_atensor(quaternion)`
ist a­qui­va­lent zum Kommando `init_atensor(clifford, 0, 0, 2)`.
**pauli** — Die Algebra der Pauli-Matrizen, die als eine Clifford-Algebra Cl(3,0)
definiert wird.  Das Kommando `init_atensor(pauli)` ist aquivalent
zum Kommando `init_atensor(clifford, 3)`.
**dirac** — Die Algebra der Dirac-Matrizen, die als eine Clifford-Algebra Cl(3,0,1)
definiert wird.  Das Kommando `init_atensor(dirac)` ist aquivalent zum
Kommando `init_atensor(clifford, 3, 0, 1)`.

See also: `sf`, `adim`, `aform`, `af`, `av`.

<!-- category: Tensors -->
<!-- keywords: init_ctensor -->
<!-- signatures: init_ctensor() -->
### Function: init_ctensor ()

Initializes the `ctensor` package.


The `init_ctensor` function reinitializes the `ctensor` package. It 
removes all arrays and matrices used by `ctensor`, resets all flags, resets
`dim` to 4, and resets the frame metric to the Lorentz-frame.

<!-- category: Tensors -->
<!-- keywords: inm -->
<!-- signatures: inm -->
### Variable: inm

The nonmetricity vector. Conformal nonmetricity is defined through the
covariant derivative of the metric tensor. Normally zero, the metric
tensor’s covariant derivative will evaluate to the following when
`inonmet_flag` is set to `true`:



```maxima
g     =- g  inm
 ij;k     ij   k
```

<!-- category: Tensors -->
<!-- keywords: inmc1 -->
<!-- signatures: inmc1 -->
### Variable: inmc1

Covariant permutation of the nonmetricity vector components. Defined as



```maxima
g   inm  - inm  g   - g   inm
            ab    c      a  bc    ac    b
inmc1    = ------------------------------
     abc                 2
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

<!-- category: Tensors -->
<!-- keywords: inmc2 -->
<!-- signatures: inmc2 -->
### Variable: inmc2

Contravariant permutation of the nonmetricity vector components. Used
in the connection coefficients if `inonmet_flag` is `true`. Defined
as:



```maxima
c         c         cd
          -inm  kdelta  - kdelta  inm  + g   inm  g
     c        a       b         a    b          d  ab
inmc2   = -------------------------------------------
     ab                        2
```


(Substitute `ifg` in place of `g` if a frame metric is used.)

<!-- category: Tensors -->
<!-- keywords: invariant1 -->
<!-- signatures: invariant1() -->
### Function: invariant1 ()

generates the mixed Euler- Lagrange tensor (field equations) for the
invariant density of R^2. The field equations are the components of an
array named `inv1`.

<!-- category: Tensors -->
<!-- keywords: invariant2 -->
<!-- signatures: invariant2() -->
### Function: invariant2 ()

*** NOT YET IMPLEMENTED ***


generates the mixed Euler- Lagrange tensor (field equations) for the
invariant density of `ric[i,j]*uriem[i,j]`. The field equations are the
components of an array named `inv2`.

<!-- category: Tensors -->
<!-- keywords: ishow -->
<!-- signatures: ishow(expr) -->
### Function: ishow (expr)

Zeigt den Ausdruck *expr* an, wobei Tensoren im Ausdruck mit tiefgestellten
kovarianten Indizes und hochgestellten kontravarianten Indizes sowie die
Ableitungen mit durch ein Komma getrennten tiefgestellte Indizes angezeigt
werden.


Beispiel:



```maxima
(%i1) load("itensor")$

(%i2) ishow(a([i,j], [k], v,w))$
                             k
(%t2)                       a
                             i j,v w
```

<!-- category: Tensors -->
<!-- keywords: itr -->
<!-- signatures: itr -->
### Variable: itr

The torsion tensor. For a metric with torsion, repeated covariant
differentiation on a scalar function will not commute, as demonstrated
by the following example:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric:g;
(%o2)                                  g
(%i3) covdiff( covdiff( f( [], []), i), j)
                      - covdiff( covdiff( f( [], []), j), i)$
(%i4) ishow(%)$
                                   %4              %2
(%t4)                    f    ichr2    - f    ichr2
                          ,%4      j i    ,%2      i j
(%i5) canform(%);
(%o5)                                  0
(%i6) itorsion_flag:true;
(%o6)                                true
(%i7) covdiff( covdiff( f( [], []), i), j)
                      - covdiff( covdiff( f( [], []), j), i)$
(%i8) ishow(%)$
                           %8             %6
(%t8)             f    icc2    - f    icc2    - f     + f
                   ,%8     j i    ,%6     i j    ,j i    ,i j
(%i9) ishow(canform(%))$
                                   %1             %1
(%t9)                     f    icc2    - f    icc2
                           ,%1     j i    ,%1     i j
(%i10) ishow(canform(ev(%,icc2)))$

                                   %1             %1
(%t10)                    f    ikt2    - f    ikt2
                           ,%1     i j    ,%1     j i

(%i11) ishow(canform(ev(%,ikt2)))$
                      %2 %1                    %2 %1
(%t11)          f    g      ikt1       - f    g      ikt1
                 ,%2            i j %1    ,%2            j i %1
(%i12) ishow(factor(canform(rename(expand(ev(%,ikt1))))))$
                           %3 %2            %1       %1
                     f    g      g      (itr    - itr   )
                      ,%3         %2 %1     j i      i j
(%t12)               ------------------------------------
                                      2
(%i13) decsym(itr,2,1,[anti(all)],[]);
(%o13)                               done
(%i14) defcon(g,g,kdelta);
(%o14)                               done
(%i15) subst(g,nounify(g),%th(3))$
(%i16) ishow(canform(contract(%)))$
                                           %1
(%t16)                           - f    itr
                                    ,%1    i j
```

<!-- category: Tensors -->
<!-- keywords: kdels -->
<!-- signatures: kdels(L1, L2) -->
### Function: kdels (L1, L2)

`kdels` gibt wie die Funktion `kdelta` ein Kronecker-Delta zuruck.
Im Unterschied zu `kdelta` ist das Kronecker-Delta der Funktion
`kdels` symmetrisch.


Beispiele:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) kdelta([1,2],[2,1]);
(%o2)                                 - 1
(%i3) kdels([1,2],[2,1]);
(%o3)                                  1
(%i4) ishow(kdelta([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  - kdelta  kdelta
                             a       b         a       b
(%i4) ishow(kdels([a,b],[c,d]))$
                             c       d         d       c
(%t4)                  kdelta  kdelta  + kdelta  kdelta
                             a       b         a       b
```

See also: `kdelta`.

<!-- category: Tensors -->
<!-- keywords: kdelta -->
<!-- signatures: kdelta(L1, L2) -->
### Function: kdelta (L1, L2)

Ist das verallgemeinerte Kronecker-Delta im `itensor`-Paket.  Das Argument
*L1* ist die Liste der kovarianten und *L2* der kontravarianten 
Indizes.  `kdelta([i],[j])` gibt das einfache Kronecker-Delta zuruck.














Das `itensor`-Paket erlaubt die Definition des Kronecker-Delta nur mit
kovarianten oder kontravarianten Indizes, wie zum Beispiel
`kdelta([i,j],[])`.  Mit diesen Großen kann gerechnet werden, sie
sind jedoch keine Tensoren.

<!-- category: Tensors -->
<!-- keywords: kinvariant -->
<!-- signatures: kinvariant -->
### Variable: kinvariant

The Kretchmann invariant. Computed by `rinvariant`.

<!-- category: Tensors -->
<!-- keywords: kt -->
<!-- signatures: kt -->
### Variable: kt

The contortion tensor, computed from `tr` by `contortion`.

<!-- category: Tensors -->
<!-- keywords: lc2kdt -->
<!-- signatures: lc2kdt(expr) -->
### Function: lc2kdt (expr)

Vereinfacht den Ausdruck *expr* mit Levi-Civita-Symbolen.  Wenn moglich
werden diese zu Kronecker-Delta-Symbolen vereinfacht.  Im Unterschied zu der
Auswertung eines Ausdrucks mit Levi-Civita-Symbolen, vermeidet die Funktion
`lc2kdt` das Einfuhren von numerischen Indizes, die fur eine weitere
symbolische Vereinfachung zum Beispiel mit den Funktionen `rename` oder
`contract` nicht geeignet sind.


Beispiel:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([k,l],[])*a([j],[k]))$
                                  i j  k
(%t2)                  levi_civita    a  levi_civita
                                       j            k l
(%i3) ishow(ev(expr,levi_civita))$
                                  i j  k       1 2
(%t3)                       kdelta    a  kdelta
                                  1 2  j       k l
(%i4) ishow(ev(%,kdelta))$
             i       j         j       i   k
(%t4) (kdelta  kdelta  - kdelta  kdelta ) a
             1       2         1       2   j

                               1       2         2       1
                        (kdelta  kdelta  - kdelta  kdelta )
                               k       l         k       l
(%i5) ishow(lc2kdt(expr))$
                     k       i       j    k       j       i
(%t5)               a  kdelta  kdelta  - a  kdelta  kdelta
                     j       k       l    j       k       l
(%i6) ishow(contract(expand(%)))$
                                 i           i
(%t6)                           a  - a kdelta
                                 l           l
```






Die Funktion `lc2kdt` benotigt in einigen Fallen den Metriktensor.
Ist der Metriktensor zuvor nicht mit der Funktion `imetric` definiert,
dann meldet Maxima einen Fehler.



```maxima
(%i7) expr:ishow('levi_civita([],[i,j])
                 *'levi_civita([],[k,l])*a([j,k],[]))$
                                 i j            k l
(%t7)                 levi_civita    levi_civita    a
                                                     j k
(%i8) ishow(lc2kdt(expr))$
Maxima encountered a Lisp error:

 Error in $IMETRIC [or a callee]:
 $IMETRIC [or a callee] requires less than two arguments.

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i9) imetric(g);
(%o9)                                done
(%i10) ishow(lc2kdt(expr))$

         %3 i       k   %4 j       l     %3 i       l   %4 j
(%t10) (g     kdelta   g     kdelta   - g     kdelta   g    
                    %3             %4               %3
              k
        kdelta  ) a
              %4   j k

(%i11) ishow(contract(expand(%)))$
                                  l i    l i  j
(%t11)                           a    - g    a
                                              j
```

See also: `rename`, `contract`, `imetric`.

<!-- category: Tensors -->
<!-- keywords: lc_l -->
<!-- signatures: lc_l -->
### Function: lc_l

`lc_l` ist eine Regel, um Ausdrucke zu vereinfachen, die
Levi-Civita-Symbole enthalten.  Zusammen mit der Regel `lc_u` kann die
Regel zum Beispiel mit der Funktion `applyb1` angewendet werden, um
Ausdrucke effizienter zu vereinfachen, als durch eine Auswertung des Symbols
`levi_civita`.


Beispiele:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) el1:ishow('levi_civita([i,j,k],[])*a([],[i])*a([],[j]))$
                             i  j
(%t2)                       a  a  levi_civita
                                             i j k
(%i3) el2:ishow('levi_civita([],[i,j,k])*a([i])*a([j]))$
                                       i j k
(%t3)                       levi_civita      a  a
                                              i  j
(%i4) canform(contract(expand(applyb1(el1,lc_l,lc_u))));
(%t4)                                  0
(%i5) canform(contract(expand(applyb1(el2,lc_l,lc_u))));
(%t5)                                  0
```

See also: `lc_u`, `applyb1`.

<!-- category: Tensors -->
<!-- keywords: lc_u -->
<!-- signatures: lc_u -->
### Function: lc_u

`lc_u` ist eine Regel, um Ausdrucke zu vereinfachen, die
Levi-Civita-Symbole enthalten.  Zusammen mit der Regel `lc_c` kann die
Regel zum Beispiel mit der Funktion `applyb1` angewendet werden, um
Ausdrucke effizienter zu vereinfachen, als durch eine Auswertung des Symbols
`levi_civita`.  Siehe `lc_l` fur Beispiele.

See also: `applyb1`, `lc_l`.

<!-- category: Tensors -->
<!-- keywords: leinstein -->
<!-- signatures: leinstein(dis) -->
### Function: leinstein (dis)

Covariant Einstein-tensor.  `leinstein` stores the values of the covariant 
Einstein tensor in the array `lein`.  The covariant Einstein-tensor is 
computed from the mixed Einstein tensor `ein` by multiplying it with the 
metric tensor.  If the argument *dis* is `true`, then the non-zero 
values of the covariant Einstein tensor are displayed.

<!-- category: Tensors -->
<!-- keywords: levi_civita -->
<!-- signatures: levi_civita(L) -->
### Function: levi_civita (L)

Ist der Levi-Civita-Tensor, der auch Permutationstensor genannt wird.  Der
Tensor hat den Wert `1`, wenn die Liste *L* eine gerade Permutation
ganzer Zahlen ist, den Wert `-1` fur eine ungerade Permutation und
ansonsten den Wert `0`.


Beispiel:


Fur eine Kreisbewegung ist die Bahngeschwindigkeit `v` das Kreuzprodukt
aus Winkelgeschwindigkeit `w` und Ortsvektor `r`.  Wir haben also
`v = w x r`.  Hier wird eine tensorielle Schreibweise des Kreuzproduktes
mit dem Levi-Civita-Tensor eingefuhrt.  Der Ausdruck wird sodann fur die
erste Komponente zu der bekannten Definition des Kreuzproduktes vereinfacht.



```maxima
(%i1) load("itensor")$

(%i2) ishow(v([],[a])=
           'levi_civita([],[a,b,c])*w([b],[])*r([c],[]))$

                    a              a b c
(%t2)              v  = levi_civita      w  r
                                          b  c

(%i3) ishow(subst([a=1],%))$
                    1              1 b c
(%t3)              v  = levi_civita      w  r
                                          b  c
(%i4) ishow(ev(%, levi_civita))$
                      1         1 b c
(%t4)                v  = kdelta      w  r
                                1 2 3  b  c
(%i5) ishow(expand(ev(%, kdelta)))$
        1         b       c               c       b
(%t5)  v  = kdelta  kdelta  w  r  - kdelta  kdelta  w  r
                  2       3  b  c         2       3  b  c
(%i6) ishow(contract(%))$
                        1
(%t6)                  v  = w  r  - r  w
                             2  3    2  3
```


In diesem Beispiel wird das Spatprodukt von drei Vektoren `a`, `b` und
`b` mit dem Levi-Civita-Tensor definiert und dann vereinfacht.



```maxima
(%i1) load("itensor")$

(%i2) ishow(levi_civita([],[i,j,k])*a([i],[])*b([j],[])*c([k],[]))$
                            i j k
(%t2)                 kdelta      a  b  c
                            1 2 3  i  j  k
(%i3) ishow(contract(expand(ev(%,kdelta))))$
(%t3) a  b  c  - b  a  c  - a  c  b  + c  a  b  + b  c  a
       1  2  3    1  2  3    1  2  3    1  2  3    1  2  3
                                                       - c  b  a
                                                          1  2  3
```

<!-- category: Tensors -->
<!-- keywords: lfg -->
<!-- signatures: lfg -->
### Variable: lfg

The covariant frame metric. By default, it is initialized to the 4-dimensional 
Lorentz frame with signature (+,+,+,-). Used when `cframe_flag` is 
`true`.

<!-- category: Tensors -->
<!-- keywords: lg -->
<!-- signatures: lg -->
### Variable: lg

The metric tensor. This tensor must be specified (as a `dim` by 
`dim` matrix) before other computations can be performed.

<!-- category: Tensors -->
<!-- keywords: liediff -->
<!-- signatures: liediff(v, ten) -->
### Function: liediff (v, ten)

Berechnet die Lie-Ableitung eines tensoriellen Ausdrucks *ten* fur das
Vektorfeld *v*.  Das Argument *ten* kann irgendeine tensorielle
Große sein.  Das Argument *v* ist der Name eines Vektorfeldes und
wird ohne Indizes angegeben.


Beispiel:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(liediff(v,a([i,j],[])*b([],[k],l)))$
       k    %2            %2          %2
(%t2) b   (v   a       + v   a     + v   a    )
       ,l       i j,%2    ,j  i %2    ,i  %2 j

                          %1  k        %1  k      %1  k
                      + (v   b      - b   v    + v   b   ) a
                              ,%1 l    ,l  ,%1    ,l  ,%1   i j
```

<!-- category: Tensors -->
<!-- keywords: listoftens -->
<!-- signatures: listoftens(expr) -->
### Function: listoftens (expr)

Gibt eine Liste mit allen Tensoren zuruck, die im Argument *expr*
enthalten sind.


Beispiel:



```maxima
(%i1) load("itensor")$

(%i2) ishow(a([i,j],[k])*b([u],[],v)+c([x,y],[])*d([],[])*e)$
                                  k
(%t2)                 d e c    + a    b
                           x y    i j  u,v
(%i3) ishow(listoftens(%))$
                        k
(%t3)                 [a   , b   , c   , d]
                        i j   u,v   x y
```

<!-- category: Tensors -->
<!-- keywords: lorentz_gauge -->
<!-- signatures: lorentz_gauge(expr) -->
### Function: lorentz_gauge (expr)

Wendet die Lorenz-Eichung an, indem alle indizierten Großen in *expr*
zu Null gesetzt werden, die einen zu einem kontravarianten Index identischen
Ableitungsindex haben.

<!-- category: Tensors -->
<!-- keywords: lriem -->
<!-- signatures: lriem -->
### Variable: lriem

The covariant Riemann tensor. Computed by `lriemann`.

<!-- category: Tensors -->
<!-- keywords: lriemann -->
<!-- signatures: lriemann(dis) -->
### Function: lriemann (dis)

Covariant Riemann-tensor (`lriem[]`).


Computes the covariant Riemann-tensor as the array `lriem`. If the
argument *dis* is `true`, unique nonzero values are displayed.


If the variable `cframe_flag` is `true`, the covariant Riemann
tensor is computed directly from the frame field coefficients. Otherwise,
the (3,1) Riemann tensor is computed first.


For information on index ordering, see `riemann`.

<!-- category: Tensors -->
<!-- keywords: makebox -->
<!-- signatures: makebox(expr, name) -->
### Function: makebox (expr, name)

Zeigt das Argument *expr* auf die gleiche Weise an wie die Funktion
`ishow` mit dem Unterschied, dass der d’Alembert-Operator *name* im
Ausdruck durch `[]` ersetzt wird.


Beispiel:



```maxima
(%i1) makebox(g([],[i,j])*p([m],[n],i,j),g);
(%o1)                     []p([m], [n])
```

See also: `ishow`.

<!-- category: Tensors -->
<!-- keywords: nm -->
<!-- signatures: nm -->
### Variable: nm

User-supplied nonmetricity vector. Used by `nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: nmc -->
<!-- signatures: nmc -->
### Variable: nmc

The nonmetricity coefficients, computed from `nm` by `nonmetricity`.

<!-- category: Tensors -->
<!-- keywords: nonmetricity -->
<!-- signatures: nonmetricity(nm) -->
### Function: nonmetricity (nm)

Computes the (2,1) nonmetricity coefficients from the nonmetricity
vector *nm*.

<!-- category: Tensors -->
<!-- keywords: np -->
<!-- signatures: np -->
### Variable: np

A Newman-Penrose null tetrad. Computed by `nptetrad`.

<!-- category: Tensors -->
<!-- keywords: npi -->
<!-- signatures: npi -->
### Variable: npi

The raised-index Newman-Penrose null tetrad. Computed by `nptetrad`.
Defined as `ug.np`. The product `np.transpose(npi)` is constant:



```maxima
(%i39) trigsimp(np.transpose(npi));
                              [  0   - 1  0  0 ]
                              [                ]
                              [ - 1   0   0  0 ]
(%o39)                        [                ]
                              [  0    0   0  1 ]
                              [                ]
                              [  0    0   1  0 ]
```

<!-- category: Tensors -->
<!-- keywords: nptetrad -->
<!-- signatures: nptetrad() -->
### Function: nptetrad ()

Computes a Newman-Penrose null tetrad (`np`) and its raised-index
counterpart (`npi`). See `petrov` for an example.


The null tetrad is constructed on the assumption that a four-diemensional
orthonormal frame metric with metric signature (-,+,+,+) is being used.
The components of the null tetrad are related to the inverse frame matrix
as follows:



```maxima
np  = (fri  + fri ) / sqrt(2)
  1       1      2

np  = (fri  - fri ) / sqrt(2)
  2       1      2

np  = (fri  + %i fri ) / sqrt(2)
  3       3         4

np  = (fri  - %i fri ) / sqrt(2)
  4       3         4
```

<!-- category: Tensors -->
<!-- keywords: ntermst -->
<!-- signatures: ntermst(f) -->
### Function: ntermst (f)

gives the user a quick picture of the "size" of the doubly subscripted
tensor (array) *f*.  It prints two element lists where the second
element corresponds to NTERMS of the components specified by the first
elements.  In this way, it is possible to quickly find the non-zero
expressions and attempt simplification.

<!-- category: Tensors -->
<!-- keywords: petrov -->
<!-- signatures: petrov() -->
### Function: petrov ()

Computes the Petrov classification of the metric characterized by 
`psi[0]` ... `psi[4]`.


For example, the following demonstrates how to obtain the Petrov-classification
of the Kerr metric:



```maxima
(%i1) load("ctensor");
(%o1)       /share/tensor/ctensor.mac
(%i2) (cframe_flag:true,gcd:spmod,ctrgsimp:true,ratfac:true);
(%o2)                                true
(%i3) ct_coordsys(exteriorschwarzschild,all);
(%o3)                                done
(%i4) ug:invert(lg)$
(%i5) weyl(false);
(%o5)                                done
(%i6) nptetrad(true);
(%t6) np =

[ sqrt(r - 2 m)           sqrt(r)                                 ]
[---------------   ---------------------    0            0        ]
[sqrt(2) sqrt(r)   sqrt(2) sqrt(r - 2 m)                          ]
[                                                                 ]
[ sqrt(r - 2 m)            sqrt(r)                                ]
[---------------  - ---------------------   0            0        ]
[sqrt(2) sqrt(r)    sqrt(2) sqrt(r - 2 m)                         ]
[                                                                 ]
[                                          r      %i r sin(theta) ]
[       0                    0          -------   --------------- ]
[                                       sqrt(2)       sqrt(2)     ]
[                                                                 ]
[                                          r       %i r sin(theta)]
[       0                    0          -------  - ---------------]
[                                       sqrt(2)        sqrt(2)    ]

                             sqrt(r)         sqrt(r - 2 m)
(%t7) npi = matrix([- ---------------------,---------------, 0, 0],
                      sqrt(2) sqrt(r - 2 m) sqrt(2) sqrt(r)

          sqrt(r)            sqrt(r - 2 m)
[- ---------------------, - ---------------, 0, 0],
   sqrt(2) sqrt(r - 2 m)    sqrt(2) sqrt(r)

           1               %i
[0, 0, ---------, --------------------],
       sqrt(2) r  sqrt(2) r sin(theta)

           1                 %i
[0, 0, ---------, - --------------------])
       sqrt(2) r    sqrt(2) r sin(theta)

(%o7)                                done
(%i7) psi(true);
(%t8)                              psi  = 0
                                      0

(%t9)                              psi  = 0
                                      1

                                          m
(%t10)                             psi  = --
                                      2    3
                                          r

(%t11)                             psi  = 0
                                      3

(%t12)                             psi  = 0
                                      4
(%o12)                               done
(%i12) petrov();
(%o12)                                 D
```


The Petrov classification function is based on the algorithm published in
"Classifying geometries in general relativity: III Classification in practice"
by Pollney, Skea, and d’Inverno, Class. Quant. Grav. 17 2885-2902 (2000).
Except for some simple test cases, the implementation is untested as of
December 19, 2004, and is likely to contain errors.

<!-- category: Tensors -->
<!-- keywords: psi -->
<!-- signatures: psi(dis) -->
### Function: psi (dis)

Computes the five Newman-Penrose coefficients `psi[0]`...`psi[4]`.
If `psi` is set to `true`, the coefficients are displayed.
See `petrov` for an example.


These coefficients are computed from the Weyl-tensor in a coordinate base.
If a frame base is used, the Weyl-tensor is first converted to a coordinate
base, which can be a computationally expensive procedure. For this reason,
in some cases it may be more advantageous to use a coordinate base in the
first place before the Weyl tensor is computed. Note however, that
constructing a Newman-Penrose null tetrad requires a frame base. Therefore,
a meaningful computation sequence may begin with a frame base, which
is then used to compute `lg` (computed automatically by `cmetric`
and then `ug`. At this point, you can switch back to a coordinate base
by setting `cframe_flag` to false before beginning to compute the
Christoffel symbols. Changing to a frame base at a later stage could yield
inconsistent results, as you may end up with a mixed bag of tensors, some
computed in a frame base, some in a coordinate base, with no means to
distinguish between the two.

<!-- category: Tensors -->
<!-- keywords: ratchristof -->
<!-- signatures: ratchristof -->
### Variable: ratchristof

Causes rational simplification to be applied by `christof`.

<!-- category: Tensors -->
<!-- keywords: rateinstein -->
<!-- signatures: rateinstein -->
### Variable: rateinstein

Default value: `true`


If `true` rational simplification will be
performed on the non-zero components of Einstein tensors; if
`ratfac` is `true` then the components will also be factored.

<!-- category: Tensors -->
<!-- keywords: ratriemann -->
<!-- signatures: ratriemann -->
### Variable: ratriemann

Default value: `true`


One of the switches which controls
simplification of Riemann tensors; if `true`, then rational
simplification will be done; if `ratfac` is `true` then each of the
components will also be factored.

<!-- category: Tensors -->
<!-- keywords: ratweyl -->
<!-- signatures: ratweyl -->
### Variable: ratweyl

Default value: `true`


If `true`, this switch causes the `weyl` function
to apply rational simplification to the values of the Weyl tensor. If
`ratfac` is `true`, then the components will also be factored.

<!-- category: Tensors -->
<!-- keywords: rediff -->
<!-- signatures: rediff(ten) -->
### Function: rediff (ten)

Wertet jedes Auftreten von Substantivformen der Funktion `idiff` in
dem tensoriellem Ausdruck *ten* aus.

See also: `idiff`.

<!-- category: Tensors -->
<!-- keywords: remcomps -->
<!-- signatures: remcomps(tensor) -->
### Function: remcomps (tensor)

Entfernt alle Werte von den Komponenten des Tensors *tensor*, die einen
Wert mit der Funktion `components` erhalten haben.

See also: `components`.

<!-- category: Tensors -->
<!-- keywords: remcon -->
<!-- signatures: remcon(tensor_1, ..., tensor_n), remcon(all) -->
### Function: remcon (tensor_1, ..., tensor_n)

Entfernt die Eigenschaften der Tensorverjungung von den Tensoren
*tensor_1*, ..., *tensor_n*.  `remcon(all)` entfernt die
Eigenschaften von der Tensorverjungung fur alle Tensoren.  Das sind die
Tensoren, die in der Liste `contractions` enthalten sind.

See also: `contractions`.

<!-- category: Tensors -->
<!-- keywords: remcoord -->
<!-- signatures: remcoord(tensor_1, tensor_2, ...), remcoord(all) -->
### Function: remcoord (tensor_1, tensor_2, ...)

Entfernt die mit der Funktion `coord` definierte Eigenschaft fur die
tensoriellen Großen *tensor_i*.  Das Kommando `remcoord(all)`
entfernt diese Eigenschaft fur alle tensoriellen Großen.

See also: `coord`.

<!-- category: Tensors -->
<!-- keywords: remsym -->
<!-- signatures: remsym(tensor, m, n) -->
### Function: remsym (tensor, m, n)

Entfernt die Symmetrieeigenschaften des Tensors *tensor*, der *m*
kovariante und *n* kontravariante Indizes hat.

<!-- category: Tensors -->
<!-- keywords: rename -->
<!-- signatures: rename(expr), rename(expr, count) -->
### Function: rename (expr)

Gibt einen zum Argument *expr* aquivalenten Ausdruck zuruck, wobei die
Summationsindizes mit den Werten aus der liste `[%1, %2, ...]` umbenannt
sind.  Wird das zusatzlich das Argument *count* angegeben, wird die
Nummerierung mit dem Wert *count* begonnen.  Jeder Summationsindex in einem
Produkt erhalt einen verschiedenen Namen.  Fur eine Summe wird der Zahler
fur jeden Term zuruckgesetzt.  Auf diese Weise wirkt die Funktion
`rename` wie eine Vereinfachung eines tensoriellen Ausdrucks.  Hat die
Optionsvariable `allsym` den Wert `true`, werden die Indizes
alphabetisch nach den kovarianten oder kontravarianten Indizes geordnet,
entsprechend dem Wert der Optionsvariablen `flipflag`.  Hat die
Optionsvariable `flipflag` den Wert `true`, werden die Indizes
entsprechend der Ordnung der kovarianten Indizes geordnet.  Es ist haufig der
Fall, dass das Ordnen sowohl nach den kovarianten als auch den kontravarianten
Indizes einen Ausdruck besser vereinfacht, als allein die Ordnung nach einer
der Indizes.


Beispiele:



```maxima
(%i1) load("itensor")$

(%i2) allsym: true;
(%o2)                         true
(%i3) g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%4],[%3])
             *ichr2([%2,%3],[u])*ichr2([%5,%6],[%1])
             *ichr2([%7,r],[%2])
 -g([],[%4,%5])*g([],[%6,%7])*ichr2([%1,%2],[u])
               *ichr2([%3,%5],[%1])*ichr2([%4,%6],[%3])
               *ichr2([%7,r],[%2])$

(%i4) expr: ishow(%)$

       %4 %5  %6 %7      %3         u          %1         %2
(%t4) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %4      %2 %3      %5 %6      %7 r
          %4 %5  %6 %7      u          %1         %3         %2
       - g      g      ichr2      ichr2      ichr2      ichr2
                            %1 %2      %3 %5      %4 %6      %7 r

(%i5) flipflag: true;
(%o5)                         true
(%i6) ishow(rename(expr))$
       %2 %5  %6 %7      %4         u          %1         %3
(%t6) g      g      ichr2      ichr2      ichr2      ichr2
                         %1 %2      %3 %4      %5 %6      %7 r
          %4 %5  %6 %7      u          %1         %3         %2
       - g      g      ichr2      ichr2      ichr2      ichr2
                            %1 %2      %3 %4      %5 %6      %7 r
(%i7) flipflag: false;
(%o7)                         false
(%i8) rename(%th(2));
(%o8)                           0
(%i9) ishow(rename(expr))$
       %1 %2  %3 %4      %5         %6         %7        u
(%t9) g      g      ichr2      ichr2      ichr2     ichr2
                         %1 %6      %2 %3      %4 r      %5 %7
          %1 %2  %3 %4      %6         %5         %7        u
       - g      g      ichr2      ichr2      ichr2     ichr2
                            %1 %3      %2 %6      %4 r      %5 %7
```

See also: `allsym`, `flipflag`.

<!-- category: Tensors -->
<!-- keywords: ric -->
<!-- signatures: ric -->
### Variable: ric

The mixed Ricci-tensor. Computed by `ricci`.

<!-- category: Tensors -->
<!-- keywords: ricci -->
<!-- signatures: ricci(dis) -->
### Function: ricci (dis)

A function in the `ctensor` (component tensor) package. `ricci` 
computes the covariant (symmetric) components `ric[i,j]` of the Ricci 
tensor.  If the argument *dis* is `true`, then the non-zero components 
are displayed.

<!-- category: Tensors -->
<!-- keywords: riem -->
<!-- signatures: riem -->
### Variable: riem

The (3,1) Riemann tensor. Computed when the function `riemann` is invoked. 
For information about index ordering, see the description of `riemann`.


If `cframe_flag` is `true`, `riem` is computed from the 
covariant Riemann-tensor `lriem`.

<!-- category: Tensors -->
<!-- keywords: riemann -->
<!-- signatures: riemann(dis) -->
### Function: riemann (dis)

A function in the `ctensor` (component tensor)
package.  `riemann` computes the Riemann curvature tensor
from the given metric and the corresponding Christoffel symbols. The following
index conventions are used:



```maxima
l      _l       _l       _l   _m    _l   _m
 R[i,j,k,l] =  R    = |      - |      + |    |   - |    |
                ijk     ij,k     ik,j     mk   ij    mj   ik
```


This notation is consistent with the notation used by the `itensor`
package and its `icurvature` function.
If the optional argument *dis* is `true`,
the non-zero components `riem[i,j,k,l]` will be displayed.
As with the Einstein tensor, various switches set by the user
control the simplification of the components of the Riemann tensor.
If `ratriemann` is `true`, then
rational simplification will be done. If `ratfac`
is `true` then
each of the components will also be factored.


If the variable `cframe_flag` is `false`, the Riemann tensor is
computed directly from the Christoffel-symbols. If `cframe_flag` is
`true`, the covariant Riemann-tensor is computed first from the
frame field coefficients.

<!-- category: Tensors -->
<!-- keywords: rinvariant -->
<!-- signatures: rinvariant() -->
### Function: rinvariant ()

Forms the Kretchmann-invariant (`kinvariant`) obtained by
contracting the tensors



```maxima
lriem[i,j,k,l]*uriem[i,j,k,l].
```


This object is not automatically simplified since it can be very large.

<!-- category: Tensors -->
<!-- keywords: scurvature -->
<!-- signatures: scurvature() -->
### Function: scurvature ()

Returns the scalar curvature (obtained by contracting
the Ricci tensor) of the Riemannian manifold with the given metric.

<!-- category: Tensors -->
<!-- keywords: sf -->
<!-- signatures: sf(u, v) -->
### Function: sf (u, v)

Eine symmetrische Bilinearform, die bei der Vereinfachung von Ausdrucken
mit der Funktion `atensimp` angewendet wird.  Die Funktion kann vom Nutzer
durch eine neue Funktion ersetzt werden.  Die Standardimplementation pruft
mit der Funktion `abasep`, ob die Argumente *u* und *v*
Basisvektoren sind und setzt fur diesen Fall den entsprechen Wert der Matrix
`aform` ein.

See also: `atensimp`, `abasep`, `aform`.

<!-- category: Tensors -->
<!-- keywords: showcomps -->
<!-- signatures: showcomps(tensor) -->
### Function: showcomps (tensor)

Zeigt die Zuweisungen mit der Funktion `components` an die Komponenten des
Tensors *tensor*.  Die Funktion `showcomps` kann auch die Komponenten
eines Tensors mit einer hoheren Stufe als 2 zeigen.


Beispiel:



```maxima
(%i1) load("ctensor")$
(%i2) load("itensor")$
(%i3) lg:matrix([sqrt(r/(r-2*m)),0,0,0],[0,r,0,0],
                [0,0,sin(theta)*r,0],[0,0,0,sqrt((r-2*m)/r)]);

               [         r                                     ]
               [ sqrt(-------)  0       0              0       ]
               [      r - 2 m                                  ]
               [                                               ]
               [       0        r       0              0       ]
(%o3)          [                                               ]
               [       0        0  r sin(theta)        0       ]
               [                                               ]
               [                                      r - 2 m  ]
               [       0        0       0        sqrt(-------) ]
               [                                         r     ]

(%i4) components(g([i,j],[]),lg);
(%o4)                                done
(%i5) showcomps(g([i,j],[]));

                  [         r                                     ]
                  [ sqrt(-------)  0       0              0       ]
                  [      r - 2 m                                  ]
                  [                                               ]
                  [       0        r       0              0       ]
(%t5)      g    = [                                               ]
            i j   [       0        0  r sin(theta)        0       ]
                  [                                               ]
                  [                                      r - 2 m  ]
                  [       0        0       0        sqrt(-------) ]
                  [                                         r     ]

(%o5)                                false
```

See also: `components`.

<!-- category: Tensors -->
<!-- keywords: simpmetderiv -->
<!-- signatures: simpmetderiv(expr), simpmetderiv(expr[, stop]) -->
### Function: simpmetderiv (expr)

Vereinfacht Ausdrucke die Produkte von Ableitungen des Metriktensors
enthalten.  Im besonderen erkennt `simpmetderiv` die folgenden
Identitaten:



```maxima
ab        ab           ab                 a
  g   g   + g   g     = (g   g  )   = (kdelta )   = 0
   ,d  bc        bc,d         bc ,d          c ,d
```


daher ist



```maxima
ab          ab
  g   g   = - g   g
   ,d  bc          bc,d
```


und



```maxima
ab          ab
 g   g     = g   g
  ,j  ab,i    ,i  ab,j
```




was aus den Symmetrien der Christoffel-Symbole folgt.








Die Funktion `simpmetderiv` akzeptiert einen optionalen Parameter
*stop*.  Ist dieser vorhanden, stoppt die Funktion nach der ersten
erfolgreichen Substitution in einem Produkt.  `simpmetderiv` beachtet
ferner die Optionsvariable `flipflag`, welche die Ordnung der Indizes
kontrolliert.





Siehe auch `weyl.dem` fur Beispiele der Funktionen `simpmetderiv`
und `conmetderiv`, die die Vereinfachung des Weyl-Tensors zeigen.










Beispiel:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) imetric(g);
(%o2)                                done
(%i3) ishow(g([],[a,b])*g([],[b,c])*g([a,b],[],d)*g([b,c],[],e))$
                             a b  b c
(%t3)                       g    g    g      g
                                       a b,d  b c,e
(%i4) ishow(canform(%))$

errexp1 has improper indices
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) ishow(simpmetderiv(%))$
                             a b  b c
(%t5)                       g    g    g      g
                                       a b,d  b c,e
(%i6) flipflag:not flipflag;
(%o6)                                true
(%i7) ishow(simpmetderiv(%th(2)))$
                               a b  b c
(%t7)                         g    g    g    g
                               ,d   ,e   a b  b c
(%i8) flipflag:not flipflag;
(%o8)                                false
(%i9) ishow(simpmetderiv(%th(2),stop))$
                               a b  b c
(%t9)                       - g    g    g      g
                                    ,e   a b,d  b c
(%i10) ishow(contract(%))$
                                    b c
(%t10)                           - g    g
                                    ,e   c b,d
```

See also: `flipflag`, `conmetderiv`.

<!-- category: Tensors -->
<!-- keywords: symmetricp -->
<!-- signatures: symmetricp(M) -->
### Function: symmetricp (M)

Returns `true` if *M* is a symmetric matrix or (2D) array.

<!-- category: Tensors -->
<!-- keywords: tensorkill -->
<!-- signatures: tensorkill -->
### Variable: tensorkill

Variable indicating if the tensor package has been initialized. Set and used by
`csetup`, reset by `init_ctensor`.

<!-- category: Tensors -->
<!-- keywords: tentex -->
<!-- signatures: tentex(expr) -->
### Function: tentex (expr)

To use the `tentex` function, you must first load `tentex`,
as in the following example:



```maxima
(%i1) load("itensor")$
(%i2) load("tentex")$
(%i3) idummyx:m;
(%o3)                                  m
(%i4) ishow(icurvature([j,k,l],[i]))$

            m1       i           m1       i           i
(%t4)  ichr2    ichr2     - ichr2    ichr2     - ichr2
            j k      m1 l        j l      m1 k        j l,k

                                                      i
                                               + ichr2
                                                      j k,l

(%i5) tentex(%)$
$$\Gamma_{j\,k}^{m_1}\,\Gamma_{l\,m_1}^{i}-\Gamma_{j\,l}^{m_1}\,
 \Gamma_{k\,m_1}^{i}-\Gamma_{j\,l,k}^{i}+\Gamma_{j\,k,l}^{i}$$
```


Note the use of the `idummyx` assignment, to avoid the appearance
of the percent sign in the TeX expression, which may lead to compile errors.


NB: This version of the `tentex` function is somewhat experimental.

<!-- category: Tensors -->
<!-- keywords: tr -->
<!-- signatures: tr -->
### Variable: tr

User-supplied rank-3 tensor representing torsion. Used by `contortion`.

<!-- category: Tensors -->
<!-- keywords: ufg -->
<!-- signatures: ufg -->
### Variable: ufg

The inverse frame metric. Computed from `lfg` when `cmetric` is 
called while `cframe_flag` is set to `true`.

<!-- category: Tensors -->
<!-- keywords: ug -->
<!-- signatures: ug -->
### Variable: ug

The inverse of the metric tensor. Computed by `cmetric`.

<!-- category: Tensors -->
<!-- keywords: undiff -->
<!-- signatures: undiff(expr) -->
### Function: undiff (expr)

Gibt einen zum Argument *expr* aquivalenten Ausdruck zuruck, in dem
alle Ableitungen von indizierten Großen durch Substantivformen der
Funktion `idiff` ersetzt sind.

See also: `idiff`.

<!-- category: Tensors -->
<!-- keywords: uric -->
<!-- signatures: uric -->
### Variable: uric

The contravariant Ricci-tensor. Computed by `uricci`.

<!-- category: Tensors -->
<!-- keywords: uricci -->
<!-- signatures: uricci(dis) -->
### Function: uricci (dis)

This function first computes the covariant components `ric[i,j]` of the 
Ricci tensor.  Then the mixed Ricci tensor is computed using the contravariant 
metric tensor.  If the value of the argument *dis* is `true`, then 
these mixed components, `uric[i,j]` (the index `i` is covariant and 
the index `j` is contravariant), will be displayed directly.  Otherwise, 
`ricci(false)` will simply compute the entries of the array 
`uric[i,j]` without displaying the results.

<!-- category: Tensors -->
<!-- keywords: uriem -->
<!-- signatures: uriem -->
### Variable: uriem

The contravariant Riemann tensor. Computed by `uriemann`.

<!-- category: Tensors -->
<!-- keywords: uriemann -->
<!-- signatures: uriemann(dis) -->
### Function: uriemann (dis)

Computes the contravariant components of the Riemann
curvature tensor as array elements `uriem[i,j,k,l]`.  These are displayed
if *dis* is `true`.

<!-- category: Tensors -->
<!-- keywords: vect_coords -->
<!-- signatures: vect_coords -->
### Variable: vect_coords

Standardwert: `false`


Tensoren konnen durch Angabe von ganzen Zahlen nach den einzelnen Komponenten
abgeleitet werden.  In diesem Fall bezeichnen die ganzen Zahlen der Reihe nach
die Indizes, die in der Optionsvariablen `vect_coords` abgelegt sind.

<!-- category: Tensors -->
<!-- keywords: weyl -->
<!-- signatures: weyl(dis) -->
### Function: weyl (dis)

Computes the Weyl conformal tensor.  If the argument *dis* is
`true`, the non-zero components `weyl[i,j,k,l]` will be displayed to 
the user.  Otherwise, these components will simply be computed and stored.
If the switch `ratweyl` is set to `true`, then the components will be
rationally simplified; if `ratfac` is `true` then the results will be
factored as well.

<!-- category: Tensors -->
<!-- keywords: | -->
<!-- signatures: | -->
### Variable: |

The vertical bar `|` denotes the "contraction with a vector" binary
operation. When a totally antisymmetric covariant tensor is contracted
with a contravariant vector, the result is the same regardless which index
was used for the contraction. Thus, it is possible to define the
contraction operation in an index-free manner.


In the `itensor` package, contraction with a vector is always carried out
with respect to the first index in the literal sorting order. This ensures
better simplification of expressions involving the `|` operator. For instance:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) decsym(a,2,0,[anti(all)],[]);
(%o2)                                done
(%i3) ishow(a([i,j],[])|v)$
                                    %1
(%t3)                              v   a
                                        %1 j
(%i4) ishow(a([j,i],[])|v)$
                                     %1
(%t4)                             - v   a
                                         %1 j
```


Note that it is essential that the tensors used with the `|` operator be
declared totally antisymmetric in their covariant indices. Otherwise,
the results will be incorrect.

<!-- category: Tensors -->
<!-- keywords: ~ -->
<!-- signatures: ~ -->
### Variable: ~

The wedge product operator is denoted by the tilde `~`. This is
a binary operator. Its arguments should be expressions involving scalars,
covariant tensors of rank one, or covariant tensors of rank `l` that
have been declared antisymmetric in all covariant indices.


The behavior of the wedge product operator is controlled by the
`igeowedge_flag` flag, as in the following example:



```maxima
(%i1) load("itensor");
(%o1)      /share/tensor/itensor.lisp
(%i2) ishow(a([i])~b([j]))$
                                 a  b  - b  a
                                  i  j    i  j
(%t2)                            -------------
                                       2
(%i3) decsym(a,2,0,[anti(all)],[]);
(%o3)                                done
(%i4) ishow(a([i,j])~b([k]))$
                          a    b  + b  a    - a    b
                           i j  k    i  j k    i k  j
(%t4)                     ---------------------------
                                       3
(%i5) igeowedge_flag:true;
(%o5)                                true
(%i6) ishow(a([i])~b([j]))$
(%t6)                            a  b  - b  a
                                  i  j    i  j
(%i7) ishow(a([i,j])~b([k]))$
(%t7)                     a    b  + b  a    - a    b
                           i j  k    i  j k    i k  j
```

