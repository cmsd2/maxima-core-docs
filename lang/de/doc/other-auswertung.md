## Auswertung

<!-- category: Other -->
<!-- keywords: ' -->
<!-- signatures: ' -->
### Function: '

Der Quote-Operator `'` unterdruckt die Auswertung eines Symbols oder
Ausdrucks.  Auf eine Funktion angewendet, unterdruckt der Quote-Operator die
Auswertung der Funktion.  Die Auswertung der Argumente der Funktion wird nicht
unterdruckt.  Das Ergebnis ist die Substantivform der Funktion.


Wird der Quote-Operator auf einen eingeklammerten Ausdruck angewendet, wird die
Auswertung aller Symbole und Funktionen innerhalb der Klammern unterdruckt.
`'(f(x))` bedeutet, dass der Ausdruck `f(x)` nicht ausgewertet werden 
soll.  `'f(x)` bedeutet, dass die Substantivform von `f` auf das 
ausgewertete Argument *x* angewendet wird.


Der Quote-Operator unterdruckt die Auswertung, aber nicht die Vereinfachung
von Ausdrucken.


Substantivformen werden mit einem Hochkomma angezeigt, wenn die Optionsvariable 
`noundisp` den Wert `true` hat.


Siehe auch den Quote-Quote-Operator `''` und den
Auswertungsschalter `nouns`.


Beispiele:


Auf ein Symbol angewendet, unterdruckt der Quote-Operator die Auswertung des
Symbols.



```maxima
(%i1) aa: 1024;
(%o1)                         1024

(%i2) aa^2;
(%o2)                        1048576

(%i3) 'aa^2;
                                 2
(%o3)                          aa
(%i4) ''%;
(%o4)                        1048576
```


Auf eine Funktion angewendet, unterdruckt der Quote-Operator die Auswertung
der Funktion.  Das Ergebnis ist die Substantivform der Funktion.



```maxima
(%i1) x0: 5;
(%o1)                           5
(%i2) x1: 7;
(%o2)                           7

(%i3) integrate (x^2, x, x0, x1);
                               218
(%o3)                          ---
                                3

(%i4) 'integrate (x^2, x, x0, x1);

                             7
                            /
                            [   2
(%o4)                       I  x  dx
                            ]
                            /
                             5

(%i5) %, nouns;
                               218
(%o5)                          ---
                                3
```


Wird der Quote-Operator auf einen eingeklammerten Ausdruck angewendet, wird die
Auswertung aller Symbole und Funktionen innerhalb der Klammern unterdruckt.



```maxima
(%i1) aa: 1024;
(%o1)                         1024
(%i2) bb: 19;
(%o2)                          19
(%i3) sqrt(aa) + bb;
(%o3)                          51
(%i4) '(sqrt(aa) + bb);
(%o4)                     bb + sqrt(aa)
(%i5) ''%;
(%o5)                          51
```


Der Quote-Operator unterdruckt nicht die Vereinfachung von Ausdrucken.



```maxima
(%i1) sin (17 * %pi) + cos (17 * %pi);
(%o1)                          - 1
(%i2) '(sin (17 * %pi) + cos (17 * %pi));
(%o2)                          - 1
```


Gleitkommarechnungen sind eine Vereinfachung und keine Auswertung.  Daher kann
die Berechnung von `sin(1.0)` nicht mit dem Quote-Operator unterdruckt
werden.



```maxima
(%i1) sin(1.0);
(%o1)                          .8414709848078965
(%i2) '(sin(1.0));
(%o2)                          .8414709848078965
```

See also: `noundisp`, `nouns`.

<!-- category: Other -->
<!-- keywords: '' -->
<!-- signatures: '' -->
### Function: ''

Der Quote-Quote-Operator `''` (zwei Hochkommata) modifiziert die 
Auswertung von Ausdrucken, die von der Eingabe gelesen werden.


Wird der Quote-Quote-Operator auf einen allgemeinen Ausdruck *expr*
angewendet, wird der Ausdruck *expr* durch seinen Wert ersetzt.


