## Ubersetzer

<!-- category: Combinatorics -->
<!-- keywords: compfile -->
<!-- signatures: compfile(filename, f_1, ..., f_n), compfile(filename, functions), compfile(filename, all) -->
### Function: compfile (filename, f_1, ..., f_n)

Ubersetzt Maxima-Funktionen nach Lisp und schreibt den ubersetzten Code in 
die Datei *filename*.  Mit dem Kommando `compfile(filename f_1, ..., f_n)` werden die als Argument angegebenen Funktionen
*f_1*, ..., *f_n* ubersetzt.  Die Kommandos
`compfile(filename, functions)` oder `compfile(filename, all)` ubersetzen dagegen alle vom Nutzer definierten Funktionen.




   



Die Lisp-Ubersetzungen werden nicht ausgewertet.  Auch wird die Ausgabedatei
nicht kompiliert.  `translate` generiert und wertet Lisp-Ubersetzungen
aus.  Die Funktion `compile_file` ubersetzt Maxima nach Lisp und fuhrt
dann den Lisp-Compiler aus.




Siehe auch die Funktionen `translate`, `translate_file` und
`compile_file`.

See also: `translate`, `translate_file`, `compile_file`.

<!-- category: Combinatorics -->
<!-- keywords: compile -->
<!-- signatures: compile(f_1, ..., f_n), compile(functions), compile(all) -->
### Function: compile (f_1, ..., f_n)

Ubersetzt die Maxima-Funktionen *f_1*, ..., *f_n* nach Lisp, 
wertet die Lisp-Ubersetzungen aus und ruft den Lisp-Compiler fur jede 
ubersetzte Funktion auf.  `compile` gibt eine Liste mit den Namen der 
kompilierten Funktionen zuruck.





`compile(all)` oder `compile(funtions)` kompiliert alle
nutzerdefinierten Funktionen.





`compile` wertet die Argumente nicht aus.  Der
Quote-Quote-Operator `''` erzwingt die Auswertung.

<!-- category: Combinatorics -->
<!-- keywords: compile_file -->
<!-- signatures: compile_file(filename), compile_file(filename, compiled_filename), compile_file(filename, compiled_filename, lisp_filename) -->
### Function: compile_file (filename)

Ubersetzt die Maxima-Datei *filename* nach Lisp, ruft den Lisp-Compiler 
auf und ladt falls erfolgreich den kompilierten Code in Maxima.






`compile_file` gibt eine Liste mit den Namen von vier Dateien zuruck:
die ursprungliche Maxima-Datei, die Lisp-Ubersetzung, eine Datei mit Notizen
zur Ubersetzungen und eine Datei mit dem kompilierten Code.  Schlagt die
Kompilierung fehlt, ist der vierte Eintrag `false`.





   




Einige Deklarationen und Definitionen sind bereits vorhanden, nachdem der 
Lisp-Code kompiliert ist und ohne das dieser geladen wurde.  Dies schließt
Funktionsdefinitionen mit dem Operator `:=`, Makros definiert mit dem
Operator `::=` sowie Definitionen der folgenden Funktionen `alias`, 
`declare`, `define_variable`, `mode_declare`, `infix`, 
`matchfix`, `nofix`, `postfix`, `prefix` und 
`compfile` ein.






Zuweisungen und Funktionsaufrufe werden nicht ausgwertet bevor der komplierte
Code geladen wird.  Im besonderen haben Zuweisungen an die 
Ubersetzungsschalter wie `tr_numer` und andere, die in der Maxima-Datei
aufgefuhrt sind, keinen Effekt auf die Ubersetzung.





   

`compile_file` kann Fehler oder Warnungen ausgegeben und `false`
zuruckgegeben, obwohl die Kompilierung erfolgreich ist.  Dies ist ein
Programmfehler




Die Datei *filename* darf keine `:lisp`-Anweisungen enthalten.




`compile_file` wertet die Argumente aus.

<!-- category: Combinatorics -->
<!-- keywords: declare_translated -->
<!-- signatures: declare_translated(f_1, f_2, ...) -->
### Function: declare_translated (f_1, f_2, ...)

