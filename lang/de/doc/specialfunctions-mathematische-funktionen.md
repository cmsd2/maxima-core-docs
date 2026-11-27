## Mathematische Funktionen

<!-- category: SpecialFunctions -->
<!-- keywords: !! -->
<!-- signatures: !! -->
### Function: !!

Ist der Operator der doppelten Fakultat.


Fur eine positive ganze Zahl `n`, wird `n!!` zu dem Produkt
`n (n-2) (n-4) (n-6) ... (n - 2 (k-1))` vereinfacht, wobei `k` gleich
`floor(n/2)` ist und `floor` die großte ganze Zahl als Ergebnis
hat, die kleiner oder gleich `n/2` ist.


Fur ein Argument `n`, das keine ganze positive Zahl ist, gibt `n!!`
die Substantivform `genfact(n, n/2,2)` zuruck.  Siehe die Funktion
`genfact`.


Die Verallgemeinerung der doppelten Fakultat fur reelle und komplexe Zahlen
ist als die Funktion `double_factorial` implementiert.


Beispiele:



```maxima
(%i1) [0!!, 1!!, 2!!, 3!!, 4!!, 5!!, 6!!, 7!!, 8!!];
(%o1)           [1, 1, 2, 3, 8, 15, 48, 105, 384]
(%i2) 1.5!!;
(%o2)                  genfact(1.5, 0, 2)
(%i3) x!!;
                                   x
(%o3)                   genfact(x, -, 2)
                                   2
```

See also: `floor`, `genfact`, `double_factorial`.

<!-- category: SpecialFunctions -->
<!-- keywords: %e_to_numlog -->
<!-- signatures: %e_to_numlog -->
### Variable: %e_to_numlog

Standardwert: `false`


Hat die Optionsvariable `%e_to_numlog` den Wert `true`, wird ein 
Ausdruck mit der Exponentialfunktion `exp` der Form `%e^(r*log(x))`
zu `x^r` vereinfacht, wenn `r` eine rationale Zahl ist.  Ist `r`
eine ganze Zahl, wird die Vereinfachung von der Optionsvariablen
`logsimp` kontrolliert.


Beispiel:



```maxima
(%i1) exp(1/2*log(x));
                              log(x)
                              ------
                                2
(%o1)                       %e
(%i2) exp(1/2*log(x)), %e_to_numlog:true;
(%o2)                        sqrt(x)
```

See also: `exp`, `logsimp`.

<!-- category: SpecialFunctions -->
<!-- keywords: %emode -->
<!-- signatures: %emode -->
### Variable: %emode

Standardwert: `true`


Die Optionsvariable `%emode` kontrolliert die Vereinfachung von
Ausdrucken mit der Exponentialfunktion `exp` der Form
`%e^(%pi %i x)`.


Ist das Argument *x* eine ganze Zahl oder eine rationale Zahl, die ein
Vielfaches von 1/2, 1/3, 1/4 oder 1/6 ist, dann wird der Ausdruck
`%e^(%pi %i x)` zu einer reellen oder komplexen Zahl vereinfacht.  Fur
Gleitkommazahlen wird diese Vereinfachung dann ausgefuhrt, wenn diese eine
ganze Zahl oder halbzahlige rationale Zahl reprasentieren.


Eine Summe im Exponenten wie zum Beispiel `%e^(%pi *%i (x+n))`, wobei 
*n* eine der oben genannten Zahlen und *x* ein allgemeiner Ausdruck ist,
wird vereinfacht, indem der Faktor `%^(%pi %i n)` entsprechend vereinfacht
wird.


Hat `%emode` den Wert `false`, werden keine speziellen Vereinfachungen
fur den Ausdruck `%e^(%pi %i x)` vorgenommen.


Beispiele:



```maxima
(%i1) exp([2*%pi*%i, 1/2*%pi*%i, 0.5*%pi*%i, 0.5b0*%pi*%i]);
(%o1)               [1, %i, 1.0 %i, 1.0b0 %i]

(%i2) exp([1/3*%pi*%i, 1/4*%pi*%i, 1/6*%pi*%i]);
         sqrt(3) %i   1    %i         1     %i   sqrt(3)
(%o2)   [---------- + -, ------- + -------, -- + -------]
             2        2  sqrt(2)   sqrt(2)  2       2

(%i3) exp((1/3+x)*%pi*%i);
                    sqrt(3) %i   1    %i %pi x
(%o3)              (---------- + -) %e
                        2        2
```

See also: `exp`.

<!-- category: SpecialFunctions -->
<!-- keywords: %enumer -->
<!-- signatures: %enumer -->
### Variable: %enumer

Standardwert: `false`


Hat `%enumer` den Wert `true`, wird die Konstante `%e` immer dann
durch ihren nummerischen Wert ersetzt, wenn die Optionsvariable `numer` den
Wert `true` hat.


Hat `%enumer` den Wert `false`, wird die Konstante `%e` nur dann
durch ihren nummerischen Wert ersetzt, wenn der Exponent von `%e^x` zu 
einer Gleitkommazahl ausgewertet wird.


Siehe auch `ev` und `numer`.


Beispiel:



```maxima
(%i1) %enumer:true;
(%o1)                         true
(%i2) exp(x);
                                 x
(%o2)                          %e
(%i3) exp(x),numer;
                                        x
(%o3)                  2.718281828459045
```

See also: `numer`, `ev`.

<!-- category: SpecialFunctions -->
<!-- keywords: %iargs -->
<!-- signatures: %iargs -->
### Variable: %iargs

Standardwert: `true`


Hat `%iargs` den Wert `true`, werden Winkelfunktionen zu 
Hyperbelfunktionen vereinfacht, wenn das Argument ein Vielfaches der 
imaginaren Einheit
`%i`
ist.


Die Vereinfachung zu Hyperbelfunktionen wird auch dann ausgefuhrt, wenn das
Argument offensichtlich reell ist.


Beispiele:



```maxima
(%i1) %iargs : false$

(%i2) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o2)           [sin(%i x), cos(%i x), tan(%i x)]

(%i3) %iargs : true$

(%i4) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o4)           [%i sinh(x), cosh(x), %i tanh(x)]
```


Auch wenn das Argument offensichtlich reell ist, wird zu einer Hyperbelfunktion
vereinfacht.



```maxima
(%i1) declare (x, imaginary)$

(%i2) [featurep (x, imaginary), featurep (x, real)];
(%o2)                     [true, false]


(%i3) sin (%i * x);
(%o3)                      %i sinh(x)
```

<!-- category: SpecialFunctions -->
<!-- keywords: %piargs -->
<!-- signatures: %piargs -->
### Variable: %piargs

Standardwert: `true`


Hat `%piargs` den Wert `true`, werden Winkel- und Hyperbelfunktionen 
sowie deren Inverse zu algebraischen Konstanten vereinfacht, wenn das Argument
ein ganzzahliges Vielfaches der folgenden Konstanten ist:
`%pi`, `%pi/2`, `%pi/3`, `%pi/4` oder `%pi/6`.


Maxima kennt weiterhin einige Identitaten, wenn die Konstante
`%pi`
mit einer Variablen multipliziert wird, die als ganzzahlig deklariert wurde.


Beispiele:



```maxima
(%i1) %piargs : false$

(%i2) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                %pi       %pi
(%o2)            [sin(%pi), sin(---), sin(---)]
                                 2         3


(%i3) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                      %pi       %pi       %pi
(%o3)            [sin(---), sin(---), sin(---)]
                       4         5         6

(%i4) %piargs : true$

(%i5) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                sqrt(3)
(%o5)                    [0, 1, -------]
                                   2


(%i6) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                         1         %pi   1
(%o6)                [-------, sin(---), -]
                      sqrt(2)       5    2


(%i7) [cos (%pi/3), cos (10*%pi/3), tan (10*%pi/3),
       cos (sqrt(2)*%pi/3)];
                1    1               sqrt(2) %pi
(%o7)          [-, - -, sqrt(3), cos(-----------)]
                2    2                    3
```


Weitere Identitaten werden angewendet, wenn
`%pi` und `%pi/2`
mit einer ganzzahligen Variable multipliziert werden.



```maxima
(%i1) declare (n, integer, m, even)$

(%i2) [sin (%pi * n), cos (%pi * m), sin (%pi/2 * m),
       cos (%pi/2 * m)];
                                      m/2
(%o2)                  [0, 1, 0, (- 1)   ]
```

<!-- category: SpecialFunctions -->
<!-- keywords: abs -->
<!-- signatures: abs(z) -->
### Function: abs (z)

Die Funktion `abs` ist die Betragsfunktion und fur das numerische und
symbolische Rechnen geeignet.  Ist das Argument *z* eine reelle oder
komplexe Zahl wird der Betrag berechnet.  Wenn moglich werden allgemeine
Ausdrucke mit der Betragsfunktion vereinfacht.  Maxima kann Ausdrucke mit
der Betragsfunktion integrieren und ableiten sowie Grenzwerte von Ausdrucken
mit der Betragsfunktion ermitteln.  Das Paket `abs_integrate` erweitert
Maximas Moglichkeiten, Integrale mit der Betragsfunktion zu losen.


Die Betragsfunktion wird automatisch auf die Elemente von Listen und Matrizen
sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Siehe die Funktion `cabs`, um den Betrag eines komplexen Ausdrucks
oder einer Funktion zu berechnen.


Beispiele:


Berechnung des Betrages fur reelle und komplexen Zahlen sowie numerische
Konstanten und unendliche Großen.  Das erste Beispiel zeigt, wie die
Betragsfunktion von Maxima auf die Elemente einer Liste angewendet wird.



```maxima
(%i1) abs([-4, 0, 1, 1+%i]);
(%o1)                  [4, 0, 1, sqrt(2)]

(%i2) abs((1+%i)*(1-%i));
(%o2)                           2
(%i3) abs(%e+%i);
                                2
(%o3)                    sqrt(%e  + 1)
(%i4) abs([inf, infinity, minf]);
(%o4)                   [inf, inf, inf]
```


Vereinfachung von Ausdrucken mit der Betragsfunktion.



```maxima
(%i5) abs(x^2);
                                2
(%o5)                          x
(%i6) abs(x^3);
                             2
(%o6)                       x  abs(x)

(%i7) abs(abs(x));
(%o7)                       abs(x)
(%i8) abs(conjugate(x));
(%o8)                       abs(x)
```


Ableitung und Integrale mit der Betragsfunktion.  Wird das Paket
abs_integrate geladen, konnen weitere Integrale mit der Betragsfunktion
gelost werden.  Das letzte Beispiel zeigt die Laplacetransformation der
Betragsfunktion.  Siehe `laplace`.



```maxima
(%i9) diff(x*abs(x),x),expand;
(%o9)                       2 abs(x)

(%i10) integrate(abs(x),x);
                             x abs(x)
(%o10)                       --------
                                2

(%i11) integrate(x*abs(x),x);
                           /
                           [
(%o11)                     I x abs(x) dx
                           ]
                           /

(%i12) load("abs_integrate")$
(%i13) integrate(x*abs(x),x);
                      2           3
                     x  abs(x)   x  signum(x)
(%o13)               --------- - ------------
                         2            6

(%i14) integrate(abs(x),x,-2,%pi);
                               2
                            %pi
(%o14)                      ---- + 2
                             2

(%i15) laplace(abs(x),x,s);
                               1
(%o15)                         --
                                2
                               s
```

See also: `abs_integrate`, `distribute_over`, `cabs`, `laplace`.

<!-- category: SpecialFunctions -->
<!-- keywords: asin, acos, atan, acot, acsc, asec -->
<!-- signatures: asin(z), acos(z), atan(z), acot(z), acsc(z), asec(z) -->
### Function: asin (z)

Die inversen Winkelfunktionen: Arkussinus, Arkuskosinus, Arkustangens,
Arkuskotangens, Arkuskosekans und Arkussekans.


Die inversen Winkelfunktionen sind fur das numerische und symbolische Rechnen
geeignet.  Die inversen Winkelfunktionen konnen fur reelle und komplexe
Gleitkommazahlen in doppelter und in beliebiger Genauigkeit berechnet werden.
Ist das Argument eine ganze oder rationale Zahl, werden die inversen
Winkelfunktionen nicht numerisch berechnet, sondern vereinfacht.  Die numerische
Berechnung kann mit den Optionsvariablen und Auswertungsschaltern
`numer` und `float` erzwungen werden.


Die inversen Winkelfunktionen sind bis auf die Funktionen `acos` und
`asec` als ungerade definiert.  Die Funktionen `acos` und `asec`
vereinfachen fur ein negatives Argument `-x` zu `%pi-acos(x)` und
`%pi-asec(x)`.  Fur die inversen Winkelfunktion `asin`, `acos`
und `atan` ist die Spiegelsymmetrie fur den Fall implementiert, dass das
komplexe Argument `x+%i*y` einen Realteil `abs(x)<1` hat.


Ist das Argument *z* eine Matrix, eine Liste oder eine Gleichung werden die
inversen Winkelfunktionen auf die Elemente der Matrix, der Liste oder auf die
beiden Seiten der Gleichung angewendet.  Dieses Verhalten wird von der
Optionsvariablen `distribute_over` kontrolliert.


Inverse Winkelfunktionen konnen fur das symbolische Rechnen verwendet
werden.  Maxima kann Ausdrucke mit inversen Winkelfunktionen differenzieren
und integrieren, Grenzwerte bestimmen sowie Gleichungen mit inversen
Winkelfunktionen losen.

 

Das Argument der inversen Winkelfunktionen kann eine Taylorreihe sein.  In
diesem Fall wird die Taylorreihenentwicklung fur die inverse Winkelfunktion
vollstandig ausgefuhrt.


