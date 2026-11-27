## Fehlersuche

<!-- category: Other -->
<!-- keywords: debugmode -->
<!-- signatures: debugmode -->
### Variable: debugmode

Standardwert: `false`







Hat die Optionsvariable `debugmode` den Wert `true`, wird der 
Maxima-Debugger gestartet, wenn ein Programmfehler auftritt.  Nach der 
Unterbrechung des Programms kann der Debugger genutzt werden.  Siehe das Kapitel
Debugger-Kommandos fur eine Liste der Kommandos des Debuggers.



  
  

Der Maxima-Debugger behandelt keine Lisp-Programmfehler.

<!-- category: Other -->
<!-- keywords: refcheck -->
<!-- signatures: refcheck -->
### Variable: refcheck

Standardwert: `false`





Hat `refcheck` den Wert `true`, gibt Maxima eine Meldung aus, wenn
einer Variablen zum ersten Mal ein Wert zugewiesen wird.

<!-- category: Other -->
<!-- keywords: setcheck -->
<!-- signatures: setcheck -->
### Variable: setcheck

Standardwert: `false`









Der Optionsvariablen `setcheck` kann eine Liste mit den Namen von Variablen
zugewiesen werden.  Dies konnen auch indizierte Variablen sein.  Immer wenn 
einer der Variablen mit den Operatoren `:` oder `::` ein Wert 
zugewiesen wird, gibt Maxima eine Meldung aus, die den Namen der Variablen und 
den zugewiesenen Wert enthalt.





`setcheck` kann den Wert `all` oder `true` erhalten.  In diesem
Fall wird fur alle Variablen eine Meldung ausgegeben.






Jede Zuweisung an `setcheck` initialisert eine neue Liste mit Variablen. 
Vorherige Zuweisungen werden uberschrieben.







Die Auswertung der Namen der Variablen muss mit dem
Quote-Operator `'` unterdruckt werden, wenn den Variablen
bereits Werte zugewiesen wurden.  Haben zum Beispiel die Variablen `x`,
`y` und `z` Werte, dann werden die Variablen mit dem folgenden Befehl
angegeben:



```maxima
setcheck: ['x, 'y, 'z]$
```





Es wird keine Meldung ausgegeben, wenn eine Variable sich selbst zugewiesen
wird, zum Beispiel `X: 'X`.

<!-- category: Other -->
<!-- keywords: setcheckbreak -->
<!-- signatures: setcheckbreak -->
### Variable: setcheckbreak

Standardwert: `false`








Hat `setcheckbreak` den Wert `true`, startet Maxima den Debugger, 
wenn einer Variablen, die in der Liste `setcheck` enthalten ist, ein
Wert zugewiesen wird.  Die Unterbrechung wird noch vor der Zuweisung des Wertes
ausgefuhrt.  Die Variable `setval` enhalt den Wert, der zugewiesen 
werden soll.  Dieser Variablen kann ein anderer Wert zugewiesen werden.




Siehe auch `setcheck` und `setval`.

See also: `setcheck`, `setval`.

<!-- category: Other -->
<!-- keywords: setval -->
<!-- signatures: setval -->
### Variable: setval

Enthalt den Wert, der einer Variable zugewiesen werden soll, wenn die 
Zuweisung mit der Optionsvariablen `setcheckbreak` unterbrochen wurde. 
`setval` kann ein anderer Wert zugewiesen werden.




Siehe auch `setcheck` und `setcheckbreak`.

See also: `setcheck`, `setcheckbreak`.

<!-- category: Other -->
<!-- keywords: timer -->
<!-- signatures: timer(f_1, ..., f_n), timer(all), timer() -->
### Function: timer (f_1, ..., f_n)

Sammelt Statistiken uber die Ausfuhrungszeiten von Funktionen.  Die 
Argumente *f_1*, ..., *f_n* sind die Namen von Funktionen zu denen 
Statistiken gesammelt werden.  `time(g)` fugt die Funktion `g` der 
Liste an Funktionen hinzu, zu denen Informationen gesammelt werden.







