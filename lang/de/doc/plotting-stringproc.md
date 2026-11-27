## stringproc

<!-- category: Plotting -->
<!-- keywords: base64 -->
<!-- signatures: base64(arg) -->
### Function: base64 (arg)

Gibt eine Base64-Darstellung von *arg* zuruck. 
Das Argument *arg* kann eine Zeichenkette, eine nicht-negative Ganzzahl 
oder eine Liste von Oktetten sein.


Beispiel:



```maxima
(%i1) base64: base64("foo bar baz");
(%o1)                          Zm9vIGJhciBiYXo=
(%i2) string: base64_decode(base64);
(%o2)                            foo bar baz
(%i3) obase: 16.$
(%i4) integer: base64_decode(base64, 'number);
(%o4)                       666f6f206261722062617a
(%i5) octets: base64_decode(base64, 'list);
(%o5)            [66, 6F, 6F, 20, 62, 61, 72, 20, 62, 61, 7A]
(%i6) ibase: 16.$
(%i7) base64(octets);
(%o7)                          Zm9vIGJhciBiYXo=
```


Sind in *arg* Umlaute oder Eszett enthalten (bzw. Oktette großer 
als 127), ist das Ergebnis von der verwendeten Plattform abhangig. 
Es wird aber durch eine Anwendung von `base64_decode` in jedem Fall 
wieder in die ursprungliche Zeichenkette zuruck verwandelt.

See also: `base64_decode`.

<!-- category: Plotting -->
<!-- keywords: base64_decode -->
<!-- signatures: base64_decode(base64-string), base64_decode(base64-string, return-type) -->
### Function: base64_decode (base64-string)

Dekodiert die Base64-kodierte Zeichenkette *base64-string* standardmaßig 
wieder zuruck in die ursprungliche Zeichenkette.


Das optionale Argument *return-type* erlaubt es `base64_decode`, 
alternativ hierzu auch die entsprechende Ganzzahl oder Liste von Oktetten 
zuruck zu geben.
*return-type* kann `string`, `number` oder `list` sein.


Beispiel: Siehe `base64`.

See also: `base64`.

<!-- category: Plotting -->
<!-- keywords: crc24sum -->
<!-- signatures: crc24sum(octets), crc24sum(octets, return-type) -->
### Function: crc24sum (octets)

Gibt standardmaßig die `CRC24`-Prufsumme einer Oktett-Liste als 
Zeichenkette zuruck.


Das optionale Argument *return-type* erlaubt es `crc24sum`, 
alternativ hierzu auch die entsprechende Ganzzahl oder Liste von Oktetten 
zuruck zu geben.
*return-type* kann `string`, `number` oder `list` sein.


Beispiel:


```maxima
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2.0.22 (GNU/Linux)

iQEcBAEBAgAGBQJVdCTzAAoJEG/1Mgf2DWAqCSYH/AhVFwhu1D89C3/QFcgVvZTM
wnOYzBUURJAL/cT+IngkLEpp3hEbREcugWp+Tm6aw3R4CdJ7G3FLxExBH/5KnDHi
rBQu+I7+3ySK2hpryQ6Wx5J9uZSa4YmfsNteR8up0zGkaulJeWkS4pjiRM+auWVe
vajlKZCIK52P080DG7Q2dpshh4fgTeNwqCuCiBhQ73t8g1IaLdhDN6EzJVjGIzam
/spqT/sTo6sw8yDOJjvU+Qvn6/mSMjC/YxjhRMaQt9EMrR1AZ4ukBF5uG1S7mXOH
WdiwkSPZ3gnIBhM9SuC076gLWZUNs6NqTeE3UzMjDAFhH3jYk1T7mysCvdtIkms=
=WmeC
-----END PGP SIGNATURE-----
```



