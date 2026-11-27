## Muster und Regeln

<!-- category: Other -->
<!-- keywords: announce_rules_firing -->
<!-- signatures: announce_rules_firing -->
### Variable: announce_rules_firing

Standardwert: `false`


Hat die Optionsvariable `announce_rules_firing` den Wert `true` und
wird mit den Funktionen `tellsimp` oder `tellsimpafter` eine Regel
definiert, dann wird immer dann eine Meldung ausgegeben, wenn die Regel
angewendet wird.  `announce_rules_firing` hat keinen Einfluss auf Regeln,
die bereits definiert sind.  Die Meldung von Regeln kann auch nicht durch das
Setzen von `announce_rules_firing` auf den Wert `false` abgeschaltet
werden.


Diese Optionsvariable ist nutzlich, wenn die Anwendung von nutzerdefinierten
Regeln fur die Fehlersuche kontrolliert werden soll.


Beispiel:



```maxima
(%i1) announce_rules_firing:true;
(%o1)                         true
(%i2) tellsimpafter(tan(x), sin(x)/cos(x));
(%o2)                 [tanrule1, simp-%tan]
(%i3) tan(x);

By tanrule1 , tan(x) --> sin(x)/cos(x) 
                             sin(x)
(%o3)                        ------
                             cos(x)
```

See also: `tellsimp`, `tellsimpafter`.

<!-- category: Other -->
<!-- keywords: apply1 -->
<!-- signatures: apply1(expr, rule_1, ..., rule_n) -->
### Function: apply1 (expr, rule_1, ..., rule_n)

Wendet die Regel *rule_1* auf den Ausdruck *expr* solange an, bis sich
das Ergebnis nicht mehr andert.  Die Regel wird zuerst auf der obersten Ebene
des Ausdrucks und dann nacheinander von links nach rechts auf die
Teilausdrucke angewendet.  Ist *expr_1* das Ergebnis der Anwendung der
Regel *rule_1*, dann wird die Regel *rule_2* auf gleiche Weise auf den
Ausdruck *expr_1* angewendet.  Zuletzt wird die Regel *rule_n*
angewendet.  Das letzte Ergebnis wird zuruckgegeben.


Die Optionsvariable `maxapplydepth` enthalt die großte
Verschachtelungstiefe, fur die die Funktionen `apply1` und
`apply2` auf einen Ausdruck angewendet werden.


Siehe auch die Funktionen `applyb1` und `apply2`, um Regeln auf
einen Ausdruck anzuwenden, die mit der Funktion `defrule` definiert sind.


Beispiele:



```maxima
(%i1) defrule(trig1, tan(x), sin(x)/cos(x));
                                      sin(x)
(%o1)               trig1 : tan(x) -> ------
                                      cos(x)
(%i2) defrule(trig2, cot(x), 1/tan(x));
                                        1
(%o2)               trig2 : cot(x) -> ------
                                      tan(x)
(%i3) apply1(cot(x), trig1, trig2);
                               1
(%o3)                        ------
                             tan(x)
(%i4) apply1(cot(x), trig2, trig1);

                             cos(x)
(%o4)                        ------
                             sin(x)
```


Die folgenden Beispiele zeigen, wie mit der Optionsvariablen
`maxapplydepth` die Tiefe kontrolliert wird, in der eine Regel
auf die Teilausdrucke angewendet wird.



```maxima
(%i1) expr: tan(x)+exp(a+2*tan(x));
                                2 tan(x) + a
(%o1)                tan(x) + %e
(%i2) defrule(trig, tan(x), sin(x)/cos(x));
                                      sin(x)
(%o2)                trig : tan(x) -> ------
                                      cos(x)
(%i3) maxapplydepth: 1;
(%o3)                           1
(%i4) apply1(expr, trig);
                     sin(x)     2 tan(x) + a
(%o4)                ------ + %e
                     cos(x)
(%i5) maxapplydepth: 4;
(%o5)                           4
(%i6) apply1(expr, trig);

                                2 sin(x)
                                -------- + a
                     sin(x)      cos(x)
(%o6)                ------ + %e
                     cos(x)
```

See also: `maxapplydepth`, `applyb1`, `apply2`, `defrule`.

<!-- category: Other -->
<!-- keywords: apply2 -->
<!-- signatures: apply2(expr, rule_1, ..., rule_n) -->
### Function: apply2 (expr, rule_1, ..., rule_n)

Zunachst werden nacheinander die Regeln *rule_1*, *rule_2*, ...
auf den Ausdruck *expr* angewendet.  Schlagt die Anwendung aller Regeln
fehl, werden die Regeln nacheinander auf die Teilausdrucke des Argumentes
*expr* angewendet.  Kann eine der Regeln erfolgreich angewendet werden,
wird die Anwendung aller Regeln auf den Teilausdruck wiederholt.


Im Unterschied zur Funktion `apply1` werden von der Funktion `apply2`
immer alle Regeln angewendet.  Sind jedoch die Regeln, die als Argumente
ubergeben werden, zirkular definiert, so fuhrt Maxima eine Endlosschleife
aus.  Siehe dazu auch das Beispiel unten.


Die Optionsvariable `maxapplydepth` enthalt die großte
Verschachtelungstiefe, fur die die Funktionen `apply1` und `apply2`
auf einen Ausdruck angewendet werden.


Siehe auch die Funktionen `apply1` und `applyb1`, um Regeln
auf einen Ausdruck anzuwenden, die mit der Funktion `defrule` definiert
sind.


Beispiele:


Im Unterschied zur Funktion `apply1` ist in diesem Fall das Ergebnis
immer `sin(x)/cos(x)`, da alle Regeln wiederholt auf einen Teilausdruck
angewendet werden, wenn sich der Ausdruck fur eine Regel andert.



```maxima
(%i1) defrule(trig1, tan(x), sin(x)/cos(x));
                                      sin(x)
(%o1)               trig1 : tan(x) -> ------
                                      cos(x)
(%i2) defrule(trig2, cot(x), 1/tan(x));
                                        1
(%o2)               trig2 : cot(x) -> ------
                                      tan(x)
(%i3) apply2(cot(x), trig1, trig2);
                             cos(x)
(%o3)                        ------
                             sin(x)
(%i4) apply2(cot(x), trig2, trig1);

                             cos(x)
(%o4)                        ------
                             sin(x)
```


Das folgende Beispiel zeigt eine zirkulare Definition der Regeln `trig1`
und `trig2`.  Mit der Funktion `apply1` hangt das Ergebnis von der
Reihenfolge der Anwendung der Regeln ab.  Die Anwendung der Funktion
`apply2` fuhrt fur dieses Beispiel zu einer Endlosschleife.



```maxima
(%i1) defrule(trig1, tan(x), sin(x)/cos(x));
                                      sin(x)
(%o1)               trig1 : tan(x) -> ------
                                      cos(x)
(%i2) defrule(trig2, sin(x)/cos(x), tan(x));
                            sin(x)
(%o2)               trig2 : ------ -> tan(x)
                            cos(x)
(%i3) expr: tan(x) + exp(sin(x)/cos(x));
                                   sin(x)
                                   ------
                                   cos(x)
(%o3)                   tan(x) + %e
(%i4) apply1(expr, trig1, trig2);
                                   tan(x)
(%o4)                   tan(x) + %e
(%i5) apply1(expr, trig2, trig1);
                                   sin(x)
                                   ------
                        sin(x)     cos(x)
(%o5)                   ------ + %e
                        cos(x)
```

See also: `apply1`, `maxapplydepth`, `applyb1`, `defrule`.

<!-- category: Other -->
<!-- keywords: applyb1 -->
<!-- signatures: applyb1(expr, rule_1, ..., rule_n) -->
### Function: applyb1 (expr, rule_1, ..., rule_n)