Die folgenden Optionsvariablen kontrollieren die Vereinfachung der
inversen Winkelfunktionen:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und ist das
Argument der inversen Winkelfunktion eine Matrix, Liste oder Gleichung wird die
Funktion auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der
Standardwert ist `true`.
**%piargs** — Hat die Optionsvariable `%piargs` den Wert `true`, werden die
inversen Winkelfunktionen fur spezielle Werte als Argument vereinfacht.
Der Standardwert ist `true`.
**%iargs** — Hat die Optionsvariable `%iargs` den Wert `true` und ist das Argument
der inversen Winkelfunktion ein Vielfaches der imaginaren Einheit `%i`
werden die inversen Winkelfunktionen zu inversen Hyperbelfunktionen vereinfacht.
Der Standardwert ist `true`.
**triginverses** — Hat die Optionsvariable `triginverses` den Wert `all` und ist das
Argument die entsprechende Winkelfunktion vereinfachen die inversen
Winkelfunktionen, zum Beispiel vereinfacht `asin(sin(x))` zu `x`.
Der Standardwert ist `true` und die Vereinfachung wird nicht vorgenommen.
**logarc** — Hat die Optionsvariable `logarc` den Wert `true`, werden inverse
Winkelfunktionen durch Logarithmusfunktionen ersetzt.  Der Standardwert von
`logarc` ist `false`.

See also: `numer`, `float`, `distribute_over`, `%piargs`, `%iargs`, `triginverses`, `logarc`.

<!-- category: SpecialFunctions -->
<!-- keywords: asinh, acosh, atanh, acoth, acsch, asech -->
<!-- signatures: asinh(x), acosh(x), atanh(x), acoth(x), acsch(x), asech(x) -->
### Function: asinh (x)

Die inversen Hyperbelfunktionen: Areasinus Hyperbolicus, Areakosinus
Hyperbolicus, Areatangens Hyperbolicus, Areakotangens Hyperbolicus, Areakosekans
Hyperbolicus, Areasekans Hyperbolicus.

<!-- category: SpecialFunctions -->
<!-- keywords: atan2 -->
<!-- signatures: atan2(y, x) -->
### Function: atan2 (y, x)

Ist der Arkustangens mit zwei Argumenten, der in Maxima wie folgt definiert ist:



     atan(y/x)           x>0
     atan(y/x) + %pi     x<0 und y>=0
     atan(y/x) - %pi     x<0 und y<0
       %pi / 2           x=0 und y>0
     - %pi / 2           x=0 und y<0
     nicht definiert     x=0 und y=0


Mit der obigen Definition ist der Wertebereich des Arkustangens
`-%pi < atan2(y,x) <= %pi`.  Alternativ kann der Arkustangens mit zwei
Argumenten definiert werden als



                              %i y + x
     atan2(y, x) = - %i log(-------------)
                                  2    2
                            sqrt(y  + x )


Der Arkustangens ist fur das symbolische und numerische Rechnen geeignet.
Fur reelle Argumente *x* und *y* deren Vorzeichen bestimmt werden
kann, vereinfacht Maxima den Arkustangens wie oben in der Definition angegeben.
Sind beide Argumente Gleitkommazahlen wird ein numerisches Ergebnis berechnet.
Die numerische Berechnung fur komplexe Gleitkommazahlen ist nicht
implementiert.  Weiterhin kennt Maxima die speziellen Werte, wenn eines der
Argumente *x* oder *y* unendlich ist.  `atan2(x, x)` und
`atan2(x, -x)` werden von Maxima vereinfacht, wenn Maxima das Vorzeichen
von *x* ermitteln kann.


Die Vereinfachung des Arkustangens wird weiterhin von den folgenden
Optionsvariablen kontrolliert:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und ist das
Argument des Arkustangens eine Matrix, Liste oder Gleichung wird die Funktion
auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der Standardwert
ist `true`.
**trigsign** — Hat die Optionsvariable `trigsign` den Wert `true`, vereinfacht
Maxima `atan2(-y, x)` zu `- atan2(y, x)`.  Der Standardwert ist
`true`.
**logarc** — Hat die Optionsvariable `logarc` den Wert `true`, wird der
Arkustangens durch einen Ausdruck mit der Logarithmusfunktionen ersetzt.
Der Standardwert von `logarc` ist `false`.


Maxima kann Ausdrucke mit dem Arkustangens ableiten und integrieren sowie die
Grenzwerte von Ausdrucken mit dem Arkustangens ermitteln.


Beispiele:



```maxima
(%i1) atan2([-1, 1],[-1, 0, 1]);
              3 %pi    %pi    %pi    3 %pi  %pi  %pi
(%o1)     [[- -----, - ---, - ---], [-----, ---, ---]]
                4       2      4       4     2    4
(%i2) atan2(1,[-0.5, 0.5]);
(%o2)         [2.034443935795703, 1.10714871779409]
(%i3) assume(a>0)$

(%i4) atan2(2*a, -2*a);
                              3 %pi
(%o4)                         -----
                                4
(%i5) diff(atan2(y,x), x);

                                 y
(%o5)                       - -------
                               2    2
                              y  + x

(%i6) integrate(atan2(y,x), x);
                          2    2
                   y log(y  + x )          y
(%o6)              -------------- + x atan(-)
                         2                 x
```

See also: `distribute_over`, `trigsign`, `logarc`.

<!-- category: SpecialFunctions -->
<!-- keywords: binomial -->
<!-- signatures: binomial(x, y) -->
### Function: binomial (x, y)

Ist der Binominialkoeffizient, der definiert ist als


```maxima
x!
             binomial(x, y) = -----------
                              (x - y)! y!
```


$$
{{x}\choose{y}}={{x!}\over{\left(x-y\right)!\,y!}}
$$


Die Funktion `binomial` ist fur das numerische und symbolische Rechnen
geeignet.


Sind die Argumente *x* oder *y* ganze Zahlen, wird der
Binominialkoeffizient zu einer ganzen Zahl vereinfacht.  Sind die Argumente
*x* und *y* reelle oder komplexe Gleitkommazahlen, wird der
Binominialkoeffizient mit der entsprechenden verallgemeinerten Fakultat
berechnet.  Siehe auch `factorial` und `gamma`.


Ist das Argument *y* oder die Differenz *x-y* eine ganz Zahl, wird
der Binominialkoeffizient zu einem Polynom vereinfacht.


Mit den Funktionen `makefact` oder `makegamma` werden
Binominialkoeffizienten in einem Ausdruck durch aquivalente Ausdrucke mit
der Fakultat oder der Gammafunktion ersetzt.


Maxima kennt die Ableitung des Binominialkoeffizienten nach den Argumenten
*x* und *y*.


Beispiele:



```maxima
(%i1) binomial(11, 7);
(%o1)                          330
(%i2) binomial(%i, 1.5);
(%o2)       .3693753994635863 %i - .7573400496142132
(%i3) binomial(x, 3);
                        (x - 2) (x - 1) x
(%o3)                   -----------------
                                6
(%i4) binomial(x+3, 3);
                     (x + 1) (x + 2) (x + 3)
(%o4)                -----------------------
                                6
(%i5) makefact(binomial(x,y));
                               x!
(%o5)                      -----------
                           (x - y)! y!

(%i6) diff(binomial(x,y), y);
(%o6)  - binomial(x, y) (psi (y + 1) - psi (- y + x + 1))
                            0             0
```

See also: `factorial`, `gamma`, `makefact`, `makegamma`.

<!-- category: SpecialFunctions -->
<!-- keywords: cabs -->
<!-- signatures: cabs(expr) -->
### Function: cabs (expr)

Berechnet den Betrag eines komplexen Ausdrucks *expr*.  Im Unterschied
zu der Funktion `abs`, zerlegt die Funktion `cabs` einen komplexen
Ausdruck immer in einen Realteil und Imaginarteil, um den komplexen Betrag zu
berechnen.  Sind *x* und *y* zwei reelle Variablen oder Ausdrucke,
berechnet die Funktion `cabs` den Betrag des komplexen Ausdrucks
`x + %i*y` als:


```maxima
2    2
                     sqrt(y  + x )
```


Die Funktion `cabs` nutzt Symmetrieeigenschaften und implementierte
Eigenschaften komplexer Funktionen, um den Betrag eines Ausdrucks zu berechnen.
Sind solche Eigenschaften fur eine Funktion vorhanden, konnen diese mit der
Funktion `properties` angezeigt werden.  Eigenschaften, die das Ergebnis
der Funktion `cabs` bestimmen, sind: `mirror symmetry`,
`conjugate function` und `complex characteristic`.


`cabs` ist eine Verbfunktion, die nicht fur das symbolische Rechnen
geeignet ist.  Fur das symbolische Rechnen wie der Integration oder der
Ableitung von Ausdrucken mit der Betragsfunktion muss die Funktion `abs`
verwendet werden.


Das Ergebnis der Funktion `cabs` kann die Betragsfunktion `abs` und
den Arkustangens `atan2` enthalten.


`cabs` wird automatisch auf die Elemente von Listen und Matrizen sowie auf
die beiden Seiten von Gleichungen angewendet.


Siehe auch die Funktionen `rectform`, `realpart`,
`imagpart`, `carg`, `conjugate`, und 
`polarform` fur das Rechnen mit komplexen Zahlen.


Beispiele:


Zwei Beispiele mit der Wurzelfunktion `sqrt` und der Sinusfunktion
`sin`.



```maxima
(%i1) cabs(sqrt(1+%i*x));
                             2     1/4
(%o1)                      (x  + 1)
(%i2) cabs(sin(x+%i*y));
                    2        2         2        2
(%o2)       sqrt(cos (x) sinh (y) + sin (x) cosh (y))
```


Die Funktion `erf` hat Spiegelsymmetrie, die hier fur die Berechnung des
komplexen Betrages angewendet wird.



```maxima
(%i3) cabs(erf(x+%i*y));

                                          2
           (erf(%i y + x) - erf(%i y - x))
(%o3) sqrt(--------------------------------
                          4
                                                               2
                                (erf(%i y + x) + erf(%i y - x))
                              - --------------------------------)
                                               4
```


Maxima kennt komplexe Eigenschaften der Besselfunktionen, um den komplexen
Betrag zu vereinfachen.  Dies ist ein Beispiel fur die Besselfunktion
`bessel_j`.



```maxima
(%i4) cabs(bessel_j(1,%i));
(%o4)                 abs(bessel_j(1, %i))
```

See also: `abs`, `properties`, `atan2`, `rectform`, `realpart`, `imagpart`, `carg`, `conjugate`, `polarform`, `sqrt`, `sin`, `erf`, `bessel_j`.

<!-- category: SpecialFunctions -->
<!-- keywords: carg -->
<!-- signatures: carg(expr) -->
### Function: carg (expr)

Gibt das komplexe Argument des Ausdrucks *expr* zuruck.  Das komplexe
Argument ist ein Winkel `theta` im Intervall `(-%pi, %pi)` derart,
dass *expr* = `r exp (theta %i)` gilt, wobei `r` den Betrag des
komplexen Ausdrucks *expr* bezeichnet.  Das ist die Polarform des Ausdrucks,
wie sie auch von der Funktion `polarform` zuruckgegeben wird.  Der Betrag
des komplexen Ausdrucks kann mit der Funktion `cabs` berechnet werden.


Das Ergebnis der Funktion `carg` kann die Funktion `atan2` enthalten.


`carg` wird automatisch auf die Elemente von Listen und Matrizen sowie auf
die beiden Seiten von Gleichungen angewendet.  Siehe `distribute_over`.


Die Funktion `carg` ist eine Verbfunktion, mit der nicht symbolisch
gerechnet werden kann.


Siehe auch die Funktionen `rectform`, `realpart` und
`imagpart` sowie die Funktionen `cabs` und `conjugate`.


Beispiele:



```maxima
(%i1) carg (1);
(%o1)                           0
(%i2) carg (1 + %i);

                               %pi
(%o2)                          ---
                                4

(%i3) carg (exp (%i));
(%o3)                           1

(%i4) carg (exp (3/2 * %pi * %i));
                                %pi
(%o4)                         - ---
                                 2
(%i5) carg(exp(x+%i*y));
(%o5)                atan2(sin(y), cos(y))

(%i6) carg(sqrt(x+%i*y));
                          atan2(y, x)
(%o6)                     -----------
                               2
(%i7) carg(sqrt(1+%i*y));
                            atan(y)
(%o7)                       -------
                               2
```

See also: `polarform`, `cabs`, `atan2`, `distribute_over`, `rectform`, `realpart`, `imagpart`, `conjugate`.

<!-- category: SpecialFunctions -->
<!-- keywords: ceiling -->
<!-- signatures: ceiling(x) -->
### Function: ceiling (x)

Die Funktion `ceiling` ist fur das numerische und symbolische Rechnen
geeignet.


Ist das Argument *x* eine reelle Zahl, gibt `ceiling` die kleinste
ganze Zahl zuruck, die großer oder gleich *x* ist.


Die Funktion `ceiling` gibt auch dann einen numerischen Wert zuruck, wenn
das Argument ein konstanter Ausdruck ist, wie zum Beispiel `1+%e`, der zu
einer reellen Zahl ausgewertet werden kann.  In diesem Fall wird der konstante
Ausdruck in eine große Gleitkommazahl umgewandelt, auf die die Funktion
`ceiling` angewendet wird.  Aufgrund von Rundungsfehlern bei der Umwandlung
in Gleitkommazahlen kann es zu Fehlern bei der Berechnung von `ceiling`
kommen.  Um diese zu minimieren, wird die Anzahl der Stellen
`fpprec` fur die Berechnung von `ceiling` um drei Stellen erhoht.


