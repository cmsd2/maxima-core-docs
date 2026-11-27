## Mengen

<!-- category: Other -->
<!-- keywords: adjoin -->
<!-- signatures: adjoin(x, a) -->
### Function: adjoin (x, a)

Vereinigt die Menge *a* mit `{x}` und gibt die vereinigte
Menge als Ergebnis zuruck.


`adjoin` gibt eine Fehlermeldung, wenn das Argument *a* keine Menge
ist.


`adjoin(x, a)` und `union(set(x), a)` sind
aquivalent.  Die Funktion `adjoin` kann etwas schneller als die Funktion
`union` sein.


Siehe auch die Funktion `disjoin`.


Beispiele:



```maxima
(%i1) adjoin (c, {a, b});
(%o1)                       {a, b, c}
(%i2) adjoin (a, {a, b});
(%o2)                        {a, b}
```

See also: `union`, `disjoin`.

<!-- category: Other -->
<!-- keywords: belln -->
<!-- signatures: belln(n) -->
### Function: belln (n)

Reprasentiert die $n$-te Bellsche Zahl.


Ist das Argument *n* eine nicht-negative ganze Zahl, vereinfacht
`belln(n)` zu der $n$-ten Bellschen Zahl.  Fur andere
Argumente vereinfacht die Funktion `belln` nicht.


Ist das Argument der Funktion `belln` eine Liste, Menge, Matrix oder
eine Gleichung, wird die Funktion auf die Elemente oder beide Seiten der
Gleichung angewendet.



Beispiele:


Anwendung der Funktion `belln` auf nicht-negative ganze Zahlen.



```maxima
(%i1) makelist (belln (i), i, 0, 6);
(%o1)               [1, 1, 2, 5, 15, 52, 203]
(%i2) is (cardinality (set_partitions ({})) = belln (0));
(%o2)                         true
(%i3) is (cardinality (set_partitions ({1, 2, 3, 4, 5, 6})) =
                       belln (6));
(%o3)                         true
```


Anwendung der Funktion `belln` auf andere Argumente als nicht-negative
ganze Zahlen.



```maxima
(%i1) [belln (x), belln (sqrt(3)), belln (-9)];
(%o1)        [belln(x), belln(sqrt(3)), belln(- 9)]
```

<!-- category: Other -->
<!-- keywords: cardinality -->
<!-- signatures: cardinality(a) -->
### Function: cardinality (a)

Gibt die Machtigkeit (Kardinalitat) einer Menge zuruck.  Fur endliche
Mengen ist die Machtigkeit die Anzahl der Elemente der Menge.


Die Funktion `cardinality` ignoriert redundante Elemente einer Menge auch
dann, wenn die Vereinfachung abgeschaltet ist.


Beispiele:



```maxima
(%i1) cardinality ({});
(%o1)                           0
(%i2) cardinality ({a, a, b, c});
(%o2)                           3
(%i3) simp : false;
(%o3)                         false
(%i4) cardinality ({a, a, b, c});
(%o4)                           3
```

<!-- category: Other -->
<!-- keywords: cartesian_product -->
<!-- signatures: cartesian_product(b_1, ..., b_n) -->
### Function: cartesian_product (b_1, ..., b_n)

Gibt das kartesische Produkt der Mengen *b_1*, ..., *b_n* zuruck.
Das kartesische Produkt ist die Menge der geordneten Paare.


Das Ergebnis ist eine Menge mit Listen der Form `[x_1, ..., x_n]`, wobei *x_1*, ..., *x_n* die Elemente der Mengen
*b_1*, ..., *b_n* sind.


Die Funktion `cartesian_product` gibt eine Fehlermeldung, wenn eines
der Argumente keine Menge ist.


Beispiele:



```maxima
(%i1) cartesian_product ({0, 1});
(%o1)                      {[0], [1]}
(%i2) cartesian_product ({0, 1}, {0, 1});
(%o2)           {[0, 0], [0, 1], [1, 0], [1, 1]}
(%i3) cartesian_product ({x}, {y}, {z});
(%o3)                      {[x, y, z]}
(%i4) cartesian_product ({x}, {-1, 0, 1});
(%o4)              {[x, - 1], [x, 0], [x, 1]}
```

<!-- category: Other -->
<!-- keywords: disjoin -->
<!-- signatures: disjoin(x, a) -->
### Function: disjoin (x, a)

Entfernt das Element *x* aus der Menge *a* und gibt das Ergebnis
zuruck.


`disjoin` gibt eine Fehlermeldung, wenn das Argument *a* keine Menge
ist.


Die Ausdrucke `disjoin(x, a)`, `delete(x, a)` und `setdifference(a, set(x))` sind aquivalent.
Von diesen Moglichkeiten ist im Allgemeinen die Funktion `disjoin` am 
schnellsten.


Siehe auch die Funktion `adjoin` sowie die Funktionen `delete` und
`setdifference`.


Beispiele:



```maxima
(%i1) disjoin (a, {a, b, c, d});
(%o1)                       {b, c, d}
(%i2) disjoin (a + b, {5, z, a + b, %pi});
(%o2)                      {5, %pi, z}
(%i3) disjoin (a - b, {5, z, a + b, %pi});
(%o3)                  {5, %pi, b + a, z}
```

See also: `adjoin`, `delete`, `setdifference`.

<!-- category: Other -->
<!-- keywords: disjointp -->
<!-- signatures: disjointp(a, b) -->
### Function: disjointp (a, b)

`disjointp` hat das Ergebnis `true`, wenn die Mengen *a* und
*b* disjunkt sind.  Zwei Mengen sind disjunkt, wenn sie kein gemeinsames
Element besitzen.


`disjointp` gibt eine Fehlermeldung, wenn eines der Argumente keine
Menge ist.


Beispiele:



```maxima
(%i1) disjointp ({a, b, c}, {1, 2, 3});
(%o1)                         true
(%i2) disjointp ({a, b, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: divisors -->
<!-- signatures: divisors(n) -->
### Function: divisors (n)

Gibt die Menge der Teiler der Zahl *n* zuruck.


Ist das Argument *n* eine von Null verschiedene ganze Zahl, vereinfacht
`divisors(n)` zu einer Menge mit ganzen Zahlen, die Teiler des
Argumentes *n* sind.  Ist das Argument *n* eine negative Zahl wird
der Betrag des Argumentes genommen.  Das Ergebnis enthalt die Elemente
*1* und *n*.


Ist das Argument der Funktion `divisors` eine Liste, Menge, Matrix oder
eine Gleichung, wird die Funktion auf die Elemente oder beide Seiten der
Gleichung angewendet.


Beispiele:


Das Beispiel zeigt, dass 28 eine perfekte Zahl ist, die gleich die Summe
ihrer Teiler außer sich selbst ist.



```maxima
(%i1) s: divisors(28);
(%o1)                 {1, 2, 4, 7, 14, 28}
(%i2) lreduce ("+", args(s)) - 28;
(%o2)                          28
```


`divisors` ist eine vereinfachende Funktion.  In diesem Beispiel braucht
daher der Ausdruck nach der Substitution nicht erneut ausgewertet werden.



```maxima
(%i1) divisors (a);
(%o1)                      divisors(a)
(%i2) subst (8, a, %);
(%o2)                     {1, 2, 4, 8}
```


Anwendung der Funktion `divisors` auf Gleichungen, Listen, Matrizen oder
Mengen.



```maxima
(%i1) divisors (a = b);
(%o1)               divisors(a) = divisors(b)
(%i2) divisors ([a, b, c]);
(%o2)        [divisors(a), divisors(b), divisors(c)]
(%i3) divisors (matrix ([a, b], [c, d]));
                  [ divisors(a)  divisors(b) ]
(%o3)             [                          ]
                  [ divisors(c)  divisors(d) ]