```maxima
(%i1) ibase : obase : 16.$
(%i2) sig64 : sconcat(
 "iQEcBAEBAgAGBQJVdCTzAAoJEG/1Mgf2DWAqCSYH/AhVFwhu1D89C3/QFcgVvZTM",
 "wnOYzBUURJAL/cT+IngkLEpp3hEbREcugWp+Tm6aw3R4CdJ7G3FLxExBH/5KnDHi",
 "rBQu+I7+3ySK2hpryQ6Wx5J9uZSa4YmfsNteR8up0zGkaulJeWkS4pjiRM+auWVe",
 "vajlKZCIK52P080DG7Q2dpshh4fgTeNwqCuCiBhQ73t8g1IaLdhDN6EzJVjGIzam",
 "/spqT/sTo6sw8yDOJjvU+Qvn6/mSMjC/YxjhRMaQt9EMrR1AZ4ukBF5uG1S7mXOH",
 "WdiwkSPZ3gnIBhM9SuC076gLWZUNs6NqTeE3UzMjDAFhH3jYk1T7mysCvdtIkms=" )$
(%i3) octets: base64_decode(sig64, 'list)$
(%i4) crc24: crc24sum(octets, 'list);
(%o4)                          [5A, 67, 82]
(%i5) base64(crc24);
(%o5)                              WmeC
```

<!-- category: Plotting -->
<!-- keywords: md5sum -->
<!-- signatures: md5sum(arg), md5sum(arg, return-type) -->
### Function: md5sum (arg)

Gibt die `md5`-Prufsumme einer Zeichenkette, einer nicht-negativen Ganzzahl 
oder einer Liste von Oktetten zuruck. Der standardmaßige Ruckgabewert 
ist eine Zeichenkette mit 32 hexadezimalen Zeichen.


Das optionale Argument *return-type* erlaubt es `md5sum`, 
alternativ hierzu auch die entsprechende Ganzzahl oder Liste von Oktetten 
zuruck zu geben.
*return-type* kann `string`, `number` oder `list` sein.



Beispiel:



```maxima
(%i1) ibase: obase: 16.$
(%i2) msg: "foo bar baz"$
(%i3) string: md5sum(msg);
(%o3)                  ab07acbb1e496801937adfa772424bf7
(%i4) integer: md5sum(msg, 'number);
(%o4)                 0ab07acbb1e496801937adfa772424bf7
(%i5) octets: md5sum(msg, 'list);
(%o5)        [0AB,7,0AC,0BB,1E,49,68,1,93,7A,0DF,0A7,72,42,4B,0F7]
(%i6) sdowncase( printf(false, "~{~2,'0x~^:~}", octets) );
(%o6)           ab:07:ac:bb:1e:49:68:01:93:7a:df:a7:72:42:4b:f7
```


Sind in *arg* Umlaute oder andere Nicht-US-ASCII-Zeichen enthalten (bzw. Oktette 
großer als 127), ist das Ergebnis von der verwendeten Plattform abhangig.

<!-- category: Plotting -->
<!-- keywords: mgf1_sha1 -->
<!-- signatures: mgf1_sha1(seed, len), mgf1_sha1(seed, len, return-type) -->
### Function: mgf1_sha1 (seed, len)

Gibt eine Pseudozufallszahl variabler Lange zuruck. 
Standardmaßig ist dies eine Zahl mit einer Lange von *len* Oktetten.


Das optionale Argument *return-type* erlaubt es `mgf1_sha1`, 
alternativ hierzu die Liste mit den *len* entsprechenden Oktetten 
zuruck zu geben.
*return-type* kann `number` oder `list` sein.


Die Berechnung des Ruckgabewerts wird in der `RFC 3447` 
im Anhang `B.2.1 MGF1` beschrieben. 
Verwendet wird dabei `SHA1` als Hashfunktion, d.h. die Zufalligkeit der 
berechneten Zahl beruht auf der Zufalligkeit von `SHA1`-Hashwerten.


Beispiel:



```maxima
(%i1) ibase: obase: 16.$
(%i2) number: mgf1_sha1(4711., 8);
(%o2)                        0e0252e5a2a42fea1
(%i3) octets: mgf1_sha1(4711., 8, 'list);
(%o3)                  [0E0,25,2E,5A,2A,42,0FE,0A1]
```

<!-- category: Plotting -->
<!-- keywords: number_to_octets -->
<!-- signatures: number_to_octets(number) -->
### Function: number_to_octets (number)