Ist das Argument *expr* der Funktion ein komplexer Ausdruck, wird eine
Substantivform zuruckgegeben.


Wenn moglich werden Ausdrucke mit der Funktion `ceiling` von Maxima
vereinfacht.  Maxima kennt insbesondere Vereinfachungen fur den Fall, dass
das Argument der Funktion `ceiling` ein Ausdruck mit den Funktionen
`floor` oder `round` ist.  Weiterhin werden fur die Vereinfachung
die Aussagen und Fakten der aktiven Kontexte herangezogen.  Siehe 
`Funktionen-und-Variablen-für-Fakten`.


`ceiling` wird automatisch auf die Elemente von Listen und Matrizen
sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Siehe auch die Funktionen `floor` und `round`.


Beispiele:



```maxima
(%i1) ceiling(ceiling(x));
(%o1)                      ceiling(x)
(%i2) ceiling(floor(x));
(%o2)                       floor(x)
(%i3) declare (n, integer)$
(%i4) ceiling([n, abs(n), max (n, 6)]);
(%o4)               [n, abs(n), max(6, n)]
(%i5) assume (x > 0, x < 1)$
(%i6) ceiling (x);
(%o6)                           1
```


Sind die Werte einer Funktion eine Teilmenge der ganzen Zahlen, kann diese als
`integervalued` deklariert werden.  Die Funktionen `ceiling` und
`floor` konnen diese Information nutzen, um Ausdrucke zu vereinfachen.



```maxima
(%i1) declare (f, integervalued)$
(%i2) floor (f(x));
(%o2)                         f(x)
(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```


Maxima kennt das Integral der Funktion `ceiling`.



```maxima
(%i1) integrate(ceiling(x),x);
               (- ceiling(x) + 2 x + 1) ceiling(x)
(%o1)          -----------------------------------
                                2
```

See also: `fpprec`, `floor`, `round`, `Funktionen-und-Variablen-für-Fakten`, `distribute_over`, `integervalued`.

<!-- category: SpecialFunctions -->
<!-- keywords: conjugate -->
<!-- signatures: conjugate(expr) -->
### Function: conjugate (expr)

Gibt den konjugiert komplexen Wert des Ausdrucks *expr* zuruck.  Sind
*x* und *y* reelle Variablen oder Ausdrucke, dann hat der Ausdruck
`x + %i*y` das Ergebnis `x - %i*y`.  Die Funktion `conjugate` ist
fur numerische und symbolische Rechnungen geeignet.


Maxima kennt Regeln, um den konjugierten Wert fur Summen, Produkte und
Quotienten von komplexen Ausdrucken zu vereinfachen.  Weiterhin kennt Maxima
Symmetrieeigenschaften und komplexe Eigenschaften von Funktionen, um den 
konjugierten Wert mit diesen Funktionen zu vereinfachen.  Sind solche
Eigenschaften fur eine Funktion vorhanden, konnen diese mit der
Funktion `properties` angezeigt werden.  Eigenschaften, die das Ergebnis
der Funktion `conjugate` bestimmen, sind: `mirror symmetry`,
`conjugate function` und `complex characteristic`.


`conjugate` wird automatisch auf die Elemente von Listen und Matrizen sowie
auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Fur das Rechnen mit komplexen Ausdrucken siehe auch die Funktionen
`cabs` und `carg` sowie `rectform` und `polarform`.


Beispiele:


Beispiele mit reellen, imaginaren und komplexen Variablen.



```maxima
(%i1) declare ([x, y], real, [z1, z2], complex, j, imaginary);
(%o1)                         done
(%i2) conjugate(x + %i*y);
(%o2)                       x - %i y
(%i3) conjugate(z1*z2);
(%o3)              conjugate(z1) conjugate(z2)
(%i4) conjugate(j/z2);
                                 j
(%o4)                    - -------------
                           conjugate(z2)
```


Im Folgenden nutzt Maxima Symmetrieeigenschaften, um den konjugiert komplexen
Wert der Funktionen `gamma` und `sin` zu berechnen.  Die
Logarithmusfunktion `log` hat Spiegelsymmetrie, wenn das Argument einen
positiven Realteil hat.



```maxima
(%i5) conjugate(gamma(x+%i*y));
(%o5)                    gamma(x - %i y)
(%i6) conjugate(sin(x+%i*y));
(%o6)                    - sin(%i y - x)
(%i7) conjugate(log(x+%i*y));
(%o7)               conjugate(log(%i y + x))
(%i8) conjugate(log(1+%i*y));
(%o8)                     log(1 - %i y)
```

See also: `properties`, `distribute_over`, `cabs`, `carg`, `rectform`, `polarform`, `gamma`, `sin`, `log`.

<!-- category: SpecialFunctions -->
<!-- keywords: double_factorial -->
<!-- signatures: double_factorial(z) -->
### Function: double_factorial (z)

Ist die doppelte Fakultat, die allgemein definiert ist als


```maxima
2  1/4 (1 - cos(z %pi))  z/2       z
             (---)                     2    gamma(- + 1)
              %pi                                 2
```


$$
\left({{2}\over{\pi}}\right)^{{{1}\over{4}}\,\left(1-\cos \left(z\,
 \pi\right)\right)}\,2^{{{z}\over{2}}}\,\Gamma\left({{z}\over{2}}+1
 \right)
$$


Die Funktion `double_factorial` ist fur das numerische und symbolische
Rechnen geeignet.  Ist das Argument *z* eine ganze Zahl, eine
Gleitkommazahl, eine große Gleitkommazahl oder eine komplexe Gleitkommazahl,
dann wird ein numerisches Ergebnis berechnet.  Fur eine positive ganze Zahl
ist das Ergebnis gleich dem Ergebnis des Operators der doppelten Fakultat
`!!`.  Fur rationale Zahlen ist das Ergebnis eine Substantivform.


Fur negative gerade ganze Zahlen ist die Funktion `double_factorial`
nicht definiert.


Hat die Optionsvariable `factorial_expand` den Wert `true`, 
vereinfacht Maxima `double_factorial` fur das Argument `n-1` und
fur Argumente `n+2*k`, wobei `k` eine ganze Zahl ist.


Maxima kennt die Ableitung der Funktion `double_factorial`.


`double_factorial` wird automatisch auf die Elemente von Listen und
Matrizen sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Beispiele:


Numerische Ergebnisse fur ganze Zahlen, Gleitkommazahlen und komplexen
Gleitkommazahlen.



```maxima
(%i1) double_factorial([-3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1) [- 1, 1, 1, 1, 2, 3, 8, 15, 48, 105, 384, 945, 3840]

(%i2) double_factorial([1.5, 1.5b0, 0.5+%i, 0.5b0+%i]);
(%o2) [1.380662681753386, 1.380662681753387b0,
.4186422526242637 - .7218816624466643 %i, 
4.186422526242633b-1 - 7.218816624466641b-1 %i]
```


Vereinfachungen, wenn die Optionsvariable `factorial_expand` den Wert
`true` hat.



```maxima
(%i3) factorial_expand:true;
(%o3)                         true
(%i4) double_factorial(n-1);
                               n!
(%o4)                  -------------------
                       double_factorial(n)
(%i5) double_factorial(n+4);
(%o5)          (n + 2) (n + 4) double_factorial(n)
(%i6) double_factorial(n-4);

                       double_factorial(n)
(%o6)                  -------------------
                            (n - 2) n
```


Die Ableitung der Funktion `double_factorial`.



```maxima
(%i7) diff(double_factorial(x), x);
                                     2
                            %pi log(---) sin(%pi x)
                                    %pi                    x
(%o7) (double_factorial(x) (----------------------- + psi (- + 1)
                                       2                 0 2
                                                     + log(2)))/2
```

See also: `!!`, `factorial_expand`, `distribute_over`.

<!-- category: SpecialFunctions -->
<!-- keywords: entier -->
<!-- signatures: entier(x) -->
### Function: entier (x)

`entier` ist eine andere Bezeichnung fur die Funktion `floor`.
Siehe `floor`.

See also: `floor`.

<!-- category: SpecialFunctions -->
<!-- keywords: exp -->
<!-- signatures: exp(z) -->
### Function: exp (z)

Ist die Exponentialfunktion.  Die Exponentialfunktion `exp` wird von Maxima
sofort zu `%e^z` vereinfacht und tritt in vereinfachten
Ausdrucken nicht auf.  Maxima vereinfacht die Exponentialfunktion daher wie
die allgemeine Exponentiation `^`.  Daruberhinaus kennt Maxima
spezielle Regeln fur die Vereinfachung der Exponentialfunktion.


Ist das Argument *z* der Exponentialfunktion eine ganze oder rationale
Zahl wird ein vereinfachter Ausdruck zuruckgegeben.  Ist das Argument
*z* eine reelle oder komplexe Gleitkommazahl wird ein numerisches
Ergebnis berechnet.


Folgende Optionsvariablen kontrollieren die Vereinfachung der
Exponentialfunktion:



**%enumer** — Hat die Optionsvariable `%enumer` den Wert `true`, vereinfacht Maxima
die Eulersche Zahl `%e` immer dann zu ihrem numerischen Wert, wenn die
Optionsvariable `numer` auch den Wert `true` hat.
**%emode** — Hat die Optionsvariable `%emode` den Wert `true`, wendet Maxima
Regeln an, um Ausdrucke der Form `%e^(x*%i*%pi)` zu vereinfachen.
Der Standardwert von `%emode` ist `true`.  Wenn mit komplexen Zahlen
in der Polarform gerechnet wird, kann es hilfreich sein, die Optionsvariable
`%emode` auf den Wert `false` zu setzen.
**%e_to_numlog** — Hat die Optionsvariable `%e_to_numlog` den Wert `true`, vereinfacht
Maxima einen Ausdruck `%e^(r*log(x)` zu `x^r`, wobei *r*
eine rationale Zahl ist.  Ist *r* eine ganze Zahl wird diese Vereinfachung
von der Optionsvariablen `logsimp` kontrolliert.  Fur reelle oder
komplexe Gleitkommazahlen wird diese Vereinfachung nicht ausgefuhrt.
**radexpand** — Die Optionsvariable `radexpand` kontrolliert die Vereinfachung von
Ausdrucken der Form `(%e^a)^b`.  Ist *a* ein reelles Argument
vereinfacht Maxima immer zu einem Ausdruck `%e^(a*b)`.  Ist *a* ein
komplexes Argument, wird die Vereinfachung `%e^(a*b)` dann ausgefuhrt,
wenn die Optionsvariable `radexpand` den Wert `all` hat.
**logsimp** — Die Optionsvariable `logsimp` kontrolliert die Vereinfachung der 
Exponentialfunktion fur den Fall, dass im Argument *expr* die
Logarithmusfunktion `log` auftritt.  Hat die `logsimp` den Wert
`true`, wird ein Ausdruck `%e^(n*log(x)` zu `x^n` vereinfacht,
wenn *n* eine ganze Zahl ist.  Mit der Optionsvariablen
`%e_to_numlog` wird diese Vereinfachung fur eine rationale Zahl *n*
kontrolliert.
**demoivre** — Ist eine Optionsvariable und eine Funktion, die auch als Auswertungsschalter
`evflag` definiert ist.  Hat die Optionsvariable `demoivre` den Wert
`true`, wird ein Ausdruck `%e^(x + %i y)` zu
`%e^x (cos(y) + %i sin(y))` vereinfacht.  Siehe auch die Optionsvariable
`exponentialize`.


Maxima kennt viele spezielle unbestimmte und bestimmte Integrale mit der 
Exponentialfunktion.

See also: `^`, `%enumer`, `%e`, `numer`, `%emode`, `%e_to_numlog`, `logsimp`, `radexpand`, `log`, `evflag`, `demoivre`, `exponentialize`.

<!-- category: SpecialFunctions -->
<!-- keywords: factcomb -->
<!-- signatures: factcomb(expr) -->
### Function: factcomb (expr)

Fasst Faktoren mit Fakultaten im Ausdruck *expr* zusammen.  Zum Beispiel
wird `(n+1)*n!` zu `(n+1)!` zusammengefasst.


Hat die Optionsvariable `sumsplitfact` den Wert `false`, wird nach
der Vereinfachung mit `factcomb` die Funktion `minfactorial` auf den 
Ausdruck *expr* angewendet.


Beispiele:



```maxima
(%i1) expr: ((n+1)*n!)/(n+2)!;
                           (n + 1) n!
(%o1)                      ----------
                            (n + 2)!
(%i2) factcomb(expr);

                            (n + 1)!
(%o2)                       --------
                            (n + 2)!

(%i3) factcomb(expr), sumsplitfact:false;
                                1
(%o3)                         -----
                              n + 2
```

See also: `sumsplitfact`, `minfactorial`.

<!-- category: SpecialFunctions -->
<!-- keywords: factlim -->
<!-- signatures: factlim -->
### Variable: factlim

Standardwert: 100000


Die Optionsvariable `factlim` spezifiziert die großte ganze Zahl, 
fur die die Fakultat einer ganzen Zahl numerisch berechnet wird.  Hat
`factlim` den Wert -1, wird die Fakultat fur jede ganze Zahl
berechnet.  Siehe die Funktion `factorial`.

See also: `factorial`.

<!-- category: SpecialFunctions -->
<!-- keywords: factorial, ! -->
<!-- signatures: factorial(z), ! -->
### Function: factorial (z)

Die Funktion `factorial` ist fur das numerische und symbolische Rechnen
der Fakultat geeignet.  Der Operator der Fakultat `!`, ist identisch
mit der Funktion `factorial`.


