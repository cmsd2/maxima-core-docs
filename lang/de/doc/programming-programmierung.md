## Programmierung

<!-- category: Programming -->
<!-- keywords: backtrace -->
<!-- signatures: backtrace(), backtrace(n) -->
### Function: backtrace ()

Gibt den Aufruf-Stack der Funktion zuruck, die ausgefuhrt wird.


Das Kommando `backtrace()` zeigt den gesamten Stack.
`backtrace(n)` zeigt die letzten *n* Funktionen
einschließlich der Funktion, die ausgefuhrt wird.


`backtrace` kann in einer Batch-Datei, die zum Beispiel mit der Funktion
`batch` geladen wird, in einer Funktion oder von einer Kommandozeile
aufgerufen werden.


Beispiele:


`backtrace()` gibt den gesamten Stack aus.



```maxima
(%i1) h(x) := g(x/7)$
(%i2) g(x) := f(x-11)$
(%i3) f(x) := e(x^2)$
(%i4) e(x) := (backtrace(), 2*x + 13)$
(%i5) h(10);
#0: e(x=4489/49)
#1: f(x=-67/7)
#2: g(x=10/7)
#3: h(x=10)
                              9615
(%o5)                         ----
                               49
```


`backtrace(n)` gibt die letzten *n* Funktionen aus.



```maxima
(%i1) h(x) := (backtrace(1), g(x/7))$
(%i2) g(x) := (backtrace(1), f(x-11))$
(%i3) f(x) := (backtrace(1), e(x^2))$
(%i4) e(x) := (backtrace(1), 2*x + 13)$
(%i5) h(10);
#0: h(x=10)
#0: g(x=10/7)
#0: f(x=-67/7)
#0: e(x=4489/49)

                              9615
(%o5)                         ----
                               49
```

See also: `batch`.

<!-- category: Programming -->
<!-- keywords: block -->
<!-- signatures: block([v_1, ..., v_m], expr_1, ..., expr_n), block(expr_1, ..., expr_n) -->
### Function: block ([v_1, ..., v_m], expr_1, ..., expr_n)

Mit der Anweisung `block` werden Ausdrucke in einer lokalen Umgebung
zusammengefasst.  `block` wertet die Argument *expr_1*, *expr_2*,
..., *expr_n* nacheinander aus und gibt das Ergebnis des letzten
ausgewerteten Ausdrucks zuruck.  Die Liste `[v_1, ..., v_m]` am Anfang
der `block`-Anweisung bezeichnet Variablen, die innerhalb der
`block`-Anweisung lokal sind.  Alle anderen Variablen, die in einem Block
verwendet werden, beziehen sich auf globale Variablen, die außerhalb des Block
definiert sind.  Dies kann ein weiterer Block oder die globale Maxima-Umgebung
sein.  `block` sichert die aktuellen Werte der Variablen *v_1*, 
..., *v_m*.  Wird `block` verlassen, werden diese Werte
wiederhergestellt.


Die Deklaration `local(v_1, ..., v_m)` innerhalb der
`block`-Anweisung sichert nicht nur die Werte, sondern auch die
Eigenschaften der Variablen wie sie zum Beispiel mit den Funktionen
`declare` oder `depends` definiert werden.  Erhalten die mit
`local` deklarierten Variablen innerhalb der `block`-Anweisung
Eigenschaften, wirken sich diese nur lokal aus.  Beim Verlassen der
`block`-Anweisung werden die globalen Eigenschaften wiederhergestellt.
Siehe auch `local`.


Die `block`-Anweisung kann verschachtelt werden.  Jeder Block kann
eigene lokale Variablen definieren.  Diese sind global zu jedem anderen Block
der sich innerhalb des Blockes befindet.  Ein Variable die nicht als lokal
definiert ist, hat den globalen Wert eines umgebenden Blocks oder den Wert der
globalen Maxima-Umgebung.


Der Ruckgabewert eines Blocks ist der Wert des letzten Ausdrucks oder der 
Wert, der mit den `return`-Anweisung zuruckgegeben wird.  Mit der 
`go`-Anweisung kann innerhalb eines Blocks zu einer Marke gesprungen 
werden.  Weiterhin kann mit der `throw`-Anweisung ein nicht-lokaler
Rucksprung zu einer entsprechenden `catch`-Anweisung erfolgen.


