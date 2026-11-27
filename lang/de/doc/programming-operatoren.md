## Operatoren

<!-- category: Programming -->
<!-- keywords: # -->
<!-- signatures: # -->
### Function: #

Ist der Operator fur eine Ungleichung.  `#` ist ein Infix-Operator mit
zwei Operanden.


Mit dem Operator `#` wird eine Ungleichung `a # b` formuliert, wobei
die Operanden `a` und `b` jeweils die linke und die rechte Seite der
Ungleichung sind und beliebige Ausdrucke sein konnen.  Die Operanden werden
ausgewertet, nicht jedoch die Ungleichung selbst.


Die Funktionen `is`, `maybe`, die logischen Operatoren
`and`, `or` und `not` sowie die Funktionen fur die
Definition von Programmanweisungen wie `if`, `while` oder
`unless` erzwingen die Auswertung einer Ungleichung.


Wegen der Regeln fur die Auswertung von Aussagen und weil `not expr` die
Auswertung des Argumentes `expr` bewirkt, ist der Ausdruck
`not (a = b)` aquivalent zu `is(a # b)` und nicht zu `a # b`.


Die Funktionen `rhs` und `lhs` geben die rechte und die linke Seite
einer Gleichung oder Ungleichung zuruck.


Siehe auch den Operator `=`, um eine Gleichung zu formulieren, sowie
die Funktionen `equal` und `notequal`.


Beispiele:



```maxima
(%i1) a = b;
(%o1)                         a = b
(%i2) is (a = b);
(%o2)                         false
(%i3) a # b;
(%o3)                         a # b
(%i4) not (a = b);
(%o4)                         true
(%i5) is (a # b);
(%o5)                         true
(%i6) is (not (a = b));
(%o6)                         true
```

See also: `is`, `maybe`, `and`, `or`, `not`, `if`, `while`, `unless`, `rhs`, `lhs`, `=`, `equal`, `notequal`.

<!-- category: Programming -->
<!-- keywords: ** -->
<!-- signatures: ** -->
### Function: **

Ist eine alternative Schreibweise fur den Operator `^` der 
Exponentiation.  In der Ausgabe wird entweder `^` angezeigt oder der 
Exponent hochgestellt.  Siehe den Operator der Exponentiation `^`.


Die Funktion `fortran` zeigt den Operator der Exponentiation immer als 
`**` an, unabhangig davon, ob `**` oder `^` eingegeben wird.


Beispiele:



```maxima
(%i1) is (a**b = a^b);
(%o1)                         true
(%i2) x**y + x^z;
                              z    y
(%o2)                        x  + x
(%i3) string (x**y + x^z);
(%o3)                        x^z+x^y
(%i4) fortran (x**y + x^z);
      x**z+x**y
(%o4)                         done
```

See also: `^`, `fortran`.

<!-- category: Programming -->
<!-- keywords: +, -, *, /, ^ -->
<!-- signatures: -, *, /, ^ -->
### Function: +

Sind die Operatoren der Addition, Multiplikation, Division und Exponentiation.
Wird der Name eines Operators in einem Ausdruck benotigt, konnen die
Bezeichnungen `"+"`, `"*"`, `"/"` und `"^"` verwendet
werden.


In Ausdrucken wie `(+a)*(-a)` oder `exp(-a)` reprasentieren die
Operatoren `+` und `-` die unare Addition und Negation.  Die Namen
der Operatoren sind `"+"` und `"-"`.


Die Subtraktion `a - b` wird von Maxima intern als Addition
`a + (- b)` dargestellt.  In der Ausgabe wird der Ausdruck `a + (- b)`
als Subtraktion `a - b` angezeigt.


Die Division `a / b` wird von Maxima intern als Multiplikation
`a * b^(- 1)` dargestellt.  In der Ausgabe wird der Ausdruck
`a * b^(- 1)` als Division `a / b` angezeigt.  Der Name des Operators
fur die Division ist `"/"`.


Die Operatoren der Addition und Multiplikation sind kommutative
N-ary-Operatoren.  Die Operatoren der  Division und Exponentiation sind
nicht-kommutative binare Operatoren.


Maxima sortiert die Operanden eines kommutativen Operators und konstruiert eine
kanonische Darstellung.  Maxima unterscheidet die interne Sortierung von der
externen Sortierung fur die Anzeige.  Die interne Sortierung wird von der
Aussagefunktion `orderlessp` bestimmt.  Die externe Sortierung fur die
Anzeige wird von der Aussagefunktion `ordergreatp` festgelegt.  Ausnahme
ist die Multiplikation.  Fur diese sind die interne und die externe
Sortierung identisch.


Arithmetische Rechnungen mit Zahlen (ganzen Zahlen, rationale Zahlen,
Gleitkommazahlen und großen Gleitkommazahlen) werden als eine Vereinfachung
und nicht als Auswertung  ausgefuhrt.  Mit Ausnahme der Exponentiation werden
alle arithmetischen Operationen mit Zahlen zu Zahlen vereinfacht.
Exponentiationen von Zahlen wie zum Beispiel `(1/3)^(1/2)` werden nicht
notwendigerweise zu Zahlen vereinfacht.  In diesem Beispiel ist das Ergebnis
der Vereinfachung `1/sqrt(3)`.


Bei einer arithmetischen Rechnung kann es zur Umwandlung in Gleitkommazahlen
kommen.  Ist eines der Argumente eine große Gleitkommazahl, so ist auch das
Ergebnis eine große Gleitkommazahl.  Entsprechend ist das Ergebnis eine
einfache Gleitkommazahl, sofern mindestens einer der Operanden eine einfache
Gleitkommazahl ist.  Treten nur ganze oder rationale Zahlen auf, ist das
Ergebnis wieder eine ganze oder rationale Zahl.


