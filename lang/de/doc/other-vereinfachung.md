## Vereinfachung

<!-- category: Other -->
<!-- keywords: additive -->
<!-- signatures: additive -->
### Variable: additive

`declare(f, additive)` deklariert eine Funktion `f` als additiv.  Hat 
die Funktion `f` ein Argument, dann wird `f(x + y)` zu 
`f(x) + f(y)` vereinfacht.


Ist `f` eine Funktion mit zwei oder mehr Argumenten, ist die
Additivitat fur das erste Argument definiert.  Zum Beispiel wird
`f(x + y,a + b)` zu `f(y, b + a) + f(x, b + a)` vereinfacht.


Siehe die Funktion `declare`.


Beispiel:



```maxima
(%i1) F3 (a + b + c);
(%o1)                     F3(c + b + a)
(%i2) declare (F3, additive);
(%o2)                         done
(%i3) F3 (a + b + c);
(%o3)                 F3(c) + F3(b) + F3(a)
```

See also: `declare`.

<!-- category: Other -->
<!-- keywords: antisymmetric -->
<!-- signatures: antisymmetric -->
### Variable: antisymmetric

`declare(f, antisymmetric)` deklariert die Funktion `f` als 
antisymmetrisch.  Zum Beispiel wird `f(y, x)` zu `- f(x, y)`
vereinfacht.


Siehe auch die Eigenschaft `symmetric` und die Funktion `declare`.


Beispiel:



```maxima
(%i1) S (b, a);
(%o1)                        S(b, a)
(%i2) declare (T, antisymmetric);
(%o2)                         done
(%i3) T (b, a);
(%o3)                       - T(a, b)
(%i4) T (a, c, e, d, b);
(%o4)                   T(a, b, c, d, e)
```

See also: `symmetric`, `declare`.

<!-- category: Other -->
<!-- keywords: combine -->
<!-- signatures: combine(expr) -->
### Function: combine (expr)

Terme einer rationalen Funktion, die denselben Nenner haben, werden 
zusammengefasst.


Beispiel:



```maxima
(%i1) x^2/(1+x)+2*x/(1+x);
                            2
                           x       2 x
(%o1)                     ----- + -----
                          x + 1   x + 1
(%i2) combine(%);
                             2
                            x  + 2 x
(%o2)                       --------
                             x + 1
```

<!-- category: Other -->
<!-- keywords: commutative -->
<!-- signatures: commutative -->
### Variable: commutative

`declare(f, commutative)` deklariert die Funktion `f` als kommutativ.
Zum Beispiel wird `f(x, z, y)` zu `f(x, y, z)` vereinfacht.
Dies hat denselben Effekt wie die Deklaration `symmetric`.


Siehe auch die Funktion `declare`.

See also: `symmetric`, `declare`.

<!-- category: Other -->
<!-- keywords: demoivre -->
<!-- signatures: demoivre(expr) -->
### Function: demoivre (expr)

Die Funktion `demoivre(expr)` konvertiert den Ausdruck *expr*, ohne
die Optionsvariable `demoivre` zu setzen.


Hat die Optionsvariable `demoivre` den Wert `true`, werden komplexe
Exponentialfunktionen in aquivalente Kreisfunktionen umgewandelt.
`exp(a + b*%i)` wird zu `%e^a*(cos(b)+%i*sin(b))` vereinfacht,
wenn `b` frei von der imaginaren Einheit `%i` ist.  `a` und 
`b` werden nicht expandiert.


Der Standardwert von `demoivre` ist `false`.


Siehe auch die Funktion `exponentialize`, um trigonometrische und
hyperbolische Funktionen in eine Exponentialform zu konvertieren.
`demoivre` und `exponentialize` konnen nicht gleichzeitig den Wert
`true` haben.

See also: `exponentialize`.

<!-- category: Other -->
<!-- keywords: distrib -->
<!-- signatures: distrib(expr) -->
### Function: distrib (expr)

Summen werden ausmultipliziert.  Im Unterschied zu der Funktion
`expand` wird `distrib` nur auf der obersten Ebene eines Ausdruckes
angewendet und ist daher schneller als `expand`.  Im Unterschied zu der
Funktion `multthru` werden die Summen der obersten Ebenen vollstandig
ausmultipliziert.