Bei der Ubersetzung einer Datei von Maxima-Code nach Lisp-Code ist es fur 
den Ubersetzer wichtig zu wissen, welche Funktionen der Datei bereits 
ubersetzte oder kompilierte Funktionen sind und welche Funktionen 
Maxima-Funktionen oder undefiniert sind.  Mit der Deklaration 
`declare_translated` am Anfang der zu ubersetzenden Datei wird dem 
Ubersetzer mitgeteilt, dass die als Argumente aufgefuhrten Funktionen 
*f_1*, *f_2*, ... zur Laufzeit des Programms eine Lisp-Funktion 
reprasentieren.  Fehlt dem Ubersetzer diese Information wird das Kommando 
`(MFUNCTION-CALL fn arg1 arg2 ...)` generiert.

<!-- category: Combinatorics -->
<!-- keywords: mode_check_errorp -->
<!-- signatures: mode_check_errorp -->
### Variable: mode_check_errorp

Standardwert: `false`


   



Hat `mode_check_errorp` den Wert `true`, bricht `mode_declare`
mit einer Fehlermeldung ab, wenn fur eine Variable die bereits einen Wert hat,
mit `mode_declare` ein verschiedener Typ deklariert werden soll.  Damit
diese Optionsvariable wirksam ist, muss `mode_checkp` den Wert `true`
haben.  Siehe `mode_checkp`.



```maxima
(%i1) n: 2.0;
(%o1)                          2.0
(%i2) mode_checkp:true;
(%o2)                         true
(%i3) mode_check_errorp:true;
(%o3)                         true
(%i4) mode_declare(n,fixnum);

Error: n was declared mode fixnum, has value: 2.0
 -- an error. To debug this try: debugmode(true);
```

See also: `mode_checkp`.

<!-- category: Combinatorics -->
<!-- keywords: mode_check_warnp -->
<!-- signatures: mode_check_warnp -->
### Variable: mode_check_warnp

Standardwert: `true`


   


Hat `mode_check_warnp` den Wert `true`, gibt `mode_declare`
eine Warnung aus, wenn fur eine Variable die bereits einen Wert hat,
mit `mode_declare` ein verschiedener Typ deklariert werden soll.  Damit
diese Optionsvariable wirksam ist, muss `mode_checkp` den Wert `true`
haben.  Siehe `mode_checkp` und `mode_check_errorp`.

See also: `mode_checkp`, `mode_check_errorp`.

<!-- category: Combinatorics -->
<!-- keywords: mode_checkp -->
<!-- signatures: mode_checkp -->
### Variable: mode_checkp

Standardwert: `true`


   



Hat die Optionsvariable `mode_checkp` den Wert `true` und wird
mit `mode_declare` fur eine Variable, die bereits einen Wert hat, ein Typ 
festgelegt, dann pruft Maxima, ob der vorgesehene Typ zum vorliegenden Wert 
passt.


Beispiel:


Im folgenden hat die Variable *n* den Wert 2.0.  Wird *n* mit
`mode_declare` als eine ganze Zahl definiert, gibt Maxima eine Warnung aus,
wenn `mode_checkp` den Wert `true` hat.



```maxima
(%i1) n: 2.0;
(%o1)                          2.0
(%i2) mode_checkp:true;
(%o2)                         true
(%i3) mode_declare(n,fixnum);
warning: n was declared with mode fixnum, but it has value: 2.0
(%o3)                          [n]
(%i4) mode_checkp:false;
(%o4)                         false
(%i5) mode_declare(n,fixnum);
(%o5)                          [n]
```

<!-- category: Combinatorics -->
<!-- keywords: mode_declare -->
<!-- signatures: mode_declare(y_1, mode_1, ..., y_n, mode_n) -->
### Function: mode_declare (y_1, mode_1, ..., y_n, mode_n)

`mode_declare` deklariert den Typ von Variablen und Funktionen fur den
Ubersetzer und den Kompilierer.  Typischerweise wird `mode_declare` am
Anfang einer Funktion oder einer Datei mit Maxima-Code ausgefuhrt.







Die Argumente werden paarweise angegeben und bezeichnen jeweils den Namen einer
Variablen sowie deren Typ.  Folgende Typen konnen die Variablen erhalten:
`boolean`, `fixnum`, `number`, `rational` oder `float`.
Anstatt dem Namen einer Variablen kann auch eine Liste mit den Namen von
Variablen angegeben werden.  In diesem Fall erhalten alle Variablen der Liste
den angegebenen Typ.


   







   



