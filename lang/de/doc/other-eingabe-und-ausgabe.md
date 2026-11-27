## Eingabe und Ausgabe

<!-- category: Other -->
<!-- keywords: appendfile -->
<!-- signatures: appendfile(filename) -->
### Function: appendfile (filename)

Startet wie die Funktion `writefile` eine Aufzeichnung aller Ein- und 
Ausgaben der Konsole.  Die Ein- und Ausgaben werden in die Datei *filename* 
geschrieben.  Im Unterschied zu `writefile` werden die Daten immer an eine 
existierende Datei angehangt, wenn diese existiert.  Existiert die Datei 
nicht, wird diese angelegt.


Die Funktion `closefile` beendet die Aufzeichnung.

See also: `writefile`, `closefile`.

<!-- category: Other -->
<!-- keywords: batch -->
<!-- signatures: batch(filename), batch(filename, option) -->
### Function: batch (filename)

Das Kommando `batch(filename)` liest Maxima-Ausdrucke aus der Datei 
*filename* ein, wertet diese aus und gibt die Ergebnisse auf der Konsole 
aus.  `batch` sucht die Datei *filename* in den Verzeichnissen, die in 
der Liste `file_search_maxima` enthalten sind.  Siehe auch die Funktion
`file_search`.


`batch(filename, demo)` entspricht dem Kommando
`demo(filename)`.  `batch` sucht fur diesen Fall die Datei in
der Liste der Verzeichnisse `file_search_demo`.  Siehe auch die Funktion
`demo`.


`batch(filename, test)` entspricht dem Kommando
`run_testsuite` mit der Option `display_all=true`.  Im Unterschied zur
Funktion `run_testsuite` sucht die Funktion `batch` die Datei 
*filename* in den Verzeichnissen der Liste `file_search_maxima` und 
nicht in der Liste `file_search_tests`.


Die Maxima-Ausdrucke in der Datei werden wie auf der Konsole mit den 
Zeichen `;` oder `$` beendet.  Die Systemvariable `%` und die
Funktion `%th` beziehen sich auf vorhergehende Zeilen in der Datei.  Die
Datei kann `:lisp`-Unterbrechungskommandos enthalten.  Leerzeichen, 
Tabulatoren, Zeilenschaltungen und Kommentare werden ignoriert.  Eine geeignete 
Datei kann mit einem Texteditor oder der Funktion `stringout` erstellt 
werden.


Den Ein- und Ausgaben werden jeweils Ein- und Ausgabemarken zugewiesen.  Tritt 
wahrend der Auswertung eines Ausdrucks ein Fehler auf, wird das Einlesen der 
Datei abgebrochen.  Werden Eingaben vom Nutzer benotigt, wie zum Beispiel bei
Fragen der Funktionen `asksign` oder `askinteger`, dann wartet 
`batch` auf die Antworten, um dann die Verarbeitung der Datei fortzusetzen.


Die Verarbeitung von `batch` kann durch die Eingabe von `control-C` 
abgebrochen werden.  Die weitere Reaktion auf einen Abbruch mit `control-C`
hangt von der Lisp-Implementation ab.


`batch` wertet die Argumente aus.  `batch` gibt den Namen der Datei
*filename* als Zeichenkette zuruck, wenn die Funktion ohne zweites 
Argument oder mit der Option `demo` aufgerufen wird.  Wird die Funktion mit 
der Option `test` aufgerufen, ist die Ruckgabe eine leere Liste `[]` 
oder eine Liste, die *filename* und die Nummern der fehlgeschlagenen Tests
enthalt.


Siehe auch die Funktionen `load` und `batchload`, um Dateien
zu laden, sowie die Funktionen `run_testsuite` und `demo`.

See also: `file_search_maxima`, `file_search`, `file_search_demo`, `demo`, `run_testsuite`, `file_search_tests`, `stringout`, `load`, `batchload`.

<!-- category: Other -->
<!-- keywords: batchload -->
<!-- signatures: batchload(filename) -->
### Function: batchload (filename)

Liest Ausdrucke aus der Datei *filename* ein und wertet diese aus, ohne 
die eingelesenen und ausgewerteten Ausdrucke anzuzeigen und ohne Zuweisung von
Eingabe- und Ausgabemarken.  Die Ausgabe von Fehlermeldungen oder sonstigem 
Text, der von Funktionen ausgegeben wird, wird nicht unterdruckt.


Die Systemvariable `%` und die Funktion `%th` beziehen sich auf die
letzte Eingabe auf der Konsole und nicht auf Zeilen oder Ergebnisse der Datei.
Im Gegensatz zur Funktion `batch` darf eine Datei, die von `batchload`
geladen wird, keine `:lisp`-Unterbrechungskommandos enthalten.


`batchload` gibt eine Zeichenkette mit dem Pfad der Datei *filename* 
zuruck.  Siehe auch die Funktionen `batch` und `load`, um 
Dateien zu laden.