Beispiele:



```maxima
(%i1) distrib ((a+b) * (c+d));
(%o1)                 b d + a d + b c + a c
(%i2) multthru ((a+b) * (c+d));
(%o2)                 (b + a) d + (b + a) c
(%i3) distrib (1/((a+b) * (c+d)));
                                1
(%o3)                    ---------------
                         (b + a) (d + c)
(%i4) expand (1/((a+b) * (c+d)), 1, 0);
                                1
(%o4)                 ---------------------
                      b d + a d + b c + a c
```

See also: `expand`, `multthru`.

<!-- category: Other -->
<!-- keywords: distribute_over -->
<!-- signatures: distribute_over -->
### Variable: distribute_over

Standardwert: `true`


Die Optionsvariable `distribute_over` kontrolliert die Anwendung von 
Funktionen auf Listen, Matrizen oder Gleichungen.  Diese Eigenschaft wird nicht 
angewendet, wenn `distribute_over` den Wert `false` hat.


Beispiele:


Die Funktion `sin` wird auf eine Liste angewendet.



```maxima
(%i1) sin([x,1,1.0]);
(%o1)                 [sin(x), sin(1), .8414709848078965]
```


Die Funktion `mod` hat zwei Argumente, die auf Listen angewendet werden
kann.  Die Funktion kann auch auf verschachtelte Listen angewendet werden.



```maxima
(%i2) mod([x,11,2*a],10);
(%o2)                    [mod(x, 10), 1, 2 mod(a, 5)]
(%i3) mod([[x,y,z],11,2*a],10);
(%o3)       [[mod(x, 10), mod(y, 10), mod(z, 10)], 1, 2 mod(a, 5)]
```


Anwendung der Funktion `floor` auf eine Matrix und eine Gleichung.



```maxima
(%i4) floor(matrix([a,b],[c,d]));
                            [ floor(a)  floor(b) ]
(%o4)                       [                    ]
                            [ floor(c)  floor(d) ]
(%i5) floor(a=b);
(%o5)                         floor(a) = floor(b)
```


Funktionen mit mehreren Argumenten konnen auf Listen fur eines der Argumente
oder alle Argumente angewendet werden.



```maxima
(%i6) expintegral_e([1,2],[x,y]);
(%o6) [[expintegral_e(1, x), expintegral_e(1, y)], 
       [expintegral_e(2, x), expintegral_e(2, y)]]
```

See also: `sin`, `mod`, `floor`.

<!-- category: Other -->
<!-- keywords: domain -->
<!-- signatures: domain -->
### Variable: domain

Standardwert: `real`


Hat `domain` den Wert `complex`, wird `sqrt(x^2)` nicht zu
`abs(x)` vereinfacht, sondern bleibt `sqrt(x^2)`.


Hat `domain` den Wert `real`, wird eine reelle Große, die mit einem
gebrochenen Exponenten aus ganzzahligem Zahler und ungeradem Nenner potenziert
wird, wie in `x^(1/3)`, `x^(2/3)` oder `x^(1/n)`, wobei `n`
als `odd` deklariert ist, als reelle Wurzel ausgewertet: `(-8)^(1/3)`
vereinfacht sich zu `-2` und `(x^3)^(1/3)` zu `x`.
`sign`, `csign`, `rectform`, `realpart`,
`imagpart`, `polarform` und `carg` behandeln eine solche
Potenz ebenfalls als reell. Hat `domain` den Wert `complex`, liegt die
Potenz auf dem Hauptzweig: `(-8)^(1/3)` vereinfacht sich zu
`2*(-1)^(1/3)`, deren `rectform` gleich `sqrt(3)*%i+1` ist.

See also: `sign`, `csign`, `rectform`, `realpart`, `imagpart`, `polarform`, `carg`.

<!-- category: Other -->
<!-- keywords: evenfun, oddfun -->
<!-- signatures: oddfun -->
### Variable: evenfun

Erhalt eine Funktion oder ein Operator mit der Funktion `declare` die
Eigenschaft `evenfun` oder `oddfun` wird die Funktion oder der
Operator von Maxima als gerade und ungerade interpretiert.  Diese Eigenschaft
wird bei der Vereinfachung von Ausdrucken von Maxima angewendet.