Wird der Quote-Quote-Operator auf den Operator eines Ausdruckes angewendet,
andert sich der Operator, wenn er in seiner Substantivform vorliegt, in die 
Verbform.


Der Quote-Quote-Operator wird vom Parser, der die Eingabe liest, sofort 
angewendet und nicht im eingelesen Ausdruck gespeichert.  Daher kann die 
Auswertung des Quote-Quote-Operators nicht durch einen weiteren Quote-Operator 
verhindert werden.  Der Quote-Quote-Operator fuhrt zur Auswertung von
Ausdrucken, deren Auswertung unterdruckt ist.  Das ist der Fall fur 
Funktionsdefinitionen, Lambda-Ausdrucke und Ausdrucke, deren Auswertung
durch den Quote-Operator verhindert wurde.


Der Quote-Quote-Operator wird von den Befehlen `batch` und
`load` erkannt.


Siehe auch den Quote-Operator `'` und den Auswertungsschalter
`nouns`.


Beispiele:


Wird der Quote-Quote-Operator auf einen Ausdruck *expr* angewendet, wird 
der Wert von *expr* in den Ausdruck eingesetzt.



```maxima
(%i1) expand ((a + b)^3);
                     3        2      2      3
(%o1)               b  + 3 a b  + 3 a  b + a
(%i2) [_, ''_];
                         3    3        2      2      3
(%o2)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i3) [%i1, ''%i1];
                         3    3        2      2      3
(%o3)     [expand((b + a) ), b  + 3 a b  + 3 a  b + a ]
(%i4) [aa : cc, bb : dd, cc : 17, dd : 29];
(%o4)                   [cc, dd, 17, 29]
(%i5) foo_1 (x) := aa - bb * x;
(%o5)                 foo_1(x) := aa - bb x
(%i6) foo_1 (10);
(%o6)                      cc - 10 dd
(%i7) ''%;
(%o7)                         - 273
(%i8) ''(foo_1 (10));
(%o8)                         - 273

(%i9) foo_2 (x) := ''aa - ''bb * x;
(%o9)                 foo_2(x) := cc - dd x

(%i10) foo_2 (10);
(%o10)                        - 273
(%i11) [x0 : x1, x1 : x2, x2 : x3];
(%o11)                    [x1, x2, x3]
(%i12) x0;
(%o12)                         x1
(%i13) ''x0;
(%o13)                         x2
(%i14) '' ''x0;
(%o14)                         x3
```


Wird der Quote-Quote-Operator auf den Operator in einem Ausdruck angewendet,
andert sich der Operator von seiner Substantivform in die Verbform.



```maxima
(%i1) declare (foo, noun);
(%o1)                         done
(%i2) foo (x) := x - 1729;
(%o2)                 ''foo(x) := x - 1729
(%i3) foo (100);
(%o3)                       foo(100)
(%i4) ''foo (100);
(%o4)                        - 1629
```


Der Quote-Quote-Operator wird vom Parser sofort auf den eingelesenen Ausdruck 
angewendet und ist nicht Teil eines Maxima-Ausdrucks.



```maxima
(%i1) [aa : bb, cc : dd, bb : 1234, dd : 5678];
(%o1)                 [bb, dd, 1234, 5678]
(%i2) aa + cc;
(%o2)                        dd + bb
(%i3) display (_, op (_), args (_));
                           _ = cc + aa

                         op(cc + aa) = +

                    args(cc + aa) = [cc, aa]

(%o3)                         done
(%i4) ''(aa + cc);
(%o4)                         6912
(%i5) display (_, op (_), args (_));

                           _ = dd + bb

                         op(dd + bb) = +

                    args(dd + bb) = [dd, bb]

(%o5)                         done
```


Der Quote-Quote-Operator bewirkt die Auswertung von Ausdrucken, deren
Auswertung unterdruckt ist wie in Funktionsdefinitionen, Lambda-Ausdrucken 
und Aus­dru­cken, auf die der Quote-Operator angewendet wurde.