(%i4) divisors ({a, b, c});
(%o4)        {divisors(a), divisors(b), divisors(c)}
```

<!-- category: Other -->
<!-- keywords: elementp -->
<!-- signatures: elementp(x, a) -->
### Function: elementp (x, a)

Gibt `true` zuruck, wenn das Argument *x* Element der Menge *a*
ist.


`elementp` gibt eine Fehlermeldung, wenn das Argument *a* keine
Menge ist.


Beispiele:



```maxima
(%i1) elementp (sin(1), {sin(1), sin(2), sin(3)});
(%o1)                         true
(%i2) elementp (sin(1), {cos(1), cos(2), cos(3)});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: emptyp -->
<!-- signatures: emptyp(a) -->
### Function: emptyp (a)

Gibt `true` zuruck, wenn das Argument *a* die leere Menge oder eine
leere Liste ist.


Beispiele:



```maxima
(%i1) map (emptyp, [{}, []]);
(%o1)                     [true, true]
(%i2) map (emptyp, [a + b, {{}}, %pi]);
(%o2)                 [false, false, false]
```

<!-- category: Other -->
<!-- keywords: equiv_classes -->
<!-- signatures: equiv_classes(s, F) -->
### Function: equiv_classes (s, F)

Gibt die Menge der Aquivalenzklassen der Menge *s* fur die
Aquivalenzrelation `F` zuruck.


Die Aquivalenzrelation `F` ist eine Funktion mit zwei Argumenten
definiert auf dem Kartesischen Produkt der Menge *s* mit *s*.  Die
Ruckgabe der Funktion `F` ist `true` oder `false` oder ein
Ausdruck *expr*, so dass `is(expr)` das Ergebnis `true`
oder `false` hat.


Ist *F* keine Aquivalenzrelation, wird die Funktion von
`equiv_classes` ohne Fehlermeldung akzeptiert.  Das Ergebnis ist jedoch
im Allgemeinen nicht korrekt.


Beispiele:


Die Aquivalenzrelation ist ein Lambda-Ausdruck mit den Ergebnissen
`true` oder `false`.



```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0},
                        lambda ([x, y], is (equal (x, y))));
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


Die Aquivalenzrelation ist der Name einer relationalen Funktion, die von
`is` zu `true` oder `false` ausgewertet wird.



```maxima
(%i1) equiv_classes ({1, 1.0, 2, 2.0, 3, 3.0}, equal);
(%o1)            {{1, 1.0}, {2, 2.0}, {3, 3.0}}
```


Die Aquivalenzklassen sind Mengen mit Zahlen, die sich um ein Vielfaches von
3 voneinander unterscheiden.



```maxima
(%i1) equiv_classes ({1, 2, 3, 4, 5, 6, 7},
                     lambda ([x, y], remainder (x - y, 3) = 0));
(%o1)              {{1, 4, 7}, {2, 5}, {3, 6}}
```

<!-- category: Other -->
<!-- keywords: every -->
<!-- signatures: every(f, s), every(f, L_1, ..., L_n) -->
### Function: every (f, s)

Gibt das Ergebnis `true` zuruck, wenn die Aussage `f` das Ergebnis
`true` fur alle Elemente der Menge *s* hat.


Ist das zweite Argument eine Menge, dann gibt `every(f, s)`
den Wert `true` zuruck, wenn `is(f(a_i))` das Ergebnis
`true` fur alle Elemente *a_i* der Menge *s* hat.  `every`
wertet *f* nicht notwendigerweise fur alle Elemente *a_i* aus, wenn
das Ergebnis bereits feststeht.  Da Mengen nicht geordnet sind, kann die
Funktion `every` die Ausdrucke `f(a_i)` in irgendeiner
Reihenfolge auswerten.


Sind die Argumente eine oder mehrere Listen, dann gibt
`every(f, L_1, ..., L_n)` den Wert `true` zuruck,
wenn `is(f(x_1, ..., x_n))` das Ergebnis `true`
fur alle *x_1*, ..., *x_n* der Listen *L_1*, ...,
*L_n* hat.  `every` wertet *f* wird nicht notwendigerweise fur 
alle Kombinationen *x_1*, ..., *x_n* aus, wenn das Ergebnis bereits
feststeht.  `every` wertet die Listen in der Reihenfolge des steigenden
Index aus.


Ist die leere Menge oder leere Liste ein Argument der Funktion `every`,
dann ist das Ergebnis immer `false`.


Hat die Optionsvariable `maperror` den Wert `true`, mussen alle
Listen *L_1*, ..., *L_n* die gleiche Lange haben.  Hat die
Optionsvariable `maperror` den Wert `false`, werden die Listen auf
die Lange der kurzesten Liste abgeschnitten.


Kann die Aussagefunktion *f* von der Funktion `is` nicht zu `true`
oder `false` ausgewertet werden, hangt das Ergebnis von der
Optionsvariablen `prederror` ab.  Hat die Optionsvariable `prederror`
den Wert `true`, werden solche Werte als `false` behandelt und die
Funktion `every` hat das Ergebnis `false`.  Hat `prederror`
den Wert `false`, werden solche Werte als `unknown` behandelt und die
Funktion `every` hat das Ergebnis `unknown`.


Beispiele:


`every` angewendet auf eine Menge.  Die Aussagefunktion hat ein Argument.



```maxima
(%i1) every (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) every (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         false
```


`every` angewendet auf zwei Listen.  Die Aussagefunktion hat zwei
Argumente entsprechend der Anzahl der Listen.



```maxima
(%i1) every ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) every ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Kann die Aussagefunktion *f* nicht zu `true` oder `false`
ausgewertet werden, hangt das Ergebnis von `every` von der 
Optionsvariablen `prederror` ab.



```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
                   [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) prederror : true;
(%o4)                         true
(%i5) every ("<", [x, y, z], [x^2, y^2, z^2]);
(%o5)                         false
```

See also: `maperror`, `prederror`.

<!-- category: Other -->
<!-- keywords: extremal_subset -->
<!-- signatures: extremal_subset(s, f, max), extremal_subset(s, f, min) -->
### Function: extremal_subset (s, f, max)

Gibt die Teilmenge von *s* zuruck, fur die die Funktion *f* maximale
oder minimale Ergebnisse hat.


`extremal_subset(s, f, max)` gibt die Teilmenge der Liste oder
Menge *s* zuruck, fur die die Funktion *f* ihre maximalen Werte
annimmt.


`extremal_subset(s, f, min)` gibt die Teilmenge der Liste oder
Menge *s* zuruck, fur die die Funktion *f* ihre minimalen Werte
annimmt.


Beispiele:



```maxima
(%i1) extremal_subset ({-2, -1, 0, 1, 2}, abs, max);
(%o1)                       {- 2, 2}
(%i2) extremal_subset ({sqrt(2), 1.57, %pi/2}, sin, min);
(%o2)                       {sqrt(2)}
```

<!-- category: Other -->
<!-- keywords: flatten -->
<!-- signatures: flatten(expr) -->
### Function: flatten (expr)

Sammelt die Argumente von allen Teilausdrucken, die denselben Operator wie
der Ausdruck *expr* haben und konstruiert einen Ausdruck mit dem Operator
des Ausdrucks *expr* und den Argumenten.  Ein einfaches Beispiel ist eine
verschachtelte Liste.  `flatten` konstruiert in diesem Fall eine Liste
aus den Elementen aller Teillisten.


Teilausdrucke, deren Operator sich von dem Hauptoperator des Ausdrucks
*expr* unterscheidet, werden als ein Argument betrachtet, auch wenn der
Teilausdruck wiederum Teilausdrucke des Hauptoperators enthalt.


Es ist moglich, dass `flatten` Ausdrucke konstruiert, in denen die
Anzahl der Argumente nicht der erforderlichen Anzahl an Argumenten des Operators
entspricht.  Dies kann zu Fehlermeldungen bei der Auswertung oder Vereinfachung
fuhren.  `flatten` kontrolliert nicht, ob die konstruierten Ausdrucke
gultig sind.


