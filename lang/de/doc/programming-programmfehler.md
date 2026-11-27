## Programmfehler

<!-- category: Programming -->
<!-- keywords: bug_report -->
<!-- signatures: bug_report() -->
### Function: bug_report ()

Zeigt die Maxima- und Lisp-Version der Installation sowie einen Link zur
Webseite des Maxima-Projekts.  Die Informationen zur Version werden auch von
`build_info` angezeigt.  Wenn ein Programmfehler berichtet wird, ist es
hilfreich, die Maxima- und Lisp-Version in den Fehlerbericht aufzunehmen.
`bug_report` gibt eine leere Zeichenkette `""` zuruck.


Beispiel:



```maxima
(%i1) bug_report();

Please report bugs to:
    https://sourceforge.net/p/maxima/bugs/
To report a bug, you must have a Sourceforge account.
Please include the following information with your bug report:
-------------------------------------------------------------
Maxima version: "5.36.1"
Maxima build date: "2015-06-02 11:26:48"
Host type: "x86_64-unknown-linux-gnu"
Lisp implementation type: "GNU Common Lisp (GCL)"
Lisp implementation version: "GCL 2.6.12"
-------------------------------------------------------------
The above information is also reported by the function 'build_info()'.
```

See also: `build_info`.

<!-- category: Programming -->
<!-- keywords: build_info -->
<!-- signatures: build_info() -->
### Function: build_info ()

Zeigt die Maxima- und Lisp-Version der Installation.  `build_info` gibt die Eigenschaften der Maxima-Version als Maxima structure (definiert durch `defstruct`) zuruck.
Die Felder der Struktur sind:
`version`, `timestamp`, `host`, `lisp_name` und `lisp_version`.
Wenn die Ausgabe formatiert erfolgt (mit `display2d:true;`),
werden die Ergebnisse als kurze Tabelle ausgegeben.


Beispiel:



```maxima
(%i1) build_info ();
(%o1) 
Maxima version: "5.36.1"
Maxima build date: "2015-06-02 11:26:48"
Host type: "x86_64-unknown-linux-gnu"
Lisp implementation type: "GNU Common Lisp (GCL)"
Lisp implementation version: "GCL 2.6.12"

(%i2) x : build_info ()$

(%i3) x@version;
(%o3)                               5.36.1


(%i4) x@timestamp;
(%o4)                         2015-06-02 11:26:48


(%i5) x@host;
(%o5)                      x86_64-unknown-linux-gnu


(%i6) x@lisp_name;
(%o6)                        GNU Common Lisp (GCL)


(%i7) x@lisp_version;
(%o7)                             GCL 2.6.12


(%i8) x;
(%o8) 
Maxima version: "5.36.1"
Maxima build date: "2015-06-02 11:26:48"
Host type: "x86_64-unknown-linux-gnu"
Lisp implementation type: "GNU Common Lisp (GCL)"
Lisp implementation version: "GCL 2.6.12"
```


Der Versionsstring (hier 5.36.1) kann auch folgendermassen aussehen:
branch_5_37_base_331_g8322940_dirty



```maxima
(%i1) build_info();
(%o1) 
Maxima version: "branch_5_37_base_331_g8322940_dirty"
Maxima build date: "2016-01-01 15:37:35"
Host type: "x86_64-unknown-linux-gnu"
Lisp implementation type: "CLISP"
Lisp implementation version: "2.49 (2010-07-07) (built 3605577779) 
     (memory 3660647857)"
```





In diesem Fall wurde Maxima nicht von einem Release sondern direkt aus dem Git checkout des
Sourcecodes compiliert.
Im obigen Beispiel ist der Checkout 331 Commits nach dem letzten Git-Tag (ublicherweise ein
Maxima-Release (5.37 im obigen Beispiel)) und der verkurzte Commit Hash des letzten Commits
lautet "8322940".

<!-- category: Programming -->
<!-- keywords: run_testsuite -->
<!-- signatures: run_testsuite([options]) -->
### Function: run_testsuite ([options])

Die Funktion `run_testsuite` fuhrt die Maxima-Testsuite aus.  
Erfolgreiche Tests und Tests, die zwar nicht erfolgreich, aber als ein bekannter
Fehler gekennzeichnet sind, geben die Meldung "passed".  `run_testsuite` 
akzeptiert die folgenden optionalen Schlusselworte als Argumente:



**display_all** — Hat das Schlusselwort `display_all` den Wert `true`, werden alle 
Tests angezeigt.  Der Standardwert ist `false`.  In diesem Fall werden nur 
die Tests angezeigt, die fehlschlagen.
**display_known_bugs** — Hat das Schlusselwort `display_known_bugs` den Wert `true`, werden 
alle Tests angezeigt, die als fehlerhaft gekennzeichnet sind.  Der Standardwert 
ist `false`.
**tests** — Das Schlusselwort `tests` erhalt eine Liste mit den Testdateien, die 
ausgefuhrt werden sollen.  Eine Testdatei kann durch eine Zeichenkette oder 
ein Symbol angegeben werden.  Der Standard ist, dass alle Testdateien 
ausgefuhrt werden, die in der Optionsvariablen `testsuite_files` 
enthalten sind.
**time** — Hat das Schlusselwort `time` den Wert `true`, werden die Laufzeiten 
der einzelnen Testdateien angezeigt.  Hat `time` den Wert `all` und
`display_all` den Wert `true`, wird die Laufzeit jedes einzelnen 
Tests angezeigt.  Der Standardwert ist `false`.


Das Ausfuhren einer Testdatei kann die Maxima-Umgebung andern.
Typischerweise fuhrt eine Testdatei zuerst das Kommando `kill(all)` aus, 
um eine definierte Umgebung herzustellen, in der keine nutzerdefinierten 
Funktionen und Variablen vorhanden sind.  Siehe auch die Funktion `kill`.


Testdateien konnen auch von der Funktion `batch` mit der Option
`test` ausgefuhrt werden.  Siehe die Dokumentation der Funktion
`batch` auch fur ein Beispiel, wie eine Testdatei aufgebaut ist.


`run_testsuite` hat den Ruckgabewert `done`.


Beispiele:



```maxima
(%i1) run_testsuite(tests = ["rtest1", rtest2]);
Running tests in rtest1: 111/111 tests passed
Running tests in rtest2: 66/66 tests passed

No unexpected errors found out of 177 tests.
Evaluation took:
  0.344 seconds of real time
  0.30402 seconds of total run time (0.30002 user, 0.00400 system)
  88.37% CPU
  581,206,031 processor cycles
  7,824,088 bytes consed
  
(%o1)                         done
```


Es werden zusatzlich alle Tests angezeigt.  Die Ausgabe wird hier nach dem
zweiten Test abgekurzt.



```maxima
(%i2) run_testsuite(display_all=true, tests=["rtest1",rtest2]);
Running tests in rtest1: 
********************** Problem 1 ***************
Input:
(fmakunbound(f), kill(functions, values, arrays))

Result:
done

... Which was correct.

********************** Problem 2 ***************
Input:
             2
f(x) := y + x

Result:
             2
f(x) := y + x

... Which was correct.

[...]
```


Im folgenden Beispiel werden die Tests ausgegeben, von denen bekannt ist, dass
sie fehlerhaft sind.  Dies sind die Tests mit den Nummern 76 und 78.



```maxima
(%i1) run_testsuite(display_known_bugs=true, tests=[rtest12]);
Running tests in rtest12:

********************** Problem 76 ***************
Input:
           2
letsimp(foo (x))

Result:
       2
1 - bar (aa)

This differed from the expected result:
       2
1 - bar (x)

********************** Problem 78 ***************
Input:
           4
letsimp(foo (x))

Result:
   4            2
bar (aa) - 2 bar (aa) + 1

This differed from the expected result:
         2         4
1 - 2 bar (x) + bar (x)

76/78 tests passed

The following 2 problems failed: (76 78)

Error summary:
Errors found in /usr/local/share/maxima/5.23post/tests/rtest12.mac,
problems: (76 78)
2 tests failed out of 78 total tests.
Evaluation took:
  0.157 seconds of real time
  0.12801 seconds of total run time (0.12401 user, 0.00400 system)
  [Run times consist of 0.008 seconds GC time, 
   and 0.121 seconds non-GC time.]
  81.53% CPU
  9 forms interpreted
  71 lambdas converted
  254,604,658 processor cycles
  6,145,064 bytes consed
  
(%o0)                         done
```

See also: `testsuite_files`, `kill`, `batch`.

<!-- category: Programming -->
<!-- keywords: testsuite_files -->
<!-- signatures: testsuite_files -->
### Variable: testsuite_files

Die Optionsvariable `testsuite_files` enthalt die Liste der Testdateien, 
die von `run_testsuite` standardmaßig ausgefuhrt werden.  Wenn 
bekannt ist, dass einzelne Tests einer Testdatei fehlschlagen werden, dann wird 
anstatt dem Namen der Datei eine Liste eingefugt, die den Namen und die 
Nummern der fehlerhaften Tests enthalt.  Das folgende Beispiel zeigt die
Zuweisung einer neuen Liste und wie fehlerhafte Tests gekennzeichnet werden:



```maxima
testsuite_files : ["rtest13s", ["rtest14", 57, 63]]
```


Die Eintrage der Liste bedeuten, dass die Dateien "rtest13s" und "rtest14" von
der Funktion `run_testsuite` ausgefuhrt werden sollen und das bekannt
ist, dass die Tests mit den Nummern 57 und 63 der Testdatei "rtest14"
fehlschlagen werden.

See also: `run_testsuite`.

