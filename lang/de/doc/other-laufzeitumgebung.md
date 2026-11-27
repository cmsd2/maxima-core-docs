## Laufzeitumgebung

<!-- category: Other -->
<!-- keywords: absolute_real_time -->
<!-- signatures: absolute_real_time() -->
### Function: absolute_real_time ()

Gibt die Sekunden zuruck, die seit dem 1. Januar 1990 UTC verstrichen 
sind.  Die Ruckgabe ist eine ganze Zahl.


Siehe auch `elapsed_real_time` und `elapsed_run_time`.



Beispiel:



```maxima
(%i1) absolute_real_time ();
(%o1)                      3502559124
(%i2) truncate(1900+absolute_real_time()/(365.25*24*3600));
(%o2)                         2010
```

See also: `elapsed_real_time`, `elapsed_run_time`.

<!-- category: Other -->
<!-- keywords: elapsed_real_time -->
<!-- signatures: elapsed_real_time() -->
### Function: elapsed_real_time ()

Gibt die Sekunden zuruck, die seit dem letzten Start von Maxima verstrichen 
sind.  Die Ruckgabe ist eine Gleitkommazahl.


Siehe auch `absolute_real_time` und `elapsed_run_time`.


Beispiel:



```maxima
(%i1) elapsed_real_time ();
(%o1)                       2.559324
(%i2) expand ((a + b)^500)$
(%i3) elapsed_real_time ();
(%o3)                       7.552087
```

See also: `absolute_real_time`, `elapsed_run_time`.

<!-- category: Other -->
<!-- keywords: elapsed_run_time -->
<!-- signatures: elapsed_run_time() -->
### Function: elapsed_run_time ()

Gibt eine Schatzung der Zeit in Sekunden zuruck, die Maxima fur 
Berechnungen seit dem letzten Start benotigt hat.  Der Ruckgabewert ist
eine Gleitkommazahl.


Siehe auch `absolute_real_time` und `elapsed_real_time`.


Beispiel:



```maxima
(%i1) elapsed_run_time ();
(%o1)                         0.04
(%i2) expand ((a + b)^500)$
(%i3) elapsed_run_time ();
(%o3)                         1.26
```

See also: `absolute_real_time`, `elapsed_real_time`.

<!-- category: Other -->
<!-- keywords: maxima_tempdir -->
<!-- signatures: maxima_tempdir -->
### Variable: maxima_tempdir

Die Systemvariable `maxima_tempdir` enthalt das Verzeichnis, in dem
Maxima temporare Dateien ablegt.  Insbesondere werden temporare
Grafikausgaben von Funktionen wie `plot2d` und `plot3d` in diesem
Verzeichnis abgelegt.  Der Standardwert von `maxima_tempdir` ist das
Home-Verzeichnis des Nutzers, sofern Maxima dieses feststellen kann.
Andernfalls initialisiert Maxima die Systemvariable `maxima_tempdir` mit
einer geeigneten Annahme.


Der Systemvariablen `maxima_tempdir` kann eine Zeichenkette zugewiesen 
werden, die ein Verzeichnis bezeichnet.

See also: `plot2d`, `plot3d`.

<!-- category: Other -->
<!-- keywords: maxima_userdir -->
<!-- signatures: maxima_userdir -->
### Variable: maxima_userdir

Die Systemvariable `maxima_userdir` enthalt ein Verzeichnis, das Maxima
durchsucht, um Maxima- oder Lisp-Dateien zu finden.  Der Standardwert der
Systemvariablen `maxima_userdir` ist ein Unterverzeichnis des
Home-Verzeichnis des Nutzers, sofern Maxima dieses bestimmen kann.  Ansonsten
initialisiert Maxima die Systemvariable `maxima_userdir` mit einer
geeigneten Annahme.  Dieses Verzeichnis ist zum Beispiel geeignet, um die
Initialisisierungsdateien `maxima-init.mac` und `maxima-init.lisp`
abzulegen.


Maxima sucht in weiteren Verzeichnissen nach Dateien.  Die vollstandige Liste
der Suchverzeichnisse ist den Variablen `file_search_maxima` und
`file_search_lisp` enthalten.


Der Systemvariablen `maxima_userdir` kann eine Zeichenkette zugewiesen 
werden, die ein Verzeichnis bezeichnet.  Wenn der Wert von `maxima_userdir`
geandert wird, werden die Variablen `file_search_maxima` und
`file_search_lisp` nicht automatisch angepasst.

See also: `file_search_maxima`, `file_search_lisp`.

<!-- category: Other -->
<!-- keywords: room -->
<!-- signatures: room(), room(true), room(false) -->
### Function: room ()