```maxima
(%i1) foo_1a (x) := ''(integrate (log (x), x));
(%o1)               foo_1a(x) := x log(x) - x
(%i2) foo_1b (x) := integrate (log (x), x);
(%o2)           foo_1b(x) := integrate(log(x), x)
(%i3) dispfun (foo_1a, foo_1b);
(%t3)               foo_1a(x) := x log(x) - x

(%t4)           foo_1b(x) := integrate(log(x), x)

(%o4)                      [%t3, %t4]
(%i5) integrate (log (x), x);
(%o5)                     x log(x) - x
(%i6) foo_2a (x) := ''%;
(%o6)               foo_2a(x) := x log(x) - x
(%i7) foo_2b (x) := %;
(%o7)                    foo_2b(x) := %
(%i8) dispfun (foo_2a, foo_2b);
(%t8)               foo_2a(x) := x log(x) - x

(%t9)                    foo_2b(x) := %

(%o9)                      [%t8, %t9]
(%i10) F : lambda ([u], diff (sin (u), u));
(%o10)            lambda([u], diff(sin(u), u))
(%i11) G : lambda ([u], ''(diff (sin (u), u)));
(%o11)                 lambda([u], cos(u))
(%i12) '(sum (a[k], k, 1, 3) + sum (b[k], k, 1, 3));
(%o12)         sum(b , k, 1, 3) + sum(a , k, 1, 3)
                    k                  k
(%i13) '(''(sum (a[k], k, 1, 3)) + ''(sum (b[k], k, 1, 3)));
(%o13)             b  + a  + b  + a  + b  + a
                    3    3    2    2    1    1
```

See also: `batch`, `load`, `nouns`.

<!-- category: Other -->
<!-- keywords: ev -->
<!-- signatures: ev(expr, arg_1, ..., arg_n) -->
### Function: ev (expr, arg_1, ..., arg_n)

Wertet den Ausdruck *expr* in einer Umgebung aus, die durch die Argumente
*arg_1*, ..., *arg_n* spezifiziert wird.  Die Argumente sind
Optionsvariablen (Boolesche Variablen), Zuweisungen, Gleichungen und Funktionen.
`ev` gibt das Ergebnis der Auswertung zuruck.


Die Auswertung wird in den folgenden Schritten durchgefuhrt:



1. Zuerst wird die Umgebung gesetzt.  Dazu werden die Argumente *arg_1*,
..., *arg_n* ausgewertet.  Folgende Argumente sind moglich:



  - *
`simp` bewirkt, dass der Ausdruck *expr* vereinfacht wird.  Der Wert
der Optionsvariablen `simp` wird dabei ignoriert.  Der Ausdruck wird also
auch dann vereinfacht, wenn die Optionsvariable *simp* den Wert `false`
hat.
  - *
`noeval` unterdruckt die Auswertungphase der Funktion `ev` (siehe 
Schritt (4) unten).  Dies ist nutzlich im Zusammenhang mit anderen Schaltern
und um einen Ausdruck *expr* erneuert zu vereinfachen, ohne dass dieser
ausgewertet wird.
  - *
`nouns` bewirkt die Auswertung von Substantivformen.  Solche 
Substantivformen sind typischerweise nicht ausgewertete Funktionen wie 
`'integrate` oder `'diff`, die im Ausdruck *expr* enthalten sind.
  - *
`expand` bewirkt die Expansion des Ausdruckes *expr*.  Siehe die 
Funktion `expand`.
  - *
`expand`(*m*, *n*) bewirkt die Expansion des Ausdruckes *expr*, 
wobei den Optionsvariablen `maxposex` und `maxnegex` die Werte der
Argumente *m* und *n* zugewiesen werden.  Siehe die Funktion
`expand`.
  - *
`detout` bewirkt, dass bei der Berechnung von Inversen von Matrizen, die im
Ausdruck *expr* enthalten sind, Determinanten den Matrizen vorangestellt
und nicht elementweise in die Matrize hereinmultipliziert werden.
  - *
