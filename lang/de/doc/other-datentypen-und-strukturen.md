## Datentypen und Strukturen

<!-- category: Other -->
<!-- keywords: %e -->
<!-- signatures: %e -->
### Variable: %e

`%e` ist die Basis des naturlichen Logarithmus, auch Eulersche Zahl 
genannt.  Der numerische Wert der Konstanten als Gleitkommazahl mit doppelter
Genauigkeit ist 2.718281828459045d0.


Die Funktion `bfloat` kann `%e` mit einer beliebigen Genauigkeit
berechnen.


Hat die Optionsvariable `numer` den Wert `true`, wird `%e` durch
den numerischen Wert ersetzt, aber nicht, wenn `%e` die Basis der
Exponentiation mit einem symbolischen Exponenten ist.  Hat zusatzlich die
Optionsvariable `%enumer` den Wert `true`, dann wird `%e` in
einem Ausdruck immer durch den numerischen Wert ersetzt.


Beispiel:


Berechnung von `%e` auf 48 Stellen.



```maxima
(%i1) fpprec: 48$
(%i2) bfloat(%e);
(%o2)  2.7182818284590452353602874713526624977572470937b0
```


Die Wirkung der Optionsvariablen `numer` und `%enumer` auf das 
Ersetzen von `%e` durch den numerischen Wert.



```maxima
(%i1) %e, numer;
(%o1)                   2.718281828459045
(%i2) %e^x, numer;
                                 x
(%o2)                          %e
(%i3) %e^x, numer, %enumer;
                                        x
(%o3)                  2.718281828459045
```


Im ersten Beispiel vereinfacht die Reihe zu `%e`.  Fur die Vereinfachung
der Reihe wird die Funktion `simplify_sum` geladen.  Im zweiten Beispiel
ist `%e` der Grenzwert.



```maxima
(%i1) load("simplify_sum")$

(%i2) sum(1/n!, n, 0, inf);
                            inf
                            ====
                            \     1
(%o2)                        >    --
                            /     n!
                            ====
                            n = 0
(%i3) simplify_sum(%);

(%o3)                          %e

(%i4) limit((1+x)^(1/x), x, 0);
(%o4)                          %e
```

See also: `bfloat`, `numer`, `%enumer`, `simplify_sum`.

<!-- category: Other -->
<!-- keywords: %gamma -->
<!-- signatures: %gamma -->
### Variable: %gamma

Die Euler-Mascheroni-Konstante mit dem Wert `0.5772156649015329` als
Gleitkommazahl in doppelter Genauigkeit.


Die Funktion `bfloat` kann `%gamma` mit einer beliebigen Genauigkeit
berechnen.


Hat die Optionsvariable `numer` den Wert `true`, wird die Konstante
`%gamma` durch ihren numerischen Wert ersetzt.  


Beispiele:


Numerische Werte fur `%gamma`.



```maxima
(%i1) %gamma, numer;
(%o1)                   .5772156649015329
(%i2) bfloat(%gamma), fpprec: 48;
(%o2)  5.7721566490153286060651209008240243104215933594b-1
```


Bestimmte Integrale, die `%gamma` als Ergebnis haben.



```maxima
(%i1) -integrate(exp(-t)*log(t), t, 0, inf);
(%o1)                        %gamma
(%i2) -integrate(log(log(1/t)),t, 0,1);
(%o2)                        %gamma
```

See also: `bfloat`, `numer`.

<!-- category: Other -->
<!-- keywords: %i -->
<!-- signatures: %i -->
### Variable: %i

`%i` ist die imaginare Einheit.


Maxima kennt keinen eigenen Typ fur komplexe Zahlen.  Komplexe Zahlen werden 
von Maxima intern als die Addition von Realteil und dem mit der imaginaren 
Einheit `%i` multiplizierten Imaginarteil dargestellt.  Zum Beispiel sind
die komplexen Zahlen `2 + 3*%i` und `2 - 3*%i` die Wurzeln der 
Gleichung `x^2 - 4*x + 13 = 0`.  Siehe auch das Kapitel
Zahlen.


Beispiele:


Einige Beispiele fur das Rechnen mit der imaginaren Einheit.



```maxima
(%i1) sqrt(-1);
(%o1)                          %i
(%i2) %i^2;
(%o2)                          - 1
(%i3) exp(%i*%pi/2);
(%o3)                          %i
(%i4) sin(%i*x);
(%o4)                      %i sinh(x)
```

See also: `%i`.

<!-- category: Other -->
<!-- keywords: %phi -->
<!-- signatures: %phi -->
### Variable: %phi

`%phi` reprasentiert die *Goldene Zahl* $(1 + sqrt(5))/2$.  Der
Wert als Gleitkommazahl in doppelter Genauigkeit ist 1.618033988749895d0.


Die Funktion `fibtophi` druckt Fibonacci-Zahlen `fib(n)` durch die
Goldene Zahl `%phi` aus.  Stan­dard­maßig kennt Maxima keine
algebraischen Eigenschaften der Konstanten `%phi`.  Mit den Eingaben
`tellrat(%phi^2-%phi-1)` und `algebraic: true` kann die Funktion
`ratsimp` einige Vereinfachungen ausfuhren.


Die Funktion `bfloat` kann `%phi` mit einer beliebigen Genauigkeit
berechnen.  Hat die Optionsvariable `numer` den Wert `true`, wird
die Konstante `%phi` durch ihren numerischen Wert ersetzt.


Beispiele:


Numerische Werte fur `%phi`.



```maxima
(%i1) %phi, numer;
(%o1)                   1.618033988749895
(%i2) bfloat(%phi), fpprec: 48;
(%o2)  1.61803398874989484820458683436563811772030917981b0
```


`fibtophi` druckt Fibonacci-Zahlen `fib(n)` durch `%phi` aus.



