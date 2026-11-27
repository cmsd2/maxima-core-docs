## Datentypen und Strukturen

<!-- category: Programming -->
<!-- keywords: [, ] -->
<!-- signatures: ] -->
### Variable: [

Die Operatoren `[` und `]` markieren den Anfang und das Ende einer
Liste.


`[` und `]` schließen auch die Indizes von Symbolen, Arrays, 
Hash-Arrays oder Array-Funktionen ein.


Beispiele:



```maxima
(%i1) x: [a, b, c];
(%o1)                       [a, b, c]
(%i2) x[3];
(%o2)                           c
(%i3) array (y, fixnum, 3);
(%o3)                           y
(%i4) y[2]: %pi;
(%o4)                          %pi
(%i5) y[2];
(%o5)                          %pi
(%i6) z['foo]: 'bar;
(%o6)                          bar
(%i7) z['foo];
(%o7)                          bar
(%i8) g[k] := 1/(k^2+1);
                                  1
(%o8)                     g  := ------
                           k     2
                                k  + 1
(%i9) g[10];
                                1
(%o9)                          ---
                               101
```

<!-- category: Programming -->
<!-- keywords: append -->
<!-- signatures: append(list_1, ..., list_n) -->
### Function: append (list_1, ..., list_n)

Gibt eine Liste mit den Elementen der Listen *list_1*, ..., *list_n*
zuruck.  Ist eines der Argumente *list_1*, ..., *list_n* keine
Liste meldet Maxima einen Fehler.


`append` kann auch fur allgemeine Ausdrucke genutzt werden.
So hat zum Beispiel `append(f(a,b), f(c,d,e))` das Ergebnis
`f(a,b,c,d,e)`.  In diesem Fall muss der Operator, der hier `f` ist,
fur beide Ausdrucke identisch sein, ansonsten meldet Maxima einen Fehler.


Siehe auch die Funktionen `cons` und `endcons`, um ein Element
einer Liste hin­zu­zu­fu­gen.


Beispiele:


In den ersten Beispielen werden jeweils Listen mit verschiedenen Elementen
zusammengefugt.  Im letzten Beispiel wird `append` genutzt, um zwei
Additionen zusammenzusetzen.



```maxima
(%i1) append([a,b], [x,y,z], [1]);
(%o1)                  [a, b, x, y, z, 1]
(%i2) append([x+y, 0, -3.2], [2.5e+20, x]);
(%o2)             [y + x, 0, - 3.2, 2.5e+20, x]
(%i3) append([2*a+b], [x+y]);
(%o3)                   [b + 2 a, y + x]
(%i4) append(2*a+b, x+y);
(%o4)                    y + x + b + 2 a
```

See also: `cons`, `endcons`.

<!-- category: Programming -->
<!-- keywords: array -->
<!-- signatures: array(name, dim_1, ..., dim_n), array(name, type, dim_1, ..., dim_n), array([name_1, ..., name_m], dim_1, ..., dim_n), array([name_1, ..., name_m], type, dim_1, ..., dim_n) -->
### Function: array (name, dim_1, ..., dim_n)

Erzeugt ein $n$-dimensionales Array.  Das Array kann bis zu 5 Dimensionen
haben.  Die Indizes der $i$-ten Dimension sind ganze Zahlen in einem 
Bereich von 0 bis einschließlich *dim_i*.


`array(name, dim_1, ..., dim_n)` erzeugt ein Array, 
dessen Elemente einen beliebigen Typ haben und auch Symbole oder Ausdrucke
sein konnen.


`array(name, type, dim_1, ..., dim_n)` erzeugt 
ein Array mit Elementen, die vom Typ *type* sind.  Das Argument *type*
kann `fixnum` fur ganze Zahlen oder `flonum` fur Gleitkommazahlen
sein.

 

`array([name_1, ..., name_m], dim_1, ..., dim_n)`
erzeugt $m$ Arrays, die alle die gleiche Dimension haben.  Wie oben kann
weiterhin der Typ der Arrays durch Angabe des Argumentes *type* als
`fixnum` oder `flonum` festgelegt werden.


Mit der Funktion `array` konnen nicht-deklarierte Arrays in ein
deklariertes Array umgewandelt werden.  Wenn das deklarierte einen Typ erhalten
soll, mussen alle Elemente des nicht-deklarierten Arrays von diesem Typ sein.


Siehe auch die Funktion `make_array`, um ein Lisp-Array zu erzeugen,
sowie die Optionsvariable `use_fast_arrays`.


Beispiele:


Es werden zwei verschiedene Arrays definiert.  Im ersten Fall erhalt das Array
keinen Typ.  Elemente, denen noch kein Wert zugewiesen wurde, werden mit dem
Symbol `#####` initialisiert.  Im zweiten Fall ist das Array vom Typ 
`fixnum`.  Jetzt wird das Array mit dem Wert `0` initialisiert.



```maxima
(%i1) array(a, 2, 2);
(%o1)                           a
(%i2) a[0,0]: 0; a[1,1]:11; a[2,2]:22;
(%o2)                           0
(%o3)                          11
(%o4)                          22
(%i5) listarray(a);
(%o5) [0, #####, #####, #####, 11, #####, #####, #####, 22]
(%i6) array(b, fixnum, 2, 2);
(%o6)                           b
(%i7) b[0,0]: 0; b[1,1]:11; b[2,2]:22;
(%o7)                           0
(%o8)                          11
(%o9)                          22
(%i10) listarray(b);
(%o10)            [0, 0, 0, 0, 11, 0, 0, 0, 22]
```


Ein nicht-deklariertes Array kann in ein deklariertes Array umgewandelt werden.



```maxima
(%i1) a[1,1]:11;
(%o1)                          11
(%i2) a[2,2]:22;
(%o2)                          22
(%i3) arrayinfo(a);
(%o3)              [hashed, 2, [1, 1], [2, 2]]
(%i4) array(a, fixnum, 2, 2);
(%o4)                           a
(%i5) arrayinfo(a);
(%o5)                 [complete, 2, [2, 2]]
```

See also: `make_array`, `use_fast_arrays`.

<!-- category: Programming -->
<!-- keywords: arrayapply -->
<!-- signatures: arrayapply(A, [i_1, ..., i_n]) -->
### Function: arrayapply (A, [i_1, ..., i_n])

Wertet `A[i_1, ... , i_n]` aus, wobei *A* ein Array
und *i_1*, ..., *i_n* die Indizes eines Array-Elementes sind.


Siehe auch die Funktion `subvar`, die die gleiche Funktionalitat hat,
sowie die Funktion `arraymake`, die die Referenz auf das Array-Element
nicht auswertet.


Beispiele:


Die Funktion `arrayapply` wertet die Referenz auf ein Array-Element aus.
Im Unterschied dazu wertet die Funktion `arraymake` die Referenz nicht aus.
Die Funktion `subvar` hat die gleiche Funktionalitat wie
`arrayapply`.



