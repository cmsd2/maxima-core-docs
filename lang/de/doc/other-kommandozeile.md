## Kommandozeile

<!-- category: Other -->
<!-- keywords: $ -->
<!-- signatures: $ -->
### Variable: $

Das Dollarzeichen schließt wie das Semikolon die Eingabe eines Ausdruckes
auf der Konsole und in einer Datei ab.  Im Unterschied zum Semikolon wird die
Ausgabe des Ergebnisses unterdruckt.  Das Ergebnis wird jedoch weiterhin
einer Ausgabemarke `outchar` zugewiesen und die Systemvariable 
`%` enthalt das Ergebnis.  Siehe auch `;`.


Beispiele:



```maxima
(%i1) expand((a+b)^2)$

(%i2) %;
                          2            2
(%o2)                    b  + 2 a b + a
(%i3) a:10$ a+b$

(%i5) %o3;
(%o5)                          10
(%i6) %o4;
(%o6)                        b + 10
```

See also: `outchar`, `%`, `;`.

<!-- category: Other -->
<!-- keywords: % -->
<!-- signatures: % -->
### Variable: %

Die Systemvariable `%` enthalt das Ergebnis des zuletzt von Maxima
ausgewerteten und vereinfachten Ausdrucks.  `%` enhalt das letzte 
Ergebnis auch dann, wenn die Ausgabe des Ergebnisses durch Abschluss der Eingabe
mit einem Dollarzeichen `$` unterdruckt wurde.


Die Systemvariable `%` wird von den Funktionen `batch` und
`load` erkannt.  Wird eine Datei mit der Funktion `batch`
ausgefuhrt, hat `%` dieselbe Bedeutung wie bei der Eingabe in einer
Kommandozeile.  Wird eine Datei mit der Funktion `load` geladen, enthalt
`%` das letzte Ergebnis des Ausdrucks, der auf der Konsole eingegeben
wurde.


Siehe auch die Systemvariablen `_`, `__` und `%th`.

See also: `$`, `batch`, `load`, `_`, `__`, `%th`.

<!-- category: Other -->
<!-- keywords: %% -->
<!-- signatures: %% -->
### Variable: %%

In zusammengesetzten Ausdrucken, wie in Ausdrucken mit `block` oder
`lambda` oder in Ausdrucken der Gestalt `(s_1, ..., s_n)`,
enthalt die Systemvariable `%%` das Ergebnis des 
vorhergehenden Ausdrucks.  Fur den ersten Ausdruck oder außerhalb eines
zusammengesetzten Ausdrucks ist `%%` nicht definiert.


Die Systemvariable `%%` wird von `batch` und `load` erkannt und
hat dieselbe Bedeutung wie bei der Eingabe in der Konsole.  Siehe auch die 
Systemvariable `%` und die Funktion `%th`.


Beispiele:


Auf die im ersten Ausdruck berechnete Stammfunktion wird im zweiten Ausdruck
mit `%%` Bezug genommen, um das Integral an der oberen und unteren Grenze
auszuwerten.



```maxima
(%i1) block (integrate (x^5, x), ev (%%, x=2) - ev (%%, x=1));
                               21
(%o1)                          --
                               2
```


Ein zusammengesetzter Ausdruck kann weitere zusammengesetzte Ausdrucke 
enthalten.  `%%` enthalt dabei jeweils das Ergebnis des letzten 
Ausdrucks.  Das folgende Beispiel hat das Ergebnis `7*a^n`.



```maxima
(%i3) block (block (a^n, %%*42), %%/6);
                                 n
(%o3)                         7 a
```


Der Wert der Systemvariablen `%%` kann nach einer Unterbrechung mit dem 
Kommando `break` inspiziert werden.  In diesem Beispiel hat die
Systemvariable `%%` den Wert 42.



```maxima
(%i4) block (a: 42, break ())$
Entering a Maxima break point. Type 'exit;' to resume.
_%%;
42
_
```

See also: `block`, `lambda`, `batch`, `load`, `%`, `%th`, `break`.

<!-- category: Other -->
<!-- keywords: %edispflag -->
<!-- signatures: %edispflag -->
### Variable: %edispflag

Standardwert: `false`


Hat `%edispflag` den Wert `true`, zeigt Maxima die Exponentiation von
`%e` mit einem negativen Exponenten als Quotienten an.  Siehe auch die
Optionsvariable `exptdispflag`.


Beispiel:



```maxima
(%i1) %e^-10;
                               - 10
(%o1)                        %e
(%i2) %edispflag:true$
(%i3) %e^-10;
                               1
(%o3)                         ----
                                10
                              %e
```

See also: `%e`, `exptdispflag`.

<!-- category: Other -->
<!-- keywords: %th -->
<!-- signatures: %th(n) -->
### Function: %th (n)

Die Funktion `%th` liefert das n-te vorhergehende Ergebnis.  Dies ist dann
nutzlich, wenn wie in Batch-Dateien die absolute Zeilennummer der letzten
Ausgabemarken nicht bekannt ist.


Die Funktion `%th` wird von den Funktionen `batch` und 
`load` erkannt.  Wird eine Datei mit `batch` ausgefuhrt, hat
`%th` dieselbe Bedeutung wie bei der Eingabe in der Konsole.  Wird eine
Datei mit der Funktion `load` geladen, enthalt `%th` das letzte 
Ergebnis der Eingabe in der Konsole.


Siehe auch `%` und `%%`.


Beispiel:


Das Beispiel zeigt, wie die letzten 5 eingegebenen Werte mit der Funktion 
`%th` aufsummiert werden.



```maxima
(%i1) 1;2;3;4;5;
(%o1)                           1
(%o2)                           2
(%o3)                           3
(%o4)                           4
(%o5)                           5
(%i6) block (s: 0, for i:1 thru 5 do s: s + %th(i), s);
(%o6)                          15
```

See also: `batch`, `load`, `%`, `%%`.

<!-- category: Other -->
<!-- keywords: ; -->
<!-- signatures: ; -->
### Variable: ;

Mit dem Semikolon `;` wird die Eingabe eines Maxima-Ausdrucks auf der
Konsole und in einer Datei abgeschlossen.  Es konnen mehrere Ausdrucke mit
einem Semikolon als Abschluss auf einer Zeile eingegeben werden.  Siehe auch
`$`.


Beispiele:



```maxima
(%i1) a:10;
(%o1)                          10
(%i2) a+b;
(%o2)                        b + 10
(%i3) x:10; x+y;
(%o3)                          10
(%o4)                        y + 10
```

See also: `$`.

<!-- category: Other -->
<!-- keywords: ? -->
<!-- signatures: ? -->
### Function: ?

Wird dem Namen einer Funktion oder Variablen ein `?` als Prafix
vorangestellt, wird der Name als ein Lisp-Symbol interpretiert.  Zum Beispiel 
bedeutet `?round` die Lisp-Funktion `ROUND`.  Siehe
`Lisp-und-Maxima` fur weitere Ausfuhrungen zu diesem Thema.


