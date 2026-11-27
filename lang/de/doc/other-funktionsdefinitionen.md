## Funktionsdefinitionen

<!-- category: Other -->
<!-- keywords: apply -->
<!-- signatures: apply(F, [x_1, ..., x_n]) -->
### Function: apply (F, [x_1, ..., x_n])

Konstruiert den Ausdruck `F(arg_1, ..., arg_n)` und 
wertet diesen aus.


`apply` versucht nicht Array-Funktionen von gewohnlichen Funktionen zu
unterscheiden.  Ist *F* der Name eine Array-Funktion, wertet `apply`
den Ausdruck `F(...)` aus.  `arrayapply` entspricht der 
Funktion `apply`, wenn *F* eine Array-Funktion ist.


Beispiele:


`apply` wertet die Argumente aus.  In diesem Beispiel wird die Funktion
`min` auf die Liste `L` angewendet.



```maxima
(%i1) L : [1, 5, -10.2, 4, 3];
(%o1)                 [1, 5, - 10.2, 4, 3]
(%i2) apply (min, L);
(%o2)                        - 10.2
```


`apply` wertet die Argumente auch dann aus, wenn die Funktion `F`
die Auswertung ihrer Argumente unterdruckt.



```maxima
(%i1) F (x) := x / 1729;

                                   x
(%o1)                     F(x) := ----
                                  1729

(%i2) fname : F;
(%o2)                           F
(%i3) dispfun (F);
                                   x
(%t3)                     F(x) := ----
                                  1729

(%o3)                         [%t3]
(%i4) dispfun (fname);
fname is not the name of a user function.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) apply (dispfun, [fname]);
                                   x
(%t5)                     F(x) := ----
                                  1729

(%o5)                         [%t5]
```


`apply` wertet den Namen der Funktion *F* aus.  Mit dem
Quote-Operator `'` wird die Auswertung unterdruckt.
`demoivre` ist der Name einer globalen Optionsvariable und einer Funktion.



```maxima
(%i1) demoivre;
(%o1)                         false
(%i2) demoivre (exp (%i * x));
(%o2)                  %i sin(x) + cos(x)
(%i3) apply (demoivre, [exp (%i * x)]);
demoivre evaluates to false
Improper name or value in functional position.
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i4) apply ('demoivre, [exp (%i * x)]);
(%o4)                  %i sin(x) + cos(x)
```

See also: `arrayapply`, `min`, `demoivre`.

<!-- category: Other -->
<!-- keywords: buildq -->
<!-- signatures: buildq(L, expr) -->
### Function: buildq (L, expr)

Die Variablen der Liste *L* werden in den Ausdruck *expr* substituiert.
Die Substitution wird parallel ausgefuhrt.  Das Ergebnis der Substitution wird
vereinfacht, aber nicht ausgewertet.


Die Elemente der Liste *L* sind Symbole oder Zuweisungen der Form
`symbol: value`.  Die Zuweisungen werden parallel ausgewertet.
Der Wert einer Variablen auf der rechten Seite einer Zuweisung ist der globale
Wert in dem Kontext in dem `buildq` aufgerufen wird und nicht der lokale
Wert einer vorhergehenden Zuweisung.  Erhalt eine Variable keinen Wert, dann 
behalt die Variable den globalen Wert.


Dann werden die in der Liste *L* enthaltenen Variablen parallel in den 
Ausdruck *expr* substituiert.


Enthalt *expr* Ausdrucke der Form `splice(x)`, muss die 
Variable *x* eine Liste sein.  Die Liste wird in den Ausdruck eingefugt.
Siehe auch `splice`.


Variablen in in dem Ausdruck *expr*, die nicht in *L* enthalten sind,
werden nicht durch einen Wert ersetzt, auch wenn es eine globale Variable mit
demselben Namen gibt, da der Ausdruck nicht ausgewertet wird.


Beispiele:


Der Variablen `a` wird der Wert zugewiesen.  Die Variable `b` erhalt
den globalen Wert.  Die Variable `c` hat keinen Wert.  Das Ergebnis ist
ein nicht ausgewerteter Ausdruck.  Die Auswertung wird mit dem 
Quote-Quote-Operator `''` erzwungen.



```maxima
(%i1) (a: 17, b: 29, c: 1729)$
(%i2) buildq ([a: x, b], a + b + c);
(%o2)                      x + c + 29
(%i3) ''%;
(%o3)                       x + 1758
```


`e` ist eine Liste, die einmal als Argument der Funktion `foo`
vorliegt und zum anderen in die Argumentliste der Funktion `bar` 
eingefugt wird.



```maxima
(%i1) buildq ([e: [a, b, c]], foo (x, e, y));
(%o1)                 foo(x, [a, b, c], y)
(%i2) buildq ([e: [a, b, c]], bar (x, splice (e), y));
(%o2)                  bar(x, a, b, c, y)
```


Das Ergebnis wird nach der Substitution vereinfacht, ansonsten hatten die
beiden folgenden Beispiele dasselbe Ergebnis.



```maxima
(%i1) buildq ([e: [a, b, c]], splice (e) + splice (e));
(%o1)                    2 c + 2 b + 2 a
(%i2) buildq ([e: [a, b, c]], 2 * splice (e));
(%o2)                        2 a b c
```


Die Variablen der Liste *L* erhalten ihren Wert parallel, ansonsten ware
das erste Ergebnis `foo(b,b)`.  Substitutionen werden parallel 
ausgefuhrt.  Im Gegensatz dazu werden die Substitutionen mit der Funktion 
`subst` nacheinander ausgefuhrt.



```maxima
(%i1) buildq ([a: b, b: a], foo (a, b));
(%o1)                       foo(b, a)
(%i2) buildq ([u: v, v: w, w: x, x: y, y: z, z: u],
              bar (u, v, w, x, y, z));
(%o2)                 bar(v, w, x, y, z, u)
(%i3) subst ([u=v, v=w, w=x, x=y, y=z, z=u],
             bar (u, v, w, x, y, z));
(%o3)                 bar(u, u, u, u, u, u)
```


Konstruktion einer Liste mit Gleichungen mit Variablen oder Ausdrucken auf 
der linken Seite und deren Werten auf der rechten Seite.  Die Funktion
`macroexpand` expandiert das Makro `show_values`.



