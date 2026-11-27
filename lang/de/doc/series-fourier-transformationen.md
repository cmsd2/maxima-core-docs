## Fourier-Transformationen

<!-- category: Series -->
<!-- keywords: absint -->
<!-- signatures: absint(f, x, halfplane), absint(f, x), absint(f, x, a, b) -->
### Function: absint (f, x, halfplane)

`absint(f, x, halfplane)` gibt das unbestimmte Integral
der Funktion *f* fur die Variable *x* zuruck.  Das Integral wird in
der angegebenen Halbebene `pos`, `neg` oder fur beide Halbebenen
mit `both` berechnet.  Der Integrand kann die Betragsfunktion enthalten:
`abs(x)`, `abs(sin(x))`, `abs(a) * exp(-abs(b) * abs(x))`.





`absint(f, x)` ist aquivalent zu
`absint(f, x, pos)`.







`absint(f, x, a, b)` gibt das bestimmte Integral
der Funktion *f* fur die Variable *x* in den Grenzen *a* und
*b* zuruck.  Der Integrand kann die Betragsfunktion enthalten.

<!-- category: Series -->
<!-- keywords: cosnpiflag -->
<!-- signatures: cosnpiflag -->
### Variable: cosnpiflag

Standardwert: `true`


Kontrolliert die Vereinfachung der Kosinus-Funktion durch die Funktion
`foursimp`.  Siehe die Funktion `foursimp`.

See also: `foursimp`.

<!-- category: Series -->
<!-- keywords: equalp -->
<!-- signatures: equalp(x, y) -->
### Function: equalp (x, y)

Gibt `true` zuruck, wenn `equal(x, y)` das Ergebnis
`true` hat.  Ansonsten ist das Ergebnis `false`.

<!-- category: Series -->
<!-- keywords: fft -->
<!-- signatures: fft(x) -->
### Function: fft (x)

Berechnet die schnelle Fourier-Transformation.  Das Argument *x* ist eine
Liste oder ein Array mit den Daten, die zu transformieren sind.  Die Anzahl der
Elemente muss eine Potenz von 2 sein.  Die Elemente mussen Zahlen (ganze,
rationale, Gleitkommazahlen oder große Gleitkommazahlen) oder numerische
Konstanten sein.  Weiterhin konnen die Elemente komplexe Zahlen
`a + b*%i` sein, wobei der Realteil und der Imaginarteil wiederum Zahlen
oder numerische Konstanten sein mussen.






`inverse_fft` gibt ein neues Objekt vom selben Typ wie *x* zuruck.
Die Ergebnisse sind immer Gleitkommazahlen oder komplexe Zahlen
`a + %i*b`, wobei `a` und `b` Gleitkommazahlen sind.









Die diskrete Fourier-Transformation ist wie folgt definiert.  Wenn `y` das
Ergebnis der Fourier-Transformation ist, dann gilt fur `k` von 0 bis
`n-1`



```maxima
y[k] = (1/n) sum(x[j] exp(-2 %i %pi j k / n), j, 0, n - 1)
```


$$
y_{k}={{1}\over{n}}
        \sum_{j=0}^{n-1}{x_{j}\,e^ {- {{2\,i\,\pi\,j\,k}\over{n}} }}
$$





Sind die Daten *x* reelle Zahlen, dann werden die reellen Koeffizienten
*a* und *b* so berechnet, dass gilt



```maxima
x[j] = sum (a[k] * cos (2*%pi*j*k / n) 
          + b[k] * sin (2*%pi*j*k / n), k, 0, n/2)
```


$$
x_{j}=\sum_{k=0}^{{{n}\over{2}}}{\left(b_{k}\,\sin \left({{2\,\pi\,
 j\,k}\over{n}}\right)+a_{k}\,\cos \left({{2\,\pi\,j\,k}\over{n}}
 \right)\right)}
$$


wobei



```maxima
a[0] = realpart (y[0])
b[0] = 0
```


$$
a_{0}={\it realpart}\left(y_{0}\right)$$
$$b_{0}=0
$$




und fur *k* von 1 bis `n/2-1`



```maxima
a[k] = realpart (y[k] + y[n - k])
b[k] = imagpart (y[n - k] - y[k])
```


$$
a_{k}={\it realpart}\left(y_{n-k}+y_{k}\right)$$
$$b_{k}={\it imagpart}\left(y_{n-k}-y_{k}\right)
$$


