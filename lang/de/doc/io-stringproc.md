## stringproc

<!-- category: IO -->
<!-- keywords: adjust_external_format -->
<!-- signatures: adjust_external_format() -->
### Function: adjust_external_format ()

Gibt Informationen zum aktuellen externen Format des Lisp Lesers aus 
und in dem Fall, dass die Kodierung des externen Formats nicht mit der 
Kodierung der Anwendung, in der Maxima lauft, ubereinstimmt, 
versucht `adjust_external_format`, die Kodierung anzupassen 
oder gibt entsprechende Hilfen oder Anleitungen aus. 
`adjust_external_format` gibt `true` zuruck, wenn das externe 
Format geandert wurde und `false`, wenn nicht.


Funktionen wie `cint`, `unicode`, `octets_to_string` 
und `string_to_octets` benotigen UTF-8 als das externe Format 
des Lisp Lesers, um uber dem vollstandigen Bereich der Unicode-Zeichen 
korrekt arbeiten zu konnen.


Beispiele (Maxima in Windows, Marz 2016): 
Die Verwendung von `adjust_external_format` in dem Fall, dass das 
externe Format nicht mit der Kodierung der Anwendung, in der Maxima lauft, 
ubereinstimmt.


1. Maxima in der Kommandozeile


Fur die Sitzung in einem Terminal wird empfohlen, ein mit SBCL kompiliertes 
Maxima zu verwenden. Unicode wird hier standardmaßig unterstutzt 
und ein Aufruf von `adjust_external_format` ist nicht notwendig. 


Falls Maxima mit CLISP oder GCL kompiliert wurde, wird empfohlen, 
die Kodierung des Terminals von CP850 in CP1252 abzuandern. 
`adjust_external_format` gibt eine entsprechende Hilfe aus.


CCL liest UTF-8, obwohl der Input vom Terminal standardmaßig in CP850 
kodiert ist. CP1252 wird jedoch von CCL nicht unterstutzt. 
`adjust_external_format` gibt deshalb eine Anleitung aus, 
wie die Kodierung des Terminals und die des externen Formats beide 
auf ISO-8859-1 abgeandert werden konnen.


2. wxMaxima


In wxMaxima liest SBCL standardmaßig CP1252.
Der Input von der Anwendung (wxMaxima) ist jedoch UTF-8-kodiert. 
Hier ist eine Anpassung erforderlich. 


Ein Aufruf von `adjust_external_format` und ein Neustart von Maxima 
andern das standardmaßige externe Format auf UTF-8.



```maxima
(%i1)adjust_external_format();
The line
(setf sb-impl::*default-external-format* :utf-8)
has been appended to the init file
C:/Users/Username/.sbclrc
Please restart Maxima to set the external format to UTF-8.
(%i1) false
```


Maxima wird neu gestartet.



```maxima
(%i1) adjust_external_format();
The external format is currently UTF-8
and has not been changed.
(%i1) false
```

See also: `cint`, `unicode`, `octets_to_string`, `string_to_octets`.

<!-- category: IO -->
<!-- keywords: alphacharp -->
<!-- signatures: alphacharp(char) -->
### Function: alphacharp (char)

Gibt `true` zuruck, falls *char* ein Buchstabe eines Alphabets ist. 


Um ein Nicht-US-ASCII-Zeichen als Buchstaben eines Alphabets erkennen zu konnen, 
muss das unter Maxima liegende Lisp Unicode voll unterstutzen. 
So wird z.B. ein Umlaut mit SBCL in GNU/Linux als Buchstabe erkannt, 
mit GCL jedoch nicht. 
(In Windows muss ein mit SBCL kompiliertes Maxima auf UTF-8 umgestellt worden sein. 
Siehe hierzu `adjust_external_format`.)


Beispiele:


Das unter Maxima liegende Lisp (SBCL, GNU/Linux) kann das eingegebene Zeichen 
in ein Lisp-Schriftzeichen umwandeln und untersuchen.



```maxima
(%i1) alphacharp("u");
(%o1)                          true
```


Mit GCL ist dies nicht moglich. Es kommt zu einem Fehlerabbruch.



```maxima
(%i1) alphacharp("u");
(%o1)                          true
(%i2) alphacharp("u");

package stringproc: u cannot be converted into a Lisp character.
 -- an error.
```

See also: `adjust_external_format`.

<!-- category: IO -->
<!-- keywords: alphanumericp -->
<!-- signatures: alphanumericp(char) -->
### Function: alphanumericp (char)

Gibt `true` zuruck, falls *char* ein Buchstabe eines Alphabets 
oder ein Zahlzeichen ist 
(als Zahlzeichen werden hier nur entprechende US-ASCII-Zeichen betrachtet).


Hinweis: Siehe Bemerkungen zu `alphacharp`.

See also: `alphacharp`.

<!-- category: IO -->
<!-- keywords: ascii -->
<!-- signatures: ascii(int) -->
### Function: ascii (int)

Gibt das US-ASCII-Zeichen zuruck, das der Ganzzahl *int* entspricht. 
*int* muss dabei kleiner als `128` sein.


Siehe `unicode` fur die Umwandlung von Codepunkten großer `127`.


Beispiele:



```maxima
(%i1) for n from 0 thru 127 do ( 
        ch: ascii(n), 
        if alphacharp(ch) then sprint(ch),
        if n = 96 then newline() )$
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

See also: `unicode`.

<!-- category: IO -->
<!-- keywords: cequal -->
<!-- signatures: cequal(char_1, char_2) -->
### Function: cequal (char_1, char_2)

Gibt `true` zuruck, falls *char_1* und *char_2* ein 
und das selbe Schriftzeichen sind.

<!-- category: IO -->
<!-- keywords: cequalignore -->
<!-- signatures: cequalignore(char_1, char_2) -->
### Function: cequalignore (char_1, char_2)

Arbeitet wie `cequal`, ignoriert jedoch die Groß- und Kleinschreibung,  
was fur Nicht-US-ASCII-Zeichen nur moglich ist, wenn das unter Maxima liegende 
Lisp einen Buchstaben auch als Buchstaben eines Alphabets erkennen kann.
Siehe hierzu die Bemerkungen zu `alphacharp`.

See also: `cequal`, `alphacharp`.

<!-- category: IO -->
<!-- keywords: cgreaterp -->
<!-- signatures: cgreaterp(char_1, char_2) -->
### Function: cgreaterp (char_1, char_2)

Gibt `true` zuruck, wenn der Codepunkt des Zeichens *char_1* 
großer ist als der des Zeichens *char_2*.

<!-- category: IO -->
<!-- keywords: cgreaterpignore -->
<!-- signatures: cgreaterpignore(char_1, char_2) -->
### Function: cgreaterpignore (char_1, char_2)

Arbeitet wie `cgreaterp`, ignoriert jedoch die Groß- und Kleinschreibung,  
was fur Nicht-US-ASCII-Zeichen nur moglich ist, wenn das unter Maxima liegende 
Lisp einen Buchstaben auch als Buchstaben eines Alphabets erkennen kann.
Siehe hierzu die Bemerkungen zu `alphacharp`.

See also: `cgreaterp`, `alphacharp`.

<!-- category: IO -->
<!-- keywords: charat -->
<!-- signatures: charat(string, n) -->
### Function: charat (string, n)

Gibt das *n*-te Schriftzeichen in *string* zuruck.
Das erste Zeichen in *string* erhalt man mit *n* = 1. 


Beispiel:



```maxima
(%i1) charat("Lisp",1);
(%o1)                           L
(%i2) charlist("Lisp")[1];
(%o2)                           L
```

<!-- category: IO -->
<!-- keywords: charlist -->
<!-- signatures: charlist(string) -->
### Function: charlist (string)

Gibt eine Liste mit allen Schriftzeichen in *string* zuruck.


Beispiel:



```maxima
(%i1) charlist("Lisp");
(%o1)                     [L, i, s, p]
```

<!-- category: IO -->
<!-- keywords: charp -->
<!-- signatures: charp(obj) -->
### Function: charp (obj)

Gibt `true` zuruck, wenn *obj* ein Schriftzeichen ist.


Beispiel: Siehe Einfuhrung.

<!-- category: IO -->
<!-- keywords: cint -->
<!-- signatures: cint(char) -->
### Function: cint (char)

Gibt den Unicode Codepunkt des Arguments *char* zuruck, das ein 
Schriftzeichen sein muss, d.h. eine Zeichenkette der Lange `1`.


Beispiele: Der hexadedimale Codepunkt von Schriftzeichen 
(Maxima kompiliert mit SBCL in GNU/Linux). 



```maxima
(%i1) obase: 16.$
(%i2) map(cint, ["$","GBP","EUR"]);
(%o2)                           [24, 0A3, 20AC]
```


Warnung: In Windows ist es nicht moglich, Schriftzeichen, 
die Codepunkten großer 16 Bit entsprechen, in wxMaxima einzugeben, 
wenn Maxima mit SBCL kompiliert wurde und das aktuelle externe Format nicht UTF-8 ist. 
Siehe `adjust_external_format` fur weitere Informationen.








CMUCL verarbeitet solche Zeichen nicht als ein einziges Zeichen und `cint` 
gibt dann `false` zuruck. 
Als Ausweg kann hier die Umwandlung von Schriftzeichen in Codepunkte uber 
UTF-8-Oktette dienen: 

`utf8_to_unicode(string_to_octets(character));`








Siehe `utf8_to_unicode`, `string_to_octets`.

See also: `adjust_external_format`, `utf8_to_unicode`, `string_to_octets`.

<!-- category: IO -->
<!-- keywords: clessp -->
<!-- signatures: clessp(char_1, char_2) -->
### Function: clessp (char_1, char_2)

Gibt `true` zuruck, wenn der Codepunkt des Zeichens *char_1* 
kleiner ist als der des Zeichens *char_2*.

<!-- category: IO -->
<!-- keywords: clesspignore -->
<!-- signatures: clesspignore(char_1, char_2) -->
### Function: clesspignore (char_1, char_2)

Arbeitet wie `clessp`, ignoriert jedoch die Groß- und Kleinschreibung,  
was fur Nicht-US-ASCII-Zeichen nur moglich ist, wenn das unter Maxima liegende 
Lisp einen Buchstaben auch als Buchstaben eines Alphabets erkennen kann.
Siehe hierzu die Bemerkungen zu `alphacharp`.

See also: `clessp`, `alphacharp`.

<!-- category: IO -->
<!-- keywords: close -->
<!-- signatures: close(stream) -->
### Function: close (stream)

Schließt den Datenstrom *stream* und gibt `true` zuruck, 
wenn *stream* noch geoffnet war.

<!-- category: IO -->
<!-- keywords: constituent -->
<!-- signatures: constituent(char) -->
### Function: constituent (char)

Gibt `true` zuruck, wenn *char* ein graphisches Schriftzeichen, 
aber kein Leerzeichen ist. 
Ein graphisches Schriftzeichen ist ein Leerzeichen oder ein Zeichen, das man sehen kann. 
(`constituent` wurde definiert von Paul Graham.
Siehe Paul Graham, ANSI Common Lisp, 1996, Seite 67.)


Beispiel:



```maxima
(%i1) for n from 0 thru 255 do ( 
tmp: ascii(n), if constituent(tmp) then sprint(tmp) )$
! " #  %  ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c
d e f g h i j k l m n o p q r s t u v w x y z { | } ~
```


Hinweis: Siehe Bemerkungen zu `alphacharp`.

See also: `alphacharp`.

<!-- category: IO -->
<!-- keywords: digitcharp -->
<!-- signatures: digitcharp(char) -->
### Function: digitcharp (char)

Gibt `true` zuruck, wenn *char* ein Zahlzeichen ist, 
wobei als Zahlzeichen hier nur entsprechende US-ASCII-Zeichen betrachtet werden.

<!-- category: IO -->
<!-- keywords: eval_string -->
<!-- signatures: eval_string(str) -->
### Function: eval_string (str)

Parse the string *str* as a Maxima expression and evaluate it.  The string
*str* may or may not have a terminator (dollar sign `$` or semicolon 
`;`).  Only the first expression is parsed and evaluated, if there is more 
than one.


Complain if *str* is not a string.


See also `parse_string`.


Examples:



```maxima
(%i1) eval_string ("foo: 42; bar: foo^2 + baz");
(%o1)                       42
(%i2) eval_string ("(foo: 42, bar: foo^2 + baz)");
(%o2)                   baz + 1764
```

See also: `parse_string`.

<!-- category: IO -->
<!-- keywords: flength -->
<!-- signatures: flength(stream) -->
### Function: flength (stream)

*stream* muss ein geoffneter Datenstrom in eine oder aus einer Datei sein. 
`flength` gibt dann die Anzahl der Bytes zuruck, die sich momentan in 
dieser Datei befinden.


Beispiel: Siehe `writebyte` .

See also: `writebyte`.

<!-- category: IO -->
<!-- keywords: flush_output -->
<!-- signatures: flush_output(stream) -->
### Function: flush_output (stream)

Leert den Inhalt des Dateiausgabestroms *stream* in die Datei.


Beispiel: Siehe `writebyte` .

See also: `writebyte`.

<!-- category: IO -->
<!-- keywords: fposition -->
<!-- signatures: fposition(stream), fposition(stream, pos) -->
### Function: fposition (stream)

Ohne das optionale Argument *pos* gibt `fposition` die aktuelle Position 
in dem Datenstrom *stream* zuruck. 
Wird *pos* verwendet, legt `fposition` diesen Wert als aktuelle Position 
in *stream* fest. *pos* muss eine positive Zahl sein. 


Die Positionen in Datenstromen sind wie in Zeichenketten und Listen 1-indiziert, 
d.h. das erste Element in *stream* hat die Position 1.

<!-- category: IO -->
<!-- keywords: freshline -->
<!-- signatures: freshline(), freshline(stream) -->
### Function: freshline ()

Schreibt einen Zeilenumbruch in den Standardausgabestrom, falls die aktuelle 
Ausgabeposition nicht gerade der Anfang einer Zeile ist und gibt `true` 
zuruck. Bei der Verwendung des optionalen Arguments *stream* wird der 
Umbruch in diesen Datenstrom geschrieben. 


Es gibt Situationen, in denen `freshline()` nicht wie erwartet funktioniert.


Siehe auch `newline`.

See also: `newline`.

<!-- category: IO -->
<!-- keywords: get_output_stream_string -->
<!-- signatures: get_output_stream_string(stream) -->
### Function: get_output_stream_string (stream)

Gibt Schriftzeichen, die aktuell in dem geoffneten Datenstrom *stream* 
enthalten sind, in einer Zeichenkette zuruck. Die zuruck gegebenen 
Zeichen werden dabei aus dem Datenstrom entfernt. *stream* muss durch 
`make_string_output_stream` erzeugt worden sein.


Beispiel: Siehe `make_string_output_stream` .

See also: `make_string_output_stream`.

<!-- category: IO -->
<!-- keywords: lowercasep -->
<!-- signatures: lowercasep(char) -->
### Function: lowercasep (char)

Gibt `true` zuruck, wenn *char* ein Kleinbuchstabe ist.


Hinweis: Siehe Bemerkungen zu `alphacharp`.

See also: `alphacharp`.

<!-- category: IO -->
<!-- keywords: make_string_input_stream -->
<!-- signatures: make_string_input_stream(string), make_string_input_stream(string, start), make_string_input_stream(string, start, end) -->
### Function: make_string_input_stream (string)

Gibt einen Datenstrom zuruck, der Teile der Zeichenkette *string* 
und ein Dateiende enthalt. 
Ohne optionale Argumente enthalt der Strom die gesamte Zeichenkette 
und ist vor dem ersten Zeichen positioniert. Mit den optionalen Argumenten 
*start* und *end* lasst sich der Abschnitt der Zeichenkette festlegen, 
den der Datenstrom enthalt. Das erste Zeichen befindet sich dabei an der 
Position 1.

 

```maxima
(%i1) istream : make_string_input_stream("text", 1, 4);
(%o1)              #<string-input stream from "text">
(%i2) (while (c : readchar(istream)) # false do sprint(c), newline())$
t e x 
(%i3) close(istream)$
```

<!-- category: IO -->
<!-- keywords: make_string_output_stream -->
<!-- signatures: make_string_output_stream() -->
### Function: make_string_output_stream ()

Gibt einen Datenstrom zuruck, der Schriftzeichen aufnehmen kann. Die aktuell  
im Strom enthaltenden Zeichen konnen mit `get_output_stream_string` 
entnommen werden.

 

```maxima
(%i1) ostream : make_string_output_stream();
(%o1)               #<string-output stream 09622ea0>
(%i2) printf(ostream, "foo")$

(%i3) printf(ostream, "bar")$

(%i4) string : get_output_stream_string(ostream);
(%o4)                            foobar
(%i5) printf(ostream, "baz")$

(%i6) string : get_output_stream_string(ostream);
(%o6)                              baz
(%i7) close(ostream)$
```

See also: `get_output_stream_string`.

<!-- category: IO -->
<!-- keywords: newline -->
<!-- signatures: newline(), newline(stream) -->
### Function: newline ()

Schreibt einen Zeilenumbruch in den Standardausgabestrom und gibt `false` 
zuruck. Bei der Verwendung des optionalen Arguments *stream* wird der 
Umbruch in diesen Datenstrom geschrieben. 
Es gibt Situationen, in denen `newline()` nicht wie erwartet funktioniert.


Beispiel: Siehe `sprint`.

See also: `sprint`.

<!-- category: IO -->
<!-- keywords: opena -->
<!-- signatures: opena(file) -->
### Function: opena (file)

Gibt einen Dateiausgabestrom fur Schriftzeichen zuruck. 
Sollte die Textdatei *file* nicht existieren, wird sie erzeugt. 
Wird eine bereits vorhandene Datei geoffnet, werden alle Ausgaben in die 
Datei am Ende hinzugefugt.


`Functions-and-Variables-for-binary-input-and-output` 
ist die entsprechende Funktion fur die Ausgabe in eine Binardatei.

See also: `Functions-and-Variables-for-binary-input-and-output`.

<!-- category: IO -->
<!-- keywords: openr -->
<!-- signatures: openr(file) -->
### Function: openr (file)

Gibt einen Dateieingabestrom fur Schriftzeichen aus einer Textdatei zuruck. 
Voraussetzung ist, dass die Datei *file* bereits existiert. 


`Functions-and-Variables-for-binary-input-and-output` 
ist die entsprechende Funktion fur die Eingabe aus einer Binardatei.

See also: `Functions-and-Variables-for-binary-input-and-output`.

<!-- category: IO -->
<!-- keywords: openw -->
<!-- signatures: openw(file) -->
### Function: openw (file)

Gibt einen Dateiausgabestrom fur Schriftzeichen zuruck. 
Sollte die Textdatei *file* nicht existieren, wird sie erzeugt. 
Wird eine bereits vorhandene Datei geoffnet, wird sie destruktiv verandert. 


`Functions-and-Variables-for-binary-input-and-output` 
ist die entsprechende Funktion fur die Ausgabe in eine Binardatei.

See also: `Functions-and-Variables-for-binary-input-and-output`.

<!-- category: IO -->
<!-- keywords: parse_string -->
<!-- signatures: parse_string(str) -->
### Function: parse_string (str)

Parse the string *str* as a Maxima expression (do not evaluate it).  The 
string *str* may or may not have a terminator (dollar sign `$` or 
semicolon `;`).  Only the first expression is parsed, if there is more 
than one.


Complain if *str* is not a string.


See also `eval_string`.


Examples:



```maxima
(%i1) parse_string ("foo: 42; bar: foo^2 + baz");
(%o1)                    foo : 42
(%i2) parse_string ("(foo: 42, bar: foo^2 + baz)");
                                   2
(%o2)          (foo : 42, bar : foo  + baz)
```

See also: `eval_string`.

<!-- category: IO -->
<!-- keywords: printf -->
<!-- signatures: printf(dest, string), printf(dest, string, expr_1, ..., expr_n) -->
### Function: printf (dest, string)

Erzeugt eine formatierte Ausgabe. Der Zielparameter *dest* gibt an, wo die 
Ausgabe erfolgen soll. Moglich sind hier ein Ausgabestrom oder die globalen 
Variablen `true` und `false`. `true` bewirkt eine Ausgabe im Terminal. 
Der Ruckgabewert von `printf` ist in diesem Fall `false`. 
`false` als Zielparameter bewirkt die Ausgabe im Ruckgabewert. 


Die Zeichen des Kontrollparameters *string* werden der Reihe nach ausgegeben, 
wobei jedoch eine Tilde eine Direktive einleitet. Die Direktiven verwenden 
dann im Allgemeinen die nachstehenden Parameter *expr_1*, ..., *expr_n*, 
um die Ausgabe zu erzeugen. Das Zeichen nach der Tilde gibt dabei an, 
welche Art der Formatierung gewunscht ist. 


`printf` stellt die Common Lisp Funktion `format` in Maxima zur Verfugung. 
Das folgende Beispiel zeigt die grundsatzliche Beziehung zwischen diesen 
beiden Funktionen.



```maxima
(%i1) printf(true, "R~dD~d~%", 2, 2);
R2D2
(%o1)                                false
(%i2) :lisp (format t "R~dD~d~%" 2 2)
R2D2
NIL
```


Die folgende Beschreibung und die Beispiele beschranken sich auf eine grobe 
Skizze der Verwendungsmoglichkeiten von `printf`.  
Die Lisp Funktion `format` ist in vielen Referenzbuchern ausfuhrlich 
beschrieben. Eine hilfreiche Quelle ist z.B. das frei verfugbare Online-Manual 
"Common Lisp the Language" von Guy L. Steele. Siehe dort das Kapitel 22.3.3. 



```maxima
~%       new line
   ~&       fresh line
   ~t       tab
   ~$       monetary
   ~d       decimal integer
   ~b       binary integer
   ~o       octal integer
   ~x       hexadecimal integer
   ~br      base-b integer
   ~r       spell an integer
   ~p       plural
   ~f       floating point
   ~e       scientific notation
   ~g       ~f or ~e, depending upon magnitude
   ~h       bigfloat
   ~a       uses Maxima function string
   ~s       like ~a, but output enclosed in "double quotes"
   ~~       ~
   ~<       justification, ~> terminates
   ~(       case conversion, ~) terminates 
   ~[       selection, ~] terminates 
   ~{       iteration, ~} terminates
```


Die Direktive ~h fur Gleitkommazahlen mit beliebiger Genauigkeit 
entspricht nicht dem Lisp-Standard und wird daher unten naher beschrieben. 


Die Direktive ~* wird nicht unterstutzt.


Ist *dest* ein Datenstrom oder `true`, gibt `printf` 
`false` zuruck. Andernfalls ist der Ruckgabewert eine Zeichenkette.



```maxima
(%i1) printf( false, "~a ~a ~4f ~a ~@r", 
              "String",sym,bound,sqrt(12),144), bound = 1.234;
(%o1)                 String sym 1.23 2*sqrt(3) CXLIV
(%i2) printf( false,"~{~a ~}",["one",2,"THREE"] );
(%o2)                          one 2 THREE 
(%i3) printf( true,"~{~{~9,1f ~}~%~}",mat ),
          mat = args(matrix([1.1,2,3.33],[4,5,6],[7,8.88,9]))$
      1.1       2.0       3.3 
      4.0       5.0       6.0 
      7.0       8.9       9.0 
(%i4) control: "~:(~r~) bird~p ~[is~;are~] singing."$
(%i5) printf( false, control, n,n, if n = 1 then 1 else 2 ), n = 2;
(%o5)                    Two birds are singing.
```


Die Direktive ~h wurde fur Gleitkommazahlen mit beliebiger Genauigkeit 
eingefuhrt.



```maxima
~w,d,e,x,o,p@H
 w : width
 d : decimal digits behind floating point
 e : minimal exponent digits
 x : preferred exponent
 o : overflow character
 p : padding character
 @ : display sign for positive numbers
```



```maxima
(%i1) fpprec : 1000$
(%i2) printf(true, "|~h|~%", 2.b0^-64)$
|0.0000000000000000000542101086242752217003726400434970855712890625|
(%i3) fpprec : 26$
(%i4) printf(true, "|~h|~%", sqrt(2))$
|1.4142135623730950488016887|
(%i5) fpprec : 24$
(%i6) printf(true, "|~h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i7) printf(true, "|~28h|~%", sqrt(2))$
|   1.41421356237309504880169|
(%i8) printf(true, "|~28,,,,,'*h|~%", sqrt(2))$
|***1.41421356237309504880169|
(%i9) printf(true, "|~,18h|~%", sqrt(2))$
|1.414213562373095049|
(%i10) printf(true, "|~,,,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-3|
(%i11) printf(true, "|~,,2,-3h|~%", sqrt(2))$
|1414.21356237309504880169b-03|
(%i12) printf(true, "|~20h|~%", sqrt(2))$
|1.41421356237309504880169|
(%i13) printf(true, "|~20,,,,'+h|~%", sqrt(2))$
|++++++++++++++++++++|
```

<!-- category: IO -->
<!-- keywords: readbyte -->
<!-- signatures: readbyte(stream) -->
### Function: readbyte (stream)

Entfernt das erste Byte aus dem binaren Eingabestrom *stream* und gibt es 
zuruck. 
Ist das Ende der Datei (EOF) erreicht, wird `false` zuruck gegeben.


Beispiel: Die ersten 16 Byte aus einer mit AES in OpenSSL verschlusselten 
Datei werden gelesen und ausgewertet. 



```maxima
(%i1) ibase: obase: 16.$

(%i2) in: openr_binary("msg.bin");
(%o2)                       #<input stream msg.bin>
(%i3) (L:[],  thru 16. do push(readbyte(in), L),  L:reverse(L));
(%o3) [53, 61, 6C, 74, 65, 64, 5F, 5F, 88, 56, 0DE, 8A, 74, 0FD, 0AD, 0F0]
(%i4) close(in);
(%o4)                                true
(%i5) map(ascii, rest(L,-8));
(%o5)                      [S, a, l, t, e, d, _, _]
(%i6) salt: octets_to_number(rest(L,8));
(%o6)                          8856de8a74fdadf0
```

<!-- category: IO -->
<!-- keywords: readchar -->
<!-- signatures: readchar(stream) -->
### Function: readchar (stream)

Entfernt und gibt das erste Schriftzeichen in *stream* zuruck. 
Falls das Ende des Streams erreicht sein sollte, gibt `readchar` 
`false` zuruck.


Beispiel: Siehe `make_string_input_stream`.

See also: `make_string_input_stream`.

<!-- category: IO -->
<!-- keywords: readline -->
<!-- signatures: readline(stream) -->
### Function: readline (stream)

Gibt die Zeichenkette zuruck, die samtliche Zeichen von der 
aktuellen Position in *stream* bis zum Ende der Zeile enthalt 
oder `false`, falls das Ende der Datei erreicht wurde.

<!-- category: IO -->
<!-- keywords: scopy -->
<!-- signatures: scopy(string) -->
### Function: scopy (string)

Gibt eine Kopie der Zeichenkette *string* als neue Zeichenkette zuruck.

<!-- category: IO -->
<!-- keywords: sdowncase -->
<!-- signatures: sdowncase(string), sdowncase(string, start), sdowncase(string, start, end) -->
### Function: sdowncase (string)

Arbeitet wie `supcase`, jedoch werden Groß- in Kleinbuchstaben umgewandelt.

See also: `supcase`.

<!-- category: IO -->
<!-- keywords: sequal -->
<!-- signatures: sequal(string_1, string_2) -->
### Function: sequal (string_1, string_2)

Gibt `true` zuruck, wenn *string_1* und *string_2* die selbe 
Zeichensequenz enthalten.

<!-- category: IO -->
<!-- keywords: sequalignore -->
<!-- signatures: sequalignore(string_1, string_2) -->
### Function: sequalignore (string_1, string_2)

Arbeitet wie `sequal`, ignoriert jedoch die Groß- und Kleinschreibung,  
was fur Nicht-US-ASCII-Zeichen nur moglich ist, wenn das unter Maxima liegende 
Lisp einen Buchstaben auch als Buchstaben eines Alphabets erkennen kann.
Siehe hierzu die Bemerkungen zu `alphacharp`.

See also: `sequal`, `alphacharp`.

<!-- category: IO -->
<!-- keywords: sexplode -->
<!-- signatures: sexplode(string) -->
### Function: sexplode (string)

`sexplode` ist ein Alias fur die Funktion `charlist`.

See also: `charlist`.

<!-- category: IO -->
<!-- keywords: simplode -->
<!-- signatures: simplode(list), simplode(list, delim) -->
### Function: simplode (list)

`simplode` takes a list of expressions and concatenates them into a string.
If no delimiter *delim* is specified, `simplode` uses no delimiter.
*delim* can be any string.


Examples:



```maxima
(%i1) simplode(["xx[",3,"]:",expand((x+y)^3)]);
(%o1)             xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
(%i2) simplode( sexplode("stars")," * " );
(%o2)                   s * t * a * r * s
(%i3) simplode( ["One","more","coffee."]," " );
(%o3)                   One more coffee.
```

<!-- category: IO -->
<!-- keywords: sinsert -->
<!-- signatures: sinsert(seq, string, pos) -->
### Function: sinsert (seq, string, pos)

Returns a string that is a concatenation of `substring (string, 1, pos - 1)`, the string *seq* and `substring (string, pos)`.  Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) s: "A submarine."$
(%i2) concat( substring(s,1,3),"yellow ",substring(s,3) );
(%o2)                  A yellow submarine.
(%i3) sinsert("hollow ",s,3);
(%o3)                  A hollow submarine.
```

<!-- category: IO -->
<!-- keywords: sinvertcase -->
<!-- signatures: sinvertcase(string), sinvertcase(string, start), sinvertcase(string, start, end) -->
### Function: sinvertcase (string)

Returns *string* except that each character from position *start* to 
*end* is inverted.  If *end* is not given, all characters from 
*start* to the end of *string* are replaced.


Examples:



```maxima
(%i1) sinvertcase("sInvertCase");
(%o1)                      SiNVERTcASE
```

<!-- category: IO -->
<!-- keywords: slength -->
<!-- signatures: slength(string) -->
### Function: slength (string)

Gibt die Anzahl der Zeichen in der Zeichenkette *string* zuruck.

<!-- category: IO -->
<!-- keywords: smake -->
<!-- signatures: smake(num, char) -->
### Function: smake (num, char)

Gibt eine neue Zeichenkette mit *num* Zeichen *char* zuruck.


Beispiel:



```maxima
(%i1) smake(3,"w");
(%o1)                          www
```

<!-- category: IO -->
<!-- keywords: smismatch -->
<!-- signatures: smismatch(string_1, string_2), smismatch(string_1, string_2, test) -->
### Function: smismatch (string_1, string_2)

Returns the position of the first character of *string_1* at which 
*string_1* and *string_2* differ or `false`.  Default test function
for matching is `sequal`.  If `smismatch` should ignore case, use 
`sequalignore` as test.


Example:



```maxima
(%i1) smismatch("seven","seventh");
(%o1)                           6
```

See also: `sequal`, `sequalignore`.

<!-- category: IO -->
<!-- keywords: space -->
<!-- signatures: space -->
### Variable: space

Das Leerzeichen.

<!-- category: IO -->
<!-- keywords: split -->
<!-- signatures: split(string), split(string, delim), split(string, delim, multiple) -->
### Function: split (string)

Returns the list of all tokens in *string*.
Each token is an unparsed string.
`split` uses *delim* as delimiter.
If *delim* is not given, the space character is the default delimiter.
*multiple* is a boolean variable with `true` by default.
Multiple delimiters are read as one.
This is useful if tabs are saved as multiple space characters.
If *multiple* is set to `false`, each delimiter is noted.


Examples:



```maxima
(%i1) split("1.2   2.3   3.4   4.5");
(%o1)                 [1.2, 2.3, 3.4, 4.5]
(%i2) split("first;;third;fourth",";",false);
(%o2)               [first, , third, fourth]
```

<!-- category: IO -->
<!-- keywords: sposition -->
<!-- signatures: sposition(char, string) -->
### Function: sposition (char, string)

Returns the position of the first character in *string* which matches 
*char*.  The first character in *string* is in position 1.
For matching characters ignoring case see `ssearch`.

See also: `ssearch`.

<!-- category: IO -->
<!-- keywords: sprint -->
<!-- signatures: sprint(expr_1, ..., expr_n) -->
### Function: sprint (expr_1, ..., expr_n)

Wertet ihre Argumente der Reihe nach von links nach rechts aus und gibt sie dann 
auf einer Linie aus. Zeilenbegrenzungen werden dabei außer Acht gelassen. 
An die ausgegebenen Ausdrucke wird jeweils rechts ein Leerzeichen angefugt. 


Beispiel: Sequentielle Ausgabe mit `sprint`. 
Zeilenumbruche werden hier mit `newline()` erzeugt.



```maxima
(%i1) for n:0 thru 19 do sprint(fib(n))$
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
(%i2) for n:0 thru 22 do ( 
         sprint(fib(n)), 
         if mod(n,10) = 9 then newline() )$
0 1 1 2 3 5 8 13 21 34 
55 89 144 233 377 610 987 1597 2584 4181 
6765 10946 17711
```

<!-- category: IO -->
<!-- keywords: sremove -->
<!-- signatures: sremove(seq, string), sremove(seq, string, test), sremove(seq, string, test, start), sremove(seq, string, test, start, end) -->
### Function: sremove (seq, string)

Returns a string like *string* but without all substrings matching 
*seq*.  Default test function for matching is `sequal`.  
If `sremove` should ignore case while searching for *seq*, 
use `sequalignore` as test.  Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.


Examples:



```maxima
(%i1) sremove("n't","I don't like coffee.");
(%o1)                   I do like coffee.
(%i2) sremove ("DO ",%,'sequalignore);
(%o2)                    I like coffee.
```

See also: `sequal`, `sequalignore`.

<!-- category: IO -->
<!-- keywords: sremovefirst -->
<!-- signatures: sremovefirst(seq, string), sremovefirst(seq, string, test), sremovefirst(seq, string, test, start), sremovefirst(seq, string, test, start, end) -->
### Function: sremovefirst (seq, string)

Like `sremove` except that only the first substring that matches `seq`
is removed.

<!-- category: IO -->
<!-- keywords: sreverse -->
<!-- signatures: sreverse(string) -->
### Function: sreverse (string)

Gibt eine Zeichenkette mit allen Zeichen von *string* in umgekehrter 
Reihenfolge zuruck.

<!-- category: IO -->
<!-- keywords: ssearch -->
<!-- signatures: ssearch(seq, string), ssearch(seq, string, test), ssearch(seq, string, test, start), ssearch(seq, string, test, start, end) -->
### Function: ssearch (seq, string)

Returns the position of the first substring of *string* that matches the 
string *seq*.  Default test function for matching is `sequal`. 
If `ssearch` should ignore case, use `sequalignore` as test.  
Use *start* and *end* to limit searching.  Note that the first character in 
*string* is in position 1.



```maxima
(%i1) ssearch("~s","~{~S ~}~%",'sequalignore);
(%o1)                                  4
```

See also: `sequal`, `sequalignore`.

<!-- category: IO -->
<!-- keywords: ssort -->
<!-- signatures: ssort(string), ssort(string, test) -->
### Function: ssort (string)

Returns a string that contains all characters from *string* in an order such
there are no two successive characters *c* and *d* such that
`test (c, d)` is `false` and `test (d, c)` is `true`.  Default test function for sorting is
`clessp`.  The set of test functions is 
`{clessp, clesspignore, cgreaterp, cgreaterpignore, cequal, cequalignore}`.



```maxima
(%i1) ssort("I don't like Mondays.");
(%o1)                    '.IMaddeiklnnoosty
(%i2) ssort("I don't like Mondays.",'cgreaterpignore);
(%o2)                 ytsoonnMlkIiedda.'
```

See also: `clessp`, `clesspignore`, `cgreaterp`, `cgreaterpignore`, `cequal`, `cequalignore`.

<!-- category: IO -->
<!-- keywords: ssubst -->
<!-- signatures: ssubst(new, old, string), ssubst(new, old, string, test), ssubst(new, old, string, test, start), ssubst(new, old, string, test, start, end) -->
### Function: ssubst (new, old, string)

Returns a string like *string* except that all substrings matching *old*
are replaced by *new*.  *old* and *new* need not to be of the same 
length.  Default test function for matching is `sequal`.  If
`ssubst` should ignore case while searching for old, use 
`sequalignore` as test.  Use *start* and *end* to limit searching.
Note that the first character in *string* is in position 1.



```maxima
(%i1) ssubst("like","hate","I hate Thai food. I hate green tea.");
(%o1)          I like Thai food. I like green tea.
(%i2) ssubst("Indian","thai",%,'sequalignore,8,12);
(%o2)         I like Indian food. I like green tea.
```

See also: `sequal`, `sequalignore`.

<!-- category: IO -->
<!-- keywords: ssubstfirst -->
<!-- signatures: ssubstfirst(new, old, string), ssubstfirst(new, old, string, test), ssubstfirst(new, old, string, test, start), ssubstfirst(new, old, string, test, start, end) -->
### Function: ssubstfirst (new, old, string)

Like `subst` except that only the first substring that matches *old*
is replaced.

See also: `subst`.

<!-- category: IO -->
<!-- keywords: strim -->
<!-- signatures: strim(seq, string) -->
### Function: strim (seq, string)

Returns a string like *string*, but with all characters that appear in 
*seq* removed from both ends.



```maxima
(%i1) "/* comment */"$
(%i2) strim(" /*",%);
(%o2)                        comment
(%i3) slength(%);
(%o3)                           7
```

<!-- category: IO -->
<!-- keywords: striml -->
<!-- signatures: striml(seq, string) -->
### Function: striml (seq, string)

Like `strim` except that only the left end of *string* is trimmed.

See also: `strim`.

<!-- category: IO -->
<!-- keywords: strimr -->
<!-- signatures: strimr(seq, string) -->
### Function: strimr (seq, string)

Like `strim` except that only the right end of string is trimmed.

See also: `strim`.

<!-- category: IO -->
<!-- keywords: stringp -->
<!-- signatures: stringp(obj) -->
### Function: stringp (obj)

Gibt `true` zuruck, wenn *obj* eine Zeichenkette ist.


Beispiel: Siehe Einfuhrung.

<!-- category: IO -->
<!-- keywords: substring -->
<!-- signatures: substring(string, start), substring(string, start, end) -->
### Function: substring (string, start)

Returns the substring of *string* beginning at position *start* and 
ending at position *end*.  The character at position *end* is not 
included.  If *end* is not given, the substring contains the rest of the 
string.  Note that the first character in *string* is in position 1.



```maxima
(%i1) substring("substring",4);
(%o1)                        string
(%i2) substring(%,4,6);
(%o2)                          in
```

<!-- category: IO -->
<!-- keywords: supcase -->
<!-- signatures: supcase(string), supcase(string, start), supcase(string, start, end) -->
### Function: supcase (string)

Returns *string* except that lowercase characters from position *start* 
to *end* are replaced by the corresponding uppercase ones.  If *end* is 
not given, all lowercase characters from *start* to the end of *string* 
are replaced.



```maxima
(%i1) supcase("english",1,2);
(%o1)                        English
```

<!-- category: IO -->
<!-- keywords: tab -->
<!-- signatures: tab -->
### Variable: tab

Das Tabulatorzeichen.

<!-- category: IO -->
<!-- keywords: tokens -->
<!-- signatures: tokens(string), tokens(string, test) -->
### Function: tokens (string)

Returns a list of tokens, which have been extracted from *string*.
The tokens are substrings whose characters satisfy a certain test function.
If *test* is not given, *constituent* is used as the default test.
`{constituent, alphacharp, digitcharp, lowercasep, uppercasep, charp, characterp, alphanumericp}` is the set of test functions. 
(The Lisp-version of `tokens` is written by Paul Graham. ANSI Common Lisp, 1996, page 67.)



```maxima
(%i1) tokens("24 October 2005");
(%o1)                  [24, October, 2005]
(%i2) tokens("05-10-24",'digitcharp);
(%o2)                     [05, 10, 24]
(%i3) map(parse_string,%);
(%o3)                      [5, 10, 24]
```

<!-- category: IO -->
<!-- keywords: unicode -->
<!-- signatures: unicode(arg) -->
### Function: unicode (arg)

Gibt das durch *arg* definierte Schriftzeichen zuruck. 
*arg* kann ein Unicode Codepunkt oder auch eine Zeichenkette mit einem Namen sein, 
falls das unter Maxima liegende Lisp Unicode vollstandig unterstutzt.


Beispiel: Durch hexadezimale Codepunkte definierte Schriftzeichen
(Maxima kompiliert mit SBCL in GNU/Linux). 



```maxima
(%i1) ibase: 16.$
(%i2) map(unicode, [24, 0A3, 20AC]);
(%o2)                            [$, GBP, EUR]
```


Warnung: In wxMaxima in Windows ist es nicht moglich, 
Codepunkte großer 16 Bit in Schriftzeichen umzuwandeln,
wenn Maxima mit SBCL kompiliert wurde 
und das aktuelle externe Format nicht UTF-8 ist. 
Siehe `adjust_external_format` fur weitere Informationen.








CMUCL verarbeitet keine Codepunkte großer 16 Bit.
`unicode` gibt dann `false` zuruck. 
Als Ausweg kann hier die Umwandlung der Codepunkte in Schriftzeichen uber 
UTF-8-Oktette dienen: 


`octets_to_string(unicode_to_utf8(code_point));`








Siehe `octets_to_string`, `unicode_to_utf8`.


Falls das unter Maxima liegende Lisp Unicode vollstandig unterstutzt, 
kann ein Schriftzeichen durch seinen Namen angegeben werden.


Das folgende Beispiel ist mit ECL, CLISP und SBCL moglich, wobei mit SBCL in 
wxMaxima in Windows das externe Format auf UTF-8 gesetzt werden muss.
`unicode(name)` wird auch von CMUCL unterstutzt, jedoch wieder beschrankt 
auf 16-Bit-Zeichen.


Die Zeichenkette als Argument fur `unicode` muss prinzipiell die sein, 
die `printf` mit der Spezifikation "~@c" zuruck gibt,  
jedoch, wie unten gezeigt, ohne den Prafix "#\". 
Unterstriche konnen durch Leerzeichen und Groß- durch Kleinbuchstaben 
ersetzt werden.


Beispiel (fortgesetzt): Ein Schriftzeichen ist durch seinen Namen gegeben 
(Maxima kompiliert mit SBCL in GNU/Linux). 



```maxima
(%i3) printf(false, "~@c", unicode(0DF));
(%o3)                    #\LATIN_SMALL_LETTER_SHARP_S
(%i4) unicode("LATIN_SMALL_LETTER_SHARP_S");
(%o4)                                  ß
(%i5) unicode("Latin small letter sharp S");
(%o5)                                  ß
```

See also: `adjust_external_format`, `octets_to_string`, `unicode_to_utf8`.

<!-- category: IO -->
<!-- keywords: unicode_to_utf8 -->
<!-- signatures: unicode_to_utf8(code_point) -->
### Function: unicode_to_utf8 (code_point)

Gibt eine Liste mit UTF-8-Code zuruck, der dem Unicode *code_point* entspricht. 


Beispiel: Umwandlung von Unicode Codepunkten in UTF-8 und umgekehrt. 



```maxima
(%i1) ibase: obase: 16.$
(%i2) map(cint, ["$","GBP","EUR"]);
(%o2)                           [24, 0A3, 20AC]
(%i3) map(unicode_to_utf8, %);
(%o3)                 [[24], [0C2, 0A3], [0E2, 82, 0AC]]
(%i4) map(utf8_to_unicode, %);
(%o4)                           [24, 0A3, 20AC]
```

<!-- category: IO -->
<!-- keywords: uppercasep -->
<!-- signatures: uppercasep(char) -->
### Function: uppercasep (char)

Gibt `true` zuruck, wenn *char* ein Großbuchstabe ist.


Hinweis: Siehe Bemerkungen zu `alphacharp`.

See also: `alphacharp`.

<!-- category: IO -->
<!-- keywords: us_ascii_only -->
<!-- signatures: us_ascii_only -->
### Variable: us_ascii_only

Diese Optionsvariable beeinflusst Maxima, wenn die Zeichenkodierung der 
Anwendung, in der Maxima lauft, UTF-8 ist, das externe Format des Lisp Readers 
jedoch nicht.


In GNU/Linux trifft dies zu, wenn Maxima mit GCL kompiliert wurde und 
in Windows in wxMaxima in GCL- und SBCL-Versionen. 
Es wird empfohlen, in der SBCL-Version das externe Format in UTF-8 abzuandern. 
Eine Festlegung von `us_ascii_only` wird damit unnotig. 
Siehe `adjust_external_format` fur Details. 


`us_ascii_only` ist standardmaßig `false`. 
Maxima analysiert dann (d.h. in der oben beschriebenen Situation) selbst die UTF-8-Kodierung.


Wurde `us_ascii_only` auf `true` gesetzt, wird angenommen, dass alle 
Zeichenketten, die als Argumente fur Funktionen des Pakets `stringproc` 
verwendet werden, nur ausschließlich US-ASCII-Zeichen enthalten. 
Durch diese Vereinbarung wird die UTF-8-Analyse des Inputs uberflussig 
und Zeichenketten konnen effizienter verarbeitet werden.

See also: `adjust_external_format`.

<!-- category: IO -->
<!-- keywords: utf8_to_unicode -->
<!-- signatures: utf8_to_unicode(list) -->
### Function: utf8_to_unicode (list)

Gibt den Unicode Codepunkt zuruck, der der Liste *list* entspricht, 
die die UTF-8-Kodierung eines einzelnen Schriftzeichens enthalten muss.


Beispiel: Siehe `unicode_to_utf8`.

See also: `unicode_to_utf8`.

<!-- category: IO -->
<!-- keywords: writebyte -->
<!-- signatures: writebyte(byte, stream) -->
### Function: writebyte (byte, stream)

Schreibt das Byte *byte* in den binaren Ausgabestrom *stream*. 
`writebyte` gibt `byte` zuruck.


Beispiel: Es werden Bytes in eine Binardatei geschrieben. 
In diesem Beispiel entsprechen samtliche Bytes druckbaren Zeichen, 
die mit Hilfe von `printfile` ausgegeben werden konnen. 
Die Bytes verbleiben so lange im Datenstrom, bis die Funktionen `flush_output` 
oder `close` aufgerufen werden.



```maxima
(%i1) ibase: obase: 16.$

(%i2) bytes: string_to_octets("GNU/Linux");
(%o2)                [47, 4E, 55, 2F, 4C, 69, 6E, 75, 78]
(%i3) out: openw_binary("test.bin");
(%o3)                      #<output stream test.bin>
(%i4) for i thru 3 do writebyte(bytes[i], out);
(%o4)                                done
(%i5) printfile("test.bin")$

(%i6) flength(out);
(%o6)                                  0
(%i7) flush_output(out);
(%o7)                                true
(%i8) flength(out);
(%o8)                                  3
(%i9) printfile("test.bin")$
GNU
(%i0A) for b in rest(bytes,3) do writebyte(b, out);
(%o0A)                               done
(%i0B) close(out);
(%o0B)                               true
(%i0C) printfile("test.bin")$
GNU/Linux
```