`timer(all)` fugt alle nutzerdefinierten Funktionen, die in der 
Informationsliste `functions` enthalten sind, der Liste der Funktionen
hinzu, uber die Informationen gesammelt werden.




Wird `timer()` ohne Argumente aufgerufen, wird eine Liste der Funktionen
zuruckgeben, uber die Informationen gesammelt werden.








Maxima misst die Zeit, die eine Funktion fur die Ausfuhrung benotigt. 
`timer_info` gibt eine Statistik fur alle Funktionen zuruck, fur die 
die Ausfuhrungszeiten gemessen werden.  Die Statistik enthalt die 
durchschnittliche Ausfuhrungszeit der Funktionen und die Anzahl der Aufrufe 
der Funktionen.  Mit der Funktion `untimer` wird die Aufzeichnung der 
Ausfuhrungszeiten beendet.





`timer` wertet die Argumente nicht aus.  Daher werden im Folgenden
`f(x) := x^2$ g:f$ timer(g)$` fur die Funktion `f` keine 
Ausfuhrungszeiten aufgezeichnet.





Wird fur die Funktion `f` mit dem Kommando `trace(f)` der Ablauf
verfolgt, hat das Kommando `timer(f)` keinen Effekt.  Fur eine Funktion
konnen nicht gleichzeitig Ausfuhrungszeiten aufgezeichnet und der Ablauf
verfolgt werden.




Siehe auch `timer_devalue`.

See also: `timer_devalue`.

<!-- category: Other -->
<!-- keywords: timer_devalue -->
<!-- signatures: timer_devalue -->
### Variable: timer_devalue

Standardwert: `false`







Hat `timer_devalue` den Wert `true`, subtrahiert Maxima bei der
Aufzeichnung der Ausfuhrungszeiten die Zeiten, welche eine Funktion in anderen
Funktionen verbringt.  Ansonsten enthalten die aufgezeichneten Zeiten auch die
Ausfuhrungszeiten der Funktionen, die aufgerufen werden.




Siehe auch `timer` und `timer_info`.

See also: `timer`, `timer_info`.

<!-- category: Other -->
<!-- keywords: timer_info -->
<!-- signatures: timer_info(f_1, ..., f_n), timer_info() -->
### Function: timer_info (f_1, ..., f_n)

Gibt eine Tabelle mit den aufgezeichneten Informationen uber die 
Ausfuhrungszeiten der Funktionen *f_1*, ..., *f_n* zuruck.  Wird 
kein Argument angegeben, werden Informationen fur alle Funktionen angezeigt, 
zu denen Informationen aufgezeichnet sind.







Die Tabelle enthalt die Namen der Funktionen, die Ausfuhrungszeit pro 
Aufruf, die Anzahl der Aufrufe, die gesamte Zeit und die `gctime`-Zeit. 
Die `gctime`-Zeit bedeutet "Garbage Collection Time".






Die Daten, die von der Funktion `timer_info` angezeigt werden, konnen 
auch mit der Funktion `get` erhalten werden:



```maxima
get(f, 'calls);  get(f, 'runtime);  get(f, 'gctime);
```




Siehe auch `timer`.

See also: `timer`.

<!-- category: Other -->
<!-- keywords: trace -->
<!-- signatures: trace(f_1, ..., f_n), trace(all), trace() -->
### Function: trace (f_1, ..., f_n)

Startet die Ablaufverfolgung fur die Funktionen *f_1*, ..., *f_n*. 
Mit dem Kommando `trace(g)` kann eine weitere Funktion hinzugefugt 
werden.





`trace(all)` startet die Ablaufverfolgung fur alle nutzerdefinierten
Funktionen, die in der Informationsliste `functions` enthalten sind.





Das Kommando `trace()` zeigt eine Liste aller Funktionen fur die eine
Ablaufverfolgung gestartet wurde.




Mit der Funktion `untrace` wird die Ablaufverfolgung beendet.  Siehe auch
`trace_options`.





`trace` wertet die Argumente nicht aus. 











