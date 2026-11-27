## Spezielle Funktionen

<!-- category: SpecialFunctions -->
<!-- keywords: airy_ai -->
<!-- signatures: airy_ai(z) -->
### Function: airy_ai (z)

Die Airy-Funktion $Ai(z)$ (A & S 10.4.2).


Die Airy-Funktion `airy_ai` ist fur das symbolische und numerische
Rechnen geeignet.  Ist das Argument `z` eine reelle oder komplexe
Gleitkommazahl, wird `airy_ai` numerisch berechnet.  Mit der
Optionsvariablen `numer` oder der Funktion `float` kann die
numerische Berechnung erzwungen werden, wenn das Argument eine ganze oder
rationale Zahl ist.  Die numerische Berechnung fur große Gleitkommazahlen
ist nicht implementiert.


Maxima kennt den speziellen Wert fur das Argument `0`.


Ist das Argument eine Liste, Matrix oder Gleichung wird die Funktion
`airy_ai` auf die Elemente der Liste oder beide Seiten der Gleichung
angewendet.  Siehe auch `distribute_over`.


Die Ableitung `diff(airy_ai(z), z)` ist als `airy_dai(z)`
implementiert.  Siehe die Funktion `airy_dai`.


Weiterhin kennt Maxima das Integral der Airy-Funktion `airy_ai`.


Siehe auch die Funktionen `airy_bi` und `airy_dbi`.


Beispiele:


Numerische Berechnung fur Gleitkommazahlen.  Fur ganze und rationale Zahlen
wird eine Substantivform zuruckgegeben.  Maxima kennt den speziellen Wert
fur das Argument `0`.



```maxima
(%i1) airy_ai([0.5, 1.0+%i]);
(%o1) [.2316936064808335, .06045830837183824
                                          - .1518895658771814 %i]
(%i2) airy_ai([1, 1/2]);

                                         1
(%o2)               [airy_ai(1), airy_ai(-)]
                                         2

(%i3) airy_ai(0);
                                1
(%o3)                     -------------
                           2/3       2
                          3    gamma(-)
                                     3
```


Ableitungen und Integral der Airy-Funktion `airy_ai`.



```maxima
(%i4) diff(airy_ai(z), z);
(%o4)                      airy_dai(z)
(%i5) diff(airy_ai(z), z, 2);
(%o5)                     z airy_ai(z)
(%i6) diff(airy_ai(z), z, 3);
(%o6)              z airy_dai(z) + airy_ai(z)
(%i7) integrate(airy_ai(z), z);
                                   3
                      1    2  4   z
      hypergeometric([-], [-, -], --) z
                      3    3  3   9
(%o7) ---------------------------------
                 2/3       2
                3    gamma(-)
                           3
                                                            3
                  1/6       2                  2    4  5   z    2
                 3    gamma(-) hypergeometric([-], [-, -], --) z
                            3                  3    3  3   9
               - ------------------------------------------------
                                      4 %pi
```

See also: `numer`, `float`, `distribute_over`, `airy_dai`, `airy_bi`, `airy_dbi`.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_bi -->
<!-- signatures: airy_bi(z) -->
### Function: airy_bi (z)

Die Airy-Funktion Bi(z) (A & S 10.4.3).


Die Airy-Funktion `airy_bi` ist fur das symbolische und numerische
Rechnen geeignet.  Ist das Argument `z` eine reelle oder komplexe
Gleitkommazahl, wird `airy_bi` numerisch berechnet.  Mit der
Optionsvariablen `numer` oder der Funktion `float` kann die
numerische Berechnung erzwungen werden, wenn das Argument eine ganze oder
rationale Zahl ist.  Die numerische Berechnung fur große Gleitkommazahlen
ist nicht implementiert.


Maxima kennt den speziellen Wert fur das Argument `0`.


Ist das Argument eine Liste, Matrix oder Gleichung wird die Funktion
`airy_bi` auf die Elemente der Liste oder beide Seiten der Gleichung
angewendet.  Siehe auch `distribute_over`.


Die Ableitung `diff(airy_bi(z), z)` ist als `airy_dbi(z)`
implementiert.  Siehe die Funktion `airy_dbi`.


Weiterhin kennt Maxima das Integral der Airy-Funktion `airy_bi`.


Siehe auch die Funktionen `airy_ai` und `airy_dai`.


Fur Beispiele siehe die Funktion `airy_ai`.

See also: `numer`, `float`, `distribute_over`, `airy_dbi`, `airy_ai`, `airy_dai`.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_dai -->
<!-- signatures: airy_dai(z) -->
### Function: airy_dai (z)

Die Ableitung der Airy-Funktion `airy_ai`.


Die Ableitung der Airy-Funktion `airy_dai` ist fur das symbolische und
numerische Rechnen geeignet.  Ist das Argument *z* eine reelle oder
komplexe Gleitkommazahl, wird `airy_dai` numerisch berechnet.  Mit der
Optionsvariablen `numer` oder der Funktion `float` kann die
numerische Berechnung erzwungen werden, wenn das Argument eine ganze oder
rationale Zahl ist.  Die numerische Berechnung fur große Gleitkommazahlen
ist nicht implementiert.


Maxima kennt den speziellen Wert fur das Argument `0`.


Ist das Argument eine Liste, Matrix oder Gleichung wird die Funktion
`airy_dai` auf die Elemente der Liste oder beide Seiten der Gleichung
angewendet.  Siehe auch `distribute_over`.


Maxima kennt die Ableitung und das Integral der Funktion `airy_dai`.


Siehe auch die Airy-Funktionen `airy_bi` und `airy_dbi`.


Fur Beispiele siehe die Funktion `airy_ai`.

See also: `airy_ai`, `numer`, `float`, `distribute_over`, `airy_bi`, `airy_dbi`.

<!-- category: SpecialFunctions -->
<!-- keywords: airy_dbi -->
<!-- signatures: airy_dbi(z) -->
### Function: airy_dbi (z)

Die Ableitung der Airy-Funktion `airy_bi`.


Die Ableitung der Airy-Funktion `airy_dbi` ist fur das symbolische und
numerische Rechnen geeignet.  Ist das Argument *z* eine reelle oder
komplexe Gleitkommazahl, wird `airy_dbi` numerisch berechnet.  Mit der
Optionsvariablen `numer` oder der Funktion `float` kann die
numerische Berechnung erzwungen werden, wenn das Argument eine ganze oder
rationale Zahl ist.  Die numerische Berechnung fur große Gleitkommazahlen
ist nicht implementiert.


Maxima kennt den speziellen Wert fur das Argument `0`.


Ist das Argument eine Liste, Matrix oder Gleichung wird die Funktion
`airy_dbi` auf die Elemente der Liste oder beide Seiten der Gleichung
angewendet.  Siehe auch `distribute_over`.


Maxima kennt die Ableitung und das Integral der Funktion `airy_dbi`.


Siehe auch die Airy-Funktionen `airy_ai` und `airy_dai`.


Fur Beispiele siehe die Funktion `airy_ai`.

See also: `airy_bi`, `numer`, `float`, `distribute_over`, `airy_ai`, `airy_dai`.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_i -->
<!-- signatures: bessel_i(v, z) -->
### Function: bessel_i (v, z)

Die modifizierte Bessel-Funktion der ersten Art der Ordnung $v$ mit dem 
Argument $v$.  `bessel_i` ist definiert als



```maxima
inf
               ====
               \              1            z 2 k + v
      I (z) =   >    -------------------  (-)
       v       /     k! gamma(v + k + 1)   2
               ====
               k = 0
```


$$
I_{v}(z)=\sum_{k=0}^{\infty }{{{1}\over{k!\,\Gamma\left(v+k+1
 \right)}}}\,\left({{z}\over{2}}\right)^{2\,k+v}
$$


Die Reihenentwicklung wird nicht fur die numerische Berechnung genutzt.


Die Bessel-Funktion `bessel_i` ist fur das numerische und symbolische
Rechnen geeignet.


Maxima berechnet `bessel_i` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente ganze oder rationale Zahlen
sind.  Die numerische Berechnung fur große Gleitkommazahlen ist nicht
implementiert.  In diesem Fall gibt Maxima eine Substantivform zuruck.


`bessel_i` hat die folgenden Eigenschaften, die mit mit der Funktion
`properties` angezeigt werden und auf das symbolische Rechnen Einfluss
haben:



**conjugate function** — `bessel_i` hat Spiegelsymmetrie, wenn das Argument *z* keine negative
reelle Zahl ist.  Die Spiegelsymmetrie wird zum Beispiel von der Funktion
`conjugate` fur die Vereinfachung eines Ausdrucks genutzt.
**complex characteristic** — Maxima kennt den Realteil und den Imaginarteil von `bessel_i` fur
spezielle Argumente $v$ und $z$.
**limit function** — Maxima kennt spezielle Grenzwerte der Funktion `bessel_i`.
**integral** — Maxima kennt das Integral der Funktion `bessel_i` fur die
Integrationsvariable $z$.
**gradef** — Maxima kennt die Ableitungen der Funktion `bessel_i` nach den
Argumenten $v$ und $z$.


Die Vereinfachung der Bessel-Funktion `bessel_i` wird von den folgenden
Optionsvariablen kontrolliert:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und sind
die Argumente von `bessel_i` eine Matrix, Liste oder Gleichung wird die
Funktion auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der
Standardwert ist `true`.
**besselexpand** — Hat die Optionsvariable `besselexpand` den Wert `true`, wird
`bessel_i` mit einer halbzahligen Ordnung $v$ als Hyperbelfunktionen
entwickelt.
**bessel_reduce** — Hat die Optionsvariable `bessel_reduce` den Wert `true`, wird
`bessel_i` mit einer ganzzahligen Ordnung $n$ nach Bessel-Funktionen
`bessel_i` mit der niedrigsten Ordnung `0` und `1` entwickelt.
**hypergeometric_representation** — Hat die Optionsvariable `hypergeometric_representation` den Wert
`true`, dann wird `bessel_i` als hypergeometrische Funktion
dargestellt.