Da arithmetische Rechnungen Vereinfachungen und keine Auswertungen sind, werden
arithmetische Rechnungen auch dann ausgefuhrt, wenn die Auswertung des
Ausdrucks zum Beispiel mit dem `'` `'` unterdruckt
ist.


Arithmetische Operatoren werden elementweise auf Listen angewendet, wenn die
Optionsvariable `listarith` den Wert `true` hat.  Auf Matrizen werden
die arithmetischen Operatoren immer elementweise angewendet.  Ist einer der
Operanden eine Liste oder Matrix und der andere Operand hat einen anderen
Typ, dann wird dieses Argument mit jedem Element der Liste oder Matrix
kombiniert.


Beispiele:


Addition und Multiplikation sind kommutative N-ary-Operatoren.  Maxima sortiert
die Operanden und konstruiert eine kanonische Darstellung.  Die Namen der 
Operatoren sind `"+"` und `"*"`.



```maxima
(%i1) c + g + d + a + b + e + f;
(%o1)               g + f + e + d + c + b + a
(%i2) [op (%), args (%)];
(%o2)              [+, [g, f, e, d, c, b, a]]
(%i3) c * g * d * a * b * e * f;
(%o3)                     a b c d e f g
(%i4) [op (%), args (%)];
(%o4)              [*, [a, b, c, d, e, f, g]]
(%i5) apply ("+", [a, 8, x, 2, 9, x, x, a]);
(%o5)                    3 x + 2 a + 19
(%i6) apply ("*", [a, 8, x, 2, 9, x, x, a]);
                                 2  3
(%o6)                       144 a  x
```


Division und Exponentiation sind nicht-kommutative binare Operatoren.  Die 
Namen der Operatoren sind `"/"` und `"^"`.



```maxima
(%i1) [a / b, a ^ b];

                              a   b
(%o1)                        [-, a ]
                              b

(%i2) [map (op, %), map (args, %)];
(%o2)              [[/, ^], [[a, b], [a, b]]]
(%i3) [apply ("/", [a, b]), apply ("^", [a, b])];
                              a   b
(%o3)                        [-, a ]
                              b
```


Subtraktion und Division werden intern als Addition und Multiplikation 
dargestellt.



```maxima
(%i1) [inpart (a - b, 0), inpart (a - b, 1), inpart (a - b, 2)];
(%o1)                      [+, a, - b]
(%i2) [inpart (a / b, 0), inpart (a / b, 1), inpart (a / b, 2)];
                                   1
(%o2)                       [*, a, -]
                                   b
```


Sind die Operanden Zahlen, werden die Rechnungen ausgefuhrt.  Ist einer der
Operanden eine Gleitkommazahl, ist das Ergebnis ebenfalls eine Gleitkommazahl.



```maxima
(%i1) 17 + b - (1/2)*29 + 11^(2/4);
                                       5
(%o1)                   b + sqrt(11) + -
                                       2

(%i2) [17 + 29, 17 + 29.0, 17 + 29b0];
(%o2)                   [46, 46.0, 4.6b1]
```


Arithmetische Rechnungen sind Vereinfachungen und keine Auswertung.



```maxima
(%i1) simp : false;
(%o1)                         false
(%i2) '(17 + 29*11/7 - 5^3);
                              29 11    3
(%o2)                    17 + ----- - 5
                                7
(%i3) simp : true;
(%o3)                         true
(%i4) '(17 + 29*11/7 - 5^3);
                                437
(%o4)                         - ---
                                 7
```


Arithmetische Rechnungen werden elementweise fur Listen und Matrizen 
ausgefuhrt.  Bei Listen wird dies mit der Optionsvariablen
`listarith` kontrolliert.



```maxima
(%i1) matrix ([a, x], [h, u]) - matrix ([1, 2], [3, 4]);

                        [ a - 1  x - 2 ]
(%o1)                   [              ]
                        [ h - 3  u - 4 ]

(%i2) 5 * matrix ([a, x], [h, u]);

                          [ 5 a  5 x ]
(%o2)                     [          ]
                          [ 5 h  5 u ]

(%i3) listarith : false;
(%o3)                         false
(%i4) [a, c, m, t] / [1, 7, 2, 9];
                          [a, c, m, t]
(%o4)                     ------------
                          [1, 7, 2, 9]
(%i5) [a, c, m, t] ^ x;
                                      x
(%o5)                     [a, c, m, t]
(%i6) listarith : true;
(%o6)                         true
(%i7) [a, c, m, t] / [1, 7, 2, 9];
                              c  m  t
(%o7)                     [a, -, -, -]
                              7  2  9

(%i8) [a, c, m, t] ^ x;
                          x   x   x   x
(%o8)                   [a , c , m , t ]
```

See also: `orderlessp`, `ordergreatp`, `'`, `listarith`.

<!-- category: Programming -->
<!-- keywords: . -->
<!-- signatures: . -->
### Function: .

Ist der Operator der nicht-kommutativen Multiplikation von Matrizen.  Siehe
fur Erlauterungen `Nicht-kommutative-Multiplikation`.

See also: `Nicht-kommutative-Multiplikation`.

<!-- category: Programming -->
<!-- keywords: : -->
<!-- signatures: : -->
### Function: :

Ist der Operator fur die Zuweisung eines Wertes an eine Variable.


Ist die linke Seite eine Variable (ohne Index), wertet der Operator `:` die
rechte Seite aus und weist den Wert der Variablen auf der linken Seite zu.


Ist die linke Seite ein Element einer Liste, Matrix oder ein deklariertes 
Maxima- oder Lisp-Array, wird die rechte Seite diesem Element zugewiesen.  Der 
Index muss ein existierendes Element bezeichnen.


Ist die linke Seite ein Element eines nicht deklarierten Arrays, dann wird
die rechte Seite diesem Element zugewiesen, falls dieses existiert.  Existiert 
das Element noch nicht, wird ein neues Element erzeugt.