Gibt eine Oktett-Darstellung der nicht-negativen Ganzzahl *number* in Form 
einer Liste zuruck. 


Beispiel:



```maxima
(%i1) ibase : obase : 16.$
(%i2) octets: [0ca,0fe,0ba,0be]$
(%i3) number: octets_to_number(octets);
(%o3)                            0cafebabe
(%i4) number_to_octets(number);
(%o4)                      [0CA, 0FE, 0BA, 0BE]
```

<!-- category: Plotting -->
<!-- keywords: octets_to_number -->
<!-- signatures: octets_to_number(octets) -->
### Function: octets_to_number (octets)

Fugt die in der Liste *octets* enthaltenden Oktette zu einer Zahl zusammen 
und gibt diese zuruck. 


Beispiel: Siehe `number_to_octets`.

See also: `number_to_octets`.

<!-- category: Plotting -->
<!-- keywords: octets_to_oid -->
<!-- signatures: octets_to_oid(octets) -->
### Function: octets_to_oid (octets)

Berechnet eine Objektkennung (OID) aus einer Liste von Oktetten.


Beispiel: RSA encryption OID



```maxima
(%i1) ibase : obase : 16.$
(%i2) oid: octets_to_oid([2A,86,48,86,0F7,0D,1,1,1]);
(%o2)                      1.2.840.113549.1.1.1
(%i3) oid_to_octets(oid);
(%o3)               [2A, 86, 48, 86, 0F7, 0D, 1, 1, 1]
```

<!-- category: Plotting -->
<!-- keywords: octets_to_string -->
<!-- signatures: octets_to_string(octets), octets_to_string(octets, encoding) -->
### Function: octets_to_string (octets)

Dekodiert den aktuellen Systemstandards entsprechend die Liste *octets* 
in eine Zeichenkette. 
Bei der Dekodierung von Oktetten, die nicht ausschließlich US-ASCII-Zeichen 
entsprechen, ist das Ergebnis abhangig von der Plattform, der Anwendung und vom 
unter Maxima liegenden Lisp. 


Beispiel: Die Verwendung des Systemstandards 
(Maxima kompiliert mit GCL, das keine Format-Definition verwendet und die 
vom GNU/Linux Terminal kodierten UTF-8-Oktette ungeandert an Maxima weitergibt).



```maxima
(%i1) octets: string_to_octets("abc");
(%o1)                            [61, 62, 63]
(%i2) octets_to_string(octets);
(%o2)                                 abc
(%i3) ibase: obase: 16.$
(%i4) unicode(20AC);
(%o4)                                  EUR
(%i5) octets: string_to_octets(%);
(%o5)                           [0E2, 82, 0AC]
(%i6) octets_to_string(octets);
(%o6)                                  EUR
(%i7) utf8_to_unicode(octets);
(%o7)                                20AC
```


In dem Fall, dass UTF-8 das externe Format des Lisp Readers ist, kann das 
optionale Argument *encoding* genutzt werden, um fur die Oktett-String-Umwandlung 
eine gewünschte Kodierung auszuwahlen. 
Siehe `adjust_external_format`, falls es notwendig sein sollte, hierfur das 
externe Format zu andern.


Die Namen einiger unterstutzter Kodierungen 
(weitere siehe das entsprechende Lisp Manual): 

CCL, CLISP, SBCL: `utf-8, ucs-2be, ucs-4be, iso-8859-1, cp1252, cp850` 

CMUCL: `utf-8, utf-16-be, utf-32-be, iso8859-1, cp1252` 

ECL: `utf-8, ucs-2be, ucs-4be, iso-8859-1, windows-cp1252, dos-cp850` 


Beispiel (fortgesetzt): Die Verwendung des optionalen Arguments 
(Maxima kompiliert mit SBCL, GNU/Linux Terminal).



```maxima
(%i8) string_to_octets("EUR", "ucs-2be");
(%o8)                              [20, 0AC]
```

See also: `adjust_external_format`.

<!-- category: Plotting -->
<!-- keywords: oid_to_octets -->
<!-- signatures: oid_to_octets(oid-string) -->
### Function: oid_to_octets (oid-string)

Verwandelt eine Objektkennung (OID) in eine Liste von Oktetten.