Weiterhin kennt Maxima die geraden und ungeraden Symmetrieeigenschaften von
`bessel_i`.  Fur eine ganze Zahl $n$ vereinfacht daher
`bessel_i(-n, z)` zu `bessel_i(n, z)`.


Siehe auch die anderen Bessel-Funktionen `bessel_j`,
`bessel_y` und `bessel_k` sowie die weiteren mit den Bessel-Funktionen
verwandten Funktionen wie die Hankel-Funktionen in `Hankel-Funktionen`,
Airy-Funktionen in `Airy-Funktionen` und Struve-Funktionen in
`Struve-Funktionen`.


Siehe die Funktion `bessel_j` fur Beispiele mit Bessel-Funktionen.

See also: `float`, `numer`, `properties`, `conjugate`, `distribute_over`, `besselexpand`, `bessel_reduce`, `hypergeometric_representation`, `bessel_j`, `bessel_y`, `bessel_k`, `Hankel-Funktionen`, `Airy-Funktionen`, `Struve-Funktionen`.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_j -->
<!-- signatures: bessel_j(v, z) -->
### Function: bessel_j (v, z)

Die Bessel-Funktion der ersten Art der Ordnung $v$ mit dem Argument
$z$.  `bessel_j` ist definiert als



```maxima
inf
               ====             k
               \           (- 1)           z 2 k + v
      J (z) =   >    -------------------  (-)
       v       /     k! gamma(v + k + 1)   2
               ====
               k = 0
```


$$
J_{v}(z)=\sum_{k=0}^{\infty }{{{\left(-1\right)^{k}}\over{k!
 \,\Gamma\left(v+k+1\right)}}}\,\left({{z}\over{2}}\right)^{2
 \,k+v}
$$


Die Reihenentwicklung wird nicht fur die numerische Berechnung genutzt.


Die Bessel-Funktion `bessel_j` ist fur das numerische und symbolische
Rechnen geeignet.


Maxima berechnet `bessel_j` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente ganze oder rationale Zahlen
sind.  Die numerische Berechnung fur große Gleitkommazahlen ist nicht
implementiert.  In diesem Fall gibt Maxima eine Substantivform zuruck.


`bessel_j` hat die folgenden Eigenschaften, die mit mit der Funktion
`properties` angezeigt werden und auf das symbolische Rechnen Einfluss
haben:



**conjugate function** — `bessel_j` hat Spiegelsymmetrie, wenn das Argument *z* keine negative
reelle Zahl ist.  Die Spiegelsymmetrie wird zum Beispiel von der Funktion
`conjugate` fur die Vereinfachung eines Ausdrucks genutzt.
**complex characteristic** — Maxima kennt den Realteil und den Imaginarteil von `bessel_j` fur
spezielle Argumente $v$ und $z$.
**limit function** — Maxima kennt spezielle Grenzwerte der Funktion `bessel_j`.
**integral** — Maxima kennt das Integral der Funktion `bessel_j` fur die
Integrationsvariable $z$.
**gradef** — Maxima kennt die Ableitungen der Funktion `bessel_j` nach den
Argumenten $v$ und $z$.


Die Vereinfachung der Bessel-Funktion `bessel_j` wird von den folgenden
Optionsvariablen kontrolliert:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und sind
die Argumente von `bessel_j` eine Matrix, Liste oder Gleichung wird die
Funktion auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der
Standardwert ist `true`.
**besselexpand** — Hat die Optionsvariable `besselexpand` den Wert `true`, wird
`bessel_j` mit einer halbzahligen Ordnung $v$ als Sinus- und
Kosinusfunktionen entwickelt.
**bessel_reduce** — Hat die Optionsvariable `bessel_reduce` den Wert `true`, wird
`bessel_j` mit einer ganzzahligen Ordnung $n$ nach Bessel-Funktionen
`bessel_j` mit der niedrigsten Ordnung `0` und `1` entwickelt.
**hypergeometric_representation** — Hat die Optionsvariable `hypergeometric_representation` den Wert
`true`, dann wird `bessel_j` als hypergeometrische Funktion
dargestellt.


Weiterhin kennt Maxima die geraden und ungeraden Symmetrieeigenschaften von
`bessel_j`.  Fur eine ganze Zahl $n$ vereinfacht daher
`bessel_j(-n, z)` zu `(-1)^n bessel_j(n, z)`.


Maxima kennt noch die Funktion `spherical_bessel_j`, die im Paket
`orthopoly` definiert ist.   Siehe auch die anderen Bessel-Funktionen
`bessel_y`, `bessel_i` und `bessel_k` sowie die
weiteren mit den Bessel-Funktionen verwandten Funktionen wie die
Hankel-Funktionen in `Hankel-Funktionen`, Airy-Funktionen in
`Airy-Funktionen` und Struve-Funktionen in `Struve-Funktionen`.


Beispiele:


Numerisches Rechnen mit der Bessel-Funktion.  Fur große Gleitkommazahlen
ist die numerische Berechnung nicht implementiert.



```maxima
(%i1) bessel_j(1,[0.5, 0.5+%i]);
(%o1) [.2422684576748739, .5124137767280905 %i
                                             + .3392601907198862]
(%i2) bessel_j(1,[0.5b0, 0.5b0+%i]);
(%o2)    [bessel_j(1, 5.0b-1), bessel_j(1, %i + 5.0b-1)]
```


Vereinfachungen der Bessel-Funktion mit den Optionsvariablen `besselexpand`
und `bessel_reduce`.



```maxima
(%i3) bessel_j(1/2,x), besselexpand:true;
                         sqrt(2) sin(x)
(%o3)                   -----------------
                        sqrt(%pi) sqrt(x)
(%i4) bessel_j(3,x), bessel_reduce:true;
         2 bessel_j(1, x)
      4 (---------------- - bessel_j(0, x))
                x
(%o4) ------------------------------------- - bessel_j(1, x)
                        x
```


Ableitungen und Integrale der Bessel-Funktion.  Das letzte Beispiel zeigt
die Laplace-Transformation der Bessel-Funktion mit der Funktion
`laplace`.



```maxima
(%i5) diff(bessel_j(2,x), x);

                 bessel_j(1, x) - bessel_j(3, x)
(%o5)            -------------------------------
                                2

(%i6) diff(bessel_j(v,x), x);
             bessel_j(v - 1, x) - bessel_j(v + 1, x)
(%o6)        ---------------------------------------
                                2
(%i7) integrate(bessel_j(v,x), x);
(%o7) 
                                               2
                    v   1    v   3            x    - v - 1  v + 1
    hypergeometric([- + -], [- + -, v + 1], - --) 2        x
                    2   2    2   2            4
    -------------------------------------------------------------
                         v   1
                        (- + -) gamma(v + 1)
                         2   2
(%i8) laplace(bessel_j(2,t), t, s);
                                1       2
                      (1 - sqrt(-- + 1))  s
                                 2
                                s
(%o8)                 ---------------------
                               1
                          sqrt(-- + 1)
                                2
                               s
```


Bessel-Funktionen als Losung einer linearen Differentialgleichung zweiter
Ordnung.



```maxima
(%i1) depends(y, x);
(%o1)                        [y(x)]
(%i2) declare(n, integer);
(%o2)                         done
(%i3) 'diff(y, x, 2)*x^2 + 'diff(y, x)*x + y*(x^2-n^2) = 0;
                                2
                     2    2    d y  2   dy
(%o3)            y (x  - n ) + --- x  + -- x = 0
                                 2      dx
                               dx
(%i4) ode2(%, y, x);
(%o4)      y = %k2 bessel_y(n, x) + %k1 bessel_j(n, x)
```

See also: `float`, `numer`, `properties`, `conjugate`, `distribute_over`, `besselexpand`, `bessel_reduce`, `hypergeometric_representation`, `spherical_bessel_j`, `bessel_y`, `bessel_i`, `bessel_k`, `Hankel-Funktionen`, `Airy-Funktionen`, `Struve-Funktionen`, `laplace`.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_k -->
<!-- signatures: bessel_k(v, z) -->
### Function: bessel_k (v, z)

Die modifizierte Bessel-Funktion der zweiten Art der Ordnung $v$ mit dem
Argument $z$.  `bessel_k` ist definiert als



```maxima
%pi csc(%pi u) (I   (z) - I (z))
                               - v       u
      K (z) = --------------------------------
       v                     2
```


$$
K_{v}(z)={{\pi\,\csc \left(\pi\,u\right)\,\left(I_{-v}(z)-I_{u}(z)
 \right)}\over{2}}
$$


fur den Fall, dass $v$ keine ganze Zahl ist.  Ist $v$ eine ganze
Zahl $n$, dann wird die Bessel-Funktion `bessel_k` wie folgt als
Grenzwert definiert



```maxima
(%o5) K (z) = limit  K (z)
       n      v -> n  v
```


$$
K_{n}(z)=\lim_{v\rightarrow n}{K_{v}(z)}
$$


Die Bessel-Funktion `bessel_k` ist fur das numerische und symbolische
Rechnen geeignet.


Maxima berechnet `bessel_k` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente ganze oder rationale Zahlen
sind.  Die numerische Berechnung fur große Gleitkommazahlen ist nicht
implementiert.  In diesem Fall gibt Maxima eine Substantivform zuruck.


`bessel_k` hat die folgenden Eigenschaften, die mit mit der Funktion
`properties` angezeigt werden und auf das symbolische Rechnen Einfluss
haben:



**conjugate function** — `bessel_k` hat Spiegelsymmetrie, wenn das Argument *z* keine negative
reelle Zahl ist.  Die Spiegelsymmetrie wird zum Beispiel von der Funktion
`conjugate` fur die Vereinfachung eines Ausdrucks genutzt.
**complex characteristic** — Maxima kennt den Realteil und den Imaginarteil von `bessel_k` fur
spezielle Argumente $v$ und $z$.
**limit function** — Maxima kennt spezielle Grenzwerte der Funktion `bessel_k`.
**integral** — Maxima kennt das Integral der Funktion `bessel_k` fur die
Integrationsvariable $z$.
**gradef** — Maxima kennt die Ableitungen der Funktion `bessel_k` nach den
Argumenten $v$ und $z$.