See also: `batch`, `load`.

<!-- category: Other -->
<!-- keywords: closefile -->
<!-- signatures: closefile() -->
### Function: closefile ()

Beendet eine Aufzeichnung, die von den Funktionen `writefile` oder 
`appendfile` gestartet wurde, und schließt die Ausgabedatei.

See also: `writefile`, `appendfile`.

<!-- category: Other -->
<!-- keywords: file_output_append -->
<!-- signatures: file_output_append -->
### Variable: file_output_append

Standardwert: `false`


Die Optionsvariable `file_output_append` kontrolliert, ob die Funktionen 
`save`, `stringout` oder `with_stdout`, die in eine Datei 
schreiben, diese loschen und neu anlegen oder die Daten anhangen.  Wenn 
`file_output_append` den Wert `true` hat, werden die Daten an die 
existierende Datei angehangt.  Ansonsten wird eine neue Datei erstellt.


Plot-Funktionen und der Ubersetzer erstellen grundsatzlich neue Dateien und
die Funktionen `tex` und `appendfile` hangen die Ausgabe immer an 
eine bestehende Datei an.

See also: `save`, `stringout`, `with_stdout`, `tex`, `appendfile`.

<!-- category: Other -->
<!-- keywords: file_search -->
<!-- signatures: file_search(filename), file_search(filename, pathlist) -->
### Function: file_search (filename)

`file_search` sucht die Datei *filename* und gibt den Pfad als eine
Zeichenkette zuruck, wenn die Datei gefunden wurde.  Ansonsten wird 
`false` zuruckgegeben.  `file_search(filename)` sucht in den 
Standardsuchverzeichnissen, die mit den Optionsvariablen 
`file_search_maxima`, `file_search_lisp` und 
`file_search_demo` spezifiziert werden.


`file_search` pruft zuerst, ob die Datei `filename` existiert.  Dann
pruft `file_search`, ob die Datei anhand von Mustern im Dateinamen 
gefunden werden kann.  Siehe `file_search_maxima` fur die Suche von
Dateien.


Das Argument *filename* kann ein Name mit einer Pfadangabe oder allein der
Dateiname sein.  Sind in den Suchverzeichnissen Dateinamen mit Mustern 
enthalten, kann die Datei auch ohne Endung angegeben werden.  Zum Beispiel 
finden die folgenden Kommandos dieselbe Datei, wenn 
`/home/wfs/special/###.mac` in der Liste `file_search_maxima` 
enthalten ist:



```maxima
file_search ("/home/wfs/special/zeta.mac");
file_search ("zeta.mac");
file_search ("zeta");
```


`file_search(filename, pathlist)` sucht nur in den
Verzeichnissen *pathlist*.  Das Argument *pathlist* uberschreibt die
Standardsuchverzeichnisse.  Auch ein einzelnes Verzeichnis muss als eine Liste 
ubergeben werden.


Die Standardsuchverzeichnisse konnen modifiziert werden.  Siehe dazu auch
`file_search_maxima`.


`file_search` wird von der Funktion `load` mit den Verzeichnislisten
`file_search_maxima` und `file_search_lisp` aufgerufen.


Siehe auch `file_search_cache`.

See also: `file_search_maxima`, `file_search_lisp`, `file_search_demo`, `load`, `file_search_cache`.

<!-- category: Other -->
<!-- keywords: file_search_cache -->
<!-- signatures: file_search_cache -->
### Variable: file_search_cache

Standardwert: `auto`


`file_search_cache` steuert die Verwendung eines Caches durch
`file_search`, um die Suche nach Dateien zu beschleunigen.


Wenn `file_search_cache` auf `auto` gesetzt ist (Standardwert), wird
der Cache aktiviert, wenn eine einmalige Prufung ergibt, dass das System
(Lisp-Implementation und Dateisystem) die Voraussetzungen erfullt.  Die
Verwendung des Caches kann erzwungen werden, indem `file_search_cache` auf
`true` gesetzt wird, doch dies wird nicht empfohlen.  Der Wert `false`
verhindert die Verwendung des Caches.


Siehe auch `file_search`.

See also: `file_search`.

<!-- category: Other -->
<!-- keywords: file_search_ignore_dirs -->
<!-- signatures: file_search_ignore_dirs -->
### Variable: file_search_ignore_dirs

Standardwert: `[".bzr", ".git", ".github", ".hg", ".svn", ".eclipse", ".idea", ".vs", ".vscode", ".zed"]`


`file_search_ignore_dirs` enthalt Verzeichnisnamen (nicht komplette Pfade),
die bei der Suche nach Dateien ignoriert werden, um die Suche zu beschleunigen.


Siehe auch `file_search`.

See also: `file_search`.

<!-- category: Other -->
<!-- keywords: file_search_maxima, file_search_lisp, file_search_demo, file_search_usage, file_search_tests -->
<!-- signatures: file_search_lisp, file_search_demo, file_search_usage, file_search_tests -->
### Variable: file_search_maxima