Ein Array sollte bereits bei seiner Deklaration einen Typ fur die Elemente
erhalten.  Haben alle Elemente des Arrays einen Wert sollte das Array mit der
Option `complete` deklariert werden, zum Beispiel
`array(a, complete, dim1, dim2, ...)`.  Sind die Elemente des Arrays
ganze Zahlen oder Gleitkommazahlen sollte der Typ als `fixnum` oder
`flonum` deklariert werden.


   












Mit der Funktion `mode_declare` kann dann der Typ des Arrays fur den
Ubersetzer oder Kompilierer festgelegt werden.  Ein Array der Große 
10 `x` 10 mit Gleitkommazahlen erhalt die Deklaration
`mode_declare(completearray(a[10, 10], float)`.











Der Typ von Funktionen wird mit dem Argument `function(f_1, f2, ...)`
deklariert.  Hier sind `f_1`, `f_2`, ... die Funktionen.  Mit
`mode_declare([function (f_1, f_2, ...)], fixnum)` werden die 
Ruckgabewerte der Funktionen `f_1`, `f_2`, ... als ganze Zahlen 
definiert.




`modedeclare` ist ein Alias-Name der Funktion `mode_declare`.

<!-- category: Combinatorics -->
<!-- keywords: mode_identity -->
<!-- signatures: mode_identity(mode, expr) -->
### Function: mode_identity (mode, expr)

Mit der Funktion `mode_identity` wird der Typ *mode* fur das
Ergebnis des Ausdrucks *expr* festgelegt.  Hat das Ergebnis einen anderen 
Typ wird in Abhangigkeit von den Werten der Optionsvariablen 
`mode_checkp`, `mode_check_warnp` und `mode_check_errorp` eine
Warnung ausgegeben oder das Programm abgebrochen.


Beispiel:








```maxima
(%i1) mode_identity(flonum, sin(1.0));
(%o1)                   .8414709848078965
(%i2) mode_identity(integer, sin(1.0));
warning: sin(1.0) was declared with mode fixnum
                            , but it has value: .8414709848078965
(%o2)                   .8414709848078965
(%i3) mode_identity(integer, sin(a));
warning: sin(a) was declared with mode fixnum, but it has value: 
                                                           sin(a)
(%o3)                        sin(a)
```

<!-- category: Combinatorics -->
<!-- keywords: savedef -->
<!-- signatures: savedef -->
### Variable: savedef

Standardwert: `true`






Hat `savedef` den Wert `true`, wird die Maxima-Definition einer
Funktion nicht geloscht, wenn die Funktion ubersetzt wird.  Damit kann die
Definition der Funktion weiterhin mit `dispfun` angzeigt werden. 





Hat `savedef` den Wert `false` wird die Maxima-Definition der Funktion
geloscht, wenn die Funktion ubersetzt wird.


Beispiele:


`savedef` hat den Wert `true`.  Die Funktion `f` kann auch nach
der Ubersetzung angzeigt werden und ist in der Liste `functions`
enthalten.










```maxima
(%i1) savedef:true;
(%o1)                         true
(%i2) f(x):=x^2+sin(x);
                                2
(%o2)                  f(x) := x  + sin(x)
(%i3) translate(f);
(%o3)                          [f]
(%i4) dispfun(f);
                                2
(%t4)                  f(x) := x  + sin(x)

(%o4)                         [%t4]
(%i5) functions;
(%o5)                        [f(x)]
```


Dasselbe fur eine Funktion `g` mit dem Wert `false` fur 
`savedef`.










```maxima
(%i6) savedef:false;
(%o6)                         false
(%i7) g(x):=sqrt(x)+cos(x)$

(%i8) translate(g);
(%o8)                          [g]
(%i9) dispfun(g);

fundef: no such function: g
 -- an error. To debug this try: debugmode(true);
(%i10) functions;
(%o10)                       [f(x)]
```

<!-- category: Combinatorics -->
<!-- keywords: tr_array_as_ref -->
<!-- signatures: tr_array_as_ref -->
### Variable: tr_array_as_ref

Standardwert: `true`







Hat `translate_fast_arrays` den Wert `false`, werden Referenzen auf
Arrays in Lisp-Code von der Variablen `tr_array_as_ref` kontrolliert.  Hat
`tr_array_as_ref` den Wert `true`, werden Array-Namen ausgewertet.