Blocke erscheinen typischerweise auf der rechten Seite einer 
Funktionsdefinitionen.  Sie konnen aber auch an anderen Stellen verwendet
werden.


Beispiel:


Das Beispiel zeigt eine einfache Implementation des Newton-Algorithmus.  Der
Block definiert die lokalen Variablen `xn`, `s` und *numer*.
`numer` ist eine Optionsvariable, die im Block einen lokalen Wert erhalt.
Im Block ist das Tag `loop` definiert.  Zu diesem Tag wird mit der
Anweisung `go(loop)` gesprungen.  Der Block und damit die Funktion wird
mit der Anweisung `return(xn)` verlassen.  Der Wert der Variablen `xn`
ist das Ergebnis der Funktion `newton`.



```maxima
newton(exp,var,x0,eps):=
   block([xn,s,numer],
      numer:true,
      s:diff(exp,var),
      xn:x0,
   loop,
      if abs(subst(xn,var,exp))<eps then return(xn),
      xn:xn-subst(xn,var,exp)/subst(xn,var,s),
      go(loop) )$
```

See also: `declare`, `depends`, `local`, `throw`, `catch`, `numer`.

<!-- category: Programming -->
<!-- keywords: break -->
<!-- signatures: break(expr_1, ..., expr_n) -->
### Function: break (expr_1, ..., expr_n)

Wertet die Ausdrucke *expr_1*, ..., *expr_n* aus, zeigt die 
Ergebnisse an und fuhrt dann eine Unterbrechung aus.  Mit dem Kommando 
`exit;` wird Maxima fortgesetzt.  Siehe das Kapitel


Beispiel:


Der Variablen `a` wird der Wert 2 zugewiesen.  Dann wird die Unterbrechung
ausgefuhrt.  Mit dem Kommando `exit;` wird Maxima fortgesetzt.



```maxima
(%i1) break(a:2);
2 

Entering a Maxima break point. Type 'exit;' to resume.
_a;
2
_exit;
(%o1)                           2
```

<!-- category: Programming -->
<!-- keywords: catch -->
<!-- signatures: catch(expr_1, ..., expr_n) -->
### Function: catch (expr_1, ..., expr_n)

Wertet die Ausdrucke *expr_1*, ..., *expr_n* nacheinander aus.
Wertet irgendeiner der Ausdrucke zu `throw(arg)` aus, dann ist das 
Ergebnis der Wert von `throw(arg)` und es werden keine weiteren Ausdrucke
ausgewertet.  Diese nicht-lokale Ruckgabe kehrt zu dem nachsten `catch`
in einer beliebigen Verschachtelungstiefe zuruck.  Wird kein `catch` 
gefunden gibt Maxima eine Fehlermeldung aus.





Fuhrt die Auswertung der Argumente nicht zu einem `throw`, dann ist
die Ruckgabe das Ergebnis des letzten Ausdrucks `expr_n`.


Beispiel:






Die Funktion `g` gibt eine Liste mit den Werten des Lambda-Ausdrucks 
zuruck.  Tritt ein negativer Wert auf, bricht die Funktion ab, in diesem 
Beispiel mit `throw(-3)`.



```maxima
(%i1) lambda ([x], if x < 0 then throw(x) else f(x))$
(%i2) g(l) := catch (map (''%, l))$
(%i3) g ([1, 2, 3, 7]);
(%o3)               [f(1), f(2), f(3), f(7)]
(%i4) g ([1, 2, -3, 7]);
(%o4)                          - 3
```

<!-- category: Programming -->
<!-- keywords: do -->
<!-- signatures: do -->
### Function: do

Die `do`-Anweisung erlaubt die Definition von Iterationen.  Aufgrund der
großen Allgemeinheit der `do`-Anweisung folgt die Beschreibung in zwei
Teilen.  Zunachst werden die bekannteren Formen beschrieben, wie sie auch in 
anderen Programmiersprachen vorhanden sind.  Dann folgen die weiteren 
Moglichkeiten.





Es gibt drei Varianten der `do`-Anweisung, die sich nur durch die
Abbruchbedingung voneinander unterscheiden.  Diese sind:



```maxima
for variable: initial_value step increment
      thru limit do body


for variable: initial_value step increment
      while condition do body


for variable: initial_value step increment
      unless condition do body
```


   






*initial_value*, *increment*, *limit* und *body* konnen 
beliebige Ausdrucke sein.  Ist das Inkrement 1, kann `step` entfallen.













Die Ausfuhrung der `do`-Anweisung beginnt mit der Zuweisung von
`initial_value` an die Kontrollvariable *variable*.  Dann folgen die 
Schritte: (1) Hat die Kontrollvariable den Wert einer `thru`-Anweisung
uberschritten oder hat die Bedingung einer `unless`-Anweisung den Wert
`true` oder hat die Bedingung einer `while`-Anweisung den Wert
`false`, dann endet die Ausfuhrung der `do`-Anweisung.  (2) Die
Ausdrucke in *body* werden ausgewertet.  (3) Das Inkrement wird zu der
Kontrollvariablen hinzuaddiert.  Die Schritte (1) bis (3) werden solange 
ausgefuhrt, bis eine der Bedingungen fur die Beendigung der 
`do`-Anweisung zutrifft.












Im Allgemeinen ist der `thru`-Test erfullt, wenn die Kontrollvariable 
großer als *limit* ist, falls *increment* nicht negativ ist.  Oder 
wenn die Kontrollvariable kleiner als `limit` ist, fur den Fall, dass das
Inkrement negativ ist.  *increment* und *limit* konnen Ausdrucke 
sein, sofern die Bedingung zum Abbruch der `do`-Anweisung ausgewertet 
werden kann.  Soll `increment` zu einem negativen Wert auswerten und kann 
dies jedoch bei Eintritt in die Schleife von Maxima nicht festgestellt werden, 
so wird das Inkrement als positiv angenommen.  Dies kann dazu fuhren, dass die
Schleife nicht korrekt ausgefuhrt wird.









*limit*, *increment* und die Bedingung fur den Abbruch der Schleife 
werden fur jeden Durchgang durch die Schleife ausgewertet.  Andern diese 
ihren Wert nicht, kann es daher effizienter sein, die Werte diese Ausdrucke 
vor Eintritt in die Schleife zu berechnen und in Variablen abzulegen, die 
anstatt der Ausdrucke in der Schleife verwendet werden.










Die `do`-Anweisung hat den Ruckgabewert `done`.  Um einen anderen
Wert zu­ruck­zu­ge­ben, kann die `return`-Anweisung innerhalb von 
`body` genutzt werden.  Befindet sich die `do`-Anweisung innerhalb 
eines Blockes, so wird dieser nicht mit einer `return`-Anweisung verlassen,
die sich innerhalb der `do`-Anweisung befindet.  Auch kann nicht mit der
`go`-Anweisung in einen umgebenen Block gesprungen werden.







Die Kontrollvariable ist immer lokal zur `do`-Anweisung.  Nach dem
Verlassen der `do`-Anweisung kann auf die Kontrollvariable nicht mehr 
zugegriffen werden.



```maxima
(%i1) for a:-3 thru 26 step 7 do display(a)$
                             a = - 3

                              a = 4

                             a = 11

                             a = 18

                             a = 25
```





Die Bedingung `while i <= 10` ist aquivalent zu den Bedingungen
`unless i > 10` und `thru 10` ist.



```maxima
(%i1) s: 0$
(%i2) for i: 1 while i <= 10 do s: s+i;
(%o2)                         done
(%i3) s;
(%o3)                          55
```




Berechne die ersten acht Terme einer Taylorreihe in einer `do`-Schleife.



```maxima
(%i1) series: 1$
(%i2) term: exp (sin (x))$
(%i3) for p: 1 unless p > 7 do
          (term: diff (term, x)/p, 
           series: series + subst (x=0, term)*x^p)$
(%i4) series;
                  7    6     5    4    2
                 x    x     x    x    x
(%o4)            -- - --- - -- - -- + -- + x + 1
                 90   240   15   8    2
```






In diesem Beispiel wird die negative Wurzel von 10 mit einem 
Newton-Raphson-Algorithmus berechnet. 