Beispiele:



```maxima
(%i1) o (- x) + o (x);
(%o1)                     o(x) + o(- x)
(%i2) declare (o, oddfun);
(%o2)                         done
(%i3) o (- x) + o (x);
(%o3)                           0
(%i4) e (- x) - e (x);
(%o4)                     e(- x) - e(x)
(%i5) declare (e, evenfun);
(%o5)                         done
(%i6) e (- x) - e (x);
(%o6)                           0
```

See also: `declare`.

<!-- category: Other -->
<!-- keywords: expand -->
<!-- signatures: expand(expr), expand(expr, p, n) -->
### Function: expand (expr)

Expandiert den Ausdruck *expr*.  Produkte von Summen und Potenzen von Summen
werden ausmultipliziert.  Die Nenner von rationalen Ausdrucken, die Summen 
sind, werden in ihre Terme aufgespalten.  Produkte (kommutative und 
nicht-kommutative) werden in Summen herein multipliziert.


Fur Polynome ist es besser, die Funktion `ratexpand` zu verwenden, welche
fur diesen Fall einen effizienteren Algorithmus hat.


`maxnegex` und `maxposex` kontrollieren den maximalen negativen und
positiven Exponenten, fur die ein Ausdruck expandiert wird.


`expand(expr, p, n)` expandiert *expr*, wobei 
`maxposex` den Wert *p* und `maxnegex` den Wert *n* erhalten.


`expon` ist der großte negative Exponent, fur den ein Ausdruck
automatisch expandiert wird.  Hat zum Beispiel `expon` den Wert 4, wird 
`(x+1)^(-5)` nicht automatisch expandiert.


`expop` ist der großte positive Exponent, fur den ein Ausdruck
automatisch expandiert wird.  So wird `(x+1)^3` dann automatisch
expandiert, wenn `expop` großer oder gleich 3 ist.  Soll 
`(x+1)^n` mit der Funktion `expand` expandiert werden, weil `n`
großer als `expop` ist, dann ist dies nur moglich, wenn `n`
kleiner als `maxposex` ist.


`expand(expr,0,0)` bewirkt eine erneuerte vollstandige Vereinfachung 
des Ausdrucks *expr*.  Der Ausdruck wird nicht erneuert ausgewertet.  Im 
Unterschied zum Kommando `ev(expr, noeval)` wird eine spezielle Darstellung
(zum Beispiel eine CRE-Form) nicht entfernt.  Siehe auch `resimplify` und
`ev`.


Das `expand`-Flag wird mit `ev` verwendet, um einen Ausdruck zu 
expandieren.


Die Datei `simplification/facexp.mac` enthalt weitere Funktionen wie 
`facsum`, `factorfacsum` und `collectterms` und Variablen wie
`nextlayerfactor` und `facsum_combine`, um Ausdrucke zu
vereinfachen.  Diese Funktionen werden automatisch geladen und erlauben
spezielle Expansionen von Ausdrucken.  Eine kurze Beschreibung ist in der 
Datei `simplification/facexp.usg` enthalten.  Eine Demo kann mit
`demo(facexp)` ausgefuhrt werden.


Beispiele:



```maxima
(%i1) expr:(x+1)^2*(y+1)^3;
                               2        3
(%o1)                   (x + 1)  (y + 1)
(%i2) expand(expr);
       2  3        3    3      2  2        2      2      2
(%o2) x  y  + 2 x y  + y  + 3 x  y  + 6 x y  + 3 y  + 3 x  y
                                                      2
                                     + 6 x y + 3 y + x  + 2 x + 1
(%i3) expand(expr,2);
               2        3              3          3
(%o3)         x  (y + 1)  + 2 x (y + 1)  + (y + 1)
(%i4) expr:(x+1)^-2*(y+1)^3;

                                   3
                            (y + 1)
(%o4)                       --------
                                   2
                            (x + 1)

(%i5) expand(expr);
            3               2
           y             3 y            3 y             1
(%o5) ------------ + ------------ + ------------ + ------------
       2              2              2              2
      x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1   x  + 2 x + 1
(%i6) expand(expr, 2, 2);
                                   3
                            (y + 1)
(%o6)                     ------------
                           2
                          x  + 2 x + 1
```


Vereinfache einen Ausdruck erneut:



```maxima
(%i7) expr:(1+x)^2*sin(x);
                                2
(%o7)                    (x + 1)  sin(x)
(%i8) exponentialize:true;
(%o8)                         true
(%i9) expand(expr, 0, 0);
                            2    %i x     - %i x
                  %i (x + 1)  (%e     - %e      )
(%o9)           - -------------------------------
                                 2
```

See also: `ratexpand`, `maxnegex`, `maxposex`, `expon`, `expop`, `resimplify`, `ev`, `facsum`, `factorfacsum`, `collectterms`, `nextlayerfactor`, `facsum_combine`.

<!-- category: Other -->
<!-- keywords: expandwrt -->
<!-- signatures: expandwrt(expr, x_1, ..., x_n) -->
### Function: expandwrt (expr, x_1, ..., x_n)

Expandiert den Ausdruck `expr` in Bezug auf die Variablen *x_1*, 
..., *x_n*.  Alle Produkte, die die Variablen enthalten, werden 
ausmultipliziert.  Das Ergebnis ist frei von Produkten von Summen, die nicht 
frei von den Variablen sind.  *x_1*, ..., *x_n* konnen Variable, 
Operatoren oder Ausdrucke sein.


Standardmaßig wird der Nenner eines rationalen Ausdrucks nicht expandiert.
Dies kann mit der Optionsvariablen `expandwrt_denom` kontrolliert werden.


Die Funktion wird automatisch aus der Datei `simplification/stopex.mac`
geladen.

See also: `expandwrt_denom`.

<!-- category: Other -->
<!-- keywords: expandwrt_denom -->
<!-- signatures: expandwrt_denom -->
### Variable: expandwrt_denom

Standardwert: `false`


`expandwrt_denom` kontrolliert die Behandlung von rationalen Ausdrucken 
durch die Funktion `expandwrt`.  Ist der Wert `true`, werden der
Zahler und der Nenner eines rationalen Ausdrucks expandiert.  Ist der Wert
`false`, wird allein der Zahler expandiert.

<!-- category: Other -->
<!-- keywords: expandwrt_factored -->
<!-- signatures: expandwrt_factored(expr, x_1, ..., x_n) -->
### Function: expandwrt_factored (expr, x_1, ..., x_n)

Ist vergleichbar mit der Funktion `expandwrt`, behandelt aber Ausdrucke 
verschieden, die Produkte enthalten.  `expandwrt_factored` expandiert nur
die Faktoren im Ausdruck `expr`, die die Variablen *x_1*, ...,
*x_n* enthalten.

See also: `expandwrt`.

<!-- category: Other -->
<!-- keywords: expon -->
<!-- signatures: expon -->
### Variable: expon

Standardwert: 0


`expon` ist der großte negative Exponent fur den ein Ausdruck 
automatisch expandiert wird.  Hat zum Beispiel `expon` den Wert 4, wird
`(x+1)^(-5)` nicht automatisch expandiert.  Siehe auch `expop`.

See also: `expop`.

<!-- category: Other -->
<!-- keywords: exponentialize -->
<!-- signatures: exponentialize(expr) -->
### Function: exponentialize (expr)

Die Funktion `exponentialize` konvertiert trigonometrische und
hyperbolische Funktion die in dem Ausdruck *expr* auftreten in 
Exponentialfunktionen, ohne dass die Optionsvariable `exponentialize`
gesetzt wird.


Hat die Optionsvariable `exponentialize` den Wert `true`, werden
trigonometrische und hyperbolischen Funktionen in eine Exponentialform 
konvertiert.  Der Standardwert ist `false`.


`demoivre` konvertiert komplexe Exponentialfunktionen in trigonometrische
und hyperbolische Funktionen.  `exponentialize` und `demoivre` 
konnen nicht gleichzeitig den Wert `true` haben.

See also: `demoivre`.

<!-- category: Other -->
<!-- keywords: expop -->
<!-- signatures: expop -->
### Variable: expop

Standardwert: 0


`expop` ist der großte positive Exponent, fur den ein Ausdruck 
automatisch expandiert wird.  So wird `(x+1)^3` dann automatisch
expandiert, wenn `expop` großer oder gleich 3 ist.  Soll
`(x+1)^n` mit der Funktion `expand` expandiert werden, weil `n`
großer als `expop` ist, dann ist dies nur moglich, wenn `n`
kleiner als `maxposex` ist.  Siehe auch `expon`.