Fur eine ganze Zahl `n`, vereinfacht `n!` zum Produkt der ganzen
Zahlen von 1 bis einschließlich `n`.  `0!` vereinfacht zu 1.
Fur reelle und komplexe Gleitkommazahlen wird `z!` mit der
Verallgemeinerung `gamma(z+1)` berechnet.  Siehe die Funktion
`gamma`.  Fur eine halbzahlige rationale Zahl `n/2`, vereinfacht
`(n/2)!` zu einem rationalen Faktor multipliziert mit `sqrt(%pi)`.


Die Optionsvariable `factlim` enthalt die großte Zahl, fur die
die Fakultat einer ganzen Zahl numerisch berechnet wird.  Ist das Argument
der Fakultat eine rationale Zahl, wird von Maxima die Funktion
`gamma` fur die numerische Berechnung aufgerufen.  In diesem Fall ist
`gammalim - 1` der großte Nenner, fur den die Fakultat vereinfacht
wird.  Siehe `gammalim`.


Hat die Optionsvariable `factorial_expand` den Wert `true`, wird die
Fakultat von Argumenten der Form `(n+k)!` oder `(n-k)!` vereinfacht,
wobei `k` eine ganze Zahl ist.


Mit den Funktionen `minfactorial` und `factcomb` konnen Fakultaten
in Ausdrucken vereinfacht werden.


Die Funktion `makegamma` ersetzt Fakultaten in einem Ausdruck durch die
Gammafunktion `gamma`.  Umgekehrt ersetzt die Funktion
`makefact` Binomialkoeffizienten und die Gammafunktion in einem Ausdruck
durch Fakultaten.


Maxima kennt die Ableitung der Fakultat und die Grenzwerte der Fakultat
fur spezielle Werte wie negative ganze Zahlen.


Siehe auch die Gammfunktion `gamma` und den Binomialkoeffizienten
`binomial`.


Beispiele:


Die Fakultat einer ganzen Zahl wird zu einer exakten Zahl vereinfacht, wenn
das Argument nicht großer als `factlim` ist.  Die Fakultat fur 
reelle und komplexe Zahlen wird als Gleitkommazahl berechnet.



```maxima
(%i1) factlim:10;
(%o1)                          10
(%i2) [0!, (7/2)!, 8!, 20!];
                     105 sqrt(%pi)
(%o2)            [1, -------------, 40320, 20!]
                          16
(%i3) [4.77!, (1.0+%i)!];
(%o3) [81.44668037931197, .3430658398165451 %i
                                             + .6529654964201663]
(%i4) [2.86b0!, (1.0b0+%i)!];
(%o4) [5.046635586910012b0, 3.430658398165454b-1 %i
                                          + 6.529654964201667b-1]
```


Die Fakultat von numerischen Konstanten oder eines konstanten Ausdrucks wird
numerisch berechnet, wenn die Konstante oder der Ausdruck zu einer Zahl
ausgewertet werden kann.



```maxima
(%i1) [(%i + 1)!, %pi!, %e!, (cos(1) + sin(1))!];
(%o1)      [(%i + 1)!, %pi!, %e!, (sin(1) + cos(1))!]
(%i2) ev (%, numer, %enumer);
(%o2) [.3430658398165451 %i + .6529654964201663, 
         7.188082728976031, 4.260820476357003, 1.227580202486819]
```


Fakultaten werden vereinfacht und nicht ausgewertet.  Daher wird die
Fakultat auch dann berechnet, wenn die Auswertung mit dem
Quote-Operator `'` unterdruckt ist.



```maxima
(%i1) '([0!, (7/2)!, 4.77!, 8!, 20!]);
            105 sqrt(%pi)
(%o1)   [1, -------------, 81.44668037931197, 40320, 20!]
                 16
```


Maxima kennt die Ableitung der Fakultat.



```maxima
(%i1) diff(x!, x);
(%o1)                    x! psi (x + 1)
                               0
```


Die Optionsvariable `factorial_expand` kontrolliert die Expansion und
Vereinfachung von Ausdrucken, die die Fakultat enthalten.



```maxima
(%i1) (n+1)!/n!,factorial_expand:true;
(%o1)                         n + 1
```

See also: `gamma`, `factlim`, `gammalim`, `factorial_expand`, `minfactorial`, `factcomb`, `makegamma`, `makefact`, `binomial`.

<!-- category: SpecialFunctions -->
<!-- keywords: factorial_expand -->
<!-- signatures: factorial_expand -->
### Variable: factorial_expand

Standardwert: `false`


Die Optionsvariable `factorial_expand` kontrolliert die Vereinfachung von
Aus­dru­cken wie `(n+k)!` oder `(n-k)!`, wobei `k` eine
ganze Zahl ist.  Siehe `factorial` fur ein Beispiel.


Siehe auch die Funktionen `minfactorial` und `factcomb` fur die
Vereinfachung von Ausdrucken mit der Fakultat.

See also: `factorial`, `minfactorial`, `factcomb`.

<!-- category: SpecialFunctions -->
<!-- keywords: fix -->
<!-- signatures: fix(x) -->
### Function: fix (x)

`fix` ist eine andere Bezeichnung fur die Funktion `floor`.  Siehe
`floor`.

See also: `floor`.

<!-- category: SpecialFunctions -->
<!-- keywords: floor -->
<!-- signatures: floor(x) -->
### Function: floor (x)

Die Funktion `floor` ist fur das numerische und symbolische Rechnen
geeignet.


Ist das Argument *x* eine reelle Zahl, gibt `floor` die großte
ganze Zahl zuruck, die kleiner oder gleich *x* ist.


Die Funktion `floor` gibt auch dann einen numerischen Wert zuruck, wenn
das Argument ein konstanter Ausdruck ist, wie zum Beispiel `1+%e`, der zu
einer reellen Zahl ausgewertet werden kann.  In diesem Fall wird der konstante
Ausdruck in eine große Gleitkommazahl umgewandelt, auf die die Funktion
`floor` angewendet wird.  Aufgrund von Rundungsfehlern bei der Umwandlung
in Gleitkommazahlen kann es zu Fehlern bei der Berechnung von `floor`
kommen.  Um diese zu minimieren, wird die Anzahl der Stellen
`fpprec` fur die Berechnung von `floor` um drei Stellen erhoht.


Ist das Argument *x* der Funktion ein komplexer Ausdruck, wird eine
Substantivform zuruckgegeben.


Wenn moglich werden Ausdrucke mit der Funktion `floor` von Maxima
vereinfacht.  Maxima kennt insbesondere Vereinfachungen fur den Fall, dass
das Argument der Funktion `floor` ein Ausdruck mit den Funktionen
`ceiling` oder `round` ist.  Weiterhin werden fur die Vereinfachung
die Aussagen und Fakten der aktiven Kontexte herangezogen.  Siehe
`Funktionen-und-Variablen-für-Fakten`.


`floor` wird automatisch auf die Elemente von Listen und Matrizen
sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Siehe auch die Funktionen `ceiling` und `round`.


Beispiele:



```maxima
(%i1) floor(ceiling(x));
(%o1)                      ceiling(x)
(%i2) floor(floor(x));
(%o2)                       floor(x)
(%i3) declare(n, integer);
(%o3)                         done
(%i4) floor([n, abs(n), min (n, 6)]);
(%o4)                [n, abs(n), min(6, n)]
(%i5) assume(x>0, x<1)$
(%i6) floor(x);
(%o6)                           0
```


Sind die Werte einer Funktion eine Teilmenge der ganzen Zahlen, kann diese als
`integervalued` deklariert werden.  Die Funktionen `ceiling` und
`floor` konnen diese Information nutzen, um Ausdrucke zu vereinfachen.



```maxima
(%i1) declare (f, integervalued)$
(%i2) floor(f(x));
(%o2)                         f(x)
(%i3) ceiling(f(x) - 1);
(%o3)                       f(x) - 1
```


Maxima kennt das Integral der Funktion `floor`.



```maxima
(%i6) integrate(floor(x),x);
                 (- floor(x) + 2 x - 1) floor(x)
(%o6)            -------------------------------
                                2
```

See also: `fpprec`, `ceiling`, `round`, `Funktionen-und-Variablen-für-Fakten`, `distribute_over`, `integervalued`.

<!-- category: SpecialFunctions -->
<!-- keywords: genfact -->
<!-- signatures: genfact(x, y, z) -->
### Function: genfact (x, y, z)

Gibt die verallgemeinerte Fakultat zuruck, die als `x (x-z) (x - 2 z) ... (x - (y - 1) z)` definiert ist.  Ist *x* eine ganze Zahl, dann
entspricht `genfact(x, x, 1)` der Fakultat `x!` und 
`genfact(x, x/2, 2)` der doppelten Fakultat `x!!`.  Siehe auch die 
Funktionen `factorial` und `double_factorial` sowie die Operatoren
`!` und `!!`.

See also: `factorial`, `double_factorial`, `!`, `!!`.

<!-- category: SpecialFunctions -->
<!-- keywords: halfangles -->
<!-- signatures: halfangles -->
### Variable: halfangles

Standardwert: `false`


Hat `halfangles` den Wert `true`, werden Winkel- und 
Hyperbelfunktionen mit halbzahligen Argumenten `expr/2` vereinfacht.


Fur ein reelles Argument *x* im Intervall `0 < x < 2*%pi` vereinfacht
der Sinus fur ein halbzahliges Argument zu einer einfachen Formel: 



```maxima
sqrt(1 - cos(x))
                         ----------------
                             sqrt(2)
```


Ein komplizierter Faktor wird gebraucht, damit die Formel korrekt ist fur ein
komplexes Argument *z*:




           realpart(z)
     floor(-----------)
              2 %pi
(- 1)                   (1 - unit_step(- imagpart(z))

                            realpart(z)            realpart(z)
                      floor(-----------) - ceiling(-----------)
                               2 %pi                  2 %pi
                ((- 1)                                          + 1))


Maxima kennt diesen Faktor und ahnliche Faktoren fur die Sinus, Kosinus,
Sinus Hyperbolicus und Kosinus Hyperbolicus Funktionen.  Fur spezielle 
Argumente $z$ dieser Funktionen vereinfachen diese Funktionen entsprechend.


Beispiele:



```maxima
(%i1) halfangles:false;
(%o1)                                false
(%i2) sin(x/2);
                                        x
(%o2)                               sin(-)
                                        2
(%i3) halfangles:true;
(%o3)                                true
(%i4) sin(x/2);
                                                    x
                                            floor(-----)
                                                  2 %pi
                      sqrt(1 - cos(x)) (- 1)
(%o4)                 ----------------------------------
                                   sqrt(2)
(%i5) assume(x>0, x<2*%pi)$
(%i6) sin(x/2);
                               sqrt(1 - cos(x))
(%o6)                          ----------------
                                   sqrt(2)
```

<!-- category: SpecialFunctions -->
<!-- keywords: imagpart -->
<!-- signatures: imagpart(expr) -->
### Function: imagpart (expr)

Gibt den Imaginarteil des Ausrucks *expr* zuruck.  Intern berechnet
Maxima den Imaginarteil mit der Funktion `rectform`, die einen
Ausdruck in den Realteil und in den Imaginarteil zerlegt.  Daher treffen die
Ausfuhrungen zu `rectform` auch auf die Funktion `imagpart` zu.


Wenn sowohl der Realteil als auch der Imaginarteil eines Ausdrucks von
Interesse sind, ist der Aufruf von `rectform` oder `real_imag_part`
effizienter als der Aufruf von `realpart` und `imagpart` auf demselben
Ausdruck.


Wie die Funktion `rectform` ist auch die Funktion `imagpart` eine
Verbfunktion, mit der nicht symbolisch gerechnet werden kann.


`imagpart` wird automatisch auf die Elemente von Listen und Matrizen sowie
auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Mit der Funktion `realpart` wird der Realteil eines Ausdrucks berechnet.


Siehe auch die Funktionen `cabs`, `carg`,
`conjugate`, `polarform` und `real_imag_part`.


Beispiele:


Fur weitere Erlauterungen dieser Beispiele siehe auch die Funktion
`rectform`.



```maxima
(%i1) imagpart((2-%i)/(1-%i));
                                1
(%o1)                           -
                                2
(%i2) imagpart(sin(x+%i*y));
(%o2)                    cos(x) sinh(y)
(%i3) imagpart(gamma(x+%i*y));
             %i (gamma(x - %i y) - gamma(%i y + x))
(%o3)        --------------------------------------
                               2
(%i4) imagpart(bessel_j(1,%i));
(%o4)                    bessel_j(1, %i)
```

See also: `rectform`, `real_imag_part`, `distribute_over`, `realpart`, `cabs`, `carg`, `conjugate`, `polarform`.

<!-- category: SpecialFunctions -->
<!-- keywords: lmax -->
<!-- signatures: lmax(L) -->
### Function: lmax (L)

Ist das Argument *L* eine Liste oder Menge, wird die Funktion `max` auf
die Elemente der Liste oder Menge angewendet und das Ergebnis zuruckgegeben.
Ist *L* keine Liste oder Menge, signalisiert Maxima einen Fehler.



Beispiel:



```maxima
(%i1) L:[1+%e, %pi, 3];
(%o1)                   [%e + 1, %pi, 3]
(%i1) lmax(L);
(%o1)                        %e + 1
```

See also: `max`.

<!-- category: SpecialFunctions -->
<!-- keywords: lmin -->
<!-- signatures: lmin(L) -->
### Function: lmin (L)

Ist das Argument *L* eine Liste oder Menge, wird die Funktion `min` auf
die Elemente der Liste oder Menge angewendet und das Ergebnis zuruckgegeben.
Ist *L* keine Liste oder Menge, signalisiert Maxima einen Fehler.


Beispiel:



```maxima
(%i1) L:[1+%e, %pi, 3];
(%o1)                   [%e + 1, %pi, 3]
(%i2) lmin(L);
(%o2)                           3
```