Beispiel: Siehe `octets_to_oid`.

See also: `octets_to_oid`.

<!-- category: Plotting -->
<!-- keywords: sha1sum -->
<!-- signatures: sha1sum(arg), sha1sum(arg, return-type) -->
### Function: sha1sum (arg)

Gibt den `SHA1`-Fingerabdruck einer Zeichenkette, einer nicht-negativen Ganzzahl 
oder einer Liste von Oktetten zuruck. Der standardmaßige Ruckgabewert 
ist eine Zeichenkette mit 40 hexadezimalen Zeichen.


Das optionale Argument *return-type* erlaubt es `sha1sum`, 
alternativ hierzu auch die entsprechende Ganzzahl oder Liste von Oktetten 
zuruck zu geben.
*return-type* kann `string`, `number` oder `list` sein.


Beispiel:



```maxima
(%i1) ibase: obase: 16.$
(%i2) msg: "foo bar baz"$
(%i3) string: sha1sum(msg);
(%o3)              c7567e8b39e2428e38bf9c9226ac68de4c67dc39
(%i4) integer: sha1sum(msg, 'number);
(%o4)             0c7567e8b39e2428e38bf9c9226ac68de4c67dc39
(%i5) octets: sha1sum(msg, 'list);
(%o5)  [0C7,56,7E,8B,39,0E2,42,8E,38,0BF,9C,92,26,0AC,68,0DE,4C,67,0DC,39]
(%i6) sdowncase( printf(false, "~{~2,'0x~^:~}", octets) );
(%o6)     c7:56:7e:8b:39:e2:42:8e:38:bf:9c:92:26:ac:68:de:4c:67:dc:39
```


Sind in *arg* Umlaute oder andere Nicht-US-ASCII-Zeichen enthalten (bzw. Oktette 
großer als 127), ist der `SHA1`-Fingerabdruck von der verwendeten 
Plattform abhangig.

<!-- category: Plotting -->
<!-- keywords: sha256sum -->
<!-- signatures: sha256sum(arg), sha256sum(arg, return-type) -->
### Function: sha256sum (arg)

Gibt den `SHA256`-Fingerabdruck einer Zeichenkette, einer nicht-negativen 
Ganzzahl oder einer Liste von Oktetten zuruck. Der standardmaßige 
Ruckgabewert ist eine Zeichenkette mit 64 hexadezimalen Zeichen.


Das optionale Argument *return-type* erlaubt es `sha256sum`, 
alternativ hierzu auch die entsprechende Ganzzahl oder Liste von Oktetten 
zuruck zu geben (siehe `sha1sum`).


Beispiel:



```maxima
(%i1) string: sha256sum("foo bar baz");
(%o1)  dbd318c1c462aee872f41109a4dfd3048871a03dedd0fe0e757ced57dad6f2d7
```


Sind in *arg* Umlaute oder andere Nicht-US-ASCII-Zeichen enthalten (bzw. Oktette 
großer als 127), ist der `SHA256`-Fingerabdruck von der verwendeten 
Plattform abhangig.

See also: `sha1sum`.

<!-- category: Plotting -->
<!-- keywords: string_to_octets -->
<!-- signatures: string_to_octets(string), string_to_octets(string, encoding) -->
### Function: string_to_octets (string)

Kodiert den aktuellen Systemstandards entsprechend die Zeichenkette *string* 
in eine Liste von Oktetten.
Bei der Kodierung von Zeichenketten, die nicht ausschließlich US-ASCII-Zeichen 
enthalten, ist das Ergebnis abhangig von der Plattform, der Anwendung und vom 
unter Maxima liegenden Lisp. 


In dem Fall, dass UTF-8 das externe Format des Lisp Readers ist, kann das 
optionale Argument *encoding* genutzt werden, um fur die String-Oktett-Umwandlung 
eine gewünschte Kodierung auszuwahlen. 
Siehe `adjust_external_format`, falls es notwendig sein sollte, hierfur das 
externe Format zu andern.


Siehe `octets_to_string` fur Beispiele und zusatzliche Informationen.

See also: `adjust_external_format`, `octets_to_string`.