See also: `expand`, `maxposex`, `expon`.

<!-- category: Other -->
<!-- keywords: lassociative -->
<!-- signatures: lassociative -->
### Variable: lassociative

`declare(f, lassociative)` deklariert `f` als eine links-assoziative
Funktion.  Zum Beispiel wird `f (f (a,b), f (c, d))` zu 
`f (f (f (a, b), c), d)` vereinfacht.


Siehe auch die Eigenschaft `rassociative` und die Funktion
`declare`.

See also: `rassociative`, `declare`.

<!-- category: Other -->
<!-- keywords: linear -->
<!-- signatures: linear -->
### Variable: linear

`declare(f, linear)` deklariert die Funktion `f` als linear.


Hat die Funktion `f` ein Argument, dann wird `f(x + y)` zu 
`f(x) + f(y)` und `f(a*x)` zu `a*f(x)` vereinfacht.


Ist `f` eine Funktion mit zwei oder mehr Argumenten, ist die
Linearitat fur das erste Argument definiert.  Zum Beispiel wird
`f(a*x + b, x)` zu `a f(x, x) + f(1, x) b` vereinfacht.


`linear` ist aquivalent zu `additive` und `outative`.  Siehe
auch `opproperties` und die Funktion `declare`.



Beispiel:



```maxima
(%i1) 'sum (F(k) + G(k), k, 1, inf);
                       inf
                       ====
                       \
(%o1)                   >    (G(k) + F(k))
                       /
                       ====
                       k = 1
(%i2) declare (nounify (sum), linear);
(%o2)                         done
(%i3) 'sum (F(k) + G(k), k, 1, inf);
                     inf          inf
                     ====         ====
                     \            \
(%o3)                 >    G(k) +  >    F(k)
                     /            /
                     ====         ====
                     k = 1        k = 1
```

See also: `additive`, `outative`, `opproperties`, `declare`.

<!-- category: Other -->
<!-- keywords: maxnegex -->
<!-- signatures: maxnegex -->
### Variable: maxnegex

Standardwert: 1000


`maxnegex` ist der großte negative Exponent, der von der Funktion 
`expand` exandieren wird.  Siehe auch `maxposex`.

See also: `expand`, `maxposex`.

<!-- category: Other -->
<!-- keywords: maxposex -->
<!-- signatures: maxposex -->
### Variable: maxposex

Standardwert: 1000


`maxposex` ist der großte positive Exponent, der von der Funktion 
`expand` expandiert wird.  Siehe auch `maxnegex`.

See also: `expand`, `maxnegex`.

<!-- category: Other -->
<!-- keywords: multiplicative -->
<!-- signatures: multiplicative -->
### Variable: multiplicative

`declare(f, multiplicative)` deklariert die Funktion `f` als 
multiplikativ.


Hat die Funktion `f` ein Argument, dann wird `f(x*y)` zu
`f(x)*f(y)` vereinfacht.


Ist `f` eine Funktion mit zwei oder mehr Argumenten, ist die
Multiplikativitat fur das erste Argument definiert.  Zum Beispiel wird
`f(a*x + b, x)` zu `f(g(x), x)*f(h(x), x)` vereinfacht.


Diese Vereinfachung werden nicht fur Ausdrucke der Form
`product(x[i], i, m, n)` ausgefuhrt.


Siehe auch die Funktion `declare`.


Beispiel:



```maxima
(%i1) F2 (a * b * c);
(%o1)                       F2(a b c)
(%i2) declare (F2, multiplicative);
(%o2)                         done
(%i3) F2 (a * b * c);
(%o3)                   F2(a) F2(b) F2(c)
```

See also: `declare`.

<!-- category: Other -->
<!-- keywords: multthru -->
<!-- signatures: multthru(expr), multthru(expr_1, expr_2) -->
### Function: multthru (expr)

Multipliziert einen oder mehrere Faktoren in eine Summe herein.  `multthru`
expandiert keine Potenzen von Summen.  `multthru` ist die effizienteste
Methode, um Produkte von Summen auszumultiplizieren.  Da Maxima intern die
Division als ein Produkt darstellt, kann `multthru` auch angewendet werden,
um einen Nenner in eine Summe hereinzumultiplizieren.