```maxima
(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1
(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)
(%i3) fibtophi (%);

            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1

(%i4) ratsimp (%);
(%o4)                           0
```


Mit den Eingaben `tellrat(%phi^2-%phi-1)` und `algebraic:true` kann 
die Funktion `ratsimp` einige Vereinfachungen fur Ausdrucke 
ausfuhren, die `%phi` enthalten.



```maxima
(%i1) e : expand ((%phi^2 - %phi - 1) * (A + 1));
                 2                      2
(%o1)        %phi  A - %phi A - A + %phi  - %phi - 1
(%i2) ratsimp (e);
                  2                     2
(%o2)        (%phi  - %phi - 1) A + %phi  - %phi - 1
(%i3) tellrat (%phi^2 - %phi - 1);
                            2
(%o3)                  [%phi  - %phi - 1]
(%i4) algebraic : true;
(%o4)                         true
(%i5) ratsimp (e);
(%o5)                           0
```

See also: `fibtophi`, `ratsimp`, `bfloat`, `numer`.

<!-- category: Other -->
<!-- keywords: %pi -->
<!-- signatures: %pi -->
### Variable: %pi

`%pi` reprasentiert die Kreiszahl.  Der numerische Wert als 
Gleitkommazahl in doppelter Genauigkeit ist `3.141592653589793d0`.


Die Funktion `bfloat` kann `%pi` mit einer beliebigen Genauigkeit
berechnen.  Hat die Optionsvariable `numer` den Wert `true`, wird die
Konstante `%pi` durch ihren numerischen Wert ersetzt.


Beispiele:


Numerische Werte fur `%pi`.



```maxima
(%i1) %pi, numer;
(%o1)                   3.141592653589793
(%i2) bfloat(%pi), fpprec:48;
(%o2)  3.14159265358979323846264338327950288419716939938b0
```


Grenzwert und bestimmte Integrale, die `%pi` als Ergebnis haben.



```maxima
(%i1) 'limit(n!^2*(n+1)^(2*n^2+n)/(2*n^(2*n^2+3*n+1)),n,inf);
                        2                     2
                   - 2 n  - 3 n - 1        2 n  + n   2
         limit    n                 (n + 1)         n!
         n -> inf
(%o1)    ----------------------------------------------
                               2
(%i2) %, nouns;
(%o2)                          %pi
(%i3) 'integrate(4*sqrt(1-t^2),t,0,1);
                         1
                        /
                        [            2
(%o3)                 4 I  sqrt(1 - t ) dt
                        ]
                        /
                         0
(%i4) %, nouns;
(%o4)                          %pi
(%i5) 'integrate(2*exp(-t^2),t,0,inf);
                           inf
                          /         2
                          [      - t
(%o5)                   2 I    %e     dt
                          ]
                          /
                           0
(%i6) %, nouns;
(%o6)                       sqrt(%pi)
```

See also: `bfloat`, `numer`.

<!-- category: Other -->
<!-- keywords: @ -->
<!-- signatures: @ -->
### Function: @

`@` ist der Operator fur den Zugriff auf ein Feld einer Struktur.  Der
Ausdruck `x@a` bezeichnet das Feld *a* der Instanz *x*
einer Struktur.  Der Feldname wird nicht ausgewertet.





Hat das Feld *a* der Instanz *x* keinen Wert, wird der Ausdruck
`x@a` zu sich selbst ausgewertet.




`kill(x@a)` loscht den Wert des Feldes *a* der Instanz
*x* einer Struktur.


Beispiele:



```maxima
(%i1) defstruct (foo (x, y, z));
(%o1)                    [foo(x, y, z)]
(%i2) u : new (foo (123, a - b, %pi));
(%o2)           foo(x = 123, y = a - b, z = %pi)
(%i3) u@z;
(%o3)                          %pi
(%i4) u@z : %e;
(%o4)                          %e
(%i5) u;
(%o5)            foo(x = 123, y = a - b, z = %e)
(%i6) kill (u@z);
(%o6)                         done
(%i7) u;
(%o7)              foo(x = 123, y = a - b, z)
(%i8) u@z;
(%o8)                          u@z
```




Der Feldname wird nicht ausgewertet.



```maxima
(%i1) defstruct (bar (g, h));
(%o1)                      [bar(g, h)]
(%i2) x : new (bar);
(%o2)                       bar(g, h)
(%i3) x@h : 42;
(%o3)                          42
(%i4) h : 123;
(%o4)                          123
(%i5) x@h;
(%o5)                          42
(%i6) x@h : 19;
(%o6)                          19
(%i7) x;
(%o7)                    bar(g, h = 19)
(%i8) h;
(%o8)                          123
```

<!-- category: Other -->
<!-- keywords: bfloat -->
<!-- signatures: bfloat(expr) -->
### Function: bfloat (expr)

Konvertiert alle Zahlen im Ausdruck *expr* in große Gleitkommazahlen.
Die Anzahl der Stellen wird durch die Optionsvariable 
`fpprec` spezifiziert.


Hat die Optionsvariable `float2bf` den Wert `false`, gibt Maxima eine
Warnung aus, wenn eine Gleitkommazahl mit doppelter Genauigkeit in eine 
große Gleitkommazahl umgewandelt wird.


Siehe auch die Funktion und den Auswertungsschalter `float` sowie die
Optionsvariable `numer` fur die Umwandlung von Zahlen in Gleitkommazahlen
mit doppelter Genauigkeit.


Beispiele:



```maxima
(%i1) bfloat([2, 3/2, 1.5]);
(%o1)                 [2.0b0, 1.5b0, 1.5b0]
(%i2) bfloat(sin(1/2));
(%o2)                  4.79425538604203b-1
(%i3) bfloat(%pi),fpprec:45;
(%o3)    3.1415926535897932384626433832795028841971694b0
```

See also: `fpprec`, `float2bf`, `float`, `numer`.

