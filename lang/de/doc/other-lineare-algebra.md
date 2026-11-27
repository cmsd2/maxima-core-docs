## Lineare Algebra

<!-- category: Other -->
<!-- keywords: addcol -->
<!-- signatures: addcol(M, list_1, ..., list_n) -->
### Function: addcol (M, list_1, ..., list_n)

Hangt eine oder mehrere Spalten, die als Listen *list_1*, ..., 
*list_n* ubergeben werden, an die Matrix *M* an.


Beispiel:



```maxima
(%i1) M:matrix([a,b],[c,d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) addcol(M,[1,2],[x,y]);
                         [ a  b  1  x ]
(%o2)                    [            ]
                         [ c  d  2  y ]
```

<!-- category: Other -->
<!-- keywords: addrow -->
<!-- signatures: addrow(M, list_1, ..., list_n) -->
### Function: addrow (M, list_1, ..., list_n)

Hangt eine oder mehrere Zeilen, die als Listen *list_1*, ...,
*list_n* ubergeben werden, an die Matrix *M* an.


Beispiel:



```maxima
(%i1) M:matrix([a,b],[c,d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) addrow(M,[1,2],[x,y]);
                            [ a  b ]
                            [      ]
                            [ c  d ]
(%o2)                       [      ]
                            [ 1  2 ]
                            [      ]
                            [ x  y ]
```

<!-- category: Other -->
<!-- keywords: adjoint -->
<!-- signatures: adjoint(M) -->
### Function: adjoint (M)

Gibt die adjungierte der Matrix *M* zuruck.

<!-- category: Other -->
<!-- keywords: augcoefmatrix -->
<!-- signatures: augcoefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: augcoefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

Gibt die erweiterte Koeffizientenmatrix fur die Variablen *x_1*, ..., 
*x_n* und dem linearen Gleichungssystem *eqn_1*, ..., *eqn_m*.
Die erweiterte Koeffizientenmatrix entsteht, wenn an die Koeffizientenmatrix 
des Gleichungssystems die Spalte mit der rechten Seite des Gleichungssystems
angefugt wird.


Beispiel:



```maxima
(%i1) m: [2*x - (a - 1)*y = 5*b, c + b*y + a*x = 0]$
(%i2) augcoefmatrix (m, [x, y]);
                       [ 2  1 - a  - 5 b ]
(%o2)                  [                 ]
                       [ a    b      c   ]
```

<!-- category: Other -->
<!-- keywords: charpoly -->
<!-- signatures: charpoly(M, x) -->
### Function: charpoly (M, x)

Gibt das charakteristische Polynom der Matrix *M* fur die Variable *x*
zuruck.  Das charakterische Polynom wird als
`determinant(M - diagmatrix(length (M), x))` berechnet.


Beispiel:



```maxima
(%i1) a: matrix ([3, 1], [2, 4]);
                            [ 3  1 ]
(%o1)                       [      ]
                            [ 2  4 ]
(%i2) expand (charpoly (a, lambda));
                           2
(%o2)                lambda  - 7 lambda + 10
(%i3) (programmode: true, solve (%));
(%o3)               [lambda = 5, lambda = 2]
(%i4) matrix ([x1], [x2]);
                             [ x1 ]
(%o4)                        [    ]
                             [ x2 ]
(%i5) ev (a . % - lambda*%, %th(2)[1]);
                          [ x2 - 2 x1 ]
(%o5)                     [           ]
                          [ 2 x1 - x2 ]
(%i6) %[1, 1] = 0;
(%o6)                     x2 - 2 x1 = 0
(%i7) x2^2 + x1^2 = 1;
                            2     2
(%o7)                     x2  + x1  = 1
(%i8) solve ([%th(2), %], [x1, x2]);
                  1               2
(%o8) [[x1 = - -------, x2 = - -------], 
               sqrt(5)         sqrt(5)

                                             1             2
                                    [x1 = -------, x2 = -------]]
                                          sqrt(5)       sqrt(5)
```

<!-- category: Other -->
<!-- keywords: coefmatrix -->
<!-- signatures: coefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: coefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

Gibt die Koeffizientenmatrix fur die Variablen *x_1*, ..., *x_n*
des linearen Gleichungssystem *eqn_1*, ..., *eqn_m* zuruck.


Beispiel:



```maxima
(%i1) coefmatrix([2*x-(a-1)*y+5*b = 0, b*y+a*x = 3], [x,y]);

                                 [ 2  1 - a ]
(%o1)                            [          ]
                                 [ a    b   ]
```

<!-- category: Other -->
<!-- keywords: col -->
<!-- signatures: col(M, i) -->
### Function: col (M, i)

Gibt die *i*-te Spalte der Matrix *M* zuruck.  Das Ergebnis ist eine
Matrix.


Beispiel:



```maxima
(%i1) M:matrix([1,2,3],[a,b,c]);
                           [ 1  2  3 ]
(%o1)                      [         ]
                           [ a  b  c ]
(%i2) col(M,2);
                              [ 2 ]
(%o2)                         [   ]
                              [ b ]
```

<!-- category: Other -->
<!-- keywords: columnvector, covect -->
<!-- signatures: columnvector(L), covect(L) -->
### Function: columnvector (L)

Gibt eine Matrix mit einer Spalte zuruck, die die Elemente der Liste *L*
enthalt.





`covect` ist ein Alias-Name fur die Funktion `columnvector`.  Das 
Kommando `load("eigen")` ladt die Funktion.






Beispiel:






```maxima
(%i1) load("eigen")$

(%i2) columnvector ([aa, bb, cc]);
                             [ aa ]
                             [    ]
(%o2)                        [ bb ]
                             [    ]
                             [ cc ]
```

<!-- category: Other -->
<!-- keywords: copymatrix -->
<!-- signatures: copymatrix(M) -->
### Function: copymatrix (M)

Gibt eine Kopie der Matrix *M* zuruck.








Die Zuweisung wie zum Beispiel `m2: m1` kopiert die Matrix `m1` nicht.
Wird nach dieser Zuweisung die Matrix `m2` geandert, wird auch die Matrix
`m1` geandert.  Um eine Kopie zu erhalten, muss `m2: copymatrix(m1)`
ausgefuhrt werden.

<!-- category: Other -->
<!-- keywords: determinant -->
<!-- signatures: determinant(M) -->
### Function: determinant (M)

Berechnet die Determinate der Matrix *M*.  Die angewendete Methode ist
vergleichbar mit dem Gauß-Verfahren.









`determinat` wird von den Schaltern `ratmx` und `sparse`
kontrolliert.  Haben beide Schalter den Wert `true`, wird ein spezieller
Algorithmus fur schwachbesetzte Matrizen aufgerufen.

<!-- category: Other -->
<!-- keywords: detout -->
<!-- signatures: detout -->
### Variable: detout

Standardwert: `false`





Hat `detout` den Wert `true`, wird die Determinate einer Matrix, fur
die die inverse Matrix berechnet wird, aus der Matrix herausmultipliziert.






Damit dieser Schalter einen Effekt hat, mussen die Optionsvariablen 
`doallmxops` und `doscmxops` den Wert `false` haben.


Beispiele:



```maxima
(%i1) m: matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) detout: true$
(%i3) doallmxops: false$
(%i4) doscmxops: false$
(%i5) invert (m);
                          [  d   - b ]
                          [          ]
                          [ - c   a  ]
(%o5)                     ------------
                           a d - b c
```

<!-- category: Other -->
<!-- keywords: diagmatrix -->
<!-- signatures: diagmatrix(n, x) -->
### Function: diagmatrix (n, x)

Gibt eine *n*-dimensionale Diagonalmatrix zuruck, deren Diagonalelemente
alle den Wert *x* haben.





*n* muss zu einer ganzen Zahl auswerten.  Ansonsten meldet Maxima einen
Fehler.






*x* kann ein beliebiger Ausdruck einschließlich einer Matrix sein.  Ist
*x* eine Matrix, dann wird diese nicht kopiert.

<!-- category: Other -->
<!-- keywords: doallmxops -->
<!-- signatures: doallmxops -->
### Variable: doallmxops

Standardwert: `true`








Hat `doallmxops` den Wert `true`, werden Matrixoperationen 
ausgefuhrt.  Ist der Wert `false`, werden nur die Matrixoperationen 
ausgefuhrt, die mit den einzelnen `dot`-Schaltern eingeschaltet sind.

<!-- category: Other -->
<!-- keywords: domxexpt -->
<!-- signatures: domxexpt -->
### Variable: domxexpt

Standardwert: `true`







Hat `domxexpt` den Wert `true`, wird die Exponentiation
`exp(M)`, wobei *M* eine Matrix ist, elementweise fur jedes
einzelne Matrixelement ausgefuhrt, so dass fur jedes Element der Matrix 
gilt `exp (m[i,j])`.  Ansonsten wird die Exponentiation als
`exp (ev(M)` ausgewertet.






`domxexpt` beeinflußt alle Ausdrucke der Form `a^b`,
wobei *a* eine Konstante oder ein skalarer Ausdruck und *b* eine
Liste oder Matrix ist.


Beispiele:



```maxima
(%i1) m: matrix ([1, %i], [a+b, %pi]);
                         [   1    %i  ]
(%o1)                    [            ]
                         [ b + a  %pi ]
(%i2) domxexpt: false$
(%i3) (1 - c)^m;
                             [   1    %i  ]
                             [            ]
                             [ b + a  %pi ]
(%o3)                 (1 - c)
(%i4) domxexpt: true$
(%i5) (1 - c)^m;
                  [                      %i  ]
                  [    1 - c      (1 - c)    ]
(%o5)             [                          ]
                  [        b + a         %pi ]
                  [ (1 - c)       (1 - c)    ]
```

<!-- category: Other -->
<!-- keywords: domxmxops -->
<!-- signatures: domxmxops -->
### Variable: domxmxops

Standardwert: `true`







Hat `domxmxops` den Wert `true`, werden allen Matrix-Matrix und 
Matrix-Listen-Operationen ausgefuhrt.

<!-- category: Other -->
<!-- keywords: domxnctimes -->
<!-- signatures: domxnctimes -->
### Variable: domxnctimes

Standardwert: `false`






Hat `domxnctimes` den Wert `true`, werden nichtkommutative Produkte
von Matrizen ausgefuhrt.

<!-- category: Other -->
<!-- keywords: doscmxops -->
<!-- signatures: doscmxops -->
### Variable: doscmxops

Standardwert: `false`






Hat `doscmxops` den Wert `true`, werden Skalar-Matrix-Operationen
ausgefuhrt.

<!-- category: Other -->
<!-- keywords: doscmxplus -->
<!-- signatures: doscmxplus -->
### Variable: doscmxplus

Standardwert: `false`






Hat `doscmxplus` den Wert `true`, haben Skalar-Matrix-Operationen
eine Matrix als Ergebnis.  Dieser Schalter ist nicht unter `doallmxops`
subsumiert.

<!-- category: Other -->
<!-- keywords: dot0nscsimp -->
<!-- signatures: dot0nscsimp -->
### Variable: dot0nscsimp

Standardwert: `true`






Hat `dot0nscsimp` den Wert `true`, werden nichtkommutative Produkte
mit einer Null und einem nichtskalaren Term zu einem kommutativen Produkt
vereinfacht.

<!-- category: Other -->
<!-- keywords: dot0simp -->
<!-- signatures: dot0simp -->
### Variable: dot0simp

Standardwert: `true`






Hat `dot0simp` den Wert `true`, werden nichtkommutative Produkte mit
einer Null und einem skalaren Term zu einem kommutatitiven Produkt vereinfacht.

<!-- category: Other -->
<!-- keywords: dot1simp -->
<!-- signatures: dot1simp -->
### Variable: dot1simp

Standardwert: `true`






Hat `dot1simp` den Wert `true`, werden nichtkommutative Produkte mit
einer Eins und einem anderen Term zu einem kommutativen Produkt vereinfacht.

<!-- category: Other -->
<!-- keywords: dotassoc -->
<!-- signatures: dotassoc -->
### Variable: dotassoc

Standardwert: `true`






Hat `dotassoc` den Wert `true`, vereinfacht Maxima ein Ausdruck
`(A.B).C` zu `A.(B.C)`.

<!-- category: Other -->
<!-- keywords: dotconstrules -->
<!-- signatures: dotconstrules -->
### Variable: dotconstrules

Standardwert: `true`









Hat `dotconstrules` den Wert `true`, werden nichtkommutative Produkte
einer Konstanten und eines Termes zu einem kommutativen Produkt vereinfacht.
Die folgenden Optionsvariablen `dot0simp`, `dot0nscsimp` und 
`dot1simp` erhalten den Wert `true`, wenn `construles` 
eingeschaltet wird.

<!-- category: Other -->
<!-- keywords: dotdistrib -->
<!-- signatures: dotdistrib -->
### Variable: dotdistrib

Standardwert: `false`





Hat `dotdistrib` den Wert `true`, vereinfacht Maxima einen Ausdruck
`A.(B + C)` zu `A.B + A.C`.

<!-- category: Other -->
<!-- keywords: dotexptsimp -->
<!-- signatures: dotexptsimp -->
### Variable: dotexptsimp

Standardwert: `true`





Hat `dotexptsimp` den Wert `true`, vereinfacht Maxima einen Ausdruck 
`A.A` zu `A^^2`.

<!-- category: Other -->
<!-- keywords: dotident -->
<!-- signatures: dotident -->
### Variable: dotident

Standardwert: 1





`dotident` ist der Wert der fur den Ausdruck `X^^0` zuruckgegeben 
wird.

<!-- category: Other -->
<!-- keywords: dotscrules -->
<!-- signatures: dotscrules -->
### Variable: dotscrules

Standardwert: `false`







Hat `dotscrules` den Wert `true`, vereinfacht Maxima Ausdrucke 
`A.SC` oder `SC.A` zu `SC*A` und `A.(SC*B)` zu 
`SC*(A.B)`.

<!-- category: Other -->
<!-- keywords: echelon -->
<!-- signatures: echelon(M) -->
### Function: echelon (M)

