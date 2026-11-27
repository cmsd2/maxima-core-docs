## Polynome

<!-- category: Polynomials -->
<!-- keywords: algebraic -->
<!-- signatures: algebraic -->
### Variable: algebraic

Standardwert: `false`


Hat die Optionsvariable `algebraic` den Wert `true`, wird beim
Umwandeln von Ausdrucken in die CRE-Form und beim Rechnen mit Ausdrucken
in einer CRE-Form der Ausdruck so vereinfacht, dass der Nenner frei von
algebraischen Zahlen (das sind Wurzeln von ganzen Zahlen) ist.



Beispiele:


Im zweiten Beispiel wird der Ausdruck automatisch mit `sqrt(2)` erweitert,
um den Nenner frei von der algebraischen Zahl `sqrt(2)` zu machen.



```maxima
(%i1) algebraic:false;
(%o1)                         false
(%i2) rat(x^2+x)/sqrt(2);
                              2
                             x  + x
(%o2)/R/                     -------
                             sqrt(2)
(%i3) algebraic:true;
(%o3)                         true
(%i4) rat(x^2+x)/sqrt(2);
                              2
                     sqrt(2) x  + sqrt(2) x
(%o4)/R/             ----------------------
                               2
```

<!-- category: Polynomials -->
<!-- keywords: berlefact -->
<!-- signatures: berlefact -->
### Variable: berlefact

Standardwert: `true`


Hat die Optionsvariable `berlefact` den Wert `false`, dann wird der
Kronecker-Al­go­rith­mus von der Funktion `factor` fur die
Faktorisierung genutzt.  Ansonsten wird der Berlekamp-Algorithmus genutzt.  Der
Standardwert ist `true`.

See also: `factor`.

<!-- category: Polynomials -->
<!-- keywords: bezout -->
<!-- signatures: bezout(p1, p2, x) -->
### Function: bezout (p1, p2, x)

Die Ruckgabe ist die Sylvestermatrix der zwei Polynome *p1* und *p2*
mit der unabhangigen Variablen *x*.  Die Determinante der Sylvestermatrix
ist die Resultante der Polynome.  Die Resultante kann auch sofort mit der
Funktion `resultant` berechnet werden.


Beispiele:



```maxima
(%i1) bezout(a*x+b, c*x^2+d, x);
                         [ b c  - a d ]
(%o1)                    [            ]
                         [  a     b   ]
(%i2) determinant(%);
                            2      2
(%o2)                      a  d + b  c
(%i3) resultant(a*x+b, c*x^2+d, x);
                            2      2
(%o3)                      a  d + b  c
```

See also: `resultant`.

<!-- category: Polynomials -->
<!-- keywords: bothcoef -->
<!-- signatures: bothcoef(expr, x) -->
### Function: bothcoef (expr, x)

Gibt eine Liste zuruck, deren erstes Element der Koeffizient der Variablen
*x* im Ausdruck *expr* und deren zweites Element der verbleibende
Teil des Ausdrucks *expr* ist.  Das Ergebnis ist also `[A,B]` und es
gilt `expr = A * x + B`.


Die Funktion `bothcoef` hat den Alias-Namen `bothcoeff`.


Siehe auch die Funktion `coeff`.


Beispiele:



```maxima
(%i1) bothcoeff(a*x+2, x);
(%o1)                        [a, 2]
(%i2) bothcoeff(x^2+a*x+2, x);
                                2
(%o2)                      [a, x  + 2]
```


Definition einer Funktion `islinear`, die die Funktion `bothcoeff`
nutzt, um den linearen Anteil eines Ausdrucks zu ermitteln.



```maxima
(%i1) islinear (expr, x) := 
         block ([c],
            c: bothcoef (rat (expr, x), x),
            is (freeof (x, c) and c[1] # 0))$
(%i2) islinear ((r^2 - (x - r)^2)/x, x);
(%o2)                         true
```

See also: `coeff`.

<!-- category: Polynomials -->
<!-- keywords: coeff -->
<!-- signatures: coeff(expr, x, n), coeff(expr, x) -->
### Function: coeff (expr, x, n)

Gibt den Koeffizienten von `x^n` des Ausdrucks *expr*
zuruck.  Das Argument *expr* ist ein Polynom in der Variablen *x*.


Das Kommando `coeff(expr, x^n)` ist aquivalent zu
`coeff(expr, x, n)`.  Das Kommando
`coeff(expr, x, 0)` gibt den Teil des Ausdrucks *expr*
zuruck, der frei von der Variablen *x* ist.  Wenn nicht angegeben, wird
das Argument *n* als `1` angenommen.


Das Argument *x* kann auch eine indizierte Variable oder ein Teilausdruck
von *expr* sein.


`coeff` wendet weder die Funktion `expand` noch die Funktion 
`factor` an, um einen Ausdruck zu expandieren oder zu faktorisieren.  Daher
kann es zu anderen Ergebnissen kommen, wenn zuvor diese Funktionen angewendet 
werden.


Wird `coeff` auf Listen, Matrizen oder Gleichungen angewendet, wird die
Funktion auf die Elemente oder beide Seiten der Gleichung angewendet.


Siehe auch die Funktion `bothcoef`.


Beispiele:


`coeff` gibt den Koeffizienten von `x^n` des Ausdrucks
*expr* zuruck.



```maxima
(%i1) coeff(b^3*a^3 + b^2*a^2 + b*a + 1, a^3);
                                3
(%o1)                          b
```


`coeff(expr, x^n)` ist aquivalent zu
`coeff(expr, x, n)`.



```maxima
(%i1) coeff(c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z, 3);
(%o1)                         - c
                                 3
(%i2) coeff(c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z^3);
(%o2)                         - c
                                 3
```


`coeff(expr, x, 0)` gibt den Teil des Ausdrucks *expr*
zuruck, der frei von der Variablen *x* ist.



```maxima
(%i1) coeff(a*u + b^2*u^2 + c^3*u^3, b, 0);
                            3  3
(%o1)                      c  u  + a u
```


*x* kann eine einfache Variable, eine indizierte Variable oder ein 
Teilausdruck des Ausdrucks *expr* sein.



```maxima
(%i1) coeff(h^4 - 2*%pi*h^2 + 1, h, 2);
(%o1)                        - 2 %pi
(%i2) coeff(v[1]^4 - 2*%pi*v[1]^2 + 1, v[1], 2);
(%o2)                        - 2 %pi
(%i3) coeff (sin(1+x)*sin(x) + sin(1+x)^3*sin(x)^3, sin(1+x)^3);
                                3
(%o3)                        sin (x)
(%i4) coeff((d - a)^2*(b + c)^3 + (a + b)^4*(c - d), a + b, 4);
(%o4)                         c - d
```


`coeff` wendet die Funktionen `expand` und `factor` nicht an.



```maxima
(%i1) coeff(c*(a + b)^3, a);
(%o1)                           0
(%i2) expand(c*(a + b)^3);
                 3          2        2        3
(%o2)           b  c + 3 a b  c + 3 a  b c + a  c
(%i3) coeff(%, a);
                                2
(%o3)                        3 b  c
(%i4) coeff(b^3*c + 3*a*b^2*c + 3*a^2*b*c + a^3*c, (a + b)^3);
(%o4)                           0
(%i5) factor(b^3*c + 3*a*b^2*c + 3*a^2*b*c + a^3*c);
                                  3
(%o5)                      (b + a)  c
(%i6) coeff(%, (a + b)^3);
(%o6)                           c
```


`coeff` wird bei Listen und Matrizen auf die Elemente und bei Gleichungen
auf die beiden Seiten angewendet.



```maxima
(%i1) coeff([4*a, -3*a, 2*a], a);
(%o1)                      [4, - 3, 2]
(%i2) coeff(matrix ([a*x, b*x], [-c*x, -d*x]), x);
                          [  a    b  ]
(%o2)                     [          ]
                          [ - c  - d ]
(%i3) coeff(a*u - b*v = 7*u + 3*v, u);
(%o3)                         a = 7
```


Die folgende Definition der Funktion `coeff_list` liefert eine Liste mit
den Koeffizienten, die in einem Polynom auftreten.  Neben der Funktion
`coeff` kommt hier die Funktion `hipow` zum Einsatz, um den hochsten
Exponenten zu ermitteln. `rat` und `ratdisrep` werden verwendet, 
um das Polynom zwischenzeitlich in die kanonische Form (CRE) zu bringen.



```maxima
(%i1) b : (x-y)^2;
                                       2
(%o1)                           (x - y)
(%i2) coeff_list(a, x) := (
   a : rat(a),
   reverse( makelist(ratdisrep(coeff(a, x, i)), i,0, hipow(a, x)) ))$

(%i3) coeff_list(b, x);
                                         2
(%o3)                        [1, - 2 y, y ]
```

See also: `bothcoef`, `hipow`, `rat`, `ratdisrep`.

<!-- category: Polynomials -->
<!-- keywords: content -->
<!-- signatures: content(p, x_1, ..., x_n) -->
### Function: content (p, x_1, ..., x_n)

Gibt eine Liste zuruck, deren erstes Element der großte gemeinsame 
Teiler der Koeffizienten des Polynoms *p* in der Variablen *x_n* ist 
und dessen zweites Element das durch den großten gemeinsamen Teiler 
dividierte Polynom ist.  Die anderen Argumente *x_1*, ..., *x_n-1*
haben dieselbe Bedeutung wie fur die Funktion `ratvars`.


Beispiel:



```maxima
(%i1) content(2*x*y + 4*x^2*y^2, y);
                                   2
(%o1)                   [2 x, 2 x y  + y]
```

See also: `ratvars`.

<!-- category: Polynomials -->
<!-- keywords: denom -->
<!-- signatures: denom(expr) -->
### Function: denom (expr)

Gibt den Nenner des Ausdrucks *expr* zuruck, wenn dieser ein
Quotient ist.  Ist der Ausdruck *expr* kein Quotient, wird `1`
zuruckgegeben.  Fur `%e^-x`, `2^-x` und `x/2` hngt das
Verhalten von den Optionen `%edispflag`, `exptdispflag` und
`pfeformat` ab.


Die Funktion `denom` wertet das Argument aus.  Siehe auch die Funktionen
`num` und `num_denom`.


Beispiel:



```maxima
(%i1) denom(x^2/(x+1));
(%o1)                         x + 1
```

See also: `%edispflag`, `exptdispflag`, `pfeformat`, `num`, `num_denom`.

<!-- category: Polynomials -->
<!-- keywords: divide -->
<!-- signatures: divide(p_1, p_2, x_1, ..., x_n) -->
### Function: divide (p_1, p_2, x_1, ..., x_n)