sowie



```maxima
a[n/2] = realpart (y[n/2])
b[n/2] = 0
```


$$
a_{{{n}\over{2}}}={\it realpart}\left(y_{{{n}\over{2}}}\right)$$
$$b_{{{n}\over{2}}}=0
$$






Das Kommando `load("fft")` ladt die Funktion.
Siehe auch `inverse_fft` fur die inverse schnelle Fourier-Transformation.


Beispiele:


Reelle Daten.



```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $
(%i4) L1 : fft (L);
(%o4) [0.0, - 1.811 %i - .1036, 0.0, .6036 - .3107 %i, 0.0, 
                         .3107 %i + .6036, 0.0, 1.811 %i - .1036]
(%i5) L2 : inverse_fft (L1);
(%o5) [1.0, 2.168L-19 %i + 2.0, 7.525L-20 %i + 3.0, 
4.256L-19 %i + 4.0, - 1.0, - 2.168L-19 %i - 2.0, 
- 7.525L-20 %i - 3.0, - 4.256L-19 %i - 4.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       3.545L-16
```


Komplexe Daten.



```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : fft (L);

(%o4) [0.5, .3536 %i + .3536, - 0.25 %i - 0.25, 
0.5 - 6.776L-21 %i, 0.0, - .3536 %i - .3536, 0.25 %i - 0.25, 
0.5 - 3.388L-20 %i]

(%i5) L2 : inverse_fft (L1);
(%o5) [1.0 - 4.066E-20 %i, 1.0 %i + 1.0, 1.0 - 1.0 %i, 
- 1.008L-19 %i - 1.0, 4.066E-20 %i - 1.0, 1.0 - 1.0 %i, 
1.0 %i + 1.0, 1.947L-20 %i + 1.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       6.83L-17
```




Berechnung der Sinus- und Kosinus-Koeffizienten.



```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, 5, 6, 7, 8] $
(%i4) n : length (L) $
(%i5) x : make_array (any, n) $
(%i6) fillarray (x, L) $
(%i7) y : fft (x) $
(%i8) a : make_array (any, n/2 + 1) $
(%i9) b : make_array (any, n/2 + 1) $
(%i10) a[0] : realpart (y[0]) $
(%i11) b[0] : 0 $
(%i12) for k : 1 thru n/2 - 1 do
   (a[k] : realpart (y[k] + y[n - k]),
    b[k] : imagpart (y[n - k] - y[k]));
(%o12)                        done
(%i13) a[n/2] : y[n/2] $
(%i14) b[n/2] : 0 $
(%i15) listarray (a);
(%o15)          [4.5, - 1.0, - 1.0, - 1.0, - 0.5]
(%i16) listarray (b);
(%o16)           [0, - 2.414, - 1.0, - .4142, 0]
(%i17) f(j) := sum (a[k] * cos (2*%pi*j*k / n) + b[k] 
                         * sin (2*%pi*j*k / n), k, 0, n/2) $
(%i18) makelist (float (f (j)), j, 0, n - 1);
(%o18)      [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
```

See also: `inverse_fft`.

<!-- category: Series -->
<!-- keywords: find_root, find_root_error, find_root_abs, find_root_rel -->
<!-- signatures: find_root(expr, x, a, b), find_root(f, a, b), find_root_error, find_root_abs, find_root_rel -->
### Function: find_root (expr, x, a, b)

Findet die Nullstellen eines Ausdrucks *expr* oder einer Funktion *f*
in dem Intervall `[a, b]`.  Der Ausdruck *expr* kann eine
Gleichung sein.  In diesem Fall sucht die Funktion `find_root` die 
Nullstellen fur den Ausdruck `lhs(expr) - rhs(expr)`.







Kann Maxima den Ausdruck *expr* oder die Funktion *f* in dem Intervall
`[a, b]` fur alle Werte auswerten und ist der Ausdruck
*expr* oder die Funktion *f* in dem Intervall stetig, dann ist sicher,
dass `find_root` die Nullstelle oder zumindest eine Nullstelle findet,
wenn mehrere Nullstellen vorhanden sind.






`find_root` beginnt mit einer binaren Suche der Nullstelle.  Erscheint
die Funktion als glatt genug, wendet Maxima einen Algorithmus mit einer linearen
Interpolation fur die Suche der Nullstelle an.