Wendet die Regel *rule_1* auf den tiefsten Teilausdruck in der Baumstruktur
eines Ausdrucks an.  Schlagt die Anwendung fehl, wird der Teilausdruck eine
Ebene hoher betrachtet, bis *rule_1* auf die oberste Ebene des Ausdrucks
*expr* angewendet wird.  Danach wird auf gleiche Weise die Regel
*rule_2* auf den Ausdruck *expr* angewendet.  Nachdem die letzte Regel
*rule_n* angewendet wurde, wird das Ergebnis zuruckgegeben.


`applyb1` ist vergleichbar mit `apply1` mit dem Unterschied, dass
die Regeln Bottom-Up angewendet werden.


Die Optionsvariable `maxapplyheight` enthalt den Wert der großten
Verschachtelungstiefe, fur die `applyb1` angewendet wird.


Siehe auch die Funktionen `apply1` und `apply2`, um Regeln auf
einen Ausdruck anzuwenden, die mit der Funktion `defrule` definiert sind.


Beispiel:


Das folgende Beispiel zeigt, wie die Regel `trig` zuerst auf die
unterste Ebene des Ausdrucks angewendet wird.  Dazu wird die Optionsvariable
`maxapplyheight` zunachst auf den Wert `1` gesetzt und dann auf den
Wert `4` erhoht.



```maxima
(%i1) matchdeclare(x, true);
(%o1)                         done
(%i2) defrule(trig, tan(x), sin(x)/cos(x));
                                      sin(x)
(%o2)                trig : tan(x) -> ------
                                      cos(x)
(%i3) expr: exp(a+2*tan(b+exp(tan(x))));

                              tan(x)
                      2 tan(%e       + b) + a
(%o3)               %e

(%i4) maxapplyheight: 1;
(%o4)                           1
(%i5) applyb1(expr, trig);

                              sin(x)
                              ------
                              cos(x)
                      2 tan(%e       + b) + a
(%o5)               %e

(%i6) maxapplyheight: 4;
(%o6)                           4
(%i7) applyb1(expr, trig);
                              sin(x)
                              ------
                              cos(x)
                      2 sin(%e       + b)
                      ------------------- + a
                             sin(x)
                             ------
                             cos(x)
                       cos(%e       + b)
(%o7)               %e
```

See also: `apply1`, `maxapplyheight`, `apply2`, `defrule`.

<!-- category: Other -->
<!-- keywords: clear_rules -->
<!-- signatures: clear_rules() -->
### Function: clear_rules ()

Fuhrt das Kommando `kill(rules)` aus und setzt die internen Zahler
fur die Benennung der Regeln fur die Addition, die Multiplikation und die
Exponentiation auf den Anfangswert zuruck.  Mit dem Kommando
`kill(rules)` werden alle Regeln entfernt, ohne dass die internen Zahler
zuruckgesetzt werden.  Siehe auch die Funktion `kill`.


Beispiel:



```maxima
(%i1) tellsimpafter(a+b, add(a,b));
(%o1)                   [+rule1, simplus]
(%i2) tellsimpafter(a*b, mul(a,b));
(%o2)                  [*rule1, simptimes]
(%i3) tellsimpafter(a^b, expt(a,b));
(%o3)                  [^rule1, simpexpt]
(%i4) rules;
(%o4)               [+rule1, *rule1, ^rule1]
(%i5) clear_rules();
(%o5)                         done
(%i6) rules;
(%o6)                          []
```


Das folgende Beispiel zeigt einen Programmfehler von Maxima.  Die Funktion
`trigsimp` ist mit Hilfe von Regeln implementiert.  Die Regeln werden
automatisch beim ersten Aufruf der Funktion `trigsimp` geladen und in die
Liste `rules` eingetragen.  Werden die Regeln mit der Funktion
`clear_rules` oder `kill` geloscht, fuhrt der nachste Aufruf
der Funktion `trigsimp` zu einem Fehler.



```maxima
(%i1) trigsimp(sin(x)^2+cos(x)^2);
(%o1)                           1
(%i2) rules;
(%o2) [trigrule1, trigrule2, trigrule3, trigrule4, htrigrule1, 
                              htrigrule2, htrigrule3, htrigrule4]
(%i3) disprule(trigrule1, trigrule2, trigrule3, trigrule4)$
                                        sin(a)
(%t3)             trigrule1 : tan(a) -> ------
                                        cos(a)

                                          1
(%t4)             trigrule2 : sec(a) -> ------
                                        cos(a)

                                          1
(%t5)             trigrule3 : csc(a) -> ------
                                        sin(a)

                                        cos(a)
(%t6)             trigrule4 : cot(a) -> ------
                                        sin(a)

(%i7) clear_rules();
(%o7)                         done
(%i8) rules;
(%o8)                          []
(%i9) trigsimp(sin(x)^2+cos(x)^2);

apply1: no such rule: trigrule1
#0: trigsimp(x=sin(x)^2+cos(x)^2)(trgsmp.mac line 71)
 -- an error. To debug this try: debugmode(true);
```

See also: `kill`, `trigsimp`, `rules`.

<!-- category: Other -->
<!-- keywords: current_let_rule_package -->
<!-- signatures: current_let_rule_package -->
### Variable: current_let_rule_package

Standardwert: `default_let_rule_package`


Die Optionsvariable `current_let_rule_package` enthalt den Namen des
aktuellen Regelpaketes, das von den Funktionen `let`,
`letrules`, `letsimp` und `remlet` verwendet wird.  Der
Optionsvariablen kann jedes mit der Funktion `let` definierte Regelpaket
zugewiesen werden.


Wird das Kommando `letsimp(expr, rule_pkg_name)` ausgefuhrt, dann wird 
fur das aktuelle Kommando das Paket `rule_pkg_name` verwendet.  Der 
Wert der Variablen `current_let_rule_package` wird nicht geandert.


Siehe auch die Optionsvariable `default_let_rule_package`.

See also: `let`, `letrules`, `letsimp`, `remlet`, `default_let_rule_package`.

<!-- category: Other -->
<!-- keywords: default_let_rule_package -->
<!-- signatures: default_let_rule_package -->
### Variable: default_let_rule_package

Standardwert: `default_let_rule_package`


Die Optionsvariable `default_let_rule_package` bezeichnet das Regelpaket,
das verwendet wird, wenn kein Regelpaket mit der Funktion `let` explizit
definiert und der Wert der Optionsvariablen `current_let_rule_package`
nicht geandert wurde.

See also: `current_let_rule_package`.

<!-- category: Other -->
<!-- keywords: defmatch -->
<!-- signatures: defmatch(progname, pattern, x_1, ..., x_n), defmatch(progname, pattern) -->
### Function: defmatch (progname, pattern, x_1, ..., x_n)

Definiert eine Aussagefunktion `progname(expr)` oder
`progname(expr, x_1, ..., x_n)`, die einen
Ausdruck *expr* testet, um zu prufen, ob dieser das Muster *pattern*
enthalt.


Das Argument *pattern* ist ein Ausdruck mit den Musterargumenten *x_1*,
..., *x_n*.  Die Musterargumente konnen entfallen.  Der Ausdruck kann
weiterhin Mustervariablen enthalten, die mit der Funktion
`matchdeclare` definiert sind.  Alle anderen Variablen und Bezeichner
entsprechen sich selbst bei einem Musterabgleich.


Das erste Argument der Aussagefunktion *progname* ist ein Ausdruck
*expr*, fur den gepruft wird, ob das Muster *pattern* enthalten ist.
Die weiteren Argumente der Funktion `progname` sind die Variablen, die den
Musterargumenten *x_1*, ..., *x_n* des Musters *pattern*
entsprechen.