`tr_array_as_ref` hat keinen Effekt, wenn `translate_fast_arrays` den
Wert `true` hat.

<!-- category: Combinatorics -->
<!-- keywords: tr_bound_function_applyp -->
<!-- signatures: tr_bound_function_applyp -->
### Variable: tr_bound_function_applyp

Standardwert: `true`





   



Hat `tr_bound_function_applyp` den Wert `true`, gibt Maxima eine
Warnung aus, wenn versucht wird, eine gebundene Variable als eine Funktion
verwendet werden soll.  `tr_bound_function_applyp` hat keinen Effekt auf
den generierten Code.





Zum Beispiel gibt ein Ausdruck der Form  `g (f, x) := f (x+1)` eine 
Warnung.

<!-- category: Combinatorics -->
<!-- keywords: tr_file_tty_messagesp -->
<!-- signatures: tr_file_tty_messagesp -->
### Variable: tr_file_tty_messagesp

Standardwert: `false`







Hat `tr_file_tty_messagesp` den Wert `true`, werden Meldungen die
von der Funktion `translate_file` wahrend einer Ubersetzung generiert 
werden auch auf der Konsole ausgegeben.  Ansonsten werden Meldungen nur in die
Datei `.UNILISP` geschrieben.

<!-- category: Combinatorics -->
<!-- keywords: tr_float_can_branch_complex -->
<!-- signatures: tr_float_can_branch_complex -->
### Variable: tr_float_can_branch_complex

Standardwert: `true`





Erklart dem Ubersetzer, dass die Funktionen `acos`, `asin`, 
`asec` und `acsc` komplexe Werte zuruckgegeben konnen.

<!-- category: Combinatorics -->
<!-- keywords: tr_function_call_default -->
<!-- signatures: tr_function_call_default -->
### Variable: tr_function_call_default

Standardwert: `general`














`false` bedeutet, gebe auf und rufe `meval` auf, `expr` bedeutet,
nehme Lisp-Argumente an.  `general`, der Standardwert, gibt Code der fur
`MEXPRS`-Funktionen geeignet ist.  Wird Maxima-Code mit dem Standardwert
`general` ubersetzt, ohne dass Warnmeldungen ausgegeben werden, kann davon
ausgegangen werden, dass der ubersetzte und komplilierte Code kompatibel mit der
ursprunglichen Funktion ist.

<!-- category: Combinatorics -->
<!-- keywords: tr_numer -->
<!-- signatures: tr_numer -->
### Variable: tr_numer

Standardwert: `false`





Hat `tr_numer` den Wert `true`, wird die `numer`-Eigenschaft
von Symbolen vom Ubersetzer angewendet.

<!-- category: Combinatorics -->
<!-- keywords: tr_optimize_max_loop -->
<!-- signatures: tr_optimize_max_loop -->
### Variable: tr_optimize_max_loop

Standardwert: 100







`tr_optimize_max_loop` enthalt die maximale Anzahl an Durchgangen, um
Makros zu expandieren und den Code zu optimieren.  Damit werden unendliche
Schleifen des Ubersetzers vermieden.

<!-- category: Combinatorics -->
<!-- keywords: tr_semicompile -->
<!-- signatures: tr_semicompile -->
### Variable: tr_semicompile

Standardwert: `false`






Hat `tr_semicompile` den Wert `true`, geben die Funktionen 
`translate_file` und `compfile` Code aus, in dem Makrofunktionen
expandiert sind, der aber nicht kompliliert ist.

<!-- category: Combinatorics -->
<!-- keywords: tr_state_vars -->
<!-- signatures: tr_state_vars -->
### Variable: tr_state_vars

Standardwert:


[transcompile, tr_semicompile, tr_warn_undeclared, tr_warn_meval,
tr_warn_fexpr, tr_warn_mode, tr_warn_undefined_variable,
tr_function_call_default, tr_array_as_ref,tr_numer]



   




Enthalt eine Liste der Schalter, die die Ubersetzung kontrollieren.

<!-- category: Combinatorics -->
<!-- keywords: tr_warn_bad_function_calls -->
<!-- signatures: tr_warn_bad_function_calls -->
### Variable: tr_warn_bad_function_calls

Standardwert: `true`