Berechnet den Quotienten und den Rest der Division des Polynom *p_1* durch
das Polynom *p_2* fur die Variable *x_n*.  Die anderen Argumente
*x_1*, ..., *x_n-1* haben dieselbe Bedeutung wie fur die Funktion
`ratvars`.  Das Ergebnis ist eine Liste, wobei das erste Element der
Quotient und das zweite Element der Rest ist.


Die Argumente der Funktion `divide` konnen auch ganze Zahlen sein.


Siehe auch die Funktionen `quotient` und `remainder`, die jeweils
den Quotienten und den Rest der Polynomdivision zuruckgegeben.


Beispiele:


Im zweiten Beispiel ist `y` die Hauptvariable des Ausdrucks.



```maxima
(%i1) divide (x + y, x - y, x);
(%o1)                       [1, 2 y]
(%i2) divide (x + y, x - y);
(%o2)                      [- 1, 2 x]
```



Ein Beispiel fur zwei Polynome in zwei Variablen.



```maxima
(%i1) poly1 : sum(x^k*y^(6-k), k, 1, 5);
                  5    2  4    3  3    4  2    5
(%o1)          x y  + x  y  + x  y  + x  y  + x  y
(%i2) poly2 : sum(2*k*x^k*y^(3-k), k, 1, 3);
                          2      2        3
(%o2)                2 x y  + 4 x  y + 6 x
(%i3) divide(poly1, poly2, x);
              3        2      2          5       2  4
           4 y  + 3 x y  + 9 x  y  23 x y  + 16 x  y
(%o3)     [----------------------, ------------------]
                     54                    27
(%i4) expand(first(%)*poly2 + second(%));
                  5    2  4    3  3    4  2    5
(%o4)          x y  + x  y  + x  y  + x  y  + x  y
```

See also: `ratvars`, `quotient`, `remainder`.

<!-- category: Polynomials -->
<!-- keywords: dontfactor -->
<!-- signatures: dontfactor -->
### Variable: dontfactor

Standardwert: `[]`


Der Optionsvariablen `dontfactor` kann eine Liste mit den Variablen
zugewiesen werden, bezuglich der ein Ausdruck nicht faktorisiert werden soll.
Weiterhin wird nicht bezuglich von Variablen faktorisiert, die gemaß
der kanonischen Ordnung der Variablen von geringerer Bedeutung sind als die
Variablen in der Liste `dontfactor`.


Beispiel:


Im zweiten Fall wird das Polynom nicht bezuglich der Variablen *x*
faktorisiert.



```maxima
(%i1) expr:expand((x+1)^3*(y+2)^2);
       3  2      2  2        2    2      3         2
(%o1) x  y  + 3 x  y  + 3 x y  + y  + 4 x  y + 12 x  y + 12 x y
                                             3       2
                                  + 4 y + 4 x  + 12 x  + 12 x + 4
(%i2) factor(expr);
                               3        2
(%o2)                   (x + 1)  (y + 2)
(%i3) dontfactor:[x];
(%o3)                          [x]
(%i4) factor(expr);
                   3      2                   2
(%o4)            (x  + 3 x  + 3 x + 1) (y + 2)
```

<!-- category: Polynomials -->
<!-- keywords: eliminate -->
<!-- signatures: eliminate([eqn_1, ..., eqn_n], [x_1, ..., x_k]) -->
### Function: eliminate ([eqn_1, ..., eqn_n], [x_1, ..., x_k])

Wendet ein Subresultanten-Verfahren an, um die Variablen *x_1*, ..., 
*x_k* aus den Gleichungen *eqn_1*, ..., *eqn_n* zu eliminieren.
Die Ruckgabe ist ein Gleichungssystem mit `n - k`
Gleichungen, wobei die *k*-Variablen *x_1*, ..., *x_k*
eliminiert sind.


Beispiel:



```maxima
(%i1) eqn1: 2*x^2 + y*x + z;
                                      2
(%o1)                    z + x y + 2 x
(%i2) eqn2: 3*x + 5*y - z - 1;
(%o2)                  - z + 5 y + 3 x - 1
(%i3) eqn3: z^2 + x - y^2 + 5;
                          2    2
(%o3)                    z  - y  + x + 5
(%i4) eliminate([eqn1, eqn2, eqn3], [y,z]);
              2      4      3       2
(%o4)       [x  (45 x  + 3 x  + 11 x  + 81 x + 124)]
```

<!-- category: Polynomials -->
<!-- keywords: ezgcd -->
<!-- signatures: ezgcd(p_1, p_2, p_3, ...) -->
### Function: ezgcd (p_1, p_2, p_3, ...)

Gibt eine Liste zuruck, deren erstes Element der großte gemeinsame
Teiler der Polynome *p_1*, ..., *p_n* ist und deren weitere Elemente
die durch den großten gemeinsamen Teiler dividierten Polynome sind.  Der
großte gemeinsame Teiler wird immer mit dem `ezgcd`-Algorithmus 
bestimmt.


Siehe auch die Funktionen `gcd`, `gcdex` `gcdivide` und
`poly_gcd`.


Beispiel:


Die drei Polynome haben den großten gemeinsamen Teiler `2*x-3`.
Der großte gemeinsame Teiler wird zuerst mit der Funktion `gcd`
berechnet.  Dann wird das Ergebnis der Funktion `ezgcd` gezeigt.



```maxima
(%i1) p1 : 6*x^3-17*x^2+14*x-3;
                        3       2
(%o1)                6 x  - 17 x  + 14 x - 3
(%i2) p2 : 4*x^4-14*x^3+12*x^2+2*x-3;

                    4       3       2
(%o2)            4 x  - 14 x  + 12 x  + 2 x - 3

(%i3) p3 : -8*x^3+14*x^2-x-3;
                          3       2
(%o3)                - 8 x  + 14 x  - x - 3

(%i4) gcd(p1, gcd(p2, p3));
(%o4)                        2 x - 3

(%i5) ezgcd(p1, p2, p3);
                   2               3      2           2
(%o5) [2 x - 3, 3 x  - 4 x + 1, 2 x  - 4 x  + 1, - 4 x  + x + 1]
```

See also: `gcd`, `gcdex`, `gcdivide`, `poly_gcd`.

<!-- category: Polynomials -->
<!-- keywords: facexpand -->
<!-- signatures: facexpand -->
### Variable: facexpand

Standardwert: `true`


Die Optionsvariable `facexpand` kontrolliert, ob die irreduziblen Faktoren
der Faktorisierung mit `factor` in einer expandierten oder in einer
rekursiven (CRE-Form) vorliegen.  Der Standard ist, dass die Faktoren expandiert
werden.

See also: `factor`.

<!-- category: Polynomials -->
<!-- keywords: factor -->
<!-- signatures: factor(expr), factor(expr, p) -->
### Function: factor (expr)

Faktorisiert den Ausdruck *expr*, der eine beliebige Zahl an Variablen 
oder Funktionen enthalten kann, in irreduzible Faktoren uber die ganzen 
Zahlen.  `factor(expr, p` faktorisiert *expr* uber den 
Korper der rationalen Zahlen, der um die Nullstellen des minimalen Polynoms
*p* erweitert ist.




`factor` ruft die Funktion `ifactors` auf, um ganze Zahlen zu 
faktorisieren.





Hat die Optionsvariable `factorflag` den Wert `false`, wird die
Faktorisierung von ganzen Zahlen unterdruckt, die im Nenner einer rationalen
Funktion auftreten.








Der Optionsvariablen `dontfactor` kann eine Liste mit den Variablen
zugewiesen werden, bezuglich der ein Ausdruck nicht faktorisiert werden soll.
Weiterhin wird nicht bezuglich von Variablen faktorisiert, die gemaß
der kanonischen Ordnung der Variablen von geringerer Bedeutung sind als die
Variablen in der Liste `dontfactor`.







Hat die Optionsvariable `savefactors` den Wert `true`, versuchen
einige Funktionen bei der Vereinfachung eine bereits vorhandene Faktorisierung
zu erhalten, um weitere Vereinfachungen zu beschleunigen.






Hat die Optionsvariable `berlefact` den Wert `false`, dann wird der
Kronecker-Al­go­rith­mus fur die Faktorisierung genutzt.  Ansonsten wird
der Berlekamp-Algorithmus genutzt.  Der Standardwert ist `true`.










Hat die Optionsvariable `intfaclim` den Wert `true`, gibt Maxima
die Faktorisierung von ganzen Zahlen auf, wenn keine Faktorisierung durch
Anwendung der Methode der Probedivision und der Pollard-Rho-Methode gefunden
werden konnten.  Hat `intfaclim` den Wert `false`, versucht Maxima
eine ganze Zahl vollstandig zu faktorisieren.  Der Wert der Optionsvariablen
`intfaclim` wird von der Funktion `factor` beachtet.  Mit dem Setzen
von `intfaclim` kann der Nutzer verhindern, dass Maxima beim Versuch sehr
große ganze Zahlen zu faktorisieren, unnotig viel Zeit verbraucht.


Beispiele:



```maxima
(%i1) factor (2^63 - 1);
                    2
(%o1)              7  73 127 337 92737 649657
(%i2) factor (-8*y - 4*x + z^2*(2*y + x));
(%o2)               (2 y + x) (z - 2) (z + 2)
(%i3) -1 - 2*x - x^2 + y^2 + 2*x*y^2 + x^2*y^2;
                2  2        2    2    2
(%o3)          x  y  + 2 x y  + y  - x  - 2 x - 1
(%i4) block ([dontfactor: [x]], factor (%/36/(1 + 2*y + y^2)));
                       2
                     (x  + 2 x + 1) (y - 1)
(%o4)                ----------------------
                           36 (y + 1)
(%i5) factor (1 + %e^(3*x));
                      x         2 x     x
(%o5)              (%e  + 1) (%e    - %e  + 1)
(%i6) factor (1 + x^4, a^2 - 2);
                    2              2
(%o6)             (x  - a x + 1) (x  + a x + 1)
(%i7) factor (-y^2*z^2 - x*z^2 + x^2*y^2 + x^3);
                       2
(%o7)              - (y  + x) (z - x) (z + x)
(%i8) (2 + x)/(3 + x)/(b + x)/(c + x)^2;
                             x + 2
(%o8)               ------------------------
                                           2
                    (x + 3) (x + b) (x + c)
(%i9) ratsimp (%);

                4                  3
(%o9) (x + 2)/(x  + (2 c + b + 3) x

     2                       2             2                   2
 + (c  + (2 b + 6) c + 3 b) x  + ((b + 3) c  + 6 b c) x + 3 b c )

(%i10) partfrac (%, x);
           2                   4                3
(%o10) - (c  - 4 c - b + 6)/((c  + (- 2 b - 6) c

     2              2         2                2
 + (b  + 12 b + 9) c  + (- 6 b  - 18 b) c + 9 b ) (x + c))

                 c - 2
 - ---------------------------------
     2                             2
   (c  + (- b - 3) c + 3 b) (x + c)


                         b - 2
 + -------------------------------------------------
             2             2       3      2
   ((b - 3) c  + (6 b - 2 b ) c + b  - 3 b ) (x + b)


                         1
 - ----------------------------------------------
             2
   ((b - 3) c  + (18 - 6 b) c + 9 b - 27) (x + 3)
(%i11) map ('factor, %);
              2
             c  - 4 c - b + 6                 c - 2
(%o11) - ------------------------- - ------------------------
                2        2                                  2
         (c - 3)  (c - b)  (x + c)   (c - 3) (c - b) (x + c)

                       b - 2                        1
            + ------------------------ - ------------------------
                             2                          2
              (b - 3) (c - b)  (x + b)   (b - 3) (c - 3)  (x + 3)
(%i12) ratsimp ((x^5 - 1)/(x - 1));
                       4    3    2
(%o12)                x  + x  + x  + x + 1
(%i13) subst (a, x, %);
                       4    3    2
(%o13)                a  + a  + a  + a + 1
(%i14) factor (%th(2), %);
                       2        3        3    2
(%o14)   (x - a) (x - a ) (x - a ) (x + a  + a  + a + 1)
(%i15) factor (1 + x^12);
                       4        8    4
(%o15)               (x  + 1) (x  - x  + 1)
(%i16) factor (1 + x^99);
                 2            6    3
(%o16) (x + 1) (x  - x + 1) (x  - x  + 1)

   10    9    8    7    6    5    4    3    2
 (x   - x  + x  - x  + x  - x  + x  - x  + x  - x + 1)

   20    19    17    16    14    13    11    10    9    7    6
 (x   + x   - x   - x   + x   + x   - x   - x   - x  + x  + x

    4    3            60    57    51    48    42    39    33
 - x  - x  + x + 1) (x   + x   - x   - x   + x   + x   - x

    30    27    21    18    12    9    3
 - x   - x   + x   + x   - x   - x  + x  + 1)
```


Das Polynom `x^4+1` lasst sich nicht uber den Korper der ganzen
Zahlen faktorisieren.  Wird der Korper um das minimale Polynom `a^2+1`
erweitert, ist die Faktorisierung moglich.  Die Nullstellen des minimalen
Polynoms sind die imaginare Einheit `%i` und `-%i`.  Das Ergebnis
entspricht der Faktorisierung mit der Funktion `gfactor`.



```maxima
(%i1) factor(x^4+1);
                              4
(%o1)                        x  + 1
(%i2) factor(x^4+1, a^2+1);
                          2        2
(%o2)                   (x  - a) (x  + a)
(%i3) gfactor(x^4+1);
                         2         2
(%o3)                  (x  - %i) (x  + %i)
```

See also: `ifactors`, `factorflag`, `dontfactor`, `savefactors`, `berlefact`, `intfaclim`, `gfactor`.

<!-- category: Polynomials -->
<!-- keywords: factorflag -->
<!-- signatures: factorflag -->
### Variable: factorflag

Standardwert: `false`


Hat die Optionsvariable `factorflag` den Wert `false`, wird die
Faktorisierung von ganzen Zahlen unterdruckt, die im Nenner einer rationalen
Funktion auftreten.


Beispiel:



```maxima
(%i1) factorflag:false;
(%o1)                         false
(%i2) factor(1/6*(x^2+2*x+1));

                                   2
                            (x + 1)
(%o2)                       --------
                               6

(%i3) factorflag:true;
(%o3)                         true
(%i4) factor(1/6*(x^2+2*x+1));
                                   2
                            (x + 1)
(%o4)                       --------
                              2 3
```

<!-- category: Polynomials -->
<!-- keywords: factorout -->
<!-- signatures: factorout(expr, x_1, x_2, ...) -->
### Function: factorout (expr, x_1, x_2, ...)

Gruppiert eine Summe *expr* in eine Summe mit Termen der Form
`f(x_1, x_2, ...) * g`, wobei `g` ein gemeinsamer Faktor
des Polynoms `f` ist.


Beispiele:


Das Polynom wird zuerst nach der Variablen *x*, dann nach *y* und 
zuletzt nach beiden Variablen faktorisiert.



```maxima
(%i1) factorout(2*a*x^2+a*x+a+a*y, x);
                                 2
(%o1)                a y + a (2 x  + x + 1)
(%i2) factorout(2*a*x^2+a*x+a+a*y, y);
                                     2
(%o2)               a (y + 1) + 2 a x  + a x
(%i3) factorout(2*a*x^2+a*x+a+a*y, y, x);
                                2
(%o3)                 a (y + 2 x  + x + 1)
```

<!-- category: Polynomials -->
<!-- keywords: factorsum -->
<!-- signatures: factorsum(expr) -->
### Function: factorsum (expr)

Versucht Terme in *expr* so zu gruppieren, dass die Teilsummen
faktorisierbar sind.  `factorsum` kann zum Beispiel das expandierte
Polynom `expand ((x + y)^2 + (z + w)^2)` wieder herstellen, nicht jedoch
das expandierte Polynom `expand ((x + 1)^2 + (x + y)^2)`, da die Terme
gemeinsame Variablen enthalten.


Beispiele:



```maxima
(%i1) expand ((x + 1)*((u + v)^2 + a*(w + z)^2));
           2      2                            2      2
(%o1) a x z  + a z  + 2 a w x z + 2 a w z + a w  x + v  x

                                     2        2    2            2
                        + 2 u v x + u  x + a w  + v  + 2 u v + u
(%i2) factorsum(%);
                                   2          2
(%o2)            (x + 1) (a (z + w)  + (v + u) )
```

<!-- category: Polynomials -->
<!-- keywords: fasttimes -->
<!-- signatures: fasttimes(p_1, p_2) -->
### Function: fasttimes (p_1, p_2)

Fuhrt eine schnelle Multiplikation der Polynome *p_1* und *p_2* aus
und gibt das Ergebnis zuruck.  Der Algorithmus ist von Vorteil, wenn die
Polynome mehrere Variablen haben und die Koeffizienten dicht besetzt sind.
Sind `n_1` und `n_2` jeweils der Grad der Polynome *p_1* und
*p_2*, dann benotigt die schnelle Multiplikation
`max(n_1, n_2)^1.585` Multiplikationen.

<!-- category: Polynomials -->
<!-- keywords: fullratsimp -->
<!-- signatures: fullratsimp(expr), fullratsimp(expr, x_1, ..., x_n) -->
### Function: fullratsimp (expr)

Die Funktion `fullratsimp` wendet die Funktion `ratsimp` auf das
Argument *expr* solange wiederholt an, bis sich das Ergebnis nicht mehr
andert.  Nach jeder Anwendung von `ratsimp` wird der Ausdruck
zusatzlich vereinfacht.


Sind nicht-rationale Ausdrucke in einem Ausdruck enthalten, kann der Ausdruck
moglicherweise mit einem Aufruf von `ratsimp` nicht vollstandig
vereinfacht werden.  Dann kann der mehrfache Aufruf von `ratsimp` zu einem
besser vereinfachten Resultat fuhren.  Die Funktion `fullratsimp` ist
fur solche Falle gedacht.


Die weiteren Argumente *x_1*, ..., *x_n* entsprechen denen der
Funktionen `ratsimp` und `rat`.


Beispiele:



```maxima
(%i1) expr: (x^(a/2) + 1)^2*(x^(a/2) - 1)^2/(x^a - 1);
                       a/2     2   a/2     2
                     (x    - 1)  (x    + 1)
(%o1)                -----------------------
                              a
                             x  - 1
(%i2) ratsimp (expr);
                          2 a      a
                         x    - 2 x  + 1
(%o2)                    ---------------
                              a
                             x  - 1
(%i3) fullratsimp (expr);
                              a
(%o3)                        x  - 1
(%i4) rat (expr);

                       a/2 4       a/2 2
                     (x   )  - 2 (x   )  + 1
(%o4)/R/             -----------------------
                              a
                             x  - 1
```

See also: `ratsimp`, `rat`.

<!-- category: Polynomials -->
<!-- keywords: fullratsubst -->
<!-- signatures: fullratsubst(a, b, c) -->
### Function: fullratsubst (a, b, c)

Entspricht der Funktion `ratsubst` mit dem Unterschied, dass die Funktion
solange rekursiv ausgefuhrt wird, bis sich das Ergebnis nicht mehr andert.
Diese Funktion kann nutzlich sein, wenn der Ausdruck, der eingesetzt wird,
und der zu ersetzende Ausdruck mehrere Variablen gemeinsam haben.


`fullratsubst` akzeptiert auch Argumente im Format der Funktion
`lratsubst`.  Das erste Argument kann also auch eine einzelne oder eine
Liste von Gleichungen sein.  Das zweite Argument ist in diesem Fall der
Ausdruck in dem die Ersetzungen durchgefuhrt werden.


Mit dem Kommando `load("lrats")` werden die Funktionen `fullratsubst`
und `lratsubst` geladen.


Beispiele:



```maxima
(%i1) load ("lrats")$
```





`subst` kann mehrfache Substitutionen ausfuhren.  Die Funktion
`lratsubst` funktioniert analog zu der Funktion `subst`.



```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```





Ist nur eine Substitution auszufuhren, kann diese als eine einzelne Gleichung
angegeben werden.



```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```





`fullratsubst` ist aquivalent zur Funktion `ratsubst` mit dem
Unterschied, dass die Funktion solange rekursiv angewendet wird, bis sich das
Ergebnis nicht mehr andert.



```maxima
(%i5) ratsubst (b*a, a^2, a^3);
                               2
(%o5)                         a  b
(%i6) fullratsubst (b*a, a^2, a^3);

                                 2
(%o6)                         a b
```





`fullratsubst` akzeptiert auch eine Liste mit Gleichungen oder eine
Gleichung als erstes Argument.



```maxima
(%i7) fullratsubst ([a^2 = b, b^2 = c, c^2 = a], a^3*b*c);
(%o7)                           b
(%i8) fullratsubst (a^2 = b*a, a^3);
                                 2
(%o8)                         a b
```




`fullratsubst` kann zu einer unendlichen Rekursion fuhren.



```maxima
(%i9) errcatch (fullratsubst (b*a^2, a^2, a^3));

*** - Lisp stack overflow. RESET
```

See also: `ratsubst`, `lratsubst`, `subst`.