Ist der Musterabgleich erfolgreich, gibt die Aussagefunktion *progname* eine
Liste mit Gleichungen zuruck.  Die linken Seiten der Gleichungen sind die
Musterargumente und Mustervariablen und die rechten Seiten sind die
Teilausdrucke, fur die der Musterabgleich eine Ubereinstimmung gefunden
hat.  Die erhaltenen Ergebnisse des Musterabgleichs werden den mit
`matchdeclare` definierten Mustervariablen, jedoch nicht den
Musterargumenten der Funktion `defmatch` zugewiesen.  Ist der
Musterabgleich nicht erfolgreich, ist die Ruckgabe `false`.


Ein Muster, das keine Musterargumente oder Mustervariablen enthalt, hat den
Ruckgabewert `true`, wenn der Musterabgleich erfolgreich ist.


Die Aussagefunktion `progname` wird in die Informationsliste
`rules` eingetragen.


Siehe auch die Funktionen `matchdeclare`, `defrule`,
`tellsimp` und `tellsimpafter`.


Beispiele:


Definition einer Funktion `linearp(expr, x)`, die pruft, ob ein Ausdruck
*expr* die Form `a*x+b` hat, wobei `a` und `b` die Variable
*x* nicht enthalten und `a` von Null verschieden ist.  Die Definition
enthalt das Musterargument *x*, so dass die Linearitat des Ausdrucks
fur eine beliebige Variable getestet werden kann.  Den Mustervariablen
`a` und `b` werden die Teilausdrucke des Musterabgleichs zugewiesen,
nicht jedoch dem Musterargument `x`.



```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), 
                    b, freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b, x);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2, z);

                         2
(%o3)              [b = y , a = y + 4, x = z]

(%i4) a;
(%o4)                         y + 4
(%i5) b;
                                2
(%o5)                          y
(%i6) x;
(%o6)                           x
```


Wie im letzten Beispiel wird eine Aussagefunktion definiert, die pruft, ob ein
Ausdruck *expr* linear ist.  In diesem Fall wird kein Musterargument
angegeben.  Der Musterabgleich kann nur feststellen, ob ein Ausdruck linear in
der Variablen *x* ist.  Eine andere Variable ist nicht moglich.



```maxima
(%i1) matchdeclare (a, lambda ([e], e#0 and freeof(x, e)), b,
                    freeof(x));
(%o1)                         done
(%i2) defmatch (linearp, a*x + b);
(%o2)                        linearp
(%i3) linearp (3*z + (y + 1)*z + y^2);
(%o3)                         false
(%i4) linearp (3*x + (y + 1)*x + y^2);
                             2
(%o4)                  [b = y , a = y + 4]
```


Definition eine Aussagefunktion `checklimits(expr)`, die pruft, ob ein
Ausdruck *expr* ein bestimmtes Integral ist.



```maxima
(%i1) matchdeclare ([a, f], true);
(%o1)                         done
(%i2) constinterval (l, h) := constantp (h - l);
(%o2)        constinterval(l, h) := constantp(h - l)
(%i3) matchdeclare (b, constinterval (a));
(%o3)                         done
(%i4) matchdeclare (x, atom);
(%o4)                         done
(%i5) simp : false;
(%o5)                         false
(%i6) defmatch (checklimits, 'integrate (f, x, a, b));
(%o6)                      checklimits
(%i7) simp : true;
(%o7)                         true
(%i8) 'integrate (sin(t), t, %pi + x, 2*%pi + x);
                       x + 2 %pi
                      /
                      [
(%o8)                 I          sin(t) dt
                      ]
                      /
                       x + %pi
(%i9) checklimits (%);
(%o9)    [b = x + 2 %pi, a = x + %pi, x = t, f = sin(t)]
```

See also: `matchdeclare`, `rules`, `defrule`, `tellsimp`, `tellsimpafter`.

<!-- category: Other -->
<!-- keywords: defrule -->
<!-- signatures: defrule(rulename, pattern, replacement) -->
### Function: defrule (rulename, pattern, replacement)

Definiert eine Regel, um das Muster *pattern* durch den Ausdruck
*replacement* zu ersetzen.  Wird die Regel mit dem Namen *rulename*
mit den Funktionen `apply1`, `apply2` oder `applyb1` auf
einen Ausdruck angewendet, werden alle Teilausdrucke, die dem Muster
*pattern* entsprechen, durch den Ausdruck *replacement* ersetzt.  Sind
Mustervariablen vorhanden, die durch den Musterabgleich einen Wert erhalten
haben, werden die Werte eingesetzt und der Ausdruck wird vereinfacht.


Die Regel *rulename* kann als eine Funktion aufgefasst werden, die einen
Ausdruck durch Anwendung eines Musterabgleichs transformiert.  Die Regel kann
wie ein Funktionsaufruf auf einen Ausdruck angewendet werden.


Schlagt der Musterabgleich fehl, gibt die Regel den Wert `false`
zuruck.


Die Regel wird in die Informationsliste `rules` eingetragen.


Beispiele:


Es wird eine Regel `trig` definiert, die den Ausdruck `sin(x)^2` nach
`1-cos(x)^2` transformiert.  Diese Definition funktioniert nur, wenn das
Argument der Sinusfunktion das Symbol `x` ist.



```maxima
(%i1) defrule(trig, sin(x)^2, 1-cos(x)^2);
                            2              2
(%o1)             trig : sin (x) -> 1 - cos (x)
(%i2) trig(sin(x)^2);
                                  2
(%o2)                      1 - cos (x)
(%i3) trig(sin(y)^2);
(%o3)                         false
```


In diesem Beispiel wird zunachst mit der Funktion `matchdeclare` eine
Mustervariable `a` definiert, der jeder Ausdruck zugewiesen werden kann
und die als Argument der Regel verwendet wird.  Jetzt kann das Argument der
Sinusfunktion ein beliebiger Ausdruck sein.



```maxima
(%i1) matchdeclare(a, true);
(%o1)                         done
(%i2) defrule(trig, sin(a)^2, 1-cos(a)^2);
                            2              2
(%o2)             trig : sin (a) -> 1 - cos (a)
(%i3) trig(sin(x)^2);
                                  2
(%o3)                      1 - cos (x)
(%i4) trig(sin(exp(x))^2);
                                 2   x
(%o4)                     1 - cos (%e )
```


Die Regel kann mit der Funktion `apply1` auf Ausdrucke angewendet werden,
wobei Teilausdrucke, die das Muster enthalten transformiert werden.



```maxima
(%i5) trig(exp(sin(x)^2));
(%o5)                         false
(%i6) apply1(exp(sin(x)^2), trig);
                                   2
                            1 - cos (x)
(%o6)                     %e
```

See also: `apply1`, `apply2`, `applyb1`, `rules`, `matchdeclare`.

<!-- category: Other -->
<!-- keywords: disprule -->
<!-- signatures: disprule(rulename_1, ..., rulename_n), disprule(all) -->
### Function: disprule (rulename_1, ..., rulename_n)

Zeigt die Regeln mit den Namen *rulename_1*, ..., *rulename_n* an,
die mit den Funktionen `defrule`, `tellsimp` oder
`tellsimpafter` definiert sind, oder ein Muster, das mit der
Funktion `defmatch` definiert ist.  Die Regeln werden mit einer
Zwischenmarke `linechar` angezeigt.


Mit dem Kommando `disprule(all)` werden alle Regeln und Muster angezeigt,
die der Nutzer definiert hat und in der Informationsliste `rules`
enthalten sind.


`disprule` wertet die Argumente nicht aus.  Der Ruckgabewert ist eine
Liste mit den Zwischenmarken, denen eine Regel zugewiesen wurde.