Ausdrucke mit speziellen Darstellungen, wie zum Beispiel CRE-Ausdrucke,
konnen von `flatten` nicht verarbeitet werden.  In diesem Fallen gibt
`flatten` das Argument unverandert zuruck.


Beispiele:


Wird `flatten` auf eine Liste angewendet, werden die Elemente aller
Teillisten zu einer Liste zusammengefugt.



```maxima
(%i1) flatten ([a, b, [c, [d, e], f], [[g, h]], i, j]);
(%o1)            [a, b, c, d, e, f, g, h, i, j]
```


Wird `flatten` auf eine Menge angewendet, werden die Elemente aller
Teilmengen zu einer Menge zusammengefugt.



```maxima
(%i1) flatten ({a, {b}, {{c}}});
(%o1)                       {a, b, c}
(%i2) flatten ({a, {[a], {a}}});
(%o2)                       {a, [a]}
```


Die Funktionsweise von `flatten` ist vergleichbar mit der Deklaration eines
Operators als ein N-ary-Operator.  Im Unterschied zu einer Deklaration hat 
`flatten` keinen Einfluss auf Teilausdrucke, die einen vom Hauptoperator
verschiedenen Operator haben.



```maxima
(%i1) expr: flatten (f (g (f (f (x)))));
(%o1)                     f(g(f(f(x))))
(%i2) declare (f, nary);
(%o2)                         done
(%i3) ev (expr);
(%o3)                      f(g(f(x)))
```


`flatten` kann Ausdrucke mit indizierte Funktionen vereinfachen.



```maxima
(%i1) flatten (f[5] (f[5] (x, y), z));
(%o1)                      f (x, y, z)
                            5
```


Es ist moglich, dass `flatten` einen Ausdruck konstruiert, der nicht die
korrekte Anzahl an Argumenten eines Operators enthalt.



```maxima
(%i1) 'mod (5, 'mod (7, 4));
(%o1)                   mod(5, mod(7, 4))
(%i2) flatten (%);
(%o2)                     mod(5, 7, 4)
(%i3) ''%, nouns;
Wrong number of arguments to mod
 -- an error.  Quitting.  To debug this try debugmode(true);
```

<!-- category: Other -->
<!-- keywords: full_listify -->
<!-- signatures: full_listify(a) -->
### Function: full_listify (a)

Ersetzt jedes Auftreten des Operators fur Mengen in dem Ausdruck *a*
durch den Operator fur Listen.  Die Ersetzung wird auch in verschachtelten
Teilausdrucken ausgefuhrt, deren Operator nicht der Operator fur Mengen
ist.


Die Funktion `listify` ersetzt nur den Hauptoperator eines Ausdrucks.



Beispiele:



```maxima
(%i1) full_listify ({a, b, {c, {d, e, f}, g}});
(%o1)               [a, b, [c, [d, e, f], g]]
(%i2) full_listify (F (G ({a, b, H({c, d, e})})));
(%o2)              F(G([a, b, H([c, d, e])]))
```

See also: `listify`.

<!-- category: Other -->
<!-- keywords: fullsetify -->
<!-- signatures: fullsetify(a) -->
### Function: fullsetify (a)

Ist *a* eine Liste, wird der Operator fur Listen durch den Operator fur
Mengen ersetzt.  Dann wird `fullsetify` auf alle Argumente der Liste
angewendet.  Ist ein Argument keine Liste, wenn das Argument unverandert
zuruckgegeben.


Die Funktion `setify` ersetzt nur den Hauptoperator eines Ausdrucks.


Beispiele:


Im zweiten Beispiel wird das Argument der Funktion `f` nicht in eine
Menge konvertiert, da der Operator des Teilausdrucks keine Liste ist.



```maxima
(%i1) fullsetify ([a, [a]]);
(%o1)                       {a, {a}}
(%i2) fullsetify ([a, f([b])]);
(%o2)                      {a, f([b])}
```

See also: `setify`.

<!-- category: Other -->
<!-- keywords: identity -->
<!-- signatures: identity(x) -->
### Function: identity (x)

Gibt fur jedes Argument *x* das Argument selbst zuruck.


Beispiele:


`identity` kann als eine Aussagefunktion genutzt werden, wenn die Argumente
boolesche Werte sind.



```maxima
(%i1) every (identity, [true, true]);
(%o1)                         true
```

<!-- category: Other -->
<!-- keywords: integer_partitions -->
<!-- signatures: integer_partitions(n), integer_partitions(n, len) -->
### Function: integer_partitions (n)

Ermittelt die Zerlegung einer ganzen Zahl *n* in ganze Zahlen, die
*n* als Summe haben.


`integer_partitions(n)` gibt eine Menge aller Zerlegungen der ganzen
Zahl *n* zuruck.  Jede Zerlegung ist eine Liste mit den ganzen Zahlen, die
*n* als Summe haben.  Die Listen sind nach der Große sortiert.


`integer_partitions(n, len)` gibt eine Menge aller Zerlegungen
der ganzen Zahl *n* zuruck, deren Listen `len` oder weniger Elemente
haben.  Listen die weniger als `len` Elemente haben, werden mit Nullen
aufgefullt.


Siehe auch die Funktionen `num_partitions` und
`num_distinct_partitions`.


Beispiele:



```maxima
(%i1) integer_partitions (3);
(%o1)               {[1, 1, 1], [2, 1], [3]}
(%i2) s: integer_partitions (25)$
(%i3) cardinality (s);
(%o3)                         1958
(%i4) map (lambda ([x], apply ("+", x)), s);
(%o4)                         {25}
(%i5) integer_partitions (5, 3);
(%o5) {[2, 2, 1], [3, 1, 1], [3, 2, 0], [4, 1, 0], [5, 0, 0]}
(%i6) integer_partitions (5, 2);
(%o6)               {[3, 2], [4, 1], [5, 0]}
```


Um alle Zerlegungen zu finden, die eine Bedingung erfullen, kann die Funktion
`subset` genutzt werden.  In diesem Beispiel werden alle Zerlegungen
der Zahl 10 ermittelt, die nur Primzahlen enthalten.



```maxima
(%i1) s: integer_partitions (10)$
(%i2) cardinality (s);
(%o2)                          42
(%i3) xprimep(x) := integerp(x) and (x > 1) and primep(x)$
(%i4) subset (s, lambda ([x], every (xprimep, x)));
(%o4) {[2, 2, 2, 2, 2], [3, 3, 2, 2], [5, 3, 2], [5, 5], [7, 3]}
```

See also: `num_partitions`, `num_distinct_partitions`, `subset`.

<!-- category: Other -->
<!-- keywords: intersect -->
<!-- signatures: intersect(a_1, ..., a_n) -->
### Function: intersect (a_1, ..., a_n)

`intersect` ist identisch mit der Funktion `intersection`.

See also: `intersection`.

<!-- category: Other -->
<!-- keywords: intersection -->
<!-- signatures: intersection(a_1, ..., a_n) -->
### Function: intersection (a_1, ..., a_n)

Gibt die Schnittmenge der Mengen *a_1*, ..., *a_n* zuruck.  Die
Schnittmenge enthalt die Elemente, die den Mengen gemeinsam sind.


`intersection` gibt eine Fehlermeldung, wenn eines der Argumente
keine Menge ist.


Beispiele:



```maxima
(%i1) S_1 : {a, b, c, d};
(%o1)                     {a, b, c, d}
(%i2) S_2 : {d, e, f, g};
(%o2)                     {d, e, f, g}
(%i3) S_3 : {c, d, e, f};
(%o3)                     {c, d, e, f}
(%i4) S_4 : {u, v, w};
(%o4)                       {u, v, w}
(%i5) intersection (S_1, S_2);
(%o5)                          {d}
(%i6) intersection (S_2, S_3);
(%o6)                       {d, e, f}
(%i7) intersection (S_1, S_2, S_3);
(%o7)                          {d}
(%i8) intersection (S_1, S_2, S_3, S_4);
(%o8)                          {}
```