<!-- category: Polynomials -->
<!-- keywords: gcd -->
<!-- signatures: gcd(p_1, p_2, x_1, ...) -->
### Function: gcd (p_1, p_2, x_1, ...)

Gibt den großten gemeinsamen Teiler der Polynome *p_1* und *p_2*
zuruck.  Die Argumente *x_1*, ... sind optional und haben dieselbe
Bedeutung wie fur die Funktion `ratvars`.  Die Optionsvariable 
`gcd` kontrolliert, welcher Algorithmus verwendet wird und kann die
folgenden Werte annehmen:



**ez** — ezgcd-Alogrithmus
**subres** — Subresultanten-Algorithmus
**red** — Reduzierter modularer Algorithmus
**spmod** — Modularer Algorithmus
**false** — kein Algorithmus, die Ruckgabe ist immer 1







Siehe auch die `ezgcd`, `gcdex`, `gcdivide`, und
`poly_gcd`.


Beispiele:



```maxima
(%i1) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i3) gcd(p1, p2);
                            2
(%o3)                    6 x  + 13 x + 6
(%i4) p1/gcd(p1, p2), ratsimp;
(%o4)                         x + 1
(%i5) p2/gcd(p1, p2), ratsimp;
                              3
(%o5)                        x  + x
```






Die Funktion `ezgcd` gibt als Ergebnis eine Liste zuruck, die als erstes
Element den großten gemeinsamen Teiler und als weitere Elemente die durch
den großten gemeinsamen Teiler dividierten Polynome enthalt.



```maxima
(%i6) ezgcd(p1, p2);
                    2                     3
(%o6)           [6 x  + 13 x + 6, x + 1, x  + x]
```

See also: `ratvars`, `ezgcd`, `gcdex`, `gcdivide`, `poly_gcd`.

<!-- category: Polynomials -->
<!-- keywords: gcdex -->
<!-- signatures: gcdex(p_1, p_2), gcdex(p_1, p_2, x) -->
### Function: gcdex (p_1, p_2)

Wendet den erweiterten Euklidischen Algorithmus fur die beiden Polynome
*p_1* und *p_2* an und gibt eine Liste `[s, t, u]` mit den
Parametern *u*, *s* und *t* als Ergebnis zuruck.  Der Parameter
*u* ist der großte gemeinsame Teiler der Polynome.  Die Parameter
*s* und *t* sind die Bezoutkoeffizienten, so dass gilt
`u = s * p_1 + t * p_2`.


Die Ruckgabe der Funktion `gcdex` ist in der CRE-Form.








Siehe auch die Funktionen `ezgcd`, `gcd` und `gcdivide`.


Die Argumente *f* und *g* konnen ganze Zahlen sein.  In diesem Falle
wird die Funktion `igcdex` von der Funktion `gcdex` aufgerufen.


Siehe auch die Funktionen `ezgcd`, `gcd`,
`gcdivide` und `poly_gcd`.


Beispiel:



```maxima
(%i1) gcdex (x^2 + 1, x^3 + 4);
                       2
                      x  + 4 x - 1  x + 4
(%o1)/R/           [- ------------, -----, 1]
                           17        17
(%i2) % . [x^2 + 1, x^3 + 4, -1];
(%o2)/R/                        0
```


Im folgenden Beispiel ist die unabhangige Variable explizit als *x*
angegeben.  Ohne diese Angabe ist *y* die unabhangige Variable.



```maxima
(%i1) gcdex (x*(y + 1), y^2 - 1, x);
                               1
(%o1)/R/                 [0, ------, 1]
                              2
                             y  - 1
```

See also: `ezgcd`, `gcd`, `gcdivide`, `igcdex`, `poly_gcd`.

<!-- category: Polynomials -->
<!-- keywords: gcfactor -->
<!-- signatures: gcfactor(g) -->
### Function: gcfactor (g)

Faktorisiert die Gaußsche Zahl *g* uber die Gaußsche Zahlen.  Eine
Gaußsche Zahl `g` ist durch `g = a + b*%i` gegeben, wobei `a`
und `b` ganze Zahlen sind.  Die Faktoren werden so normalisiert, dass
*a* und *b* nicht negativ sind.


Beispiele:



```maxima
(%i1) gcfactor(5);
(%o1)               - %i (1 + 2 %i) (2 + %i)
(%i2) expand(%);
(%o2)                           5
(%i3) gcfactor(5+%i);
(%o3)               - %i (1 + %i) (2 + 3 %i)
(%i4) expand(%);
(%o4)                        %i + 5
```

<!-- category: Polynomials -->
<!-- keywords: gfactor -->
<!-- signatures: gfactor(expr) -->
### Function: gfactor (expr)

Faktorisiert das Polynom *expr* uber die Gaußschen Zahlen.  Das ist
die Faktorisierung uber den Korper der ganzen Zahlen, der um das Element
*%i* erweitert ist.


Die Faktorisierung der Funktion `gfactor` ist aquivalent zu
`factor(expr), a^2+1)` mit dem minimalen Polynom
`a^2+1`, das die Nullstelle `%i` hat.  Siehe auch
`factor`.


Beispiel:



```maxima
(%i1) gfactor(x^4 - 1);
(%o1)           (x - 1) (x + 1) (x - %i) (x + %i)
(%i2) factor(x^4 - 1, a^2+1);
(%o2)            (x - 1) (x + 1) (x - a) (x + a)
```

See also: `factor`.

<!-- category: Polynomials -->
<!-- keywords: gfactorsum -->
<!-- signatures: gfactorsum(expr) -->
### Function: gfactorsum (expr)

Entspricht der Funktion `factorsum` mit den Unterschied, dass anstatt der
Funktion `factor` die Funktion `gfactor` angewendet wird, um den
Ausdruck *expr* zu faktorisieren.

See also: `factorsum`, `factor`, `gfactor`.

<!-- category: Polynomials -->
<!-- keywords: hipow -->
<!-- signatures: hipow(expr, x) -->
### Function: hipow (expr, x)

Gibt den großten Exponenten des Arguments *x* zuruck, der im
Ausdruck *expr* auftritt.  Treten symbolische Exponenten auf, wird ein
Ausdruck mit `max` zuruckgegeben.  Ist das Argument *x* nicht im
Ausdruck vorhanden, ist die Ruckgabe `0`.


Die Funktion `hipow` betrachtet keine aquivalenten Ausdrucke.  Daher
konnen die Ausdrucke `expand(expr)` und *expr* ein
verschiedenes Ergebnis haben.


Siehe auch die Funktionen `lopow` und `coeff`.



Beispiele:



```maxima
(%i1) hipow (y^3 * x^2 + x * y^4, x);
(%o1)                           2
(%i2) hipow ((x + y)^5, x);
(%o2)                           1
(%i3) hipow (expand ((x + y)^5), x);
(%o3)                           5
(%i4) hipow ((x + y)^5, x + y);
(%o4)                           5
(%i5) hipow (expand ((x + y)^5), x + y);
(%o5)                           0
(%i1) hipow ((x+y)^2 + (x+y)^a, x+y);
(%o1)                       max(2, a)
```

See also: `lopow`, `coeff`.

<!-- category: Polynomials -->
<!-- keywords: intfaclim -->
<!-- signatures: intfaclim -->
### Variable: intfaclim

Standardwert: `true`










   

   
   




Hat die Optionsvariable `intfaclim` den Wert `true`, gibt Maxima
die Faktorisierung von ganzen Zahlen auf, wenn keine Faktorisierung durch
Anwendung der Methode der Probedivision und der Pollard-Rho-Methode gefunden
werden konnten.


Hat `intfaclim` den Wert `false`, versucht Maxima eine ganze Zahl
vollstandig zu faktorisieren.  `intfaclim` wird von den Funktionen
`divisors`, `divsum` und `totient` auf den Wert `false`
gesetzt.


Der Wert der Optionsvariablen `intfaclim` wird von der Funktion
`factor` beachtet.  Mit dem Setzen von `intfaclim` kann der Nutzer
verhindern, dass Maxima beim Versuch sehr große ganze Zahlen zu
faktorisieren, unnotig viel Zeit verbraucht.

See also: `intfaclim`, `divisors`, `divsum`, `totient`.

<!-- category: Polynomials -->
<!-- keywords: keepfloat -->
<!-- signatures: keepfloat -->
### Variable: keepfloat

Standardwert: `false`










Hat die Optionsvariable `keepfloat` den Wert `true`, werden
Gleitkommazahlen nicht in rationale Zahlen umgewandelt, wenn Ausdrucke mit
Gleitkommazahlen in eine CRE-Form umgewandelt werden.


Die Funktion `solve` und Funktionen, die `solve` aufrufen, beachten
den Wert von `keepfloat` nicht.


Beispiele:



```maxima
(%i1) rat(x/2.0);

rat: replaced 0.5 by 1/2 = 0.5
                                x
(%o1)/R/                        -
                                2
(%i2) rat(x/2.0), keepfloat;
(%o2)/R/                      0.5 x
```




Die Funktion `solve` ignoriert den Wert der Optionsvariablen
`keepfloat`.



```maxima
(%i3) solve(1.0-x,x), keepfloat;

rat: replaced 1.0 by 1/1 = 1.0
(%o3)                        [x = 1]
```

See also: `solve`.

<!-- category: Polynomials -->
<!-- keywords: lopow -->
<!-- signatures: lopow(expr, x) -->
### Function: lopow (expr, x)

Gibt den kleinsten Exponenten von *x* zuruck, der im Ausdruck *expr*
auftritt.  Treten symbolische Exponententen auf, wird ein Ausdruck mit 
`min` zuruckgegeben.  Ist das Argument *x* nicht im
Ausdruck enthalten, ist die Ruckgabe 0.


Die Funktion `lopow` betrachtet keine aquivalenten Ausdrucke.  Daher
konnen die Ausdrucke `expand(expr)` und *expr* ein
verschiedenes Ergebnis haben.


Siehe auch die Funktionen `hipow` und `coeff`.


Beispiele:



```maxima
(%i1) lopow ((x+y)^2 + (x+y)^a, x+y);
(%o1)                       min(a, 2)
```

See also: `hipow`, `coeff`.

<!-- category: Polynomials -->
<!-- keywords: lratsubst -->
<!-- signatures: lratsubst(L, expr) -->
### Function: lratsubst (L, expr)

Ist analog zum Kommando `subst (L, expr)` mit dem Unterschied,
dass anstatt der Funktion `subst` die Funktion `ratsubst` genutzt
wird.









Das erste Argument der Funktion `lratsubst` ist eine Gleichung oder eine
Liste mit Gleichungen, die dem Format der Funktion `subst` entsprechen.
Die Substitutionen werden in der Reihenfolge der Gleichungen der Liste von links
nach rechts ausgefuhrt.