Siehe auch die Funktion `letrules`, die die Regeln anzeigt, die mit
der Funktion `let` definiert sind.


Beispiele:



```maxima
(%i1) tellsimpafter (foo (x, y), bar (x) + baz (y));
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (x + y, special_add (x, y));
(%o2)                   [+rule1, simplus]
(%i3) defmatch (quux, mumble (x));
(%o3)                         quux
(%i4) disprule (foorule1, "+rule1", quux);
(%t4)        foorule1 : foo(x, y) -> baz(y) + bar(x)

(%t5)          +rule1 : y + x -> special_add(x, y)

(%t6)                quux : mumble(x) -> []

(%o6)                    [%t4, %t5, %t6]
(%i6) ''%;
(%o6) [foorule1 : foo(x, y) -> baz(y) + bar(x), 
     +rule1 : y + x -> special_add(x, y), quux : mumble(x) -> []]
```

See also: `defrule`, `tellsimp`, `tellsimpafter`, `defmatch`, `linechar`, `rules`, `letrules`, `let`.

<!-- category: Other -->
<!-- keywords: let -->
<!-- signatures: let(prod, repl), let(prod, repl, predname, arg_1, ..., arg_n), let([prod, repl, predname, arg_1, ..., arg_n], package_name) -->
### Function: let (prod, repl)

Definiert eine Regel, die mit der Funktion `letsimp` auf einen Ausdruck
angewendet werden kann, so dass *prod* durch *repl* ersetzt wird.
Das Argument *prod* ist ein Produkt von positiven oder negativen Potenzen
der folgenden Terme:



- *
Atome, nach denen die Funktion `letsimp` wortlich sucht, wenn diese keine
Mustervariablen sind, die mit Funktion `matchdeclare` definiert sind,
sowie Atome, die Mustervariablen sind.  In diesem Fall fuhrt die Funktion
`letsimp` einen Musterabgleich fur die Atome durch, auf die die mit
der Funktion `matchdeclare` zugeordnete Aussagefunktion zutrifft.
- *
Terme wie `sin(x)`, `n!` oder `f(x,y)`:  wie fur Atome
sucht die Funktion `letsimp` nach wortlichen Ubereinstimmungen,
außer wenn die Argumente der Terme Mustervariablen sind, die mit der
Funktion `matchdeclare` definiert sind.  In diesem Fall wird ein
Musterabgleich ausgefuhrt.


Ein Term mit einer positiven Potenz stimmt mit einem Ausdruck nur dann
uberein, wenn dieser mindestens dieselbe Potenz hat.  Entsprechend gilt fur
einen Term mit einer negativen Potenz, dass dieser dann mit einem Ausdruck
ubereinstimmt, wenn dieser mindestens dieselbe negative Potenz hat.  Fur
negative Potenzen wird eine Ubereinstimmung nur dann gefunden, wenn
die Optionsvariable `letrat` den Wert `true` hat.


Hat die Funktion `let` eine Aussagefunktion *predname* als Argument
mit den Argumenten *arg_1*, ..., *arg_n*, wird eine
Ubereinstimmung dann festgestellt, wenn der Ausdruck
`predname(arg_1', ..., arg_n')` das Ergebnis `true` hat.  Dabei sind
die Argumente *arg_i’* die Werte aus dem Musterabgleich.  Die Argumente
*arg_i* konnen die Namen von Variablen oder Termen sein, die im Ausdruck
*pred* auftreten.  *repl* kann ein beliebiger rationaler Ausdruck sein.
Treten irgendwelche der Symbole oder Argumente aus *prod* im Argument
*repl* auf, wird die entsprechende Substitution ausgefuhrt.


Die Optionsvariable `letrat` kontrolliert die Vereinfachung von Quotienten
durch `letsimp`.  Hat `letrat` den Wert `false`, werden der
Zahler und der Nenner eines Bruches einzeln vereinfacht.  Der Bruch als ganzes
wird dagegen nicht vereinfacht.  Hat die Optionsvariable `letrat` den Wert
`true`, werden nacheinander der Zahler, der Nenner und dann der Bruch
vereinfacht.


Die Funktion `letsimp` kann mit verschiedenen Regelpaketen arbeiten.  Jedes
Regelpaket kann eine beliebige Anzahl an Regeln enthalten.  Das Kommando
`let([prod, repl, predname, arg_1, ..., arg_n], package_name)` fugt die Regel *predname* dem Paket
*package_name* hinzu.


Die Optionsvariable `current_let_rule_package` enthalt den Namen des
Regelpaketes, das aktuell von der Funktion `letsimp` verwendet wird.  Der
Optionsvariablen kann jedes mit dem Kommando `let` definierte Regelpaket 
zugewiesen werden.  Wird mit `letsimp(expr, package_name)`
ein Regelpaket als Argument ubergeben, wird dieses anstatt dem in 
`current_let_rule_package` enthaltene Regelpaket fur die Vereinfachung
verwendet.  Wenn nicht anders spezifiziert, hat `current_let_rule_package`
den Standardwert `default_let_rule_package`.


Die Informationsliste `let_rule_packages` enthalt die definierten
Regelpakete.  Mit der Funktion `letrules` konnen alle definierten Regeln
oder Regeln einzelner Pakete angezeigt werden.


Beispiele:


Die Funktion `isintegerp` pruft auch, ob Variablen oder Ausdrucke eine
ganze Zahl reprasentieren.  Es wird eine Regel definiert, die dann angewendet
wird, wenn das Argument eine ganze Zahl reprasentiert.



```maxima
(%i1) isintegerp(x) := featurep(x, integer)$

(%i2) let(tan(x), sin(x)/cos(x), isintegerp, x);
(%o2) tan(x) --> sin(x)/cos(x) where isintegerp(x)

(%i3) letsimp(tan(x));
(%o3) tan(x)

(%i4) declare(x, integer)$

(%i5) letsimp(tan(x));
(%o5) sin(x)/cos(x)
(%i6) letsimp(tan(1));
(%o6) tan(1)
```


Weitere Beispiele:



```maxima
(%i1) matchdeclare ([a, a1, a2], true)$
(%i2) oneless (x, y) := is (x = y-1)$
(%i3) let (a1*a2!, a1!, oneless, a2, a1);
(%o3)         a1 a2! --> a1! where oneless(a2, a1)
(%i4) letrat: true$
(%i5) let (a1!/a1, (a1-1)!);
                        a1!
(%o5)                   --- --> (a1 - 1)!
                        a1
(%i6) letsimp (n*m!*(n-1)!/m);
(%o6)                      (m - 1)! n!
(%i7) let (sin(a)^2, 1 - cos(a)^2);
                        2               2
(%o7)                sin (a) --> 1 - cos (a)
(%i8) letsimp (sin(x)^4);
                        4           2
(%o8)                cos (x) - 2 cos (x) + 1
```

See also: `letsimp`, `matchdeclare`, `letrat`, `current_let_rule_package`, `default_let_rule_package`, `let_rule_packages`, `letrules`.

<!-- category: Other -->
<!-- keywords: let_rule_packages -->
<!-- signatures: let_rule_packages -->
### Variable: let_rule_packages

Standardwert: `[default_let_rule_package]`


`let_rule_packages` ist eine Informationsliste mit den vom Nutzer mit der
Funktion `let` definierten Regelpaketen.

See also: `let`.

<!-- category: Other -->
<!-- keywords: letrat -->
<!-- signatures: letrat -->
### Variable: letrat

Standardwert: `false`


Hat die Optionsvariable `letrat` den Wert `false`, werden von der
Funktion `letsimp` der Zahler und der Nenner eines Bruches einzeln
vereinfacht.  Der Bruch als ganzes wird dagegen nicht vereinfacht.