```maxima
(%i1) poly: 0$
(%i2) for i: 1 thru 5 do
          for j: i step -1 thru 1 do
              poly: poly + i*x^j$
(%i3) poly;
                  5      4       3       2
(%o3)          5 x  + 9 x  + 12 x  + 14 x  + 15 x
(%i4) guess: -3.0$
(%i5) for i: 1 thru 10 do
          (guess: subst (guess, x, 0.5*(x + 10/x)),
           if abs (guess^2 - 10) < 0.00005 then return (guess));
(%o5)                  - 3.162280701754386
```








Anstatt eines festes Inkrements mit `step` kann die Kontrollvariable auch 
mit `next` fur jeden Schleifendurchgang berechnet werden.



```maxima
(%i6) for count: 2 next 3*count thru 20 do display (count)$
                            count = 2

                            count = 6

                           count = 18
```


   






Anstatt mit der Syntax `for variable: value ...` kann die
Kontrollvariable auch mit `for variable from value ...do...`
initialisiert werden.  Wird auch `from value` fortgelassen, wird
die Kontrollvariable mit dem Wert 1 initialisiert.








Manchmal kann es von Interesse sein, in einer Schleife keine Kontrollvariable
zu nutzen.  In diesem Fall genugt es allein die Bedingung fur den Abbruch 
der Schleife anzugeben.  Im folgenden wird die Wurzel aus 5 mit dem 
Heron-Verfahren bestimmt.



```maxima
(%i1) x: 1000$
(%i2) thru 20 do x: 0.5*(x + 5.0/x)$
(%i3) x;
(%o3)                   2.23606797749979
(%i4) sqrt(5), numer;
(%o4)                   2.23606797749979
```







Auch die Abbruchbedingung kann fortgelassen werden.  Wird allein
`do body` angegeben, wird die Schleife unendlich oft ausgefuhrt. 
Die Schleife kann mit der `return`-Anweisung verlassen werden.   Das 
folgende Beispiel zeigt eine Implementierung des Newton-Algorithmus.



```maxima
(%i1) newton (f, x):= ([y, df, dfx], df: diff (f ('x), 'x),
          do (y: ev(df), x: x - f(x)/y, 
              if abs (f (x)) < 5e-6 then return (x)))$

(%i2) sqr (x) := x^2 - 5.0$
(%i3) newton (sqr, 1000);
(%o3)                   2.236068027062195
```


   







Eine weitere Syntax ist die folgende:



```maxima
for variable in list end_tests do body
```









Die Elemente der Liste *list* konnen beliebige Ausdrucke sein, die
nacheinander der Kontrollvariablen zugewiesen werden.  Die Schleife bricht ab, 
wenn die optionale Abbruchbedingung `end_test` zutrifft, wenn die Liste
*list* keine weiteren Elemente enthalt oder wenn die Schleife zum Beispiel
mit der Funktion `return` verlassen wird.



```maxima
(%i1)  for f in [log, rho, atan] do ldisp(f(1))$
(%t1)                                  0
(%t2)                                rho(1)
                                     %pi
(%t3)                                 ---
                                      4
(%i4) ev(%t3,numer);
(%o4)                             0.78539816
```

<!-- category: Programming -->
<!-- keywords: errcatch -->
<!-- signatures: errcatch(expr_1, ..., expr_n) -->
### Function: errcatch (expr_1, ..., expr_n)

Wertet die Ausdrucke *expr_1*, ..., *expr_n* nacheinander aus und
gibt das Ergebnis des letzten Ausdrucks als eine Liste `[expr_n]`
zuruck, wenn kein Fehler bei der Auswertung auftritt.  Tritt ein Fehler
bei der Auswertung eines der Ausdrucke auf, ist die Ruckgabe eine leere 
Liste `[]`.






`errcatch` ist nutzlich in Batch-Dateien.  Mit `errcatch` kann ein
moglicher Fehler abgefangen werden, ohne das die Verarbeitung der Batch-Datei
abbricht.


Beispiele:



```maxima
(%i1) errcatch(x:2,1/x);
                                1
(%o1)                          [-]
                                2
(%i2) errcatch(x:0,1/x);

Division by 0
(%o2)                          []
```

<!-- category: Programming -->
<!-- keywords: error -->
<!-- signatures: error(expr_1, ..., expr_n) -->
### Function: error (expr_1, ..., expr_n)