See also: `min`.

<!-- category: SpecialFunctions -->
<!-- keywords: log -->
<!-- signatures: log(z) -->
### Function: log (z)

Ist der naturliche Logarithmus zur Basis $e$.  Die Logarithmusfunktion
ist fur das numerische und symbolische Rechnen geeignet.


Maxima hat keine vordefinierte Logarithmusfunktion zur Basis 10 oder anderen 
Basen.  Eine einfache Definition ist zum Beispiel 
`log10(x) := log(x)/log(10)`.  Mit dem Kommando `load("log10")` kann ein
Paket geladen werden, dass eine dekadische Logarithmusfunktion `log10`
definiert.


Ist das Argument *z* der Logarithmusfunktion eine ganze oder rationale
Zahl wird ein vereinfachter Ausdruck zuruckgegeben.  Ist das Argument
*z* eine reelle oder komplexe Gleitkommazahl wird ein numerisches
Ergebnis berechnet.


Die folgenden Optionsvariablen kontrollieren die Vereinfachung und Auswertung
der Logarithmusfunktion:



**logexpand** — Hat die Optionsvariable `logexpand` den Wert `true`, dann wird
`log(a^b)` zu `b*log(a)` vereinfacht.  Hat `logexpand` den
Wert `all`, wird zusatzlich `log(a*b)` zu `log(a)+log(b)`
vereinfacht.  Mit den Wert `super` vereinfacht Maxima weiterhin
`log(a/b)` zu `log(a)-log(b)`, wobei `a/b` eine rationale Zahl
ist.  `log(1/b` wird fur eine ganze Zahl `b` immer vereinfacht.
Hat die Optionsvariable `logexpand` den Wert `false` werden alle
obigen Vereinfachungen ausgeschaltet.
**logsimp** — Hat die Optionsvariable `logsimp` den Wert `false`, werden 
Exponentialfunktionen `exp`, die Logarithmusfunktionen im Exponenten
enthalten, nicht vereinfacht.
**lognegint** — Hat die Optionsvariable `lognegint` den Wert `true`, wird
`log(-n)` zu `log(n)+%i*%pi` fur positive `n` vereinfacht.
**%e_to_numlog** — Hat die Optionsvariable `%e_to_numlog` den Wert `true`, wird ein 
Ausdruck `%e^(r*log(x))` zu `x^r` vereinfacht.  Dabei sind `r`  
eine rationale Zahl und `x` ein beliebiger Ausdruck.  Die Funktion 
`radcan` fuhrt diese Vereinfachung ebenfalls aus.


Die Logarithmusfunktion wird automatisch auf die Elemente von Listen und
Matrizen sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Beispiele:


Verschiedene Beispiele mit der Logarithmusfunktion.



```maxima
(%i1) log(%e);
(%o1)                           1
(%i2) log(100.0);
(%o2)                   4.605170185988092
(%i3) log(2.5+%i);
(%o3)       .3805063771123649 %i + .9905007344332917
(%i4) taylor(log(1+x),x,0,5);
                       2    3    4    5
                      x    x    x    x
(%o4)/T/          x - -- + -- - -- + -- + . . .
                      2    3    4    5
(%i5) rectform(log(x+%i*y));
                       2    2
                  log(y  + x )
(%o5)             ------------ + %i atan2(y, x)
                       2
(%i6) limit(log(x),x,0,plus);
(%o6)                         minf
(%i7) integrate(log(z)^n,z);

                                                    - n - 1
(%o7) - gamma_incomplete(n + 1, - log(z)) (- log(z))
                                                            n + 1
                                                      log(z)

(%i8) laplace(log(t),t,s);

                        - log(s) - %gamma
(%o8)                   -----------------
                                s

(%i9) depends(y,x);
(%o9)                        [y(x)]
(%i10) ode2(diff(y,x)+log(y)+1,y,x);
            - 1
(%o10)    %e    expintegral_e(1, - log(y) - 1) = x + %c
```

See also: `exp`, `distribute_over`.

<!-- category: SpecialFunctions -->
<!-- keywords: logabs -->
<!-- signatures: logabs -->
### Variable: logabs

Standardwert: `false`


Treten bei der unbestimmten Integration Logarithmusfunktionen im Ergebnis auf,
so wird der Betrag der Argumente der Logarithmusfunktionen gebildet, wenn die
Optionsvariable `logabs` den Wert `true` hat.


Beispiele:



```maxima
(%i1) logabs:true;
(%o1)                         true
(%i2) integrate(1/x,x);
(%o2)                      log(abs(x))
(%i3) integrate(1/(1+x^3),x);
                                                   2 x - 1
            ! 2        !                      atan(-------)
        log(!x  - x + 1!)   log(abs(x + 1))        sqrt(3)
(%o3) - ----------------- + --------------- + -------------
                6                  3             sqrt(3)
```

<!-- category: SpecialFunctions -->
<!-- keywords: logarc -->
<!-- signatures: logarc(expr) -->
### Function: logarc (expr)

Hat die Optionsvariable `logarc` den Wert `true`, werden inverse
Winkel- und Hyperbelfunktionen durch Logarithmusfunktionen ersetzt.  Der 
Standardwert von `logarc` ist `false`.


Die Funktion `logarc(expr)` fuhrt diese Ersetzung aus, ohne dass 
die Optionsvariable `logarc` gesetzt wird.


Beispiele:



```maxima
(%i1) logarc(asin(x));
                                     2
(%o1)             - %i log(sqrt(1 - x ) + %i x)
(%i2) logarc:true;
(%o2)                         true
(%i3) asin(x);
                                     2
(%o3)             - %i log(sqrt(1 - x ) + %i x)
```

<!-- category: SpecialFunctions -->
<!-- keywords: logconcoeffp -->
<!-- signatures: logconcoeffp -->
### Variable: logconcoeffp

Standardwert: `false`


Der Optionsvariablen `logconcoeffp` kann eine Aussagefunktion mit einem
Argument zugewiesen werden, die kontrolliert, welche Koeffizienten von
der Funktion `logcontract` zusammengezogen werden.  Sollen zum Beispiel
Wurzeln generiert werden, kann folgende Aussagefunktion definiert werden:



```maxima
logconcoeffp:'logconfun$ 
logconfun(m) := featurep(m,integer) or ratnump(m)$
```


Das Kommando `logcontract(1/2*log(x))` liefert nun das Ergebnis
`log(sqrt(x))`.

See also: `logcontract`.

<!-- category: SpecialFunctions -->
<!-- keywords: logcontract -->
<!-- signatures: logcontract(expr) -->
### Function: logcontract (expr)

Der Ausdruck *expr* wird rekursiv nach Ausdrucken der Form 
`a1*log(b1) + a2*log(b2) + c` durchsucht.  Diese werden zu
`log(ratsimp(b1^a1 * b2^a2)) + c` transformiert.



```maxima
(%i1) 2*(a*log(x) + 2*a*log(y))$
(%i2) logcontract(%);
                                 2  4
(%o2)                     a log(x  y )
```


Wird die Variable *n* mit dem Kommando `declare(n, integer)` als eine
ganze Zahl deklariert, dann wird  `logcontract(2*a*n*log(x))` zu
`a*log(x^(2*n))` vereinfacht.  Die Koeffizienten, die zusammengezogen 
werden, sind in diesem Fall die Zahl 2 und die Variable *n*, welche
die folgende Aussage erfullen `featurep(coeff, integer)`.
Der Nutzer kann kontrollieren, welche Koeffizienten zusammengezogen werden.
Dazu wird der Optionsvariablen `logconcoeffp` eine Aussagefunktion mit 
einem Argument zugewiesen.  Sollen zum Beispiel Wurzeln generiert werden, kann 
folgende Definition verwendet: `logconcoeffp: 'logconfun$ logconfun(m) := featurep(m,integer) or ratnump(m)$`.  Dann hat das Kommando
`logcontract(1/2*log(x))` das Ergebnis `log(sqrt(x))`.

See also: `logconcoeffp`.

<!-- category: SpecialFunctions -->
<!-- keywords: logexpand -->
<!-- signatures: logexpand -->
### Variable: logexpand

Standardwert: `true`


Die Optionsvariable `logexpand` kontrolliert die Vereinfachung der
Logarithmusfunktion `log`.


Hat `logexpand` den Wert `true`, wird `log(a^b)` zu
`b*log(a)` vereinfacht.  Hat `logexpand` den Wert `all`, wird
zusatzlich `log(a*b)` zu `log(a)+log(b)` vereinfacht.  Mit dem Wert
`super` vereinfacht Maxima weiterhin `log(a/b)` zu
`log(a)-log(b)`, wobei `a/b` eine rationale Zahl ist.  `log(1/b`
wird fur eine ganze Zahl `b` immer vereinfacht.  Hat die Optionsvariable
`logexpand` den Wert `false` werden alle obigen Vereinfachungen
ausgeschaltet.

See also: `log`.

<!-- category: SpecialFunctions -->
<!-- keywords: lognegint -->
<!-- signatures: lognegint -->
### Variable: lognegint

Standardwert: `false`


Hat die Optionsvariable `lognegint` den Wert `true`, wird
`log(-n)` zu `log(n)+%i*%pi` fur positive `n` vereinfacht.

<!-- category: SpecialFunctions -->
<!-- keywords: logsimp -->
<!-- signatures: logsimp -->
### Variable: logsimp

Standardwert: `true`


Hat die Optionsvariable `logsimp` den Wert `false`, werden 
Exponentialfunktionen `exp`, die Logarithmusfunktionen im Exponenten
enthalten, nicht vereinfacht.

See also: `exp`.

<!-- category: SpecialFunctions -->
<!-- keywords: make_random_state -->
<!-- signatures: make_random_state(n), make_random_state(s), make_random_state(true), make_random_state(false) -->
### Function: make_random_state (n)

Ein Zufallszustand reprasentiert den Zustand des Zufallszahlengenerators.  Der
Zustand enthalt 627 32-Bit Worte.


`make_random_state(n)` gibt einen neuen Zufallszustand zuruck, der 
aus einer ganzen Zahl *n* modulo 2^32 erzeugt wird.  *n* kann eine 
negative Zahl sein.


`make_random_state(s)` gibt eine Kopie des Zufallszutandes *s*
zuruck.


`make_random_state(true)` gibt einen neuen Zufallszustand zuruck, der aus
der aktuellen Systemzeit des Computers erzeugt wird.


`make_random_state(false)` gibt eine Kopie des aktuellen Zustands des
Zufallszahlengenerators zuruck.

<!-- category: SpecialFunctions -->
<!-- keywords: max -->
<!-- signatures: max(x_1, ..., x_n) -->
### Function: max (x_1, ..., x_n)

Sind alle Argumente *x_1*, ..., *x_n* Zahlen oder konstante
Ausdrucke wie zum Beispiel `1+%e` oder `sin(1)`, dann wird der
großte Zahlenwert zuruckgegeben.  Sind symbolische Variablen oder
allgemeine Ausdrucke unter den Argumenten, gibt Maxima einen vereinfachten
Ausdruck zuruck.  Die unendliche Großen `inf` und `minf`
konnen als Argument auftreten.


Die Vereinfachung der Funktion `max` kann kontrolliert werden, in dem mit
der Funktion `put` dem Symbol `trylevel` zu der Eigenschaft
`maxmin` ein Wert zwischen 1 bis 3 gegeben wird.  Folgende Werte konnen 
mit der Funktion `put` gesetzt werden:



**put(trylevel, 1, maxmin)** — `trylevel` hat den Wert 1.  Das ist der Standardwert.  Maxima fuhrt
keine besonderen Vereinfachungen aus.
**put(trylevel, 2, maxmin)** — Maxima wendet die Vereinfachung `max(e,-e) --> |e|` an.
**put(trylevel, 3, maxima)** — Maxima wendet die Vereinfachung `max(e,-e) --> |e|` an und versucht
Ausdrucke zu eliminieren, die zwischen zwei anderen Argumenten liegen.  So
wird zum Beispiel `max(x, 2*x, 3*x)` zu `max(x, 3*x)` vereinfacht.


Mit dem Kommando `get(trylevel, maxmin)` wird der aktuelle Wert fur
das Symbol `trylevel` angezeigt.  Siehe die Funktion `get`.


`max` berucksichtigt bei der Vereinfachung von Ausdrucken die
Aussagen und Fakten der aktiven Kontexte.  Siehe das Kapitel
`Funktionen-und-Variablen-für-Fakten`.


Beispiele:



```maxima
(%i1) max(1.6, 3/2, 1);
(%o1)                          1.6
(%i2) max(1.5b0,1.5,3/2);

                                3
(%o2)                           -
                                2

(%i3) max(%e,%pi,1,2,3);
(%o3)                          %pi
(%i4) max(1+%e,%pi,1,2,3);
(%o4)                        %e + 1
(%i5) max(minf,inf);
(%o5)                          inf
(%i6) assume(a>b);
(%o6)                        [a > b]
(%i7) max(a,b);
(%o7)                           a
```

See also: `inf`, `minf`, `put`, `get`, `Funktionen-und-Variablen-für-Fakten`.

<!-- category: SpecialFunctions -->
<!-- keywords: min -->
<!-- signatures: min(x_1, ..., x_n) -->
### Function: min (x_1, ..., x_n)

Sind alle Argumente *x_1*, ..., *x_n* Zahlen oder konstante
Ausdrucke wie zum Beispiel `1+%e` oder `sin(1)`, dann wird der
kleinste Zahlenwert zuruckgegeben.  Sind symbolische Variablen oder
allgemeine Ausdrucke unter den Argumenten, gibt Maxima einen vereinfachten
Ausdruck zuruck.  Die unendliche Großen `inf` und `minf`
konnen als Argument auftreten.