Hat die Optionsvariable `letrat` den Wert `true`, werden nacheinander
der Zahler, der Nenner und dann der Bruch vereinfacht.


Beispiele:



```maxima
(%i1) matchdeclare (n, true)$
(%i2) let (n!/n, (n-1)!);
                         n!
(%o2)                    -- --> (n - 1)!
                         n
(%i3) letrat: false$
(%i4) letsimp (a!/a);
                               a!
(%o4)                          --
                               a
(%i5) letrat: true$
(%i6) letsimp (a!/a);
(%o6)                       (a - 1)!
```

See also: `letsimp`.

<!-- category: Other -->
<!-- keywords: letrules -->
<!-- signatures: letrules(), letrules(package_name) -->
### Function: letrules ()

Zeigt die Regeln eines Regelpaketes an.  Das Kommando `letrules()` zeigt
die Regeln des aktuellen Regelpaketes an, das durch die Optionsvariable
`current_let_rule_package` bezeichnet wird.  Das Kommando
`letrules(package_name)` zeigt die Regeln des Paketes
*package_name* an.


Wenn der Optionsvariablen `current_let_rule_package` kein Name eines
Paketes zugewiesen wurde, enthalt es den Standardwert
`default_let_rule_package`.


Siehe auch die Funktion `disprule`, um Regeln anzuzeigen, die mit
den Funktionen `tellsimp`, `tellsimpafter` und `defrule`
definiert wurden.


Beispiel:


Im folgenden Beispiel werden einem Paket mit dem Namen `trigrules` zwei
Regeln hinzugefugt.  Die Regeln werden mit dem Kommando 
`letrules(trigrules)` angezeigt.  Wird das Paket zum aktuellen Paket
erklart, indem es der Variablen `current_let_rule_package` zugewiesen
wird, dann werden die Regeln auch mit dem Kommando `letrules()` angezeigt.



```maxima
(%i1) let([sin(x)^2, 1-cos(x)^2], trigrules);
                        2               2
(%o1)                sin (x) --> 1 - cos (x)
(%i2) let([tan(x), sin(x)/cos(x)], trigrules);
                                   sin(x)
(%o2)                   tan(x) --> ------
                                   cos(x)
(%i3) letrules(trigrules);

                                   sin(x)
                        tan(x) --> ------
                                   cos(x)



                        2               2
                     sin (x) --> 1 - cos (x)


(%o3)                         done
(%i4) letrules();
(%o4)                         done
(%i5) current_let_rule_package: trigrules;
(%o5)                       trigrules
(%i6) letrules();
                                   sin(x)
                        tan(x) --> ------
                                   cos(x)

                        2               2
                     sin (x) --> 1 - cos (x)

(%o6)                         done
```

See also: `current_let_rule_package`, `default_let_rule_package`, `disprule`, `tellsimp`, `tellsimpafter`, `defrule`.

<!-- category: Other -->
<!-- keywords: letsimp -->
<!-- signatures: letsimp(expr), letsimp(expr, package_name), letsimp(expr, package_name_1, ..., package_name_n) -->
### Function: letsimp (expr)

Wendet die Regeln, die mit der Funktion `let` definiert sind,
solange an, bis sich das Argument *expr* nicht mehr andert.
`letsimp(expr)` wendet die aktuellen Regeln an, die mit der
Optionsvariablen `current_let_rule_package` bezeichnet werden.


`letsimp(expr, package_name)` wendet die Regeln des
Argumentes *package_name* an.  Die Optionsvariable
`current_let_rule_package` andert ihren Wert nicht.  Es konnen auch
mehrere Regelpakete *package_name_1*, ..., *package_name_n*
angegeben werden.


Die Optionsvariable `letrat` kontrolliert die Vereinfachung von Quotienten
durch `letsimp`.  Hat `letrat` den Wert `false`, werden der
Zahler und der Nenner eines Bruches einzeln vereinfacht.  Der Bruch als ganzes
wird dagegen nicht vereinfacht.  Hat die Optionsvariable `letrat` den Wert
`true`, werden nacheinander der Zahler, der Nenner und dann der Bruch
vereinfacht.

See also: `let`, `current_let_rule_package`, `letrat`.

<!-- category: Other -->
<!-- keywords: matchdeclare -->
<!-- signatures: matchdeclare(a_1, pred_1, ..., a_n, pred_n) -->
### Function: matchdeclare (a_1, pred_1, ..., a_n, pred_n)

Mit der Funktion `matchdeclare` werden Mustervariablen definiert.
`matchdeclare` ordnet eine Aussagefunktion *pred_k* einer Variable
oder eine Liste von Variablen *a_k* zu, so dass *a_k* bei einem
Musterabgleich mit Ausdrucken ubereinstimmt, fur die die Aussage ein
anderes Ergebnis als `false` hat.


Eine Aussagefunktion *pred_i* kann durch den Namen einer Funktion, einen
Lambda-Ausdruck, einen Funktionsaufruf, einen Lambda-Ausdruck, dem das letzte
Argument fehlt, oder die Werte `true` oder `all` bezeichnet werden.
Ist die Aussagefunktion ein Funktionsaufruf oder ein Lambda-Aufruf, dann wird
der zu testende Ausdruck der Liste der Argumente hinzugefugt.  Die Argumente
werden ausgewertet, wenn der Musterabgleich ausgefuhrt wird.  Ist die Aussage
der Name einer Funktion oder ein Lambda-Ausdruck, ist die zu testende Aussage
das einzige Argument.  Die Aussagefunktion braucht noch nicht definiert zu sein,
wenn mit `matchdeclare` eine Mustervariable definiert wird, da die
Aussagefunktion erst aufgerufen wird, wenn ein Musterabgleich durchgefuhrt
wird.


Eine Aussagefunktion kann einen logischen Ausdruck oder die Werte `true`
oder `false` zuruckgeben.  Logische Ausdrucke werden von der Funktion
`is` ausgewertet, wenn die Regel angewendet wird.  Daher ist es nicht
notwendig, dass die Aussagefunktion selbst die Funktion `is` aufruft.


Wenn fur einen Ausdruck eine Ubereinstimmung bei einem Musterabgleich
gefunden wird, wird der Mustervariablen der Ausdruck zugewiesen.  Jedoch nicht
fur Mustervariablen, die Argumente der Addition `+` oder Multiplikation
`*` sind.  Diese Operatoren werden besonders behandelt.  Andere Maxima oder
vom Nutzer definierte N-ary-Operatoren werden dagegen wie normale Funktionen
behandelt.


Im Falle der Addition und der Multiplikation kann der Mustervariablen ein
einzelner Term zugewiesen werden, fur den der Musterabgleich zu einer
Uberstimmung fuhrt, oder auch eine Summe oder ein Produkt von Termen.  Die
mehrfache Ubereinstimmung hat Vorrang.  Aussagefunktionen werden in der
Reihenfolge ausgewertet, in der die der Aussagefunktion zugeordneten
Mustervariablen im Muster auftreten.  Fuhrt der Musterabgleich fur einen
Term zu einer Ubereinstimmung mit mehreren Aussagefunktionen, dann wird der
Term der Mustervariablen zugeordnet fur den die erste Aussagefunktion
zutrifft.  Jede Aussagefunktion wird zunachst auf alle Argumente einer Summe
oder eines Produktes angewendet, bevor die nachste Aussagefunktion ausgewertet
wird.  Wird fur die Zahlen 0 oder 1 eine Ubereinstimmung gefunden und es
sind keine weiteren Terme vorhanden, wird der Mustervariablen 0 oder 1
zugewiesen.


Der Algorithmus, um Muster abzugleichen, die die Addition oder die
Multiplikation als Operanden enthalten, kann von der Anordnung der Terme im
Muster oder im zu prufenden Ausdruck abhangen.  Solange sich jedoch die
einzelnen Aussagefunktionen gegeneinander ausschließen, wird das Ergebnis
nicht von der Reihenfolge der Argumente beeinflußt.