<!-- category: Other -->
<!-- keywords: bfloatp -->
<!-- signatures: bfloatp(number) -->
### Function: bfloatp (number)

Gibt den Wert `true` zuruck, wenn das Argument *number* eine
große Gleitkommazahl ist, ansonsten den Wert `false`.


Siehe auch die Funktionen `numberp`, `floatnump`,
`ratnump` und `integerp`.


Beispiele:



```maxima
(%i1) bfloatp(1.5b0);
(%o1)                         true
(%i2) a:bfloat(%e);
(%o2)                  2.718281828459045b0
(%i3) bfloatp(a);
(%o3)                         true
(%i4) bfloatp(1.5);
(%o4)                         false
```

See also: `numberp`, `floatnump`, `ratnump`, `integerp`.

<!-- category: Other -->
<!-- keywords: bftorat -->
<!-- signatures: bftorat -->
### Variable: bftorat

Standardwert: `false`


Die Optionsvariable `bftorat` kontrolliert die Umwandlung von großen
Gleitkommazahlen in rationale Zahlen.  Hat `bftorat` den Wert `false`,
wird die Genauigkeit der Umwandlung von der Optionsvariablen
`ratepsilon` kontrolliert.  Hat dagegen `bftorat` den Wert
`true`, wird die große Gleitkommazahl exakt durch die rationale Zahl 
reprasentiert.


Hinweis: `bftorat` hat keinen Einfluss auf die Umwandlung in rationale
Zahlen mit der Funktion `rationalize`.


Beispiel:



```maxima
(%i1) ratepsilon:1e-4;
(%o1)                         1.e-4
(%i2) rat(bfloat(11111/111111)), bftorat:false;
`rat' replaced 9.99990999991B-2 by 1/10 = 1.0B-1
                               1
(%o2)/R/                       --
                               10
(%i3) rat(bfloat(11111/111111)), bftorat:true;
`rat' replaced 9.99990999991B-2 by 11111/111111 = 9.99990999991B-2
                             11111
(%o3)/R/                     ------
                             111111
```

See also: `ratepsilon`, `rationalize`.

<!-- category: Other -->
<!-- keywords: bftrunc -->
<!-- signatures: bftrunc -->
### Variable: bftrunc

Standardwert: `true`


Hat die Optionsvariable `bftrunc` den Wert `true`, werden bei der
Ausgabe einer großen Gleitkommazahl nachfolgende Nullen nicht angezeigt.


Beispiele:



```maxima
(%i1) bftrunc:true;
(%o1)                         true
(%i2) bfloat(1);
(%o2)                         1.0b0
(%i3) bftrunc:false;
(%o3)                         false
(%i4) bfloat(1);
(%o4)                  1.000000000000000b0
```

<!-- category: Other -->
<!-- keywords: concat -->
<!-- signatures: concat(arg_1, arg_2, ...) -->
### Function: concat (arg_1, arg_2, ...)

Verkettet die Argumente *arg_1*, *arg_2*, ... zu einer Zeichenkette 
oder einem Symbol.  Die Argumente mussen sich zu einem Atom auswerten lassen.
Der Ruckgabewert ist ein Symbol, wenn das erste Argument ein Symbol ist.
Ansonsten wird eine Zeichenkette zuruckgegeben.


`concat` wertet die Argumente aus.  Der Quote-Operator `'`
verhindert die Auswertung.  Siehe auch die Funktion `sconcat`.


Beispiele:



```maxima
(%i1) y: 7$
(%i2) z: 88$
(%i3) stringdisp:true$
(%i4) concat(y, z/2);
(%o4)                         "744"
(%i5) concat('y, z/2);
(%o5)                          y44
```


Einem Symbol, das mit `concat` konstruiert wird, kann ein Wert zugewiesen
werden und es kann in Ausdrucken auftreten.



```maxima
(%i6) a: concat ('y, z/2);
(%o6)                          y44

(%i7) a:: 123;
(%o7)                          123

(%i8) y44;
(%o8)                          123
(%i9) b^a;
                               y44
(%o9)                         b
(%i10) %, numer;
                                123
(%o11)                         b
```


`concat(1, 2)` gibt eine Zeichenkette als Ergebnis zuruck.



```maxima
(%i12) concat (1, 2) + 3;
(%o12)                       "12" + 3
```

See also: `sconcat`.

<!-- category: Other -->
<!-- keywords: defstruct -->
<!-- signatures: defstruct(S(a_1, ..., a_n)), defstruct(S(a_1=v_1, ..., a_n=v_n)) -->
### Function: defstruct (S(a_1, ..., a_n))

Definiert eine Struktur, als eine Liste mit den Feldnamen *a_1*, ...,
*a_n* und dem Namen *S* fur die Struktur.  Eine Instanz einer
Struktur ist ein Ausdruck mit dem Operator *S* und *n* Argumenten,
die die Werte der Felder sind.  Mit dem Kommando `new(S` wird eine
neue Instanz einer Struktur *S* generiert.  Siehe auch `new`.







Mit einem Symbol *a* als Argument wird der Name eines Feldes bezeichnet.
Mit einer Gleichung `a = v` wird der Name des Feldes als
*a* bezeichnet und ein Standardwert *v* definiert.  Der Standardwert
*v* kann ein beliebiger Ausdruck sein.





`defstruct` legt die Definition der Struktur *S* in der
Informationsliste `structures` ab.





Mit dem Kommando `kill(S)` wird die Definition einer Struktur
geloscht und von der Informationsliste `structures` entfernt.


Beispiele:



```maxima
(%i1) defstruct (foo (a, b, c));
(%o1)                    [foo(a, b, c)]
(%i2) structures;
(%o2)                    [foo(a, b, c)]
(%i3) new (foo);
(%o3)                     foo(a, b, c)
(%i4) defstruct (bar (v, w, x = 123, y = %pi));
(%o4)             [bar(v, w, x = 123, y = %pi)]
(%i5) structures;
(%o5)      [foo(a, b, c), bar(v, w, x = 123, y = %pi)]
(%i6) new (bar);
(%o6)              bar(v, w, x = 123, y = %pi)
(%i7) kill (foo);
(%o7)                         done
(%i8) structures;
(%o8)             [bar(v, w, x = 123, y = %pi)]
```

See also: `new`, `structures`.

<!-- category: Other -->
<!-- keywords: evenp -->
<!-- signatures: evenp(expr) -->
### Function: evenp (expr)

Ist das Argument *expr* eine gerade ganze Zahl, wird `true`
zuruckgegeben.  In allen anderen Fallen wird `false` zuruckgegeben.


`evenp` gibt fur Symbole oder Ausdrucke immer den Wert `false` 
zuruck, auch wenn das Symbol als gerade ganze Zahl deklariert ist oder der 
Ausdruck eine gerade ganze Zahl reprasentiert.  Siehe die Funktion
`featurep`, um zu testen, ob ein Symbol oder Ausdruck eine gerade
ganze Zahl reprasentiert.


Beispiele:



```maxima
(%i1) evenp(2);
(%o1)                         true
(%i2) evenp(3);
(%o2)                         false
(%i3) declare(n, even);
(%o3)                         done
(%i4) evenp(n);
(%o4)                         false
(%i5) featurep(n, even);
(%o5)                         true
```

See also: `featurep`.

<!-- category: Other -->
<!-- keywords: false -->
<!-- signatures: false -->
### Variable: false

Reprasentiert den logischen Wert `falsch`.  `false` wird intern
von Maxima durch die Lisp-Konstante `NIL` dargestellt.


Siehe auch `true` fur den logischen Wert `wahr`.

See also: `true`.

<!-- category: Other -->
<!-- keywords: float -->
<!-- signatures: float(expr) -->
### Function: float (expr)

Die Funktion `float` konvertiert ganze, rationale und große
Gleitkommazahlen, die im Argument *expr* enthalten sind, in Gleitkommazahlen
mit doppelter Genauigkeit.


`float` ist auch eine Optionsvariable mit dem Standardwert `false` und
ein Auswertungsschalter fur die Funktion `ev`.  Erhalt die
Optionsvariable `float` den Wert `true`, werden rationale und
große Gleitkommazahlen sofort in Gleitkommazahlen umgewandelt.  Als
Auswertungsschalter der Funktion `ev` hat `float` denselben Effekt,
ohne dass die Optionsvariable `float` ihren Wert andert.  Im Unterschied
zur Funktion `float` werden durch das Setzen der Optionsvariablen oder bei
Verwendung als Auswertungsschalter keine ganze Zahlen in Gleitkommazahlen
umgewandelt.  Daher konnen die beiden Kommandos `ev(expr, float)` und
`float(expr)` ein unterschiedliches Ergebnis haben.


Siehe auch die Optionsvariable `numer`.


Beispiele:


In den ersten zwei Beispielen werden die Zahlen `1/2` und `1` in eine
Gleitkommazahl umgewandelt.  Die Sinusfunktion vereinfacht sodann zu einem
numerischen Wert.  Das Auswertungsschalter `float` wandelt ganze Zahlen
nicht in eine Gleitkommazahl um.  Daher wird `sin(1)` nicht zu einem
numerischen Wert vereinfacht.



```maxima
(%i1) float(sin(1/2));
(%o1)                   0.479425538604203
(%i2) float(sin(1));
(%o2)                   .8414709848078965
(%i3) sin(1/2),float;
(%o3)                   0.479425538604203
(%i4) sin(1),float;
(%o4)                        sin(1)
```

See also: `ev`, `numer`.

<!-- category: Other -->
<!-- keywords: float2bf -->
<!-- signatures: float2bf -->
### Variable: float2bf

Standardwert: `true`

 

Hat die Optionsvariable `float2bf` den Wert `false`, wird eine
Warnung ausgegeben, wenn eine Gleitkommazahl in eine große Gleitkommazahl 
umgewandelt wird, da die Umwandlung zu einem Verlust an Genauigkeit fuhren 
kann.


Beispiele:



```maxima
(%i1) float2bf:true;
(%o1)                         true
(%i2) bfloat(1.5);
(%o2)                         1.5b0
(%i3) float2bf:false;
(%o3)                         false
(%i4) bfloat(1.5);
bfloat: converting float 1.5 to bigfloat.
(%o4)                         1.5b0
```

<!-- category: Other -->
<!-- keywords: floatnump -->
<!-- signatures: floatnump(number) -->
### Function: floatnump (number)

Gibt den Wert `true` zuruck, wenn das Argument *number* eine 
Gleitkommazahl ist.  Ansonsten wird `false` zuruckgegeben.  Auch wenn 
*number* eine große Gleitkommazahl ist, ist das Ergebnis `false`.


Siehe auch die Funktionen `numberp`, `bfloatp`,
`ratnump` und `integerp`.


Beispiele:



```maxima
(%i1) floatnump(1.5);
(%o1)                         true
(%i2) floatnump(1.5b0);
(%o2)                         false
```

See also: `numberp`, `bfloatp`, `ratnump`, `integerp`.

<!-- category: Other -->
<!-- keywords: fpprec -->
<!-- signatures: fpprec -->
### Variable: fpprec

Standardwert: 16


`ffprec` ist die Zahl der Stellen fur das Rechnen mit großen 
Gleitkommazahlen.  `ffprec` hat keinen Einfluß auf das Rechnen mit
Gleitkommazahlen in doppelter Genauigkeit.  Siehe auch `bfloat` und 
`fpprintprec`.


Beispiele:



```maxima
(%i1) fpprec:16;
(%o1)                          16
(%i2) bfloat(%pi);
(%o2)                  3.141592653589793b0
(%i3) fpprec:45;
(%o3)                          45
(%i4) bfloat(%pi);
(%o4)    3.1415926535897932384626433832795028841971694b0
(%i5) sin(1.5b0);
(%o5)   9.97494986604054430941723371141487322706651426b-1
```

See also: `bfloat`, `fpprintprec`.

<!-- category: Other -->
<!-- keywords: fpprintprec -->
<!-- signatures: fpprintprec -->
### Variable: fpprintprec

Standardwert: 0


`fpprintprec` ist die Anzahl der Stellen, die angezeigt werden, wenn eine
Gleitkommazahl ausgegeben wird.


Hat `fpprintprec` einen Wert zwischen 2 und 16, ist die Anzahl der 
angezeigten Stellen fur einfache Gleitkommazahlen gleich dem Wert von 
`fpprintprec`.  Hat `fpprintprec` den Wert 0 oder ist großer als
16 werden 16 Stellen angezeigt.


Hat fur große Gleitkommazahlen `fpprintprec` einen Wert zwischen 2 
und `fpprec`, ist die Anzahl der angezeigten Stellen gleich
`fpprintprec`.  Ist der Wert von `fpprintprec` gleich 0 oder 
großer als `fpprec` werden `fpprec` Stellen angezeigt.


`fpprintprec` kann nicht den Wert 1 erhalten.


Beispiele:



```maxima
(%i1) fpprec:16;
(%o1)                          16
(%i2) fpprintprec:5;
(%o2)                           5
(%i3) float(%pi);
(%o3)                        3.1416
(%i4) bfloat(%pi);
(%o4)                       3.1415b0
(%i5) fpprintprec:25;
(%o5)                          25
(%i6) bfloat(%pi);
(%o6)                  3.141592653589793b0
(%i7) bfloat(%pi);
(%o7)                  3.141592653589793b0
(%i8) fpprec:45;
(%o8)                          45
(%i9) bfloat(%pi);
(%o9)             3.141592653589793238462643b0
(%i10) fpprintprec:45;
(%o10)                         45
(%i11) bfloat(%pi);
(%o11)   3.1415926535897932384626433832795028841971694b0
```

See also: `fpprec`.

<!-- category: Other -->
<!-- keywords: ind -->
<!-- signatures: ind -->
### Variable: ind

`ind` reprasentiert ein unbestimmtes Ergebnis.  Siehe auch `und`
und die Funktion `limit`.


Beispiel:



```maxima
(%i1) limit(sin(1/x), x, 0);
(%o1)                          ind
```

See also: `und`, `limit`.

<!-- category: Other -->
<!-- keywords: inf -->
<!-- signatures: inf -->
### Variable: inf

`inf` reprasentiert einen positiven unendlich großen Wert.  Siehe
auch `minf` und `infinity`.


Die unendlichen Großen, aber auch die unbestimmten Großen
`ind` und `und`, eignen sich nicht fur das arithmetische
Rechnen.  Diese Großen werden von Maxima in Rechnungen
wie Symbole behandelt, was zu fehlerhaften Ergebnissen fuhrt.  Daher sollten
unendliche Großen nur im Zusammenhang mit Grenzwerten
`limit`, bestimmten Integralen `integrate` oder Reihen
`sum` verwendet werden.

See also: `minf`, `infinity`, `ind`, `und`, `limit`, `integrate`, `sum`.

<!-- category: Other -->
<!-- keywords: infinity -->
<!-- signatures: infinity -->
### Variable: infinity

`infinity` reprasentiert einen komplexen unendlichen Wert.  Siehe
auch `inf` und `minf`.


Die unendlichen Großen, aber auch die unbestimmten Großen 
`ind` und `und`, eignen sich nicht fur das arithmetische 
Rechnen.  Diese Großen werden von Maxima in Rechnungen
wie Symbole behandelt, was zu fehlerhaften Ergebnissen fuhrt.  Daher sollten
unendliche Großen nur im Zusammenhang mit Grenzwerten
`limit`, bestimmten Integralen `integrate` oder Reihen
`sum` verwendet werden.

See also: `inf`, `minf`, `ind`, `und`, `limit`, `integrate`, `sum`.

<!-- category: Other -->
<!-- keywords: integerp -->
<!-- signatures: integerp(number) -->
### Function: integerp (number)

Hat den Ruckgabewert `true`, wenn das Argument *number* eine ganze 
Zahl ist.  In allen anderen Fallen gibt `integerp` den Wert `false` 
zuruck.


`integerp` gibt fur Symbole oder Ausdrucke immer den Wert `false` 
zuruck, auch wenn das Symbol als ganze Zahl deklariert ist oder der Ausdruck 
eine ganze Zahl reprasentiert.  Siehe die Funktion `featurep`, um zu
testen, ob ein Symbol oder Ausdruck eine ganze Zahl reprasentiert.


Beispiele:



```maxima
(%i1) integerp (1);
(%o1)                         true
(%i2) integerp (1.0);
(%o2)                         false
(%i3) integerp (%pi);
(%o3)                         false
(%i4) declare (n, integer)$
(%i5) integerp (n);
(%o5)                         false
```

See also: `featurep`.

<!-- category: Other -->
<!-- keywords: m1pbranch -->
<!-- signatures: m1pbranch -->
### Variable: m1pbranch

Standardwert: `false`


Die Optionsvariable `m1pbranch` kontrolliert die Vereinfachung der
Exponentiation von `-1` fur den Fall, dass die Optionsvariable
`domain` den Wert `complex` hat.  Hat `m1pbranch` fur diesen
Fall den Wert `true`, wird die Exponentiation von `-1` zu einem
Ausdruck vereinfacht, der dem Hauptwert entspricht.  Die Auswirkung der
Optionsvariable `m1pbranch` ist in der folgenden Tabelle gezeigt.



