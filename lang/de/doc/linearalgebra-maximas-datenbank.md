## Maximas Datenbank

<!-- category: LinearAlgebra -->
<!-- keywords: alphabetic -->
<!-- signatures: alphabetic -->
### Variable: alphabetic

Das Kommando `declare(string, alphabetic)` deklariert die Zeichen der 
Zeichenkette *string* als alphabetisch.  Das Argument *string* muss eine
Zeichenkette sein.  Zeichen, die als alphabetisch deklariert sind, konnen in
Maxima-Bezeichnern verwendet werden.  Siehe auch `Bezeichner`.


Beispiele:


Die Zeichen `"~"`, `"@"` und ``` als alphabetisch erklart.



```maxima
(%i1) xx\~yy\`\@ : 1729;
(%o1)                         1729
(%i2) declare ("~`@", alphabetic);
(%o2)                         done
(%i3) xx~yy`@ + @yy`xx + `xx@@yy~;
(%o3)               `xx@@yy~ + @yy`xx + 1729
(%i4) listofvars (%);
(%o4)                  [@yy`xx, `xx@@yy~]
```

See also: `Bezeichner`.

<!-- category: LinearAlgebra -->
<!-- keywords: bindtest -->
<!-- signatures: bindtest -->
### Variable: bindtest

Hat ein Symbol *x* die Eigenschaft `bindtest` und wird es ausgewertet,
ohne das dem Symbol bisher ein Wert zugewiesen wurde, signalisiert Maxima einen 
Fehler.  Siehe auch die Funktion `declare`.


Beispiel:



```maxima
(%i1) aa + bb;
(%o1)                        bb + aa
(%i2) declare (aa, bindtest);
(%o2)                         done
(%i3) aa + bb;
aa unbound variable
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) aa : 1234;
(%o4)                         1234
(%i5) aa + bb;
(%o5)                       bb + 1234
```

See also: `declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: constant -->
<!-- signatures: constant -->
### Variable: constant

Das Kommando `declare(a, constant)` deklariert ein Symbol *a*
als konstant.  Die Funktion `constantp` hat fur dieses Symbol dann das
Ergebnis `true`.  Die Deklaration als eine Konstante verhindert nicht, dass
dem Symbol ein Wert zugewiesen werden kann.  Siehe `declare` und
`constantp`.


Beispiel:



```maxima
(%i1) declare(c, constant);
(%o1)                         done
(%i2) constantp(c);
(%o2)                         true
(%i3) c : x;
(%o3)                           x
(%i4) constantp(c);
(%o4)                         false
```

See also: `constantp`, `declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: constantp -->
<!-- signatures: constantp(expr) -->
### Function: constantp (expr)

Gibt fur einen konstanten Ausdruck *expr* den Wert `true` zuruck,
andernfalls `false`.


Ein Ausdruck wird von Maxima als ein konstanter Ausdruck erkannt, wenn seine 
Argumente Zahlen sind (einschließlich von Zahlen in einer CRE-Darstellung), 
symbolische Konstanten wie `%pi`, `%e` und `%i`, 
Variablen, die einen konstanten Wert haben, Variablen, die mit 
`declare` als konstant deklariert sind, oder Funktionen, deren Argumente 
konstant sind.


Die Funktion `constantp` wertet das Argument aus.


Siehe auch die Eigenschaft `constant`.


Beispiele:



```maxima
(%i1) constantp (7 * sin(2));
(%o1)                                true
(%i2) constantp (rat (17/29));
(%o2)                                true
(%i3) constantp (%pi * sin(%e));
(%o3)                                true
(%i4) constantp (exp (x));
(%o4)                                false
(%i5) declare (x, constant);
(%o5)                                done
(%i6) constantp (exp (x));
(%o6)                                true
(%i7) constantp (foo (x) + bar (%e) + baz (2));
(%o7)                                false
(%i8)
```

See also: `constant`.

<!-- category: LinearAlgebra -->
<!-- keywords: declare -->
<!-- signatures: declare(a_1, p_1, a_2, p_2, ...) -->
### Function: declare (a_1, p_1, a_2, p_2, ...)

