## Maximas Datenbank

<!-- category: Other -->
<!-- keywords: activate -->
<!-- signatures: activate(context_1, ..., context_n) -->
### Function: activate (context_1, ..., context_n)

Das Kommando `activate(context)` aktiviert den Kontext *context*.
Der Funktion `activate` konnen mehrere Kontexte *context_1*, ...,
*context_n* ubergeben werden.  Nur die Aussagen und Fakten eines aktiven
Kontextes stehen fur die Auswertung von Aussagen zur Verfugung.


Maxima gibt `done` zuruck, wenn der Kontext erfolgreich aktiviert werden
konnte oder wenn der Kontext bereits aktiv ist.  Wird versucht einen nicht 
existierenden Kontext zu aktivieren, gibt Maxima eine Fehlermeldung aus.


Das Kommando `facts()` gibt die Fakten und Aussagen des aktuellen Kontextes
aus.  Die Aussagen und Fakten anderer Kontexte konnen zwar aktiv sein, sind 
aber in der Ruckgabe von `facts` nicht enthalten.  Um die Aussagen und 
Fakten eines anderen als des aktuellen Kontexts auszugeben, kann das Kommando 
`facts(context)` ausgefuhrt werden.


Die Systemvariable `activecontexts` enthalt eine Liste der aktiven
Kontexte.  Siehe auch die Systemvariable `contexts` fur eine Liste
aller Kontexte, die Maxima kennt.

See also: `activecontexts`, `contexts`.

<!-- category: Other -->
<!-- keywords: activecontexts -->
<!-- signatures: activecontexts -->
### Variable: activecontexts

Standardwert: `[]`


Die Systemvariable `activecontexts` enthalt eine Liste der Kontexte, die
mit der Funktion `activate` aktiviert wurden.  Unterkontexte sind aktiv,
ohne dass die Funktion `activate` aufgerufen werden muss und sind nicht in
der Liste `activecontexts` enthalten.  Siehe auch die Funktion
`activate` fur die Aktivierung eines Kontextes und die Systemvariable
`contexts` fur eine Liste aller vorhandenen Kontexte.

See also: `activate`, `contexts`.

<!-- category: Other -->
<!-- keywords: ask_hide_prompt -->
<!-- signatures: ask_hide_prompt -->
### Variable: ask_hide_prompt

Standardwert: `false`


Wenn auf `true` gesetzt, geben die Funktionen `askequal`,
`askinteger` und `asksign` keine Eingabeaufforderung aus, wenn
Eingaben vom Benutzer angefordert werden. Dies ist nutzlich, um die Ausgabe
in nicht-interaktiven Sitzungen oder automatisierten Tests zu reduzieren.

<!-- category: Other -->
<!-- keywords: askinteger -->
<!-- signatures: askinteger(expr, integer), askinteger(expr), askinteger(expr, even), askinteger(expr, odd) -->
### Function: askinteger (expr, integer)

Das Kommando `askinteger(expr, integer)` versucht anhand der Aussagen
und Fakten der aktiven Kontexte zu entscheiden, ob *expr* eine ganze Zahl
reprasentiert.  Kann `askinteger` die Frage nicht entscheiden, fragt 
Maxima den Nutzer.  Die Antwort wird dem aktuellen Kontext hinzugefugt.  
`askinteger(expr)` ist aquivalent zu 
`askinteger(expr, integer)`.


`askinteger(expr, even)` und `askinteger(expr, odd)`
versuchen zu entscheiden, ob *expr* eine gerade oder ungerade ganze Zahl
reprasentiert.  Kann Maxima dies nicht entscheiden, wird der Nutzer gefragt.
Die Antwort wird dem aktuellen Kontext hinzugefugt.


Beispiele:



```maxima
(%i1) askinteger(n,integer);
Is n an integer?
yes;
(%o1)                          yes
(%i2) askinteger(e,even);
Is e an even number?
yes;
(%o2)                          yes
(%i3) facts();
(%o3)           [kind(n, integer), kind(e, even)]
(%i4) declare(f,integervalued);
(%o4)                         done
(%i5) askinteger(f(x));
(%o5)                          yes
```

<!-- category: Other -->
<!-- keywords: asksign -->
<!-- signatures: asksign(expr) -->
### Function: asksign (expr)

Die Funktion `asksign` versucht zu entscheiden, ob der Ausdruck *expr*
einen positiven, negativen oder den Wert Null reprasentiert.  Kann Maxima dies
nicht feststellen, wird der Nutzer nach weiteren Informationen gefragt, um die 
Frage zu entscheiden.  Die Antworten des Nutzers werden fur die laufende 
Auswertung dem aktuellen Kontext hinzugefugt.  Der Ruckgabewert der 
Funktion `asksign` ist `pos`, `neg` oder `zero` fur einen
positiven, negativen oder den Wert Null.

<!-- category: Other -->
<!-- keywords: assume -->
<!-- signatures: assume(pred_1, ..., pred_n) -->
### Function: assume (pred_1, ..., pred_n)