Ist die linke Seite eine Liste mit Variablen (ohne Index), muss die rechte Seite
zu einer Liste auswerten.  Die Elemente der Liste auf der rechten Seite werden 
den Elementen auf der linken Seite parallel zugewiesen.


Siehe auch `kill` und `remvalue` fur die Aufhebung der Zuweisung
eines Wertes an ein Symbol.


Beispiele:


Zuweisung an eine einfache Variable.



```maxima
(%i1) a;
(%o1)                           a
(%i2) a : 123;
(%o2)                          123
(%i3) a;
(%o3)                          123
```


Zuweisung an ein Element einer Liste.



```maxima
(%i1) b : [1, 2, 3];
(%o1)                       [1, 2, 3]
(%i2) b[3] : 456;
(%o2)                          456
(%i3) b;
(%o3)                      [1, 2, 456]
```


Die Zuweisung erzeugt ein nicht deklariertes Array.



```maxima
(%i1) c[99] : 789;
(%o1)                          789
(%i2) c[99];
(%o2)                          789
(%i3) c;
(%o3)                           c
(%i4) arrayinfo (c);
(%o4)                   [hashed, 1, [99]]
(%i5) listarray (c);
(%o5)                         [789]
```


Mehrfache Zuweisung.



```maxima
(%i1) [a, b, c] : [45, 67, 89];
(%o1)                     [45, 67, 89]
(%i2) a;
(%o2)                          45
(%i3) b;
(%o3)                          67
(%i4) c;
(%o4)                          89
```


Die mehrfache Zuweisung wird parallel ausgefuhrt.  Die Werte von `a` und
`b` werden in diesem Beispiel ausgetauscht.



```maxima
(%i1) [a, b] : [33, 55];
(%o1)                       [33, 55]
(%i2) [a, b] : [b, a];
(%o2)                       [55, 33]
(%i3) a;
(%o3)                          55
(%i4) b;
(%o4)                          33
```

See also: `kill`, `remvalue`.

<!-- category: Programming -->
<!-- keywords: :: -->
<!-- signatures: :: -->
### Function: ::

Ist der Operator fur die Zuweisung eines Wertes an eine Variable.


Der Operator `::` ist vergleichbar mit dem Operator `:` mit dem
Unterschied, dass `::` sowohl die rechte als auch die linke Seite
auswertet.


Beispiele:



```maxima
(%i1) x : 'foo;
(%o1)                          foo
(%i2) x :: 123;
(%o2)                          123
(%i3) foo;
(%o3)                          123
(%i4) x : '[a, b, c];
(%o4)                       [a, b, c]
(%i5) x :: [11, 22, 33];
(%o5)                     [11, 22, 33]
(%i6) a;
(%o6)                          11
(%i7) b;
(%o7)                          22
(%i8) c;
(%o8)                          33
```

See also: `:`.

<!-- category: Programming -->
<!-- keywords: ::= -->
<!-- signatures: ::= -->
### Function: ::=

Ist der Operator fur die Definition von Makro-Funktionen.


Der Operator `::=` definiert eine Makro-Funktion, das ist eine Funktion,
die ihre Argumente nicht auswertet.  Der Ausdruck, der die Makro-Funktion
definiert, wird in dem Kontext ausgewertet, in dem das Makro aufgerufen wird.
Ansonsten verhalt sich eine Makro-Funktion wie eine gewohnliche Funktion.


Die Funktion `macroexpand` expandiert eine Makro-Funktion, ohne sie
auszuwerten.  `macroexpand(foo(x))` dem `''%` folgt, ist aquivalent
zu `foo(x)`, wenn `foo` eine Makro-Funktion ist.


Der Operator `::=` fugt den Namen der neuen Makro-Funktion der 
Informationsliste `macros` hinzu.  Die Funktionen `kill`,
`remove` und `remfunction` heben die Zuweisung der Makro-Funktion an
ein Symbol auf und entfernen die Makro-Funktion von der Informationsliste
`macros`.


Die Funktionen `fundef` oder `dispfun` geben die Definition einer
Makro-Funktion zuruck oder weisen die Makro-Funktion einer Marke zu.


Makro-Funktionen enthalten haufig Ausdrucke mit den Funktionen
`buildq` und `splice`.  Mit diesen werden Ausdrucke konstruiert,
die dann ausgewertet werden.



Beispiele:


Eine Makro-Funktion wertet ihre Argumente nicht aus.  Daher zeigt Beispiel (1)
`y - z` und nicht den Wert von `y - z`.  Das Makro wird in 
dem Kontext ausgewertet, in dem das Makro aufgerufen wird.  Dies zeigt (2).



```maxima
(%i1) x: %pi$

(%i2) y: 1234$

(%i3) z: 1729 * w$

(%i4) printq1 (x) ::= block (print ("(1) x is equal to", x),
      '(print ("(2) x is equal to", x)))$

(%i5) printq1 (y - z);
(1) x is equal to y - z
(2) x is equal to %pi
(%o5)                                 %pi
```


Eine gewohnliche Funktion wertet ihre Argumente aus.  Daher zeigt (1) den Wert 
von `y - z`.  Der Ruckgabewert wird nicht ausgewertet und gibt (2).  Mit
`''%` wird die Auswertung erzwungen.



```maxima
(%i1) x: %pi$

(%i2) y: 1234$

(%i3) z: 1729 * w$

(%i4) printe1 (x) := block (print ("(1) x is equal to", x),
      '(print ("(2) x is equal to", x)))$

(%i5) printe1 (y - z);
(1) x is equal to 1234 - 1729 w
(%o5)                     print((2) x is equal to, x)
(%i6) ''%;
(2) x is equal to %pi
(%o6)                                 %pi
```


`macroexpand` gibt die Expansion des Makros zuruck.
`macroexpand(foo(x))` dem `''%` folgt, ist aquivalent zu 
`foo(x)`, wenn `foo` eine Makro-Funktion ist.