Gibt die Matrix *m* in ihrer Stufenform zuruck, wie sie im Gaußschen
Eliminationsverfahren auftritt.





Im Unterschied zur Funktion `triangularize` wird die Matrix so normiert,
dass die Hauptdiagonalelemente den Wert 1 haben.





`lu_factor` und `cholesky` sind weitere Funktionen, um 
Dreiecksmatrizen zu erhalten.


Beispiel:



```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) echelon (M);

                  [ 1  - 8  - 5      - 2     ]
                  [                          ]
                  [         28       11      ]
                  [ 0   1   --       --      ]
(%o2)             [         37       37      ]
                  [                          ]
                  [              37 bb - 119 ]
                  [ 0   0    1   ----------- ]
                  [              37 aa - 313 ]
```

<!-- category: Other -->
<!-- keywords: eigenvalues, eivals -->
<!-- signatures: eigenvalues(M), eivals(M) -->
### Function: eigenvalues (M)

Gibt eine Liste mit den Eigenwerten der Matrix *M* und deren
Multiplizitaten zuruck.  Die erste Teilliste enthalt die Eigenwerte, die
zweite deren Multiplizitaten.




`eivals` ist ein Alias-Name der Funktion `eigenvalues`.











`eigenvalues` ruft die Funktion `solve` auf, um die Nullstellen des
charakeristischen Polynoms der Matrix zu finden.  Wenn `solve` keine
Nullstellen finden kann, funktionieren einige Funktionen des Pakets nicht.
Dies trifft nicht auf die Funktionen `innerproduct`, `unitvector`, 
`columnvector` und `gramschmidt` zu.








Die Eigenwerte, die `solve` findet, konnen sehr komplizierte Ausdrucke 
sein.  Es kann moglich sein, solche Ausdrucke weiter zu vereinfachen.








Das Paket `eigen` wird automatisch geladen, wenn eine der Funktionen
`eigenvalues` oder `eigenvectors` aufgerufen wird.

<!-- category: Other -->
<!-- keywords: eigenvectors, eivects -->
<!-- signatures: eigenvectors(M), eivects(M) -->
### Function: eigenvectors (M)

Berechnet die Eigenvektoren der Matrix *M*.  Die Ruckgabe ist eine Liste, 
die zwei weitere Listen enthalt.  Die erste Liste enthalt die Eigenwerte der
Matrix *m* und deren Multiplizitaten.  Die zweite Liste enthalt die
Eigenvektoren.




`eivects` ist ein Alias-Name der Funktion `eigenvectors`.







Das Paket `eigen` wird automatisch geladen, wenn die Funktionen
`eigenvalues` oder `eigenvectors` aufgerufen werden.




Folgende Schalter kontrollieren `eigenvectors`:



**nondiagonalizable** — `nondiagonalizabel` hat den Wert `true` oder `false` nach
Ruckkehr der Funktion `eigenvectros` abhangig davon, ob die Matrix 
diagonalisierbar ist oder nicht.
**hermitianmatrix** — Hat `hermitianmatrix` den Wert `true`, werden die entarteten
Eigenvektoren einer Hermitischen Matrix mit dem Gram-Schmidt-Verfahren 
orthogonalisiert.
**knowneigvals** — Hat `knowneigvals` den Wert `true`, werden die Eigenwerte der Matrix 
von den Funktionen des Paketes `eigen` als bekannt angenommen.  Die
Eigenwerte sind in diesem Fall in der Liste `listeigvals` abgespeichert.
Die Liste `listeigvals` muss dieselbe Form haben, wie die Ruckgabe der
Funktion `eigenvalues`.










Die Eigenvektoren werden von der Funktion `algsys` berechnet.  Es ist 
moglich, dass `algsys` die Eigenvektoren nicht findet.  In diesem Fall 
konnen moglicherweise zunachst die Eigenwerte bestimmt und weiter 
vereinfacht werden.  Dannach kann die Funktion `eigenvectors` mit dem 
Schalter `knowneigvals` aufgerufen werden.




Siehe auch `eigenvalues`.


Beispiele:




Eine Matrix, die einen Eigenvektor zu jedem Eigenwert hat.



```maxima
(%i1) M1 : matrix ([11, -1], [1, 7]);
                           [ 11  - 1 ]
(%o1)                      [         ]
                           [ 1    7  ]
(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[9 - sqrt(3), sqrt(3) + 9], [1, 1]], 
                        [[[1, sqrt(3) + 2]], [[1, 2 - sqrt(3)]]]]
(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                       val  = 9 - sqrt(3)
                          1

                            mult  = 1
                                1

                    vec  = [[1, sqrt(3) + 2]]
                       1

                       val  = sqrt(3) + 9
                          2

                            mult  = 1
                                2

                    vec  = [[1, 2 - sqrt(3)]]
                       2

(%o3)                         done
```




Eine Matrix, die zwei Eigenvektoren zu jedem Eigenwert hat.



```maxima
(%i1) M1 : matrix([0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], 
                  [0, 0, 0, 2]);

                         [ 0  1  0  0 ]
                         [            ]
                         [ 0  0  0  0 ]
(%o1)                    [            ]
                         [ 0  0  2  0 ]
                         [            ]
                         [ 0  0  0  2 ]

(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[0, 2], [2, 2]], [[[1, 0, 0, 0]],
                                   [[0, 0, 1, 0], [0, 0, 0, 1]]]]
(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                            val  = 0
                               1

                            mult  = 2
                                1

                      vec  = [[1, 0, 0, 0]]
                         1

                            val  = 2
                               2

                            mult  = 2
                                2

               vec  = [[0, 0, 1, 0], [0, 0, 0, 1]]
                  2

(%o3)                         done
```

See also: `eigenvalues`.

<!-- category: Other -->
<!-- keywords: ematrix -->
<!-- signatures: ematrix(m, n, x, i, j) -->
### Function: ematrix (m, n, x, i, j)

Gibt eine *m* `x` *n*-Matrix zuruck, deren Elemente den Wert 0 
haben, bis auf das Element `[i, j]`, das den Wert *x* hat.

<!-- category: Other -->
<!-- keywords: entermatrix -->
<!-- signatures: entermatrix(m, n) -->
### Function: entermatrix (m, n)

Gibt eine *m* `x` *n*-Matrix zuruck, die von der Konsole 
eingelesen wird.






Ist *n* gleich *m*, fragt Maxima nach dem Typ der Matrix.  Folgende
Typen konnen angegeben werden: diagonal, symmetric, antisymmetric oder 
allgemein.  Dannach werden die einzelnen Elemente der Matrix abgefragt.




Sind *n* und *m* voneinander verschieden, fragt Maxima nach jedem 
Element der Matrix.





Die Elemente konnen beliebige Ausdrucke sein, die ausgewertet werden.
`entermatrix` wertet die Argumente aus.


Beispiel:



```maxima
(%i1) n: 3$
(%i2) m: entermatrix (n, n)$

Is the matrix  1. Diagonal  2. Symmetric  3. Antisymmetric 
4. General
Answer 1, 2, 3 or 4 : 
1$
Row 1 Column 1: 
(a+b)^n$
Row 2 Column 2: 
(a+b)^(n+1)$
Row 3 Column 3: 
(a+b)^(n+2)$

Matrix entered.
(%i3) m;
                [        3                     ]
                [ (b + a)      0         0     ]
                [                              ]
(%o3)           [                  4           ]
                [    0      (b + a)      0     ]
                [                              ]
                [                            5 ]
                [    0         0      (b + a)  ]
```

