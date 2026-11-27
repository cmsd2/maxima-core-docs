## Ausdrucke

<!-- category: Other -->
<!-- keywords: alias -->
<!-- signatures: alias(new_name_1, old_name_1, ..., new_name_n, old_name_n) -->
### Function: alias (new_name_1, old_name_1, ..., new_name_n, old_name_n)

Die Funktion `alias` ermoglicht einen alternativen Alias-Namen fur eine 
Maxima-Funktion, einer Variablen oder einem Array.  Der Funktion `alias` 
kann eine beliebige Anzahl von paarweisen Namen und Alias-Namen ubergeben 
werden.


`alias` gibt eine Liste mit den Symbolen zuruck, denen ein Alias-Name
zugewiesen werden konnte.  Wurde einem Symbol bereits derselbe Alias-Name 
gegeben, enthalt die Liste den Wert `false`.  Wird versucht einem Symbol,
das bereits einen Alias-Namen hat, einen neuen Alias-Namen zu geben, bricht
`alias` mit einer Fehlermeldung ab.


Symbole, die einen Alias-Namen erhalten haben, werden in die Systemvariable 
`aliases` eingetragen.  Siehe die Systemvariable `aliases`.


Die Funktionen `ordergreat` und `orderless` sowie die Deklaration
eines Symbols als ein `noun` mit der Funktion `declare` erzeugen
automatisch Alias-Namen, die in die Liste `aliases` eingetragen werden.


Der Alias-Name kann mit der Funktion `kill` entfernt werden.


Beispiel:



```maxima
(%i1) alias(mysqrt,sqrt);
(%o1)                        [sqrt]
(%i2) aliases;
(%o2)                        [sqrt]
(%i3) mysqrt(4);
(%o3)                           2
(%i4) kill(mysqrt);
(%o4)                         done
(%i5) mysqrt(4);
(%o5)                       mysqrt(4)
(%i6) aliases;
(%o6)                          []
```

See also: `aliases`, `ordergreat`, `orderless`, `noun`, `declare`, `kill`.

<!-- category: Other -->
<!-- keywords: aliases -->
<!-- signatures: aliases -->
### Variable: aliases

Anfangswert: `[]`


Die Systemvariable `aliases` ist eine Informationsliste der Symbole, die 
einen vom Nutzer definierten Alias-Namen mit dem Kommando `alias` 
erhalten haben.  Weiterhin werden von den Funktionen `ordergreat` und 
`orderless` sowie bei der Deklaration eines Symbols als ein
`noun` mit der Funktion `declare` Alias-Namen generiert, die in die
Liste `aliases` eingetragen werden.


Siehe auch die Funktion `alias` fur ein Beispiel.

See also: `ordergreat`, `orderless`, `noun`, `declare`, `alias`.

<!-- category: Other -->
<!-- keywords: allbut -->
<!-- signatures: allbut -->
### Variable: allbut

Das Schlusselwort `allbut` wird bei `part`-Befehlen wie
`part`, `inpart`, `substpart`,
`substinpart`, `dpart` und `lpart` genutzt, um Indizes bei
der Auswahl von Teilausdrucken auszuschließen.


Das Schlusselwort `allbut` kann auch zusammen mit dem Kommando
`kill` verwendet werden.  `kill(allbut(a_1, a_2, ...))`
hat denselben Effekt wie `kill(all)` mit der Ausnahme, dass die Symbole 
*a_1*, *a_2*, ... von `kill` ausgenommen werden.  Siehe die 
Funktion `kill`.


Beispiele:



```maxima
(%i1) expr : e + d + c + b + a;
(%o1)                   e + d + c + b + a
(%i2) part (expr, [2, 5]);
(%o2)                         d + a

(%i3) expr : e + d + c + b + a;
(%o3)                   e + d + c + b + a
(%i4) part (expr, allbut (2, 5));
(%o4)                       e + c + b
```


Das Schlusselwort `allbut` kann zusammen mit dem Kommando `kill`
verwendet werden.



```maxima
(%i1) [aa : 11, bb : 22, cc : 33, dd : 44, ee : 55];
(%o1)                 [11, 22, 33, 44, 55]
(%i2) kill (allbut (cc, dd));
(%o0)                         done
(%i1) [aa, bb, cc, dd];
(%o1)                   [aa, bb, 33, 44]
```

See also: `part`, `inpart`, `substpart`, `substinpart`, `dpart`, `lpart`, `kill`.

<!-- category: Other -->
<!-- keywords: args -->
<!-- signatures: args(expr) -->
### Function: args (expr)

Die Funktion `args` gibt eine Liste mit den Argumenten des Hauptoperators
des Ausdrucks *expr* zuruck.


Die Anordnung der Argumente der Ergebnisliste wird von der Optionsvariablen
`inflag` beeinflußt.  Hat `inflag` den Wert `true`, ist die
Anordnung entsprechend der internen Darstellung des Ausdrucks *expr*.
Ansonsten ist die Anordnung wie in der externen Darstellung fur die Anzeige.
Siehe die Optionsvariable `inflag`.


`args(expr)` ist aquivalent zu 
`substpart("[", expr, 0)`.  Siehe auch `substpart` und 
`op`.


Beispiele:



```maxima
(%i1) args(gamma_incomplete(a,x));
(%o1)                        [a, x]
(%i2) args(x+y+z);
(%o2)                       [z, y, x]
(%i3) args(x+y+z),inflag:true;
(%o3)                       [x, y, z]
(%i4) args(x+2*a);
(%o4)                       [x, 2 a]
```

See also: `inflag`, `substpart`, `op`.

<!-- category: Other -->
<!-- keywords: atom -->
<!-- signatures: atom(expr) -->
### Function: atom (expr)

Gibt den Wert `true` zuruck, wenn das Argument *expr* ein Atom ist.
Atome sind ganze Zahlen, Gleitkommazahlen, Zeichenketten und Symbole.  Siehe
auch die Funktionen `symbolp` und `listp`.




Beispiele:



```maxima
(%i1) atom(5);
(%o1)                         true
(%i2) atom(5.0);
(%o2)                         true
(%i3) atom(5.0b0);
(%o3)                         true
(%i4) atom(1/2);
(%o4)                         false
(%i5) atom('a);
(%o5)                         true
(%i6) atom(2*x);
(%o6)                         false
(%i7) atom("string");
(%o7)                         true
```

See also: `symbolp`, `listp`.

<!-- category: Other -->
<!-- keywords: box -->
<!-- signatures: box(expr), box(expr, a) -->
### Function: box (expr)

Die Funktion `box(expr)` umschließt den Ausdruck *expr* in 
der Ausgabe mit einem Rahmen, wenn `display2d` den Wert `true` hat.
Ansonsten ist der Ruckgabewert ein Ausdruck mit `box` als Operator und 
*expr* als Argument.


`box(expr, a)` umschließt *expr* mit einem Rahmen, der
mit einer Marke *a* bezeichnet ist.  Ist die Marke langer als der Rahmen,
werden Zeichen abgeschnitten.


Die Funktion `box` wertet ihre Argumente aus.  Die eingerahmten Ausdrucke
werden dagegen nicht mehr ausgewertet.


Die Optionsvariable `boxchar` enthalt das Zeichen, das von den Funktionen
`box` sowie `dpart` und `lpart` verwendet wird, um den Rahmen
auszugeben.


Beispiele:



```maxima
(%i1) box (a^2 + b^2);
                            """""""""
                            " 2    2"
(%o1)                       "b  + a "
                            """""""""
(%i2) a : 1234;
(%o2)                         1234
(%i3) b : c - d;
(%o3)                         c - d
(%i4) box (a^2 + b^2);
                      """"""""""""""""""""
                      "       2          "
(%o4)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i5) box (a^2 + b^2, term_1);
                      term_1""""""""""""""
                      "       2          "
(%o5)                 "(c - d)  + 1522756"
                      """"""""""""""""""""
(%i6) 1729 - box (1729);
                                 """"""
(%o6)                     1729 - "1729"
                                 """"""
```