Die Genauigkeit der Nullstellensuche wird von den Optionsvariablen
`find_root_abs` und `find_root_rel` kontrolliert.  `find_root`
endet, wenn die Auswertung der Funktion ein Ergebnis hat, das kleiner als
`find_root_abs` ist oder wenn aufeinander folgende Auswertungen
Ergebnisse *x_0* und *x_1* haben, die sich voneinander weniger als
`find_root_rel * max(abs(x_0), abs(x_1))` unterscheiden.  Der Standardwert
der Optionsvariablen `find_root_abs` und `find_root_rel` ist Null.











`find_root` erwartet, dass die Funktion an den Endpunkten des Intervalls
fur die Nullstellensuche ein unterschiedliches Vorzeichen hat.  Hat die
Funktion an den Endpunkten des Intervalls dasselbe Vorzeichen, wird das
Verhalten der Funktion `find_root` von der Optionsvariablen
`find_root_error` kontrolliert.  Hat `find_root_error` den Wert
`true`, wird eine Fehlermeldung ausgegeben.  Ansonsten wird von
`find_root` der Wert von `find_root_error` als Ergebnis
zuruckgegeben.  Der Standardwert von `find_root_error` ist `true`.






Kann die Funktion *f* bei der Nullstellensuche nicht zu einer Zahl
ausgewertet werden, gibt `find_root` ein teilweise ausgewertetes Ergebnis
zuruck.





Die Reihenfolge der Grenzen des Intervalls *a* und *b* wird ignoriert.
`find_root` sucht die Nullstellen immer in dem Intervall
`[min(a, b), max(a, b)]`.


Beispiele:



```maxima
(%i1) f(x) := sin(x) - x/2;
                                        x
(%o1)                  f(x) := sin(x) - -
                                        2
(%i2) find_root (sin(x) - x/2, x, 0.1, %pi);
(%o2)                   1.895494267033981
(%i3) find_root (sin(x) = x/2, x, 0.1, %pi);
(%o3)                   1.895494267033981
(%i4) find_root (f(x), x, 0.1, %pi);
(%o4)                   1.895494267033981
(%i5) find_root (f, 0.1, %pi);
(%o5)                   1.895494267033981
(%i6) find_root (exp(x) = y, x, 0, 100);
                            x
(%o6)           find_root(%e  = y, x, 0.0, 100.0)
(%i7) find_root (exp(x) = y, x, 0, 100), y = 10;
(%o7)                   2.302585092994046
(%i8) log (10.0);
(%o8)                   2.302585092994046
```

<!-- category: Series -->
<!-- keywords: fourcos -->
<!-- signatures: fourcos(f, x, p) -->
### Function: fourcos (f, x, p)

Gibt die Kosinus-Koeffizienten einer Fourierreihe fur die Funktion
`f(x)` zuruck, die auf dem Intervall `[0, p]`
definiert ist.

<!-- category: Series -->
<!-- keywords: fourexpand -->
<!-- signatures: fourexpand(l, x, p, limit) -->
### Function: fourexpand (l, x, p, limit)

Konstruiert aus der Liste der Fourier-Koeffizienten *l* eine Fourierreihe
mit *limit* Termen.  Das Argument *limit* kann `inf` sein.  Die
Argumente *x* und *p* haben dieselbe Bedeutung wie fur die Funktion
`fourier`.


Siehe die Funktion `fourier` fur ein Beispiel.

See also: `fourier`.

<!-- category: Series -->
<!-- keywords: fourier -->
<!-- signatures: fourier(f, x, l) -->
### Function: fourier (f, x, l)

Berechnet die Fourier-Koeffizienten `a[0]`, `a[n]` und `b[n]`
der Funktion `f(x)` fur das Intervall `[-l, l]`.  Die
Fourierreihe ist definiert als:



```maxima
inf
         ====
         \             %pi n x           %pi n x
  f(x) =  >    (b  sin(-------) + a  cos(-------))
         /       n        l        n        l
         ====
         n = 0
```


Die Koeffizienten der Fourierreihe werden folgendermaßen berechnet:



```maxima
l
                    /
                - 1 [
      a  = 1/2 l    I    f(x) dx
       0            ]
                    /
                     - l
```



```maxima
l
                /
            - 1 [                  - 1
      a  = l    I    f(x) cos(%pi l    n x) dx
       n        ]
                /
                 - l
```