`multthru(expr_1, expr_2)` multipliziert jeden Term des
Ausdrucks *expr_2* mit *expr_1*.  Der Ausdruck *expr_2* kann dabei 
eine Summe oder eine Gleichung sein.


Siehe auch die Funktionen `expand` und `function_distrib`.



```maxima
(%i1) x/(x-y)^2 - 1/(x-y) - f(x)/(x-y)^3;
                      1        x         f(x)
(%o1)             - ----- + -------- - --------
                    x - y          2          3
                            (x - y)    (x - y)
(%i2) multthru ((x-y)^3, %);
                           2
(%o2)             - (x - y)  + x (x - y) - f(x)
(%i3) ratexpand (%);
                           2
(%o3)                   - y  + x y - f(x)
(%i4) ((a+b)^10*s^2 + 2*a*b*s + (a*b)^2)/(a*b*s^2);
                        10  2              2  2
                 (b + a)   s  + 2 a b s + a  b
(%o4)            ------------------------------
                                  2
                             a b s
(%i5) multthru (%);  /* note that this does not expand (b+a)^10 */
                                        10
                       2   a b   (b + a)
(%o5)                  - + --- + ---------
                       s    2       a b
                           s
(%i6) multthru (a.(b+c.(d+e)+f));
(%o6)            a . f + a . c . (e + d) + a . b
(%i7) expand (a.(b+c.(d+e)+f));
(%o7)         a . f + a . c . e + a . c . d + a . b
```

See also: `expand`, `function_distrib`.

<!-- category: Other -->
<!-- keywords: negdistrib -->
<!-- signatures: negdistrib -->
### Variable: negdistrib

Standardwert: `true`


Hat `negdistrib` den Wert `true`, wird die Zahl -1 in eine Summe
hereinmultipliziert.  Zum Beispiel wird `-(x + y)` zu `- y - x` 
vereinfacht.  `true` ist der Standardwert von `negdistrib`.


Erhalt `negdistrib` den Wert `false` wird `-(x + y)`
nicht vereinfacht.  `negdistrib` sollte sehr umsichtig und nur in 
speziellen Fallen fur lokale Vereinfachungen genutzt werden.

<!-- category: Other -->
<!-- keywords: opproperties -->
<!-- signatures: opproperties -->
### Variable: opproperties

`opproperties` ist eine Liste mit den Eigenschaften, die eine Funktion oder
ein Operator erhalten kann und die die Vereinfachung der Funktionen und 
Operatoren kontrollieren.  Diese Eigenschaften erhalten die Funktionen und
Operatoren mit der Funktion `declare`.  Es gibt weitere Eigenschaften,
die Funktionen, Operatoren und Variablen erhalten konnen.  Die Systemvariable
`features` enthalt eine vollstandige Liste der Eigenschaften, die in 
Maximas Datenbank eingetragen werden.  Daruberhinaus konnen mit der Funktion
`declare` noch Eigenschaften definiert werden, die in der
Lisp-Eigenschaftsliste eingetragen werden.


Die folgenden Eigenschaften sind in der Liste `opproperties` enthalten und
kontrollieren die Vereinfachung von Funktionen und Operatoren:



   linear          additive        multiplicative
   outative        commutative     symmetric      
   antisymmetric   nary            lassociativ
   rassociative    evenfun         oddfun

See also: `declare`, `features`.

<!-- category: Other -->
<!-- keywords: outative -->
<!-- signatures: outative -->
### Variable: outative

`declare(f, outative)` deklariert eine Funktion `f` als outative.
Hat der Operator oder die Funktion Argumente mit konstanten Faktoren, so werden
diese konstanten Faktoren herausgezogen.


Hat die Funktion `f` ein Argument, dann wird `f(a*x)` zu 
`a*f(x)` vereinfacht, wenn `a` ein konstanter Faktor ist.


Ist `f` eine Funktion mit zwei oder mehr Argumenten, ist die
Outativitat fur das erste Argument definiert.  Zum Beispiel wird
`f(a*g(x), x)` zu `a*f(g(x),x)` vereinfacht, wenn `a` ein
konstanter Faktor ist.