Gebe Warnungen aus, wenn Funktionsaufrufe generiert werden, die moglicherweise
nicht korrekt sind, aufgrund von ungeeigneten Deklarationen fur die 
Ubersetzung.

<!-- category: Combinatorics -->
<!-- keywords: tr_warn_fexpr -->
<!-- signatures: tr_warn_fexpr -->
### Variable: tr_warn_fexpr

Standardwert: `compfile`






Gebe Warnungen aus, wenn `FEXPR`-Ausdrucke im ubersetzten Code 
auftreten.

<!-- category: Combinatorics -->
<!-- keywords: tr_warn_meval -->
<!-- signatures: tr_warn_meval -->
### Variable: tr_warn_meval

Standardwert: `compfile`





Gebe Warnungen aus, wenn die Funktion `meval` aufgerufen wird.  Dies
signalisiert Probleme bei der Ubersetzung.

<!-- category: Combinatorics -->
<!-- keywords: tr_warn_mode -->
<!-- signatures: tr_warn_mode -->
### Variable: tr_warn_mode

Standardwert: `all`





Gebe Warnungen aus, wenn Variablen Werte zugewiesen werden, die nicht zu dem
deklarierten Typ passen.

<!-- category: Combinatorics -->
<!-- keywords: tr_warn_undeclared -->
<!-- signatures: tr_warn_undeclared -->
### Variable: tr_warn_undeclared

Standardwert: `compile`




Kontrolliert, wann Warnungen uber nicht-deklarierte Variablen angezeigt werden
sollen.

<!-- category: Combinatorics -->
<!-- keywords: tr_warn_undefined_variable -->
<!-- signatures: tr_warn_undefined_variable -->
### Variable: tr_warn_undefined_variable

Standardwert: `all`




Gebe eine Warnung aus, wenn undefinierte globale Variablen auftreten.

<!-- category: Combinatorics -->
<!-- keywords: tr_warnings_get -->
<!-- signatures: tr_warnings_get() -->
### Function: tr_warnings_get ()

Gebe die Liste der Warnungen aus, welche bei der letzten Ubersetzung erzeugt 
wurden.

<!-- category: Combinatorics -->
<!-- keywords: transcompile -->
<!-- signatures: transcompile -->
### Variable: transcompile

Standardwert: `true`





   
   

Hat `transcompile` den Wert `true`, generieren die Funktionen
`translate` und `translate_file` Deklarationen, die das Kompilieren
des Codes verbessern.




`compfile` setzt den Wert von `transcompile` zu `true`.

<!-- category: Combinatorics -->
<!-- keywords: translate -->
<!-- signatures: translate(f_1, ..., f_n), translate(functions), translate(all) -->
### Function: translate (f_1, ..., f_n)

Die vom Nutzer definierten Maxima-Funktionen *f_1*, ..., *f_n* 
werden nach Lisp ubersetzt.  Typischerweise sind die ubersetzten Funktionen 
schneller als die Maxima-Funktionen.





`translate(all)` oder `translate(functions)` ubersetzt alle vom
Benutzer definierten Funktionen.








Funktionen, die ubersetzt werden sollen, sollten mit `mode_declare` den
Typ von Variablen und Funktionen deklarieren, um effizienteren Code zu erhalten.
Im Folgenden Beispiel sind *x_1*, *x_2*, ... die Argumente der 
Funktion und *v_1*, *v_2*, ... sind die lokalen Variablen.



```maxima
f (x_1, x_2, ...) := block ([v_1, v_2, ...],
    mode_declare (v_1, mode_1, v_2, mode_2, ...), ...)
```






Die Namen von ubersetzten Funktionen werden von der Informationsliste
`functions` entfernt, wenn die Optionsvariable `savedef` den Wert
`false` hat.  Sie werden der Informationsliste `props` hinzugefugt.




Funktionen sollten erst ubersetzt werden, wenn sie vollstandig von Fehlern
befreit wurden.







Ausdrucke werden als vereinfacht angenommen.  Sind sie es nicht, wird zwar
korrekter, aber nicht optimierter Code erzeugt.  Daher sollte der Schalter
`simp` nicht den Wert `false` haben, wodurch die Vereinfachung von
Ausdrucken unterdruckt ware.





Hat der Schalter `translate` den Wert `true`, werden nutzerdefinierte
Funktionen automatisch nach Lisp ubersetzt.








   