Fugt die Aussagen *pred_1*, ..., *pred_n* dem aktuellen Kontext 
hinzu.  Eine inkonsistente oder redundante Aussage wird dem Kontext nicht
hinzugefugt.  `assume` gibt eine Liste mit den Aussagen zuruck, die dem
Kontext hinzugefugt wurden, oder die Symbole `redunant` und 
`inconsistent`.


Die Aussagen *pred_1*, ..., *pred_n* konnen nur Ausdrucke mit 
den relationalen Operatoren `"<"`, `"<="`, `equal`, 
`notequal`, `">="` und `">"` sein.  Aussagen konnen nicht die
Operatoren `"="` fur Gleichungen oder `"#"` fur Ungleichungen 
enthalten.  Auch konnen keine Aussagefunktionen wie `integerp` verwendet
werden.


Zusammengesetzte Aussagen mit dem Operator `and` der Form 
`pred_1 and ... and pred_n` sind moglich, nicht dagegen 
Aussagen mit dem Operator `or` der Form `pred_1 or ... or pred_n`.  Ein Ausdruck mit dem Operator `not` der Form 
`not(pred_k)` ist dann moglich, wenn *pred_k* eine 
relationale Aussage ist.  Aussagen der Form `not (pred_1 and pred_2)` und `not (pred_1 or pred_2)` sind dagegen nicht
moglich.


Der Folgerungsmechanismus von Maxima ist nicht sehr stark.  Viele 
Schlußfolgerungen konnen von Maxima nicht abgeleitet werden.  Dies ist 
eine bekannte Schwache von Maxima.


`assume` behandelt keine Aussagen mit komplexen Zahlen.  Enthalt eine
Aussage eine komplexe Zahl, gibt `assume` den Wert `inconsistent`
oder `redunant` zuruck.


`assume` wertet die Argumente aus.


Siehe auch `is`, `facts`, `forget`,
`context` und `declare`.


Beispiele:



```maxima
(%i1) assume (xx > 0, yy < -1, zz >= 0);
(%o1)              [xx > 0, yy < - 1, zz >= 0]
(%i2) assume (aa < bb and bb < cc);
(%o2)                  [bb > aa, cc > bb]
(%i3) facts ();
(%o3)     [xx > 0, - 1 > yy, zz >= 0, bb > aa, cc > bb]
(%i4) is (xx > yy);
(%o4)                         true
(%i5) is (yy < -yy);
(%o5)                         true
(%i6) is (sinh (bb - aa) > 0);
(%o6)                         true
(%i7) forget (bb > aa);
(%o7)                       [bb > aa]
(%i8) prederror : false;
(%o8)                         false
(%i9) is (sinh (bb - aa) > 0);
(%o9)                        unknown
(%i10) is (bb^2 < cc^2);
(%o10)                       unknown
```

See also: `is`, `facts`, `forget`, `context`, `declare`.

<!-- category: Other -->
<!-- keywords: assume_pos -->
<!-- signatures: assume_pos -->
### Variable: assume_pos

Standardwert: `false`


Die Optionsvariable `assume_pos` kontrolliert das Ergebnis der Funktionen
`sign` und `asksign`, fur den Fall, dass Maxima das Vorzeichen
einer Variablen oder indizierten Variablen nicht aus den aktiven Kontexten 
ermitteln kann.  Hat `assume_pos` den Wert `true`, dann wird fur 
Variable oder indizierte Variable, immer das Ergebnis `pos` ermittelt, wenn
die Optionsvariable `assume_pos_pred` den Standardwert `false` hat und
das Vorzeichen nicht aus den aktiven Kontexten ermittelt werden kann.


Die Optionsvariable `assume_pos_pred` hat den Standardwert `false`.
In diesem Fall werden von Maxima Variablen und indizierte Variablen als positiv
angenommen, wenn `assume_pos` den Wert `true` hat.  Der 
Optionsvariablen `assume_pos_pred` kann eine Aussagefunktion mit einem
Argument zugewiesen werden.  Hat die Aussagefunktion fur ein Argument 
*expr* das Ergebnis `true`, wird das Argument als positiv 
angenommen, wenn die Optionsvariable `assume_pos` den Wert `true` hat
und Maxima das Vorzeichen nicht aus den aktiven Kontexten ermitteln kann.


Die Funktionen `sign` und `asksign` versuchen das Vorzeichen eines
Ausdrucks anhand der Vorzeichen der Argumente zu ermitteln.  Sind zum Beispiel
`a` und `b` beide positiv, dann wird fur den Ausdruck `a+b` ein
positives Vorzeichen ermittelt.  Auch wenn die Vorzeichen der Variablen `a`
und `b` nicht bekannt sind, hat daher `asksign(a+b)` das Ergebnis
`pos`, wenn `assume_pos` den Wert `true` hat, da in diesem Fall
die Variablen als positiv angenommen werden.


Es gibt jedoch keine Moglichkeit, alle Ausdrucke grundsatzlich als positiv
zu erklaren.  Selbst wenn der Optionsvariablen `assume_pos_pred` eine 
Aussagefunktion zugewiesen wird, die alle Ausdrucke als positiv erklart,
werden Differenzen `a-b` oder das Vorzeichen der Logarithmusfunktion 
`log(a)` nicht als positiv ermittelt.  Die Fragen der Funktion 
`asksign` an den Nutzer konnen daher nie vollstandig mit dem 
Mechanismus der Optionsvariablen `assume_pos` unterdruckt werden.