See also: `boxchar`, `dpart`, `lpart`.

<!-- category: Other -->
<!-- keywords: boxchar -->
<!-- signatures: boxchar -->
### Variable: boxchar

Standardwert: `"`


Die Optionsvariable `boxchar` enthalt das Zeichen, welches von den 
Funktionen `box` sowie `dpart` und `lpart` genutzt wird, um
einen Rahmen auszugeben.


Die Rahmen werden immer mit dem aktuellen Wert von `boxchar` ausgegeben.
Das Zeichen `boxchar` wird nicht zusammen mit dem eingerahmten Ausdruck
gespeichert.

See also: `box`, `dpart`, `lpart`.

<!-- category: Other -->
<!-- keywords: collapse -->
<!-- signatures: collapse(expr), collapse([expr_1, expr_2, ...]) -->
### Function: collapse (expr)

Komprimiert einen Ausdruck *expr*, indem gemeinsame Teilausdrucke 
denselben Speicher nutzen.  `collapse` wird von der Funktion 
`optimize` aufgerufen.  `collapse` kann auch mit einer Liste 
aufgerufen werden, die mehrere Argumente enthalt.




Siehe auch die Funktion `optimize`.

See also: `optimize`.

<!-- category: Other -->
<!-- keywords: disolate -->
<!-- signatures: disolate(expr, x_1, ..., x_n) -->
### Function: disolate (expr, x_1, ..., x_n)

Die Funktion `disolate` arbeitet ahnlich wie die Funktion `isolate`.
Teilausdrucke im Ausdruck *expr*, die die Variablen *x_1*, ..., 
*x_n* nicht enthalten, werden durch Zwischenmarken `%t1`, `%t2`, 
... ersetzt.  Im Unterschied zu der Funktion `isolate` kann die
Funktion `disolate` Teilausdrucke zu mehr als einer Variablen aus einem
Ausdruck isolieren.


Die Ersetzung von Teilausdrucken durch Zwischenmarken kann mit der 
Optionsvariable `isolate_wrt_times` kontrolliert werden.  Hat die
Optionsvariable `isolate_wrt_times` den Wert `true`, werden 
Ersetzungen in Produkten ausgefuhrt.  Der Standardwert ist `false`.
Siehe `isolate_wrt_times` fur Beispiele.


Die Optionsvariable `exptisolate` hat im Unterschied zur Funktion
`isolate` keinen Einfluss auf die Ersetzung von Teilausdrucken durch
Zwischenmarken.


`disolate` wird automatisch aus der Datei
`share/simplification/disol.mac` geladen.  Das Kommando 
`demo(disol)$` zeigt Beispiele.


Siehe auch die Funktion `isolate`.


Beispiel:



```maxima
(%i1) expr:a*(e*(g+f)+b*(d+c));
(%o1)               a (e (g + f) + b (d + c))
(%i2) disolate(expr,a,b,e);
(%t2)                         d + c

(%t3)                         g + f

(%o3)                   a (%t3 e + %t2 b)
```

See also: `isolate_wrt_times`, `exptisolate`, `isolate`.

<!-- category: Other -->
<!-- keywords: dispform -->
<!-- signatures: dispform(expr), dispform(expr, all) -->
### Function: dispform (expr)

`dispform` formatiert den Ausdruck *expr* von der internen Darstellung
in eine externe Darstellung, wie sie fur die Anzeige des Ausdrucks benotigt 
wird.  Bei der Formatierung sind Optionsvariablen wie `dispflag` und
`powerdisp` wirksam.


Beispiele fur die interne und externe Darstellung von Ausdrucken sind:



```maxima
Interne Darstellung            Externe Darstellung
------------------------------------------------------------
-x      : ((MTIMES) -1 $x)               ((MMINUS) $x)
sqrt(x) : ((MEXPT) $x ((RAT) 1 2))       ((%SQRT) $X)
a/b     : ((MTIMES) $A ((MEXPT) $B -1))  ((MQUOTIENT) $A $B)
```


`dispform(expr)` gibt die externe Darstellung nur fur den ersten 
Operator im Ausdruck zuruck.  `dispform(expr, all)` gibt die 
externe Darstellung aller Operatoren im Ausdruck *expr* zuruck.


Siehe auch `part`, `inpart` und `inflag`.


Beispiel:


Die Funktion `dispform` kann genutzt werden, um die Wurzelfunktion in
einem Ausdruck zu substituieren.  Die Wurzelfunktion ist nur in der externen
Darstellung eines Ausdruckes vorhanden:



```maxima
(%i1) expr: sqrt(5)/(5+sqrt(2));
                             sqrt(5)
(%o1)                      -----------
                           sqrt(2) + 5
(%i2) subst(f,sqrt,expr);
                             sqrt(5)
(%o2)                      -----------
                           sqrt(2) + 5
(%i3) subst(f,sqrt,dispform(expr));
                              f(5)
(%o3)                      -----------
                           sqrt(2) + 5
(%i4) subst(f,sqrt,dispform(expr,all));
                              f(5)
(%o4)                       --------
                            f(2) + 5
```

See also: `dispflag`, `powerdisp`, `part`, `inpart`, `inflag`.

<!-- category: Other -->
<!-- keywords: dpart -->
<!-- signatures: dpart(expr, n_1, ..., n_k) -->
### Function: dpart (expr, n_1, ..., n_k)

Wahlt wie die Funktion `part` einen Teilausdruck aus, gibt aber den 
vollstandigen Ausdruck zuruck, wobei der ausgewahlte Teilausdruck 
eingerahmt ist.  Der Rahmen ist Teil des zuruckgegebenen Ausdrucks.


Siehe auch `part`, `inpart` und `lpart` sowie `box`.


Beispiel:



```maxima
(%i1) dpart (x+y/z^2, 1, 2, 1);
                             y
(%o1)                       ---- + x
                               2
                            """
                            "z"
                            """
```

See also: `part`, `inpart`, `lpart`, `box`.

<!-- category: Other -->
<!-- keywords: exptisolate -->
<!-- signatures: exptisolate -->
### Variable: exptisolate

Standardwert: `false`


Hat `exptisolate` den Wert `true`, dann sucht die Funktion
`isolate` auch in den Exponenten von Zahlen oder Symbolen nach
Teilausdrucken zu einer Variablen.


Siehe die Funktion `isolate` fur Beispiele.

See also: `isolate`.

<!-- category: Other -->
<!-- keywords: exptsubst -->
<!-- signatures: exptsubst -->
### Variable: exptsubst

Standardwert: `false`


Die Optionsvariable `exptsubst` kontrolliert die Substitution von
Ausdrucken mit der Exponentialfunktion durch die Funktionen `subst` und
`psubst`.


Beispiele:



```maxima
(%i1) subst(y,%e^x,%e^(a*x)),exptsubst:false;
                                a x
(%o1)                         %e
(%i2) subst(y,%e^x,%e^(a*x)),exptsubst:true;
                                a
(%o2)                          y
```

See also: `subst`, `psubst`.

<!-- category: Other -->
<!-- keywords: freeof -->
<!-- signatures: freeof(x, expr), freeof(x_1, ..., x_n, expr) -->
### Function: freeof (x, expr)

`freeof(x, expr)` gibt das Ergebnis `true` zuruck, wenn
das Argument *x* nicht im Ausdruck *expr* enthalten ist.  Ansonsten ist
der Ruckgabewert `false`.


`freeof(x_1, ..., x_n, expr)` gibt das Ergebnis 
`true` zuruck, wenn keines der Argumente *x_1*, *x_2*, ...
im Ausdruck *expr* enthalten ist.