Die Funktionen `sum`, `integrate` und `limit` haben die
Eigenschaft `outative`.  Siehe auch die Funktion `declare`.


Beispiel:



```maxima
(%i1) F1 (100 * x);
(%o1)                       F1(100 x)
(%i2) declare (F1, outative);
(%o2)                         done
(%i3) F1 (100 * x);
(%o3)                       100 F1(x)
(%i4) declare (zz, constant);
(%o4)                         done
(%i5) F1 (zz * y);
(%o5)                       zz F1(y)
```

See also: `sum`, `integrate`, `limit`, `declare`.

<!-- category: Other -->
<!-- keywords: radcan -->
<!-- signatures: radcan(expr) -->
### Function: radcan (expr)

Die Funktion `radcan` vereinfacht Ausdrucke, die die Logarithmusfunktion,
Exponentialfunktionen und Wurzeln enthalten.


Beispiele:



```maxima
(%i1) radcan((log(x+x^2)-log(x))^a/log(1+x)^(a/2));
                                           a/2
(%o1)                            log(x + 1)

(%i2) radcan((log(1+2*a^x+a^(2*x))/log(1+a^x)));
(%o2)                                  2

(%i3) radcan((%e^x-1)/(1+%e^(x/2)));
                                     x/2
(%o3)                              %e    - 1
```

<!-- category: Other -->
<!-- keywords: radexpand -->
<!-- signatures: radexpand -->
### Variable: radexpand

Standardwert: `true`




`radexpand` kontrolliert die Vereinfachung von Wurzeln.


Hat `radexpand` den Wert `all`, werden die nten-Wurzeln der Faktoren
eines Produktes, die eine n-te Potenz sind, aus der Wurzel herausgezogen.  Zum 
Beispiel vereinfacht `sqrt(16*x^2` zu `4*x`.


Inbesondere vereinfacht der Ausdruck `sqrt(x^2)` folgendermaßen:



- *
Hat `radexpand` den Wert `all` oder wurde `assume(x>0)` 
ausgefuhrt, dann vereinfacht `sqrt(x^2)` zu `x`.
- *
Hat `radexpand` den Wert `true` und `domain` ist `real`,
dann vereinfacht `sqrt(x^2)` zu `abs(x)`.
- *
Hat `radexpand` den Wert `false` oder hat `radexpand` den Wert
`true` und `domain` ist `complex`, dann wird `sqrt(x^2)`
nicht vereinfacht.

See also: `domain`.

<!-- category: Other -->
<!-- keywords: rassociative -->
<!-- signatures: rassociative -->
### Variable: rassociative

`declare(f, rassociative)` deklariert die Funktion `f` als
rechts-assioziativ.  Zum Beispiel wird `f(f(a, b), f(c, d))` zu 
`f(a, f(b, f(c, d)))` vereinfacht.


Siehe auch die Eigenschaft `lassociative` und die Funktion
`declare`.

See also: `lassociative`, `declare`.

<!-- category: Other -->
<!-- keywords: resimplify -->
<!-- signatures: resimplify(expr) -->
### Function: resimplify (expr)

Vereinfacht den Ausdruck *expr* erneut basierend auf der aktuellen Umgebung.
Diese Funktion ist nutzlich, wenn die Faktendatenbank, Optionsvariablen oder
tellsimp-Regeln geandert wurden, seitdem der Ausdruck zuletzt vereinfacht
wurde.


Beispiel:



```maxima
(%i1) expr : sin(x)^2 + cos(x)^2;
                                  2         2
(%o1)                          sin (x) + cos (x)
(%i2) exponentialize : true;
(%o2)                                true
(%i3) expr;
                                  2         2
(%o3)                          sin (x) + cos (x)
(%i4) resimplify(%);
                     %i x     - %i x 2      %i x     - %i x 2
                  (%e     + %e      )    (%e     - %e      )
(%o4)             -------------------- - --------------------
                           4                      4
(%i5) ratsimp(%);
(%o5)                                  1
```

<!-- category: Other -->
<!-- keywords: scsimp -->
<!-- signatures: scsimp(expr, rule_1, ..., rule_n) -->
### Function: scsimp (expr, rule_1, ..., rule_n)