Das Laufzeitverhalten von ubersetzten Funktionen kann sich von dem 
nicht-ubersetzter Funktionen unterscheiden.  Grundsatzlich sollte die 
Funktion `rat` nicht mit mehr als zwei Argumenten und die Funktion 
`ratvars` nicht genutzt werden, wenn irgendeine der Variablen eine CRE-Form
mit Deklaration mit `mode_declare` aufweisen.  Auch wird 
`prederror:false` nicht ubersetzt.










Hat die Optionsvariable `savedef` den Wert `true`, wird die
Originalversion einer Funktion nicht entfernt.  Siehe `savedef`.  Mit
dem Wert `false` fur `transrun` werden, wenn noch vorhanden, die 
Originalversionen der ubersetzten Funktion ausgefuhrt.





Das Ergebnis der Funktion `translate` ist eine Liste der Namen der
ubersetzten Funktionen.

See also: `savedef`.

<!-- category: Combinatorics -->
<!-- keywords: translate_file -->
<!-- signatures: translate_file(maxima_filename), translate_file(maxima_filename, lisp_filename) -->
### Function: translate_file (maxima_filename)

Ubersetzt eine Datei mit Maxima-Code in eine Datei mit Lisp-Code.
`translate_file` gibt eine Liste mit drei Dateien zuruck, die den
Namen der Maxima-Datei, den Namen der Lisp-Datei und den Namen einer Datei
mit Informationen zur Ubersetzung enthalt.  `translate_file` wertet die
Argumente aus.





   

Die Kommandos `translate_file("foo.mac")` und `load("foo.LISP")` 
haben bis auf wenige Ausnahmen dieselbe Wirkung wie `batch("foo.mac")`.  
Zum Beispiel funktionieren `''` und `%` unterschiedlich.








`translate_file(maxima_filename)` ubersetzt die Maxima-Datei
*maxima_filename* in ein Lisp-Datei mit einem vergleichbaren Namen.  Zum
Beispiel wird die Maxima-Datei `foo.mac` zu `foo.LISP`.  Der Name der 
Maxima-Datei kann Pfadangaben enthalten.  In diesem Fall wird die Lisp-Datei
in dasselbe Verzeichnis wie die Maxima-Datei geschrieben.









`translate_file(maxima_filename, lisp_filename)` ubersetzt
die Maxima-Datei *maxima_filename* in eine Lisp-Datei mit dem Namen
`lisp_filename`.  `translate_file` ignoriert eine angegebene 
Dateiendung des Dateinamenes `lisp_filename`.  Die Dateiendung ist immer
`.LISP`.  Der Name der Lisp-Datei kann Pfadangaben enthalten, um die
Lisp-Datei in das gewunschte Verzeichnis zu schreiben.








`translate_file` schreibt eine Ausgabedatei mit Meldungen des 
Ubersetzers.  Die Dateiendung der Ausgabedatei ist `.UNILISP`.  Die 
Informationen dieser Datei konnen fur die Fehlersuche genutzt werden.  Die 
Datei wird immer in das Verzeichnis geschrieben, das die Maxima-Datei enthalt.






`translate_file` generiert Lisp-Code mit Deklarationen und Definitionen,
die bereits beim Kompilieren des Codes wirksam werden.  Siehe 
`compile_file` fur mehr Informationen.


   



Siehe auch die folgenden Optionsvariablen:



`tr_array_as_ref`,



`tr_bound_function_applyp`,


`tr_exponent`,
`tr_file_tty_messagesp`, 
`tr_float_can_branch_complex`,
`tr_function_call_default`, 
`tr_numer`,
`tr_optimize_max_loop`, 
`tr_semicompile`,
`tr_state_vars`, 
`tr_warnings_get`,
`tr_warn_bad_function_calls`,
`tr_warn_fexpr`, 
`tr_warn_meval`,
`tr_warn_mode`,
`tr_warn_undeclared`,
und `tr_warn_undefined_variable`.

See also: `compile_file`.

<!-- category: Combinatorics -->
<!-- keywords: transrun -->
<!-- signatures: transrun -->
### Variable: transrun

Standardwert: `true`






Hat `transrun` den Wert `false`, werden die nicht-ubersetzten 
Versionen ausgefuhrt, falls diese noch vorhanden sind.  
Siehe `savedef`.

See also: `savedef`.