```maxima
(%i1) a[1,2]: 12;
(%o1)                          12
(%i2) a[x,y]: x^y;
                                y
(%o2)                          x
(%i3) arrayapply(a, [1, 2]);
(%o3)                          12
(%i4) arrayapply(a, [x, y]);
                                y
(%o4)                          x
(%i5) arraymake(a, [x,y]);
(%o5)                         a
                               x, y
(%i6) subvar(a, x, y);
                                y
(%o6)                          x
```

See also: `subvar`, `arraymake`.

<!-- category: Programming -->
<!-- keywords: arrayinfo -->
<!-- signatures: arrayinfo(A) -->
### Function: arrayinfo (A)

Gibt Informationen uber das Array *A* zuruck.  Das Argument *A* kann
ein deklariertes oder ein nicht-deklariertes Array sowie eine Array-Funktion
oder eine indizierte Funktion sein.


Fur ein deklarierte Array gibt `arrayinfo` eine Liste zuruck, die 
`declared`, die Zahl der Dimensionen und die Große der Dimensionen 
enthalt.  Die Elemente des Arrays werden von der Funktion `listarray`
zuruckgegeben.


Fur ein nicht-deklariertes Array (Hashed-Array) gibt `arrayinfo` eine
Liste zuruck, die `hashed`, die Zahl der Indizes und die Indizes
enthalt, deren Elemente einen Wert haben.  Die Werte der Elemente werden mit
der Funktion `listarray` zuruckgegeben.


Fur Array-Funktionen gibt `arrayinfo` eine Liste zuruck, die 
`hashed` die Zahl der Indizes und die Indizes enthalt, fur die 
Funktionen im Array enthalten sind.  Die Funktionen werden mit der Funktion 
`listarray` angezeigt.


Fur indizierte Funktionen gibt `arrayinfo` eine Liste zuruck, die 
`hashed`, die Zahl der Indizes und die Indizes enthalt, fur die 
Lambda-Ausdrucke vorhanden sind.  Die `lambda`-Ausdrucke werden von der
Funktion `listarray` angezeigt.


Die Funktion `arrayinfo` kann auch fur Lisp-Arrays angewendet werden,
die mit der Funktion `make_array` erzeugt werden.


Beispiele:


`arrayinfo` und `listarray` angewendet auf ein deklariertes Array.



```maxima
(%i1) array(aa, 2, 3);
(%o1)                          aa


(%i2) aa[2, 3] : %pi;
(%o2)                          %pi


(%i3) aa[1, 2] : %e;
(%o3)                          %e


(%i4) arrayinfo(aa);
(%o4)                 [declared, 2, [2, 3]]


(%i5) listarray(aa);
(%o5) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]
```


`arrayinfo` und `listarray` angewendet auf ein nicht-deklariertes
Array.



```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)


(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)


(%i3) arrayinfo (bb);
(%o3)               [hashed, 1, [BAR], [FOO]]


(%i4) listarray (bb);
                              3         2
(%o4)                 [(c - d) , (b + a) ]
```


`arrayinfo` und `listarray` angewendet auf eine Array-Funktion.



```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x


(%i2) cc [u, v];
                                v
(%o2)                           -
                                u


(%i3) cc [4, z];
                                z
(%o3)                           -
                                4


(%i4) arrayinfo (cc);
(%o4)              [hashed, 2, [4, z], [u, v]]


(%i5) listarray (cc);
                              z  v
(%o5)                        [-, -]
                              4  u
```


`arrayinfo` und `listarray` angewendet auf eine indizierte Funktion.



```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x


(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )


(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )


(%i4) arrayinfo (dd);
(%o4)             [hashed, 1, [b + a], [v - u]]


(%i5) listarray (dd);
                         b + a                v - u
(%o5)      [lambda([y], y     ), lambda([y], y     )]
```

See also: `listarray`, `lambda`, `make_array`.

<!-- category: Programming -->
<!-- keywords: arraymake -->
<!-- signatures: arraymake(A, [i_1, ..., i_n]) -->
### Function: arraymake (A, [i_1, ..., i_n])

Gibt den Ausdruck `A[i_1, ..., i_n]` zuruck.  Das 
Ergebnis ist eine nicht ausgewertete Referenz auf ein Element des Arrays
*A*.  `arraymake` ist vergleichbar mit der Funktion `funmake`.


Ist das Array *A* ein Lisp-Array, wie es mit der Funktion 
`make_array` erzeugt wird, dann gibt `arraymake` einen Lisp-Fehler
zuruck.  Das ist ein Programmfehler.


Siehe auch die Funktionen `arrayapply` und `subvar`, die die
Referenz auswerten.


Beispiele:



```maxima
(%i1) arraymake (A, [1]);
(%o1)                          A
                                1


(%i2) arraymake (A, [k]);
(%o2)                          A
                                k


(%i3) arraymake (A, [i, j, 3]);
(%o3)                       A
                             i, j, 3


(%i4) array (A, fixnum, 10);
(%o4)                           A


(%i5) fillarray (A, makelist (i^2, i, 1, 11));
(%o5)                           A


(%i6) arraymake (A, [5]);
(%o6)                          A
                                5


(%i7) ''%;
(%o7)                          36


(%i8) L : [a, b, c, d, e];
(%o8)                    [a, b, c, d, e]


(%i9) arraymake ('L, [n]);
(%o9)                          L
                                n


(%i10) ''%, n = 3;
(%o10)                          c


(%i11) A2 : make_array (fixnum, 10);
(%o11)          {Array:  #(0 0 0 0 0 0 0 0 0 0)}


(%i12) fillarray (A2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o12)          {Array:  #(1 2 3 4 5 6 7 8 9 10)}


(%i13) arraymake ('A2, [8]);
(%o13)                         A2
                                 8


(%i14) ''%;
(%o14)                          9
```

See also: `funmake`, `make_array`, `arrayapply`, `subvar`.

<!-- category: Programming -->
<!-- keywords: arrays -->
<!-- signatures: arrays -->
### Variable: arrays

Standardwert: `[]`


`arrays` ist eine Informationsliste `infolists` der vom Nutzer 
definierten Arrays.  Die Liste enthalt deklarierte Arrays, nicht-deklarierte
Arrays und Array-Funktionen, die der Nutzer mit dem Operator `:=` oder der
Funktion `define` definiert hat.  Dagegen sind Arrays, die mit
`make_array` definiert sind, nicht in der Liste enthalten.


Siehe auch die Funktion `array`, um ein Array zu definieren.


Beispiele:



```maxima
(%i1) array (aa, 5, 7);
(%o1)                          aa


(%i2) bb [FOO] : (a + b)^2;
                                   2
(%o2)                       (b + a)


(%i3) cc [x] := x/100;
                                   x
(%o3)                      cc  := ---
                             x    100


(%i4) dd : make_array ('any, 7);
(%o4)       {Array:  #(NIL NIL NIL NIL NIL NIL NIL)}


(%i5) arrays;
(%o5)                     [aa, bb, cc]
```

See also: `infolists`, `:=`, `define`, `make_array`, `array`.