`diff` bewirkt, dass alle Ableitungen ausgefuhrt werden, die im Ausdruck
*expr* enthalten sind.
  - *
`derivlist(x, y, z, ...)` bewirkt, dass die Ableitungen
bezuglich der angegebenen Variablen *x*, *y*, *z*, ...
ausgefuhrt werden.
  - *
`risch` bewirkt das Integrale im Ausdruck *expr* mit dem
Risch-Algorithmus berechnet werden.  Siehe `risch`.  Wird der Schalter
`nouns` benutzt, wird der Standardalgorithmus fur Integrale verwendet.
  - *
`float` bewirkt, dass rationale Zahlen in Gleitkommazahlen konvertiert 
werden.
  - *
`numer` bewirkt, dass mathematische Funktionen mit numerischen Argumenten 
ein Ergebnis in Gleitkommazahlen liefern.  Variablen in `expr`, denen
numerische Werte zugewiesen wurden, werden durch diese ersetzt.  Der Schalter
`float` wird zusatzlich wirksam.
  - *
`pred` bewirkt, dass Aussagen zu `true` oder `false` ausgewertet 
werden.
  - *
`eval` bewirkt eine zusatzliche Auswertung des Ausdrucks *expr*.
(Siehe Schritt (5) unten).  `eval` kann mehrfach angewendet werden.  Jedes 
Auftreten von `eval` fuhrt zu einer weiteren Auswertung.
  - *
`A`, wobei `A` ein Symbol ist, das als ein Auswertungsschalter
`evflag` definiert ist.  Wahrend der Auswertung des Ausdrucks *expr* 
erhalt `A` den Wert `true`.
  - *
`V: expression` (oder alternativ `V=expression`) bewirkt, dass 
`V` wahrend der Auswertung des Ausdrucks *expr* den Wert
`expression` erhalt.  `V` kann auch eine Optionsvariable sein, die
fur die Auswertung den Wert `expression` erhalt.  Wenn mehr als ein 
Argument der Funktion `ev` ubergeben wird, wird die Zuweisung der Werte
parallel ausgefuhrt.  Wenn `V` kein Atom ist, wird anstatt einer
Zuweisung eine Substitution ausgefuhrt.
  - *
`F`, wobei `F` der Name einer Funktion ist, die als eine
Auswertungsfunktion (siehe `evfun`) definiert wurde.  `F` bewirkt,
dass die Auswertungsfunktion auf den Ausdruck *expr* angewendet wird.
  - *
Jeder andere Funktionsname (zum Beispiel `sum`) bewirkt, dass jedes
Auftreten dieser Funktion im Ausdruck *expr* ausgewertet wird.
  - *
Zusatzlich kann fur die Auswertung von *expr* eine lokale Funktion
`F(x) := expression` definiert werden.
  - *
Wird ein Symbol, eine indizierte Variable oder ein indizierter Ausdruck, der
oben nicht genannt wurde, als Argument ubergeben, wird das Argument
ausgewertet.  Wenn das Ergebnis eine Gleichung oder eine Zuweisung ist, werden
die entsprechenden Zuweisungen und Substitutionen ausgefuhrt.  Wenn das
Ergebnis eine Liste ist, werden die Elemente der Liste als zusatzliche
Argumente von `ev` betrachtet.  Dies erlaubt, das eine Liste mit
Gleichungen (zum Beispiel `[%t1, %t2]`, wobei `%t1` und `%t2` 
Gleichungen sind) wie sie zum Beispiel von der Funktion `solve` erzeugt
wird, als Argument verwendet werden kann.


Die Argumente der Funktion `ev` konnen in einer beliebigen Reihenfolge
ubergeben werden.  Ausgenommen sind Gleichungen mit Substitutionen, die
nacheinander von links nach rechts ausgewertet werden, sowie
Auswertungsfunktionen, die verkettet werden.  So wird zum Beispiel
`ev(expr, ratsimp, realpart)` zu
`realpart(ratsimp(expr))`.