Der Aufruf von `matchdeclare` fur eine Variable *a* uberschreibt
eine vorhergehende Definition fur diese Variable.  Wird eine Regel definiert,
ist die letzte mit `matchdeclare` definierte Zuordnung zu einer
Aussagefunktion wirksam.  Der erneute Aufruf von `matchdeclare` fur eine
Variable hat keinen Einfluss auf bereits vorhandene Regeln.


Das Kommando `propvars(matchdeclare)` gibt eine Liste der Variablen
zuruck, die mit `matchdeclare` als Mustervariable definiert sind.
`printprops(a, matchdeclare)` gibt die der Variable *a*
zugeordnete Aussagefunktion zuruck.  `printprops(all, matchdeclare)`
gibt die Aussagefunktionen aller Mustervariablen zuruck.  Mit dem Kommando
`remove(a, matchdeclare)` wird die Definition von *a* als
Mustervariable entfernt.  Siehe auch die Funktionen `propvars`,
`printprops` und `remove`.


Mit den Funktionen `defmatch`, `defrule`,
`tellsimp`, `tellsimpafter` und `let` werden Regeln
definiert, die fur Ausdrucke einen Musterabgleich ausfuhren, wobei die
Mustervariablen mit den Werten belegt werden, fur die eine Ubereinstimmung
gefunden wird.


`matchdeclare` wertet die Argumente nicht aus.  `matchdeclare` gibt
immer `done` als Ergebnis zuruck.


Beispiele:


Eine Aussagefunktion kann mit dem Namen einer Funktion, einem Lambda-Ausdruck,
einem Funktionsaufruf, einem Lambda-Ausdruck, dem das letzte Argument fehlt,
oder den Werten `true` oder `all` bezeichnet werden.



```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) matchdeclare (bb, lambda ([x], x > 0));
(%o2)                         done
(%i3) matchdeclare (cc, freeof (%e, %pi, %i));
(%o3)                         done
(%i4) matchdeclare (dd, lambda ([x, y], gcd (x, y) = 1) (1728));
(%o4)                         done
(%i5) matchdeclare (ee, true);
(%o5)                         done
(%i6) matchdeclare (ff, all);
(%o6)                         done
```


Wird fur einen Ausdruck beim Musterabgleich eine Ubereinstimmung gefunden,
wird dieser der Mustervariablen zugewiesen.



```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) defrule (r1, bb^aa, ["integer" = aa, "atom" = bb]);
                    aa
(%o2)        r1 : bb   -> [integer = aa, atom = bb]
(%i3) r1 (%pi^8);
(%o3)               [integer = 8, atom = %pi]
```


Im Falle der Addition und Multiplikation kann der Mustervariablen ein einzelner
Term zugewiesen werden, welcher mit der Aussage ubereinstimmt, aber auch 
eine Summe oder ein Produkt solcher Ausdrucke.



```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + sin(x));
(%o3)     [all atoms = 8, all nonatoms = sin(x) + a b]
(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * sin(x));
(%o5)    [all atoms = 8, all nonatoms = (b + a) sin(x)]
```


Wird nach Ubereinstimmungen fur die Argumente der Operatoren `+` oder
`*` gesucht und schließen sich die Aussagefunktionen gegeneinander
aus, ist das Ergebnis unabhangig von der Anordnung der Terme.



```maxima
(%i1) matchdeclare (aa, atom, bb, lambda ([x], not atom(x)));
(%o1)                         done
(%i2) defrule (r1, aa + bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb + aa partitions `sum'
(%o2)  r1 : bb + aa -> [all atoms = aa, all nonatoms = bb]
(%i3) r1 (8 + a*b + %pi + sin(x) - c + 2^n);
                                                     n
(%o3) [all atoms = %pi + 8, all nonatoms = sin(x) + 2  - c + a b]
(%i4) defrule (r2, aa * bb, ["all atoms" = aa, "all nonatoms" =
               bb]);
bb aa partitions `product'
(%o4)   r2 : aa bb -> [all atoms = aa, all nonatoms = bb]
(%i5) r2 (8 * (a + b) * %pi * sin(x) / c * 2^n);
                                                  n
                                         (b + a) 2  sin(x)
(%o5) [all atoms = 8 %pi, all nonatoms = -----------------]
                                                 c
```


Die Funktionen `propvars` und `printprops` geben Informationen uber
Mustervariablen aus.



```maxima
(%i1) matchdeclare ([aa, bb, cc], atom, [dd, ee], integerp);
(%o1)                         done
(%i2) matchdeclare (ff, floatnump, gg, lambda ([x], x > 100));
(%o2)                         done
(%i3) propvars (matchdeclare);
(%o3)             [aa, bb, cc, dd, ee, ff, gg]
(%i4) printprops (ee, matchdeclare);
(%o4)                    [integerp(ee)]
(%i5) printprops (gg, matchdeclare);
(%o5)              [lambda([x], x > 100, gg)]
(%i6) printprops (all, matchdeclare);
(%o6) [lambda([x], x > 100, gg), floatnump(ff), integerp(ee), 
                      integerp(dd), atom(cc), atom(bb), atom(aa)]
```

See also: `is`, `propvars`, `printprops`, `remove`, `defmatch`, `defrule`, `tellsimp`, `tellsimpafter`, `let`.

<!-- category: Other -->
<!-- keywords: maxapplydepth -->
<!-- signatures: maxapplydepth -->
### Variable: maxapplydepth

Standardwert: 10000


`maxapplydepth` ist die maximale Verschachtelungstiefe fur die die
Funktionen `apply1` und `apply2` auf die Baumstruktur eines Ausdrucks
angewendet werden.

See also: `apply1`, `apply2`.

<!-- category: Other -->
<!-- keywords: maxapplyheight -->
<!-- signatures: maxapplyheight -->
### Variable: maxapplyheight

Standardwert: 10000


`maxapplyheight` ist die maximale Verschachtelungstiefe fur die die
Funktion `applyb1` Bottom-up auf die Baumstruktur eines Ausdrucks
angewendet wird.

See also: `applyb1`.

<!-- category: Other -->
<!-- keywords: remlet -->
<!-- signatures: remlet(prod, package_name), remlet(), remlet(all), remlet(all, package_name) -->
### Function: remlet (prod, package_name)

Entfernt die Regel *prod* –> *repl*, die zuletzt mit der Funktion
`let` definiert wurde.  Wird mit dem Argument *package_name*
ein Paket angegeben, wird die Regeln aus dem entsprechenden Paket entfernt.


`remlet()` und `remlet(all)` entfernen alle Regeln aus dem aktuellen
Paket, das mit `current_let_rule_package` bezeichnet ist.  Wird der Name
eines Regelpaketes als Argument angegeben, werden zusatzlich die Regeln dieses
Paketes entfernt.


Soll eine vorhandene Regel durch eine neue Definition ersetzt werden, muss die
Regel nicht zuvor mit `remlet` entfernt werden.  Die neue Definition
uberschreibt eine vorhandene Regel.  Wurde eine vorhandene Regel
uberschrieben und wird die letzte Regel entfernt, dann ist die vorhergehende
Regel wieder aktiv.


Siehe auch die Funktion `remrule`, um Regeln zu entfernen, die mit
den Funktionen `tellsimp` oder `tellsimpafter` definiert sind.

See also: `let`, `current_let_rule_package`, `remrule`, `tellsimp`, `tellsimpafter`.

<!-- category: Other -->
<!-- keywords: remrule -->
<!-- signatures: remrule(op, rulename), remrule(op, all) -->
### Function: remrule (op, rulename)