<!-- category: Programming -->
<!-- keywords: assoc -->
<!-- signatures: assoc(key, list, default), assoc(key, list) -->
### Function: assoc (key, list, default)

Ist das Argument `list` eine Liste mit paarweisen Elementen der Form
`[[key_1, value_1], [key_2, value_2], ...]`, wobei *key_i* ein
Schlussel und *value_i* der dazugehorige Wert ist, dann gibt die
Funktion `assoc` den zum Schlussel *key* gehorenden Wert
`value` zuruck.  Wird der Schlussel nicht gefunden, wird das Argument
`default` zuruckgegeben, wenn es vorhanden ist, oder der Wert
`false`.


Anstatt Paare `[key_i, value_i]` konnen auch allgemeine Ausdrucke in 
der Liste enthalten sein, die zwei Argumente haben.  Zum Beispiel sind 
Eintrage der Form `x=1` oder `a^b` moglich.  Im ersten Fall ist 
`x` der Schlussel und im zweiten Fall `a`.  Die Werte sind jeweils 
`1` und `b`.


Beispiele:



```maxima
(%i1) l : [[info, 10], [warn, 20], [err, 30]];
(%o1)          [[info, 10], [warn, 20], [err, 30]]
(%i2) assoc(info, l);
(%o2)                          10
(%i3) assoc(warn, l);
(%o3)                          20
(%i4) assoc(err, l);
(%o4)                          30
(%i5) l : [x+y, a^(2*b), sin(x) = 0.5];
                            2 b
(%o5)              [y + x, a   , sin(x) = 0.5]
(%i6) assoc(x, l);
(%o6)                           y
(%i7) assoc(y, l);
(%o7)                         false
(%i8) assoc(a, l);
(%o8)                          2 b
(%i9) assoc(sin(x), l);
(%o9)                          0.5
```

<!-- category: Programming -->
<!-- keywords: cons -->
<!-- signatures: cons(expr, list) -->
### Function: cons (expr, list)

Fugt den Ausdruck *expr* als erstes Element der Liste *list* hinzu.


`cons` arbeitet auch mit allgemeinen Ausdrucken als Argument *list*.
In diesem Fall wird dem Hauptoperator des Arguments *list* der Ausdruck
*expr* als erstes Argument hinzugefugt.


Siehe auch die Funktion `endcons`, um ein Element an das Ende einer
Liste anzuhangen sowie die Funktion `append`, um zwei Listen
zusammenzufugen.


Beispiele:



```maxima
(%i1) cons(x, [a, b, c]);
(%o1)                     [x, a, b, c]
(%i2) cons(x^2+1, [a, b, c]);
                          2
(%o2)                   [x  + 1, a, b, c]
(%i3) cons(x^2+1, a+b+c);
                        2
(%o3)                  x  + c + b + a + 1
(%i4) cons(x^2+1, f(a,b,c));
                          2
(%o4)                  f(x  + 1, a, b, c)
```

See also: `endcons`, `append`.

<!-- category: Programming -->
<!-- keywords: copylist -->
<!-- signatures: copylist(list) -->
### Function: copylist (list)

Gibt eine Kopie der Liste *list* zuruck.


Im Unterschied zur Funktion `copylist` wird mit dem Zuweisungsoperator
`:` keine Kopie, sondern eine Referenz auf das Original zugewiesen.  Das
folgende Beispiel zeigt den Unterschied fur den Fall, dass das Original
modifiziert wird.



```maxima
(%i1) list : [x,y,z];
(%o1)                       [x, y, z]
(%i2) a: list;
(%o2)                       [x, y, z]
(%i3) b: copylist(list);
(%o3)                       [x, y, z]
(%i4) list[2]:99;
(%o4)                          99
(%i5) list;
(%o5)                      [x, 99, z]
(%i6) a;
(%o6)                      [x, 99, z]
(%i7) b;
(%o7)                       [x, y, z]
```

See also: `:`.

<!-- category: Programming -->
<!-- keywords: create_list -->
<!-- signatures: create_list(expr, x_1, list_1, ..., x_n, list_n) -->
### Function: create_list (expr, x_1, list_1, ..., x_n, list_n)

Erzeugt eine Liste, indem der Ausdruck *expr* zunachst fur die Variable
*x_1* ausgewertet wird.  Der Variablen *x_1* werden fur die Auswertung 
nacheinander die Werte der Liste *list_1* zugewiesen.  Dann wird der
Ausdruck *expr* fur die Variable *x_2* mit den Werten der Liste
*list_2* ausgewertet u.s.w.  Die Anzahl der Elemente der Ergebnisliste ist
das Produkt der Anzahl der Elemente der einzelnen Listen *list_i*.  Die
Variablen *x_i* mussen Symbole sein, die nicht ausgewertet werden.  Die 
Elemente der Listen *list_i* werden vor der Iteration ausgewertet.


Anstatt einer Liste *list_i* mit den Elementen fur die Iteration kann auch
eine untere und obere Grenze angegeben werden.  Die Grenzen konnen ganze
Zahlen oder Gleitkommazahlen sowie Ausdrucke sein, die zu einer Zahl
auswerten.  Die Schrittweite ist immer 1.  Siehe auch das Beispiel weiter unten.


Beispiele:



```maxima
(%i1) create_list(x^i, i, [1, 3, 7]);
                 3   7
(%o1)       [x, x , x ]
```


In diesem Beispiel wird fur zwei Listen iteriert.



```maxima
(%i1) create_list([i, j], i, [a, b], j, [e, f, h]);
(%o1) [[a, e], [a, f], [a, h], [b, e], [b, f], [b, h]]
```


Anstatt einer Liste *list_i* konnen auch zwei Argumente ubergeben 
werden, die jedes zu einer Nummer auswerten.  Diese Werte sind die untere und
die obere Grenze fur die Iteration.



```maxima
(%i1) create_list([i,j],i,[1,2,3],j,1,i);
(%o1) [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]
```

<!-- category: Programming -->
<!-- keywords: delete -->
<!-- signatures: delete(expr, list), delete(expr, list, n) -->
### Function: delete (expr, list)

`delete(expr, list)` entfernt aus der Liste *list* die
Elemente, die gleich dem Ausdruck *expr* sind.  Mit dem Argument *n*
kann die Anzahl der Elemente spezifiziert werden, die aus der Liste entfernt
werden sollen.  `delete` gibt eine neue Liste zuruck.  Das Argument
*list* wird nicht modifiziert.


Die Gleichheit wird mit dem Operator `=` gepruft.  Daher werden nur
Ausdrucke als gleich erkannt, die syntaktisch ubereinstimmen.  Aquivalente
Ausdrucke, die syntaktisch voneinander verschieden sind, werden nicht aus der
Liste entfernt.  Zum Beispiel sind die Ausdrucke `x^2-1` und
`(x+1)*(x-1)` aquivalent, aber syntaktisch verschieden.


Das zweite Argument *list* kann auch ein allgemeiner Ausdruck sein.  In 
diesem Fall werden die Argumente des Hauptoperators als die Elemente einer Liste
angenommen.