```maxima
l
                 /
            - 1 [                  - 1
      b  = l    I    f(x) sin(%pi l    n x) dx
       n        ]
                /
                 - l
```


`fourier` weist die Fourier-Koeffizienten Zwischenmarken zu.  Die
Zwischenmarken werden als eine Liste zuruckgegeben.


Der Index der Summe ist immer das Symbol *n*.  Sinus- und Kosinusfunktionen
mit ganzzahligen Vielfachen von `%pi` werden nicht automatisch vereinfacht.
Dies kann mit der Funktion `foursimp` erreicht werden, der als Argument
die Liste der Fourier-Koeffizienten ubergeben wird.


Mit der Funktion `fourexpand` kann die Fourierreihe aus den
Fourier-Koeffizienten konstruiert werden.  Siehe auch die Funktion
`totalfourier`.


Mit den Funktionen `fourcos` und `foursin` werden jeweils die
Koeffizienten der Kosinus- und Sinus-Entwicklung berechnet.


Beispiel:



```maxima
(%i1) load("fourie")$

(%i2) fourier(x, x, 1);
(%t2)                        a  = 0
                              0

(%t3)                        a  = 0
                              n

                        sin(%pi n)   cos(%pi n)
(%t4)           b  = 2 (---------- - ----------)
                 n          2  2       %pi n
                         %pi  n

(%o4)                    [%t2, %t3, %t4]
(%i5) foursimp(%);
(%t5)                        a  = 0
                              0

(%t6)                        a  = 0
                              n

                                       n
                                2 (- 1)
(%t7)                    b  = - --------
                          n      %pi n

(%o7)                    [%t5, %t6, %t7]
(%i8) fourexpand(%, x, 1, inf);
                      inf
                      ====       n
                      \     (- 1)  sin(%pi n x)
                    2  >    -------------------
                      /              n
                      ====
                      n = 1
(%o8)             - ---------------------------
                                %pi
```

See also: `foursimp`, `fourexpand`, `totalfourier`, `fourcos`, `foursin`.

<!-- category: Series -->
<!-- keywords: fourint -->
<!-- signatures: fourint(f, x) -->
### Function: fourint (f, x)

Konstruiert eine Liste der Fourierintegral-Koeffizienten der Funktion
`f(x)`, die auf dem Intervall `[minf, inf]` definiert ist.

<!-- category: Series -->
<!-- keywords: fourintcos -->
<!-- signatures: fourintcos(f, x) -->
### Function: fourintcos (f, x)

Gibt die Koeffizienten des Kosinus-Fourierintegrals der Funktion
`f(x)` zuruck, die auf dem Intervall `[0, inf]`
definiert ist.

<!-- category: Series -->
<!-- keywords: fourintsin -->
<!-- signatures: fourintsin(f, x) -->
### Function: fourintsin (f, x)

Gibt die Koeffizienten des Sinus-Fourierintegrals der Funktion
`f(x)` zuruck, die auf dem Intervall `[0, inf]`
definiert ist.

<!-- category: Series -->
<!-- keywords: foursimp -->
<!-- signatures: foursimp(l) -->
### Function: foursimp (l)

`foursimp` wird auf das Ergebnis der Funktion `fourier` angewendet,
um Sinus- und Kosinus-Funktionen zu vereinfachen, die ganzzahlige Vielfache
von `%pi` enthalten.  Das Argument *l* ist eine Liste mit den
Koeffizienten der Fourierreihe, fur die die Vereinfachung ausgefuhrt werden
soll.


`sin(n %pi)` wird zu `0` vereinfacht, wenn die Optionsvariable
`sinnpiflag` den Wert `true` hat, und `cos(n %pi)` wird zu
`(-1)^n`, wenn die Optionsvariable `cosnpiflag` den Wert `true`
hat.


Siehe die Funktion `fourier` fur ein Beispiel.

See also: `fourier`, `sinnpiflag`, `cosnpiflag`.

<!-- category: Series -->
<!-- keywords: foursin -->
<!-- signatures: foursin(f, x, p) -->
### Function: foursin (f, x, p)

Gibt die Sinus-Koeffizienten einer Fourierreihe fur die Funktion
`f(x)` zuruck, die auf dem Intervall `[0, p]`
definiert ist.

<!-- category: Series -->
<!-- keywords: funp -->
<!-- signatures: funp(f, expr), funp(f, expr, x) -->
### Function: funp (f, expr)