Die Eingabe `? word` ist eine Kurzschreibweise fur das Kommando 
`describe("word")`.  Das Fragezeichen muss am Anfang einer Eingabezeile 
stehen, damit Maxima die Eingabe als eine Anfrage nach der Dokumentation
interpretiert.  Siehe auch `describe`.

See also: `Lisp-und-Maxima`, `describe`.

<!-- category: Other -->
<!-- keywords: ?? -->
<!-- signatures: ?? -->
### Function: ??

Die Eingabe `?? word` ist eine Kurzschreibweise fur das Kommando 
`describe("word", inexact)`.  Die Fragezeichen mussen am Anfang einer 
Eingabezeile stehen, damit Maxima die Eingabe als eine Anfrage nach der 
Dokumentation interpretiert.  Siehe auch `describe`.

See also: `describe`.

<!-- category: Other -->
<!-- keywords: _ -->
<!-- signatures: _ -->
### Variable: _

Die Systemvariable `_` enthalt den zuletzt eingegebenen Ausdruck 
*expr*.  Der Ausdruck *expr* wird der Systemvariablen `_` vor der 
Auswertung und Vereinfachung zugewiesen.


Die Systemvariable `_` wird von den Funktionen `batch` und
`load` erkannt.  Wird eine Datei mit der Funktion `batch`
ausgefuhrt, hat `_` dieselbe Bedeutung wie bei der Eingabe in einer
Kommandozeile.  Wird eine Datei mit der Funktion `load` geladen, enthalt
`_` das zuletzt in der Kommandozeile eingegebene Kommando.


Siehe auch die Systemvariablen `__` und `%`.


Beispiele:


Die Funktion `cabs` wird ausgewertet und nicht vereinfacht.  Das Beispiel
zeigt, dass die Systemvariable `_` den zuletzt eingelesenen Ausdruck vor
der Auswertung enthalt.



```maxima
(%i1) cabs(1+%i);
(%o1)                        sqrt(2)
(%i2) _;
(%o2)                     cabs(%i + 1)
```


Die Funktion `abs` vereinfacht einen Ausdruck.  Wird der Inhalt der 
Systemvariablen `_` ausgegeben, wird das fur die Ausgabe vereinfachte
Ergebnis angezeigt.  Mit der Funktion `string` wird der Inhalt der 
Systemvariablen `_` vor der Ausgabe in ein Zeichenkette umgewandelt, um 
den nicht vereinfachten Wert sichtbar zu machen.



```maxima
(%i3) abs(1+%i);
(%o3)                        sqrt(2)
(%i4) _;
(%o4)                        sqrt(2)
(%i5) abs(1+%i);
(%o5)                        sqrt(2)
(%i6) string(_);
(%o6)                       abs(1+%i)
```

See also: `batch`, `load`, `__`, `%`, `cabs`, `abs`, `string`.

<!-- category: Other -->
<!-- keywords: __ -->
<!-- signatures: __ -->
### Variable: __

Wahrend einer laufenden Auswertung enthalt die Systemvariable `__` den
zuletzt vom Parser eingelesenen Ausdruck *expr*.  Der Ausdruck *expr*
wird der Systemvariablen `__` vor der Auswertung und Vereinfachung
zugewiesen.


Die Systemvariable `__` wird von den Funktionen `batch` und
`load` erkannt.  Wird eine Datei mit der Funktion `batch`
ausgefuhrt, hat `__` dieselbe Bedeutung wie bei der Eingabe in einer 
Kommandozeile.  Wird eine Datei mit dem Namen `filename` mit der Funktion 
`load` geladen, enthalt `__` den Ausdruck 
`load(filename)`.  Das ist die letzte Eingabe in der Kommandozeile.


Siehe auch die Systemvariablen `_` und `%`.


Beispiele:



```maxima
(%i1) print ("I was called as: ", __)$
I was called as:  print(I was called as, __) 

(%i2) foo (__);
(%o2)                     foo(foo(__))

(%i3) g (x) := (print ("Current input expression =", __), 0)$
(%i4) [aa : 1, bb : 2, cc : 3]$
(%i5) (aa + bb + cc)/(dd + ee + g(x))$

                            cc + bb + aa
Current input expression = -------------- 
                           g(x) + ee + dd
```

See also: `batch`, `load`, `_`, `%`.

<!-- category: Other -->
<!-- keywords: absboxchar -->
<!-- signatures: absboxchar -->
### Variable: absboxchar

Standardwert: `!`


Die Optionsvariable `absboxchar` enthalt das Zeichen, das von Maxima
benutzt wird, um den Betrag eines Ausdruckes anzuzeigen, der mehr als eine
Zeile benotigt.


Beispiel:



```maxima
(%i1) abs((x^3+1));
                            ! 3    !
(%o1)                       !x  + 1!
```

<!-- category: Other -->
<!-- keywords: disp -->
<!-- signatures: disp(expr_1, expr_2, ...) -->
### Function: disp (expr_1, expr_2, ...)

Ist ahnlich wie die Funktion `display`.  Die Funktion `disp`
zeigt jedoch keine Gleichungen sondern nur die Ergebnisse der Ausdrucke
*expr_1*, *expr_2*, ... an.


Siehe auch die Funktionen `ldisp`, `display` und `print`.


Beispiele:



```maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$
(%i3) disp(x, b[1,2], sin(1.0));
                               123

                                  2
                             x - x

                        .8414709848078965

(%o3)                         done
```

See also: `display`, `ldisp`, `print`.

<!-- category: Other -->
<!-- keywords: display -->
<!-- signatures: display(expr_1, expr_2, ...) -->
### Function: display (expr_1, expr_2, ...)

Die Variablen oder Ausdrucke *expr_i* werden als eine Gleichung 
ausgegeben.  Die linke Seite der Gleichung ist die Variable oder der Ausdruck 
*expr_i* und die rechte Seite der Wert der Variablen oder das Ergebnis des 
Ausdrucks.  Die Argumente konnen Variable, indizierte Variable oder Funktionen
sein.


Siehe auch die Funktionen `ldisplay`, `disp` und `ldisp`.


Beispiele:



```maxima
(%i1) b[1,2]:x-x^2$
(%i2) x:123$
(%i3) display(x, b[1,2], sin(1.0));
                             x = 123

                                      2
                         b     = x - x
                          1, 2

                  sin(1.0) = .8414709848078965

(%o3)                         done
```

See also: `ldisplay`, `disp`, `ldisp`.

<!-- category: Other -->
<!-- keywords: display2d -->
<!-- signatures: display2d -->
### Variable: display2d

Standardwert: `true`


Hat `display2d` den Wert `false`, werden Ausdrucke auf der Konsole
linear und nicht zweidimensional angezeigt.


Siehe auch die Optionsvariable `leftjust`, um Formeln linksbundig
auszugeben.


Beispiel:



```maxima
(%i1) x/(x^2+1);
                               x
(%o1)                        ------
                              2
                             x  + 1
(%i2) display2d:false$
(%i3) x/(x^2+1);
(%o3) x/(x^2+1)
```

See also: `leftjust`.

<!-- category: Other -->
<!-- keywords: display_format_internal -->
<!-- signatures: display_format_internal -->
### Variable: display_format_internal

Standardwert: `false`


Hat `display_format_internal` den Wert `true`, werden Ausdrucke 
fur die Anzeige nicht in die externe Darstellung transformiert.  Die Ausgabe 
erfolgt wie in der internen Darstellung.  Das entspricht der Ruckgabe der 
Funktion `inpart`.


Siehe die Funktion `dispform` fur Beispiele, die den Unterschied zwischen
der internen und der externen Darstellung zeigen.

See also: `inpart`, `dispform`.

<!-- category: Other -->
<!-- keywords: dispterms -->
<!-- signatures: dispterms(expr) -->
### Function: dispterms (expr)

Der Ausdruck *expr* wird zeilenweise ausgegeben.  Auf der ersten Zeile wird
der Operator des Ausdrucks *expr* ausgegeben.  Dann werden die Argumente des
Operators zeilenweise ausgegeben.  Dies kann nutzlich sein, wenn ein Ausdruck 
sehr lang ist.


Beispiel:



```maxima
(%i1) dispterms(2*a*sin(x)+%e^x);

+

2 a sin(x)

  x
%e

(%o1)                         done
```

<!-- category: Other -->
<!-- keywords: expt, ncexpt -->
<!-- signatures: expt(a, b), ncexpt(a, b) -->
### Variable: expt

Ist ein Exponentialausdruck zu lang, um ihn als `a^b` 
anzuzeigen, wird stattdessen `expt(a, b)` angezeigt.
Entsprechend wird statt `a^^b`, `ncexpt(a, b)`
angezeigt.  `expt` und `ncexpt` sind keine Funktionen und erscheinen 
nur in der Ausgabe.

<!-- category: Other -->
<!-- keywords: exptdispflag -->
<!-- signatures: exptdispflag -->
### Variable: exptdispflag

Standardwert: `true`


Hat die Optionsvariable `exptdispflag` den Wert `true`, werden
Ausdrucke mit einem negativen Exponenten als Quotient angezeigt.  Siehe auch
die Optionsvariable `%edispflag`.


Beispiele:



```maxima
(%i1) exptdispflag:true;
(%o1)                         true
(%i2) 10^-x;
                                1
(%o2)                          ---
                                 x
                               10
(%i3) exptdispflag:false;
(%o3)                         false
(%i4) 10^-x;
                                - x
(%o4)                         10
```

See also: `%edispflag`.

<!-- category: Other -->
<!-- keywords: grind -->
<!-- signatures: grind(expr) -->
### Function: grind (expr)

Die Funktion `grind` gibt den Ausdruck *expr* auf der Konsole in einer
Form aus, die fur die Eingabe in Maxima geeignet ist.  `grind` gibt 
`done` zuruck.


Ist *expr* der Name einer Funktion oder eines Makros, gibt `grind`
die Definition der Funktion oder des Makros aus.


Siehe auch die Funktion `string`, die einen Ausdruck als eine
Zeichenkette zuruckgibt.


Hat die Optionsvariable `grind` den Wert `true`, haben die Ergebnisse
der Funktionen `stringout` und `string` dasselbe Format wie die 
Funktion `grind`.  Ansonsten werden keine spezielle Formatierungen
von diesen Funktionen vorgenommen.  Der Standardwert der Optionsvariablen
`grind` ist `false`.


`grind` kann auch ein Argument der Funktion `playback` sein.  In
diesem Fall gibt `playback` die Eingabe im gleichen Format wie die Funktion
`grind` aus.


`grind` wertet das Argument aus.


Beispiele:



```maxima
(%i1) aa + 1729;
(%o1)                       aa + 1729
(%i2) grind (%);
aa+1729$
(%o2)                         done
(%i3) [aa, 1729, aa + 1729];
(%o3)                 [aa, 1729, aa + 1729]
(%i4) grind (%);
[aa,1729,aa+1729]$
(%o4)                         done
(%i5) matrix ([aa, 17], [29, bb]);
                           [ aa  17 ]
(%o5)                      [        ]
                           [ 29  bb ]
(%i6) grind (%);
matrix([aa,17],[29,bb])$
(%o6)                         done
(%i7) set (aa, 17, 29, bb);
(%o7)                   {17, 29, aa, bb}
(%i8) grind (%);
{17,29,aa,bb}$
(%o8)                         done
(%i9) exp (aa / (bb + 17)^29);

                                aa
                            -----------
                                     29
                            (bb + 17)
(%o9)                     %e

(%i10) grind (%);
%e^(aa/(bb+17)^29)$
(%o10)                        done
(%i11) expr: expand ((aa + bb)^10);

         10           9        2   8         3   7         4   6
(%o11) bb   + 10 aa bb  + 45 aa  bb  + 120 aa  bb  + 210 aa  bb
         5   5         6   4         7   3        8   2
 + 252 aa  bb  + 210 aa  bb  + 120 aa  bb  + 45 aa  bb
        9        10
 + 10 aa  bb + aa

(%i12) grind (expr);

bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6
     +252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2
     +10*aa^9*bb+aa^10$
(%o12)                        done

(%i13) string (expr);
(%o13) bb^10+10*aa*bb^9+45*aa^2*bb^8+120*aa^3*bb^7+210*aa^4*bb^6\
+252*aa^5*bb^5+210*aa^6*bb^4+120*aa^7*bb^3+45*aa^8*bb^2+10*aa^9*\
bb+aa^10
```

See also: `string`, `stringout`, `playback`.

<!-- category: Other -->
<!-- keywords: ibase -->
<!-- signatures: ibase -->
### Variable: ibase

Standardwert: `10`


`ibase` enthalt die Basis der ganzen Zahlen, welche von Maxima eingelesen
werden.


`ibase` kann eine ganze Zahl zwischen 2 und einschließlich 36 
zugewiesen werden.  Ist `ibase` großer als 10, werden die Zahlen 0 
bis 9 und die Buchstaben A, B, C, ... fur die Darstellung der Zahl in der 
Basis `ibase` herangezogen.  Große und kleine Buchstaben werden nicht 
unterschieden.  Die erste Stelle muss immer eine Ziffer sein, damit Maxima den 
eingelesenen Ausdruck als eine Zahl interpretiert.


Gleitkommazahlen werden immer zur Basis 10 interpretiert.


Siehe auch `obase`.


Beispiele:


`ibase` ist kleiner als 10.



```maxima
(%i1) ibase : 2 $
(%i2) obase;
(%o2)                          10
(%i3) 1111111111111111;
(%o3)                         65535
```


`ibase` ist großer als 10.  Die erste Stelle muss eine Ziffer sein.