Die Argumente *x_1*, ..., *x_n* konnen die Namen von Funktionen 
und Variablen sein, indizierte Namen, die Namen von Operatoren oder allgemeine
Ausdrucke.  Die Funktion `freeof` wertet die Argumente aus.


Bei der Prufung, ob ein Teilausdruck *x* im Ausdruck *expr* enthalten
ist, untersucht die Funktion `freeof` den Ausdruck *expr* in der 
vorliegenden Form (nach Auswertung und Vereinfachung) und versucht nicht 
herauszufinden, ob der Teilausdruck in einem aquivalenten Ausdruck enthalten
ware.


`freeof` ignoriert Dummy-Variablen.  Dummy-Variablen sind Variablen, die 
außerhalb eines Ausdrucks nicht in Erscheinung treten.  Folgende 
Dummy-Variablen werden von `freeof` ignoriert: der Index einer Summe oder 
eines Produktes, die unabhangige Variable in einem Grenzwert, die 
Integrationsvariable eines bestimmten Integrals oder einer 
Laplacetransformation, formale Variablen in `at`- oder
`lambda`-Ausdrucke, lokale Variablen eines Blocks oder einer
`do`-Schleife.


Das unbestimmte Integral ist *nicht* frei von der Integrationsvariablen.


Beispiele:


Argumente sind Namen von Funktionen, Variablen, indizierten Variablen, 
Operatoren und Ausdrucke.  `freeof(a, b, expr)` ist aquivalent zu
`freeof(a, expr) and freeof(b, expr)`.



```maxima
(%i1) expr: z^3 * cos (a[1]) * b^(c+d);

                                 d + c  3
(%o1)                   cos(a ) b      z
                             1

(%i2) freeof(z, expr);
(%o2)                         false
(%i3) freeof(cos, expr);
(%o3)                         false
(%i4) freeof(a[1], expr);
(%o4)                         false
(%i5) freeof(cos (a[1]), expr);
(%o5)                         false
(%i6) freeof(b^(c+d), expr);
(%o6)                         false
(%i7) freeof("^", expr);
(%o7)                         false
(%i8) freeof(w, sin, a[2], sin (a[2]), b*(c+d), expr);
(%o8)                         true
```


Die Funktion `freeof` wertet die Argumente aus.



```maxima
(%i1) expr: (a+b)^5$
(%i2) c: a$
(%i3) freeof(c, expr);
(%o3)                         false
```


`freeof` betrachtet keine aquivalenten Ausdrucke.  Vereinfachungen 
konnen einen aquivalenten Ausdruck liefern, der jedoch den Teilausdruck 
nicht mehr enthalt.



```maxima
(%i1) expr: (a+b)^5$
(%i2) expand(expr);
          5        4       2  3       3  2      4      5
(%o2)    b  + 5 a b  + 10 a  b  + 10 a  b  + 5 a  b + a
(%i3) freeof(a+b, %);
(%o3)                         true
(%i4) freeof(a+b, expr);
(%o4)                         false
```


Die Exponentialfunktion `exp(x)` wird von Maxima sofort zu `%e^x` 
vereinfacht.  Der Name `exp` der Exponentialfunktion ist daher nicht in
einem Ausdruck enthalten.



```maxima
(%i5) exp(x);
                                 x
(%o5)                          %e
(%i6) freeof(exp, exp (x));
(%o6)                         true
```


Eine Summe ist frei von dem Index und ein bestimmtes Integral ist frei von der
Integrationsvariablen.  Ein unbestimmtes Integral ist nicht frei von der 
Integrationsvariablen.



```maxima
(%i1) freeof(i, 'sum (f(i), i, 0, n));
(%o1)                         true
(%i2) freeof(x, 'integrate (x^2, x, 0, 1));
(%o2)                         true
(%i3) freeof(x, 'integrate (x^2, x));
(%o3)                         false
```

See also: `at`, `lambda`, `do`.

<!-- category: Other -->
<!-- keywords: inflag -->
<!-- signatures: inflag -->
### Variable: inflag

Standardwert: `false`


Hat die Optionsvariable `inflag` den Wert `true`, wird von Funktionen,
die Teile eines Ausdrucks `expr` extrahieren, die interne Form des
Ausdrucks `expr` betrachtet.


Die Anordnung der Argumente der internen Darstellung unterscheidet sich zum
Beispiel fur die Addition von der externen Darstellung fur die Anzeige.
Daher hat `first(x+y)` das Ergebnis `x`, wenn `inflag` den Wert
`true` hat, und `y`, wenn `inflag` den Wert `false` hat.
Der Ausdruck `first(y+x)` gibt in beiden Fallen dasselbe Ergebnis.


Hat `inflag` den Wert `true`, entsprechen die Funktionen `part` 
und `substpart` den Funktionen `inpart` und `substinpart`.


Folgende Funktionen werden von der Optionsvariablen `inflag` beeinflusst:
`part`, `substpart`, `first`, `rest`,
`last`, `length`, die Konstruktion `for` ...
`in`, `map`, `fullmap`, `maplist`,
`reveal`, `pickapart`, `args` und `op`.

See also: `part`, `substpart`, `first`, `rest`, `last`, `length`, `for`, `map`, `fullmap`, `maplist`, `reveal`, `pickapart`, `args`, `op`.

<!-- category: Other -->
<!-- keywords: inpart -->
<!-- signatures: inpart(expr, n_1, ..., n_k) -->
### Function: inpart (expr, n_1, ..., n_k)

Die Funktion `inpart` ist ahnlich wie `part`, arbeitet aber mit der 
internen Darstellung eines Ausdruckes und nicht mit der externen Darstellung 
fur die Anzeige.  Da keine Formatierung vorgenommen wird, ist die Funktion 
`inpart` schneller als `part`.


Immer dann, wenn sich die interne und die externe Darstellung eines Ausdrucks
voneinander unterscheiden, haben die Funktionen `inpart` und `part`
verschiedene Ergebnisse.  Dies trifft zu fur die Anordnung der Argumente einer
Addition, der Subtraktion und Division sowie zum Beispiel fur die 
Wurzelfunktion.


Ist das letzte Argument einer `part`-Funktion eine Liste mit Indizes, 
werden mehrere Teilausdrucke heraus gepickt.  So hat
`inpart(x + y + z, [1, 3])` das Ergebnis `z+x`.


Siehe auch `part`, `dpart` und `lpart`.


Beispiele:



```maxima
(%i1) x + y + w*z;
(%o1)                      w z + y + x
(%i2) inpart (%, 3, 2);
(%o2)                           z
(%i3) part (%th (2), 1, 2);
(%o3)                           z
(%i4) 'limit (f(x)^g(x+1), x, 0, minus);
                                  g(x + 1)
(%o4)                 limit   f(x)
                      x -> 0-
(%i5) inpart (%, 1, 2);
(%o5)                       g(x + 1)
```

See also: `part`, `dpart`, `lpart`.

<!-- category: Other -->
<!-- keywords: isolate -->
<!-- signatures: isolate(expr, x) -->
### Function: isolate (expr, x)

Teilausdrucke im Ausdruck *expr*, die die Variable *x* nicht 
enthalten, werden durch Zwischenmarken `%t1`, `%t2`, ... ersetzt.
Dies kann genutzt werden, um die weitere Auswertung und Vereinfachung dieser
Teilausdrucke zu verhindern.  Die Ersetzung der Teilausdrucke kann durch 
eine Auswertung des Ausdrucks ruckgangig gemacht werden.


Die Ersetzung von Teilausdrucken kann mit den Optionsvariablen 
`exptisolate` und `isolate_wrt_times` kontrolliert werden.  Hat die
Optionsvariable `exptisolate` den Wert `true`, werden Ersetzungen auch
fur die Exponentiation ausgefuhrt.  Die Basis muss dabei eine Zahl oder ein 
Symbol wie `%e` sein.  Hat die Optionsvariable `isolate_wrt_times` den 
Wert `true`, werden Ersetzungen in Produkten ausgefuhrt.  Siehe
`isolate_wrt_times` fur Beispiele.