<!-- category: Other -->
<!-- keywords: express -->
<!-- signatures: express(expr) -->
### Function: express (expr)

Expandiert Differentialoperatoren in einem Ausdruck in partielle Ableitungen.
`express` erkennt die Operatoren `grad`, `div`, `curl`, 
`laplacian` und das Kreuzprodukt `~`.






Enthalt die Ruckgabe Substantivformen von Ableitungen, konnen diese mit 
der Funktion `ev` und den Auswertungsschaltern `nouns` oder 
`diff` ausgewertet werden.






Mit dem Kommando `load("vect")` wird die Funktion geladen.


Beispiele:



```maxima
(%i1) load ("vect")$
(%i2) grad (x^2 + y^2 + z^2);
                              2    2    2
(%o2)                  grad (z  + y  + x )
(%i3) express (%);
       d    2    2    2   d    2    2    2   d    2    2    2
(%o3) [-- (z  + y  + x ), -- (z  + y  + x ), -- (z  + y  + x )]
       dx                 dy                 dz
(%i4) ev (%, diff);
(%o4)                    [2 x, 2 y, 2 z]
(%i5) div ([x^2, y^2, z^2]);
                              2   2   2
(%o5)                   div [x , y , z ]
(%i6) express (%);
                   d    2    d    2    d    2
(%o6)              -- (z ) + -- (y ) + -- (x )
                   dz        dy        dx
(%i7) ev (%, diff);
(%o7)                    2 z + 2 y + 2 x
(%i8) curl ([x^2, y^2, z^2]);
                               2   2   2
(%o8)                   curl [x , y , z ]
(%i9) express (%);
       d    2    d    2   d    2    d    2   d    2    d    2
(%o9) [-- (z ) - -- (y ), -- (x ) - -- (z ), -- (y ) - -- (x )]
       dy        dz       dz        dx       dx        dy
(%i10) ev (%, diff);
(%o10)                      [0, 0, 0]
(%i11) laplacian (x^2 * y^2 * z^2);
                                  2  2  2
(%o11)                laplacian (x  y  z )
(%i12) express (%);
         2                2                2
        d     2  2  2    d     2  2  2    d     2  2  2
(%o12)  --- (x  y  z ) + --- (x  y  z ) + --- (x  y  z )
          2                2                2
        dz               dy               dx
(%i13) ev (%, diff);
                      2  2      2  2      2  2
(%o13)             2 y  z  + 2 x  z  + 2 x  y
(%i14) [a, b, c] ~ [x, y, z];
(%o14)                [a, b, c] ~ [x, y, z]
(%i15) express (%);
(%o15)          [b z - c y, c x - a z, a y - b x]
```

<!-- category: Other -->
<!-- keywords: genmatrix -->
<!-- signatures: genmatrix(a, i_2, j_2, i_1, j_1), genmatrix(a, i_2, j_2, i_1), genmatrix(a, i_2, j_2) -->
### Function: genmatrix (a, i_2, j_2, i_1, j_1)

Generiert eine Matrix aus einem Array *a*.  Das erste Element der Matrix
ist der Wert `a[i_1,j_1]` und das letzte Element der
Matrix ist `a[i_2,j_2]`.  *a* muss ein deklariertes
Array sein, dass mit der Funktion `array` definiert wurde.  Weiterhin kann
*a* ein undeklariertes Array, eine Array-Funktion oder ein lambda-Ausdruck
mit zwei Argumenten sein.





Wird *j_1* nicht angegeben, nimmt Maxima an, das der Wert gleich *i_1* 
ist.  Werden beide Argumente *j_1* und *i_1* nicht angegeben, werden
die Werte zu 1 angenommen.





Ist eines der Elemente `[i,j]` des Arrays nicht definiert, enthalt die
Matrix den symbolischen Wert `a[i,j]`.


Beispiele:



```maxima
(%i1) h [i, j] := 1 / (i + j - 1);

                                    1
(%o1)                  h     := ---------
                        i, j    i + j - 1

(%i2) genmatrix (h, 3, 3);
                           [    1  1 ]
                           [ 1  -  - ]
                           [    2  3 ]
                           [         ]
                           [ 1  1  1 ]
(%o2)                      [ -  -  - ]
                           [ 2  3  4 ]
                           [         ]
                           [ 1  1  1 ]
                           [ -  -  - ]
                           [ 3  4  5 ]
(%i3) array (a, fixnum, 2, 2);
(%o3)                           a
(%i4) a [1, 1] : %e;
(%o4)                          %e
(%i5) a [2, 2] : %pi;
(%o5)                          %pi
(%i6) genmatrix (a, 2, 2);
                           [ %e   0  ]
(%o6)                      [         ]
                           [ 0   %pi ]
(%i7) genmatrix (lambda ([i, j], j - i), 3, 3);
                         [  0    1   2 ]
                         [             ]
(%o7)                    [ - 1   0   1 ]
                         [             ]
                         [ - 2  - 1  0 ]
(%i8) genmatrix (B, 2, 2);
                        [ B      B     ]
                        [  1, 1   1, 2 ]
(%o8)                   [              ]
                        [ B      B     ]
                        [  2, 1   2, 2 ]
```

<!-- category: Other -->
<!-- keywords: gramschmidt -->
<!-- signatures: gramschmidt(x), gramschmidt(x, F) -->
### Function: gramschmidt (x)

Wendet das Gram-Schmidtsche Orthogonalisierungsverfahren auf das Argument
*x* an.  *x* ist eine Matrix oder eine Liste mit Listen fur die 
Spalten.  Das Argument *x* wird von `gramschmidt` nicht verandert.
*F* bezeichnet eine Funktion, die als Skalarprodukt fur das Verfahren 
verwendet wird.  Wird *F* nicht angegeben, wird die Funktion 
`innerproduct` fur das Skalarprodukt angewendet.









Ist *x* eine Matrix, wird der Algorithmus auf die Zeilen der Matrix
angewendet.  Ist *x* eine Liste mit Listen, wird der Algorithmus auf die
Teillisten angewendet, die jeweils die gleiche Anzahl an Elementen haben
mussen.






Jede Stufe des Verfahrens ruft die Funktion `factor` auf, um die 
Zwischenergebnisse zu vereinfachen.  Dadurch kann das Ergebnis faktorisierte
ganze Zahlen enthalten.




Das Kommando `load("eigen")` ladt die Funktion.


Beispiele:




Das Gram-Schmidtsche Orthogonalisierungsverfahren mit `innerproduct` 
als Skalarprodukt.