Mit dem Kommando `lrats` werden die Funktionen `fullratsubst` und
`lratsubst` geladen.  Siehe auch die Funktion `fullratsubst`.


Beispiele:



```maxima
(%i1) load ("lrats")$
```





`subst` kann mehrfache Substitutionen ausfuhren.  `lratsubst` ist
analog zu `subst`.



```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```





Soll nur eine Substitution ausgefuhrt werden, kann eine einzelne Gleichung
als erstes Argument angegeben werden.



```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```

See also: `subst`, `ratsubst`, `fullratsubst`.

<!-- category: Polynomials -->
<!-- keywords: modulus -->
<!-- signatures: modulus -->
### Variable: modulus

Standardwert: `false`










   

Hat die Optionsvariable `modulus` eine positive Zahl *p* als Wert,
werden Operationen fur rationale Zahlen, wie von der Funktion `rat` und
verwandte Funktionen, modulo *p* ausgefuhrt.


`n` mod *p* ist definiert als eine ganze Zahl, die fur ungerade
*p* die Werte `[-(p-1)/2, ..., 0, ..., (p-1)/2]` annimmt
und fur gerade *p* die Werte `[-(p/2 - 1), ..., 0, ...., p/2]`, so dass  `a p + k` gleich *n* ist fur
eine ganze Zahl *a*.


   
   




Liegt ein Ausdruck *expr* bereits in einer CRE-Form vor und wird der Wert
der Optionsvariable `modulus` geandert, dann sollte der Ausdruck zum
Beispiel mit dem Kommando `expr: rat (ratdisrep (expr))` zunachst in die
Standardform gebracht werden, um dann erneut in die CRE-Form umgewandelt zu
werden, um korrekte Ergebnisse zu erzielen.








Typischerweise erhalt die Optionsvariable `modulus` eine Primzahl als
Wert.  Erhalt `modulus` eine positive ganze Zahl als Wert, die nicht eine
Primzahl ist, wird die Zuweisung akzeptiert, jedoch eine Warnung ausgegeben.
Wird Null oder eine negative Zahl zugewiesen signalisiert Maxima einen Fehler.


Beispiele:



```maxima
(%i1) modulus:7;
(%o1)                           7
(%i2) polymod([0,1,2,3,4,5,6,7]);
(%o2)            [0, 1, 2, 3, - 3, - 2, - 1, 0]
(%i3) modulus:false;
(%o3)                         false
(%i4) poly:x^6+x^2+1;
                            6    2
(%o4)                      x  + x  + 1
(%i5) factor(poly);
                            6    2
(%o5)                      x  + x  + 1
(%i6) modulus:13;
(%o6)                          13
(%i7) factor(poly);

                      2        4      2
(%o7)               (x  + 6) (x  - 6 x  - 2)

(%i8) polymod(%);
                            6    2
(%o8)                      x  + x  + 1
```

See also: `rat`.

<!-- category: Polynomials -->
<!-- keywords: num -->
<!-- signatures: num(expr) -->
### Function: num (expr)

Gibt den Zahler des Ausdrucks *expr* zuruck, wenn dieser ein
Quotient ist.  Ist der Ausdruck *expr* kein Quotient, wird *expr*
zuruckgegeben.  Fur `%e^-x`, `2^-x` und `x/2` hngt das
Verhalten von den Optionen `%edispflag`, `exptdispflag` und
`pfeformat` ab.


Die Funktion `num` wertet das Argument aus.  Siehe auch die Funktionen
`denom` und `num_denom`.


Beispiel:



```maxima
(%i1) num(x^2/(x+1));
                                2
(%o1)                          x
```

See also: `%edispflag`, `exptdispflag`, `pfeformat`, `denom`, `num_denom`.

<!-- category: Polynomials -->
<!-- keywords: num_denom -->
<!-- signatures: num_denom(expr) -->
### Function: num_denom (expr)

Gibt eine Liste `[num(expr), denom(expr)]` zuruck, jedoch
auf effizientere Weise.


Die Funktion `num_denom` wertet das Argument aus.  Siehe auch die Funktionen
`num` und `denom`.


Beispiel:



```maxima
(%i1) num_denom(x^2/(x+1));
                            2
(%o1)                     [x , x + 1]
(%i2) [n, d] : num_denom(x^2/(x+1))$
(%i3) print("Der Zaehler ist", n, "und der Nenner ist", d)$
                 2
Der Zaehler ist x  und der Nenner ist x + 1
```

See also: `num`, `denom`.

<!-- category: Polynomials -->
<!-- keywords: partfrac -->
<!-- signatures: partfrac(expr, var) -->
### Function: partfrac (expr, var)

Fuhrt fur den Ausdruck *expr* eine vollstandige Partialbruchzerlegung
aus.



```maxima
(%i1) 1/(1+x)^2 - 2/(1+x) + 2/(2+x);
                      2       2        1
(%o1)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
(%i2) ratsimp (%);
                                 x
(%o2)                 - -------------------
                         3      2
                        x  + 4 x  + 5 x + 2
(%i3) partfrac (%, x);
                      2       2        1
(%o3)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
```

<!-- category: Polynomials -->
<!-- keywords: polydecomp -->
<!-- signatures: polydecomp(p, x) -->
### Function: polydecomp (p, x)

Zerlegt das Polynom *p* in der Variablen *x* in Polynome, die
miteinander verkettet das ursprungliche Polynom ergeben.  `polydecomp`
gibt eine Liste `[p_1, ..., p_n]` zuruck, so dass der
folgende Ausdruck gleich dem Polynom *p* ist:



```maxima
lambda ([x], p_1) (lambda ([x], p_2) (... (lambda ([x], p_n) (x))
  ...))
```





Der Grad des Polynoms *p_i* ist großer als 1 fur *i* kleiner
als *n*.




Eine solche Zerlegung ist nicht eindeutig.


Beispiele:



```maxima
(%i1) polydecomp (x^210, x);
                          7   5   3   2
(%o1)                   [x , x , x , x ]
(%i2) p : expand (subst (x^3 - x - 1, x, x^2 - a));
                6      4      3    2
(%o2)          x  - 2 x  - 2 x  + x  + 2 x - a + 1
(%i3) polydecomp (p, x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```





Die folgende Funktion verkettet die Elemente der Liste
`L = [e_1, ..., e_n]` zu einer Funktion in der Variablen *x*.  Diese
Funktion ist die Inverse Operation zu der Funktion `polydecomp`.



```maxima
compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $
```




Anwendung der Funktionen `compose` und `polydecomp`.



```maxima
(%i3) polydecomp (compose ([x^2 - a, x^3 - x - 1], x), x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```







Wahrend  `compose (polydecomp (p, x), x)` immer das
Polynom *p* als Ergebnis hat, hat `polydecomp (compose ([p_1, ..., p_n], x), x)` nicht notwendigerweise das Ergebnis
`[p_1, ..., p_n]`.



```maxima
(%i4) polydecomp (compose ([x^2 + 2*x + 3, x^2], x), x);
                          2       2
(%o4)                   [x  + 2, x  + 1]
(%i5) polydecomp (compose ([x^2 + x + 1, x^2 + x + 1], x), x);

                      2       2
                     x  + 3  x  + 5
(%o5)               [------, ------, 2 x + 1]
                       4       2
```

<!-- category: Polynomials -->
<!-- keywords: polymod -->
<!-- signatures: polymod(p), polymod(p, m) -->
### Function: polymod (p)

Konvertiert das Polynom *p* in eine modulare Darstellung bezuglich
dem aktuellen Modul.  Das Modul ist der Wert der Variablen `modulus`.





`polymod(p, m` konvertiert das Polynom bezuglich dem Modul 
*m*, anstatt dem aktuellen Modul `modulus`.




Siehe auch `modulus`.

See also: `modulus`.

<!-- category: Polynomials -->
<!-- keywords: powers -->
<!-- signatures: powers(expr, x) -->
### Function: powers (expr, x)

Gibt eine Liste mit den Potenzen der Variablen *x* zuruck, die im
Ausdruck *expr* auftreten.


Mit dem Kommando `load("powers")` wird die Funktion geladen.

<!-- category: Polynomials -->
<!-- keywords: quotient -->
<!-- signatures: quotient(p_1, p_2), quotient(p_1, p_2, x_1, ..., x_n) -->
### Function: quotient (p_1, p_2)

Berechnet den Quotienten der Polynome *p_1* und *p_2* fur die Variable
*x_n*.  Die anderen Variablen *x_1*, ..., *x_n-1* haben dieselbe
Bedeutung wie fur die Funktion `ratvars`.


`quotient` gibt das erste Element des Ergebnisses der Funktion
`divide` zuruck.


Siehe auch die Funktion `remainder`.


Beispiel:



```maxima
(%i1) poly1 : x^3-2*x^2-5*x+7;
                        3      2
(%o1)                  x  - 2 x  - 5 x + 7
(%i2) poly2 : x-1;
(%o2)                         x - 1
(%i3) quotient(poly1, poly2, x);
                            2
(%o3)                      x  - x - 6
```

See also: `ratvars`, `divide`, `remainder`.

<!-- category: Polynomials -->
<!-- keywords: radsubstflag -->
<!-- signatures: radsubstflag -->
### Variable: radsubstflag

Standardwert: `false`








Hat `radsubstflag` den Wert `true`, werden Wurzeln von der Funktion
`ratsubst` auch dann substituiert, wenn diese nicht explizit im Ausdruck
enthalten sind.


Beispiel:



```maxima
(%i1) radsubstflag: false$
(%i2) ratsubst (u, sqrt(x), x);
(%o2)                           x
(%i3) radsubstflag: true$
(%i4) ratsubst (u, sqrt(x), x);
                                2
(%o4)                          u
```

See also: `ratsubst`.

<!-- category: Polynomials -->
<!-- keywords: rat -->
<!-- signatures: rat(expr), rat(expr, x_1, ..., x_n) -->
### Function: rat (expr)

Konvertiert einen Ausdruck *expr* in die CRE-Form.  Der Ausdruck wird so 
expandiert und gruppiert, dass alle Terme einen gemeinsamen Nenner haben und
der großte gemeinsame Teiler gekurzt ist.  Weiterhin werden
Gleitkommazahlen in rationale Zahlungen umgewandelt.  Die Toleranz der
Umwandlung wird von der Optionsvariablen `ratepsilon` kontrolliert.  Die
Variablen im Ausdruck werden entsprechend der Funktion `ratvars`
gemaß der angegebenen Argumente *x_1*, ..., *x_n* angeordnet.