Wertet die Ausdrucke *expr_1*, ..., *expr_n* aus, gibt diese auf 
der Konsole aus und generiert einen Fehler, der zur obersten Ebene von Maxima 
fuhrt oder zu dem nachsten `errcatch`.







Der Systemvariablen `error` wird eine Liste zugewiesen, die eine 
Beschreibung des Fehlers enthalt.  Das erste Element der Liste ist eine
Zeichenkette und die weiteren Elemente enthalten die Argumente die keine 
Zeichenkette sind.





`errormsg()` formatiert und gibt die Fehlermeldung in `error` aus.
Damit wird die letzte Fehlermeldung erneut ausgegeben.


Beispiel:



```maxima
(%i1) f(x):= if x=0 then 
                error("Division durch", x, "ist nicht gestattet.") 
             else 1/x$
(%i2) f(0);

Division durch 0 ist nicht gestattet.
#0: f(x=0)
 -- an error. To debug this try: debugmode(true);
(%i3) errormsg();

Division durch 0 ist nicht gestattet.
(%o3)                         done
(%i4) error;
(%o4)      [Division durch ~M ist nicht gestattet., 0]
```

<!-- category: Programming -->
<!-- keywords: error_size -->
<!-- signatures: error_size -->
### Variable: error_size

Standardwert: 10









`error_size` kontrolliert die Ausgabe eines Ausdrucks der zu einem Fehler
gefuhrt hat.  Ist der Ausdruck großer als `error_size` wird der 
Ausdruck bei der Ausgabe einer Fehlermeldung durch ein Symbol ersetzt und dem 
Symbol wird der Ausdruck zugewiesen.  Die Symbole werden aus der Liste 
`error_syms` ausgewahlt.





Ist der Ausdruck kleiner als `error_size` wird dieser mit der Fehlermeldung
ausgegeben.




Siehe auch `error` und `error_syms`.


Beispiel:




Die Große des Ausdrucks `U` ist 24.



```maxima
(%i1) U: (C^D^E + B + A)/(cos(X-1) + 1)$

(%i2) error_size: 20$

(%i3) error ("Example expression is", U);

Example expression is errexp1
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) errexp1;
                            E
                           D
                          C   + B + A
(%o4)                    --------------
                         cos(X - 1) + 1
(%i5) error_size: 30$

(%i6) error ("Example expression is", U);

                         E
                        D
                       C   + B + A
Example expression is --------------
                      cos(X - 1) + 1
 -- an error.  Quitting.  To debug this try debugmode(true);
```

See also: `error`, `error_syms`.

<!-- category: Programming -->
<!-- keywords: error_syms -->
<!-- signatures: error_syms -->
### Variable: error_syms

Standardwert: `[errexp1, errexp2, errexp3]`







In Fehlermeldungen werden Ausdrucke, die großer als `error_size` 
sind, durch Symbole ersetzt, denen der Ausdruck zugewiesen wird.  Die Symbole 
werden nacheinander der Liste `error_syms` entnommen.






Sind keine Symbole mehr vorhanden, werden automatisch neue Symbole mit
`concat('errexp, n)` gebildet.




Siehe auch `error` und `error_size`.

See also: `error`, `error_size`.

<!-- category: Programming -->
<!-- keywords: errormsg -->
<!-- signatures: errormsg() -->
### Function: errormsg ()

Gibt die letzte Fehlermeldung erneut aus.  Die Fehlermeldung ist in der
Systemvariablen `errormsg` enthalten.  Die Funktion `errormsg`
formatiert diese und gibt sie aus.

<!-- category: Programming -->
<!-- keywords: eval_when -->
<!-- signatures: eval_when(keyword, expr_1, ..., expr_n), eval_when([keyword_1, keyword_2, ...], expr_1, ..., expr_n) -->
### Function: eval_when (keyword, expr_1, ..., expr_n)