```maxima
(%i1) x: %pi$

(%i2) y: 1234$

(%i3) z: 1729 * w$

(%i4) g (x) ::= buildq ([x], print ("x is equal to", x))$

(%i5) macroexpand (g (y - z));
(%o5)                     print(x is equal to, y - z)
(%i6) ''%;
x is equal to 1234 - 1729 w
(%o6)                            1234 - 1729 w
(%i7) g (y - z);
x is equal to 1234 - 1729 w
(%o7)                            1234 - 1729 w
```

See also: `macroexpand`, `macros`, `kill`, `remove`, `remfunction`, `fundef`, `dispfun`, `buildq`, `splice`.

<!-- category: Programming -->
<!-- keywords: := -->
<!-- signatures: := -->
### Function: :=

Ist der Operator fur Funktionsdefinitionen.


`f(x_1, ..., x_n)` := *expr* definiert eine Funktion
mit dem Namen *f*, den Argumenten *x_1*, ..., *x_n* und der
Funktionsdefinition *expr*.  Der Operator `:=` wertet die 
Funktionsdefinition nicht aus.  Die Auswertung kann mit dem
Quote-Quote-Operator `''` erzwungen werden.  Die definierte
Funktion kann eine gewohnliche Maxima-Funktion `f(x)` sein oder eine
Array-Funktion `f[i](x)`.


Ist das letzte oder das einzige Argument der Funktion *x_n* eine Liste mit
einem Element, dann akzeptiert die mit `:=` definierte Funktion eine
variable Anzahl an Argumenten.  Die Argumente werden zunachst nacheinander den
Argumenten *x_1*, ..., *x_(n - 1)* zugewiesen.  Sind weitere
Argumente vorhanden, werden diese *x_n* als Liste zugewiesen.


Funktionsdefinitionen erscheinen im globalen Namensraum.  Wird eine Funktion
`f` innerhalb einer Funktion `g` definiert, wird die Reichweite der
Funktion nicht automatisch auf `g` beschrankt.  Dagegen fuhrt
`local(f)` zu einer Definition, die nur innerhalb eines Blockes oder einem
anderen zusammengesetzten Ausdruck erscheint.  Siehe auch `local`.


Ist eines der Argumente ein Symbol auf das der Quote-Operator
`'` angewendet wurde, wird dieses Argument nicht ausgewertet.  Ansonsten
werden alle Argumente ausgewertet.


Siehe auch `define` und `::=`.


Beispiele:


`:=` wertet die Funktionsdefinition nie aus, außer wenn der
Quote-Quote-Operator angewendet wird.



```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) F1 (x, y) := expr;
(%o2)                   F1(x, y) := expr
(%i3) F1 (a, b);
(%o3)                    cos(y) - sin(x)
(%i4) F2 (x, y) := ''expr;
(%o4)              F2(x, y) := cos(y) - sin(x)
(%i5) F2 (a, b);
(%o5)                    cos(b) - sin(a)
```


Mit dem Operator `:=` definierte Funktionen konnen eine gewohnliche
Maxima-Funktion oder eine Array-Funktion sein.



```maxima
(%i1) G1 (x, y) := x.y - y.x;
(%o1)               G1(x, y) := x . y - y . x
(%i2) G2 [x, y] := x.y - y.x;
(%o2)                G2     := x . y - y . x
                       x, y
```


Ist das letzte oder einzige Argument *x_n* eine Liste mit einem Element,
dann akzeptiert die Funktion eine variable Anzahl an Argumenten.



```maxima
(%i1) H ([L]) := apply ("+", L);
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


`local` erzeugt eine lokale Funktionsdefinition.



```maxima
(%i1) foo (x) := 1 - x;
(%o1)                    foo(x) := 1 - x
(%i2) foo (100);
(%o2)                         - 99
(%i3) block (local (foo), foo (x) := 2 * x, foo (100));
(%o3)                          200
(%i4) foo (100);
(%o4)                         - 99
```

See also: `local`, `define`, `::=`.

<!-- category: Programming -->
<!-- keywords: <, <=, >=, > -->
<!-- signatures: <=, >=, > -->
### Function: < (=)

Die Symbole `<`, `<=`, `>=` und `>` sind die relationalen
Operatoren "kleiner als", "kleiner als oder gleich", "großer als oder 
gleich" und "großer als".  Die Namen dieser Operatoren sind jeweils: 
`"<"`, `"<="`, `">="` und `">"`.  Diese konnen dort 
eingesetzt werden, wo der Name des Operators benotigt wird.


Die relationalen Operatoren sind binare Operatoren.  Ausdrucke wie 
`a < b < c` werden von Maxima nicht erkannt und generieren eine
Fehlermeldung.


Relationale Ausdrucke werden von den Funktionen `is` und
`maybe` sowie den Funktionen `if`, `while` und
`unless` zu booleschen Werten ausgewertet.  Relationale Ausdrucke werden
ansonsten nicht zu booleschen Werten ausgewertet oder vereinfacht.  Jedoch
werden die Operanden eines booleschen Ausdruckes ausgewertet, wenn die
Auswertung nicht mit dem `'` `'` unterdruckt ist.


Wenn ein relationaler Ausdruck mit den Funktionen `is` oder `if` nicht
zu `true` oder `false` ausgewertet werden kann, wird das Verhalten der
Funktionen von der Optionsvariablen `prederror` kontrolliert.  Hat
`prederror` den Wert `true`, wird von `is` und `if` ein
Fehler erzeugt.  Hat `prederror` den Wert `false`, hat `is` den
Ruckgabewert `unknown` und `if` gibt einen konditionalen Ausdruck
zuruck, der teilweise ausgewertet ist.


Die Funktion `maybe` verhalt sich immer so, als ob `prederror` den
Wert `false` hat, und die Schleifenanweisungen `while` sowie
`unless` verhalten sich immer so, als ob `prederror` den Wert
`true` hat.


Relationale Operatoren werden nicht auf die Elemente von Listen oder Matrizen
sowie auf die beiden Seiten einer Gleichung angewendet.


Siehe auch die Operatoren `=` und `#` sowie die Funktionen
`equal` und `notequal`.


