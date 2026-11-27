## Zahlentheorie

<!-- category: Other -->
<!-- keywords: bern -->
<!-- signatures: bern(n) -->
### Function: bern (n)

Gibt die *n*-te Bernoulli-Zahl der ganzen Zahl *n* zuruck. Hat die
Optionsvariable `zerobern` den Wert `false`, werden Bernoulli-Zahlen
unterdruckt, die Null sind.


Siehe auch `burn`.



```maxima
(%i1) zerobern: true$

(%i2) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                  1  1       1      1        1
(%o2)       [1, - -, -, 0, - --, 0, --, 0, - --]
                  2  6       30     42       30

(%i3) zerobern: false$
(%i4) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
            1  1    1   5     691   7    3617  43867
(%o4) [1, - -, -, - --, --, - ----, -, - ----, -----]
            2  6    30  66    2730  6    510    798
```

See also: `burn`.

<!-- category: Other -->
<!-- keywords: bernpoly -->
<!-- signatures: bernpoly(x, n) -->
### Function: bernpoly (x, n)

Gibt das *n*-te Bernoulli-Polynom in der Variablen *x* zuruck.

<!-- category: Other -->
<!-- keywords: bfhzeta -->
<!-- signatures: bfhzeta(s, h, n) -->
### Function: bfhzeta (s, h, n)

Die Hurwitzsche Zeta-Funktion fur die Argumente *s* und *h*, die wie
folgt definiert ist:



$$
\zeta \left(s,h\right) = \sum_{k=0}^\infty {1 \over \left(k+h\right)^{s}}
$$


```maxima
inf
                        ====
                        \        1
         zeta (s,h)  =   >    --------
                        /            s
                        ====  (k + h)
                        k = 0
```


`bfhzeta` gibt einen Wert als große Gleitkommazahl zuruck.  Die 
Anzahl der Stellen wird durch das Argument *n* angegeben.

<!-- category: Other -->
<!-- keywords: bfzeta -->
<!-- signatures: bfzeta(s, n) -->
### Function: bfzeta (s, n)

Die Riemannsche Zeta-Funktion fur das Argument *s*, die wie folgt 
definiert ist:



$$
\zeta\left(s\right)=\sum_{k=1}^{\infty }{{{1}\over{k^{s}}}}
$$


```maxima
inf
                 ====
                 \     1
     zeta(s) =    >    --
                 /      s
                 ====  k
                 k = 1
```


`bfzeta` gibt einen Wert als große Gleitkommazahl zuruck.  Die Anzahl 
der Stellen wird durch das Argument *n* angegeben.


Anstatt der Funktion `bfzeta` ist die Funktion `zeta` zu bevorzugen,
die sowohl fur reelle und komplexe Gleitkommazahlen und Gleitkommazahlen mit
eine beliebigen Genauigkeit die Riemannsche Zeta-Funktion berechnen kann.

See also: `zeta`.

<!-- category: Other -->
<!-- keywords: burn -->
<!-- signatures: burn(n) -->
### Function: burn (n)

Gibt eine rational Zahl zuruck, die eine Naherung fur die *n*-te 
Bernoulli Zahl fur die ganze Zahl *n* ist.  `burn` berechnet eine 
Naherung als große Gleitkommatzahl mit der folgenden Beziehung:



```maxima
n - 1  1 - 2 n
              (- 1)      2        zeta(2 n) (2 n)!
     B(2 n) = ------------------------------------
                                2 n
                             %pi
```








`burn` kann effizienter als die Funktion `bern` fur große, 
einzelne ganze Zahlen *n* sein, da `bern` zunachst alle Bernoulli 
Zahlen bis *n* berechnet.  `burn` ruft fur ungerade ganze Zahlen und 
Zahlen die kleiner oder gleich 255 die Funktion `bern` auf.




Das Kommando `load("bffac")` ladt die Funktion.  Siehe auch `bern`.

See also: `bern`.

<!-- category: Other -->
<!-- keywords: chinese -->
<!-- signatures: chinese([r_1, ..., r_n], [m_1, ..., m_n]) -->
### Function: chinese ([r_1, ..., r_n], [m_1, ..., m_n])

Lost die simultanen Kongruenzen `x = r_1 mod m_1`, ..., `x = r_n mod m_n`.
Die Reste *r_n* und die Moduli *m_n* mussen ganze Zahlen sein, 
die Moduli zusatzlich positiv und paarweise teilerfremd.



```maxima
(%i1) mods : [1000, 1001, 1003, 1007];
(%o1)                   [1000, 1001, 1003, 1007]
(%i2) lreduce('gcd, mods);
(%o2)                               1
(%i3) x : random(apply("*", mods));
(%o3)                         685124877004
(%i4) rems : map(lambda([z], mod(x, z)), mods);
(%o4)                       [4, 568, 54, 624]
(%i5) chinese(rems, mods);
(%o5)                         685124877004
(%i6) chinese([1, 2], [3, n]);
(%o6)                    chinese([1, 2], [3, n])
(%i7) %, n = 4;
(%o7)                              10
```

<!-- category: Other -->
<!-- keywords: divsum -->
<!-- signatures: divsum(n, k), divsum(n) -->
### Function: divsum (n, k)

`divsum(n, k)` potenziert die Teiler des Argumentes *n* 
mit dem Argument *k* und gibt die Summe als Ergebnis zuruck.




`divsum(n)` gibt die Summe der Teiler der Zahl *n* zuruck.



```maxima
(%i1) divsum (12);
(%o1)                          28
(%i2) 1 + 2 + 3 + 4 + 6 + 12;
(%o2)                          28
(%i3) divsum (12, 2);
(%o3)                          210
(%i4) 1^2 + 2^2 + 3^2 + 4^2 + 6^2 + 12^2;
(%o4)                          210
```

<!-- category: Other -->
<!-- keywords: euler -->
<!-- signatures: euler(n) -->
### Function: euler (n)

Gibt die *n*-te Eulersche Zahl fur eine nichtnegative ganze Zahl *n*
zuruck.




Fur die Euler-Mascheroni Konstante siehe `%gamma`.


Beispiele:



```maxima
(%i1) map (euler, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1)    [1, 0, - 1, 0, 5, 0, - 61, 0, 1385, 0, - 50521]
```

See also: `%gamma`.

<!-- category: Other -->
<!-- keywords: factors_only -->
<!-- signatures: factors_only -->
### Variable: factors_only

Standardwert: `false`


Hat `factors_only` den Standardwert `false`, werden von der 
Funktion `ifactors` zusammen mit den berechneten Primfaktoren auch deren 
Multiplizitaten angegeben. Hat `factors_only` den Wert `true`, 
werden nur die Primfaktoren zuruck gegeben.


Beispiel: Siehe `ifactors`.

See also: `ifactors`.

<!-- category: Other -->
<!-- keywords: fib -->
<!-- signatures: fib(n) -->
### Function: fib (n)

Gibt die *n*-te Fibonacci-Zahl zuruck.  Die Fibonacci-Folge ist rekursiv 
definiert:



```maxima
fib(0) = 0
   fib(1) = 1
   fib(n) = fib(n-1) + fib(n-2)
```


Fur negative ganze Zahlen kann die Fibonacci-Folge wie folgt erweitert werden:



```maxima
n + 1
   fib(- n) = (- 1)      fib(n)
```
 






Nach einem Aufruf der Funktion `fib(n)`, enthalt die Systemvariable 
`prevfib` die zur Zahl `n` vorhergehende Fibonacci-Zahl.