Die Vereinfachung der Bessel-Funktion `bessel_k` wird von den folgenden
Optionsvariablen kontrolliert:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und sind
die Argumente von `bessel_k` eine Matrix, Liste oder Gleichung wird die
Funktion auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der
Standardwert ist `true`.
**besselexpand** — Hat die Optionsvariable `besselexpand` den Wert `true`, wird
`bessel_k` mit einer halbzahligen Ordnung $v$ als Exponentialfunktion
entwickelt.
**bessel_reduce** — Hat die Optionsvariable `bessel_reduce` den Wert `true`, wird
`bessel_k` mit einer ganzzahligen Ordnung $n$ nach Bessel-Funktionen
`bessel_k` mit der niedrigsten Ordnung `0` und `1` entwickelt.
**hypergeometric_representation** — Hat die Optionsvariable `hypergeometric_representation` den Wert
`true`, dann wird `bessel_k` als hypergeometrische Funktion
dargestellt.  Es ist zu beachten, dass die hypergeometrische Funktion nur fur
eine nicht ganzzahlige Ordnung $v$ gultig ist.


Weiterhin kennt Maxima die geraden und ungeraden Symmetrieeigenschaften von
`bessel_k`.  Fur eine ganze Zahl $n$ vereinfacht daher
`bessel_k(-n, z)` zu `bessel_y(n, z)`.


Siehe auch die anderen Bessel-Funktionen `bessel_j`, `bessel_y`
und `bessel_i` sowie die weiteren mit den Bessel-Funktionen verwandten
Funktionen wie die Hankel-Funktionen in `Hankel-Funktionen`, Airy-Funktionen
in `Airy-Funktionen` und Struve-Funktionen in `Struve-Funktionen`.


Siehe die Funktion `bessel_j` fur Beispiele mit Bessel-Funktionen.

See also: `float`, `numer`, `properties`, `conjugate`, `distribute_over`, `besselexpand`, `bessel_reduce`, `hypergeometric_representation`, `bessel_j`, `bessel_y`, `bessel_i`, `Hankel-Funktionen`, `Airy-Funktionen`, `Struve-Funktionen`.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_reduce -->
<!-- signatures: bessel_reduce -->
### Variable: bessel_reduce

Standardwert: `false`


Hat die Optionsvariable `bessel_reduce` den Wert `true`, werden 
Bessel-Funktionen mit einer ganzzahligen Ordnung $n$ nach Bessel-Funktionen
mit der niedrigsten Ordnung $0$ und $1$ entwickelt.

<!-- category: SpecialFunctions -->
<!-- keywords: bessel_y -->
<!-- signatures: bessel_y(v, z) -->
### Function: bessel_y (v, z)

Die Bessel-Funktion der zweiten Art der Ordnung $v$ mit dem Argument
$z$.  `bessel_y` ist definiert als



```maxima
cos(%pi v) J (z) - J   (z)
                          v       - v
      Y (z) = --------------------------
       v              sin(%pi v)
```


$$
Y_{v}(z)={{\cos \left(\pi\,v\right)\,J_{v}(z)-J_{-v}(z)}\over{\sin 
 \left(\pi\,v\right)}}
$$


fur den Fall, dass $v$ keine ganze Zahl ist.  Ist $v$ eine ganze
Zahl $n$, dann wird die Bessel-Funktion `bessel_y` wie folgt als
ein Grenzwert definiert



```maxima
Y (z) = limit  Y (z)
       n      v -> n  v
```


$$
Y_{n}(z)=\lim_{v\rightarrow n}{Y_{v}(z)}
$$


Die Bessel-Funktion `bessel_y` ist fur das numerische und symbolische
Rechnen geeignet.


Maxima berechnet `bessel_y` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente ganze oder rationale Zahlen
sind.  Die numerische Berechnung fur große Gleitkommazahlen ist nicht
implementiert.  In diesem Fall gibt Maxima eine Substantivform zuruck.


`bessel_y` hat die folgenden Eigenschaften, die mit mit der Funktion
`properties` angezeigt werden und auf das symbolische Rechnen Einfluss
haben:



**conjugate function** — `bessel_y` hat Spiegelsymmetrie, wenn das Argument *z* keine negative
reelle Zahl ist.  Die Spiegelsymmetrie wird zum Beispiel von der Funktion
`conjugate` fur die Vereinfachung eines Ausdrucks genutzt.
**complex characteristic** — Maxima kennt den Realteil und den Imaginarteil von `bessel_y` fur
spezielle Argumente $v$ und $z$.
**limit function** — Maxima kennt spezielle Grenzwerte der Funktion `bessel_y`.
**integral** — Maxima kennt das Integral der Funktion `bessel_y` fur die
Integrationsvariable $z$.
**gradef** — Maxima kennt die Ableitungen der Funktion `bessel_y` nach den
Argumenten $v$ und $z$.


Die Vereinfachung der Bessel-Funktion `bessel_y` wird von den folgenden
Optionsvariablen kontrolliert:



**distribute_over** — Hat die Optionsvariable `distribute_over` den Wert `true` und sind
die Argumente von `bessel_y` eine Matrix, Liste oder Gleichung wird die
Funktion auf die Elemente oder beiden Seiten der Gleichung angewendet.  Der
Standardwert ist `true`.
**besselexpand** — Hat die Optionsvariable `besselexpand` den Wert `true`, wird
`bessel_y` mit einer halbzahligen Ordnung $v$ als Sinus- und
Kosinusfunktionen entwickelt.
**bessel_reduce** — Hat die Optionsvariable `bessel_reduce` den Wert `true`, wird
`bessel_y` mit einer ganzzahligen Ordnung $n$ nach Bessel-Funktionen
`bessel_y` mit der niedrigsten Ordnung `0` und `1` entwickelt.
**hypergeometric_representation** — Hat die Optionsvariable `hypergeometric_representation` den Wert
`true`, dann wird `bessel_y` als hypergeometrische Funktion
dargestellt.  Es ist zu beachten, dass die hypergeometrische Funktion nur fur
eine nicht ganzzahlige Ordnung $v$ gultig ist.


Weiterhin kennt Maxima die geraden und ungeraden Symmetrieeigenschaften von
`bessel_y`.  Fur eine ganze Zahl $n$ vereinfacht daher
`bessel_y(-n, z)` zu `(-1)^n bessel_y(n, z)`.


Maxima kennt noch die Funktion `spherical_bessel_y`, die im Paket
`orthopoly` definiert ist.   Siehe auch die anderen Bessel-Funktionen
`bessel_j`, `bessel_i` und `bessel_k` sowie die
weiteren mit den Bessel-Funktionen verwandten Funktionen wie die
Hankel-Funktionen in `Hankel-Funktionen`, Airy-Funktionen in
`Airy-Funktionen` und Struve-Funktionen in `Struve-Funktionen`.


Siehe die Funktion `bessel_j` fur Beispiele mit Bessel-Funktionen.

See also: `float`, `numer`, `properties`, `conjugate`, `distribute_over`, `besselexpand`, `bessel_reduce`, `hypergeometric_representation`, `spherical_bessel_y`, `bessel_j`, `bessel_i`, `bessel_k`, `Hankel-Funktionen`, `Airy-Funktionen`, `Struve-Funktionen`.

<!-- category: SpecialFunctions -->
<!-- keywords: besselexpand -->
<!-- signatures: besselexpand -->
### Variable: besselexpand

Standardwert: `false`


Hat die Optionsvariable `besselexpand` den Wert `true`, werden
Bessel-Funktion mit einer halbzahligen Ordnung $v$ als Sinus-,
Kosinus-, Hyperbel- oder Exponentialfunktionen entwickelt.  Die Optionsvariable
`besselexpand` kontrolliert auch die Entwicklung der Hankel-Funktionen
`hankel_1` und `hankel_2` sowie der Struve-Funktionen `struve_h`
und `struve_l`.


Beispiele:



```maxima
(%i1) besselexpand: false$

(%i2) bessel_j(3/2, z);
                                  3
(%o2)                    bessel_j(-, z)
                                  2
(%i3) besselexpand: true$

(%i4) bessel_j(3/2, z);
                                 sin(z)   cos(z)
                sqrt(2) sqrt(z) (------ - ------)
                                    2       z
                                   z
(%o4)           ---------------------------------
                            sqrt(%pi)
```


Weitere Beispiele fur die Entwicklungen der Funktionen `bessel_k` und
`struve_h`.



```maxima
(%i5) bessel_k(3/2, z);
                                1        - z
                     sqrt(%pi) (- + 1) %e
                                z
(%o5)                -----------------------
                         sqrt(2) sqrt(z)

(%i6) struve_h(3/2, z);
                                           2
                  2 z sin(z) + 2 cos(z) - z  - 2
(%o6)           - ------------------------------
                                         3/2
                      sqrt(2) sqrt(%pi) z
```

See also: `hankel_1`, `hankel_2`, `struve_h`, `struve_l`, `bessel_k`.

<!-- category: SpecialFunctions -->
<!-- keywords: beta -->
<!-- signatures: beta(a, b) -->
### Function: beta (a, b)

Die Betafunktion ist definiert als `gamma(a) gamma(b)/gamma(a+b)`
(A & S 6.2.1).


Maxima vereinfacht die Betafunktion fur positive ganze Zahlen *a* und
*b* sowie rationale Zahlen, deren Summe `a + b` eine ganze
Zahl ist.  Hat die Optionsvariable `beta_args_sum_to_integer` den Wert
`true`, vereinfacht Maxima die Betafunktion fur allgemeine Ausdrucke
*a* und *b*, deren Summe eine ganze Zahl ist.


Ist eines der Argumente *a* oder *b* Null, ist die Betafunktion nicht
definiert.