Weist dem Symbol *a_i* die Eigenschaft *p_i* zu.  Die Argumente
*a_i* und *p_i* konnen Listen sein.  Ist *a_i* eine Liste, dann
erhalt jedes Symbol der Liste die Eigenschaft *p_i*.  Ist umgekehrt
*p_i* eine Liste mit Eigenschaften, dann erhalt das Symbol *a_i* 
diese Eigenschaften.  Entsprechend erhalten alle Symbole einer Liste *a_i*
die Eigenschaften einer Liste *p_i*.


Die Funktion `declare` wertet die Argumente nicht aus.  `declare` gibt
stets `done` als Ergebnis zuruck.


Hat ein Symbol *sym* die Eigenschaft *prop* mit der Funktion 
`declare` erhalten, dann hat das Kommando `featurep(sym, prop)` das Ergebnis `true`.  Mit der Funktion `properties`
konnen alle Eigenschaften eines Symbols angezeigt werden.


Mit der Funktion `declare` konnen Symbole die folgenden Eigenschaften
erhalten:



**additive** — Hat eine Funktion `f` die Eigenschaft `additive`, wird ein Ausdruck
der Form `f(x + y + z + ...)` zu `f(x) + f(y) + f(z) + ...`
vereinfacht.  Siehe `additive`.
**alphabetic** — *a_i* ist eine Zeichenkette, deren Zeichen als alphabetische Zeichen 
deklariert werden.  Die Zeichen konnen dann in Maxima-Bezeichnern verwendet
werden.  Siehe `alphabetic` fur Beispiele.
**antisymmetric, commutative, symmetric** — *a_i* wird als eine symmetrische, antisymmetrische oder kommutative Funktion
interpretiert.  Die Eigenschaften `commutative` und `symmetric` sind
aquivalent.  Siehe `antisymmetric`, `commutative` und
`symmetric`.
**bindtest** — Hat ein Symbol die Eigenschaft `bindtest` und wird es ausgewertet, ohne 
das dem Symbol bisher ein Wert zugewiesen wurde, signalisiert Maxima einen 
Fehler.  Siehe `bindtest` fur Beispiele.
**constant** — Hat ein Symbol die Eigenschaft `constant`, wird es von Maxima als eine 
Konstante interpretiert.  Siehe auch `constant`.
**even, odd** — Erhalt eine Variable die Eigenschaft `even` oder `odd`, wird sie als
gerade oder ungerade interpretiert.
**evenfun, oddfun** — Erhalt eine Funktion oder ein Operator die Eigenschaft `evenfun` oder 
`oddfun` wird die Funktion oder der Operator von Maxima als gerade und 
ungerade interpretiert.  Diese Eigenschaft wird bei der Vereinfachung von 
Ausdrucken von Maxima angewendet.  Siehe `evenfun` und `oddfun`.
**evflag** — Deklariert die Variable `a_i` als einen Auswertungsschalter.  Wahrend der
Auswertung eines Ausdrucks mit der Funktion `ev`, erhalt der 
Auswertungsschalter `a_i` den Wert `true`.  Siehe `evflag` fur 
Beispiele.
**evfun** — Deklariert eine Funktion *a_i* als eine Auswertungsfunktion.  Tritt die 
Funktion *a_i* als Argument der Funktion `ev` auf, so wird die Funktion
auf den Ausdruck angewendet.  Siehe `evfun` fur Beispiele.
**feature** — *a_i* wird als eine Eigenschaft `feature` interpretiert.  Andere
Symbole konnen dann diese vom Nutzer definierte Eigenschaft erhalten.
Siehe `feature`.
**increasing, decreasing** — Erhalt eine Funktion die Eigenschaft `decreasing` oder `increasing`, 
wird die Funktion als eine monoton steigende oder fallende Funktion
interpretiert.  Siehe `decreasing` und `increasing`.
**integer, noninteger** — *a_i* wird als eine ganzzahlige oder nicht-ganzzahlige Variable
interpretiert.  Siehe `integer` und `noninteger`.
**integervalued** — Erhalt eine Funktion die Eigenschaft `integervalued`, nimmt Maxima fur
Vereinfachungen an, dass die Funktionen einen ganzzahligen Wertebereich hat.
Fur ein Beispiel siehe `integervalued`.
**lassociative, rassociative** — *a_i* wird als eine rechts- oder links-assoziative Funktion interpretiert.
Siehe `lassociative` und `rassociative`.
**linear** — Entspricht der Deklaration einer Funktion als `outative` und
`additive`.  Siehe auch `linear`.
**mainvar** — Wird eine Variable als *mainvar* deklariert, wird sie als eine 
"Hauptvariable" interpretiert.  Eine Hauptvariable wird vor allen Konstanten und
Variablen in einer kanonischen Ordnung eines Maxima-Ausdruckes angeordnet.
Die Anordnung wird durch die Funktion `ordergreatp` bestimmt.  Siehe auch
`mainvar`.
**multiplicative** — Hat eine Funktion `f` die Eigenschaft `multiplicative`, werden
Ausdrucke der Form `a_i(x * y * z * ...)` zu
`a_i(x) * a_i(y) * a_i(z) * ...` vereinfacht.  Die
Vereinfachung wird nur fur das erste Argument der Funktion *f*
ausgefuhrt.  Siehe `multiplicative`.
**nary** — Erhalt eine Funktion oder ein Operator die Eigenschaft `nary`, wird die
Funktion oder der Operator bei der Vereinfachung als Nary-Funktion oder
Nary-Operator interpretiert.  Verschachtelte Ausdrucke wie 
`foo(x, foo(y, z))` werden zum Beispiel zu `foo(x, y, z)` vereinfacht.
Die Deklaration `nary` unterscheidet sich von der Funktion `nary`.
Wahrend der Funktionsaufruf einen neuen Operator definiert, wirkt sich die 
Deklaration nur auf die Vereinfachung aus.  Siehe auch 
`property_nary`.
**nonarray** — Hat ein Symbol *a_i* die Eigenschaft `nonarray`, wird es nicht als ein
Array interpretiert, wenn das Symbol einen Index erhalt.  Diese Deklaration
verhindert die mehrfache Auswertung, wenn *a_i* als indizierte Variable
genutzt wird.  Siehe  `nonarray`.
**nonscalar** — *a_i* wird als eine nicht-skalare Variable interpretiert.  Ein Symbol wird
also als ein Vektor oder eine Matrix deklariert.  Siehe `nonscalar`.
**noun** — *a_i* wird als Substantivform interpretiert.  Abhangig vom Kontext wird 
*a_i* durch `'a_i` oder `nounify(a_i)` ersetzt.
Siehe auch `noun`. fur ein Beispiel.
**outative** — Ausdrucke mit der Funktion *a_i* werden so vereinfacht, dass konstante 
Faktoren aus dem Argument herausgezogen werden.  Hat die Funktion *a_i* ein 
Argument, wird ein Faktor dann als konstant angesehen, wenn er ein Symbol oder 
eine deklarierte Konstante ist.  Hat die Funktion *a_i* zwei oder mehr 
Argumente, wird ein Faktor dann als konstant angesehen, wenn das zweite Argument
ein Symbol und der Faktor unabhangig vom zweiten Argument ist.  Siehe auch
`outative`.
**posfun** — *a_i* wird als eine Funktion interpretiert, die nur positive Werte hat.
Siehe `posfun`.
**rational, irrational** — *a_i* wird als eine rationale oder irrationale Zahl interpretiert.  Siehe
`rational` und `irrational`.
**real, imaginary, complex** — *a_i* wird als eine reelle, imaginare oder komplexe Zahl interpretiert.
Siehe `real`, `imaginary` und `complex`.
**scalar** — *a_i* wird als skalare Variable interpretiert.  Siehe `scalar`.

