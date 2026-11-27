## Gleichungen

<!-- category: Other -->
<!-- keywords: %rnum -->
<!-- signatures: %rnum -->
### Variable: %rnum

Standardwert: `0`


Wenn notwendig erzeugen die Funktionen `solve` und `algsys` freie
Parameter, die in die Losungen eingesetzt werden.  Die Parameter haben den 
Namen `%r<num>`.  Die Optionsvariable `%rnum` enthalt die
Nummer *num*, die an den Prafix `%r` angehangt wird.  Maxima
erhoht `%rnum` automatisch.  Siehe auch die Systemvariable
`%rnum_list` fur eine Liste der Parameter einer Losung.

See also: `solve`, `algsys`, `%rnum_list`.

<!-- category: Other -->
<!-- keywords: %rnum_list -->
<!-- signatures: %rnum_list -->
### Variable: %rnum_list

Standardwert: `[]`


`%rnum_list` ist die Liste der freien Parameter, die von `solve` und
`algsys` in Losungen eingesetzt werden.  Die Parameter werden der Liste
`%rnum_list` in der Reihenfolge hinzugefugt, in der sie erzeugt werden.


Beispiele:



```maxima
(%i1) solve ([x + y = 3], [x,y]);
(%o1)              [[x = 3 - %r1, y = %r1]]


(%i2) %rnum_list;
(%o2)                       [%r1]


(%i3) sol : solve ([x + 2*y + 3*z = 4], [x,y,z]);
(%o3)   [[x = - 2 %r3 - 3 %r2 + 4, y = %r3, z = %r2]]


(%i4) %rnum_list;
(%o4)                     [%r2, %r3]


(%i5) for i : 1 thru length (%rnum_list) do
        sol : subst (t[i], %rnum_list[i], sol)$


(%i6) sol;
(%o6)     [[x = - 2 t  - 3 t  + 4, y = t , z = t ]]
                     2      1           2       1
```

See also: `solve`, `algsys`.

<!-- category: Other -->
<!-- keywords: algepsilon -->
<!-- signatures: algepsilon -->
### Variable: algepsilon

Standardwert: `10^8`


Kontrolliert die Genauigkeit einer numerischen Losung der Funktion 
`algsys` fur den Fall, dass die Optionsvariable `realonly` den Wert
`true` hat, also nur die reellen Losungen gesucht werden.


Beispiele:


Numerische Losung der Gleichung `x^3-2` fur zwei verschiedene Wert
fur `algepsilon`.



```maxima
(%i1) realonly:true$
(%i2) algepsilon:10^2;
(%o2)                          100
(%i3) algsys([x^3-2],[x]);
(%o3)                  [[x = 1.26171875]]
(%i4) algepsilon: 10^8;
(%o4)                       100000000
(%i5) algsys([x^3-2],[x]);
(%o5)               [[x = 1.259921095381759]]
```


`algepsilon` hat keinen Einfluss auf die Genauigkeit der Losung, wenn
auch die komplexen Losungen gesucht werden.



```maxima
(%i6) realonly:false$
(%i7) algepsilon: 10^2;
(%o7)                          100
(%i8) algsys([x^3-2],[x]);
(%o8) [[x = - 1.091123635971721 %i - .6299605249474366], 
[x = 1.091123635971721 %i - .6299605249474366], 
[x = 1.259921095381759]]
```

See also: `algsys`, `realonly`.

<!-- category: Other -->
<!-- keywords: algexact -->
<!-- signatures: algexact -->
### Variable: algexact

Standardwert: `false`


Die Optionsvariable `algexact` kontrolliert die Funktion `algsys`
folgendermaßen:



- *
Hat `algexact` den Wert `true`, wird von der Funktion `algsys` 
stets `solve` aufgerufen.  Findet `solve` keine Losung, wird die 
Funktion `realroots` aufgerufen.
- *
Hat `algexact` den Wert `false`, wird die Funktion `solve` nur
fur Gleichungen aufgerufen, die von mehr als einer Variablen abhangen und
fur quadratische oder kubische Gleichungen.


Der Wert `true` fur `algexact` garantiert nicht, dass `algsys`
nur exakte Lo­sung­en findet.  Findet `algsys` keine exakten
Losungen, versucht `solve` immer Naherungslosungen zu finden.


Beispiele:



```maxima
(%i1) algexact:true$

(%i2) algsys([x^5-1],[x]);
                                      sqrt(5)   5
                               sqrt(- ------- - -)
                     sqrt(5)             2      2    1
(%o2) [[x = 1], [x = ------- + ------------------- - -], 
                        4               2            4
                      sqrt(5)   5
               sqrt(- ------- - -)
     sqrt(5)             2      2    1
[x = ------- - ------------------- - -], 
        4               2            4
                      sqrt(5)   5
                 sqrt(------- - -)
       sqrt(5)           2      2    1
[x = - ------- + ----------------- - -], 
          4              2           4
                      sqrt(5)   5
                 sqrt(------- - -)
       sqrt(5)           2      2    1
[x = - ------- - ----------------- - -]]
          4              2           4

(%i3) algexact:false$

(%i4) algsys([x^5-1],[x]);
(%o4) [[x = 1], [x = - .5877852522924731 %i
 - .8090169943749475], [x = .5877852522924731 %i
 - .8090169943749475], [x = .3090169943749475
 - .9510565162951535 %i], [x = .9510565162951535 %i
 + .3090169943749475]]
```


Auch wenn die Optionsvariable `algexact` den Wert `true` hat, gibt
`algsys` numerische Naherungslosungen zuruck, wenn `solve`
keine Losungen finden kann.



```maxima
(%i5) algexact:true$

(%i6) algsys([x^5-x^3+1],[x]);
(%o6) [[x = - 1.236505681818182], 
[x = - 0.785423103049449 %i - .3407948661970064], 
[x = 0.785423103049449 %i - .3407948661970064], 
[x = .9590477178927559 - .4283659562541893 %i], 
[x = .4283659562541893 %i + .9590477178927559]]

(%i7) solve([x^5-x^3+1],[x]);
                              5    3
(%o7)                   [0 = x  - x  + 1]
```


Fur eine quadratische Gleichung wird immer eine exakte Losung zuruckgeben.