Im allgemeinen ist die Betafunktion nicht definiert fur negative ganze Zahlen
als Argument.  Ausnahme ist der Fall, dass *a = -n*, wobei *n* eine
positive ganze Zahl und *b* eine positive ganze Zahl mit *b <= b* ist.
In diesem Fall kann eine analytische Fortsetzung der Betafunktion definiert
werden.  Maxima gibt fur diesen Fall ein Ergebnis zuruck.


Hat die Optionsvariable `beta_expand` den Wert `true`, werden
Ausdrucke wie `beta(a+n, b` und `beta(a-n, b)` oder
`beta(a, b+n` und `beta(a, b-n)` entwickelt.


Maxima berechnet die Betafunktion fur reelle und komplexe Gleitkommazahlen
numerisch.  Fur die numerische Berechnung nutzt Maxima die Funktion
`log_gamma`:



```maxima
- log_gamma(b + a) + log_gamma(b) + log_gamma(a)
         %e
```


Maxima kennt Symmetrieeigenschaften der Betafunktion.  Die Betafunktion ist
symmetrisch und hat Spiegelsymmetrie.


Maxima kennt die Ableitung der Betafunktion nach den Argumenten *a* und
*b*.


Mit der Funktion `makegamma` kann die Betafunktion durch Gammafunktionen
ersetzt werden.  Entsprechend ersetzt die Funktion `makefact`
Betafunktionen in einem Ausdruck durch Fakultaten.


Beispiele:


Vereinfachung der Betafunktion, wenn eines der Argumente eine ganze Zahl ist.



```maxima
(%i1) [beta(2,3),beta(2,1/3),beta(2,a)];

                               1   9      1
(%o1)                         [--, -, ---------]
                               12  4  a (a + 1)
```


Vereinfachung der Betafunktion fur zwei rationale Argumente, die sich zu
einer ganzen Zahl summieren.



```maxima
(%i2) [beta(1/2,5/2),beta(1/3,2/3),beta(1/4,3/4)];
                          3 %pi   2 %pi
(%o2)                    [-----, -------, sqrt(2) %pi]
                            8    sqrt(3)
```


Hat die Optionsvariable `beta_args_sum_to_integer` den Wert `true`,
vereinfacht die Betafunktion fur allgemeine Ausdrucke, die sich zu einer
ganzen Zahl summieren.



```maxima
(%i3) beta_args_sum_to_integer:true$
(%i4) beta(a+1,-a+2);
                                %pi (a - 1) a
(%o4)                         ------------------
                              2 sin(%pi (2 - a))
```


Die moglichen Ergebnisse, wenn eines der Argumente eine negative ganze
Zahl ist.



```maxima
(%i5) [beta(-3,1),beta(-3,2),beta(-3,3)];
                                    1  1    1
(%o5)                            [- -, -, - -]
                                    3  6    3
```


Vereinfachungen, wenn die Optionsvariable `beta_expand` den Wert
`true` hat.



```maxima
(%i6) beta_expand:true$
(%i7) [beta(a+1,b),beta(a-1,b),beta(a+1,b)/beta(a,b+1)];
                    a beta(a, b)  beta(a, b) (b + a - 1)  a
(%o7)              [------------, ----------------------, -]
                       b + a              a - 1           b
```


Die Betafunktion ist nicht definiert, wenn eines der Argumente Null ist.



```maxima
(%i7) beta(0,b);
beta: expected nonzero arguments; found 0, b
 -- an error.  To debug this try debugmode(true);
```


Numerische Berechnung der Betafunktion fur reelle und komplexe Argumente.



```maxima
(%i8) beta(2.5,2.3);
(%o8) .08694748611299981

(%i9) beta(2.5,1.4+%i);
(%o9) 0.0640144950796695 - .1502078053286415 %i

(%i10) beta(2.5b0,2.3b0);
(%o10) 8.694748611299969b-2

(%i11) beta(2.5b0,1.4b0+%i);
(%o11) 6.401449507966944b-2 - 1.502078053286415b-1 %i
```


Die Betafunktion ist symmetrisch und hat Spiegelsymmetrie.



```maxima
(%i14) beta(a,b)-beta(b,a);
(%o14)                                 0
(%i15) declare(a,complex,b,complex)$
(%i16) conjugate(beta(a,b));
(%o16)                 beta(conjugate(a), conjugate(b))
```


Ableitung der Betafunktion.



```maxima
(%i17) diff(beta(a,b),a);
(%o17)               - beta(a, b) (psi (b + a) - psi (a))
                                      0             0
```

See also: `beta_args_sum_to_integer`, `log_gamma`, `makegamma`, `makefact`.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_args_sum_to_integer -->
<!-- signatures: beta_args_sum_to_integer -->
### Variable: beta_args_sum_to_integer

Standardwert: `false`





Hat die Optionsvariable `beta_args_sum_to_integer` den Wert `true`,
vereinfacht Maxima die Funktion `beta(a,b)`, wenn sich die Argumente
*a* und *b* zu einer ganzen Zahlen summieren.  Siehe auch `beta`.

See also: `beta`.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_expand -->
<!-- signatures: beta_expand -->
### Variable: beta_expand

Standardwert: `false`






Hat die Optionsvariable `beta_expand` den Wert `true`, werden
`beta(a,b)` und verwandte Funktionen fur Argumente $a+n$ oder
$a-n$ entwickelt, wobei *n* eine positive ganze Zahl ist.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete -->
<!-- signatures: beta_incomplete(a, b, z) -->
### Function: beta_incomplete (a, b, z)

Die Definition der unvollstandigen Betafunktion ist (A & S 6.6.1)



```maxima
z
                      /
                      [         b - 1  a - 1
                      I  (1 - t)      t      dt
                      ]
                      /
                       0
```


Diese Definition ist moglich fur $realpart(a)>0$ und
$realpart(b)>0$ sowie $abs(z)<1$.  Fur andere Werte kann die
unvollstandige Betafunktion als eine verallgemeinerte Hypergeometrische
Funktion definiert werden:



```maxima
gamma(a) hypergeometric_generalized([a, 1 - b], [a + 1], z) z
```