Die Schalter `simp`, `numer`, `float` und 
`detout` sind auch Optionsvariablen, die lokal in einem Block oder global
gesetzt werden konnen.


Ist *expr* ein kanonischer rationaler Ausdruck (CRE = canonical rational
expression), ist auch das Ergebnis der Funktion `ev` ein CRE-Ausdruck, 
falls nicht die beiden Schalter `float` und `numer` den Wert 
`true` haben.
2. Wahrend des Schritts (1) wird eine Liste der nicht indizierten Variablen
erstellt, die auf der linken Seite von Gleichungen auftreten.  Die Gleichungen
konnen dabei entweder als Argument oder als Wert eines Argumentes vorliegen.
Variablen, die nicht in dieser Liste enthalten sind, werden durch ihre globalen 
Werte ersetzt.  Davon ausgenommen sind Variablen, die eine Array-Funktion 
reprasentieren.  Ist zum Beispiel *expr* eine Marke wie `%i2` im
Beispiel unten oder das letzte Ergebnis `%`, so wird in diesem Schritt der
globale Wert dieser Marke eingesetzt und die Bearbeitung durch `ev`
fortgesetzt.
3. Wenn in den Argumenten Substitutionen aufgefuhrt sind, werden diese nun 
ausgefuhrt.
4. Der resultierende Ausdruck wird erneut ausgewertet, außer wenn `noeval` 
unter den Argumente ist, und vereinfacht.  Die Funktionsaufrufe in *expr* 
werden erst ausgefuhrt, wenn die enthaltenden Variablen ausgewertet sind.
Dadurch verhalt sich `ev(F(x))` wie `F(ev(x))`.
5. Fur jedes Auftreten des Schalters `eval` in den Argumenten werden die 
Schritte (3) und (4) wiederholt.


Anstatt der Anwendung der Funktion `ev` konnen alternativ der Ausdruck
und die Argumente durch Kommata getrennt eingegeben werden:



```maxima
expr, arg_1, ..., arg_n
```


Diese Kurzschreibweise ist jedoch als Teil eines anderen Ausdrucks, zum Beispiel
in Funktionen oder Blocken nicht gestattet.


Beispiele:



```maxima
(%i1) sin(x) + cos(y) + (w+1)^2 + 'diff (sin(w), w);
                                     d                    2
(%o1)              cos(y) + sin(x) + -- (sin(w)) + (w + 1)
                                     dw

(%i2) ev (%, numer, expand, diff, x=2, y=1);
                               2
(%o2)                cos(w) + w  + 2 w + 2.449599732693821
```


Im folgenden Beispiel werden die Zuweisungen parallel durchgefuhrt.  Es wird
die Kurzschreibweise der Funktion `ev` angewendet.



```maxima
(%i3) programmode: false;
(%o3)                                false
(%i4) x+y, x: a+y, y: 2;
(%o4)                              y + a + 2
(%i5) 2*x - 3*y = 3$
(%i6) -3*x + 2*y = -4$
(%i7) solve ([%o5, %o6]);
Solution


                                          1
(%t7)                               y = - -
                                          5


                                         6
(%t8)                                x = -
                                         5
(%o8)                            [[%t7, %t8]]
(%i8) %o6, %o8;
(%o8)                              - 4 = - 4
(%i9) x + 1/x > gamma (1/2);
                                   1
(%o9)                          x + - > sqrt(%pi)
                                   x
(%i10) %, numer, x=1/2;
(%o10)                      2.5 > 1.772453850905516
(%i11) %, pred;
(%o11)                               true
```

See also: `simp`, `expand`, `maxposex`, `maxnegex`, `nouns`, `float`, `evflag`, `evfun`, `solve`, `numer`, `detout`.

<!-- category: Other -->
<!-- keywords: eval -->
<!-- signatures: eval -->
### Variable: eval

Als Argument des Kommandos `ev(expr, eval)` bewirkt `eval` eine
zusatzliche Auswertung des Ausdrucks `expr`.


`eval` kann mehrfach auftreten.  Jedes Auftreten fuhrt zu einer
zusatzlichen Auswertung.