```maxima
(%i8) algsys:true$

(%i9) algsys([x^2+x-1],[x]);
                 sqrt(5) - 1          sqrt(5) + 1
(%o9)      [[x = -----------], [x = - -----------]]
                      2                    2
(%i11) algsys:false$

(%i12) algsys([x^2+x-1],[x]);
                  sqrt(5) - 1          sqrt(5) + 1
(%o12)      [[x = -----------], [x = - -----------]]
                       2                    2
```

See also: `algsys`, `solve`, `realroots`.

<!-- category: Other -->
<!-- keywords: algsys -->
<!-- signatures: algsys([expr_1, ..., expr_m], [x_1, ..., x_n]), algsys([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: algsys ([expr_1, ..., expr_m], [x_1, ..., x_n])

Lost ein Gleichungssystem mit den Polynomen *expr_1*, ...,
*expr_m* oder den Gleichungen *eqn_1*, ..., *eqn_m* fur die
Variablen *x_1*, ..., *x_n*.  Werden Polynome *expr_i* als
Argument ubergeben, werden diese als Gleichungen `expr_i = 0`
interpretiert.  Die Anzahl der Gleichungen und Variablen kann verschieden sein.


`algsys` gibt eine Liste mit den Losungen zuruck.  Jede Losung ist
wiederum eine Liste mit den Losungen fur die einzelnen Variablen *x_i*,
die als Gleichungen angegeben sind.  Kann `algsys` keine Losung finden,
wird eine leere Liste `[]` zuruckgegeben.


Haben die Losungen freie Parameter, setzt `algsys` die Symbole
`%r1`, `%r2`, ... in die Losungen ein.  Die freien Parameter
werden der Liste `%rnum_list` hinzugefugt.  Siehe `%rnum_list`.


Die Funktion `algsys` fuhrt die folgenden Schritte aus, um Losungen
eines Gleichungssystems zu finden:



1. Die Gleichungen werden faktorisiert und in Teilsysteme *S_i* aufgeteilt.
2. Fur jedes Teilsystem *S_i* werden eine Gleichung *E*, die den
niedrigsten von Null verschiedenen Grad hat und eine Variable *x*
ausgewahlt.  Dann wird die Resultante der Gleichungen *E* und *E_j*
fur die Variable *x* sowie allen verbleibenden Gleichungen *E_j* des
Teilsystems *S_i* berechnet.  Dieses Verfahren eliminiert die Variable
*x* und hat ein neues Teilsystem *S_i’* als Ergebnis.  Der Algorithmus
wiederholt dann den 1. Schritt.
3. Besteht das Teilsystem nur noch aus einer Gleichung, hat diese Gleichung
mehrere Variablen und enthalt diese keine Gleitkommazahlen, dann wird 
`solve` aufgerufen, um eine exakte Losung zu finden.


Es kann sein, dass `solve` keine Losung oder einen sehr großen 
Ausdruck als Losung findet.


Auch fur Gleichungen, die nur eine Variable enthalten und die entweder linear,
quadratisch oder quartisch sind sowie keine Gleitkommazahlen enthalten, wird 
`solve` aufgerufen, um eine exakte Losung zu finden.  Trifft dies nicht 
zu, wird in dem Fall, dass die `realonly` den Wert `true` hat, die
Funktion `realroots`.  Ansonsten wird die Funktion `allroots`
aufgerufen.  Die Funktion `realroots` sucht reelle Losungen der
Gleichung, wahrend die Funktion `allroots` auch komplex Losungen sucht.


Fur den Fall, dass `realonly` den Wert `true` hat, wird die
Genauigkeit einer numerischen Losung von der Optionsvariablen
`algepsilon` kontrolliert.


Hat die Optionsvariable `algexact` den Wert `true`, wird immer die
Funktion `solve` aufgerufen.
4. Zuletzt werden die erhaltenen Losungen in das betrachtete Teilsystem 
eingesetzt und der Losungsalgorithmus mit dem 1. Schritt fortgesetzt.


Tritt beim Losen des Gleichungssystems eine Gleichung auf, die von mehreren
Variablen abhangt und Gleitkommazahlen enthalt, dann wird der Algorithmus 
mit der Meldung `algsys cannot solve - system too complicated."`
abgebrochen.  Ein Naherung mit Gleitkommazahlen kann in vorgehenden Schritten 
auftreten, wenn keine exakten Losungen auffindbar sind.


Ist das Argument der Funktion `allroots` kein Polynom, gibt Maxima eine
Fehlermeldung aus.  Die Losungen eines Gleichungssystems konnen sehr
große Ausdrucke sein.  Obwohl die Losung reell ist, kann die imaginare
Einheit `%i` in den Losungen enthalten sein.  Fur die weitere
Bearbeitung der Losungen konnen die Funktionen `pickapart` oder
`reveal` hilfreich sein.


Beispiele:



```maxima
(%i1) e1: 2*x*(1 - a1) - 2*(x - 1)*a2;
(%o1)              2 (1 - a1) x - 2 a2 (x - 1)
(%i2) e2: a2 - a1; 
(%o2)                        a2 - a1
(%i3) e3: a1*(-y - x^2 + 1); 
                                   2
(%o3)                   a1 (- y - x  + 1)
(%i4) e4: a2*(y - (x - 1)^2);
                                       2
(%o4)                   a2 (y - (x - 1) )
(%i5) algsys ([e1, e2, e3, e4], [x, y, a1, a2]);
(%o5) [[x = 0, y = %r1, a1 = 0, a2 = 0], 

                                  [x = 1, y = 0, a1 = 1, a2 = 1]]
(%i6) e1: x^2 - y^2;
                              2    2
(%o6)                        x  - y
(%i7) e2: -1 - y + 2*y^2 - x + x^2;
                         2        2
(%o7)                 2 y  - y + x  - x - 1
(%i8) algsys ([e1, e2], [x, y]);
                 1            1
(%o8) [[x = - -------, y = -------], 
              sqrt(3)      sqrt(3)

        1              1             1        1
[x = -------, y = - -------], [x = - -, y = - -], [x = 1, y = 1]]
     sqrt(3)        sqrt(3)          3        3
```

See also: `%rnum_list`, `solve`, `realonly`, `realroots`, `allroots`, `algepsilon`, `algexact`, `pickapart`, `reveal`.

<!-- category: Other -->
<!-- keywords: allroots -->
<!-- signatures: allroots(expr), allroots(eqn) -->
### Function: allroots (expr)

Berechnet numerische Naherungen der reellen und komplexen Wurzeln 
des Polynoms *expr* oder der Polynomgleichung *eqn* mit einer Variablen.


Hat der Schalter `polyfactor` den Wert `true`, wird das Polynom
uber die reellen oder komplexen Zahlen faktorisiert.


Fur den Fall mehrfacher Wurzeln kann `allroots` ungenaue Ergebnisse 
liefern.  Ist das Polynom reell, kann es sein, dass `allroots(%i*p)`)
genauere Approximationen liefern als `allroots (p)`, da
`allroots` in diesem Fall einen anderen Algorithmus verwendet.


Der Zahler des Arguments der Funktion `allroots` muss nach Anwendung der
Funktion `rat` ein Polynom sein und darf im Nenner hochstens eine 
komplexe Zahl enthalten.  Ist das Argument der Funktion `allroots` kein 
Polynom, gibt Maxima eine Fehlermeldung.  Daher wird von der Funktion
`allroots` immer ein aquivalenter, jedoch faktorisierter Ausdruck
zuruckgegeben, wenn die Optionsvariable `polyfactor` den Wert `true`
hat.


Fur komplexe Polynome wird ein Algorithmus von Jenkins und Traub verwendet 
(Algorithm 419, *Comm. ACM*, vol. 15, (1972), p. 97).
Fur reelle Polynome wird ein Algorithmus von Jenkins verwendet
(Algorithm 493, *ACM TOMS*,vol. 1, (1975), p.178).


Beispiele:



```maxima
(%i1) eqn: (1 + 2*x)^3 = 13.5*(1 + x^5);
                            3          5
(%o1)              (2 x + 1)  = 13.5 (x  + 1)
(%i2) soln: allroots (eqn);
(%o2) [x = .8296749902129361, x = - 1.015755543828121, 

x = .9659625152196369 %i - .4069597231924075, 

x = - .9659625152196369 %i - .4069597231924075, x = 1.0]
(%i3) for e in soln
        do (e2: subst (e, eqn), disp (expand (lhs(e2) - rhs(e2))));
                      - 3.5527136788005E-15

                     - 5.32907051820075E-15

         4.44089209850063E-15 %i - 4.88498130835069E-15

        - 4.44089209850063E-15 %i - 4.88498130835069E-15

                       3.5527136788005E-15

(%o3)                         done
(%i4) polyfactor: true$
(%i5) allroots (eqn);
(%o5) - 13.5 (x - 1.0) (x - .8296749902129361)

                           2
 (x + 1.015755543828121) (x  + .8139194463848151 x

 + 1.098699797110288)
```

See also: `polyfactor`.

<!-- category: Other -->
<!-- keywords: backsubst -->
<!-- signatures: backsubst -->
### Variable: backsubst

Standardwert: `true`


Hat `backsubst` den Wert `false`, werden die Losungen der Funktion
`linsolve` nicht rucksubstituiert.  Dies kann hilfreich sein, wenn die
Rucksubstitution zu sehr großen Ausdrucken fuhrt.


Beispiele:



```maxima
(%i1) eq1 : x + y + z = 6$
(%i2) eq2 : x - y + z = 2$
(%i3) eq3 : x + y - z = 0$
(%i4) backsubst : false$

(%i5) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o5)             [x = z - y, y = 2, z = 3]

(%i6) backsubst : true$

(%i7) linsolve ([eq1, eq2, eq3], [x,y,z]);
(%o7)               [x = 1, y = 2, z = 3]
```

See also: `linsolve`.

<!-- category: Other -->
<!-- keywords: bfallroots -->
<!-- signatures: bfallroots(expr), bfallroots(eqn) -->
### Function: bfallroots (expr)

Berechnet numerische Naherungen der reellen und komplexen Wurzeln des Polynoms 
*expr* oder der Polynomgleichung *eqn* in einer Variable.


`bfallroots` entspricht der Funktion `allroots` mit dem Unterschied,
dass die Funktion `bfallroots` die Naherungen mit großen
Gleitkommazahlen berechnet.  Siehe `allroots`.


Beispiel:


Dasselbe Beispiel wie für die Funktion `allroots`.  Die Ergebnisse
sind große Gleitkommazahlen.



```maxima
(%i1) eqn: (1 + 2*x)^3 = 13.5*(1 + x^5);

                            3          5
(%o1)              (2 x + 1)  = 13.5 (x  + 1)

(%i2) soln: bfallroots(eqn);
(%o2) [x = 8.296749902129362b-1, x = - 1.015755543828121b0, 
x = 9.65962515219637b-1 %i - 4.069597231924075b-1, 
x = - 9.65962515219637b-1 %i - 4.069597231924075b-1, x = 1.0b0]
```

See also: `allroots`.

<!-- category: Other -->
<!-- keywords: breakup -->
<!-- signatures: breakup -->
### Variable: breakup

Standardwert: `true`


Hat die Optionsvariablen `programmode` den Wert `false` und die
Optionsvariable `breakup` den Wert `true`, dann werden fur
gemeinsame Terme in Losungen von kubischen und quartischen Gleichungen
Zwischenmarken erzeugt.


Beispiele:



```maxima
(%i1) programmode: false$
(%i2) breakup: true$
(%i3) solve (x^3 + x^2 - 1);

                        sqrt(23)    25 1/3
(%t3)                  (--------- + --)
                        6 sqrt(3)   54
Solution:

                                      sqrt(3) %i   1
                                      ---------- - -
                sqrt(3) %i   1            2        2   1
(%t4)    x = (- ---------- - -) %t3 + -------------- - -
                    2        2            9 %t3        3


                                      sqrt(3) %i   1
                                    - ---------- - -
              sqrt(3) %i   1              2        2   1
(%t5)    x = (---------- - -) %t3 + ---------------- - -
                  2        2             9 %t3         3


                                   1     1
(%t6)                  x = %t3 + ----- - -
                                 9 %t3   3
(%o6)                    [%t4, %t5, %t6]
(%i6) breakup: false$
(%i7) solve (x^3 + x^2 - 1);
Solution:

             sqrt(3) %i   1
             ---------- - -
                 2        2        sqrt(23)    25 1/3
(%t7) x = --------------------- + (--------- + --)
             sqrt(23)    25 1/3    6 sqrt(3)   54
          9 (--------- + --)
             6 sqrt(3)   54

                                              sqrt(3) %i   1    1
                                           (- ---------- - -) - -
                                                  2        2    3

           sqrt(23)    25 1/3  sqrt(3) %i   1
(%t8) x = (--------- + --)    (---------- - -)
           6 sqrt(3)   54          2        2

                                            sqrt(3) %i   1
                                          - ---------- - -
                                                2        2      1
                                      + --------------------- - -
                                           sqrt(23)    25 1/3   3
                                        9 (--------- + --)
                                           6 sqrt(3)   54

            sqrt(23)    25 1/3             1             1
(%t9)  x = (--------- + --)    + --------------------- - -
            6 sqrt(3)   54          sqrt(23)    25 1/3   3
                                 9 (--------- + --)
                                    6 sqrt(3)   54
(%o9)                    [%t7, %t8, %t9]
```

See also: `programmode`.

<!-- category: Other -->
<!-- keywords: dimension -->
<!-- signatures: dimension(eqn), dimension(eqn_1, ..., eqn_n) -->
### Function: dimension (eqn)

`dimen` ist ein Paket fur die Dimensionsanalyse.  `load("dimen")`
ladt dieses Paket.  `demo(dimen)` zeigt eine kleine Demonstration.

<!-- category: Other -->
<!-- keywords: dispflag -->
<!-- signatures: dispflag -->
### Variable: dispflag

Standardwert: `true`








Hat `dispflag` den Wert `false`, werden Ausgaben der Funktion
`solve` unterdruckt.

<!-- category: Other -->
<!-- keywords: funcsolve -->
<!-- signatures: funcsolve(eqn, g(t)) -->
### Function: funcsolve (eqn, g(t))

Das Argument *eqn* ist eine Gleichung, die ein Polynom erster Ordnung in den
Funktionen `g(t)` und `g(t+1)` ist.
`funcsolve` sucht die rationale Funktion `g(t)`, die
Losung der Gleichung *eqn* ist.


Warnung: Die Funktion ist nur sehr rudimentar implementiert.  Offensichtliche
Verallgemeinerungen fehlen.


Beispiel:



```maxima
(%i1) eqn: (n + 1)*f(n) - (n + 3)*f(n + 1)/(n + 1) =
      (n - 1)/(n + 2);
                            (n + 3) f(n + 1)   n - 1
(%o1)        (n + 1) f(n) - ---------------- = -----
                                 n + 1         n + 2
(%i2) funcsolve (eqn, f(n));

Dependent equations eliminated:  (4 3)
                                   n
(%o2)                f(n) = ---------------
                            (n + 1) (n + 2)
```

<!-- category: Other -->
<!-- keywords: globalsolve -->
<!-- signatures: globalsolve -->
### Variable: globalsolve

Standardwert: `false`


Hat `globalsolve` den Wert `true`, werden den unbekannten Variablen
eines linearen Gleichungssystems die Werte der Losungen der Funktionen
`linsolve` und `solve` zugewiesen.


Hat `globalsolve` den Wert `false`, werden den unbekannten Variablen
eines linearen Gleichungssystems keine Werte zugewiesen.  Die Losungen werden 
als Gleichungen mit den unbekannten Variablen ausgedruckt.


Fur andere als lineare Gleichungssysteme wird der Wert von `globalsolve`
ignoriert.  Die Funktion `algsys` ignoriert `globalsolve` immer.


Beispiele:



```maxima
(%i1) globalsolve: true$
(%i2) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t2)                        x : --
                                 7

                                   1
(%t3)                        y : - -
                                   7
(%o3)                     [[%t2, %t3]]
(%i3) x;
                               17
(%o3)                          --
                               7
(%i4) y;
                                 1
(%o4)                          - -
                                 7
(%i5) globalsolve: false$
(%i6) kill (x, y)$
(%i7) solve ([x + 3*y = 2, 2*x - y = 5], [x, y]);
Solution

                                 17
(%t7)                        x = --
                                 7

                                   1
(%t8)                        y = - -
                                   7
(%o8)                     [[%t7, %t8]]
(%i8) x;
(%o8)                           x
(%i9) y;
(%o9)                           y
```

See also: `linsolve`, `solve`, `algsys`.

<!-- category: Other -->
<!-- keywords: ieqn -->
<!-- signatures: ieqn(ie, unk, tech, n, guess) -->
### Function: ieqn (ie, unk, tech, n, guess)

`inteqn` ist ein Paket zur Losung von Integralgleichungen zweiter 
Art der Form



```maxima
b(x)
                      /
                      [
    p(x) = q(x, p(x), I     w(x, u, p(x), p(u)) du)
                      ]
                      /
                       a(x)
```


und von Integralgleichungen erster Art der Form



```maxima
b(x)
           /
           [
    f(x) = I     w(x, u, p(u)) du
           ]
           /
            a(x)
```


Das Kommando `load("inteqn")` ladt das Paket.


Das erste Argument *ie* ist die Integralgleichung und das Argument *unk*
die unbekannte Funktion.  Mit dem Argument *tech* wird die Methode
angegeben, die zur Losung der Integralgleichung angewendet werden soll.
Erhalt das Argument *tech* den Wert `first`, wird das Ergebnis der
ersten erfolgreichen Methode zuruckgegeben.  Mit `all` werden alle
Methoden angewendet.  Das Argument *n* gibt die maximale Anzahl an Termen
an, die von den Methoden `taylor`, `neumann`, `firstkindseries`
oder `fredseries` verwendet werden.  *n* ist auch die maximale Tiefe
der Rekursion fur der Differentiationsmethode.  Das Argument *guess* ist
der Startwert der Methoden `neumann` oder `firstkindseries`.


Die Standardwerte der Argumente sind:



**unk** — `p(x)`, wobei *p* die erste im Integranden aufgefundene
Funktion ist, die Maxima unbekannt ist, und *x* die Variable ist, die im
Falle einer Integralgleichung der zweiten Art als Argument der Funktion
*p* außerhalb des Integrals vorgefunden wird, oder im Falle einer 
Integralgleichung der ersten Art die einzige andere Variable neben der 
Integrationsvariable ist.  Wenn der Versuch fehlschlagt, die Variable *x*
zu finden, wird der Nutzer nach der unabhangigen Variablen gefragt.
**tech** — `first`
**n** — `1`
**guess** — `none`, bewirkt, dass der Ansatz `f(x)` als Startwert
der Losungsmethoden `neumann` und `firstkindseries` verwendet wird.


Siehe `share/integequations/inteqn.usg` fur weitere Informationen.

<!-- category: Other -->
<!-- keywords: ieqnprint -->
<!-- signatures: ieqnprint -->
### Variable: ieqnprint

Standardwert: `true`


`ieqnprint` kontrolliert die Ausgabe des Ergebnisses der Funktion 
`ieqn`.  Hat die Optionsvariable `ieqnprint` den Wert `true`,
dann hat das Ergebnis der Funktion `ieqn` die Form
`[solution, technique used, nterms, flag]`.
Ist die Losung exakt, tritt das Element `flag` nicht auf.
Ansonsten erhalt das Element `flag` den Wert `approximate`
fur eine nicht exakte Losung und den Wert `incomplete` fur eine nicht
geschlossene Losung.  Wurde die Losung mit einer Methode gefunden, die einen
Reihenansatz verwendet, enthalt *nterms* die Anzahl der Terme der
Entwicklung.

See also: `ieqn`.

<!-- category: Other -->
<!-- keywords: lhs -->
<!-- signatures: lhs(expr) -->
### Function: lhs (expr)

Gibt die linke Seite des Ausdrucks *expr* zuruck, wenn der Operator von
*expr* einer der relationalen Operatoren
`< <= = # equal notequal >= >`, einer der Zuweisungsoperatoren
`:= ::= : ::` oder ein nutzerdefinierter binarer Infix-Operator ist, der
mit der Funktion `infix` deklariert wurde.  Die linke Seite des Ausdrucks
ist fur die hier genannten Operatoren das erste Argument.


Wenn *expr* ein Atom ist oder sein Operator ein anderer als oben 
aufgelistet, gibt `lhs` den Ausdruck *expr* zuruck.  Siehe auch 
`rhs`.


Beispiele:



```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [lhs (aa < bb), lhs (aa <= bb), lhs (aa >= bb),
       lhs (aa > bb)];
(%o4)                   [aa, aa, aa, aa]
(%i5) [lhs (aa = bb), lhs (aa # bb), lhs (equal (aa, bb)),
       lhs (notequal (aa, bb))];
(%o5)                   [aa, aa, aa, aa]

(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x

(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y
(%i10) [lhs (e1), lhs (e2), lhs (e3), lhs (e4)];
(%o10)               [foo(x), bar(y), x, x]
(%i11) infix ("][");
(%o11)                         ][
(%i12) lhs (aa ][ bb);
(%o12)                         aa
```

See also: `infix`, `rhs`.

<!-- category: Other -->
<!-- keywords: linsolve -->
<!-- signatures: linsolve([expr_1, ..., expr_m], [x_1, ..., x_n]) -->
### Function: linsolve ([expr_1, ..., expr_m], [x_1, ..., x_n])

Lost das lineare Gleichungssystem mit den Gleichungen oder Polynomen
[*expr_1*, ..., *expr_m*] und den Variablen [*x_1*, ..., 
*x_n*].  Jede Gleichung muss ein Polynom in den angegebenen Variablen sein.


Hat die Optionsvariable `globalsolve` den Wert `true`, werden die
Losungen des Gleichungssystems den angegebenen Variablen zugewiesen.


Hat die Optionsvariable `backsubst` den Wert `false`, fuhrt
`linsolve` keine Rucksubstitutionen aus.  Dies kann hilfreich sein, wenn
die Rucksubstitution zu sehr großen Ausdrucken fuhrt.


Hat die Optionsvariable `linsolve_params` den Wert `true`, setzt
`linsolve` fur ein unterbestimmtes Gleichungssystem freie Parameter in
die Losungen ein, die mit `%r`-Symbolen bezeichnet werden.  Siehe auch
`%rnum` und `%rnum_list`.


Hat die Optionsvariable `programmode` den Wert `false`, werden die
Losungen von `linsolve` Zwischenmarken `%t` zugewiesen.  Die
Zwischenmarken werden als Liste zuruckgegeben.


Beispiele:



```maxima
(%i1) e1: x + z = y;
(%o1)                       z + x = y
(%i2) e2: 2*a*x - y = 2*a^2;
                                       2
(%o2)                   2 a x - y = 2 a
(%i3) e3: y - 2*z = 2;
(%o3)                      y - 2 z = 2
(%i4) [globalsolve: false, programmode: true];
(%o4)                     [false, true]
(%i5) linsolve ([e1, e2, e3], [x, y, z]);
(%o5)            [x = a + 1, y = 2 a, z = a - 1]
(%i6) [globalsolve: false, programmode: false];
(%o6)                    [false, false]
(%i7) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t7)                       z = a - 1

(%t8)                        y = 2 a

(%t9)                       x = a + 1
(%o9)                    [%t7, %t8, %t9]
(%i9) ''%;
(%o9)            [z = a - 1, y = 2 a, x = a + 1]
(%i10) [globalsolve: true, programmode: false];
(%o10)                    [true, false]
(%i11) linsolve ([e1, e2, e3], [x, y, z]);
Solution

(%t11)                      z : a - 1

(%t12)                       y : 2 a

(%t13)                      x : a + 1
(%o13)                 [%t11, %t12, %t13]
(%i13) ''%;
(%o13)           [z : a - 1, y : 2 a, x : a + 1]
(%i14) [x, y, z];
(%o14)                 [a + 1, 2 a, a - 1]
(%i15) [globalsolve: true, programmode: true];
(%o15)                    [true, true]
(%i16) linsolve ([e1, e2, e3], '[x, y, z]);
(%o16)           [x : a + 1, y : 2 a, z : a - 1]
(%i17) [x, y, z];
(%o17)                 [a + 1, 2 a, a - 1]
```

See also: `globalsolve`, `backsubst`, `linsolve_params`, `%rnum`, `%rnum_list`, `programmode`.

<!-- category: Other -->
<!-- keywords: linsolve_params -->
<!-- signatures: linsolve_params -->
### Variable: linsolve_params

Standardwert: `true`


Hat `linsolve_params` den Wert `true`, setzt die Funktion
`linsolve` fur ein unterbestimmtes Gleichungssystem freie Parameter in
die Losungen ein, die mit `%r`-Symbolen bezeichnet werden.  Siehe auch
`%rnum` und `%rnum_list`.

See also: `linsolve`, `%rnum`, `%rnum_list`.

<!-- category: Other -->
<!-- keywords: linsolvewarn -->
<!-- signatures: linsolvewarn -->
### Variable: linsolvewarn

Standardwert: `true`


Hat `linsolvewarn` den Wert `true`, gibt die Funktion
`linsolve` gegebenenfalls die Meldung `Dependent equations eliminated`
aus.

See also: `linsolve`.

<!-- category: Other -->
<!-- keywords: multiplicities -->
<!-- signatures: multiplicities -->
### Variable: multiplicities

Standardwert: `not_set_yet`


`multiplicities` ist die Liste der Vielfachheiten der  
Losungen, die von `solve`, `realroots` oder `allroots`
zuruckgegeben werden.


Beispiel:



```maxima
(%i1) solve(x^2*(x+1)^2, x);
(%o1)                   [x = - 1, x = 0]
(%i2) multiplicities;
(%o2)                        [2, 2]
```

See also: `solve`, `realroots`, `allroots`.

<!-- category: Other -->
<!-- keywords: nroots -->
<!-- signatures: nroots(p, low, high) -->
### Function: nroots (p, low, high)

Gibt die Anzahl der reellen Wurzeln des reellen univariaten Polynoms *p* im 
halboffenen Intervall `(low, high]` zuruck.
Die Grenzen des Intervalls konnen auch negativ unendlich `minf` oder 
positiv unendlich `inf` sein.


`nroots` verwendet die Methode der Sturm-Sequenzen.


Beispiel:



```maxima
(%i1) p: x^10 - 2*x^4 + 1/2$
(%i2) nroots (p, -6, 9.1);
(%o2)                           4
```

<!-- category: Other -->
<!-- keywords: nthroot -->
<!-- signatures: nthroot(p, n) -->
### Function: nthroot (p, n)

Das Argument *p* ist ein Polynom mit ganzzahligen Koeffizienten und das
Argument *n* eine positive ganze Zahl.  `nthroot` gibt ein Polynom 
$q$ uber die ganzen Zahlen zuruck, so dass $q^n = p$ gilt.
Existiert kein derartiges Polynom *q* gibt Maxima eine Fehlermeldung aus.
`nthroot` ist wesentlich schneller als die Funktionen `factor` oder
`sqfr`.

See also: `factor`, `sqfr`.

<!-- category: Other -->
<!-- keywords: polyfactor -->
<!-- signatures: polyfactor -->
### Variable: polyfactor

Standardwert: `false`


Hat die Optionsvariable `polyfactor` den Wert `true`, werden die
Losungen der Funktionen `allroots` und `bfallroots` uber die 
reellen Zahlen faktorisiert, wenn das Polynom reell ist, und uber die
komplexen Zahlen, wenn das Polynome komplex ist.


Siehe `allroots` fur ein Beispiel.

See also: `allroots`.

<!-- category: Other -->
<!-- keywords: programmode -->
<!-- signatures: programmode -->
### Variable: programmode

Standardwert: `true`


Hat `programmode` den Wert `true`, geben die Funktionen
`solve`, `realroots`, `allroots`,
`bfallroots` und `linsolve` die Losungen als Elemente einer Liste
zuruck.


Hat `programmode` den Wert `false`, werden die Losungen der oben 
genannten Funktionen Zwischenmarken `%t` zugewiesen.  Die Ruckgabe der 
Funktionen ist in diesem Fall eine Liste der Zwischenmarken.

See also: `solve`, `realroots`, `allroots`, `bfallroots`, `linsolve`.

<!-- category: Other -->
<!-- keywords: realonly -->
<!-- signatures: realonly -->
### Variable: realonly

Standardwert: `false`


Hat `realonly` den Wert `true`, gibt `algsys` nur Losungen
zuruck, die nicht die imaginare Einheit `%i` enthalten.

See also: `algsys`.

<!-- category: Other -->
<!-- keywords: realroots -->
<!-- signatures: realroots(expr, bound), realroots(eqn, bound), realroots(expr), realroots(eqn) -->
### Function: realroots (expr, bound)

Computes rational approximations of the real roots of the polynomial *expr*
or polynomial equation *eqn* of one variable, to within a tolerance of 
*bound*.  Coefficients of *expr* or *eqn* must be literal numbers;
symbol constants such as `%pi` are rejected.


`realroots` assigns the multiplicities of the roots it finds to the global 
variable `multiplicities`.


`realroots` constructs a Sturm sequence to bracket each root, and then 
applies bisection to refine the approximations.  All coefficients are converted 
to rational equivalents before searching for roots, and computations are carried
out by exact rational arithmetic.  Even if some coefficients are floating-point 
numbers, the results are rational (unless coerced to floats by the `float` 
or `numer` flags).


When *bound* is less than 1, all integer roots are found exactly.  When 
*bound* is unspecified, it is assumed equal to the global variable 
`rootsepsilon`.


When the global variable `programmode` is `true`, `realroots` 
returns a list of the form `[x = x_1, x = x_2, ...]`.  When 
`programmode` is `false`, `realroots` creates intermediate 
expression labels `%t1`, `%t2`, ..., assigns the results to them, and 
returns the list of labels.


Examples:



```maxima
(%i1) realroots (-1 - x + x^5, 5e-6);
                               612003
(%o1)                     [x = ------]
                               524288
(%i2) ev (%[1], float);
(%o2)                 x = 1.167303085327148
(%i3) ev (-1 - x + x^5, %);
(%o3)                - 7.396496210176905E-6
```



```maxima
(%i1) realroots (expand ((1 - x)^5 * (2 - x)^3 * (3 - x)), 1e-20);
(%o1)                 [x = 1, x = 2, x = 3]
(%i2) multiplicities;
(%o2)                       [5, 3, 1]
```

<!-- category: Other -->
<!-- keywords: rhs -->
<!-- signatures: rhs(expr) -->
### Function: rhs (expr)

Gibt die rechte Seite des Ausdrucks *expr* 
zuruck, wenn der Operator von *expr* einer der relationalen Operatoren
`< <= = # equal notequal >= >`, einer der Zuweisungsoperatoren 
`:= ::= : ::` oder ein nutzerdefinierter binarer Infixoperator ist, der
mit der Funktion `infix` deklariert wurde.  Die rechte Seite des Ausdrucks
ist fur die hier genannten Operatoren das zweite Argument.


Ist *expr* ein Atom oder hat der Ausdruck *expr* einen anderen Operator
als oben angegeben, dann ist das Ergebnis `0`.  Siehe auch `lhs`.


Beispiele:



```maxima
(%i1) e: aa + bb = cc;
(%o1)                     bb + aa = cc
(%i2) lhs (e);
(%o2)                        bb + aa
(%i3) rhs (e);
(%o3)                          cc
(%i4) [rhs (aa < bb), rhs (aa <= bb), rhs (aa >= bb),
       rhs (aa > bb)];
(%o4)                   [bb, bb, bb, bb]
(%i5) [rhs (aa = bb), rhs (aa # bb), rhs (equal (aa, bb)),
       rhs (notequal (aa, bb))];
(%o5)                   [bb, bb, bb, bb]
(%i6) e1: '(foo(x) := 2*x);
(%o6)                     foo(x) := 2 x
(%i7) e2: '(bar(y) ::= 3*y);
(%o7)                    bar(y) ::= 3 y
(%i8) e3: '(x : y);
(%o8)                         x : y
(%i9) e4: '(x :: y);
(%o9)                        x :: y

(%i10) [rhs (e1), rhs (e2), rhs (e3), rhs (e4)];
(%o10)                  [2 x, 3 y, y, y]

(%i11) infix ("][");
(%o11)                         ][
(%i12) rhs (aa ][ bb);
(%o12)                         bb
```

See also: `lhs`.

<!-- category: Other -->
<!-- keywords: rootsepsilon -->
<!-- signatures: rootsepsilon -->
### Variable: rootsepsilon

Standardwert: `1.0e-7`


`rootsepsilon` ist die Toleranz, die den Vertrauensbereich fur die von 
der Funktion `realroots` gefundenen Wurzeln festsetzt.

See also: `realroots`.

<!-- category: Other -->
<!-- keywords: solve -->
<!-- signatures: solve(expr, x), solve(expr), solve([eqn_1, ..., eqn_n], [x_1, ..., x_n]) -->
### Function: solve (expr, x)

Lost eine algebraische Gleichung *expr* nach der Variablen *x* auf.
Wenn *expr* keine Gleichung ist, wird die Gleichung `expr = 0` 
angenommen.  *x* kann eine Funktion wie zum Beispiel `f(x)`) sein oder
ein allgemeiner Ausdruck.  Ausgenommen sind Summen und Produkte.  Hat die 
Gleichung nur eine Variable, braucht diese nicht angegeben zu werden.
*expr* kann ein rationaler Ausdruck sein und trigonometrische Funktionen, 
Exponentialfunktionen und andere Funktionen enthalten.  Zur Losung wird die
folgende Methode verwendet:



1. Sei *E* ein Ausdruck und *X* die Variable.  Ist *E* linear in 
*X*, dann kann die Gleichung sofort nach der Variablen `X` aufgelost 
werden.  Hat *E* die Form `A*X^N + B`, dann ist das Ergebnis 
`(-B/A)^1/N)` multipliziert mit der `N`-ten Einheitswurzel.
2. Ist *E* nicht linear in *X*, wird der großte gemeinsame Teiler 
*N* der Exponenten der Variable *X* bestimmt.  Die Exponenten der 
Variablen werden durch *N* dividiert und die Multiplizitat der Losungen 
mit *N* multipliziert.  `solve` wird erneut fur den Ausdruck 
aufgerufen.  Kann *E* faktorisiert werden, wird `solve` fur jeden 
Faktor aufgerufen.  Zuletzt pruft `solve`, ob einer der Algorithmen fur
quadratische, kubische oder quartische Gleichungen angewendet werden kann.
3. Ist *E* ein Polynom in einer Funktion `F(X)` mit *X* als der
Variablen, wird zunachst die Losung des Polynoms fur `F(X)` gesucht.
Ist *C* eine solche Losung, kann die Gleichung `F(X)=C` gelost 
werden, wenn die Umkehrfunktion zu `F(X)` bekannt ist.