```maxima
(%i1) ibase : 16 $
(%i2) obase;
(%o2)                          10
(%i3) 1000;
(%o3)                         4096
(%i4) abcd;
(%o4)                         abcd
(%i5) symbolp (abcd);
(%o5)                         true
(%i6) 0abcd;
(%o6)                         43981
(%i7) symbolp (0abcd);
(%o7)                         false
```


Wird eine ganze Zahl mit einem Dezimalpunkt beendet, wird die Zahl als 
Gleitkommazahl interpretiert.



```maxima
(%i1) ibase : 36 $
(%i2) obase;
(%o2)                          10
(%i3) 1234;
(%o3)                         49360
(%i4) 1234.;
(%o4)                         1234
```

See also: `obase`.

<!-- category: Other -->
<!-- keywords: inchar -->
<!-- signatures: inchar -->
### Variable: inchar

Standardwert: `%i`


Die Optionsvariable `inchar` enthalt den Prafix der Eingabemarken.
Maxima erzeugt die Eingabemarken automatisch aus dem Prafix `inchar` und
der Zeilennummer `linenum`.


Der Optionsvariablen `inchar` kann eine Zeichenkette oder ein Symbol 
zugewiesen werden, die auch mehr als ein Zeichen haben konnen.  Da Maxima 
intern nur das erste Zeichen berucksichtigt, sollten sich die Prafixe
`inchar`, `outchar` und `linechar` im ersten Zeichen voneinander
unterscheiden.  Ansonsten funktionieren einige Kommandos wie zum Beispiel 
`kill(inlabels)` nicht wie erwartet.


Siehe auch die Funktion und Systemvariable `labels` sowie die
Optionsvariablen `outchar` und `linechar`.


Beispiele:



```maxima
(%i1) inchar: "input";
(%o1)                         input
(input2) expand((a+b)^3);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(input3)
```

See also: `linenum`, `labels`, `outchar`, `linechar`.

<!-- category: Other -->
<!-- keywords: infolists -->
<!-- signatures: infolists -->
### Variable: infolists

Die Systemvariable `infolists` enthalt eine Liste der Informationslisten,
die Maxima zur Verfugung stellt.  Diese sind:



**labels** — Enthalt die Marken `%i`, `%o` und `%t`, denen bisher ein 
Ausdruck zugewiesen wurde.
**values** — Enthalt die vom Nutzer mit den Operatoren `:` oder `::` definierten
Variablen.
**functions** — Enthalt die vom Nutzer mit dem Operator `:=` oder der Funktion
`define` definierten Funktionen.
**arrays** — Enthalt die mit den Operatoren `:`, `::` oder `:=` definierten
Arrays oder Array-Funktionen.
**macros** — Enthalt die vom Nutzer mit dem Operator `::=` definierten Makros.
**myoptions** — Enthalt die Optionsvariablen, die vom Nutzer bisher einen neuen Wert erhalten
haben.
**rules** — Enthalt die vom Nutzer mit den Funktionen `tellsimp`,
`tellsimpafter`, `defmatch` oder `defrule`
definierten Regeln.
**aliases** — Enthalt die Symbole, die einen vom Nutzer definierten Alias-Namen mit der
Funktion `alias` erhalten haben.  Weiterhin erzeugen die Funktionen
`ordergreat` und `orderless` sowie eine Deklaration als
`noun` mit der Funktion `declare` Alias-Namen, die in die Liste
eingetragen werden.
**dependencies** — Enthalt alle Symbole, fur die mit den Funktionen `depends` oder
`gradef` eine Abhangigkeit definiert ist.
**gradefs** — Enthalt die Funktionen, fur die der Nutzer mit der Funktion
`gradef` eine Ableitung definiert hat.
**props** — Enthalt die Symbole, die eine Eigenschaft mit der Funktion
`declare` erhalten haben.
**let_rule_packages** — Enthalt die vom Nutzer definierten `let`-Regeln.

See also: `:`, `::`, `:=`, `define`, `::=`, `tellsimp`, `tellsimpafter`, `defmatch`, `defrule`, `alias`, `ordergreat`, `orderless`, `noun`, `declare`, `depends`, `gradef`, `let`.

<!-- category: Other -->
<!-- keywords: kill -->
<!-- signatures: kill(a_1, ..., a_n), kill(labels), kill(inlabels, outlabels, linelabels), kill(n), kill([m, n]), kill(values, functions, arrays, ...), kill(all), kill(allbut(a_1, ..., a_n)) -->
### Function: kill (a_1, ..., a_n)

Die Funktion `kill` entfernt alle Zuweisungen (Werte, Funktionen, Arrays 
oder Regeln) und Eigenschaften von den Argumenten *a_1*, ..., *a_n*.
Ein Argument *a_k* kann ein Symbol oder ein einzelnes Array-Element sein.
Ist *a_k* ein einzelnes Array-Element, entfernt `kill` die Zuweisungen
an dieses Element, ohne die anderen Elemente des Arrays zu beeinflussen.


`kill` kennt verschiedene spezielle Argumente, die auch kombiniert werden 
konnen wie zum Beispiel `kill(inlabels, functions, allbut(foo, bar))`.


`kill(labels)` entfernt alle Zuweisungen an Eingabe-, Ausgabe- und 
Zwischenmarken.  `kill(inlabels)` entfernt nur die Zuweisungen an 
Eingabemarken, die mit dem aktuellen Wert von `inchar` beginnen.
Entsprechend entfernt `kill(outlabels)` die Zuweisungen an die 
Ausgabemarken, die mit dem aktuellen Wert von `outchar` beginnen und
`kill(linelabels)` die Zuweisungen an die Zwischenmarken, die mit dem
aktuellen Wert von `linechar` beginnen.


`kill(n)`, wobei *n* eine ganze Zahl ist, entfernt die 
Zuweisungen an die *n* letzten Eingabe- und Ausgabemarken.
`kill([m, n])` entfernt die Zuweisungen an die Eingabe- und 
Ausgabemarken mit den Nummern von *m* bis *n*.


`kill(infolist)`, wobei *infolist* eine Informationsliste wie zum
Beispiel `values`, `functions` oder `arrays` ist, entfernt
die Zuweisungen an allen Eintragen der Liste *infolist*.  Siehe auch
`infolists`.


`kill(all)` entfernt die Zuweisungen an die Eintrage in samtlichen
Informationslisten.  `kill(all)` setzt keine Optionsvariablen auf ihre
Standardwerte zuruck.  Siehe die Funktion `reset`, um
Optionsvariablen auf ihre Standwerte zuruckzusetzen.


`kill(allbut(a_1, ..., a_n))` entfernt alle Zuweisungen bis 
auf Zuweisungen an die Variablen *a_1*, ..., *a_n*.
`kill(allbut(infolist))` entfernt alle Zuweisungen bis auf denen in 
der Informationsliste *infolist*.