Siehe auch die Funktion `ev` sowie die Auswertungsschalter
`noeval` und `infeval`


Beispiele:



```maxima
(%i1) [a:b,b:c,c:d,d:e];
(%o1)                            [b, c, d, e]
(%i2) a;
(%o2)                                  b
(%i3) ev(a);
(%o3)                                  c
(%i4) ev(a),eval;
(%o4)                                  e
(%i5) a,eval,eval;
(%o5)                                  e
```

See also: `ev`, `noeval`, `infeval`.

<!-- category: Other -->
<!-- keywords: evflag -->
<!-- signatures: evflag -->
### Variable: evflag

Wenn ein Symbol *x* die Eigenschaft eines Auswertungsschalters besitzt, sind
die Ausdrucke `ev(expr, x)` und `expr, x`
aquivalent zu `ev(expr, x = true)`.  Wahrend der Auswertung
von *expr* erhalt also *x* den Wert `true`.


Mit `declare(x, evflag)` wird der Variablen *x* die
`evflag`-Eigenschaft gegeben.  Siehe auch die Funktion
`declare`.  Mit `kill` oder `remove` kann diese Eigenschaft
wieder entfernt werden.  Siehe auch `properties` fur die Anzeige von
Eigenschaften.


Folgende Optionsvariablen haben bereits die `evflag`-Eigenschaft:



   algebraic           cauchysum       demoivre         
   dotscrules          %emode          %enumer     
   exponentialize      exptisolate     factorflag
   float               halfangles      infeval
   isolate_wrt_times   keepfloat       letrat
   listarith           logabs          logarc
   logexpand           lognegint       
   m1pbranch           numer_pbranch   programmode
   radexpand           ratalgdenom     ratfac
   ratmx               ratsimpexpons   simp
   simpproduct         simpsum         sumexpand
   trigexpand


Beispiele:



```maxima
(%i1) sin (1/2);
                                 1
(%o1)                        sin(-)
                                 2
(%i2) sin (1/2), float;
(%o2)                   0.479425538604203
(%i3) sin (1/2), float=true;
(%o3)                   0.479425538604203
(%i4) simp : false;
(%o4)                         false
(%i5) 1 + 1;
(%o5)                         1 + 1
(%i6) 1 + 1, simp;
(%o6)                           2
(%i7) simp : true;
(%o7)                         true

(%i8) sum (1/k^2, k, 1, inf);
                            inf
                            ====
                            \     1
(%o8)                        >    --
                            /      2
                            ====  k
                            k = 1

(%i9) sum (1/k^2, k, 1, inf), simpsum;
                                 2
                              %pi
(%o9)                         ----
                               6
(%i10) declare (aa, evflag);
(%o10)                        done
(%i11) if aa = true then YES else NO;
(%o11)                         NO
(%i12) if aa = true then YES else NO, aa;
(%o12)                         YES
```

See also: `declare`, `kill`, `remove`, `properties`.

<!-- category: Other -->
<!-- keywords: evfun -->
<!-- signatures: evfun -->
### Variable: evfun

Wenn eine Funktion *F* die Eigenschaft `evfun` besitzt, sind die 
Ausdrucke `ev(expr, F)` und `expr, F`
aquivalent zu `F(ev(expr))`.


Zwei oder mehr `evfun`-Funktionen *F*, *G*, ... werden in der 
aufgefuhrten Reihenfolge auf den Ausdruck *expr* angewendet.


Mit `declare(F, evfun)` wird der Funktion *F* die
`evfun`-Eigenschaft gegeben.  Siehe auch die Funktion `declare`.
Mit `kill` oder `remove` kann diese Eigenschaft wieder entfernt
werden.  Siehe auch `properties` fur die Anzeige von Eigenschaften.


Funktionen, die bereits die `evfun`-Eigenschaft besitzen, sind:



   bfloat          factor       fullratsimp
   logcontract     polarform    radcan
   ratexpand       ratsimp      rectform
   rootscontract   trigexpand   trigreduce


Beispiele:



```maxima
(%i1) x^3 - 1;
                              3
(%o1)                        x  - 1
(%i2) x^3 - 1, factor;

                                2
(%o2)                 (x - 1) (x  + x + 1)

(%i3) factor (x^3 - 1);
                                2
(%o3)                 (x - 1) (x  + x + 1)
(%i4) cos(4 * x) / sin(x)^4;
                            cos(4 x)
(%o4)                       --------
                               4
                            sin (x)
(%i5) cos(4 * x) / sin(x)^4, trigexpand;
                 4           2       2         4
              sin (x) - 6 cos (x) sin (x) + cos (x)
(%o5)         -------------------------------------
                                4
                             sin (x)
(%i6) cos(4 * x) / sin(x)^4, trigexpand, ratexpand;

                           2         4
                      6 cos (x)   cos (x)
(%o6)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)

(%i7) ratexpand (trigexpand (cos(4 * x) / sin(x)^4));
                           2         4
                      6 cos (x)   cos (x)
(%o7)               - --------- + ------- + 1
                          2          4
                       sin (x)    sin (x)
(%i8) declare ([F, G], evfun);
(%o8)                         done
(%i9) (aa : bb, bb : cc, cc : dd);
(%o9)                          dd
(%i10) aa;
(%o10)                         bb
(%i11) aa, F;
(%o11)                        F(cc)
(%i12) F (aa);
(%o12)                        F(bb)
(%i13) F (ev (aa));
(%o13)                        F(cc)
(%i14) aa, F, G;
(%o14)                      G(F(cc))
(%i15) G (F (ev (aa)));
(%o15)                      G(F(cc))
```

See also: `declare`, `kill`, `remove`, `properties`.

<!-- category: Other -->
<!-- keywords: infeval -->
<!-- signatures: infeval -->
### Variable: infeval

Standardwert: `false`


`infeval` bewirkt, dass die Funktion `ev` die Auswertung eines
Ausdrucks solange wiederholt, bis dieser sich nicht mehr andert.  Um zu
verhindern, dass eine Variable in diesem Modus durch die Auswertung
verschwindet, kann zum Beispiel fur eine Variable `x` der Ausdruck
`x='x` als Argument von `ev` einfugt werden.  Ausdrucke wie
`ev(x, x=x+1, infeval)` fuhren in diesem Modus zu Endlosschleifen.


Siehe auch die Auswertungsschalter `noeval` und `eval`.

See also: `ev`, `noeval`, `eval`.

<!-- category: Other -->
<!-- keywords: noeval -->
<!-- signatures: noeval -->
### Variable: noeval

`noeval` unterdruckt die Auswertungsphase der Funktion `ev`.
Der Schalter kann im Zusammenhang mit anderen Auswertungsschaltern genutzt
werden, um einen Ausdruck erneut zu vereinfachen, ohne diesen auszuwerten.


Siehe auch die Optionsvariable `infeval` und den Auswertungsschalter
`eval`.

See also: `ev`, `infeval`, `eval`.

<!-- category: Other -->
<!-- keywords: nouns -->
<!-- signatures: nouns -->
### Variable: nouns

`nouns` ist ein Auswertungsschalter.  Wird dieser Schalter als eine Option
der Funktion `ev` genutzt, werden alle Substantivformen, die in dem
Ausdruck enthalten sind, in Verbformen umgewandelt und ausgewertet.


Siehe auch die Eigenschaft `noun` und die Funktionen `nounify` und
`verbify`.

See also: `ev`, `noun`, `nounify`, `verbify`.

<!-- category: Other -->
<!-- keywords: pred -->
<!-- signatures: pred -->
### Variable: pred

Wird `pred` als ein Argument der Funktion `ev` eingesetzt, werden
Aussagen zu `true` oder `false` ausgewertet.  Siehe die Funktion
`ev`.


Beispiel:



```maxima
(%i1) 1 < 2;
(%o1)                                1 < 2
(%i2) 1 < 2,pred;
(%o2)                                true
```

See also: `ev`.