See also: `additive`, `alphabetic`, `antisymmetric`, `commutative`, `symmetric`, `bindtest`, `constant`, `evenfun`, `oddfun`, `evflag`, `evfun`, `feature`, `decreasing`, `increasing`, `integer`, `noninteger`, `integervalued`, `lassociative`, `rassociative`, `linear`, `mainvar`, `multiplicative`, `property_nary`, `nonarray`, `nonscalar`, `noun`, `outative`, `posfun`, `rational`, `irrational`, `real`, `imaginary`, `complex`, `scalar`.

<!-- category: LinearAlgebra -->
<!-- keywords: decreasing, increasing -->
<!-- signatures: increasing -->
### Variable: decreasing

Erhalt eine Funktion mit der Funktion `declare` die Eigenschaft 
`decreasing` oder `increasing` wird die Funktion als eine steigende 
oder fallende Funktion interpretiert.


Beispiel:



```maxima
(%i1) assume(a > b);
(%o1)                        [a > b]
(%i2) is(f(a) > f(b));
(%o2)                        unknown
(%i3) declare(f, increasing);
(%o3)                         done
(%i4) is(f(a) > f(b));
(%o4)                         true
```

See also: `declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: even, odd -->
<!-- signatures: odd -->
### Variable: even

Hat eine Variable mit der Funktion `declare` die Eigenschaft `even`
oder `odd` erhalten, wird sie von Maxima als gerade oder ungerade
ganze Zahl interpretiert.  Diese Eigenschaften werden jedoch nicht von den
Funktionen `evenp`, `oddp` oder `integerp` erkannt.


Siehe auch die Funktion `askinteger`.


Beispiele:



```maxima
(%i1) declare(n, even);
(%o1)                         done
(%i2) askinteger(n, even);
(%o2)                          yes
(%i3) askinteger(n);
(%o3)                          yes
(%i4) evenp(n);
(%o4)                         false
```

See also: `declare`, `evenp`, `oddp`, `integerp`, `askinteger`.

<!-- category: LinearAlgebra -->
<!-- keywords: feature -->
<!-- signatures: feature -->
### Variable: feature

`feature` ist eine Eigenschaft, die ein Symbol *sym* mit der Funktion
`declare` erhalten kann.  In diesem Fall ist das Symbol *sym* selbst
eine Eigenschaft, so dass das Kommando `declare(x, sym)` einem Symbol
*x* die vom Nutzer definierte Eigenschaft `sym` gibt.


Maxima unterscheidet Systemeigenschaften und mathematische Eigenschaften, die 
Symbole und Ausdrucke haben konnen.  Fur Systemeigenschaften siehe die 
Funktion `status`.  Fur mathematische Eigenschaften siehe die 
Funktionen `declare` und `featurep`.


Beispiel:



```maxima
(%i1) declare (FOO, feature);
(%o1)                         done
(%i2) declare (x, FOO);
(%o2)                         done
(%i3) featurep (x, FOO);
(%o3)                         true
```

See also: `status`, `declare`, `featurep`.

<!-- category: LinearAlgebra -->
<!-- keywords: featurep -->
<!-- signatures: featurep(a, p) -->
### Function: featurep (a, p)

Stellt fest, ob das Symbol oder der Ausdruck *a* die Eigenschaft *p* 
hat.  Maxima nutzt die Fakten der aktiven Kontexte und die definierten
Eigenschaften fur Symbole und Funktionen.


`featurep` gibt sowohl fur den Fall `false` zuruck, dass das 
Argument *a* nicht die Eigenschaft *p* hat, als auch fur den Fall, 
dass Maxima dies nicht anhand der bekannten Fakten und Eigenschaften entscheiden
kann.


`featurep` wertet die Argumente aus.


Siehe auch `declare` und `featurep`..


Beispiele:



```maxima
(%i1) declare (j, even)$
(%i2) featurep (j, integer);
(%o2)                           true
```

See also: `declare`, `featurep`.

<!-- category: LinearAlgebra -->
<!-- keywords: features -->
<!-- signatures: features -->
### Variable: features

Maxima kennt spezielle mathematische Eigenschaften von Funktionen und 
Variablen.


`declare(x)`, *foo* gibt der Funktion oder Variablen *x* die
Eigenschaft *foo*.


`declare(foo, feature)` deklariert die neue Eigenschaft *foo*.
Zum  Beispiel deklariert `declare([red, green, blue], feature)` die drei 
neuen Eigenschaften `red`, `green` und `blue`.


`featurep(x, foo)` hat die Ruckgabe `true`, wenn *x* 
die Eigenschaft *foo* hat.  Ansonsten wird `false` zuruckgegeben.


Die Informationsliste `features` enthalt eine Liste der Eigenschaften, 
die Funktionen und Variablen erhalten konnen und die in die Datenbank
eingetragen werden:



   integer         noninteger       even 
   odd             rational         irrational
   real            imaginary        complex
   analytic        increasing       decreasing
   oddfun          evenfun          posfun
   commutative     lassociative     rassociative
   symmetric       antisymmetric


Hinzu kommen die vom Nutzer definierten Eigenschaften.


`features` ist eine Liste der mathematischen Eigenschaften.  Es gibt 
weitere Eigenschaften.  Siehe `declare` und `status`.

See also: `declare`, `status`.

<!-- category: LinearAlgebra -->
<!-- keywords: get -->
<!-- signatures: get(a, i) -->
### Function: get (a, i)

Gibt die Eigenschaft *i* des Symbols *a* zuruck.  Hat das Symbol
*a* nicht die Eigenschaft *i*, wird `false` zuruckgegeben.


`get` wertet die Argumente aus.


Beispiele:



```maxima
(%i1) put (%e, 'transcendental, 'type);
(%o1)                    transcendental
(%i2) put (%pi, 'transcendental, 'type)$
(%i3) put (%i, 'algebraic, 'type)$
(%i4) typeof (expr) := block ([q],
        if numberp (expr)
        then return ('algebraic),
        if not atom (expr)
        then return (maplist ('typeof, expr)),
        q: get (expr, 'type),
        if q=false
        then errcatch (error(expr,"is not numeric.")) else q)$
(%i5) typeof (2*%e + x*%pi);
x is not numeric.
(%o5)  [[transcendental, []], [algebraic, transcendental]]
(%i6) typeof (2*%e + %pi);
(%o6)     [transcendental, [algebraic, transcendental]]
```

<!-- category: LinearAlgebra -->
<!-- keywords: integer, noninteger -->
<!-- signatures: noninteger -->
### Variable: integer

Hat eine Variable mit der Funktion `declare` die Eigenschaft `integer`
oder `noninteger` erhalten, wird sie von Maxima als eine ganze Zahl oder 
als nicht-ganze Zahl interpretiert.  Siehe auch `askinteger`.


Beispiele:



```maxima
(%i1) declare(n, integer, x, noninteger);
(%o1)                         done
(%i2) askinteger(n);
(%o2)                          yes
(%i3) askinteger(x);
(%o3)                          no
```

See also: `declare`, `askinteger`.

<!-- category: LinearAlgebra -->
<!-- keywords: integervalued -->
<!-- signatures: integervalued -->
### Variable: integervalued

Erhalt eine Funktion mit `declare` die Eigenschaft `integervalued`,
nimmt Maxima fur Vereinfachungen an, dass der Wertebereich der Funktion
ganzzahlig ist.


Beispiel:



```maxima
(%i1) exp(%i)^f(x);
                              %i f(x)
(%o1)                      (%e  )
(%i2) declare(f, integervalued);
(%o2)                         done
(%i3) exp(%i)^f(x);
                              %i f(x)
(%o3)                       %e
```

See also: `declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: nonarray -->
<!-- signatures: nonarray -->
### Function: nonarray

`declare(a, nonarray)` gibt dem Symbol *a* die Eigenschaft nicht ein
Array zu sein.  Dies verhindert die mehrfache Auswertung, wenn das Symbol
*a* als indizierte Variable genutzt wird.


Beispiel:



```maxima
(%i1) a:'b$ b:'c$ c:'d$

(%i4) a[x];
(%o4)                          d
                                x
(%i5) declare(a, nonarray);
(%o5)                         done
(%i6) a[x];
(%o6)                          a
                                x
```

<!-- category: LinearAlgebra -->
<!-- keywords: nonscalar -->
<!-- signatures: nonscalar -->
### Variable: nonscalar

Hat ein Symbol die Eigenschaft `nonscalar`, verhalt es sich wie eine
Matrix oder Liste bei nicht-kommutativen Rechenoperationen.

<!-- category: LinearAlgebra -->
<!-- keywords: nonscalarp -->
<!-- signatures: nonscalarp(expr) -->
### Function: nonscalarp (expr)

Gibt `true` zuruck, wenn der Ausdruck *expr* kein Skalar ist.  Der
Ausdruck enthalt dann Matrizen, Listen oder Symbole, die als `nonscalar`
deklariert wurden.

<!-- category: LinearAlgebra -->
<!-- keywords: posfun -->
<!-- signatures: posfun -->
### Variable: posfun

`declare(f, posfun)` deklariert die Funktion `f` als eine Funktion,
die nur positive Werte annimmt.  `is(f(x) > 0)` gibt dann `true`
zuruck.

<!-- category: LinearAlgebra -->
<!-- keywords: printprops -->
<!-- signatures: printprops(a, i), printprops([a_1, ..., a_n], i), printprops(all, i) -->
### Function: printprops (a, i)

Zeigt die zum Kennzeichen *i* zugeordnete Eigenschaft des Atoms *a* an.
*i* kann einer der Werte `gradef`, `atvalue`, `atomgrad` oder
`matchdeclare` sein.  *a* kann sowohl eine Liste von Atomen, als auch
das Atom `all` sein.  In diesem Fall werden alle Atome angezeigt, die eine
Eigenschaft zum Kennzeichen *i* haben.


Beispiel:



```maxima
(%i1) gradef(f(x), 2*g(x));
(%o1)                         f(x)
(%i2) printprops(f,gradef);
                       d
                       -- (f(x)) = 2 g(x)
                       dx

(%o2)                         done
```

<!-- category: LinearAlgebra -->
<!-- keywords: properties -->
<!-- signatures: properties(a) -->
### Function: properties (a)

Gibt eine Liste mit den Eigenschaften zuruck, die das Symbol *a* von
Maxima oder dem Nutzer erhalten hat.  Die Ruckgabe kann jede Eigenschaft
enthalten, die mit der Funktion `declare` einem Symbol zugewiesen ist.
Diese Eigenschaften sind:



   linear         additive       multiplicative
   outative       commutative    symmetric      
   antisymmetric  nary           lassociativ
   rassociative   evenfun        oddfun
   bindtest       feature        alphabetic
   scalar         nonscalar      nonarray
   constant       integer        noninteger
   even           odd            rational
   irrational     real           imaginary
   complex        increasing     decreasing
   posfun         integervalued


Die folgenden Eintrage beschreiben Eigenschaften, die Variablen haben
konnen:



**value** — Der Variable ist mit dem Operatoren `:` oder `::` ein Wert zugewiesen.
**system value** — Die Variable ist eine Optionsvariable oder Systemvariable, die von Maxima
definiert ist.
**numer** — Die Variable hat einen numerischen Wert auf der Eigenschaftsliste, der mit
der Funktion `numerval` zugewiesen ist.
**assign property** — Die Variable hat eine eine Funktion auf der Eigenschaftsliste, die die Zuweisung
eines Wertes kontrolliert.


Eintrage, die die Eigenschaften von Funktionen beschreiben:



**function** — Eine mit dem Operator `:=` oder der Funktion `define` definierte
Nutzerfunktion.
**macro** — Eine mit dem Operator `::=` definierte Makrofunktion.
**system function** — Ein interne Maxima-Funktion.
**special evaluation form** — Eine Maxima-Spezialform, die die Argumente nicht auswertet.
**transfun** — Wird eine Nutzerfunktion mit `translate` ubersetzt oder mit der Funktion
`compile` kompiliert, erhalt sie die Eigenschaft `transfun`.
Interne Maxima-Funktionen, die mit dem Lisp-Makro `defmfun` definiert
werden, haben ebenfalls diese Eigenschaft.
**deftaylor** — Fur die Funktion ist eine Taylorreihenentwicklung definiert.
**gradef** — Die Funktion hat eine Ableitung.
**integral** — Die Funktion hat eine Stammfunktion.
**distribute over bags** — Ist das Argument der Funktion eine Liste, Matrix oder Gleichung so wird die
Funktion auf die Elemente oder beide Seiten der Gleichung angewendet.
**limit function** — Es existiert eine Funktion fur die Behandlung spezieller Grenzwerte.
**conjugate function** — Es existiert eine Funktion, um die konjugiert komplexe Funktion fur spezielle
Wertebereiche zu ermitteln.
**mirror symmetry** — Die Funktion hat die Eigenschaft der Spiegelsymmetrie.
**complex characteristic** — Es existiert eine Funktion, um den Realteil und den Imaginarteil der Funktion
fur spezielle Wertebereiche zu ermitteln.
**user autoload function** — Die Funktion wird automatisch beim ersten Aufruf aus einer Datei geladen.  Der
Nutzer kann mit dem Funktion `setup_autoload` eine solche Funktion
definieren.


Weitere Eigenschaften, die Symbole erhalten konnen:



**operator** — Das Symbol ist ein Maxima-Operator oder ein nutzerdefinierte Operator.
**rule** — Die Funktion oder der Operator haben eine Regel fur die Vereinfachung.
**alias**
**database info** — Das Symbol hat Eintrage in Maximas Datenbank.
**hashed array, declared array, complete array** — Ein Hashed-Array, ein deklariertes Array oder ein Array dessen Elemente
einen bestimmten Typ haben.
**array function** — Eine Array-Funktion die mit dem Operator `:=` definiert ist.
**atvalue** — Dem Symbol ist mit der Funktion `atvalue` ein Wert an einer Stelle
zugewiesen.
**atomgrad** — Fur das Symbol ist mit der Funktion `gradef` eine Ableitung definiert.
**dependency** — Fur das Symbol ist eine Abhangigkeit mit der Funktion `depends`
definiert.
**matchdeclare** — Das Symbol ist eine mit `matchdeclare` definierte Mustervariable, der eine
Aussagefunktion zugeordnet ist.
**modedeclare** — Fur das Symbol ist mit der Funktion `mode_declare` ein Typ definiert.
**user properties**
**context** — Das Symbol bezeichnet einen Kontext.
**activecontext** — Das Symbol bezeichnet einen aktiven Kontextes.

See also: `declare`, `:`, `::`, `numerval`, `:=`, `define`, `::=`, `translate`, `compile`, `setup_autoload`, `atvalue`, `gradef`, `depends`, `matchdeclare`, `mode_declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: props -->
<!-- signatures: props -->
### Variable: props

Standardwert: `[]`


`props` ist eine Liste der Symbole, die vom Nutzer eine Eigenschaft
erhalten haben, die in die Lisp-Eigenschaftsliste des Symbols eingetragen wird.
Neben den Funktionen `put` und `qput`, mit denen der Nutzer
direkt eine Eigenschaft zu einem Symbol in die Lisp-Eigenschaftsliste eintragen
kann, legen auch Maxima-Funktionen Eigenschaften zu Symbolen in der 
Eigenschaftsliste ab und tragen diese Symbole in die Systemvariable `props`
ein.  Zu diesen Funktionen gehoren zum Beispiel `declare`,
`numerval`, `matchdeclare`, `mode_declare`,
`gradef` oder `setup_autoload`.


Nach dem Start von Maxima sollte die Systemvariable `props` keine Symbole
enthalten.  Das ist jedoch nicht der Fall und kann als ein Fehler betrachtet
werden, der in Zukunft zu beheben ist.

See also: `put`, `qput`, `declare`, `numerval`, `matchdeclare`, `mode_declare`, `gradef`, `setup_autoload`.

<!-- category: LinearAlgebra -->
<!-- keywords: propvars -->
<!-- signatures: propvars(prop) -->
### Function: propvars (prop)

Gibt eine Liste mit den Atomen zuruck, die in der Informationsliste 
`props` eingetragen sind und die die Eigenschaft *prop* haben.  Zum 
Beispiel gibt `propvars(atvalue)` eine Liste der Atome zuruck, die die 
Eigenschaft `atvalue` haben.

<!-- category: LinearAlgebra -->
<!-- keywords: put -->
<!-- signatures: put(atom, value, indicator) -->
### Function: put (atom, value, indicator)

Weist den Wert *value* der Eigenschaft *indicator* des Atoms *atom*
zu.  *indicator* kann eine beliebige Eigenschaft sein und beschrankt sich
nicht auf die vom System definierten Eigenschaften.  `put` wertet die 
Argumente aus.  `put` gibt *value* zuruck.


Beispiele:



```maxima
(%i1) put (foo, (a+b)^5, expr);
                                   5
(%o1)                       (b + a)
(%i2) put (foo, "Hello", str);
(%o2)                         Hello
(%i3) properties (foo);
(%o3)            [[user properties, str, expr]]
(%i4) get (foo, expr);

                                   5
(%o4)                       (b + a)

(%i5) get (foo, str);
(%o5)                         Hello
```

<!-- category: LinearAlgebra -->
<!-- keywords: qput -->
<!-- signatures: qput(atom, value, indicator) -->
### Function: qput (atom, value, indicator)

Entspricht der Funktion `put` mit dem Unterschied, dass `qput` die
Argumente nicht auswertet.


Beispiele:



```maxima
(%i1) foo: aa$ 
(%i2) bar: bb$
(%i3) baz: cc$
(%i4) put (foo, bar, baz);
(%o4)                          bb
(%i5) properties (aa);
(%o5)                [[user properties, cc]]
(%i6) get (aa, cc);
(%o6)                          bb
(%i7) qput (foo, bar, baz);
(%o7)                          bar
(%i8) properties (foo);
(%o8)            [value, [user properties, baz]]
(%i9) get ('foo, 'baz);
(%o9)                          bar
```

<!-- category: LinearAlgebra -->
<!-- keywords: rational, irrational -->
<!-- signatures: irrational -->
### Variable: rational

Hat eine Variable mit der Funktion `declare` die Eigenschaft 
`rational` oder `irrational` erhalten, wird sie von Maxima als eine 
rationale Zahl oder als eine nicht rationale Zahl interpretiert.

See also: `declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: real, imaginary, complex -->
<!-- signatures: imaginary, complex -->
### Variable: real

Hat eine Variable mit der Funktion `declare` die Eigenschaft `real`,
`imaginary` oder `complex` erhalten, wird sie von Maxima als eine 
reelle Zahl, imaginare Zahl oder als eine komplexe Zahl interpretiert.

See also: `declare`.

<!-- category: LinearAlgebra -->
<!-- keywords: rem -->
<!-- signatures: rem(atom, indicator) -->
### Function: rem (atom, indicator)

Entfernt die Eigenschaft *indicator* vom Atom *atom*.

<!-- category: LinearAlgebra -->
<!-- keywords: remove -->
<!-- signatures: remove(a_1, p_1, ..., a_n, p_n), remove([a_1, ..., a_m], [p_1, ..., p_n], ...), remove("a", operator), remove(a, transfun), remove(all, p) -->
### Function: remove (a_1, p_1, ..., a_n, p_n)

Entfernt Eigenschaften von Atomen.


Aussagen im Kontext `global` sind fest in Maxima eingebaut und konnen
mit `remove` nicht entfernt werden. In diesem Fall gibt `remove`
`not_done` zuruck. Der Ruckgabewert `done` bedeutet jedoch nicht,
dass die angegebene Eigenschaft tatschlich vorhanden war.


`remove(a_1, p_1, ..., a_n, p_n)` entfernt die
Eigenschaft `p_k` von dem Atom `a_k`.


`remove([a_1, ..., a_m], [p_1, ..., p_n], ...)`
entfernt die Eigenschaften *p_1*, ..., *p_n* von den Atomen 
*a_1*, ..., *a_m*.  Es konnen mehrere Paare an Listen angegeben 
werden.


`remove(all, p)` entfernt die Eigenschaft *p* von allen Atomen, 
die diese Eigenschaft aufweisen.


Die zu entfernenden Eigenschaften konnen vom System definierte Eigenschaften
wie `function`, `macro`, `mode_declare` oder nutzerdefinierte
Eigenschaften sein.


`remove("a", operator)` oder `remove("a", op)`
entfernen vom Atom *a* die Operatoreigenschaften, die mit den Funktionen
`prefix`, `infix`, `nary`, `postfix`,
`matchfix` oder `nofix` definiert wurden.  Die Namen von Operatoren
mussen als eine Zeichenkette angegeben werden.


`remove` gibt immer `done` zuruck.

See also: `prefix`, `infix`, `nary`, `postfix`, `matchfix`, `nofix`.

<!-- category: LinearAlgebra -->
<!-- keywords: scalar -->
<!-- signatures: scalar -->
### Variable: scalar

Hat ein Symbol die Eigenschaft `scalar`, verhalt es sich wie ein Skalar 
bei nicht-kommutativen Rechenoperationen.

<!-- category: LinearAlgebra -->
<!-- keywords: scalarp -->
<!-- signatures: scalarp(expr) -->
### Function: scalarp (expr)

Gibt `true` zuruck, wenn der Ausdruck *expr* eine Zahl, Konstante, 
ein als Skalar definiertes Symbol oder ein aus diesen Objekten zusammengesetzter
Ausdruck ist.  Der Ausdruck darf jedoch keine Liste oder eine Matrix sein.