Diese Optionsvariablen bezeichnen Listen mit Verzeichnissen, die von Funktionen 
wie `load` und `demo` durchsucht werden, um eine Datei zu finden.  Die
Standardwerte bezeichnen verschiedene Verzeichnisse der Maxima-Installation.


Diese Variablen konnen modifiziert werden, indem die Standardwerte ersetzt 
oder weitere Verzeichnisse angehangt werden.  Zum Beispiel wird im Folgenden 
der Standardwert der Optionsvariablen `file_search_maxima` ersetzt:



```maxima
file_search_maxima: ["/usr/local/foo/###.mac",
    "/usr/local/bar/###.mac"]$
```


In diesem Beispiel werden zwei weitere Verzeichnisse zu der Optionsvariablen 
`file_search_maxima` hinzugefugt:



```maxima
file_search_maxima: append (file_search_maxima,
    ["/usr/local/foo/###.mac", "/usr/local/bar/###.mac"])$
```


Soll eine erweiterte Liste der Suchverzeichnisse nach jedem Start von Maxima
zur Verfugung stehen, kann das obige Kommando in die Datei
`maxima-init.mac` aufgenommen werden.


Mehrere Dateiendungen und Pfade konnen mit Wildcard-Konstruktionen 
spezifiziert werden.  Eine Zeichenkette `###` wird durch einen Dateinamen
ersetzt.  Werden mehrere Zeichenketten durch Kommata getrennt und mit 
geschweiften Klammern angegeben wie zum Beispiel `{foo, bar, baz}`, 
expandiert die Liste in mehrere Zeichenketten.  Das folgende Beispiel expandiert
fur `neumann` 



```maxima
"/home/{wfs,gcj}/###.{lisp,mac}"
```


in `/home/wfs/neumann.lisp`, `/home/gcj/neumann.lisp`, 
`/home/wfs/neumann.mac` und `/home/gcj/neumann.mac`.

See also: `load`, `demo`.

<!-- category: Other -->
<!-- keywords: file_type -->
<!-- signatures: file_type(filename) -->
### Function: file_type (filename)

Gibt eine Vermutung uber den Typ der Datei *filename* zuruck.  Es 
wird nur die Dateiendung betrachtet.


Die Ruckgabe ist das Symbol `maxima` oder `lisp`, wenn die
Dateiendung einen der Werte der Optionsvariablen `file_type_maxima` oder
der Optionsvariablen `file_type_lisp` entspricht.  Ansonsten ist die
Ruckgabe das Symbol `object`.


Siehe auch die Funktion `pathname_type`.

See also: `file_type_maxima`, `file_type_lisp`, `pathname_type`.

<!-- category: Other -->
<!-- keywords: file_type_lisp -->
<!-- signatures: file_type_lisp -->
### Variable: file_type_lisp

Standardwert:  `[l, lsp, lisp]`


Die Optionsvariable `file_type_lisp` enthalt die Dateiendungen, die
Maxima als die Bezeichnung fur eine Lisp-Datei annimmt.


Siehe auch die Funktion `file_type`.

See also: `file_type`.

<!-- category: Other -->
<!-- keywords: file_type_maxima -->
<!-- signatures: file_type_maxima -->
### Variable: file_type_maxima

Standardwert:  `[mac, mc, demo, dem, dm1, dm2, dm3, dmt]`


Die Optionsvariable `file_type_maxima` enthalt die Dateiendungen, die
Maxima als die Bezeichnung fur eine Maxima-Datei annimmt.


Siehe auch die Funktion `file_type`.

See also: `file_type`.

<!-- category: Other -->
<!-- keywords: filename_merge -->
<!-- signatures: filename_merge(path, filename) -->
### Function: filename_merge (path, filename)

Setzt einen Pfad aus *path* und *filename* zusammen.  Endet *path*
mit einer Zeichenkette der Form `###.something`, wird diese 
Zeichenkette durch `filename.something` ersetzt.  Ansonsten 
wird der Endbestandteil durch *filename* ersetzt.


Die Ruckgabe ist ein Lisp-Dateiname.


Beispiele:



```maxima
(%i1) filename_merge("user/", "myfile");
(%o1)                      user/myfile

(%i2) filename_merge("user/###.lisp", "myfile");
(%o2)                   user/myfile.lisp
```

<!-- category: Other -->
<!-- keywords: get_tex_environment, set_tex_environment -->
<!-- signatures: get_tex_environment(op), set_tex_environment(op, before, after) -->
### Function: get_tex_environment (op)

Customize the TeX environment output by `tex`.
As maintained by these functions, the TeX environment comprises two strings:
one is printed before any other TeX output, and the other is printed after.


Only the TeX environment of the top-level operator in an expression
is output; TeX environments associated with other operators are ignored.