Beispiele:


Relationale Ausdrucke werden von einigen Funktionen zu booleschen Werten 
ausgewertet.



```maxima
(%i1) [x, y, z] : [123, 456, 789];
(%o1)                    [123, 456, 789]
(%i2) is (x < y);
(%o2)                         true
(%i3) maybe (y > z);
(%o3)                         false
(%i4) if x >= z then 1 else 0;
(%o4)                           0
(%i5) block ([S], S : 0, for i:1 while i <= 100 do S : S + i, 
             return (S));
(%o5)                         5050
```


Relationale Ausdrucke werden ansonsten nicht zu booleschen Werten ausgewertet 
oder vereinfacht, jedoch werden die Operanden eines relationalen Ausdruckes
ausgewertet.



```maxima
(%i1) [x, y, z] : [123, 456, 789];
(%o1)                    [123, 456, 789]
(%i2) [x < y, y <= z, z >= y, y > z];
(%o2)    [123 < 456, 456 <= 789, 789 >= 456, 456 > 789]
(%i3) map (is, %);
(%o3)               [true, true, true, false]
```

See also: `is`, `maybe`, `if`, `while`, `unless`, `'`, `prederror`, `=`, `#`, `equal`, `notequal`.

<!-- category: Programming -->
<!-- keywords: = -->
<!-- signatures: = -->
### Function: =

Ist der Operator fur eine Gleichung.  `=` ist ein Infix-Operator mit
zwei Operanden.


Mit dem Operator `=` wird eine Gleichung `a = b` formuliert, wobei die
Operanden `a` und `b` jeweils die linke und die rechte Seite der
Gleichung sind und beliebige Ausdrucke sein konnen.  Die Operanden werden
ausgewertet, nicht jedoch die Gleichung selbst.  Nicht ausgewertete Gleichungen
konnen als Argument von Funktionen wie zum Beispiel den Funktionen
`solve`, `algsys` oder `ev` auftreten.


Die Funktion `is` wertet eine Gleichung `=` zu einem booleschen Wert
aus.  `is(a = b)` wertet die Gleichung `a = b` zum Wert `true`
aus, wenn `a` und `b` identische Ausdrucke sind.  Das trifft zu,
wenn `a` und `b` identische Atome sind oder wenn ihre Operatoren sowie
die Operanden identisch sind.  In jedem anderen Fall ist das Ergebnis
`false`.  Das Ergebnis der Auswertung ist nie `unkown`.  Hat
`is(a = b)` das Ergebnis `true`, werden `a` und `b` als
syntaktisch gleich bezeichnet.  Im Unterschied dazu gilt fur aquivalente
Ausdrucke, dass `is(equal(a, b))` den Wert `true` hat.  Ausdrucke
konnen aquivalent aber syntaktisch verschieden sein.


Eine Ungleichung wird mit dem Operator `#` formuliert.  Wie fur den
Operator `=` fur eine Gleichung wird eine Ungleichung `a # b` nicht
ausgewertet.  Eine Auswertung erfolgt mit `is(a # b)`, welche die Werte
`true` oder `false` als Ergebnis hat.


Neben `is` werten auch die Operatoren `if`, `and`,
`or` und `not` Gleichungen mit dem Operator `=` oder
Ungleichungen mit dem Operator `#` zu den Werten `true` oder
`false` aus.


Wegen der Regeln fur die Auswertung von Aussagen und weil im Ausdruck
`not expr` der Operand `expr` ausgewertet wird, ist
`not a = b` aquivalent zu `is(a # b)` und nicht zu `a # b`.


Die Funktionen `rhs` und `lhs` geben die rechte und die linke Seite
einer Gleichung oder Ungleichung zuruck.


Siehe auch den Operator `#` fur Ungleichungen sowie die Funktionen
`equal` und `notequal`.


Beispiele:


Ein Ausdruck `a = b` reprasentiert eine nicht ausgewertete Gleichung.



```maxima
(%i1) eq_1 : a * x - 5 * y = 17;
(%o1)                    a x - 5 y = 17
(%i2) eq_2 : b * x + 3 * y = 29;
(%o2)                    3 y + b x = 29
(%i3) solve ([eq_1, eq_2], [x, y]);
                        196         29 a - 17 b
(%o3)          [[x = ---------, y = -----------]]
                     5 b + 3 a       5 b + 3 a
(%i4) subst (%, [eq_1, eq_2]);
         196 a     5 (29 a - 17 b)
(%o4) [--------- - --------------- = 17, 
       5 b + 3 a      5 b + 3 a
                                  196 b     3 (29 a - 17 b)
                                --------- + --------------- = 29]
                                5 b + 3 a      5 b + 3 a
(%i5) ratsimp (%);
(%o5)                  [17 = 17, 29 = 29]
```


`is(a = b)` wertet die Gleichung `a = b` zu `true` aus, wenn
`a` und `b` syntaktisch gleich sind.  Ausdrucke konnen
aquivalent sein, ohne syntaktisch gleich zu sein.



```maxima
(%i1) a : (x + 1) * (x - 1);
(%o1)                    (x - 1) (x + 1)
(%i2) b : x^2 - 1;
                              2
(%o2)                        x  - 1
(%i3) [is (a = b), is (a # b)];
(%o3)                     [false, true]
(%i4) [is (equal (a, b)), is (notequal (a, b))];
(%o4)                     [true, false]
```


Einige Operatoren werten `=` und `#` zu `true` oder `false`
aus.