Die Ersetzung von Teilausdrucken fur mehrere Variable kann mit der Funktion
`disolate` ausgefuhrt werden.  Siehe `disolate`.


Beispiele:



```maxima
(%i1) (b+a)^4*(x*((d+c)^2+2*x)+1);
                       4                  2
(%o1)           (b + a)  (x (2 x + (d + c) ) + 1)
(%i2) isolate(%,x);

                                   2
(%t2)                       (d + c)


                                   4
(%t3)                       (b + a)

(%o3)                %t3 (x (2 x + %t2) + 1)
(%i4) ratexpand(%);
                          2
(%o4)              2 %t3 x  + %t2 %t3 x + %t3
(%i5) ev(%);
                  4  2          4        2            4
(%o5)    2 (b + a)  x  + (b + a)  (d + c)  x + (b + a)
(%i6) (b+a)*(b+a+x)^2*%e^(b+a*x+x^2);
                                       2
                                  2   x  + a x + b
(%o6)          (b + a) (x + b + a)  %e
(%i7) ev(isolate(%,x),exptisolate:true);

(%t7)                         b + a


                                 b
(%t8)                          %e

                                        2
                                   2   x  + a x
(%o8)             %t7 %t8 (x + %t7)  %e
```

See also: `exptisolate`, `isolate_wrt_times`, `disolate`.

<!-- category: Other -->
<!-- keywords: isolate_wrt_times -->
<!-- signatures: isolate_wrt_times -->
### Variable: isolate_wrt_times

Standardwert: `false`


Hat die Optionsvariable `isolate_wrt_times` den Wert `true`, fuhren 
die Funktionen `isolate` und `disolate` auch Ersetzungen in Produkten 
aus.


Siehe auch die Funktionen `isolate` und `disolate`.


Beispiele:



```maxima
(%i1) isolate_wrt_times: true$
(%i2) isolate (expand ((a+b+c)^2), c);

(%t2)                          2 a


(%t3)                          2 b


                          2            2
(%t4)                    b  + 2 a b + a

                     2
(%o4)               c  + %t3 c + %t2 c + %t4
(%i4) isolate_wrt_times: false$
(%i5) isolate (expand ((a+b+c)^2), c);
                     2
(%o5)               c  + 2 b c + 2 a c + %t4
```

See also: `isolate`, `disolate`.

<!-- category: Other -->
<!-- keywords: lfreeof -->
<!-- signatures: lfreeof(list, expr) -->
### Function: lfreeof (list, expr)

Fur jedes Element *m* der Liste *list* wird die Funktion
`freeof` aufgerufen.  `lfreeof` hat den Ruckgabewert `true`,
wenn keines der Elemente der Liste *list* im Ausdruck `expr` enthalten
ist.  Ansonsten ist der Ruckgabewert `false`.


Siehe auch die Funktion `freeof`.

See also: `freeof`.

<!-- category: Other -->
<!-- keywords: listconstvars -->
<!-- signatures: listconstvars -->
### Variable: listconstvars

Standardwert: `false`


Hat die Optionsvariable `listconstvars` den Wert `true`, werden
Konstante wie `%e`, `%pi` und Variablen, die als konstant
deklariert sind, von der Funktion `listofvars` in die Ergebnisliste
aufgenommen.  Der Standardwert von `listconstvars` ist `false` und
Konstante werden ignoriert.

See also: `%e`, `%pi`, `listofvars`.

<!-- category: Other -->
<!-- keywords: listdummyvars -->
<!-- signatures: listdummyvars -->
### Variable: listdummyvars

Standardwert: `true`


Hat `listdummyvars` den Wert `false`, werden die Dummy-Variablen eines
Ausdrucks von der Funktion `listofvars` ignoriert.  Dummy-Variablen sind
zum Beispiel der Index einer Summe, die Grenzwertvariable oder die
Integrationsvariable eines bestimmten Integrals.


Beispiele:



```maxima
(%i1) listdummyvars: true$
(%i2) listofvars ('sum(f(i), i, 0, n));
(%o2)                        [i, n]
(%i3) listdummyvars: false$
(%i4) listofvars ('sum(f(i), i, 0, n));
(%o4)                          [n]
```

See also: `listofvars`.

<!-- category: Other -->
<!-- keywords: listofvars -->
<!-- signatures: listofvars(expr) -->
### Function: listofvars (expr)

Die Funktion `listofvars` gibt eine Liste der Variablen zuruck, die im 
Ausdruck *expr* enthalten sind.


Hat die Optionsvariable `listconstvars` den Wert `true`, werden auch
Konstante wie `%e`, `%pi` und `%i` sowie als konstant
deklarierte Variable in die Liste aufgenommen.  Der Standardwert von
`listconstvars` ist `false`.


Siehe entsprechend die Optionsvariable `listdummyvars` fur 
Dummy-Variablen.


Beispiel:



```maxima
(%i1) listofvars (f (x[1]+y) / g^(2+a));
(%o1)                     [g, a, x , y]
                                  1
```

See also: `listconstvars`, `%e`, `%pi`, `%i`, `listdummyvars`.

<!-- category: Other -->
<!-- keywords: lpart -->
<!-- signatures: lpart(label, expr, n_1, ..., n_k) -->
### Function: lpart (label, expr, n_1, ..., n_k)

Die Funktion `lpart` ist ahnlich zu `dpart`, verwendet aber einen
Rahmen, der mit einer Marke gekennzeichnet ist.


Siehe auch `part`, `inpart` und `dpart`.

See also: `part`, `inpart`, `dpart`.

<!-- category: Other -->
<!-- keywords: mainvar -->
<!-- signatures: mainvar -->
### Variable: mainvar

Die Deklaration einer Variablen als eine Hauptvariable mit der Funktion
`declare` andert deren Anordnung in einem Ausdruck der kanonisch geordnet
ist.  Hauptvariable sind bezuglich der Funktionen `ordergreatp` und
`orderlessp` stets großer als alle anderen Symbole, Konstanten und
Zahlen.




Beispiel:



```maxima
(%i1) sort([9, 1, %pi, g, t, a]);
(%o1)                 [1, 9, %pi, a, g, t]

(%i2) declare(a, mainvar)$
(%i3) sort([9, 1, %pi, g, t, a]);
(%o3)                 [1, 9, %pi, g, t, a]
```

See also: `declare`, `ordergreatp`, `orderlessp`.

<!-- category: Other -->
<!-- keywords: noun -->
<!-- signatures: noun -->
### Variable: noun

`noun` ist eine der Optionen des Kommandos `declare`.  Wird eine
Funktion als `noun` deklariert, wird diese als Substantivform behandelt
und nicht ausgewertet.


Ein Symbol `f`, dass als `noun` deklariert wird, wird in die
Informationsliste `aliases` eingetragen und die Ruckgabe der Funktion
`properties` enthalt den Eintrag `noun`.


Beispiel:



```maxima
(%i1) factor (12345678);
                             2
(%o1)                     2 3  47 14593
(%i2) declare (factor, noun);
(%o2)                         done
(%i3) factor (12345678);
(%o3)                   factor(12345678)
(%i4) ''%, nouns;
                             2
(%o4)                     2 3  47 14593
```

See also: `declare`, `aliases`, `properties`.

<!-- category: Other -->
<!-- keywords: noundisp -->
<!-- signatures: noundisp -->
### Variable: noundisp

Standardwert: `false`


Hat `noundisp` den Wert `true`, werden Substantivformen mit einem
vorangestelltem Hochkomma angezeigt.  Diese Optionsvariable hat immer den Wert
`true`, wenn die Definition von Funktionen angezeigt wird.

<!-- category: Other -->
<!-- keywords: nounify -->
<!-- signatures: nounify(f) -->
### Function: nounify (f)