```maxima
(%i1) load ("eigen")$
(%i2) x: matrix ([1, 2, 3], [9, 18, 30], [12, 48, 60]);
                         [ 1   2   3  ]
                         [            ]
(%o2)                    [ 9   18  30 ]
                         [            ]
                         [ 12  48  60 ]
(%i3) y: gramschmidt (x);
                       2      2            4     3
                      3      3   3 5      2  3  2  3
(%o3)  [[1, 2, 3], [- ---, - --, ---], [- ----, ----, 0]]
                      2 7    7   2 7       5     5
(%i4) map (innerproduct, [y[1], y[2], y[3]], [y[2], y[3], y[1]]);
(%o4)                       [0, 0, 0]
```




Das Gram-Schmidtsche Orthogonalisierungsverfahren mit einer selbstdefinierten
Funktion fur das Skalarprodukt.



```maxima
(%i1) load ("eigen")$
(%i2) ip (f, g) := integrate (f * g, u, a, b);
(%o2)          ip(f, g) := integrate(f g, u, a, b)
(%i3) y : gramschmidt([1, sin(u), cos(u)], ip), a=-%pi/2, b=%pi/2;
                               %pi cos(u) - 2
(%o3)              [1, sin(u), --------------]
                                    %pi
(%i4) map(ip,[y[1],y[2],y[3]],[y[2],y[3],y[1]]), a=-%pi/2, b=%pi/2;
(%o4)                       [0, 0, 0]
```

<!-- category: Other -->
<!-- keywords: ident -->
<!-- signatures: ident(n) -->
### Function: ident (n)

Gibt eine *n* `x` *n*-Einheitsmatrix zuruck.

<!-- category: Other -->
<!-- keywords: innerproduct, inprod -->
<!-- signatures: innerproduct(x, y), inprod(x, y) -->
### Function: innerproduct (x, y)

Gibt das Skalarprodukt der Argumente *x* und *y* zuruck.  Die Argument
konnen Listen oder 1-spaltige oder 1-reihige Matrizen sein.  Das Skalarprodukt
wird als `conjugate(x) . y` berechnet, wobei `.` der Operator der
nicht-kommutativen Multiplikation ist.




Das Kommando `load("eigen")` ladt die Funktion.




`inprod` ist ein Alias-Name der Funktion `innerproduct`.

<!-- category: Other -->
<!-- keywords: invert -->
<!-- signatures: invert(M) -->
### Function: invert (M)

Gibt die inverse Matrix der Matrix *M* zuruck.  Die inverse Matrix wird
mittels der Adjunkten Matrix berechnet.





Mit dieser Methode kann die inverse Matrix auch fur große Gleitkommazahlen
sowie Polynomme als Matrixelemente berechnet werden.






Die Kofaktoren werden mit der Funktion `determinant` berechnet.  Hat die
Optionsvariable `ratmx` den Wert `true`, wird die inverse Matrix
daher ohne einen Wechsel der Darstellung berechnet.




Die implementierte Methode ist jedoch ineffizient fur große Matrizen.





Hat die Optionsvariable `detout` den Wert `true`, wird die 
Determinante als Faktor aus der Matrix herausgezogen.








Die Elemente der inversen Matrix werden nicht automatisch expandiert.  Hat
*M* Polynome als Elemente, hat das Ergebnis moglicherweise mit dem
Kommando `expand(invert(m)), detout` eine einfachere Form.  Mit der Funktion
`multthru` die Determinate in die Matrix hereinmultipliziert werden.  Die
inverse Matrix kann auch folgendermaßen berechnet werden:



```maxima
expand (adjoint (m)) / expand (determinant (m))
invert (m) := adjoint (m) / determinant (m)
```





Siehe auch den Operator `^^` der nicht-kommutativen Exponentiation fur 
eine andere Methode zur Berechnung der inversen Matrix.

<!-- category: Other -->
<!-- keywords: lmxchar -->
<!-- signatures: lmxchar -->
### Variable: lmxchar

Standardwert: `[`





`lmxchar` ist das Zeichen, das fur die linke Seite einer Matrix 
ausgegeben wird.  Siehe auch `rmxchar`.


Beispiel:



```maxima
(%i1) lmxchar: "|"$
(%i2) matrix ([a, b, c], [d, e, f], [g, h, i]);
                           | a  b  c ]
                           |         ]
(%o2)                      | d  e  f ]
                           |         ]
                           | g  h  i ]
```

<!-- category: Other -->
<!-- keywords: matrix -->
<!-- signatures: matrix(row_1, ..., row_n) -->
### Function: matrix (row_1, ..., row_n)

Gibt eine Matrix mit den Spalten *row_1*, ..., *row_n* zuruck.
Jede Spalte ist eine Liste mit Asudrucken.  Alle Spalten mussen die gleiche
Lange haben.












Die Addition `+`, Subtraktion `-`, Multiplikation `*` und 
Division `/` werden elementweise ausgefuhrt, wenn die Argumente zwei 
Matrizen, ein Skalar und eine Matrix oder eine Matrix und ein Skalar sind.
Die Exponentiation `^` wird elementweise ausgefuhrt, wenn die Argumente
ein Skalar und eine Matrix oder umgekehrt sind.







Die nichtkommutatie Multiplikation von Matrizen wird mit dem Operator `.`
ausgefuhrt.  Der entsprechende Operator fur die nichtkommutative 
Exponentiation ist `^^`. Fur eine Matrix `A` ist 
`A . A = A^^2`. `A^^-1` ist die inverse 
Matrix, falls diese existiert.








Folgende Schalter kontrollieren die Vereinfachung von Ausdrucken, welche die
nichtkommutative Multiplikation und Matrizen enthalten:


`doallmxops`,
`domxexpt`,
`domxmxops`, 
`doscmxops` und 
`doscmxplus`.







Weitere Optionsvariablen fur Matrizen sind:


`lmxchar`, 
`rmxchar`, 
`ratmx`, 
`listarith`, 
`detout`,
`scalarmatrix` und
`sparse`.









Folgende Funktionen akzeptieren Matrizen als ein Argument oder haben eine 
Matrix als Ruckgabewert: 


`eigenvalues`, 
`eigenvectors`,
`determinant`,
`charpoly`, 
`genmatrix`, 
`addcol`, 
`addrow`, 
`copymatrix`, 
`transpose`, 
`echelon` and
`rank`.


Beispiele:




Konstruiere eine Matrix mit Listen.



```maxima
(%i1) x: matrix ([17, 3], [-8, 11]);
                           [ 17   3  ]
(%o1)                      [         ]
                           [ - 8  11 ]
(%i2) y: matrix ([%pi, %e], [a, b]);
                           [ %pi  %e ]
(%o2)                      [         ]
                           [  a   b  ]
```




Elementweise Addition zweier Matrizen.



```maxima
(%i3) x + y;
                      [ %pi + 17  %e + 3 ]
(%o3)                 [                  ]
                      [  a - 8    b + 11 ]
```




Elementweise Subtraktion zweier Matrizen.



```maxima
(%i4) x - y;
                      [ 17 - %pi  3 - %e ]
(%o4)                 [                  ]
                      [ - a - 8   11 - b ]
```




Elementweise Multiplikation zweier Matrizen.



```maxima
(%i5) x * y;
                        [ 17 %pi  3 %e ]
(%o5)                   [              ]
                        [ - 8 a   11 b ]
```




Elementweise Division zweier Matrizen.