<!-- category: Other -->
<!-- keywords: kron_delta -->
<!-- signatures: kron_delta(x_1, x_2, ..., x_p) -->
### Function: kron_delta (x_1, x_2, ..., x_p)

Ist die Kronecker-Delta-Funktion.









`kron_delta` vereinfacht zu `1`, wenn die Argumente *x_i* und
*y_i* fur alle Paare gleich sind, und zu `0`, wenn *x_i* und 
*y_i* nicht gleich sind fur irgendein Paar der Argumente.  Die Gleichheit
wird festgestellt mit `is(equal(xi,xj))` und die Ungleichheit mit
`is(notequal(xi,xj))`.  Wird nur ein Argument angegeben, signalisiert
die Funktion `kron_delta` einen Fehler.


Beispiele:



```maxima
(%i1) kron_delta(a,a);
(%o1)                                  1
(%i2) kron_delta(a,b,a,b);
(%o2)                          kron_delta(a, b)
(%i3) kron_delta(a,a,b,a+1);
(%o3)                                  0
(%i4) assume(equal(x,y));
(%o4)                            [equal(x, y)]
(%i5) kron_delta(x,y);
(%o5)                                  1
```

<!-- category: Other -->
<!-- keywords: listify -->
<!-- signatures: listify(a) -->
### Function: listify (a)

Ist das Argument *a* eine Menge, werden die Elemente der Menge als eine
Liste zuruckgegeben.  Ansonsten wird *a* zuruckgegeben.


Siehe die Funktion `full_listify`, um auch Mengen in Teilausdrucken
von *a* durch Listen zu ersetzen.


Beispiele:



```maxima
(%i1) listify ({a, b, c, d});
(%o1)                     [a, b, c, d]
(%i2) listify (F ({a, b, c, d}));
(%o2)                    F({a, b, c, d})
```

See also: `full_listify`.

<!-- category: Other -->
<!-- keywords: lreduce -->
<!-- signatures: lreduce(F, s), lreduce(F, s, s_0) -->
### Function: lreduce (F, s)

Wendet eine Funktion *F*, die zwei Argumente hat, auf die Elemente einer
Liste *s* an, indem die Funktionsaufrufe verkettet werden.


Das Kommando `lreduce(F, s)` bildet den Ausdruck
`F(... F(F(s_1, s_2), s_3), ... s_n)`.  Ist das optionale Argument
*s_0* vorhanden, dann ist das Ergebnis aquivalent zu
`lreduce(F, cons(s_0, s))`.


Siehe auch `rreduce`, `xreduce` und `tree_reduce`.



Beispiele:


`lreduce` ohne das optionale Argument.



```maxima
(%i1) lreduce (f, [1, 2, 3]);
(%o1)                     f(f(1, 2), 3)
(%i2) lreduce (f, [1, 2, 3, 4]);
(%o2)                  f(f(f(1, 2), 3), 4)
```


`lreduce` mit dem optionalen Argument.



```maxima
(%i1) lreduce (f, [1, 2, 3], 4);
(%o1)                  f(f(f(4, 1), 2), 3)
```


`lreduce` mit den binaren Operatoren der Exponentiation "^" und der
Division "/".



```maxima
(%i1) lreduce ("^", args ({a, b, c, d}));
                               b c d
(%o1)                       ((a ) )
(%i2) lreduce ("/", args ({a, b, c, d}));
                                a
(%o2)                         -----
                              b c d
```

See also: `rreduce`, `xreduce`, `tree_reduce`.

<!-- category: Other -->
<!-- keywords: makeset -->
<!-- signatures: makeset(expr, x, s) -->
### Function: makeset (expr, x, s)

Generiert eine Menge, indem der Ausdruck *expr* ausgewertet wird, wobei das
Argument *x* eine Liste mit Variablen des Ausdrucks und *s* eine
Menge oder eine Liste mit Listen ist.  Ein Element der Menge wird generiert,
indem die Variablen in *x* nacheinander an die Elemente in *s*
gebunden werden.


Jedes Element des Argumentes *s* muss dieselbe Lange wie *x* haben.
Die Liste der Variablen *x* muss eine List mit Symbolen sein.  Indizierte
Variablen sind nicht moglich.  Auch wenn nur eine Variable angegeben wird,
muss diese Element einer Liste sein und jedes Element von *s* muss eine
Liste mit einem Element sein.


Siehe auch die Funktion `makelist`, um eine Liste zu generieren.


Beispiele:



```maxima
(%i1) makeset (i/j, [i, j], [[1, a], [2, b], [3, c], [4, d]]);
                           1  2  3  4
(%o1)                     {-, -, -, -}
                           a  b  c  d
(%i2) S : {x, y, z}$
(%i3) S3 : cartesian_product (S, S, S);
(%o3) {[x, x, x], [x, x, y], [x, x, z], [x, y, x], [x, y, y], 
[x, y, z], [x, z, x], [x, z, y], [x, z, z], [y, x, x], 
[y, x, y], [y, x, z], [y, y, x], [y, y, y], [y, y, z], 
[y, z, x], [y, z, y], [y, z, z], [z, x, x], [z, x, y], 
[z, x, z], [z, y, x], [z, y, y], [z, y, z], [z, z, x], 
[z, z, y], [z, z, z]}
(%i4) makeset (i + j + k, [i, j, k], S3);
(%o4) {3 x, 3 y, y + 2 x, 2 y + x, 3 z, z + 2 x, z + y + x, 
                                       z + 2 y, 2 z + x, 2 z + y}
(%i5) makeset (sin(x), [x], {[1], [2], [3]});
(%o5)               {sin(1), sin(2), sin(3)}
```

See also: `makelist`.

<!-- category: Other -->
<!-- keywords: moebius -->
<!-- signatures: moebius(n) -->
### Function: moebius (n)

Ist die Mobiusfunktion.


Ist die naturliche Zahl *n* quadratfrei, dann vereinfacht die
Mobiusfunktion zu `-1^k`, wobei *k* die Anzahl der Primfaktoren der
Zahl *n* ist.  Eine Zahl ist quadratfrei, wenn sie nur voneinander
verschiedene Primfaktoren hat.  Fur `n = 1` vereinfacht die
Mobiusfunktion zu `1` und fur alle anderen positiven ganzen Zahlen zum
Wert `0`.  Fur andere Argumente wird eine Substantivform als Ergebnis
zuruckgegeben.


Ist das Argument der Funktion `moebius` eine Liste, Menge, Matrix oder
eine Gleichung, wird die Funktion auf die Elemente oder beide Seiten der
Gleichung angewendet.


Beispiele:



```maxima
(%i1) moebius (1);
(%o1)                           1
(%i2) moebius (2 * 3 * 5);
(%o2)                          - 1
(%i3) moebius (11 * 17 * 29 * 31);
(%o3)                           1
(%i4) moebius (2^32);
(%o4)                           0
(%i5) moebius (n);
(%o5)                      moebius(n)
(%i6) moebius (n = 12);
(%o6)                    moebius(n) = 0
(%i7) moebius ([11, 11 * 13, 11 * 13 * 15]);
(%o7)                      [- 1, 1, 1]
(%i8) moebius (matrix ([11, 12], [13, 14]));
                           [ - 1  0 ]
(%o8)                      [        ]
                           [ - 1  1 ]
(%i9) moebius ({21, 22, 23, 24});
(%o9)                      {- 1, 0, 1}
```

<!-- category: Other -->
<!-- keywords: multinomial_coeff -->
<!-- signatures: multinomial_coeff(a_1, ..., a_n), multinomial_coeff() -->
### Function: multinomial_coeff (a_1, ..., a_n)