```maxima
(%i1) map (fib, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o1)         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

<!-- category: Other -->
<!-- keywords: fibtophi -->
<!-- signatures: fibtophi(expr) -->
### Function: fibtophi (expr)

Fibonacci-Zahlen im Ausdruck *expr* werden durch die Goldene Zahl 
`%phi` ausgedruckt.  Siehe `%phi`.


Beispiele:



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

See also: `%phi`.

<!-- category: Other -->
<!-- keywords: ifactors -->
<!-- signatures: ifactors(n) -->
### Function: ifactors (n)

Faktorisiert eine positive ganze Zahl *n*.  Sind `n = p1^e1 * ... * pk^nk` die
Faktoren der ganzen Zahl *n*, dann gibt `ifactor` das Ergebnis
`[[p1, e1], ..., [pk, ek]]` zuruck.


Fur die Faktorisierung kommen Probedivisionen mit Primzahlen bis 9973, 
Pollards Rho- und p-1-Methode oder Elliptischen Kurven zum Einsatz.


Die Ruckgabe von ifactors wird von der Optionsvariablen `factors_only`  
beeinflusst. 
Werden lediglich die Primfaktoren ohne ihre Multiplizitat benotigt, 
genugt es hierfur, `factors_only : true` zu setzen.



```maxima
(%i1) ifactors(51575319651600);
(%o1)     [[2, 4], [3, 2], [5, 2], [1583, 1], [9050207, 1]]
(%i2) apply("*", map(lambda([u], u[1]^u[2]), %));
(%o2)                        51575319651600
(%i3) ifactors(51575319651600), factors_only : true;
(%o3)                   [2, 3, 5, 1583, 9050207]
```

See also: `factors_only`.

<!-- category: Other -->
<!-- keywords: igcdex -->
<!-- signatures: igcdex(n, k) -->
### Function: igcdex (n, k)

Gibt die Liste `[a, b, u]` zuruck, in der `u` der 
großte gemeinsame Teiler von *n* und *k* ist und in der zusatzlich 

gilt, dass `u = a * n + b * k`. 


`igcdex` verwendet den Euklidischen Algorithmus.  Siehe auch `gcdex`.


Die Eingabe `load("gcdex")` ladt diese Funktion.


Beispiele:



```maxima
(%i1) load("gcdex")$

(%i2) igcdex(30, 18);
(%o2)                      [- 1, 2, 6]
(%i3) igcdex(1526757668, 7835626735736);
(%o3)            [845922341123, - 164826435, 4]
(%i4) igcdex(fib(20), fib(21));
(%o4)                   [4181, - 2584, 1]
```

See also: `gcdex`.

<!-- category: Other -->
<!-- keywords: inrt -->
<!-- signatures: inrt(x, n) -->
### Function: inrt (x, n)

Gibt die ganzzahlige *n*-te Wurzel des Betrags von *x* zuruck.



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], inrt (10^a, 3)), l);
(%o2) [2, 4, 10, 21, 46, 100, 215, 464, 1000, 2154, 4641, 10000]
```

<!-- category: Other -->
<!-- keywords: inv_mod -->
<!-- signatures: inv_mod(n, m) -->
### Function: inv_mod (n, m)

Berechnet das modulare Inverse von *n* zum Modul *m*.  Das Argument
*n* muss eine ganze Zahl und der Modul *p* eine positive ganze Zahl 
sein.  `inv_mod(n, m)` gibt `false` zuruck, wenn das modulare Inverse
nicht existiert.  Das modulare Inverse existiert, wenn *n* teilerfremd zum 
Modul *m* ist.


Siehe auch die Funktionen `power_mod` und `mod`.


Beispiele:



```maxima
(%i1) inv_mod(3, 41);
(%o1)                           14
(%i2) ratsimp(3^-1), modulus = 41;
(%o2)                           14
(%i3) inv_mod(3, 42);
(%o3)                          false
```

See also: `power_mod`, `mod`.

<!-- category: Other -->
<!-- keywords: isqrt -->
<!-- signatures: isqrt(x) -->
### Function: isqrt (x)

Gibt die ganzzahlige Wurzel des Betrages von *x* zuruck, wenn *x* eine
ganze Zahl ist.  Andernfalls wird eine Substantivform zuruckgegeben.

<!-- category: Other -->
<!-- keywords: jacobi -->
<!-- signatures: jacobi(p, q) -->
### Function: jacobi (p, q)

Berechnet das Jacobi-Symbol fur die Argumente *p* und *q*.



```maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$
(%i2) map (lambda ([a], jacobi (a, 9)), l);
(%o2)         [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
```

<!-- category: Other -->
<!-- keywords: lcm -->
<!-- signatures: lcm(expr_1, ..., expr_n) -->
### Function: lcm (expr_1, ..., expr_n)

Gibt das kleinste gemeinsame Vielfache der Argumente zuruck.  Die Argumente 
konnen ganze Zahlen und allgemeine Ausdrucke sein.




Mit dem Kommando `load("functs")` wird die Funktion geladen.

<!-- category: Other -->
<!-- keywords: lucas -->
<!-- signatures: lucas(n) -->
### Function: lucas (n)

Gibt die *n*-te Lucas-Zahl zuruck.  Die Lucas-Folge ist rekursiv 
definiert:



```maxima
lucas(0) = 0
   lucas(1) = 1
   lucas(n) = lucas(n-1) + lucas(n-2)
```


Fur negative ganze Zahlen kann die Lucas-Folge wie folgt erweitert werden:



```maxima
-n
   lucas(- n) = (- 1)   lucas(n)
```
 


```maxima
(%i1) map (lucas, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o1)             [7, - 4, 3, - 1, 2, 1, 3, 4, 7, 11, 18, 29, 47]
```


Nach einem Aufruf von `lucas` enthalt die globale Variable 
`next_lucas` den Nachfolger der zuletzt zurck gegebenen Lucas-Zahl.
Das Beispiel zeigt, wie Fibonacci-Zahlen mit Hilfe von `lucas` 
und `next_lucas` berechnet werden konnen.



```maxima
(%i1) fib_via_lucas(n) := 
         block([lucas : lucas(n)],
         signum(n) * (2*next_lucas - lucas)/5 )$
(%i2) map (fib_via_lucas, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o2)             [- 3, 2, - 1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
```

<!-- category: Other -->
<!-- keywords: mod -->
<!-- signatures: mod(x, p) -->
### Function: mod (x, p)

Berechnet den Divisionsrest `x mod y` des Arguments *x* zum Modul *y*. 
*x* und *y* konnen ganze Zahlen, rationale Zahlen, Gleitkommazahlen 
oder allgemeine Ausdrucke sein.


Sind *x* und *y* reelle Zahlen und ist *y* ungleich Null, gibt 
`mod(x, y)` das Ergebnis von `x - y * floor(x / y)` zuruck.  Weiterhin gilt fur alle reellen Zahlen
`mod(x, 0) = x`.  Fur eine Diskussion dieser Definition siehe
Kapitel 3.4, "Concrete Mathematics" von Graham, Knuth, and Patashnik.  Die 
Funktion `mod(x, 1)` ist eine Sagezahnfunktion mit der Periode 1 
mit `mod(1, 1) = 0` und `mod(0, 1) = 0`.






Der Hauptwert einer komplexen Zahl, die im Intervall `(-%pi, %pi)` liegt,
kann mit `%pi - mod(%pi - x, 2*%pi)` bestimmt werden, wobei *x*
die komplexe Zahl ist.







Sind *x* und *y* konstante Ausdrucke, wie zum Beispiel `10 * %pi`,
verwendet `mod` dasselbe `bfloat`-Auswertungsschema wie `floor` 
und `ceiling`. Diese Umwandlung kann, wenn auch unwahrscheinlich, 
zu Fehlern fuhren.