Ein Ausdruck mit der Funktion `eval_when` wird an oberster Stelle in einer
Datei definiert und erlaubt die bedingte Auswertung von Ausdrucken beim Laden,
Ubersetzen oder Kompilieren einer Datei.  Das Argument *keyword* ist eines
der Schlusselworte `batch`, `translate`, `compile` oder
`loadfile`.  Das erste Argument kann ein einzelnes Schlusselwort oder
ein Liste mit mehreren Schlusselworten sein.  Trifft die mit dem
Schlusselwort angegebene Bedingung zu, wird eine oder mehrere der folgenden
Aktionen ausgefuhrt:



**batch** — Wird die Datei mit einer der Funktionen `load`, `batch`,
`batchload` oder `demo` geladen und ist `batch` in der Liste der
Schlusselworte enthalten, dann werden die Ausdrucke *expr1*, ...,
*expr_n* genau einmal beim Laden der Datei ausgewertet.  Die Ruckgabe der
Funktion `eval_when` ist ein Ausdruck `evaluated_when(result)`,
wobei *result* das Ergebnis der Auswertung ist.  Ist das Schlusselwort
`batch` nicht vorhanden, ist die Ruckgabe das Symbol
`not_evaluated_when`.
**translate** — Wird die Datei mit dem Kommando `translate_file` oder
`compile_file` geladen und ist `translate` unter den
Schlusselworten, dann werden die Ausdrucke *expr_1*, ...,
*expr_n* sofort ausgewertet.  Seiteneffekte wie Zuweisungen von Werten
an Optionsvariablen oder Deklarationen sind fur die folgende Ubersetzung
der Datei nach Lisp wirksam.  Die Ausdrucke sind jedoch nicht Teil des
ubersetzten Programms.
**loadfile** — Wird die Datei mit dem Kommando `translate_file` oder dem Kommando
`compile_file` geladen und ist `loadfile` unter den
Schlus­sel­wor­ten, dann werden die Ausdrucke *expr_1*, ...,
*expr_n* nach Lisp ubersetzt und als Block der Form
`(PROGN EXPR_1 ... EXPR_N)` in das Lisp Programm eingesetzt.  Hier sind
die Anweisungen *EXPR_I* die nach Lisp ubersetzten Maxima-Ausdrucke
*expr_i*.
**compile** — Wird die Datei mit dem Kommando `translate_file` oder
`compile_file` geladen und ist `compile` unter den
Schlus­sel­wor­ten, dann werden die Ausdrucke *expr_1*, ...,
*expr_n* nach Lisp ubersetzt und als eine Lisp-Anweisung in das
Lisp-Programm eingesetzt, die die Form `(EVAL-WHEN (:COMPILE-TOPLEVEL) (EXPR_1 ... EXPR_N))` hat.  Das Schlusselwort `compile` kann nicht mit
dem Schlusselwort `loadfile` in einem `eval_when`-Ausdruck
kombiniert werden.  In diesem Fall wird das Schlusselwort `compile`
ignoriert.


Beispiele:


Fur die folgende Beispiele ist eine Datei mit den Namen
`eval_when.mac` definiert, die verschiedene `eval_when`-Anweisungen
enthalt.



```maxima
(%i1) file: file_search("eval_when.mac");
(%o1)        /home/dieter/.maxima/eval_when.mac
(%i2) printfile(file);

eval_when(batch,     print("called in mode BATCH"));
eval_when(loadfile,  print("called in mode LOADFILE"));
eval_when(compile,   print("called in mode COMPILE"));
eval_when(translate, print("called in mode TRANSLATE"));

(%o2)        /home/dieter/.maxima/eval_when.mac
```


Die Datei wird mit dem Kommando `load` geladen.  Die Anweisung mit
dem Schlusselwort `batch` wird beim Laden einmal ausgefuhrt.



```maxima
(%i1) file: file_search("eval_when.mac");
(%o1)        /home/dieter/.maxima/eval_when.mac
(%i2) load("file");
called in mode BATCH
(%o2)        /home/dieter/.maxima/eval_when.mac
```


In diesem Fall wird die Datei mit dem Befehl `batch` geladen.  Die
Anweisung mit dem Schlusselwort `batch` wird einmal ausgefuhrt.
Die anderen `eval_when`-Anweisungen werten jeweils zum Ergebnis
`not_evaluated_when` aus.