Hat die Optionsvariable `breakup` den Wert `false`, werden die
Losungen von kubischen und quartischen Gleichungen nicht in gemeinsame
Teilausdrucke zerlegt.


Die Systemvariable `multiplicities` enthalt eine Liste mit den
Vielfachheiten der einzelnen Losungen.












`solve ([eqn_1, ..., eqn_n], [x_1, ..., x_n])`
lost ein Gleichungssystem mit den Polynomen *eqn_1*, ..., *eqn_n* 
fur die Variablen *x_1*, ..., *x_n*.  Die Polynome konnen linear 
oder nichtlinear sein.  Um das System zu losen, werden die Funktionen 
`linsolve` oder `algsys` aufgerufen.  Das Ergebnis ist eine Liste mit 
den Losungen.  Ist die Anzahl der Gleichungen gleich der Anzahl der Variablen 
des Systems, kann das Argument mit der Liste der Variablen entfallen.


Hat die Optionsvariable `programmode` den Wert `false` ist, zeigt
`solve` die Losungen mit Hilfe von Zwischenmarken (`%t`) an und
gibt die Liste der Marken zuruck.


Hat die Optionsvariable `globalsolve` den Wert `true`, werden den
unbekannten Variablen eines linearen Gleichungssystems die Werte der Losung
der Funktionen `linsolve` und `solve` zugewiesen.