```maxima
(%i6) x / y;
                        [ 17       - 1 ]
                        [ ---  3 %e    ]
                        [ %pi          ]
(%o6)                   [              ]
                        [   8    11    ]
                        [ - -    --    ]
                        [   a    b     ]
```




Elementweise Exponentiation einer Matrix mit einem Skalar.



```maxima
(%i7) x ^ 3;
                         [ 4913    27  ]
(%o7)                    [             ]
                         [ - 512  1331 ]
```




Elementweise Exponentiation eines Skalars mit einer Matrix.



```maxima
(%i8) exp(y); 
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o8)                    [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```





Die Exponentiation zweier Matrizen wird nicht elementweise ausgefuhrt.



```maxima
(%i9) x ^ y;
                                [ %pi  %e ]
                                [         ]
                                [  a   b  ]
                     [ 17   3  ]
(%o9)                [         ]
                     [ - 8  11 ]
```




Nichtkommutative Multiplikation zweier Matrizen.



```maxima
(%i10) x . y;
                  [ 3 a + 17 %pi  3 b + 17 %e ]
(%o10)            [                           ]
                  [ 11 a - 8 %pi  11 b - 8 %e ]
(%i11) y . x;
                [ 17 %pi - 8 %e  3 %pi + 11 %e ]
(%o11)          [                              ]
                [  17 a - 8 b     11 b + 3 a   ]
```






Nichtkommutative Exponentiation einer Matrix.  Ist die Basis ein Skalar wird die
Exponentiation elementweise ausgefuhrt.  Daher haben die Operationen `^^`
und `^` fur diesen Fall dasselbe Ergebnis.



```maxima
(%i12) x ^^ 3;
                        [  3833   1719 ]
(%o12)                  [              ]
                        [ - 4584  395  ]
(%i13) %e ^^ y;
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o13)                   [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```





Berechnung der inversen Matrix mit `x^^-1`.



```maxima
(%i14) x ^^ -1;

                         [ 11      3  ]
                         [ ---  - --- ]
                         [ 211    211 ]
(%o14)                   [            ]
                         [  8    17   ]
                         [ ---   ---  ]
                         [ 211   211  ]

(%i15) x . (x ^^ -1);
                            [ 1  0 ]
(%o15)                      [      ]
                            [ 0  1 ]
```

<!-- category: Other -->
<!-- keywords: matrix_element_add -->
<!-- signatures: matrix_element_add -->
### Variable: matrix_element_add

Standardwert: `+`








`matrix_element_add` enthalt die Operation fur die Ausfuhrung der
Addition von Matrizen.  Der Optionsvariablen `matrix_element_add` kann
ein N-Ary-Operator zugewiesen werden.  Der zugewiesene Wert kann der Name
eines Operators, einer Funktion oder ein Lambda-Ausdruck sein.




Siehe auch `matrix_element_mult` und `matrix_element_transpose`.


Beispiele:



```maxima
(%i1) matrix_element_add: "*"$
(%i2) matrix_element_mult: "^"$
(%i3) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o3)                      [         ]
                           [ d  e  f ]
(%i4) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o4)                      [         ]
                           [ x  y  z ]
(%i5) aa . transpose (bb);
                     [  u  v  w   x  y  z ]
                     [ a  b  c   a  b  c  ]
(%o5)                [                    ]
                     [  u  v  w   x  y  z ]
                     [ d  e  f   d  e  f  ]
```

<!-- category: Other -->
<!-- keywords: matrix_element_mult -->
<!-- signatures: matrix_element_mult -->
### Variable: matrix_element_mult

Standardwert: `*`








`matrix_element_mult` enthalt die Operation fur die Ausfuhrung der
Multiplikation von Matrizen.  Der Optionsvariablen `matrix_element_mult` 
kann ein binarer Operator zugewiesen werden.  Der zugewiesene Wert kann der 
Name eines Operators, einer Funktion oder ein Lambda-Ausdruck sein.




Der nichtkommutative Operator `.` kann eine sinnvolle Alternative sein.




Siehe auch `matrix_element_add` und `matrix_element_transpose`.


Beispiele:



```maxima
(%i1) matrix_element_add: lambda ([[x]], sqrt (apply ("+", x)))$
(%i2) matrix_element_mult: lambda ([x, y], (x - y)^2)$
(%i3) [a, b, c] . [x, y, z];
                          2          2          2
(%o3)         sqrt((c - z)  + (b - y)  + (a - x) )
(%i4) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o4)                      [         ]
                           [ d  e  f ]
(%i5) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o5)                      [         ]
                           [ x  y  z ]
(%i6) aa . transpose (bb);
               [             2          2          2  ]
               [ sqrt((c - w)  + (b - v)  + (a - u) ) ]
(%o6)  Col 1 = [                                      ]
               [             2          2          2  ]
               [ sqrt((f - w)  + (e - v)  + (d - u) ) ]

                         [             2          2          2  ]
                         [ sqrt((c - z)  + (b - y)  + (a - x) ) ]
                 Col 2 = [                                      ]
                         [             2          2          2  ]
                         [ sqrt((f - z)  + (e - y)  + (d - x) ) ]
```

<!-- category: Other -->
<!-- keywords: matrix_element_transpose -->
<!-- signatures: matrix_element_transpose -->
### Variable: matrix_element_transpose

Standardwert: `false`







`matrix_element_transpose` enthalt die Operation fur die Ausfuhrung 
der Transponierung einer Matrix.  Der Optionsvariablen
`matrix_element_mult` kann ein unarer Operator zugewiesen werden.  Der 
zugewiesene Wert kann der Name eines Operators, einer Funktion oder ein
Lambda-Ausdruck sein.










Hat `matrix_element_transpose` den Wert `transpose`, wird die 
Funktion `transpose` auf jedes Element der Matrix angewendet.  Hat
`matrix_element_transpose` den Wert `nonscalars`, wird die Funktion
`transpose` auf nichtskalare Elemente der Matrix angewendet.  Ist eines
der Elemente ein Atom, muss in diesem Fall das Atom als `nonscalar`
deklariert sein.




Mit dem Standardwert `false` wird keine Operation angewendet.




Siehe auch `matrix_element_add` und `matrix_element_mult`.


Beispiele:



```maxima
(%i1) declare (a, nonscalar)$
(%i2) transpose ([a, b]);
                        [ transpose(a) ]
(%o2)                   [              ]
                        [      b       ]
(%i3) matrix_element_transpose: nonscalars$
(%i4) transpose ([a, b]);
                        [ transpose(a) ]
(%o4)                   [              ]
                        [      b       ]
(%i5) matrix_element_transpose: transpose$
(%i6) transpose ([a, b]);
                        [ transpose(a) ]
(%o6)                   [              ]
                        [ transpose(b) ]
(%i7) matrix_element_transpose: lambda ([x], realpart(x)
      - %i*imagpart(x))$
(%i8) m: matrix ([1 + 5*%i, 3 - 2*%i], [7*%i, 11]);
                     [ 5 %i + 1  3 - 2 %i ]
(%o8)                [                    ]
                     [   7 %i       11    ]
(%i9) transpose (m);
                      [ 1 - 5 %i  - 7 %i ]
(%o9)                 [                  ]
                      [ 2 %i + 3    11   ]
```