`kill(symbol)` entfernt samtliche Zuweisungen und Eigenschaften
des Symbols *symbol*.  Im Gegensatz dazu entfernen
`remvalue`, `remfunction`, `remarray` und
`remrule` jeweils eine spezielle Eigenschaft eines Symbols.


`kill` wertet die Argumente nicht aus.  Der
Quote-Quote-Operator `''` kann die Auswertung erzwingen.
`kill` gibt immer `done` zuruck.

See also: `inchar`, `outchar`, `linechar`, `values`, `functions`, `arrays`, `infolists`, `reset`, `remvalue`, `remfunction`, `remarray`, `remrule`.

<!-- category: Other -->
<!-- keywords: labels -->
<!-- signatures: labels(symbol) -->
### Function: labels (symbol)

Die Funktion `labels` gibt eine Liste der Eingabe-, Ausgabe- und 
Zwischenmarken zuruck, die mit dem Argument *symbol* beginnen.
Typischerweise ist *symbol* der Wert von
`inchar`, `outchar` oder `linechar`.  Dabei kann das
Prozentzeichen fortgelassen werden.  So haben zum Beispiel die Kommandos
`labels(i)` und `labels(%i)` dasselbe Ergebnis.


Wenn keine Marke mit *symbol* beginnt, gibt `labels` eine leere Liste 
zuruck.


Die Funktion `labels` wertet das Argument nicht aus.  Mit dem
Quote-Quote-Operator `''` kann die Auswertung erzwungen
werden.  Zum Beispiel gibt das Kommando `labels(''inchar)` die Marken
zuruck, die mit dem aktuellen Buchstaben fur die Eingabemarken beginnen.


Die Systemvariable `labels` ist eine Informationsliste, die die Eingabe-, 
Ausgabe- und Zwischenmarken enthalt.  In der Liste sind auch die Marken
enthalten, die vor einer Anderung von `inchar`, `outchar` oder 
`linechar` erzeugt wurden.


Standardmaßig zeigt Maxima das Ergebnis jeder Eingabe an, wobei dem
Ergebnis eine Ausgabemarke hinzugefugt wird.  Die Anzeige der Ausgabe wird
durch die Eingabe eines abschließenden `$` (Dollarzeichen) statt eines
`;` (Semikolon) unterdruckt.  Dabei wird eine Ausgabemarke erzeugt und
das Ergebnis zugewiesen, jedoch nicht angezeigt.  Die Marke kann aber in der 
gleichen Art und Weise wie bei angezeigten Ausgabemarken referenziert werden.
Siehe auch `%`, `%%` und `%th`.


Einige Funktionen erzeugen Zwischenmarken.  Die Optionsvariable 
`programmode` kontrolliert, ob zum Beispiel `solve` und einige andere
Funktionen Zwischenmarken erzeugen, anstatt eine Liste von Ausdrucken 
zuruckzugeben.  Andere Funktionen wie zum Beispiel `ldisplay` erzeugen
stets Zwischenmarken.


Siehe auch `infolists`.

See also: `inchar`, `outchar`, `linechar`, `$`, `;`, `%`, `%%`, `%th`, `programmode`, `solve`, `ldisplay`, `infolists`.

<!-- category: Other -->
<!-- keywords: ldisp -->
<!-- signatures: ldisp(expr_1, ..., expr_n) -->
### Function: ldisp (expr_1, ..., expr_n)

Die Ausdrucke *expr_1*, ..., *expr_n* werden auf der Konsole 
ausgegeben.  Dabei wird jedem Ausdruck eine Zwischenmarke zugewiesen.  Die Liste
der Zwischenmarken wird als Ergebnis zuruckgegeben.


Siehe auch die Funktionen `disp`, `display` und `ldisplay`.



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)