Gibt den Multinomialkoeffizienten zuruck.  Im Spezialfall `k = 2`
ergibt sich die Binomialverteilung.  Siehe `binomial`.


Enthalt das Ergebnis Fakultaten, kann das Ergebnis moglicherweise mit der
Funktion `minfactorial` weiter vereinfacht werden.


Beispiele:



```maxima
(%i1) multinomial_coeff (1, 2, x);
                            (x + 3)!
(%o1)                       --------
                              2 x!
(%i2) minfactorial (%);
                     (x + 1) (x + 2) (x + 3)
(%o2)                -----------------------
                                2
(%i3) multinomial_coeff (-6, 2);
                             (- 4)!
(%o3)                       --------
                            2 (- 6)!
(%i4) minfactorial (%);
(%o4)                          10
```

See also: `binomial`, `minfactorial`.

<!-- category: Other -->
<!-- keywords: num_distinct_partitions -->
<!-- signatures: num_distinct_partitions(n), num_distinct_partitions(n, list) -->
### Function: num_distinct_partitions (n)

Gibt die Anzahl der Moglichkeiten an, eine naturliche Zahl *n* in
Summanden zu zerlegen, wobei jeder Summand nur einmal vorkommt.  Ist *n*
keine naturliche Zahl wird eine Substantivform als Ergebnis zuruckgegeben.


`num_distinct_partitions(n, list)` gibt eine Liste mit der Anzahl
der voneinander verschiedenen Partitionen der naturlichen Zahlen 1, 2, 3,
..., *n* zuruck.


Siehe auch die Funktionen `num_partitions` und `integer_partitions`.


Beispiele:



```maxima
(%i1) num_distinct_partitions (12);
(%o1)                          15
(%i2) num_distinct_partitions (12, list);
(%o2)      [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15]
(%i3) num_distinct_partitions (n);
(%o3)              num_distinct_partitions(n)
```

See also: `num_partitions`, `integer_partitions`.

<!-- category: Other -->
<!-- keywords: num_partitions -->
<!-- signatures: num_partitions(n), num_partitions(n, list) -->
### Function: num_partitions (n)

Gibt die Anzahl der Moglichkeiten an, eine naturliche Zahl *n* in
Summanden zu zerlegen.  Ist *n* keine naturliche Zahl wird eine
Substantivform als Ergebnis zuruckgegeben.


`num_partitions(n, list)` gibt eine Liste mit der Anzahl
der Partitionen der naturlichen Zahlen 1, 2, 3, ..., *n* zuruck.


Das Kommando `num_partitions(n)` ist fur eine naturliche Zahl
*n* aquivalent zu `cardinality(integer_partitions(n))`.
Da die Funktion `num_partitions` die Menge nicht konstruiert, ist diese
Funktion deutlich schneller.


Siehe auch die Funktionen `num_distinct_partitions` und
`integer_partitions`.


Beispiele:



```maxima
(%i1) num_partitions (5) = cardinality (integer_partitions (5));
(%o1)                         7 = 7
(%i2) num_partitions (8, list);
(%o2)            [1, 1, 2, 3, 5, 7, 11, 15, 22]
(%i3) num_partitions (n);
(%o3)                   num_partitions(n)
```

See also: `num_distinct_partitions`, `integer_partitions`.

<!-- category: Other -->
<!-- keywords: partition_set -->
<!-- signatures: partition_set(a, f) -->
### Function: partition_set (a, f)

Zerlegt eine Menge *a* mit der Aussagefunktion *f*.


`partition_set` gibt eine Liste mit zwei Elementen zuruck.  Das erste
Element ist die Menge der Elemente, fur die die Aussagefunktion *f* zu
`false` ausgewertet wird.  Das zweite Element ist die Menge aller anderen
Elemente.  `partition_set` wendet nicht die Funktion `is` auf das
Ergebnis der Aussagefunktion *f* an.


`partition_set` gibt eine Fehlermeldung, wenn *a* keine Menge ist.


Siehe auch die Funktion `subset`.


Beispiele:



```maxima
(%i1) partition_set ({2, 7, 1, 8, 2, 8}, evenp);
(%o1)                   [{1, 7}, {2, 8}]
(%i2) partition_set ({x, rat(y), rat(y) + z, 1},
                     lambda ([x], ratp(x)));
(%o2)/R/              [{1, x}, {y, y + z}]
```

See also: `subset`.

<!-- category: Other -->
<!-- keywords: permutations -->
<!-- signatures: permutations(a) -->
### Function: permutations (a)

Gibt eine Menge mit allen voneinander verschiedenen Permutationen der Elemente
der Liste oder Menge *a* zuruck.  Die Permutationen sind Listen.


Ist das Argument *a* eine Liste, werden auch doppelte Elemente in die
moglichen Permutationen eingeschlossen.


`permutations` gibt eine Fehlermeldung, wenn *a* keine Liste oder
Menge ist.


Siehe auch die Funktion `random_permutation`.


Beispiele:



```maxima
(%i1) permutations ([a, a]);
(%o1)                       {[a, a]}
(%i2) permutations ([a, a, b]);
(%o2)           {[a, a, b], [a, b, a], [b, a, a]}
```

See also: `random_permutation`.

<!-- category: Other -->
<!-- keywords: powerset -->
<!-- signatures: powerset(a), powerset(a, n) -->
### Function: powerset (a)

Gibt die Menge aller Teilmengen der Menge *a* oder eine Teilmenge dieser
Menge zuruck.


`powerset(a)` gibt die Menge aller Teilmengen der Menge *a*
zuruck.  Die Ergebnismenge hat `2^cardinality(a)` Elemente.


`powerset(a, n)` gibt die Menge aller Teilmengen der Menge
*a* zuruck, die die Machtigkeit *n* haben.


`powerset` gibt eine Fehlermeldung, wenn *a* keine Menge oder *n*
keine naturliche Zahl ist.


Beispiele:



```maxima
(%i1) powerset ({a, b, c});
(%o1) {{}, {a}, {a, b}, {a, b, c}, {a, c}, {b}, {b, c}, {c}}
(%i2) powerset ({w, x, y, z}, 4);
(%o2)                    {{w, x, y, z}}
(%i3) powerset ({w, x, y, z}, 3);
(%o3)     {{w, x, y}, {w, x, z}, {w, y, z}, {x, y, z}}
(%i4) powerset ({w, x, y, z}, 2);
(%o4)   {{w, x}, {w, y}, {w, z}, {x, y}, {x, z}, {y, z}}
(%i5) powerset ({w, x, y, z}, 1);
(%o5)                 {{w}, {x}, {y}, {z}}
(%i6) powerset ({w, x, y, z}, 0);
(%o6)                         {{}}
```

<!-- category: Other -->
<!-- keywords: random_permutation -->
<!-- signatures: random_permutation(a) -->
### Function: random_permutation (a)

Gibt eine zufallige Permutation der Menge oder Liste *a* zuruck, die mit
dem Knuth-Misch-Algorithmus generiert wird.


Die Ruckgabe ist eine neue Liste, die verschieden vom Argument *a*.
Jedoch werden nicht die Elemente kopiert.


Beispiele:



```maxima
(%i1) random_permutation ([a, b, c, 1, 2, 3]);
(%o1)                  [c, 1, 2, 3, a, b]
(%i2) random_permutation ([a, b, c, 1, 2, 3]);
(%o2)                  [b, 3, 1, c, a, 2]
(%i3) random_permutation ({x + 1, y + 2, z + 3});
(%o3)                 [y + 2, z + 3, x + 1]
(%i4) random_permutation ({x + 1, y + 2, z + 3});
(%o4)                 [x + 1, y + 2, z + 3]
```

<!-- category: Other -->
<!-- keywords: rreduce -->
<!-- signatures: rreduce(F, s), rreduce(F, s, s_{n + 1}) -->
### Function: rreduce (F, s)