```maxima
(%i1) if expand ((x + y)^2) = x^2 + 2 * x * y + y^2 then FOO else
      BAR;
(%o1)                          FOO
(%i2) eq_3 : 2 * x = 3 * x;
(%o2)                       2 x = 3 x
(%i3) eq_4 : exp (2) = %e^2;
                              2     2
(%o3)                       %e  = %e
(%i4) [eq_3 and eq_4, eq_3 or eq_4, not eq_3];
(%o4)                  [false, true, true]
```


Da `not expr` die Auswertung des Ausdrucks `expr` bewirkt, ist
`not (a = b)` aquivalent zu `is(a # b)`.



```maxima
(%i1) [2 * x # 3 * x, not (2 * x = 3 * x)];
(%o1)                   [2 x # 3 x, true]
(%i2) is (2 * x # 3 * x);
(%o2)                         true
```

See also: `solve`, `algsys`, `ev`, `is`, `#`, `if`, `and`, `or`, `not`, `rhs`, `lhs`, `equal`, `notequal`.

<!-- category: Programming -->
<!-- keywords: ^^ -->
<!-- signatures: ^^ -->
### Function: ^^

Ist der Operator der nicht-kommutativen Exponentiation von Matrizen.  In der 
linearen Ausgabe wird der nicht-kommutative Operator als `^^` angezeigt.
In der zweidimensionalen Ausgabe wird der hochgestellte Exponent von spitzen 
Klammern `< >` eingeschlossen.


Beispiele:



```maxima
(%i1) a . a . b . b . b + a * a * a * b * b;
                        3  2    <2>    <3>
(%o1)                  a  b  + a    . b
(%i2) string (a . a . b . b . b + a * a * a * b * b);
(%o2)                  a^3*b^2+a^^2 . b^^3
```

<!-- category: Programming -->
<!-- keywords: and -->
<!-- signatures: and -->
### Function: and

Ist der logische Operator der Konjunktion.  `and` ist ein 
N-ary-Operator.  Die Operanden sind boolesche Ausdrucke und das Ergebnis ist
ein boolescher Wert.


Der Operator `and` erzwingt die Auswertung aller oder einen Teil der
Operanden.  Die Operanden werden in der Reihenfolge ausgewertet, in der sie
auftreten.  `and` wertet nur so viele Operanden aus, wie notig sind, um
das Ergebnis des Ausdrucks zu bestimmen.  Hat irgendein Argument den Wert
`false`, ist das Ergebnis `false` und die weiteren Argumente werden
nicht ausgewertet.


Die Optionsvariable `prederror` kontrolliert das Verhalten von `and`
fur den Fall, dass ein Operand nicht zu `true` oder `false`
ausgewertet werden kann.  `and` gibt eine Fehlermeldung aus, wenn 
`prederror` den Wert `true` hat.  Andernfalls werden Operanden
akzeptiert, die nicht zu `true` oder `false` ausgewertet werden
konnen und das Ergebnis ist ein boolescher Ausdruck.


`and` ist nicht kommutativ, da aufgrund von nicht ausgewerteten Operanden
die Ausdrucke `a and b` und `b and a` ein unterschiedliches Ergebnis
haben konnen.


Beispiele:



```maxima
(%i1) n:2;
(%o1)                           2
(%i2) integerp(n) and evenp(n);
(%o2)                         true
(%i3) not(a=b) and 1=1 and integerp(2);
(%o3)                         true
(%i4) not(a=b) and 1=1 and oddp(2);
(%o4)                         false
(%i5) a and b;
(%o5)                        a and b
(%i6) prederror:true$
(%i7) a and b;

Unable to evaluate predicate a
 -- an error. To debug this try: debugmode(true);
```


Da `and` nur so viele Operanden auswertet wie notwendig sind, um das
Ergebnis festzustellen, fuhrt der syntaktische Fehler im zweiten Operanden
nicht zu einer Fehlermeldung, das das Ergebnis bereits mit dem ersten
Operanden feststeht.



```maxima
(%i8) a=b and sin(2,2);
(%o8)                         false
```

See also: `prederror`.

<!-- category: Programming -->
<!-- keywords: infix -->
<!-- signatures: infix(op), infix(op, lbp, rbp), infix(op, lbp, rbp, lpos, rpos, pos) -->
### Function: infix (op)

Deklariert *op* als einen Infix-Operator.  Ein Infix-Operator hat eine 
Funktionsdefinition mit zwei Argumenten.  Der Infix-Operator steht zwischen den
Operanden.  Zum Beispiel ist die Subtraktion `-` ein Infix-Operator.


`infix(op)` deklariert *op* als einen Infix-Operator mit einem
links- und rechtsseitigen Vorrang von jeweils 180.


`infix(op, lbp, rbp)` deklariert *op* als einen
Infix-Operator mit den angegebenen Werten fur den links- und rechtsseitigen
Vorrang.


`infix(op, lbp, rbp, lpos, rpos, pos)`
deklariert *op* als einen Infix-Operator mit den angegebenen
Vorrangen sowie den Wortarten *lpos*, *rpos* und *pos* fur
den linken und den rechten Operanden sowie das Ergebnis des Operators.


Beispiele:


Sind die rechtsseitigen und linksseitigen Vorrange eines Operators
*op* großer als die entsprechenden Vorrange eines anderen
Operators, dann hat der Operator *op* Vorrang.



```maxima
(%i1) :lisp (get '$+ 'lbp)
100
(%i1) :lisp (get '$+ 'rbp)
100
(%i1) infix ("##", 101, 101);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")");
(%o2)       (a ## b) := sconcat("(", a, ",", b, ")")
(%i3) 1 + a ## b + 2;
(%o3)                       (a,b) + 3
(%i4) infix ("##", 99, 99);
(%o4)                          ##
(%i5) 1 + a ## b + 2;
(%o5)                       (a+1,b+2)
```


Ein großerer linksseitige Vorrang *lbp* bewirkt, dass der
Operator *op* rechts-assoziativ ist.  Ein großerer rechtsseitiger
Vorrang macht dagegen den Operator *op* links-as­so­zia­tiv.