Gibt eine Beschreibung der Speicherplatznutzung aus.  Die Darstellung und der
Inhalt der Beschreibung hangt von dem Maxima zugrunde liegendem Lisp ab.  Mit
den Argumenten `true` und `false` kann der Umfang der auszugebenden
Information kontrolliert werden, sofern die Option vom verwendeten Lisp
unterstutzt wird.  Mit dem Argument `true` wird die umfangreichste
Darstellung ausgegeben und mit dem Argument `false` die kurzeste.



Beispiel:


Das folgende Beispiel zeigt die Ausgabe auf einem Linux-System mit der 
Lisp-Im­ple­men­tie­rung SBCL 1.0.45.



```maxima
(%i1) room(false);
Dynamic space usage is:   63,719,856 bytes.
Read-only space usage is:      3,512 bytes.
Static space usage is:         2,256 bytes.
Control stack usage is:        1,440 bytes.
Binding stack usage is:          184 bytes.
Control and binding stack usage is for the current thread only.
Garbage collection is currently enabled.
(%o2)                         false
```

<!-- category: Other -->
<!-- keywords: sstatus -->
<!-- signatures: sstatus(keyword, item) -->
### Function: sstatus (keyword, item)

Hat das Argument *keyword* den Wert `feature`, wird das Argument
*item* der internen Lisp-Eigenschaftsliste `*features*` hinzugefugt.
Das Kommando `status(feature, item)` hat dann das Ergebnis `true`.
Hat das Argument *keyword* den Wert `nofeature`, wird das Argument
*item* von der internen Lisp-Eigenschaftsliste `*features*` entfernt.


Siehe auch die Funktion `status`.

See also: `status`.

<!-- category: Other -->
<!-- keywords: status -->
<!-- signatures: status(feature), status(feature, item) -->
### Function: status (feature)

Das Kommando `status(feature)` gibt die interne Lisp-Eigenschaftsliste
`*features*` zuruck.  `status(feature,item)` gibt `true`
zuruck, wenn das Argument *item* in der internen Lisp-Eigenschaftsliste
`*features*` enthalten ist.  Ansonsten ist die Ruckgabe `false`.
`status` wertet die Argumente nicht aus.  Eine Systemeigenschaft
*item*, die Sonderzeichen wie `-` oder `*` enthalt, muss als
Zeichenkette angegeben werden.


Siehe auch die Funktion `sstatus`.


Die Lisp-Variable `*features*` steht in keinem Zusammenhang mit der
Maxima-Systemvariablen `features`, die eine Liste mit mathematischen
Eigenschaften enthalt, die Funktionen und Variablen erhalten konnen.


Beispiel:


Das folgende Beispiel zeigt die Ausgabe fur ein Linux-System mit SBCL als
Lisp.  Die Ausgabe ist abgekurzt.



```maxima
(%i1) status(feature);
(%o1) [sb-bsd-sockets-addrinfo, asdf2, asdf, cl, mk-defsystem, 
cltl2, ansi-cl, common-lisp, sbcl, ...]

(%i2) status(feature,"ansi-cl");
(%o2)                         true
```

See also: `sstatus`, `features`.

<!-- category: Other -->
<!-- keywords: system -->
<!-- signatures: system(command) -->
### Function: system (command)

`system(command)` fuhrt das Kommando *command* in einem eigenen 
Prozess aus.  Das Kommando wird an die Standard-Shell ubergeben.
`system` wird nicht von allen Betriebssystemen unterstutzt, steht aber im
Allgemeinen unter Unix oder Unix ahnlichen Betriebssystemen zur Verfugung.

<!-- category: Other -->
<!-- keywords: time -->
<!-- signatures: time(%o1, %o2, %o3, ...) -->
### Function: time (%o1, %o2, %o3, ...)

Gibt eine Liste mit den Ausfuhrungszeiten zuruck, die benotigt wurden, um
die Ergebnisse `%o1`, `%o2`, `%o3`, ... zu berechnen.
Die Argumente der Funktion `time` konnen nur Ausgabemarken sein.  Fur 
andere Argumente ist das Ergebnis `unknown`.


Siehe die Optionsvariable `showtime`, um die Ausfuhrungszeiten fur 
jede einzelne Berechnung anzuzeigen.


Beispiel:


Die Zeit fur die Berechnung der Fakultat einer großen ganzen Zahl wird 
mit `time` ausgegeben.



```maxima
(%i1) factorial(100000)$

(%i2) time(%o1);
(%o2)                        [7.589]
```

See also: `showtime`.

<!-- category: Other -->
<!-- keywords: timedate -->
<!-- signatures: timedate() -->
### Function: timedate ()

Gibt eine Zeichenkette zuruck, die das aktuelle Datum und die aktuelle Zeit 
enthalt.  Die Zeichenkette hat das Format `yyyy-mm-dd HH:MM:SS (GMT-n)`.


Beispiel:



```maxima
(%i1) timedate();
(%o1)               2010-12-28 21:56:32+01:00
```