Beispiele:


Entferne Elemente einer Liste.



```maxima
(%i1) delete (y, [w, x, y, z, z, y, x, w]);
(%o1)                  [w, x, z, z, x, w]
```


Entferne Terme einer Summe.



```maxima
(%i1) delete (sin(x), x + sin(x) + y);
(%o1)                         y + x
```


Entferne Faktoren eines Produkts.



```maxima
(%i1) delete (u - x, (u - w)*(u - x)*(u - y)*(u - z));
(%o1)                (u - w) (u - y) (u - z)
```


Entferne Argumente einer Funktion.



```maxima
(%i1) delete (a, f(a, b, c, d, a));
(%o1)                     f(b, c, d)
```


Das Element `a` tritt mehrfach auf.  Es werden zwei Elemente entfernt.



```maxima
(%i1) delete (a, f(a, b, a, c, d, a), 2);
(%o1)                    f(b, c, d, a)
```


Die Gleichheit wird mit dem Operator `=` gepruft.



```maxima
(%i1) [is(equal (0, 0)), is(equal (0, 0.0)), is(equal (0, 0b0))];

`rat' replaced 0.0 by 0/1 = 0.0
`rat' replaced 0.0B0 by 0/1 = 0.0B0
(%o1)                  [true, true, true]
(%i2) [is (0 = 0), is (0 = 0.0), is (0 = 0b0)];
(%o2)                 [true, false, false]
(%i3) delete (0, [0, 0.0, 0b0]);
(%o3)                     [0.0, 0.0b0]
(%i4) is (equal ((x + y)*(x - y), x^2 - y^2));
(%o4)                         true
(%i5) is ((x + y)*(x - y) = x^2 - y^2);
(%o5)                         false
(%i6) delete ((x + y)*(x - y), [(x + y)*(x - y), x^2 - y^2]);
                              2    2
(%o6)                       [x  - y ]
```

See also: `=`.

<!-- category: Programming -->
<!-- keywords: endcons -->
<!-- signatures: endcons(expr, list) -->
### Function: endcons (expr, list)

Fugt den Ausdruck *expr* als letztes Element der Liste *list* hinzu.


`endcons` arbeitet auch mit allgemeinen Ausdrucken als Argument
*list*.  In diesem Fall wird dem Hauptoperator des Arguments *list* der
Ausdruck *expr* als letztes Argument hinzugefugt.


Siehe auch die Funktion `cons`, um ein Element am Anfang einer
Liste einzufugen sowie die Funktion `append`, um zwei Listen
zusammenzufugen.


Beispiele:



```maxima
(%i1) endcons(x, [a, b, c]);
(%o1)                     [a, b, c, x]
(%i2) endcons(x^2+1, [a, b, c]);
                                   2
(%o2)                   [a, b, c, x  + 1]
(%i3) endcons(x^2+1, a+b+c);
                        2
(%o3)                  x  + c + b + a + 1
(%i4) endcons(x^2+1, f(a,b,c));
                                   2
(%o4)                  f(a, b, c, x  + 1)
```

See also: `cons`, `append`.

<!-- category: Programming -->
<!-- keywords: fillarray -->
<!-- signatures: fillarray(A, B) -->
### Function: fillarray (A, B)

Fullt das Array *A* mit den Werten aus *B*.  Das Argument *B* ist 
eine Liste oder ein Array.


Hat das Array *A* einen Typ, dann kann es nur mit Elementen gefullt
werden, die den gleichen Typ haben.


Sind die Dimensionen von *A* und *B* verschieden, werden zunachst die
Zeilen des Arrays *A* aufgefullt.  Hat die Liste oder das Array *B*
nicht genugend Elemente, um das Array *A* aufzufullen, werden die 
restlichen Elemente mit dem letzten Wert von *B* aufgefullt.
Uberzahlige Elemente in *B* werden ignoriert.


`fillarray` gibt das erste Argument zuruck.


Siehe die Funktionen `array` und `make_array`, um ein Array
zu definieren.


Beispiele:


Erzeuge ein Array mit 9 Elementen und fulle es mit den Elementen einer Liste.