Die Vereinfachung der Funktion `min` kann kontrolliert werden, in dem mit
der Funktion `put` dem Symbol `trylevel` zu der Eigenschaft
`maxmin` ein Wert zwischen 1 bis 3 gegeben wird.  Folgende Werte konnen
mit der Funktion `put` gesetzt werden:



**put(trylevel, 1, maxmin)** — `trylevel` hat den Wert 1.  Das ist der Standardwert.  Maxima fuhrt
keine besonderen Vereinfachungen aus.
**put(trylevel, 2, maxmin)** — Maxima wendet die Vereinfachung `min(e,-e) --> |e|` an.
**put(trylevel, 3, maxima)** — Maxima wendet die Vereinfachung `min(e,-e) --> |e|` an und versucht
Ausdrucke zu eliminieren, die zwischen zwei anderen Argumenten liegen.  So
wird zum Beispiel `min(x, 2*x, 3*x)` zu `min(x, 3*x)` vereinfacht.


Mit dem Kommando `get(trylevel, maxmin)` wird der aktuelle Wert fur
das Symbol `trylevel` angezeigt.  Siehe die Funktion `get`.


`min` berucksichtigt bei der Vereinfachung von Ausdrucken die
Aussagen und Fakten der aktiven Kontexte.  Siehe das Kapitel
Funktionen und Variablen fur Fakten.


Beispiele:



```maxima
(%i1) min(1.6, 3/2, 1);
(%o1)                           1
(%i2) min(1.5b0,1.5,3/2);
                                3
(%o2)                           -
                                2
(%i3) min(%e,%pi,3);
(%o3)                          %e
(%i4) min(1+%e,%pi,3);
(%o4)                           3
(%i5) min(minf,inf);
(%o5)                         minf
(%i6) assume(a>b);
(%o6)                        [a > b]
(%i7) min(a,b);
(%o7)                           b
```

See also: `inf`, `minf`, `put`, `get`.

<!-- category: SpecialFunctions -->
<!-- keywords: minfactorial -->
<!-- signatures: minfactorial(expr) -->
### Function: minfactorial (expr)

Die Funktion `minfactorial` vereinfacht Fakultaten `factorial` in
dem Ausdruck *epxr*, die sich um eine ganze Zahl voneinander unterscheiden.
Siehe auch die Funktion `factcomb`, um Fakultaten zusammenzufassen,
sowie die Optionsvariable `factorial_expand`.



```maxima
(%i1) n!/(n+2)!;
                               n!
(%o1)                       --------
                            (n + 2)!
(%i2) minfactorial (%);
                                1
(%o2)                    ---------------
                         (n + 1) (n + 2)
```

See also: `factorial`, `factcomb`, `factorial_expand`.

<!-- category: SpecialFunctions -->
<!-- keywords: ntrig -->
<!-- signatures: ntrig -->
### Variable: ntrig

Das Paket `ntrig` enthalt Regeln, um Winkelfunktionen zu vereinfachen, 
die Argumente der Form `f(n %pi/10)` haben.  *f* ist eine 
der Funktionen `sin`, `cos`, `tan`, `csc`, `sec` oder 
`cot`.


Das Kommando `load("ntrig")` ladt das Paket.  Die Vereinfachungen werden
dann von Maxima automatisch ausgefuhrt.

<!-- category: SpecialFunctions -->
<!-- keywords: plog -->
<!-- signatures: plog(x) -->
### Function: plog (x)

Gibt den Hauptwert des komplexen naturlichen Logarithmus im Intervall
`-%pi` < `carg(x)` <= `+%pi` zuruck.

<!-- category: SpecialFunctions -->
<!-- keywords: polarform -->
<!-- signatures: polarform(expr) -->
### Function: polarform (expr)

Gibt den Ausdruck *expr* in der Polarform `r %e^(%i theta)` zuruck.
`r` ist der Betrag des komplexen Ausdrucks, wie er auch mit der Funktion
`cabs` berechnet werden kann.  `theta` ist das Argument des komplexen
Ausdrucks, das mit der Funktion `carg` berechnet werden kann.


Maxima kennt komplexe Eigenschaften von Funktionen, die bei der Berechnung der
Polarform angewendet werden.  Siehe die Funktion `cabs` fur weitere
Erlauterungen.


Wenn mit komplexen Ausdrucken in der Polarform gerechnet werden soll, ist es
hilfreich die Optionsvariable `%emode` auf den Wert `false` zu setzen.
Damit wird verhindert, dass Maxima komplexe Ausdrucke mit der
Exponentialfunktion `exp` automatisch in die Standardform vereinfacht.


`polarform` wird automatisch auf die Elemente von Listen und Matrizen sowie
auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Die Funktion `polarform` ist eine Verbfunktion, mit der nicht symbolisch
gerechnet werden kann.


Siehe auch die Funktionen `cabs`, `carg` und
`conjugate` fur das Rechnen mit komplexen Zahlen.  Mit der Funktion
`rectform` kann ein komplexer Ausdruck in die Standardform gebracht werden.


Beispiele:


Die allgemeine Polarform eines komplexen Ausdrucks.  Die Variablen *x* und
*y* werden von Maxima als reell angenommen.



```maxima
(%i1) polarform(x+%i*y);

                       2    2    %i atan2(y, x)
(%o1)            sqrt(y  + x ) %e
```


Die Polarform einer komplexen Zahl und eines Ausdrucks mit einer reellen 
Variablen *x*.



```maxima
(%i2) polarform(4/5+3*%i/5);
                           %i atan(3/4)
(%o2)                    %e
(%i3) polarform(sqrt(1+%i*x));
                                  %i atan(x)
                                  ----------
                      2     1/4       2
(%o3)               (x  + 1)    %e
```


Wenn in der Polarform gerechnet werden soll, ist es hilfreich die
Optionsvariable `%emode` auf den Wert `false` zu setzen.  Damit wird
verhindert, dass Maxima komplexe Ausdrucke mit der Exponentialfunktion 
`exp` automatisch in eine Standardform vereinfacht.



```maxima
(%i4) z:polarform(1+%i);
                                  %i %pi
                                  ------
                                    4
(%o4)                   sqrt(2) %e
(%i5) z^3;
                     3/2    %i         1
(%o5)               2    (------- - -------)
                          sqrt(2)   sqrt(2)
(%i6) %emode:false;
(%o6)                         false
(%i7) z^3;
                                3 %i %pi
                                --------
                          3/2      4
(%o7)                    2    %e
```

See also: `cabs`, `carg`, `%emode`, `exp`, `distribute_over`, `conjugate`, `rectform`.

<!-- category: SpecialFunctions -->
<!-- keywords: random -->
<!-- signatures: random(x) -->
### Function: random (x)

Erzeugt eine Pseudo-Zufallszahl.  Ist *x* eine ganze Zahl, gibt 
`random(x)` eine ganze Zahl im Intervall 0 bis einschließlich
`x-1` zuruck.  Ist *x* eine Gleitkommazahl, gibt
`random(x)` eine positive Gleitkommazahl zuruck, die kleiner als
*x* ist.  `random` gibt eine Fehlermeldung, wenn *x* weder eine
ganze Zahl noch eine Gleitkommazahl ist oder wenn *x* eine negative Zahl 
ist.


Die Funktionen `make_random_state` und `set_random_state` verwalten
den Zustand des Zufallszahlengenerators.


Der Maxima-Zufallszahlengenerator ist eine Implementation des Mersenne twister
MT 19937.


Beispiele:



```maxima
(%i1) s1: make_random_state (654321)$
(%i2) set_random_state (s1);
(%o2)                         done
(%i3) random (1000);
(%o3)                          768
(%i4) random (9573684);
(%o4)                        7657880
(%i5) random (2^75);
(%o5)                11804491615036831636390
(%i6) s2: make_random_state (false)$
(%i7) random (1.0);
(%o7)                   .2310127244107132
(%i8) random (10.0);
(%o8)                   4.394553645870825
(%i9) random (100.0);
(%o9)                   32.28666704056853
(%i10) set_random_state (s2);
(%o10)                        done
(%i11) random (1.0);
(%o11)                  .2310127244107132
(%i12) random (10.0);
(%o12)                  4.394553645870825
(%i13) random (100.0);
(%o13)                  32.28666704056853
```

<!-- category: SpecialFunctions -->
<!-- keywords: real_imag_part -->
<!-- signatures: real_imag_part(expr) -->
### Function: real_imag_part (expr)

Gibt eine Liste `[a, b]` zuruck, so dass `a + b %i` zu *expr*
aquivalent ist und *a* und *b* rein reell sind.


Beispiele:



```maxima
(%i1) real_imag_part(sqrt(2)*%e^(%i*%pi/4));
(%o1)                        [1, 1]
(%i2) real_imag_part(sqrt(b^2+a^2)*%e^(%i*atan2(b, a)));
(%o2)                        [a, b]
(%i3) real_imag_part(sqrt(5)*%e^(%i*atan(2)));
(%o3)                        [1, 2]
(%i4) [r, i] : real_imag_part(log(x))$
(%i5) print("Der Realteil ist", r, "und der Imaginaerteil ist", i)$
Der Realteil ist log(abs(x)) und der Imaginaerteil ist atan2(0, x)
```

<!-- category: SpecialFunctions -->
<!-- keywords: realpart -->
<!-- signatures: realpart(expr) -->
### Function: realpart (expr)

Gibt den Realteil des Ausdrucks *expr* zuruck.  Intern berechnet Maxima
den Realteil mit der Funktion `rectform`, die einen Ausdruck in den
Realteil und in den Imaginarteil zerlegt.  Daher treffen die Ausfuhrungen
zu `rectform` auch auf die Funktion `realpart` zu.


Wenn sowohl der Realteil als auch der Imaginarteil eines Ausdrucks von
Interesse sind, ist der Aufruf von `rectform` oder `real_imag_part`
effizienter als der Aufruf von `realpart` und `imagpart` auf
demselben Ausdruck.


Wie die Funktion `rectform` ist auch die Funktion `realpart` eine
Verbfunktion, mit der nicht symbolisch gerechnet werden kann.


`realpart` wird automatisch auf die Elemente von Listen und Matrizen sowie
auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Mit der Funktion `imagpart` wird der Imaginarteil eines Ausdrucks
berechnet.


Siehe auch die Funktionen `cabs`, `carg`,
`conjugate`, `polarform`, `rectform` und
`real_imag_part`.


Beispiele:


Fur weitere Erlauterungen dieser Beispiele siehe auch die Funktion
`rectform`.



```maxima
(%i1) realpart((2-%i)/(1-%i));
                                3
(%o1)                           -
                                2
(%i2) realpart(sin(x+%i*y));
(%o2)                    sin(x) cosh(y)
(%i3) realpart(gamma(x+%i*y));
                gamma(%i y + x) + gamma(x - %i y)
(%o3)           ---------------------------------
                                2
(%i4) realpart(bessel_j(1,%i));
(%o4)                           0
```

See also: `rectform`, `real_imag_part`, `distribute_over`, `imagpart`, `cabs`, `carg`, `conjugate`, `polarform`.

<!-- category: SpecialFunctions -->
<!-- keywords: rectform -->
<!-- signatures: rectform(expr) -->
### Function: rectform (expr)

Zerlegt den Ausdruck *expr* in den Realteil `a` und den Imaginarteil
`b` und gibt den komplexen Ausdruck in der Standardform `a + b %i`
zuruck. Um *a* und *b* direkt zu erhalten, kann stattdessen die
Funktion `real_imag_part` verwendet werden.


Die Funktion `rectform` nutzt Symmetrieeigenschaften und implementierte
Eigenschaften komplexer Funktionen, um den Realteil und Imaginarteil eines
komplexen Ausdrucks zu berechnen.  Sind solche Eigenschaften fur eine Funktion
vorhanden, konnen diese mit der Funktion `properties` angezeigt werden.
Eigenschaften, die das Ergebnis der Funktion `rectform` bestimmen, sind:
`mirror symmetry`, `conjugate function` und
`complex characteristic`.


`rectform` ist eine Verbfunktion, die nicht fur das symbolische Rechnen
geeignet ist.


`rectform` wird automatisch auf die Elemente von Listen und Matrizen sowie
auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Die Funktionen `realpart` und `imagpart` geben jeweils allein den
Realteil und den Imaginarteil eines Ausdrucks zuruck.  Um einen Ausdruck in
die Polarform zu bringen, kann die Funktion `polarform` verwendet werden.


Siehe auch die Funktionen `cabs`, `carg`,
`conjugate`, `polarform` und `real_imag_part`..


Beispiele:


Zerlegung eines komplexen Ausdrucks und der Sinusfunktion `sin` in den
Realteil und Imaginarteil.  Maxima kennt komplexe Eigenschaften der
trigonometrischen Funktionen, um den Realteil und den Imaginarteil zu
bestimmen.



```maxima
(%i1) rectform((2-%i)/(1-%i));

                             %i   3
(%o1)                        -- + -
                             2    2

(%i2) rectform(sin(x+%i*y));
(%o2)          %i cos(x) sinh(y) + sin(x) cosh(y)
```


Bei der Zerlegung in einen Realteil und einen Imaginarteil nutzt Maxima die
Spiegelsymmetrie der Gammfunktion `gamma`.  Die Eigenschaft der 
Spiegelsymmetrie wird mit der Funktion `properties` angezeigt, der Eintrag
lautet `mirror symmetry`.



```maxima
(%i3) properties(gamma);
(%o3)    [mirror symmetry, noun, rule, gradef, transfun]

(%i4) rectform(gamma(x+%i*y));
      gamma(%i y + x) + gamma(x - %i y)
(%o4) ---------------------------------
                      2
                                gamma(x - %i y) - gamma(%i y + x)
                              - ---------------------------------
                                                2
```