Wendet eine Funktion *F*, die zwei Argumente hat, auf die Elemente einer
Liste *s* an, indem die Funktionsaufrufe verkettet werden.


Das Kommando `rreduce(F, s)` bildet den Ausdruck
`F(s_1, ... F(s_{n - 2}, F(s_{n - 1}, s_n)))`.  Ist das optionale
Argument *s_0* vorhanden, dann ist das Ergebnis aquivalent zu
`rreduce(F, endcons(s_{n + 1}, s))`.


Siehe auch `lreduce`, `xreduce` und `tree_reduce`.


Beispiele:


`rreduce` ohne das optionale Argument.



```maxima
(%i1) rreduce (f, [1, 2, 3]);
(%o1)                     f(1, f(2, 3))
(%i2) rreduce (f, [1, 2, 3, 4]);
(%o2)                  f(1, f(2, f(3, 4)))
```


`rreduce` mit dem optionalen Argument.



```maxima
(%i1) rreduce (f, [1, 2, 3], 4);
(%o1)                  f(1, f(2, f(3, 4)))
```


`rreduce` mit den binaren Operatoren der Exponentiation "^" und der
Division "/".



```maxima
(%i1) rreduce ("^", args ({a, b, c, d}));
                                 d
                                c
                               b
(%o1)                         a
(%i2) rreduce ("/", args ({a, b, c, d}));
                               a c
(%o2)                          ---
                               b d
```

See also: `lreduce`, `xreduce`, `tree_reduce`.

<!-- category: Other -->
<!-- keywords: set_partitions -->
<!-- signatures: set_partitions(a), set_partitions(a, n) -->
### Function: set_partitions (a)

Gibt die Menge aller Partitionen der Menge *a* oder eine Teilmenge
dieser Menge zuruck.


`set_partitions(a, n)` gibt eine Menge aller Zerlegungen der
Menge *a* in *n* nicht-leere voneinander disjunkte Teilmengen zuruck.


`set_partitions(a)` gibt die Menge aller Zerlegungen zuruck.


`stirling2` gibt die Machtigkeit einer Menge zuruck, die alle
Zerlegungen einer Menge enthalt.


Eine Menge mit Zerlegungen $P$ ist eine Zerlegung der Menge $S$, wenn



1. jedes Elemente der Menge $P$ eine nicht-leere Menge ist,
2. verschiedene Elemente der Menge $P$ voneinander disjunkt sind,
3. die Vereinigung von Elementen der Menge $P$ gleich der Menge $S$ ist.


Beispiele:


Die leere Menge ist eine Zerlegung von sich selbst.



```maxima
(%i1) set_partitions ({});
(%o1)                         {{}}
```


Die Machtigkeit der Menge der Zerlegungen einer Menge kann mit der Funktion
`stirling2` ermittelt werden.



```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) cardinality(p) = stirling2 (6, 3);
(%o3)                        90 = 90
```


Jedes Element der Menge `p` hat 3 Elemente.



```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (cardinality, p);
(%o3)                          {3}
```


Fur jedes Element der Menge `p`, ist die Vereinigung ihrer Elemente
gleich der Menge `s`.



```maxima
(%i1) s: {0, 1, 2, 3, 4, 5}$
(%i2) p: set_partitions (s, 3)$ 
(%i3) map (lambda ([x], apply (union, listify (x))), p);
(%o3)                 {{0, 1, 2, 3, 4, 5}}
```

See also: `stirling2`.

<!-- category: Other -->
<!-- keywords: setdifference -->
<!-- signatures: setdifference(a, b) -->
### Function: setdifference (a, b)

Gibt eine Menge mit den Elementen zuruck, die in der Menge *a*, aber nicht
in der Menge *b* enthalten sind.


`setdifference` gibt eine Fehlermeldung, wenn die Argumente *a* oder
*b* keine Mengen sind.


Beispiele:



```maxima
(%i1) S_1 : {a, b, c, x, y, z};
(%o1)                  {a, b, c, x, y, z}
(%i2) S_2 : {aa, bb, c, x, y, zz};
(%o2)                 {aa, bb, c, x, y, zz}
(%i3) setdifference (S_1, S_2);
(%o3)                       {a, b, z}
(%i4) setdifference (S_2, S_1);
(%o4)                     {aa, bb, zz}
(%i5) setdifference (S_1, S_1);
(%o5)                          {}
(%i6) setdifference (S_1, {});
(%o6)                  {a, b, c, x, y, z}
(%i7) setdifference ({}, S_1);
(%o7)                          {}
```

<!-- category: Other -->
<!-- keywords: setequalp -->
<!-- signatures: setequalp(a, b) -->
### Function: setequalp (a, b)

Gibt das Ergebnis `true` zuruck, wenn die Mengen *a* und *b*
dieselbe Anzahl an Elementen haben und der Ausdruck `is(x = y)`
das Ergebnis `true` fur alle Elemente *x* der Menge *a* und
*y* der Menge *b* hat.  Dabei haben die Elemente eine Ordnung wie sie
von der Funktion `listify` generiert wird.  Ansonsten ist das Ergebnis
`false`.


Beispiele:



```maxima
(%i1) setequalp ({1, 2, 3}, {1, 2, 3});
(%o1)                         true
(%i2) setequalp ({a, b, c}, {1, 2, 3});
(%o2)                         false
(%i3) setequalp ({x^2 - y^2}, {(x + y) * (x - y)});
(%o3)                         false
```

<!-- category: Other -->
<!-- keywords: setify -->
<!-- signatures: setify(a) -->
### Function: setify (a)

Konstruiert eine Menge aus den Elementen der Liste *a*.  Doppelte Elemente
der Liste *a* werden entfernt und die Elemente werden mit der
Aussagefunktion `orderlessp` sortiert.


`setify` gibt eine Fehlermeldung, wenn *a* keine Liste ist.


Beispiele:



```maxima
(%i1) setify ([1, 2, 3, a, b, c]);
(%o1)                  {1, 2, 3, a, b, c}
(%i2) setify ([a, b, c, a, b, c]);
(%o2)                       {a, b, c}
(%i3) setify ([7, 13, 11, 1, 3, 9, 5]);
(%o3)                {1, 3, 5, 7, 9, 11, 13}
```

See also: `orderlessp`.

<!-- category: Other -->
<!-- keywords: setp -->
<!-- signatures: setp(a) -->
### Function: setp (a)

Gibt das Ergebnis `true` zuruck, wenn das Argument *a* eine Menge
ist.


`setp` gibt `true` auch fur Mengen zuruck, die noch nicht
vereinfacht sind, also moglicherweise doppelte Elemente enthalten.


`setp` ist aquivalent zu dem Kommando `setp(a) := not atom(a) and op(a) = 'set`.


Beispiele:



```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) {a, a, a};
(%o2)                       {a, a, a}
(%i3) setp (%);
(%o3)                         true
```

<!-- category: Other -->
<!-- keywords: some -->
<!-- signatures: some(f, a), some(f, L_1, ..., L_n) -->
### Function: some (f, a)

Gibt das Ergebnis `true` zuruck, wenn die Aussage *f* das Ergebnis
`true` fur eines oder mehrere Argumente hat.


Ist eine Menge *a* als Argument gegeben, gibt `some(f, s)`
das Ergebnis `true` zuruck, wenn `is(f(a_i))` das Ergebnis
`true` fur eines oder mehrere Elemente *a_i* der Menge *a* hat.
`some` wertet *f* nicht notwendigerweise fur alle Elemente *a_i*
aus, wenn das Ergebnis bereits feststeht.  Da Mengen nicht geordnet sind, kann
die Funktion `some` die Ausdrucke `f(a_i)` in
irgendeiner Reihenfolge auswerten.