Siehe fur weitere Beispiele die Optionsvariable `assume_pos_pred`.


Beispiele:


Das Vorzeichen der Variablen `x` ist nicht bekannt.  Erhalt die
Optionsvariable `assume_pos` den Wert `true`, wird fur die Variable
`x` und die indizierte Variable `x[1]` ein positives Vorzeichen
ermittelt.



```maxima
(%i1) sign(x);
(%o1)                          pnz
(%i2) assume_pos:true;
(%o2)                         true
(%i3) sign(x);
(%o3)                          pos
(%i4) sign(x[1]);
(%o4)                          pos
```


Die Vorzeichen der Variablen `a` und `b` sind nicht bekannt.  Maxima
ermittelt ein positives Vorzeichen fur die Summe der Variablen.  Das
Vorzeichen der Differenz ist dagegen weiterhin nicht bekannt.



```maxima
(%i5) sign(a+b);
(%o5)                          pos
(%i6) sign(a-b);
(%o6)                          pnz
```

See also: `sign`, `asksign`, `assume_pos_pred`.

<!-- category: Other -->
<!-- keywords: assume_pos_pred -->
<!-- signatures: assume_pos_pred -->
### Variable: assume_pos_pred

Standardwert: `false`


Der Optionsvariablen `assume_pos_pred` kann eine Aussagefunktion wie zum
Beispiel `symbolp` oder ein Lambda-Ausdruck mit einem Argument `x`
zugewiesen werden.  Hat die Optionsvariable `assume_pos` den Wert
`true`, werden Variablen, indizierte Variablen oder die Werte von 
Funktionen dann als positiv angenommen, wenn die Aussagefunktion das Ergebnis 
`true` hat.


Die Aussagefunktion wird intern von den Funktionen `sign` und 
`asksign` aufgerufen, wenn die Optionsvariable `assume_pos` den Wert
`true` hat und das Vorzeichen einer Variablen, indizierten Variablen oder
fur den Wert einer Funktion nicht ermittelt werden konnte.  Gibt die
Aussagefunktion das Ergebnis `true` zuruck, wird das Argument als
positiv angenommen.


Hat die Optionsvariable `assume_pos_pred` den Standardwert `false`
werden Variablen und indizierte Variablen von Maxima als positiv angenommen,
wenn die Optionsvariable `assume_pos` den Wert `true` hat.  Das 
entspricht einer Aussagefunktion, die als `lambda([x], symbolp(x) or subvarp(x))` definiert wird.


Siehe auch `assume` und `assume_pos`.


Beispiele:


Der Optionsvariablen `assume_pos_pred` wird der Name der Aussagefunktion
`symbolp` zugewiesen.  Indizierte Variablen werden nun nicht mehr als 
positiv angenommen, wie es fur den Standartwert `false` gilt.



```maxima
(%i1) assume_pos: true$
(%i2) assume_pos_pred: symbolp$
(%i3) sign (a);
(%o3)                          pos
(%i4) sign (a[1]);
(%o4)                          pnz
```


Der Optionsvariablen `assume_pos_pred` wird ein Lambda-Ausdruck zugewiesen,
der fur alle Argumente das Ergebnis `true` hat.  Die Funktion `sign`
ermittelt nun fur Variablen, indizierte Variablen und den Werten von 
Funktionen ein positives Vorzeichen.  Dies trifft jedoch nicht fur die 
Logarithmusfunktion oder eine Differenz zu.



```maxima
(%i1) assume_pos: true$
(%i2) assume_pos_pred: lambda([x], true);
(%o2)                   lambda([x], true)
(%i3) sign(a);
(%o3)                          pos
(%i4) sign(a[1]);
(%o4)                          pos
(%i5) sign(foo(x));
(%o5)                          pos
(%i6) sign(foo(x)+foo(y));
(%o6)                          pos
(%i7) sign(log(x));
(%o7)                          pnz
(%i8) sign(x-y);
(%o8)                          pnz
```

See also: `symbolp`, `assume_pos`, `sign`, `asksign`, `assume`.

<!-- category: Other -->
<!-- keywords: assumescalar -->
<!-- signatures: assumescalar -->
### Variable: assumescalar

Standardwert: `true`


Die Optionsvariable `assumescalar` kontrolliert, wie ein Ausdruck von den
arithmetischen Operatoren `"+"`, `"*"`, `"^"`, `"."` und
`"^^"` behandelt wird, wenn Maxima nicht ermitteln kann, ob der Ausdruck
ein Skalar oder Nicht-Skalar ist.  `assumescalar` hat drei mogliche
Werte:



**false** — Unbekannte Ausdrucke werden als ein Nicht-Skalar behandelt.
**true** — Unbekannte Ausdrucke werden als ein Skalar fur die kommutativen 
arithmetischen Operatoren `"+"`, `"*"` und `"^"` behandelt.
**all** — Unbekannte Ausdrucke werden fur alle arithmetischen Operatoren als ein
Skalar behandelt.