```maxima
(%i1) show_values ([L]) ::= buildq ([L], map ("=", 'L, L))$
(%i2) (a: 17, b: 29, c: 1729)$
(%i3) show_values (a, b, c - a - b);
(%o3)          [a = 17, b = 29, c - b - a = 1683]
(%i4) macroexpand (show_values (a, b, c - a - b));
(%o4)    map(=, '([a, b, c - b - a]), [a, b, c - b - a])
```


Konstruktion einer Funktion.



```maxima
(%i1) curry (f, [a]) :=
        buildq ([f, a], lambda ([[x]], apply (f, append (a, x))))$
(%i2) by3 : curry ("*", 3);
(%o2)        lambda([[x]], apply(*, append([3], x)))
(%i3) by3 (a + b);
(%o3)                       3 (b + a)
```

See also: `splice`, `subst`, `macroexpand`.

<!-- category: Other -->
<!-- keywords: define -->
<!-- signatures: define(f(x_1, ..., x_n), expr), define(f[x_1, ..., x_n], expr), define(funmake(f, [x_1, ..., x_n]), expr), define(arraymake(f, [x_1, ..., x_n]), expr), define(ev(expr_1), expr_2) -->
### Function: define (f(x_1, ..., x_n), expr)

Definiert eine Funktion mit dem Namen *f* und den Argumenten *x1*, 
..., *x_n* und der Funktionsdefinition *expr*.  `define`
wertet das zweite Argument immer aus.


Ist das letzte oder einzige Argument *x_n* eine Liste mit einem Element, 
dann akzeptiert die Funktion eine variable Anzahl an Argumenten.  Die Argumente
der Funktion werden nacheinander den Variablen *x_1*, ..., *x_(n-1)*
zugewiesen.  Sind weitere Argumente vorhanden, werden diese als Liste der
Variablen *x_n* zugewiesen.


Ist das erste Argument der Funktion `define` ein Ausdruck der Form
`f(x_1, ..., x_n)` oder `f[x_1, ..., x_n]` werden die Argumente der Funktion ausgewertet, aber nicht die
Funktion *f* selbst.  *f* wird auch dann nicht ausgewertet, wenn es
bereits eine Funktion mit dem Namen *f* gibt.


Das erste Argument wird dann ausgewertet, wenn es ein Ausdruck mit den 
Funktionen `funmake`, `arraymake` oder `ev` ist.


Alle Funktionsdefinitionen treten in demselben Namensraum auf.  Die Definition
einer Funktion `g` innerhalb einer Funktion `f` fuhrt nicht 
automatisch zu einer lokalen Definition.  Um eine lokale Funktion zu erhalten,
kann `lokal(g)` innerhalb der Funktion `f` ausgefuhrt werden.
Siehe auch `local`.


Ist eines der Argumente *x_k* nach der Auswertung ein quotiertes Symbol,
wertet die mit `define` definierte Funktion das Argument nicht aus.
Alle weiteren Argumente der Funktion werden ausgewertet.


Siehe auch `:=` und `::=`.


Beispiele:


`define` wertet das zweite Argument aus.



```maxima
(%i1) expr : cos(y) - sin(x);
(%o1)                    cos(y) - sin(x)
(%i2) define (F1 (x, y), expr);
(%o2)              F1(x, y) := cos(y) - sin(x)
(%i3) F1 (a, b);
(%o3)                    cos(b) - sin(a)
(%i4) F2 (x, y) := expr;
(%o4)                   F2(x, y) := expr
(%i5) F2 (a, b);
(%o5)                    cos(y) - sin(x)
```



Mit `define` konnen gewohnliche Maxima-Funktionen und Array-Funktionen 
definiert werden.



```maxima
(%i1) define (G1 (x, y), x.y - y.x);
(%o1)               G1(x, y) := x . y - y . x
(%i2) define (G2 [x, y], x.y - y.x);
(%o2)                G2     := x . y - y . x
                       x, y
```


Ist das letzte oder einzige Argument *x_n* eine Liste mit einem Element,
akzeptiert die mit `define` definierte Funktion eine variable Anzahl an
Argumenten.



```maxima
(%i1) define (H ([L]), '(apply ("+", L)));
(%o1)                H([L]) := apply("+", L)
(%i2) H (a, b, c);
(%o2)                       c + b + a
```


Ist das erste Argument ein Ausdruck mit den Funktionen `funmake`,
`arraymake` oder `ev` wird das Argument ausgewertet.



```maxima
(%i1) [F : I, u : x];
(%o1)                        [I, x]
(%i2) funmake (F, [u]);
(%o2)                         I(x)
(%i3) define (funmake (F, [u]), cos(u) + 1);
(%o3)                  I(x) := cos(x) + 1
(%i4) define (arraymake (F, [u]), cos(u) + 1);
(%o4)                   I  := cos(x) + 1
                         x
(%i5) define (foo (x, y), bar (y, x));
(%o5)                foo(x, y) := bar(y, x)
(%i6) define (ev (foo (x, y)), sin(x) - cos(y));
(%o6)             bar(y, x) := sin(x) - cos(y)
```

See also: `funmake`, `arraymake`, `ev`, `local`, `:=`, `::=`.

<!-- category: Other -->
<!-- keywords: define_variable -->
<!-- signatures: define_variable(name, default_value, mode) -->
### Function: define_variable (name, default_value, mode)

Definiert eine globale Variable in der Maxima-Umgebung.  `define_variable`
ist nutzlich fur das Schreiben von Paketen, die haufig ubersetzt oder 
kompiliert werden.  `define_variable` fuhrt die folgenden Schritte aus:



1. `mode_declare(name, mode)` deklariert den Typ der Variablen
*name* fur den Ubersetzer.  Siehe `mode_declare` fur eine Liste 
der moglichen Typen.
2. Hat die Variable keinen Wert, wird der Variablen der Wert *default_value*
zugewiesen.
3. `declare(name, special)` deklariert die Variable als Special.
4. Ordnet der Variablen *name* eine Testfunktion zu, um sicherzustellen, dass 
der Variablen nur Werte zugewiesen werden konnen.


Einer mit `define_variable` definierten Variablen, die einen anderen Typ 
als `any` erhalten hat, kann die Eigenschaft `value_check` zugewiesen
werden.  Die `value_check`-Eigenschaft ist eine Aussagefunktion mit einer
Variablen oder ein Lambda-Ausdruck, die aufgerufen werden, wenn der Variablen
ein Wert zugewiesen werden soll.  Das Argument der `value_check`-Funktion
ist der Wert, den die Variable erhalten soll.