`funp(f, expr)` hat das Ergebnis `true`, wenn der
Ausdruck *expr* die Funktion *f* enthalt.






`funp(f, expr, x)` hat das Ergebnis `true`, wenn
der Ausdruck *expr* die Funktion *f* enthält und die Variable *x*
ein Argument der Funktion *f* ist.

<!-- category: Series -->
<!-- keywords: horner -->
<!-- signatures: horner(expr, x), horner(expr) -->
### Function: horner (expr, x)

Formt ein Polynom *expr* in das Horner-Schema um.  Mit *x* wird die
Variable angegeben, fur die das Horner-Schema zu bilden ist.  Wird das
Argument *x* nicht angegeben, wird die Hauptvariable des kanonischen
Ausdrucks *expr* fur die Bildung des Horner-Schemas genutzt.






Das Horner-Schema kann die Stabilitat der numerischen Berechnung eines
Ausdrucks verbessern.


Beispiel:



```maxima
(%i1) expr: 1e-155*x^2 - 5.5*x + 5.2e155;
                           2
(%o1)            1.0E-155 x  - 5.5 x + 5.2E+155
(%i2) expr2: horner (%, x), keepfloat: true;
(%o2)            (1.0E-155 x - 5.5) x + 5.2E+155
(%i3) ev (expr, x=1e155);
Maxima encountered a Lisp error:

 floating point overflow

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
(%i4) ev (expr2, x=1e155);
(%o4)                       7.0E+154
```

<!-- category: Series -->
<!-- keywords: inverse_fft -->
<!-- signatures: inverse_fft(y) -->
### Function: inverse_fft (y)

Berechnet die inverse schnelle Fourier-Transformation.  Das Argument *y* ist
eine Liste oder ein Array mit den Daten, die zu transformieren sind.  Die Anzahl
der Daten muss eine Potenz von 2 sein.  Die Elemente mussen Zahlen (ganze,
rationale, Gleitkommazahlen oder große Gleitkommazahlen) oder numerische
Konstanten sein.  Weiterhin konnen die Elemente komplexe Zahlen
`a + b*%i` sein, wobei der Realteil und der Imaginarteil wiederum Zahlen
oder numerische Konstanten sein mussen.






`inverse_fft` gibt ein neues Objekt vom selben Typ wie *y* zuruck.
Die Ergebnisse sind immer Gleitkommazahlen oder komplexe Zahlen
`a + %i*b`, wobei `a` und `b` Gleitkommazahlen sind.









Die inverse diskrete Fourier-Transformation ist wie folgt definiert.  Wenn
`x` das Ergebnis der inversen Fourier-Transformation ist, dann gilt fur
`j` von 0 bis `n-1`



```maxima
x[j] = sum(y[k] exp(2 %i %pi j k / n), k, 0, n - 1)
```


$$
x_{j}=\sum_{k=0}^{n-1}{y_{k}\,e^{{{2\,i\,\pi\,j\,k}\over{n}}}}
$$






Mit dem Kommando `load("fft")` wird die Funktion geladen.  Siehe auch 
`fft` fur die schnelle Fourier-Transformation.


Beispiele:




Reelle Daten.



```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $
(%i3) L : [1, 2, 3, 4, -1, -2, -3, -4] $
(%i4) L1 : inverse_fft (L);
(%o4) [0.0, 14.49 %i - .8284, 0.0, 2.485 %i + 4.828, 0.0, 
                       4.828 - 2.485 %i, 0.0, - 14.49 %i - .8284]
(%i5) L2 : fft (L1);
(%o5) [1.0, 2.0 - 2.168L-19 %i, 3.0 - 7.525L-20 %i, 
4.0 - 4.256L-19 %i, - 1.0, 2.168L-19 %i - 2.0, 
7.525L-20 %i - 3.0, 4.256L-19 %i - 4.0]
(%i6) lmax (abs (L2 - L));
(%o6)                       3.545L-16
```




Komplexe Daten.