Es ist besser Variablen als ein Skalar oder Nicht-Skalar mit der Funktion
`declare` zu deklarieren, anstatt die Vereinfachung mit der 
Optionsvariablen `assumescalar` zu kontrollieren.  Siehe auch die 
Eigenschaften `scalar` und `nonscalar` sowie die Funktionen 
`scalarp` und `nonscalarp`.


Beispiele:


Maxima kann nicht ermitteln, ob das Symbol `x` ein Skalar oder ein
Nicht-Skalar ist.



```maxima
(%i1) scalarp(x);
(%o1)                         false
(%i2) nonscalarp(x);
(%o2)                         false
```


Hat `assumescalar` den Wert `true`, behandelt Maxima das Symbol 
`x` als einen Skalar fur die kommutative Multiplikation.



```maxima
(%i3) x * [a,b,c], assumescalar:false;
(%o3)                      x [a, b, c]
(%i4) x * [a,b,c], assumescalar:true;
(%o4)                    [a x, b x, c x]
```


Fur die nicht kommutative Multiplikation behandelt Maxima das Symbol `x`
dann als einen Skalar, wenn `assumescalar` den Wert `all` hat.



```maxima
(%i5) x . [a,b,c], assumescalar:false;
(%o5)                     x . [a, b, c]
(%i6) x . [a,b,c], assumescalar:true;
(%o6)                     x . [a, b, c]
(%i7) x . [a,b,c], assumescalar:all;
(%o7)                 [x . a, x . b, x . c]
```

See also: `declare`, `scalar`, `nonscalar`, `scalarp`, `nonscalarp`.

<!-- category: Other -->
<!-- keywords: charfun -->
<!-- signatures: charfun(p) -->
### Function: charfun (p)

Gibt den Wert 0 zuruck, wenn die Aussage *p* zu `false` ausgewertet
werden kann und den Wert 1, wenn die Auswertung `true` liefert.  Kann
die Aussage weder zu `false` oder `true` ausgewertet werden, wird eine
Substantiv-Form zuruck gegeben.


Beispiele:



```maxima
(%i1) charfun (x < 1);
(%o1)                    charfun(x < 1)
(%i2) subst (x = -1, %);
(%o2)                           1
(%i3) e : charfun ('"and" (-1 < x, x < 1))$
(%i4) [subst (x = -1, e), subst (x = 0, e), subst (x = 1, e)];
(%o4)                       [0, 1, 0]
```

<!-- category: Other -->
<!-- keywords: compare -->
<!-- signatures: compare(x, y) -->
### Function: compare (x, y)

Liefert den Vergleichsoperator *op* (`<`, `<=`, `>`, 
`>=`, `=` oder `#`), so dass der Ausdruck `is(x op y)` zu `true` ausgewertet werden kann.  Ist eines der
Argumente eine komplexe Zahl, dann wird `notcomparable` zuruckgegeben.
Kann Maxima keinen Vergleichsoperator bestimmen, wird `unknown`
zuruckgegeben.


Beispiele:



```maxima
(%i1) compare (1, 2);
(%o1)                           <
(%i2) compare (1, x);
(%o2)                        unknown
(%i3) compare (%i, %i);
(%o3)                           =
(%i4) compare (%i, %i + 1);
(%o4)                     notcomparable
(%i5) compare (1/x, 0);
(%o5)                           #
(%i6) compare (x, abs(x));
(%o6)                          <=
```


Die Funktion `compare` versucht nicht festzustellen, ob der Wertebereich
einer Funktion reelle Zahlen enthalt.  Obwohl der Wertebereich von 
`acos(x^2+1)` bis auf Null keine reellen Zahlen enthalt, gibt 
`compare` das folgende Ergebnis zuruck:



```maxima
(%i1) compare (acos (x^2 + 1), acos (x^2 + 1) + 1);
(%o1)                           <
```

<!-- category: Other -->
<!-- keywords: context -->
<!-- signatures: context -->
### Variable: context

Standardwert: `initial`


Die Optionsvariable `context` enthalt den Namen des aktuellen Kontextes.
Das ist der Kontext, der die Aussagen der Funktion `assume` oder die mit 
der Funktion `declare` definierten Eigenschaften aufnimmt und aus dem die 
Aussagen mit der Funktion `forget` oder die Eigenschaften mit der Funktion
`remove` geloscht werden.


Wird der Optionsvariablen `context` der Name eines existierenden Kontextes
zugewiesen, wird dieser zum aktuellen Kontext.  Existiert der Kontext noch 
nicht, wird er durch Aufruf der Funktion `newcontext` erzeugt.


Siehe auch `contexts` fur eine allgemeinere Beschreibung von Kontexten.


Beispiele:


Der Standardkontext ist `initial`.  Es wird ein neuer Kontext
`mycontext` generiert, der die Aussagen und Eigenschaften aufnimmt.



```maxima
(%i1) context;
(%o1)                        initial
(%i2) context:mycontext;
(%o2)                       mycontext
(%i3) contexts;
(%o3)             [mycontext, initial, global]
(%i4) assume(a>0);
(%o4)                        [a > 0]
(%i5) declare(b,integer);
(%o5)                         done
(%i6) facts(mycontext);
(%o6)               [a > 0, kind(b, integer)]
```