`define_variable` wertet `default_value` aus.  Die Argumente 
`name` und `mode` werden nicht ausgewertet.  `define_variable`
gibt den aktuellen Wert der Variable `name` zuruck.  Dieser ist
`default_value`, wenn der Variablen bisher kein Wert zugewiesen wurde.


Beispiele:


`foo` ist eine boolesche Variable mit dem Wert `true`.



```maxima
(%i1) define_variable (foo, true, boolean);
(%o1)                         true
(%i2) foo;
(%o2)                         true
(%i3) foo: false;
(%o3)                         false
(%i4) foo: %pi;
Error: foo was declared mode boolean, has value: %pi
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i5) foo;
(%o5)                         false
```


`bar` ist eine Variable mit dem Typ einer ganzen Zahl, die eine Primzahl
sein muss.



```maxima
(%i1) define_variable (bar, 2, integer);
(%o1)                           2
(%i2) qput (bar, prime_test, value_check);
(%o2)                      prime_test
(%i3) prime_test (y) := if not primep(y) then
                           error (y, "is not prime.");
(%o3) prime_test(y) := if not primep(y)

                                   then error(y, "is not prime.")
(%i4) bar: 1439;
(%o4)                         1439
(%i5) bar: 1440;
1440 is not prime.
#0: prime_test(y=1440)
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) bar;
(%o6)                         1439
```


`baz_quux` ist eine Variable, der kein Wert zugewiesen werden kann.  Der
Typ `any_check` ist vergleichbar mit `any`.  Aber `any_check` 
ruft im Gegensatz zu `any` den `value_check`-Mechanismus auf.



```maxima
(%i1) define_variable (baz_quux, 'baz_quux, any_check);
(%o1)                       baz_quux
(%i2) F: lambda ([y], if y # 'baz_quux then
                 error ("Cannot assign to `baz_quux'."));
