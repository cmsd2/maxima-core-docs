## Analysis

<!-- category: Other -->
<!-- keywords: lhospitallim -->
<!-- signatures: lhospitallim -->
### Variable: lhospitallim

Standardwert: 4


Die Optionsvariable `lhospitallim` enthalt die maximale Zahl an
Iterationen, fur die die L’Hospitalsche Regel von der Funktion
`limit` angewendet wird.  Damit wird verhindert, dass die Funktion
`limit` in eine unendliche Schleife gerat.

See also: `limit`.

<!-- category: Other -->
<!-- keywords: limit -->
<!-- signatures: limit(expr, x, val, dir), limit(expr, x, val), limit(expr) -->
### Function: limit (expr, x, val, dir)

Berechnet den Grenzwert des Ausdrucks *expr*, wenn die reelle Variable
*x* gegen den Wert *val* in Richtung *dir* geht.  Die Richtung
*dir* kann die Werte *plus* fur einen Grenzwert von oben und 
*minus* fur einen Grenzwert von unten haben.  Fur einen zweiseitigen 
Grenzwert wird die Richtung *dir* nicht angegeben.


Maxima verwendet die folgenden Symbole fur unendliche und infinitesimale 
Großen sowie undefinierte und unbestimmte Großen, die als
Ergebnis eines Grenzwertes oder als Wert fur die Bestimmung eines Grenzwertes 
auftreten konnen:



**inf** — positiv unendlich
**minf** — negativ unendlich
**infinity** — komplex unendlich
**zeroa** — positiv unendlich klein
**zerob** — negativ unendlich klein
**und** — ein nicht definiertes Ergebnis
**ind** — ein unbestimmtes Ergebnis














Die Optionsvariable `lhospitallim` enthalt die maximale Zahl an
Iterationen, fur die die L’Hospitalsche Regel von der Funktion `limit`
angewendet wird.


Hat `tlimswitch` den Wert `true`, nutzt die Funktion `limit` eine
Taylor-Rei­hen­ent­wick­lung, wenn der Grenzwert nicht mit anderen Methoden 
bestimmt werden kann.


Hat die Optionsvariable `limsubst` den Wert `false`, wird die
Ersetzung von `limit(f(g(x)),x,x0)` durch `f(limit(g(x),x,x0))` fur
eine unbekannte Funktion `f` verhindert.  Siehe auch `limsubst`.


`limit` kann mit einem Argument aufgerufen werden, um Ausdrucke
zu vereinfachen, die unendliche oder infinitesimale Großen enthalten.
Zum Beispiel wird `limit(inf-1)` zu `inf` vereinfacht.


Der Algorithmus ist in der folgenden Arbeit beschrieben: Wang, P., "Evaluation 
of Definite Integrals by Symbolic Manipulation", Ph.D. thesis, MAC TR-92, 
October 1971.


Beispiele:



```maxima
(%i1) limit(x*log(x),x,0,plus)
(%o1)                           0
(%i2) limit((x+1)^(1/x),x,0)
(%o2)                          %e
(%i3) limit(%e^x/x,x,inf)
(%o3)                          inf
(%i4) limit(sin(1/x),x,0)
(%o4)                          ind
```

See also: `lhospitallim`, `tlimswitch`, `limsubst`.

<!-- category: Other -->
<!-- keywords: limsubst -->
<!-- signatures: limsubst -->
### Variable: limsubst

Standardwert: `false`


Ist eine Funktion `f` teil eines Ausdrucks fur den Maxima den Grenzwert 
sucht, dann wird folgende Ersetzung ausgefuhrt:



```maxima
limit   f(g(x)) = f(limit   g(x))
   x -> x0             x -> x0
```


Hat die Optionsvariable `limsubst` den Wert `false`, fuhrt 
`limit` die oben gezeigte Ersetzung nicht fur unbekannte Funktionen 
`f` aus.  Dies vermeidet Fehler wie zum Beispiel ein Ergebnis von 1 fur 
den Grenzwert `limit (f(n)/f(n+1), n, inf)`.  Hat `limsubst` den Wert 
`true`, fuhrt Maxima die oben gezeigte Ersetzung auch fur unbekannte 
Funktionen `f` aus.


Beispiele:


Die Funktion `f` ist nicht definiert.  Maxima gibt im ersten Fall eine
Substantivform zuruck.  Im zweiten Fall nimmt Maxima den Grenzwert fur die
unbekannte Funktion als `f(10)` an.



```maxima
(%i1) limit(f(x),x,10),limsubst:false;
(%o1)                     limit   f(x)
                          x -> 10
(%i2) limit(f(x),x,10),limsubst:true;
(%o2)                         f(10)
```

See also: `limit`.

<!-- category: Other -->
<!-- keywords: tlimit -->
<!-- signatures: tlimit(expr, x, val, dir), tlimit(expr, x, val), tlimit(expr) -->
### Function: tlimit (expr, x, val, dir)

Bestimmt den Grenzwert mit Hilfe der Taylor-Reihenwicklung des Ausdrucks
`expr`, wenn die Variable *x* gegen den Wert `val` aus der
Richtung *dir* geht.  Diese Methode wird von `limit` angewendet, wenn
die Optionsvariable `tlimswitch` den Wert `true` ist.  Das ist der
Standardwert.

See also: `tlimswitch`.

<!-- category: Other -->
<!-- keywords: tlimswitch -->
<!-- signatures: tlimswitch -->
### Variable: tlimswitch

Standardwert: `true`


Hat `tlimswitch` den Wert `true`, nutzt die Funktion `limit` eine
Taylor-Rei­hen­ent­wick­lung, wenn der Grenzwert nicht mit anderen Methoden
bestimmt werden kann.

See also: `limit`.