Maxima kennt komplexe Eigenschaften der Besselfunktionen.  Die Besselfunktion
`bessel_j` ist fur eine ganzzahlige Ordnung und einem imaginaren
Argument rein imaginar.



```maxima
(%i5) rectform(bessel_j(1,%i));
(%o5)                  %i bessel_j(1, %i)
```

See also: `real_imag_part`, `properties`, `distribute_over`, `realpart`, `imagpart`, `polarform`, `cabs`, `carg`, `conjugate`, `sin`, `gamma`, `bessel_j`.

<!-- category: SpecialFunctions -->
<!-- keywords: rootsconmode -->
<!-- signatures: rootsconmode -->
### Variable: rootsconmode

Standardwert: `true`


`rootsconmode` kontrolliert das Verhalten der Funktion 
`rootscontract`.  Siehe die Funktion `rootscontract` fur Details.

See also: `rootscontract`.

<!-- category: SpecialFunctions -->
<!-- keywords: rootscontract -->
<!-- signatures: rootscontract(expr) -->
### Function: rootscontract (expr)

Konvertiert Produkte von Wurzeln in Wurzeln von Produkten.  Zum Beispiel hat 
`rootscontract(sqrt(x)*y^(3/2))` das Ergebnis `sqrt(x*y^3)`.


Hat die Optionsvariable `radexpand` den Wert `true` und die
Optionsvariable `domain` den Wert `real`, das sind die Standardwerte,
wird `abs(x)` zu `sqrt(x^2)` vereinfacht.  Zum Beispiel hat
`rootscontract(abs(x) * sqrt(y))` das Ergebnis `sqrt(x^2*y)`.


Die Optionsvariable `rootsconmode` kontrolliert das Ergebnis
folgendermaßen:



```maxima
Problem             Wert             Ergebnis 
                    rootsconmode     rootscontract
      
x^(1/2)*y^(3/2)     false            sqrt(x*y^3)
x^(1/2)*y^(1/4)     false            sqrt(x)*y^(1/4)
x^(1/2)*y^(1/4)     true             sqrt(x*sqrt(y))
x^(1/2)*y^(1/3)     true             sqrt(x)*y^(1/3)
x^(1/2)*y^(1/4)     all              (x^2*y)^(1/4)
x^(1/2)*y^(1/3)     all              (x^3*y^2)^(1/6)
```


Hat `rootsconmode` den Wert `false`, kontrahiert `rootscontract`
nur Faktoren mit rationalen Exponenten, die den gleichen Nenner haben.  Hat
`rootsconmode` den Wert `all`, wird das kleinste gemeinsame Vielfache
des Nenners der Faktoren verwendet, um die Faktoren zusammenzufassen.


Ahnlich wie bei der Funktion `logcontract` werden von
`rootscontract` die Argumente unter der Wurzel mit der Funktion 
`ratsimp` vereinfacht.


Beispiele:



```maxima
(%i1) rootsconmode: false$
(%i2) rootscontract (x^(1/2)*y^(3/2));
                                   3
(%o2)                      sqrt(x y )
(%i3) rootscontract (x^(1/2)*y^(1/4));
                                   1/4
(%o3)                     sqrt(x) y
(%i4) rootsconmode: true$
(%i5) rootscontract (x^(1/2)*y^(1/4));
(%o5)                    sqrt(x sqrt(y))

(%i6) rootscontract (x^(1/2)*y^(1/3));
                                   1/3
(%o6)                     sqrt(x) y

(%i7) rootsconmode: all$
(%i8) rootscontract (x^(1/2)*y^(1/4));
                              2   1/4
(%o8)                       (x  y)
(%i9) rootscontract (x^(1/2)*y^(1/3));
                             3  2 1/6
(%o9)                      (x  y )
(%i10) rootsconmode: false$
(%i11) rootscontract (sqrt(sqrt(x) + sqrt(1 + x))
                    *sqrt(sqrt(1 + x) - sqrt(x)));
(%o11)                          1
(%i12) rootsconmode: true$
(%i13) rootscontract (sqrt(5+sqrt(5)) - 5^(1/4)*sqrt(1+sqrt(5)));
(%o13)                          0
```

See also: `radexpand`, `domain`, `rootsconmode`, `logcontract`, `ratsimp`.

<!-- category: SpecialFunctions -->
<!-- keywords: round -->
<!-- signatures: round(x) -->
### Function: round (x)

Die Funktion `round` ist fur das numerische und symbolische Rechnen
geeignet.


Ist das Argument *x* eine reelle Zahl, gibt `round` die am
nachsten liegende ganze Zahl zuruck.  Vielfache von 1/2 werden auf die 
nachste gerade ganze Zahl gerundet.


Die Funktion `round` gibt auch dann einen numerischen Wert zuruck, wenn
das Argument ein konstanter Ausdruck ist, wie zum Beispiel `1+%e`, der zu
einer reellen Zahl ausgewertet werden kann.  In diesem Fall wird der konstante
Ausdruck in eine große Gleitkommazahl umgewandelt, auf die die Funktion
`round` angewendet wird.  Aufgrund von Rundungsfehlern bei der Umwandlung
in Gleitkommazahlen kann es zu Fehlern bei der Berechnung von `round`
kommen.  Um diese zu minimieren, wird die Anzahl der Stellen
`fpprec` fur die Berechnung von `round` um drei Stellen erhoht.


Ist das Argument *x* der Funktion ein komplexer Ausdruck, wird eine
Substantivform zuruckgegeben.


Wenn moglich werden Ausdrucke mit der Funktion `round` von Maxima
vereinfacht.  Maxima kennt insbesondere Vereinfachungen fur den Fall, dass
das Argument der Funktion `round` ein Ausdruck mit den Funktionen
`ceiling` oder `floor` ist.  Weiterhin werden fur die Vereinfachung
die Aussagen und Fakten der aktiven Kontexte herangezogen.  Siehe 
`Funktionen-und-Variablen-für-Fakten`.


`round` wird automatisch auf die Elemente von Listen und Matrizen
sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Siehe auch die Funktionen `ceiling` und `floor`.


Beispiele:



```maxima
(%i1) round(floor(x));
(%o1)                       floor(x)
(%i2) round(round(x));
(%o2)                       round(x)
(%i3) declare(n, integer);
(%o3)                         done
(%i4) round([n, abs(n), min(n,6)]);
(%o4)                [n, abs(n), min(6, n)]
```


Sind die Werte einer Funktion eine Teilmenge der ganzen Zahlen, kann diese als
`integervalued` deklariert werden.  Die Funktion `round` kann diese
Information nutzen, um Ausdrucke zu vereinfachen.



```maxima
(%i1) declare(f, integervalued);
(%o1)                         done
(%i2) round(f(x));
(%o2)                         f(x)
(%i3) round(f(x) - 1);
(%o3)                       f(x) - 1
```

See also: `fpprec`, `ceiling`, `floor`, `Funktionen-und-Variablen-für-Fakten`, `distribute_over`, `integervalued`.

<!-- category: SpecialFunctions -->
<!-- keywords: set_random_state -->
<!-- signatures: set_random_state(s) -->
### Function: set_random_state (s)

Kopiert *s* in den Zufallszustand des Zufallszahlengenerators.


`set_random_state` gibt immer `done` zuruck.

<!-- category: SpecialFunctions -->
<!-- keywords: signum -->
<!-- signatures: signum(z) -->
### Function: signum (z)

Die Signumfunktion `signum` ist fur das numerische und symbolische
Rechnen geeignet.  Ist das Argument *z* eine Zahl, ist das Ergebnis 0, 1
oder -1, wenn die Zahl Null, positiv oder negativ ist.  Das Argument kann auch
ein konstanter Ausdruck wie `%pi` oder `1+%e` sein.  Ist das Argument
*z* eine komplexe Zahl, vereinfacht die der Ausdruck `signum(z)` zu
`z/abs(z)`.


Ist das Argument *z* keine Zahl oder kein konstanter Ausdruck, versucht
Maxima den Ausdruck zu vereinfachen.  Maxima kann die Funktion `signum`
differenzieren.  Wird das Paket abs_integrate geladen, kann Maxima
Integrale mit der Funktion `signum` losen.


`signum` wird automatisch auf die Elemente von Listen und Matrizen
sowie auf die beiden Seiten von Gleichungen angewendet.  Siehe
`distribute_over`.


Beispiele:


Ergebnisse fur verschiedene Zahlen und konstante Ausdrucke.  Die Beispiele
zeigen, dass das Ergebnis der Signumfunktion den Typ der Zahl erhalt.  Die
unendlichen Großen `minf` und `inf` konnen als Argument
auftreten.



```maxima
(%i1) signum([-1.5, 0, 0.0, 1.5, 1.5b0, %e, sin(1), cos(4)]);
(%o1)        [- 1.0, 0, 0.0, 1.0, 1.0b0, 1, 1, - 1]
(%i2) signum(1+%i);
                          %i         1
(%o2)                   ------- + -------
                        sqrt(2)   sqrt(2)
(%i3) signum([minf,inf]);
(%o3)                      [- 1, 1]
```


Vereinfachungen der Signumfunktion.



```maxima
(%i3) signum(x*y);
(%o3)                  signum(x) signum(y)
(%i4) signum(-x);
(%o4)                      - signum(x)
```


Wird das Paket abs_integrate geladen, kann Maxima Integrale mit der
Signumfunktion losen.  Ausdrucke mit der Signumfunktion konnen
differenziert werden.



```maxima
(%i5) load("abs_integrate")$

(%i6) integrate(signum(x),x);
(%o6)                        abs(x)

(%i7) integrate(sin(x)*signum(x),x);
(%o7)               (1 - cos(x)) signum(x)

(%i7) diff(%,x);
(%o7)                  signum(x) sin(x)
```

See also: `distribute_over`, `minf`, `inf`.

<!-- category: SpecialFunctions -->
<!-- keywords: sin, cos, tan, cot, csc, sec -->
<!-- signatures: sin(z), cos(z), tan(z), cot(z), csc(z), sec(z) -->
### Function: sin (z)

Die Winkelfunktionen: Sinus, Kosinus, Tangens, Kotangens, Kosekans und Sekans.


Die Winkelfunktionen sind fur das numerische und symbolische Rechnen geeignet.
Die Winkelfunktionen konnen fur reelle und komplexe Gleitkommazahlen in
doppelter und in beliebiger Genauigkeit berechnet werden.  Ist das Argument 
eine ganze oder rationale Zahl, werden die Winkelfunktionen nicht numerisch
berechnet, sondern vereinfacht.  Die numerische Berechnung kann mit den
Optionsvariablen und Auswertungsschaltern `numer` und `float`
erzwungen werden.


Die Winkelfunktionen sind gerade oder ungerade und haben Spiegelsymmetrie.
Maxima wendet diese Symmetrieeigenschaften automatisch bei der Vereinfachung
von Ausdrucken mit Winkelfunktionen an.


Ist das Argument *z* eine Matrix, eine Liste oder eine Gleichung werden die
Winkelfunktionen auf die Elemente der Matrix, der Liste oder auf die beiden
Seiten der Gleichung angewendet.  Dieses Verhalten wird von der Optionsvariablen
`distribute_over` kontrolliert.


Winkelfunktionen konnen fur das symbolische Rechnen verwendet werden.
Maxima kann Ausdrucke mit Winkelfunktionen differenzieren und integrieren,
Grenzwerte bestimmen sowie Gleichungen und  Differentialgleichungen mit
Winkelfunktionen losen.


Das Argument der Winkelfunktionen kann eine Taylorreihe sein.  In diesem Fall
wird die Taylorreihenentwicklung fur die Winkelfunktion vollstandig
ausgefuhrt.


Die folgenden Optionsvariablen kontrollieren die Vereinfachung der
Winkelfunktionen:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und ist das
Argument der Winkelfunktion eine Matrix, Liste oder Gleichung wird die Funktion
auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der Standardwert
ist `true`.
**%piargs** — Hat die Optionsvariable `%piargs` den Wert `true`, werden die
Winkelfunktionen fur ganzzahlige und halbzahlige Vielfache der Konstanten
`%pi` zu speziellen Werten vereinfacht.  Der Standardwert ist `true`.
**%iargs** — Hat die Optionsvariable `%iargs` den Wert `true` und ist das Argument
der Winkelfunktion ein Vielfaches der imaginaren Einheit `%i` werden die
Winkelfunktionen zu Hyperbelfunktionen vereinfacht.  Der Standardwert ist
`true`.
**trigsign** — Hat die Optionsvariable `trigsign` den Wert `true`, werden die gerade
oder ungerade Symmetrie der Winkelfunktionen bei der Vereinfachung angewendet.
Der Standardwert ist `true`.
**triginverses** — Hat die Optionsvariable `triginverses` den Wert `true` und ist das
Argument eine inverse Winkelfunktion vereinfachen die Winkelfunktionen zu einem
einfachen algebraischen Ausdruck, zum Beispiel vereinfacht `sin(acos(x))`
zu `sqrt(1-x^2)`.  Der Standardwert ist `true`.
**trigexpand** — Hat die Optionsvariable `trigexpand` den Wert `true`, dann werden die
Winkelfunktionen fur ein Argument expandiert, das eine Summe oder ein Produkt
mit einer ganzen Zahl ist.  Der Standardwert ist `false`.
**exponentialize** — Hat die Optionsvariable `exponentialize` den Wert `true`, dann werden
die Winkelfunktionen in eine Exponentialform transformiert.  Der Standardwert
ist `false`.
**halfangles** — Hat die Optionsvariable `halfangles` den Wert `true`, dann werden die
Winkelfunktionen fur halbzahlige Argumente zu einem aquivalenten Ausdruck
transformiert.  Der Standardwert ist `false`.