See also: `assume`, `declare`, `forget`, `remove`, `newcontext`, `contexts`.

<!-- category: Other -->
<!-- keywords: contexts -->
<!-- signatures: contexts -->
### Variable: contexts

Standardwert: `[initial, global]`


Die Systemvariable `contexts` enthalt eine Liste der Kontexte, die 
Maxima bekannt sind.  Die Liste enthalt auch die nicht aktiven Kontexte.


Die Kontexte `global` und `initial` sind immer vorhanden.  Diese 
werden von Maxima initialisiert und konnen nicht entfernt werden.  Der Kontext
`global` enthalt Aussagen und Fakten fur Systemvariablen und
Systemfunktionen.  Mit den Funktionen `newcontext` oder
`supcontext` kann der Nutzer weitere Kontexte anlegen.


Die Kontexte haben eine Hierarchie.  Die Wurzel ist immer der Kontext
`global`, der damit ein Unterkontext aller anderen Kontexte und immer aktiv
ist.  Der Kontext `initial` ist anfangs leer und nimmt, sofern kein 
weiterer Kontext angelegt wurde, die Aussagen und Fakten des Nutzers auf, die 
mit den Funktionen `assume` und `declare` definiert werden.  Mit der
Funktion `facts` konnen die Aussagen und Fakten von Kontexten angezeigt
werden.


Die Verwaltung verschiedener Kontexte ermoglicht es, Aussagen und Fakten in
einem Kontext zusammenzustellen.  Durch das Aktivieren mit der Funktion
`activate` oder Deaktivieren mit der Funktion `deactivate` konnen
diese Aussagen und Fakten fur Maxima verfugbar gemacht oder wieder
ausgeschaltet werden.


Die Aussagen und Fakten in einem Kontext bleiben so lange verfugbar, bis sie 
mit den Funktionen `forget` oder `remove` geloscht werden.
Weiterhin kann der gesamte Kontext mit der Funktion `killcontext` entfernt
werden.


Der Kontext `global` kann nicht verandert werden: Er kann nicht zum
aktuellen Kontext gemacht werden, und die Fakten in ihm knnen nicht entfernt
werden.


Beispiel:


Das folgende Beispiel zeigt wie ein Kontext `mycontext` angelegt wird.  Der
Kontext enthalt die Aussage `[a>0]`.  Der Kontext kann mit der Funktion
`activate` aktiviert werden, um die Aussage verfugbar zu machen.



```maxima
(%i1) newcontext(mycontext);
(%o1)                       mycontext
(%i2) context;
(%o2)                       mycontext
(%i3) assume(a>0);
(%o3)                        [a > 0]
(%i4) context:initial;
(%o4)                        initial
(%i5) is(a>0);
(%o5)                        unknown
(%i6) activate(mycontext);
(%o6)                         done
(%i7) is(a>0);
(%o7)                         true
```

See also: `newcontext`, `supcontext`, `assume`, `declare`, `facts`, `activate`, `deactivate`, `forget`, `remove`, `killcontext`.

<!-- category: Other -->
<!-- keywords: deactivate -->
<!-- signatures: deactivate(context_1, ..., context_n) -->
### Function: deactivate (context_1, ..., context_n)

Die Kontexte *context_1*, ..., *context_n* werden deaktiviert.  Die
Aussagen und Fakten dieser Kontexte stehen fur die Auswertung von Aussagen 
nicht mehr zur Verfugung.  Die Kontexte werden nicht geloscht und konnen 
mit der Funktion `activate` wieder aktiviert werden.


Die deaktivierten Kontexte werden aus der Liste `activecontexts` entfernt.

See also: `activate`, `activecontexts`.

<!-- category: Other -->
<!-- keywords: equal -->
<!-- signatures: equal(a, b) -->
### Function: equal (a, b)

Reprasentiert die Aquivalenz, das heißt den gleichen Wert.


`equal` wird nicht ausgewertet oder vereinfacht.  Die Funktion
`is` versucht einen Ausdruck mit `equal` zu einem booleschen Wert
auszuwerten.  `is(equal(a, b))` gibt `true` oder
`false` zuruck, wenn und nur wenn *a* und *b* gleich oder
ungleich sind fur alle Werte ihrer Variablen, was mit `ratsimp(a - b)` bestimmt wird.  Gibt `ratsimp` das Ergebnis 0 zuruck, werden
die beiden Ausdrucke als aquivalent betracht.  Zwei Ausdrucke konnen
aquivalent sein, obwohl sie nicht syntaktisch gleich (im allgemeinen
identisch) sind.


Kann `is` einen Ausdruck mit `equal` nicht zu `true` oder 
`false` auswerten, hangt das Ergebnis vom Wert des globalen Flags 
`prederror` ab.  Hat `prederror` den Wert `true`, gibt `is`
eine Fehlermeldung zuruck.  Ansonsten wird `unknown` zuruckgegeben.


Es gibt weitere Operatoren, die einen Ausdruck mit `equal` zu `true`
oder `false` auswerten konnen.  Dazu gehoren `if`,
`and`, `or` und `not`.