Sequential Comparative Simplification (Methode nach Stoute).


`scsimp` versucht den Ausdruck *expr* mit Hilfe der Regeln 
*rule_1*, ..., *rule_n* zu vereinfachen.  Die Regeln werden 
nacheinander solange angewendet, bis sich der Ausdruck nicht weiter vereinfacht.
Fuhrt keine der Regeln zu einem Erfolg, wird der ursprungliche Ausdruck
zuruckgegeben.


`example(scsimp)` zeigt einige Beispiele.

<!-- category: Other -->
<!-- keywords: simp -->
<!-- signatures: simp -->
### Variable: simp

Standardwert: `true`


`simp` kontrolliert die Vereinfachung von Ausdrucken.  Der Standardwert 
von `simp` ist `true` und Ausdrucke werden vereinfacht.  `simp`
ist auch ein Auswertungsschalter fur die Funktion `ev`.


Wird `simp` als ein Auswertungschalter mit dem Wert `false` genutzt,
dann wird die Vereinfachung nur wahrend der Auswertungsphase unterdruckt.
`simp` kann nicht die Vereinfachung unterdrucken, die sich der Auswertung
anschließt.


Beispiele:


Die Vereinfachung wird ausgeschaltet.  Der Ausdruck `sin(1.0)` wird nicht 
zu einem numerischen Wert vereinfacht.  Der Auswertungsschalter `simp`
schaltet die Vereinfachung ein.



```maxima
(%i1) simp:false;
(%o1)                                false
(%i2) sin(1.0);
(%o2)                              sin(1.0)
(%i3) sin(1.0),simp;
(%o3)                          .8414709848078965
```


Die Vereinfachung wird wieder eingeschaltet.  Der Auswertungsschalter 
`simp` kann die Vereinfachung nicht vollstandig unterdrucken.  In der 
Ausgabe ist der Ausdruck vereinfacht, aber die Variable `x` enthalt einen
nicht vereinfachten Ausdruck, da die Zuweisung noch wahrend der 
Auswertungsphase des Ausdrucks vorgenommen wurde.



```maxima
(%i4) simp:true;
(%o4)                                true
(%i5) x:sin(1.0),simp:false;
(%o5)                          .8414709848078965
(%i6) :lisp $X
((%SIN) 1.0)
```

See also: `ev`.

<!-- category: Other -->
<!-- keywords: symmetric -->
<!-- signatures: symmetric -->
### Variable: symmetric

`declare(f, symmetric)` deklariert die Funktion `f` als symmetrisch.
Zum Beispiel wird `f(x, z, y)` zu `f(x, y, z)` vereinfacht.


`commutative` entspricht `symmetric`  Siehe auch die Funktion
`declare`.


Beispiel:



```maxima
(%i1) S (b, a);
(%o1)                        S(b, a)
(%i2) declare (S, symmetric);
(%o2)                         done
(%i3) S (b, a);
(%o3)                        S(a, b)
(%i4) S (a, c, e, d, b);
(%o4)                   S(a, b, c, d, e)
```

See also: `commutative`, `declare`.

<!-- category: Other -->
<!-- keywords: xthru -->
<!-- signatures: xthru(expr) -->
### Function: xthru (expr)

Die Terme einer Summe des Ausdrucks *expr* werden so zusammengefasst, dass
sie einen gemeinsamen Nenner haben.  Produkte und Potenzen von Summen werden
dabei nicht expandiert.  Gemeinsame Faktoren im Zahler und Nenner werden
gekurzt.


Es kann vorteilhaft sein, vor dem Ausfuhren von `ratsimp` zunachst mit
`xthru` die gemeinsamen Faktoren eines rationalen Ausdrucks zu kurzen.


Siehe auch die Funktion `combine`.


Beispiele:



```maxima
(%i1) ((x+2)^20 - 2*y)/(x+y)^20 + (x+y)^(-19) - x/(x+y)^20;
                                20
                 1       (x + 2)   - 2 y       x
(%o1)        --------- + --------------- - ---------
                    19             20             20
             (y + x)        (y + x)        (y + x)
(%i2) xthru (%);
                                 20
                          (x + 2)   - y
(%o2)                     -------------
                                   20
                            (y + x)
```

See also: `ratsimp`, `combine`.