```maxima
(%i3) batch(file);

read and interpret file: /home/dieter/.maxima/eval_when.mac
(%i4)     eval_when(batch, print(called in mode BATCH))
called in mode BATCH 
(%o4)         evaluated_when(called in mode BATCH)
(%i5)  eval_when(loadfile, print(called in mode LOADFILE))
(%o5)                  not_evaluated_when
(%i6)   eval_when(compile, print(called in mode COMPILE))
(%o6)                  not_evaluated_when
(%i7) eval_when(translate, print(called in mode TRANSLATE))
(%o7)                  not_evaluated_when
(%o7)        /home/dieter/.maxima/eval_when.mac
```


Jetzt wird die Datei mit dem Kommando `translate_file` geladen und nach
Lisp ubersetzt.  Der Ausdruck mit dem Schlusselwort `translate` wird
sofort ausgewertet.  Das ubersetzte Programm wird in die Ausgabedatei
`eval_when.LISP` geschrieben.  Die `eval_when`-Anweisung zum
Schlusselwort wird nicht ausgewertet.



```maxima
(%i1) file: file_search("eval_when.mac");
(%o1)        /home/dieter/.maxima/eval_when.mac
(%i2) translate_file(file);
translator: begin translating /home/dieter/.maxima/eval_when.mac.
called in mode TRANSLATE 
(%o2) [/home/dieter/.maxima/eval_when.mac, 
/home/dieter/.maxima/eval_when.LISP, 
/home/dieter/.maxima/eval_when.UNLISP]
```


Dies ist der Inhalt der Ausgabedatei `eval_when.LISP`.  Die Ausgabedatei
enthalt eine `PROGN`-Anweisung mit dem Ausdruck
`($print '"called in mode LOADFILE")` fur den `eval_when`-Ausdruck
zum Schlusselwort `loadfile` sowie eine `EVAL-WHEN`-Anweisung mit
dem Ausdruck `($print '"called in mode COMPILE")` fur den
`eval_when`-Ausdruck mit dem Schlusselwort `compile`.



;;; -*- Mode: Lisp; package:maxima; syntax:common-lisp ;Base: 10 -*- ;;;
;;; Translated on: 2011-10-02 13:35:37+02:00
;;; Maxima version: 5.25post
;;; Lisp implementation: SBCL
;;; Lisp version: 1.0.45
(in-package :maxima)

[...]