```maxima
(%i1) array (a1, fixnum, 8);
(%o1)                          a1


(%i2) listarray (a1);
(%o2)              [0, 0, 0, 0, 0, 0, 0, 0, 0]


(%i3) fillarray (a1, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
(%o3)                          a1


(%i4) listarray (a1);
(%o4)              [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


Sind zu wenige Elemente vorhanden, um das Array aufzufullen, wird das Array
mit dem letzten Element aufgefullt.  Uberzahlige Elemente werden 
ignoriert.



```maxima
(%i1) a2 : make_array (fixnum, 8);
(%o1)             {Array:  #(0 0 0 0 0 0 0 0)}


(%i2) fillarray (a2, [1, 2, 3, 4, 5]);
(%o2)             {Array:  #(1 2 3 4 5 5 5 5)}


(%i3) fillarray (a2, [4]);
(%o3)             {Array:  #(4 4 4 4 4 4 4 4)}


(%i4) fillarray (a2, makelist (i, i, 1, 100));
(%o4)             {Array:  #(1 2 3 4 5 6 7 8)}
```


Arrays werden zeilenweise aufgefullt.



```maxima
(%i1) a3 : make_array (fixnum, 2, 5);
(%o1)        {Array:  #2A((0 0 0 0 0) (0 0 0 0 0))}


(%i2) fillarray (a3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
(%o2)        {Array:  #2A((1 2 3 4 5) (6 7 8 9 10))}


(%i3) a4 : make_array (fixnum, 5, 2);
(%o3)     {Array:  #2A((0 0) (0 0) (0 0) (0 0) (0 0))}


(%i4) fillarray (a4, a3);
(%o4)     {Array:  #2A((1 2) (3 4) (5 6) (7 8) (9 10))}
```

See also: `array`, `make_array`.

<!-- category: Programming -->
<!-- keywords: first -->
<!-- signatures: first(list) -->
### Function: first (list)

Gibt das erste Element der Liste *list* zuruck.


Das Argument *list* kann auch ein allgemeiner Ausdruck wie zum Beispiel
der Term einer Summe, der Faktor eines Produktes oder die erste Spalte einer
Matrix sein.  Die Funktion `first` und verwandte Funktionen wie
`last` oder `rest` arbeiten mit der externen Darstellung eines
Ausdrucks, wie sie in der Anzeige erscheint.  Dies kann mit der Optionsvariablen
`inflag` kontrolliert werden.  Hat die Optionsvariable `inflag` den
Wert `true`, wird von diesen Funktionen die interne Darstellung betrachtet.


Die Funktionen `second` bis `tenth` geben jeweils das 2. bis 10. 
Element zuruck.


Beispiele:



```maxima
(%i1) l: [a,b,c];
(%o1)                       [a, b, c]
(%i2) first(l);
(%o2)                           a
(%i3) first(x + y);
(%o3)                           y
(%i4) first(x * y);
(%o4)                           x
(%i5) first(f(x, y, z));
(%o5)                           x
```

See also: `last`, `rest`, `inflag`, `second`, `tenth`.

<!-- category: Programming -->
<!-- keywords: join -->
<!-- signatures: join(list_1, list_2) -->
### Function: join (list_1, list_2)

Erzeugt eine neue Liste aus den Elementen der Listen *list_1* und
*list_2*, wobei die Elemente abwechselnd ubernommen werden.  Das Ergebnis
hat die Form `[list_1[1], list_2[1], list_1[2], list_2[2], ...]`.


Haben die Listen verschiedene Langen, werden die zusatzlichen Elemente der
langeren Liste ignoriert.


Sind *list_1* oder *list_2* keine Listen, gibt Maxima einen Fehler aus.


Beispiele:



```maxima
(%i1) L1: [a, sin(b), c!, d - 1];
(%o1)                [a, sin(b), c!, d - 1]
(%i2) join (L1, [1, 2, 3, 4]);
(%o2)          [a, 1, sin(b), 2, c!, 3, d - 1, 4]
(%i3) join (L1, [aa, bb, cc, dd, ee, ff]);
(%o3)        [a, aa, sin(b), bb, c!, cc, d - 1, dd]
```

<!-- category: Programming -->
<!-- keywords: last -->
<!-- signatures: last(list) -->
### Function: last (list)

Gibt das letzte Element der Liste *list* zuruck.


Das Argument *list* kann auch ein allgemeiner Ausdruck sein.  Siehe
`first` fur weitere Erlauterungen.


Beispiele:



```maxima
(%i1) l: [a,b,c];
(%o1)                       [a, b, c]
(%i2) last(x + y);
(%o2)                           x
(%i3) last(x * y);
(%o3)                           y
(%i4) last(f(x, y, z));
(%o4)                           z
```

See also: `first`.

<!-- category: Programming -->
<!-- keywords: length -->
<!-- signatures: length(list) -->
### Function: length (list)

Gibt die Anzahl der Elemente der Liste *list* zuruck.


Das Argument *list* kann auch ein allgemeiner Ausdruck sein.  Wie bei
anderen Funktionen fur Listen wird auch von der Funktion `length` die
externe Darstellung eines Ausdrucks betrachtet, wie sie fur die Ausgabe
vorliegt.  Die Optionsvariable `inflag` hat daher Einfluss auf das Ergebnis
der Funktion `length`.


Beispiele:



```maxima
(%i1) length([a, x^2, sin(x), y+3]);
(%o1)                           4
(%i2) length(a/(b*x));
(%o2)                           2
(%i3) length(a/(b*x)),inflag:true;
(%o3)                           3
```

See also: `inflag`.

<!-- category: Programming -->
<!-- keywords: listarith -->
<!-- signatures: listarith -->
### Variable: listarith

Standardwert: `true`


Hat die Optionsvariable `listarith` den Wert `true`, werden 
Rechenoperationen mit Matrizen und Listen elementweise ausgefuhrt.  Das 
Ergebnis von Rechnungen mit Listen und Matrizen sind wieder Listen und Matrizen.
Hat die Optionsvariable `listarith` den Wert `false`, wird die
elementweise Ausfuhrung der Rechenoperationen unterdruckt.


Beispiele:



```maxima
(%i1) listarith: true;
(%o1)                         true
(%i2) 2 + [a, b, c];
(%o2)                 [a + 2, b + 2, c + 2]
(%i3) 2^[a, b, c];
                            a   b   c
(%o3)                     [2 , 2 , 2 ]
(%i4) [1, 2, 3] + [a, b, c];
(%o4)                 [a + 1, b + 2, c + 3]
(%i5) listarith: false;
(%o5)                         false
(%i6) 2 + [a, b, c];
(%o6)                     [a, b, c] + 2
(%i7) 2^[a, b, c];
                            [a, b, c]
(%o7)                      2
(%i8) [1, 2, 3] + [a, b, c];
(%o8)                 [a, b, c] + [1, 2, 3]
```

<!-- category: Programming -->
<!-- keywords: listarray -->
<!-- signatures: listarray(A) -->
### Function: listarray (A)

Gibt eine Liste mit den Elementen des Arrays *A* zuruck.  Das Argument 
*A* kann ein deklariertes, nicht-deklariertes, eine Array-Funktion oder eine
indizierte Funktion sein.


Die Elemente werden zeilenweise ausgegeben.  Fur nicht-deklarierte Arrays mit
Indizes, die keine ganze Zahlen sind, wird die Sortierung von der
Aussagefunktion `orderlessp` bestimmt.


Fur nicht-deklarierte Arrays, Array-Funktionen und indizierte Funktionen
werden die Elemente in der Reihenfolge wie von der Funktion 
`arrayinfo` zuruckgegeben.


Elemente von deklarierten Arrays, denen noch kein Wert zugewiesen wurde und die
keinen Typ haben, werden als `#####` zuruckgegeben.  Elemente von
deklarierten Arrays mit einem Typ, geben den Wert 0 fur den Typ `fixnum`
und 0.0 fur den Typ `flonum` zuruck.


Ist das Argument *A* ein Lisp-Array, wie es von der Funktion
`make_array` erzeugt wird, generiert Maxima einen Lisp-Fehler.  Das ist ein
Programmfehler.


Beispiele:


Anwendung der Funktionen `listarray` und `arrayinfo` fur ein
deklariertes Array.



```maxima
(%i1) array (aa, 2, 3);
(%o1)                          aa


(%i2) aa [2, 3] : %pi;
(%o2)                          %pi


(%i3) aa [1, 2] : %e;
(%o3)                          %e


(%i4) listarray (aa);
(%o4) [#####, #####, #####, #####, #####, #####, %e, #####, 
                                        #####, #####, #####, %pi]


(%i5) arrayinfo (aa);
(%o5)                 [declared, 2, [2, 3]]
```


Anwendung der Funktionen `listarray` und `arrayinfo` fur ein
nicht-deklariertes Array.



```maxima
(%i1) bb [FOO] : (a + b)^2;
                                   2
(%o1)                       (b + a)


(%i2) bb [BAR] : (c - d)^3;
                                   3
(%o2)                       (c - d)


(%i3) listarray (bb);
                              3         2
(%o3)                 [(c - d) , (b + a) ]


(%i4) arrayinfo (bb);
(%o4)               [hashed, 1, [BAR], [FOO]]
```


Anwendung der Funktionen `listarray` und `arrayinfo` fur eine
Array-Funktion.



```maxima
(%i1) cc [x, y] := y / x;
                                     y
(%o1)                      cc     := -
                             x, y    x


(%i2) cc [u, v];
                                v
(%o2)                           -
                                u


(%i3) cc [4, z];
                                z
(%o3)                           -
                                4


(%i4) listarray (cc);
                              z  v
(%o4)                        [-, -]
                              4  u


(%i5) arrayinfo (cc);
(%o5)              [hashed, 2, [4, z], [u, v]]
```


Anwendung der Funktionen `listarray` und `arrayinfo` fur ein
indizierte Funktion.



```maxima
(%i1) dd [x] (y) := y ^ x;
                                     x
(%o1)                     dd (y) := y
                            x


(%i2) dd [a + b];
                                    b + a
(%o2)                  lambda([y], y     )


(%i3) dd [v - u];
                                    v - u
(%o3)                  lambda([y], y     )


(%i4) listarray (dd);
                         b + a                v - u
(%o4)      [lambda([y], y     ), lambda([y], y     )]


(%i5) arrayinfo (dd);
(%o5)             [hashed, 1, [b + a], [v - u]]
```

See also: `orderlessp`, `arrayinfo`, `make_array`.

<!-- category: Programming -->
<!-- keywords: listp -->
<!-- signatures: listp(expr) -->
### Function: listp (expr)

Gibt `true` zuruck, wenn *expr* eine Liste ist.  Ansonsten ist der 
Ruckgabewert `false`.

<!-- category: Programming -->
<!-- keywords: make_array -->
<!-- signatures: make_array(type, dim_1, ..., dim_n) -->
### Function: make_array (type, dim_1, ..., dim_n)

Gibt ein Lisp-Array zuruck.  Das Argument *type* kann die Werte
`any`, `flonum`, `fixnum` oder `hashed` haben.  Das Array
hat $i$ Dimensionen und der Index $i$ lauft von 0 bis 
einschließlich $dim_i-1$.




Die meisten Funktionen, die auf ein Array angewendet werden konnen, das mit
der Funktion `array` definiert wurde, konnen auch auf Lisp-Arrays
angewendet werden.  Einige Funktionalitaten stehen jedoch nicht zur
Verfugung.  Dies ist auf eine unzureichende Implementation der Lisp-Arrays
zuruckzufuhren und kann als Programmfehler betrachtet werden.  Hinweise auf
Einschrankungen sind bei den einzelnen Funktionen fur Arrays zu finden.


Erhalt die Optionsvariable `use_fast_arrays` den Wert `true`,
erzeugt Maxima ausschließlich Lisp-Arrays.  Dies trifft auch auf die
Funktion `array` zu.  Wie bereits oben erlautert, ist in diesem Fall
jedoch mit einer eingeschrankten Funktionalitat zu rechnen.


Beispiele:



```maxima
(%i1) A1 : make_array (fixnum, 10);
(%o1)           {Array:  #(0 0 0 0 0 0 0 0 0 0)}


(%i2) A1 [8] : 1729;
(%o2)                         1729


(%i3) A1;
(%o3)          {Array:  #(0 0 0 0 0 0 0 0 1729 0)}


(%i4) A2 : make_array (flonum, 10);
(%o4) {Array:  #(0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}


(%i5) A2 [2] : 2.718281828;
(%o5)                      2.718281828


(%i6) A2;
(%o6) 
     {Array:  #(0.0 0.0 2.718281828 0.0 0.0 0.0 0.0 0.0 0.0 0.0)}


(%i7) A3 : make_array (any, 10);
(%o7) {Array:  #(NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL)}


(%i8) A3 [4] : x - y - z;
(%o8)                      - z - y + x


(%i9) A3;
(%o9) {Array:  #(NIL NIL NIL NIL ((MPLUS SIMP) $X ((MTIMES SIMP)\
 -1 $Y) ((MTIMES SIMP) -1 $Z))
  NIL NIL NIL NIL NIL)}


(%i10) A4 : make_array (fixnum, 2, 3, 5);
(%o10) {Array:  #3A(((0 0 0 0 0) (0 0 0 0 0) (0 0 0 0 0)) ((0 0 \
0 0 0) (0 0 0 0 0) (0 0 0 0 0)))}


(%i11) fillarray (A4, makelist (i, i, 1, 2*3*5));
(%o11) {Array:  #3A(((1 2 3 4 5) (6 7 8 9 10) (11 12 13 14 15))
    ((16 17 18 19 20) (21 22 23 24 25) (26 27 28 29 30)))}


(%i12) A4 [0, 2, 1];
(%o12)                         12
```

See also: `array`, `use_fast_arrays`.

<!-- category: Programming -->
<!-- keywords: makelist -->
<!-- signatures: makelist(expr, i, i_0, i_1), makelist(expr, x, list) -->
### Function: makelist (expr, i, i_0, i_1)

Erzeugt eine Liste, indem der Ausdruck *expr* fur die Variable *i*
ausgewertet wird.  Die Variable *i* nimmt nacheinander die Werte von
*i_0* bis *i_1* an, wobei die Schrittweite 1 ist.  Alternativ kann eine
Liste *list* als Argument ubergeben werden.  In diesem Fall nimmt die
Variable *i* nacheinander die Werte der Liste *list* an.


Siehe auch die Funktion `create_list`, um eine Liste zu generieren.


Beispiele:



```maxima
(%i1) makelist(concat(x, i), i, 1, 6);
(%o1)               [x1, x2, x3, x4, x5, x6]
(%i2) makelist(x = y, y, [a, b, c]);
(%o2)                 [x = a, x = b, x = c]
```

See also: `create_list`.

<!-- category: Programming -->
<!-- keywords: member -->
<!-- signatures: member(expr, list) -->
### Function: member (expr, list)

Gibt `true` zuruck, wenn der Ausdruck *expr* gleich einem Element in
der Liste *list* ist.  Die Gleichheit wird dem Operator
`=` festgestellt.


Die Gleichheit wird mit dem Operator `=` gepruft.  Daher werden nur
Ausdrucke als gleich erkannt, die syntaktisch ubereinstimmen.  Aquivalente
Ausdrucke, die syntaktisch voneinander verschieden sind, werden nicht aus der
Liste entfernt.  Zum Beispiel sind die Ausdrucke `x^2-1` und
`(x+1)*(x-1)` aquivalent, aber syntaktisch verschieden.


Das Argument *list* kann auch ein allgemeiner Ausdruck sein.  Dabei werden
die Argumente des Hauptoperators betrachtet.


Siehe auch die Funktion `elementp`.


Beispiele:



```maxima
(%i1) member (8, [8, 8.0, 8b0]);
(%o1)                         true
(%i2) member (8, [8.0, 8b0]);
(%o2)                         false
(%i3) member (b, [a, b, c]);
(%o3)                         true
(%i4) member (b, [[a, b], [b, c]]);
(%o4)                         false
(%i5) member ([b, c], [[a, b], [b, c]]);
(%o5)                         true
(%i6) F (1, 1/2, 1/4, 1/8);
                               1  1  1
(%o6)                     F(1, -, -, -)
                               2  4  8
(%i7) member (1/8, %);
(%o7)                         true
(%i8) member ("ab", ["aa", "ab", sin(1), a + b]);
(%o8)                         true
```

See also: `=`, `elementp`.

<!-- category: Programming -->
<!-- keywords: pop -->
<!-- signatures: pop(list) -->
### Function: pop (list)

Die Funktion `pop` entfernt das erste Element der Liste *list* und
gibt dieses Element zuruck.  *list* muss ein Symbol sein, dem eine Liste
zugewiesen wurde, und kann nicht selbst eine Liste sein.


Ist dem Argument *list* keine Liste zugewiesen, gibt Maxima eine
Fehlermeldung aus.


Siehe auch die Funktion `push` fur Beispiele.


Mit dem Kommando `load("basic")` wird die Funktion geladen.

See also: `push`.

<!-- category: Programming -->
<!-- keywords: push -->
<!-- signatures: push(item, list) -->
### Function: push (item, list)

Die Funktion `push` fugt das Argument *item* als erstes Element der
Liste *list* hinzu und gibt die neue Liste zuruck.  Das Argument
*list* muss ein Symbol sein, dem eine Liste zugewiesen wurde, und kann nicht
selbst eine Liste sein.  Das Argument *item* kann ein beliebiger Ausdruck
sein.


Ist dem Argument *list* keine Liste zugewiesen, gibt Maxima eine 
Fehlermeldung aus.


Siehe auch die Funktion `pop`, um das erste Element einer Liste zu
entfernen.


Mit dem Kommando `load("basic")` wird die Funktion geladen.


Beispiele:



```maxima
(%i1) ll:[];
(%o1)                          []
(%i2) push(x,ll);
(%o2)                          [x]
(%i3) push(x^2+y,ll);
                                 2
(%o3)                      [y + x , x]
(%i4) a:push("string",ll);
                                     2
(%o4)                  [string, y + x , x]
(%i5) pop(ll);
(%o5)                        string
(%i6) pop(ll);
                                  2
(%o6)                        y + x
(%i7) pop(ll);
(%o7)                           x
(%i8) ll;
(%o8)                          []
(%i9) a;
                                     2
(%o9)                  [string, y + x , x]
```

See also: `pop`.

<!-- category: Programming -->
<!-- keywords: rearray -->
<!-- signatures: rearray(A, dim_1, ..., dim_n) -->
### Function: rearray (A, dim_1, ..., dim_n)

Die Funktion `rearray` erlaubt es, ein Array *A* zu vergroßern
oder auch zu verkleinern.  Die Anzahl der Dimensionen *n* sowie der Typ
eines Arrays konnen nicht geandert werden.


Das neue Array wird zeilenweise mit den Werten des alten Arrays aufgefullt.
Hat das alte Array nicht genugend Elemente werden die restlichen Elemente
entsprechend dem Typ des Arrays mit `false`, `0.0` oder `0`
aufgefullt.


Siehe die Funktionen `array` und `make_array`, um ein Array
zu definieren.


Beispiel:


In diesem Beispiel wird das Array `A` verkleinert.  Der Ruckgabewert von
`rearray` ist ein internes Lisp-Array auch fur den Fall, dass das Array
selbst kein Lisp-Array ist.



```maxima
(%i1) array(A, fixnum, 2, 2);
(%o1)                           A
(%i2) listarray(A);
(%o2)              [0, 0, 0, 0, 0, 0, 0, 0, 0]
(%i3) rearray(A, 1, 1);
(%o3)              {Array:  #2A((0 0) (0 0))}
(%i4) listarray(A);
(%o4)                     [0, 0, 0, 0]
```

See also: `array`, `make_array`.

<!-- category: Programming -->
<!-- keywords: remarray -->
<!-- signatures: remarray(A_1, ..., A_n), remarray(all) -->
### Function: remarray (A_1, ..., A_n)

Entfernt Arrays und Array-Funktionen.  Der vom Array belegte Speicher wird
freigegeben.  Die Argumente konnen deklarierte und nicht-deklarierte Arrays
sowie Array-Funktionen und indizierte Funktionen sein.


`remarray(all)` entfernt alle Arrays, die in der Informationsliste
`arrays` enthalten sind.


`remarray` gibt eine Liste der Arrays zuruck, die entfernt wurden.
`remarray` wertet die Argumente nicht aus.

See also: `arrays`.

<!-- category: Programming -->
<!-- keywords: rest -->
<!-- signatures: rest(list, n), rest(list) -->
### Function: rest (list, n)

Entfernt das erste Element oder, wenn *n* eine positive ganze Zahl ist, die
ersten *n* Elemente der Liste *list* und gibt den Rest der Liste als
Ergebnis zuruck.  Ist *n* eine negative Zahl, werden die letzten *n*
Elemente von der Liste entfernt und der Rest als Ergebnis zuruckgegeben.


Das Argument *list* kann auch ein allgemeiner Ausdruck sein.


Siehe auch die Funktionen `first` und `last`.


Beispiele:



```maxima
(%i1) rest([a,b,c]);
(%o1)                        [b, c]
(%i2) rest(a+b+c);
(%o2)                         b + a
```

See also: `first`, `last`.

<!-- category: Programming -->
<!-- keywords: reverse -->
<!-- signatures: reverse(list) -->
### Function: reverse (list)

Kehrt die Anordnung der Elemente einer Liste *list* um und gibt die
Ergebnisliste zuruck.  Das Argument *list* kann auch ein allgemeiner
Ausdruck sein.


Beispiele:



```maxima
(%i1) reverse([a, b, c]);
(%o1)                       [c, b, a]
(%i2) reverse(sin(x)=2*x^2+1);
                           2
(%o2)                   2 x  + 1 = sin(x)
```

<!-- category: Programming -->
<!-- keywords: second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth -->
<!-- signatures: second(list), third(list), fourth(list), fifth(list), sixth(list), seventh(list), eighth(list), ninth(list), tenth(list) -->
### Function: second (list)

Die Funktionen `second` bis `tenth` geben das 2. bis 10. Element eines
Ausdrucks oder einer Liste *list* zuruck.  Siehe `first`.

See also: `first`.

<!-- category: Programming -->
<!-- keywords: sort -->
<!-- signatures: sort(L, P), sort(L) -->
### Function: sort (L, P)

Sortiert eine Liste *L* und gibt die sortierte Liste zuruck.  Das
optionale Argument *P* ist eine Aussagefunktion mit zwei Argumenten, die
eine Ordnung der Elemente definiert.  Die Aussagefunktion kann eine Funktion,
ein binarer Operator oder ein Lambda-Ausdruck sein.  Wird kein Argument
*P* angegeben, werden die Elemente der Liste mit der Aussagefunktion
`orderlessp` geordnet.


Die Aussagefunktion `orderlessp` sortiert eine List aufsteigend.  Mit der
Aussagefunktion `ordergreatp` kann die Liste absteigend sortiert werden.
Die Aussagefunktion `ordermagnitudep` sortiert Maxima Zahlen, Konstante 
oder Ausdrucke, die zu einer Zahl oder Konstanten ausgewertet werden konnen,
nach der Große.  Mit dem Operator `<` kann auch nach der Große
sortiert werden.  Im Unterschied zur Aussagefunktion `ordermagnitudep` ist
die Ordnung nicht vollstandig, wenn einzelne Elemente der Liste nicht
vergleichbar unter dem Operator `<` sind.


Beispiele:



```maxima
(%i1) sort ([11, -17, 29b0, 7.55, 3, -5/2, b + a, 9 * c,
      19 - 3 * x]);
               5
(%o1) [- 17, - -, 3, 7.55, 11, 2.9b1, b + a, 9 c, 19 - 3 x]
               2
(%i2) sort ([11, -17, 29b0, 7.55, 3, -5/2, b + a, 9*c, 19 - 3*x],
      ordergreatp);
                                                   5
(%o2) [19 - 3 x, 9 c, b + a, 2.9b1, 11, 7.55, 3, - -, - 17]
                                                   2
(%i3) sort ([%pi, 3, 4, %e, %gamma]);
(%o3)                [3, 4, %e, %gamma, %pi]
(%i4) sort ([%pi, 3, 4, %e, %gamma], "<");
(%o4)                [%gamma, %e, 3, %pi, 4]
(%i5) my_list: [[aa,hh,uu], [ee,cc], [zz,xx,mm,cc], [%pi,%e]];
(%o5) [[aa, hh, uu], [ee, cc], [zz, xx, mm, cc], [%pi, %e]]
(%i6) sort (my_list);
(%o6) [[%pi, %e], [aa, hh, uu], [ee, cc], [zz, xx, mm, cc]]
(%i7) sort (my_list, lambda ([a, b], orderlessp (reverse (a),
      reverse (b))));
(%o7) [[%pi, %e], [ee, cc], [zz, xx, mm, cc], [aa, hh, uu]]
```


Ordne Maxima Zahlen, Konstante und konstante Ausdrucke nach der Große.
Alle anderen Elemente werden aufsteigend sortiert.



```maxima
(%i8) sort([%i,1+%i,2*x,minf,inf,%e,sin(1),0,1,2,3,1.0,1.0b0],
           ordermagnitudep);

(%o8) [minf, 0, sin(1), 1, 1.0, 1.0b0, 2, %e, 3, inf, %i, 
                                                     %i + 1, 2 x]
```

See also: `orderlessp`, `ordergreatp`, `ordermagnitudep`, `<`.

<!-- category: Programming -->
<!-- keywords: sublist -->
<!-- signatures: sublist(L, P) -->
### Function: sublist (L, P)

Gibt die Elemente der Liste *L* als eine Liste zuruck, fur die die
Aussagefunktion `P` das Ergebnis `true` hat.  `P` ist eine
Funktion mit einem Argument wie zum Beispiel die Funktion
`integerp`.  Siehe auch die Funktion `sublist_indices`.


Beispiele:



```maxima
(%i1) L: [1, 2, 3, 4, 5, 6];
(%o1)                  [1, 2, 3, 4, 5, 6]
(%i2) sublist (L, evenp);
(%o2)                       [2, 4, 6]
```

See also: `integerp`, `sublist_indices`.

<!-- category: Programming -->
<!-- keywords: sublist_indices -->
<!-- signatures: sublist_indices(L, P) -->
### Function: sublist_indices (L, P)

Gibt die Indizes der Elemente der Liste *L* zuruck, fur die die
Aussagefunktion `P` das Ergebnis `true` hat.  `P` ist eine
Funktion mit einem Argument wie zum Beispiel die Funktion
`integerp`.  Siehe auch die Funktion `sublist`.


Beispiele:



```maxima
(%i1) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b],
                       lambda ([x], x='b));
(%o1)                     [2, 3, 7, 9]
(%i2) sublist_indices ('[a, b, b, c, 1, 2, b, 3, b], symbolp);
(%o2)                  [1, 2, 3, 4, 7, 9]
(%i3) sublist_indices ([1 > 0, 1 < 0, 2 < 1, 2 > 1, 2 > 0],
                       identity);
(%o3)                       [1, 4, 5]
(%i4) assume (x < -1);
(%o4)                       [x < - 1]
(%i5) map (maybe, [x > 0, x < 0, x < -2]);
(%o5)                [false, true, unknown]
(%i6) sublist_indices ([x > 0, x < 0, x < -2], identity);
(%o6)                          [2]
```

See also: `integerp`, `sublist`.

<!-- category: Programming -->
<!-- keywords: subvar -->
<!-- signatures: subvar(x, i_1, x_2, ...) -->
### Function: subvar (x, i_1, x_2, ...)

Wertet den indizierten Ausdruck `x[i_1, i_2, ...]` aus.
`subvar` wertet die Argumente aus.


Siehe die Funktion `arrayapply`, die dieselbe Funktionalitat hat, und
die Funktion `arraymake`, die eine Referenz auf das Array-Element
zuruckgibt, ohne diese auszuwerten.


Beispiele:



```maxima
(%i1) x : foo $
(%i2) i : 3 $

(%i3) subvar (x, i);
(%o3)                         foo
                                 3

(%i4) foo : [aa, bb, cc, dd, ee]$

(%i5) subvar (x, i);
(%o5)                          cc


(%i6) arraymake (x, [i]);
(%o6)                         foo
                                 3


(%i7) ''%;
(%o7)                          cc
```

See also: `arrayapply`, `arraymake`.

<!-- category: Programming -->
<!-- keywords: subvarp -->
<!-- signatures: subvarp(expr) -->
### Function: subvarp (expr)

Gibt `true` zuruck, wenn *expr* eine indizierte Variable wie zum
Beispiel `a[i]` ist.

<!-- category: Programming -->
<!-- keywords: unique -->
<!-- signatures: unique(L) -->
### Function: unique (L)

Gibt eine Liste mit den Elementen der Liste *L* zuruck, die sich
voneinander unterscheiden.  Sind alle Elemente der Liste *L* verschieden,
gibt `unique` eine Kopie der Liste *L* und nicht die Liste selbst
zuruck.  Ist *L* keine Liste, gibt `unique` den Ausdruck *L*
zuruck.


Beispiel:



```maxima
(%i1) unique ([1, %pi, a + b, 2, 1, %e, %pi, a + b, [1]]);
(%o1)              [1, 2, %e, %pi, [1], b + a]
```

<!-- category: Programming -->
<!-- keywords: use_fast_arrays -->
<!-- signatures: use_fast_arrays -->
### Variable: use_fast_arrays

Standardwert: `false`


Erhalt die Optionsvariable `use_fast_arrays` den Wert `true`,
erzeugt Maxima ausschließlich Lisp-Arrays, wie sie auch von der Funktion
`make_array` erzeugt werden.  Dies trifft auch auf die Funktion 
`array` zu.  Der Vorteil der Lisp-Arrays ist, dass diese effizienter sind.


Die Implementation der Lisp-Arrays ist jedoch nicht vollstandig ausgefuhrt,
so dass es zu einer eingeschrankten Funktionalitat kommt.  Dies ist ein 
Programmfehler.  Hinweise auf einzelne Einschrankungen sind bei den einzelnen
Funktionen zu finden.


Siehe die Funktion `make_array` fur weitere Ausfuhrungen zu
Lisp-Arrays.

See also: `use_fast_arrays`, `make_array`, `array`.