Beispiele:


Im Folgenden werden Beispiele fur die Sinusfunktion gezeigt.  Numerische
Berechnungen fur Gleitkommazahlen:



```maxima
(%i1) sin(1+%i);
(%o1)                      sin(%i + 1)
(%i2) sin(1.0+%i);
(%o2)       .6349639147847361 %i + 1.298457581415977
(%i3) sin(1.0b0+%i);
(%o3)     6.349639147847361b-1 %i + 1.298457581415977b0
(%i4) sin(1.0b0),fpprec:45;
(%o4)   8.41470984807896506652502321630298999622563061b-1
```


Einige Vereinfachungen der Sinusfunktionen:



```maxima
(%i5) sin(%i*(x+y));
(%o5)                    %i sinh(y + x)
(%i6) sin(%pi/3);
                             sqrt(3)
(%o6)                        -------
                                2
(%i2) sin(x+y),trigexpand:true;
(%o2)             cos(x) sin(y) + sin(x) cos(y)
(%i3) sin(2*x+y),trigexpand:true;
           2         2
(%o3)  (cos (x) - sin (x)) sin(y) + 2 cos(x) sin(x) cos(y)
```


Grenzwerte, Ableitungen und Integrale mit der Sinusfunktion:



```maxima
(%i4) limit(sin(x)/x,x,0);
(%o4)                          1
(%i5) diff(sin(sqrt(x))/x,x);
                  cos(sqrt(x))   sin(sqrt(x))
(%o5)             ------------ - ------------
                        3/2            2
                     2 x              x
(%i6) integrate(sin(x^3),x);

(%o6) 
                         1      3                     1        3
        gamma_incomplete(-, %i x ) + gamma_incomplete(-, - %i x )
                         3                            3
      - ---------------------------------------------------------
                                   12
```


Reihenentwicklung der Sinusfunktion:



```maxima
(%i7) taylor(sin(x),x,0,3);

                              3
                             x
(%o7)/T/                 x - -- + . . .
                             6
```

See also: `numer`, `float`, `distribute_over`, `%piargs`, `%iargs`, `trigsign`, `triginverses`, `trigexpand`, `exponentialize`, `halfangles`.

<!-- category: SpecialFunctions -->
<!-- keywords: sinh, cosh, tanh, coth, csch, sech -->
<!-- signatures: sinh(x), cosh(x), tanh(x), coth(x), csch(x), sech(x) -->
### Function: sinh (x)

Die Hyperbelfunktionen: Sinus Hyperbolicus, Kosinus Hyperbolicus, Tangens
Hyperbolicus, Kotangens Hyperbolicus, Kosekans Hyperbolicus, Sekans
Hyperbolicus.

<!-- category: SpecialFunctions -->
<!-- keywords: sqrt -->
<!-- signatures: sqrt(z) -->
### Function: sqrt (z)

Ist die Wurzelfunktion.  Die Wurzelfunktion wird von Maxima sofort zu
`x^(1/2)` vereinfacht und tritt in Ausdrucken nicht auf.


Die Wurzelfunktion ist fur das numerische und symbolische Rechnen geeignet.
Ist das Argument *z* der Wurzelfunktion eine Gleitkommazahl, wird ein
numerisches Ergebnis zuruckgegeben.  Fur ganze und rationale Zahlen wird
die Wurzelfunktion vereinfacht.  Die numerische Berechnung kann mit den 
Optionsvariablen und Auswertungsschaltern `numer` und
`float` kontrolliert werden.


Hat die Optionsvariable `radexpand` den Wert `true`, werden die
n-ten Wurzeln von Faktoren unter einer Wurzel aus der Wurzel herausgezogen.
So wird zum Beispiel `sqrt(16*x^2)` nur dann zu `4*x` vereinfacht,
wenn `radexpand` den Wert `true` hat.


Siehe auch die Funktionen `rootscontract` und `sqrtdenest` fur die
Vereinfachung von Ausdrucken, die die Wurzelfunktion enthalten.


Beispiele:


Verschiedene Beispiele mit der Wurzelfunktion.



```maxima
(%i1) sqrt(4);
(%o1)                           2
(%i2) sqrt(24);
(%o2)                       2 sqrt(6)
(%i3) sqrt(2.0);
(%o3)                   1.414213562373095
(%i4) taylor(sqrt(1+x),x,0,5);
                       2    3      4      5
                  x   x    x    5 x    7 x
(%o4)/T/      1 + - - -- + -- - ---- + ---- + . . .
                  2   8    16   128    256
(%i5) rectform(sqrt(x+%i*y));
           2    2 1/4     atan2(y, x)
(%o5) %i (y  + x )    sin(-----------)
                               2
                                      2    2 1/4     atan2(y, x)
                                  + (y  + x )    cos(-----------)
                                                          2
(%i6) integrate(sqrt(t)*(t+1)^-2,t,0,1);
                             %pi - 2
(%o6)                        -------
                                4
```

See also: `numer`, `float`, `radexpand`, `rootscontract`, `sqrtdenest`.

<!-- category: SpecialFunctions -->
<!-- keywords: sumsplitfact -->
<!-- signatures: sumsplitfact -->
### Variable: sumsplitfact

Standardwert: `true`


Hat die Optionsvariable `sumsplitfact` den Wert `false`, wird von
der Funktion `factcomb` nach der Zusammenfassung von Fakultaten die
Funktion `minfactorial` angewendet.  Siehe die Funktion
`factcomb` fur ein Beispiel.

See also: `minfactorial`, `factcomb`.

<!-- category: SpecialFunctions -->
<!-- keywords: trigexpand -->
<!-- signatures: trigexpand(expr) -->
### Function: trigexpand (expr)

Die Funktion `trigexpand` expandiert Winkel- und Hyperbelfunktionen im 
Ausdruck *expr*, die Summen und Vielfache von Winkeln als Argument haben.
Die besten Ergebnisse werden erzielt, wenn der Ausdruck *expr* zunachst
expandiert wird.


Folgende Schalter kontrollieren `trigexpand`:



**trigexpand** — Wenn `true`, werden Sinus- und Kosinusfunktionen expandiert.
**halfangles** — Wenn `true`, werden Vereinfachungen fur halbzahlige Argumente angewendet.
**trigexpandplus** — Wenn `true`, werden Winkelfunktionen, die eine Summe als Argument haben,
wie zum Beispiel `sin(x+y)`, vereinfacht.
**trigexpandtimes** — Wenn `true`,  werden Winkelfunktionen, die ein Produkt als Argument haben,
wie zum Beispiel `sin(2 x)`, vereinfacht.


Beispiele:



```maxima
(%i1) x+sin(3*x)/sin(x),trigexpand=true,expand;
                         2           2
(%o1)               - sin (x) + 3 cos (x) + x


(%i2) trigexpand(sin(10*x+y));
(%o2)          cos(10 x) sin(y) + sin(10 x) cos(y)
```

<!-- category: SpecialFunctions -->
<!-- keywords: trigexpandplus -->
<!-- signatures: trigexpandplus -->
### Variable: trigexpandplus

Standardwert: `true`


`trigexpandplus` kontrolliert die Vereinfachung von Winkelfunktionen mit
der Funktion `trigexpand` fur den Fall, dass Winkelfunktionen mit Summen
als Argumente auftreten.  Hat `trigexpandplus` den Wert `true`,
werden zum Beispiel Winkelfunktionen wie `sin(x+y)` vereinfacht.

See also: `trigexpand`.

<!-- category: SpecialFunctions -->
<!-- keywords: trigexpandtimes -->
<!-- signatures: trigexpandtimes -->
### Variable: trigexpandtimes

Standardwert: `true`


`trigexpandtimes` kontrolliert die Vereinfachung von Winkelfunktionen mit
der Funktion `trigexpand` fur den Fall, dass Winkelfunktionen mit
Produkten als Argumente auftreten.  Hat `trigexpandtimes` den Wert 
`true`, werden zum Beispiel Winkelfunktionen wie `sin(2 x)` 
vereinfacht.

See also: `trigexpand`.

<!-- category: SpecialFunctions -->
<!-- keywords: triginverses -->
<!-- signatures: triginverses -->
### Variable: triginverses

Standardwert: `true`


Kontrolliert die Vereinfachung, wenn das Argument einer Winkelfunktion oder
Hyperbelfunktion eine der inversen Funktion ist.


Hat `triginverses` den Wert `all`, vereinfachen beide Ausdrucke
`atan(tan(x))` und `tan(atan(x))` zum Wert *x*.


Hat `triginverses` den Wert `all`, wird
`arcfun(fun(x))` nicht vereinfacht.


Hat `triginverses` den Wert `false`, werden
`arcfun(fun(x))` und 
`fun(arcfun(x))` nicht vereinfacht.

<!-- category: SpecialFunctions -->
<!-- keywords: trigrat -->
<!-- signatures: trigrat(expr) -->
### Function: trigrat (expr)

Gives a canonical simplifyed quasilinear form of a trigonometrical expression; 
*expr* is a rational fraction of several `sin`, `cos` or 
`tan`, the arguments of them are linear forms in some variables (or 
kernels) and `%pi/n` (*n* integer) with integer coefficients.
The result is a simplified fraction with numerator and denominator linear in 
`sin` and `cos`.  Thus `trigrat` linearize always when it is 
possible.



```maxima
(%i1) trigrat(sin(3*a)/sin(a+%pi/3));
(%o1)            sqrt(3) sin(2 a) + cos(2 a) - 1
```


The following example is taken from
Davenport, Siret, and Tournier, *Calcul Formel*, Masson (or in English,
Addison-Wesley), section 1.5.5, Morley theorem.



```maxima
(%i1) c : %pi/3 - a - b$
(%i2) bc : sin(a)*sin(3*c)/sin(a+b);

                                          %pi
                  sin(a) sin(3 (- b - a + ---))
                                           3
(%o2)             -----------------------------
                           sin(b + a)

(%i3) ba : bc, c=a, a=c;

                                         %pi
                    sin(3 a) sin(b + a - ---)
                                          3
(%o3)               -------------------------
                                  %pi
                          sin(a - ---)
                                   3

(%i4) ac2 : ba^2 + bc^2 - 2*bc*ba*cos(b);

         2         2         %pi
      sin (3 a) sin (b + a - ---)
                              3
(%o4) ---------------------------
                2     %pi
             sin (a - ---)
                       3
                                       %pi
 - (2 sin(a) sin(3 a) sin(3 (- b - a + ---)) cos(b)
                                        3
             %pi            %pi
 sin(b + a - ---))/(sin(a - ---) sin(b + a))
              3              3
      2       2              %pi
   sin (a) sin (3 (- b - a + ---))
                              3
 + -------------------------------
                2
             sin (b + a)

(%i5) trigrat (ac2);

(%o5) - (sqrt(3) sin(4 b + 4 a) - cos(4 b + 4 a)
 - 2 sqrt(3) sin(4 b + 2 a) + 2 cos(4 b + 2 a)
 - 2 sqrt(3) sin(2 b + 4 a) + 2 cos(2 b + 4 a)
 + 4 sqrt(3) sin(2 b + 2 a) - 8 cos(2 b + 2 a) - 4 cos(2 b - 2 a)
 + sqrt(3) sin(4 b) - cos(4 b) - 2 sqrt(3) sin(2 b) + 10 cos(2 b)
 + sqrt(3) sin(4 a) - cos(4 a) - 2 sqrt(3) sin(2 a) + 10 cos(2 a)
 - 9)/4
```

<!-- category: SpecialFunctions -->
<!-- keywords: trigreduce -->
<!-- signatures: trigreduce(expr, x), trigreduce(expr) -->
### Function: trigreduce (expr, x)

Produkte und Potenzen von Winkelfunktionen und den Hyperbelfunktionen mit dem
Argument *x* werden zu Funktionen vereinfacht, die Vielfache von *x*
enthalten.  `trigreduce` versucht auch, Sinus- und Kosinusfunktionen in
einem Nenner zu eliminieren.  Wird keine Variable *x* angegeben, werden alle
Variablen im Ausdruck `expr` betrachtet.


Siehe auch `poissimp`.



```maxima
(%i1) trigreduce(-sin(x)^2+3*cos(x)^2+x);
               cos(2 x)      cos(2 x)   1        1
(%o1)          -------- + 3 (-------- + -) + x - -
                  2             2       2        2
```

See also: `poissimp`.

<!-- category: SpecialFunctions -->
<!-- keywords: trigsign -->
<!-- signatures: trigsign -->
### Variable: trigsign

Standardwert: `true`


Hat `trigsign` den Wert `true`, werden Winkelfunktionen mit einem
negativem Argument vereinfacht.  Zum Beispiel vereinfacht in diesem Fall
`sin(-x)` zu `-sin(x)`.

<!-- category: SpecialFunctions -->
<!-- keywords: trigsimp -->
<!-- signatures: trigsimp(expr) -->
### Function: trigsimp (expr)

Wendet die Identitaten
`sin(x)^2 + cos(x)^2 = 1`
und
`cosh(x)^2 - sinh(x)^2 = 1`
an, um Ausdrucke, die Funktionen wie `tan`, `sec`, usw. enthalten, 
zu Ausdrucken mit den Funktionen `sin`, `cos`, `sinh`, 
`cosh` zu vereinfachen.


Die Anwendung von Funktionen wie `trigreduce`, `ratsimp` und
`radcan` kann den Ausdruck weiter vereinfachen.


Das Kommando `demo(trgsmp)` zeigt einige Beispiele.

See also: `trigreduce`, `ratsimp`, `radcan`.