Die Funktion `nounify` gibt den Namen einer Funktion *f* in einer 
Substantivform zuruck.  Der Name *f* ist ein Symbol oder eine
Zeichenkette.


Einige Funktionen geben eine Substantivform zuruck, wenn die Funktion nicht 
ausgewertet werden kann.  Wird einem Funktionsaufruf wie zum Beispiel 
`'f(x)` oder `'(f(x))` ein Hochkomma vorangestellt, wird ebenfalls 
eine Substantivform zuruckgegeben.


Siehe auch die Funktion `verbify`.

See also: `verbify`.

<!-- category: Other -->
<!-- keywords: nterms -->
<!-- signatures: nterms(expr) -->
### Function: nterms (expr)

Die Funktion `nterms` gibt die Anzahl der Terme des Ausdrucks *expr* 
zuruck, wobei der Ausdruck als vollstandig expandiert angenommen wird, ohne 
dass Terme gekurzt oder zusammengefasst werden.


Ausdrucke wie `sin(expr)`, `sqrt(expr)` oder 
`exp(expr)` werden dabei als ein Term gezahlt.

<!-- category: Other -->
<!-- keywords: op -->
<!-- signatures: op(expr) -->
### Function: op (expr)

Die Funktion `op` gibt den Hauptoperator des Ausdrucks *expr* zuruck.
`op(expr)` ist aquivalent zu `part(expr, 0)`.


Ist der Hauptoperator des Ausdrucks *expr* ein Operator wie "+", "*" oder 
"/" wird der Name des Operators als Zeichenkette zuruckgegeben.  Andernfalls 
wird ein Symbol zuruckgegeben.


`op` beachtet den Wert der Optionsvariablen `inflag`.  `op`
wertet die Argumente aus.  Siehe auch `args`.


Beispiele:



```maxima
(%i1) stringdisp: true$
(%i2) op (a * b * c);
(%o2)                          "*"
(%i3) op (a * b + c);
(%o3)                          "+"
(%i4) op ('sin (a + b));
(%o4)                          sin
(%i5) op (a!);
(%o5)                          "!"
(%i6) op (-a);
(%o6)                          "-"
(%i7) op ([a, b, c]);
(%o7)                          "["
(%i8) op ('(if a > b then c else d));
(%o8)                         "if"
(%i9) op ('foo (a));
(%o9)                          foo
(%i10) prefix (foo);
(%o10)                        "foo"
(%i11) op (foo a);
(%o11)                        "foo"
(%i12) op (F [x, y] (a, b, c));
(%o12)                        F
                               x, y
(%i13) op (G [u, v, w]);
(%o13)                          G
```

See also: `inflag`, `args`.

<!-- category: Other -->
<!-- keywords: operatorp -->
<!-- signatures: operatorp(expr, op), operatorp(expr, [op_1, ..., op_n]) -->
### Function: operatorp (expr, op)

Das Kommando `operatorp(expr, op)` gibt `true` zuruck,
wenn *op* der Hauptoperator des Ausdrucks *expr* ist.


`operatorp(expr, [op_1, ..., op_n])` gibt `true` 
zuruck, wenn einer der Operatoren *op_1*, ..., *op_n* der 
Hauptoperator des Ausdrucks *expr* ist.

<!-- category: Other -->
<!-- keywords: opsubst -->
<!-- signatures: opsubst -->
### Variable: opsubst

Hat die Optionsvariable `opsubst` den Wert `false`, fuhrt die 
Funktion `subst` keine Substitution in einen Operator eines Ausdrucks aus.
Zum Beispiel hat `(opsubst: false, subst(x^2, r, r+r[0]))` das Ergebnis
`x^2+r[0]`.

See also: `subst`.

<!-- category: Other -->
<!-- keywords: optimize -->
<!-- signatures: optimize(expr) -->
### Function: optimize (expr)

Die Funktion `optimize` gibt einen Ausdruck zuruck, der dasselbe Ergebnis 
und dieselben Seiteneffekte wie *expr* hat, der jedoch effizienter 
ausgewertet werden kann.  Im neuen Ausdruck wird die mehrfache Berechnung 
gleicher Teilausdrucke vermieden und gleiche Teilausdrucke werden 
zusammengefasst.


Siehe auch die Funktion `collapse`.




`example(optimize)` zeigt ein Beispiel.

See also: `collapse`.

<!-- category: Other -->
<!-- keywords: optimprefix -->
<!-- signatures: optimprefix -->
### Variable: optimprefix

Standardwert: `%`


Die Optionsvariable `optimprefix` enthalt den Prafix, der von der 
Funktion `optimize` benutzt wird, um einen Teilausdruck zu benennen.

See also: `optimize`.

<!-- category: Other -->
<!-- keywords: ordergreat, orderless -->
<!-- signatures: ordergreat(v_1, ..., v_n), orderless(v_1, ..., v_n) -->
### Function: ordergreat (v_1, ..., v_n)

Die Funktion `ordergreat` andert die kanonische Anordnung der Symbole so,
dass *v_1* > *v_2* > ... > *v_n*.  Weiterhin ist *v_n* 
kleiner als jedes andere Symbol, das nicht in der Liste enthalten ist.


`orderless` andert die kanonische Anordnung der Symbole so, dass
*v_1* < *v_2* < ... < *v_n*.  Weiterhin ist *v_n*
großer als jedes andere Symbol, das nicht in der Liste enthalten ist.


Die durch `ordergreat` und `orderless` definierte Ordnung wird durch
`unorder` wieder aufgehoben.  `ordergreat` und `orderless` 
konnen jeweils nur einmal aufgerufen werden, solange nicht mit `unorder` 
zuvor die definierte Ordnung aufgehoben wird.


Siehe auch `ordergreatp`, `orderlessp` und `mainvar`.

See also: `unorder`, `ordergreatp`, `orderlessp`, `mainvar`.

<!-- category: Other -->
<!-- keywords: ordergreatp, orderlessp -->
<!-- signatures: ordergreatp(expr_1, expr_2), orderlessp(expr_1, expr_2) -->
### Function: ordergreatp (expr_1, expr_2)

Die Funktion `ordergreatp` gibt `true` zuruck, wenn in der 
kanonischen Ordnung von Maxima *expr_1* großer als *expr_2* ist.
Ansonsten ist das Ergebnis `false`.


Die Funktion `orderlessp` gibt `true` zuruck, wenn in der 
kanonischen Ordnung von Maxima *expr_1* kleiner als *expr_2* ist.
Ansonsten ist das Ergebnis `false`.


Alle Maxima-Atome und Ausdrucke sind vergleichbar unter `ordergreatp` und
`orderlessp`.  Die kanonische Ordnung von Atomen ist folgendermaßen:



   

Numerische Konstanten <
   deklarierte Konstanten <
   deklarierte Skalare <
   erstes Argument von `orderless` <
   weitere Argumente von `orderless` <
   letztes Argument von `orderless` <
   Variablen beginnend mit a, ... <
   Variablen beginnend mit Z <
   letzte Argument von `ordergreat` <
   weitere Argumente von `ordergreat` <
   erste Argument von `ordergreat` <
   deklarierte Hauptvariablen.



Die Ordnung fur Ausdrucke, die keine Atome sind, wird von der fur Atome 
abgeleitet.  Fur die Operatoren `"+"`, `"*"` und `"^"` kann die
Ordnung nicht einfach beschrieben werden.  Andere Operatoren, Funktionen und 
Ausdrucke werden angeordnet nach den Argumenten, dann nach den Namen.
Bei Ausdrucken mit Indizes wird der Name des Symbols als Operator und der 
Index als Argument betrachtet.


Die kanonische Ordnung der Ausdrucke wird modifiziert durch die Funktionen
`ordergreat` und `orderless` sowie der Deklarationen
`mainvar`, `constant` und `scalar`.


Siehe auch `sort`.


Beispiele:


Ordne Symbole und Konstanten.  `%pi` wird nicht nach dem numerischen Wert
sortiert, sondern wie eine Konstante.



```maxima
(%i1) stringdisp : true;
(%o1)                         true
(%i2) sort ([%pi, 3b0, 3.0, x, X, "foo", 3, a, "bar", 4.0, 4b0]);
(%o2) [3, 3.0, 4.0, 3.0b0, 4.0b0, %pi, "bar", "foo", a, x, X]
```


Anwendung der Funktionen `ordergreat` und `orderless`.



```maxima
(%i1) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o1)           [A, E, G, H, J, K, M, P, S, T, W]
(%i2) ordergreat (S, J);
(%o2)                         done
(%i3) orderless (M, H);
(%o3)                         done
(%i4) sort ([M, H, K, T, E, W, G, A, P, J, S]);
(%o4)           [M, H, A, E, G, K, P, T, W, J, S]
```


Anwendung der Deklarationen `mainvar`, `constant` und `scalar`.



```maxima
(%i1) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o1)   [aa, bar, baz, bb, cc, dd, foo, quux, A1, B1, C1]
(%i2) declare (aa, mainvar);
(%o2)                         done
(%i3) declare ([baz, quux], constant);
(%o3)                         done
(%i4) declare ([A1, B1], scalar);
(%o4)                         done
(%i5) sort ([aa, foo, bar, bb, baz, quux, cc, dd, A1, B1, C1]);
(%o5)   [baz, quux, A1, B1, bar, bb, cc, dd, foo, C1, aa]
```


Ordne nicht atomare Ausdrucke.



```maxima
(%i1) sort ([f(1), f(2), f(2, 1), g(1), g(1, 2), g(n), f(n, 1)]);
(%o1) [f(1), g(1), g(1, 2), f(2), f(2, 1), g(n), f(n, 1)]
(%i2) sort ([foo(1), X[1], X[k], foo(k), 1, k]);
(%o2)            [1, foo(1), X , k, foo(k), X ]
                              1              k
```

See also: `ordergreat`, `orderless`, `mainvar`, `constant`, `scalar`, `sort`, `%pi`.

<!-- category: Other -->
<!-- keywords: ordermagnitudep -->
<!-- signatures: ordermagnitudep(expr_1, expr_2) -->
### Function: ordermagnitudep (expr_1, expr_2)

Ist eine Aussagefunktion, die das Ergebnis `true` hat, wenn die Argumente
*expr_1* und *expr_2* Zahlen, Konstante oder konstante Ausdrucke
reprasentieren und *expr_1* kleiner als *expr_2* ist.  Sind die
Argumente nicht der Große nach vergleichbar, wird die Ordnung durch die
Aussagefunktion `orderlessp` bestimmt.


Wird die Aussagefunktion `ordermagnitudep` als Argument der Funktion 
`sort` verwendet, werden die Elemente einer Liste nach der Große
sortiert.


Beispiele:



```maxima
(%i1) ordermagnitudep(1, 2);
(%o1)                         true
(%i2) ordermagnitudep(%e, %pi);
(%o2)                         true
(%i3) sort([%e, %pi, sin(1), 0, 1, 2, 3, 4]);
(%o3)           [0, 1, 2, 3, 4, %e, %pi, sin(1)]
(%i4) sort([%e, %pi, sin(1), 0, 1, 2, 3, 4], ordermagnitudep);
(%o4)           [0, sin(1), 1, 2, %e, 3, %pi, 4]
```

See also: `orderlessp`, `sort`.

<!-- category: Other -->
<!-- keywords: part -->
<!-- signatures: part(expr, n_1, ..., n_k) -->
### Function: part (expr, n_1, ..., n_k)

Die Funktion `part` gibt einen Teilausdruck des Ausdrucks *expr*
zuruck.  Der Ausdruck *expr* wird zuvor in das Format fur die Anzeige
umgewandelt.


Der Teilausdruck wird durch die Indizes *n_1*, ..., *n_k* 
ausgewahlt.  Zuerst wird der Teilausdruck *n_1* ermittelt, von diesem der
Teilausdruck *n_2*, u.s.w.  Der zum Index *n_k* zuletzt gewonnene 
Teilausdruck ist dann das Ergebnis.


`part` kann auch verwendet werden, um ein Element einer Liste oder die
Zeile einer Matrix zu erhalten.


Das letzte Argument einer `part`-Funktion kann eine Liste mit Indizes sein.
In diesem Fall werden alle angegebenen Teilausdrucke als Ergebnis
zuruckgegeben.  Zum Beispiel hat das Kommando `part(x + y + z, [1, 3])`
das Ergebnis `z+x`.


Die Systemvariable `piece` enthalt den letzten Ausdruck, der bei der
Verwendung einer `part`-Funktion ausgewahlt wurde.


Hat die Optionsvariable `partswitch` den Wert `true`, wird `end`
zuruckgegeben, wenn versucht wurde, einen Teilausdruck zu bilden, der nicht
existiert, andernfalls wird eine Fehlermeldung ausgegeben.


Siehe auch `inpart`, `substpart`, `substinpart`,
`dpart` und `lpart`.

 

Beispiele:



```maxima
(%i1) part(z+2*y+a,2);
(%o1)                                 2 y
(%i2) part(z+2*y+a,[1,3]);
(%o2)                                z + a
(%i3) part(z+2*y+a,2,1);
(%o3)                                  2
```


`example(part)` zeigt weitere Beispiele.

See also: `piece`, `partswitch`, `inpart`, `substpart`, `substinpart`, `dpart`, `lpart`.

<!-- category: Other -->
<!-- keywords: partition -->
<!-- signatures: partition(expr, var) -->
### Function: partition (expr, var)

Die Funktion `partition` gibt eine Liste mit zwei Ausdrucken zuruck.
Ist das Argument *expr* ein Produkt enthalt das erste Element die
Faktoren, die die Variable `var` enthalten, und das zweite Element
enthalt die ubrigen Faktoren.  Entsprechend enthalt das erste Element die
Terme einer Summe oder die Elemente einer Liste, die die Variable *var*
enthalten, und das zweite Elemente die verbleibende Terme der Summe oder
Elemente der Liste.



```maxima
(%i1) partition (2*a*x*f(x), x);
(%o1)                     [2 a, x f(x)]
(%i2) partition (a+b, x);
(%o2)                      [b + a, 0]
(%i3) partition ([a, b, f(a), c], a); 
(%o3)                  [[b, c], [a, f(a)]]
```

<!-- category: Other -->
<!-- keywords: partswitch -->
<!-- signatures: partswitch -->
### Variable: partswitch

Standardwert: `false`


Hat die Optionsvariable `partswitch` den Wert `true`, wird `end` 
zuruckgegeben, wenn versucht wird, einen Teilausdruck zu bilden, der nicht
existiert, andernfalls wird eine Fehlermeldung ausgegeben.

<!-- category: Other -->
<!-- keywords: pickapart -->
<!-- signatures: pickapart(expr, n) -->
### Function: pickapart (expr, n)

Den Teilausdrucken in einer Tiefe *n* eines verschachtelten Ausdrucks 
werden Zwischenmarken zugewiesen.  *n* ist eine ganze positive Zahl.  Die 
Ruckgabe von `pickapart` ist ein aquivalenter Ausdruck, der die 
Zwischenmarken enthalt.


Siehe auch `part`, `dpart`, `lpart`,
`inpart` und `reveal`.


Beispiele:



```maxima
(%i1) expr: (a+b)/2 + sin (x^2)/3 - log (1 + sqrt(x+1));

                                          2
                                     sin(x )   b + a
(%o1)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2

(%i2) pickapart (expr, 0);

                                          2
                                     sin(x )   b + a
(%t2)       - log(sqrt(x + 1) + 1) + ------- + -----
                                        3        2

(%o2)                          %t2
(%i3) pickapart (expr, 1);

(%t3)                - log(sqrt(x + 1) + 1)


                                  2
                             sin(x )
(%t4)                        -------
                                3


                              b + a
(%t5)                         -----
                                2

(%o5)                    %t5 + %t4 + %t3
(%i5) pickapart (expr, 2);

(%t6)                 log(sqrt(x + 1) + 1)


                                  2
(%t7)                        sin(x )


(%t8)                         b + a

                         %t8   %t7
(%o8)                    --- + --- - %t6
                          2     3
(%i8) pickapart (expr, 3);

(%t9)                    sqrt(x + 1) + 1


                                2
(%t10)                         x


                  b + a              sin(%t10)
(%o10)            ----- - log(%t9) + ---------
                    2                    3

(%i10) pickapart (expr, 4);

(%t11)                     sqrt(x + 1)

                      2
                 sin(x )   b + a
(%o11)           ------- + ----- - log(%t11 + 1)
                    3        2
(%i11) pickapart (expr, 5);

(%t12)                        x + 1

                   2
              sin(x )   b + a
(%o12)        ------- + ----- - log(sqrt(%t12) + 1)
                 3        2
(%i12) pickapart (expr, 6);
                  2
             sin(x )   b + a
(%o12)       ------- + ----- - log(sqrt(x + 1) + 1)
                3        2
```

See also: `part`, `dpart`, `lpart`, `inpart`, `reveal`.

<!-- category: Other -->
<!-- keywords: piece -->
<!-- signatures: piece -->
### Variable: piece

Die Systemvariable `piece` enthalt den letzten Ausdruck, der bei der 
Verwendung einer `part`-Funktion ausgewahlt wurde.


Siehe auch `part` und `inpart`.

See also: `part`, `inpart`.

<!-- category: Other -->
<!-- keywords: psubst -->
<!-- signatures: psubst(list, expr), psubst(a, b, expr) -->
### Function: psubst (list, expr)

`psubst(a, b, expr)` ist identisch mit `subst`.
Siehe `subst`.


Im Unterschied zu `subst` fuhrt die Funktion `psubst` Substitutionen
parallel aus, wenn das erste Argument *list* eine Liste mit Gleichungen ist.


Siehe auch die Funktion `sublis`, um Substitutionen parallel
auszufuhren.


Beispiel:


Das erste Beispiel zeigt die parallele Substitution mit `psubst`.  Das 
zweite Beispiel zeigt das Ergebnis fur die Funktion `subst`.  In diesem
Fall werden die Substitutionen nacheinander ausgefuhrt.



```maxima
(%i4) psubst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o4)                           sin(b) + sin(a)
(%i5) subst ([a^2=b, b=a], sin(a^2) + sin(b));
(%o5)                              2 sin(a)
```

See also: `subst`, `sublis`.

<!-- category: Other -->
<!-- keywords: rembox -->
<!-- signatures: rembox(expr, unlabelled), rembox(expr, label), rembox(expr) -->
### Function: rembox (expr, unlabelled)

Die Funktion `rembox` entfernt Rahmen aus dem Ausdruck *expr*.
`rembox(expr, unlabelled)` entfernt alle Rahmen, die keine Marke 
haben.  `rembox(expr, label)` entfernt nur Rahmen, die mit der 
Marke *label* gekennzeichnet sind.  `rembox(expr)` entfernt alle 
Rahmen.


Rahmen werden mit den Funktionen `box`, `dpart` und
`lpart` einem Ausdruck hinzugefugt.


Beispiele:



```maxima
(%i1) expr: (a*d - b*c)/h^2 + sin(%pi*x);
                                  a d - b c
(%o1)                sin(%pi x) + ---------
                                      2
                                     h

(%i2) dpart (dpart (expr, 1, 1), 2, 2);
                        """""""    a d - b c
(%o2)               sin("%pi x") + ---------
                        """""""      """"
                                     " 2"
                                     "h "
                                     """"

(%i3) expr2: lpart (BAR, lpart (FOO, %, 1), 2);
                  FOO"""""""""""   BAR""""""""
                  "    """"""" "   "a d - b c"
(%o3)             "sin("%pi x")" + "---------"
                  "    """"""" "   "  """"   "
                  """"""""""""""   "  " 2"   "
                                   "  "h "   "
                                   "  """"   "
                                   """""""""""

(%i4) rembox (expr2, unlabelled);

                                  BAR""""""""
                   FOO"""""""""   "a d - b c"
(%o4)              "sin(%pi x)" + "---------"
                   """"""""""""   "    2    "
                                  "   h     "
                                  """""""""""


(%i5) rembox (expr2, FOO);

                                  BAR""""""""
                       """""""    "a d - b c"
(%o5)              sin("%pi x") + "---------"
                       """""""    "  """"   "
                                  "  " 2"   "
                                  "  "h "   "
                                  "  """"   "
                                  """""""""""


(%i6) rembox (expr2, BAR);

                   FOO"""""""""""
                   "    """"""" "   a d - b c
(%o6)              "sin("%pi x")" + ---------
                   "    """"""" "     """"
                   """"""""""""""     " 2"
                                      "h "
                                      """"


(%i7) rembox (expr2);
                                  a d - b c
(%o7)                sin(%pi x) + ---------
                                      2
                                     h
```

See also: `box`, `dpart`, `lpart`.

<!-- category: Other -->
<!-- keywords: reveal -->
<!-- signatures: reveal(expr, depth) -->
### Function: reveal (expr, depth)

Ersetzt Teile des Ausdrucks *expr* in der ganzzahligen Tiefe *depth* 
durch eine beschreibende Zusammenfassung:



- *
Summen und Differenzen werden durch `Sum(n)` ersetzt, wobei *n*
die Anzahl der Terme der Summe oder Differenz ist.
- *
Produkte werden durch `Product(n)` ersetzt, wobei *n* die Anzahl
der Faktoren des Produktes ist.
- *
Exponentiationen werden durch `Expt` ersetzt.
- *
Quotienten werden durch `Quotient` ersetzt.
- *
Die Negation wird durch `Negterm` ersetzt.
- *
Listen werden durch `List(n)` ersetzt, wobei *n* die Anzahl der 
Elemente der Liste ist.


Ist *depth* großer oder gleich der maximalen Tiefe des Ausdrucks 
*expr*, gibt `reveal` den Ausdruck *expr* unverandert zuruck.


`reveal` wertet die Argumente aus.  `reveal` gibt die 
Zusammenfassung zuruck.


Beispiele:



```maxima
(%i1) e: expand ((a - b)^2)/expand ((exp(a) + exp(b))^2);

                          2            2
                         b  - 2 a b + a
(%o1)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e

(%i2) reveal (e, 1);
(%o2)                       Quotient
(%i3) reveal (e, 2);
                             Sum(3)
(%o3)                        ------
                             Sum(3)
(%i4) reveal (e, 3);
                     Expt + Negterm + Expt
(%o4)               ------------------------
                    Product(2) + Expt + Expt
(%i5) reveal (e, 4);
                       2                 2
                      b  - Product(3) + a
(%o5)         ------------------------------------
                         Product(2)     Product(2)
              2 Expt + %e           + %e
(%i6) reveal (e, 5);
                         2            2
                        b  - 2 a b + a
(%o6)              --------------------------
                       Sum(2)     2 b     2 a
                   2 %e       + %e    + %e
(%i7) reveal (e, 6);
                          2            2
                         b  - 2 a b + a
(%o7)               -------------------------
                        b + a     2 b     2 a
                    2 %e      + %e    + %e
```

<!-- category: Other -->
<!-- keywords: sublis -->
<!-- signatures: sublis(list, expr) -->
### Function: sublis (list, expr)

Fuhrt im Unterschied zu der Funktion `subst` die Substitutionen der
Liste *list* parallel und nicht nacheinander aus.