<!-- category: Other -->
<!-- keywords: matrixmap -->
<!-- signatures: matrixmap(f, M) -->
### Function: matrixmap (f, M)

Gibt eine Matrix mit den Elementen `[i,j]` zuruck, die mit
`f(M[i,j])` berechnet werden.




Siehe auch `map`, `fullmap`, `fullmapl`, and `apply`.

<!-- category: Other -->
<!-- keywords: matrixp -->
<!-- signatures: matrixp(expr) -->
### Function: matrixp (expr)

Gibt `true` zuruck, wenn *expr* eine Matrix ist.  Ansonsten wird
`false` zuruckgegeben.

<!-- category: Other -->
<!-- keywords: mattrace -->
<!-- signatures: mattrace(M) -->
### Function: mattrace (M)

Gibt die Spur einer quadratischen Matrix *M* zuruck.

<!-- category: Other -->
<!-- keywords: minor -->
<!-- signatures: minor(M, i, j) -->
### Function: minor (M, i, j)

Gibt den Minor zu *i*, *j* der Matrix *M* zuruck.  Die Matrix
entsteht durch Streichen der *i*-ten Spalte und *j*-ten Zeile.

<!-- category: Other -->
<!-- keywords: ncharpoly -->
<!-- signatures: ncharpoly(M, x) -->
### Function: ncharpoly (M, x)

Gibt das charakteristische Polynom der Matrix *M* fur die Variable *x*
zuruck.  Diese Funktion ist eine Alternative zur Funktion `charpoly`.













Der Algorithmus von `ncharpoly` ist vorteilhaft gegenuber 
`charpoly`, wenn große und dunn besetzte Matrizen vorliegen.  Das 
Kommando `load("nchrpl")` ladt die Funktion.

<!-- category: Other -->
<!-- keywords: newdet -->
<!-- signatures: newdet(M, n) -->
### Function: newdet (M, n)

Berechnet die Determinate der Matrix oder eines Arrays *M* mit dem
Johnson-Gentleman-Algorithmus.  Das Argument *n* ist die Ordnung.  Fur
eine Matrix ist *n* ein optionales Argument.

<!-- category: Other -->
<!-- keywords: permanent -->
<!-- signatures: permanent(M, n) -->
### Function: permanent (M, n)

Berechnet die Permanente der Matrix *M*.  Die Permanente ist ahnlich der
Determinate, aber es fehlen die Vorzeichenwechsel.

<!-- category: Other -->
<!-- keywords: potential -->
<!-- signatures: potential(givengradient) -->
### Function: potential (givengradient)

The calculation makes use of the global variable `potentialzeroloc[0]`
which must be `nonlist` or of the form



```maxima
[indeterminatej=expressionj, indeterminatek=expressionk, ...]
```


the former being equivalent to the nonlist expression for all right-hand 
sides in the latter.  The indicated right-hand sides are used as the lower 
limit of integration.  The success of the integrations may depend upon their 
values and order.  `potentialzeroloc` is initially set to 0.

<!-- category: Other -->
<!-- keywords: rank -->
<!-- signatures: rank(M) -->
### Function: rank (M)

Berechnet den Rang der Matrix *M*.






*rank* kann ein falsches Ergebnis geben, wenn ein Element aquivalent
zu Null ist, dies aber nicht von Maxima festgestellt werden kann.

<!-- category: Other -->
<!-- keywords: ratmx -->
<!-- signatures: ratmx -->
### Variable: ratmx

Standardwert: `false`







Hat `ratmx` den Wert `false`, werden die Berechnung einer Determinante
sowie die Operationen der Addition, Subtraktion und Multiplikation in der
allgemeinen Darstellung ausgefuhrt.  Das Ergebnis ist wieder eine allgemeine
Darstellung.







Hat `ratmx` den Wert `true`, werden die oben genannten Operationen
in einer CRE-Darstellung ausgefuhrt un das Ergebnis ist in einer 
CRE-Darstellung.

<!-- category: Other -->
<!-- keywords: rmxchar -->
<!-- signatures: rmxchar -->
### Variable: rmxchar

Standardwert: `]`




`rmxchar` ist das Zeichen, das fur die rechte Seite einer Matrix 
ausgegeben wird.  Siehe auch `lmxchar`.

<!-- category: Other -->
<!-- keywords: row -->
<!-- signatures: row(M, i) -->
### Function: row (M, i)

Gibt die *i*-te Spalte der Matrix *M* zuruck.  Der Ruckgabewert ist 
eine Matrix.

<!-- category: Other -->
<!-- keywords: scalarmatrixp -->
<!-- signatures: scalarmatrixp -->
### Variable: scalarmatrixp

Standardwert: `true`






Hat `scalarmatrixp` den Wert `true`, dann werden 1 x 1-Matrizen, die
als Ergebnis einer nicht-kommutativen Multiplikation auftreten, zu einem
Skalar vereinfacht.





Hat `scalarmatrixp` den Wert `all`, dann werden alle 1 x 1-Matrizen
zu einem Skalar vereinfacht.





Hat `scalarmatrixp` den Wert `false`, werden 1 x 1-Matrizen nicht zu
einem Skalar vereinfacht.

<!-- category: Other -->
<!-- keywords: scalefactors -->
<!-- signatures: scalefactors(coordinatetransform) -->
### Function: scalefactors (coordinatetransform)

Here coordinatetransform evaluates to the form [[expression1, expression2,
...], indeterminate1, indeterminat2, ...], where indeterminate1, 
indeterminate2, etc. are the curvilinear coordinate variables and where a set of
rectangular Cartesian components is given in terms of the curvilinear
coordinates by [expression1, expression2, ...].  `coordinates` is set
to the vector [indeterminate1, indeterminate2, ...], and `dimension` is 
set to the length of this vector.  SF[1], SF[2], ..., SF[DIMENSION] are set
to the coordinate scale factors, and `sfprod` is set to the product of
these scale factors.  Initially, `coordinates` is [X, Y, Z],
`dimension` is 3, and SF[1]=SF[2]=SF[3]=SFPROD=1, corresponding to 
3-dimensional rectangular Cartesian coordinates.  To expand an expression into 
physical components in the current coordinate system, there is a function with 
usage of the form

<!-- category: Other -->
<!-- keywords: setelmx -->
<!-- signatures: setelmx(x, i, j, M) -->
### Function: setelmx (x, i, j, M)

Weist *x* dem Matrixelement `[i,j]` zu und gibt die
modifizierte Matrix zuruck.





`M[i, j]: x` hat denselben Effekt.  In diesem Fall
wird jedoch der Wert *x* zuruckgeben und nicht die Matrix.

<!-- category: Other -->
<!-- keywords: similaritytransform, simtran -->
<!-- signatures: similaritytransform(M), simtran(M) -->
### Function: similaritytransform (M)

`similaritytransform` computes a similarity transform of the matrix 
`M`.  It returns a list which is the output of the `uniteigenvectors`
command.  In addition if the flag `nondiagonalizable` is `false` two 
global matrices `leftmatrix` and `rightmatrix` are computed.  These 
matrices have the property that `leftmatrix . M . rightmatrix` is a 
diagonal matrix with the eigenvalues of *M* on the diagonal.  If 
`nondiagonalizable` is `true` the left and right matrices are not 
computed.