(Siehe [https://functions.wolfram.com/]() fur eine Definition der unvollstandigen
Betafunktion.)


Fur negative ganze Zahlen $a = -n$ und positive ganze Zahlen
$b = m$ mit $m <= n$ kann die unvollstandige Betafunktion definiert
werden als



```maxima
m - 1           k
                            ====  (1 - m)  z
                      n - 1 \            k
                     z       >    -----------
                            /     k! (n - k)
                            ====
                            k = 0
```


Maxima nutzt diese Definition, um die Funktion `beta_incomplete` fur
negative ganzzahlige Argumente *a* zu vereinfachen.


Fur positive ganzzahlige Argumente *a* vereinfacht `beta_incomplete`
fur jedes Argument *b* und *z*.  Entsprechend vereinfacht
`beta_incomplete` fur ein positives ganzzahliges Argument *b* mit
der Ausnahme, dass *a* eine negative ganze Zahl ist.


Fur $z=0$ und $realpart(a) > 0$ hat `beta_incomplete` den
speziellen Wert Null.  Fur *z=1* und $realpart(b) > 0$ vereinfacht
`beta_incomplete` zu einem Ausdruck mit der Betafunktion `beta(a, b)`.


Maxima berechnet `beta_incomplete` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente.  Fur die numerische Berechnung nutzt Maxima
eine Entwicklung der unvollstandigen Betafunktion als Kettenbruch.


Hat die Optionsvariable `beta_expand` den Wert `true`, entwickelt
Maxima Ausdrucke der Form `beta_incomplete(a+n, b, z)` und
`beta_incomplete(a-n, b, z)`, wobei `n` eine ganze Zahl ist.


Maxima kennt die Ableitungen der unvollstandigen Betafunktion nach den
Variablen *a*, *b* und *z* und das Integral fur die 
Integrationsvariable *z*.


Beispiele:


Vereinfachung fur eine positive ganze Zahl als Argument *a*.



```maxima
(%i1) beta_incomplete(2,b,z);
                                       b
                            1 - (1 - z)  (b z + 1)
(%o1)                       ----------------------
                                  b (b + 1)
```


Vereinfachung fur eine positive ganze Zahl als Argument *b*.



```maxima
(%i2) beta_incomplete(a,2,z);
                                               a
                              (a (1 - z) + 1) z
(%o2)                         ------------------
                                  a (a + 1)
```


Vereinfachung fur positive ganzzahlige Argumente *a* und *b*.



```maxima
(%i3) beta_incomplete(3,2,z);
                                               3
                              (3 (1 - z) + 1) z
(%o3)                         ------------------
                                      12
```


*a* ist eine negative ganze Zahl mit $b <= (-a)$.  Maxima vereinfacht
fur diesem Fall.



```maxima
(%i4) beta_incomplete(-3,1,z);
                                       1
(%o4)                              - ----
                                        3
                                     3 z
```


Fur die speziellen Werte $z=0$ und $z=1$ vereinfacht Maxima.



```maxima
(%i5) assume(a>0,b>0)$
(%i6) beta_incomplete(a,b,0);
(%o6)                                 0
(%i7) beta_incomplete(a,b,1);
(%o7)                            beta(a, b)
```


Numerische Berechnung fur reelle Argumente.



```maxima
(%i8) beta_incomplete(0.25,0.50,0.9);
(%o8)                          4.594959440269333
(%i9)  fpprec:25$
(%i10) beta_incomplete(0.25,0.50,0.9b0);
(%o10)                    4.594959440269324086971203b0
```


Fur $abs(z) > 1$ ist das Ergebnis komplex.



```maxima
(%i11) beta_incomplete(0.25,0.50,1.7);
(%o11)              5.244115108584249 - 1.45518047787844 %i
```


Numerische Ergebnisse fur komplexe Argumente.



```maxima
(%i14) beta_incomplete(0.25+%i,1.0+%i,1.7+%i);
(%o14)             2.726960675662536 - .3831175704269199 %i
(%i15) beta_incomplete(1/2,5/4*%i,2.8+%i);
(%o15)             13.04649635168716 %i - 5.802067956270001
(%i16)
```


Entwicklung, wenn `beta_expand` den Wert `true` hat.



```maxima
(%i23) beta_incomplete(a+1,b,z),beta_expand:true;
                                                       b  a
                   a beta_incomplete(a, b, z)   (1 - z)  z
(%o23)             -------------------------- - -----------
                             b + a                 b + a

(%i24) beta_incomplete(a-1,b,z),beta_expand:true;
                                                           b  a - 1
           beta_incomplete(a, b, z) (- b - a + 1)   (1 - z)  z
(%o24)     -------------------------------------- - ---------------
                           1 - a                         1 - a
```

 

Ableitung und Integral der unvollstandigen Betafunktion.



```maxima
(%i34) diff(beta_incomplete(a, b, z), z);
                              b - 1  a - 1
(%o34)                 (1 - z)      z
(%i35) integrate(beta_incomplete(a, b, z), z);
              b  a
       (1 - z)  z
(%o35) ----------- + beta_incomplete(a, b, z) z
          b + a
                                       a beta_incomplete(a, b, z)
                                     - --------------------------
                                                 b + a
(%i36) factor(diff(%, z));
(%o36)              beta_incomplete(a, b, z)
```

See also: `beta_expand`.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete_generalized -->
<!-- signatures: beta_incomplete_generalized(a, b, z1, z2) -->
### Function: beta_incomplete_generalized (a, b, z1, z2)

Die Definition der verallgemeinerten unvollstandigen Betafunktion ist



```maxima
z2
                     /
                     [          b - 1  a - 1
                     I   (1 - t)      t      dt
                     ]
                     /
                      z1
```





Maxima vereinfacht `beta_incomplete_refularized` fur positive ganzzahlige
Argumente *a* und *b*.







Ist $realpart(a)>0$ und $z1=0$ oder $z2=0$, vereinfacht Maxima
`beta_incomplete_generalized` zu der Funktion
`beta_incomplete`.  Ist $realpart(b)>0$ und $z1=1$ oder
*z2=1*, vereinfacht Maxima zu einem Ausdruck mit der Funktion
`beta` und `beta_incomplete`.





Maxima berechnet `beta_incomplete_regularized` numerisch fur reelle und
komplexe Gleitkommazahlen in doppelter und beliebiger Genauigkeit.






Hat die Optionsvariable `beta_expand` den Wert `true`, dann expandiert
Maxima `beta_incomplete_generalized` fur Argumente $a+n$ und
$a-n$, wobei *n* eine positive ganze Zahl ist.






Maxima kennt die Ableitung der Funktion `beta_incomplete_generalized` nach
den Variablen *a*, *b*, *z1* und *z2* sowie die Integrale
fur die Integrationsvariablen  *z1* und *z2*.


Beispiele:





Maxima vereinfacht `beta_incomplete_generalized`, wenn *a* und *b*
positive ganze Zahlen sind.



```maxima
(%i1) beta_incomplete_generalized(2,b,z1,z2);

                   b                      b
           (1 - z1)  (b z1 + 1) - (1 - z2)  (b z2 + 1)
(%o1)      -------------------------------------------
                            b (b + 1)

(%i2) beta_incomplete_generalized(a,2,z1,z2);

                              a                      a
           (a (1 - z2) + 1) z2  - (a (1 - z1) + 1) z1
(%o2)      -------------------------------------------
                            a (a + 1)

(%i3) beta_incomplete_generalized(3,2,z1,z2);
              2      2                       2      2
      (1 - z1)  (3 z1  + 2 z1 + 1) - (1 - z2)  (3 z2  + 2 z2 + 1)
(%o3) -----------------------------------------------------------
                                  12
```





Vereinfachung fur die speziellen Werte $z1=0$, $z2=0$, $z1=1$
und $z2=1$.



```maxima
(%i4) assume(a > 0, b > 0)$
(%i5) beta_incomplete_generalized(a,b,z1,0);
(%o5)                    - beta_incomplete(a, b, z1)

(%i6) beta_incomplete_generalized(a,b,0,z2);
(%o6)                    - beta_incomplete(a, b, z2)

(%i7) beta_incomplete_generalized(a,b,z1,1);
(%o7)              beta(a, b) - beta_incomplete(a, b, z1)

(%i8) beta_incomplete_generalized(a,b,1,z2);
(%o8)              beta_incomplete(a, b, z2) - beta(a, b)
```




Numerische Berechnung fur reelle Argumente in doppelter und beliebiger
Gleitkommagenauigkeit.



```maxima
(%i9) beta_incomplete_generalized(1/2,3/2,0.25,0.31);
(%o9)                        .09638178086368676

(%i10) fpprec:32$
(%i10) beta_incomplete_generalized(1/2,3/2,0.25,0.31b0);
(%o10)               9.6381780863686935309170054689964b-2
```




Numerische Berechnung fur komplexe Argumente in doppelter und beliebiger
Gleitkommagenauigkeit.



```maxima
(%i11) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31);
(%o11)           - .09625463003205376 %i - .003323847735353769
(%i12) fpprec:20$
(%i13) beta_incomplete_generalized(1/2+%i,3/2+%i,0.25,0.31b0);
(%o13)     - 9.6254630032054178691b-2 %i - 3.3238477353543591914b-3
```





Expansion fur $a+n$ oder $a-n$ und *n* eine positive ganze Zahl,
wenn `beta_expand` den Wert `true` hat.



```maxima
(%i14) beta_expand:true$

(%i15) beta_incomplete_generalized(a+1,b,z1,z2);

               b   a           b   a
       (1 - z1)  z1  - (1 - z2)  z2
(%o15) -----------------------------
                   b + a
                      a beta_incomplete_generalized(a, b, z1, z2)
                    + -------------------------------------------
                                         b + a

(%i16) beta_incomplete_generalized(a-1,b,z1,z2);

       beta_incomplete_generalized(a, b, z1, z2) (- b - a + 1)
(%o16) -------------------------------------------------------
                                1 - a
                                    b   a - 1           b   a - 1
                            (1 - z2)  z2      - (1 - z1)  z1
                          - -------------------------------------
                                            1 - a
```




Ableitung nach der Variablen *z1* und die Integrale fur die
Integrationsvariablen *z1* und *z2*.



```maxima
(%i17) diff(beta_incomplete_generalized(a,b,z1,z2),z1);
                               b - 1   a - 1
(%o17)               - (1 - z1)      z1
(%i18) integrate(beta_incomplete_generalized(a,b,z1,z2),z1);
(%o18) beta_incomplete_generalized(a, b, z1, z2) z1
                                  + beta_incomplete(a + 1, b, z1)
(%i19) integrate(beta_incomplete_generalized(a,b,z1,z2),z2);
(%o19) beta_incomplete_generalized(a, b, z1, z2) z2
                                  - beta_incomplete(a + 1, b, z2)
```

See also: `beta_incomplete`, `beta`, `beta_expand`.

<!-- category: SpecialFunctions -->
<!-- keywords: beta_incomplete_regularized -->
<!-- signatures: beta_incomplete_regularized(a, b, z) -->
### Function: beta_incomplete_regularized (a, b, z)

Die regularisierte unvollstandige Beta Funktion (A & S 6.6.2), die definiert
ist als



```maxima
beta_incomplete(a, b, z)
              ------------------------
                     beta(a, b)
```






Wie bei der Funktion `beta_incomplete` ist diese Definition nicht
vollstandig.  Siehe [https://functions.wolfram.com]() fur eine vollstandige
Definition der Funktion.








`beta_incomplete_regularized` vereinfacht, wenn das Argument *a* oder
*b* eine positive ganze Zahl ist.  Fur Argumente `z = 0` und
`realpart(a) > 0` vereinfacht die Funktion
`beta_incomplete_regularized` zu `0`.  Fur `z = 1` und
`realpart(b) > 0` vereinfacht die Funktion
`beta_incomplete_regularized` zu `1`.





Maxima berechnet `beta_incomplete_regularized` fur reelle und komplexe
Gleitkommazahlen als Argumente numerisch.


When `beta_expand` is `true`, Maxima expands 
`beta_incomplete_regularized` for arguments $a+n$ or $a-n$, 
where n is an integer.


Hat die Optionsvariable `beta_expand` den Wert `true`, expandiert
Maxima `beta_incomplete_regularized` fur Argumente $a+n$ oder
$a-n$, wobei *n* eine ganze Zahl ist.






Maxima kennt die Ableitung der Funktion `beta_incomplete_regularized`
nach den Argumenten *a*, *b* und *z* sowie das Integral fur das
Argument *z*.


Beispiele:




Vereinfachung, wenn die Argumente *a* oder *b* ganze Zahlen sind.



```maxima
(%i1) beta_incomplete_regularized(2,b,z);
                                b
(%o1)                1 - (1 - z)  (b z + 1)
(%i2) beta_incomplete_regularized(a,2,z);
                                        a
(%o2)                  (a (1 - z) + 1) z
(%i3) beta_incomplete_regularized(3,2,z);
                                        3
(%o3)                  (3 (1 - z) + 1) z
```




Fur die speziellen Werte $z=0$ und $z=1$ vereinfacht Maxima.



```maxima
(%i4) assume(a>0,b>0)$

(%i5) beta_incomplete_regularized(a,b,0);
(%o5)                           0
(%i6) beta_incomplete_regularized(a,b,1);
(%o6)                           1
```





Numerische Berechnung fur reelle und komplexe Argumente.



```maxima
(%i7) beta_incomplete_regularized(0.12,0.43,0.9);
(%o7)                   .9114011367359802
(%i8) fpprec:32$

(%i9) beta_incomplete_regularized(0.12,0.43,0.9b0);
(%o9)         9.1140113673598075519946998779975b-1
(%i10) beta_incomplete_regularized(1+%i,3/3,1.5*%i);
(%o10)      .2865367499935405 %i - .1229959633346841
(%i11) fpprec:20$

(%i12) beta_incomplete_regularized(1+%i,3/3,1.5b0*%i);
(%o12) 2.8653674999354036142b-1 %i - 1.2299596333468400163b-1
```




Expansion, wenn `beta_expand` den Wert `true` hat.



```maxima
(%i13) beta_incomplete_regularized(a+1,b,z);
                                                     b  a
                                              (1 - z)  z
(%o13) beta_incomplete_regularized(a, b, z) - ------------
                                              a beta(a, b)
(%i14) beta_incomplete_regularized(a-1,b,z);

(%o14) beta_incomplete_regularized(a, b, z)
                                                     b  a - 1
                                              (1 - z)  z
                                         - ----------------------
                                           beta(a, b) (b + a - 1)
```




Die Ableitung und das Integral der Funktion.



```maxima
(%i15) diff(beta_incomplete_regularized(a,b,z),z);
                              b - 1  a - 1
                       (1 - z)      z
(%o15)                 -------------------
                           beta(a, b)
(%i16) integrate(beta_incomplete_regularized(a,b,z),z);
(%o16) beta_incomplete_regularized(a, b, z) z
                                                           b  a
                                                    (1 - z)  z
          a (beta_incomplete_regularized(a, b, z) - ------------)
                                                    a beta(a, b)
        - -------------------------------------------------------
                                   b + a
```

See also: `beta_incomplete`, `beta_expand`.

<!-- category: SpecialFunctions -->
<!-- keywords: bffac -->
<!-- signatures: bffac(x, fpprec) -->
### Function: bffac (x, fpprec)

Berechnet die Fakultat fur große Gleitkommazahlen.  Das Argument *x*
muss eine große Gleitkommazahl sein.  Das zweite Argument *fpprec* ist
die Anzahl der Stellen, fur die die Fakultat berechnet wird.  Das Ergebnis
ist eine große Gleitkommazahl.


Fur das symbolische Rechnen mit der Fakultat und der Gammafunktion siehe die
entsprechenden Funktionen `factorial` und `gamma`.  Maxima ruft
intern die Funktion `bffac` auf, um die Fakultat `factorial` und
die Gammafunktion `gamma` fur eine große Gleitkommazahl numerisch zu
berechnen.


Siehe auch die Funktion `cbffac` fur die Berechnung der Fakultat fur
komplexe große Gleitkommazahlen.


Beispiel:



```maxima
(%i1) bffac(10.5b0, 25);
(%o1)             1.189942308396224845701304b7
(%i2) fpprec:25$
(%i3) 10.5b0!;
(%o3)             1.189942308396224845701303b7
```

See also: `factorial`, `gamma`, `cbffac`.

<!-- category: SpecialFunctions -->
<!-- keywords: bfpsi, bfpsi0 -->
<!-- signatures: bfpsi(n, x, fpprec), bfpsi0(x, fpprec) -->
### Function: bfpsi (n, x, fpprec)

`bfpsi` ist die Polygammafunktion fur ein reelles Argument *x* und
einer ganzzahligen Ordnung *n*.  `bfpsi0` ist die Digammafunktion.
`bfpsi0(x, fpprec)` ist aquivalent zu `bfpsi(0, x, fpprec)`.


Das Argument *x* der Funktionen `bfpsi` und `bfpsi0` muss eine
große Gleitkommazahl sein.  Das Argument *fpprec* gibt die Anzahl der
Stellen an, fur die die Funktion berechnet wird.  Das Ergebnis ist eine
große Gleitkommazahl.


Fur das symbolische Rechnen mit der Polygammafunktion siehe die Funktion
`psi`.  Maxima ruft intern die Funktion `bfpsi` auf, um die
Polygammafunktion fur große Gleitkommazahlen numerisch zu berechnen.


Beispiel:



```maxima
(%i1) bfpsi(0, 1, 25);
(%o1)            - 5.772156649015328606065121b-1
(%i2) fpprec:25$

(%i3) psi[0](1.0b0);
(%o3)            - 5.772156649015328606065121b-1
```

See also: `psi`.

<!-- category: SpecialFunctions -->
<!-- keywords: cbffac -->
<!-- signatures: cbffac(z, fpprec) -->
### Function: cbffac (z, fpprec)

Berechnet die Fakultat fur komplexe große Gleitkommazahlen.  Das
Argument *z* ist eine komplexe große Gleitkommazahl.  Das zweite
Argument *fpprec* ist die Anzahl der Stellen, fur die die Fakultat
berechnet wird.  Das Ergebnis ist eine komplexe große Gleitkommazahl.


Fur das symbolische Rechnen mit der Fakultat und der Gammafunktion siehe die
entsprechenden Funktionen `factorial` und `gamma`.  Maxima ruft
intern die Funktion `cbffac` auf, um die Fakultat `factorial` und
die Gammafunktion `gamma` fur eine komplexe große Gleitkommazahl
numerisch zu berechnen.


Siehe auch die Funktion `bffac`.

See also: `factorial`, `gamma`, `bffac`.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma -->
<!-- signatures: gamma(z) -->
### Function: gamma (z)

Die Definition der Gammafunktion ist (A & S 6.1.1)



```maxima
inf
                      /
                      [     z - 1   - t
           gamma(z) = I    t      %e    dt
                      ]
                      /
                       0
```


Die Gammafunktion `gamma` ist fur das numerische und symbolische Rechnen
geeignet.  Fur positive ganze Zahlen und rationale Zahlen als Argument *z*
wird die Gammafunktion vereinfacht.  Fur halbzahlige rationale Zahlen ist das
Ergebnis der Vereinfachung eine rationale Zahl multipliziert mit
`sqrt(%pi)`.  Die Vereinfachung fur ganze Zahlen wird von der
Optionsvariablen `factlim` kontrolliert.  Fur ganze Zahlen, die
großer als `factlim` sind, kann es zu einem Uberlauf bei der
Berechnung der Gammafunktion kommen.  Entsprechend wird die Vereinfachung fur
rationale Zahlen von der Optionsvariablen `gammalim` kontrolliert.


Fur negative ganze Zahlen ist die Gammafunktion `gamma` nicht definiert.


Maxima berechnet `gamma` numerisch fur reelle und komplexe Argumente
*z*.  Das Ergebnis ist eine reelle oder komplexe Gleitkommazahl.


`gamma` hat Spiegelsymmetrie.


Hat die Optionsvariable `gamma_expand` den Wert `true`, entwickelt
Maxima die Gammafunktion fur Argumente der Form `z+n` und `z-n`,
wobei *n* eine ganze Zahl ist.


Maxima kennt die Ableitung der Gammafunktion `gamma`.


Siehe auch die Funktion `makegamma`, um Fakultaten und
Betafunktionen in einem Ausdruck durch die Gammafunktion zu ersetzen.


Die Euler-Mascheroni-Konstante ist `%gamma`.


Beispiele:


Vereinfachung fur ganze Zahlen und rationale Zahlen.



```maxima
(%i1) map('gamma,[1,2,3,4,5,6,7,8,9]);
(%o1)        [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
(%i2) map('gamma,[1/2,3/2,5/2,7/2]);
                    sqrt(%pi)  3 sqrt(%pi)  15 sqrt(%pi)
(%o2)   [sqrt(%pi), ---------, -----------, ------------]
                        2           4            8
(%i3) map('gamma,[2/3,5/3,7/3]);
                                  2           1
                          2 gamma(-)  4 gamma(-)
                      2           3           3
(%o3)          [gamma(-), ----------, ----------]
                      3       3           9
```


Numerische Berechnung fur reelle und komplexe Argumente.



```maxima
(%i4) map('gamma,[2.5,2.5b0]);
(%o4)     [1.329340388179137, 1.3293403881791370205b0]
(%i5) map('gamma,[1.0+%i,1.0b0+%i]);
(%o5) [0.498015668118356 - .1549498283018107 %i, 
          4.9801566811835604272b-1 - 1.5494982830181068513b-1 %i]
```


`gamma` hat Spiegelsymmetrie.



```maxima
(%i6) declare(z,complex)$
(%i7) conjugate(gamma(z));
(%o7)                  gamma(conjugate(z))
```


Maxima entwickelt `gamma(z+n)` und `gamma(z-n)`, wenn die
Optionsvariable `gamma_expand` den Wert `true` hat.



```maxima
(%i8) gamma_expand:true$

(%i9) [gamma(z+1),gamma(z-1),gamma(z+2)/gamma(z+1)];

                               gamma(z)
(%o9)             [z gamma(z), --------, z + 1]
                                z - 1
```


Die Ableitung der Gammafunktion `gamma`.



```maxima
(%i10) diff(gamma(z),z);
(%o10)                  psi (z) gamma(z)
                           0
```

See also: `factlim`, `gammalim`, `gamma_expand`, `makegamma`, `%gamma`.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_expand -->
<!-- signatures: gamma_expand -->
### Variable: gamma_expand

Standardwert: `false`


Kontrolliert die Vereinfachung der Gammafunktion `gamma` und verwandte
Funktionen wie `gamma_incomplete` fur den Fall, dass das Argument die
Form `z+n` oder `z-n` hat.  Dabei ist `z` ist ein beliebiges
Argument und `n` ist eine ganze Zahl.


Siehe die Funktion `gamma` fur ein Beispiel.

See also: `gamma`, `gamma_incomplete`.

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete -->
<!-- signatures: gamma_incomplete(a, z) -->
### Function: gamma_incomplete (a, z)

Die unvollstandige Gammafunktion (A & S 6.5.2) die definiert ist als



$$
\int_{z}^{\infty }{t^{a-1}\,e^ {- t }\;dt}
$$


```maxima
inf
                 /
                 [     a - 1   - t
                 I    t      %e    dt
                 ]
                 /
                  z
```

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_generalized -->
<!-- signatures: gamma_incomplete_generalized(a, z1, z2) -->
### Function: gamma_incomplete_generalized (a, z1, z2)

Verallgemeinerte unvollstandige Gammafunktion



$$
\int_{z1}^{z2}{t^{a-1}\,e^ {- t }\;dt}
$$


```maxima
z2
                 /
                 [    a - 1   - t
                 I   t      %e    dt
                 ]
                 /
                  z1
```

<!-- category: SpecialFunctions -->
<!-- keywords: gamma_incomplete_regularized -->
<!-- signatures: gamma_incomplete_regularized(a, z) -->
### Function: gamma_incomplete_regularized (a, z)

Regularisierte unvollstandige Gammafunktion (A & S 6.5.1)



$$
{{{\it gamma\_incomplete}\left(a , z\right)}\over{\Gamma\left(a
 \right)}}
$$


```maxima
gamma_incomplete(a, z)
               ----------------------
                      gamma(a)
```

<!-- category: SpecialFunctions -->
<!-- keywords: gammalim -->
<!-- signatures: gammalim -->
### Variable: gammalim

Standardwert: 1000000


Kontrolliert die Vereinfachung der Gammafunktion fur rationale Argumente.
Ist der Betrag des Arguments der Gammafunktion großer als `gammalim`,
wird die Gammafunktion nicht vereinfacht.  Damit wird verhindert, dass
die Berechnung der Gammafunktion zu einem Uberlauf fuhrt und mit einem
Fehler abbricht.


Siehe auch die Optionsvariable `factlim`, um die Vereinfachung fur
ganze Zahlen zu kontrollieren.

See also: `factlim`.

<!-- category: SpecialFunctions -->
<!-- keywords: hankel_1 -->
<!-- signatures: hankel_1(v, z) -->
### Function: hankel_1 (v, z)

Die Hankel-Funktion der ersten Art der Ordnung $v$ mit dem Argument
$z$.  Siehe A & S 9.1.3.  `hankel_1` ist definiert als



```maxima
H1 (z) = J (z) + %i Y (z)
        v       v          v
```


$$
{\it H1}_{v}(z)=J_{v}(z)+i\,Y_{v}(z)
$$


Die Hankel-Funktion `hankel_1` ist fur das numerische und symbolische
Rechnen geeignet.


Maxima berechnet `hankel_1` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente Zahlen sind.  Die numerische
Berechnung fur große Gleitkommazahlen ist nicht implementiert.  In diesem
Fall gibt Maxima eine Substantivform zuruck.


Hat die Optionsvariable `besselexpand` den Wert `true`, werden
Hankel-Funktionen `hankel_1` mit einer halbzahligen Ordnung $v$ als
Sinus- und Kosinusfunktionen entwickelt.


Maxima kennt die Ableitung der Hankel-Funktion `hankel_1` nach dem zweiten
Argument `z`.


Siehe auch die Funktion `hankel_2` sowie die Bessel-Funktionen in
`Bessel-Funktionen`.


Beispiele:


Numerische Berechnung.



```maxima
(%i1) hankel_1(1, 0.5);
(%o1)       .2422684576748738 - 1.471472392670243 %i
(%i2) hankel_1(1, 0.5+%i);
(%o2)      - .2558287994862166 %i - 0.239575601883016
```


Fur eine komplex Ordnung kann Maxima keinen numerischen Wert berechnet.  Das
Ergebnis ist eine Substantivform.



```maxima
(%i3) hankel_1(%i, 0.5+%i);
(%o3)                hankel_1(%i, %i + 0.5)
```


Entwicklung der Hankel-Funktion `hankel_1`, wenn die Optionsvariable
`besselexpand` den Wert `true` hat.



```maxima
(%i4) hankel_1(1/2, z), besselexpand:true;
               sqrt(2) sin(z) - sqrt(2) %i cos(z)
(%o4)          ----------------------------------
                       sqrt(%pi) sqrt(z)
```


Ableitung der Hankel-Funktion `hankel_1` nach dem Argument *z*.  Die
Ableitung nach der Ordnung *v* ist nicht implementiert.  Maxima gibt eine
Substantivform zuruck.



```maxima
(%i5)  diff(hankel_1(v,z), z);
             hankel_1(v - 1, z) - hankel_1(v + 1, z)
(%o5)        ---------------------------------------
                                2
(%i6)  diff(hankel_1(v,z), v);
                       d
(%o6)                  -- (hankel_1(v, z))
                       dv
```

See also: `float`, `numer`, `besselexpand`, `hankel_2`, `Bessel-Funktionen`.

<!-- category: SpecialFunctions -->
<!-- keywords: hankel_2 -->
<!-- signatures: hankel_2(v, z) -->
### Function: hankel_2 (v, z)

Die Hankel-Funktion der zweiten Art der Ordnung $v$ mit dem Argument
$z$.  Siehe A & S 9.1.4.  `hankel_2` ist definiert als



```maxima
H2 (z) = J (z) - %i Y (z)
        v       v          v
```


$$
{\it H2}_{v}(z)=J_{v}(z)-i\,Y_{v}(z)
$$


Die Hankel-Funktion `hankel_2` ist fur das numerische und symbolische
Rechnen geeignet.


Maxima berechnet `hankel_2` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente Zahlen sind.  Die numerische
Berechnung fur große Gleitkommazahlen ist nicht implementiert.  In diesem
Fall gibt Maxima eine Substantivform zuruck.


Hat die Optionsvariable `besselexpand` den Wert `true`, werden
Hankel-Funktionen `hankel_2` mit einer halbzahligen Ordnung $v$ als
Sinus- und Kosinusfunktionen entwickelt.


Maxima kennt die Ableitung der Hankel-Funktion `hankel_2` nach dem zweiten
Argument `z`.


Fur Beispiele siehe `hankel_1`.  Siehe auch die Bessel-Funktionen in
`Bessel-Funktionen`.

See also: `float`, `numer`, `besselexpand`, `hankel_1`, `Bessel-Funktionen`.

<!-- category: SpecialFunctions -->
<!-- keywords: log_gamma -->
<!-- signatures: log_gamma(z) -->
### Function: log_gamma (z)

Der Logarithmus der Gammafunktion.

<!-- category: SpecialFunctions -->
<!-- keywords: makefact -->
<!-- signatures: makefact(expr) -->
### Function: makefact (expr)

Ersetzt Binomial-, Gamma- und Beta-Funktionen, die im Ausdruck *expr*
auftreten, durch Fakultaten.


Siehe auch die Funktion `makegamma`.

See also: `makegamma`.

<!-- category: SpecialFunctions -->
<!-- keywords: makegamma -->
<!-- signatures: makegamma(expr) -->
### Function: makegamma (expr)

Ersetzt Fakultaten sowie Binomial- und Betafunktionen durch die Gammafunktion
`gamma` im Ausdruck *expr*.


Siehe auch die Funktion `makefact`, um stattdessen Fakultaten in den
Ausdruck einzusetzen.


Beispiel:



```maxima
(%i1) expr: binomial(a,b)*gamma(b+1)/gamma(a+1);
                   binomial(a, b) gamma(b + 1)
(%o1)              ---------------------------
                          gamma(a + 1)
(%i2) makegamma(expr);
                               1
(%o2)                  ------------------
                       gamma(- b + a + 1)
```

See also: `gamma`, `makefact`.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsifracdenom -->
<!-- signatures: maxpsifracdenom -->
### Variable: maxpsifracdenom

Standardwert: `6`


Die Optionsvariable `maxpsifracdenom` kontrolliert die Vereinfachung der
Funktion `psi`.  Ist das Argument *x* der Funktion `psi` eine
rationale Zahl kleiner als eins mit `p/q` und ist der Nenner `q`
großer als `maxpsifracdenom`, dann versucht Maxima nicht
`psi[n](x)` zu vereinfachen.


Siehe auch `maxpsifracnum`, `maxpsiposint` und
`maxpsinegint`.


Beispiele:



```maxima
(%i1) maxpsifracdenom: 6;
(%o1)                           6
(%i2) psi[0](1/6);
            3 log(3)              sqrt(3) %pi
(%o2)     - -------- - 2 log(2) - ----------- - %gamma
               2                       2
(%i3) maxpsifracdenom: 4;
(%o3)                           4
(%i4) psi[0](1/6);

                                  1
(%o4)                        psi (-)
                                0 6

(%i5) psi[0](1/5);
                                  1
(%o5)                        psi (-)
                                0 5
(%i6) psi[0](1/4);
                                 %pi
(%o6)               - 3 log(2) - --- - %gamma
                                  2
```

See also: `psi`, `maxpsifracnum`, `maxpsiposint`, `maxpsinegint`.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsifracnum -->
<!-- signatures: maxpsifracnum -->
### Variable: maxpsifracnum

Standardwert: `6`


Die Optionsvariable `maxpsifracnum` kontrolliert die Vereinfachung der
Funktion `psi`.  Ist das Argument *x* der Funktion `psi` eine
rationale Zahl kleiner als eins mit `p/q` und ist der Zahler `p`
großer als `maxpsifracnum`, dann versucht Maxima nicht
`psi[n](x)` zu vereinfachen.


Siehe auch `maxpsifracdenom`, `maxpsiposint` und
`maxpsinegint`.


Beispiele:



```maxima
(%i1) maxpsifracnum: 6;
(%o1)                           6
(%i2) psi[0](5/6);
            3 log(3)              sqrt(3) %pi
(%o2)     - -------- - 2 log(2) + ----------- - %gamma
               2                       2
(%i3) maxpsifracnum: 3;
(%o3)                           3
(%i4) psi[0](5/6);
                                  5
(%o4)                        psi (-)
                                0 6
```

See also: `psi`, `maxpsifracdenom`, `maxpsiposint`, `maxpsinegint`.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsinegint -->
<!-- signatures: maxpsinegint -->
### Variable: maxpsinegint

Standardwert: `-10`


Die Optionsvariable `maxpsinegint` kontrolliert die Vereinfachung der
Funktion `psi` und enthalt eine untere negative Schranke.  Ist das
Argument *x* der Funktion `psi` kleiner als `maxpsinegint`,
dann versucht Maxima nicht `psi[n](x)` zu vereinfachen.


Siehe auch `maxpsifracdenom`, `maxpsifracnum` und
`maxpsiposint`.


Beispiele:



```maxima
(%i1) maxpsinegint:-10;
(%o1)                         - 10
(%i2) psi[0](-3/2);
                                           8
(%o2)                - 2 log(2) - %gamma + -
                                           3
(%i3) maxpsinegint:-1;
(%o3)                          - 1
(%i4) psi[0](-3/2);
                                   3
(%o4)                       psi (- -)
                               0   2
(%i5) psi[0](-1/2);
(%o5)                - 2 log(2) - %gamma + 2
```

See also: `psi`, `maxpsifracdenom`, `maxpsifracnum`, `maxpsiposint`.

<!-- category: SpecialFunctions -->
<!-- keywords: maxpsiposint -->
<!-- signatures: maxpsiposint -->
### Variable: maxpsiposint

Standardwert: `20`


Die Optionsvariable `maxpsiposint` kontrolliert die Vereinfachung der
Funktion `psi` und enthalt eine obere positive Schranke.  Ist das
Argument *x* der Funktion `psi` großer als `maxpsiposint`,
dann versucht Maxima nicht `psi[n](x)` zu vereinfachen.


Siehe auch `maxpsifracdenom`, `maxpsifracnum` und
`maxpsinegint`.


Beispiele:



```maxima
(%o1)                          20
(%i2) psi[0](20);
                       275295799
(%o2)                  --------- - %gamma
                       77597520
(%i3) maxpsiposint:10;
(%o3)                          10
(%i4) psi[0](20);
(%o4)                       psi (20)
                               0
(%i5) psi[0](10);
                          7129
(%o5)                     ---- - %gamma
                          2520
```

See also: `psi`, `maxpsifracdenom`, `maxpsifracnum`, `maxpsinegint`.

<!-- category: SpecialFunctions -->
<!-- keywords: numfactor -->
<!-- signatures: numfactor(expr) -->
### Function: numfactor (expr)

Gibt einen numerischen Faktor des Produktes *expr* zuruck.  Ist *expr*
kein Produkt oder enthalt das Produkt keinen numerischen Faktor ist die
Ruckgabe `1`.


Beispiel:



```maxima
(%i1) gamma (7/2);
                          15 sqrt(%pi)
(%o1)                     ------------
                               8
(%i2) numfactor (%);
                               15
(%o2)                          --
                               8
```

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i -->
<!-- signatures: scaled_bessel_i(v, z) -->
### Function: scaled_bessel_i (v, z)

Die skalierte modifizierte Bessel-Funktion der ersten Art der Ordnung
$v$ mit dem Argument $z$.  Diese ist definiert als



```maxima
- abs(z)
      scaled_bessel_i(v, z) = bessel_i(v, z) %e
```


`scaled_bessel_i` liefert ein numerisches Ergebnis, wenn die Argumente 
$v$ und $z$ Zahlen sind.  Die Funktion kann geeignet sein, wenn
`bessel_i` fur große Argumente $z$ numerisch berechnet werden
soll.  Ganze, rationale oder große Gleitkommazahlen werden in
Gleitkommazahlen mit doppelter Genauigkeit umgewandelt.  Sind die Argumente
keine Zahlen, wird ein vereinfachter Ausdruck mit der Funktion
`bessel_i` zuruckgegeben.


`scaled_bessel_i` ist eine Verbfunktion, die nicht fur das symbolische
Rechnen geeignet ist.  Fur das symbolische Rechnen ist die Funktion
`bessel_i` zu verwenden.


Beispiele:



```maxima
(%i1) scaled_bessel_i(1, 50);
(%o1)                  .05599312389289544
(%i2) scaled_bessel_i(1/2, 50);
(%o2)                  .05641895835477567
(%i3) scaled_bessel_i(v, x);
                                     - abs(x)
(%o3)               bessel_i(v, x) %e
```

See also: `bessel_i`.

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i0 -->
<!-- signatures: scaled_bessel_i0(z) -->
### Function: scaled_bessel_i0 (z)

Entspricht `scaled_bessel_i(0,z)`.  Siehe `scaled_bessel_i`.

See also: `scaled_bessel_i`.

<!-- category: SpecialFunctions -->
<!-- keywords: scaled_bessel_i1 -->
<!-- signatures: scaled_bessel_i1(z) -->
### Function: scaled_bessel_i1 (z)

Entspricht `scaled_bessel_i(1,z)`.  Siehe `scaled_bessel_i`.

See also: `scaled_bessel_i`.

<!-- category: SpecialFunctions -->
<!-- keywords: struve_h -->
<!-- signatures: struve_h(v, z) -->
### Function: struve_h (v, z)

Die Struve-Funktion $H$ der Ordnung $v$ mit dem Argument
$z$.  Siehe Abramowitz und Stegun, Handbook of Mathematical Functions,
Kapitel 12.  Die Definition ist



```maxima
inf
                       ====                  k  2 k
               z v + 1 \                (- 1)  z
      H (z) = (-)       >    ----------------------------------
       v       2       /      2 k           3                3
                       ====  2    gamma(k + -) gamma(v + k + -)
                       k = 0                2                2
```


$$
H_{v}(z)=\left({{z}\over{2}}\right)^{v+1}\,\sum_{k=0}^{\infty }{{{\left(-1
 \right)^{k}\,z^{2\,k}}\over{2^{2\,k}\,\Gamma\left(k+{{3}\over{2}}
 \right)\,\Gamma\left(v+k+{{3}\over{2}}\right)}}}
$$


Die Struve-Funktion `struve_h` ist fur das numerische und symbolische
Rechnen geeignet.  Im Unterschied zu den Bessel-Funktionen ist jedoch
die Implementation der Funktion `struve_h` weniger vollstandig.


Maxima berechnet `struve_h` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente Zahlen sind.  Die numerische
Berechnung fur große Gleitkommazahlen ist nicht implementiert.  In diesem
Fall gibt Maxima eine Substantivform zuruck.


Hat die Optionsvariable `besselexpand` den Wert `true`, wird die
Struve-Funktion `struve_h` mit einer halbzahligen Ordnung $v$ als
Sinus- und Kosinusfunktionen entwickelt.


Maxima kennt die Ableitung der Struve-Funktion `struve_h` nach dem
Argument $z$.


Siehe auch die Struve-Funktion `struve_l`.


Beispiele:



```maxima
(%i1) struve_h(1, 0.5);
(%o1)                  .05217374424234107
(%i2) struve_h(1, 0.5+%i);
(%o2)       0.233696520211436 %i - .1522134290663428
(%i3) struve_h(3/2,x), besselexpand: true;
                                           2
                  2 x sin(x) + 2 cos(x) - x  - 2
(%o3)           - ------------------------------
                                         3/2
                      sqrt(2) sqrt(%pi) x
(%i4) diff(struve_h(v, x), x);
                   v
                  x
(%o4) (------------------------- - struve_h(v + 1, x)
                  v           3
       sqrt(%pi) 2  gamma(v + -)
                              2
                                          + struve_h(v - 1, x))/2
```

See also: `float`, `numer`, `besselexpand`, `struve_l`.

<!-- category: SpecialFunctions -->
<!-- keywords: struve_l -->
<!-- signatures: struve_l(v, z) -->
### Function: struve_l (v, z)

Die modifizierte Struve-Funktion $L$ der Ordnung $v$ mit dem Argument
$z$.  Siehe Abramowitz und Stegun, Handbook of Mathematical Functions, 
Kapitel 12.  Die Definition ist



```maxima
inf
                       ====                  2 k
               z v + 1 \                    z
      L (z) = (-)       >    ----------------------------------
       v       2       /      2 k           3                3
                       ====  2    gamma(k + -) gamma(v + k + -)
                       k = 0                2                2
```


$$
L_{v}(z)=\left({{z}\over{2}}\right)^{v+1}\,\sum_{k=0}^{\infty }{{{z^{2\,k}
 }\over{2^{2\,k}\,\Gamma\left(k+{{3}\over{2}}\right)\,\Gamma\left(v+k
 +{{3}\over{2}}\right)}}}
$$


Die Struve-Funktion `struve_l` ist fur das numerische und symbolische
Rechnen geeignet.  Im Unterschied zu den Bessel-Funktionen ist jedoch
die Implementation der Funktion `struve_l` weniger vollstandig.


Maxima berechnet `struve_l` numerisch fur reelle und komplexe
Gleitkommazahlen als Argumente fur $v$ und $z$.  Mit der Funktion
`float` oder der Optionsvariablen `numer` kann die numerische
Auswertung erzwungen werden, wenn die Argumente Zahlen sind.  Die numerische
Berechnung fur große Gleitkommazahlen ist nicht implementiert.  In diesem
Fall gibt Maxima eine Substantivform zuruck.


Hat die Optionsvariable `besselexpand` den Wert `true`, wird die
Struve-Funktion `struve_l` mit einer halbzahligen Ordnung $v$ als
Sinus- und Kosinusfunktionen entwickelt.


Maxima kennt die Ableitung der Struve-Funktion `struve_l` nach dem
Argument $z$.


Siehe auch die Struve-Funktion `struve_h`.


Beispiele:



```maxima
(%i1) struve_l(1, 0.5);
(%o1)                  .05394218262352267
(%i2) struve_l(1, 0.5+%i);
(%o2)       .1912720461247995 %i - .1646185598117401
(%i3) struve_l(3/2,x), besselexpand: true;
                                           2
                2 x sinh(x) - 2 cosh(x) - x  + 2
(%o3)           --------------------------------
                                        3/2
                     sqrt(2) sqrt(%pi) x
(%i4) diff(struve_l(v, x), x);
                   v
                  x
(%o4) (------------------------- + struve_l(v + 1, x)
                  v           3
       sqrt(%pi) 2  gamma(v + -)
                              2
                                          + struve_l(v - 1, x))/2
```

See also: `float`, `numer`, `besselexpand`, `struve_h`.