Die Umkehrung von `equal` ist `notequal`.


Beispiele:


`equal` wird von allein weder ausgewertet noch vereinfacht:



```maxima
(%i1) equal (x^2 - 1, (x + 1) * (x - 1));
                        2
(%o1)            equal(x  - 1, (x - 1) (x + 1))
(%i2) equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) equal (x, y);
(%o3)                      equal(x, y)
```


Die Funktion `is` versucht, `equal` zu einem booleschen Wert
auszuwerten.  Der Ausdruck `is(equal(a, b))` gibt den Wert
`true` zuruck, when `ratsimp(a - b)` den Wert 0 hat.
Zwei Ausdrucke konnen aquivalent sein, obwohl sie nicht syntaktisch
gleich sind.



```maxima
(%i1) ratsimp (x^2 - 1 - (x + 1) * (x - 1));
(%o1)                           0
(%i2) is (equal (x^2 - 1, (x + 1) * (x - 1)));
(%o2)                         true
(%i3) is (x^2 - 1 = (x + 1) * (x - 1));
(%o3)                         false
(%i4) ratsimp (x - (x + 1));
(%o4)                          - 1
(%i5) is (equal (x, x + 1));
(%o5)                         false
(%i6) is (x = x + 1);
(%o6)                         false
(%i7) ratsimp (x - y);
(%o7)                         x - y
(%i8) is (equal (x, y));
(%o8)                        unknown
(%i9) is (x = y);
(%o9)                         false
```


Kann `is` einen Ausdruck mit `equal` nicht zu `true` oder
`false` vereinfachen, hangt das Ergebnis vom Wert des globalen Flags
`prederror` ab.



```maxima
(%i1) [aa : x^2 + 2*x + 1, bb : x^2 - 2*x - 1];
                    2             2
(%o1)             [x  + 2 x + 1, x  - 2 x - 1]
(%i2) ratsimp (aa - bb);
(%o2)                        4 x + 2
(%i3) prederror : true;
(%o3)                         true
(%i4) is (equal (aa, bb));
Maxima was unable to evaluate the predicate:
       2             2
equal(x  + 2 x + 1, x  - 2 x - 1)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) prederror : false;
(%o5)                         false
(%i6) is (equal (aa, bb));
(%o6)                        unknown
```


Einige weitere Operatoren werten `equal` und `notequal` zu einem
booleschen Wert aus.



```maxima
(%i1) if equal (y, y - 1) then FOO else BAR;
(%o1)                          BAR
(%i2) eq_1 : equal (x, x + 1);
(%o2)                    equal(x, x + 1)
(%i3) eq_2 : equal (y^2 + 2*y + 1, (y + 1)^2);
                         2                   2
(%o3)             equal(y  + 2 y + 1, (y + 1) )
(%i4) [eq_1 and eq_2, eq_1 or eq_2, not eq_1];
(%o4)                  [false, true, true]
```


Da `not expr` den Ausdruck *expr* auswertet, ist 
`not equal(a, b)` aquivalent zu 
`is(notequal(a, b))`



```maxima
(%i1) [notequal (2*z, 2*z - 1), not equal (2*z, 2*z - 1)];
(%o1)            [notequal(2 z, 2 z - 1), true]
(%i2) is (notequal (2*z, 2*z - 1));
(%o2)                         true
```

See also: `is`, `ratsimp`, `prederror`, `if`, `and`, `or`, `not`, `notequal`.

<!-- category: Other -->
<!-- keywords: facts -->
<!-- signatures: facts(item), facts() -->
### Function: facts (item)

Ist *item* der Name eines Kontextes, gibt `facts(item)` eine
Liste der Aussagen und Fakten des Kontextes `item` zuruck.


Ist *item* nicht der Name eines Kontextes, gibt `facts(item)` 
eine Liste mit den Aussagen und Fakten zuruck, die zu *item* im aktuellen
Kontext bekannt sind.  Aussagen und Fakten die zu einem anderen aktiven Kontext
gehoren einschließlich der Unterkontexte, sind nicht in der Liste 
enthalten.


`facts()` gibt eine Liste der Fakten des aktuellen Kontextes zuruck.


Beispiel:



```maxima
(%i1) context:mycontext;
(%o1)                       mycontext
(%i2) assume(a>0, a+b>0, x<0);
(%o2)               [a > 0, b + a > 0, x < 0]
(%i3) facts();
(%o3)               [a > 0, b + a > 0, 0 > x]
(%i4) facts(a);
(%o4)                  [a > 0, b + a > 0]
(%i5) facts(x);
(%o5)                        [0 > x]
(%i6) context:initial;
(%o6)                        initial
(%i7) activate(mycontext);
(%o7)                         done
(%i8) facts();
(%o8)                          []
(%i9) facts(mycontext);
(%o9)               [a > 0, b + a > 0, 0 > x]
```

<!-- category: Other -->
<!-- keywords: forget -->
<!-- signatures: forget(pred_1, ..., pred_n), forget(L) -->
### Function: forget (pred_1, ..., pred_n)