Beispiele:



```maxima
(%i1) solve (asin (cos (3*x))*(f(x) - 1), x);

SOLVE is using arc-trig functions to get a solution.
Some solutions will be lost.
                            %pi
(%o1)                  [x = ---, f(x) = 1]
                             6
(%i2) ev (solve (5^f(x) = 125, f(x)), solveradcan);

                                log(125)
(%o2)                   [f(x) = --------]
                                 log(5)

(%i3) [4*x^2 - y^2 = 12, x*y - x = 2];
                      2    2
(%o3)             [4 x  - y  = 12, x y - x = 2]
(%i4) solve (%, [x, y]);
(%o4) [[x = 2, y = 2], [x = .5202594388652008 %i

 - .1331240357358706, y = .0767837852378778

 - 3.608003221870287 %i], [x = - .5202594388652008 %i

 - .1331240357358706, y = 3.608003221870287 %i

 + .0767837852378778], [x = - 1.733751846381093, 

y = - .1535675710019696]]
(%i5) solve (1 + a*x + x^3, x);
                                       3
              sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(%o5) [x = (- ---------- - -) (--------------- - -)
                  2        2      6 sqrt(3)      2

        sqrt(3) %i   1
       (---------- - -) a
            2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

                          3
 sqrt(3) %i   1   sqrt(4 a  + 27)   1 1/3
(---------- - -) (--------------- - -)
     2        2      6 sqrt(3)      2

         sqrt(3) %i   1
      (- ---------- - -) a
             2        2
 - --------------------------, x = 
              3
      sqrt(4 a  + 27)   1 1/3
   3 (--------------- - -)
         6 sqrt(3)      2

         3
 sqrt(4 a  + 27)   1 1/3               a
(--------------- - -)    - --------------------------]
    6 sqrt(3)      2                  3
                              sqrt(4 a  + 27)   1 1/3
                           3 (--------------- - -)
                                 6 sqrt(3)      2

(%i6) solve (x^3 - 1);

             sqrt(3) %i - 1        sqrt(3) %i + 1
(%o6)   [x = --------------, x = - --------------, x = 1]
                   2                     2

(%i7) solve (x^6 - 1);
           sqrt(3) %i + 1      sqrt(3) %i - 1
(%o7) [x = --------------, x = --------------, x = - 1, 
                 2                   2

                     sqrt(3) %i + 1        sqrt(3) %i - 1
               x = - --------------, x = - --------------, x = 1]
                           2                     2
(%i8) ev (x^6 - 1, %[1]);
                                      6
                      (sqrt(3) %i + 1)
(%o8)                 ----------------- - 1
                             64
(%i9) expand (%);
(%o9)                           0
(%i10) x^2 - 1;
                              2
(%o10)                       x  - 1
(%i11) solve (%, x);
(%o11)                  [x = - 1, x = 1]
(%i12) ev (%th(2), %[1]);
(%o12)                          0
```