`rat` vereinfacht im Allgemeinen keine Ausdrucke bis auf die Addition
`+`, Subtraktion `-`, Multiplikation `*`, Division `/`
und die Exponentiation `^` mit einer ganzen Zahl.  Dagegen fuhrt die
Funktion `ratsimp` auch weitere Vereinfachungen aus.  Variablen und Zahlen
in einer CRE-Form sind nicht identisch mit denen in der Standardform.  Zum
Beispiel hat `rat(x)- x` das Ergebnis `rat(0)`, welches eine 
andere interne Darstellung als `0` hat.


   











Hat die Optionsvariable `ratfac` den Wert `true`, wird ein Ausdruck
von der Funktion `rat` nur teilweise faktorisiert.  Bei der Ausfuhrung
von Operationen wird bleibt der Ausdruck so vollstandig als moglich in
seiner faktorisierten Form, ohne dass eine Faktorisierung ausgefuhrt wird.
Damit kann Rechenzeit eingespart werden.






Hat die Optionsvariable `ratprint` den Wert `false`, werden
Meldungen unterdruckt, wenn eine Gleitkommazahl in eine rationale
umgewandelt wird.





Hat die Optionsvariable `keepfloat` den Wert `true`, werden
Gleitkommazahlen nicht in rationale Zahlen umgewandelt.




Siehe auch die Funktionen `ratexpand` und `ratsimp`, um
Ausdrucke zu vereinfachen, sowie die Funktion `ratdisrep`, um einen
Ausdruck von einer CRE-Form in eine allgemeine Form zu transformieren.


Beispiele:



```maxima
(%i1) ((x - 2*y)^4/(x^2 - 4*y^2)^2 + 1)*(y + a)*(2*y + x) /
      (4*y^2 + x^2);
                                           4
                                  (x - 2 y)
              (y + a) (2 y + x) (------------ + 1)
                                   2      2 2
                                 (x  - 4 y )
(%o1)         ------------------------------------
                              2    2
                           4 y  + x
(%i2) rat (%, y, a, x);

                            2 a + 2 y
(%o2)/R/                    ---------
                             x + 2 y
```

See also: `ratepsilon`, `ratvars`, `ratsimp`, `ratfac`, `ratprint`, `keepfloat`, `ratexpand`, `ratdisrep`.

<!-- category: Polynomials -->
<!-- keywords: ratalgdenom -->
<!-- signatures: ratalgdenom -->
### Variable: ratalgdenom

Standardwert: `true`







Hat die Optionsvariable `ratalgdenom` den Wert `true`, versucht
Maxima den Nenner beim Auftreten von Wurzeln rational zu machen.
`ratalgdenom` wirkt sich nur aus, wenn die Optionsvariable
`algebraic` den Wert `true` hat und der Ausdruck in einer CRE-Form
vorliegt.


Beispiele:



```maxima
(%i1) algebraic:true$

(%i2) ratalgdenom:false$

(%i3) rat(sqrt(3)/sqrt(2));
                             sqrt(3)
(%o3)/R/                     -------
                             sqrt(2)
(%i4) ratalgdenom:true$

(%i5) rat(sqrt(3)/sqrt(2));
                         sqrt(2) sqrt(3)
(%o5)/R/                 ---------------
                                2
(%i6) algebraic:false$

(%i7) rat(sqrt(3)/sqrt(2));
                             sqrt(3)
(%o7)/R/                     -------
                             sqrt(2)
```

See also: `algebraic`.

<!-- category: Polynomials -->
<!-- keywords: ratcoef -->
<!-- signatures: ratcoef(expr, x, n), ratcoef(expr, x) -->
### Function: ratcoef (expr, x, n)

Gibt den Koeffizienten des Ausdrucks `x^n` in dem Argument
*expr* zuruck.  Wenn das Argument *n* nicht angegeben ist, wird
der Wert zu `1` angenommen.






Die Ruckgabe ist frei von der Variablen *x*.  Existiert kein Koeffizient
`x^n` dann ist die Ruckgabe `0`.






   



`ratcoef` expandiert und vereinfacht das Argument *expr*.  Daher kann
`ratcoef` ein anderes Ergebnis als die Funktion `coeff` haben, die
keine Vereinfachungen ausfuhrt.  Daher `ratcoef((x + 1)/y + x, x)` das
Ergebnis `(y + 1)/y` und nicht das Ergebnis `1` wie es von der
Funktion `coeff` zuruckgegeben wird.




   



`ratcoef(expr, x, 0)` gibt eine Summe der Terme zuruck, die
die Variable *x* nicht enthalten.


   




Beispiele:



```maxima
(%i1) s: a*x + b*x + 5$
(%i2) ratcoef (s, a + b);
(%o2)                           x
```

See also: `coeff`.

<!-- category: Polynomials -->
<!-- keywords: ratdenom -->
<!-- signatures: ratdenom(expr) -->
### Function: ratdenom (expr)

Gibt den Nenner des Argumentes *expr* zuruck.  `ratdenom` wandelt
den Ausdruck zuerst in eine CRE-Form um und gibt das Ergebnis in einer 
CRE-Form zuruck.


Das Argument *expr* wird von der Funktion `rat` in eine CRE-Form
gebracht, falls *expr* nicht bereits in einer CRE-Form vorliegt.  Diese
Transformation kann den Ausdruck *expr* verandern, da alle Terme uber
einen gemeinsamen Nenner zusammengefasst werden.


Die Funktion `denom` ist vergleichbar.  `denom` wandelt den Ausdruck
jedoch nicht eine CRE-Form um und hat als Ergebnis einen Ausdruck in der
Standardform.  Daher konnen sich die Ergebnisse von `ratdenom` und 
`denom` voneinander unterscheiden.


Beispiel:



```maxima
(%i1) expr: expand((x^2+2*x+3)/(x-1));

                        2
                       x       2 x      3
(%o1)                 ----- + ----- + -----
                      x - 1   x - 1   x - 1

(%i2) ratdenom(expr);
(%o2)/R/                      x - 1
(%i3) denom(expr);
(%o3)                           1
```

See also: `rat`, `denom`.

<!-- category: Polynomials -->
<!-- keywords: ratdenomdivide -->
<!-- signatures: ratdenomdivide -->
### Variable: ratdenomdivide

Standardwert: `true`









Hat die Optionsvariable `ratdenomdivide` den Wert `true`, expandiert
die Funktion `ratexpand` einen Quotienten der im Zahler eine Summe hat,
in eine Summe der Quotienten.  Ansonsten werden die Terme uber einen
gemeinsamen Nenner zusammengefasst.


Beispiele:



```maxima
(%i1) expr: (x^2 + x + 1)/(y^2 + 7);
                            2
                           x  + x + 1
(%o1)                      ----------
                              2
                             y  + 7
(%i2) ratdenomdivide: true$
(%i3) ratexpand (expr);
                       2
                      x        x        1
(%o3)               ------ + ------ + ------
                     2        2        2
                    y  + 7   y  + 7   y  + 7
(%i4) ratdenomdivide: false$
(%i5) ratexpand (expr);
                            2
                           x  + x + 1
(%o5)                      ----------
                              2
                             y  + 7
(%i6) expr2: a^2/(b^2 + 3) + b/(b^2 + 3);

                                     2
                           b        a
(%o6)                    ------ + ------
                          2        2
                         b  + 3   b  + 3

(%i7) ratexpand (expr2);
                                  2
                             b + a
(%o7)                        ------
                              2
                             b  + 3
```

See also: `ratexpand`.

<!-- category: Polynomials -->
<!-- keywords: ratdiff -->
<!-- signatures: ratdiff(expr, x) -->
### Function: ratdiff (expr, x)

Differenziert einen rationalen Ausdruck *expr* nach der Variablen *x*.
*expr* muss eine rationale Funktion oder ein Polynom in der Variablen
*x* sein.  Das Argument *x* kann ein Teilausdruck des Argumentes
*expr* sein.






Das Ergebnis ist aquivalent zum Ergebnis der Funktion `diff`,
kann aber eine andere Form haben.  Fur rationale Funktionen kann die
Funktion `ratdiff` schneller sein.





`ratdiff` gibt das Ergebnis in einer CRE-Form zuruck, wenn das Argument
in einer CRE-Form vorliegt.  Ansonsten ist das Ergebnis in der Standardform.





`ratdiff` beachtet nur die Abhangigkeit des Ausdrucks von der Variablen
*x*.  Abhangigkeiten die mit der Funktion `depends` definiert werden,
werden von der Funktion `ratdiff` ignoriert.








Beispiele:



```maxima
(%i1) expr: (4*x^3 + 10*x - 11)/(x^5 + 5);
                           3
                        4 x  + 10 x - 11
(%o1)                   ----------------
                              5
                             x  + 5
(%i2) ratdiff (expr, x);
                    7       5       4       2
                 8 x  + 40 x  - 55 x  - 60 x  - 50
(%o2)          - ---------------------------------
                          10       5
                         x   + 10 x  + 25
(%i3) expr: f(x)^3 - f(x)^2 + 7;
                         3       2
(%o3)                   f (x) - f (x) + 7
(%i4) ratdiff (expr, f(x));
                           2
(%o4)                   3 f (x) - 2 f(x)
(%i5) expr: (a + b)^3 + (a + b)^2;
                              3          2
(%o5)                  (b + a)  + (b + a)
(%i6) ratdiff (expr, a + b);

                    2                    2
(%o6)            3 b  + (6 a + 2) b + 3 a  + 2 a
```

See also: `diff`, `depends`.

<!-- category: Polynomials -->
<!-- keywords: ratdisrep -->
<!-- signatures: ratdisrep(expr) -->
### Function: ratdisrep (expr)

Gibt das Argument *expr* als einen allgemeinen Ausdruck zuruck.  Ist
*expr* bereits ein allgemeiner Ausdruck, wird dieser unverandert
zuruckgegeben.







   



Im Allgemeinen wird die Funktion `ratdisrep` aufgerufen, um einen
Ausdruck von der CRE-Form in einen allgemeinen Ausdruck umzuwandeln.




Siehe auch die Funktion `totaldisrep`.

See also: `totaldisrep`.

<!-- category: Polynomials -->
<!-- keywords: ratexpand -->
<!-- signatures: ratexpand(expr) -->
### Function: ratexpand (expr)

Expandiert das Argument *expr* indem Produkte und Potenzen von Summen
ausmultipliziert, Bruche uber einen gemeinsamen Nenner dargestellt werden
und der großte gemeinsamen Teiler heraus gekurzt wird.  Ist der Zahler
eine Summe, wird er in seine Terme aufgespalten, die jeweils durch den Nenner
dividiert werden.





Die Ruckgabe der Funktion `ratexpand` ist ein allgemeiner Ausdruck, auch
wenn das Argument *expr* ein Ausdruck in der CRE-Form ist.


   