Entfernt Aussagen, die mit `assume` einem Kontext hinzugefugt wurden.
Die Aussagen konnen Ausdrucke sein, die aquivalent aber nicht unbedingt
identisch zu vorherigen Fakten sind.


`forget` berucksichtigt nur die Fakten, die im aktuellen Kontext aktiv
sind: die des aktuellen Kontextes selbst, seiner Unterkontexte und der mit
`activate` aktivierten Kontexte. Fakten in anderen Kontexten werden nicht
entfernt, und eine Aussage, die nur dort vorkommt, gilt als nicht in der
Datenbank gefunden. Ist dieselbe Aussage in mehreren aktiven Kontexten
gespeichert, wird zuerst die des aktuellen Kontextes entfernt.


Aussagen im Kontext `global` sind fest in Maxima eingebaut und konnen
mit `forget` nicht entfernt werden.


`forget` gibt die entfernten Fakten zuruck, `redundant` fur
Fakten, die nicht in der Datenbank gefunden wurden, und `not_done` fur
eingebaute Fakten aus dem Kontext `global`. Dies bezieht sich nur auf
gespeicherte Fakten, nicht darauf, was von ihnen abgeleitet werden kann:
Nach `assume(x > 1)` wird durch `forget(x > 0)` nichts entfernt, und
`is(x > 0)` ist immer noch `true`.


`forget(L)` entfernt alle Aussagen, die in der Liste *L*
enthalten sind.

See also: `activate`.

<!-- category: Other -->
<!-- keywords: is -->
<!-- signatures: is(expr) -->
### Function: is (expr)

Versucht festzustellen, ob die Aussage *expr* mit Hilfe der Aussagen und 
Fakten der aktiven Kontexte entschieden werden kann.


Kann die Aussage *expr* zu `true` oder `false` entschieden werden,
wird das entsprechende Ergebnis zuruckgegeben.  Andernfalls wird der 
Ruckgabewert durch den Schalter `prederror` bestimmt.  Hat 
`prederror` den Wert `true`, wird eine Fehlermeldung ausgegeben.  
Ansonsten wird `unknown` zuruckgegeben.


Siehe auch `assume`, `facts` und `maybe`.


Beispiele:


`is` wertet Aussagen aus.



```maxima
(%i1) %pi > %e;
(%o1)                       %pi > %e
(%i2) is (%pi > %e);
(%o2)                         true
```


`is` versucht Aussagen anhand der Aussagen und Fakten der aktiven
Kontexte zu entscheiden.



```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) assume (b > c);
(%o2)                        [b > c]
(%i3) is (a < b);
(%o3)                         false
(%i4) is (a > c);
(%o4)                         true
(%i5) is (equal (a, c));
(%o5)                         false
```


Wenn `is` eine Aussage anhand der Aussagen und Fakten der aktiven Kontexte 
nicht entscheiden kann, wird der Ruckgabewert vom Wert des Schalters 
`prederror` bestimmt.



```maxima
(%i1) assume (a > b);
(%o1)                        [a > b]
(%i2) prederror: true$
(%i3) is (a > 0);
Maxima was unable to evaluate the predicate:
a > 0
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) prederror: false$
(%i5) is (a > 0);
(%o5)                        unknown
```

See also: `prederror`, `assume`, `facts`, `maybe`.

<!-- category: Other -->
<!-- keywords: killcontext -->
<!-- signatures: killcontext(context_1, ..., context_n) -->
### Function: killcontext (context_1, ..., context_n)

Das Kommando `killcontext(context)` loscht den Kontext 
*context*.


Ist einer der Kontexte der aktuelle Kontext, wird der erste vorhandene 
Unterkontext zum aktuellen Kontext.  Ist der erste verfugbare Kontext der 
Kontext `global`, dann wird der Kontext `initial` zum aktuellen 
Kontext.  Wird der Kontext `initial` geloscht, dann wird eine neuer 
leerer Kontext `initial` erzeugt.


`killcontext` loscht einen Kontext nicht, wenn dieser ein Unterkontext
des aktuellen Kontextes oder eines mit der Funktion `activate` aktivierten
Kontextes ist, da jener Kontext von ihm abhangt.  Ein Kontext, der selbst
aktiviert wurde, wird vor dem Loschen deaktiviert.


`killcontext` wertet die Argumente aus.


`killcontext` gibt `not_done` zuruck, wenn einer der angegebenen
Kontexte nicht geloscht werden konnte, da er nicht existiert, ein Unterkontext
des aktuellen oder eines aktivierten Kontextes ist oder der Kontext
`global` ist. Anderenfalls wird `done` zuruckgegeben.

<!-- category: Other -->
<!-- keywords: maybe -->
<!-- signatures: maybe(expr) -->
### Function: maybe (expr)

Versucht festzustellen, ob die Aussage *expr* anhand der Aussagen und
Fakten der aktive Kontexte entschieden werden kann.


Kann die Aussage als `true` oder `false` entschieden werden, gibt 
`maybe` entsprechend `true` oder `false` zuruck.  Andernfalls
gibt `maybe` den Wert `unknown` zuruck.


`maybe` entspricht der Funktion `is` mit `prederror: false`.
Dabei wird `maybe` ausgefuhrt, ohne dass `prederror` einen Wert 
erhalt.