```maxima
(%i1) infix ("##", 100, 99);
(%o1)                          ##
(%i2) "##"(a, b) := sconcat("(", a, ",", b, ")")$
(%i3) foo ## bar ## baz;
(%o3)                    (foo,(bar,baz))
(%i4) infix ("##", 100, 101);
(%o4)                          ##
(%i5) foo ## bar ## baz;
(%o5)                    ((foo,bar),baz)
```


Maxima kann Syntaxfehler beim Einlesen eines Ausdrucks feststellen, wenn der
eingelesene Operand nicht die fur den Operator definierte Wortart hat.



```maxima
(%i1) infix ("##", 100, 99, expr, expr, expr);
(%o1)                          ##
(%i2) if x ## y then 1 else 0;
Incorrect syntax: Found algebraic expression where 
logical expression expected
if x ## y then 
             ^
(%i2) infix ("##", 100, 99, expr, expr, clause);
(%o2)                          ##
(%i3) if x ## y then 1 else 0;
(%o3)                if x ## y then 1 else 0
```

See also: `-`.

<!-- category: Programming -->
<!-- keywords: matchfix -->
<!-- signatures: matchfix(ldelimiter, rdelimiter), matchfix(ldelimiter, rdelimiter, arg_pos, pos) -->
### Function: matchfix (ldelimiter, rdelimiter)

Deklariert einen Matchfix-Operator mit dem linksseitigen Begrenzungszeichen 
*ldelimiter* und dem rechtsseitigen Begrenzungszeichen *rdelimiter*.


Ein Matchfix-Operator hat eine beliebige Anzahl an Argumenten, die zwischen
dem linksseitigen und dem rechtsseitigen Begrenzungszeichen stehen.  Das
Begrenzungszeichen kann eine beliebige Zeichenkette sein.  Einige Zeichen wie
`%`, `,`, `$` und `;` konnen nicht als Begrenzungszeichen
definiert werden.


Ein linksseitiges Begrenzungszeichen kann nicht verschiedene rechtsseitige
Begrenzungszeichen haben.


Maxima-Operatoren konnen als Matchfix-Operatoren definiert werden, ohne 
dass sich die sonstigen Operatoreigenschaften andern.  So kann zum Beispiel
der Operator `+` als Matchfix-Operator definiert werden.


`matchfix(ldelimiter, rdelimiter, arg_pos, pos)`
definiert die Wortarten fur die Argumente *arg_pos* und das Ergebnis
*pos* sowie das linksseitige *ldelimiter* und rechtsseitige
*rdelimiter* Begrenzungszeichen.


Die zu einem Matchfix-Operator zugehorige Funktion kann jede 
nutzerdefinierte Funktion sein, die mit `:=` oder `define` definiert
wird.  Die Definition der Funktion kann mit `dispfun(ldelimiter)` 
ausgegeben werden.


Maxima kennt nur den Operator fur Listen `[ ]` als Matchfix-Operator.
Klammern `( )` und Anfuhrungszeichen `" "` arbeiten wie 
Matchfix-Operatoren, werden aber vom Parser nicht als Matchfix-Operatoren 
behandelt.


`matchfix` wertet die Argumente aus.  `matchfix` gibt das erste
Argument *ldelimiter* als Ergebnis zuruck.


Beispiele:


Begrenzungszeichen konnen eine beliebige Zeichenkette sein.



```maxima
(%i1) matchfix ("@@", "~");
(%o1)                          @@
(%i2) @@ a, b, c ~;
(%o2)                      @@a, b, c~
(%i3) matchfix (">>", "<<");
(%o3)                          >>
(%i4) >> a, b, c <<;
(%o4)                      >>a, b, c<<
(%i5) matchfix ("foo", "oof");
(%o5)                          foo
(%i6) foo a, b, c oof;
(%o6)                     fooa, b, coof
(%i7) >> w + foo x, y oof + z << / @@ p, q ~;
                     >>z + foox, yoof + w<<
(%o7)                ----------------------
                            @@p, q~
```


Matchfix-Operatoren konnen fur nutzerdefinierte Funktionen definiert 
werden.



```maxima
(%i1) matchfix ("!-", "-!");
(%o1)                         "!-"
(%i2) !- x, y -! := x/y - y/x;
                                    x   y
(%o2)                   !-x, y-! := - - -
                                    y   x
(%i3) define (!-x, y-!, x/y - y/x);
                                    x   y
(%o3)                   !-x, y-! := - - -
                                    y   x
(%i4) define ("!-" (x, y), x/y - y/x);
                                    x   y
(%o4)                   !-x, y-! := - - -
                                    y   x
(%i5) dispfun ("!-");
                                    x   y
(%t5)                   !-x, y-! := - - -
                                    y   x

(%o5)                         done
(%i6) !-3, 5-!;
                                16
(%o6)                         - --
                                15
(%i7) "!-" (3, 5);
                                16
(%o7)                         - --
                                15
```

See also: `:=`, `define`, `matchfix`.

<!-- category: Programming -->
<!-- keywords: nary -->
<!-- signatures: nary(op), nary(op, bp, arg_pos, pos) -->
### Function: nary (op)

`nary(op)` definiert einen `N-ary`-Operator *op* mit einem
linksseitigen Vorrang von 180.  Der rechtsseitige Vorrang wird nicht benotigt.


`nary(op, bp, arg_pos, pos)` definiert einen
`N-ary`-Operator *op* mit einem rechtsseitigen Vorrang von *bp* und
der Wortart *arg_pos* fur den Operanden und der Wortart *pos* für das
Ergebnis.


Ein `N-ary`-Operator ist ein Operator, der eine beliebige Anzahl an 
Argumenten haben kann.  Die Argumente werden durch den Operator voneinander 
getrennt, so ist zum Beispiel `+` ein `N-ary`-Operator und 
`A+B+C`.