Entfernt Regeln, die mit den Funktionen `tellsimp` oder 
`tellsimpafter` definiert sind.


`remrule(op, rulename)` entfernt die Regel mit dem Namen
*rulename* vom Operator *op*.  Ist der Operator *op* ein 
Maxima-Operator oder ein nutzerdefinierter Operator, der mit Funktionen wie
`infix` oder `prefix` definiert wurde, muss der Name des Operators
*op* als eine Zeichenkette in Anfuhrungszeichen angegeben werden.


`remrule(op, all)` entfernt alle Regeln des Operators *op*.


Siehe auch die Funktion `remlet`, um Regeln zu entfernen, die mit der
Funktion `let` definiert sind.


Beispiele:



```maxima
(%i1) tellsimp (foo (aa, bb), bb - aa);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (aa + bb, special_add (aa, bb));
(%o2)                   [+rule1, simplus]
(%i3) infix ("@@");
(%o3)                          @@
(%i4) tellsimp (aa @@ bb, bb/aa);
(%o4)                   [@@rule1, false]
(%i5) tellsimpafter (quux (%pi, %e), %pi - %e);
(%o5)                  [quuxrule1, false]
(%i6) tellsimpafter (quux (%e, %pi), %pi + %e);
(%o6)             [quuxrule2, quuxrule1, false]
(%i7) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
       quux (%e, %pi)];
                                     bb
(%o7) [bb - aa, special_add(aa, bb), --, %pi - %e, %pi + %e]
                                     aa
(%i8) remrule (foo, foorule1);
(%o8)                          foo
(%i9) remrule ("+", ?\+rule1);
(%o9)                           +
(%i10) remrule ("@@", ?\@\@rule1);
(%o10)                         @@
(%i11) remrule (quux, all);
(%o11)                        quux
(%i12) [foo (aa, bb), aa + bb, aa @@ bb, quux (%pi, %e),
        quux (%e, %pi)];
(%o12) [foo(aa, bb), bb + aa, aa @@ bb, quux(%pi, %e), 
                                         quux(%e, %pi)]
```

See also: `tellsimp`, `tellsimpafter`, `infix`, `prefix`, `remlet`, `let`.

<!-- category: Other -->
<!-- keywords: rules -->
<!-- signatures: rules -->
### Variable: rules

Standardwert: `[]`


`rules` ist eine Informationsliste, die die vom Nutzer mit den Funktionen
`tellsimp`, `tellsimpafter`, `defmatch` oder `defrule`
definierten Regeln enthalt.


Regeln, die mit der Funktion `let` definiert sind, sind nicht in der Liste
`rules` enthalten.  Diese Regeln werden in Paketen organisiert, die in
der Systemvariablen `let_rule_packages` aufgelistet und mit der Funktion
`letrules` angezeigt werden.


Siehe auch die Systemvariable `infolists`.

See also: `let`, `let_rule_packages`, `letrules`, `infolists`.

<!-- category: Other -->
<!-- keywords: tellsimp -->
<!-- signatures: tellsimp(pattern, replacement) -->
### Function: tellsimp (pattern, replacement)

`tellsimp` ist vergleichbar mit der Funktion `tellsimpafter`,
wobei mit `tellsimp` Regeln fur die Vereinfachung von Ausdrucken
definiert werden, die noch vor den Regeln angewendet werden, die intern in
Maxima bekannt sind.


`tellsimp` wird daher eingesetzt, wenn Maxima Regeln fur die
Vereinfachung des Ausdruckes kennt, es jedoch notwendig ist, noch vor Anwendung
dieser Regeln den Ausdruck auf eine andere Art zu modifizieren.  Fur den Fall
das Maxima den Ausdruck nicht ausreichend vereinfacht, kann es besser sein, eine
Regel mit der Funktion `tellsimpafter` zu definieren.


Das Argument *pattern* kann keine Summe, kein Produkt, keine einzelne
Variable und keine Zahl sein.


Regeln die mit `tellsimp` definiert werden, werden in die Informationsliste
`rules` aufgenommen.


Beispiele:



```maxima
(%i1) matchdeclare (x, freeof (%i));
(%o1)                         done
(%i2) %iargs: false$
(%i3) tellsimp (sin(%i*x), %i*sinh(x));
(%o3)                 [sinrule1, simp-%sin]
(%i4) trigexpand (sin (%i*y + x));
(%o4)         sin(x) cos(%i y) + %i cos(x) sinh(y)
(%i5) %iargs:true$
(%i6) errcatch(0^0);
 0
0  has been generated
(%o6)                          []
(%i7) ev (tellsimp (0^0, 1), simp: false);
(%o7)                  [^rule1, simpexpt]
(%i8) 0^0;
(%o8)                           1
(%i9) remrule ("^", %th(2)[1]);
(%o9)                           ^
(%i10) tellsimp (sin(x)^2, 1 - cos(x)^2);
(%o10)                 [^rule2, simpexpt]
(%i11) (1 + sin(x))^2;
                                      2
(%o11)                    (sin(x) + 1)
(%i12) expand (%);
                                   2
(%o12)               2 sin(x) - cos (x) + 2
(%i13) sin(x)^2;
                                  2
(%o13)                     1 - cos (x)
(%i14) kill (rules);
(%o14)                        done
(%i15) matchdeclare (a, true);
(%o15)                        done
(%i16) tellsimp (sin(a)^2, 1 - cos(a)^2);
(%o16)                 [^rule3, simpexpt]
(%i17) sin(y)^2;
                                  2
(%o17)                     1 - cos (y)
```

See also: `tellsimpafter`, `rules`.

<!-- category: Other -->
<!-- keywords: tellsimpafter -->
<!-- signatures: tellsimpafter(pattern, replacement) -->
### Function: tellsimpafter (pattern, replacement)

Definiert eine Regel fur die Vereinfachung eines Ausdrucks, die nach Anwendung
der Regeln angewendet wird, die Maxima intern kennt.  *pattern* ist ein
Ausdruck, der Mustervariablen enthalt, die mit der Funktion
`matchdeclare` definiert sind und weitere Symbole und Operatoren, fur
die die wortliche Ubereinstimmung bei einem Musterabgleich angenommen wird.
*replacement* wird in den Ausdruck substituiert, wenn der Musterabgleich
das Muster *pattern* im Ausdruck findet.  Den Mustervariablen in
*replacement* werden die Werte des Musterabgleichs zugewiesen.


Das Muster *pattern* kann ein beliebiger Ausdruck sein, in dem der 
Hauptoperator keine Mustervariable ist.  Die neue Regel wird nach dem
Hauptoperator des Musters benannt und diesem zugeordnet.  Der Name von
Funktionen, mit einer unten beschriebenen Ausnahme, Listen und Arrays konnen
in *pattern* nicht als eine Mustervariable auftreten.  Daher konnen
Ausdrucke wie `aa(x)` oder `bb[y]` nicht als Muster verwendet
werden, wenn `aa` oder `bb` Mustervariablen sind.  Die Namen
von Funktionen, Listen und Arrays, welche Mustervariablen sind, konnen dann
in dem Muster *pattern* auftreten, wenn sie nicht der Hauptoperator sind.


Es gibt eine Ausnahme der oben genannten Einschrankung fur die Verwendung
von Funktionsnamen.  Der Name einer indizierten Funktion wie `aa[x](y)`
kann eine Mustervariable sein, da der Hauptoperator nicht `aa` ist, sondern
das interne Symbol `mqapply`.  Dies ist eine Konsequenz der internen
Darstellung einer indizierten Funktion.