Fur nicht numerische Argumente *x* oder *y* kennt `mod`
verschiedene Vereinfachungen.


Siehe auch die Funktionen `power_mod` und `inv_mod`.


Beispiele:


Zeige fur zwei große ganze Zahlen, dass fur das modulare Rechnen die 
Regel `mod(a+b, m) = mod(mod(a, m) + mod(b, m), m)` gilt.



```maxima
(%i1) a : random(10^20) + 10^19;
(%o1)                 72588919020045581148
(%i2) b : random(10^20) + 10^19;
(%o2)                 35463666253140008825
(%i3) m : random(10^20) + 10^19;
(%o3)                 39127433614020247557
(%i4) mod(a+b, m);
(%o4)                 29797718045145094859
(%i5) mod(mod(a, m) + mod(b, m), m);
(%o5)                 29797718045145094859
```


Vereinfachung fur nicht numerische Argumente.



```maxima
(%i1) mod (x, 0);
(%o1)                           x
(%i2) mod (a*x, a*y);
(%o2)                      a mod(x, y)
(%i3) mod (0, x);
(%o3)                           0
```

See also: `bfloat`, `power_mod`, `inv_mod`.

<!-- category: Other -->
<!-- keywords: next_prime -->
<!-- signatures: next_prime(n) -->
### Function: next_prime (n)

Gibt die kleinste Primzahl zuruck, die der Zahl *n* folgt.



```maxima
(%i1) next_prime(27);
(%o1)                       29
```

<!-- category: Other -->
<!-- keywords: power_mod -->
<!-- signatures: power_mod(a, n, m) -->
### Function: power_mod (a, n, m)

Verwendet einen modularen Algorithmus, um `a^n mod m` zu berechnen. 
Die Argumente *a* und *n* mussen ganze Zahlen und der Modul *m* 
eine positive ganze Zahl sein.  Ist *n* negativ, wird `inv_mod` zur 
Berechnung des modularen Inversen aufgerufen.


`power_mod (a, n, m)` ist aquivalent zu 
`mod(a^n, m)`.  Der Algorithmus von `power_mod` ist jedoch 
insbesondere fur große ganze Zahlen wesentlich effizienter.


Siehe auch die Funktionen `inv_mod` und `mod`.


Beispiele:


`power_mod(a, n, m)` ist aquivalent zu `mod(a^n, m`.  Das modulare
Inverse wird mit der Funktion `inv_mod` berechnet.



```maxima
(%i1) power_mod(3, 15, 5);
(%o1)                          2
(%i2) mod(3^15, 5);
(%o2)                          2
(%i3) power_mod(2, -1, 5);
(%o3)                          3
(%i4) inv_mod(2, 5);
(%o4)                          3
```


Fur große ganze Zahlen ist `power_mod` effizienter.  Der folgende 
Wert kann in keiner vernunftigen Zeit mit `mod(a^n, m)` berechnet
werden.



```maxima
(%i1) power_mod(123456789, 123456789, 987654321);
(%o1)                       598987215
```

See also: `inv_mod`, `mod`.

<!-- category: Other -->
<!-- keywords: prev_prime -->
<!-- signatures: prev_prime(n) -->
### Function: prev_prime (n)

Gibt die großte Primzahl zuruck, die kleiner als die Zahl *n* ist.



```maxima
(%i1) prev_prime(27);
(%o1)                       23
```

<!-- category: Other -->
<!-- keywords: primep -->
<!-- signatures: primep(n) -->
### Function: primep (n)

Fuhrt einen Primzahltest fur das Argument *n* durch.  Liefert
`primep` das Ergebnis `false`, ist *n* keine Primzahl.  Ist das
Ergebnis `true`, ist *n* mit sehr großer Wahrscheinlichkeit eine 
Primzahl.


Fur ganze Zahlen *n* kleiner als 3317044064679887385961981 wird eine deterministische
Variante des Miller-Rabin-Tests angewandt.  Hat in diesem Fall `primep` den Wert
`true`, dann ist *n* mit Sicherheit eine Primzahl.


Fur ganze Zahlen *n* großer 3317044064679887385961981 fuhrt `primep`
`primep_number_of_tests` Pseudo-Primzahl-Tests nach Miller-Rabin und 
einen Pseudo-Primzahl-Test nach Lucas durch.  Die Wahrscheinlichkeit, dass 
eine zusammen gesetzte Zahl *n* einen Miller-Rabin-Test besteht, ist kleiner
als 1/4.  Mit dem Standardwert 25 `primpe_number_of_tests` sinkt diese 
Wahrscheinlichkeit damit unter einen Wert von 10^-15.

See also: `primep_number_of_tests`.

<!-- category: Other -->
<!-- keywords: primep_number_of_tests -->
<!-- signatures: primep_number_of_tests -->
### Variable: primep_number_of_tests

Standardwert: 25




Die Anzahl der Pseudo-Primzahl-Tests nach Miller-Rabin in der Funktion 
`primep`.

See also: `primep`.

<!-- category: Other -->
<!-- keywords: primes -->
<!-- signatures: primes(start, end) -->
### Function: primes (start, end)

Gibt eine Liste mit allen Primzahlen von *start* bis *end* zuruck.



```maxima
(%i1) primes(3, 7);
(%o1)                     [3, 5, 7]
```

<!-- category: Other -->
<!-- keywords: qunit -->
<!-- signatures: qunit(n) -->
### Function: qunit (n)

Findet fur das Argument *n* Losungen der Pellschen Gleichung 
`a^2 - n b^2 = 1`.



```maxima
(%i1) qunit (17);
(%o1)                     sqrt(17) + 4
(%i2) expand (% * (sqrt(17) - 4));
(%o2)                           1
```

<!-- category: Other -->
<!-- keywords: totient -->
<!-- signatures: totient(n) -->
### Function: totient (n)

Gibt die Anzahl der ganzen Zahlen zuruck, die kleiner oder gleich *n*
und teilerfremd zu *n* sind.

<!-- category: Other -->
<!-- keywords: zerobern -->
<!-- signatures: zerobern -->
### Variable: zerobern

Standardwert: `true`






Hat `zerobern` den Wert `false`, werden von den Funktionen `bern`
diejenigen Bernoulli-Zahlen und von `euler` diejenigen Euler-Zahlen 
ausgeschlossen, die gleich Null sind.  Siehe `bern` und `euler`.

See also: `bern`, `euler`.

<!-- category: Other -->
<!-- keywords: zeta -->
<!-- signatures: zeta(n) -->
### Function: zeta (n)

Die Riemannsche Zeta-Funktion fur *s*, die wie folgt definiert ist:



$$
\zeta\left(s\right)=\sum_{k=1}^{\infty }{{{1}\over{k^{s}}}}
$$


```maxima
inf
                 ====
                 \     1
     zeta(s) =    >    --
                 /      s
                 ====  k
                 k = 1
```


Fur negative ganze Zahlen *n*, Null und positive gerade ganze Zahlen 
wird `zeta` zu einem exakten Ergebnis vereinfacht.  
Damit diese Vereinfachung fur positive ganze Zahlen ausgefuhrt wird, 
muss die Optionsvariable `zeta%pi` den Wert `true` haben.  
Siehe `zeta%pi`. Fur einfache und beliebig genaue Gleitkommazahlen 
(Typ `bfloat`) hat `zeta` ein numerisches Ergebnis.  
Fur alle anderen Argumente einschließlich der komplexen und 
rationalen Zahlen gibt `zeta` eine Substantivform zuruck.  Hat die 
Optionsvariable `zeta%pi` den Wert `false`, gibt `zeta` auch 
fur gerade ganze Zahlen eine Substantivform zuruck.