Im Unterschied zur Definition eines Operators kann eine Funktion `f` auch
als `nary` mit der Funktion `declare` deklariert werden.  Die
Deklaration hat Auswirkung auf die Vereinfachung der Funktion.  Zum Beispiel
wird ein Ausdruck `j(j(a,b),j(c,d)` zu `j(a,b,c,d)` vereinfacht.

See also: `nary`, `declare`.

<!-- category: Programming -->
<!-- keywords: nofix -->
<!-- signatures: nofix(op), nofix(op, pos) -->
### Function: nofix (op)

`nofix(op)` definiert den Operator *op* als einen Nofix-Operator.


`nofix(op, pos)` definiert einen Nofix-Operator mit der
Wortart *pos* fur das Ergebnis.


Nofix-Operatoren sind Operatoren, die kein Argument haben.  Tritt ein solcher 
Operator allein auf, wird die dazugehorige Funktion ausgewertet.  Zum Beispiel
beendet die Funktion `quit()` eine Maxima-Sitzung.  Wird diese Funktion 
mit `nofix("quit")` als ein Nofix-Operator definiert, genugt die
Eingabe von `quit`, um eine Maxima-Sitzung zu beenden.

<!-- category: Programming -->
<!-- keywords: not -->
<!-- signatures: not -->
### Function: not

Ist die logische Negation.  `not` ist ein Prefix-Operator.  Der Operand
ist ein boolescher Ausdruck und das Ergebnis ein boolescher Wert.


Der Operator `not` erzwingt die Auswertung des Operanden.  Die
Optionsvariable `prederror` kontrolliert das Verhalten von `not` fur
den Fall, dass der Operand nicht zu `true` oder `false` ausgewertet
werden kann.  `not` gibt eine Fehlermeldung, wenn `prederror` den Wert
`true` hat.  Andernfalls wird ein Operand akzeptiert, der nicht zu
`true` oder `false` ausgewertet werden kann, und das Ergebnis ist ein
boolescher Ausdruck.


Beispiele:



```maxima
(%i1) not integerp(2);
(%o1)                         false
(%i2) not (a=b);
(%o2)                         true
(%i3) not a;
(%o3)                         not a
(%i4) prederror:true$
(%i5) not a;

Unable to evaluate predicate a
 -- an error. To debug this try: debugmode(true);
```

See also: `prederror`.

<!-- category: Programming -->
<!-- keywords: or -->
<!-- signatures: or -->
### Function: or

Ist der logische Operator der Disjunktion.  `or` ist ein N-ary-Operator.
Die Operanden sind boolesche Ausdrucke und das Ergebnis ist ein boolescher
Wert.


Der Operator `or` erzwingt die Auswertung aller oder einen Teil der
Operanden.  Die Operanden werden in der Reihenfolge ausgewertet, in der sie
auftreten.  `or` wertet nur so viele Operanden aus wie notig sind, um
das Ergebnis des Ausdrucks zu bestimmen.  Hat irgendein Operand den Wert
`true`, ist das Ergebnis `true` und die weiteren Operanden werden
nicht ausgewertet.


Die Optionsvariable `prederror` kontrolliert das Verhalten von `or`
fur den Fall, dass ein Operand nicht zu `true` oder `false`
ausgewertet werden kann.  `or` gibt eine Fehlermeldung, wenn
`prederror` den Wert `true` hat.  Andernfalls werden Operanden
akzeptiert, die nicht zu `true` oder `false` ausgewertet werden
konnen und das Ergebnis ist ein boolescher Ausdruck.


`or` ist nicht kommutativ, da aufgrund von nicht ausgewerteten Operanden
die Ausdrucke `a or b` und `b or a` ein unterschiedliches Ergebnis
haben konnen.


Beispiele:



```maxima
(%i1) n:2;
(%o1)                           2
(%i2) oddp(n) or evenp(n);
(%o2)                         true
(%i3) a=b or not(1=1) or integerp(2);
(%o3)                         true
(%i4) a or b;
(%o4)                        a or b
(%i5) prederror:true$
(%i6) a or b;

Unable to evaluate predicate a
 -- an error. To debug this try: debugmode(true);
```


Da `or` nur so viele Operanden auswertet wie notwendig sind, um das
Ergebnis festzustellen, fuhrt der syntaktische Fehler im zweiten Operanden
nicht zu einer Fehlermeldung, da das Ergebnis bereits mit dem ersten
Operanden feststeht.



```maxima
(%i7) integerp(2) or sin(2,2);
(%o7)                         true
```

See also: `prederror`.

<!-- category: Programming -->
<!-- keywords: postfix -->
<!-- signatures: postfix(op), postfix(op, lbp, lpos, pos) -->
### Function: postfix (op)

`postfix (op)` definiert einen Postfix-Operator *op*.


`postfix (op, lbp, lpos, pos)` definiert einen
Postfix-Operator *op* mit einem linksseitigem Vorrang von *lbp* sowie
den Wortarten *lpos* fur den Operanden und *pos* fur das Ergebnis.


Ein Postfix-Operator hat einen Operanden, der dem Operator vorangestellt ist.
Ein Beispiel ist der `!`-Operator mit `3!`.  Die Funktion
`postfix("x")` erweitert die Maxima-Syntax um den Postfix-Operator 
`x`.

<!-- category: Programming -->
<!-- keywords: prefix -->
<!-- signatures: prefix(op), prefix(op, rbp, rpos, pos) -->
### Function: prefix (op)

`prefix (op)` definiert einen Prefix-Operator *op*.


`prefix (op, lbp, lpos, pos)` definiert einen
Prefix-Operator *op* mit einem rechtsseitigem Vorrang von *rbp* sowie
den Wortarten *rpos* fur den Operanden und *pos* fur das Ergebnis.


Ein Prefix-Operator hat einen Operanden, der dem Operator nachfolgt.  Mit
`prefix("x")` wird die Maxima-Syntax um einen Prefix-Operator `x`
erweitert.