Die Optionsvariable `ratexpand` kontrolliert die Vereinfachung der Funktion
`ratsimp`.  Hat `ratexpand` den Wert `true`, wird ein Ausdruck
vollstandig ausmultipliziert. Ist der Wert `false`, wird der Ausdruck
nur bezuglich der Hauptvariablen ausmultipliziert.  Zum Beispiel hat 
`ratsimp((x+1)*(y+1))` das Ergebnis `x y + y + x + 1`, wenn
`ratexpand` den Wert `true` hat, ansonsten ist das Ergebnis
`(x + 1) y + x + 1`.  Siehe auch die Funktion `ratsimp`.








Hat die Optionsvariable `ratdenomdivide` den Wert `true`, expandiert
die Funktion `ratexpand` einen Quotienten der im Zahler eine Summe hat,
in eine Summe der Quotienten.  Ansonsten werden die Terme uber einen
gemeinsamen Nenner zusammengefasst.






Hat die Optionsvariable `keepfloat` den Wert `true`, werden
Gleitkommazahlen im Argument *expr* nicht in rationale Zahlen umgewandelt,
wenn der Ausdruck in eine CRE-Form umgewandelt wird.


Beispiele:



```maxima
(%i1) ratexpand ((2*x - 3*y)^3);
                     3         2       2        3
(%o1)          - 27 y  + 54 x y  - 36 x  y + 8 x
(%i2) expr: (x - 1)/(x + 1)^2 + 1/(x - 1);

                         x - 1       1
(%o2)                   -------- + -----
                               2   x - 1
                        (x + 1)

(%i3) expand (expr);
                    x              1           1
(%o3)          ------------ - ------------ + -----
                2              2             x - 1
               x  + 2 x + 1   x  + 2 x + 1
(%i4) ratexpand (expr);
                        2
                     2 x                 2
(%o4)           --------------- + ---------------
                 3    2            3    2
                x  + x  - x - 1   x  + x  - x - 1
```

See also: `ratsimp`, `ratdenomdivide`, `ratexpand`, `keepfloat`.

<!-- category: Polynomials -->
<!-- keywords: ratfac -->
<!-- signatures: ratfac -->
### Variable: ratfac

Standardwert: `false`














Hat die Optionsvariable `ratfac` den Wert `true`, werden Ausdrucke
in einer CRE-Form nur teilweise faktorisiert.  Bei der Ausfuhrung
von Operationen bleibt der Ausdruck so vollstandig als moglich in
seiner faktorisierten Form, ohne dass eine Faktorisierung mit der Funktion
`factor` ausgefuhrt wird.  Auf diese Weise kann Rechenzeit eingespart
werden.














Der `ratweight`-Mechanismus ist nicht kompatibel mit dem Setzen der
Variablen `ratfac`.

See also: `factor`, `ratweight`.

<!-- category: Polynomials -->
<!-- keywords: ratnumer -->
<!-- signatures: ratnumer(expr) -->
### Function: ratnumer (expr)

Gibt den Zahler des Argumentes *expr* zuruck.  `ratnumer` wandelt
den Ausdruck zuerst in eine CRE-Form um und gibt das Ergebnis in einer 
CRE-Form zuruck.


   





Das Argument *expr* wird von der Funktion `rat` in eine CRE-Form
gebracht, falls *expr* nicht bereits in einer CRE-Form vorliegt.  Diese
Transformation kann den Ausdruck *expr* verandern, da alle Terme uber
einen gemeinsamen Nenner zusammengefasst werden.







Die Funktion `num` ist vergleichbar.  `num` wandelt den Ausdruck
jedoch nicht eine CRE-Form um und hat als Ergebnis einen Ausdruck in der
Standardform.  Daher konnen sich die Ergebnisse von `ratnumer` und 
`num` voneinander unterscheiden.

See also: `rat`, `num`.

<!-- category: Polynomials -->
<!-- keywords: ratp -->
<!-- signatures: ratp(expr) -->
### Function: ratp (expr)

Gibt das Ergebnis `true` zuruck, wenn das Argument *expr* in einer
CRE-Form oder einer erweiterten CRE-Form vorliegt.





CRE-Formen werden von der Funktion `rat` und verwandten Funktionen erzeugt.
Erweiterte CRE-Formen werden von der Funktion `taylor` und verwandten
Funktionen erzeugt.

See also: `rat`, `taylor`.

<!-- category: Polynomials -->
<!-- keywords: ratprint -->
<!-- signatures: ratprint -->
### Variable: ratprint

Standardwert: `true`






Hat die Optionsvariable `ratprint` den Wert `true`, gibt Maxima eine
Meldung aus, wenn eine Gleitkommazahl in eine rationale Zahl umgewandelt wird.


Beispiel:



```maxima
(%i1) ratprint:true;
(%o1)                         true
(%i2) rat(0.75*x);

rat: replaced 0.75 by 3/4 = 0.75
                               3 x
(%o2)/R/                       ---
                                4
(%i3) ratprint:false;
(%o3)                         false
(%i4) rat(0.75*x);
                               3 x
(%o4)/R/                       ---
                                4
```

<!-- category: Polynomials -->
<!-- keywords: ratsimp -->
<!-- signatures: ratsimp(expr), ratsimp(expr, x_1, ..., x_n) -->
### Function: ratsimp (expr)

Vereinfacht den Ausdruck *expr* und alle Teilausdrucke, einschließlich
der nicht rationalen Anteile.  Das Ergebnis ist ein Quotient aus zwei Polynomen
in einer rekursiven Form.  In der rekursiven Form ist das Polynom nach der
Hauptvariablen vollstandig ausmultipliziert und ein Polynom in allen anderen
Variablen.  Variable konnen auch nicht-rationale Ausdrucke wie
`sin(x^2 + 1)` sein.






`ratsimp(expr, x_1, ..., x_n)` vereinfacht einen Ausdruck
mit einer Ordnung der Variablen wie sie von der Funktion `ratvars`
definiert wird.





Hat die Optionsvariable `ratsimpexpons` den Wert `true`, wird
`ratsimp` auch auf die Exponenten von Ausdrucke angewendet.






Siehe auch die Funktion `ratexpand`.  Die Funktion `ratsimp` wird
auch von einigen Schaltern kontrolliert, die Einfluss auf `ratexpand`
haben.


Beispiele:



```maxima
(%i1) sin (x/(x^2 + x)) = exp ((log(x) + 1)^2 - log(x)^2);
                                         2      2
                   x         (log(x) + 1)  - log (x)
(%o1)        sin(------) = %e
                  2
                 x  + x
(%i2) ratsimp (%);
                             1          2
(%o2)                  sin(-----) = %e x
                           x + 1
(%i3) ((x - 1)^(3/2) - (x + 1)*sqrt(x - 1))/sqrt((x - 1)*(x + 1));

                       3/2
                (x - 1)    - sqrt(x - 1) (x + 1)
(%o3)           --------------------------------
                     sqrt((x - 1) (x + 1))

(%i4) ratsimp (%);

                           2 sqrt(x - 1)
(%o4)                    - -------------
                                 2
                           sqrt(x  - 1)

(%i5) x^(a + 1/a), ratsimpexpons: true;
                               2
                              a  + 1
                              ------
                                a
(%o5)                        x
```

See also: `ratvars`, `ratsimpexpons`, `ratexpand`.

<!-- category: Polynomials -->
<!-- keywords: ratsimpexpons -->
<!-- signatures: ratsimpexpons -->
### Variable: ratsimpexpons

Standardwert: `false`





Hat die Optionsvariable `ratsimpexpons` den Wert `true`, wird
`ratsimp` auch auf die Exponenten von Ausdrucke angewendet.


Beispiel:



```maxima
(%i1) expr: x^(a+1/a);
                             a + 1/a
(%o1)                       x
(%i2) ratsimpexpons: false;
(%o2)                         false
(%i3) ratsimp(expr);
                             a + 1/a
(%o3)                       x
(%i4) ratsimpexpons: true;
(%o4)                         true
(%i5) ratsimp(expr);
                               2
                              a  + 1
                              ------
                                a
(%o5)                        x
```

<!-- category: Polynomials -->
<!-- keywords: ratsubst -->
<!-- signatures: ratsubst(a, b, c) -->
### Function: ratsubst (a, b, c)

Substituiert *a* fur *b* in den Ausdruck *c* und gibt das Ergebnis
der Substitution zuruck.


   





Im Unterschied zu `subst` kann `ratsubst` auch Teilausdrucke im
Ausdruck *c* substituieren.  So hat `subst(a, x + y, x + y + z)` das
Ergebnis `x + y + z` und `ratsubst` das Ergebnis `z + a`.






Hat `radsubstflag` den Wert `true`, werden Wurzeln von der Funktion
`ratsubst` auch dann substituiert, wenn diese nicht explizit im Ausdruck
enthalten sind.


Beispiel:



```maxima
(%i1) ratsubst (a, x*y^2, x^4*y^3 + x^4*y^8);
                              3      4
(%o1)                      a x  y + a
(%i2) cos(x)^4 + cos(x)^3 + cos(x)^2 + cos(x) + 1;
               4         3         2
(%o2)       cos (x) + cos (x) + cos (x) + cos(x) + 1
(%i3) ratsubst (1 - sin(x)^2, cos(x)^2, %);
            4           2                     2
(%o3)    sin (x) - 3 sin (x) + cos(x) (2 - sin (x)) + 3
(%i4) ratsubst (1 - cos(x)^2, sin(x)^2, sin(x)^4);

                        4           2
(%o4)                cos (x) - 2 cos (x) + 1

(%i5) radsubstflag: false$
(%i6) ratsubst (u, sqrt(x), x);
(%o6)                           x
(%i7) radsubstflag: true$
(%i8) ratsubst (u, sqrt(x), x);
                                2
(%o8)                          u
```

See also: `subst`.

<!-- category: Polynomials -->
<!-- keywords: ratvars -->
<!-- signatures: ratvars(x_1, ..., x_n), ratvars() -->
### Function: ratvars (x_1, ..., x_n)

Deklariert die Variablen *x_1*, ..., *x_n* zu Hauptvariablen einer
rationalen Funktion.  Ist die Variable *x_n* in einem Ausdruck vorhanden,
wird diese zur Hauptvariablen.  Ist *x_n* nicht im Ausdruck vorhanden, 
wird einer der vorhergehenden Variablen *x_i* zur Hauptvariablen.





Eine Variable einer rationalen Funktion, die nicht unter den *x_1*, ...,
*x_n* ist, erhalt eine geringe Prioritat als *x_1*.





Die Argumente der Funktion `ratvars` konnen auch nicht-rationale
Ausdrucke wie `sin(x)` sein.