`zeta(1)` ist nicht definiert.  Maxima kennt jedoch die einseitigen
Grenzwerte `limit(zeta(x), x, 1, plus` und 
`limit(zeta(x), x, 1, minus`.




Die Riemannsche Zeta-Funktion wird auf die Argumente von Listen, Matrizen und 
Gleichungen angewendet, wenn die Optionsvariable `distribute_over`
den Wert `true` hat.




Siehe auch `bfzeta` und `zeta%pi`.


Beispiele:



```maxima
(%i1) zeta([-2,-1,0,0.5,2,3,1+%i]);
                                             2
            1     1                       %pi
(%o1) [0, - --, - -, - 1.460354508809586, ----, zeta(3), 
            12    2                        6
                                                    zeta(%i + 1)]
(%i2) limit(zeta(x),x,1,plus);
(%o2)                          inf
(%i3) limit(zeta(x),x,1,minus);
(%o3)                         minf
```

See also: `zeta%pi`, `bfzeta`.

<!-- category: Other -->
<!-- keywords: zeta%pi -->
<!-- signatures: zeta%pi -->
### Variable: zeta%pi

Standardwert: `true`






Hat `zeta%pi` den Wert `true`, vereinfacht die Funktion `zeta(n)`
fur gerade ganzen Zahlen *n* zu einem Ergebnis, das proportional zu 
`%pi^n` ist.  Ansonsten ist das Ergebnis von `zeta` eine 
Substantivform fur gerade ganze Zahlen.


Beispiele:



```maxima
(%i1) zeta%pi: true$
(%i2) zeta (4);
                                 4
                              %pi
(%o2)                         ----
                               90
(%i3) zeta%pi: false$
(%i4) zeta (4);
(%o4)                        zeta(4)
```

<!-- category: Other -->
<!-- keywords: zn_add_table -->
<!-- signatures: zn_add_table(n) -->
### Function: zn_add_table (n)