Siehe auch `assume`, `facts` und `is`.


Beispiele:



```maxima
(%i1) maybe (x > 0);
(%o1)                        unknown
(%i2) assume (x > 1);
(%o2)                        [x > 1]
(%i3) maybe (x > 0);
(%o3)                         true
```

See also: `assume`, `facts`, `is`.

<!-- category: Other -->
<!-- keywords: newcontext -->
<!-- signatures: newcontext(name) -->
### Function: newcontext (name)

`newcontext(name)` erzeugt einen neuen, leeren Kontext mit dem 
Namen *name*. Der neue Kontext hat den Kontext `global` als Subkontext
und wird zum aktuellen Kontext.


`newcontext` wertet seine Argumente aus.  `newcontext` gibt 
`name` zuruck.

<!-- category: Other -->
<!-- keywords: notequal -->
<!-- signatures: notequal(a, b) -->
### Function: notequal (a, b)

Reprasentiert die Verneinung von `equal(a, b)`.


Beispiele:



```maxima
(%i1) equal (a, b);
(%o1)                      equal(a, b)
(%i2) maybe (equal (a, b));
(%o2)                        unknown
(%i3) notequal (a, b);
(%o3)                    notequal(a, b)
(%i4) not equal (a, b);
(%o4)                    notequal(a, b)
(%i5) maybe (notequal (a, b));
(%o5)                        unknown
(%i6) assume (a > b);
(%o6)                        [a > b]
(%i7) equal (a, b);
(%o7)                      equal(a, b)
(%i8) maybe (equal (a, b));
(%o8)                         false
(%i9) notequal (a, b);
(%o9)                    notequal(a, b)
(%i10) maybe (notequal (a, b));
(%o10)                        true
```

<!-- category: Other -->
<!-- keywords: prederror -->
<!-- signatures: prederror -->
### Variable: prederror

Standardwert: `false`


Hat `prederror` den Wert `true`, wird eine Fehlermeldung ausgegeben,
wenn eine Aussage mit einer `if`-Anweisung oder der Funktion `is` 
nicht zu `true` oder `false` ausgewertet werden kann.


Hat `prederror` den Wert `false`, wird fur diese Falle 
`unknown` zuruckgegeben.


Siehe auch `is` und `maybe`.

See also: `is`, `maybe`.

<!-- category: Other -->
<!-- keywords: sign -->
<!-- signatures: sign(expr) -->
### Function: sign (expr)

Versucht das Vorzeichen des Ausdrucks *expr* auf Grundlage der Fakten der
aktuellen Datenbank zu finden.  `sign` gibt eine der folgende Antworten 
zuruck: `pos` (positiv), `neg` (negative), `zero` (null),
`pz` (positive oder null), `nz` (negative oder null), `pn`
(positiv oder negative) oder `pnz` (positiv, negative oder null, fur den
Fall das Vorzeichen nicht bekannt ist).

<!-- category: Other -->
<!-- keywords: supcontext -->
<!-- signatures: supcontext(name, context), supcontext(name) -->
### Function: supcontext (name, context)

Erzeugt einen neuen Kontext, mit dem Namen `name`, der den Kontext 
`context` als einen Unterkontext enthalt.  Der Kontext *context* muss
existieren.


Wird *context* nicht angegeben, wird der aktuelle Kontext angenommen.

<!-- category: Other -->
<!-- keywords: unknown -->
<!-- signatures: unknown(expr) -->
### Function: unknown (expr)

Gibt den Wert `true` zuruck, wenn der Ausdruck *expr* einen Operator
oder eine Funktion enthalt, die nicht von Maximas Vereinfacher erkannt wird.

<!-- category: Other -->
<!-- keywords: zeroequiv -->
<!-- signatures: zeroequiv(expr, v) -->
### Function: zeroequiv (expr, v)

Testet, ob ein Ausdruck *expr* mit der Variablen *v* aquivalent zu 
Null ist.  Die Funktion gibt `true`, `false` oder `dontknow` 
zuruck.


`zeroequiv` hat Einschrankungen:



1. Funktionen im Ausdruck *expr* mussen von Maxima differenzierbar und 
auswertbar sein.
2. Hat der Ausdruck Pole auf der reellen Achse, konnen Fehler auftreten.
3. Enthalt der Ausdruck Funktionen, die nicht Losung einer 
Differentialgleichung erster Ordnung sind (zum Beispiel Bessel Funktionen), 
konnen die Ergebnisse fehlerhaft sein.
4. Der Algorithmus wertet die Funktion an zufallig Punkten fur ausgewahlte
Teilausdrucke aus.  Dies ist ein riskantes Verfahren und kann zu Fehlern 
fuhren.


`zeroequiv(sin(2*x) - 2*sin(x)*cos(x), x)` hat zum Beispiel das Ergebnis 
`true` und  `zeroequiv (%e^x + x, x)` hat das Ergebnis `false`.
Andererseits hat `zeroequiv (log(a*b) - log(a) - log(b), a)` das Ergebnis
`dontknow`, wegen dem zusatzlichem Parameter `b`.