```maxima
domain:real
                            
(-1)^(1/3):      -1
(-1)^(1/4):   (-1)^(1/4)

             domain:complex
          
m1pbranch:false          m1pbranch:true
(-1)^(1/3)               1/2+%i*sqrt(3)/2
(-1)^(1/4)              sqrt(2)/2+%i*sqrt(2)/2
```


Siehe auch die Optionsvariable `numer_pbranch`.

See also: `domain`, `numer_pbranch`.

<!-- category: Other -->
<!-- keywords: minf -->
<!-- signatures: minf -->
### Variable: minf

`minf` reprasentiert einen negativen unendlichen Wert.  Siehe
auch `inf` und `infinity`.


Die unendlichen Großen, aber auch die unbestimmten Großen 
`ind` und `und`, eignen sich nicht fur das arithmetische 
Rechnen.  Diese Großen werden von Maxima in Rechnungen
wie Symbole behandelt, was zu fehlerhaften Ergebnissen fuhrt.  Daher sollten
unendliche Großen nur im Zusammenhang mit Grenzwerten 
`limit`, bestimmten Integralen `integrate` oder Reihen
`sum` verwendet werden.

See also: `inf`, `infinity`, `ind`, `und`, `limit`, `integrate`, `sum`.

<!-- category: Other -->
<!-- keywords: new -->
<!-- signatures: new(S), new(S(v_1, ..., v_n)) -->
### Function: new (S)

`new` erzeugt eine neue Instanz einer Struktur.






Das Kommando `new(S)` erzeugt eine neue Instanz der Struktur *S*,
die mit der Funktion `defstruct` definiert wurde.  Die Felder werden mit
den Standardwerten belegt, wenn die Definition der Struktur Standardwerte
enthalt.  Ansonsten erhalten die Felder keine Werte.






Das Kommando `new(S(v_1, ..., v_n))` erzeugt eine neue
Instanz der Struktur *S*, wobei die Felder mit den Werten *v_1*,
..., *v_n* initialisiert werden.


Beispiele:



```maxima
(%i1) defstruct (foo (w, x = %e, y = 42, z));
(%o1)              [foo(w, x = %e, y = 42, z)]
(%i2) new (foo);
(%o2)               foo(w, x = %e, y = 42, z)
(%i3) new (foo (1, 2, 4, 8));
(%o3)            foo(w = 1, x = 2, y = 4, z = 8)
```

See also: `defstruct`.

<!-- category: Other -->
<!-- keywords: nonnegintegerp -->
<!-- signatures: nonnegintegerp(number) -->
### Function: nonnegintegerp (number)

Gibt den Wert `true` zuruck, wenn `number` eine ganze positive Zahl
oder Null ist.  Siehe auch `integerp`.


Beispiele:



```maxima
(%i1) nonnegintegerp(2);
(%o1)                         true
(%i2) nonnegintegerp(-2);
(%o2)                         false
```

See also: `integerp`.

<!-- category: Other -->
<!-- keywords: numberp -->
<!-- signatures: numberp(number) -->
### Function: numberp (number)

Hat das Ergebnis `true`, wenn *number* eine ganze, rationale, eine
Gleitkommazahl oder eine große Gleitkommazahl ist.  Ansonsten ist das 
Ergebnis `false`.


`numberp` gibt fur ein Symbol immer das Ergebnis `false` zuruck.
Dies ist auch dann der Fall, wenn das Symbol eine numerische Konstante wie 
`%pi` ist oder wenn das Symbol mit der Funktion `declare` eine 
Eigenschaft wie `integer`, `real` oder `complex` erhalten
hat.


Beispiele:



```maxima
(%i1) numberp (42);
(%o1)                         true
(%i2) numberp (-13/19);
(%o2)                         true
(%i3) numberp (3.14159);
(%o3)                         true
(%i4) numberp (-1729b-4);
(%o4)                         true
(%i5) map (numberp, [%e, %pi, %i, %phi, inf, minf]);
(%o5)      [false, false, false, false, false, false]
(%i6) declare(a,even, b,odd, c,integer, d,rational, e,real);
(%o6)                         done
(%i7) map (numberp, [a, b, c, d, e]);
(%o7) [false, false, false, false, false]
```

See also: `%pi`, `declare`, `integer`, `real`, `complex`.

<!-- category: Other -->
<!-- keywords: numer -->
<!-- signatures: numer -->
### Variable: numer

Standardwert: `false`


Hat die Optionsvariable `numer` den Wert `true`, werden rationale
Zahlen und große Gleitkommazahlen in Gleitkommazahlen umgewandelt.
Weiterhin werden Konstante wie zum Beispiel `%pi`, die einen
numerischen Wert haben, durch diesen ersetzt.  Mathematische Funktionen mit
numerischen Argumenten vereinfachen zu einer Gleitkommazahl.  Wird die
Optionsvariable `numer` gesetzt, erhalt die Optionsvariable
`float` denselben Wert.  Im Unterschied zur Optionsvariablen `float`
vereinfachen auch mathematische Funktionen mit einem ganzzahligen Wert wie zum
Beispiel `sin(1)` zu einem numerischen Wert.


`numer` ist auch ein Auswertungsschalter der Funktion `ev`.  Der
Auswertungsschalter hat die gleiche Funktionsweise wie die Optionsvariable,
ohne dass die Optionsvariable ihren Wert andert.


Siehe auch `float` und `%enumer`.


Beispiele:


Erhalt `numer` den Wert `true`, werden rationale Zahlen, Konstante
mit einem numerischen Wert und mathematische Funktionen mit numerischen
Argumenten zu einer Gleitkommazahl ausgewertet oder vereinfacht.