```maxima
(%i1) load ("fft") $
(%i2) fpprintprec : 4 $                 
(%i3) L : [1, 1 + %i, 1 - %i, -1, -1, 1 - %i, 1 + %i, 1] $
(%i4) L1 : inverse_fft (L);
(%o4) [4.0, 2.711L-19 %i + 4.0, 2.0 %i - 2.0, 
- 2.828 %i - 2.828, 0.0, 5.421L-20 %i + 4.0, - 2.0 %i - 2.0, 
2.828 %i + 2.828]
(%i5) L2 : fft (L1);
(%o5) [4.066E-20 %i + 1.0, 1.0 %i + 1.0, 1.0 - 1.0 %i, 
1.55L-19 %i - 1.0, - 4.066E-20 %i - 1.0, 1.0 - 1.0 %i, 
1.0 %i + 1.0, 1.0 - 7.368L-20 %i]
(%i6) lmax (abs (L2 - L));                    
(%o6)                       6.841L-17
```

See also: `fft`.

<!-- category: Series -->
<!-- keywords: polartorect -->
<!-- signatures: polartorect(r, t) -->
### Function: polartorect (r, t)

Transformiert komplexe Zahlen der Form `r %e^(%i t)` in die Standardform
`a + b %i`.  *r* ist der Betrag der komplexen Zahl und *t* die
Phase.  Die Argumente *r* und *t* sind eindimensionale Arrays derselben
Große.  Die Große der Arrays muss eine Potenz von 2 sein.










Die Werte der originalen Arrays werden durch den Realteil `a = r cos(t)`
und den Imaginarteil `b = r sin(t)` ersetzt.





`polartorect` ist die inverse Funktion zu `recttopolar`.
Das Kommando `load("fft")` ladt die Funktion.

See also: `recttopolar`.

<!-- category: Series -->
<!-- keywords: recttopolar -->
<!-- signatures: recttopolar(a, b) -->
### Function: recttopolar (a, b)

Transformiert komplexe Zahlen der Form `a + b %i` in die Polarform
`r %e^(%i t)`.  *a* ist der Realteil und *b* der Imaginarteil der
komplexen Zahl.  Die Argumente *a* und *b* sind eindimensionale Arrays
derselben Große.  Die Große der Arrays muss eine Potenz von 2 sein.










Die Werte der originalen Arrays werden durch den Betrag
`r = sqrt(a^2 + b^2` und die Phase `t = atan2(b, a)` ersetzt.  Die
Phase ist ein Winkel in dem Bereich `-%pi` bis `%pi`.





`recttoploar` ist die inverse Funktion zu `polartorect`.
Das Kommando `load("fft")` ladt die Funktion.

See also: `polartorect`.

<!-- category: Series -->
<!-- keywords: remfun -->
<!-- signatures: remfun(f, expr), remfun(f, expr, x) -->
### Function: remfun (f, expr)

`remfun(f, expr` ersetzt `f(arg)` durch
*arg* im Ausdruck *expr*.






`remfun(f, expr, x)` ersetzt `f (arg)`
durch *arg* im Ausdruck *expr* nur dann, wenn *arg* die Variable
*x* enthalt.

<!-- category: Series -->
<!-- keywords: sinnpiflag -->
<!-- signatures: sinnpiflag -->
### Variable: sinnpiflag

Standardwert: `true`


Kontrolliert die Vereinfachung der Sinus-Funktion durch die Funktion
`foursimp`.  Siehe die Funktion `foursimp`.

See also: `foursimp`.

<!-- category: Series -->
<!-- keywords: totalfourier -->
<!-- signatures: totalfourier(f, x, l) -->
### Function: totalfourier (f, x, l)

Gibt die Fourierreihe der Funktion *f(x)* fur das Intervall
`[-l, l]` zuruck.  Das Ergebnis wird berechnet, indem
die nacheinander die Funktionen `foursimp` und `fourexpand` auf das
Ergebnis der Funktion `fourier` angewendet werden.


Beispiel:



```maxima
(%i1) load("fourie")$

(%i2) totalfourier(x, x, 1);
(%t2)                        a  = 0
                              0

(%t3)                        a  = 0
                              n

                        sin(%pi n)   cos(%pi n)
(%t4)           b  = 2 (---------- - ----------)
                 n          2  2       %pi n
                         %pi  n

(%t5)                        a  = 0
                              0

(%t6)                        a  = 0
                              n

                                       n
                                2 (- 1)
(%t7)                    b  = - --------
                          n      %pi n


                      inf
                      ====       n
                      \     (- 1)  sin(%pi n x)
                    2  >    -------------------
                      /              n
                      ====
                      n = 1
(%o7)             - ---------------------------
                                %pi
```

See also: `foursimp`, `fourexpand`, `fourier`.