Die Symbole `%r` bezeichnen freie Konstanten einer Losung.
Siehe `algsys` und `%rnum_list` fur mehr Informationen.



```maxima
(%i1) solve([x+y=1,2*x+2*y=2],[x,y]);

solve: dependent equations eliminated: (2)
(%o1)                      [[x = 1 - %r1, y = %r1]]
```

See also: `breakup`, `multiplicities`, `linsolve`, `algsys`, `programmode`, `globalsolve`, `%rnum_list`.

<!-- category: Other -->
<!-- keywords: solvedecomposes -->
<!-- signatures: solvedecomposes -->
### Variable: solvedecomposes

Standardwert: `true`





Hat `solvedecomposes` den Wert `true`, ruft `solve` die Funktion
`polydecomp` auf, um Polynome zu zerlegen.

See also: `solve`, `polydecomp`.

<!-- category: Other -->
<!-- keywords: solveexplicit -->
<!-- signatures: solveexplicit -->
### Variable: solveexplicit

Standardwert: `false`


Hat `solveexplicit` den Wert `true`, gibt die Funktion
`solve` keine impliziten Losungen der Form `F(x) = 0` zuruck.


Beispiel:



```maxima
(%i1) solveexplicit:false;
(%o1)                         false
(%i2) solve(gamma(x)*x^3-1);
                           3      1
(%o2)                    [x  = --------]
                               gamma(x)
(%i3) solveexplicit:true;
(%o3)                         true
(%i4) solve(gamma(x)*x^3-1);
(%o4)                          []
```