Die Systemvariable `ratvars` enthalt die Liste der zuletzt mit der
Funktion `ratvars` zu Hauptvariablen erklarten Variablen.  Jeder Aufruf
der Funktion `ratvars` setzt diese Liste zuruck.  Der Aufruf ohne
Argumente `ratvars()` loscht die Systemvariable `ratvars`.

<!-- category: Polynomials -->
<!-- keywords: ratweight -->
<!-- signatures: ratweight(x_1, w_1, ..., x_n, w_n), ratweight() -->
### Function: ratweight (x_1, w_1, ..., x_n, w_n)

Weist der Variablen *x_i* ein Gewicht *w_i* zu.  Hat ein Term einer
rationalen Funktion ein großeres Gewicht als der Wert der Variablen
`ratwtlvl` wird der Term durch `0` ersetzt.  Das Gewicht eines Terms
wird anhand der mit `ratweight` den Variablen zugewiesenen Gewichte
ermittelt.  Die Gewichte der Variablen in einem Term werden mit der Potenz
der Variablen multipliziert und dann addiert.  Zum Beispiel hat der Term
`3 x_1^2 x_2` das Gewicht `2 w_1 + w_2`.  Terme die den Wert
von `ratwtlvl` ubersteigen, werden nur dann entfernt, wenn rationale
Funktionen in einer CRE-Form multipliziert oder potenziert werden.


`ratweight()` gibt die Liste der zugewiesenen Gewichte zuruck.





Der `ratweight`-Mechanismus ist nicht kompatibel mit dem Setzen der
Variablen `ratfac`.


Beispiele:



```maxima
(%i1) ratweight (a, 1, b, 1);
(%o1)                     [a, 1, b, 1]
(%i2) expr1: rat(a + b + 1)$
(%i3) expr1^2;
                  2                  2
(%o3)/R/         b  + (2 a + 2) b + a  + 2 a + 1
(%i4) ratwtlvl: 1$
(%i5) expr1^2;
(%o5)/R/                  2 b + 2 a + 1
```

See also: `ratwtlvl`, `ratweight`.

<!-- category: Polynomials -->
<!-- keywords: ratweights -->
<!-- signatures: ratweights -->
### Variable: ratweights

Standardwert: `[]`






Die Systemvariable `ratweights` enthalt die Liste der Gewichte die
Variablen mit der Funktion `ratweights` zugewiesen sind.


   


Die Gewichte konnen mit dem Kommando `kill(ratweights)` geloscht
werden.

See also: `ratweights`.

<!-- category: Polynomials -->
<!-- keywords: ratwtlvl -->
<!-- signatures: ratwtlvl -->
### Variable: ratwtlvl

Standardwert: `false`






Die Optionsvariable wird im Zusammenhang mit den `ratweight`-Mechanismus
genutzt und kontrolliert das Entfernen von Termen einer rationalen Funktion in
einer CRE-Form, wenn deren Gewicht den Wert von `ratwtlvl` ubersteigt.
Mit dem Standardwert `false` werden keine Terme entfernt.

See also: `ratweight`.

<!-- category: Polynomials -->
<!-- keywords: remainder -->
<!-- signatures: remainder(p_1, p_2), remainder(p_1, p_2, x_1, ..., x_n) -->
### Function: remainder (p_1, p_2)

Berechnet den Rest der Polynomdivision von *p_1* und *p_2* fur die
Variable *x_n*.  Die anderen Variablen *x_1*, ..., *x_n-1*
haben dieselbe Bedeutung wie fur die Funktion `ratvars`.


`remainder` gibt das zweite Element des Ergebnisses der Funktion
`divide` zuruck.


Siehe auch die Funktion `quotient`.


Beispiel:



```maxima
(%i1) poly1 : x^3-2*x^2-5*x+7;
                        3      2
(%o1)                  x  - 2 x  - 5 x + 7
(%i2) poly2 : x^2+1;
                              2
(%o2)                        x  + 1
(%i3) remainder(poly1, poly2, x);
(%o3)                        9 - 6 x
```

See also: `ratvars`, `divide`, `quotient`.

<!-- category: Polynomials -->
<!-- keywords: resultant -->
<!-- signatures: resultant(p_1, p_2, x) -->
### Function: resultant (p_1, p_2, x)

Berechnet die Resultante der Polynome *p_1* und *p_2* und eliminiert
die unabhangige Variable *x*.  Die Resultante ist die Determinante der
Sylvestermatrix fur die beiden Polynome.  Das Ergebnis ist Null, wenn die
beiden Polynome *p_1* und *p_2* einen gemeinsamen Faktor haben.





Konnen die Polynome *p_1* oder *p_2* faktorisiert werden, kann es
von Vorteil sein, die Faktorisierung zuvor auszufuhren.










Die Optionsvariable `resultant` kontrolliert, welcher Algorithmus fur
die Berechnung der Resultante von Maxima genutzt wird.  Siehe die 
Optionsvariable `option_resultant`.






Die Funktion `bezout` berechnet die Sylvestermatrix der Polynome
*p_1* und *p_2*.  Die Determinante der Sylvestermatrix ist die
Resultante.



Beispiele:



```maxima
(%i1) resultant(2*x^2+3*x+1, 2*x^2+x+1, x);
(%o1)                           8
(%i2) resultant(x+1, x+1, x);
(%o2)                           0
(%i3) resultant((x+1)*x, (x+1), x);
(%o3)                           0
(%i4) resultant(a*x^2+b*x+1, c*x + 2, x);
                         2
(%o4)                   c  - 2 b c + 4 a

(%i5) bezout(a*x^2+b*x+1, c*x+2, x);
                        [ 2 a  2 b - c ]
(%o5)                   [              ]
                        [  c      2    ]
(%i6) determinant(%);
(%o6)                   4 a - (2 b - c) c
```

See also: `option_resultant`, `bezout`.

<!-- category: Polynomials -->
<!-- keywords: savefactors -->
<!-- signatures: savefactors -->
### Variable: savefactors

Standardwert: `false`








Hat die Optionsvariable `savefactors` den Wert `true`, versuchen
einige Funktionen bei der Vereinfachung eine bereits vorhandene Faktorisierung
zu erhalten, um weitere Vereinfachungen zu beschleunigen.

<!-- category: Polynomials -->
<!-- keywords: showratvars -->
<!-- signatures: showratvars(expr) -->
### Function: showratvars (expr)

Gibt eine Liste mit den Variablen des Ausdrucks *expr* zuruck.  Der
Ausdruck liegt in einer CRE-Form vor.


Siehe auch die Funktion `ratvars`.

See also: `ratvars`.

<!-- category: Polynomials -->
<!-- keywords: sqfr -->
<!-- signatures: sqfr(expr) -->
### Function: sqfr (expr)

Entspricht der Funktion `factor` mit dem Unterschied, dass faktorisierte
Polynome quadratfrei sind.



Beispiel:



```maxima
(%i1) sqfr (4*x^4 + 4*x^3 - 3*x^2 - 4*x - 1);
                                2   2
(%o1)                  (2 x + 1)  (x  - 1)
```

See also: `factor`.

<!-- category: Polynomials -->
<!-- keywords: tellrat -->
<!-- signatures: tellrat(p_1, ..., p_n), tellrat() -->
### Function: tellrat (p_1, ..., p_n)

Fugt dem Ring der ganzen Zahlen, die algebraische Zahlen hinzu, die Losungen
der minimalen Polynome *p_1*, ..., *p_n* sind.  Jedes Argument
*p_i* ist ein Polynom, dessen Koeffizienten ganze Zahlen sind.





`tellrat(x)` bedeutet, dass in einer rationalen Funktion die
Variable *x* mit dem Wert `0` substituiert wird.




`tellrat()` gibt eine Liste der minimalen Polynome zuruck.





Die Optionsvariable `algebraic` muss den Wert `true` haben, damit
die Vereinfachungen von algebraischen Zahlen ausgefuhrt wird.





Maxima kennt bereits die Erweiterungen um die Imaginare Einheit `%i` und
die Wurzeln der ganzen Zahlen.





Die Funktion `untellrat` entfernt die Eigenschaften, die mit der Funktion
`tellrat` definiert wurden.









Hat ein minimales Polynom mehrere Variablen, wie zum Beispiel in
`tellrat(x^2 - y^2)`, dann entsteht eine Mehrdeutigkeit, da Maxima nicht
ermitteln kann, ob *x^2* fur *y^2* zu ersetzten ist, oder umgekehrt.
In diesem Fall kann die Syntax `tellrat (y^2 = x^2)` genutzt werden, die
besagt, dass *y^2* durch *x^2* zu ersetzen ist.











Beispiele:



```maxima
(%i1) 10*(%i + 1)/(%i + 3^(1/3));

                           10 (%i + 1)
(%o1)                      -----------
                                  1/3
                            %i + 3

(%i2) ev (ratdisrep (rat(%)), algebraic);

             2/3      1/3              2/3      1/3
(%o2)    (4 3    - 2 3    - 4) %i + 2 3    + 4 3    - 2

(%i3) tellrat (1 + a + a^2);
                            2
(%o3)                     [a  + a + 1]
(%i4) 1/(a*sqrt(2) - 1) + a/(sqrt(3) + sqrt(2));
                      1                 a
(%o4)           ------------- + -----------------
                sqrt(2) a - 1   sqrt(3) + sqrt(2)
(%i5) ev (ratdisrep (rat(%)), algebraic);
         (7 sqrt(3) - 10 sqrt(2) + 2) a - 2 sqrt(2) - 1
(%o5)    ----------------------------------------------
                               7
(%i6) tellrat (y^2 = x^2);
                        2    2   2
(%o6)                 [y  - x , a  + a + 1]
```

See also: `algebraic`, `untellrat`.

<!-- category: Polynomials -->
<!-- keywords: totaldisrep -->
<!-- signatures: totaldisrep(expr) -->
### Function: totaldisrep (expr)

Konvertiert alle Teilausdrucke im Ausdruck *expr* von der CRE-Form in die
allgemeine Form und gibt das Ergebnis zuruck.  Ist *expr* selbst eine
CRE-Form, dann entspricht `totaldisrep` der Funktion `ratdisrep`.





`totaldisrep` ist insbesondere hilfreich, wenn Gleichungen, Listen oder
Matrizen in eine allgemeine Form zu konvertieren sind.

<!-- category: Polynomials -->
<!-- keywords: untellrat -->
<!-- signatures: untellrat(x_1, ..., x_n) -->
### Function: untellrat (x_1, ..., x_n)

Entfernt Eigenschaften von den Symbolen *x_1*, ..., *x_n*, die mit
der Funktion `tellrat` zugewiesen wurden.