Die Ablaufverfolgung kann fur eine Funktion `f` nicht gestartet werden,
wenn fur die Funktion bereits mit der Funktion `timer` Informationen 
uber die Ausfuhrungszeiten gesammelt werden.

See also: `trace_options`.

<!-- category: Other -->
<!-- keywords: trace_options -->
<!-- signatures: trace_options(f, option_1, ..., option_n), trace_options(f) -->
### Function: trace_options (f, option_1, ..., option_n)

Setzt Optionen fur die Ablaufverfolgung einer Funktion *f*.  Bereits 
vorliegende Optionen werden ersetzt.




`trace_options(f)` setzt alle Optionen auf die Standardwerte 
zuruck.




Die Optionen sind:



**noprint** — Gebe keine Meldung beim Eintritt in eine oder dem Austritt aus einer Funktion 
aus.
**break** — Setze eine Unterbrechnung vor dem Eintritt in eine Funktion und nach dem
Austritt aus einer Funktion.  Siehe `break`.
**`lisp_print`** — Zeige die Argumente und Ruckgabewerte in der Lisp-Syntax an.
**info** — Gebe `-> true` beim Eintritt in und Austritt aus einer Funktion aus.
**`errorcatch`** — Catch errors, giving the option to signal an error,
 retry the function call, or specify a return value.














Es konnen bedingte Optionen fur die Ablaufverfolgung definiert werden.  Dazu
wird eine Option zusammen mit einer Aussagefunktion angegeben.  Die Argumente 
der Aussagefunktion fur eine bedingte Option sind immer 
`[level, direction, function, item]`.  `level` ist die Rekursionstiefe
der Funktion, `direction` enthalt die Werte `enter` oder 
`exit`, `function` ist der Name der Funktion und `item` ist eine 
Liste der Argumente oder der Ruckgabewert beim Verlassen der Funktion.




Dies ist ein Beispiel fur eine Ablaufverfolgung ohne Bedingungen:



```maxima
(%i1) ff(n) := if equal(n, 0) then 1 else n * ff(n - 1)$

(%i2) trace (ff)$

(%i3) trace_options (ff, lisp_print, break)$

(%i4) ff(3);
```





In diesem Fall wird eine Aussagefunktion fur eine bedingte Ablaufverfolgung
angegeben:



```maxima
(%i5) trace_options (ff, break(pp))$

(%i6) pp (level, direction, function, item) := block (print (item),
    return (function = 'ff and level = 3 and direction = exit))$

(%i7) ff(6);
```

See also: `break`.

<!-- category: Other -->
<!-- keywords: untimer -->
<!-- signatures: untimer(f_1, ..., f_n), untimer() -->
### Function: untimer (f_1, ..., f_n)

`untimer` beendet die Aufzeichnung von Informationen zur Ausfuhrungszeit
fur die Funktionen *f_1*, ..., *f_n*.





Wird `untimer` ohne Argument aufgerufen, wird die Aufzeichnung fur alle
Funktionen beendet.








Die aufgezeichneten Informationen zu einer Funktion `f` konnen mit dem
Kommando `timer_info(f)` auch dann abgerufen werden, wenn zuvor mit dem 
Kommando `untimer(f)` die Aufzeichnung fur die Funktion `f` beendet 
wurde.  Jedoch werden die aufgezeichneten Informationen fur die Funktion 
`f` nicht mit dem Kommando `timer_info()` angezeigt.  Das Kommando
`timer(f)` setzt alle aufgezeichneten zuruck und startet die Aufzeichnung
fur die Funktion erneut.

<!-- category: Other -->
<!-- keywords: untrace -->
<!-- signatures: untrace(f_1, ..., f_n), untrace() -->
### Function: untrace (f_1, ..., f_n)

Beendet die Ablaufverfolgung fur die Funktionen *f_1*, ..., *f_n*. 
Das Kommando `untrace()` beendet die Ablaufverfolgung fur alle 
Funktionen.




`untrace` gibt eine Liste der Funktionen zuruck, fur die die 
Ablaufverfolgung beendet wurde.

