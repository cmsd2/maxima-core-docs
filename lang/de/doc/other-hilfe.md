## Hilfe

<!-- category: Other -->
<!-- keywords: apropos -->
<!-- signatures: apropos(string) -->
### Function: apropos (string)

Gibt eine Liste der Maxima-Symbole zuruck, die die Zeichenkette *string*
im Namen enthalten.  Das Kommando `apropos("")` gibt eine Liste mit allen
Maxima-Symbolen zuruck.  Wenn `apropos` kein Maxima-Symbol finden kann,
das die Zeichenkette *string* im Namen enthalt, ist das Ergebnis eine
leere Liste `[]`.


Beispiel:


Zeige alle Maxima-Symbole, die die Zeichenkette `"gamma"` im Namen
enthalten:



```maxima
(%i1) apropos("gamma");
(%o1) [%gamma, gamma, gammalim, gamma_expand, gamma_incomplete_lower, 
gamma_incomplete, gamma_incomplete_generalized, 
gamma_incomplete_regularized, Gamma, log_gamma, makegamma, 
prefer_gamma_incomplete, 
gamma_incomplete_generalized_regularized]
```

<!-- category: Other -->
<!-- keywords: browser -->
<!-- signatures: browser -->
### Variable: browser

Damit wird das Browserkommando angegeben, mit dem die HTML Dateien dargestellt werden.
Der String hat die Form `<cmd> ~A` wobei `~A` mit der URL ersetzt wird und `<cmd>`
ist das Programm, das die URL im Argument im Browser darstellt.



Auf Windows ist der Standardwert `"start ~A"`,
was den Default-Browser öffnet.  Das kann beispielsweise durch `start firefox ~A`, `start chrome ~A`
oder `start iexplore ~A` ersetzt werden, um andere Browser als den Standardbrowser zu verwenden.



Unter anderen Betriebssystemen wird der Standardbrowser automatisch verwendet
(unter Verwendung von `xdg-open` unter Linux/Unix und `open` auf MacOS).
Die `browser` variable kann auf einen Nicht-Default-Browser gesetzt werden, z.B.
`browser:"firefox '~A'";` oder `browser:"chromium '~A'";`


Siehe auch `output_format_for_help` und `url_base`.

See also: `output_format_for_help`, `url_base`.

<!-- category: Other -->
<!-- keywords: demo -->
<!-- signatures: demo(filename) -->
### Function: demo (filename)

Fuhrt die Beispiele der Demo-Datei *filename* aus.  Das Argument
*filename* kann ein Symbol oder eine Zeichenkette sein.  `demo` macht
nach jeder Ausgabe eine Pause und wartet auf eine Eingabe.  `demo` sucht in
den Ordnern, die in der Optionsvariablen `file_search_demo` enthalten sind,
nach der Datei *filename*.  Die Dateiendung *.dem* muss nicht angegeben
werden.


Siehe auch die Funktion `file_search` fur die Suche von Dateien und die
Funktion `batch` fur den Aufbau einer Demo-Datei.  Demo-Dateien konnen
auch von der Funktion `batch` mit der Option `demo` ausgefuhrt
werden.  `demo` wertet das Argument aus.  `demo` gibt den Namen der
Demo-Datei zuruck, die ausgefuhrt wird.


Beispiel:



```maxima
(%i1) demo ("disol");
batching /home/wfs/maxima/share/simplification/disol.dem
 At the _ prompt, type ';' followed by enter to get next demo
(%i2)                      load("disol")
_
(%i3)           exp1 : a (e (g + f) + b (d + c))
(%o3)               a (e (g + f) + b (d + c))
_
(%i4)                disolate(exp1, a, b, e)
(%t4)                         d + c

(%t5)                         g + f

(%o5)                   a (%t5 e + %t4 b)
_
```

See also: `file_search_demo`, `file_search`, `batch`.

<!-- category: Other -->
<!-- keywords: describe -->
<!-- signatures: describe(topic), describe(topic, exact), describe(topic, inexact) -->
### Function: describe (topic)

`describe(topic)` entspricht dem Kommando `describe(topic, exact)`.  Das Argument *topic* ist eine Zeichenkette oder ein Symbol.  Wenn
*topic* ein Operator wie zum Beispiel `+`, `*`, `do` oder
`if` ist, muss der Name des Operators als eine Zeichenkette angegeben
werden.  Der Name des Operators `+` fur die Addition ist zum Beispiel
`"+"`.


`describe(topic, exact)` findet Eintrage, die mit *topic* 
ubereinstimmen.  Bei der Suche nach einer Ubereinstimmung werden Klein- und
Großschreibung nicht voneinander unterschieden.
`describe(topic, inexact)` findet Eintrage, die *topic*
enthalten.  Sind mehrere Eintrage vorhanden, fragt Maxima, welcher der 
Eintrage angezeigt werden soll.


`? foo` (mit einem Leerzeichen zwischen `?` und `foo`) entspricht
`describe("foo", exact)` und `?? foo` entspricht 
`describe("foo", inexact)`.  In der Kurzschreibweise muss das Argument ein
Symbol sein.  Siehe auch `?` und `??`.


`describe("", inexact)` gibt alle Themen aus, die in der Dokumentation
enthalten sind.


`describe` wertet das Argument nicht aus.  `describe` gibt `true` 
zuruck, wenn Eintrage gefunden wurden, ansonsten `false`.