(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisp (e, f);
                                   3
(%t3)                       (b + a)

                     3        2      2      3
(%t4)               b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                   3
(%o4)                       (b + a)
(%i5) %t4;
                     3        2      2      3
(%o5)               b  + 3 a b  + 3 a  b + a
```

See also: `disp`, `display`, `ldisplay`.

<!-- category: Other -->
<!-- keywords: ldisplay -->
<!-- signatures: ldisplay(expr_1, ..., expr_n) -->
### Function: ldisplay (expr_1, ..., expr_n)

Die Ausdrucke *expr_1*, ..., *expr_n* werden als eine Gleichung
der Form `lhs = rhs` ausgegeben.  `lhs` ist eines der Argumente der
Funktion `ldisplay` und `rhs` ist der Wert oder das Ergebnis des
Argumentes.  Im Unterschied zur Funktion `display` wird jeder Gleichung
eine Zwischenmarke zugewiesen, die als Liste zuruckgegeben werden.


Siehe auch `display`, `disp` und `ldisp`.


Beispiele:



```maxima
(%i1) e: (a+b)^3;
                                   3
(%o1)                       (b + a)
(%i2) f: expand (e);
                     3        2      2      3
(%o2)               b  + 3 a b  + 3 a  b + a
(%i3) ldisplay (e, f);
                                     3
(%t3)                     e = (b + a)

                       3        2      2      3
(%t4)             f = b  + 3 a b  + 3 a  b + a

(%o4)                      [%t3, %t4]
(%i4) %t3;
                                     3
(%o4)                     e = (b + a)
(%i5) %t4;
                       3        2      2      3
(%o5)             f = b  + 3 a b  + 3 a  b + a
```

See also: `display`, `disp`, `ldisp`.

<!-- category: Other -->
<!-- keywords: leftjust -->
<!-- signatures: leftjust -->
### Variable: leftjust

Standardwert: `false`


Hat die Optionsvariable `leftjust` den Wert `true`, werden Formeln
linksbundig und nicht zentriert ausgegeben.


Siehe auch die Optionsvariable `display2d`, um zwischen der 
1D- und 2D-Anzeige umzuschalten.


Beispiel:



```maxima
(%i1) expand((x+1)^3);
                        3      2
(%o1)                  x  + 3 x  + 3 x + 1
(%i2) leftjust:true$
(%i3) expand((x+1)^3);
       3      2
(%o3) x  + 3 x  + 3 x + 1
```

See also: `display2d`.

<!-- category: Other -->
<!-- keywords: linechar -->
<!-- signatures: linechar -->
### Variable: linechar

Standardwert: `%t`


Die Optionsvariable `linechar` enthalt den Prafix der Zwischenmarken.
Maxima generiert die Zwischenmarken automatisch aus `linechar`.


Der Optionsvariablen `linechar` kann eine Zeichenkette oder ein Symbol 
zugewiesen werden, die auch mehr als ein Zeichen haben konnen.  Da Maxima 
intern nur das erste Zeichen berucksichtigt, sollten sich die Prafixe 
`inchar`, `outchar` und `linechar` im ersten Zeichen
voneinander unterscheiden.  Ansonsten funktionieren einige Kommandos wie
`kill(inlabels)` nicht wie erwartet.


Die Ausgabe von Zwischenmarken kann mit verschiedenen Optionsvariablen 
kontrolliert werden.  Siehe `programmode` und `labels`.

See also: `inchar`, `outchar`, `programmode`, `labels`.

<!-- category: Other -->
<!-- keywords: linel -->
<!-- signatures: linel -->
### Variable: linel

Standardwert: `79`


Die Optionsvariable `linel` enthalt die Anzahl der Zeichen einer Zeile
der Ausgabe.  `linel` konnen beliebige positive ganze Zahlen zugewiesen
werden, wobei sehr kleine oder große Werte unpraktisch sein konnen.  Text,
der von internen Funktionen ausgegeben wird, wie Fehlermeldungen oder Ausgaben
der Hilfe, werden von `linel` nicht beeinflusst.

<!-- category: Other -->
<!-- keywords: linenum -->
<!-- signatures: linenum -->
### Variable: linenum

Enthalt die Zeilennummer der aktuellen Ein- und Ausgabemarken.  Die
Zeilennummer wird von Maxima automatisch erhoht.  Siehe auch
`labels`, `inchar` und `outchar`.

See also: `labels`, `inchar`, `outchar`.

<!-- category: Other -->
<!-- keywords: lispdisp -->
<!-- signatures: lispdisp -->
### Variable: lispdisp

Standardwert: `false`


Hat die Optionsvariable `lispdisp` den Wert `true`, werden 
Lisp-Symbole mit einem vorangestelltem Fragezeichen `?` angezeigt.


Beispiele:



```maxima
(%i1) lispdisp: false$
(%i2) ?foo + ?bar;
(%o2)                       foo + bar
(%i3) lispdisp: true$
(%i4) ?foo + ?bar;
(%o4)                      ?foo + ?bar
```

<!-- category: Other -->
<!-- keywords: myoptions -->
<!-- signatures: myoptions -->
### Variable: myoptions

`myoptions` ist eine Informationsliste, die die Optionsvariablen enthalt,
die vom Nutzer wahrend einer Sitzung geandert wurden.  Die Variable 
verbleibt in der Liste, auch wenn sie wieder auf den Standardwert
zuruckgesetzt wird.

<!-- category: Other -->
<!-- keywords: negsumdispflag -->
<!-- signatures: negsumdispflag -->
### Variable: negsumdispflag

Standardwert: `true`


Hat `negsumdispflag` den Wert `true`, wird eine Differenz mit zwei
Argumenten `x - y` als `x - y` und nicht als `-y + x` angezeigt.
Hat `negsumdispflag` den Wert `false`, wird die Differenz als
`-y + x` angezeigt.

<!-- category: Other -->
<!-- keywords: nolabels -->
<!-- signatures: nolabels -->
### Variable: nolabels

Standardwert: `false`


Hat `nolabels` den Wert `true`, werden die Eingabe- und Ausgabemarken 
zwar angezeigt, ihnen werden aber keine Eingaben und Ergebnisse zugewiesen und
sie werden nicht der Informationsliste `labels` hinzugefugt.  Andernfalls
werden den Marken die Eingabe und die Ergebnisse zugewiesen und in die
Informationsliste `labels` eingetragen.


Zwischenmarken `%t` werden durch `nolabels` nicht beeinflusst.  Den
Marken werden unabhangig vom Wert, den `nolabels` hat, Zwischenergebnisse
zugewiesen und sie werden in die Informationsliste `labels` eingetragen.


Siehe auch `labels`.

See also: `labels`.

<!-- category: Other -->
<!-- keywords: obase -->
<!-- signatures: obase -->
### Variable: obase

Standardwert: `10`


`obase` enthalt die Basis fur ganze Zahlen fur die Ausgabe von
Maxima.  `obase` kann eine ganze Zahl zwischen 2 und einschließlich 36
zugewiesen werden.  Ist `obase` großer als 10, werden die Zahlen 0 
bis 9 und die Buchstaben A, B, C, ... fur die Darstellung der Zahl in der 
Basis `obase` herangezogen.  Große und kleine Buchstaben werden nicht 
unterschieden.  Die erste Stelle ist immer eine Ziffer.


Siehe auch `ibase`.


Beispiele:



```maxima
(%i1) obase : 2;
(%o1)                          10
(%i2) 2^8 - 1;
(%o10)                      11111111
(%i3) obase : 8;
(%o3)                          10
(%i4) 8^8 - 1;
(%o4)                       77777777
(%i5) obase : 16;
(%o5)                          10
(%i6) 16^8 - 1;
(%o6)                       0FFFFFFFF
(%i7) obase : 36;
(%o7)                          10
(%i8) 36^8 - 1;
(%o8)                       0ZZZZZZZZ
```

See also: `ibase`.

<!-- category: Other -->
<!-- keywords: optionset -->
<!-- signatures: optionset -->
### Variable: optionset

Standardwert: `false`


Hat `optionset` den Wert `true`, gibt Maxima eine Meldung aus, wenn 
einer Optionsvariablen ein Wert zugewiesen wird.


Beispiel:



```maxima
(%i1) optionset:true;
assignment: assigning to option optionset
(%o1)                         true
(%i2) gamma_expand:true;
assignment: assigning to option gamma_expand
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: outchar -->
<!-- signatures: outchar -->
### Variable: outchar

Standardwert: `%o`


Die Optionsvariable `outchar` enthalt den Prafix der Ausgabemarken.
Maxima generiert die Ausgabemarken automatisch aus `outchar` und 
`linenum`.


Der Optionsvariablen `outchar` kann eine Zeichenkette oder ein Symbol 
zugewiesen werden, die auch mehr als ein Zeichen haben konnen.  Da Maxima 
intern nur das erste Zeichen berucksichtigt, sollten sich die Prafixe 
`inchar`, `outchar` und `linechar` im ersten Zeichen
voneinander unterscheiden.  Ansonsten funktionieren einige Kommandos wie
`kill(inlabels)` nicht wie erwartet.


Siehe auch `labels`.


Beispiele:



```maxima
(%i1) outchar: "output";
(output1)                    output
(%i2) expand((a+b)^3);
                     3        2      2      3
(output2)           b  + 3 a b  + 3 a  b + a
(%i3)
```

See also: `linenum`, `inchar`, `linechar`, `labels`.

<!-- category: Other -->
<!-- keywords: pfeformat -->
<!-- signatures: pfeformat -->
### Variable: pfeformat

Standardwert: `false`


Hat die Optionsvariable `pfeformat` den Wert `true`, werden Bruche
mit ganzen Zahlen auf einer Zeile mit dem Zeichen `/` dargestellt.  Ist
der Nenner eine ganze Zahl, wird dieser als `1/n` vor den Ausdruck 
gestellt.


Beispiele:



```maxima
(%i1) pfeformat: false$
(%i2) 2^16/7^3;
                              65536
(%o2)                         -----
                               343
(%i3) (a+b)/8;
                              b + a
(%o3)                         -----
                                8
(%i4) pfeformat: true$ 
(%i5) 2^16/7^3;
(%o5)                       65536/343
(%i6) (a+b)/8;
(%o6)                      1/8 (b + a)
```

<!-- category: Other -->
<!-- keywords: playback -->
<!-- signatures: playback(), playback(n), playback([m, n]), playback([m]), playback(input), playback(slow), playback(time), playback(grind) -->
### Function: playback ()

Zeigt Eingaben, Ergebnisse und Zwischenergebnisse an, ohne diese neu zu 
berechnen.  `playback` zeigt nur die Eingaben und Ergebnisse an, die Marken
zugewiesen wurden.  Andere Ausgaben, wie zum Beispiel durch
`print`, `describe` oder Fehlermeldungen, werden nicht angezeigt.
Siehe auch `labels`.


`playback()` zeigt samtliche Eingaben und Ergebnisse an, die bis dahin
erzeugt wurden.  Ein Ergebnis wird auch dann angezeigt, wenn die Ausgabe mit 
`$` unterdruckt war.


`playback(n)` zeigt die letzten *n* Ausdrucke an.  Jeder 
Eingabe-, Ausgabe- und Zwischenausdruck zahlt dabei als ein Ausdruck.
`playback([m, n])` zeigt die Eingabe-, Ausgabe- und 
Zwischenausdrucke mit den Zahlen von *m* bis einschließlich *n* 
an.  `playback([m])` ist aquivalent zu `playback([m, m])`.  Die Ausgabe ist ein Paar von Ein- und Ausgabeausdrucken.


`playback(input)` zeigt samtliche Eingabeausdrucke an, die bis dahin 
erzeugt wurden.


`playback(slow)` macht nach jeder Ausgabe eine Pause und wartet auf eine
Eingabe.  Dieses Verhalten ist vergleichbar mit der Funktion `demo`.


`playback(time)` zeigt fur jeden Ausdruck die fur die Berechnung
benotigte Zeit an.


`playback(grind)` zeigt die Eingabeausdrucke in dem gleichen Format an,
wie die Funktion `grind`.  Ausgabeausdrucke werden von der Option
`grind` nicht beeinflusst.  Siehe auch `grind`.


Die Argumente konnen kombiniert werden, wie zum Beispiel im folgenden
Kommando `playback([5, 10], grind, time, slow)`.


`playback` wertet die Argumente nicht aus.  `playback` gibt stets 
`done` zuruck.

See also: `print`, `describe`, `labels`, `$`, `demo`, `grind`.

<!-- category: Other -->
<!-- keywords: powerdisp -->
<!-- signatures: powerdisp -->
### Variable: powerdisp

Standardwert: `false`


Hat `powerdisp` den Wert `true`, werden die Terme einer Summe mit
steigender Potenz angezeigt.  Der Standardwert ist `false` und die Terme
werden mit fallender Potenz angezeigt.


Beispiele:



```maxima
(%i1) powerdisp:true;
(%o1)                         true
(%i2) x^2+x^3+x^4;
                           2    3    4
(%o2)                     x  + x  + x
(%i3) powerdisp:false;
(%o3)                         false
(%i4) x^2+x^3+x^4;
                           4    3    2
(%o4)                     x  + x  + x
```

<!-- category: Other -->
<!-- keywords: print -->
<!-- signatures: print(expr_1, ..., expr_n) -->
### Function: print (expr_1, ..., expr_n)

Wertet die Argumente *expr_1*, ..., *expr_n* nacheinander von links 
nach rechts aus und zeigt die Ergebnisse an.  `print` gibt das Ergebnis des 
letzten Arguments als Ergebnis zuruck.  `print` erzeugt keine 
Zwischenmarken.


Siehe auch `display`, `disp`, `ldisplay` und 
`ldisp`.  Siehe `printfile`, um den Inhalt einer Datei 
anzuzeigen.


Beispiele:



```maxima
(%i1) r: print ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is",
      radcan (log (a^10/b)))$
            3        2      2      3
(a+b)^3 is b  + 3 a b  + 3 a  b + a  log (a^10/b) is 

                                              10 log(a) - log(b) 
(%i2) r;
(%o2)                  10 log(a) - log(b)
(%i3) disp ("(a+b)^3 is", expand ((a+b)^3), "log (a^10/b) is",
      radcan (log (a^10/b)))$
                           (a+b)^3 is


                     3        2      2      3
                    b  + 3 a b  + 3 a  b + a


                         log (a^10/b) is

                       10 log(a) - log(b)
```

See also: `display`, `disp`, `ldisplay`, `ldisp`, `printfile`.

<!-- category: Other -->
<!-- keywords: prompt -->
<!-- signatures: prompt -->
### Variable: prompt

Standardwert: `_`


Die Optionsvariable `prompt` enthalt das Zeichen fur die
Eingabeaufforderung der Funktionen `demo` und `playback` sowie
nach einer Unterbrechung, wie zum Beispiel durch das Kommando `break`.

See also: `demo`, `playback`, `break`.

<!-- category: Other -->
<!-- keywords: quit -->
<!-- signatures: quit([returnwert]) -->
### Function: quit ([returnwert])

Die Funktion `quit()` beendet eine Maxima-Sitzung.
Die Funktion muss als `quit();` oder `quit()$`, nicht `quit` allein
aufgerufen werden.
`quit` kann einen Returnwert retournieren, wenn der Lisp-Compiler und das
Betriebssystem Returnwerte unterstützt.
Standardmässig wird der Wert 0 retourniert (meist als kein Fehler interpretiert).
`quit(1)` könnte der Shell daher einen Fehler anzeigen.
Das kann für Skripte nützlich sein, wo Maxima dadurch anzeigen kann,
dass Maxima irgendwas nicht berechnen konnte oder ein sonstiger Fehler
aufgetreten ist.


Mit der Tastatureingabe `control-c` oder `Strg-c` kann in der Konsole
die Verarbeitung abgebrochen werden.  Stan­dard­maßig wird die
Maxima-Sitzung fortgesetzt.  Hat die globale Lisp-Variable
`*debugger-hook*` den Wert `nil`, wird der Lisp-Debugger gestartet.
Siehe `Fehlersuche`.

See also: `Fehlersuche`.

<!-- category: Other -->
<!-- keywords: read -->
<!-- signatures: read(expr_1, ..., expr_n) -->
### Function: read (expr_1, ..., expr_n)

Gibt die Ausdrucke *expr_1*, ... *expr_n* auf der Konsole aus, 
liest sodann einen Ausdruck von der Konsole ein und wertet diesen aus.  Die 
Eingabe des Ausdrucks wird mit den Zeichen `;` oder `$` beendet.


Siehe auch `readonly`.


Beispiele:



```maxima
(%i1) foo: 42$ 
(%i2) foo: read ("foo is", foo, " -- enter new value.")$
foo is 42  -- enter new value.
(a+b)^3;
(%i3) foo;
                                     3
(%o3)                         (b + a)
```

See also: `;`, `$`, `readonly`.

<!-- category: Other -->
<!-- keywords: readonly -->
<!-- signatures: readonly(expr_1, ..., expr_n) -->
### Function: readonly (expr_1, ..., expr_n)

Gibt die Ausdrucke *expr_1*, ... *expr_n* auf der Konsole aus, 
liest sodann einen Ausdruck von der Konsole ein und gibt den eingelesenen 
Ausdruck zuruck ohne diesen auszuwerten.  Die Eingabe des Ausdrucks wird mit 
den Zeichen `;` oder `$` beendet.


Siehe auch `read`.


Beispiele:



```maxima
(%i1) aa: 7$
(%i2) foo: readonly ("Enter an expression:");
Enter an expression: 
2^aa;
                                  aa
(%o2)                            2
(%i3) foo: read ("Enter an expression:");
Enter an expression: 
2^aa;
(%o3)                            128
```

See also: `;`, `$`, `read`.

<!-- category: Other -->
<!-- keywords: reset -->
<!-- signatures: reset() -->
### Function: reset ()

`reset()` setzt globale Maxima- und Lisp-Variablen und Optionen auf ihre 
Standardwerte zuruck.  Maxima legt eine interne Liste mit den Standardwerten 
von globalen Variablen an.  Alle Variablen, die in dieser Liste enthalten sind, 
werden auf ihre Standardwerte zuruckgesetzt.  Nicht alle globalen Variablen 
sind mit ihren Standwerten in diese Liste eingetragen.  Daher kann `reset` 
die Anfangswerte stets nur unvollstandig wiederherstellen.


`reset(arg_1, ..., arg_n)` setzt die Variablen *arg_1*, ..., 
*arg_n* auf ihren Standardwert zuruck.


`reset` gibt eine Liste mit den Variablen zuruck, die auf ihren
Standardwert zuruckgesetzt wurden.  Ist die Liste leer, wurden keine Variablen
zuruckgesetzt.


Siehe auch `reset_verbosely`.

See also: `reset_verbosely`.

<!-- category: Other -->
<!-- keywords: reset_verbosely -->
<!-- signatures: reset_verbosely(), reset_verbosely(arg_1, ..., arg_n) -->
### Function: reset_verbosely ()

Entspricht der Funktion `reset`.  Im Unterschied zu `reset` wird zu
jeder Variable, die zuruckgesetzt wird, zusatzlich der Standardwert
angezeigt.


Siehe `reset`.

See also: `reset`.

<!-- category: Other -->
<!-- keywords: showtime -->
<!-- signatures: showtime -->
### Variable: showtime

Standardwert: `false`


Hat `showtime` den Wert `true`, werden die interne Rechenzeit und die 
gesamte verstrichene Zeit zu jeder Ausgabe angezeigt.


Die Rechenzeit wird unabhangig vom Wert der Optionsvariablen `showtime`
nach jeder Auswertung eines Ausdruckes in den Ausgabemarken abgespeichert.
Daher konnen die Funktionen `time` und `playback` die Rechenzeit
auch dann anzeigen, wenn `showtime` den Wert `false` hat.


Siehe auch `timer`.

See also: `time`, `playback`, `timer`.

<!-- category: Other -->
<!-- keywords: sqrtdispflag -->
<!-- signatures: sqrtdispflag -->
### Variable: sqrtdispflag

Standardwert: `true`


Hat die Optionsvariable den Wert `false`, wird die Wurzelfunktion als
Exponentiation mit dem Exponenten `1/2` angezeigt.

<!-- category: Other -->
<!-- keywords: stardisp -->
<!-- signatures: stardisp -->
### Variable: stardisp

Standardwert: `false`


Hat die Optionsvariable `stardisp` den Wert `true`, wird die 
Multiplikation mit einem Stern `*` angezeigt.

<!-- category: Other -->
<!-- keywords: to_lisp -->
<!-- signatures: to_lisp() -->
### Function: to_lisp ()

Wechselt zu einer Lisp-Sitzung.  `(to-maxima)` wechselt von der 
Lisp-Sitzung zuruck in die Maxima-Sitzung.


Beispiel:


Definiere eine Funktion und wechsle zu Lisp.  Die Definition wird von der 
Eigenschaftsliste gelesen.  Dann wird die Definition der Funktion geholt, 
faktorisiert und in der Variablen `$result` gespeichert.  Die Variable 
kann nach der Ruckkehr in Maxima genutzt werden.



```maxima
(%i1) f(x):=x^2+x;
                                  2
(%o1)                    f(x) := x  + x
(%i2) to_lisp();
Type (to-maxima) to restart, ($quit) to quit Maxima.
MAXIMA> (symbol-plist '$f)
(MPROPS (NIL MEXPR ((LAMBDA) ((MLIST) $X) 
                             ((MPLUS) ((MEXPT) $X 2) $X))))
MAXIMA> (setq $result ($factor (caddr (mget '$f 'mexpr))))
((MTIMES SIMP FACTORED) $X ((MPLUS SIMP IRREDUCIBLE) 1 $X))
MAXIMA> (to-maxima)
Returning to Maxima
(%o2)                         true
(%i3) result;
(%o3)                       x (x + 1)
```

<!-- category: Other -->
<!-- keywords: ttyoff -->
<!-- signatures: ttyoff -->
### Variable: ttyoff

Standardwert: `false`

 

Hat die Optionsvariable `ttyoff` den Wert `true`, werden Ergebnisse
nicht angezeigt.  Die Ergebnisse werden weiter berechnet und sie werden 
Marken zugewiesen.  Siehe `labels`.


Textausgaben von Funktionen, wie Fehlermeldungen und Ausgaben der Hilfe mit
`describe` werden nicht beeinflusst.

See also: `labels`, `describe`.

<!-- category: Other -->
<!-- keywords: values -->
<!-- signatures: values -->
### Variable: values

Anfangswert: `[]`


`values` ist eine Informationsliste, die die Variablen enthalt, die vom
Nutzer mit den Operatoren `:` oder `::` einen Wert erhalten haben.
Wird der Wert einer Variablen mit den Kommandos `kill`,
`remove` oder `remvalue` entfernt, wird die Variable von der Liste
`values` entfernt.


Siehe auch `functions` fur die Informationsliste mit den vom Nutzer 
definierten Funktionen sowie `infolists`.


Beispiele:









```maxima
(%i1) [a:99, b::a-90, c:a-b, d, f(x):= x^2];
                                           2
(%o1)              [99, 9, 90, d, f(x) := x ]
(%i2) values;
(%o2)                       [a, b, c]
(%i3) [kill(a), remove(b,value), remvalue(c)];
(%o3)                   [done, done, [c]]
(%i4) values;
(%o4)                          []
```

See also: `:`, `::`, `kill`, `remove`, `remvalue`, `functions`, `infolists`.

