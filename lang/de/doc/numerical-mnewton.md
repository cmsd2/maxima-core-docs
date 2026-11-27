## mnewton

<!-- category: Numerical -->
<!-- keywords: mnewton -->
<!-- signatures: mnewton(FuncList, VarList, GuessList) -->
### Function: mnewton (FuncList, VarList, GuessList)

Implementation des Newton-Verfahrens fur das numerische Losen von
Gleichungen in mehreren Variablen.  Das Argument *FuncList* ist die Liste
der Gleichungen, fur die eine numerische Losung gesucht wird.  Das Argument
*VarList* ist eine Liste der Variablen und das Argument *GuessList*
ist eine Liste mit den Startwerten des Newton-Verfahrens.





Die Losungen werden als eine Liste zuruckgegeben.  Kann keine Losung
gefunden werden, ist die Ruckgabe eine leere Liste `[]`.





`mnewton` wird von den Funktionen `newtonepsilon` und
`newtonmaxiter` kontrolliert.





Die Funktion wird mit dem Kommando `load("mnewton")` geladen.  Siehe die
Funktion `newton` fur eine alternative Implementierung des
Newton-Verfahrens.


Beispiele:



```maxima
(%i1) load("mnewton")$

(%i2) mnewton([x1+3*log(x1)-x2^2, 2*x1^2-x1*x2-5*x1+1],
              [x1, x2], [5, 5]);
(%o2) [[x1 = 3.756834008012769, x2 = 2.779849592817897]]
(%i3) mnewton([2*a^a-5],[a],[1]);
(%o3)             [[a = 1.70927556786144]]
(%i4) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o4) [[u = 1.066618389595407, v = 1.552564766841786]]
```






Die Optionsvariable `newtonepsilon` kontrolliert die Genauigkeit der
Approximation.  Weiterhin kontrolliert die Optionsvariable, ob die Berechnung
mit Gleitkommazahlen in doppelter oder großer Genauigkeit durchgefuhrt
wird.



```maxima
(%i1) load("mnewton")$

(%i2) (fpprec : 25, newtonepsilon : bfloat(10^(-fpprec+5)))$

(%i3) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o3) [[u = 1.066618389595406772591173b0, 
                               v = 1.552564766841786450100418b0]]
```

See also: `newtonepsilon`, `newtonmaxiter`, `newton`.

<!-- category: Numerical -->
<!-- keywords: newton -->
<!-- signatures: newton(expr, x, x_0, eps) -->
### Function: newton (expr, x, x_0, eps)

Die Funktion `newton` gibt eine Naherungslosung der Gleichung
`expr = 0` zuruck, die mit dem Newton-Verfahren berechnet wird.
Der Ausdruck *expr* ist eine Funktion einer Variablen *x*.  Der
Anfangswert ist `x = x_0`.  Der Algorithmus bricht ab, wenn
`abs(expr) < eps`, wobei der Ausdruck *expr* fur den
aktuellen Naherungswert *x* ausgewertet wird.







`newton` erlaubt symbolische Variablen im Ausdruck *expr*, wenn der
Ausdruck `abs(expr) < eps` zu `true` oder `false`
ausgewertet werden kann.  Daher ist es nicht notwendig, dass der Ausdruck
*expr* zu einer Zahl ausgewertet werden kann.




Das Kommando `load("newton1")` ladt die Funktion.





Siehe auch die Funktionen `realroots`, `allroots` und
`find_root`, um numerische Losungen von Gleichungen zu finden.
Das Paket mnewton enthalt mit der Funktion `mnewton` eine weitere
Implementation des Newton-Verfahrens.


Achtung: Auch mit `load("newton")` wird eine Funktion mit dem Namen
`newton` geladen, die sich jedoch in ihrer Syntax von der hier
beschriebenen Funktion unterscheidet und auch nicht dokumentiert ist.


Beispiele:



```maxima
(%i1) load ("newton1");
(%o1) /usr/share/maxima/5.10.0cvs/share/numeric/newton1.mac
(%i2) newton (cos (u), u, 1, 1/100);
(%o2)                   1.570675277161251
(%i3) ev (cos (u), u = %);
(%o3)                 1.2104963335033528E-4
(%i4) assume (a > 0);
(%o4)                        [a > 0]
(%i5) newton (x^2 - a^2, x, a/2, a^2/100);
(%o5)                  1.00030487804878 a
(%i6) ev (x^2 - a^2, x = %);
                                           2
(%o6)                6.098490481853958E-4 a
```

See also: `realroots`, `allroots`, `find_root`, `mnewton`.

<!-- category: Numerical -->
<!-- keywords: newtonepsilon -->
<!-- signatures: newtonepsilon -->
### Variable: newtonepsilon

Standardwert: `1.0e-8`





Genauigkeit mit der getestet wird, wie gut die Funktion `mnewton` sich der
Losung angenahert hat.  Unterschreitet die Anderung der Approximation
den Wert `newtonepsilon`, bricht der Algorithmus ab und gibt das Ergebnis
zuruck.

See also: `mnewton`.

<!-- category: Numerical -->
<!-- keywords: newtonmaxiter -->
<!-- signatures: newtonmaxiter -->
### Variable: newtonmaxiter

Standardwert: `50`





Obere Grenze fur die Anzahl an Iterationen, falls die Funktion
`mnewton` nicht oder sehr langsam konvergiert.

See also: `mnewton`.