Regeln fur die Vereinfachung werden nach der Auswertung eines Ausdrucks
angewendet, sofern die Auswertung, zum Beispiel mit dem Schalter
`noeval`, nicht unterdruckt wurde.  Regeln, die mit
`tellsimpafter` definiert sind, werden nach den internen Regeln und in der
Reihenfolge angewendet, in der sie definiert sind.  Die Regeln fur die
Vereinfachung werden zunachst fur Teilausdrucke und zuletzt fur den
ganzen Ausdruck angewendet.  Es kann notwendig sein, Regeln fur die
Vereinfachung mehrfach zum Beispiel mit dem Quote-Quote-Operator
`''` oder dem Auswertungsschalter `infeval` anzuwenden, um zu
erreichen, dass alle Regeln angewendet werden.


Mustervariable werden als lokale Variablen in Regeln fur die Vereinfachung
behandelt.  Sobald eine Regel definiert ist, beeinflusst die Zuweisung eines
Wertes an die Mustervariable nicht die Regel und die Variable wird nicht von
der Regel beeinflusst.  Die Zuweisung an eine Mustervariable, die aufgrund eines
erfolgreichen Musterabgleichs vorgenommen wird, beeinflusst nicht den aktuellen
Wert der Variablen.  Jedoch sind die Eigenschaften der Mustervariablen, wie sie
zum Beispiel auch mit der Funktion `put` definiert werden konnen, global
in Maxima.


Eine mit `tellsimpafter` definierte Regel wird nach dem Hauptoperator des
Musters *pattern* benannt.  Regeln fur Maxima-Operatoren und fur
Funktionen, die mit `infix`, `prefix`, `postfix`,
`matchfix` und `nofix` als Operator definiert sind, haben einen
Lisp-Bezeichner als Namen.  Alle anderen Regeln erhalten einen Maxima-Bezeichner
als Namen.


















`tellsimpafter` wertet die Argumente nicht aus.  `tellsimpafter` gibt
eine Liste der Regeln zuruck, die fur den Hauptoperator des Musters
*pattern* definiert sind.


Siehe auch die Funktionen `matchdeclare`, `defmatch`,
`defrule`, `tellsimp`, `remrule` und
`clear_rules`.


Beispiele:


Das Muster *pattern* kann ein beliebiger Ausdruck sein, in dem der
Hauptoperator keine Mustervariable ist.



```maxima
(%i1) matchdeclare (aa, atom, [ll, mm], listp, xx, true)$
(%i2) tellsimpafter (sin (ll), map (sin, ll));
(%o2)                 [sinrule1, simp-%sin]
(%i3) sin ([1/6, 1/4, 1/3, 1/2, 1]*%pi);
                    1  sqrt(2)  sqrt(3)
(%o3)              [-, -------, -------, 1, 0]
                    2     2        2
(%i4) tellsimpafter (ll^mm, map ("^", ll, mm));
(%o4)                  [^rule1, simpexpt]
(%i5) [a, b, c]^[1, 2, 3];
                                2   3
(%o5)                      [a, b , c ]
(%i6) tellsimpafter (foo (aa (xx)), aa (foo (xx)));
(%o6)                   [foorule1, false]
(%i7) foo (bar (u - v));
(%o7)                    bar(foo(u - v))
```


Regeln werden in der Reihenfolge angewendet, in der sie definiert sind.
Treffen zwei Regeln bei einem Musterabgleich zu, wird die zuerst definierte
Regel angewendet.



```maxima
(%i1) matchdeclare (aa, integerp);
(%o1)                         done
(%i2) tellsimpafter (foo (aa), bar_1 (aa));
(%o2)                   [foorule1, false]
(%i3) tellsimpafter (foo (aa), bar_2 (aa));
(%o3)              [foorule2, foorule1, false]
(%i4) foo (42);
(%o4)                       bar_1(42)
```


Mustervariable werden als lokale Variable beim Musterabgleich der mit der
Funktion `tellsimpafter` definierten Regel behandelt.  Im Unterschied dazu
werden von Regeln, die mit `defmatch` definiert sind, Mustervariable als
globale Variable behandelt.



```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) bb: 12345;
(%o3)                         12345
(%i4) foo (42, %e);
(%o4)                 bar(aa = 42, bb = %e)
(%i5) bb;
(%o5)                         12345
```


Die Eigenschaften von Mustervariablen sind global, auch wenn die Werte lokal 
sind.  In diesem Beispiel wird eine Eigenschaft fur die Zuweisung an eine
Variable mit der Funktion `define_variable` definiert.  Die Eigenschaft 
des Symbols `bb` ist global in Maxima.



```maxima
(%i1) matchdeclare (aa, integerp, bb, atom);
(%o1)                         done
(%i2) tellsimpafter (foo(aa, bb), bar('aa=aa, 'bb=bb));
(%o2)                   [foorule1, false]
(%i3) foo (42, %e);
(%o3)                 bar(aa = 42, bb = %e)
(%i4) define_variable (bb, true, boolean);
(%o4)                         true
(%i5) foo (42, %e);
Error: bb was declared mode boolean, has value: %e
 -- an error.  Quitting.  To debug this try debugmode(true);
```


Regeln werden nach dem Hauptoperator benannt.  Die Namen der Regeln fur
Maxima-Funktionen und nutzerdefinierte Operatoren sind Lisp-Bezeichner.  Alle
anderen Namen sind Maxima-Bezeichner.



```maxima
(%i1) tellsimpafter (foo (%pi + %e), 3*%pi);
(%o1)                   [foorule1, false]
(%i2) tellsimpafter (foo (%pi * %e), 17*%e);
(%o2)              [foorule2, foorule1, false]
(%i3) tellsimpafter (foo (%i ^ %e), -42*%i);
(%o3)         [foorule3, foorule2, foorule1, false]
(%i4) tellsimpafter (foo (9) + foo (13), quux (22));
(%o4)                   [+rule1, simplus]
(%i5) tellsimpafter (foo (9) * foo (13), blurf (22));
(%o5)                  [*rule1, simptimes]
(%i6) tellsimpafter (foo (9) ^ foo (13), mumble (22));
(%o6)                  [^rule1, simpexpt]
(%i7) rules;
(%o7) [foorule1, foorule2, foorule3, +rule1, *rule1, ^rule1]
(%i8) foorule_name: first (%o1);
(%o8)                       foorule1
(%i9) plusrule_name: first (%o4);
(%o9)                        +rule1
(%i10) remrule (foo, foorule1);
(%o10)                         foo
(%i11) remrule ("^", ?\^rule1);
(%o11)                          ^
(%i12) rules;
(%o12)        [foorule2, foorule3, +rule1, *rule1]
```


Ein ausgearbeitetes Beispiel der nicht-kommutativen Multiplikation.



```maxima
(%i1) gt (i, j) := integerp(j) and i < j;
(%o1)           gt(i, j) := integerp(j) and i < j
(%i2) matchdeclare (i, integerp, j, gt(i));
(%o2)                         done
(%i3) tellsimpafter (s[i]^^2, 1);
(%o3)                 [^^rule1, simpncexpt]
(%i4) tellsimpafter (s[i] . s[j], -s[j] . s[i]);
(%o4)                   [.rule1, simpnct]
(%i5) s[1] . (s[1] + s[2]);
(%o5)                    s  . (s  + s )
                          1     2    1
(%i6) expand (%);
(%o6)                      1 - s  . s
                                2    1
(%i7) factor (expand (sum (s[i], i, 0, 9)^^5));
(%o7) 100 (s  + s  + s  + s  + s  + s  + s  + s  + s  + s )
            9    8    7    6    5    4    3    2    1    0
```

See also: `matchdeclare`, `noeval`, `infeval`, `put`, `infix`, `prefix`, `postfix`, `matchfix`, `nofix`, `defmatch`, `defrule`, `tellsimp`, `remrule`, `clear_rules`, `define_variable`.