Mit der Optionsvariablen `sublis_apply_lambda` wird die Vereinfachung
von Lamda-Ausdrucken kontrolliert, nachdem die Substitution ausgefuhrt 
wurde.


Siehe auch die Funktion `psubst`, um parallele Substitutionen
auszufuhren.


Beispiele:



```maxima
(%i1) sublis ([a=b, b=a], sin(a) + cos(b));
(%o1)                    sin(b) + cos(a)
```

See also: `subst`, `sublis_apply_lambda`, `psubst`.

<!-- category: Other -->
<!-- keywords: sublis_apply_lambda -->
<!-- signatures: sublis_apply_lambda -->
### Variable: sublis_apply_lambda

Standardwert: `true`


Kontrolliert, ob Lambda-Ausdrucke nach einer Substitution ausgewertet werden.
Hat `sublis_apply_lambda` den Wert `true` werden Lambda-Ausdrucke
ausgewertet.  Ansonsten verbleiben diese nach der Substitution im Ausdruck.

<!-- category: Other -->
<!-- keywords: subnumsimp -->
<!-- signatures: subnumsimp -->
### Variable: subnumsimp

Default value: `false`


If `true` then the functions `subst` and `psubst` can substitute
a subscripted variable `f[x]` with a number, when only the symbol `f`
is given.


See also `subst`.



```maxima
(%i1) subst(100,g,g[x]+2);

subst: cannot substitute 100 for operator g in expression g
                                                           x
 -- an error. To debug this try: debugmode(true);

(%i2) subst(100,g,g[x]+2),subnumsimp:true;
(%o2)                          102
```

See also: `subst`, `psubst`.

<!-- category: Other -->
<!-- keywords: subst -->
<!-- signatures: subst(a, b, c) -->
### Function: subst (a, b, c)

Substituiert *a* fur *b* in den Ausdruck *c*.  Das Argument 
*b* muss ein Atom oder ein vollstandiger Teilausdruck von *c* sein.
Zum Beispiel ist `x+y+z` ein vollstandiger Teilausdruck von
`2*(x+y+z)/w`, nicht aber `x+y`.  Hat *b* nicht diese Eigenschaft,
dann konnen moglicherweise die Funktionen `substpart` oder 
`ratsubst` angewendet werden.


Hat *b* die Form `e/f`, kann `subst(a*f, e, c)` verwendet werden.
Ist `b` von der Form `e^(1/f)`, dann kann `subst(a^f, e, c)`
verwendet werden.  Die Funktion `subst` erkennt auch den Ausdruck 
`x^y` in `x^-y`, so dass `subst(a, sqrt(x), 1/sqrt(x))` das
Ergebnis `1/a` hat.  *a* und *b* konnen auch die Namen von 
Operatoren oder Funktionen sein.  Soll die unabhangige Variable in
Ausdrucken mit Ableitungen substituiert werden, sollte die Funktion
`at` verwendet werden.


`subst` ist der Alias-Name fur `substitute`.


`subst(eq_1, expr)` und `subst([eq_1, ..., eq_k], expr)` sind weitere mogliche Formen.  *eq_i* sind
Gleichungen, die angeben, welche Substitutionen auszufuhren sind.  Fur 
jede Gleichung wird die rechte Seite der Gleichung fur die linke Seite in den
Ausdruck *expr* substituiert.


Hat die Optionsvariable `exptsubst` den Wert `true`, wird eine
Substitution wie `y` fur `%e^x` in einem Ausdruck der Form 
`%e^(a*x)` nicht ausgefuhrt.


Hat die Optionsvariable `option_opsubst` den Wert `false`,
fuhrt die Funktion `subst` keine Substitution in einen Operator eines
Ausdrucks aus.  Zum Beispiel hat `(opsubst: false, subst(x^2, r, r+r[0]))`
das Ergebnis `x^2+r[0]`.


Beispiele:



```maxima
(%i1) subst (a, x+y, x + (x+y)^2 + y);
                                    2
(%o1)                      y + x + a
(%i2) subst (-%i, %i, a + b*%i);
(%o2)                       a - %i b
```



Weitere Beispiele werden mit `example(subst)` angezeigt.

See also: `substpart`, `ratsubst`, `at`, `exptsubst`, `option_opsubst`.

<!-- category: Other -->
<!-- keywords: substinpart -->
<!-- signatures: substinpart(x, expr, n_1, ..., n_k) -->
### Function: substinpart (x, expr, n_1, ..., n_k)

Die Funktion `substinpart` ist vergleichbar mit `substpart`.
`substinpart` wirkt jedoch auf die interne Darstellung des Ausdrucks 
*expr*.


Beispiele:



```maxima
(%i1) x . 'diff (f(x), x, 2);

                              2
                             d
(%o1)                   x . (--- (f(x)))
                               2
                             dx

(%i2) substinpart (d^2, %, 2);
                                  2
(%o2)                        x . d
(%i3) substinpart (f1, f[1](x + 1), 0);
(%o3)                       f1(x + 1)
```

See also: `substpart`.

<!-- category: Other -->
<!-- keywords: substpart -->
<!-- signatures: substpart(x, expr, n_1, ..., n_k) -->
### Function: substpart (x, expr, n_1, ..., n_k)

Substituiert *x* fur den Teilausdruck, der mit den restlichen Argumenten 
der Funktion `substpart` ausgewahlt wird.  Es wird der neue Ausdruck 
*expr* zuruckgegeben.  *x* kann auch der Name eines Operators sein,
der fur einen Operator im Ausdruck *expr* substituiert wird.  Zum Beispiel
hat `substpart("+", a*b, 0)` das Ergebnis `b + a`).


Mit dem Wert `true` fur die Optionsvariable `inflag`, verhalt
sich die Funktion `substpart` wie `substinpart`.


Beispiele:



```maxima
(%i1) 1/(x^2 + 2);
                               1
(%o1)                        ------
                              2
                             x  + 2
(%i2) substpart (3/2, %, 2, 1, 2);

                               1
(%o2)                       --------
                             3/2
                            x    + 2

(%i3) a*x + f(b, y);
(%o3)                     a x + f(b, y)
(%i4) substpart ("+", %, 1, 0);
(%o4)                    x + f(b, y) + a
```

See also: `inflag`, `substinpart`.

<!-- category: Other -->
<!-- keywords: symbolp -->
<!-- signatures: symbolp(expr) -->
### Function: symbolp (expr)

Gibt `true` zuruck, wenn *expr* ein Symbol ist, ansonsten 
`false`.  Das Kommando `symbolp(x)` ist aquivalent zu
`atom(x) and not numberp(x)`.


Siehe auch Bezeichner.

<!-- category: Other -->
<!-- keywords: unorder -->
<!-- signatures: unorder() -->
### Function: unorder ()

Loscht die Ordnung, die mit dem letzten Aufruf der Funktionen 
`ordergreat` oder `orderless` erzeugt wurde.


Siehe auch `ordergreat` und `orderless`.


Beispiele:



```maxima
(%i1) unorder();
(%o1)                          []
(%i2) b*x + a^2;
                                   2
(%o2)                       b x + a
(%i3) ordergreat (a);
(%o3)                         done
(%i4) b*x + a^2;
 %th(1) - %th(3);
                             2
(%o4)                       a  + b x
(%i5) unorder();
                              2    2
(%o5)                        a  - a
```

See also: `ordergreat`, `orderless`.

<!-- category: Other -->
<!-- keywords: verbify -->
<!-- signatures: verbify(f) -->
### Function: verbify (f)

Gibt das Verb des Symbols *f* zuruck.  Siehe auch das Kapitel
Substantive und Verben, sowie `noun` und `nounify`.


Beispiele:



```maxima
(%i1) verbify ('foo);
(%o1)                          foo
(%i2) :lisp $%
$FOO
(%i2) nounify (foo);
(%o2)                          foo
(%i3) :lisp $%
%FOO
```

See also: `noun`, `nounify`.