```maxima
(%i1) numer:false;
(%o1)                         false
(%i2) [1, 1/3, %pi, sin(1)];
                           1
(%o2)                  [1, -, %pi, sin(1)]
                           3
(%i3) numer:true;
(%o3)                         true
(%i4) [1, 1/3, %pi, sin(1)];
(%o4) [1, .3333333333333333, 3.141592653589793, 
                                               .8414709848078965]
```


`numer` ist auch ein Auswertungsschalter der Funktion `ev`.  Hier wird
die Kurzschreibweise der Funktion `ev` verwendet.



```maxima
(%i1) [sqrt(2), sin(1), 1/(1+sqrt(3))];
                                        1
(%o1)            [sqrt(2), sin(1), -----------]
                                   sqrt(3) + 1

(%i2) [sqrt(2), sin(1), 1/(1+sqrt(3))],numer;
(%o2) [1.414213562373095, .8414709848078965, .3660254037844387]
```

See also: `%pi`, `float`, `ev`, `%enumer`.

<!-- category: Other -->
<!-- keywords: numer_pbranch -->
<!-- signatures: numer_pbranch -->
### Variable: numer_pbranch

Standardwert: `false`


Die Optionsvariable `numer_pbranch` kontrolliert die Vereinfachung der
Exponentiation einer negativen ganzen, rationalen oder Gleitkommazahl.
Hat `numer_pbranch` den Wert `true` und ist der Exponent eine 
Gleitkommazahl oder hat die Optionsvariable `numer` den Wert `true`, 
dann berechnet Maxima den Hauptwert der Exponentiation.  Ansonsten wird ein 
vereinfachter Ausdruck, aber nicht numerischer Wert zuruckgegeben.  Siehe auch
die Optionsvariable `m1pbranch`.


Beispiele:



```maxima
(%i1) (-2)^0.75;
(%o1) (-2)^0.75

(%i2) (-2)^0.75,numer_pbranch:true;
(%o2) 1.189207115002721*%i-1.189207115002721

(%i3) (-2)^(3/4);
(%o3) (-1)^(3/4)*2^(3/4)

(%i4) (-2)^(3/4),numer;
(%o4) 1.681792830507429*(-1)^0.75

(%i5) (-2)^(3/4),numer,numer_pbranch:true;
(%o5) 1.189207115002721*%i-1.189207115002721
```

See also: `numer`, `m1pbranch`.

<!-- category: Other -->
<!-- keywords: numerval -->
<!-- signatures: numerval(x_1, val_1, ..., var_n, val_n) -->
### Function: numerval (x_1, val_1, ..., var_n, val_n)

Die Variablen *x_1*, ..., *x_n* erhalten die numerischen Werte
*val_1*, ..., `val_n`.  Die numerischen Werte werden immer dann
fur die Variablen in Ausdrucke eingesetzt, wenn die Optionsvariable 
`numer` den Wert `true` hat.  Siehe auch `ev`.


Die Argumente *val_1*, ..., *val_n* konnen auch beliebige 
Ausdrucke sein, die wie numerische Werte fur Variablen eingesetzt werden.


Beispiele:



```maxima
(%i1) numerval(a, 123, b, x^2)$

(%i2) [a, b];
(%o2)                        [a, b]
(%i3) numer:true;
(%o3)                         true
(%i4) [a, b];
                                   2
(%o4)                       [123, x ]
```

See also: `numer`, `ev`.

<!-- category: Other -->
<!-- keywords: oddp -->
<!-- signatures: oddp(expr) -->
### Function: oddp (expr)

Gibt `true` zuruck, wenn das Argument *expr* eine ungerade ganze Zahl
ist.  In allen anderen Fallen wird `false` zuruckgegeben.


`oddp` gibt fur Symbole oder Ausdrucke immer den Wert `false` 
zuruck, auch wenn das Symbol als ungerade ganze Zahl deklariert ist oder der 
Ausdruck eine ungerade ganze Zahl reprasentiert.  Siehe die Funktion 
`featurep`, um zu testen, ob ein Symbol oder Ausdruck eine ungerade 
ganze Zahl reprasentiert.


Beispiele:



```maxima
(%i1) oddp(3);
(%o1)                         true
(%i2) oddp(2);
(%o2)                         false
(%i3) declare(n,odd);
(%o3)                         done
(%i4) oddp(n);
(%o4)                         false
(%i5) featurep(n,odd);
(%o5)                         true
```

See also: `featurep`.

<!-- category: Other -->
<!-- keywords: ratepsilon -->
<!-- signatures: ratepsilon -->
### Variable: ratepsilon

Standardwert: `2.0e-15`


Die Optionsvariable `ratepsilon` kontrolliert die Genauigkeit, mit der
Gleitkommazahlen in rationale Zahlen umgewandelt werden, wenn die
Optionsvariable `bftorat` den Wert `false` hat.  Fur ein Beispiel
siehe die Optionsvariable `bftorat`.

See also: `bftorat`.

<!-- category: Other -->
<!-- keywords: rationalize -->
<!-- signatures: rationalize(expr) -->
### Function: rationalize (expr)

Konvertiert alle Gleitkommazahlen einschließlich großer 
Gleitkommazahlen, die in dem Ausdruck *expr* auftreten, in rationale Zahlen.


Es mag uberraschend sein, dass `rationalize(0.1)` nicht das Ergebnis
`1/10` hat.  Dies ist nicht speziell fur Maxima.  Ursache ist, dass die 
gebrochene Zahl `1/10` in der internen Darstellung als binare Zahl keine
endliche Darstellung hat.


Siehe auch die Funktionen `float` und `bfloat` sowie die
Auswertungsschalter `float` und `numer`, um eine rationale Zahl
in eine Gleitkommazahl umzuwandeln.


Beispiele:



```maxima
(%i1) rationalize (0.5);
                                1
(%o1)                           -
                                2
(%i2) rationalize (0.1);
                        3602879701896397
(%o2)                   -----------------
                        36028797018963968
(%i3) fpprec : 5$
(%i4) rationalize (0.1b0);
                             209715
(%o4)                        -------
                             2097152
(%i5) fpprec : 20$

(%i6) rationalize (0.1b0);
                     236118324143482260685
(%o6)                ----------------------
                     2361183241434822606848

(%i7) rationalize (sin (0.1*x + 5.6));

               3602879701896397 x   3152519739159347
(%o7)      sin(------------------ + ----------------)
               36028797018963968    562949953421312

(%i8) float(%);
(%o8)                          sin(0.1 x + 5.6)
```

See also: `float`, `bfloat`, `numer`.

<!-- category: Other -->
<!-- keywords: ratnump -->
<!-- signatures: ratnump(number) -->
### Function: ratnump (number)

Gibt `true` zuruck, wenn *number* eine ganze oder rationale Zahl ist.
In allen anderen Fallen ist das Ergebnis `false`.


Siehe auch die Funktionen `numberp`, `integerp`,
`floatnump` und `bfloatp`.


Beispiele:



```maxima
(%i1) ratnump(1/2);
(%o1)                         true
(%i2) ratnump(3);
(%o2)                         true
(%i3) ratnump(3.0);
(%o3)                         false
```

See also: `numberp`, `integerp`, `floatnump`, `bfloatp`.

<!-- category: Other -->
<!-- keywords: sconcat -->
<!-- signatures: sconcat(arg_1, arg_2, ...) -->
### Function: sconcat (arg_1, arg_2, ...)

Verkettet die Argumente *arg_1*, *arg_2*, ... zu einer Zeichenkette.
Im Unterschied zu der Funktion `concat` mussen die Argumente *nicht* 
Atome sein.  Der Ruckgabewert ist eine Zeichenkette.


Beispiel:



```maxima
(%i1) sconcat ("xx[", 3, "]:", expand ((x+y)^3));
(%o1)               xx[3]:y^3+3*x*y^2+3*x^2*y+x^3
```

See also: `concat`.

<!-- category: Other -->
<!-- keywords: string -->
<!-- signatures: string(expr) -->
### Function: string (expr)

Konvertiert das Argument `expr` in eine lineare Darstellung, wie sie auch
vom Parser von der Eingabe eingelesen wird.  Die Ruckgabe von `string`
ist eine Zeichenkette.  Diese kann nicht als Eingabe fur eine Berechnung
genutzt werden.


Beispiele:


Die hier verwendete Funktion `stringp` ist im Paket `stringproc`
definiert und wird automatisch geladen.



```maxima
(%i1) stringdisp:true;
(%o1)                         true
(%i2) string(expand((a+b)^2));
(%o2)                    "b^2+2*a*b+a^2"
(%i3) stringp(%);
(%o3)                         true
```

See also: `stringp`, `stringproc`.

<!-- category: Other -->
<!-- keywords: stringdisp -->
<!-- signatures: stringdisp -->
### Variable: stringdisp

Standardwert: `false`


Hat `stringdisp` den Wert `true`, werden Zeichenketten mit
Anfuhrungszeichen ausgegeben.  Ansonsten werden keine Anfuhrungszeichen
ausgegeben.


Wird die Definition einer Funktion ausgegeben, werden enthaltene Zeichenketten
unabhangig vom Wert der Optionsvariablen `stringdisp` immer mit
Anfuhrungszeichen ausgegeben.


Beispiele:



```maxima
(%i1) stringdisp: false$
(%i2) "This is an example string.";
(%o2)              This is an example string.
(%i3) foo () :=
      print ("This is a string in a function definition.");
(%o3) foo() := 
              print("This is a string in a function definition.")
(%i4) stringdisp: true$
(%i5) "This is an example string.";
(%o5)             "This is an example string."
```

<!-- category: Other -->
<!-- keywords: structures -->
<!-- signatures: structures -->
### Variable: structures

`structures` ist eine Informationsliste, die die vom Benutzer mit der
Funktion `defstruct` definierten Strukturen enthalt.

See also: `defstruct`.

<!-- category: Other -->
<!-- keywords: true -->
<!-- signatures: true -->
### Variable: true

`true` reprasentiert den logischen Wert `wahr`.  Intern ist 
`true` als die Lisp-Konstante `T` implementiert.


Siehe auch `false` fur den logischen Wert `falsch`.

See also: `false`.

<!-- category: Other -->
<!-- keywords: und -->
<!-- signatures: und -->
### Variable: und

`und` reprasentiert ein nicht definiertes Ergebnis.  Siehe auch 
`ind` und die Funktion `limit`.


Beispiel:



```maxima
(%i1) limit (x*sin(x), x, inf);
(%o1)                          und
```

See also: `ind`, `limit`.

<!-- category: Other -->
<!-- keywords: zeroa -->
<!-- signatures: zeroa -->
### Variable: zeroa

`zeroa` reprasentiert eine positive unendlich kleine Zahl.  `zeroa`
kann in Ausdrucken benutzt werden.  Die Funktion `limit` vereinfacht
Ausdrucke, die infinitesimale Großen enthalten.


Siehe auch `zerob` und `limit`.


Beispiele:


`limit` vereinfacht Ausdrucke, die infinitesimale Großen enthalten.



```maxima
(%i1) limit(zeroa);
(%o1)                           0
(%i2) limit(x+zeroa);
(%o2)                           x
```

See also: `zerob`, `limit`.

<!-- category: Other -->
<!-- keywords: zerob -->
<!-- signatures: zerob -->
### Variable: zerob

`zerob` reprasentiert eine negative unendlich kleine Zahl.  `zerob`
kann in Ausdrucken benutzt werden.  Die Funktion `limit` vereinfacht
Ausdrucke, die infinitesimale Großen enthalten.


Siehe auch `zeroa` und `limit`.

See also: `zeroa`, `limit`.