nil
(progn ($print '"called in mode LOADFILE"))
(eval-when (:compile-toplevel) ($print '"called in mode COMPILE"))
nil

See also: `load`, `batch`, `batchload`, `demo`, `translate_file`, `compile_file`.

<!-- category: Programming -->
<!-- keywords: for -->
<!-- signatures: for -->
### Function: for

Anweisung fur Interationen.  Siehe die `do`-Anweisung fur eine 
Beschreibung der Iterationsmoglichkeiten von Maxima.

See also: `do`.

<!-- category: Programming -->
<!-- keywords: go -->
<!-- signatures: go(tag) -->
### Function: go (tag)

Erlaubt einen Sprung innerhalb eines Blocks zu einer Marke mit dem Namen 
`tag`.  Um eine Anweisung mit einer Sprungmarke zu versehen, wird der
Anweisung die Marke vorangestellt.  Ein Beispiel ist:



```maxima
block ([x], x:1, loop, x+1, ..., go(loop), ...)
```






Das Argument der Funktion `go` muss der Name einer Marke sein, die in
demselben Block erscheint.  Es ist nicht moglich in einen anderen Block zu
springen.

<!-- category: Programming -->
<!-- keywords: if -->
<!-- signatures: if -->
### Function: if

Ist die bedingte Anweisung.  Verschiedene Formen einer bedingten Anweisung sind
moglich.






`if cond_1 then expr_1 else expr_0` wertet zu 
*expr_1* aus, wenn die Bedingung *cond_1* den Wert `true` hat.
Ansonsten wertet der Ausdruck zu *expr_0* aus.







Die zusammengesetzte bedingte Anweisung `if cond_1 then expr_1 elseif cond_2 then expr_2 elseif ... else expr_0` wertet 
zu *expr_k* aus, wenn die Bedingung *cond_k* den Wert `true` hat 
und alle vorhergehenden Bedingungen den Wert `false` haben.  Trifft keine 
der Bedingungen zu, wertet der Ausdruck zu *expr_0* aus.









Fehlt die Anweisung `else`, wird diese zu `else false` angenommen.
`if cond_1 then expr_1` ist daher aquivalent zu 
`if cond_1 then expr_1 else false` und `if cond_1 then expr_1 elseif ... elseif cond_n then expr_n` ist 
aquivalent zu `if cond_1 then expr_1 elseif ... elseif cond_n then expr_n else false`.







Die Anweisungen *expr_0*, ..., *expr_n* konnen beliebige 
Maxima-Ausdrucke ein­schließ­lich weiterer `if`-Anweisungen sein.  
Die Anweisungen werden nicht vereinfacht oder ausgewertet, solange die 
dazugehorende Bedingung nicht das Ergebnis `true` hat.











Die Bedingungen *cond_1*, ..., *cond_n* sind Ausdrucke, die zu 
`true` oder `false` ausgewertet werden konnen.  Kann eine Bedingung
nicht zu `true` oder `false` ausgewertet werden, hangt die Reaktion
von der Optionsvariablen `prederror` ab.  Hat `prederror` den Wert
`true`, dann meldet Maxima einen Fehler, wenn eine Bedingung nicht zu
`true` oder `false` ausgewertet werden kann.  Ansonsten werden
Bedingungen akzeptiert, die nicht zu `true` oder `false` ausgewertet
werden konnen und das Ergebnis ist ein bedingter Ausdruck.





Die Bedingungen konnen die folgenden Operatoren enthalten:


   
   
   


```maxima
Operation              Symbol      Typ
 
less than              <           relational infix
less than              <=
  or equal to                      relational infix
equality (syntactic)   =           relational infix
negation of =          #           relational infix
equality (value)       equal       relational function
negation of equal      notequal    relational function
greater than           >=
  or equal to                      relational infix
greater than           >           relational infix
and                    and         logical infix
or                     or          logical infix
not                    not         logical prefix
```

<!-- category: Programming -->
<!-- keywords: local -->
<!-- signatures: local(v_1, ..., v_n) -->
### Function: local (v_1, ..., v_n)

Speichert alle Eigenschaften der Symbole *v_1*, ..., *v_n*, entfernt
die Eigenschaften und stellt die abgespeicherten Eigenschaften nach dem Austritt
aus einem Block oder einem zusammengesetzten Ausdruck in dem `local`
auftritt wieder her.










Einige Deklarationen sind als Eigenschaft eines Symbols implementiert.  Dazu
gehoren Deklarationen mit `:=`, `array`, `dependencies`, 
`atvalue`, `matchdeclare`, `atomgrad`, `constant`, 
`nonscalar` oder `assume`.  Der Effekt von `local` ist, dass
solche Deklarationen nur lokal in dem Block wirksam sind.






`local` kann nur in `block`-Anweisungen oder in einer 
Funktionsdefinition oder in einem Lambda-Ausdruck verwendet werden. Weiterhin
darf `local` jeweils nur einmal auftreten.




`local` wertet die Argumente aus.  `local` hat die Ruckgabe 
`done`.


Beispiel:


Eine lokale Funktionsdefinition.



```maxima
(%i1) foo (x) := 1 - x;
(%o1)                    foo(x) := 1 - x
(%i2) foo (100);
(%o2)                         - 99
(%i3) block (local (foo), foo (x) := 2 * x, foo (100));
(%o3)                          200
(%i4) foo (100);
(%o4)                         - 99
```

<!-- category: Programming -->
<!-- keywords: return -->
<!-- signatures: return(value) -->
### Function: return (value)

Die `return`-Anweisung wird in einem Block verwendet, um den Block mit dem
Ergebnis *value* zu verlassen.  Siehe `block` fur mehr Informationen.

See also: `block`.

<!-- category: Programming -->
<!-- keywords: throw -->
<!-- signatures: throw(expr) -->
### Function: throw (expr)

Wertet den Ausdruck *expr* aus und generiert eine Ausnahme mit dem Ergebnis
der Auswertung, die von der letzten `catch`-Anweisung behandelt wird.

<!-- category: Programming -->
<!-- keywords: while, unless -->
<!-- signatures: unless -->
### Function: while

Siehe den Operator `do`.

See also: `do`.