Sind die Argumente eine oder mehrere Listen, dann gibt
`some(f, L_1, ..., L_n)` den Wert `true` zuruck,
wenn `is(f(x_1, ..., x_n))` das Ergebnis `true`
fur eines oder mehrere Elemente *x_1*, ..., *x_n* der Listen
*L_1*, ..., *L_n* hat.  `some` wertet *f* wird nicht
notwendigerweise fur alle Kombinationen *x_1*, ..., *x_n* aus,
wenn das Ergebnis bereits feststeht.  `some` wertet die Listen in der
Reihenfolge des steigenden Index aus.


Ist die leere Menge `{}` oder die leere Liste  `[]` unter den 
Argumenten, ist das Ergebnis immer `false`.


Hat die Optionsvariable `maperror` den Wert `true`, mussen alle
Listen *L_1*, ..., *L_n* die gleiche Lange haben.  Hat die
Optionsvariable `maperror` den Wert `false`, werden Listen auf die
Lange der kurzesten Liste abgeschnitten.


Kann die Aussagefunktion *f* von der Funktion `is` nicht zu `true`
oder `false` ausgewertet werden, hangt das Ergebnis von der
Optionsvariablen `prederror` ab.  Hat die Optionsvariable `prederror`
den Wert `true`, werden solche Werte als `false` behandelt.  Hat
`prederror` den Wert `false`, werden solche Werte als `unknown`
behandelt.


Beispiele:


`some` fur eine Menge als Argument.  Die Aussage ist eine Funktion mit
einem Argument.



```maxima
(%i1) some (integerp, {1, 2, 3, 4, 5, 6});
(%o1)                         true
(%i2) some (atom, {1, 2, sin(3), 4, 5 + y, 6});
(%o2)                         true
```


`some` angewendet auf zwei Listen.  Die Aussage ist eine Funktion mit
zwei Argumenten.



```maxima
(%i1) some ("=", [a, b, c], [a, b, c]);
(%o1)                         true
(%i2) some ("#", [a, b, c], [a, b, c]);
(%o2)                         false
```


Ergebnisse der Aussage *f*, die zu einem Ergebnis verschieden von
`true` oder `false` auswerten,  werden von der Optionsvariablen
`prederror` kontrolliert.



```maxima
(%i1) prederror : false;
(%o1)                         false
(%i2) map (lambda ([a, b], is (a < b)), [x, y, z],
           [x^2, y^2, z^2]);
(%o2)              [unknown, unknown, unknown]
(%i3) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o3)                        unknown
(%i4) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o4)                         true
(%i5) prederror : true;
(%o5)                         true
(%i6) some ("<", [x, y, z], [x^2, y^2, z^2]);
(%o6)                         false
(%i7) some ("<", [x, y, z], [x^2, y^2, z + 1]);
(%o7)                         true
```

See also: `maperror`, `prederror`.

<!-- category: Other -->
<!-- keywords: stirling1 -->
<!-- signatures: stirling1(n, m) -->
### Function: stirling1 (n, m)

Berechnet Stirling-Zahlen der ersten Art.


Sind die Argumente *n* und *m* naturliche Zahlen, ist der Wert von
`stirling1(n, m)` die Anzahl der Permutationen einer Menge
mit *n* Elementen, die *m* Zyklen hat.  Fur Details siehe Graham,
Knuth und Patashnik in *Conrecte Mathematics*.  Maxima nutzt eine Rekursion,
um `stirling1(n, m)` fur *m* kleiner als `0` zu
berechnen.  Die Funktion ist nicht definiert fur `n` kleiner als `0`
und fur Argumente die keine ganze Zahlen sind.


`stirling1` ist eine vereinfachende Funktion.  Maxima kennt die folgenden
Beziehungen (siehe [1]).



- *
`stirling1(0, n) = kron_delta(0, n)`
- *
`stirling1(n, n) = 1`
- *
`stirling1(n, n - 1) = binomial(n, 2)`
- *
`stirling1(n + 1, 0) = 0`
- *
`stirling1(n + 1, 1) = n!`
- *
`stirling1(n + 1, 2) = 2^n - 1`


Diese Beziehungen werden angewendet, wenn die Argumente ganze Zahlen oder
Symbole sind, die als ganze Zahlen deklariert sind, und das erste Argument
keine negative Zahl ist.  `stirling1` vereinfacht nicht fur Argumente,
die keine ganzen Zahlen sind.


Referenz:


[1] Donald Knuth, *The Art of Computer Programming,*
third edition, Volume 1, Section 1.2.6, Equations 48, 49, and 50.


Beispiele:



```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n, n);
(%o3)                           1
```


`stirling1` vereinfacht nicht fur Argumente, die keine ganzen Zahlen
sind.



```maxima
(%i1) stirling1 (sqrt(2), sqrt(2));
(%o1)              stirling1(sqrt(2), sqrt(2))
```


Maxima kennt Vereinfachungen der Funktion `stirling1`.



```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling1 (n + 1, n);
                            n (n + 1)
(%o3)                       ---------
                                2
(%i4) stirling1 (n + 1, 1);
(%o4)                          n!
```

<!-- category: Other -->
<!-- keywords: stirling2 -->
<!-- signatures: stirling2(n, m) -->
### Function: stirling2 (n, m)

Berechnet Stirling-Zahlen der zweiten Art.


Sind die Argumente *n* und *m* naturliche Zahlen, ist der Wert von
`stirling2(n, m)` die Anzahl der Moglichkeiten, mit der eine
Menge der Machtigkeit *n* in *m* disjunkte Mengen zerlegt werden kann.
Maxima nutzt eine Rekursion, um `stirling2(n, m)` fur *m*
kleiner als `0` zu berechnen.  Die Funktion ist nicht definiert fur
`n` kleiner als `0` und fur Argumente, die keine ganze Zahlen sind.


`stirling2` ist eine vereinfachende Funktion.  Maxima kennt die folgenden
Beziehungen (siehe [1], [2], [3]).



- *
`stirling2(0, n) = kron_delta(0, n)`
- *
`stirling2(n, n) = 1`
- *
`stirling2(n, n - 1) = binomial(n, 2)`
- *
`stirling2(n + 1, 1) = 1`
- *
`stirling2(n + 1, 2) = 2^n - 1`
- *
`stirling2(n, 0) = kron_delta(n, 0)`
- *
`stirling2(n, m) = 0` fur `m > n`
- *
`stirling2(n, m) = sum((-1)^(m - k) binomial(m k) k^n,i,1,m) / m!`, wenn
$m$ und $n$ ganze Zahlen und $n$ eine naturliche Zahl ist.


Diese Beziehungen werden angewendet, wenn die Argumente ganze Zahlen oder
Symbole sind, die als ganze Zahlen deklariert sind, und das erste Argument
keine negative Zahl ist.  `stirling2` vereinfacht nicht fur Argumente,
die keine ganzen Zahlen sind.


Referenzen:


[1] Donald Knuth.  *The Art of Computer Programming*,
    third edition, Volume 1, Section 1.2.6, Equations 48, 49, and 50.


[2] Graham, Knuth, and Patashnik.  *Concrete Mathematics*, Table 264.


[3] Abramowitz and Stegun.  *Handbook of Mathematical Functions*,
    Section 24.1.4.


Beispiele:



```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n, n);
(%o3)                           1
```


`stirling2` vereinfacht nicht, wenn die Argumente keine ganze Zahlen sind.



```maxima
(%i1) stirling2 (%pi, %pi);
(%o1)                  stirling2(%pi, %pi)
```


Maxima kennt Vereinfachungen der Funktion `stirling2`.



```maxima
(%i1) declare (n, integer)$
(%i2) assume (n >= 0)$
(%i3) stirling2 (n + 9, n + 8);
                         (n + 8) (n + 9)
(%o3)                    ---------------
                                2
(%i4) stirling2 (n + 1, 2);
                              n
(%o4)                        2  - 1
```

<!-- category: Other -->
<!-- keywords: subset -->
<!-- signatures: subset(a, f) -->
### Function: subset (a, f)