`get_tex_environment` returns the TeX enviroment which is applied
to the operator *op*; returns the default if no other environment
has been assigned.


`set_tex_environment` assigns the TeX environment for the operator 
*op*.


Examples:



```maxima
(%i1) get_tex_environment (":=");
(%o1) [
\begin{verbatim}
, ;
\end{verbatim}
]
(%i2) tex (f (x) := 1 - x);

\begin{verbatim}
f(x):=1-x;
\end{verbatim}

(%o2)                         false
(%i3) set_tex_environment (":=", "$$", "$$");
(%o3)                       [$$, $$]
(%i4) tex (f (x) := 1 - x);
$$f(x):=1-x$$
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: get_tex_environment_default, set_tex_environment_default -->
<!-- signatures: get_tex_environment_default(), set_tex_environment_default(before, after) -->
### Function: get_tex_environment_default ()

Customize the TeX environment output by `tex`.
As maintained by these functions, the TeX environment comprises two strings:
one is printed before any other TeX output, and the other is printed after.


`get_tex_environment_default` returns the TeX environment which is
applied to expressions for which the top-level operator has no
specific TeX environment (as assigned by `set_tex_environment`).


`set_tex_environment_default` assigns the default TeX environment.


Examples:



```maxima
(%i1) get_tex_environment_default ();
(%o1)                       [$$, $$]
(%i2) tex (f(x) + g(x));
$$g\left(x\right)+f\left(x\right)$$
(%o2)                         false
(%i3) set_tex_environment_default ("\\begin{equation}
", "
\\end{equation}");
(%o3) [\begin{equation}
, 
\end{equation}]
(%i4) tex (f(x) + g(x));
\begin{equation}
g\left(x\right)+f\left(x\right)
\end{equation}
(%o4)                         false
```

<!-- category: Other -->
<!-- keywords: load -->
<!-- signatures: load(filename) -->
### Function: load (filename)

Wertet die Ausdrucke in der Datei *filename* aus, wodurch die Variablen,
Funktionen und andere Objekte in Maxima geladen werden.  Alle bisher zugewiesen
Variablen und Definitionen werden uberschrieben.  Um die Datei zu finden, wird
von `load` die Funktion `file_search` mit den Verzeichnislisten
`file_search_maxima` und `file_search_lisp` aufgerufen.  Ist 
`load` erfolgreich, wird der Dateiname zuruckgegeben.  Ansonsten gibt
`load` eine Fehlermeldung aus.


`load` verarbeitet Dateien mit Lisp-Code oder Maxima-Code.  Dateien, die 
mit den Funktionen `save`, `translate_file` und
`compile_file` erstellt wurden, enthalten Lisp-Code.  Dateien, die mit
`stringout` erstellt wurden, enthalten Maxima-Code.  Die Ausgabedateien
dieser Funktionen konnen mit `load` geladen werden.  `load` ruft die
Funktion `loadfile` auf, um Lisp-Dateien und `batchload` auf, um 
Maxima-Da­tei­en zu verarbeiten.


`load` erkennt keine `:lisp`-Unterbrechungskommandos in 
Maxima-Dateien.  Die Systemvariablen `_`, `__` und `%` und 
die Funktion `%th` behalten jeweils ihren letzten Wert vor dem Aufruf von 
`load`.


Siehe auch die Funktionen `loadfile`, `batch`, 
`batchload` und `demo`.  `loadfile` verarbeitet 
Lisp-Da­tei­en.  `batch`, `batchload` und `demo` verarbeiten 
Maxima-Dateien.


Siehe `file_search` fur mehr Informationen, wie Maxima Dateien in 
Verzeichnissen findet.  `load` wertet die Argumente aus.

See also: `file_search`, `file_search_maxima`, `file_search_lisp`, `save`, `translate_file`, `compile_file`, `stringout`, `loadfile`, `batchload`, `_`, `__`, `%`, `%th`, `batch`, `demo`.

<!-- category: Other -->
<!-- keywords: load_pathname -->
<!-- signatures: load_pathname -->
### Variable: load_pathname

Standardwert: `false`


Wird eine Datei mit den Funktionen `load`, `loadfile` oder
`batchload` geladen, enthalt die Systemvariable `load_pathname`
den Namen der Datei.  Der Wert der Systemvariablen kann in der Datei, die 
geladen wird, ausgelesen werden.


Beispiele:


Ist eine Batch-Datei mit den Namen `test.mac` in dem Verzeichnis


```maxima
"/home/dieter/workspace/mymaxima/temp/"
```
 

abgelegt und enthalt die Datei die folgenden Befehle



```maxima
print("The value of load_pathname is: ", load_pathname)$
print("End of batchfile")$
```


dann wird das Folgende ausgegeben:



```maxima
(%i1) load("/home/dieter/workspace/mymaxima/temp/test.mac")$
The value of load_pathname is:  
              /home/dieter/workspace/mymaxima/temp/test.mac 
End of batchfile
```

See also: `load`, `loadfile`, `batchload`.

<!-- category: Other -->
<!-- keywords: loadfile -->
<!-- signatures: loadfile(filename) -->
### Function: loadfile (filename)

Ladt die Datei *filename* und wertet die Lisp-Ausdrucke in der Datei 
aus.  `filename` ruft nicht `file_search` auf, um eine Datei zu 
finden.  Daher muss `filename` ein voll­stan­di­ger Dateiname sein.


`loadfile` kann Dateien verarbeiten, die mit den Funktionen 
`save`, `translate_file` und `compile_file` erzeugt wurden.

See also: `file_search`, `save`, `translate_file`, `compile_file`.

<!-- category: Other -->
<!-- keywords: loadprint -->
<!-- signatures: loadprint -->
### Variable: loadprint

Standardwert: `true`


`loadprint` kontrolliert, ob Meldungen ausgegeben werden, wenn eine Datei
geladen wird.



- * 
Hat `loadprint` den Wert `true`, wird immer eine Meldung 
      ausgegeben.
- * 
Hat `loadprint` den Wert `'loadfile`, wird eine Meldung 
      ausgegeben, wenn die Datei mit der Funktion `loadfile` geladen wird.
- * 
Hat `loadprint` den Wert `'autoload`, wird eine Meldung 
      ausgegeben, wenn eine Datei automatisch geladen wird.
- * 
Hat `loadprint` den Wert `false`, werden keine Meldungen beim 
      Laden von Dateien ausgegeben.

See also: `loadfile`.

<!-- category: Other -->
<!-- keywords: pathname_directory, pathname_name, pathname_type -->
<!-- signatures: pathname_directory(pathname), pathname_name(pathname), pathname_type(pathname) -->
### Function: pathname_directory (pathname)

Diese Funktionen geben die Bestandteile eines Pfadnamens zuruck.


Beispiele:



```maxima
(%i1) pathname_directory("/home/dieter/maxima/changelog.txt");
(%o1)                 /home/dieter/maxima/
(%i2) pathname_name("/home/dieter/maxima/changelog.txt");
(%o2)                       changelog
(%i3) pathname_type("/home/dieter/maxima/changelog.txt");
(%o3)                          txt
```

<!-- category: Other -->
<!-- keywords: printfile -->
<!-- signatures: printfile(path) -->
### Function: printfile (path)

Druckt eine Datei mit dem Namen *path* auf der Konsole aus.  *path* kann
ein Symbol oder eine Zeichenkette sein.  `printfile` sucht die Datei in den 
Verzeichnissen, die in der Optionsvariablen `file_search_usage` enthalten 
sind.


`printfile` gibt *path* zuruck, wenn die Datei existiert.

See also: `file_search_usage`.

<!-- category: Other -->
<!-- keywords: save -->
<!-- signatures: save(filename, name_1, name_2, name_3, ...), save(filename, values, functions, labels, ...), save(filename, [m, n]), save(filename, name_1=expr_1, ...), save(filename, all), save(filename, name_1=expr_1, name_2=expr_2, ...) -->
### Function: save (filename, name_1, name_2, name_3, ...)

Speichert die aktuellen Werte von *name_1*, *name_2*, *name_3*, 
..., in die Datei *filename*.  Die Argumente sind die Namen von 
Variablen, Funktionen oder anderen Objekten.  Argumente, die keinen Wert haben, 
werden ignoriert.  `save` gibt den Namen der Datei `filename` 
zuruck.


`save` speichert die Daten in einem Lisp-Format.  Die gespeicherten Daten
konnen mit dem Kommando `load(filename)` zuruckgelesen werden.
Siehe `load`.


Die Optionsvariable `file_output_append` kontrolliert, ob `save` die
Daten an die Ausgabedatei anhangt, wenn diese bereits existiert, oder die 
Ausgabedatei zuvor loscht.  Hat `file_output_append` den Wert 
`true`, werden die Daten angehangt.  Ansonsten wird die Datei geloscht
und neu angelegt, wenn diese bereits existiert.  Existiert die Ausgabedatei
noch nicht, wird diese angelegt.


`save(filename, values, functions, labels, ...)` speichert die
Werte aller Ein­tra­ge der Listen `values`, `functions`, 
`labels`, u.s.w. in die Ausgabedatei.  Es kann jede der vorhandenen
Informationslisten, die in der Systemvariablen `infolists` enthalten ist, 
als Argument ubergeben werden.  `values` enthalt zum Beispiel alle vom
Nutzer definierten Variablen.


`save(filename, [m, n])` speichert die Werte der Eingabe-
und Ausgabemarken von *m* bis *n*.  *m* und *n* mussen ganze 
Zahlen sein.  Die Eingabe- und Ausgabemarken konnen auch einzeln gespeichert 
werden, zum Beispiel mit dem Kommando `save("foo.1", %i42, %o42)`.
`save(filename, labels)` speichert alle Eingabe- und Ausgabemarken.
Beim Zurucklesen der Marken werden vorhandene Werte uberschrieben.


`save(filename, name_1 = expr_1, name_2 = expr_2, ...)` speichert die Werte *expr_1*, *expr_2*, ..., 
unter den Namen *name_1*, *name_2*, ... ab.  Dies kann  nutz­lich
sein, um zum Beispiel die Werte von Marken unter einem neuen Namen 
abzuspeichern.  Die rechte Seite der Gleichungen kann ein beliebiger 
ausgewerteter Ausdruck sein.  Die neuen Namen werden der aktuellen Sitzung nicht
hinzugefugt und nur in der Ausgabedatei gespeichert.


Die verschiedenen Moglichkeiten der Funktion `save`, konnen
miteinander kombiniert werden.  Das Kommando
`save(filename, aa, bb, cc=42, functions, [11,17])` ist dafur ein
Beispiel.


`save(filename, all)` speichert den aktuellen Zustand von Maxima
in eine Ausgabedatei.  Eingeschlossen sind alle nutzerdefinierten Variablen, 
Funktionen oder Arrays, einschließlich automatischer Definitionen.  Die 
gespeicherten Daten enthalten auch die Werte von geanderten System- oder
Optionsvariablen.  Siehe dazu auch `myoptions`.


`save` wertet das Argument *filename* aus.  Alle anderen Argumente
werden nicht ausgewertet.

See also: `load`, `file_output_append`, `myoptions`.

<!-- category: Other -->
<!-- keywords: stringout -->
<!-- signatures: stringout(filename, expr_1, expr_2, expr_3, ...), stringout(filename, [m, n]), stringout(filename, input), stringout(filename, functions), stringout(filename, values) -->
### Function: stringout (filename, expr_1, expr_2, expr_3, ...)

`stringout` schreibt Ausdrucke in einem Format in eine Datei, dass 
identisch mit dem Format der Eingabe ist.  Die Datei kann als Eingabedatei fur
die Funktionen `batch` oder `demo` genutzt werden.  Sie kann mit 
einem Texteditor fur jeden Zweck editiert werden.  `stringout` kann
ausgefuhrt werden, wenn das Kommando `writefile` aktiv ist.


Die Optionsvariable `file_output_append` kontrolliert, ob `stringout`
die Daten an die Ausgabedatei anhangt, wenn diese bereits existiert oder die 
Ausgabedatei zuvor loscht.  Hat `file_output_append` den Wert 
`true`, werden die Daten angehangt, wenn die Datei bereits existiert.  
Ansonsten wird die Datei geloscht und neu angelegt.  Existiert die 
Ausgabedatei noch nicht, wird diese angelegt.


Die allgemeine Form von `stringout` schreibt die Werte eines oder mehrerer
Ausdrucke in die Ausgabedatei.  Ist ein Ausdruck eine Variable, wird nur der
Wert der Variablen, nicht jedoch der Name der Variablen in die Ausgabedatei 
geschrieben.  Ein nutzlicher Spezialfall ist, dass die Werte der Eingabe- 
und Ausgabemarken (`%i1`, `%i2`, `%i3`, ... und `%o1`, 
`%o2`, `%o3`, ...) in die Datei geschrieben werden konnen.


Hat die Optionsvariable `grind` den Wert `true`, wird die Ausgabe
im Format der Funktion `grind` in die Ausgabedatei geschrieben.  Ansonsten
wird das Format der Funktion `string` fur die Ausgabe genutzt.


`stringout(filename, [m, n])` schreibt die Werte aller
Eingabemarken von *m* bis *n* in die Ausgabedatei.
`stringout(filename, input)` schreibt alle Eingabemarken in die
Ausgabedatei.  `stringout(filename, functions)` schreibt alle vom 
Nutzer definierten Funktionen, die in der Informationsliste `functions` 
enthalten sind, in die Ausgabedatei.


`stringout(filename, values)` schreibt alle benuzterdefinierten
Variablen, die in der Informationsliste `values` enthalten sind, in die
Ausgabedatei.  Die Variablen werden als eine Zuweisung, mit dem Namen der 
Variablen, dem Zuweisungsoperator `:` und dem Wert in die Datei 
geschrieben.  Im Unterschied dazu, speichert die allgemeine Form der Funktion
`stringout` die Variablen nicht als Zuweisung.

See also: `batch`, `demo`, `writefile`, `file_output_append`, `grind`, `string`.

<!-- category: Other -->
<!-- keywords: tex -->
<!-- signatures: tex(expr), tex(expr, destination), tex(expr, false), tex(label), tex(label, destination), tex(label, false) -->
### Function: tex (expr)

Prints a representation of an expression suitable for the TeX document 
preparation system. The result is a fragment of a document, which can be copied
into a larger document but not processed by itself.


`tex (expr)` prints a TeX representation of *expr* on the 
console.


`tex (label)` prints a TeX representation of the expression named by 
*label* and assigns it an equation label (to be displayed to the left of 
the expression). The TeX equation label is the same as the Maxima label.


*destination* may be an output stream or file name. When *destination* 
is a file name, `tex` appends its output to the file. The functions 
`openw` and `opena` create output streams.


`tex (expr, false)` and `tex (label, false)` return their
TeX output as a string.


`tex` evaluates its first argument after testing it to see if it is a 
label. Quote-quote `''` forces evaluation of the argument, thereby 
defeating the test and preventing the label.


See also `texput`.


Examples:



```maxima
(%i1) integrate (1/(1+x^3), x);
                                    2 x - 1
                  2            atan(-------)
             log(x  - x + 1)        sqrt(3)    log(x + 1)
(%o1)      - --------------- + ------------- + ----------
                    6             sqrt(3)          3
(%i2) tex (%o1);
$$-{{\log \left(x^2-x+1\right)}\over{6}}+{{\arctan \left({{2\,x-1
 }\over{\sqrt{3}}}\right)}\over{\sqrt{3}}}+{{\log \left(x+1\right)
 }\over{3}}\leqno{\tt (\%o1)}$$
(%o2)                          (\%o1)
(%i3) tex (integrate (sin(x), x));
$$-\cos x$$
(%o3)                           false
(%i4) tex (%o1, "foo.tex");
(%o4)                          (\%o1)
```


`tex (expr, false)` returns its TeX output as a string.



```maxima
(%i1) S : tex (x * y * z, false);
(%o1) $$x\,y\,z$$
(%i2) S;
(%o2) $$x\,y\,z$$
```

<!-- category: Other -->
<!-- keywords: tex1 -->
<!-- signatures: tex1(e) -->
### Function: tex1 (e)

Returns a string which represents the TeX output for the expressions *e*.
The TeX output is not enclosed in delimiters for an equation or any other 
environment.


Examples:



```maxima
(%i1) tex1 (sin(x) + cos(x));
(%o1)                     \sin x+\cos x
```

<!-- category: Other -->
<!-- keywords: texput -->
<!-- signatures: texput(a, s), texput(a, f), texput(a, s, operator_type), texput(a, [s_1, s_2], matchfix), texput(a, [s_1, s_2, s_3], matchfix) -->
### Function: texput (a, s)

Assign the TeX output for the atom *a*, which can be a symbol or the name 
of an operator.


`texput (a, s)` causes the `tex` function to interpolate 
the string *s* into the TeX output in place of *a*.


`texput (a, f)` causes the `tex` function to call the 
function *f* to generate TeX output. *f* must accept one argument, 
which is an expression which has operator *a*, and must return a string 
(the TeX output). *f* may call `tex1` to generate TeX output for the 
arguments of the input expression.


`texput (a, s, operator_type)`, where *operator_type*
is `prefix`, `infix`, `postfix`, `nary`, or `nofix`,
causes the `tex` function to interpolate *s* into the TeX output in 
place of *a*, and to place the interpolated text in the appropriate 
position.


`texput (a, [s_1, s_2], matchfix)` causes the `tex` 
function to interpolate *s_1* and *s_2* into the TeX output on either 
side of the arguments of *a*. The arguments (if more than one) are separated
by commas.


`texput (a, [s_1, s_2, s_3], matchfix)` causes the 
`tex` function to interpolate *s_1* and *s_2* into the TeX output 
on either side of the arguments of *a*, with *s_3* separating the 
arguments.


Examples:


Assign TeX output for a variable.



```maxima
(%i1) texput (me,"\\mu_e");
(%o1)                         \mu_e
(%i2) tex (me);
$$\mu_e$$
(%o2)                         false
```


Assign TeX output for an ordinary function (not an operator).



```maxima
(%i1) texput (lcm, "\\mathrm{lcm}");
(%o1)                     \mathrm{lcm}
(%i2) tex (lcm (a, b));
$$\mathrm{lcm}\left(a , b\right)$$
(%o2)                         false
```


Call a function to generate TeX output.



```maxima
(%i1) texfoo (e) := block ([a, b], [a, b] : args (e),
  concat ("\\left[\\stackrel{", tex1 (b), 
          "}{", tex1 (a), "}\\right]"))$
(%i2) texput (foo, texfoo);
(%o2)                        texfoo
(%i3) tex (foo (2^x, %pi));
$$\left[\stackrel{\pi}{2^{x}}\right]$$
(%o3)                         false
```


Assign TeX output for a prefix operator.



```maxima
(%i1) prefix ("grad");
(%o1)                         grad
(%i2) texput ("grad", " \\nabla ", prefix);
(%o2)                        \nabla 
(%i3) tex (grad f);
$$ \nabla f$$
(%o3)                         false
```


Assign TeX output for an infix operator.



```maxima
(%i1) infix ("~");
(%o1)                           ~
(%i2) texput ("~", " \\times ", infix);
(%o2)                        \times 
(%i3) tex (a ~ b);
$$a \times b$$
(%o3)                         false
```


Assign TeX output for a postfix operator.



```maxima
(%i1) postfix ("##");
(%o1)                          ##
(%i2) texput ("##", "!!", postfix);
(%o2)                          !!
(%i3) tex (x ##);
$$x!!$$
(%o3)                         false
```


Assign TeX output for a nary operator.



```maxima
(%i1) nary ("@@");
(%o1)                          @@
(%i2) texput ("@@", " \\circ ", nary);
(%o2)                         \circ 
(%i3) tex (a @@ b @@ c @@ d);
$$a \circ b \circ c \circ d$$
(%o3)                         false
```


Assign TeX output for a nofix operator.



```maxima
(%i1) nofix ("foo");
(%o1)                          foo
(%i2) texput ("foo", "\\mathsc{foo}", nofix);
(%o2)                     \mathsc{foo}
(%i3) tex (foo);
$$\mathsc{foo}$$
(%o3)                         false
```


Assign TeX output for a matchfix operator.



```maxima
(%i1) matchfix ("<<", ">>");
(%o1)                          <<
(%i2) texput ("<<", [" \\langle ", " \\rangle "], matchfix);
(%o2)                [ \langle ,  \rangle ]
(%i3) tex (<<a>>);
$$ \langle a \rangle $$
(%o3)                         false
(%i4) tex (<<a, b>>);
$$ \langle a , b \rangle $$
(%o4)                         false
(%i5) texput ("<<", [" \\langle ", " \\rangle ", " \\, | \\,"],
      matchfix);
(%o5)           [ \langle ,  \rangle ,  \, | \,]
(%i6) tex (<<a>>);
$$ \langle a \rangle $$
(%o6)                         false
(%i7) tex (<<a, b>>);
$$ \langle a \, | \,b \rangle $$
(%o7)                         false
```

<!-- category: Other -->
<!-- keywords: with_stdout -->
<!-- signatures: with_stdout(f, expr_1, expr_2, expr_3, ...), with_stdout(s, expr_1, expr_2, expr_3, ...) -->
### Function: with_stdout (f, expr_1, expr_2, expr_3, ...)

`with_stdout` wertet Argumente *expr_1*, *expr_2*, *expr_3*, 
... aus und schreibt die Ergebnisse der Auswertung in die Ausgabedatei 
`f` oder in den Stream `s`.  Die Ergebnisse werden nicht auf der 
Konsole ausgegeben.


Die Optionsvariable `file_output_append` bestimmt, ob `with_stdout` 
die Daten an die Ausgabedatei anhangt oder die Ausgabedatei zuvor loscht. 
Hat `file_output_append` den Wert `true`, werden die Daten 
angehangt.  Ansonsten wird die Datei geloscht und neu angelegt.  Existiert
die Ausgabedatei noch nicht, wird diese angelegt.


`with_stout` gibt das Ergebnis des letzten Argumentes zuruck.  


Siehe auch `writefile`.


Beispiel:



```maxima
(%i1) with_stdout ("tmp.out", for i:5 thru 10 do
         print (i, "! yields", i!))$
(%i2) printfile ("tmp.out")$
5 ! yields 120 
6 ! yields 720 
7 ! yields 5040 
8 ! yields 40320 
9 ! yields 362880 
10 ! yields 3628800
```

See also: `writefile`.

<!-- category: Other -->
<!-- keywords: writefile -->
<!-- signatures: writefile(filename) -->
### Function: writefile (filename)

Startet eine Aufzeichnung aller Ein- und Ausgaben der Konsole.  Die Ein- und 
Ausgaben werden in die Datei *filename* geschrieben.


Die Ausgabedatei kann von Maxima nicht wieder zuruckgelesen werden.  Um ein 
Datei zu erzeugen, die von Maxima zuruckgelesen werden kann, siehe die 
Funktionen `save` und `stringout`.  `save` speichert 
Ausdrucke in einem Lisp-Format und `stringout` in einem Maxima-Format.


Die Reaktion der Funktion `writefile` fur den Fall, dass die Ausgabedatei
bereits existiert, hangt von der Lisp-Implementation ab.  Die Ausgabedatei
kann zuruckgesetzt werden oder die Daten werden angehangt.  Die Funktion
`appendfile` hangt die Daten immer an eine existierende Datei an.


Um eine Aufzeichnung ohne Textausgaben von Funktionen zu erhalten, kann 
`writefile` nach der Ausfuhrung von `playback` ausgefuhrt werden. 
`playback` gibt alle vorhergenden Eingabe- und Ausgabemarken aus, jedoch 
nicht sonstige Textausgaben von Maxima-Funktionen.


Mit `closefile` wird die Aufzeichnung beendet.

See also: `save`, `stringout`, `appendfile`, `closefile`.