See also: `solve`.

<!-- category: Other -->
<!-- keywords: solvefactors -->
<!-- signatures: solvefactors -->
### Variable: solvefactors

Standardwert: `true`


Hat `solvefactors` den Wert `false`, versucht die Funktion
`solve` nicht, den Ausdruck zu faktorisieren.  Das Setzen der
Optionsvariable `solvefactors` auf den Wert `false` kann notwendig
sein, wenn die Faktorisierung nicht benotigt wird, damit `solve` eine
Losung findet.

See also: `solve`.

<!-- category: Other -->
<!-- keywords: solvenullwarn -->
<!-- signatures: solvenullwarn -->
### Variable: solvenullwarn

Standardwert: `true`


Hat `solvenullwarn` den Wert `true`, gibt die Funktion
`solve` eine Warnmeldung aus, wenn keine Gleichungen oder keine Variablen
als Argument ubergeben wurden.


Beispiel:



```maxima
(%i1) solvenullwarn:true;
(%o1)                         true
(%i2) solve(x^2*y+1,[]);

solve: variable list is empty, continuing anyway.
(%o2)                          []
(%i3) solvenullwarn:false;
(%o3)                         false
(%i4) solve(x^2*y+1,[]);
(%o4)                          []
```

See also: `solve`.

<!-- category: Other -->
<!-- keywords: solveradcan -->
<!-- signatures: solveradcan -->
### Variable: solveradcan

Standardwert: `false`


Hat `solveradcan` den Wert `true`, ruft `solve` die Funktion
`radcan` auf, um Ausdrucke zu vereinfachen, die Exponentialfunktionen
und Logarithmen enthalten.

See also: `solve`, `radcan`.

<!-- category: Other -->
<!-- keywords: solvetrigwarn -->
<!-- signatures: solvetrigwarn -->
### Variable: solvetrigwarn

Standardwert: `true`


Hat `solvetrigwarn` den Wert `true`, gibt die Funktion
`solve` eine Warnung aus, wenn inverse trigonometrische Funktionen genutzt
werden, um Losungen zu finden.  In diesem Fall konnen Losungen verloren
gehen.


Beispiel:



```maxima
(%i1) solvetrigwarn:true;
(%o1)                         true
(%i2) solve(cos(x)+1);

solve: using arc-trig functions to get a solution.
Some solutions will be lost.
(%o2)                       [x = %pi]
(%i3) solvetrigwarn:false;
(%o3)                         false
(%i4) solve(cos(x)+1);
(%o4)                       [x = %pi]
```

See also: `solve`.