(%o2) lambda([y], if y # 'baz_quux

                        then error(Cannot assign to `baz_quux'.))
(%i3) qput (baz_quux, ''F, value_check);
(%o3) lambda([y], if y # 'baz_quux

                        then error(Cannot assign to `baz_quux'.))
(%i4) baz_quux: 'baz_quux;
(%o4)                       baz_quux
(%i5) baz_quux: sqrt(2);
Cannot assign to `baz_quux'.
#0: lambda([y],if y # 'baz_quux then
                 error("Cannot assign to `baz_quux'."))(y=sqrt(2))
 -- an error.  Quitting.  To debug this try debugmode(true);
(%i6) baz_quux;
(%o6)                       baz_quux
```

See also: `mode_declare`.

<!-- category: Other -->
<!-- keywords: dispfun -->
<!-- signatures: dispfun(f_1, ..., f_n), dispfun(all) -->
### Function: dispfun (f_1, ..., f_n)

Zeigt die Definitionen der nutzerdefinierten Funktionen *f_1*, ..., 
*f_n* an.  Die Argumente konnen gewohnliche Funktionen, Makros, 
Array-Funktionen oder indizierte Funktionen sein.


`dispfun(all)` zeigt die Definitionen aller nutzerdefinierten Funktionen
an, die in den Informationslisten `functions`, `arrays` oder
`macros` enthalten sind.


`dispfun` erzeugt Zwischenmarken `%t` fur jede einzelne anzuzeigende
Funktion und weist die Funktionsdefinitionen den Zwischenmarken zu.  Im 
Gegensatz dazu, zeigt die Funktion `fundef` die Funktionsdefinition ohne
Zwischenmarken an.


`dispfun` wertet die Argumente nicht aus.  `dispfun` gibt eine Liste
mit den Zwischenmarken zuruck, die zu den angezeigten Funktionen gehoren.


Beispiele:



```maxima
(%i1) m(x, y) ::= x^(-y);
                                     - y
(%o1)                   m(x, y) ::= x
(%i2) f(x, y) :=  x^(-y);
                                     - y
(%o2)                    f(x, y) := x
(%i3) g[x, y] :=  x^(-y);
                                    - y
(%o3)                     g     := x
                           x, y
(%i4) h[x](y) :=  x^(-y);
                                    - y
(%o4)                     h (y) := x
                           x
(%i5) i[8](y) :=  8^(-y);
                                    - y
(%o5)                     i (y) := 8
                           8
(%i6) dispfun (m, f, g, h, h[5], h[10], i[8]);
                                     - y
(%t6)                   m(x, y) ::= x

                                     - y
(%t7)                    f(x, y) := x

                                    - y
(%t8)                     g     := x
                           x, y

                                    - y
(%t9)                     h (y) := x
                           x

                                    1
(%t10)                     h (y) := --
                            5        y
                                    5


                                     1
(%t11)                    h  (y) := ---
                           10         y
                                    10


                                    - y
(%t12)                    i (y) := 8
                           8

(%o12)       [%t6, %t7, %t8, %t9, %t10, %t11, %t12]
(%i12) ''%;

                     - y              - y            - y
(%o12) [m(x, y) ::= x   , f(x, y) := x   , g     := x   , 
                                            x, y
                  - y           1              1             - y
        h (y) := x   , h (y) := --, h  (y) := ---, i (y) := 8   ]
         x              5        y   10         y   8
                                5             10
```

See also: `functions`, `arrays`, `macros`, `fundef`.

<!-- category: Other -->
<!-- keywords: fullmap -->
<!-- signatures: fullmap(f, expr_1, ...) -->
### Function: fullmap (f, expr_1, ...)

Die Funktion `fullmap` ist vergleichbar mit der Funktion `map`.
Im  Unterschied zu der Funktion `map` kann `fullmap` auf
verschachtelte Ausdrucke angewendet werden.


Intern wird `fullmap` von Maxima fur die Vereinfachung von Matrizen 
aufgerufen.  Daher konnen bei der Vereinfachung von Matrizen Fehlermeldungen 
im Zusammenhang mit `fullmap` auftreten, ohne dass die Funktion direkt 
aufgerufen wurde.


Beispiele:



```maxima
(%i1) a + b * c;
(%o1)                        b c + a
(%i2) fullmap (g, %);
(%o2)                   g(b) g(c) + g(a)
(%i3) map (g, %th(2));
(%o3)                     g(b c) + g(a)
```

See also: `map`.

<!-- category: Other -->
<!-- keywords: fullmapl -->
<!-- signatures: fullmapl(f, list_1, ...) -->
### Function: fullmapl (f, list_1, ...)

Die Funktion `fullmapl` ist vergleichbar mit `fullmap`.
`fullmapl` kann jedoch nur auf Matrizen und Listen angewendet werden kann.


Beispiele:



```maxima
(%i1) fullmapl ("+", [3, [4, 5]], [[a, 1], [0, -1.5]]);
(%o1)                [[a + 3, 4], [4, 3.5]]
```

See also: `fullmap`.

<!-- category: Other -->
<!-- keywords: functions -->
<!-- signatures: functions -->
### Variable: functions

Standardwert: `[]`


`functions` ist eine Informationsliste, die die vom Nutzer mit dem
Operator `:=` oder der Funktion `define` definierten Funktionen
enthalt.  Siehe auch die Systemvariable `infolists`.


Array-Funktionen und indizierte Funktionen werden nicht in die Informationsliste
`functions`, sondern in die Informationsliste `arrays`
eingetragen.


Beispiele:



```maxima
(%i1) F_1 (x) := x - 100;
(%o1)                   F_1(x) := x - 100
(%i2) F_2 (x, y) := x / y;
                                      x
(%o2)                    F_2(x, y) := -
                                      y
(%i3) define (F_3 (x), sqrt (x));
(%o3)                   F_3(x) := sqrt(x)
(%i4) G_1 [x] := x - 100;
(%o4)                    G_1  := x - 100
                            x
(%i5) G_2 [x, y] := x / y;
                                     x
(%o5)                     G_2     := -
                             x, y    y
(%i6) define (G_3 [x], sqrt (x));
(%o6)                    G_3  := sqrt(x)
                            x
(%i7) H_1 [x] (y) := x^y;
                                      y
(%o7)                     H_1 (y) := x
                             x
(%i8) functions;
(%o8)              [F_1(x), F_2(x, y), F_3(x)]
(%i9) arrays;
(%o9)                 [G_1, G_2, G_3, H_1]
```

See also: `:=`, `define`, `infolists`, `functions`, `arrays`.

<!-- category: Other -->
<!-- keywords: fundef -->
<!-- signatures: fundef(f) -->
### Function: fundef (f)

Gibt die Definition der Funktion *f* zuruck.


Das Argument *f* kann eine gewohnliche Funktion, eine Makro-Funktion, eine
Array-Funktion oder eine indizierte Funktion sein.


`fundef` wertet das Argument aus.  Siehe auch `dispfun`.

See also: `dispfun`.

<!-- category: Other -->
<!-- keywords: funmake -->
<!-- signatures: funmake(F, [arg_1, ..., arg_n]) -->
### Function: funmake (F, [arg_1, ..., arg_n])

Gibt den Ausdruck `F(arg_1, ..., arg_n)` zuruck.  Die
Ruckgabe wird vereinfacht, aber nicht ausgewertet.  Die Funktion *F* wird
also nicht aufgerufen, auch wenn diese existiert.


`funmake` versucht nicht, Array-Funktionen von gewohnlichen Funktionen zu 
unterscheiden.  Ist *F* der Name einer Array-Funktion, dann gibt
`funmake` einen Ausdruck der Form `F(...)` zuruck.
Fur Array-Funktionen kann die Funktion `arraymake` verwendet werden.


`funmake` wertet die Argumente aus.


Beispiele:


`funmake` angewendet auf eine gewohnliche Funktion.



```maxima
(%i1) F (x, y) := y^2 - x^2;
                                   2    2
(%o1)                  F(x, y) := y  - x
(%i2) funmake (F, [a + 1, b + 1]);
(%o2)                    F(a + 1, b + 1)
(%i3) ''%;
                              2          2
(%o3)                  (b + 1)  - (a + 1)
```


`funmake` angewendet auf ein Makro.



```maxima
(%i1) G (x) ::= (x - 1)/2;
                                  x - 1
(%o1)                    G(x) ::= -----
                                    2
(%i2) funmake (G, [u]);
(%o2)                         G(u)
(%i3) ''%;
                              u - 1
(%o3)                         -----
                                2
```


`funmake` angewendet auf eine indizierte Funktion.



```maxima
(%i1) H [a] (x) := (x - 1)^a;
                                        a
(%o1)                   H (x) := (x - 1)
                         a
(%i2) funmake (H [n], [%e]);
                                       n
(%o2)               lambda([x], (x - 1) )(%e)
(%i3) ''%;
                                    n
(%o3)                       (%e - 1)
(%i4) funmake ('(H [n]), [%e]);
(%o4)                        H (%e)
                              n
(%i5) ''%;
                                    n
(%o5)                       (%e - 1)
```


`funmake` angewendet auf ein Symbol, welches keine Funktion 
reprasentiert.



```maxima
(%i1) funmake (A, [u]);
(%o1)                         A(u)
(%i2) ''%;
(%o2)                         A(u)
```


`funmake` wertet die Argumente, aber nicht die Ruckgabe aus.



```maxima
(%i1) det(a,b,c) := b^2 -4*a*c;
                                    2
(%o1)              det(a, b, c) := b  - 4 a c
(%i2) (x : 8, y : 10, z : 12);
(%o2)                          12
(%i3) f : det;
(%o3)                          det
(%i4) funmake (f, [x, y, z]);
(%o4)                    det(8, 10, 12)
(%i5) ''%;
(%o5)                         - 284
```


Maxima vereinfacht den Ruckgabewert der Funktion `funmake`.



```maxima
(%i1) funmake (sin, [%pi / 2]);
(%o1)                           1
```

See also: `arraymake`.

<!-- category: Other -->
<!-- keywords: lambda -->
<!-- signatures: lambda([x_1, ..., x_m], expr_1, ..., expr_n), lambda([[L]], expr_1, ..., expr_n), lambda([x_1, ..., x_m, [L]], expr_1, ..., expr_n) -->
### Function: lambda ([x_1, ..., x_m], expr_1, ..., expr_n)

Definiert einen Lambda-Ausdruck, der auch als anonyme Funktion bezeichnet wird,
und gibt diesen zuruck.  Die Funktion kann Argumente *x_1*, ...,
*x_m* und optionale Argumente *L* haben.  Die Ruckgabe der Funktion
ist das Ergebnis des Ausdrucks *exprn*.  Ein Lambda-Ausdruck kann einer
Variablen zugewiesen werden und wertet wie eine gewohnliche Funktion aus.  Ein
Lambda-Ausdruck kann an solchen Stellen verwendet werden, wo der Name einer
Funktion erwartet wird.


Wird der Lambda-Ausdruck ausgewertet, werden lokale Variablen *x_1*, 
..., *x_m* erzeugt.  `lambda` kann innerhalb von Blocken oder 
anderen Lambda-Ausdrucken verwendet werden.  Mit jeder `block`-Anweisung 
oder jedem Lambda-Ausdruck werden erneut lokale Variablen erzeugt.  Die lokalen
Variablen sind jeweils global zu jeder eingeschlossenen `block`-Anweisung
oder zu jedem eingeschlossenen Lambda-Ausdruck.  Ist eine Variable innerhalb von
`block` oder `lambda` nicht lokal, hat sie den Wert der 
nachst hoheren Anweisung, die ihr einen Wert gibt oder den globalen Wert der 
Maxima-Umgebung.


Nachdem die lokalen Variablen erzeugt sind, werden die Ausdrucke *expr_1*,
..., *expr_n* nacheinander ausgewertet.  Die Systemvariable `%%`,
welche das Ergebnis eines vorhergehendes Ausdrucks enthalt, kann verwendet 
werden.  In einem Lambda-Ausdruck konnen die Anweisungen `catch` und
`throw` verwendet werden.


Die `return`-Anweisung kann in einem Lambda-Ausdruck nur verwendet werden,
wenn sie von einer `block`-Anweisung eingeschlossen wird.  Die 
`return`-Anweisung definiert jedoch den Ruckgabewert des Blocks und nicht 
des Lambda-Ausdrucks.  Auch die `go`-Anweisung kann in einem
Lambda-Ausdrucks nur in einem Block verwendet werden.


`lambda` wertet die Argumente nicht aus.


Beispiele:


Ein Lambda-Ausdruck kann einer Variablen zugewiesen werden und wie eine
gewohnliche Funktion ausgewertet werden.



```maxima
(%i1) f: lambda ([x], x^2);
                                      2
(%o1)                    lambda([x], x )
(%i2) f(a);
                                2
(%o2)                          a
```


Ein Lamda-Ausdruck kann an Stellen verwendet werden, wo der Name einer Funktion
erwartet wird.



```maxima
(%i3) lambda ([x], x^2) (a);
                                2
(%o3)                          a
(%i4) apply (lambda ([x], x^2), [a]);
                                2
(%o4)                          a
(%i5) map (lambda ([x], x^2), [a, b, c, d, e]);
                        2   2   2   2   2
(%o5)                 [a , b , c , d , e ]
```


Die Argumente sind lokale Variablen.  Andere Variablen sind globale Variablen.
Globale Variablen werden zu dem Zeitpunkt ausgewertet, wenn der Lambda-Ausdruck
ausgewertet wird.



```maxima
(%i6) a: %pi$
(%i7) b: %e$
(%i8) g: lambda ([a], a*b);
(%o8)                   lambda([a], a b)
(%i9) b: %gamma$
(%i10) g(1/2);
                             %gamma
(%o10)                       ------
                               2
(%i11) g2: lambda ([a], a*''b);
(%o11)                lambda([a], a %gamma)
(%i12) b: %e$
(%i13) g2(1/2);
                             %gamma
(%o13)                       ------
                               2
```


Lambda-Ausdrucke konnen verschachtelt werden.  Lokale Variablen eines
außeren Lambda-Ausdrucks sind global zu den enthaltenen
Lambda-Ausdrucken, außer diese werden wieder als lokal erklart.



```maxima
(%i14) h: lambda ([a, b], h2: lambda ([a], a*b), h2(1/2));
                                                   1
(%o14)    lambda([a, b], h2 : lambda([a], a b), h2(-))
                                                   2
(%i15) h(%pi, %gamma);
                             %gamma
(%o15)                       ------
                               2
```


Da `lambda` die Argumente nicht auswertet, definiert der unten angegebene
Ausdruck `i` keine Funktion "multipliziere mit `a`".  Solch eine
Funktion kann mit Hilfe der Funktion `buildq` definiert werden.



```maxima
(%i16) i: lambda ([a], lambda ([x], a*x));
(%o16)            lambda([a], lambda([x], a x))
(%i17) i(1/2);
(%o17)                  lambda([x], a x)
(%i18) i2: lambda([a], buildq([a: a], lambda([x], a*x)));
(%o18)    lambda([a], buildq([a : a], lambda([x], a x)))
(%i19) i2(1/2);
                                     x
(%o19)                   lambda([x], -)
                                     2
(%i20) i2(1/2)(%pi);
                               %pi
(%o20)                         ---
                                2
```


Ein Lambda-Ausdruck kann eine variable Anzahl an Argumenten haben, wenn das
letzte Argument eine Liste mit einem Element ist.



```maxima
(%i1) f : lambda ([aa, bb, [cc]], aa * cc + bb);
(%o1)          lambda([aa, bb, [cc]], aa cc + bb)
(%i2) f (foo, %i, 17, 29, 256);
(%o2)       [17 foo + %i, 29 foo + %i, 256 foo + %i]
(%i3) g : lambda ([[aa]], apply ("+", aa));
(%o3)             lambda([[aa]], apply(+, aa))
(%i4) g (17, 29, x, y, z, %e);
(%o4)                  z + y + x + %e + 46
```

See also: `catch`, `throw`, `return`, `go`, `buildq`.

<!-- category: Other -->
<!-- keywords: macroexpand -->
<!-- signatures: macroexpand(expr) -->
### Function: macroexpand (expr)

Ist das Argument *expr* ein Makro, wird das Makro expandiert, ohne dass es 
ausgewertet wird.  Ansonsten wird *expr* zuruckgegeben.


Ist die Expansion des Makros selbst ein Makro, wird dieses Makro wiederholt
expandiert.


`macroexpand` wertet das Argument *expr* nicht aus.  Hat die Expansion
des Makros Seiteneffekte, dann werden diese ausgefuhrt.


Siehe auch `::=` und `macroexpand1`.


Beispiele:



```maxima
(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99
(%i2) h (x) ::= buildq ([x], g (x - a));
(%o2)            h(x) ::= buildq([x], g(x - a))
(%i3) a: 1234;
(%o3)                         1234
(%i4) macroexpand (h (y));
                              y - a
(%o4)                         -----
                               99
(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

See also: `::=`, `macroexpand1`.

<!-- category: Other -->
<!-- keywords: macroexpand1 -->
<!-- signatures: macroexpand1(expr) -->
### Function: macroexpand1 (expr)

Gibt die Makro-Expansion von *expr* zuruck, ohne das Ergebnis auszuwerten.
Ist *expr* keine Makro-Funktion gibt `macroexpand1` das Argument
*expr* zuruck.


`macroexpand1` wertet das Argument nicht aus.  Hat die Expansion des Makros
Seiteneffekte, dann werden diese ausgefuhrt.


Enthalt die Expansion *expr* wiederum Makros, werden diese im Unterschied
zur Funktion `macroexpand` nicht expandiert.


Siehe auch `::=` und `macroexpand`.


Beispiele:



```maxima
(%i1) g (x) ::= x / 99;
                                    x
(%o1)                      g(x) ::= --
                                    99
(%i2) h (x) ::= buildq ([x], g (x - a))$
(%i3) a: 1234;
(%o3)                         1234
(%i4) macroexpand1 (h (y));
(%o4)                       g(y - a)
(%i5) h (y);
                            y - 1234
(%o5)                       --------
                               99
```

See also: `::=`, `macroexpand`.

<!-- category: Other -->
<!-- keywords: macroexpansion -->
<!-- signatures: macroexpansion -->
### Variable: macroexpansion

Standardwert: `false`


`macroexpansion` kontrolliert die Expansion von Makros.



**false** — Die Expansion des Makros wird nicht fur die aufrufende Funktion ersetzt.
**expand** — Wird die Makro-Funktion das erste Mal ausgewertet, wird die Expansion des Makros
gespeichert.  Weitere Aufrufe werten das Makro nicht erneut aus.  Seiteneffekte,
wie Zuweisungen an globale Variablen, werden nur bei der ersten Auswertung 
wirksam.  Die Expansion des Makros beeinflusst nicht andere Ausdrucke, die das
Makro ebenfalls aufrufen.
**displace** — Wird die Makro-Funktion das erste mal ausgewertet, wird die Expansion des Makros
in den aufrufenden Ausdruck eingesetzt.  Weitere Aufrufe werten das Makro nicht
erneut aus.  Seiteneffekte, wie Zuweisungen an globale Variablen, werden nur bei
der ersten Auswertung wirksam.  Die Expansion des Makros beeinflusst nicht 
andere Ausdrucke, die das Makro ebenfalls aufrufen.


Beispiele:


Hat `macroexpansion` den Wert `false`, wird eine Makro-Funktion
jedes mal aufgerufen, wenn der aufrufende Ausdruck ausgewertet wird.  Der
aufrufende Ausdruck wird nicht modifiziert.



```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)

(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));

(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: false;
(%o4)                         false
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o7)                       --------
                            a b + 99
```


Hat `macroexpansion` den Wert `expand`, wird eine Makro-Funktion nur
einmal aufgerufen.  Der aufrufende Ausdruck wird nicht modifiziert.



```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: expand;
(%o4)                        expand
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x
 
                            a b - 99
(%o5)                       --------
                            a b + 99

(%i6) dispfun (f);
                                  h(x)
(%t6)                     f(x) := ----
                                  g(x)

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```


Hat `macroexpansion` den Wert `displace`, wird eine Makro-Funktion
nur einmal aufgerufen.  Der aufrufende Ausdruck wird modifiziert.



```maxima
(%i1) f (x) := h (x) / g (x);
                                  h(x)
(%o1)                     f(x) := ----
                                  g(x)
(%i2) g (x) ::= block (print ("x + 99 is equal to", x),
                       return (x + 99));
(%o2) g(x) ::= block(print("x + 99 is equal to", x), 
                                                  return(x + 99))
(%i3) h (x) ::= block (print ("x - 99 is equal to", x),
                       return (x - 99));
(%o3) h(x) ::= block(print("x - 99 is equal to", x), 
                                                  return(x - 99))
(%i4) macroexpansion: displace;
(%o4)                       displace
(%i5) f (a * b);
x - 99 is equal to x 
x + 99 is equal to x 
                            a b - 99
(%o5)                       --------
                            a b + 99
(%i6) dispfun (f);
                                 x - 99
(%t6)                    f(x) := ------
                                 x + 99

(%o6)                         done
(%i7) f (a * b);
                            a b - 99
(%o7)                       --------
                            a b + 99
```

<!-- category: Other -->
<!-- keywords: macros -->
<!-- signatures: macros -->
### Variable: macros

Standardwert: `[]`


Die Systemvariable `macros` ist eine Informationsliste, die die vom Nutzer
mit dem Operator `::=` definierten Makros enthalt.  Wird das Makro mit
einer der Funktionen `kill`, `remove` oder `remfunction`
geloscht, wird der Eintrag aus der Informationsliste entfernt.  Siehe auch die
Systemvariable `infolists`.

See also: `::=`, `kill`, `remove`, `remfunction`, `infolists`.

<!-- category: Other -->
<!-- keywords: map -->
<!-- signatures: map(f, expr_1, ..., expr_n) -->
### Function: map (f, expr_1, ..., expr_n)

Gibt einen Ausdruck zuruck, dessen Hauptoperator derselbe ist, wie der der
Argumente *expr_1*, ..., *expr_n* aber dessen Operanden das Ergebnis
der Anwendung des Operators *f* auf die Teilausdrucke des Ausdrucks sind.
*f* ist entweder der Name einer Funktion mit $n$ Argumenten oder
ein Lambda-Ausdruck mit $n$ Argumenten.


Hat `maperror` den Wert `false`, wird die Anwendung der Funktion
*f* gestoppt, (1) wenn die Anwendung auf den kurzesten Ausdruck 
*expr_i* beendet ist und die Ausdrucke nicht alle dieselbe Lange haben 
oder (2) wenn die Ausdrucke *expr_i* einen verschiedenen Typ haben.  Hat 
`maperror` den Wert `true` wird in den obigen Fallen eine 
Fehlermeldung ausgegeben.








   
   

Beispiele:



```maxima
(%i1) map(f,x+a*y+b*z);
(%o1)                        f(b z) + f(a y) + f(x)
(%i2) map(lambda([u],partfrac(u,x)),x+1/(x^3+4*x^2+5*x+2));
                           1       1        1
(%o2)                     ----- - ----- + -------- + x
                         x + 2   x + 1          2
                                         (x + 1)
(%i3) map(ratsimp, x/(x^2+x)+(y^2+y)/y);
                                      1
(%o3)                            y + ----- + 1
                                    x + 1
(%i4) map("=",[a,b],[-0.5,3]);
(%o4)                          [a = - 0.5, b = 3]
```

See also: `maperror`.

<!-- category: Other -->
<!-- keywords: mapatom -->
<!-- signatures: mapatom(expr) -->
### Function: mapatom (expr)

Gibt den Wert `true` zuruck, wenn der Ausdruck *expr* von Funktionen 
die auf Argumente angewendete werden, als ein Atom betrachtet wird.  Als Atome
werden Zahlen, einschließlich rationaler Zahlen und großer 
Gleitkommazahlen, Symbole und indizierte Symbole betrachtet.

<!-- category: Other -->
<!-- keywords: maperror -->
<!-- signatures: maperror -->
### Variable: maperror

Standardwert: `true`


Hat `maperror` den Wert `false`, wird die Anwendung der Funktion 
*f* gestoppt, (1) wenn die Anwendung auf den kurzesten Ausdruck 
*expr_i* beendet ist und die Ausdrucke nicht alle dieselbe Lange haben 
oder (2) wenn die Ausdrucke *expr_i* einen verschiedenen Typ haben.  Hat 
`maperror` den Wert `true` wird in den obigen Fallen eine 
Fehlermeldung ausgegeben.

<!-- category: Other -->
<!-- keywords: maplist -->
<!-- signatures: maplist(f, expr_1, ..., expr_n) -->
### Function: maplist (f, expr_1, ..., expr_n)

Wendet die Funktion *f* auf die Ausdrucke *expr_1*, ..., 
*expr_n* an und gibt das Ergebnis als eine Liste zuruck.  *f* ist der 
Name einer Funktion oder ein lambda-Ausdruck.


Im Unterschied zu `maplist` gibt die Funktion `map` einen Ausdruck
zuruck, der denselben Hauptoperator wie die Ausdrucke *expr_i* hat.

See also: `map`.

<!-- category: Other -->
<!-- keywords: mapprint -->
<!-- signatures: mapprint -->
### Variable: mapprint

Standardwert: `true`


Hat `mapprint` den Wert `true`, werden verschiedene Informationen von
den Funktionen `map`, `maplist` und `fullmap` ausgegeben.
Dies ist der Fall, wenn die Funktion `map` die Funktion `apply`
aufruft oder wenn fur die Funktion `map` die Argumente eine verschiedene
Lange haben.


Hat `mapprint` den Wert `false`, werden diese Meldungen unterdruckt.

See also: `map`, `maplist`, `fullmap`.

<!-- category: Other -->
<!-- keywords: outermap -->
<!-- signatures: outermap(f, a_1, ..., a_n) -->
### Function: outermap (f, a_1, ..., a_n)

Wendet die Funktion *f* auf jedes Element des außeren Produktes der
Argumente *a_1* `x` *a_2* `x` ... `x` *a_n* an. 


*f* ist der Name einer Funktion mit $n$ Argumenten oder ein 
Lambda-Ausdruck mit $n$ Argumenten.  Jedes Argument *a_k* kann eine
Liste oder verschachtelte Liste, eine Matrix oder irgendein anderer Ausdruck
sein.








`outermap` wertet die Argumente aus.


Siehe auch `map`, `maplist` und `apply`.


Beispiele:


Einfaches Beispiel fur `outermap`.  Die Funktion `F` ist 
undefiniert.



```maxima
(%i1) outermap(F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) outermap(F, matrix([a, b],[c, d]), matrix([1, 2],[3, 4]));
         [ [ F(a, 1)  F(a, 2) ]  [ F(b, 1)  F(b, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(a, 3)  F(a, 4) ]  [ F(b, 3)  F(b, 4) ] ]
(%o2)    [                                            ]
         [ [ F(c, 1)  F(c, 2) ]  [ F(d, 1)  F(d, 2) ] ]
         [ [                  ]  [                  ] ]
         [ [ F(c, 3)  F(c, 4) ]  [ F(d, 3)  F(d, 4) ] ]
(%i3) outermap (F, [a, b], x, matrix ([1, 2], [3, 4]));
       [ F(a, x, 1)  F(a, x, 2) ]  [ F(b, x, 1)  F(b, x, 2) ]
(%o3) [[                        ], [                        ]]
       [ F(a, x, 3)  F(a, x, 4) ]  [ F(b, x, 3)  F(b, x, 4) ]
(%i4) outermap (F, [a, b], matrix ([1, 2]), matrix ([x], [y]));
       [ [ F(a, 1, x) ]  [ F(a, 2, x) ] ]
(%o4) [[ [            ]  [            ] ], 
       [ [ F(a, 1, y) ]  [ F(a, 2, y) ] ]
                              [ [ F(b, 1, x) ]  [ F(b, 2, x) ] ]
                              [ [            ]  [            ] ]]
                              [ [ F(b, 1, y) ]  [ F(b, 2, y) ] ]
(%i5) outermap ("+", [a, b, c], [1, 2, 3]);
(%o5) [[a + 1, a + 2, a + 3], [b + 1, b + 2, b + 3], 
                                           [c + 1, c + 2, c + 3]]
```


Das Beispiel zeigt die Ruckgabe der Funktion `outermap` detaillierter.
Das erste, zweite und dritte Argument sind eine Matrix, eine Liste und eine
Matrix.  Der Ruckgabewert ist eine Matrix.  Jedes Element der Matrix ist eine
Liste und jedes Element der Liste ist eine Matrix.



```maxima
(%i1) arg_1 :  matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) arg_2 : [11, 22];
(%o2)                       [11, 22]
(%i3) arg_3 : matrix ([xx, yy]);
(%o3)                      [ xx  yy ]
(%i4) xx_0 : outermap(lambda([x, y, z], x / y + z), arg_1,
                                                   arg_2, arg_3);
               [  [      a        a  ]  [      a        a  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
(%o4)  Col 1 = [                                              ]
               [  [      c        c  ]  [      c        c  ]  ]
               [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
               [  [      11       11 ]  [      22       22 ]  ]
                 [  [      b        b  ]  [      b        b  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
         Col 2 = [                                              ]
                 [  [      d        d  ]  [      d        d  ]  ]
                 [ [[ xx + --  yy + -- ], [ xx + --  yy + -- ]] ]
                 [  [      11       11 ]  [      22       22 ]  ]
(%i5) xx_1 : xx_0 [1][1];
           [      a        a  ]  [      a        a  ]
(%o5)     [[ xx + --  yy + -- ], [ xx + --  yy + -- ]]
           [      11       11 ]  [      22       22 ]
(%i6) xx_2 : xx_0 [1][1] [1];
                      [      a        a  ]
(%o6)                 [ xx + --  yy + -- ]
                      [      11       11 ]
(%i7) xx_3 : xx_0 [1][1] [1] [1][1];
                                  a
(%o7)                        xx + --
                                  11
(%i8) [op (arg_1), op (arg_2), op (arg_3)];
(%o8)                  [matrix, [, matrix]
(%i9) [op (xx_0), op (xx_1), op (xx_2)];
(%o9)                  [matrix, [, matrix]
```


`outermap` erhalt die Struktur der Argumente im Ergebnis.  Die Funktion
`cartesian_product` erhalt die Struktur der Argumente nicht.



```maxima
(%i1) outermap (F, [a, b, c], [1, 2, 3]);
(%o1) [[F(a, 1), F(a, 2), F(a, 3)], [F(b, 1), F(b, 2), F(b, 3)], 
                                     [F(c, 1), F(c, 2), F(c, 3)]]
(%i2) setify (flatten (%));
(%o2) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i3) map(lambda([L], apply(F, L)),
                     cartesian_product({a, b, c}, {1, 2, 3}));
(%o3) {F(a, 1), F(a, 2), F(a, 3), F(b, 1), F(b, 2), F(b, 3), 
                                       F(c, 1), F(c, 2), F(c, 3)}
(%i4) is (equal (%, %th (2)));
(%o4)                         true
```

See also: `map`, `maplist`, `apply`.

<!-- category: Other -->
<!-- keywords: remfunction -->
<!-- signatures: remfunction(f_1, ..., f_n), remfunction(all) -->
### Function: remfunction (f_1, ..., f_n)

Hebt die Bindung der Symbole *f_1*, ..., *f_n* an ihre
Funktionsdefinitionen auf.  Die Argumente konnen die Namen von Funktionen 
sein, die mit dem Operator `:=` oder der Funktion `define` definiert
wurden sowie Makro-Funktionen, die mit dem Operator `::=` definiert wurden.


`remfunction(all)` entfernt alle Bindungen von Funktionsdefinitionen.


`remfunction` gibt eine Liste mit den Symbolen zuruck, die von ihren 
Funktionsdefinitionen entbunden wurden.  `false` wird fur die Symbole
zuruckgegeben, fur die es keine Funktionsdefinition gibt.


`remfunction` wertet die Argumente nicht aus.


`remfunction` kann nicht auf Array-Funktionen und indizierte Funktionen
angewendet werden.  Fur diese Funktionen kann `remarray` verwendet
werden.

See also: `:=`, `define`, `::=`, `remarray`.

<!-- category: Other -->
<!-- keywords: scanmap -->
<!-- signatures: scanmap(f, expr), scanmap(f, expr, bottomup), scanmap(f, expr, topdown) -->
### Function: scanmap (f, expr)

Wendet die Funktion *f* rekursiv auf alle Teilausdrucke in *expr* an.
Dies kann zum Beispiel verwendet werden, um einen Ausdruck vollstandig zu 
faktorisieren.


Beispiele:



```maxima
(%i1) exp:(a^2+2*a+1)*y + x^2$
(%i2) scanmap(factor,exp);
                                    2      2
(%o2)                         (a + 1)  y + x
```



```maxima
(%i3) scanmap(factor,expand(exp));
                           2                  2
(%o3)                      a  y + 2 a y + y + x
```


Ein weiteres Beispiel fur die Anwendung einer Funktion auf alle 
Teilausdrucke.



```maxima
(%i4) expr : u*v^(a*x+b) + c$
(%i5) scanmap('f, expr);
                    f(f(f(a) f(x)) + f(b))
(%o5) f(f(f(u) f(f(v)                      )) + f(c))
```


`scanmap (f, expr, bottomup)` wendet die Funktion *f*
Bottom-up auf den Ausdruck *expr* an.





```maxima
scanmap(f,a*x+b) ->
   f(a*x+b) -> f(f(a*x)+f(b)) -> f(f(f(a)*f(x))+f(b))
scanmap(f,a*x+b,bottomup) -> f(a)*f(x)+f(b)
    -> f(f(a)*f(x))+f(b) ->
     f(f(f(a)*f(x))+f(b))
```


`scanmap (f, expr, topdown)` verhalt sich genau wie
`scanmap (f, expr)`.

<!-- category: Other -->
<!-- keywords: splice -->
<!-- signatures: splice(a) -->
### Function: splice (a)

Die Funktion `splice` kann nur im Zusammenhang mit der Funktion 
`buildq` verwendet werden.  Das Argument *a* bezeichnet eine Liste, die
an Stelle von `splice(a)` in einen Ausdruck eingefugt wird.  *a* kann
nicht selbst eine Liste oder ein Ausdruck sein, der zu einer Liste auswertet.


Beispiele:



```maxima
(%i1) buildq ([x: [1, %pi, z - y]], foo (splice (x)) / length (x));
                       foo(1, %pi, z - y)
(%o1)                -----------------------
                     length([1, %pi, z - y])
(%i2) buildq ([x: [1, %pi]], "/" (splice (x)));
                                1
(%o2)                          ---
                               %pi
(%i3) matchfix ("<>", "<>");
(%o3)                          <>
(%i4) buildq ([x: [1, %pi, z - y]], "<>" (splice (x)));
(%o4)                   <>1, %pi, z - y<>
```

See also: `buildq`.