If the flag `hermitianmatrix` is `true` then `leftmatrix` is the 
complex conjugate of the transpose of `rightmatrix`.  Otherwise 
`leftmatrix` is the inverse of `rightmatrix`.


`rightmatrix` is the matrix the columns of which are the unit eigenvectors 
of *M*.  The other flags (see `eigenvalues` and `eigenvectors`) 
have the same effects since `similaritytransform` calls the other functions
in the package in order to be able to form `rightmatrix`.


`load ("eigen")` loads this function.


`simtran` is a synonym for `similaritytransform`.

<!-- category: Other -->
<!-- keywords: sparse -->
<!-- signatures: sparse -->
### Variable: sparse

Standardwert: `false`






Haben `sparse` und `ratmx` den Wert `true`, verwendet die 
Funktion `determinant` einen speziellen Algorithmus fur dunn besetzte
Matrizen, um die Determinante einer Matrix zu berechnen.

<!-- category: Other -->
<!-- keywords: submatrix -->
<!-- signatures: submatrix(i_1, ..., i_m, M, j_1, ..., j_n), submatrix(i_1, ..., i_m, M), submatrix(M, j_1, ..., j_n) -->
### Function: submatrix (i_1, ..., i_m, M, j_1, ..., j_n)

Gibt eine Kopie der Matrix *M* zuruck, in der die Zeilen 
*i_1*, ..., *i_m* und Spalten *j_1*, ..., *j_n* 
nicht enthalten sind.

<!-- category: Other -->
<!-- keywords: transpose -->
<!-- signatures: transpose(M) -->
### Function: transpose (M)

Gibt die Transponierte der Matrix *M* zuruck.





Ist *M* eine Matrix, ist das Ergebnis eine Matrix *N* mit den 
Elementen `N[i,j] = M[j,i]`.





Ist *M* eine Liste, ist die Ruckgabe eine Matrix *N* mit
`length(M)` Spalten und einer Zeile.  Die Elemente sind 
`N[i,1] = M[i]`.





Ansonsten wird eine Substantivform `'transpose(M)` zuruckgegeben.

<!-- category: Other -->
<!-- keywords: triangularize -->
<!-- signatures: triangularize(M) -->
### Function: triangularize (M)

Gibt die obere Dreiecksmatrix fur die Matrix `M` zuruck, wie sie mit 
dem Gaußschen Eliminationsverfahren berechnet wird.  Die Dreiecksmatrix 
entspricht der Ruckgabe der Funktion `echelon` mit dem Unterschied, dass 
die Elemente auf der Diagonalen nicht zu 1 normalisiert sind.





Mit den Funktionen `lu_factor` und `cholesky` kann ebenfalls eine
Matrix in die Dreiecksform transformiert werden.


Beispiel:



```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) triangularize (M);
             [ - 1   8         5            2      ]
             [                                     ]
(%o2)        [  0   - 74     - 56         - 22     ]
             [                                     ]
             [  0    0    626 - 74 aa  238 - 74 bb ]
```

<!-- category: Other -->
<!-- keywords: uniteigenvectors, ueivects -->
<!-- signatures: uniteigenvectors(M), ueivects(M) -->
### Function: uniteigenvectors (M)

Berechnet die Einheitsvektoren der Matrix *M*.  Die Ruckgabe ist eine 
Liste, die zwei weitere Listen enthalt.  Die erste Liste enthalt die 
Eigenwerte der Matrix *M* und deren Multiplizitaten.  Die zweite Liste 
enthalt die Einheitsvektoren.


Ansonsten entspricht `uniteigenvectors` der Funktion `eigenvectors`.





















Das Kommando `load("eigen")` ladt die Funktion.




`ueivects` ist ein Alias-Name der Funkion `uniteigenvectors`.

<!-- category: Other -->
<!-- keywords: unitvector, uvect -->
<!-- signatures: unitvector(x), uvect(x) -->
### Function: unitvector (x)

Gibt den Einheitsvektor $x/norm(x)$ zuruck.




Das Kommando `load("eigen")` ladt die Funktion.




`uvect` ist ein Alias-Name der Funktion `unitvector`.

<!-- category: Other -->
<!-- keywords: vect_cross -->
<!-- signatures: vect_cross -->
### Variable: vect_cross

Standardwert: `false`






Hat `vect_cross` den Wert `true`, werden Ausdrucke, die die 
Ableitung eines Kreuzproduktes enthalten, vereinfacht.


Beispiel:



```maxima
(%i1) load("vect")$

(%i2) vect_cross:false;
(%o2)                         false
(%i3) diff(f(x)~g(x),x);
                        d
(%o3)                   -- (f(x) ~ g(x))
                        dx
(%i4) vect_cross:true;
(%o4)                         true
(%i5) diff(f(x)~g(x),x);
                     d                    d
(%o5)        f(x) ~ (-- (g(x))) - g(x) ~ (-- (f(x)))
                     dx                   dx
```

<!-- category: Other -->
<!-- keywords: vectorpotential -->
<!-- signatures: vectorpotential(givencurl) -->
### Function: vectorpotential (givencurl)

Returns the vector potential of a given curl vector, in the current 
coordinate system.  `potentialzeroloc` has a similar role as for 
`potential`, but the order of the left-hand sides of the equations must 
be a cyclic permutation of the coordinate variables.

<!-- category: Other -->
<!-- keywords: vectorsimp -->
<!-- signatures: vectorsimp(expr) -->
### Function: vectorsimp (expr)

Applies simplifications and expansions according to the following global flags:



expandall         expanddot             expanddotplus
expandcross       expandcrossplus       expandcrosscross
expandgrad        expandgradplus        expandgradprod
expanddiv         expanddivplus         expanddivprod
expandcurl        expandcurlplus        expandcurlcurl 
expandlaplacian   expandlaplacianplus   expandlaplacianprod


All these flags have default value `false`.  The `plus` suffix refers
to employing additivity or distributivity.  The `prod` suffix refers to 
the expansion for an operand that is any kind of product.



**expandcrosscross** — Simplifies `p ~ (q ~ r)` to `(p . r)*q - (p . q)*r`.
**expandcurlcurl** — Simplifies `curl curl p` to `grad div p + div grad p`.
**expandlaplaciantodivgrad** — Simplifies `laplacian p` to `div grad p`.
**expandcross** — Enables `expandcrossplus` and `expandcrosscross`.
**expandplus** — Enables `expanddotplus`, `expandcrossplus`, `expandgradplus`,
`expanddivplus`, `expandcurlplus`, and `expandlaplacianplus`.
**expandprod** — Enables `expandgradprod`, `expanddivprod`, and 
`expandlaplacianprod`.



These flags have all been declared `evflag`.

<!-- category: Other -->
<!-- keywords: zeromatrix -->
<!-- signatures: zeromatrix(m, n) -->
### Function: zeromatrix (m, n)

Gibt eine *m* x *n*-Matrix zuruck, deren Elemente alle Null sind.