zeigt eine Additionstabelle von allen Elementen in (Z/*n*Z).


Siehe auch `zn_mult_table`, `zn_power_table`.

See also: `zn_mult_table`, `zn_power_table`.

<!-- category: Other -->
<!-- keywords: zn_carmichael_lambda -->
<!-- signatures: zn_carmichael_lambda(n) -->
### Function: zn_carmichael_lambda (n)

Gibt `1` zuruck, wenn *n* gleich `1` ist und andernfalls 
den großten charakteristischen Faktor des Totienten von *n*. 


Fur Erlauterungen und Beispiele siehe `zn_characteristic_factors`.

See also: `zn_characteristic_factors`.

<!-- category: Other -->
<!-- keywords: zn_characteristic_factors -->
<!-- signatures: zn_characteristic_factors(n) -->
### Function: zn_characteristic_factors (n)

Gibt eine Liste mit den charakteristischen Faktoren des Totienten von *n* zuruck.


Mit Hilfe der charakteristischen Faktoren kann eine modulo *n* multiplikative Gruppe 
als direktes Produkt zyklischer Untergruppen dargestellt werden. 


Ist die Gruppe selbst zyklisch, dann enthalt die Liste nur den Totienten 
und mit `zn_primroot` kann ein Generator berechnet werden. 
Zerfallt der Totient in mehrere charakteristische Faktoren, 
konnen Generatoren der entsprechenden Untergruppen mit `zn_factor_generators` 
ermittelt werden.


Jeder der `r` Faktoren in der Liste teilt die weiter rechts stehenden Faktoren. 
Fuer den letzten Faktor `f_r` gilt daher `a^f_r = 1 (mod n)` 
fur alle `a` teilerfremd zu *n*. 
Dieser Faktor ist auch als Carmichael Funktion bzw. Carmichael Lambda bekannt.


Fur `n > 2` ist `totient(n)/2^r` die Anzahl der quadratischen Reste 
in der Gruppe und jeder dieser Reste hat `2^r` Wurzeln.


Siehe auch `totient`, `zn_primroot`, `zn_factor_generators`.


Beispiele:


Die multiplikative Gruppe modulo `14` ist zyklisch und ihre `6` Elemente 
lassen sich durch eine Primitivwurzel erzeugen.



```maxima
(%i1) [zn_characteristic_factors(14), phi: totient(14)];
(%o1)                              [[6], 6]
(%i2) [zn_factor_generators(14), g: zn_primroot(14)];
(%o2)                              [[3], 3]
(%i3) M14: makelist(power_mod(g,i,14), i,0,phi-1);
(%o3)                         [1, 3, 9, 13, 11, 5]
```


Die multiplikative Gruppe modulo `15` ist nicht zyklisch und ihre `8` Elemente 
lassen sich mit Hilfe zweier Faktorgeneratoren erzeugen.



```maxima
(%i1) [[f1,f2]: zn_characteristic_factors(15), totient(15)];
(%o1)                             [[2, 4], 8]
(%i2) [[g1,g2]: zn_factor_generators(15), zn_primroot(15)];
(%o2)                           [[11, 7], false]
(%i3) UG1: makelist(power_mod(g1,i,15), i,0,f1-1);
(%o3)                               [1, 11]
(%i4) UG2: makelist(power_mod(g2,i,15), i,0,f2-1);
(%o4)                            [1, 7, 4, 13]
(%i5) M15: create_list(mod(i*j,15), i,UG1, j,UG2);
(%o5)                      [1, 7, 4, 13, 11, 2, 14, 8]
```


Fur den letzten charakteristischen Faktor `4` gilt 
`a^4 = 1 (mod 15)` fuer alle `a` in `M15`. 


`M15` hat `2` charakteristische Faktoren und daher die `8/2^2` 
quadratischen Reste `1` und `4`, und diese haben jeweils `2^2` Wurzeln.



```maxima
(%i6) zn_power_table(15);
                               [ 1   1  1   1 ]
                               [              ]
                               [ 2   4  8   1 ]
                               [              ]
                               [ 4   1  4   1 ]
                               [              ]
                               [ 7   4  13  1 ]
(%o6)                          [              ]
                               [ 8   4  2   1 ]
                               [              ]
                               [ 11  1  11  1 ]
                               [              ]
                               [ 13  4  7   1 ]
                               [              ]
                               [ 14  1  14  1 ]
(%i7) map(lambda([i], zn_nth_root(i,2,15)), [1,4]);
(%o7)                   [[1, 4, 11, 14], [2, 7, 8, 13]]
```

See also: `totient`, `zn_primroot`, `zn_factor_generators`.

<!-- category: Other -->
<!-- keywords: zn_determinant -->
<!-- signatures: zn_determinant(matrix, p) -->
### Function: zn_determinant (matrix, p)

verwendet die Technik der LR-Dekomposition, um die Determinante der 
Matrix *matrix* uber (Z/*p*Z) zu berechnen, wobei *p* 
eine Primzahl sein muss. 


Ist die Determinante nicht von Null verschieden, kann es sein, dass die 
LR-Dekomposition nicht moglich ist. `zn_determinant` berechnet 
diesem Fall die Determinante nicht-modular und reduziert im Nachhinein.


Siehe auch `zn_invert_by_lu`.


Beispiel:



```maxima
(%i1) m : matrix([1,3],[2,4]);
                                [ 1  3 ]
(%o1)                           [      ]
                                [ 2  4 ]
(%i2) zn_determinant(m, 5);
(%o2)                               3
(%i3) m : matrix([2,4,1],[3,1,4],[4,3,2]);
                               [ 2  4  1 ]
                               [         ]
(%o3)                          [ 3  1  4 ]
                               [         ]
                               [ 4  3  2 ]
(%i4) zn_determinant(m, 5);
(%o4)                               0
```

See also: `zn_invert_by_lu`.

<!-- category: Other -->
<!-- keywords: zn_factor_generators -->
<!-- signatures: zn_factor_generators(n) -->
### Function: zn_factor_generators (n)

Gibt eine Liste mit Faktorgeneratoren zuruck, die zu den charakteristischen 
Faktoren des Totienten von *n* passen. 


Fur Erlauterungen und Beispiele siehe `zn_characteristic_factors`.

See also: `zn_characteristic_factors`.

<!-- category: Other -->
<!-- keywords: zn_invert_by_lu -->
<!-- signatures: zn_invert_by_lu(matrix, p) -->
### Function: zn_invert_by_lu (matrix, p)

verwendet die Technik der LR-Dekomposition, um ein modulares Inverses der 
Matrix *matrix* uber (Z/*p*Z) zu berechnen. Voraussetzung ist, 
dass *matrix* invertierbar und *p* eine Primzahl ist. 
Sollte *matrix* nicht invertierbar sein, gibt `zn_invert_by_lu` 
`false` zurck.


Siehe auch `zn_determinant`.


Beispiele:



```maxima
(%i1) m : matrix([1,3],[2,4]);
                                [ 1  3 ]
(%o1)                           [      ]
                                [ 2  4 ]
(%i2) zn_determinant(m, 5);
(%o2)                               3
(%i3) mi : zn_invert_by_lu(m, 5);
                                [ 3  4 ]
(%o3)                           [      ]
                                [ 1  2 ]
(%i4) matrixmap(lambda([a], mod(a, 5)), m . mi);
                                [ 1  0 ]
(%o4)                           [      ]
                                [ 0  1 ]
```

See also: `zn_determinant`.

<!-- category: Other -->
<!-- keywords: zn_log -->
<!-- signatures: zn_log(a, g, n), zn_log(a, g, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_log (a, g, n)

Berechnet den diskreten Logarithmus.  Sei (Z/*n*Z)* eine zyklische Gruppe, 
*g* eine Primitivwurzel modulo *n* oder der Generator einer Untergruppe 
von (Z/*n*Z)* und *a* ein Element dieser Gruppe.
Dann berechnet `zn_log (a, g, n)` eine Losung der Kongruenz 
`g^x = a mod n`.  Man beachte, dass `zn_log` nicht terminiert, 
falls *a* keine Potenz von *g* modulo *n* ist.



Der verwendete Algorithmus benotigt die Primfaktorzerlegung von `zn_order(g)` 
bzw. des Totienten von *n*. 
Da diese Berechnung ebenfalls zeitaufwandig ist, kann es eventuell sinnvoll 
sein, die Primfaktoren von `zn_order(g)` vorab zu berechnen und `zn_log` als 
viertes Argument zu ubergeben. Die Form muss dabei der Ruckgabe von 
`ifactors(totient(n))` mit der Standardeinstellung `false` der 
Optionsvariable `factors_only` entsprechen. 
Verglichen mit der Laufzeit fur die Berechnung des Logarithmus hat dies jedoch nur 
einen recht kleinen Effekt.


Als Algorithmus wird die Pohlig-Hellman-Reduktion und das Rho-Verfahren von 
Pollard fur den diskreten Logarithmus verwendet. Die Laufzeit von `zn_log` 
hangt im Wesentlichen von der Bitlange des großten Primfaktors des 
Totienten von *n* ab. 


Siehe auch `zn_primroot`, `zn_order`, `ifactors`, `totient`.


Beispiele:


`zn_log (a, g, n)` findet eine Losung der Kongruenz `g^x = a mod n`.



```maxima
(%i1) n : 22$
(%i2) g : zn_primroot(n);
(%o2)                               7
(%i3) ord_7 : zn_order(7, n);
(%o3)                              10
(%i4) powers_7 : makelist(power_mod(g, x, n), x, 0, ord_7 - 1);
(%o4)              [1, 7, 5, 13, 3, 21, 15, 17, 9, 19]
(%i5) zn_log(9, g, n);
(%o5)                               8
(%i6) map(lambda([x], zn_log(x, g, n)), powers_7);
(%o6)                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(%i7) ord_5 : zn_order(5, n);
(%o7)                               5
(%i8) powers_5 : makelist(power_mod(5,x,n), x, 0, ord_5 - 1);
(%o8)                       [1, 5, 3, 15, 9]
(%i9) zn_log(9, 5, n);
(%o9)                               4
```


Das optionale vierte Argument muss der Ruckgabe von `ifactors(totient(n))` 
entsprechen. 
Die Laufzeit hangt im Wesentlichen von der Bitlange des großten
Primfaktors von `zn_order(g)` ab.



```maxima
(%i1) (p : 2^127-1, primep(p));
(%o1)                             true
(%i2) ifs : ifactors(p - 1)$
(%i3) g : zn_primroot(p, ifs);
(%o3)                              43
(%i4) a : power_mod(g, 4711, p)$
(%i5) zn_log(a, g, p, ifs);
(%o5)                             4711
(%i6) f_max : last(ifs);  
(%o6)                       [77158673929, 1]
(%i7) ord_5 : zn_order(5,p,ifs)$
(%i8) (p - 1)/ord_5;
(%o8)                              73
(%i9) ifs_5 : ifactors(ord_5)$
(%i10) a : power_mod(5, 4711, p)$
(%i11) zn_log(a, 5, p, ifs_5);
(%o11)                            4711
```

See also: `zn_primroot`, `zn_order`, `ifactors`, `totient`.

<!-- category: Other -->
<!-- keywords: zn_mult_table -->
<!-- signatures: zn_mult_table(n), zn_mult_table(n, gcd) -->
### Function: zn_mult_table (n)

Ohne das optionale Argument *gcd* zeigt `zn_mult_table(n)` 
eine Multiplikationstabelle von allen Elementen in (Z/*n*Z)*, 
d.h. von allen zu *n* teilerfremden Elementen.


Das optionale zweite Argument *gcd* erlaubt es, eine bestimmte Untermenge 
von (Z/*n*Z) auszuwahlen. 
Ist *gcd* eine naturliche Zahl, enthalt die Multiplikationstabelle 
alle Restklassen `x` mit `gcd(x,n) =`*gcd*. 
Zur besseren Lesbarkeit werden Zeilen- und Spaltenkopfe hinzugefugt. 
Falls notwendig, lassen sich diese mit `submatrix(1, tabelle, 1)` 
wieder einfach entfernen. 


Wird *gcd* auf `all` gesetzt, wird die Tabelle fur samtliche 
von Null verschiedene Elemente in (Z/*n*Z) ausgegeben.


Das zweite Beispiel unten zeigt einen alternativen Weg, fur Untergruppen 
eine Multiplikationstabelle zu erzeugen.


Siehe auch `zn_add_table`, `zn_power_table`.


Beispiele:


Die Standardtabelle zeigt alle Elemente aus (Z/*n*Z)* und erlaubt, 
grundlegende Eigenschaften von modularen Multiplikationsgruppen zu zeigen und 
zu studieren. Z.B. stehen in der Hauptdiagonale samtliche quadratische Reste, 
jede Zeile und Spalte enthalt alle Elemente, die Tabelle ist symmetrisch, etc..


Wird *gcd* auf `all` gesetzt, wird die Tabelle fur samtliche 
von Null verschiedene Elemente in (Z/*n*Z) ausgegeben.



```maxima
(%i1) zn_mult_table(8);
                                [ 1  3  5  7 ]
                                [            ]
                                [ 3  1  7  5 ]
(%o1)                           [            ]
                                [ 5  7  1  3 ]
                                [            ]
                                [ 7  5  3  1 ]
(%i2) zn_mult_table(8, all);
                            [ 1  2  3  4  5  6  7 ]
                            [                     ]
                            [ 2  4  6  0  2  4  6 ]
                            [                     ]
                            [ 3  6  1  4  7  2  5 ]
                            [                     ]
(%o2)                       [ 4  0  4  0  4  0  4 ]
                            [                     ]
                            [ 5  2  7  4  1  6  3 ]
                            [                     ]
                            [ 6  4  2  0  6  4  2 ]
                            [                     ]
                            [ 7  6  5  4  3  2  1 ]
```


Ist *gcd* eine Zahl, wird zur besseren Lesbarkeit ein Zeilen- und Spaltenkopf 
hinzugefugt.


Ist die mit *gcd* ausgewahlte Teilmenge eine Gruppe, gibt es einen 
alternativen Weg, die Multiplikationstabelle zu erzeugen.
Die Isomorphie zu einer Gruppe mit `1` als Identitat lasst sich nutzen, 
um eine leicht lesbare Tabelle zu erhalten. Die Abbildung gelingt mit dem CRT.


In der so erzeugten zweiten Version der Tabelle `T36_4` steht genau wie 
bei `T9` die Identitat, hier `28`, in der linken oberen Ecke. 




```maxima
(%i1) T36_4: zn_mult_table(36,4);
                        [ *   4   8   16  20  28  32 ]
                        [                            ]
                        [ 4   16  32  28  8   4   20 ]
                        [                            ]
                        [ 8   32  28  20  16  8   4  ]
                        [                            ]
(%o1)                   [ 16  28  20  4   32  16  8  ]
                        [                            ]
                        [ 20  8   16  32  4   20  28 ]
                        [                            ]
                        [ 28  4   8   16  20  28  32 ]
                        [                            ]
                        [ 32  20  4   8   28  32  16 ]
(%i2) T9: zn_mult_table(36/4);
                             [ 1  2  4  5  7  8 ]
                             [                  ]
                             [ 2  4  8  1  5  7 ]
                             [                  ]
                             [ 4  8  7  2  1  5 ]
(%o2)                        [                  ]
                             [ 5  1  2  7  8  4 ]
                             [                  ]
                             [ 7  5  1  8  4  2 ]
                             [                  ]
                             [ 8  7  5  4  2  1 ]
(%i3) T36_4: matrixmap(lambda([x], chinese([0,x],[4,9])), T9);
                          [ 28  20  4   32  16  8  ]
                          [                        ]
                          [ 20  4   8   28  32  16 ]
                          [                        ]
                          [ 4   8   16  20  28  32 ]
(%o3)                     [                        ]
                          [ 32  28  20  16  8   4  ]
                          [                        ]
                          [ 16  32  28  8   4   20 ]
                          [                        ]
                          [ 8   16  32  4   20  28 ]
```

See also: `zn_add_table`, `zn_power_table`.

<!-- category: Other -->
<!-- keywords: zn_nth_root -->
<!-- signatures: zn_nth_root(x, n, m), zn_nth_root(x, n, m, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_nth_root (x, n, m)

Gibt eine Liste mit allen *n*-ten Wurzeln von *x* aus der multiplikativen 
Untergruppe von (Z/*m*Z) zuruck, in der sich *x* befindet, 
oder `false`, falls *x* keine *n*-te Potenz modulo *m* oder 
kein Element einer multiplikativen Untergruppe von (Z/*m*Z) ist.


*x* ist Element einer multiplikativen Untergruppe modulo *m*, wenn der 
großte gemeinsame Teiler `g = gcd(x,m)` zu `m/g` teilerfremd ist.


`zn_nth_root` basiert auf einem Algorithmus von Adleman, Manders und Miller 
und Satzen uber modulare Multiplikationsgruppen von Daniel Shanks.


Der Algorithmus benotigt eine Primfaktorzerlegung des Modulus *m*. 
Es kann eventuell sinnvoll sein, diese Zerlegung vorab zu berechnen und 
als viertes Argument zu ubergeben. Die Form muss dabei der Ruckgabe von 
`ifactors(m)` mit der Standardeinstellung `false` der 
Optionsvariable `factors_only` entsprechen. 


Beispiele:


Eine Potenztabelle der multiplikativen Gruppe modulo `14` 
gefolgt von einer Liste mit Listen von *n*-ten Wurzeln der `1`, 
wobei *n* von `1` bis `6` variiert.



```maxima
(%i1) zn_power_table(14);
                         [ 1   1   1   1   1   1 ]
                         [                       ]
                         [ 3   9   13  11  5   1 ]
                         [                       ]
                         [ 5   11  13  9   3   1 ]
(%o1)                    [                       ]
                         [ 9   11  1   9   11  1 ]
                         [                       ]
                         [ 11  9   1   11  9   1 ]
                         [                       ]
                         [ 13  1   13  1   13  1 ]
(%i2) makelist(zn_nth_root(1,n,14), n,1,6);
(%o2)  [[1], [1, 13], [1, 9, 11], [1, 13], [1], [1, 3, 5, 9, 11, 13]]
```


Im folgenden Beispiel ist *x* nicht zu *m* teilerfremd, 
aber es ist Element einer multiplikativen Untergruppe von (Z/*m*Z) 
und jede *n*-te Wurzel ist aus der selben Untergruppe. 


Die Restklasse `3` ist kein Element in irgend einer multiplikativen 
Untergruppe von (Z/63Z) und wird daher nicht als dritte Wurzel von `27` 
zuruck gegeben.


Hier zeigt `zn_power_table` alle Reste `x` in (Z/63Z) 
mit `gcd(x,63) = 9`. Diese Untergruppe ist isomorph zu (Z/7Z)* 
und seine Identitat `36` wird mit Hilfe des CRT berechnet.



```maxima
(%i1) m: 7*9$

(%i2) zn_power_table(m,9);
                         [ 9   18  36  9   18  36 ]
                         [                        ]
                         [ 18  9   36  18  9   36 ]
                         [                        ]
                         [ 27  36  27  36  27  36 ]
(%o2)                    [                        ]
                         [ 36  36  36  36  36  36 ]
                         [                        ]
                         [ 45  9   27  18  54  36 ]
                         [                        ]
                         [ 54  18  27  9   45  36 ]
(%i3) zn_nth_root(27,3,m);
(%o3)                           [27, 45, 54]
(%i4) id7:1$  id63_9: chinese([id7,0],[7,9]);
(%o5)                                36
```


Im folgenden RSA-ahnlichen Beispiel, in dem der Modulus `N` quadratfrei ist, 
d.h. in paarweise verschiedene Primfaktoren zerfallt, 
ist jedes `x` von `0` bis `N-1`
in einer multiplikativen Untergruppe enthalten.


Zur Entschlusselung wird die `e`-te Wurzel berechnet. 
`e` ist teilerfremd zu `N` und die `e`-te Wurzel ist deshalb 
eindeutig. `zn_nth_root` wendet hier effektiv den als CRT-RSA 
bekannten Algorithmus an.
(Man beachte, dass `flatten` Klammern entfernt und keine Losungen.)



```maxima
(%i1) [p,q,e]: [5,7,17]$  N: p*q$

(%i3) xs: makelist(x,x,0,N-1)$

(%i4) ys: map(lambda([x],power_mod(x,e,N)),xs)$

(%i5) zs: flatten(map(lambda([y], zn_nth_root(y,e,N)), ys))$

(%i6) is(zs = xs);
(%o6)                             true
```


Im folgenden Beispiel ist die Faktorisierung des Modulus bekannt und wird 
als viertes Argument ubergeben.



```maxima
(%i1) p: 2^107-1$  q: 2^127-1$  N: p*q$

(%i4) ibase: obase: 16$

(%i5) msg: 11223344556677889900aabbccddeeff$

(%i6) enc: power_mod(msg, 10001, N);
(%o6)    1a8db7892ae588bdc2be25dd5107a425001fe9c82161abc673241c8b383
(%i7) zn_nth_root(enc, 10001, N, [[p,1],[q,1]]);
(%o7)               [11223344556677889900aabbccddeeff]
```

<!-- category: Other -->
<!-- keywords: zn_order -->
<!-- signatures: zn_order(x, n), zn_order(x, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_order (x, n)

Ist *x* eine Einheit in der endlichen Gruppe (Z/*n*Z)*, so berechnet 
`zn_order` die Ordnung dieses Elements.  Andernfalls gibt `zn_order` 
`false` zuruck.  *x* ist eine Einheit modulo *n*, falls *x* 
teilerfremd zu *n* ist.


Der verwendete Algorithmus benotigt die Primfaktorzerlegung des Totienten von *n*. 
Da diese Berechnung manchmal recht zeitaufwandig ist, kann es eventuell sinnvoll 
sein, die Primfaktoren des Totienten vorab zu berechnen und `zn_order` als 
drittes Argument zu ubergeben. Die Form muss dabei der Ruckgabe von 
`ifactors(totient(n))` mit der Standardeinstellung `false` der 
Optionsvariable `factors_only` entsprechen. 


Siehe auch `zn_primroot`, `ifactors`, `totient`.


Beispiele:


`zn_order` berechnet die Ordnung einer Einheit *x* aus (Z/*n*Z)*.



```maxima
(%i1) n : 22$
(%i2) g : zn_primroot(n);
(%o2)                               7
(%i3) units_22 : sublist(makelist(i,i,1,21), lambda([x], gcd(x, n) = 1));
(%o3)              [1, 3, 5, 7, 9, 13, 15, 17, 19, 21]
(%i4) (ord_7 : zn_order(7, n)) = totient(n);
(%o4)                            10 = 10
(%i5) powers_7 : makelist(power_mod(g,i,n), i,0,ord_7 - 1);
(%o5)              [1, 7, 5, 13, 3, 21, 15, 17, 9, 19]
(%i6) map(lambda([x], zn_order(x, n)), powers_7);
(%o6)              [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]
(%i7) map(lambda([x], ord_7/gcd(x, ord_7)), makelist(i, i,0,ord_7 - 1));
(%o7)              [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]
(%i8) totient(totient(n));
(%o8)                               4
```


Das optionale dritte Argument muss der Ruckgabe von `ifactors(totient(n))` 
entsprechen. 



```maxima
(%i1) (p : 2^142 + 217, primep(p));
(%o1)                             true
(%i2) ifs : ifactors( totient(p) )$
(%i3) g : zn_primroot(p, ifs);
(%o3)                               3
(%i4) is( (ord_3 : zn_order(g, p, ifs)) = totient(p) );
(%o4)                             true
(%i5) map(lambda([x], ord_3/zn_order(x, p, ifs)), makelist(i,i,2,15));
(%o5)        [22, 1, 44, 10, 5, 2, 22, 2, 8, 2, 1, 1, 20, 1]
```

See also: `zn_primroot`, `ifactors`, `totient`.

<!-- category: Other -->
<!-- keywords: zn_power_table -->
<!-- signatures: zn_power_table(n), zn_power_table(n, gcd), zn_power_table(n, gcd, max_exp) -->
### Function: zn_power_table (n)

Ohne ein optionales Argument zeigt `zn_power_table(n)` 
eine Potenzierungstabelle von allen Elementen in (Z/*n*Z)*, 
d.h. von allen zu *n* teilerfremden Elementen. 
Der Exponent variiert dabei jeweils zwischen `1` und 
dem großten charakteristischen Faktor des Totienten von *n*
(auch bekannt als Carmichael Funktion bzw. Carmichael Lambda), 
so dass die Tabelle rechts mit einer Spalte von Einsen endet.


Das optionale zweite Argument *gcd* erlaubt es, eine bestimmte Untermenge 
von (Z/*n*Z) auszuwahlen. 
Ist *gcd* eine naturliche Zahl, werden Potenzen von allen Restklassen 
`x` mit `gcd(x,n) =`*gcd* zuruck gegeben, 
d.h. *gcd* ist standardmaßig `1`.
Wird *gcd* auf `all` gesetzt, wird die Tabelle fur samtliche 
Elemente in (Z/*n*Z) ausgegeben.


Wird das optionale dritte Argument *max_exp* angegeben, variiert der 
Exponent zwischen `1` und *max_exp*.


Siehe auch `zn_add_table`, `zn_mult_table`.


Beispiele:


Die Standardeinstellung *gcd*`= 1` erlaubt es, grundlegende Satze, 
wie die von Fermat and Euler, zu zeigen und zu betrachten.


Das Argument *gcd* erlaubt es, bestimmte Teilmengen von (Z/*n*Z) 
auszuwahlen und multiplikative Untergruppen und Isomorphismen zu untersuchen. 


Z.B. sind die Gruppen `G10` und `G10_2` unter der Multiplikation 
beide isomorph zu `G5`. `1` ist die Identitat in `G5`. 
So sind `1` bzw. `6` die Identitaten in `G10` bzw. `G10_2`. 
Entsprechende Zuordnungen ergeben sich bei den Primitivwurzeln, n-ten Wurzeln, etc..



```maxima
(%i1) zn_power_table(10);
                              [ 1  1  1  1 ]
                              [            ]
                              [ 3  9  7  1 ]
(%o1)                         [            ]
                              [ 7  9  3  1 ]
                              [            ]
                              [ 9  1  9  1 ]
(%i2) zn_power_table(10,2);
                              [ 2  4  8  6 ]
                              [            ]
                              [ 4  6  4  6 ]
(%o2)                         [            ]
                              [ 6  6  6  6 ]
                              [            ]
                              [ 8  4  2  6 ]
(%i3) zn_power_table(10,5);
(%o3)                         [ 5  5  5  5 ]
(%i4) zn_power_table(10,10);
(%o4)                         [ 0  0  0  0 ]
(%i5) G5: [1,2,3,4];
(%o6)                          [1, 2, 3, 4]
(%i6) G10_2: map(lambda([x], chinese([0,x],[2,5])), G5);
(%o6)                          [6, 2, 8, 4]
(%i7) G10: map(lambda([x], power_mod(3, zn_log(x,2,5), 10)), G5);
(%o7)                          [1, 3, 7, 9]
```


Wird *gcd* auf `all` gesetzt, wird die Tabelle fur samtliche 
Elemente in (Z/*n*Z) ausgegeben.


Das dritte Argument *max_exp* erlaubt, den hochsten Exponenten zu wahlen.  
Die folgende Tabelle zeigt ein kleines RSA-Beispiel.



```maxima
(%i1) N:2*5$ phi:totient(N)$ e:7$ d:inv_mod(e,phi)$

(%i5) zn_power_table(N, all, e*d);
       [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
       [                                                               ]
       [ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1 ]
       [                                                               ]
       [ 2  4  8  6  2  4  8  6  2  4  8  6  2  4  8  6  2  4  8  6  2 ]
       [                                                               ]
       [ 3  9  7  1  3  9  7  1  3  9  7  1  3  9  7  1  3  9  7  1  3 ]
       [                                                               ]
       [ 4  6  4  6  4  6  4  6  4  6  4  6  4  6  4  6  4  6  4  6  4 ]
(%o5)  [                                                               ]
       [ 5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5 ]
       [                                                               ]
       [ 6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6 ]
       [                                                               ]
       [ 7  9  3  1  7  9  3  1  7  9  3  1  7  9  3  1  7  9  3  1  7 ]
       [                                                               ]
       [ 8  4  2  6  8  4  2  6  8  4  2  6  8  4  2  6  8  4  2  6  8 ]
       [                                                               ]
       [ 9  1  9  1  9  1  9  1  9  1  9  1  9  1  9  1  9  1  9  1  9 ]
```

See also: `zn_add_table`, `zn_mult_table`.

<!-- category: Other -->
<!-- keywords: zn_primroot -->
<!-- signatures: zn_primroot(n), zn_primroot(n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_primroot (n)

Ist die multiplikative Gruppe (Z/*n*Z)* zyklisch, berechnet `zn_primroot` 
die kleinste Primitivwurzel modulo *n*.  Dies ist der Fall, wenn *n* gleich 
`2`, `4`, `p^k` oder `2*p^k` ist, wobei `p` ungerade und 
prim und `k` eine naturliche Zahl ist.  `zn_primroot` 
fuhrt einen entsprechenden Pratest durch, wenn die Optionsvariable 
`zn_primroot_pretest` (Standardwert: `false`) `true` gesetzt wurde.
In jedem Fall wird die Suche durch die obere Schranke `zn_primroot_limit` begrenzt.


Ist (Z/*n*Z)* nicht zyklisch oder kann bis `zn_primroot_limit` 
keine Primitivwurzel modulo *n* gefunden werden, gibt `zn_primroot` 
`false` zuruck. 


Der verwendete Algorithmus benotigt die Primfaktorzerlegung des Totienten von *n*. 
Diese Berechnung kann zeitaufwandig sein und es kann daher eventuell sinnvoll 
sein, die Primfaktoren des Totienten vorab zu berechnen und `zn_primroot` 
als zusatzliches Argument zu ubergeben. Die Form muss dabei der Ruckgabe  
von `ifactors(totient(n))` mit der Standardeinstellung `false` der 
Optionsvariable `factors_only` entsprechen. 


Siehe auch `zn_primroot_p`, `zn_order`, `ifactors`, `totient`.


Beispiele:


`zn_primroot` berechnet die kleinste Primitivwurzel modulo *n* oder gibt 
`false` zuruck.



```maxima
(%i1) n : 14$
(%i2) g : zn_primroot(n);
(%o2)                               3
(%i3) zn_order(g, n) = totient(n);
(%o3)                             6 = 6
(%i4) n : 15$
(%i5) zn_primroot(n);
(%o5)                             false
```


Das optionale zweite Argument muss der Ruckgabe von `ifactors(totient(n))` 
entsprechen. 



```maxima
(%i1) (p : 2^142 + 217, primep(p));
(%o1)                             true
(%i2) ifs : ifactors( totient(p) )$
(%i3) g : zn_primroot(p, ifs);
(%o3)                               3
(%i4) [time(%o2), time(%o3)];
(%o4)                    [[15.556972], [0.004]]
(%i5) is(zn_order(g, p, ifs) = p - 1);
(%o5)                             true
(%i6) n : 2^142 + 216$
(%i7) ifs : ifactors(totient(n))$
(%i8) zn_primroot(n, ifs), 
      zn_primroot_limit : 200, zn_primroot_verbose : true;
`zn_primroot' stopped at zn_primroot_limit = 200
(%o8)                             false
```

See also: `zn_primroot_pretest`, `zn_primroot_limit`, `zn_primroot_p`, `zn_order`, `ifactors`, `totient`.

<!-- category: Other -->
<!-- keywords: zn_primroot_limit -->
<!-- signatures: zn_primroot_limit -->
### Variable: zn_primroot_limit

Standardwert: `1000` 


Definiert die obere Schranke fur die Suche von `zn_primroot` nach einer 
Primitivwurzel.  Wurde die Optionsvariable `zn_primroot_verbose`
(Standardwert: `false`) `true` gesetzt, wird beim Erreichen von 
`zn_primroot_limit` ein entsprechender Hinweis ausgegeben.

See also: `zn_primroot`, `zn_primroot_verbose`.

<!-- category: Other -->
<!-- keywords: zn_primroot_p -->
<!-- signatures: zn_primroot_p(x, n), zn_primroot_p(x, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_primroot_p (x, n)

Testet, ob *x* eine Primitivwurzel in der multiplikativen Gruppe (Z/*n*Z)* 
ist. 


Der verwendete Algorithmus benotigt die Primfaktorzerlegung des Totienten von  
*n*.  Wird dieser Test nacheinander auf mehrere Zahlen angewandt, 
kann es sinnvoll sein, die Primfaktoren des Totienten vorab zu berechnen 
und `zn_primroot_p` als zusatzliches drittes Argument zu ubergeben. 
Die Form muss dabei der Ruckgabe von `ifactors(totient(n))` mit der 
Standardeinstellung `false` der Optionsvariable `factors_only` 
entsprechen. 


Siehe auch `zn_primroot`, `zn_order`, `ifactors`, `totient`.


Beispiele:


`zn_primroot_p` als Pradikatfunktion.



```maxima
(%i1) n : 14$
(%i2) units_14 : sublist(makelist(i,i,1,13), lambda([i], gcd(i, n) = 1));
(%o2)                     [1, 3, 5, 9, 11, 13]
(%i3) zn_primroot_p(13, n);
(%o3)                            false
(%i4) sublist(units_14, lambda([x], zn_primroot_p(x, n)));
(%o4)                            [3, 5]
(%i5) map(lambda([x], zn_order(x, n)), units_14);
(%o5)                      [1, 6, 6, 3, 3, 2]
```


Das optionale dritte Argument muss der Ruckgabe von `ifactors(totient(n))` 
entsprechen. 



```maxima
(%i1) (p : 2^142 + 217, primep(p));
(%o1)                             true
(%i2) ifs : ifactors( totient(p) )$
(%i3) sublist(makelist(i,i,1,50), lambda([x], zn_primroot_p(x, p, ifs)));
(%o3)      [3, 12, 13, 15, 21, 24, 26, 27, 29, 33, 38, 42, 48]
(%i4) [time(%o2), time(%o3)];
(%o4)                   [[7.748484], [0.036002]]
```

See also: `zn_primroot`, `zn_order`, `ifactors`, `totient`.

<!-- category: Other -->
<!-- keywords: zn_primroot_pretest -->
<!-- signatures: zn_primroot_pretest -->
### Variable: zn_primroot_pretest

Standardwert: `false` 


Eine multiplikative Gruppe (Z/`n`Z)* ist zyklisch, wenn `n` gleich 
`2`, `4`, `p^k` oder `2*p^k` ist, wobei `p` prim und 
großer `2` und `k` eine naturliche Zahl ist. 


`zn_primroot_pretest` entscheidet daruber, ob `zn_primroot` vor 
der Berechnung der kleinsten Primitivwurzel in (Z/`n`Z)* uberpruft, 
ob auf `n` uberhaupt einer der oben genannten Falle zutrifft.  Nur wenn  
`zn_primroot_pretest` `true` ist, wird dieser Pratest ausgefuhrt.

See also: `zn_primroot`.

<!-- category: Other -->
<!-- keywords: zn_primroot_verbose -->
<!-- signatures: zn_primroot_verbose -->
### Variable: zn_primroot_verbose

Standardwert: `false` 


Entscheidet, ob `zn_primroot` beim Erreichen von `zn_primroot_limit`
einen Hinweis ausgibt.

See also: `zn_primroot`, `zn_primroot_limit`.