Gibt eine Teilmenge der Menge *a* zuruck, deren Elemente der Bedingung
*f* genugen.


`subset` gibt eine Menge zuruck, die alle Elemente der Menge *a*
enthalt, die fur die Bedingung *f* ein von `false` verschiedenes
Ergebnis haben.  `subset` wendet nicht die Funktion `is` auf das
Ergebnis der Bedingung `f` an.


`subset` gibt eine Fehlermeldung, wenn das Argument *a* keine Menge
ist.


Siehe auch die Funktion `partition_set`.


Beispiele:



```maxima
(%i1) subset ({1, 2, x, x + y, z, x + y + z}, atom);
(%o1)                     {1, 2, x, z}
(%i2) subset ({1, 2, 7, 8, 9, 14}, evenp);
(%o2)                      {2, 8, 14}
```

See also: `partition_set`.

<!-- category: Other -->
<!-- keywords: subsetp -->
<!-- signatures: subsetp(a, b) -->
### Function: subsetp (a, b)

Gibt das Ergebnis `true` zuruck, wenn die Menge *a* einer Teilmenge
der Menge *b* ist.


`subsetp` gibt eine Fehlermeldung, wenn eines der Argumente keine Menge
ist.


Beispiele:



```maxima
(%i1) subsetp ({1, 2, 3}, {a, 1, b, 2, c, 3});
(%o1)                         true
(%i2) subsetp ({a, 1, b, 2, c, 3}, {1, 2, 3});
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: symmdifference -->
<!-- signatures: symmdifference(a_1, ..., a_n) -->
### Function: symmdifference (a_1, ..., a_n)

Gibt die symmetrische Differenz der Mengen `a_1, ..., a_n`
zuruck.  Fur zwei Argumente ist die symmetrische Differenz aquivalent zu
`union(setdifference(a, b), setdifference(b, a))`.


`symmdifference` gibt eine Fehlermeldung, wenn eines der Argumente keine
Menge ist.


Beispiele:



```maxima
(%i1) S_1 : {a, b, c};
(%o1)                       {a, b, c}
(%i2) S_2 : {1, b, c};
(%o2)                       {1, b, c}
(%i3) S_3 : {a, b, z};
(%o3)                       {a, b, z}
(%i4) symmdifference ();
(%o4)                          {}
(%i5) symmdifference (S_1);
(%o5)                       {a, b, c}
(%i6) symmdifference (S_1, S_2);
(%o6)                        {1, a}
(%i7) symmdifference (S_1, S_2, S_3);
(%o7)                        {1, b, z}
(%i8) symmdifference ({}, S_1, S_2, S_3);
(%o8)                        {1,b, z}
```

<!-- category: Other -->
<!-- keywords: tree_reduce -->
<!-- signatures: tree_reduce(F, s), tree_reduce(F, s, s_0) -->
### Function: tree_reduce (F, s)

Wendet eine Funktion *F*, die zwei Argumente hat, auf die Elemente einer
Liste oder Menge *s* an, indem die Funktionsaufrufe verkettet werden.


`tree_reduce` fuhrt folgende Operationen aus: Die Funktion *F* wird
auf Paare von Elementen der Liste *s* angewendet, wodurch die neue Liste
`[F(s_1, s_2), F(s_3, s_4), ...]`
entsteht.  Hat die Liste eine ungerade Anzahl an Elementen, bleibt das letzte
Element unverandert.  Dann wird das Verfahren solange wiederholt, bis nur noch
ein einziges Element ubrig ist.  Dieses wird als Ergebnis zuruckgegeben.


Ist das optionale Argument *s_0* vorhanden, dann ist das Ergebnis 
aquivalent zu `tree_reduce(F, cons(s_0, s)`.


Werden Gleitkommazahlen addiert, dann kann `tree_reduce` ein Ergebnis
mit einem kleineren Rundungsfehler als `lreduce` oder `rreduce`
liefern.


Siehe auch `lreduce`, `rreduce` und `xreduce`.


Beispiele:


`tree_reduce` angewendet auf eine Liste mit einer geraden Anzahl an
Elementen.



```maxima
(%i1) tree_reduce (f, [a, b, c, d]);
(%o1)                  f(f(a, b), f(c, d))
```


`tree_reduce` angewendet auf eine List mit einer ungeraden Anzahl an
Elementen.



```maxima
(%i1) tree_reduce (f, [a, b, c, d, e]);
(%o1)               f(f(f(a, b), f(c, d)), e)
```

See also: `lreduce`, `rreduce`, `xreduce`.

<!-- category: Other -->
<!-- keywords: union -->
<!-- signatures: union(a_1, ..., a_n) -->
### Function: union (a_1, ..., a_n)

Gibt die Vereinigung der Mengen *a_1*, ..., *a_n* zuruck.  Wird
`union` ohne ein Argument aufgerufen, wird die leere Menge zuruckgegeben.


`union` gibt eine Fehlermeldung, wenn eines der Argumente keine Menge ist.


Beispiele:



```maxima
(%i1) S_1 : {a, b, c + d, %e};
(%o1)                   {%e, a, b, d + c}
(%i2) S_2 : {%pi, %i, %e, c + d};
(%o2)                 {%e, %i, %pi, d + c}
(%i3) S_3 : {17, 29, 1729, %pi, %i};
(%o3)                {17, 29, 1729, %i, %pi}
(%i4) union ();
(%o4)                          {}
(%i5) union (S_1);
(%o5)                   {%e, a, b, d + c}
(%i6) union (S_1, S_2);
(%o6)              {%e, %i, %pi, a, b, d + c}
(%i7) union (S_1, S_2, S_3);
(%o7)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
(%i8) union ({}, S_1, S_2, S_3);
(%o8)       {17, 29, 1729, %e, %i, %pi, a, b, d + c}
```

<!-- category: Other -->
<!-- keywords: xreduce -->
<!-- signatures: xreduce(F, s), xreduce(F, s, s_0) -->
### Function: xreduce (F, s)

Wendet eine Funktion *F*, die zwei Argumente hat, auf die Elemente einer
Liste oder Menge *s* an, indem die Funktionsaufrufe verkettet werden.  Ist
die Funktion eine N-ary-Funktion wird die Funktion *F* auf die Liste
angewendet.  Ist die Funktion *F* keine N-ary_Funktion ist `xreduce`
aquivalent zu `lreduce`.


Folgende N-ary-Funktionen und Operatoren kennt `xreduce`:
Addition `"+"`, Multiplikation `"*"`, `and`, `or`,
`max`, `min` und `append`.  Funktionen und Operatoren konnen
mit der Funktion `declare` als `nary` deklariert werden.  Fur diese
Funktionen ist `xreduce` schneller als `lreduce` oder
`rreduce`.


Ist das optionale Argument *s_0* vorhanden, dann ist das Ergebnis 
aquivalent zu `xreduce(s, cons(s_0, s))`.


Siehe auch `lreduce`, `rreduce` und `tree_reduce`.


Beispiele:


`xreduce` angewendet mit einer N-ary-Funktion.  `F` wird einmal mit
allen Argumenten aufgerufen.



```maxima
(%i1) declare (F, nary);
(%o1)                         done
(%i2) F ([L]) := L;
(%o2)                      F([L]) := L
(%i3) xreduce (F, [a, b, c, d, e]);
(%o3)         [[[[[("[", simp), a], b], c], d], e]
```


`xreduce` angewendet mit einer Funktion, die nicht die Eigenschaft 
`nary` hat.



```maxima
(%i1) G ([L]) := L;
(%o1)                      G([L]) := L
(%i2) xreduce (G, [a, b, c, d, e]);
(%o2)         [[[[[("[", simp), a], b], c], d], e]
(%i3) lreduce (G, [a, b, c, d, e]);
(%o3)                 [[[[a, b], c], d], e]
```

See also: `lreduce`, `declare`, `nary`, `rreduce`, `tree_reduce`.