Beispiel:


Im folgenden Beispiel werden die Eintrage 2 und 3 ausgewahlt (Die Ausgabe 
ist verkurzt wiedergeben).  Alle oder keiner der Eintrage werden mit 
`all` oder `none` ausgewahlt.  Die Eingabe kann mit `a` oder 
`n` abgekurzt werden.



```maxima
(%i1) ?? integrat
 0: Functions and Variables for Integration
 1: Introduction to Integration
 2: integrate (Functions and Variables for Integration)
 3: integrate_use_rootsof (Functions and Variables for Integration)
 4: integration_constant (Functions and Variables for Integration)
 5: integration_constant_counter (Functions and Variables for 
    Integration)
Enter space-separated numbers, `all' or `none': 2 3

 -- Function: integrate (<expr>, <x>)
 -- Function: integrate (<expr>, <x>, <a>, <b>)
     Attempts to symbolically compute the integral of <expr> with
     respect to <x>.  `integrate (<expr>, <x>)' is an indefinite
     integral, while `integrate (<expr>, <x>, <a>, <b>)' is a 
     definite integral, with limits of integration <a> and <b>.
     [...]

 -- Option variable: integrate_use_rootsof
     Default value: `false'

     When `integrate_use_rootsof' is `true' and the denominator of
     a rational function cannot be factored, `integrate' returns
     the integral in a form which is a sum over the roots (not yet 
     known) of the denominator.
     [...]
```

See also: `?`, `??`.

<!-- category: Other -->
<!-- keywords: example -->
<!-- signatures: example(topic), example() -->
### Function: example (topic)

Das Kommando `example(topic)` zeigt Beispiele fur das Argument
*topic*.  *topic* ist ein Symbol oder eine Zeichenkette.  Ist das
Argument ein Operator, wie zum Beispiel `+`, `*` oder `do`, muss
das Argument *topic* eine Zeichenkette sein.  Der Name des Operators
`+` fur die Addition ist zum Beispiel `"+"`.  Groß- und
Kleinschreibung werden nicht unterschieden.


`example()` zeigt eine Liste aller Themen, fur die Beispiele 
vorhanden sind.


Die Optionsvariable `manual_demo` enthalt den Namen der Datei, die die 
Beispiele enthalt.  Der Standardwert ist `"manual.demo"`.


`example` wertet das Argument nicht aus.  `example` gibt `done`
zuruck, außer wenn kein Argument angeben ist oder wenn kein Beispiel 
gefunden wurde.  In diesen Fallen wird eine Liste mit allen Themen ausgegeben, 
zu denen Beispiele vorhanden sind.


Beispiele:







```maxima
(%i1) example(append);
(%i2) append([x+y,0,-3.2],[2.5e+20,x])
(%o2)             [y + x, 0, - 3.2, 2.5e+20, x]
(%o2)                         done
(%i3) example("lambda");

(%i4) lambda([x,y,z],z^2+y^2+x^2)
                                    2    2    2
(%o4)            lambda([x, y, z], z  + y  + x )
(%i5) %(1,2,a)
                              2
(%o5)                        a  + 5
(%i6) a+2+1
(%o6)                         a + 3
(%o6)                         done
```

See also: `manual_demo`.

<!-- category: Other -->
<!-- keywords: manual_demo -->
<!-- signatures: manual_demo -->
### Variable: manual_demo

Standardwert: `"manual.demo"`


Die Optionsvariable `manual_demo` enthalt den Namen der Datei, die die 
Beispiele fur die Funktion `example` enthalt.  Siehe `example`.

See also: `example`.

<!-- category: Other -->
<!-- keywords: output_format_for_help -->
<!-- signatures: output_format_for_help -->
### Variable: output_format_for_help

Standardwert: `text`


`output_format_for_help` gibt an, wie `describe` die Hilfe darstellt.


`output_format_for_help` kann auf folgende Werte gesetzt werden:


**text** — Die Hilfe wird als Text am Terminal dargestellt. Das ist der Standard.
**html** — Die Hilfe wird mit einem Browser als HTML Version des Handbuchs dargestellt.
**frontend** — Die Hilfe wird mit dem Hilfesystem des Frontends dargestellt. Wenn kein Frontend
verwendet wird, wird ein Fehler ausgegeben. Frontends sind beispielsweise wxMaxima oder Xmaxima.


Andere Werte sind Fehler.


Siehe auch `browser` und `url_base`.

See also: `browser`, `url_base`.

<!-- category: Other -->
<!-- keywords: url_base -->
<!-- signatures: url_base -->
### Variable: url_base

Wenn die Hilfe mit einem Webbrowser dargestellt wird, definiert `url_base`
die zu verwendende URL. Der Standardwert ist eine `file://` URL, die
zum Directory mit den HTML-Dateien zeigt.
Man könnte z.B. auch `http://localhost:8080/` oder andere URLs
verwenden, wo die Hilfe abrufbar ist. Achtung: Diese URL muß exakt
dieselben HTML-Dateien enthalten, die aus dem Maxima-Sourcecode
gebaut werden; eine Tabelle wird verwendet, um aus einem Thema
die richtige Position in einer HTML-Datei zu finden.


Siehe auch `output_format_for_help` und `browser`..

See also: `output_format_for_help`, `browser`.

